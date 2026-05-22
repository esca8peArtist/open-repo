---
title: "Phase 5 Candidate Decision Framework — May 25–26 Decision"
project: open-repo
phase: 5
status: decision-required
created: 2026-05-22
decision_deadline: "2026-05-25 to 2026-05-26"
candidates: [ZimWriter libzim, OPDS feedgen, Platform accessibility audit]
author: General Research Agent
tags: [phase-5, decision-framework, zimwriter, opds, accessibility, a11y, offline-export]
---

# Phase 5 Candidate Decision Framework

**Decision needed by**: May 25–26, 2026  
**Phase 4 status**: Complete — 194 tests passing, federation stack stable  
**Current split state**: PR #3 merged to `open-repo/main` remote (real libzim); local `master` still has stub + 88 export tests passing, 240 backend tests passing  
**Pi 5 thermal baseline**: 80.7°C idle (at soft-throttle boundary — watch heading into compute-intensive runs)

---

## Executive Summary

Prioritize Candidate 1 (ZimWriter libzim activation) first, without qualification. It is the only candidate that directly fulfills the project's core mission — getting the open-repo knowledge base into the hands of people who cannot reach the internet. The code is complete, deployed to the Jetson, 4/4 libzim integration tests pass, 88 export-pipeline tests pass, and the implementation is a 2-hour minimum viable path. It unblocks both downstream candidates. Candidate 2 (OPDS feedgen) cannot produce a meaningful catalog until Candidate 1 exists, and Candidate 3 (platform accessibility audit) benefits from auditing a system that already exports — not stubs. After Candidate 1 merges, Candidate 3 is the stronger second pick: it broadens who can use the system at all, while Candidate 2 improves how existing Kiwix users discover it. For May 25–26, the decision is: approve Candidate 1 immediately; schedule the Candidate 2 vs. 3 decision for the week following Candidate 1's merge.

---

## Candidate 1: ZimWriter libzim Activation

### What It Accomplishes

ZimWriter converts the open-repo knowledge base into a `.zim` archive — a compressed, self-contained, fully-indexed offline file readable by Kiwix on Android, iOS, Windows, macOS, Linux, and Raspberry Pi. A 32-article corpus produces roughly a 22–80 MB file. Once produced, the archive requires no internet connection, no login, and no ongoing server — it can be copied to a USB drive, distributed on a local school network, or loaded on a device in a field clinic.

ZIM is the dominant format for offline knowledge distribution in the NGO and humanitarian sector. UNHCR uses it. Médecins Sans Frontières deploys Kiwix ZIM files in field hospitals. The Kali Linux project, Wikipedia offline, and thousands of other educational archives use the same format. Kiwix reports tens of millions of users in countries with poor connectivity.

The project goal is "a distributed, free, one-stop shop to find and share information that benefits all of humanity." For the segment of humanity with intermittent or no internet — approximately 2.7 billion people as of 2026 — offline export is not a feature enhancement; it is the only viable access mechanism.

### Technical Readiness

This candidate is the most thoroughly de-risked item in the entire Phase 5 set:

- libzim 3.10.0 (C++ 9.7.0) installed, wheel verified on aarch64 (Pi 5 / Jetson)
- All 88 export-pipeline tests pass on local master
- 4/4 libzim integration tests pass (real ZIM file generation, magic bytes, Xapian indexing, article retrieval)
- 32 corpus articles pass schema validation
- `ArticleItem` adapter class, `create_zim()` context manager, `_apply_metadata_to_creator()`, and Alembic migration 003 are all committed to the remote branch
- 5 exact code change sites documented with line numbers
- Minimum viable path: 2 hours. Production-ready path: 6–7 hours.

Status: **READY TO MERGE**. The blocking item is user approval, not code.

### Pre-Requisites and Blockers

Three items are not yet complete on local master (from the Phase 5.1 pre-merge audit):

| Item | Blocking | Resolution |
|------|----------|------------|
| `html.escape()` on `source_node_url` in attribution footer | Federated content safety | ~20 min fix |
| `ZimExport` SQLAlchemy ORM class in `app/models.py` | Candidate 2 `from_zim_export()` factory | Committed to remote — sync during merge |
| `libzim>=3.10.0,<4.0` in `pyproject.toml` | End-to-end ZIM integration tests | One-line change |

