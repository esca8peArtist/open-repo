---
title: "Phase 5 Candidate Decision Matrix — Quick Selection Guide"
project: open-repo
date: 2026-05-19
status: "ready for user decision"
decision_needed_by: "2026-05-20 morning"
---

# Phase 5 Candidate Decision Matrix

**Your decision needed by: May 20 morning (tomorrow)** to enable immediate Phase 5 launch.

---

## One-Minute Summary

| Candidate | User Value | Complexity | Timeline | Go/No-Go |
|-----------|------------|-----------|----------|----------|
| **1: ZimWriter** | Users in low-bandwidth regions can download and read the entire open-repo knowledge base offline (50–80 MB, any device, no internet) | LOW — scaffold 100% complete, fill-in exercise | 8–11 hours | ✅ **GO** (prerequisite for everything else) |
| **3: Accessibility Audit** | Blind/low-vision/motor-impaired users can actually use the system; equal access for all humanity | HIGH — audit is bounded, remediation scope is unknown | 18–36 hours (scope-dependent) | ⚠️ **CONDITIONAL** (depends on post-audit prioritization) |
| **2: OPDS Feed Migration** | Kiwix app users can discover and one-click-install archives from within the app (cleaner discoverability) | MEDIUM — feedgen API is straightforward, but namespace handling has silent-failure modes | 8–11 hours (depends on Candidate 1 first) | ⏳ **DEFER** (only after ZimWriter) |

**Recommended path**: **ZimWriter first** (mandatory), then decide between Accessibility (if inclusive design is priority) vs OPDS (if user discovery is priority).

---

## Decision Matrix: Implementation Readiness

### Candidate 1: ZimWriter (Recommended First)

**The Ask**: Replace stub implementations in `zim_writer.py` with real libzim.writer calls.

| Question | Answer | Impact |
|----------|--------|--------|
| **Can I start immediately?** | ✅ YES — scaffold is 100% complete, no blockers | All 84 existing tests already cover the public interface |
| **Do I need infrastructure changes?** | ✅ NO — schema ready, database ready, pipeline ready | One-line dependency addition: `libzim>=3.2,<4.0` |
| **Is there a fallback if something breaks?** | ✅ YES — if libzim doesn't work, ZIP export of HTML files provides offline access | Worst-case: 30-second revert, zero user impact |
| **Will it unblock other work?** | ✅ YES — OPDS (Candidate 2) depends on this producing valid ZIM output | This is the prerequisite. Everything else is downstream. |
| **Timeline risk?** | ✅ LOW — complete scaffolding + no unknowns = high predictability | 8–11 hours is well within the May 19–June 5 window |
| **What's the user outcome?** | ✅ DIRECT — "offline access for all humanity" = core mission | Users in low-bandwidth regions, field workers, disaster responders can read open-repo without internet |

**Decision**: **IMMEDIATE GO** — This is the prerequisite for the entire Phase 5 work. All downstream candidates depend on it.

**Immediate next step after approval**:
1. Create branch: `git checkout -b feature/zimwriter-integration`
2. Add dependency: edit `pyproject.toml`, add `libzim>=3.2,<4.0`
3. Replace stubs: 4 main calls in `zim_writer.py` (add_article, add_image_resource, enable indexing, zimcheck)
4. Verify: run `uv run pytest tests/export/` — all 84 tests should pass
5. Manual test: export a small archive, open in Kiwix Android (F-Droid), verify offline read
6. Create PR, merge to main

---

### Candidate 2: OPDS Feed Migration (Conditional: After ZimWriter)

**The Ask**: Migrate from hardcoded `xml.etree` to feedgen library for cleaner OPDS catalog generation.

| Question | Answer | Impact |
|----------|--------|--------|
| **Can I start immediately?** | ⏳ CONDITIONAL — must wait for ZimWriter to land first (Candidate 1) | This depends on Candidate 1 producing valid ZIM exports |
| **Do I need infrastructure changes?** | ✅ NO — only code changes, no schema migrations | One-line dependency addition: `feedgen>=0.9` |
| **Is there a fallback if something breaks?** | ✅ YES — revert to raw `xml.etree` (already proven working) | Zero user impact, just less elegant code |
| **Will it unblock other work?** | ⚠️ MEDIUM — improves user discovery but not essential | ZimWriter matters more; OPDS is polish |
| **Timeline risk?** | ⚠️ MEDIUM — feedgen has inactive maintenance (no PyPI release in 12+ months); namespace handling can silently fail | 8–11 hours if no surprises, but debugging Kiwix catalog parsing is slow |
| **What's the user outcome?** | ⚠️ MEDIUM — Kiwix app users can one-click-install from the in-app catalog instead of copy-pasting a URL | Discoverability improvement, not essential functionality |

