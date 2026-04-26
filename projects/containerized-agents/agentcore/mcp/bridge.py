"""
Bridges MCP tools into OpenAI Agents SDK function_tools format.

The SDK expects tools as Python functions with type annotations decorated
with @function_tool.  This bridge dynamically creates those wrapper functions
from MCPToolSchema definitions so that any MCP tool can be passed directly to
SDKAgent(tools=[...]).

Usage example
-------------
from agentcore.mcp.registry import MCPToolRegistry
from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.bridge import build_sdk_tools

registry = MCPToolRegistry()
registry.register_all_tools()

context = MCPContext(agent_id="abc", session_id="xyz", is_online=True)
sdk_tools = build_sdk_tools(registry, profile="personal_productivity", context=context)

# Pass to OpenAI Agents SDK agent:
# agent = Agent(tools=sdk_tools, ...)
"""
from __future__ import annotations

import asyncio
import functools
import json
import logging
from typing import Any

from agentcore.mcp.protocol import MCPContext, MCPToolSchema
from agentcore.mcp.registry import MCPToolRegistry

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def build_sdk_tools(
    registry: MCPToolRegistry,
    profile: str,
    context: MCPContext,
) -> list[Any]:
    """
    Build a list of openai-agents function_tool objects for a given profile.

    Each MCP tool whose profile list includes *profile* (or is empty / all)
    becomes an SDK-compatible function_tool.  Returns a list ready to pass to
    ``Agent(tools=[...])``.

    If the ``agents`` package is not installed the function returns a list of
    plain async callables that behave identically (useful for testing without
    the full SDK dependency).
    """
    tools = registry.get_tools_for_profile(profile)
    sdk_tools = [mcp_tool_to_function(t.schema, registry, context) for t in tools]
    logger.debug(
        "Built %d SDK tools for profile '%s'",
        len(sdk_tools),
        profile,
    )
    return sdk_tools


def mcp_tool_to_function(
    tool_schema: MCPToolSchema,
    registry: MCPToolRegistry,
    context: MCPContext,
) -> Any:
    """
    Convert a single MCPToolSchema into an openai-agents function_tool.

    The generated function:
    - Accepts **kwargs corresponding to the tool's input_schema properties.
    - Delegates execution to registry.invoke().
    - Returns a JSON string (the SDK expects str from function tools).
    - Handles errors gracefully — never raises; returns an error JSON string.

    If the ``agents`` SDK is available the function is decorated with
    ``@function_tool``; otherwise it is returned as a plain async callable
    so that the rest of the system can still test tool execution.
    """
    tool_name = tool_schema.name
    tool_description = tool_schema.description

    # Build the async implementation
    async def _tool_impl(**kwargs: Any) -> str:
        try:
            result = await registry.invoke(
                tool_name=tool_name,
                arguments=dict(kwargs),
                context=context,
            )
            return json.dumps(
                {
                    "success": result.success,
                    "content": result.content,
                    "error": result.error,
                    "duration_ms": result.duration_ms,
                },
                default=str,
            )
        except Exception as exc:
            logger.exception("Unexpected error in SDK wrapper for tool '%s': %s", tool_name, exc)
            return json.dumps({"success": False, "content": None, "error": str(exc)})

    # Name the function after the tool so the SDK can reflect on it
    _tool_impl.__name__ = tool_name
    _tool_impl.__doc__ = tool_description

    # Attempt to wrap with the openai-agents SDK decorator
    try:
        from agents import function_tool  # type: ignore[import]

        wrapped = function_tool(_tool_impl)
        return wrapped
    except ImportError:
        # SDK not installed — return the raw async callable.
        # The ToolDispatcher bridge will still work; only the SDK integration
        # path is unavailable.
        logger.debug(
            "openai-agents SDK not available — tool '%s' returned as plain coroutine.",
            tool_name,
        )
        return _tool_impl


# ---------------------------------------------------------------------------
# Async helper for non-SDK invocation (used by ToolDispatcher bridge)
# ---------------------------------------------------------------------------


async def invoke_mcp_tool(
    registry: MCPToolRegistry,
    tool_name: str,
    arguments: dict,
    context: MCPContext,
) -> dict:
    """
    Invoke an MCP tool and return a plain dict compatible with the
    existing ToolDispatcher result format  {output: ..., error: ...}.

    This is the glue used by ToolDispatcher.dispatch() when it delegates to
    the MCPToolRegistry.
    """
    result = await registry.invoke(tool_name, arguments, context)
    if result.success:
        return {"output": result.content}
    return {
        "error": result.error or "unknown error",
        "output": result.error or f"Tool '{tool_name}' failed.",
    }
