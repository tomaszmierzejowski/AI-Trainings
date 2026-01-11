## Pega Workflow Acceleration (Outcomes)

### Slide Outline
- **The Goal**: Remove friction from Intake, Triage, and Action.
- **KPIs**: Reduce AHT by 20%, improve Classification Accuracy to 90%.
- **Pattern**:
  1. **Intake**: LLM extracts structured data (JSON) from messy text.
  2. **Triage**: Pega rules + LLM confidence score routing.
  3. **Action**: GenAI drafts the response/summary for human review.

### Speaker Notes
- **Friction**: "Where does the process stall? Usually reading/classifying or writing responses."
- **Intake**: "Don't just OCR. Extract intent. 'I want a refund' vs 'Where is my refund'."
- **Triage**: "Use the LLM to suggest, but let Pega rules decide. If Confidence < 0.8, route to human."
- **Action**: "Never auto-send without review. Draft the email, let the agent click send."

### Audiobook Script (5 min)
"We apply AI to accelerate the Pega workflow, not replace it.
Focus on three points: Intake, Triage, and Action.
At Intake, use an LLM to turn unstructured emails into structured JSON data. Extract the Intent, the Entities, and the Urgency.
At Triage, combine Pega's deterministic rules with the LLM's confidence score. If the model is 95% sure, automate. If 60%, route to a human expert.
At Action, use GenAI to draft the reply or the case summary. This saves the agent 5 minutes per case.
Multiply that by 1000 cases, and you have massive ROI. Always keep a human in the loop for the final click."
