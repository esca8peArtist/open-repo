"""
Wizard tests: step 12 writes .wizard-complete marker, sets setup_complete=True,
and redirects to the dashboard.
"""
from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch, call

import pytest

from wizard.state import WizardState, get_state, save_state


class TestWizardCompleteMarker:
    """complete_setup() must write the .wizard-complete marker file."""

    @pytest.mark.asyncio
    async def test_complete_setup_writes_marker(self, tmp_path):
        """complete_setup() must create the WIZARD_COMPLETE_MARKER file."""
        from wizard.steps.step12_golive import complete_setup

        marker_path = tmp_path / ".wizard-complete"
        state_file = tmp_path / "state.json"

        state = WizardState()

        with (
            patch("wizard.steps.step12_golive.WIZARD_COMPLETE_MARKER", marker_path),
            patch("wizard.state.STATE_FILE", state_file),
            patch("wizard.state._state", None),
            patch("subprocess.run", return_value=MagicMock(returncode=0)),
        ):
            await complete_setup(state)

        assert marker_path.exists()

    @pytest.mark.asyncio
    async def test_complete_setup_sets_setup_complete_true(self, tmp_path):
        """complete_setup() must set state.setup_complete=True."""
        from wizard.steps.step12_golive import complete_setup

        marker_path = tmp_path / ".wizard-complete"
        state_file = tmp_path / "state.json"

        state = WizardState()
        assert state.setup_complete is False

        with (
            patch("wizard.steps.step12_golive.WIZARD_COMPLETE_MARKER", marker_path),
            patch("wizard.state.STATE_FILE", state_file),
            patch("wizard.state._state", None),
            patch("subprocess.run", return_value=MagicMock(returncode=0)),
        ):
            await complete_setup(state)

        assert state.setup_complete is True

    @pytest.mark.asyncio
    async def test_complete_setup_saves_dashboard_url(self, tmp_path):
        """complete_setup() must persist the DASHBOARD_URL in state.local_url."""
        from wizard.steps.step12_golive import complete_setup
        from wizard.config import DASHBOARD_URL

        marker_path = tmp_path / ".wizard-complete"
        state_file = tmp_path / "state.json"

        state = WizardState()

        with (
            patch("wizard.steps.step12_golive.WIZARD_COMPLETE_MARKER", marker_path),
            patch("wizard.steps.step12_golive.DASHBOARD_URL", "http://agent.local:8080"),
            patch("wizard.state.STATE_FILE", state_file),
            patch("wizard.state._state", None),
            patch("subprocess.run", return_value=MagicMock(returncode=0)),
        ):
            await complete_setup(state)

        assert state.local_url == "http://agent.local:8080"

    @pytest.mark.asyncio
    async def test_complete_setup_marker_parent_created(self, tmp_path):
        """complete_setup() must create parent directories for the marker if needed."""
        from wizard.steps.step12_golive import complete_setup

        marker_path = tmp_path / "nested" / "dir" / ".wizard-complete"
        state_file = tmp_path / "state.json"

        state = WizardState()

        with (
            patch("wizard.steps.step12_golive.WIZARD_COMPLETE_MARKER", marker_path),
            patch("wizard.state.STATE_FILE", state_file),
            patch("wizard.state._state", None),
            patch("subprocess.run", return_value=MagicMock(returncode=0)),
        ):
            await complete_setup(state)

        assert marker_path.exists()

    @pytest.mark.asyncio
    async def test_complete_setup_marker_write_failure_is_nonfatal(self, tmp_path):
        """If marker write fails due to permissions, complete_setup() must not raise."""
        from wizard.steps.step12_golive import complete_setup

        marker_path = tmp_path / ".wizard-complete"
        state_file = tmp_path / "state.json"
        state = WizardState()

        with (
            patch("wizard.steps.step12_golive.WIZARD_COMPLETE_MARKER", marker_path),
            patch("wizard.state.STATE_FILE", state_file),
            patch("wizard.state._state", None),
            patch("subprocess.run", return_value=MagicMock(returncode=0)),
            patch.object(Path, "touch", side_effect=OSError("Permission denied")),
            patch.object(Path, "mkdir", return_value=None),
        ):
            # Must not raise
            await complete_setup(state)

    @pytest.mark.asyncio
    async def test_complete_setup_calls_systemctl(self, tmp_path):
        """complete_setup() must attempt to enable agentcore.service via systemctl."""
        from wizard.steps.step12_golive import complete_setup

        marker_path = tmp_path / ".wizard-complete"
        state_file = tmp_path / "state.json"
        state = WizardState()

        mock_run = MagicMock(returncode=0)

        with (
            patch("wizard.steps.step12_golive.WIZARD_COMPLETE_MARKER", marker_path),
            patch("wizard.state.STATE_FILE", state_file),
            patch("wizard.state._state", None),
            patch("subprocess.run", return_value=mock_run) as mock_subprocess,
        ):
            await complete_setup(state)

        # systemctl must have been called
        assert mock_subprocess.called
        args = mock_subprocess.call_args[0][0]
        assert "systemctl" in args

    @pytest.mark.asyncio
    async def test_complete_setup_systemctl_not_found_is_nonfatal(self, tmp_path):
        """If systemctl is not available (Docker mode), complete_setup() must not raise."""
        from wizard.steps.step12_golive import complete_setup

        marker_path = tmp_path / ".wizard-complete"
        state_file = tmp_path / "state.json"
        state = WizardState()

        with (
            patch("wizard.steps.step12_golive.WIZARD_COMPLETE_MARKER", marker_path),
            patch("wizard.state.STATE_FILE", state_file),
            patch("wizard.state._state", None),
            patch("subprocess.run", side_effect=FileNotFoundError("systemctl not found")),
        ):
            # Must not raise
            await complete_setup(state)

        assert state.setup_complete is True  # still completes


class TestStep12Idempotency:
    """Step 12 must be idempotent — calling it twice must not break state."""

    @pytest.mark.asyncio
    async def test_double_complete_setup_idempotent(self, tmp_path):
        """Calling complete_setup() twice must not raise or corrupt state."""
        from wizard.steps.step12_golive import complete_setup

        marker_path = tmp_path / ".wizard-complete"
        state_file = tmp_path / "state.json"
        state = WizardState()

        with (
            patch("wizard.steps.step12_golive.WIZARD_COMPLETE_MARKER", marker_path),
            patch("wizard.state.STATE_FILE", state_file),
            patch("wizard.state._state", None),
            patch("subprocess.run", return_value=MagicMock(returncode=0)),
        ):
            await complete_setup(state)
            await complete_setup(state)  # second call must be safe

        assert state.setup_complete is True
        assert marker_path.exists()

    def test_wizard_state_setup_complete_default_false(self):
        """Fresh WizardState must have setup_complete=False."""
        state = WizardState()
        assert state.setup_complete is False
        assert state.local_url == ""

    def test_wizard_state_all_step_fields_present(self):
        """WizardState must expose fields for all 12 steps."""
        state = WizardState()
        # Step 1
        assert hasattr(state, "language")
        assert hasattr(state, "agent_name")
        # Step 2
        assert hasattr(state, "selected_profile")
        # Step 4
        assert hasattr(state, "telegram_token")
        assert hasattr(state, "twilio_account_sid")
        # Step 9
        assert hasattr(state, "hardware_tier_detected")
        assert hasattr(state, "benchmark_score")
        # Step 10
        assert hasattr(state, "license_bound")
        # Step 11
        assert hasattr(state, "health_check_passed")
        # Step 12
        assert hasattr(state, "setup_complete")
        assert hasattr(state, "local_url")
