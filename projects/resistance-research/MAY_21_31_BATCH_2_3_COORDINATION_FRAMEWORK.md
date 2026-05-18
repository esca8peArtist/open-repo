---
title: "May 21–31 Batch 2–3 Advanced Coordination Framework"
created: 2026-05-18
revised: 2026-05-18
status: PRODUCTION-READY — activate May 20 morning after reviewing early signals
scope: "Batch 2-3 conditional sequencing with open rate and institutional reply thresholds, Domain 42 DEA deadline integration, Tier 2 secondary contact follow-up, contingency escalation decision trees, May 20–31 operations calendar"
decision_gates:
  - "May 20 10:00 UTC — open rate threshold check: >50% triggers Batch 2 acceleration"
  - "May 21 20:00 UTC — final classification gate"
  - "May 22–23 — Batch 3 institutional reply rate gate (>60% / 30–59% / <30%)"
  - "May 25 — Domain 42 outer limit for AG contacts"
  - "May 28 — DEA-1362 hard cutoff"
domain_42_deadline: "May 28, 2026 — DEA Docket DEA-1362 participation notice deadline (HARD CUTOFF)"
audience: "thorn — standalone executable document; no other file required at decision point"
companion_files:
  - WAVE_1_MONITORING_DASHBOARD.md
  - WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md
  - DOMAIN_42_AMPLIFICATION_STRATEGY.md
  - DISTRIBUTION_OUTREACH_CONTACTS.md
  - PHASE_1_POST_WAVE1_CONTINGENCY.md
  - PHASE_2_OUTCOME_LAUNCH_ROADMAP.md
---

# May 21–31 Batch 2–3 Advanced Coordination Framework

**Purpose**: Pre-stage all decision paths for Batches 2–3 before May 20 morning signals are known. Sections 1–2 govern early signal reading and the May 20 open rate gate. Section 3 controls Batch 2 conditional sequencing. Section 4 controls Batch 3 institutional reply rate activation. Section 5 integrates Domain 42 media and policy outreach with Batch 2–3 timing around the May 28 DEA hearing. Section 6 is the Tier 2 secondary contact follow-up protocol for May 23–25. Section 7 is the consolidated contingency escalation system.

**Wave 1 status**: COMPLETE. All 5 Batch 1 emails sent May 18, 08:00–10:00 UTC (Goodman, Weiser, Chenoweth, Bassin, Elias). Monitoring window open May 18–21.

**Domain 42 status**: May 28 DEA participation notice deadline (Docket DEA-1362) is hard and non-extensible. Organizations must have materials by May 25 at the outer limit to have 3 days for drafting and filing.

---

## SECTION 1: May 20 Signal Reading Protocol

### 1.1 What to Check on May 20 Morning (before 10:00 UTC)

By May 20 morning you have 48–60 hours of post-send data from Batch 1. Policy org contacts (Weiser, Bassin) are within their 2–5 day response window. Elias is the fastest likely responder given Callais litigation framing urgency. Law school contacts (Goodman, Chenoweth) are not yet in their response window — silence from them at 48 hours is within sector norm and does not penalize overall classification.

The May 20 assessment is a provisional classification. It activates preparation, not execution. The final classification runs May 21 at 20:00 UTC per WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md Section 2.

**Before reading the May 20 signals, pull these three data sources in order**:

1. Email inbox — reply count, reply type, Score assignments for each of the 5 Batch 1 contacts
2. Bitly/Gist analytics — total click delta on all shared URLs since 06:00 UTC May 18
3. Bounce notifications — any hard bounce is a delivery failure requiring immediate address correction before classification

### 1.2 May 20 Provisional Classification Table

Execute top to bottom; stop at first match:

| Priority | Condition | Classification | Immediate Action |
|----------|-----------|----------------|-----------------|
| 1 | Any Score 5 signal (integration in published work product, formal collaboration offered) | STRONG — override | Begin Batch 2 sends today; activate Section 3A |
| 2 | 2+ substantive replies (Score 3+) | STRONG (provisional) | Begin Batch 2 sends today; activate Section 3A |
| 3 | 1 substantive reply (Score 3+) | MODERATE (provisional) | Prepare Batch 2 drafts; sends start May 21; activate Section 3B |
| 4 | Gist delta >5 views, zero replies | MODERATE (lower end) | Prepare Batch 2 drafts; sends start May 21; do not accelerate |
| 5 | 1+ acknowledgment-only reply (Score 1), zero Score 3+ | MODERATE (lower end) | Same as Priority 4 |
| 6 | Zero replies, zero Gist delta, zero bounces | WEAK (suspected) | Run delivery diagnosis before any classification; Domain 42 AG sends proceed regardless |
| 7 | Hard bounces detected | PAUSE | Fix delivery before classification; Domain 42 AG sends proceed regardless |

**Domain 42 exception**: Priorities 6 and 7 do not pause Domain 42 state AG outreach. The May 28 deadline is external to the main framework delivery system. Send Domain 42 AG emails regardless of classification status.

---

## SECTION 2: Batch 2 Open Rate Threshold — Acceleration Decision (May 20 10:00 UTC)

### 2.1 The Open Rate Gate

The standard Batch 2 send window is May 21 (all paths). There is one condition under which Batch 2 accelerates to May 20: a >50% estimated open rate on Batch 1 emails by May 20 10:00 UTC.

**Why open rate, not reply rate, for the acceleration trigger**: Reply rate at 48 hours is a lagging signal — it reflects both interest and response-cycle norms, and law school contacts will not reply within 48 hours even if they read carefully. Open rate at 48 hours is a leading signal for delivery confirmation and initial engagement. A 50%+ open rate at 48 hours means at least 3 of the 5 contacts opened the email — confirmation that the distribution is reaching inboxes and that the subject line cleared initial attention filters. At that engagement level, the marginal benefit of waiting another 24 hours for the May 21 standard window is lower than the cost of delayed momentum.

**Open rate measurement**: The open rate proxy is Gist click delta + any email open pixel fire if your email client supports it. If you sent with a tracked link (Bitly): total Bitly click events divided by 5 sent = click-through rate, not open rate. Adjust: at 30–40% CTR (click-through rate), the estimated open rate is approximately 1.5–2x CTR given that not all openers click. Use CTR >25% as the proxy for >50% open rate if direct open tracking is unavailable.

### 2.2 Acceleration Decision Logic

