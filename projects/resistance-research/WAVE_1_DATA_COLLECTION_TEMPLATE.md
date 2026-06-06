---
title: "Wave 1 Data Collection Template"
subtitle: "15-Minute Weekly Operational Checklist — June 16 through August 8"
created: "2026-06-06"
version: "1.0"
status: "production-ready — execute starting June 16 (Day 7 checkpoint)"
scope: >
  Operational data collection checklist for Wave 1 impact tracking. 15 minutes per week.
  Covers email engagement, Bitly click tracking, GitHub Gist/fork data, open-web monitoring,
  and decision gate escalation triggers. Structured for copy-paste completion.
word_count: "~1,050"
companion_files:
  - WAVE_1_IMPACT_MEASUREMENT_FRAMEWORK.md
  - WAVE_1_PHASE_2_SEQUENCING_DECISION_MATRIX.md
  - DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md
purpose: >
  Keeps total measurement overhead at 15 minutes per week. Pre-identifies every data source,
  lookup procedure, and decision gate. The person running this on June 16 needs no prior
  context — all steps are self-contained.
---

# Wave 1 Data Collection Template

**Version 1.0 — June 6, 2026**

**How to use**: Run this checklist every Monday during the active monitoring period (June 16 – August 8). At Day 7 (June 16), also run DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md for the full composite score calculation — that document takes an additional 15 minutes and is the primary decision gate. The weekly template here is the ongoing maintenance checklist, not the one-time gate.

**Total time per week**: 15 minutes, broken into four steps.

---

## Weekly Run Schedule

| Week | Date | Day Number | Priority |
|------|------|-----------|---------|
| Week 1 | June 16 | Day 7 | DAY 7 CHECKPOINT — run both this checklist AND DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md |
| Week 2 | June 23 | Day 14 | Standard weekly run |
| Week 3 | June 30 | Day 21 | Standard weekly run |
| Week 4 | July 7 | Day 28 | Pre-Day-30 data collection |
| Week 5 | July 9 | Day 30 | DAY 30 CHECKPOINT — run both this checklist AND Day 30 review in WAVE_1_IMPACT_MEASUREMENT_FRAMEWORK.md Section 5 |
| Week 6 | July 14 | Day 35 | Standard weekly run |
| Week 7 | July 21 | Day 42 | Standard weekly run |
| Week 8 | August 8 | Day 60 | DAY 60 CHECKPOINT — final impact assessment |

---

## Step 1: Email Inbox Audit (5 minutes)

**Open Gmail. Run this search**: `from:(campaignlegal OR issueone OR commoncause OR lwvc OR cleanmoney) after:2026/06/09`

For each reply found since last Monday, complete one row in the log below:

| Date Found | Organization | Contact | Reply Type | Score (1–5) | Key Content Keywords | Action Required? |
|-----------|-------------|---------|-----------|------------|----------------------|-----------------|
| | | | OOO / Form / Substantive / Forward / Adopt | | | Y / N |
| | | | | | | |
| | | | | | | |

**Reply scoring reference** (copy from DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md):
- **1**: OOO only
- **2**: Form acknowledgment, no substantive content
- **3**: Substantive — domain-specific question or reference to current organizational work
- **4**: Forward or network multiplier — names a colleague or sends to a team
- **5**: Explicit adoption — "We will use/cite/integrate this in [specific project]"

**High-value content keywords to flag immediately**:
- "FEC enforcement" / "200-day shutdown" — CLC litigation integration signal
- "DISCLOSE Act markup" / "DISCLOSE Act timeline" — legislative urgency signal
- "AI PAC" / "Fairshake" / "OpenAI PAC" — Issue One bipartisan angle confirmed
- "Fair Elections Act" / "SB-42" / "Californians for Fair Elections" — ballot campaign integration signal
- "Citizens United architecture" / "dark money" — general framework engagement confirmed
- Any colleague name or organization referral — network multiplier event, log separately

**If any Score 5 reply found**: Stop. Update CHECKIN.md under "Needs Your Input" immediately. Do not wait for the weekly checkpoint. Note the organization, contact, and adoption specifics. This triggers STRONG override regardless of other metrics.

**If any reply references a specific deadline or filing**: Flag as urgency indicator. A contact mentioning a court date, hearing, or publication deadline within their reply upgrades the effective score by 0.5 (a Score 3 with a deadline reference functions as Score 3.5 for Phase 2 decision purposes).

**Action items from email audit**:
- [ ] Score 3+ replies requiring substantive response: ___
- [ ] Referrals to follow up: ___
- [ ] Adoption signals to log in Adoption Signal Registry: ___

