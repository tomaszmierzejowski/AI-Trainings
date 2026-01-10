## Pega Workflow AI (Poland Delivery)

### Slides
- Slide 1 — Target Flow (Polish: Docelowy przepływ)  
  - Intake → triage → NBA → fulfillment → feedback.  
  - Domains: claims, onboarding, service (fictional).  
  - Speaker notes: Tie to Krakow delivery patterns.

- Slide 2 — Pega Assets (Polish: Zasoby Pega)  
  - App Studio templates, data objects, personas.  
  - Prediction Studio for scoring; Decisioning for arbitration.  
  - Speaker notes: Start template first; AI later.

- Slide 3 — GenAI Touchpoints (Polish: GenAI)  
  - Classify intake, extract fields, draft notes, summarize interactions.  
  - Outputs bounded: JSON for routing; short summaries.  
  - Speaker notes: No irreversible decisions by LLM; keep humans for high risk.

- Slide 4 — Governance (Polish: Nadzór)  
  - Access groups, masked data pages, audit logs, approved LLM endpoints.  
  - Logging of prompts/responses; no real data.  
  - Speaker notes: Mention client-specific endpoint list.

- Slide 5 — Demo Plan (Polish: Plan demo)  
  - Email intake → case type + routing → NBA suggestion → summary note.  
  - KPI lens: cycle time, SLA hits, CSAT.  
  - Speaker notes: Use Polish examples for end-user text; keep specs in English.

### Audiobook Script (6–7 min + Q&A)
"For the Krakow teams, we focus on fast, governed delivery. The flow is intake, triage, decision, action, and feedback. Intake uses an LLM to classify and extract fields from an email or form. Triage uses a prediction to score urgency. Decisioning runs next-best-action with constraints. Action drafts the response or case note. Feedback logs the outcome to improve prompts and models.  
We start in App Studio with a case template, then attach Prediction Studio scores and Decision strategies. GenAI connectors classify and summarize but never make irreversible choices; keep outputs structured as JSON for routing and short summaries for people.  
Use fictional Polish/English data for demos. Access groups, masked data pages, logging, and approved LLM endpoints keep us compliant. This pattern fits claims, onboarding, and service and can be adapted quickly per client."  

Likely Q&A:
- Q: Can the LLM decide routing?  
  A: It can propose routing with confidence, but final routing should be in rules/decision tables.  
- Q: How do we keep it bilingual?  
  A: Specs and logic in English; user-facing text can include Polish variants; keep prompts clear about language.  
- Q: What logs do we keep?  
  A: Prompts, responses, model version, user, decision taken; store without PII and under approved retention.  
