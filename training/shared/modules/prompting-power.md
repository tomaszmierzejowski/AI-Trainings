## Prompting Power Skills (The Masterclass)

### Slides
- Slide 1 — The Foundation: RTF Framework (Polish: Model RTF)
  - **Role**: Who is the AI? (Senior Pega Architect, Data Scientist).
  - **Task**: What must it do? (Draft code, Summarize logic).
  - **Format**: How should it look? (JSON, Table, Markdown list).
  - Speaker notes: "If you only learn one thing, learn Role-Task-Format. It solves 80% of bad outputs. 
    - **Walkthrough**: Ask audience for a bad prompt ('Write an email'). Live-edit it to RTF ('Act as a Support Agent. Write a denial email. Format: 3 paragraphs')."

- Slide 2 — Technique 1: Few-Shot Prompting (Polish: Few-Shot)
  - Don't just tell; show.
  - Provide 2-3 examples of Input -> Desired Output.
  - Use for: JSON structures, specific Pega rule formats.
  - Speaker notes: "The model mimics patterns. Give it the pattern.
    - **Example**: To get Pega-compliant JSON, paste a valid snippet first.
    - **Pitfall**: Don't use real PII in examples. Use 'Jane Doe'."

- Slide 3 — Technique 2: Chain-of-Thought (Polish: Łańcuch Myśli)
  - Ask the model to "Think step-by-step".
  - Reduces logic errors in complex routing or decisioning tasks.
  - Speaker notes: "Forcing reasoning before the answer increases accuracy by 40%+.
    - **Demo**: Ask a logic riddle. It fails. Add 'Think step-by-step'. It succeeds."

- Slide 4 — Technique 3: Iterative Refinement (Polish: Iteracja)
  - "Critique this code for security flaws, then rewrite it."
  - The "Refusal" check: "If you lack info, state what is missing."
  - Speaker notes: "Don't accept the first draft. Make the AI be its own editor.
    - **Tactic**: Use the 'Critique and Revise' loop for important emails or code."

- Slide 5 — Advanced: Prompt Ladders & Decomp (Polish: Drabinka i Dekompozycja)
  - Break big tasks (Build App) into small steps (Define Data -> Define Stages -> Define UI).
  - Laddering: Start simple, verify, then add constraints.
  - Speaker notes: "Don't eat the elephant in one bite. Prompt for components.
    - **Metric**: Success = Working code block, not a whole broken app."

- Slide 6 — Safety & Governance (Polish: Bezpieczeństwo)
  - No PII (Names, IDs). Use placeholders ([Client_ID]).
  - Approved endpoints only.
  - Speaker notes: "Treat the prompt window like a public billboard.
    - **Checklist**: Redact names, mask account numbers, check endpoint URL."

### Deep Dive: How to Teach This
1.  **Define RTF**: It's "Function Definition" for English. Inputs -> Processing -> Outputs.
2.  **Why it matters**: Reduces "prompt fatigue" (trying 10 times).
3.  **Live Exercise**: Have everyone open ChatGPT. Give them a vague task ("Summarize this text"). Then force them to use RTF. Compare results.
4.  **Success Metric**: The output must be copy-paste ready with zero edits.

### Audiobook Script (8 min + Q&A)
"Welcome to the Prompt Engineering Masterclass. We are moving beyond 'chatting' to 'engineering'.
The core framework is RTF: Role, Task, Format.
**Role**: Assign a persona. 'Act as a Senior Pega System Architect.' This primes the model's vocabulary.
**Task**: Be specific. 'Refactor this activity to reduce database calls.'
**Format**: Define the output. 'Return a markdown table with columns: Issue, Fix, Impact.'
Next, we use 'Few-Shot Prompting'. If you need a specific JSON format for a Pega interface, paste two examples of valid JSON before your request. The model will copy the structure perfectly.
For complex logic, use 'Chain-of-Thought'. Simply adding 'Think step-by-step' forces the model to reason through the problem, drastically reducing logic errors in routing or eligibility rules.
Finally, practice 'Decomposition'. Don't ask for a whole application. Ask for the Data Model. Then the Case Stages. Then the UI. Assemble the pieces.
Safety is non-negotiable. Never paste real customer data. Use placeholders. If you wouldn't email it to a competitor, don't paste it in a prompt."

Likely Q&A:
- Q: What is the biggest mistake beginners make?
  A: Assuming the AI knows the context. It doesn't. You must provide the 'Role' and the 'Context' explicitly.
- Q: When do I use Few-Shot?
  A: Whenever the output format is strict (e.g., JSON, SQL, specific Pega XML).
- Q: Does "please" help?
  A: Surprisingly, yes. It sets a cooperative tone. But clarity (RTF) matters far more than politeness.