---

## Step 2: Bitly Click Data Pull (3 minutes)

**URL**: bitly.com/a/dashboard

**Step-by-step**:
1. Log in to Bitly
2. Locate the Domain 51 short link (back-half: domain51-campaign-finance or equivalent per DISTRIBUTION_GIST_URLS.md)
3. Click on the link name to open link analytics
4. Select "Clicks" tab
5. Record daily click counts for the 7-day window since last Monday

| Date | Clicks | Notes |
|------|--------|-------|
| Monday (last week) | | |
| Tuesday | | |
| Wednesday | | |
| Thursday | | |
| Friday | | |
| Saturday | | |
| Sunday | | |
| **Week Total** | | |
| **Cumulative Total** | | Running sum from June 9 baseline |

**Spike detection** (mark YES if any single day shows 5+ clicks):
- Spike detected this week: YES / NO
- Spike date: ___
- Correlation to send activity: Within 72h of a send = delivery confirmed. Organic (no corresponding send) = network amplification event.
- Flag organic spike in CHECKIN.md: YES / NO

**Velocity interpretation**:
- Clicks concentrated in first 3 days after a send = initial read-through, no forwarding
- Clicks distributed evenly or rising in Days 4–7 = forwarding occurring, organic circulation
- Zero clicks in a week where no new sends occurred = organic engagement has ended for this period (expected after Day 14 if no organic circulation has started)

---

## Step 3: GitHub Gist / Fork / Star Check (3 minutes)

**Gist URL**: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

**Navigate to Gist page. Record**:

| Metric | Current Count | Last Week Count | Delta | Notes |
|--------|--------------|----------------|-------|-------|
| Forks | | | | New fork = Score 4 equivalent signal |
| Stars | | | | New star from named/org-linked account = Score 3 signal |
| GitHub view count (if visible) | | | | Only available if author-authenticated view data accessible |

**Fork attribution**: If a new fork appeared since last Monday, check the forking account's profile. If the account is linked to any Wave 1 organization or campaign finance / democracy advocacy domain, log it as a confirmed adoption signal. A fork from a generic or unattributable account has lower signal weight but still warrants a note.

**If any fork detected**: Log in the Adoption Signal Registry (PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md format). Record: date detected, account name, likely organization affiliation (if determinable), signal type (Fork = adaptation intent).

---

## Step 4: Web Monitoring and Open-Web Sweep (4 minutes)

**4a. Google Alerts check** (1 minute):
- Check Gmail label for Google Alert notifications since last Monday
- Alerts active: "campaign finance dark money architecture" OR "FEC enforcement shutdown" OR "AI PAC campaign finance" OR "Domain 51 democratic renewal"
- Any new alert: verify the source, confirm it references Wave 1 materials or vocabulary, log as open-web amplification signal

**4b. CLC publication check** (1 minute):
- campaignlegal.org/publications — scan for any new publication since last check that references FEC enforcement, dark money architecture, or AI PAC proliferation
- If found: check whether Domain 51 vocabulary appears. If yes, log as delayed adoption signal even if no direct reply was received.

**4c. Issue One publication check** (1 minute):
- issueone.org/news — scan for any new publication, ReFormers Caucus update, or DISCLOSE Act commentary
- If any publication uses "AI PAC," "Fairshake template," or "dark money reporting gap" vocabulary from Domain 51, log as adoption signal

**4d. California ballot campaign check** (1 minute):
- yesfairelections.org and californiansforairelections.org (or current campaign committee URL) — check for any new research citations, policy briefs, or campaign communications
- Any document published by the campaign coalition that cites the Citizens United architecture analysis, AI PAC proliferation data, or dark money reporting gaps from Domain 51 constitutes a Type B adoption signal

**Open-web findings log** (enter any new findings):

| Date | Source | URL | Signal Type | Domain 51 Vocabulary Used | Log in Adoption Registry? |
|------|--------|-----|-------------|--------------------------|--------------------------|
| | | | Publication / Alert / Social | | Y / N |
| | | | | | |

---

## Decision Gates: When to Escalate

The following conditions require immediate action outside the weekly checklist cycle. Check these gates at every weekly run and immediately if any alert arrives outside the schedule.

### Gate 1: Score 5 Override (Act Immediately)
**Trigger**: Any contact sends an explicit adoption statement — citing Domain 51 in a specific publication, filing, testimony, or campaign communication.
**Action**: Update CHECKIN.md "Needs Your Input" within the hour. Proceed to WAVE_1_PHASE_2_SEQUENCING_DECISION_MATRIX.md STRONG path immediately. Do not wait for the next weekly check.

