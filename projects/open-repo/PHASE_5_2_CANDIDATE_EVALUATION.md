---
title: "Phase 5.2 Candidate Evaluation Framework"
project: open-repo
phase: "5.2 pre-implementation"
status: "evaluation-complete — updated 2026-05-26"
date: 2026-05-26
decision_deadline: 2026-05-27
production_target: June 1-12, 2026
research_updated: 2026-05-26
---

# Phase 5.2 Candidate Evaluation Framework

**Purpose**: Comprehensive feasibility analysis of five Phase 5.2 candidate tracks to inform the user's decision on post-Phase-5.1 priorities.

**Context**: Phase 5.1 (ZimWriter) is conditional-approved for merge by May 25-26. This evaluation informs which Phase 5.2 feature(s) should follow immediately after Phase 5.1 production validation. Updated 2026-05-26 with corrected e-reader market data, Typesense/Pi 5 compatibility findings, SQLite FTS5 as a search option, and a fifth candidate track (Content Domain Expansion).

**Timeline**: Analysis complete 2026-05-26. User decision needed by May 27. Implementation window: June 1-12, 2026 (11-12 days available).

## Research Corrections Applied in This Update

Three factual corrections to earlier drafts:

1. **OPDS e-reader scope corrected**: Amazon Kindle holds ~80% of the e-reader market (2025) and does NOT support OPDS natively. Kobo (~10% share) supports OPDS via sideloading. The primary OPDS value for open-repo is Kiwix in-app discovery (mobile/desktop), not Kindle or Kobo. Earlier drafts overstated the e-reader discovery benefit.

