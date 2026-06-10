---
title: "Phase 3 Launch Decision Automation Matrix"
subtitle: "GO / CAUTION / NO-GO × 4 Dimensions — Automatic Escalation Triggers"
date: 2026-06-10
version: 1.0
status: active — valid June 17 through June 22 launch
sprint-window: June 22 – August 3, 2026 (contractor) | June 22 – September 24, 2026 (solo)
contractor-gate: June 17, 2026 EOD
cross-references:
  - PHASE_3_COMPREHENSIVE_RISK_REGISTER.md (8 risks, P×I scoring)
  - PHASE_3_CONTINGENCY_EXECUTION_PLAYBOOKS.md (5 scenario playbooks)
  - PHASE_3_RISK_DAILY_MONITORING_CHECKLIST.md (June 18–22 countdown)
  - CONTRACTOR_SOURCING_CHANNEL_VALIDATION.md (Upwork primary; channels ranked)
  - PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (9-week solo architecture)
tags: [seedwarden, phase-3, decision-matrix, automation, go-no-go, contingency]
---

# Phase 3 Launch Decision Automation Matrix
## GO / CAUTION / NO-GO — 4 Dimensions, 16-Cell Grid

**Purpose**: Eliminate real-time decision burden June 17–22. Every launch-eve situation maps to one cell. The cell specifies the decision — no user deliberation required.

**How to use**: On any day June 17–22, score each of the four dimensions independently. Find the intersection cell. Execute the stated action.

**Decision authority**: This matrix is pre-authorized. No confirmation required to execute a GO, CAUTION, or NO-GO action. Log every decision in WORKLOG.md within one hour.

---

## The Four Dimensions

| Dimension | What It Measures | Key Gate Date |
|-----------|-----------------|---------------|
| **D1 — Contractor Status** | Is a qualified contractor confirmed for the sprint? | June 17 EOD |
| **D2 — Sourcing Readiness** | Are CC images pre-staged for all 6 bundles? | June 19 EOD |
| **D3 — Content Progress** | Are outlines complete and time estimates credible? | June 21 EOD |
| **D4 — Platform Availability** | Is Kit (email) + Etsy operational for June 22 launch? | June 21 EOD |

---

## Dimension 1: Contractor Status

Evaluate as of June 17 EOD.

| Score | Condition | Label |
|-------|-----------|-------|
| **GO** | Contract signed, deposit paid, contractor has confirmed sprint start June 22 in writing | Contractor GO |
| **CAUTION** | At least 1 candidate at Tier B or above, rate within $1,350 ceiling, contract pending — offer made, not yet signed | Contractor CAUTION |
| **NO-GO** | Zero candidates have completed screening; or all candidates above $1,350 after scope negotiation; or June 12 Upwork gate produced fewer than 3 proposals and backup channels did not surface alternatives | Contractor NO-GO — activate solo fallback |

**Threshold definitions**:
- Tier A: Portfolio confirmed publication-quality, herbalist background confirmed, rate within ceiling, availability June 22–September 24 confirmed
- Tier B: Portfolio confirms publication-quality, botanical knowledge shown in portfolio, rate within ceiling, availability confirmed
- Tier C or below: Portfolio adequate, no botanical knowledge signal — do NOT hire; activate solo

**Numeric contractor gate**: If Upwork produces zero proposals in 48 hours of posting (by June 12), the posting is misconfigured or the budget is below market. Immediately: (1) boost posting via Upwork promoted jobs, (2) activate Reddit and Instagram backup channels per PHASE_3_CONTINGENCY_EXECUTION_PLAYBOOKS.md Playbook 1. If still fewer than 3 qualified proposals by June 14: Contractor NO-GO is near-certain. Begin solo fallback prep now.

**If 1–2 proposals by June 12**: Assess tier. If both are Tier C or lower after screening, activate solo fallback June 12 — do not wait for June 17. The timeline has no slack for a second screening round.

**Auto-escalation at NO-GO**: Log in WORKLOG.md. Activate solo fallback architecture Section 6 checklist immediately. All Phase 3 content is user-written. Phase 4 start adjusts to October 1.

---

## Dimension 2: Sourcing Readiness

Evaluate as of June 19 EOD. Repeat check June 21 EOD.

| Score | Condition | Label |
|-------|-----------|-------|
| **GO** | PHOTO_ATTRIBUTION_LOG.md confirms at least 1 CC-licensed image per bundle (6 bundles = 6 images minimum), all with source URL + license + attribution text | Sourcing GO |
| **CAUTION** | 4–5 of 6 bundles confirmed; 1–2 bundles have 0 images logged | Sourcing CAUTION — run targeted Wikimedia sourcing sprint (30 min per missing bundle) |
| **NO-GO** | 3 or more bundles have 0 images confirmed by June 21 EOD | Sourcing NO-GO — activate image bottleneck playbook (Playbook 5) |

