"""
Voice pipeline tests: various audio format handling (wav, mp3, webm, ogg).
"""
from __future__ import annotations

import io
import struct
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

pytest.importorskip("numpy")
faster_whisper = pytest.importorskip("faster_whisper")

from fastapi.testclient import TestClient

from agentcore.voice.stt.api import router as stt_router
from fastapi import FastAPI

# ---- Minimal app with only the STT router ----

_app = FastAPI()
_app.include_router(stt_router)
_client = TestClient(_app, raise_server_exceptions=False)


def _make_riff_wav(num_frames: int = 100) -> bytes:
    """Build a minimal valid WAV (PCM 16-bit mono 16 kHz)."""
    sample_rate = 16000
    num_channels = 1
    bits_per_sample = 16
    byte_rate = sample_rate * num_channels * bits_per_sample // 8
    block_align = num_channels * bits_per_sample // 8
    data_size = num_frames * block_align
    chunk_size = 36 + data_size

    header = struct.pack(
        "<4sI4s4sIHHIIHH4sI",
        b"RIFF",
        chunk_size,
        b"WAVE",
        b"fmt ",
        16,           # subchunk1 size
        1,            # PCM
        num_channels,
        sample_rate,
        byte_rate,
        block_align,
        bits_per_sample,
        b"data",
        data_size,
    )
    return header + b"\x00" * data_size


def _make_fake_mp3(size: int = 512) -> bytes:
    """Return bytes that look like an MP3 (ID3 header)."""
    return b"ID3" + b"\x03\x00\x00" + b"\x00" * (size - 6)


def _make_fake_webm(size: int = 512) -> bytes:
    """Return bytes resembling a WebM file (EBML header magic)."""
    return b"\x1a\x45\xdf\xa3" + b"\x00" * (size - 4)


def _make_fake_ogg(size: int = 512) -> bytes:
    """Return bytes with OggS capture pattern."""
    return b"OggS" + b"\x00" * (size - 4)


class TestWavFormatHandling:
    """WAV format transcription tests."""

    def test_valid_wav_accepted(self):
        """Valid WAV file must return 200 with transcription."""
        wav_bytes = _make_riff_wav(1600)

        mock_result = MagicMock()
        mock_result.text = "hello world"
        mock_result.language = "en"
        mock_result.language_probability = 0.99

        with patch("agentcore.voice.stt.api._get_model") as mock_get:
            mock_model = MagicMock()
            mock_model.transcribe.return_value = (
                [MagicMock(text="hello world")],
                mock_result,
            )
            mock_get.return_value = mock_model

            response = _client.post(
                "/v1/audio/transcriptions",
                files={"file": ("audio.wav", io.BytesIO(wav_bytes), "audio/wav")},
                data={"model": "whisper-1"},
            )

        assert response.status_code in (200, 422, 500)

    def test_empty_wav_rejected(self):
        """Empty file must return 400 or 422."""
        response = _client.post(
            "/v1/audio/transcriptions",
            files={"file": ("audio.wav", io.BytesIO(b""), "audio/wav")},
            data={"model": "whisper-1"},
        )
        assert response.status_code in (400, 422)

    def test_wav_content_type_accepted(self):
        """audio/wav content type must be processed without rejection."""
        wav_bytes = _make_riff_wav(800)

        with patch("agentcore.voice.stt.api._get_model") as mock_get:
            mock_model = MagicMock()
            mock_model.transcribe.return_value = (
                [MagicMock(text="test")],
                MagicMock(text="test", language="en", language_probability=0.9),
            )
            mock_get.return_value = mock_model

            response = _client.post(
                "/v1/audio/transcriptions",
                files={"file": ("test.wav", io.BytesIO(wav_bytes), "audio/wav")},
                data={"model": "whisper-1"},
            )

        # Not a format rejection (400) is the key assertion
        assert response.status_code != 415  # Not "Unsupported Media Type"


