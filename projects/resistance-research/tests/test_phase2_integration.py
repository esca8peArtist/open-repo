#!/usr/bin/env python3
"""
Phase 2 Integration Tests — phase_2_domain_trackers.py

Three test cases per domain monitor:
1. Mock API response — verifies detection logic
2. State persistence — verifies JSON round-trip
3. Error handling — verifies graceful degradation on network failure

Additional:
- Parallel runner test (run_all_monitors_parallel)
- Email router Phase 2 keyword extension test
"""

import json
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

import pytest

# Add src to path
_TESTS_DIR = Path(__file__).parent.resolve()
_SRC_DIR = _TESTS_DIR.parent / "src"
sys.path.insert(0, str(_SRC_DIR))

from phase_2_domain_trackers import (
    Domain58SCOTUSMonitor,
    Domain39HHSTracker,
    Domain40ElectionMonitor,
    Domain2CoalitionEmailRouter,
    run_all_monitors_parallel,
    load_config,
)
from monitors.scotus_opinion_monitor import SCOTUSRuling
from monitors.hhs_guidance_monitor import HHSGuidance
from monitors.election_events_monitor import ElectionEvent
from monitors.coalition_email_router import CoalitionEmail


# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def base_config():
    """Minimal config that passes initialization checks."""
    return {
        "scotus_discord_webhook":          "https://discord.test/webhook/123",
        "scotus_polling_interval_minutes": 14,
        "hhs_discord_webhook":             "https://discord.test/webhook/123",
        "hhs_slack_webhook":               "https://slack.test/webhook/456",
        "hhs_polling_interval_minutes":    60,
        "election_discord_webhook":        "https://discord.test/webhook/123",
        "election_polling_interval_minutes": 240,
        "gmail_enabled":                   False,
        "gmail_credentials":               "",
        "gmail_label":                     "phase-1-responses",
        "email_lookback_hours":            168,
        "email_polling_interval_minutes":  60,
        "phase1_start_date":               "2026-05-28",
    }


@pytest.fixture
def scotus_monitor(base_config):
    return Domain58SCOTUSMonitor(config=base_config)


@pytest.fixture
def hhs_tracker(base_config):
    return Domain39HHSTracker(config=base_config)


@pytest.fixture
def election_monitor(base_config):
    return Domain40ElectionMonitor(config=base_config)


@pytest.fixture
def email_router(base_config):
    return Domain2CoalitionEmailRouter(config=base_config)


# ===========================================================================
# Domain 58 SCOTUS Monitor — 3 tests
# ===========================================================================


class TestDomain58SCOTUSMonitor:
    """Tests for Domain58SCOTUSMonitor wrapper."""

    # Test 1: Mock API — ruling detected on supremecourt.gov
    @patch("monitors.scotus_opinion_monitor.requests.get")
    @patch("monitors.scotus_opinion_monitor.requests.post")
    def test_run_once_ruling_detected(self, mock_post, mock_get, scotus_monitor):
        """Mock SCOTUS.gov returning opinion page with ruling link."""
        # Mock HTTP GET (opinion page)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = (
            '<a href="/opinions/25-365.pdf">Trump v. Barbara 25-365 opinion</a>'
        )
        mock_get.return_value = mock_response

        # Mock Discord POST
        mock_discord = Mock()
        mock_discord.status_code = 204
        mock_post.return_value = mock_discord

        # Ensure ruling_found starts False
        scotus_monitor._monitor.state["ruling_found"] = False

        result = scotus_monitor.run_once()

        assert result["status"] == "ruling_found"
        assert result["ruling"] is not None
        assert result["ruling"]["case_number"] == "25-365"
        assert result["ruling"]["source"] == "supremecourt.gov"
        assert result["alert_sent"] is True

    # Test 2: State persistence — ruling_found survives JSON round-trip
    def test_state_persistence_ruling_found(self, scotus_monitor):
        """Ruling state is persisted and reloaded correctly."""
        scotus_monitor._monitor.state["ruling_found"] = True
        scotus_monitor._monitor.state["ruling_date"] = "2026-06-28"
        scotus_monitor._monitor.state["ruling_url"] = "https://supremecourt.gov/opinions/25-365.pdf"
        scotus_monitor._monitor._save_state()

        # Reload from same state file
        reloaded_state = scotus_monitor._monitor._load_state()
        assert reloaded_state["ruling_found"] is True
        assert reloaded_state["ruling_date"] == "2026-06-28"

    # Test 3: Error handling — network timeout returns "pending" not exception
    @patch("monitors.scotus_opinion_monitor.requests.get")
    def test_run_once_network_error_graceful(self, mock_get, scotus_monitor):
        """Network error returns status=pending (not exception)."""
        import requests as req_mod
        mock_get.side_effect = req_mod.RequestException("Connection refused")

        scotus_monitor._monitor.state["ruling_found"] = False

        result = scotus_monitor.run_once()

        # Should degrade gracefully — no ruling means status=pending
        assert result["status"] in ("pending", "error")
        # Should never raise
        assert "monitor" in result
        assert result.get("ruling") is None

    def test_already_alerted_skips_recheck(self, scotus_monitor):
        """If ruling already found and alerted, run_once returns already_alerted."""
        scotus_monitor._monitor.state["ruling_found"] = True
        scotus_monitor._monitor.state["ruling_date"] = "2026-06-28"

        result = scotus_monitor.run_once()

        assert result["status"] == "already_alerted"
        assert result["alert_sent"] is False

    def test_polling_interval_is_sub_15_minutes(self, scotus_monitor):
        """SCOTUS monitor must poll at < 15 minute interval."""
        assert scotus_monitor._monitor.polling_interval < 15

    def test_get_state_returns_dict(self, scotus_monitor):
        """get_state() returns a dict with expected keys."""
        state = scotus_monitor.get_state()
        assert isinstance(state, dict)
        assert "ruling_found" in state
        assert "alerts_sent" in state


