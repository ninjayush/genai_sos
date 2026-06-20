from typing import List, Optional
import chromadb
from chromadb.config import Settings

from src.ingestion.chunk import Chunk

_COLLECTION_NAME = "ma_due_diligence"

# Persistent client — stores the DB to disk
_client: chromadb.PersistentClient = None
_collection = None


def _get_collection(persist_dir: str = "outputs/chromadb"):
    global _client, _collection
    if _collection is None:
        _client = chromadb.PersistentClient(path=persist_dir)
        _collection = _client.get_or_create_collection(
            name=_COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )
    return _collection


def ingest_chunks(
    chunks: List[Chunk],
    persist_dir: str = "outputs/chromadb",
) -> int:
    """
    Inserts a list of embedded Chunk objects into ChromaDB.
    Skips chunks that already exist (idempotent via chunk_id).

    Returns:
        Number of chunks successfully inserted.
    """
    collection = _get_collection(persist_dir)

    ids        = [c.chunk_id for c in chunks]
    documents  = [c.text for c in chunks]
    embeddings = [c.embedding for c in chunks]
    metadatas  = [
        {
            "company":     c.company,
            "section":     c.section,
            "source_file": c.source_file,
            "char_start":  str(c.char_start or ""),
            "char_end":    str(c.char_end or ""),
            "token_est":   str(c.token_estimate or ""),
        }
        for c in chunks
    ]

    # Upsert handles duplicates gracefully
    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    print(f"Upserted {len(chunks)} chunks into ChromaDB collection '{_COLLECTION_NAME}'.")
    return len(chunks)


def retrieve(
    query_embedding: List[float],
    top_k: int = 20,
    persist_dir: str = "outputs/chromadb",
    where: Optional[dict] = None,
) -> List[dict]:
    """
    Retrieves top-k most similar chunks from ChromaDB using cosine similarity.

    Args:
        query_embedding: 384-dim embedding vector for the query.
        top_k:           Number of candidates to retrieve.
        persist_dir:     Path to ChromaDB persistence directory.
        where:           Optional metadata filter (e.g. {"company": "Apple"}).

    Returns:
        List of result dicts with keys: id, text, metadata, distance.
    """
    collection = _get_collection(persist_dir)

    kwargs = dict(
        query_embeddings=[query_embedding],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"],
    )
    if where:
        kwargs["where"] = where

    results = collection.query(**kwargs)

    output = []
    for i in range(len(results["ids"][0])):
        output.append({
            "id":       results["ids"][0][i],
            "text":     results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i],
        })

    return output


def collection_stats(persist_dir: str = "outputs/chromadb") -> dict:
    """Return basic stats about the current collection."""
    collection = _get_collection(persist_dir)
    return {
        "collection_name": _COLLECTION_NAME,
        "total_chunks":    collection.count(),
    }
