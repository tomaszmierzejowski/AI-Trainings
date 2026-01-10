# TTS Comparison

Summary: Offline TTS (say + ffmpeg-static) succeeded for all SSML files. Online TTS (google-tts-api) also succeeded for all files using 200-char chunking.

## Per-file Status
| Module | Offline MP3 (path, duration, bitrate) | Online MP3 (Google) | Notes |
| --- | --- | --- | --- |
| AI Fundamentals (shared) | training/shared/audio/ai-fundamentals.mp3 — 00:01:54 @ 32 kb/s | training/shared/audio-online/ai-fundamentals.mp3 (Success) | Online typically shorter/faster than offline. |
| Prompting Power (shared) | training/shared/audio/prompting-power.mp3 — 00:01:34 @ 32 kb/s | training/shared/audio-online/prompting-power.mp3 (Success) | |
| Cursor/ChatGPT/Perplexity (shared) | training/shared/audio/cursor-chatgpt-perplexity.mp3 — 00:01:28 @ 32 kb/s | training/shared/audio-online/cursor-chatgpt-perplexity.mp3 (Success) | |
| Governance & Safety (shared) | training/shared/audio/governance-safety.mp3 — 00:01:37 @ 32 kb/s | training/shared/audio-online/governance-safety.mp3 (Success) | |
| Pega Workflow AI (shared) | training/shared/audio/pega-workflow-ai.mp3 — 00:01:22 @ 32 kb/s | training/shared/audio-online/pega-workflow-ai.mp3 (Success) | |
| Productivity Recipes (shared) | training/shared/audio/productivity-recipes.mp3 — 00:01:34 @ 32 kb/s | training/shared/audio-online/productivity-recipes.mp3 (Success) | |
| Builder Tools (shared) | training/shared/audio/builder-tools.mp3 — 00:01:15 @ 32 kb/s | training/shared/audio-online/builder-tools.mp3 (Success) | |
| Pega Workflow AI (Pega) | training/pega-poland/audio/pega-workflow-ai.mp3 — 00:01:15 @ 32 kb/s | training/pega-poland/audio-online/pega-workflow-ai.mp3 (Success) | |
| Pega Productivity (Pega) | training/pega-poland/audio/pega-productivity.mp3 — 00:01:22 @ 32 kb/s | training/pega-poland/audio-online/pega-productivity.mp3 (Success) | |
| Pega Builder Demos (Pega) | training/pega-poland/audio/pega-builder-demos.mp3 — 00:01:10 @ 32 kb/s | training/pega-poland/audio-online/pega-builder-demos.mp3 (Success) | |
| All-Hands (shared/Pega) | N/A (no SSML) | N/A | Slides only; no TTS. |

## Recommendation
- Online (Google) provides higher quality voice but requires internet access during build.
- Offline (Windows SAPI) is a safe fallback for air-gapped environments.
- Both sets are generated and available. Logs: tools/logs/tts-online.log (Google).
