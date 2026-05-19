---
title: "Post-Wave-1 Signal Analysis Framework"
created: 2026-05-19
version: 1.0
status: OPERATIVE — execute May 20–21
scope: "Operationalized scoring schema, sector baselines, STRONG/MODERATE/WEAK thresholds, contingency protocol, and May 21 decision procedure for Wave 1 monitoring window (May 18–21 10:30 UTC)"
audience: thorn — mechanical execution May 20–21; orchestrator synthesis input May 21 19:00–20:00 UTC
wave_1_send: "May 18, 08:00–10:00 UTC (5 emails)"
monitoring_close: "May 21 10:30 UTC (72-hour window)"
synthesis_deadline: "May 21 19:00 UTC (classification input) → 20:00 UTC (CHECKIN.md post)"
decision_output: "STRONG / MODERATE / WEAK → hand to PHASE_2_DOMAIN_RESEARCH_SEQUENCING.md Part 4"
companion_files:
  - post-wave-1-monitoring/wave-1-signal-log-may18-21.md
  - WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md
  - PHASE_2_DOMAIN_RESEARCH_SEQUENCING.md
  - post-wave-1-monitoring/may21-synthesis-execution-checklist.md
---

# Post-Wave-1 Signal Analysis Framework

**Purpose**: This document operationalizes what "signal" means, how to score it, what counts as STRONG versus MODERATE versus WEAK, and exactly how to reach and record a determination by May 21 20:00 UTC. It is designed for mechanical execution by a single operator in under 45 minutes. No judgment calls are needed — every edge case has a rule.

**Wave 1 actual send**: 5 emails dispatched May 18, 08:00–10:00 UTC to Ryan Goodman (Just Security / NYU Law), Wendy Weiser (Brennan Center), Erica Chenoweth (Harvard Kennedy School), Ian Bassin (Protect Democracy), Marc Elias (Democracy Docket / Elias Law Group).

---

## PART 1: RESPONSE CLASSIFICATION SCHEMA

### 1.1 Signal Types and Weights

Every response event receives a **Signal Weight** used in aggregate scoring. Record each signal separately — one contact can produce multiple signals across different channels (email reply + Gist click, for example).

| Signal Type | Weight | What Qualifies | What Does Not Qualify |
|-------------|--------|---------------|----------------------|
| Direct reply to coordinator email | **3.0** | Any email reply to the sender's address that goes beyond automated or generic acknowledgment | Auto-responder OOO (treated as administrative, not signal); list-unsubscribe |
| Engagement with shared brief / document (Gist click, timed dwell, download) | **2.0** | Gist view count delta attributable to a specific contact (verified by timing, follow-up reference); or document download from shared link | Unverifiable Gist delta (untraceable to a specific contact — counted as proxy only, see Section 2.2) |
| Follow-on meeting request | **3.5** | Explicit request to speak, schedule a call, or arrange a briefing — initiated by the contact, not the sender | Meeting suggested in passing without date / format ("maybe sometime") — score as direct reply (3.0) only |
| Silent re-share within network | **0.5** | Evidence of forwarding (a third party reaches out referencing the framework without having received an email) OR social mention without direct engagement | Unverified assumption of forwarding without any traceable third-party contact |
| Public citation / integration | **5.0 OVERRIDE** | Framework cited in a filing, brief, published article, testimony, or public post by a Batch 1 contact | Draft or internal citation not yet published — score as direct reply (3.0) with a note |
| Referral to named colleague or organization | **4.0** | Contact explicitly names a person or organization they are forwarding to — within the email reply | "I'll share this around" without naming anyone — score as direct reply (3.0) only |
| Substantive methodological question | **3.0** | Domain-specific question citing a section, dataset, or argument by name — same weight as direct reply because it is one | Generic "how did you compile this?" without domain specificity — score 2.0 (engagement without signal) |
| Acknowledgment only | **1.0** | "Thanks, will read," "received," or generic positive without substance | Counts as confirmed delivery; does not contribute to aggregate score |
| Decline or no-interest response | **0.0** | "Not relevant to our work," "unsubscribe," explicit no | Counts as confirmed delivery; remove from expectation denominator |

