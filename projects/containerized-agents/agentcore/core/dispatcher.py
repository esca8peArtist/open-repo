"""
ToolDispatcher — routes tool calls to registered handlers.

Handles graceful degradation: internet-dependent tools fail cleanly when
the device is offline (fully offline-capable by design requirement).

MCP Integration
---------------
ToolDispatcher now acts as the unified entry point for both:
  1. Legacy simple handlers registered via register() — used for built-in tools
     like get_current_time and echo that don't need the full MCP machinery.
  2. MCP tools registered in MCPToolRegistry — all profile tools (calendar,
     email, CRM, GitHub, etc.) go through the registry.

Resolution order for dispatch():
  1. Check legacy handler dict (_tools).
  2. If not found, delegate to the MCPToolRegistry if one is attached.
  3. Return a graceful "unknown tool" error if neither has it.

The MCPContext passed to MCP tools is constructed from the dispatcher's
current connectivity status plus sensible defaults.
"""
from __future__ import annotations

import asyncio
import logging
import time
from collections.abc import Callable, Coroutine
from typing import TYPE_CHECKING, Any

import httpx

if TYPE_CHECKING:
    from agentcore.mcp.registry import MCPToolRegistry

logger = logging.getLogger(__name__)

# Type alias for a tool handler coroutine
ToolHandler = Callable[..., Coroutine[Any, Any, dict[str, Any]]]


