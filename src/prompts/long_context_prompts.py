def footnote_extraction_prompt(document_text: str) -> str:
    """
    Prompt designed to test long-context retrieval of specific footnotes or financial clauses.
    """
    return f"""
You are an expert M&A analyst reviewing a massive corporate financial document (10-K).

Here is the entire document text:
<document>
{document_text}
</document>

Your task is to identify and extract highly specific footnotes or financial clauses related to:
1. Contingent liabilities or pending litigations.
2. Unrecognized tax benefits or tax-related risks.
3. Commitments and leases.

Please return your findings in the following format:
- **Topic**: [Brief description of the finding]
- **Clause/Footnote Excerpt**: [Exact or highly accurate paraphrase from the text]
- **Implication for M&A**: [Brief analysis of why this matters for due diligence]

If you cannot find anything related to one of the topics, explicitly state that it is not present in the provided text.
"""
