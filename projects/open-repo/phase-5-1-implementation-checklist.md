---
title: "Phase 5.1 Pre-Merge Implementation Checklist"
feature_branch: feature/zimwriter-libzim-activation
created: 2026-05-21
session: 1447
status: READY_TO_MERGE
---

# Phase 5.1 Pre-Merge Implementation Checklist

**Branch**: `feature/zimwriter-libzim-activation` → `master`
**Created**: 2026-05-21 (session 1447)
**Status**: READY TO MERGE (stub phase) | ACTIVATION CHECKLIST follows merge

This document provides two checklists:
- **Part A**: Pre-merge validation steps (run before approving the merge PR)
- **Part B**: Post-merge activation steps (run before replacing stub with real libzim)

---

## Part A: Pre-Merge Validation Checklist

These steps validate the feature branch is safe to merge. All items in Part A have been completed by the session 1447 audit.

### A1. Code Security Review

**Status**: COMPLETE

- [x] Review `zim_writer.py` for injection vulnerabilities
  - Result: No shell injection. `subprocess.run()` uses list-form command, `shell=False` by default
  - Result: `zimcheck_binary` defaults to `"zimcheck"` (not user-supplied via HTTP)
- [x] Check for path traversal in output file handling
  - Result: `output_path` is a `pathlib.Path` set by the application, not user input
  - Result: `ZimEntry.path` is validated (no leading slash, no `//`), ZIM paths are archive-internal
- [x] Check attribution footer for XSS (federated content)
  - Result: FINDING — `source_node_url` and `source_node_name` are interpolated into HTML without `html.escape()`
  - Action: Post-merge fix required before federation activation (see Part B item B1)
- [x] Verify no `shell=True` in subprocess calls
  - Result: Confirmed 0 occurrences of `shell=True`
- [x] Verify no hardcoded credentials or API keys
  - Result: None found
- [x] Check `open()` calls for path manipulation
  - Result: 2 calls — `open(path, "rb")` for illustration file reading; path is caller-supplied and validated

**Security linter note**: `bandit` is not available in the project venv. Manual review was conducted. To run a formal bandit scan post-merge:
```bash
uv pip install bandit
bandit -r projects/open-repo/backend/app/services/export/ --severity-level low
```

Expected bandit findings (acceptable/known):
- B603 (`subprocess.run` without shell): Will flag as informational; this call is safe (list-form, no user input in command args)
- B605/B607: Not applicable (no `shell=True`, no `os.system`)

### A2. Integration Test Suite

**Status**: COMPLETE — ALL PASS

- [x] Run the full integration test suite
  ```bash
  cd projects/open-repo/backend
  .venv/bin/python -m pytest tests/integration/test_export_pipeline.py -v
  ```
  - Result: **88 passed in 0.13 seconds** (no failures, no warnings)
- [x] Verify ZimMetadata validation tests pass (8 tests)
- [x] Verify ExportConfig validation tests pass (6 tests)
- [x] Verify ZimEntry validation tests pass (7 tests)
- [x] Verify ZimWriter initialization tests pass (3 tests)
- [x] Verify add_article / add_resource tests pass (9 tests)
- [x] Verify create_zim lifecycle tests pass (7 tests)
- [x] Verify attribution footer tests pass (3 tests)
- [x] Verify static method tests pass (8 tests)
- [x] Verify OPDS entry/generator tests pass (21 tests)
- [x] Verify end-to-end pipeline tests pass (3 tests)
- [x] Verify libzim integration readiness tests pass (4 tests)
  - [x] Fallback PNG is valid 48x48 PNG (IHDR verified by struct.unpack)
  - [x] `_get_illustration_bytes()` always returns bytes (fallback path confirmed)
  - [x] `config_indexing(True, "eng")` call verified via MagicMock
  - [x] ZIM stub file created and readable

### A3. Dependency Compatibility Check

**Status**: COMPLETE

- [x] Confirm Python version compatibility
  - System Python: 3.11.2 — libzim supports cp311 on aarch64
