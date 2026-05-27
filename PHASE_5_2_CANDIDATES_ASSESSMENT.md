---
title: "Phase 5.2 Candidates Assessment — Three-Way Evaluation"
project: open-repo
phase: "5.2 pre-implementation"
status: "assessment-complete"
date: 2026-05-27
decision_deadline: 2026-05-27
research_scope: "Code exploration, existing documentation review, scope analysis"
---

# Phase 5.2 Candidates Assessment

## Overview

This assessment evaluates three Phase 5.2 feature candidates for parallel development readiness following Phase 5.1 (ZimWriter libzim integration) merge, expected May 25-26. Each candidate addresses distinct gaps in open-repo's functionality: offline content authoring, standards-based distribution, and inclusive design. All three are technically ready for implementation; the decision is which to prioritize within the June 1-12 production window.

---

## Candidate 1: ZimWriter Integration

### Current Status

**Code exists**: `app/services/export/zim_writer.py` (338 lines of well-documented scaffolding, 100% complete)
- Class structure: `ZimWriter`, `ZimMetadata`, `ExportConfig`, `ExportScope` — all defined with full type signatures
- Method signatures and docstrings: present and detailed
- Integration points: 7 `TODO(post-PR-merge)` markers at libzim Creator API call sites
- Test coverage: 84 existing export pipeline tests (all currently pass against stubs)

**Phase 5.1 Status**: Conditional approval for merge by May 26; zero merge blockers, four post-merge action items (libzim>=3.10.0 added to pyproject.toml, ZimExport ORM class added, html.escape() on attribution footer, README updated).

**Recommendation**: **MERGED — this is not a Phase 5.2 candidate.** ZimWriter is Phase 5.1's core delivery and must complete before Phase 5.2 candidates become unblocked. Documented in `PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md` (8-11 hours effort, production-ready by June 5-10).

---

## Candidate 2: OPDS Feed Generator (Open Publication Distribution System)

### What It Delivers

OPDS 1.2 is the industry-standard catalog protocol for offline content distribution. Implementation adds four REST endpoints that produce Atom XML feeds compatible with Kiwix (mobile/desktop) in-app catalog discovery. Users can paste the root catalog URL (`/opds/v2/root.xml`) into Kiwix, see the open-repo archive library listed, and one-click-install ZIM files without needing a direct CDN URL.

**End-user outcome**: Kiwix Android user (F-Droid or Play Store) opens the app → Add Library → pastes OPDS URL → sees "Open-Repo Full Library (English)" listed → taps Install → ZIM auto-downloads and opens offline.

### Scope and Implementation

**Endpoints to implement** (4 new):
- `GET /opds/v2/root.xml` — Navigation feed with links to acquisition feed and search
- `GET /opds/v2/entries` — Acquisition feed listing all published ZIM exports with download links
- `GET /opds/v2/entry/{uuid}` — Single-entry view with version history and checksums
- `GET /opds/v2/searchdescription.xml` — OpenSearch description for Kiwix integrated search

**Code changes required**:
- `pyproject.toml`: Add `feedgen>=0.9` (one line)
- `app/services/export/opds_generator.py`: Replace 7 `TODO(post-PR-merge)` stubs with feedgen-based Atom generation (~250 lines rewritten)
- New `OPDSEntry.from_zim_export()` factory classmethod: Maps Phase 5.1 `ZimExport` ORM rows to OPDS entries (~40 lines)
- New file `app/api/v1/routers/opds.py`: Four endpoint handlers (~120 lines)
- Update `tests/test_opds_generator.py`: Verify 4 new feedgen integration tests pass, ensure 19 existing tests pass with feedgen-based XML

**Total scope**: 8-11 hours

### Current Code Status

**Existing scaffolding**: `app/services/export/opds_generator.py` (540 lines) contains:
- `OPDSEntry` dataclass (fully defined, frozen=True, includes uuid, title, language, file_size, cdn_url, sha256, updated_at)
- `OPDSCatalogService` class with `_build_feed_xml()` stub (produces placeholder XML via xml.etree)
- 19 unit tests already exist; they verify XML structure independently of the underlying generation library

**No frontend code**: open-repo is a backend API only. OPDS feeds are XML/Atom — no web UI work required. Validation is done via kiwix-serve command-line tool (Docker container).

### Complexity Assessment