# ===========================================================================
# Domain 39 HHS Tracker — 3 tests
# ===========================================================================


class TestDomain39HHSTracker:
    """Tests for Domain39HHSTracker wrapper."""

    # Test 1: Mock check_federal_register directly to inject guidance objects
    @patch("monitors.hhs_guidance_monitor.requests.post")
    def test_run_once_guidance_detected(self, mock_post, hhs_tracker):
        """Patch check_federal_register to inject a Medicaid disenrollment item."""
        mock_discord = Mock()
        mock_discord.status_code = 204
        mock_post.return_value = mock_discord

        fake_guidance = HHSGuidance(
            title="Medicaid Disenrollment Final Rule",
            guidance_type="final_rule",
            guidance_date="2026-06-01",
            guidance_url="https://federalregister.gov/documents/2026/06/01/test",
            source="federal_register",
            domain_relevance="domain_39",
            summary="Final rule on disenrollment procedures effective June 1, 2026",
            confidence=0.9,
            key_dates=["June 1, 2026"],
        )

        # Patch at the monitor level — bypass HTTP entirely
        with patch.object(hhs_tracker._monitor, "check_federal_register", return_value=[fake_guidance]):
            with patch.object(hhs_tracker._monitor, "check_hhs_newsroom", return_value=[]):
                result = hhs_tracker.run_once()

        assert result["status"] == "new_guidance"
        assert result["items_found"] >= 1
        assert len(result["immediate_items"]) >= 1
        assert result["immediate_items"][0]["relevance"] == "domain_39"

    # Test 2: State persistence — items_seen survives restart
    def test_state_persistence_items_seen(self, hhs_tracker):
        """items_seen list survives JSON serialization and reload."""
        test_items = ["fr-https://test.example.com/item1", "fr-https://test.example.com/item2"]
        hhs_tracker._monitor.state["items_seen"] = test_items
        hhs_tracker._monitor._save_state()

        reloaded = hhs_tracker._monitor._load_state()
        assert all(item in reloaded["items_seen"] for item in test_items)

    # Test 3: Error handling — Federal Register timeout returns empty result
    @patch("monitors.hhs_guidance_monitor.requests.get")
    def test_run_once_federal_register_timeout(self, mock_get, hhs_tracker):
        """Federal Register timeout returns no_new_items, not exception."""
        import requests as req_mod
        mock_get.side_effect = req_mod.RequestException("Read timeout")

        result = hhs_tracker.run_once()

        assert result["status"] in ("no_new_items", "error")
        assert result["items_found"] == 0
        assert isinstance(result["immediate_items"], list)

    def test_polling_interval_default_hourly(self, hhs_tracker):
        """HHS tracker polls hourly by default."""
        assert hhs_tracker._monitor.polling_interval == 60

    def test_domain39_relevance_detection_integrated(self, hhs_tracker):
        """Domain 39 keyword relevance is correctly classified."""
        is_rel, level = hhs_tracker._monitor._is_domain39_relevant(
            "Medicaid Disenrollment Interim Final Rule",
            "Effective January 27, 2027 for continuous enrollment"
        )
        assert is_rel is True
        assert level == "domain_39"

    def test_adjacent_relevance_classified_correctly(self, hhs_tracker):
        """Healthcare-adjacent items get domain_39_adjacent relevance."""
        is_rel, level = hhs_tracker._monitor._is_domain39_relevant(
            "CMS Coverage Notice",
            "New healthcare enrollment guidance"
        )
        assert is_rel is True
        assert level in ("domain_39", "domain_39_adjacent")


