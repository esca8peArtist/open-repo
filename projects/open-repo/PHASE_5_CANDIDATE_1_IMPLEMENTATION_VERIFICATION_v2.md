---
title: "Phase 5 Candidate 1 — ZimWriter/libzim Pre-Deployment Verification (v2)"
project: open-repo
phase: 5
candidate: 1
document_type: pre-deployment-audit
status: verified-ready-with-caveats
date: 2026-05-20
auditor: General Research Agent (Session 1435)
supersedes: PHASE_5_CANDIDATE_1_IMPLEMENTATION_VERIFICATION.md
---

# Phase 5 Candidate 1: Pre-Deployment Verification Report (v2)
## ZimWriter/libzim — Definitive State Audit

**Bottom line up front**: Candidate 1 is ready to implement. libzim 3.9.0 is installed and verified functional. 88 existing tests pass. The scaffold is complete. One API-level bug exists in the roadmap's Change 3 (config_indexing placement) that will cause a RuntimeError at runtime if not corrected — this is documented and fixable with a single line reorder. No other blockers.

**Correction to previous reports**: The `PHASE_5_CANDIDATE_1_IMPLEMENTATION_VERIFICATION_FINAL.md` document (Session 1353) reported implementation as "100% complete" on branch `feature/zimwriter-libzim-activation`. Live inspection of the codebase on 2026-05-20 shows `zim_writer.py` still contains `_stub_write_placeholder()` and the `create_zim()` method still calls it. The implementation is NOT yet complete in the working tree. The feature branches exist but have not been merged to master. This report reflects the actual state as of the current working tree.

---

## Section 1: libzim Python Bindings Audit

### 1.1 Installation Status

| Item | Result |
|------|--------|
| libzim in uv environment | **INSTALLED — 3.9.0** |
| Install command | `uv pip install "libzim>=3.2,<4.0"` (already done) |
| Import test | `from libzim.writer import Creator, Item, StringProvider, Hint` — **PASS** |
| Underlying C library | **libzim 9.5.1** (via `libzim.get_libzim_version()`) |
| Python version | 3.11.2 (exceeds >=3.10 requirement) |
| Platform | Linux aarch64 (Raspberry Pi 5, 64-bit OS) |
| Wheel type | Pre-built binary: `manylinux_2_27_aarch64` |
| Compiler required | **No** — binary wheel, no source compilation |

The version pinned in the roadmap (`>=3.2,<4.0`) is satisfied by 3.9.0. The constraint also covers 3.10.0, which is the latest release on PyPI as of the audit date, meaning `uv pip install "libzim>=3.2,<4.0"` will currently resolve to 3.10.0 if installed fresh. Both versions use identical API.

### 1.2 Xapian Status

Xapian full-text search support is bundled inside the libzim binary wheel. No system packages required. Verified:

```
uv run python3 -c "from libzim.writer import Creator; print(dir(Creator))"
# config_indexing is present in the output
```

**Critical finding — config_indexing placement**: The roadmap's Change 3 code block shows:

```python
with Creator(str(self.output_path)) as creator:
    creator.config_indexing(True, self.config.language_iso3)  # ← WRONG POSITION
    creator.set_mainpath("index")
    ...
```

This will raise `RuntimeError: Creator started` at runtime. The libzim API requires `config_indexing()` to be called BEFORE the `with` context is entered. Verified:

```python
# This raises RuntimeError: Creator started
with Creator(str(out)) as creator:
    creator.config_indexing(True, 'eng')  # ERROR

# Correct pattern:
creator = Creator(str(out))
creator.config_indexing(True, 'eng')  # Before __enter__
with creator:
    creator.add_metadata(...)
```

`set_mainpath()` and `add_metadata()` placement rules:
- `set_mainpath()`: Can be called before OR after context entry — works both ways
- `add_metadata()`: Must be called INSIDE the context (raises `Creator not started` if before)
- `add_illustration()`: INSIDE the context — confirmed functional
- `add_item()`: INSIDE the context — confirmed functional

The existing test `test_config_indexing_call_in_metadata_apply` uses a MagicMock to assert `config_indexing` is called, but does not test the actual sequencing. The mock does not detect this placement bug.

### 1.3 pyproject.toml Gap

libzim 3.9.0 is installed in the uv environment but is NOT declared in `pyproject.toml`. Current `[project.dependencies]` list:

```toml
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn[standard]>=0.24.0",
    "pydantic>=2.0.0",
    "pydantic[email]>=2.0.0",
    "asyncpg>=0.29.0",
    "sqlalchemy>=2.0.0",
    "alembic>=1.13.0",
    "python-multipart>=0.0.6",
    "meilisearch>=0.30.0",
]
```

`libzim` and `jinja2` are both missing. `jinja2 3.1.6` is installed transitively but not declared. Both must be added.

---

## Section 2: ZIM Stub Validation — Sample of 10

### 2.1 What "88 stubs" means

The 88 stubs are Python test cases in `tests/integration/test_export_pipeline.py` (1,573 lines, 88 tests confirmed passing). The `ZimWriter.create_zim()` method still calls `_stub_write_placeholder()`, which writes a text placeholder file. The stubs are **test coverage stubs that will pass through to real libzim once the 5 code changes are applied** — not literal data files.

Baseline confirmed: `88 passed in 0.30s`

### 2.2 Random sample of 10 test scenarios — schema consistency

Ten tests were manually executed against the current stub implementation. All pass. Schema findings:

| Test | Schema Coverage | Status | Notes |
|------|----------------|--------|-------|
| `test_valid_metadata_initializes` | title, language, name, flavour, creator, publisher, source_url | PASS | All required fields accepted without error |
| `test_date_auto_generated_when_none` | date field (YYYY-MM-DD auto-fill) | PASS | Auto-generates current date when `date=None` |
| `test_validate_returns_empty_for_valid` | all 8 required fields | PASS | `ZimMetadata.validate()` returns `[]` for valid data |
| `test_validate_reports_description_over_80_chars` | description ≤80 chars | PASS | `validate()` returns error string containing "description" |
| `test_invalid_name_raises_value_error` | name format (`{pub}_{lang}_{flavour}`) | PASS | Invalid name raises `ValueError` at construction time |
| `test_valid_entry_initializes` | path, title, content, is_front_article | PASS | Default mime_type is `text/html`, is_front_article is `True` |
| `test_path_cannot_start_with_slash` | path validation | PASS | Raises `ValueError` on `/invalid` |
| `test_add_article_increments_count` | article buffering | PASS | `article_count` increments correctly |
| `test_create_zim_returns_sha256` | sha256 output | PASS | 64-character hex string returned even for stub |
| `test_create_zim_only_once` | re-entrancy guard | PASS | Second call raises `RuntimeError` |

### 2.3 Required ZIM field coverage in current schema

| ZIM Mandatory Field | In ZimMetadata | Python Validation | Test Coverage | Gap |
|--------------------|---------------|-------------------|--------------|-----|
| Title | `title` | Non-empty check | Yes | None |
| Description | `description` | ≤80 chars (hard) | Yes | None |
| Language | `language` | Non-empty check | Yes | No ISO 639-3 format validation |
| Creator | `creator` | Non-empty check | Yes | None |
| Publisher | `publisher` | Non-empty check | Yes | None |
| Date | `date` | YYYY-MM-DD regex | Yes | None |
| Name | `name` | Full naming regex | Yes | None |
| Illustration_48x48 | fallback constant | File existence check | Yes (4 tests) | None |
| Flavour | `flavour` | Enum | Yes | None |
| Tags | `tags` | Default provided | Indirect | None |
| Scraper | `scraper` | Default provided | Indirect | None |

**One gap**: Language validation only confirms the field is non-empty. A malformed code like `"e"` or `"english"` passes Python validation but fails zimcheck's ISO 639-3 check. Low risk given existing fixtures use `"eng"`.

### 2.4 Fallback illustration verification

The `_FALLBACK_ILLUSTRATION_PNG` constant in `zim_writer.py` (line 55) was verified by parsing the PNG IHDR chunk:
- PNG signature: valid (`\x89PNG\r\n\x1a\n`)
- Dimensions: **48x48** (confirmed by parsing `width` and `height` from IHDR)
- `creator.add_illustration(48, FALLBACK)` inside a Creator context: **no error**

---

## Section 3: Missing Pre-Requisites

### 3.1 Blocking items (must complete before implementation)