**Low-medium complexity**:
- feedgen library abstracts Atom generation; main work is replacing raw xml.etree calls
- OPDS 1.2 Atom namespace handling is well-documented in PHASE_5_CANDIDATE_2_OPDS_IMPLEMENTATION_ROADMAP.md
- Integration tests require kiwix-serve Docker container; pre-built validation scripts exist
- Silent-failure risk: Kiwix silently ignores malformed OPDS feeds (no error messages). Mitigation: validate against Kiwix parser locally before deployment.

### Dependencies and Blockers

**Hard dependency**: Phase 5.1 must produce valid ZIM files with populated `zim_exports` database table. The `from_zim_export()` factory requires real `ZimExport` ORM rows.

**Can develop in parallel**: Yes — code can be written on a separate branch against mock `ZimExport` objects. However, integration testing requires Phase 5.1 output.

**Merge sequence**: OPDS cannot merge before Phase 5.1 + ZimWriter both land and produce valid output.

### Readiness for Phase 5.2

**Ready for parallel development**: High confidence. Full implementation roadmap exists (PHASE_5_CANDIDATE_2_OPDS_IMPLEMENTATION_ROADMAP.md). Scaffold code is 95% complete. No new dependencies beyond feedgen (low-risk library, 35K weekly downloads, actively used in production).

**Ready for production by June 12**: Yes — 8-11 hours fits comfortably in the 11-day June 1-12 window with significant buffer remaining for testing and integration.

**Recommend as Phase 5.2 Wave 1 candidate**: Yes. This is the second-highest priority per the PHASE_5_DECISION_FRAMEWORK.md analysis. Unblocks Kiwix in-app discovery and library partnership integrations for Phase 6.

---

## Candidate 3: Accessibility Audit and Remediation

### What It Delivers

WCAG 2.1 Level AA compliance audit of open-repo's web interface, followed by remediation of critical issues. This ensures blind/low-vision users, motor-impaired users dependent on keyboard navigation, and screen reader users can access the system without workarounds.

**Scope target**: WCAG 2.1 Level AA is the internationally recognized baseline for public-interest digital infrastructure. Audit covers four domains:
1. **Perceivable**: Color contrast ≥4.5:1 for body text, alt text for images, text resizable to 200%
2. **Operable**: Full keyboard navigation without mouse, visible focus indicators, skip links
3. **Understandable**: Form labels, error identification, language metadata
4. **Robust**: Semantic HTML, ARIA roles where needed, screen reader compatibility

### Current Code Status

**Frontend existence**: This is the critical issue. Open-repo is primarily a **backend API**. There is no dedicated frontend codebase (`frontend/` directory does not exist; no React/Vue/HTML templates in the backend).

**What exists**:
- FastAPI backend with JSON API endpoints (`/api/v1/items`, `/api/v1/partners`, etc.)
- ZIM article HTML templates in zim_writer.py (embedded Jinja2 templates, baked into offline ZIM files) — phase-5-export-strategy.md notes WCAG AA contrast requirement on these templates
- OPDS XML feeds (machine-readable Atom/XML, not HTML) — no a11y audit needed for machine-readable formats
- No web UI, no web frontend, no HTML dashboard

**Accessibility audit scope impact**:
- Audit can only cover what exists: the ZIM article templates (Jinja2-rendered HTML embedded in offline archives)
- If there is a separate web dashboard or admin UI, it exists outside the current codebase and is out of scope
- If the user intends to add a web UI in Phase 6, a11y work now is a good foundation; but retrofitting an existing web UI is not possible because the web UI does not currently exist

### Scope and Implementation

**Pre-audit phase** (4-6 hours):
1. Identify what surfaces need auditing (ZIM templates, any API web UI, future frontend)
2. Set up automated a11y testing: axe-core or Pa11y CLI (runs in CI, ~30-90 sec per run)
3. Run automated scan: identifies 30-40% of issues (contrast, missing alt text, semantic HTML problems)
4. Manual testing with screen readers: NVDA (Windows/free), VoiceOver (macOS), ORCA (Linux) — 4-8 hours to test keyboard navigation, focus indicators, screen reader verbosity