# ===========================================================================
# Domain 40 Election Monitor — 3 tests
# ===========================================================================


class TestDomain40ElectionMonitor:
    """Tests for Domain40ElectionMonitor wrapper."""

    # Test 1: Mock check_fec_complaints directly to inject ElectionEvent objects
    @patch("monitors.election_events_monitor.requests.post")
    def test_run_once_election_event_detected(self, mock_post, election_monitor):
        """Patch check_fec_complaints to inject a Texas voter suppression event."""
        mock_discord = Mock()
        mock_discord.status_code = 204
        mock_post.return_value = mock_discord

        fake_event = ElectionEvent(
            title="Texas Voter Suppression Violation",
            event_type="suppression",
            event_date="2026-06-01",
            event_url="https://api.fec.gov/v1/violations/test-1",
            source="fec",
            state_context="Texas",
            domain_relevance="domain_1",
            summary="Voter ID requirement in Texas restricts ballot access",
            confidence=0.85,
            is_named_state=True,
        )

        # Patch at the monitor level — bypass HTTP entirely
        with patch.object(election_monitor._monitor, "check_fec_complaints", return_value=[fake_event]):
            with patch.object(election_monitor._monitor, "check_election_protection", return_value=[]):
                with patch.object(election_monitor._monitor, "check_voting_rights_news", return_value=[]):
                    result = election_monitor.run_once()

        assert result["status"] == "events_found"
        assert result["events_found"] >= 1

    # Test 2: State persistence — items_seen survives restart
    def test_state_persistence_items_seen(self, election_monitor):
        """Election monitor items_seen persists across restarts."""
        test_items = ["fec-https://api.fec.gov/test1"]
        election_monitor._monitor.state["items_seen"] = test_items
        election_monitor._monitor._save_state()

        reloaded = election_monitor._monitor._load_state()
        assert test_items[0] in reloaded["items_seen"]

    # Test 3: Error handling — FEC API unavailable returns empty result
    @patch("monitors.election_events_monitor.requests.get")
    def test_run_once_fec_unavailable(self, mock_get, election_monitor):
        """FEC API error returns no_new_events gracefully."""
        import requests as req_mod
        mock_get.side_effect = req_mod.RequestException("FEC API unavailable")

        result = election_monitor.run_once()

        assert result["status"] in ("no_new_events", "error")
        assert result["events_found"] == 0
        assert isinstance(result["deepfake_events"], list)

    def test_deepfake_keywords_extended(self, election_monitor):
        """Domain40 monitor has deepfake-specific keywords loaded."""
        assert "deepfake" in election_monitor._monitor.SUPPRESSION_KEYWORDS
        assert "election interference" in election_monitor._monitor.SUPPRESSION_KEYWORDS

    def test_named_state_filter_active(self, election_monitor):
        """Only named-state events surface (opinion pieces filtered out)."""
        state, is_named = election_monitor._monitor._extract_state_context(
            "National analysis: voting trends"
        )
        assert is_named is False

    def test_state_specific_detection(self, election_monitor):
        """Named state is correctly identified in election event text."""
        state, is_named = election_monitor._monitor._extract_state_context(
            "Georgia election deepfake case"
        )
        assert is_named is True
        assert state == "Georgia"


# ===========================================================================
# Domain 2 Coalition Email Router — 3 tests
# ===========================================================================


