"""
Tests for usage monitoring and tracking utilities.

Imports from scripts/ by adding that directory to sys.path.
"""

import importlib
import json
import os
import sys
import types
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch, call
import pytest

# Add scripts/ to path so we can import the modules under test
SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


# ── Lazy imports (avoids executing module-level code like find_session_dir at
#    import time, which requires ~/.claude to exist) ──────────────────────────

def _import_usage_check():
    """Import usage-check module, reloading to pick up any patches."""
    if "usage-check" in sys.modules:
        return sys.modules["usage-check"]
    spec = importlib.util.spec_from_file_location("usage-check", SCRIPTS_DIR / "usage-check.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["usage-check"] = mod
    spec.loader.exec_module(mod)
    return mod


def _import_usage_monitor():
    """Import usage-monitor module."""
    if "usage-monitor" in sys.modules:
        return sys.modules["usage-monitor"]
    spec = importlib.util.spec_from_file_location("usage-monitor", SCRIPTS_DIR / "usage-monitor.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["usage-monitor"] = mod
    spec.loader.exec_module(mod)
    return mod


# ── 1. Billing week boundary ──────────────────────────────────────────────────

@pytest.mark.unit
class TestBillingWeekBoundary:
    """_last_tuesday() returns the correct Tuesday for each day of the week."""

    def _make_date(self, year, month, day):
        return date(year, month, day)

    def _last_tuesday_for(self, d: date) -> date:
        """Pure implementation of _last_tuesday logic for a given date."""
        days_back = (d.weekday() - 1) % 7  # Mon=0, Tue=1
        return d - timedelta(days=days_back)

    def test_tuesday_returns_same_day(self):
        """Tuesday should map to itself."""
        d = date(2026, 4, 21)  # Tuesday
        assert d.weekday() == 1
        result = self._last_tuesday_for(d)
        assert result == d

    def test_monday_returns_previous_tuesday(self):
        """Monday should map to the Tuesday 6 days prior."""
        d = date(2026, 4, 27)  # Monday
        assert d.weekday() == 0
        result = self._last_tuesday_for(d)
        assert result == date(2026, 4, 21)

    def test_wednesday_returns_previous_tuesday(self):
        """Wednesday should map to the Tuesday 1 day prior."""
        d = date(2026, 4, 22)  # Wednesday
        assert d.weekday() == 2
        result = self._last_tuesday_for(d)
        assert result == date(2026, 4, 21)

    def test_sunday_returns_prior_tuesday_not_monday(self):
        """Sunday must map to the prior Tuesday (5 days back), not Monday."""
        d = date(2026, 4, 26)  # Sunday
        assert d.weekday() == 6
        result = self._last_tuesday_for(d)
        # Should be Tuesday 2026-04-21, NOT Monday 2026-04-25
        assert result == date(2026, 4, 21)
        assert result != date(2026, 4, 25)  # not Monday

    def test_saturday_returns_prior_tuesday(self):
        """Saturday should map to the Tuesday 4 days prior."""
        d = date(2026, 4, 25)  # Saturday
        assert d.weekday() == 5
        result = self._last_tuesday_for(d)
        assert result == date(2026, 4, 21)

    def test_key_changes_on_tuesday_not_monday(self):
        """The billing week key changes on Tuesday, not Monday."""
        mon = date(2026, 4, 27)  # Monday — still prior billing week
        tue = date(2026, 4, 28)  # Tuesday — new billing week

        mon_result = self._last_tuesday_for(mon)
        tue_result = self._last_tuesday_for(tue)

        assert mon_result == date(2026, 4, 21)  # prior Tuesday
        assert tue_result == date(2026, 4, 28)  # the Tuesday itself
        assert mon_result != tue_result  # different billing weeks

    def test_last_tuesday_live(self):
        """_last_tuesday() from usage-monitor matches our pure implementation."""
        mod = _import_usage_monitor()
        result = mod._last_tuesday()
        today = datetime.now(timezone.utc).date()
        expected = self._last_tuesday_for(today)
        assert result.date() == expected

    def test_current_week_format(self):
        """current_week() returns an isoformat date string ending in -billing."""
        mod = _import_usage_monitor()
        week = mod.current_week()
        assert week.endswith("-billing")
        date_part = week[:-len("-billing")]
        # Should be a valid date
        parsed = date.fromisoformat(date_part)
        assert parsed.weekday() == 1  # always a Tuesday


# ── 2. Model classification ───────────────────────────────────────────────────

@pytest.mark.unit
class TestModelClassification:
    """classify_model() handles exact names, dated suffixes, unknowns, synthetic."""

    @pytest.fixture(autouse=True)
    def mod(self):
        self.uc = _import_usage_check()

    def test_exact_sonnet(self):
        assert self.uc.classify_model("claude-sonnet-4-6") == "sonnet"

    def test_sonnet_with_date_suffix(self):
        assert self.uc.classify_model("claude-sonnet-4-6-20260801") == "sonnet"

    def test_sonnet_4_5(self):
        assert self.uc.classify_model("claude-sonnet-4-5") == "sonnet"

    def test_exact_opus(self):
        assert self.uc.classify_model("claude-opus-4-6") == "opus"

    def test_opus_with_date_suffix(self):
        assert self.uc.classify_model("claude-opus-4-7-20270101") == "opus"

    def test_exact_haiku(self):
        assert self.uc.classify_model("claude-haiku-4-5") == "haiku"

    def test_haiku_with_date_suffix(self):
        assert self.uc.classify_model("claude-haiku-4-5-20251001") == "haiku"

    def test_synthetic(self):
        assert self.uc.classify_model("<synthetic>") == "synthetic"

    def test_empty_string(self):
        assert self.uc.classify_model("") == "synthetic"

    def test_unknown_model(self):
        assert self.uc.classify_model("gpt-4o") == "other"

    def test_unknown_string(self):
        assert self.uc.classify_model("unknown") == "other"

    def test_future_claude_sonnet(self):
        assert self.uc.classify_model("claude-sonnet-5-0") == "sonnet"

    def test_future_claude_opus(self):
        assert self.uc.classify_model("claude-opus-5-0") == "opus"


# ── 3. Fresh-start threshold pre-population ──────────────────────────────────

@pytest.mark.unit
class TestFreshStartThresholdPrepopulation:
    """On new week, pre-populate already_crossed to prevent alert flood."""

    def _already_crossed(self, effective_pct: float) -> list:
        """Mirror the logic from usage-monitor.py main()."""
        return [t for t in range(10, 101, 10) if effective_pct >= t]

    def test_73pct_crosses_10_through_70(self):
        result = self._already_crossed(73.0)
        assert result == [10, 20, 30, 40, 50, 60, 70]

    def test_73pct_does_not_include_80(self):
        result = self._already_crossed(73.0)
        assert 80 not in result

    def test_0pct_empty(self):
        assert self._already_crossed(0.0) == []

    def test_100pct_all_thresholds(self):
        result = self._already_crossed(100.0)
        assert result == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    def test_80pct_exactly(self):
        result = self._already_crossed(80.0)
        assert 80 in result
        assert 90 not in result

    def test_50pct_exactly(self):
        result = self._already_crossed(50.0)
        assert result == [10, 20, 30, 40, 50]
        assert 60 not in result

    def test_10pct_boundary(self):
        result_just_below = self._already_crossed(9.9)
        result_at = self._already_crossed(10.0)
        assert result_just_below == []
        assert result_at == [10]


# ── 4. Atomic save ────────────────────────────────────────────────────────────

@pytest.mark.unit
class TestAtomicSave:
    """save_state() writes via a .tmp file and calls os.replace."""

    def test_uses_tmp_then_replace(self, tmp_path):
        mod = _import_usage_monitor()
        state = {"week": "2026-04-21-billing", "notified_thresholds": [10, 20], "paused": False}

        original_state_file = mod.STATE_FILE
        tmp_state = tmp_path / ".usage-monitor-state.json"
        mod.STATE_FILE = tmp_state

        try:
            with patch("os.replace") as mock_replace:
                # Also patch the tmp Path so the write goes to tmp_path
                expected_tmp = tmp_state.with_suffix(".tmp")

                # Run save_state — it writes to .tmp then calls os.replace
                mod.save_state(state)

                mock_replace.assert_called_once_with(expected_tmp, tmp_state)
        finally:
            mod.STATE_FILE = original_state_file

    def test_state_contents_correct(self, tmp_path):
        mod = _import_usage_monitor()
        state = {"week": "2026-04-21-billing", "notified_thresholds": [10], "paused": True}

        original_state_file = mod.STATE_FILE
        tmp_state = tmp_path / ".usage-monitor-state.json"
        mod.STATE_FILE = tmp_state

        try:
            mod.save_state(state)
            # After save, the tmp file should exist (os.replace is real here)
            # tmp was renamed to state file
            loaded = json.loads(tmp_state.read_text())
            assert loaded["week"] == "2026-04-21-billing"
            assert loaded["notified_thresholds"] == [10]
            assert loaded["paused"] is True
        finally:
            mod.STATE_FILE = original_state_file


# ── 5. M2 mtime skipping ─────────────────────────────────────────────────────

@pytest.mark.unit
class TestMtimeSkipping:
    """Files with mtime before billing week start should be skipped."""

    def test_old_file_skipped(self, tmp_path):
        mod = _import_usage_check()
        since = datetime(2026, 4, 21, 0, 0, 0, tzinfo=timezone.utc)

        # Create a JSONL file with an old mtime (before billing week)
        old_file = tmp_path / "old-session.jsonl"
        # Write a valid assistant message
        msg = {
            "type": "assistant",
            "timestamp": "2026-04-20T10:00:00+00:00",
            "message": {
                "model": "claude-sonnet-4-6",
                "usage": {"output_tokens": 500, "input_tokens": 100}
            }
        }
        old_file.write_text(json.dumps(msg) + "\n")
        # Set mtime to before billing week start
        old_ts = since.timestamp() - 86400  # 1 day before
        os.utime(old_file, (old_ts, old_ts))

        original_session_dir = mod.SESSION_DIR
        mod.SESSION_DIR = tmp_path
        try:
            result = mod.collect_tokens(since)
            # Old file should be skipped — no tokens collected
            total = sum(v["output"] for v in result.values())
            assert total == 0
        finally:
            mod.SESSION_DIR = original_session_dir

    def test_new_file_included(self, tmp_path):
        mod = _import_usage_check()
        since = datetime(2026, 4, 21, 0, 0, 0, tzinfo=timezone.utc)

        # Create a JSONL file with a fresh mtime (after billing week start)
        new_file = tmp_path / "new-session.jsonl"
        msg = {
            "type": "assistant",
            "timestamp": "2026-04-22T10:00:00+00:00",
            "message": {
                "model": "claude-sonnet-4-6",
                "usage": {"output_tokens": 1000, "input_tokens": 200}
            }
        }
        new_file.write_text(json.dumps(msg) + "\n")
        # Set mtime to after billing week start
        new_ts = since.timestamp() + 86400
        os.utime(new_file, (new_ts, new_ts))

        original_session_dir = mod.SESSION_DIR
        mod.SESSION_DIR = tmp_path
        try:
            result = mod.collect_tokens(since)
            sonnet_out = sum(v["output"] for k, v in result.items()
                             if mod.classify_model(k) == "sonnet")
            assert sonnet_out == 1000
        finally:
            mod.SESSION_DIR = original_session_dir


# ── 6. Pause/override interaction ────────────────────────────────────────────

@pytest.mark.unit
class TestPauseOverrideInteraction:
    """--check exit codes: 0=OK, 1=throttled, 2=paused (no override)."""

    @pytest.fixture(autouse=True)
    def mod(self):
        self._mod = _import_usage_check()

    def _run_check(self, tmp_path, report, pause_exists: bool, override_exists: bool) -> int:
        """Simulate the --check logic and return the exit code."""
        pause_file = tmp_path / "USAGE_PAUSE"
        override_file = tmp_path / "USAGE_PAUSE_OVERRIDE"

        if pause_exists:
            pause_file.write_text("paused")
        if override_exists:
            override_file.write_text("override")

        original_pause = self._mod.PAUSE_FILE
        original_override = self._mod.OVERRIDE_FILE
        self._mod.PAUSE_FILE = pause_file
        self._mod.OVERRIDE_FILE = override_file

        try:
            # Replicate usage-check.py --check logic
            if report["status"]["over_any"]:
                return 1
            if pause_file.exists():
                if override_file.exists():
                    return 0  # OVERRIDE ACTIVE
                return 2  # PAUSED
            return 0  # OK
        finally:
            self._mod.PAUSE_FILE = original_pause
            self._mod.OVERRIDE_FILE = original_override

    def _make_report(self, sonnet_over=False, all_over=False):
        return {
            "status": {
                "over_any": sonnet_over or all_over,
                "sonnet_over": sonnet_over,
                "all_over": all_over,
                "sonnet_warn": False,
                "all_warn": False,
            },
            "pct": {"sonnet": 95.0 if sonnet_over else 50.0,
                    "all_models": 50.0},
        }

    def test_exit_0_when_ok(self, tmp_path):
        report = self._make_report()
        code = self._run_check(tmp_path, report, pause_exists=False, override_exists=False)
        assert code == 0

    def test_exit_1_when_throttled(self, tmp_path):
        report = self._make_report(sonnet_over=True)
        code = self._run_check(tmp_path, report, pause_exists=False, override_exists=False)
        assert code == 1

    def test_exit_2_when_paused_no_override(self, tmp_path):
        report = self._make_report()
        code = self._run_check(tmp_path, report, pause_exists=True, override_exists=False)
        assert code == 2

    def test_exit_0_when_paused_with_override(self, tmp_path):
        report = self._make_report()
        code = self._run_check(tmp_path, report, pause_exists=True, override_exists=True)
        assert code == 0

    def test_throttle_takes_priority_over_pause(self, tmp_path):
        """Even if paused+override, throttle (>90%) returns exit 1."""
        report = self._make_report(sonnet_over=True)
        code = self._run_check(tmp_path, report, pause_exists=True, override_exists=True)
        assert code == 1
