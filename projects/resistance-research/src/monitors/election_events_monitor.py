#!/usr/bin/env python3
"""
Election Events & Voting Suppression Trigger Monitor

Monitors election protection and voting suppression news for Domain 40
(Surveillance/Election Integrity) and Domain 1 (Voting Rights) distribution
triggers. Checks FEC filing API, election protection RSS feeds, state
election officials, and voting rights news.

Usage:
  python3 election_events_monitor.py --run-now
  python3 election_events_monitor.py --continuous

Environment:
  DISCORD_WEBHOOK_URL: Discord webhook for alerts
  FEC_API_KEY: Federal Election Commission API key (optional)

Configuration (adoption-tracking-config.json):
  election_discord_webhook: Discord webhook URL
  election_polling_interval_minutes: Poll frequency (default: 240 = 4 hours)
"""

import os
import sys
import json
import logging
import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Optional, List, Tuple
import re
from dataclasses import dataclass, asdict
from time import sleep
from urllib.parse import urljoin

# Configure logging
log_dir = Path(__file__).parent.parent.parent / "phase-1-adoption" / "logs"
log_dir.mkdir(exist_ok=True, parents=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(log_dir / "election_monitor.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


@dataclass
class ElectionEvent:
    """Election event detection result."""
    title: str
    event_type: str  # "suppression", "ballot_measure", "election_admin", "voting_restriction"
    event_date: str
    event_url: str
    source: str  # "fec", "election_protection", "state_election", "news"
    state_context: Optional[str]  # Named state (not opinion pieces)
    domain_relevance: str  # "domain_1", "domain_40", "both"
    summary: Optional[str] = None
    confidence: float = 1.0
    is_named_state: bool = False  # Only alert on named states


class ElectionEventsMonitor:
    """Monitor for election suppression and voting integrity events."""

    # Data sources
    FEC_COMPLAINTS_API = "https://api.fec.gov/v1/violations/"
    ELECTION_PROTECTION_RSS = "https://www.electionprotection.org/feed/"
    VOTING_RIGHTS_NEWS = "https://votingrights.news/"  # Conceptual; check actual feeds
    COMMON_CAUSE_RSS = "https://www.commoncause.org/feed/"

    # State abbreviations for verification
    US_STATES = {
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
        "DC",
    }

    # Full state names
    STATE_NAMES = {
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
        "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
        "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
        "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
        "New Hampshire", "New Jersey", "New Mexico", "New York",
        "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
        "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
        "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
        "West Virginia", "Wisconsin", "Wyoming", "District of Columbia",
    }

    # Election suppression keywords
    SUPPRESSION_KEYWORDS = [
        "voter suppression",
        "voting restriction",
        "polling place closure",
        "voter id requirement",
        "purge",
        "ballot access",
        "election integrity",
        "election administration",
        "ballot measure",
        "voter registration",
        "early voting",
        "mail voting",
        "deepfake",
        "disinformation",
        "election security",
    ]

    # Monitoring state file
    STATE_FILE = Path(__file__).parent.parent.parent / "phase-1-adoption" / "data" / "election-monitor-state.json"

    def __init__(self, config: Optional[Dict] = None):
        """Initialize monitor with optional config override."""
        self.config = config or self._load_config()
        self.state = self._load_state()
        self.discord_webhook = (
            self.config.get("election_discord_webhook") or
            os.getenv("DISCORD_WEBHOOK_URL")
        )
        self.fec_api_key = os.getenv("FEC_API_KEY", "")
        self.polling_interval = self.config.get("election_polling_interval_minutes", 240)
        logger.info(f"Election Monitor initialized (polling every {self.polling_interval}m)")

    def _load_config(self) -> Dict:
        """Load configuration from adoption-tracking-config.json."""
        config_path = Path(__file__).parent.parent.parent / "phase-1-adoption" / "adoption-tracking-config.json"
        if config_path.exists():
            try:
                with open(config_path) as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load config: {e}; using defaults")
        return {}

    def _load_state(self) -> Dict:
        """Load monitoring state from file."""
        self.STATE_FILE.parent.mkdir(exist_ok=True, parents=True)
        if self.STATE_FILE.exists():
            try:
                with open(self.STATE_FILE, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load state: {e}; using defaults")
        return {
            "last_check": None,
            "items_seen": [],
            "alerts_sent": 0,
            "last_fec_check": None,
            "last_election_protection_check": None,
            "last_news_check": None,
        }

    def _save_state(self) -> None:
        """Persist monitoring state."""
        self.state["last_check"] = datetime.now(timezone.utc).isoformat()
        if len(self.state.get("items_seen", [])) > 200:
            self.state["items_seen"] = self.state["items_seen"][-200:]
        self.STATE_FILE.parent.mkdir(exist_ok=True, parents=True)
        with open(self.STATE_FILE, "w") as f:
            json.dump(self.state, f, indent=2)
        logger.debug(f"Saved state to {self.STATE_FILE}")

    def _extract_state_context(self, text: str) -> Tuple[Optional[str], bool]:
        """
        Extract state references from text.
        Returns: (state_name, is_named_state) where is_named_state=True only for specific state mentions
        """
        text_upper = text.upper()

        # Look for specific state names
        for state in self.STATE_NAMES:
            pattern = rf"\b{state}\b"
            if re.search(pattern, text, re.IGNORECASE):
                return state, True

        # Look for state abbreviations
        for abbrev in self.US_STATES:
            pattern = rf"\b{abbrev}\b"
            if re.search(pattern, text, re.IGNORECASE):
                return abbrev, True

        return None, False

    def _detect_event_type(self, title: str, content: str) -> str:
        """Detect what type of election event this is."""
        text = (title + " " + content).lower()

        type_keywords = {
            "suppression": ["suppression", "restriction", "closure", "voter id"],
            "ballot_measure": ["ballot", "amendment", "proposition", "measure"],
            "election_admin": ["election administration", "poll worker", "election official"],
            "voting_restriction": ["restrict", "limit", "reduce", "early vote", "mail"],
        }

        for event_type, keywords in type_keywords.items():
            if any(kw in text for kw in keywords):
                return event_type

        return "election_admin"  # Default

    def check_fec_complaints(self) -> List[ElectionEvent]:
        """
        Check FEC Violations API for election-related complaints.
        Returns: List of detected events
        """
        results = []
        try:
            logger.info("Checking FEC complaints API...")

            params = {
                "per_page": 50,
                "sort": "-issue_date",
            }
            if self.fec_api_key:
                params["api_key"] = self.fec_api_key

            response = requests.get(
                self.FEC_COMPLAINTS_API,
                params=params,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0 (Phase 2 tracking automation)"},
            )
            response.raise_for_status()

            data = response.json()
            violations = data.get("results", [])[:20]

            for violation in violations:
                title = violation.get("title", "")
                url = violation.get("url", "") or self.FEC_COMPLAINTS_API
                issue_date = violation.get("issue_date", "")
                description = violation.get("description", "")

                # Check for election-related keywords
                combined_text = f"{title} {description}".lower()
                if not any(kw in combined_text for kw in self.SUPPRESSION_KEYWORDS):
                    continue

                # Extract state
                state, is_named = self._extract_state_context(title + " " + description)

                # Skip opinion pieces (only named states)
                if not is_named:
                    continue

                # Dedup
                item_id = f"fec-{url}"
                if item_id in self.state.get("items_seen", []):
                    continue

                event_type = self._detect_event_type(title, description)
                event = ElectionEvent(
                    title=title,
                    event_type=event_type,
                    event_date=issue_date,
                    event_url=url,
                    source="fec",
                    state_context=state,
                    domain_relevance="domain_1",  # Voting rights
                    summary=description[:500] if description else None,
                    confidence=0.85,
                    is_named_state=is_named,
                )
                results.append(event)
                self.state.setdefault("items_seen", []).append(item_id)
                logger.info(f"Found: {title[:60]}... ({state})")

            logger.info(f"FEC check complete ({len(results)} new items)")
            self.state["last_fec_check"] = datetime.now(timezone.utc).isoformat()
            return results

        except requests.RequestException as e:
            logger.warning(f"Failed to check FEC API: {e}")
            return []

    def check_election_protection(self) -> List[ElectionEvent]:
        """
        Check Election Protection RSS for voting issues.
        Returns: List of detected events
        """
        results = []
        try:
            logger.info("Checking Election Protection...")
            response = requests.get(
                self.ELECTION_PROTECTION_RSS,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0 (Phase 2 tracking automation)"},
            )
            response.raise_for_status()

            # Parse RSS/HTML for items
            text = response.text
            # Simple extraction of article titles and links
            title_pattern = r'<(?:title|h[1-3])[^>]*>([^<]+)</(?:title|h[1-3])>'
            link_pattern = r'<link>([^<]+)</link>'

            titles = re.findall(title_pattern, text, re.IGNORECASE)
            links = re.findall(link_pattern, text, re.IGNORECASE)

            for i, title in enumerate(titles[:20]):
                title = title.strip()
                if not title or len(title) < 10:
                    continue

                # Check relevance
                combined = f"{title}".lower()
                if not any(kw in combined for kw in self.SUPPRESSION_KEYWORDS):
                    continue

                # Extract state
                state, is_named = self._extract_state_context(title)
                if not is_named:
                    continue

                # URL
                url = links[i] if i < len(links) else self.ELECTION_PROTECTION_RSS

                # Dedup
                item_id = f"ep-{url}"
                if item_id in self.state.get("items_seen", []):
                    continue

                event = ElectionEvent(
                    title=title,
                    event_type=self._detect_event_type(title, ""),
                    event_date=datetime.now(timezone.utc).isoformat(),
                    event_url=url,
                    source="election_protection",
                    state_context=state,
                    domain_relevance="domain_40",  # Election integrity
                    confidence=0.8,
                    is_named_state=is_named,
                )
                results.append(event)
                self.state.setdefault("items_seen", []).append(item_id)
                logger.info(f"Found: {title[:60]}... ({state})")

            logger.info(f"Election Protection check complete ({len(results)} new items)")
            self.state["last_election_protection_check"] = datetime.now(timezone.utc).isoformat()
            return results

        except requests.RequestException as e:
            logger.warning(f"Failed to check Election Protection: {e}")
            return []

    def check_voting_rights_news(self) -> List[ElectionEvent]:
        """
        Check for voting rights and election news (news aggregator pattern).
        Returns: List of detected events
        """
        results = []
        try:
            logger.info("Checking voting rights news...")

            # Common Cause RSS is a reliable voting rights source
            response = requests.get(
                self.COMMON_CAUSE_RSS,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0 (Phase 2 tracking automation)"},
            )
            response.raise_for_status()

            # Parse for voting rights content
            title_pattern = r'<title>([^<]+)</title>'
            link_pattern = r'<link>([^<]+)</link>'

            titles = re.findall(title_pattern, response.text)
            links = re.findall(link_pattern, response.text)

            for i, title in enumerate(titles[1:21]):  # Skip feed title
                title = title.strip()
                if not title or len(title) < 10:
                    continue

                # Check relevance
                combined = f"{title}".lower()
                if not any(kw in combined for kw in self.SUPPRESSION_KEYWORDS):
                    continue

                # Extract state
                state, is_named = self._extract_state_context(title)
                if not is_named:
                    continue

                url = links[i + 1] if i + 1 < len(links) else self.COMMON_CAUSE_RSS

                # Dedup
                item_id = f"voting-{url}"
                if item_id in self.state.get("items_seen", []):
                    continue

                event = ElectionEvent(
                    title=title,
                    event_type=self._detect_event_type(title, ""),
                    event_date=datetime.now(timezone.utc).isoformat(),
                    event_url=url,
                    source="news",
                    state_context=state,
                    domain_relevance="both",  # Affects both Domain 1 and 40
                    confidence=0.75,
                    is_named_state=is_named,
                )
                results.append(event)
                self.state.setdefault("items_seen", []).append(item_id)
                logger.info(f"Found: {title[:60]}... ({state})")

            logger.info(f"Voting rights news check complete ({len(results)} new items)")
            self.state["last_news_check"] = datetime.now(timezone.utc).isoformat()
            return results

        except requests.RequestException as e:
            logger.warning(f"Failed to check voting rights news: {e}")
            return []

    def run_check(self) -> List[ElectionEvent]:
        """
        Check all sources for election events.
        Returns: List of new election events
        """
        logger.info("=" * 60)
        logger.info("Election Events Monitor check cycle")
        logger.info("=" * 60)

        all_events = []

        # Check FEC
        all_events.extend(self.check_fec_complaints())

        # Check Election Protection
        all_events.extend(self.check_election_protection())

        # Check voting rights news
        all_events.extend(self.check_voting_rights_news())

        logger.info(f"Check cycle complete: {len(all_events)} new items")
        self._save_state()

        return all_events

    def send_alert(self, events: List[ElectionEvent]) -> bool:
        """
        Send alert via Discord.
        Returns: True if sent successfully
        """
        if not events or not self.discord_webhook:
            return False

        try:
            embeds = []

            # Separate by domain relevance
            domain_1_events = [e for e in events if e.domain_relevance in ("domain_1", "both")]
            domain_40_events = [e for e in events if e.domain_relevance in ("domain_40", "both")]

            # Create embeds for each event
            for event in events[:15]:  # Limit to 15
                field_value = (
                    f"**Type**: {event.event_type}\n"
                    f"**State**: {event.state_context or 'National'}\n"
                    f"**Source**: {event.source}\n"
                    f"**Confidence**: {event.confidence * 100:.0f}%"
                )

                embed = {
                    "title": event.title[:256],
                    "url": event.event_url,
                    "description": event.summary[:500] if event.summary else "Election event detected",
                    "color": 15158332,  # Red
                    "fields": [{"name": "Details", "value": field_value, "inline": False}],
                }
                embeds.append(embed)

            # Main alert embed
            alert_text = f"DOMAIN {', '.join(set(['1'] if domain_1_events else []) | set(['40'] if domain_40_events else []))} POSSIBLE TRIGGER"
            main_embed = {
                "title": alert_text,
                "description": f"Election event(s) detected ({len(events)} item(s))",
                "color": 15158332,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "footer": {"text": "Phase 2 Automation — election_events_monitor.py"},
            }
            embeds.insert(0, main_embed)

            payload = {"embeds": embeds}
            response = requests.post(
                self.discord_webhook,
                json=payload,
                timeout=10,
                headers={"User-Agent": "Phase 2 Election Monitor"},
            )
            response.raise_for_status()
            logger.info(f"Alert sent via Discord (HTTP {response.status_code})")
            self.state["alerts_sent"] += 1
            return True

        except requests.RequestException as e:
            logger.error(f"Failed to send alert: {e}")
            return False

    def run_continuous(self, duration_hours: Optional[int] = None):
        """
        Run monitor continuously in polling loop.
        Args:
            duration_hours: Stop after N hours (None = run indefinitely)
        """
        start_time = datetime.now(timezone.utc)
        logger.info(f"Starting continuous monitoring (interval={self.polling_interval}m)")

        try:
            while True:
                if duration_hours:
                    elapsed = (datetime.now(timezone.utc) - start_time).total_seconds() / 3600
                    if elapsed > duration_hours:
                        logger.info(f"Duration limit reached ({duration_hours}h); stopping")
                        break

                events = self.run_check()
                if events:
                    self.send_alert(events)
                    logger.info(f"Monitor found {len(events)} new election events; alert sent")

                logger.info(f"Next check in {self.polling_interval} minutes...")
                sleep(self.polling_interval * 60)

        except KeyboardInterrupt:
            logger.info("Monitor stopped by user")
            self._save_state()


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Election Events Monitor")
    parser.add_argument("--run-now", action="store_true", help="Run single check cycle")
    parser.add_argument("--continuous", action="store_true", help="Run continuous polling")
    parser.add_argument("--duration-hours", type=int, help="Stop after N hours (with --continuous)")
    parser.add_argument("--config", type=str, help="Config file path")

    args = parser.parse_args()

    config = None
    if args.config:
        try:
            with open(args.config) as f:
                config = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Failed to load config: {e}")
            sys.exit(1)

    monitor = ElectionEventsMonitor(config=config)

    if args.run_now:
        events = monitor.run_check()
        if events:
            monitor.send_alert(events)
            sys.exit(0)
        logger.info("No new election events found")
        sys.exit(1)

    elif args.continuous:
        monitor.run_continuous(duration_hours=args.duration_hours)
        sys.exit(0)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
