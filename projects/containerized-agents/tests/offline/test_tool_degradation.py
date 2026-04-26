"""
Offline/degradation tests: every internet-requiring MCP tool must degrade gracefully.
"""
from __future__ import annotations

import pytest

from agentcore.mcp.protocol import MCPContext, MCPToolResult
from agentcore.mcp.tools.web_search import WebSearchTool
from agentcore.mcp.tools.calendar import GetCalendarEventsTool
from agentcore.mcp.tools.github import (
    SearchCodeTool,
    GetFileTool,
    CreateIssueTool,
    ListPullRequestsTool,
)


class TestInternetToolsOfflineDegradation:
    """Every tool with requires_internet=True must return a graceful error when offline."""

    @pytest.mark.asyncio
    async def test_web_search_offline_graceful(self, offline_context):
        """WebSearchTool must return success=False with an internet-related error."""
        tool = WebSearchTool()
        result = await tool.execute({"query": "anything"}, offline_context)
        assert isinstance(result, MCPToolResult)
        assert result.success is False
        assert result.error is not None
        assert "internet" in result.error.lower() or "online" in result.error.lower() or "connection" in result.error.lower()

    @pytest.mark.asyncio
    async def test_web_search_offline_no_exception(self, offline_context):
        """WebSearchTool must never raise an exception when offline."""
        tool = WebSearchTool()
        result = await tool.execute({"query": "test"}, offline_context)
        assert isinstance(result, MCPToolResult)

    @pytest.mark.asyncio
    async def test_calendar_offline_graceful(self, offline_context):
        """GetCalendarEventsTool must degrade when offline."""
        tool = GetCalendarEventsTool()
        result = await tool.execute(
            {"start_date": "2026-03-01T00:00:00", "end_date": "2026-03-31T23:59:59"},
            offline_context,
        )
        assert result.success is False
        assert result.error is not None

    @pytest.mark.asyncio
    async def test_github_search_code_offline(self, offline_context):
        """SearchCodeTool must degrade when offline."""
        tool = SearchCodeTool()
        result = await tool.execute({"query": "def main"}, offline_context)
        assert result.success is False
        assert "internet" in result.error.lower() or "connection" in result.error.lower()

    @pytest.mark.asyncio
    async def test_github_get_file_offline(self, offline_context):
        """GetFileTool must degrade when offline."""
        tool = GetFileTool()
        result = await tool.execute({"repo": "owner/repo", "path": "README.md"}, offline_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_github_create_issue_offline(self, offline_context):
        """CreateIssueTool must degrade when offline."""
        tool = CreateIssueTool()
        result = await tool.execute(
            {"repo": "owner/repo", "title": "Test", "body": "Test body"},
            offline_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_github_list_prs_offline(self, offline_context):
        """ListPullRequestsTool must degrade when offline."""
        tool = ListPullRequestsTool()
        result = await tool.execute({"repo": "owner/repo"}, offline_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_all_internet_tools_return_mcp_result(self, offline_context):
        """Every internet tool must return MCPToolResult (not raise) when offline."""
        tools_and_args = [
            (WebSearchTool(), {"query": "test"}),
            (GetCalendarEventsTool(), {"start_date": "2026-01-01T00:00:00", "end_date": "2026-01-31T23:59:59"}),
            (SearchCodeTool(), {"query": "main"}),
            (GetFileTool(), {"repo": "a/b", "path": "f.py"}),
            (CreateIssueTool(), {"repo": "a/b", "title": "t", "body": "b"}),
            (ListPullRequestsTool(), {"repo": "a/b"}),
        ]

        for tool, args in tools_and_args:
            result = await tool.execute(args, offline_context)
            assert isinstance(result, MCPToolResult), (
                f"{tool.schema.name} returned {type(result)} instead of MCPToolResult"
            )

    @pytest.mark.asyncio
    async def test_internet_tools_schema_declares_requires_internet(self):
        """All internet tools must declare requires_internet=True in their schema."""
        tools = [
            WebSearchTool(),
            GetCalendarEventsTool(),
            SearchCodeTool(),
            GetFileTool(),
            CreateIssueTool(),
            ListPullRequestsTool(),
        ]
        for tool in tools:
            assert tool.schema.requires_internet is True, (
                f"{tool.schema.name} does not declare requires_internet=True"
            )
