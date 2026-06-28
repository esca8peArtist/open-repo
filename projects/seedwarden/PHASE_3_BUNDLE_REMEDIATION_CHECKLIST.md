---
title: "Phase 3 Bundle Remediation Checklist — Actionable Items Before Week 5-6 Handoff"
date: 2026-06-28
version: 1.0
item: Exploration Queue Item 13
status: active
cross-references:
  - PHASE_3_BUNDLE_CONTENT_GAP_LIST.md (source of all items below)
  - PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md (quality gates)
  - PHASE_3_LAUNCH_CALENDAR.md (deadline dates)
---

# Phase 3 Bundle Remediation Checklist

**Scope**: All YELLOW items from PHASE_3_BUNDLE_CONTENT_GAP_LIST.md.
**Priority ranking**: Items 1-3 are blocking (must resolve before the relevant bundle upload). Items 4-9 are non-blocking but must resolve before Week 5 final handoff (July 27). No RED items were identified.

---

## Priority 1 — BLOCKING (Must Resolve Before Upload Date)

### Item 1: Red Clover Constituent Mislabeling — Women's Health
- **Bundle**: Women's Health
- **Upload date**: June 29, 2026
- **Status**: ✅ **RESOLVED (Session 4469, 2026-06-28 20:16 UTC)**
- **Resolution**: Tracker file (Q3_MEDICINAL_BUNDLES_COMPLETION_TRACKER.md) had incorrect constituent label; bundle draft was already correct. Updated tracker lines 52 & 98: (1) Changed "berberine-interaction caution" to "correct isoflavone constituents (formononetin, biochanin A, daidzein, genistein)" (2) Fixed QA checklist to reference isoflavone-CYP1A2/CYP2C9 interactions (not berberine). Women's Health bundle draft verified correct and production-ready for June 29 upload. Commit: 9fd29d5b.

---

### Item 2: Vitex Contraindication Completeness — Women's Health
- **Bundle**: Women's Health
- **Upload date**: June 29, 2026
- **Status**: ✅ **RESOLVED (Session 4469, 2026-06-28 20:25 UTC)**
- **Resolution**: Women's Health bundle Vitex section was missing explicit MAOI antidepressant warning. Updated Safety Notes section to include: (1) "Do not combine with MAOI antidepressants without medical supervision — Vitex's dopaminergic activity may potentiate MAOI effects" (2) Expanded oral contraceptive caution to clarify prescriber communication requirement. Bundle now meets remediation checklist quality gate for June 29 upload. Commit: 3b3d7470.

---

### Item 3: Ashwagandha Thyroid Mechanism Depth — Immunity
- **Bundle**: Immunity Support
- **Upload date**: July 20, 2026
- **Status**: ✅ **RESOLVED (Session 4469, 2026-06-28 20:32 UTC)**
- **Resolution**: Immunity bundle Ashwagandha section was missing explicit withanolide mechanism on thyroid hormone axis. Updated: (1) Main section: Added "The withanolide constituents in ashwagandha root act on the thyroid hormone axis, modulating TSH and thyroid hormone production" (2) Safety Notes: Specified "withanolide constituents directly modulate the thyroid hormone axis" with clinical monitoring protocol (TSH, free T3, free T4 at baseline + 4-6 weeks). Bundle now meets remediation checklist quality gate for July 18 upload + July 14 contractor payment milestone 2 gate. Commit: 3b3d7470.

---

## Priority 2 — NON-BLOCKING (Must Resolve Before Week 5 Final Handoff, July 27)

### Item 4: Valerian Double-Mention of Sedative Warning — Sleep
- **Bundle**: Sleep and Nervines
- **Upload date**: July 27 (Sleep tracker date) / July 13 (Launch Calendar date — discrepancy noted below)
- **Gap**: PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md (Part 5, Valerian section) states the sedative drug interaction warning "appears twice: in the contraindications section and in the preparation methods section when tincture preparation is described." The tracker confirms the contraindications section has the warning but does not confirm the second appearance in the preparation methods section. The outline treats this double-mention as mandatory.
- **Owner**: User (verification) or writer (if contractor-written)
- **Action**: Open Sleep bundle draft. Locate the Valerian tincture preparation description. Confirm a sedative warning note appears adjacent to the tincture dose instructions (e.g., "Do not combine with benzodiazepines, prescription sedatives, or alcohol"). If absent, add a one-sentence warning before final handoff.
- **Deadline**: Before July 26 per launch calendar (all writer revision rounds complete by July 26)
- **Evidence**: Sleep bundle draft — search for "tincture" in Valerian section. Confirm a drug interaction warning appears within that subsection, separate from the contraindications table.

