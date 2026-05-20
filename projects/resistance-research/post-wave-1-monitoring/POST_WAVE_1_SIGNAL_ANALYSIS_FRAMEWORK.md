---
title: "Post-Wave-1 Signal Analysis Framework"
date: 2026-05-20
status: READY FOR EXECUTION — May 21 19:00–20:00 UTC
scope: "Operationalize May 21 synthesis decision with objective metrics. Eliminate ambiguity in STRONG/MODERATE/WEAK classification."
audience: Orchestrator + user (thorn) for May 21 20:00 UTC synthesis checkpoint
related_items:
  - EXPLORATION_QUEUE.md Item 73
  - wave-1-signal-log-may18-21.md (live data source)
  - wave-1-synthesis-framework-skeleton.md (executable template)
---

# Post-Wave-1 Signal Analysis Framework

## Overview

This framework translates Wave 1 response signals into an objective classification (STRONG / MODERATE / WEAK / TOO_EARLY). The synthesis checkpoint happens May 21, 20:00 UTC (72 hours after send). This document defines:

1. **Response Classification Schema** — what counts as a signal, weighted by quality
2. **Sector-Specific Baselines** — expected response rates per contact type
3. **STRONG/MODERATE/WEAK Thresholds** — quantitative decision rules
4. **Contingency Triggers** — what to do if signals stall before May 21
5. **Decision Protocol** — exact May 21 execution steps

---

## 1. RESPONSE CLASSIFICATION SCHEMA

### 1.1 Signal Scoring System (Primary Metric)

Each contact's first reply is scored 0–5 on a single dimension: **engagement quality**.

| Score | Definition | Quality Points | Examples | When to Assign |
|-------|-----------|-----------------|----------|---|
| **0** | No signal | 0 | Silence through monitoring window | No reply received by checkpoint |
| **1** | Acknowledgment only | 0 | "Thanks, will read"; "Got it" | Confirms delivery, zero engagement content |
| **2** | General positive | 0 | "This is interesting"; "Good work" | Positive framing, no domain-specific content |
| **3** | Substantive engagement | 1 point | "How does D37 interact with *Curtis-Wright*?"; methodological critique; specific citation request | Domain-specific question OR methodological critique OR targeted request |
| **4** | Implementation signal | 2 points | "Can you send D57 formatted for amicus brief?"; "I'll share with [colleague X]"; asks how to operationalize | Practical application ask OR named referral OR implementation question |
| **5** | STRONG OVERRIDE | = STRONG immediately | Public citation in work/brief/testimony; formal collaboration proposal; Elias-specific litigation match | Contact cites framework in published work OR offers formal partnership |

**Quality Points accumulation**: Sum points from all contacts' initial replies.  
**Maximum possible**: 4 contacts × 2 points = 8 points (Score 4 signals from 4 contacts)

---

### 1.2 Secondary Metrics

**Gist Analytics Signal** — indicates internal sharing without formal reply

| Metric | Collection | Interpretation |
|--------|-----------|---|
| Gist total view delta since H+0 | User checks incognito (daily, no sign-in bias) | Views > 0 = at least one contact accessed the link |
| Dominant Gist (most views) | Check which Gist URL received most traffic | Domain most relevant to this cohort? |
| View delta > 10 | Indicates network-level sharing without email reply | **Gist bonus**: +0.5 quality points if delta > 10 AND zero email replies |

**Delivery Confirmation** — required before weak signals trigger remediation

| Signal | Interpretation |
|--------|---|
| Any Gist delta > 0 | At least one contact opened the link — delivery confirmed |
| Any Score 1+ reply | Confirmed delivery |
| Self-test lands in spam | Sender reputation issue — do not classify; resend after domain fix |
| Zero Gist delta + zero replies + no bounces after 72h | Possible spam; run delivery diagnosis before classifying WEAK |

---

## 2. SECTOR-SPECIFIC BASELINES

### 2.1 Contact Cohort Composition