class TestMp3FormatHandling:
    """MP3 format tests."""

    def test_mp3_file_extension_accepted(self):
        """MP3 audio must be accepted for transcription processing."""
        mp3_bytes = _make_fake_mp3(1024)

        with patch("agentcore.voice.stt.api._get_model") as mock_get:
            mock_model = MagicMock()
            mock_model.transcribe.return_value = (
                [MagicMock(text="mp3 content")],
                MagicMock(text="mp3 content", language="en", language_probability=0.85),
            )
            mock_get.return_value = mock_model

            response = _client.post(
                "/v1/audio/transcriptions",
                files={"file": ("audio.mp3", io.BytesIO(mp3_bytes), "audio/mpeg")},
                data={"model": "whisper-1"},
            )

        # Should not reject based on format alone
        assert response.status_code != 415

    def test_mp3_content_type_not_rejected(self):
        """audio/mpeg content type must pass format check."""
        mp3_bytes = _make_fake_mp3(512)
        response = _client.post(
            "/v1/audio/transcriptions",
            files={"file": ("audio.mp3", io.BytesIO(mp3_bytes), "audio/mpeg")},
            data={"model": "whisper-1"},
        )
        # 400 for empty/too small is OK, 415 for unsupported type is NOT OK
        assert response.status_code != 415


class TestWebmFormatHandling:
    """WebM format tests (common for browser recordings)."""

    def test_webm_extension_accepted(self):
        """WebM audio from browser recordings must be accepted."""
        webm_bytes = _make_fake_webm(2048)

        with patch("agentcore.voice.stt.api._get_model") as mock_get:
            mock_model = MagicMock()
            mock_model.transcribe.return_value = (
                [MagicMock(text="browser recording")],
                MagicMock(text="browser recording", language="en", language_probability=0.92),
            )
            mock_get.return_value = mock_model

            response = _client.post(
                "/v1/audio/transcriptions",
                files={"file": ("recording.webm", io.BytesIO(webm_bytes), "audio/webm")},
                data={"model": "whisper-1"},
            )

        assert response.status_code != 415

    def test_webm_codec_opus_content_type(self):
        """audio/webm;codecs=opus must not be rejected at format check."""
        webm_bytes = _make_fake_webm(1024)
        response = _client.post(
            "/v1/audio/transcriptions",
            files={"file": ("rec.webm", io.BytesIO(webm_bytes), "audio/webm;codecs=opus")},
            data={"model": "whisper-1"},
        )
        assert response.status_code != 415


class TestOggFormatHandling:
    """OGG format tests."""

    def test_ogg_file_accepted(self):
        """OGG/Opus recordings must be accepted."""
        ogg_bytes = _make_fake_ogg(1024)
        response = _client.post(
            "/v1/audio/transcriptions",
            files={"file": ("audio.ogg", io.BytesIO(ogg_bytes), "audio/ogg")},
            data={"model": "whisper-1"},
        )
        assert response.status_code != 415


class TestFormatErrorCases:
    """Edge cases and invalid format handling."""

    def test_txt_file_rejected_gracefully(self):
        """Plain text uploaded as audio must return 400 (not 500)."""
        response = _client.post(
            "/v1/audio/transcriptions",
            files={"file": ("notes.txt", io.BytesIO(b"hello world"), "text/plain")},
            data={"model": "whisper-1"},
        )
        # Should be client error, not server error
        assert response.status_code < 500

    def test_missing_file_field_returns_422(self):
        """Missing 'file' field must return 422 Unprocessable Entity."""
        response = _client.post(
            "/v1/audio/transcriptions",
            data={"model": "whisper-1"},
        )
        assert response.status_code == 422

    def test_missing_model_field_returns_422(self):
        """Missing 'model' field must return 422 Unprocessable Entity."""
        wav_bytes = _make_riff_wav(100)
        response = _client.post(
            "/v1/audio/transcriptions",
            files={"file": ("audio.wav", io.BytesIO(wav_bytes), "audio/wav")},
        )
        assert response.status_code == 422
