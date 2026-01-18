## Pega Workflow Acceleration (Business Outcomes)

### Slides
- Slide 1 — The Friction Points (Polish: Punkty tarcia)
  - Intake (Reading/Classifying): Slow, manual, error-prone.
  - Triage (Routing): Bottleneck of expertise.
  - Action (Response): Repetitive typing.
  - Speaker notes: "AI solves the 'Blank Page' problem and the 'Data Entry' problem.
    - **Context**: Ask 'Who loves typing data from PDFs?' No hands go up."

- Slide 2 — Pattern 1: Intelligent Intake (Polish: Inteligentny wlot)
  - **Input**: Unstructured email/PDF.
  - **AI Task**: Extract Entities (Name, ID, Intent) -> JSON.
  - **Pega Action**: Map JSON to Clipboard.
  - **Result**: Case created in milliseconds, not minutes.
  - Speaker notes: "This is the 'OCR on steroids'. It reads intent, not just pixels."

- Slide 3 — Pattern 2: Confidence-Based Triage (Polish: Triage)
  - **AI Task**: Predict Case Type & Routing.
  - **Constraint**: If Confidence > 90%, Auto-route. Else, Human Workbasket.
  - **Safety**: Human-in-the-loop for low confidence.
  - **Result**: Experts focus only on hard cases.
  - Speaker notes: "We don't trust AI blindly. We trust it when it's sure."

- Slide 4 — Pattern 3: Generative Action (Polish: Generatywna akcja)
  - **AI Task**: Draft "Apology Email" or "Approval Note".
  - **Context**: Case History + Policy.
  - **User**: Reviews and clicks "Send".
  - **Result**: AHT (Average Handle Time) reduced by 30%.
  - Speaker notes: "The agent is the pilot; AI is the co-pilot drafting the flight plan."

- Slide 5 — The ROI Model (Polish: Model zwrotu z inwestycji)
  - Time Saved x Hourly Rate x Volume.
  - Example: 5 min/case x $50/hr x 10,000 cases = Massive savings.
  - Speaker notes: "Show this slide to your stakeholders. This is why we do AI."

- Slide 6 — Governance Overlay (Polish: Nadzór)
  - Audit every AI decision.
  - Version control your prompts.
  - Never bypass Pega security rules.
  - Speaker notes: "Pega is the Brain (State). AI is the Muscle (Work). Brain controls Muscle."

### Deep Dive: Implementation Steps
1.  **Ingest**: Use Pega Email Listener to capture text.
2.  **Process**: Call GenAI Connector with the "Intake Prompt".
3.  **Map**: Use a Data Transform to map the JSON response to Case properties.
4.  **Route**: Use a Decision Table: If `Confidence > 0.9` -> `WorkBasket:Auto`; Else -> `WorkBasket:Triage`.

### Audiobook Script (6 min + Q&A)
"We don't use AI just to be cool. We use it to smash friction points in the Pega workflow.
The first friction is **Intake**. Humans hate data entry. We use LLMs to read unstructured emails and extract clean JSON. Case creation becomes instant.
The second friction is **Triage**. Why should a senior agent route simple tickets? We use AI to classify. If the model is 90% confident, we auto-route. If not, we ask a human. This keeps your experts on expert work.
The third friction is **Action**. Drafting responses takes time. We use GenAI to draft the email based on the case history. The agent just reviews and sends. We slash Average Handle Time.
Calculate the ROI: Save 5 minutes per case. Multiply by your volume. The business case writes itself.
But remember: Pega is the brain. AI is the muscle. Pega holds the state, the security, and the audit trail. AI just does the heavy lifting."

Likely Q&A:
- Q: What if the AI misclassifies?
  A: That's why we have confidence thresholds. Low confidence always goes to a human. And we audit the logs to retrain.
- Q: Is this hard to build?
  A: No. With Pega GenAI Connectors, it's a drag-and-drop integration. The hard part is the prompt, not the code.
- Q: Does this replace agents?
  A: No, it upgrades them. They stop being data entry clerks and start being problem solvers.