| Contact | Organization | Sector | Response Cycle | Batch 1 Include? |
|---------|--------------|--------|---|---|
| Ryan Goodman | Just Security / NYU Law | Law School | 5–10 days | Yes |
| Erica Chenoweth | Harvard Kennedy School | Law School | 5–10 days | Yes |
| Wendy Weiser | Brennan Center | Think Tank / Policy | 1–3 days | Yes |
| Ian Bassin | Protect Democracy | Think Tank / Policy | 1–3 days | Yes |
| Marc Elias | Democracy Docket / ELG | Immigration Legal Aid / Litigation | 48–72 hours | Yes |

**Total Batch 1 contacts**: 5

---

### 2.2 Sector-Level Expected Response Rates

#### Law Schools (Goodman, Chenoweth)

**Timeline**: Academic calendar response cycle.  
**Day 1 (May 18)**: ~0% (end of business Friday in US Eastern)  
**Day 2–3 (May 19–20)**: ~5–10% (weekend; low likelihood)  
**Day 5–7 (May 22–24)**: ~40% expected (first full academic week)  
**Day 14 (May 31)**: ~80% expected (end of first full two weeks)

**Interpretation at 72-hour checkpoint (May 21)**:  
- Score 1+: AHEAD OF SCHEDULE; document signal carefully
- Score 0: **TOO EARLY** — do not count as non-response; continue to May 25

**Why**: Law school academics operate on semester timelines with email backlogs. Response clock starts Monday morning, not Friday evening.

---

#### Think Tanks / Policy Organizations (Weiser, Bassin)

**Timeline**: Business cycle response; policy orgs monitor inbound continuously.  
**Day 1 (May 18)**: ~20% (late business Friday, end of day)  
**Day 2 (May 19)**: ~40–50% expected (first full business day after send)  
**Day 3 (May 20)**: ~60% expected (cumulative)  
**Day 5 (May 22)**: ~75% expected

**Interpretation at 72-hour checkpoint (May 21)**:  
- 2 of 2 at Score 1+: STRONG signal (above baseline; likely captured substantive interest)
- 1 of 2 at Score 1+: MODERATE signal (on baseline)
- 0 of 2 replies: Could be anomaly (check delivery); could be genuine disinterest

**Why**: Policy org workflows prioritize external inbound. If no reply by 72h, either email bounced/spammed or recipient determined low priority.

---

#### Immigration Legal Aid / Litigation (Elias)

**Timeline**: Litigator response cycle; case docket dependent.  
**Day 1–2 (May 18–19)**: ~30% (case-loaded calendars; may delay if in hearing/deposition)  
**Day 2–3 (May 19–20)**: ~50–70% expected (if case-relevant)  
**Day 4 (May 21)**: **Critical anomaly point** — if no reply by 72h, likely not relevant to active docket

**Interpretation at 72-hour checkpoint (May 21)**:  
- Score 3+ (case-specific): STRONG signal (domain-expert engagement; litigation applicability confirmed)
- Score 1–2: MODERATE signal (acknowledged relevance, not actively litigated)
- Score 0 after 72h: WEAK signal for this contact; may indicate no active case match

**Why**: Elias's firm (ELG / Democracy Docket) operates on active litigation dockets. Relevant materials get same-day or next-day response. Silence beyond 72h suggests materials don't map to current active cases.

---

### 2.3 Aggregate Response Rate Thresholds

| Threshold | Interpretation | Action |
|-----------|---|---|
| **3–5 of 5 replies by 72h** | STRONG baseline signal; above expected for this cohort | Prepare STRONG path |
| **2–3 of 5 replies by 72h** | ON baseline for this cohort; requires quality assessment | Check quality scores; if Score 3+, proceed MODERATE; if Score 1–2, continue monitoring to May 25 |
| **0–1 of 5 replies by 72h** | BELOW baseline; requires delivery diagnosis | Before declaring WEAK, confirm delivery via Gist delta or self-test |

---

## 3. STRONG / MODERATE / WEAK / TOO_EARLY THRESHOLDS

### 3.1 Quantitative Decision Rules

#### **STRONG** (Proceed immediately to Phase 2 STRONG path)