### 1.2 Aggregate Scoring: Response Strength Score (RSS)

**Definition**: The Response Strength Score (RSS) is the sum of all signal weights across all contacts and all channels within the monitoring window.

**Formula**:

```
RSS = Σ (Signal Weight × Confirmation Factor) for all signals received

Confirmation Factor:
  - Verified signal (email thread, named contact): 1.0
  - Proxy signal (unverifiable Gist delta): 0.5 (applied to engagement weight of 2.0 → contributes 1.0 per 15-view block, capped at 2.0 total from proxy sources)
  - Administrative (OOO, bounce): 0.0 — removes contact from denominator; does not add or subtract from RSS
```

**Example calculation**:
- Elias replies with case-specific Callais content (direct reply 3.0) + requests a call (meeting request 3.5) = 6.5
- Bassin replies with a methodological question (direct reply 3.0)
- Gist delta of 18 views unverifiable to specific contact (proxy: 18/15 = 1 block × 1.0 cap = 1.0)
- Weiser: no reply, no Gist signal
- Goodman: OOO (remove from denominator)
- Chenoweth: silence (within law school norm; no penalty)

**RSS = 6.5 + 3.0 + 1.0 = 10.5**

Adjusted sent count = 4 (Goodman removed for OOO). Effective RSS denominator = 4 contacts.

### 1.3 Quality Reply Count (QRC) — Companion Metric

In addition to RSS, track the raw count of contacts who produced at least one signal at weight >= 3.0 (substantive engagement). This is the "how many people actually engaged" number, distinct from the weighted score.

**QRC = number of contacts with at least one signal at weight >= 3.0**

A contact who sends an acknowledgment only (weight 1.0) does NOT count toward QRC. A contact who sends a meeting request (weight 3.5) counts as QRC = 1 for that contact regardless of how many signals they produce.

---

## PART 2: SECTOR-SPECIFIC BASELINE EXPECTATIONS

### 2.1 Why Sector Baselines Matter

Wave 1 Batch 1 is 5 contacts, not a statistically representative sample. Whether 1 reply is strong or weak depends entirely on what sector that contact comes from and how long they have had to respond. A law school contact replying at 48 hours is anomaly-level speed. A civil rights organization replying at 5 days is within baseline. Applying one threshold to both would either overclaim or underclaim.

The baselines below are drawn from sector-specific norms documented in `WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md` Section 1.1 and `preliminary-signal-analysis-may18.md` Section 2, calibrated against M+R Benchmarks 2026 (1.4% nonprofit mass email baseline), Hunter.io 2026 targeted cold email data (6.2% for 21–50 recipient campaigns), and the 340% personalization multiplier for contact-specific research framing.

### 2.2 Sector Baseline Table

| Sector | Typical Reply Rate | Expected Window | Expected Substantive Reply Rate (Score 3+) | What "Above Baseline" Means |
|--------|-------------------|-----------------|--------------------------------------------|----------------------------|
| **Law schools / academic law** | 20–30% within 10 days | 5–10 days | 1 of 2 within 10 days is strong performance | A reply within 72h is anomaly-level; treat as STRONG signal regardless of content |
| **Think tanks / policy orgs** | 35–50% within 5 days | 2–5 days | 1 of 2 within 5 days is strong; 0 of 2 within 7 days is weak | A reply within 48h with domain-specific content; OR 2 of 2 within 5 days at any score |
| **Legal aid / active litigators** | 25–40% within 48h (for domain-relevant research) | 1–3 days | 1 of 1 within 3 days is baseline; Score 4+ within 48h is above baseline | A case-specific reply within 48h (names a docket, brief, or litigation theory) |
| **Labor / civil rights organizations** | 25–35% within 72h | 2–4 days | 1–2 of 5 within 5 days | Organizing focus signals (requests for materials, coalition engagement) rather than policy-only responses |
| **Academic (non-law, Kennedy School / policy)** | 30–45% within 7 days | 3–7 days | 1 of 2 within 7 days | Research or citation interest signals — asking for underlying data or methodology |
| **Government / agency** | 10–20% within 5 business days | 3–7 business days | 0–1 of 5 within 7 days is baseline; 1+ within 3 days is above baseline | High-weight when it occurs — even a low-quality reply from a government contact is scored at minimum 2.0 regardless of content specificity |

