"""
OpenAI-compatible /v1/audio/transcriptions endpoint.
Drop-in replacement so Open WebUI can point to us instead of OpenAI.

Endpoint: POST /v1/audio/transcriptions
Request:  multipart/form-data — same fields as OpenAI's Audio API.
Response: JSON {"text": "..."} or verbose JSON with segments.

Ref: https://platform.openai.com/docs/api-reference/audio/createTranscription
"""

import logging
from typing import Optional

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import JSONResponse, PlainTextResponse

from .transcriber import transcribe_bytes, SUPPORTED_FORMATS

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/v1/audio")

# Supported response_format values (subset of OpenAI's API).
_SUPPORTED_RESPONSE_FORMATS = frozenset({"json", "text", "verbose_json"})

# Maximum audio file size: 25 MB (same as OpenAI's limit).
_MAX_AUDIO_SIZE_BYTES = 25 * 1024 * 1024


@router.post("/transcriptions")
async def create_transcription(
    file: UploadFile = File(..., description="Audio file to transcribe"),
    model: str = Form(
        default="whisper-1",
        description="Model ID (ignored — we always use large-v3, accepted for compatibility)",
    ),
    language: Optional[str] = Form(
        default=None,
        description="BCP-47 language code (e.g. 'en'). Auto-detected if not provided.",
    ),
    response_format: str = Form(
        default="json",
        description="Response format: json | text | verbose_json",
    ),
    prompt: Optional[str] = Form(
        default=None,
        description="Optional context prompt to guide transcription (passed to Whisper).",
    ),
    temperature: float = Form(
        default=0.0,
        description="Sampling temperature 0.0–1.0 (0.0 = greedy/deterministic).",
    ),
) -> JSONResponse | PlainTextResponse:
    """OpenAI-compatible transcription endpoint.

    Accepts a multipart audio file upload and returns the transcription in
    the requested format. The `model` parameter is accepted for API
    compatibility but is always routed to Whisper large-v3 locally.

    Returns:
        - response_format="json":         {"text": "..."}
        - response_format="text":         Plain text string
        - response_format="verbose_json": {"text": "...", "language": "...",
                                           "duration": ..., "segments": [...]}
    """
    if response_format not in _SUPPORTED_RESPONSE_FORMATS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported response_format '{response_format}'. "
                f"Supported: {', '.join(sorted(_SUPPORTED_RESPONSE_FORMATS))}"
            ),
        )

    # Validate file extension.
    filename = file.filename or ""
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else "wav"
    if ext not in SUPPORTED_FORMATS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported audio format '{ext}'. "
                f"Supported: {', '.join(sorted(SUPPORTED_FORMATS))}"
            ),
        )

    # Read the uploaded file into memory.
    audio_bytes = await file.read()

    if len(audio_bytes) > _MAX_AUDIO_SIZE_BYTES:
        raise HTTPException(
            status_code=413,
            detail=(
                f"Audio file too large: {len(audio_bytes):,} bytes. "
                f"Maximum: {_MAX_AUDIO_SIZE_BYTES:,} bytes (25 MB)."
            ),
        )

    if len(audio_bytes) == 0:
        raise HTTPException(status_code=400, detail="Uploaded audio file is empty.")

    # Transcribe.
    try:
        result = await transcribe_bytes(audio_bytes, format=ext)
    except Exception as exc:
        logger.exception("Transcription failed for file '%s': %s", filename, exc)
        raise HTTPException(status_code=500, detail=f"Transcription failed: {exc}")

    # Format response.
    if response_format == "text":
        return PlainTextResponse(content=result.text)

    if response_format == "verbose_json":
        return JSONResponse(
            content={
                "task": "transcribe",
                "language": result.language,
                "duration": round(result.duration_seconds, 3),
                "text": result.text,
                "segments": result.segments,
            }
        )

    # Default: "json"
    return JSONResponse(content={"text": result.text})
