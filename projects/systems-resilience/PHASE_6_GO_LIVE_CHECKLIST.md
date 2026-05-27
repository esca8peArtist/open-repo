---
title: "Phase 6 Go-Live Checklist — June 1 06:00 UTC Activation"
project: systems-resilience
phase: 6
status: READY FOR JUNE 1 ACTIVATION — user decisions required by May 31
decision_deadline: 2026-05-31
activation_target: 2026-06-01T06:00:00Z
created: 2026-05-28
session: 1711
purpose: "Single-point checklist for June 1 06:00 UTC Phase 6 orchestrator activation. All gates must be green before research agent dispatch."
companion_docs:
  - PHASE_6_DOMAIN_SELECTION_TOOLKIT.md
  - PHASE_6_AUTHOR_HIRING_AND_ONBOARDING_FRAMEWORK.md
  - PHASE_6_ORCHESTRATOR_BURN_FORECAST.md
  - DECISION_SUPPORT_RECOMMENDATIONS.md
---

# Phase 6 Go-Live Checklist

**Activation target**: June 1, 2026 06:00 UTC  
**Decision deadline**: May 31, 2026 23:59 UTC  
**How to use**: Work through each section in order. Items marked [USER] require input from the user before June 1. Items marked [AGENT] execute automatically on June 1. All [USER] items must be confirmed before [AGENT] items begin.

---

## Section 1: User Decision Confirmation

These three decisions must be logged in CHECKIN.md by May 31 23:59 UTC. The June 1 activation is conditioned on all three.

### 1.1 Phase 5 Publication Option

- [ ] **[USER] Publication option selected**: A (staged June 5 + June 30) / B (unified June 15) / C (rolling weekly)
- [ ] **[USER] Option A selected**: Confirm no Wave 3 content additions required before June 30 (current 22,821-word corpus is sufficient for publication)
- [ ] **[USER] Option B selected**: Confirm 10–15 hours editorial integration capacity available June 1–14 with no competing multi-project disruptions
- [ ] **[USER] Option C selected**: Confirm weekly publication availability confirmed for 6 consecutive weeks (May 30–July 10)

If no decision is logged by May 31 23:59, Option A is the default activation per `DECISION_SUPPORT_RECOMMENDATIONS.md` (Section 7). Phase 5 editorial begins June 1 under Option A terms.

### 1.2 Phase 6 Domain Selection

- [ ] **[USER] Domain selection logged in CHECKIN.md**: Solo (A, C, or D) / A+C / A+D / other
- [ ] **[USER] Domain A (Economic Resilience) if selected**: Confirm source library readiness acknowledged (75–80%, production begins June 8)
- [ ] **[USER] Domain C (Skills Development) if selected**: Confirm 5-day learning curve research sprint (June 8–12) is acknowledged; production begins June 10
- [ ] **[USER] Domain D (Governance Scaling) if selected**: Confirm extended source sprint (June 1–10) is acknowledged; production begins June 15; weekly scope audits approved

Default if no domain selection logged: Domain A (Community Economic Resilience) activates as solo selection. Per `PHASE_6_DECISION_SUPPORT.md` lead recommendation.

### 1.3 Author Hiring Status

- [ ] **[USER] Author confirmed or path selected**: Primary author confirmed / Fallback author confirmed / Self-execute path active
- [ ] **[USER] Author contract signed** (if author path): Agreement countersigned; first milestone (20%) payment processed or confirmed pending
- [ ] **[USER] Self-execute path** (if activated): Confirm Orchestrator is the producer; peer reviewer identified for domain

If author status is unresolved at June 1 06:00 UTC, self-execute path activates automatically with onboarding beginning June 1 regardless.

---

## Section 2: Infrastructure Readiness

These items should be confirmed by May 31. They can be checked asynchronously before June 1 — no user decision is required, only verification.

### 2.1 Communications and Notifications

- [ ] Project Slack channel (or email thread) created for Phase 6 — Orchestrator, author (if confirmed), research agent communication
- [ ] Author contact information confirmed (email; phone for time-sensitive follow-ups)
- [ ] Friday status email protocol confirmed with author (Friday 17:00 author local time; Orchestrator responds by Sunday)
- [ ] Checkpoint calendar invites sent (or calendar entries logged): June 29, July 13, July 27, August 9 at agreed times

### 2.2 Document and File Infrastructure

- [ ] Phase 6 project directory confirmed present: `projects/systems-resilience/phase-6/`
- [ ] Pre-research assets verified committed to master:
  - [ ] Farm equipment Track A pre-research (44,000+ words, 78 sources): `04-phase-4b-agricultural-intensification.md` and related files
  - [ ] Meshtastic Track B pre-research (15,600+ words, 71 sources): `PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md` and related files
  - [ ] Domain A pre-research: `phase-6-candidate-community-economic-resilience.md`
  - [ ] Domain C pre-research: `phase-6-candidate-skills-development.md`
  - [ ] Domain D pre-research: `phase-6-candidate-governance-scaling.md`
