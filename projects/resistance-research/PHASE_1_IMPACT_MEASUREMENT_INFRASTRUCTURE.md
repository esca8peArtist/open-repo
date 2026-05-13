---
title: "Phase 1 Impact Measurement Infrastructure"
subtitle: "Real-Time Success/Failure Detection for Democratic Renewal Framework Distribution"
created: 2026-05-13
version: 1.0
status: production-ready
phase: Phase 1 (arm May 31, live June 1 with first send wave)
scope: >
  End-to-end measurement infrastructure for Phase 1 distribution across all channels:
  email tracking, GitHub/Gist analytics, policy uptake monitoring, coalition tracking,
  real-time dashboards, success thresholds, contingency triggers, and cross-project integration.
relationship-to-existing-docs: >
  This document is the operational dashboard layer. The conceptual architecture
  (adoption levels, attribution methodology, sector SLAs) lives in
  phase-1-adoption-tracking-automation.md. The Google Sheets column schema
  lives in adoption-automation-infrastructure.md. This document provides
  copy-paste setup instructions, formulas, Discord webhook config, and
  trigger-based contingency protocols NOT covered by the existing infrastructure.
  Do not duplicate those documents — cross-reference them.
---

# Phase 1 Impact Measurement Infrastructure
## Real-Time Success/Failure Detection — Democratic Renewal Framework

**Version 1.0 — May 13, 2026**

**Lead finding**: The first 7 days after Wave 1 sends are the highest-diagnostic period in Phase 1. Early signal patterns — bounce rates, Gist view velocity, reply timing — predict the 30-day and 90-day trajectories with high fidelity. This document builds the system that captures those signals automatically, surfaces anomalies within 24 hours, and routes them to actionable contingency protocols. Arm it May 31 evening. Activate it June 1 morning when the first email goes out.

---

## Relationship to Existing Infrastructure

Three documents already contain the measurement conceptual architecture for resistance-research Phase 1. **Read them before this document**. This document does not re-explain what they cover — it builds on top of them:

- `execution/phase-1-adoption-tracking-automation.md` — 5-level adoption scale, 7-sheet Google Sheets schema, weekly/monthly report templates, sector SLA table, 30/90/180-day decision gates
- `execution/adoption-automation-infrastructure.md` — Full column schema with auto-calc formulas for the Master Contact Log
- `execution/success-metrics.md` — Tier 1/2/3 engagement metrics, 30-day and 90-day checkpoint assessments, diagnostic protocols

**What those documents do not cover** (covered here):
- Bitly link setup and daily click extraction for resistance-research
- Gmail label automation via Zapier with reply categorization
- Real-time Gist spike detection (automated, not manual)
- Domain 42 DEA-specific participation tracking (docket monitoring, June 22 participant list)
- Discord webhook daily briefing (setup, payload format, anomaly alerts)
- Congress.gov keyword monitoring (new — not in existing docs)
- Cross-project integration metrics (cybersecurity-hardening, seedwarden, Domain 42)
- Contingency trigger protocols (trigger-based, not subjective)

---

## Section 1: Email Reply Tracking Infrastructure

### 1.1 Bitly Link Setup

**Purpose**: Click tracking as the primary engagement proxy. Email open tracking is unreliable (Apple Mail Privacy Protection inflates opens; institutional mail servers strip pixels). Bitly click data is the cleaner signal.

**Time required**: 15 minutes one-time.

**Setup steps**:

1. Go to `bitly.com`. Create a free account. The free tier supports unlimited links and daily analytics.

2. Create one Bitly link per major Gist distributed in Phase 1. Using separate links per Gist (not per contact) gives you content-level analytics without fragmenting click data:

| Gist | Recommended Back-Half | Destination URL |
|------|-----------------------|-----------------|
| Democratic Renewal Proposal | `bit.ly/drp-2026` | `https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261` |
| Executive Summary | `bit.ly/drp-summary` | `https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4` |
| Litigation Tracker | `bit.ly/drp-litigation` | `https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0` |
| First Amendment Tracker | `bit.ly/drp-fa` | `https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c` |
| Domain 42 DEA Briefing | `bit.ly/drp-dea42` | `https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab` |

3. For each link: After creating it, open a private/incognito browser, paste the short URL, verify the Gist loads, then return to Bitly dashboard and confirm the click registered within 60 seconds.

4. Replace all raw Gist URLs in email templates with the corresponding Bitly short links before any Wave 1 send.

**Daily click extraction** (5 minutes, every morning during Weeks 1–4):

1. Log in to `bitly.com/a/dashboard`.
2. The dashboard shows each link with daily click counts and cumulative totals.
3. Record the daily delta (today's total minus yesterday's total) in the Google Sheets "Gist View Log" sheet under the `bitly_clicks_daily` column.
4. If any link shows a single-day spike >5 clicks: flag in the sheet (`spike_flag=YES`) and cross-reference the timing against which Wave was sent most recently. Referrer data (Bitly shows this on paid tier; on free tier, note geographic concentration from the country breakdown) is a secondary forward-signal.

**Key limitation**: Bitly free tier shows aggregate clicks per link, not per-contact attribution. A `.gov` or `.edu` domain appearing in referrer data (visible even on free tier) is a strong institutional engagement signal. Note these manually in the Master Contact Log `notes` field.

**When to upgrade**: If click counts exceed 100 in Week 1, upgrade to Bitly Starter ($8/month) for contact-level UTM attribution. Below 100 clicks, free tier is sufficient.

### 1.2 Gmail Label Structure and Reply Routing

**Purpose**: Route all Phase 1 replies automatically to labeled folders so the Master Contact Log can be updated without scanning your entire inbox.

**Setup** (8 minutes):

In Gmail, create the following nested label structure via Settings → Labels → Create new label:

```
phase1-outreach/
  ├── sent/
  │   ├── wave-1
  │   ├── wave-2
  │   └── wave-3
  ├── replies/
  │   ├── substantive
  │   ├── auto-ack
  │   ├── bounce
  │   └── forward-detected
  └── monitoring/
      ├── google-alerts
      └── courtlistener-alerts
```

**Manual labeling on send**: When you send each Wave email, immediately apply the label `phase1-outreach/sent/wave-1` (or wave-2/wave-3). This allows filtering by wave when auditing non-responders.

**Reply routing via Zapier** (30 minutes, one-time):

Zapier free tier supports 5 Zaps (automated workflows). Use two Zaps for email:

**Zap 1 — Incoming reply logger**:
- Trigger: Gmail — New Email Matching Search
- Search query: `in:inbox label:phase1-outreach/sent`
- Action: Google Sheets — Append Row in the "Master Contact Log" sheet
- Row data: `{{sender_email}} | {{subject}} | {{date}} | REPLY_RECEIVED | [leave reply_category blank for manual categorization]`

**Zap 2 — Bounce detector**:
- Trigger: Gmail — New Email Matching Search
- Search query: `from:(mailer-daemon OR postmaster) subject:(delivery failed OR undeliverable OR bounce)`
- Action: Google Sheets — Append Row in the "Failure Mode Log" sheet
- Row data: `{{date}} | BOUNCE | {{original_recipient}} | [to be resolved within 72h]`

**Reply categorization** (manual, takes 2 minutes per reply):

When a reply arrives, open it, read it, apply one of the four labels, and update the Master Contact Log `reply_category` column with one of these values (definitions from `phase-1-adoption-tracking-automation.md` Part 4):

| Gmail Label | Spreadsheet Value | Definition |
|-------------|-------------------|------------|
| `replies/substantive` | `Implementation Question` or `Integration Request` | Any reply with a question, critique, or stated intent to use |
| `replies/auto-ack` | `Thanks / No Action` | "Received" with no content, vacation reply, generic acknowledgment |
| `replies/bounce` | `Bounced` | Permanent delivery failure |
| `replies/forward-detected` | `Forward Detected` | Reply from a contact you did not email, indicating a Tier 1 contact forwarded |

