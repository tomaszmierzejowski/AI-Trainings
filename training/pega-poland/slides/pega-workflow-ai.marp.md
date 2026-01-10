---
marp: true
theme: default
paginate: true
---

# Pega Workflow AI (Poland)
- Intake → triage → NBA → fulfillment → feedback
- Fictional PL/EN data only
Notes: Tailored to Krakow delivery/presales.

---
# Agenda
- Target flow & domains
- Pega assets
- GenAI touchpoints
- Governance
- Demo plan
Notes: 45–60 minutes.

---
# Target Flow (Docelowy przepływ)
- Intake, triage, decision, action, feedback
- Domains: claims, onboarding, service
Notes: Anchor to local use cases; Polish user text optional.

---
# Pega Assets (Zasoby)
- App Studio templates, data objects, personas
- Prediction Studio scoring; Decisioning arbitration
Notes: Template first; intelligence later.

---
# GenAI Touchpoints (GenAI)
- Classify intake; extract fields
- Draft notes; summarize interactions
- Outputs bounded (JSON/short summaries)
Notes: No irreversible decisions by LLM.

---
# Governance (Nadzór)
- Access groups; masked data pages
- Audit logs; approved endpoints
- HITL for high-risk changes
Notes: Client endpoint list required.

---
# Demo Plan (Plan demo)
- Email intake → case type + routing
- NBA suggestion → summary note
- KPIs: cycle time, SLA hits, CSAT
Notes: Use fictional data; bilingual user text where needed.

---
# Wrap
- Structured outputs + logging
- Start with highest-friction step
- Iterate with feedback and golden sets
Notes: Point to labs and prompt packs.
