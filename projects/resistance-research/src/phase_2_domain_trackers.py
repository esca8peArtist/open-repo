#!/usr/bin/env python3
"""
Phase 2 Domain-Specific Tracking Automation — v1.0
June 2, 2026

Unified module exposing four domain-specific monitor classes for parallel
operation alongside the Phase 1 Gist-polling workflow. Designed to be imported
by phase-1-adoption-tracking-script.py and run via concurrent.futures so each
monitor operates independently without blocking the others.

Classes
-------
Domain58SCOTUSMonitor
    Wraps SCOTUSOpinionMonitor. Polls supremecourt.gov, SCOTUSBlog, and the
    NARF Indian Law Tracker every <15 minutes for the Trump v. Barbara (25-365)
    ruling. Fires a Discord embed-alert on first detection.

Domain39HHSTracker
    Wraps HHSGuidanceMonitor. Polls Federal Register JSON API and HHS newsroom
    hourly for healthcare disenrollment and Medicaid-related rules/guidance.
    Sends Discord (primary) or Slack (secondary) alert on new items.

Domain40ElectionMonitor
    Wraps ElectionEventsMonitor. Polls FEC Violations API, Election Protection
    RSS, and Common Cause RSS every 4 hours for election/deepfake/suppression
    events. Only surfaces items that name a specific US state.

CoalitionEmailRouter
    Wraps CoalitionEmailRouter. Syncs Gmail label phase-1-responses hourly,
    applies sub-labels (phase-1-responses/domain_39 etc.) based on keyword
    scoring, and writes a routing report to CHECKIN.md on new tags.

Parallel runner
---------------
run_all_monitors_parallel(config) → Dict[str, Any]
    Launches all four monitors in a ThreadPoolExecutor, collects results, and
    returns a merged summary dict. Intended to be called from the Phase 1
    adoption-tracking main loop.

Usage
-----
  python3 src/phase_2_domain_trackers.py --run-now
  python3 src/phase_2_domain_trackers.py --check-status
  python3 src/phase_2_domain_trackers.py --continuous --duration-hours 24

Environment variables (all optional, override config file values)
-----------------------------------------------------------------
  DISCORD_WEBHOOK_URL       Shared fallback webhook for all monitors
  SLACK_WEBHOOK_URL         Slack fallback for HHS monitor
  GITHUB_TOKEN              For Gist metadata in SCOTUS alert
  FEC_API_KEY               FEC Violations API (raises rate limit from 20 to 1000/hr)
  GMAIL_CREDENTIALS_JSON    Path to Gmail OAuth2 credentials.json

Configuration (phase-1-adoption/adoption-tracking-config.json)
-------------------------------------------------------------
  scotus_discord_webhook          str   Discord webhook for SCOTUS alerts
  scotus_polling_interval_minutes int   Default 14 (sub-15-minute requirement)
  hhs_discord_webhook             str   Discord webhook for HHS alerts
  hhs_slack_webhook               str   Slack webhook for HHS alerts (fallback)
  hhs_polling_interval_minutes    int   Default 60 (hourly during comment windows)
  election_discord_webhook        str   Discord webhook for election alerts
  election_polling_interval_minutes int Default 240 (4 hours)
  gmail_enabled                   bool  Enable email router
  gmail_credentials               str   Path to OAuth2 credentials.json
  gmail_label                     str   Base label (default: phase-1-responses)
  email_lookback_hours            int   Default 168 (1 week)
  email_polling_interval_minutes  int   Default 60 (hourly)
"""

import os
import sys
import json
import logging
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

_SRC_DIR = Path(__file__).parent.resolve()
_PROJ_DIR = _SRC_DIR.parent.resolve()
_PHASE1_DIR = _PROJ_DIR / "phase-1-adoption"
_DATA_DIR = _PHASE1_DIR / "data"
_LOG_DIR = _PHASE1_DIR / "logs"
_CONFIG_PATH = _PHASE1_DIR / "adoption-tracking-config.json"
_CHECKIN_PATH = _PROJ_DIR / "CHECKIN.md"