class TestDomain2CoalitionEmailRouter:
    """Tests for Domain2CoalitionEmailRouter wrapper."""

    # Test 1: Phase 2 domain keywords loaded correctly
    def test_phase2_keywords_loaded(self, email_router):
        """All Phase 2 domain keyword sets are merged into router."""
        phase2_domains = [
            "domain_48", "domain_49", "domain_50",
            "domain_51", "domain_54", "domain_57", "domain_59",
        ]
        for domain in phase2_domains:
            assert domain in email_router._router.DOMAIN_KEYWORDS, \
                f"Missing Phase 2 domain: {domain}"

    # Test 2: State persistence — messages_processed survives restart
    def test_state_persistence_message_count(self, email_router):
        """Email router message count persists across restarts."""
        email_router._router.state["messages_processed"] = 99
        email_router._router.state["messages_tagged"] = 42
        email_router._router._save_state()

        reloaded = email_router._router._load_state()
        assert reloaded["messages_processed"] == 99
        assert reloaded["messages_tagged"] == 42

    # Test 3: Not-authenticated returns graceful result
    def test_run_once_not_authenticated(self, email_router):
        """run_once() without Gmail auth returns not_authenticated (not exception)."""
        # Gmail disabled in base_config; should degrade gracefully
        result = email_router.run_once()
        assert result["status"] in ("not_authenticated", "no_new_emails", "error")
        assert "monitor" in result

    def test_domain_48_criminal_justice_keywords(self, email_router):
        """Domain 48 criminal justice keywords match correctly."""
        text = "criminal justice reform and mass incarceration policy"
        keywords = email_router._router.DOMAIN_KEYWORDS["domain_48"]["keywords"]
        assert any(kw in text for kw in keywords)

    def test_domain_49_environmental_keywords(self, email_router):
        """Domain 49 environmental keywords match correctly."""
        text = "EPA climate rollback threatens clean air standards"
        keywords = email_router._router.DOMAIN_KEYWORDS["domain_49"]["keywords"]
        assert any(kw in text for kw in keywords)

    def test_domain_50_lgbtq_keywords(self, email_router):
        """Domain 50 LGBTQ+ keywords match correctly."""
        text = "transgender rights non-discrimination policy"
        keywords = email_router._router.DOMAIN_KEYWORDS["domain_50"]["keywords"]
        assert any(kw in text for kw in keywords)

    def test_domain_51_campaign_finance_keywords(self, email_router):
        """Domain 51 campaign finance keywords match correctly."""
        text = "dark money super PAC spending citizens united"
        keywords = email_router._router.DOMAIN_KEYWORDS["domain_51"]["keywords"]
        assert any(kw in text for kw in keywords)

    def test_domain_54_youth_civic_keywords(self, email_router):
        """Domain 54 youth civic keywords match correctly."""
        text = "student voter campus polling place 26th amendment"
        keywords = email_router._router.DOMAIN_KEYWORDS["domain_54"]["keywords"]
        assert any(kw in text for kw in keywords)

    def test_domain_59_economic_precarity_keywords(self, email_router):
        """Domain 59 economic precarity keywords match correctly."""
        text = "child tax credit CTC poverty economic inequality"
        keywords = email_router._router.DOMAIN_KEYWORDS["domain_59"]["keywords"]
        assert any(kw in text for kw in keywords)

    def test_get_state_returns_router_state(self, email_router):
        """get_state() delegates to inner router state."""
        state = email_router.get_state()
        assert isinstance(state, dict)
        assert "messages_processed" in state


# ===========================================================================
# Parallel Runner Tests
# ===========================================================================


