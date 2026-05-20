---
title: "Phase 5 Candidate 1 — Implementation Checklist (v2, Corrected)"
project: open-repo
phase: 5
candidate: 1
document_type: execution-checklist
status: ready-to-execute
date: 2026-05-20
session: 1435
prerequisite: "Phase 4 PR #1 merged; user approval of Phase 5"
correction: "Fixes config_indexing placement bug from roadmap v1"
---

# Phase 5 Candidate 1: Step-by-Step Implementation Checklist (v2)

**Audience**: The agent or developer executing Phase 5 implementation.
**Purpose**: Mechanical execution guide. Follow sequentially. No design decisions required.
**Total time**: 8–10 hours
**Branch**: `feature/zimwriter-libzim-integration`
**Key correction from v1**: Change 3 uses corrected `config_indexing()` placement (before `with` context, not inside it).

---

## Pre-Flight Checks

| # | Check | Command | Expected |
|---|-------|---------|----------|
| P1 | Phase 4 PR #1 merged | `git log --oneline -5` | Phase 4 commit in history |
| P2 | Working directory clean | `git status` | No uncommitted changes |
| P3 | Create feature branch | `git checkout -b feature/zimwriter-libzim-integration` | Branch created |
| P4 | Baseline tests pass | `cd backend && python3 -m pytest tests/integration/test_export_pipeline.py -q` | `88 passed` |
| P5 | libzim importable | `cd backend && uv run python3 -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('OK')"` | `OK` |
| P6 | Disk space | `df -h /tmp` | At least 5 GB free |

**Note**: If P5 fails, run `uv pip install "libzim>=3.2,<4.0"` before proceeding.

---

## Phase A: Environment Setup (20 minutes)

### Step A1: Declare dependencies in pyproject.toml

**Duration**: 5 minutes
**File**: `backend/pyproject.toml`
**Blocker**: None

Add to `[project.dependencies]`:
```toml
"libzim>=3.2,<4.0",
"jinja2>=3.1",
```

**Verify**:
```bash
cd backend
uv pip install -e ".[dev]"
```
Expected: No errors. Both packages resolve without conflict.

---

### Step A2: Install zimcheck binary

**Duration**: 3 minutes
**Blocker**: None (run in parallel with A1)

```bash
sudo apt install zim-tools
```

**Verify**:
```bash
zimcheck --version
```
Expected: Output contains `3.1.3` or similar version string.

If unavailable: continue without zimcheck. Integration tests that require it are marked `@pytest.mark.integration` and can be deferred. The core implementation (Changes 1–4) does not require zimcheck.

---

### Step A3: Confirm baseline

**Duration**: 30 seconds

```bash
cd backend
python3 -m pytest tests/integration/test_export_pipeline.py -q
```
Expected: `88 passed` — no regressions from environment changes.

---

## Phase B: Core Implementation (3–4 hours)

### Step B1: Add libzim import guard

**Duration**: 15 minutes
**File**: `backend/app/services/export/zim_writer.py`
**Location**: After line 50 (`from typing import Optional`)
**Blocker**: A1 complete

Insert exactly:
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
    Item = object  # type: ignore[assignment,misc]
    StringProvider = None  # type: ignore[assignment,misc]
    Hint = None  # type: ignore[assignment,misc]
```

**Verify**:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q
```
Expected: `88 passed`. Module must load without error.

---

### Step B2: Add ArticleItem adapter class

**Duration**: 45 minutes
**File**: `backend/app/services/export/zim_writer.py`
**Location**: After the `ZimEntry` dataclass ends (around line 406), before the `# Main ZimWriter class` comment
**Blocker**: B1 complete

