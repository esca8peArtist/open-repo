"""
Text-to-speech using Kokoro-82M (Apache 2.0 license).
Runs fully offline. ~0.5-1s synthesis latency.

Kokoro-82M is a lightweight 82-million-parameter TTS model that produces
high-quality natural speech. It supports multiple voices covering American
and British English accents, both male and female.

The model is loaded once (singleton) on first use. Long texts are split into
sentences and synthesised sequentially, then the WAV buffers are concatenated,
which reduces perceived latency for the first sentence.
"""

import asyncio
import io
import logging
import re
from dataclasses import dataclass
from typing import List, Optional

import numpy as np
import soundfile as sf

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SAMPLE_RATE = 24000         # Kokoro output sample rate in Hz
DEFAULT_VOICE = "af_heart"

# All available Kokoro-82M voices.
# Prefix key: af = American Female, am = American Male,
#             bf = British Female, bm = British Male
AVAILABLE_VOICES = [
    "af_heart",
    "af_bella",
    "af_sarah",
    "am_adam",
    "am_michael",
    "bf_emma",
    "bf_isabella",
    "bm_george",
    "bm_lewis",
]

_VOICE_METADATA = {
    "af_heart":    {"language": "en-US", "gender": "female", "accent": "American"},
    "af_bella":    {"language": "en-US", "gender": "female", "accent": "American"},
    "af_sarah":    {"language": "en-US", "gender": "female", "accent": "American"},
    "am_adam":     {"language": "en-US", "gender": "male",   "accent": "American"},
    "am_michael":  {"language": "en-US", "gender": "male",   "accent": "American"},
    "bf_emma":     {"language": "en-GB", "gender": "female", "accent": "British"},
    "bf_isabella": {"language": "en-GB", "gender": "female", "accent": "British"},
    "bm_george":   {"language": "en-GB", "gender": "male",   "accent": "British"},
    "bm_lewis":    {"language": "en-GB", "gender": "male",   "accent": "British"},
}

# Maximum characters per synthesis chunk. Kokoro degrades on very long inputs;
# sentence splitting handles this transparently.
_MAX_CHUNK_CHARS = 300


# ---------------------------------------------------------------------------
# Result type
# ---------------------------------------------------------------------------


@dataclass
class SynthesisResult:
    audio_bytes: bytes          # WAV format, 24kHz, mono, 16-bit PCM
    duration_seconds: float
    voice: str
    sample_rate: int


# ---------------------------------------------------------------------------
# Kokoro model singleton
# ---------------------------------------------------------------------------

_kokoro_pipeline = None
_kokoro_lock = asyncio.Lock()


async def _ensure_model_loaded():
    """Async-safe lazy load of the Kokoro pipeline (singleton)."""
    global _kokoro_pipeline
    if _kokoro_pipeline is not None:
        return _kokoro_pipeline

    async with _kokoro_lock:
        if _kokoro_pipeline is not None:
            return _kokoro_pipeline

        def _load():
            # kokoro package exposes a KPipeline class for inference.
            # Import here to defer the heavy import until first use.
            from kokoro import KPipeline  # type: ignore[import]
            logger.info("Loading Kokoro-82M TTS pipeline...")
            pipeline = KPipeline(lang_code="a")  # "a" = English
            logger.info("Kokoro-82M pipeline loaded successfully")
            return pipeline

        loop = asyncio.get_running_loop()
        _kokoro_pipeline = await loop.run_in_executor(None, _load)

    return _kokoro_pipeline


# ---------------------------------------------------------------------------
# Sentence splitting
# ---------------------------------------------------------------------------


def _split_into_sentences(text: str) -> List[str]:
    """Split text into sentences suitable for chunked TTS synthesis.

    Splits on sentence-ending punctuation (., !, ?) followed by whitespace.
    Long sentences that exceed _MAX_CHUNK_CHARS are split further at commas
    or clause boundaries.

    Args:
        text: Input text to split.

    Returns:
        List of sentence strings. Each is at most _MAX_CHUNK_CHARS characters.
    """
    # Basic sentence split on period/exclamation/question followed by space or end.
    raw_sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    result: List[str] = []
    for sentence in raw_sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        if len(sentence) <= _MAX_CHUNK_CHARS:
            result.append(sentence)
        else:
            # Long sentence: split at commas or semicolons.
            sub_parts = re.split(r"[,;]\s*", sentence)
            current = ""
            for part in sub_parts:
                if current and len(current) + len(part) + 2 > _MAX_CHUNK_CHARS:
                    if current:
                        result.append(current.strip())
                    current = part
                else:
                    current = f"{current}, {part}" if current else part
            if current.strip():
                result.append(current.strip())

    return result or [text[:_MAX_CHUNK_CHARS]]


