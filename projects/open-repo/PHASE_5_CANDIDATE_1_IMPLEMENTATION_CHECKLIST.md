---
title: "Phase 5 Candidate 1 — ZimWriter Implementation Checklist"
project: open-repo
phase: 5
candidate: 1
document_type: execution-checklist
status: ready-to-execute
date: 2026-05-19
session: 1361
prerequisite: "Phase 4 PR #1 merged (255 tests passing)"
---

# Phase 5 Candidate 1: Step-by-Step Implementation Checklist

**Audience**: The person executing Phase 5 implementation.
**Purpose**: Mechanical execution guide. No design decisions required — all decisions have been made. Follow sequentially unless a parallel opportunity is explicitly noted.
**Total time**: 8–11 hours
**Branch**: `feature/zimwriter-libzim-integration`

---

## Pre-Flight Checklist (Complete Before Starting)

| # | Check | Command | Expected |
|---|-------|---------|----------|
| P1 | Phase 4 PR #1 merged | `git log --oneline -5` | Phase 4 commit visible in history |
| P2 | Working directory clean | `git status` | No uncommitted changes |
| P3 | On correct branch or create one | `git checkout -b feature/zimwriter-libzim-integration` | Branch created |
| P4 | Baseline tests pass | `cd backend && python3 -m pytest tests/integration/test_export_pipeline.py -q` | `84 passed` |
| P5 | Disk space adequate | `df -h /tmp` | At least 5 GB free |

---

## Phase A: Environment Setup (30 minutes)

### Step A1: Install libzim Python wheel

**Duration**: 2 minutes
**Blockers**: None

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
uv pip install "libzim>=3.2,<4.0"
```

**Verify**:
```bash
uv run python3 -c "from libzim.writer import Creator, Item, StringProvider, Hint; import libzim; print('libzim version:', libzim.__version__)"
```
**Expected**: `libzim version: 3.10.0`
**If it fails**: Check `uv pip list | grep libzim`. If not present, run `uv pip install libzim --verbose` to see error.

---

### Step A2: Install zimcheck binary

**Duration**: 3 minutes
**Blockers**: None (can run in parallel with A1)

```bash
sudo apt install zim-tools
```

**Verify**:
```bash
zimcheck --version
```
**Expected**: Version line mentioning 3.1.3 or similar.

---

### Step A3: Update pyproject.toml

**Duration**: 5 minutes
**File**: `backend/pyproject.toml`
**Blockers**: None

Add to `[project.dependencies]` list:
```toml
"libzim>=3.2,<4.0",
"jinja2>=3.1",
```

**Verify**:
```bash
uv pip install -e ".[dev]"
```
**Expected**: No errors; libzim already installed, jinja2 pulled or confirmed present.

---

### Step A4: Confirm baseline still holds

**Duration**: 30 seconds
**Blockers**: A1, A2, A3 complete

```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q
```
**Expected**: `84 passed` — no regressions from environment changes.

---

## Phase B: Core Integration (2.5 hours)

### Step B1: Add libzim import guard

**Duration**: 15 minutes
**File**: `app/services/export/zim_writer.py`
**Location**: After line 49 (`from typing import Optional`)
**Blockers**: A1 (libzim installed)

Insert:
```python
# ---------------------------------------------------------------------------
# libzim integration (optional import guard for environments without wheel)
# ---------------------------------------------------------------------------
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None  # type: ignore[assignment,misc]
```

**Verify**:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q
```
**Expected**: `84 passed` — no regressions. Module still loads even with guard in place.

---

### Step B2: Add _FALLBACK_ILLUSTRATION_PNG constant

**Duration**: 15 minutes
**File**: `app/services/export/zim_writer.py`
**Location**: After the import guard block (before `class ExportScope`)
**Blockers**: B1

Insert:
```python
# Minimal transparent PNG used as fallback ZIM illustration when no branded icon is provided.
# Replace with a real 48x48 open-repo branded PNG before production deployment.
# zimcheck will warn (not fail) on illustration dimensions for this placeholder.
_FALLBACK_ILLUSTRATION_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\x00\x000"
    b"\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x0bIDATx\x9cc"
    b"\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
)
```

