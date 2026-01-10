const fs = require("fs");
const path = require("path");
const os = require("os");
const { spawn } = require("child_process");
const { WebSocket } = require("ws");
const crypto = require("crypto");
let speechsdk = null;
try { speechsdk = require("microsoft-cognitiveservices-speech-sdk"); } catch (e) { speechsdk = null; }

const ffmpegPath = require("ffmpeg-static");
const logPath = path.join("tools", "logs", "tts-online.log");
const chunkLimit = 3000;
const defaultVoice = "en-US-JennyNeural";

function log(line) {
  const stamp = new Date().toISOString();
  fs.appendFileSync(logPath, `${stamp} ${line}\r\n`, "utf8");
}

function readSSMLFiles(dir) {
  return fs.readdirSync(dir).filter((f) => f.endsWith(".ssml"));
}

function extractVoice(ssml) {
  const m = ssml.match(/<voice[^>]*name=['"]([^'"<>]+)['"]/i);
  return m ? m[1] : defaultVoice;
}

function extractProsody(ssml) {
  const rateMatch = ssml.match(/rate=['"]([^'"<>]+)['"]/i);
  const pitchMatch = ssml.match(/pitch=['"]([^'"<>]+)['"]/i);
  return { rate: rateMatch ? rateMatch[1] : null, pitch: pitchMatch ? pitchMatch[1] : null };
}

function ssmlToPlainText(ssml) {
  return ssml.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
}

function chunkText(text) {
  const chunks = [];
  let remaining = text;
  while (remaining.length > chunkLimit) {
    let cut = remaining.lastIndexOf(" ", chunkLimit);
    if (cut <= 0) cut = chunkLimit;
    chunks.push(remaining.slice(0, cut).trim());
    remaining = remaining.slice(cut).trim();
  }
  if (remaining.length) chunks.push(remaining);
  return chunks;
}

function buildChunkSsml(chunk, voice, prosody) {
  const open = `<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'><voice name='${voice}'>`;
  const close = `</voice></speak>`;
  if (prosody.rate || prosody.pitch) {
    const rateAttr = prosody.rate ? ` rate='${prosody.rate}'` : "";
    const pitchAttr = prosody.pitch ? ` pitch='${prosody.pitch}'` : "";
    return `${open}<prosody${rateAttr}${pitchAttr}>${chunk}</prosody>${close}`;
  }
  return `${open}${chunk}${close}`;
}

function concatMp3(files, output) {
  const listFile = path.join(os.tmpdir(), `tts-${crypto.randomUUID()}.txt`);
  fs.writeFileSync(listFile, files.map(f => `file '${f.replace(/'/g, "'\\''")}'`).join("\n"));
  return new Promise((resolve, reject) => {
    const ff = spawn(ffmpegPath, ["-y", "-f", "concat", "-safe", "0", "-i", listFile, "-c", "copy", output]);
    ff.stderr.on("data", () => {});
    ff.on("close", (code) => {
      fs.unlinkSync(listFile);
      if (code === 0) resolve(); else reject(new Error(`ffmpeg concat failed code ${code}`));
    });
  });
}

async function synthesizeEdge(ssml, outPath) {
  const baseUrl = "speech.platform.bing.com/consumer/speech/synthesize/readaloud";
  const token = "6A5AA1D4EAFF4E9FB37E23D68491D6F4";
  const webSocketURL = `wss://${baseUrl}/edge/v1?TrustedClientToken=${token}`;
  const uuid = () => crypto.randomUUID().replaceAll("-", "");
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(`${webSocketURL}&ConnectionId=${uuid()}`, {
      host: "speech.platform.bing.com",
      origin: "chrome-extension://jdiccldimpdaibmpdkjnbmckianbfold",
      headers: {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
      }
    });
    const audioData = [];
    ws.on("message", (rawData, isBinary) => {
      if (!isBinary) {
        const data = rawData.toString("utf8");
        if (data.includes("turn.end")) {
          fs.writeFileSync(outPath, Buffer.concat(audioData));
          ws.close();
          resolve();
        }
        return;
      }
      const separator = "Path:audio\r\n";
      const content = rawData.subarray(rawData.indexOf(separator) + separator.length);
      audioData.push(content);
    });
    ws.on("error", reject);
    const speechConfig = JSON.stringify({ context: { synthesis: { audio: { metadataoptions: { sentenceBoundaryEnabled: false, wordBoundaryEnabled: false }, outputFormat: "audio-24khz-48kbitrate-mono-mp3" } } } });
    const configMessage = `X-Timestamp:${Date()}\r\nContent-Type:application/json; charset=utf-8\r\nPath:speech.config\r\n\r\n${speechConfig}`;
    ws.on("open", () => {
      ws.send(configMessage, { compress: true }, (configError) => {
        if (configError) reject(configError);
        const ssmlMessage =
          `X-RequestId:${uuid()}\r\nContent-Type:application/ssml+xml\r\n` +
          `X-Timestamp:${Date()}Z\r\nPath:ssml\r\n\r\n` + ssml;
        ws.send(ssmlMessage, { compress: true }, (ssmlError) => {
          if (ssmlError) reject(ssmlError);
        });
      });
    });
  });
}

