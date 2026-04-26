"""
Speech-to-text using faster-whisper (Whisper large-v3, MIT license).
Runs fully offline. ~1-2s transcription latency.
Supports 90+ languages.

faster-whisper is a reimplementation of OpenAI's Whisper model using
CTranslate2, which enables efficient CPU inference with int8 quantization.
Model is loaded once (singleton) on first use to avoid repeated cold-starts.
"""

import asyncio
import io
import logging
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from faster_whisper import WhisperModel

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODEL_SIZE = "large-v3"
COMPUTE_TYPE = "int8"       # CPU-optimised; change to "float16" if GPU available
DEVICE = "cpu"              # "cuda" if NVIDIA GPU is present and CTranslate2-GPU installed
CPU_THREADS = 4             # Number of threads to use for inference

# Supported audio formats (via soundfile / ffmpeg fallback in faster-whisper).
SUPPORTED_FORMATS = frozenset({"wav", "mp3", "m4a", "ogg", "flac", "webm"})


# ---------------------------------------------------------------------------
# Result type
# ---------------------------------------------------------------------------


@dataclass
class TranscriptionResult:
    text: str
    language: str
    language_probability: float
    duration_seconds: float
    segments: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# Model singleton
# ---------------------------------------------------------------------------

_model: Optional[WhisperModel] = None
_model_lock = asyncio.Lock()


def get_model() -> WhisperModel:
    """Lazy-load the Whisper model (singleton).

    Not async — loading is blocking but happens only once. Callers that need
    async loading should use _ensure_model_loaded() instead.

    Returns:
        The loaded WhisperModel instance.
    """
    global _model
    if _model is None:
        logger.info(
            "Loading faster-whisper model '%s' (compute_type=%s, device=%s)...",
            MODEL_SIZE,
            COMPUTE_TYPE,
            DEVICE,
        )
        _model = WhisperModel(
            MODEL_SIZE,
            device=DEVICE,
            compute_type=COMPUTE_TYPE,
            cpu_threads=CPU_THREADS,
            # Download to the default cache dir (~/.cache/huggingface/).
            # In the container, this is /app/data/whisper-models/ via a volume mount.
        )
        logger.info("faster-whisper model loaded successfully")
    return _model


async def _ensure_model_loaded() -> WhisperModel:
    """Async-safe model loading. Uses asyncio.Lock to prevent concurrent loads."""
    global _model
    if _model is not None:
        return _model
    async with _model_lock:
        if _model is None:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, get_model)
    return _model  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Transcription
# ---------------------------------------------------------------------------


async def transcribe(
    audio_path: Path, language: Optional[str] = None
) -> TranscriptionResult:
    """Transcribe audio file to text.

    Supports: wav, mp3, m4a, ogg, flac, webm.
    Auto-detects language if not specified.

    faster-whisper's transcribe() is CPU-bound; it is offloaded to a thread
    executor to avoid blocking the asyncio event loop.

    Args:
        audio_path: Path to an audio file in a supported format.
        language:   BCP-47 language code (e.g. "en", "es", "fr"). If None,
                    faster-whisper auto-detects the language from the first
                    30 seconds of audio.

    Returns:
        TranscriptionResult with full transcript, detected language,
        language confidence, duration, and raw segment list.

    Raises:
        FileNotFoundError: If audio_path does not exist.
        ValueError: If the file extension is not in SUPPORTED_FORMATS.
    """
    audio_path = Path(audio_path)

    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    ext = audio_path.suffix.lstrip(".").lower()
    if ext not in SUPPORTED_FORMATS:
        raise ValueError(
            f"Unsupported audio format: '{ext}'. "
            f"Supported: {', '.join(sorted(SUPPORTED_FORMATS))}"
        )

    model = await _ensure_model_loaded()

    def _run_transcription():
        segments_iter, info = model.transcribe(
            str(audio_path),
            language=language,
            beam_size=5,
            best_of=5,
            temperature=0.0,       # greedy decoding — most deterministic
            vad_filter=True,       # skip silent regions (Voice Activity Detection)
            vad_parameters={
                "min_silence_duration_ms": 500,
            },
        )
        segments = list(segments_iter)  # materialise the generator
        return segments, info

    loop = asyncio.get_running_loop()
    segments, info = await loop.run_in_executor(None, _run_transcription)

    full_text = " ".join(seg.text.strip() for seg in segments if seg.text.strip())

    result = TranscriptionResult(
        text=full_text.strip(),
        language=info.language,
        language_probability=info.language_probability,
        duration_seconds=info.duration,
        segments=[
            {
                "start": seg.start,
                "end": seg.end,
                "text": seg.text.strip(),
                "no_speech_prob": seg.no_speech_prob,
            }
            for seg in segments
        ],
    )

    logger.info(
        "Transcribed '%s': %.1fs audio → %d chars (lang=%s, conf=%.2f)",
        audio_path.name,
        info.duration,
        len(full_text),
        info.language,
        info.language_probability,
    )
    return result


async def transcribe_bytes(
    audio_bytes: bytes, format: str = "wav"
) -> TranscriptionResult:
    """Transcribe raw audio bytes.

    Saves the bytes to a temporary file, transcribes, then cleans up.

    Args:
        audio_bytes: Raw audio data.
        format:      File extension hint for the audio format (default "wav").

    Returns:
        TranscriptionResult from the transcribed audio.
    """
    fmt = format.lstrip(".").lower()
    if fmt not in SUPPORTED_FORMATS:
        raise ValueError(
            f"Unsupported audio format: '{fmt}'. "
            f"Supported: {', '.join(sorted(SUPPORTED_FORMATS))}"
        )

    # Write to a named temp file; faster-whisper needs a file path.
    with tempfile.NamedTemporaryFile(
        suffix=f".{fmt}", delete=False
    ) as tmp:
        tmp.write(audio_bytes)
        tmp_path = Path(tmp.name)

    try:
        return await transcribe(tmp_path)
    finally:
        try:
            tmp_path.unlink(missing_ok=True)
        except Exception:
            pass
