"""
AgentCore API tests: full CRUD lifecycle for agent configs via REST API.
"""
from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from agentcore.models import AgentConfig, AgentProfile, ChannelConfig, ChannelType


class TestAgentsCRUD:
    """Full CRUD lifecycle tests for /api/agents."""

    def _make_config(self, name: str = "Test Agent") -> dict:
        return {
            "name": name,
            "profile": "personal_productivity",
            "model": "qwen2.5:7b-instruct",
            "system_prompt": "You are a helpful assistant.",
            "tools": [],
            "channels": [{"channel_type": "web", "enabled": True}],
            "hardware_tier": 1,
            "rag_enabled": False,
            "active": True,
        }

    def test_list_agents_empty(self, api_client, auth_headers, test_app):
        """GET /api/agents returns empty list when no agents configured."""
        test_app.state.registry.list_agents = AsyncMock(return_value=[])
        response = api_client.get("/api/agents", headers=auth_headers)
        assert response.status_code == 200
        assert response.json() == []

    def test_list_agents_returns_agents(self, api_client, auth_headers, test_app, sample_agent_config):
        """GET /api/agents returns list of configured agents."""
        test_app.state.registry.list_agents = AsyncMock(return_value=[sample_agent_config])
        response = api_client.get("/api/agents", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["name"] == sample_agent_config.name

    def test_create_agent_returns_201(self, api_client, auth_headers, test_app):
        """POST /api/agents returns 201 Created with agent_id."""
        new_id = str(uuid.uuid4())
        test_app.state.registry.create_agent = AsyncMock(return_value=new_id)

        response = api_client.post(
            "/api/agents",
            json=self._make_config("New Agent"),
            headers=auth_headers,
        )
        assert response.status_code == 201
        data = response.json()
        assert "agent_id" in data
        assert data["status"] == "created"

    def test_get_existing_agent(self, api_client, auth_headers, test_app, sample_agent_config):
        """GET /api/agents/{id} returns the agent config."""
        test_app.state.registry.list_agents = AsyncMock(return_value=[sample_agent_config])
        response = api_client.get(f"/api/agents/{sample_agent_config.id}", headers=auth_headers)
        assert response.status_code == 200
        assert response.json()["name"] == sample_agent_config.name

    def test_get_nonexistent_agent_returns_404(self, api_client, auth_headers, test_app):
        """GET /api/agents/{unknown_id} must return 404."""
        test_app.state.registry.list_agents = AsyncMock(return_value=[])
        response = api_client.get(f"/api/agents/{uuid.uuid4()}", headers=auth_headers)
        assert response.status_code == 404

    def test_update_existing_agent(self, api_client, auth_headers, test_app, sample_agent_config):
        """PUT /api/agents/{id} updates agent and returns status='updated'."""
        test_app.state.registry.update_agent = AsyncMock(return_value=True)
        updated_config = self._make_config("Updated Agent")
        response = api_client.put(
            f"/api/agents/{sample_agent_config.id}",
            json=updated_config,
            headers=auth_headers,
        )
        assert response.status_code == 200
        assert response.json()["status"] == "updated"

    def test_update_nonexistent_agent_returns_404(self, api_client, auth_headers, test_app):
        """PUT /api/agents/{unknown_id} must return 404."""
        test_app.state.registry.update_agent = AsyncMock(return_value=False)
        response = api_client.put(
            f"/api/agents/{uuid.uuid4()}",
            json=self._make_config(),
            headers=auth_headers,
        )
        assert response.status_code == 404

    def test_delete_existing_agent(self, api_client, auth_headers, test_app):
        """DELETE /api/agents/{id} deletes agent and returns status='deleted'."""
        agent_id = str(uuid.uuid4())
        test_app.state.registry.delete_agent = AsyncMock(return_value=True)
        response = api_client.delete(f"/api/agents/{agent_id}", headers=auth_headers)
        assert response.status_code == 200
        assert response.json()["status"] == "deleted"

    def test_delete_nonexistent_agent_returns_404(self, api_client, auth_headers, test_app):
        """DELETE /api/agents/{unknown_id} must return 404."""
        test_app.state.registry.delete_agent = AsyncMock(return_value=False)
        response = api_client.delete(f"/api/agents/{uuid.uuid4()}", headers=auth_headers)
        assert response.status_code == 404

    def test_all_crud_require_auth(self, api_client):
        """All CRUD operations require authentication."""
        agent_id = str(uuid.uuid4())
        config = self._make_config()

        assert api_client.get("/api/agents").status_code == 401
        assert api_client.post("/api/agents", json=config).status_code == 401
        assert api_client.get(f"/api/agents/{agent_id}").status_code == 401
        assert api_client.put(f"/api/agents/{agent_id}", json=config).status_code == 401
        assert api_client.delete(f"/api/agents/{agent_id}").status_code == 401