```
MAY 20 10:00 UTC — BATCH 2 ACCELERATION CHECK

INPUTS:
  □ Estimated open rate (or Bitly CTR >25% as proxy): ____%
  □ Any Score 3+ replies already in: Y / N — count: ___
  □ Provisional classification (from Section 1.2): STRONG / MODERATE / WEAK / PAUSE

DECISION:
  □ Open rate >50% AND classification is STRONG (provisional):
    → ACCELERATE — Send Batch 2 Priority Group 1 today (5 contacts, May 20)
    → Continue with May 21 Priority Group 2–3 sends on STRONG schedule
    → Domain 42 Tier 1 AG sends also go today

  □ Open rate >50% AND classification is MODERATE (provisional):
    → PARTIAL ACCELERATE — Prepare Priority Group 1 today, send May 21 morning
    → Open rate confirms delivery and interest; reply rate is still within normal lag window
    → Domain 42 Tier 1 AG sends go today

  □ Open rate ≤50% AND classification is STRONG (provisional):
    → No acceleration — May 21 standard launch
    → STRONG classification from replies is sufficient signal; no need to push further

  □ Open rate ≤50% AND classification is MODERATE or WEAK:
    → No acceleration — May 21 standard (MODERATE) or diagnostic hold (WEAK)
    → Do not use open rate <50% as an independent justification for acceleration

OUTCOME: ACCELERATE / PARTIAL ACCELERATE / STANDARD / HOLD
```

### 2.3 What Acceleration Does and Does Not Change

**What it changes**: Priority Group 1 sends shift from May 21 morning to May 20. Domain 42 Tier 1 AG sends also shift to May 20 (they were already eligible for May 20 under STRONG path regardless).

**What it does not change**: The May 21 final classification gate. The May 24 Batch 3 go/no-go gate. The May 25 Domain 42 AG outer limit. The May 28 DEA filing deadline. None of these dates compress because of Batch 2 acceleration.

**Social proof in accelerated Batch 2 emails**: Under acceleration, you do not yet have the full May 21 engagement data. Reference only signals you have confirmed by May 20 morning. Do not project or extrapolate. If Weiser replied substantively, you can reference "early engagement from colleagues at the Brennan Center." If only Gist click signals exist, do not reference any engagement — lead with the domain hook directly.

---

## SECTION 3: Batch 2 Contact Sequencing (May 20–21)

### 3.1 Priority Group Assignments

Batch 2 draws from the academic, think tank, and media pillars in DISTRIBUTION_OUTREACH_CONTACTS.md. The send sequence below is pre-sorted by (a) domain alignment strength, (b) fastest response cycle, and (c) May 28 DEA deadline urgency.

**Priority Group 1 — Law School Election Law and Democracy Clinics (10 contacts)**

These produce the highest-value social proof for subsequent Batch 3 sends. Their domain overlap with Domains 1, 37, 56, 57, and 59 is direct. Send May 20 (STRONG + acceleration) or May 21 (all other paths).

| # | Contact | Institution | Primary Domain | Allocation |
|---|---------|-------------|---------------|-----------|
| 1 | Nicholas Stephanopoulos | Harvard Law | D1 (efficiency gap), D37 | May 20 (accel) / May 21 |
| 2 | Nikolas Bowie | Harvard Law | D2, D34 (impoundment) | May 20 (accel) / May 21 |
| 3 | Ruth Greenwood | Harvard Law / Voting Rights Litigation Clinic | D1, D33, D37 | May 20 (accel) / May 21 |
| 4 | Olatunde Johnson | Columbia Law / Constitutional Democracy Initiative | D2, D6, D29 | May 21 (all paths) |
| 5 | Gillian Metzger | Columbia Law | D2, D26, D34 | May 21 (all paths) |
| 6 | Kenji Yoshino | NYU Law | D7, D22 | May 21 (all paths) |
| 7 | Pamela Karlan | Stanford Law | D1, D6, D35 | May 21 (STRONG/MODERATE) |
| 8 | Erwin Chemerinsky | UC Berkeley Law | Full framework, D6, D29 | May 21 (STRONG/MODERATE) |
| 9 | William Baude | University of Chicago Law | D6, D35, D37 | May 21 (STRONG/MODERATE) |
| 10 | Richard Hasen | UCLA Law | D1, D33, D37 | May 21 (all paths — fastest academic responder) |

**Priority Group 2 — Policy Schools (5 contacts)**

| # | Contact | Institution | Primary Domain | Allocation |
|---|---------|-------------|---------------|-----------|
| 11 | Theda Skocpol | Harvard Kennedy School | D3, case studies | May 21 (all paths) |
| 12 | Archon Fung | Harvard Kennedy School / Ash Center | D3, D9, D26 | May 21 (all paths) |
| 13 | Jacob Hacker | Yale | D5, D17, D20 | May 21 (all paths) |
| 14 | Suzanne Mettler | Cornell | D3, D18, D26 | May 21 (STRONG/MODERATE) |
| 15 | Barry Rabe | Michigan Ford School | D15, D9 | May 27 (STRONG/MODERATE) |

**Priority Group 3 — Think Tanks (15 contacts)**

| # | Contact | Organization | Primary Domain | Allocation |
|---|---------|-------------|---------------|-----------|
| 16 | Molly Reynolds | Brookings | D2, D26, D34 | May 21 (STRONG/MODERATE) |
| 17 | Shahrzad Shams | Roosevelt Institute | D2, D26, D34 | May 20 (accel) / May 21 |
| 18 | Patrick Oakford | Roosevelt Institute | D17, D18 | May 21 (all paths) |
| 19 | Celine McNicholas | Economic Policy Institute | D17, D2 | May 21 (all paths) |
| 20 | Michael Waldman | Brennan Center | Full framework | May 21 (STRONG/MODERATE) |
| 21 | Kareem Crayton | Brennan Center | D1, D22, D33 | May 21 (STRONG/MODERATE) |
| 22 | Joanna Lydgate | States United Democracy Center | D37, D33, D1 | May 20 (accel, D37 urgency) / May 21 |
| 23 | Virginia Kase Solomón | Common Cause | D1, D2, D3 | May 21 (all paths) |
| 24 | Justin Florence | Protect Democracy | D2, D29 | May 21 (STRONG/MODERATE) |
| 25 | Todd Tucker | Roosevelt Institute | D23 | May 27 (STRONG/MODERATE) |
| 26 | Samara Angel | Brookings | D29, D26 | May 27 (STRONG) / hold (MODERATE/WEAK) |
| 27 | Matthew Continetti | AEI | D2, D34 (bipartisan frame) | May 27 (STRONG only) |
| 28 | Yuval Levin | AEI / National Affairs | D26, D2, D9 | May 27 (STRONG only) |
| 29 | A.J. D'Amico | Knight Foundation | D8, D4, D21 | May 27 (STRONG/MODERATE) |
| 30 | Jack Balkin | Yale Law | D6, D35 — litigation tracker specifically | May 27 (STRONG/MODERATE) |

**Priority Group 4 — Media (Domain 42 deadline-driven, all paths)**

