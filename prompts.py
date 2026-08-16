"""Prompt templates for Lab 4 decision-support pipeline."""

SUMMARY_SYSTEM_PROMPT = (
    "You are an assistant to a microfinance loan officer. "
    "Write a factual, neutral 3-4 sentence summary of the letter. "
    "Do not invent details. If information is missing, state that clearly."
)

EXTRACT_PROMPT = """
Extract fields from the loan letter and return ONLY valid JSON with exactly these keys:
- applicant_name (string)
- amount_ghs (number)
- purpose (string)
- monthly_profit_ghs (number or null)
- has_collateral_or_guarantor (boolean)
- repayment_months (number or null)

Rules:
- If a field is not explicitly stated, use null.
- Do not guess.
- Do not include markdown fences.

Few-shot example (do not copy values, only format):
Letter:
\"\"\"
My name is Ama Owusu. I run a soap business. I request GHS 6,000 to buy molds.
My monthly profit is GHS 700. My brother will guarantee the loan.
I propose repayment over 12 months.
\"\"\"
Output:
{
  "applicant_name": "Ama Owusu",
  "amount_ghs": 6000,
  "purpose": "buy molds",
  "monthly_profit_ghs": 700,
  "has_collateral_or_guarantor": true,
  "repayment_months": 12
}
"""

BRIEF_PROMPT = """
You are supporting a human loan officer. Using the loan letter and extracted JSON, produce:
1. Strengths (bullet points grounded in the letter)
2. Risks / red flags (bullet points)
3. Missing information to request
4. Suggested next step

Important:
- Do not output approve/reject decisions.
- Final lending decisions must be made by a human.
- Do not invent facts that are not present in the input.
"""
