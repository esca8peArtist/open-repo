---
title: "Wave 2 Execution Timeline with Domain 39 Response Triggers"
created: "2026-06-01"
purpose: "Master calendar for Wave 2 (Domains 39, 38, 40) with explicit dependency points where Domain 39 response data adjusts sequencing"
domains: [39, 38, 40]
external_triggers:
  - Trump v. Barbara ruling (late June – early July, domain 58 — independent track)
  - EU AI Act Article 50 enforcement (August 2, 2026 — Domain 38 anchor)
  - November 3, 2026 (US midterm elections — Domain 40 absolute deadline)
hard_constraints:
  - Domain 39 send: June 1 (complete)
  - Domain 38 Tier A send: June 15 (adjustable per PHASE_2_ACTIVATION_DECISION_TREE.md)
  - Domain 40 Tier A send: July 15 default (adjustable based on Phase 2 path)
cross_references:
  - PHASE_2_ACTIVATION_DECISION_TREE.md
  - DOMAIN_39_RESPONSE_MONITORING_PLAN.md
  - DOMAIN_38_40_CONTINGENCY_DECISION_TREE.md
  - DOMAIN_58_RULING_TRIGGER_READINESS.md
status: "execution-ready — default timeline active; trigger adjustments noted throughout"
---

# Wave 2 Execution Timeline with Domain 39 Response Triggers
## June 1 – November 3, 2026 Master Calendar

*This document is the master calendar for Wave 2. It builds on DOMAIN_38_40_EXECUTION_TIMELINE.md (the predecessor) by adding explicit Domain 39 response trigger points that modify Domain 38 and Domain 40 sequencing. Read this document alongside PHASE_2_ACTIVATION_DECISION_TREE.md — the decision tree specifies what to do at each gate; this document specifies when to do it and what changes downstream.*

*Default timeline assumes the MODERATE Phase 2 path (2 Domain 39 responses by T+14). STRONG path accelerations and WEAK path delays are marked with trigger annotations throughout.*

---

## Architecture Overview

Wave 2 runs three parallel tracks plus one ruling-dependent track:

**Track A — Domain 38 (AI Regulatory Capture)**
- Hard deadline: EU AI Act Article 50 enforcement, August 2, 2026
- Tier A distribution: June 15–20 (default); June 8–12 if STRONG path triggered
- Track A is Wave 2's primary track June 2 – July 14

**Track B — Domain 40 (Surveillance Capitalism / Electoral Manipulation)**
- Hard deadline: November 3, 2026 midterm elections
- Tier A distribution: July 15–20 (default); June 15 if STRONG path + D40 Gist ready; August 1 if WEAK path
- Track B prepares June 2 – July 14, then executes July 15+

**Track C — Domain 39 (ongoing)**
- Send complete June 1
- Tier 2 outreach: June 5–12 (MODERATE/STRONG) or June 15–July 15 (WEAK path)
- Response tracking continues through T+45 (July 16)

**Track D — Domain 58 (Tribal Sovereignty — independent)**
- Ruling-triggered; independent of Tracks A/B/C
- Pre-staging complete; monitoring begins June 15
- Activates same day Trump v. Barbara ruling issues (late June – early July)

---

## Phase 1: Post-Send Activation Window
### June 2–3, 2026

**Purpose**: Activate Wave 2 planning based on Domain 39 send status (not outcome). Confirm all infrastructure is in place.

| Day/Time (UTC) | Action | Domain | Trigger |
|---|---|---|---|
| June 2, 09:00 | Log Domain 39 Day 1 status: any responses? any bounces? | D39 | Always |
| June 2, 09:30 | Run Wave 2 pre-tree checklist (PHASE_2_ACTIVATION_DECISION_TREE.md) | All | Always |
| June 2, 10:00 | Confirm D38 source ready: `domain-38-ai-regulatory-capture-governance.md` | D38 | Always |
| June 2, 10:15 | Confirm D40 source ready: `domain-40-surveillance-capitalism-electoral-manipulation.md` | D40 | Always |
| June 2, 10:30 | Verify D58 Gist creation status (DOMAIN_58_GIST_URL.md) | D58 | Always |
| June 2, 11:00 | Begin D38 content review: read current draft, note any updates needed | D38 | Always |
| June 3 | D38 content refinement: update any time-sensitive sections | D38 | Always |
| June 3 | Begin D40 content review | D40 | Always |

No emails go out June 2–3. This is planning and infrastructure confirmation only.

---

## Phase 2: D39 T+3 Signal + D38 Content Preparation
### June 4–7, 2026