**Escalation rule for Integration Requests**: If any reply is an Integration Request ("we'd like to use this in our work"), do not reply yourself — flag it in the spreadsheet `next_action` column as "USER RESPONSE REQUIRED — 48h" and notify via Discord (see Section 5).

### 1.3 Email Open Rate Aggregation

Gmail does not natively track opens. The Bitly click data is the more reliable proxy. However, if you use a bulk email platform for any sub-component of distribution (e.g., Substack posts count as a mass email channel), those platforms provide open rate data directly.

**Substack open rates**: Available in the Substack dashboard under each post's analytics. Aggregate across posts in the Google Sheets "Substack Metrics" tab (see Section 5.1). Target: 35%+ open rate. If below 25%, treat as a signal to shorten future posts and strengthen subject lines.

**Individual Gmail sends**: Open tracking for individual Gmail sends is available via the Streak CRM extension (free tier, Gmail extension). Install from `streak.com/streak-for-gmail`. Streak adds a "viewed" indicator to sent emails. Note: tracking pixels are blocked by many institutional mail servers (law schools, AG offices, federal agencies). A "not viewed" indicator is not evidence of non-engagement — it may simply mean the pixel was blocked. Do not use Streak open data as a primary metric; use it only to confirm engagement when combined with Bitly clicks.

**Unsubscribe rate monitoring**: Substack tracks unsubscribes per post. If any single post generates >3 unsubscribes (>5% of subscriber base for a list under 60 subscribers, or >3% for a list above 100), that is an anomaly requiring review. Log in the "Failure Mode Log" under failure_mode=`Decay`. See Section 7, Contingency Trigger 4 for the unsubscribe escalation protocol.

---

## Section 2: GitHub/Gist Impact Metrics

### 2.1 Gist View Tracking — Existing Infrastructure Extension

The existing `phase-1-adoption-tracking-automation.md` Section 3.1 documents the weekly manual Gist pull procedure. This section adds three enhancements: (a) the Bitly layer as a more reliable click signal, (b) a GitHub star tracking protocol for the linked repository (if any), and (c) a spike-notification system via Discord.

**Weekly Gist pull procedure** (10 minutes, every Monday — from existing doc, confirmed):

1. Log in to `github.com` as the Gist-owner account (`esca8peArtist`).
2. For each of the 6 canonical Gists, navigate to `https://gist.github.com/esca8peArtist/[GIST_ID]/analytics`.
3. The analytics tab shows daily view counts for the prior 14 days.
4. Record the current cumulative total in Google Sheets "Gist View Log" sheet column `week_N_cumulative`.
5. The `week_N_delta` formula auto-calculates. If delta >10 in a single week, set `spike_flag=YES` and trigger the Discord spike notification (see Section 5.2).

**Enhanced tracking: Gist fork detection**:

GitHub does not provide fork notifications for Gists via email. Check manually during the weekly pull:

For each canonical Gist, in the analytics tab, look for the "Forks" count (shown at the top of the Gist page alongside Stars). A fork indicates someone has copied the Gist to their own GitHub account — a strong downstream adoption signal.

Record in Google Sheets "Gist View Log" sheet column `fork_count_week_N`. A fork from an organization's official GitHub account (e.g., `brennancenter`, `aclu-org`) is a Level 3 adoption event — log it in the Citation Log immediately.

**Gist star tracking**:

A Gist star indicates a public "this is worth saving" signal from a GitHub user. Check the star count during the weekly pull and record in column `star_count_week_N`. Stars from GitHub accounts associated with policy organizations, law schools, or journalists are qualitatively more significant than anonymous stars.

To identify star owners: click the star count number on the Gist page; GitHub shows all users who starred that Gist. Scan for `.edu` accounts, organizational handles, or recognizable researcher names. Log any significant star in the Citation Log with `detection_source=GitHub Star`.

**Domain 42 DEA Gist — separate tracking**:

The Domain 42 DEA Gist (`https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab`) operates on a different timeline and success metric than the main distribution Gists. Track it in a separate row in the "Gist View Log" sheet. The key milestone dates are:

- May 28: Views in the 72 hours before the deadline = organizations actively reviewing the material before filing
- June 22: DEA publishes the designated participant list. Search the list for any organization that received Domain 42 outreach. Log confirmed participants in the "Citation Log" as `adoption_level=3` (Operational)

### 2.2 GitHub Traffic Referrer Analysis

GitHub provides referrer data for Gists (who linked to this Gist — i.e., what site brought traffic here). Check this during the weekly pull:

Navigate to each Gist analytics page. The "Referring sites" section shows external domains sending traffic. Common high-value referrers:
- `reddit.com` — the Reddit distribution is working
- `twitter.com` or `x.com` — the social media distribution is working
- `courtlistener.com` — a legal filing or docket entry linked to the Gist
- Any `.gov` domain — government staff engaged
- Any known policy organization domain — institutional adoption signal

Record top referrers in the "Gist View Log" sheet `top_referrers_week_N` column. Any `.gov` or `.edu` referrer appearing for the first time should be noted in the Master Contact Log for the most likely corresponding contact.

### 2.3 Issue and Discussion Traffic

The 6 canonical Gists are read-only (Gists do not have Issues). However, if any content is also posted to a GitHub repository, monitor the Issues and Discussions tabs. For the current Gist-only distribution, the equivalent community engagement signals are:

- Gist comments (GitHub allows comments on Gists — check the comments section during weekly pull)
- External Reddit threads or Hacker News posts linking to the Gists (picked up by Google Alerts and referrer data)
- GitHub Gist forks with public comments added in the fork

Any comment on a canonical Gist is a high-value engagement signal. Reply within 48 hours to any substantive comment.

---

## Section 3: Policy Uptake Monitoring

### 3.1 CourtListener Docket Monitoring

**Setup** (20 minutes, one-time; from existing doc — reproduced here with Domain 42 additions):

At `courtlistener.com`, create saved searches with email alerts enabled. The free tier supports 5 alert-enabled saved searches:

| Search # | Query | Scope | Expected First Results |
|----------|-------|-------|------------------------|
| 1 | `"democratic renewal proposal" OR "35-domain democratic"` | All federal courts | Month 3–6 (citation lag) |
| 2 | `"ICE at polls" OR "NVRA quiet period" OR "SAVE database" voter roll` | All federal courts | Month 1–3 (Domain 1 litigation dense) |
| 3 | `"appellate capture" OR "fiscal authority bypass" OR "state legislative autocratization"` | All federal courts | Month 2–6 |
| 4 | `DEA-1362 "marijuana" "democratic" OR "disenfranchisement" OR "civil rights"` | All federal courts + DEA administrative docket | Week 1–4 (DEA-specific) |
| 5 | `"amicus" "voting rights" "democratic renewal" OR "electoral reform" 2026` | Federal circuit courts | Month 2–6 |

**Domain 42 DEA monitoring — special procedure**:

CourtListener indexes some federal administrative agency dockets, but the DEA docket (DEA-1362) is a Regulations.gov docket, not a federal court docket. Monitor it separately:

1. Go to `regulations.gov/docket/DEA-1362`.
2. The docket page shows all submitted comments and participation notices.
3. Before June 22 (when DEA publishes its participant list), check Regulations.gov weekly for submitted participation notices from Phase 1 contact organizations.
4. Download any notice from a Phase 1 contact organization and record it in the Citation Log as `adoption_level=3`, `document_url=[Regulations.gov URL]`.

The DEA hearing participant list (published approximately June 22) is the primary policy uptake milestone for Domain 42. When it publishes, cross-reference every organization on the participant list against the Phase 1 Domain 42 outreach contact list. Count confirmed participants as strong success events.

**Monitoring cadence**: CourtListener alerts email on match — passive monitoring. Check the Regulations.gov DEA-1362 docket page manually every Wednesday during May 14–June 22.

### 3.2 Google Scholar Alerts — Legal and Academic Tracking

