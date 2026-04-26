"""
GitHub MCP tools — GitHub REST API v3 via httpx.

Tools
-----
search_code         — search code across GitHub repositories
get_file            — retrieve file contents from a repository
create_issue        — open a new issue in a repository
list_pull_requests  — list pull requests for a repository

All tools require internet access and a valid GITHUB_TOKEN.

Config (env vars)
-----------------
GITHUB_TOKEN — Personal access token or fine-grained token with repo scope.

Profiles: developer_assistant (4)
requires_internet: True
"""
from __future__ import annotations

import logging
from typing import Any

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

logger = logging.getLogger(__name__)

_PROFILES = ["developer_assistant"]
_API_BASE = "https://api.github.com"
_TIMEOUT = 20.0


def _headers() -> dict[str, str]:
    token = get_settings().github_token
    h = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


async def _gh_get(path: str, params: dict | None = None) -> tuple[int, Any]:
    import httpx  # noqa: PLC0415  — deferred import (httpx declared in project deps)
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(f"{_API_BASE}{path}", headers=_headers(), params=params)
    return resp.status_code, resp.json()


async def _gh_post(path: str, body: dict) -> tuple[int, Any]:
    import httpx  # noqa: PLC0415
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.post(f"{_API_BASE}{path}", headers=_headers(), json=body)
    return resp.status_code, resp.json()


def _check_online(context: MCPContext) -> MCPToolResult | None:
    if not context.is_online:
        return MCPToolResult(
            success=False,
            content=None,
            error="GitHub tools require an internet connection.",
        )
    return None


def _check_token() -> MCPToolResult | None:
    if not get_settings().github_token:
        return MCPToolResult(
            success=False,
            content=None,
            error="GITHUB_TOKEN environment variable is not set.",
        )
    return None


# ---------------------------------------------------------------------------
# Tool 1: search_code
# ---------------------------------------------------------------------------