- [ ] Author onboarding files ready to share:
  - [ ] `AUTHOR_ONBOARDING_TEMPLATE.md` filled in (zero [BRACKETED] placeholders remain)
  - [ ] `phase-6-author-onboarding-kit.md` confirmed current
  - [ ] Source library folder assembled (30–40 verified sources, annotated)
- [ ] Model document confirmed accessible to author: `phase-5-wave-2-community-implementation-playbook.md`

### 2.3 Phase 5 Publication Assets

- [ ] Wave 1+2 document list confirmed (7 documents, 43,621 words):
  - [ ] `phase-5-wave-2-microgrids-research.md` (Wave 1)
  - [ ] `phase-5-wave-2-veterinary-care-guide.md`
  - [ ] `phase-5-wave-2-psychological-support-guide.md`
  - [ ] `phase-5-wave-2-conflict-resolution-framework.md`
  - [ ] `phase-5-wave-2-community-implementation-playbook.md`
  - [ ] (+ any additional Wave 1+2 docs to confirm)
- [ ] Wave 3 document list confirmed (5 documents, 22,821 words): verify all 5 in `projects/systems-resilience/phase-5/` directory
- [ ] Zero placeholders in all Phase 5 documents: `grep -r "\[fill\]\|\[TBD\]" projects/systems-resilience/phase-5*/` returns zero results
- [ ] Distribution channel selected for Phase 5 publication (GitHub, Gist, PDF, other — confirm with publication decision)

---

## Section 3: Author Onboarding Status

This section confirms the author is ready to begin by June 10. All items should be complete by June 9.

### 3.1 Onboarding Email and Files Sent

- [ ] **[AGENT] Onboarding email sent June 1**: Template 2 from `AUTHOR_ONBOARDING_TEMPLATE.md` sent to confirmed author with zero [BRACKETED] placeholders
- [ ] **[AGENT] File access granted June 1**: Author added to project folder (Google Drive or equivalent); can access all five required documents
- [ ] **[AGENT] Agreement signed and payment confirmed June 1**: Author has countersigned agreement; first milestone payment (20%) confirmed

### 3.2 First-Week Milestones (June 1–9)

- [ ] **June 4**: Author confirms scope alignment — 2–3 sentence summary of three research questions received and acknowledged
- [ ] **June 7**: Verified source list submitted by author; Orchestrator reviews flagged sources (any inaccessible sources resolved)
- [ ] **June 9**: Research outline submitted by author (10–12 sections, scope per section, sources per section, word count estimate, Zone 5 implication note); Orchestrator reviews by June 9 end of day
- [ ] **June 9**: Orchestrator confirms research outline is free of scope violations and author is cleared for June 10 production start

### 3.3 Day 1 Orientation (June 1 or 2)

- [ ] **[AGENT] Kickoff email or call completed**: Author can restate the three research questions in their own words; out-of-scope boundaries confirmed; checkpoint schedule confirmed
- [ ] If synchronous call preferred: 30-minute video call scheduled for June 1 or 2 at author's preferred time

---

## Section 4: Pre-Research Asset Confirmation

Before Phase 6 research agents begin, confirm the pre-research foundation is complete and accessible.

### 4.1 Farm Equipment Track A

**Status**: 44,000+ words, 78 sources committed to master (per Session 1707 completion records).

- [ ] Verify `04-phase-4b-agricultural-intensification.md` accessible and complete (word count check: should be 44,000+ words)
- [ ] Verify `04-technology-repair-equipment-protocols.md` and `04-technology-repair-community-infrastructure.md` present and accessible
- [ ] Confirm 6 documented research gaps (hydraulic seal chemistry, cold-start flow data, bypass thresholds, pressure washer protocols, paper pot transplanter parts, ethanol fuel storage) are noted in the document and do not block June 1 launch
- [ ] These gaps will be filled during June 5–15 integration phase — confirm no new research sprint needed before June 1

### 4.2 Meshtastic Track B

**Status**: 15,600+ words, 71 sources committed to master (per Session 1707 completion records).

- [ ] Verify `PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md` and related Track B files accessible
- [ ] Confirm 4 documented research gaps (ARES repeater listings, LiFePO4 cold-climate data, inter-village link performance, corn canopy attenuation) are noted and do not block June 1 launch
- [ ] FCC 902–928 MHz spectrum policy: no changes as of May 2026 — confirm monitoring note is present in Track B document