class TestParallelRunner:
    """Tests for run_all_monitors_parallel()."""

    @patch("phase_2_domain_trackers.Domain58SCOTUSMonitor.run_once")
    @patch("phase_2_domain_trackers.Domain39HHSTracker.run_once")
    @patch("phase_2_domain_trackers.Domain40ElectionMonitor.run_once")
    @patch("phase_2_domain_trackers.Domain2CoalitionEmailRouter.run_once")
    def test_parallel_runner_collects_all_results(
        self, mock_email, mock_election, mock_hhs, mock_scotus, base_config
    ):
        """Parallel runner collects results from all 4 monitors."""
        mock_scotus.return_value   = {"monitor": "domain_58_scotus",     "status": "pending",       "alert_sent": False}
        mock_hhs.return_value      = {"monitor": "domain_39_hhs",        "status": "no_new_items",  "alert_sent": False}
        mock_election.return_value = {"monitor": "domain_40_election",   "status": "no_new_events", "alert_sent": False}
        mock_email.return_value    = {"monitor": "coalition_email_router","status": "no_new_emails", "alert_sent": False}

        summary = run_all_monitors_parallel(config=base_config)

        assert "domain_58_scotus"      in summary
        assert "domain_39_hhs"         in summary
        assert "domain_40_election"    in summary
        assert "coalition_email_router" in summary
        assert "timestamp"             in summary
        assert "total_alerts_sent"     in summary
        assert "has_urgent"            in summary

    @patch("phase_2_domain_trackers.Domain58SCOTUSMonitor.run_once")
    @patch("phase_2_domain_trackers.Domain39HHSTracker.run_once")
    @patch("phase_2_domain_trackers.Domain40ElectionMonitor.run_once")
    @patch("phase_2_domain_trackers.Domain2CoalitionEmailRouter.run_once")
    def test_parallel_runner_counts_alerts(
        self, mock_email, mock_election, mock_hhs, mock_scotus, base_config
    ):
        """total_alerts_sent is sum of alert_sent=True across monitors."""
        mock_scotus.return_value   = {"monitor": "domain_58_scotus",     "status": "ruling_found",  "alert_sent": True}
        mock_hhs.return_value      = {"monitor": "domain_39_hhs",        "status": "new_guidance",  "alert_sent": True}
        mock_election.return_value = {"monitor": "domain_40_election",   "status": "no_new_events", "alert_sent": False}
        mock_email.return_value    = {"monitor": "coalition_email_router","status": "no_new_emails", "alert_sent": False}

        summary = run_all_monitors_parallel(config=base_config)

        assert summary["total_alerts_sent"] == 2

    @patch("phase_2_domain_trackers.Domain58SCOTUSMonitor.run_once")
    @patch("phase_2_domain_trackers.Domain39HHSTracker.run_once")
    @patch("phase_2_domain_trackers.Domain40ElectionMonitor.run_once")
    @patch("phase_2_domain_trackers.Domain2CoalitionEmailRouter.run_once")
    def test_parallel_runner_scotus_sets_has_urgent(
        self, mock_email, mock_election, mock_hhs, mock_scotus, base_config
    ):
        """has_urgent=True when SCOTUS ruling_found is detected."""
        mock_scotus.return_value   = {"monitor": "domain_58_scotus", "status": "ruling_found", "alert_sent": True}
        mock_hhs.return_value      = {"monitor": "domain_39_hhs",    "status": "no_new_items", "alert_sent": False}
        mock_election.return_value = {"monitor": "domain_40_election","status": "no_new_events","alert_sent": False}
        mock_email.return_value    = {"monitor": "coalition_email_router","status": "no_new_emails","alert_sent": False}

        summary = run_all_monitors_parallel(config=base_config)

        assert summary["has_urgent"] is True

    @patch("phase_2_domain_trackers.Domain58SCOTUSMonitor.run_once")
    @patch("phase_2_domain_trackers.Domain39HHSTracker.run_once")
    @patch("phase_2_domain_trackers.Domain40ElectionMonitor.run_once")
    @patch("phase_2_domain_trackers.Domain2CoalitionEmailRouter.run_once")
    def test_parallel_runner_error_isolation(
        self, mock_email, mock_election, mock_hhs, mock_scotus, base_config
    ):
        """One monitor error does not stop others from running."""
        mock_scotus.side_effect    = RuntimeError("Unexpected error in SCOTUS monitor")
        mock_hhs.return_value      = {"monitor": "domain_39_hhs",    "status": "no_new_items",  "alert_sent": False}
        mock_election.return_value = {"monitor": "domain_40_election","status": "no_new_events", "alert_sent": False}
        mock_email.return_value    = {"monitor": "coalition_email_router","status": "no_new_emails","alert_sent": False}

        summary = run_all_monitors_parallel(config=base_config)

        # Runner should collect results from all 4 keys even if SCOTUS errors
        assert "domain_39_hhs"         in summary
        assert "domain_40_election"    in summary
        assert "coalition_email_router" in summary
        # Errors list should contain the SCOTUS error
        assert any("domain_58_scotus" in e or "Unexpected" in e for e in summary.get("errors", []))


# ===========================================================================
# Config loader test
# ===========================================================================


class TestConfigLoader:
    """Test config loading with env var fallbacks."""

    def test_load_config_from_env_vars(self, monkeypatch):
        """Config falls back to env vars when file missing."""
        monkeypatch.setenv("DISCORD_WEBHOOK_URL", "https://discord.test/webhook/env")
        monkeypatch.setenv("GITHUB_TOKEN", "ghp_test_token_123")

        # Temporarily make config path unreachable
        with patch("phase_2_domain_trackers._CONFIG_PATH", Path("/nonexistent/config.json")):
            cfg = load_config()

        assert cfg.get("scotus_discord_webhook") == "https://discord.test/webhook/env"
        assert cfg.get("github_token") == "ghp_test_token_123"

    def test_load_config_sets_defaults(self, monkeypatch):
        """Env-var config includes all required interval defaults."""
        with patch("phase_2_domain_trackers._CONFIG_PATH", Path("/nonexistent/config.json")):
            cfg = load_config()

        assert cfg["scotus_polling_interval_minutes"] == 14
        assert cfg["hhs_polling_interval_minutes"] == 60
        assert cfg["election_polling_interval_minutes"] == 240
        assert cfg["email_polling_interval_minutes"] == 60


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
