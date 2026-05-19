---
title: "Phase 5 Decision Framework — Candidate Evaluation"
project: open-repo
phase: 5
status: decision-required
date: 2026-05-19
author: research-agent
tags: [phase-5, decision, zimwriter, opds, accessibility, a11y]
---

# Phase 5 Decision Framework: ZimWriter vs. OPDS vs. Accessibility Audit

**Status**: Framework complete — user decision required  
**Phase 4 result**: 194 tests passing, 0 failures, federation stack complete (Wave 4)  
**Window**: May 19 – June 5, 2026 (approximately 2.5 weeks)  
**Decision needed by**: May 20 early morning to allow immediate Phase 5 launch

---

## Phase 4 Completion Baseline

Phase 4 (Wave 4) delivered the complete federation infrastructure:

- **Partner registration API** with RSA-SHA256 HTTP signature verification (RFC 8017)
- **ActivityPub inbox** endpoint receiving Announce and Undo activities
- **Endorsement propagation** service with cross-node vote aggregation
- **Conflict detection and logging** with admin resolution dashboard
- **Test suite**: 194 executed, 4 skipped, 0 failures; 73% coverage overall; 93-99% on federation modules
- **ZimWriter and OPDSCatalogService stubs** committed to `app/services/export/` with `TODO(post-PR-merge)` markers at every integration point — scaffolding 100% complete, real implementation deferred

No Phase 5 work is currently blocked on code quality or stability. All three candidates can start immediately on separate branches.

---

## Section 1: Technical Scope per Candidate

### Candidate 1: ZimWriter (libzim Integration)

**What is involved**: Replace stub placeholders in `app/services/export/zim_writer.py` with real `libzim.writer.Creator` calls. The scaffold is fully built — class hierarchy, metadata models, `ExportConfig`, `ArticleItem`, `ZimWriter`, and HTML rendering with Jinja2 templates are all present. Every integration point carries a `TODO(post-PR-merge)` comment.

**Specific change surface**:
- Add `libzim>=3.2,<4.0` to `pyproject.toml` (one line)
- Replace `_stub_write_placeholder()` calls with a `libzim.writer.Creator` context manager
- Wire `add_article()` and `add_image_resource()` to `creator.add_item()`
- Enable Xapian full-text indexing via `creator.config_indexing(True, "eng")`
- Re-enable `zimcheck` subprocess validation in `run_zimcheck()`
- 84 existing export pipeline tests already cover the public interface; stubs swap out without changing signatures

**Dependency situation**: python-libzim 3.8.0 released March 2026 — actively maintained, pre-built wheels available for Linux x86/ARM64, macOS, Windows (CPython only; source distribution available for other platforms). No compiler required for standard deployments.

**Integration points**: Reads from the `content_items` table (Phase 4 schema), streams items in batches of 200, renders via embedded Jinja2 templates (no external dependencies in output HTML), passes through `zimcheck` validation, computes SHA-256 checksum. Downstream consumers (OPDS catalog, CDN upload, scheduled exports) all depend on this producing valid ZIM output.

**Known complexity**: The libzim Creator API uses a context manager pattern; `add_item()` takes a `WritingBlob` subclass rather than raw bytes. The Xapian indexing configuration is a single method call but requires non-empty `get_title()` on every article item. The `zimcheck` subprocess is already wired; just needs the disabled flag removed. Scope is narrow: no schema migrations, no new API endpoints, no cross-service dependencies.

---

### Candidate 2: OPDS feedgen Migration

**Current hardcoded approach**: `app/services/export/opds_generator.py` builds OPDS XML using Python's `xml.etree.ElementTree` directly. Raw element construction, manual namespace injection, and string concatenation handle the Atom feed structure. Four `TODO(post-PR-merge)` markers defer: feedgen library switch (line 353), `dc:language`/`dc:issued`/`opensearch` elements (line 544), version-history sub-entries (line 396), and the search endpoint (line 442). The `OPDSEntry.from_zim_export()` factory method (line 155) is a stub — the catalog cannot currently be populated from real ZIM export records.

**What auto-generation requires**:
- Add `feedgen>=0.9` to `pyproject.toml`
- Rewrite `OPDSCatalogService._build_feed_xml()` to use feedgen's `FeedGenerator` and `FeedEntry` objects, eliminating raw `xml.etree` construction
- Implement `OPDSEntry.from_zim_export(zim_export_orm_row)` — maps database export records to OPDS entries with acquisition links, file sizes, and checksums
- Add missing OPDS 1.2 elements: `dc:language`, `dc:issued`, `opensearch` description, version-history sub-entries
- Add OPDS search endpoint integration (`/opds/v2/searchdescription.xml`)
- Update 19 existing OPDS tests — most assertions remain valid after the rewrite; namespace handling and element ordering may require minor adjustments

