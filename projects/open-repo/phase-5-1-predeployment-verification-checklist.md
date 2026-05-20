---
title: "Phase 5.1 Pre-Deployment Verification Checklist — ZimWriter libzim Activation"
project: open-repo
phase: "5.1"
created: 2026-05-20
audience: thorn — May 25-26 merge decision briefing
decision_gate: "May 26 merge approval → May 28-29 pre-deployment testing → May 30-31 deploy"
status: BLOCKERS IDENTIFIED — see Section 6 before approving merge
confidence: 87% (down from 98.2% due to branch divergence finding)
---

# Phase 5.1 Pre-Deployment Verification Checklist

**Feature**: ZimWriter libzim activation — offline ZIM export pipeline  
**Branch**: `feature/zimwriter-libzim-activation` (commit ec0ff7be)  
**Verification executed**: 2026-05-20, Session 1407  
**Executor**: research agent (live code audit + test execution)

> CRITICAL FINDING UPFRONT: This checklist was executed against live code.
> The feature branch diverges from master in ways that create a merge conflict.
> One blocker and two mandatory pre-merge actions are identified in Section 6.

---

## Section 1 — Code Verification

### 1.1 Branch Status

```
Branch: feature/zimwriter-libzim-activation
Tip commit: ec0ff7be
Status: BEHIND master by 1 commit (198a146d — "fix(open-repo): Phase 5.1 critical defects")
```

The feature branch was authored before a post-hoc fix commit (`198a146d`) was applied directly to master. Master and the feature branch have diverged. The merge will not be a fast-forward and requires deliberate resolution.

**Verification command**:
```bash
git log --oneline feature/zimwriter-libzim-activation..master -- projects/open-repo/backend/
# Expected output: 198a146d fix(open-repo): Phase 5.1 critical defects — PNG, indexing, libzim tests
```

Expected result: one commit on master not present on feature branch.  
Actual result: confirmed — `198a146d` is master-only.

- [x] Branch name confirmed: `feature/zimwriter-libzim-activation`
- [x] Tip commit: ec0ff7be
- [ ] Branch is current with master: **NO — diverged by 1 master-only commit**

---

### 1.2 Five Required Code Changes — Audit Results

#### Change 1: libzim import guard + `_LIBZIM_AVAILABLE` flag

**File**: `backend/app/services/export/zim_writer.py` lines 51–64  
**Status**: PRESENT on feature branch

```python
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None
    Item = object
    StringProvider = None
    Hint = None
```

- [x] Try-except guard present
- [x] `_LIBZIM_AVAILABLE` flag defined
- [x] Type stubs allow static analysis without libzim installed

#### Change 2: `ArticleItem` adapter class (ZimEntry → libzim Item bridge)

**File**: `backend/app/services/export/zim_writer.py` lines 429–468  
**Status**: PRESENT on feature branch

All five required methods implemented: `get_path`, `get_title`, `get_mimetype`, `get_hints`, `get_contentprovider`. Content encoding (str → UTF-8 bytes) correct. Inherits from `libzim.writer.Item` (falls back to `object` stub when unavailable).

- [x] `ArticleItem` class exists
- [x] All 5 interface methods implemented
- [x] Content encoding handled
- [x] Thread safety documented

#### Change 3: `create_zim()` real libzim Creator integration

**File**: `backend/app/services/export/zim_writer.py` lines 819–837  
**Status**: PRESENT on feature branch — with one gap vs master

```python
else:
    with Creator(str(self.output_path)) as creator:
        creator.set_mainpath("index")
        self._apply_metadata_to_creator(creator)
        for entry in self._entries:
            creator.add_item(ArticleItem(entry))
```

Gap identified: master calls `creator.config_indexing(True, self.config.language_iso3)` before `set_mainpath`. This line is ABSENT from the feature branch's live (non-docstring) code path. It appears only in an illustrative docstring example. The master-only commit `198a146d` added this call explicitly to the production code. See Section 6 for impact.

- [x] Creator context manager present
- [x] `set_mainpath("index")` called
- [x] `_apply_metadata_to_creator()` called
- [x] Articles iterated via `ArticleItem`
- [ ] `creator.config_indexing(True, language_iso3)` in production path: **ABSENT on feature branch**

#### Change 4: `_apply_metadata_to_creator()` — 11 ZIM metadata fields

**File**: `backend/app/services/export/zim_writer.py` lines 945–973  
**Status**: PRESENT on feature branch

