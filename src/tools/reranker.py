from typing import List, Tuple
from sentence_transformers import CrossEncoder

# ms-marco cross-encoder — strong reranker, runs locally
_RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
_reranker: CrossEncoder = None


def _get_reranker() -> CrossEncoder:
    """Lazily load the CrossEncoder reranker."""
    global _reranker
    if _reranker is None:
        print(f"Loading CrossEncoder reranker: {_RERANKER_MODEL} ...")
        _reranker = CrossEncoder(_RERANKER_MODEL, max_length=512)
    return _reranker


def rerank(
    query: str,
    candidates: List[dict],
    top_k: int = 5,
) -> List[dict]:
    """
    Reranks a list of retrieved candidate chunks using a CrossEncoder.

    The CrossEncoder scores each (query, passage) pair jointly, which is
    much more accurate than the dot-product/cosine score from the bi-encoder
    but too slow to run over the full corpus — so we apply it only to the
    top-20 candidates from ChromaDB.

    Args:
        query:      The raw user query string.
        candidates: List of result dicts from vector_store.retrieve().
        top_k:      Number of top chunks to return after reranking.

    Returns:
        Sorted list of the top_k highest-scoring dicts, each with an added
        `rerank_score` field.
    """
    reranker = _get_reranker()

    pairs = [(query, c["text"]) for c in candidates]
    scores: List[float] = reranker.predict(pairs).tolist()

    # Attach scores and sort descending
    for candidate, score in zip(candidates, scores):
        candidate["rerank_score"] = round(score, 6)

    reranked = sorted(candidates, key=lambda x: x["rerank_score"], reverse=True)
    return reranked[:top_k]
