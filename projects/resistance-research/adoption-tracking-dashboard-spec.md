---
title: "Adoption Tracking Dashboard Specification"
date: 2026-05-05
status: production-ready
phase: Phase 1 measurement tooling
distribution_paths: A / A+37 / B (path-independent)
companion_files:
  - post-distribution-impact-measurement.md          # Sector pathways, metrics framework, baselines
  - post-distribution-impact-measurement-framework.md # Attribution methodology, four attribution tests
  - impact-measurement-tools-inventory.md            # Full tools inventory with cost and setup
  - tracking-template.json                           # Structured tracking schema
  - DISTRIBUTION_OUTREACH_CONTACTS.md                # Outreach contact list for scorecard population
scope: "Data source specifications; measurement tools; tracking template; reporting cadence; dashboard structure for visualization"
---

# Adoption Tracking Dashboard — Specification and Implementation Guide

**May 5, 2026 — Phase 1 Execution Prep. Activate on distribution launch.**

This document specifies the tooling architecture, operational templates, reporting cadence, and dashboard visualization structure for measuring institutional adoption of the 35-domain Democratic Renewal Framework across all three distribution paths. It translates the measurement framework from `post-distribution-impact-measurement.md` into concrete instruments: what to build on Day 0, what to track at each milestone, and what the outputs look like at 7 days, 30 days, 90 days, and 180 days.

The system is designed to operate with free or low-cost tools on 2–4 hours of monitoring time per week. All components can run in a spreadsheet or Obsidian database without additional software. Optional paid enhancements are flagged explicitly.

---

## Dashboard Architecture

The adoption tracking system has six components.

| Component | What it measures | Primary tool | Update cadence |
|-----------|-----------------|--------------|---------------|
| 1. Citation Monitor | When and where the framework appears in published work | Google Alerts + CourtListener + Overton | Daily automated; weekly manual review |
| 2. Adoption Scorecard | Who is using it and at what depth | Manual contact log (spreadsheet) | Per event |
| 3. Domain Heat Map | Which domains are generating engagement | Aggregated from citation log | Weekly |
| 4. Failure Mode Detector | Signs of misapplication, decay, or stalled diffusion | Structured audit of citation log | Monthly |
| 5. Network Cascade Tracker | Second- and third-order amplification from bridge nodes | Bridge node contact log | Per event |
| 6. Legislative and Policy Monitor | Bills, regulations, or policies incorporating framework language | LegiScan API + state leg databases | Weekly automated |

---

## Component 1: Citation Monitor

### 1.1 Google News Alerts (Setup time: 15 minutes; Cost: free)

Create at news.google.com/alerts with daily email delivery to a dedicated folder (e.g., `monitoring/google-alerts/`).

**Set A — Framework identity**
- `"democratic renewal proposal"`
- `"35-domain democratic"`
- `"democratic renewal framework" democracy`
- `"domain 37" election interference 2026`

**Set B — Framework-specific coinages**
- `"ICE-at-polls" election`
- `"NVRA quiet period" 2026`
- `"state legislative autocratization"`
- `"appellate capture" judicial independence`
- `"constraint failure" executive democratic`
- `"fiscal authority bypass" OMB`

**Set C — Bridge node citations (second-order adoption detection)**
- `"Brennan Center" "voting rights" "democratic renewal"`
- `"Just Security" "judicial independence" 2026`
- `"Democracy Docket" "voter roll" SAVE 2026`

Configuration: set all alerts to "All results" (not "Best results") and weekly digest format. Note: Google Alerts has known coverage gaps for PDF documents and legal filings — supplement with CourtListener for litigation monitoring.

### 1.2 Google Scholar Alerts (Setup time: 10 minutes; Cost: free)

At scholar.google.com/scholar_alerts, create alerts for:
- `"democratic renewal proposal"`
- `"35-domain" democracy institutional`
- `"domain 6 judicial independence" democratic`
- `"state legislative autocratization" institutional`

