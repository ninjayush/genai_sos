# Week 1 Prompting Analysis: Gemini vs. Groq

## Overview
This report evaluates how Gemini 2.5 Flash and Groq (Llama 3.3 70B) handle Zero-shot, Few-shot, and Chain-of-Thought (CoT) prompting when extracting SWOT points from unformatted financial text.

### Test Text
> AlphaCorp reported robust Q3 earnings, demonstrating a strong market share and innovative product line. However, supply chain disruptions have led to increased operational costs and delayed shipments. Looking ahead, expanding into emerging markets presents a significant growth opportunity. On the downside, looming regulatory changes and intense competition from startups pose substantial risks to future profitability.

---

## 1. Zero-Shot Prompting

**Gemini 2.5 Flash:**
```
Here are the SWOT points extracted from the text:

**Strengths:**
*   Robust Q3 earnings
*   Strong market share
*   Innovative product line

**Weaknesses:**
*   Increased operational costs (due to supply chain disruptions)
*   Delayed shipments (due to supply chain disruptions)

**Opportunities:**
*   Expanding into emerging markets

**Threats:**
*   Looming regulatory changes
*   Intense competition from startups
```

**Groq (Llama 3.3 70B):**
```
Here are the SWOT points extracted from the text:

**Strengths:**
1. Strong market share
2. Innovative product line

**Weaknesses:**
1. Supply chain disruptions
2. Increased operational costs
3. Delayed shipments

**Opportunities:**
1. Expanding into emerging markets

**Threats:**
1. Looming regulatory changes
2. Intense competition from startups
```
**Analysis**: Both models successfully extract the basic points without formatting guidance, though output styles may vary.

---

## 2. Few-Shot Prompting

**Gemini 2.5 Flash:**
```
- Strengths: Robust Q3 earnings, Strong market share, Innovative product line
- Weaknesses: Increased operational costs (due to supply chain disruptions), Delayed shipments (due to supply chain disruptions)
- Opportunities: Expanding into emerging markets
- Threats: Looming regulatory changes, Intense competition from startups
```

**Groq (Llama 3.3 70B):**
```
- Strengths: Strong market share, innovative product line, robust Q3 earnings
- Weaknesses: Supply chain disruptions, increased operational costs, delayed shipments
- Opportunities: Expanding into emerging markets
- Threats: Looming regulatory changes, intense competition from startups
```
**Analysis**: The inclusion of an example firmly anchors both models to the requested output structure. They reliably conform to the bullet-point format provided in the few-shot prompt.

---

## 3. Chain-of-Thought (CoT) Prompting

**Gemini 2.5 Flash:**
```
Here's the SWOT analysis for AlphaCorp based on the provided text:

**1. Strengths**
*   Robust Q3 earnings
*   Strong market share
*   Innovative product line

**2. Weaknesses**
*   Increased operational costs (due to supply chain disruptions)
*   Delayed shipments (due to supply chain disruptions)

**3. Opportunities**
*   Expanding into emerging markets

**4. Threats**
*   Looming regulatory changes
*   Intense competition from startups
```

**Groq (Llama 3.3 70B):**
```
To analyze the given text using the SWOT framework (Strengths, Weaknesses, Opportunities, Threats), let's break it down step by step:

1. **Strengths**: 
   - Strong market share: AlphaCorp has a robust presence in the market, indicating its products are well-received and it has a significant customer base.
   - Innovative product line: The company has a line of innovative products, which likely contributes to its strong market share and earnings.

2. **Weaknesses**:
   - Supply chain disruptions: These have resulted in increased operational costs and delayed shipments, affecting the company's efficiency and potentially its customer satisfaction.
   - Increased operational costs: As a direct consequence of the supply chain disruptions, the company is facing higher costs, which could impact its profitability.

3. **Opportunities**:
   - Expanding into emerging markets: This presents a significant growth opportunity for AlphaCorp, allowing it to tap into new customer bases and potentially increase its market share and revenue.

4. **Threats**:
   - Looming regulatory changes: These could impose new requirements or restrictions on AlphaCorp's operations, potentially increasing costs or limiting its ability to operate as it currently does.
   - Intense competition from startups: Startups often bring innovative and disruptive technologies or business models, posing a risk to established companies like AlphaCorp by potentially attracting away their customers or disrupting their market share.
```
**Analysis**: CoT instructions ("Think step by step" followed by an ordered list structure) resulted in a more methodical breakdown. Both models effectively step through Strengths, Weaknesses, Opportunities, and Threats sequentially, ensuring no category is missed.

## Conclusion
Both **Gemini 2.5 Flash** and **Groq (Llama 3.3 70B)** demonstrate strong proficiency in financial entity and sentiment extraction. Few-shot prompting is highly effective for enforcing a specific output schema, while CoT ensures a structured reasoning path.
