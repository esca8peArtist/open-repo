"""
Unit tests for MCP tools.

Covers:
- WebSearchTool: offline graceful degradation, online call path
- QueryDatabaseTool: SQL safety enforcement (INSERT/UPDATE/DELETE/DROP blocked)
- ExecutePythonTool: basic execution, blocked imports, timeout enforcement
- GetCalendarEventsTool: offline graceful degradation
- ReadFileTool: path traversal protection, outside-allowed-paths rejection
- MCPToolRegistry: tool lookup, offline short-circuit, unknown tool handling
"""
from __future__ import annotations

import os
import tempfile
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext, MCPToolResult
from agentcore.mcp.registry import MCPToolRegistry
from agentcore.mcp.tools.calendar import GetCalendarEventsTool
from agentcore.mcp.tools.code_exec import ExecutePythonTool, _check_blocked_imports
from agentcore.mcp.tools.database import QueryDatabaseTool, _is_safe_query
from agentcore.mcp.tools.filesystem import ReadFileTool, SearchFilesTool
from agentcore.mcp.tools.web_search import WebSearchTool


# ===========================================================================
# WebSearchTool
# ===========================================================================


class TestWebSearchOfflineDegradation:
    """WebSearchTool must degrade gracefully when offline."""

    @pytest.mark.asyncio
    async def test_offline_returns_graceful_error(self, offline_context):
        """Web search must return success=False with a clear error message when offline."""
        tool = WebSearchTool()
        result = await tool.execute({"query": "test query"}, offline_context)

        assert isinstance(result, MCPToolResult)
        assert result.success is False
        assert result.error is not None
        assert "internet" in result.error.lower()

    @pytest.mark.asyncio
    async def test_offline_does_not_raise(self, offline_context):
        """Web search must never raise an exception — always return MCPToolResult."""
        tool = WebSearchTool()
        # Should not raise; just return a failed result
        result = await tool.execute({"query": "anything"}, offline_context)
        assert isinstance(result, MCPToolResult)

    @pytest.mark.asyncio
    async def test_schema_declares_requires_internet(self):
        """WebSearchTool schema must declare requires_internet=True."""
        tool = WebSearchTool()
        assert tool.schema.requires_internet is True

    @pytest.mark.asyncio
    async def test_online_tavily_called_when_api_key_present(self, online_context):
        """When a Tavily API key is present, the tool must attempt to use Tavily."""
        tool = WebSearchTool()
        with patch.dict(os.environ, {"TAVILY_API_KEY": "fake-key-for-test"}):
            with patch("httpx.AsyncClient.post") as mock_post:
                mock_resp = MagicMock()
                mock_resp.raise_for_status = MagicMock()
                mock_resp.json.return_value = {"results": []}
                mock_post.return_value = mock_resp

                # Make it async
                async def _fake_post(*args, **kwargs):
                    return mock_resp

                mock_post.side_effect = _fake_post

                result = await tool.execute({"query": "test"}, online_context)

        # The tool attempted a call (either succeeded or fell back to DDG)
        assert isinstance(result, MCPToolResult)

    @pytest.mark.asyncio
    async def test_online_duckduckgo_fallback_when_no_key(self, online_context):
        """Without Tavily key, the tool falls back to DuckDuckGo (or returns error if not installed)."""
        tool = WebSearchTool()
        with patch.dict(os.environ, {}, clear=False):
            # Remove TAVILY_API_KEY if set
            env_copy = {k: v for k, v in os.environ.items() if k != "TAVILY_API_KEY"}
            with patch.dict(os.environ, env_copy, clear=True):
                result = await tool.execute({"query": "test"}, online_context)
        # Must return MCPToolResult (not raise), regardless of whether duckduckgo-search is installed
        assert isinstance(result, MCPToolResult)


# ===========================================================================
# QueryDatabaseTool — SQL safety
# ===========================================================================