Scholar alerts deliver when new academic papers matching the query are indexed. These will be sparse for the first 3–4 months — absence before Month 4 is not a failure signal. Scholar alerts are the primary detection mechanism for the 12–24 month law review adoption window.

### 1.3 CourtListener RECAP Search Alerts (Setup time: 20 minutes; Cost: free, 5 alerts/day on free tier)

At courtlistener.com, create saved searches with email alerts:

**Search 1 — Framework title**
Query: `"democratic renewal proposal"`
Scope: All federal courts

**Search 2 — Domain-specific litigation phrases**
Query: `"ICE at polls" OR "NVRA quiet period" OR "SAVE database" voter roll 2026`
Scope: All federal courts

**Search 3 — Active dockets from litigation tracker**
For each Tier A case in `litigation-tracker-2026.md`, bookmark the CourtListener docket page. Check monthly for new filings. Priority dockets: Wilcox/Slaughter (independent agency removal), any AG-filed SAVE Act litigation, Oregon 9th Circuit voter roll appeal (oral argument May 19, 2026).

**Search 4 — Amicus brief monitoring**
Query: `"amicus" "voting rights" "democratic" 2026`
Scope: Federal district and circuit courts

CourtListener's RECAP alerts function as Google Alerts for federal court filings. A RECAP alert means a document matching search terms has been docketed — download and review for framework language immediately.

### 1.4 Overton.io (Setup time: 30 minutes; Cost: free public tier; institutional access via SAGE partnership)

Register at overton.io. If affiliated with a university library with Overton institutional access, use that login. The free public tier provides limited search access; institutional access provides full 21 million+ document database search with export.

Overton indexes policy documents (government reports, think tank publications, IGO documents, NGO reports) and tracks citations. The indexing lag is 6–18 months, making Overton useful beginning at Month 4.

**Monthly search template (run at Month 4, Month 8, Month 12):**
- Primary search: `"democratic renewal" proposal institutional`
- Secondary search: `"state legislative autocratization" OR "appellate capture" OR "ICE at polls"`
- Filter by document type separately: government, think tank, intergovernmental organization
- Export results to `monitoring/overton-results-[YYYY-MM].csv`

Overton is the only tool that systematically indexes grey literature (think tank reports, NGO publications) for citation patterns. It is not a real-time monitor — it is a lagging indicator tool for confirming what the citation monitor detected months earlier.

### 1.5 LegiScan API (Setup time: 30 minutes for account; Cost: free tier = 30,000 API queries/month)

Register at legiscan.com/legiscan-register.

Create full-text saved searches in priority states (CA, NY, MN, WI, PA, MI, CO, AZ, OH, VA, NC, GA):

**Set A — Domain 1 / 37 election language**
- `"voter roll" purge SAVE 2026`
- `"ICE" polling place election interference`
- `"NVRA" voter removal quiet period`
- `"election security" federal interference`

**Set B — Domain 33 state autocratization language**
- `preemption "local government" ballot initiative restriction`
- `"election administration" override legislature`

**Set C — Domain 6 / 34 institutional authority language**
- `"judicial independence" federal funding`
- `"fiscal authority" executive impoundment`
- `"independent agency" removal president`

Configure daily email notifications for new or amended bills. Log any alert that matches to Component 2 (Adoption Scorecard) under the "Legislative sector" row.

---

## Component 2: Adoption Scorecard

### Schema

Maintain as a Google Sheet or Obsidian database table. One row per organization in the outreach universe (populated from `DISTRIBUTION_OUTREACH_CONTACTS.md`).

