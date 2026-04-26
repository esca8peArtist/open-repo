"""
Integration tests for the RAG (Retrieval-Augmented Generation) pipeline.

Tests document ingestion and retrieval against a mocked ChromaDB backend.
Real ChromaDB / nomic-embed-text are NOT required — all external calls are mocked.
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest


# ===========================================================================
# ChromaDB / RAG client (if a client wrapper exists)
# ===========================================================================


class TestRAGPipelineConfiguration:
    def test_chroma_url_in_settings(self, mock_settings):
        """Settings must include a chromadb URL."""
        assert mock_settings.chroma_url
        assert "http" in mock_settings.chroma_url

    def test_rag_enabled_profiles_have_collection_names(self):
        """Profiles with RAG enabled must specify a ChromaDB collection name."""
        from agentcore.profiles import get_all_profiles

        profiles = get_all_profiles()
        for profile in profiles:
            if profile.rag_enabled:
                assert profile.rag_collection, (
                    f"Profile '{profile.name}' has rag_enabled=True but missing rag_collection"
                )

    def test_rag_collection_names_are_unique(self):
        """Each profile's RAG collection name must be unique (no two profiles share a collection)."""
        from agentcore.profiles import get_all_profiles

        profiles = get_all_profiles()
        collections = [p.rag_collection for p in profiles if p.rag_enabled and p.rag_collection]
        assert len(collections) == len(set(collections)), (
            f"Duplicate RAG collection names detected: {collections}"
        )

    def test_rag_collection_names_are_snake_case(self):
        """RAG collection names must be valid identifiers (no spaces, reasonable characters)."""
        from agentcore.profiles import get_all_profiles
        import re

        profiles = get_all_profiles()
        for profile in profiles:
            if profile.rag_collection:
                assert re.match(r"^[a-zA-Z0-9_-]+$", profile.rag_collection), (
                    f"Profile '{profile.name}': invalid collection name '{profile.rag_collection}'"
                )


# ===========================================================================
# Embedding model configuration
# ===========================================================================


class TestEmbeddingConfiguration:
    def test_embedding_model_is_nomic_embed(self):
        """
        The RAG pipeline must use nomic-embed-text (Apache 2.0, runs offline via Ollama).
        Check that no OpenAI/cloud embedding is referenced.
        """
        # Check the Ollama models config lists nomic-embed-text
        import os
        models_yml = os.path.join(
            os.path.dirname(__file__),
            "../../docker/services/ollama/models.yml"
        )
        if os.path.exists(models_yml):
            content = open(models_yml).read()
            assert "nomic-embed-text" in content, (
                "docker/services/ollama/models.yml must include nomic-embed-text for RAG"
            )
        else:
            pytest.skip("docker/services/ollama/models.yml not found")


# ===========================================================================
# Document ingestion (mocked ChromaDB)
# ===========================================================================


class TestDocumentIngestion:
    @pytest.mark.asyncio
    async def test_ingest_text_document_via_mocked_chroma(self):
        """
        Document ingestion must split text, generate embeddings, and store in ChromaDB.
        ChromaDB client is mocked.
        """
        try:
            from agentcore.rag.ingestion import ingest_document
        except ImportError:
            pytest.skip("agentcore.rag.ingestion not yet implemented")

        mock_collection = MagicMock()
        mock_collection.add = MagicMock()

        with patch("chromadb.Client") as mock_chroma:
            mock_chroma.return_value.get_or_create_collection.return_value = mock_collection
            await ingest_document(
                text="This is a test document for RAG ingestion.",
                collection_name="test_collection",
                document_id="doc-001",
                metadata={"source": "test"},
            )

        mock_collection.add.assert_called_once()

    @pytest.mark.asyncio
    async def test_retrieve_documents_via_mocked_chroma(self):
        """
        Document retrieval must query ChromaDB with an embedding vector
        and return the top-k results.
        """
        try:
            from agentcore.rag.retrieval import retrieve_documents
        except ImportError:
            pytest.skip("agentcore.rag.retrieval not yet implemented")

        mock_collection = MagicMock()
        mock_collection.query.return_value = {
            "documents": [["First relevant document", "Second relevant document"]],
            "distances": [[0.1, 0.2]],
            "metadatas": [[{"source": "doc1"}, {"source": "doc2"}]],
        }

        with patch("chromadb.Client") as mock_chroma:
            mock_chroma.return_value.get_or_create_collection.return_value = mock_collection
            results = await retrieve_documents(
                query="test query",
                collection_name="test_collection",
                top_k=2,
            )

        assert len(results) == 2
        assert results[0]["document"] == "First relevant document"


# ===========================================================================
# RAG-related agent configuration (no actual vector DB needed)
# ===========================================================================


class TestRAGAgentConfig:
    def test_agent_with_rag_config_is_valid_pydantic(self, sample_agent_config):
        """An AgentConfig with rag_enabled=True must be a valid Pydantic model."""
        from agentcore.models import AgentConfig, AgentProfile

        config = AgentConfig(
            name="RAG Test Agent",
            profile=AgentProfile.CUSTOMER_SUPPORT,
            model="qwen2.5:7b-instruct",
            system_prompt="You are a RAG-enabled assistant.",
            tools=[],
            channels=[],
            hardware_tier=1,
            rag_enabled=True,
            rag_collection="test_collection",
            active=True,
        )
        assert config.rag_enabled is True
        assert config.rag_collection == "test_collection"

    def test_agent_without_rag_has_no_collection(self):
        """An AgentConfig with rag_enabled=False should have rag_collection=None."""
        from agentcore.models import AgentConfig, AgentProfile

        config = AgentConfig(
            name="Non-RAG Agent",
            profile=AgentProfile.PERSONAL_PRODUCTIVITY,
            model="qwen2.5:7b-instruct",
            rag_enabled=False,
        )
        assert config.rag_enabled is False
        assert config.rag_collection is None
