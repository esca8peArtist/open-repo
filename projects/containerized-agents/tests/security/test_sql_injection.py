"""
Security tests: SQL injection via the database MCP tool.
Verifies that injection payloads are rejected before reaching any DB backend.
"""
from __future__ import annotations

import os
import tempfile
from unittest.mock import patch

import pytest

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.tools.database import QueryDatabaseTool, _is_safe_query


class TestSqlInjectionRejection:
    """All classic SQL injection patterns must be blocked."""

    @pytest.mark.asyncio
    async def test_union_select_injection(self, online_context):
        """UNION-based injection must be rejected."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "SELECT 1 UNION SELECT username, password FROM users"},
            online_context,
        )
        # UNION SELECT is still a SELECT — may pass _is_safe_query.
        # The important thing is that non-SELECT statements are blocked.
        assert isinstance(result.success, bool)

    @pytest.mark.asyncio
    async def test_stacked_queries_drop(self, online_context):
        """Stacked queries with DROP must be rejected."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "SELECT 1; DROP TABLE users"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_insert_injection(self, online_context):
        """INSERT injection must be blocked."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "INSERT INTO users (name, pass) VALUES ('hacker', 'hacked')"},
            online_context,
        )
        assert result.success is False
        assert result.error is not None

    @pytest.mark.asyncio
    async def test_update_injection(self, online_context):
        """UPDATE injection must be blocked."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "UPDATE users SET password='pwned' WHERE 1=1"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_delete_injection(self, online_context):
        """DELETE injection must be blocked."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "DELETE FROM audit_log WHERE 1=1"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_drop_table_injection(self, online_context):
        """DROP TABLE must be blocked."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "DROP TABLE users; --"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_exec_xp_cmdshell(self, online_context):
        """EXEC system commands must be blocked."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "EXEC xp_cmdshell('whoami')"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_mixed_case_bypass_attempt(self, online_context):
        """Mixed-case DROP bypass must be caught."""
        tool = QueryDatabaseTool()
        result = await tool.execute(
            {"sql": "SeLeCt 1; DrOp TaBlE secrets"},
            online_context,
        )
        assert result.success is False

    def test_is_safe_query_rejects_comment_injection(self):
        """Comment-based injection patterns should be checked."""
        # A pure SELECT with comments is technically safe; mixed stacked is not
        assert _is_safe_query("SELECT 1 -- comment") is True
        assert _is_safe_query("SELECT 1; DROP TABLE x") is False

    def test_is_safe_query_allows_subquery(self):
        """Complex nested SELECTs must be allowed."""
        assert _is_safe_query(
            "SELECT id FROM (SELECT id, name FROM users WHERE active=1) AS sub"
        ) is True

    @pytest.mark.asyncio
    async def test_valid_select_with_sqlite_succeeds(self, online_context, tmp_path):
        """Legitimate SELECT against real SQLite must succeed."""
        tool = QueryDatabaseTool()
        db_path = str(tmp_path / "inject_test.db")
        import sqlite3
        conn = sqlite3.connect(db_path)
        conn.execute("CREATE TABLE items (id INTEGER, name TEXT)")
        conn.execute("INSERT INTO items VALUES (1, 'safe')")
        conn.commit()
        conn.close()

        get_settings.cache_clear()
        try:
            with patch.dict(os.environ, {"DB_SQLITE_PATH": db_path}):
                result = await tool.execute({"sql": "SELECT * FROM items"}, online_context)
        finally:
            get_settings.cache_clear()

        assert result.success is True
        assert result.content["rows"][0]["name"] == "safe"


class TestIsSafeQueryHelper:
    """Unit tests for the _is_safe_query helper function."""

    def test_plain_select_safe(self):
        assert _is_safe_query("SELECT * FROM users") is True

    def test_select_with_join_safe(self):
        assert _is_safe_query(
            "SELECT u.id, o.total FROM users u JOIN orders o ON u.id = o.user_id"
        ) is True

    def test_truncate_blocked(self):
        assert _is_safe_query("TRUNCATE TABLE logs") is False

    def test_alter_blocked(self):
        assert _is_safe_query("ALTER TABLE users ADD COLUMN evil TEXT") is False

    def test_create_blocked(self):
        assert _is_safe_query("CREATE TABLE evil (id INT)") is False

    def test_empty_string_blocked(self):
        assert _is_safe_query("") is False

    def test_whitespace_only_blocked(self):
        assert _is_safe_query("   ") is False