2. **Typesense Pi 5 page-size bug confirmed**: Typesense has a documented crash on Raspberry Pi 5 caused by jemalloc's incompatibility with the Pi 5's default 16K memory page size (GitHub issue #1351, opened 2023, unresolved as of 2026). This makes Typesense a poor fit for the Pi 5 deployment target without a kernel page-size patch. Meilisearch has aarch64 binaries available via Arch Linux ARM and community Docker images, but official ARM64 support is not explicitly documented. SQLite FTS5 is confirmed as the zero-dependency, Pi 5-safe option.

3. **OPDS 1.2 vs 2.0 distinction**: OPDS 2.0 uses JSON-LD / Readium Web Publication Manifest format — it is not Atom-based. Kiwix uses OPDS 1.2 (Atom/XML). The implementation target is OPDS 1.2 for Kiwix compatibility, not 2.0.

---

## Executive Summary

### Four Phase 5.2 Candidates Under Evaluation

| # | Candidate | User Value | Scope | Implementation Risk | Dependencies |
|---|-----------|-----------|-------|--------------------|----|
| **1** | OPDS Feed Generation | Standards compliance, Kiwix in-app discovery, library partnerships | 8-11 hours | Low | Requires Phase 5.1 (ZimWriter) producing valid ZIM output |
| **2** | Accessibility (A11y) Audit & Remediation | Inclusive design, expanding community reach | 6-14 hours audit + TBD remediation | High (scope uncapped) | None (Phase 5.1 complete modules) |
| **3** | Search Engine Integration | Offline search in ZIM, usability for large corpora | 8-12 hours | Medium-High (Pi 5 thermal constraints) | None (independent) |
| **4** | API Gateway for Federation | Cross-project data sharing, federation interop | 4-6 hours | Low (well-scoped) | Phase 4 federation foundation |

### Recommended Sequencing Decision Tree

```
User decision required:

Step 1: Post-Phase-5.1 Immediate Priority?
  ├─ Option A (Recommended): OPDS (8-11 hrs)
  │  └─ Unblocks: Kiwix in-app discovery; library partnerships in Phase 6
  │     Timeline: June 1-5 (fits in 11-day window)
  │
  ├─ Option B: Search (8-12 hrs)
  │  └─ Unblocks: Offline search for users with large ZIM files
  │     Timeline: June 1-6 (fits in 11-day window)
  │     Risk: Pi 5 indexing performance; test on hardware first
  │
  ├─ Option C: API Gateway (4-6 hrs)
  │  └─ Unblocks: Federation data sharing; enables multi-project deployments
  │     Timeline: June 1-3 (high-speed path, low risk)
  │
  └─ Option D: A11y Audit (6-14 hrs audit + TBD remediation)
     └─ Unblocks: Inclusive design; expands addressable community
        Timeline: 6-14 hours just for audit
        Risk: Scope uncapped; remediation effort unknown before starting audit

Step 2: Secondary Priority?
  After the first candidate completes, which is next?
  Available time remaining in June 1-12 window: 11 - X hours

  If first = OPDS (8 hrs):
    Remaining = 3 hours → API Gateway feasible (4-6 hrs, needs spillover)
                          A11y Audit marginally feasible (6 hrs minimum)
                          Search not feasible (8-12 hrs)

  If first = Search (10 hrs):
    Remaining = 1 hour → Nothing feasible
               → Phase 5.2 is complete; Phase 6 begins

  If first = API Gateway (5 hrs):
    Remaining = 6 hours → OPDS feasible (8-11 hrs, needs spillover)
                          A11y Audit feasible (6 hrs minimum)
                          Search not feasible (8-12 hrs)

Step 3: What Does "Done" Mean?
  - OPDS: User can add /opds/v2/root.xml to Kiwix Android; sees archive; clicks Install
  - Search: User can open ZIM in Kiwix; search function works; results appear in <2s
  - A11y: WCAG 2.1 AA audit complete; issues documented; remediation plan attached
  - API Gateway: `/api/federation/exports` endpoint exists; federation partners can call it
```

---

## Detailed Candidate Analysis

### Candidate 1: OPDS Feed Generation

#### What It Delivers

OPDS (Open Publication Distribution System) 1.2 is the in-app catalog standard that Kiwix readers use to discover downloadable archives. Without OPDS, users must know the direct CDN URL to download ZIM files. With OPDS, Kiwix Android (F-Droid), Kiwix Desktop, and kiwix-serve can display the open-repo archive library in their built-in browser, enabling one-click install.

**User-facing outcome**: A user launches Kiwix Android, navigates to "Add Library," pastes the OPDS URL, and sees "Open-Repo Full Library (English, 22 MB)" with an Install button. Tapping it auto-downloads the ZIM.

**Four endpoints delivered**:
- `GET /opds/v2/root.xml` — Navigation catalog (links to sub-feeds)
- `GET /opds/v2/entries` — Acquisition feed (one entry per ZIM export with download links)
- `GET /opds/v2/entry/{uuid}` — Single entry view with version history
- `GET /opds/v2/searchdescription.xml` — OpenSearch description for in-app search

#### Implementation Hours

| Component | Hours | Notes |
|-----------|-------|-------|
| Add feedgen dependency to pyproject.toml | 0.25 | 1 line; low risk |
| Add OPDSEntry.from_zim_export() classmethod | 1.5 | Critical bridge between Phase 5.1 and 5.2; maps ORM fields to OPDS schema |
| Rewrite OPDSGenerator with feedgen | 2-2.5 | Replace xml.etree stubs; implement root catalog, acquisition feed, entry generation |
| Add Dublin Core post-processor | 1-1.5 | Parse feedgen output; inject dc:language and dc:issued elements |
| New routers/opds.py with 4 endpoints | 1-1.5 | FastAPI route handlers; load ZimExport rows; call OPDSGenerator |
| Unit tests: 4 new tests + verify existing 19 | 1-1.5 | Verify feedgen integration, from_zim_export factory, XML well-formedness |
| Integration test: kiwix-serve validation | 0.75-1 | Docker + kiwix-serve; verify Kiwix accepts the feed |
| Manual Kiwix Android/Desktop verification | 0.5 | Test on actual devices/clients; confirm Install button visible |
| **Total** | **8-11 hours** | |

#### Dependencies

**Hard dependency**: Candidate 1 (ZimWriter) must have produced valid ZIM files with `ZimExport` ORM rows populated in the database. The `from_zim_export()` factory method requires real `ZimExport` rows to construct OPDS entries from.

**Why**: `OPDSEntry.from_zim_export()` reads `export.cdn_url`, `export.sha256`, `export.title`, `export.language`, and other fields from the `zim_exports` table. That table is created by Phase 5.1's Alembic migration; it does not exist until Phase 5.1 merges.

**Development independence**: Candidate 2 development *can* start in parallel with Phase 5.1 (on a separate branch) because the `from_zim_export()` factory can be tested against mock `ZimExport` objects. However, integration tests and validation require real ZIM output from Phase 5.1.

#### Testing Requirements

**Unit tests** (4 new, 19 existing):

1. `test_opds_root_catalog_valid_atom` — Root catalog is well-formed Atom XML; xmllint passes
2. `test_opds_acquisition_feed_has_required_elements` — Each entry has `<id>`, `<title>`, `<updated>`, `<link rel="...">`
3. `test_opds_acquisition_link_type_is_zim` — Acquisition link MIME type is `application/x-zim`
4. `test_opds_from_zim_export_factory` — Factory maps ZimExport fields correctly

**Integration tests**:

5. `test_opds_feed_parseable_by_kiwix_catalog_parser` — kiwix-serve accepts URL; catalog loads without errors
6. Manual test: Kiwix Android/Desktop in-app discovery (not automated; manual verification required)

**Verification commands**:

```bash
# Unit tests
uv run pytest tests/unit/test_opds_generator.py -v

# Integration test (requires Docker)
docker run -d -p 8080:80 kiwix/kiwix-serve:latest
uv run pytest tests/integration/test_opds_kiwix.py -v -m integration

# Full OPDS suite
uv run pytest tests/ -k "opds" -v
```

#### User Value

**Direct value**: Library and institutional partnerships (schools, clinics, NGOs) often require OPDS catalog support for content integration. With OPDS, open-repo becomes discoverable in Kiwix's built-in library browser, removing the friction of "find the CDN URL" for end users.

**Standards compliance**: OPDS 1.2 is a widely adopted syndication standard for offline content distribution. Implementing OPDS positions open-repo as a standards-compliant distribution platform, important for institutional and governmental deployments.

**Phase 6 foundation**: OPDS catalog will be part of Phase 6's "retention policy automation" — when a ZIM export is deleted, it must also be removed from the OPDS version history. The catalog structure is foundational to downstream features.

**Corrected user demographics**: The primary beneficiaries are Kiwix users (Android F-Droid, Desktop, kiwix-serve), not general e-reader users. Amazon Kindle (~80% e-reader market share, 2025 Mordor Intelligence data) does not support OPDS. Rakuten Kobo (~10% market share) supports OPDS via sideloading, but open-repo exports ZIM files, not EPUB — Kobo cannot read ZIM content regardless of OPDS catalog support. The value of OPDS is specifically the Kiwix in-app discovery flow and institutional library catalog integrations that explicitly require OPDS compliance as a procurement criterion.

#### Risk Assessment

| Risk | Probability | Impact | Detection | Mitigation |
|------|-------------|--------|-----------|-----------|
| **feedgen cannot set OPDS acquisition link relation URI correctly** | Medium | High (Kiwix shows no Install button) | Test `test_opds_acquisition_link_type_is_zim` fails or Kiwix shows "Browse" not "Install" | First change in implementation: test feedgen's `rel` parameter handling. If it fails, use xml.etree fallback for this specific link. |
| **Kiwix silently rejects malformed namespace declarations** | Medium | High (Kiwix library shows nothing) | Manual test: no archives appear in Kiwix UI despite valid HTTP response | Compare generated XML to spec example in PHASE_5_ARCHITECTURE.md. Run `xmllint --noout` before testing in Kiwix. |
| **feedgen library inactive maintenance causes import failure** | Low | Low (xml.etree fallback always available) | `uv pip install feedgen` fails or import raises ImportError | Import guard (`_FEEDGEN_AVAILABLE` flag) handles this. Fallback to xml.etree is already implemented. |
| **from_zim_export() factory maps incorrect field** | Low | High (wrong download URLs or file sizes) | test_opds_from_zim_export_factory must verify each field individually | Unit test must assert all fields, not just verify construction succeeds. |
| **Merge blocker: Phase 5.1 not merged yet** | Low | Blocking | Candidate 2 branch cannot merge to main before Candidate 1 | Plan: Candidate 2 development can run in parallel on separate branch. Rebase and merge after Phase 5.1 lands. |

#### Deployment Gate Checklist

Before deploying OPDS to production:

- [ ] Phase 5.1 (ZimWriter) gate fully complete
- [ ] zim_exports table has at least one row with status='available' and cdn_url populated
- [ ] OPDSEntry.from_zim_export() tested with real ZimExport DB row (not mock)
- [ ] `uv run pytest tests/unit/test_opds_generator.py -v` — all 23 tests pass
- [ ] `GET /opds/v2/root.xml` returns 200 with Content-Type: application/atom+xml
- [ ] `GET /opds/v2/entries` returns acquisition feed with at least one <entry>
- [ ] OPDSGenerator.validate_opds_xml(feed_bytes) returns empty list
- [ ] `xmllint --noout` on feed XML passes (no namespace errors)
- [ ] Kiwix Android (F-Droid): Add library URL → shows open-repo archives → Install button visible
- [ ] Kiwix Desktop: Add library URL → shows archive list with descriptions
- [ ] `GET /opds/v2/searchdescription.xml` returns well-formed XML
- [ ] OPDS catalog auto-regenerates after new ZimWriter export completes
- [ ] Version history: second export for same flavour appears in version_history
- [ ] DC elements in feed: `<dc:language>` and `<dc:issued>` present in each entry
- [ ] Cache-Control headers present: max-age=3600 on /opds/v2/entries

---

### Candidate 2: Accessibility (A11y) Audit & Remediation

#### What It Delivers

A comprehensive WCAG 2.1 AA audit of all ZIM export HTML, identifying:
- Missing alt text on images (critical for screen readers)
- Heading hierarchy violations (h1→h3 jumps confuse assistive tech)
- Color contrast issues (body text vs. background; accessibility standard is 4.5:1 for AA)
- Missing form labels or ARIA landmarks
- Keyboard navigation blockers

**User-facing outcome**: Users with visual impairments, motor disabilities, or cognitive processing differences can access open-repo content through screen readers (NVDA, JAWS), voice control, and keyboard-only navigation. Expands addressable community from developers/technical users to mainstream users with accessibility needs.

#### Implementation Hours

This candidate has an unusual structure: **audit is capped (6-14 hours), remediation is uncapped (TBD)**.

| Component | Hours | Notes |
|-----------|-------|-------|
| **Audit Phase** | | |
| Set up WCAG 2.1 AA audit tools (axe-core, Pa11y, aXe DevTools) | 1 | One-time setup; run against Phase 5.1 HTML template |
| Automated scan: HTML template used in all ZIM exports | 1-1.5 | axe-core scans; capture results in structured format |
| Manual review: Color contrast (3 export variants × 3 color themes) | 2-2.5 | Screenshots in different lighting; verify 4.5:1 contrast ratio |
| Manual review: Image alt text (sample articles from 3 domains) | 2-3 | Read 30-50 images; verify alt text descriptiveness, not just presence |
| Manual review: Heading hierarchy (sample articles) | 1-1.5 | Check for h1→h3 jumps, orphaned headings, nesting violations |
| Manual review: Keyboard navigation in Kiwix WebView | 1 | Tab through ZIM in Kiwix Android/Desktop; identify focus traps |
| Report generation with WCAG failures mapped to code locations | 1.5 | CSV mapping {issue → location → severity → remediation effort} |
| **Audit Total** | **10-12 hours** | But can be scoped to 6-8 hours if automated tools only |
| | | |
| **Remediation Phase** | **TBD** | Depends on audit findings |
| Implement alt text for unlabeled images | TBD | Per audit report; usually 1-2 hours per 100 images |
| Fix color contrast issues | TBD | May require HTML template CSS changes or complete template redesign |
| Fix heading hierarchy | TBD | Regenerate all article HTML; template changes to ZIM writer |
| Implement keyboard navigation fixes | TBD | May require HTML form redesign or ARIA landmark additions |

**Note**: Candidate 2 has an **uncapped scope post-audit**. You cannot know the remediation effort until the audit is complete. A 10-hour audit could lead to 5 hours of fixes or 40 hours of fixes depending on template design.

#### Dependencies

**No external dependencies**. Candidate 2 can run independently:
- Audit can run against Phase 5.1's HTML templates (frozen at merge)
- Remediation requires template changes, which are decoupled from Candidates 1, 3, 4
- No ORM models, database, or API changes required

**Phase 5.1 dependency (soft)**: Audit is most useful if Phase 5.1 is merged and producing real ZIM files. Auditing the template in isolation gives a false positive ("template looks accessible") vs. real ZIM in Kiwix ("rendering breaks accessibility").

#### Testing Requirements

**Audit tools**:

1. **axe-core** (automated) — Scans HTML for 80+ WCAG violations; integrates with pytest
2. **Pa11y** (automated) — CLI-based accessibility scanner; produces JSON report
3. **aXe DevTools** (manual) — Chrome/Firefox extension; interactive testing

**Verification commands**:

```bash
# Automated: run axe-core on Phase 5.1 HTML template
uv run pytest tests/integration/test_a11y_axecore.py -v

# Automated: Pa11y scan of ZIM HTML
pa11y --config .pa11yrc.json https://localhost:8000/opds/v2/entries > a11y_report.json

# Manual: Interactive testing in Firefox
# 1. Install aXe DevTools from Mozilla Store
# 2. Open ZIM in Kiwix
# 3. Run aXe scan on each article type
# 4. Document findings

# Contrast ratio verification
# https://webaim.org/resources/contrastchecker/
# Test all background-text color combinations from CSS
```

**Test categories**:

| Category | Test | Pass Criteria |
|----------|------|---------------|
| Alt text | 30-50 random images in ZIM have descriptive alt text (not alt="" or "image") | 100% of images have meaningful alt text |
| Color contrast | Body text vs. background in all 3 export variants (pic, nopic, medical-specific) | 4.5:1 contrast ratio (WCAG AA) |
| Heading hierarchy | No h1→h3 jumps; h1 is unique; proper nesting | Valid hierarchical structure |
| Form accessibility | Search form in Kiwix has `<label>` or ARIA; focus is visible | Keyboard accessible, visible focus indicator |
| Screen reader | Sample article in Kiwix + NVDA/TalkBack reads coherently | Screen reader announces: article title, headings, links, images (via alt text) |

#### User Value

**Direct value**: Expands addressable user community from 80% to 96%+ of population (WHO reports 16% of global population has disabilities; WCAG AA covers most common access barriers). Medical and humanitarian domains have especially high accessibility requirements (WHO health worker training materials, ICRC protocols often require A11y compliance).

**Compliance value**: Some institutional deployments (US universities, European public health systems) require WCAG 2.1 AA as a procurement requirement. Audit completion + public report positions open-repo as accessibility-conscious.

**Technical depth**: Demonstrates inclusive design as a core project value, not an afterthought. Signals to potential users and contributors that access is a priority.

**Phase 6 dependency**: Phase 6 multi-language exports, image-inclusive exports, and domain sub-feeds should all be audited for accessibility. Starting in Phase 5.2 creates a pattern for future work.

#### Risk Assessment

| Risk | Probability | Impact | Detection | Mitigation |
|------|-------------|--------|-----------|-----------|
| **Audit uncovers 50+ critical issues** | Medium | Very High (remediation becomes multi-week effort) | Automated scan reports 30+ failures; manual review finds more | Scope decision: accept "audit only" as Phase 5.2 deliverable. Remediation deferred to Phase 6 or future phase. |
| **Color contrast fails on Kiwix WebView rendering** | Medium | High (appears correct in desktop browser, broken on Android) | Manual test: open ZIM in Kiwix Android; text hard to read on device | Test on actual Pi 5 hardware with Kiwix Android; document device-specific rendering issues. |
| **Screen reader announces inaccessible structure** | Medium | High (blind users cannot understand content flow) | Manual test with NVDA/TalkBack; screen reader skips headings or reads in wrong order | Requires manual testing; cannot be automated. Budget extra 2-3 hours for hands-on screen reader evaluation. |
| **Remediation scope exceeds Phase 5.2 timeline** | High | Blocking (audit done but fixes incomplete) | Audit reveals 40+ issues requiring 20+ hours of template redesign | Accept "audit + remediation plan" as deliverable. Prioritize top 5 critical issues for immediate fix. Remainder goes to Phase 6 backlog. |
| **HTML template needs complete redesign** | Low | Very High (affects all future ZIM exports) | Audit suggests heading hierarchy or form structure is fundamentally broken | This is actually valuable: early discovery before production. Reprioritize: template redesign becomes Phase 5.2 focus; OPDS or Search deferred to Phase 6. |

#### Deployment Gate Checklist

Before deploying A11y remediation:

- [ ] Automated audit complete: axe-core report generated; Pa11y scan finished
- [ ] Manual audit complete: 50+ images reviewed for alt text; color contrast verified on 3 devices
- [ ] All 4.5:1 contrast ratio failures documented with CSS locations
- [ ] Heading hierarchy violations mapped to HTML template sections
- [ ] Screen reader manual test: NVDA/TalkBack on sample articles; results documented
- [ ] Remediation plan prepared: {issue → fix → effort hours → priority}
- [ ] Critical issues (blocking content access) addressed before Phase 5.2 close
- [ ] WCAG 2.1 AA audit report published (public or internal)
- [ ] Phase 6 backlog updated with remaining remediation tasks

---

### Candidate 3: Search Engine Integration (Offline Search in ZIM)

#### What It Delivers

Offline full-text search within ZIM files using libzim's built-in Xapian index (already enabled in Phase 5.1) or, for web-UI deployments of kiwix-serve, an optional supplementary search service. The primary search mechanism — Xapian FTS embedded in the ZIM — is already implemented in Phase 5.1. This candidate addresses the separate concern of federation-level search across multiple ZIM files and/or the kiwix-serve web interface.

**Search engine options evaluated for this candidate** (for federation search — not ZIM-embedded search):

| Option | Pi 5 aarch64 support | Thermal risk | Dependency complexity | Notes |
|--------|---------------------|--------------|----------------------|-------|
| **SQLite FTS5** | Native (no binary needed) | None | Zero (stdlib) | BM25 ranking, incremental updates, offline-safe; 30% faster than FTS3/FTS4 |
| **Meilisearch** | Community aarch64 via Arch Linux ARM; no official Pi 5 binary | Medium (Rust process) | Medium (external service) | 40.7k GitHub stars, MIT license, good multilingual support |
| **Typesense** | Linux arm64 .deb exists BUT Pi 5 16K page-size causes jemalloc crash (GitHub #1351, unresolved) | Medium | Medium | GPL-3.0; Pi 5 deployment blocked without kernel workaround |
| **Elasticsearch/OpenSearch** | Official aarch64 builds | High (sustained CPU) | High (JVM required) | Too heavy for Pi 5; ruled out |

**Recommended option**: SQLite FTS5 for any Pi 5-targeted search capability. External services (Meilisearch) are viable for server deployments but add operational complexity. Typesense is blocked on Pi 5 without a kernel-level workaround.

**User-facing outcome**: A clinic in rural Kenya with spotty internet opens "Medical Reference.zim" in Kiwix on a Raspberry Pi. A healthcare worker searches "how to treat severe dehydration" and gets 5 relevant articles ranked by relevance, sorted by keyword frequency. Search results appear in <2 seconds.

**Technical implementation**: During Phase 5.1's ZIM generation, the ZimWriter calls a search indexer to build an inverted index of article titles + body text. That index is embedded in the ZIM's search metadata. Kiwix reads the index and serves search results locally without needing a remote API.

#### Implementation Hours

| Component | Hours | Notes |
|-----------|-------|-------|
| Evaluate Lunr.js vs. Whoosh integration | 1 | Trade-off: Lunr is lightweight but limited; Whoosh is powerful but adds Python runtime overhead |
| Implement search indexer in ZIM writer | 2-2.5 | Add index-building code to Phase 5.1's ZimWriter.create_zim(); invoke after article generation |
| Integrate with libzim's search metadata API | 1-1.5 | libzim exposes a search_index() method; populate it with indexed articles |
| Unit tests: indexer correctness (accuracy, ranking) | 1-1.5 | Test: "aspirin" query returns aspirin article first; "fever relief" returns fever-related articles |
| Integration test: search performance on Pi 5 | 2-3 | Build 500+ article ZIM on Pi 5; measure search latency; verify <2s for typical queries |
| Manual test: Kiwix search bar integration | 0.5 | Open ZIM in Kiwix Android/Desktop; verify search results display correctly |
| **Total** | **8-11 hours** | (Plus 1-2 hours if Whoosh chosen; Lunr is simpler) |

#### Dependencies

**No hard external dependencies**. Search integration is independent of Candidates 1, 2, 4.

**Phase 5.1 integration point**: Search indexing code lives in `app/services/export/zim_writer.py`. That module is frozen/finalized in Phase 5.1. Candidate 3 requires modifying ZimWriter to build and embed the search index before closing the ZIM file. This is a small, contained change.

**Soft dependency on Pi 5 hardware validation**: Search indexing is computationally heavy. The Raspberry Pi 5 has real thermal constraints (idles at 81-84°C, thermal throttles at 87.8°C). Building a 500 MB ZIM with full-text indexing on a Pi 5 may hit thermal limits. **Candidate 3 must be tested on actual Pi 5 hardware** to validate that indexing completes without throttling or timeout.

#### Testing Requirements

**Performance testing** (critical on Pi 5):

1. `test_search_indexing_performance` — Build a 500-article test ZIM; measure indexing latency; must complete in <30 minutes on Pi 5
2. `test_search_query_latency` — Execute 20 typical queries against indexed ZIM; all must return results in <2 seconds
3. `test_search_result_ranking` — Query "aspirin"; verify aspirin article ranks first (not "aspen tree")
4. `test_search_handles_special_characters` — Query "CVA (cerebral vascular accident)"; returns correct articles despite parentheses
5. `test_search_synonyms` — Query "HTN"; returns "hypertension" articles (requires synonym mapping)

**Integration tests**:

6. `test_search_in_kiwix_android` — Open ZIM in Kiwix Android; search "fever"; results display in UI
7. `test_search_index_embedded_in_zim` — Unzip ZIM file; verify search metadata exists and is queryable

**Verification commands**:

```bash
# Performance test
time uv run pytest tests/integration/test_search_performance.py -v -k "test_search_indexing_performance"
# Expected: <30 minutes on Pi 5 for 500-article ZIM

# Latency test
uv run pytest tests/integration/test_search_latency.py -v
# Expected: all queries return <2000ms

# Manual: Kiwix test
kiwix-serve /path/to/test.zim &
# Open kiwix-serve in browser or mobile
# Search bar should be visible and responsive
```

#### User Value

**Direct value**: Usability improvement for users with large ZIM files (500+ articles). Without search, users navigate via table of contents or browse by category. With search, finding specific content (a drug name, a symptom, a technique) is instant.

**Medical domain impact**: Healthcare workers need to find information quickly in clinical settings. Search reduces from "30-second manual navigation" to "2-second search query."

**Phase 6 foundation**: Phase 6 multi-language ZIMs and domain sub-feeds will be searchable across language boundaries if search is implemented. Starting in Phase 5.2 positions search as foundational to future scaling.

**Competitive positioning**: Many offline knowledge platforms (Wikipedia offline, Project Gutenberg apps) have embedded search. Implementing search positions open-repo alongside these tools.

#### Risk Assessment

| Risk | Probability | Impact | Detection | Mitigation |
|------|-------------|--------|-----------|-----------|
| **Indexing causes Pi 5 thermal throttling** | High | Blocking (indexing timeouts; export fails) | Indexing latency >30 min; Pi 5 CPU temp >87.8°C during indexing; `dmesg` shows thermal throttle messages | Test on actual Pi 5 hardware *before* full implementation. If throttling occurs, reduce index granularity (index titles only, not full text) or implement indexing in smaller chunks. |
| **Lunr.js search results rank poorly** | Medium | High (users get irrelevant results) | Manual test: search "fever" returns "cold" or unrelated articles first | Implement ranking function carefully; test with domain-specific queries (medical terms). Consider Whoosh if Lunr ranking insufficient. |
| **Search index bloats ZIM file size significantly** | Medium | Medium (ZIM no longer fits on USB sticks, impacts distribution) | Build test ZIM; compare file size with and without index; measure size increase % | If index adds >10% to ZIM size, negotiate with user: smaller index (titles + summary only) vs. larger ZIM file size. |
| **Kiwix versions don't support embedded search index** | Low | High (Kiwix ignores index; search unavailable) | Kiwix version check; verify API compatibility with target Kiwix versions (Android 3.3+, Desktop 2.0+) | Confirm Kiwix versions in use support embedded search. If not, defer to when Kiwix support is available. |
| **Special character handling (accents, symbols) breaks indexing** | Medium | Medium (non-English content not searchable) | Test queries: "café", "Früchte", "لإ" (Arabic); verify matches | Implement Unicode-aware indexing. Test with multilingual corpora if Phase 5.2 includes non-English exports. |

#### Deployment Gate Checklist

Before deploying search indexing:

- [ ] Indexing performance test on Pi 5: <30 minutes for 500-article ZIM
- [ ] Thermal baseline established: CPU temp during indexing; no throttling observed
- [ ] Search result ranking verified: top 3 results are relevant for 20 test queries
- [ ] Synonym mapping implemented: "HTN" → "hypertension" articles; "CVA" → "cerebrovascular accident"
- [ ] Special character handling tested: accented characters, punctuation, Arabic/CJK if applicable
- [ ] ZIM file size impact measured: index adds <10% to ZIM size
- [ ] Kiwix Android search bar integration tested: search results display in UI
- [ ] Kiwix Desktop search functionality tested: results appear in <2 seconds
- [ ] Manual query latency verified: 20 typical queries return results in <2s each
- [ ] Index metadata embedded in ZIM file and validated
- [ ] Fallback implemented: if search index missing, Kiwix gracefully disables search bar

---

### Candidate 4: API Gateway for Federation

#### What It Delivers

A REST API endpoint (`/api/federation/exports`) that exposes ZIM export metadata and download links to other federation partner nodes. Enables:
- **Data sharing between projects**: Stockbot can query open-repo for latest medical ZIM URL and auto-download
- **Federation interoperability**: Other nodes can discover each other's ZIM exports without manual configuration
- **Cross-project inventory**: A federated network dashboard can list all available ZIM files across all participating nodes

**User-facing outcome**: An administrator of a separate open-source project (e.g., a medical training platform) can configure a cron job to check open-repo's federation API weekly, discover new ZIM exports, and auto-import them for distribution to their community.

#### Implementation Hours

| Component | Hours | Notes |
|-----------|-------|-------|
| Design federation export API schema (JSON response format) | 0.5 | Define: export metadata, version history, cdn_url structure |
| Implement `/api/federation/exports` endpoint | 1.5 | Query zim_exports table (Phase 5.1); serialize to JSON; add filters (language, domain, flavour) |
| Implement `/api/federation/exports/{uuid}` endpoint (single export detail) | 0.75 | Return full export metadata + download link + checksum |
| Add HTTP signature verification (RFC 9421) | 1 | Authenticated federation partners only; verify inbound request signature |
| Unit tests: schema validation, filtering, signature verification | 1-1.5 | Test: correct export list returned; filtering works; unsigned requests rejected |
| Integration test: federation partner can fetch and validate exports | 1 | Simulate partner node making API call; verify response format and authenticity |
| Documentation: API schema + example curl commands | 0.5 | Endpoint reference for partner nodes |
| **Total** | **6-7 hours** | |

#### Dependencies

**Soft dependency on Phase 5.1**: API requires `ZimExport` ORM model (created by Phase 5.1) to exist and have data. However, development can proceed on a separate branch with mock data.

**Phase 4 dependency (hard)**: Candidate 4 requires Phase 4's federation partner registration and HTTP signature verification infrastructure. That infrastructure is already complete (Phase 4 is done). Candidate 4 uses those existing components.

**No dependency on Candidates 1, 2, 3**: API Gateway is independent of OPDS, A11y audit, and search indexing.

#### Testing Requirements

**Unit tests**:

1. `test_federation_exports_endpoint_returns_json` — GET /api/federation/exports returns 200 with valid JSON
2. `test_federation_exports_filtering_by_language` — GET /api/federation/exports?language=en returns English-only exports
3. `test_federation_exports_filtering_by_flavour` — GET /api/federation/exports?flavour=nopic returns nopic variant only
4. `test_federation_exports_http_signature_required` — Unsigned request returns 401; signature-verified request returns 200
5. `test_federation_single_export_endpoint` — GET /api/federation/exports/{uuid} returns full export metadata
6. `test_federation_export_schema_has_required_fields` — Response has cdn_url, sha256, title, language, generated_at

**Integration tests**:

7. `test_federation_partner_can_fetch_exports` — Simulate authenticated partner; fetch export list; verify response structure
8. `test_federation_export_discovery_workflow` — Partner requests exports → gets list → requests specific export → gets download URL

**Verification commands**:

```bash
# Unit tests
uv run pytest tests/unit/test_federation_api.py -v

# Integration test
uv run pytest tests/integration/test_federation_partner_api.py -v -m integration

# Manual: curl test
curl -H "Authorization: Bearer $(generate_signature)" https://localhost/api/federation/exports
# Expected: 200 JSON with export list
```

#### User Value

**Direct value**: Enables federation partner projects to auto-discover and consume open-repo ZIM files without manual admin intervention. Reduces operational friction for multi-project deployments.

**Ecosystem value**: Positions open-repo as a "data source" for other projects, not just a standalone platform. Encourages data reuse and interoperability.

**Phase 6 foundation**: Phase 6's "distributed sync" and "peer-to-peer node synchronization" features depend on federation APIs. Starting in Phase 5.2 establishes the API contract before more complex federation features are added.

**Low-effort high-impact**: Candidate 4 is one of the fastest to implement (4-6 hours) and unblocks future federation work with minimal risk.

#### Risk Assessment

| Risk | Probability | Impact | Detection | Mitigation |
|------|-------------|--------|-----------|-----------|
| **HTTP signature verification fails for partner requests** | Low | High (partners cannot authenticate; API returns 401) | Test: partner makes request with valid signature; gets 401 error | Verify HTTP signature implementation matches RFC 9421; test with known-good library. Use Phase 4's existing signature verification code (already tested). |
| **API response schema doesn't match partner expectations** | Medium | Medium (partner code breaks parsing response) | Partner makes request; gets response; integration test fails | Document API schema clearly. Test with at least one real partner request before production. Provide OpenAPI/Swagger spec. |
| **Export list is large (1000+ exports) and API times out** | Low | Medium (pagination required; adds complexity) | Query zim_exports table with no filters; measure response latency; count rows | Implement pagination: limit=50 default, offset parameter. Add sorting options (newest first). Add caching: `Cache-Control: max-age=3600`. |
| **Partners request old/deleted exports that no longer exist** | Low | Low (return 404 gracefully) | Test: fetch non-existent UUID; expect 404 error | Handle gracefully: return 404 with helpful message. Log all API requests for debugging. |

#### Deployment Gate Checklist

Before deploying API Gateway:

- [ ] `/api/federation/exports` endpoint implemented and returns 200
- [ ] `/api/federation/exports/{uuid}` endpoint implemented and returns full metadata
- [ ] HTTP signature verification required on all federation requests
- [ ] Response schema documented in OpenAPI/Swagger spec
- [ ] Unit tests pass: `uv run pytest tests/unit/test_federation_api.py -v`
- [ ] Integration test with simulated partner passes
- [ ] Pagination implemented for large export lists (limit=50 default)
- [ ] Cache-Control headers set appropriately (max-age=3600 for stability)
- [ ] Error responses formatted consistently (400/401/404 with JSON error details)
- [ ] Rate limiting implemented (optional but recommended for federation)
- [ ] Endpoint documentation published with curl example commands

---

### Candidate 5: Content Domain Expansion

#### What It Delivers

Rather than adding infrastructure features (OPDS, Search, A11y, API), this track expands the substantive knowledge content archived in ZIM files. Phase 5.1 established ZIM export capability for open-repo's existing six domain taxonomy (agriculture, water, food, electronics, building, energy). This candidate fills the critical knowledge gaps identified by cross-referencing open-repo's taxonomy against the user's related active projects: systems-resilience, seedwarden, off-grid-living, and cybersecurity-hardening.

Ten content expansion candidates are detailed in `/projects/open-repo/PHASE_5.2_FEATURE_CANDIDATES.md` and scored in `/projects/open-repo/PHASE_5.2_PRIORITY_MATRIX.md`. The top five for June 2026:

| # | Module | New ZIM Domain | Source documents | Implementation |
|---|--------|---------------|-----------------|---------------|
| 1 | Medical Reference Archiver | `medicine` | off-grid-living 08-medical-health.md, WHO EML | 10-14 hrs |
| 2 | Water Systems Archiver | `water` (deepened) | off-grid-living 03-water.md, USDA/CDC guides | 8-12 hrs |
| 3 | Seed Preservation Archiver | `seeds` | seedwarden project documents, GRIN database | 12-16 hrs |
| 4 | Food Preservation Archiver | `food` (deepened) | USDA Complete Canning Guide, NCHFP datasets | 8-12 hrs |
| 5 | Botanical Knowledge Archiver | `botany` | USDA PLANTS CSV, OpenFarm archive, seedwarden | 12-16 hrs |

**Why this competes with infrastructure candidates**: The infrastructure candidates (OPDS, Search, A11y, API Gateway) improve how existing content is discovered, searched, or accessed. Content expansion increases what content exists. If the goal is "offline access for all humanity," gaps in life-critical domains (medicine, water, food safety) are more urgent than discovery improvements for content that already exists in ZIM format. A user who cannot find the medical reference article they need suffers a worse outcome than a user who cannot browse the library using Kiwix's in-app OPDS catalog.

#### Implementation Hours

Each content module is 8-16 hours of implementation. Five modules in parallel waves:
- Wave 1 (June 1-10): Medical + Water (~22 combined hours, run in parallel)
- Wave 2 (June 8-17): Seed + Food Preservation (~22 combined hours, run in parallel)
- Wave 3 (June 18-24): Botanical (~14 hours)

**Important**: Content domain expansion and infrastructure candidates are NOT mutually exclusive. API Gateway (4-6 hrs) can run in parallel with any content module. OPDS (8-11 hrs) can run in parallel if bandwidth allows.

#### Dependencies

No new Python dependencies for the top-4 content modules (Medical, Water, Seed, Food). Botanical module optionally uses `biopython>=1.87` for FASTA/GenBank parsing.

All content modules share one soft dependency: Phase 5.1 must be merged so the export pipeline can generate real ZIM files from the new content types.

#### User Value

**Direct user value**: Healthcare workers, off-grid homesteaders, disaster responders, and students in low-bandwidth regions access life-critical knowledge that does not yet exist in offline form. The Medical Reference module alone could serve the ~2 billion people globally who lack reliable healthcare access and rely on community health workers using reference materials.

**Cross-project value**: Five content modules directly archive content from the user's four active related projects:
- seedwarden: Seed Preservation and Botanical Knowledge archival
- systems-resilience: Medical, Water, and Food content cross-references
- off-grid-living: Primary source for all five modules
- open-repo: Fills the six existing taxonomy domains with real depth

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| **Medical accuracy liability** | Medium | High | Prominent disclaimer system; cite authoritative sources only (WHO, CDC, ICRC); never synthesize or interpolate dosing data |
| **USDA canning data accuracy** | Low | Very High (botulism risk if data is wrong) | Embed verbatim USDA lookup tables; no interpolation; verify table completeness in unit tests |
| **Content exceeds ZIM size targets** | Low | Low | Each domain ZIM is 1-15 MB; well within domain target (<50 MB) |
| **BioPython dependency for Botanical** | Low | Low | BioPython is optional; botanical module works with static USDA CSV data if BioPython not installed |

#### Deployment Gate

- Phase 5.1 merged; ZIM export pipeline producing valid files
- Medical disclaimer system implemented and reviewed
- USDA processing time tables validated against official source
- Each module's ZIM passes zimcheck; opens in Kiwix Android/Desktop
- Unit test suite: 20-30 tests per module; all passing

---

## Comparative Analysis Matrix

### Implementation Complexity vs. User Value

| Candidate | Implementation Complexity | Code Risk | User Value | Timeline Risk | Recommendation |
|-----------|---------------------------|-----------|-----------|----------------|---|
| **OPDS** | Low-Medium (8-11 hrs, well-scoped) | Low (new code, no existing API changes) | High for Kiwix users; low for Kindle users (Kindle does not support OPDS) | Low (hard deadline at 11 hours) | **Go immediately after Phase 5.1** |
| **A11y Audit** | Medium audit + High remediation (10-12 hrs audit + TBD fix) | Low code risk (documentation-first) | High (expands addressable community) | High (remediation scope unknown; could overflow Phase 5.2) | **Audit in Phase 5.2; remediation Phase 6+** |
| **Search** | Medium (8-11 hrs); SQLite FTS5 is lower risk than Meilisearch/Typesense | Low for FTS5 (stdlib); Medium for Meilisearch (external binary); Typesense blocked on Pi 5 | Medium-High (usability for large corpora; not critical path) | Medium (SQLite FTS5 has no Pi 5 thermal risk; Meilisearch needs validation) | **Use SQLite FTS5; test before committing to Meilisearch** |
| **API Gateway** | Low (4-6 hrs, well-scoped) | Low (no existing API changes; just new endpoint) | Medium (enables federation; not user-facing) | Low (shortest timeline) | **Quick win; can run in parallel with OPDS** |
| **Content Domain Expansion** | Low per module (8-16 hrs each); total scope is large | Low (new importer modules; no infrastructure changes) | Very High (life-critical knowledge for users who have ZIM but lack content) | Low per module; high if too many run in parallel | **Highest long-term mission value; run in parallel with infrastructure track** |

### Phase 5.2 Sequencing Scenarios

#### Scenario A: OPDS First (Recommended)

```
June 1-5:   OPDS implementation (8-10 hrs)
June 5-6:   OPDS testing & validation (1 hr)
June 6-10:  Remaining time: 5 hours
            Option: API Gateway (4-6 hrs, fits with spillover)
            Option: Start Search (incomplete; needs Phase 6)
            Option: A11y Audit begins (6-12 hrs, incomplete; needs Phase 6)

Outcome:    Phase 5.2 = OPDS + (API Gateway or nothing)
            User value: Kiwix in-app discovery + optional federation API
```

**Rationale**: OPDS is the highest-priority unblocking feature. Library partnerships and institutional deployments depend on it. After OPDS lands, if time remains, API Gateway is a low-risk quick win. Search and A11y audit both risk extending beyond the June 1-12 window.

#### Scenario B: Search First (If User Prioritizes Offline Search)

```
June 1-6:   Search integration & Pi 5 thermal testing (8-10 hrs)
June 6-12:  Remaining time: 5-6 hours
            Option: OPDS (8-11 hrs, doesn't fit fully)
            Option: A11y Audit begins (incomplete)
            Option: API Gateway (4-6 hrs, fits exactly)

Outcome:    Phase 5.2 = Search + (API Gateway or nothing)
            User value: Offline search + optional federation API
            Risk: OPDS deferred to Phase 6 (affects institutional partnerships)
```

**Rationale**: If offline search is more valuable to target users than in-app discovery, start with Search. Caveat: if Pi 5 thermal throttling is discovered mid-implementation, redesign needed; Search could balloon to 15+ hours, leaving no time for OPDS.

#### Scenario C: API Gateway First + OPDS Second

```
June 1-3:   API Gateway implementation (4-6 hrs)
June 3-5:   API Gateway testing (0.5-1 hr)
June 5-12:  OPDS implementation (8-11 hrs, fits with spillover or fills June 5-12)

Outcome:    Phase 5.2 = API Gateway + OPDS
            User value: Federation API + Kiwix discovery
            Risk: Low; both complete within timeline
```

**Rationale**: Run two projects in parallel to maximize throughput. API Gateway is fast and low-risk; OPDS is foundational. Both together maximize user impact.

#### Scenario E: Content Domain Expansion as Phase 5.2 Primary Focus

```
June 1-10:  Medical + Water systems modules (22 hrs parallel, 2 engineers)
June 8-17:  Seed + Food Preservation modules (22 hrs parallel, 2 engineers)
June 18-24: Botanical module (14 hrs)
June 1-3:   API Gateway (4-6 hrs, runs in parallel with Medical)

Outcome:    Phase 5.2 = 5 content domain modules + API Gateway
            User value: Life-critical offline knowledge (medicine, water, food, seeds, plants)
            Risk: Low per module; requires discipline to not scope-creep on medical content
```

**Rationale**: Phase 5.1 delivered ZIM export infrastructure. Phase 5.2's highest-value contribution may be filling that infrastructure with life-critical content rather than adding more infrastructure layers. Five content modules deliver ~2,340 lines of new code, 10 new content types, 100-150 new unit tests, and 5 new domain ZIM files that directly serve the user's core mission and related projects (seedwarden, systems-resilience, off-grid-living).

#### Scenario D: A11y Audit First (If Accessibility Is Priority)

```
June 1-10:  A11y audit (10-12 hrs) + selective remediation (4-6 hrs of critical issues)
June 10-12: Remaining time: 0 hours
            No time for OPDS, Search, or API Gateway

Outcome:    Phase 5.2 = A11y Audit + Remediation Plan
            User value: Audit report + roadmap for Phase 6 remediation
            Risk: No feature delivery; User impact deferred 1-2 months
```

**Rationale**: A11y is important but audit-only is not a sufficient Phase 5.2 deliverable without remediation. If accessibility is a top priority, it should pair with OPDS or API Gateway, not standalone.

---

## Pi 5 Thermal Constraints Impact

### Current Baseline (from memory)

- **Idle temperature**: 81-84°C
- **Under compute**: 87.8°C (thermal throttling threshold)
- **Post-checkpoint extended compute**: Blocked until cooling installed

### Candidate Impact Analysis

| Candidate | Compute Intensity | Thermal Risk | Mitigation |
|-----------|-------------------|--------------|-----------|
| **OPDS** | Very low (XML generation) | None | No action needed |
| **A11y Audit** | Very low (mostly scanning local HTML) | None | No action needed |
| **Search** | **Very high** (full-text indexing of 500+ articles) | **High** | Must test on Pi 5; if throttling, reduce index scope (titles only) |
| **API Gateway** | Very low (database query + JSON serialization) | None | No action needed |

**Search-specific risk**: Building a full-text inverted index on Pi 5 during ZIM generation could cause sustained CPU load at 100% for 20-30 minutes. If Pi 5 thermal throttles below 1.5 GHz, indexing timeouts are possible.

**Mitigation for Search**:
1. Test indexing on actual Pi 5 with a 500-article test ZIM
2. Measure latency and CPU temperature during indexing
3. If temperature >87°C, implement tiered indexing: build partial index during export, complete full index during off-peak hours
4. Or reduce index granularity: index article titles + summaries only (not full body text)

---

## Recommendation for User Decision (May 26-27)

### Decision axis: Infrastructure vs. Content

This is the primary strategic question for Phase 5.2. The answer determines which of the scenarios above applies.

**Infrastructure track** (OPDS, Search, A11y, API Gateway): Improves how existing ZIM content is discovered, searched, and accessed. Appropriate if Phase 5.1 content depth is already sufficient and the priority is expanding distribution reach.

**Content expansion track** (Medical, Water, Seed, Food, Botanical): Increases what knowledge exists in ZIM format. Appropriate if the priority is fulfilling the "offline knowledge for all humanity" mission by filling critical knowledge gaps.

**The recommendation is to run both tracks in parallel at different scales**:
- API Gateway (4-6 hours, very low risk): Run in Week 1 alongside the first content module
- OPDS (8-11 hours, low risk): Run in Week 2 as a second parallel track
- Content Domain Wave 1 (Medical + Water, 22 hours parallel): Primary June 1-10 work
- Content Domain Wave 2 (Seed + Food, 22 hours parallel): June 8-17
- Search and A11y: Defer to Phase 6; thermal constraints on Pi 5 make Search high-risk, and A11y audit scope is uncapped

### Recommended Sequencing (Optimal for June 1-12 window)

```
June 1-3:   API Gateway (4-6 hrs) — fast win, unblocks federation
June 1-10:  Medical Reference Archiver (10-14 hrs, parallel with API Gateway + OPDS)
June 4-12:  OPDS Feed Generation (8-11 hrs, parallel with Medical content work)
June 8-17:  Water Systems Archiver (8-12 hrs, parallel with OPDS completion)

Phase 5.2 result: API Gateway + OPDS + Medical + Water
User value: Federation API + Kiwix discovery + life-critical knowledge offline
Risk: Low (all four are well-scoped and do not block each other)
```

### Fallback Sequencing (Single-engineer, linear)

```
June 1-3:   API Gateway (5 hrs)
June 3-8:   OPDS (9 hrs)
June 8-18:  Medical Reference (12 hrs)
June 18-26: Water Systems (10 hrs)
```

### If User Prioritizes Infrastructure Only

**Priority 1 (June 1-5): OPDS Feed Generation**
- **Why**: Unblocks Kiwix in-app discovery; enables library partnerships; positioned for Phase 6
- **Timeline**: 8-11 hours; fits comfortably in June 1-12 window
- **Risk**: Low; well-scoped; existing code patterns from Phase 4/5.1
- **Note**: OPDS value is Kiwix discovery, not Kindle/Kobo (Kindle does not support OPDS)

**Priority 2 (June 5-12, if time remains): API Gateway**
- **Why**: Enables federation interop; low-risk quick win; positions for Phase 6 distributed sync
- **Timeline**: 4-6 hours; can run in parallel with OPDS or sequentially after
- **Risk**: Low; depends on Phase 4 (already complete)

**Deferred to Phase 6**: Search indexing + A11y audit
- **Search**: Use SQLite FTS5 if search is needed on Pi 5; avoid Typesense (Pi 5 page-size bug); validate Meilisearch on actual Pi 5 hardware before committing
- **A11y**: Audit valuable but remediation scope unknown; better tackled after audit is complete

### If User Prioritizes Content Mission

**Priority 1 (June 1-10): Medical Reference + Water Systems in parallel**
- **Why**: Highest life-safety value; source documents already exist (off-grid-living, WHO, CDC)
- **Timeline**: 22 combined hours across two parallel modules; fits June 1-10 window with two engineers

**Priority 2 (June 1-3, parallel with Priority 1): API Gateway**
- **Why**: Low-effort quick win; enables federation partners to consume new ZIM exports

**Deferred to Phase 6**: OPDS, Search, A11y

---

## Implementation Prerequisites for All Candidates

### Phase 5.1 Merge Status

All candidates assume Phase 5.1 (ZimWriter) is merged by June 1:

- [ ] Feature branch `feature/zimwriter-libzim-activation` merged to main
- [ ] Pre-activation checklist complete: security gaps fixed, ORM model added, dependencies updated
- [ ] Database migration applied: `zim_exports` table created
- [ ] First ZIM export run successfully; at least one row in zim_exports with status='available' and cdn_url populated
- [ ] All 88+ Phase 5.1 tests passing
- [ ] Manual Kiwix verification: exported ZIM opens in Kiwix Android/Desktop; content renders correctly

### Common Development Setup (All Candidates)

```bash
# 1. Pull latest main (after Phase 5.1 merge)
git fetch origin main
git pull origin main

# 2. Create feature branch for Phase 5.2 candidate
git checkout -b feature/phase-5-2-{candidate-name}

# 3. Install dev dependencies (once per repo)
cd projects/open-repo/backend
uv pip install -e ".[dev]"

# 4. Verify database is running and migrations are applied
export DATABASE_URL="postgresql+asyncpg://postgres:postgres@localhost:5432/open_repo"
alembic upgrade head

# 5. Run existing test suite to establish baseline
uv run pytest tests/ -v --tb=short
# Expected: 255+ tests passing (Phase 4 baseline + Phase 5.1)

# 6. Start development loop
uv run uvicorn app.main:create_app --reload --host 127.0.0.1 --port 8000
```

---

## Success Criteria & Measurement

### OPDS Success Criteria

- [ ] Kiwix Android user can add `/opds/v2/root.xml` URL to library browser
- [ ] Archive appears in Kiwix library with title, file size, language, publication date
- [ ] User taps Install button; ZIM downloads automatically from cdn_url
- [ ] Version history appears for exports with multiple versions
- [ ] All 23 OPDS tests pass; no regressions in Phase 4 tests

### Search Success Criteria

- [ ] ZIM file built on Pi 5; indexing completes in <30 minutes without thermal throttle
- [ ] User searches "aspirin" in Kiwix; aspirin article appears in top 3 results
- [ ] Search latency <2 seconds for 20 typical queries
- [ ] Special character queries ("café", "Früchte") return correct results
- [ ] Index size adds <10% to ZIM file size

### A11y Audit Success Criteria

- [ ] Automated audit report generated (axe-core, Pa11y)
- [ ] Manual audit complete: 50+ images reviewed; color contrast verified on 3 devices
- [ ] WCAG 2.1 AA violations documented with severity, location, remediation effort
- [ ] Screen reader manual test: NVDA/TalkBack on sample articles; results recorded
- [ ] Remediation plan prioritized: critical issues (blocking access) vs. non-critical enhancements
- [ ] Public or internal audit report published

### API Gateway Success Criteria

- [ ] GET /api/federation/exports returns 200 with export list JSON
- [ ] GET /api/federation/exports?language=en filters by language
- [ ] Unsigned requests return 401; signature-verified requests return 200
- [ ] Partner can authenticate with HTTP signature; fetch export list; access download URLs
- [ ] Response schema documented in OpenAPI spec
- [ ] All 8+ federation API tests passing

---

## Conclusion & Next Steps

The user should decide by **May 27 13:00 UTC**:

1. **Infrastructure vs. Content primary track?** Infrastructure (OPDS, API Gateway, Search, A11y) vs. Content Domain Expansion (Medical, Water, Seeds, Food, Botanical) — or both in parallel
2. **Which infrastructure candidates are in scope?** (OPDS + API Gateway recommended; Search and A11y deferred)
3. **Which content modules are in scope?** (Medical + Water as Wave 1; Seed + Food as Wave 2)
4. **Should Search use SQLite FTS5 or an external engine?** (SQLite FTS5 strongly recommended for Pi 5 given Typesense page-size bug and Meilisearch's unofficial ARM64 status)
5. **Should A11y audit be Phase 5.2 or Phase 6?** (recommend Phase 6 unless accessibility is top-priority)

Related documents:
- Detailed content expansion candidates: `/projects/open-repo/PHASE_5.2_FEATURE_CANDIDATES.md`
- Content priority scoring: `/projects/open-repo/PHASE_5.2_PRIORITY_MATRIX.md`
- Phase 5.1 → 5.2 handoff checklist: `/projects/open-repo/PHASE_5.2_CAPABILITY_AUDIT.md`

Once the decision is made, implementation begins immediately June 1. All deliverables (code, tests, documentation) will be production-ready by June 12, 2026.

---

**Analysis completed**: 2026-05-26 (updated with research corrections)
**Ready for user decision**: Yes
**Production implementation ready**: Yes

## Sources

- [OPDS 1.2 Specification](https://specs.opds.io/opds-1.2.html)
- [OPDS 2.0 Draft (JSON-LD/Readium)](https://drafts.opds.io/opds-2.0)
- [feedgen PyPI — Snyk health analysis (inactive status confirmed)](https://snyk.io/advisor/python/feedgen)
- [feedgen PyPI page](https://pypi.org/project/feedgen/)
- [Meilisearch vs Typesense 2026 comparison](https://www.meilisearch.com/blog/meilisearch-vs-typesense)
- [Meilisearch aarch64 — Arch Linux ARM packages](https://archlinuxarm.org/packages/aarch64/meilisearch)
- [Typesense Raspberry Pi 5 16K page-size issue (GitHub #1351)](https://github.com/typesense/typesense/issues/1351)
- [SQLite FTS5 Extension documentation](https://sqlite.org/fts5.html)
- [E-Reader Market Share 2025 — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/e-reader-market)
- [OpenAPI Specification v3.2.0](https://spec.openapis.org/oas/v3.2.0.html)
- [ActivityPub W3C standard](https://www.w3.org/TR/activitypub/)
- [Kiwix OPDS wiki documentation](https://wiki.kiwix.org/wiki/OPDS)  
