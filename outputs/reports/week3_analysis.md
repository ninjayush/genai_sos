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

The most significant litigation risks and legal contingencies for each company are:

**Apple:**
*   Apple is currently subject to antitrust investigations and litigation in various jurisdictions around the world [Source 3].
*   The company is also subject to civil antitrust lawsuits in the U.S. alleging monopolization or attempted monopolization [Source 3].
*   General legal and regulatory challenges are associated with operating in new businesses, regions, or countries, potentially leading to greater-than-expected liabilities and expenses [Source 1].

**Microsoft:**
*   Microsoft is subject to a variety of new, existing, and evolving legal and regulatory requirements globally [Source 2].
*   Due to new and evolving technologies and business offerings, Microsoft may experience new and novel legal claims [Source 5]. Adverse outcomes in these claims could result in significant monetary damages or injunctive relief that could adversely affect their ability to conduct business [Source 5].

**Nvidia:**
*   Nvidia's business is exposed to the burden and risks associated with litigation, investigations, and regulatory proceedings [Source 4].
*   Nvidia is, and will likely continue to be, subject to claims, litigation, and other actions, including potential regulatory proceedings, involving patent and other intellectual property matters, taxes, labor and employment, competition and antitrust, and commercial disputes [Source 6].

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

*   **Apple:** As of September 27, 2025, Apple's total gross unrecognized tax benefits amounted to $23.2 billion. Of this, $10.6 billion, if recognized, would impact the Company’s effective tax rate. In the prior year, as of September 28, 2024, the total gross unrecognized tax benefits were $22.0 billion, with $10.8 billion impacting the effective tax rate if recognized [Source 1, Source 2].
*   **Microsoft:** The provided context does not contain sufficient information regarding Microsoft's unrecognized tax benefit position.
*   **Nvidia:** The provided context mentions Nvidia's policy for recognizing tax benefits, stating that a benefit is recognized only if it is "more-likely-than-not" that the position would be sustained upon audit, and that interest and penalties related to unrecognized tax benefits are included as a component of income tax expense [Source 3]. It also indicates that a reconciliation of gross unrecognized tax benefits exists [Source 4], but the actual amounts or reconciliation details for Nvidia's unrecognized tax benefits are not provided in the given excerpts.

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

The largest contractual purchase obligations identified are both from Apple:

*   **Apple's "Other Purchase Obligations"**: Totaling **$14.8 billion** as of September 27, 2025. These primarily consist of noncancelable obligations to acquire capital assets (including product manufacturing assets), supplier arrangements, licensed intellectual property and content, and distribution rights. Of this amount, $7.0 billion is payable within 12 months [Source 1].
*   **Apple's "Unconditional Purchase Obligations"**: Totaling **$13.308 billion** ($13,308 million) as of September 27, 2025, for obligations with a remaining term in excess of one year. These primarily consist of supplier arrangements, licensed intellectual property and content, and distribution rights. A breakdown of future payments is provided: $4,752 million in 2026, $3,708 million in 2027, $1,981 million in 2028, $1,306 million in 2029, $788 million in 2030, and $773 million thereafter [Source 2].

Comparing these, Apple's "Other Purchase Obligations" ($14.8 billion) appear to be slightly larger than its "Unconditional Purchase Obligations" ($13.308 billion) [Source 1, Source 2]. Both categories share similar underlying components such as supplier arrangements, licensed intellectual property, and distribution rights.

The provided context does not contain sufficient information regarding total contractual purchase obligations for Nvidia or Microsoft to allow for a direct comparison with Apple's figures [Source 3, Source 4, Source 5, Source 6].

