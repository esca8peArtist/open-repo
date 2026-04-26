"""
MCP (Model Context Protocol) implementation.

All tools follow this protocol for standardized invocation and result handling.
Tools declare their schema via MCPToolSchema; the registry invokes them via
execute(arguments, context) -> MCPToolResult.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel


# ---------------------------------------------------------------------------
# Core MCP types
# ---------------------------------------------------------------------------


class MCPToolSchema(BaseModel):
    """Declarative description of a single MCP tool."""

    name: str
    description: str
    input_schema: dict  # JSON Schema for input parameters
    requires_internet: bool = False
    profiles: list[str] = []  # which profiles can use this tool; empty = all


class MCPToolResult(BaseModel):
    """Standardised result returned from any MCP tool invocation."""

    success: bool
    content: Any  # The actual result payload
    error: str | None = None
    cached: bool = False
    duration_ms: int = 0


class MCPContext(BaseModel):
    """Runtime context passed to every tool invocation."""

    agent_id: str
    session_id: str
    hardware_tier: int = 1
    is_online: bool = True


# ---------------------------------------------------------------------------
# Abstract base class for all MCP tools
# ---------------------------------------------------------------------------


class MCPTool(ABC):
    """
    Abstract base class for every MCP tool implementation.

    Subclasses must implement:
        schema  — property returning MCPToolSchema
        execute — async method performing the actual work
    """

    @property
    @abstractmethod
    def schema(self) -> MCPToolSchema:
        """Return the tool's schema (name, description, input_schema, flags)."""
        ...

    @abstractmethod
    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        """
        Execute the tool.

        Args:
            arguments: Validated input arguments (keys match input_schema properties).
            context:   Runtime context (agent_id, session_id, is_online, …).

        Returns:
            MCPToolResult — always returned, never raised.
        """
        ...
