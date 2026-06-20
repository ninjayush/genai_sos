# Week 4: Conversational RAG with Memory & Structured Outputs
## Architecture
| Component | Choice |
|---|---|
| **Retriever** | Local ChromaDB (all-MiniLM-L6-v2) via `langchain-chroma` |
| **Primary LLM** | Gemini 2.5 Flash via `langchain-google-genai` |
| **Structured Output** | Pydantic `FinancialSnapshot` via `.with_structured_output()` |
| **Memory** | `ConversationSummaryBufferMemory` (2,000 tokens, Groq summariser) |
| **Chain** | LCEL `RunnablePassthrough` (LangChain 1.x) |

## Conversation Logs

### Turn 1
**User:** What is Apple's total revenue and what are their most significant noted risks?

**System:**
```json
{
  "company_name": "Apple Inc.",
  "total_revenue": "$416,161 million for 2025",
  "debt_obligations": "Term debt includes fixed-rate notes totaling $86,781 million as of September 27, 2025, with maturities from 2025 to 2062.",
  "noted_risks": "Key risks include the inability to compete successfully, challenges in managing frequent product and service introductions, significant risks of supply shortages and price increases, exposure to various legal proceedings and claims, potential impacts from political events, trade disputes, and geopolitical tensions, design and manufacturing defects in products and services, intense media, political and regulatory scrutiny, cybersecurity vulnerabilities (hacking, ransomware attacks, employee error), and dependence on third-party software developers and resellers."
}
```

### Turn 2
**User:** Now give me the same breakdown for Nvidia. Pay attention to their debt obligations too.

**System:**
```json
{
  "company_name": "NVIDIA Corporation",
  "total_revenue": "$215,938 million for Jan 25, 2026",
  "debt_obligations": "Debt includes 3.20% Notes Due 2026 of $1,000 million, other commitments of $3,400 million as of January 25, 2026 (majority due through fiscal year 2027), and long-term operating lease liabilities of $2,572 million as of January 25, 2026.",
  "noted_risks": "N/A"
}
```

### Turn 3
**User:** Compare the risk profiles of Apple and Nvidia based on what we just discussed.

**System:**
```json
{
  "company_name": "Apple Inc. vs. NVIDIA Corporation",
  "total_revenue": "N/A",
  "debt_obligations": "N/A",
  "noted_risks": "Apple's risk profile highlights challenges in maintaining competitiveness through frequent product introductions, significant supply chain risks (shortages, price increases), exposure to legal and regulatory proceedings, impacts from political and geopolitical events, potential design and manufacturing defects, cybersecurity vulnerabilities, and reliance on third-party software developers and resellers. NVIDIA's risk profile emphasizes the failure to meet evolving industry and market needs due to rapid technological changes, risks from security incidents (including loss or misuse of source code), potential restrictions on the use, resale, repair, or transfer of its products (especially internationally), and dependence on customers' and partners' ability to secure capital, energy, and build datacenter infrastructure. Both companies share risks related to competition, cybersecurity, and reliance on third parties, but Apple has a more pronounced focus on supply chain and broad geopolitical/regulatory scrutiny, while NVIDIA's risks are more centered on rapid technological shifts and specific product/infrastructure dependencies."
}
```

