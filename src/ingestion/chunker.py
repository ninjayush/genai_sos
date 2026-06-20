import re
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.ingestion.chunk import Chunk

# Maps known filename patterns to structured metadata
_COMPANY_MAP = {
    "apple":  {"company": "Apple",     "ticker": "AAPL"},
    "ms":     {"company": "Microsoft", "ticker": "MSFT"},
    "nvidia": {"company": "Nvidia",    "ticker": "NVDA"},
}

# Section header patterns found in 10-K filings
_SECTION_PATTERNS = [
    (r"risk factors",                        "Risk_Factors"),
    (r"legal proceedings",                   "Legal_Proceedings"),
    (r"management.s discussion",             "MD&A"),
    (r"quantitative.*qualitative.*market",   "Market_Risk"),
    (r"financial statements",                "Financial_Statements"),
    (r"notes to.*financial statements",      "Financial_Notes"),
    (r"commitments and contingencies",       "Commitments_Contingencies"),
    (r"income tax",                          "Income_Tax"),
    (r"business",                            "Business_Overview"),
]


def _detect_company(filename: str) -> dict:
    """Infer company metadata from the filename."""
    lower = filename.lower()
    for key, meta in _COMPANY_MAP.items():
        if key in lower:
            return meta
    return {"company": "Unknown", "ticker": "N/A"}


def _detect_section(text: str) -> str:
    """Heuristically label a chunk's section from its content."""
    lower = text.lower()
    for pattern, label in _SECTION_PATTERNS:
        if re.search(pattern, lower):
            return label
    return "General"


def chunk_document(
    text: str,
    source_file: str,
    chunk_size: int = 512,
    chunk_overlap: int = 64,
) -> List[Chunk]:
    """
    Splits document text using RecursiveCharacterTextSplitter and tags
    every chunk with rich metadata (company, section, position).

    Args:
        text:         Full document text string.
        source_file:  Original filename (e.g. "apple10k.pdf") for metadata.
        chunk_size:   Target character size for each chunk.
        chunk_overlap: Character overlap between consecutive chunks.

    Returns:
        List of Chunk objects with metadata attached.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    company_meta = _detect_company(source_file)
    raw_chunks = splitter.split_text(text)

    chunks = []
    char_cursor = 0

    for i, chunk_text in enumerate(raw_chunks):
        char_start = text.find(chunk_text, char_cursor)
        char_end = char_start + len(chunk_text) if char_start != -1 else None

        section = _detect_section(chunk_text)

        chunk = Chunk(
            text=chunk_text,
            chunk_id=f"{company_meta['ticker']}_{i:05d}",
            company=company_meta["company"],
            section=section,
            source_file=source_file,
            char_start=char_start if char_start != -1 else None,
            char_end=char_end,
            token_estimate=len(chunk_text) // 4,   # rough estimate
        )

        chunks.append(chunk)

        if char_start != -1:
            char_cursor = char_start + 1

    return chunks
