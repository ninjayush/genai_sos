import tiktoken
import pandas as pd

from src.ingestion.document import FinancialDocument


class TokenAnalyzer:

    def __init__(self):

        self.encoder = tiktoken.get_encoding(
            "cl100k_base"
        )

    def count_tokens(self, text):

        return len(
            self.encoder.encode(text)
        )

    def analyze_document(
        self,
        document: FinancialDocument
    ):

        document.token_count = self.count_tokens(
            document.text
        )

        return document

    def paragraph_statistics(
        self,
        document: FinancialDocument
    ):
        import re

        # Split on one or more blank lines or single newlines to handle PDF text
        raw_paragraphs = re.split(r'\n{2,}|\n', document.text)

        # Filter out empty or whitespace-only paragraphs
        paragraphs = [p.strip() for p in raw_paragraphs if p.strip()]

        rows = []
        cumulative = 0

        for i, para in enumerate(paragraphs):
            token_count = self.count_tokens(para)
            char_count = len(para)
            cumulative += token_count

            rows.append(
                {
                    "paragraph_id": i,
                    "char_count": char_count,
                    "tokens": token_count,
                    "token_density": round(token_count / char_count, 4) if char_count > 0 else 0,
                    "cumulative_tokens": cumulative,
                    "preview": para[:120]
                }
            )

        return pd.DataFrame(rows)

    def document_summary(
        self,
        document: FinancialDocument
    ) -> dict:
        """Returns a high-level summary of token statistics for the document."""
        import re
        raw_paragraphs = re.split(r'\n{2,}|\n', document.text)
        paragraphs = [p.strip() for p in raw_paragraphs if p.strip()]
        token_counts = [self.count_tokens(p) for p in paragraphs]

        df = pd.Series(token_counts)

        return {
            "total_chars": len(document.text),
            "total_tokens": document.token_count,
            "total_paragraphs": len(paragraphs),
            "avg_tokens_per_para": round(df.mean(), 2),
            "median_tokens_per_para": round(df.median(), 2),
            "max_tokens_para": int(df.max()),
            "min_tokens_para": int(df.min()),
            "std_dev_tokens": round(df.std(), 2),
            "p90_tokens": round(df.quantile(0.90), 2),
            "paragraphs_over_500_tokens": int((df > 500).sum()),
            "paragraphs_over_1000_tokens": int((df > 1000).sum()),
        }