**Integration complexity**: Moderate. The feedgen library abstracts Atom/RSS generation but does not have native OPDS support — OPDS-specific link relations (`rel="acquisition"`, `type="application/x-zim"`) must be set via feedgen's `add_link()` extension mechanism. OPDS 1.2 has namespace subtleties: the `opds:` and `dc:` namespaces must be declared correctly or Kiwix app catalog discovery silently fails. Feedgen's health status is a concern: as of 2026, the library shows inactive release cadence (no new PyPI release in 12+ months) with approximately 35,000 weekly downloads. A fallback to `xml.etree` (currently working) is always available.

**Dependency on Candidate 1**: The `OPDSEntry.from_zim_export()` factory needs real `ZimExport` ORM rows, which only exist after Candidate 1 produces valid output. OPDS can be developed in parallel on a separate branch but should not merge before Candidate 1 lands.

---

### Candidate 3: Accessibility Audit and Improvements

**Audit scope**: WCAG 2.1 Level AA is the appropriate target — it is the internationally recognized standard and the baseline for most public-interest digital infrastructure projects. The audit covers four domains: (1) perceivable content (color contrast 4.5:1 minimum for body text, alt text for images, text resizing to 200%); (2) operable interfaces (full keyboard navigation without mouse, skip links, focus indicators visible); (3) understandable content (form labels, error identification, language declaration); (4) robust markup (semantic HTML, ARIA roles where needed, screen reader compatibility).

The `phase-5-export-strategy.md` document already notes a WCAG AA contrast requirement on the ZIM article HTML template (minimum 4.5:1 contrast ratio), but no audit has been run against the web frontend.

**Scope ambiguity**: Open-repo is primarily a backend API. The "web interface" surface depends on what frontend exists — if the current phase only delivers API endpoints and the offline ZIM export, the a11y audit scope is largely limited to the ZIM article HTML template (which is rendered once and baked into offline archives) and any API response format used by screen-reader-accessible clients. A full frontend a11y audit requires a frontend to audit.

**Tools available**:
- Automated (catches 30-40% of issues): axe-core (usable in Cypress/Playwright), Pa11y CLI, Accessibility Insights by Microsoft
- Manual (required for the remainder): keyboard-only navigation testing, VoiceOver (macOS), NVDA (Windows/free), ORCA (Linux)

**Typical open-source a11y backlog**: Automated scanning on a moderately complex web application typically surfaces 15-50 distinct issue types. Remediation effort is highly variable — missing alt text across many images can be 40+ hours; form label fixes take minutes each; color contrast issues require CSS changes that may ripple through the design system. Professional audits of similar-scope projects estimate 120-160 hours total remediation for comprehensive WCAG AA compliance on a site with 10-20 unique page templates.

---

## Section 2: User Value Ranking

| Candidate | Who benefits | User outcome | Mission alignment | Rank |
|-----------|-------------|-------------|-------------------|------|
| **1: ZimWriter** | Users in low-bandwidth regions, field workers, disaster responders, off-grid installations | Download a ~50-80 MB ZIM file; read the entire open-repo knowledge base offline in Kiwix on any device; no internet required | Direct — "distributed free info for all humanity" is meaningless without offline access for users who cannot reach the internet reliably | **1st** |
| **3: A11y** | Blind and low-vision users, motor-impaired users who depend on keyboard navigation, screen reader users | Can actually use open-repo without assistive technology workarounds; equal access to community knowledge | High — "for all humanity" explicitly includes disabled users; without accessibility, a portion of humanity is excluded by design | **2nd** |
| **2: OPDS** | Kiwix app users who browse the in-app content directory rather than using a direct URL | Discover and one-click-install open-repo archives from within Kiwix Android/Desktop without needing a URL | Medium — improves distribution discoverability and enables library/institutional partnerships that rely on OPDS catalog standards; depends on Candidate 1 first | **3rd** |

**Ranking rationale**: ZimWriter is ranked first because it is the prerequisite for the project's core offline value proposition — nothing downstream (OPDS, CDN, partnerships) matters without a valid ZIM file. Accessibility is ranked second because it broadens who can use the system at all, which is a harder constraint than how easily users discover it. OPDS is ranked third because it is a discoverability polish layer on top of a working offline export, not a standalone feature.

