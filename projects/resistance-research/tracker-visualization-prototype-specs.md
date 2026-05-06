---
title: "Tracker Visualization Prototype Specifications"
subtitle: "UI mockups, JSON schema, embedding options, and accessibility standards for four civil liberties trackers"
date: 2026-05-06
status: complete
phase: phase-2-preparation
project: resistance-research
purpose: Phase 2 enrichment strategy — post-Phase-1-launch implementation
cross_references:
  - tracker-source-audit-detailed.md
  - tracker-automation-feasibility.md
  - tracker-measurement-framework.md
---

# Tracker Visualization Prototype Specifications

*Created: May 6, 2026. This document specifies visualization designs for each tracker as static mockups (Figma/Excalidraw descriptions) without code. The data format specifications are sufficient for a developer to implement; the embedding options cover the solo operator's realistic deployment scenarios; accessibility standards are specific and actionable.*

**Design principle**: Every visualization here must work without a backend server — either as a static export (PDF, SVG, HTML generated from CSV) or as a Datasette instance that can run locally or on a $6/month VPS. No React apps, no D3.js custom builds, no maintenance-intensive interactive tools. The goal is institutional-grade visual output that a solo operator can deploy and keep current.

---

## 1. First Amendment Suppression Tracker

### 1.1 Primary Visualization: Event Timeline

**Type**: Horizontal timeline with event categories shown as color-coded vertical marks.

**Canvas description** (for Figma/Excalidraw implementation):

The timeline occupies the full width of the visualization area. The x-axis represents time (left = earliest entry, right = most recent). The y-axis is not numerical — it shows event category lanes.

```
CATEGORY LANES (top to bottom):
─────────────────────────────────────────────────────────────────────
 Press crackdowns     ●────────●────●──────────────●────●───────────
─────────────────────────────────────────────────────────────────────
 Anti-protest laws       ●──────────────●──────●───────────────●────
─────────────────────────────────────────────────────────────────────
 Deplatforming/censure         ●─────────────────────●──────────────
─────────────────────────────────────────────────────────────────────
 SLAPP suits            ●───────────────●───────────────────────────
─────────────────────────────────────────────────────────────────────
 Court rulings        ●──────────────────────●────────●─────────────
─────────────────────────────────────────────────────────────────────
 Civil society prose.                                     ●──────────
─────────────────────────────────────────────────────────────────────

[2025 Q1] [2025 Q2] [2025 Q3] [2025 Q4] [2026 Q1] [2026 Q2]
```

Each circle (●) is a click/hover target: hovering surfaces a tooltip with event name, date, actor, and outcome. Filled circles = event finalized or ruling issued. Hollow circles = pending or ongoing.

**Color palette** (colorblind-safe; see Section 4 on accessibility):
- Press crackdowns: #0077BB (blue)
- Anti-protest laws: #EE7733 (orange)
- Deplatforming/censure: #CC3311 (red)
- SLAPP suits: #009988 (teal)
- Court rulings: #33BBEE (cyan)
- Civil society prosecution: #AA3377 (magenta)

**Legend**: Horizontal color-coded legend bar directly above the timeline.

**Responsive behavior**: On mobile (screen width < 768px), collapse to single-column card list sorted by date descending, with category color coded.

### 1.2 Secondary Visualization: Trend Chart

**Type**: Bar chart, event count per month, stacked by category.

**Canvas description**:

```
Monthly event count — First Amendment suppression tracker
30 ┤
25 ┤            ████
20 ┤       ████ ████ ████
15 ┤  ████ ████ ████ ████ ████
10 ┤  ████ ████ ████ ████ ████ ████
 5 ┤  ████ ████ ████ ████ ████ ████
 0 └─────────────────────────────────────
    Jan   Feb   Mar   Apr   May   Jun
         2026

    ■ Press  ■ Anti-protest  ■ Deplatforming  ■ SLAPP  ■ Rulings  ■ Civil soc.
```

Each bar is stacked by category using the same color palette as the timeline. Hovering a segment shows the category count for that month.

**Design intent**: This chart answers "are restrictions accelerating?" — the question institutional partners are most likely to ask when using the tracker. An upward trend in any category is the most important pattern signal.

### 1.3 Tertiary Visualization: Category Breakdown Pie / Donut

**Type**: Donut chart showing category distribution for a selectable time window (30 days, 90 days, all time).

**Canvas description**:

