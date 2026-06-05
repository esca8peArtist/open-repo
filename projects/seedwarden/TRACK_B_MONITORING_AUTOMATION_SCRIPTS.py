#!/usr/bin/env python3
"""
Track B Day 3/7/14 Checkpoint Automation Scripts
Item 85 — Seedwarden Project

Automated monitoring for Track B post-launch phase.
Integrates Campaign Monitor, GitHub Gist, Etsy, and Kit Creator (ConvertKit)
into a single orchestrated checkpoint runner that applies the contingency
decision tree from CONTINGENCY_TRIGGER_DECISION_TREE.md and writes a
dated markdown report to CHECKPOINT_REPORTS/.

Launch date:       2026-06-04 (Track B)
Day 3 checkpoint:  2026-06-07 09:00 UTC  (automated via cron)
Day 7 checkpoint:  2026-06-11 10:00 UTC
Day 14 checkpoint: 2026-06-18 11:00 UTC

Usage:
    uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --day 3
    uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --day 7
    uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --day 14
    uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --day 3 --dry-run

Environment variables (load from ~/.claude_env or export before running):
    CAMPAIGN_MONITOR_API_KEY  — Campaign Monitor API key
    CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL1 through EMAIL5 — per-template campaign IDs
    CAMPAIGN_MONITOR_LIST_ID  — subscriber list ID
    GIST_URL                  — full public URL of the Zone Card Gist
    ETSY_API_KEY              — Etsy API v3 key
    ETSY_SHOP_ID              — Etsy shop numeric ID
    KIT_API_KEY               — Kit Creator (ConvertKit) API key
    KIT_FORM_ID               — Kit landing page form ID
    DISCORD_WEBHOOK_URL       — optional; if set, posts summary to Discord
    LAUNCH_DATE               — ISO date string, default 2026-06-04
    CHECKPOINT_REPORTS_DIR    — override output dir, default projects/seedwarden/CHECKPOINT_REPORTS

No external dependencies beyond Python stdlib + requests.
Install requests: uv pip install requests
"""

import os
import re
import json
import sqlite3
import datetime
import argparse
import sys
import unittest
from typing import Optional

# ---------------------------------------------------------------------------
# Optional dependency: requests (stdlib-absent)
# ---------------------------------------------------------------------------
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

REQUESTS_MISSING_MSG = (
    "The 'requests' library is required. Install with: uv pip install requests"
)

# ---------------------------------------------------------------------------
# Constants — pulled from CONTINGENCY_TRIGGER_DECISION_TREE.md
# ---------------------------------------------------------------------------

LAUNCH_DATE_DEFAULT = datetime.date(2026, 6, 4)

# Checkpoint UTC hours (cron schedule)
CHECKPOINT_HOUR_DAY3 = 9
CHECKPOINT_HOUR_DAY7 = 10
CHECKPOINT_HOUR_DAY14 = 11

API_TIMEOUT = 30  # seconds — hard max per API call

CHECKPOINT_REPORTS_DIR_DEFAULT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "CHECKPOINT_REPORTS",
)

# Thresholds from CONTINGENCY_TRIGGER_DECISION_TREE.md (Threshold Master Table)
# and TRACK_B_MONITORING_AUTOMATION_FRAMEWORK.md
THRESHOLDS = {
    3: {
        "email_open_rate_pct": {"go": 20.0, "caution_lo": 10.0},
        "email_unsub_rate_pct": {"caution_hi": 5.0, "nogo_hi": 5.0},
        "gist_views": {"go": 70, "caution_lo": 30},
        "kit_new_subscribers": {"go": 5, "caution_lo": 1},
        "etsy_orders": {"go": 1},           # CAUTION = views but 0 sales
        "influencer_public_shares": {"go": 1, "nogo_lo": 0},
    },
    7: {
        "email_open_rate_pct": {"go": 20.0, "caution_lo": 10.0},
        "email_unsub_rate_pct": {"nogo_hi": 5.0},
        "gist_views": {"go": 200, "caution_lo": 100, "nogo_lo": 50},
        "kit_new_subscribers": {"go": 15, "caution_lo": 5, "nogo_lo": 5},
        "etsy_orders": {"go": 1, "nogo_lo": 0},
        "influencer_public_shares": {"go": 3, "caution_lo": 1, "nogo_lo": 0},
    },
    14: {
        "email_open_rate_pct": {"go": 20.0},
        "email_unsub_rate_pct": {"nogo_hi": 5.0},
        "gist_views": {"go": 400, "caution_lo": 150, "nogo_lo": 150},
        "kit_new_subscribers": {"go": 30, "caution_lo": 10, "nogo_lo": 10},
        "etsy_orders": {"go": 3, "caution_lo": 1},
        "influencer_public_shares": {"go": 3, "caution_lo": 1},
    },
}

# Email template IDs referenced in Item 59 (1-indexed, Email 1–5)
EMAIL_TEMPLATE_SLOTS = ["EMAIL1", "EMAIL2", "EMAIL3", "EMAIL4", "EMAIL5"]

# Etsy coupon codes for per-template attribution (from scope spec)
ETSY_COUPON_CODES = {
    "EMAIL1": "EMAIL1",
    "EMAIL2": "EMAIL2",
    "EMAIL3": "EMAIL3",
    "EMAIL4": "EMAIL4",
    "EMAIL5": "EMAIL5",
}


# ---------------------------------------------------------------------------
# Module 1: Campaign Monitor API Client
# ---------------------------------------------------------------------------

class CampaignMonitorClient:
    """
    Authenticates with Campaign Monitor API and fetches email metrics.

    Endpoint reference:
        GET /api/v3.2/campaigns/{campaign_id}/summary.json
        GET /api/v3.2/lists/{list_id}/stats.json

    Auth: HTTP Basic, API key as username, literal 'x' as password.
    """

    BASE_URL = "https://api.createsend.com/api/v3.2"

    def __init__(self, api_key: str, timeout: int = API_TIMEOUT):
        if not api_key:
            raise ValueError("CAMPAIGN_MONITOR_API_KEY is not set")
        self.api_key = api_key
        self.timeout = timeout
        self._auth = (api_key, "x")

    def _get(self, path: str) -> dict:
        """GET helper with timeout and structured error handling."""
        if not HAS_REQUESTS:
            raise RuntimeError(REQUESTS_MISSING_MSG)
        url = f"{self.BASE_URL}{path}"
        try:
            resp = requests.get(url, auth=self._auth, timeout=self.timeout)
            resp.raise_for_status()
            return resp.json()
        except requests.Timeout:
            raise RuntimeError(
                f"Campaign Monitor API timed out after {self.timeout}s "
                f"(URL: {url})"
            )
        except requests.HTTPError as exc:
            raise RuntimeError(
                f"Campaign Monitor API HTTP error {exc.response.status_code}: "
                f"{exc.response.text[:200]}"
            ) from exc
        except requests.RequestException as exc:
            raise RuntimeError(f"Campaign Monitor request failed: {exc}") from exc

    def fetch_campaign_summary(self, campaign_id: str) -> dict:
        """
        Fetch summary stats for a single campaign broadcast.

        Returns raw API dict with keys:
            TotalRecipients, UniqueOpened, Clicks, Unsubscribed, Bounced
        """
        if not campaign_id:
            raise ValueError("campaign_id must not be empty")
        return self._get(f"/campaigns/{campaign_id}/summary.json")

    def compute_template_metrics(self, campaign_id: str, template_label: str) -> dict:
        """
        Compute per-template metrics including open rate, click rate, unsub rate.

        Args:
            campaign_id: Campaign Monitor campaign ID
            template_label: Human label, e.g. 'EMAIL1'

        Returns:
            dict with keys: template, total_sent, open_rate_pct, click_rate_pct,
            unsub_rate_pct, bounces, unique_opens, clicks
        """
        raw = self.fetch_campaign_summary(campaign_id)
        total = raw.get("TotalRecipients", 0) or 1  # guard div-by-zero
        opens = raw.get("UniqueOpened", 0)
        clicks = raw.get("Clicks", 0)
        unsubs = raw.get("Unsubscribed", 0)
        bounces = raw.get("Bounced", 0)
        return {
            "template": template_label,
            "campaign_id": campaign_id,
            "total_sent": raw.get("TotalRecipients", 0),
            "unique_opens": opens,
            "clicks": clicks,
            "bounces": bounces,
            "unsubscribes": unsubs,
            "open_rate_pct": round(opens / total * 100, 2),
            "click_rate_pct": round(clicks / total * 100, 2),
            "unsub_rate_pct": round(unsubs / total * 100, 2),
        }

    def fetch_all_template_metrics(self, campaign_id_map: dict) -> list[dict]:
        """
        Fetch metrics for all templates in campaign_id_map.

        Args:
            campaign_id_map: dict mapping template label -> campaign_id
                e.g. {"EMAIL1": "abc123", "EMAIL2": "def456"}

        Returns:
            List of per-template metric dicts (same shape as compute_template_metrics)
            Skips templates with missing IDs with a warning.
        """
        results = []
        for label, cid in campaign_id_map.items():
            if not cid:
                print(
                    f"  [CM] WARNING: no campaign ID configured for {label}, skipping",
                    file=sys.stderr,
                )
                continue
            try:
                metrics = self.compute_template_metrics(cid, label)
                results.append(metrics)
            except RuntimeError as exc:
                print(f"  [CM] ERROR fetching {label}: {exc}", file=sys.stderr)
        return results

    def detect_anomalies(self, template_metrics: list[dict]) -> list[str]:
        """
        Detect anomalies across all templates.

        Current rule set (from Item 85 scope):
        - Flag >30% open-rate drop between consecutive emails as low-engagement warning.
        - Flag unsub rate > 5% on any template as NO-GO trigger.
        - Flag open rate < 10% on any template as deliverability concern.

        Returns:
            List of human-readable warning strings (empty if clean).
        """
        warnings = []
        prev_open = None
        for m in template_metrics:
            label = m["template"]
            open_rate = m["open_rate_pct"]
            unsub_rate = m["unsub_rate_pct"]

            # Rule 1: >30% drop from previous template
            if prev_open is not None and prev_open > 0:
                drop_pct = (prev_open - open_rate) / prev_open * 100
                if drop_pct > 30:
                    warnings.append(
                        f"LOW-ENGAGEMENT WARNING: {label} open rate ({open_rate:.1f}%) "
                        f"dropped {drop_pct:.0f}% from previous email "
                        f"({prev_open:.1f}%)"
                    )
            prev_open = open_rate

            # Rule 2: high unsubscribe
            if unsub_rate > 5.0:
                warnings.append(
                    f"NO-GO TRIGGER: {label} unsubscribe rate {unsub_rate:.1f}% "
                    f"exceeds 5% threshold (Scenario 5)"
                )

            # Rule 3: deliverability concern
            if open_rate < 10.0:
                warnings.append(
                    f"DELIVERABILITY CONCERN: {label} open rate {open_rate:.1f}% "
                    f"is below 10% (Scenario 1 NO-GO)"
                )
        return warnings


