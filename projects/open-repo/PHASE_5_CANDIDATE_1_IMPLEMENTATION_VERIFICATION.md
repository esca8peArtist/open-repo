---
title: "Phase 5 Candidate 1 — ZimWriter/libzim Implementation Verification"
project: open-repo
phase: 5
candidate: 1
document_type: audit
status: complete
date: 2026-05-19
auditor: General Research Agent (Session 1361)
confidence: high
---

# Phase 5 Candidate 1: Implementation Verification

**Bottom line up front**: Candidate 1 (ZimWriter/libzim) is production-ready to implement. The scaffold is complete, all 84 existing tests pass in 0.22 seconds, ARM64 wheels are confirmed available on PyPI for Python 3.11 (the system version on this Raspberry Pi 5), and zim-tools/zimcheck is installable from apt. The roadmap is accurate and actionable. The only blocking step before implementation is installing the libzim PyPI wheel. Total implementation effort: 8–11 hours as estimated.

---

## Section 1: libzim Python Bindings Audit

### 1.1 Current System State

| Item | Result |
|------|--------|
| `python3 -c "import libzim"` | **FAILS — not installed** (ModuleNotFoundError) |
| libzim PyPI package name | `libzim` (not `python-libzim`) |
| Latest version on PyPI | **3.10.0** (verified 2026-05-19) |
| All available versions | 0.0.1 through 3.10.0 (21 releases) |
| Roadmap pinned version | `>=3.2,<4.0` |
| 3.10.0 satisfies pin | Yes — no conflict |
| Python version on system | 3.11.2 |
| System architecture | `aarch64` (ARM64, Raspberry Pi 5) |
| System OS | Raspberry Pi OS (Debian-based, ARM64) |

The roadmap specifies pinning `libzim>=3.2,<4.0`. Version 3.10.0 is the latest stable release and satisfies this constraint. The roadmap mentions "March 2026 release" — 3.10.0 is the most recent release as of audit date and is the correct target.

### 1.2 ARM64 Wheel Availability (Raspberry Pi 5 Compatibility)

Verified by querying the PyPI JSON API for libzim 3.10.0. Pre-built binary wheels are available for all supported Python versions on Linux ARM64 (`manylinux_2_27_aarch64`):

| Python Version | Wheel Available | Filename Pattern |
|----------------|-----------------|-----------------|
| 3.10 | Yes | `libzim-3.10.0-cp310-cp310-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl` |
| **3.11** | **Yes** | **`libzim-3.10.0-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl`** |
| 3.12 | Yes | `libzim-3.10.0-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl` |
| 3.13 | Yes | `libzim-3.10.0-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl` |
| 3.14 | Yes | `libzim-3.10.0-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl` |

The cp311 manylinux2 ARM64 wheel matches Python 3.11.2 running on this Raspberry Pi 5 exactly. No source compilation is required. `uv pip install "libzim>=3.2,<4.0"` will resolve to 3.10.0 and install the pre-built binary wheel — no compiler, no `libzim-dev` system headers, no build-isolation flags needed.

**Risk 1 from roadmap ("wheel not available for ARM64") is not a risk at 3.10.0.** This concern applied to earlier versions but is fully resolved.

### 1.3 Xapian: Bundled or Separate

The libzim PyPI wheel is a self-contained manylinux binary. The manylinux packaging standard requires that all non-glibc dependencies be bundled inside the wheel — Xapian is bundled, not a system dependency.

| System Package | Available via apt | Required for libzim wheel | Notes |
|---------------|------------------|--------------------------|-------|
| `libxapian-dev` | Yes (v1.4.22-1, arm64) | **No** | Dev headers only; not needed |
| `libxapian30` | Yes | **No** | Runtime library; bundled in wheel |
| Python `xapian` binding (`import xapian`) | Not installed | **No** | libzim exposes Xapian via `Creator.config_indexing()` |
| `libzim-dev` (apt, v8.1.1-0.2) | Yes | **No** | C++ headers only; PyPI wheel path requires none of these |

**Summary**: Install `libzim` from PyPI only. No apt packages are needed before wheel installation. After installation, Xapian full-text indexing is enabled by calling `creator.config_indexing(True, "eng")` inside the Creator context — no separate configuration required.

### 1.4 Installation Method Decision

The correct command for this project (UV-managed, per CLAUDE.md):

```bash
uv pip install "libzim>=3.2,<4.0"
```

Verify installation:

```bash
uv run python3 -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('libzim OK')"
```