```
Category distribution — last 90 days

        Press crackdowns (32%)
      ╔══════════╗
     ╔╝          ╚╗   ← Anti-protest (24%)
    ╔╝   47 events╚╗
    ║     (90 days) ║  ← SLAPP suits (18%)
    ╚╗             ╔╝
     ╚╗           ╔╝   ← Court rulings (14%)
      ╚═══════════╝
                        ← Civil soc. prosecution (8%)
                        ← Other (4%)
```

**Selection control**: Three radio buttons or a dropdown: "Last 30 days | Last 90 days | All time." This makes the chart useful for both current-events reporting (last 30 days) and longitudinal pattern analysis (all time).

---

## 2. Environmental Rollbacks Tracker

### 2.1 Primary Visualization: Parallel Timeline

**Type**: Three parallel horizontal timelines showing the regulatory lifecycle for each tracked rule: (A) rule originally enacted / baseline, (B) rollback finalized, (C) litigation status.

**Canvas description**:

```
Environmental Rollbacks — Regulatory Lifecycle View

Rule Name              │ [Original rule] → [Rollback proposed] → [Rollback final] → [Litigation status]
─────────────────────────────────────────────────────────────────────────────────────────────────────
Endangerment Finding   │ [Dec 2009 ●]────────────────[Aug 2025 ◐]───[Feb 2026 ●]──[DC Cir. PENDING ◻]
MATS Rule (2024 amend.)│ [May 2024 ●]────────────────[Jun 2025 ◐]───[Feb 2026 ●]──[DC Cir. PENDING ◻]
PM2.5 NAAQS            │ [Feb 2024 ●]────────────────[Jul 2025 ◐]───[Mar 2026 ●]──[DC Cir. PENDING ◻]
WOTUS Clean Water Rule │ [Jan 2023 ●]────────────────[Apr 2025 ◐]───[Sep 2025 ●]──[STAYED ▲]
Vehicle GHG Standards  │ [Apr 2021 ●]────────────────[Aug 2025 ◐]───[Feb 2026 ●]──[DC Cir. PENDING ◻]
```

Symbol key:
- ● Finalized / effective
- ◐ Proposed / notice-and-comment
- ◻ Pending court action
- ▲ Stayed by court (rule not in effect pending litigation)
- ✗ Litigation failed (rollback upheld)
- ✓ Litigation succeeded (rollback blocked)

**Color coding**:
- Timeline track: Blue for original rule (protective), Red for rollback actions, Gray for litigation pending, Green for litigation success (rollback blocked), Dark orange for litigation failure (rollback upheld)

**Critical design note**: The parallel timeline makes the litigation outcome visually scannable. Institutional partners (law school clinics, advocacy organizations) can immediately identify which rollbacks are still contested vs. which are legally settled. This is the most decision-relevant visualization for the target audience.

### 2.2 Secondary Visualization: Geographic Impact Map

**Type**: US state map, chloropleth shading by count of EPA rollbacks affecting that state based on documented geographic scope of affected rules.

**Canvas description**:

```
States most affected by EPA rollbacks — by rule count

  [WA][ ][MT][ND]
  [ ][ID][WY][SD][MN][WI][MI][ ][ ]
  [OR][  ][CO][NE][IA][IL][IN][OH][PA][NY][CT]
  [CA][NV][UT][KS][MO][KY][WV][VA][MD][DE][NJ]
  [  ][AZ][NM][OK][AR][TN][NC][SC][  ][ ][  ]
  [  ][  ][TX][LA][MS][AL][GA][FL][  ]

  Color scale:
  ░░ 1–3 rules  ▒▒ 4–7 rules  ▓▓ 8–12 rules  ██ 13+ rules
```

States with large industrial emissions inventories (Texas, Pennsylvania, West Virginia, Ohio) will show the highest rule impact counts because air and water rules affect industrial facilities concentrated in those states.

**Data source for this visualization**: Each tracker entry already contains "states affected" in the real-world impact section. For map generation, extract state names from entry text (this can be partially automated with NLP entity extraction or manually maintained).

### 2.3 Tertiary Visualization: Financial Impact Trend

**Type**: Bar chart showing health/economic cost estimates from regulatory rollbacks, by year.

**Data**: Each tracker entry documents projected health costs (premature deaths, asthma attacks) and regulatory burden changes. Aggregating these into an annual estimate produces a "cost to public health per year" metric.