**Botanical garden contact rule**: If botanical garden outreach was not confirmed responsive by June 15, treat sourcing as dependent on Wikimedia Commons and iNaturalist only. Do not wait for botanical garden response after June 15. CC-licensed Wikimedia images cover all 14 sprint species.

**iNaturalist fallback**: All observations marked CC BY or CC BY-SA are usable. Verify license on the individual observation page (not the species page). Record photographer, observation URL, and license code in PHOTO_ATTRIBUTION_LOG.md.

**Pre-validated iNaturalist search procedure**:
1. Go to inaturalist.org/observations
2. Search species name, filter Research Grade only
3. Click individual observation; check License field on right sidebar
4. Acceptable licenses: CC0, CC BY, CC BY-SA
5. Not acceptable: CC BY-NC (non-commercial restriction), CC BY-ND, All Rights Reserved

**Stock photo budget trigger (pre-authorized)**: If Wikimedia + iNaturalist produce fewer than 1 confirmed image for any bundle by June 19 EOD, allocate up to $75 per affected bundle for licensed stock botanical photography. Acceptable sources: Shutterstock, Adobe Stock, Alamy. This is pre-authorized — no separate approval required. Log purchase receipt URL in WORKLOG.md.

**Maximum exposure**: 6 bundles × $75 = $450 if all bundles fail CC sourcing. This is the worst-case sourcing budget.

---

## Dimension 3: Content Progress

Evaluate as of June 21 EOD.

Content outlines are the measurable proxy for content progress pre-sprint. An outline complete means the structural scaffold is in place and the writing sprint can start at pace on June 22.

| Bundle | Time Budget (contractor model) | Time Budget (solo model) | Outline Required by June 21 |
|--------|-------------------------------|-------------------------|------------------------------|
| Women's Health | 14–16 hrs | 14–16 hrs (user-written in all models) | Yes — zero float |
| Respiratory | 12–14 hrs | 12–14 hrs | Yes |
| Immunity | 13–15 hrs | 13–15 hrs | Yes |
| Sleep | 11–13 hrs | 11–13 hrs | Yes |
| Digestive | 12–14 hrs | 12–14 hrs | Yes |
| Integrative | 10–12 hrs | 10–12 hrs | Yes |

| Score | Condition | Label |
|-------|-----------|-------|
| **GO** | All 6 bundle outlines complete; section word targets specified per bundle; contraindication reference files open or bookmarked | Content GO |
| **CAUTION** | 4–5 outlines complete; 1–2 bundles have partial outlines (sections listed, word targets not specified) | Content CAUTION — complete missing outlines June 21 before EOD; do not carry this into June 22 |
| **NO-GO** | 3 or more bundles have no outline; OR the Women's Health outline is incomplete (zero-float bundle) | Content NO-GO — delay sprint start by 24 hours; complete all outlines on June 22 before writing begins |

**Content delay cascade rule**: If actual writing time for any bundle exceeds its budget by more than 10% after Day 5 of that bundle's sprint window:
1. First action: Reduce secondary sections (regional variants, historical context, extended preparation methods). Preserve contraindications, herb profiles, and clinical evidence sections intact.
2. Second action (if first action does not recover pace): Defer the next scheduled bundle by 7 days. Log in WORKLOG.md. Adjust upload schedule. This is a scope correction, not a sprint failure.
3. Third action (contractor model only): Request contractor sprint on the deferred bundle. Use Playbook 3 email template.

**10% overage thresholds by bundle**:
- Women's Health (15 hrs budget): trigger at 16.5 hrs
- Respiratory (13 hrs budget): trigger at 14.3 hrs
- Immunity (14 hrs budget): trigger at 15.4 hrs
- Sleep (12 hrs budget): trigger at 13.2 hrs
- Digestive (13 hrs budget): trigger at 14.3 hrs
- Integrative (11 hrs budget): trigger at 12.1 hrs

---

## Dimension 4: Platform Availability

Evaluate as of June 21 EOD.

| Score | Condition | Label |
|-------|-----------|-------|
| **GO** | Kit (email): login confirmed, landing page live, post-purchase email sequence active. Etsy: store operational, test listing successfully created and deleted. | Platform GO |
| **CAUTION** | One platform has a non-critical issue (e.g., Kit automation sequence not confirmed active, but login works and landing page is live). | Platform CAUTION — resolve before June 22 9am ET |
| **NO-GO** | Kit is inaccessible: login failure with no response from Kit support within 24 hours. OR Etsy store is suspended or blocked from listing. | Platform NO-GO — activate platform fallback |