### 2.3 Batch 1 Contacts Mapped to Sector Baselines

| Contact | Sector | Response Window | First Meaningful Window | Above-Baseline Trigger |
|---------|--------|----------------|------------------------|------------------------|
| Ryan Goodman | Law school / academic | 5–10 days | May 23–28 | Reply with domain-specific content by May 23 (5 days) |
| Wendy Weiser | Think tank / policy org | 2–5 days | May 20–23 | Reply at Score 3+ by May 23; OR any reply within 48h (May 20) at any score |
| Erica Chenoweth | Academic (Kennedy School) | 3–7 days | May 21–25 | Reply with research or citation interest by May 22 |
| Ian Bassin | Think tank / policy org | 2–5 days | May 20–23 | Reply at Score 3+ by May 23; named referral to state AG network = Score 4 |
| Marc Elias | Legal aid / active litigator | 1–3 days | May 19–21 | Case-specific content (docket name, brief reference) by May 20 10:00 UTC = STRONG regardless of other signals |

### 2.4 What "Early Signal Above Baseline" Looks Like Per Sector

**Law schools (Goodman, Chenoweth)**: A reply within the first 48 hours of send is statistically unusual. Any substantive reply by May 20 should be logged as "above baseline — law school early response" and treated as equivalent to a Score 4 (implementation signal), regardless of its literal content quality, because the speed itself signals high salience.

**Think tanks (Weiser, Bassin)**: A reply on May 19 (same business day as send for US Eastern time zones) would be above baseline. A reply that names a specific affiliated colleague to forward to is above baseline regardless of when it arrives.

**Legal aid (Elias)**: The 48-hour anomaly window is May 20 ~08:00–10:00 UTC. Any reply by that window with case-specific content (a docket number, a brief title, a litigation theory) is above baseline. A reply without case specificity within that window is baseline — still worth logging at Score 3 (direct reply with engagement) but not anomaly-level.

**The silence rule**: Silence from law school contacts (Goodman, Chenoweth) through the full May 21 72-hour window is NOT a negative signal and must not be scored or classified as such. Their window remains open through May 28. The May 21 classification for those two contacts is: TOO EARLY — do not classify.

---

## PART 3: STRONG / MODERATE / WEAK DECISION THRESHOLDS

### 3.1 Threshold Table (Primary)

The following thresholds apply to the final aggregate at May 21 10:30 UTC (72-hour window close) and the May 21 synthesis at 19:00–20:00 UTC. Apply top to bottom. Stop at first match.

| Priority | Condition | Classification | Rationale |
|----------|-----------|----------------|-----------|
| **1 (override)** | Any contact produces a public citation / integration signal (weight 5.0) — framework cited in a filing, brief, testimony, or published article | **STRONG** — immediate, stop classification | One confirmed adoption signal changes the strategic situation faster than any aggregate metric. Route directly to PHASE_2_DOMAIN_RESEARCH_SEQUENCING.md STRONG path. |
| **2** | RSS >= 8.0 AND QRC >= 2 | **STRONG** | Two substantive engagements at aggregate weight 8+ constitutes strong performance relative to sector baselines on a 5-contact targeted send. |
| **3** | RSS >= 5.0 AND QRC >= 1 AND at least one signal at weight >= 3.5 (meeting request or referral) | **STRONG** | Single high-weight engagement with above-baseline signal type is sufficient at this scale. |
| **4** | RSS >= 4.0 AND QRC >= 2 | **MODERATE** (borderline strong — treat as MODERATE, flag as "approaching STRONG") | Two substantive contacts at aggregate 4.0+ without a high-weight signal. Sufficient for standard Phase 2 timeline. |
| **5** | RSS >= 2.0 AND QRC >= 1 | **MODERATE** | Single substantive engagement is the minimum viable signal at this contact volume. Not enough for accelerated Phase 2 but sufficient for standard timeline. |
| **6** | RSS >= 1.0 AND proxy Gist delta > 15 views AND QRC = 0 | **MODERATE** (borderline — delivery is working, conversion pending) | Gist engagement without email reply suggests the material is being read. Do not classify as Weak when delivery is confirmed via Gist activity. |
| **7** | RSS < 1.0 AND QRC = 0 AND Gist delta <= 5 | **WEAK** — but run delivery check before confirming | Before any content diagnosis, send a test email from the same account to yourself. If it lands in spam, classify as delivery failure, not content failure. |
| **8** | RSS = 0 AND Gist delta = 0 AND no bounces AND no OOOs | **TOO EARLY** — law school window not closed; do not classify as Weak | This scenario most likely reflects law school response timing. Hold classification to May 25. |
| **9** | >= 2 hard bounces from Batch 1 contacts | **PAUSE** — delivery failure diagnosis before any classification | Fix delivery before scoring content. |

