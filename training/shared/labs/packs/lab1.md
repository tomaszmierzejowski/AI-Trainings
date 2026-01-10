# Lab 1 Prompt Pack — Case Intake & Triage (Shared)

## Prompt (final)
You are a Pega consultant. Classify the inbound message into a case_type (claims, onboarding, service) and propose routing_queue. Extract customer_type, product, urgency (low/med/high), and channel. Return JSON array with: case_type, routing_queue, confidence (0–1), rationale (<=35 words).

Queues: claims_intake, onboarding_ops, service_care.

Safety: fictional data only; no PII; cap rationale length.

## Test Cases (10)
| id | message | expected_case_type | expected_queue |
|----|---------|--------------------|----------------|
|1|"Car accident, airbags deployed, need tow"|claims|claims_intake|
|2|"Open checking account; student; ID ready"|onboarding|onboarding_ops|
|3|"Password reset not working on portal"|service|service_care|
|4|"Broken pipe in kitchen; urgent claim"|claims|claims_intake|
|5|"Upgrade to premium card; existing client"|onboarding|onboarding_ops|
|6|"Double charge on invoice; please refund"|service|service_care|
|7|"Minor fender bender, photos attached"|claims|claims_intake|
|8|"Set up payroll direct deposit"|onboarding|onboarding_ops|
|9|"Outage in mobile app; error 500"|service|service_care|
|10|"Travel claim: lost luggage, reference ABC123"|claims|claims_intake|

## Expected Output Shape
[
  {
    "case_type": "claims",
    "routing_queue": "claims_intake",
    "confidence": 0.0,
    "rationale": "..."
  }
]

## Checkpoints
- JSON valid; confidence present; rationale <=35 words.
- Queues only from list; case_type only allowed values.
- ≥80% test cases correct.
