---
title: "Phase 1 Adoption Tracking Automation — Operator's Guide"
date: 2026-05-09
status: production-ready
phase: Phase 1 — activate on first send wave
scope: >
  Single consolidated reference for running the adoption tracking system
  from Day 0 through Month 6. Covers spreadsheet schema, data collection
  procedures, auto-update protocols, weekly and monthly reporting templates,
  and success criteria. Replaces the need to cross-reference multiple
  specification documents during active operations.
companion_files:
  - adoption-automation-infrastructure.md          # Full column schema with auto-calc formulas
  - adoption-tracking-dashboard-spec.md            # Citation monitor setup, tool configuration
  - post-distribution-tracking.md                  # Sector pathways, decision trees, Week 1–4 roadmap
  - post-distribution-adoption-framework.md        # Attribution methodology, conceptual typology
  - DISTRIBUTION_OUTREACH_CONTACTS.md             # Full 45+ Tier 1 contact list
  - DISTRIBUTION_GIST_URLS.md                     # All canonical Gist IDs
  - phase-1-baseline-metrics.md                   # Pre-distribution search baselines
---

# Phase 1 Adoption Tracking Automation — Operator's Guide

**May 9, 2026. Activates on Wave 1 send (Path A / A+37 / B — path-independent).**

This is the single document you open during active Phase 1 operations. It tells you what to build before the first email goes out, what to do each week, what auto-updates are available, and what success looks like at 30, 90, and 180 days. It does not reproduce the full theoretical architecture — that lives in the companion documents. Everything here is actionable.

---

## Part 1 — What Counts as Adoption

Adoption is not reading. Adoption is not replying. Adoption is an institutional actor doing something consequential with the framework — incorporating its analysis, vocabulary, or structure into work that reaches other actors.

### The Five-Level Scale

| Level | Label | Definition | First evidence |
|-------|-------|------------|----------------|
| 0 | No engagement | Sent; no signal of any kind | — |
| 1 | Awareness | Confirmed receipt, substantive reply, or Gist views >3; no published output | Reply email, Gist analytics |
| 2 | Reference | Framework vocabulary or analysis appears in the organization's published work | Published document URL |
| 3 | Operational | Domain analysis used in active casework, testimony, brief, or legislation | Court filing, bill text, testimony transcript |
| 4 | Coalition | Organization actively distributes framework to its own networks, triggering secondary adoption | Secondary org using framework language; direct confirmation |

**Minimum meaningful adoption for Phase 1 success**: 3 organizations reach Level 2 or above within 6 months, across at least 2 institutional sectors.

### What Does Not Count as Adoption

- Email reply without any published output (Level 1, not 2)
- Social media share by an individual not acting in an organizational capacity
- A website link to the Gist without any analytical use of the content
- A "thanks for sharing" reply with no follow-through signal within 60 days

### Vocabulary Markers — Attribution Fingerprints

Before sending Wave 1, run baseline Google searches for each phrase below and record the result count in `phase-1-baseline-metrics.md`. Post-distribution, any document using these phrases that post-dates the organization's first contact is a strong attribution signal.

| Domain cluster | Marker phrases |
|----------------|----------------|
| Domain 1 / 37 (voting, election) | "NVRA quiet period," "ICE-at-polls," "SAVE database voter roll purge" |
| Domain 6 / 33 (judiciary, state autocratization) | "appellate capture," "state legislative autocratization," "REDMAP 2.0 pipeline" |
| Domain 16 (immigration) | "warrantless arrest escalation pattern," "pattern-and-practice enforcement escalation" |
| Domain 29 (prosecutorial) | "22-case retaliatory pattern," "bank fraud contradiction" |
| Domain 34 (fiscal) | "fiscal authority bypass," "OMB apportionment abuse," "pocket rescissions" |
| Domain 28 (war powers) | "arrest operation theory," "Vance doctrine Youngstown" |

Expected pre-distribution baseline for novel coinages: 0–2 results. Any post-distribution result exceeding baseline in a document published after confirmed contact constitutes a vocabulary adoption signal.

---

## Part 2 — Tracking Spreadsheet Schema

Maintain one Google Sheets workbook with the sheets described below. The workbook should be created in the same Google account used for outreach, so alert emails land in the same inbox.

### Sheet 1: Master Contact Log

One row per organization (not per individual). Where an institution has multiple contacts, use the primary contact as the canonical row and note secondary contacts in the `notes` column.

**Identity columns — populate before Wave 1 send**

| Column | Type | Source |
|--------|------|--------|
| `org_id` | Integer 1–45 | Assign sequentially |
| `org_name` | Text | `DISTRIBUTION_OUTREACH_CONTACTS.md` |
| `org_short` | Text | Abbreviated handle (e.g., "Brennan Center") |
| `sector` | Dropdown: Law School / Think Tank / Civil Rights Org / Legal Services / Labor / Foundation | `DISTRIBUTION_OUTREACH_CONTACTS.md` |
| `tier` | Integer 1–3 | From contact list |
| `primary_contact` | Text | Named individual |
| `contact_email` | Text | Verify live before each wave |
| `gist_url_sent` | URL | Which Gist URL was included in this org's email |
| `domain_focus` | Text | Domain numbers relevant to this org (e.g., "1, 6, 33") |

