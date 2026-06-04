---
title: "Phase 6 Wave 2 Activation Checklist"
project: systems-resilience
phase: 6
wave: 2
status: PRODUCTION-READY — June 15 deployment
created: 2026-06-04
revised: 2026-06-04
activation_date: 2026-06-20
non_negotiable_anchors:
  - "June 20 Wave 2 start — immovable"
  - "June 27 T+7 first-draft checkpoint — must be met"
cross_references:
  - PHASE_6_WAVE_1_EXECUTION_CHECKLIST.md
  - WAVE_2_DOMAIN_SEQUENCING_FRAMEWORK.md
  - RESOURCE_CONTENTION_MITIGATION_JUNE_15_30.md
  - WAVE_2_GENERIC_ONBOARDING_TEMPLATE.md
  - AUTHOR_READINESS_INTAKE_FORM.md
word_count: ~2,400
---

# Phase 6 Wave 2 Activation Checklist
## June 15–20 Transition: Wave 1 Completion → Wave 2 Initialization

**Prepared**: June 4, 2026 (production deployment)
**Activation start**: June 20, 2026 (immovable)
**Transition window**: June 15–20 (Wave 1 publication finalization + Wave 2 prep)
**T+7 first-draft checkpoint**: June 27 (non-negotiable)
**Platform**: Nextcloud+Matrix (activated June 4 13:00 UTC)
**Lead**: Orchestrator + Wave 2 domain leads

---

## Part 1: June 15–20 Transition Task List

### June 15 — Wave 1 Final Review Day

- [ ] **Publication gate decision** (09:00 UTC): Are all 5 Phase 5 Wave 1 domains (governance, food, info, security, scaling) peer-reviewed and approved? If yes → proceed. If 3-4 approved → proceed with scope note. If fewer than 3 → activate Trigger 2 below.
- [ ] **Wave 2 author roster confirmed**: ≥4 authors confirmed with June 20 start date, payment terms signed, communication channel verified in Nextcloud+Matrix. If fewer than 4 → activate Trigger 1 below.
- [ ] **June 15 go/no-go decision recorded** in ORCHESTRATOR_STATE.md with author count, Wave 1 publication status, and any contingency routes activated.

### June 16 — Onboarding Kit Delivery

- [ ] Send Wave 2 onboarding kit (see Part 2 below) to all confirmed authors via email + Matrix DM.
- [ ] Kit delivery confirmed: each author acknowledges receipt in their Nextcloud+Matrix domain room (`#wave2-[domain]:resilience-hub`).
- [ ] Pre-staged source library published to each author's Nextcloud domain folder (`Phase6-Wave2-[Domain]/00-SOURCES.md`).
- [ ] Domain outline committed to `projects/systems-resilience/phase-6/` for each confirmed Wave 2 domain.

### June 17 — Cross-Domain Integration Audit

- [ ] Terminology audit: key terms (governance, scale, community, resilience, Dunbar threshold) defined consistently across all 5 Phase 5 Wave 1 domains. Flag mismatches → minor: fix before June 18; major: log as "Wave 2 alignment note" and brief authors.
- [ ] Citation format consistent: URL format, access notation, citation style match across all published domains.
- [ ] Cross-references verified: if Domain A cites Domain B, Domain B acknowledges the connection.
- [ ] Tonal consistency: all domains address the same practitioner/policymaker reader.

### June 18 — Author Orientation Async Delivery

- [ ] Wave 1 context summary (3-page doc) delivered to all Wave 2 authors: major findings across 5 domains, reader feedback themes, integration notes.
- [ ] Peer-mentor assignments sent: each Wave 1 domain author receives their Wave 2 mentee assignment; introductory Matrix message sent.
- [ ] Domain dependency map (text or visual, from WAVE_2_DOMAIN_SEQUENCING_FRAMEWORK.md Part 3) included in orientation materials.
- [ ] Optional sync orientation offered: 30-min Matrix audio call (if ≥3 authors in overlapping time zones). Record asynchronously if called.

### June 19 — R-Gate Final Check (All Gates Must Be Green by EOD)

