const fs = require("fs");
const path = require("path");
const { WebSocket } = require("ws");
const crypto = require("crypto");

const baseUrl = "speech.platform.bing.com/consumer/speech/synthesize/readaloud";
const token = "6A5AA1D4EAFF4E9FB37E23D68491D6F4";
const webSocketURL = `wss://${baseUrl}/edge/v1?TrustedClientToken=${token}`;

const voice = process.env.TTS_VOICE || "en-US-JennyMultilingualNeural";

function uuid() {
  return crypto.randomUUID().replaceAll("-", "");
}

function patchSsml(content) {
  const trimmed = content.trim();
  const openTag = `<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>`;
  if (trimmed.startsWith("<speak")) {
    return trimmed
      .replace("<speak>", `${openTag}<voice name='${voice}'>`)
      .replace("</speak>", `</voice></speak>`);
  }
  return `${openTag}<voice name='${voice}'>${trimmed}</voice></speak>`;
}

async function synthesize(ssml, outputPath) {
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
          fs.writeFileSync(outputPath, Buffer.concat(audioData));
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

    const speechConfig = JSON.stringify({
      context: {
        synthesis: {
          audio: {
            metadataoptions: { sentenceBoundaryEnabled: false, wordBoundaryEnabled: false },
            outputFormat: "audio-24khz-48kbitrate-mono-mp3"
          }
        }
      }
    });
    const configMessage = `X-Timestamp:${Date()}\r\nContent-Type:application/json; charset=utf-8\r\nPath:speech.config\r\n\r\n${speechConfig}`;

    ws.on("open", () => {
      ws.send(configMessage, { compress: true }, (configError) => {
        if (configError) reject(configError);
        const ssmlMessage =
          `X-RequestId:${uuid()}\r\nContent-Type:application/ssml+xml\r\n` +
          `X-Timestamp:${Date()}Z\r\nPath:ssml\r\n\r\n` +
          ssml;
        ws.send(ssmlMessage, { compress: true }, (ssmlError) => {
          if (ssmlError) reject(ssmlError);
        });
      });
    });
  });
}

async function run() {
  const jobs = [
    { src: "training/shared/tts", dest: "training/shared/audio" },
    { src: "training/pega-poland/tts", dest: "training/pega-poland/audio" }
  ];

  for (const job of jobs) {
    const files = fs.readdirSync(job.src).filter((f) => f.endsWith(".ssml"));
    for (const file of files) {
      const ssmlPath = path.join(job.src, file);
      const outPath = path.join(job.dest, path.parse(file).name + ".mp3");
      const content = fs.readFileSync(ssmlPath, "utf8");
      const patched = patchSsml(content);
      console.log(`Synthesizing ${ssmlPath} -> ${outPath}`);
      await synthesize(patched, outPath);
    }
  }
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