**Send-state columns — populate as waves execute**

| Column | Type | Notes |
|--------|------|-------|
| `email_sent_date` | Date YYYY-MM-DD | Populate on send |
| `wave_number` | Integer | 1 / 2 / 3 |
| `days_since_send` | Formula | `=IF(email_sent_date="","",TODAY()-email_sent_date)` |
| `sla_respond_by` | Formula | Sector SLA lookup (see SLA Reference sheet) |
| `bounce_detected` | Boolean Y/N | Check within 24 hours of send |
| `bounce_type` | Dropdown: Hard / Soft / None | Hard = permanent failure; Soft = temporary |
| `alt_contact_tried` | Boolean Y/N | Fill if bounce=Y |

**Signal columns — update per event, not per week**

| Column | Type | Notes |
|--------|------|-------|
| `email_reply_received` | Boolean Y/N | Any substantive reply |
| `reply_date` | Date | Date of first non-auto-acknowledgment reply |
| `reply_category` | Dropdown: Implementation Question / Methodology Critique / Integration Request / Thanks-No-Action / Bounced | See Part 4 for definitions |
| `gist_views_d7` | Integer | Cumulative view count at Day 7 |
| `gist_views_d14` | Integer | Cumulative view count at Day 14 |
| `gist_views_d28` | Integer | Cumulative view count at Day 28 |
| `secondary_dist_detected` | Boolean Y/N | Org forwarded material to others |
| `secondary_dist_evidence` | Text/URL | Source of secondary distribution signal |
| `vocab_adoption_detected` | Boolean Y/N | Framework vocabulary in org's public output |
| `vocab_evidence_url` | URL | Link to document with the vocabulary usage |
| `structural_adoption_detected` | Boolean Y/N | Framework analytical structure used in output |
| `citation_detected` | Boolean Y/N | Explicit citation in published document |
| `citation_url` | URL | Link to citing document |

**Scoring and status columns — recalculate at each checkpoint**

| Column | Type | Notes |
|--------|------|-------|
| `engagement_score` | Integer 0–5 | Rubric: Section 2.2 below |
| `score_d7` | Integer | Snapshot at Day 7 |
| `score_d14` | Integer | Snapshot at Day 14 |
| `score_delta` | Formula | `=score_d14-score_d7` — positive = momentum |
| `adoption_level` | Integer 0–4 | Five-level scale from Part 1 |
| `tier2_candidate` | Boolean Y/N | Composite readiness score ≥ 7 (see Part 3) |
| `attribution_confidence` | Dropdown: High / Medium / Low / Insufficient | Attribution test results |
| `next_action` | Text | What to do and by when |
| `last_updated` | Date | Date of most recent row edit |
| `notes` | Text | Free text |

### Sheet 2: SLA Reference

Reference table for the `sla_respond_by` auto-calc field on the Master Contact Log.

| Sector | SLA Days | Rationale |
|--------|----------|-----------|
| Legal Services / Immigration Legal Aid | 5–14 | Active docket pressure; fastest processors |
| Mutual Aid / Grassroots Organizing | 2–7 | Small staff, fast decisions |
| Think Tanks | 14–30 | Internal review and publication pipeline |
| Civil Rights Litigation Orgs | 7–21 | Case-driven urgency |
| Law Schools (clinic directors) | 21–60 | Semester cycle; faculty review lag |
| Academics / Policy School Faculty | 14–42 | Research calendar dependent |
| Foundations | 30–60 | Grantmaking cycle; routing to program officers |
| Labor Unions | 21–45 | Research department review cycle |

Formula for `sla_respond_by`: `=email_sent_date + VLOOKUP(sector, SLA_table, 2, FALSE)`

### Sheet 3: Gist View Log

One row per Gist, one column per week. The six canonical Gists to track:

| Gist | ID | Purpose |
|------|----|---------|
| Full Proposal | `2dec7fd03b08ab5b41c55d402f44c261` | Primary distribution artifact |
| Executive Summary | `2869da6eaeb15a47246ade3bbbc4a3f4` | Compact send for time-constrained contacts |
| Litigation Tracker | `418d51bda087f15a04d685ab171a5ee0` | AG and civil rights org sends |
| First Amendment Tracker | `10d0a86e386e6c3c11c3830295a6503c` | Press freedom and First Amendment contacts |
| Environmental Rollbacks | `87e2bdb931b77480e56a08044c567bc4` | Environmental sector sends |
| Police Consent Decrees | `1f5cb28527c98d12526c14302c725731` | Criminal justice contacts |

Weekly entry structure:

| Column | Content |
|--------|---------|
| `gist_id` | Gist hash ID |
| `gist_label` | Short label |
| `week_N_cumulative` | Cumulative view count at end of Week N |
| `week_N_delta` | `=week_N_cumulative - week_(N-1)_cumulative` |
| `spike_flag` | "YES" if delta >10 in a single week |

### Sheet 4: Citation Log

One row per citation event detected through any monitoring channel.

