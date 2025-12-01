import os
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "writings"

def load_user_corpus(max_chars: int = 8000) -> str:
    """
    Load all text files from data/writings, concatenate into a single string,
    and trim to max_chars (so prompts don't explode).
    """
    texts = []

    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Directory not found: {DATA_DIR}")

    for file in DATA_DIR.iterdir():
        if file.suffix.lower() in {".txt", ".md"} and file.is_file():
            with open(file, "r", encoding="utf-8") as f:
                texts.append(f.read())

    full_text = "\n\n".join(texts).strip()
    if not full_text:
        raise ValueError("No text found in writings directory")

    # Optional: use a splitter to pick representative chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", "!", "?", " "]
    )
    chunks = splitter.split_text(full_text)

    # Join chunks until we hit max_chars
    selected = []
    total_len = 0
    for ch in chunks:
        if total_len + len(ch) > max_chars:
            break
        selected.append(ch)
        total_len += len(ch)

    style_corpus = "\n\n".join(selected)
    return style_corpus