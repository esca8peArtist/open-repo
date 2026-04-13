#!/usr/bin/env python3
"""
civic-tracker.py — Civic Intelligence Brief

Aggregates civic intelligence from multiple public sources and produces
a formatted summary report. Designed to automate the "check primary
sources weekly" task from the personal action plan.

Usage:
    uv run civic-tracker.py
    uv run civic-tracker.py --full
    uv run civic-tracker.py --save
    uv run civic-tracker.py --full --save

Dependencies (auto-installed by uv if pyproject.toml or inline script metadata):
    httpx, feedparser, rich
"""

# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "httpx>=0.27",
#   "feedparser>=6.0",
#   "rich>=13.0",
# ]
# ///

from __future__ import annotations

import argparse
import json
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import feedparser
import httpx

# ---------------------------------------------------------------------------
# Optional rich import — graceful fallback to plain text
# ---------------------------------------------------------------------------
try:
    from rich import box
    from rich.console import Console
    from rich.panel import Panel
    from rich.rule import Rule
    from rich.table import Table
    from rich.text import Text

    RICH_AVAILABLE = True
    console = Console()
except ImportError:
    RICH_AVAILABLE = False
    console = None  # type: ignore[assignment]

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CACHE_DIR = Path(__file__).parent / ".civic-tracker-cache"
CACHE_TTL_SECONDS = 3600  # 1 hour

CONGRESS_API_BASE = "https://api.congress.gov/v3"

# Bills to actively track by number (congress number, bill type, bill number).
# Format: (congress, type, number, short label)
TRACKED_BILLS: list[tuple[int, str, int, str]] = [
    (119, "hr", 1, "Laken Riley Act (immigration detention)"),
    (119, "s", 103, "SAVE Act (voter ID)"),
    (119, "hr", 22, "DOGE Act / efficiency oversight"),
]

# Keyword searches for recent legislation — (query, label)
CONGRESS_KEYWORD_SEARCHES: list[tuple[str, str]] = [
    ("immigration detention", "Immigration Detention"),
    ("voting rights", "Voting Rights"),
    ("DOGE oversight", "DOGE Oversight"),
]

RSS_FEEDS: list[tuple[str, str]] = [
    ("https://www.justsecurity.org/feed/", "Just Security"),
    ("https://www.brennancenter.org/feeds/news", "Brennan Center"),
    ("https://www.aclu.org/news/feed", "ACLU News"),
]

DEMOCRACY_DOCKET_RSS = "https://www.democracydocket.com/feed/"

PROJECT_2025_URL = "https://project2025.observer"

ICE_LOCATOR_URL = "https://locator.ice.gov/odls/homePage.do"
TRAC_ICE_URL = "https://trac.syr.edu/phptools/immigration/detention/"

DEFAULT_TIMEOUT = 15.0  # seconds
MAX_HEADLINES_PER_SOURCE = 5
MAX_BILLS_FROM_SEARCH = 5

TODAY = datetime.now(tz=timezone.utc)
TODAY_STR = TODAY.strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


@dataclass
class NewsItem:
    title: str
    url: str
    published: str
    source: str
    summary: str = ""


@dataclass
class LegalCase:
    title: str
    url: str
    published: str
    summary: str = ""
    state: str = ""


@dataclass
class BillInfo:
    number: str
    title: str
    status: str
    last_action: str
    url: str
    label: str = ""


@dataclass
class SourceResult:
    """Wrapper for a data fetch result with optional error."""

    name: str
    data: list = field(default_factory=list)
    error: Optional[str] = None
    cached: bool = False


# ---------------------------------------------------------------------------
# Cache helpers
# ---------------------------------------------------------------------------


def _cache_path(key: str) -> Path:
    """Return cache file path for a given key."""
    safe_key = "".join(c if c.isalnum() else "_" for c in key)
    return CACHE_DIR / f"{safe_key}.json"


def _read_cache(key: str) -> Optional[dict]:
    """Read cached data if it exists and is still fresh."""
    path = _cache_path(key)
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text())
        stored_at = payload.get("stored_at", 0)
        if time.time() - stored_at < CACHE_TTL_SECONDS:
            return payload.get("data")
    except (json.JSONDecodeError, OSError):
        pass
    return None


