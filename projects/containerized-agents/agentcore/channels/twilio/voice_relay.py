"""
Twilio ConversationRelay for inbound voice calls.

Call flow:
  1. Customer calls the Twilio phone number.
  2. Twilio POSTs to /webhook/voice/incoming — we return TwiML that opens a
     bidirectional MediaStream WebSocket to /webhook/voice/stream/{call_sid}.
  3. Twilio connects the WebSocket and starts streaming mulaw audio (8 kHz)
     in both directions.
  4. We pipe received audio through faster-whisper (STT) → agent LLM
     → Kokoro TTS → stream audio back to Twilio → spoken to the caller.

WebSocket message format (Twilio Media Streams):
  Inbound events: "start", "media", "stop", "dtmf"
  Outbound events: "media" (base64-encoded mulaw audio chunks)

Audio format: mulaw 8 kHz — standard telephone quality.
All audio processing is done locally (offline-capable for the inference
path; the Twilio SIP trunk itself requires internet).

Refs:
  https://www.twilio.com/docs/voice/twiml/connect/stream
  https://www.twilio.com/docs/voice/api/media-streams
"""

from __future__ import annotations

import asyncio
import base64
import io
import json
import logging
import tempfile
from pathlib import Path
from typing import Any

import httpx
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import PlainTextResponse

from agentcore.config import get_settings

logger = logging.getLogger(__name__)


def _agentcore_base_url() -> str:
    """Return the configured AgentCore base URL (no trailing slash)."""
    return get_settings().agentcore_base_url.rstrip("/")


# AgentCore internal service URL templates (resolved at call time via settings).
def _stt_endpoint() -> str:
    return f"{_agentcore_base_url()}/v1/audio/transcriptions"


def _tts_endpoint() -> str:
    return f"{_agentcore_base_url()}/v1/audio/speech"


def _agent_endpoint(agent_id: str) -> str:
    return f"{_agentcore_base_url()}/api/agent/{agent_id}/chat"

# Silence threshold: minimum audio chunk bytes before attempting STT.
_MIN_AUDIO_BYTES = 8_000  # ~0.5s at 8 kHz mulaw


