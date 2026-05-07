---
title: "Adoption Automation Infrastructure — Phase 1 Tier 1 Tracking"
date: 2026-05-07
status: production-ready
phase: Pre-launch (path decision pending)
companion_files:
  - post-distribution-adoption-framework.md     # Conceptual typology, historical precedent
  - adoption-tracking-dashboard-spec.md         # Tool specs, citation monitors, reporting cadence
  - post-distribution-tracking.md               # Real-time decision trees, Week 1–4 roadmap
  - DISTRIBUTION_OUTREACH_CONTACTS.md           # Full 45+ Tier 1 contact list
  - github-api-integration-guide.md             # Gist view tracking API reference
scope: "Operational spreadsheet schema, data collection pipeline, dashboard mockups, feedback triage, attribution protocol — execution-ready for May 8 Wave 1 launch"
---

# Adoption Automation Infrastructure
## Phase 1 — Tier 1 Tracking, 45 Organizations, 6-Month Window

**Today: May 7, 2026. Wave 1 email launches May 8 pending path decision (A / A+37 / B).**

This document builds the operational layer beneath the conceptual framework in `post-distribution-adoption-framework.md` and the tool specifications in `adoption-tracking-dashboard-spec.md`. Those documents answer "what to measure and why." This document answers "how to run it, what the spreadsheet looks like, and what to do when a signal arrives."

The 45 Tier 1 organizations span five sectors: law schools (15), think tanks (11), civil rights and litigation organizations (12), labor unions and worker organizations (4), and foundations (3 Tier 1 funders who are simultaneously distribution multipliers). The full contact list is in `DISTRIBUTION_OUTREACH_CONTACTS.md`.

---

## 1. Tier 1 Tracking Spreadsheet Architecture

### 1.1 Master Contact Sheet — Column Structure

One row per organization, not per individual contact. Where an institution has multiple contacts (e.g., Brennan Center has Wendy Weiser, Michael Waldman, and Kareem Crayton), use the primary contact's row as the canonical record and log secondary contacts in the Notes column.

**Identity Columns (populate before May 8)**

| Column | Type | Notes |
|--------|------|-------|
| `org_id` | Integer | Sequential 1–45; use for cross-sheet references |
| `org_name` | Text | Full official name |
| `org_short` | Text | Short handle used in email drafts (e.g., "Brennan Center") |
| `sector` | Dropdown | Law School / Think Tank / Civil Rights Org / Legal Services Nonprofit / Labor / Foundation |
| `sub_sector` | Text | More specific (e.g., "Election Law Clinic," "National Security Law Journal") |
| `primary_contact` | Text | Name of primary outreach recipient |
| `contact_email` | Text | Professional email — verify live before sending |
| `gist_url_sent` | URL | Which Gist URL was included in this org's email |
| `domain_focus` | Text | Primary domain numbers relevant to this org (e.g., "1, 33, 37") |

**Send-State Columns (populate as Wave 1–3 execute)**

| Column | Type | Notes |
|--------|------|-------|
| `email_sent_date` | Date (YYYY-MM-DD) | Populate on send |
| `wave_number` | Integer | 1 (May 8) / 2 (May 10–12) / 3 (May 12–17) |
| `subject_variant` | Text | A / B / C — which subject line used |
| `days_since_send` | Auto-calc | `=TODAY()-email_sent_date` |
| `respond_by_target` | Auto-calc | Sector-specific SLA: `email_sent_date + sector_sla_days` |
| `bounce_detected` | Boolean | Y / N — flag within 24h of send |
| `bounce_type` | Dropdown | Hard / Soft / None |
| `alternate_contact_tried` | Boolean | Y / N — filled if bounce=Y |

**Signal Columns (update per event, not per week)**

| Column | Type | Notes |
|--------|------|-------|
| `email_reply_received` | Boolean | Y / N |
| `reply_date` | Date | First substantive reply (not auto-ack) |
| `reply_category` | Dropdown | Implementation Question / Methodology Critique / Integration Request / Thanks-No-Action / Bounced |
| `gist_views_d7` | Integer | Cumulative Gist views at Day 7 — pulled manually from analytics tab |
| `gist_views_d14` | Integer | Cumulative views at Day 14 |
| `gist_views_d28` | Integer | Cumulative views at Day 28 |
| `secondary_dist_detected` | Boolean | Y / N — org shared the material onward |
| `secondary_dist_evidence` | Text/URL | Source of secondary distribution signal |
| `vocab_adoption_detected` | Boolean | Y / N — framework vocabulary appears in org's public output |
| `vocab_evidence_url` | URL | Link to document or search result |
| `structural_adoption_detected` | Boolean | Y / N — framework analytical structure used in output |
| `citation_detected` | Boolean | Y / N — explicit citation in published document |
| `citation_url` | URL | Link to citing document |