- [ ] **R-Gate 1**: ≥4 authors confirmed, start date June 20, payment first-milestone terms in writing.
- [ ] **R-Gate 2**: ≥3 of 5 Wave 1 domains peer-reviewed and approved; publication timeline committed (June 22, June 30, or deferred with impact note).
- [ ] **R-Gate 3**: Source libraries (25–35 verified URLs per domain), domain outlines, peer-reviewer roster (≥1 per domain) all present in Nextcloud.
- [ ] **R-Gate 4**: Git directory structure ready (`projects/systems-resilience/phase-6/` with placeholder `.md` files for each Wave 2 domain). ORCHESTRATOR_STATE.md can accept Wave 2 activation entry.
- [ ] **Resource contention check**: confirm which RESOURCE_CONTENTION_MITIGATION_JUNE_15_30.md scenario (A/B/C) is active as of June 19 EOD.

### June 20 — Wave 2 T+0 Kickoff (06:00 UTC)

- [ ] Orchestrator pre-flight: read ORCHESTRATOR_STATE.md; confirm all R-gates green; confirm Wave 1 publication status and any blocking conditions.
- [ ] Kickoff emails sent to all Wave 2 authors (07:00–09:00 UTC): domain framing, research kit link, timeline, peer-mentor contact, payment first-milestone confirmation.
- [ ] Peer reviewer roster notified: introductory note, review window expectation (T+10 = June 30 to T+12 = July 2).
- [ ] Project setup (09:00–17:00 UTC): Wave 2 domain `.md` files created with YAML frontmatter (title, author, status: IN-PROGRESS, created: 2026-06-20). Shared source libraries populated. ORCHESTRATOR_STATE.md updated: Phase 6 Wave 2 activated, domain list, author roster.

---

## Part 2: Author Readiness Assessment

### Who from Wave 1 Can Lead Wave 2?

Wave 2 domain leads are drawn from the Wave 1 author pool or from a second recruitment cohort. Wave 1 authors qualify to lead a Wave 2 domain if they meet all three criteria:

1. **Domain expertise match**: Their Wave 1 domain directly informs one or more Wave 2 domains (e.g., a Wave 1 governance author has direct relevance to Wave 2 institutional scaling).
2. **Writing quality**: Their Wave 1 document met publication standards on first or second peer review pass (not requiring structural overhaul).
3. **Timeline commitment**: They can commit 4–6 hours/week June 20–July 10 for Wave 2 (not just peer-mentor capacity, but active research authorship if assigned a new domain).

Wave 1 authors who cannot commit new authorship hours serve as **peer mentors** only (2–3 questions/week, informal feedback on drafts) — not as domain leads.

### Tier A/B/C Author Stratification

All Wave 2 authors are assigned a tier using the AUTHOR_READINESS_INTAKE_FORM.md scoring matrix. Tier determines onboarding path and support level:

**Tier A — Leadership Capacity**

- Profile: 5+ years domain expertise; has published practitioner-oriented long-form documents (4,000+ words); comfortable with async work, Markdown, and self-directed research; can identify scope boundaries independently.
- Intake form indicators: Domain Knowledge rating 4–5; Long-Form Writing rating 4–5; Platform Familiarity rating 3+; explicitly states they do not need check-in calls.
- Onboarding path: Receive kit; skip orientation call; submit outline T+3 (June 23); first check-in at T+7 (June 27). Minimal orchestrator overhead.
- Ceiling: Can handle two Wave 2 deliverables if capacity permits (e.g., primary author on Domain A, peer mentor on Domain B simultaneously).
- Bandwidth: 6–8 hrs/week available during June 20–July 10 sprint.

**Tier B — Technical Depth, Standard Support**

- Profile: Strong domain expertise (3–4 years applied practice); has produced long documents but primarily for internal or academic audiences; may need editorial scaffolding on structure and practitioner-audience calibration; reliable but not self-directed.
- Intake form indicators: Domain Knowledge rating 3–4; Long-Form Writing rating 2–3; flags some uncertainty about scope or citation standards.
- Onboarding path: Complete full onboarding kit; receive one additional check-in at T+3 (June 23, before outline due); orchestrator reviews outline before proceeding. Moderate overhead.
- Ceiling: One Wave 2 domain as primary author. Can serve as peer reviewer on a second domain.
- Bandwidth: 4–6 hrs/week available.

