---
marp: true
theme: default
paginate: true
---

# Governance & Safety
- Safety is a feature
- English-first; Polish titles optional
Notes: Lead with principles; keep crisp.

---
# Agenda
- Principles
- Risks
- Controls
- Process
- Logging & monitoring
- Pega tie-ins
Notes: 30–40 minutes; link to checklist.

---
# Principles (Zasady)
- Least privilege; data minimization
- Approved endpoints only
- Auditability by default
Notes: Set tone: governed by design.

---
# Risks (Ryzyka)
- Hallucination; prompt injection
- Data leakage; bias; overreliance
Notes: Show quick injection example.

---
# Controls (Kontrole)
- Allow/deny lists; PII redaction
- Content filters; output validation
- Size caps; strip URLs/HTML
Notes: Mention placeholders if no redaction tool.

---
# Process (Proces)
- Approvals + RACI; change tickets
- Golden sets + abuse cases
- Rollback path defined
Notes: Evidence of tests and sign-offs required.

---
# Logging & Monitoring (Logowanie)
- Log prompt/response/model/user/decision
- Retention + access controls
- Monitors for drift/toxicity/policy hits
Notes: No PII in logs; align with policy.

---
# Pega Tie-ins
- Access groups; masked data pages
- Decisioning governance; guardrail warnings
- Centralized connectors; audit trails
Notes: AI should not bypass guardrails.

---
# Wrap
- Governed inputs/outputs; HITL on high risk
- Test with golden + abuse cases
- Log everything; review regularly
Notes: Point to governance checklist.