| Item | Current State | Action | Priority |
|------|--------------|--------|----------|
| `config_indexing()` placement in Change 3 | Bug: placed inside context (will raise RuntimeError) | Reorder: call before `with Creator(...)` context entry | **P0 — must fix before implementing** |
| `libzim>=3.2,<4.0` in pyproject.toml | Not declared (installed manually) | Add to `[project.dependencies]` | P0 |
| `jinja2>=3.1` in pyproject.toml | Not declared (installed transitively) | Add to `[project.dependencies]` | P0 |

### 3.2 Non-blocking items (required before go-live, not before implementation)

| Item | Current State | Action | Priority |
|------|--------------|--------|----------|
| `zimcheck` binary | Not installed (`zim-tools 3.1.3-1` available in apt cache) | `sudo apt install zim-tools` | P1 (before integration tests) |
| Alembic migration 003 | Does not exist (only 001 and 002) | `alembic revision --autogenerate -m "add_zim_exports_table"` | P1 (before go-live) |
| `ZimExport` SQLAlchemy model in `app/models.py` | Not present | Add `ZimExportStatus` enum + `ZimExport` model | P1 (before go-live) |
| Export API endpoint | Not present (`app/api/v1/` has only `admin/`) | Create `app/api/v1/export.py` | P1 (before go-live) |
| 48x48 branded PNG | Using fallback transparent PNG | Commission real branded icon | P2 (before public launch) |
| Cloudflare R2 CDN credentials | Not configured | Required only for CDN upload step | P2 (Phase 5.2) |
| APScheduler weekly export job | Not implemented | Required for automated exports | P2 (Phase 5.2) |

### 3.3 Python version and system compatibility

| Check | Result | Notes |
|-------|--------|-------|
| Python 3.11.2 ≥ 3.10 | PASS | |
| Linux aarch64 wheel available | PASS | `manylinux_2_27_aarch64` |
| Disk space (`/tmp`) | PASS | 201 GB free (project memory) |
| RAM available | PASS | 6.9 GB — 500-item buffer peaks ~50 MB |
| Thermal throttling | MONITOR | RPi5 idle 81-84°C; schedule exports at 02:00 UTC |

### 3.4 Feature branch status

Three feature branches exist in git:
- `feature/zimwriter-libzim-activation` (also on `remotes/open-repo/`)
- `feature/phase5-zimwriter-libzim-implementation` (also on `remotes/open-repo/`)
- `feature/phase5-zimwriter-add-migration-003`

These branches were created by previous sessions but have **not been merged to master**. The working tree on master still has the stub implementation. The checklist below assumes work starts fresh on master (or from one of these branches, after verifying their state independently).

---

## Section 4: Hour-by-Hour Implementation Timeline

### 4.1 The 5 code changes + corrected API sequencing

All changes land in `backend/app/services/export/zim_writer.py` plus `pyproject.toml`.

**Change 0: Update pyproject.toml (15 minutes)**

Add to `[project.dependencies]`:
```toml
"libzim>=3.2,<4.0",
"jinja2>=3.1",
```

Verify: `uv pip install -e ".[dev]"` succeeds; `from libzim.writer import Creator` works.

**Change 1: Add libzim import guard (15 minutes)**

After line 50 (after `from typing import Optional`), insert:
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

Verify: all 88 tests still pass after this change alone.

**Change 2: Add ArticleItem adapter class (45 minutes)**

After the `ZimEntry` dataclass (before the `ZimWriter` class, around line 408), add:
```python
class ArticleItem(Item):
    def __init__(self, entry: "ZimEntry") -> None:
        super().__init__()
        self._entry = entry

    def get_path(self) -> str:
        return self._entry.path

    def get_title(self) -> str:
        return self._entry.title

    def get_mimetype(self) -> str:
        return self._entry.mime_type

    def get_hints(self) -> dict:
        return {Hint.FRONT_ARTICLE: self._entry.is_front_article}

    def get_contentprovider(self) -> "StringProvider":
        content = self._entry.content
        if isinstance(content, str):
            content = content.encode("utf-8")
        return StringProvider(content)
```

Verify: all 88 tests still pass.

**Change 3: Replace stub in create_zim() (1 hour)**

**CORRECTED implementation** (corrects config_indexing placement bug):

Replace the stub block at line 762:
```python
        # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
        # See the docstring above for the correct implementation pattern.
        # For now, write a placeholder file to allow test harness to run.
        self._stub_write_placeholder()
```