**Verify** (validate dimensions — if PIL is available):
```bash
uv run python3 -c "
import io
try:
    from PIL import Image
    img = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x0bIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB\x60\x82'))
    print('Size:', img.size)
except ImportError:
    print('PIL not available — verify manually that bytes are valid PNG')
"
```
**Note**: If dimensions are not 48x48, use a real 48x48 branded PNG bytes instead. zimcheck requires exactly 48x48.

---

### Step B3: Add ArticleItem adapter class

**Duration**: 45 minutes
**File**: `app/services/export/zim_writer.py`
**Location**: After `ZimEntry` dataclass ends (before `class ZimWriter`, around line 408)
**Blockers**: B1 (import guard, so `Item`, `StringProvider`, `Hint` are importable)

Insert the full `ArticleItem` class:

```python
class ArticleItem(Item):  # type: ignore[misc]
    """
    Adapter from ZimEntry to libzim's Item interface.

    libzim.writer.Creator.add_item() requires an Item subclass.
    This class bridges ZimEntry (our data model) to libzim's API.

    Thread safety: Each ArticleItem instance is consumed once by add_item()
    and not retained. Thread-safe as long as the owning ZimWriter is
    called from a single thread (which is enforced by ZimWriter's docs).
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

**Verify**:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q
```
**Expected**: `84 passed`. ArticleItem is not yet exercised by existing tests but must not break anything.

Write a quick sanity test (can be temporary, not committed):
```python
from app.services.export.zim_writer import ZimEntry, ArticleItem
entry = ZimEntry(path="test/item", title="Test Article", content="<html><body><h1>Test</h1></body></html>")
item = ArticleItem(entry)
assert item.get_path() == "test/item"
assert item.get_title() == "Test Article"
assert item.get_mimetype() == "text/html"
print("ArticleItem OK")
```

---

### Step B4: Replace stub in create_zim()

**Duration**: 1 hour
**File**: `app/services/export/zim_writer.py`
**Location**: Around line 762, inside `create_zim()` method
**Blockers**: B1 (import guard), B3 (ArticleItem exists)

Find this block:
```python
        # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
        # See the docstring above for the correct implementation pattern.
        # For now, write a placeholder file to allow test harness to run.
        self._stub_write_placeholder()
```

Replace with:
```python
        if not _LIBZIM_AVAILABLE:
            # Fallback for environments without libzim installed (CI without wheel)
            self._stub_write_placeholder()
        else:
            with Creator(str(self.output_path)) as creator:
                creator.config_indexing(True, self.config.language_iso3)
                creator.set_mainpath("index")
                self._apply_metadata_to_creator(creator)
                for entry in self._entries:
                    creator.add_item(ArticleItem(entry))
            # Creator.__exit__ triggers ZIM file finalization and write to disk
```

**Verify — ZIM magic header test** (run before writing the formal test):
```bash
uv run python3 -c "
import tempfile, os
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

tmp = tempfile.mkdtemp()
meta = ZimMetadata(title='Test Export', description='Test library', language='eng',
    name='open-repo_en_nopic', flavour='nopic', creator='Test', publisher='Test',
    source_url='https://example.org')
config = ExportConfig()
writer = ZimWriter(metadata=meta, config=config, output_path=Path(tmp) / 'test.zim', zimcheck_binary=None)
writer.add_article(path='index', content='<html><body><h1>Home</h1></body></html>', article_type='procedure')
result = writer.create_zim(run_zimcheck=False)
with open(result.output_path, 'rb') as f:
    magic = f.read(4)
print('Magic bytes:', magic.hex())
assert magic == b'\\x5a\\x49\\x4d\\x04', f'Expected ZIM magic, got: {magic.hex()}'
print('ZIM magic OK — real ZIM file written!')
"
```
**Expected**: `ZIM magic OK — real ZIM file written!`

