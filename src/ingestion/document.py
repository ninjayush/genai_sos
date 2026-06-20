from dataclasses import dataclass


@dataclass
class FinancialDocument:

    source: str
    text: str
    token_count: int = 0