With:
```python
        if not _LIBZIM_AVAILABLE:
            self._stub_write_placeholder()
        else:
            # config_indexing MUST be called before entering the Creator context
            creator = Creator(str(self.output_path))
            creator.config_indexing(True, self.config.language_iso3)
            creator.set_mainpath("index")
            with creator:
                self._apply_metadata_to_creator(creator)
                for entry in self._entries:
                    creator.add_item(ArticleItem(entry))
            # Creator.__exit__ triggers ZIM file finalization
```

**Why the docstring example in the roadmap is wrong**: The docstring on line 735 shows `creator.config_indexing()` inside the `with` block. That pattern raises `RuntimeError: Creator started`. The corrected pattern above instantiates the Creator, configures it, then enters the context.

Verify: generate a 5-article ZIM and confirm magic bytes = `b'\x5a\x49\x4d\x04'`:
```bash
uv run python3 -c "
import tempfile
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

tmp = tempfile.mkdtemp()
m = ZimMetadata(title='Test', description='Test library', language='eng',
    name='open-repo_en_nopic', flavour='nopic', creator='Test', publisher='Test',
    source_url='https://example.org')
writer = ZimWriter(metadata=m, config=ExportConfig(), output_path=Path(tmp)/'t.zim', zimcheck_binary=None)
writer.add_article(path='index', content='<html><body><h1>Home</h1></body></html>', article_type='procedure')
result = writer.create_zim(run_zimcheck=False)
magic = open(result.output_path, 'rb').read(4)
print('Magic:', magic.hex(), '— valid ZIM:', magic == b'\x5a\x49\x4d\x04')
"
```

**Change 4: Implement _apply_metadata_to_creator() (30 minutes)**

The method at line 873 already has the correct implementation body (it was partially pre-filled with a try/except AttributeError guard). Review the current implementation against the required fields, confirm all 11 `add_metadata()` calls are present, and verify `add_illustration()` is included.

The current implementation wraps everything in `try: ... except AttributeError: pass`. This should remain for safety (it allows the mock-based test `test_config_indexing_call_in_metadata_apply` to pass), but note that in production this silently swallows real errors. Before the PR is merged, the AttributeError guard should be removed or narrowed.

**Change 5: zimcheck integration (30 minutes, no code changes)**

Install: `sudo apt install zim-tools`
Verify: `zimcheck --version` returns `3.1.3`
Test: run zimcheck against the Change 3 output ZIM. Expected: exit code 0.

If zimcheck fails, common causes and fixes:
- Illustration wrong dimensions: fallback PNG is confirmed 48x48, so this is unlikely
- Description >80 chars: test data uses short descriptions, confirmed safe
- Name format invalid: `test_en_nopic` passes the naming regex
- Empty article title: `ZimEntry.__post_init__` raises ValueError for empty front-article titles

### 4.2 Hour-by-hour timeline

| Hour | Task | Completion Gate |
|------|------|----------------|
| 0:00–0:15 | Change 0: Add libzim + jinja2 to pyproject.toml | `uv pip install -e ".[dev]"` succeeds |
| 0:15–0:30 | git checkout feature branch, run baseline 88 tests | `88 passed` confirmed |
| 0:30–0:45 | Change 1: Add import guard | `88 passed` — no regressions |
| 0:45–1:30 | Change 2: Add ArticleItem class | `88 passed`; sanity test ArticleItem methods |
| 1:30–2:30 | Change 3: Replace stub in create_zim() (corrected API) | ZIM magic bytes test passes |
| 2:30–3:00 | Change 4: Verify _apply_metadata_to_creator() | Metadata readback test passes |
| 3:00–3:30 | Change 5: Install zimcheck, run on test ZIM | zimcheck exit code 0 |
| 3:30–5:00 | Write 12 new integration tests (3 files) | All 12 new tests pass |
| 5:00–6:00 | Manual E2E: generate ZIM, verify offline read | Articles display in kiwix-serve |
| 6:00–6:30 | Remove `_stub_write_placeholder()` method | `100 passed` (88+12) |
| 6:30–7:30 | Alembic migration + ZimExport model | `alembic upgrade head` succeeds |
| 7:30–8:30 | Export API endpoint skeleton | POST /api/exports returns 200 + job_id |
| 8:30–9:30 | Buffer: cleanup, PR prep | PR ready for review |

**Critical path**: Changes 0→1→2→3 are strictly sequential. Change 4 and 5 can proceed in parallel after Change 3. Test authorship (Phase C) can begin in parallel after Change 3.