```
Projected health cost of 2025–2026 rollbacks (CATF / NRDC estimates)

$B/year │
  25 ┤                                    ████
  20 ┤                         ████       ████
  15 ┤              ████       ████       ████
  10 ┤   ████       ████       ████       ████
   5 ┤   ████       ████       ████       ████
   0 └──────────────────────────────────────────
       Pre-MATS  Pre-PM2.5  Post-EF    Post-Vehicle
       rollback  rollback   rollback   std rollback
       (2025)    (2025)     (2026)     (2026)

  Source: Clean Air Task Force health impact modeling
  Note: These are estimates; litigation may restore some standards
```

**Caveats to display prominently**: Advocacy organization estimates (CATF, NRDC) are the primary source; independent academic modeling would increase credibility. The chart should display "ESTIMATED COSTS" in the header, not absolute figures, to avoid overstating certainty.

---

## 3. Police Brutality / Consent Decree Tracker

### 3.1 Primary Visualization: Geographic Heatmap

**Type**: US state map with bubble overlays on city locations. Each bubble = one consent decree or settlement. Bubble size = settlement dollar amount or number of decree provisions. Bubble color = compliance status.

**Canvas description**:

```
Active police consent decrees and oversight status — May 2026

     [Seattle ●]         [Chicago ●]  [Baltimore ●]
                                       [Minneapolis ●]
                                       [Louisville ✕]
  [Los Angeles ●]                     [Newark ●]
                                       [Cleveland ●]
                    [Denver ●]

  ● Active decree, monitoring ongoing (compliance %)
  ✕ Decree dismissed (May 21 2025 withdrawal)
  ◐ State-level substitute oversight (no federal decree)
  ○ Investigation closed, no decree (DOJ withdrawal)

  Bubble size = number of consent decree provisions (larger = more comprehensive reform required)
  Color intensity = compliance percentage (darker = higher compliance)
```

**Tooltip content on hover**: City name, decree date, monitoring entity, current compliance percentage (where available), date of last monitoring report.

**Legend**: Bottom-right corner. Symbol legend + compliance color scale.

### 3.2 Secondary Visualization: Compliance Timeline

**Type**: Multi-line chart showing compliance percentage over time for each tracked city.

**Canvas description**:

```
Consent decree compliance — tracked cities over time

100%│
 80%│                                    ─────── Newark (est. ~95%)
 60%│
 40%│                               ─────────── Seattle (~65%)
 25%│ ─────────────────────────────────────── Chicago (25% after 7 years)
 20%│
  0%│─────────────────────────────────────────────────────────────────
    2019    2020    2021    2022    2023    2024    2025    2026

    Legend: ─── Chicago  ─── Seattle  ─── Baltimore  ─── Newark
    Source: Independent monitor reports, Chicago AG consent decree monitoring team
    Note: Minneapolis and Louisville decrees were dismissed May 21, 2025
```

**Design intent**: The Chicago line — flat near 25% for seven years — is the most important data point. It makes the "consent decrees require enforcement teeth" argument visually immediate.

### 3.3 Tertiary Visualization: Settlement Amount Trend

**Type**: Bar chart of police misconduct settlement payments by city, by year.

**Data source**: ProPublica Injustice on Your Block database (quarterly updates).

```
Police misconduct settlement payouts — selected cities (2022–2025)

$M/year│
  200 ┤   ████
  150 ┤   ████ ████
  100 ┤   ████ ████ ████
   50 ┤   ████ ████ ████ ████
    0 └─────────────────────────────────────────────
        Chicago  LAPD    NYC    Baltimore  Others

  Source: ProPublica Injustice on Your Block database
  Interpretation: High settlement costs while consent decree compliance remains low
                  indicates structural, not occasional, misconduct
```

**Critical editorial annotation**: Include a text box on this chart noting that "settlement costs are paid by taxpayers, not officers or the departments themselves — the financial accountability is misaligned from the behavioral accountability required by consent decrees."

---

## 4. Prosecutorial Weaponization Tracker

### 4.1 Primary Visualization: Network Graph

**Type**: Force-directed network graph showing relationships between prosecutors, defendants, and documented targeting patterns.

**Canvas description** (for Excalidraw implementation):

Nodes: Three types. Prosecutor nodes (squares): named officials (Kash Patel, Todd Blanche, specific USAOs). Defendant nodes (circles): named organizations and individuals. Pattern nodes (diamonds): documented targeting categories (progressive nonprofits, Democratic officials, journalists, protest organizers).

Edges: Prosecutor → Defendant (thick red line = active prosecution, thin orange = investigation, dashed gray = closed). Defendant → Pattern (categorization links showing which pattern category each defendant fits).

