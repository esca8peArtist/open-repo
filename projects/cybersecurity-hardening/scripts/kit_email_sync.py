#!/usr/bin/env python3
"""
kit_email_sync.py — Kit (ConvertKit) to Google Sheets email engagement sync
Phase 1 measurement automation for cybersecurity-hardening project
Run daily at 20:00 UTC via cron: 0 20 * * * /path/to/kit_email_sync.py

Pulls open/click/reply metrics for each broadcast by email ID
and writes rows to the Email Engagement Log tab in Google Sheets.

Dependencies (all stdlib or pip-installable, no CLI tools required):
    pip install requests google-auth google-auth-oauthlib google-api-python-client
"""

import os
import sys
import json
import datetime
import time
import logging
import requests

# Google Sheets API
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ---------------------------------------------------------------------------
# CONFIGURATION — copy values from config/measurement_env_template.txt
# ---------------------------------------------------------------------------

KIT_API_SECRET   = os.environ.get("KIT_API_SECRET", "")        # v3 API secret
KIT_API_BASE     = "https://api.convertkit.com/v3"
SHEETS_CREDS_JSON = os.environ.get("SHEETS_CREDS_JSON", "")    # path to service-account JSON
SPREADSHEET_ID   = os.environ.get("SPREADSHEET_ID", "")        # Google Sheets ID from URL
ENGAGEMENT_TAB   = "Email Engagement Log"                       # exact tab name
KPI_TAB          = "KPI Summary Dashboard"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# KIT API HELPERS
# ---------------------------------------------------------------------------

def _kit_get(endpoint: str, params: dict | None = None, retries: int = 3) -> dict:
    """GET request to Kit v3 API with retry on 429/5xx."""
    url = f"{KIT_API_BASE}/{endpoint}"
    p = {"api_secret": KIT_API_SECRET}
    if params:
        p.update(params)
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, params=p, timeout=20)
            if r.status_code == 429:
                wait = int(r.headers.get("Retry-After", 60))
                log.warning("Rate-limited by Kit API — sleeping %ds (attempt %d)", wait, attempt)
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as exc:
            log.error("Kit API error attempt %d/%d: %s", attempt, retries, exc)
            if attempt == retries:
                raise
            time.sleep(5 * attempt)
    return {}


def fetch_broadcasts() -> list[dict]:
    """Return list of broadcasts (emails) from Kit account."""
    data = _kit_get("broadcasts", {"page": 1})
    broadcasts = data.get("broadcasts", [])
    log.info("Fetched %d broadcasts from Kit", len(broadcasts))
    return broadcasts


def fetch_broadcast_stats(broadcast_id: int) -> dict:
    """Return open/click stats for a single broadcast."""
    data = _kit_get(f"broadcasts/{broadcast_id}/stats")
    return data.get("broadcast", {}).get("stats", {})


def fetch_subscribers_for_broadcast(broadcast_id: int) -> list[dict]:
    """
    Return subscriber-level data for a broadcast.
    Kit v3 exposes this via the subscribers endpoint filtered by tag or
    segment; for a single broadcast, use the broadcast recipients call
    (available in Kit Creator plans).  Falls back to aggregate stats only.
    """
    try:
        data = _kit_get(f"broadcasts/{broadcast_id}/subscribers", {"page": 1})
        return data.get("subscribers", [])
    except Exception:
        log.warning("Subscriber-level data not available for broadcast %d — using aggregate", broadcast_id)
        return []

# ---------------------------------------------------------------------------
# GOOGLE SHEETS HELPERS
# ---------------------------------------------------------------------------

def _sheets_service():
    """Build authenticated Sheets API service from service-account credentials."""
    if not SHEETS_CREDS_JSON or not os.path.exists(SHEETS_CREDS_JSON):
        raise FileNotFoundError(
            f"Service account JSON not found at '{SHEETS_CREDS_JSON}'. "
            "Set SHEETS_CREDS_JSON env variable to the correct path."
        )
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(SHEETS_CREDS_JSON, scopes=scopes)
    return build("sheets", "v4", credentials=creds, cache_discovery=False)


def append_rows(service, tab: str, rows: list[list]) -> None:
    """Append rows to the named tab in the configured spreadsheet."""
    range_name = f"'{tab}'!A1"
    body = {"values": rows}
    try:
        service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=range_name,
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body=body,
        ).execute()
        log.info("Appended %d row(s) to tab '%s'", len(rows), tab)
    except HttpError as exc:
        log.error("Sheets API error writing to '%s': %s", tab, exc)
        raise


def read_existing_broadcast_ids(service, tab: str) -> set[str]:
    """Return set of broadcast IDs already logged to avoid duplicate rows."""
    range_name = f"'{tab}'!A:A"
    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=range_name,
        ).execute()
        values = result.get("values", [])
        return {str(row[0]) for row in values if row}
    except HttpError:
        return set()

# ---------------------------------------------------------------------------
# SYNC LOGIC
# ---------------------------------------------------------------------------

def build_engagement_row(broadcast: dict, stats: dict) -> list:
    """Map Kit broadcast + stats fields to the Email Engagement Log columns."""
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    send_date = (broadcast.get("published_at") or broadcast.get("created_at") or "")[:10]
    subject   = broadcast.get("subject", "")
    b_id      = broadcast.get("id", "")

    recipients   = stats.get("recipients", 0)
    opens        = stats.get("open_rate", 0.0)   # Kit returns as decimal 0.0–1.0
    clicks       = stats.get("click_rate", 0.0)
    unsubscribes = stats.get("unsubscribes", 0)

    open_pct  = round(opens * 100, 1) if opens else 0.0
    click_pct = round(clicks * 100, 1) if clicks else 0.0

    return [
        str(b_id),          # A: Broadcast ID
        send_date,          # B: Email Date
        subject,            # C: Subject Line
        recipients,         # D: Recipients
        open_pct,           # E: Open Rate %
        click_pct,          # F: Click Rate %
        unsubscribes,       # G: Unsubscribes
        "",                 # H: Reply Y/N (manual — cannot be pulled from Kit)
        "",                 # I: Sentiment (manual)
        now,                # J: Last Synced
    ]


def run_sync() -> None:
    """Main sync: pull Kit broadcasts, write new rows to Sheets."""
    if not KIT_API_SECRET:
        log.error("KIT_API_SECRET is not set. Export the env variable and retry.")
        sys.exit(1)
    if not SPREADSHEET_ID:
        log.error("SPREADSHEET_ID is not set. Export the env variable and retry.")
        sys.exit(1)

    log.info("Starting Kit → Sheets sync")
    service = _sheets_service()
    existing_ids = read_existing_broadcast_ids(service, ENGAGEMENT_TAB)
    log.info("Found %d existing broadcast IDs in Sheets", len(existing_ids))

    broadcasts = fetch_broadcasts()
    new_rows = []

    for b in broadcasts:
        bid = str(b.get("id", ""))
        if bid in existing_ids:
            log.debug("Broadcast %s already logged — skipping", bid)
            continue

        stats = fetch_broadcast_stats(int(bid))
        row   = build_engagement_row(b, stats)
        new_rows.append(row)
        log.info("Queued broadcast %s (%s) — opens %.1f%% clicks %.1f%%",
                 bid, b.get("subject", "?")[:40], row[4], row[5])
        time.sleep(0.5)  # polite rate-spacing between stat requests

    if new_rows:
        append_rows(service, ENGAGEMENT_TAB, new_rows)
        log.info("Sync complete — %d new broadcast(s) written", len(new_rows))
    else:
        log.info("Sync complete — no new broadcasts to write")


# ---------------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run_sync()