| Column | Content |
|--------|---------|
| `date_detected` | YYYY-MM-DD |
| `citing_org` | Organization name |
| `document_title` | Title or description of citing document |
| `document_url` | URL or PACER/CourtListener docket reference |
| `domain_cited` | Domain number(s) referenced |
| `sector` | Citing organization's sector |
| `adoption_level_implied` | Level 2 / 3 / 4 |
| `detection_source` | Google Alerts / Scholar Alert / CourtListener / LegiScan / Manual / Direct contact |
| `vocabulary_test_passed` | Y/N |
| `structural_test_passed` | Y/N |
| `timing_test_passed` | Y/N |
| `attribution_confidence` | High / Medium / Low |
| `notes` | Free text |

### Sheet 5: Domain Heat Map

One row per domain (1–37+). Columns track cumulative citation events by month.

| Column | Content |
|--------|---------|
| `domain_num` | Integer |
| `domain_name` | Abbreviated title |
| `month_1` | Citation event count at Day 30 |
| `month_3` | Count at Day 90 |
| `month_6` | Count at Day 180 |
| `month_12` | Count at Day 365 |
| `dominant_sector` | Sector accounting for most citations |
| `status` | Baseline / Active (1+) / Hot (5+) / Stalled / Captured |

Update the `status` field monthly based on citation event counts and whether adoption is growing or stalled.

### Sheet 6: Failure Mode Log

| Column | Content |
|--------|---------|
| `date_detected` | YYYY-MM-DD |
| `failure_mode` | False adoption / Misinterpretation / Capture / Decay / Partial bias |
| `institution` | Organization name |
| `domain` | Domain number |
| `evidence` | Description or URL |
| `response_taken` | Action taken |
| `resolution` | Resolved / Monitoring / Escalated |

### Sheet 7: Tier 2 Candidates

A filtered view of the Master Contact Log where `tier2_candidate=Y`, sorted by composite readiness score descending. Add three columns not on the Master sheet:

| Column | Content |
|--------|---------|
| `factor1_engagement` | Engagement score (0–5) from Master Log |
| `factor2_integration` | Integration signal strength (0–3): 0=none, 1=vocabulary, 2=structural, 3=formal cite/pilot |
| `factor3_network` | Network multiplier (0–2): 0=internal reach, 1=sector influence, 2=high-velocity distribution |
| `composite_score` | `=factor1+factor2+factor3` |
| `tier2_action` | "1-on-1 brief within 48h" if composite ≥9; "Add to Tier 2 list" if composite 7–8 |

---

## Engagement Score Rubric (0–5)

| Score | Condition |
|-------|-----------|
| 0 | Email sent; no signal of any kind |
| 1 | No bounce; Gist viewed 1+ times; no reply |
| 2 | Substantive email reply received (any category except Bounced) |
| 3 | Reply + Gist views >3, or secondary distribution detected |
| 4 | Vocabulary or structural adoption detected in public output |
| 5 | Explicit citation, litigation reference, curriculum integration, or formal policy proposal |

---

## Part 3 — Data Collection Methods

### 3.1 Gist View Tracking (Primary Engagement Proxy)

GitHub does not expose Gist analytics via its public REST API. The analytics view is owner-only. The procedure is manual and takes approximately 10 minutes per week.

**Weekly Gist pull procedure (run every Monday):**

1. Log in to `github.com` as the Gist-owner account
2. For each of the six canonical Gists, navigate to `https://gist.github.com/[username]/[GIST_ID]/analytics`
3. The analytics tab shows daily view counts for the prior 30 days
4. Record the current cumulative total in the Gist View Log sheet under `week_N_cumulative`
5. The delta formula (`week_N_cumulative - week_(N-1)_cumulative`) auto-calculates new views this week
6. If any Gist shows a delta >10 in a single week, flag `spike_flag=YES` and cross-reference which organizations were sent that Gist URL. Follow up with those organizations if they have not yet replied.

**Disambiguation note**: A single organization opening the same Gist multiple times inflates the count. To partially disambiguate engagement across organizations, send different organizations slightly different Gist URLs when the content permits (e.g., executive summary Gist vs. full proposal Gist). Differential view trajectories reveal which content drives engagement.

**Limitation**: Gist view counts are a proxy, not a direct measure of who opened the email. Organizations that stripped email pixels (most law school, AG, and civil rights org mail servers do this) will generate zero email open data. Gist views are the best available indirect signal.

### 3.2 Email Reply Monitoring (Highest-Signal, Zero Automation Needed)

A substantive reply is the clearest adoption signal available. Check the outreach email account daily during Weeks 1–4, then every 2–3 days thereafter.

**Substantive reply** = any reply containing more than a generic acknowledgment — a question, a critique, a referral offer, a domain-specific request, or any statement of intended use.

**Non-substantive** = auto-acknowledgment, "received" with no content, vacation auto-reply.

Log all substantive replies within 24 hours of receipt using the routing logic in Part 4.

### 3.3 Google Alerts — Automated Citation Detection

**Setup (15 minutes, one-time):**