Note: `libzim-dev` (apt package, version 8.1.1-0.2) is present in the apt cache. It is NOT needed and should NOT be installed — it provides C++ headers for compiling against libzim from source, which is irrelevant when using the PyPI binary wheel.

---

## Section 2: Validation of 84 Existing ZIM Stubs

### 2.1 What "84 Stubs" Actually Means

There are no literal `.json` or `.zim` stub files in the project repository. The 84 stubs referenced throughout the Phase 5 roadmap are **84 passing Python test cases** in `backend/tests/integration/test_export_pipeline.py` (1,427 lines). Each test exercises the ZimWriter scaffold, which currently writes placeholder text files instead of real ZIM binaries. The "stub" refers to the implementation stub in `create_zim()`, not to file stubs.

Verified by running the full test suite on 2026-05-19:

```
$ cd backend && python3 -m pytest tests/integration/test_export_pipeline.py -q
84 tests collected in 0.07s
84 passed in 0.22s
```

All 84 tests pass. No failures, no skips.

### 2.2 Sample of 10 Test Cases: Schema Consistency Audit

Ten tests were selected across all test classes to validate coverage of required ZIM fields:

| Test Name | Schema Valid | Required Fields Present | Notes |
|-----------|-------------|------------------------|-------|
| `test_valid_metadata_initializes` | Yes | title, language, name | Confirms initialization without error |
| `test_date_auto_generated_when_none` | Yes | date (YYYY-MM-DD) | Auto-fill confirmed; format regex checked |
| `test_validate_returns_empty_list_for_valid_metadata` | Yes | All 7 mandatory fields | Full validation pass on good metadata |
| `test_validate_reports_description_over_80_chars` | Yes | description length constraint | 80-char hard limit enforced at Python level |
| `test_writer_raises_for_invalid_metadata` | Yes | All fields | ValueError on bad metadata before ZIM creation |
| `test_add_article_increments_count` | Yes | path, content | Article buffering and count tracking |
| `test_create_zim_returns_result_with_sha256` | Yes | sha256 (64-char hex) | Checksum format and length validated |
| `test_create_zim_returns_correct_article_count` | Yes | article_count | Article count fidelity over 7 articles |
| `test_full_pipeline_with_synthetic_data` | Yes | All fields end-to-end | Full pipeline: 5 local items → ZIM → OPDS catalog |
| `test_unicode_content_handled_correctly` | Yes | content encoding (UTF-8) | French, Japanese, Arabic, Spanish characters |

### 2.3 Required ZIM Field Coverage

Comparing the openZIM mandatory fields against current test and data model coverage:

| ZIM Mandatory Field | In ZimMetadata | Validated | Tested | Notes |
|--------------------|---------------|-----------|--------|-------|
| `Title` | Yes | Warn if >30 chars | Yes | Warning logged; not a hard error (zimcheck-aligned) |
| `Description` | Yes | Hard error if >80 chars | Yes | Enforced at Python layer before libzim |
| `Language` | Yes | Present check only | Yes | ISO 639-3 format; no RFC 5646 validation |
| `Creator` | Yes | Non-empty check | Yes | Validated as non-empty string |
| `Publisher` | Yes | Non-empty check | Yes | Validated as non-empty string |
| `Date` | Yes | YYYY-MM-DD regex | Yes | Auto-generated if None |
| `Name` | Yes | Full naming regex | Yes | Pattern: `{publisher}_{lang}_{flavour}` |
| `Illustration_48x48` | Yes | File existence if path given | Yes | Fallback constant defined in roadmap |
| `Flavour` | Yes | Enum validation | Yes | 10 valid values hardcoded |
| `Tags` | Yes | Default only | Indirectly | Default: `"offline;practical-knowledge;procedures"` |

### 2.4 Schema Drift Assessment

**Finding**: No schema drift detected. The `ZimMetadata`, `ZimEntry`, and `ExportConfig` dataclasses are internally consistent and aligned with the openZIM specification as documented in the architecture files.

**Gap identified**: The `_apply_metadata_to_creator()` method body is currently `pass`. Until Change 4 is implemented, there is no test that verifies all 11 `add_metadata()` calls are made correctly with the right values against a real Creator. A mock-Creator unit test asserting each `add_metadata()` call should be added alongside Change 4.

**Second gap**: Language validation only checks that the language field is non-empty. A malformed language code (e.g., `"e"` or `"english"`) would pass Python validation but cause zimcheck to fail at the ISO 639-3 format check. This is a low-risk gap (the fixtures use `"eng"`) but should be noted.

