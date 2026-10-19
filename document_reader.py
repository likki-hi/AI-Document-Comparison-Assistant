
import re
from pypdf import PdfReader


STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on",
    "at", "to", "for", "of", "is", "are", "was", "were",
    "be", "been", "being", "am", "i", "you", "we", "they",
    "he", "she", "it", "my", "your", "our", "their",
    "with", "from", "as", "by", "this", "that", "these",
    "those", "have", "has", "had", "do", "does", "did"
}


def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def clean_text(text):
    text = text.lower()

    # Keep letters and spaces; remove numbers and punctuation
    text = re.sub(r"[^a-z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def get_keywords(text):
    cleaned = clean_text(text)
    words = cleaned.split()

    # Remove common words
    keywords = {
        word for word in words
        if word not in STOP_WORDS and len(word) > 1
    }

    return keywords