At `news.google.com/alerts`, create alerts with daily email delivery routed to a dedicated label (e.g., `monitoring/google-alerts/`). Use "All results" mode, not "Best results."

Alert set A — Framework identity:
- `"democratic renewal proposal"`
- `"35-domain democratic"`
- `"democratic renewal framework" democracy`

Alert set B — Vocabulary markers (use the full marker list from Part 1):
- `"ICE-at-polls" election`
- `"NVRA quiet period" 2026`
- `"state legislative autocratization"`
- `"appellate capture" judicial independence`
- `"fiscal authority bypass" OMB`
- `"arrest operation theory" "war powers"`

Alert set C — Bridge node second-order detection:
- `"Brennan Center" "voting rights" "democratic renewal"`
- `"Just Security" "judicial independence" 2026`
- `"Democracy Docket" "voter roll" SAVE 2026`

**Review cadence**: Scan the alert digest folder each Monday. Any hit from a recognized policy, legal, academic, or media organization goes into the Citation Log immediately. Hits from unrecognized sources: note but do not log until source is verified.

**Coverage limitation**: Google Alerts does not reliably index PDF documents, legal filings, or password-gated academic platforms. Supplement with CourtListener for litigation monitoring and Google Scholar for academic papers.

### 3.4 Google Scholar Alerts — Academic Citation Detection

**Setup (10 minutes, one-time):**

At `scholar.google.com/scholar_alerts`:
- `"democratic renewal proposal"`
- `"35-domain" democracy institutional`
- `"state legislative autocratization" institutional`

Scholar alerts fire when new indexed academic papers match the query. Expect zero alerts for the first 3–4 months — academic indexing has a significant lag. These alerts are the primary detection mechanism for the 12–24 month law review adoption window, not the Phase 1 window.

### 3.5 CourtListener Saved Searches — Litigation Citation Detection

**Setup (20 minutes, one-time; free tier supports 5 alert-enabled searches):**

At `courtlistener.com`, create saved searches with email alerts enabled:

- Search 1: `"democratic renewal proposal"` — scope: All federal courts
- Search 2: `"ICE at polls" OR "NVRA quiet period" OR "SAVE database" voter roll 2026` — scope: All federal courts
- Search 3: `"appellate capture" OR "fiscal authority bypass"` — scope: All federal courts
- Search 4: `"amicus" "voting rights" "democratic" 2026` — scope: Federal district and circuit courts
- Search 5: Bookmark each active case from `litigation-tracker-2026.md` for manual docket review

When a CourtListener alert fires, download and read the document within 48 hours. Check for framework vocabulary markers and structural convergence. Log any confirmed citation in the Citation Log.

### 3.6 LegiScan API — State Legislative Bill Monitoring

**Setup (30 minutes, one-time; free tier: 30,000 queries/month):**

Register at `legiscan.com/legiscan-register`. Create full-text saved searches in priority states (CA, NY, MN, WI, PA, MI, CO, AZ, OH, VA, NC, GA):

Set A — Domain 1 / 37 election language:
- `"voter roll" purge SAVE 2026`
- `"ICE" polling place election interference`
- `"NVRA" voter removal quiet period`

Set B — Domain 33 state autocratization language:
- `preemption "local government" ballot initiative restriction`
- `"election administration" override legislature`

Set C — Domain 6 / 34 institutional authority language:
- `"judicial independence" federal funding`
- `"fiscal authority" executive impoundment`

Configure daily email notifications. Log any matching bill in Sheet 4 (Citation Log) under sector "Legislative — State."

### 3.7 Secondary Distribution Detection

Secondary distribution is evidence of Level 4 adoption in progress. Three methods to detect it:

**(a) Site search.** Once per week, run: `site:[org-domain] "democratic renewal"` and `site:[org-domain] "fiscal authority bypass"` for each of the 45 Tier 1 organizations. If framework language appears on an org's own website after distribution, log `secondary_dist_detected=Y`.

**(b) Social media sweep.** Once per week, run these Boolean searches:
- Twitter/X: `"democratic renewal proposal" OR "35-domain" OR "fiscal authority bypass" OR "ICE-at-polls"`
- Bluesky: Same at `bsky.app/search`
- Reddit: `site:reddit.com "democratic renewal proposal"`

Log any mention from a policy-adjacent account (verified org accounts, researchers, journalists) in `vocab_evidence_url` with platform prefix.

**(c) GitHub activity.** Set a Google Alert for `gist.github.com/[username]` to catch external links to Gist content from GitHub READMEs or research repositories. A fork or star on a repository linking to the Gists is a secondary distribution signal.

### 3.8 Overton.io — Policy Document Citation Monitoring

Register at `overton.io`. Overton indexes 21 million+ policy documents (government reports, think tank publications, NGO reports) and tracks citations. The indexing lag is 6–18 months.

Do not run Overton searches before Month 4 — they will return zero results and create false negatives. The Overton monitoring schedule:

| Month | Action |
|-------|--------|
| Month 4 (September 2026) | First search: `"democratic renewal" proposal institutional` and vocabulary markers. Record result count. |
| Month 8 (January 2027) | Second search: same queries. Compare against Month 4 baseline. |
| Month 12 (May 2027) | Third search: full vocabulary sweep. Export results for impact report. |

