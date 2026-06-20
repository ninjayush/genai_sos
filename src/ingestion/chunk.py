from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Chunk:
    """Represents a single text chunk with associated metadata."""
    text: str
    chunk_id: str
    company: str
    section: str
    source_file: str
    page_number: Optional[int] = None
    char_start: Optional[int] = None
    char_end: Optional[int] = None
    token_estimate: Optional[int] = None
    embedding: Optional[list] = field(default=None, repr=False)