**Setup** (10 minutes, one-time — from existing doc):

At `scholar.google.com/scholar_alerts`, create alerts for:
- `"democratic renewal proposal"`
- `"35-domain" democracy institutional`
- `"state legislative autocratization" institutional`
- `"appellate capture" judicial reform`
- `"regulatory capture" DEA "marijuana rescheduling" "democratic" OR "civil rights"` (Domain 42)

Scholar alerts fire when new indexed academic papers match. Expect zero results for Months 1–4 for the framework-specific queries. The Domain 42 DEA regulatory capture query may produce earlier results because the academic literature on DEA rulemaking is active.

**Manual quarterly sweep** (30 minutes, every 3 months):

Run all alert queries manually in Google Scholar and record result counts. Compare against the pre-distribution baselines recorded in `execution/phase-1-baseline-metrics.md`. Any new result from a document dated after Phase 1 launch should be read, assessed against the attribution tests in `phase-1-adoption-tracking-automation.md` Part 1, and logged in the Citation Log.

### 3.3 Legislative Tracking — Congress.gov and LegiScan

**Congress.gov keyword monitoring** (new in this document):

Go to `congress.gov/search`. This free tool provides full-text search of bill text across all Congress sessions.

Create a bookmark folder "Phase 1 Legislative Monitoring" with these saved searches:

| Search | URL to bookmark |
|--------|-----------------|
| Democratic renewal language | `https://www.congress.gov/search?q=%22democratic+renewal%22+%22voting+rights%22&searchResultViewType=expanded` |
| NVRA quiet period | `https://www.congress.gov/search?q=%22NVRA%22+%22quiet+period%22&searchResultViewType=expanded` |
| DEA rescheduling democratic | `https://www.congress.gov/search?q=%22DEA%22+%22rescheduling%22+%22disenfranchisement%22` |
| Fiscal impoundment | `https://www.congress.gov/search?q=%22impoundment%22+%22fiscal+authority%22+%22democratic%22` |

Check each bookmark every Friday during the first 90 days. Record any new bill or resolution in the Citation Log under sector "Legislative — Federal."

**LegiScan state monitoring** (from existing doc — setup confirmed, reproduced for completeness):

Register at `legiscan.com/legiscan-register`. In priority states (CA, NY, MN, WI, PA, MI, CO, AZ, OH, VA, NC, GA), create full-text saved searches with daily email notifications:

- `"voter roll" purge SAVE 2026`
- `preemption "local government" ballot initiative restriction`
- `"DEA" "marijuana rescheduling" "civil rights" state level`

**How legislative citations count**: A state bill using vocabulary from the framework's domain analysis — even without attribution — scores `vocab_adoption_detected=Y` in the Master Contact Log for any Tier 1 state AG contact from that state. This is Level 2 adoption.

### 3.4 News Mention Tracking — Google Alerts + Manual Verification

**Google Alerts setup** (15 minutes, one-time — from existing doc, extended here):

At `news.google.com/alerts`, with delivery to `monitoring/google-alerts/` Gmail label, create alerts:

**Framework identity alerts**:
- `"democratic renewal proposal"` — All results, daily
- `"35-domain democratic"` — All results, daily
- `"democratic renewal framework" democracy` — All results, daily

**Domain 42 DEA alerts** (new):
- `"DEA-1362" "civil rights" OR "disenfranchisement"` — All results, daily
- `"marijuana rescheduling" "democratic" hearing participation` — All results, daily

**Vocabulary marker alerts**:
- `"NVRA quiet period" 2026` — All results, daily
- `"state legislative autocratization"` — All results, daily
- `"appellate capture" judicial independence` — All results, daily
- `"fiscal authority bypass" OMB` — All results, daily

**Bridge node second-order alerts**:
- `"Brennan Center" "voting rights" "democratic renewal"` — All results, daily
- `"Democracy Docket" "voter roll" SAVE 2026` — All results, daily
- `"Drug Policy Alliance" OR "NORML" DEA-1362 hearing 2026` — All results, daily

**Alert review cadence**: Check the `monitoring/google-alerts/` label every Monday morning. Spend 10 minutes scanning subject lines. Open any hit from a policy or media organization, read for framework vocabulary, and log confirmed citations in the Citation Log.

**News source quality filter**: Only log articles from:
- National media with editorial standards (NYT, WaPo, Guardian, The Atlantic, Vox, Slate, Reuters, AP, NPR, Politico)
- Specialist legal/policy media (Lawfare, Just Security, Law360, Courthouse News, Democracy Docket, National Law Journal)
- Credible local media (state newspaper of record or major urban daily)
- Non-profit journalism (ProPublica, Marshall Project, The Intercept with editorial disclosure)

Do not log articles from advocacy blogs, anonymous newsletters, or sites without a visible editorial process. These may appear in alerts but do not count as verified media citations.

### 3.5 Overton Window Tracking

The Overton window (the range of policy ideas considered publicly acceptable) shifts slowly. This is a 6–18 month tracking effort, not a Week 1 metric.

**Primary tool**: `overton.io` — indexes 21 million+ policy documents and tracks citations across government reports, think tank publications, and NGO outputs.

**Schedule** (from existing doc — confirmed appropriate):
- Month 4 (September 2026): First search. Run all framework vocabulary markers. Record result counts.
- Month 8 (January 2027): Second search. Compare against Month 4 baseline.
- Month 12 (May 2027): Third search. Export results for impact assessment.

**Supplementary Overton signal** — track these as leading indicators before Month 4:
- Think tank publication language: Does Brennan Center, Protect Democracy, or CAP use "regulatory capture" in a DEA or FDA context after Phase 1? That is an Overton shift signal even without explicit framework citation.
- Legislative testimony language: Search C-SPAN video captions at `c-span.org` for testimony using framework vocabulary. Any congressional or state legislative testimony using unique framework coinages is a strong Overton signal.

---

## Section 4: Coalition and Network Tracking

### 4.1 Contact Response Classification

**Reference**: `phase-1-adoption-tracking-automation.md` Part 4 defines five response categories. This section operationalizes them into the daily tracking workflow.

**When a reply arrives** — 3-step process (takes 5 minutes):

Step 1: Apply the Gmail label (`replies/substantive`, `replies/auto-ack`, `replies/bounce`, or `replies/forward-detected`).

Step 2: Open the Google Sheets "Master Contact Log." Find the row for the replying organization. Update:
- `email_reply_received` = Y
- `reply_date` = today's date
- `reply_category` = the appropriate category (Implementation Question / Methodology Critique / Integration Request / Thanks-No-Action / Bounced)
- `engagement_score` = recalculate per rubric in `phase-1-adoption-tracking-automation.md` Section 2.2
- `next_action` = specific follow-up text and deadline

Step 3: If `reply_category = Integration Request`, trigger the Discord "ESCALATE" alert (see Section 5.2) and do not reply to the email until the user has authored the response.

**Organization-level aggregation by sector**:

The Google Sheets "KPI Summary" tab (Section 5.1) aggregates response rates by sector using COUNTIF formulas. If any sector is significantly below its SLA deadline with zero replies, it surfaces as an alert. See the formula set in Section 5.1.

### 4.2 Secondary Contact Discovery

Secondary contacts are organizations or individuals who engage with the framework without being directly contacted in Phase 1 — evidence that a Tier 1 contact forwarded the material.

**Three detection methods**:

**(a) Inbound email from unknown address**: Any reply from an email domain not on the Phase 1 contact list — open it, determine organization, add to Master Contact Log as `tier=2` with `source=secondary_discovery`, record which Tier 1 contact most likely forwarded (check timing and domain alignment). This is the highest-confidence secondary discovery signal.

**(b) Social media mention from policy-adjacent account**: The weekly social media sweep (Section 3.4 third bullet) catches this. Any mention from a policy organization's verified account that uses framework language is a secondary discovery. Record the organization in the Master Contact Log.