**Any one of**:
- **Score 5 reply from any contact** → immediate STRONG, flag in CHECKIN.md, no further analysis needed
- **Score 4 + Score 3 from different contacts** (≥ 2 quality points total) → STRONG
- **2+ Score 4 replies** (≥ 4 quality points total) → STRONG
- **Elias-specific**: Score 4+ with case-specific litigation content (case name, docket number, theory match) within 72h → STRONG for immigration legal constituency
- **Weiser/Bassin-specific**: One contact at Score 4+ + state/org distribution ask → STRONG for think tank constituency
- **Response rate ≥ 60%** (3+ of 5) AND ≥ 1 Quality Reply Point → STRONG

**Additional indicator**: Gist total delta > 20 views (suggests network-level sharing + direct reply combo)

**Confidence**: HIGH — signals indicate substantive engagement sufficient to justify Phase 2 acceleration to June 15.

---

#### **MODERATE** (Continue monitoring; Phase 2 standard timeline)

**Threshold**:
- **1 Quality Reply Point** (exactly one Score 3 or one Score 4) with confirmed delivery → MODERATE
- **2+ Score 2 replies + 1+ Gist delta > 5** (indicates internal sharing despite email acknowledgment-only) → MODERATE
- **Response rate 40–59%** (2+ of 5) with Score 1–2 only → MODERATE (on-baseline delivery confirmation)
- **Gist total delta 10–20** with zero email replies → MODERATE (network sharing detected, no direct reply)

**Decision gate**: May 25 final classification. Continue standard Phase 2 timeline unless May 25 data shifts to STRONG or WEAK.

**Confidence**: MEDIUM — signals indicate interest but ambiguity about implementation/integration. Phase 2 proceeds on standard timeline (Domains 56, 58, 57 June 10–15).

---

#### **WEAK** (Requires delivery diagnosis + potential messaging revision)

**Threshold**:
- **Score 0 (zero replies) + Gist delta = 0 + no bounces** (possible spam) → Requires delivery diagnosis before WEAK declaration
- **Score 1 only (acknowledgment with no follow-up) + zero other replies + Gist delta ≤ 2** (confirmed delivery, zero engagement) → WEAK
- **Response rate < 20%** (0–1 of 5) AND all Score 0 (zero replies) → WEAK (after delivery confirmed)
- **Quality Reply Points = 0** + response rate < 40% → WEAK

**Before classifying WEAK**:
1. **Run self-test**: Send from same account to own email. Check spam folder.
2. **Check Gist analytics**: If any Gist shows delta > 0, at least one contact accessed the link — delivery confirmed.
3. **If self-test lands in spam**: Do not classify WEAK yet. Fix sender reputation; resend Batch 1; restart clock.

**If delivery confirmed genuinely weak**:
- Flag in CHECKIN.md: "WEAK outcome — Phase 1 messaging/contact quality audit required before Phase 2."
- Begin diagnosis: Is issue (a) delivery/spam, (b) messaging framing, (c) contact list relevance, or (d) timing?
- Continue Phase 2 timeline (Domains 56, 58, 39 proceed on schedule) while conducting audit alongside.

**Confidence**: MEDIUM — signals indicate possible delivery or messaging issue, not necessarily framework irrelevance.

---

#### **TOO_EARLY** (Do not classify; continue monitoring to May 25)

**Trigger**:
- **Zero replies from all 5 contacts** (Score 0 across the board) **AND** zero Gist delta AND no bounces after 72h

**Why TOO_EARLY, not WEAK**:
- 2 of 5 contacts (Goodman, Chenoweth) operate on 5–10 day academic cycles — silence at 72h is structurally expected for this cohort
- 1 of 5 contacts (Elias) has 48–72h response window; silence through 72h may indicate reply scheduled for Day 4–5
- Decision framework requires complete evidence base (law school data + litigation data); 72h window is insufficient

**Action**:
- Do not activate WEAK remediation pathway
- Do not pause Phase 2 domain work
- Continue monitoring May 22–24 per daily monitoring template
- Final classification at May 25 gate with law school response window closed