### 3.2 Precise Threshold Values

| Classification | RSS Range | QRC Minimum | High-Weight Signal Required? | Notes |
|---------------|-----------|-------------|------------------------------|-------|
| **STRONG** | >= 8.0, OR >= 5.0 + meeting/referral signal, OR any weight-5.0 event | >= 2 (or 1 with weight-5.0 override) | Weight >= 3.5 required for the RSS 5.0 route; not required for the RSS 8.0 route | A single Elias reply with case content (weight 3.0) + Elias meeting request (weight 3.5) = 6.5 from one contact = STRONG (RSS 6.5 >= 5.0, meeting signal present) |
| **MODERATE** | 2.0–7.9 | >= 1 | No | A single Weiser substantive reply (weight 3.0) = RSS 3.0, QRC 1 = MODERATE |
| **WEAK** | < 2.0 | 0 | N/A | Must confirm delivery before classifying as Weak |
| **TOO EARLY** | 0 | 0 | N/A — silence only | No bounces, no OOOs, no Gist activity. Law school window still open. |

### 3.3 Tiebreaker Rules

When the RSS score falls exactly on a boundary (e.g., RSS = 4.0, QRC = 1, no high-weight signal — sits between rows 4 and 5 in the threshold table), apply the following tiebreakers in order:

**Tiebreaker 1 — Response quality over count**: If QRC = 1 and that single reply includes a named colleague referral or explicit application ask (even if technically classified at weight 3.0 rather than 4.0 due to phrasing), upgrade to the higher threshold.

**Tiebreaker 2 — Sector distribution**: If the single replying contact is from the legal aid or policy org sector (Elias, Weiser, Bassin), weight the classification toward the higher threshold. Replies from the highest-velocity sectors indicate faster adoption potential than the same RSS from an academic contact at this stage.

**Tiebreaker 3 — Timing clustering**: If 2 or more signals arrive within the same 24-hour window (regardless of whether they are from the same contact), treat as elevated signal — the timing cluster suggests the material is circulating. Upgrade toward the higher threshold.

**Tiebreaker 4 — Default to conservative**: If tiebreakers 1–3 are inconclusive, classify at the lower threshold. It is operationally better to underclassify (run MODERATE when borderline STRONG) than to overcommit Phase 2 resources on ambiguous data. The May 25 final gate provides a correction opportunity.

### 3.4 Worked Scenarios (Illustrative)

**Scenario A — Clear STRONG**
- Elias replies May 20 (within 48h): "The Callais cascade analysis is directly relevant to Watson v. RNC. Can you send the Domain 37 standalone brief? I'm forwarding to our litigation team." 
- Signal decomposition: direct reply (3.0) + referral signal (4.0) = two separate weight events from one contact.
- RSS = 3.0 + 4.0 = 7.0. QRC = 1. No high-weight signal at 3.5+ from a second contact yet.
- Threshold check: Row 3 (RSS >= 5.0 AND QRC >= 1 AND at least one signal at weight >= 3.5 — the referral = 4.0). **STRONG.**