**(c) Direct follow-up questioning in Day 30 email**: The Day 30 follow-up email template (from `success-metrics.md`) includes: "Has this been useful enough to share with any colleagues? If so, I'd welcome knowing who else has seen it." Responses identifying specific secondary contacts should be immediately logged.

**Tracking secondary contacts**: Add them to the Master Contact Log with:
- `tier=2` (automatically qualifies for Tier 2 outreach)
- `source=secondary_discovery`
- `secondary_from=[Tier 1 org name that forwarded]`
- `email_sent_date` = blank (they were not formally contacted; contact them in Wave 2 or 3)

A secondary contact discovery in Week 1 is a Level 4 adoption signal for the forwarding Tier 1 organization.

### 4.3 Decision Velocity Measurement

Decision velocity tracks how quickly an organization moves from first contact to a consequential action (filing a participation notice, publishing a briefing incorporating framework analysis, or making a public statement).

**Tracking columns in Master Contact Log** (add these to the existing schema):

| Column | Formula | Notes |
|--------|---------|-------|
| `days_to_first_reply` | `=IF(reply_date="","",reply_date - email_sent_date)` | Days from send to first substantive reply |
| `days_to_adoption` | `=IF(adoption_date="","",adoption_date - email_sent_date)` | Days from send to first Level 2+ adoption event |
| `adoption_date` | Manual entry | Date of first confirmed adoption event |

**Velocity benchmarks** (derived from sector SLA table in adoption tracking doc):

| Sector | Fast (top quartile) | Median | Slow (flag for follow-up) |
|--------|--------------------|---------|-----------------------------|
| Legal Services / Immigration Legal Aid | <7 days to reply | 14 days | >21 days |
| Mutual Aid / Grassroots | <3 days | 7 days | >14 days |
| Civil Rights Litigation Orgs | <10 days | 18 days | >28 days |
| Think Tanks | <14 days | 28 days | >45 days |
| Law Schools | <21 days | 42 days | >60 days |

If any contact in the Legal Services sector has not replied by Day 21, flag `next_action = "Follow-up required — SLA exceeded"` and add to the weekly action list.

### 4.4 Organization-Level Aggregation

The "KPI Summary" Google Sheets tab aggregates tracking data by organizational sector to identify which sectors are engaging and which need attention.

**Aggregation table** (pre-built formulas in Section 5.1):

| Sector | Orgs Sent | Orgs Replied (L1+) | Orgs Adopted (L2+) | Avg Days to Reply | Notes |
|--------|-----------|--------------------|--------------------|-------------------|-------|
| State AGs | [COUNTIF] | [COUNTIF] | [COUNTIF] | [AVERAGEIF] | |
| Think Tanks | [COUNTIF] | [COUNTIF] | [COUNTIF] | [AVERAGEIF] | |
| Civil Rights Orgs | [COUNTIF] | [COUNTIF] | [COUNTIF] | [AVERAGEIF] | |
| Law Schools | [COUNTIF] | [COUNTIF] | [COUNTIF] | [AVERAGEIF] | |
| Labor Unions | [COUNTIF] | [COUNTIF] | [COUNTIF] | [AVERAGEIF] | |
| Drug Policy Orgs (D42) | [COUNTIF] | [COUNTIF] | [COUNTIF] | [AVERAGEIF] | |

---

## Section 5: Real-Time Dashboards

### 5.1 Google Sheets Master Dashboard

**Architecture**: 8-tab workbook (the 7 tabs documented in `phase-1-adoption-tracking-automation.md` plus one new "D42 DEA Tracking" tab for Domain 42-specific data).

**Tab 8 — D42 DEA Tracking** (new, not in existing schema):

This tab tracks Domain 42 DEA-1362 participation outcomes, separate from the main adoption ladder.

| Column | Content |
|--------|---------|
| `org_name` | Organization name |
| `email_sent_date` | When the Domain 42 email was sent |
| `wave_number` | Wave 1 / 2 / 3 |
| `reply_received` | Y/N |
| `reply_date` | Date |
| `commitment_to_file` | Y/Unclear/N |
| `participation_notice_filed` | Y/N (check Regulations.gov) |
| `filed_date` | Date notice appeared on Regulations.gov |
| `domain42_cited` | Y/N (does the notice cite democratic exclusion / disenfranchisement framing?) |
| `dea_participant_selected` | Y/N (update June 22 when DEA publishes participant list) |
| `notes` | |

**KPI Summary tab — pre-built formulas**:

Copy these formulas into the "KPI Summary" tab. They reference the "Master Contact Log" sheet (name it `Contacts` in your workbook).

Assume the Master Contact Log has:
- Column B = sector
- Column K = email_reply_received (Y/N)
- Column N = reply_category
- Column S = adoption_level (0–4)
- Column X = days_to_first_reply

```
=== OVERALL METRICS (Row 2–15 on KPI Summary) ===

B2: Total contacts sent
Formula: =COUNTA(Contacts!A2:A200)-1

B3: Total replies received
Formula: =COUNTIF(Contacts!K2:K200,"Y")

B4: Reply rate (%)
Formula: =IF(B2=0,"N/A",TEXT(B3/B2,"0.0%"))

B5: Level 1+ engagement (awareness)
Formula: =COUNTIF(Contacts!S2:S200,">=1")

B6: Level 2+ adoption (reference)
Formula: =COUNTIF(Contacts!S2:S200,">=2")

B7: Level 3+ operational adoption
Formula: =COUNTIF(Contacts!S2:S200,">=3")

B8: Level 4 coalition adoption
Formula: =COUNTIF(Contacts!S2:S200,"4")

B9: Avg days to first reply (all replies)
Formula: =IFERROR(AVERAGEIF(Contacts!K2:K200,"Y",Contacts!X2:X200),"No replies yet")

B10: Bounces detected
Formula: =COUNTIF(Contacts!L2:L200,"Y")

B11: Bounce rate (%)
Formula: =IF(B2=0,"N/A",TEXT(B10/B2,"0.0%"))

=== SECTOR BREAKDOWN (Rows 18–30) ===

C18: Think Tank reply rate
Formula: =IFERROR(COUNTIFS(Contacts!B2:B200,"Think Tank",Contacts!K2:K200,"Y")/COUNTIF(Contacts!B2:B200,"Think Tank"),"0%")

C19: Civil Rights Org reply rate
Formula: =IFERROR(COUNTIFS(Contacts!B2:B200,"Civil Rights Org",Contacts!K2:K200,"Y")/COUNTIF(Contacts!B2:B200,"Civil Rights Org"),"0%")

C20: Law School reply rate
Formula: =IFERROR(COUNTIFS(Contacts!B2:B200,"Law School",Contacts!K2:K200,"Y")/COUNTIF(Contacts!B2:B200,"Law School"),"0%")

C21: State AG reply rate
Formula: =IFERROR(COUNTIFS(Contacts!B2:B200,"State AG",Contacts!K2:K200,"Y")/COUNTIF(Contacts!B2:B200,"State AG"),"0%")

C22: Drug Policy Org (D42) reply rate
Formula: =IFERROR(COUNTIFS(Contacts!B2:B200,"Drug Policy Org",Contacts!K2:K200,"Y")/COUNTIF(Contacts!B2:B200,"Drug Policy Org"),"0%")

=== ALERT CELLS (Rows 35–42) ===

These cells turn RED (use conditional formatting: red fill if formula returns "ALERT") when thresholds are breached.

D35: Day 7 reply rate alert
Formula: =IF(AND(TODAY()-MIN(Contacts!H2:H200)>=7,B4<0.10),"ALERT: <10% reply rate at Day 7 — see Contingency Trigger 1","OK")

D36: Bounce rate alert
Formula: =IF(B11>0.05,"ALERT: Bounce rate >5% — audit contact list","OK")

D37: Sector silence alert (Think Tanks)
Formula: =IF(AND(TODAY()-MIN(Contacts!H2:H200)>=21,C18=0),"ALERT: Think tanks completely silent at Day 21","OK")

D38: Sector silence alert (Drug Policy Orgs)
Formula: =IF(AND(TODAY()-MIN(Contacts!H2:H200)>=7,C22=0),"ALERT: Zero D42 replies at Day 7 — DEA deadline approaching","OK")
```

