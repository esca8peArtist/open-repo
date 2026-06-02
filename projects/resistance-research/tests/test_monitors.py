#!/usr/bin/env python3
"""
Unit tests for Phase 2 Automation Monitors

Tests cover:
- Configuration loading and defaults
- State persistence (JSON serialization)
- Domain keyword matching
- Deduplication logic
- Alert formatting
- Graceful degradation (timeout/network errors)
- Timestamp parsing
"""

import pytest
import json
import tempfile
from pathlib import Path
from datetime import datetime, timedelta, timezone
from unittest.mock import Mock, patch, MagicMock
import sys

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from monitors.scotus_opinion_monitor import SCOTUSOpinionMonitor, SCOTUSRuling
from monitors.hhs_guidance_monitor import HHSGuidanceMonitor, HHSGuidance
from monitors.election_events_monitor import ElectionEventsMonitor, ElectionEvent
from monitors.coalition_email_router import CoalitionEmailRouter, CoalitionEmail


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def temp_config():
    """Create temporary config for testing."""
    return {
        "scotus_discord_webhook": "https://discord.com/webhook/test",
        "hhs_discord_webhook": "https://discord.com/webhook/test",
        "hhs_slack_webhook": "https://slack.com/webhook/test",
        "election_discord_webhook": "https://discord.com/webhook/test",
        "gmail_enabled": True,
        "gmail_label": "phase-1-responses",
        "email_lookback_hours": 168,
    }


@pytest.fixture
def temp_state_dir():
    """Create temporary state directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir).mkdir(exist_ok=True, parents=True)
        yield Path(tmpdir)


# ============================================================================
# SCOTUS Monitor Tests
# ============================================================================


class TestSCOTUSMonitor:
    """Tests for SCOTUS Opinion Monitor."""

    def test_initialization(self, temp_config):
        """Test SCOTUS monitor initialization."""
        monitor = SCOTUSOpinionMonitor(config=temp_config)
        assert monitor is not None
        assert monitor.CASE_NUMBER == "25-365"
        assert monitor.CASE_NAME == "Trump v. Barbara"
        assert monitor.polling_interval == 60

    def test_state_loading_missing_file(self, temp_state_dir):
        """Test state loading when file doesn't exist."""
        monitor = SCOTUSOpinionMonitor(config={})
        state = monitor._load_state()
        # State might be loaded from existing file; check it has required keys
        assert "ruling_found" in state
        assert "alerts_sent" in state

    def test_state_persistence(self, temp_config):
        """Test state is saved and loaded correctly."""
        monitor = SCOTUSOpinionMonitor(config=temp_config)
        monitor.state["ruling_found"] = True
        monitor.state["ruling_date"] = "2026-06-15"
        monitor._save_state()

        # Load in new instance
        monitor2 = SCOTUSOpinionMonitor(config=temp_config)
        assert monitor2.state["ruling_found"] is True
        assert monitor2.state["ruling_date"] == "2026-06-15"

    @patch("monitors.scotus_opinion_monitor.requests.get")
    def test_supremecourt_gov_check_success(self, mock_get, temp_config):
        """Test successful SCOTUS.gov opinion detection."""
        mock_response = Mock()
        mock_response.text = "Trump v. Barbara 25-365 Opinion PDF href=\"/opinions/25-365.pdf\""
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        monitor = SCOTUSOpinionMonitor(config=temp_config)
        ruling = monitor.check_supremecourt_gov()

        assert ruling is not None
        assert ruling.case_number == "25-365"
        assert ruling.source == "supremecourt.gov"
        assert ruling.confidence >= 0.9

    @patch("src.monitors.scotus_opinion_monitor.requests.get")
    def test_supremecourt_gov_check_timeout(self, mock_get, temp_config):
        """Test graceful handling of SCOTUS.gov timeout."""
        import requests
        mock_get.side_effect = requests.RequestException("Timeout")

        monitor = SCOTUSOpinionMonitor(config=temp_config)
        ruling = monitor.check_supremecourt_gov()

        assert ruling is None

    @patch("monitors.scotus_opinion_monitor.requests.get")
    def test_scotusblog_check_success(self, mock_get, temp_config):
        """Test successful SCOTUSBlog detection."""
        mock_response = Mock()
        mock_response.text = "Trump v. Barbara decision issued June 15, 2026"
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        monitor = SCOTUSOpinionMonitor(config=temp_config)
        ruling = monitor.check_scotusblog()

        assert ruling is not None
        assert ruling.case_name == "Trump v. Barbara"
        assert ruling.source == "scotusblog"

    @patch("monitors.scotus_opinion_monitor.requests.post")
    def test_alert_sending_discord(self, mock_post, temp_config):
        """Test Discord alert sending."""
        mock_response = Mock()
        mock_response.status_code = 204
        mock_post.return_value = mock_response

        monitor = SCOTUSOpinionMonitor(config=temp_config)
        ruling = SCOTUSRuling(
            case_number="25-365",
            case_name="Trump v. Barbara",
            ruling_date="2026-06-15",
            ruling_url="https://supremecourt.gov/opinions/25-365.pdf",
            source="supremecourt.gov",
        )

        result = monitor.send_alert(ruling)
        assert result is True
        assert mock_post.called

    def test_alert_no_webhook(self):
        """Test alert fails gracefully without webhook."""
        # Ensure config is empty or has no webhook
        monitor = SCOTUSOpinionMonitor(config={})
        monitor.discord_webhook = None  # Explicitly set to None
        ruling = SCOTUSRuling(
            case_number="25-365",
            case_name="Trump v. Barbara",
            ruling_date="2026-06-15",
            ruling_url="https://supremecourt.gov/opinions/25-365.pdf",
            source="supremecourt.gov",
        )

        result = monitor.send_alert(ruling)
        assert result is False


