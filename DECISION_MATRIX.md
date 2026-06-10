# User Decision Matrix — June 10, 2026

> Consolidated view of all pending user decisions blocking project progress.
> Each decision has: recommendation, deadline (if any), consequence of delay, and next action.

---

## Priority 1: Stockbot Codebase Assessment — Bug Sprint vs Feature Implementation

**Decision needed**: Approve Tier-1 critical bug fixes before proceeding with feature work, OR proceed with features as-is.

**Context**: Session 2980 completed comprehensive codebase assessment. Three critical bugs identified:
- **C-1**: Walk-forward t-stat broken (10–15 line fix). Gate G3 results spurious.
- **C-2**: OOS features computed 2× per fold (doubles inference time for ensemble models).
- **C-3**: Cash pool inflation risk (concurrent closes can push pool above account cash).

**Documents for review**: 
- `projects/stockbot/docs/AGENT_LOOP_WORKFLOW.md`
- `projects/stockbot/docs/CODEBASE_REVIEW_COMPREHENSIVE.md`
- `projects/stockbot/docs/MODEL_ARCHITECTURE_ASSESSMENT.md`
- `projects/stockbot/docs/IMPLEMENTATION_IDEAS.md`

**Recommendation**: Fix critical bugs first (1–1.5 sessions) → gate results become trustworthy → feature development proceeds faster with accurate validation.

**Consequence of delay**: Feature development proceeds on broken validation gates; time spent on features may need to be redone after C-1/C-2 fixes.

**Deadline**: None (but blocks Phase 2 feature work).

**Next action**: (1) User reviews 4 documents in `projects/stockbot/docs/`. (2) User decides: Bug Sprint (Phase 1) or Feature Implementation (Phase 0). (3) Orchestrator queues work accordingly.

---

## Priority 2: systems-resilience Platform Deployment — Discourse vs Nextcloud+Matrix

**Decision needed**: Which platform to deploy (Discourse recommended) + provide IP/domain/SMTP credentials.

**Status**: ⚠️ **DEADLINE PASSED** (June 8 18:00 UTC was the deployment window). Currently June 10.

**Context**: Session 2987 created three production-ready deployment documents (14.6K words total):
- `DISCOURSE_DEPLOYMENT_RUNBOOK.md` (6.6K) — 12-phase ARM64 Docker deployment
- `PHASE_5_1_PUBLICATION_OPERATIONAL_PROCEDURES.md` (4.5K) — June 9 publication workflow
- `PHASE_5_1_PUBLICATION_ROLLBACK_PROCEDURE.md` (3.6K) — Failure recovery procedures

