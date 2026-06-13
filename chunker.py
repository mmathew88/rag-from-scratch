def chunk_text(text: str, chunk_size: int = 200, overlap: int = 50) -> list[dict]:
    """
    Split text into overlapping chunks.

    Args:
        text: the full document text
        chunk_size: target size of each chunk in characters
        overlap: how many characters to repeat between chunks
    """
    chunks = []
    start = 0
    chunk_index = 0

    while start < len(text):
        end = start + chunk_size
        chunk_text_content = text[start:end]

        chunks.append({
            "index": chunk_index,
            "text": chunk_text_content,
            "start_char": start,
            "end_char": min(end, len(text)),
            "char_count": len(chunk_text_content)
        })

        # Step forward but overlap so chunks share context
        start += chunk_size - overlap
        chunk_index += 1

    return chunks


if __name__ == "__main__":
    sample = """
Retrieval Augmented Generation (RAG) is a technique that combines
information retrieval with text generation. Instead of relying solely
on what a language model learned during training, RAG first searches
a knowledge base to find relevant documents, then uses those documents
as context when generating an answer. This makes the model's answers
grounded in real, up-to-date information.
""".strip()

    chunks = chunk_text(sample, chunk_size=150, overlap=30)
    for c in chunks:
        print(f"[Chunk {c['index']}] chars {c['start_char']}–{c['end_char']} ({c['char_count']} chars)")
        print(f"  {c['text'][:80]}...")
        print()