### Gate 2: California July 1 Window Closing (Act by June 30)
**Trigger**: June 30 arrives with zero substantive engagement (Score 3+) from California ballot campaign contacts (Common Cause CA, LWV CA, or Clean Money Action Fund).
**Action**: The ballot campaign messaging development window closes approximately July 1. On June 25, send a single 2-sentence follow-up to Common Cause CA only: "Following up on the research I shared June 11 — the July 1 messaging window is approaching and I wanted to make sure it reached the right person." Log follow-up send date. Do not send to LWV CA or Clean Money Action Fund.

### Gate 3: Composite Score Below 3 at Day 7 (Act within 2 hours)
**Trigger**: DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md composite score is below 3.
**Action**: Run infrastructure diagnostic immediately (email delivery confirmation, Gist URL accessibility, Bitly link test). Do not draw content conclusions until infrastructure is cleared. Log diagnostic results in CHECKIN.md. Escalate to user if delivery is confirmed but engagement is zero.

### Gate 4: Organic Spike Without Corresponding Send (Act within 24 hours)
**Trigger**: Bitly spike of 5+ clicks on a day where no new send occurred.
**Action**: Note the spike date and volume. Check DISTRIBUTION_GIST_URLS.md and DISTRIBUTION_EXECUTION_LOG.md for any send activity within the prior 72 hours. If truly organic: this is a network amplification event. Log in the Adoption Signal Registry as "organic amplification — referral or forwarding from Wave 1 contact." Upgrade Wave 1 classification if cumulative organic spikes support MODERATE-to-STRONG upgrade.

### Gate 5: Hard Bounce on Any Tier A Contact (Act within 24 hours)
**Trigger**: Hard bounce notification from CLC (ymaluf@campaignlegalcenter.org or info@campaignlegal.org) or Issue One (npenniman@issueone.org or info@issueone.org).
**Action**: Verify alternate contact. CLC secondary: check campaignlegal.org/our-team for current campaign finance staff. Issue One secondary: check issueone.org/about/team. Re-send to verified alternate address within 24 hours. Log re-send in DISTRIBUTION_EXECUTION_LOG.md. A bounce on a Tier A contact does not constitute WEAK signal — it is an infrastructure problem with a mechanical fix.

### Gate 6: July 15 Domain 50 Hard Deadline Pressure (Act by July 15)
**Trigger**: July 15 arrives and Domain 50 (LGBTQ+ Rights, Lambda Legal / AT4E) distribution infrastructure is not verified ready.
**Action**: Per PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md Checkpoint 4, Domain 50's August 1 ballot campaign deadline is the hardest deadline in Phase 2. If any execution friction in Domain 50 preparation appears by July 15, deprioritize Domain 49 preparation and focus exclusively on Domain 50. Log escalation in CHECKIN.md.

---

## Adoption Signal Registry (Running Log)

Enter each confirmed adoption event here. This log accumulates across all weekly runs and feeds the Day 30 and Day 60 checkpoint assessments.

| Signal_ID | Date | Organization | Type | Domain | Evidence Source | Verification | People Reached (Est.) |
|-----------|------|-------------|------|--------|----------------|--------------|----------------------|
| WAS001 | | | | 51 | | Confirmed / Probable | |
| WAS002 | | | | | | | |

**Signal types**: Curriculum / Litigation Toolkit / Policy Brief / Campaign Communication / Testimony / Training Module / Forward/Referral / Citation / Other

**People Reached estimates by organization type**:
- CLC publication: 1,000–5,000 (subscriber base + policy audience)
- Issue One ReFormers Caucus communication: 500–2,000 (former member network + congressional staff)
- Common Cause CA campaign communication: 5,000–50,000 (full coalition supporter base)
- LWV CA voter education publication: 2,000–10,000
- Clean Money Action Fund communication: 1,000–5,000

**Day 60 threshold check**: At Day 60 (August 8), total estimated People Reached should exceed 100. One confirmed CLC publication or Common Cause CA campaign communication exceeds this threshold alone.

---

*Template prepared June 6, 2026. Active monitoring period: June 16 – August 8, 2026. Total measurement overhead: 15 min/week for standard weeks, 30 min for checkpoint weeks (Day 7, Day 30, Day 60). Companion decision documents: WAVE_1_IMPACT_MEASUREMENT_FRAMEWORK.md (thresholds and methodology), WAVE_1_PHASE_2_SEQUENCING_DECISION_MATRIX.md (Phase 2 routing from checkpoint outputs).*
