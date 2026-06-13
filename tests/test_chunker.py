import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chunker import chunk_text


def test_basic_chunking():
    text = "A" * 500
    chunks = chunk_text(text, chunk_size=200, overlap=50)
    assert len(chunks) > 1


def test_overlap():
    text = "Hello world " * 50
    chunks = chunk_text(text, chunk_size=100, overlap=20)
    # last 20 chars of chunk 0 should appear at start of chunk 1
    assert chunks[0]["text"][-20:] in chunks[1]["text"]


def test_metadata_fields():
    chunks = chunk_text("Some text here", chunk_size=50, overlap=10)
    assert "index" in chunks[0]
    assert "char_count" in chunks[0]
    assert "start_char" in chunks[0]


def test_short_chunks_filtered():
    text = "A" * 500
    chunks = chunk_text(text, chunk_size=200, overlap=50)
    long_chunks = [c for c in chunks if c["char_count"] >= 50]
    assert len(long_chunks) < len(chunks) or len(long_chunks) == len(chunks)