---

## Section 3: Missing Pre-Requisites from Roadmap

### 3.1 Roadmap Accuracy Assessment

The `PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md` is accurate. The code snippets, API calls, and file locations all match the actual codebase. Specific findings:

- Line numbers cited in the roadmap (e.g., "around line 762") are approximate — the actual stub call is at line 762 (`self._stub_write_placeholder()`). The "around" qualifier is appropriate.
- The `_apply_metadata_to_creator()` method is at line 870, matching the roadmap's "around line 870" reference.
- The class hierarchy and method signatures are unchanged from the roadmap's description.

### 3.2 System Package Status

| Package | Required | Status | Action |
|---------|----------|--------|--------|
| `libzim` (PyPI wheel) | **Yes — blocking** | Not installed | `uv pip install "libzim>=3.2,<4.0"` |
| `zim-tools` (apt, provides zimcheck) | Yes — for validation | Not installed (v3.1.3 available in apt) | `sudo apt install zim-tools` |
| `libzim-dev` (apt) | No | Available but not needed | Do not install; irrelevant |
| `libxapian-dev` (apt) | No | Available (v1.4.22) | Do not install; bundled in wheel |
| `jinja2` | Yes — for HTML templates | Transitively available via FastAPI | Add explicitly to pyproject.toml |

### 3.3 Python Dependency Version Matrix

| Package | Current in pyproject.toml | Phase 5 Requirement | Action |
|---------|--------------------------|--------------------|-|
| `libzim` | **Not listed** | `>=3.2,<4.0` | **Add** |
| `jinja2` | **Not listed** | `>=3.1` | **Add** (currently only a transitive dependency) |
| `fastapi` | `>=0.104.0` | No change | None |
| `sqlalchemy` | `>=2.0.0` | No change (ZimExport model added) | None |
| `alembic` | `>=1.13.0` | Migration needed for zim_exports table | Add migration file |
| `pytest` | `>=7.4.0` (dev) | No change | None |

The roadmap specifies `"libzim>=3.2,<4.0"` for pyproject.toml. Adding `"jinja2>=3.1"` alongside it ensures the HTML template rendering is explicit rather than relying on FastAPI's transitive pull.

### 3.4 Raspberry Pi 5 Deployment Considerations

The Raspberry Pi 5 is confirmed as the production deployment target (per project memory: idle at 81-84°C, under compute at 87.8°C, thermal throttling is a known constraint).

| Concern | Status | Recommendation |
|---------|--------|----------------|
| ARM64 wheel available | **Clear** | No action needed |
| ZIM generation CPU load | **Monitor** | ZIM creation is CPU-intensive. Benchmark with 100-article export; if generation time approaches 60 seconds, schedule exports at 02:00 UTC (roadmap default) when ambient temperature is lowest |
| Temp directory space | **Clear** | 201 GB free. ZIM files up to 500 MB have ample space. |
| Memory for article buffering | **Clear** | 6.9 GB available. 500-1,000 items at 50 KB avg HTML = 25-50 MB buffered — well within limits |
| Docker on Raspberry Pi | **Not applicable** | Deployment is bare-metal; apt-installed zimcheck is correct path |
| zimcheck timeout | **Calibrate** | Default 300-second timeout in `_run_zimcheck()` is generous. For nopic export at 500 items, expect 5-30 seconds. |

### 3.5 Configuration Requirements Before Go-Live

| Configuration | Current State | Action Required | Priority |
|--------------|--------------|----------------|----------|
| libzim PyPI installed | Missing | Install | P0 |
| zimcheck binary on PATH | Missing | `sudo apt install zim-tools` | P0 |
| 48x48 branded PNG | Using fallback constant | Create real icon (48x48 px exactly) | P1 before production |
| Cloudflare R2 credentials | Not configured | Required for CDN upload step only | P1 (post-ZIM-generation) |
| APScheduler weekly job | Not implemented | Required for automated exports | P2 (manual trigger works first) |
| Temp file cleanup | No cleanup job | Add `/tmp/*.zim.partial` cleanup on crash recovery | P2 |
| Export API endpoint | Not implemented | `app/api/v1/export.py` — needed for manual trigger | P1 |

---

## Section 4: Implementation Checklist with Hour-by-Hour Timeline

### 4.1 The 5 Code Changes: Detailed Assessment

