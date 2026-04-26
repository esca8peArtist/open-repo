"""
Web search MCP tool.

Strategy
--------
1. Try Tavily API (TAVILY_API_KEY env var) — structured, high quality.
2. Fall back to DuckDuckGo via duckduckgo-search (no API key, free).
3. Offline: return graceful error.

Config (env vars)
-----------------
TAVILY_API_KEY — optional; enables Tavily as primary search engine

Profiles: personal_productivity (1)
requires_internet: True
"""
from __future__ import annotations

import logging
from typing import Any

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

logger = logging.getLogger(__name__)

_PROFILES = ["personal_productivity"]


class WebSearchTool(MCPTool):
    """Search the web using Tavily (primary) or DuckDuckGo (fallback)."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="web_search",
            description=(
                "Search the internet for current information. "
                "Returns a list of results with title, url, and snippet. "
                "Requires an active internet connection."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query string.",
                    },
                    "num_results": {
                        "type": "integer",
                        "description": "Number of results to return (default: 5, max: 20).",
                        "default": 5,
                        "minimum": 1,
                        "maximum": 20,
                    },
                },
                "required": ["query"],
            },
            requires_internet=True,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        if not context.is_online:
            return MCPToolResult(
                success=False,
                content=None,
                error="Web search requires internet connection",
            )

        query: str = arguments["query"]
        num_results: int = min(int(arguments.get("num_results", 5)), 20)

        tavily_key = get_settings().tavily_api_key
        if tavily_key:
            result = await self._search_tavily(query, num_results, tavily_key)
            if result.success:
                return result
            logger.warning("Tavily search failed (%s), falling back to DuckDuckGo.", result.error)

        return await self._search_duckduckgo(query, num_results)

    async def _search_tavily(self, query: str, num_results: int, api_key: str) -> MCPToolResult:
        try:
            import httpx

            async with httpx.AsyncClient(timeout=15.0) as client:
                response = await client.post(
                    "https://api.tavily.com/search",
                    json={
                        "api_key": api_key,
                        "query": query,
                        "max_results": num_results,
                        "search_depth": "basic",
                        "include_answer": False,
                    },
                )
                response.raise_for_status()
                data = response.json()

            results = [
                {
                    "title": r.get("title", ""),
                    "url": r.get("url", ""),
                    "snippet": r.get("content", ""),
                    "score": r.get("score", 0.0),
                }
                for r in data.get("results", [])
            ]
            return MCPToolResult(
                success=True,
                content={"results": results, "query": query, "source": "tavily"},
            )
        except Exception as exc:
            return MCPToolResult(success=False, content=None, error=f"Tavily error: {exc}")

    async def _search_duckduckgo(self, query: str, num_results: int) -> MCPToolResult:
        try:
            import asyncio

            from duckduckgo_search import DDGS  # type: ignore[import]

            loop = asyncio.get_running_loop()

            def _sync_search():
                with DDGS() as ddgs:
                    return list(ddgs.text(query, max_results=num_results))

            raw = await loop.run_in_executor(None, _sync_search)
            results = [
                {
                    "title": r.get("title", ""),
                    "url": r.get("href", ""),
                    "snippet": r.get("body", ""),
                }
                for r in raw
            ]
            return MCPToolResult(
                success=True,
                content={"results": results, "query": query, "source": "duckduckgo"},
            )
        except ImportError:
            return MCPToolResult(
                success=False,
                content=None,
                error=(
                    "Web search is unavailable: neither Tavily API key is configured "
                    "nor the duckduckgo-search library is installed. "
                    "Install with: pip install duckduckgo-search"
                ),
            )
        except Exception as exc:
            logger.error("DuckDuckGo search error: %s", exc)
            return MCPToolResult(success=False, content=None, error=f"DuckDuckGo error: {exc}")
