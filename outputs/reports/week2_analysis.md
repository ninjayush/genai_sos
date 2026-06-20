# Week 2: Long Context Retrieval Analysis (Apple 10-K)

## 1. Tokenization Statistics

The Apple 10-K (FY2025) was loaded and analysed using the `cl100k_base` (tiktoken) tokenizer, which is the same vocabulary used by OpenAI GPT-4 and is a reliable proxy for most modern LLMs.

| Metric                           | Value   |
| -------------------------------- | ------- |
| Total Characters                 | 273,800 |
| Total Tokens                     | 60,566  |
| Total Paragraphs (lines)         | 4,790   |
| Avg. Tokens per Paragraph        | 11.95   |
| Median Tokens per Paragraph      | 5.0     |
| Std. Dev. (Tokens)               | 12.31   |
| 90th Percentile (Tokens)         | 30.0    |
| Max Tokens in a Single Paragraph | 71      |
| Min Tokens in a Single Paragraph | 1       |
| Paragraphs > 500 Tokens          | 0       |
| Paragraphs > 1,000 Tokens        | 0       |

Full per-paragraph breakdown: [`outputs/token_stats/apple_token_stats.csv`](../token_stats/apple_token_stats.csv)

---

## 2. Tokenization & Context Window Analysis

### 2.1 Document Density

The raw 10-K document is 273,800 characters and tokenizes down to **60,566 tokens** — a character-to-token ratio of approximately **4.52 chars/token**. This is slightly above the typical English-language average of ~4 chars/token, which can be attributed to:

- Dense financial terminology and abbreviations (e.g., "R&D", "ECJ", "GAAP") tokenizing as single or double tokens.
- Numeric values (e.g., "$56.2 billion", "10%") being tokenized very compactly.
- Tables and structured data being tokenized more efficiently than prose.

### 2.2 Paragraph Distribution

The median paragraph length is only **5 tokens**, which tells us the PDF has a fragmented layout (individual lines, table cells, header text, page numbers). This is typical of machine-extracted PDF text and explains why the `std_dev` of 12.31 is very high relative to the mean of 11.95. There is extreme variance — the document is highly skewed towards very short lines with occasional denser prose blocks.

> **Key Insight**: No paragraph exceeded 71 tokens. This confirms that the 10-K is not written in long flowing narrative paragraphs but rather in structured tables, bullet points, and short statements — which is characteristic of formal SEC filings.

### 2.3 Fitting Within the Context Window

Gemini 2.5 Flash supports a **1,000,000 token** context window on the free tier. The Apple 10-K at 60,566 tokens uses only **~6%** of the available context. This means:

- The entire document is trivially small relative to what the model can handle in one shot.
- No chunking, summarization, or RAG (Retrieval-Augmented Generation) was required.
- A larger corpus (e.g., all three 10-Ks combined: Apple + Microsoft + Nvidia) could still comfortably fit within a single prompt.

---

## 3. Gemini 2.5 Flash — M&A Footnote Extraction

The entire Apple 10-K text was passed in a single API call. Gemini was asked to locate and extract **contingent liabilities**, **unrecognized tax benefits**, and **lease/purchase commitments** — specific financial clauses that are often buried deep in footnotes and are critical for M&A due diligence.

### 3.1 Was the Response Useful? -> Yes — Highly Effective

The model returned **7 well-structured findings** across all three requested topic areas, with direct quotes from the document and actionable M&A implications for each. Here is our assessment:

#### Completeness

The response was thorough. It captured both major and minor disclosures:

- Three distinct legal proceedings (DMA, DOJ antitrust, Epic Games injunction), each with escalating severity.
- Two separate tax-related items (unrecognized tax benefits and the EU State Aid ECJ ruling).
- Three categories of commitment obligations (leases, manufacturing, IP/content).

This level of coverage from a single raw-text prompt is remarkable — a human analyst would have needed to manually scan dozens of pages across multiple sections of the filing.

#### Accuracy

The financial figures quoted by the model were **specific and verifiable**:

- `$23.2 billion` in gross unrecognized tax benefits.
- `$56.2 billion` in manufacturing purchase obligations (with `$55.4 billion` payable within 12 months).
- `€500 million` EU DMA fine, with a risk of fines up to **10% of global annual revenue**.

This suggests the model maintained accurate positional awareness throughout the 60k-token document without losing track of numbers or confusing figures across sections.

#### Relevance & M&A Framing

Every finding was correctly framed in the context of due diligence. Notably, the model correctly identified that:

- The Epic Games injunction and DMA investigation **directly threaten Apple's Services revenue** — the company's highest-growth segment.
- The `$56.2B` manufacturing obligation due within 12 months represents a **working capital constraint** critical for any acquirer's financial modelling.
- The `$23.2B` unrecognized tax benefit is a **valuation-sensitive figure** that could materially change the acquisition price depending on how tax authorities resolve it.

#### Limitations

- The model did not return **page numbers or exact footnote references** (a limitation of raw text extraction vs. a structured PDF parser).
- Short-sentence sections from tables were excluded from the response, meaning some minor commitments embedded in tabular footnotes may have been overlooked.
- The model did not explicitly rank or prioritize the findings by risk severity.

### 3.2 Summary Table

| Finding                                     | Risk Level  | M&A Impact                                               |
| ------------------------------------------- | ----------- | -------------------------------------------------------- |
| EU DMA Fine + ongoing investigation         | 🔴 High     | Services revenue at risk; potential 10% of global sales  |
| DOJ Antitrust Lawsuit                       | 🔴 High     | Core iPhone market business model at risk                |
| Epic Games Injunction / Criminal Contempt   | 🔴 Critical | App Store commissions banned; criminal risk              |
| Unrecognized Tax Benefits ($23.2B)          | 🟡 Medium   | Could materially impact effective tax rate & valuation   |
| EU State Aid Tax Charge ($10.2B)            | 🟡 Medium   | Resolved but highlights international tax risk exposure  |
| Lease Obligations ($16.8B)                  | 🟠 Moderate | Long-term cash outflow; operational flexibility concerns |
| Manufacturing Purchase Obligations ($56.2B) | 🟠 Moderate | Large short-term commitment; supplier dependency         |
| Other Purchase Obligations ($14.8B)         | 🟠 Moderate | IP/content licensing risks for Services ecosystem        |

---

## 4. Conclusion

This experiment demonstrates that **Gemini 2.5 Flash is a highly capable long-context retrieval engine** for financial documents at the free tier. Without any chunking or embedding, a single API call over a raw 60k-token 10-K produced structured, accurate, and M&A-relevant insights.

The tokenization analysis confirmed that SEC filings are token-efficient and heavily structured, making them ideal candidates for direct context window injection — validating the Week 2 architectural approach of cloud-first, zero-cost document intelligence.
