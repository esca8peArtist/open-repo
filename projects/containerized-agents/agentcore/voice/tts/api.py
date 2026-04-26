"""
OpenAI-compatible /v1/audio/speech endpoint.
Drop-in so Open WebUI can use our Kokoro TTS.

Endpoint: POST /v1/audio/speech
Request:  JSON body — same fields as OpenAI's Audio Speech API.
Response: Binary audio (WAV or MP3 depending on response_format).

Ref: https://platform.openai.com/docs/api-reference/audio/createSpeech
"""

import io
import logging
from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field, field_validator

from .synthesizer import synthesize, list_voices as _list_voices, AVAILABLE_VOICES

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/v1/audio")

# Supported output formats.
_SUPPORTED_FORMATS = frozenset({"wav", "mp3", "opus", "aac", "flac", "pcm"})

# MIME types for supported audio formats.
_MIME_TYPES: dict[str, str] = {
    "wav":  "audio/wav",
    "mp3":  "audio/mpeg",
    "opus": "audio/ogg; codecs=opus",
    "aac":  "audio/aac",
    "flac": "audio/flac",
    "pcm":  "audio/pcm",
}


# ---------------------------------------------------------------------------
# Request model
# ---------------------------------------------------------------------------


class SpeechRequest(BaseModel):
    model: str = Field(
        default="tts-1",
        description="TTS model ID (ignored — we always use Kokoro-82M, accepted for compatibility).",
    )
    input: str = Field(
        ...,
        description="Text to synthesise. Maximum 4096 characters.",
        max_length=4096,
    )
    voice: str = Field(
        default="af_heart",
        description=f"Voice ID. One of: {', '.join(AVAILABLE_VOICES)}",
    )
    response_format: str = Field(
        default="wav",
        description="Audio format: wav | mp3 | opus | aac | flac | pcm. Default: wav.",
    )
    speed: float = Field(
        default=1.0,
        ge=0.25,
        le=4.0,
        description="Speech rate multiplier. 1.0 = normal. Clipped to [0.5, 2.0] internally.",
    )

    @field_validator("voice")
    @classmethod
    def validate_voice(cls, v: str) -> str:
        if v not in AVAILABLE_VOICES:
            raise ValueError(
                f"Unknown voice '{v}'. Available voices: {', '.join(AVAILABLE_VOICES)}"
            )
        return v

    @field_validator("response_format")
    @classmethod
    def validate_format(cls, v: str) -> str:
        if v not in _SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported response_format '{v}'. "
                f"Supported: {', '.join(sorted(_SUPPORTED_FORMATS))}"
            )
        return v


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@router.post("/speech")
async def create_speech(request: SpeechRequest) -> Response:
    """OpenAI-compatible TTS endpoint.

    Synthesises the input text using Kokoro-82M and returns the audio
    as a binary response. The Content-Type header matches the requested format.

    Note: Currently only WAV output is natively produced by Kokoro. Requests
    for mp3/opus/aac/flac will fall back to WAV with a note header unless a
    conversion library (e.g. pydub + ffmpeg) is available in the container.
    PCM returns raw float32 samples at 24kHz.
    """
    if not request.input.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    try:
        result = await synthesize(
            text=request.input,
            voice=request.voice,
            speed=request.speed,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:
        logger.exception("TTS synthesis failed: %s", exc)
        raise HTTPException(status_code=500, detail=f"Synthesis failed: {exc}")

    # Determine output audio data and content type.
    audio_data = result.audio_bytes
    fmt = request.response_format

    if fmt == "pcm":
        # Return raw 16-bit signed PCM samples (strip WAV header).
        # WAV header is 44 bytes for standard PCM WAV.
        audio_data = result.audio_bytes[44:]
        content_type = _MIME_TYPES["pcm"]
    elif fmt != "wav":
        # Attempt format conversion via pydub + ffmpeg if available.
        try:
            from pydub import AudioSegment  # type: ignore[import]
            import io as _io

            wav_buf = _io.BytesIO(result.audio_bytes)
            segment = AudioSegment.from_wav(wav_buf)
            out_buf = _io.BytesIO()
            segment.export(out_buf, format=fmt)
            audio_data = out_buf.getvalue()
            content_type = _MIME_TYPES.get(fmt, "application/octet-stream")
        except ImportError:
            # pydub not available — return WAV with informational header.
            logger.warning(
                "pydub not available; returning WAV instead of %s. "
                "Install pydub + ffmpeg for format conversion.",
                fmt,
            )
            audio_data = result.audio_bytes
            content_type = _MIME_TYPES["wav"]
    else:
        content_type = _MIME_TYPES["wav"]

    return Response(
        content=audio_data,
        media_type=content_type,
        headers={
            "X-Synthesis-Duration": str(round(result.duration_seconds, 3)),
            "X-Voice": result.voice,
            "X-Sample-Rate": str(result.sample_rate),
        },
    )


@router.get("/voices")
async def list_voices_endpoint():
    """List available Kokoro voices.

    Returns a list of voice objects with metadata (voice_id, language,
    gender, accent). This endpoint is an extension beyond the standard
    OpenAI API and is used by the AgentCore admin UI.
    """
    voices = await _list_voices()
    return {"voices": voices}