---

## Section 3: Developer Experience Impact

**Candidate 1 (ZimWriter)**: Adds one new production dependency (`libzim`). Wheel availability is strong for standard deployment targets (Linux x86/ARM64, macOS, Windows); edge cases on unusual platforms require building from source. CI gains a real ZIM validation step via `zimcheck` subprocess — this adds approximately 10-15 seconds to the test suite for a small export but catches format errors that unit mocks cannot. The 84 existing export pipeline tests immediately become meaningful rather than stub-verifying placeholders. Long-term: high maintainability gain — the export pipeline becomes a testable, drivable system rather than a collection of TODOs. No schema migrations, no API surface changes.

**Candidate 2 (OPDS feedgen migration)**: Removes raw `xml.etree` string construction in favor of feedgen's API — cleaner, shorter code at the cost of an inactive-maintenance upstream dependency. If feedgen is abandoned, the fallback path is a revert to `xml.etree` (already proven to work). The rewrite makes adding RSS variants, alternate ordering, and domain-specific sub-catalogs straightforward; each is a new `FeedEntry` loop, not a string-building exercise. Testing complexity is low: 19 existing tests plus feedgen's own format validation. Long-term: moderate maintainability improvement, with the dependency-health caveat.

**Candidate 3 (A11y audit)**: Introduces testing infrastructure with no equivalent in the current codebase. Automated a11y tests (axe-core via Playwright) run in CI and fail builds on regressions — valuable safety net but adds 30-90 seconds per CI run depending on the test surface. Manual testing with screen readers is not automatable; it must be re-run after each significant frontend change. The audit itself does not add technical debt — it reveals existing debt. Fixes may range from trivial (missing ARIA labels) to substantive (restructuring semantic HTML). If the project's current frontend surface is small, a11y work is well-contained. If the frontend grows later without an a11y baseline established now, retrofitting becomes significantly harder. Long-term: establishing a11y infrastructure now prevents the compounding cost of retrofitting an inaccessible system.

---

## Section 4: Timeline Feasibility (May 19 – June 5, 2026)

### Candidate 1: ZimWriter — 8-12 hours, strong fit

| Sub-task | Estimate |
|----------|----------|
| Add `libzim` dependency, verify wheel install | 30 min |
| Replace stubs with `libzim.writer.Creator` context | 2-3 hours |
| Wire `add_article()`, `add_image_resource()` | 1-2 hours |
| Enable Xapian indexing | 30 min |
| Re-enable and tune `zimcheck` validation | 1 hour |
| Verify 84 existing tests pass | 1 hour |
| Run manual test on Kiwix Android (F-Droid) | 1-2 hours |
| Documentation update | 1 hour |
| **Total** | **8-11 hours** |

**Risk to timeline**: Low. The scaffolding is complete; this is a fill-in exercise, not a design exercise. The primary unknown is whether `zimcheck` reveals metadata edge cases in the rendered HTML, but the existing test suite is designed to catch these.

**Python binding maturity risk**: Low-to-medium. python-libzim 3.8.0 (March 2026) is actively maintained by the openZIM Foundation (the same team that maintains the ZIM format specification). Pre-built wheels cover the expected CI and deployment platforms. The risk is not "will it work" but "will it work on an unusual target" — Raspberry Pi ARM is supported, which is the most important deployment edge case for this project.

### Candidate 2: OPDS feedgen migration — 6-10 hours, fits with dependency caveat

| Sub-task | Estimate |
|----------|----------|
| Add `feedgen` dependency, audit its OPDS extension support | 1 hour |
| Rewrite `_build_feed_xml()` with feedgen | 2-3 hours |
| Implement `OPDSEntry.from_zim_export()` factory | 1-2 hours |
| Add missing OPDS 1.2 elements | 1-2 hours |
| Add search endpoint | 1 hour |
| Update 19 existing tests | 1 hour |
| Validate against Kiwix catalog discovery | 1 hour |
| **Total** | **8-11 hours** |

**Risk to timeline**: Medium. Feedgen's inactive maintenance status means OPDS-specific namespace handling may require workarounds. The silent-failure mode (Kiwix app ignores malformed catalogs without error messages) makes debugging slow. Cannot merge before Candidate 1 — this creates a sequencing dependency within the window.

**OPDS spec risk**: The OPDS 1.2 specification is standardized and stable, which reduces interpretation risk. The risk is feedgen's integration path for non-standard link relations, not spec ambiguity.

