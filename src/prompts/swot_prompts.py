def zero_shot_prompt(text):

    return f"""
    Extract SWOT points.

    Text:

    {text}
    """


def cot_prompt(text):

    return f"""
    Think step by step.

    1. Strengths
    2. Weaknesses
    3. Opportunities
    4. Threats

    Text:

    {text}
    """


def few_shot_prompt(text):

    return f"""
    Extract SWOT points.

    Example 1:
    Text: The company has strong brand recognition but struggles with high debt. New markets offer growth, though competitors are fierce.
    Output:
    - Strengths: Strong brand recognition
    - Weaknesses: High debt
    - Opportunities: New markets
    - Threats: Fierce competitors

    Text:

    {text}
    """