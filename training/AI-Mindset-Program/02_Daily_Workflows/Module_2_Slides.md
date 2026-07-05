# Module 2 — Rewiring the Daily Workflow: Cursor, NotebookLM, Gemini, Claude (Slide Outline)

**Format:** half-day with hands-on labs · **22 slides** · Audience: mixed; labs split by track (technical / non-technical)
**Design intent:** every tool is taught as a *habit replacement* — "old behavior → new behavior" appears on every tool slide. No feature tours.

---

**Slide 1 — Title**
"Rewiring the Daily Workflow"
Subtitle: *Four tools. Four habits. One rule: AI is your first step.*

**Slide 2 — The principle**
Old model: task → do it the old way → (maybe) ask AI to polish. New model: task → AI first draft/first answer → your judgment → done.
One line: "We are not adding tools to your day. We are changing the order of your day."

**Slide 3 — Anti-pattern: tool sprawl**
Visual: 15 AI logos, all greyed out. "Ten tools and zero habits is worse than one tool and one habit."
Rule of the day: leave with **one habit per tool, maximum four** — and even that only if all four fit your work.

**Slide 4 — The map: four tools, four jobs**
| Tool | Job in your workflow | First-step trigger |
|---|---|---|
| **Claude** | Thinking partner: drafting, reasoning, long documents, agents | "I need to write/decide/analyze" |
| **Cursor** | Building: code with full project context | "I need to change or understand code" |
| **NotebookLM** | Learning: grounded synthesis of *your* sources | "I need to understand this pile of documents" |
| **Gemini** | Scale & multimodal: video, meetings, huge context, Workspace | "The input isn't text, or it's enormous" |

**Slide 5 — Prompting is a behavior, not a trick**
The RTF frame: **Role — Task — Format.**
"You are a [role]. Do [specific task]. Deliver as [format]."
One line: the single highest-leverage habit in this course.

**Slide 6 — RTF before/after (live example)**
Bad: "summarize this document." Good: "You are a risk auditor reporting to a CFO. Extract the five largest financial risks from this document. Deliver as a table: risk, likelihood, evidence quote."
Speaker runs this live on a fictional dataset.

**Slide 7 — The second habit: iterate, don't regenerate**
Refine ("shorter; more formal; add the compliance angle") instead of re-rolling the dice. Decompose big asks into steps.
One line: "Treat it like a brilliant new colleague on day one — brief it, don't fire it."

**Slide 8 — Claude: the thinking partner**
Old behavior → new behavior: "Stare at a blank page" → "Interrogate a draft."
Core workflows: first drafts of anything; 'explain this document to me'; devil's-advocate review of your plan; multi-step analysis.

**Slide 9 — Claude in practice (demo)**
Live: paste a (fictional) messy meeting transcript → RTF prompt → decision log + action items + risks in 60 seconds. Then one refinement pass.

**Slide 10 — Cursor: the codebase conversation**
Old behavior → new behavior: "grep + tribal knowledge + coffee" → "ask the codebase directly."
Core workflows: codebase Q&A *before* writing code; inline edits; agent mode for scoped multi-file changes.

**Slide 11 — Cursor rule of engagement** *(bridge to Module 3)*
"The larger the change, the smaller the leash." Inline edit → review each hunk. Agent mode → review the diff like a hostile PR.
VERIFIED sidebar: this working pattern is how 20 legacy applications were understood in 3 weeks (Project Velocity, 4–8× faster understanding, 187 endpoints mapped).

**Slide 12 — NotebookLM: grounded learning**
Old behavior → new behavior: "PDF graveyard you'll never read" → "a notebook that answers only from your sources, with citations."
Core workflows: onboarding to a new domain/project; audio overview for the commute; "what do my sources disagree about?"

**Slide 13 — NotebookLM: the killer property**
It answers from *your uploaded sources* and cites them — hallucination surface drastically reduced by design.
One line: "This is evidence-over-opinion as a product."

**Slide 14 — Gemini: scale and modality**
Old behavior → new behavior: "I'll watch the 90-minute recording later (never)" → "interrogate the video/meeting/spreadsheet directly."
Core workflows: very long documents and codebases (massive context), video/audio/image inputs, Workspace integration (Docs/Sheets/Meet).

**Slide 15 — Choosing without paralysis**
Decision tree (one glance): Is it code? → Cursor. Is it *your* document pile? → NotebookLM. Is it video/audio/huge? → Gemini. Everything else — thinking, writing, deciding? → Claude.
One line: "When in doubt, start in Claude; move when a specialist tool earns it."

**Slide 16 — Proof of autonomy: Lidka** *(VERIFIED)*
A non-technical publisher needed a children's audiobook store with Polish payments and logistics (Tpay + InPost). Built in days — and she operates it herself, with full autonomy.
One line: "The fishing rod works for non-engineers. That's the point of it."

**Slide 17 — Proof of discipline: PresoGen AI & Mana Menu** *(VERIFIED)*
AI-first development ≠ sloppy development: PresoGen AI ships with ~600 automated tests across 3 LLM providers; Mana Menu with ~657 tests behind 37 controllers.
One line: "Speed and rigor are not a trade-off when verification is a habit."

**Slide 18 — Lab briefing**
Everyone brings one *real* task from their actual backlog. Tracks: (A) technical — Cursor on a provided legacy codebase sample + Claude for the write-up; (B) non-technical — NotebookLM on provided source docs + Claude/Gemini for the deliverable.
Success criterion: a shippable artifact + the prompt trail that produced it.

**Slide 19 — Lab (working block, ~90 min)**
Slide stays up: RTF reminder, decision tree, "iterate don't regenerate," trainer circulating.

**Slide 20 — Lab debrief**
Three volunteers show: the task, the first prompt, the refinement that mattered, the final artifact. Trainer names the *behaviors* observed, not the outputs.

**Slide 21 — The verification handshake** *(bridge)*
Every artifact produced today has one thing in common: a human signed it. "AI generates. You verify. You own."
One line: "Module 3 makes that trustworthy at scale."

**Slide 22 — Habit contract**
Each participant writes: tool → trigger → old behavior it replaces → first calendar slot this week. Pairs exchange contracts (accountability partner). These feed Module 5.