### 4.3 Domain A/C/D Candidate Files

- [ ] `phase-6-candidate-community-economic-resilience.md`: complete with source list, three research questions, Zone 5 notes, timeline estimate
- [ ] `phase-6-candidate-skills-development.md`: complete with source list, research questions, learning curve gap documentation
- [ ] `phase-6-candidate-governance-scaling.md`: complete with source list, research questions, scope management notes, failure case study gap documentation

---

## Section 5: Rollback Procedures

If activation conditions are not met on June 1, the following rollback procedures apply. These are not failure modes — they are planned contingencies.

### Rollback 1: Author Onboarding Slips

**Condition**: Author has not confirmed source list verification or research outline by June 9.

**Trigger**: Orchestrator does not receive a research outline by June 9 17:00 UTC.

**Action**:
- Extend onboarding window by 3 days (June 12 production start instead of June 10)
- Send a structured prompt to the author on June 10: "Please submit your research outline by June 12 — this is required before production writing can begin."
- If no outline by June 12: activate self-execute path. Orchestrator produces the domain outline (2–3 hours); author begins production from Orchestrator outline.

**Cascade effect**: 2-day production slip. Final delivery slips from August 9 to August 11. Within the August 16 comfortable buffer. No cascade to Phase 6b (September 1 launch).

### Rollback 2: Domain Selection Not Received

**Condition**: No domain selection logged in CHECKIN.md by June 1 06:00 UTC.

**Action**: Domain A (Community Economic Resilience) activates as default. Per `PHASE_6_DECISION_SUPPORT.md` recommendation. Orchestrator notes the default activation in the daily log and requests user confirmation by June 3.

**No cascade**: Domain A has the highest source readiness (75–80%) and lowest scope risk — it is the safest default. Production proceeds normally. If user later confirms a different domain, activate that domain as Phase 6b beginning September 1.

### Rollback 3: Phase 5 Publication Delayed Beyond June 7 (Option A)

**Condition**: Wave 1+2 publication does not complete by June 7 (e.g., platform issue, link failure, distribution partner delay).

**Action**: Phase 6 research continues unaffected — the research agent is independent of the publication track. Phase 5 publication rescheduled to June 8–10 (still well before June 15 buffer date). Wave 3 publication slips to July 3–5 (3-day slip from June 30 target). No Phase 6 impact.

### Rollback 4: Jetson Unreachable June 1

**Condition**: SSH to xxsb-01 (100.120.18.84) times out on June 1.

**Action**: Per `DECISION_SUPPORT_RECOMMENDATIONS.md` Contingency Trigger table — stockbot Lever B configuration deferred. Phase 6 and Phase 5 editorial continue unaffected (Jetson is not in either critical path). Stockbot connectivity diagnosis batched into June 2–3. Per `RESOURCE_CONTENTION_ANALYSIS.md` Section 4: "Jetson monitoring is passive; it does not compete with editorial writing, research agent production, or author onboarding."

### Rollback 5: Author Declines After June 1 Onboarding Begins

**Condition**: Author resigns or withdraws commitment after June 1.

**Action**:
- Initiate backup author outreach immediately (parallel to self-execute path activation)
- Self-execute path begins June 2: Orchestrator produces domain sections at 3,000–5,000 words/day using pre-research foundation
- If backup author confirmed within 7 days: hand off to backup author with completed sections as starting point
- If no backup author available within 7 days: continue self-execute to completion. Final delivery slips to August 23 (2-week extension). Still above August 30 distribution preparation deadline.

---

## Go / No-Go Summary

| Gate | Owner | Status at June 1 06:00 UTC | Go? |
|---|---|---|---|
| Phase 5 publication option selected | User | Must be logged in CHECKIN.md | YES (or Option A default activates) |
| Phase 6 domain selection confirmed | User | Must be logged in CHECKIN.md | YES (or Domain A default activates) |
| Author hired or self-execute path active | Orchestrator | Must have one path confirmed | YES |
| Domain candidate files accessible | Orchestrator | Pre-committed to master | YES (verify June 1) |
| Track A and B pre-research accessible | Orchestrator | Pre-committed to master | YES (verify June 1) |
| Phase 5 documents zero-placeholder | Orchestrator | Verified in Session 1707 | YES (re-verify if any edits made) |
| Author onboarding email sent | Orchestrator | Send June 1 | YES |
| Research agent briefed | Orchestrator | June 1–3 | YES |

**All gates green = June 1 activation proceeds as planned.**

---

*Created: 2026-05-28 (Session 1711)*  
*Activation target: June 1, 2026 06:00 UTC*  
*Decision deadline: May 31, 2026 23:59 UTC*
