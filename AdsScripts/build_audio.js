const fs = require("fs");
const path = require("path");
const os = require("os");
const say = require("say");
const { spawn } = require("child_process");
const ffmpegPath = require("ffmpeg-static");

// --- Configuration ---
const INPUT_FILE = path.join(__dirname, "Video_Script_Final.md");
const OUTPUT_FILE = path.join(__dirname, "Video_Script_Final.mp3");
const TEMP_DIR = path.join(os.tmpdir(), "audiobook-gen-" + Date.now());

// Voice Configuration
const VOICES = {
    "CEO": { name: "Microsoft David Desktop", speed: 1.0 },
    "TOMASZ": { name: "Microsoft David Desktop", speed: 1.1 }, // Slightly faster to distinguish
    "NARRATOR": { name: "Microsoft Zira Desktop", speed: 1.0 }
};

// --- Helpers ---
function parseMarkdown(content) {
    const lines = content.split(/\r?\n/);
    const blocks = [];
    let currentSpeaker = null;

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();

        // Check for speaker
        if (line.match(/^(\*\*?)?(CEO|TOMASZ)(\*\*?)?(\s*\(.*\))?:?$/)) {
            const match = line.match(/^(\*\*?)?(CEO|TOMASZ)/);
            if (match) {
                currentSpeaker = match[2];
            }
            continue;
        }

        // Check for dialogue
        if (line.startsWith(">") && currentSpeaker) {
            let text = line.substring(1).trim();
            // Remove leading/trailing quotes if present
            if (text.startsWith('"') && text.endsWith('"')) {
                text = text.substring(1, text.length - 1);
            }
            
            // Clean up Markdown bold/italic
            text = text.replace(/\*\*/g, "").replace(/\*/g, "");

            // If text is not empty, add it
            if (text) {
                blocks.push({
                    speaker: currentSpeaker,
                    text: text
                });
            }
        }
    }
    return blocks;
}

function generateWav(text, voiceConfig, outputPath) {
    return new Promise((resolve, reject) => {
        say.export(text, voiceConfig.name, voiceConfig.speed, outputPath, (err) => {
            if (err) reject(err);
            else resolve(outputPath);
        });
    });
}

function concatAudio(files, output) {
    const listFile = path.join(TEMP_DIR, "filelist.txt");
    const fileContent = files.map(f => `file '${f.replace(/\\/g, "/")}'`).join("\n");
    fs.writeFileSync(listFile, fileContent);

    return new Promise((resolve, reject) => {
        const args = [
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", listFile,
            "-c:a", "libmp3lame", // Convert to MP3
            "-q:a", "2", // High quality
            output
        ];

        console.log(`Running ffmpeg with args: ${args.join(" ")}`);
        const ff = spawn(ffmpegPath, args);

        ff.stderr.on("data", (data) => {
            // console.log(`ffmpeg: ${data}`); // Verbose
        });

        ff.on("close", (code) => {
            if (code === 0) resolve();
            else reject(new Error(`ffmpeg exited with code ${code}`));
        });
    });
}

// --- Main ---
async function main() {
    if (!fs.existsSync(TEMP_DIR)) fs.mkdirSync(TEMP_DIR);
    
    try {
        console.log(`Reading ${INPUT_FILE}...`);
        const content = fs.readFileSync(INPUT_FILE, "utf8");
        const blocks = parseMarkdown(content);
        console.log(`Found ${blocks.length} dialogue blocks.`);

        const wavFiles = [];

        for (let i = 0; i < blocks.length; i++) {
            const block = blocks[i];
            const voiceConfig = VOICES[block.speaker] || VOICES["NARRATOR"];
            const filename = path.join(TEMP_DIR, `part-${i.toString().padStart(3, '0')}.wav`);
            
            console.log(`Generating part ${i + 1}/${blocks.length}: [${block.speaker}] ${block.text.substring(0, 30)}...`);
            await generateWav(block.text, voiceConfig, filename);
            wavFiles.push(filename);
        }

        console.log("Combining audio files...");
        await concatAudio(wavFiles, OUTPUT_FILE);
        
        console.log(`Audiobook created at: ${OUTPUT_FILE}`);

    } catch (err) {
        console.error("Error:", err);
    } finally {
        // Cleanup
        if (fs.existsSync(TEMP_DIR)) {
            // fs.rmdirSync(TEMP_DIR, { recursive: true }); // Keep for debug if needed
            console.log(`Temp files left in ${TEMP_DIR}`);
        }
    }
}

main();
