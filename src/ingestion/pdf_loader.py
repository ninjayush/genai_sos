import fitz

from src.ingestion.document import FinancialDocument


def load_pdf(pdf_path: str):

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    return FinancialDocument(
        source=pdf_path,
        text=text
    )