**Decision**: **SECONDARY PRIORITY** — defer until after ZimWriter lands and proves it generates valid ZIM output. Then revisit for Phase 5 Phase 2 (late May or early June).

**Implementation checklist (ready when you want it)**:
- [ ] Candidate 1 (ZimWriter) merged and tested
- [ ] Rewrite `_build_feed_xml()` using feedgen API (2–3 hours)
- [ ] Implement `OPDSEntry.from_zim_export()` factory (1–2 hours)
- [ ] Add missing OPDS 1.2 elements: `dc:language`, `dc:issued`, `opensearch`, version-history (1–2 hours)
- [ ] Update 19 existing OPDS tests (1 hour)
- [ ] Validate feed format against Kiwix catalog parser (1 hour)
- [ ] PR review + merge

---

### Candidate 3: Accessibility Audit (Conditional: Design Priority)

**The Ask**: Audit the codebase for WCAG 2.1 Level AA compliance (international standard for accessible digital infrastructure). Scope: ZIM article HTML template + web API responses.

| Question | Answer | Impact |
|----------|--------|--------|
| **Can I start immediately?** | ✅ YES — no blockers | But scope unknown until audit runs |
| **Do I need infrastructure changes?** | ✅ YES — CI integration for automated a11y testing (axe-core via Playwright) | Adds 30–90 seconds to each CI run |
| **Is there a fallback if something breaks?** | ⚠️ PARTIAL — audit findings are just findings; you decide which fixes are critical vs backlog | Audit itself is low-risk; remediation scope is unknown |
| **Will it unblock other work?** | ❌ NO — this is parallel work, not a prerequisite | Can run alongside ZimWriter/OPDS |
| **Timeline risk?** | ⚠️ HIGH — audit phase is predictable (4–6 hours), but remediation scope depends on findings (4–12 hours for critical fixes) | Scope creep is the primary risk in the May 19–June 5 window |
| **What's the user outcome?** | ✅ HIGH IMPACT — blind, low-vision, motor-impaired users can actually use open-repo without workarounds | "For all humanity" explicitly includes disabled users |

**Decision**: **DESIGN PRIORITY** — do this if inclusive design is a stated priority. Otherwise, defer to Phase 6.

**Two-path approach**:
1. **Path A (Inclusive Design Priority)**: Run audit now, commit to fixing **critical findings only** (contrast, missing labels, semantic HTML) in the May 19–June 5 window. Backlog non-critical findings (nice-to-have ARIA, minor layout improvements).
2. **Path B (Feature Priority)**: Defer audit to Phase 6. Focus May 19–June 5 on ZimWriter + OPDS.

**Implementation checklist (if Path A is chosen)**:
- [ ] Set up axe-core in Playwright (2–4 hours)
- [ ] Run automated scan against ZIM article template + API response surfaces (1–2 hours)
- [ ] Manual keyboard-only navigation testing (4–6 hours)
- [ ] Manual screen reader testing (NVDA on Windows, VoiceOver on macOS) (4–8 hours)
- [ ] Triage findings into critical/non-critical (1 hour)
- [ ] Fix critical findings only: contrast, missing `alt` text, semantic HTML (4–12 hours depending on audit results)
- [ ] Write regression tests to prevent regressions (2–3 hours)
- [ ] PR review + merge

---

## Quick Decision Guide

**If your answer is YES to any of these, pick that path:**

| If... | Then... |
|------|---------|
| **"I want offline access to open-repo for users without internet"** | → **ZimWriter (Candidate 1)** — DO THIS FIRST |
| **"I want blind and low-vision users to have equal access"** | → **Accessibility Audit (Candidate 3)** — Optional but high-impact |
| **"I want Kiwix app users to discover open-repo from within the app"** | → **OPDS Migration (Candidate 2)** — DO THIS AFTER ZimWriter |
| **"I want to maximize user outcomes per hour spent"** | → **ZimWriter + Accessibility** — Both high-impact, Accessibility unblocks disabled users |