---

### Item 5: Cross-Reference Sentence Confirmation — Immunity (Echinacea and Elderberry condensed sections)
- **Bundle**: Immunity Support
- **Gap**: PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md specifies exact cross-reference sentence placement for condensed species sections: the sentence must appear in the condensed section itself, not in the introduction or sources. The tracker does not explicitly confirm these sentences are placed. Without them, buyers who purchase both Immunity and Respiratory see repetitive content with no explanatory link.
- **Owner**: User (review during draft acceptance) or writer (instruction in Week 2 check-in)
- **Action**: When reviewing the Immunity first draft (due July 8), confirm: (1) Echinacea condensed section contains the sentence "For the full cultivation comparison of E. purpurea and E. angustifolia, including the conservation sidebar for E. angustifolia, see the Respiratory Health Herbs Guide." (2) Elderberry condensed section contains the sentence directing readers to the Respiratory bundle for full cultivation and elderflower content. If absent, add to revision notes.
- **Deadline**: Before July 18 Immunity final draft
- **Evidence**: Immunity draft — search for "Respiratory Health" in both Echinacea and Elderberry sections. Should return at least one cross-reference sentence each.

---

### Item 6: Lemon Balm Cross-Reference Placement — Digestive
- **Bundle**: Digestive Support
- **Upload date**: August 3, 2026
- **Gap**: PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md Cross-Sell Placement Rules specify cross-references appear "in exactly two places per bundle: in the condensed species section and in the Practitioner Context section." The Digestive Lemon Balm cross-reference to the Sleep bundle must not appear in the introduction or contraindications. Tracker confirms Lemon Balm is complete but does not confirm cross-reference placement.
- **Owner**: User (review during draft acceptance)
- **Action**: When reviewing the Digestive bundle draft (due July 21): locate the Lemon Balm section and confirm the cross-reference to the Sleep bundle is placed within the condensed species section body text, not in the introduction or contraindications subsection. If in the wrong location, move to the correct position.
- **Deadline**: Before July 24 Digestive final draft
- **Evidence**: Digestive draft — search for "Sleep" in Lemon Balm section. Confirm it appears in the body text of the species section, not in intro paragraph or contraindications.

---

### Item 7: Echinacea Root Harvest Timeline Standardization — Respiratory
- **Bundle**: Respiratory Health
- **Upload date**: July 6, 2026
- **Gap**: Minor inconsistency: PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md specifies 3-year harvest for E. purpurea root and 5-year for E. angustifolia root. Q3_MEDICINAL_BUNDLES_COMPLETION_TRACKER.md notes "year 2-3 / year 4-5." PHASE_3_MEDICINAL_HERBS_BUNDLE_CONTENT.md (the master content file) states "fall of year 3 or 4" for E. purpurea and implies longer for angustifolia. The Immunity bundle outline specifies 3 years (purpurea) and 5 years (angustifolia). Inconsistent timeline language across documents is a practitioner credibility risk.
- **Owner**: User
- **Action**: Before July 6 Respiratory upload, verify the Respiratory bundle draft specifies "3 years minimum for E. purpurea root" and "5 years for E. angustifolia root" (or range with minimum stated). Align with the Immunity bundle text so the same species has the same timeline in both bundles. The conservative (longer) figure should be preferred.
- **Deadline**: Before July 6 Respiratory upload
- **Evidence**: Compare Respiratory and Immunity bundle Echinacea sections. Both should use the same harvest timeline range for each species.

---

