const fs = require("fs");
const path = require("path");
const os = require("os");
const { spawn } = require("child_process");
const crypto = require("crypto");
const ffmpegPath = require("ffmpeg-static");
const googleTTS = require("google-tts-api");

const logPath = path.join("tools", "logs", "tts-online.log");
const chunkLimit = 200; // google-tts-api limit is typically small per req

function log(line) {
  const stamp = new Date().toISOString();
  fs.appendFileSync(logPath, `${stamp} ${line}\r\n`, "utf8");
}

function readSSMLFiles(dir) {
  return fs.readdirSync(dir).filter((f) => f.endsWith(".ssml"));
}

function ssmlToText(ssml) {
  return ssml
    .replace(/<break[^>]*time=['"](\d+)(m?s)['"][^>]*>/gi, (m, val, unit) => {
      // rough pause mapping: insert punctuation to force pause
      return unit === 's' ? '. '.repeat(Math.ceil(val)) : '. ';
    })
    .replace(/<[^>]+>/g, " ")
    .replace(/\s+/g, " ")
    .trim();
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

function concatMp3(files, output) {
  const listFile = path.join(os.tmpdir(), `tts-alt-${crypto.randomUUID()}.txt`);
  fs.writeFileSync(listFile, files.map(f => `file '${f.replace(/'/g, "'\\''")}'`).join("\n"));
  return new Promise((resolve, reject) => {
    const ff = spawn(ffmpegPath, ["-y", "-f", "concat", "-safe", "0", "-i", listFile, "-c", "copy", output]);
    ff.stderr.on("data", () => {});
    ff.on("close", (code) => {
      if (fs.existsSync(listFile)) fs.unlinkSync(listFile);
      if (code === 0) resolve(); else reject(new Error(`ffmpeg concat failed code ${code}`));
    });
  });
}

async function synthesizeChunk(text, outPath, attempt=1) {
  const backoffs = [1000, 2000, 4000];
  try {
    const url = googleTTS.getAudioUrl(text, {
      lang: 'en',
      slow: false,
      host: 'https://translate.google.com',
    });
    // fetch base64/buffer
    const res = await fetch(url);
    if (!res.ok) throw new Error(`Fetch failed ${res.status}`);
    const buf = await res.arrayBuffer();
    fs.writeFileSync(outPath, Buffer.from(buf));
    return true;
  } catch (err) {
    if (attempt <= backoffs.length) {
      log(`chunk retry attempt=${attempt} err=${err.message}`);
      await new Promise(r => setTimeout(r, backoffs[attempt-1]));
      return synthesizeChunk(text, outPath, attempt+1);
    }
    log(`chunk fail final err=${err.message}`);
    return false;
  }
}

async function processFile(ssmlDir, audioDir, file) {
  const ssmlPath = path.join(ssmlDir, file);
  const outPath = path.join(audioDir, path.parse(file).name + ".mp3");
  const content = fs.readFileSync(ssmlPath, "utf8");
  const text = ssmlToText(content);
  const chunks = chunkText(text);
  
  log(`start alt file=${ssmlPath} chunks=${chunks.length} service=google-tts-api`);
  const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), "tts-alt-"));
  const chunkFiles = [];
  let allOk = true;

  for (let i = 0; i < chunks.length; i++) {
    if (!chunks[i].length) continue;
    const chunkOut = path.join(tempDir, `chunk-${i}.mp3`);
    const ok = await synthesizeChunk(chunks[i], chunkOut);
    if (!ok) { allOk = false; break; }
    chunkFiles.push(chunkOut);
  }

  if (allOk && chunkFiles.length) {
    await concatMp3(chunkFiles, outPath);
    log(`success file=${ssmlPath} output=${outPath}`);
  } else {
    log(`failed file=${ssmlPath}`);
  }

  // Cleanup
  chunkFiles.forEach(f => { if (fs.existsSync(f)) fs.unlinkSync(f); });
  if (fs.existsSync(tempDir)) fs.rmdirSync(tempDir);
}

async function main() {
  const jobs = [
    { src: "training/shared/tts", dest: "training/shared/audio-online" },
    { src: "training/pega-poland/tts", dest: "training/pega-poland/audio-online" }
  ];
  for (const job of jobs) {
    if (!fs.existsSync(job.dest)) fs.mkdirSync(job.dest, { recursive: true });
    const files = readSSMLFiles(job.src);
    for (const f of files) {
      try {
        await processFile(job.src, job.dest, f);
      } catch (err) {
        log(`error file=${f} err=${err.message}`);
      }
    }
  }
}

main().catch((err) => {
  console.error(err);
  log(`fatal ${err.message}`);
  process.exit(1);
});