**Recommended sequence**:
1. **Phase 5a (Immediate)**: Approve ZimWriter → I build it (8–11 hours) → merge by May 25
2. **Phase 5b (June)**: Decide on Accessibility OR OPDS → I build it (8–11 hours) → merge by June 5

---

## How to Decide: Yes/No Questions

Answer these three questions:

### Q1: Is offline access (ZimWriter) a priority?
- **YES** → Approve ZimWriter immediately. This is the prerequisite.
- **NO** → Unusual, but you can defer. OPDS and Accessibility work independently.

### Q2: Is inclusive design (Accessibility) important to you?
- **YES** → Add Accessibility to the Phase 5 roadmap. Can run alongside ZimWriter.
- **NO** → Skip for now. You can backfill later without breaking anything.

### Q3: Is user discoverability (OPDS) a priority for this phase?
- **YES, and I approved ZimWriter** → Add OPDS to Phase 5b (early June, after ZimWriter lands).
- **NO or unsure** → Skip for now. OPDS is nice-to-have, not essential.

---

## What Happens Next (Timeline)

**If you approve ZimWriter immediately** (recommended):
- **May 19–20**: You decide. I await your approval.
- **May 20–22**: I implement ZimWriter (8–11 hours)
- **May 23–25**: Test and verify offline access in Kiwix
- **May 25**: ZimWriter merges to main
- **May 26–June 5**: Depending on your Phase 5b decision (Accessibility or OPDS or both)

**Approval format** (reply with one of these):
- **"Approved: ZimWriter immediately. Decide on Phase 5b after."** ← Recommended
- **"Approved: ZimWriter + Accessibility (both parallel)."** ← Inclusive design focus
- **"Approved: ZimWriter + OPDS (Phase 5b after ZimWriter lands)."** ← Discoverability focus
- **"Approved: ZimWriter + Accessibility + OPDS (all three)."** ← Maximum impact

---

## Appendix: Detailed Implementation Checklists

### ZimWriter Implementation Checklist

```
[ ] Add libzim>=3.2,<4.0 to pyproject.toml
[ ] Replace _stub_write_placeholder() with libzim.writer.Creator context
[ ] Wire add_article() and add_image_resource() to creator.add_item()
[ ] Enable Xapian full-text indexing via creator.config_indexing(True, "eng")
[ ] Re-enable zimcheck subprocess validation
[ ] Verify 84 export pipeline tests pass: uv run pytest tests/export/ -v
[ ] Manual test: export small archive, open in Kiwix Android (F-Droid)
[ ] Update documentation (README, CONTRIBUTING, schema docs)
[ ] Create PR, await review, merge to main
```

**Effort**: 8–11 hours
**Risk**: Low
**User outcome**: Offline access for all users

---

### Accessibility Audit Checklist (Path A only)

```
[ ] Set up axe-core in Playwright (automated scanning)
[ ] Run full scan against ZIM article HTML template
[ ] Run full scan against web API response surfaces
[ ] Manual keyboard-only navigation testing (all major flows)
[ ] Manual screen reader testing with NVDA (Windows)
[ ] Manual screen reader testing with VoiceOver (macOS)
[ ] Document all findings (critical + non-critical)
[ ] Triage findings into critical (fix now) vs non-critical (backlog)
[ ] Fix critical findings: contrast, missing alt text, semantic HTML
[ ] Write automated regression tests to prevent regressions
[ ] Create PR with audit report, await review, merge to main
```

**Effort**: 18–36 hours (scope-dependent); commit to critical fixes only (~4–12 hours)
**Risk**: Medium (scope creep in remediation phase)
**User outcome**: Equal access for disabled users

---

### OPDS Feed Migration Checklist (Phase 5b, after ZimWriter)

```
[ ] Verify ZimWriter lands and produces valid ZIM exports
[ ] Add feedgen>=0.9 to pyproject.toml
[ ] Rewrite _build_feed_xml() using feedgen FeedGenerator API
[ ] Implement OPDSEntry.from_zim_export() factory method
[ ] Add missing OPDS 1.2 elements (dc:language, dc:issued, opensearch)
[ ] Add OPDS search endpoint integration (/opds/v2/searchdescription.xml)
[ ] Update 19 existing OPDS tests
[ ] Validate feed format against Kiwix catalog parser
[ ] Create PR, await review, merge to main
```

**Effort**: 8–11 hours
**Risk**: Medium (feedgen inactive maintenance, namespace handling edge cases)
**User outcome**: In-app discoverability for Kiwix users

