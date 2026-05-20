---
title: "Phase 5 Candidate 1: ZimWriter libzim Integration — Implementation Checklist"
project: open-repo
phase: 5
candidate: 1
document_type: execution-checklist
status: ready-to-execute
date: 2026-05-20
total_effort: "0.5–1h (Path A: merge feature branch) or 8–11h (Path B: from scratch)"
---

# Phase 5 Candidate 1: Implementation Checklist
## Hour-by-Hour Breakdown for ZimWriter libzim Integration

**Situation**: The implementation is complete on `feature/zimwriter-libzim-activation` (commit `ec0ff7be`). Two paths are available:

- **Path A (Recommended)**: Merge the feature branch. Total time: 0.5–1 hour.
- **Path B**: Implement from scratch using the roadmap. Total time: 8–11 hours.

---

## Pre-Flight Verification (Both Paths — 10 minutes)

Complete all checks before starting.

| # | Check | Command | Expected |
|---|-------|---------|----------|
| PF1 | Python version | `python3 --version` | `Python 3.11.x` |
| PF2 | Architecture | `uname -m` | `aarch64` |
| PF3 | Working directory | `git status` | On `master`, clean |
| PF4 | Baseline tests pass | `cd projects/open-repo/backend && python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no` | `84 passed` |
| PF5 | Feature branch exists | `git branch -a \| grep zimwriter` | Shows `feature/zimwriter-libzim-activation` |
| PF6 | Disk space | `df -h /tmp` | At least 2 GB free |
| PF7 | Network (libzim install) | `curl -s https://pypi.org/pypi/libzim/json \| python3 -c "import json,sys; d=json.load(sys.stdin); print(d['info']['version'])"` | `3.10.0` |

**BLOCKER**: If PF4 fails (not 84 passed), stop. Do not proceed until baseline is restored.

---

## Path A: Merge Feature Branch (Recommended — 0.5–1 hour)

### A.1 Environment Setup
**Duration**: 15 minutes  
**Blocker for**: Everything else in Path A.

#### A.1.1 Install libzim wheel
**Time**: 2–3 minutes

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
uv pip install "libzim>=3.2,<4.0"
```

Verify immediately:
```bash
uv run python3 -c "
from libzim.writer import Creator, Item, StringProvider, Hint
import libzim
print('libzim version:', libzim.__version__)
print('Creator:', Creator)
print('All imports OK')
"
```

Expected output:
```
libzim version: 3.10.0
Creator: <class 'libzim.writer.Creator'>
All imports OK
```

**If install fails**: Run `uv pip install libzim --verbose` to see the error. If "no matching distribution," verify Python 3.11 and aarch64 with `python3 --version && uname -m`. The wheel `libzim-3.10.0-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl` should resolve. If behind a proxy, set `UV_HTTP_TIMEOUT=120`.

#### A.1.2 Install zimcheck binary
**Time**: 2–3 minutes  
**Parallel with A.1.1**: Yes, run in a second terminal.

```bash
sudo apt-get install -y zim-tools
```

Verify:
```bash
which zimcheck && zimcheck --version
```

Expected: Path printed (e.g., `/usr/bin/zimcheck`), version `3.1.3` or similar.

**If apt fails**: Download static binary from `https://github.com/openzim/zim-tools/releases`, extract to `/usr/local/bin/zimcheck`, and `chmod +x`.

---

### A.2 Merge Feature Branch
**Duration**: 5–10 minutes  
**Blocker for**: A.3 onward.

```bash
cd /home/awank/dev/SuperClaude_Framework
git checkout master
git merge feature/zimwriter-libzim-activation --no-ff -m "feat(phase-5): activate libzim integration in ZimWriter"
```

**If merge conflicts appear**: The feature branch diverged from master at commit `ec0ff7be`. Conflicts most likely in:
1. `projects/open-repo/backend/pyproject.toml` — accept the feature branch version (adds `"libzim>=3.2,<4.0"`)
2. `projects/open-repo/backend/app/services/export/zim_writer.py` — accept the feature branch version (adds import guard, ArticleItem, real create_zim() path, metadata implementation)