class SearchCodeTool(MCPTool):
    """Search GitHub code with the GitHub code search API."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="search_code",
            description=(
                "Search code on GitHub using the code search API. "
                "Optionally restrict to a specific repository (owner/repo). "
                "Returns matching files with path, repository, and URL."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query string (GitHub code search syntax supported).",
                    },
                    "repo": {
                        "type": "string",
                        "description": "Optional repository in 'owner/repo' format to scope the search.",
                    },
                },
                "required": ["query"],
            },
            requires_internet=True,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        if err := _check_online(context):
            return err
        if err := _check_token():
            return err

        query: str = arguments["query"]
        repo: str | None = arguments.get("repo")

        q = f"{query} repo:{repo}" if repo else query

        try:
            status, data = await _gh_get("/search/code", params={"q": q, "per_page": 10})
            if status != 200:
                return MCPToolResult(
                    success=False,
                    content=None,
                    error=f"GitHub API error {status}: {data.get('message', 'unknown')}",
                )

            items = [
                {
                    "name": item["name"],
                    "path": item["path"],
                    "repository": item["repository"]["full_name"],
                    "url": item["html_url"],
                    "sha": item["sha"],
                }
                for item in data.get("items", [])
            ]
            return MCPToolResult(
                success=True,
                content={"results": items, "total_count": data.get("total_count", 0)},
            )
        except Exception as exc:
            logger.error("search_code error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


# ---------------------------------------------------------------------------
# Tool 2: get_file
# ---------------------------------------------------------------------------


class GetFileTool(MCPTool):
    """Retrieve the contents of a file from a GitHub repository."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="get_file",
            description=(
                "Get the contents of a file from a GitHub repository. "
                "Returns the decoded file content as a string."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "repo": {
                        "type": "string",
                        "description": "Repository in 'owner/repo' format.",
                    },
                    "path": {
                        "type": "string",
                        "description": "File path within the repository (e.g. 'src/main.py').",
                    },
                    "ref": {
                        "type": "string",
                        "description": "Branch, tag, or commit SHA (default: repository default branch).",
                    },
                },
                "required": ["repo", "path"],
            },
            requires_internet=True,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        if err := _check_online(context):
            return err
        if err := _check_token():
            return err

        repo: str = arguments["repo"]
        path: str = arguments["path"]
        ref: str | None = arguments.get("ref")

        params = {"ref": ref} if ref else None

        try:
            status, data = await _gh_get(f"/repos/{repo}/contents/{path}", params=params)
            if status == 404:
                return MCPToolResult(
                    success=False, content=None, error=f"File '{path}' not found in {repo}."
                )
            if status != 200:
                return MCPToolResult(
                    success=False,
                    content=None,
                    error=f"GitHub API error {status}: {data.get('message', 'unknown')}",
                )

            import base64

            raw = data.get("content", "")
            encoding = data.get("encoding", "base64")
            if encoding == "base64":
                content = base64.b64decode(raw.replace("\n", "")).decode("utf-8", errors="replace")
            else:
                content = raw

            return MCPToolResult(
                success=True,
                content={
                    "path": data.get("path"),
                    "name": data.get("name"),
                    "size": data.get("size"),
                    "sha": data.get("sha"),
                    "content": content,
                    "html_url": data.get("html_url"),
                },
            )
        except Exception as exc:
            logger.error("get_file error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


# ---------------------------------------------------------------------------
# Tool 3: create_issue
# ---------------------------------------------------------------------------


class CreateIssueTool(MCPTool):
    """Open a new GitHub issue in a repository."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="create_issue",
            description="Create a new issue in a GitHub repository.",
            input_schema={
                "type": "object",
                "properties": {
                    "repo": {
                        "type": "string",
                        "description": "Repository in 'owner/repo' format.",
                    },
                    "title": {"type": "string", "description": "Issue title."},
                    "body": {"type": "string", "description": "Issue body (Markdown supported)."},
                    "labels": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional list of label names to apply.",
                    },
                },
                "required": ["repo", "title", "body"],
            },
            requires_internet=True,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        if err := _check_online(context):
            return err
        if err := _check_token():
            return err

        repo: str = arguments["repo"]
        title: str = arguments["title"]
        body: str = arguments["body"]
        labels: list[str] = arguments.get("labels", [])

        payload: dict = {"title": title, "body": body}
        if labels:
            payload["labels"] = labels

        try:
            status, data = await _gh_post(f"/repos/{repo}/issues", payload)
            if status not in (200, 201):
                return MCPToolResult(
                    success=False,
                    content=None,
                    error=f"GitHub API error {status}: {data.get('message', 'unknown')}",
                )
            return MCPToolResult(
                success=True,
                content={
                    "number": data.get("number"),
                    "title": data.get("title"),
                    "url": data.get("html_url"),
                    "state": data.get("state"),
                },
            )
        except Exception as exc:
            logger.error("create_issue error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


# ---------------------------------------------------------------------------
# Tool 4: list_pull_requests
# ---------------------------------------------------------------------------


class ListPullRequestsTool(MCPTool):
    """List pull requests for a GitHub repository."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="list_pull_requests",
            description="List pull requests for a GitHub repository.",
            input_schema={
                "type": "object",
                "properties": {
                    "repo": {
                        "type": "string",
                        "description": "Repository in 'owner/repo' format.",
                    },
                    "state": {
                        "type": "string",
                        "enum": ["open", "closed", "all"],
                        "description": "Filter by PR state (default: 'open').",
                        "default": "open",
                    },
                },
                "required": ["repo"],
            },
            requires_internet=True,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        if err := _check_online(context):
            return err
        if err := _check_token():
            return err

        repo: str = arguments["repo"]
        state: str = arguments.get("state", "open")

        try:
            status, data = await _gh_get(
                f"/repos/{repo}/pulls",
                params={"state": state, "per_page": 30, "sort": "updated"},
            )
            if status != 200:
                return MCPToolResult(
                    success=False,
                    content=None,
                    error=f"GitHub API error {status}: {data.get('message', 'unknown')}",
                )

            prs = [
                {
                    "number": pr.get("number"),
                    "title": pr.get("title"),
                    "state": pr.get("state"),
                    "author": pr.get("user", {}).get("login"),
                    "url": pr.get("html_url"),
                    "created_at": pr.get("created_at"),
                    "updated_at": pr.get("updated_at"),
                    "draft": pr.get("draft", False),
                }
                for pr in data
            ]
            return MCPToolResult(
                success=True, content={"pull_requests": prs, "count": len(prs)}
            )
        except Exception as exc:
            logger.error("list_pull_requests error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))