# ---------------------------------------------------------------------------
# Module 2: Gist View Count Poller
# ---------------------------------------------------------------------------

class GistViewPoller:
    """
    Fetches the view count for a public GitHub Gist by scraping the HTML.

    GitHub's API does not expose view counts for Gists (confirmed in
    TRACK_B_MONITORING_AUTOMATION_FRAMEWORK.md, Metric 2 note).
    The view count appears in the page HTML as text near "views".
    """

    # Regex patterns targeting the Gist page counter format
    _VIEW_PATTERNS = [
        re.compile(r'(\d[\d,]*)\s*view', re.IGNORECASE),
        re.compile(r'"viewCount"\s*:\s*(\d+)'),
        re.compile(r'data-view-count="(\d+)"'),
    ]

    def __init__(
        self,
        gist_url: str,
        baseline_views: int = 0,
        timeout: int = API_TIMEOUT,
    ):
        """
        Args:
            gist_url: Full HTTPS URL of the public Gist.
            baseline_views: Day 0 view count to compute delta growth.
            timeout: Request timeout in seconds.
        """
        if not gist_url:
            raise ValueError("GIST_URL is not set")
        self.gist_url = gist_url
        self.baseline_views = baseline_views
        self.timeout = timeout

    def fetch_view_count(self) -> int:
        """
        Fetch and parse the view count from the Gist HTML page.

        Returns:
            Integer view count (cumulative since Gist creation).

        Raises:
            RuntimeError if the page cannot be fetched or count cannot be parsed.
        """
        if not HAS_REQUESTS:
            raise RuntimeError(REQUESTS_MISSING_MSG)
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 "
                "Seedwarden-Monitor/1.0"
            ),
            "Accept": "text/html,application/xhtml+xml",
        }
        try:
            resp = requests.get(
                self.gist_url, headers=headers, timeout=self.timeout
            )
            resp.raise_for_status()
        except requests.Timeout:
            raise RuntimeError(
                f"Gist page fetch timed out after {self.timeout}s ({self.gist_url})"
            )
        except requests.RequestException as exc:
            raise RuntimeError(f"Gist fetch failed: {exc}") from exc

        html = resp.text
        for pattern in self._VIEW_PATTERNS:
            match = pattern.search(html)
            if match:
                raw = match.group(1).replace(",", "")
                return int(raw)

        raise RuntimeError(
            f"Could not parse view count from Gist page. "
            f"URL: {self.gist_url}. "
            f"The page structure may have changed — update _VIEW_PATTERNS."
        )

    def compare_to_baseline(self, current_views: int) -> dict:
        """
        Compare current view count to baseline and expected growth.

        Expected growth curve (from Item 59 / CONTINGENCY_TRIGGER_DECISION_TREE.md):
            Day 3:  > 70 views (GO), 30-70 (CAUTION), < 30 (NO-GO)
            Day 7:  > 200 views (GO), 100-200 (CAUTION), < 50 (NO-GO)
            Day 14: > 400 views (GO), 150-400 (CAUTION), < 150 (NO-GO)

        Args:
            current_views: Views fetched from the Gist page.

        Returns:
            dict with keys: current_views, baseline_views, delta, growth_ratio
        """
        delta = current_views - self.baseline_views
        ratio = current_views / max(self.baseline_views, 1)
        return {
            "current_views": current_views,
            "baseline_views": self.baseline_views,
            "delta_since_baseline": delta,
            "growth_ratio_vs_baseline": round(ratio, 2),
        }

    def get_status(self, current_views: int, checkpoint_day: int) -> str:
        """
        Classify GO/CAUTION/NO-GO based on checkpoint-day thresholds.

        Args:
            current_views: Cumulative view count.
            checkpoint_day: 3, 7, or 14.

        Returns:
            'GO', 'CAUTION', or 'NO-GO'
        """
        day_thresholds = THRESHOLDS.get(checkpoint_day, {}).get("gist_views", {})
        if current_views >= day_thresholds.get("go", 9999):
            return "GO"
        if current_views >= day_thresholds.get("caution_lo", 0):
            return "CAUTION"
        return "NO-GO"


# ---------------------------------------------------------------------------
# Module 3: Etsy Sales Extractor
# ---------------------------------------------------------------------------

