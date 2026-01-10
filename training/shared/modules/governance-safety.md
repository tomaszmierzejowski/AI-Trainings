## Governance & Safety

### Slides
- Slide 1 — Principles (Polish: Zasady)  
  - Least privilege; data minimization; auditability.  
  - Approved endpoints only; no real customer data in prompts.  
  - Speaker notes: Governance is a feature; set this tone.

- Slide 2 — Risks (Polish: Ryzyka)  
  - Hallucination, prompt injection, leakage, bias, overreliance.  
  - Speaker notes: Give a quick example of prompt injection (malicious instructions in input).

- Slide 3 — Controls (Polish: Kontrole)  
  - Allow/deny lists; PII redaction; content filters; output validation.  
  - Size caps; remove URLs/HTML; enforce formats.  
  - Speaker notes: Mention automated redaction where available; fall back to placeholders.

- Slide 4 — Process (Polish: Proces)  
  - Approvals, RACI, change tickets, rollback plans.  
  - Golden sets + abuse cases; regression prompts.  
  - Speaker notes: Keep evidence of tests and sign-offs.

- Slide 5 — Logging & Monitoring (Polish: Logowanie)  
  - Log prompts/responses, model version, decision, user, dataset.  
  - Monitors: drift, toxicity, policy hits.  
  - Speaker notes: Stress retention and access control on logs.

- Slide 6 — Pega Tie-ins (Polish: Pega)  
  - Access groups; masked data pages; decisioning governance.  
  - Guardrail warnings; centralized connectors; audit trails.  
  - Speaker notes: Use existing Pega guardrails first; AI should not bypass them.

### Audiobook Script (6–7 min + Q&A)
"Safety is designed in, not bolted on. Start with least privilege and data minimization—send only what the model needs and only to approved endpoints. Risks include hallucination, prompt injection, leakage, and bias. We counter with allow/deny lists, redaction, format constraints, and human checkpoints for high-stakes steps.  
Process matters: require approvals for new prompts or model changes, track them in tickets, and keep golden sets and abuse cases to test regressions. Logging is mandatory: prompts, responses, model versions, user, and decisions. Monitor for drift and policy violations.  
In Pega, lean on access groups, masked data pages, decisioning governance, and guardrail warnings. Centralize GenAI connectors, log usage, and keep humans in the loop where risk is high. This keeps AI useful, compliant, and explainable."  

Likely Q&A:
- Q: What if a user pastes sensitive data?  
  A: Use redaction, enforce placeholders, and block outbound calls that carry PII; add user training and logging.  
- Q: How do we audit AI decisions?  
  A: Log prompts, responses, model version, and resulting decisions; tie logs to cases for traceability.  
- Q: How to test against prompt injection?  
  A: Include abuse cases in golden sets, strip untrusted HTML/URLs, constrain inputs, and validate outputs before acting.  