# Ensure directories exist at module load time
_DATA_DIR.mkdir(parents=True, exist_ok=True)
_LOG_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(_LOG_DIR / "phase2_domain_trackers.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Internal imports — monitors package
# ---------------------------------------------------------------------------

sys.path.insert(0, str(_SRC_DIR))

from monitors.scotus_opinion_monitor import SCOTUSOpinionMonitor, SCOTUSRuling
from monitors.hhs_guidance_monitor import HHSGuidanceMonitor, HHSGuidance
from monitors.election_events_monitor import ElectionEventsMonitor, ElectionEvent
from monitors.coalition_email_router import CoalitionEmailRouter, CoalitionEmail

# ---------------------------------------------------------------------------
# Config loader
# ---------------------------------------------------------------------------


def load_config() -> Dict:
    """Load from JSON file; fall back to environment variables."""
    if _CONFIG_PATH.exists():
        try:
            with open(_CONFIG_PATH) as f:
                cfg = json.load(f)
            logger.info(f"Config loaded: {_CONFIG_PATH}")
            return cfg
        except (json.JSONDecodeError, IOError) as exc:
            logger.warning(f"Config load error ({exc}); using environment variables")

    return {
        "github_token":                    os.getenv("GITHUB_TOKEN", ""),
        "github_username":                 os.getenv("GITHUB_USERNAME", "esca8peArtist"),
        "gmail_enabled":                   bool(os.getenv("GMAIL_CREDENTIALS_JSON")),
        "gmail_credentials":               os.getenv("GMAIL_CREDENTIALS_JSON", ""),
        "gmail_label":                     os.getenv("GMAIL_LABEL", "phase-1-responses"),
        "email_lookback_hours":            168,
        "email_polling_interval_minutes":  60,
        "scotus_discord_webhook":          os.getenv("DISCORD_WEBHOOK_URL", ""),
        "scotus_polling_interval_minutes": 14,
        "hhs_discord_webhook":             os.getenv("DISCORD_WEBHOOK_URL", ""),
        "hhs_slack_webhook":               os.getenv("SLACK_WEBHOOK_URL", ""),
        "hhs_polling_interval_minutes":    60,
        "election_discord_webhook":        os.getenv("DISCORD_WEBHOOK_URL", ""),
        "election_polling_interval_minutes": 240,
        "phase1_start_date":               "2026-05-28",
    }


# ---------------------------------------------------------------------------
# Domain 58 — SCOTUS Monitor wrapper
# ---------------------------------------------------------------------------


class Domain58SCOTUSMonitor:
    """
    Wrapper around SCOTUSOpinionMonitor for integration into the Phase 2
    automation suite.

    Key constraints:
    - Polling interval: 14 minutes (sub-15-minute requirement for <15 min alert)
    - Single-shot mode for parallel runner compatibility
    - Discord embed alert fires once on first detection; subsequent checks skip
      if ruling_found is already True in state

    Thread safety: Each instance maintains its own state file; safe to run in
    a ThreadPoolExecutor alongside other monitors.
    """

    DOMAIN = "domain_58"
    LABEL = "Trump v. Barbara (SCOTUS)"
    DEFAULT_POLLING_INTERVAL = 14  # minutes — sub-15-minute SLA

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or load_config()
        # Force 14-minute interval unless explicitly overridden
        self.config.setdefault("scotus_polling_interval_minutes", self.DEFAULT_POLLING_INTERVAL)
        self._monitor = SCOTUSOpinionMonitor(config=self.config)
        logger.info(
            f"Domain58SCOTUSMonitor ready "
            f"(interval={self._monitor.polling_interval}m, "
            f"ruling_found={self._monitor.state.get('ruling_found', False)})"
        )

    def run_once(self) -> Dict[str, Any]:
        """
        Execute a single check cycle.

        Returns a result dict:
          status: "ruling_found" | "pending" | "already_alerted" | "error"
          ruling: dict or None
          alert_sent: bool
          timestamp: ISO string
        """
        result: Dict[str, Any] = {
            "monitor": self.DOMAIN,
            "label": self.LABEL,
            "status": "pending",
            "ruling": None,
            "alert_sent": False,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        try:
            # Skip if already alerted
            if self._monitor.state.get("ruling_found"):
                result["status"] = "already_alerted"
                result["ruling"] = {
                    "date": self._monitor.state.get("ruling_date"),
                    "url":  self._monitor.state.get("ruling_url"),
                    "source": self._monitor.state.get("ruling_source"),
                }
                logger.info(f"{self.LABEL}: ruling already detected; no re-alert")
                return result

            ruling = self._monitor.run_check()
            if ruling:
                result["status"] = "ruling_found"
                result["ruling"] = {
                    "case_number": ruling.case_number,
                    "case_name":   ruling.case_name,
                    "date":        ruling.ruling_date,
                    "url":         ruling.ruling_url,
                    "source":      ruling.source,
                    "confidence":  ruling.confidence,
                }
                # Persist state before sending alert
                self._monitor.state["ruling_found"] = True
                self._monitor.state["ruling_date"]  = ruling.ruling_date
                self._monitor.state["ruling_url"]   = ruling.ruling_url
                self._monitor.state["ruling_source"] = ruling.source
                self._monitor._save_state()

                result["alert_sent"] = self._monitor.send_alert(ruling)
                self._write_checkin_alert(ruling)
                logger.info(
                    f"{self.LABEL}: RULING DETECTED (source={ruling.source}, "
                    f"confidence={ruling.confidence:.0%}, alert_sent={result['alert_sent']})"
                )
            else:
                result["status"] = "pending"
                logger.info(f"{self.LABEL}: no ruling yet")

        except Exception as exc:
            result["status"] = "error"
            result["error"] = str(exc)
            logger.error(f"{self.LABEL} check error: {exc}")

        return result

    def _write_checkin_alert(self, ruling: SCOTUSRuling) -> None:
        """Write urgent ruling alert to CHECKIN.md."""
        if not _CHECKIN_PATH.exists():
            logger.warning(f"CHECKIN.md not found: {_CHECKIN_PATH}")
            return
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        block = (
            f"\n\n## DOMAIN 58 IMMEDIATE — Trump v. Barbara Ruling Issued ({now})\n\n"
            f"Source: phase_2_domain_trackers.py (automated)\n\n"
            f"- Case: {ruling.case_name} ({ruling.case_number})\n"
            f"- Date: {ruling.ruling_date}\n"
            f"- URL: {ruling.ruling_url}\n"
            f"- Detection source: {ruling.source} (confidence {ruling.confidence:.0%})\n\n"
            f"Required action: Execute Domain 58 rapid-response distribution immediately.\n"
            f"Reference: DOMAIN_58_TRUMP_V_BARBARA_RAPID_RESPONSE.md\n"
        )
        with open(_CHECKIN_PATH, "a") as f:
            f.write(block)
        logger.info("CHECKIN.md updated with Domain 58 ruling alert")

    def get_state(self) -> Dict:
        """Return current monitor state."""
        return dict(self._monitor.state)


# ---------------------------------------------------------------------------
# Domain 39 — HHS Guidance Tracker wrapper
# ---------------------------------------------------------------------------


class Domain39HHSTracker:
    """
    Wrapper around HHSGuidanceMonitor for Phase 2 automation suite.

    Polling schedule:
    - Default: every 60 minutes (hourly)
    - Active during HHS comment windows: June–December 2026
    - Alert routing: Discord primary, Slack secondary

    Surfaces two relevance tiers:
    - domain_39: direct Medicaid / disenrollment items → IMMEDIATE alert
    - domain_39_adjacent: general healthcare policy → DECISION_REQUIRED alert
    """

    DOMAIN = "domain_39"
    LABEL = "HHS Healthcare Guidance"
    DEFAULT_POLLING_INTERVAL = 60  # minutes — hourly

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or load_config()
        self.config.setdefault("hhs_polling_interval_minutes", self.DEFAULT_POLLING_INTERVAL)
        self._monitor = HHSGuidanceMonitor(config=self.config)
        logger.info(
            f"Domain39HHSTracker ready (interval={self._monitor.polling_interval}m)"
        )

    def run_once(self) -> Dict[str, Any]:
        """
        Execute a single HHS guidance check cycle.

        Returns result dict:
          status: "new_guidance" | "no_new_items" | "error"
          items_found: int
          immediate_items: list[dict]  — domain_39 direct hits
          adjacent_items: list[dict]  — domain_39_adjacent hits
          alert_sent: bool
          timestamp: ISO string
        """
        result: Dict[str, Any] = {
            "monitor": self.DOMAIN,
            "label": self.LABEL,
            "status": "no_new_items",
            "items_found": 0,
            "immediate_items": [],
            "adjacent_items": [],
            "alert_sent": False,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        try:
            guidance_list = self._monitor.run_check()
            if not guidance_list:
                logger.info(f"{self.LABEL}: no new items")
                return result

            result["status"] = "new_guidance"
            result["items_found"] = len(guidance_list)

            for g in guidance_list:
                item = {
                    "title":        g.title,
                    "type":         g.guidance_type,
                    "date":         g.guidance_date,
                    "url":          g.guidance_url,
                    "source":       g.source,
                    "relevance":    g.domain_relevance,
                    "confidence":   g.confidence,
                    "key_dates":    g.key_dates or [],
                }
                if g.domain_relevance == "domain_39":
                    result["immediate_items"].append(item)
                else:
                    result["adjacent_items"].append(item)

            # Alert: Discord first, Slack fallback
            alert_sent = self._monitor.send_alert(guidance_list, channel="discord")
            if not alert_sent and self._monitor.slack_webhook:
                alert_sent = self._monitor.send_alert(guidance_list, channel="slack")
            result["alert_sent"] = alert_sent

            # Write to CHECKIN.md for immediate items
            if result["immediate_items"]:
                self._write_checkin_alert(result["immediate_items"])

            logger.info(
                f"{self.LABEL}: {len(guidance_list)} new items "
                f"({len(result['immediate_items'])} immediate, "
                f"{len(result['adjacent_items'])} adjacent), "
                f"alert_sent={alert_sent}"
            )

        except Exception as exc:
            result["status"] = "error"
            result["error"] = str(exc)
            logger.error(f"{self.LABEL} check error: {exc}")

        return result

    def _write_checkin_alert(self, items: List[Dict]) -> None:
        """Write urgent HHS guidance alerts to CHECKIN.md."""
        if not _CHECKIN_PATH.exists():
            return
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        lines = [
            f"\n\n## DOMAIN 39 IMMEDIATE — HHS Guidance ({now})\n",
            f"Source: phase_2_domain_trackers.py (automated)\n",
        ]
        for item in items[:5]:
            lines.append(
                f"- [{item['type'].upper()}] {item['title']}\n"
                f"  URL: {item['url']}\n"
                f"  Key dates: {', '.join(item['key_dates']) if item['key_dates'] else 'none'}\n"
            )
        lines.append("\nRequired action: Review and route via Domain 39 distribution protocol.\n")
        with open(_CHECKIN_PATH, "a") as f:
            f.writelines(lines)
        logger.info("CHECKIN.md updated with Domain 39 HHS guidance alert")

    def get_state(self) -> Dict:
        """Return current monitor state."""
        return dict(self._monitor.state)


# ---------------------------------------------------------------------------
# Domain 40 — Election Events Monitor wrapper
# ---------------------------------------------------------------------------


class Domain40ElectionMonitor:
    """
    Wrapper around ElectionEventsMonitor for Phase 2 automation suite.

    Data sources:
    - FEC Violations API (quarterly filing monitor, election-interference refs)
    - Election Protection RSS
    - Common Cause RSS

    Keyword triggers: "election" + "deepfake", voter suppression, ballot
    access, election administration, voting restriction.

    Alert gate: Only surfaces items naming a specific US state (filters out
    national opinion pieces).

    Default polling interval: 240 minutes (4 hours).
    """

    DOMAIN = "domain_40"
    LABEL = "Election / Deepfake Events"
    DEFAULT_POLLING_INTERVAL = 240  # minutes — 4 hours

    # Extended deepfake keywords added to base SUPPRESSION_KEYWORDS
    DEEPFAKE_KEYWORDS = [
        "deepfake",
        "synthetic media",
        "ai-generated",
        "election manipulation",
        "election interference",
        "disinformation campaign",
    ]

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or load_config()
        self.config.setdefault("election_polling_interval_minutes", self.DEFAULT_POLLING_INTERVAL)
        self._monitor = ElectionEventsMonitor(config=self.config)
        # Extend suppression keywords with deepfake terms
        self._monitor.SUPPRESSION_KEYWORDS.extend(
            kw for kw in self.DEEPFAKE_KEYWORDS
            if kw not in self._monitor.SUPPRESSION_KEYWORDS
        )
        logger.info(
            f"Domain40ElectionMonitor ready (interval={self._monitor.polling_interval}m, "
            f"deepfake_keywords={len(self.DEEPFAKE_KEYWORDS)} added)"
        )

    def run_once(self) -> Dict[str, Any]:
        """
        Execute a single election events check cycle.

        Returns result dict:
          status: "events_found" | "no_new_events" | "error"
          events_found: int
          deepfake_events: list[dict]   — items matching deepfake/AI keywords
          suppression_events: list[dict] — voter suppression items
          alert_sent: bool
          timestamp: ISO string
        """
        result: Dict[str, Any] = {
            "monitor": self.DOMAIN,
            "label": self.LABEL,
            "status": "no_new_events",
            "events_found": 0,
            "deepfake_events": [],
            "suppression_events": [],
            "alert_sent": False,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        try:
            events = self._monitor.run_check()
            if not events:
                logger.info(f"{self.LABEL}: no new events")
                return result

            result["status"] = "events_found"
            result["events_found"] = len(events)

            for e in events:
                item = {
                    "title":      e.title,
                    "type":       e.event_type,
                    "date":       e.event_date,
                    "url":        e.event_url,
                    "source":     e.source,
                    "state":      e.state_context,
                    "relevance":  e.domain_relevance,
                    "confidence": e.confidence,
                }
                combined = (e.title + " " + (e.summary or "")).lower()
                if any(kw in combined for kw in self.DEEPFAKE_KEYWORDS):
                    result["deepfake_events"].append(item)
                else:
                    result["suppression_events"].append(item)

            result["alert_sent"] = self._monitor.send_alert(events)

            # Write to CHECKIN.md for deepfake events (highest urgency)
            if result["deepfake_events"]:
                self._write_checkin_alert(result["deepfake_events"], alert_type="DEEPFAKE")

            logger.info(
                f"{self.LABEL}: {len(events)} new events "
                f"({len(result['deepfake_events'])} deepfake, "
                f"{len(result['suppression_events'])} suppression), "
                f"alert_sent={result['alert_sent']}"
            )

        except Exception as exc:
            result["status"] = "error"
            result["error"] = str(exc)
            logger.error(f"{self.LABEL} check error: {exc}")

        return result

    def _write_checkin_alert(self, items: List[Dict], alert_type: str = "ELECTION") -> None:
        """Write urgent election event alerts to CHECKIN.md."""
        if not _CHECKIN_PATH.exists():
            return
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        lines = [
            f"\n\n## DOMAIN 40 {alert_type} ALERT ({now})\n",
            f"Source: phase_2_domain_trackers.py (automated)\n",
        ]
        for item in items[:5]:
            lines.append(
                f"- [{item['type'].upper()}] {item['title']} ({item['state'] or 'US'})\n"
                f"  URL: {item['url']}\n"
            )
        lines.append(
            "\nRequired action: Review and route via Domain 40 distribution protocol.\n"
        )
        with open(_CHECKIN_PATH, "a") as f:
            f.writelines(lines)
        logger.info(f"CHECKIN.md updated with Domain 40 {alert_type} alert")

    def get_state(self) -> Dict:
        """Return current monitor state."""
        return dict(self._monitor.state)


# ---------------------------------------------------------------------------
# Coalition Email Router wrapper
# ---------------------------------------------------------------------------


class Domain2CoalitionEmailRouter:
    """
    Wrapper around CoalitionEmailRouter for Phase 2 automation suite.

    Extends base router with Phase 2 domain keyword sets:
    - domain_48: Criminal justice, policing, incarceration
    - domain_49: Environmental justice, rollbacks
    - domain_50: LGBTQ+ rights, non-discrimination
    - domain_51: Campaign finance, dark money, PAC
    - domain_54: Youth civic power, student voting
    - domain_56: Civil service, federal employees
    - domain_57: Multilateral institutions, treaty withdrawal
    - domain_58: Tribal sovereignty, birthright citizenship
    - domain_59: Economic precarity, child tax credit

    Authentication: Requires prior Gmail OAuth2 flow (run --auth flag).
    When not authenticated, run_once() returns graceful degradation result.
    """

    DOMAIN = "coalition_email_router"
    LABEL = "Coalition Email Router"

    # Phase 2 extended domain keyword mappings
    PHASE2_DOMAIN_KEYWORDS: Dict[str, Dict] = {
        "domain_48": {
            "keywords": [
                "criminal justice",
                "policing",
                "incarceration",
                "mass incarceration",
                "prison reform",
                "bail reform",
                "public defender",
                "sentencing",
                "carceral",
            ],
            "weight": 1.0,
        },
        "domain_49": {
            "keywords": [
                "environmental",
                "climate",
                "pollution",
                "epa",
                "rollback",
                "clean air",
                "clean water",
                "environmental justice",
                "carbon",
                "fossil fuel",
            ],
            "weight": 1.0,
        },
        "domain_50": {
            "keywords": [
                "lgbtq",
                "transgender",
                "gender identity",
                "non-discrimination",
                "conversion therapy",
                "pride",
                "same-sex",
                "marriage equality",
                "queer",
            ],
            "weight": 1.0,
        },
        "domain_51": {
            "keywords": [
                "campaign finance",
                "dark money",
                "super pac",
                "citizens united",
                "fec",
                "campaign contribution",
                "disclosure",
                "dark money",
                "unlimited spending",
            ],
            "weight": 1.0,
        },
        "domain_54": {
            "keywords": [
                "youth voting",
                "student voter",
                "campus",
                "young voter",
                "26th amendment",
                "student id",
                "college voter",
                "youth civic",
            ],
            "weight": 1.0,
        },
        "domain_57": {
            "keywords": [
                "multilateral",
                "treaty",
                "nato",
                "un",
                "international agreement",
                "withdrawal",
                "world trade",
                "paris agreement",
                "alliance",
            ],
            "weight": 1.0,
        },
        "domain_59": {
            "keywords": [
                "economic precarity",
                "child tax credit",
                "ctc",
                "poverty",
                "food insecurity",
                "snap",
                "welfare",
                "earned income",
                "economic inequality",
                "working poor",
            ],
            "weight": 1.0,
        },
    }

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or load_config()
        self._router = CoalitionEmailRouter(config=self.config)
        # Merge Phase 2 domains into router keyword set
        self._router.DOMAIN_KEYWORDS.update(self.PHASE2_DOMAIN_KEYWORDS)
        logger.info(
            f"Domain2CoalitionEmailRouter ready "
            f"(total domains={len(self._router.DOMAIN_KEYWORDS)}, "
            f"gmail_configured={bool(self.config.get('gmail_credentials'))})"
        )

    def authenticate(self, credentials_path: Optional[str] = None) -> bool:
        """Run Gmail OAuth2 authentication flow."""
        return self._router.authenticate(credentials_path)

    def run_once(self) -> Dict[str, Any]:
        """
        Execute a single email routing sync cycle.

        Returns result dict:
          status: "emails_tagged" | "no_new_emails" | "not_authenticated" | "error"
          emails_processed: int
          emails_tagged: int
          domain_breakdown: dict[str, int]  — emails per domain tag
          report_written: bool
          timestamp: ISO string
        """
        result: Dict[str, Any] = {
            "monitor": self.DOMAIN,
            "label": self.LABEL,
            "status": "no_new_emails",
            "emails_processed": 0,
            "emails_tagged": 0,
            "domain_breakdown": {},
            "report_written": False,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        if not self._router.gmail_service:
            # Attempt auth if credentials configured
            creds = self.config.get("gmail_credentials")
            if creds and self.config.get("gmail_enabled"):
                logger.info("Coalition router: attempting Gmail authentication...")
                if not self._router.authenticate(creds):
                    result["status"] = "not_authenticated"
                    logger.warning(
                        "Coalition router: not authenticated — "
                        "run --auth to complete OAuth2 flow"
                    )
                    return result
            else:
                result["status"] = "not_authenticated"
                logger.info(
                    "Coalition router: Gmail not configured; skipping. "
                    "Set gmail_enabled=true and gmail_credentials in config."
                )
                return result

        try:
            tagged_emails = self._router.sync_emails()
            result["emails_processed"] = self._router.state.get("messages_processed", 0)
            result["emails_tagged"] = len(tagged_emails)

            if not tagged_emails:
                logger.info(f"{self.LABEL}: no new emails to tag")
                return result

            result["status"] = "emails_tagged"

            # Build domain breakdown
            breakdown: Dict[str, int] = {}
            for email in tagged_emails:
                for domain in email.detected_domains:
                    breakdown[domain] = breakdown.get(domain, 0) + 1
            result["domain_breakdown"] = breakdown

            # Write routing report to CHECKIN.md
            report = self._router.generate_routing_report(tagged_emails)
            if report:
                self._write_routing_report(report)
                result["report_written"] = True

            logger.info(
                f"{self.LABEL}: {len(tagged_emails)} emails tagged; "
                f"domains={dict(sorted(breakdown.items()))}"
            )

        except Exception as exc:
            result["status"] = "error"
            result["error"] = str(exc)
            logger.error(f"{self.LABEL} sync error: {exc}")

        return result

    def _write_routing_report(self, report: str) -> None:
        """Append email routing report to CHECKIN.md."""
        if not _CHECKIN_PATH.exists():
            return
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        header = f"\n\n## Coalition Email Routing Report ({now})\n\n"
        with open(_CHECKIN_PATH, "a") as f:
            f.write(header + report)
        logger.info("CHECKIN.md updated with email routing report")

    def get_state(self) -> Dict:
        """Return current router state."""
        return dict(self._router.state)


# ---------------------------------------------------------------------------
# Parallel runner
# ---------------------------------------------------------------------------


def run_all_monitors_parallel(config: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Launch all four domain monitors in parallel using ThreadPoolExecutor.

    Each monitor runs its run_once() method independently. Results are
    collected and merged into a single summary dict.

    Args:
        config: Optional config dict; loads from file if None.

    Returns:
        Dict with keys:
          timestamp: ISO string
          domain_58_scotus: result dict from Domain58SCOTUSMonitor
          domain_39_hhs: result dict from Domain39HHSTracker
          domain_40_election: result dict from Domain40ElectionMonitor
          coalition_email_router: result dict from Domain2CoalitionEmailRouter
          errors: list[str] — any uncaught exceptions
          total_alerts_sent: int
          has_urgent: bool — True if any SCOTUS ruling found or CHECKIN.md written
    """
    if config is None:
        config = load_config()

    now = datetime.now(timezone.utc)
    logger.info("=" * 70)
    logger.info("Phase 2 Domain Trackers — Parallel Run")
    logger.info(f"Timestamp: {now.isoformat()}")
    logger.info("=" * 70)

    monitors = {
        "domain_58_scotus":    Domain58SCOTUSMonitor(config=config),
        "domain_39_hhs":       Domain39HHSTracker(config=config),
        "domain_40_election":  Domain40ElectionMonitor(config=config),
        "coalition_email_router": Domain2CoalitionEmailRouter(config=config),
    }

    summary: Dict[str, Any] = {
        "timestamp":       now.isoformat(),
        "errors":          [],
        "total_alerts_sent": 0,
        "has_urgent":      False,
    }

    # Run all monitors concurrently — IO-bound so threads are appropriate
    with ThreadPoolExecutor(max_workers=4, thread_name_prefix="phase2-monitor") as pool:
        future_to_key: Dict[Future, str] = {
            pool.submit(monitor.run_once): key
            for key, monitor in monitors.items()
        }

        for future in as_completed(future_to_key):
            key = future_to_key[future]
            try:
                result = future.result(timeout=60)
                summary[key] = result
                if result.get("alert_sent"):
                    summary["total_alerts_sent"] += 1
                if key == "domain_58_scotus" and result.get("status") == "ruling_found":
                    summary["has_urgent"] = True
                if result.get("status") == "error":
                    summary["errors"].append(f"{key}: {result.get('error', 'unknown error')}")
            except Exception as exc:
                msg = f"{key}: uncaught exception — {exc}"
                logger.error(msg)
                summary["errors"].append(msg)
                summary[key] = {"monitor": key, "status": "error", "error": str(exc)}

    # Summary logging
    logger.info("=" * 70)
    logger.info("Phase 2 Parallel Run Complete")
    for key in monitors:
        result = summary.get(key, {})
        logger.info(f"  {key}: status={result.get('status', 'unknown')}")
    logger.info(f"  Total alerts sent: {summary['total_alerts_sent']}")
    logger.info(f"  Urgent (SCOTUS ruling found): {summary['has_urgent']}")
    if summary["errors"]:
        logger.warning(f"  Errors: {summary['errors']}")
    logger.info("=" * 70)

    # Persist combined run log
    _write_run_log(summary)

    return summary


def _write_run_log(summary: Dict) -> None:
    """Write combined run summary to data directory."""
    log_path = _DATA_DIR / f"phase2-run-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M')}.json"
    try:
        with open(log_path, "w") as f:
            json.dump(summary, f, indent=2, default=str)
        logger.info(f"Run log written: {log_path}")
    except IOError as exc:
        logger.warning(f"Failed to write run log: {exc}")


# ---------------------------------------------------------------------------
# Status checker
# ---------------------------------------------------------------------------


def check_status(config: Optional[Dict] = None) -> None:
    """Print current state of all monitors."""
    if config is None:
        config = load_config()

    print()
    print("=" * 70)
    print("Phase 2 Domain Trackers — Status")
    print("=" * 70)
    print()

    monitors = {
        "Domain 58 SCOTUS":         Domain58SCOTUSMonitor(config=config),
        "Domain 39 HHS":            Domain39HHSTracker(config=config),
        "Domain 40 Election":       Domain40ElectionMonitor(config=config),
        "Coalition Email Router":   Domain2CoalitionEmailRouter(config=config),
    }

    for label, monitor in monitors.items():
        state = monitor.get_state()
        print(f"  {label}")
        print(f"    Last check:     {state.get('last_check', 'never')}")
        print(f"    Alerts sent:    {state.get('alerts_sent', 0)}")

        # Domain-58-specific
        if hasattr(monitor, '_monitor') and hasattr(monitor._monitor, 'state'):
            if 'ruling_found' in state:
                print(f"    Ruling found:   {state.get('ruling_found', False)}")
                if state.get('ruling_found'):
                    print(f"    Ruling date:    {state.get('ruling_date', 'unknown')}")
                    print(f"    Ruling URL:     {state.get('ruling_url', 'unknown')}")

            # HHS/Election items seen
            if 'items_seen' in state:
                print(f"    Items tracked:  {len(state.get('items_seen', []))}")

            # Email router
            if 'messages_processed' in state:
                print(f"    Msgs processed: {state.get('messages_processed', 0)}")
                print(f"    Msgs tagged:    {state.get('messages_tagged', 0)}")
        print()

    print(f"  Config file:     {'exists' if _CONFIG_PATH.exists() else 'MISSING — using env vars'}")
    print(f"  Config path:     {_CONFIG_PATH}")
    print(f"  Data dir:        {_DATA_DIR}")
    print(f"  CHECKIN.md:      {'exists' if _CHECKIN_PATH.exists() else 'NOT FOUND'}")
    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 2 Domain-Specific Tracking Automation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  --run-now           Execute all four monitors in parallel (single pass)
  --check-status      Print current state of all monitors
  --continuous        Run all monitors in continuous polling loops
  --auth-gmail        Run Gmail OAuth2 flow for email router
  --config PATH       Override config file path

Examples:
  python3 src/phase_2_domain_trackers.py --run-now
  python3 src/phase_2_domain_trackers.py --check-status
  python3 src/phase_2_domain_trackers.py --auth-gmail
  python3 src/phase_2_domain_trackers.py --continuous --duration-hours 24
        """,
    )
    parser.add_argument("--run-now",       action="store_true", help="Single parallel run")
    parser.add_argument("--check-status",  action="store_true", help="Print monitor states")
    parser.add_argument("--continuous",    action="store_true", help="Run continuous polling")
    parser.add_argument("--auth-gmail",    action="store_true", help="Authenticate Gmail")
    parser.add_argument("--duration-hours", type=int, default=None,
                        help="Stop continuous mode after N hours")
    parser.add_argument("--config", type=str, default=None,
                        help="Path to config JSON file")
    args = parser.parse_args()

    # Load config
    config: Optional[Dict] = None
    if args.config:
        try:
            with open(args.config) as f:
                config = json.load(f)
        except (json.JSONDecodeError, IOError) as exc:
            logger.error(f"Failed to load config: {exc}")
            return 1

    if args.check_status:
        check_status(config=config)
        return 0

    if args.auth_gmail:
        router = Domain2CoalitionEmailRouter(config=config)
        creds = (config or load_config()).get("gmail_credentials")
        if router.authenticate(creds):
            logger.info("Gmail authentication successful")
            return 0
        logger.error("Gmail authentication failed")
        return 1

    if args.run_now:
        summary = run_all_monitors_parallel(config=config)
        print(json.dumps(summary, indent=2, default=str))
        return 0 if not summary.get("errors") else 1

    if args.continuous:
        from time import sleep
        import threading

        cfg = config or load_config()
        start = datetime.now(timezone.utc)
        logger.info("Starting continuous Phase 2 monitoring...")

        # The sub-monitors have their own sleep loops; here we orchestrate a
        # master loop that re-runs each monitor's run_once() in parallel at the
        # shortest common interval (SCOTUS = 14m).
        scotus_interval  = cfg.get("scotus_polling_interval_minutes", 14) * 60
        hhs_interval     = cfg.get("hhs_polling_interval_minutes", 60) * 60
        election_interval = cfg.get("election_polling_interval_minutes", 240) * 60
        email_interval   = cfg.get("email_polling_interval_minutes", 60) * 60

        monitors = {
            "domain_58_scotus":      (Domain58SCOTUSMonitor(cfg),   scotus_interval),
            "domain_39_hhs":         (Domain39HHSTracker(cfg),      hhs_interval),
            "domain_40_election":    (Domain40ElectionMonitor(cfg),  election_interval),
            "coalition_email_router":(Domain2CoalitionEmailRouter(cfg), email_interval),
        }

        last_run: Dict[str, float] = {k: 0.0 for k in monitors}

        try:
            while True:
                # Duration check
                if args.duration_hours:
                    elapsed = (datetime.now(timezone.utc) - start).total_seconds() / 3600
                    if elapsed > args.duration_hours:
                        logger.info(f"Duration limit reached ({args.duration_hours}h); stopping")
                        break

                import time
                now_ts = time.time()
                due = [
                    key for key, (mon, interval) in monitors.items()
                    if now_ts - last_run[key] >= interval
                ]

                if due:
                    with ThreadPoolExecutor(max_workers=len(due)) as pool:
                        futures = {
                            pool.submit(monitors[key][0].run_once): key
                            for key in due
                        }
                        for future in as_completed(futures):
                            key = futures[future]
                            try:
                                result = future.result(timeout=60)
                                last_run[key] = time.time()
                                logger.info(
                                    f"[continuous] {key}: status={result.get('status', 'unknown')}"
                                )
                            except Exception as exc:
                                logger.error(f"[continuous] {key} error: {exc}")

                sleep(60)  # Master tick: check every minute which monitors are due

        except KeyboardInterrupt:
            logger.info("Continuous monitoring stopped by user")

        return 0

    # Default: show help + status
    parser.print_help()
    print()
    check_status(config=config)
    return 0


if __name__ == "__main__":
    sys.exit(main())
