---
title: "Phase 5.1 Post-Merge Verification Report"
project: open-repo
phase: "5.1"
created: 2026-05-22
status: VERIFIED — stub still active on local master; real implementation on open-repo/main remote
scope: "Post-merge state audit: libzim compatibility, schema validation, dependency check, performance baseline, thermal risk, documentation gaps"
audience: thorn — activation decision support
---

# Phase 5.1 Post-Merge Verification Report

**Verification date**: 2026-05-22 (Session 1500)
**Executor**: research agent (live code audit, test execution, benchmarking)
**Word count**: ~3,000

---

## Executive Summary — Most Important Finding First

PR #3 ("feat(zimwriter): Phase 5.1 MVP — libzim activation + zim_exports migration") was merged to the `open-repo/main` remote branch on May 19, 2026 by user `esca8peArtist`. The real libzim Creator integration exists on that remote. **However, local `master` diverged: it still contains the stub implementation.** The feature branch code that activates libzim has not been rebased or merged into the SuperClaude_Framework local master.

This creates an important split in the post-merge narrative:

- `open-repo/main` (remote): Real libzim, no stub, migration 003 present, 84 tests
- Local `master`: Stub still in `create_zim()`, `_LIBZIM_AVAILABLE` removed, migration 003 absent in working tree, ZimExport ORM added separately (commit 274eb1f2), 88 tests passing (including 4 new integration tests from commit 198a146d)

The verification below addresses the **actual state on local master** and what must be reconciled before Phase 5.1 goes live.

---

## 1. Libzim Python Bindings Version Compatibility

### Installed Version

| Component | Version | Status |
|-----------|---------|--------|
| libzim Python package (PyPI) | 3.10.0 | Installed in `.venv` |
| libzim C++ bundled library | 9.7.0 | Confirmed via `get_libzim_version()` |
| Python runtime | 3.11.2 (CPython) | aarch64 |
| Wheel platform | `manylinux_2_27_aarch64.manylinux_2_28_aarch64` | Confirmed in dist-info |

Verification command run:
```
/home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/.venv/bin/python -c \
  "from libzim.writer import Creator, Item, StringProvider, Hint; \
   from libzim.version import get_libzim_version; \
   print(get_libzim_version())"
# Output: 9.7.0
```

All writer classes (`Creator`, `Item`, `StringProvider`, `Hint`) import without error. The wheel is correctly resolved for `cp311-aarch64-manylinux_2_28`.

### March 2026+ Release Analysis

The task context asked specifically about releases from March 2026 onward. The most recent releases in the `>=3.2,<4.0` window are:

- **3.9.0** (released approximately Q4 2025) — wheel for `cp311-aarch64` confirmed via prior download test (8.3 MB)
- **3.10.0** (released approximately April/May 2026 — confirmed "May 19, 2026" by previous session audit) — currently installed (8.3 MB wheel, same size)

The pyproject.toml on `open-repo/main` pins `libzim>=3.2,<4.0`. Local master's pyproject.toml was updated to `libzim>=3.10.0,<4.0` via commit 274eb1f2. Both constraints are satisfied by the installed 3.10.0.

**Compatibility verdict**: Full compatibility confirmed. libzim 3.10.0 on aarch64/Pi5 with Python 3.11.2 is the production wheel. No source-build fallback is needed. The C++ library version (9.7.0) is the libzim core version bundled in the wheel; this is the version that will be called by `Creator`.

**ARM64/Pi5 specifics**: No known ARM64 incompatibilities with libzim 3.x. The manylinux wheel bundles its own Xapian, so no system Xapian installation is required. Confirmed that `pkg-config --modversion xapian-core` returns "not installed" and this does not block the wheel.

### Critical Gap: `_LIBZIM_AVAILABLE` Removed from Local Master

The local master's `zim_writer.py` no longer contains the `_LIBZIM_AVAILABLE` flag or the `try/except ImportError` guard. The import is an unconditional top-level import on `open-repo/main` (the remote). On local master, the `from libzim.writer import` block was removed entirely along with the conditional logic.

