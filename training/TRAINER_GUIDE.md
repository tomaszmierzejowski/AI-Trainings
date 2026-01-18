# Trainer Guide: Practical AI Enablement

## 🎯 Your Mission
Deliver a high-impact, hands-on training that gets participants from "curious" to "capable" in 1-3 days. Focus on **Prompt Mastery** and **Tool Selection**.

## 📦 Asset Map
| Asset | Location | Usage |
|---|---|---|
| **Agendas** | `training/shared/agendas.md` | Pick 1-Day (Fast) or 3-Day (Deep). |
| **Slides (EN)** | `training/shared/pptx/*.pptx` | Primary presentation decks. |
| **Slides (PL)** | `training/shared/pptx-pl/*.pptx` | Polish variants. |
| **Audio (EN/PL)** | `training/shared/audio-online/*.mp3` | For self-paced or refresher. |
| **Labs** | `training/shared/labs.md` | Step-by-step workshop instructions. |
| **Datasets** | `training/shared/assets/fictional-datasets/` | CSVs for Lab 1 & 2. |

## 🗣️ The Narrative Arc
1.  **The Hook**: "We are drowning in busywork. AI is the life raft."
2.  **The Method**: "Don't chat. Engineer prompts (RTF) and pick the right tool."
3.  **The Proof**: "Let's build a Pega intake process in 30 minutes."

## 🛠️ How to Run the Labs
*   **Lab 1 (Intake)**: Have them open `service.csv`. Challenge them to extract JSON. Compare results.
*   **Lab 2 (Decisioning)**: Brainstorm fraud rules. Use ChatGPT to turn them into a table.
*   **Lab 3 (Build)**: Use MagicUI to dream a UI, then Cursor to spec it for Pega.

## 🎤 Demo Scripts (Cheat Sheet)
*   **ChatGPT**: Show "Bad Prompt" vs "RTF Prompt". (See `prompting-power.md`).
*   **Perplexity**: Search "Latest Pega 8.8 features" vs Google search.
*   **Cursor**: Open a file, hit `Cmd+K`, type "Refactor this to be cleaner".

## 🛡️ Safety & Governance
*   **Remind often**: "If you wouldn't put it on a billboard, don't put it in a prompt."
*   **Hallucinations**: Teach "Grounding" (checking sources) and "Constraints" (asking the AI to refuse if unsure).

## ❓ Common Q&A / Objections
*   **"Will it steal our data?"**: "We use approved enterprise endpoints. Data is not trained on."
*   **"It makes mistakes."**: "Yes. It's a reasoning engine, not a database. Verify everything."
*   **"Why not just use ChatGPT for everything?"**: "It doesn't know your codebase (Cursor does) and can't search the web live (Perplexity does)."

## 🆘 Troubleshooting
*   **Internet down?**: Switch to offline slides and describe the demos.
*   **Access issues?**: Have participants pair programming style.
*   **Boredom?**: Run a "Prompt Battle" - who can summarize this email in 5 words?