Resolve and then:
```bash
git add projects/open-repo/backend/pyproject.toml
git add projects/open-repo/backend/app/services/export/zim_writer.py
git add projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py
git merge --continue
```

---

### A.3 Validate Against Real libzim
**Duration**: 5 minutes  
**Blocker**: A.1.1 (libzim installed).

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=short
```

Expected: `84 passed` (identical to pre-merge baseline — tests run in stub mode because test fixtures pass `zimcheck_binary=None` and libzim generates a real ZIM but tests only verify interface contracts).

**If any test fails**: Stop. Do not proceed. Investigate the failure — it indicates a merge conflict was resolved incorrectly or a new incompatibility was introduced.

---

### A.4 Smoke Test — Real ZIM File
**Duration**: 5 minutes  
**Blocker**: A.1.1 (libzim installed), A.2 (feature branch merged).

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

uv run python3 -c "
from pathlib import Path
from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ExportScope
)

metadata = ZimMetadata(
    title='Open-Repo Test',
    description='Smoke test export',
    language='eng',
    name='open-repo_en_nopic',
    flavour='nopic',
    creator='Open-Repo Community',
    publisher='Open-Repo',
    source_url='https://test.example.org',
)
config = ExportConfig(
    scope=ExportScope.LOCAL_ONLY,
    flavour='nopic',
    include_images=False,
    language='en',
    language_iso3='eng',
)
writer = ZimWriter(
    metadata=metadata,
    config=config,
    output_path=Path('/tmp/smoke-test.zim'),
    zimcheck_binary=None,
)
writer.add_article(
    path='index',
    content='<html><body><h1>Smoke Test</h1><p>Real ZIM output.</p></body></html>',
    article_type='procedure',
)
result = writer.create_zim(run_zimcheck=False)
print('Output path:', result.output_path)
print('File size:', result.file_size_bytes, 'bytes')
print('SHA-256:', result.sha256)
print('Article count:', result.article_count)
print()
magic = open('/tmp/smoke-test.zim', 'rb').read(4)
print('ZIM magic bytes:', magic.hex())
assert magic == b'\x5a\x49\x4d\x04', f'FAIL: bad magic {magic!r}'
print('ZIM magic header: PASS')
"
```

Expected output:
```
Output path: /tmp/smoke-test.zim
File size: [>1024] bytes
SHA-256: [64 hex chars]
Article count: 1
ZIM magic bytes: 5a494d04
ZIM magic header: PASS
```

**Blocker if smoke test fails**: The `_LIBZIM_AVAILABLE` flag may be `False` despite installation. Check with `uv run python3 -c "from libzim.writer import Creator; print('OK')"`. If this fails, libzim is not in the UV venv — run `uv pip install "libzim>=3.2,<4.0"` again inside the backend directory.

---

### A.5 zimcheck Validation
**Duration**: 3 minutes  
**Blocker**: A.1.2 (zimcheck installed), A.4 (real ZIM file produced).

```bash
zimcheck /tmp/smoke-test.zim
echo "zimcheck exit code: $?"
```

Expected: Output with no `ERROR` lines; exit code 0. Possible warnings about illustration size or title length are acceptable — they do not indicate failure.

**If zimcheck fails**: Common causes and fixes:
- `Description` metadata > 80 chars: `ZimMetadata.validate()` enforces this at Python level; should not occur
- Missing illustration: `_FALLBACK_ILLUSTRATION_PNG` is always set; should not occur
- Title > 30 chars: zimcheck warning only (not failure) in version 3.1.3
- Name format invalid: Must match `[a-z0-9-]+_[a-z]{2,3}_[a-z0-9-]+` pattern; enforced at Python level

Run `zimcheck /tmp/smoke-test.zim --verbose` for detailed error output.

