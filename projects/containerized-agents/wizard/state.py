"""
Wizard session state — persisted between requests.
Stored at /app/data/wizard-state.json inside the wizard-data volume
(overridable via WIZARD_STATE_FILE). The file is created with 0o600
permissions so only the wizard process can read it.
"""
from __future__ import annotations

import json
import logging
import os
from pathlib import Path

from pydantic import BaseModel

from wizard.config import STATE_FILE

logger = logging.getLogger(__name__)


class WizardState(BaseModel):
    current_step: int = 1
    completed_steps: list[int] = []

    # Step 1 — Welcome
    language: str = "en"
    agent_name: str = ""

    # Step 2 — Profile selection
    selected_profile: int | None = None

    # Step 3 — Multi-agent setup
    additional_profiles: list[int] = []
    resource_allocation: dict = {}

    # Step 4 — Communication channels
    telegram_token: str = ""
    telegram_enabled: bool = False
    telegram_bot_username: str = ""
    twilio_account_sid: str = ""
    twilio_auth_token: str = ""
    twilio_phone: str = ""
    twilio_enabled: bool = False
    whatsapp_enabled: bool = False
    voice_calls_enabled: bool = False

    # Step 5 — Knowledge base
    uploaded_documents: list[str] = []
    rag_urls: list[str] = []

    # Step 6 — Integrations
    caldav_url: str = ""
    caldav_username: str = ""
    caldav_password: str = ""
    smtp_host: str = ""
    smtp_port: int = 587
    email_user: str = ""
    email_password: str = ""

    # Step 7 — Model pull
    models_to_pull: list[str] = []
    models_pulled: list[str] = []

    # Step 8 — Voice setup
    mic_tested: bool = False
    speaker_tested: bool = False
    stt_model_downloaded: bool = False
    tts_model_downloaded: bool = False

    # Step 9 — Hardware validation
    hardware_tier_detected: int = 1
    benchmark_score: float = 0.0
    profile_compatible: bool = True
    ram_gb: float = 0.0

    # Step 10 — License binding
    license_type: str = ""  # "tpm" or "key"
    license_bound: bool = False
    license_tier: int = 0

    # Step 11 — Health check
    health_check_passed: bool = False
    health_check_results: dict = {}

    # Step 12 — Go live
    setup_complete: bool = False
    local_url: str = ""


# ---------------------------------------------------------------------------
# Module-level singleton (in-process cache between requests)
# ---------------------------------------------------------------------------

_state: WizardState | None = None


def get_state() -> WizardState:
    """Return the current wizard state, loading from disk if necessary."""
    global _state
    if _state is not None:
        return _state

    if STATE_FILE.exists():
        try:
            data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
            _state = WizardState.model_validate(data)
            return _state
        except Exception as exc:
            logger.warning("Failed to load wizard state from %s: %s — starting fresh", STATE_FILE, exc)

    _state = WizardState()
    return _state


def save_state(state: WizardState) -> None:
    """Persist wizard state to disk. Falls back to in-memory only on write error.

    The state file is written with 0o600 permissions (owner read/write only)
    to prevent other processes from reading credentials stored in the state.
    """
    global _state
    _state = state
    try:
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(state.model_dump_json(indent=2), encoding="utf-8")
        # Restrict to owner-only read/write — credentials are held in state.
        os.chmod(STATE_FILE, 0o600)
    except OSError as exc:
        logger.warning("Could not persist wizard state to %s: %s", STATE_FILE, exc)


def reset_state() -> WizardState:
    """Reset wizard state to defaults (used for testing / re-run)."""
    global _state
    _state = WizardState()
    save_state(_state)
    return _state