**Daily/Weekly/Monthly views**:

The workbook has three standard views configured as filtered views (not separate tabs):

- "Daily View": Filter Master Contact Log to show only rows where `last_updated = TODAY()` or `days_since_send <= 7`. Sorts by `next_action` column. Shows the daily task list.
- "Weekly View": Filter to show rows where `sla_respond_by` falls within the next 14 days. Shows upcoming SLA deadlines.
- "Monthly View": Show all rows sorted by `adoption_level` descending. The adoption ladder as of today.

### 5.2 Discord Notification Setup

**Purpose**: Surface time-sensitive signals (Integration Requests, anomalies, spike alerts) without requiring daily spreadsheet monitoring. A Discord channel with a webhook delivers a daily briefing and event-triggered alerts.

**Setup** (15 minutes):

1. In your Discord server, create a new channel named `#phase1-metrics`.

2. Go to channel Settings → Integrations → Webhooks → New Webhook.

3. Name the webhook "Phase1Bot". Copy the webhook URL. It will look like: `https://discord.com/api/webhooks/[NUMERIC_ID]/[TOKEN]`

4. Save the webhook URL in a password manager. Do not commit it to any public repository.

5. Test the webhook by running this curl command in a terminal:

```bash
curl -H "Content-Type: application/json" \
     -X POST \
     -d '{"content": "**Phase 1 Tracking: Webhook test** — If you see this, the webhook is live."}' \
     "https://discord.com/api/webhooks/[YOUR_WEBHOOK_URL]"
```

The message should appear in `#phase1-metrics` within 5 seconds.

**Daily briefing** — paste this Python script into a file called `daily_briefing.py`. Run it each morning (or schedule via cron/Zapier):

```python
#!/usr/bin/env python3
"""
Phase 1 Daily Discord Briefing
Run each morning during Phase 1 active period.
Requires: requests library (pip install requests)
"""
import requests
from datetime import date

WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"

# Update these manually each morning before running
metrics = {
    "day_number": 0,          # Days since Wave 1 send date
    "total_sent": 45,
    "total_replies": 0,
    "reply_rate_pct": 0.0,
    "level2_adopters": 0,
    "new_replies_today": 0,
    "gist_views_delta_week": 0,
    "d42_participation_notices": 0,  # Confirmed DEA-1362 filers
    "anomaly_flag": "None",    # "None" or description of anomaly
}

def format_status_emoji(value, threshold_warn, threshold_alert):
    if value >= threshold_warn:
        return "✅"
    elif value >= threshold_alert:
        return "⚠️"
    else:
        return "🔴"

payload = {
    "embeds": [{
        "title": f"📊 Phase 1 Daily Briefing — Day {metrics['day_number']}",
        "color": 0x2F80ED,
        "fields": [
            {
                "name": "Reply Rate",
                "value": f"{format_status_emoji(metrics['reply_rate_pct'], 20, 10)} {metrics['reply_rate_pct']:.1f}% ({metrics['total_replies']}/{metrics['total_sent']})",
                "inline": True
            },
            {
                "name": "Level 2+ Adoption",
                "value": f"{format_status_emoji(metrics['level2_adopters'], 3, 1)} {metrics['level2_adopters']} orgs",
                "inline": True
            },
            {
                "name": "New Replies Today",
                "value": f"{metrics['new_replies_today']}",
                "inline": True
            },
            {
                "name": "Gist Views This Week",
                "value": f"{metrics['gist_views_delta_week']} total across 6 Gists",
                "inline": True
            },
            {
                "name": "D42 DEA Filers",
                "value": f"{metrics['d42_participation_notices']} confirmed (of 5 Wave 1 orgs)",
                "inline": True
            },
            {
                "name": "Anomaly Flag",
                "value": metrics['anomaly_flag'],
                "inline": False
            }
        ],
        "footer": {"text": f"Phase 1 Tracking | {date.today().isoformat()}"},
    }]
}

response = requests.post(WEBHOOK_URL, json=payload)
print(f"Sent: {response.status_code}")
```

**Event-triggered alerts** — copy-paste these curl commands for immediate use when triggered events occur:

**Integration Request received** (copy-paste, replace ORG_NAME):
```bash
curl -H "Content-Type: application/json" -X POST \
  -d '{"content": "🚨 **ESCALATE: Integration Request from [ORG_NAME]** — User response required within 48h. Check Gmail label: phase1-outreach/replies/substantive"}' \
  "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
```

**Gist spike detected** (copy-paste, replace GIST_NAME and DELTA):
```bash
curl -H "Content-Type: application/json" -X POST \
  -d '{"content": "📈 **Gist Spike: [GIST_NAME]** — [DELTA] new views this week. Cross-reference which orgs were sent this URL. Consider follow-up if in SLA window."}' \
  "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
```

**Contingency trigger fired** (copy-paste, replace TRIGGER_NAME):
```bash
curl -H "Content-Type: application/json" -X POST \
  -d '{"content": "⚡ **Contingency Trigger: [TRIGGER_NAME]** — See PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md Section 7 for escalation protocol."}' \
  "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
```

### 5.3 Weekly Review Template

Run every Monday during Phase 1 active period. Takes 20–30 minutes.

Save as `monitoring/week-[N]-summary-[YYYY-MM-DD].md` in the `projects/resistance-research/` directory.

```markdown
# Phase 1 Weekly Summary — Week [N] (Day [X] from Launch)
Date: [YYYY-MM-DD]

## Quick Stats
- Reply rate: [N]% ([N]/[total sent])
- Level 2+ adopters: [N]
- New replies this week: [N]
- Gist views this week: [N] total (delta from last week: [+/-N])
- Bitly clicks this week: [N] across all links
- Google Alerts hits: [N] (logged citations: [N])
- D42 DEA participation notices confirmed: [N]/5

## New Signals
- [Org name] — [reply category] — [adoption level update]
- [Gist spike if any] — [delta] views — [likely source]
- [Citation detected if any] — [source, sector, domain cited]

## Alert Status
- Day 7 reply rate: [GREEN / YELLOW / RED]
- Bounce rate: [GREEN / YELLOW / RED]
- Think tank sector silence: [GREEN / YELLOW / RED]
- D42 Drug Policy sector silence: [GREEN / YELLOW / RED]

## Contingency Status
[None triggered / Trigger [N] active — see escalation notes below]

## Next Week Actions
- [ ] [Specific follow-up action — org name, deadline]
- [ ] [SLA deadline for org X]
- [ ] [Any contingency escalation step due]

## Domain Heat Map Update
| Domain | New Signals | Source | Level |
|--------|-------------|--------|-------|
| D1 (Voting) | | | |
| D6 (Judiciary) | | | |
| D29 (Prosecutorial) | | | |
| D42 (Drug Policy/DEA) | | | |
| [others with new signal] | | | |
```

---

## Section 6: Success Metrics Framework

### 6.1 Baseline Reference Table

The following baselines define the minimum, strong, and stretch outcomes for Phase 1. They are calibrated to the 35-domain framework distributed to 45+ Tier 1 contacts plus Domain 42 distributed to 5–24 specialized drug policy and civil rights contacts.

These supplement (not replace) the detailed sector-by-sector targets in `phase-1-adoption-tracking-automation.md` Part 7 and `success-metrics.md` Section 1–3.

