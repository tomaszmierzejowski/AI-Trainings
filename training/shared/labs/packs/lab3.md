# Lab 3 Prompt Pack — Low-Code Case Prototype + UI Scaffold (Shared)

## Prompts
**UI Mock (MagicUI/Lovable)**
Create an intake form for a claims case with fields: policy_id (text), claim_type (dropdown), amount (currency), severity (low/med/high), channel (email/chat/web), description (textarea). Add validation and helper text. Use fictional data only.

**Routing Notes (Cursor/ChatGPT)**
Summarize routing rules: if severity=high or amount>5000 -> queue=claims_high; else claims_std. Add SLA hours: high=4, std=24.

**Stakeholder Summary**
Summarize the prototype in <=180 words; include scope, data used, routing, and next steps. English; add one Polish sentence for user-facing text.

## Test Cases (10 fictional inputs)
1) policy P-1001, claim_type auto, amount 1200, severity low, channel email.
2) policy P-1010, auto, amount 7800, severity high, channel email.
3) policy P-1005, auto, amount 4200, severity med, channel chat.
4) policy P-1006, home, amount 15000, severity high, channel phone.
5) policy P-1009, home, amount 2200, severity med, channel web.
6) policy P-1008, travel, amount 2500, severity med, channel email.
7) policy P-1014, home, amount 4000, severity med, channel chat.
8) policy P-1012, travel, amount 1300, severity med, channel chat.
9) policy P-1015, travel, amount 900, severity low, channel email (Polish text).
10) policy P-1017, home, amount 7000, severity high, channel email.

## Expected Outputs
- UI mock includes all fields with validations and helper text.
- Routing notes map each case to claims_high (2,4,10) or claims_std (others).
- Summary <=180 words; one Polish sentence for user-facing copy.

## Checkpoints
- No real data; only fictional values.
- Validation present for required fields and formats.
- Routing notes include queues and SLA hours.