**Confidence**: HIGH — TOO_EARLY is the correct classification when evidence base is incomplete, not when signals are negative.

---

### 3.2 Decision Matrix (Quick Reference)

| Scenario | Quality Points | Response Rate | Gist Delta | Decision | Confidence |
|----------|---|---|---|---|---|
| 1 Score 4 + 1 Score 3 | 3 pts | 40%+ | >0 | **STRONG** | HIGH |
| 1 Score 4 + 0 other replies | 2 pts | 20% | >0 | **STRONG** | HIGH |
| 1 Score 3 + 2 Score 1 | 1 pt | 60% | >0 | **MODERATE** | MEDIUM |
| 2 Score 1 + 0 Gist | 0 pts | 40% | 0 | **MODERATE** | MEDIUM (delivery confirmed) |
| 0 responses + Gist delta 0 | 0 pts | 0% | 0 | **TOO_EARLY** | HIGH (delivery status unclear) |
| 1 Score 1 + 3 Score 0 + Gist 0 | 0 pts | 20% | 0 | **WEAK** | MEDIUM (after delivery confirmed) |
| 1 Score 1 + 3 Score 0 + Gist > 5 | 0.5 pts | 20% | >5 | **MODERATE** | MEDIUM (network sharing detected) |

---

## 4. CONTINGENCY TRIGGERS & FALLBACK LOGIC

### 4.1 Signal Stall Scenarios

**Scenario A: Zero responses through May 20 evening (24 hours before synthesis)**

**Trigger**: No replies by May 20 22:00 UTC (48 hours post-send for Weiser/Bassin, 48-72h for Elias)

**Diagnosis**:
- Check Gist delta. If > 0: delivery confirmed, proceed with 48h data as preliminary signal.
- Check self-test: send to own email; confirm lands in inbox (not spam).
- If all checks pass: Silence at 48h is within baseline for law school contacts but suggests weak signal for policy orgs / Elias.

**Fallback action**:
- Continue monitoring through May 21 10:30 UTC with higher sensitivity to Elias (should reply by 72h if case-relevant).
- Prepare MODERATE or WEAK path for synthesis, not STRONG.
- Do not pause Phase 2 domain research based on 48h silence alone.

---

**Scenario B: Only law school contacts reply; policy org silence (May 20 evening)**

**Trigger**: Goodman OR Chenoweth reply by May 20, but Weiser + Bassin + Elias silent

**Interpretation**: 
- Law school response violates baseline (should be silent at 48–60h). Indicates either (a) strong relevance to academic work, or (b) anomalously fast email processing.
- Policy org silence at 48–60h is below baseline (should be 40%+ response rate by now).

**Fallback path**:
- If Goodman/Chenoweth reply is Score 3+: Proceed MODERATE (academic engagement confirmed; policy org data insufficient).
- If Goodman/Chenoweth reply is Score 1–2: Proceed TOO_EARLY (academic response outside normal cycle; insufficient data).
- Continue monitoring policy org contacts through May 21.
- Do not switch to WEAK path based on policy org silence alone.

---

**Scenario C: Elias silence through May 21 10:30 UTC (beyond 72h window)**

**Trigger**: No reply from Elias despite confirmed delivery by May 21 10:00 UTC

**Interpretation**:
- Elias's 48–72h response window has closed with zero signal.
- Either framework does not match active dockets, OR email did not arrive despite confirmation indicator.

**Fallback action**:
- Do not re-send immediately. Proceed with synthesis using other 4 contacts' data.
- If other contacts show STRONG/MODERATE signals, proceed with Phase 2 (immigration legal constituency marked "WEAK" in constituency-specific assessment, but overall outcome driven by think tank/law school data).
- If all 5 show silence, classify as TOO_EARLY (law school baseline dominates).
- Flag for May 25: re-verify Elias email; if re-verification needed, prepare Tier 2 batch with Elias alternative (Tom Jawetz, Gustavo Montes de Oca, or other democracy.org litigation contacts).