All 5 changes land in `app/services/export/zim_writer.py`. One additional change is in `pyproject.toml`.

#### Change 0: Install dependency and update pyproject.toml (30 min)

**File**: `pyproject.toml`
**What**: Add `"libzim>=3.2,<4.0"` and `"jinja2>=3.1"` under `[project.dependencies]`
**Dependencies**: None — first step
**Testing**: `uv run python3 -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('OK')"`
**Blocker for**: Everything. Nothing else can proceed without libzim installed.

#### Change 1: Add libzim import guard (15 min)

**File**: `zim_writer.py`, after line 49 (`from typing import Optional`)
**What**: Add `try: from libzim.writer import Creator, Item, StringProvider, Hint; _LIBZIM_AVAILABLE = True` guard
**Dependencies**: Change 0 (libzim installed)
**Testing**: All 84 existing tests must still pass — module must load without error even if import fails
**Note**: The guard allows gradual rollout. In CI environments without libzim, the stub path runs. Remove guard after CI is confirmed to install libzim.

#### Change 2: Add ArticleItem adapter class (45 min)

**File**: `zim_writer.py`, new class after `ZimEntry` dataclass (before line 409)
**What**: Add `class ArticleItem(Item)` with `get_path()`, `get_title()`, `get_mimetype()`, `get_hints()`, `get_contentprovider()` methods
**Dependencies**: Change 1 (import guard; `Item`, `StringProvider`, `Hint` must be importable)
**Testing**: New unit test: construct `ArticleItem(entry)` and assert all 5 methods return correct values. Can run against a mock Creator without real ZIM file creation.
**Critical path position**: YES. This adapter is called for every article in the Creator loop. A bug here corrupts all content.

#### Change 3: Replace stub in create_zim() (1 hour)

**File**: `zim_writer.py`, around line 762 — replace `self._stub_write_placeholder()` call
**What**: Replace stub with `with Creator(str(self.output_path)) as creator: creator.config_indexing(True, self.config.language_iso3); creator.set_mainpath("index"); self._apply_metadata_to_creator(creator); for entry in self._entries: creator.add_item(ArticleItem(entry))`
**Dependencies**: Change 1 (import guard), Change 2 (ArticleItem exists)
**Testing**: `test_zim_writer_creates_real_zim_file` — open output with `open(path, 'rb').read(4)` and assert bytes equal ZIM magic header `b'\x5a\x49\x4d\x04'`
**Critical path position**: YES. This is the integration point where libzim's Creator is invoked.

#### Change 4: Implement _apply_metadata_to_creator() (45 min)

**File**: `zim_writer.py`, method at line 870 — replace `pass` with full implementation
**What**: Add all 11 `creator.add_metadata()` calls plus `creator.add_illustration(48, illustration_bytes)`. Also add `_FALLBACK_ILLUSTRATION_PNG` constant at module level.
**Dependencies**: Change 1 (import guard), Change 3 (Creator context established before this method is called)
**Testing**: `test_zim_metadata_all_mandatory_fields` — use `libzim.reader.Archive` to open the output ZIM and call `archive.get_metadata("Title")`, etc., asserting correct values for all 11 fields
**Note**: Add `_FALLBACK_ILLUSTRATION_PNG` constant. Verify the bytes in the roadmap represent a valid 48x48 PNG — the constant comment says "1x1 transparent PNG" but the size declaration says 48. Validate with `from PIL import Image; img = Image.open(io.BytesIO(_FALLBACK_ILLUSTRATION_PNG)); assert img.size == (48, 48)` before merging.

#### Change 5: Verify zimcheck integration (30 min)

**File**: No code changes needed
**What**: Install zimcheck (`sudo apt install zim-tools`), run `zimcheck` against a 10-article test ZIM, confirm exit code 0
**Dependencies**: Changes 3 and 4 complete (ZIM must be valid binary for zimcheck to pass)
**Testing**: `test_zimcheck_passes_on_valid_export` — generate 10-article ZIM and assert `result.zimcheck_passed == True`
**Note**: The existing `_run_zimcheck()` method is already correct. No code changes required. This step is verification only.

### 4.2 Hour-by-Hour Timeline

