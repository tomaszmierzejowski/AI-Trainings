# Training Asset Index

Generated with local marp-cli (PPTX) and offline say+ffmpeg TTS (offline MP3). Online TTS generated via google-tts-api (free endpoint).

## Shared Modules
| Module | PPTX | SSML | SRT | MP3 (offline) | MP3 (online - Google) |
| --- | --- | --- | --- | --- | --- |
| AI Fundamentals | training/shared/pptx/ai-fundamentals.pptx | training/shared/tts/ai-fundamentals.ssml | training/shared/tts/ai-fundamentals.srt | training/shared/audio/ai-fundamentals.mp3 | training/shared/audio-online/ai-fundamentals.mp3 |
| Prompting Power | training/shared/pptx/prompting-power.pptx | training/shared/tts/prompting-power.ssml | training/shared/tts/prompting-power.srt | training/shared/audio/prompting-power.mp3 | training/shared/audio-online/prompting-power.mp3 |
| Cursor/ChatGPT/Perplexity | training/shared/pptx/cursor-chatgpt-perplexity.pptx | training/shared/tts/cursor-chatgpt-perplexity.ssml | training/shared/tts/cursor-chatgpt-perplexity.srt | training/shared/audio/cursor-chatgpt-perplexity.mp3 | training/shared/audio-online/cursor-chatgpt-perplexity.mp3 |
| Governance & Safety | training/shared/pptx/governance-safety.pptx | training/shared/tts/governance-safety.ssml | training/shared/tts/governance-safety.srt | training/shared/audio/governance-safety.mp3 | training/shared/audio-online/governance-safety.mp3 |
| Pega Workflow AI (shared) | training/shared/pptx/pega-workflow-ai.pptx | training/shared/tts/pega-workflow-ai.ssml | training/shared/tts/pega-workflow-ai.srt | training/shared/audio/pega-workflow-ai.mp3 | training/shared/audio-online/pega-workflow-ai.mp3 |
| Productivity Recipes | training/shared/pptx/productivity-recipes.pptx | training/shared/tts/productivity-recipes.ssml | training/shared/tts/productivity-recipes.srt | training/shared/audio/productivity-recipes.mp3 | training/shared/audio-online/productivity-recipes.mp3 |
| Builder Tools | training/shared/pptx/builder-tools.pptx | training/shared/tts/builder-tools.ssml | training/shared/tts/builder-tools.srt | training/shared/audio/builder-tools.mp3 | training/shared/audio-online/builder-tools.mp3 |
| All-Hands | training/shared/pptx/all-hands.pptx | N/A | N/A | N/A | N/A |

## Pega Poland Modules
| Module | PPTX | SSML | SRT | MP3 (offline) | MP3 (online - Google) |
| --- | --- | --- | --- | --- | --- |
| Pega Workflow AI | training/pega-poland/pptx/pega-workflow-ai.pptx | training/pega-poland/tts/pega-workflow-ai.ssml | training/pega-poland/tts/pega-workflow-ai.srt | training/pega-poland/audio/pega-workflow-ai.mp3 | training/pega-poland/audio-online/pega-workflow-ai.mp3 |
| Pega Productivity | training/pega-poland/pptx/pega-productivity.pptx | training/pega-poland/tts/pega-productivity.ssml | training/pega-poland/tts/pega-productivity.srt | training/pega-poland/audio/pega-productivity.mp3 | training/pega-poland/audio-online/pega-productivity.mp3 |
| Pega Builder Demos | training/pega-poland/pptx/pega-builder-demos.pptx | training/pega-poland/tts/pega-builder-demos.ssml | training/pega-poland/tts/pega-builder-demos.srt | training/pega-poland/audio/pega-builder-demos.mp3 | training/pega-poland/audio-online/pega-builder-demos.mp3 |
| All-Hands | training/pega-poland/pptx/all-hands.pptx | N/A | N/A | N/A | N/A |

## Data (fictional)
- Shared CSVs: training/shared/assets/fictional-datasets/{claims.csv,onboarding.csv,service.csv}
- Pega mirrors: training/pega-poland/assets/fictional-datasets/{claims.csv,onboarding.csv,service.csv}

## Lab Packs
- Shared: training/shared/labs/packs/lab1.md, lab2.md, lab3.md
- Pega: training/pega-poland/labs/packs/lab1.md, lab2.md, lab3.md

## Governance & Readouts
- Checklists: training/shared/governance-checklist.md, training/pega-poland/governance-checklist.md
- Readouts: training/shared/readout-template.md, training/pega-poland/readout-template.md
- Delivery notes (Pega): training/pega-poland/delivery-notes.md

## Tools/Commands Used
- PPTX: npx marp <file>.marp.md --pptx --output <dest>
- Audio offline: node tools/ssml-to-mp3-offline.js (say + ffmpeg-static)
- Audio online: node tools/ssml-to-mp3-online-alt.js (google-tts-api, 200-char chunks)