---

### 4.2 Pre-May-21 Escalation Triggers

**Escalate to user via CHECKIN.md immediately if**:

| Trigger | Escalation Text |
|---------|---|
| Any Score 5 signal received before May 21 | "STRONG OVERRIDE detected: [Contact] cited/partnered. Phase 2 STRONG path activates immediately pending your confirmation." |
| Gist total delta > 30 by May 20 | "HIGH network-level sharing detected (30+ views). Indicates strong secondary dissemination. Prepare for STRONG/MODERATE path." |
| Elias reply with case name/docket by May 20 | "Immigration legal ad constituency signaling: [Case name] match detected. Strong indicator of litigation applicability. STRONG path likely for D37." |
| Self-test lands in spam by May 19 | "Delivery alert: self-test lands in spam folder. Sender reputation issue detected. Do not classify as WEAK until resend verified. Recommend domain fix before May 25." |

---

## 5. MAY 21 DECISION PROTOCOL (EXECUTION STEPS)

### 5.1 Pre-Synthesis Checklist (May 21, 16:00 UTC)

**Orchestrator actions at 16:00 UTC (4 hours before synthesis)**:

- [ ] Read wave-1-signal-log-may18-21.md completely (all entries through May 21 10:30 UTC)
- [ ] Tabulate total response count + score distribution
- [ ] Check Gist analytics (user provides incognito view counts)
- [ ] Verify no hard bounces in logs
- [ ] Identify any Score 4+ signals (flag for immediate preliminary gate)
- [ ] Prepare preliminary classification (A/B/C/D) based on thresholds above

**If any Score 4+ detected before synthesis**:
- Write preliminary notification in CHECKIN.md: "Preliminary STRONG signal detected — [Contact], [score], [content]. Synthesis at 20:00 UTC will confirm."
- Continue to synthesis (do not skip analytical rigor; STRONG must be confirmed by formula).

---

### 5.2 Synthesis Execution (May 21, 19:00–20:00 UTC)

**Step 1: Data Assembly (5 minutes)**

Use wave-1-synthesis-framework-skeleton.md Part 1 to populate:
- Contact response summary (one row per contact, including Score, Quality Points, delivery status)
- Gist analytics (total delta, dominant URL, bonus points calculation)
- Aggregate metrics (total sent, bounces, adjusted send count, substantive response rate, total quality reply points)

---

**Step 2: Classification Formula (10 minutes)**

Use Section 3 thresholds (above) to determine preliminary classification:

1. Check for Score 5 override: Yes/No?
   - If YES: STRONG (skip remaining steps, proceed to Part 3)
   - If NO: continue

2. Tabulate total Quality Reply Points: _____ / 8 possible

3. Calculate response rate: _____ / _____ ×100 = _____ %

4. Consult Decision Matrix (Section 3.2) for your scenario:
   - Match your Quality Points + Response Rate + Gist Delta row
   - Read decision: **[STRONG / MODERATE / WEAK / TOO_EARLY]**

---

**Step 3: Constituency-Level Assessment (5 minutes)**

Run thresholds for each constituency independently:

| Constituency | Contacts | Score | Quality Reply Points | 72h Response Rate | Threshold Assessment |
|---|---|---|---|---|---|
| Law Schools | Goodman, Chenoweth | [fill] | [fill] | [fill] | TOO_EARLY (baseline) or STRONG/MODERATE if reply |
| Think Tanks | Weiser, Bassin | [fill] | [fill] | [fill] | STRONG / MODERATE / WEAK |
| Immigration Legal | Elias | [fill] | [fill] | [fill] | STRONG / MODERATE / WEAK |

Use these in CHECKIN.md presentation (e.g., "Law schools TOO_EARLY; think tanks STRONG; immigration legal MODERATE → aggregate MODERATE path with law school wildcard at May 25").

---

**Step 4: Present to User (by 20:00 UTC)**

Write CHECKIN.md entry (under "Needs Your Input" section):