This means:
- Import of `_LIBZIM_AVAILABLE` from `zim_writer.py` will raise `ImportError` (confirmed by live test)
- The current `create_zim()` on local master always calls `_stub_write_placeholder()` regardless of whether libzim is installed

---

## 2. Schema Validation of ZIM Stub Articles

### Corpus Size and Claim Reconciliation

The task referenced "84 ZIM stub articles." The actual corpus in `data/openfarm_procedures.jsonl` contains **32 articles**, not 84. The number 84 refers to the test suite size (84 tests on the feature branch; 88 on local master). No separate ZIM stub article set exists as a standalone file.

The 32 OpenFarm procedure articles are the intended input corpus for Phase 5.1 MVP exports.

### Full Corpus Schema Validation (32/32)

All 32 records were validated against the mandatory field set. Results:

| Field | Present in 32/32 | Notes |
|-------|-----------------|-------|
| `@context` | 32/32 | Three-element array: ActivityStreams, Schema.org, OpenRepo NS |
| `@type` | 32/32 | Always `"procedure"` |
| `cid` | 32/32 | Always `"sha256-"` prefix + 64 hex chars |
| `title` | 32/32 | Multilingual object with `"en"` key |
| `domain` | 32/32 | Always `"procedural"` |
| `license` | 32/32 | Always `"CC0-1.0"` |
| `language` | 32/32 | Array `["en"]` |
| `outcome` | 32/32 | Present in all records |
| `difficulty` | 32/32 | `"beginner"` or `"intermediate"` |
| `steps` | 32/32 | Non-empty in all records |

**CID path validation**: All 32 CIDs match `^sha256-[a-f0-9]{64}$`. These are safe to use directly as ZIM article paths (no characters that require URL-encoding).

### Random Sample Deep Validation (10 of 32)

Seed 42 sample validated for field presence, CID format, type/domain correctness, step non-emptiness:

```
[OK] ...f50620562af1006c | Growing Basil: From Seed to Kitchen       steps=3
[OK] ...12a7ff0c60c5ebc3 | Growing Potatoes: Earthing Up             steps=4
[OK] ...6284c84ab3baabdb | Growing Sweet Potatoes in Warm Climates   steps=4
[OK] ...383cba9fab1a9455 | Growing Onions from Sets                  steps=3
[OK] ...c66443a3fb8dfab6 | Growing Chives: Hardy Perennial Allium    steps=3
[OK] ...6e212732d7168f88 | Growing Parsley: A Patient Herb           steps=3
[OK] ...954a487d947eaa23 | Growing Carrots: Soil Preparation         steps=4
[OK] ...0bf95597c7203da6 | Establishing Thyme as a Perennial Herb    steps=3
[OK] ...ffc6f16a51368ec4 | Growing Strawberries: Year One            steps=4
[OK] ...4dcb868ec0645394 | Growing Cilantro: Managing Bolt-Prone     steps=3
```

Overall result: **10/10 PASS** across all validation criteria.

### Content Metrics

| Metric | Min | Max | Average |
|--------|-----|-----|---------|
| Steps per article | 3 | 5 | 3.4 |
| Words per article | 153 | 248 | 193 |
| Total corpus words | — | — | 6,162 |

The corpus is small and tightly structured. Each article renders to roughly 1–3 KB of HTML. Total corpus size pre-compression is approximately 100–200 KB of HTML content, making this an ideal performance baseline corpus.

### Schema Consistency Assessment

All records are sourced from the same OpenFarm import pipeline and exhibit identical structural consistency. There are no schema version mismatches, no records with missing mandatory fields, and no CID format anomalies. The corpus is ready for ZIM ingestion.

**One concern**: The `steps[].body.en` field contains embedded environment/soil/light metadata in parenthetical blocks (e.g., "Sun requirement: Full Sun. Minimum growing temperature: 7°C."). This is human-readable in HTML but would benefit from structured rendering in the Kiwix template. Not a blocker, but a Phase 5.2 styling task.

