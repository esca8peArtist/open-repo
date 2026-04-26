"""
agentcore.mcp — Model Context Protocol implementation.

Provides standardized tool invocation across all agent profiles with:
- MCPToolSchema / MCPToolResult / MCPContext types  (protocol.py)
- Central MCPToolRegistry                            (registry.py)
- Bridge to OpenAI Agents SDK function_tools         (bridge.py)
- Concrete tool implementations                      (tools/)
"""
from agentcore.mcp.protocol import MCPContext, MCPToolResult, MCPToolSchema
from agentcore.mcp.registry import MCPToolRegistry

__all__ = [
    "MCPToolSchema",
    "MCPToolResult",
    "MCPContext",
    "MCPToolRegistry",
]