async function synthesizeAzure(ssml, outPath, voice) {
  if (!speechsdk) throw new Error("speechsdk not installed");
  const key = process.env.AZURE_SPEECH_KEY;
  const region = process.env.AZURE_SPEECH_REGION;
  if (!key || !region) throw new Error("AZURE env missing");
  return new Promise((resolve, reject) => {
    const speechConfig = speechsdk.SpeechConfig.fromSubscription(key, region);
    speechConfig.speechSynthesisVoiceName = voice || defaultVoice;
    const audioConfig = speechsdk.AudioConfig.fromAudioFileOutput(outPath);
    const synthesizer = new speechsdk.SpeechSynthesizer(speechConfig, audioConfig);
    synthesizer.speakSsmlAsync(ssml, result => {
      synthesizer.close();
      if (result.reason === speechsdk.ResultReason.SynthesizingAudioCompleted) resolve();
      else reject(new Error(result.errorDetails || "Azure synthesis failed"));
    }, err => { synthesizer.close(); reject(err); });
  });
}

async function synthesizeChunk(ssml, outPath, preferAzure) {
  const backoffs = [2000, 4000, 8000];
  const service = preferAzure ? "azure" : "edge";
  for (let attempt = 0; attempt < backoffs.length; attempt++) {
    try {
      if (service === "azure") {
        await synthesizeAzure(ssml, outPath);
      } else {
        await synthesizeEdge(ssml, outPath);
      }
      return { ok: true, service };
    } catch (err) {
      const code = err && err.message ? err.message : String(err);
      log(`chunk fail service=${service} attempt=${attempt + 1} err=${code}`);
      if (attempt < backoffs.length - 1) await new Promise(r => setTimeout(r, backoffs[attempt]));
    }
  }
  return { ok: false, service: preferAzure ? "azure" : "edge" };
}

async function processFile(ssmlDir, audioDir, file) {
  const ssmlPath = path.join(ssmlDir, file);
  const outPath = path.join(audioDir, path.parse(file).name + ".mp3");
  const content = fs.readFileSync(ssmlPath, "utf8");
  const voice = extractVoice(content);
  const prosody = extractProsody(content);
  const text = ssmlToPlainText(content);
  const chunks = chunkText(text);
  const preferAzure = !!(process.env.AZURE_SPEECH_KEY && process.env.AZURE_SPEECH_REGION && speechsdk);
  log(`start file=${ssmlPath} chunks=${chunks.length} service=${preferAzure ? "azure" : "edge"}`);
  const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), "tts-online-"));
  const chunkFiles = [];
  let allOk = true;
  for (let i = 0; i < chunks.length; i++) {
    const chunkSsml = buildChunkSsml(chunks[i], voice, prosody);
    const chunkOut = path.join(tempDir, `chunk-${i}.mp3`);
    const res = await synthesizeChunk(chunkSsml, chunkOut, preferAzure);
    if (!res.ok) { allOk = false; break; }
    chunkFiles.push(chunkOut);
  }
  if (allOk && chunkFiles.length) {
    await concatMp3(chunkFiles, outPath);
    log(`success file=${ssmlPath} output=${outPath} chunks=${chunkFiles.length}`);
  } else {
    log(`failed file=${ssmlPath}`);
  }
  chunkFiles.forEach(f => { if (fs.existsSync(f)) fs.unlinkSync(f); });
  if (fs.existsSync(tempDir)) fs.rmdirSync(tempDir);
}

async function main() {
  const jobs = [
    { src: "training/shared/tts", dest: "training/shared/audio-online" },
    { src: "training/pega-poland/tts", dest: "training/pega-poland/audio-online" }
  ];
  for (const job of jobs) {
    const files = readSSMLFiles(job.src);
    for (const f of files) {
      try {
        await processFile(job.src, job.dest, f);
      } catch (err) {
        log(`error file=${path.join(job.src, f)} err=${err && err.message ? err.message : err}`);
      }
    }
  }
}

main().catch((err) => {
  log(`fatal ${err && err.message ? err.message : err}`);
  process.exit(1);
});
