---
marp: true
theme: default
paginate: true
---

# Prompting Power Skills
- Structure > luck
- English-first; Polish only for user-facing text
Notes: Focus on repeatable patterns and safety.

---
# Agenda (Porządek)
- Prompt formula
- Patterns that work
- Prompt ladders
- Safety
- Pega examples
Notes: 45–60 minutes; hands-on friendly.

---
# Prompt Formula (Formuła)
- Instruction → context → format → constraints → examples (optional)
- Keep concise; state role and audience
- Ask for structured outputs (JSON/table)
Notes: Show template; stress minimal but clear context.

---
# Patterns (Wzorce)
- Short chain-of-thought then clean answer
- Critique-and-revise loop
- Delimit inputs with fences
- Few-shot only when structure matters
Notes: Demo a short reasoning + final answer pattern.

---
# Prompt Ladders (Drabinka)
- Start coarse → test 5–10 cases → tighten
- Log versions in prompt cookbook
- Measure failures; fix one at a time
Notes: Encourage iteration with golden cases.

---
# Safety (Bezpieczeństwo)
- No real data; use placeholders
- Redact PII; approved endpoints only
- Log prompts/responses; cap rationale length
Notes: Remind audit and word limits reduce leakage.

---
# Pega Examples (Przykłady)
- Intake classification + routing JSON
- Stage summaries and AC drafts
- Decision table candidates
- Meeting notes to actions/owners
Notes: Tie each to labs and cookbook entries.

---
# Wrap
- Templates + ladders = reliability
- Keep outputs structured and short
- Store good prompts in the cookbook
Notes: Point to lab and prompt packs.
