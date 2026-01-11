# Presenter Guide: Practical AI Enablement

## The Narrative Arc (Hero's Journey)
1. **The Call**: "We are drowning in busywork (emails, summaries, diffs)."
2. **The Guide**: "AI isn't magic; it's a power tool. We need to learn to hold it."
3. **The Challenge**: "Hallucinations, bad prompts, wrong tools."
4. **The Transformation**: "Prompt Mastery + The Right Stack = 10x Speed."
5. **The Return**: "You go back to your desk with a Cookbook and a Plan."

## Prompt Mastery Quickstart
*Teach this early and often.*
1. **Formula**: Instruction + Context + Output + Constraints.
2. **Laddering**:
   - Level 1: "Write code." (Bad)
   - Level 2: "Write a Python script to parse CSV." (Better)
   - Level 3: "Write a Python script to parse CSV. Handle missing columns. Output JSON. Use Pandas." (Best)
3. **Safety Check**: "Would you put this on a billboard? No? Then don't put it in a public LLM."

## Tool Selection Decision Tree
| Need | Tool | Why |
|---|---|---|
| **Facts, News, Citations** | **Perplexity** | Real-time web search, sources provided. |
| **Drafting, Logic, Summaries** | **ChatGPT** | Strong reasoning, great for text/content. |
| **Code, Diffs, Refactoring** | **Cursor** | Context-aware, applies changes to files. |
| **Rapid UI Prototypes** | **MagicUI/Lovable** | Visual only, throwaway code for demos. |

## Demo Flow (The "Golden Thread")
1. **Research (Perplexity)**: "Find the latest policy on [Topic]." -> Copy citation.
2. **Draft (ChatGPT)**: "Based on this policy, draft an email to the client." -> Iterate prompt with RTF.
3. **Build (Cursor)**: "Now let's implement the rule validation in code." -> Generate tests.

## Live Demo Scripts

### Demo 1: ChatGPT Reasoning (15 min)
- **Goal**: Show CoT and RTF.
- **Step 1**: "Write a rejection email." (Show generic output).
- **Step 2**: Apply RTF: "Act as Claims Adjuster. Context: Policy #123 excludes flood. Output: Empathetic email. Constraint: Cite section 4.a."
- **Step 3**: Show superior result.
- **Step 4**: "Critique this email for tone." -> Iterate.

### Demo 2: The Tool Stack (15 min)
- **Step 1 (Perplexity)**: "What are the GDPR fines for email leaks in 2025?" -> Show citations.
- **Step 2 (ChatGPT)**: "Draft a memo to the team summarizing these risks."
- **Step 3 (Cursor)**: "Open `UserClass.java`. Add a logging mask for the email field." -> Show diff.

## Objection Handling
- **"We don't have budget."** -> "Cursor has a free tier. ChatGPT Free is powerful. You can start today for $0."
- **"It's not secure."** -> "We use approved endpoints. We never paste PII. We treat it like a public web search."
- **"It hallucinates."** -> "Yes. That's why we use 'Grounding' (Perplexity) and 'Constraints'. Humans hallucinate too; we call it 'guessing'. We verify everything."
- **"Will it replace me?"** -> "It replaces the boring parts of your job. It replaces data entry. It doesn't replace judgment."

## Troubleshooting
- **Internet issues**: Switch to offline slides + pre-recorded demos.
- **Tool access denied**: Use the provided "Sandbox" accounts or pair up.
- **Low energy**: Switch to a "Prompt Battle" – who can get the best output in 2 minutes?
