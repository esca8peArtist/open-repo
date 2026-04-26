"""
Offline tests: core agent features work without internet access.
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.tools.crm import SearchContactsTool, GetContactTool
from agentcore.mcp.tools.scheduler import ScheduleTaskTool, ListScheduledTasksTool
from agentcore.mcp.tools.filesystem import ReadFileTool
from agentcore.mcp.tools.database import QueryDatabaseTool


class TestOfflineToolsWork:
    """Tools that don't require internet must work when offline."""

    @pytest.mark.asyncio
    async def test_crm_search_offline(self, offline_context, crm_db_path):
        """CRM search must work offline (uses local SQLite)."""
        tool = SearchContactsTool()
        with patch.dict("os.environ", {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute({"query": "test"}, offline_context)
        assert result.success is True
        assert result.content["contacts"] == []  # empty DB

    @pytest.mark.asyncio
    async def test_scheduler_list_offline(self, offline_context, tmp_path):
        """Scheduler list must work offline (uses local SQLite)."""
        tool = ListScheduledTasksTool()
        db_path = str(tmp_path / "sched.db")
        with patch.dict("os.environ", {"SCHEDULER_DB_URL": "", "DB_POSTGRES_URL": ""}):
            # Force SQLite fallback path
            with patch("agentcore.mcp.tools.scheduler._SQLITE_FALLBACK", db_path):
                result = await tool.execute({}, offline_context)
        assert result.success is True
        assert result.content["tasks"] == []

    @pytest.mark.asyncio
    async def test_crm_schema_does_not_require_internet(self):
        """CRM tools must declare requires_internet=False."""
        for tool in [SearchContactsTool(), GetContactTool()]:
            assert tool.schema.requires_internet is False

    @pytest.mark.asyncio
    async def test_scheduler_schema_does_not_require_internet(self):
        """Scheduler tools must declare requires_internet=False."""
        for tool in [ScheduleTaskTool(), ListScheduledTasksTool()]:
            assert tool.schema.requires_internet is False

    @pytest.mark.asyncio
    async def test_database_tool_schema_does_not_require_internet(self):
        """QueryDatabaseTool must declare requires_internet=False."""
        tool = QueryDatabaseTool()
        assert tool.schema.requires_internet is False


class TestAgentCoreOffline:
    """Agent inference path must work without internet if Ollama is local."""

    @pytest.mark.asyncio
    async def test_agent_chat_offline_no_tools(self, agent_instance, offline_context):
        """Agent chat must work offline when no internet tools are needed."""
        response = await agent_instance.chat(
            "Hello, what is 2+2?",
            session_id="offline-test",
            stream=False,
        )
        assert response is not None
        assert response.message is not None
        assert len(response.message) > 0

    @pytest.mark.asyncio
    async def test_agent_session_cleared_offline(self, agent_instance):
        """clear_session must work without internet access."""
        session_id = "test-session-clear"
        agent_instance.clear_session(session_id)
        # No exception means success
        messages = agent_instance.get_session_messages(session_id)
        assert messages == []

    @pytest.mark.asyncio
    async def test_rag_retrieval_returns_empty_offline(self):
        """RAG retrieval must return empty list gracefully when ChromaDB is unavailable."""
        pytest.importorskip("chromadb", reason="chromadb not installed")
        from agentcore.rag.retrieval import retrieve

        with patch("agentcore.rag.retrieval.get_chroma_client") as mock_chroma:
            mock_client = MagicMock()
            mock_client.get_collection = AsyncMock(side_effect=Exception("ChromaDB unavailable"))
            mock_chroma.return_value = mock_client

            results = await retrieve("test query", agent_id="test-agent")

        assert results == []
