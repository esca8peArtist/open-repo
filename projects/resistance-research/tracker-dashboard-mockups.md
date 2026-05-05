---
title: "Tracker Dashboard Mockups — Visualization and Institutional Partner Formats"
subtitle: "Design specifications for static export, interactive web dashboard, institutional briefings, and accessibility standards"
date: 2026-05-05
status: design-phase
project: resistance-research
purpose: Post-Phase-1 automation infrastructure
cross_references:
  - tracker-automation-architecture.md
  - tracker-data-source-audit.md
  - tracker-maintenance-playbook.md
---

# Tracker Dashboard Mockups

*Created: May 5, 2026. Purpose: Design concrete visualization and distribution formats for all four trackers. All design decisions here are specific enough to implement directly. Technology stack choices are justified against the project's constraints (small team, no dedicated frontend developer, institutional partner requirements).*

---

## Design Principles

Before the mockups, three decisions that shape all of the following:

**Decision 1: Static-first, interactive-optional.** A static dashboard (a PDF or a GitHub Pages site generated from Markdown/CSV) can be produced now with zero infrastructure. An interactive web dashboard adds value but requires ongoing maintenance. The design here prioritizes static formats that institutional partners can receive, open, and use immediately, with an interactive layer added in a second phase.

**Decision 2: Datasette as the interactive layer.** Rather than building a custom web app, Datasette renders a SQLite database as a browseable, filterable, searchable web interface with zero custom frontend code. It produces the URL structure `/tracker/entries` with automatic column filters, full-text search, and CSV/JSON export. This eliminates the need for a frontend developer.

**Decision 3: Separate formats for different audiences.** Institutional partners (law schools, advocacy organizations) need a one-page PDF briefing. Journalists need a filterable web interface with CSV export. The general public needs a clean, readable summary page. These are three different products built from the same database.

---

## 1. Static Dashboard (PDF / Printable Web Page)

The static dashboard is the minimum viable product. It can be generated from the tracker database with a Python script and Pandoc, requiring no web hosting. A new version can be emailed to partners weekly.

### 1.1 Layout (One Page Per Tracker)

```
┌────────────────────────────────────────────────────────────────────┐
│  [TRACKER NAME] TRACKER                        Updated: 2026-05-05 │
│  resistance-research.org / [tracker-slug]                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  SUMMARY STATISTICS (this month vs. last month)                    │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐              │
│  │ 47 New       │ │ 23 States    │ │ 12 Federal   │              │
│  │ Entries      │ │ Affected     │ │ Actions      │              │
│  │ (+18% vs     │ │              │ │              │              │
│  │ last month)  │ │              │ │              │              │
│  └──────────────┘ └──────────────┘ └──────────────┘              │
│                                                                    │
│  CATEGORY BREAKDOWN (last 90 days)                                 │
│  ████████████████████ Prosecutorial (38%)                          │
│  ███████████████ Civil (29%)                                       │
│  ██████████ Press Freedom (19%)                                    │
│  ████████ Legislative (14%)                                        │
│                                                                    │
│  TREND (weekly entry volume, last 90 days)                         │
│  15 │          ╭─╮                                                 │
│  10 │      ╭───╯ ╰───╮   ╭──                                      │
│   5 │  ╭───╯         ╰───╯                                        │
│   0 └──────────────────────────────────────────                   │
│       Feb        Mar        Apr        May                         │
│                                                                    │
│  RECENT HIGH-CONFIDENCE ENTRIES (last 14 days)                     │
│  2026-05-02  FBI retaliatory investigation of NYT reporter         │
│              [High] [press-exclusion] [federal]                    │
│  2026-04-27  SPLC indictment — 11 counts wire fraud               │
│              [High] [civil-society-targeting] [federal]            │
│  2026-04-21  SCOTUS Villarreal QI denial — press accountability    │
│              [High] [qualified-immunity] [federal]                 │
│  ...                                                               │
│                                                                    │
│  HIGHEST-FREQUENCY STATES (last 90 days)                           │
│  California (12)  Texas (9)  Florida (8)  New York (7)            │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### 1.2 Generation Script

The static dashboard is generated from the tracker database using Python + Jinja2 templates + Pandoc.

```python
# generate_static_dashboard.py
from jinja2 import Template
import subprocess, sqlite3, json
from datetime import date, timedelta