Run existing 84 tests:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q
```
**Expected**: `84 passed`. The stub path is still active for these tests (they pass `zimcheck_binary=None` and the `_LIBZIM_AVAILABLE` guard means stubs still work in environments without libzim — but libzim IS now installed, so the Creator path will run. Verify test output file exists and is a real ZIM.)

---

### Step B5: Implement _apply_metadata_to_creator()

**Duration**: 45 minutes
**File**: `app/services/export/zim_writer.py`
**Location**: Method `_apply_metadata_to_creator()`, around line 870
**Blockers**: B1 (import guard), B4 (Creator context established)

Find the method body which currently contains only `pass` and replace the entire method body with:

```python
    def _apply_metadata_to_creator(self, creator: object) -> None:
        """Apply all ZimMetadata fields to the open libzim Creator instance."""
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
        # Add illustration — required for zimcheck to pass
        illustration_bytes = self._get_illustration_bytes()
        if illustration_bytes:
            creator.add_illustration(48, illustration_bytes)
        else:
            creator.add_illustration(48, _FALLBACK_ILLUSTRATION_PNG)
```

**Verify — metadata readback** (requires libzim reader):
```bash
uv run python3 -c "
import tempfile
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig
from libzim.reader import Archive

tmp = tempfile.mkdtemp()
meta = ZimMetadata(title='Open-Repo Test', description='Offline knowledge library', language='eng',
    name='open-repo_en_nopic', flavour='nopic', creator='Open-Repo Community',
    publisher='Open-Repo', source_url='https://example.org')
config = ExportConfig()
writer = ZimWriter(metadata=meta, config=config, output_path=Path(tmp) / 'test.zim', zimcheck_binary=None)
writer.add_article(path='index', content='<html><body><h1>Home</h1></body></html>', article_type='procedure')
result = writer.create_zim(run_zimcheck=False)

archive = Archive(str(result.output_path))
print('Title:', archive.get_metadata('Title'))
print('Language:', archive.get_metadata('Language'))
print('Creator:', archive.get_metadata('Creator'))
print('Name:', archive.get_metadata('Name'))
assert archive.get_metadata('Title') == 'Open-Repo Test'
assert archive.get_metadata('Language') == 'eng'
print('All metadata fields readable — PASS')
"
```

---

### Step B6: Verify zimcheck on real ZIM

**Duration**: 30 minutes
**Blockers**: B4 and B5 complete (ZIM must be valid binary with metadata)

```bash
uv run python3 -c "
import tempfile
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

tmp = tempfile.mkdtemp()
meta = ZimMetadata(title='Open-Repo Test', description='Offline knowledge library', language='eng',
    name='open-repo_en_nopic', flavour='nopic', creator='Open-Repo Community',
    publisher='Open-Repo', source_url='https://example.org')
config = ExportConfig()
writer = ZimWriter(metadata=meta, config=config, output_path=Path(tmp) / 'test.zim', zimcheck_binary='zimcheck')
for i in range(10):
    writer.add_article(path=f'item/{i:03d}', content=f'<html><head><title>Article {i}</title></head><body><h1>Article {i}</h1><p>Content here.</p></body></html>', article_type='procedure')
writer.add_article(path='index', content='<html><head><title>Home</title></head><body><h1>Open-Repo</h1></body></html>', article_type='procedure')
result = writer.create_zim(run_zimcheck=True)
print('zimcheck passed:', result.zimcheck_passed)
print('File size:', result.file_size_bytes, 'bytes')
print('SHA-256:', result.sha256[:16], '...')
"
```

**Expected**:
```
zimcheck passed: True
File size: [some number > 1024]
SHA-256: [16 hex chars] ...
```

**If zimcheck fails**: Run `zimcheck --verbose {path}` to see specific errors. Common causes:
- Illustration dimensions wrong: verify `_FALLBACK_ILLUSTRATION_PNG` is 48x48
- Description >80 chars: check `ZimMetadata.description` field in test
- Name format invalid: must match `{pub}_{lang}_{flavour}` regex

---

## Phase C: Write 12 New Integration Tests (1.5 hours)

**Blockers**: B4 and B5 complete

Create three new test files:

### Step C1: tests/unit/test_zim_writer_libzim.py

**Duration**: 45 minutes
**Contains**: Tests 1–5, 10–12 from roadmap test matrix

Key tests to implement:

- `test_zim_writer_creates_real_zim_file`: Assert `output.read(4) == b'\x5a\x49\x4d\x04'`
- `test_zim_metadata_all_mandatory_fields`: Use `Archive.get_metadata()` for all fields
- `test_xapian_index_populated`: Use `Archive.search("keyword")` and assert >=1 result
- `test_article_count_matches_database`: Assert article count matches via Archive iteration
- `test_html_no_external_dependencies`: BeautifulSoup scan on all entries for `http://` in src/href
- `test_period_collision_handling`: `ZimWriter.compute_period(["2026-05"], now=datetime(2026, 5, 19)) == "2026-05a"`
- `test_zimwriter_not_reusable_after_finalize`: Second `create_zim()` raises RuntimeError
- `test_nopic_variant_excludes_images`: No entries with `mime_type.startswith("image/")`