class EtsySalesExtractor:
    """
    Queries Etsy API v3 for orders, segments by coupon code, and computes
    per-template revenue attribution.

    Etsy API v3 reference:
        GET /v3/application/shops/{shop_id}/receipts
        Parameters: min_created, max_created, was_paid=true
    """

    BASE_URL = "https://openapi.etsy.com/v3/application"

    def __init__(self, api_key: str, shop_id: str, timeout: int = API_TIMEOUT):
        """
        Args:
            api_key: Etsy API key (from ETSY_API_KEY env var).
            shop_id: Etsy shop numeric ID (from ETSY_SHOP_ID env var).
            timeout: Request timeout in seconds.
        """
        if not api_key:
            raise ValueError("ETSY_API_KEY is not set")
        if not shop_id:
            raise ValueError("ETSY_SHOP_ID is not set")
        self.api_key = api_key
        self.shop_id = str(shop_id)
        self.timeout = timeout

    def _get(self, path: str, params: Optional[dict] = None) -> dict:
        """GET helper against the Etsy v3 API."""
        if not HAS_REQUESTS:
            raise RuntimeError(REQUESTS_MISSING_MSG)
        url = f"{self.BASE_URL}{path}"
        headers = {"x-api-key": self.api_key, "Accept": "application/json"}
        try:
            resp = requests.get(
                url, headers=headers, params=params or {}, timeout=self.timeout
            )
            resp.raise_for_status()
            return resp.json()
        except requests.Timeout:
            raise RuntimeError(
                f"Etsy API timed out after {self.timeout}s (URL: {url})"
            )
        except requests.HTTPError as exc:
            raise RuntimeError(
                f"Etsy API HTTP error {exc.response.status_code}: "
                f"{exc.response.text[:200]}"
            ) from exc
        except requests.RequestException as exc:
            raise RuntimeError(f"Etsy request failed: {exc}") from exc

    def fetch_orders_by_date_range(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> list[dict]:
        """
        Fetch all paid orders within the given date range via paginated API calls.

        Args:
            start_date: Inclusive start date.
            end_date: Inclusive end date.

        Returns:
            List of Etsy receipt dicts (each represents one order).
        """
        min_ts = int(
            datetime.datetime.combine(start_date, datetime.time.min).timestamp()
        )
        max_ts = int(
            datetime.datetime.combine(end_date, datetime.time.max).timestamp()
        )
        orders = []
        limit = 100
        offset = 0
        while True:
            params = {
                "was_paid": "true",
                "min_created": min_ts,
                "max_created": max_ts,
                "limit": limit,
                "offset": offset,
            }
            data = self._get(
                f"/shops/{self.shop_id}/receipts", params=params
            )
            batch = data.get("results", [])
            orders.extend(batch)
            if len(batch) < limit:
                break
            offset += limit
        return orders

    def segment_by_coupon(self, orders: list[dict]) -> dict[str, list[dict]]:
        """
        Group orders by the coupon code used.

        Etsy receipt objects carry a "coupon" field with a "coupon_code" key.
        Orders without a coupon are grouped under the key 'NO_COUPON'.

        Args:
            orders: List of raw Etsy receipt dicts.

        Returns:
            dict mapping coupon_code -> list of order dicts.
        """
        segments: dict[str, list[dict]] = {}
        for order in orders:
            coupon_info = order.get("coupon") or {}
            code = (coupon_info.get("coupon_code") or "NO_COUPON").upper()
            segments.setdefault(code, []).append(order)
        return segments

    def compute_revenue_attribution(
        self, orders: list[dict]
    ) -> dict[str, dict]:
        """
        Compute revenue totals per email template coupon code.

        Args:
            orders: All orders in the monitoring window.

        Returns:
            dict with template keys EMAIL1–EMAIL5 + NO_COUPON, each mapping to:
                {order_count, total_revenue_usd}
        """
        segments = self.segment_by_coupon(orders)
        attribution: dict[str, dict] = {}
        all_codes = set(ETSY_COUPON_CODES.values()) | {"NO_COUPON"}
        for code in all_codes:
            code_orders = segments.get(code, [])
            total_revenue = sum(
                float(o.get("grandtotal", {}).get("amount", 0))
                / max(float(o.get("grandtotal", {}).get("divisor", 1)), 1)
                for o in code_orders
            )
            attribution[code] = {
                "order_count": len(code_orders),
                "total_revenue_usd": round(total_revenue, 2),
            }
        return attribution


# ---------------------------------------------------------------------------
# Module 4: Kit Creator Funnel Fetcher
# ---------------------------------------------------------------------------

class KitFunnelFetcher:
    """
    Fetches subscriber funnel metrics from Kit Creator (ConvertKit) API.

    Kit API v4 reference:
        GET /v4/subscribers           — list subscribers
        GET /v4/forms/{form_id}/subscribers — subscribers via a specific form
        GET /v4/broadcasts/{broadcast_id} — broadcast stats

    Auth: Bearer token (KIT_API_KEY).

    Funnel stages tracked:
        1. Landing page registrations  (Kit form subscribers)
        2. Email 1 open / PDF click    (Kit broadcast or sequence step stats)
        3. Email subscription total    (cumulative subscriber count)
    """

    BASE_URL = "https://api.kit.com/v4"

    def __init__(
        self,
        api_key: str,
        form_id: str,
        timeout: int = API_TIMEOUT,
    ):
        """
        Args:
            api_key: Kit API secret key (from KIT_API_KEY env var).
            form_id: Kit form/landing page ID (from KIT_FORM_ID env var).
            timeout: Request timeout in seconds.
        """
        if not api_key:
            raise ValueError("KIT_API_KEY is not set")
        if not form_id:
            raise ValueError("KIT_FORM_ID is not set")
        self.api_key = api_key
        self.form_id = str(form_id)
        self.timeout = timeout

    def _get(self, path: str, params: Optional[dict] = None) -> dict:
        """GET helper for Kit API."""
        if not HAS_REQUESTS:
            raise RuntimeError(REQUESTS_MISSING_MSG)
        url = f"{self.BASE_URL}{path}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }
        try:
            resp = requests.get(
                url, headers=headers, params=params or {}, timeout=self.timeout
            )
            resp.raise_for_status()
            return resp.json()
        except requests.Timeout:
            raise RuntimeError(
                f"Kit API timed out after {self.timeout}s (URL: {url})"
            )
        except requests.HTTPError as exc:
            raise RuntimeError(
                f"Kit API HTTP error {exc.response.status_code}: "
                f"{exc.response.text[:200]}"
            ) from exc
        except requests.RequestException as exc:
            raise RuntimeError(f"Kit request failed: {exc}") from exc

    def fetch_subscriber_count_since(self, since_date: datetime.date) -> int:
        """
        Count subscribers who joined on or after since_date.

        Paginates through /v4/subscribers with created_after filter.

        Args:
            since_date: Start date (inclusive).

        Returns:
            Integer subscriber count.
        """
        since_dt = datetime.datetime.combine(
            since_date, datetime.time.min
        ).isoformat() + "Z"
        params: dict = {"created_after": since_dt, "per_page": 500}
        total = 0
        cursor = None
        while True:
            if cursor:
                params["after"] = cursor
            data = self._get("/subscribers", params)
            subscribers = data.get("subscribers", [])
            total += len(subscribers)
            pagination = data.get("pagination", {})
            if not pagination.get("has_next_page"):
                break
            cursor = pagination.get("end_cursor")
        return total

    def fetch_form_subscriber_count(self) -> int:
        """
        Fetch total subscriber count via the landing page form.

        Returns:
            Integer subscriber count on this form.
        """
        data = self._get(f"/forms/{self.form_id}/subscribers")
        return data.get("total_subscribers", len(data.get("subscribers", [])))

    def fetch_funnel_metrics(self, launch_date: datetime.date) -> dict:
        """
        Fetch the full registration-to-subscription funnel.

        Funnel stages:
            1. new_subscribers      — count since launch_date
            2. form_total           — all-time form subscriber count
            3. estimated_pdf_opens  — not directly available; proxied via
                                      Kit open rate on Email 1 sequence step
                                      if broadcast stats are exposed.

        Note: Kit's public API exposes subscriber counts and form stats
        but does not return per-email open rates in v4 (those are visible
        in the dashboard). This method returns what the API provides; open
        rate is left as None with a note for manual entry.

        Returns:
            dict with keys:
                new_subscribers_since_launch, form_total_subscribers,
                email1_open_rate_pct (None if not available via API),
                data_note (string)
        """
        try:
            new_subs = self.fetch_subscriber_count_since(launch_date)
        except RuntimeError as exc:
            new_subs = None
            print(f"  [Kit] WARNING: could not fetch new subscriber count: {exc}",
                  file=sys.stderr)

        try:
            form_total = self.fetch_form_subscriber_count()
        except RuntimeError as exc:
            form_total = None
            print(f"  [Kit] WARNING: could not fetch form subscriber count: {exc}",
                  file=sys.stderr)

        return {
            "new_subscribers_since_launch": new_subs,
            "form_total_subscribers": form_total,
            "email1_open_rate_pct": None,
            "data_note": (
                "Kit v4 API provides subscriber counts; open/click rates for "
                "automation steps must be read from Kit dashboard manually and "
                "passed via --email-open-rate flag."
            ),
        }


# ---------------------------------------------------------------------------
# Module 5: Contingency Decision Engine
# ---------------------------------------------------------------------------
# Python translation of CONTINGENCY_TRIGGER_DECISION_TREE.md
# 8 Named Scenarios, each producing GO / CAUTION / NO-GO
# ---------------------------------------------------------------------------

class ContingencyDecisionEngine:
    """
    Applies the 8-scenario contingency decision tree from
    CONTINGENCY_TRIGGER_DECISION_TREE.md to aggregated checkpoint metrics.

    Each scenario is evaluated independently. If two or more scenarios are
    simultaneously in NO-GO, Scenario 8 (Multi-Failure Escalation) fires.
    """

    # Scenario definitions (numeric thresholds only — runbook text is in
    # CONTINGENCY_TRIGGER_DECISION_TREE.md)
    SCENARIOS = {
        "S1_email_open_rate": {
            "name": "Scenario 1: Low Email Open Rate",
            "metric": "email_open_rate_pct",
            "go_threshold": 20.0,
            "caution_range": (10.0, 19.9),
            "nogo_threshold": 10.0,
            "description": (
                "Campaign Monitor open rate on launch broadcast. "
                "GO: >=20%. CAUTION: 10-19%. NO-GO: <10%."
            ),
        },
        "S2_gist_views": {
            "name": "Scenario 2: Low Gist View Count",
            "metric": "gist_views",
            "thresholds_by_day": {
                3:  {"go": 70,  "caution_lo": 30,  "nogo_hi": 30},
                7:  {"go": 200, "caution_lo": 100, "nogo_hi": 50},
                14: {"go": 400, "caution_lo": 150, "nogo_hi": 150},
            },
            "description": (
                "Cumulative Gist view count. Thresholds differ per checkpoint day."
            ),
        },
        "S3_sales": {
            "name": "Scenario 3: Zero Sales",
            "metric": "etsy_orders",
            "description": (
                "Day 3: note but do not escalate. "
                "Day 7 NO-GO: 0 sales AND Etsy listing Active 3+ days. "
                "Day 14 NO-GO: 0 sales AND listing Active 5+ days."
            ),
        },
        "S4_influencer_silence": {
            "name": "Scenario 4: Influencer Silence",
            "metric": "influencer_responses",
            "caution_day3": 0,
            "nogo_day7": 0,
            "description": (
                "Day 3 CAUTION: 0 responses (normal — 3-7d response time). "
                "Day 7 NO-GO: 0 responses from all 15 contacts."
            ),
        },
        "S5_unsubscribe_rate": {
            "name": "Scenario 5: High Unsubscribe Rate",
            "metric": "email_unsub_rate_pct",
            "caution_threshold": 2.0,
            "nogo_threshold": 5.0,
            "description": (
                "CAUTION: 2-5% of recipients unsub. "
                "NO-GO: >5% on any single broadcast or cumulative."
            ),
        },
        "S6_social_zero_traction": {
            "name": "Scenario 6: Social Media Zero Traction",
            "metric": "instagram_reach",
            "nogo_day7": 200,
            "description": (
                "Day 7 NO-GO: <200 Instagram reach AND 0 Twitter mentions "
                "AND Reddit posts removed or 0 upvotes."
            ),
        },
        "S7_revenue_channel_mismatch": {
            "name": "Scenario 7: Sales / Revenue Channel Mismatch",
            "metric": None,  # qualitative — detected from attribution data
            "description": (
                "Revenue present but concentrated in one unexpected channel. "
                "Detected from Etsy coupon attribution vs email/social signal divergence."
            ),
        },
        "S8_multi_failure": {
            "name": "Scenario 8: Multi-Failure Escalation Protocol",
            "description": (
                "Fires automatically when 2+ scenarios are simultaneously in NO-GO. "
                "Root cause A: launch did not execute. "
                "Root cause B: distribution infrastructure broken. "
                "Root cause C: audience mismatch."
            ),
        },
    }

    def evaluate(self, metrics: dict, checkpoint_day: int) -> dict:
        """
        Evaluate all 8 scenarios and return a structured decision.

        Args:
            metrics: dict with keys matching scenario metric names.
                Required keys: email_open_rate_pct, gist_views, etsy_orders,
                influencer_responses, email_unsub_rate_pct,
                instagram_reach (optional).
            checkpoint_day: 3, 7, or 14.

        Returns:
            dict with keys:
                overall_status: 'GO', 'CAUTION', 'NO-GO'
                scenario_results: list of per-scenario dicts
                    {scenario_key, name, status, metric_value, rationale}
                active_nogo_scenarios: list of scenario keys in NO-GO
                multi_failure_triggered: bool
                recommended_action: human-readable string
        """
        results = []
        nogo_scenarios = []

        # S1: Email open rate
        open_rate = metrics.get("email_open_rate_pct")
        s1 = self._evaluate_s1_email_open_rate(open_rate)
        results.append(s1)
        if s1["status"] == "NO-GO":
            nogo_scenarios.append("S1")

        # S2: Gist views
        gist_views = metrics.get("gist_views")
        s2 = self._evaluate_s2_gist_views(gist_views, checkpoint_day)
        results.append(s2)
        if s2["status"] == "NO-GO":
            nogo_scenarios.append("S2")

        # S3: Sales
        orders = metrics.get("etsy_orders")
        etsy_listing_active = metrics.get("etsy_listing_active", True)
        s3 = self._evaluate_s3_sales(orders, checkpoint_day, etsy_listing_active)
        results.append(s3)
        if s3["status"] == "NO-GO":
            nogo_scenarios.append("S3")

        # S4: Influencer silence
        influencer_responses = metrics.get("influencer_responses")
        s4 = self._evaluate_s4_influencer(influencer_responses, checkpoint_day)
        results.append(s4)
        if s4["status"] == "NO-GO":
            nogo_scenarios.append("S4")

        # S5: Unsubscribe rate
        unsub_rate = metrics.get("email_unsub_rate_pct")
        s5 = self._evaluate_s5_unsub_rate(unsub_rate)
        results.append(s5)
        if s5["status"] == "NO-GO":
            nogo_scenarios.append("S5")

        # S6: Social zero traction (Day 7+ only)
        instagram_reach = metrics.get("instagram_reach")
        twitter_mentions = metrics.get("twitter_mentions", None)
        reddit_upvotes = metrics.get("reddit_upvotes", None)
        s6 = self._evaluate_s6_social(
            instagram_reach, twitter_mentions, reddit_upvotes, checkpoint_day
        )
        results.append(s6)
        if s6["status"] == "NO-GO":
            nogo_scenarios.append("S6")

        # S7: Revenue channel mismatch (qualitative — auto-flag if Etsy 0 but email GO)
        s7 = self._evaluate_s7_channel_mismatch(metrics, checkpoint_day)
        results.append(s7)
        if s7["status"] == "NO-GO":
            nogo_scenarios.append("S7")

        # S8: Multi-failure
        multi_failure = len(nogo_scenarios) >= 2
        s8_status = "NO-GO" if multi_failure else "GO"
        s8 = {
            "scenario_key": "S8",
            "name": self.SCENARIOS["S8_multi_failure"]["name"],
            "status": s8_status,
            "metric_value": len(nogo_scenarios),
            "rationale": (
                f"{len(nogo_scenarios)} scenarios in NO-GO state: {', '.join(nogo_scenarios)}. "
                "Execute root-cause triage before individual scenario runbooks."
                if multi_failure
                else "Fewer than 2 NO-GO scenarios — multi-failure not triggered."
            ),
        }
        results.append(s8)

        # Overall status
        if multi_failure or len(nogo_scenarios) >= 1:
            overall = "NO-GO"
        elif any(r["status"] == "CAUTION" for r in results):
            overall = "CAUTION"
        else:
            overall = "GO"

        recommended_action = self._build_recommended_action(
            overall, nogo_scenarios, multi_failure, checkpoint_day
        )

        return {
            "overall_status": overall,
            "scenario_results": results,
            "active_nogo_scenarios": nogo_scenarios,
            "multi_failure_triggered": multi_failure,
            "recommended_action": recommended_action,
        }

    # --- Internal scenario evaluators ---

    def _evaluate_s1_email_open_rate(self, open_rate: Optional[float]) -> dict:
        if open_rate is None:
            return self._scenario_result(
                "S1", "S1_email_open_rate", "CAUTION", open_rate,
                "Email open rate not available — verify Campaign Monitor API credentials."
            )
        if open_rate >= 20.0:
            status = "GO"
            rationale = f"Open rate {open_rate:.1f}% meets GO threshold (>=20%)."
        elif open_rate >= 10.0:
            status = "CAUTION"
            rationale = (
                f"Open rate {open_rate:.1f}% is in CAUTION range (10-19%). "
                "Send re-engagement broadcast to non-openers with revised subject."
            )
        else:
            status = "NO-GO"
            rationale = (
                f"Open rate {open_rate:.1f}% is below NO-GO threshold (<10%). "
                "Check spam folder, SPF/DKIM records. "
                "Fallback: send to Tier 1 contacts via Gmail manually."
            )
        return self._scenario_result(
            "S1", "S1_email_open_rate", status, open_rate, rationale
        )

    def _evaluate_s2_gist_views(
        self, views: Optional[int], checkpoint_day: int
    ) -> dict:
        day_t = self.SCENARIOS["S2_gist_views"]["thresholds_by_day"].get(
            checkpoint_day, {}
        )
        if views is None:
            return self._scenario_result(
                "S2", "S2_gist_views", "CAUTION", views,
                "Gist view count not available — check GIST_URL and page accessibility."
            )
        go = day_t.get("go", 70)
        caution_lo = day_t.get("caution_lo", 30)
        nogo_hi = day_t.get("nogo_hi", 30)
        if views >= go:
            status, rationale = "GO", f"Gist views {views} >= GO threshold ({go})."
        elif views >= caution_lo:
            status = "CAUTION"
            rationale = (
                f"Gist views {views} in CAUTION range ({caution_lo}–{go-1}). "
                "Cross-post to one new community (r/homesteading or r/foraging)."
            )
        else:
            status = "NO-GO"
            rationale = (
                f"Gist views {views} below NO-GO threshold ({nogo_hi}). "
                "Audit URL placement in all social bios; check Reddit post removal. "
                "Consider free Etsy listing or Pinterest as alternate distribution."
            )
        return self._scenario_result(
            "S2", "S2_gist_views", status, views, rationale
        )

    def _evaluate_s3_sales(
        self,
        orders: Optional[int],
        checkpoint_day: int,
        listing_active: bool,
    ) -> dict:
        if orders is None:
            return self._scenario_result(
                "S3", "S3_sales", "CAUTION", orders,
                "Etsy order count not available — check ETSY_API_KEY and ETSY_SHOP_ID."
            )
        if checkpoint_day == 3:
            if orders >= 1:
                status = "GO"
                rationale = f"{orders} order(s) at Day 3 — strong early signal."
            else:
                status = "CAUTION"
                rationale = (
                    "0 sales at Day 3 — expected if paid listing not yet active. "
                    "Verify Etsy listing status."
                )
        elif checkpoint_day == 7:
            if orders >= 1:
                status = "GO"
                rationale = f"{orders} order(s) at Day 7."
            elif not listing_active:
                status = "NO-GO"
                rationale = (
                    "0 sales AND Etsy listing is not Active. "
                    "Publish listing immediately. A free Gist does not generate Etsy sales."
                )
            else:
                status = "CAUTION"
                rationale = (
                    "0 sales despite Active listing. Check impressions vs views ratio. "
                    "Possible SEO or thumbnail issue. "
                    "Ensure title includes: 'wild edibles guide', 'zone quick-start', "
                    "'USDA hardiness zone', 'native plants identification'."
                )
        else:  # Day 14
            if orders >= 3:
                status = "GO"
                rationale = f"{orders} order(s) at Day 14."
            elif orders >= 1:
                status = "CAUTION"
                rationale = (
                    f"{orders} order(s) at Day 14 — below GO threshold (3). "
                    "Add 'try before you buy' Gist CTA to listing. "
                    "Run 10% off Etsy sale."
                )
            else:
                status = "NO-GO"
                rationale = (
                    "0 sales at Day 14 with Active listing. "
                    "Lower price by $2 as test. "
                    "If still 0: pivot to Kit-gated PDF as primary monetization."
                )
        return self._scenario_result(
            "S3", "S3_sales", status, orders, rationale
        )

    def _evaluate_s4_influencer(
        self, responses: Optional[int], checkpoint_day: int
    ) -> dict:
        if responses is None:
            return self._scenario_result(
                "S4", "S4_influencer_silence", "CAUTION", responses,
                "Influencer response count not provided — enter manually via --influencer-responses."
            )
        if checkpoint_day == 3:
            if responses >= 1:
                status = "GO"
                rationale = f"{responses} influencer response(s) at Day 3."
            else:
                status = "CAUTION"
                rationale = (
                    "0 influencer responses at Day 3. "
                    "Normal — response window is 3-7 days. No action yet."
                )
        else:  # Day 7 or 14
            if checkpoint_day == 7 and responses == 0:
                status = "NO-GO"
                rationale = (
                    "0 influencer responses at Day 7. "
                    "Send one follow-up to top 5 Tier 1 contacts with actual view count. "
                    "Try Instagram DM if email bounced."
                )
            elif responses >= 3:
                status = "GO"
                rationale = f"{responses} influencer shares confirmed."
            elif responses >= 1:
                status = "CAUTION"
                rationale = (
                    f"{responses} influencer response(s). "
                    "Continue monitoring. Follow up with remaining Tier 1 contacts."
                )
            else:
                status = "NO-GO"
                rationale = (
                    f"0 influencer responses at Day {checkpoint_day}. "
                    "Pivot to direct platform engagement: comment on recent posts, "
                    "share in communities those influencers participate in."
                )
        return self._scenario_result(
            "S4", "S4_influencer_silence", status, responses, rationale
        )

    def _evaluate_s5_unsub_rate(self, unsub_rate: Optional[float]) -> dict:
        if unsub_rate is None:
            return self._scenario_result(
                "S5", "S5_unsubscribe_rate", "GO", unsub_rate,
                "Unsubscribe rate not available — assumed OK."
            )
        if unsub_rate > 5.0:
            status = "NO-GO"
            rationale = (
                f"Unsubscribe rate {unsub_rate:.1f}% exceeds NO-GO threshold (5%). "
                "Immediately pause all broadcast emails. "
                "Audit subscriber source for audience mismatch."
            )
        elif unsub_rate >= 2.0:
            status = "CAUTION"
            rationale = (
                f"Unsubscribe rate {unsub_rate:.1f}% in CAUTION range (2-5%). "
                "Pause additional broadcasts for 48h. "
                "Review and revise next broadcast before sending."
            )
        else:
            status = "GO"
            rationale = f"Unsubscribe rate {unsub_rate:.1f}% is healthy (<2%)."
        return self._scenario_result(
            "S5", "S5_unsubscribe_rate", status, unsub_rate, rationale
        )

    def _evaluate_s6_social(
        self,
        instagram_reach: Optional[int],
        twitter_mentions: Optional[int],
        reddit_upvotes: Optional[int],
        checkpoint_day: int,
    ) -> dict:
        # S6 is only meaningful at Day 7+
        if checkpoint_day == 3:
            return self._scenario_result(
                "S6", "S6_social_zero_traction", "GO", instagram_reach,
                "Social traction evaluated at Day 7+. No Day 3 threshold."
            )
        if instagram_reach is None:
            return self._scenario_result(
                "S6", "S6_social_zero_traction", "CAUTION", instagram_reach,
                "Instagram reach not provided — enter manually."
            )
        # Day 7 NO-GO: <200 reach AND 0 Twitter mentions AND Reddit 0 upvotes
        reach_low = instagram_reach < 200
        twitter_zero = twitter_mentions is not None and twitter_mentions == 0
        reddit_zero = reddit_upvotes is not None and reddit_upvotes == 0
        if reach_low and (twitter_zero or reddit_zero):
            status = "NO-GO"
            rationale = (
                f"Instagram reach {instagram_reach} < 200 AND "
                f"Twitter mentions: {twitter_mentions}, Reddit upvotes: {reddit_upvotes}. "
                "Check account standing. Shift to community participation on Reddit. "
                "If Day 7: test $10-20 Instagram ad targeting gardening/herbalism interests."
            )
        elif instagram_reach < 200:
            status = "CAUTION"
            rationale = (
                f"Instagram reach {instagram_reach} below 200 threshold. "
                "Increase community participation before expanding posts."
            )
        else:
            status = "GO"
            rationale = f"Instagram reach {instagram_reach} meets threshold."
        return self._scenario_result(
            "S6", "S6_social_zero_traction", status, instagram_reach, rationale
        )

    def _evaluate_s7_channel_mismatch(
        self, metrics: dict, checkpoint_day: int
    ) -> dict:
        # Qualitative: flag if email is GO but Etsy shows 0 sales, or vice versa.
        open_rate = metrics.get("email_open_rate_pct")
        orders = metrics.get("etsy_orders")
        if open_rate is None or orders is None or checkpoint_day == 3:
            return self._scenario_result(
                "S7", "S7_revenue_channel_mismatch", "GO", None,
                "Channel mismatch evaluated at Day 7+. Insufficient data at Day 3."
            )
        # Email strong, no Etsy sales
        email_strong = open_rate >= 20.0
        no_sales = orders == 0
        if email_strong and no_sales:
            status = "CAUTION"
            rationale = (
                f"Email open rate {open_rate:.1f}% (GO) but 0 Etsy sales — "
                "channel mismatch. Add above-the-fold CTA at top of Gist linking to Etsy. "
                "Check Etsy listing thumbnail and title SEO."
            )
        else:
            status = "GO"
            rationale = "No significant channel mismatch detected."
        return self._scenario_result(
            "S7", "S7_revenue_channel_mismatch", status, open_rate, rationale
        )

    @staticmethod
    def _scenario_result(
        key: str, scenario_key: str, status: str, value, rationale: str
    ) -> dict:
        scenario_info = ContingencyDecisionEngine.SCENARIOS.get(scenario_key, {})
        return {
            "scenario_key": key,
            "name": scenario_info.get("name", scenario_key),
            "status": status,
            "metric_value": value,
            "rationale": rationale,
        }

    @staticmethod
    def _build_recommended_action(
        overall: str,
        nogo_scenarios: list[str],
        multi_failure: bool,
        checkpoint_day: int,
    ) -> str:
        if overall == "GO":
            return (
                "All thresholds met or exceeded. "
                "Continue executing launch plan. "
                "Consider activating amplification actions "
                "(Track A holdouts, affiliate outreach, paid test)."
            )
        if multi_failure:
            return (
                "Multi-failure: 2+ NO-GO scenarios. "
                "Execute Scenario 8 root-cause triage BEFORE any individual scenario. "
                "Check: (A) was launch fully executed, (B) is distribution infrastructure intact, "
                "(C) audience mismatch. "
                "See CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 8."
            )
        if overall == "NO-GO":
            return (
                f"NO-GO on: {', '.join(nogo_scenarios)}. "
                "Execute matching scenario runbook from CONTINGENCY_TRIGGER_DECISION_TREE.md. "
                "Stabilize before committing to Phase 2 expansion."
            )
        return (
            "CAUTION on some metrics. Continue current plan. "
            "Investigate the specific gap. Do not expand scope until gap is understood."
        )


# ---------------------------------------------------------------------------
# Module 6: Checkpoint Orchestrator — unified entry point
# ---------------------------------------------------------------------------

class CheckpointOrchestrator:
    """
    Orchestrates all 4 metric modules, aggregates results, applies the
    contingency decision engine, and writes a markdown checkpoint report
    to CHECKPOINT_REPORTS/.

    Idempotent: running the same checkpoint twice overwrites the same
    report file with the same content (stable filename per checkpoint day).
    """

    def __init__(self, config: dict):
        """
        Args:
            config: dict with keys:
                checkpoint_day: 3, 7, or 14
                launch_date: datetime.date
                dry_run: bool — if True, skip live API calls and use dummy data
                output_dir: str — path to CHECKPOINT_REPORTS directory
                env: dict — environment variables (API keys, IDs, etc.)
                manual_overrides: dict — manually provided metric values
        """
        self.checkpoint_day = config["checkpoint_day"]
        self.launch_date = config.get("launch_date", LAUNCH_DATE_DEFAULT)
        self.dry_run = config.get("dry_run", False)
        self.output_dir = config.get("output_dir", CHECKPOINT_REPORTS_DIR_DEFAULT)
        self.env = config.get("env", {})
        self.manual_overrides = config.get("manual_overrides", {})
        self.decision_engine = ContingencyDecisionEngine()
        self._errors: list[str] = []

    def _validate_credentials(self) -> list[str]:
        """Check that required env vars are present. Returns list of missing keys."""
        required = {
            "CAMPAIGN_MONITOR_API_KEY": "Campaign Monitor API client",
            "GIST_URL": "Gist view poller",
        }
        optional_warn = {
            "ETSY_API_KEY": "Etsy sales extractor",
            "ETSY_SHOP_ID": "Etsy sales extractor",
            "KIT_API_KEY": "Kit funnel fetcher",
            "KIT_FORM_ID": "Kit funnel fetcher",
        }
        missing = []
        for key, module in required.items():
            if not self.env.get(key):
                missing.append(f"MISSING REQUIRED: {key} ({module})")
        for key, module in optional_warn.items():
            if not self.env.get(key):
                print(
                    f"  [Config] WARNING: {key} not set — {module} will be skipped.",
                    file=sys.stderr,
                )
        return missing

    def run(self) -> dict:
        """
        Execute the full checkpoint run.

        Returns:
            Aggregated metrics + decision dict suitable for JSON serialization
            and markdown report generation.
        """
        print(f"\n=== Track B Day {self.checkpoint_day} Checkpoint ===")
        print(f"Launch date: {self.launch_date}  |  Run mode: {'DRY-RUN' if self.dry_run else 'LIVE'}")

        if not self.dry_run:
            cred_errors = self._validate_credentials()
            if cred_errors:
                for err in cred_errors:
                    print(f"  {err}", file=sys.stderr)
                raise RuntimeError(
                    "Missing required credentials. "
                    "Set environment variables or use --dry-run."
                )

        metrics = {}

        # 1. Campaign Monitor
        metrics.update(self._run_campaign_monitor())

        # 2. Gist view count
        metrics.update(self._run_gist_poller())

        # 3. Etsy sales
        metrics.update(self._run_etsy_extractor())

        # 4. Kit funnel
        metrics.update(self._run_kit_fetcher())

        # Apply manual overrides (highest priority — user-supplied values win)
        for key, val in self.manual_overrides.items():
            if val is not None:
                metrics[key] = val
                print(f"  [Override] {key} = {val}")

        # 5. Decision engine
        print("\n--- Applying contingency decision tree ---")
        decision = self.decision_engine.evaluate(metrics, self.checkpoint_day)

        result = {
            "checkpoint_day": self.checkpoint_day,
            "launch_date": str(self.launch_date),
            "run_timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
            "dry_run": self.dry_run,
            "metrics": metrics,
            "decision": decision,
            "errors": self._errors,
        }

        # 6. Write markdown report
        report_path = self._write_report(result)
        result["report_path"] = str(report_path)

        return result

    def _run_campaign_monitor(self) -> dict:
        print("\n[1/4] Campaign Monitor...")
        if self.dry_run:
            return {
                "email_open_rate_pct": 22.5,
                "email_click_rate_pct": 8.1,
                "email_unsub_rate_pct": 1.2,
                "email_total_sent": 340,
                "email_template_metrics": [
                    {"template": "EMAIL1", "open_rate_pct": 22.5,
                     "click_rate_pct": 8.1, "unsub_rate_pct": 1.2},
                ],
                "email_anomalies": [],
                "email_source": "DRY-RUN",
            }

        api_key = self.env.get("CAMPAIGN_MONITOR_API_KEY", "")
        campaign_id_map = {}
        for slot in EMAIL_TEMPLATE_SLOTS:
            env_key = f"CAMPAIGN_MONITOR_CAMPAIGN_ID_{slot}"
            cid = self.env.get(env_key, "")
            if cid:
                campaign_id_map[slot] = cid

        if not campaign_id_map:
            msg = (
                "No campaign IDs configured. Set "
                "CAMPAIGN_MONITOR_CAMPAIGN_ID_EMAIL1 ... EMAIL5."
            )
            print(f"  [CM] WARNING: {msg}", file=sys.stderr)
            self._errors.append(msg)
            return {"email_source": "SKIPPED — no campaign IDs"}

        try:
            client = CampaignMonitorClient(api_key)
            template_metrics = client.fetch_all_template_metrics(campaign_id_map)
            anomalies = client.detect_anomalies(template_metrics)

            # Aggregate across all templates (use EMAIL1 as primary open rate)
            primary = next(
                (m for m in template_metrics if m["template"] == "EMAIL1"),
                template_metrics[0] if template_metrics else {}
            )
            for anomaly in anomalies:
                print(f"  [CM] ANOMALY: {anomaly}")

            return {
                "email_open_rate_pct": primary.get("open_rate_pct"),
                "email_click_rate_pct": primary.get("click_rate_pct"),
                "email_unsub_rate_pct": primary.get("unsub_rate_pct"),
                "email_total_sent": primary.get("total_sent"),
                "email_template_metrics": template_metrics,
                "email_anomalies": anomalies,
                "email_source": "Campaign Monitor API",
            }
        except RuntimeError as exc:
            msg = f"Campaign Monitor error: {exc}"
            print(f"  [CM] ERROR: {msg}", file=sys.stderr)
            self._errors.append(msg)
            return {"email_source": "ERROR", "email_error": str(exc)}

    def _run_gist_poller(self) -> dict:
        print("\n[2/4] Gist view count...")
        if self.dry_run:
            return {
                "gist_views": 85,
                "gist_baseline": 0,
                "gist_delta": 85,
                "gist_growth_ratio": 85.0,
                "gist_status": "GO",
                "gist_source": "DRY-RUN",
            }

        gist_url = self.env.get("GIST_URL", "")
        baseline = int(self.env.get("GIST_BASELINE_VIEWS", "0"))
        try:
            poller = GistViewPoller(gist_url, baseline_views=baseline)
            current = poller.fetch_view_count()
            comparison = poller.compare_to_baseline(current)
            status = poller.get_status(current, self.checkpoint_day)
            print(f"  [Gist] Current views: {current} | Status: {status}")
            return {
                "gist_views": current,
                "gist_baseline": baseline,
                "gist_delta": comparison["delta_since_baseline"],
                "gist_growth_ratio": comparison["growth_ratio_vs_baseline"],
                "gist_status": status,
                "gist_source": gist_url,
            }
        except RuntimeError as exc:
            msg = f"Gist poller error: {exc}"
            print(f"  [Gist] ERROR: {msg}", file=sys.stderr)
            self._errors.append(msg)
            return {"gist_source": "ERROR", "gist_error": str(exc)}

    def _run_etsy_extractor(self) -> dict:
        print("\n[3/4] Etsy sales...")
        if self.dry_run:
            return {
                "etsy_orders": 2,
                "etsy_total_revenue_usd": 14.98,
                "etsy_listing_active": True,
                "etsy_attribution": {
                    "EMAIL1": {"order_count": 1, "total_revenue_usd": 7.49},
                    "EMAIL2": {"order_count": 1, "total_revenue_usd": 7.49},
                    "NO_COUPON": {"order_count": 0, "total_revenue_usd": 0.0},
                },
                "etsy_source": "DRY-RUN",
            }

        api_key = self.env.get("ETSY_API_KEY", "")
        shop_id = self.env.get("ETSY_SHOP_ID", "")
        if not api_key or not shop_id:
            msg = "ETSY_API_KEY or ETSY_SHOP_ID not set — Etsy module skipped."
            print(f"  [Etsy] WARNING: {msg}", file=sys.stderr)
            return {"etsy_source": "SKIPPED — credentials not set"}

        try:
            extractor = EtsySalesExtractor(api_key, shop_id)
            end_date = datetime.date.today()
            orders = extractor.fetch_orders_by_date_range(self.launch_date, end_date)
            attribution = extractor.compute_revenue_attribution(orders)
            total_revenue = sum(
                v["total_revenue_usd"] for v in attribution.values()
            )
            print(
                f"  [Etsy] Orders: {len(orders)} | Revenue: ${total_revenue:.2f}"
            )
            return {
                "etsy_orders": len(orders),
                "etsy_total_revenue_usd": round(total_revenue, 2),
                "etsy_listing_active": True,  # assumed; use manual override if not
                "etsy_attribution": attribution,
                "etsy_source": f"Etsy API shop {shop_id}",
            }
        except RuntimeError as exc:
            msg = f"Etsy extractor error: {exc}"
            print(f"  [Etsy] ERROR: {msg}", file=sys.stderr)
            self._errors.append(msg)
            return {"etsy_source": "ERROR", "etsy_error": str(exc)}

    def _run_kit_fetcher(self) -> dict:
        print("\n[4/4] Kit Creator funnel...")
        if self.dry_run:
            return {
                "kit_new_subscribers": 12,
                "kit_form_total": 12,
                "kit_email1_open_rate_pct": None,
                "kit_source": "DRY-RUN",
                "kit_note": (
                    "Kit v4 API provides subscriber counts; "
                    "open/click rates must be read from Kit dashboard."
                ),
            }

        api_key = self.env.get("KIT_API_KEY", "")
        form_id = self.env.get("KIT_FORM_ID", "")
        if not api_key or not form_id:
            msg = "KIT_API_KEY or KIT_FORM_ID not set — Kit module skipped."
            print(f"  [Kit] WARNING: {msg}", file=sys.stderr)
            return {"kit_source": "SKIPPED — credentials not set"}

        try:
            fetcher = KitFunnelFetcher(api_key, form_id)
            funnel = fetcher.fetch_funnel_metrics(self.launch_date)
            print(
                f"  [Kit] New subscribers since launch: "
                f"{funnel.get('new_subscribers_since_launch')}"
            )
            return {
                "kit_new_subscribers": funnel.get("new_subscribers_since_launch"),
                "kit_form_total": funnel.get("form_total_subscribers"),
                "kit_email1_open_rate_pct": funnel.get("email1_open_rate_pct"),
                "kit_source": "Kit API v4",
                "kit_note": funnel.get("data_note"),
            }
        except RuntimeError as exc:
            msg = f"Kit fetcher error: {exc}"
            print(f"  [Kit] ERROR: {msg}", file=sys.stderr)
            self._errors.append(msg)
            return {"kit_source": "ERROR", "kit_error": str(exc)}

    def _write_report(self, result: dict) -> str:
        """Write markdown checkpoint report. Idempotent (same filename per day)."""
        os.makedirs(self.output_dir, exist_ok=True)
        filename = (
            f"checkpoint-day{self.checkpoint_day}-"
            f"{datetime.date.today().isoformat()}.md"
        )
        filepath = os.path.join(self.output_dir, filename)

        metrics = result["metrics"]
        decision = result["decision"]
        ts = result["run_timestamp_utc"]
        dry_note = "  \n**DRY-RUN MODE — live API calls were skipped.**\n" if result["dry_run"] else ""

        template_table = ""
        tmpl_list = metrics.get("email_template_metrics", [])
        if tmpl_list:
            template_table = (
                "\n| Template | Open Rate | Click Rate | Unsub Rate | Sent |\n"
                "|----------|-----------|------------|------------|------|\n"
            )
            for t in tmpl_list:
                template_table += (
                    f"| {t.get('template','-')} "
                    f"| {t.get('open_rate_pct','-')}% "
                    f"| {t.get('click_rate_pct','-')}% "
                    f"| {t.get('unsub_rate_pct','-')}% "
                    f"| {t.get('total_sent','-')} |\n"
                )

        etsy_attribution = metrics.get("etsy_attribution", {})
        attribution_rows = ""
        for code, data in etsy_attribution.items():
            attribution_rows += (
                f"| {code} | {data.get('order_count',0)} | "
                f"${data.get('total_revenue_usd',0.0):.2f} |\n"
            )

        scenario_rows = ""
        for s in decision.get("scenario_results", []):
            status_badge = {
                "GO": "GO",
                "CAUTION": "CAUTION",
                "NO-GO": "NO-GO",
            }.get(s["status"], s["status"])
            scenario_rows += (
                f"| {s['scenario_key']} | {s['name']} | **{status_badge}** | "
                f"{s['metric_value']} | "
                f"{s['rationale'][:80]}{'...' if len(s['rationale']) > 80 else ''} |\n"
            )

        errors_section = ""
        if result["errors"]:
            errors_section = (
                "\n## Errors / Warnings\n\n"
                + "\n".join(f"- {e}" for e in result["errors"])
                + "\n"
            )

        anomalies_section = ""
        anomalies = metrics.get("email_anomalies", [])
        if anomalies:
            anomalies_section = (
                "\n## Email Anomalies\n\n"
                + "\n".join(f"- {a}" for a in anomalies)
                + "\n"
            )

        overall = decision["overall_status"]
        badge = {"GO": "GO", "CAUTION": "CAUTION", "NO-GO": "NO-GO"}.get(overall, overall)

        lines = []
        lines.append(f"# Track B Day {self.checkpoint_day} Checkpoint Report")
        lines.append("")
        if result["dry_run"]:
            lines.append("**DRY-RUN MODE — live API calls were skipped.**")
            lines.append("")
        lines.append(f"**Generated**: {ts}")
        lines.append(f"**Launch date**: {result['launch_date']}")
        lines.append(f"**Checkpoint day**: Day {self.checkpoint_day}")
        lines.append("**Report written by**: TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py (Item 85)")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append(f"## Overall Status: {badge}")
        lines.append("")
        lines.append(f"**Decision**: {decision.get('overall_status')}")
        lines.append("")
        lines.append("**Recommended action**:")
        lines.append(decision.get("recommended_action", "See scenario results below."))
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## Metric Summary")
        lines.append("")
        lines.append("| Metric | Value | Source |")
        lines.append("|--------|-------|--------|")
        lines.append(f"| Email open rate | {metrics.get('email_open_rate_pct', 'N/A')}% | {metrics.get('email_source', 'N/A')} |")
        lines.append(f"| Email unsub rate | {metrics.get('email_unsub_rate_pct', 'N/A')}% | Campaign Monitor |")
        lines.append(f"| Email click rate | {metrics.get('email_click_rate_pct', 'N/A')}% | Campaign Monitor |")
        lines.append(f"| Gist views (cumulative) | {metrics.get('gist_views', 'N/A')} | {metrics.get('gist_source', 'N/A')} |")
        lines.append(f"| Gist growth ratio vs baseline | {metrics.get('gist_growth_ratio', 'N/A')} | computed |")
        lines.append(f"| Etsy orders | {metrics.get('etsy_orders', 'N/A')} | {metrics.get('etsy_source', 'N/A')} |")
        lines.append(f"| Etsy total revenue | ${metrics.get('etsy_total_revenue_usd', 'N/A')} | Etsy API |")
        lines.append(f"| Kit new subscribers | {metrics.get('kit_new_subscribers', 'N/A')} | {metrics.get('kit_source', 'N/A')} |")
        lines.append(f"| Influencer responses | {metrics.get('influencer_responses', 'N/A')} | manual |")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## Email Template Performance")
        lines.append("")
        if template_table:
            lines.append(template_table.strip())
        else:
            lines.append("_No template metrics available._")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## Etsy Revenue Attribution by Coupon Code")
        lines.append("")
        lines.append("| Coupon Code | Orders | Revenue |")
        lines.append("|-------------|--------|---------|")
        if attribution_rows:
            lines.append(attribution_rows.strip())
        else:
            lines.append("_No Etsy attribution data._")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## Contingency Decision Tree — Scenario Results")
        lines.append("")
        lines.append("| # | Scenario | Status | Value | Rationale |")
        lines.append("|---|----------|--------|-------|-----------|")
        if scenario_rows:
            lines.append(scenario_rows.strip())
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## Multi-Failure Status")
        lines.append("")
        if decision.get("multi_failure_triggered"):
            lines.append("**MULTI-FAILURE TRIGGERED** — Execute Scenario 8 triage first.")
        else:
            lines.append("Multi-failure not triggered.")
        lines.append("")
        nogo_list = ", ".join(decision.get("active_nogo_scenarios", [])) or "None"
        lines.append(f"Active NO-GO scenarios: {nogo_list}")
        lines.append("")
        lines.append("---")
        if anomalies_section:
            lines.append(anomalies_section.strip())
            lines.append("")
        if errors_section:
            lines.append(errors_section.strip())
            lines.append("")
        lines.append("## Next Checkpoint")
        lines.append("")
        lines.append("| Day | Date | UTC Time |")
        lines.append("|-----|------|----------|")
        lines.append("| Day 3  | 2026-06-07 | 09:00 UTC |")
        lines.append("| Day 7  | 2026-06-11 | 10:00 UTC |")
        lines.append("| Day 14 | 2026-06-18 | 11:00 UTC |")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("_References: CONTINGENCY_TRIGGER_DECISION_TREE.md, TRACK_B_MONITORING_AUTOMATION_FRAMEWORK.md_")
        lines.append("")
        markdown = "\n".join(lines)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"\n  [Report] Written to: {filepath}")
        return filepath