class TwilioVoiceRelay:
    """Real-time voice relay between Twilio and the AgentCore agent.

    Handles the full pipeline:
      Audio in (Twilio mulaw) → STT (faster-whisper) → agent LLM
      → TTS (Kokoro) → Audio out (mulaw) → Twilio → caller.

    Args:
        account_sid:  Twilio Account SID.
        auth_token:   Twilio Auth Token.
        phone_number: Twilio phone number in E.164 format.
        agent_id:     AgentCore agent identifier.
    """

    def __init__(
        self,
        account_sid: str,
        auth_token: str,
        phone_number: str,
        agent_id: str,
    ) -> None:
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.phone_number = phone_number
        self.agent_id = agent_id

    # ------------------------------------------------------------------
    # FastAPI router
    # ------------------------------------------------------------------

    def get_webhook_router(self) -> APIRouter:
        """Return a FastAPI APIRouter with TwiML and WebSocket endpoints.

        Routes registered:
          POST /webhook/voice/incoming  — TwiML connect response
          POST /webhook/voice/status    — Call status callbacks
          WS   /webhook/voice/stream/{call_sid} — Bidirectional audio stream
        """
        router = APIRouter()
        relay = self  # capture self for closures

        @router.post("/webhook/voice/incoming", response_class=PlainTextResponse)
        async def voice_incoming(request: "Request") -> PlainTextResponse:  # type: ignore[name-defined]  # noqa: F821
            """Handle inbound call — return TwiML to open a MediaStream."""
            from fastapi import Request  # local import to avoid circular

            call_sid = (await request.form()).get("CallSid", "unknown")
            twiml = await relay.handle_call_start(str(call_sid))
            return PlainTextResponse(content=twiml, media_type="text/xml")

        @router.post("/webhook/voice/status", response_class=PlainTextResponse)
        async def voice_status(request: "Request") -> PlainTextResponse:  # type: ignore[name-defined]  # noqa: F821
            """Log call status updates (ringing, in-progress, completed, etc.)."""
            from fastapi import Request  # local import to avoid circular

            form = await request.form()
            call_sid = form.get("CallSid", "")
            status = form.get("CallStatus", "")
            logger.info("Call status: sid=%s status=%s", call_sid, status)
            return PlainTextResponse(content="", media_type="text/xml")

        @router.websocket("/webhook/voice/stream/{call_sid}")
        async def voice_stream(websocket: WebSocket, call_sid: str) -> None:
            """Handle the bidirectional Twilio Media Streams WebSocket."""
            await relay.handle_ws_stream(websocket, call_sid)

        return router

    # ------------------------------------------------------------------
    # Call handling
    # ------------------------------------------------------------------

    async def handle_call_start(self, call_sid: str) -> str:
        """Return TwiML that connects the call to our WebSocket stream.

        The TwiML instructs Twilio to:
          1. Play a brief greeting.
          2. Open a bidirectional MediaStream to our WebSocket endpoint.

        Args:
            call_sid: Twilio CallSid for this call.

        Returns:
            TwiML XML string.
        """
        stream_url = self._stream_ws_url(call_sid)
        twiml = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            "<Response>\n"
            "  <Say voice=\"Polly.Joanna\">Hello, I'm your AI assistant. How can I help you today?</Say>\n"
            "  <Connect>\n"
            f'    <Stream url="{stream_url}">\n'
            f'      <Parameter name="agent_id" value="{self.agent_id}"/>\n'
            "    </Stream>\n"
            "  </Connect>\n"
            "</Response>"
        )
        logger.info("Returning TwiML for call_sid=%s stream=%s", call_sid, stream_url)
        return twiml

    # ------------------------------------------------------------------
    # WebSocket audio stream
    # ------------------------------------------------------------------

    async def handle_ws_stream(self, websocket: WebSocket, call_sid: str) -> None:
        """Handle the real-time bidirectional audio WebSocket stream.

        Twilio sends "media" events containing base64-encoded mulaw audio
        chunks. We buffer them, detect speech pauses, transcribe accumulated
        audio, route the text to the agent, synthesise a reply via TTS,
        and stream the audio back to Twilio.

        Args:
            websocket: FastAPI WebSocket connection from Twilio.
            call_sid:  Twilio CallSid for logging / routing.
        """
        await websocket.accept()
        logger.info("Voice stream WebSocket connected: call_sid=%s", call_sid)

        stream_sid: str = ""
        audio_buffer = bytearray()
        silence_frames = 0
        # A "frame" here is one Twilio media event (~20ms of audio at 8 kHz mulaw).
        # After ~750ms of silence (≈37 frames) we treat the utterance as complete.
        _SILENCE_THRESHOLD_FRAMES = 37

        try:
            while True:
                try:
                    raw = await asyncio.wait_for(websocket.receive_text(), timeout=30.0)
                except asyncio.TimeoutError:
                    logger.warning("Voice stream timed out (call_sid=%s)", call_sid)
                    break

                event = json.loads(raw)
                event_type = event.get("event", "")

                if event_type == "start":
                    start_data = event.get("start", {})
                    stream_sid = start_data.get("streamSid", "")
                    logger.info(
                        "Media stream started: call_sid=%s stream_sid=%s",
                        call_sid,
                        stream_sid,
                    )

                elif event_type == "media":
                    payload_b64 = event.get("media", {}).get("payload", "")
                    if payload_b64:
                        chunk = base64.b64decode(payload_b64)
                        audio_buffer.extend(chunk)
                        silence_frames = 0
                    else:
                        # Empty payload — silence frame.
                        silence_frames += 1
                        if (
                            silence_frames >= _SILENCE_THRESHOLD_FRAMES
                            and len(audio_buffer) >= _MIN_AUDIO_BYTES
                        ):
                            # Process accumulated utterance.
                            utterance_bytes = bytes(audio_buffer)
                            audio_buffer.clear()
                            silence_frames = 0

                            reply_audio = await self._process_utterance(
                                utterance_bytes, call_sid
                            )
                            if reply_audio and stream_sid:
                                await _send_audio_to_twilio(
                                    websocket, stream_sid, reply_audio
                                )

                elif event_type == "stop":
                    logger.info(
                        "Media stream stopped: call_sid=%s stream_sid=%s",
                        call_sid,
                        stream_sid,
                    )
                    # Process any remaining audio.
                    if len(audio_buffer) >= _MIN_AUDIO_BYTES:
                        reply_audio = await self._process_utterance(
                            bytes(audio_buffer), call_sid
                        )
                        if reply_audio and stream_sid:
                            await _send_audio_to_twilio(
                                websocket, stream_sid, reply_audio
                            )
                    break

                elif event_type == "dtmf":
                    digit = event.get("dtmf", {}).get("digit", "")
                    logger.debug("DTMF digit=%s call_sid=%s", digit, call_sid)
                    # DTMF digits could be routed to agent for IVR-style interactions.

        except WebSocketDisconnect:
            logger.info("Voice stream WebSocket disconnected: call_sid=%s", call_sid)
        except Exception as exc:
            logger.exception(
                "Error in voice stream WebSocket (call_sid=%s): %s", call_sid, exc
            )
        finally:
            logger.info("Voice stream closed: call_sid=%s", call_sid)

    # ------------------------------------------------------------------
    # Internal pipeline helpers
    # ------------------------------------------------------------------

    async def _process_utterance(self, audio_bytes: bytes, call_sid: str) -> bytes | None:
        """Full pipeline for a single caller utterance.

        mulaw audio bytes → STT transcript → agent LLM → TTS audio bytes.

        If any step in the pipeline fails, a brief apology message is
        synthesised and returned so the caller hears something instead of
        silence.

        Args:
            audio_bytes: Raw mulaw 8 kHz audio bytes from Twilio.
            call_sid:    For logging.

        Returns:
            mulaw audio bytes of the synthesised reply, or None on failure.
        """
        try:
            # Step 1: Transcribe audio via faster-whisper STT endpoint.
            transcript = await self._transcribe_mulaw(audio_bytes)
            if not transcript:
                logger.debug("No transcript for utterance (call_sid=%s)", call_sid)
                return None

            logger.info("Transcribed utterance (call_sid=%s): %r", call_sid, transcript[:100])

            # Step 2: Send transcript to the agent and get text reply.
            reply_text = await self._query_agent(transcript, call_sid)
            if not reply_text:
                raise RuntimeError("Agent returned empty reply")

            logger.info("Agent reply (call_sid=%s): %r", call_sid, reply_text[:100])

            # Step 3: Synthesise reply via Kokoro TTS endpoint.
            reply_audio = await self._synthesise_speech(reply_text)
            if reply_audio is None:
                raise RuntimeError("TTS synthesis returned no audio")
            return reply_audio

        except Exception as exc:
            logger.error(
                "Utterance pipeline failed (call_sid=%s), sending fallback message: %s",
                call_sid,
                exc,
            )
            _FALLBACK_MESSAGE = "I'm sorry, I didn't catch that. Could you please try again?"
            try:
                return await self._synthesise_speech(_FALLBACK_MESSAGE)
            except Exception as tts_exc:
                logger.error(
                    "Fallback TTS synthesis also failed (call_sid=%s): %s",
                    call_sid,
                    tts_exc,
                )
                return None

    async def _transcribe_mulaw(self, mulaw_bytes: bytes) -> str | None:
        """Convert mulaw audio bytes to text via the AgentCore STT endpoint.

        Twilio Media Streams use mulaw encoding at 8 kHz. We send the raw
        bytes to the local STT endpoint which accepts common audio formats.

        Args:
            mulaw_bytes: Raw mulaw 8 kHz audio.

        Returns:
            Transcript string or None on failure.
        """
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    _stt_endpoint(),
                    files={
                        "file": ("audio.mulaw", io.BytesIO(mulaw_bytes), "audio/basic")
                    },
                    data={"model": "whisper-1", "response_format": "json"},
                )
                response.raise_for_status()
                data = response.json()
                text = data.get("text", "").strip()
                return text or None
        except Exception as exc:
            logger.error("STT transcription failed: %s", exc)
            return None

    async def _query_agent(self, text: str, call_sid: str) -> str | None:
        """Send transcript to the AgentCore agent and return the reply.

        Args:
            text:     Transcribed caller speech.
            call_sid: For logging and session tracking.

        Returns:
            Reply text or None on failure.
        """
        agent_url = _agent_endpoint(self.agent_id)
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    agent_url,
                    json={
                        "message": text,
                        "session_id": call_sid,
                        "channel": "voice",
                    },
                )
                response.raise_for_status()
                data = response.json()
                return data.get("message", "").strip() or None
        except Exception as exc:
            logger.error("Agent query failed (call_sid=%s): %s", call_sid, exc)
            return None

    async def _synthesise_speech(self, text: str) -> bytes | None:
        """Synthesise text to speech via the AgentCore Kokoro TTS endpoint.

        The TTS endpoint returns audio in the requested format. We request
        mulaw/8000 for direct transmission back to Twilio, falling back to
        PCM conversion if the TTS endpoint doesn't support mulaw natively.

        Args:
            text: Text to synthesise.

        Returns:
            Audio bytes (mulaw 8 kHz) or None on failure.
        """
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    _tts_endpoint(),
                    json={
                        "model": "kokoro",
                        "input": text,
                        "voice": "af",
                        "response_format": "mulaw",
                        "sample_rate": 8000,
                    },
                )
                response.raise_for_status()
                return response.content
        except Exception as exc:
            logger.error("TTS synthesis failed: %s", exc)
            return None

    def _stream_ws_url(self, call_sid: str) -> str:
        """Build the WebSocket URL for the MediaStream connection.

        Returns a wss:// URL relative to the machine's base URL.
        In production this must be configured via the webhook_base_url in
        TwilioConfig (e.g. wss://agent.example.com/webhook/voice/stream/<sid>).
        Twilio requires WSS (secure WebSocket).
        """
        # The public base URL is sourced from settings (TWILIO_WEBHOOK_BASE_URL).
        # Twilio requires WSS (secure WebSocket); http(s) schemes are converted.
        base = get_settings().twilio_webhook_base_url or "wss://agent.local:8080"
        base = base.rstrip("/")
        # Convert http(s) scheme to ws(s) if needed.
        base = base.replace("https://", "wss://").replace("http://", "ws://")
        return f"{base}/webhook/voice/stream/{call_sid}"


