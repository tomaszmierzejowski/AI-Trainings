# AI-Mindset Module 2 — Rewiring the Daily Workflow with Cursor, NotebookLM, Gemini, and Claude (NotebookLM Source Document)

This document describes how to convert the AI-Mindset from principle into daily practice using four tools — Claude, Cursor, NotebookLM, and Gemini — each taught as a habit replacement rather than a feature set. It covers the two foundational prompting habits (the Role–Task–Format frame and iterative refinement), the job each tool owns in a working day, a decision rule that prevents tool paralysis, and verified proof points showing the approach works for both non-technical and highly technical practitioners.

## The operating principle: change the order, not the toolbox

The module's principle restates the program thesis operationally: value comes not from adding tools to a workday but from changing the sequence of the workday. The old model is task, then manual execution, then optionally asking AI to polish the result. The new model is task, then an AI first draft or first answer, then human judgment, then done. The failure mode this module explicitly guards against is tool sprawl: an organization with ten AI tools and zero ingrained habits is worse off than one with a single tool and a single reliable habit, because sprawl produces decision fatigue and dabbling. The module's rule is a maximum of one new habit per tool, and only for tools that genuinely fit the participant's work.

## The two prompting habits

The first habit is the Role–Task–Format (RTF) frame: state who the AI should be, what specifically it should do, and what shape the output should take. For example, instead of "summarize this document," an RTF prompt reads: "You are a risk auditor reporting to a CFO. Extract the five largest financial risks from this document. Deliver as a table with columns for risk, likelihood, and an evidence quote." RTF is deliberately the only prompting framework taught in the program, on the principle that one frame practiced daily beats five frameworks admired in a slide. The program intentionally attaches no numerical accuracy claim to prompting techniques, because no defensible published source supports the percentages commonly quoted in AI training materials; the evidence offered is a live before-and-after contrast on the same document.

The second habit is iterative refinement: when the first output disappoints, refine the instruction ("shorter; more formal; add the compliance angle") rather than regenerating and hoping. The working analogy is a brilliant new colleague on their first day — nobody fires a new hire over a mediocre first draft; they give feedback. Large requests should be decomposed into steps for the same reason large tasks are decomposed for people.

## Four tools, four jobs

Claude is the thinking partner and the default first step for knowledge work: first drafts of documents and emails, explanation and interrogation of long materials, devil's-advocate review of plans, and multi-step analysis. The behavior it replaces is staring at a blank page; the new behavior is interrogating a draft.

Cursor is the building tool: an AI-integrated code editor with full project context. Its highest-value behavior for mixed audiences is codebase question-answering before any code is written — replacing the old pattern of searching, guessing, and waiting for a colleague who remembers the system. For engineers, its editing modes follow a proportionality rule the program calls the leash rule: the larger the change, the smaller the leash. Inline edits are reviewed hunk by hunk; agent-mode multi-file changes are reviewed like a pull request from an unknown contributor. VERIFIED: this working pattern, industrialized into a designed pipeline with verification gates, is how the Proof of Scale engagement understood 20 legacy Java applications in three weeks — a 4–8× acceleration over conventional application comprehension, with 187 endpoints mapped.

NotebookLM is the grounded learning tool: the user uploads their own sources (documents, transcripts, reports) and the tool answers questions strictly from those sources, with citations that link back to the exact passage, and can generate an audio overview for passive review. The behavior it replaces is the unread PDF graveyard; the new behavior is interrogating the pile and requiring receipts. Its source-grounded design makes it the program's flagship example of evidence-over-opinion embodied in a product — with the honest caveat that citations shrink the verification job but do not eliminate it, since summaries can be imperfect and sources themselves can be wrong.

Gemini owns scale and modality: very long inputs (massive context windows), non-text inputs such as video and audio recordings, and integration with Google Workspace. The behavior it replaces is "I'll watch the 90-minute recording later," which in practice means never; the new behavior is interrogating the recording directly.

The decision rule that prevents paralysis: if the task is code, use Cursor; if it is a pile of your own documents, use NotebookLM; if the input is audio, video, or enormous, use Gemini; for everything else — thinking, writing, deciding — start in Claude and move only when a specialist tool earns it. The rule is a default, not a doctrine; its purpose is to eliminate the debate about where to start.

## Verified proof points

Two silent objections predictably arise in every audience, and each has a verified answer from the author's own delivered work.

The non-technical objection — "this works for engineers, not for me" — is answered by Lidka: a non-technical children's-book publisher needed an audiobook e-commerce store with Polish payment and logistics integrations (Tpay and InPost). The store was built in days, and the decisive fact is not the build speed but the outcome: the owner operates it herself with full autonomy. This is the fishing-rod philosophy demonstrated — the deliverable was independence, not dependency.

The engineering objection — "AI-first development must mean test-poor development" — is answered by PresoGen AI, a commercial desktop application shipping with approximately 600 automated tests across a pipeline spanning three LLM providers, and by Mana Menu, a consumer product backend with approximately 657 automated tests behind 37 controllers. Speed and rigor are not a trade-off when verification is a habit rather than an afterthought.

## The lab and the habit contract

The module's centerpiece is a roughly 90-minute lab in which every participant works on one real task from their actual backlog — not a canned exercise — in one of two tracks: a technical track pairing Cursor (on a provided legacy codebase sample) with Claude for the write-up, and a non-technical track pairing NotebookLM (on provided source documents) with Claude or Gemini for the deliverable. The success criterion is a shippable artifact plus the prompt trail that produced it; the trainer coaches behaviors without touching keyboards. All demonstration and lab data is fictional, modeling the governance reflex — no client names, no real personal data — that Module 3 formalizes.

The module closes with the verification handshake — "AI generates. You verify. You own." — and a written habit contract per participant: which tool, attached to which recurring trigger, replacing which old behavior, starting at which calendar slot in the coming week. Contracts are exchanged with a partner for accountability and return in Module 5's 30-day behavior plan.