**Scoring Columns (recalculate at each checkpoint)**

| Column | Type | Notes |
|--------|------|-------|
| `engagement_score` | Integer 0–5 | Scoring rubric: Section 1.3 below |
| `score_d7` | Integer | Snapshot at Day 7 for trend analysis |
| `score_d14` | Integer | Snapshot at Day 14 |
| `score_delta` | Auto-calc | `=score_d14 - score_d7` — positive = momentum |
| `tier2_candidate` | Boolean | Y / N — see Section 3.3 for readiness formula |
| `adoption_level` | Integer 0–4 | 0=No engagement / 1=Awareness / 2=Reference / 3=Operational / 4=Coalition |
| `attribution_confidence` | Dropdown | High / Medium / Low / Insufficient-data |
| `next_action` | Text | Free text — what to do by when |
| `last_updated` | Date | Date of most recent row edit |

### 1.2 Auto-Calculation Fields

**Days Since Send:** `=IF(email_sent_date="","",TODAY()-email_sent_date)`

**Days to Respond By (sector-specific SLA):** Map sector to expected-response window using a lookup table on a reference sheet:

| Sector | SLA Days | Rationale |
|--------|----------|-----------|
| Legal Services / Immigration Legal Aid | 5–14 | Active docket pressure; fastest readers |
| Mutual Aid / Grassroots Organizing | 2–7 | Small staff, fast decisions |
| Think Tanks | 14–30 | Internal review cycle; publication pipeline |
| Civil Rights Litigation Orgs | 7–21 | Case-driven urgency |
| Law Schools (clinic directors) | 21–60 | Semester cycle; faculty review lag |
| Academics / Policy School Faculty | 14–42 | Research calendar dependent |
| Foundations | 30–60 | Grantmaking cycle; routing to program officers |
| Labor Unions | 21–45 | Research department review cycle |

Formula: `=email_sent_date + VLOOKUP(sector, SLA_table, 2, FALSE)`

**Score Trend:** `=IF(score_d7="","",score_d14 - score_d7)` — display as +N or -N with conditional formatting (green for positive, red for negative).

### 1.3 Engagement Score Rubric (0–5)

| Score | Condition |
|-------|-----------|
| 0 | Email sent; no signal of any kind |
| 1 | Email not bounced; Gist viewed 1+ times; no reply |
| 2 | Substantive email reply received (any category except Bounced) |
| 3 | Reply + Gist views >3 OR secondary distribution detected |
| 4 | Vocabulary or structural adoption detected in public output |
| 5 | Citation, litigation reference, curriculum integration, or formal policy proposal |

### 1.4 Data Validation Rules

**Bounce detection:** Within 24 hours of each send wave, check for undeliverable notices in the outreach email account. Set `bounce_detected=Y`, log `bounce_type` (Hard = permanent address failure; Soft = mailbox full / temporary). For any Hard bounce, set `next_action = "Find alternate contact at [org_short] within 72h"` and consult `DISTRIBUTION_OUTREACH_CONTACTS.md` for secondary contacts.

**Duplicate send prevention:** Before each wave send, run a filter on `email_sent_date` — any row with a non-empty date must not receive another send in the same wave. The `wave_number` column enforces separation.

**Response channel mapping:** Log each response type in `reply_category` using these definitions: (a) an email reply that describes a design or integration question → Implementation Question; (b) an email reply identifying a methodological problem → Methodology Critique; (c) a Gist comment → flag in Notes and copy text; (d) a social media mention → log in `vocab_evidence_url` with platform prefix (e.g., "twitter: [URL]"); (e) a GitHub fork or star of a repository linking to the Gist → log in `secondary_dist_evidence` with "github:".

### 1.5 Example Spreadsheet — 5 Organizations

The following prototype shows five representative Tier 1 organizations at Day 14 post-launch. Values are illustrative but calibrated to realistic signal rates.