---

## 3. Dependencies and System Packages Validation

### pyproject.toml — Current State on Local Master

```toml
[project.dependencies]
  "fastapi>=0.104.0",
  "uvicorn[standard]>=0.24.0",
  "pydantic>=2.0.0",
  "pydantic[email]>=2.0.0",
  "asyncpg>=0.29.0",
  "sqlalchemy>=2.0.0",
  "alembic>=1.13.0",
  "python-multipart>=0.0.6",
  "meilisearch>=0.30.0",
```

**Critical finding**: `libzim>=3.10.0,<4.0` is listed in local master's pyproject.toml (added by commit 274eb1f2). The venv has libzim 3.10.0 installed. This is confirmed consistent.

**But** the `open-repo/main` remote still pins `libzim>=3.2,<4.0`. If the remote is the deployment target, the pin there should be upgraded to `>=3.10.0,<4.0` to match the installed wheel version and harden against 3.2–3.9 regressions.

### Dependency Installation Status

| Package | Version Installed | Source | Status |
|---------|-----------------|--------|--------|
| libzim | 3.10.0 | .venv site-packages | INSTALLED |
| fastapi | present (via venv) | pip | INSTALLED |
| sqlalchemy | present | pip | INSTALLED |
| alembic | present | pip | INSTALLED |
| pytest | 7.4.4 | pip | INSTALLED |
| pytest-asyncio | 0.23.8 | pip | INSTALLED |

**System packages gap**: `zimcheck` (from the `zim-tools` Debian package) is NOT installed. Verification: `which zimcheck` returns nothing; `dpkg -l | grep zim-tools` returns nothing.

This matters because `create_zim(run_zimcheck=True)` will silently skip validation when `zimcheck` is not found (`_run_zimcheck()` returns `True` when `self.zimcheck_binary` is falsy). Exports will appear to succeed validation but will not actually be checked.

### jinja2

`jinja2` is referenced in some older Phase 5 docs as a dependency. It is NOT in pyproject.toml and is NOT required by the current `zim_writer.py` (which uses direct string concatenation for HTML, not templates). Not a blocker; remove from documentation if mentioned.

### Summary: Dependency Gaps Before Activation

| Item | Status | Priority |
|------|--------|----------|
| libzim 3.10.0 in venv | INSTALLED | Done |
| libzim pin in pyproject.toml | `>=3.10.0,<4.0` on local master | Done |
| zimcheck binary | NOT INSTALLED | Required before activation |
| jinja2 | Not needed | Low (remove from docs) |
| migration 003 in working tree | ABSENT from local master | Required before deployment |

---

## 4. Performance Baseline: Write-Time Testing on Pi 5

### Benchmark Conditions

- **Platform**: aarch64 (Raspberry Pi 5)
- **OS**: Debian GNU/Linux 12 (Bookworm)
- **Python**: 3.11.2
- **libzim**: 3.10.0 (C++ 9.7.0)
- **Corpus**: 32 OpenFarm procedure articles, average 193 words/article
- **Baseline temperature**: 80.7°C (idle, measured during verification)

### Benchmark Result — Stub Path (Current Local Master)

The local master `create_zim()` always calls `_stub_write_placeholder()`. The benchmark completed in:

```
Articles: 32
File size: 109 bytes (0.1 KB)
Generation time: 0.000s
Output type: STUB TEXT (not real ZIM)
```

This confirms the stub is active and measures essentially zero. **This is not a useful performance baseline** — the stub writes a 109-byte text file with no ZIM structure.

### Estimated Performance for Real libzim Creator (Remote Main Implementation)