**Scenario B — Borderline, tiebreaker resolves MODERATE**
- Bassin replies May 21 with a methodological question about Domain 29 data sourcing. Weight 3.0. RSS = 3.0. QRC = 1.
- Gist delta = 8 views, unverifiable to specific contact. Proxy contribution: 0.5 × 2.0 = 1.0 (8 views < 15-view block threshold for proxy counting; treat as 0 proxy bonus).
- RSS = 3.0. Threshold row 5: RSS >= 2.0 AND QRC >= 1 = **MODERATE.**

**Scenario C — 48h contingency trigger**
- By May 20 12:00 UTC: 0 replies, Gist delta = 3 views. RSS = 0. QRC = 0.
- Threshold check: Row 7 (RSS < 1.0, Gist delta <= 5) — but window has not closed (still 10.5 hours remaining).
- Action: Do not classify yet. Flag as "contingency monitoring active." Run delivery self-test. See Part 4.

**Scenario D — TOO EARLY classification**
- May 21 20:00 UTC: 0 replies, 0 bounces, 0 OOOs, Gist delta = 0.
- RSS = 0. Threshold row 8: TOO EARLY.
- Note in CHECKIN.md: "Law school window remains open through May 28. Delivery unconfirmed via Gist. Run delivery self-test before May 22 morning."

---

## PART 4: CONTINGENCY MONITORING PROTOCOL

### 4.1 The 48-Hour Check — May 20 12:00 UTC

**What to assess**: Has any contact produced a signal at weight >= 2.0 by this point?

**Trigger condition for contingency**: RSS = 0 AND QRC = 0 AND Gist delta <= 3 at May 20 12:00 UTC.

**If contingency triggered, choose one of three options**:

| Option | Description | When to Choose |
|--------|-------------|---------------|
| **A — Extend Wave 1 to Reserve list** | Send 2–3 additional personalized emails to the Reserve contacts identified in `DISTRIBUTION_PATH_EXECUTION_GUIDE.md` (Category B civil rights organizations). Use the MODERATE framing template from WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md Section 3B. | If delivery self-test confirms emails are landing in inbox (delivery is working, content may need augmentation). |
| **B — Accelerate Batch 2 prep** | Begin Batch 2 template customization immediately (standard lead time is May 25–28 for STRONG, June 1–3 for MODERATE). Batch 2 can be ready to send as early as May 22 if contingency confirms messaging needs recalibration. | If delivery is confirmed but RSS remains 0 — faster Batch 2 deploy gives 3 additional days before synthesis to capture a broader signal. |
| **C — Pause synthesis decision pending 72h close** | Take no new action. Continue monitoring through May 21 10:30 UTC (full 72h window). Do not activate contingency. | If Gist delta is > 3 but < 15, indicating possible reading without reply — delivery is working, conversion may be pending. |

**Default option if unclear**: Option C. The 72-hour window has not closed at 48 hours. Reserve contingency activation for confirmed 0-signal situations only.

### 4.2 Delivery Self-Test (Required if RSS = 0 at Any Check Point)

Before any content diagnosis or contingency activation, run this test:
1. Send a test email to yourself from the same sending account used for Batch 1.
2. Does it land in inbox or spam?
   - **Inbox**: Delivery is confirmed working. Proceed with content assessment.
   - **Spam**: Delivery failure. Do NOT classify as WEAK content. Do NOT revise messaging. Fix sender reputation or sending domain. Report to CHECKIN.md as "DELIVERY PROBLEM — do not classify as content failure."

### 4.3 The 72-Hour Close — May 21 10:30 UTC

The 72-hour monitoring window closes at May 21 10:30 UTC. At that point:
- Record final signal log entry in `post-wave-1-monitoring/wave-1-signal-log-may18-21.md`
- Note any signals received between 10:00 and 10:30 UTC (final 30-minute window)
- No new signals after 10:30 UTC count toward the 72-hour RSS calculation — they count in the extended window for the May 25 final gate