# ---------------------------------------------------------------------------
# Unit Tests (3-5 cases per module, nominal + error path)
# ---------------------------------------------------------------------------

class TestCampaignMonitorClient(unittest.TestCase):
    """Tests for CampaignMonitorClient metric computation."""

    def test_compute_template_metrics_nominal(self):
        client = CampaignMonitorClient.__new__(CampaignMonitorClient)
        client.api_key = "fake"
        client.timeout = 30
        client._auth = ("fake", "x")
        raw = {
            "TotalRecipients": 200,
            "UniqueOpened": 50,
            "Clicks": 10,
            "Unsubscribed": 2,
            "Bounced": 1,
        }
        # Monkey-patch fetch
        client.fetch_campaign_summary = lambda _: raw
        metrics = client.compute_template_metrics("camp123", "EMAIL1")
        self.assertAlmostEqual(metrics["open_rate_pct"], 25.0)
        self.assertAlmostEqual(metrics["unsub_rate_pct"], 1.0)

    def test_compute_template_metrics_zero_sent(self):
        """Guard against division by zero when TotalRecipients is 0."""
        client = CampaignMonitorClient.__new__(CampaignMonitorClient)
        client.api_key = "fake"
        client.timeout = 30
        client._auth = ("fake", "x")
        raw = {
            "TotalRecipients": 0,
            "UniqueOpened": 0,
            "Clicks": 0,
            "Unsubscribed": 0,
            "Bounced": 0,
        }
        client.fetch_campaign_summary = lambda _: raw
        metrics = client.compute_template_metrics("camp123", "EMAIL1")
        self.assertEqual(metrics["open_rate_pct"], 0.0)

    def test_detect_anomalies_open_rate_drop(self):
        client = CampaignMonitorClient.__new__(CampaignMonitorClient)
        client.api_key = "fake"
        client.timeout = 30
        client._auth = ("fake", "x")
        template_metrics = [
            {"template": "EMAIL1", "open_rate_pct": 40.0, "unsub_rate_pct": 1.0},
            {"template": "EMAIL2", "open_rate_pct": 20.0, "unsub_rate_pct": 1.0},
        ]
        # 50% drop should trigger low-engagement warning
        anomalies = client.detect_anomalies(template_metrics)
        self.assertTrue(
            any("LOW-ENGAGEMENT WARNING" in a for a in anomalies),
            msg=f"Expected drop warning, got: {anomalies}",
        )

    def test_detect_anomalies_high_unsub(self):
        client = CampaignMonitorClient.__new__(CampaignMonitorClient)
        client.api_key = "fake"
        client.timeout = 30
        client._auth = ("fake", "x")
        template_metrics = [
            {"template": "EMAIL1", "open_rate_pct": 22.0, "unsub_rate_pct": 6.5},
        ]
        anomalies = client.detect_anomalies(template_metrics)
        self.assertTrue(any("NO-GO TRIGGER" in a for a in anomalies))

    def test_missing_api_key_raises(self):
        with self.assertRaises(ValueError):
            CampaignMonitorClient("")