| Hour | Task | Files Affected | Completion Gate |
|------|------|---------------|----------------|
| 0:00–0:30 | Install libzim; add to pyproject.toml; verify import works | `pyproject.toml` | `from libzim.writer import Creator` succeeds |
| 0:30–0:45 | Add import guard (Change 1) | `zim_writer.py` | All 84 existing tests still pass |
| 0:45–1:30 | Add ArticleItem class (Change 2) | `zim_writer.py` | New ArticleItem unit tests pass |
| 1:30–2:30 | Replace stub in create_zim() (Change 3) | `zim_writer.py` | ZIM magic header test passes |
| 2:30–3:15 | Implement _apply_metadata_to_creator() (Change 4) | `zim_writer.py` | Metadata readback test passes |
| 3:15–4:00 | apt install zim-tools; run zimcheck on test ZIM (Change 5) | None | zimcheck exit code 0 |
| 4:00–5:30 | Write 12 new integration tests (3 files) | `tests/unit/`, `tests/integration/` | All 12 new tests pass |
| 5:30–6:30 | Manual E2E: generate real ZIM from test data, open in Kiwix | None | Articles display, search returns results |
| 6:30–7:00 | Remove _stub_write_placeholder(); re-run full test suite | `zim_writer.py` | All 84 + 12 tests pass, 0 failures |
| 7:00–8:00 | Write Alembic migration for zim_exports table | `alembic/versions/` | `alembic upgrade head` succeeds |
| 8:00–9:00 | Add ZimExport SQLAlchemy model to app/models.py | `app/models.py` | Model reflects zim_exports schema |
| 9:00–10:00 | Write export API endpoint skeleton | `app/api/v1/export.py` | `POST /api/exports` returns 200 + job_id |
| 10:00–11:00 | Buffer: risk mitigation, cleanup, PR prep | Various | PR ready for review |

**Total**: 8–11 hours (confirms roadmap estimate)

### 4.3 Critical Path

```
Change 0 (install libzim; pyproject.toml)
  └── Change 1 (import guard)
        └── Change 2 (ArticleItem class)  ← PRIMARY BLOCKER
              └── Change 3 (create_zim() integration)  ← PRIMARY BLOCKER
                    ├── Change 4 (metadata application)
                    └── Change 5 (zimcheck verification)
```

Changes 0→1→2→3 are strictly sequential. Nothing can be parallelized before Change 3 completes. Changes 4 and 5 can proceed in any order after Change 3.

### 4.4 Parallel Opportunities

Once Change 3 is complete (hour 2:30), three tasks can run in parallel:

- **Thread A**: Implement Change 4 (`_apply_metadata_to_creator()`) + write metadata readback test
- **Thread B**: Install `zim-tools` + run zimcheck verification (Change 5)
- **Thread C**: Write the 12 new integration test stubs (test authorship does not depend on implementation)

This parallelism, if executed with two sessions (per the 3.5x throughput memory), can compress hours 2:30–5:30 to approximately 1.5 hours, bringing total time to 7–9 hours.

---

## Section 5: Test Environment Setup Checklist

### 5.1 Pre-Implementation Setup

| Setup Step | Duration | Deliverable |
|-----------|----------|-------------|
| `uv pip install "libzim>=3.2,<4.0"` | 2 minutes | libzim 3.10.0 installed, cp311 ARM64 wheel |
| `sudo apt install zim-tools` | 3 minutes | `zimcheck` binary at `/usr/bin/zimcheck` |
| `uv run pytest tests/integration/test_export_pipeline.py -q` | 30 seconds | Baseline: 84 tests pass before changes |
| `git checkout -b feature/zimwriter-libzim-integration` | 1 minute | Isolated branch for PR |
| Create `tests/unit/test_zim_writer_libzim.py` (stub file) | 15 minutes | 8 test stubs ready for implementation |
| Create `tests/integration/test_zimcheck_validation.py` (stub file) | 10 minutes | 2 test stubs ready |
| Create `tests/integration/test_zim_readback.py` (stub file) | 10 minutes | 2 test stubs ready |

### 5.2 Isolated Testing Approach

The existing 84 tests use `pytest`'s `tmp_path` fixture for complete isolation. ZimWriter writes to ephemeral temp directories that are cleaned up after each test. The ZimWriter does not interact with the database during writing — content items are passed in via `add_article()` calls with synthetic data. This pattern continues for all new tests.

| Test Layer | Isolation Method | Notes |
|-----------|-----------------|-------|
| Unit tests (no libzim) | `tmp_path` fixture + stub placeholder | All 84 existing tests — unchanged |
| Unit tests (with libzim) | `tmp_path` fixture + real Creator | New tests in `test_zim_writer_libzim.py`; temp .zim deleted after test |
| Integration tests (zimcheck) | `tmp_path` fixture + zimcheck subprocess | Requires `zimcheck` on PATH |
| Integration tests (reader) | `tmp_path` fixture + `libzim.reader.Archive` | Reads same temp .zim that was just written |
| Manual E2E | Developer-chosen output path | Transfer to phone/laptop for Kiwix open |