| Column | Description | Values |
|--------|-------------|--------|
| Organization | Full institutional name | Text |
| Sector | AG / Law school / Think tank / Litigation org / Advocacy / Media | Category |
| Tier | Outreach priority tier | 1 / 2 / 3 |
| Primary domains | Relevant domain numbers | Domain list (e.g., "1, 37") |
| Outreach date | Date of first contact attempt | YYYY-MM-DD |
| Delivery confirmed | Date of confirmed delivery | YYYY-MM-DD or "Unconfirmed" |
| First response | Date and type of first substantive reply | YYYY-MM-DD / reply type |
| Adoption level | Current depth of engagement (0–4) | Integer |
| Adoption evidence | URL or file path to supporting document | URL or file path |
| Attribution tests passed | Which of the four attribution tests are met (1/2/3/4) | Comma-separated test numbers |
| Tier classification | Tier 1/2/3/4 per `post-distribution-impact-measurement.md` Section 2 | 1 / 2 / 3 / 4 |
| Last update | Date of last status change | YYYY-MM-DD |
| Next action | Required follow-up | Text |
| Notes | Free text | Text |

**Adoption level scale (0–4):**
- 0: No engagement (framework sent; no response)
- 1: Awareness (confirmed receipt; substantive reply; no published output yet)
- 2: Reference (cited or used vocabulary in published work)
- 3: Operational (domain analysis in active casework, testimony, brief, or legislation)
- 4: Coalition (actively introducing framework to other organizations; secondary distribution)

### Pre-Populated Tier 1 Rows

Copy this table as starting point; extend with full contact list from `DISTRIBUTION_OUTREACH_CONTACTS.md`:

| Organization | Sector | Primary domains | Adoption level |
|-------------|--------|----------------|----------------|
| Brennan Center | Think tank | 1, 6, 29 | 0 |
| ACLU | Litigation org | 16, 28, 29 | 0 |
| Democracy Docket | Litigation org | 1, 33, 37 | 0 |
| Protect Democracy | Think tank / litigation | 6, 28, 34 | 0 |
| States United Democracy Center | Advocacy / think tank | 1, 33, 37 | 0 |
| Just Security | Media / think tank | 6, 28, 29 | 0 |
| Harvard Election Law Clinic | Law school | 1, 33, 37 | 0 |
| Ohio State Election Law | Law school | 1, 37 | 0 |
| NAACP LDF | Litigation org | 1, 29, 37 | 0 |
| SPLC | Litigation org | 16, 28, 29 | 0 |
| AFL-CIO | Advocacy / union | 34, 37, 4 | 0 |
| SEIU | Advocacy / union | 4, 37 | 0 |
| National Immigrant Justice Center | Litigation org / advocacy | 16, 28 | 0 |

---

## Component 3: Domain Heat Map

### Structure

Maintain as a separate sheet or table. One row per domain (1–37+). Columns track citation events by month.

| Domain | Domain name (abbreviated) | Month 1 citations | Month 3 citations | Month 6 citations | Month 12 citations | Dominant sector | Status |
|--------|--------------------------|-------------------|-------------------|-------------------|---------------------|-----------------|--------|
| 1 | Voting rights / NVRA | 0 | — | — | — | — | Baseline |
| 6 | Judicial independence | 0 | — | — | — | — | Baseline |
| 16 | Immigration enforcement | 0 | — | — | — | — | Baseline |
| 29 | Prosecutorial independence | 0 | — | — | — | — | Baseline |
| 33 | State legislative authority | 0 | — | — | — | — | Baseline |
| 34 | Fiscal authority | 0 | — | — | — | — | Baseline |
| 37 | Federal election interference | 0 | — | — | — | — | Baseline |
| *(all domains)* | | 0 | — | — | — | — | Baseline |

**Status field values:** Baseline / Active (1+ citation events) / Hot (5+ citation events) / Stalled (active at Month 3; zero events since) / Captured (cited by opposing actors).

**Monthly update protocol:** Aggregate all new citation events from the Citation Monitor (Component 1) into domain rows. Update the dominant sector column (which sector accounts for the most citations for that domain). Flag domains with zero events at Month 3 for targeted outreach.

---

## Component 4: Failure Mode Detector

### Monthly Audit Checklist

Run this checklist on the first Monday of each month. Document findings in `monitoring/failure-mode-log-[YYYY-MM].md`.