**Between 10:30 and 19:00 UTC on May 21**: No new outreach or response action required. Prepare the data assembly for the 19:00 UTC synthesis.

### 4.4 May 21 Synthesis Execution — 19:00–20:00 UTC

This is the primary decision event. Full step-by-step procedure is in `post-wave-1-monitoring/may21-synthesis-execution-checklist.md`. The present framework provides the scoring schema that feeds that checklist. Summary:

1. Collect all signal log data from `post-wave-1-monitoring/wave-1-signal-log-may18-21.md`
2. Calculate RSS using Part 1 formula
3. Calculate QRC (count of contacts with weight >= 3.0 signal)
4. Run threshold table (Part 3.1) — stop at first match
5. Apply tiebreakers if needed (Part 3.3)
6. Record classification in CHECKIN.md using the template in `may21-synthesis-execution-checklist.md` Step 10
7. Hand classification to `PHASE_2_DOMAIN_RESEARCH_SEQUENCING.md` Part 4

---

## PART 5: MAY 21 DECISION PROTOCOL

### 5.1 Data Collection Responsibility

| Task | Who | When |
|------|-----|------|
| Check email inbox for replies | **User** | May 20 morning (US ET), May 20 evening, May 21 morning before 10:30 UTC |
| Check Gist view counts in incognito browser | **User** | Same cadence as inbox checks |
| Log signals in `wave-1-signal-log-may18-21.md` | **User** logs raw data; orchestrator compiles count and runs formula | Real-time as signals arrive; final compile at May 21 19:00 UTC |
| Check for third-party contacts (silent re-share proxy) | **User** | May 20–21 — any new email from unknown contacts referencing the framework |
| Run delivery self-test | **User** | If RSS = 0 at any check; mandatory before any WEAK classification |
| Calculate RSS, QRC, run threshold table | **Orchestrator** | May 21 19:00 UTC synthesis |
| Write CHECKIN.md classification entry | **Orchestrator** | May 21 by 20:00 UTC |
| Hand to PHASE_2_DOMAIN_RESEARCH_SEQUENCING.md | **Orchestrator** | May 21 20:00 UTC; Phase 2 execution May 22+ pending user approval |

### 5.2 Data Collection Timeline

| Check Point | UTC Time | What to Check | Log Destination |
|------------|----------|--------------|----------------|
| May 20 morning | ~12:00 UTC | Inbox (Elias 48h anomaly window opens); Gist delta | wave-1-signal-log-may18-21.md Day 2 snapshot |
| May 20 evening | ~22:00 UTC | Inbox (Weiser/Bassin second-chance window); Gist delta | wave-1-signal-log-may18-21.md Day 2 update |
| May 21 morning | ~09:00 UTC | Inbox final pre-close check; Gist delta | wave-1-signal-log-may18-21.md Day 3 snapshot |
| May 21 window close | 10:30 UTC | Final signal log entry; no new signals count after this | wave-1-signal-log-may18-21.md — close entry |
| May 21 synthesis | 19:00–20:00 UTC | Compile RSS, QRC, run threshold table, write CHECKIN.md | CHECKIN.md + wave-1-signal-log-may18-21.md |

### 5.3 Classification-to-Phase-2 Handoff

Once the classification is written to CHECKIN.md:

| Classification | Immediate Next Action | Phase 2 Start | User Approval Required Before? |
|---------------|----------------------|---------------|-------------------------------|
| **STRONG** | Flag CHECKIN.md "STRONG — Phase 2 June 1 parallel launch pending user approval." Begin Domain 57 + 59 pre-production checklists. | June 1 | Yes — user must confirm before D57/D59 pre-production begins |
| **MODERATE** | Standard timeline. Continue monitoring to May 25 final gate. | Domain 57 June 10; Domain 59 July 1 | Yes — user approves at May 25 gate |
| **WEAK** | Flag CHECKIN.md "WEAK confirmed — post-mortem required. No Batch 2 or Phase 2 research until user reviews revised messaging." | Domain 39 June 8 non-negotiable; D57/D59 deferred | Yes — user must approve revised messaging before any send |
| **TOO EARLY** | Hold. Monitoring continues May 22–24. Default to WEAK path if no signal by May 25 midnight. | Per WEAK path default | Yes |

