---
title: "Wave 1 Synthesis Framework — Skeleton for May 21, 2026"
created: 2026-05-18
status: SKELETON — populate with live data May 21 20:00 UTC
scope: "Structured synthesis framework for May 21 72-hour classification checkpoint; path-activation decision tree; user gate at May 21 14:00 UTC (preliminary) and May 25 (final)"
execute_at: "May 21, 20:00 UTC"
user_gate: "May 21, 14:00 UTC (preliminary); May 25 (final confirmation)"
audience: thorn — executable framework; all sections marked [FILL] require live data at time of synthesis
companion_files:
  - WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md
  - post-wave-1-monitoring/wave-1-signal-log-may18-21.md
  - post-wave-1-monitoring/preliminary-signal-analysis-may18.md
  - PHASE_2_OUTCOME_LAUNCH_ROADMAP.md
  - WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv
---

# Wave 1 Synthesis Framework — May 21, 2026

*Execute at May 21, 20:00 UTC. Populate all [FILL] sections with live data from wave-1-signal-log-may18-21.md before running classification.*

---

## PART 1: DATA ASSEMBLY (May 21 20:00 UTC)

Pull all data from wave-1-signal-log-may18-21.md. Complete every row before proceeding to Part 2.

### 1.1 Contact Response Summary

| Contact | Org | Reply Received | Score | Quality Reply Points | OOO | Bounce | Notes |
|---------|-----|----------------|-------|---------------------|-----|--------|-------|
| Ryan Goodman | Just Security / NYU Law | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | |
| Wendy Weiser | Brennan Center | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | |
| Erica Chenoweth | Harvard Kennedy School | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | |
| Ian Bassin | Protect Democracy | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | |
| Marc Elias | Democracy Docket / ELG | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | |

**Quality Reply Points calculation**:
- Score 5: STRONG OVERRIDE — stop, classify as STRONG, flag in CHECKIN.md
- Score 4 = 2 points
- Score 3 = 1 point
- Score 1–2 = 0 points (confirmed delivery only)
- OOO: remove from denominator; add return date to pending list
- Hard bounce: remove from denominator; add re-verification task

### 1.2 Gist Analytics

| Metric | Value |
|--------|-------|
| Total Gist view delta since H+0 (all URLs) | [FILL] |
| Dominant Gist (most views) | [FILL] |
| Gist bonus points (delta / 5, capped at 1.0) | [FILL] |

### 1.3 Aggregate Metrics

| Metric | Value |
|--------|-------|
| Total sent | 5 |
| Hard bounces | [FILL] |
| OOOs (removed from denominator) | [FILL] |
| Adjusted send count | [FILL] |
| Total substantive replies (Score 3+) | [FILL] |
| Raw substantive response rate | [FILL]% |
| TOTAL QUALITY REPLY POINTS (contact scores + Gist bonus) | [FILL] |

---

## PART 2: CLASSIFICATION FORMULA

*From WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md Section 2.*

### 2.1 Score 5 Override Check

Has any Batch 1 contact cited the framework in a published work, filing, testimony, or offered formal collaboration?  
[ ] YES — classify as STRONG immediately; skip to Part 3 (STRONG path). Flag in CHECKIN.md.  
[ ] NO — proceed to Step 2.2.

### 2.2 Quality Reply Points Classification

**Total Quality Reply Points**: [FILL from Part 1.3]

| Threshold | Classification |
|-----------|---------------|
| >= 2 Quality Reply Points AND >= 40% response rate | STRONG |
| >= 1 Quality Reply Point (any Score 3+) OR Gist delta > 10 with zero replies | MODERATE |
| < 1 Quality Reply Point AND response rate < 20% AND Gist delta <= 5 | WEAK (after delivery confirmed) |

**Preliminary classification**: [ ] STRONG [ ] MODERATE [ ] WEAK [ ] TOO EARLY (law school cycle)

### 2.3 Constituency-Level Classification

