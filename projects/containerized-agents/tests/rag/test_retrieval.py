"""
RAG pipeline tests: similarity search and context building (ChromaDB mocked).
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

chromadb = pytest.importorskip("chromadb")

from agentcore.rag.retrieval import build_context, retrieve


class TestRetrieve:
    """retrieve() tests with mocked ChromaDB and embeddings."""

    def _mock_chroma(self, documents=None, distances=None, metadatas=None, count=10):
        """Build a mock ChromaDB client/collection setup."""
        mock_collection = AsyncMock()
        mock_collection.count = AsyncMock(return_value=count)
        mock_collection.query = AsyncMock(
            return_value={
                "documents": [documents or []],
                "distances": [distances or []],
                "metadatas": [metadatas or []],
            }
        )

        mock_client = MagicMock()
        mock_client.get_collection = AsyncMock(return_value=mock_collection)
        return mock_client, mock_collection

    @pytest.mark.asyncio
    async def test_retrieve_no_collection_returns_empty(self):
        """When the agent has no ChromaDB collection, retrieve returns empty list."""
        with patch("agentcore.rag.retrieval.get_chroma_client") as mock_chroma:
            mock_client = MagicMock()
            mock_client.get_collection = AsyncMock(side_effect=Exception("Collection not found"))
            mock_chroma.return_value = mock_client

            results = await retrieve("test query", "agent-without-kb")

        assert results == []

    @pytest.mark.asyncio
    async def test_retrieve_empty_collection_returns_empty(self):
        """Empty ChromaDB collection must return empty list."""
        mock_client, _ = self._mock_chroma(count=0)

        with patch("agentcore.rag.retrieval.get_chroma_client", return_value=mock_client):
            results = await retrieve("test query", "empty-agent")

        assert results == []

    @pytest.mark.asyncio
    async def test_retrieve_returns_results_above_min_score(self):
        """retrieve() must return results with similarity >= min_score."""
        docs = ["Relevant chunk about Python.", "Another relevant chunk."]
        # Cosine distances: 0.1 → similarity=0.95, 0.2 → similarity=0.90
        distances = [0.1, 0.2]
        metadatas = [{"source": "doc1.pdf"}, {"source": "doc2.pdf"}]

        mock_client, _ = self._mock_chroma(documents=docs, distances=distances, metadatas=metadatas)

        with patch("agentcore.rag.retrieval.get_chroma_client", return_value=mock_client):
            with patch("agentcore.rag.retrieval.embed_text", new=AsyncMock(return_value=[0.1] * 768)):
                results = await retrieve("Python query", "agent-1", min_score=0.7)

        assert len(results) == 2
        for text, score, meta in results:
            assert score >= 0.7

    @pytest.mark.asyncio
    async def test_retrieve_filters_below_min_score(self):
        """Results below min_score must be filtered out."""
        docs = ["High relevance chunk.", "Low relevance chunk."]
        # High: distance=0.05 → similarity=0.975; Low: distance=1.8 → similarity=0.1
        distances = [0.05, 1.8]
        metadatas = [{"source": "a.pdf"}, {"source": "b.pdf"}]

        mock_client, _ = self._mock_chroma(documents=docs, distances=distances, metadatas=metadatas)

        with patch("agentcore.rag.retrieval.get_chroma_client", return_value=mock_client):
            with patch("agentcore.rag.retrieval.embed_text", new=AsyncMock(return_value=[0.1] * 768)):
                results = await retrieve("query", "agent-2", min_score=0.7)

        # Only the high-relevance result should pass
        assert len(results) == 1
        assert results[0][1] > 0.7

    @pytest.mark.asyncio
    async def test_retrieve_results_sorted_by_descending_score(self):
        """retrieve() must return results sorted by descending similarity score."""
        docs = ["Medium doc.", "High doc.", "Low doc."]
        distances = [0.3, 0.05, 0.8]
        metadatas = [{"source": "m.pdf"}, {"source": "h.pdf"}, {"source": "l.pdf"}]

        mock_client, _ = self._mock_chroma(documents=docs, distances=distances, metadatas=metadatas, count=3)

        with patch("agentcore.rag.retrieval.get_chroma_client", return_value=mock_client):
            with patch("agentcore.rag.retrieval.embed_text", new=AsyncMock(return_value=[0.1] * 768)):
                results = await retrieve("query", "agent-3", min_score=0.0)

        scores = [r[1] for r in results]
        assert scores == sorted(scores, reverse=True)


class TestBuildContext:
    """build_context() tests."""

    @pytest.mark.asyncio
    async def test_build_context_returns_empty_string_no_results(self):
        """build_context must return empty string when retrieve returns nothing."""
        with patch("agentcore.rag.retrieval.retrieve", new=AsyncMock(return_value=[])):
            context = await build_context("query", "agent-no-kb")

        assert context == ""

    @pytest.mark.asyncio
    async def test_build_context_includes_source_citation(self):
        """build_context must include source citations in the output."""
        chunks = [
            ("Relevant text about Python.", 0.92, {"source": "python_guide.pdf", "page": 3}),
        ]

        with patch("agentcore.rag.retrieval.retrieve", new=AsyncMock(return_value=chunks)):
            context = await build_context("Python question", "agent-1")

        assert "python_guide.pdf" in context
        assert "page 3" in context
        assert "0.92" in context

    @pytest.mark.asyncio
    async def test_build_context_respects_max_tokens(self):
        """build_context must truncate output to approximately max_tokens."""
        # Create a large chunk that would exceed the budget
        large_text = "word " * 2000  # ~10000 chars
        chunks = [
            (large_text, 0.9, {"source": "big_doc.pdf"}),
        ]

        with patch("agentcore.rag.retrieval.retrieve", new=AsyncMock(return_value=chunks)):
            context = await build_context("query", "agent-1", max_tokens=100)

        # max_tokens=100 → char_budget ≈ 360; context must be smaller
        assert len(context) < 5000

    @pytest.mark.asyncio
    async def test_build_context_multiple_chunks_numbered(self):
        """build_context must number each chunk [1], [2], etc."""
        chunks = [
            ("First chunk text.", 0.95, {"source": "a.pdf"}),
            ("Second chunk text.", 0.88, {"source": "b.pdf"}),
        ]

        with patch("agentcore.rag.retrieval.retrieve", new=AsyncMock(return_value=chunks)):
            context = await build_context("query", "agent-1")

        assert "[1]" in context
        assert "[2]" in context
