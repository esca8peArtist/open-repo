---
title: "Wave 1 Synthesis Framework — May 21 Decision Instrument (Item 61)"
item: "61"
created: 2026-05-18
revised: 2026-05-18
status: PRODUCTION-READY — execute May 21, 10:30–14:00 UTC without consulting any other document
scope: "72-hour signal aggregation, STRONG/MODERATE/WEAK classification with exact thresholds, Phase 2 pathway per outcome, Batch 2-3 timing triggers, May 21 decision gate checklist, contingency scenarios"
audience: "thorn — standalone. No other file required at the May 21 decision point."
monitoring_window: "May 18 10:32 UTC — May 21 10:30 UTC (72 hours)"
decision_gate: "May 21 14:00 UTC (Phase 2 path confirmed by user)"
companion_files:
  - WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md  # deeper signal logic and 12-item May 25 checklist
  - MAY_21_31_BATCH_2_3_COORDINATION_FRAMEWORK.md       # full Batch 2-3 contact lists and templates
  - DOMAIN_42_AMPLIFICATION_STRATEGY.md                 # DEA hearing coordination (path-independent)
  - WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv            # raw signal log
  - WAVE_1_MONITORING_DASHBOARD.md                      # daily tracking and sector breakdowns
  - WAVE_1_CONTINGENCY_DECISION_TREE.md                 # constituency-weighted CRS calculation for May 25
---

# Wave 1 Synthesis Framework — May 21 Decision Instrument (Item 61)

**What this document is**: The single operational guide for May 21, 10:30–14:00 UTC. Read it top to bottom. It tells you which signals to collect, how to weight them, how to classify the result, and exactly what to do next under each outcome. You do not need to open any other file to make the Phase 2 path decision.

**What this document is not**: A monitoring log or historical record. The raw data lives in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv and WAVE_1_MONITORING_DASHBOARD.md. This document processes that data into a decision.

**Timeline this document governs**:

| Time (UTC) | Action |
|---|---|
| 10:30 | Monitoring window closes. Collect the 7 key metrics (Section 2). |
| 10:45 | Run signal aggregation formula. Calculate Classification Score. |
| 11:00 | Map score to STRONG / MODERATE / WEAK (Section 3). Log classification. |
| 11:15 | Activate corresponding Batch 2-3 path (Section 4). Update CHECKIN.md. |
| 11:30–13:30 | Execute path-specific immediate actions. Queue sends. |
| 14:00 | User reviews classification and confirms Phase 2 path (Section 6). No research begins without this confirmation. |

---

## EXECUTIVE QUICK REFERENCE

### The 7 Metrics You Need at 10:30 UTC

Open your email inbox, Bitly dashboard, and Gist analytics simultaneously. Record every number before touching anything else.

| # | Metric | Where to Find It | Your Number |
|---|---|---|---|
| 1 | Hard bounces | Bounce notifications in inbox | ___ of 5 |
| 2 | OOO autoreplies | Inbox auto-replies | ___ of 5 |
| 3 | Adjusted contact count (5 minus bounces minus OOOs) | Calculate | ___ |
| 4 | Substantive replies — Score 3+ (clarification question, critique, implementation ask, referral, or integration signal) | Inbox | ___ of adjusted count |
| 5 | Integration / referral signals — Score 4-5 specifically | Inbox — review all replies for these | ___ contacts |
| 6 | Institutional reply rate (Score 3+ / adjusted count × 100) | Calculate | ___% |
| 7 | Gist view delta (all tracked Gist URLs, total views above May 18 baseline) | Bitly dashboard | +___ views |

**Score reference (what qualifies as each level)**:

- Score 5 (Integration): Contact cited the research in a filing, brief, publication, testimony, or offered formal collaboration. ONE Score 5 = STRONG regardless of all other metrics.
- Score 4 (Implementation / Referral): Contact asked how to operationalize the framework, OR said they are forwarding it to a colleague, a network, or an AG contact.
- Score 3 (Substantive): Contact asked a specific question referencing a domain by number, OR raised a substantive methodological critique.
- Score 1-2 (Acknowledgment): "Thanks, will read" or generic interest. Does NOT qualify as a substantive reply.
- Score 0 (Silence): No reply. Expected for law school contacts (Goodman, Chenoweth) through Day 10. Normal for policy org contacts through Day 5.

**Law school silence adjustment**: At 10:30 UTC May 21, Goodman (NYU) and Chenoweth (Harvard Kennedy) have been in-window for 72 hours. Their sector norm is 5-10 days. Silence from them at 72 hours is within expectations and does not count against the institutional reply rate. The classification window for law school contacts extends to May 28 (Day 10). The primary signal sources at this gate are the three non-law-school contacts: Weiser (Brennan Center), Bassin (Protect Democracy), and Elias (Democracy Docket).

---

### One-Minute Classification Pre-Check

Before running the full formula, answer these three questions in order. The first YES terminates the process:

```
1. Has ANY contact produced a Score 5 (Integration) signal?
   YES → STRONG. Skip to Section 4A immediately.
   NO  → Continue.

2. Is the institutional reply rate 60% or above AND are there 3 or more integration signals (Score 4-5)?
   YES → STRONG. Go to Section 4A.
   NO  → Continue.

3. Is the institutional reply rate between 30% and 59%, OR are there 1-2 integration signals?
   YES → MODERATE. Go to Section 4B.
   NO (rate below 30% and zero integration signals) → Continue to full formula in Section 3.
```

---

### One-Line Activation Summary Per Path

| Classification | Batch 2 | Phase 2 Research | Domain 42 |
|---|---|---|---|
| STRONG | Launch Batch 2 immediately today (May 21) — social proof framing, ~20 sends | Begin Domain 57 + Domain 59 by May 25 | Full amplification — all 5 DEA orgs accelerated |
| MODERATE | Schedule Batch 2 May 21-22, standard urgency framing | Domain 39 June 1; Domain 57 June 8 (12-week timeline) | Standard coordination — materials by May 22 |
| WEAK | HOLD Batch 2 — post-mortem required first | Domain 37 supplement immediate; Domain 39 no later than June 8 | Accelerated DEA push regardless of classification — May 28 hard deadline |

---

## SECTION 1: Monitoring Window Baseline — What Was Expected

### 1.1 Batch 1 Contacts

All 5 emails sent May 18, 08:00–10:00 UTC. Monitoring window: May 18 10:32 UTC through May 21 10:30 UTC (72 hours).

| Contact | Institution | Sector | 72h Expectation | Notes |
|---|---|---|---|---|
| Ryan Goodman | Just Security / NYU Law | Law School | Silence within sector norms through Day 10 | Do not penalize silence at 72h gate |
| Wendy Weiser | Brennan Center | Policy Org | Full response window open; reply plausible | SAVE Act litigation framing; 2-5 day cycle |
| Erica Chenoweth | Harvard Kennedy School | Law School | Silence within sector norms through Day 10 | Do not penalize silence at 72h gate |
| Ian Bassin | Protect Democracy | Policy Org | Full response window open; end of primary window | Constitutional litigation focus; May 21 is the outer edge |
| Marc Elias | Democracy Docket / Elias Law | Litigation / Legal | Fastest likely responder; full window closed | Callais cascade framing has topical urgency; silence at 72h is a weak signal |