def generate_dashboard(tracker_name, db_path, output_path):
    conn = sqlite3.connect(db_path)
    
    # Pull statistics
    thirty_days_ago = (date.today() - timedelta(days=30)).isoformat()
    stats = conn.execute("""
        SELECT 
            COUNT(*) as new_entries,
            COUNT(DISTINCT state) as states_affected,
            SUM(CASE WHEN state = 'federal' THEN 1 ELSE 0 END) as federal_count
        FROM entries 
        WHERE tracker = ? AND date >= ? AND is_published = 1
    """, (tracker_name, thirty_days_ago)).fetchone()
    
    # Pull recent entries
    recent = conn.execute("""
        SELECT date, headline, confidence, category, state
        FROM entries
        WHERE tracker = ? AND is_published = 1
        ORDER BY date DESC LIMIT 10
    """, (tracker_name,)).fetchall()
    
    # Render template
    with open(f"templates/dashboard_{tracker_name}.md.j2") as f:
        template = Template(f.read())
    
    rendered = template.render(stats=stats, recent=recent, 
                               updated=date.today().isoformat())
    
    with open(f"/tmp/dashboard_{tracker_name}.md", "w") as f:
        f.write(rendered)
    
    # Convert to PDF via Pandoc
    subprocess.run([
        "pandoc", f"/tmp/dashboard_{tracker_name}.md",
        "-o", output_path,
        "--pdf-engine=xelatex",
        "--template=templates/briefing.tex"
    ])
```

---

## 2. Interactive Dashboard (Datasette-Based)

Datasette serves the tracker database as a live, searchable web interface. It requires Python and SQLite only — no database server, no custom frontend code.

### 2.1 What Datasette Provides Out of the Box

After running `datasette tracker.db`, the following endpoints are available immediately:

- `/tracker` — browse all tables
- `/tracker/entries` — paginated, sortable list of all entries
- `/tracker/entries?tracker=first-amendment` — filtered view
- `/tracker/entries?_search=journalist` — full-text search
- `/tracker/entries.csv` — instant CSV export
- `/tracker/entries.json` — instant JSON export
- `/tracker/entries?date__gte=2026-01-01` — date-range filter
- `/tracker/entries?confidence=high` — confidence filter
- `/tracker/entries?state=CA` — state filter

This eliminates the need to build a custom filter interface.

### 2.2 Custom Plugin: RSS Feed Generation

Datasette's plugin system allows generating an RSS feed from any query. Install `datasette-atom` plugin:

```bash
pip install datasette-atom
```

Then add a `metadata.yml` configuration:
```yaml
plugins:
  datasette-atom:
    feeds:
      - sql: |
          SELECT
            headline as title,
            date as updated,
            description as content_html,
            source_url as link,
            id
          FROM entries
          WHERE tracker = :tracker AND is_published = 1
          ORDER BY date DESC LIMIT 50
        title: "{tracker} Tracker — Resistance Research"
        link: https://resistance-research.org/tracker/{tracker}
```

This generates `https://your-datasette-instance/feeds/first-amendment.atom` — a valid Atom/RSS feed that partners can subscribe to in any RSS reader.

### 2.3 Filters Available to End Users

The Datasette interface exposes these filters without any custom code:

