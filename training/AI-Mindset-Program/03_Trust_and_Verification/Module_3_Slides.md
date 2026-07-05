# Module 3 — Trust, Verification, and Evidence over Opinion (Slide Outline)

**Format:** 90-minute lecture + live exercise · **14 slides** · Audience: mixed
**Design intent:** reframe verification from bureaucracy to professional identity. One planted-error exercise is the emotional core.

---

**Slide 1 — Title**
"Trust, Verification, and Evidence over Opinion"
Subtitle: *AI generates. You verify. You own.*

**Slide 2 — Two ways to fail** *(FRAMEWORK — automation bias, Parasuraman & Riley)*
Left: **Under-trust** — "I checked everything twice, so AI saved me nothing." (waste)
Right: **Over-trust** — "It sounded confident, so I shipped it." (damage)
One line: both are calibration failures. Calibration is trainable.

**Slide 3 — What a hallucination actually is**
A language model predicts plausible text; it does not look up facts. Confidence in tone ≠ confidence in truth.
One line: "It's not lying. It's completing. Your job is to know the difference."

**Slide 4 — Rule 1: truth lives in systems of record**
LLMs understand and reason; databases, code, and documents hold the facts. The winning pattern is fusion: AI for understanding, grounded sources for truth, human judgment to arbitrate.
(Adapted from the governance module — the strongest survivor of the earlier training kit.)

**Slide 5 — Grounding in practice**
Three grounding behaviors, cheapest first: (1) paste the source into the prompt; (2) use source-grounded tools (NotebookLM, RAG) that cite; (3) demand citations and click them.
One line: "No citation, no claim — the same standard I'm held to on these slides."

**Slide 6 — Case: Project Axiom** *(VERIFIED)*
A national infrastructure operator needed a reliable pre-ERP analysis. AI-assisted analysis of **97 projects**, 17 modules identified — **zero erroneous conclusions**.
The how: every AI finding passed a human verification gate before entering the report. Not a better model — a better *protocol*.

**Slide 7 — Case: evidence-tagged discovery** *(VERIFIED)*
A Nordic transaction-processing enterprise: **143 business rules** extracted from ~220,000 lines of legacy code at **94% confidence** — with **312 evidence-tagged citations**, every finding traceable to a line of source code.
One line: "Discovery you can audit beats discovery you must believe."

**Slide 8 — Why this matters: hidden complexity** *(STUDY)*
Standish CHAOS (2020): only ~31% of software projects succeed outright. A dominant cause: decisions made on assumed knowledge of systems nobody fully understands.
One line: "Most organizations don't have a knowledge problem. They have an *unverified-assumption* problem."

**Slide 9 — The calibrated-trust matrix**
2×2: **Stakes** (low/high) × **Verifiability** (easy/hard).
Low stakes + easy to verify → delegate freely. High stakes + easy → delegate, verify always. Low + hard → use for inspiration only. High stakes + hard to verify → don't delegate; decompose until verifiable.
One line: "Trust is not a feeling about the tool. It's a property of the task."

**Slide 10 — Verification as behavior, not virtue**
Concrete habits: citations-required prompts; the 60-second spot-check (names, numbers, dates first — highest hallucination density); tests as trust for code *(VERIFIED sidebar: PresoGen AI — ~600 automated tests as the trust mechanism across 3 LLM providers)*; second-model cross-check for high-stakes claims.

**Slide 11 — Governance essentials**
The non-negotiables: no client-identifying data or personal data into non-approved tools; least-privilege for agent access; treat external content pasted into prompts as untrusted (prompt injection); log what AI touched in deliverables.
One line: "Governance is what lets you say yes quickly and safely — it's an enabler, not a brake."

**Slide 12 — Case: Antystyki.pl** *(VERIFIED)*
An AI content pipeline for statistics journalism — 17+ statistical sources, every published item passes a **human-in-the-loop governance gate**.
One line: "Even a content pipeline about *statistics* keeps a human on the trigger. So can your workflows."

**Slide 13 — Exercise: catch the confident lie**
Participants receive a polished AI-generated analysis of a fictional dataset containing **three planted errors** (a wrong number, a fabricated citation, a subtly inverted conclusion). 10 minutes, pairs. Debrief: which error survived longest, and why (it *sounded* right).

**Slide 14 — Recap**
(1) Calibrate trust per task, not per tool. (2) Ground everything; no citation, no claim. (3) Verification is the professional identity: AI generates, you verify, you own.
Bridge: "Module 4: what happens when the thing you verify is not a paragraph but an entire pipeline of agents."