**False adoption check (citation without implementation)**
- [ ] For each new Tier 1 citation event: does the citing institution's output use the domain's analytical structure, or only mention the framework in passing?
- [ ] For each institution that cited the framework in Month N: does a search of their Month N+1 and N+2 outputs show continued vocabulary or structural use?
- [ ] Flag: citation events where the citing institution shows no follow-on signal within 8 weeks

**Misinterpretation check**
- [ ] For each new citation event from an organization on the capture risk list: review the citing context
- [ ] Flag: any citation where the context inverts the domain's argument (see Section 4.2 in `post-distribution-impact-measurement.md`)
- [ ] Log: any citation by a federal agency or executive-branch-aligned legal organization

**Partial adoption audit**
- [ ] Count the number of domains with zero citation events as of this review date
- [ ] Flag: any domain that has been zero since Month 3 (requires targeted re-outreach)
- [ ] Flag: if 5 or fewer domains account for 80%+ of total citation events

**Decay detection**
- [ ] For each confirmed Tier 1 or Tier 2 adoption event older than 6 months: has the institution produced any follow-on output in the last 3 months?
- [ ] Flag: any institution with Level 2+ adoption score and no new output in 90 days

**Capture risk review**
- [ ] Review capture risk list (maintained in this document, Section 4.5 of `post-distribution-impact-measurement.md`)
- [ ] Flag: any new citation by an organization added to the capture risk list in the previous month

---

## Component 5: Network Cascade Tracker

### Bridge Node Log