| Filter | Type | Example |
|--------|------|---------|
| Tracker | Dropdown | `first-amendment` |
| Date range | Date picker | `2026-01-01` to `2026-05-05` |
| Category | Dropdown | `journalist-arrest` |
| Confidence level | Dropdown | `high`, `medium` |
| State | Dropdown or text | `CA`, `federal` |
| Keyword search | Free text | `SPLC`, `consent decree` |
| Sort | Column header click | Date, confidence, state |

### 2.4 Embedding for Partner Websites

Partners can embed a filtered view of the tracker in their own website using an iframe:

```html
<iframe 
  src="https://your-datasette-instance/tracker/entries?tracker=first-amendment&confidence=high&_facet=category"
  width="100%"
  height="600px"
  frameborder="0">
</iframe>
```

This provides a read-only, filterable view of high-confidence First Amendment entries without any data migration required.

### 2.5 Hosted Deployment Options

| Option | Cost | Setup Effort | Best For |
|--------|------|-------------|----------|
| Datasette Cloud | $15–150/month | Zero | Partners who need uptime guarantees |
| DigitalOcean Droplet ($6/mo) | $6/month | 2–3 hours | Current project scale |
| Fly.io free tier | $0 | 1–2 hours | Development / proof of concept |
| Vercel (static export) | $0 | 1 hour | Read-only public access |

Recommendation: Start on Fly.io free tier for testing, migrate to DigitalOcean when ready for institutional partner demos.

---

## 3. Institutional Briefing Format

This is the highest-value distribution format for law schools, advocacy organizations, and legislative staff. It provides analysis, not just data.

### 3.1 One-Page Briefing Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│  FIRST AMENDMENT SUPPRESSION — MONTHLY BRIEFING                    │
│  Resistance Research Project  |  May 2026  |  resistance-research.org │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LEAD FINDING                                                       │
│  Federal prosecution of civil society organizations has escalated   │
│  sharply in April–May 2026. The SPLC indictment (April 21) and the  │
│  FBI investigation of NYT reporter Elizabeth Williamson (May 2026)  │
│  represent a new phase: not just access restriction, but criminal   │
│  process as a suppression tool.                                     │
│                                                                     │
│  KEY STATISTICS (April 2026)                                        │
│  • 47 new entries (vs. 29 in March 2026, +62%)                     │
│  • 23 states affected (vs. 19 in March)                            │
│  • Federal actions: 34 of 47 (72%)                                 │
│  • High-confidence entries: 31 of 47 (66%)                         │
│                                                                     │
│  CASE STUDIES (3 highest-impact entries this month)                │
│                                                                     │
│  1. SPLC Indictment (April 21, 2026)                               │
│     The DOJ grand jury indicted the Southern Poverty Law Center     │
│     on 11 counts of wire fraud and money laundering, stemming       │
│     from its paid informant program. SPLC has operated similar      │
│     programs in coordination with law enforcement for decades.      │
│     [Legal significance] [Recommended action] [Tracking URL]       │
│                                                                     │
│  2. FBI Investigation of NYT Reporter (May 2026)                   │
│     ...                                                             │
│                                                                     │
│  RECOMMENDED ACTIONS                                                │
│  [ ] Law clinics: Monitor SPLC case for amicus opportunities        │
│  [ ] Advocacy: File state shield law requests in uncovered states   │
│  [ ] Legislative: Track Kansas SB 61 model legislation spread      │
│                                                                     │
│  CONTACT FOR COLLABORATION                                          │
│  [contact information]                                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Automated Generation

The briefing is generated from the database on the first Monday of each month:

```python
# monthly_briefing.py — generates institutional briefing as PDF
def generate_monthly_briefing(tracker, month, year):
    # Pull high-confidence entries from target month
    # Pull lead finding from CHECKIN.md (manually written)
    # Pull statistics from database
    # Pull top-3 entries by impact score (confidence + category weight)
    # Render Jinja2 template
    # Convert to PDF via Pandoc
    # Email to partner list via SendGrid
    pass
```

