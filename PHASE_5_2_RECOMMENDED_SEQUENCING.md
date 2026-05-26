---
title: "Phase 5.2 Recommended Sequencing Strategy"
project: open-repo
phase: "5.2 implementation planning"
status: "ready-for-execution"
date: 2026-05-26
decision_window: May 26-June 1, 2026
implementation_window: June 1-12, 2026
author: Research Synthesis Agent
tags: [sequencing, timeline, unblocking, priority, parallel-execution, feasibility]
---

# Phase 5.2 Recommended Sequencing Strategy

## Executive Summary

This document provides three recommended sequencing paths for Phase 5.2 candidates, ranked by **unblocking value** (which candidate unblocks the most downstream work), **implementation speed** (which candidate reaches production fastest), and **timeline risk** (which sequencing minimizes the chance of extending beyond June 12, 2026).

**Timeline constraint**: June 1-12, 2026 (11 days, approximately 88 engineering hours available)

**Available candidates**:
1. OPDS Feed Generation (8-11 hours)
2. Accessibility Audit & Remediation (10-12 hours audit + TBD remediation)
3. Search Engine Integration (8-11 hours, Pi 5 thermal risk)
4. API Gateway for Federation (4-6 hours)

**Key insight**: The phase 5.2 window is tight. Two-candidate parallel execution is the high-throughput option; single-candidate focus is safer if uncertainty exists.

---

## Sequencing Recommendation Hierarchy

### Tier 1: PRIMARY RECOMMENDATION — OPDS + API Gateway (Parallel Execution)

**Timeline**: June 1-12 (fits comfortably within window)  
**Total effort**: 12-17 hours (OPDS 8-11h + API Gateway 4-6h)  
**Feasibility**: High (both are well-scoped, low-risk)  
**Expected outcome by June 12**: Both features production-ready

#### Why This Sequencing?

**Unblocking value**:
- OPDS unblocks Kiwix in-app discovery, enabling institutional partnerships, library system integrations, and non-technical end-user adoption. This is foundational for Phase 6's federation roadmap.
- API Gateway unblocks cross-project data sharing and federation partner integrations, positioning open-repo as a reusable data source for related projects.
- Together, they maximize Phase 5.2 user impact (feature completeness + ecosystem integration).

**Speed to value**:
- OPDS is visible to end users immediately: library staff add the catalog URL to Kiwix and see archives in-app.
- API Gateway is visible to federation partners: they can auto-discover and consume exports via REST API.
- Both unblock Phase 6 features without creating technical debt.

**Timeline safety**:
- Combined 12-17 hours leaves 71-76 hours buffer in the 88-hour window.
- OPDS development can start June 1; API Gateway can run in parallel on a separate branch.
- Sequential merge timing: API Gateway (June 3-5) → OPDS (June 5-10) → final testing (June 10-12).
- If either feature encounters unexpected complexity, remaining buffer allows recovery.

#### Implementation Schedule (Tier 1)

```
Week 1 (June 1-5):
  Monday June 1:
    ├─ 09:00 UTC: Create feature/phase-5-2-opds branch; begin OPDS implementation
    └─ 09:30 UTC: Create feature/phase-5-2-api-gateway branch; begin API Gateway implementation
  
  Tuesday June 2:
    ├─ OPDS: Complete OPDSEntry.from_zim_export() factory; begin OPDSGenerator rewrite
    └─ API Gateway: Design federation export API schema; implement endpoints
  
  Wednesday June 3:
    ├─ OPDS: Finish OPDSGenerator; begin router implementation
    └─ API Gateway: Complete endpoint implementation; begin tests
  
  Thursday June 4:
    ├─ OPDS: Complete routers/opds.py; begin 4 endpoint integration
    └─ API Gateway: Complete tests; prepare for merge
  
  Friday June 5:
    ├─ OPDS: Begin unit test suite; validate first endpoint
    └─ API Gateway: Code review; merge to main after approval

Week 2 (June 6-12):
  Monday June 6:
    ├─ API Gateway: Post-merge validation; monitor for integration issues
    └─ OPDS: Complete unit tests (4 new + 19 existing); begin integration test
  
  Tuesday June 7:
    ├─ OPDS: Integration test: kiwix-serve validation; manual Kiwix Android/Desktop test
    └─ All: Buffer time for unexpected issues
  
  Wednesday June 8:
    ├─ OPDS: Code review; documentation completion
    └─ All: Staging deployment preparation
  
  Thursday June 9:
    ├─ All: Final testing; merge OPDS to main
    └─ All: Production deployment readiness
  
  Friday June 10:
    ├─ All: Production deployment; smoke tests
    └─ All: Monitor for issues; 24-hour post-deployment watch
  
  Saturday-Sunday June 11-12:
    └─ Stabilization; documentation finalization; Phase 5.2 closure
```

