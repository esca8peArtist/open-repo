"""
Integration tests: internet-dependent tools fail gracefully offline.

This file focuses exclusively on verifying that every internet-requiring MCP tool
returns a well-formed error (not an exception, not a crash) when the device is
offline, and that the error message is user-readable.
"""
from __future__ import annotations

import pytest

from agentcore.mcp.protocol import MCPContext, MCPToolResult
from agentcore.mcp.registry import MCPToolRegistry
from agentcore.mcp.tools.calendar import CreateCalendarEventTool, GetCalendarEventsTool
from agentcore.mcp.tools.email import SendEmailTool
from agentcore.mcp.tools.github import (
    CreateIssueTool,
    GetFileTool,
    ListPullRequestsTool,
    SearchCodeTool,
)
from agentcore.mcp.tools.web_search import WebSearchTool


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------


def _offline() -> MCPContext:
    return MCPContext(agent_id="test", session_id="test", is_online=False)


def _assert_graceful_failure(result: MCPToolResult, tool_name: str) -> None:
    """Assert that a result represents a graceful offline failure."""
    assert isinstance(result, MCPToolResult), (
        f"{tool_name}: execute() must return MCPToolResult, not raise"
    )
    assert result.success is False, (
        f"{tool_name}: success must be False when offline"
    )
    assert result.error is not None, (
        f"{tool_name}: error message must not be None when offline"
    )
    assert len(result.error) >= 5, (
        f"{tool_name}: error message too short to be user-readable: {result.error!r}"
    )


# ===========================================================================
# WebSearchTool
# ===========================================================================


class TestWebSearchGracefulDegradation:
    @pytest.mark.asyncio
    async def test_offline_graceful_failure(self):
        tool = WebSearchTool()
        result = await tool.execute({"query": "latest news"}, _offline())
        _assert_graceful_failure(result, "web_search")

    @pytest.mark.asyncio
    async def test_offline_error_mentions_internet(self):
        tool = WebSearchTool()
        result = await tool.execute({"query": "test"}, _offline())
        assert "internet" in result.error.lower() or "connection" in result.error.lower(), (
            f"Error should mention internet/connection: {result.error!r}"
        )

    @pytest.mark.asyncio
    async def test_requires_internet_flag_in_schema(self):
        assert WebSearchTool().schema.requires_internet is True


# ===========================================================================
# CalendarTool
# ===========================================================================


class TestCalendarGracefulDegradation:
    @pytest.mark.asyncio
    async def test_get_events_offline_graceful(self):
        tool = GetCalendarEventsTool()
        result = await tool.execute(
            {"start_date": "2026-03-01T00:00:00", "end_date": "2026-03-31T23:59:59"},
            _offline(),
        )
        _assert_graceful_failure(result, "get_calendar_events")

    @pytest.mark.asyncio
    async def test_create_event_offline_graceful(self):
        tool = CreateCalendarEventTool()
        result = await tool.execute(
            {
                "title": "Test Meeting",
                "start": "2026-03-15T10:00:00",
                "end": "2026-03-15T11:00:00",
            },
            _offline(),
        )
        _assert_graceful_failure(result, "create_calendar_event")

    @pytest.mark.asyncio
    async def test_calendar_tools_require_internet_flag(self):
        assert GetCalendarEventsTool().schema.requires_internet is True
        assert CreateCalendarEventTool().schema.requires_internet is True


# ===========================================================================
# GitHub tools
# ===========================================================================


class TestGitHubToolsGracefulDegradation:
    @pytest.mark.asyncio
    async def test_search_code_offline_graceful(self):
        tool = SearchCodeTool()
        result = await tool.execute({"query": "def process_data"}, _offline())
        _assert_graceful_failure(result, "search_code")

    @pytest.mark.asyncio
    async def test_get_file_offline_graceful(self):
        tool = GetFileTool()
        result = await tool.execute(
            {"repo": "owner/repo", "path": "README.md"},
            _offline(),
        )
        _assert_graceful_failure(result, "get_file")

    @pytest.mark.asyncio
    async def test_create_issue_offline_graceful(self):
        tool = CreateIssueTool()
        result = await tool.execute(
            {"repo": "owner/repo", "title": "Bug report", "body": "Something is broken"},
            _offline(),
        )
        _assert_graceful_failure(result, "create_issue")

    @pytest.mark.asyncio
    async def test_list_pull_requests_offline_graceful(self):
        tool = ListPullRequestsTool()
        result = await tool.execute({"repo": "owner/repo"}, _offline())
        _assert_graceful_failure(result, "list_pull_requests")

    @pytest.mark.asyncio
    async def test_github_tools_require_internet_flag(self):
        assert SearchCodeTool().schema.requires_internet is True
        assert GetFileTool().schema.requires_internet is True
        assert CreateIssueTool().schema.requires_internet is True
        assert ListPullRequestsTool().schema.requires_internet is True