---

### A.6 Apply Alembic Migration
**Duration**: 5 minutes  
**Blocker**: Requires running PostgreSQL instance.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
alembic upgrade head
```

Expected:
```
INFO  [alembic.runtime.migration] Running upgrade 002 -> 003, Add zim_exports table for Phase 5
```

Verify migration applied:
```bash
alembic current
# Expected: 003 (head)
```

**If database is not available**: This step can be deferred. The zim_writer.py changes and smoke test above work without the database migration. Apply migration when the database instance is accessible.

---

### A.7 Optional — Kiwix Device Test
**Duration**: 15–30 minutes (optional but strongly recommended before declaring production-ready)

```bash
# Transfer ZIM to an Android device or open on desktop
# Option A: Kiwix Desktop (Linux)
apt-get install -y kiwix-tools
kiwix-serve /tmp/smoke-test.zim --port 8080
# Open http://localhost:8080 in browser

# Option B: Transfer to Android
adb push /tmp/smoke-test.zim /sdcard/Download/
# Open Kiwix app on device, add library → navigate to /sdcard/Download/smoke-test.zim
```

Verify:
- Article displays with correct title ("Smoke Test")
- HTML renders without broken styles
- (Xapian search not expected to work until Phase 5.2 adds `config_indexing()` call)

---

### Path A Summary

| Step | Duration | Blocker? | Gate Condition |
|------|----------|----------|----------------|
| A.1.1 Install libzim wheel | 2–3 min | Yes (for A.4) | `from libzim.writer import Creator` succeeds |
| A.1.2 Install zimcheck | 2–3 min | No (for tests) | `zimcheck --version` prints version |
| A.2 Merge feature branch | 5–10 min | Yes (for A.3) | No conflicts, clean merge |
| A.3 Validate 84 tests | 5 min | Yes (stop if fail) | `84 passed` |
| A.4 Smoke test ZIM | 5 min | Yes (stop if fail) | ZIM magic header `5a494d04` |
| A.5 zimcheck validation | 3 min | Recommended | Exit code 0, no ERROR lines |
| A.6 Alembic migration | 5 min | Deferred OK | `alembic current` shows `003` |
| A.7 Kiwix device test | 15–30 min | Optional | Articles display correctly |
| **Total Path A** | **0.5–1h** | | All gate conditions met |

---

## Path B: From-Scratch Implementation (8–11 hours)

Use Path B only if the feature branch is unavailable or has been abandoned.

### B.0 — Setup and Branch Creation (30 minutes)
**Duration**: 30 minutes

```bash
# Create feature branch
git checkout -b feature/zimwriter-libzim-integration

# Install libzim
cd projects/open-repo/backend
uv pip install "libzim>=3.2,<4.0"

# Install zimcheck
sudo apt-get install -y zim-tools

# Verify baseline
python3 -m pytest tests/integration/test_export_pipeline.py -q
# Expected: 84 passed
```

Gate: `from libzim.writer import Creator, Item, StringProvider, Hint` succeeds.

---

### B.1 — Add libzim Import Guard (15 minutes)
**Duration**: 15 minutes  
**File**: `app/services/export/zim_writer.py`  
**Location**: After line 49 (`from typing import Optional`)

Add import guard immediately after the standard library imports:

```python
# TRY-EXCEPT import guard for libzim
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None  # type: ignore[assignment,misc]
    Item = object   # type: ignore[assignment,misc]
    StringProvider = None  # type: ignore[assignment,misc]
    Hint = None  # type: ignore[assignment,misc]

# Fallback 48x48 transparent PNG for ZIM illustration
_FALLBACK_ILLUSTRATION_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\x00\x000"
    b"\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x0bIDATx\x9cc"
    b"\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
)
```

Gate: `python3 -m pytest tests/integration/test_export_pipeline.py -q` still shows `84 passed`.

---

### B.2 — Add ArticleItem Adapter Class (45 minutes)
**Duration**: 45 minutes  
**File**: `app/services/export/zim_writer.py`  
**Location**: New class, after the `ZimEntry` dataclass (before the `ZimWriter` class)

```python
# ---------------------------------------------------------------------------
# libzim adapter class
# ---------------------------------------------------------------------------


