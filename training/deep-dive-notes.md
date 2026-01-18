# Deep Dive Notes & Expansion Pack

**Purpose**: This is the master reference for trainers and advanced participants. It expands every agenda item into a concrete, step-by-step guide with no buzzwords.

---

## Module 1: Prompt Mastery (The "Engineering" Approach)

### Concept: The RTF Framework
*   **Definition**: A formula to force LLMs to behave like software functions. **Role** (Who), **Task** (What), **Format** (How).
*   **Why it matters**: Reduces "regenerate" loops by 50%. Gets usable business outputs (JSON/Tables) instead of chatty prose.
*   **How to do it**:
    1.  **Role**: Assign a persona relevant to the Pega domain (e.g., "Senior LSA", "Claims Adjuster").
    2.  **Task**: Start with an active verb ("Draft", "Refactor", "Summarize").
    3.  **Format**: Specify the exact shape (JSON, CSV, Markdown Table, XML).
    4.  **Constraint**: Add "do not" rules.
*   **Example**:
    *   *Input*: "Fix this rule." (Bad)
    *   *Output*: "Act as a Pega LSA (**Role**). Refactor this Java step to use a Data Page (**Task**). Return the new code block and a list of 3 unit tests (**Format**). Do not use 'PublicAPI' (**Constraint**)."
*   **Demo Script (2 min)**:
    1.  Open ChatGPT.
    2.  Type: "Write a rejection email." -> Show generic result.
    3.  Type: "Act as a Claims Adjuster. Write a rejection email for Policy #123 (Flood exclusion). Tone: Empathetic but firm. Format: 3 paragraphs." -> Show superior result.
*   **Pitfalls**:
    *   *Too vague*: "Make it professional." (Fix: "Use 8th-grade reading level, no jargon.")
    *   *Missing Format*: "Give me a list." (Fix: "Give me a Markdown table with columns A, B, C.")
*   **Q&A**:
    *   *Q: Does "please" matter?* A: Yes, it sets a cooperative tone, but structural clarity (RTF) is 10x more important.
    *   *Q: Can I save these?* A: Yes, save your best RTF prompts in a "Prompt Cookbook" (see `prompt-cookbook.md`).

### Concept: Chain-of-Thought (CoT)
*   **Definition**: Forcing the model to show its work before giving the final answer.
*   **Why it matters**: Increases accuracy on logic/math/routing tasks by >40%. Prevents "hallucinated" quick answers.
*   **How to do it**: Add the phrase "Think step-by-step" or "Explain your reasoning before the final JSON."
*   **Example**:
    *   *Task*: "Route this case."
    *   *Prompt*: "Classify this email. **Think step-by-step**: 1. Identify the intent. 2. Check urgency keywords. 3. Map to queue. Final Output: JSON only."
*   **Metrics**: Accuracy of routing decisions (compare to human baseline).

---

## Module 2: Tool Selection (The "Right Tool" Matrix)

### Concept: Perplexity (The Knowledge Engine)
*   **Definition**: A search engine that summarizes answers with citations.
*   **Why it matters**: Stops you from inventing facts. Essential for Pega documentation, compliance laws, and market research.
*   **Demo Script**:
    1.  Ask ChatGPT: "What is the Pega 8.8 syntax for 'IsinasPage'?" (Might be outdated/wrong).
    2.  Ask Perplexity: "What is the Pega 8.8 syntax for 'IsinasPage'? Cite official docs." (Returns link to Pega Academy).
*   **Pitfall**: Trusting it blindly. Always click one citation to verify.

### Concept: Cursor (The Build Engine)
*   **Definition**: A code editor (VS Code fork) that sees your local files and git history.
*   **Why it matters**: It fixes *your* specific code, not generic code.
*   **How to do it**:
    1.  Open a legacy file.
    2.  Highlight a complex block.
    3.  Press `Cmd+K` (or `Ctrl+K`).
    4.  Type: "Refactor this to use a switch statement."
*   **Polish Note**: "Cursor to Twój 'programista w parze' (Pair Programmer)."

---

## Module 3: Pega Workflow Acceleration

### Pattern: Intelligent Intake
*   **Definition**: Converting unstructured text (email/PDF) into structured data (JSON) *before* a human sees it.
*   **Why it matters**: Eliminates manual data entry. Reduces Case Creation time from 5 mins to 2 seconds.
*   **How to do it**:
    1.  **Input**: Raw email text.
    2.  **Prompt**: "Extract entities: ClientName, PolicyID, IncidentDate. Output: JSON."
    3.  **Pega**: Map JSON to Clipboard Page.
*   **Pitfall**: Parsing errors. *Fix*: Use Pega's JSON Data Transform or ask LLM to "Validate JSON schema."

### Pattern: Generative Action
*   **Definition**: Pre-drafting communications for the agent.
*   **Why it matters**: Agents spend 30% of time typing. This reduces Average Handle Time (AHT).
*   **Demo Script**:
    1.  Show a "Claim Denied" screen in Pega (mock).
    2.  Show the "Draft Email" button.
    3.  Prompt: "Draft an apology email using the 'Flood Exclusion' clause. Keep it under 100 words."
    4.  Result: Agent reviews, edits 1 word, sends.
*   **Metrics**: Reduction in AHT (Average Handle Time).

---

## Lab 1: Intelligent Intake (Deep Dive)

### Steps
1.  **Open** `training/shared/assets/fictional-datasets/service.csv`.
2.  **Pick** one row (e.g., "I'm angry about my bill").
3.  **Goal**: Create a prompt that outputs: `{"sentiment": "negative", "intent": "billing_dispute", "urgency": "high"}`.
4.  **Iteration**:
    *   *Attempt 1*: "Classify this." -> Result: Paragraph text. (Fail).
    *   *Attempt 2*: "Classify into JSON." -> Result: Good format, wrong intent.
    *   *Attempt 3 (Success)*: "Role: Support Bot. Task: Extract sentiment/intent/urgency. Constraints: Intent must be one of [billing, tech, general]. Format: JSON."
5.  **Validation**: Paste the result into a JSON validator or Pega Data Transform.

---

## Governance & Safety

### Concept: The "Billboard" Rule
*   **Definition**: Never put anything in a prompt you wouldn't put on a highway billboard.
*   **Why it matters**: Public LLMs learn from data (unless Enterprise mode is on). PII leakage is a GDPR violation.
*   **How to do it**:
    1.  **Redact**: "Client John Smith" -> "Client [ID]".
    2.  **Genericize**: "Pega Bank Poland" -> "A large bank".
*   **Q&A**:
    *   *Q: Is Enterprise ChatGPT safe?* A: Yes, OpenAI does not train on Enterprise data. But we still practice "Data Minimization" (send only what is needed).