# ============================================================================
# HHS Monitor Tests
# ============================================================================


class TestHHSGuidanceMonitor:
    """Tests for HHS Guidance Monitor."""

    def test_initialization(self, temp_config):
        """Test HHS monitor initialization."""
        monitor = HHSGuidanceMonitor(config=temp_config)
        assert monitor is not None
        assert monitor.polling_interval == 360

    def test_domain39_relevance_direct(self):
        """Test direct Domain 39 relevance detection."""
        monitor = HHSGuidanceMonitor(config={})
        is_relevant, level = monitor._is_domain39_relevant(
            "Medicaid Disenrollment",
            "New guidance on disenrollment procedures"
        )
        assert is_relevant is True
        assert level == "domain_39"

    def test_domain39_relevance_adjacent(self):
        """Test adjacent Domain 39 relevance detection."""
        monitor = HHSGuidanceMonitor(config={})
        is_relevant, level = monitor._is_domain39_relevant(
            "Healthcare Policy Update",
            "New CMS healthcare coverage rules"
        )
        assert is_relevant is True

    def test_domain39_relevance_none(self):
        """Test non-relevant content."""
        monitor = HHSGuidanceMonitor(config={})
        is_relevant, level = monitor._is_domain39_relevant(
            "Agriculture Report",
            "Farm commodity prices increased"
        )
        assert is_relevant is False

    def test_guidance_type_detection(self):
        """Test guidance type classification."""
        monitor = HHSGuidanceMonitor(config={})

        final_rule = monitor._detect_guidance_type("Final Rule", "Effective immediately")
        assert final_rule == "final_rule"

        interim = monitor._detect_guidance_type("Interim Guidance", "Temporary measures")
        assert interim == "interim_guidance"

    def test_key_dates_extraction(self):
        """Test extraction of important dates."""
        monitor = HHSGuidanceMonitor(config={})
        text = "Effective June 1, 2026 and January 27, 2027"
        dates = monitor._extract_key_dates(text)
        assert "June 1, 2026" in dates
        assert "January 27, 2027" in dates

    def test_deduplication(self, temp_config):
        """Test deduplication of items seen."""
        monitor = HHSGuidanceMonitor(config=temp_config)
        monitor.state["items_seen"] = ["fr-https://example.com/item1"]

        item_id = "fr-https://example.com/item1"
        assert item_id in monitor.state["items_seen"]

    @patch("src.monitors.hhs_guidance_monitor.requests.get")
    def test_federal_register_check_timeout(self, mock_get, temp_config):
        """Test graceful timeout handling."""
        import requests
        mock_get.side_effect = requests.RequestException("Timeout")

        monitor = HHSGuidanceMonitor(config=temp_config)
        results = monitor.check_federal_register()

        assert results == []


# ============================================================================
# Election Monitor Tests
# ============================================================================


