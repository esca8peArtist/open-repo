---
title: "Tracker Automation Feasibility Matrix"
subtitle: "What can be automated, what must stay manual, cost projections, labor savings, and rollout sequencing for four civil liberties trackers"
date: 2026-05-06
status: complete
phase: phase-2-preparation
project: resistance-research
purpose: Phase 2 enrichment strategy — immediate post-Phase-1-launch execution
cross_references:
  - tracker-source-audit-detailed.md
  - tracker-visualization-prototype-specs.md
  - tracker-measurement-framework.md
---

# Tracker Automation Feasibility Matrix

*Created: May 6, 2026. This document assesses automation feasibility for each tracker across four dimensions: what the current manual process looks like, which updates can be automated with existing free tools, the legal and ethical constraints per source type, and realistic cost and labor projections for a solo operator.*

**Lead finding**: For three of the four trackers, the most valuable automation target is not the narrative writing — that requires human judgment — but the signal detection layer: learning that a relevant event happened within hours rather than days, so human writing time is spent on current events rather than on discovery of events that already occurred. A solo operator who currently spends 5 hours/week per tracker on monitoring and discovery can realistically reduce that to 1.5–2 hours/week with free automation, redirecting the saved time to analysis and narrative quality. The total cost for this level of automation, excluding labor, is $0–$30/month.

---

## 1. First Amendment Suppression Tracker

### 1.1 Current Manual Process

**Daily time investment**: 45–75 minutes.

The researcher performs the following activities in sequence, typically in the morning:

1. **News scan** (20–30 minutes): Opens NYT, WaPo, Guardian, and CNN in browser. Searches for "press freedom," "First Amendment," "journalist arrested," "anti-protest," "SLAPP suit," and "court ruling free speech." Clips relevant articles to a working notes document.

2. **ACLU case check** (10–15 minutes): Opens aclu.org/cases and filters by First Amendment. Notes new cases not yet in the tracker. Checks case pages already in the tracker for status updates.

3. **Inbox scan** (5–10 minutes): Scans email subscriptions from FPF, RCFP, PEN America, CPJ for press releases. Many days these are empty or irrelevant; significant press releases appear 3–5 times per week.

4. **Write and publish** (15–30 minutes for new entries): Drafts the tracker entry, verifies all cited URLs are live, checks for cross-reference connections to existing entries, updates the "last updated" header.

**Weekly time investment**: 5–6 hours total (daily process × 7 days, with some variation).

**Identified inefficiency**: Steps 1 and 2 could surface 70–80% of relevant events automatically. The researcher is doing search work that a script could do better and faster. Step 4 (writing) cannot be automated without quality loss.

### 1.2 Automatable Updates

The following components of this tracker's update process are directly automatable:

**Signal detection — fully automatable**:
- Press Freedom Tracker API polling: `GET /api/edge/incidents/?date_lower={yesterday}` → returns all press freedom incidents verified in the past 24 hours. This eliminates approximately 80% of the news scan time for press freedom incidents.
- EFF Deeplinks RSS: Covers digital speech suppression events with same-day publication. RSS reader ingestion: 0 minutes of human time.
- FIRE Newsdesk RSS: Covers campus speech and viewpoint discrimination cases. Same mechanism.
- Federal Register API: Daily query for executive orders and agency notices affecting press access. 0 minutes of human time after setup.
- CourtListener webhooks: Set alert for new filings in tracked dockets (AP v. Budowich, NYT v. DOD, In re Natanson). Alert delivered by webhook or email.

**Signal detection — partially automatable**:
- GDELT DOC 2.0 queries for keyword clusters: Returns article lists with titles, URLs, and sentiment. Requires human review to filter false positives (GDELT is noisy for narrow topics). Estimated false positive rate: 40–60% for broad First Amendment queries; can be reduced to 20–30% with refined keyword exclusion lists ("First Amendment rights" without "Second Amendment," "Third Amendment," etc.).
- LegiScan API for state anti-protest bills: Can be queried daily but requires human review to distinguish anti-protest bills from unrelated "public assembly" permit procedures.