class ToolDispatcher:
    """
    Central registry and dispatcher for all agent tools.

    Tools register themselves at startup (or dynamically).  When the model
    emits a function-call, the dispatcher looks up the handler, checks
    connectivity requirements, and calls the handler.

    Connectivity checks are cached for `_connectivity_cache_ttl` seconds to
    avoid hammering the network on every tool call in offline scenarios.

    MCP registry integration
    ------------------------
    Call set_mcp_registry(registry) after construction to enable MCP tool
    delegation.  MCP tools are tried as a fallback when a tool name is not
    found in the legacy handler dict.
    """

    def __init__(self, connectivity_check_url: str = "https://1.1.1.1", cache_ttl: int = 30) -> None:
        self._tools: dict[str, ToolHandler] = {}
        self._online_tools: set[str] = set()
        self._connectivity_check_url = connectivity_check_url
        self._connectivity_cache_ttl = cache_ttl

        # Connectivity cache
        self._online_status: bool | None = None
        self._online_checked_at: float = 0.0

        # Lock to prevent concurrent connectivity checks
        self._connectivity_lock = asyncio.Lock()

        # MCP registry (optional — set via set_mcp_registry)
        self._mcp_registry: MCPToolRegistry | None = None

        # Agent context hints — used to build MCPContext for MCP tool calls
        self._agent_id: str = "unknown"
        self._session_id: str = "unknown"
        self._hardware_tier: int = 1

    # ------------------------------------------------------------------
    # MCP registry integration
    # ------------------------------------------------------------------

    def set_mcp_registry(self, registry: MCPToolRegistry) -> None:
        """
        Attach an MCPToolRegistry.

        Once set, any tool name not found in the legacy handler dict will be
        looked up in the registry and dispatched via registry.invoke().
        """
        self._mcp_registry = registry
        logger.info(
            "MCPToolRegistry attached to ToolDispatcher (%d MCP tools available).",
            len(registry.list_tool_names()),
        )

    def set_agent_context(
        self, agent_id: str, session_id: str, hardware_tier: int = 1
    ) -> None:
        """Update the context hints used when building MCPContext for MCP calls."""
        self._agent_id = agent_id
        self._session_id = session_id
        self._hardware_tier = hardware_tier

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register(
        self,
        name: str,
        handler: ToolHandler,
        requires_internet: bool = False,
    ) -> None:
        """
        Register a tool handler.

        Args:
            name: Tool name (must match the name used in the LLM function schema).
            handler: Async callable.  Receives **kwargs matching the tool arguments.
            requires_internet: If True, the tool will return a graceful error when offline.
        """
        self._tools[name] = handler
        if requires_internet:
            self._online_tools.add(name)
        logger.debug("Registered tool: %s (requires_internet=%s)", name, requires_internet)

    def unregister(self, name: str) -> None:
        """Remove a tool from the dispatcher."""
        self._tools.pop(name, None)
        self._online_tools.discard(name)

    def list_tools(self) -> list[str]:
        """Return names of all registered tools (legacy + MCP combined)."""
        names = list(self._tools.keys())
        if self._mcp_registry:
            for name in self._mcp_registry.list_tool_names():
                if name not in names:
                    names.append(name)
        return names

    # ------------------------------------------------------------------
    # Dispatch
    # ------------------------------------------------------------------

    async def dispatch(self, tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        """
        Dispatch a tool call.

        Resolution order:
        1. Legacy handler dict (built-in tools registered via register()).
        2. MCPToolRegistry (all profile tools) — if registry is attached.

        Returns a dict with at minimum an `output` key.
        On error, returns a dict with an `error` key — never raises.
        """
        # ----------------------------------------------------------
        # 1. Legacy handler path
        # ----------------------------------------------------------
        if tool_name in self._tools:
            # Check connectivity requirement for legacy tools
            if tool_name in self._online_tools:
                online = await self.is_online()
                if not online:
                    logger.warning("Tool '%s' requires internet but device is offline.", tool_name)
                    return {
                        "error": "offline",
                        "output": (
                            f"The '{tool_name}' tool requires internet connectivity, "
                            "which is not currently available. "
                            "Please try again when the device is online."
                        ),
                    }

            handler = self._tools[tool_name]
            try:
                result = await handler(**arguments)
                if not isinstance(result, dict):
                    result = {"output": str(result)}
                return result
            except TypeError as exc:
                logger.error("Tool '%s' argument error: %s", tool_name, exc)
                return {"error": str(exc), "output": f"Invalid arguments for tool '{tool_name}'."}
            except Exception as exc:
                logger.exception("Tool '%s' raised an exception: %s", tool_name, exc)
                return {
                    "error": type(exc).__name__,
                    "output": f"Tool '{tool_name}' encountered an error: {exc}",
                }

        # ----------------------------------------------------------
        # 2. MCP registry path
        # ----------------------------------------------------------
        if self._mcp_registry is not None:
            mcp_tool = self._mcp_registry.get_tool(tool_name)
            if mcp_tool is not None:
                return await self._dispatch_mcp(tool_name, arguments)

        # ----------------------------------------------------------
        # 3. Unknown tool
        # ----------------------------------------------------------
        return {
            "error": f"Unknown tool '{tool_name}'",
            "output": f"Tool '{tool_name}' is not available.",
        }

    async def _dispatch_mcp(
        self, tool_name: str, arguments: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Delegate a tool call to the MCPToolRegistry.

        Builds an MCPContext from the current dispatcher state (connectivity
        status, agent_id, session_id, hardware_tier) and calls registry.invoke().
        Converts the MCPToolResult to the legacy {output, error} dict format.
        """
        from agentcore.mcp.bridge import invoke_mcp_tool
        from agentcore.mcp.protocol import MCPContext

        online = await self.is_online()
        context = MCPContext(
            agent_id=self._agent_id,
            session_id=self._session_id,
            hardware_tier=self._hardware_tier,
            is_online=online,
        )

        try:
            return await invoke_mcp_tool(
                registry=self._mcp_registry,  # type: ignore[arg-type]
                tool_name=tool_name,
                arguments=arguments,
                context=context,
            )
        except Exception as exc:
            logger.exception("MCP dispatch error for tool '%s': %s", tool_name, exc)
            return {
                "error": type(exc).__name__,
                "output": f"MCP tool '{tool_name}' encountered an error: {exc}",
            }

    # ------------------------------------------------------------------
    # Connectivity
    # ------------------------------------------------------------------

    async def is_online(self) -> bool:
        """
        Return True if the device has internet access.

        The result is cached for `_connectivity_cache_ttl` seconds to avoid
        repeated network calls during a burst of tool invocations.
        """
        now = time.monotonic()
        if self._online_status is not None and (now - self._online_checked_at) < self._connectivity_cache_ttl:
            return self._online_status

        async with self._connectivity_lock:
            # Double-check after acquiring lock (another coroutine may have updated)
            now = time.monotonic()
            if self._online_status is not None and (now - self._online_checked_at) < self._connectivity_cache_ttl:
                return self._online_status

            try:
                async with httpx.AsyncClient(timeout=3.0) as client:
                    response = await client.head(self._connectivity_check_url)
                    self._online_status = response.status_code < 600
            except Exception:
                self._online_status = False

            self._online_checked_at = time.monotonic()
            logger.debug("Connectivity check: online=%s", self._online_status)
            return self._online_status  # type: ignore[return-value]

    def invalidate_connectivity_cache(self) -> None:
        """Force the next call to is_online() to perform a fresh check."""
        self._online_status = None
        self._online_checked_at = 0.0


# ---------------------------------------------------------------------------
# Built-in tool handlers (registered at server startup)
# ---------------------------------------------------------------------------


async def tool_get_current_time(**kwargs: Any) -> dict[str, Any]:
    """Return the current UTC time — no internet required."""
    from datetime import datetime, timezone

    now = datetime.now(timezone.utc).isoformat()
    return {"output": now}


async def tool_echo(**kwargs: Any) -> dict[str, Any]:
    """Debug echo tool — returns its arguments. No internet required."""
    return {"output": str(kwargs)}


def register_builtin_tools(dispatcher: ToolDispatcher) -> None:
    """Register the built-in tools that ship with every AgentCore instance."""
    dispatcher.register("get_current_time", tool_get_current_time, requires_internet=False)
    dispatcher.register("echo", tool_echo, requires_internet=False)