### 5.4 Escalation Rule for Borderline Outcomes

If the outcome falls on a threshold boundary and tiebreakers (Part 3.3) do not resolve it:

**Default rule: classify conservative, flag the ambiguity explicitly.**

Example: RSS = 4.2, QRC = 1, no high-weight signal. Primary threshold table row 4 (RSS >= 4.0 AND QRC >= 2) fails at QRC = 1. Row 5 (RSS >= 2.0 AND QRC >= 1) applies. Classification: **MODERATE**. Flag in CHECKIN.md: "Borderline — approaching STRONG threshold. Monitor May 22–25 for additional signals before Phase 2 domain commit."

The conservative rule (assume MODERATE over STRONG) is preferred over the aggressive rule because:
- Phase 2 research can be accelerated if May 25 signals improve; it cannot be un-spent if resources are committed prematurely.
- MODERATE path (Domain 57 June 10) is only 10 days behind STRONG (June 1) — a defensible delay in exchange for data confidence.
- The May 25 gate exists precisely to catch borderline cases that resolve with additional time.

---

## PART 6: WORKED EXAMPLES WITH REAL BASELINES

### Scenario A — Solid MODERATE, 48h cluster

**Situation**: By May 20 18:00 UTC, the following signals have arrived:
- Weiser replies May 19 (Day 1): "This framework is directly relevant to our SAVE Act amicus work. Can you format Domain 37 as a standalone one-pager for state AG contacts?" — direct reply (3.0) + meeting/use request (3.5) = 6.5
- Bassin replies May 20 (Day 2): "Interesting methodology. How does Domain 29's prosecutorial weaponization data interact with the Weil findings on state AG suppression? I'd like to share this with our state AG network." — direct reply (3.0) + referral (4.0) = 7.0
- Two silent re-shares: one unidentified contact emails saying "I received this from someone at Protect Democracy" — one confirmed silent re-share (0.5)
- Gist delta: 12 views (proxy, unverifiable — 12 < 15 view threshold for proxy counting; 0 proxy bonus)

**RSS Calculation**: 6.5 (Weiser) + 7.0 (Bassin) + 0.5 (silent re-share) = **14.0**

**QRC**: Weiser (weight 3.0+ signal: YES), Bassin (weight 3.0+ signal: YES) = **QRC = 2**

**Threshold check (Part 3.1)**:
- Row 2: RSS >= 8.0 AND QRC >= 2. RSS = 14.0 >= 8.0 AND QRC = 2 >= 2. **STRONG.**

**Classification: STRONG.**

**CHECKIN.md entry**: "Wave 1 Synthesis — STRONG. RSS = 14.0. QRC = 2 (Weiser, Bassin). Strongest signal: Bassin Score 4 (referral to state AG network). Law school window open. Phase 2 June 1 parallel launch pending user approval."

---

### Scenario B — 48h contingency triggered

**Situation**: May 20 12:00 UTC. Inbox check:
- 0 replies
- 0 bounces
- 0 OOOs
- Gist delta since H+0: 4 views (unverifiable proxy)

**RSS at 48h**: 0 (proxy Gist delta 4 views < 15-view threshold, no bonus). **QRC = 0.**

**Contingency check (Part 4.1)**: RSS = 0 AND QRC = 0 AND Gist delta <= 3? Gist delta = 4, slightly above threshold — borderline. Apply delivery self-test before activating contingency.

**Delivery self-test**: Send test email to self from same account. It lands in inbox.

**Delivery is confirmed.** Gist delta 4 = marginal (reads may have occurred but without document dwell). 

**Decision**: Activate contingency Option C (pause, monitor through 72h close). Gist activity is slight but present. Document in signal log: "May 20 12:00 UTC — 48h contingency check. Delivery confirmed. Gist delta 4 (borderline). Option C selected — monitor to 72h close. No Reserve list activation yet."

