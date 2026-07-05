# Module 4 — From Writing Code to Writing Specifications (Trainer Guide)

**Total time:** half-day (≈3.5 h incl. break) · **Audience note:** invite leaders for the first hour (slides 1–8); the deep-dive (9–20) is for technical staff · **Materials:** rules-file templates (CLAUDE.md / AGENTS.md / .cursorrules), spec template handout, sample codebase, MCP demo environment (test before the session — have a recorded fallback)

## Timing plan

| Segment | Slides | Time |
|---|---|---|
| Provocation + what stays scarce | 1–5 | 30 min |
| Specification design + rules files | 6–8 | 35 min |
| — leaders may exit / break — | | 15 min |
| MCP + A2A + the two layers | 9–13 | 40 min |
| Production pipeline + economics + failure modes | 14–16 | 25 min |
| Career reframe | 17 | 10 min |
| Exercise + debrief | 18–19 | 60 min |
| Recap + 90-day path | 20 | 10 min |

## Speaker notes by segment

### Slides 1–3 (The provocation)
Badge discipline is the persuasion strategy here: announce loudly that slides 2–3 are OPINION. "For ninety minutes today I'm going to argue a position. I'll mark exactly where the evidence ends and my conviction begins — because that's the standard this whole program runs on." This buys you the right to be provocative without losing the skeptics.
The Gutenberg analogy lands best delivered with respect for the craft being disrupted: the scribes were the *most* literate people of their age — that's exactly why some of them became the first publishers.

### Slides 4–5 (What stays scarce)
This is the emotional pivot of the module — from threat to plan. Slow down. Ask the room: "How much of your last week was typing, and how much was context, judgment, verification, decomposition?" Most senior people discover they're already mostly an orchestrator with a typing habit.

### Slides 6–8 (Specification design)
The prompt-vs-spec contrast (slide 6) should be run live: same task, one-liner vs. full spec, side-by-side outputs. Let the delta speak.
Slide 7's worked example: use a spec you have actually used. Walk it slowly — the **non-goals** section always surprises people ("you have to tell it what NOT to do?" — yes, exactly like a contractor).
Slide 8 is a physical takeaway moment: distribute the templates and say the fishing-rod line: "This is the rod. You'll adapt it to your repo this week — 90-day path, step one."

### Slides 9–13 (MCP + A2A)
Keep protocol detail proportional to the audience — the *behavioral* meaning is the mandatory content, the wire format is not. The two anchor sentences: "MCP gives an agent hands. A2A gives agents colleagues." and "You don't manage the typing. You manage the org chart."
MCP facts you can state with confidence: Anthropic, November 2024, open standard, industry-wide adoption. A2A facts: Google, April 2025, now Linux Foundation governance, capability discovery via agent cards. If asked which will "win": "They're complementary layers, not competitors — one connects agents to tools, the other connects agents to each other. Betting on open standards is the safe move either way."
Demo risk management: MCP demos are live-demo-fragile. Test the same morning; keep a recording as fallback; a smooth recording beats a broken live demo every time.

### Slides 14–16 (The production pipeline — your strongest material)
This is where three modules of metrics get their explanation: the numbers the audience has seen since Module 1 (20 apps/3 weeks, 4–8×, 143 rules @94%) were produced *by the thing this module teaches* — staged specialist agents with human verification gates. Say it explicitly: "You've been looking at orchestration's output for two days. This is the machine."
Slide 16 (failure modes) is your credibility peak — do not rush it. Field-honest notes: error propagation is the nastiest (one bad extraction quietly poisons everything downstream — which is *why* gates sit between stages, not just at the end); black-box outputs are a real adoption killer — internal enterprise feedback on early discovery tooling was precisely "too technical, too much of a black box" — evidence tagging exists because stakeholders must be able to audit, not believe. Do not attribute that feedback to any named organization.

### Slide 17 (Career reframe)
Land it personally, not corporately: "Nobody in this room is being replaced. The role is being recompiled — and everything in the new build is something you already do in the best hours of your week."

### Slides 18–19 (Exercise)
The spec-swap twist is where the learning happens: pairs run *each other's* specs, and every ambiguity becomes a visible agent misbehavior. During debrief ask: "Whose agent did something technically-compliant-but-wrong? Read us the spec line that allowed it." Review against acceptance criteria, not taste — enforce this; it's the whole point.

### Slide 20 (90-day path)
Concrete and small: rules file (weeks 1–2), spec-first habit (3–6), one two-stage pipeline with a gate (7–12). Warn against skipping to stage three: "A pipeline built by someone who hasn't internalized spec-writing is a very fast ambiguity amplifier."

## Discussion prompts
1. "What fraction of your last code review was about *what* was built vs. *how* it was typed?"
2. "Which recurring task on your team is the best first candidate for a two-stage pipeline — and what would the verification gate check?"
3. "What would your CLAUDE.md / rules file forbid an agent from ever touching?"

## Likely objections & responses
- **"AI code quality isn't good enough for our standards."** — "Under a one-line prompt, agreed. Under a spec with acceptance criteria and your rules file, test it before concluding. The 4-day migration kept 92% of the original code and shipped with zero regressions — quality came from constraints plus verification, not from hope."
- **"This deskills juniors — who becomes the next senior?"** — Take it seriously; it's the best objection in the field. "Juniors must still learn to verify, and verification requires understanding. What changes is the curriculum: less syntax, more system thinking, earlier exposure to specs and review. The apprenticeship moves up the stack — it doesn't disappear." (OPINION — label it.)
- **"MCP/A2A will be obsolete in a year."** — "Specific protocols may evolve; the *layers* — agent-to-tools and agent-to-agent — are here to stay, and both current standards are open and multi-vendor. The skill being taught is orchestration; protocols are its current syntax."
- **"We tried an AI pipeline and stakeholders ignored the output."** — "Was the output auditable? The single biggest field lesson: technical black-box output gets ignored no matter how correct it is. Evidence tagging — every claim traceable to a source line — is what converts output into decisions."
- **"Isn't this just waterfall — big spec up front?"** — "A spec here is per-task and hours-scale, not per-project and months-scale. It's closer to a good ticket than to a requirements phase. You iterate specs the way you iterate prompts — Module 2's habit, one level up."

## Failure modes for the trainer
- Letting the provocation slides run unbadged — skeptics disengage permanently if opinion arrives dressed as fact.
- Protocol-lecturing. If you're explaining JSON-RPC framing to a mixed room, you've lost the mindset thread. Behavioral meaning first; spec pointers for the curious.
- Presenting the pipeline as magic. The failure-modes slide is mandatory, never cut for time — it's the difference between evangelism and engineering.