**What cannot be automated**:
- Assessing whether an event is tracker-significant (not every press freedom incident rises to tracker-entry level; judgment is required)
- Writing the narrative entry (2–4 paragraphs with context, sources, and analysis)
- Identifying cross-references to other tracker entries or litigation-tracker cases
- Updating the "lead finding" and "how to use" sections when the overall pattern shifts

### 1.3 Legal and Ethical Constraints

**Press Freedom Tracker API**: No constraints. Open-source, CC-licensed data. Attribution required; redistribution permitted. The data agreement explicitly permits automated ingestion.

**CourtListener RECAP API**: Terms of Service explicitly permit programmatic access. Free Law Project is a nonprofit that encourages automated use of its data. Rate limit: 5,000 queries/hour for authenticated users. Note: CourtListener announced in April 2026 that it is transitioning to a membership model that may affect free-tier rate limits. Current 5,000/hour limit is adequate for this tracker's polling volume (estimate: 20–50 queries/day). Monitor their membership policy announcement.

**Federal Register API**: Public domain. No terms restrictions. The Federal Register is a government publication; automated access is explicitly encouraged by the NARA/GPO developer program.

**GDELT DOC 2.0**: Free to use. Attribution to GDELT required. The GDELT project's terms specify that "redistribution of GDELT data in raw form requires scrutiny" — meaning redistribution of the raw data table is restricted, but using GDELT to identify articles and then citing those articles directly (not the GDELT data) is standard practice with no restrictions.

**LegiScan API**: Free tier at 30,000 operations/month. Terms of service permit automated querying for research and advocacy purposes. Commercial redistribution of bulk data is restricted; monitoring for internal tracker use is permitted.

**FIRE RSS and EFF RSS**: RSS feeds are public by design. No restrictions on automated ingestion. Attribution required when citing specific articles.

**PACER access**: Searching PACER is free (no per-search charge). Document downloads cost $0.10/page, with a $3.00 quarterly cap for small users (under 150 pages/quarter). CourtListener's RECAP archive covers most PACER documents at no cost by aggregating user-contributed uploads.

### 1.4 Cost Analysis

**Current monthly cost**: $0 (entirely manual, no subscriptions).

**Post-automation monthly cost** (conservative estimate for solo operator):

| Component | Setup Cost | Monthly Cost |
|-----------|-----------|-------------|
| Press Freedom Tracker API polling script | 2 hours (setup) | $0 |
| EFF + FIRE + Just Security RSS | 30 minutes | $0 |
| Federal Register API script | 1.5 hours | $0 |
| CourtListener webhooks | 1 hour | $0 (or ~$10/mo if membership tier required) |
| GDELT query filtering | 4 hours | $0 |
| LegiScan API | 4–6 hours | $0 |
| Small VPS or GitHub Actions runner | — | $5–10/mo |
| **Total** | **~14 hours one-time** | **$5–10/mo** |

A GitHub Actions workflow (free tier: 2,000 minutes/month) can run all daily polling scripts at zero hosting cost within GitHub's free plan. A small VPS (e.g., DigitalOcean $6/month droplet) provides more reliability and flexibility for logging and alert routing.

### 1.5 Labor Hour Savings

**Current estimate**: 5–6 hours/week for monitoring, discovery, and entry writing.

**Post-automation estimate**:
- Signal detection automated: saves 30–40 minutes/day → 3.5–4.5 hours/week
- Entry writing (cannot be automated): 1–1.5 hours/week remains
- Review and validation queue (human oversight of automated signals): 30 minutes/day → 3.5 hours/week
- **Net time after automation**: 1.5–2 hours/week

**Effective labor saving**: 65–70% reduction in time spent on discovery; total weekly time drops from 5–6 hours to 1.5–2 hours. Caveat: the first 4–6 weeks after automation requires more time to tune false-positive filters.

### 1.6 False Positive Risk Assessment

**Press Freedom Tracker API**: Low false positive risk. FPF/CPJ verify incidents before publication. Occasional edge cases where a "resolved" incident (case dismissed, journalist released) generates a new API entry that might superficially appear to be a new incident. Risk: 5–10%.

