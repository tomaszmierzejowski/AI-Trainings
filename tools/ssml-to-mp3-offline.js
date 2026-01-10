const fs = require("fs");
const path = require("path");
const say = require("say");
const ffmpegPath = require("ffmpeg-static");
const ffmpeg = require("fluent-ffmpeg");

ffmpeg.setFfmpegPath(ffmpegPath);

function ssmlToText(content) {
  return content
    .replace(/<break[^>]*>/gi, ". ")
    .replace(/<[^>]+>/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function exportWav(text, wavPath, voice = null, speed = 1.0) {
  return new Promise((resolve, reject) => {
    say.export(text, voice, speed, wavPath, (err) => {
      if (err) reject(err);
      else resolve();
    });
  });
}

function wavToMp3(wavPath, mp3Path) {
  return new Promise((resolve, reject) => {
    ffmpeg(wavPath)
      .toFormat("mp3")
      .on("error", reject)
      .on("end", resolve)
      .save(mp3Path);
  });
}

async function convertDir(src, dest) {
  const files = fs.readdirSync(src).filter((f) => f.endsWith(".ssml"));
  for (const file of files) {
    const ssmlPath = path.join(src, file);
    const outPath = path.join(dest, path.parse(file).name + ".mp3");
    const wavPath = outPath + ".wav";
    const content = fs.readFileSync(ssmlPath, "utf8");
    const text = ssmlToText(content);
    console.log(`Synthesizing offline ${ssmlPath} -> ${outPath}`);
    await exportWav(text, wavPath);
    await wavToMp3(wavPath, outPath);
    fs.unlinkSync(wavPath);
  }
}

async function run() {
  await convertDir("training/shared/tts", "training/shared/audio");
  await convertDir("training/pega-poland/tts", "training/pega-poland/audio");
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