#### Parallel Branch Coordination

Both branches operate independently until final integration:

**OPDS branch** (`feature/phase-5-2-opds`):
- Depends on Phase 5.1 merge (zim_exports table exists)
- Modifies: `app/services/export/opds_generator.py`, `routers/opds.py`, `tests/unit/test_opds_*.py`
- No conflicts with API Gateway (different module namespaces)
- Can merge independently after Phase 5.1 lands

**API Gateway branch** (`feature/phase-5-2-api-gateway`):
- Soft dependency on Phase 5.1 (uses ZimExport ORM; can mock if needed)
- Modifies: `routers/federation.py` (new), `tests/unit/test_federation_*.py` (new)
- No conflicts with OPDS (different routers)
- Can merge independently after Phase 4 federation infrastructure is confirmed

**Merge order** (optional but recommended):
1. API Gateway merges first (June 5) — faster, unblocks federation testing
2. OPDS merges second (June 10) — allows longer integration testing post-Phase-5.1 merge

**Conflict prevention**:
- Both branches created from main immediately after Phase 5.1 merge (June 1)
- No cross-branch dependencies; independent feature sets
- Both branches maintained continuously; rebase if main changes during development
- Merge reviews can happen in parallel

---

### Tier 2: OPDS-FIRST ALTERNATIVE (If Sequential Preferred)

**Timeline**: June 1-12 (fits comfortably within window)  
**Total effort**: 8-11 hours (OPDS only; API Gateway deferred)  
**Feasibility**: Very High (single-feature focus, maximum testing)  
**Expected outcome by June 12**: OPDS production-ready; API Gateway deferred to Phase 6

#### Why This Sequencing?

**Rationale**: 
- OPDS is the highest-user-value feature for Phase 5.2
- Eliminates parallel execution risk if project team prefers single-feature focus
- Leaves 77-80 hours buffer for unexpected issues, extended testing, or refactoring
- API Gateway can be fast-tracked in Phase 6 (only 4-6 hours)

**When to choose**:
- Team prefers to avoid context-switching between parallel features
- Uncertainty exists about Phase 5.1 merge timing; single-feature development is safer
- Extended OPDS testing/validation is a priority
- Team bandwidth is limited; single-track implementation reduces coordination overhead

#### Implementation Schedule (Tier 2)

```
Week 1 (June 1-7):
  June 1-3:   OPDS implementation (code + unit tests)
  June 3-5:   OPDS integration testing + validation
  June 5-6:   OPDS code review + minor fixes

Week 2 (June 8-12):
  June 8:     OPDS merge to main
  June 9-10:  Staging deployment + smoke tests
  June 10-12: Production deployment + stabilization
  June 12:    Phase 5.2 complete; begin Phase 6 planning
```

**API Gateway deferred**: Scheduled for Phase 6 as a fast-track feature (estimated June 15-20 in Phase 6 Wave 1).

---

### Tier 3: SEARCH-FIRST ALTERNATIVE (If Offline Search Is Priority)

**Timeline**: June 1-12 (fits within window if Pi 5 validation succeeds)  
**Total effort**: 8-11 hours (Search only)  
**Feasibility**: Medium-High (dependent on Pi 5 thermal testing; redesign risk if throttling found)  
**Expected outcome by June 12**: Search indexing production-ready (or remediation plan if Pi 5 issues found)

