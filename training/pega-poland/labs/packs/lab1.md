# Lab 1 Prompt Pack — Email Intake & Routing (Pega Poland)

## Prompt (final)
You are a Pega consultant. Classify the email into case_type (claims, onboarding, service) and propose routing_queue. Extract customer_type, product, urgency (low/med/high), channel. Return JSON with confidence (0–1) and rationale <=35 words. Add Polish queue label only if user-facing.

Queues: claims_intake_pl, onboarding_ops_pl, service_care_pl.

## Test Cases (10)
| id | message | expected_case_type | expected_queue |
|----|---------|--------------------|----------------|
|1|"Airbags deployed, need tow, policy P-1010"|claims|claims_intake_pl|
|2|"Set up new checking account; student"|onboarding|onboarding_ops_pl|
|3|"Password reset not working"|service|service_care_pl|
|4|"Pipe burst in kitchen; urgent"|claims|claims_intake_pl|
|5|"Upgrade to premium card; existing client"|onboarding|onboarding_ops_pl|
|6|"Double charge on invoice"|service|service_care_pl|
|7|"Minor bumper damage; photos attached"|claims|claims_intake_pl|
|8|"Set payroll direct deposit"|onboarding|onboarding_ops_pl|
|9|"Mobile app outage; error 500"|service|service_care_pl|
|10|"Lost luggage on trip; ref ABC123"|claims|claims_intake_pl|

## Expected Output Shape
[
  {
    "case_type": "claims",
    "routing_queue": "claims_intake_pl",
    "confidence": 0.0,
    "rationale": "..."
  }
]

## Checkpoints
- JSON valid; rationale <=35 words; queues limited to list.
- ≥80% accuracy on test cases.
- No PII or real data.
