# Week 3: RAG Pipeline — M&A Due Diligence Analysis

## Architecture
```
3 PDFs → Chunking → MiniLM Embeddings → ChromaDB → Per-Company Retrieval → CrossEncoder → Top-2/Company → Gemini
```

## ChromaDB Collection Stats
- **Collection**: `ma_due_diligence`
- **Total Chunks Ingested**: 2595

---

## Query: What are the most significant litigation risks and legal contingencies for each company?

**Candidates Retrieved Total:** 30  
**Reranked to Top-2 per company**

### Final Context Chunks

| Rank | Company | Section | Rerank Score |
|------|---------|---------|-------------|
| 1 | Apple | Business_Overview | 0.290726 |
| 2 | Microsoft | Business_Overview | -0.128831 |
| 3 | Apple | Legal_Proceedings | -1.051093 |
| 4 | Nvidia | Risk_Factors | -3.271593 |
| 5 | Microsoft | Business_Overview | -3.350368 |
| 6 | Nvidia | General | -6.299269 |

### Gemini Response

Here are the most significant litigation risks and legal contingencies for each company based on the provided sources:

**Apple**
*   The Company is currently subject to antitrust investigations and litigation in various jurisdictions globally, including civil antitrust lawsuits in the U.S. alleging monopolization or attempted monopolization. These proceedings could have a material adverse impact on the Company’s business, results of operations, financial condition, and stock price [Source 3].
*   The company is exposed to legal and regulatory challenges associated with operating in new businesses, regions, or countries, and some transactions (including investments and acquisitions) are exposed to additional risks [Source 1].

**Microsoft**
*   The company is subject to a variety of new, existing, and evolving legal and regulatory requirements, which could adversely affect its results of operations [Source 2].
*   With new offerings, Microsoft may experience new and novel legal claims. Adverse outcomes in these claims could result in significant monetary damages or injunctive relief that might adversely affect the ability to conduct its business [Source 5]. The company is also subject to a wide range of laws, regulations, and legal requirements globally [Source 2].

**Nvidia**
*   Nvidia's business is exposed to the burden and risks associated with litigation, investigations, and regulatory proceedings [Source 4].
*   The company is, and will likely continue to be, subject to claims, litigation, and other actions, including potential regulatory proceedings, involving patent and other intellectual property matters, taxes, labor and employment, competition and antitrust, commercial disputes, and goods and services offered by them and third parties [Source 6].
*   Delaware law, provisions in Nvidia's governing documents, and its agreement with Microsoft could delay or prevent a change in control [Source 4].

---

## Query: Compare the unrecognized tax benefit positions across Apple, Microsoft, and Nvidia.

**Candidates Retrieved Total:** 30  
**Reranked to Top-2 per company**

### Final Context Chunks

| Rank | Company | Section | Rerank Score |
|------|---------|---------|-------------|
| 1 | Apple | General | 3.647098 |
| 2 | Apple | Financial_Statements | 0.000112 |
| 3 | Nvidia | Income_Tax | -0.293541 |
| 4 | Nvidia | Financial_Statements | -1.143766 |
| 5 | Microsoft | Income_Tax | -7.774927 |
| 6 | Microsoft | Business_Overview | -8.917454 |

### Gemini Response

Based on the provided context:

**Apple:**
As of September 27, 2025, Apple's total gross unrecognized tax benefits were $23.2 billion, with $10.6 billion of that amount, if recognized, impacting the Company’s effective tax rate [Source 1, Source 2]. As of September 28, 2024, the total gross unrecognized tax benefits were $22.0 billion, of which $10.8 billion would have impacted the effective tax rate [Source 1].

**Microsoft:**
The provided context does not contain sufficient information regarding Microsoft's unrecognized tax benefit position.

**Nvidia:**
Nvidia recognizes the benefit from a tax position if it is more-likely-than-not that the position would be sustained upon audit based solely on its technical merits. Their policy is to include interest and penalties related to unrecognized tax benefits as a component of income tax expense [Source 3]. While the context mentions "A reconciliation of gross unrecognized tax benefits is as follows:" [Source 4], the specific financial figures for Nvidia's unrecognized tax benefits are not provided.

---

## Query: What are the largest contractual purchase obligations and how do they compare?

**Candidates Retrieved Total:** 30  
**Reranked to Top-2 per company**

### Final Context Chunks

| Rank | Company | Section | Rerank Score |
|------|---------|---------|-------------|
| 1 | Apple | General | 1.820704 |
| 2 | Apple | General | 1.427413 |
| 3 | Nvidia | General | -2.446243 |
| 4 | Nvidia | General | -4.170700 |
| 5 | Microsoft | General | -6.554435 |
| 6 | Microsoft | General | -8.183130 |

### Gemini Response

The largest contractual purchase obligations identified in the provided sources are both related to Apple:

1.  **Apple's other purchase obligations** amount to **$14.8 billion** as of September 27, 2025 [Source 1]. These obligations primarily consist of noncancelable commitments to acquire capital assets (including product manufacturing assets), supplier arrangements, licensed intellectual property and content, and distribution rights [Source 1].
2.  **Apple's unconditional purchase obligations** total **$13.308 billion** as of September 27, 2025 [Source 2]. These primarily consist of supplier arrangements, licensed intellectual property and content, and distribution rights [Source 2].

**Comparison:**
Apple's "other purchase obligations" at $14.8 billion are larger than its "unconditional purchase obligations" at $13.308 billion.

Nvidia mentions "noncancelable purchase commitments" but does not provide a specific monetary value to compare [Source 3]. Microsoft's excerpts discuss "performance obligations" but do not provide specific figures for purchase obligations [Source 4, Source 5, Source 6].