Run independently for each constituency. Used for PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 2 domain matrix.

**Law Schools** (Goodman, Chenoweth):  
Expected at 72h: TOO EARLY — do not classify at this checkpoint. Return: May 25.  
72h result: [FILL] | Constituency note: [FILL]

**Think Tanks / Policy Orgs** (Weiser, Bassin):  
STRONG threshold: 1 of 2 at Score 3+ within 5 days. Have 5 days elapsed? [FILL]  
72h result: [FILL] | Constituency classification: STRONG / MODERATE / WEAK / TOO EARLY

**Immigration Legal Aid** (Elias):  
STRONG threshold: Score 3+ within 72h, or case-specific content within 5 days.  
72h result: [FILL] | Constituency classification: STRONG / MODERATE / WEAK / TOO EARLY

**Unions / Labor**: No Batch 1 contact. N/A at this gate — Tier 2 only.

---

## PART 3: PATH-ACTIVATION DECISION TREE

### Branch A: STRONG (Quality Reply Points >= 2 + response rate >= 40%; or Score 5 override)

**Immediate actions** (Day of classification):
1. Flag in CHECKIN.md: "STRONG outcome — Phase 2 June 15 parallel launch approval pending user confirmation."
2. Queue Domain 57 pre-production checklist (confirm 21 source URLs live; constitutional asymmetry outline for Section 2 by June 8; acquire Ikenberry)
3. Queue Domain 59 pre-production checklist (confirm 22 source URLs live; read D31 and D47 for Section 5 synthesis prep; acquire BLS gig economy data by June 8)
4. Prepare Tier 2 pre-contact list: immigration legal aid and law schools first (fastest response cycles); unions second (Week 6); think tanks concurrent (research-in-progress access)

**Phase 2 domain sequence**:
- Domain 39 pre-distribution: by June 1 (non-negotiable)
- Domain 56 distribution: May 28 (on schedule)
- Domain 58 distribution: June 15 (on schedule)
- Domain 57 LAUNCH: June 15 (Week 5, parallel with D59)
- Domain 59 LAUNCH: June 15 (Week 5, parallel with D57)
- Tier 2 pre-contact activation: Week 5 (June 15–21) for all four constituencies

**User gate**: Confirm STRONG path before Phase 2 June 15 launch. Do not begin D57/D59 pre-production research without user approval.

---

### Branch B: MODERATE (1 Quality Reply Point; or Gist delta > 10 with zero replies)

**Immediate actions** (Day of classification):
1. Log MODERATE classification in wave-1-signal-log-may18-21.md.
2. Continue monitoring to May 25 final gate. No accelerated action required.
3. At May 25 gate: run full Week 1 synthesis per WAVE_1_DAILY_MONITORING_TEMPLATE.md Step 1–4.

**Phase 2 domain sequence**:
- Domain 39 pre-distribution: by June 1 (non-negotiable)
- Domain 56 distribution: May 28 (on schedule)
- Domain 58 distribution: June 15 (on schedule)
- Domain 57 PRIMARY research launch: June 10 (one week earlier than STRONG but primary domain)
- Domain 59 SECONDARY research launch: July 1 (compressed; no peer review buffer before Aug 1 target)
- Tier 2 pre-contact activation: Week 6 (June 22–28) — lead with policy window urgency, not social proof

**User gate**: May 25 final classification. Confirm MODERATE path before Domain 57 June 10 launch. Social proof framing in Tier 2 emails available only if Wave 1 produced at least one Score 3+ reply — use specifically, not generically.

---

### Branch C: WEAK (Quality Reply Points < 1, response rate < 20%, Gist delta <= 5)

**Before classifying as WEAK — delivery diagnosis required**:
1. Run delivery self-test: send from same account to own email. Does it land in spam?
2. Check all Gist URLs: if any shows delta > 0, at least one contact opened the link — delivery confirmed
3. If self-test lands in spam: pause classification; pause all further sends; fix sender reputation; resend to Batch 1 from revised domain; restart classification clock from confirmed successful resend date

