# Week 4: Conversational RAG with Memory & Structured Outputs

## Architecture

| Component | Choice |
|---|---|
| **Retriever** | Local ChromaDB (all-MiniLM-L6-v2) via `langchain-chroma` |
| **Primary LLM** | Gemini 2.5 Flash (`gemini-2.5-flash`) via `langchain-google-genai` |
| **Structured Output** | Pydantic `FinancialSnapshot` bound via `.with_structured_output()` |
| **Memory** | `ConversationSummaryBufferMemory` (2,000 token limit, Groq Llama-3 background summariser) |
| **Chain type** | LCEL `RunnablePassthrough` (LangChain 1.x equivalent of `create_retrieval_chain`) |

## Pydantic Schema — FinancialSnapshot

```python
class FinancialSnapshot(BaseModel):
    company_name:    str  # name of company analysed
    total_revenue:   str  # revenue figures from context
    debt_obligations: str  # debt / lease obligations
    noted_risks:     str  # key risks from context
```

## How Memory Works

`ConversationSummaryBufferMemory` keeps recent messages verbatim up to the 2,000-token limit, then automatically summarises older messages into a compact paragraph using the Groq Llama-3 model. This lets the pipeline maintain coherent multi-turn conversations even when cumulative context would otherwise overflow the LLM's context window.

## Conversation Logs

### Turn 1
**User:** What is Apple's total revenue and what are their most significant noted risks?

**System (structured JSON):**
```json
{
  "company_name": "Apple",
  "total_revenue": "N/A",
  "debt_obligations": "N/A",
  "noted_risks": "N/A"
}
```

### Turn 2
**User:** Now give me the same breakdown for Nvidia. Pay attention to their debt obligations too.

**System (structured JSON):**
```json
{
  "company_name": "Nvidia",
  "total_revenue": "N/A",
  "debt_obligations": "N/A",
  "noted_risks": "N/A"
}
```

### Turn 3
**User:** Compare the risk profiles of Apple and Nvidia based on what we just discussed.

**System (structured JSON):**
```json
{
  "company_name": "N/A",
  "total_revenue": "N/A",
  "debt_obligations": "N/A",
  "noted_risks": "N/A"
}
```

