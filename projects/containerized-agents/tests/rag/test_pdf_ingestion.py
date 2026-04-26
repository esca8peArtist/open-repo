"""
RAG pipeline tests: ingest a minimal synthetic PDF, verify chunks stored.
"""
from __future__ import annotations

import io
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

bs4 = pytest.importorskip("bs4")

from agentcore.rag.ingestion import DocumentChunk, ingest_pdf, ingest_text


class TestPdfIngestion:
    """PDF ingestion tests using a minimal synthetic PDF."""

    def _make_minimal_pdf(self, tmp_path: Path, text: str = "Hello PDF content here.") -> Path:
        """Create a minimal PDF using pypdf or reportlab if available, otherwise skip."""
        try:
            from reportlab.pdfgen import canvas
            pdf_path = tmp_path / "test.pdf"
            c = canvas.Canvas(str(pdf_path))
            c.drawString(100, 750, text)
            c.save()
            return pdf_path
        except ImportError:
            pass

        # Fallback: use pypdf to create a very simple PDF
        try:
            from pypdf import PdfWriter
            writer = PdfWriter()
            writer.add_blank_page(width=612, height=792)
            pdf_path = tmp_path / "test.pdf"
            with open(pdf_path, "wb") as f:
                writer.write(f)
            return pdf_path
        except Exception:
            pytest.skip("Cannot create test PDF — reportlab or pypdf not available")

    @pytest.mark.asyncio
    async def test_ingest_pdf_returns_chunks(self, tmp_path):
        """ingest_pdf must return at least one DocumentChunk for a non-empty PDF."""
        try:
            from reportlab.pdfgen import canvas
            pdf_path = tmp_path / "content.pdf"
            c = canvas.Canvas(str(pdf_path))
            c.drawString(100, 750, "This is test content for RAG pipeline ingestion testing purposes.")
            c.save()
        except ImportError:
            pytest.skip("reportlab not available")

        chunks = await ingest_pdf(pdf_path, agent_id="agent-test")
        assert len(chunks) >= 1
        assert all(isinstance(c, DocumentChunk) for c in chunks)

    @pytest.mark.asyncio
    async def test_ingest_pdf_chunks_have_metadata(self, tmp_path):
        """Each PDF chunk must have source, page, chunk_index, doc_id, file_type metadata."""
        try:
            from reportlab.pdfgen import canvas
            pdf_path = tmp_path / "meta.pdf"
            c = canvas.Canvas(str(pdf_path))
            c.drawString(100, 750, "Sample content for metadata test.")
            c.save()
        except ImportError:
            pytest.skip("reportlab not available")

        chunks = await ingest_pdf(pdf_path, agent_id="agent-meta")
        for chunk in chunks:
            assert "source" in chunk.metadata
            assert "page" in chunk.metadata
            assert "chunk_index" in chunk.metadata
            assert "doc_id" in chunk.metadata
            assert chunk.metadata["file_type"] == "pdf"
            assert chunk.metadata["agent_id"] == "agent-meta"

    @pytest.mark.asyncio
    async def test_ingest_text_file_returns_chunks(self, tmp_path):
        """ingest_text must produce chunks from a plain text file."""
        text_file = tmp_path / "doc.txt"
        text_file.write_text("This is a test document.\n\n" + "More content. " * 50)

        chunks = await ingest_text(text_file, agent_id="agent-txt")
        assert len(chunks) >= 1
        assert all(isinstance(c, DocumentChunk) for c in chunks)

    @pytest.mark.asyncio
    async def test_ingest_text_metadata_correct(self, tmp_path):
        """ingest_text chunks must have correct file_type and agent_id."""
        text_file = tmp_path / "notes.txt"
        text_file.write_text("Test content " * 20)

        chunks = await ingest_text(text_file, agent_id="agent-123")
        for chunk in chunks:
            assert chunk.metadata["file_type"] == "txt"
            assert chunk.metadata["agent_id"] == "agent-123"
            assert chunk.metadata["source"] == str(text_file)

    @pytest.mark.asyncio
    async def test_ingest_document_raises_file_not_found(self):
        """ingest_document must raise FileNotFoundError for missing files."""
        from agentcore.rag.ingestion import ingest_document

        with pytest.raises(FileNotFoundError):
            await ingest_document("/nonexistent/path/to/file.pdf", "agent-000")

    @pytest.mark.asyncio
    async def test_ingest_document_raises_for_unsupported_type(self, tmp_path):
        """ingest_document must raise ValueError for unsupported file extensions."""
        from agentcore.rag.ingestion import ingest_document

        unsupported_file = tmp_path / "data.xyz"
        unsupported_file.write_text("data")

        with pytest.raises(ValueError, match="Unsupported"):
            await ingest_document(str(unsupported_file), "agent-000")