class TestGistViewPoller(unittest.TestCase):
    """Tests for GistViewPoller view count parsing."""

    def test_compare_to_baseline(self):
        poller = GistViewPoller("https://gist.github.com/test/abc", baseline_views=10)
        result = poller.compare_to_baseline(50)
        self.assertEqual(result["delta_since_baseline"], 40)
        self.assertAlmostEqual(result["growth_ratio_vs_baseline"], 5.0)

    def test_status_go_day3(self):
        poller = GistViewPoller("https://gist.github.com/test/abc", baseline_views=0)
        self.assertEqual(poller.get_status(75, 3), "GO")

    def test_status_nogo_day7(self):
        poller = GistViewPoller("https://gist.github.com/test/abc", baseline_views=0)
        self.assertEqual(poller.get_status(40, 7), "NO-GO")

    def test_status_caution_day14(self):
        poller = GistViewPoller("https://gist.github.com/test/abc", baseline_views=0)
        self.assertEqual(poller.get_status(200, 14), "CAUTION")

    def test_missing_gist_url_raises(self):
        with self.assertRaises(ValueError):
            GistViewPoller("")

    def test_view_count_regex_parse(self):
        """Regex patterns should match typical Gist HTML."""
        poller = GistViewPoller("https://gist.github.com/test/abc")
        html = '<span>1,234 views</span>'
        for pattern in poller._VIEW_PATTERNS:
            match = pattern.search(html)
            if match:
                raw = match.group(1).replace(",", "")
                self.assertEqual(int(raw), 1234)
                return
        self.fail("No regex pattern matched expected HTML fragment")