```
                     [Kash Patel ■]─────────────────────────────
                           │                                     │
                    [Todd Blanche ■]                             │
                           │                                     ▼
              ┌────────────┼──────────────┐           [Civil rights NPO ◆]
              │            │              │                      │
              ▼            ▼              ▼                      │
          [SPLC ●]    [NAACP ○]    [Dem. officials ●]            │
              │                          │            [Press freedom ◆]
              └──────────────────────────┘                       │
                           │                                     │
                           ▼                                  [RCFP ●]
              [Pattern: anti-civil-society ◆]

  ■ Prosecutor/official   ● Named defendant (active)
  ○ Under investigation   ◆ Pattern category
  ─── Active prosecution  ─ ─ Investigation/closed
```

**Design note**: Network graphs are the most cognitively demanding visualization type. This graph is justified here because the pattern structure (same officials, similar legal theories, similar target categories) is exactly what a network graph reveals that a timeline cannot. The SPLC case only becomes legible as weaponization when it's visually connected to 21 other cases with the same structural elements.

**Implementation tool**: Gephi (free, desktop, exports to SVG) for initial static version. Observable Plot (JavaScript, free, embeddable) for interactive version. For the solo-operator Phase 2 context, Gephi export + PDF is the realistic first version.

### 4.2 Secondary Visualization: Case Timeline with Outcome Distribution

**Type**: Horizontal case timeline (similar to First Amendment tracker) with outcome status shown via symbol.

**Canvas description**:

```
Documented prosecutorial weaponization cases — 2025–2026

Case type     │ [Pending/active cases] ────────────────────────────────►
──────────────┼───────────────────────────────────────────────────────────
Civil society │ ●─────────────────────────────────────────────●─────────
Democratic    │    ●──────●─────────────────────────────●────────────────
  officials   │
Press freedom │         ●──────────────●──────────────────────────────
Protest       │              ●────────────────────●──────────────────────
  suppression │
──────────────┼───────────────────────────────────────────────────────────
              [2025 Q1]   [2025 Q2]   [2025 Q3]   [2025 Q4]   [2026 Q1]

  ● Active prosecution    ◻ Charges dismissed    ✓ Acquittal    ✗ Conviction
```

### 4.3 Outcome Distribution Chart

**Type**: Horizontal bar chart showing case outcomes to date.

```
Prosecutorial weaponization cases — outcome status (May 2026)

Pending prosecution     ████████████████████████████ 18 cases
Charges dismissed              ███ 2 cases
Judicial finding               ██ 1 case (Nashville)
  (vindictive prosecution)
Plea / settlement              █ 1 case
Acquittal                      □ 0 cases
Conviction                     □ 0 cases

Total documented cases: 22
Note: Most cases are recent (2025–2026); most have not reached trial.
```

---

## 5. Data Format Specifications — JSON Schema

Every entry across all four trackers must conform to a common base schema to enable visualization, cross-tracker search, and automated validation. Tracker-specific fields are added at the entry level.

### 5.1 Common Base Schema

```json
{
  "id": "fa-2026-001",
  "tracker": "first_amendment | environmental | police_brutality | prosecutorial",
  "title": "Short descriptive title (max 100 chars)",
  "date_of_event": "2026-01-14",
  "date_entered": "2026-01-16",
  "date_last_updated": "2026-04-09",
  "category": "[tracker-specific category value]",
  "actors": {
    "government_actor": "FBI",
    "target": "Hannah Natanson / Washington Post",
    "jurisdiction": "federal | state | local",
    "state": "DC"
  },
  "outcome": {
    "status": "pending | resolved | appealed | dismissed",
    "summary": "Court-supervised privilege review ordered Feb 24"
  },
  "sources": [
    {
      "outlet": "Washington Post",
      "url": "https://www.washingtonpost.com/national-security/2026/04/09/...",
      "date": "2026-04-09",
      "type": "news | court_filing | government | academic | advocacy"
    }
  ],
  "confidence": "high | medium | low",
  "geographic_scope": ["national", "DC", "MD", "VA"],
  "cross_references": ["fa-2026-002", "lt-2026-045"]
}
```

### 5.2 Tracker-Specific Extension Fields

**First Amendment entries** — additional fields:
```json
{
  "first_amendment_category": "press_freedom | anti_protest | deplatforming | slapp | civil_society_prosecution",
  "legal_basis_claimed": "national security | public safety | fraud | other",
  "litigation_docket": "1:26-cv-00XXX",
  "court_level": "district | circuit | supreme_court"
}
```