**Tier C — Emerging Contributor, Extended Support**

- Profile: Solid domain knowledge but limited long-form publication history; first major practitioner-facing research project; may need scope narrowing consultation and extended timeline.
- Intake form indicators: Domain Knowledge rating 3; Long-Form Writing rating 1–2; flags uncertainty about structure, citation standards, or time commitment.
- Onboarding path: Full onboarding kit; scope narrowing consultation June 20–21; first draft target adjusted to 3,000–4,000 words (instead of 5,000–7,000); additional orchestrator check-in at T+5 (June 25) before T+7 deadline; T+7 first-draft checkpoint is a progress check, not a hard gate. Higher orchestrator overhead.
- Ceiling: One Wave 2 domain, lighter scope. Not assigned peer mentor duties in addition to own authorship.
- Bandwidth: 4 hrs/week minimum required; confirm before assignment.

---

## Part 3: Onboarding Kit Components

The Wave 2 onboarding kit adapts WAVE_2_GENERIC_ONBOARDING_TEMPLATE.md for the Phase 6 context. Each author receives a customized version with the following components:

**Component 1: Domain Framing Document (2 pages)**
- The problem this domain solves within Phase 6 community-scale resilience.
- Explicit connection to Phase 5 Wave 1 domains: which of the 5 community-scale domains (governance, food, info, security, scaling) does this domain build on?
- Reader audience: practitioners, policymakers, community organizers — same as Wave 1.
- Tonal model: name the closest Phase 5 Wave 1 document as structural reference.

**Component 2: Research Scope Brief (2 pages)**
- Scope statement (what IS in scope) and out-of-scope statement (what is NOT covered, why).
- Section outline (drawn from Phase 6 candidate document or orchestrator-defined).
- Word target: 5,000–7,000 words (Tier C: 3,000–4,000).
- Citation requirement: 25–40 citations; green/amber/red quality rating per WAVE_2_GENERIC_ONBOARDING_TEMPLATE.md Section 5.

**Component 3: Pre-Staged Source Library (in Nextcloud)**
- 25–35 verified, accessible URLs with annotations (Section, quality rating, relevance note).
- Wave 1 reference documents: links to the Phase 5 Wave 1 domains in Nextcloud.
- Cross-reference checklist: terminology alignment requirements (e.g., "use 'Dunbar threshold' as defined in Wave 1 Governance domain").
- Peer-mentor contact: name, Matrix handle, domain expertise, available hours.

**Component 4: Timeline and Milestone Card (1 page)**
- T+0 June 20: Kickoff message in Matrix domain room.
- T+3 June 23: Outline submission (H2/H3 structure + section purpose notes).
- T+7 June 27: **Non-negotiable first-draft checkpoint** — 50% draft: all headings, Sections 1–2 narrative-complete, citations roughed in.
- T+10 June 30: Full first draft (all sections, citations verified).
- T+12 July 2: Peer review feedback received.
- T+14 July 4: Revision complete, submitted for final readiness gate.
- Publication readiness gate: July 5 go/no-go.

**Component 5: Platform Access Instructions (Nextcloud+Matrix)**
- Nextcloud login: server URL, username format, workspace folder structure (00-SCOPE.md, 00-SOURCES.md, DRAFT-[domain].md, PEER-REVIEW.md).
- Matrix rooms: `#wave2-[domain]:resilience-hub` (primary) and `#wave2-general:resilience-hub` (cross-author coordination).
- First action: post T+0 kickoff message in domain Matrix room by June 20 noon UTC.
- Editor test: add/delete test line in DRAFT file to confirm write permissions.

**Component 6: Wave 1 Feedback Summary (2 pages)**
- Reader feedback themes from Phase 5 Wave 1 early readers: structure wins, common gaps, framing issues.
- Integration learnings from editorial pass: cross-domain terminology, citation patterns, tonal notes.
- Quality bar: peer review criteria from Wave 1; Wave 2 uses identical framework.