class TestEtsySalesExtractor(unittest.TestCase):
    """Tests for EtsySalesExtractor revenue attribution."""

    def _make_order(self, coupon_code, amount_usd):
        return {
            "coupon": {"coupon_code": coupon_code},
            "grandtotal": {"amount": int(amount_usd * 100), "divisor": 100},
        }

    def test_segment_by_coupon(self):
        extractor = EtsySalesExtractor.__new__(EtsySalesExtractor)
        orders = [
            self._make_order("EMAIL1", 7.49),
            self._make_order("EMAIL1", 7.49),
            self._make_order("EMAIL2", 7.49),
        ]
        segments = extractor.segment_by_coupon(orders)
        self.assertEqual(len(segments["EMAIL1"]), 2)
        self.assertEqual(len(segments["EMAIL2"]), 1)

    def test_compute_revenue_attribution(self):
        extractor = EtsySalesExtractor.__new__(EtsySalesExtractor)
        orders = [
            self._make_order("EMAIL1", 7.49),
            self._make_order("EMAIL3", 7.49),
        ]
        attribution = extractor.compute_revenue_attribution(orders)
        self.assertEqual(attribution["EMAIL1"]["order_count"], 1)
        self.assertAlmostEqual(attribution["EMAIL1"]["total_revenue_usd"], 7.49)
        self.assertEqual(attribution["EMAIL3"]["order_count"], 1)

    def test_no_coupon_order(self):
        extractor = EtsySalesExtractor.__new__(EtsySalesExtractor)
        orders = [{"coupon": None, "grandtotal": {"amount": 749, "divisor": 100}}]
        segments = extractor.segment_by_coupon(orders)
        self.assertIn("NO_COUPON", segments)

    def test_missing_api_key_raises(self):
        with self.assertRaises(ValueError):
            EtsySalesExtractor("", "12345")

    def test_missing_shop_id_raises(self):
        with self.assertRaises(ValueError):
            EtsySalesExtractor("valid_key", "")


