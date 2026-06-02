#!/usr/bin/env python3
"""
Phase 1 Adoption Tracking Script — v2.0
June 3, 2026 production deployment

Automates weekly monitoring of:
1. GitHub Gist engagement signals (comments, forks via REST API)
2. Bitly click counts for short links embedded in outreach emails
3. Email replies (Gmail API, label: phase-1-responses)
4. State persistence across weekly runs (JSON in data/)
5. Alert detection and CHECKIN.md flagging
6. Weekly summary Markdown generation

Usage:
  python3 phase-1-adoption-tracking-script.py --check-config
  python3 phase-1-adoption-tracking-script.py --run-now
  python3 phase-1-adoption-tracking-script.py --schedule-weekly
  python3 phase-1-adoption-tracking-script.py --day7-report
  python3 phase-1-adoption-tracking-script.py --day30-report

Configuration (adoption-tracking-config.json or environment variables):
  github_token          GitHub personal access token (5000 req/hr when set)
  github_username       GitHub account username
  gmail_credentials     Path to Gmail OAuth2 credentials.json
  gmail_label           Gmail label name (default: phase-1-responses)
  bitly_token           Bitly generic access token
  bitly_links           Dict of label -> bitlink_id pairs
  phase1_start_date     ISO date of first Wave 1 send (default: 2026-05-28)

Cron (auto-printed via --schedule-weekly):
  0 9 * * 1 /usr/bin/python3 /path/to/script.py --run-now
  Runs every Monday 09:00 UTC
"""

import os
import sys
import json
import logging
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Optional Google API imports with graceful fallback
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google.auth.oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    HAS_GOOGLE = True
except ImportError:
    HAS_GOOGLE = False

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent.resolve()
CONFIG_PATH = SCRIPT_DIR / "adoption-tracking-config.json"
DATA_DIR = SCRIPT_DIR / "data"
LOG_DIR = SCRIPT_DIR / "logs"
# CHECKIN.md lives one level up in projects/resistance-research/
CHECKIN_PATH = SCRIPT_DIR.parent / "CHECKIN.md"

# Phase 2 domain trackers — imported lazily to avoid hard dependency
PHASE2_SRC_DIR = SCRIPT_DIR.parent / "src"

# Canonical Gist IDs — Phase 1 live distribution (verified June 1, 2026)
CANONICAL_GISTS = {
    "domain_56_civil_service":      "8f11e868397921a4e6556b41196d1b1f",
    "domain_39_healthcare":         "131e8a94c955b973b87f7fb87d0f594b",
    "domain_59_economic_precarity": "70b18a6f26dc879e3399c6d147d882ba",
    "domain_37_fed_interference":   "1277f5d5bcb0fe46604bbaba8fa37fd0",
    "domain_58_tribal_sovereignty": "0caf4e1ab5661355ea2df5e53d3c169f",
    "full_proposal":                "2dec7fd03b08ab5b41c55d402f44c261",
    "executive_summary":            "2869da6eaeb15a47246ade3bbbc4a3f4",
    "litigation_tracker":           "418d51bda087f15a04d685ab171a5ee0",
}

CANONICAL_USERNAME = "esca8peArtist"
DEFAULT_GMAIL_LABEL = "phase-1-responses"

# Thresholds from PHASE_1_MEASUREMENT_SYSTEM.md Section 4
WEEKLY_CLICK_TARGETS: Dict[int, int] = {1: 15, 2: 25, 4: 50, 8: 100}
DAY7_CLICKS_HOLD = 15
DAY7_CLICKS_MONITOR_LOW = 5
DAY7_REPLIES_HOLD = 2
DAY7_BOUNCE_ALERT = 3
DAY30_STRONG_REPLY_RATE = 0.50
DAY30_STRONG_CONSTITUENCIES = 4
DAY30_STRONG_CROSS_ORG = 3
DAY30_STRONG_ADOPTIONS = 2

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "adoption-tracking.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

def load_config() -> Dict:
    """Load config from JSON file or environment variables."""
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            config = json.load(f)
        logger.info(f"Loaded config: {CONFIG_PATH}")
        return config

    logger.warning(f"Config not found at {CONFIG_PATH}; reading environment variables")
    return {
        "github_token":       os.getenv("GITHUB_TOKEN", ""),
        "github_username":    os.getenv("GITHUB_USERNAME", CANONICAL_USERNAME),
        "gmail_enabled":      bool(os.getenv("GMAIL_CREDENTIALS_JSON", "")),
        "gmail_credentials":  os.getenv("GMAIL_CREDENTIALS_JSON", ""),
        "gmail_label":        os.getenv("GMAIL_LABEL", DEFAULT_GMAIL_LABEL),
        "bitly_enabled":      bool(os.getenv("BITLY_TOKEN", "")),
        "bitly_token":        os.getenv("BITLY_TOKEN", ""),
        "bitly_links":        {},
        "canonical_gists":    CANONICAL_GISTS,
        "phase1_start_date":  "2026-05-28",
        "email_lookback_hours": 168,
    }