#### Why This Sequencing?

**Rationale**: 
- Search is the highest-user-value feature for users with large ZIM files (500+ articles)
- Reduces manual navigation burden for healthcare workers, researchers, students using Kiwix
- Positions offline search as a competitive advantage vs. cloud-dependent platforms

**Critical decision gate**: **Must test on Pi 5 hardware by June 2 to validate feasibility**

**When to choose**:
- Target user demographic (healthcare workers, researchers) prioritizes search over in-app discovery
- Offline usability is more critical than institutional integration (OPDS)
- Team has Pi 5 hardware available and can run thermal stress tests early

#### Implementation Schedule (Tier 3)

```
Week 1 (June 1-7):
  June 1-2:   Pre-implementation: Pi 5 thermal test (critical gate)
              ├─ If test passes: Proceed to implementation June 2
              └─ If test fails: Escalate; trigger redesign (tiered indexing or title-only index)
  
  June 2-5:   Search indexing implementation (if thermal test passes)
  June 5-6:   Search latency testing on Pi 5 + Kiwix integration

Week 2 (June 8-12):
  June 8-9:   Code review + special character handling validation
  June 9:     Merge to main
  June 10-12: Staging/production deployment + stabilization
```

**Critical risk**: If Pi 5 thermal throttling is discovered mid-implementation (June 2-3), timeline extends due to redesign:
- Tiered indexing approach: +3-4 hours (build partial index during export, complete offline)
- Title-only index approach: -2 hours (faster but lower relevance)

**Mitigation**: Run Pi 5 test by June 1 end-of-day. If issues found, trigger redesign before June 2 implementation starts.

---

### Tier 4: NOT RECOMMENDED — A11y Audit-First

**Timeline**: June 1-10+ (audit scope 10-12h; remediation uncapped)  
**Total effort**: 10-12 hours audit + TBD remediation (high uncertainty)  
**Feasibility**: Low (remediation scope unknown until audit completes; high overflow risk)  
**Expected outcome by June 12**: Audit report + remediation plan; features deferred to Phase 6

#### Why NOT Recommended

**Key issues**:
- Audit has capped scope (10-12 hours); remediation is uncapped (TBD until audit findings available)
- High probability of overflowing Phase 5.2 window if critical issues discovered
- Audit-only deliverable (without remediation) is incomplete; end users don't see feature until Phase 6
- Phase 6 can run accessibility audit in parallel with other Phase 6 features; no sequencing advantage

**When to choose A11y audit**:
- Organization has accessibility compliance mandate (government, EU public health system)
- User explicitly prioritizes accessibility over feature delivery
- Audit is needed for procurement/grant compliance and must complete by June 12

**Compromise approach**: Defer A11y audit to Phase 6 (parallel execution during Phase 6 Wave 1 or 2). By then, team will have operational experience with Phase 5.1/5.2 features and can scope remediation more accurately.

---

## Decision Matrix: Which Sequencing for Your Priorities?

### User Priority: "I want features visible to end users immediately"

**→ Tier 1 recommendation**: OPDS + API Gateway (parallel)

**Why**:
- OPDS makes archives visible in Kiwix in-app library (end-user visible)
- API Gateway makes open-repo discoverable to federation partners (ecosystem visible)
- Both create momentum for Phase 6 expansion
- High-impact, low-risk execution

---

### User Priority: "I want maximum feature delivery in Phase 5.2"

**→ Tier 1 recommendation**: OPDS + API Gateway (parallel)

**Why**:
- Delivers two complete features instead of one
- OPDS (8-11h) + API Gateway (4-6h) = 12-17h of two independent features
- Search (8-11h) = one feature, higher risk due to Pi 5 thermal uncertainty
- Two features maximize Phase 5.2 momentum for Phase 6

---

### User Priority: "Offline search is critical for my users"

**→ Tier 3 recommendation**: Search-first (with Pi 5 gate)