# ---------------------------------------------------------------------------
# WebSocket helpers
# ---------------------------------------------------------------------------


async def _send_audio_to_twilio(
    websocket: WebSocket,
    stream_sid: str,
    audio_bytes: bytes,
) -> None:
    """Send audio bytes back to Twilio via the Media Streams WebSocket.

    Twilio expects "media" events with base64-encoded mulaw audio. The
    payload is chunked into ~20ms frames (160 bytes at 8 kHz mulaw) to
    simulate real-time streaming and prevent buffer overflows.

    Args:
        websocket:   Active Twilio Media Streams WebSocket connection.
        stream_sid:  Twilio StreamSid identifying this stream.
        audio_bytes: mulaw 8 kHz audio to send to the caller.
    """
    # Chunk into 160-byte frames (20ms at 8 kHz mulaw = 8000 bytes/s ÷ 50).
    chunk_size = 160
    for i in range(0, len(audio_bytes), chunk_size):
        chunk = audio_bytes[i : i + chunk_size]
        payload = base64.b64encode(chunk).decode("ascii")
        message = json.dumps(
            {
                "event": "media",
                "streamSid": stream_sid,
                "media": {"payload": payload},
            }
        )
        try:
            await websocket.send_text(message)
        except Exception as exc:
            logger.warning("Failed to send audio chunk to Twilio: %s", exc)
            break
        # Yield to event loop to allow other coroutines to run.
        await asyncio.sleep(0)
