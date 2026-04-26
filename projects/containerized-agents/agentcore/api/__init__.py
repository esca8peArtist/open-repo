"""AgentCore REST API — FastAPI routers for agents, chat, health, and admin."""

from agentcore.api.agents import router as agents_router
from agentcore.api.admin import router as admin_router
from agentcore.api.chat import router as chat_router
from agentcore.api.health import router as health_router

__all__ = ["agents_router", "admin_router", "chat_router", "health_router"]