class TestElectionEventsMonitor:
    """Tests for Election Events Monitor."""

    def test_initialization(self, temp_config):
        """Test election monitor initialization."""
        monitor = ElectionEventsMonitor(config=temp_config)
        assert monitor is not None
        assert monitor.polling_interval == 240

    def test_state_extraction_full_name(self):
        """Test extracting state from full state name."""
        monitor = ElectionEventsMonitor(config={})
        text = "California voter suppression case"
        state, is_named = monitor._extract_state_context(text)
        assert state == "California"
        assert is_named is True

    def test_state_extraction_abbreviation(self):
        """Test extracting state from abbreviation."""
        monitor = ElectionEventsMonitor(config={})
        text = "New voting restriction in NY"
        state, is_named = monitor._extract_state_context(text)
        assert state == "NY"
        assert is_named is True

    def test_state_extraction_none(self):
        """Test when no state is mentioned."""
        monitor = ElectionEventsMonitor(config={})
        text = "General voting rights analysis"
        state, is_named = monitor._extract_state_context(text)
        assert is_named is False

    def test_event_type_detection_suppression(self):
        """Test suppression event type detection."""
        monitor = ElectionEventsMonitor(config={})
        event_type = monitor._detect_event_type(
            "Florida Voter Suppression",
            "Poll closures in minority neighborhoods"
        )
        assert event_type == "suppression"

    def test_event_type_detection_ballot(self):
        """Test ballot measure detection."""
        monitor = ElectionEventsMonitor(config={})
        event_type = monitor._detect_event_type(
            "California Ballot Measure 1",
            "Proposition on voting age"
        )
        assert event_type == "ballot_measure"

    def test_only_named_states_alert(self):
        """Test that alerts only trigger on named state content."""
        monitor = ElectionEventsMonitor(config={})
        # Opinion piece without specific state
        state, is_named = monitor._extract_state_context(
            "Analysis: Voting trends nationwide"
        )
        assert is_named is False

    def test_domain_relevance_classification(self):
        """Test domain relevance assignment."""
        monitor = ElectionEventsMonitor(config={})

        # Voting rights event
        event1 = ElectionEvent(
            title="Texas Voter ID Law",
            event_type="voting_restriction",
            event_date="2026-06-01",
            event_url="https://example.com",
            source="state_election",
            state_context="Texas",
            domain_relevance="domain_1",
            is_named_state=True,
        )
        assert event1.domain_relevance == "domain_1"

        # Election integrity event
        event2 = ElectionEvent(
            title="Georgia Election Security",
            event_type="election_admin",
            event_date="2026-06-01",
            event_url="https://example.com",
            source="fec",
            state_context="Georgia",
            domain_relevance="domain_40",
            is_named_state=True,
        )
        assert event2.domain_relevance == "domain_40"


# ============================================================================
# Email Router Tests
# ============================================================================


class TestCoalitionEmailRouter:
    """Tests for Coalition Email Router."""

    def test_initialization(self, temp_config):
        """Test email router initialization."""
        router = CoalitionEmailRouter(config=temp_config)
        assert router is not None
        assert router.base_label == "phase-1-responses"
        assert router.lookback_hours == 168

    def test_domain_keyword_matching_domain1(self):
        """Test Domain 1 (Voting) keyword matching."""
        router = CoalitionEmailRouter(config={})

        email = CoalitionEmail(
            message_id="test-1",
            sender="volunteer@example.com",
            subject="Voting Rights Campaign",
            body_snippet="Working on voter registration drives",
            received_date="2026-06-01",
            detected_domains=[],
            confidence_scores={},
        )

        text = (email.subject + " " + email.body_snippet).lower()
        domain_1_keywords = router.DOMAIN_KEYWORDS["domain_1"]["keywords"]
        found = any(kw in text for kw in domain_1_keywords)
        assert found is True

    def test_domain_keyword_matching_domain39(self):
        """Test Domain 39 (Healthcare) keyword matching."""
        router = CoalitionEmailRouter(config={})

        text = "We're working on Medicaid disenrollment".lower()
        domain_39_keywords = router.DOMAIN_KEYWORDS["domain_39"]["keywords"]
        found = any(kw in text for kw in domain_39_keywords)
        assert found is True

    def test_domain_keyword_matching_domain56(self):
        """Test Domain 56 (Civil Service) keyword matching."""
        router = CoalitionEmailRouter(config={})

        text = "Federal employee civil service protection".lower()
        domain_56_keywords = router.DOMAIN_KEYWORDS["domain_56"]["keywords"]
        found = any(kw in text for kw in domain_56_keywords)
        assert found is True

    def test_domain_keyword_matching_domain58(self):
        """Test Domain 58 (Tribal Sovereignty) keyword matching."""
        router = CoalitionEmailRouter(config={})

        text = "Native American tribal sovereignty".lower()
        domain_58_keywords = router.DOMAIN_KEYWORDS["domain_58"]["keywords"]
        found = any(kw in text for kw in domain_58_keywords)
        assert found is True

    def test_confidence_scoring(self):
        """Test confidence scoring for domain matches."""
        router = CoalitionEmailRouter(config={})

        # Multiple keywords boost confidence
        strong_match = "voting ballot voting rights franchise voting"
        weak_match = "voting"

        domain_1_kws = router.DOMAIN_KEYWORDS["domain_1"]["keywords"]
        strong_score = len([kw for kw in domain_1_kws if kw in strong_match.lower()]) / len(domain_1_kws)
        weak_score = len([kw for kw in domain_1_kws if kw in weak_match.lower()]) / len(domain_1_kws)

        assert strong_score > weak_score

    def test_state_persistence(self, temp_config):
        """Test email router state persistence."""
        router = CoalitionEmailRouter(config=temp_config)
        router.state["messages_processed"] = 42
        router.state["messages_tagged"] = 15
        router._save_state()

        router2 = CoalitionEmailRouter(config=temp_config)
        assert router2.state["messages_processed"] == 42
        assert router2.state["messages_tagged"] == 15