None of these block MVP activation. The stub fallback (`_LIBZIM_AVAILABLE = False`) remains in place until these are resolved. For minimum viable: confirm libzim import, run 88 existing tests, generate one test ZIM file, open in Kiwix.

**Thermal note**: ZIM creation for 32 articles takes 2–3 seconds on Pi 5. No sustained compute load. The 80.7°C idle baseline does not create risk for short export runs, but do not run simultaneous ZIM builds and unrelated compute jobs without monitoring temperature.

---

## Candidate 2: OPDS Feedgen Catalog Migration

### What It Accomplishes

OPDS (Open Publication Distribution System) is the in-app catalog standard for ebook and offline-content readers. Kiwix Android, Kiwix Desktop, and kiwix-serve all support OPDS catalog discovery: a user types one URL into the app, and the app displays a browseable library of available ZIM archives with one-tap download. Without OPDS, users must know the direct CDN URL for each file.

The current `OPDSCatalogService` builds OPDS XML using Python's raw `xml.etree` module with four deferred `TODO(post-PR-merge)` markers. This candidate migrates the generator to the `feedgen` library (cleaner namespace handling, shorter code), implements the `OPDSEntry.from_zim_export()` factory method that populates the catalog from real ZIM export database records, adds missing OPDS 1.2 `dc:language`, `dc:issued`, and `opensearch:totalResults` elements, and adds a search endpoint.

The institutional value extends beyond individual users: UN agencies, educational networks, and NGOs standardize on OPDS catalog integration for deploying content at scale. An OPDS endpoint makes open-repo discoverable by library management systems without any manual configuration.

### Technical Readiness

- Detailed implementation roadmap exists (`PHASE_5_CANDIDATE_2_OPDS_IMPLEMENTATION_ROADMAP.md`)
- 19 existing OPDS tests pass; 4 new tests documented
- feedgen 0.9+ available on PyPI (35K weekly downloads, inactive release cadence — fallback to `xml.etree` always available)
- Architecture diagrams and field-mapping tables complete

**Hard dependency**: `OPDSEntry.from_zim_export()` requires real `ZimExport` ORM rows, which only exist after Candidate 1 produces valid ZIM output and the Alembic migration 003 runs. OPDS can be developed in parallel on a feature branch but must not merge before Candidate 1.

**Known risk (medium)**: feedgen does not have native OPDS support. OPDS-specific link relations (`rel="http://opds-spec.org/acquisition"`) and Dublin Core namespace elements (`dc:language`) must be added via a feedgen extension or lxml post-processing step. The silent failure mode — Kiwix app silently ignoring malformed catalog feeds with no error message — makes debugging slow. The fallback (revert to existing `xml.etree` path) eliminates user impact.

Status: **CONDITIONAL** — development can begin on a feature branch, must not merge before Candidate 1.

### Timeline

8–11 hours. Fits within the May 25–June 12 window assuming Candidate 1 merges by May 28.

---

## Candidate 3: Platform Accessibility Audit

### What It Accomplishes

A WCAG 2.1 Level AA accessibility audit identifies barriers that prevent blind, low-vision, and motor-impaired users from using the platform. The audit covers four domains:

1. **Perceivable**: color contrast (4.5:1 minimum for body text), alt text on images, text scalability to 200%
2. **Operable**: full keyboard navigation, skip links, visible focus indicators
3. **Understandable**: form labels, error identification, HTML `lang` attribute
4. **Robust**: semantic HTML, ARIA roles, screen reader compatibility

For open-repo specifically, the audit surface is the ZIM article HTML template (rendered once and baked into offline archives) and the web API response format for any future frontend. The ZIM template is particularly important: accessibility fixes applied before the ZIM is generated persist in every downloaded archive, on every device, offline. Fixing them after the ZIM ships requires regenerating all archives.

This matters for the project goal at a first-principles level. "For all humanity" is not a figure of speech — it is a design constraint. Approximately 253 million people worldwide have significant visual impairment, and a larger number rely on keyboard navigation due to motor impairments. A platform that requires a mouse to navigate or has unreadable contrast ratios excludes those users by default.

WCAG 2.1 AA is also the baseline for public-sector procurement in most jurisdictions and for partnerships with UN agencies, NGOs, and educational institutions. An accessible system is a more credible institutional partner.

### Technical Readiness

The audit has no code prerequisites and can begin immediately. The remediation scope is unknown until the audit runs — this is the fundamental uncertainty:

- Automated scanning (axe-core via Playwright, Pa11y CLI) catches 30–40% of issues; setup is 2–4 hours
- Manual keyboard navigation testing: 4–6 hours
- Screen reader testing (NVDA on Windows, VoiceOver on macOS, ORCA on Linux): 4–8 hours
- Findings triage: 1 hour
- Critical-only remediation (contrast, missing alt text, semantic HTML): 4–12 hours depending on what the audit finds

Industry data: professional audits of similar-scope projects (10–20 unique page templates) typically surface 15–50 distinct issue categories. Remediation for critical issues only averages 120–160 total hours for a complex site; for a narrowly-scoped API backend with one HTML template, critical-only fixes are likely 4–15 hours.

**Scope management is the key risk**: without a triage protocol (P0 fixes = screen reader breaks entirely; P1 = significant degradation; P2 = best-practice improvements), audit findings can expand indefinitely. Commit only to P0 fixes in this window.

Status: **PLANNABLE** — no blockers, but scope is unknown until audit runs. Lower implementation certainty than Candidates 1 or 2.

---

## Decision Matrix

| Dimension | Candidate 1: ZimWriter | Candidate 2: OPDS Feedgen | Candidate 3: A11y Audit |
|-----------|----------------------|--------------------------|------------------------|
| **Status** | READY TO MERGE | Conditional (after C1) | Plannable (no blockers) |
| **User impact score** | 9/10 | 5/10 | 7/10 |
| **Implementation risk** | 2/10 (low) | 5/10 (medium) | 7/10 (scope-variable) |
| **Timeline to MVP** | 2 hours (minimal), 6–7 hours (production) | 8–11 hours | 12–30 hours |
| **Dependency on other candidates** | None — prerequisite for all downstream work | Hard dependency on C1 | None — fully independent |
| **Unblocks future work** | OPDS (C2), CDN pipeline, Phase 5.2 content modules, IPFS integration | Library/institutional partnerships via OPDS | A11y baseline prevents retrofit cost as system grows |
| **Reversibility** | High — stub fallback in 30 seconds | High — xml.etree fallback always available | Medium — audit reveals debt; remediation is not reversible |
| **Mission alignment** | Core — offline access for 2.7B disconnected users | Medium — discoverability for existing Kiwix users | High — equal access for 253M+ users with visual/motor impairment |
| **Thermal risk (Pi 5)** | Minimal — 2–3 second export runs | Negligible | Negligible (audit is read-only) |
| **Recommended sequence** | **First** | Third | Second |

**Impact score rationale**: Candidate 1 scores 9/10 because it is the delivery mechanism for the project's core value at the highest scale. Candidate 3 scores 7/10 because it removes exclusion barriers for a large and underserved user segment — but it does not exist without Candidate 1 first producing something to audit. Candidate 2 scores 5/10 because OPDS discoverability is a polish layer: users can already get ZIM files via direct CDN URL; OPDS makes that easier but does not unlock new access.

**Risk score rationale**: Higher score = higher risk. Candidate 1 is 2/10 because the implementation is a fill-in exercise against a 100%-complete scaffold with verified binary wheels. Candidate 2 is 5/10 because feedgen's silent OPDS failure modes are slow to debug and the hard merge dependency introduces scheduling risk. Candidate 3 is 7/10 because remediation scope is unknown until the audit runs — this is the core uncertainty of any a11y engagement.

---

## Final Recommendation

**Candidate 1 first. Immediately. Without waiting for the other two decisions.**

The rationale is not primarily about technical readiness (though that is the strongest of the three). It is about mission logic: nothing else in Phase 5 delivers value to users without a valid ZIM file. The OPDS catalog links to ZIM files that do not yet exist. An accessibility audit on an HTML template that gets baked into ZIM files is most valuable immediately before those ZIMs start being distributed, not after. Candidate 1 is both the prerequisite and the highest-impact single item.

**Candidate 3 second** (not Candidate 2). The project goal is "for all humanity" — and an accessible system is a prerequisite to that claim being true. The accessibility audit should target the ZIM article HTML template specifically, before that template is baked into large numbers of distributed archives. Retrofitting accessibility into widely-distributed offline files means regenerating them all. The audit is independent of Candidate 1 (it can begin now or in parallel) and the triage protocol limits scope risk: commit to P0 fixes only in the May–June window and backlog everything else.