| Metric | Minimum Viable | Strong | Stretch | Measurement Point |
|--------|---------------|--------|---------|-------------------|
| Tier 1 reply rate | 20% (9/45) | 30% (14/45) | 45%+ (20+/45) | Day 30 |
| Tier 1 Level 2+ adoption | 3 orgs / 2+ sectors | 8 orgs / 3+ sectors | 15+ orgs / 4+ sectors | Day 90 |
| D42 DEA participation notices | 2 confirmed | 4+ confirmed | 5+ with D42 framing cited | May 28 |
| Policy uptake (any) | 1 bill/testimony using framework language | 3+ events across levels | 7+ events (bills, testimony, filings) | Day 90 |
| Coalition formation | 1 org coordinates advocacy with another | 3+ orgs coordinate | 5+ orgs formal coalition | Day 90 |
| Media amplification | 1 named mention | 5+ stories | 10+ stories with attribution | Day 90 |
| Secondary contact discovery | 3+ known forwards | 10+ new secondary contacts identified | 20+ secondary contacts | Day 30 |
| Gist cumulative views (all Gists) | 100 | 500 | 2,000+ | Day 30 |

### 6.2 Historical Baselines and Comparison Points

These comparison points provide context for interpreting Phase 1 results against analogous policy outreach campaigns.

**Institutional policy brief campaigns** (from RAND, Brookings distribution research):
- Cold outreach to policy professionals: 15–25% reply rate is typical for well-targeted personalized outreach
- Reply rate below 10% indicates either contact list mismatch or email delivery problems (not content failure)

**Congressional Research Service distribution benchmarks**:
- Policy briefings distributed to Senate staff: median first response in 14–21 days; 30–40% response rate for topic-matched briefs
- Our 36% Tier 1 response target (from `success-metrics.md`) is consistent with this benchmark

**Drug policy administrative comment campaigns** (DEA precedent):
- 2024 DEA-1362 predecessor proceedings: 160+ participation notices filed; DEA selected ~25 participants
- For 5 Wave 1 organizations: getting 2+ participation notices filed that cite democratic exclusion framing is a better-than-median outcome relative to the 2024 participant pool composition
- "Counterfactual participation" standard: at least 1 organization that would not have filed without Domain 42 outreach

**Law review citation lag**:
- Average time from policy document publication to first law review citation: 6–24 months
- 0 academic citations at Day 90 is normal and expected — do not treat as failure

### 6.3 Decision Tree for 30-Day Assessment

```
DAY 30 ASSESSMENT
│
├── Reply rate ≥ 30% (14+ of 45)?
│   ├── YES → Proceed to Tier 2 launch without modification
│   └── NO
│       ├── Reply rate 20-29%?
│       │   ├── YES → Review messaging; proceed to Tier 2 with adjusted subject lines
│       │   └── NO (below 20%) → Halt Tier 2; run diagnostic (Contingency Trigger 1)
│
├── Any Level 2+ adoption events?
│   ├── YES → Strong signal; continue current strategy
│   └── NO → Check for delivery problems; Level 2 at Day 30 is early but absence is worth noting
│
├── D42 DEA results (May 28 deadline already passed by Day 30):
│   ├── 3+ organizations filed → Strong D42 outcome
│   ├── 1–2 filed → Acceptable; document and proceed
│   └── 0 filed → Assess whether outreach was received; document for future DEA proceedings
│
└── Any secondary contacts discovered?
    ├── YES → Coalition formation signals are healthy; log and contact them
    └── NO at Day 30 → Explicit "ask to forward" was likely absent; add to Tier 2 emails
```

---

## Section 7: Contingency Detection Triggers

These triggers are binary: each condition is either met or not. When a trigger fires, the corresponding escalation protocol is mandatory — not optional.

### Trigger 1: Low Reply Rate (Critical — Week 1)

**Condition**: Fewer than 10% of Wave 1 contacts have replied with any substantive response by Day 7 (i.e., fewer than 3 of the first 25 contacts sent).

**Detection**: KPI Summary tab cell D35 shows "ALERT". Discord daily briefing shows reply rate < 10%.

**Escalation protocol**:

1. **Check delivery first** (Day 7): Log in to the Gmail account used for outreach. Search `sent:wave-1 to:[any contact email]`. Do the emails show as Delivered in Streak (if installed), or do you see any bounce notifications in `monitoring/bounce` folder? If >3 bounces from a single domain (e.g., all `.edu` addresses bouncing), that is a mail server filter problem, not a messaging problem.

2. **Check Gist URLs** (Day 7): Navigate to the raw Gist URLs in each email template. Confirm they load. If a Gist was accidentally deleted or made private, every click link is broken — this would explain zero engagement even with delivery.

3. **Send one test email to a personal address** (Day 8): Send the exact template you used for Wave 1 to a personal Gmail address. Does it arrive? Does the Bitly link work? Is the subject line clear or likely to trigger spam filters?

4. **If delivery confirmed and no engagement**: The subject line or opening paragraph is not compelling enough for the recipient's context. Revise the subject line for Wave 2. Examples:
   - Instead of: "Democratic Renewal Framework — Phase 1 Distribution"
   - Try: "Re: [specific current event relevant to their work]" or "[First name] — question about [their recent publication/case]"

5. **If no improvement by Day 14**: Do not send Wave 2 until performing 3 direct phone/LinkedIn outreach attempts to top-priority Tier 1 contacts (Ryan Goodman at Just Security, Wendy Weiser at Brennan Center, or the AG contact most closely tied to an active case). A warm voice conversation can unlock the email relationship.

**Discord notification**: Fire "Contingency Trigger 1 active" alert.

### Trigger 2: High Bounce Rate (Urgent — Day 1–3)

**Condition**: More than 5% of sent emails bounce (more than 2 hard bounces from a 25-email Wave 1, or more than 4 from a 45-email full Tier 1 send).

**Detection**: KPI Summary tab cell D36 shows "ALERT". Bounce notifications appear in `monitoring/bounce` Gmail folder via Zapier.

**Escalation protocol**:

1. **Halt Wave 2** immediately until bounces are resolved.

2. **Categorize each bounce**: Hard bounce (permanent — email address no longer valid) vs. Soft bounce (temporary — mailbox full, server timeout). Hard bounces require contact re-verification. Soft bounces: retry after 48 hours.

3. **Re-verify hard-bounce contacts**: Return to `execution/domain-42-contact-list.md` or `DISTRIBUTION_OUTREACH_CONTACTS.md`. Use the organization's current website contact page to find updated email. Update the Master Contact Log `contact_email` field.

4. **If a domain class is bouncing** (e.g., all `.gov` addresses, or all addresses at a specific org): the organization may have changed email systems. Search the org's website for the most recent "Contact Us" or staff directory page. Do not assume the email format is the same as before.

5. **After re-verification**: Re-send to hard-bounce contacts with corrected email. Set `alt_contact_tried=Y` in Master Contact Log.

**Discord notification**: Fire "Contingency Trigger 2 — Bounce Rate Alert" immediately.

### Trigger 3: Zero Policy Interest (Longer-Term — Day 21)

**Condition**: By Day 21, no Tier 1 think tank contact has replied, no state AG office has replied, and no policy-focused media outlet has mentioned the framework.

**Detection**: Weekly review shows all AG-sector cells at `engagement_score=0`; all Think Tank cells at `engagement_score=0`; Google Alerts has produced zero results.

**Escalation protocol**:

1. **Audience pivot assessment** (Day 21): Are the Tier 1 contacts actually the right audience for the current political moment? In May–June 2026, the highest-urgency issues are the FISA Section 702 declassification (June 12), the DEA-1362 hearing (June 29–July 15), and pre-midterm election integrity work. If outreach leads with general "democratic renewal" framing but think tanks are currently focused on immediate election security, a framing misalignment may exist.

2. **Re-lead with urgency-proximate content**: For AG and civil rights contacts, re-send with a one-line subject line referencing the most current high-profile litigation matching their sector (e.g., for voting rights contacts: "The Callais ruling changes Domain 1 analysis — updated section attached"). Contacts who did not respond to the general outreach sometimes respond to a specific update.

3. **Direct route through bridge nodes**: If think tanks are silent, attempt direct outreach to the individual researchers who have published on domains most closely matching Domains 6, 16, and 29. A direct email to the author of a recent Brennan Center paper — specifically referencing that paper — bypasses the institutional contact routing problem.