The "recommended actions" section is the one element that requires human authorship — it cannot be automated because it requires legal and strategic judgment. Target: 30 minutes of researcher time per monthly briefing.

---

## 4. Data Export Formats

All export formats are generated from the same database query. The format is selected by URL suffix in Datasette or by command-line argument in the export script.

### 4.1 CSV Export

Standard spreadsheet format. Column headers match the canonical event schema fields. Dates in ISO 8601 format (YYYY-MM-DD). Encoding: UTF-8 with BOM for Excel compatibility.

Sample row:
```
id,tracker,date,headline,category,state,confidence,source_url
a3f2b1c4,first-amendment,2026-04-21,"SPLC indictment — 11 counts wire fraud",civil-society-targeting,federal,high,https://www.justice.gov/opa/pr/splc-indictment
```

Partners who want CSV: journalists building their own analyses, law school researchers using R or Python, advocacy organizations building their own dashboards.

### 4.2 JSON Export

Full event schema including all fields, tags, and source URLs. Useful for programmatic access.

```json
{
  "tracker": "first-amendment",
  "as_of": "2026-05-05",
  "entry_count": 247,
  "entries": [
    {
      "id": "a3f2b1c4",
      "date": "2026-04-21",
      "headline": "SPLC indictment — 11 counts wire fraud",
      "description": "...",
      "category": "civil-society-targeting",
      "state": "federal",
      "confidence": "high",
      "sources": [
        {"name": "DOJ Press Release", "url": "https://..."},
        {"name": "Democracy Now!", "url": "https://..."}
      ],
      "tags": ["SPLC", "DOJ", "civil-society", "wire-fraud", "political-prosecution"]
    }
  ]
}
```

### 4.3 RSS/Atom Feed

Auto-generated by Datasette-Atom plugin. Updates whenever new high-confidence entries are published. Partners subscribe in an RSS reader (Feedly, NewsBlur, self-hosted FreshRSS) and receive an alert within minutes of a new entry.

Feed URL pattern: `https://your-datasette-instance/feeds/{tracker-name}.atom`

### 4.4 iCalendar Feed (.ics)

For entries with specific future dates — court hearing deadlines, comment period closes, consent decree anniversary milestones — an iCalendar feed allows partners to add tracker events directly to Google Calendar or Outlook.

Generated for events with a `deadline_date` field (added manually by reviewers for time-sensitive entries):

```python
from icalendar import Calendar, Event
from datetime import datetime

def generate_ics(tracker):
    cal = Calendar()
    cal.add('prodid', f'-//Resistance Research//{tracker}//EN')
    
    for entry in get_deadline_entries(tracker):
        event = Event()
        event.add('summary', entry['headline'])
        event.add('dtstart', datetime.fromisoformat(entry['deadline_date']))
        event.add('description', entry['description'])
        event.add('url', entry['source_url'])
        cal.add_component(event)
    
    return cal.to_ical()
```

Use cases: Environmental comment period deadlines (Regulations.gov notices), consent decree compliance hearing dates, FISA reauthorization windows.

---

## 5. Visualization Options

The following visualizations are available as embeddable components using Observable Framework (open source, no backend required) or as static charts generated by Python matplotlib/plotly exported to SVG.

### 5.1 Timeline View

Entries displayed chronologically on a scrollable horizontal timeline. Color-coded by category. Click any dot to open the entry detail.

**Implementation**: Observable Plot (free, open source) with the tracker JSON export as the data source. Embed as a static HTML file in GitHub Pages or on the Datasette instance.

```javascript
// Observable Plot timeline
Plot.plot({
  marks: [
    Plot.dot(entries, {
      x: "date", 
      y: "category",
      fill: "category",
      title: "headline",
      r: 4
    })
  ],
  color: {legend: true}
})
```

### 5.2 Geographic Map

Entries plotted by state, with color intensity showing density. States with more entries appear darker. Federal actions plotted separately.

