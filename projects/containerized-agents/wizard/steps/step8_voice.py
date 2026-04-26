"""
Step 8 — Voice setup: test microphone/speaker, download STT/TTS models.
"""
from __future__ import annotations

import logging

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from wizard.config import TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")
logger = logging.getLogger(__name__)

_STT_MODEL = "whisper:large-v3"
_TTS_MODEL = "kokoro:82m"


@router.get("/step/8", response_class=HTMLResponse)
async def get_step8(request: Request) -> HTMLResponse:
    state = get_state()
    return templates.TemplateResponse(
        "step8.html",
        {
            "request": request,
            "state": state,
            "stt_model": _STT_MODEL,
            "tts_model": _TTS_MODEL,
            "current_step": 8,
            "total_steps": TOTAL_STEPS,
            "step_title": "Voice Setup",
        },
    )


@router.post("/api/voice/test-mic")
async def test_microphone() -> JSONResponse:
    """Record a 2-second clip and return whether audio was detected."""
    try:
        import subprocess

        result = subprocess.run(
            ["arecord", "--duration=2", "--format=cd", "/tmp/wizard-mic-test.wav"],
            capture_output=True,
            timeout=5,
        )
        success = result.returncode == 0
        state = get_state()
        state.mic_tested = success
        save_state(state)
        return JSONResponse({"success": success, "message": "Microphone detected audio." if success else result.stderr.decode()})
    except FileNotFoundError:
        return JSONResponse({"success": False, "message": "arecord not found — ALSA utils may not be installed."})
    except Exception as exc:
        logger.exception("Mic test failed")
        return JSONResponse({"success": False, "message": str(exc)})


@router.post("/api/voice/test-speaker")
async def test_speaker() -> JSONResponse:
    """Play a short test tone via aplay."""
    try:
        import subprocess

        result = subprocess.run(
            ["speaker-test", "-t", "sine", "-f", "440", "-l", "1", "-s", "1"],
            capture_output=True,
            timeout=6,
        )
        success = result.returncode == 0
        state = get_state()
        state.speaker_tested = success
        save_state(state)
        return JSONResponse({"success": success, "message": "Speaker test complete." if success else result.stderr.decode()})
    except FileNotFoundError:
        return JSONResponse({"success": False, "message": "speaker-test not found."})
    except Exception as exc:
        logger.exception("Speaker test failed")
        return JSONResponse({"success": False, "message": str(exc)})


@router.post("/api/voice/download-models")
async def download_voice_models() -> JSONResponse:
    """Download STT and TTS models via ollama pull."""
    import asyncio
    import subprocess

    results: dict[str, bool] = {}
    for model_tag, key in [(_STT_MODEL, "stt"), (_TTS_MODEL, "tts")]:
        try:
            proc = await asyncio.create_subprocess_exec(
                "ollama", "pull", model_tag,
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL,
            )
            await proc.wait()
            results[key] = proc.returncode == 0
        except Exception as exc:
            logger.warning("Failed to pull %s: %s", model_tag, exc)
            results[key] = False

    state = get_state()
    state.stt_model_downloaded = results.get("stt", False)
    state.tts_model_downloaded = results.get("tts", False)
    save_state(state)
    return JSONResponse(results)


@router.post("/step/8")
async def post_step8(
    request: Request,
    skip_voice: str = Form(""),
) -> RedirectResponse:
    state = get_state()
    if 8 not in state.completed_steps:
        state.completed_steps.append(8)
    state.current_step = 9
    save_state(state)
    return RedirectResponse("/step/9", status_code=303)