4. **Assess whether email is the right channel**: Some Tier 1 contacts respond better to direct LinkedIn InMail or Twitter DM than to cold email. If the framework is on social media and generating engagement, use that engagement as a bridge ("I saw you were engaged with the thread about X — the full analysis is here").

**Discord notification**: Fire "Contingency Trigger 3 — Zero Policy Interest at Day 21" alert.

### Trigger 4: Abnormal Unsubscribe Rate (Substack-Specific)

**Condition**: Any single Substack post generates more than 5% unsubscribe rate (e.g., 3+ unsubscribes from a list of 50, or 6+ unsubscribes from a list of 100).

**Detection**: Check the Substack analytics page for each post within 72 hours of publication. Unsubscribes are shown per-post in Substack dashboard → Stats.

**Escalation protocol**:

1. **Do not publish the next planned Substack post** until the unsubscribe cause is identified.

2. **Read the unsubscribed post** with the following questions: Was the post substantially longer than previous posts? Did it introduce a significantly different tone (more explicitly political, more alarming, more detailed/academic)? Did it focus on a topic that is less directly relevant to the likely subscriber base?

3. **Diagnosis categories**:
   - **Tone mismatch**: Post was more alarming or advocacy-oriented than the academic/analytical baseline. Solution: return to analytical framing in subsequent posts.
   - **Topic drift**: Post covered a domain (e.g., environmental rollbacks) that does not match the primary audience interest (voting rights, judicial independence). Solution: re-sequence topic coverage.
   - **Frequency fatigue**: Multiple posts in a short period. Solution: extend time between posts to 7–10 days.
   - **List quality**: Early Substack subscribers may include a non-target audience (e.g., people who followed from a Reddit thread about a topic not central to the framework). An early churn of 5–10% may be healthy attrition toward a higher-quality list.

4. **Threshold to flag**: 5% from a single post once is a yellow flag. 5%+ from two consecutive posts is a red flag requiring strategy reassessment.

**Discord notification**: Fire "Contingency Trigger 4 — Unsubscribe Anomaly" alert.

### Trigger 5: Coalition Formation Failure (Day 45)

**Condition**: By Day 45, no two Phase 1 contact organizations have independently begun coordinating on an advocacy action that references the framework (e.g., no joint statement, no shared amicus brief, no joint testimony referencing the same framework analysis).

**Detection**: This requires active monitoring — it will not surface in passive Google Alerts. The Day 30 follow-up email asking about forwards is the primary detection method.

**Escalation protocol**:

1. **Identify the two most engaged Tier 1 contacts** at Day 45 (highest engagement_score). Email each one separately and ask: "I know [Organization B] has also been working on [related issue]. Is there any value in an introduction between the two of you, focused on the [Domain X] analysis?" This is a direct introduction offer — the researcher as connector.

2. **Create a coordinating artifact**: Draft a 1-page synthesis brief that combines the analysis from two or three Tier 1 contacts' current active cases. Send it to both organizations with the message: "This combines what [Org A] is doing on X with what [Org B] is doing on Y — I thought it might be useful for both of you." A shared document creates a natural coordination hook.

3. **Use Domain 42 as a coalition entry point**: The DEA-1362 hearing (June 29–July 15) is a natural coordination venue. If 2+ organizations have filed participation notices, they are already co-participants. Introduce the two organizations to each other around the shared hearing participation — that is an organic coalition formation moment.

**Discord notification**: Fire "Contingency Trigger 5 — Coalition Formation Lag" alert at Day 45.

---

## Section 8: Integration Points

### 8.1 Cybersecurity-Hardening Phase 1 Timing

**Context**: The cybersecurity-hardening project has its own Phase 1 distribution (25 contacts, June 1 launch target), with its own measurement infrastructure documented in `projects/cybersecurity-hardening/PHASE_1_MEASUREMENT_AUTOMATION.md`.

**Cross-project integration opportunity**:

The resistance-research Phase 1 and cybersecurity-hardening Phase 1 target overlapping institutional sectors (civil rights organizations, law schools, think tanks) but different primary audiences. If the resistance-research Phase 1 generates strong early engagement (Level 1+ reply rate >30% by Day 14), that creates a "warm list" effect: contacts who have already engaged with the democratic renewal framework are more likely to engage with the cybersecurity threat model when they receive it in a subsequent wave.

**Tracking signal**: In the Master Contact Log, add a column `cyber_phase1_candidate` (Y/N). When a resistance-research contact replies substantively, evaluate whether their institutional role also matches the cybersecurity distribution target (primarily: immigration legal services, civil rights orgs, sanctuary city government contacts). If yes, set `cyber_phase1_candidate=Y`. Share this column with the cybersecurity project tracking when cyber Phase 1 launches.

**Sequencing note**: Do not send both the resistance-research Phase 1 email and the cybersecurity Phase 1 email to the same contact within the same week. Stagger by at least 14 days. The resistance-research email creates awareness; the cybersecurity email adds operational depth. They are most effective as a sequence, not a simultaneous send.

**Approval gate integration**: Cybersecurity Phase 1 is currently blocked on user approval of launch date. If resistance-research Phase 1 produces strong early signals, those signals should be included in the cybersecurity Phase 1 launch rationale — evidence that the distribution network is receptive.

### 8.2 Seedwarden May 30 Visibility Window

**Context**: The Seedwarden project has a Track B launch target of May 30, 2026 — overlapping with the resistance-research Phase 1 launch preparation window (May 31 setup, June 1 send).

**Potential audience overlap**: Seedwarden's Track B targets a sustainability/self-sufficiency audience. The resistance-research Phase 1 targets policy professionals, legal scholars, and civil rights organizations. These audiences have minimal direct overlap — the same person rarely appears in both.

**However**, there is an indirect overlap through Substack: if any resistance-research contacts are also interested in community resilience themes, the Seedwarden content may amplify engagement. The cross-promotion opportunity is small and not worth actively pursuing unless organic overlap emerges.

**Practical integration**: The main scheduling risk is concentration of user attention. Phase 1 resistance-research launch (June 1) and Seedwarden Track B launch (May 30) land within 2 days of each other. The May 31 evening setup window for resistance-research measurement infrastructure competes with Seedwarden pre-launch preparation. **Resolution**: If both launches are happening simultaneously, arm the resistance-research measurement infrastructure on May 28–29, not May 31. This frees May 31 for Seedwarden Track B preparation. All setup steps in this document can be completed 2–3 days early without any loss of tracking fidelity.

### 8.3 Domain 42 DEA Hearing Amplification

**Context**: The Domain 42 DEA-1362 distribution is the only Phase 1 sub-component with an external hard deadline (May 28, 2026). If Phase 1 general distribution produces strong early results (reply rate >25% by Day 7), those results can be used to strengthen the Domain 42 follow-up strategy in two ways.

**Amplification mechanism 1 — Social proof**:
When following up with Domain 42 Wave 2 and Wave 3 contacts (civil rights organizations and state AG offices, respectively), if you have already received substantive engagement from Wave 1 drug policy organizations, include a note: "Drug Policy Alliance and NORML have both expressed interest in filing participation notices. I'm reaching out to civil rights and voting rights organizations who may want to establish standing in the same proceedings." Social proof from early responders increases the response rate for later waves.

**Amplification mechanism 2 — Coalition coordination**:
If two or more Domain 42 organizations have committed to filing participation notices, introduce them to each other before May 28. Organizations that are co-filing in the same DEA docket are natural coalition partners. A coordinated amicus-style filing strategy (multiple organizations citing the same democratic exclusion framing) is stronger than isolated individual filings.

**Post-May 28 amplification — Hearing preparation**:
After May 28, if Domain 42 has generated 2+ confirmed DEA hearing participants, the next advocacy window is the hearing itself (June 29–July 15). The measurement infrastructure for this window is: monitor the DEA designated participant list (published approximately June 22) and verify which Phase 1 contacts are selected. If any are selected, offer to help prepare hearing testimony materials incorporating Domain 42 analysis.

