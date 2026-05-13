#!/usr/bin/env python3
"""
discord_daily_briefing.py — Daily 20:00 UTC engagement briefing to Discord
Phase 1 measurement automation for cybersecurity-hardening project
Run daily at 20:00 UTC via cron: 0 20 * * * /path/to/discord_daily_briefing.py

Reads KPI data from Google Sheets, computes trend and anomaly signals,
then posts a formatted status briefing to a Discord channel via webhook.

Status levels:
  GREEN  — all KPIs at or above target
  YELLOW — any KPI in warning band (90-100% of target)
  RED    — any KPI below warning threshold (triggers escalation language)

Dependencies (all pip-installable, no CLI tools required):
    pip install requests google-auth google-auth-oauthlib google-api-python-client
"""

import os
import sys
import json
import datetime
import logging
import requests

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")
SHEETS_CREDS_JSON   = os.environ.get("SHEETS_CREDS_JSON", "")
SPREADSHEET_ID      = os.environ.get("SPREADSHEET_ID", "")

KPI_TAB             = "KPI Summary Dashboard"
ENGAGEMENT_TAB      = "Email Engagement Log"
MEETING_TAB         = "Meeting Schedule"
POLICY_TAB          = "Policy Uptake Signals"

# KPI thresholds from TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md
THRESHOLDS = {
    "click_rate":      {"target": 45.0, "warning": 30.0, "unit": "%"},
    "reply_rate":      {"target": 20.0, "warning": 10.0, "unit": "%"},
    "stage1_ratio":    {"target": 60.0, "warning": 40.0, "unit": "%"},
    "meeting_rate":    {"target": 60.0, "warning": 30.0, "unit": "%"},
    "adoption_rate":   {"target": 10.0, "warning": 5.0,  "unit": "%"},
    "bounce_rate":     {"target": 5.0,  "warning": 8.0,  "unit": "% (lower is better)"},
}

# Campaign Day 1 = June 1, 2026
PHASE_1_START = datetime.date(2026, 6, 1)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# GOOGLE SHEETS READER
# ---------------------------------------------------------------------------

def _sheets_service():
    if not SHEETS_CREDS_JSON or not os.path.exists(SHEETS_CREDS_JSON):
        raise FileNotFoundError(
            f"Service account JSON not found at '{SHEETS_CREDS_JSON}'. "
            "Set SHEETS_CREDS_JSON env variable."
        )
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    creds = Credentials.from_service_account_file(SHEETS_CREDS_JSON, scopes=scopes)
    return build("sheets", "v4", credentials=creds, cache_discovery=False)


def read_tab(service, tab: str, range_suffix: str = "") -> list[list[str]]:
    range_name = f"'{tab}'!A1:Z500" if not range_suffix else f"'{tab}'!{range_suffix}"
    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=range_name,
        ).execute()
        return result.get("values", [])
    except HttpError as exc:
        log.error("Sheets read error for tab '%s': %s", tab, exc)
        return []

# ---------------------------------------------------------------------------
# KPI PARSING
# ---------------------------------------------------------------------------

def safe_float(val: str | None, default: float = 0.0) -> float:
    try:
        return float(str(val).replace("%", "").strip())
    except (TypeError, ValueError):
        return default


def safe_int(val: str | None, default: int = 0) -> int:
    try:
        return int(str(val).replace(",", "").strip())
    except (TypeError, ValueError):
        return default


def parse_kpi_tab(rows: list[list[str]]) -> dict:
    """
    Parse the KPI Summary Dashboard tab.
    Expected row structure (from TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md Tab 5):
      Row 1: header
      Rows 2–17: [Metric, Week1, Week2, Week3, Final]
    Returns dict keyed by metric name with list of weekly values.
    """
    kpi = {}
    if not rows:
        return kpi
    header = rows[0] if rows else []
    for row in rows[1:]:
        if not row:
            continue
        metric = row[0].strip() if row else ""
        values = row[1:]  # weekly columns
        kpi[metric] = [safe_float(v) for v in values]
    return kpi


