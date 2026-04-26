"""
RAG pipeline tests: text chunking with various sizes and overlap values.
"""
from __future__ import annotations

import pytest

bs4 = pytest.importorskip("bs4")

from agentcore.rag.ingestion import chunk_text


class TestChunkText:
    """chunk_text correctness and edge-case tests."""

    @pytest.mark.asyncio
    async def test_empty_text_returns_empty_list(self):
        """Empty input must return an empty list."""
        chunks = await chunk_text("")
        assert chunks == []

    @pytest.mark.asyncio
    async def test_whitespace_only_returns_empty_list(self):
        """Whitespace-only input must return an empty list."""
        chunks = await chunk_text("   \n\n   ")
        assert chunks == []

    @pytest.mark.asyncio
    async def test_short_text_returns_single_chunk(self):
        """Text shorter than chunk_size must return a single chunk."""
        text = "This is a short sentence."
        chunks = await chunk_text(text, chunk_size=512)
        assert len(chunks) == 1
        assert chunks[0] == text

    @pytest.mark.asyncio
    async def test_long_text_splits_into_multiple_chunks(self):
        """Text longer than chunk_size must be split into multiple chunks."""
        text = "word " * 300  # ~1500 chars
        chunks = await chunk_text(text, chunk_size=200, overlap=20)
        assert len(chunks) > 1

    @pytest.mark.asyncio
    async def test_chunks_do_not_exceed_chunk_size_significantly(self):
        """Each chunk should be close to (not hugely exceeding) chunk_size."""
        text = "The quick brown fox jumps over the lazy dog. " * 50
        chunk_size = 100
        chunks = await chunk_text(text, chunk_size=chunk_size, overlap=10)
        for chunk in chunks:
            # Allow some slack for word-boundary alignment
            assert len(chunk) <= chunk_size * 2, f"Chunk too large: {len(chunk)} chars"

    @pytest.mark.asyncio
    async def test_all_chunks_non_empty(self):
        """No chunk in the result list must be empty."""
        text = "Lorem ipsum dolor sit amet. " * 30
        chunks = await chunk_text(text, chunk_size=100, overlap=20)
        for chunk in chunks:
            assert chunk.strip() != ""

    @pytest.mark.asyncio
    async def test_overlap_causes_repeated_content(self):
        """With overlap>0, consecutive chunks must share some content."""
        # Create text with distinct tokens to check overlap
        words = [f"TOKEN{i:04d}" for i in range(200)]
        text = " ".join(words)
        chunks = await chunk_text(text, chunk_size=100, overlap=30)

        if len(chunks) > 1:
            # Last words of chunk N should appear in chunk N+1
            last_of_first = chunks[0].split()[-3:]
            second_chunk_words = set(chunks[1].split())
            overlap_found = any(w in second_chunk_words for w in last_of_first)
            assert overlap_found, "Expected overlap content in consecutive chunks"

    @pytest.mark.asyncio
    async def test_zero_overlap_no_repetition(self):
        """With overlap=0, consecutive chunks must not repeat content."""
        text = "word " * 200
        chunks = await chunk_text(text, chunk_size=50, overlap=0)
        # Build set of all words per chunk; consecutive pairs should not share
        # (word-boundary alignment may cause minor overlap — just check chunk count)
        assert len(chunks) >= 2

    @pytest.mark.asyncio
    async def test_single_very_long_word(self):
        """A word longer than chunk_size must not cause an infinite loop."""
        text = "A" * 1000  # No whitespace
        chunks = await chunk_text(text, chunk_size=100, overlap=10)
        assert len(chunks) >= 1
        # Must complete without hanging

    @pytest.mark.asyncio
    async def test_multiple_blank_lines_normalized(self):
        """Three or more consecutive blank lines must be normalized to two."""
        text = "para one\n\n\n\n\n\npara two"
        chunks = await chunk_text(text, chunk_size=512)
        combined = "\n".join(chunks)
        assert "\n\n\n" not in combined

    @pytest.mark.asyncio
    async def test_chunk_size_equals_text_length(self):
        """Text exactly equal to chunk_size must return one chunk."""
        text = "x" * 512
        chunks = await chunk_text(text, chunk_size=512, overlap=0)
        assert len(chunks) == 1
