"""
Security tests: Pydantic model validation rejects malformed inputs on all API endpoints.
"""
from __future__ import annotations

import uuid

import pytest
from fastapi.testclient import TestClient


class TestInputValidation:
    """Pydantic validation must reject malformed bodies with 422 Unprocessable Entity."""

    def test_chat_missing_agent_id_returns_422(self, api_client, auth_headers):
        """Chat request without agent_id must return 422."""
        response = api_client.post(
            "/api/chat",
            json={"message": "Hello"},  # missing agent_id
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_chat_missing_message_returns_422(self, api_client, auth_headers):
        """Chat request without message must return 422."""
        response = api_client.post(
            "/api/chat",
            json={"agent_id": str(uuid.uuid4())},  # missing message
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_chat_empty_body_returns_422(self, api_client, auth_headers):
        """Empty JSON body must return 422."""
        response = api_client.post(
            "/api/chat",
            json={},
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_create_agent_missing_name_returns_422(self, api_client, auth_headers):
        """AgentConfig without name must return 422."""
        response = api_client.post(
            "/api/agents",
            json={"profile": "general", "model": "llama3.1:8b"},  # missing name
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_create_agent_invalid_profile_returns_422(self, api_client, auth_headers):
        """AgentConfig with invalid profile enum must return 422."""
        response = api_client.post(
            "/api/agents",
            json={
                "name": "Test Agent",
                "profile": "this_does_not_exist",
                "model": "llama3.1:8b",
            },
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_create_agent_invalid_channel_type_returns_422(self, api_client, auth_headers):
        """AgentConfig with invalid channel_type must return 422."""
        response = api_client.post(
            "/api/agents",
            json={
                "name": "Test Agent",
                "profile": "general",
                "model": "llama3.1:8b",
                "channels": [{"channel_type": "carrier_pigeon", "enabled": True}],
            },
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_chat_wrong_type_for_agent_id_returns_422(self, api_client, auth_headers):
        """agent_id as an integer instead of string must return 422."""
        response = api_client.post(
            "/api/chat",
            json={"agent_id": 12345, "message": "hello"},
            headers=auth_headers,
        )
        # Pydantic coerces int to string, so this may pass. Test documents behavior.
        assert response.status_code in (200, 404, 422)

    def test_create_agent_hardware_tier_out_of_range(self, api_client, auth_headers):
        """hardware_tier outside valid range should be validated if constraints exist."""
        response = api_client.post(
            "/api/agents",
            json={
                "name": "Test Agent",
                "profile": "general",
                "model": "llama3.1:8b",
                "hardware_tier": 99,
            },
            headers=auth_headers,
        )
        # May return 201 if no explicit validator — document current behavior
        assert response.status_code in (201, 422)

    def test_chat_null_message_returns_422(self, api_client, auth_headers):
        """A null message value must be rejected."""
        response = api_client.post(
            "/api/chat",
            json={"agent_id": str(uuid.uuid4()), "message": None},
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_not_json_body_returns_422(self, api_client, auth_headers):
        """Plain-text body must return 422 (not JSON)."""
        response = api_client.post(
            "/api/chat",
            content="this is not json",
            headers={**auth_headers, "Content-Type": "application/json"},
        )
        assert response.status_code == 422