| Day/Time (UTC) | Action | Domain | Trigger |
|---|---|---|---|
| June 4, 09:00 | **T+3 CHECKPOINT**: Count D39 responses; check bounces | D39 | Always |
| June 4, 09:30 | Log T+3 results in RESPONSE_MONITORING_DASHBOARD_TEMPLATE.md | D39 | Always |
| June 4 | If bounce: activate alternative contact immediately (see PHASE_2_ACTIVATION_DECISION_TREE.md Branch 1D) | D39 | Bounce only |
| June 4–7 | **D38 content preparation**: finalize Gist assembly; review all contact-specific hooks | D38 | Always |
| June 4–7 | **D38 Gist creation**: follow DOMAIN_38_GIST_CREATION_STEPS.md | D38 | Always |
| June 5–7 | **D39 Tier 2 sends** (if MODERATE or STRONG path is already clear from T+3): CBPP, NDRN, DRA, AMCHP, SisterSong | D39 | MODERATE/STRONG early signal |
| June 4–7 | **D40 content review**: begin reading and note any June 2026 updates needed | D40 | Always |

**Trigger annotations**:
- If T+3 shows 0 responses: no change to D38 preparation; continue as planned
- If T+3 shows 2+ responses: begin Domain 39 Tier 2 outreach immediately (June 5–7 sends)
- If T+3 shows 5 responses (exceptional): Begin D40 Gist creation June 4 (moved up from June 21)

---

## Phase 3: T+7 Signal + D38 Tier A Launch Preparation
### June 8–14, 2026

| Day/Time (UTC) | Action | Domain | Trigger |
|---|---|---|---|
| June 8, 09:00 | **T+7 CHECKPOINT**: Count D39 cumulative responses | D39 | Always |
| June 8, 09:30 | Log T+7 results; assess Phase 2 path early signal | D39 | Always |
| June 8 | If T+7 = 0: expand D38 Tier A send list with 5 Tier B contacts; prepare alternative subject lines | D38 | Branch 2A only |
| June 8 | If T+7 = 5: begin D40 Gist creation (moved up from June 21) | D40 | Branch 2D only |
| June 8–11 | Finalize 15 D38 Tier A email drafts (one per contact, personalization complete) | D38 | Always |
| June 8–11 | Confirm D38 Gist is live and accessible | D38 | Always |
| June 9–12 | Begin Domain 58 daily monitoring: check SCOTUSblog and SCOTUS opinions page | D58 | Always (start June 15 minimum; earlier is fine) |
| June 11–14 | Final D38 pre-send review: all templates, placeholders, Gist URL confirmed | D38 | Always |
| June 14 | Final check: D38 Tier A send list confirmed (15 contacts or 20 if Tier B expansion triggered) | D38 | Always |

**Trigger annotations**:
- If T+7 Branch 2A (0 responses): D38 Tier A list expands to include Tier B contacts; alternative subject lines finalized by June 11
- If T+7 Branch 2D (5 responses): D40 Gist creation begins June 8; assess whether D40 can send simultaneously with D38 on June 15
- Default (T+7 1–4 responses): No D38 adjustments; proceed to June 15 as planned

---

## Phase 4: T+14 Primary Gate + D38 Tier A Launch
### June 15, 2026 — CRITICAL DATE

**Two major events occur June 15**:
1. T+14 Domain 39 response assessment (09:00 UTC)
2. Domain 38 Tier A first send (09:30+ UTC)

**Assessment before send**: Do not begin D38 sends until T+14 assessment is complete.

| Time (UTC) | Action | Domain | Trigger |
|---|---|---|---|
| June 15, 09:00 | **T+14 CHECKPOINT**: Full D39 response tally; weighted score; Phase 2 path determination | D39 | Always |
| June 15, 09:15 | Log T+14 results and Phase 2 path in RESPONSE_MONITORING_DASHBOARD_TEMPLATE.md | D39 | Always |
| June 15, 09:30 | If STRONG or MODERATE: Begin D38 Tier A sends | D38 | STRONG / MODERATE |
| June 15, 09:30 | If WEAK: Proceed with D38 Tier A sends but add social distribution simultaneously | D38 | WEAK (no delay to D38) |
| June 15, 10:00–18:00 | D38 Tier A send window: 15 contacts (or up to 20 if Tier B expansion triggered) | D38 | Always |
| June 15 | If STRONG: In D38 Tier A emails, reference D39 engagement as social proof | D38 | STRONG only |
| June 15 | If WEAK: Launch D38 social distribution simultaneously (Reddit, Twitter) | D38 | WEAK only |
| June 15–July 15 | If WEAK path: D39 Tier 2 outreach window (CBPP, NDRN, DRA, SisterSong, NACHC) | D39 | WEAK only |