---

## Part 4 — Feedback Triage and Auto-Update Procedures

### Reply Categories and Routing

Every substantive email reply gets categorized and routed within 24 hours of receipt.

**Category definitions:**

| Category | Definition | Signal weight |
|----------|------------|---------------|
| Implementation Question | Contact is designing an adoption: "Can we use this in our amicus strategy?" or "Which domain covers ICE enforcement at polling sites?" | High |
| Methodology Critique | Contact challenges an analytical claim or empirical figure | Medium — engagement is substantive; critique may improve framework |
| Integration Request | Contact wants to formally adopt a domain for their toolkit: "We'd like to adapt Domain 16 for our know-your-rights training" | Very High — this is a Tier 2 pilot trigger |
| Thanks / No Action | Receipt acknowledgment with no stated next step | Low — log and wait; sector SLA still applies |
| Bounced | Permanent delivery failure | Zero for engagement; requires immediate action |

**Routing procedure:**

```
Reply received
  |
  ├── Implementation Question
  |     → Set engagement_score +1; check Tier 2 composite score
  |     → Respond within 48h (Template A, below)
  |     → Update adoption_level to 1 if not already higher
  |
  ├── Methodology Critique
  |     → Log verbatim quote in Notes; flag domain number
  |     → Note for version review cycle
  |     → Respond within 48h (Template B, below)
  |
  ├── Integration Request
  |     → ESCALATE TO USER SAME DAY
  |     → Set engagement_score=5; set adoption_level=3
  |     → User authors response within 48h (Template C, below)
  |
  ├── Thanks / No Action
  |     → Log reply_date; set engagement_score=2
  |     → Schedule check-in at sector SLA midpoint
  |     → No immediate response unless a question is embedded
  |
  └── Bounced
        → Set bounce_detected=Y; log bounce_type
        → Identify alternate contact from DISTRIBUTION_OUTREACH_CONTACTS.md
        → Send alternate contact within 72h; set alt_contact_tried=Y
```

### Response Templates

**Template A — Implementation Question**

> Thank you for reaching out about [Domain X / the framework]. The analysis you're asking about is in [Domain X, Section Y]. The most direct application for your context is [specific framing — 2 sentences].
>
> If useful, I can share [supplementary document / litigation tracker excerpt / domain update file] that connects directly to [org's current work context].
>
> Would a brief conversation be helpful? I'm available [general availability framing].

**Template B — Methodology Critique**

> Thank you for the detailed engagement with [Domain X] — this is exactly the kind of scrutiny that strengthens the analysis.
>
> On your point about [specific claim]: [either acknowledge the gap ("You're right; this will be incorporated in the next version") or provide the underlying reasoning and primary source citation].
>
> Your feedback will inform the next version of [Domain X]. Would you be open to reviewing the updated version before public release?

**Template C — Integration Request (user-authored, triggered by system flag)**

> Thank you — we're glad the [Domain X / framework] is directly useful for your work on [org's stated application].
>
> We designed the framework to be adaptable for exactly this kind of institutional application. I'd welcome a conversation to understand your specific context and make the material as useful as possible.
>
> Would you have 30 minutes in the next week? [Scheduling link or availability window]

### Leading-Indicator Alerts — Immediate Actions

| Alert trigger | Threshold | Action |
|---------------|-----------|--------|
| Day 3 bounce rate | >10% of wave (>4–5 bounces out of 45) | Halt next wave; audit contact list before proceeding |
| Day 7 zero Gist views | All sent Gists at 0 cumulative views | Check Gist URLs in sent emails; verify links not broken |
| Day 14 zero replies | 0 substantive replies from any Tier 1 org | Check spam folder; try alternate contact for top 3 orgs |
| Day 28 engagement stalled | <3 orgs at engagement_score ≥3 | Run targeted secondary outreach to 5 highest-SLA orgs with a current-event hook |
| Day 60 adoption flatline | 0 orgs at adoption_level ≥2 | Diagnose: channel problem vs. content problem; brief top 2 bridge node contacts directly |

---

## Part 5 — Weekly and Monthly Reporting Templates

### Weekly Report (run every Monday, 15–20 minutes)

**Inputs**: Gist view pull (Part 3.1) + Google Alerts review + any replies received + LegiScan alerts.

**Output format:**