**GDELT**: High false positive risk. The query "First Amendment journalist arrested" returns articles about historical events, international incidents, op-eds about First Amendment principles, and articles discussing protests with no arrest. Realistic working false positive rate without tuning: 50–60%. With keyword exclusion lists and geographic filtering to US-only sources: 20–30%. Every GDELT-flagged article requires human review; GDELT reduces discovery time but does not eliminate it.

**LegiScan**: Moderate false positive risk. Searching for anti-protest bills in state legislatures will surface many bills about "public assembly permits" and "noise ordinances" that are not First Amendment restrictions. Manual review of bill text is required for each flagged bill. False positive rate without refinement: 40–50%; with refined queries: 15–25%.

**CourtListener webhooks**: Low false positive risk for tracked dockets (each tracked case is known to be relevant). Higher risk for broad keyword searches (many "First Amendment" filings are irrelevant — routine employment discrimination cases citing the First Amendment tangentially).

### 1.7 Rollout Sequencing

**Week 1**:
- Subscribe to Press Freedom Tracker API (20 minutes, immediate value)
- Subscribe to EFF Deeplinks, FIRE Newsdesk, and Just Security RSS in any feed reader (30 minutes)
- Set up CourtListener webhooks for 5 priority tracked dockets (1 hour)

**Week 2–3**:
- Write and deploy Federal Register API polling script (1.5 hours; deploy to GitHub Actions free tier)
- Write and deploy Press Freedom Tracker API daily diff script (2 hours)

**Week 4–6**:
- Implement GDELT query with initial keyword exclusion list; run for 2 weeks to measure false positive rate; refine
- Implement LegiScan API state legislature monitoring; calibrate keyword filters

**Month 2+**:
- Add Lumen Database API for legal threat monitoring
- Add Media Cloud for regional coverage gaps
- Evaluate whether PACER Case Locator named-target monitoring is worth the additional complexity

---

## 2. Environmental Rollbacks Tracker

### 2.1 Current Manual Process

**Daily time investment**: 20–30 minutes.
**Weekly deep-dive**: 2–3 hours on Tuesdays (when Federal Register publishes most final rules).

**Daily**: Quick scan of EPA newsroom and email subscriptions (Earthjustice, NRDC alerts). Take notes on anything that might be tracker-relevant.

**Weekly deep-dive**:
1. Open Federal Register website, filter to EPA, filter to current week. Browse all documents. Note proposed rules (advocacy window), final rules (tracker entries), and major notices.
2. Open Harvard EELP tracker index; check for new entries since last visit.
3. Check Regulations.gov for major EPA dockets with upcoming comment deadlines.
4. Review queued notes from daily monitoring; draft 1–3 tracker entries.

**Weekly time investment**: 4–5 hours total.

**Identified inefficiency**: The Federal Register browsing step (step 1 of weekly deep-dive) is the most significant automated-replacement opportunity. A script can perform this query in seconds, producing a structured list of every EPA document published that week with title, type (proposed vs. final), and Federal Register citation number. The researcher then reviews the list (5–10 minutes) rather than manually browsing the website (20–30 minutes).

### 2.2 Automatable Updates

**Fully automatable**:
- Federal Register daily polling (EPA, Interior, NOAA, DOE, USDA): Eliminates manual website browsing. Returns structured JSON with document type, agency, title, dates, and links.
- Earthjustice RSS ingestion: Automates monitoring of litigation responses to rollbacks.
- Regulations.gov comment period calendar: Automates identification of upcoming comment deadlines — the advocacy intervention window.
- EDGI website-change detection: Automates monitoring of EPA website content removals.

**Partially automatable**:
- Harvard EELP tracker monitoring: No API. Change-detection tool monitors the EELP tracker index page for new entries (new URLs appearing in the list). When a new entry appears, the tool alerts; human must read the entry and draft a tracker summary.
- EPA ECHO enforcement data: API access is straightforward, but building a meaningful "enforcement collapse" metric requires quarterly aggregation and comparison logic. Automation handles data retrieval; human handles analysis.

**What cannot be automated**:
- Assessing the significance and downstream impact of a rule change (the Endangerment Finding entry is 500+ words of context and analysis; this cannot be auto-generated)
- Understanding the regulatory history that makes a specific rule change consequential
- Identifying how a federal rollback interacts with existing litigation and advocacy campaigns
- Drafting the "real-world impact" and "litigation status" sections