### 1.2 Performance Benchmarks

These numbers calibrate the thresholds. When you calculate your metrics at 10:30 UTC, these are the reference points:

- Mass nonprofit email baseline (M+R Benchmarks 2026): 1.4% reply rate
- Targeted cold outreach, 5-25 personalized recipients (Hunter.io 2026): 6.2% reply rate
- Applied multiplier for Batch 1 depth of personalization: ~8-10% per-contact reply probability within 72 hours for policy org contacts
- Batch 1 success threshold: 40% reply rate (2 of 5) = strong relative to all benchmarks; 20% (1 of 5) = minimum viable; 0% = delivery diagnosis required before content diagnosis

**At 5 contacts, the numbers are small and each reply moves the rate substantially. 1 reply = 20% rate. 2 replies = 40% rate. 3 replies = 60% rate.** This is why the quality of each individual reply matters as much as the count.

### 1.3 Expected Signal Distribution at 72 Hours

Under normal conditions at the 72-hour gate:
- Policy org contacts (Weiser, Bassin, Elias): full response window has elapsed — any reply or silence is interpretable
- Law school contacts (Goodman, Chenoweth): response window is NOT complete — silence is not a signal

**Adjusted analytical universe at May 21 10:30 UTC**: 3 contacts (Weiser, Bassin, Elias) are in their primary window. 2 contacts (Goodman, Chenoweth) are in their secondary window (extends through May 28). Classification is based on 3-contact performance, not 5.

If any of the 5 contacts have produced a reply (including law school contacts who responded faster than expected), score and count them normally. Do not exclude law school contacts who chose to respond early — exclusion applies only to non-response, not to early engagement.

---

## SECTION 2: Signal Aggregation Protocol

### 2.1 Signal Collection Table

Complete every row before calculating anything. This is the authoritative May 21 10:30 UTC snapshot.

| Contact | Sector | Reply? | Reply Type | Score (0-5) | Gist Clicked? | OOO? | Bounce? | Quality Points |
|---|---|---|---|---|---|---|---|---|
| Ryan Goodman | Law School | Y / N | | | Y / N | Y / N | Y / N | |
| Wendy Weiser | Policy Org | Y / N | | | Y / N | Y / N | Y / N | |
| Erica Chenoweth | Law School | Y / N | | | Y / N | Y / N | Y / N | |
| Ian Bassin | Policy Org | Y / N | | | Y / N | Y / N | Y / N | |
| Marc Elias | Litigation | Y / N | | | Y / N | Y / N | Y / N | |

**Quality Points per contact**:
- Score 5 = STRONG OVERRIDE — stop, record STRONG, go to Section 4A
- Score 4 = 2 quality points
- Score 3 = 1 quality point
- Score 1-2 = 0 quality points (delivery confirmed only)
- Score 0, no bounce, no OOO = 0 quality points
- OOO: remove this contact from adjusted count; record return date; add follow-up date (return + 1 business day)
- Bounce: remove this contact from adjusted count; identify alternate address within 24 hours; log in DISTRIBUTION_EXECUTION_LOG.md

**Running totals**:

| Metric | Your Value |
|---|---|
| Total hard bounces | ___ |
| Total OOO contacts | ___ |
| Adjusted contact count (5 − bounces − OOOs) | ___ |
| Contacts with Score 3+ replies | ___ |
| Institutional reply rate (Score 3+ / adjusted count × 100) | ___% |
| Integration signals received (Score 4 or 5 count) | ___ |
| Total quality points (sum of column above) | ___ |

### 2.2 Gist Delta Aggregation

Check every Gist URL in DISTRIBUTION_GIST_URLS.md against its May 18 pre-send baseline (recorded before 08:00 UTC May 18). If no baseline was recorded, use the earliest available Bitly timestamp after 08:00 UTC May 18 as a proxy.

| Gist URL / Topic | May 18 Baseline Count | Current Count (10:30 UTC May 21) | Delta |
|---|---|---|---|
| Gist 1: | | | |
| Gist 2: | | | |
| Gist 3: | | | |
| Gist 4: | | | |
| Gist 5: | | | |
| **TOTAL DELTA** | | | **___** |

**Gist delta bonus** (adds to quality points, capped at 1.0 total from Gist):
- Total Gist delta ÷ 5 = ___ (round down)
- Cap at 1.0: ___
- Add to total quality points

**Adjusted total quality points (including Gist bonus)**: ___

### 2.3 Signal Weighting Logic

The signal hierarchy, from least to most impactful:

| Signal | What It Proves | Weight in Classification |
|---|---|---|
| Gist view delta above baseline | Delivery working; content being read — proxy for engagement | 0.5 quality points per 5 views, capped at 1.0 total |
| Acknowledgment only (Score 1-2) | Confirmed delivery; no content engagement yet | 0 quality points — does not count as substantive reply |
| Substantive question / critique (Score 3) | Content is being engaged seriously; contact is reading carefully enough to form a question | 1 quality point; counts toward reply rate |
| Implementation / referral signal (Score 4) | Contact sees operational utility; is acting on the research by forwarding or asking how to use it | 2 quality points; counts toward reply rate AND integration signal count |
| Integration signal (Score 5) | Contact has confirmed adoption in actual work product | STRONG OVERRIDE — bypasses all other metrics |

**Why the weighting is asymmetric**: A single Score 5 signal changes the strategic situation in a way that no number of Score 3 signals can match. If Elias cites a domain in a brief, or Weiser invites the framework into a Brennan Center report, the research has achieved institutional embedding. That is the Phase 2 goal. An accumulation of "looks interesting" replies does not achieve that goal. The weighting reflects this reality.

### 2.4 Sector-Level Signal Analysis

After completing the contact table, analyze which sectors are producing signals. This shapes Batch 2 framing regardless of classification.

| Sector (Batch 1 contacts) | Replied Substantively? | Signal Strength | What This Means for Batch 2 |
|---|---|---|---|
| Law School (Goodman, Chenoweth) | Y / N / Window still open | | If yes (unexpected): academic framing is landing. Lead Batch 2 law school contacts with domain numbers that resonated. |
| Policy Org (Weiser, Bassin) | Y / N | | If yes: policy urgency framing is working. Batch 2 policy org contacts get same urgency hook. |
| Litigation (Elias) | Y / N | | If yes: operational/case framing is working. Priority for Batch 2 litigation and legal aid contacts. |

### 2.5 Ancillary Signal Check

If email signals are sparse, check these before concluding WEAK:

| Signal | Where to Check | What a Positive Means |
|---|---|---|
| Gist view spike (single Gist +10 or more views) | Bitly dashboard → specific link | Content being read internally; likely forwarded — moderate confirming signal |
| Social media mention | LinkedIn, X — search proposal-related terms | Amplification signal; rare at 72h but significant if present |
| Media pickup | Google News — "DEA hearing democratic exclusion" or similar | Domain 42 press contact working |
| DEA-1362 docket participation notices | nprm@dea.gov docket check | One of the Domain 42 sub-batch orgs filed — direct action signal |