```
WEEKLY ENGAGEMENT SUMMARY — Week of [DATE] (Day N from launch)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sector               | Sent | Engaged (Score ≥1) | Adopted (Score ≥4) | Tier 2 Ready
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Law Schools (15)     |  15  |  [N] ([N]%)        |  [N] ([N]%)        |  [N]
Think Tanks (11)     |  11  |  [N] ([N]%)        |  [N] ([N]%)        |  [N]
Civil Rights (12)    |  12  |  [N] ([N]%)        |  [N] ([N]%)        |  [N]
Labor Unions (4)     |   4  |  [N] ([N]%)        |  [N] ([N]%)        |  [N]
Foundations (3)      |   3  |  [N] ([N]%)        |  [N] ([N]%)        |  [N]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL (45)           |  45  |  [N] ([N]%)        |  [N] ([N]%)        |  [N]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Engaged = any signal (reply, Gist views >3, secondary dist detected)
Adopted = vocabulary or structural adoption in public output (Level 2+)

NEW THIS WEEK:
  Citation events: [N] (from: [sources])
  New replies: [N] (categories: [tally])
  Gist view spikes: [which Gists, delta count]
  New Tier 2 candidates: [org names or "none"]
  Alerts triggered: [list any leading-indicator alerts]

DOMAIN HEAT MAP UPDATE (domains with new signal this week):
  Domain [N] — [signal type] — [source org]
  Domain [N] — [signal type] — [source org]
  (none if no new signals)

NEXT WEEK ACTIONS:
  [ ] [Specific follow-up or outreach to complete]
  [ ] [Any alert responses required]
  [ ] [SLA deadline approaching for which orgs]
```

Save each weekly report as `monitoring/week-[N]-summary-[YYYY-MM-DD].md`.

### Monthly Synthesis Report

Run on the first Monday of each month. Takes 60–90 minutes.

**Inputs**: All weekly reports since last monthly synthesis + Gist view log + Citation log + all email replies received.

**Output format:**

```
MONTHLY ADOPTION SYNTHESIS — Month [N] ([DATE])
════════════════════════════════════════════════════════════════

ADOPTION SCORECARD
  Total orgs at Level 0 (no engagement):          [N] / 45
  Total orgs at Level 1 (awareness):              [N] / 45
  Total orgs at Level 2 (reference/vocabulary):   [N] / 45
  Total orgs at Level 3 (operational):            [N] / 45
  Total orgs at Level 4 (coalition):              [N] / 45

  Engagement rate (Level 1+):    [N]%
  Adoption rate (Level 2+):      [N]%
  Month-over-month delta:        [+/- N orgs at Level 2+]

CITATION EVENTS (cumulative since launch)
  Total citation events:                  [N]
  Unique citing organizations:            [N]
  Unique domains cited:                   [N] of 37
  By sector:
    Think tanks:                          [N]
    Civil rights / litigation orgs:       [N]
    Law schools / academia:               [N]
    Media:                                [N]
    Legislative (state/federal):          [N]
    AG offices:                           [N]

DOMAIN HEAT MAP — Top 5 Domains by Citation Count
  1. Domain [N] — [name] — [N] events — dominant sector: [sector]
  2. Domain [N] — [name] — [N] events — dominant sector: [sector]
  3. Domain [N] — [name] — [N] events — dominant sector: [sector]
  4. Domain [N] — [name] — [N] events — dominant sector: [sector]
  5. Domain [N] — [name] — [N] events — dominant sector: [sector]

  Domains at zero events (flag for targeted outreach if Month 3+):
  [list domain numbers]

BRIDGE NODES
  [Bridge node name] — status: [Depth 0/1/2/3] — latest output: [description or "none"]
  [Bridge node name] — status: [Depth 0/1/2/3] — latest output: [description or "none"]

FEEDBACK RECEIVED THIS MONTH
  Implementation questions:   [N]
  Methodology critiques:      [N] (domain flags: [list])
  Integration requests:       [N] (escalated to user: [Y/N])
  Thanks / no action:         [N]
  Bounces:                    [N] (resolved: [N])

FAILURE MODE AUDIT
  False adoption flags:       [N]
  Misinterpretation flags:    [N]
  Capture risk flags:         [N]
  Decay flags:                [N]

REQUIRED ACTIONS BEFORE NEXT MONTHLY SYNTHESIS
  [ ] [Specific action — who, what, by when]
  [ ] [Specific action]
  [ ] [Specific action]
```

Save each monthly synthesis as `monitoring/month-[N]-synthesis-[YYYY-MM].md`.

---

## Part 6 — Milestone Snapshots and Decision Gates

### Day 7 Operational Check

**Purpose**: Confirm monitoring infrastructure is running. Capture any fast-mover signals.

**Checklist:**
- [ ] Google Alerts delivering to dedicated folder
- [ ] Scholar Alerts confirmed active
- [ ] CourtListener saved searches created
- [ ] LegiScan saved searches configured
- [ ] All 45 Tier 1 rows populated in Master Contact Log
- [ ] Gist analytics access confirmed for all 6 canonical Gists
- [ ] Bounce check complete for Wave 1 (any Hard bounces re-routed within 72h)
- [ ] `gist_views_d7` populated for all Wave 1 orgs
- [ ] `score_d7` populated for all Wave 1 orgs

**Expected state at Day 7**: 0–2 citation events (fast-mover think tanks or journalists). Any AG substantive response within Day 7 is a strong signal. Zero citations and zero replies at Day 7 is normal — do not adjust strategy.

---

### Month 1 Assessment (Day 30)

**Purpose**: First meaningful adoption signal check.

**Required tasks:**
1. Run full weekly report protocol
2. Update Domain Heat Map — which domains have any signal
3. Run first bridge node status review — which of the priority 7 bridge nodes have engaged
4. Update `score_d14` and `score_d28` columns; calculate `score_delta`
5. Identify any Tier 2 candidates (composite score ≥7)