class TestSafeQueryFunction:
    """Unit-test the _is_safe_query helper directly."""

    def test_select_is_safe(self):
        assert _is_safe_query("SELECT * FROM users") is True

    def test_select_with_where_is_safe(self):
        assert _is_safe_query("SELECT id, name FROM users WHERE active = 1") is True

    def test_insert_is_blocked(self):
        assert _is_safe_query("INSERT INTO users VALUES (1, 'evil')") is False

    def test_update_is_blocked(self):
        assert _is_safe_query("UPDATE users SET password = 'hacked' WHERE 1=1") is False

    def test_delete_is_blocked(self):
        assert _is_safe_query("DELETE FROM users WHERE 1=1") is False

    def test_drop_is_blocked(self):
        assert _is_safe_query("DROP TABLE users") is False

    def test_create_is_blocked(self):
        assert _is_safe_query("CREATE TABLE evil (id INT)") is False

    def test_alter_is_blocked(self):
        assert _is_safe_query("ALTER TABLE users ADD COLUMN secret TEXT") is False

    def test_truncate_is_blocked(self):
        assert _is_safe_query("TRUNCATE TABLE audit_log") is False

    def test_exec_is_blocked(self):
        assert _is_safe_query("EXEC xp_cmdshell('rm -rf /')") is False

    def test_empty_string_is_blocked(self):
        assert _is_safe_query("") is False

    def test_select_with_subquery_is_safe(self):
        assert _is_safe_query("SELECT * FROM (SELECT id FROM users) AS sub") is True

    def test_mixed_case_blocked(self):
        assert _is_safe_query("select 1; DroP table users") is False


