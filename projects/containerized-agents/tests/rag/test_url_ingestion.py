"""
RAG pipeline tests: URL scraping and content extraction (httpx mocked).
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

bs4 = pytest.importorskip("bs4")

from agentcore.rag.ingestion import ingest_url, DocumentChunk


class TestUrlIngestion:
    """URL ingestion tests with mocked httpx."""

    def _mock_http_response(self, html: str, status_code: int = 200):
        """Create a mock httpx response."""
        mock_resp = MagicMock()
        mock_resp.status_code = status_code
        mock_resp.text = html
        mock_resp.raise_for_status = MagicMock()
        if status_code >= 400:
            import httpx
            mock_resp.raise_for_status.side_effect = httpx.HTTPStatusError(
                f"HTTP {status_code}", request=MagicMock(), response=mock_resp
            )
        return mock_resp

    @pytest.mark.asyncio
    async def test_ingest_url_basic_html(self):
        """URL ingestion must extract text and return DocumentChunks."""
        html = """<html><body>
            <main>
                <p>This is the main content of the page. It contains useful information.</p>
                <p>More content here to ensure chunking works correctly across paragraphs.</p>
            </main>
        </body></html>"""

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=self._mock_http_response(html))
            mock_client_cls.return_value = mock_client

            with patch("agentcore.rag.ingestion.embed_batch", new=AsyncMock(return_value=[[0.1] * 768])):
                with patch("agentcore.rag.ingestion._get_chroma_client") as mock_chroma:
                    mock_collection = AsyncMock()
                    mock_chroma.return_value.get_or_create_collection = AsyncMock(return_value=mock_collection)
                    chunks = await ingest_url("https://example.com/page", "agent-123")

        assert len(chunks) >= 1
        assert all(isinstance(c, DocumentChunk) for c in chunks)

    @pytest.mark.asyncio
    async def test_ingest_url_metadata_includes_source(self):
        """Each chunk must include source and domain in metadata."""
        html = "<html><body><p>" + "Content. " * 50 + "</p></body></html>"

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=self._mock_http_response(html))
            mock_client_cls.return_value = mock_client

            chunks = await ingest_url("https://docs.example.com/guide", "agent-456")

        for chunk in chunks:
            assert chunk.metadata["source"] == "https://docs.example.com/guide"
            assert "domain" in chunk.metadata
            assert chunk.metadata["domain"] == "docs.example.com"

    @pytest.mark.asyncio
    async def test_ingest_url_strips_nav_footer_scripts(self):
        """Navigation, footer, scripts must be stripped from extracted text."""
        html = """<html><body>
            <nav>Navigation menu - should not appear</nav>
            <main>Actual content here</main>
            <footer>Footer content - should not appear</footer>
            <script>console.log('should not appear');</script>
        </body></html>"""

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=self._mock_http_response(html))
            mock_client_cls.return_value = mock_client

            chunks = await ingest_url("https://example.com", "agent-789")

        combined = " ".join(c.text for c in chunks)
        assert "Navigation menu" not in combined
        assert "Footer content" not in combined
        assert "console.log" not in combined
        assert "Actual content" in combined

    @pytest.mark.asyncio
    async def test_ingest_url_http_error_raises(self):
        """HTTP 404 from the target URL must raise HTTPStatusError."""
        import httpx

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_resp = self._mock_http_response("<html></html>", status_code=404)
            mock_client.get = AsyncMock(return_value=mock_resp)
            mock_client_cls.return_value = mock_client

            with pytest.raises(httpx.HTTPStatusError):
                await ingest_url("https://example.com/missing", "agent-000")

    @pytest.mark.asyncio
    async def test_ingest_url_empty_page_returns_no_chunks(self):
        """Empty page body must return zero chunks."""
        html = "<html><body></body></html>"

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=self._mock_http_response(html))
            mock_client_cls.return_value = mock_client

            chunks = await ingest_url("https://example.com/empty", "agent-000")

        assert chunks == []