**Quantitative targets:**
- Substantive institutional replies: 4–8 (any tier)
- Orgs at engagement_score ≥2: 8–15
- Citation events (any type): 0–3 (low at Month 1 is normal)
- Tier 2 candidates identified: 1–3

**Decision trigger**: Zero substantive replies from ALL Tier 1 think tank contacts AND zero from ALL Tier 1 AG contacts by Day 30 is the failure signal — not zero citations. If both groups are fully silent, investigate delivery (emails to spam, Gist URL broken) before adjusting strategy.

---

### Month 3 Assessment (Day 90)

**Purpose**: First substantive adoption trajectory evaluation.

**Required tasks:**
1. Export all Google Alerts from monitoring folder since launch; categorize by sector, domain, and tier
2. Run vocabulary sweep — Google News search for each coinage from Part 1 marker list; compare against pre-distribution baseline in `phase-1-baseline-metrics.md`
3. Run first Overton search (establish baseline; no results expected; document query for comparison)
4. Update Domain Heat Map Month 3 column; flag any domain at zero
5. Run full Failure Mode Audit (Sheet 6)
6. Update all 45 Tier 1 adoption levels
7. Compile Tier 2 candidate shortlist for user review

**Quantitative targets at Month 3:**
- Citation events: 5+ across 2+ sectors
- Think tank adoption (Level 1–2): 1–3 events from Brennan Center / CAP / Protect Democracy
- Journalism adoption: 3–8 article mentions from Tier 1 network journalists
- AG adoption (any): 0–2 events (filing lags mean Month 3 is early)
- Orgs at Level 2+: 2–5

**Month 3 decision framework:**

| Pattern | Diagnosis | Action |
|---------|-----------|--------|
| Zero events in all sectors | Distribution failure, not framework failure | Investigate delivery; run secondary distribution push |
| Events in journalism only, think tanks silent | Think tanks not yet engaged | Run targeted secondary outreach with domain-specific framing |
| Events in think tanks + journalism | Normal trajectory | Continue monitoring; escalate direct outreach to AG contacts |
| Events in civil rights orgs only | Strong sector-specific penetration | Use as social proof for think tank outreach |

---

### Month 6 Assessment (Day 180)

**Purpose**: First full institutional cycle. First meaningful litigation impact assessment.

**Required tasks:**
1. Full adoption scorecard review — all 45 Tier 1 orgs
2. Litigation impact review — CourtListener search for amicus briefs and new filings; compare vocabulary against pre-distribution baseline
3. Structural convergence review — compare legislation in priority states against Domain 1, 33, 34, and 37 framework recommendations
4. Full Failure Mode Audit including 6-month decay review (any org at Level 2+ with no follow-on output in 90 days)
5. Second Overton search; compare against Month 3 baseline
6. Attribution analysis for all adoption events — apply three attribution tests (vocabulary, structural, timing) and assign `attribution_confidence`
7. Compile final Tier 2 candidate shortlist

**Quantitative targets at Month 6:**
- Orgs at Level 2+ (Reference): 5–10
- Orgs at Level 3 (Operational): 2–4
- Think tank publications incorporating framework: 2–4
- AG adoption (any confirmed use in coalition strategy or brief): 1–3
- Law school or academic engagement: 3–5 clinic directors or faculty at Level 1+
- Media pieces incorporating domain framing: 3–8
- State legislative bills with framework-aligned language: 1–3
- Court filing citations: 0–1 (aspirational; 0 is not failure at 6 months)

**Month 6 decision framework:**

| Adoption rate at Level 2+ | Diagnosis | Action |
|--------------------------|-----------|--------|
| 40%+ of Tier 1 (18+ orgs) | Strong adoption | Approve Phase 2 domain expansion; begin domain maintenance cycle for high-citation domains |
| 10–39% (4–17 orgs) | Moderate adoption | Continue current strategy; deepen engagement with adopting institutions; run targeted outreach to lagging sectors |
| <10% (0–3 orgs) | Weak adoption | Reassess distribution channel before content; run 1-on-1 briefings with 3 highest-leverage non-engaged Tier 1 contacts; diagnose messaging or channel barrier |

---

## Part 7 — Success Criteria and Milestone Targets

### Phase 1 Minimum Viable Success (6-Month Window)

All three conditions must be met:

1. **Sector penetration**: At least 3 institutional sectors show at least 1 confirmed Level 2 adoption event (vocabulary or structural adoption in published work)
2. **Bridge node activation**: At least 1 of the 7 priority bridge nodes (Brennan Center, California AG, ProPublica, Democracy Docket, ACLU, AFL-CIO, Just Security) reaches Depth 1 (published output using framework analysis)
3. **Domain coverage**: At least 5 distinct domains have generated at least 1 citation event

### Phase 1 Strong Success (12-Month Window)