| org_id | org_short | sector | email_sent_date | days_since_send | bounce | reply_cat | gist_views_d7 | gist_views_d14 | sec_dist | vocab_adopt | score_d7 | score_d14 | score_delta | tier2_candidate | adoption_level |
|--------|-----------|--------|-----------------|-----------------|--------|-----------|---------------|----------------|----------|-------------|----------|-----------|-------------|-----------------|----------------|
| 1 | Brennan Center | Think Tank | 2026-05-08 | 14 | N | Implementation Question | 12 | 31 | Y | Y | 3 | 5 | +2 | Y | 3 |
| 2 | Democracy Docket | Civil Rights Org | 2026-05-08 | 14 | N | Thanks-No-Action | 7 | 9 | N | N | 2 | 2 | 0 | N | 1 |
| 3 | Harvard Law Election Clinic | Law School | 2026-05-08 | 14 | N | (no reply) | 4 | 8 | N | N | 1 | 1 | 0 | N | 0 |
| 4 | Protect Democracy | Think Tank | 2026-05-08 | 14 | N | Integration Request | 9 | 22 | Y | N | 3 | 4 | +1 | Y | 2 |
| 5 | NAACP LDF | Civil Rights Org | 2026-05-10 | 12 | Hard | Bounced | — | — | N | N | 0 | 0 | 0 | N | 0 |

Row 1 (Brennan Center): Reply within Day 5, high Gist views, confirmed they forwarded to two program staff (secondary distribution detected), and a Brennan Center blog post published Day 12 used "fiscal authority bypass" — a framework coinage. Score jumped 2 points in week 2. Tier 2 candidate.

Row 3 (Harvard Law Clinic): No reply yet, but 8 Gist views at Day 14 suggest the material was opened. Score stays at 1 (viewed, no reply). Sector SLA is 21–60 days; no action needed until Day 21.