The real `create_zim()` on `open-repo/main` uses:
1. `creator = Creator(str(output_path))` — opens output file, initializes ZIM writer
2. `creator.config_compression(Compression.zstd)` — configures Zstandard compression
3. `creator.config_indexing(True, language_iso3)` — initializes Xapian index
4. Context manager entry — begins article accumulation
5. 32 `creator.add_item(ArticleItem(entry))` calls — each encodes article to UTF-8, passes to C++ layer
6. Context manager exit — triggers Xapian indexing + Zstandard compression + ZIM file finalization

**Estimated wall-clock time for 32-article corpus on Pi 5**:

Based on libzim documentation and known Pi 5 performance characteristics:
- ZIM creation initialization (Xapian, zstd): 0.2–0.5 seconds
- Per-article encoding and indexing: approximately 5–20ms each
- Finalization and compression pass: 0.5–2.0 seconds
- **Total estimate for 32 articles**: 1.0–3.5 seconds

For the 500-article test case asked about in the task spec:
- Per-article time scales approximately linearly until Xapian RAM usage becomes an issue (unlikely at 500 articles)
- **Total estimate for 500 articles**: 10–40 seconds

These estimates have medium confidence (not executed against real libzim Creator on this hardware — the stub blocks it on local master). The first-run real benchmark should be captured during Stage B.3 activation.

### Corpus Scaling Concerns

At the current seed data size (32 articles, ~6,200 words, ~200 KB HTML), the ZIM output will likely be 500 KB – 2 MB depending on Xapian index size. This is well within Pi 5 memory and I/O constraints.

The memory concern (ZimWriter buffers all entries before `create_zim()`) becomes relevant at approximately 5,000 articles. At 32 articles, each entry holding ~2 KB of HTML, the buffer is approximately 64 KB — negligible.

---

## 5. Thermal Throttling Risk Assessment

### Current Baseline

**Idle temperature recorded during verification: 80.7°C**

This is the resting temperature with no active compute workload. This is 0.7°C above the previously documented idle range of 81–84°C — still within range but at the lower bound.

### Throttling Thresholds on Raspberry Pi 5

The BCM2712 (Pi 5 SoC) thermal management:
- **Soft throttle onset**: 80°C (frequency begins scaling down)
- **Hard throttle**: 85°C (aggressive clock reduction)
- **Emergency shutdown**: 85°C+ sustained (thermal protection)

At 80.7°C idle, the Pi 5 is **already at the soft throttle boundary**. Any sustained compute load will push into the throttle band immediately.

### Impact on ZIM Export

For a 32-article export (estimated 1–3.5 seconds):
- **Risk**: LOW. A 3-second burst will not sustain heat long enough for thermal protection to engage
- Temperature may peak at 82–84°C during the 3-second window, then return to baseline

For a 500-article export (estimated 10–40 seconds):
- **Risk**: MEDIUM-HIGH. Sustained compute for 30+ seconds at 80.7°C baseline will push into 85°C+ range
- At 87°C (previously observed under compute), CPU frequency scales to approximately 60–70% of peak, extending export time
- The thermal spiral: throttling extends duration, extending heat accumulation

### Mitigation Recommendations

1. **Immediate**: Do not schedule Phase 5.1 activation exports during the daytime (ambient temperature is highest)
2. **Pre-activation**: Verify heatsink is properly seated (or fan installed). Prior sessions noted the Pi 5 lacks active cooling
3. **Export scheduling**: Schedule automated exports at 02:00–04:00 UTC when ambient is lowest
4. **Concurrency**: Do not run ZIM export concurrently with Meilisearch indexing, ActivityPub federation sync, or other CPU-intensive services
5. **Temperature monitoring**: `vcgencmd measure_temp` before and after the smoke test; abort if >85°C at the start

**Verdict**: The 80.7°C idle baseline is a yellow flag. For the smoke test (2 articles, sub-second duration), thermal risk is negligible. For any multi-minute export, active cooling is strongly recommended before scheduling.

---

## 6. Documentation Gaps for Phase 5, ZIM, and OPDS

### Backend README.md — Current State