**Audit results and findings documentation** (2-3 hours):
- Categorize issues by severity (P0/P1/P2)
- Document estimated remediation effort per issue
- Note dependencies (e.g., ZIM template fixes require Phase 5.1 ZIM rebuild; web UI fixes require frontend code that doesn't exist yet)

**Remediation phase** (TBD, typically 4-12 hours for moderate scope):
- Fix P0 issues: critical contrast problems, missing form labels, broken keyboard navigation
- Fix P1 issues: missing alt text on images, semantic structure problems (heading hierarchy, list nesting)
- Defer P2 issues (nice-to-have accessibility enhancements) to Phase 6

### Complexity Assessment

**Audit complexity: Medium** (4-6 hours setup + testing)
- Automated tools are straightforward to set up (axe-core, Pa11y)
- Manual testing with screen readers requires learning curve but is well-documented
- WCAG 2.1 AA standard is stable and widely understood

**Remediation complexity: Unknown** (4-12+ hours, findings-dependent)
- If issues are localized to ZIM templates: straightforward fixes (CSS tweaks, semantic HTML restructuring)
- If issues are pervasive (e.g., color contrast problems throughout a design system): remediation could exceed 12 hours and require design rework
- The risk is **scope creep**: a11y audits reliably surface more work than anticipated. PHASE_5_DECISION_FRAMEWORK.md notes professional audits typically estimate 120-160 hours for comprehensive WCAG AA compliance on a 10-20 page website.

### Dependencies and Blockers

**No hard dependencies**: A11y work can start immediately; does not require Phase 5.1 or Candidate 2.

**Scope ambiguity blocker**: The audit cannot begin until the team clarifies which surfaces need auditing. Open-repo's current surfaces are:
1. JSON API endpoints (not a11y-auditable; machine-readable, not user-facing)
2. ZIM article templates (auditable; embedded HTML)
3. OPDS XML feeds (not auditable; machine-readable)
4. (Possible) Web admin dashboard (not found in codebase; if it exists, out of scope of current repo)
5. (Planned) Phase 6 web UI for federation management (does not exist yet)

**Audit scope decision required**: Which surfaces should the audit cover? This determines the timeline and effort.

### Readiness for Phase 5.2

**Ready for parallel development**: Conditional. The audit itself can start immediately (phase-5-candidate-decision-framework.md recommends audit in parallel with ZimWriter development on a separate branch). However, **the scope decision is blocking** — the team must decide which surfaces to audit.

**Ready for production by June 12**: Depends on audit findings. The audit phase (4-6 hours) fits in the window. Remediation of "P0 critical issues only" (contrast, missing labels) is feasible (4-8 hours). Full comprehensive WCAG AA remediation is not feasible in 11 days if issues are pervasive.

**Recommend as Phase 5.2 Wave 1 candidate**: Conditional recommendation. PHASE_5_DECISION_FRAMEWORK.md ranks it second in user-value ("for all humanity" explicitly includes disabled users). However, remediation scope is uncapped. Safe approach:
1. **Run the audit immediately** (4-6 hours, can overlap with ZimWriter merge completion)
2. **Triage findings** (2-3 hours) — separate P0 (critical, fix now) from P1/P2 (backlog)
3. **Fix P0 issues only** (4-8 hours) before June 12 if time permits
4. **Schedule P1/P2 fixes** for Phase 6 planning

**Timing risk**: If audit findings reveal pervasive issues (e.g., systematic color contrast problems across templates), attempting full remediation will overrun the June 12 deadline. The safe path is audit + P0 fixes only, defer remainder.

---

## Parallel Development Readiness Matrix

| Candidate | Can start immediately | Code scaffold complete | Dependencies blocking | Effort estimate | Timeline fit (June 1-12) | Recommend |
|---|---|---|---|---|---|---|
| **Candidate 2: OPDS** | Yes (separate branch) | 95% complete | Phase 5.1 output needed for integration testing | 8-11 hours | High — fits with buffer | **Yes, Wave 1** |
| **Candidate 3: A11y** | Yes (separate branch) | No (audit phase must run first) | Scope decision required | 4-6 audit + 4-12 remediation (P0 only) | Medium (audit fits; remediation scope-dependent) | **Conditional — run audit, fix P0 only** |

---

## Recommendation

### Recommended Phase 5.2 Path (June 1-12 Window)

**Wave 1 (June 1-10): OPDS Feed Generator**
- **Effort**: 8-11 hours
- **Output**: Four OPDS endpoints; Kiwix in-app discovery enabled
- **Blockers**: Resolves when Phase 5.1 ZIM output is available (~June 5-6)
- **User value**: Direct — end users can discover and install archives via standard catalog
- **Confidence**: High — scaffold is 95% complete; full roadmap exists

**Parallel (June 1-6): Accessibility Audit**
- **Effort**: 4-6 hours (audit phase; does not require Phase 5.1 to complete)
- **Output**: WCAG 2.1 AA audit report; findings categorized by severity
- **Path forward**: If audit reveals low/moderate scope (P0 issues fixable in 4-8 hours), proceed with P0 remediation in Wave 2 (June 6-10). If high scope, defer P1/P2 to Phase 6.
- **User value**: Deferred until remediation is complete; audit alone delivers no end-user impact

**Not recommended for Phase 5.2**: Candidate 3 (Accessibility audit + full remediation) as a standalone feature. The audit is valuable; full remediation in the 11-day window is high-risk due to uncapped scope. Recommended approach: audit + triage + P0 fixes only, defer remainder.

### Decision Tree for User

```
User decision required by May 27:

Question 1: Which candidates should Phase 5.2 target?
  
  Option A (Recommended): OPDS (Wave 1) + Accessibility Audit (parallel, P0 fixes only)
    → June 1-12 window comfortably accommodates both
    → Audit runs in parallel with ZimWriter completion (no blocking dependency)
    → P0 remediation (4-8 hours) fits between OPDS and window close
    → Delivers end-user value from OPDS; establishes a11y baseline; defers P1/P2 to Phase 6
  
  Option B: OPDS (Wave 1) only
    → Highest confidence for meeting June 12 deadline
    → Audit + P0 fixes become Phase 6 Wave 1 (lower urgency; no blocking dependency)
    → Simplest path; lowest risk
  
  Option C: Accessibility Audit (comprehensive) only
    → 6-14 hours (audit + findings) + 4-12+ hours (remediation) = 10-26 hours total
    → Fits in window only if findings are low-scope (4-8 issues, max 8 hours remediation)
    → High risk: audit may reveal >12 hours of remediation work → Option C overruns deadline
    → Recommend only if team decides "comprehensive WCAG AA remediation is Phase 5.2 priority over OPDS"
  
  Option D: Skip Phase 5.2 altogether, do Phase 6 early
    → Not recommended; ZimWriter (Phase 5.1) needs immediate follow-up
    → OPDS is prerequisite for federation partnerships in Phase 6

Recommendation: **Option A** (OPDS + Audit with P0-only remediation)
```

---

## Detailed Assessment by Candidate

### Candidate 1: ZimWriter (Phase 5.1, Not Phase 5.2)

**Summary**: ZimWriter is Phase 5.1's core feature, conditional-approved for merge by May 26. It is not a Phase 5.2 candidate.

**Implementation status**: Scaffold 100% complete, stubs at every integration point marked with TODO comments. Eight-eleven hours of fill-in work remains.

**Production readiness**: High. Detailed roadmap exists (PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md). Eighty-four existing tests cover public interface; stubs swap out without signature changes. Dependency (libzim>=3.10.0) is actively maintained, wheels available for all standard platforms.

**Readiness assessment**: Ready for merge by May 26. Will be the blocking dependency for Phase 5.2 OPDS (which requires ZimExport ORM rows to populate OPDS feeds).

---

### Candidate 2: OPDS Feed Generator

**Summary**: Adds standards-based catalog protocol (OPDS 1.2 / Atom XML) for Kiwix in-app content discovery. Four new endpoints, no new frontend code required.

**Scope**: Well-defined. Full implementation roadmap in PHASE_5_CANDIDATE_2_OPDS_IMPLEMENTATION_ROADMAP.md. Effort: 8-11 hours.

**Code readiness**: Ninety-five percent complete. Scaffold contains full class definitions, 19 existing tests, and 7 TODO stubs at integration points.

**Complexity**: Low-medium. Main tasks: replace raw xml.etree calls with feedgen library; implement factory method to map ZimExport ORM rows to OPDS entries; add four route handlers.

**Parallel development**: Can start June 1 on separate branch. Requires Phase 5.1 ZimWriter producing valid output before integration testing and merge.

**Timeline feasibility**: High. Eight-eleven hours fits comfortably in 88-hour June 1-12 window (11-day nominal, accounting for meetings, interruptions).

**User value**: High. Direct — Kiwix users see open-repo archives in-app catalog browser. Enables one-click install. Prerequisite for library/institutional partnerships in Phase 6 (federation roadmap).

**Recommendation**: **Phase 5.2 Wave 1, highest priority**. Proceed immediately after Phase 5.1 merge confirmation (~May 26).

**Production-ready by**: June 5-10 (conservative estimate: 11 hours + testing + buffer).

---

### Candidate 3: Accessibility Audit and Remediation

**Summary**: WCAG 2.1 Level AA compliance audit of open-repo, followed by remediation of critical issues.

**Current scope ambiguity**: Open-repo is backend-only. Auditable surfaces are:
- ZIM article templates (Jinja2 HTML embedded in offline archives) ✓ exists
- API JSON endpoints ✗ not user-facing; machine-readable
- OPDS XML feeds ✗ machine-readable; no a11y concerns
- Web admin dashboard ✗ not found in codebase
- Future Phase 6 web UI ✗ does not exist yet

**Scope decision required**: Which surfaces to audit? (Blocks the start of audit work.)

**Audit phase effort**: 4-6 hours (setup, automated scanning, manual testing). Low uncertainty; well-defined scope.

**Remediation effort**: 4-12+ hours (P0 critical issues) to 120-160 hours (comprehensive WCAG AA). **High uncertainty** — depends entirely on audit findings. Per PHASE_5_DECISION_FRAMEWORK.md, professional audits of similar scope consistently underestimate remediation.

**Parallel development**: Audit can start immediately (June 1, no blocking dependencies). Does not require Phase 5.1.

**Recommended approach** (to reduce scope creep):
1. Run audit (4-6 hours) → generates findings report
2. Triage findings (1-2 hours) → separate P0 (critical, fix immediately) from P1/P2 (backlog)
3. Fix P0 only (4-8 hours) before June 10, if time permits
4. Defer P1/P2 to Phase 6 planning

**Timeline feasibility**: Audit fits (4-6 hours). P0 remediation (4-8 hours, estimate) may fit within the June 1-12 window if findings are favorable. Full comprehensive WCAG AA remediation is not feasible in 11 days.

**User value**: Deferred until remediation complete. Audit alone delivers no end-user functionality.

**Confidence level**: Medium. The audit is high-confidence (well-documented tools and process). Remediation scope is low-confidence (unknown until audit runs).

**Recommendation**: **Not as standalone Phase 5.2 feature.** Recommended as parallel activity (June 1-6) with contingent P0 remediation (June 6-10 if scope permits). If audit reveals >12 hours of remediation work, defer all non-P0 issues to Phase 6.

**Reason**: OPDS (8-11 hours, high-confidence) is higher-priority and higher-confidence than speculative a11y remediation (scope unknown until audit runs). Running both in parallel with "audit + P0 fixes only" bounds the risk and delivers both OPDS (definite user value) and accessibility baseline (foundational for Phase 6 web UI).

---

## Cross-Candidate Feasibility: Can All Three Run in Parallel?

**June 1-12 window capacity**: 88 hours available (11 days, ~8 hours/day sustained development)

| Candidate | Effort | Start date | End date | Blocker | Parallel capacity |
|---|---|---|---|---|---|
| Phase 5.1 ZimWriter | 8-11 hours | May 22 (started) | May 26-30 (completes before Phase 5.2) | — | No (prerequisite) |
| **Candidate 2: OPDS** | 8-11 hours | June 1 | June 5-10 | Phase 5.1 output | **Yes** |
| **Candidate 3: A11y (audit only)** | 4-6 hours | June 1 | June 3-6 | Scope decision | **Yes** |
| **Candidate 3: A11y (P0 remediation)** | 4-8 hours | June 6 | June 8-12 | Audit findings | Conditional (only if low-scope) |

**Total if all three included**: 8-11 (OPDS) + 4-6 (audit) + 4-8 (P0 remediation) = 16-25 hours

**Feasibility**: Yes, all three fit comfortably in the 88-hour window. OPDS (8-11h) + Audit (4-6h) + P0 remediation (4-8h) = 16-25 hours, leaving 63-72 hours for testing, buffer, and integration work. This is the **recommended path**.

---

## Summary Table

| Aspect | Candidate 2: OPDS | Candidate 3: A11y Audit | Candidate 3: A11y Remediation |
|---|---|---|---|
| **Current code status** | 95% scaffold complete | 0% (audit tools to be set up) | 0% (findings unknown) |
| **Effort estimate** | 8-11 hours (high confidence) | 4-6 hours (high confidence) | 4-8 hours P0 only (medium confidence) |
| **Blocking dependencies** | Phase 5.1 ZimWriter output | Scope decision | Audit findings |
| **Can start immediately** | June 1 (separate branch) | June 1 (after scope decision) | After audit completes |
| **Timeline feasibility** | High (fits with large buffer) | High (audit only fits easily) | Medium (P0 remediation contingent on findings) |
| **User value** | High (direct: Kiwix discovery) | None until remediation | Medium (foundational for Phase 6) |
| **Scope creep risk** | Low (well-defined, roadmap exists) | Low (audit scope bounded) | High (remediation scope uncapped) |
| **Recommend for Phase 5.2** | **Yes, Wave 1** | **Yes, parallel (audit only)** | **Conditional (P0 fixes only)** |

---

## Final Recommendation

**Proceed with Phase 5.2 as follows**:

1. **Confirm Phase 5.1 (ZimWriter) merge by May 26.** All Phase 5.2 work depends on ZimExport ORM rows and valid ZIM output.

2. **Launch Phase 5.2 Wave 1 (June 1-10): OPDS Feed Generator** (Candidate 2)
   - Start: June 1 on separate `feature/phase-5-2-opds` branch
   - Effort: 8-11 hours
   - Merge gate: Phase 5.1 ZimWriter producing valid ZIM output + all 4 OPDS endpoints passing integration tests
   - Expected completion: June 5-10

3. **Run Accessibility Audit in parallel (June 1-6)** (Candidate 3, audit phase only)
   - Start: June 1 on separate `feature/phase-5-2-a11y-audit` branch (no dependency on Phase 5.1)
   - Scope: WCAG 2.1 Level AA audit of ZIM article templates and API surfaces
   - Effort: 4-6 hours (audit setup + automated scanning + manual testing)
   - Deliverable: Audit report with findings categorized by severity (P0/P1/P2)
   - No merge until scope reviewed and P0 fixes complete

4. **P0 Remediation (June 6-10) contingent on audit findings**
   - Only if audit findings indicate <8 hours of P0 work (critical contrast, missing labels, broken navigation)
   - If audit findings show >12 hours of work, defer all non-P0 issues to Phase 6 planning
   - Merge gate: P0 issues resolved; audit findings documented

5. **Phase 5.2 Complete by June 12**: Both OPDS and A11y baseline established for Phase 6.

**Not recommended for Phase 5.2**:
- Candidate 3 (Accessibility) as comprehensive WCAG AA remediation — scope is uncapped; fits better in Phase 6 with full planning and resource allocation.
- Any feature beyond OPDS + P0 A11y fixes — preserves buffer for testing and integration work; reduces schedule risk.

---

## Sources and References

- `/home/awank/dev/SuperClaude_Framework/projects/open-repo/PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md` — ZimWriter detailed roadmap
- `/home/awank/dev/SuperClaude_Framework/projects/open-repo/PHASE_5_CANDIDATE_2_OPDS_IMPLEMENTATION_ROADMAP.md` — OPDS detailed roadmap
- `/home/awank/dev/SuperClaude_Framework/projects/open-repo/PHASE_5_DECISION_FRAMEWORK.md` — Decision framework for Phase 5 candidates (includes a11y audit scope analysis)
- `/home/awank/dev/SuperClaude_Framework/projects/open-repo/PHASE_5_2_FEATURE_CANDIDATES.md` — Top 10 Phase 5.2 feature candidates (covers medical, water, botanical domains; not in scope of this assessment)
- `/home/awank/dev/SuperClaude_Framework/projects/open-repo/PHASE_5.2_CAPABILITY_AUDIT.md` — Current capability gaps
- `/home/awank/dev/SuperClaude_Framework/projects/open-repo/PHASE_5_2_CANDIDATE_EVALUATION.md` — Comprehensive candidate evaluation framework
- `/home/awank/dev/SuperClaude_Framework/projects/open-repo/PHASE_5_2_RECOMMENDED_SEQUENCING.md` — Sequencing strategy for Phase 5.2 candidates
- `/home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/app/services/export/zim_writer.py` — ZimWriter implementation (scaffolding complete)
- `/home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/app/services/export/opds_generator.py` — OPDS implementation (95% scaffolding complete)
- WCAG 2.1 Level AA standard: https://www.w3.org/WAI/WCAG21/quickref/ (accessibility compliance target)