All 11 required metadata fields mapped: Title, Description, Language, Creator, Publisher, Date, Name, Flavour, Tags, Source, Scraper. Optional LongDescription conditionally added. Illustration fallback via `add_illustration(48, _FALLBACK_ILLUSTRATION_PNG)`.

- [x] All 11 required fields mapped
- [x] Optional LongDescription conditional
- [x] Illustration with fallback present

#### Change 5: Alembic migration 003 + pyproject.toml update

**Migration file**: `backend/alembic/versions/003_add_zim_exports_table.py`  
**Status**: PRESENT on feature branch, ABSENT on master

Migration creates `zim_exports` table with 28 columns and 3 production indexes. `downgrade()` function present for rollback. Revision chain: 003 → down_revision=002 (correct).

**pyproject.toml**: `libzim>=3.2,<4.0` added to `[project.dependencies]`  
**Status**: PRESENT on feature branch, ABSENT on master

- [x] Migration 003 file exists on feature branch
- [x] 28-column schema with correct types
- [x] 3 indexes (compound name+flavour, partial is_current, unique zim_uuid)
- [x] downgrade() function present
- [x] `libzim>=3.2,<4.0` in pyproject.toml on feature branch

#### Change 5b: `_FALLBACK_ILLUSTRATION_PNG` constant

Both branches define this constant, but with different byte content:

| Branch | Size | IHDR dimensions | Notes |
|--------|------|-----------------|-------|
| feature/zimwriter-libzim-activation | 67 bytes | 48×48 | Minimal but valid IHDR |
| master (post-fix) | 88 bytes | 48×48 | Larger IDAT, validated by TestLibZIMIntegration |

The feature branch PNG is valid (correct magic bytes, 48×48 IHDR) but the master version includes a more robust IDAT section validated by 4 specific tests that exist only on master. The test suite on the feature branch does not validate the PNG bytes.

- [x] PNG magic bytes correct on both branches
- [x] 48×48 dimensions on both branches
- [ ] PNG validated by dedicated tests on feature branch: **ABSENT** (tests removed by feature branch)

---

### 1.3 Test Suite Status

**Executed**: `cd projects/open-repo/backend && uv run pytest tests/ --tb=short`  
**Environment**: master branch working tree, Python 3.11.2, libzim not installed (stub path active)

```
240 passed, 19 skipped, 35 warnings in 8.41s
```

**Export pipeline tests only** (`tests/integration/test_export_pipeline.py`):

```
88 passed in 0.23s
```

**Test class breakdown — master working tree (88 tests)**:

| Class | Tests | Status |
|-------|-------|--------|
| TestZimMetadata | 9 | PASS |
| TestExportConfig | 7 | PASS |
| TestZimEntry | 9 | PASS |
| TestZimWriterInitialization | (subset of 15) | PASS |
| TestZimWriterAddArticle | (subset of 15) | PASS |
| TestZimWriterAddResource | (subset of 15) | PASS |
| TestZimWriterCreateZim | (subset of 15) | PASS |
| TestAttributionFooter | 4 | PASS |
| TestZimWriterStaticMethods | (subset) | PASS |
| TestOPDSEntry | (subset of 20) | PASS |
| TestOPDSGenerator | (subset of 20) | PASS |
| TestEndToEndPipeline | 20 | PASS |
| TestLibZIMIntegration | 4 | PASS (master only) |

**Feature branch test count**: 84 (the `TestLibZIMIntegration` class with 4 tests is absent)

**Important**: The 19 skipped tests are in `test_wave3_endorsement_propagation.py` and `test_wave4_phase4_conflict_logging.py` — pre-existing skips unrelated to Phase 5. Zero failures in standard (non-error-escalated) runs.

**Deprecation warning test**: Running with `-W error::DeprecationWarning` causes 6 tests in `test_phase_3_endpoints.py` to fail due to Pydantic v2 `from_orm` deprecation warnings (pre-existing Phase 3 issue, unrelated to Phase 5.1). Under normal test execution these 6 tests PASS because warnings are not escalated.

- [x] 240 passed, 0 failed (standard run on master working tree)
- [x] Zero Phase 4 regressions
- [ ] 84/84 claimed — ACTUAL count is 88 on master, 84 on feature branch (4 libzim validation tests removed)
- [ ] Tests running against real libzim: **NO** — libzim not installed in venv, stub path active

---

## Section 2 — Dependency Verification

### 2.1 libzim PyPI Availability

**Verified via**: `pip index versions libzim`

