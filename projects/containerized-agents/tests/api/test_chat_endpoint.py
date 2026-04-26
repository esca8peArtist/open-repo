"""
AgentCore API tests: /api/chat sync and streaming endpoints.
"""
from __future__ import annotations

import json
import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from agentcore.models import ChatResponse


class TestChatEndpoint:
    """Synchronous /api/chat endpoint tests."""

    def test_chat_no_api_key_returns_401(self, api_client):
        """Chat without API key must return 401."""
        response = api_client.post(
            "/api/chat",
            json={"agent_id": "test", "message": "hello"},
        )
        assert response.status_code == 401

    def test_chat_unknown_agent_returns_404(self, api_client, auth_headers, test_app):
        """Chat with unknown agent_id must return 404."""
        test_app.state.registry.get_agent = AsyncMock(return_value=None)
        response = api_client.post(
            "/api/chat",
            json={"agent_id": str(uuid.uuid4()), "message": "hello"},
            headers=auth_headers,
        )
        assert response.status_code == 404

    def test_chat_with_agent_returns_200(self, api_client, auth_headers, test_app, agent_instance):
        """Chat with a known agent must return 200 and a ChatResponse."""
        test_app.state.registry.get_agent = AsyncMock(return_value=agent_instance)

        response = api_client.post(
            "/api/chat",
            json={
                "agent_id": "test-agent-id",
                "message": "Hello, what is 2+2?",
                "session_id": str(uuid.uuid4()),
            },
            headers=auth_headers,
        )
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "agent_id" in data
        assert "session_id" in data

    def test_chat_response_schema_valid(self, api_client, auth_headers, test_app, agent_instance):
        """Chat response must match the ChatResponse schema."""
        test_app.state.registry.get_agent = AsyncMock(return_value=agent_instance)

        response = api_client.post(
            "/api/chat",
            json={"agent_id": "test-agent", "message": "test"},
            headers=auth_headers,
        )
        assert response.status_code == 200
        data = response.json()
        # Validate required fields
        assert isinstance(data["message"], str)
        assert isinstance(data["tokens_used"], int)
        assert isinstance(data["duration_ms"], int)

    def test_chat_missing_message_returns_422(self, api_client, auth_headers):
        """Missing message field must return 422."""
        response = api_client.post(
            "/api/chat",
            json={"agent_id": "test"},
            headers=auth_headers,
        )
        assert response.status_code == 422


class TestChatStreamEndpoint:
    """SSE streaming /api/chat/stream endpoint tests."""

    def test_stream_no_api_key_returns_401(self, api_client):
        """Stream without API key must return 401."""
        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": "test", "message": "hello"},
        )
        assert response.status_code == 401

    def test_stream_unknown_agent_returns_404(self, api_client, auth_headers, test_app):
        """Stream with unknown agent must return 404."""
        test_app.state.registry.get_agent = AsyncMock(return_value=None)
        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": str(uuid.uuid4()), "message": "hello"},
            headers=auth_headers,
        )
        assert response.status_code == 404

    def test_stream_returns_event_stream_content_type(self, api_client, auth_headers, test_app, agent_instance):
        """Stream endpoint must return text/event-stream content-type."""
        async def _fake_stream(message, session_id):
            yield "Hello"
            yield " world"

        agent_instance.chat_stream = _fake_stream
        test_app.state.registry.get_agent = AsyncMock(return_value=agent_instance)

        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": "test", "message": "hello"},
            headers=auth_headers,
        )
        assert response.status_code == 200
        assert "text/event-stream" in response.headers.get("content-type", "")

    def test_stream_chunks_have_correct_format(self, api_client, auth_headers, test_app, agent_instance):
        """Each SSE chunk must be in 'data: {...}' format."""
        async def _fake_stream(message, session_id):
            yield "chunk1"
            yield "chunk2"

        agent_instance.chat_stream = _fake_stream
        test_app.state.registry.get_agent = AsyncMock(return_value=agent_instance)

        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": "test", "message": "hello"},
            headers=auth_headers,
        )
        assert response.status_code == 200
        lines = [line for line in response.text.split("\n") if line.startswith("data:")]
        assert len(lines) >= 1
        for line in lines:
            payload = json.loads(line[len("data: "):])
            assert "delta" in payload
            assert "done" in payload
            assert "session_id" in payload

    def test_stream_final_chunk_has_done_true(self, api_client, auth_headers, test_app, agent_instance):
        """The last SSE chunk must have done=True."""
        async def _fake_stream(message, session_id):
            yield "last"

        agent_instance.chat_stream = _fake_stream
        test_app.state.registry.get_agent = AsyncMock(return_value=agent_instance)

        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": "test", "message": "hello"},
            headers=auth_headers,
        )
        lines = [line for line in response.text.split("\n") if line.startswith("data:")]
        last = json.loads(lines[-1][len("data: "):])
        assert last["done"] is True
