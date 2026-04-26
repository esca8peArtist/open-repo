"""
MCP tool tests: filesystem tools — allowed paths, traversal rejection, file read.
"""
from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.tools.filesystem import ReadFileTool, SearchFilesTool


class TestReadFileToolPaths:
    @pytest.mark.asyncio
    async def test_read_file_in_allowed_path(self, online_context, tmp_path):
        """File in allowed path must be readable."""
        tool = ReadFileTool()
        test_file = tmp_path / "notes.txt"
        test_file.write_text("important notes here")

        get_settings.cache_clear()
        try:
            with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
                result = await tool.execute({"path": str(test_file)}, online_context)
        finally:
            get_settings.cache_clear()

        assert result.success is True
        assert "important notes" in result.content["content"]

    @pytest.mark.asyncio
    async def test_read_file_etc_passwd_denied(self, online_context):
        """Reading /etc/passwd must always be denied."""
        tool = ReadFileTool()
        result = await tool.execute({"path": "/etc/passwd"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_path_traversal_from_allowed_base(self, online_context, tmp_path):
        """../../ traversal from allowed base must be blocked."""
        tool = ReadFileTool()
        evil = str(tmp_path / ".." / ".." / "etc" / "passwd")
        get_settings.cache_clear()
        try:
            with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
                result = await tool.execute({"path": evil}, online_context)
        finally:
            get_settings.cache_clear()
        assert result.success is False

    @pytest.mark.asyncio
    async def test_read_nonexistent_file_returns_not_found(self, online_context, tmp_path):
        """Non-existent file in allowed path must return success=False."""
        tool = ReadFileTool()
        get_settings.cache_clear()
        try:
            with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
                result = await tool.execute({"path": str(tmp_path / "ghost.txt")}, online_context)
        finally:
            get_settings.cache_clear()
        assert result.success is False
        assert "not found" in result.error.lower()

    @pytest.mark.asyncio
    async def test_read_file_outside_default_allowed_path(self, online_context):
        """/proc/self/cmdline outside any allowed path must be denied."""
        tool = ReadFileTool()
        result = await tool.execute({"path": "/proc/self/cmdline"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_read_large_file_in_allowed_path(self, online_context, tmp_path):
        """Large file in allowed path must be readable (no size limit crash)."""
        tool = ReadFileTool()
        large_file = tmp_path / "big.txt"
        large_file.write_text("A" * 50000)

        get_settings.cache_clear()
        try:
            with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
                result = await tool.execute({"path": str(large_file)}, online_context)
        finally:
            get_settings.cache_clear()

        assert result.success is True
        assert len(result.content["content"]) > 0


class TestSearchFilesTool:
    @pytest.mark.asyncio
    async def test_search_in_allowed_path(self, online_context, tmp_path):
        """Search in allowed directory returns matching files."""
        tool = SearchFilesTool()
        (tmp_path / "foo.py").write_text("x = 1")
        (tmp_path / "bar.txt").write_text("hello")

        get_settings.cache_clear()
        try:
            with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
                result = await tool.execute({"directory": str(tmp_path), "pattern": "*.py"}, online_context)
        finally:
            get_settings.cache_clear()

        assert result.success is True
        files = result.content.get("matches", [])
        assert any("foo.py" in f for f in files)

    @pytest.mark.asyncio
    async def test_search_outside_allowed_path_blocked(self, online_context):
        """Search in /etc must be blocked."""
        tool = SearchFilesTool()
        result = await tool.execute({"directory": "/etc", "pattern": "*.conf"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_search_no_matches_returns_empty_list(self, online_context, tmp_path):
        """Search with pattern matching nothing returns empty list."""
        tool = SearchFilesTool()
        get_settings.cache_clear()
        try:
            with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
                result = await tool.execute({"directory": str(tmp_path), "pattern": "*.nonexistent_ext"}, online_context)
        finally:
            get_settings.cache_clear()
        assert result.success is True
        assert result.content.get("matches", []) == []