**Implementation**: Observable Plot + US states GeoJSON. Requires joining entry state codes to GeoJSON polygon data. The map updates automatically when the underlying JSON export updates.

**Colorblindness note**: Use a sequential blue palette (not red-green) for density. All states should be distinguishable in grayscale for print.

### 5.3 Category Treemap

Categories displayed as nested rectangles. Rectangle size = entry count. Clicking a category filters the entry list below.

**Implementation**: D3.js treemap layout, driven by the category breakdown query from the database. Static version can be exported as SVG for PDF inclusion.

### 5.4 Trend Line

Weekly entry volume over the last 90 days, with a 4-week rolling average overlay. Useful for identifying escalation periods.

**Implementation**: Observable Plot line chart. Data: SQL query aggregating entries by week.

### 5.5 Word Cloud

Most frequent keywords from entry headlines and descriptions over the last 30 days. Useful for identifying emerging themes not captured by the category taxonomy.

**Implementation**: Python `wordcloud` library. Generate weekly as a PNG and embed in the static dashboard PDF. Exclude stopwords and tracker-specific common terms (e.g., "federal," "court," "DOJ") that appear in every entry.

---

## 6. Accessibility Standards

All dashboard outputs — static PDFs, interactive web interface, embedded charts — must meet WCAG 2.1 Level AA.

### 6.1 Color

- All charts use colorblind-safe palettes. Default: ColorBrewer "Set2" (distinguishable by deuteranopes and protanopes).
- No information conveyed by color alone. Every color-coded element also has a text label, shape, or pattern distinguishing it.
- Minimum contrast ratio for text: 4.5:1 (AA standard). Use WebAIM Contrast Checker to verify.

### 6.2 Chart Accessibility

- Every chart has an `<aria-label>` or `<figcaption>` with a plain-text description of what the chart shows and its key finding.
- Interactive charts are keyboard-navigable (Tab to focus, Enter to select, Arrow keys to navigate data points).
- All charts provide a link to the underlying data table for users who cannot read visual charts.

Example:
```html
<figure>
  <figcaption>
    Bar chart showing category distribution of First Amendment suppression entries. 
    Largest category: press exclusion (38%), followed by journalist arrest (29%), 
    book bans (19%), and anti-protest laws (14%).
  </figcaption>
  <img src="category_chart.svg" alt="Category distribution bar chart">
  <p><a href="/tracker/entries.csv">Download the data (CSV)</a></p>
</figure>
```

### 6.3 Mobile Responsiveness

All HTML dashboards use a single-column layout at viewport widths below 768px. Charts resize using `width: 100%; max-width: 800px`. Touch targets (buttons, links) are at least 44x44px.

Datasette's default CSS is not fully mobile-optimized; install `datasette-css-properties` plugin and override with a mobile-first stylesheet.

### 6.4 Text-Only Summary

Each tracker's weekly update includes a text-only version (plain Markdown, no charts) for partners who receive updates via email and cannot view embedded HTML or PDFs. The text-only version contains all statistics and entry lists from the static dashboard, formatted as a numbered list.

```
FIRST AMENDMENT TRACKER — WEEK OF 2026-04-28

New entries this week: 7
Notable entries:
1. [2026-04-27] 10th Circuit reverses Portland tear gas injunctions (court ruling, protest restriction)
   Source: https://...
2. [2026-04-21] SPLC indictment — 11 counts wire fraud (DOJ press release, civil-society-targeting)
   Source: https://...
[...]
Full tracker: https://your-datasette-instance/tracker/entries?tracker=first-amendment
```

---

*Sources: [Datasette](https://datasette.io/) | [Observable Framework](https://observablehq.com/framework/) | [datasette-atom plugin](https://datasette.io/plugins/datasette-atom) | [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/) | [ColorBrewer](https://colorbrewer2.org/) | [Observable Plot](https://observablehq.com/plot/) | [icalendar Python](https://pypi.org/project/icalendar/)*