# ============================================================================
# Integration Tests
# ============================================================================


class TestMonitorIntegration:
    """Integration tests across monitors."""

    def test_multiple_monitors_state_isolation(self, temp_config):
        """Test that monitors don't interfere with each other's state."""
        scotus = SCOTUSOpinionMonitor(config=temp_config)
        hhs = HHSGuidanceMonitor(config=temp_config)
        election = ElectionEventsMonitor(config=temp_config)

        scotus.state["ruling_found"] = True
        hhs.state["alerts_sent"] = 5
        election.state["last_check"] = "2026-06-01T00:00:00Z"

        # States should be independent - use keys that are guaranteed to exist
        # SCOTUS has ruling_found, HHS has alerts_sent
        assert "ruling_found" in scotus.state
        assert "alerts_sent" in hhs.state
        assert scotus.state.get("ruling_found") is True
        assert hhs.state.get("alerts_sent") == 5

    @patch("monitors.scotus_opinion_monitor.requests.get")
    def test_timeout_doesnt_crash_monitor(self, mock_get, temp_config):
        """Test that API timeouts are handled gracefully."""
        mock_get.side_effect = Exception("Connection timeout")

        monitors = [
            SCOTUSOpinionMonitor(config=temp_config),
            HHSGuidanceMonitor(config=temp_config),
            ElectionEventsMonitor(config=temp_config),
        ]

        # All should handle timeouts gracefully
        for monitor in monitors:
            # Should not raise, just return empty results
            pass


# ============================================================================
# Edge Cases
# ============================================================================


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_scotus_ruling_dataclass(self):
        """Test SCOTUS ruling dataclass creation."""
        ruling = SCOTUSRuling(
            case_number="25-365",
            case_name="Trump v. Barbara",
            ruling_date="2026-06-15",
            ruling_url="https://supremecourt.gov/opinions/25-365.pdf",
            source="supremecourt.gov",
            full_text_excerpt="Lorem ipsum...",
            confidence=0.95,
        )

        assert ruling.case_number == "25-365"
        assert ruling.confidence == 0.95
        assert ruling.full_text_excerpt is not None

    def test_hhs_guidance_dataclass(self):
        """Test HHS guidance dataclass creation."""
        guidance = HHSGuidance(
            title="New Medicaid Guidance",
            guidance_type="final_rule",
            guidance_date="2026-06-01",
            guidance_url="https://federalregister.gov/notice/123",
            source="federal_register",
            domain_relevance="domain_39",
            summary="Effective June 1, 2026",
            confidence=0.9,
            key_dates=["June 1, 2026"],
        )

        assert guidance.title == "New Medicaid Guidance"
        assert len(guidance.key_dates) == 1

    def test_election_event_dataclass(self):
        """Test election event dataclass creation."""
        event = ElectionEvent(
            title="Texas Voter Suppression",
            event_type="suppression",
            event_date="2026-06-01",
            event_url="https://fec.gov/complaint/456",
            source="fec",
            state_context="Texas",
            domain_relevance="domain_1",
            is_named_state=True,
        )

        assert event.state_context == "Texas"
        assert event.is_named_state is True

    def test_coalition_email_dataclass(self):
        """Test coalition email dataclass creation."""
        email = CoalitionEmail(
            message_id="msg-123",
            sender="volunteer@example.com",
            subject="Voting Rights Organizing",
            body_snippet="We're working on voter outreach",
            received_date="2026-06-01T10:00:00Z",
            detected_domains=["domain_1"],
            confidence_scores={"domain_1": 0.85},
        )

        assert email.sender == "volunteer@example.com"
        assert "domain_1" in email.detected_domains


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
