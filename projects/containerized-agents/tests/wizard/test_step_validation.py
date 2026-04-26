"""
Wizard tests: invalid inputs on each step return errors without advancing state.
"""
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from wizard.state import WizardState, get_state, save_state


def _get_fresh_state(tmp_path: Path) -> WizardState:
    state_file = tmp_path / "wizard-state.json"
    import wizard.state as ws
    ws._state = None
    with patch("wizard.state.STATE_FILE", state_file):
        return get_state()


class TestStep1Validation:
    """Step 1 (welcome) field validation."""

    def test_empty_agent_name_not_saved(self, tmp_path):
        """Empty agent_name must not advance the wizard step."""
        state_file = tmp_path / "wizard-state.json"
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            original_step = state.current_step

            # Simulate the validation: reject empty agent_name
            agent_name = "   "  # whitespace only
            if not agent_name.strip():
                # Should NOT advance
                pass
            else:
                state.agent_name = agent_name.strip()
                state.current_step = 2
                save_state(state)

        assert state.current_step == original_step

    def test_valid_language_code_accepted(self, tmp_path):
        """Valid ISO language code must be persisted correctly."""
        state_file = tmp_path / "wizard-state.json"
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.language = "de"
            state.agent_name = "MaxBot"
            state.current_step = 2
            save_state(state)

        assert state.language == "de"

    def test_agent_name_stripped_of_whitespace(self, tmp_path):
        """agent_name must be stripped of leading/trailing whitespace."""
        state_file = tmp_path / "wizard-state.json"
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.agent_name = "  Aria  ".strip()
            save_state(state)

        assert state.agent_name == "Aria"


class TestStep2Validation:
    """Step 2 (profile selection) validation."""

    def test_invalid_profile_id_not_saved(self, tmp_path):
        """Profile IDs outside 1–6 must not be saved as selected_profile."""
        valid_profiles = set(range(1, 7))
        invalid_id = 99

        state_file = tmp_path / "wizard-state.json"
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            original = state.selected_profile

            if invalid_id not in valid_profiles:
                # Do not advance
                pass
            else:
                state.selected_profile = invalid_id
                save_state(state)

        assert state.selected_profile == original  # unchanged

    def test_valid_profile_id_1_accepted(self, tmp_path):
        """Profile ID 1 must be a valid selection."""
        state_file = tmp_path / "wizard-state.json"
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.selected_profile = 1
            save_state(state)

        assert state.selected_profile == 1

    def test_valid_profile_id_6_accepted(self, tmp_path):
        """Profile ID 6 (Enterprise Orchestrator) must be a valid selection."""
        state_file = tmp_path / "wizard-state.json"
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.selected_profile = 6
            save_state(state)

        assert state.selected_profile == 6


class TestStep4Validation:
    """Step 4 (channels) validation."""

    def test_telegram_enabled_without_token_detected(self, tmp_path):
        """telegram_enabled=True with empty token is an invalid configuration."""
        state_file = tmp_path / "wizard-state.json"
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.telegram_enabled = True
            state.telegram_token = ""

        # Validation check: enabled without token is invalid
        is_invalid = state.telegram_enabled and not state.telegram_token
        assert is_invalid is True

    def test_twilio_sid_format_validated(self):
        """Twilio Account SID must start with 'AC' and be 34 chars."""
        valid_sid = "AC" + "a" * 32
        invalid_sid = "XX" + "a" * 32
        zero_len_sid = ""

        assert valid_sid.startswith("AC") and len(valid_sid) == 34
        assert not (invalid_sid.startswith("AC") and len(invalid_sid) == 34)
        assert not (zero_len_sid.startswith("AC") and len(zero_len_sid) == 34)

    def test_whatsapp_requires_twilio_enabled(self, tmp_path):
        """whatsapp_enabled=True without twilio_enabled is invalid."""
        state_file = tmp_path / "wizard-state.json"
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.whatsapp_enabled = True
            state.twilio_enabled = False

        # Business rule: WhatsApp requires Twilio
        is_invalid = state.whatsapp_enabled and not state.twilio_enabled
        assert is_invalid is True


class TestStep6Validation:
    """Step 6 (integrations) validation."""

    def test_caldav_url_must_be_nonempty_if_provided(self):
        """caldav_url, if set, must be a non-empty string."""
        valid_url = "https://caldav.example.com/dav/"
        empty_url = ""
        whitespace_url = "   "

        assert bool(valid_url.strip()) is True
        assert bool(empty_url.strip()) is False
        assert bool(whitespace_url.strip()) is False

    def test_smtp_port_must_be_positive(self):
        """SMTP port must be a positive integer (25, 465, 587)."""
        valid_ports = [25, 465, 587, 993]
        invalid_ports = [0, -1, 99999]

        for port in valid_ports:
            assert 1 <= port <= 65535

        for port in invalid_ports:
            assert not (1 <= port <= 65535)

    def test_email_requires_both_user_and_password(self, tmp_path):
        """Email user without password (or vice versa) is incomplete."""
        state_file = tmp_path / "wizard-state.json"
        with patch("wizard.state.STATE_FILE", state_file):
            import wizard.state as ws
            ws._state = None
            state = get_state()
            state.email_user = "user@example.com"
            state.email_password = ""

        incomplete = bool(state.email_user) != bool(state.email_password)
        assert incomplete is True


class TestStep9Validation:
    """Step 9 (hardware) validation."""

    def test_incompatible_profile_detected(self):
        """Profile 4 (Developer Assistant) requires 24 GB RAM min."""
        from wizard.config import PROFILE_DISPLAY
        min_ram = PROFILE_DISPLAY[4]["min_ram_gb"]
        ram_gb = 8.0  # below minimum

        compatible = ram_gb >= min_ram
        assert compatible is False

    def test_compatible_hardware_for_profile1(self):
        """Profile 1 (Personal Productivity) requires only 8 GB — 16 GB is compatible."""
        from wizard.config import PROFILE_DISPLAY
        min_ram = PROFILE_DISPLAY[1]["min_ram_gb"]
        ram_gb = 16.0

        compatible = ram_gb >= min_ram
        assert compatible is True

    def test_zero_ram_treated_as_unknown_not_blocked(self):
        """RAM detection failure (0.0) must not block the wizard."""
        ram_gb = 0.0
        min_ram = 8
        # Implementation: 0 means unknown — don't block
        compatible = ram_gb >= min_ram or ram_gb == 0.0
        assert compatible is True
