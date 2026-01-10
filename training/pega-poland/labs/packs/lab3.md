# Lab 3 Prompt Pack — Low-Code Prototype + UI Mock (Pega Poland)

## Prompts
**UI Mock (MagicUI/Lovable)**
Create an intake form for onboarding with fields: applicant_id, product, kyc_flag, risk_score, region, channel, notes. Add validation and helper text. Use fictional data; labels in English with Polish in parentheses where user-facing.

**Routing Notes (Cursor/ChatGPT)**
Routing: if risk_score>0.6 or kyc_flag=true -> queue=onboarding_risk; else onboarding_std. SLA: risk=8h, std=24h.

**Stakeholder Summary**
Summarize prototype in <=180 words; include scope, data used, routing, next steps. English with one Polish sentence for user-facing text.

## Test Cases (10 fictional inputs)
1) A-2004, mortgage, kyc_flag=true, risk_score 0.65, region EMEA, channel email.
2) A-2003, retail-checking, kyc_flag=true, risk_score 0.18, region CEE, channel chat (Polish text).
3) A-2002, credit-card, kyc_flag=false, risk_score 0.41, region NA, channel web.
4) A-2007, credit-card, kyc_flag=false, risk_score 0.52, region NA, channel chat.
5) A-2009, mortgage, kyc_flag=true, risk_score 0.58, region EMEA, channel email.
6) A-2010, wealth, kyc_flag=true, risk_score 0.40, region NA, channel email.
7) A-2013, mortgage, kyc_flag=true, risk_score 0.62, region CEE, channel web (Polish).
8) A-2016, credit-card, kyc_flag=false, risk_score 0.37, region EMEA, channel email.
9) A-2018, wealth, kyc_flag=true, risk_score 0.32, region APAC, channel web.
10) A-2019, retail-checking, kyc_flag=true, risk_score 0.25, region CEE, channel chat (Polish).

## Expected Outputs
- UI mock includes all fields with validation and helper text (English/Polish labels).
- Routing notes map to onboarding_risk for (1,2,5,6,7,9,10) due to kyc_flag/risk; onboarding_std otherwise.
- Summary <=180 words; includes one Polish sentence.

## Checkpoints
- No real data; fictional only.
- Validation present; routing rules explicit with queues and SLA hours.
