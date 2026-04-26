"""
Agent configuration REST endpoints.

All endpoints require the X-API-Key header to match the configured api_secret_key.

Routes (all under /api/agents):
    GET    /api/agents              — list all agents
    POST   /api/agents              — create a new agent
    GET    /api/agents/{agent_id}   — get one agent's config
    PUT    /api/agents/{agent_id}   — update an agent's config
    DELETE /api/agents/{agent_id}   — delete an agent
"""
from __future__ import annotations

import logging

from fastapi import APIRouter, Depends, HTTPException, Request, status

from agentcore.models import AgentConfig

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/agents", tags=["agents"])


# ---------------------------------------------------------------------------
# Auth dependency
# ---------------------------------------------------------------------------


async def _require_api_key(request: Request) -> None:
    """Validate X-API-Key header against the configured secret."""
    settings = request.app.state.settings
    provided = request.headers.get("X-API-Key", "")
    if not provided or provided != settings.api_secret_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API key.")


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@router.get("", response_model=list[AgentConfig], dependencies=[Depends(_require_api_key)])
async def list_agents(request: Request):
    """Return all active agent configurations."""
    registry = request.app.state.registry
    return await registry.list_agents()


@router.post("", response_model=dict, status_code=status.HTTP_201_CREATED, dependencies=[Depends(_require_api_key)])
async def create_agent(config: AgentConfig, request: Request):
    """Create a new agent configuration and persist it to the database."""
    registry = request.app.state.registry
    agent_id = await registry.create_agent(config)
    logger.info("Agent created via API: %s", agent_id)
    return {"agent_id": agent_id, "status": "created"}


@router.get("/{agent_id}", response_model=AgentConfig, dependencies=[Depends(_require_api_key)])
async def get_agent(agent_id: str, request: Request):
    """Return a single agent's configuration by id."""
    registry = request.app.state.registry
    configs = await registry.list_agents()
    for cfg in configs:
        if cfg.id == agent_id:
            return cfg
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Agent '{agent_id}' not found.")


@router.put("/{agent_id}", response_model=dict, dependencies=[Depends(_require_api_key)])
async def update_agent(agent_id: str, config: AgentConfig, request: Request):
    """Update an existing agent's configuration."""
    registry = request.app.state.registry
    success = await registry.update_agent(agent_id, config)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Agent '{agent_id}' not found or update failed.")
    logger.info("Agent updated via API: %s", agent_id)
    return {"agent_id": agent_id, "status": "updated"}


@router.delete("/{agent_id}", response_model=dict, dependencies=[Depends(_require_api_key)])
async def delete_agent(agent_id: str, request: Request):
    """Delete an agent configuration."""
    registry = request.app.state.registry
    success = await registry.delete_agent(agent_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Agent '{agent_id}' not found or delete failed.")
    logger.info("Agent deleted via API: %s", agent_id)
    return {"agent_id": agent_id, "status": "deleted"}