def check_config() -> bool:
    """Print configuration status and return True if minimum config is present."""
    config = load_config()
    print()
    print("=" * 60)
    print("Phase 1 Adoption Tracking — Configuration Status")
    print("=" * 60)
    print()

    rows = [
        ("Config file",            CONFIG_PATH.exists(), f"{CONFIG_PATH}"),
        ("GitHub token",           bool(config.get("github_token")), "Required for 5000 req/hr; optional for 60 req/hr"),
        ("GitHub username",        bool(config.get("github_username")), config.get("github_username", "NOT SET")),
        ("Gmail enabled",          config.get("gmail_enabled", False), "Optional; enables reply monitoring"),
        ("Gmail credentials path", bool(config.get("gmail_credentials")), config.get("gmail_credentials", "NOT SET")),
        ("Bitly enabled",          config.get("bitly_enabled", False), "Optional; enables click tracking"),
        ("Bitly links count",      None, str(len(config.get("bitly_links", {}))) + " links configured"),
        ("Canonical Gists",        None, str(len(config.get("canonical_gists", CANONICAL_GISTS))) + " Gists tracked"),
        ("Phase 1 start date",     None, config.get("phase1_start_date", "NOT SET")),
        ("Data directory",         DATA_DIR.exists(), str(DATA_DIR)),
        ("Logs directory",         LOG_DIR.exists(), str(LOG_DIR)),
    ]

    ready = True
    for label, status, note in rows:
        if status is None:
            tag = "INFO"
        elif status:
            tag = "OK"
        else:
            tag = "MISSING"
            if label in ("GitHub username",):
                ready = False
        print(f"  [{tag:7}] {label}: {note}")

    print()
    if ready:
        print("Minimum config present. Run --run-now to collect data.")
        print()
        print("For full functionality, also configure:")
        print("  gmail_enabled: true + gmail_credentials path (email reply monitoring)")
        print("  bitly_enabled: true + bitly_token + bitly_links (click tracking)")
    else:
        print("Action required: edit adoption-tracking-config.json")
        print(f"  Location: {CONFIG_PATH}")
    print()
    return ready


# ---------------------------------------------------------------------------
# State persistence
# ---------------------------------------------------------------------------

def load_state() -> Dict:
    state_path = DATA_DIR / "state.json"
    if state_path.exists():
        with open(state_path) as f:
            return json.load(f)
    return {
        "first_run": None,
        "last_run": None,
        "week_number": 0,
        "cumulative_clicks": 0,
        "gist_baseline": {},
        "run_history": [],
    }


def save_state(state: Dict):
    state_path = DATA_DIR / "state.json"
    with open(state_path, "w") as f:
        json.dump(state, f, indent=2, default=str)
    logger.info(f"State saved: {state_path}")


# ---------------------------------------------------------------------------
# GitHub Gist poller
# ---------------------------------------------------------------------------