Insert:
```python
class ArticleItem(Item):  # type: ignore[misc]
    """
    Adapter from ZimEntry to libzim's Item interface.

    libzim.writer.Creator.add_item() requires an Item subclass.
    This class bridges ZimEntry (our data model) to libzim's API.

    Thread safety: Each instance consumed once by Creator.add_item() and
    not retained. Thread-safe as long as the owning ZimWriter is called
    from a single thread (which is enforced by ZimWriter's docs).
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

**Quick sanity test** (temporary, not committed):
```bash
uv run python3 -c "
import sys; sys.path.insert(0, 'backend')
from app.services.export.zim_writer import ZimEntry, ArticleItem
e = ZimEntry(path='test/item', title='Test Article', content='<html><body>Test</body></html>')
item = ArticleItem(e)
assert item.get_path() == 'test/item'
assert item.get_title() == 'Test Article'
assert item.get_mimetype() == 'text/html'
print('ArticleItem OK')
"
```

**Verify**:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q
```
Expected: `88 passed`. ArticleItem not yet exercised but must not break anything.

---

### Step B3: Replace stub in create_zim() — CORRECTED API

**Duration**: 1 hour
**File**: `backend/app/services/export/zim_writer.py`
**Location**: Around line 762
**Blocker**: B1 (import guard), B2 (ArticleItem exists)

**WARNING — API BUG IN ORIGINAL ROADMAP**: The original roadmap shows `creator.config_indexing()` inside the `with Creator(...) as creator:` block. This raises `RuntimeError: Creator started`. The corrected pattern below must be used instead.

Find this block (lines 762–765):
```python
        # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
        # See the docstring above for the correct implementation pattern.
        # For now, write a placeholder file to allow test harness to run.
        self._stub_write_placeholder()
```

Replace with:
```python
        if not _LIBZIM_AVAILABLE:
            # Fallback for environments without libzim installed
            self._stub_write_placeholder()
        else:
            # config_indexing() MUST be called before entering the Creator context.
            # Calling it inside the 'with' block raises RuntimeError: Creator started.
            creator = Creator(str(self.output_path))
            creator.config_indexing(True, self.config.language_iso3)
            creator.set_mainpath("index")
            with creator:
                self._apply_metadata_to_creator(creator)
                for entry in self._entries:
                    creator.add_item(ArticleItem(entry))
            # Creator.__exit__ triggers ZIM file finalization and write to disk
```

Also update the docstring on the method (around line 735). Change the code example from:
```python
# OLD (incorrect — raises RuntimeError):
with Creator(str(self.output_path)) as creator:
    creator.config_indexing(True, self.config.language_iso3)
```
To:
```python
# CORRECT: config_indexing before __enter__
creator = Creator(str(self.output_path))
creator.config_indexing(True, self.config.language_iso3)
creator.set_mainpath("index")
with creator:
    self._apply_metadata_to_creator(creator)
    for entry in self._entries:
        creator.add_item(ArticleItem(entry))
```

**Verify — ZIM magic bytes**:
```bash
uv run python3 -c "
import tempfile, sys
sys.path.insert(0, 'backend')
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
print('Magic:', magic.hex())
assert magic == b'\x5a\x49\x4d\x04', f'Expected ZIM magic, got: {magic.hex()}'
print('Real ZIM file written!')
print('File size:', result.file_size_bytes, 'bytes')
"
```
Expected: `Real ZIM file written!` and `File size: > 1000`

**Run existing tests** (critical regression check):
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q
```
Expected: `88 passed`. The stub path remains active for tests that do not install libzim, but since libzim IS now installed, the Creator path runs.

---

### Step B4: Verify _apply_metadata_to_creator()

**Duration**: 30 minutes
**File**: `backend/app/services/export/zim_writer.py`
**Location**: Method body around line 873
**Blocker**: B3 complete

Review the existing method body. It contains a try/except AttributeError guard wrapping the metadata calls. Confirm all 11 required fields plus illustration are present:

Required calls:
```python
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
# Optional:
if self.metadata.long_description:
    creator.add_metadata("LongDescription", self.metadata.long_description)
# Illustration:
creator.add_illustration(48, illustration_bytes)  # or fallback PNG
```

If the `try: ... except AttributeError: pass` guard is present, remove it — it silently swallows real errors in production. Replace with a direct implementation (no guard needed when libzim is properly installed).

**Verify — metadata readback**:
```bash
uv run python3 -c "
import tempfile, sys
sys.path.insert(0, 'backend')
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig
from libzim import Archive