# ---------------------------------------------------------------------------
# Audio helpers
# ---------------------------------------------------------------------------


def _numpy_to_wav_bytes(audio_array: np.ndarray, sample_rate: int) -> bytes:
    """Convert a numpy float32 audio array to WAV bytes (16-bit PCM).

    Args:
        audio_array: 1-D float32 numpy array with values in [-1, 1].
        sample_rate: Sample rate in Hz.

    Returns:
        WAV-encoded bytes.
    """
    # Clip to [-1, 1] to prevent integer overflow on conversion.
    clipped = np.clip(audio_array, -1.0, 1.0)

    buf = io.BytesIO()
    sf.write(buf, clipped, samplerate=sample_rate, format="WAV", subtype="PCM_16")
    buf.seek(0)
    return buf.read()


# ---------------------------------------------------------------------------
# Public synthesis API
# ---------------------------------------------------------------------------


async def synthesize(
    text: str,
    voice: str = DEFAULT_VOICE,
    speed: float = 1.0,
) -> SynthesisResult:
    """Synthesize text to speech.

    Returns WAV audio bytes at 24kHz mono. For texts longer than
    _MAX_CHUNK_CHARS, splits into sentences and synthesises each chunk
    independently, then concatenates the audio arrays before encoding.

    Args:
        text:  Input text to synthesise (UTF-8).
        voice: Kokoro voice ID. Must be one of AVAILABLE_VOICES.
               Defaults to "af_heart".
        speed: Speech rate multiplier. 1.0 = normal, 0.75 = slower, 1.25 = faster.
               Clipped to [0.5, 2.0].

    Returns:
        SynthesisResult with WAV bytes, duration, voice, and sample rate.

    Raises:
        ValueError: If the voice is not in AVAILABLE_VOICES.
    """
    if voice not in AVAILABLE_VOICES:
        raise ValueError(
            f"Unknown voice '{voice}'. Available: {', '.join(AVAILABLE_VOICES)}"
        )

    speed = max(0.5, min(2.0, float(speed)))
    text = text.strip()

    if not text:
        # Return minimal silent WAV (44-byte header + 0 samples).
        silent = np.zeros(0, dtype=np.float32)
        wav_bytes = _numpy_to_wav_bytes(silent, SAMPLE_RATE)
        return SynthesisResult(
            audio_bytes=wav_bytes,
            duration_seconds=0.0,
            voice=voice,
            sample_rate=SAMPLE_RATE,
        )

    pipeline = await _ensure_model_loaded()
    sentences = _split_into_sentences(text)

    all_audio_chunks: List[np.ndarray] = []

    def _synthesise_sentence(sentence: str) -> np.ndarray:
        """Run Kokoro inference synchronously (CPU-bound)."""
        # KPipeline.__call__ yields (graphemes, phonemes, audio_array) tuples.
        # We collect all audio chunks and concatenate.
        audio_parts: List[np.ndarray] = []
        for _, _, audio in pipeline(sentence, voice=voice, speed=speed):
            if audio is not None and len(audio) > 0:
                audio_parts.append(audio)
        if audio_parts:
            return np.concatenate(audio_parts)
        return np.zeros(0, dtype=np.float32)

    loop = asyncio.get_running_loop()

    # Process sentences sequentially in thread pool (Kokoro is not thread-safe
    # with concurrent calls on the same pipeline instance).
    for sentence in sentences:
        chunk = await loop.run_in_executor(None, _synthesise_sentence, sentence)
        all_audio_chunks.append(chunk)

    # Concatenate all audio chunks.
    full_audio = np.concatenate(all_audio_chunks) if all_audio_chunks else np.zeros(0, dtype=np.float32)
    duration_seconds = float(len(full_audio)) / SAMPLE_RATE

    wav_bytes = _numpy_to_wav_bytes(full_audio, SAMPLE_RATE)

    logger.info(
        "TTS synthesis: %d chars → %.2fs audio (voice=%s, speed=%.2f)",
        len(text),
        duration_seconds,
        voice,
        speed,
    )

    return SynthesisResult(
        audio_bytes=wav_bytes,
        duration_seconds=duration_seconds,
        voice=voice,
        sample_rate=SAMPLE_RATE,
    )


async def list_voices() -> list[dict]:
    """List available voices with metadata.

    Returns:
        List of dicts with voice_id, language, gender, and accent fields.
    """
    return [
        {
            "voice_id": voice_id,
            **_VOICE_METADATA.get(voice_id, {}),
        }
        for voice_id in AVAILABLE_VOICES
    ]
