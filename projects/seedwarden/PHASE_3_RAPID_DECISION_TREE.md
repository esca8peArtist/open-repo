---
title: "Phase 3 Rapid Decision Tree"
date: 2026-05-31
status: production-ready — staged for June 1 review
scope: Automated Phase 3 launch scope decision upon June 15-20 data arrival; orchestrator execution in <5 minutes
cross-references:
  - PHASE_3_PRODUCTION_ACCELERATION_FRAMEWORK.md (per-scenario production timelines and cost models)
  - PHASE_3_UPLOAD_SEQUENCE_OPTIMIZATION.md (upload sequencing per scenario)
  - PHASE_3_DECISION_GATES_FRAMEWORK.md (sprint gates — executed after this decision tree)
  - phase-3-assets/PHASE_3_EXECUTION_GUIDE.md (original gate condition documentation)
word_count: ~1,300
---

# Phase 3 Rapid Decision Tree

**Prepared**: May 31, 2026  
**Purpose**: Single-pass decision logic that converts June 15–20 Phase 2 data into an unambiguous Phase 3 scope selection in under 5 minutes. No interpretation required. Follow the tree; record the outcome; activate the corresponding execution package.

**Orchestrator runs this on**: June 20, 2026 (or earliest date when all three data inputs are available post-June 15 launch).

**Data sources**:
- Etsy Shop Manager → Traffic tab: conversion rate
- Kit (email platform) → Subscriber list → Tags breakdown: cohort composition %
- Etsy Finances → This month's earnings: cumulative revenue

---

## One-Page Decision Flowchart

```
START HERE — Run June 20, 2026

Step 1: Read Phase 2 conversion rate (Etsy Shop Manager → Traffic)
────────────────────────────────────────────────────────────────────
│
├── Conversion < 1.5%? ──────────────────────────────────────► GO TO [DEFER PATH]
│
└── Conversion ≥ 1.5%? → Continue to Step 2

Step 2: Read forager/herbalist cohort composition (Kit → Tags)
────────────────────────────────────────────────────────────────────
│
├── Cohort < 20% herbalist/practitioner? ────────────────────► GO TO [DEFER PATH]
│
└── Cohort ≥ 20% herbalist/practitioner? → Continue to Step 3

Step 3: Read cumulative revenue (Etsy Finances → This Month)
────────────────────────────────────────────────────────────────────
│
├── Revenue < $200? ─────────────────────────────────────────► GO TO [DEFER PATH]
│
└── Revenue ≥ $200? → All three gates GREEN → Continue to Step 4

Step 4: Determine scope (all three gates passed)
────────────────────────────────────────────────────────────────────
│
├── Conversion > 3% AND cohort > 30% AND revenue > $500?
│   └── YES ─────────────────────────────────────────────────► [SCENARIO C: FULL QUAD]
│
├── Conversion 2.5–3% AND cohort 25–34% AND revenue $400–$699?
│   └── YES ─────────────────────────────────────────────────► [SCENARIO B: WH + RESPIRATORY]
│
└── Conversion 1.5–2.5% AND cohort 20–29% AND revenue $200–$499?
    └── YES ─────────────────────────────────────────────────► [SCENARIO A: WH SOLO]

BOUNDARY CASES (one metric slightly above, one slightly below range):
- Use the lower scenario if any single metric is below its threshold for the higher scenario
- Example: Conversion 2.8% (Scenario C threshold) + cohort 23% (Scenario B range) → Scenario B
- The lower scenario is always the safe default; upgrade only if all three metrics clear the threshold
```

---

## 1. Data Gate Triggers — Exact Thresholds

### Scenario A — Women's Health Solo
| Metric | Minimum | Preferred |
|---|---|---|
| Conversion rate | 1.5% | 1.5–2.5% |
| Herbalist/practitioner cohort | 20% of subscribers | 20–29% |
| Cumulative revenue (days 1–15) | $200 | $200–$499 |

### Scenario B — Women's Health + Respiratory
| Metric | Minimum | Preferred |
|---|---|---|
| Conversion rate | 2.5% | 2.5–3% |
| Herbalist/practitioner cohort | 25% of subscribers | 25–34% |
| Cumulative revenue (days 1–15) | $400 | $400–$699 |

### Scenario C — Full Quad-Bundle
| Metric | Minimum | All three required |
|---|---|---|
| Conversion rate | > 3% | Yes |
| Herbalist/practitioner cohort | > 30% | Yes |
| Cumulative revenue (days 1–15) | > $500 | Yes |

### Defer Path — Phase 3 Deferred
**Trigger**: ANY of the following is true:
- Conversion rate < 1.5%
- Cohort < 20% herbalist/practitioner
- Revenue < $200

**Defer path is not failure**: Track A (Etsy organic) continues. Etsy listing drafts (pre-staged during Phase 2 observation window) remain as drafts indefinitely. Reassess at August 1 checkpoint using 60-day Phase 2 data. The defer path simply means Phase 3 production does not begin until the data warrants the investment.

---

## 2. Per-Outcome Execution Package

### If Scenario A Selected (June 20)

