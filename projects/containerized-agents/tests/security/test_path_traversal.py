"""
Security tests: path traversal via the filesystem MCP tool.
Verifies that ../../etc/passwd and similar patterns are rejected.
"""
from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.tools.filesystem import ReadFileTool, SearchFilesTool


class TestPathTraversalRejection:
    """All path traversal attempts must be blocked before file I/O."""

    @pytest.mark.asyncio
    async def test_etc_passwd_rejected(self, online_context):
        """Direct path to /etc/passwd must be denied."""
        tool = ReadFileTool()
        result = await tool.execute({"path": "/etc/passwd"}, online_context)
        assert result.success is False
        assert result.error is not None

    @pytest.mark.asyncio
    async def test_etc_shadow_rejected(self, online_context):
        """Direct path to /etc/shadow must be denied."""
        tool = ReadFileTool()
        result = await tool.execute({"path": "/etc/shadow"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_dotdot_traversal_absolute(self, online_context):
        """Absolute traversal with ../ must be blocked."""
        tool = ReadFileTool()
        result = await tool.execute({"path": "/data/../../../etc/passwd"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_dotdot_traversal_deep(self, online_context):
        """Deep traversal must be blocked."""
        tool = ReadFileTool()
        result = await tool.execute(
            {"path": "/data/uploads/../../../../../etc/shadow"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_proc_self_environ_rejected(self, online_context):
        """Access to /proc/self/environ (env vars with secrets) must be denied."""
        tool = ReadFileTool()
        result = await tool.execute({"path": "/proc/self/environ"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_url_encoded_traversal_rejected(self, online_context):
        """URL-encoded traversal path must be rejected."""
        tool = ReadFileTool()
        # %2e%2e = ".." in URL encoding
        result = await tool.execute({"path": "/data/%2e%2e%2f%2e%2e%2fetc/passwd"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_null_byte_path_rejected(self, online_context):
        """Null byte injection in path must be rejected."""
        tool = ReadFileTool()
        result = await tool.execute({"path": "/data/file.txt\x00.evil"}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_allowed_path_reads_file(self, online_context, tmp_path):
        """A legitimate file in the allowed path must be readable."""
        tool = ReadFileTool()
        test_file = tmp_path / "allowed.txt"
        test_file.write_text("allowed content")

        get_settings.cache_clear()
        try:
            with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
                result = await tool.execute({"path": str(test_file)}, online_context)
        finally:
            get_settings.cache_clear()

        assert result.success is True
        assert "allowed content" in result.content["content"]

    @pytest.mark.asyncio
    async def test_traversal_from_allowed_base_blocked(self, online_context, tmp_path):
        """Traversal escaping from an allowed path must be blocked."""
        tool = ReadFileTool()
        # Try to escape from tmp_path
        evil_path = str(tmp_path / ".." / ".." / "etc" / "passwd")

        with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
            result = await tool.execute({"path": evil_path}, online_context)

        assert result.success is False

    @pytest.mark.asyncio
    async def test_missing_file_in_allowed_path_returns_not_found(self, online_context, tmp_path):
        """Missing file in allowed path returns a helpful error, not an exception."""
        tool = ReadFileTool()
        missing = tmp_path / "does_not_exist.txt"

        with patch.dict(os.environ, {"FILESYSTEM_ALLOWED_PATHS": str(tmp_path)}):
            result = await tool.execute({"path": str(missing)}, online_context)

        assert result.success is False
        assert result.error is not None


class TestSearchFilesPathSecurity:
    """SearchFilesTool also must not escape allowed paths."""

    @pytest.mark.asyncio
    async def test_search_outside_allowed_paths_blocked(self, online_context):
        """Searching /etc/ must be blocked."""
        tool = SearchFilesTool()
        result = await tool.execute({"directory": "/etc", "pattern": "*.conf"}, online_context)
        assert result.success is False
