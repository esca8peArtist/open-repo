"""
Voice pipeline tests: /v1/audio/speech endpoint (Kokoro TTS mocked).
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

pytest.importorskip("numpy")
soundfile = pytest.importorskip("soundfile")

from fastapi import FastAPI
from fastapi.testclient import TestClient

from agentcore.voice.tts.api import router as tts_router
from agentcore.voice.tts.synthesizer import AVAILABLE_VOICES


@pytest.fixture
def tts_app():
    """Minimal FastAPI app with the TTS router."""
    app = FastAPI()
    app.include_router(tts_router)
    return app


@pytest.fixture
def tts_client(tts_app):
    return TestClient(tts_app)


class TestTTSApiEndpoint:
    """TTS speech endpoint tests."""

    def test_create_speech_success(self, tts_client, mock_synthesis_result):
        """POST /v1/audio/speech must return 200 with audio bytes."""
        with patch("agentcore.voice.tts.api.synthesize", new=AsyncMock(return_value=mock_synthesis_result)):
            response = tts_client.post(
                "/v1/audio/speech",
                json={"model": "tts-1", "input": "Hello world", "voice": AVAILABLE_VOICES[0]},
            )
        assert response.status_code == 200
        assert len(response.content) > 0

    def test_create_speech_wav_content_type(self, tts_client, mock_synthesis_result):
        """WAV format must return audio/wav content type."""
        with patch("agentcore.voice.tts.api.synthesize", new=AsyncMock(return_value=mock_synthesis_result)):
            response = tts_client.post(
                "/v1/audio/speech",
                json={"model": "tts-1", "input": "Test", "voice": AVAILABLE_VOICES[0], "response_format": "wav"},
            )
        assert "audio" in response.headers.get("content-type", "")

    def test_create_speech_empty_input_returns_400(self, tts_client):
        """Empty input text must return 400."""
        response = tts_client.post(
            "/v1/audio/speech",
            json={"model": "tts-1", "input": "   ", "voice": AVAILABLE_VOICES[0]},
        )
        assert response.status_code == 400

    def test_create_speech_invalid_voice_returns_422(self, tts_client):
        """Unknown voice ID must return 422 (Pydantic validation)."""
        response = tts_client.post(
            "/v1/audio/speech",
            json={"model": "tts-1", "input": "Hello", "voice": "nonexistent_voice_xyz"},
        )
        assert response.status_code == 422

    def test_create_speech_invalid_format_returns_422(self, tts_client):
        """Unsupported response_format must return 422."""
        response = tts_client.post(
            "/v1/audio/speech",
            json={"model": "tts-1", "input": "Hello", "voice": AVAILABLE_VOICES[0], "response_format": "xyz_unsupported"},
        )
        assert response.status_code == 422

    def test_create_speech_speed_out_of_range_returns_422(self, tts_client):
        """Speed outside [0.25, 4.0] must return 422."""
        response = tts_client.post(
            "/v1/audio/speech",
            json={"model": "tts-1", "input": "Hello", "voice": AVAILABLE_VOICES[0], "speed": 10.0},
        )
        assert response.status_code == 422

    def test_create_speech_response_headers(self, tts_client, mock_synthesis_result):
        """TTS response must include custom headers: X-Synthesis-Duration, X-Voice, X-Sample-Rate."""
        with patch("agentcore.voice.tts.api.synthesize", new=AsyncMock(return_value=mock_synthesis_result)):
            response = tts_client.post(
                "/v1/audio/speech",
                json={"model": "tts-1", "input": "Hello", "voice": AVAILABLE_VOICES[0]},
            )
        assert "X-Synthesis-Duration" in response.headers or "x-synthesis-duration" in response.headers
        assert "X-Voice" in response.headers or "x-voice" in response.headers

    def test_create_speech_synthesizer_error_returns_500(self, tts_client):
        """Synthesizer exception must return 500."""
        with patch("agentcore.voice.tts.api.synthesize", new=AsyncMock(side_effect=RuntimeError("Kokoro crash"))):
            response = tts_client.post(
                "/v1/audio/speech",
                json={"model": "tts-1", "input": "Hello", "voice": AVAILABLE_VOICES[0]},
            )
        assert response.status_code == 500

    def test_list_voices_endpoint(self, tts_client):
        """GET /v1/audio/voices must return a list of available voices."""
        with patch("agentcore.voice.tts.api._list_voices", new=AsyncMock(return_value=[{"voice_id": v} for v in AVAILABLE_VOICES])):
            response = tts_client.get("/v1/audio/voices")
        assert response.status_code == 200
        assert "voices" in response.json()