class ArticleItem(Item):
    """
    Adapter from ZimEntry to libzim's Item interface.

    libzim.writer.Creator.add_item() requires an Item subclass.
    This class bridges ZimEntry (our data model) to libzim's API.

    Thread safety: Each ArticleItem instance is consumed once by add_item()
    and not retained. Thread-safe as long as the owning ZimWriter is called
    from a single thread (enforced by ZimWriter's design).
    """

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

Gate: Unit test that constructs `ArticleItem(entry)` and asserts all 5 methods return correct values (see test sketch below).

```python
# Quick sanity test — run manually before continuing:
uv run python3 -c "
from app.services.export.zim_writer import ZimEntry, ArticleItem
entry = ZimEntry(
    path='test/article',
    title='Test Article',
    content='<h1>Test</h1>',
    mime_type='text/html; charset=utf-8',
    is_front_article=True,
)
item = ArticleItem(entry)
assert item.get_path() == 'test/article'
assert item.get_title() == 'Test Article'
assert item.get_mimetype() == 'text/html; charset=utf-8'
print('ArticleItem: PASS')
"
```

---

### B.3 — Replace Stub in create_zim() (1 hour)
**Duration**: 1 hour  
**File**: `app/services/export/zim_writer.py`  
**Location**: Around line 759–762

Find the stub call:
```python
# TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
# See the docstring above for the correct implementation pattern.
# For now, write a placeholder file to allow test harness to run.
self._stub_write_placeholder()
```

Replace with:
```python
if not _LIBZIM_AVAILABLE:
    # Fallback stub for environments without libzim installed (dev/CI without wheel)
    placeholder_content = (
        f"STUB ZIM PLACEHOLDER\n"
        f"name={self.metadata.name}\n"
        f"articles={self._article_count}\n"
        f"resources={self._resource_count}\n"
        f"generated_at={datetime.utcnow().isoformat()}\n"
    ).encode("utf-8")
    self.output_path.write_bytes(placeholder_content)
else:
    # Use real libzim Creator for ZIM file generation
    with Creator(str(self.output_path)) as creator:
        creator.config_indexing(True, self.config.language_iso3)  # Enable Xapian FTS
        creator.set_mainpath("index")
        self._apply_metadata_to_creator(creator)
        for entry in self._entries:
            creator.add_item(ArticleItem(entry))
    # Creator.__exit__ triggers ZIM file finalization and write
```

Note: This adds `creator.config_indexing()` which the feature branch omits. Including it here enables Xapian FTS from the start.

Gate: ZIM magic bytes test:
```bash
uv run python3 -c "
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope
metadata = ZimMetadata(title='Test', description='Test', language='eng',
    name='test_en_nopic', flavour='nopic', creator='Test', publisher='Test',
    source_url='https://example.org')
config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour='nopic',
    include_images=False, language='en', language_iso3='eng')
writer = ZimWriter(metadata=metadata, config=config,
    output_path=Path('/tmp/b3-test.zim'), zimcheck_binary=None)
writer.add_article(path='index', content='<h1>Test</h1>', article_type='procedure')
result = writer.create_zim(run_zimcheck=False)
magic = open('/tmp/b3-test.zim', 'rb').read(4)
assert magic == b'\x5a\x49\x4d\x04', f'FAIL: {magic!r}'
print('ZIM magic header: PASS; size', result.file_size_bytes, 'bytes')
"
```

---

### B.4 — Implement _apply_metadata_to_creator() (45 minutes)
**Duration**: 45 minutes  
**File**: `app/services/export/zim_writer.py`  
**Location**: `_apply_metadata_to_creator()` method (currently `pass`)

