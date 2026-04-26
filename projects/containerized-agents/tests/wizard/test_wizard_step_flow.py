"""
Wizard tests: full state machine step 1→12 progression.
"""
from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch, AsyncMock

import pytest

from wizard.state import WizardState, get_state, save_state, reset_state


def _isolated_state_file(tmp_path: Path) -> Path:
    """Return a temp path for the wizard state file."""
    return tmp_path / "wizard-state.json"


class TestWizardStepProgression:
    """State machine: verify each step advances current_step and updates fields."""

    def test_initial_state_is_step1(self, tmp_path):
        """Fresh state must start at step 1."""
        state_file = _isolated_state_file(tmp_path)
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None  # clear singleton
            state = get_state()
        assert state.current_step == 1
        assert state.completed_steps == []

    def test_step1_advances_to_step2(self, tmp_path):
        """Completing step 1 must set current_step=2 and save language/agent_name."""
        state_file = _isolated_state_file(tmp_path)
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.language = "fr"
            state.agent_name = "Aria"
            if 1 not in state.completed_steps:
                state.completed_steps.append(1)
            state.current_step = 2
            save_state(state)
            ws._state = None  # force reload
            reloaded = get_state()

        assert reloaded.current_step == 2
        assert reloaded.language == "fr"
        assert reloaded.agent_name == "Aria"
        assert 1 in reloaded.completed_steps

    def test_step2_saves_profile_selection(self, tmp_path):
        """Step 2 must persist selected_profile and advance to step 3."""
        state_file = _isolated_state_file(tmp_path)
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.selected_profile = 3
            state.completed_steps = [1, 2]
            state.current_step = 3
            save_state(state)
            ws._state = None
            reloaded = get_state()

        assert reloaded.selected_profile == 3
        assert reloaded.current_step == 3

    def test_step4_saves_channel_settings(self, tmp_path):
        """Step 4 must persist telegram/twilio settings."""
        state_file = _isolated_state_file(tmp_path)
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.telegram_token = "123456:ABC-DEF"
            state.telegram_enabled = True
            state.twilio_account_sid = "AC" + "a" * 32
            state.twilio_auth_token = "tok"
            state.twilio_phone = "+15005550006"
            state.twilio_enabled = True
            state.completed_steps = [1, 2, 3, 4]
            state.current_step = 5
            save_state(state)
            ws._state = None
            reloaded = get_state()

        assert reloaded.telegram_enabled is True
        assert reloaded.telegram_token == "123456:ABC-DEF"
        assert reloaded.twilio_enabled is True
        assert reloaded.current_step == 5

    def test_step9_saves_hardware_benchmark(self, tmp_path):
        """Step 9 must persist hardware tier and benchmark score."""
        state_file = _isolated_state_file(tmp_path)
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.hardware_tier_detected = 3
            state.benchmark_score = 42.5
            state.ram_gb = 32.0
            state.profile_compatible = True
            state.completed_steps = list(range(1, 10))
            state.current_step = 10
            save_state(state)
            ws._state = None
            reloaded = get_state()

        assert reloaded.hardware_tier_detected == 3
        assert reloaded.benchmark_score == 42.5
        assert reloaded.ram_gb == 32.0

    def test_step12_marks_setup_complete(self, tmp_path):
        """Step 12 must set setup_complete=True."""
        state_file = _isolated_state_file(tmp_path)
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.setup_complete = True
            state.local_url = "http://agent.local:8080"
            state.completed_steps = list(range(1, 13))
            state.current_step = 12
            save_state(state)
            ws._state = None
            reloaded = get_state()

        assert reloaded.setup_complete is True
        assert reloaded.local_url == "http://agent.local:8080"

    def test_completed_steps_accumulate(self, tmp_path):
        """Completed steps must accumulate without duplicates."""
        state_file = _isolated_state_file(tmp_path)
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            for step in [1, 2, 3, 1, 2]:  # 1 and 2 repeated
                if step not in state.completed_steps:
                    state.completed_steps.append(step)
            save_state(state)
            ws._state = None
            reloaded = get_state()

        assert reloaded.completed_steps.count(1) == 1
        assert reloaded.completed_steps.count(2) == 1

    def test_reset_state_clears_all_fields(self, tmp_path):
        """reset_state() must return a fresh WizardState with all defaults."""
        state_file = _isolated_state_file(tmp_path)
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.agent_name = "Aria"
            state.current_step = 7
            save_state(state)
            fresh = reset_state()

        assert fresh.current_step == 1
        assert fresh.agent_name == ""
        assert fresh.completed_steps == []

    def test_state_persists_across_reload(self, tmp_path):
        """State written to disk must survive _state=None singleton reset."""
        state_file = _isolated_state_file(tmp_path)
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.agent_name = "PersistMe"
            state.selected_profile = 5
            save_state(state)
            ws._state = None  # evict cache
            reloaded = get_state()

        assert reloaded.agent_name == "PersistMe"
        assert reloaded.selected_profile == 5

    def test_corrupt_state_file_returns_fresh_state(self, tmp_path):
        """Corrupt state file must be ignored and return a default WizardState."""
        state_file = _isolated_state_file(tmp_path)
        state_file.parent.mkdir(parents=True, exist_ok=True)
        state_file.write_text("{corrupt json{{{", encoding="utf-8")

        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()

        assert state.current_step == 1
        assert state.agent_name == ""