**Immediate actions (June 20–21, ~1 hour)**:
- [ ] Log decision in WORKLOG.md: "June 20 — Scenario A confirmed. Conversion [X]%, cohort [X]%, revenue $[X]."
- [ ] Activate Women's Health authoring sprint — open `PHASE_3_BUNDLE_MASTER_TEMPLATE.md`
- [ ] Confirm photography booking or Wikimedia CC sourcing for Women's Health 5 herbs
- [ ] Review Etsy draft listing for Women's Health — confirm photos placeholder, price TBD
- [ ] No second author outreach needed at Scenario A scope

**Production begins**: June 21
**Upload target**: July 19 (4 weeks from decision)
**Reference**: Scenario A timeline in `PHASE_3_PRODUCTION_ACCELERATION_FRAMEWORK.md` Section 3

---

### If Scenario B Selected (June 20)

**Immediate actions (June 20–21, ~2 hours)**:
- [ ] Log decision in WORKLOG.md: "June 20 — Scenario B confirmed. Conversion [X]%, cohort [X]%, revenue $[X]."
- [ ] Activate Women's Health + Respiratory authoring sprint — Women's Health first
- [ ] Confirm 2-day photography session booking (both bundles in one session)
- [ ] Assess second author: review pre-shortlisted candidates from Phase 2 observation window; activate outreach if 5–6 week timeline is the target
- [ ] Review both Etsy draft listings (Women's Health + Respiratory)
- [ ] Plan cross-bundle landing page timing (publish after both bundles live)

**Production begins**: June 21
**Women's Health upload target**: July 26 (5 weeks from decision)
**Respiratory upload target**: August 2 (6 weeks from decision)
**Reference**: Scenario B timeline in `PHASE_3_PRODUCTION_ACCELERATION_FRAMEWORK.md` Section 3

---

### If Scenario C Selected (June 20)

**Immediate actions (June 20–21, ~3 hours)**:
- [ ] Log decision in WORKLOG.md: "June 20 — Scenario C confirmed. Conversion [X]%, cohort [X]%, revenue $[X]."
- [ ] Activate second author outreach immediately — use pre-shortlisted candidates; Scenario C requires second author to hit July/August window
- [ ] Plan parallel authoring tracks: Author A (Women's Health + Sleep), Author B (Respiratory + Immunity)
- [ ] Book 2 photography sessions or 1 extended 2-day session
- [ ] Confirm Kit full 8-email herbalist funnel is ready for activation (per `phase-3-assets/email-templates/phase-3-broadcast-sequence.md`)
- [ ] Review all four Etsy draft listings and Full Library Bundle draft

**Production begins**: June 21 (both authors, parallel)
**First bundle upload target**: July 26 (Women's Health, 5 weeks)
**Final bundle upload target**: August 16 (Immunity, 8 weeks — with second author)
**Reference**: Scenario C timeline in `PHASE_3_PRODUCTION_ACCELERATION_FRAMEWORK.md` Section 3

---

### If Defer Path Triggered (June 20)

**Immediate actions (June 20, ~30 minutes)**:
- [ ] Log decision in WORKLOG.md: "June 20 — Phase 3 deferred. [State which gate(s) failed and the actual values]."
- [ ] Keep all Etsy drafts in draft status (do not delete — cost is $0 to hold drafts)
- [ ] Confirm Track A Etsy organic continues (no action needed — ongoing)
- [ ] Set August 1 calendar reminder for 60-day Phase 2 data reassessment
- [ ] No production work begins; no photography booking; no second author outreach

**August 1 reassessment**: Run this decision tree again with 60-day Phase 2 data. If gates clear by August 1, production can begin August 1 for a September/October launch (delayed but viable).

---

## 3. Timeline Adjustments Per Scenario

| Scenario | Decision date | First bundle upload | Final bundle upload | Key dependency |
|---|---|---|---|---|
| A (WH Solo) | June 20 | July 19 | July 19 | Solo authoring pace (13–16 hours with templates) |
| B (WH + Respiratory) | June 20 | July 26 | August 2 | Second author decision on June 20–21 |
| C (Full Quad) | June 20 | July 26 | August 16 | Second author confirmed June 21; parallel tracks |
| Defer | June 20 | Earliest: August 15 | N/A | August 1 reassessment gate |

---

## 4. Rollback Scenario

If Phase 2 underperforms (Defer path selected June 20):

**Short rollback**: Phase 2 Track A organic continues. Phase 3 all-draft status maintained. No additional investment. Reassess August 1.

**Extended rollback (August 1 data also misses gates)**: Phase 3 deferred to 2027 planning cycle. Phase 3 draft documents remain in `projects/seedwarden/` as a complete production-ready package for future activation. Track B influencer audience continues to build organically. No sunk cost except the pre-staging time invested in the Phase 2 observation window.

**The rollback is not catastrophic**: Phase 3 pre-staging costs (Sections 1–6 of this framework, all five files) represent approximately 14 hours of preparation work. If Phase 3 is deferred entirely, that work is recoverable in full when Phase 3 is reactivated — every document remains current through the 2026 growing season.

---

*Run this tree on June 20. Record the outcome. Open the corresponding execution package. Proceed.*