Replace the `pass` body with:

```python
    def _apply_metadata_to_creator(self, creator: object) -> None:
        """Apply all ZimMetadata fields to a python-libzim Creator instance."""
        creator.add_metadata("Title", self.metadata.title)
        creator.add_metadata("Description", self.metadata.description)
        creator.add_metadata("Language", self.metadata.language)
        creator.add_metadata("Creator", self.metadata.creator)
        creator.add_metadata("Publisher", self.metadata.publisher)
        creator.add_metadata("Date", self.metadata.date)
        creator.add_metadata("Name", self.metadata.name)
        creator.add_metadata("Flavour", self.metadata.flavour)
        creator.add_metadata("Tags", self.metadata.tags)
        creator.add_metadata("Source", self.metadata.source_url)
        creator.add_metadata("Scraper", self.metadata.scraper)
        if self.metadata.long_description:
            creator.add_metadata("LongDescription", self.metadata.long_description)
        illustration_bytes = self._get_illustration_bytes()
        if illustration_bytes:
            creator.add_illustration(48, illustration_bytes)
        else:
            creator.add_illustration(48, _FALLBACK_ILLUSTRATION_PNG)
```

Gate: Use `libzim.reader.Archive` to verify metadata roundtrip:
```bash
uv run python3 -c "
# Re-use /tmp/b3-test.zim from B.3 (or regenerate)
from libzim.reader import Archive
a = Archive('/tmp/b3-test.zim')
print('Title:', a.get_metadata('Title'))
print('Description:', a.get_metadata('Description'))
print('Language:', a.get_metadata('Language'))
# If these print correct values, metadata integration is working
"
```

---

### B.5 — pyproject.toml Update (10 minutes)
**Duration**: 10 minutes  
**File**: `pyproject.toml`

Add under `[project.dependencies]`:
```toml
"libzim>=3.2,<4.0",
```

Gate: `uv pip install -e .` resolves without conflicts.

---

### B.6 — Run Full 84-Test Suite (15 minutes)
**Duration**: 15 minutes

```bash
python3 -m pytest tests/integration/test_export_pipeline.py -v --tb=short
```

Expected: `84 passed` (tests run in stub-or-real mode; all should pass because tests do not check ZIM binary format).

**Blocker**: Any failure here blocks all subsequent steps.

---

### B.7 — zimcheck Integration Test (30 minutes)
**Duration**: 30 minutes

```bash
# Generate a 10-article test export
uv run python3 -c "
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

metadata = ZimMetadata(
    title='Open-Repo Full Test',
    description='zimcheck validation',
    language='eng',
    name='open-repo_en_nopic',
    flavour='nopic',
    creator='Open-Repo Community',
    publisher='Open-Repo',
    source_url='https://test.open-repo.example.org',
)
config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour='nopic',
    include_images=False, language='en', language_iso3='eng')
writer = ZimWriter(metadata=metadata, config=config,
    output_path=Path('/tmp/b7-test.zim'),
    zimcheck_binary='/usr/bin/zimcheck')

# Add index + 9 articles
writer.add_article(path='index', content='<html><body><h1>Library</h1></body></html>', article_type='procedure')
for i in range(9):
    writer.add_article(
        path=f'agriculture/article-{i:02d}',
        content=f'<html><body><h1>Article {i}</h1><p>Content of article {i}.</p></body></html>',
        article_type='procedure',
    )

result = writer.create_zim(run_zimcheck=True)
print('zimcheck_passed:', result.zimcheck_passed)
print('Article count:', result.article_count)
"
```

Expected: `zimcheck_passed: True`.

**If zimcheck fails**: Run `zimcheck /tmp/b7-test.zim --verbose` to get specific error messages. Common fixes listed in Section A.5 above.

---

### B.8 — Alembic Migration (1 hour)
**Duration**: 1 hour  
**File**: `alembic/versions/003_add_zim_exports_table.py`

