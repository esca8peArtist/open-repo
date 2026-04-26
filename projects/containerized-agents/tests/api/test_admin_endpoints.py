"""
AgentCore API tests: /api/admin/* endpoints (reload, status, connectivity, routing).
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient


class TestAdminReloadEndpoint:
    """POST /api/admin/reload tests."""

    def test_reload_no_auth_returns_401(self, api_client):
        """Reload without API key must return 401."""
        assert api_client.post("/api/admin/reload").status_code == 401

    def test_reload_with_auth_returns_200(self, api_client, auth_headers, test_app):
        """Reload with valid API key must return 200."""
        test_app.state.registry.reload = AsyncMock()
        test_app.state.registry.list_agents = AsyncMock(return_value=[])
        response = api_client.post("/api/admin/reload", headers=auth_headers)
        assert response.status_code == 200

    def test_reload_response_schema(self, api_client, auth_headers, test_app):
        """Reload response must include status, agents_loaded, and timestamp."""
        test_app.state.registry.reload = AsyncMock()
        test_app.state.registry.list_agents = AsyncMock(return_value=[])
        response = api_client.post("/api/admin/reload", headers=auth_headers)
        data = response.json()
        assert data["status"] == "ok"
        assert "agents_loaded" in data
        assert isinstance(data["agents_loaded"], int)
        assert "timestamp" in data

    def test_reload_calls_registry_reload(self, api_client, auth_headers, test_app):
        """Reload must call registry.reload()."""
        test_app.state.registry.reload = AsyncMock()
        test_app.state.registry.list_agents = AsyncMock(return_value=[])
        api_client.post("/api/admin/reload", headers=auth_headers)
        test_app.state.registry.reload.assert_called_once()


class TestAdminStatusEndpoint:
    """GET /api/admin/status tests."""

    def test_status_no_auth_returns_401(self, api_client):
        """Status without API key must return 401."""
        assert api_client.get("/api/admin/status").status_code == 401

    def test_status_returns_200(self, api_client, auth_headers, test_app):
        """Status with valid API key must return 200."""
        test_app.state.registry.list_agents = AsyncMock(return_value=[])
        response = api_client.get("/api/admin/status", headers=auth_headers)
        assert response.status_code == 200

    def test_status_response_has_required_fields(self, api_client, auth_headers, test_app):
        """Status response must include all expected keys."""
        test_app.state.registry.list_agents = AsyncMock(return_value=[])
        response = api_client.get("/api/admin/status", headers=auth_headers)
        data = response.json()
        for field in ["status", "version", "uptime_seconds", "agents", "connectivity", "settings"]:
            assert field in data, f"Missing field: {field}"

    def test_status_agents_schema(self, api_client, auth_headers, test_app):
        """Status.agents must have total_configured and live_instances."""
        test_app.state.registry.list_agents = AsyncMock(return_value=[])
        response = api_client.get("/api/admin/status", headers=auth_headers)
        agents = response.json()["agents"]
        assert "total_configured" in agents
        assert "live_instances" in agents

    def test_status_settings_no_secrets(self, api_client, auth_headers, test_app):
        """Status settings must not expose api_secret_key or DB passwords."""
        test_app.state.registry.list_agents = AsyncMock(return_value=[])
        response = api_client.get("/api/admin/status", headers=auth_headers)
        raw = response.text
        # api_secret_key value must not appear in the response
        assert "test-secret-key-32-chars-minimum" not in raw


class TestAdminConnectivityEndpoint:
    """POST /api/admin/connectivity tests."""

    def test_connectivity_no_auth_returns_401(self, api_client):
        """Connectivity check without API key must return 401."""
        assert api_client.post("/api/admin/connectivity").status_code == 401

    def test_connectivity_returns_200(self, api_client, auth_headers, test_app):
        """Connectivity with valid API key must return 200."""
        test_app.state.dispatcher.is_online = AsyncMock(return_value=True)
        test_app.state.dispatcher.invalidate_connectivity_cache = MagicMock()
        response = api_client.post("/api/admin/connectivity", headers=auth_headers)
        assert response.status_code == 200

    def test_connectivity_response_has_online_field(self, api_client, auth_headers, test_app):
        """Connectivity response must include 'online' bool."""
        test_app.state.dispatcher.is_online = AsyncMock(return_value=True)
        test_app.state.dispatcher.invalidate_connectivity_cache = MagicMock()
        response = api_client.post("/api/admin/connectivity", headers=auth_headers)
        data = response.json()
        assert "online" in data
        assert isinstance(data["online"], bool)

    def test_connectivity_no_dispatcher_returns_503(self, api_client, auth_headers, test_app):
        """If dispatcher is not available, must return 503."""
        del test_app.state.dispatcher
        response = api_client.post("/api/admin/connectivity", headers=auth_headers)
        assert response.status_code == 503


class TestAdminLiveInstancesEndpoint:
    """GET /api/admin/agents/instances tests."""

    def test_instances_no_auth_returns_401(self, api_client):
        """Instances endpoint without API key must return 401."""
        assert api_client.get("/api/admin/agents/instances").status_code == 401

    def test_instances_returns_200(self, api_client, auth_headers, test_app):
        """Instances endpoint with valid key must return 200."""
        test_app.state.registry._instances = {}
        response = api_client.get("/api/admin/agents/instances", headers=auth_headers)
        assert response.status_code == 200

    def test_instances_schema(self, api_client, auth_headers, test_app):
        """Instances response must have live_instances list and count."""
        test_app.state.registry._instances = {"agent-1": MagicMock()}
        response = api_client.get("/api/admin/agents/instances", headers=auth_headers)
        data = response.json()
        assert "live_instances" in data
        assert "count" in data
        assert data["count"] == 1
        assert "agent-1" in data["live_instances"]
