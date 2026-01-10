# Project Tooling & Structure

Purpose: This project contains reusable training assets (slides, audio, labs, datasets, checklists) for AI enablement at Pega Poland and shared contexts. Assets are generated via automated tooling (PPTX from Marp, MP3 from SSML).

## Folder Structure

### Shared (	raining/shared/)
- **slides/**: Source .marp.md decks (e.g., ai-fundamentals, prompting-power).
- **pptx/**: Generated PowerPoint files.
- **	ts/**: Source .ssml scripts and .srt cues.
- **udio/**: Generated offline MP3s (Windows SAPI).
- **udio-online/**: Generated online MP3s (Google TTS).
- **labs/packs/**: Prompt packs (e.g., lab1.md) with test cases.
- **ssets/fictional-datasets/**: Clean CSVs (claims, onboarding, service).
- **modules/**: Markdown outlines/scripts (deprecated by full slides/SSML).
- **	emplates/**: Lab, readout, and audiobook script templates.
- **gendas.md, survey.md, daptation-guide.md**: Core docs.
- **governance-checklist.md, 
eadout-template.md**: Process assets.

### Pega Poland (	raining/pega-poland/)
- Mirrors shared structure with localized/specific assets.
- **slides/**: Pega-specific decks (workflow-ai, productivity, builder-demos).
- **delivery-notes.md, daptation-notes.md**: Context for Krakow hub delivery.

## Tooling & Generation

### Slides (Marp → PPTX)
- **Source**: *.marp.md files in slides/ folders.
- **Engine**: Local @marp-team/marp-cli.
- **Command**: 
px marp <file>.marp.md --pptx --output <dest>.pptx
- **Output**: pptx/ folders.

### Audio (SSML → MP3)
Two paths exist; compare results in 	raining/tts-comparison.md.

1. **Offline TTS (Default)**
   - **Engine**: say (Windows SAPI) + fmpeg-static.
   - **Script**: 
ode tools/ssml-to-mp3-offline.js.
   - **Output**: udio/ folders.
   - **Pros**: Works air-gapped; free. **Cons**: Robotic voice.

2. **Online TTS (Alternate)**
   - **Engine**: google-tts-api (unauthenticated, chunked to 200 chars).
   - **Script**: 
ode tools/ssml-to-mp3-online-alt.js.
   - **Output**: udio-online/ folders.
   - **Note**: Previous Edge/Azure attempts (	ools/ssml-to-mp3-online.js) return 403.

## Usage Guide

### How to Update Slides
1. Edit 	raining/shared/slides/*.marp.md or 	raining/pega-poland/slides/*.marp.md.
2. Run 
px marp <path-to-file> --pptx --output <path-to-output>.
3. Verify PPTX opens correctly.

### How to Regenerate Audio
1. Edit .ssml files in 	ts/ folders.
2. Run 
ode tools/ssml-to-mp3-offline.js for offline MP3s.
3. Run 
ode tools/ssml-to-mp3-online-alt.js for online MP3s.
4. Check 	ools/logs/tts-online.log for errors.

### Labs & Datasets
- **Labs**: Defined in 	raining/shared/labs.md and 	raining/pega-poland/labs.md.
- **Prompt Packs**: Stored in labs/packs/ (e.g., lab1.md) with 10 fictional test cases.
- **Data**: Fictional CSVs in ssets/fictional-datasets/. **Never use real client data.**

### Governance
- Use governance-checklist.md before delivery to confirm endpoints/approvals.
- Use 
eadout-template.md for final presentations.

## Indexes
- **	raining/index.md**: Master list of all generated assets (PPTX, MP3, datasets, packs).
- **	raining/tts-comparison.md**: Status and duration of offline vs. online audio files.

## Important Notes
- **Line Endings**: Keep CRLF for all text files.
- **Data Safety**: All datasets and examples must remain fictional/scrubbed.
- **Secrets**: Do not commit API keys or credentials to the repo.