### Candidate 3: Accessibility audit — 12-30 hours, tight and scope-dependent

| Sub-task | Estimate |
|----------|----------|
| Automated axe-core/Pa11y scan | 2-4 hours setup + run |
| Manual keyboard navigation testing | 4-6 hours |
| Screen reader testing (NVDA + VoiceOver) | 4-8 hours |
| Document findings | 2-3 hours |
| Fix critical issues (contrast, missing labels, semantic HTML) | 4-12 hours (findings-dependent) |
| Write regression tests | 2-3 hours |
| **Total** | **18-36 hours** |

**Scope risk**: High. The audit phase is bounded (4-6 hours for automated + basic manual), but remediation scope is unknown until the audit runs. If the ZIM article HTML template and web frontend have pervasive contrast or semantic structure issues, fixing them could easily exceed the window. The correct scoping decision is to do the audit, then triage findings into "critical (fix now)" and "non-critical (backlog)," and only commit to critical fixes in this window.

**Unpredictable scope risk**: This is the primary risk for the May 19-June 5 window. A11y audits reliably surface more work than anticipated.

---

## Section 5: Risk Assessment

### Candidate 1: ZimWriter

**What can break**:
- libzim wheel not available for the CI/deployment platform — low probability for standard Linux/macOS
- `zimcheck` validation fails for metadata edge cases (title length > 30 chars, missing illustration, non-ASCII in metadata fields)
- Xapian indexing generates a corrupt or oversize index for malformed HTML input
- HTML rendering produces external dependencies (inline `<script>` or external `<link>`) that zimcheck rejects

**Recovery paths**:
- Platform wheel missing: switch to source distribution build in CI (adds 5-10 minutes to CI but unblocks work)
- zimcheck failures: documented error messages are specific and actionable; fix is typically a metadata value correction
- Xapian issues: disable indexing (`config_indexing(False)`) to produce a valid but unsearchable ZIM as a fallback; re-enable after fixing HTML rendering
- **Fallback (worst case)**: Revert to stub behavior — 30 seconds to undo. ZIP export of HTML files provides a non-ZIM offline option if libzim proves unworkable

**Recovery path clarity**: High. Every failure mode has a specific fix or bypass.

---

### Candidate 2: OPDS feedgen migration

**What can break**:
- feedgen does not natively support OPDS acquisition link relations — workaround needed via `add_link()` extension
- Namespace declaration order causes Kiwix catalog parser to silently reject the feed
- `from_zim_export()` factory maps fields incorrectly (wrong MIME type, incorrect file size units, missing acquisition href)
- OPDS search endpoint returns malformed `searchdescription.xml` that breaks Kiwix search integration

**Recovery paths**:
- feedgen OPDS limitation: fall back to raw `xml.etree` (already working, just verbose) — zero user impact
- Namespace ordering: test against Kiwix catalog parser locally before shipping; the OPDS spec has known-good example XML that can be diffed
- Factory method bugs: 19 existing tests cover acquisition link structure; failures surface immediately in test run
- **Version the feed format**: expose both `/opds/v1/` (current raw XML) and `/opds/v2/` (feedgen) during transition so existing integrations do not break

**Recovery path clarity**: Medium-high. The main risk (feedgen OPDS namespace handling) has a clean fallback.

---

### Candidate 3: Accessibility audit

**What can break**:
- Audit reveals widespread issues that take significantly longer to fix than anticipated (underestimation risk)
- Screen reader testing reveals interaction patterns that require substantial semantic HTML restructuring
- CI a11y tests become flaky (false positives) and erode developer trust in the test suite
- Fixing contrast or semantic structure breaks the visual design of the ZIM article template, requiring design re-review

**Recovery paths**:
- Scope explosion: explicit triage protocol — categorize findings as P0 (blocks screen reader use entirely), P1 (degrades experience significantly), P2 (best-practice improvements); commit only to P0 fixes in this window; defer P1/P2 to backlog
- Flaky a11y tests: run axe-core in report-only mode (not blocking) initially; graduate to blocking after the backlog is stable
- Template design regression: keep a11y fixes scoped to semantic structure and ARIA attributes; avoid visual redesign within this window
- **If audit finds only minor issues**: This is actually the ideal outcome — fixes are fast, a11y infrastructure is established, future work stays clean

**Recovery path clarity**: Medium. The audit's failure mode is a large backlog, not a broken feature. "Unmanageable" risk is low as long as the triage protocol is applied; without it, scope creep is a real risk for the 2.5-week window.

---

## Decision Matrix

