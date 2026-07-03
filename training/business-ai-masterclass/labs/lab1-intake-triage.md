# Lab 1: The Prompt Engineering Workbench

## Objective
Move beyond "vibes-based" prompting to "engineering-based" prompting. You will benchmark three different strategies for a complex reasoning task.

## The Task: Mortgage Approval Logic
**Scenario**: You are a bank's risk engine. You must evaluate a loan application based on messy notes.

**Input Data**:
```text
Applicant: John Doe. Income: $50k/year (contractor, variable). Credit Score: 680. 
Debts: $500/mo car payment, $200/mo student loan. 
Requested Loan: $300k home. 
Policy: 
1. Max DTI (Debt-to-Income) is 43%. 
2. Credit score must be > 700 OR (Score > 650 AND DTI < 35%).
3. Self-employed requires 2 years of tax returns (missing here).
```

## Strategy A: Zero-Shot (The Baseline)
**Prompt**:
> "Approve or deny this loan based on the policy."

**Analyze**: 
- Did it calculate DTI correctly? ($50k/12 = $4166/mo. Debts = $700. DTI = 16%.)
- Did it catch the missing tax returns?
- *Record the result.*

## Strategy B: Chain of Thought (CoT)
**Prompt**:
> "Role: Senior Underwriter.
> Task: Evaluate the loan application.
> Format:
> 1. List all debts and calculate total monthly debt.
> 2. Calculate monthly gross income.
> 3. Compute DTI ratio (Show the math).
> 4. Check Credit Score condition.
> 5. Check Documentation condition.
> 6. Final Decision (Approve/Deny/Request Info).
> 
> Think step-by-step."

**Analyze**:
- Is the math more accurate?
- Is the reasoning clearer?

## Strategy C: Few-Shot + CoT (The Gold Standard)
**Prompt**:
> [Paste the System Prompt from Strategy B]
> 
> [Example 1]
> Input: Jane Smith...
> Reasoning: Income $10k... DTI 10%... Score 800... Docs OK.
> Decision: Approve.
> 
> [Example 2]
> Input: Bob Jones...
> Reasoning: Income $3k... DTI 50%...
> Decision: Deny (High DTI).
> 
> [Your Input]
> Applicant: John Doe...

**Analyze**:
- Does the output format perfectly match the examples?

## Deliverable
Create a table comparing the 3 strategies:
- **Accuracy**: (Pass/Fail)
- **Hallucination**: (Did it invent facts?)
- **Speed**: (Slow/Fast)
