"""
AgentCore API tests: /health and /api/health return correct schema.
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient


class TestHealthEndpoint:
    """Health check endpoint tests."""

    def test_health_returns_200(self, api_client):
        """GET /health must return 200 OK."""
        response = api_client.get("/health")
        assert response.status_code == 200

    def test_api_health_returns_200(self, api_client):
        """GET /api/health must return 200 OK."""
        response = api_client.get("/api/health")
        assert response.status_code == 200

    def test_health_has_status_ok(self, api_client):
        """Health response must have status='ok'."""
        response = api_client.get("/health")
        data = response.json()
        assert data["status"] == "ok"

    def test_health_has_version(self, api_client):
        """Health response must include a version string."""
        response = api_client.get("/health")
        data = response.json()
        assert "version" in data
        assert isinstance(data["version"], str)
        assert len(data["version"]) > 0

    def test_health_has_timestamp(self, api_client):
        """Health response must include a timestamp."""
        response = api_client.get("/health")
        data = response.json()
        assert "timestamp" in data
        assert "T" in data["timestamp"]  # ISO format

    def test_health_has_uptime(self, api_client):
        """Health response must include uptime_seconds >= 0."""
        response = api_client.get("/health")
        data = response.json()
        assert "uptime_seconds" in data
        assert data["uptime_seconds"] >= 0

    def test_health_has_dependencies(self, api_client):
        """Health response must include a dependencies dict."""
        response = api_client.get("/health")
        data = response.json()
        assert "dependencies" in data
        deps = data["dependencies"]
        assert isinstance(deps, dict)
        assert "postgres" in deps
        assert "redis" in deps

    def test_health_dependencies_valid_values(self, api_client):
        """Dependency values must be 'ok', 'unavailable', or 'unconfigured'."""
        response = api_client.get("/health")
        data = response.json()
        valid_values = {"ok", "unavailable", "unconfigured"}
        for dep_name, dep_status in data["dependencies"].items():
            assert dep_status in valid_values, (
                f"Dependency '{dep_name}' has unexpected status: '{dep_status}'"
            )

    def test_api_health_same_schema_as_health(self, api_client):
        """Both /health and /api/health must return identical schemas."""
        r1 = api_client.get("/health").json()
        r2 = api_client.get("/api/health").json()
        # Same keys (values may differ due to timing)
        assert set(r1.keys()) == set(r2.keys())

    def test_health_no_auth_required(self, api_client):
        """Health endpoints must work without X-API-Key."""
        # No auth headers provided
        r1 = api_client.get("/health")
        r2 = api_client.get("/api/health")
        assert r1.status_code == 200
        assert r2.status_code == 200

    def test_health_redis_unavailable_when_redis_ping_fails(self, api_client, test_app):
        """When Redis ping fails, health must report redis='unavailable' (not 500)."""
        test_app.state.redis.ping = AsyncMock(side_effect=Exception("Connection refused"))
        response = api_client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["dependencies"]["redis"] == "unavailable"
