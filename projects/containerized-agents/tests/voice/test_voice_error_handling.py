"""
Voice pipeline tests: graceful handling of corrupt/empty audio.
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
    app = FastAPI()
    app.include_router(stt_router)
    return app


@pytest.fixture
def stt_client(stt_app):
    return TestClient(stt_app)


class TestVoiceErrorHandling:
    """Corrupt and edge-case audio input must be handled gracefully."""

    def test_empty_wav_returns_400(self, stt_client):
        """Zero-byte audio file must return 400."""
        response = stt_client.post(
            "/v1/audio/transcriptions",
            files={"file": ("empty.wav", io.BytesIO(b""), "audio/wav")},
            data={"model": "whisper-1"},
        )
        assert response.status_code == 400

    def test_corrupt_wav_header_returns_500_or_400(self, stt_client):
        """Corrupt WAV with invalid header must return 400 or 500 (not 200)."""
        with patch("agentcore.voice.stt.api.transcribe_bytes", new=AsyncMock(side_effect=Exception("Invalid WAV"))):
            response = stt_client.post(
                "/v1/audio/transcriptions",
                files={"file": ("corrupt.wav", io.BytesIO(b"not a valid wav file bytes"), "audio/wav")},
                data={"model": "whisper-1"},
            )
        assert response.status_code in (400, 500)

    def test_too_large_audio_returns_413(self, stt_client):
        """File exceeding 25 MB must return 413."""
        big_audio = b"\x00" * (26 * 1024 * 1024)  # 26 MB
        response = stt_client.post(
            "/v1/audio/transcriptions",
            files={"file": ("big.wav", io.BytesIO(big_audio), "audio/wav")},
            data={"model": "whisper-1"},
        )
        assert response.status_code == 413

    def test_unsupported_audio_format_returns_400(self, stt_client):
        """Audio file with .xyz extension must return 400."""
        response = stt_client.post(
            "/v1/audio/transcriptions",
            files={"file": ("audio.xyz", io.BytesIO(b"data"), "application/octet-stream")},
            data={"model": "whisper-1"},
        )
        assert response.status_code == 400

    def test_transcriber_oom_returns_500(self, stt_client):
        """Out-of-memory error during transcription must return 500."""
        with patch("agentcore.voice.stt.api.transcribe_bytes", new=AsyncMock(side_effect=MemoryError("OOM"))):
            response = stt_client.post(
                "/v1/audio/transcriptions",
                files={"file": ("test.wav", io.BytesIO(b"\x00" * 200), "audio/wav")},
                data={"model": "whisper-1"},
            )
        assert response.status_code == 500

    def test_very_short_audio_accepted(self, stt_client, mock_transcription_result):
        """Very short but valid WAV (100 samples) must be accepted."""
        num_samples = 100
        data_size = num_samples * 2
        header = struct.pack(
            "<4sI4s4sIHHIIHH4sI",
            b"RIFF", 36 + data_size, b"WAVE", b"fmt ",
            16, 1, 1, 16000, 32000, 2, 16,
            b"data", data_size,
        )
        wav_bytes = header + b"\x00" * data_size

        with patch("agentcore.voice.stt.api.transcribe_bytes", new=AsyncMock(return_value=mock_transcription_result)):
            response = stt_client.post(
                "/v1/audio/transcriptions",
                files={"file": ("short.wav", io.BytesIO(wav_bytes), "audio/wav")},
                data={"model": "whisper-1"},
            )
        assert response.status_code == 200

    def test_missing_file_field_returns_422(self, stt_client):
        """Request without file field must return 422."""
        response = stt_client.post(
            "/v1/audio/transcriptions",
            data={"model": "whisper-1"},
        )
        assert response.status_code == 422