**Trigger annotations (June 15 decisions are binding for downstream timeline)**:

| Phase 2 Path | D38 Launch | D40 Timing | D39 Tier 2 |
|---|---|---|---|
| STRONG | June 15, default | July 15 or accelerated | June 5–12 (already executing) |
| MODERATE | June 15, default | July 15 default | June 10–15 |
| WEAK | June 15 + social simultaneously | August 1 (delayed) | June 15–July 15 |
| DELIVERY_PROBLEM | June 15 if delivery resolved | July 15 default | June 15 after resolution |

---

## Phase 5: D38 Monitoring Window + D40 Preparation
### June 16 – July 14, 2026

| Date Range | Action | Domain | Trigger |
|---|---|---|---|
| June 16–20 | Complete D38 Tier A send window (remaining 10 contacts) | D38 | Always |
| June 18 | D38 Day 3 response check (see DOMAIN_38_40_RESPONSE_MONITORING_FRAMEWORK.md) | D38 | Always |
| June 21–28 | D38 Tier B sends (MODERATE/STRONG path) or July 1–10 (if D38 Tier A weak) | D38 | Path-dependent |
| June 21–30 | **D40 Gist creation** (default) or already underway if Branch 2D triggered | D40 | Default / moved up if STRONG |
| June 22 | D38 Day 7 response check | D38 | Always |
| June 29 | D38 Day 14 response check — assess whether D38 is STRONG/MODERATE/WEAK | D38 | Always |
| June 29 | If D38 Day 14 weak AND D39 T+30 weak: activate dual weak-outcome protocol | Both | Dual-weak only |
| June 15–July 1 | Daily SCOTUSblog monitoring for Trump v. Barbara ruling | D58 | Always (ruling expected) |
| Late June – July 1 | **Trump v. Barbara ruling expected**: activate DOMAIN_58_RULING_TRIGGER_READINESS.md same day | D58 | Ruling issuance |
| June 30–July 5 | Finalize D40 Tier A email templates (15 contacts) | D40 | Always |
| July 1–10 | D38 Tier B secondary sends (if STRONG/MODERATE path and Tier B expansion activated) | D38 | STRONG/MODERATE |

**Key dependency point — June 29 D38 Day 14 check**:
- D38 Day 14 result feeds directly into D40 launch strategy
- If D38 is STRONG by June 29: D40 Tier A may be moved to July 1 (simultaneous with D38 Tier B)
- If D38 is MODERATE: D40 proceeds July 15 default
- If D38 is WEAK: D40 Tier A delayed to August 1 (per WEAK Phase 2 path)

---

## Phase 6: T+30 Domain 39 Final + D40 Tier A Launch
### July 1–20, 2026

| Date/Time (UTC) | Action | Domain | Trigger |
|---|---|---|---|
| July 1, 09:00 | **D39 T+30 FINAL CHECKPOINT**: Complete response tally; citation check; Phase 2 final assessment | D39 | Always |
| July 1, 09:30 | Log T+30 results; update Phase 2 path assessment | D39 | Always |
| July 1 | D38 Day 16 assessment (if Domain 38 Tier A went out June 15, this is Day 16) | D38 | Always |
| July 5–12 | D40 Tier A email final preparation (confirm all contacts, Gist URL, templates) | D40 | Always |
| July 10 | Trump v. Barbara ruling deadline (near-certain by July 10 if not yet issued) | D58 | Always |
| July 14 | Final D40 pre-send verification: Gist live; all templates complete; contacts confirmed | D40 | Always |
| July 15, 09:00 | **D40 Tier A launch** (or August 1 if WEAK path) | D40 | Default |
| July 15 | D38 Day 30 final assessment (see DOMAIN_38_40_RESPONSE_MONITORING_FRAMEWORK.md Gate 4) | D38 | Always |
| July 18 | D40 Day 3 response check | D40 | Always |
| July 15–20 | Complete D40 Tier A send window | D40 | Always |

**Key dependency point — July 15**:
- D38 Day 30 final assessment occurs same day D40 Tier A launches
- D38 Day 30 result (STRONG/MODERATE/WEAK) informs how D40 Tier A emails are framed:
  - If D38 STRONG: "Organizations working on AI governance engaged with this framework — the companion electoral manipulation analysis connects to the same democratic infrastructure crisis"
  - If D38 MODERATE: Standard cold outreach with electoral calendar urgency hook
  - If D38 WEAK: Lead with EU enforcement news from August 2 as external hook (13 days away)

---

## Phase 7: D40 Monitoring + Final Campaign Assessment
### July 22 – November 3, 2026

