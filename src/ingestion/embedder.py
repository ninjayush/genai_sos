from typing import List
from sentence_transformers import SentenceTransformer

from src.ingestion.chunk import Chunk

# Model is cached locally after first download (~90MB)
_MODEL_NAME = "all-MiniLM-L6-v2"
_model: SentenceTransformer = None


def _get_model() -> SentenceTransformer:
    """Lazily load the embedding model to avoid startup cost."""
    global _model
    if _model is None:
        print(f"Loading embedding model: {_MODEL_NAME} ...")
        _model = SentenceTransformer(_MODEL_NAME)
    return _model


def embed_chunks(chunks: List[Chunk], batch_size: int = 64) -> List[Chunk]:
    """
    Embeds each chunk's text using all-MiniLM-L6-v2 (384-dim vectors).
    Modifies chunks in place and returns the list.

    Args:
        chunks:     List of Chunk objects.
        batch_size: Number of chunks to embed at once.

    Returns:
        Same list with `.embedding` field populated on each Chunk.
    """
    model = _get_model()
    texts = [c.text for c in chunks]

    print(f"Embedding {len(texts)} chunks in batches of {batch_size}...")
    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
    )

    for chunk, emb in zip(chunks, embeddings):
        chunk.embedding = emb.tolist()

    return chunks


def embed_query(query: str) -> List[float]:
    """Embed a single query string for retrieval."""
    model = _get_model()
    return model.encode(query, convert_to_numpy=True).tolist()
