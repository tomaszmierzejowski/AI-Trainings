# Module 4 — From Writing Code to Writing Specifications: MCP, A2A, and Orchestration (Slide Outline)

**Format:** half-day with exercise · **20 slides** · Audience: technical leads, architects, senior engineers (leaders welcome for slides 1–8)
**Design intent:** the career-reframe module. Opinion slides are explicitly badged OPINION — this is the program's provocative chapter, and its honesty about that is the persuasion strategy.

---

**Slide 1 — Title**
"From Writing Code to Writing Specifications"
Subtitle: *The shift from manual coding to specification design and agent orchestration.*

**Slide 2 — The provocation** *(OPINION — clearly badged)*
"Code is becoming a commodity. The specification is becoming the product."
One line: "This slide is a position, not a finding. By the end of the module you'll have the evidence to argue with it — or with me."

**Slide 3 — The Gutenberg analogy** *(OPINION)*
Before print: scribes' craft was penmanship. After: writing mattered more than handwriting.
Hand-crafted code : AI-generated code :: illuminated manuscripts : printed books.
One line: "The scribes didn't disappear. The ones who became *authors* thrived."

**Slide 4 — What actually stays scarce**
Four durable skills: **context** (knowing what the business needs), **judgment** (knowing what good looks like), **verification** (proving it's right — Module 3), **orchestration** (designing who/what does which step).
One line: none of these are typing.

**Slide 5 — The orchestrator role**
Definition: someone who decomposes work into agent-executable steps, writes the specifications those agents consume, designs the verification gates between steps, and owns the result.
One line: "From typist to conductor."

**Slide 6 — Specification design: the new core skill**
A prompt is a request. A specification is a contract: **goal, constraints, acceptance criteria, examples, non-goals.**
Visual: same task as a one-line prompt vs. a 15-line spec, with the output quality delta.

**Slide 7 — Anatomy of a good spec (worked example)**
Live walk-through of a real spec: context block → task → constraints ("must not touch the public API") → acceptance criteria ("all existing tests pass; new endpoint returns 404 for unknown ids") → examples → non-goals.
One line: "Everything you'd tell a contractor. Written down. Once."

**Slide 8 — Standing specifications: rules files** *(takeaway)*
CLAUDE.md / AGENTS.md / .cursorrules — the spec you write once and every agent session inherits: project conventions, forbidden zones, verification commands.
Participants receive working templates (from the AI Coaching template set).
One line: "Your project's constitution, readable by every agent you'll ever hire."

--- *(leaders may drop off here; technical deep-dive begins)* ---

**Slide 9 — The integration problem**
Agents are only as useful as what they can reach. Without standards: N tools × M systems = N×M custom integrations.
Visual: the tangle diagram.

**Slide 10 — MCP: Model Context Protocol** *(VERIFIED landscape facts)*
Open standard introduced by Anthropic (Nov 2024), since adopted across the major vendors. One protocol for connecting AI applications to tools, data, and systems — "USB-C for AI."
What it means behaviorally: your agent can read your Jira, your repo, your database — through one standard socket, under the permissions you grant (least privilege — Module 3).

**Slide 11 — MCP in daily work (demo)**
Live or recorded: an agent using an MCP server to query a (fictional) issue tracker and produce a grounded status report — citing real ticket ids.
One line: "Grounding, industrialized."

**Slide 12 — A2A: Agent2Agent protocol**
Open protocol announced by Google (April 2025), now under the Linux Foundation. Lets *agents discover and talk to other agents* — publish capabilities ("agent card"), exchange tasks, cooperate across vendors.
One line: "MCP gives an agent hands. A2A gives agents colleagues."

**Slide 13 — The two layers together**
Diagram: You (specifier/verifier) → orchestrator agent → [A2A] specialist agents → [MCP] tools & systems of record.
One line: "You don't manage the typing. You manage the org chart."

**Slide 14 — This is not theory: the discovery pipeline** *(VERIFIED)*
The author's production pipeline for legacy-system discovery: staged, specialized agents — ingestion → semantic analysis → security scan → compliance mapping → synthesis — with human verification gates between stages.
Results (from Modules 1–3, now explained): 20 apps in 3 weeks; 4–8× faster understanding (Proof of Scale); 100+ business rules extracted with source-traceable findings.

**Slide 15 — The economics** *(VERIFIED)*
Same discovery scope: ~3 weeks orchestrated vs. ~14 weeks traditional; ≈87% cost reduction on the reference engagement (discovery and analysis phase only).
One line: "This is why the orchestrator role exists: the pipeline doesn't run itself."

**Slide 16 — Where orchestration fails (honesty slide)**
Field-observed failure modes: error propagation between stages (one bad extraction poisons downstream agents); context-window overflow on large systems; black-box outputs that stakeholders can't trust or act on; over-engineering — a pipeline where a prompt would do.
One line: "Every one of these is mitigated by the same two things: verification gates and evidence tagging."

**Slide 17 — The career reframe**
What to stop over-investing in: syntax fluency, boilerplate speed, memorizing APIs.
What to double down on: domain context, specification writing, verification design, system decomposition, agent-pipeline debugging.
One line: "Nobody in this room is being replaced by AI. The role is being *recompiled*."

**Slide 18 — Exercise: spec → agent → review**
Pairs: write a specification (template provided) for a task on the sample codebase → hand it to an agent (Cursor agent mode or Claude) → review the result *against the spec's acceptance criteria*, not against taste.
Twist: pairs then swap specs and run each other's — ambiguity becomes visible instantly.

**Slide 19 — Exercise debrief**
Surface: which spec ambiguities the agent exploited; which acceptance criteria caught problems; what a second iteration of the spec fixed.
One line: "You just did the job. That was orchestration."

**Slide 20 — Recap + 90-day orchestrator path**
Week 1–2: rules file in your main repo. Week 3–6: every non-trivial task starts with a written spec. Week 7–12: one two-stage pipeline with a verification gate, on a real recurring task.
Bridge: "Module 5 makes all four modules survive contact with your calendar."