### 2.3 Legal and Ethical Constraints

**Federal Register API**: Public domain. The Federal Register is a government publication produced by the Office of the Federal Register (OFR) and the Government Publishing Office (GPO). Automated access is explicitly supported — the API was built for programmatic use.

**Regulations.gov API v4**: Free with API key (registration at api.data.gov). The GSA explicitly permits automated querying for reading dockets and documents. The POST API (comment submission) was restricted to federal agencies in August 2025, but the GET/read API remains unrestricted. This is the most important constraint to document: anyone who built comment-submission automation before August 2025 will find that broken; read-only monitoring is unaffected.

**EPA ECHO API**: Public domain federal data. The ECHO database is explicitly designed for public programmatic access. No restrictions on automated querying.

**Earthjustice RSS**: RSS is a public web standard. No restrictions on automated ingestion. Attribution required when citing specific litigation updates.

**Harvard EELP monitoring**: EELP does not prohibit automated change-detection monitoring. Their terms do not restrict reading their publicly available pages. Automated bulk crawling of EELP's full content (e.g., downloading all tracker entries) would be outside reasonable use; monitoring the index page for new entries is standard practice.

**Changedetection.io / Distill.io** (for EELP and Protect Democracy monitoring): These are monitoring services that poll web pages for changes. Both services operate by making normal HTTP requests; no terms of service are violated for normal page monitoring. Rate limiting applies: monitoring a page at most once per hour is standard; more frequent polling risks being blocked.

### 2.4 Cost Analysis

**Current monthly cost**: $0.

**Post-automation monthly cost**:

| Component | Setup Cost | Monthly Cost |
|-----------|-----------|-------------|
| Federal Register API script (multi-agency) | 2.5 hours | $0 |
| Regulations.gov comment period calendar | 3 hours | $0 |
| Earthjustice RSS ingestion | 10 minutes | $0 |
| Harvard EELP change-detection | 30 minutes | $5–15 |
| EPA ECHO quarterly aggregation script | 8–12 hours | $0 |
| GitHub Actions runner | — | $0 (free tier) |
| **Total** | **~15 hours one-time** | **$5–15/mo** |

This tracker has the lowest ongoing cost because its most valuable sources (Federal Register, Regulations.gov, Earthjustice) are all fully free APIs or RSS feeds. The only paid component is a change-detection service for EELP, which has no API.

### 2.5 Labor Hour Savings

**Current estimate**: 4–5 hours/week.

**Post-automation estimate**:
- Federal Register browsing automated: saves 20–30 min/week
- Regulations.gov comment calendar automated: saves 15 min/week
- Earthjustice alert delay reduced from email to RSS ingest: saves 10–15 min/week
- EPA ECHO quarterly reports: replaces 2–3 hour manual data gathering with 15-min review
- **Net time after automation**: 2.5–3 hours/week

**Effective labor saving**: 35–45% reduction. This tracker has higher inherently-manual content than the First Amendment tracker — each entry requires deep regulatory knowledge — so automation gains are smaller in percentage terms but still significant. The EPA ECHO quarterly report is the highest-leverage single automation item.

### 2.6 False Positive Risk Assessment

**Federal Register API**: Low false positive risk for formal rules. Moderate risk for notices (many notices are routine administrative actions, not significant rollbacks). Filter: exclude documents with type "NOTICE" where keywords don't include "enforcement," "standard," "repeal," "rescind," or agency-specific rule names.

**Regulations.gov**: Low for comment period monitoring. Most EPA comment periods are directly relevant (they are all rulemaking actions).

**Earthjustice RSS**: Very low. Earthjustice publishes about its own cases and analyses; almost all are tracker-relevant.

**EELP change-detection**: Zero false positive risk (EELP only publishes tracker entries about significant regulatory actions). The only "false positive" would be an update to an existing entry rather than a new entry — both are tracker-relevant.

### 2.7 Rollout Sequencing

**Week 1**:
- Set up Federal Register API multi-agency polling script (2.5 hours) — highest immediate value
- Subscribe to Earthjustice RSS (10 minutes)

