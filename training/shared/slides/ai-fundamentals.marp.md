---
marp: true
theme: default
paginate: true
---

# AI Fundamentals (Enterprise)
- Pegasystems Poland | Shared deck
- English-first; Polish titles in () where helpful
- Fictional data only
Notes: Welcome; hybrid audience; emphasize governance + speed.

---
# Agenda (Porządek)
- Why AI + low-code now
- Model types & grounding
- Patterns & risks
- Metrics & Pega tie-ins
Notes: Set expectations; 45–60 minutes module.

---
# Why AI + Low-Code Now (Dlaczego teraz?)
- Faster discovery + build; guardrails via low-code
- Text-heavy steps: intake, triage, summarize, decide
- KPIs: cycle time, SLA hits, CSAT/NPS, conversion
Notes: Tie to Krakow teams delivering faster with safety.

---
# Model Types (Typy modeli)
- LLMs: language + reasoning; not a database
- Predictive models: structured scoring (propensity, risk)
- Retrieval: fetch facts at request time
Notes: Stress fusion: LLM understand, prediction score, retrieval for truth.

---
# Grounding > Fine-Tuning (Ugruntowanie > trenowanie)
- Default: retrieval + instructions
- Fine-tune only if narrow, stable, high-volume, approved
- Keep prompts/data fictional in training
Notes: Highlight freshness and safety of grounding.

---
# Enterprise Patterns (Wzorce)
- Classify, extract, summarize, route, recommend, draft
- Agentic: plan → act → check; HITL on high-risk
- Structured outputs (JSON/table) for routing/eligibility
Notes: Map to email intake → classify → route → summarize.

---
# Risks & Mitigations (Ryzyka)
- Hallucination, prompt injection, leakage, bias
- Mitigate: allow/deny lists, redaction, filters, logging, HITL
Notes: Give quick prompt-injection example and stripping URLs/HTML.

---
# Metrics (Metryki)
- Quality: precision/recall, factuality
- Impact: cycle time, SLA adherence, CSAT
- Offline tests + inline monitors; golden sets 10–20 cases
Notes: Connect to business KPIs; keep golden sets current.

---
# Pega Tie-ins (Pega kontekst)
- Process AI for signals/predictions
- Decisioning for NBA arbitration
- GenAI connectors to classify/summarize/draft
- Guardrails: access groups, masked data pages, logging
Notes: AI augments decisioning; does not bypass guardrails.

---
# Wrap
- Start with one friction point and a bounded LLM task
- Keep outputs structured; log everything
- Measure both quality and business impact
Notes: Invite questions; point to lab and cookbook.