**Kit NO-GO protocol** (pre-authorized, execute without approval):
1. Email-only launch via Gmail: BCC all current subscribers. Subject: "Seedwarden is live — Women's Health Bundle now available." Link directly to Etsy listing.
2. Migrate subscriber list to Mailchimp Free within 48 hours (up to 500 contacts). Reconstruct 3-email welcome sequence. Import subscriber CSV from Kit export.
3. If Etsy is also unavailable: create Gumroad account and upload all 6 bundle PDFs as separate products priced identically to Etsy listings. Gumroad charges 10% fee; no approval delay.

**Etsy NO-GO protocol** (pre-authorized):
1. Create Gumroad account if not already active. Upload all 6 bundle PDFs. Price identically.
2. Notify email list of temporary purchase location.
3. Open Etsy support ticket with suspension documentation. Etsy reinstatement: typically 2–7 business days.
4. Content sprint continues on schedule regardless of platform status.

---

## 16-Cell Decision Matrix

The matrix covers D1 × D2 as the two highest-stakes pre-launch dimensions. D3 and D4 are applied as modifiers.

### Primary Grid: Contractor Status (D1) × Sourcing Readiness (D2)

|  | D2: Sourcing GO | D2: Sourcing CAUTION | D2: Sourcing NO-GO |
|--|-----------------|---------------------|-------------------|
| **D1: Contractor GO** | Cell 1-A: FULL GO | Cell 1-B: CAUTION | Cell 1-C: CAUTION |
| **D1: Contractor CAUTION** | Cell 2-A: CAUTION | Cell 2-B: CAUTION | Cell 2-C: NO-GO (sourcing) |
| **D1: Contractor NO-GO** | Cell 3-A: GO (solo) | Cell 3-B: CAUTION (solo) | Cell 3-C: NO-GO (escalate) |

### Cell Definitions

**Cell 1-A: FULL GO**
Both contractor and sourcing are confirmed. Apply D3 + D4 checks. If both pass: launch June 22 as planned. No escalation required.

**Cell 1-B: CAUTION — Sourcing gap with contractor confirmed**
Contractor confirmed; 1–2 bundles missing images. Action: run Wikimedia sourcing sprint on June 19–20 for missing bundles (30 min each). If not resolved by June 21 EOD: allocate stock photo budget ($75 per bundle). Launch proceeds on schedule. Log sourcing actions in WORKLOG.md.

**Cell 1-C: CAUTION — Sourcing bottleneck with contractor confirmed**
3 or more bundles missing images. Action: run full sourcing sprint June 19–20 (2–3 hours). Activate stock photo budget for any bundle not resolved by Wikimedia or iNaturalist. Do not delay launch. Images can be added to listings post-launch via Etsy listing update without resetting review count or listing age.

**Cell 2-A: CAUTION — Contractor pending, sourcing ready**
Offer made, contract not yet signed. Sourcing confirmed. Action: pursue contract signature before June 17 EOD. If not signed by June 17 EOD: activate solo fallback immediately (Cell 3-A rules apply from that point). Do not run parallel planning tracks after June 17.

**Cell 2-B: CAUTION — Contractor pending, sourcing partial**
Both dimensions have open items. This is the maximum viable CAUTION state — two unresolved dimensions simultaneously. Action: prioritize contract signature first (time-critical). Run sourcing sprint simultaneously. If either remains unresolved at June 17 EOD: contractor reverts to solo fallback; sourcing activates stock photo budget. Launch proceeds June 22 in solo model with sourcing complete.

**Cell 2-C: NO-GO (sourcing) — Contractor pending, sourcing failed**
3 or more bundles have no images and contractor is not yet signed. The sourcing NO-GO triggers stock photo budget activation regardless of contractor status. Action: (1) Activate stock photo budget for all 6 bundles (up to $450). (2) Assume solo fallback will activate June 17 EOD unless contract is signed that day. (3) Log both actions in WORKLOG.md.

**Cell 3-A: GO (solo) — Solo fallback active, sourcing ready**
Contractor search closed June 17. Solo sprint activates June 22. Sourcing is confirmed. This is the clean solo launch state. Action: confirm solo fallback architecture Section 6 checklist is complete. Log: "Solo sprint confirmed — June 22 start. All sourcing confirmed." Launch on schedule.