| # | Outlet | Pitch Angle | DEA Deadline Priority | Allocation |
|---|--------|-------------|----------------------|-----------|
| 31 | AP Policy desk | May 28 DEA deadline, democratic exclusion | HIGH | May 19–20 (all paths) |
| 32 | Reuters Political | DEA hearing democratic exclusion angle | HIGH | May 19–20 |
| 33 | Axios Pro Rata | Regulatory capture angle | HIGH | May 19–20 |
| 34 | Politico Influence | Lobbying/regulatory capture | HIGH | May 19–20 |
| 35 | The Hill | DEA hearing news hook | HIGH | May 19–20 |
| 36 | Filter Magazine | Weill Cornell racial disparity data | May 20–21 | May 20–21 |
| 37 | NORML News | DEA hearing call to action | May 20–21 | May 20–21 |
| 38 | DRCNet | Democratic design argument | May 20–21 | May 20–21 |
| 39 | The Appeal | Felony disenfranchisement angle | May 24–25 | May 24–25 (STRONG/MODERATE) |
| 40 | The Marshall Project | 4M disenfranchised | May 24–25 | May 24–25 (STRONG/MODERATE) |
| 41 | WaPo Politics | Democratic participation angle | May 25 | May 25 (STRONG) |
| 42 | Mother Jones | Drug war as democratic exclusion | May 24–25 | May 24–25 (STRONG/MODERATE) |

---

## SECTION 4: Batch 3 Conditional Activation — Institutional Reply Rate Gate

### 4.1 What Triggers Batch 3

Batch 3 (labor unions, civil rights organizations, state AG networks, faith coalitions — 35+ contacts) activates on conditional logic, not on a fixed date. The activation condition is the **combined institutional reply rate** from Batch 1 + Batch 2 contacts assessed at two gate points: May 22 evening (preliminary) and May 24 18:00 UTC (final).

**Combined institutional reply rate** is defined as: (Score 3+ replies from Batch 1 + Batch 2 combined) divided by (Batch 1 + Batch 2 total adjusted sent count, excluding bounces and OOOs).

This metric differs from the Batch 1-only reply rate used in Section 1 classification. By May 22–23, you have 18–22 Batch 2 sends in addition to the 5 Batch 1 sends — a denominator of 23–27 contacts. A 60% institutional reply rate at that scale is a meaningful signal. A 30% rate is a different strategic situation. Less than 30% at that denominator indicates the framework is not resonating at the institutional level and Batch 3 requires messaging revision before sending.

### 4.2 Three-Scenario Activation Logic

**Scenario A — >60% combined institutional reply rate (May 22–23 or deferred to May 23–24)**

**Definition**: More than 60% of adjusted sent contacts (Batch 1 + Batch 2 combined) produce substantive replies (Score 3+) by May 22 18:00 UTC, OR by May 23 18:00 UTC if the May 22 assessment produces 50–60% (borderline — wait 24 hours to confirm).

**What this means at scale**: At 25 combined sent contacts (5 Batch 1 + 20 Batch 2), >60% = 15 or more substantive replies. This is above the typical benchmark for targeted institutional outreach (M+R 2026 adjusted baseline: 30–40% for highly targeted, personalized campaigns). A >60% signal means the framework argument is producing immediate operational recognition, not just acknowledgment.

**Batch 3 activation under Scenario A**:
- Activate May 22–23 (do not wait for May 24 18:00 UTC gate)
- Lead all Batch 3 emails with social proof from the strongest-performing Batch 1–2 constituency
- Prioritize civil rights organizations and labor unions in that order — both have been waiting for Batch 3 and have the fastest operational response cycles
- Batch 3 full volume: activate all 35+ contacts across the May 22–28 window

**Batch 3 Scenario A send schedule**:

| Date | Sector | Contacts | Messaging Variant |
|------|--------|----------|-----------------|
| May 22 | Civil rights Wave 1 | NAACP LDF, Lawyers' Committee, ACLU Voting Rights | STRONG with social proof |
| May 23 | Labor Wave 1 | CWA, SEIU, AFL-CIO Policy, AFSCME | STRONG with Domain 59 hook |
| May 24 | Civil rights Wave 2 | Color of Change, UnidosUS, AAJC, M4BL | STRONG |
| May 25 | Labor Wave 2 | UAW, USW, NEA, AFT, Jobs with Justice | STRONG with D39 urgency |
| May 27 | State networks + faith | Remaining AGs beyond D42 track; Poor People's Campaign; Faith in Action | STRONG |
| May 28 | Cross-aisle | Continetti (AEI), Levin (AEI) | Bipartisan rule-of-law framing |

---

**Scenario B — 30–59% combined institutional reply rate**

**Definition**: Between 30% and 59% of adjusted sent contacts produce substantive replies (Score 3+) by May 23 18:00 UTC.

**What this means at scale**: At 25 contacts, 30–59% = 8–15 substantive replies. This is within the expected range for targeted institutional outreach. The framework is producing engagement but not at the signal strength that warrants compressing the Batch 3 timeline.

**Batch 3 activation under Scenario B — Deferred to June 1**:
- Hold Batch 3 until June 1 for all contacts except labor (see exception below)
- Deferral rationale: Scenario B signal is sufficient to continue distribution but insufficient to justify burning the highest-operational-value Batch 3 contacts (civil rights, state networks) without a stronger social proof anchor. One more week of Batch 2 engagement data meaningfully improves the social proof available for the June 1 send.
- **Labor exception**: CWA, SEIU, AFL-CIO Policy, AFSCME send May 27 (not June 1) under Scenario B. Labor has the fastest operational response cycle of any Batch 3 sector and the least dependency on academic credibility social proof. They respond to domain utility framing directly. May 27 gives Domain 39 HHS urgency framing (June 1 HHS rule) maximum relevance.
- Civil rights, state networks, and faith coalitions: June 1 send with Scenario B MODERATE messaging variant

**Batch 3 Scenario B send schedule**:

| Date | Sector | Contacts | Messaging Variant |
|------|--------|----------|-----------------|
| May 27 | Labor only | CWA, SEIU, AFL-CIO, AFSCME | MODERATE with D39 urgency |
| June 1 | Civil rights | NAACP LDF, Lawyers' Committee, ACLU Voting Rights, M4BL, Mijente | MODERATE |
| June 1–3 | State networks | Remaining AG contacts; Color of Change, UnidosUS, AAJC | MODERATE |
| June 4–5 | Labor Wave 2 + faith | UAW, USW, NEA, AFT, JwJ; faith coalitions | MODERATE |

---

**Scenario C — <30% combined institutional reply rate**

**Definition**: Fewer than 30% of adjusted sent contacts produce substantive replies (Score 3+) by May 23 18:00 UTC (or by May 24 18:00 UTC as the final confirmation gate).

**What this means at scale**: At 25 contacts, <30% = fewer than 8 substantive replies. At the personalization depth and contact quality of Batch 1–2, this indicates a content-framing mismatch — the framework is not landing with institutional practitioners at operational depth. This is not a delivery failure (delivery is already confirmed by Batch 1 send); it is a messaging signal.

**Batch 3 activation under Scenario C — Messaging Rewrite + Extension**:
- DO NOT send Batch 3 with current messaging
- Begin messaging rewrite immediately: pivot from institutional credibility framing to election protection utility framing (specific analysis the contact can use operationally in the next 30 days)
- Revised Batch 3 messaging uses the Weak-path variant from PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 3 — leads with domain utility, no social proof, no reference to Wave 1 engagement
- Rewrite timeline: 2–3 hours to revise lead paragraphs for each sector; 1 day to review and confirm before sending
- Batch 3 extended launch: May 29–31 (labor and civil rights with revised messaging), June 3–5 (state networks and faith)
- Domain 42 track does not wait: state AG sends execute on the original May 20–25 schedule regardless of Scenario C classification