def current_week_number() -> int:
    today = datetime.date.today()
    delta = (today - PHASE_1_START).days
    return max(1, (delta // 7) + 1)


def get_latest_kpi_value(kpi: dict, metric_key: str) -> float:
    """Return the most recent non-zero weekly value for a metric."""
    values = kpi.get(metric_key, [])
    for v in reversed(values):
        if v > 0:
            return v
    return 0.0


def get_7d_trend(kpi: dict, metric_key: str) -> str:
    """Return trend arrow comparing last two non-zero weekly values."""
    values = [v for v in kpi.get(metric_key, []) if v > 0]
    if len(values) < 2:
        return "—"
    delta = values[-1] - values[-2]
    if delta > 1.0:
        return "↑"
    elif delta < -1.0:
        return "↓"
    return "→"

# ---------------------------------------------------------------------------
# STATUS CLASSIFICATION
# ---------------------------------------------------------------------------

def classify_kpi(metric: str, value: float) -> str:
    """Return GREEN / YELLOW / RED status for a KPI value."""
    t = THRESHOLDS.get(metric, {})
    target  = t.get("target", 0.0)
    warning = t.get("warning", 0.0)

    # Bounce rate: lower is better — invert logic
    if metric == "bounce_rate":
        if value <= target:
            return "GREEN"
        elif value <= warning:
            return "YELLOW"
        return "RED"

    pct_of_target = (value / target * 100) if target else 0
    if pct_of_target >= 100:
        return "GREEN"
    elif pct_of_target >= 90:
        return "YELLOW"
    elif value >= warning:
        return "YELLOW"
    return "RED"


def overall_status(statuses: list[str]) -> str:
    if "RED" in statuses:
        return "RED"
    if "YELLOW" in statuses:
        return "YELLOW"
    return "GREEN"


STATUS_EMOJI = {"GREEN": "✅", "YELLOW": "⚠️", "RED": "🚨"}
STATUS_LABEL = {"GREEN": "GREEN", "YELLOW": "YELLOW", "RED": "RED  — ESCALATION REQUIRED"}

# ---------------------------------------------------------------------------
# ANOMALY DETECTION
# ---------------------------------------------------------------------------

def detect_anomalies(kpi: dict, meetings_count: int, policy_signals: int) -> list[str]:
    """
    Check the 5 anomaly triggers from the measurement framework.
    Returns list of anomaly description strings (empty list = no anomalies).
    """
    anomalies = []

    # Trigger 1: Wave 1 reply rate below 15%
    reply_rate = get_latest_kpi_value(kpi, "Reply rate %")
    if reply_rate > 0 and reply_rate < 15.0:
        anomalies.append(
            f"Reply rate is {reply_rate:.1f}% — below the 15% Wave 1 minimum. "
            "Check contact routing (named individual vs. general inbox)."
        )

    # Trigger 2: Adoption below 5%
    adoption = get_latest_kpi_value(kpi, "Adoption signals logged")
    sends     = get_latest_kpi_value(kpi, "Total sends")
    if sends > 0:
        adoption_rate = (adoption / sends * 100)
        if adoption_rate < 5.0 and current_week_number() >= 4:
            anomalies.append(
                f"Adoption rate is {adoption_rate:.1f}% (Week 4+). "
                "Week-4 follow-up emails needed — zero adoption signals at Week 6 triggers Scenario 4."
            )

    # Trigger 3: No meetings scheduled (Days 1-21)
    if meetings_count == 0 and current_week_number() >= 2:
        anomalies.append(
            "Zero briefing calls scheduled. "
            "Replace vague CTAs with a specific 20-minute offer + Calendly link in all follow-ups."
        )

    # Trigger 4: Zero policy uptake signals for 7+ days
    if policy_signals == 0 and current_week_number() >= 3:
        anomalies.append(
            "No policy uptake signals logged in the past 7 days. "
            "Check Tab 4 entries — ensure post-meeting notes are being captured."
        )

    # Trigger 5: Bounce rate elevated
    bounces = get_latest_kpi_value(kpi, "Bounce rate %")
    if bounces >= 5.0:
        anomalies.append(
            f"Bounce rate is {bounces:.1f}% — above the 5% warning threshold. "
            "Stop wave sends and re-validate all remaining contact emails before proceeding."
        )

    return anomalies

# ---------------------------------------------------------------------------
# DISCORD PAYLOAD BUILDER
# ---------------------------------------------------------------------------

def build_discord_message(kpi: dict, meetings_count: int, policy_signals: int) -> dict:
    today    = datetime.date.today()
    camp_day = (today - PHASE_1_START).days + 1
    week_num = current_week_number()
    now_utc  = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # Collect KPI lines
    metric_map = {
        "click_rate":   "Bitly Click Rate %",
        "reply_rate":   "Reply rate %",
        "stage1_ratio": "Stage 1+ ratio %",
        "meeting_rate": "Meeting rate %",
        "bounce_rate":  "Bounce rate %",
    }

    kpi_lines = []
    kpi_statuses = []
    for key, sheet_name in metric_map.items():
        value  = get_latest_kpi_value(kpi, sheet_name)
        trend  = get_7d_trend(kpi, sheet_name)
        status = classify_kpi(key, value)
        kpi_statuses.append(status)
        t = THRESHOLDS[key]
        kpi_lines.append(
            f"{STATUS_EMOJI[status]} **{sheet_name}**: {value:.1f}{t['unit']} "
            f"(target: {t['target']}{t['unit']}) {trend}"
        )

    adoption_key = "Adoption signals logged"
    adoption_val = get_latest_kpi_value(kpi, adoption_key)
    sends_val    = get_latest_kpi_value(kpi, "Total sends")
    adoption_pct = round(adoption_val / sends_val * 100, 1) if sends_val else 0.0
    adopt_status = classify_kpi("adoption_rate", adoption_pct)
    kpi_statuses.append(adopt_status)
    kpi_lines.append(
        f"{STATUS_EMOJI[adopt_status]} **Adoption signals**: {int(adoption_val)} "
        f"({adoption_pct:.1f}% of {int(sends_val)} sends) — target 10% by Week 6"
    )

    overall = overall_status(kpi_statuses)
    anomalies = detect_anomalies(kpi, meetings_count, policy_signals)

    # Sparkline note (Sheets handles actual sparklines; we report trend text here)
    trend_summary = "7-day trend: " + ", ".join(
        f"{THRESHOLDS[k]['unit'].replace('% ','').strip() or k}: {get_7d_trend(kpi, v)}"
        for k, v in metric_map.items()
    )

    lines = [
        f"## Phase 1 Daily Briefing — {now_utc}",
        f"**Campaign Day {camp_day}  |  Week {week_num}**",
        f"**Overall Status: {STATUS_EMOJI[overall]} {STATUS_LABEL[overall]}**",
        "",
        "### KPI Snapshot",
        *kpi_lines,
        "",
        f"_Meetings confirmed: {meetings_count}  |  Policy signals logged: {policy_signals}_",
        f"_{trend_summary}_",
    ]

    if anomalies:
        lines += [
            "",
            "### Anomaly Triggers",
            *[f"- {a}" for a in anomalies],
        ]

    if overall == "RED":
        lines += [
            "",
            "**Action required**: Review escalation matrix in TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md "
            "Section 3 and apply the relevant Warning Trigger protocol before the next send window.",
        ]
    elif overall == "YELLOW":
        lines += [
            "",
            "_Yellow KPIs require monitoring — apply sector-specific follow-up adjustments "
            "before the next wave send._",
        ]
    else:
        lines.append("")
        lines.append("_All KPIs on track. No action required._")

    # Discord embeds via content field (plain webhook, no bot token needed)
    content = "\n".join(lines)
    return {"content": content}

# ---------------------------------------------------------------------------
# DISCORD SEND
# ---------------------------------------------------------------------------

def post_to_discord(payload: dict, retries: int = 3) -> None:
    if not DISCORD_WEBHOOK_URL:
        log.error("DISCORD_WEBHOOK_URL is not set. Export the env variable and retry.")
        sys.exit(1)

    headers = {"Content-Type": "application/json"}
    for attempt in range(1, retries + 1):
        try:
            r = requests.post(
                DISCORD_WEBHOOK_URL,
                data=json.dumps(payload),
                headers=headers,
                timeout=15,
            )
            if r.status_code == 429:
                retry_after = r.json().get("retry_after", 5)
                log.warning("Discord rate-limited — sleeping %.1fs", retry_after)
                import time; import time as _t; _t.sleep(retry_after)
                continue
            if r.status_code not in (200, 204):
                log.error("Discord webhook returned %d: %s", r.status_code, r.text[:200])
                r.raise_for_status()
            log.info("Discord briefing posted successfully (HTTP %d)", r.status_code)
            return
        except requests.exceptions.RequestException as exc:
            log.error("Discord post attempt %d/%d failed: %s", attempt, retries, exc)
            if attempt == retries:
                raise
            import time as _t; _t.sleep(5 * attempt)

# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def count_meetings(rows: list[list[str]]) -> int:
    """Count rows in Meeting Schedule tab with status Completed or Scheduled."""
    count = 0
    for row in rows[1:]:  # skip header
        if len(row) >= 7:
            status = row[6].strip().lower()
            if status in ("completed", "scheduled"):
                count += 1
    return count


def count_policy_signals(rows: list[list[str]]) -> int:
    """Count non-empty signal rows in Policy Uptake Signals tab."""
    count = 0
    for row in rows[1:]:  # skip header
        if row and row[0].strip():
            count += 1
    return count


def run() -> None:
    if not SPREADSHEET_ID:
        log.error("SPREADSHEET_ID is not set. Export the env variable and retry.")
        sys.exit(1)

    log.info("Connecting to Google Sheets")
    service = _sheets_service()

    log.info("Reading KPI tab")
    kpi_rows     = read_tab(service, KPI_TAB)
    kpi          = parse_kpi_tab(kpi_rows)

    log.info("Reading Meeting Schedule tab")
    meeting_rows = read_tab(service, MEETING_TAB)
    meetings_n   = count_meetings(meeting_rows)

    log.info("Reading Policy Uptake Signals tab")
    policy_rows  = read_tab(service, POLICY_TAB)
    policy_n     = count_policy_signals(policy_rows)

    log.info("Building Discord payload")
    payload = build_discord_message(kpi, meetings_n, policy_n)

    log.info("Posting to Discord")
    post_to_discord(payload)
    log.info("Daily briefing complete")


if __name__ == "__main__":
    run()