**Recommendation**: Discourse deployment (8GB RAM, 2–3 hours, simpler ops vs Nextcloud's 16GB/4–6 hours). Confidence: 92%.

**Consequence of delay**: June 9 publication deadline (13:00–15:00 UTC) likely missed. Phase 5.1 content (61,611 words, 336+ citations) has nowhere to publish.

**Next action**: (1) Clarify whether deployment happened post-June 8 deadline. (2) If not deployed, approve Discourse path + provide IP, domain, SMTP credentials. (3) Orchestrator proceeds with deployment if still viable OR escalates if too late.

**Question for user**: Did you deploy the platform between June 8 18:00 UTC and now (June 10)? Or should we reschedule publication?

---

## Priority 3: open-repo Deployment Timing — 09:00 UTC vs 20:00 UTC

**Decision needed**: Clarify deployment start time (June 12, 2026).

**Status**: Timing conflict exists in deployment documentation. Four newer docs specify 09:00 UTC. Two older docs specify 20:00 UTC.

**Context**: Session 2987 created three production-ready pre-flight documents (118 KB total):
- `DEPLOYMENT_JUNE12_PREFLIGHT_ENVIRONMENT.md` (50K, 8 binary PASS/FAIL gates)
- `DEPLOYMENT_JUNE12_RISK_MITIGATION.md` (37K, 6 failure modes + recovery)
- `DEPLOYMENT_JUNE12_SUCCESS_CRITERIA.md` (31K, SLA targets + monitoring)

**Consequence of delay**: Documentation inconsistency prevents execution. Deployment window (June 12) is known. Timing decision is needed before June 11 evening to coordinate stakeholders.

**Next action**: (1) User clarifies: 09:00 UTC (business hours) or 20:00 UTC (after-hours)? (2) Orchestrator updates deployment documents with unified timing. (3) Pre-flight verification begins June 11. (4) Deployment executes June 12 per chosen window.

**Question for user**: Should open-repo deploy at 09:00 UTC (business hours) or 20:00 UTC (after-hours)?

---

## Priority 4: cybersecurity-hardening Phase 2 Scope

**Decision needed**: Clarify Phase 2 scope (defensive hardening only, or replacement scope).

**Status**: Phase 1 in progress (Step 1.3 VeraCrypt restart pending).

**Context**: Session 2987 analysis flagged that Phase 2 planning request included operational evasion procedures (forensic wiping, counter-surveillance, law enforcement avoidance, border crossing response) which exceeds **defensive security** scope into operational evasion.

**Current Phase 1 status**:
- ✅ Step 1.1 Signal — complete
- ✅ Step 1.2 iPhone tracking — mostly complete (Step 4 waiting for Apple security delay)
- 🔄 Step 1.3 VeraCrypt — restart pending (user action)
- ⏳ Steps 1.4–1.7 — ready to execute (2–3 hours post-restart)

**Phase 2 playbooks ready (all v1.1 complete, deployment-ready)**:
- Journalist operational security playbook
- Immigration surveillance evasion playbook
- Activist organizing security playbook

**Decision options**:
- **Option A**: Phase 2 focuses on defensive hardening only (biometric hardening, data compartmentalization, privacy infrastructure)
- **Option B**: Replace Phase 2 with standalone tactical defensive hardening (Faraday cage design, device compartmentalization, redundant backups, air-gapped systems)
- **Option C**: Defer Phase 2 planning until Phase 1 completes

**Recommendation**: Option A (defensive hardening only) aligns with existing Phase 2 playbooks and avoids evasion tradecraft scope creep.

**Next action**: (1) User clarifies Phase 2 scope. (2) Restart VeraCrypt on Windows + complete Steps 1.4–1.7 (Ente Auth, Bitwarden, data broker opt-outs). (3) Orchestrator sequences Phase 2 work accordingly.

**Question for user**: Should Phase 2 cover defensive hardening only (biometric, data compartmentalization, privacy), or replace with different scope?

---

## Lower Priority: Blocked Items (User Actions)

### mfg-farm: Test Print Execution
**Status**: Paused. Phase 1 launch sequence production-ready. Awaiting test print execution (user action).

**Spec**: 0.20mm layer height, PLA+, 3 walls, 220–225°C. Evaluate snap-arm tolerance (1.4mm highest-risk feature).

**Next action**: Execute test print → report outcome → orchestrator routes to corresponding Part 4 launch branch (PASS/PASS-WITH-ADJUSTMENTS/FAIL/PARTIAL-FAIL).

### cybersecurity-hardening: VeraCrypt Restart
**Status**: In progress. Step 1.3 needs Windows restart to complete VeraCrypt pre-boot test.

**Next action**: Restart Windows → enter VeraCrypt password → click Encrypt to start background encryption → resume Phase 1 from Step 1.4.

---

## Summary Table

| Project | Decision | Deadline | Recommendation | Status |
|---------|----------|----------|-----------------|--------|
| **stockbot** | Bug Sprint vs Feature? | None | Bug Sprint first (1–1.5 sessions) | Awaiting review |
| **systems-resilience** | Platform + credentials? | **PASSED** (June 8 18:00) | Discourse + IP/domain/SMTP | Awaiting clarification |
| **open-repo** | 09:00 or 20:00 UTC? | June 12 @ chosen time | Clarify for stakeholder coordination | Awaiting clarification |
| **cybersecurity-hardening** | Phase 2 scope? | None | Defensive hardening only (Option A) | Awaiting clarification |

---

## Consequences of Pause Directive

**Projects paused** (zero autonomous work):
- resistance-research (Phase 2 execution ready, all contacts verified)
- cybersecurity-hardening (Phase 1 in progress)
- mfg-farm (Phase 1 launch ready)
- seedwarden (status TBD)
- off-grid-living (complete, awaiting user social media execution)
- workout, resume, open-source-rideshare

**Pause can be lifted by**:
1. User explicitly unpausing via Discord or PROJECTS.md update
2. OR user approving one of the above four decisions, which unblocks that project's work
3. OR orchestrator completing exploration queue items that lead to unblock

**Recommended next step**: User makes the four Priority 1–4 decisions above → orchestrator resumes execution on approved items → pause can remain for other projects or be fully lifted.