**Cell 3-B: CAUTION (solo) — Solo fallback active, sourcing partial**
Solo sprint active; 1–2 bundles missing images. Action: run sourcing sprint June 19–20. Allocate stock photo budget for any gap by June 21. Solo sprint proceeds June 22. Sourcing gap does not delay launch.

**Cell 3-C: NO-GO (escalate) — Solo fallback active, sourcing failed**
Both contractor search and image sourcing have failed simultaneously. This is the only state requiring user escalation. Action: (1) Activate full stock photo budget ($450). (2) Delay sprint start by 48 hours to June 24. (3) Send Escalation Email E1 (see PHASE_3_RISK_DAILY_MONITORING_CHECKLIST.md). (4) Complete sourcing sprint June 22–23. Solo sprint begins June 24. Upload dates cascade by 2 days across all bundles.

---

### D3 Modifier (Content Progress)

Apply after primary grid cell is identified.

| D3 Score | Modifier |
|----------|----------|
| Content GO | No change to primary cell decision |
| Content CAUTION | Append "complete missing outlines before June 22 writing begins" to any GO or CAUTION cell |
| Content NO-GO | Downgrade any GO cell to CAUTION; downgrade any CAUTION cell to NO-GO with 24-hour delay; Cell 3-C NO-GO becomes 48-hour delay |

---

### D4 Modifier (Platform Availability)

Apply after D3 modifier is applied.

| D4 Score | Modifier |
|----------|----------|
| Platform GO | No change |
| Platform CAUTION | Append "resolve platform issue before June 22 9am ET" to any cell; does not delay launch if resolved in time |
| Platform NO-GO | Does not delay content sprint. Activates email-only + Gumroad fallback for sales channel immediately. Content production continues on schedule. |

---

## Auto-Escalation Triggers Summary

| Trigger | Condition | Threshold | Auto-Action | Playbook |
|---------|-----------|-----------|-------------|----------|
| T1 — Contractor zero-response | June 12 EOD | 0 Upwork proposals OR 0 Tier A replies | Activate backup channels: Reddit, Instagram, ASBA | Playbook 1, Step 2 |
| T2 — Contractor Tier C only | June 12–14 | 1–2 proposals, none pass Tier B screen | Activate solo fallback immediately; close contractor search | Playbook 1, Step 3 |
| T3 — Contractor gate fail | June 17 EOD | No contract signed | Activate solo fallback; stop all contractor outreach | Playbook 1, Step 4 |
| T4 — Sourcing gap | June 19 EOD | Any bundle with 0 CC images | Source Wikimedia (30 min per bundle); stock photo budget if gap persists to June 21 | Playbook 5 |
| T5 — Sourcing bottleneck | June 21 EOD | 3 or more bundles with 0 images | Activate full $450 stock photo budget; delay launch 48 hours | Playbook 5 |
| T6 — Content pace gate fail | June 24 EOD | Women's Health below 2,500 words | Activate Option C scope reduction; reduce secondary sections | Playbook 3 |
| T7 — Bundle time overrun | Any bundle Day 5 | Actual time exceeds budget by 10% | Reduce secondary sections; defer next bundle 7 days if unresolved | Playbook 3 |
| T8 — Contractor mid-sprint silence | Any sprint day | 3 consecutive days no communication | Assume dropout; activate mid-sprint recovery within 48 hours | Playbook 1 |
| T9 — Platform outage | June 22 | Kit or Etsy inaccessible | Email-only launch + Gumroad fallback; content sprint unaffected | Playbook 4 |

---

## Decision Log Format

Every matrix cell decision must be logged in WORKLOG.md within 1 hour of the trigger date.

```
[DECISION MATRIX] [Date] — D1: [GO/CAUTION/NO-GO] | D2: [GO/CAUTION/NO-GO] | D3: [GO/CAUTION/NO-GO] | D4: [GO/CAUTION/NO-GO]
Cell: [e.g., 3-A + D3 GO + D4 GO]
Decision: [e.g., FULL GO — solo model, sourcing confirmed]
Action taken: [e.g., Solo fallback checklist completed. Sprint start confirmed June 22.]
Next check: [date]
```

---

*Prepared: June 10, 2026. Foundation references: PHASE_3_COMPREHENSIVE_RISK_REGISTER.md (risks 1–8, P×I scoring), CONTRACTOR_SOURCING_CHANNEL_VALIDATION.md (Upwork primary, June 17 hard deadline), PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md, CONTINGENCY_SOURCING_PLAYBOOK.md (4 scenarios A–D), TIER_A_CANDIDATE_PRE_SCREEN.md.*