Bridge nodes are institutions whose adoption of the framework triggers secondary adoption across their networks. They are not just adopters — they are amplifiers. The three primary bridge node categories are Tier 1 think tanks (Brennan Center, CAP, Protect Democracy), NAAG-affiliated AG offices, and major journalism outlets (ProPublica, The Atlantic, Democracy Docket's media partnerships).

**Bridge node log schema:**

| Bridge node | Contact date | First engagement | Secondary contact identified | Secondary contact date | Secondary output date | Cascade depth |
|-------------|-------------|-----------------|-----------------------------|-----------------------|----------------------|---------------|
| Brennan Center | — | — | — | — | — | 0 |
| California AG | — | — | — | — | — | 0 |
| ProPublica | — | — | — | — | — | 0 |
| *(expand from contact list)* | | | | | | |

**Cascade depth definition:**
- Depth 0: Received framework, no output
- Depth 1: Published output using framework analysis
- Depth 2: Their output was cited by another institution (detected through citation monitor)
- Depth 3+: Third-order citation chain established

A Depth 2 event is the first evidence of autonomous diffusion — the framework spreading through citation chains without direct outreach. Log every Depth 2+ event as a Priority Signal.

---

## Component 6: Legislative and Policy Monitor

### State Legislative Database Coverage

**Primary tool:** LegiScan API (free tier sufficient; alerts configured in Component 1.5 above)

**Secondary tool:** Voting Rights Lab Election Policy Tracker (tracker.votingrightslab.org) — tracks voting legislation in all 50 states; free access; updated continuously.

**Tertiary tool:** Brennan Center State Voting Laws Roundup (brennancenter.org/series/state-voting-laws-roundups) — monthly roundup of voting legislation; useful for confirming legislative adoption signals detected through LegiScan.

**Federal legislative monitoring:** Congress.gov bill search (congress.gov/search) — full text of all introduced legislation. Search terms: same as LegiScan Set A-C above. Free; no account required.

**Update cadence:** Weekly automated alerts via LegiScan; monthly manual review of Voting Rights Lab and Brennan Center roundups.

---

## Tracking Template: Daily, Weekly, Monthly Protocols

### Day 7 Snapshot (First Week Check-In)

Date: Day 7 from distribution launch.
Purpose: Confirm monitoring infrastructure operational; capture any fast-mover signals.

| Check | Action | Tool |
|-------|--------|------|
| Google Alerts active | Confirm delivery to dedicated folder | Gmail / Alerts dashboard |
| Scholar Alerts active | Confirm at least one test alert received | Scholar Alerts dashboard |
| CourtListener alerts active | Confirm saved searches created | CourtListener account |
| Scorecard populated | Confirm all Tier 1 contacts in scorecard | Spreadsheet |
| Day 7 citation count | Count any new citations from alert inbox | Tally from folder |
| Day 7 network activity | Any bridge node contact responses? | Scorecard |

**Day 7 expected results:** Zero to two citation events (fast-mover think tanks or journalists). Any AG response within Day 7 is a strong signal. Document any contacts made, responses received, or distribution confirmations.

---

### Month 1 Snapshot

Date: 30 days from distribution launch.
Purpose: First meaningful adoption signal assessment.

**Quantitative counts:**
- Total citation events (all sectors combined)
- Unique institutions citing the framework
- Unique domains cited
- Tier 1 adoption events (explicit citation + structural use)
- Tier 2 adoption events (vocabulary convergence, no citation)
- AG responses (any sector: reply, material request, meeting)
- Think tank outputs using framework language
- Journalist mentions

**Qualitative assessment:**
- Which bridge nodes have engaged substantively?
- Any early misinterpretation signals?
- Which domains are generating engagement vs. silence?

**Decision trigger:** Zero Tier 1 or Tier 2 events at Month 1 does not indicate failure — academic and AG adoption is invisible for the first 4–8 weeks. The correct Month 1 failure signal is: zero responses from all Tier 1 think tank contacts AND zero responses from all Tier 1 AG contacts. If both are true, investigate distribution delivery (emails going to spam, Gist link broken) before redesigning strategy.

---

### Month 3 Snapshot

Date: 90 days from distribution launch.
Purpose: First substantive assessment of adoption trajectory.

**Required reviews:**
1. Citation monitor audit — export all alerts received since launch; categorize by sector, domain, and tier
2. Vocabulary sweep — run Google News search for each coinage on the framework vocabulary list; export results; compare against pre-distribution baseline
3. Overton search — first Overton search run (may return zero results; document baseline query results for later comparison)
4. Domain heat map update — populate Month 3 column; flag domains with zero events
5. Failure mode audit — run Component 4 monthly checklist
6. Scorecard update — update adoption levels for all Tier 1 and Tier 2 contacts

**Quantitative targets at Month 3:**
- Minimum meaningful adoption: 5+ unique citation events across 2+ sectors
- Expected think tank adoption: 1–3 Tier 2 events from Brennan Center / CAP / Protect Democracy
- Expected litigation adoption: 0–2 events (filing lags mean Month 3 is early for court documents)
- Expected journalism adoption: 3–8 article mentions from journalists in the Tier 1 network

**Month 3 decision framework:**
- Zero events in all sectors: Distribution failure, not framework failure. Investigate delivery. Run secondary distribution push.
- Events in journalism only: Think tanks and AGs not yet engaged. Run targeted secondary outreach with domain-specific framing.
- Events in think tanks + journalism: Normal trajectory. Continue monitoring; escalate direct outreach to AG contacts.

---

### Month 6 Snapshot

Date: 180 days from distribution launch.
Purpose: First full institutional cycle assessment; litigation impact evaluation.

**Required reviews:**
1. Full sector assessment — complete adoption scorecard review for all Tier 1 and Tier 2 contacts
2. Litigation impact review — CourtListener search for all amicus briefs and new filings in framework domain areas; compare vocabulary against pre-distribution baseline
3. Structural convergence review — compare legislation introduced in priority states against Domain 1, 33, 34, and 37 recommendations
4. Failure mode audit — full Component 4 checklist plus six-month decay review
5. Overton search — second Overton query; compare against Month 3 results
6. Pre-post baseline comparison — run same searches used to establish pre-distribution baselines; compute delta

**Quantitative targets at Month 6:**
- Minimum institutional adoption: 3+ confirmed Tier 1 or Tier 2 events across 3+ sectors
- AG adoption: at least 1 confirmed Tier 2 or Tier 3 event (vocabulary convergence in a filing or coalition letter)
- Think tank adoption: at least 2 confirmed Tier 1 or Tier 2 events
- Journalism: at least 1 investigative piece (500+ words) using domain framing as organizing structure

**Month 6 decision framework:**
- Strong adoption (40%+ of Tier 1 contacts at Level 2+): Proceed to Phase 2 domain expansion approval. Begin domain maintenance cycle (update domains with highest citation volume first).
- Moderate adoption (10–39% of Tier 1 contacts at Level 2+): Continue current strategy; deepen engagement with adopting institutions; run targeted outreach to lagging sectors.
- Weak adoption (<10% of Tier 1 contacts at Level 2+): Reassess distribution channel before content. Run a one-on-one briefing with the three highest-leverage Tier 1 contacts who have not yet engaged. Diagnose: messaging barrier, channel problem, or timing issue.

---

## Reporting Cadence Summary

| Report | Date | Audience | Format | File |
|--------|------|----------|--------|------|
| Day 7 operational check | Day 7 | Internal | Checklist | `monitoring/day7-check.md` |
| Month 1 snapshot | Day 30 | Internal | Quantitative summary + qualitative notes | `monitoring/month1-snapshot.md` |
| Month 3 assessment | Day 90 | Internal + potential bridge node briefing | Full report | `monitoring/month3-assessment.md` |
| Month 6 evaluation | Day 180 | Internal + potential funder/partner briefing | Full evaluation with visualizations | `monitoring/month6-evaluation.md` |
| Month 12 impact report | Day 365 | Public-facing if adoption is strong | Comprehensive impact report | `monitoring/month12-impact-report.md` |

---

## Dashboard Visualization Structure (Google Sheets / Tableau)

### Sheet 1: Summary Dashboard

**Five KPI cells (top row, large font):**
1. Total citation events (all time)
2. Unique institutions engaged (Adoption Level 1+)
3. Unique institutions adopted (Adoption Level 2+)
4. Domains with at least 1 citation event (of 37 total)
5. Network cascade depth (maximum depth achieved)

**Charts (below KPI row):**
- Bar chart: Citation events by sector (AGs / Law schools / Think tanks / Litigation orgs / Advocacy / Media / Other)
- Bar chart: Citation events by domain (sorted by count, descending)
- Line chart: Cumulative citation events over time (Day 0 to current)
- Heatmap table: Domains × Months (cells colored by citation volume — white=0, light=1-2, medium=3-5, dark=6+)

### Sheet 2: Adoption Scorecard

Full contact database with all columns from Component 2 above. Add conditional formatting: rows where Adoption Level = 0 are gray; Level 1 = yellow; Level 2 = orange; Level 3 = green; Level 4 = dark green.

### Sheet 3: Failure Mode Log

One row per failure mode event detected. Columns: date detected, failure mode type (false adoption / misinterpretation / partial bias / capture / decay), institution, domain, evidence, response taken, resolution.

### Sheet 4: Legislative Monitor

One row per matching bill or regulatory filing. Columns: jurisdiction, bill number, title, domain match, date introduced, status, vocabulary evidence, link.

### Sheet 5: Baseline Comparison

Side-by-side table: pre-distribution baseline count (from Section 5 of `post-distribution-impact-measurement.md`) and current count for each baseline metric. Delta column auto-calculated. Updated at Month 6 and Month 12.

---

*Sources: [CourtListener / RECAP Suite — Free Law Project](https://free.law/recap/) | [Overton impact tracking](https://www.overton.io/policy-impact) | [LegiScan](https://legiscan.com/legiscan-register) | [Voting Rights Lab Election Policy Tracker](https://tracker.votingrightslab.org/) | [Democracy Docket](https://www.democracydocket.com/cases/) | [Brennan Center State Voting Laws Roundups](https://www.brennancenter.org/series/state-voting-laws-roundups) | [Google Scholar Alerts](https://scholar.google.com/scholar_alerts) | [Congress.gov](https://congress.gov/search)*