**Batch 3 Scenario C send schedule**:

| Date | Sector | Contacts | Messaging Variant |
|------|--------|----------|-----------------|
| May 24–25 | Messaging rewrite — no sends to Batch 3 | — | Revise: WEAK utility-forward framing |
| May 29 | Labor only (revised) | CWA, SEIU, AFL-CIO, AFSCME | WEAK — election protection utility |
| May 30 | Civil rights (revised) | NAACP LDF, Lawyers' Committee, ACLU Voting Rights | WEAK — election protection utility |
| May 31–June 2 | State networks + faith | Remaining AGs; civil rights Wave 2; faith coalitions | WEAK |
| June 3–5 | Extension sends | Remaining labor, remaining civil rights | WEAK |

### 4.3 Batch 3 Institutional Reply Rate Gate Checklist

```
BATCH 3 ACTIVATION GATE — MAY 23 18:00 UTC (preliminary) + MAY 24 18:00 UTC (final)

1. REPLY COUNT (5 min):
   □ Batch 1 substantive replies (Score 3+): ___
   □ Batch 2 substantive replies (Score 3+): ___
   □ Combined total substantive replies: ___
   □ Total adjusted sent (Batch 1+2, minus bounces/OOOs): ___
   □ Combined institutional reply rate: ___% (divide substantive replies by adjusted sent)

2. SCENARIO CLASSIFICATION (1 min):
   □ Rate >60%: SCENARIO A — activate Batch 3 May 22–23
   □ Rate 30–59%: SCENARIO B — labor May 27, all others June 1
   □ Rate <30%: SCENARIO C — messaging rewrite, May 29–31 launch

3. INTEGRATION SIGNAL CHECK (2 min):
   □ Any Score 4 or 5 from any Batch 1–2 contact: Y / N
   □ If yes: regardless of rate, use STRONG messaging variant in Batch 3

4. DOMAIN 42 STATUS CONFIRMATION (2 min):
   □ Tier 1 AGs (Mayes, Bonta, Weiser/CO, Nessel, Brown) — sent: Y / N
   □ Tier 2 AGs (Raoul, Kaul, Ford, Rosenblum) — sent: Y / N
   □ Any AG filing intent confirmed: Y / N — which AGs: ___

5. IMMEDIATE ACTION (5 min):
   □ Scenario A: Pull Batch 3 civil rights Wave 1 list; send May 22–23
   □ Scenario B: Pull labor sub-list for May 27; set June 1 reminder for full Batch 3
   □ Scenario C: Begin messaging rewrite now; pull PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 3 WEAK templates
   □ All scenarios: Check Domain 42 AG sends; any gaps must be filled by May 25 outer limit
```

---

## SECTION 5: Domain 42 Amplification Coordination (May 21–28)

### 5.1 Why Domain 42 Is Path-Independent

The May 28 DEA participation notice deadline (Docket DEA-1362) is external to the distribution pipeline. Whether Wave 1 produces STRONG, MODERATE, or WEAK signals, Domain 42 outreach to drug policy organizations and state AG offices executes on its own track. These contacts have faster institutional response cycles and a specific legal deadline creating genuine urgency that is independent of academic social proof.

**Confirmed deadline**: May 28, 2026. nprm@dea.gov. Docket No. DEA-1362. Hard cutoff — no extensions. Hearing dates: June 29–July 15, 2026 (DEA Hearing Facility, 700 Army Navy Drive, Arlington, VA 22202).

**Domain 42 distribution status at framework creation**: Waves 1 and 2 to drug policy and civil rights organizations already executed May 8–14 per DOMAIN_42_MAY_28_EXECUTION_PREP.md. Remaining work: Wave 3 (state AGs) and media amplification.

### 5.2 Domain 42 Media Outreach Coordination with Batch 2–3 Timing

The Domain 42 media calendar runs in parallel with the Batch 2–3 contact sequence. The key coordination constraint is that media pitches need to go before the organization contact sends for the same outlet or organization — a journalist covering the story creates context for the organizations receiving research materials, not the reverse.

**Week 1 (May 19–21) — Policy Press — Batch 2 concurrent**

Domain 42 policy press pitches begin May 19, the same day that Batch 2 Priority Group 4 media contacts receive their outreach. These sends are simultaneous by design: policy press coverage of the DEA deadline creates an ambient urgency signal for the academic and think tank contacts receiving Batch 2 outreach that same week.

| Date | Outlet | Pitch Lead | Batch 2 Coordination |
|------|--------|-----------|---------------------|
| May 19 (Mon) | AP Policy, Reuters Political | "May 28 DEA deadline — democratic exclusion architecture affecting 4M+ disenfranchised Americans" | Concurrent with Priority Group 4 media outreach |
| May 19 | Axios Pro Rata | Regulatory capture angle — 200 words max | Same |
| May 20 | Politico Influence, The Hill | Lobbying/regulatory capture frame | Phone follow-up May 21 |
| May 21 | Non-responder follow-up | One follow-up email to AP, Reuters, Axios | Concurrent with Batch 2 Priority Group 1–3 academic/think tank sends |

**Week 2 (May 20–23) — Drug Policy Specialized Press**

Drug policy specialized press has faster publication cycles than policy press. Filter Magazine, NORML News, DRCNet pitch the same democratic accountability angle to a sector audience that is already mobilized around the DEA hearing. These sends are specifically timed to precede the May 23 Batch 3 civil rights Wave 1 activation (Scenario A) or labor pre-activation (Scenario B) — coverage in drug policy press supports the social proof claim for organizations receiving Batch 3 outreach that the research has broader ecosystem traction.

| Date | Outlet | Data Hook | Batch 3 Coordination |
|------|--------|----------|---------------------|
| May 20 | Filter Magazine | Weill Cornell May 1 data: legalization alone does not close racial disparities | Before Batch 3 civil rights Wave 1 (May 22–23, Scenario A) |
| May 20 | NORML News | DEA hearing democratic participation angle | Same |
| May 20 | DRCNet | Democratic design argument — structural exclusion architecture | Same |
| May 21 | LEAP newsletter | Law enforcement perspective on regulatory capture | Cross-partisan |
| May 21 | MPP newsletter | Federal-state conflict + SAFER Banking | Before Batch 3 state AG outreach |

**Week 3 (May 24–27) — Civil Rights and National Press — Around May 28 deadline**

The civil rights and national press outreach runs alongside the May 24–27 Batch 3 sends. This is the most time-sensitive coordination window. Organizations receiving Batch 3 outreach May 22–25 will see civil rights press coverage of the DEA hearing within the same week — reinforcing the urgency framing and providing external validation of the democratic accountability angle.