Create the migration file (copy from `PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md`, Section "Database Schema"). Full schema: 22 columns, 2 custom indexes.

Apply:
```bash
alembic upgrade head
alembic current  # Expected: 003 (head)
```

---

### B.9 — Write 12 New Integration Tests (1.5 hours)
**Duration**: 1.5 hours

Create two new test files (see roadmap Section "Test Matrix" for 12 test IDs):

- `tests/unit/test_zim_writer_real.py` — Tests 1-5, 11-12 (no subprocess, verify ZIM binary)
- `tests/integration/test_zimcheck_validation.py` — Tests 6-7 (requires zimcheck)
- `tests/integration/test_zim_readback.py` — Tests 8-9 (uses libzim.reader.Archive)

Gate: All 12 new tests pass alongside the original 84.

---

### B.10 — Remove Stub Method (15 minutes)
**Duration**: 15 minutes  
**File**: `app/services/export/zim_writer.py`

Delete `_stub_write_placeholder()` method entirely (approximately lines 914–931). Re-run full test suite to confirm nothing breaks:

```bash
python3 -m pytest tests/ -k "export or zim" -v
```

Gate: All tests pass; no stub references remain.

---

### B.11 — Manual End-to-End Test (30 minutes)
**Duration**: 30 minutes (required before PR)

```bash
# Generate a realistic 50-article export from test data
# Transfer to Kiwix Desktop or Android (see A.7 above)
```

Verify:
- Articles display correctly
- Navigation works
- In-app search returns results (requires Xapian FTS enabled via `config_indexing()`)

---

### B.12 — Commit and PR (30 minutes)
**Duration**: 30 minutes

```bash
git add projects/open-repo/backend/app/services/export/zim_writer.py
git add projects/open-repo/backend/pyproject.toml
git add projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py
git add projects/open-repo/backend/tests/unit/test_zim_writer_real.py
git add projects/open-repo/backend/tests/integration/test_zimcheck_validation.py
git add projects/open-repo/backend/tests/integration/test_zim_readback.py

git commit -m "feat(phase-5): activate libzim integration in ZimWriter

- Replace stub _stub_write_placeholder() with real Creator context manager
- Add ArticleItem adapter class (ZimEntry -> libzim.writer.Item)
- Implement _apply_metadata_to_creator() with all 11 ZIM metadata fields
- Add Alembic migration 003: zim_exports table (22 columns, 3 indexes)
- Add libzim>=3.2,<4.0 to pyproject.toml dependencies
- Import guard preserves test compatibility without libzim installed
- Enable Xapian FTS via creator.config_indexing()

All 84 existing tests pass. 12 new integration tests added."
```

---

### Path B Summary

| Step | Duration | Blocker? | Gate |
|------|----------|----------|------|
| B.0 Setup, branch, install | 30 min | Yes | 84 tests pass; libzim imports OK |
| B.1 Import guard + fallback PNG | 15 min | Yes (for B.2) | 84 tests still pass |
| B.2 ArticleItem class | 45 min | Yes (for B.3) | get_path/title/etc. return correct values |
| B.3 create_zim() integration | 1 hr | Yes (for B.4) | ZIM magic header `5a494d04` |
| B.4 _apply_metadata_to_creator() | 45 min | Yes (for B.7) | Metadata roundtrip via Archive |
| B.5 pyproject.toml update | 10 min | No | `uv pip install -e .` resolves |
| B.6 Full 84-test suite | 15 min | Yes (stop if fail) | `84 passed` |
| B.7 zimcheck integration test | 30 min | Recommended | zimcheck_passed=True |
| B.8 Alembic migration | 1 hr | Deferred OK | `alembic current` = 003 |
| B.9 12 new integration tests | 1.5 hr | Recommended | All 12 pass |
| B.10 Remove stub method | 15 min | Yes | All tests pass post-deletion |
| B.11 Manual E2E test | 30 min | Recommended | Articles display in Kiwix |
| B.12 Commit and PR | 30 min | | PR ready for review |
| **Total Path B** | **8–11 hr** | | All gate conditions met |

