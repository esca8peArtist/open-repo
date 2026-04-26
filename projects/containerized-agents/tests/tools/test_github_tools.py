"""
MCP tool tests: GitHub tools — mock GitHub API responses, test all 4 operations.
"""
from __future__ import annotations

import base64
import json
import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.tools.github import (
    CreateIssueTool,
    GetFileTool,
    ListPullRequestsTool,
    SearchCodeTool,
)


@pytest.fixture
def github_env():
    """Patch GITHUB_TOKEN for tests and clear the lru_cache so Settings reloads."""
    get_settings.cache_clear()
    with patch.dict(os.environ, {"GITHUB_TOKEN": "test-token-abc123"}):
        yield
    get_settings.cache_clear()


class TestSearchCodeTool:
    @pytest.mark.asyncio
    async def test_search_offline_returns_error(self, offline_context):
        """SearchCodeTool must return error when offline."""
        tool = SearchCodeTool()
        result = await tool.execute({"query": "def main"}, offline_context)
        assert result.success is False
        assert "internet" in result.error.lower()

    @pytest.mark.asyncio
    async def test_search_no_token_returns_error(self, online_context):
        """Missing GITHUB_TOKEN must return success=False."""
        tool = SearchCodeTool()
        get_settings.cache_clear()
        # Remove only GITHUB_TOKEN; keep required vars (POSTGRES_URL, REDIS_URL,
        # API_SECRET_KEY) so get_settings() does not call sys.exit(1).
        env_without_token = {k: v for k, v in os.environ.items() if k != "GITHUB_TOKEN"}
        with patch.dict(os.environ, env_without_token, clear=True):
            result = await tool.execute({"query": "def main"}, online_context)
        get_settings.cache_clear()
        assert result.success is False
        assert "GITHUB_TOKEN" in result.error

    @pytest.mark.asyncio
    async def test_search_returns_results(self, online_context, github_env):
        """Successful search returns items with path, repository, url."""
        tool = SearchCodeTool()
        mock_response = {
            "items": [
                {
                    "name": "main.py",
                    "path": "src/main.py",
                    "repository": {"full_name": "owner/repo"},
                    "html_url": "https://github.com/owner/repo/blob/main/src/main.py",
                    "sha": "abc123",
                }
            ],
            "total_count": 1,
        }

        with patch("agentcore.mcp.tools.github._gh_get", new=AsyncMock(return_value=(200, mock_response))):
            result = await tool.execute({"query": "def main"}, online_context)

        assert result.success is True
        assert result.content["total_count"] == 1
        assert result.content["results"][0]["name"] == "main.py"

    @pytest.mark.asyncio
    async def test_search_with_repo_scope(self, online_context, github_env):
        """Search with repo parameter appends repo: to query."""
        tool = SearchCodeTool()

        with patch("agentcore.mcp.tools.github._gh_get", new=AsyncMock(return_value=(200, {"items": [], "total_count": 0}))) as mock_get:
            await tool.execute({"query": "def main", "repo": "owner/repo"}, online_context)

        call_args = mock_get.call_args
        params = call_args[1].get("params") or call_args[0][1]
        assert "owner/repo" in params.get("q", "")

    @pytest.mark.asyncio
    async def test_search_api_error_returns_failure(self, online_context, github_env):
        """GitHub API 403 must return success=False."""
        tool = SearchCodeTool()

        with patch("agentcore.mcp.tools.github._gh_get", new=AsyncMock(return_value=(403, {"message": "Forbidden"}))):
            result = await tool.execute({"query": "test"}, online_context)

        assert result.success is False
        assert "403" in result.error or "Forbidden" in result.error


class TestGetFileTool:
    @pytest.mark.asyncio
    async def test_get_file_success(self, online_context, github_env):
        """get_file returns decoded file content."""
        tool = GetFileTool()
        content = "def hello():\n    print('Hello')"
        encoded = base64.b64encode(content.encode()).decode()

        mock_data = {
            "path": "src/hello.py",
            "name": "hello.py",
            "size": len(content),
            "sha": "abc123",
            "content": encoded + "\n",
            "encoding": "base64",
            "html_url": "https://github.com/owner/repo/blob/main/src/hello.py",
        }

        with patch("agentcore.mcp.tools.github._gh_get", new=AsyncMock(return_value=(200, mock_data))):
            result = await tool.execute({"repo": "owner/repo", "path": "src/hello.py"}, online_context)

        assert result.success is True
        assert "def hello" in result.content["content"]

    @pytest.mark.asyncio
    async def test_get_file_not_found(self, online_context, github_env):
        """get_file 404 returns success=False."""
        tool = GetFileTool()

        with patch("agentcore.mcp.tools.github._gh_get", new=AsyncMock(return_value=(404, {"message": "Not Found"}))):
            result = await tool.execute({"repo": "owner/repo", "path": "missing.py"}, online_context)

        assert result.success is False
        assert "not found" in result.error.lower()

    @pytest.mark.asyncio
    async def test_get_file_offline(self, offline_context):
        """get_file must degrade offline."""
        tool = GetFileTool()
        result = await tool.execute({"repo": "a/b", "path": "f.py"}, offline_context)
        assert result.success is False


class TestCreateIssueTool:
    @pytest.mark.asyncio
    async def test_create_issue_success(self, online_context, github_env):
        """create_issue returns issue number and URL on success."""
        tool = CreateIssueTool()
        mock_data = {
            "number": 42,
            "title": "Test Issue",
            "html_url": "https://github.com/owner/repo/issues/42",
            "state": "open",
        }

        with patch("agentcore.mcp.tools.github._gh_post", new=AsyncMock(return_value=(201, mock_data))):
            result = await tool.execute(
                {"repo": "owner/repo", "title": "Test Issue", "body": "Details here"},
                online_context,
            )

        assert result.success is True
        assert result.content["number"] == 42

    @pytest.mark.asyncio
    async def test_create_issue_offline(self, offline_context):
        """create_issue must degrade offline."""
        tool = CreateIssueTool()
        result = await tool.execute({"repo": "a/b", "title": "t", "body": "b"}, offline_context)
        assert result.success is False


class TestListPullRequestsTool:
    @pytest.mark.asyncio
    async def test_list_prs_success(self, online_context, github_env):
        """list_pull_requests returns list of PR objects."""
        tool = ListPullRequestsTool()
        mock_prs = [
            {
                "number": 1,
                "title": "Fix bug",
                "state": "open",
                "user": {"login": "alice"},
                "html_url": "https://github.com/owner/repo/pull/1",
                "created_at": "2026-01-01T00:00:00Z",
                "updated_at": "2026-01-02T00:00:00Z",
                "draft": False,
            }
        ]

        with patch("agentcore.mcp.tools.github._gh_get", new=AsyncMock(return_value=(200, mock_prs))):
            result = await tool.execute({"repo": "owner/repo"}, online_context)

        assert result.success is True
        assert result.content["count"] == 1
        assert result.content["pull_requests"][0]["number"] == 1

    @pytest.mark.asyncio
    async def test_list_prs_offline(self, offline_context):
        """list_pull_requests must degrade offline."""
        tool = ListPullRequestsTool()
        result = await tool.execute({"repo": "a/b"}, offline_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_list_prs_api_error(self, online_context, github_env):
        """GitHub API error returns success=False."""
        tool = ListPullRequestsTool()

        with patch("agentcore.mcp.tools.github._gh_get", new=AsyncMock(return_value=(401, {"message": "Unauthorized"}))):
            result = await tool.execute({"repo": "owner/repo"}, online_context)

        assert result.success is False