**Candidate 2 third**. OPDS is real value — institutional partnerships depend on it, and Kiwix in-app discovery is meaningfully better UX than copy-pasting a CDN URL. But it requires Candidate 1 to exist first, and it is a discoverability improvement on top of a working system, not access-unlocking infrastructure. Deploy it once Candidate 1 has proven stable and the `zim_exports` table has real rows.

**Proposed sequence for the decision**:
- May 25–26: Approve Candidate 1. Begin merge reconciliation (local master ← open-repo/main remote)
- May 26–28: Activate Candidate 1 production path; confirm ZIM output readable in Kiwix
- May 28–30: Run accessibility audit on ZIM article template while Candidate 1 is fresh; triage P0 findings
- June 1–5: Fix P0 accessibility findings (if any); merge accessibility improvements
- June 5+: Begin Candidate 2 OPDS feedgen development (after Candidate 1 confirmed stable)

---

## Implementation Notes and Sequencing Dependencies

### Candidate 1 — Merge Reconciliation Steps

Local master diverged from open-repo/main. Before MVP activation:

1. Sync the real libzim implementation from remote (`open-repo/main` branch has PR #3 merged)
2. Confirm `libzim>=3.10.0,<4.0` is in `pyproject.toml` (installed version is 3.10.0)
3. Verify `ZimExport` ORM class is in `app/models.py` (committed in local master at commit 274eb1f2)
4. Run pre-flight: `python3 -m pytest tests/ -q --tb=no` — expect 240 passed, 19 skipped (backend); 88 passed (export pipeline)
5. Thermal check before extended compute: `vcgencmd measure_temp` — must be below 82°C

The 2-hour minimal viable path ends at: `create_zim()` produces a real ZIM file with correct magic bytes, readable in Kiwix. The 6–7-hour production path adds: export API endpoint (`app/api/v1/export.py`), Alembic migration 003 confirmed, end-to-end test with real DB data, documentation update.

### Candidate 3 — Accessibility Audit Scope Control

The single most important implementation decision for Candidate 3 is the triage protocol:

- **P0 (fix in this window)**: Screen reader cannot access content at all (missing ARIA landmarks, broken keyboard traps, zero-contrast text, missing `<html lang>`)
- **P1 (backlog)**: Screen reader experience degraded but functional (poor heading hierarchy, missing skip links, non-descriptive link text)
- **P2 (out of scope for Phase 5)**: Best-practice enhancements (ARIA live regions, enhanced focus styles beyond minimum visible)

Automated scanning with axe-core covers 30–40% of P0 issues and takes under 4 hours to set up. Do not estimate remediation hours before seeing audit findings — the scope is genuinely unknown until the audit runs.

ZIM article template audit is the highest-priority surface because accessibility problems baked into the HTML template propagate into every distributed archive. Web API surface is secondary and can be deferred to Phase 5.3.

### Candidate 2 — Hard Gate

Do not merge Candidate 2 before:
- `zim_exports` table exists (Alembic migration 003 confirmed run on production DB)
- At least one row in `zim_exports` with `status='available'` and `cdn_url` populated
- All 84 Candidate 1 tests still passing with real libzim (not stub)

The OPDS silent-failure risk (Kiwix silently ignoring malformed catalog feeds) requires local validation against `kiwix-serve` before PR opens. Test command: `GET /opds/v2/root.xml` and confirm the "Install" button appears in Kiwix Android.

---

## Sources

- [python-libzim PyPI — version history and wheel availability](https://pypi.org/project/libzim/)
- [Kiwix — Catalog and distribution solutions](https://get.kiwix.org/en/solutions/catalog/)
- [Kiwix OPDS documentation](https://wiki.kiwix.org/wiki/OPDS)
- [OPDS Catalog 1.2 Specification](https://specs.opds.io/opds-1.2.html)
- [feedgen PyPI](https://pypi.org/project/feedgen/)
- [WCAG 2.1 Overview — W3C WAI](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [AllAccessible — WCAG audit guide and remediation effort estimates](https://www.allaccessible.org/blog/website-accessibility-audit-guide-wcag-template)
- [ADA Title II Digital Accessibility 2026: WCAG 2.1 AA compliance requirements](https://www.sdettech.com/blogs/ada-title-ii-digital-accessibility-2026-wcag-2-1-aa)
- [Kiwix for K-12 — offline educational use case](https://blog.tcea.org/kiwix/)
- [MobileRead Wiki — OPDS protocol overview](https://wiki.mobileread.com/wiki/OPDS)