**Cross-reference**: The complete Domain 42 timeline is documented in `execution/DOMAIN_42_OUTREACH_URGENCY_STRATEGY.md` and `execution/domain-42-success-tracking.md`.

---

## Section 9: Pre-Launch Setup Checklist

Complete all items before June 1 morning send. Items marked **[June 1 morning]** can be done same-day. All others should be completed May 28–31.

### Tier A: One-Time Infrastructure (Complete May 28–31)

- [ ] **Bitly links created** for all 5 Phase 1 Gists (Section 1.1). Each link tested in private browser. Clicks confirmed registering in Bitly dashboard.
- [ ] **Gmail labels created** with full nested structure (Section 1.2). Test: apply `phase1-outreach/sent/wave-1` label to a test email sent to yourself.
- [ ] **Zapier Zaps active** — Zap 1 (reply logger) and Zap 2 (bounce detector) (Section 1.2). Test: send a test email to yourself, reply to it, confirm the reply-logger Zap fires and appends a row to the Google Sheet.
- [ ] **Google Sheets workbook created** with 8 tabs (7 from existing schema + D42 DEA tab) (Section 5.1). All 45 Tier 1 + D42 contact rows populated. KPI Summary tab: all formulas confirmed returning numbers (not errors).
- [ ] **Discord webhook live** in `#phase1-metrics` channel (Section 5.2). Test message sent and received. Daily briefing script saved and tested.
- [ ] **Google Alerts created** — all 12 alert queries from Section 3.4. Delivery routing to `monitoring/google-alerts/` Gmail label confirmed.
- [ ] **CourtListener saved searches created** — all 5 searches with email alerts enabled (Section 3.1).
- [ ] **LegiScan saved searches configured** — 3 query sets, daily email notification, priority states (Section 3.3).
- [ ] **Pre-distribution baseline** recorded in `execution/phase-1-baseline-metrics.md` — run each vocabulary marker query in Google, Google Scholar, and Congress.gov; record result counts.

### Tier B: Launch-Day Verification (June 1 morning, before first send)

- [ ] **Bitly click count confirmed at 0** for all links (reset baseline — confirm no stray clicks from testing).
- [ ] **Gist view count noted** for all 6 Gists (baseline for Day 0). Record in "Gist View Log" sheet as `week_0_cumulative`.
- [ ] **Master Contact Log row 1** populated for the first Wave 1 contact (Drug Policy Alliance if sending D42, or Batch 1 if sending general Phase 1). `email_sent_date` column ready.
- [ ] **KPI Summary alert cells** all showing "OK" (not "ALERT") — confirms baseline is clean.
- [ ] **Discord daily briefing** sent manually as a Day 0 baseline message.

### Tier C: Ongoing Cadence (after launch)

- **Daily**: Check Bitly dashboard (5 min). Check Gmail `monitoring/bounce` label. Update Master Contact Log for any new replies.
- **Weekly (Monday)**: Pull Gist view analytics. Run Google Alerts sweep. Check Regulations.gov DEA-1362 docket (through June 22). Complete Weekly Review Template. Send Discord weekly summary.
- **Day 7**: Complete Day 7 Operational Check from `phase-1-adoption-tracking-automation.md` Part 6.
- **Day 28**: Congress.gov bookmark sweep. Monthly synthesis report. 30-day Decision Tree assessment (Section 6.3).
- **Day 45**: Coalition formation trigger check (Section 7, Trigger 5).
- **June 22**: DEA designated participant list published. Cross-reference against D42 contact list. Update D42 DEA Tracking tab.

---

## Appendix A: Tool Reference

| Tool | Purpose | Cost | Setup Time | URL |
|------|---------|------|------------|-----|
| Bitly | Link click tracking | Free | 15 min | bitly.com |
| Google Sheets | Master dashboard | Free | 60–90 min | sheets.google.com |
| Zapier | Gmail automation | Free (5 Zaps) | 30 min | zapier.com |
| Discord webhook | Real-time alerts | Free | 15 min | discord.com |
| Streak (optional) | Gmail open tracking | Free tier | 5 min | streak.com |
| CourtListener | Litigation citation detection | Free | 20 min | courtlistener.com |
| LegiScan | State legislative tracking | Free tier | 30 min | legiscan.com |
| Google Alerts | News and web monitoring | Free | 15 min | google.com/alerts |
| Google Scholar Alerts | Academic citation detection | Free | 10 min | scholar.google.com |
| Congress.gov | Federal legislative tracking | Free | 10 min | congress.gov |
| Regulations.gov | DEA-1362 docket monitoring | Free | 5 min | regulations.gov |
| Overton.io | Policy document citation (Month 4+) | Free registration | 10 min | overton.io |

**Total setup time** (Tier A items): approximately 3.5–4 hours. Timing recommendation: 3 hours on May 28–29, 30 minutes on June 1 morning (Tier B).

**Total ongoing time**: 25–35 minutes per week during Weeks 1–4; 15–20 minutes per week from Month 2 onward.

---

## Appendix B: Gist IDs Quick Reference

| Gist | GitHub ID | Bitly Back-Half |
|------|-----------|-----------------|
| Democratic Renewal Proposal | `2dec7fd03b08ab5b41c55d402f44c261` | `bit.ly/drp-2026` |
| Executive Summary | `2869da6eaeb15a47246ade3bbbc4a3f4` | `bit.ly/drp-summary` |
| Litigation Tracker | `418d51bda087f15a04d685ab171a5ee0` | `bit.ly/drp-litigation` |
| First Amendment Tracker | `10d0a86e386e6c3c11c3830295a6503c` | `bit.ly/drp-fa` |
| Environmental Tracker | `87e2bdb931b77480e56a08044c567bc4` | `bit.ly/drp-env` |
| Police Consent Decree Tracker | `1f5cb28527c98d12526c14302c725731` | `bit.ly/drp-pd` |
| Domain 42 DEA Briefing | `98dc61a3294a612482b37bd90f5c94ab` | `bit.ly/drp-dea42` |

---

## Appendix C: Phase 2 Expansion Notes

This document is versioned for Phase 1 (35-domain framework + Domain 42 DEA distribution, 45 Tier 1 contacts). When Phase 2 domain expansion launches (Domains 41, 42-Expansion, 43), the following measurement additions are needed:

1. **Expand D42 DEA Tracking tab** into a "Policy Window Tracking" tab that covers all domain-specific external deadlines (CFPB comment windows for Domain 41, HUD CoC NOFO for Domain 43).

2. **Add a "Phase 2 Contact Log" sheet** for Phase 2 expansion contacts (estimated 30–50 new contacts) with the same schema as the Master Contact Log.

3. **Expand Bitly link set** to include Phase 2 Gists when they are created.

4. **Expand LegiScan searches** to cover Domain 41 state rate cap legislation and Domain 43 state preemption reversal legislation.

5. **Add Regulations.gov monitoring** for CFPB formal rule rescission proceedings (Domain 41 advocacy window) alongside the existing DEA-1362 monitoring.

These Phase 2 additions require approximately 60 minutes of setup when Phase 2 distribution begins. The core infrastructure (Google Sheets, Discord, Bitly, Google Alerts, CourtListener) does not need to be rebuilt — only extended.

---

*Document version: 1.0 — May 13, 2026*
*Status: Production-ready — arm May 28–31, activate June 1*
*Relationship to existing docs: Operational layer above `phase-1-adoption-tracking-automation.md` (conceptual architecture), `adoption-automation-infrastructure.md` (column schema), and `success-metrics.md` (engagement targets). Cross-references `execution/DOMAIN_42_OUTREACH_URGENCY_STRATEGY.md` (D42 DEA timeline) and `projects/cybersecurity-hardening/PHASE_1_MEASUREMENT_AUTOMATION.md` (cross-project coordination).*