**Prerequisites**:
- [ ] Pi 5 thermal test completed by June 1 (must know if thermal throttling will occur)
- [ ] If throttling found: redesign planned (tiered indexing or title-only); add 3-4 hours to timeline
- [ ] Team is comfortable with medium-high implementation risk

**Post-Search (June 6-12)**:
- Time available: 5-6 hours
- Can fit: API Gateway (4-6h) as parallel feature
- Doesn't fit: OPDS (8-11h) — would require spillover to Phase 6

---

### User Priority: "Institutional partnerships and library integrations matter most"

**→ Tier 2 recommendation**: OPDS-first (sequential)

**Why**:
- OPDS is the library system integration standard
- Kiwix in-app discovery is foundational for institutional deployments
- Schools, clinics, NGOs expect OPDS support
- Extended OPDS testing reduces deployment risk

**Fallback to Tier 1**: If timeline allows and team has bandwidth, add API Gateway (June 6-12) after OPDS merges.

---

### User Priority: "I'm uncertain about priorities; minimize risk"

**→ Tier 2 recommendation**: OPDS-first (sequential)

**Why**:
- Single-feature focus eliminates parallel-execution coordination overhead
- OPDS is highest-impact feature (Kiwix discovery + library partnerships)
- 77-80 hour buffer allows for unexpected issues, extended testing, refactoring
- Sequential merging is lower-complexity git workflow
- Phase 6 can absorb API Gateway and Search (no critical sequencing dependency)

---

## Unblocking Value Analysis

### What does OPDS unblock?

**Immediate (Phase 5.2 completion)**:
- Kiwix in-app catalog discovery for end users
- One-click install for non-technical users
- Library system integration partnerships (schools, clinics, NGOs)

**Phase 6 foundation**:
- OPDS version history tracking (deletion policies, retention rules)
- Multi-language OPDS catalogs (one feed per language variant)
- Domain-specific sub-feeds (medical exports separate from educational)
- OPDS search integration (in-app search across all archives)

**Downstream projects**:
- Stockbot can integrate open-repo ZIM exports into medical training platform
- Community libraries can advertise their content through OPDS

### What does API Gateway unblock?

**Immediate (Phase 5.2 completion)**:
- Federation partner discovery (REST API for auto-discovery of exports)
- Cross-project data sharing (Stockbot, related medical platforms can consume open-repo exports)
- Automated content sync (partners can fetch latest exports on schedule)