**Next check**: May 20 22:00 UTC. If still 0 replies and Gist delta still <= 5 total: activate Option A (Reserve list) — the window is 12.5 hours from close and there is no further risk in reaching out to 2 Reserve contacts.

---

### Scenario C — WEAK confirmed

**Situation**: May 21 10:30 UTC (72h window close):
- 0 replies from all 5 contacts
- 0 bounces
- 0 OOOs
- Gist delta: 2 views total across all URLs

**RSS**: 0. **QRC**: 0. **Gist delta**: 2 (< 5 threshold).

**Threshold check**: Row 7 (RSS < 1.0 AND Gist delta <= 5) — WEAK, pending delivery check.

**Delivery self-test**: Test email lands in inbox. Delivery confirmed.

**Classification: WEAK (delivery confirmed).**

**CHECKIN.md entry**: "Wave 1 Synthesis — WEAK. RSS = 0. QRC = 0. Delivery confirmed via self-test. Law school window still open — do NOT classify Goodman/Chenoweth as non-response until May 28. Post-mortem protocol required: delivery audit + messaging audit + contact quality audit (May 25–28). No Batch 2 or Phase 2 research until user reviews revised messaging. Domain 39 June 8 non-negotiable regardless of post-mortem status."

---

## PART 7: DECISION OUTPUT FORMAT

### 7.1 Required CHECKIN.md Entry (May 21, by 20:00 UTC)

Post this entry under "Needs Your Input" using the following fields:

```
## Wave 1 Synthesis — May 21, 20:00 UTC

**Classification**: [STRONG / MODERATE / WEAK / TOO EARLY]
**RSS Total**: [X.X]
**QRC (contacts at weight >= 3.0)**: [X]
**Strongest signal**: [Contact], [Org], Weight [X] — [one sentence: what they said or did]
**Law school constituency (Goodman, Chenoweth)**: TOO EARLY — open through May 28
**Think tank constituency (Weiser, Bassin)**: [STRONG / MODERATE / WEAK / TOO EARLY]
**Legal aid constituency (Elias)**: [STRONG / MODERATE / WEAK / TOO EARLY]
**Gist delta (total views since H+0)**: [X] views
**Delivery confirmed**: [YES / NO — self-test result]

**Phase 2 path triggered**: [see PHASE_2_DOMAIN_RESEARCH_SEQUENCING.md Part 4 — STRONG/MODERATE/WEAK branch]
**User approval required before**: [D57/D59 pre-production / Batch 2 launch / messaging revision]
**May 25 final gate**: [what remains open / what to confirm by May 25]
**Domain 42 DEA deadline**: May 28 — [X] days. Check BATCH_1_CONTACT_LOG.md send status.
```

### 7.2 Handoff to PHASE_2_DOMAIN_RESEARCH_SEQUENCING.md

The classification feeds directly into `PHASE_2_DOMAIN_RESEARCH_SEQUENCING.md` Part 4 (Execution Strategy by Outcome Path). No translation required — that document uses the same STRONG/MODERATE/WEAK vocabulary. Once the May 21 classification is recorded in CHECKIN.md, the orchestrator reads Part 4 of the sequencing document on May 22 morning and activates the corresponding path branch.

**No ambiguity at handoff.** Classification is binary-path: one classification, one branch, one set of domain timelines, one set of subagent assignments. The synthesis framework (this document) produces the classification. The sequencing document (PHASE_2_DOMAIN_RESEARCH_SEQUENCING.md) executes it.

---

*Document prepared: May 19, 2026. Grounded in: Wave 1 actual send data (5 contacts, May 18, 08:00–10:00 UTC); WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md scoring schema; preliminary-signal-analysis-may18.md sector response norms; PHASE_2_DOMAIN_RESEARCH_SEQUENCING.md Part 4 path branches.*

*Sector baseline sources: M+R Benchmarks 2026 (nonprofit advocacy email: 1.4% mass; 6.2% targeted); Hunter.io State of Cold Email 2026; WAVE_1_MONITORING_DASHBOARD.md sector response norm calibration; DISTRIBUTION_PATH_EXECUTION_GUIDE.md response window documentation.*
