#!/usr/bin/env python3
"""
Trump v. Barbara SCOTUS Opinion Monitor

Continuously monitors for Trump v. Barbara (No. 25-365) Supreme Court ruling.
Polls SCOTUS opinions API, SCOTUSBlog RSS, and NARF Tracker during court term
(June-July 2026). Triggers Domain 58 (Tribal Sovereignty/Birthright Citizenship)
rapid-response workflow upon ruling issuance.

Usage:
  python3 scotus_opinion_monitor.py --run-now
  python3 scotus_opinion_monitor.py --continuous

Environment:
  DISCORD_WEBHOOK_URL: Discord webhook for ruling alerts
  GITHUB_TOKEN: GitHub token for Gist update (optional)

Configuration (adoption-tracking-config.json):
  scotus_discord_webhook: Discord webhook URL
  scotus_polling_interval_minutes: Poll frequency (default: 60)
  scotus_case_number: Docket number (default: 25-365)
"""

import os
import sys
import json
import logging
import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Optional, Tuple, List
import re
from dataclasses import dataclass, asdict
from time import sleep

# Optional feedparser for RSS parsing (not used in SCOTUS, but good to have)
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
        logging.FileHandler(log_dir / "scotus_monitor.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


@dataclass
class SCOTUSRuling:
    """SCOTUS ruling detection result."""
    case_number: str
    case_name: str
    ruling_date: str
    ruling_url: str
    source: str  # "supremecourt.gov", "scotusblog", "narf"
    full_text_excerpt: Optional[str] = None
    confidence: float = 1.0


class SCOTUSOpinionMonitor:
    """Monitor for Trump v. Barbara ruling on multiple sources."""

    # Case identifiers
    CASE_NUMBER = "25-365"
    CASE_NAME = "Trump v. Barbara"
    DOCKET_URL = "https://www.supremecourt.gov/docket/25-365"

    # SCOTUS sources
    SUPREMECOURT_API = "https://www.supremecourt.gov/opinions/"
    SCOTUSBLOG_CASE = "https://www.scotusblog.com/case-files/cases/trump-v-barbara/"
    NARF_TRACKER = "https://narf.org/legal/indian-law-tracker/"

    # Monitoring state file
    STATE_FILE = Path(__file__).parent.parent.parent / "phase-1-adoption" / "data" / "scotus-monitor-state.json"

    def __init__(self, config: Optional[Dict] = None):
        """Initialize monitor with optional config override."""
        self.config = config or self._load_config()
        self.state = self._load_state()
        self.discord_webhook = (
            self.config.get("scotus_discord_webhook") or
            os.getenv("DISCORD_WEBHOOK_URL")
        )
        self.polling_interval = self.config.get("scotus_polling_interval_minutes", 60)
        self.github_token = os.getenv("GITHUB_TOKEN")
        logger.info(f"SCOTUS Monitor initialized (polling every {self.polling_interval}m)")

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
            "ruling_found": False,
            "ruling_date": None,
            "ruling_url": None,
            "ruling_source": None,
            "alerts_sent": 0,
            "last_scotusblog_check": None,
            "last_narf_check": None,
        }

    def _save_state(self) -> None:
        """Persist monitoring state."""
        self.state["last_check"] = datetime.now(timezone.utc).isoformat()
        self.STATE_FILE.parent.mkdir(exist_ok=True, parents=True)
        with open(self.STATE_FILE, "w") as f:
            json.dump(self.state, f, indent=2)
        logger.debug(f"Saved state to {self.STATE_FILE}")

    def check_supremecourt_gov(self) -> Optional[SCOTUSRuling]:
        """
        Check SCOTUS website for recent opinions.
        Returns: SCOTUSRuling or None
        """
        try:
            logger.info("Checking supremecourt.gov for opinions...")
            response = requests.get(
                "https://www.supremecourt.gov/opinions/slipopinion/",
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0 (Phase 2 tracking automation)"},
            )
            response.raise_for_status()

            # Parse for Trump v. Barbara mentions
            patterns = [
                rf"Trump\s+v\.\s+Barbara.*?25-365",
                r"25-365.*?Trump\s+v\.\s+Barbara",
                r"Trump.*?Barbara.*?25-365",
            ]

            for pattern in patterns:
                if re.search(pattern, response.text, re.IGNORECASE | re.DOTALL):
                    # Look for PDF link
                    pdf_pattern = r'href=["\']([^"\']*\.pdf)["\']'
                    matches = re.finditer(pdf_pattern, response.text)
                    for match in matches:
                        pdf_url = match.group(1)
                        if "25-365" in response.text[max(0, match.start() - 200) : match.end() + 200]:
                            if not pdf_url.startswith("http"):
                                pdf_url = "https://www.supremecourt.gov" + pdf_url
                            logger.info(f"Found ruling on supremecourt.gov: {pdf_url}")
                            return SCOTUSRuling(
                                case_number=self.CASE_NUMBER,
                                case_name=self.CASE_NAME,
                                ruling_date=datetime.now(timezone.utc).isoformat(),
                                ruling_url=pdf_url,
                                source="supremecourt.gov",
                                confidence=0.95,
                            )

            return None

        except requests.RequestException as e:
            logger.warning(f"Failed to check supremecourt.gov: {e}")
            return None

    def check_scotusblog(self) -> Optional[SCOTUSRuling]:
        """
        Check SCOTUSBlog for case updates (live blog format).
        Returns: SCOTUSRuling or None
        """
        try:
            logger.info("Checking SCOTUSBlog for updates...")
            response = requests.get(
                self.SCOTUSBLOG_CASE,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0 (Phase 2 tracking automation)"},
            )
            response.raise_for_status()

            # Look for decision markers
            decision_markers = [
                "decision issued",
                "ruling handed down",
                "opinion released",
                "court has decided",
                "majority opinion",
                "decision today",
            ]

            text_lower = response.text.lower()
            if any(marker in text_lower for marker in decision_markers):
                # Extract decision date if present
                date_patterns = [
                    r"(\w+\s+\d{1,2},?\s+20\d{2})",  # June 15, 2026
                    r"(\d{4}-\d{2}-\d{2})",  # 2026-06-15
                ]
                decision_date = None
                for pattern in date_patterns:
                    match = re.search(pattern, response.text)
                    if match:
                        decision_date = match.group(1)
                        break

                logger.info(f"Found decision markers on SCOTUSBlog")
                return SCOTUSRuling(
                    case_number=self.CASE_NUMBER,
                    case_name=self.CASE_NAME,
                    ruling_date=decision_date or datetime.now(timezone.utc).isoformat(),
                    ruling_url=self.SCOTUSBLOG_CASE,
                    source="scotusblog",
                    confidence=0.85,
                )

            return None

        except requests.RequestException as e:
            logger.warning(f"Failed to check SCOTUSBlog: {e}")
            return None

    def check_narf_tracker(self) -> Optional[SCOTUSRuling]:
        """
        Check NARF Indian Law Tracker for case updates.
        Returns: SCOTUSRuling or None
        """
        try:
            logger.info("Checking NARF tracker for updates...")
            response = requests.get(
                self.NARF_TRACKER,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0 (Phase 2 tracking automation)"},
            )
            response.raise_for_status()

            # Look for Trump v. Barbara mentions with decision indicators
            decision_keywords = ["decided", "affirmed", "reversed", "remanded", "opinion"]
            text = response.text.lower()

            if "trump" in text and "barbara" in text and any(kw in text for kw in decision_keywords):
                logger.info("Found case update on NARF tracker")
                return SCOTUSRuling(
                    case_number=self.CASE_NUMBER,
                    case_name=self.CASE_NAME,
                    ruling_date=datetime.now(timezone.utc).isoformat(),
                    ruling_url=self.NARF_TRACKER,
                    source="narf",
                    confidence=0.75,
                )

            return None

        except requests.RequestException as e:
            logger.warning(f"Failed to check NARF tracker: {e}")
            return None

    def run_check(self) -> Optional[SCOTUSRuling]:
        """
        Check all sources for ruling. Returns ruling if found on any source.
        Prioritizes high-confidence sources.
        """
        logger.info("=" * 60)
        logger.info("SCOTUS Monitor check cycle")
        logger.info("=" * 60)

        # Check sources in priority order
        ruling = self.check_supremecourt_gov()
        if ruling:
            logger.info(f"RULING FOUND (supremecourt.gov, confidence={ruling.confidence})")
            return ruling

        ruling = self.check_scotusblog()
        if ruling:
            logger.info(f"RULING FOUND (scotusblog, confidence={ruling.confidence})")
            return ruling

        ruling = self.check_narf_tracker()
        if ruling:
            logger.info(f"RULING FOUND (narf, confidence={ruling.confidence})")
            return ruling

        logger.info("No ruling found; case still pending")
        self._save_state()
        return None

    def send_alert(self, ruling: SCOTUSRuling) -> bool:
        """
        Send alert via Discord webhook.
        Returns: True if sent successfully
        """
        if not self.discord_webhook:
            logger.warning("No Discord webhook configured; alert not sent")
            return False

        try:
            # Build alert message
            embed = {
                "title": f"DOMAIN 58 IMMEDIATE: {ruling.case_name} Ruling Issued",
                "description": f"Supreme Court ruling in {ruling.case_name} (Docket {ruling.case_number}) has been issued.",
                "color": 15158332,  # Red
                "fields": [
                    {"name": "Case", "value": f"{ruling.case_name} ({ruling.case_number})", "inline": False},
                    {"name": "Ruling Date", "value": ruling.ruling_date, "inline": True},
                    {"name": "Source", "value": ruling.source, "inline": True},
                    {"name": "Confidence", "value": f"{ruling.confidence * 100:.0f}%", "inline": True},
                    {"name": "Opinion URL", "value": f"[Read Opinion]({ruling.ruling_url})", "inline": False},
                    {
                        "name": "Distribution Routing",
                        "value": "Domain 58 (Tribal Sovereignty/Birthright Citizenship) - Execute Phase 2 rapid-response",
                        "inline": False,
                    },
                    {"name": "Action Required", "value": "Immediate distribution of Domain 58 materials via CHECKIN.md routing", "inline": False},
                ],
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "footer": {"text": "Phase 2 Automation — scotus_opinion_monitor.py"},
            }

            payload = {"embeds": [embed]}

            response = requests.post(
                self.discord_webhook,
                json=payload,
                timeout=10,
                headers={"User-Agent": "Phase 2 SCOTUS Monitor"},
            )
            response.raise_for_status()

            logger.info(f"Alert sent via Discord (HTTP {response.status_code})")
            self.state["alerts_sent"] += 1
            return True

        except requests.RequestException as e:
            logger.error(f"Failed to send Discord alert: {e}")
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
                ruling = self.run_check()
                if ruling and not self.state["ruling_found"]:
                    self.state["ruling_found"] = True
                    self.state["ruling_date"] = ruling.ruling_date
                    self.state["ruling_url"] = ruling.ruling_url
                    self.state["ruling_source"] = ruling.source
                    self.send_alert(ruling)
                    self._save_state()
                    logger.info("SCOTUS monitor detected ruling; alert sent")

                # Sleep before next check
                logger.info(f"Next check in {self.polling_interval} minutes...")
                sleep(self.polling_interval * 60)

        except KeyboardInterrupt:
            logger.info("Monitor stopped by user")
            self._save_state()


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="SCOTUS Opinion Monitor")
    parser.add_argument("--run-now", action="store_true", help="Run single check cycle")
    parser.add_argument("--continuous", action="store_true", help="Run continuous polling")
    parser.add_argument("--duration-hours", type=int, help="Stop after N hours (with --continuous)")
    parser.add_argument("--config", type=str, help="Config file path")

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

    monitor = SCOTUSOpinionMonitor(config=config)

    if args.run_now:
        ruling = monitor.run_check()
        if ruling:
            monitor.send_alert(ruling)
            sys.exit(0)
        sys.exit(1)

    elif args.continuous:
        monitor.run_continuous(duration_hours=args.duration_hours)
        sys.exit(0)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
