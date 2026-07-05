# Module 4 Handout — Specification Template (+ worked example)

A prompt is a request. A specification is a contract. Use this template for any task you hand to an agent that would take you more than ~30 minutes by hand. Standing rules that apply to *every* task (conventions, forbidden zones, verify commands) belong in your rules file instead — working templates for CLAUDE.md / AGENTS.md / .cursorrules are provided separately (adapted from the AI Coaching template set).

---

## The template

```
# SPEC: <short imperative title>

## Context
<2–5 sentences: what this system/document is, why this task exists now,
what the agent cannot infer on its own. Business context beats technical
context when you can only afford one.>

## Goal
<One sentence. If you need two, you have two specs.>

## Constraints
- <What must NOT change (public APIs, existing behavior, file X, tone Y)>
- <Technology / style / length boundaries>
- <Data rules: what must never appear in the output>

## Acceptance criteria
- [ ] <Testable statement — a yes/no check, not a vibe>
- [ ] <"All existing tests pass" belongs here for code>
- [ ] <For documents: "every claim carries a source reference">

## Examples
<One input→output pair showing the expected shape/quality.
For code: a sample call and expected response.
For documents: 3 lines of the tone/format you want.>

## Non-goals
- <The adjacent thing the agent will be tempted to do — forbidden explicitly>
- <Scope you're deferring on purpose>

## Verification
<The exact command / procedure the result will be checked with.
If you can't write this line, the task belongs in a harder quadrant
of the trust matrix — decompose it until you can.>
```

---

## Worked example (document task, non-technical)

```
# SPEC: Q2 status brief for the steering committee

## Context
Quarterly steering meeting for the platform migration program. Audience
is non-technical executives who read only the first half-page. Inputs:
the attached sprint reports (6 files) and the risk register export.

## Goal
Produce a one-page status brief the program director can send unedited.

## Constraints
- Max 400 words; no jargon; no acronyms without expansion on first use.
- Only information present in the attached inputs — no outside knowledge.
- No individual names in the risk section (roles only).

## Acceptance criteria
- [ ] Every number in the brief appears verbatim in an attached input.
- [ ] Status verdict (green/amber/red) is stated in line 1 with a reason.
- [ ] Top 3 risks each carry: impact, owner role, next action, date.
- [ ] Fits one A4 page at 11pt.

## Examples
Opening line style: "Program status: AMBER — data-migration rehearsal
slipped two weeks; go-live date unchanged."

## Non-goals
- Do not propose new mitigations (the committee decides those).
- Do not restate the full risk register — top 3 only.

## Verification
Reviewer cross-checks every number against inputs (Module 3 spot-check:
numbers, dates, names first), then reads it aloud in under 3 minutes.
```

---

## Exercise instructions (spec → agent → swap)

1. **Write** (20 min): pick the marked task on the sample codebase (Track A) or the document task (Track B). Fill every section — an empty Non-goals section means you haven't imagined the failure yet.
2. **Run** (15 min): hand the spec verbatim to the agent (Cursor agent mode / Claude). Do not coach it mid-run; let the spec do the work.
3. **Review** (10 min): score the result **only against your acceptance criteria** — not against taste. Note criteria that turned out untestable.
4. **Swap** (15 min): exchange specs with your pair and run *theirs*. Every place their agent did something technically-compliant-but-wrong is an ambiguity — write it down; that list is the lesson.
5. **Debrief:** bring your best ambiguity: the spec line, what the agent did, and the one-line fix.
