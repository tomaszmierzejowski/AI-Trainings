## Prompt Cookbook (Pega Poland)

### Format
- Provide: role, goal, input, output format, constraints, few-shot examples (fictional), safety notes.
- English-first; Polish labels only for user-facing text.

### BA / Consultant (Krakow)
**Stage description & ACs**
Instruction: "Draft 3 stage descriptions and 5 acceptance criteria for <case type>. Keep UI text concise; add Polish labels in parentheses where user-facing." Output: bullets.

**Playback summary**
Instruction: "Summarize workshop transcript into decisions, risks, actions. Output JSON with decisions[], risks[], actions[]."

### Sales Engineer
**Persona + demo storyline (Pega features)**
Instruction: "Create a persona and demo storyline showing case intake, decisioning/NBA, GenAI summary. Output JSON."

**Follow-up email**
Instruction: "Draft a follow-up email after a demo. Include next steps, owners, dates. 120 words max."

### System Architect
**Explain-this-rule**
Instruction: "Explain this Pega rule and propose a safer refactor. List potential regressions."

**Test generation**
Instruction: "Generate 6 edge-case tests for this rule. Output table: test_id, intent, input, expected_result."

### Cross-role
**Case classification + routing**
Instruction: "Classify message into case_type (claims/onboarding/service) and propose routing_queue with confidence 0–1 and one-sentence rationale. Output JSON; add Polish queue label if user-facing."

**Meeting notes**
Instruction: "Summarize meeting into agenda, decisions, actions, owners, due_dates. Output JSON arrays."  

Safety: approved endpoints only; redact PII; log prompts/responses; fictional data only.