class TestContingencyDecisionEngine(unittest.TestCase):
    """Tests for the 8-scenario decision tree."""

    def _base_metrics(self, day=3):
        """Nominal GO metrics for a given checkpoint day."""
        if day == 3:
            return {
                "email_open_rate_pct": 25.0,
                "email_unsub_rate_pct": 1.0,
                "gist_views": 80,
                "etsy_orders": 1,
                "etsy_listing_active": True,
                "influencer_responses": 1,
                "instagram_reach": 300,
                "twitter_mentions": 2,
                "reddit_upvotes": 15,
            }
        if day == 7:
            return {
                "email_open_rate_pct": 25.0,
                "email_unsub_rate_pct": 1.0,
                "gist_views": 210,
                "etsy_orders": 2,
                "etsy_listing_active": True,
                "influencer_responses": 4,
                "instagram_reach": 600,
                "twitter_mentions": 3,
                "reddit_upvotes": 30,
            }
        return {}

    def test_all_go_nominal(self):
        engine = ContingencyDecisionEngine()
        result = engine.evaluate(self._base_metrics(3), 3)
        self.assertEqual(result["overall_status"], "GO")

    def test_nogo_email_open_rate(self):
        engine = ContingencyDecisionEngine()
        metrics = self._base_metrics(3)
        metrics["email_open_rate_pct"] = 5.0
        result = engine.evaluate(metrics, 3)
        self.assertIn("S1", result["active_nogo_scenarios"])

    def test_nogo_gist_day7(self):
        engine = ContingencyDecisionEngine()
        metrics = self._base_metrics(7)
        metrics["gist_views"] = 40  # below Day 7 NO-GO of 50
        result = engine.evaluate(metrics, 7)
        self.assertIn("S2", result["active_nogo_scenarios"])

    def test_multi_failure_triggers_s8(self):
        engine = ContingencyDecisionEngine()
        metrics = self._base_metrics(7)
        metrics["email_open_rate_pct"] = 5.0   # S1 NO-GO
        metrics["gist_views"] = 40             # S2 NO-GO
        result = engine.evaluate(metrics, 7)
        self.assertTrue(result["multi_failure_triggered"])

    def test_caution_email_open_rate(self):
        engine = ContingencyDecisionEngine()
        metrics = self._base_metrics(3)
        metrics["email_open_rate_pct"] = 15.0
        result = engine.evaluate(metrics, 3)
        # S1 should be CAUTION
        s1 = next(s for s in result["scenario_results"] if s["scenario_key"] == "S1")
        self.assertEqual(s1["status"], "CAUTION")

    def test_high_unsub_rate_nogo(self):
        engine = ContingencyDecisionEngine()
        metrics = self._base_metrics(3)
        metrics["email_unsub_rate_pct"] = 6.0
        result = engine.evaluate(metrics, 3)
        self.assertIn("S5", result["active_nogo_scenarios"])


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def _load_env_file(path: str) -> dict:
    """Load key=value pairs from a .env file, ignoring comments and blanks."""
    env = {}
    if not os.path.exists(path):
        return env
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, val = line.partition("=")
                env[key.strip()] = val.strip().strip('"').strip("'")
    return env


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Track B Day 3/7/14 Checkpoint Automation — Item 85 "
            "(TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py)"
        )
    )
    parser.add_argument(
        "--day",
        type=int,
        choices=[3, 7, 14],
        required=False,
        default=None,
        help="Checkpoint day to run (3, 7, or 14). Required unless --test is set.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip live API calls and use dummy data (for testing)",
    )
    parser.add_argument(
        "--env-file",
        default=os.path.expanduser("~/.claude_env"),
        help="Path to .env file (default: ~/.claude_env)",
    )
    parser.add_argument(
        "--output-dir",
        default=CHECKPOINT_REPORTS_DIR_DEFAULT,
        help="Directory for checkpoint reports",
    )
    parser.add_argument(
        "--launch-date",
        default=str(LAUNCH_DATE_DEFAULT),
        help="Launch date in YYYY-MM-DD format (default: 2026-06-04)",
    )
    # Manual metric overrides
    parser.add_argument("--email-open-rate", type=float, metavar="PCT",
                        help="Override: email open rate %%")
    parser.add_argument("--email-unsub-rate", type=float, metavar="PCT",
                        help="Override: email unsubscribe rate %%")
    parser.add_argument("--gist-views", type=int,
                        help="Override: Gist cumulative view count")
    parser.add_argument("--etsy-orders", type=int,
                        help="Override: Etsy order count")
    parser.add_argument("--kit-subscribers", type=int,
                        help="Override: Kit new subscribers since launch")
    parser.add_argument("--influencer-responses", type=int,
                        help="Override: influencer public share / response count")
    parser.add_argument("--instagram-reach", type=int,
                        help="Override: Instagram cumulative reach")
    parser.add_argument("--twitter-mentions", type=int,
                        help="Override: Twitter/X mention count")
    parser.add_argument("--reddit-upvotes", type=int,
                        help="Override: Reddit cumulative upvotes")
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run unit tests instead of checkpoint",
    )

    args = parser.parse_args()

    if args.test:
        # Run unit tests
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        for test_class in [
            TestCampaignMonitorClient,
            TestGistViewPoller,
            TestEtsySalesExtractor,
            TestContingencyDecisionEngine,
        ]:
            suite.addTests(loader.loadTestsFromTestCase(test_class))
        runner = unittest.TextTestRunner(verbosity=2)
        test_result = runner.run(suite)
        sys.exit(0 if test_result.wasSuccessful() else 1)

    if args.day is None:
        parser.error("--day is required unless --test is set")

    # Load environment
    env = {}
    env.update(_load_env_file(args.env_file))
    env.update(os.environ)  # OS env takes precedence over file

    # Manual overrides
    manual_overrides = {}
    if args.email_open_rate is not None:
        manual_overrides["email_open_rate_pct"] = args.email_open_rate
    if args.email_unsub_rate is not None:
        manual_overrides["email_unsub_rate_pct"] = args.email_unsub_rate
    if args.gist_views is not None:
        manual_overrides["gist_views"] = args.gist_views
    if args.etsy_orders is not None:
        manual_overrides["etsy_orders"] = args.etsy_orders
    if args.kit_subscribers is not None:
        manual_overrides["kit_new_subscribers"] = args.kit_subscribers
    if args.influencer_responses is not None:
        manual_overrides["influencer_responses"] = args.influencer_responses
    if args.instagram_reach is not None:
        manual_overrides["instagram_reach"] = args.instagram_reach
    if args.twitter_mentions is not None:
        manual_overrides["twitter_mentions"] = args.twitter_mentions
    if args.reddit_upvotes is not None:
        manual_overrides["reddit_upvotes"] = args.reddit_upvotes

    launch_date = datetime.date.fromisoformat(args.launch_date)

    config = {
        "checkpoint_day": args.day,
        "launch_date": launch_date,
        "dry_run": args.dry_run,
        "output_dir": args.output_dir,
        "env": env,
        "manual_overrides": manual_overrides,
    }

    orchestrator = CheckpointOrchestrator(config)
    result = orchestrator.run()

    # Print final summary
    decision = result["decision"]
    overall = decision["overall_status"]
    print(f"\n{'='*60}")
    print(f"Day {args.day} Checkpoint: {overall}")
    print(f"{'='*60}")
    print(f"Action: {decision.get('recommended_action', '')}")
    if result.get("errors"):
        print(f"\nErrors ({len(result['errors'])}):")
        for e in result["errors"]:
            print(f"  - {e}")
    print(f"\nReport: {result.get('report_path', 'not written')}")

    # Exit code
    exit_codes = {"GO": 0, "CAUTION": 1, "NO-GO": 2}
    sys.exit(exit_codes.get(overall, 3))


if __name__ == "__main__":
    main()