No shared test database, no network calls, no external fixtures required. All test data is synthetic (as established in the existing `sample_content_items` fixture).

### 5.3 Performance Benchmarking Baseline

| Benchmark | Target | Measurement Method |
|-----------|--------|-------------------|
| Generation time, 10 articles | < 2 seconds | `ZimWriteResult.generation_duration_seconds` |
| Generation time, 100 articles | < 10 seconds | Same; logged in export job |
| Generation time, 500 articles (nopic) | < 60 seconds | Roadmap success criterion |
| ZIM file size, 100 articles (nopic) | 1–5 MB compressed | `ZimWriteResult.file_size_bytes` |
| Xapian index overhead | ~10–20% of content size | Archive size minus estimated content-only size |
| Compression ratio (zstd default) | 2.5–3x | Uncompressed HTML total / ZIM file size |

Benchmarks should be captured on first run at 02:00 UTC (cool system) and again after 30-minute sustained load to characterize thermal throttling impact on Raspberry Pi 5.

### 5.4 Quality Verification: Kiwix Compatibility

| Verification Step | Tool | Pass Criterion |
|------------------|------|---------------|
| ZIM binary validity | `zimcheck {file}.zim` | Exit code 0; no ERROR lines in stdout |
| Magic header check | `python3 -c "open('{file}','rb').read(4)"` | Equals `b'\x5a\x49\x4d\x04'` |
| SHA-256 sidecar | `sha256sum -c {file}.sha256` | Exit code 0 |
| libzim reader roundtrip | `libzim.reader.Archive.get_entry_by_path()` | Returns exact UTF-8 content written |
| Kiwix Android (F-Droid) | Manual sideload | Articles display; search returns results for 3+ keywords |
| kiwix-serve (Docker) | `docker run -v $(pwd):/data kiwix/kiwix-serve kiwix-serve /data/{file}.zim` | HTTP GET localhost:8080 returns article HTML |

### 5.5 New Test Infrastructure Required

These files do not yet exist. They must be created as part of Phase 5 implementation:

| File | Test IDs from Roadmap | Dependencies |
|------|-----------------------|-------------|
| `tests/unit/test_zim_writer_libzim.py` | Tests 1–5, 10–12 (unit, no subprocess, uses libzim reader) | libzim installed |
| `tests/integration/test_zimcheck_validation.py` | Tests 6–7 (zimcheck subprocess) | libzim + zim-tools |
| `tests/integration/test_zim_readback.py` | Tests 8–9 (libzim.reader.Archive roundtrip) | libzim |

The existing `test_export_pipeline.py` (84 tests) continues unchanged. New tests are additive only.

---

## Go / No-Go Assessment

| Dimension | Status | Evidence |
|-----------|--------|----------|
| Scaffold completeness | **GO** | 84 tests pass; ZimWriter class complete except TODO stubs |
| libzim ARM64 wheel | **GO** | cp311 manylinux aarch64 wheel confirmed in 3.10.0 |
| zimcheck availability | **GO** | zim-tools 3.1.3 in apt cache; `sudo apt install zim-tools` |
| Xapian bundled in wheel | **GO** | manylinux wheel is self-contained; no system Xapian needed |
| Disk space | **GO** | 201 GB free |
| Memory for export | **GO** | 6.9 GB available; 500-item export peaks at ~50 MB |
| Jinja2 explicit dependency | **CAUTION** | Add to pyproject.toml alongside libzim |
| Illustration constant | **CAUTION** | Verify _FALLBACK_ILLUSTRATION_PNG bytes are valid 48x48 before commit |
| Thermal throttling | **MONITOR** | Schedule exports at 02:00 UTC; benchmark under load |
| Phase 4 PR blocker | **CONDITIONAL** | Feature branch work can start; must not merge to main before Phase 4 PR #1 |

**Recommendation**: Proceed with Candidate 1 implementation immediately. Use `PHASE_5_CANDIDATE_1_IMPLEMENTATION_CHECKLIST.md` as the execution guide. Begin with `git checkout -b feature/zimwriter-libzim-integration` and `uv pip install "libzim>=3.2,<4.0"`.