### 4.3 Parallel opportunities after hour 2:30

Once Change 3 is verified (magic bytes test passes), three tasks can run in parallel:
- **Thread A**: Change 4 verification + metadata readback test
- **Thread B**: Change 5 (zimcheck install + validation)
- **Thread C**: Write 12 new test stubs

Using two Claude sessions in parallel (per the 3.5x throughput memory), hours 2:30–5:00 compress to approximately 1 hour, bringing total implementation time to 7–8 hours.

---

## Section 5: Test Environment Requirements

### 5.1 Docker isolation (optional but recommended)

The existing tests use `tmp_path` fixtures and require no database, no network, and no external services. Docker is optional for isolation but not required. Direct local testing is faster.

If Docker isolation is needed for a clean-room re-verification:

```dockerfile
FROM python:3.11-slim-bookworm

# Install zim-tools for zimcheck
RUN apt-get update && apt-get install -y zim-tools && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv pip install -e ".[dev]"

COPY app/ ./app/
COPY tests/ ./tests/

CMD ["python3", "-m", "pytest", "tests/", "-v", "--tb=short"]
```

Build and run:
```bash
docker build -t open-repo-test -f Dockerfile.test .
docker run --rm open-repo-test
```

The `--rm` flag ensures no container state persists. The test suite completes in under 30 seconds.

### 5.2 New test files required

Three test files do not yet exist. They must be created during Phase C of implementation:

| File | Tests | Dependencies |
|------|-------|-------------|
| `tests/unit/test_zim_writer_libzim.py` | Tests 1-5, 10-12 from roadmap matrix | libzim installed |
| `tests/integration/test_zimcheck_validation.py` | Tests 6-7 from roadmap matrix | libzim + zim-tools installed |
| `tests/integration/test_zim_readback.py` | Tests 8-9 from roadmap matrix | libzim installed |

The existing `tests/integration/test_export_pipeline.py` is unchanged. New tests are additive.

### 5.3 Kiwix compatibility verification

After implementation, verify the generated ZIM opens correctly in at least one Kiwix client:

| Method | Command | Pass criterion |
|--------|---------|---------------|
| kiwix-serve (Docker) | `docker run -v /tmp:/data kiwix/kiwix-serve /data/test.zim` | `curl localhost:8080` returns article HTML |
| Kiwix Android | `adb push /tmp/test.zim /sdcard/` | Articles display; search returns 3+ results |
| libzim reader (Python) | `Archive(path).get_entry_by_path("index")` | Returns HTML bytes matching what was written |

### 5.4 Performance baseline (Raspberry Pi 5)

| Export size | Expected generation time | Thermal note |
|-------------|------------------------|-------------|
| 10 articles | < 1 second | Negligible |
| 100 articles | 2–5 seconds | Monitor CPU temperature |
| 500 articles (nopic) | 15–45 seconds | Schedule at 02:00 UTC (lowest ambient temperature) |
| 1,000 articles | 30–90 seconds | Benchmark first; may need to reduce max_items |

---

## Go / No-Go Summary

| Dimension | Status | Action Required |
|-----------|--------|----------------|
| libzim 3.9.0 installed | GO | None |
| ARM64 wheel available | GO | None |
| Xapian bundled | GO | None |
| 88 tests passing | GO | None |
| Scaffold complete | GO | None |
| config_indexing placement | **MUST FIX** | Use corrected Change 3 pattern (before `with`) |
| pyproject.toml | **MUST FIX** | Add libzim + jinja2 declarations |
| zimcheck binary | CAUTION | `sudo apt install zim-tools` before integration tests |
| Alembic migration | CAUTION | Create after core implementation verified |
| _stub_write_placeholder still active | CAUTION | Will be removed as final step |
| Phase 4 PR gate | CONDITIONAL | Feature branch work can start; must not merge to main before Phase 4 PR #1 |

**Recommendation**: Proceed with Candidate 1 implementation. Use the corrected Change 3 pattern above. Begin with `git checkout -b feature/zimwriter-libzim-integration` (or examine the existing `feature/zimwriter-libzim-activation` branch to determine if it can be recovered).

---

*Audit completed: 2026-05-20*
*Live verification: zim_writer.py read, 10 schema tests executed, libzim API lifecycle tested, fallback PNG dimensions confirmed, pyproject.toml contents inspected*
*All findings based on actual file state on master branch*