| Date | Action | Domain |
|---|---|---|
| July 22 | D40 Day 7 response check — if 0 responses, begin social distribution immediately | D40 |
| July 29 | D40 Day 14 CRITICAL gate (see DOMAIN_38_40_RESPONSE_MONITORING_FRAMEWORK.md Gate 3) | D40 |
| July 16 | D39 T+45 final check (secondary citation search; campaign close) | D39 |
| July 30 | D38 Day 45 citation check | D38 |
| August 1–7 | D40 Tier A launch (if WEAK path delays from July 15) | D40 |
| August 2 | EU AI Act Article 50 enforcement — use as D38/D40 amplification hook | D38, D40 |
| August 14 | D40 Day 30 final assessment | D40 |
| August 29 | D40 Day 45 citation check + EU enforcement hook assessment | D40 |
| September–October | D40 Tier B/C/D social and community distribution (pre-election window) | D40 |
| November 3, 2026 | US midterm elections — Wave 2 complete | — |

---

## Trigger Dependency Summary

The following are explicit points where Domain 39 response data directly adjusts Domain 38 and Domain 40 sequencing:

| Trigger Point | Date | Adjustment Made |
|---|---|---|
| D39 T+3 bounce | June 4 | Alternative contact protocol immediately; does not change D38 launch date |
| D39 T+3 = 5 responses | June 4 | D40 Gist creation begins June 4 (10 days early) |
| D39 T+7 = 0 responses | June 8 | D38 Tier A expands to include 5 Tier B contacts; alternative subject lines |
| D39 T+7 = 5 responses | June 8 | D40 Gist creation begins June 8 if not already; assess June 15 simultaneous launch |
| **D39 T+14 STRONG (3+)** | **June 15** | **D38 emails reference social proof; D40 July 15 default; Tier B accelerated** |
| **D39 T+14 MODERATE (2)** | **June 15** | **Default timeline; caution gates; contingency Tier 2 standing by** |
| **D39 T+14 WEAK (0–1)** | **June 15** | **D38 adds social distribution June 15; D40 delayed to August 1; D39 Tier 2 activates** |
| D38 Day 14 = STRONG | June 29 | D40 may advance to July 1 simultaneous with D38 Tier B |
| D38 Day 14 = WEAK | June 29 | If also D39 WEAK: dual weak protocol; D40 to August 15; shift to social |
| D39 T+30 = 6+ | July 1 | Coalition facilitation; D38 + D40 simultaneous Tier A possible; Tier 0 contacts |
| D38 Day 30 = STRONG | July 15 | D40 emails reference D38 engagement as social proof |
| D38 Day 30 = WEAK | July 15 | D40 leads with EU enforcement deadline (August 2) as external hook |
| Trump v. Barbara ruling | Late June – July 1 | D58 same-day activation (independent; does not affect D38/D40 timing) |

---

## Timeline Quick Reference

| Date | Key Event | Domain | Adjustable? |
|------|-----------|--------|-------------|
| June 1 | D39 Tier A send (complete) | D39 | No |
| June 4 | D39 T+3 check | D39 | — |
| June 8 | D39 T+7 check | D39 | — |
| **June 15** | **D39 T+14 PRIMARY GATE + D38 Tier A launch** | **D39 / D38** | **Yes (STRONG may accelerate; WEAK adds social)** |
| June 18 | D38 Day 3 check | D38 | — |
| June 22 | D38 Day 7 check | D38 | — |
| June 29 | D38 Day 14 check | D38 | — |
| Late June – July 1 | Trump v. Barbara ruling | D58 | No (ruling-triggered) |
| July 1 | D39 T+30 final + D38 Day 16 | D39/D38 | — |
| **July 15** | **D40 Tier A launch (default)** | **D40** | **Yes (accelerated to July 1 if STRONG; delayed to Aug 1 if WEAK)** |
| July 29 | D40 Day 14 critical gate | D40 | — |
| August 2 | EU AI Act enforcement (D38 amplification hook) | D38/D40 | No |
| November 3 | US midterms (D40 absolute deadline) | D40 | No |

---

*Created June 1, 2026. Companion files: PHASE_2_ACTIVATION_DECISION_TREE.md, DOMAIN_39_RESPONSE_MONITORING_PLAN.md, DOMAIN_38_40_CONTINGENCY_DECISION_TREE.md (predecessor), DOMAIN_38_40_EXECUTION_TIMELINE.md (predecessor), DOMAIN_58_RULING_TRIGGER_READINESS.md, RESPONSE_MONITORING_DASHBOARD_TEMPLATE.md.*