**If delivery confirmed and signals are genuinely weak**:
1. Log WEAK classification in wave-1-signal-log-may18-21.md.
2. Flag in CHECKIN.md: "WEAK outcome — Phase 1 remediation required; messaging audit before Phase 2."
3. Begin delivery audit, messaging audit, contact quality audit (8–12 hrs/week through June 1 alongside domain work)

**Phase 2 domain sequence**:
- Domain 39 pre-distribution: by June 1 (non-negotiable, regardless of Weak outcome)
- Domain 56 distribution: May 28 (on schedule)
- Domain 58 distribution: June 15 (on schedule)
- Domain 38 (AI Regulatory Capture): pre-production begins June 3; distribution target June 30 (5 weeks before Aug 2 EU AI Act)
- Domain 40 (Surveillance Capitalism): production begins June 22; target July 15
- Domain 57: deferred to August 1 research start (September 1 completion; 3-week UNGA lead time)
- Domain 59: deferred to July 15 research start (August 31 completion; no peer review buffer)
- Tier 2 activation: Week 7 (June 29–July 5), contingent on D39 producing at least one positive engagement signal

**User gate**: Before any messaging revision, confirm with user whether the issue is delivery or content. Do not revise content until delivery diagnosis is complete.

---

### Branch D: TOO EARLY (Law school contacts not yet within response window; no Think Tank / Policy signals)

**When to use**: 72-hour checkpoint shows zero replies from all contacts AND zero Gist delta AND no bounces.

**Actions**:
1. Log as TOO EARLY — not WEAK — in wave-1-signal-log-may18-21.md.
2. Run delivery self-test to confirm emails were delivered (not spam-folded).
3. Continue to May 25 gate without any path-activation decision.
4. Do not begin Phase 1 remediation based on 72h silence alone.

**Why**: 2 of 5 contacts (Goodman, Chenoweth) operate on 5–10 day academic cycles. A third contact (Elias) is a litigator whose 48-hour window has not yet produced data at the 72-hour mark if reply arrives Day 4+. TOO EARLY is the correct classification when the evidence base is structurally insufficient, not when signals are negative.

---

## PART 4: SIGNAL CLASSIFICATION RUBRIC

*For consistent scoring of every reply. Apply to each response as it arrives.*

### STRONG Indicators (any one sufficient for constituency-level STRONG)

- Score 4: Contact asks how to operationalize or names a colleague/org receiving the materials
- Score 4: Contact asks for a domain extract formatted for a specific use (brief, testimony, clinic application)
- Score 5: Contact cites the framework in a public document (STRONG OVERRIDE for aggregate classification)
- Score 5: Contact offers formal institutional collaboration (co-publication, co-filing, institutional distribution)
- Elias-specific: Any reply referencing a case name, docket number, or specific litigation theory within 72h
- Weiser/Bassin-specific: Any reply requesting distribution to a named state or organizational partner

### MODERATE Indicators

- Score 3: Domain-specific question ("How does Domain 57 interact with the Curtiss-Wright sole organ doctrine?")
- Score 3: Methodological critique referencing specific causal claims or data sources
- Score 3: Request for additional materials (source list, full domain text, related domains) — without naming a specific application
- Gist delta > 10 with zero email replies — indicates link was shared internally; high proxy for genuine engagement without formal reply

### WEAK Indicators (do not apply until Day 7 for policy orgs; Day 14 for law schools)

- Score 1 only: "Thanks for this, will read when I get a chance" — confirmed delivery but zero engagement quality
- Silence through Day 7 with confirmed delivery (policy orgs / think tanks)
- Silence through Day 14 with confirmed delivery (law school contacts)
- Score 1 followed by silence through Day 10 (any constituency)

### Administrative (not a signal, just logistics)