---

## SECTION 3: STRONG / MODERATE / WEAK Classification Logic

### 3.1 Primary Thresholds

These are the classification gates used in this framework. They are more conservative than the "default calibrated" thresholds in WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md and reflect the task-specified parameters.

| Outcome | Institutional Reply Rate | Integration Signals (Score 4-5) | Logic |
|---|---|---|---|
| STRONG | ≥60% (3 of 5 contacts, or 3 of adjusted count) | ≥3 integration signals by May 21 10:30 UTC | Both conditions must be met unless Score 5 override applies |
| MODERATE | 30-59% (1-2 of 5 contacts) OR 1-2 integration signals | 1-2 integration signals (either/or with rate) | Either rate OR signal count qualifies |
| WEAK | <30% (0 contacts with Score 3+) OR 0 integration signals | 0 integration signals | Neither threshold reached |

**Score 5 override**: Any single Score 5 (Integration) signal from any contact at any time before 10:30 UTC May 21 triggers STRONG immediately, regardless of all other metrics. This override rule supersedes the institutional reply rate and integration signal count requirements.

### 3.2 Classification Decision Table

Run this table top to bottom. Stop at the first row that applies.

| Priority | Condition | Classification | Next Step |
|---|---|---|---|
| 1 (override) | Any contact produced Score 5 (Integration signal confirmed) | STRONG | Go to Section 4A immediately — no further calculation needed |
| 2 | Institutional reply rate ≥60% AND integration signals ≥3 | STRONG | Go to Section 4A |
| 3 | Institutional reply rate ≥60% AND integration signals 1-2 AND total quality points ≥4 | STRONG | Go to Section 4A — high rate with some integration depth |
| 4 | Institutional reply rate 30-59% AND integration signals ≥1 | MODERATE | Go to Section 4B |
| 5 | Institutional reply rate 30-59% AND integration signals = 0 | MODERATE | Go to Section 4B — note "lower end MODERATE" |
| 6 | Institutional reply rate <30% AND integration signals 1-2 | MODERATE | Go to Section 4B — note "integration-only MODERATE, rate below threshold" |
| 7 | Institutional reply rate <30% AND integration signals = 0 AND Gist delta >10 | MODERATE (borderline) | Go to Section 4B — note "borderline, delivery working, conversion pending" |
| 8 | Institutional reply rate <30% AND integration signals = 0 AND Gist delta ≤5 | WEAK — run delivery check first | Go to Section 3.3 before confirming |
| 9 | Institutional reply rate <30% AND integration signals = 0 AND Gist delta = 0 AND zero bounces | WEAK — likely technical failure | Go to Section 3.3; suspect spam filter |
| 10 | ≥2 hard bounces AND Institutional reply rate = 0% | PAUSE — do not classify | Fix delivery. Resend to verified alternate addresses. Re-run table after resends. |

**Your classification (10:45 UTC)**: ___________________
**Priority row matched**: ___________________

### 3.3 Delivery Check Protocol (Required Before Confirming WEAK)

Do not confirm WEAK until this check is complete. Zero replies + zero Gist delta + zero bounces across 5 targeted personalized emails is more likely a technical delivery failure than a content or contact quality failure.

**Step 1**: Send a test email to yourself from the same sending account. Check whether it lands in inbox or spam.
- Inbox: delivery is working. Proceed to WEAK classification.
- Spam: technical failure. Do NOT classify the content as failed. Fix sender reputation before any further sends. Log in CHECKIN.md under "Needs Your Input — Technical."

**Step 2**: Check Bitly for any click data. Zero clicks + zero opens + zero replies + zero bounces at 72 hours = spam filter interception is the leading explanation, not disengagement.

**Step 3**: Only confirm WEAK if delivery test confirms email is reaching inbox. Log result here: ___________________

### 3.4 Law School Silence Adjustment

If Goodman and Chenoweth have not replied: log this explicitly in the classification record.

Required language: "Law school response window (Goodman, Chenoweth) remains open through May 28, 2026 (Day 10). Silence at 72h is within sector norms. Classification does not count law school non-response at this gate. Law school signals will be incorporated at the May 25 secondary gate."

If either law school contact has replied (unexpected but positive): score them normally and include their signal in the institutional reply rate calculation.

### 3.5 Classification Record (Complete at 10:45 UTC)

```
CLASSIFICATION: ___________________
Confirmed at: ___ UTC, May 21, 2026
Classification rule (priority row from Section 3.2): Row ___

Metrics at classification:
  Institutional reply rate: ___%
  Integration signals (Score 4-5): ___
  Total quality points: ___
  Adjusted contact count: ___
  Gist delta: ___
  Hard bounces: ___
  OOO contacts (pending): ___

Law school window: OPEN through May 28 (Day 10)
Law school contacts replied: YES / NO
Delivery check: PASSED / FAILED / NOT REQUIRED (non-WEAK outcome)

Notes (any atypical signals or ambiguities):
___________________
```

---

## SECTION 4: Phase 2 Pathway Per Outcome

### 4A: STRONG Path — Launch Immediately

**What STRONG means**: Institutional contacts are engaging at a rate that validates the research framing and creates social proof leverage. The momentum window is open. Every day of delay reduces the value of the Tier 1 engagement signal that Batch 2 will lead with.

**Immediate actions (11:00–13:30 UTC May 21)**:

**Step 1 — Log and flag**:
1. Log STRONG classification in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv row 61 (Final column)
2. Flag in CHECKIN.md: "STRONG outcome confirmed at May 21 10:45 UTC. Phase 2 June 1 start pending user approval at 14:00 UTC. Batch 2 queued for immediate send."
3. Record which contacts produced the qualifying signals (by name and score) — this verbatim data is the social proof framing material for Batch 2

**Step 2 — Queue Batch 2 sends**:

Open MAY_21_31_BATCH_2_3_COORDINATION_FRAMEWORK.md Section 3A for the full STRONG path contact list. Priority Group 1 sends execute today:

| Contact | Institution | Domain Framing | Send Order |
|---|---|---|---|
| Nicholas Stephanopoulos | Harvard Law — election law | Domain 1/37 | 1 |
| Lydgate / States United Democracy Center | Voting rights organization | Domain 37 urgency | 2 |
| Shahrzad Shams | Roosevelt Institute | Domain 2/26 | 3 |
| Damon Hewitt | Lawyers' Committee for Civil Rights | Domain 1/22 | 4 |
| Janai Nelson | NAACP LDF | Domain 22/1/14 | 5 |

Stagger sends 30 minutes apart. Total Batch 2 May 21 STRONG sends: Priority Group 1 (~5) + Priority Group 2 (~5-10) = approximately 10-15 sends today, remainder May 22-23.

**Step 3 — Batch 2 STRONG framing**:

Lead with social proof, not urgency. Template opening: "Following initial distribution to institutional contacts including [name institution only — e.g., 'Brennan Center,' 'Protect Democracy,' 'Democracy Docket'] — do not name individual contacts without their implicit consent — we are extending this research framework to [Batch 2 contact's sector]..."

The engagement signal type (e.g., "implementation question about Domain 37" or "referral to an AG coalition") can be described without naming the specific contact. Their reply itself constitutes consent to describe the engagement type.

**Step 4 — Domain 42 state AG sends (path-independent, execute regardless)**:
- Kris Mayes, Arizona AG (azag.gov)
- Rob Bonta, California AG (oag.ca.gov)
- Phil Weiser, Colorado AG (coag.gov)
- Dana Nessel, Michigan AG (michigan.gov/ag)
- Nick Brown, Washington AG (atg.wa.gov)

These 5 go today under all classifications. May 28 DEA-1362 deadline is 7 days away. Use Domain 42 urgency framing from DOMAIN_42_AMPLIFICATION_STRATEGY.md.

**Step 5 — Phase 2 research authorization**:
This requires user confirmation at 14:00 UTC. Flag the following for the 14:00 gate:
- Domain 57 (Multilateral Withdrawal): research begins May 25
- Domain 59 (Economic Precarity): research begins May 25 in parallel
- Domain 39 (Healthcare): research begins June 1 (hard anchor — HHS interim Medicaid work requirements rule effective June 1, regardless of path)
- Domain 38 (AI Regulatory Capture): research begins June 8

**Full STRONG path cadence**:

| Date | Action | Contact Count |
|---|---|---|
| May 21 (today) | Batch 2 Priority Groups 1-2 + Domain 42 state AGs | ~15-20 sends |
| May 22-23 | Batch 2 Priority Group 3 (media: AP, Reuters, Axios, Filter, NORML News) | ~10 sends |
| May 24 | Batch 3 labor unions (CWA, SEIU, AFL-CIO, AFSCME, Jobs With Justice) | ~12 sends |
| May 25 | Phase 2 research begins: Domain 57 + Domain 59 | Research sprint |
| May 25-27 | Batch 3 civil rights orgs (NAACP LDF batch 2, ACLU VRP, Color of Change, M4BL) | ~8 sends |
| May 27 | Batch 3 remaining (Teamsters, NEA, AFT, USW, AEI bipartisan, state AGs 6-11) | ~15 sends |
| June 1 | Domain 39 research begins (non-negotiable HHS anchor) | Research sprint |
| June 8 | Domain 38 research begins | Research sprint |
| August 10 | Domain 57 distribution to UNGA 81 contacts | Distribution |

---

### 4B: MODERATE Path — Batch 2 on Schedule

**What MODERATE means**: Expected performance. The outreach is working but has not yet generated the institutional depth that triggers social proof framing. Law school contacts are still in their window. Proceed with Batch 2 on original schedule using urgency framing rather than social proof.

**Immediate actions (11:00–13:30 UTC May 21)**:

**Step 1 — Log and flag**:
1. Log MODERATE classification in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv row 61
2. Flag in CHECKIN.md: "MODERATE outcome at May 21 10:45 UTC. Batch 2 queued for May 21-22 standard framing. Phase 2 standard timeline pending user approval at 14:00 UTC."
3. Note which sector produced the signal — this shapes Batch 2 framing prioritization

**Step 2 — Queue Batch 2 sends**:

Open MAY_21_31_BATCH_2_3_COORDINATION_FRAMEWORK.md Section 3B for the MODERATE path contact list. Priority sends May 21-22:

| Contact | Institution | Domain Framing | Send Date |
|---|---|---|---|
| Olatunde Johnson | Columbia Law | Domain 2/6/29 | May 21 |
| Gillian Metzger | Columbia Law | Domain 2/26/34 | May 21 |
| Kenji Yoshino | NYU Law | Domain 7/22 | May 22 |
| Theda Skocpol | Harvard Kennedy | Domain 3 | May 22 |
| Richard Hasen | UCLA Law | Domain 1/33/37 | May 21 — fastest academic responder |

Stagger sends 30 minutes apart.

**Step 3 — Batch 2 MODERATE framing**:

Lead with policy window urgency, not social proof (social proof is thin at MODERATE). Template opening: "With the HHS interim rule on Medicaid work requirements now in effect, this research framework directly addresses the state-level implementation gap that advocacy organizations face through August 2026. Domain [X] maps directly to [contact's published work or institutional focus]."

Reference specific external deadlines — June 1 HHS, August 10 UNGA 81, November 3 midterms — to create urgency independent of social proof.

**Step 4 — Domain 42 state AG sends (path-independent, execute regardless)**:
Same 5 state AG contacts as STRONG path. Execute today. May 28 deadline is 7 days away.

**Step 5 — Phase 2 research authorization (12-week timeline)**:
Flag for 14:00 UTC user confirmation:
- Domain 37 supplement: update existing Gist May 25 (1-2 hour task, not a full sprint)
- Domain 39 (Healthcare): research begins June 1 (hard anchor)
- Domain 57 (Multilateral Withdrawal): research begins June 8
- Domain 59 (Economic Precarity): research begins June 15
- Domains 38, 40: begin July 1

**Full MODERATE path cadence**:

| Date | Action | Contact Count |
|---|---|---|
| May 21 | Domain 42 state AGs (deadline-driven) + Batch 2 Priority Group 1 | 5 + ~5 sends |
| May 22-23 | Batch 2 Priority Groups 2-3 (policy schools, governance programs, think tanks) | ~15 sends |
| May 24 | Batch 3 civil rights orgs (NAACP LDF, Lawyers' Committee, ACLU VRP) | ~6 sends |
| May 25 | Domain 37 Gist supplement update (not a full research sprint) | Internal |
| May 27 | Batch 3 labor (AFL-CIO, SEIU, AFSCME, CWA) + state AGs 6-11 | ~10 sends |
| June 1 | Domain 39 research begins (non-negotiable) | Research sprint |
| June 1-3 | First Tier 2 batch (policy window urgency framing) | ~8-10 contacts |
| June 8 | Domain 57 research begins | Research sprint |
| June 15 | Domain 59 research begins | Research sprint |
| June 15-17 | Second Tier 2 batch | ~8-10 contacts |
| August 10 | Domain 57 distribution to UNGA 81 contacts | Distribution |

**Non-responding Tier 1 follow-up protocol (MODERATE only)**:
On June 1-2, send one follow-up to non-responding high-weight contacts who have not sent OOO and have not declined. The follow-up must reference a specific policy event that occurred after May 18 — do not re-send the original email. Target 200-250 words maximum. Do not follow up with contacts who: (a) sent OOO with return date still pending, (b) acknowledged with Score 1-2, (c) declined.

---

### 4C: WEAK Path — Hold Batch 2, Diagnose First

**What WEAK means**: One of three possible causes: (1) delivery failure — emails went to spam (technical problem, not content failure), (2) contact quality issue — wrong people for this content at this time, (3) messaging misalignment — right people, wrong framing. Do not interpret WEAK as proposal failure. Determine the cause before revising anything.

**Before activating this path, confirm the delivery check from Section 3.3 is complete.**

**Immediate actions (11:00–13:30 UTC May 21)**:

**Step 1 — Log and flag**:
1. Log WEAK classification in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv row 61
2. Flag in CHECKIN.md under "Needs Your Input": "WEAK outcome confirmed at May 21 10:45 UTC. Post-mortem protocol required. No Batch 2 or Phase 2 sends until post-mortem complete and user approves revised messaging."
3. DO NOT send Batch 2. Burning 25+ contacts with unvalidated messaging wastes the entire Tier 2 pipeline.

**Step 2 — Domain 42 state AG sends (path-independent exception)**:
The 5 state AG Domain 42 contacts go regardless of WEAK classification. May 28 is a hard external deadline. This is the sole exception to the WEAK hold. Use Domain 42 urgency framing exclusively — do not attach the broader research framework to these sends.

**Step 3 — Domain 37 immediate action**:
Domain 37 election protection: update the existing Gist and distribute to election protection organizations on CISA and SAVE Act hooks. This does NOT require Phase 1 momentum — it is topically self-sufficient. Domain 37 base research is complete (May 6, ~6,800 words, 43 citations). This is a 2-3 hour update task, not a research sprint.

**Step 4 — Post-mortem protocol (May 22-27)**:

| Date | Task | Output |
|---|---|---|
| May 22-23 | Delivery audit: forward brief delivery test to each non-responding address; identify whether silence = delivery failure or disengagement | Confirmed delivery status per contact |
| May 23-24 | Messaging audit: review each template against: subject line specificity (reference a specific policy event or the contact's recent work?), opening paragraph relevance (arrives at "why this contact" within 2 sentences?), email length (>300 words = too long for policy org contacts), Gist link prominence (buried or in paragraph 2?) | Specific revision recommendations |
| May 24-25 | Contact quality audit: verify current institutional affiliations for all non-responding contacts; check for recent publications that anchor a revised subject line | Updated contact notes |
| May 25-27 | Produce revised messaging templates | Templates ready for user review |
| May 27 | User reviews and approves revised templates | Approval logged in CHECKIN.md |

**Step 5 — Phase 2 research (WEAK pivot)**:
- Domain 37 supplement: immediate (today, standalone)
- Domain 39 healthcare: begin no later than June 8 (hard HHS deadline anchor — cannot slip past June 8 even under WEAK)
- Domains 57, 59: begin July 15 (compressed 8-week sprint; still reaches August 10 deadline with minimal margin)
- All other Phase 2 domains: hold until Batch 2 revised messaging produces at least one quality reply

**WEAK path cadence**:

| Date | Action |
|---|---|
| May 21 | Log WEAK. Flag CHECKIN.md. HOLD Batch 2. |
| May 21 | Domain 42 state AG outreach — 5 sends (deadline exception). |
| May 22-24 | Domain 37 Gist update + election protection org distribution (standalone). |
| May 22-23 | Delivery audit. |
| May 23-25 | Messaging + contact quality audit. |
| May 25-27 | Revised templates produced. User reviews. |
| May 27 | User approves templates — Batch 2 revised send authorized. |
| May 26-28 | Batch 2 revised send (only after user approval). |
| June 8 | Domain 39 research begins (hard deadline anchor). |
| July 15 | Domain 57 + Domain 59 begin (parallel sprint). |

---

## SECTION 5: Batch 2-3 Timing Adjustments Per Classification

This section maps classification to exact Batch 2-3 dispatch dates, framing approach, and contingency handling.

### 5.1 STRONG — Accelerated Batch 2-3

**Batch 2 launch**: May 21 (today) — Priority Groups 1-2 execute within hours of classification confirmation.

**Why today, not May 22-23**: The institutional engagement signal has a half-life. Each day of delay reduces the social proof leverage. Under STRONG, the optimal window is while Tier 1 engagement signals are fresh (within 72-96 hours of receiving the qualifying reply).

**Batch 2 target count (STRONG)**: 20 sends by end of May 21. Stagger at 30-minute intervals.

**Batch 3 launch**: May 24 (labor unions) + May 27 (remaining civil rights orgs, state AGs). Full contact lists in MAY_21_31_BATCH_2_3_COORDINATION_FRAMEWORK.md Section 2.2.

**Batch 3 framing**: By May 24, Domain 57 research sprint will have begun (May 25 start). Batch 3 contacts in international law, labor, and civil society sectors can be offered both Phase 1 engagement validation AND early Phase 2 domain availability.

**Cadence summary (STRONG)**:
- May 21: ~20 sends (Batch 2 Priority Groups 1-2 + Domain 42 AGs)
- May 22-23: ~10 sends (Batch 2 Priority Group 3 — media)
- May 24: ~12 sends (Batch 3 labor)
- May 24-25: ~8 sends (Batch 3 civil rights)
- May 27: ~15 sends (Batch 3 remaining)
- Total by end of May: ~65 sends

### 5.2 MODERATE — Standard Batch 2-3

**Batch 2 launch**: May 21-22 (standard schedule). Priority Group 1 goes today; remainder May 22-23.

**Why not today for all**: Under MODERATE, social proof is thin (1-2 substantive replies). Batch 2 will use urgency framing, not social proof framing, which does not create the same time pressure as social proof. The 24-hour stagger allows Batch 2 preparation to be thorough.

**Batch 3 launch**: Check Batch 2 Day 5 signals before finalizing. If Batch 2 generates ≥1 quality reply by approximately June 1-3, proceed with Batch 3 June 8-10. If Batch 2 is also weak, hold Batch 3 contacts in reserve and redirect bandwidth to Phase 2 research production.

**Batch 3 decision gate (MODERATE)**: Approximately June 1-3 (Batch 2 Day 5 from a May 21-22 launch).
- ≥1 quality reply from Batch 2: proceed with Batch 3 June 8-10
- <1 quality reply: hold Batch 3; redirect to Phase 2 research; Batch 3 contacts receive research-led outreach when Domain 39 or Domain 57 is complete (June 30+)

**Cadence summary (MODERATE)**:
- May 21: 5 state AG sends (Domain 42) + ~5 Batch 2 Priority Group 1 = ~10 total
- May 22-23: ~15 sends (Batch 2 Priority Groups 2-3)
- May 24: ~6 sends (Batch 3 civil rights — does not wait for Batch 2 assessment for civil rights orgs with direct domain alignment)
- May 27: ~10 sends (Batch 3 labor + AGs 6-11)
- June 8-10: Batch 3 secondary (if Batch 2 ≥1 quality reply confirmed)
- Total by end of May: ~36 sends

### 5.3 WEAK — Extended Batch 2-3 to June 1+

**Batch 2 launch**: June 1 minimum, and only after: (1) post-mortem complete, (2) revised messaging templates produced, (3) user explicitly approves templates.

**Batch 2 revised framing (WEAK)**: Do not use original Batch 1 templates. Required revisions:
- Subject line: reference a specific policy event after May 18 OR the contact's recent published work by title
- Opening paragraph: "why this specific contact" within the first two sentences — no context-setting throat-clearing
- Length: 200-250 words maximum for policy org contacts; 300 words maximum for academic contacts
- Gist link: in paragraph 2, not buried at the end
- Offer framing: "This may be useful to your work on [specific domain/project]" not "I'd like to share this with you"

**Batch 3**: Do not plan Batch 3 until Batch 2 revised messaging produces ≥1 quality reply. Three waves of outreach with unvalidated messaging burns contacts and sender reputation.

**Revised Batch 2-3 cadence (WEAK)**:
- May 26-28: Batch 2 revised send (if post-mortem complete and user approves)
- June 8+: Assess Batch 2 results; if ≥1 quality reply, proceed with Batch 3
- If Batch 2 also weak: pause outreach entirely; redirect to Phase 2 research; return to outreach with Domain 39 or Domain 57 research as distribution hook (estimated return: July 2026)

---

## SECTION 6: May 21 Decision Gate Checklist

Execute all items between 10:30 UTC and 14:00 UTC. The 14:00 gate is the user decision confirmation. Every item below must be checked or explicitly flagged before the 14:00 gate.

### 10:30 UTC — Collect Metrics

- [ ] **Metric 1 — Bounces**: All hard bounce notifications checked. Count: ___. For each bounce, alternate address identified or verification initiated.
- [ ] **Metric 2 — OOO**: All auto-replies checked. Count: ___. Return dates logged. Follow-up dates scheduled (return date + 1 business day).
- [ ] **Metric 3 — Adjusted count**: 5 minus bounces minus OOOs = ___. This is the denominator for all rate calculations.
- [ ] **Metric 4 — Score 3+ replies**: All inbox emails read and scored. Count of contacts with Score 3 or higher: ___.
- [ ] **Metric 5 — Integration signals**: All replies re-read specifically for Score 4 or 5 language. Count: ___.
- [ ] **Metric 6 — Institutional reply rate**: (Score 3+ count) ÷ (adjusted count) × 100 = ___%
- [ ] **Metric 7 — Gist delta**: All Gist URLs checked against May 18 baseline. Total delta: ___. Gist bonus calculated: ___.
- [ ] **Signal aggregation table complete** (Section 2.1 — every row filled, no blank cells in Contact, Reply, Score, OOO, Bounce columns)
- [ ] **Sector analysis populated** (Section 2.4 — which sector(s) produced signals, if any)

### 10:45 UTC — Classify

- [ ] **Decision table run** (Section 3.2) — first matching priority row identified: Row ___
- [ ] **Classification confirmed**: STRONG / MODERATE / WEAK
- [ ] **If WEAK**: Delivery check completed and result logged (Section 3.3)
- [ ] **Law school silence explicitly noted** as expected and not penalized (Section 3.4)
- [ ] **Classification record filled in** (Section 3.5 text block — all fields populated)

### 11:00 UTC — Activate Path

- [ ] **Classification logged** in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv row 61 (Final column)
- [ ] **Path section opened**: Section 4A (STRONG) / Section 4B (MODERATE) / Section 4C (WEAK)
- [ ] **CHECKIN.md updated** with classification result, path recommendation, and "awaiting user 14:00 UTC confirmation"
- [ ] **Domain 42 state AG emails queued** (path-independent — 5 sends regardless of classification)
- [ ] **STRONG or MODERATE**: Batch 2 emails personalized and queued for send with correct framing
- [ ] **WEAK**: Batch 2 hold logged; post-mortem protocol initiated (Section 4C Step 4); Domain 42 sends confirmed as deadline exception

### 11:15–13:30 UTC — Execute

- [ ] **STRONG**: Batch 2 Priority Groups 1-2 sent (staggered 30 minutes apart)
- [ ] **MODERATE**: Batch 2 Priority Group 1 sent; Groups 2-3 queued for May 22-23
- [ ] **WEAK**: Domain 42 state AG 5 sends executed; Domain 37 Gist update initiated
- [ ] **All paths**: Domain 42 state AG sends dispatched
- [ ] **Gist view baseline**: New Gist view count snapshot taken after all sends, to establish fresh baseline for Batch 2 monitoring

### 14:00 UTC — User Decision Gate

- [ ] **Gist view progression analyzed**: Delta from pre-send baseline through current (any meaningful increase?)
- [ ] **All bounce rates confirmed**: Hard bounces documented; alternate addresses verified; resends completed or scheduled
- [ ] **Secondary contact follow-ups initiated for non-respondents**: For each non-responding contact with no OOO and no bounce, one secondary contact at the same organization identified and noted in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv column O
- [ ] **Tier 2 pipeline identified**: At least 10 Tier 2 organizations identified with verified contact emails, ready for Batch 2-3 sends under STRONG or MODERATE
- [ ] **Phase 2 path decision documented**: Classification (STRONG / MODERATE / WEAK) written in CHECKIN.md with specific Phase 2 domain sequence and start dates
- [ ] **User has reviewed classification and path recommendation**
- [ ] **User confirms**: "Proceed with [STRONG / MODERATE / WEAK] path" (or requests modification)
- [ ] **Phase 2 research start date confirmed** per Section 4A / 4B / 4C
- [ ] **Domain 42 coordination confirmed as active** regardless of classification
- [ ] **May 25 secondary gate scheduled**: "Re-run classification with full 7-day data including law school signals; final Phase 2 path confirmation; no Phase 2 research begins before this secondary gate unless STRONG path with user override"

**Authorization status after 14:00 gate**:
- [ ] APPROVED — path: ___
- [ ] PENDING USER DECISION (need to reschedule gate)
- [ ] MODIFIED — user requested change: ___

---

## SECTION 7: Contingency Scenarios

### 7.1 Partial Reply Scenarios (Batch 1 Partially Responds)

**Scenario A — 2 of 5 reply within 48 hours (by May 20 10:30 UTC)**:

This is an early positive signal — 2 replies within 48 hours represents strong performance against the policy org response norms. Assess the quality:
- If both are Score 3+: provisional STRONG (may upgrade to confirmed STRONG at 72h if third reply arrives)
- If 1 is Score 3+ and 1 is Score 1-2: provisional MODERATE
- If both are Score 1-2: MODERATE (lower end) — delivery confirmed, engagement not yet demonstrated

At the 72-hour gate (May 21 10:30 UTC), apply the full Section 3.2 table with all 72-hour data. A 2-of-3 result (adjusted for law schools) reaches 67% rate — STRONG if ≥1 is Score 4-5.

**Action if 2 replies arrive by May 20**: Do not launch Batch 2 early. Pre-stage Batch 2 emails (personalize and draft) so they are ready to send immediately at the 10:45 UTC classification confirmation. This saves 2-3 hours on May 21.

**Scenario B — 1 of 5 replies within 72 hours (by May 21 10:30 UTC), Score 4**:

Institutional reply rate = 1 of 3 (adjusted) = 33%. Integration signals: 1. This maps to Priority Row 4 in Section 3.2: Rate 30-59% AND integration signals ≥1 → MODERATE.

Classification: MODERATE. Batch 2 proceeds on schedule. The Score 4 signal (implementation or referral) is the key piece of social proof framing material — describe the engagement type (not the individual) in Batch 2 messaging.

**Scenario C — 1 of 5 replies within 72 hours, Score 3 (no integration signal)**:

Institutional reply rate = 1 of 3 (adjusted) = 33%. Integration signals: 0. This maps to Row 5: Rate 30-59% AND signals = 0 → MODERATE (lower end).

Classification: MODERATE. No social proof framing available — use policy urgency framing exclusively. Note in CHECKIN.md: "MODERATE lower end — monitoring closely for additional signals through May 25."

**Scenario D — Law school contact (Goodman or Chenoweth) replies before May 21 10:30 UTC**:

This is unexpected (early for their sector norm) but positive. Score normally and include in the institutional reply rate calculation. A Score 4 reply from Goodman (e.g., "I'm mentioning this in a Just Security piece" or "forwarding to the Just Security editorial team") would be the highest-value signal in the entire Batch 1 cohort given Just Security's reach to legal and policy audiences.

If Goodman or Chenoweth replies before May 21 10:30 UTC with Score 3+: adjust the analytical universe to all 5 contacts (or adjusted count if bounces/OOOs apply) and recalculate accordingly.

**Scenario E — One contact replies with Score 3+ and another responds with OOO (return date after May 21)**:

Adjusted count: 4 (removing the OOO contact). Rate: 1 of 4 = 25%. Below MODERATE threshold of 30%.

Action: Check integration signals. If the Score 3+ reply is also Score 4 (implementation/referral), Row 4 applies (Rate 30-59% OR integration ≥1 → MODERATE based on integration signal alone under Row 6 interpretation). If Score 3 only with no integration: borderline. Apply the Gist delta. If Gist delta > 10, Row 7 → MODERATE borderline. If Gist delta ≤ 5: WEAK.

Note the OOO return date in the tracker. When the contact returns, send a brief follow-up referencing the specific domain most relevant to their recent work.

### 7.2 Technical Failure Scenarios

**Scenario F — Hard bounce from one of the 5 Batch 1 contacts**:

1. Identify whether hard or soft bounce. Hard: permanent address failure. Soft: temporary.
2. For hard bounce: re-verify address against the institution's current staff page. Do not use LinkedIn — use the institutional website directly.
3. Resend to verified alternate address within 24 hours.
4. Remove the bounced contact from the adjusted count in the classification formula. Add to the re-verification log in DISTRIBUTION_EXECUTION_LOG.md.
5. If the resend goes to a different address and subsequently produces a reply: count that reply normally at the May 25 secondary gate, not at the May 21 gate (72-hour window will have passed for the resend).

**Scenario G — 2 or more hard bounces detected**:

This triggers Priority Row 10 (PAUSE) in Section 3.2. Do not classify. Fix delivery first.

Steps:
1. Re-verify all 5 addresses immediately (institutional websites, not LinkedIn)
2. Resend to verified addresses as soon as confirmed
3. Re-run Section 3.2 decision table after resends are confirmed delivered (24-48 hours)
4. Do not launch Batch 2 until delivery is confirmed across the corrected Batch 1 addresses
5. Flag in CHECKIN.md under "Needs Your Input — Technical": "2+ hard bounces detected. Delivery fix in progress. May 21 classification deferred pending re-verification."

**Scenario H — Gist inaccessible or URL broken**:

If the Gist URL is returning a 404 or the Bitly short link is not resolving:
1. Check GitHub Gist directly: is the Gist set to public or secret? Secret Gists are accessible only via the direct link — check that the correct URL was sent in the email.
2. If the Gist has been deleted or made private: create a replacement immediately using the same content. Update DISTRIBUTION_GIST_URLS.md with the new URL. Send a brief follow-up email to all 5 Batch 1 contacts with the corrected link: "Quick follow-up — the link in my earlier email has been updated. The correct link is: [new URL]."
3. Do not interpret zero Gist clicks as disengagement if a Gist access issue is confirmed. Exclude Gist delta from the classification formula and note "Gist delta excluded — technical access issue."

**Scenario I — Email account flagged or sending limit hit**:

If Gmail or the sending account has triggered a sending rate limit (uncommon at 5 emails but possible if the account flagged suspicious activity):
1. Wait 24 hours before attempting resends from the same account.
2. If the account is suspended: contact Gmail support. Do NOT create a new account and resend from an unrecognized address to institutional contacts — this will trigger spam filters.
3. Alternative: send from a secondary account (if available) that has pre-established history with at least one of the 5 contacts, or send via a personal email address that the contact might recognize.
4. Flag in CHECKIN.md: "Sending account issue. Batch 1 may not have been fully delivered. Technical resolution in progress. Classification deferred."

### 7.3 Response Pattern Anomalies

**Anomaly 1 — Response from unexpected direction (non-institutional reply)**:

If a colleague, assistant, or junior staff member from one of the Batch 1 organizations responds on behalf of the primary contact: score based on the content, not the sender. An assistant saying "Dr. Chenoweth asked me to request the Domain 38 full text" is a Score 4 (implementation signal) — the organizational intent is what matters.

**Anomaly 2 — Two contacts from the same organization respond independently**:

If, for example, two Brennan Center staff respond to the same email (Weiser forwarded it internally and a colleague replied independently): this is a cascade signal. Mark both responses. The second contact (not the primary Batch 1 contact) is a strong Tier 2 candidate. Record both in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv. Count only the primary contact's response in the institutional reply rate formula.

**Anomaly 3 — Hostile or critical response**:

A substantive methodological critique is Score 3 (it demonstrates careful reading). Only score as 0 (Decline) if the contact explicitly opts out or says the research is not relevant. A hostile engagement is still engagement — the person read the material and formed a strong view. Log the specific critique verbatim in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv column O for Phase 2 research calibration.

**Anomaly 4 — Media pickup before May 21**:

If a journalist or publication references the research in an article before the May 21 gate: this is an unsolicited integration signal. Score as 5 (Integration) for the Domain 42 or relevant contact pathway. Flag immediately in CHECKIN.md. This triggers STRONG classification regardless of email reply rate.

**Anomaly 5 — Zero signals of any kind (zero replies, zero bounces, zero Gist delta)**:

This is the scenario most likely explained by spam filter interception, not disengagement. Before classifying as WEAK, complete Section 3.3 delivery check. If delivery test confirms spam filter issue: do not classify. Fix sender reputation. The content and contacts have not been tested yet.

---

## SECTION 8: May 25 Secondary Gate

The May 21 classification is **preliminary**. The May 25 secondary gate is the **final confirmation** after law school contacts have had their full 7-day response window.

**Execute at May 25 20:00 UTC** (or morning if working US Eastern time).

**At May 25**:
1. Re-populate Section 2.1 with any new signals received May 21-25
2. Re-run Section 3.2 decision table with full 7-day data (all 5 contacts now in their primary windows)
3. If classification upgrades (e.g., MODERATE at May 21 → STRONG at May 25 because Goodman replied Day 5 with Score 4): upgrade Batch 2-3 framing and accelerate Phase 2 research timeline
4. If classification holds: confirm Phase 2 path and proceed
5. Run the 12-item May 25 checklist in WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md Section 5 for full validation
6. Populate WAVE_1_CONTINGENCY_DECISION_TREE.md Part 2 (Composite Wave 1 Score table) with constituency-weighted data for final validation
7. Get explicit user approval for Phase 2 research start before any research sprint begins

**May 25 is the Phase 2 research authorization gate.** The May 21 classification authorizes Batch 2-3 preparation and domain-independent Domain 42 sends. Phase 2 research begins with explicit user approval at May 25.

**Exception**: Under STRONG classification, user may authorize Phase 2 research start at the May 21 14:00 gate without waiting for May 25. This requires explicit "proceed with STRONG Phase 2 June 1 start" language from the user. Without that language, May 25 is the Phase 2 authorization gate even under STRONG.

---

## SECTION 9: Measurement Framework Cross-References

### How this document feeds WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv

| This document | CSV Location |
|---|---|
| Section 2.1 contact table — Reply, Type, Score | Rows 2-6, Columns K-N |
| Section 2.1 contact table — Verbatim signal quotes | Rows 2-6, Column O (Notes) |
| Section 2.1 contact table — Gist Clicked, OOO, Bounce | Rows 2-6, Columns I-J, and bounce column |
| Section 3.5 classification record — Final classification | Row 61, Column E (Final) |
| Sector analysis (Section 2.4) | Rows 53-58, Columns B-J (Sector Summary) |

### Files updated at the May 21 14:00 gate

| File | What to Update |
|---|---|
| WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv | Rows 2-6 per-contact, row 61 classification, rows 53-58 sector summary |
| WAVE_1_MONITORING_DASHBOARD.md | Section 2 daily status block for May 20-21; Section 3 sector tables |
| PHASE_2_OUTCOME_FRAMEWORK.md | Section 7 Monitoring Log; Classification field |
| DISTRIBUTION_EXECUTION_LOG.md | Daily entry for May 21 synthesis and bounce/OOO log |
| CHECKIN.md | "Needs Your Input" — classification result + path recommendation + Phase 2 start date |

### Files updated at May 25 secondary gate

| File | What to Update |
|---|---|
| WAVE_1_CONTINGENCY_DECISION_TREE.md | Part 2 CRS table — all five constituency rows |
| PHASE_2_LAUNCH_DECISION_TRIGGERS.md | Scenario selection — mark one ACTIVE after user approval |
| WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md | Section 5 — 12-item May 25 gate checklist completed |

---

## Appendix A: Contact Reference

### Batch 1 (Wave 1 — sent May 18, 08:00–10:00 UTC)

| Contact | Email | Sector | 72h Gate Expectation |
|---|---|---|---|
| Ryan Goodman | ryan@justsecurity.org | Law School / NYU | Silence expected; window extends to May 28 |
| Wendy Weiser | wweiser@brennancenter.org | Policy Org / Brennan Center | Reply possible; window closed at 72h |
| Erica Chenoweth | erica_chenoweth@hks.harvard.edu | Law School / Harvard Kennedy | Silence expected; window extends to May 28 |
| Ian Bassin | ian@protectdemocracy.org | Policy Org / Protect Democracy | Reply possible; window closed at 72h |
| Marc Elias | melias@elias.law | Litigation / Democracy Docket | Reply possible; fastest expected responder |

### Domain 42 Sub-Batch (path-independent — execute regardless of classification)

| Contact | Email | Deadline |
|---|---|---|
| Drug Policy Alliance | press@drugpolicy.org | May 21 send; follow-up May 24-26 |
| NORML | norml@norml.org | May 21 send; follow-up May 24-26 |
| ACLU Criminal Law Reform | nationaloffice@aclu.org | May 21 send; follow-up May 24-26 |
| The Sentencing Project | staff@sentencingproject.org | May 21 send; follow-up May 24-26 |
| LEAP | info@leap.cc | May 21 send; follow-up May 24-26 |

DEA-1362 filing deadline: May 28 (nprm@dea.gov). Organizations must have materials by May 22 to prepare and file in time.

### Domain 42 State AGs (path-independent — send today regardless of classification)

| Contact | Email / Portal | Deadline |
|---|---|---|
| Kris Mayes / Arizona AG | azag.gov | May 21 |
| Rob Bonta / California AG | oag.ca.gov | May 21 |
| Phil Weiser / Colorado AG | coag.gov | May 21 |
| Dana Nessel / Michigan AG | michigan.gov/ag | May 21 |
| Nick Brown / Washington AG | atg.wa.gov | May 21 |

---

## Appendix B: Source Documents

This framework synthesizes data from the following files. Consult them for deeper detail; this document is the May 21 operational instrument.

| Document | What It Adds Beyond This Document |
|---|---|
| WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md | Deeper signal logic, conservative vs. calibrated threshold comparison, full worked examples, CSV column mapping, 12-item May 25 checklist |
| MAY_21_31_BATCH_2_3_COORDINATION_FRAMEWORK.md | Full Batch 2-3 contact lists (70+ contacts), path-specific email templates, Batch 3 labor/civil rights sequencing detail |
| DOMAIN_42_AMPLIFICATION_STRATEGY.md | Full DEA hearing media calendar (May 12-28), sector-specific messaging for Domain 42, organization preparation checklist |
| WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv | Raw signal log — populate as replies arrive; authoritative verbatim reply notes and daily summaries |
| WAVE_1_CONTINGENCY_DECISION_TREE.md | Constituency-weighted Composite Wave 1 Score (CRS) calculation — use at May 25 for validated final classification |
| WAVE_1_MONITORING_DASHBOARD.md | Real-time daily tracking, sector breakdowns, early warning signals, non-response thresholds |
| PHASE_2_LAUNCH_DECISION_TRIGGERS.md | Three-scenario Phase 2 activation framework, standing external deadlines, per-constituency Phase 2 domain sequences |
| PHASE_2_OUTCOME_FRAMEWORK.md | Phase 2 monitoring log; classification field; domain research production targets |
| DISTRIBUTION_OUTREACH_CONTACTS.md | Full Tier 1 and Tier 2 contact list with verification status |
| DISTRIBUTION_EXECUTION_LOG.md | Historical record of all sends, bounces, and daily monitoring entries |

---

*Framework created: May 18, 2026. Revised: May 18, 2026 (Item 61 expansion — added Section 7 contingency scenarios, expanded Section 5 Batch 2-3 timing, expanded Section 6 decision gate checklist, added Appendix A contact reference). Calibrated against M+R Benchmarks 2026 (1.4% nonprofit advocacy baseline), Hunter.io 2026 targeted outreach data (6.2% targeted campaign reply rate), and sector-specific response cycle norms documented in WAVE_1_MONITORING_DASHBOARD.md. All 5 Batch 1 emails confirmed sent May 18, 08:00–10:00 UTC.*
