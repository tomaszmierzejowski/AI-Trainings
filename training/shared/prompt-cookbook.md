## Prompt Cookbook (Shared)

### Format
- Provide: role, goal, input, output format, constraints, few-shot examples (fictional), and safety notes.
- Keep outputs structured (JSON/table) when driving routing/eligibility.

### BA / Consultant
**Stage description & ACs**
Instruction: "You are a business analyst. Draft 3 stage descriptions and 5 acceptance criteria for <case type>. Keep user text concise."
Output: bullets; note assumptions; add Polish UI labels only if user-facing.
Safety: fictional data only; no PII.

**Workshop playback summary**
Instruction: "Summarize this workshop transcript into decisions, risks, actions. Output JSON with decisions[], risks[], actions[]."

### Sales Engineer
**Persona + demo storyline**
Instruction: "Create a persona (name, role, goal, pain) and a demo storyline highlighting case intake, decisioning/NBA, and AI summary. Output JSON."

**Follow-up email**
Instruction: "Draft a concise follow-up email after a demo. Include next steps, owners, and date options. 120 words max."

### System Architect
**Explain-this-rule**
Instruction: "Explain this Pega rule in plain English and propose a safer version. List potential regressions."

**Test generation**
Instruction: "Generate 6 edge-case tests for this rule. Output a table: test_id, intent, input, expected_result."

### Cross-role
**Case classification + routing**
Instruction: "Classify the message into case_type (claims/onboarding/service) and propose routing_queue with confidence 0–1 and one-sentence rationale. Output JSON."
Few-shot: provide 2–3 fictional examples.

**Meeting notes**
Instruction: "Summarize the meeting into agenda, decisions, actions, owners, due_dates. Output JSON arrays."  

Safety reminders: approved endpoints only; redact PII; log prompts/responses; keep word limits to reduce leakage.