### Item 8: Upload Date Discrepancy — Sleep Bundle
- **Bundle**: Sleep and Nervines
- **Gap**: PHASE_3_LAUNCH_CALENDAR.md lists Sleep bundle upload as July 13, 2026. Q3_MEDICINAL_BUNDLES_COMPLETION_TRACKER.md lists upload target as July 27, 2026. These are two different dates in two authoritative documents for the same bundle. The Launch Calendar is labeled as the authoritative sprint calendar source per its own header. If the July 13 date is correct, the Sleep bundle is a zero-float item at the Sprint Close milestone, not a Week 4 bundle.
- **Owner**: User (decision required)
- **Action**: Confirm which upload date is operative for Sleep: July 13 (Launch Calendar sprint close) or July 27 (Tracker estimate). Update the incorrect document. The Practitioner tier launch on July 15 requires at least 3 bundles live — if Sleep is July 27, the Practitioner tier may need to launch on only Women's Health + Respiratory (only 2 bundles), which is below the stated 3-bundle minimum. This dependency makes the Sleep upload date critical.
- **Deadline**: Resolve by July 1 (before Week 2 begins)
- **Evidence**: PHASE_3_LAUNCH_CALENDAR.md line: "Jul 13 — UPLOAD Sleep and Nervines bundle 9-10am ET — Sprint close." Tracker line: "Sleep & Nervines... Upload Target: July 27." These are in direct conflict.

---

### Item 9: Practitioner Tier FTC Framing Reminder — Practitioner Tier
- **Bundle**: Practitioner Tier (pricing/license construct)
- **Gap**: Communication templates (Template 1 and Template 5 in PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md) do not include an FTC framing reminder specific to Practitioner-tier marketing. If the user writes Practitioner-tier listing copy or sends marketing to clinical buyers that includes language about patient education efficacy, this copy needs to pass the same FTC structure-function review as bundle content.
- **Owner**: Claude (add note to templates) or User (apply when writing Practitioner marketing copy)
- **Action**: Before writing any Practitioner-tier Etsy listing description or email marketing copy, apply the FTC Quick Reference: no disease-treatment claims; all clinical utility language framed as "educational resource for [application area]" not "treats [condition]." Add a comment note to the Practitioner tier Etsy listing draft referencing the FTC block language in PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md Block A.
- **Deadline**: Before July 15 Practitioner tier launch
- **Evidence**: Practitioner tier Etsy draft listing text — no sentences structured as "helps patients [therapeutic outcome]." All claims use "educational resource for healthcare practitioners" framing.

---

## Remediation Summary

| # | Bundle | Category | Deadline | Owner | Blocking? |
|---|--------|----------|----------|-------|-----------|
| 1 | Women's Health | Content / Species accuracy | June 29 | User + Claude | YES — upload day |
| 2 | Women's Health | Compliance / Contraindications | June 29 | User | YES — upload day |
| 3 | Immunity | Compliance / Mechanism depth | July 18 | User (milestone gate) | YES — milestone payment |
| 4 | Sleep | Content / Double-mention warning | July 26 | User/Writer | No |
| 5 | Immunity | Content / Cross-reference placement | July 18 | User/Writer | No |
| 6 | Digestive | Content / Cross-reference placement | July 24 | User | No |
| 7 | Respiratory | Content / Timeline consistency | July 6 | User | No |
| 8 | Sleep | Scope / Date discrepancy | July 1 | User (decision) | No — but cascades Practitioner tier |
| 9 | Practitioner | Compliance / FTC framing | July 15 | User | No |

**Top 3 remediation priorities**:
1. Item 1 — Red Clover berberine mislabeling (correctness risk, upload June 29)
2. Item 8 — Sleep upload date discrepancy (cascades to Practitioner tier launch eligibility)
3. Item 3 — Ashwagandha thyroid mechanism depth (dashboard quality gate, controls milestone payment)

---

*Prepared: June 28, 2026. Exploration Queue Item 13. Source: PHASE_3_BUNDLE_CONTENT_GAP_LIST.md. All items are YELLOW (no RED items). Resolve items 1-3 before their respective upload or payment dates; items 4-9 before Week 5 handoff (July 27).*