- [x] Confirm platform wheel availability
  - Platform: aarch64 (Raspberry Pi 5)
  - Available wheel: `libzim-3.9.0-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl`
  - Recommend: `libzim>=3.10.0,<4.0` (C++ 9.7.0 hardening patches)
- [x] Confirm glibc version compatibility
  - Pi OS Bookworm (Debian 12): glibc 2.36 >> manylinux_2_27 requirement (2.27)
- [x] Confirm no conflicts with existing dependencies
  - libzim has zero Python transitive dependencies (self-contained wheel)
  - No conflicts with fastapi, pydantic, sqlalchemy, asyncpg
- [x] Confirm zimcheck is installable
  - `sudo apt-get install zim-tools` provides `zimcheck` binary
- [x] Verify migration 003 chain
  - `003_add_zim_exports_table.py` sets `down_revision = "002"` — correct chain

### A4. Feature Branch Diff Review

**Status**: COMPLETE

Files changed in `feature/zimwriter-libzim-activation` vs `master`:

| File | Change | Status |
|---|---|---|
| `backend/app/services/export/zim_writer.py` | New file (1,109 lines) | REVIEWED |
| `backend/alembic/versions/003_add_zim_exports_table.py` | New file | REVIEWED |
| `backend/pyproject.toml` | No changes | NOTE: libzim must be added post-merge |
| `backend/README.md` | No changes | NOTE: needs Phase 5 section post-merge |
| `phase-5-candidate-1-implementation-checklist.md` | Updated | Informational |
| `phase-5-candidate-1-implementation-verification.md` | Updated | Informational |

- [x] `zim_writer.py` reviewed — complete stub with valid API contracts
- [x] `003_add_zim_exports_table.py` reviewed — 23-column table, correct indexes, correct down_revision
- [x] No accidental `0.0.0.0` bindings introduced
- [x] No API endpoints introduced (no routes.py changes) — export is backend-only at this stage
- [x] No changes to existing test files that might break CI

### A5. Go/No-Go Merge Decision

**Decision criteria**:

| Criterion | Status |
|---|---|
| All 88 integration tests pass | PASS |
| No CVEs in libzim dependency | PASS |
| No merge-blocking security vulnerabilities | PASS |
| ARM64 wheel confirmed available | PASS |
| Migration chain is correct | PASS |
| No 0.0.0.0 bindings introduced | PASS |
| Code security review complete | PASS |

**GO/NO-GO: GO — merge is approved for stub phase.**

Post-merge, follow Part B before activating real libzim integration.

---

## Part B: Post-Merge Activation Checklist

Run these steps after merging to master, before replacing `_stub_write_placeholder()` with real libzim Creator calls.

### B1. Fix Attribution Footer XSS (Security)

**Priority: HIGH — required before federation activation**
**Estimated effort**: 15 minutes

In `app/services/export/zim_writer.py`, update `_apply_attribution_footer()`:

```python
import html as html_lib  # Add to imports

def _apply_attribution_footer(self, content, source_node_url, source_node_name,
                               license_name, license_url):
    if not source_node_url:
        return content

    # Validate URL scheme to prevent javascript: protocol injection
    from urllib.parse import urlparse
    parsed = urlparse(source_node_url)
    if parsed.scheme not in ("http", "https"):
        logger.warning("Rejecting source_node_url with unsafe scheme: %s", parsed.scheme)
        return content

    # HTML-escape all user-controlled strings
    safe_name = html_lib.escape(source_node_name or "")
    safe_license_name = html_lib.escape(license_name or "")
    # source_node_url and license_url are used in href — scheme already validated above
    ...
```

After fixing:
- Add a test case for `source_node_name = '<script>alert(1)</script>'`
- Add a test case for `source_node_url = 'javascript:alert(1)'`
- Run the full test suite to confirm 88+ tests still pass

### B2. Add ZimExport SQLAlchemy ORM Model

**Priority: HIGH — required before wiring the export service to the database**
**Estimated effort**: 30 minutes

Add to `app/models.py`:

```python
class ExportStatus(str, enum.Enum):
    """Export job status enumeration."""
    GENERATING = "generating"
    COMPLETE = "complete"
    FAILED = "failed"
    SUPERSEDED = "superseded"


class ZimExport(Base):
    """ZIM export job record — mirrors zim_exports table from migration 003."""

    __tablename__ = "zim_exports"

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    zim_uuid = Column(String(36), nullable=False, unique=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    flavour = Column(String(50), nullable=False, index=True)
    language = Column(String(10), nullable=False)
    period = Column(String(10), nullable=False, index=True)
    article_count = Column(Integer, nullable=False)
    file_size_bytes = Column(BigInteger, nullable=False)
    sha256 = Column(String(64), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(80), nullable=False)
    cdn_url = Column(String(512), nullable=True)
    local_path = Column(String(512), nullable=True)
    status = Column(String(20), nullable=False, default='generating', index=True)
    is_current = Column(Boolean, nullable=False, default=False, index=True)
    is_reference = Column(Boolean, nullable=False, default=False)
    export_scope = Column(String(20), nullable=False)
    scope_value = Column(String(100), nullable=True)
    include_images = Column(Boolean, nullable=False, default=False)
    zimcheck_passed = Column(Boolean, nullable=True)
    zimcheck_output = Column(Text, nullable=True)
    generation_duration_seconds = Column(Float, nullable=True)
    started_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    superseded_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<ZimExport id={self.id} name={self.name} period={self.period} status={self.status}>"
```

Also add `Boolean` and `Float` to the SQLAlchemy imports in `models.py`.

Verification: Run `alembic check` to confirm the ORM model matches the migration.

### B3. Install libzim Dependency

**Priority: HIGH — required to replace stub with real Creator calls**
**Estimated effort**: 5 minutes (install) + 2–4 hours (implementation)

Step 1: Add to `pyproject.toml` dependencies:
```toml
"libzim>=3.10.0,<4.0",  # ZIM file generation (Phase 5.1)
```

Step 2: Install:
```bash
cd projects/open-repo/backend
uv pip install -e ".[dev]"

# Verify installation
.venv/bin/python -c "import libzim; print(libzim.__version__)"
```

Step 3: Install zimcheck:
```bash
sudo apt-get install zim-tools
zimcheck --version
```

Step 4: Replace stub in `create_zim()`. The correct implementation pattern is already documented in the `create_zim()` docstring at lines 719–741:

```python
from libzim.writer import Creator, Item, StringProvider, Hint

class ArticleItem(Item):
    def __init__(self, entry: ZimEntry): self.entry = entry
    def get_path(self): return self.entry.path
    def get_title(self): return self.entry.title
    def get_mimetype(self): return self.entry.mime_type
    def get_hints(self):
        return {Hint.FRONT_ARTICLE: self.entry.is_front_article}
    def get_contentprovider(self):
        content = self.entry.content
        if isinstance(content, str):
            content = content.encode("utf-8")
        return StringProvider(content)

with Creator(str(self.output_path)) as creator:
    creator.config_indexing(True, self.config.language_iso3)
    creator.set_mainpath("index")
    self._apply_metadata_to_creator(creator)
    for entry in self._entries:
        creator.add_item(ArticleItem(entry))
# Creator.__exit__ triggers ZIM file write
```

Step 5: Remove `_stub_write_placeholder()` method and its call from `create_zim()`.

Step 6: Change `run_zimcheck=False` to `run_zimcheck=True` in test fixtures (or keep False for unit tests but add an explicit integration test that uses real libzim against a real ZIM file).

### B4. Run Performance Baseline Test

**Priority: MEDIUM — validate Pi 5 can handle real ZIM creation**
**Estimated effort**: 1 hour

After installing real libzim:

```python
# Save as scripts/benchmark_zimwriter.py
import time
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

metadata = ZimMetadata(
    title="Open-Repo: Benchmark Test",
    description="Performance baseline measurement",
    language="eng",
    name="open-repo_en_nopic",
    flavour="nopic",
    creator="Open-Repo Community",
    publisher="Open-Repo",
    source_url="https://test.example.org",
)
config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
output_path = Path("/tmp/benchmark_export.zim")

writer = ZimWriter(metadata=metadata, config=config, output_path=output_path)

# Generate 500 synthetic articles (~8 KB each = ~4 MB raw)
start = time.time()
for i in range(500):
    html = f"""<!DOCTYPE html>
<html><head><title>Procedure {i}: Water Safety</title></head>
<body><h1>Procedure {i}</h1>
<p>{"Step content. " * 100}</p>
</body></html>"""
    writer.add_article(
        path=f"water/article-{i:04d}",
        content=html,
        article_type="procedure",
    )

result = writer.create_zim(run_zimcheck=True)
elapsed = time.time() - start

print(f"Articles: {result.article_count}")
print(f"ZIM size: {result.file_size_bytes / 1024 / 1024:.1f} MB")
print(f"Wall time: {elapsed:.1f} seconds")
print(f"zimcheck: {'PASSED' if result.zimcheck_passed else 'FAILED'}")
print(f"SHA-256: {result.sha256[:16]}...")
```

Run: `uv run python scripts/benchmark_zimwriter.py`

Record results in WORKLOG.md. Expected targets:
- 500 articles: < 60 seconds wall time
- ZIM file size: < 5 MB (after zstd compression)
- zimcheck: PASSED

If write time > 120 seconds for 500 articles, investigate whether Raspberry Pi thermal throttling is the cause (check `vcgencmd measure_temp`).

### B5. Update README

**Priority: LOW — user-facing documentation**
**Estimated effort**: 30 minutes

Add to `backend/README.md`:

1. Update header: "Phase 5 Complete - ... + ZIM Offline Export"
2. Add to "What's Implemented" section: ZIM export service and OPDS catalog
3. Add "Offline Export" section:
   - How to trigger a ZIM export
   - How to download the ZIM file
   - How to use with Kiwix (link to kiwix.org)
4. Update "Project Structure" tree to include `app/services/export/`
5. Add `libzim` and `zim-tools` to Quick Start setup commands
6. Update "Next Phases" section to reflect actual current state

### B6. Wire Export Service to API

**Priority: MEDIUM — makes the feature user-accessible**
**Estimated effort**: 2–4 hours

This step is out of scope for the current PR but is the next logical task:

1. Create `app/services/export/export_service.py` — queries ContentItem from DB, calls ZimWriter
2. Add `POST /api/exports/zim` endpoint to `routes.py` — triggers async export job
3. Add `GET /opds/v2/root.xml` endpoint — returns OPDS catalog XML
4. Add `GET /opds/v2/entries.xml` endpoint — returns acquisition feed
5. Wire migration 003 by running `alembic upgrade head` in production

---

## Summary: Go/No-Go Criteria

### Merge Decision (Stub Phase)

| Criteria | Requirement | Actual | Decision |
|---|---|---|---|
| Test suite | All pass | 88/88 pass | GO |
| Security blockers | 0 merge blockers | 0 | GO |
| ARM64 wheel | Available | Confirmed | GO |
| Migration chain | Correct | 001 → 002 → 003 | GO |
| 0.0.0.0 bindings | None introduced | None found | GO |

**MERGE DECISION: GO**

### Activation Decision (Real libzim Integration)

| Criteria | Requirement | Status | Decision |
|---|---|---|---|
| B1: Attribution XSS fix | html.escape() applied | NOT YET | HOLD |
| B2: ZimExport ORM model | Added to models.py | NOT YET | HOLD |
| B3: libzim installed | pip install libzim | NOT YET | HOLD |
| B3: _stub_write_placeholder replaced | Real Creator calls | NOT YET | HOLD |
| B4: Performance baseline | < 60s for 500 articles | NOT TESTED | HOLD |
| zimcheck passing | Real ZIM validates | NOT TESTED | HOLD |

**ACTIVATION DECISION: HOLD — 3 required steps before going live**

---

## Change Log

| Date | Session | Change |
|---|---|---|
| 2026-05-21 | 1447 | Initial checklist created from pre-merge audit |