**Phase 6 foundation**:
- Distributed peer synchronization (federation nodes can query each other's exports)
- Automated content mirroring (federation networks can maintain copies of each other's data)
- Trust and signature verification (partners authenticate via HTTP signatures)

**Downstream scaling**:
- Regional libraries can form federation networks without central authority
- Offline communities can sync content via p2p federation

### What does Search unblock?

**Immediate (Phase 5.2 completion)**:
- Offline full-text search for users with large ZIMs
- Reduced manual navigation burden for healthcare workers, researchers
- Competitive feature parity with Wikipedia offline, Project Gutenberg apps

**Phase 6 foundation**:
- Multi-language search across language boundaries
- Domain-specific ranking (medical articles ranked higher for "heart failure")
- Synonym expansion (HTN → hypertension; CVA → cerebrovascular accident)

**Downstream scaling**:
- Indexing medical domain exports improves clinical decision support
- Indexing botanical domain enables seed identification workflows

### What does A11y audit unblock?

**Immediate (Phase 5.2 completion)**:
- Audit report + remediation plan (not feature delivery)
- WCAG 2.1 AA compliance assessment
- Roadmap for Phase 6 remediation

**Phase 6 foundation**:
- Template redesign (if audit discovers structural issues)
- All Phase 6 exports inherit A11y fixes
- Expanded addressable user community (from 80% to 96%+)

**Downstream impact**:
- Government, EU institutional deployments requiring A11y compliance
- Expanded addressable user community (people with visual, motor, cognitive disabilities)

---

## Timeline Risk Analysis by Sequencing

### Tier 1: OPDS + API Gateway (Parallel) — Risk Profile

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| Phase 5.1 merge delayed past June 1 | Low | High (OPDS blocked) | Start OPDS on mock ZimExport objects; rebase once Phase 5.1 merges |
| Parallel branch merge conflict | Low | Medium (resolve + retest) | Independent module namespaces; unlikely conflict |
| OPDS takes 11h, API Gateway takes 6h (17h total) | Low | Low (71h buffer remains) | Still well within 88h window |
| Kiwix integration test discovers incompatibility | Medium | High (redesign feedgen integration) | Test early (June 4-5); fallback to xml.etree if needed |
| API Gateway HTTP signature verification fails | Low | Medium (debug + redesign) | Use Phase 4's proven signature code; test thoroughly June 3-4 |
| **Overall window overflow risk** | **Low (5%)** | — | Both features complete by June 10; 2 days buffer remains |

### Tier 2: OPDS-First (Sequential) — Risk Profile

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| Phase 5.1 merge delayed past June 1 | Low | High (OPDS blocked) | Start on mock objects; rebase once Phase 5.1 merges |
| Kiwix integration test discovers incompatibility | Medium | High (redesign required) | Test early (June 3-4); fallback to xml.etree if needed |
| OPDS takes full 11h; integration testing extends | Low | Low (55h buffer remains) | Still well within 88h window |
| **Overall window overflow risk** | **Very Low (2%)** | — | OPDS complete by June 8; 4 days buffer remains |

### Tier 3: Search-First — Risk Profile

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| **Pi 5 thermal throttling discovered June 1-2** | **High (40%)** | **Blocking (redesign required)** | **GATE: Test Pi 5 by June 1. If throttling: decide immediately — tiered index (+3h) or title-only (-2h)** |
| Indexing latency >2s per query on Pi 5 | Medium | Medium (optimize or reduce scope) | Test query performance June 5-6; optimize if needed |
| Search index adds >10% to ZIM size | Medium | Medium (negotiate scope) | Measure size June 4-5; reduce granularity if needed |
| Special character handling (accents, CJK) breaks | Low | Medium (implement Unicode support +2h) | Test June 6-7; fix before merge if needed |
| **Overall window overflow risk** | **Medium (25%)** | — | Depends on Pi 5 thermal test outcome; redesign extends to June 12 |

---

## Implementation Prerequisites (All Paths)

### Critical Gate 1: Phase 5.1 Merge (Required by June 1)

All Phase 5.2 candidates depend on Phase 5.1 being merged:

```
✓ feature/zimwriter-libzim-activation merged to main
✓ zim_exports table created and migration applied
✓ First ZIM export executed; at least one zim_exports row exists
✓ All 51 ZIM integration tests passing
✓ Manual Kiwix verification: exported ZIM opens in Kiwix
```

**If Phase 5.1 not merged by June 1**:
- OPDS: Blocked (requires ZimExport ORM); use mock objects for development
- API Gateway: Blocked (requires ZimExport ORM); use mock objects for development
- Search: Can proceed independently (integrate with ZimWriter directly)
- A11y: Can proceed independently (audit Phase 5.1 HTML template)

### Critical Gate 2: Pi 5 Thermal Validation (Required by June 1 if Search chosen)

If Search sequencing is selected, **must validate Pi 5 thermal behavior by June 1 EOD**:

```bash
# Test: Build 500-article ZIM with indexing on Pi 5
time uv run python scripts/export_to_zim.py \
  --domain medical \
  --enable-search-indexing \
  --output thermal_test.zim \
  --thermal-monitor

# Check: CPU temperature during indexing
dmesg | grep -i "thermal"
watch -n 1 'vcgencmd measure_temp'  # Raspberry Pi temperature
```

**Expected results**:
- Indexing completes in <30 minutes
- CPU temp stays <87.8°C (no thermal throttling)
- Search query latency <2 seconds

**If thermal throttling detected**: Escalate immediately; trigger redesign (tiered indexing or title-only index; adds 3-4 hours to timeline).

### Common Setup (All Candidates)

```bash
# 1. Verify Phase 5.1 merge
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
git log main --oneline | grep -i "zimwriter\|phase.5.1" | head -3

# 2. Create feature branch
git checkout -b feature/phase-5-2-{opds|search|api-gateway}

# 3. Verify database connectivity
export DATABASE_URL="postgresql+asyncpg://postgres:postgres@localhost:5432/open_repo"
alembic upgrade head
sqlite3 sqlite.db ".tables" | grep -i "zim_export"  # Verify table exists

# 4. Establish baseline test pass rate
cd projects/open-repo
uv run pytest tests/ -v --tb=short 2>&1 | tail -5
# Expected: 255+ tests passing (Phase 4 + Phase 5.1 baseline)

# 5. Start development
uv run uvicorn app.main:create_app --reload --host 127.0.0.1 --port 8000
```

---

## Daily Checkpoint Schedule

### Tier 1: OPDS + API Gateway (Parallel)

**Monday June 1**:
- [ ] Phase 5.1 merge confirmed; zim_exports table exists
- [ ] Create feature/phase-5-2-opds branch
- [ ] Create feature/phase-5-2-api-gateway branch
- [ ] OPDS: OPDSEntry.from_zim_export() skeleton created
- [ ] API Gateway: Federation export API schema drafted
- **Success**: Both branches created; baseline tests passing

**Tuesday June 2**:
- [ ] OPDS: OPDSEntry factory complete; 60% of OPDSGenerator rewrite done
- [ ] API Gateway: /api/federation/exports endpoint 70% complete
- [ ] Both: Unit tests skeleton created (failing, expected)
- **Success**: Both features on track; no blockers

**Wednesday June 3**:
- [ ] OPDS: OPDSGenerator rewrite complete; routers/opds.py 50% done
- [ ] API Gateway: Both endpoints complete; tests 80% done
- [ ] **Gate**: API Gateway integration tests passing?
- **Success**: API Gateway ready for review by day end

**Thursday June 4**:
- [ ] OPDS: routers/opds.py complete; 4 endpoints responding
- [ ] API Gateway: Code review; merge to main pending approval
- [ ] **Gate**: OPDS first endpoint responding with valid XML?
- **Success**: OPDS on track for merge June 5-6

**Friday June 5**:
- [ ] API Gateway: Merged to main; post-merge validation underway
- [ ] OPDS: Unit tests 80% done; integration test 30% done
- **Success**: API Gateway in production; OPDS final sprint begins

**Monday June 6**:
- [ ] OPDS: Unit tests 100% done (all 23 passing); integration test 60% done
- [ ] OPDS: Kiwix integration test in progress
- **Gate**: All unit tests passing? No regressions in Phase 4 tests?
- **Success**: OPDS on track for merge June 9-10

**Tuesday June 7**:
- [ ] OPDS: Integration test with kiwix-serve complete
- [ ] OPDS: Manual Kiwix Android/Desktop test complete
- [ ] OPDS: Code review underway
- **Success**: OPDS ready for merge

**Wednesday June 8**:
- [ ] OPDS: Merged to main; post-merge validation underway
- [ ] All: Staging deployment preparation
- **Success**: Both features now on main; production prep begins

**Thursday-Friday June 9-10**:
- [ ] All: Staging smoke tests
- [ ] All: Production readiness checklist
- **Success**: Production deployment approved

**Saturday-Sunday June 11-12**:
- [ ] All: Production deployment completed; 24-hour watch begins
- [ ] All: Phase 5.2 closure; documentation finalized
- **Success**: Phase 5.2 complete; Phase 6 planning begins

---

## Success Definition by Sequencing

### Tier 1 (OPDS + API Gateway) Success Criteria

By June 12, all of:
- [ ] OPDS: Kiwix Android user adds `/opds/v2/root.xml`; archives visible; Install button works
- [ ] OPDS: All 23 tests passing; no Phase 4 regressions
- [ ] API Gateway: `/api/federation/exports` returns 200 with valid JSON
- [ ] API Gateway: HTTP signature verification working; all 8+ tests passing
- [ ] Both: Production deployment complete; 0 P0 errors in first 24h
- [ ] Both: Documentation published; operational runbooks ready

**Phase 5.2 outcome**: Two complete, production-ready features; Phase 6 foundation established.

### Tier 2 (OPDS-First) Success Criteria

By June 12, all of:
- [ ] OPDS: Kiwix discovery functional; one-click install works
- [ ] OPDS: All 23 tests passing; no Phase 4 regressions
- [ ] OPDS: Production deployment complete; 0 P0 errors in first 24h
- [ ] OPDS: Documentation published; operational runbooks ready
- [ ] API Gateway: Deferred to Phase 6; not a June 12 deliverable

**Phase 5.2 outcome**: One complete, production-ready feature with extended testing; API Gateway fast-tracked for Phase 6.

### Tier 3 (Search-First) Success Criteria

By June 12, all of:
- [ ] Pi 5 thermal test complete; no throttling or redesign path confirmed
- [ ] Search: ZIM file built with embedded full-text index; Kiwix search bar functional
- [ ] Search: Queries return <2s latency; results ranked correctly
- [ ] Search: All tests passing; index adds <10% to ZIM size
- [ ] Search: Production deployment complete; 0 P0 errors in first 24h
- [ ] Search: Documentation published; operational runbooks ready

**Phase 5.2 outcome**: One complete, production-ready feature; validated on Pi 5 hardware.

---

## Implementation Rollback Procedure (If Critical Issues Found)

If a feature encounters critical issues during implementation, execution may be paused to:
1. Fix the issue (if timeline allows)
2. Defer feature to Phase 6 (if fix exceeds remaining buffer)

### Rollback decision gate (applies to all candidates):

**If issue discovered before June 8**:
- Attempt fix if estimated effort <2 hours
- If fix extends beyond 2 hours: defer to Phase 6; redeploy buffer hours to another candidate

**If issue discovered June 8+**:
- Only fix if critical to production (P0 security, data corruption risk)
- Otherwise: defer to Phase 6; preserve timeline

### Example rollback scenarios:

**Scenario A**: OPDS Kiwix integration fails June 5
- Fix attempt: Revert to xml.etree fallback; retest (2 hours)
- Outcome: OPDS delays to June 6-10; API Gateway still merges June 5

**Scenario B**: Search Pi 5 thermal throttling June 2
- Fix attempt: Implement tiered indexing (3-4 hours)
- Outcome: Search delays to June 8-12; tight but feasible

**Scenario C**: API Gateway HTTP signature fails June 4
- Fix attempt: Debug with Phase 4 reference code (1-2 hours)
- Outcome: API Gateway reschedules to June 4-6; OPDS unaffected

---

## Conclusion & Next Steps

**Decision required by May 26 (today)**:

1. **Which Tier sequencing aligns with your priorities?**
   - Tier 1 (OPDS + API Gateway parallel): Maximum Phase 5.2 impact, well-managed risk
   - Tier 2 (OPDS-first sequential): Single-feature focus, maximum buffer, safest path
   - Tier 3 (Search-first): User-focused, contingent on Pi 5 validation

2. **If Tier 3 (Search) selected: Has Pi 5 thermal testing been scheduled for June 1?**
   - If yes: Proceed with Tier 3 planning
   - If no: Defer Search to Phase 6; recommend Tier 1 or Tier 2

3. **Who owns each feature branch during parallel execution (Tier 1)?**
   - OPDS owner: [assign developer]
   - API Gateway owner: [assign developer]
   - Code review owner: [assign reviewer]

4. **What is the escalation path if a feature hits critical issues mid-development?**
   - Critical issues (P0): Fix immediately; extend timeline if necessary
   - High issues (P1): Fix if <2 hour effort; else defer to Phase 6
   - Medium issues (P2): Defer to Phase 6; keep Phase 5.2 timeline

**Once decision is made**, implementation begins immediately June 1. All deliverables (code, tests, documentation) will be production-ready by June 12, 2026.

---

**Document status**: Ready for execution  
**Date prepared**: 2026-05-26 10:45 UTC  
**Next review**: June 1 (post-Phase-5.1-merge verification)  
**Final delivery target**: June 12, 2026 23:59 UTC