Row 5 (NAACP LDF): Hard bounce. Alternate contact (Janai Nelson's direct line at naacpldf.org, per `DISTRIBUTION_OUTREACH_CONTACTS.md`) should be tried within 72 hours of detecting the bounce.

---

## 2. Data Collection Pipeline

### 2.1 Email Tracking Without Embedded Pixels

Many civil rights organizations, law school networks, and government-adjacent institutions have email clients that strip or block tracking pixels by default. The Brennan Center, ACLU, and most AG-affiliated organizations fall in this category. Do not rely on pixel-based open tracking.

**Viable alternatives in order of reliability:**

**(a) Gist view statistics (primary engagement proxy).** Each domain-specific Gist linked in an outreach email accumulates view counts visible to the Gist owner at `https://gist.github.com/[username]/[GIST_ID]/analytics`. This requires being logged in as the Gist owner. Check once per week (not daily — GitHub analytics display daily counts for the prior 30 days, so weekly review captures the full picture without artificial urgency). Log cumulative totals in `gist_views_d7`, `gist_views_d14`, `gist_views_d28`.

Limitation: If a single org opens the Gist 15 times and another org never opens it, the aggregate view count is indistinguishable. To partially disambiguate, send different orgs slightly different Gist URLs when possible (e.g., the executive summary Gist vs. the full proposal Gist) — differential view trajectories across Gist IDs reveal which content is drawing engagement.

**(b) Manual reply review (highest signal, no automation needed).** An email reply is unambiguous evidence of engagement. Log all substantive replies within 24 hours of receipt. "Substantive" means any reply containing more than a generic acknowledgment — a question, a critique, a referral offer, or a request.

**(c) Google Alerts as click proxy.** Set up Google Alerts on each Gist URL (per `adoption-tracking-dashboard-spec.md` Section 1.1). If an external page links to the Gist URL, Google Alerts will flag it within 1–3 days. This captures the high-signal scenario where an organization publishes a resource page, blog post, or email newsletter citing the Gist link.

### 2.2 Gist View Tracking — Weekly Protocol

The GitHub REST API does not expose Gist view analytics programmatically (the analytics page is owner-only and not available via API endpoint). The weekly protocol is therefore manual:

1. Log in to `github.com/[username]`
2. For each canonical Gist in `DISTRIBUTION_GIST_URLS.md`, navigate to `[GIST_URL]/analytics`
3. Record the current cumulative view count in the tracking spreadsheet under the appropriate `gist_views_dN` column
4. Calculate week-over-week delta: (current count) - (prior week count) = new views this week
5. If a Gist accumulates >10 new views in a single week, flag the org(s) that were sent that Gist URL for a follow-up check

The six canonical Gists to track:
- Proposal Gist (`2dec7fd03b08ab5b41c55d402f44c261`)
- Executive Summary Gist (`2869da6eaeb15a47246ade3bbbc4a3f4`)
- Litigation Tracker Gist (`418d51bda087f15a04d685ab171a5ee0`)
- First Amendment Tracker Gist (`10d0a86e386e6c3c11c3830295a6503c`)
- Environmental Rollbacks Gist (`87e2bdb931b77480e56a08044c567bc4`)
- Police Consent Decrees Gist (`1f5cb28527c98d12526c14302c725731`)

Domain 37 Gist: record ID in `DISTRIBUTION_GIST_URLS.md` once created.

### 2.3 Secondary Distribution Detection

**Institutional website scanning:** Run a Google search once per week using the pattern `site:[org-domain] "democratic renewal"` OR `site:[org-domain] "fiscal authority bypass"` (or any framework coinage from the vocabulary marker list). If an org's website now contains framework language that it did not contain pre-distribution, that is secondary distribution confirmation. Log in `secondary_dist_detected=Y` and capture the URL.

**GitHub activity monitoring:** Watch for forks or stars on any repository that links to the Gists. Set up a Google Alert for `gist.github.com/[username]` to catch external links to Gist content from GitHub READMEs, research repositories, or org-managed code repositories.

**Social media search:** Run a weekly Boolean search on Twitter/X using `"democratic renewal proposal" OR "35-domain" OR "fiscal authority bypass" OR "ICE-at-polls"`. The same search on Bluesky (bsky.app/search) and Reddit via `reddit.com/search?q="democratic renewal proposal"`. Log any mention from a policy-adjacent account (verified org accounts, researchers, journalists) in `vocab_evidence_url`.

**Overton.io sweep:** Beginning at Month 4 post-launch, run a monthly Overton search for framework coinages in think tank and NGO publications. Overton indexes with a 6–18 month lag, so Month 4 is the earliest point where new citations could appear.

### 2.4 Citation Discovery — Automated Weekly Searches

Run these searches on Monday of each week. Log any new results in the adoption scorecard and in the citation monitor folder.

| Tool | Search Query | What It Catches |
|------|-------------|-----------------|
| Google News | `"democratic renewal proposal" OR "35-domain democratic"` | Journalism, blog posts, org websites |
| Google Scholar | `"democratic renewal proposal" institutional` | Academic working papers (6–18 month lag) |
| CourtListener | `"democratic renewal" OR "ICE at polls" OR "NVRA quiet period"` | Federal court filings, amicus briefs |
| LegiScan | Saved searches from `adoption-tracking-dashboard-spec.md` Section 1.5 | State legislative bills using framework language |
| Congress.gov | `"voter roll" SAVE 2026` / `"fiscal authority bypass"` | Federal bill text |

### 2.5 Feedback Intake Triage

All email replies should be read within 24 hours and logged using this intake sequence:

1. Assign `reply_category` from the five-category taxonomy (Section 4 below)
2. Update `engagement_score` based on the revised rubric
3. Trigger routing action (Section 4.2)
4. If the reply contains a question, draft a response within 48 hours using templates in Section 4.3
5. Log date and summary of outbound response in `notes` column

---

## 3. Dashboard Mockups

### 3.1 Weekly Engagement Summary — Sector View

Updated weekly (Monday morning, before sending any new outreach). Five rows correspond to the five sectors in the 45-org Tier 1 universe.

```
WEEKLY ENGAGEMENT SUMMARY — Week of [DATE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sector              | Sent | Opened/Engaged | Adopted Signal | Tier 2 Ready
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Law Schools (15)    |  15  |   4 (27%)      |  1 (7%)        |  1
Think Tanks (11)    |  11  |   7 (64%)      |  3 (27%)       |  3
Civil Rights (12)   |  12  |   5 (42%)      |  2 (17%)       |  2
Labor Unions (4)    |   4  |   2 (50%)      |  0 (0%)        |  0
Foundations (3)     |   3  |   2 (67%)      |  1 (33%)       |  1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL (45)          |  45  |  20 (44%)      |  7 (16%)       |  7
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Opened/Engaged" = any signal: reply, Gist views >3, secondary dist detected
"Adopted Signal" = engagement_score >= 4 (vocab or structural adoption in public output)
"Tier 2 Ready" = readiness score >= 7 (see Section 3.3)
```

### 3.2 Sector-Specific Success Signals

Expected response timing and what counts as adoption proof, by sector:

```
SECTOR SUCCESS SIGNAL REFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sector               | Response Window | Adoption Proof Types
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Law Schools          | 21–60 days      | Curriculum mention (syllabus), clinic
(clinic directors)   |                 | case strategy incorporating domain
                     |                 | analysis, faculty publication cite
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Immigration          | 5–14 days       | Litigation brief using domain
Legal Aid            |                 | argument structure, know-your-rights
                     |                 | material using framework vocabulary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mutual Aid /         | 2–7 days        | Secondary distribution to chapters,
Grassroots Orgs      |                 | member education material using
                     |                 | framework analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Think Tanks          | 14–30 days      | Published report citing framework,
                     |                 | blog post, testimony, secondary
                     |                 | distribution to grantees or networks
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Academics /          | 14–42 days      | Working paper citation, course
Policy Faculty       |                 | syllabus inclusion, public lecture
                     |                 | reference, research agenda shift
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Civil Rights         | 7–21 days       | Litigation strategy adoption, public
Litigation Orgs      |                 | position statement using domain
                     |                 | language, amicus brief structure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Labor Unions         | 21–45 days      | Incorporation into member education,
                     |                 | testimony before Congress or state
                     |                 | legislature, public campaign adoption
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3.3 Tier 2 Candidate Identification — 3-Factor Readiness Score

Three factors each scored 0–5; threshold for Tier 2 candidacy is a composite score of 7 or higher.

**Factor 1 — Engagement Depth (0–5):** `engagement_score` from the master tracking sheet. A score of 4 or 5 here is a prerequisite for Tier 2 candidacy.

**Factor 2 — Integration Signal Strength (0–3):**
- 0: No integration signal
- 1: Vocabulary adoption detected (framework coinages appearing in org output)
- 2: Structural adoption detected (framework analytical structure in published work)
- 3: Cited / piloted / integrated (formal citation, active pilot, or stated integration into org toolkit)

**Factor 3 — Network Multiplier (0–2):**
- 0: Organization's output reaches primarily internal stakeholders
- 1: Sector influence — organization's publications reach peer institutions (medium bridge node)
- 2: High-velocity distribution — organization actively distributes to networks of 10+ downstream organizations (primary bridge node: Brennan Center, ACLU, AFL-CIO, NAACP)

**Composite formula:** Factor1 + Factor2 + Factor3. Score ≥ 7 = Tier 2 candidate. Score ≥ 9 = immediate Tier 2 outreach trigger (offer 1-on-1 briefing call within 48 hours).

### 3.4 Leading-Indicator Alerts

These thresholds trigger named actions, not just documentation:

| Alert | Threshold | Action |
|-------|-----------|--------|
| Day 3 bounce rate | >10% of wave (e.g., >5 bounces out of 45) | Halt Wave 2; audit contact list before proceeding |
| Day 7 zero open/engage | Gist views = 0 across all sent Gists | Check Gist URLs in sent emails; verify links not broken |
| Day 14 zero replies | 0 substantive replies from any Tier 1 org | Check spam folder; try alternate contact for top 3 orgs |
| Day 28 engagement stalled | <3 orgs at engagement_score ≥ 3 | Run targeted secondary outreach to 5 highest-SLA orgs with a triggering current event prompt |
| Day 60 adoption flatline | 0 orgs at adoption_level ≥ 2 | Diagnose: channel problem vs. content problem; brief top 2 bridge node contacts directly |

### 3.5 Monthly Evolution Chart

Six-month adoption curve by sector. X-axis milestones: Day 0 / Day 7 / Day 14 / Day 28 / Day 60 / Day 90 (Month 3) / Day 180 (Month 6). Y-axis: mean engagement score per sector (0–5 scale, averaged across all orgs in sector).

```
SECTOR ADOPTION CURVES — Projected (Day 0 baseline; fill in as actuals accumulate)

Score
  5 |                                              ....TT
    |                                          ..TT
  4 |                                      ..CR
    |                              ....TT.CR
  3 |                          ..TT
    |                   LS..CR.
  2 |               TT.CR
    |           LS.TT
  1 |       LS.
    |  ALL
  0 +--+----+----+------+--------+-----------+---------> Days
     D0  D7  D14  D28    D60       D90         D180

TT = Think Tanks  CR = Civil Rights Orgs  LS = Law Schools
(Labor and Foundations not shown for clarity; Labor tracks ~2 weeks behind Think Tanks)

Interpretation:
- Think tanks are expected to show the steepest early curve (fastest publication cycle)
- Civil rights orgs close the gap by D60 as litigation signals accumulate
- Law schools lag until D60–D90 (semester cycle) then accelerate toward curriculum integration
- D180 is the first realistic point to assess law school adoption level ≥ 2
```

---

## 4. Feedback Triage Workflow

### 4.1 Five Reply Categories — Definitions and Signal Weight

**(a) Implementation Question** — The contact is designing an adoption. Examples: "Can we use this analysis in our amicus strategy?", "Which domain covers ICE enforcement at polling sites most directly?", "Is there a version of this formatted for litigation teams?" Signal weight: **High**. This contact has moved from awareness to active use; they are working with the framework, not just reading it.

**(b) Methodology Critique** — The contact challenges an analytical claim, empirical figure, or prescriptive recommendation. Examples: "The Section 3 analysis in Domain 37 doesn't account for the procedural posture of Couy Griffin," "Your impoundment framework overstates OMB's discretion post-Hein." Signal weight: **Medium** — engagement is substantive, and the critique may improve the framework for Tier 2 distribution. Do not interpret critique as rejection.

**(c) Integration Request** — The contact wants to customize or formally adopt a domain for their organizational toolkit. Examples: "We'd like to adapt the Domain 16 framework for our know-your-rights training," "Can we use the electoral interference analysis as the basis for a Brennan Center brief?" Signal weight: **Very High** — this is the Tier 2 pilot trigger. Escalate to user within 24 hours.

**(d) Thanks / No Action** — Receipt acknowledgment with no stated next step. Examples: "Thank you for sharing, I'll look at this when I have a chance," "This looks interesting." Signal weight: **Low**. Log and wait; sector SLA still applies. These contacts may re-emerge once they have processed the material.

**(e) Bounced** — Permanent delivery failure. Signal weight: **Zero for engagement; requires immediate action.** Hard bounces need alternate contact within 72 hours. Log and reroute.

### 4.2 Routing Logic

```
Reply received
     |
     ├── Category: Implementation Question
     |       → Log score +1; check Tier 2 readiness score; if ≥ 7 add to Tier 2 candidate list
     |       → Respond within 48h with Implementation Template (Section 4.3a)
     |
     ├── Category: Methodology Critique
     |       → Log in Notes column with verbatim quote; flag domain number
     |       → Note for version review cycle (Section 4.2 of post-distribution-adoption-framework.md)
     |       → Respond within 48h with Critique Response Template (Section 4.3b)
     |
     ├── Category: Integration Request
     |       → ESCALATE TO USER IMMEDIATELY (same day)
     |       → Log score at maximum 5; update adoption_level to 3
     |       → User offers 1-on-1 conversation within 48h using Integration Template (Section 4.3c)
     |
     ├── Category: Thanks / No Action
     |       → Log reply_date; update engagement_score to 2
     |       → Schedule check-in at sector-SLA midpoint
     |       → No immediate response required unless a question is embedded
     |
     └── Category: Bounced
             → Set bounce_detected=Y; log bounce_type
             → Identify alternate contact within org from DISTRIBUTION_OUTREACH_CONTACTS.md
             → Send alternate contact email within 72h; log in alternate_contact_tried column
```

### 4.3 Response Templates

**Template A — Implementation Question Response**

> Thank you for reaching out about [Domain X / the framework generally]. The analysis you're asking about [specific question context] is in [Domain X, Section Y]. The most direct application for your context would be [specific framing — 2 sentences].
>
> If it's useful, I can share [supplementary document / the domain update file / the litigation tracker excerpt] that connects directly to [org's current work context].
>
> Would a brief conversation be helpful to work through the application? I'm available [general availability framing].

**Template B — Methodology Critique Response**

> Thank you for the detailed engagement with [Domain X] — this is exactly the kind of scrutiny that strengthens the analysis.
>
> On your point about [specific claim]: [either acknowledge the gap with gratitude ("You're right that the Domain X analysis doesn't account for [X]; this will be incorporated in the next version") or explain the underlying reasoning if the critique rests on a misreading ("The [claim] is based on [specific source] — here is the precise citation and context")].
>
> Your feedback will inform the next version of [Domain X]. Would you be open to reviewing the updated version before public release?

**Template C — Integration Request / Tier 2 Escalation** (drafted by user, not the tracking system)

This template is conversation-specific; the tracking system flags the reply for the user to handle directly. The flag message to the user is: "TIER 2 TRIGGER — [org_short] has requested integration. Recommend user-authored response within 48 hours offering a direct conversation. Draft response attached as Template C baseline."

> Thank you — we're glad the [Domain X / framework] is directly useful for your work on [org's stated application].
>
> We designed the framework to be adaptable for exactly this kind of institutional application. I'd welcome a conversation to understand your specific context and make sure the material is as useful as possible for [org's purpose].
>
> Would you have 30 minutes in the next week? [Scheduling link or availability window]

---

## 5. Attribution Measurement

### 5.1 Three Operative Attribution Tests

The full attribution methodology is in `post-distribution-adoption-framework.md` Section 5. For operational tracking, three tests are sufficient to classify each adoption event.

**Test 1 — Vocabulary Marker Test.** Each domain contains 3–4 signature coinages that distinguish framework-derived analysis from independent parallel work. Example vocabulary markers by domain:

- Domain 1 / 37: "NVRA quiet period," "ICE-at-polls," "SAVE database voter roll purge"
- Domain 6 / 33: "appellate capture," "state legislative autocratization," "REDMAP 2.0 pipeline"
- Domain 16: "warrantless arrest escalation pattern," "pattern-and-practice enforcement escalation"
- Domain 34: "fiscal authority bypass," "OMB apportionment abuse," "pocket rescissions"

**Protocol:** Before distribution, run baseline Google searches for each coinage. Record zero-count or near-zero-count results. Post-distribution, if an institutional document uses a coinage that had <5 pre-distribution occurrences and the document was published after the organization received the framework, flag `vocab_adoption_detected=Y`. This is a strong attribution signal.

**Test 2 — Structural Convergence Test.** Does the organization's output use the framework's analytical structure, not just its conclusions? The signature structural patterns: Domain 34's four-mechanism fiscal bypass taxonomy (OMB apportionment → agency holds → Treasury interference → pocket rescissions), Domain 33's four-mechanism state autocratization sequence (REDMAP 2.0 → state court capture → ballot initiative suppression → voter suppression escalation), Domain 37's three-track interference model (administrative, legal, operational). If an organization's published work uses the same multi-mechanism taxonomy in the same sequence, log `structural_adoption_detected=Y`.

**Test 3 — Timing and Contact Test.** Did the institutional output appear within 30 days of confirmed first contact? Combined with vocabulary or structural adoption evidence, timing-plus-contact establishes prima facie attribution. For outputs appearing 30–90 days post-contact, the attribution confidence is "Medium." Beyond 90 days, independent parallel development becomes more plausible and confidence drops to "Low" unless vocabulary or structural markers are present.

### 5.2 Counterfactual Baseline Protocol

Before distributing Wave 1 on May 8, run and record the following baseline searches. Store results in `phase-1-baseline-metrics.md`.

1. Google News search for each vocabulary marker — record result count (expected: 0–2 for novel coinages)
2. Google Scholar search for `"democratic renewal proposal"` — record result count
3. CourtListener full-text search for each litigation-relevant coinage — record result count
4. Brennan Center, Protect Democracy, Democracy Docket publication archives — record last publication date for any content addressing framework-equivalent topics

These baselines serve as the zero-line for attribution. Any post-distribution result that exceeds the baseline by a statistically significant margin, combined with documented contact, constitutes a contribution claim (not a causation claim, per the attribution language guidance in `post-distribution-adoption-framework.md` Section 5.4).

**Control group approximation:** Identify 5–8 organizations in each sector that are NOT in the Tier 1 distribution list but work on the same domain areas (e.g., state-level legal aid organizations, smaller think tanks). Run the same vocabulary searches against their published output at Day 90 and Day 180. If vocabulary marker usage is near-zero in the control group and measurable in the Tier 1 group, the gap supports a contribution claim.

---

## 6. Implementation Roadmap

### Week 1 (May 1–7, Pre-Launch)

- [ ] Build tracking spreadsheet from schema in Section 1 (Google Sheets; share link with user)
- [ ] Populate all 45 Tier 1 rows with org_name, sector, contact_email, gist_url_sent, domain_focus from `DISTRIBUTION_OUTREACH_CONTACTS.md`
- [ ] Verify GitHub Gist analytics access (navigate to `[GIST_URL]/analytics` for each of the six canonical Gists; confirm view data is visible)
- [ ] Run pre-distribution baseline searches (Section 5.2); log results in `phase-1-baseline-metrics.md`
- [ ] Set up Google Alerts for vocabulary markers and Gist URLs (per `adoption-tracking-dashboard-spec.md` Section 1.1)
- [ ] Set up CourtListener saved searches (5 searches on free tier)
- [ ] Configure LegiScan API saved searches for priority states
- [ ] Prepare response templates A/B/C in a separate doc for rapid deployment

### Week 2 (May 8–14, Wave 1 Launch)

- [ ] Send Wave 1 (all 45 Tier 1 contacts or per path decision batch sequence)
- [ ] Monitor for bounces hourly for first 24 hours; log and reroute any Hard bounces within 72h
- [ ] Day 3 bounce rate check: if >10% (>4 bounces), halt Wave 2 pending list audit
- [ ] Begin daily reply monitoring; triage within 24 hours of receipt
- [ ] Day 7 Gist view pull: log cumulative views for each canonical Gist; populate `gist_views_d7` for each relevant org
- [ ] Day 7 engagement summary: populate score_d7; run leading-indicator alert check

### Weeks 3–6 (May 15 – June 11)

- [ ] Weekly Gist view pull (Monday morning; log `gist_views_d14`, `gist_views_d28`)
- [ ] Weekly Google Alerts review; log any citation events in adoption scorecard
- [ ] Weekly vocabulary marker search (Tuesday); log any new usage
- [ ] Day 14 score_d14 population; calculate score_delta for all 45 orgs
- [ ] Day 28 engagement summary: first sector-level aggregate dashboard
- [ ] Identify any Tier 2 candidates (composite score ≥ 7); escalate to user for 1-on-1 outreach
- [ ] Run secondary distribution search (Section 2.3) on institutional websites for all 45 orgs

### Weeks 7–26 (June 12 – November 6, Monthly Cadence)

- [ ] Monthly engagement summary dashboard update (first Monday of each month)
- [ ] Month 3 (August 8): full sector assessment per `adoption-tracking-dashboard-spec.md` Month 3 Snapshot; first Overton search run (establish baseline; no adoption results expected yet)
- [ ] Month 3: domain heat map update; flag any domain at zero across all 45 orgs for re-framing decision
- [ ] Month 4 (September): first Overton search likely to return results; log and compare to baseline
- [ ] Month 6 (November 8): full 6-month evaluation per `adoption-tracking-dashboard-spec.md` Month 6 Snapshot
- [ ] Month 6: run attribution analysis for each confirmed adoption event (three-test protocol, Section 5.1); assign attribution_confidence for all orgs at adoption_level ≥ 2
- [ ] Month 6: compile Tier 2 candidate shortlist for Phase 2 distribution decision

---

## Appendix: Spreadsheet Sheet Structure

| Sheet name | Contents |
|------------|----------|
| `Master Contact Log` | All 45 Tier 1 orgs, full column schema from Section 1.1 |
| `SLA Reference` | Sector-to-SLA mapping table for auto-calc fields |
| `Gist View Log` | Weekly Gist view counts for all 6 canonical Gists; delta calculations |
| `Citation Log` | One row per citation event; columns: date, source org, document URL, domain cited, test passed (vocab/structural/timing) |
| `Failure Mode Log` | From `adoption-tracking-dashboard-spec.md` Component 4 |
| `Domain Heat Map` | Domain × Month grid; cell value = citation event count |
| `Baseline Metrics` | Pre-distribution search results (Section 5.2 baseline); updated at Month 3, Month 6 |
| `Tier 2 Candidates` | Filtered view of Master Contact Log where tier2_candidate=Y; composite readiness score |

All sheets should be in a single Google Sheets workbook shared between the user and any distribution support staff. Sheet-level permissions: Failure Mode Log and Tier 2 Candidates are restricted to user only; all others can be read by distribution staff.

---

*Companion documents: `post-distribution-adoption-framework.md` (conceptual typology, historical precedent, attribution methodology) — `adoption-tracking-dashboard-spec.md` (citation monitors, tool setup, reporting cadence) — `post-distribution-tracking.md` (Week 1–4 real-time decision trees) — `DISTRIBUTION_OUTREACH_CONTACTS.md` (full Tier 1 contact list) — `github-api-integration-guide.md` (Gist API reference, view analytics access).*