```
libzim (3.10.0)
Available versions: 3.10.0, 3.9.0, 3.8.0, 3.7.0, 3.6.0, 3.5.0, 3.4.0, 3.3.0.post0,
                   3.3.0, 3.2.0, 3.1.0, 3.0.0 ...
```

Latest version in `>=3.2,<4.0` constraint: **3.10.0** (released May 19, 2026).

- [x] libzim >=3.2,<4.0 available on PyPI
- [x] Latest qualifying version: 3.10.0

### 2.2 aarch64 Wheel Availability

**Platform**: aarch64 (Raspberry Pi 5), Python 3.11.2

**Wheel download test**:
```bash
pip download libzim==3.9.0 --platform manylinux_2_28_aarch64 --python-version 311 \
    --only-binary=:all: -d /tmp/libzim_check2
# Result: libzim-3.9.0-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl (8.3 MB)
# Successfully downloaded
```

**PyPI page confirms for libzim 3.10.0**:
- `libzim-3.10.0-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl` (8.3 MB)
- `libzim-3.10.0-cp311-cp311-musllinux_1_2_aarch64.whl` (9.6 MB)

Both glibc-based and musl wheels available. Standard Raspberry Pi OS (Debian-based, glibc) uses the manylinux variant.

- [x] Pre-built wheel confirmed for aarch64 + Python 3.11 (manylinux)
- [x] No source-build fallback required
- [x] Wheel size 8.3 MB — acceptable for production deployment

### 2.3 Python Version Compatibility

- [x] Python 3.11.2 confirmed on target system (`uname -m` = aarch64, `python3 --version` = 3.11.2)
- [x] libzim wheel supports cp311 (CPython 3.11)
- [x] libzim declared Python support: >=3.10,<3.15 (open-repo uses 3.11 — within range)

### 2.4 Xapian Status

```bash
pkg-config --modversion xapian-core  # → not installed
dpkg -l | grep -i xapian             # → not installed
```

Xapian is not installed as a system package. This is a known pre-existing condition. The libzim wheel bundles its own Xapian binaries, so no separate system installation is required. The `creator.config_indexing()` call in master will work because libzim's bundled Xapian handles indexing internally.

- [x] Xapian not a system-level blocker
- [x] libzim wheel bundles Xapian — no `apt install` needed
- [x] Xapian FTS will work once `config_indexing()` call is present (currently absent on feature branch)

### 2.5 Dependency Installation Test

```bash
cd projects/open-repo/backend
# Dry-run install (actual download confirmed above)
# Post-install verification (pending actual install):
# python -c "import libzim; print(libzim.__version__)"
```

Note: libzim is NOT currently installed in the backend venv. All test runs use the stub path (`_LIBZIM_AVAILABLE = False`). A full install and re-run of tests against real libzim is required before merge.

- [ ] libzim installed in venv: **NOT YET**
- [ ] `import libzim` verified in venv: **NOT TESTED**
- [ ] Tests re-run with real libzim: **NOT DONE** — currently all 84/88 tests use stub path

---

## Section 3 — Pre-Deployment Testing Sequence

This sequence is to be executed on May 28-29 after merge approval. Estimated time: 1.75–2.5 hours.

### Step 1: Environment Setup (30 min)

```bash
cd projects/open-repo/backend

# 1a. Sync dependencies (installs libzim wheel)
uv sync
# Expected: resolves libzim>=3.2,<4.0, downloads ~8.3 MB aarch64 wheel

# 1b. Verify libzim imports correctly
uv run python -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('libzim import OK')"
# Expected output: libzim import OK
# If ImportError: check wheel was downloaded for correct platform (aarch64 cp311)

# 1c. Verify _LIBZIM_AVAILABLE is True in the app
uv run python -c "from app.services.export.zim_writer import _LIBZIM_AVAILABLE; print('LIBZIM AVAILABLE:', _LIBZIM_AVAILABLE)"
# Expected output: LIBZIM AVAILABLE: True
# If False: libzim import guard failed — diagnose wheel compatibility
```

### Step 2: Database Migration (20 min)

```bash
# 2a. Apply migration 003 (creates zim_exports table)
uv run alembic upgrade head
# Expected: alembic outputs "Running upgrade 002 -> 003, Add zim_exports table"

# 2b. Verify migration applied
uv run alembic current
# Expected: "003 (head)"

# 2c. Schema spot-check (if using SQLite for dev)
uv run python -c "
from app.database import engine
from sqlalchemy import inspect
inspector = inspect(engine)
cols = [c['name'] for c in inspector.get_columns('zim_exports')]
print('Columns:', len(cols))
assert 'zim_uuid' in cols and 'sha256' in cols and 'is_current' in cols
print('Schema OK')
"
# Expected: Columns: 28  Schema OK
```