# ===========================================================================
# Email tool (SMTP/IMAP — LAN-capable but can require internet for external)
# ===========================================================================


class TestEmailGracefulDegradation:
    @pytest.mark.asyncio
    async def test_send_email_schema_exists(self):
        """SendEmailTool must have a valid schema regardless of online status."""
        tool = SendEmailTool()
        schema = tool.schema
        assert schema.name == "send_email"
        assert schema.input_schema is not None

    @pytest.mark.asyncio
    async def test_send_email_without_smtp_config_fails_gracefully(self):
        """SendEmailTool without SMTP credentials must fail gracefully, not raise."""
        import os
        tool = SendEmailTool()
        # Clear SMTP config
        env_clean = {k: v for k, v in os.environ.items()
                     if k not in ("SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD", "SMTP_PORT")}
        online_ctx = MCPContext(agent_id="test", session_id="test", is_online=True)
        with __import__("unittest.mock", fromlist=["patch"]).patch.dict(os.environ, env_clean, clear=True):
            result = await tool.execute(
                {
                    "to": "test@example.com",
                    "subject": "Test",
                    "body": "Test body",
                },
                online_ctx,
            )
        # Must return MCPToolResult (not raise)
        assert isinstance(result, MCPToolResult)


# ===========================================================================
# Registry-level offline check
# ===========================================================================


class TestRegistryOfflineShortCircuit:
    @pytest.mark.asyncio
    async def test_all_internet_tools_blocked_via_registry(self):
        """
        Invoking every internet-requiring tool via the registry in offline mode
        must return graceful errors for all of them.
        """
        registry = MCPToolRegistry()
        registry.register_all_tools()

        offline_ctx = _offline()
        internet_tools = [
            name for name in registry.list_tool_names()
            if registry.get_tool(name).schema.requires_internet
        ]

        assert len(internet_tools) >= 1, "Expected at least some internet-requiring tools registered"

        for tool_name in internet_tools:
            # Build minimal valid arguments based on tool schema
            tool = registry.get_tool(tool_name)
            required_keys = tool.schema.input_schema.get("required", [])
            props = tool.schema.input_schema.get("properties", {})
            args = {}
            for key in required_keys:
                prop = props.get(key, {})
                if prop.get("type") == "string":
                    args[key] = "test"
                elif prop.get("type") == "integer":
                    args[key] = 1
                elif prop.get("type") == "array":
                    args[key] = []
                elif prop.get("type") == "object":
                    args[key] = {}

            result = await registry.invoke(tool_name, args, offline_ctx)
            assert result.success is False, (
                f"Registry must block '{tool_name}' when offline, but got success=True"
            )
            assert result.error is not None, (
                f"Registry must provide error message for '{tool_name}' when offline"
            )

    @pytest.mark.asyncio
    async def test_offline_tools_not_blocked_by_registry(self):
        """
        Offline-capable tools (requires_internet=False) must NOT be blocked
        by the registry's offline check — they should attempt execution.
        """
        registry = MCPToolRegistry()
        registry.register_all_tools()

        offline_ctx = _offline()
        offline_tools = [
            name for name in registry.list_tool_names()
            if not registry.get_tool(name).schema.requires_internet
        ]

        # The registry should attempt to execute offline tools
        # (they may fail for other reasons, but NOT for "offline" reasons)
        for tool_name in offline_tools[:3]:  # Test just the first few
            tool = registry.get_tool(tool_name)
            required_keys = tool.schema.input_schema.get("required", [])
            props = tool.schema.input_schema.get("properties", {})
            args = {}
            for key in required_keys:
                prop = props.get(key, {})
                if prop.get("type") == "string":
                    args[key] = "test_value"
                elif prop.get("type") == "integer":
                    args[key] = 1

            result = await registry.invoke(tool_name, args, offline_ctx)
            # If it failed, it should NOT be because of the offline check
            if not result.success and result.error:
                assert "internet" not in result.error.lower() or "connection" not in result.error.lower(), (
                    f"Offline tool '{tool_name}' was incorrectly blocked by the offline check"
                )