def _write_cache(key: str, data: dict | list) -> None:
    """Write data to cache with a timestamp."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = _cache_path(key)
    try:
        path.write_text(json.dumps({"stored_at": time.time(), "data": data}))
    except OSError:
        pass  # Non-fatal — caching is best-effort


# ---------------------------------------------------------------------------
# HTTP helper
# ---------------------------------------------------------------------------


def _get(
    url: str, params: Optional[dict] = None, timeout: float = DEFAULT_TIMEOUT
) -> httpx.Response:
    """Perform a GET request with a descriptive User-Agent."""
    headers = {
        "User-Agent": (
            "civic-tracker/1.0 (personal civic intelligence tool; "
            "github.com/SuperClaude-Org/SuperClaude_Framework)"
        ),
        "Accept": "application/json, text/html, application/xhtml+xml, */*",
    }
    return httpx.get(
        url, params=params, headers=headers, timeout=timeout, follow_redirects=True
    )


# ---------------------------------------------------------------------------
# Source: Congress.gov — tracked bills
# ---------------------------------------------------------------------------


def fetch_tracked_bills() -> SourceResult:
    """Fetch status for explicitly tracked bills from Congress.gov."""
    name = "Congress.gov (Tracked Bills)"
    cached = _read_cache("tracked_bills")
    if cached is not None:
        bills = [BillInfo(**b) for b in cached]
        return SourceResult(name=name, data=bills, cached=True)

    bills: list[BillInfo] = []
    errors: list[str] = []

    for congress, bill_type, bill_num, label in TRACKED_BILLS:
        url = f"{CONGRESS_API_BASE}/bill/{congress}/{bill_type}/{bill_num}"
        try:
            resp = _get(url, params={"format": "json"})
            resp.raise_for_status()
            payload = resp.json()
            bill = payload.get("bill", {})
            actions = bill.get("latestAction", {})
            title = bill.get("title", "Unknown title")
            status = bill.get("type", "").upper() + str(bill.get("number", ""))
            last_action = (
                f"{actions.get('actionDate', 'N/A')}: {actions.get('text', 'N/A')}"
            )
            bill_url = (
                f"https://www.congress.gov/{congress}/bills/"
                f"{bill_type}{bill_num}/BILLS-{congress}{bill_type}{bill_num}is.htm"
            )
            bills.append(
                BillInfo(
                    number=f"{bill_type.upper()}{bill_num}",
                    title=title,
                    status=status,
                    last_action=last_action,
                    url=f"https://www.congress.gov/bill/{congress}th-congress/"
                    + ("house" if bill_type == "hr" else "senate")
                    + f"-bill/{bill_num}",
                    label=label,
                )
            )
        except httpx.HTTPStatusError as e:
            errors.append(
                f"HTTP {e.response.status_code} for {bill_type.upper()}{bill_num}"
            )
        except (httpx.RequestError, KeyError, ValueError) as e:
            errors.append(f"Error fetching {bill_type.upper()}{bill_num}: {e}")

    _write_cache("tracked_bills", [b.__dict__ for b in bills])
    error_msg = "; ".join(errors) if errors else None
    return SourceResult(name=name, data=bills, error=error_msg)


# ---------------------------------------------------------------------------
# Source: Congress.gov — keyword search
# ---------------------------------------------------------------------------


def fetch_congress_keyword_search() -> SourceResult:
    """Search Congress.gov for recently updated bills matching tracked keywords."""
    name = "Congress.gov (Keyword Search)"
    cached = _read_cache("congress_keywords")
    if cached is not None:
        bills = [BillInfo(**b) for b in cached]
        return SourceResult(name=name, data=bills, cached=True)

    bills: list[BillInfo] = []
    seen_ids: set[str] = set()
    errors: list[str] = []

    for query, label in CONGRESS_KEYWORD_SEARCHES:
        params = {
            "format": "json",
            "limit": MAX_BILLS_FROM_SEARCH,
            "sort": "updateDate+desc",
            "query": query,
        }
        url = f"{CONGRESS_API_BASE}/bill"
        try:
            resp = _get(url, params=params)
            resp.raise_for_status()
            payload = resp.json()
            for b in payload.get("bills", []):
                bill_id = (
                    f"{b.get('type', '')}{b.get('number', '')}_{b.get('congress', '')}"
                )
                if bill_id in seen_ids:
                    continue
                seen_ids.add(bill_id)
                congress = b.get("congress", 119)
                bill_type = b.get("type", "").lower()
                bill_num = b.get("number", "")
                last_action = b.get("latestAction", {})
                chamber = (
                    "house"
                    if bill_type in ("hr", "hres", "hjres", "hconres")
                    else "senate"
                )
                bills.append(
                    BillInfo(
                        number=f"{b.get('type', '')}{bill_num}",
                        title=b.get("title", "No title"),
                        status=b.get("type", "").upper(),
                        last_action=(
                            f"{last_action.get('actionDate', 'N/A')}: "
                            f"{last_action.get('text', 'N/A')}"
                        ),
                        url=f"https://www.congress.gov/bill/{congress}th-congress/{chamber}-bill/{bill_num}",
                        label=label,
                    )
                )
        except httpx.HTTPStatusError as e:
            errors.append(f"HTTP {e.response.status_code} searching '{query}'")
        except (httpx.RequestError, KeyError, ValueError) as e:
            errors.append(f"Error searching '{query}': {e}")

    _write_cache("congress_keywords", [b.__dict__ for b in bills])
    error_msg = "; ".join(errors) if errors else None
    return SourceResult(name=name, data=bills, error=error_msg)


# ---------------------------------------------------------------------------
# Source: Democracy Docket RSS
# ---------------------------------------------------------------------------


def fetch_democracy_docket() -> SourceResult:
    """Fetch recent case updates from Democracy Docket RSS feed."""
    name = "Democracy Docket"
    cached = _read_cache("democracy_docket")
    if cached is not None:
        cases = [LegalCase(**c) for c in cached]
        return SourceResult(name=name, data=cases, cached=True)

    try:
        # feedparser handles its own HTTP but we wrap in try/except
        feed = feedparser.parse(DEMOCRACY_DOCKET_RSS)
        if feed.bozo and not feed.entries:
            raise ValueError(f"Feed parse error: {feed.bozo_exception}")

        cases: list[LegalCase] = []
        for entry in feed.entries[:8]:
            published = ""
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                published = time.strftime("%Y-%m-%d", entry.published_parsed)
            elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
                published = time.strftime("%Y-%m-%d", entry.updated_parsed)

            summary = ""
            if hasattr(entry, "summary"):
                # Strip HTML tags simply
                import re

                summary = re.sub(r"<[^>]+>", "", entry.summary).strip()
                summary = summary[:300] + "..." if len(summary) > 300 else summary

            # Try to extract state from categories or tags
            state = ""
            if hasattr(entry, "tags"):
                for tag in entry.tags:
                    term = tag.get("term", "")
                    if len(term) == 2 and term.isupper():
                        state = term
                        break

            cases.append(
                LegalCase(
                    title=entry.get("title", "Untitled"),
                    url=entry.get("link", DEMOCRACY_DOCKET_RSS),
                    published=published,
                    summary=summary,
                    state=state,
                )
            )

        _write_cache("democracy_docket", [c.__dict__ for c in cases])
        return SourceResult(name=name, data=cases)

    except Exception as e:
        return SourceResult(name=name, data=[], error=str(e))


# ---------------------------------------------------------------------------
# Source: Project 2025 Observer
# ---------------------------------------------------------------------------


def fetch_project2025() -> SourceResult:
    """
    Attempt to fetch implementation status from project2025.observer.

    The site does not publish a formal API or RSS feed, so we do a lightweight
    GET and report the HTTP status / page availability. A --full run includes
    a direct link for manual review.
    """
    name = "Project 2025 Observer"
    try:
        resp = _get(PROJECT_2025_URL, timeout=10.0)
        if resp.status_code == 200:
            # Site is up — no machine-readable API available
            return SourceResult(
                name=name,
                data=[
                    {
                        "status": "online",
                        "url": PROJECT_2025_URL,
                        "note": (
                            "project2025.observer is online. No public API is available. "
                            "Visit directly to review implementation status."
                        ),
                    }
                ],
            )
        else:
            return SourceResult(
                name=name,
                data=[],
                error=f"Site returned HTTP {resp.status_code}",
            )
    except httpx.RequestError as e:
        return SourceResult(name=name, data=[], error=f"Connection error: {e}")


# ---------------------------------------------------------------------------
# Source: ICE detention population
# ---------------------------------------------------------------------------


def fetch_ice_detention() -> SourceResult:
    """
    Attempt to retrieve ICE detention population figures.

    locator.ice.gov does not expose a public API. TRAC Immigration at
    Syracuse University publishes detention statistics, but requires
    navigating JavaScript-heavy pages. We check reachability and
    surface direct links for manual review.
    """
    name = "ICE Detention Stats"
    results = []

    for label, url in [
        ("ICE Online Detainee Locator", ICE_LOCATOR_URL),
        ("TRAC Immigration Detention Data", TRAC_ICE_URL),
    ]:
        try:
            resp = _get(url, timeout=10.0)
            status = "online" if resp.status_code < 400 else f"HTTP {resp.status_code}"
        except httpx.RequestError as e:
            status = f"unreachable ({e})"

        results.append({"label": label, "url": url, "status": status})

    return SourceResult(
        name=name,
        data=results,
        error=(
            None
            if any(r["status"] == "online" for r in results)
            else "Both ICE/TRAC sources appear unreachable"
        ),
    )


# ---------------------------------------------------------------------------
# Source: RSS news feeds
# ---------------------------------------------------------------------------


def fetch_rss_feed(feed_url: str, source_name: str) -> SourceResult:
    """Fetch and parse a single RSS feed."""
    cache_key = f"rss_{source_name.replace(' ', '_').lower()}"
    cached = _read_cache(cache_key)
    if cached is not None:
        items = [NewsItem(**i) for i in cached]
        return SourceResult(name=source_name, data=items, cached=True)

    try:
        feed = feedparser.parse(feed_url)
        if feed.bozo and not feed.entries:
            raise ValueError(f"Feed parse error: {feed.bozo_exception}")

        items: list[NewsItem] = []
        for entry in feed.entries[:MAX_HEADLINES_PER_SOURCE]:
            published = ""
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                published = time.strftime("%Y-%m-%d", entry.published_parsed)
            elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
                published = time.strftime("%Y-%m-%d", entry.updated_parsed)

            summary = ""
            if hasattr(entry, "summary"):
                import re

                summary = re.sub(r"<[^>]+>", "", entry.summary).strip()
                summary = summary[:250] + "..." if len(summary) > 250 else summary

            items.append(
                NewsItem(
                    title=entry.get("title", "Untitled"),
                    url=entry.get("link", feed_url),
                    published=published,
                    source=source_name,
                    summary=summary,
                )
            )

        _write_cache(cache_key, [i.__dict__ for i in items])
        return SourceResult(name=source_name, data=items)

    except Exception as e:
        return SourceResult(name=source_name, data=[], error=str(e))


def fetch_all_rss_feeds() -> list[SourceResult]:
    """Fetch all configured RSS news feeds."""
    return [fetch_rss_feed(url, name) for url, name in RSS_FEEDS]


# ---------------------------------------------------------------------------
# Rendering — rich version
# ---------------------------------------------------------------------------


def _render_rich(
    tracked_bills: SourceResult,
    keyword_bills: SourceResult,
    docket: SourceResult,
    p2025: SourceResult,
    ice: SourceResult,
    feeds: list[SourceResult],
    full: bool,
) -> str:
    """Render a rich-formatted report to terminal and return plain-text version."""
    assert console is not None

    lines: list[str] = []  # plain-text accumulator for --save

    def _hr(title: str = "") -> None:
        console.rule(f"[bold cyan]{title}[/bold cyan]" if title else "", style="cyan")
        lines.append(f"\n{'─' * 60}\n{title}")

    def _section(heading: str, emoji: str = "") -> None:
        label = f"{emoji}  {heading}" if emoji else heading
        console.print(f"\n[bold yellow]{label}[/bold yellow]")
        lines.append(f"\n{label}\n{'─' * len(label)}")

    def _item(text: str, indent: int = 2) -> None:
        pad = " " * indent
        console.print(f"{pad}[white]{text}[/white]")
        lines.append(f"{pad}{text}")

    def _dim(text: str, indent: int = 4) -> None:
        pad = " " * indent
        console.print(f"{pad}[dim]{text}[/dim]")
        lines.append(f"{pad}{text}")

    def _error(text: str) -> None:
        console.print(f"  [red]  {text}[/red]")
        lines.append(f"  ERROR: {text}")

    def _warn(text: str) -> None:
        console.print(f"  [yellow]  {text}[/yellow]")
        lines.append(f"  NOTE: {text}")

    # Header
    console.print()
    console.rule(
        f"[bold white]CIVIC INTELLIGENCE BRIEF — {TODAY_STR}[/bold white]",
        style="bold cyan",
    )
    console.print()
    lines.append(f"\n{'═' * 60}")
    lines.append(f"  CIVIC INTELLIGENCE BRIEF — {TODAY_STR}")
    lines.append(f"{'═' * 60}\n")

    # ── LEGISLATION ──────────────────────────────────────────────
    _section("LEGISLATION UPDATES", "📊")

    if tracked_bills.data or tracked_bills.error:
        console.print("  [bold]Tracked Bills:[/bold]")
        lines.append("\n  Tracked Bills:")
        if tracked_bills.cached:
            _warn("(from cache)")
        if tracked_bills.error:
            _error(f"Partial errors: {tracked_bills.error}")
        for b in tracked_bills.data:
            b: BillInfo
            console.print(
                f"  [cyan]{b.number}[/cyan] — [white]{b.label or b.title[:60]}[/white]"
            )
            lines.append(f"  {b.number} — {b.label or b.title[:60]}")
            _dim(f"Status: {b.last_action}")
            _dim(f"URL: {b.url}")

    if keyword_bills.data:
        console.print("\n  [bold]Recently Active Bills (keyword search):[/bold]")
        lines.append("\n  Recently Active Bills (keyword search):")
        if keyword_bills.cached:
            _warn("(from cache)")
        current_label = ""
        for b in keyword_bills.data:
            b: BillInfo
            if b.label != current_label:
                console.print(f"  [yellow]{b.label}:[/yellow]")
                lines.append(f"  {b.label}:")
                current_label = b.label
            title_trunc = b.title[:70] + "..." if len(b.title) > 70 else b.title
            _item(f"{b.number}: {title_trunc}", indent=4)
            if full:
                _dim(b.last_action)
                _dim(b.url)
    elif keyword_bills.error:
        _error(f"Keyword search: {keyword_bills.error}")

    # ── LITIGATION ───────────────────────────────────────────────
    _section("LITIGATION", "⚖️")

    if docket.error and not docket.data:
        _error(f"Democracy Docket unavailable: {docket.error}")
        _warn("Check directly: https://democracydocket.com/cases/")
    else:
        if docket.cached:
            _warn("(from cache)")
        for case in docket.data:
            case: LegalCase
            state_tag = f" [{case.state}]" if case.state else ""
            console.print(
                f"  [cyan]{case.published}[/cyan]{state_tag}  "
                f"[white]{case.title[:70]}[/white]"
            )
            lines.append(f"  {case.published}{state_tag}  {case.title[:70]}")
            if full and case.summary:
                _dim(case.summary)
            _dim(case.url) if full else None

    # ── PROJECT 2025 ─────────────────────────────────────────────
    _section("PROJECT 2025 TRACKER", "🗂️")

    if p2025.data:
        item = p2025.data[0]
        status_color = "green" if item.get("status") == "online" else "red"
        console.print(
            f"  [{status_color}]{item.get('status', 'unknown').upper()}[/{status_color}]  "
            f"{PROJECT_2025_URL}"
        )
        lines.append(f"  {item.get('status', 'unknown').upper()}  {PROJECT_2025_URL}")
        _dim(item.get("note", ""))
    elif p2025.error:
        _error(f"project2025.observer: {p2025.error}")

    # ── ICE DETENTION ────────────────────────────────────────────
    _section("ICE DETENTION", "🔒")

    if ice.error and not ice.data:
        _error(ice.error)
    else:
        for r in ice.data:
            status_color = "green" if r["status"] == "online" else "red"
            console.print(
                f"  [{status_color}]{r['status'].upper()}[/{status_color}]  "
                f"[dim]{r['label']}[/dim]"
            )
            lines.append(f"  {r['status'].upper()}  {r['label']}")
            _dim(r["url"]) if full else None
        _warn(
            "No public API available for real-time detention counts. "
            "Visit TRAC link for statistical reports."
        )

    # ── NEWS HEADLINES ───────────────────────────────────────────
    _section("RECENT HEADLINES", "📰")

    any_news = False
    for result in feeds:
        if result.error and not result.data:
            _error(f"{result.name}: {result.error}")
            continue
        if not result.data:
            continue
        any_news = True
        console.print(f"\n  [bold]{result.name}[/bold]")
        lines.append(f"\n  {result.name}")
        if result.cached:
            _warn("(from cache)")
        for item in result.data:
            item: NewsItem
            console.print(
                f"  [cyan]{item.published}[/cyan]  [white]{item.title}[/white]"
            )
            lines.append(f"  {item.published}  {item.title}")
            if full and item.summary:
                _dim(item.summary)
            _dim(item.url) if full else None

    if not any_news:
        _warn("No news items retrieved from any RSS feed.")

    # ── FOOTER ───────────────────────────────────────────────────
    console.print()
    console.rule(style="cyan")
    console.print(
        "[bold cyan]  Next actions:[/bold cyan]\n"
        "  1. Review flagged legislation and call your representatives (5calls.org)\n"
        "  2. Share any Democracy Docket cases with local legal networks\n"
        "  3. Visit project2025.observer for implementation detail\n"
        "  4. Check TRAC for updated detention population figures\n"
        "  5. Forward relevant headlines to your organizing network"
    )
    console.rule(style="cyan")
    console.print()

    lines.append(f"\n{'═' * 60}")
    lines.append("  Next actions:")
    lines.append(
        "  1. Review flagged legislation and call your representatives (5calls.org)"
    )
    lines.append("  2. Share any Democracy Docket cases with local legal networks")
    lines.append("  3. Visit project2025.observer for implementation detail")
    lines.append("  4. Check TRAC for updated detention population figures")
    lines.append("  5. Forward relevant headlines to your organizing network")
    lines.append(f"{'═' * 60}\n")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Rendering — plain text fallback
# ---------------------------------------------------------------------------


def _render_plain(
    tracked_bills: SourceResult,
    keyword_bills: SourceResult,
    docket: SourceResult,
    p2025: SourceResult,
    ice: SourceResult,
    feeds: list[SourceResult],
    full: bool,
) -> str:
    """Render a plain-text report (no rich dependency)."""
    out: list[str] = []

    def h(text: str) -> None:
        out.append(f"\n{'═' * 60}")
        out.append(f"  {text}")
        out.append(f"{'═' * 60}")

    def s(text: str) -> None:
        out.append(f"\n{text}")
        out.append("─" * len(text))

    def item(text: str, indent: int = 2) -> None:
        out.append(" " * indent + text)

    def dim(text: str, indent: int = 4) -> None:
        out.append(" " * indent + text)

    h(f"CIVIC INTELLIGENCE BRIEF — {TODAY_STR}")

    s("LEGISLATION UPDATES")
    if tracked_bills.data:
        out.append("\n  Tracked Bills:")
        if tracked_bills.error:
            out.append(f"  [PARTIAL ERROR] {tracked_bills.error}")
        for b in tracked_bills.data:
            item(f"{b.number} — {b.label or b.title[:60]}")
            dim(f"Last action: {b.last_action}")
            if full:
                dim(f"URL: {b.url}")

    if keyword_bills.data:
        out.append("\n  Recently Active Bills (keyword search):")
        current_label = ""
        for b in keyword_bills.data:
            if b.label != current_label:
                out.append(f"  {b.label}:")
                current_label = b.label
            title_trunc = b.title[:70] + "..." if len(b.title) > 70 else b.title
            dim(f"{b.number}: {title_trunc}")
            if full:
                dim(f"  {b.last_action}")

    s("LITIGATION")
    if docket.error and not docket.data:
        out.append(f"  [ERROR] Democracy Docket: {docket.error}")
        out.append("  Check: https://democracydocket.com/cases/")
    else:
        for case in docket.data:
            state_tag = f" [{case.state}]" if case.state else ""
            item(f"{case.published}{state_tag}  {case.title[:70]}")
            if full and case.summary:
                dim(case.summary)

    s("PROJECT 2025 TRACKER")
    if p2025.data:
        item_d = p2025.data[0]
        item(f"{item_d.get('status', '?').upper()}  {PROJECT_2025_URL}")
        dim(item_d.get("note", ""))
    elif p2025.error:
        item(f"[ERROR] {p2025.error}")

    s("ICE DETENTION")
    for r in ice.data:
        item(f"{r['status'].upper()}  {r['label']}")
        if full:
            dim(r["url"])
    if ice.data:
        item("No public API for real-time counts — visit TRAC link for stats.")

    s("RECENT HEADLINES")
    for result in feeds:
        if result.error and not result.data:
            out.append(f"  [ERROR] {result.name}: {result.error}")
            continue
        if not result.data:
            continue
        out.append(f"\n  {result.name}")
        for news in result.data:
            item(f"{news.published}  {news.title}")
            if full and news.summary:
                dim(news.summary)
            if full:
                dim(news.url)

    out.append(f"\n{'═' * 60}")
    out.append("  Next actions:")
    out.append(
        "  1. Review flagged legislation and call your representatives (5calls.org)"
    )
    out.append("  2. Share any Democracy Docket cases with local legal networks")
    out.append("  3. Visit project2025.observer for implementation detail")
    out.append("  4. Check TRAC for updated detention population figures")
    out.append("  5. Forward relevant headlines to your organizing network")
    out.append(f"{'═' * 60}\n")

    report = "\n".join(out)
    print(report)
    return report


# ---------------------------------------------------------------------------
# Save report to markdown
# ---------------------------------------------------------------------------


def save_report(content: str, output_dir: Path) -> Path:
    """Write the report as a markdown file."""
    filename = output_dir / f"civic-tracker-report-{TODAY_STR}.md"
    header = (
        f"# Civic Intelligence Brief — {TODAY_STR}\n\n"
        f"*Generated by civic-tracker.py on {TODAY.strftime('%Y-%m-%d %H:%M UTC')}*\n\n"
        "---\n\n"
    )
    filename.write_text(header + content, encoding="utf-8")
    return filename


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    """Entry point: parse arguments, fetch data, render report."""
    parser = argparse.ArgumentParser(
        description="Civic Intelligence Brief — aggregate public civic data sources",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  uv run civic-tracker.py\n"
            "  uv run civic-tracker.py --full\n"
            "  uv run civic-tracker.py --full --save\n"
            "  uv run civic-tracker.py --no-cache\n"
        ),
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Include summaries, URLs, and extended detail in output",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save report to civic-tracker-report-YYYY-MM-DD.md in script directory",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Ignore cached responses and fetch fresh data from all sources",
    )
    parser.add_argument(
        "--plain",
        action="store_true",
        help="Use plain-text output even if rich is available",
    )
    args = parser.parse_args()

    # If --no-cache, clear the cache directory
    if args.no_cache and CACHE_DIR.exists():
        import shutil

        shutil.rmtree(CACHE_DIR)

    # Fetch all data (in straightforward sequential order — each source is
    # independent and most are fast; async would complicate error handling
    # for minimal gain on a weekly-use tool)
    if RICH_AVAILABLE and not args.plain:
        console.print("[dim]Fetching data from sources...[/dim]")  # type: ignore[union-attr]

    tracked = fetch_tracked_bills()
    keywords = fetch_congress_keyword_search()
    docket = fetch_democracy_docket()
    p2025 = fetch_project2025()
    ice = fetch_ice_detention()
    feeds = fetch_all_rss_feeds()

    use_rich = RICH_AVAILABLE and not args.plain

    if use_rich:
        plain_content = _render_rich(
            tracked_bills=tracked,
            keyword_bills=keywords,
            docket=docket,
            p2025=p2025,
            ice=ice,
            feeds=feeds,
            full=args.full,
        )
    else:
        plain_content = _render_plain(
            tracked_bills=tracked,
            keyword_bills=keywords,
            docket=docket,
            p2025=p2025,
            ice=ice,
            feeds=feeds,
            full=args.full,
        )

    if args.save:
        output_path = save_report(plain_content, Path(__file__).parent)
        if use_rich and console:
            console.print(f"[green]Report saved:[/green] {output_path}")
        else:
            print(f"Report saved: {output_path}")


if __name__ == "__main__":
    main()