| Date | Outlet | Angle | Coordination |
|------|--------|-------|-------------|
| May 24 | The Appeal | Felony disenfranchisement feedback loop — DEA hearing as democratic participation moment | Concurrent with Batch 3 civil rights Wave 2 |
| May 24 | The Marshall Project | 4M disenfranchised Americans, criminal justice reform frame | Same |
| May 25 | WaPo Politics | Democratic participation angle — broadest national audience | Concurrent with Domain 42 AG outer limit |
| May 25 | Mother Jones | Drug war as democratic exclusion — investigative framing | Same |
| May 26 | ACLU Communications, Sentencing Project | Amplify any existing coverage | Coalition voice — supports any coverage already in play |
| May 27 | Voting rights journalists at national outlets | Callais cascade + drug disenfranchisement intersection | Concurrent with Batch 3 labor completion |

### 5.3 Domain 42 State AG Send Schedule

State AG outreach executes regardless of Wave 1–2 classification. The schedule accelerates relative to the standard Batch 3 timeline because AG offices need the full 3-day drafting buffer before May 28.

| AG Tier | Organizations | Target Send | Materials |
|---------|--------------|------------|---------|
| Tier 1 | AZ (Mayes), CA (Bonta), CO (Weiser), MI (Nessel), WA (Brown) | May 20–21 | D42 Section 4 (federal-state conflict) + participation notice template |
| Tier 2 | IL (Raoul), WI (Kaul), NV (Ford), OR (Rosenblum) | May 21–22 | D42 Sections 4 + 3 (disenfranchisement) |
| Tier 3 | NY (James), NJ, PA, MN, CT | May 22–23 | D42 Sections 2 + 4 |
| Tier 4 | Remaining SAFER Banking signatories | May 23–24 | D42 Section 4 only (federalism framing) |

**May 25 is the outer limit for all AG sends under MODERATE path. Under WEAK path, all AG sends must complete by May 23 to give the full 5-day buffer.**

### 5.4 May 28 Post-Deadline Assessment Metrics

Check the following on May 29–30 via the Federal Register docket for DEA-1362:

| Metric | How to Check | Success Threshold |
|--------|-------------|------------------|
| Participation notices filed by contacted organizations | federalregister.gov docket for DEA-1362 | ≥1 organization we contacted files |
| Media coverage citing democratic accountability angle | Google News: "DEA marijuana democratic" / "DEA rescheduling disenfranchisement" | Any article using the framework angle |
| Direct replies confirming hearing participation | Email inbox | Any organization confirming they filed |
| State AG formal comment or brief | AG press releases; docket page | ≥1 AG office filed or announced intent |

---

## SECTION 6: Tier 2 Secondary Contact Follow-Up (May 23–25)

### 6.1 Who This Protocol Applies To

The Tier 2 secondary follow-up activates May 23 for organizations that have shown integration signals (Score 4–5) from any Batch 1 or Batch 2 send, or any Domain 42 Wave 1–2 organization that replied but has not confirmed filing intent for the DEA hearing. This is a targeted escalation of the highest-value existing relationships — not new outreach.

**Integration signal definition** (Score 4–5 per WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv):
- Score 5: Cited the research in a filing, brief, publication, or internal document
- Score 4: Asked how to operationalize, mentioned a colleague they are forwarding to, or forwarded internally
- Any Domain 42 organization that acknowledged receipt but has not confirmed a participation notice

**Target window**: May 23 (two business days after May 21 Batch 2 sends) through May 25 (Domain 42 AG outer limit). This window is tight by design — organizations are already engaged, and the May 28 deadline creates a natural urgency anchor for all three follow-up asks.

### 6.2 The Three-Ask Strategy

**Rule**: One ask per organization, per follow-up. Do not compound asks in a single email. Choose the ask most aligned with the organization's signal and operational capacity.

**Ask 1 — Implementation Commitment**

Use when: The organization has the research and has asked substantive questions (Score 3–4) but has not specified how they will use it. The goal is to convert interest into a concrete use-case commitment.

Target organizations (Score 3–4 from Batch 2 or Domain 42 Wave 1–2 with no stated use):
- Brennan Center (Waldman, Crayton) if they asked substantive questions without specifying use
- States United Democracy Center (Lydgate) if they replied without implementation detail
- Common Cause (Solomón) if they replied generally
- Any Batch 2 think tank that replied at Score 3 without naming a specific integration plan

**Subject line**: `Following up — implementing [Domain X] analysis in your work`

**Template body**:

> Thank you for your reply to my [date] email. One specific follow-up question: do you see an opportunity to incorporate the [Domain X] analysis into [specific work product — a brief you are preparing / an upcoming report / your organization's public communications]?
>
> The section most directly relevant to [organization's current focus] is [Section reference — e.g., "Section 4.2 on the SAVE Act false positive data" / "the NVRA-Medicaid enrollment nexus in Section 3.1"]. I can send a targeted excerpt with source citations formatted for direct integration if that would be useful.
>
> The reason I am following up now is the May 28 DEA hearing deadline — if your organization's current work touches drug policy or felony disenfranchisement, the Domain 42 section may be deployable before that date.
>
> No action required if this timing does not work. I will follow up on the broader framework in mid-June when the hearing pressure has passed.
>
> [Your name] | [Contact information]

**Personalization requirement**: Replace [Domain X] with the domain the contact asked about. Replace [specific work product] with something concrete you know they are working on from their reply or their organization's website. The May 28 DEA hook is optional — omit if the organization's work has no drug policy connection.

---

**Ask 2 — DEA Testimony Commitment**

Use when: The organization's work directly overlaps with DEA hearing topics — drug policy, felony disenfranchisement, regulatory capture, federalism conflicts with state cannabis laws. The ask is explicit: will they file a participation notice by May 28?

Target organizations (highest priority):
- Drug Policy Alliance (press@drugpolicy.org) — Wave 1 sent; follow up May 21–22 if no notice confirmed
- NORML (norml@norml.org) — Wave 1 sent; follow up on participation notice status
- The Sentencing Project (staff@sentencingproject.org) — Wave 1 sent; highest natural alignment for testimony
- LEAP (info@leap.cc) — Wave 1 sent; law enforcement angle is high-credibility for DEA
- State AGs who replied to Domain 42 outreach — AG participation notice carries higher institutional weight than advocacy testimony
- Prison Policy Initiative (info@prisonpolicy.org) — disenfranchisement data directly applicable

**Subject line**: `DEA hearing May 28 — will [organization] file a participation notice?`

**Template body**:

> Following up on the Domain 42 research I shared on [date]. The DEA-1362 participation notice deadline is May 28 — that is [X] days away.
>
> I want to ask directly: is [organization] planning to file a participation notice for the June 29 hearing?
>
> If yes: I have a pre-drafted participation notice template that can be adapted to [organization]'s letterhead in approximately 30 minutes. The template covers [the democratic exclusion argument / the felony disenfranchisement feedback loop / the SAFER Banking federalism conflict] with specific citations to your organization's existing published work. I can send it immediately.
>
> If you are on the fence because of staff bandwidth: the participation notice itself is a 200–400 word letter stating intent to participate and a brief summary of testimony focus. You do not need written testimony by May 28 — only the notice of intent.
>
> If your organization is not planning to file: would it be possible to amplify another organization's filing through your newsletter or social media? I can provide a social post template that takes five minutes.
>
> [Your name] | [Contact information]

**Personalization notes**: Fill [X] days with the accurate countdown (May 23 = 5 days; May 24 = 4 days; May 25 = 3 days). For state AG offices: replace "participation notice" with "formal comment or amicus brief filing" and omit the social media offer.

---

**Ask 3 — Co-Sign or Coalition Statement**

Use when: The organization has engaged at Score 4–5 and has institutional stature to co-sign a joint communication — an open letter, joint op-ed, or coalition statement to the DEA. This is the highest-ask variant and goes only to organizations with demonstrated engagement depth.

Target organizations (co-sign ask only to Score 4–5 confirmed):
- Any Batch 1 contact that produced Score 4–5 reply — highest-trust relationship at this point
- Brennan Center (if engaged) — co-sign a coalition letter to DEA or joint op-ed on democratic exclusion
- NAACP LDF (if engaged by May 23) — joint statement on the disenfranchisement-drug policy nexus
- Multiple state AGs who replied — joint state AG letter to DEA carries maximum institutional weight
- Drug Policy Alliance + The Sentencing Project (if both engaged) — joint op-ed from two leading organizations

**Subject line**: `Coalition opportunity — [organization] + [project] joint statement on DEA-1362`

**Template body**:

> I am reaching out because of the strong engagement you have shown with the research I shared — specifically [reference the specific signal: "your question about the SAFER Banking federal-state conflict" / "your note that this aligns with your current felony disenfranchisement report"].
>
> I want to propose something more direct: would [organization] be willing to co-sign a brief joint statement published publicly before the May 28 DEA hearing deadline?
>
> The statement makes three points: (1) the DEA rescheduling decision has democratic participation implications extending beyond drug policy, specifically the 4+ million Americans subject to felony disenfranchisement, disproportionately in states where cannabis reform has the most democratic support; (2) the DEA-1362 proceeding has excluded civil rights and voting rights organizations in ways that parallel previous democratic exclusion from drug policy design; (3) the signing organizations urge DEA to extend the participation period and convene a round of testimony from voting rights, civil rights, and democratic accountability experts before June 29.
>
> I can draft the full statement text and circulate for review within 24 hours. Your organization's signature requires: one staff member reviews the draft, approves, and sends a confirmation email. Estimated time investment: 30 minutes.
>
> If this is too much for current bandwidth: the testimony ask (Template B above) requires significantly less and has the same deadline. I can downshift if preferred.
>
> [Your name] | [Contact information]

### 6.3 Tier 2 Follow-Up Target Table

| # | Organization | Contact | Follow-Up Type | Send Date | Trigger Condition |
|---|-------------|---------|---------------|-----------|-----------------|
| T2-1 | Drug Policy Alliance | press@drugpolicy.org | Ask 2 (Testimony) | May 21 if no reply to Wave 1; May 23 if acknowledgment only | Wave 1 sent May 8–14 |
| T2-2 | NORML | norml@norml.org | Ask 2 (Testimony) | May 21 if no reply; May 23 if acknowledgment | Same |
| T2-3 | The Sentencing Project | staff@sentencingproject.org | Ask 2 (Testimony) | May 21 if no reply; May 23 if acknowledgment | Highest natural alignment |
| T2-4 | LEAP | info@leap.cc | Ask 2 (Testimony) | May 21 if no reply; May 23 if acknowledgment | Law enforcement angle |
| T2-5 | ACLU Criminal Law Reform | nationaloffice@aclu.org | Ask 2 (Testimony) | May 22–23 | D42 Wave 1 sent; 4-day follow-up window |
| T2-6 | Prison Policy Initiative | info@prisonpolicy.org | Ask 2 (Testimony) | May 22 | First D42 outreach triggers follow-up at 24h |
| T2-7 | Brennan Center (Waldman/Crayton) | Via Brennan Center contact | Ask 1 (Implementation) | May 23 | Batch 2 sent May 21; follow up on Score 3+ signal |
| T2-8 | States United Democracy Center (Lydgate) | Via statesunited.org | Ask 1 or 3 | May 23 | Depends on engagement score from Batch 2 |
| T2-9 | NAACP LDF (Nelson) | naacpldf.org/contact | Ask 3 (Co-sign) | May 23 | Only if Score 4–5 from Batch 2; do not cold-pitch co-sign |
| T2-10 | First 3 state AGs to reply | Per Section 5.3 allocation | Ask 2 or 3 | May 23–24 | Any AG reply to D42 outreach triggers escalation |
| T2-11 | Common Cause (Solomón) | Via commoncause.org | Ask 1 (Implementation) | May 24 | Batch 2 sent May 21; any reply |
| T2-12 | Any Batch 1 contact with Score 4–5 | Per original Batch 1 addresses | Ask 3 (Co-sign) | May 23 | Score 4–5 from Wave 1 monitoring |

**Follow-up send discipline**: One follow-up per organization per thread. If Ask 2 produces no reply by May 26, do not send a second follow-up before May 28. The deadline itself will either move them or it will not. Multiple follow-ups before the deadline signal desperation and reduce credibility.

---

## SECTION 7: Contingency Escalation Paths

### 7.1 Escalation Threshold Overview

Three contingency branches activate based on quantitative triggers. Run the escalation check at the May 21 20:00 UTC classification gate and again at the May 24 18:00 UTC Batch 3 go/no-go gate.

| Branch | Trigger | Activates |
|--------|---------|----------|
| 1 — Low reply rate | <30% substantive reply rate by May 21 10:30 UTC from Batch 1 | Section 7.2 |
| 2 — Bounce spike | >10% hard bounce rate in Batch 2 sends | Section 7.3 |
| 3 — Negative sentiment | Any reply with hostile, adversarial, or professionally damaging framing | Section 7.4 |

### 7.2 Branch 1 — Low Reply Rate Escalation

**Trigger confirmation**: Before activating Branch 1, confirm this is a content signal, not a delivery signal. Run the 5-minute delivery diagnosis:
1. Check inbox for bounce notifications — any hard bounce = delivery problem, not engagement problem
2. Check Bitly: any click events = delivery confirmed to at least one inbox
3. Send a test email to yourself from the same account and time of day — if it lands in spam, you have a delivery failure, not a content failure. Fix delivery via PHASE_1_POST_WAVE1_CONTINGENCY.md Variant A1 before running any Branch 1 action

**If delivery is confirmed and reply rate is still <30%**:

**Immediate action 1 — SSRN submission (within 2 hours of trigger confirmation)**:

Submit Domain 42 as a standalone research paper to SSRN. The title must include "DEA" and "democratic" for hearing discoverability. Use this abstract:

> *This paper examines the DEA rescheduling proceeding (Docket No. DEA-1362) through the lens of democratic participation and institutional accountability. Three accountability failures are documented: exclusion of civil rights and voting rights stakeholders from a proceeding affecting felony disenfranchisement for 4+ million Americans; federal-state conflict between DEA scheduling authority and voter-approved frameworks in 24 states; and regulatory capture in the selection of authorized hearing participants. Three structural interventions are proposed: mandatory stakeholder inclusion requirements for DEA scheduling decisions; a judicial review pathway for democratic-exclusion claims; and a congressional reporting requirement connecting scheduling decisions to documented civil rights impacts.*

SSRN indexes within 24–48 hours. Google Scholar picks up within 48–72 hours of SSRN indexing. By May 25 the paper is discoverable via "DEA rescheduling democratic accountability" searches.

**Immediate action 2 — A2 retargets to Batch 1 (same day as trigger confirmation)**:

Send revised single-hook follow-ups to the 5 Batch 1 contacts. Each email: 150 words maximum, one specific question, one Gist URL (not all 8), no advocacy language in subject line.

| Contact | New Hook | New Subject Line |
|---------|---------|-----------------|
| Ryan Goodman | April 21 SPLC indictment — documented charging defects | "One question — SPLC indictment charging defects" |
| Wendy Weiser | SAVE Act 81% false positive rate — four-state analog data | "SAVE Act false positive rate — methodology question" |
| Erica Chenoweth | 3.5% threshold — US reversibility vs. Poland vs. Hungary | "Threshold question — reversibility comparison" |
| Ian Bassin | Enforcement gap when DOJ is institutionally captured | "Litigation theory question — DOJ capture enforcement gap" |
| Marc Elias | NVRA 90-day quiet period — 77 days to window close | "NVRA quiet-period — 77 days to window close" |

**Immediate action 3 — Academic coalition bypass (May 22–23)**:

Send directly to 10 domain-specific academic contacts who are closer to the DEA hearing topic than the main Batch 2 academic law sequence:

| # | Contact | Institution | Email | Why Prioritize Under Low Reply |
|---|---------|-------------|-------|-------------------------------|
| AC-1 | Rachel Barkow | NYU Law | rbarkow@law.nyu.edu | Regulatory capture in criminal law — exact fit |
| AC-2 | Mason Marks | FSU Law | mason.marks@fsu.edu | DEA administrative capture — his own published work |
| AC-3 | Ohio State DEPC team | Moritz Law | depc@moritz.osu.edu | Drug enforcement and policy — closest academic center to DEA procedural question |
| AC-4 | Alex Kreit | Thomas Jefferson Law | Via TJSL | Controlled substances law casebook author |
| AC-5 | Jonathan Caulkins | Carnegie Mellon Heinz | Via CMU | Most quantitative drug policy voice |
| AC-6 | Keith Humphreys | Stanford | humphreys@stanford.edu | Clinical/policy bridge |
| AC-7 | Erik Luna | George Mason Law | eluna@gmu.edu | Criminal law and admin law overlap |
| AC-8 | Douglas Husak | Rutgers | Via Rutgers Philosophy | Philosophy of drug law — democratic theory angle |
| AC-9 | Morgan Fox | NORML | Via NORML | Policy practitioner with academic framing capacity |
| AC-10 | Mark Kleiman colleagues | NYU Marron Institute | Via Marron Institute | Drug policy empirics network |

**Branch 1 implementation timeline**:

| Day | Action |
|-----|--------|
| Day 0 (trigger confirmed) | SSRN submission (2 hours); A2 retargets to Batch 1 (1 hour) |
| Day 0 + 24h | SSRN indexed; Google Scholar crawl begins |
| Day 1 | Academic coalition outreach (10 emails, 90 minutes) |
| Day 2 | Domain 42 AG outreach proceeds independently (Section 5.3) |
| Day 3 | Check SSRN abstract page for view count; Batch 3 labor + civil rights proceed regardless |
| Day 4 | Google Scholar indexes; paper discoverable |
| May 28 | Deadline — paper is on record regardless of engagement outcome |

### 7.3 Branch 2 — Bounce Spike Escalation

**Trigger**: More than 2 hard bounces out of the first 20 Batch 2 sends (>10% bounce rate). Contact list source (DISTRIBUTION_OUTREACH_CONTACTS.md) was last verified April 27 — approximately 3.5 weeks old at the May 20 send date. Academic email addresses turn over at 5–8% annually.

**Immediate action**:
1. Pause all remaining Batch 2 sends
2. Run spot-check on the next 10 contacts — verify current institutional affiliation and email address against their organization's faculty/staff page the day of sending, not from the saved list
3. Resume sends with verified addresses only; each correction logged

**High-confidence fallback contacts** (use if bounce spike is severe and time is critical):

| # | Contact | Email | Confidence Basis |
|---|---------|-------|-----------------|
| HC-1 | Ryan Goodman | ryan@justsecurity.org | Non-institutional domain — lowest churn risk |
| HC-2 | Wendy Weiser | wweiser@brennancenter.org | Organizational address; stable |
| HC-3 | Marc Elias | melias@elias.law | Personal law practice domain |
| HC-4 | Ian Bassin | ian@protectdemocracy.org | Founder address |
| HC-5 | Richard Hasen | rhasen@law.ucla.edu | Long-tenure faculty |
| HC-6 | Joanna Lydgate | Via statesunited.org | President; small org, stable routing |
| HC-7 | Virginia Kase Solomón | Via commoncause.org/contact | CEO-level; organizational routing |

**Timeline after bounce-spike trigger**: Hour 0–1 pause and spot-check. Hour 1–3 verify and update addresses. Hour 3+ resume with verified addresses only. Domain 42 AG sends (governmental addresses) are unaffected — governmental email addresses have negligible churn rates.

### 7.4 Branch 3 — Negative Sentiment Escalation

**Trigger**: Any reply that contains explicitly hostile, dismissive, or professionally damaging language — including a reply indicating the contact is sharing the communication negatively with colleagues, or a removal request that includes critique of the research framing.

**What is NOT a trigger**: Substantive methodological critique ("I think Domain 3 overstates the evidence for X") = Score 3, not a contingency trigger. The trigger is adversarial or adversely-networked framing, not critical engagement.

**Immediate action (within 2 hours)**:
1. Pause Batch 3 sends (Batch 2 pauses only if the hostile contact is in a sector that shares networks with remaining Batch 2 targets — e.g., if the hostile contact is at Harvard Law and remaining Batch 2 includes Harvard Law colleagues)
2. Domain 42 AG sends do NOT pause — they are independent materials to independent contacts
3. Log the reply verbatim in CHECKIN.md under "Needs Your Input — Negative Signal" immediately
4. Send the damage-control response to the specific contact within 4 hours

**Damage Control Template (Template D1)**:

> Thank you for your reply. I want to respond directly to [specific concern raised].
>
> [If the concern is about methodology]: You are raising a legitimate question I should address more precisely. The claim that [X] is based on [specific source + link]. If you see a gap in that evidence chain, I would genuinely welcome the correction — improving the analysis is the goal.
>
> [If the concern is about framing or politics]: I understand how [framing element] could read as [their concern]. The intent was [original intent] — I can revise the relevant section to address this.
>
> [If the concern is about being contacted]: I will not reach out to you further. I am removing your address from my distribution list now.
>
> [Your name]

**Proactive Stakeholder Communication Template (Template D2)** — use only if evidence exists that the hostile reply has been shared with colleagues:

> I am following up on a message that [contact name] may have shared with you. I want to address the concern directly: [one-sentence response to the core objection].
>
> The research is available at [Gist URL] for your own review. I welcome any feedback and will not reach out further unless you respond.
>
> [Your name]

**Branch 3 stakeholder contacts for proactive damage control** (if negative signal has traveled):

| # | Organization | Why Prioritized | Contact |
|---|-------------|----------------|---------|
| SC-1 | Brennan Center | Policy/law sector convergence point | wweiser@brennancenter.org |
| SC-2 | Protect Democracy | Bassin's network; if any Batch 1 contact shares a negative response, Bassin may hear | ian@protectdemocracy.org |
| SC-3 | Just Security | Goodman is a networked editor — negative signals from shared contacts travel through his editorial network | ryan@justsecurity.org |
| SC-4 | Democracy Docket | Elias's voting rights network is large; negative response in voting rights community may reach him quickly | melias@elias.law |

**Branch 3 implementation timeline**:

| Time | Action |
|------|--------|
| Hour 0 | Receive hostile reply; log verbatim in CHECKIN.md immediately |
| Hour 0–1 | Pause Batch 3 (conditional per above); Domain 42 AG sends continue |
| Hour 1–4 | Draft and send Template D1 response to hostile contact |
| Hour 4 | Assess whether signal has traveled — check for follow-up from other contacts referencing the hostile reply |
| Hour 4–8 | If signal has traveled: send Template D2 proactively to SC-1 through SC-4 as appropriate |
| Day 2 | Resume Batch 3 if no further negative signals |
| Day 3+ | Resume normal cadence; consider whether a messaging adjustment is warranted for remaining sends |

---

## SECTION 8: May 21–31 Consolidated Operations Calendar

This calendar integrates Batch 2–3 conditional sends, Domain 42 media and AG outreach, Tier 2 follow-ups, and contingency checks into a single day-by-day view. Columns show the STRONG path; MODERATE and Scenario B/C deviations are noted in parentheses.

| Date | Primary Batch Actions | Domain 42 Action | Tier 2 Follow-Ups | Decision Gate |
|------|----------------------|-----------------|------------------|---------------|
| May 20 | STRONG + accel: 5 Priority Group 1 sends (Stephanopoulos, Lydgate, Shams, Hewitt, Nelson) / MODERATE: Prepare only | Tier 1 AGs (Mayes, Bonta, Weiser/CO) — all paths | — | Open rate check 10:00 UTC (Section 2.2) |
| May 21 | 15–22 Batch 2 (Priority Groups 1–3, Tier A think tanks) | Tier 2 AGs; AP, Reuters, Axios media pitches | T2-1–T2-4 follow-up if no Wave 1 reply (Template Ask 2) | 20:00 UTC final classification (WAVE_1_SYNTHESIS) |
| May 22 | Scenario A: Batch 3 civil rights Wave 1 / Others: Batch 2 completion | Tier 2 AGs (Raoul, Kaul, Ford, Rosenblum); drug policy press (Filter, NORML, DRCNet) | T2-5, T2-6 (ACLU, Prison Policy Initiative — Ask 2) | — |
| May 23 | Scenario A: Batch 3 labor Wave 1 / Scenario B: Prepare labor (May 27) | Civil rights press (The Appeal, The Marshall Project) | T2-7–T2-12 opens: Brennan Center, States United, NAACP LDF, Common Cause (Asks 1–3 based on signal) | Batch 3 institutional reply rate preliminary gate 18:00 UTC |
| May 24 | Scenario A: Batch 3 civil rights Wave 2, think tanks / Scenario B: Hold (June 1) | Tier 3 AGs (NY, NJ, PA); outer limit for MODERATE AG sends | T2-10: first 3 AG replies → Ask 2 or Ask 3 escalation | Batch 3 go/no-go final gate 18:00 UTC |
| May 25 | Remaining think tanks (D'Amico, Tucker if not sent) | OUTER LIMIT — all AG contacts must have materials; WaPo, Mother Jones pitch | T2-11: Common Cause follow-up if not yet replied | Domain 42 assessment checkpoint (Section 5.4) |
| May 26 | Balkin (Yale); SSRN check if Branch 1 active | Reminder-only to AGs not yet confirmed; voting rights journalists | — | — |
| May 27 | Labor completion (NEA, AFT, Teamsters, USW, JwJ); Scenario B labor Wave 1 (CWA, SEIU, AFL-CIO, AFSCME) | No new AG outreach | Final follow-up to any T2 contacts who have not replied (one email maximum) | — |
| May 28 | STRONG only: cross-aisle think tanks (Continetti, Levin) | HARD DEADLINE 23:59 UTC — monitor nprm@dea.gov filings | — | Domain 42 filing deadline |
| May 29–30 | Phase 2 research planning; law school window still open through Day 10 | Post-deadline impact assessment (Section 5.4) | — | — |
| May 31 | Final close-out; May 31 assessment in PROJECTS.md | Final docket check; confirm all AG sends logged | — | May 31 close-out |

**Total sends across May 20–31**:
- STRONG path (Scenario A): 70–90 contacts
- MODERATE path (Scenario B): 55–70 contacts
- WEAK path (Scenario C): 30–50 contacts

---

## SECTION 9: Cross-Document Reference Index

This framework is executable without consulting any other document. The following references are for extending context only:

| Reference | File | What It Adds |
|-----------|------|-------------|
| Wave 1 classification formula | WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md Section 2 | Full STRONG/MODERATE/WEAK scoring logic |
| Batch 1 engagement data | WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv rows 2–6 | Real-time reply scores and Gist click data |
| Phase 2 domain sequencing | PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 2 | Domain prioritization matrix by constituency outcome |
| Domain 42 DEA details | DOMAIN_42_AMPLIFICATION_STRATEGY.md | Full media calendar, sector messaging variants, organization checklist |
| Weak-path messaging variants | PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 3 | Ready-to-use Weak-path email templates for all constituencies |
| Post-Wave-1 contingency playbook | PHASE_1_POST_WAVE1_CONTINGENCY.md | Full delivery diagnosis, Variant A1/A2/A3 escalation procedures |
| Tier 2 pre-contact checklist | PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 5 | Complete Tier 2 preparation checklist for June sends |

---

*Document revised: May 18, 2026. Supersedes the May 18 initial version with enhanced Batch 2 open rate gate (Section 2), Batch 3 three-scenario institutional reply rate logic (Section 4), Domain 42 coordination calendar integrated with Batch 2–3 timing (Section 5), Tier 2 secondary contact follow-up protocol with three ask templates (Section 6), and consolidated contingency escalation decision trees (Section 7).*

*Execution status: Production-ready. Next required action: May 20 10:00 UTC open rate check (Section 2.2) and provisional classification (Section 1.2).*