class GistPoller:
    """Fetch Gist metadata from GitHub REST API."""

    API_BASE = "https://api.github.com"

    def __init__(self, github_token: str = "", username: str = CANONICAL_USERNAME):
        self.username = username
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        # Reject obvious placeholder values
        is_real_token = (
            github_token
            and not github_token.startswith("YOUR_")
            and len(github_token) > 10
        )
        if is_real_token:
            self.headers["Authorization"] = f"token {github_token}"
            logger.info("GitHub: authenticated (5000 req/hr)")
        else:
            logger.info("GitHub: unauthenticated (60 req/hr) — set a real github_token in config for higher limits")

    def get_gist(self, gist_id: str) -> Optional[Dict]:
        """
        Fetch Gist metadata.

        Note: GitHub REST API does not expose Gist view counts.
        Comments and forks serve as proxy engagement signals.
        Use Bitly click counts as the primary engagement metric.
        """
        url = f"{self.API_BASE}/gists/{gist_id}"
        try:
            resp = requests.get(url, headers=self.headers, timeout=10)
            if resp.status_code == 403:
                logger.warning(f"Rate limit hit on {gist_id}; will retry next run")
                return {"gist_id": gist_id, "error": "rate_limited"}
            resp.raise_for_status()
            d = resp.json()
            return {
                "gist_id":    gist_id,
                "url":        d.get("html_url", ""),
                "comments":   d.get("comments", 0),
                "forks":      len(d.get("forks", [])),
                "created_at": d.get("created_at", "")[:10],
                "updated_at": d.get("updated_at", "")[:10],
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        except requests.RequestException as e:
            logger.error(f"Gist fetch error {gist_id}: {e}")
            return {"gist_id": gist_id, "error": str(e)}

    def poll_all(self, gists: Dict[str, str]) -> Dict[str, Optional[Dict]]:
        results = {}
        for label, gist_id in gists.items():
            logger.info(f"  Polling {label} ({gist_id[:8]}...)")
            results[label] = self.get_gist(gist_id)
        return results


# ---------------------------------------------------------------------------
# Bitly click tracker
# ---------------------------------------------------------------------------

class BitlyTracker:
    """Retrieve Bitly click counts for Phase 1 short links."""

    API = "https://api-ssl.bitly.com/v4"

    def __init__(self, access_token: str):
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    def get_clicks(self, bitlink: str, units: int = 7, unit: str = "day") -> Optional[int]:
        """
        Fetch weekly click count for a Bitly link.

        Args:
            bitlink: Bitlink without https:// (e.g., 'bit.ly/drp-d56')
            units: Number of time units (7 = last 7 days)
            unit: 'day', 'week', or 'month'
        """
        bitlink = bitlink.replace("https://", "").replace("http://", "")
        url = f"{self.API}/bitlinks/{bitlink}/clicks/summary"
        try:
            resp = requests.get(url, headers=self.headers, params={"unit": unit, "units": units}, timeout=10)
            resp.raise_for_status()
            return resp.json().get("total_clicks", 0)
        except requests.RequestException as e:
            logger.error(f"Bitly error for {bitlink}: {e}")
            return None

    def get_all(self, bitlinks: Dict[str, str]) -> Dict[str, Optional[int]]:
        results = {}
        for label, link in bitlinks.items():
            logger.info(f"  Bitly clicks: {label} ({link})")
            results[label] = self.get_clicks(link)
        return results


# ---------------------------------------------------------------------------
# Gmail reply monitor
# ---------------------------------------------------------------------------

class GmailMonitor:
    """Monitor Gmail for Phase 1 adoption reply signals."""

    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    TOKEN_PATH = SCRIPT_DIR / "token.json"

    def __init__(self, credentials_path: str, label: str = DEFAULT_GMAIL_LABEL):
        self.credentials_path = credentials_path
        self.label = label
        self.service = None
        if HAS_GOOGLE:
            self._authenticate()
        else:
            logger.warning("Google libraries not installed; Gmail monitoring disabled")
            logger.warning("Install: pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client")

    def _authenticate(self):
        creds = None
        if self.TOKEN_PATH.exists():
            creds = Credentials.from_authorized_user_file(str(self.TOKEN_PATH), self.SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                logger.info("Refreshing Gmail token...")
                creds.refresh(Request())
            else:
                cpath = Path(self.credentials_path)
                if not cpath.exists():
                    logger.error(f"Gmail credentials not found: {self.credentials_path}")
                    logger.error("Run oauth2_login.py to generate credentials")
                    return
                logger.info("Running Gmail OAuth2 flow (browser required)...")
                flow = InstalledAppFlow.from_client_secrets_file(str(cpath), self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(self.TOKEN_PATH, "w") as f:
                f.write(creds.to_json())
            logger.info(f"Token saved: {self.TOKEN_PATH}")

        try:
            self.service = build("gmail", "v1", credentials=creds)
            logger.info("Gmail authenticated")
        except Exception as e:
            logger.error(f"Gmail build failed: {e}")

    def _resolve_label_id(self) -> Optional[str]:
        if not self.service:
            return None
        try:
            resp = self.service.users().labels().list(userId="me").execute()
            for lbl in resp.get("labels", []):
                if lbl["name"].lower() == self.label.lower():
                    return lbl["id"]
            logger.warning(
                f"Gmail label '{self.label}' not found. "
                "Create it: Gmail > Settings > Labels > Create new label."
            )
        except Exception as e:
            logger.error(f"Label list error: {e}")
        return None

    def get_recent_replies(self, lookback_hours: int = 168) -> List[Dict]:
        """Return emails from phase-1-responses label in the lookback window."""
        if not self.service:
            return []

        label_id = self._resolve_label_id()
        cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
        query = f"after:{cutoff.strftime('%Y/%m/%d')}"
        if label_id:
            query += f" label:{self.label}"
        else:
            query += " in:inbox subject:Re:"

        logger.info(f"Gmail query: {query}")
        try:
            result = self.service.users().messages().list(
                userId="me", q=query, maxResults=50
            ).execute()
            msgs = result.get("messages", [])
            logger.info(f"  {len(msgs)} messages found")

            replies = []
            for ref in msgs:
                try:
                    msg = self.service.users().messages().get(
                        userId="me", id=ref["id"], format="metadata",
                        metadataHeaders=["From", "Subject", "Date"]
                    ).execute()
                    hdrs = {h["name"]: h["value"] for h in msg["payload"]["headers"]}
                    replies.append({
                        "id":        msg["id"],
                        "thread_id": msg.get("threadId", ""),
                        "from_addr": hdrs.get("From", "")[:80],
                        "subject":   hdrs.get("Subject", "")[:100],
                        "date":      hdrs.get("Date", "")[:40],
                        "snippet":   msg.get("snippet", "")[:200],
                    })
                except Exception as e:
                    logger.warning(f"Message {ref['id']} fetch failed: {e}")

            return replies

        except Exception as e:
            logger.error(f"Gmail fetch failed: {e}")
            return []


# ---------------------------------------------------------------------------
# Alert detection
# ---------------------------------------------------------------------------

class AlertDetector:
    """Evaluate metrics against Phase 1 thresholds from PHASE_1_MEASUREMENT_SYSTEM.md."""

    def __init__(self, phase1_start_date: str = "2026-05-28"):
        try:
            self.start = datetime.fromisoformat(phase1_start_date).replace(tzinfo=timezone.utc)
        except ValueError:
            self.start = datetime(2026, 5, 28, tzinfo=timezone.utc)

    def days_elapsed(self) -> int:
        return max(0, (datetime.now(timezone.utc) - self.start).days)

    def week_number(self) -> int:
        return max(1, (self.days_elapsed() // 7) + 1)

    def click_target(self, week: int) -> int:
        for w in sorted(WEEKLY_CLICK_TARGETS.keys(), reverse=True):
            if week >= w:
                return WEEKLY_CLICK_TARGETS[w]
        return WEEKLY_CLICK_TARGETS[1]

    def evaluate(
        self,
        clicks_this_week: int,
        cumulative_clicks: int,
        reply_count: int,
        bounce_count: int = 0,
        score4_count: int = 0,
        score5_count: int = 0,
    ) -> List[Dict]:
        """
        Return list of alert dicts with keys: level, code, message, action.
        Levels: INFO, MONITOR, ESCALATE, FAILURE_IMMINENT, ESCALATE_NOW, URGENT
        """
        alerts = []
        day = self.days_elapsed()
        week = self.week_number()
        target = self.click_target(week)

        # Bounce threshold
        if bounce_count >= DAY7_BOUNCE_ALERT:
            alerts.append({
                "level": "URGENT",
                "code":  "BOUNCE_THRESHOLD",
                "message": f"{bounce_count} bounces (threshold: {DAY7_BOUNCE_ALERT})",
                "action": "Verify contact list; re-send to corrected addresses within 24h; restart Day 7 clock",
            })

        # Score 5 — confirmed adoption
        if score5_count > 0:
            alerts.append({
                "level": "ESCALATE_NOW",
                "code":  "SCORE_5_ADOPTION",
                "message": f"{score5_count} confirmed adoption signal(s)",
                "action": "Log in Adoptions sheet immediately; notify user same day; pre-activate Phase 2",
            })

        # Score 4 cluster — pre-Day-30 STRONG
        if score4_count >= 2 and day <= 14:
            alerts.append({
                "level": "ESCALATE_NOW",
                "code":  "SCORE_4_CLUSTER",
                "message": f"{score4_count} Score 4 replies in first 14 days (pre-Day-30 STRONG signal)",
                "action": "Execute STRONG protocol: launch Domain 39 + 56 within 48h; begin Tier 2 staging",
            })

        # Day 7 checks
        if 7 <= day < 14:
            if clicks_this_week < DAY7_CLICKS_MONITOR_LOW and reply_count == 0:
                alerts.append({
                    "level": "ESCALATE",
                    "code":  "DAY7_DELIVERY_FAILURE",
                    "message": f"Day {day}: {clicks_this_week} clicks, 0 replies (critical — delivery may have failed)",
                    "action": "Verify Bitly links; check Gmail spam folder; contact Tier 1 directly within 24h",
                })
            elif clicks_this_week < DAY7_CLICKS_HOLD or reply_count < DAY7_REPLIES_HOLD:
                alerts.append({
                    "level": "MONITOR",
                    "code":  "DAY7_BELOW_HOLD",
                    "message": f"Day {day}: {clicks_this_week} clicks, {reply_count} replies (hold requires 15+ clicks, 2+ replies)",
                    "action": "Recheck at Day 14; monitor for reply spikes Days 8-14; no action yet",
                })

        # Day 14 checks
        if 14 <= day < 21:
            if cumulative_clicks < 10:
                alerts.append({
                    "level": "FAILURE_IMMINENT",
                    "code":  "DAY14_CRITICAL",
                    "message": f"Day {day}: cumulative {cumulative_clicks} clicks (critical threshold: <10)",
                    "action": "Contact Tier 1 by phone/video; create new Bitly links; execute failure recovery protocol",
                })
            elif cumulative_clicks < 25:
                alerts.append({
                    "level": "MONITOR",
                    "code":  "DAY14_BELOW_TARGET",
                    "message": f"Day {day}: cumulative {cumulative_clicks} clicks (target: 25+)",
                    "action": "Apply Modification 2 (single-domain framing revision); plan Day 45 re-send",
                })

        # Below weekly click target (any week after Day 7)
        if day > 7 and cumulative_clicks < target:
            alerts.append({
                "level": "MONITOR",
                "code":  "BELOW_CLICK_TARGET",
                "message": f"Week {week}: cumulative {cumulative_clicks} below target {target}",
                "action": f"Check Bitly dashboard; confirm short links are embedded in all outreach emails",
            })

        return alerts


# ---------------------------------------------------------------------------
# Output generation
# ---------------------------------------------------------------------------

def generate_weekly_summary(
    week: int,
    day: int,
    gist_data: Dict,
    replies: List[Dict],
    alerts: List[Dict],
    cumulative_clicks: int,
    clicks_this_week: int,
) -> str:
    now = datetime.now(timezone.utc)
    lines = [
        f"# Phase 1 Adoption Tracking — Week {week} Summary (Day {day})",
        f"Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "---",
        "",
        "## 1. Gist Engagement (GitHub API proxy signals)",
        "",
        "Note: GitHub does not expose view counts. Comments and forks are proxy signals only.",
        "Primary click metric = Bitly dashboard (manual pull).",
        "",
    ]

    if gist_data:
        for label, data in gist_data.items():
            if data and "error" not in data:
                lines.append(
                    f"- **{label}**: {data.get('comments', 0)} comments | "
                    f"{data.get('forks', 0)} forks | "
                    f"updated {data.get('updated_at', 'unknown')}"
                )
            elif data and data.get("error") == "rate_limited":
                lines.append(f"- **{label}**: rate limited — retry next run")
            else:
                lines.append(f"- **{label}**: fetch failed (check log)")
    else:
        lines.append("- No Gist data retrieved (verify GitHub token and network)")

    lines += [
        "",
        "## 2. Click Tracking Summary",
        "",
        f"Clicks this week (automated): **{clicks_this_week}**",
        f"Cumulative total (automated): **{cumulative_clicks}**",
        "",
        "Manual step: Log in to bitly.com > Analytics to get per-link click counts.",
        "Enter in Google Sheets > Gist_Views tab for this week's row.",
        "",
        "## 3. Email Replies",
        "",
    ]

    if replies:
        lines.append(f"Total replies retrieved this week: **{len(replies)}**")
        lines.append("")
        lines.append("Score each reply using reply-triage-framework.md before entering in Sheets.")
        lines.append("")
        for i, r in enumerate(replies[:20], 1):
            lines.append(f"### Reply {i}")
            lines.append(f"- **From**: {r.get('from_addr', 'unknown')}")
            lines.append(f"- **Subject**: {r.get('subject', '')}")
            lines.append(f"- **Date**: {r.get('date', '')}")
            lines.append(f"- **Snippet**: {r.get('snippet', '')[:180]}...")
            lines.append(f"- Score: [fill 1-5] | Type: [fill] | Follow-up: [YES/NO]")
            lines.append("")
    else:
        lines.append("No replies retrieved.")
        lines.append("")
        lines.append("If Gmail is configured, check that the `phase-1-responses` label exists and")
        lines.append("that a filter applies it to Phase 1 replies automatically.")

    if alerts:
        lines += ["", "## 4. Alerts Triggered", ""]
        for alert in alerts:
            lines.append(f"### [{alert['level']}] {alert['code']}")
            lines.append(f"**{alert['message']}**")
            lines.append(f"Required action: {alert['action']}")
            lines.append("")
    else:
        lines += ["", "## 4. Alerts", "", "- No alerts triggered this week.", ""]

    lines += [
        "",
        "## 5. Manual Actions Required This Week",
        "",
        "- [ ] Pull Bitly click counts from bitly.com and enter in Gist_Views tab",
        "- [ ] Score each new reply (1-5) using reply-triage-framework.md",
        "- [ ] Enter scored replies in Replies tab of Google Sheets",
        "- [ ] Update Contacts tab: Reply_Date, Reply_Score, Delivery_Status for any changes",
        "- [ ] Check Constituencies tab formula results (auto-calculated)",
        "- [ ] If checkpoint week: run decision tree (day-7-14-30-decision-trees.md)",
        "- [ ] Update CHECKIN.md if any URGENT or ESCALATE_NOW alerts above",
        "",
        "## 6. Reference Files",
        "",
        "- Measurement system: PHASE_1_MEASUREMENT_SYSTEM.md",
        "- Decision trees: day-7-14-30-decision-trees.md",
        "- Reply scoring: reply-triage-framework.md",
        "- Sheets spec: PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md",
        "- Weekly synthesis: PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md",
    ]

    return "\n".join(lines)


def append_to_checkin(alerts: List[Dict], week: int):
    """Write urgent alerts to CHECKIN.md under 'Needs Your Input'."""
    urgent = [a for a in alerts if a["level"] in ("URGENT", "ESCALATE_NOW", "FAILURE_IMMINENT")]
    if not urgent:
        return
    if not CHECKIN_PATH.exists():
        logger.warning(f"CHECKIN.md not found at {CHECKIN_PATH}")
        return

    now = datetime.now(timezone.utc)
    block = [
        "",
        f"## Phase 1 Tracking Alert — Week {week} ({now.strftime('%Y-%m-%d %H:%M UTC')})",
        "",
        "Source: phase-1-adoption-tracking-script.py (automated)",
        "",
    ]
    for a in urgent:
        block.append(f"- [{a['level']}] {a['code']}: {a['message']}")
        block.append(f"  Action: {a['action']}")
        block.append("")

    with open(CHECKIN_PATH, "a") as f:
        f.write("\n".join(block))
    logger.info(f"Appended {len(urgent)} urgent alert(s) to CHECKIN.md")


def generate_day7_report(state: Dict) -> str:
    """Day 7 checkpoint template for manual use."""
    lines = [
        "# Phase 1 Day 7 Checkpoint",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "Pull three numbers from your Google Sheets dashboard, then follow the tree.",
        "",
        "## Inputs",
        "",
        "| # | Metric | Pull from | Value |",
        "|---|--------|-----------|-------|",
        "| 1 | Week 1 Bitly clicks (total all links) | Gist_Views tab > col I, row 2 | [X] |",
        "| 2 | Bounce count | Contacts tab > =COUNTIF(G:G,'Bounced') | [X] |",
        "| 3 | Total replies (any score) | Contacts tab > summary row 'Any reply' | [X] |",
        "",
        "## Decision Tree (check in order)",
        "",
        "Step 1: Bounces >= 3?",
        "  YES -> CONTACT_VERIFY: Fix email list, resend, restart Day 7 clock",
        "  NO  -> Step 2",
        "",
        "Step 2: Total clicks >= 15?",
        "  YES -> Step 3",
        "  NO  -> Check range:",
        "         Clicks 5-14: MONITOR (recheck Day 14)",
        "         Clicks 0-4 with confirmed delivery: ESCALATE (delivery diagnostic)",
        "",
        "Step 3: Replies >= 2?",
        "  YES -> HOLD (normal trajectory; checkpoint again Day 30)",
        "  NO  -> MONITOR (check again Day 14; no action yet)",
        "",
        "## Determination Reference",
        "",
        "| Result | Criteria | Next Step |",
        "|--------|----------|-----------|",
        "| HOLD | 15+ clicks AND 2+ replies | Continue to Day 30 |",
        "| MONITOR | 5-14 clicks OR 0-1 replies | Recheck Day 14 (June 11) |",
        "| ESCALATE | 0-4 clicks, confirmed delivery | Run delivery diagnostic NOW |",
        "| CONTACT_VERIFY | 3+ bounces | Fix emails, restart Day 7 |",
        "",
        "## CHECKIN.md Entry Template",
        "",
        "Copy and paste this into CHECKIN.md:",
        "",
        "---",
        "## Phase 1 Day 7 Checkpoint — [DATE]",
        "",
        "**Determination**: [HOLD / MONITOR / ESCALATE / CONTACT_VERIFY]",
        "",
        "**Metrics**:",
        "- Domain 56 clicks: [X]",
        "- Domain 39 clicks: [X]",
        "- Total clicks: [X]",
        "- Total replies: [X]",
        "- Bounces: [X]",
        "",
        "**Next action**: [e.g., 'No action; Day 30 checkpoint June 27']",
        "---",
    ]
    return "\n".join(lines)


def generate_day30_report() -> str:
    """Day 30 checkpoint decision template."""
    lines = [
        "# Phase 1 Day 30 Checkpoint",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "Pull five data points from Google Sheets, then run the decision tree.",
        "Check order: FAILURE first, then STRONG, MODERATE, WEAK, ASSESS.",
        "",
        "## Inputs",
        "",
        "| Variable | Formula | Value |",
        "|----------|---------|-------|",
        "| (A) Score 3+ reply rate | Contacts summary: Score 3+ rate | [X%] |",
        "| (B) Constituencies at strong threshold | Constituencies!I2:I8 count 'YES' | [X of 7] |",
        "| (C) Cross-org references | Replies tab: COUNTIF(E:E,'Forward') | [X] |",
        "| (D) Confirmed adoptions | Adoptions tab: COUNTIF(H:H,'Confirmed') | [X] |",
        "| (E) Week 3-4 Bitly clicks = 0? | Gist_Views rows 4-5 col I = 0? | [YES/NO] |",
        "",
        "## Decision Tree",
        "",
        "FAILURE: A<10% AND C=0 AND D=0 AND E=YES",
        "  -> Stop all evaluation. Update CHECKIN.md 'Needs Your Input'.",
        "  -> User decides within 48h: CONTINUE (Mods 1-3) / PIVOT (public channels) / CLOSE",
        "  -> Send Domain 39 regardless (healthcare deadline non-negotiable)",
        "",
        "STRONG: A>=50% AND B>=4 AND C>=3 AND D>=2",
        "  -> Phase 2 full launch: Domain 39 Day 1, Domain 56 Day 1-2",
        "  -> Begin Tier 2 (91-contact) outreach preparation",
        "  -> Stage Domain 58 and 59 for Weeks 5-8 activation",
        "",
        "MODERATE: A 20-49% OR B>=3 OR C>=1 OR D>=1 (but not STRONG)",
        "  -> Domain 39 launches Day 1 (non-negotiable)",
        "  -> Domain 56 holds to Day 37",
        "  -> Extend Phase 1 monitoring through Day 60",
        "  -> Prepare Tier 2 but do not send yet",
        "",
        "WEAK: A<20% AND B<2 AND C=0 AND D=0 (but not FAILURE)",
        "  -> Domain 39 sends (non-negotiable)",
        "  -> Domain 56 holds to Day 60",
        "  -> Apply Modification 1 (stakeholder substitution, by Day 37)",
        "  -> Apply Modification 2 (framing revision, by Day 35)",
        "  -> Apply Modification 3 (channel shift, by Day 45)",
        "  -> Set Day 90 extension checkpoint",
        "",
        "ASSESS: Partial signals — some of A/B/C/D nonzero but below MODERATE",
        "  -> Domain 39 only",
        "  -> Prepare both contingency and normal Phase 2 paths in parallel",
        "  -> Next formal checkpoint: Day 60 (July 27)",
        "",
        "## Domain 58 / 59 Activation Gate",
        "",
        "Domain 58 (Tribal Sovereignty): Activate at Day 30 STRONG or Day 60 MODERATE",
        "Domain 59 (Economic Precarity): Activate at Day 30 MODERATE or better",
        "Both require: Score 3+ replies from at least 1 constituency in their target sector",
        "",
        "## CHECKIN.md Entry Template",
        "",
        "---",
        "## Phase 1 Day 30 Checkpoint — [DATE]",
        "",
        "**Determination**: [STRONG / MODERATE / WEAK / ASSESS / FAILURE]",
        "",
        "**Metrics**:",
        "- (A) Score 3+ reply rate: [X%]",
        "- (B) Constituencies at strong threshold: [X of 7]",
        "- (C) Cross-org references: [X]",
        "- (D) Confirmed adoptions: [X]",
        "",
        "**Phase 2 decisions**:",
        "- Domain 39: [status]",
        "- Domain 56: [status]",
        "- Domain 58: [status]",
        "- Domain 59: [status]",
        "- Tier 2 expansion: [status]",
        "",
        "**Next checkpoint**: [Day 60, July 27 / other]",
        "---",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Phase 2 domain tracker integration
# ---------------------------------------------------------------------------

def _import_phase2_trackers():
    """
    Lazily import Phase 2 domain trackers from src/phase_2_domain_trackers.py.

    Returns the run_all_monitors_parallel function, or None if the module
    is not available (e.g., monitors package not installed).
    """
    try:
        import sys as _sys
        _src = str(PHASE2_SRC_DIR)
        if _src not in _sys.path:
            _sys.path.insert(0, _src)
        from phase_2_domain_trackers import run_all_monitors_parallel
        return run_all_monitors_parallel
    except ImportError as exc:
        logger.warning(f"Phase 2 domain trackers not available: {exc}")
        logger.warning(f"Expected module at: {PHASE2_SRC_DIR / 'phase_2_domain_trackers.py'}")
        return None


def run_phase2_parallel(config: Dict) -> Dict:
    """
    Run all four Phase 2 domain monitors in parallel alongside the Phase 1
    Gist-polling workflow.

    Invoked from run_collection() when --run-phase2 flag is set, or from
    --run-all which runs both Phase 1 and Phase 2 together.

    Args:
        config: Loaded config dict (same one used by Phase 1)

    Returns:
        Phase 2 summary dict from run_all_monitors_parallel(), or an error dict
        if the module could not be imported.
    """
    runner = _import_phase2_trackers()
    if runner is None:
        return {
            "error": "phase_2_domain_trackers module not importable",
            "hint": f"Verify {PHASE2_SRC_DIR / 'phase_2_domain_trackers.py'} exists",
        }

    logger.info("\n[PHASE 2] Launching domain-specific monitors in parallel...")
    try:
        result = runner(config=config)
        logger.info(
            f"[PHASE 2] Complete: "
            f"scotus={result.get('domain_58_scotus', {}).get('status', '?')} | "
            f"hhs={result.get('domain_39_hhs', {}).get('status', '?')} | "
            f"election={result.get('domain_40_election', {}).get('status', '?')} | "
            f"email={result.get('coalition_email_router', {}).get('status', '?')} | "
            f"alerts_sent={result.get('total_alerts_sent', 0)} | "
            f"urgent={result.get('has_urgent', False)}"
        )
        return result
    except Exception as exc:
        msg = f"Phase 2 parallel run failed: {exc}"
        logger.error(msg)
        return {"error": msg}


# ---------------------------------------------------------------------------
# Main collection workflow
# ---------------------------------------------------------------------------

def run_collection(config: Dict) -> Dict:
    """Execute the full weekly collection and return summary dict."""
    state = load_state()
    now = datetime.now(timezone.utc)
    detector = AlertDetector(config.get("phase1_start_date", "2026-05-28"))
    week = detector.week_number()
    day = detector.days_elapsed()

    logger.info("=" * 60)
    logger.info(f"Phase 1 Adoption Tracking — Week {week}, Day {day}")
    logger.info(f"Timestamp: {now.isoformat()}")
    logger.info("=" * 60)

    summary: Dict = {
        "timestamp":        now.isoformat(),
        "week_number":      week,
        "day_elapsed":      day,
        "gist_data":        {},
        "bitly_clicks":     {},
        "clicks_this_week": 0,
        "replies":          [],
        "alerts":           [],
        "errors":           [],
    }

    # Step 1: Poll Gists
    logger.info("\n[1/3] Polling GitHub Gist metadata...")
    gists = config.get("canonical_gists", CANONICAL_GISTS)
    poller = GistPoller(
        github_token=config.get("github_token", ""),
        username=config.get("github_username", CANONICAL_USERNAME),
    )
    try:
        summary["gist_data"] = poller.poll_all(gists)
        ok = sum(1 for v in summary["gist_data"].values() if v and "error" not in v)
        logger.info(f"  {ok}/{len(gists)} Gists fetched without error")
    except Exception as e:
        msg = f"Gist polling failed: {e}"
        logger.error(msg)
        summary["errors"].append(msg)

    # Step 1b: Bitly clicks (if configured)
    if config.get("bitly_enabled") and config.get("bitly_token") and config.get("bitly_links"):
        logger.info("\n[1b/3] Fetching Bitly click counts...")
        tracker = BitlyTracker(config["bitly_token"])
        try:
            summary["bitly_clicks"] = tracker.get_all(config["bitly_links"])
            summary["clicks_this_week"] = sum(v or 0 for v in summary["bitly_clicks"].values())
            logger.info(f"  Clicks this week: {summary['clicks_this_week']}")
        except Exception as e:
            msg = f"Bitly fetch failed: {e}"
            logger.error(msg)
            summary["errors"].append(msg)
    else:
        logger.info("\n[1b/3] Bitly: not configured — manual dashboard check required")
        logger.info("  To enable: set bitly_token and bitly_links in config")

    # Step 2: Gmail replies
    logger.info("\n[2/3] Fetching Gmail replies...")
    if config.get("gmail_enabled") and config.get("gmail_credentials"):
        monitor = GmailMonitor(
            credentials_path=config["gmail_credentials"],
            label=config.get("gmail_label", DEFAULT_GMAIL_LABEL),
        )
        try:
            summary["replies"] = monitor.get_recent_replies(
                lookback_hours=config.get("email_lookback_hours", 168)
            )
            logger.info(f"  {len(summary['replies'])} replies retrieved")
        except Exception as e:
            msg = f"Gmail fetch failed: {e}"
            logger.error(msg)
            summary["errors"].append(msg)
    else:
        logger.info("  Gmail not configured — set gmail_enabled: true and gmail_credentials path")

    # Step 3: Alert detection
    logger.info("\n[3/3] Running alert detection...")
    prev_cumulative = state.get("cumulative_clicks", 0)
    cumulative = prev_cumulative + summary["clicks_this_week"]
    summary["alerts"] = detector.evaluate(
        clicks_this_week=summary["clicks_this_week"],
        cumulative_clicks=cumulative,
        reply_count=len(summary["replies"]),
    )
    logger.info(f"  {len(summary['alerts'])} alert(s) — check output for details")

    # Save weekly summary
    summary_text = generate_weekly_summary(
        week=week, day=day,
        gist_data=summary["gist_data"],
        replies=summary["replies"],
        alerts=summary["alerts"],
        cumulative_clicks=cumulative,
        clicks_this_week=summary["clicks_this_week"],
    )
    summary_path = DATA_DIR / f"week-{week:02d}-{now.strftime('%Y-%m-%d')}-summary.md"
    summary_path.write_text(summary_text, encoding="utf-8")
    logger.info(f"\nWeekly summary: {summary_path}")

    # Save raw JSON
    raw_path = DATA_DIR / f"week-{week:02d}-raw.json"
    with open(raw_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)

    # Update cumulative Gist log (migrate old dict format to list if necessary)
    gist_log_path = DATA_DIR / "gist-view-tracking.json"
    if gist_log_path.exists():
        raw = json.loads(gist_log_path.read_text())
        gist_log = raw if isinstance(raw, list) else []
    else:
        gist_log = []
    gist_log.append({"week": week, "date": now.isoformat(), "gist_data": summary["gist_data"]})
    gist_log_path.write_text(json.dumps(gist_log, indent=2, default=str))

    # Persist state
    state.update({
        "last_run":         now.isoformat(),
        "week_number":      week,
        "cumulative_clicks": cumulative,
        "first_run":        state.get("first_run") or now.isoformat(),
    })
    state.setdefault("run_history", []).append({
        "week":    week,
        "date":    now.isoformat(),
        "clicks":  summary["clicks_this_week"],
        "replies": len(summary["replies"]),
        "alerts":  len(summary["alerts"]),
    })
    save_state(state)

    # Escalate to CHECKIN.md
    append_to_checkin(summary["alerts"], week)

    logger.info("=" * 60)
    logger.info(f"Done — Week {week} | {summary['clicks_this_week']} clicks | "
                f"{len(summary['replies'])} replies | {len(summary['alerts'])} alerts")
    logger.info("=" * 60)

    return summary


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 1 Adoption Tracking — v2.1 (Phase 2 integrated)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  --check-config      Validate configuration (run this first)
  --run-now           Execute Phase 1 Gist/email weekly collection
  --run-phase2        Execute Phase 2 domain monitors only (parallel)
  --run-all           Execute Phase 1 + Phase 2 together (recommended for cron)
  --schedule-weekly   Print crontab entries for weekly scheduling
  --day7-report       Print Day 7 checkpoint decision template
  --day30-report      Print Day 30 checkpoint decision template

Phase 2 monitors (run via --run-phase2 or --run-all):
  Domain 58 SCOTUS    Trump v. Barbara ruling (<15 min alert)
  Domain 39 HHS       Federal Register / HHS healthcare guidance (hourly)
  Domain 40 Election  FEC + election/deepfake news (4-hourly)
  Coalition Router    Gmail auto-tag by domain keyword (hourly)
        """,
    )
    parser.add_argument("--run-now",          action="store_true",
                        help="Phase 1 weekly collection (Gist + email)")
    parser.add_argument("--run-phase2",       action="store_true",
                        help="Phase 2 domain monitors only (parallel)")
    parser.add_argument("--run-all",          action="store_true",
                        help="Phase 1 + Phase 2 together (recommended)")
    parser.add_argument("--check-config",     action="store_true")
    parser.add_argument("--schedule-weekly",  action="store_true")
    parser.add_argument("--day7-report",      action="store_true")
    parser.add_argument("--day30-report",     action="store_true")
    parser.add_argument("--config", default=str(CONFIG_PATH))
    args = parser.parse_args()

    if args.check_config:
        check_config()
        return 0

    if args.schedule_weekly:
        script = Path(__file__).resolve()
        cron_p1 = f"0 9 * * 1 /usr/bin/python3 {script} --run-now --config {CONFIG_PATH}"
        cron_p2 = f"*/14 * * * * /usr/bin/python3 {script} --run-phase2 --config {CONFIG_PATH}"
        cron_all = f"0 9 * * 1 /usr/bin/python3 {script} --run-all --config {CONFIG_PATH}"
        print()
        print("Crontab entries:")
        print()
        print("# Phase 1 only — weekly Gist + email collection (Monday 09:00 UTC)")
        print(f"  {cron_p1}")
        print()
        print("# Phase 2 only — domain monitors every 14 minutes (SCOTUS sub-15min SLA)")
        print(f"  {cron_p2}")
        print()
        print("# Full suite — Phase 1 + Phase 2 every Monday (simpler single cron)")
        print(f"  {cron_all}")
        print()
        print("Install: crontab -e  then add preferred entry above")
        print("Verify:  crontab -l | grep adoption-tracking")
        return 0

    if args.day7_report:
        print(generate_day7_report(load_state()))
        return 0

    if args.day30_report:
        print(generate_day30_report())
        return 0

    if args.run_now:
        config = load_config()
        result = run_collection(config)
        print(f"\nPhase 1 result: week {result['week_number']} | "
              f"{result['clicks_this_week']} clicks | "
              f"{len(result['replies'])} replies | "
              f"{len(result['alerts'])} alerts | "
              f"{len(result['errors'])} errors")
        return 0

    if args.run_phase2:
        config = load_config()
        p2_result = run_phase2_parallel(config)
        if "error" in p2_result and len(p2_result) == 1:
            print(f"\nPhase 2 FAILED: {p2_result['error']}")
            return 1
        print(json.dumps(p2_result, indent=2, default=str))
        return 0 if not p2_result.get("errors") else 1

    if args.run_all:
        config = load_config()
        errors: list = []

        # Run Phase 1 and Phase 2 concurrently via ThreadPoolExecutor
        # Phase 1 is IO-bound (GitHub + Gmail API calls); safe for threads
        with ThreadPoolExecutor(max_workers=2, thread_name_prefix="adoption-suite") as pool:
            p1_future = pool.submit(run_collection, config)
            p2_future = pool.submit(run_phase2_parallel, config)

            p1_result: Dict = {}
            p2_result: Dict = {}

            for future in as_completed([p1_future, p2_future]):
                if future is p1_future:
                    try:
                        p1_result = future.result(timeout=120)
                    except Exception as exc:
                        msg = f"Phase 1 collection failed: {exc}"
                        logger.error(msg)
                        errors.append(msg)
                        p1_result = {"week_number": "?", "clicks_this_week": 0,
                                     "replies": [], "alerts": [], "errors": [msg]}
                else:
                    try:
                        p2_result = future.result(timeout=120)
                    except Exception as exc:
                        msg = f"Phase 2 monitors failed: {exc}"
                        logger.error(msg)
                        errors.append(msg)
                        p2_result = {"errors": [msg]}

        print(f"\nPhase 1: week {p1_result.get('week_number', '?')} | "
              f"{p1_result.get('clicks_this_week', 0)} clicks | "
              f"{len(p1_result.get('replies', []))} replies | "
              f"{len(p1_result.get('alerts', []))} alerts | "
              f"{len(p1_result.get('errors', []))} errors")
        print(f"Phase 2: "
              f"scotus={p2_result.get('domain_58_scotus', {}).get('status', '?')} | "
              f"hhs={p2_result.get('domain_39_hhs', {}).get('status', '?')} | "
              f"election={p2_result.get('domain_40_election', {}).get('status', '?')} | "
              f"email={p2_result.get('coalition_email_router', {}).get('status', '?')} | "
              f"alerts={p2_result.get('total_alerts_sent', 0)} | "
              f"urgent={p2_result.get('has_urgent', False)}")

        return 0 if not errors else 1

    # Default: show help + config check
    parser.print_help()
    print()
    check_config()
    return 0


if __name__ == "__main__":
    sys.exit(main())
