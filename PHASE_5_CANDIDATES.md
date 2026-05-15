# Phase 5 Candidates

**Status**: Planning (PR #1 open, awaiting merge)  
**Date**: 2026-05-15  
**PR**: https://github.com/esca8peArtist/open-repo/pull/1

---

## Phase 4 Summary (PR #1 Deliverables)

PR #1 ("Wave 4 Phase 2 — Federation Service Infrastructure") delivered the complete federation
layer for the open-repo backend. Specific deliverables:

- **Partner registration API**: endpoints for registering federated nodes with input validation
- **Federation service layer**: centralized request/response handling, activity routing
- **Admin routes**: dashboard for managing partner registrations and federation status
- **HTTP signature verification**: RFC 9421-compliant cryptographic verification of inbound requests
- **Request signing**: automatic signing of outbound federation activities
- **Conflict detection**: detection and logging of concurrent-edit conflicts in federated data
- **Test coverage**: 194 tests passing (4 skipped, 0 failures) across unit, integration, and
  admin route tests

The backend now has a functional federation stack. The `ZimWriter` and `OPDSCatalogService`
stubs (for offline export) also exist in `app/services/export/` but are not yet wired to
`libzim` — every integration point carries a `TODO(post-PR-merge)` marker.

---

## Candidate Items

### Candidate 1 — ZimWriter libzim Integration (Phase 5 Step 2 activation)

**Title**: Implement python-libzim integration in `ZimWriter`

**Description**:  
`app/services/export/zim_writer.py` contains a complete class hierarchy (metadata models,
`ExportConfig`, `ZimWriter`, article rendering) with stub placeholders at every `libzim.Creator`
call site. The stubs write a plain-text placeholder file instead of a real ZIM archive, and
`zimcheck` validation is explicitly disabled during this phase. Activating the real integration
requires:

1. Add `libzim>=3.2,<4.0` to `pyproject.toml`
2. Replace `_stub_write_placeholder()` calls with a proper `libzim.writer.Creator` context
3. Wire `add_article()` and `add_image_resource()` to `creator.add_item()`
4. Enable Xapian indexing (`creator.config_indexing(True, "eng")`)
5. Re-enable `zimcheck` subprocess validation in `run_zimcheck()`
6. Run the 84 existing export pipeline tests — they already cover the public interface;
   the stubs will swap out without changing test signatures

This is the highest-value single item: everything downstream (OPDS catalog, CDN upload,
scheduled exports) depends on producing a valid ZIM file.

**Effort estimate**: 4-6 hours  
**Rationale**: The scaffold is 100% complete. The change is additive — no new API surface,
no schema migrations, no cross-service coordination. It is fully independent of the PR review
outcome (the export module does not share code paths with the federation layer under review).  
**PR dependency**: None — can be developed on a separate feature branch right now. Must not
be merged to main until PR #1 lands (to keep the git history clean), but development and
testing can proceed immediately.

---

### Candidate 2 — OPDS Catalog feedgen Migration and Schema Completion

**Title**: Migrate OPDS generator from raw XML to `feedgen` and complete OPDS 1.2 schema

**Description**:  
`app/services/export/opds_generator.py` currently builds OPDS XML using Python's `xml.etree`
directly. The file contains four `TODO(post-PR-merge)` markers for deferred work:

- Switch to `feedgen` library for cleaner namespace handling (line 353)
- Add `dc:language`, `dc:issued`, and `opensearch` elements on the root feed (line 544)
- Add version-history sub-entries per catalog entry (line 396)
- Add a proper OPDS search endpoint (line 442)

Additionally, the `OPDSEntry.from_zim_export()` factory method is listed as a TODO (line 155),
meaning the catalog currently cannot be populated from real ZIM export records — it requires
manual construction of `OPDSEntry` objects.

Completing this item means:

1. Add `feedgen>=0.9` to `pyproject.toml`
2. Rewrite `OPDSCatalogService._build_feed_xml()` to use feedgen atoms
3. Implement `OPDSEntry.from_zim_export(zim_export_orm_row)` so the catalog populates from DB
4. Add missing OPDS 1.2 elements and validate output against the spec
5. Add/update unit tests — the existing OPDS test suite has 19 tests that already exercise
   the public interface; most should pass without modification after the swap

**Effort estimate**: 3-4 hours  
**Rationale**: OPDS is the in-app discovery mechanism for Kiwix Android and Desktop. Without
a valid OPDS catalog, users cannot discover or download archives from within the Kiwix app —
they must use a direct URL. Completing this item eliminates that UX gap. It is also independent
of federation code and has no migration dependency.

---

### Candidate 3 — README Accuracy Pass and New-Contributor Setup Guide

**Title**: Update README to reflect Phase 4 state and add a contributor quickstart

**Description**:  
The backend `README.md` was last updated at Phase 2 completion. It currently states:

- "Status: Phase 2 Complete" (line 4)
- "35 passing tests" (line 40) — actual count is 194
- The project structure diagram omits `app/api/v1/`, `app/services/`, `app/http_signatures.py`
- The "Next Phases" section describes Phase 3 (contributions) as the next step
- The development server command binds to `0.0.0.0` (line 93) — a violation of the project
  security rule requiring specific interface binding (`127.0.0.1`)
- `API.md` is stamped "MVP Phase 1" and does not document any federation or export endpoints

For a public repository, an outdated README is a friction point that deters contributors.
Required updates:

1. Correct status line, test count, and phase description
2. Update the project structure diagram to match the actual directory tree
3. Fix the `--host` flag: `uvicorn app.main:create_app --reload --host 127.0.0.1 --port 8000`
4. Update "Next Phases" to reference Phase 5 (offline export / Kiwix)
5. Add a brief section on the federation endpoints and their authentication model
6. Update `API.md` version and endpoint list to cover Wave 4 routes

**Effort estimate**: 2-3 hours  
**Rationale**: This is purely a documentation task. It requires no code changes, no test
changes, and no dependency updates. It can be done on a feature branch right now, merged
independently, and is valuable regardless of when PR #1 merges. It also fixes a live security
concern (`0.0.0.0` binding in the developer quickstart).

---

## Recommendation

**Recommended order**:

1. **Candidate 3 (README / docs)** — Start here. Zero risk, zero dependencies, immediately
   mergeable. Fixes the `0.0.0.0` binding issue in the quickstart (security rule violation)
   and brings the public-facing documentation in line with the actual codebase state. Any
   community member looking at the repo right now sees Phase 2 documentation for a Phase 4
   project.

2. **Candidate 1 (ZimWriter libzim integration)** — After the docs PR lands, open a feature
   branch for the libzim activation. This is the critical path item for Phase 5: nothing
   downstream (OPDS, CDN, scheduled exports) is useful without a valid ZIM file. The stubs
   are comprehensive enough that the implementation is a fill-in exercise, not a design
   exercise.

3. **Candidate 2 (OPDS feedgen migration)** — Third, because it depends on Candidate 1
   completing: `OPDSEntry.from_zim_export()` needs real ZIM export records to be meaningful,
   and those only exist after ZimWriter produces valid output. The feedgen rewrite can be
   developed in parallel with Candidate 1 if bandwidth allows, but should not be merged first.

**What to hold**: The Phase 5 week-by-week timeline in `PHASE_5_ARCHITECTURE.md` prescribes
a "Week 1: Kiwix format learning" checkpoint. All three candidates above let the team build
confidence with libzim and OPDS before touching database migrations or CDN infrastructure.
None of them require PR #1 to be merged before starting.