**Environmental rollback entries** — additional fields:
```json
{
  "rollback_category": "final_rule | proposed_rule | guidance | enforcement_gap",
  "original_rule_date": "2009-12-15",
  "original_rule_citation": "74 FR 66496",
  "rollback_effective_date": "2026-04-20",
  "health_impact_estimate": {
    "premature_deaths_per_year": 30000,
    "source": "Clean Air Task Force, 2026",
    "confidence": "medium"
  },
  "litigation_status": "pending | stayed | upheld | blocked",
  "litigation_docket": "DC Circuit 26-1021"
}
```

**Police brutality entries** — additional fields:
```json
{
  "entry_type": "consent_decree | settlement | shooting_incident | systemic_pattern",
  "city": "Chicago",
  "police_department": "CPD",
  "decree_date": "2019-01-31",
  "monitoring_entity": "Illinois AG / Judge Pallmeyer",
  "compliance_percentage": 25,
  "compliance_date": "2026-04",
  "settlement_amount_usd": null,
  "decree_provisions_total": null,
  "decree_provisions_compliant": null
}
```

**Prosecutorial weaponization entries** — additional fields:
```json
{
  "prosecution_category": "civil_society | democratic_officials | journalists | protesters | former_officials",
  "charging_official": "USAO SD Alabama",
  "charges": ["wire_fraud", "false_statements", "money_laundering"],
  "legal_theory_assessment": "defective_multiple_counts | novel_weak | facially_valid_but_targeted",
  "vindictive_prosecution_motion_filed": false,
  "pattern_test_score": {
    "pre_identified_as_opposition": true,
    "legal_theory_precedent": false,
    "pattern_of_similar_actions": true
  }
}
```

### 5.3 Schema Validation Rules

Every entry must pass these validation checks before publication:

1. `date_of_event` must be in ISO 8601 format (YYYY-MM-DD)
2. At least one `sources` entry must have `type: "court_filing"` or `type: "government"` (tracker is a factual record, not a media monitor)
3. `confidence` field must be set; no entry defaults to "high" without at least two independent sources
4. `outcome.status` must be current as of `date_last_updated`
5. All source URLs must have been verified live within 30 days of `date_last_updated`

---

## 6. Embedding Options

### 6.1 Institutional Briefing PDF (Monthly Export)

**Use case**: Law school clinics, advocacy organizations, congressional offices, and journalists who need a printable one-page overview of each tracker's current state.

**Production method**: Python script using Jinja2 templates + WeasyPrint (or Pandoc) converts tracker database to PDF. No manual formatting required after initial template setup.

**Layout**: One page per tracker. Header with tracker name, update date, and key statistics. Main body: 5–7 most recent significant entries with abbreviated text. Footer: source list, project URL, contact.

**Update cadence**: Monthly automated generation. Weekly for high-activity periods.

**Distribution**: Email attachment to institutional partners. GitHub releases for public access.

### 6.2 Datasette Interactive Web Interface

**Use case**: Journalists, researchers, and sophisticated users who want to filter, search, and export tracker data.

**Implementation**: Datasette renders the SQLite tracker database as a browsable, filterable, searchable web interface with automatic CSV/JSON export. Zero custom frontend code required.

- Column filters: allows user to filter by tracker, category, state, outcome status, date range
- Full-text search: searches all entry text, title, and source outlet names
- CSV export: one-click download of filtered results
- JSON API: automatic at `/tracker.json` endpoint for programmatic access

**Hosting option A** (free): GitHub Pages + Datasette Lite (WebAssembly version runs entirely in browser, no server required). Limitations: slower for large datasets; no server-side logging.

**Hosting option B** ($6–12/month): DigitalOcean or Render VPS running Datasette. Faster, supports server-side logging, analytics.

**Embed code** (for partner websites):
```html
<iframe
  src="https://[your-datasette-url]/tracker/entries?_facet=tracker&_facet=category"
  width="100%"
  height="600"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>
```

### 6.3 Static Blog/Substack Embed

**Use case**: Weekly summary posts on Substack or blog, with the current tracker statistics embedded inline.

**Method**: Python script generates a Markdown snippet (or HTML table) with the week's tracker statistics — new entries count, active cases, recent rulings. This snippet is copy-pasted into Substack or blog posts. No dynamic embedding needed; Substack does not support iframes.

