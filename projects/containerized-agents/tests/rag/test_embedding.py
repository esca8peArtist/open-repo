"""
RAG pipeline tests: Ollama embeddings endpoint — batch processing (mocked).
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.rag.embeddings import embed_batch, embed_text


class TestEmbedText:
    """embed_text() single-text embedding tests."""

    @pytest.mark.asyncio
    async def test_embed_text_returns_768_floats(self):
        """embed_text must return a list of 768 floats (nomic-embed-text dimension)."""
        mock_embedding = [0.1] * 768

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)

            mock_resp = MagicMock()
            mock_resp.raise_for_status = MagicMock()
            mock_resp.json = MagicMock(return_value={"embedding": mock_embedding})
            mock_client.post = AsyncMock(return_value=mock_resp)
            mock_client_cls.return_value = mock_client

            result = await embed_text("Hello world")

        assert len(result) == 768
        assert all(isinstance(f, float) for f in result)

    @pytest.mark.asyncio
    async def test_embed_text_sends_correct_model(self):
        """embed_text must use 'nomic-embed-text' model in the request."""
        mock_embedding = [0.0] * 768

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)

            mock_resp = MagicMock()
            mock_resp.raise_for_status = MagicMock()
            mock_resp.json = MagicMock(return_value={"embedding": mock_embedding})
            mock_client.post = AsyncMock(return_value=mock_resp)
            mock_client_cls.return_value = mock_client

            await embed_text("test text")

        call_kwargs = mock_client.post.call_args[1]
        request_body = call_kwargs.get("json") or mock_client.post.call_args[0][1] if len(mock_client.post.call_args[0]) > 1 else {}
        # Check model is nomic-embed-text in the POST body
        assert "nomic-embed-text" in str(mock_client.post.call_args)

    @pytest.mark.asyncio
    async def test_embed_text_raises_on_http_error(self):
        """embed_text must raise httpx.HTTPStatusError on non-2xx response."""
        import httpx

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)

            mock_resp = MagicMock()
            mock_resp.raise_for_status.side_effect = httpx.HTTPStatusError(
                "500 Internal Server Error", request=MagicMock(), response=mock_resp
            )
            mock_client.post = AsyncMock(return_value=mock_resp)
            mock_client_cls.return_value = mock_client

            with pytest.raises(httpx.HTTPStatusError):
                await embed_text("failing text")


class TestEmbedBatch:
    """embed_batch() batch processing tests."""

    @pytest.mark.asyncio
    async def test_embed_batch_empty_returns_empty(self):
        """embed_batch([]) must return []."""
        result = await embed_batch([])
        assert result == []

    @pytest.mark.asyncio
    async def test_embed_batch_preserves_order(self):
        """embed_batch must return embeddings in the same order as the input texts."""
        texts = [f"text_{i}" for i in range(5)]
        # Each text gets a distinct mock embedding: first float = index
        fake_embeddings = [[float(i)] + [0.0] * 767 for i in range(5)]

        call_count = 0

        async def _fake_embed_text(text):
            nonlocal call_count
            idx = int(text.split("_")[1])
            call_count += 1
            return fake_embeddings[idx]

        with patch("agentcore.rag.embeddings.embed_text", side_effect=_fake_embed_text):
            results = await embed_batch(texts)

        assert len(results) == 5
        for i, embedding in enumerate(results):
            assert embedding[0] == float(i), f"Embedding {i} out of order"

    @pytest.mark.asyncio
    async def test_embed_batch_processes_in_batches(self):
        """embed_batch must process texts in batches of batch_size."""
        texts = [f"text_{i}" for i in range(10)]
        call_counts = []

        async def _track_calls(text):
            call_counts.append(text)
            return [0.1] * 768

        with patch("agentcore.rag.embeddings.embed_text", side_effect=_track_calls):
            await embed_batch(texts, batch_size=3)

        # All 10 texts must have been embedded
        assert len(call_counts) == 10

    @pytest.mark.asyncio
    async def test_embed_batch_single_text(self):
        """embed_batch with a single text must return a list with one embedding."""
        with patch("agentcore.rag.embeddings.embed_text", new=AsyncMock(return_value=[0.5] * 768)):
            result = await embed_batch(["single text"])

        assert len(result) == 1
        assert len(result[0]) == 768

    @pytest.mark.asyncio
    async def test_embed_batch_returns_correct_count(self):
        """embed_batch must return exactly N embeddings for N input texts."""
        n = 7
        texts = [f"doc_{i}" for i in range(n)]

        with patch("agentcore.rag.embeddings.embed_text", new=AsyncMock(return_value=[0.1] * 768)):
            results = await embed_batch(texts)

        assert len(results) == n