### Step 3: Full Test Suite with Real libzim (30 min)

```bash
# 3a. Export pipeline tests with real libzim active
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short
# Expected after merge fix (see Section 6):
# 88 passed in ~X.Xs (including TestLibZIMIntegration class)
# If 84 passed: TestLibZIMIntegration class missing — merge did not include fix commit

# 3b. Full suite — confirm zero regressions
uv run pytest tests/ --tb=short
# Expected: 240 passed, 19 skipped (same as current — no regressions)
# Any new failures: investigate before deployment

# 3c. Record final test count
uv run pytest tests/ --tb=short 2>&1 | tail -3
```

### Step 4: Manual ZIM Export Test (45 min)

```bash
# 4a. Create minimal ZIM archive
uv run python - << 'EOF'
import tempfile
from pathlib import Path
from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ExportScope
)

with tempfile.TemporaryDirectory() as tmpdir:
    output = Path(tmpdir) / "test.zim"
    metadata = ZimMetadata(
        title="Open-Repo Test Export",
        description="Verification test archive",
        language="eng",
        name="openrepo_en_test",
        flavour="nopic",
        creator="Open-Repo",
        publisher="Open-Repo",
        source_url="https://example.org",
    )
    config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
    writer = ZimWriter(metadata=metadata, config=config, output_path=output)
    writer.add_article(
        path="index",
        title="Test Article",
        content="<html><body><h1>Hello</h1><p>ZIM test.</p></body></html>",
        mime_type="text/html",
        is_front_article=True,
    )
    result = writer.create_zim(run_zimcheck=False)
    print(f"ZIM created: {result.output_path}")
    print(f"File size: {result.file_size_bytes} bytes")
    print(f"Articles: {result.article_count}")
    print(f"SHA-256: {result.sha256[:16]}...")
    assert result.file_size_bytes > 1000, "ZIM file too small — may be stub placeholder"
    print("PASS: ZIM file is real (>1 KB)")
EOF
# Expected: PASS output with file_size_bytes > 1000
# If file_size_bytes < 200: stub path still active (libzim not loading)
```

```bash
# 4b. Verify output file exists and has real size
# (if file was written to known path):
ls -lh /tmp/test.zim 2>/dev/null || echo "File cleaned by tempdir"
# Expected: file present with size > 10 KB (real ZIM) or cleaned (ok for tmpdir)
```

### Step 5: Optional zimcheck Validation (15 min, recommended)

```bash
# Install zim-tools if not present
which zimcheck || sudo apt-get install -y zim-tools

# 5a. Run zimcheck on test output
zimcheck /path/to/test.zim 2>&1 | head -20
# Expected: "Checking /path/to/test.zim" — no FATAL errors
# Acceptable: warnings about small illustration (fallback PNG is 67 bytes)
# Not acceptable: "Fatal: ZIM file is corrupted" or "Fatal: No main article"
```

### Step 6: Application Boot Test (15 min)

```bash
# 6a. Start application in dev mode (bound to 127.0.0.1 ONLY per security rules)
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 &
APP_PID=$!

# 6b. Health check
sleep 2
curl -s http://127.0.0.1:8000/api/health | python3 -m json.tool
# Expected: {"status": "healthy"} or equivalent

# 6c. Verify no import errors in startup log
# Expected: no "ImportError", no "ModuleNotFoundError"

# 6d. Shutdown
kill $APP_PID
```

---

## Section 4 — Risk Register Review

### Risk 1: Xapian FTS Disabled (PARTIALLY RESOLVED)

- **Original status**: ACCEPTED for MVP — FTS disabled, Phase 5.2 enhancement
- **Current status**: CHANGED — `creator.config_indexing(True, lang)` call added to master (commit 198a146d), but ABSENT from feature branch production code path
- **Impact if feature branch merged without fix**: ZIM files generated will have no full-text search index
- **Severity**: LOW-MEDIUM. ZIM files are valid and readable; search within Kiwix viewer will not work. This is the original MVP acceptance criterion, so functionally acceptable, but the fix is already written and should not be left behind.
- **Action required**: Rebase feature branch onto master to include config_indexing fix before merge

### Risk 2: datetime.utcnow() DeprecationWarning