### Step C2: tests/integration/test_zimcheck_validation.py

**Duration**: 20 minutes
**Contains**: Tests 6–7 from roadmap

- `test_zimcheck_passes_on_valid_export`: 10-article ZIM, assert `result.zimcheck_passed == True`
- `test_zimcheck_fails_on_corrupted_archive`: Corrupt bytes after write, assert file renamed to `.zim.invalid`

Add `@pytest.mark.integration` to both tests.

### Step C3: tests/integration/test_zim_readback.py

**Duration**: 25 minutes
**Contains**: Tests 8–9 from roadmap

- `test_offline_read_article_by_path`: Write ZIM, read back via `Archive.get_entry_by_path()`, assert content matches
- `test_unicode_content_survives_roundtrip`: Write article with French, Arabic, Spanish chars; read back; assert no replacement characters

Add `@pytest.mark.integration` to both tests.

### Step C4: Run all new tests

```bash
python3 -m pytest tests/ -q
```
**Expected**: `96 passed` (84 existing + 12 new)

---

## Phase D: Manual End-to-End Verification (1 hour)

**Blockers**: All Phase B and C complete

### Step D1: Generate E2E test ZIM

```bash
uv run python3 -c "
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

meta = ZimMetadata(title='Open-Repo E2E Test', description='End-to-end verification export', language='eng',
    name='open-repo_en_nopic', flavour='nopic', creator='Open-Repo Community',
    publisher='Open-Repo', source_url='https://example.org', date='2026-05-19')
config = ExportConfig()
writer = ZimWriter(metadata=meta, config=config, output_path=Path('/tmp/open-repo_e2e_test.zim'))

# Add representative content
writer.add_article(path='index', content='<html><head><title>Open-Repo</title><style>body{font-family:sans-serif;margin:1rem;}</style></head><body><h1>Open-Repo Offline Library</h1><p>Knowledge for offline use.</p></body></html>', article_type='procedure')

domains = ['water', 'agriculture', 'energy', 'recipes', 'building']
for i in range(20):
    domain = domains[i % len(domains)]
    title = f'{domain.title()} Guide {i+1}'
    writer.add_article(path=f'{domain}/item-{i:03d}', content=f'<html><head><title>{title}</title><style>body{{font-family:sans-serif;margin:1rem;}}</style></head><body><h1>{title}</h1><p>Practical guide content for {domain}. Step 1: preparation. Step 2: execution. Step 3: verification.</p></body></html>', article_type='procedure')

result = writer.create_zim()
print('E2E ZIM written:', result.output_path)
print('Articles:', result.article_count)
print('File size:', result.file_size_bytes, 'bytes')
print('zimcheck passed:', result.zimcheck_passed)
print('SHA-256:', result.sha256)
"
```

**Expected output**:
```
E2E ZIM written: /tmp/open-repo_e2e_test.zim
Articles: 21
File size: [> 10000]
zimcheck passed: True
SHA-256: [64 hex chars]
```

### Step D2: Verify in Kiwix (Manual)

Transfer `/tmp/open-repo_e2e_test.zim` to a device with Kiwix installed:

| Platform | Transfer Method | Verify |
|----------|----------------|--------|
| Android (F-Droid Kiwix) | `adb push` or file share | Open library → articles display → search "water" returns results |
| kiwix-serve (if Docker available) | `docker run -v /tmp:/data kiwix/kiwix-serve kiwix-serve /data/open-repo_e2e_test.zim` | `curl localhost:8080` returns HTML |