tmp = tempfile.mkdtemp()
m = ZimMetadata(title='Open-Repo Test', description='Offline knowledge library', language='eng',
    name='open-repo_en_nopic', flavour='nopic', creator='Open-Repo Community',
    publisher='Open-Repo', source_url='https://example.org')
writer = ZimWriter(metadata=m, config=ExportConfig(), output_path=Path(tmp)/'t.zim', zimcheck_binary=None)
writer.add_article(path='index', content='<html><body><h1>Open-Repo</h1></body></html>', article_type='procedure')
result = writer.create_zim(run_zimcheck=False)

archive = Archive(str(result.output_path))
title = archive.get_metadata('Title')
lang = archive.get_metadata('Language')
print('Title:', title)
print('Language:', lang)
assert title == b'Open-Repo Test', f'Wrong title: {title}'
assert lang == b'eng', f'Wrong language: {lang}'
print('Metadata readback PASS')
"
```

---

### Step B5: zimcheck validation

**Duration**: 30 minutes
**Blocker**: B3 and B4 complete; A2 (zimcheck installed)

```bash
uv run python3 -c "
import tempfile, sys
sys.path.insert(0, 'backend')
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

tmp = tempfile.mkdtemp()
m = ZimMetadata(title='Open-Repo Test', description='Offline knowledge library', language='eng',
    name='open-repo_en_nopic', flavour='nopic', creator='Open-Repo Community',
    publisher='Open-Repo', source_url='https://example.org')
writer = ZimWriter(metadata=m, config=ExportConfig(), output_path=Path(tmp)/'t.zim', zimcheck_binary='zimcheck')
for i in range(10):
    writer.add_article(
        path=f'item/{i:03d}',
        content=f'<html><head><title>Article {i}</title></head><body><h1>Article {i}</h1><p>Content.</p></body></html>',
        article_type='procedure')
writer.add_article(path='index',
    content='<html><head><title>Home</title></head><body><h1>Open-Repo</h1></body></html>',
    article_type='procedure')
result = writer.create_zim(run_zimcheck=True)
print('zimcheck passed:', result.zimcheck_passed)
print('File size:', result.file_size_bytes, 'bytes')
"
```
Expected: `zimcheck passed: True` and `File size: > 10000`

**If zimcheck fails**: Run `zimcheck --verbose /tmp/t.zim` for specific error messages. Common fixes:
- `illustration dimensions`: Replace `_FALLBACK_ILLUSTRATION_PNG` with a confirmed 48x48 PNG
- `description too long`: Test description is 27 chars — should not trigger
- `name invalid`: `open-repo_en_nopic` matches the naming regex

**Estimated duration**: 30 min including troubleshooting buffer

---

## Phase C: Write 12 New Integration Tests (1.5 hours)

**Blocker**: B3 and B4 complete

Create three new test files:

### Step C1: tests/unit/test_zim_writer_libzim.py

**Duration**: 45 minutes
**Tests 1–5, 10–12 from roadmap matrix**

Implement:
- `test_zim_writer_creates_real_zim_file`: Assert `open(path,'rb').read(4) == b'\x5a\x49\x4d\x04'`
- `test_zim_metadata_all_mandatory_fields`: Use `Archive.get_metadata()` for Title, Language, Creator, Name
- `test_xapian_index_populated`: Use `Archive`'s search API; assert >=1 result for known keyword
- `test_article_count_matches_database`: Generate 50-article ZIM; verify `archive.entry_count >= 50`
- `test_html_no_external_dependencies`: Parse rendered HTML with `re.findall(r'src="http|href="http', content)`; assert empty
- `test_period_collision_handling`: `ZimWriter.compute_period(["2026-05"], now=datetime(2026, 5, 19)) == "2026-05a"`
- `test_zimwriter_not_reusable_after_finalize`: Second `create_zim()` raises `RuntimeError`
- `test_nopic_variant_excludes_images`: No entries with `mime_type.startswith("image/")` in nopic ZIM

### Step C2: tests/integration/test_zimcheck_validation.py

**Duration**: 20 minutes
**Tests 6–7 from roadmap matrix**

Implement:
- `test_zimcheck_passes_on_valid_export`: 10-article ZIM; `result.zimcheck_passed == True`
- `test_zimcheck_fails_on_corrupted_archive`: Write ZIM, then corrupt bytes; verify file renamed to `.zim.invalid`

Decorate both with `@pytest.mark.integration`.

### Step C3: tests/integration/test_zim_readback.py

**Duration**: 25 minutes
**Tests 8–9 from roadmap matrix**

Implement:
- `test_offline_read_article_by_path`: Write article at `agriculture/biosand-filter`; read back via `Archive.get_entry_by_path()`; assert content matches
- `test_unicode_content_survives_roundtrip`: Write article with French (`é`), Arabic (`ح`), Spanish (`ñ`); read back; assert no `�` replacement characters

Decorate both with `@pytest.mark.integration`.

### Step C4: Run full test suite

```bash
cd backend
python3 -m pytest tests/ -q
```
Expected: `100 passed` (88 existing + 12 new)

---

## Phase D: Manual End-to-End Verification (1 hour)

**Blocker**: All Phase B and C complete

### Step D1: Generate verification ZIM

```bash
uv run python3 -c "
import sys
sys.path.insert(0, 'backend')
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig

m = ZimMetadata(title='Open-Repo E2E Test', description='End-to-end verification export', language='eng',
    name='open-repo_en_nopic', flavour='nopic', creator='Open-Repo Community',
    publisher='Open-Repo', source_url='https://example.org', date='2026-05-20')
writer = ZimWriter(metadata=m, config=ExportConfig(), output_path=Path('/tmp/open-repo_e2e_2026-05.zim'))

writer.add_article(path='index',
    content='<html><head><title>Open-Repo</title><style>body{font-family:sans-serif;}</style></head><body><h1>Open-Repo Library</h1><p>Knowledge for offline use.</p></body></html>',
    article_type='procedure')

domains = ['water', 'agriculture', 'energy', 'recipes', 'building']
for i in range(20):
    d = domains[i % len(domains)]
    writer.add_article(
        path=f'{d}/item-{i:03d}',
        content=f'<html><head><title>{d.title()} Guide {i+1}</title><style>body{{font-family:sans-serif;}}</style></head><body><h1>{d.title()} Guide {i+1}</h1><p>Practical guide for {d}.</p></body></html>',
        article_type='procedure')

result = writer.create_zim()
print('Written:', result.output_path)
print('Articles:', result.article_count)
print('Size:', result.file_size_bytes, 'bytes')
print('zimcheck passed:', result.zimcheck_passed)
print('SHA-256:', result.sha256)
"
```

Expected:
```
Articles: 21
Size: > 50000
zimcheck passed: True
SHA-256: [64 hex characters]
```

### Step D2: Verify offline read

```bash
# Option A: kiwix-serve (Docker)
docker run --rm -v /tmp:/data kiwix/kiwix-serve /data/open-repo_e2e_2026-05.zim &
curl -s localhost:8080 | grep -i "open-repo\|html"