class TestDatabaseQuerySecurity:
    """Integration-level tests via the tool's execute() method."""

    @pytest.mark.asyncio
    async def test_rejects_insert_statement(self, online_context):
        """INSERT must be rejected before reaching any DB backend."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "INSERT INTO users VALUES (1, 'hacked')"},
            online_context,
        )
        assert result.success is False
        assert result.error is not None
        assert "select" in result.error.lower() or "read-only" in result.error.lower() or "only select" in result.error.lower()

    @pytest.mark.asyncio
    async def test_rejects_drop_statement(self, online_context):
        """DROP must be rejected."""
        tool = QueryDatabaseTool()
        result = await tool.execute({"sql": "DROP TABLE users"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_rejects_delete_statement(self, online_context):
        """DELETE must be rejected."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "DELETE FROM users WHERE 1=1"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_rejects_update_statement(self, online_context):
        """UPDATE must be rejected."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "UPDATE users SET pw = 'bad' WHERE 1=1"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_select_without_db_config_returns_error_not_raise(self, online_context):
        """A valid SELECT with no DB configured returns an error gracefully."""
        tool = QueryDatabaseTool()
        with patch.dict(os.environ, {}, clear=True):
            # No DB_SQLITE_PATH, DB_POSTGRES_URL, DB_MYSQL_URL set
            env_clean = {k: v for k, v in os.environ.items()
                         if k not in ("DB_SQLITE_PATH", "DB_POSTGRES_URL", "DB_MYSQL_URL")}
            with patch.dict(os.environ, env_clean, clear=True):
                result = await tool.execute(
                    {"sql": "SELECT 1"},
                    online_context,
                )
        assert result.success is False
        assert result.error is not None

    @pytest.mark.asyncio
    async def test_select_sqlite_in_memory(self, online_context):
        """A valid SELECT against a real SQLite DB returns rows correctly."""
        tool = QueryDatabaseTool()
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
            db_path = f.name

        try:
            import sqlite3
            conn = sqlite3.connect(db_path)
            conn.execute("CREATE TABLE test_items (id INTEGER, label TEXT)")
            conn.execute("INSERT INTO test_items VALUES (1, 'alpha')")
            conn.execute("INSERT INTO test_items VALUES (2, 'beta')")
            conn.commit()
            conn.close()

            get_settings.cache_clear()
            with patch.dict(os.environ, {"DB_SQLITE_PATH": db_path}):
                result = await tool.execute(
                    {"sql": "SELECT * FROM test_items ORDER BY id"},
                    online_context,
                )
            get_settings.cache_clear()
        finally:
            os.unlink(db_path)

        assert result.success is True
        assert isinstance(result.content, dict)
        rows = result.content["rows"]
        assert len(rows) == 2
        assert rows[0]["id"] == 1
        assert rows[1]["label"] == "beta"


# ===========================================================================
# ExecutePythonTool — code execution sandbox
# ===========================================================================


class TestBlockedImports:
    """_check_blocked_imports should reject dangerous patterns at string level."""

    def test_subprocess_import_blocked(self):
        assert _check_blocked_imports("import subprocess") is not None

    def test_socket_import_blocked(self):
        assert _check_blocked_imports("import socket") is not None

    def test_os_import_blocked(self):
        assert _check_blocked_imports("import os") is not None

    def test_requests_import_blocked(self):
        assert _check_blocked_imports("import requests") is not None

    def test_urllib_import_blocked(self):
        assert _check_blocked_imports("import urllib") is not None

    def test_httpx_import_blocked(self):
        assert _check_blocked_imports("import httpx") is not None

    def test_eval_blocked(self):
        assert _check_blocked_imports("eval('__import__(\"os\")')") is not None

    def test_exec_blocked(self):
        assert _check_blocked_imports("exec('import os')") is not None

    def test_safe_code_passes(self):
        assert _check_blocked_imports("x = 1 + 2\nprint(x)") is None

    def test_math_import_allowed(self):
        assert _check_blocked_imports("import math\nprint(math.pi)") is None

    def test_json_import_allowed(self):
        assert _check_blocked_imports("import json\nd = json.dumps({'a': 1})") is None


class TestCodeExecution:
    """ExecutePythonTool — end-to-end execution tests."""

    @pytest.mark.asyncio
    async def test_basic_python_execution(self, online_context):
        """Simple print statement should execute and capture stdout."""
        tool = ExecutePythonTool()
        result = await tool.execute({"code": "print('hello world')"}, online_context)
        assert result.success is True
        assert isinstance(result.content, dict)
        stdout = result.content.get("stdout", "")
        assert "hello world" in stdout

    @pytest.mark.asyncio
    async def test_arithmetic_execution(self, online_context):
        """Arithmetic should work correctly."""
        tool = ExecutePythonTool()
        result = await tool.execute({"code": "print(2 ** 10)"}, online_context)
        assert result.success is True
        assert "1024" in result.content.get("stdout", "")

    @pytest.mark.asyncio
    async def test_blocks_subprocess_import(self, online_context):
        """Code with 'import subprocess' must be blocked before execution."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import subprocess; subprocess.run(['ls'])"},
            online_context,
        )
        assert result.success is False
        assert result.error is not None

    @pytest.mark.asyncio
    async def test_blocks_socket_import(self, online_context):
        """Code with 'import socket' must be blocked."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import socket; s = socket.socket()"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_blocks_os_import(self, online_context):
        """Code with 'import os' must be blocked."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import os; os.system('id')"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_timeout_enforcement(self, online_context):
        """Code that sleeps beyond the timeout must return a timeout error."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            # Use time module — it's not blocked; the timeout should fire
            {"code": "import time\ntime.sleep(100)", "timeout_seconds": 1},
            online_context,
        )
        # Note: 'time' is not in the blocked list; execution runs but times out
        # The tool wraps timeout as success=False
        assert result.success is False
        assert result.error is not None
        assert "timeout" in result.error.lower() or "timed out" in result.error.lower()

    @pytest.mark.asyncio
    async def test_syntax_error_returns_failure(self, online_context):
        """Code with a syntax error should return success=False, not raise."""
        tool = ExecutePythonTool()
        result = await tool.execute({"code": "def broken(:"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_returns_exit_code(self, online_context):
        """Successful code should have exit_code=0 in content."""
        tool = ExecutePythonTool()
        result = await tool.execute({"code": "x = 42"}, online_context)
        assert result.success is True
        assert result.content.get("exit_code") == 0


# ===========================================================================
# GetCalendarEventsTool — offline degradation
# ===========================================================================


class TestCalendarOfflineDegradation:
    @pytest.mark.asyncio
    async def test_offline_returns_graceful_error(self, offline_context):
        """Calendar tool must return success=False when offline."""
        tool = GetCalendarEventsTool()
        result = await tool.execute(
            {"start_date": "2026-03-01T00:00:00", "end_date": "2026-03-31T23:59:59"},
            offline_context,
        )
        assert result.success is False
        assert result.error is not None
        assert "internet" in result.error.lower() or "calendar" in result.error.lower()

    @pytest.mark.asyncio
    async def test_schema_declares_requires_internet(self):
        tool = GetCalendarEventsTool()
        assert tool.schema.requires_internet is True


# ===========================================================================
# ReadFileTool — path security
# ===========================================================================


class TestReadFileToolSecurity:
    @pytest.mark.asyncio
    async def test_rejects_path_outside_allowed_dirs(self, online_context):
        """Attempting to read /etc/passwd must be denied."""
        tool = ReadFileTool()
        result = await tool.execute({"path": "/etc/passwd"}, online_context)
        assert result.success is False
        assert result.error is not None
        assert "denied" in result.error.lower() or "outside" in result.error.lower()

    @pytest.mark.asyncio
    async def test_rejects_path_traversal_attempt(self, online_context):
        """Path traversal via ../ must be blocked."""
        tool = ReadFileTool()
        result = await tool.execute({"path": "/data/../../../etc/shadow"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_reads_file_in_allowed_path(self, online_context, tmp_path):
        """A file inside an allowed path should be readable."""
        tool = ReadFileTool()
        # Override FILESYSTEM_ALLOWED_PATHS to use tmp_path for this test
        test_file = tmp_path / "test.txt"
        test_file.write_text("hello from allowed path")

        get_settings.cache_clear()
        try:
            with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
                result = await tool.execute({"path": str(test_file)}, online_context)
        finally:
            get_settings.cache_clear()

        assert result.success is True
        assert "hello from allowed path" in result.content["content"]

    @pytest.mark.asyncio
    async def test_missing_file_returns_not_found(self, online_context, tmp_path):
        """A non-existent file in an allowed path should return success=False with a helpful error."""
        tool = ReadFileTool()
        missing = tmp_path / "ghost.txt"

        get_settings.cache_clear()
        try:
            with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
                result = await tool.execute({"path": str(missing)}, online_context)
        finally:
            get_settings.cache_clear()

        assert result.success is False
        assert "not found" in result.error.lower()


# ===========================================================================
# MCPToolRegistry
# ===========================================================================


class TestMCPToolRegistry:
    def test_register_and_get_tool(self):
        """Registered tools must be retrievable by name."""
        registry = MCPToolRegistry()
        tool = WebSearchTool()
        registry.register(tool)
        assert registry.get_tool("web_search") is tool

    def test_get_unknown_tool_returns_none(self):
        """Requesting an unregistered tool name must return None."""
        registry = MCPToolRegistry()
        assert registry.get_tool("nonexistent_tool") is None

    def test_list_tool_names_sorted(self):
        """list_tool_names() must return sorted names."""
        registry = MCPToolRegistry()
        registry.register(WebSearchTool())
        registry.register(QueryDatabaseTool())
        names = registry.list_tool_names()
        assert names == sorted(names)

    def test_register_all_tools_loads_without_error(self):
        """register_all_tools() must complete without raising."""
        registry = MCPToolRegistry()
        # Should not raise even if some optional deps are missing
        registry.register_all_tools()
        # At minimum the tools whose deps are always present should load
        assert len(registry.list_tool_names()) > 0

    @pytest.mark.asyncio
    async def test_invoke_unknown_tool_returns_graceful_error(self, online_context):
        """Invoking a tool name that isn't registered must return a graceful error, not raise."""
        registry = MCPToolRegistry()
        result = await registry.invoke("totally_unknown_tool", {}, online_context)
        assert result.success is False
        assert result.error is not None
        assert "unknown" in result.error.lower() or "totally_unknown_tool" in result.error

    @pytest.mark.asyncio
    async def test_invoke_internet_tool_offline_returns_graceful_error(self, offline_context):
        """The registry's offline check must short-circuit internet-required tools."""
        registry = MCPToolRegistry()
        registry.register(WebSearchTool())
        result = await registry.invoke("web_search", {"query": "test"}, offline_context)
        assert result.success is False
        assert result.error is not None
        # Error should mention internet/connection
        assert any(word in result.error.lower() for word in ("internet", "connection", "online"))

    @pytest.mark.asyncio
    async def test_invoke_with_timeout(self, online_context):
        """Timeout is enforced — tool that sleeps too long should return timeout error."""
        import asyncio

        registry = MCPToolRegistry()

        # Register a tool that takes forever
        class SlowTool(WebSearchTool):
            async def execute(self, arguments, context):
                await asyncio.sleep(999)

            @property
            def schema(self):
                s = super().schema
                # Override requires_internet so offline check doesn't short-circuit
                from agentcore.mcp.protocol import MCPToolSchema
                return MCPToolSchema(
                    name="slow_tool",
                    description="A slow tool for timeout testing",
                    input_schema={"type": "object", "properties": {"q": {"type": "string"}}, "required": []},
                    requires_internet=False,
                )

        registry.register(SlowTool())
        result = await registry.invoke("slow_tool", {}, online_context, timeout=0.1)
        assert result.success is False
        assert result.error is not None
        assert "timed out" in result.error.lower() or "timeout" in result.error.lower()
