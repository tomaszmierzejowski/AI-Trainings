const fs = require("fs");
const path = require("path");
const os = require("os");

// Polyfill global crypto for msedge-tts on Node < 19
if (!global.crypto) {
    const { webcrypto } = require('node:crypto');
    global.crypto = webcrypto;
}

const { MsEdgeTTS, OUTPUT_FORMAT } = require("msedge-tts");
const { spawn } = require("child_process");
const ffmpegPath = require("ffmpeg-static");

// --- Configuration ---
const INPUT_FILE = path.join(__dirname, "Video_Script_Final.md");
const OUTPUT_FILE = path.join(__dirname, "Video_Script_Final_Online.mp3");
const TEMP_DIR = path.join(os.tmpdir(), "audiobook-online-" + Date.now());

// Voice Configuration
const VOICES = {
    "CEO": "en-US-ChristopherNeural",
    "TOMASZ": "en-US-EricNeural", 
    "NARRATOR": "en-US-AriaNeural"
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

function escapeXml(unsafe) {
    return unsafe.replace(/[<>&'"]/g, function (c) {
        switch (c) {
            case '<': return '&lt;';
            case '>': return '&gt;';
            case '&': return '&amp;';
            case '\'': return '&apos;';
            case '"': return '&quot;';
        }
    });
}

function generateAudio(text, voice, outputPath) {
    return new Promise(async (resolve, reject) => {
        const tts = new MsEdgeTTS();
        await tts.setMetadata(voice, OUTPUT_FORMAT.AUDIO_24KHZ_48KBITRATE_MONO_MP3);
        
        try {
            const { audioFilePath } = await tts.toFile(path.dirname(outputPath), text);
            // Rename the file to expected output path if needed, 
            // but toFile usually takes a directory and generates a name? 
            // The README says: tts.toFile("./tmpfolder", "Hi, how are you?");
            // And returns { audioFilePath }.
            // We should check if we can specify filename.
            
            // Actually, let's just use toStream and write to file to be sure of the path.
            
            /*
            const { audioStream } = await tts.toStream(text);
            const writeStream = fs.createWriteStream(outputPath);
            audioStream.pipe(writeStream);
            writeStream.on('finish', resolve);
            writeStream.on('error', reject);
            */
           
           // Using toFile helps with buffering maybe?
           // Let's retry with toStream logic which is cleaner for custom filenames.
           const { audioStream } = tts.toStream(text); // toStream is synchronous in getting the stream object? No, README says `const {audioStream} = tts.toStream(...)` but wait, example has `await tts.toStream`.
           // Let's use await.
           
           const streamRes = await tts.toStream(text);
           const audio = streamRes.audioStream;
           
           const file = fs.createWriteStream(outputPath);
           audio.pipe(file);
           
           file.on('finish', () => {
               file.close();
               resolve();
           });
           
           file.on('error', (err) => {
               fs.unlink(outputPath, () => reject(err));
           });
           
        } catch (error) {
            reject(error);
        }
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
            "-c", "copy", // Copy codec since they are already MP3s
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

        const audioFiles = [];

        for (let i = 0; i < blocks.length; i++) {
            const block = blocks[i];
            const voice = VOICES[block.speaker] || VOICES["NARRATOR"];
            const filename = path.join(TEMP_DIR, `part-${i.toString().padStart(3, '0')}.mp3`);
            
            console.log(`Generating part ${i + 1}/${blocks.length}: [${block.speaker}] (${voice}) ${block.text.substring(0, 30)}...`);
            
            // Retry logic
            let retries = 3;
            while (retries > 0) {
                try {
                    const safeText = escapeXml(block.text);
                    await generateAudio(safeText, voice, filename);
                    break;
                } catch (e) {
                    console.warn(`Error generating part ${i+1}, retrying... (${3-retries+1}/3)`, e.message);
                    retries--;
                    if (retries === 0) throw e;
                    await new Promise(r => setTimeout(r, 2000));
                }
            }
            
            audioFiles.push(filename);
        }

        console.log("Combining audio files...");
        await concatAudio(audioFiles, OUTPUT_FILE);
        
        console.log(`Audiobook created at: ${OUTPUT_FILE}`);

    } catch (err) {
        console.error("Error:", err);
    } finally {
        // Cleanup
        if (fs.existsSync(TEMP_DIR)) {
            try {
                fs.rmdirSync(TEMP_DIR, { recursive: true });
            } catch (e) {
                console.warn("Could not clean up temp dir:", e.message);
            }
        }
    }
}

main();