**Component 7: Payment and Logistics (1 page)**
- Honorarium schedule (first milestone on June 23 upon outline approval; second milestone on July 5 upon publication readiness gate).
- Communication channel preference (Matrix async primary; email for blocking questions).
- Escalation path: blocking question → tag @project-lead in Matrix room AND email [PROJECT LEAD EMAIL] with "Wave 2 scope — urgent" subject line.
- Reduced availability windows: June 20–23 (stockbot expansion peak, see RESOURCE_CONTENTION_MITIGATION_JUNE_15_30.md Scenario A); orchestrator response target 6 hours, not 4.

---

## Part 4: Contingency — Author Unavailability

### Trigger: Fewer Than 4 Authors Confirmed by June 15

**Day 0 (June 15 09:00 UTC)**: Count confirmed authors.

- **4+ confirmed**: Proceed with full Wave 2 scope (5–7 domains, see WAVE_2_DOMAIN_SEQUENCING_FRAMEWORK.md). No action required.
- **3 confirmed**: Proceed with reduced scope (3 domains). Assign one domain per confirmed author from priority list (Ecosystem Restoration, Institutional Learning, Access & Equity in that order). Fourth domain deferred to July 1 Wave 2.5 cohort. Notify confirmed authors of scope reduction.
- **2 confirmed**: Activate self-execute path for 2 domains (orchestrator authors outline + research brief; external editor completes prose). Recruit 2 additional authors June 16–18 from candidate list. Wave 2 starts June 20 for confirmed authors; deferred domains start July 1.
- **0–1 confirmed**: Defer full Wave 2 to July 1. All orchestrator capacity June 20–30 redirected to Phase 5 Wave 1 publication completion and stockbot expansion. Wave 2 activation checklist re-runs from Part 1 on July 1.

### Trigger: Author Drops Out After June 20 (Mid-Sprint)

**Detection**: Author silent in Matrix domain room for 48+ hours after T+0, OR explicit withdrawal message.

**Response sequence** (complete within 24 hours of detection):

1. Contact author directly (Matrix DM + email) — confirm withdrawal vs. technical issue.
2. If withdrawn: assess their draft state. If outline (T+3) is complete → reassign to peer mentor or alternate author for continuation. If no outline → defer domain to July 1 or activate orchestrator self-execute for that domain.
3. If technical issue: troubleshoot Nextcloud+Matrix access within same day. See DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md for access recovery steps.
4. Notify remaining authors: brief note in `#wave2-general` that one domain is being handled; no disruption to their tracks.

### Cross-Training Procedure

All Wave 2 domain leads receive a brief cross-domain summary (1-page) of each other's domain scope. Purpose: if one author drops, an adjacent author can pick up the outline within 2–3 days rather than starting cold. Cross-domain summaries delivered with onboarding kit on June 16.

---

## Part 5: Non-Negotiable Anchors

Two dates are immovable regardless of any contingency trigger:

**June 20 — Wave 2 Start Date**

The June 20 start is locked because: (a) it follows the minimum publication preparation window for Wave 1 (June 15–19), (b) it precedes the July 5 publication readiness gate that Phase 7 pilot recruitment depends on, and (c) the June 20–30 stockbot expansion window means that any Wave 2 delay past June 20 will collide with a stockbot CAUTION/ROLLBACK window rather than running parallel to it. If author recruitment stalls, activate the reduced-scope path (Part 4 above) rather than delaying the start date.

**June 27 — T+7 First-Draft Checkpoint**

The June 27 checkpoint is the first real quality signal of the Wave 2 sprint. A 50% draft on June 27 confirms: (a) the author has fully engaged with the source library, (b) the domain scope is workable within the timeline, and (c) the T+14 (July 4) full-draft gate is achievable. If this checkpoint is missed by more than 3 days, the publication readiness gate slips from July 4–5 to July 11–12, compressing the Wave 3 start window and creating Phase 7 pilot timeline risk. If an author cannot meet the June 27 checkpoint, escalate immediately: scope reduction or replacement, not timeline extension.

---

**Summary**: This checklist governs the June 15–20 transition from Phase 5 Wave 1 publication completion to Phase 6 Wave 2 research initiation. The critical path item is author roster confirmation by June 15. All five R-gates must be green by June 19 EOD. June 20 start and June 27 T+7 checkpoint are immovable. Contingency routes for author shortfall, mid-sprint dropout, and platform access failures are pre-defined and do not require user escalation to execute.