**Week 2**:
- Set up Regulations.gov comment period calendar (3 hours)
- Set up Harvard EELP change-detection (30 minutes + $5–15/month tool subscription)

**Month 2**:
- Implement EPA ECHO quarterly enforcement aggregation script
- Add state environmental agency RSS monitoring (TX, WY, LA)

**Month 3+**:
- Evaluate EDGI website-change monitoring integration
- Add GovInfo API for EIS tracking if Interior actions become a higher priority

---

## 3. Police Brutality / Consent Decree Tracker

### 3.1 Current Manual Process

**Weekly time investment**: 5–7 hours (heaviest of the four trackers in terms of manual effort, due to the complexity of consent decree compliance monitoring).

**Daily (30–40 minutes)**:
- DOJ newsroom check: justice.gov/news, filter by Civil Rights. Any new press releases?
- ACLU national cases check.
- News scan for police shootings, consent decree developments, excessive force verdicts.

**Weekly deep-dive (3–4 hours)**:
- Pull and read any new independent monitor reports from tracked cities. These are filed as PDFs with federal courts; currently requires manual PACER access or waiting for news coverage.
- Update compliance percentage figures for tracked cities (Chicago, Seattle, Baltimore, LAPD, Minneapolis, Cleveland).
- Check for new state AG enforcement actions or announcements.
- Draft new entries or update existing ones.

**Identified inefficiency**: The independent monitor report discovery process is the highest-friction step. Monitor reports are filed with federal courts on quarterly or semi-annual schedules; they are not newsworthy unless they show extreme results. The researcher currently finds out about them through news coverage (which is delayed) or through periodic PACER browsing (which requires knowing which dockets to check). CourtListener docket monitoring would automate this discovery.

### 3.2 Automatable Updates

**Fully automatable**:
- DOJ Civil Rights Division RSS: Replaces manual justice.gov browsing.
- State AG RSS feeds (6 states): Replaces manual monitoring of 6 separate AG websites.
- CourtListener consent decree docket monitoring: Automates discovery of new monitor report filings, court orders, and exit motion filings in tracked cases.
- Mapping Police Violence Airtable API polling: Daily new incidents feed.

**Partially automatable**:
- GDELT police violence filtering: Fast signal for breaking incidents; 30–40% false positive rate requires human filtering.
- Law Enforcement Knowledge Lab dashboard monitoring: No API; change-detection tool appropriate.

**What cannot be automated**:
- Reading and summarizing monitor reports (these are 50–200 page PDFs; key findings must be identified and contextualized)
- Assessing whether a new incident rises to tracker-entry level (not every police shooting is a tracker entry; selection criteria require judgment)
- City-level compliance analysis (interpreting compliance percentages in context of prior monitoring history)
- Cross-referencing to First Amendment suppression entries when police use of force occurs at protests

### 3.3 Legal and Ethical Constraints

**DOJ RSS feeds**: Public domain. No restrictions.

**State AG RSS feeds**: Public domain. All six targeted state AG offices publish RSS feeds as a public communications service.

**CourtListener RECAP**: As noted for the First Amendment tracker: free, terms permit automation, transitioning to membership model as of April 2026. The docket monitoring use case requires maintaining a list of 10–15 specific docket numbers; this is a very low query volume (20–30 queries/day) that will remain well within any free tier.

**Mapping Police Violence Airtable**: Public Airtable base. Airtable's terms of service permit reading public bases via the API. Non-commercial use preferred. The Mapping Police Violence team explicitly supports advocacy use of their data.

**LEKL Federal Interventions Dashboard**: No formal terms for automated monitoring. Change-detection monitoring makes normal HTTP requests; standard practice for any publicly accessible web page. Recommend checking periodically for a robots.txt exclusion or terms update.

**CourtListener rate limit concern for this tracker specifically**: Consent decree docket monitoring requires ongoing polling of a maintained list of docket numbers. At 15 dockets × 4 polls/day = 60 queries/day, well within the current 5,000 queries/hour limit even under a restrictive tiered model.

### 3.4 Cost Analysis

**Current monthly cost**: $0, plus PACER access costs (estimates: $5–15/month for monitor report document access).

**Post-automation monthly cost**:

| Component | Setup Cost | Monthly Cost |
|-----------|-----------|-------------|
| DOJ Civil Rights RSS + State AG RSS | 1 hour | $0 |
| CourtListener docket monitoring script | 4–6 hours | $0 |
| Mapping Police Violence Airtable polling | 3–4 hours | $0 |
| LEKL change-detection | 30 minutes | $5–15 |
| GDELT police violence filter | 3 hours | $0 |
| VPS or GitHub Actions | — | $0–10 |
| **Total** | **~13 hours one-time** | **$5–25/mo** |

Note: PACER access costs for monitor report downloads are $0.10/page with a $3.00 quarterly cap for small users. If monitor reports average 75 pages each and there are 10 active decrees with quarterly reports, annual PACER document cost is approximately $30 — well under the quarterly cap. CourtListener RECAP often has these documents for free if another user already uploaded them.

### 3.5 Labor Hour Savings

**Current estimate**: 5–7 hours/week.

**Post-automation estimate**:
- DOJ and state AG monitoring automated: saves 30–40 min/week
- CourtListener docket monitoring: saves 1.5–2 hours/week (eliminates manual PACER docket browsing)
- Mapping Police Violence daily feed: saves 30 min/week
- GDELT rapid incident signal: saves 20–30 min/week
- **Net time after automation**: 2.5–3.5 hours/week

**Effective labor saving**: 45–55% reduction. Monitor report reading remains fully manual (no way to summarize 75-page PDFs at quality without significant AI investment); this is the irreducible core of this tracker's time requirement.

### 3.6 False Positive Risk Assessment

**DOJ Civil Rights RSS**: Very low false positive risk. DOJ CRT press releases are almost entirely relevant. Under current administration, volume is low (CRT is not announcing new enforcement actions); the risk is missed events (false negatives) more than false positives.

**State AG RSS feeds**: Low-moderate. State AGs publish on many topics; keyword filtering for "police," "consent decree," "pattern or practice," "use of force," "civil rights" narrows to relevant items. Estimated relevant rate after filtering: 40–60% (AGs also announce consumer protection, antitrust, and other cases).

**CourtListener docket monitoring**: Near-zero false positive risk for tracked dockets. The dockets are known relevant cases; every new filing is at minimum noteworthy even if not every filing requires a tracker entry.

**Mapping Police Violence**: Low for incident data. The MPV team verifies incidents before publication; false inclusion in their database is uncommon. The tracker-relevant subset (incidents in cities with active consent decrees) requires geographic filtering.

**GDELT**: Moderate-high (40–50%) for police violence queries. "Police brutality" and "consent decree" in GDELT returns articles about historical cases, opinion pieces, international incidents. Human review required for every flagged item.

### 3.7 Rollout Sequencing

**Week 1**:
- Subscribe to DOJ Civil Rights RSS and 6 state AG RSS feeds (1 hour)
- Set up CourtListener consent decree docket list and monitoring script (5 hours) — this is the highest-value single item

**Week 2–3**:
- Implement Mapping Police Violence Airtable API polling (3–4 hours)
- Set up LEKL change-detection ($5–15/month tool)

**Month 2**:
- Implement GDELT police violence filter; calibrate false positive threshold
- Add ProPublica Injustice on Your Block quarterly data pull

---

## 4. Prosecutorial Weaponization Tracker

### 4.1 Current Manual Process

No systematic manual process exists. This tracker's current state is distributed across two analysis documents (first-amendment-suppression.md Section 7, domain-29). This means the "current manual process" is essentially: "researcher notices a major prosecution in the news and adds it to the relevant analysis document."

This is not a process — it is reactive coverage. The estimated miss rate is 50–70% of politically relevant prosecutions.

**Pre-Phase-2 prerequisite**: Before automation can be designed, the tracker needs a dedicated file (`prosecutorial-weaponization-tracker.md` analogous to the other three trackers). The automation architecture below assumes this file exists.

**Estimated time to create the base tracker file from domain-29 content**: 3–4 hours. The 22 documented cases in domain-29 provide the starting content; they need to be reformatted into the consistent tracker entry structure used by the other three trackers.

### 4.2 Automatable Updates