`backend/README.md` last updated for "Phase 4 Complete" status. It contains no mention of:
- Phase 5.1 offline export capability
- ZimWriter service (`app/services/export/zim_writer.py`)
- libzim dependency or installation instructions
- `zim-tools` system package requirement (zimcheck)
- Migration 003 (zim_exports table)
- Kiwix — how to use generated ZIM files
- OPDS catalog (`app/services/export/opds_generator.py`) — undocumented in README
- `ExportConfig`, `ZimMetadata`, `ExportScope` — undocumented data models
- Environment variables for export output directory

The README project structure tree shows:
```
backend/
├── app/
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
```

The export service directory (`app/services/export/`) is not shown. The tree is stale by at least two phases.

### API.md — Current State

`API.md` documents Phase 1–4 endpoints. Missing:
- `POST /api/v1/export/zim` (Phase 5.2 scope, but schema should be documented)
- `GET /api/exports/health` (recommended monitoring endpoint)
- OPDS feed endpoints (if any are wired to routes)

### Phase 5 Architecture Docs — Inconsistencies

Multiple Phase 5 architecture documents exist (`PHASE_5_ARCHITECTURE.md`, `PHASE_5_CANDIDATES.md`, `phase-5-kiwix-architecture.md`, etc.). These have inconsistent claims:
- Some reference migration 003 as "planned" (outdated post-merge)
- Some reference `libzim>=3.2,<4.0` (should be `>=3.10.0`)
- Some describe the "stub phase" as current (no longer accurate on remote main)

### ZIM Naming Convention Documentation

No single document clearly explains the ZIM naming convention (`open-repo_en_nopic`) or its relationship to `ZimMetadata.name`. The convention is embedded in docstrings but not surfaced in user-facing docs.

### OPDS Catalog Gap

The OPDS generator (`opds_generator.py`) is fully implemented (20 tests pass). There is no documentation for:
- How to access the OPDS feed URL
- How to configure an OPDS client (e.g., KOReader, Calibre) to point at the node's feed
- The relationship between `ZimExport` records and OPDS entries

### Deployment Operations Gap

No runbook exists for:
- Applying migration 003 in production
- First-run ZIM export execution
- CDN upload step (mentioned in `ZimWriteResult.cdn_url` but not documented)
- Export rotation logic (`is_current`, `superseded_at` fields in migration 003)

### Summary: Documentation Gaps Table

| Gap | Location | Priority | Effort |
|-----|----------|----------|--------|
| Phase 5 offline export section in README | backend/README.md | HIGH | 1 hour |
| libzim + zimcheck install instructions | README | HIGH | 20 min |
| Project structure tree update (export service) | README | MEDIUM | 15 min |
| API.md: export endpoint skeleton | API.md | MEDIUM | 30 min |
| OPDS feed URL and client setup | README or new OPDS.md | MEDIUM | 45 min |
| Migration 003 deployment runbook | New DEPLOYMENT.md or README section | HIGH | 30 min |
| ZIM naming convention explanation | ZIM_GUIDE.md or README | LOW | 20 min |
| CDN upload step documentation | README or OPERATIONS.md | LOW | 30 min |

---

## 7. Integration Test Results Summary

### Current State on Local Master

**Full test suite**: 240 passed, 19 skipped, 35 warnings — 0 failures
**Export pipeline tests only** (`tests/integration/test_export_pipeline.py`): **88 passed** — 0 failures

The 19 skipped tests are pre-existing skips in `test_wave3_endorsement_propagation.py` and `test_wave4_phase4_conflict_logging.py`, unrelated to Phase 5.

### Test Class Breakdown (88 Export Tests)

| Class | Tests | Status |
|-------|-------|--------|
| TestZimMetadata | 9 | PASS |
| TestExportConfig | 7 | PASS |
| TestZimEntry | 9 | PASS |
| TestZimWriterInitialization | 3 | PASS |
| TestZimWriterAddArticle | 5 | PASS |
| TestZimWriterAddResource | 5 | PASS |
| TestZimWriterCreateZim | 7 | PASS |
| TestAttributionFooter | 3 | PASS |
| TestZimWriterStaticMethods | 8 | PASS |
| TestOPDSEntry | 10 | PASS |
| TestOPDSGenerator | 11 | PASS |
| TestEndToEndPipeline | 7 | PASS |
| TestLibZIMIntegration | 4 | PASS |
| **Total** | **88** | **ALL PASS** |