| Criterion | Candidate 1 (ZimWriter) | Candidate 2 (OPDS feedgen) | Candidate 3 (A11y audit) |
|-----------|------------------------|---------------------------|--------------------------|
| **User Impact** | High — offline access for low-bandwidth, disaster, off-grid users; core mission deliverable | Medium — easier discovery for existing Kiwix users; requires Candidate 1 first | High — equal access for disabled users; broadens "all humanity" to include impaired users |
| **Technical Risk** | Low — scaffold complete, libzim 3.8.0 actively maintained, 84 existing tests | Medium — feedgen inactive maintenance, OPDS namespace gotchas, silent failure mode | Medium-High — audit scope unknown, remediation effort unpredictable |
| **Timeline Feasibility (May 19–June 5)** | 8-11h, strong fit | 8-11h, fits but depends on Candidate 1 merging first | 12-30h, fits only with explicit triage and scope cap on fixes |
| **Developer Experience** | Adds one actively-maintained dependency; 84 stub tests become real | Removes raw XML boilerplate; adds inactive-maintenance dependency | Adds testing infrastructure; reveals existing debt without creating new debt |
| **Mission Alignment** | "Distributed free info for all humanity" — offline access is the primary distribution channel for humanity's most disconnected users | "Distributed knowledge" — feeds enable library and institutional partnerships at scale | "For all" — inclusion of disabled users is a prerequisite to "all humanity" |
| **Unblocks Future Work** | Unblocks OPDS (Candidate 2), CDN upload, scheduled exports, IPFS integration | Unblocks library/institutional distribution partnerships | Unblocks inclusive design across future features; prevents compounding retrofit cost |
| **Recovery Path** | High clarity — specific fallbacks for every failure mode | Medium-high — raw xml.etree fallback always available | Medium — triage protocol controls scope; no code rollback needed |

---

## Recommendation

**Pick Candidate 1 (ZimWriter)** as Phase 5 first work item. The scaffold is 100% complete, the dependency is actively maintained, the risk profile is the lowest of the three, and it unblocks every other downstream Phase 5 deliverable. Completing ZimWriter immediately converts 84 stub-verifying tests into real validation and delivers the project's core offline value proposition — the one thing users in low-bandwidth regions and field deployments actually need.

**Candidate 3 (Accessibility audit) is the smart second pick** if the window allows it: run the audit in parallel with ZimWriter development, triage findings, and fix only P0 issues before June 5. Establishing a11y infrastructure now is significantly cheaper than retrofitting after the frontend grows. Candidate 2 (OPDS) should follow Candidate 1 but is lower urgency — direct URL download from CDN works without an OPDS catalog; in-app discovery is a polish layer, not a prerequisite.

---

## User Decision Path

Review the three candidates and select one of the following paths:

**Path A — Core feature first (recommended)**: "Start Candidate 1 (ZimWriter). Launch by May 21. Close by May 28. Then assess whether to run Candidate 3 audit in parallel or defer."

**Path B — Core + accessibility in parallel**: "Start Candidate 1 immediately. Start Candidate 3 audit simultaneously on a separate branch. Triage audit findings and fix P0 issues before June 5. Merge both before window closes."

**Path C — Accessibility first**: "Run Candidate 3 audit before building new features. Ensures the ZIM article HTML template and web layer are a11y-clean before Candidate 1 bakes them into offline archives."

**Path D — All three sequentially**: "Candidate 1 → Candidate 2 → Candidate 3. Full Phase 5 offline stack plus OPDS discoverability plus accessibility baseline. Requires 24-42 hours of work over 2.5 weeks — tight but possible if bandwidth is consistent."

**Confirm selection by May 20 to allow immediate Phase 5 branch creation and work start.**

---

## Sources

- [python-libzim PyPI](https://pypi.org/project/libzim/)
- [python-libzim GitHub (openzim)](https://github.com/openzim/python-libzim)
- [feedgen PyPI](https://pypi.org/project/feedgen/)
- [feedgen GitHub — "Dead Project?" issue](https://github.com/lkiesow/python-feedgen/issues/106)
- [feedgen Snyk health report](https://snyk.io/advisor/python/feedgen)
- [WCAG 2.1 AA audit standard rationale (2025)](https://accessible.org/wcag-21-aa-audit-standard-2025/)
- [WCAG 2 Overview — W3C WAI](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [Accessibility audit scope and effort estimates](https://www.allaccessible.org/blog/website-accessibility-audit-guide-wcag-template)
- [OPDS catalog standard](https://opds.io/)
