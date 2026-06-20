def rag_query_prompt(query: str, context_chunks: list) -> str:
    """
    Constructs the final prompt for Gemini using the top-5 reranked chunks.
    Each chunk is clearly delimited and its metadata is shown so the model
    can cite sources accurately.
    """
    context_blocks = []
    for i, chunk in enumerate(context_chunks, 1):
        meta = chunk.get("metadata", {})
        block = (
            f"--- Source {i} ---\n"
            f"Company: {meta.get('company', 'N/A')} | "
            f"Section: {meta.get('section', 'N/A')} | "
            f"File: {meta.get('source_file', 'N/A')}\n"
            f"Rerank Score: {chunk.get('rerank_score', 'N/A')}\n\n"
            f"{chunk['text']}"
        )
        context_blocks.append(block)

    context_str = "\n\n".join(context_blocks)

    return f"""You are an expert M&A due diligence analyst. You have been given a set of highly relevant excerpts from corporate 10-K filings, ranked and filtered for relevance.

Answer the following query using ONLY the information provided in the sources below. For each key claim, cite the source number (e.g. [Source 1]).

If the answer cannot be found in the provided sources, explicitly state: "The provided context does not contain sufficient information to answer this question."

=== USER QUERY ===
{query}

=== CONTEXT (Top-5 Reranked Chunks) ===
{context_str}

=== YOUR ANALYSIS ==="""