### Important Caveat: Tests Run Against Stub Path

All 88 tests execute against `create_zim()` which calls `_stub_write_placeholder()`. The `TestLibZIMIntegration` class (4 tests) tests:
1. Fallback PNG dimensions (48x48 confirmed via IHDR parse — PASS)
2. `_get_illustration_bytes()` always returns bytes — PASS
3. `_apply_metadata_to_creator()` calls `config_indexing(True, "eng")` via MagicMock — PASS
4. ZIM magic bytes check (stub text file — test accepts stub marker — PASS)

None of the 88 tests exercise the real `libzim.writer.Creator`. The 4 `TestLibZIMIntegration` tests are interface-contract tests, not integration tests against the real binary.

### Claim Reconciliation: "51/51 tests passing"

The task context states "libzim integration tests passing 51/51 as of merge time." This number does not match the local state (88 tests) or the remote main state (84 tests at merge). The most likely explanation: "51" refers to the test count at a specific earlier point in the feature branch development (possibly the 51-test state before the OPDS generator tests were added). The actual post-merge test counts are 84 (remote main) and 88 (local master, including 4 post-fix tests).

**The correct verified number is 88 passing on local master, 0 failures.**

---

## 8. Confidence Assessment and Known Gaps

### High Confidence Findings

- libzim 3.10.0 is installed and importable in the venv (verified)
- 88 tests pass on local master, 0 failures (executed)
- All 32 corpus articles pass schema validation (executed)
- PNG fallback is valid 48x48 (verified via IHDR parse)
- `config_indexing(True, "eng")` is called in `_apply_metadata_to_creator()` (verified via MagicMock test)
- Remote `open-repo/main` has real libzim Creator activation (verified via git show)

### Medium Confidence Findings

- Performance estimate for real Creator (1–3.5s for 32 articles) — not executed due to stub on local master
- Thermal impact under sustained compute — modeled from known Pi 5 throttle behavior

### Gap: Real libzim Creator Has Not Been Exercised on This Hardware

The real `create_zim()` path (via `open-repo/main` code) has not been executed on this Pi 5. The first real execution is the smoke test in Stage B.3 of the activation checklist. Until that test passes, the Phase 5.1 implementation is unvalidated against actual hardware.

The prior session report noted the config_indexing() ordering issue (must be called before context manager entry). The `open-repo/main` code has this correct (verified: `creator.config_indexing(True, ...)` is called before `with creator:`). The local master's `_apply_metadata_to_creator()` also calls it correctly, but that method is never reached in real execution because the stub bypasses it.

---

## Appendix: File Locations

| Purpose | Path |
|---------|------|
| ZimWriter implementation (local master, stub) | `projects/open-repo/backend/app/services/export/zim_writer.py` |
| ZimWriter implementation (remote main, real) | `open-repo/main:backend/app/services/export/zim_writer.py` |
| OPDS generator | `projects/open-repo/backend/app/services/export/opds_generator.py` |
| Export pipeline tests | `projects/open-repo/backend/tests/integration/test_export_pipeline.py` |
| Migration 003 (feature branch only) | `projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py` (absent from local master working tree) |
| Corpus data | `projects/open-repo/data/openfarm_procedures.jsonl` (32 articles) |
| pyproject.toml | `projects/open-repo/backend/pyproject.toml` |
| ZimExport ORM model | `projects/open-repo/backend/app/models.py` (ZimExport class present — added via commit 274eb1f2) |

---

*Verification executed: 2026-05-22, live code audit + test execution + schema validation*
*Sources: live `pytest` run, `git show` against remote branches, Python interpreter, corpus JSON parsing*
