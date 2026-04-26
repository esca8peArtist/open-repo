"""
AgentCore API tests: SSE streaming delivers chunks correctly.
"""
from __future__ import annotations

import json
from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient


class TestStreamingSSE:
    """Detailed SSE streaming correctness tests."""

    def _collect_sse_events(self, raw_text: str) -> list[dict]:
        """Parse all SSE data lines from raw response text."""
        events = []
        for line in raw_text.split("\n"):
            line = line.strip()
            if line.startswith("data:"):
                payload = line[5:].strip()
                if payload:
                    try:
                        events.append(json.loads(payload))
                    except json.JSONDecodeError:
                        pass
        return events

    def test_stream_delivers_multiple_chunks(self, api_client, auth_headers, test_app, agent_instance):
        """Stream must deliver all yielded chunks in order."""
        chunks = ["Hello", " ", "world", "!"]

        async def _fake_stream(message, session_id, conversation_id=None):
            for c in chunks:
                yield c

        agent_instance.chat_stream = _fake_stream
        test_app.state.registry.get_agent = AsyncMock(return_value=agent_instance)

        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": "test", "message": "hi"},
            headers=auth_headers,
        )
        events = self._collect_sse_events(response.text)
        # Expect N delta events + 1 final done event
        delta_events = [e for e in events if not e.get("done")]
        done_events = [e for e in events if e.get("done")]

        assert len(delta_events) == len(chunks)
        assert len(done_events) == 1
        assert [e["delta"] for e in delta_events] == chunks

    def test_stream_session_id_consistent(self, api_client, auth_headers, test_app, agent_instance):
        """All stream events must share the same session_id."""
        session_id = "fixed-session-123"

        async def _fake_stream(message, session_id, conversation_id=None):
            yield "chunk"

        agent_instance.chat_stream = _fake_stream
        test_app.state.registry.get_agent = AsyncMock(return_value=agent_instance)

        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": "test", "message": "hi", "session_id": session_id},
            headers=auth_headers,
        )
        events = self._collect_sse_events(response.text)
        for event in events:
            assert event["session_id"] == session_id

    def test_stream_done_event_has_empty_delta(self, api_client, auth_headers, test_app, agent_instance):
        """The final done event must have an empty delta string."""
        async def _fake_stream(message, session_id, conversation_id=None):
            yield "content"

        agent_instance.chat_stream = _fake_stream
        test_app.state.registry.get_agent = AsyncMock(return_value=agent_instance)

        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": "test", "message": "hi"},
            headers=auth_headers,
        )
        events = self._collect_sse_events(response.text)
        done_event = next(e for e in events if e.get("done") is True)
        assert done_event["delta"] == ""

    def test_stream_error_during_generation_yields_error_event(self, api_client, auth_headers, test_app, agent_instance):
        """When stream raises, the error must be surfaced in an SSE event (not 500)."""
        async def _failing_stream(message, session_id, conversation_id=None):
            yield "partial"
            raise RuntimeError("Simulated generation failure")

        agent_instance.chat_stream = _failing_stream
        test_app.state.registry.get_agent = AsyncMock(return_value=agent_instance)

        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": "test", "message": "hi"},
            headers=auth_headers,
        )
        # Must not 500; response body should contain an error event
        assert response.status_code == 200
        events = self._collect_sse_events(response.text)
        # Should have at least one event with done=True
        done_events = [e for e in events if e.get("done")]
        assert len(done_events) >= 1

    def test_stream_cache_control_header_set(self, api_client, auth_headers, test_app, agent_instance):
        """SSE response must set Cache-Control: no-cache."""
        async def _fake_stream(message, session_id, conversation_id=None):
            yield "ok"

        agent_instance.chat_stream = _fake_stream
        test_app.state.registry.get_agent = AsyncMock(return_value=agent_instance)

        response = api_client.post(
            "/api/chat/stream",
            json={"agent_id": "test", "message": "hi"},
            headers=auth_headers,
        )
        assert "no-cache" in response.headers.get("cache-control", "").lower()