---

## Phase E: Cleanup and Finalization (1 hour)

### Step E1: Remove _stub_write_placeholder() method

**Duration**: 15 minutes
**File**: `app/services/export/zim_writer.py`
**Location**: Lines 914-931 (the `_stub_write_placeholder` method)

Delete the entire method:
```python
    def _stub_write_placeholder(self) -> None:
        """..."""
        placeholder_content = (
            ...
        ).encode("utf-8")
        self.output_path.write_bytes(placeholder_content)
```

Also remove the `if not _LIBZIM_AVAILABLE: self._stub_write_placeholder()` branch from `create_zim()`. The import guard can remain for now (remove in a follow-up PR after CI confirms libzim is always installed).

**Verify**:
```bash
python3 -m pytest tests/ -q
```
**Expected**: `96 passed`

---

### Step E2: Write Alembic migration for zim_exports table

**Duration**: 30 minutes
**File**: `alembic/versions/{date}_add_zim_exports_table.py`

```bash
cd backend
alembic revision --autogenerate -m "add_zim_exports_table"
```

Review the generated migration. Ensure it contains all columns from the `ZimExport` model (see roadmap for full schema). Apply:

```bash
alembic upgrade head
```

**Verify**:
```bash
alembic current
```
**Expected**: Head revision shows as current.

---

### Step E3: Add ZimExport SQLAlchemy model

**Duration**: 20 minutes
**File**: `app/models.py`

Add `ZimExportStatus` enum and `ZimExport` model class as specified in the roadmap's "SQLAlchemy model" section. Import `ZimExport` in the alembic `env.py` target_metadata so autogenerate can detect future changes.

---

### Step E4: Final test suite run

```bash
python3 -m pytest tests/ -v 2>&1 | tail -20
```
**Expected**: All tests pass. Zero failures.

---

### Step E5: Create PR

```bash
git add app/services/export/zim_writer.py pyproject.toml app/models.py tests/ alembic/
git commit -m "feat(phase-5): activate libzim integration in ZimWriter"
```

PR title: `feat(phase-5): activate libzim integration in ZimWriter`
PR body: Reference roadmap doc, list 5 changes, note test count (84 + 12 = 96), note zimcheck validation passing.

**Gate**: Do not merge to main until Phase 4 PR #1 has landed.

---

## Risk Mitigation Quick Reference

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `ModuleNotFoundError: libzim` | Wheel not installed | `uv pip install "libzim>=3.2,<4.0"` |
| `zimcheck FAILED: illustration` | Fallback PNG wrong dimensions | Replace `_FALLBACK_ILLUSTRATION_PNG` with real 48x48 branded PNG |
| `zimcheck FAILED: Description too long` | Description >80 chars | Edit `ZimMetadata.description` to <=80 chars |
| `zimcheck FAILED: Name invalid` | Name has uppercase or spaces | Verify name matches `{pub}_{lang}_{flavour}` pattern |
| Export OOM killed | Article buffer too large | Reduce `max_items` in ExportConfig for test; add streaming mode in Phase 5.1 |
| Export >60 seconds | Thermal throttling on RPi 5 | Schedule at 02:00 UTC; add CPU governor hint |
| `ZimCheckError` raised | zimcheck exit code != 0 | Run `zimcheck --verbose {file}` for specific error line |
| Magic bytes wrong | Stub path still running | Confirm `_LIBZIM_AVAILABLE == True`; check import guard |

---

## Completion Definition

Phase 5 Candidate 1 is complete when:

- [ ] `uv run pytest tests/ -q` reports `96 passed` (84 + 12)
- [ ] `zimcheck` passes on a 20-article test ZIM (exit code 0)
- [ ] ZIM opens in Kiwix Android (F-Droid) or kiwix-serve — articles display
- [ ] `sha256sum -c {file}.sha256` passes
- [ ] `alembic upgrade head` applied cleanly
- [ ] PR created, linked to Phase 4 PR #1 as dependency
- [ ] `_stub_write_placeholder()` method deleted from codebase