---

## Docker Test Environment (Optional — Isolated Testing)

Use this to validate ZIM output in a clean environment separate from the host system.

```dockerfile
# File: projects/open-repo/docker/zim-test.Dockerfile
FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y \
    zim-tools \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY projects/open-repo/backend/pyproject.toml .
COPY projects/open-repo/backend/app/ ./app/
COPY projects/open-repo/backend/tests/ ./tests/

RUN pip install -e ".[dev]" && \
    pip install "libzim>=3.2,<4.0"

CMD ["python3", "-m", "pytest", "tests/integration/test_export_pipeline.py", "-v"]
```

Build and run:
```bash
docker build -t open-repo-zim-test -f projects/open-repo/docker/zim-test.Dockerfile .
docker run --rm open-repo-zim-test
```

Expected: `84 passed` inside the container.

For generating and validating a real ZIM inside the container:
```bash
docker run --rm \
  -v /tmp/zim-output:/output \
  open-repo-zim-test \
  python3 -c "
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope
# ... same smoke test as A.4 above, output to /output/smoke-test.zim
"
zimcheck /tmp/zim-output/smoke-test.zim
```

---

## Flags and Known Issues

### Issue 1: Xapian FTS Omitted in Feature Branch

The feature branch `ec0ff7be` does NOT call `creator.config_indexing()` in the production `else` block, even though the docstring shows it as part of the correct pattern. ZIM archives produced by the feature branch will not have in-app search.

**For Path A users**: Add one line after merge:

In `create_zim()`, inside the `with Creator(...) as creator:` block, add:
```python
creator.config_indexing(True, self.config.language_iso3)
```
immediately before `creator.set_mainpath("index")`.

**For Path B users**: B.3 above already includes this line.

### Issue 2: Export API Endpoint Absent

No HTTP endpoint exists to trigger ZIM generation. Phase 5 MVP works via direct Python calls or an APScheduler job. The export API endpoint (`POST /api/v1/exports`) is Phase 5.2 scope. Document this in the PR description.

### Issue 3: Database Required for Alembic Migration

Steps A.6 and B.8 require a running PostgreSQL instance. If unavailable, defer migration. The ZimWriter code and tests work without the DB migration; the migration is only needed to persist `ZimWriteResult` data in production.

---

## Definition of Done

Before declaring Phase 5.1 complete, all of these must be checked:

- [ ] All 84 existing tests pass with real libzim installed (`84 passed`)
- [ ] ZIM magic header verified (`5a494d04`)
- [ ] zimcheck passes on a 10-article test export (exit code 0)
- [ ] `alembic upgrade head` applies migration 003 cleanly
- [ ] ZIM archive opens in Kiwix (Desktop or Android)
- [ ] SHA-256 checksum sidecar file produces correct verification (`sha256sum -c`)
- [ ] No `0.0.0.0` bindings introduced (per CLAUDE.md absolute rule)
- [ ] PR does not merge until Phase 4 PR #1 is merged to main (dependency gate)
- [ ] Phase 5.2 items documented in PR description: Xapian FTS, branded PNG, export API
- [ ] `_stub_write_placeholder()` method removed after all tests confirmed passing (Path B only)

---

## Sources

- [python-libzim ReadTheDocs](https://python-libzim.readthedocs.io/en/latest/)
- [python-libzim PyPI](https://pypi.org/project/libzim/)
- [openZIM Metadata specification](https://wiki.openzim.org/wiki/Metadata)
- [openZIM ZIM file format](https://wiki.openzim.org/wiki/ZIM_file_format)
- [zim-tools releases](https://github.com/openzim/zim-tools/releases)
- [Kiwix OPDS documentation](https://wiki.kiwix.org/wiki/OPDS)