- OOO with return date: remove from denominator; schedule follow-up for return date + 1 business day
- Hard bounce: re-verify email immediately; do not count as non-response in classification

---

## PART 5: USER GATE STRUCTURE

### May 21, 14:00 UTC — Preliminary Gate

*If strong signals are present at the 72-hour checkpoint, flag in CHECKIN.md before 20:00 UTC synthesis.*

**Trigger for preliminary gate notification**: Any Score 4+ signal from any Batch 1 contact.

**What to flag**: "PRELIMINARY STRONG SIGNAL — [Contact] replied at Score [X] with [content summary]. 72-hour synthesis at 20:00 UTC. Phase 2 STRONG path may activate pending your confirmation."

**User decision required**: Confirm or modify Phase 2 path selection at the May 21 20:00 UTC synthesis.

### May 21, 20:00 UTC — Primary Synthesis Gate

**Actions at this gate**:
1. Populate Part 1–2 of this document with live data
2. Run classification formula (Part 2)
3. Identify preliminary path per Part 3 decision tree
4. Present to user in CHECKIN.md: classification, confidence level, recommended path, required approvals
5. If STRONG: request user approval for Phase 2 June 15 launch
6. If MODERATE: request user confirmation of May 25 final classification process
7. If WEAK: request user decision on delivery diagnosis vs. content revision

**Format for CHECKIN.md entry**:
```
## Wave 1 Synthesis — May 21, 20:00 UTC

**Preliminary classification**: [STRONG / MODERATE / WEAK / TOO EARLY]
**Quality Reply Points**: [X] / 5 adjusted contacts
**Strongest signal**: [Contact], [Org], Score [X], [one-sentence content summary]
**Law school constituency**: TOO EARLY — classify at May 25
**Think tank constituency**: [STRONG / MODERATE / WEAK]
**Immigration legal constituency**: [STRONG / MODERATE / WEAK]

**Recommended path**: [A: STRONG / B: MODERATE / C: WEAK / D: TOO EARLY]
**Needs Your Input**: [specific decision required, with options]
```

### May 25 — Final Classification Gate

*Requires no additional synthesis document — run WAVE_1_DAILY_MONITORING_TEMPLATE.md Week 1 Checkpoint steps 1–4 and update wave-1-signal-log-may18-21.md with final data.*

**At May 25**:
- Law school response window closes (Day 7 — expected first replies from Goodman/Chenoweth)
- OOO contacts with return dates before May 25 should now be responding
- Final Quality Reply Points calculated with law school constituency included
- Phase 2 path confirmed; Phase 2 domain sequencing and Tier 2 pre-contact activation proceeds

---

## PART 6: TRANSITION TO MAY 21 SYNTHESIS TASK

**When to execute this framework**: May 21, beginning at 19:00 UTC. Allow 30–45 minutes to complete Parts 1–2 and identify preliminary path. User gate notification in CHECKIN.md by 20:00 UTC.

**What to read before executing**:
1. wave-1-signal-log-may18-21.md — all entries through May 21 (raw signal data)
2. WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv — scoring reference
3. WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md Section 2 — classification formula
4. PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 1 — constituency-level threshold reference

**Documents to update upon classification**:
- wave-1-signal-log-may18-21.md: Day 3 / 72-hour snapshot section
- CHECKIN.md: Wave 1 synthesis entry under "Needs Your Input" (if strong signals or WEAK diagnosis needed)
- preliminary-signal-analysis-may18.md: Update section 6 (update log)

**If STRONG path confirmed**: Begin PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 4.2 domain pre-production checklists immediately.

**If MODERATE or TOO EARLY**: No research action until May 25 final gate. Continue monitoring May 22–24 per WAVE_1_DAILY_MONITORING_TEMPLATE.md Days 4–6.

**If WEAK (delivery confirmed)**: Begin Phase 1 remediation per PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 4.4 Week 1 protocol. Flag in CHECKIN.md.
