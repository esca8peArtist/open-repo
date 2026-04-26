"""
Central registry of all MCP tools.

Tools register themselves; the registry makes them available to agents by
profile.  The registry also owns connectivity checks, input validation,
timeout enforcement, and graceful-degradation logic.
"""
from __future__ import annotations

import asyncio
import importlib
import json
import logging
import time
from typing import TYPE_CHECKING

import jsonschema

from agentcore.metrics import TOOL_CALLS
from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)

# Default per-tool timeout in seconds
_DEFAULT_TOOL_TIMEOUT = 30


class MCPToolRegistry:
    """
    Central registry that holds every MCPTool available on this node.

    Lifecycle
    ---------
    1. Create an instance.
    2. Call register_all_tools() once at startup.
    3. Use get_tools_for_profile() to build an agent's tool list.
    4. Use invoke() to execute a tool call coming from the LLM.
    """

    def __init__(self) -> None:
        self._tools: dict[str, MCPTool] = {}

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register(self, tool: MCPTool) -> None:
        """Register a tool instance under its schema name."""
        name = tool.schema.name
        if name in self._tools:
            logger.warning("MCP tool '%s' already registered — overwriting.", name)
        self._tools[name] = tool
        logger.debug("MCP tool registered: %s", name)

    def register_all_tools(self) -> None:
        """
        Register all built-in MCP tools.

        Called once at AgentCore startup (from server.py lifespan).
        Each tool module is imported here; import errors are caught and logged
        so that a missing optional dependency doesn't prevent startup.
        """
        tool_modules = [
            ("agentcore.mcp.tools.calendar", ["GetCalendarEventsTool", "CreateCalendarEventTool"]),
            ("agentcore.mcp.tools.email", ["SendEmailTool", "ReadEmailsTool"]),
            ("agentcore.mcp.tools.web_search", ["WebSearchTool"]),
            ("agentcore.mcp.tools.database", ["QueryDatabaseTool"]),
            ("agentcore.mcp.tools.code_exec", ["ExecutePythonTool"]),
            ("agentcore.mcp.tools.crm", ["SearchContactsTool", "GetContactTool", "AddNoteTool", "UpdateContactStatusTool"]),
            ("agentcore.mcp.tools.scheduler", ["ScheduleTaskTool", "ListScheduledTasksTool", "CancelTaskTool"]),
            ("agentcore.mcp.tools.github", ["SearchCodeTool", "GetFileTool", "CreateIssueTool", "ListPullRequestsTool"]),
            ("agentcore.mcp.tools.filesystem", ["ReadFileTool", "ListDirectoryTool", "SearchFilesTool"]),
            ("agentcore.mcp.tools.report", ["GeneratePdfReportTool"]),
        ]

        registered = 0
        for module_path, class_names in tool_modules:
            try:
                mod = importlib.import_module(module_path)
                for class_name in class_names:
                    cls = getattr(mod, class_name)
                    self.register(cls())
                    registered += 1
            except ImportError as exc:
                logger.warning(
                    "MCP tool module '%s' could not be imported (missing dependency?): %s",
                    module_path,
                    exc,
                )
            except Exception as exc:
                logger.error("Failed to register tools from '%s': %s", module_path, exc)

        logger.info("MCPToolRegistry: %d tools registered.", registered)

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------

    def get_tool(self, name: str) -> MCPTool | None:
        """Return a registered tool by name, or None if not found."""
        return self._tools.get(name)

    def get_tools_for_profile(self, profile: str) -> list[MCPTool]:
        """
        Return all tools available for a given agent profile.

        A tool is included if its schema.profiles list is empty (meaning it
        is available to all profiles) OR if the given profile name appears in
        its profiles list.
        """
        result: list[MCPTool] = []
        for tool in self._tools.values():
            allowed = tool.schema.profiles
            if not allowed or profile in allowed:
                result.append(tool)
        return result

    def list_tool_names(self) -> list[str]:
        """Return sorted list of all registered tool names."""
        return sorted(self._tools.keys())

    # ------------------------------------------------------------------
    # Invocation
    # ------------------------------------------------------------------

    async def invoke(
        self,
        tool_name: str,
        arguments: dict,
        context: MCPContext,
        timeout: float = _DEFAULT_TOOL_TIMEOUT,
    ) -> MCPToolResult:
        """
        Invoke a named tool.

        Handles:
        - Unknown tool lookup (graceful error)
        - Online/offline check for internet-dependent tools
        - Input validation against the tool's JSON Schema
        - Timeout enforcement (default 30 s per tool)
        - Error capture and graceful degradation
        """
        tool = self._tools.get(tool_name)
        if tool is None:
            TOOL_CALLS.labels(tool_name=tool_name, status="error").inc()
            return MCPToolResult(
                success=False,
                content=None,
                error=f"Unknown MCP tool: '{tool_name}'",
            )

        schema = tool.schema

        # -- Offline check -----------------------------------------------
        if schema.requires_internet and not context.is_online:
            logger.warning("Tool '%s' requires internet but context.is_online=False.", tool_name)
            TOOL_CALLS.labels(tool_name=tool_name, status="error").inc()
            return MCPToolResult(
                success=False,
                content=None,
                error=f"Tool '{tool_name}' requires an internet connection, which is not currently available.",
            )

        # -- Input validation --------------------------------------------
        validation_error = _validate_arguments(arguments, schema.input_schema)
        if validation_error:
            TOOL_CALLS.labels(tool_name=tool_name, status="error").inc()
            return MCPToolResult(
                success=False,
                content=None,
                error=f"Invalid arguments for tool '{tool_name}': {validation_error}",
            )

        # -- Execute with timeout ----------------------------------------
        start = time.monotonic()
        try:
            result = await asyncio.wait_for(
                tool.execute(arguments, context),
                timeout=timeout,
            )
        except asyncio.TimeoutError:
            elapsed_ms = int((time.monotonic() - start) * 1000)
            logger.error("Tool '%s' timed out after %d ms.", tool_name, elapsed_ms)
            TOOL_CALLS.labels(tool_name=tool_name, status="error").inc()
            return MCPToolResult(
                success=False,
                content=None,
                error=f"Tool '{tool_name}' timed out after {timeout:.0f}s.",
                duration_ms=elapsed_ms,
            )
        except Exception as exc:
            elapsed_ms = int((time.monotonic() - start) * 1000)
            logger.exception("Tool '%s' raised an exception: %s", tool_name, exc)
            TOOL_CALLS.labels(tool_name=tool_name, status="error").inc()
            return MCPToolResult(
                success=False,
                content=None,
                error=f"Tool '{tool_name}' encountered an error: {exc}",
                duration_ms=elapsed_ms,
            )

        result.duration_ms = int((time.monotonic() - start) * 1000)
        TOOL_CALLS.labels(tool_name=tool_name, status="success").inc()
        return result


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _validate_arguments(arguments: dict, input_schema: dict) -> str | None:
    """
    Validate *arguments* against *input_schema* (JSON Schema).

    Returns None if valid, or an error message string if invalid.
    """
    if not input_schema:
        return None
    try:
        jsonschema.validate(instance=arguments, schema=input_schema)
        return None
    except jsonschema.ValidationError as exc:
        return exc.message
    except Exception as exc:
        # jsonschema itself failing — treat as valid so execution can proceed
        logger.warning("JSON Schema validation error: %s", exc)
        return None