| Category | 12-Month Target |
|----------|----------------|
| Total Level 1+ events | 25–40 events across all sectors |
| Level 2+ events (Reference or higher) | 10–18 events |
| Level 3 events (Operational) | 4–8 events |
| Level 4 events (Coalition) | 1–3 events |
| Bridge node cascade depth 2+ | 2–3 cascades |
| Think tank publications citing framework | 8–12 publications |
| AG coalition statements or brief citations | 2–4 references |
| Media pieces incorporating domain framing | 6–12 pieces |
| State legislative bills with framework language | 2–5 bills |
| Law review notes or academic working papers | 0–2 papers |
| Court filing citations (amicus or brief) | 0–2 citations |

### Sector-Specific Success and Failure Thresholds

| Sector | 6-Month Success | 6-Month Failure Signal |
|--------|----------------|------------------------|
| State AGs | 2–3 confirmed uses of domain material in litigation strategy or coalition statement | Zero AG substantive contact by Month 3 |
| Law schools | 3–5 clinic or faculty engagements; 1 law review inquiry | Zero law school response by Month 3 |
| Think tanks | 4–6 publication citations; 2 Level 2 adoptions | Zero think tank publication mention by Month 4 |
| Civil rights coalitions | 3–4 orgs at Level 1+; 1–2 at Level 2+ | Zero civil rights org engagement by Month 3 |
| Legislative (state) | 2–3 state bills with framework-aligned language | Zero state legislative contact by end of spring session |
| Legislative (federal) | Any Hill staff confirmation of use | No federal legislative signal before Month 6 is expected — not a failure |
| Media | 3–6 named mentions in news or opinion coverage | Zero named mentions from Tier 1 journalists by Month 6 |
| Legal (court filings) | 1 amicus brief citation | Zero court citations expected at 6 months — aspirational only |

### What Success and Failure Actually Look Like at Month 6

**Success scenario**: The Brennan Center has produced a judicial independence brief incorporating Domain 6's comparative term-limits analysis (Level 2). Just Security has published a piece citing Domain 28 or 29 (Level 1 generating credibility). One AG coalition is using Domain 1 constitutional analysis in SAVE Act litigation (Level 3). Indivisible's training materials reference the 3.5% threshold without explicit citation (Level 2 via vocabulary adoption). At least one state has moved a voting rights bill using Domain 1 model legislation language (Level 3, state legislative). Total: 6–8 confirmed adoption events at Level 2 or higher.

**Failure scenario**: At Month 6, all engagement is Level 1 only, and primarily from Tier 3 general audience. No Tier 1 think tank has incorporated the framework into published work. No AG has used domain analysis in litigation. No law school clinic has used the material in active casework. This almost always indicates a distribution problem — the right institutional contacts were not reached, or the outreach emails were filtered — rather than a content problem. Response: targeting recalibration and direct warm-referral outreach, not document revision.

**Most likely scenario (partial success)**: 2–4 domains generate genuine Tier 1 institutional adoption (particularly Domains 6, 16, 29, and 28 based on current litigation density) while the remaining domains remain at Level 0 or Level 1. This is the expected pattern — institutional adoption concentrates in domains that map to the adopting organization's current priority fight. The correct response is to use the high-adoption domains as entry points for relationship-building that eventually expands to other domains.

---

## Part 8 — Pre-Launch Checklist (Complete Before Wave 1 Sends)

- [ ] Google Sheets workbook created with all 7 sheets
- [ ] All 45 Tier 1 rows populated in Master Contact Log (from `DISTRIBUTION_OUTREACH_CONTACTS.md`)
- [ ] SLA Reference sheet populated
- [ ] `gist_url_sent` field populated per org (which Gist was linked in their email)
- [ ] GitHub analytics access verified for all 6 canonical Gists (navigate to `[GIST_URL]/analytics`; confirm view data visible)
- [ ] Pre-distribution baseline searches run and recorded in `phase-1-baseline-metrics.md`
- [ ] Google Alerts configured (15 minutes)
- [ ] Google Scholar Alerts configured (10 minutes)
- [ ] CourtListener saved searches created (20 minutes)
- [ ] LegiScan account registered and saved searches configured (30 minutes)
- [ ] Response Templates A, B, C saved in a separate doc for rapid deployment
- [ ] Dedicated email label/folder created for monitoring alerts (`monitoring/google-alerts/`)

**Estimated setup time**: 90–120 minutes, all one-time. Weekly maintenance thereafter: 20–30 minutes per week for Weeks 1–4; 15–20 minutes per week from Month 2 onward.

---

*Activation date: Day 0 = date of first Wave 1 send. All day-count references in this document are relative to that date. Save weekly reports as `monitoring/week-[N]-summary-[YYYY-MM-DD].md` and monthly syntheses as `monitoring/month-[N]-synthesis-[YYYY-MM].md` within the `projects/resistance-research/` directory. Cross-reference: `adoption-automation-infrastructure.md` (full column schema with formulas) — `adoption-tracking-dashboard-spec.md` (citation monitor tool configuration) — `post-distribution-tracking.md` (sector pathways and Week 1–4 decision trees) — `DISTRIBUTION_OUTREACH_CONTACTS.md` (full 45-org contact list) — `DISTRIBUTION_GIST_URLS.md` (canonical Gist IDs) — `phase-1-baseline-metrics.md` (pre-distribution baselines).*
