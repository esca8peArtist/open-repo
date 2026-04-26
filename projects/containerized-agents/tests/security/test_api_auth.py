"""
Security tests: all admin and dashboard endpoints reject requests without a valid API key.
"""
from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from agentcore.models import AgentConfig, AgentProfile


class TestApiAuthEnforcement:
    """Every protected endpoint must return 401 without a valid X-API-Key."""

    def test_chat_endpoint_no_key_returns_401(self, api_client):
        """POST /api/chat without API key must return 401."""
        response = api_client.post(
            "/api/chat",
            json={"agent_id": "test-id", "message": "hello"},
        )
        assert response.status_code == 401

    def test_chat_stream_no_key_returns_401(self, api_client):
        """POST /api/chat/stream without API key must return 401."""
        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": "test-id", "message": "hello"},
        )
        assert response.status_code == 401

    def test_list_agents_no_key_returns_401(self, api_client):
        """GET /api/agents without API key must return 401."""
        response = api_client.get("/api/agents")
        assert response.status_code == 401

    def test_create_agent_no_key_returns_401(self, api_client):
        """POST /api/agents without API key must return 401."""
        response = api_client.post(
            "/api/agents",
            json={"name": "Test", "profile": "general", "model": "llama3.1:8b"},
        )
        assert response.status_code == 401

    def test_get_agent_no_key_returns_401(self, api_client):
        """GET /api/agents/{id} without API key must return 401."""
        response = api_client.get(f"/api/agents/{uuid.uuid4()}")
        assert response.status_code == 401

    def test_update_agent_no_key_returns_401(self, api_client):
        """PUT /api/agents/{id} without API key must return 401."""
        response = api_client.put(
            f"/api/agents/{uuid.uuid4()}",
            json={"name": "Updated", "profile": "general", "model": "llama3.1:8b"},
        )
        assert response.status_code == 401

    def test_delete_agent_no_key_returns_401(self, api_client):
        """DELETE /api/agents/{id} without API key must return 401."""
        response = api_client.delete(f"/api/agents/{uuid.uuid4()}")
        assert response.status_code == 401

    def test_admin_reload_no_key_returns_401(self, api_client):
        """POST /api/admin/reload without API key must return 401."""
        response = api_client.post("/api/admin/reload")
        assert response.status_code == 401

    def test_admin_status_no_key_returns_401(self, api_client):
        """GET /api/admin/status without API key must return 401."""
        response = api_client.get("/api/admin/status")
        assert response.status_code == 401

    def test_admin_connectivity_no_key_returns_401(self, api_client):
        """POST /api/admin/connectivity without API key must return 401."""
        response = api_client.post("/api/admin/connectivity")
        assert response.status_code == 401

    def test_wrong_api_key_returns_401(self, api_client):
        """Wrong API key must return 401."""
        response = api_client.get(
            "/api/agents",
            headers={"X-API-Key": "definitely-wrong-key"},
        )
        assert response.status_code == 401

    def test_correct_api_key_passes_auth(self, api_client, auth_headers):
        """Correct API key must pass the auth check (not 401)."""
        response = api_client.get("/api/agents", headers=auth_headers)
        # Should return 200 (empty list) since registry is mocked
        assert response.status_code == 200

    def test_health_endpoint_no_auth_required(self, api_client):
        """GET /health must not require API key (liveness probe)."""
        response = api_client.get("/health")
        assert response.status_code == 200

    def test_api_health_no_auth_required(self, api_client):
        """GET /api/health must not require API key."""
        response = api_client.get("/api/health")
        assert response.status_code == 200

    def test_empty_api_key_rejected(self, api_client):
        """An empty string API key must be rejected."""
        response = api_client.get("/api/agents", headers={"X-API-Key": ""})
        assert response.status_code == 401