**Example output snippet**:

```
[TRACKER UPDATE — Week of May 5, 2026]

First Amendment: 3 new entries (journalist indictment, state press shield law
challenge, SLAPP suit filing). Active cases: 47. Courts pending: 12.

Environmental: 2 new final rules (vehicle GHG standards effective; WOTUS
comment period closed). Litigation pending: 18 challenges in DC Circuit.

Police Brutality: 1 new monitor report (Chicago at 25% after 7 years).
Active decrees: 6. Cities without federal oversight after May 21 withdrawal: 8.

Prosecutorial: 1 new case (SPLC arraignment confirmed). Active cases: 22.
Judicial findings of vindictive prosecution: 1 (Nashville).
```

### 6.4 Nightly PDF for Partner Distribution

**Use case**: Partners who cannot receive dynamic web content (government officials, some academic institutions) but need current tracker data.

**Production method**: GitHub Actions workflow runs nightly at 11 PM ET. If any tracker was updated that day, workflow runs the PDF generation script and emails the updated PDF to the partner distribution list via SendGrid or Mailgun (both have free tiers covering 100 emails/day).

**Cost**: $0 within free tiers. If partner list exceeds 100 recipients, SendGrid's basic plan ($20/month) covers 50,000 emails.

---

## 7. Accessibility Specifications

### 7.1 Color-Blind Safe Palettes

All visualizations use the Paul Tol colorblind-safe palette. The category colors specified in Section 1.1 are verified against the three most common color vision deficiencies: protanopia (red-blind), deuteranopia (green-blind), and tritanopia (blue-blind).

**Tol's qualitative palette** (confirmed safe for all three variants):
- #0077BB — blue
- #33BBEE — cyan
- #009988 — teal
- #EE7733 — orange
- #CC3311 — red
- #EE3377 — magenta/pink
- #BBBBBB — gray

**Never use red/green combinations** for status indicators. Use filled/hollow/striped patterns in addition to color for any status distinction (pending/active/resolved). The outcome symbols used in the timeline mockups (●, ◐, ◻, ▲, ✓, ✗) work without color.

### 7.2 Keyboard Navigation

All interactive elements (hover tooltips, filter dropdowns, date range selectors) must be reachable via Tab key and activated via Enter or Space. Focus indicators must be visible (minimum 2px outline in high-contrast color).

Datasette's default implementation is keyboard-navigable. For any custom elements added to the Datasette interface, the WCAG 2.1 AA keyboard navigation standard applies.

### 7.3 Screen Reader Compatibility

**Tables**: All data tables must have `<caption>` elements and appropriate `<th scope="col/row">` attributes. The Datasette interface generates accessible table markup automatically.

**Charts and maps**: Every visualization must have:
1. An `<alt>` text description (maximum 150 characters) summarizing the key finding
2. A `<figure>` with `<figcaption>` providing full data in text form
3. For maps: a linked table version of the same data

Example alt text: "Line chart showing Chicago CPD consent decree compliance at 25% after seven years, with other cities at 65% (Seattle) and 95% (Newark)."

**PDF exports**: Use PDF/UA (Universal Accessibility) standard. WeasyPrint and Pandoc both support tagged PDF output. Ensure reading order matches visual order; avoid text in images.

### 7.4 Mobile Responsiveness

The Datasette interface is responsive by default. For static exports:

- Minimum tap target size: 44×44 pixels (WCAG 2.1 AA)
- Timeline visualizations collapse to vertical card list below 768px screen width
- Map visualizations: provide a table fallback below 480px
- PDF exports: designed for US Letter (8.5×11") but must be readable at 100% zoom on a 375px mobile screen (iPhone SE width)

### 7.5 Language and Readability

All tracker text should target a Flesch-Kincaid Grade Level of 12–14 (readable by most college-educated users but not simplified for general audiences; the tracker's institutional audience is lawyers, advocates, and journalists).

Legal terminology should be defined on first use within each visualization context (a PDF briefing may arrive without the full tracker context).

---

*Sources: [Datasette documentation](https://datasette.io/) | [Datasette Lite (WebAssembly)](https://lite.datasette.io/) | [Paul Tol colorblind-safe palettes](https://personal.sron.nl/~pault/) | [WCAG 2.1 accessibility guidelines](https://www.w3.org/TR/WCAG21/) | [WeasyPrint PDF generation](https://weasyprint.org/) | [Gephi network visualization](https://gephi.org/)*
