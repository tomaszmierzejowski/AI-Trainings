## Prompt Mastery Quickstart (Practical)

### Slide Outline
- **The Formula**: Instruction + Context + Output + Constraints.
- **Laddering**: Start simple → Test → Fail → Refine constraints.
- **Few-Shot**: When to show vs. tell (formatting).
- **Evaluation**: Does it parse? Is it true? Is it safe?

### Speaker Notes
- **Hook**: "Prompting is coding in English. Syntax matters."
- **The Formula**: Show a bad prompt ("Write an email") vs. a good one ("Act as a support agent. Write a refund denial email for claim #123. Tone: empathetic but firm. Max 100 words.").
- **Laddering**:
  1. Base: "Classify this email." -> Result: Too vague.
  2. +Context: "Classify into Claims, Service, Sales." -> Result: Better.
  3. +Output: "Return JSON with {category, confidence}." -> Result: Parsable.
  4. +Constraints: "If unsure, mark as 'Human Review'." -> Result: Safe.
- **Few-Shot**: Use 2-3 examples when you need a specific table format or JSON structure.
- **Safety**: "Never put real PII in the prompt window. Use placeholders like [Client_Name]."

### Audiobook Script (5 min)
"Welcome to Prompt Mastery. This isn't magic; it's engineering. We use a formula: Instruction, Context, Output, and Constraints.
Don't just say 'Summarize this.' Say 'Act as a Senior BA. Summarize these notes into three bullets: Decisions, Risks, and Actions. Max 50 words per bullet.'
We use 'Laddering' to build robustness. Start with the base instruction. Test it. If it hallucinates, add a constraint. If the format is wrong, add a few-shot example.
Always evaluate: Is the output true? Is it safe? Does it meet the format?
By the end of this module, you'll have a 'Prompt Cookbook' you can reuse daily."