**Fully automatable**:
- DOJ USAO RSS feed polling with keyword filter: The primary official signal for new prosecutions. Every federal prosecution announcement appears here first. Requires keyword filter (list of known targets, organization names, categories of political prosecution).
- Just Security RSS: Expert analysis of prosecutorial weaponization cases. Near-zero false positive rate for relevant coverage.
- Wikipedia revision feed for political targeting article: Secondary completeness check; alerts when community editors document a new target.

**Partially automatable**:
- Protect Democracy tracker change-detection: Alerts when new entries are added; requires human review to read and summarize new entries.
- CourtListener vindictive/selective prosecution motion search: Automated query; human review to assess political relevance.
- GDELT political prosecution query: Automated signal; moderate false positive rate.
- PACER Case Locator named-target monitoring: Semi-automated; requires maintaining a watchlist of names.

**What cannot be automated**:
- Applying the three-question pattern test (was the target identified as political opposition? Does the legal theory have precedent? Is there a pattern of similar actions?)
- Assessing legal theory validity (requires legal knowledge; the SPLC *Thompson* bank fraud issue required a former federal prosecutor to identify)
- Updating the domain-29 systemic pattern analysis as new cases modify the aggregate pattern
- Identifying the normative violations (staging of press conferences, jurisdictional choices, absence of victim complaints) that distinguish weaponization from ordinary prosecution

### 4.3 Legal and Ethical Constraints

**DOJ USAO RSS**: Public domain. No restrictions.

**PACER/CourtListener**: As documented above. The named-target monitoring use case (querying PACER Case Locator for specific individuals) raises a distinct consideration: PACER's terms of service prohibit "commercial bulk data extraction" but explicitly permit research and advocacy access. Monitoring a watchlist of 20–50 political targets once daily is well within these terms. The $0.10/page charge for PACER document downloads applies only when the full document is accessed; case locator searches are free.

**Protect Democracy tracker monitoring**: Protect Democracy is a nonpartisan advocacy organization. Their retaliatory action tracker is published publicly and explicitly intended for civil society use. Change-detection monitoring makes standard HTTP requests; no restrictions. Recommend confirming their robots.txt allows automated access.

**Wikipedia API**: CC-BY-SA licensed. Attribution required. Wikipedia's terms explicitly permit automated API access for research and monitoring purposes. The Wikimedia Foundation actively supports this use case.

**GDELT**: As documented above. The key constraint for this tracker is avoiding republication of GDELT's raw data — using GDELT to identify articles and then citing those articles' original URLs is standard practice with no restrictions.

**Keyword watchlist ethics**: The keyword filter for DOJ USAO RSS will include names of real people (Democratic officials, civil rights lawyers, activists) who are potential prosecution targets. This is not a surveillance program — it is monitoring public government press releases for government action against people. There is no legal or ethical constraint on this practice; it is standard journalism and advocacy practice.

### 4.4 Cost Analysis

**Current monthly cost**: $0 (no systematic process).

**Post-automation monthly cost**:

| Component | Setup Cost | Monthly Cost |
|-----------|-----------|-------------|
| DOJ USAO RSS with keyword filter | 3–4 hours | $0 |
| Just Security + Wikipedia RSS/API | 1 hour | $0 |
| Protect Democracy change-detection | 1 hour | $5–15 |
| CourtListener vindictive prosecution query | 3 hours | $0 |
| GDELT political prosecution filter | 3 hours | $0 |
| PACER Case Locator watchlist (optional) | 4 hours | $0 (search free) |
| Base tracker file creation | 3–4 hours | — |
| **Total** | **~20 hours one-time** | **$5–15/mo** |

The 3–4 hours for base tracker file creation are a prerequisite, not an automation cost.

### 4.5 Labor Hour Savings

**Baseline**: Estimated 0–1 hours/week currently spent on this tracker (reactive, not systematic).

**Post-automation estimate**:
- Systematic monitoring established
- Signal detection: 1–2 hours/week of alert review
- Entry writing and analysis: 2–3 hours/week
- **Net time after automation**: 3–5 hours/week (more than current — this represents net new investment as the tracker is properly activated)