```
## Wave 1 Synthesis — May 21, 20:00 UTC

**Preliminary classification**: [STRONG / MODERATE / WEAK / TOO_EARLY]
**Quality Reply Points**: [X] / 8
**Response rate**: [X]%
**Gist delta**: [X] views

**Constituency breakdown**:
- Law schools: [TOO_EARLY / STRONG / MODERATE / WEAK]
- Think tanks: [STRONG / MODERATE / WEAK]
- Immigration legal: [STRONG / MODERATE / WEAK]

**Strongest signals** (if any):
- [Contact], [Org], Score [X]: [one-sentence summary]

**Recommended path**: [A: STRONG / B: MODERATE / C: WEAK / D: TOO_EARLY]

**Phase 2 sequencing** (if STRONG/MODERATE):
- Domain 56/58 on schedule (May 28 / June 15)
- Domain 57 pre-production: [June 15 (STRONG) / June 10 (MODERATE)]
- Domain 59: [June 15 (STRONG) / July 1 (MODERATE)]
- Tier 2 activation: [Week 5 (STRONG) / Week 6 (MODERATE)]

**Needs Your Input**:
- Do you agree with [STRONG/MODERATE/WEAK] classification?
- If WEAK: Should we run delivery diagnosis (May 22–24) or content audit (May 25+)?
- If TOO_EARLY: Confirm we continue standard monitoring to May 25?

**Next checkpoint**: May 25 final classification (law school response window closes; OOO contacts expected to reply).
```

---

### 5.3 Fallback Decision Path (if ambiguous)

**If synthesis produces ambiguous result** (e.g., MODERATE by formula but one Score 4 signal from borderline contact):

1. Consult CHECKIN.md preliminary gates from May 21 14:00 UTC
2. If any Score 4+ was flagged, escalate to user for tie-breaker decision
3. User decides: activate STRONG path or hold MODERATE?
4. Document user choice in CHECKIN.md
5. Proceed with user-selected path (do not override with formula alone)

---

## 6. SUMMARY: QUICK REFERENCE FOR MAY 21 SYNTHESIS

### Decision Tree

```
START (May 21 20:00 UTC)
  ↓
[Any Score 5 reply?] → YES → STRONG ✓
  ↓ NO
[Quality Reply Points ≥ 2 OR Response Rate ≥ 60%?] → YES → STRONG ✓
  ↓ NO
[Quality Reply Points = 1 OR Gist delta 10-20 with zero replies?] → YES → MODERATE ✓
  ↓ NO
[All zero replies + zero Gist delta?] → YES → TOO_EARLY ✓
  ↓ NO
[Score 1 + zero other replies + low Gist delta?] → YES → [Deliver diagnosis check]
  ↓ → Delivery confirmed → WEAK ✓
  ↓ → Delivery unclear → TOO_EARLY ✓
```

### Three-Minute Classification Protocol

1. **Count replies**: _____ / 5 (exclude bounces, OOOs removed from denominator)
2. **Sum quality points**: _____ (Score 4+ only; Scale 1–2 = 0 points)
3. **Check Gist delta**: _____ views (bonus 0.5 points if > 10 and zero replies)
4. **Match Decision Matrix** (Section 3.2) with your numbers
5. **Read output**: [STRONG / MODERATE / WEAK / TOO_EARLY]
6. **Present to user** with constituency breakdown

---

## 7. REFERENCES

- **wave-1-signal-log-may18-21.md** — Live signal data (read before synthesis)
- **wave-1-synthesis-framework-skeleton.md** — Executable template (populate at synthesis)
- **WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv** — Scoring reference table
- **preliminary-signal-analysis-may18.md** — Sector baseline detail (background reading)
- **PHASE_2_OUTCOME_LAUNCH_ROADMAP.md** — Path activation procedures post-classification
- **WAVE_1_DAILY_MONITORING_TEMPLATE.md** — May 22–25 contingency monitoring (if WEAK/TOO_EARLY)

---

**Document Status**: READY FOR EXECUTION
**Execution Window**: May 21, 19:00–20:00 UTC
**Next Review**: May 25 (final classification gate)
