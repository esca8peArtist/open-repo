# Civic Intelligence Tracker

A command-line tool that aggregates civic intelligence from multiple public sources and produces a formatted summary report. Designed to automate the "check primary sources weekly" task from the personal action plan.

---

## What it tracks

| Source | What you get |
|---|---|
| **Congress.gov** | Status of explicitly tracked bills (Laken Riley Act, SAVE Act, DOGE Act) + keyword search results for immigration detention, voting rights, and DOGE oversight bills |
| **Democracy Docket** | Recent voting rights and election law case updates via RSS |
| **Project 2025 Observer** | Availability check with direct link to implementation tracker |
| **ICE / TRAC** | Reachability check and direct links for detention population stats |
| **Just Security** | Recent headlines via RSS |
| **Brennan Center** | Recent headlines via RSS |
| **ACLU News** | Recent headlines via RSS |

No API keys are required. All sources are free and public.

---

## How to run it

This project uses `uv` for Python dependency management. The script uses inline dependency metadata, so `uv` will auto-install `httpx`, `feedparser`, and `rich` on first run.

```bash
# Standard run — formatted terminal output
uv run civic-tracker.py

# Full output — includes summaries, URLs, extended detail
uv run civic-tracker.py --full

# Save report to markdown file
uv run civic-tracker.py --save

# Full output + save
uv run civic-tracker.py --full --save

# Skip cache — fetch fresh data from all sources
uv run civic-tracker.py --no-cache

# Plain text output (no rich formatting)
uv run civic-tracker.py --plain
```

### Saved report location

When `--save` is used, the report is written to:

```
projects/resistance-research/civic-tracker-report-YYYY-MM-DD.md
```

---

## Caching

Responses are cached for 1 hour in a `.civic-tracker-cache/` directory next to the script. This prevents hammering sources if you run the script multiple times in a session. Use `--no-cache` to force a fresh fetch.

---

## How to add new sources

### Add an RSS feed

1. Find the RSS URL for the source (e.g., `https://example.org/feed`)
2. Add it to the `RSS_FEEDS` list near the top of `civic-tracker.py`:

```python
RSS_FEEDS: list[tuple[str, str]] = [
    ("https://www.justsecurity.org/feed/", "Just Security"),
    ("https://www.brennancenter.org/feeds/news", "Brennan Center"),
    ("https://www.aclu.org/news/feed", "ACLU News"),
    ("https://example.org/feed", "My New Source"),  # add here
]
```

That's it — the `fetch_all_rss_feeds()` function handles the rest.

### Track a new bill

Add to the `TRACKED_BILLS` list with the congress number, bill type, bill number, and a descriptive label:

```python
TRACKED_BILLS: list[tuple[int, str, int, str]] = [
    (119, "hr", 1, "Laken Riley Act (immigration detention)"),
    (119, "s", 103, "SAVE Act (voter ID)"),
    (119, "s", 999, "My New Bill"),  # add here
]
```

Bill types: `hr` (House bill), `s` (Senate bill), `hres`, `sres`, `hjres`, `sjres`.

### Add a keyword search

Add to `CONGRESS_KEYWORD_SEARCHES`:

```python
CONGRESS_KEYWORD_SEARCHES: list[tuple[str, str]] = [
    ("immigration detention", "Immigration Detention"),
    ("voting rights", "Voting Rights"),
    ("emergency powers", "Emergency Powers"),  # add here
]
```

### Add a custom data source

Write a function following the `SourceResult` pattern:

```python
def fetch_my_source() -> SourceResult:
    """Fetch data from my source."""
    name = "My Source"
    try:
        resp = _get("https://example.org/data.json")
        resp.raise_for_status()
        data = resp.json()
        # transform data into a list of dicts or dataclass instances
        return SourceResult(name=name, data=data)
    except Exception as e:
        return SourceResult(name=name, data=[], error=str(e))
```

Then call it in `main()` and add rendering logic in both `_render_rich()` and `_render_plain()`.

---

## Scheduling

### Linux / WSL — cron

Run every Sunday at 8am and save the report:

```bash
# Open crontab
crontab -e

# Add this line (adjust the path to match your actual install location):
0 8 * * 0 cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research && uv run civic-tracker.py --full --save >> /tmp/civic-tracker.log 2>&1
```

To verify the cron job was added:

```bash
crontab -l
```

### Windows Task Scheduler (from WSL)

Create a `.bat` file that calls WSL:

```bat
@echo off
wsl -e bash -c "cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research && uv run civic-tracker.py --full --save"
```

Then schedule it in Task Scheduler (search "Task Scheduler" in Start menu):
1. Create Basic Task
2. Set trigger: Weekly, Sunday, 8:00 AM
3. Action: Start a program → point to your `.bat` file

### Email the report to yourself (optional)

Append to your cron command using `mail` or `sendmail`:

```bash
0 8 * * 0 cd /path/to/dir && uv run civic-tracker.py --full --save && cat civic-tracker-report-$(date +\%Y-\%m-\%d).md | mail -s "Weekly Civic Brief" you@example.com
```

---

## Sources and rationale

| Source | Why it's included |
|---|---|
| **Congress.gov API** | Official, free, no key required, machine-readable |
| **Democracy Docket** | Primary tracker for voting rights / election law litigation; publishes RSS |
| **Project 2025 Observer** | Tracks implementation of Project 2025 agenda items in real time |
| **TRAC Immigration** | Syracuse University data project; most comprehensive public detention stats |
| **Just Security** | Rigorous analysis of national security, rule of law, and democracy issues |
| **Brennan Center** | Nonpartisan law and policy institute focused on voting, justice, security |
| **ACLU** | Litigation and advocacy tracker across civil liberties issues |

---

## Limitations

- **Project 2025 Observer** and **ICE/TRAC** do not have public machine-readable APIs. The script checks that those sites are reachable and surfaces direct links for manual review.
- Congress.gov rate limits unauthenticated requests. The 1-hour cache prevents hitting limits during repeated runs. If you see HTTP 429 errors, wait an hour or register for a free API key at [api.congress.gov](https://api.congress.gov) and add it to `_get()` as a header.
- RSS feeds may change their URLs. If a feed stops working, check the source site for an updated feed URL and update `RSS_FEEDS`.
