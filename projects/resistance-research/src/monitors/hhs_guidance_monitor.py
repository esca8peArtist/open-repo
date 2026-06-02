#!/usr/bin/env python3
"""
HHS Guidance Tracking Monitor

Monitors Federal Register notices and HHS website for Domain 39 (Healthcare
Disenrollment) and related June-July 2026 timeline events. Detects final rules,
interim final guidance, and key effective dates (June 1, Jan 27).

Usage:
  python3 hhs_guidance_monitor.py --run-now
  python3 hhs_guidance_monitor.py --continuous

Environment:
  SLACK_WEBHOOK_URL: Slack webhook for alerts
  DISCORD_WEBHOOK_URL: Discord webhook for alerts

Configuration (adoption-tracking-config.json):
  hhs_slack_webhook: Slack webhook URL
  hhs_discord_webhook: Discord webhook URL
  hhs_polling_interval_minutes: Poll frequency (default: 360 = 6 hours)
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

# Optional feedparser for RSS parsing
try:
    import feedparser
except ImportError:
    feedparser = None

# Configure logging
log_dir = Path(__file__).parent.parent.parent / "phase-1-adoption" / "logs"
log_dir.mkdir(exist_ok=True, parents=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(log_dir / "hhs_monitor.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


@dataclass
class HHSGuidance:
    """HHS guidance detection result."""
    title: str
    guidance_type: str  # "final_rule", "interim_guidance", "notice", "news"
    guidance_date: str
    guidance_url: str
    source: str  # "federal_register", "hhs.gov", "cms.gov"
    domain_relevance: str  # "domain_39", "domain_39_adjacent"
    summary: Optional[str] = None
    confidence: float = 1.0
    key_dates: Optional[List[str]] = None


class HHSGuidanceMonitor:
    """Monitor for HHS healthcare disenrollment guidance."""

    # Data sources
    FEDERAL_REGISTER_HEALTHCARE_RSS = (
        "https://www.federalregister.gov/documents/search.json?agencies=hhs&"
        "conditions[]=current_year&per_page=100"
    )
    HHS_NEWS_RSS = "https://www.hhs.gov/news/index.html"
    CMS_GUIDANCE = "https://www.cms.gov/newsroom"

    # Key terms and patterns
    DISENROLLMENT_KEYWORDS = [
        "disenrollment",
        "medicaid unwinding",
        "continuous enrollment",
        "coverage termination",
        "public charge",
        "non-citizen",
        "eligibility verification",
        "redetermination",
    ]

    GUIDANCE_TYPE_KEYWORDS = {
        "final_rule": ["final rule", "final regulation", "final guidance"],
        "interim_guidance": ["interim final rule", "interim guidance", "proposed rule"],
        "notice": ["notice", "guidance", "clarification"],
        "news": ["announcement", "news", "press release"],
    }

    # Key dates to watch
    KEY_DATES = [
        "June 1, 2026",
        "January 27, 2027",
        "May 31, 2026",
    ]

    # Monitoring state file
    STATE_FILE = Path(__file__).parent.parent.parent / "phase-1-adoption" / "data" / "hhs-monitor-state.json"

    def __init__(self, config: Optional[Dict] = None):
        """Initialize monitor with optional config override."""
        self.config = config or self._load_config()
        self.state = self._load_state()
        self.slack_webhook = (
            self.config.get("hhs_slack_webhook") or
            os.getenv("SLACK_WEBHOOK_URL")
        )
        self.discord_webhook = (
            self.config.get("hhs_discord_webhook") or
            os.getenv("DISCORD_WEBHOOK_URL")
        )
        self.polling_interval = self.config.get("hhs_polling_interval_minutes", 360)
        logger.info(f"HHS Monitor initialized (polling every {self.polling_interval}m)")

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
            "last_federal_register_check": None,
            "last_hhs_check": None,
            "last_cms_check": None,
        }

    def _save_state(self) -> None:
        """Persist monitoring state."""
        self.state["last_check"] = datetime.now(timezone.utc).isoformat()
        # Keep only last 200 items to avoid state file bloat
        if len(self.state.get("items_seen", [])) > 200:
            self.state["items_seen"] = self.state["items_seen"][-200:]
        self.STATE_FILE.parent.mkdir(exist_ok=True, parents=True)
        with open(self.STATE_FILE, "w") as f:
            json.dump(self.state, f, indent=2)
        logger.debug(f"Saved state to {self.STATE_FILE}")

    def _is_domain39_relevant(self, title: str, content: str) -> Tuple[bool, str]:
        """
        Determine if content is relevant to Domain 39.
        Returns: (is_relevant, relevance_level)
        """
        text = (title + " " + content).lower()

        # Check for direct relevance
        for keyword in self.DISENROLLMENT_KEYWORDS:
            if keyword in text:
                return True, "domain_39"

        # Check for adjacent relevance (healthcare policy but not direct disenrollment)
        adjacent_keywords = [
            "healthcare",
            "medicaid",
            "cms",
            "coverage",
            "enrollment",
            "health insurance",
        ]
        if any(kw in text for kw in adjacent_keywords):
            return True, "domain_39_adjacent"

        return False, ""

    def _extract_key_dates(self, text: str) -> List[str]:
        """Extract referenced key dates from text."""
        found_dates = []
        for date_str in self.KEY_DATES:
            if date_str.lower() in text.lower():
                found_dates.append(date_str)

        # Also look for ISO dates
        iso_pattern = r"\d{4}-\d{2}-\d{2}"
        for match in re.finditer(iso_pattern, text):
            found_dates.append(match.group(0))

        return list(set(found_dates))  # Deduplicate

    def _detect_guidance_type(self, title: str, content: str) -> str:
        """Detect what type of guidance this is."""
        text = (title + " " + content).lower()

        for gtype, keywords in self.GUIDANCE_TYPE_KEYWORDS.items():
            if any(kw in text for kw in keywords):
                return gtype

        return "notice"  # Default

    def check_federal_register(self) -> List[HHSGuidance]:
        """
        Check Federal Register for HHS healthcare notices.
        Returns: List of detected guidance
        """
        results = []
        try:
            logger.info("Checking Federal Register for healthcare notices...")
            response = requests.get(
                self.FEDERAL_REGISTER_HEALTHCARE_RSS,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0 (Phase 2 tracking automation)"},
            )
            response.raise_for_status()

            data = response.json()
            documents = data.get("results", [])[:25]  # Check first 25 results

            for doc in documents:
                title = doc.get("title", "")
                url = doc.get("html_url", "")
                publication_date = doc.get("publication_date", "")
                summary = doc.get("summary", "")

                # Check relevance
                is_relevant, relevance = self._is_domain39_relevant(title, summary)
                if not is_relevant:
                    continue

                # Check for deduplication
                item_id = f"fr-{url}"
                if item_id in self.state.get("items_seen", []):
                    continue

                # Extract details
                guidance_type = self._detect_guidance_type(title, summary)
                key_dates = self._extract_key_dates(title + " " + summary)

                guidance = HHSGuidance(
                    title=title,
                    guidance_type=guidance_type,
                    guidance_date=publication_date,
                    guidance_url=url,
                    source="federal_register",
                    domain_relevance=relevance,
                    summary=summary[:500] if summary else None,
                    confidence=0.9,
                    key_dates=key_dates if key_dates else None,
                )
                results.append(guidance)
                self.state.setdefault("items_seen", []).append(item_id)
                logger.info(f"Found: {title[:60]}...")

            logger.info(f"Federal Register check complete ({len(results)} new items)")
            self.state["last_federal_register_check"] = datetime.now(timezone.utc).isoformat()
            return results

        except requests.RequestException as e:
            logger.warning(f"Failed to check Federal Register: {e}")
            return []

    def check_hhs_newsroom(self) -> List[HHSGuidance]:
        """
        Check HHS newsroom for healthcare policy announcements.
        Returns: List of detected guidance
        """
        results = []
        try:
            logger.info("Checking HHS newsroom...")
            response = requests.get(
                self.HHS_NEWS_RSS,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0 (Phase 2 tracking automation)"},
            )
            response.raise_for_status()

            # Parse for healthcare-related news
            text = response.text
            lines = text.split("\n")

            # Look for article links and titles
            url_pattern = r'href=["\']([^"\']*newsroom[^"\']*)["\']'
            title_pattern = r'<(?:title|h[1-3])[^>]*>([^<]+)</(?:title|h[1-3])>'

            current_section = ""
            for i, line in enumerate(lines):
                title_match = re.search(title_pattern, line, re.IGNORECASE)
                if title_match:
                    current_section = title_match.group(1).strip()

                url_match = re.search(url_pattern, line)
                if url_match and current_section:
                    url = url_match.group(1)
                    if not url.startswith("http"):
                        url = urljoin("https://www.hhs.gov", url)

                    # Check relevance
                    is_relevant, relevance = self._is_domain39_relevant(current_section, "")
                    if not is_relevant:
                        continue

                    # Dedup
                    item_id = f"hhs-{url}"
                    if item_id in self.state.get("items_seen", []):
                        continue

                    guidance = HHSGuidance(
                        title=current_section,
                        guidance_type="news",
                        guidance_date=datetime.now(timezone.utc).isoformat(),
                        guidance_url=url,
                        source="hhs.gov",
                        domain_relevance=relevance,
                        confidence=0.75,
                    )
                    results.append(guidance)
                    self.state.setdefault("items_seen", []).append(item_id)

            logger.info(f"HHS newsroom check complete ({len(results)} new items)")
            self.state["last_hhs_check"] = datetime.now(timezone.utc).isoformat()
            return results

        except requests.RequestException as e:
            logger.warning(f"Failed to check HHS newsroom: {e}")
            return []

    def run_check(self) -> List[HHSGuidance]:
        """
        Check all sources for new HHS guidance.
        Returns: List of new guidance items
        """
        logger.info("=" * 60)
        logger.info("HHS Guidance Monitor check cycle")
        logger.info("=" * 60)

        all_guidance = []

        # Check Federal Register
        all_guidance.extend(self.check_federal_register())

        # Check HHS newsroom
        all_guidance.extend(self.check_hhs_newsroom())

        logger.info(f"Check cycle complete: {len(all_guidance)} new items")
        self._save_state()

        return all_guidance

    def send_alert(self, guidance_list: List[HHSGuidance], channel: str = "discord") -> bool:
        """
        Send alert via Discord or Slack.
        Args:
            guidance_list: List of HHSGuidance objects
            channel: "discord" or "slack"
        Returns: True if sent successfully
        """
        if not guidance_list:
            return False

        if channel == "discord" and not self.discord_webhook:
            logger.warning("No Discord webhook configured")
            return False
        if channel == "slack" and not self.slack_webhook:
            logger.warning("No Slack webhook configured")
            return False

        try:
            # Build message
            if channel == "discord":
                embeds = []
                for guidance in guidance_list[:10]:  # Limit to 10 embeds per message
                    field_value = (
                        f"**Type**: {guidance.guidance_type}\n"
                        f"**Source**: {guidance.source}\n"
                        f"**Confidence**: {guidance.confidence * 100:.0f}%"
                    )
                    if guidance.key_dates:
                        field_value += f"\n**Key Dates**: {', '.join(guidance.key_dates)}"

                    embed = {
                        "title": guidance.title[:256],
                        "url": guidance.guidance_url,
                        "description": guidance.summary[:500] if guidance.summary else "New HHS guidance detected",
                        "color": 16744192 if guidance.domain_relevance == "domain_39" else 16754432,  # Blue for direct, orange for adjacent
                        "fields": [{"name": "Details", "value": field_value, "inline": False}],
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                    }
                    embeds.append(embed)

                # Main alert embed
                main_embed = {
                    "title": f"DOMAIN 39 {'IMMEDIATE' if any(g.domain_relevance == 'domain_39' for g in guidance_list) else 'DECISION REQUIRED'}",
                    "description": f"New HHS healthcare guidance detected ({len(guidance_list)} item(s))",
                    "color": 15158332 if any(g.domain_relevance == "domain_39" for g in guidance_list) else 16776960,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "footer": {"text": "Phase 2 Automation — hhs_guidance_monitor.py"},
                }

                embeds.insert(0, main_embed)

                payload = {"embeds": embeds}
                response = requests.post(
                    self.discord_webhook,
                    json=payload,
                    timeout=10,
                    headers={"User-Agent": "Phase 2 HHS Monitor"},
                )
                response.raise_for_status()
                logger.info(f"Alert sent via Discord (HTTP {response.status_code})")

            else:  # Slack
                text = f"*DOMAIN 39 DECISION REQUIRED* - {len(guidance_list)} new HHS guidance items\n"
                for guidance in guidance_list[:5]:  # Show top 5 in Slack
                    text += f"\n• {guidance.title}\n  <{guidance.guidance_url}|View>\n"

                payload = {
                    "text": text,
                    "blocks": [
                        {
                            "type": "header",
                            "text": {"type": "plain_text", "text": "DOMAIN 39 HHS Guidance Alert"},
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"New guidance detected: {len(guidance_list)} item(s)",
                            },
                        },
                    ],
                }
                response = requests.post(
                    self.slack_webhook,
                    json=payload,
                    timeout=10,
                    headers={"User-Agent": "Phase 2 HHS Monitor"},
                )
                response.raise_for_status()
                logger.info(f"Alert sent via Slack (HTTP {response.status_code})")

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
                # Check for duration limit
                if duration_hours:
                    elapsed = (datetime.now(timezone.utc) - start_time).total_seconds() / 3600
                    if elapsed > duration_hours:
                        logger.info(f"Duration limit reached ({duration_hours}h); stopping")
                        break

                # Run check
                guidance_list = self.run_check()
                if guidance_list:
                    self.send_alert(guidance_list, channel="discord")
                    logger.info(f"HHS monitor found {len(guidance_list)} new items; alert sent")

                # Sleep before next check
                logger.info(f"Next check in {self.polling_interval} minutes...")
                sleep(self.polling_interval * 60)

        except KeyboardInterrupt:
            logger.info("Monitor stopped by user")
            self._save_state()


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="HHS Guidance Monitor")
    parser.add_argument("--run-now", action="store_true", help="Run single check cycle")
    parser.add_argument("--continuous", action="store_true", help="Run continuous polling")
    parser.add_argument("--duration-hours", type=int, help="Stop after N hours (with --continuous)")
    parser.add_argument("--config", type=str, help="Config file path")
    parser.add_argument("--channel", choices=["discord", "slack"], default="discord", help="Alert channel")

    args = parser.parse_args()

    # Load config if specified
    config = None
    if args.config:
        try:
            with open(args.config) as f:
                config = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Failed to load config: {e}")
            sys.exit(1)

    monitor = HHSGuidanceMonitor(config=config)

    if args.run_now:
        guidance_list = monitor.run_check()
        if guidance_list:
            monitor.send_alert(guidance_list, channel=args.channel)
            sys.exit(0)
        logger.info("No new guidance found")
        sys.exit(1)

    elif args.continuous:
        monitor.run_continuous(duration_hours=args.duration_hours)
        sys.exit(0)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
