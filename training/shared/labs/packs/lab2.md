# Lab 2 Prompt Pack — Real-Time Decisioning Mock (Shared)

## Prompt (final)
Draft a next-best-action table for actions: retain, upsell, service_recover. Inputs: intent, value_tier (low/med/high), risk_flag (true/false), channel, sentiment (neg/neu/pos). For each action, output eligibility (boolean), priority (1=highest), and rationale <=20 words. Output JSON array.

Guardrails: block upsell if risk_flag=true; prioritize retain for high value_tier; only one action at priority 1.

## Test Scenarios (10)
| id | intent | value_tier | risk_flag | channel | sentiment | expected_top_action |
|----|--------|------------|-----------|---------|-----------|---------------------|
|1|cancel|high|false|email|neg|retain|
|2|upgrade|high|false|chat|pos|upsell|
|3|complaint|med|false|phone|neg|service_recover|
|4|info|low|false|web|neu|upsell|
|5|complaint|high|true|email|neg|service_recover|
|6|cancel|med|true|phone|neg|retain|
|7|upgrade|med|true|chat|pos|retain|
|8|info|high|false|email|pos|upsell|
|9|complaint|low|false|web|neg|service_recover|
|10|cancel|high|true|phone|neg|retain|

## Expected Output Shape
[
  {
    "action": "retain",
    "eligibility": true,
    "priority": 1,
    "rationale": "..."
  }
]

## Checkpoints
- Exactly one action with priority 1 per scenario.
- Guardrails respected (no upsell when risk_flag=true).
- Rationale <=20 words; JSON valid.