This is the one tracker where automation does not primarily save time — it primarily enables a function that currently does not exist. The investment is justified by the coverage gap: 50–70% miss rate on politically relevant prosecutions means the tracker as currently structured is not performing its function.

### 4.6 False Positive Risk Assessment

**DOJ USAO RSS with keyword filter**: This is the most significant false positive challenge across all four trackers. DOJ publishes hundreds of press releases weekly; the keyword filter must identify politically relevant cases without flooding the review queue with drug cases, immigration prosecutions, and routine fraud charges. Estimated false positive rate for initial broad filter: 60–70%. With refined keyword exclusion (filtering out drug type names, immigration violation categories, bank robbery): 20–30%. Target: 5–10% after 4–6 weeks of filter calibration.

**Protect Democracy change-detection**: Near-zero false positive risk. Protect Democracy applies a rigorous three-question test before adding entries; their tracker is conservative in what it includes.

**Just Security RSS**: Very low. Just Security publishes only high-confidence analysis; they are not a breaking news aggregator.

**Wikipedia revision feed**: Moderate false positive risk. Wikipedia editors add content from multiple perspectives; not every addition to the political targeting article reflects a newly identified case (editors also update existing entries, correct errors, add context). Human review required.

**CourtListener vindictive prosecution search**: Moderate. "Vindictive prosecution" appears in thousands of criminal defense motions, most of which are not politically motivated cases. The relevant subset (cases with political-opposition defendants, civil society organization defendants, or journalists) requires a secondary filter.

### 4.7 Rollout Sequencing

**Week 1** (prerequisite):
- Create `prosecutorial-weaponization-tracker.md` base file from domain-29 content (3–4 hours)

**Week 1–2** (automation):
- Set up DOJ USAO RSS with initial keyword filter (3–4 hours)
- Subscribe to Just Security RSS (10 minutes)
- Set up Wikipedia revision API polling (1 hour)

**Week 3–4**:
- Implement Protect Democracy change-detection monitoring ($5–15/month tool)
- Calibrate DOJ USAO RSS keyword filter based on first two weeks of output; reduce false positive rate

**Month 2**:
- Implement CourtListener vindictive prosecution query
- Evaluate PACER Case Locator named-target watchlist (based on whether the DOJ RSS filter is missing cases that PACER would catch)

---

## Cross-Tracker Automation Summary

**Total one-time implementation investment**: 60–75 hours across all four trackers. With focused effort (10 hours/week), this is 6–8 weeks of part-time work.

**Total ongoing monthly cost**: $10–40, depending on which change-detection tools are used and whether a VPS is deployed (GitHub Actions free tier may be sufficient).

**Total labor savings per week (once operational)**: 10–15 hours/week saved across the four trackers, from a combined baseline of ~20–23 hours/week. This represents approximately a 50% reduction in monitoring time, with the saved time redirected to higher-quality analysis.

**Single highest-value implementation item**: Federal Register API for the Environmental tracker. 2 hours of setup; daily automated polling of all EPA and environmental agency rulemaking; $0 ongoing cost; eliminates 20–30 minutes/week of manual browsing that currently produces less complete results.

**Lowest-cost highest-coverage upgrade**: Subscribe to Press Freedom Tracker API, EFF Deeplinks RSS, FIRE RSS, Just Security RSS, Earthjustice RSS, DOJ Civil Rights RSS, and six state AG RSS feeds. Combined setup time: approximately 2 hours. Cost: $0. This single step upgrades monitoring coverage across all four trackers with essentially no implementation burden.

---

*Sources: [CourtListener API](https://www.courtlistener.com/help/api/) | [CourtListener membership transition — GitHub issue #7200](https://github.com/freelawproject/courtlistener/issues/7200) | [Federal Register API developers](https://www.federalregister.gov/developers/documentation/api/v1) | [Regulations.gov API and POST API restriction](https://open.gsa.gov/api/regulationsgov/) | [PACER Case Locator API guide](https://pacer.uscourts.gov/help/pacer/pacer-case-locator-pcl-api-user-guide) | [EPA ECHO API](https://echo.epa.gov/tools/web-services) | [Datasette for data publishing](https://datasette.io/) | [GitHub Actions free tier](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions)*
