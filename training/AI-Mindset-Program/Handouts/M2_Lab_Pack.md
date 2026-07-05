# Module 2 Lab Pack — "One Real Task, Four Tools"

**Duration:** ~90 min · **Output required:** one shippable artifact + the prompt trail that produced it.
**Data rule (read aloud before start):** no client names, no real personal data in any tool. Fictional datasets are provided; your real task must be sanitized before it enters a prompt.

---

## Track A — Technical (Cursor + Claude)

**Setup:** provided legacy codebase sample (trainer: reuse the discovery-sample repo; verify it opens in Cursor on a locked-down laptop the week before).

**Your task (pick one, or bring your own):**
1. Answer, using codebase Q&A only (no manual grep): "What happens end-to-end when a user submits the main form?" Produce a one-page flow description with file references.
2. Find and describe the three riskiest areas of the codebase (no tests, high coupling, dead config). Produce a mini risk register.
3. Make one scoped inline change (trainer marks candidates in the repo) — then write the PR description with Claude.

**Required behaviors (this is what's graded, not the output):**
- Codebase Q&A *before* any editing.
- RTF on every prompt (role, task, format).
- The leash rule: review every hunk of any edit.
- At least one refinement pass — iterate, don't regenerate.

## Track B — Non-technical (NotebookLM + Claude/Gemini)

**Setup:** provided source-doc pack (trainer: 4–6 fictional documents — policy doc, two reports with a deliberate disagreement between them, meeting transcript, spreadsheet export).

**Your task (pick one, or bring your own):**
1. Build a notebook from the pack and produce a one-page executive brief answering: "What do these sources agree on, where do they conflict, and what's missing?" Every claim cited.
2. Turn the meeting transcript into a decision log + action list + open risks (Claude, RTF prompt), then verify names/numbers/dates against the transcript.
3. Generate an audio overview of the pack; listen to 3 minutes; write down one thing it got subtly wrong or overweighted. (This doubles as Module 3 foreshadowing.)

**Required behaviors:**
- Sources uploaded before questions asked — no free-floating chat.
- Click at least three citations to the source passage.
- One refinement pass on the final artifact.

## Bring-your-own-task rules (both tracks)
The task must be: (a) real — from your actual backlog; (b) yours — you own the outcome; (c) completable to *one artifact* in 90 minutes. Sanitize before starting.

**Backup tasks** (if someone arrives empty-handed): draft a job description; turn the provided claims.csv into a QBR summary; write an onboarding one-pager from the provided onboarding.csv; produce a status update email from the fictional transcript; document one team process you know by heart and let AI interrogate the gaps.

## Debrief preparation (last 10 min of lab)
Fill in, ready to show:
1. The task, in one sentence.
2. Your first prompt (verbatim).
3. The refinement that mattered most (verbatim).
4. The artifact.
5. One thing you had to correct — and how you caught it.