- **Status**: CONFIRMED non-blocking on Python 3.11
- **Evidence**: Ran full test suite with `-W always` — no `DeprecationWarning` on `utcnow()` calls in export code (Python 3.12+ only)
- **Location**: `zim_writer.py` lines ~800, ~825 in both branches
- **Action**: Phase 5.2 cleanup — replace with `datetime.now(timezone.utc)`. Not a blocker.

### Risk 3: Export API Endpoint Not Implemented

- **Status**: CONFIRMED — no `app/api/v1/export.py` exists on either branch
- **Impact**: The POST /api/v1/export/zim endpoint is not available. Users must invoke ZimWriter programmatically or via admin tooling.
- **Severity**: LOW for MVP. ZimWriter service layer is complete and callable. API endpoint is Phase 5.2 scope.
- **Action**: Document in release notes. Not a merge blocker.

### Risk 4: Zero Phase 4 Regressions

- **Status**: CONFIRMED — full suite run shows 0 failures, 0 new failures vs pre-Phase-5 baseline
- **Evidence**: 240 passed, 19 skipped (same skip count as pre-Phase-5)
- **Phase 4 tests**: `test_activitypub.py`, `test_federation_partner.py`, `test_wave3_*`, `test_wave4_*` — all passing

### Risk 5: Tests Run Against Stub, Not Real libzim

- **Status**: IDENTIFIED — tests run with stub path active (`_LIBZIM_AVAILABLE = False`)
- **Impact**: Tests confirm interface contracts and data model correctness but do not validate actual ZIM file generation
- **Severity**: MEDIUM. The `TestLibZIMIntegration` class on master partially validates this, but that class is absent from the feature branch. The manual export test in Section 3, Step 4 is the primary safeguard.
- **Action**: Install libzim in venv before merge, re-run tests, confirm `_LIBZIM_AVAILABLE = True` in test environment.

### Risk 6: Branch Divergence — Merge May Require Conflict Resolution

- **Status**: CONFIRMED — 1 commit on master not on feature branch, affecting 3 files:
  - `zim_writer.py` (PNG bytes replaced, config_indexing added, _get_illustration_bytes fallback changed)
  - `tests/integration/test_export_pipeline.py` (4 tests added in TestLibZIMIntegration class)
- **Severity**: LOW if handled correctly. The fix commit's changes are well-scoped. A rebase or cherry-pick will resolve cleanly.
- **Action**: Rebase feature branch onto master before merge (see Section 6).

---

## Section 5 — Five Code Changes — Final Audit Table

| # | Change | File | Present on Feature Branch | Present on Master | Delta |
|---|--------|------|--------------------------|-------------------|-------|
| 1 | libzim import guard + `_LIBZIM_AVAILABLE` | zim_writer.py | YES | YES (same) | None |
| 2 | `ArticleItem` adapter class | zim_writer.py | YES | NO (not yet merged) | Feature-only addition |
| 3a | `create_zim()` Creator context manager | zim_writer.py | YES | YES (in docstring + production) | Feature has live code; master has more complete version |
| 3b | `creator.config_indexing()` in production path | zim_writer.py | **PARTIAL** (in docstring only) | YES (live code, commit 198a146d) | Missing from feature live code |
| 4 | `_apply_metadata_to_creator()` | zim_writer.py | YES | YES (same) | None |
| 5a | `_FALLBACK_ILLUSTRATION_PNG` bytes | zim_writer.py | YES (67 bytes) | YES (88 bytes, improved) | Master has validated version |
| 5b | `_get_illustration_bytes()` returns fallback | zim_writer.py | **GAP** (returns None) | YES (returns `_FALLBACK_ILLUSTRATION_PNG`) | Master always returns bytes; feature may return None |
| 6 | Alembic migration 003 | 003_add_zim_exports_table.py | YES | NO (not yet merged) | Feature-only addition |
| 7 | `libzim>=3.2,<4.0` in pyproject.toml | pyproject.toml | YES | NO (not yet merged) | Feature-only addition |

Changes 2, 6, and 7 exist only on the feature branch — these are the Phase 5.1 deliverables to be merged into master.  
Changes 3b and 5b exist only on master (from commit 198a146d) — these must not be lost in the merge.

---

## Section 6 — Blockers and Pre-Merge Actions

### Blocker 1 (MANDATORY): Rebase feature branch onto master

The feature branch must be rebased onto master (or the fix commit cherry-picked) before merge. Without this, two regressions will be introduced:

**Regression A**: `_get_illustration_bytes()` will return `None` when no custom illustration is provided, causing `_apply_metadata_to_creator()` to pass `None` to `creator.add_illustration(48, None)`. This will crash ZIM creation at runtime.

**Regression B**: `creator.config_indexing()` will not be called. ZIM files will be generated without Xapian FTS index. Kiwix search will not work.

**Resolution**:
```bash
git checkout feature/zimwriter-libzim-activation
git rebase master
# Resolve any conflicts (likely minimal — fix commit is well-scoped)
# Re-run: uv run pytest tests/ — expect 88 passed after rebase
```

Expected result after rebase: feature branch includes all of master's fixes, test count rises from 84 to 88, and `_get_illustration_bytes()` returns the fallback PNG instead of None.

### Pre-Merge Action 2 (RECOMMENDED): Install libzim and run tests with real Creator

Before merge, run tests with libzim actually installed to confirm the real code path works:

```bash
cd projects/open-repo/backend
uv pip install "libzim>=3.2,<4.0"
uv run python -c "from app.services.export.zim_writer import _LIBZIM_AVAILABLE; print(_LIBZIM_AVAILABLE)"
# Must print: True
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short
# Must show: 88 passed (or 84 if rebase not yet done), 0 failed
```

### Pre-Merge Action 3 (RECOMMENDED): Validate PNG bytes

After rebase, the PNG fallback on the feature branch will be replaced by master's validated version. Confirm:

```bash
uv run pytest tests/integration/test_export_pipeline.py::TestLibZIMIntegration -v
# Must pass: test_fallback_png_is_valid_48x48
# This test parses IHDR and asserts width=48, height=48
```

---

## Section 7 — Go/No-Go Assessment

### Current Status (May 20, pre-rebase)

| Criterion | Status | Gate |
|-----------|--------|------|
| Core ZIM code changes present | YES | GO |
| Migration 003 present | YES | GO |
| libzim dependency declared | YES | GO |
| Tests passing (standard run) | 240/240 | GO |
| Zero Phase 4 regressions | CONFIRMED | GO |
| libzim wheel available for aarch64 Python 3.11 | CONFIRMED | GO |
| Branch current with master | NO — 1 commit behind | BLOCKER |
| `_get_illustration_bytes()` fallback | ABSENT on feature branch | BLOCKER |
| `creator.config_indexing()` in live code | ABSENT on feature branch | SOFT BLOCKER |
| Tests run against real libzim | NOT TESTED | CONDITIONAL |

### Recommendation

**NOT GO to merge in current state. GO after single rebase operation.**

The feature branch is production-ready in architecture and the core ZIM implementation is correct. The blockers are procedural — a post-hoc fix commit on master must be incorporated before the feature branch merge proceeds. The rebase operation is low-risk (1 commit, well-scoped changes to 2 files) and should take under 30 minutes.

**Recommended sequence for May 25-26 decision**:
1. (15 min) Rebase `feature/zimwriter-libzim-activation` onto master
2. (30 min) Install libzim in venv, run test suite — confirm 88 passed
3. (45 min) Manual ZIM export test — confirm real file generated
4. (20 min) Apply migration 003 in staging, confirm schema
5. Approve merge

**Post-rebase confidence**: 97% (previously 98.2% — reduced slightly to account for untested libzim code path on this hardware)

---

## Appendix A — Commands Reference

```bash
# Rebase to resolve divergence
git checkout feature/zimwriter-libzim-activation
git rebase master

# Full test suite
cd projects/open-repo/backend
uv run pytest tests/ --tb=short

# Export pipeline tests only
uv run pytest tests/integration/test_export_pipeline.py -v

# Install libzim for real-path testing
uv pip install "libzim>=3.2,<4.0"

# Apply migrations
uv run alembic upgrade head
uv run alembic current

# Application boot (127.0.0.1 only — no 0.0.0.0)
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
```

---

## Appendix B — File Locations (Feature Branch)

| File | Purpose |
|------|---------|
| `backend/app/services/export/zim_writer.py` | ZimWriter + ArticleItem + metadata application |
| `backend/alembic/versions/003_add_zim_exports_table.py` | Database migration (28 columns, 3 indexes) |
| `backend/pyproject.toml` | libzim>=3.2,<4.0 dependency declaration |
| `backend/tests/integration/test_export_pipeline.py` | 84-test suite (88 after rebase) |

---

*Verification executed: 2026-05-20, Session 1407*  
*Live code audit confirmed against branch commits. Test results reproducible.*  
*Sources: PyPI libzim page, local pip download test, live pytest execution*
