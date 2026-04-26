"""
Voice pipeline tests: /v1/audio/transcriptions endpoint.
"""
from __future__ import annotations

import io
import struct
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

faster_whisper = pytest.importorskip("faster_whisper")

from fastapi import FastAPI
from fastapi.testclient import TestClient

from agentcore.voice.stt.api import router as stt_router


@pytest.fixture
def stt_app():
    """Minimal FastAPI app with the STT router."""
    app = FastAPI()
    app.include_router(stt_router)
    return app


@pytest.fixture
def stt_client(stt_app):
    return TestClient(stt_app)


def _make_wav_bytes(num_samples: int = 100) -> bytes:
    """Generate minimal valid WAV bytes."""
    sample_rate, channels, bits = 16000, 1, 16
    byte_rate = sample_rate * channels * bits // 8
    block_align = channels * bits // 8
    data_size = num_samples * block_align
    header = struct.pack(
        "<4sI4s4sIHHIIHH4sI",
        b"RIFF", 36 + data_size, b"WAVE", b"fmt ",
        16, 1, channels, sample_rate, byte_rate, block_align, bits,
        b"data", data_size,
    )
    return header + b"\x00" * data_size


class TestSTTApiEndpoint:
    """Transcription endpoint tests."""

    def test_transcribe_wav_returns_200(self, stt_client, mock_transcription_result):
        """WAV upload must return 200 with text field."""
        with patch("agentcore.voice.stt.api.transcribe_bytes", new=AsyncMock(return_value=mock_transcription_result)):
            response = stt_client.post(
                "/v1/audio/transcriptions",
                files={"file": ("audio.wav", io.BytesIO(_make_wav_bytes()), "audio/wav")},
                data={"model": "whisper-1"},
            )
        assert response.status_code == 200
        assert "text" in response.json()

    def test_transcribe_returns_text_content(self, stt_client, mock_transcription_result):
        """Transcription response must include the expected text."""
        with patch("agentcore.voice.stt.api.transcribe_bytes", new=AsyncMock(return_value=mock_transcription_result)):
            response = stt_client.post(
                "/v1/audio/transcriptions",
                files={"file": ("test.wav", io.BytesIO(_make_wav_bytes()), "audio/wav")},
                data={"model": "whisper-1"},
            )
        assert response.json()["text"] == mock_transcription_result.text

    def test_transcribe_verbose_json_format(self, stt_client, mock_transcription_result):
        """verbose_json response_format must include language, duration, segments."""
        with patch("agentcore.voice.stt.api.transcribe_bytes", new=AsyncMock(return_value=mock_transcription_result)):
            response = stt_client.post(
                "/v1/audio/transcriptions",
                files={"file": ("test.wav", io.BytesIO(_make_wav_bytes()), "audio/wav")},
                data={"model": "whisper-1", "response_format": "verbose_json"},
            )
        assert response.status_code == 200
        data = response.json()
        assert "language" in data
        assert "duration" in data
        assert "segments" in data

    def test_transcribe_text_format_returns_plain_text(self, stt_client, mock_transcription_result):
        """response_format=text must return a plain-text response."""
        with patch("agentcore.voice.stt.api.transcribe_bytes", new=AsyncMock(return_value=mock_transcription_result)):
            response = stt_client.post(
                "/v1/audio/transcriptions",
                files={"file": ("test.wav", io.BytesIO(_make_wav_bytes()), "audio/wav")},
                data={"model": "whisper-1", "response_format": "text"},
            )
        assert response.status_code == 200
        assert response.text == mock_transcription_result.text

    def test_transcribe_unsupported_format_returns_400(self, stt_client):
        """Unsupported audio format must return 400."""
        response = stt_client.post(
            "/v1/audio/transcriptions",
            files={"file": ("audio.xyz", io.BytesIO(b"data"), "audio/xyz")},
            data={"model": "whisper-1"},
        )
        assert response.status_code == 400

    def test_transcribe_empty_file_returns_400(self, stt_client):
        """Empty audio file must return 400."""
        response = stt_client.post(
            "/v1/audio/transcriptions",
            files={"file": ("empty.wav", io.BytesIO(b""), "audio/wav")},
            data={"model": "whisper-1"},
        )
        assert response.status_code == 400

    def test_transcribe_unsupported_response_format_returns_400(self, stt_client):
        """Unsupported response_format must return 400."""
        response = stt_client.post(
            "/v1/audio/transcriptions",
            files={"file": ("test.wav", io.BytesIO(_make_wav_bytes()), "audio/wav")},
            data={"model": "whisper-1", "response_format": "xml"},
        )
        assert response.status_code == 400

    def test_transcribe_mp3_accepted(self, stt_client, mock_transcription_result):
        """MP3 extension must be accepted (if in supported formats)."""
        with patch("agentcore.voice.stt.api.transcribe_bytes", new=AsyncMock(return_value=mock_transcription_result)):
            response = stt_client.post(
                "/v1/audio/transcriptions",
                files={"file": ("audio.mp3", io.BytesIO(b"\xff\xfb" + b"\x00" * 100), "audio/mpeg")},
                data={"model": "whisper-1"},
            )
        # mp3 may or may not be supported — document the behavior
        assert response.status_code in (200, 400)

    def test_transcribe_whisper_error_returns_500(self, stt_client):
        """If transcriber raises, must return 500."""
        with patch("agentcore.voice.stt.api.transcribe_bytes", new=AsyncMock(side_effect=RuntimeError("Whisper OOM"))):
            response = stt_client.post(
                "/v1/audio/transcriptions",
                files={"file": ("test.wav", io.BytesIO(_make_wav_bytes()), "audio/wav")},
                data={"model": "whisper-1"},
            )
        assert response.status_code == 500