# Option B: libzim reader (Python, no Docker needed)
uv run python3 -c "
from libzim import Archive
archive = Archive('/tmp/open-repo_e2e_2026-05.zim')
print('Entry count:', archive.entry_count)
entry = archive.get_entry_by_path('index')
content = entry.get_item().content.tobytes()
print('Index article length:', len(content), 'bytes')
print('Content preview:', content[:100])
"
```

---

## Phase E: Cleanup and PR Preparation (1 hour)

### Step E1: Remove _stub_write_placeholder()

**Duration**: 15 minutes
**File**: `backend/app/services/export/zim_writer.py`
**Location**: Lines 922–939 (the `_stub_write_placeholder` method)

Delete the entire method. Also remove the `if not _LIBZIM_AVAILABLE: self._stub_write_placeholder()` branch from `create_zim()` if libzim is confirmed always available in the deployment environment. Keep the import guard for now.

```bash
python3 -m pytest tests/ -q
```
Expected: `100 passed` — no regressions from removing the stub.

---

### Step E2: Alembic migration for zim_exports table

**Duration**: 30 minutes
**Blocker**: None (can run in parallel with E1)

```bash
cd backend
alembic revision --autogenerate -m "add_zim_exports_table"
```

Review the generated migration. Ensure it matches the schema in the roadmap (28 columns, 3 indexes). Apply:

```bash
alembic upgrade head
alembic current
```
Expected: Head revision shown as current.

---

### Step E3: Add ZimExport SQLAlchemy model

**Duration**: 20 minutes
**File**: `backend/app/models.py`

Add `ZimExportStatus` enum and `ZimExport` model as specified in the roadmap. Import `ZimExport` in `alembic/env.py`'s `target_metadata` so future autogenerate detects model changes.

---

### Step E4: Final test suite

```bash
python3 -m pytest tests/ -v 2>&1 | tail -25
```
Expected: All tests pass. Zero failures.

---

### Step E5: Create PR

```bash
git add backend/app/services/export/zim_writer.py backend/pyproject.toml backend/app/models.py backend/tests/ backend/alembic/
git commit -m "feat(phase-5): activate libzim integration in ZimWriter"
```

PR title: `feat(phase-5): activate libzim integration in ZimWriter`

PR body should reference:
- 5 code changes in `zim_writer.py`
- Test count: 88 + 12 = 100 total
- zimcheck validation passing
- Corrected config_indexing sequencing (must be before Creator context)
- Phase 4 PR #1 dependency (do not merge before Phase 4 lands)

---

## Risk Mitigation Quick Reference

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `RuntimeError: Creator started` | `config_indexing()` inside context | Move to before `with creator:` — see corrected Change 3 |
| `ModuleNotFoundError: libzim` | Wheel not installed in uv env | `uv pip install "libzim>=3.2,<4.0"` |
| `zimcheck FAILED: illustration` | Fallback PNG wrong dimensions | Verify `_FALLBACK_ILLUSTRATION_PNG` is 48x48 (confirmed in this audit) |
| `zimcheck FAILED: Description too long` | Description >80 chars | Shorten to ≤80 chars |
| `zimcheck FAILED: Name invalid` | Name format mismatch | Must match `{pub}_{lang}_{flavour}` with lowercase alnum + hyphens |
| Magic bytes wrong (`53544742...`) | Stub path still executing | Confirm `_LIBZIM_AVAILABLE == True`; check import guard |
| Articles missing from ZIM | `add_article()` not called before `create_zim()` | Verify article addition loop executes |
| Export OOM-killed | Article buffer too large | Reduce max_items in ExportConfig |
| Export >90 seconds | Thermal throttling (RPi5) | Schedule at 02:00 UTC; check CPU temperature |
| `AttributeError` swallowed | `try/except AttributeError` in `_apply_metadata_to_creator` | Remove the guard once libzim is confirmed installed |

---

## Completion Definition

Phase 5 Candidate 1 is complete when:

- [ ] `python3 -m pytest tests/ -q` reports `100 passed` (88 + 12)
- [ ] `zimcheck` passes on a 20-article test ZIM (exit code 0)
- [ ] ZIM opens in Kiwix (kiwix-serve or Kiwix Android) — articles display, search works
- [ ] `sha256sum -c {file}.sha256` passes
- [ ] `alembic upgrade head` applied cleanly
- [ ] `ZimExport` model added to `app/models.py`
- [ ] `_stub_write_placeholder()` method deleted from codebase
- [ ] No `TODO(post-PR-merge)` markers remaining in `zim_writer.py`
- [ ] PR created, linked to Phase 4 PR #1 as dependency
- [ ] Corrected `config_indexing()` placement documented in method docstring

---

*Checklist created: 2026-05-20 (Session 1435)*
*Supersedes: candidate-1-implementation-checklist.md and PHASE_5_CANDIDATE_1_IMPLEMENTATION_CHECKLIST.md*
*Critical correction: config_indexing() must be called before Creator context entry, not inside it*
