---
title: "Phase 5 Candidate 1 — ZimWriter/libzim Activation Checklist"
project: open-repo
phase: 5
candidate: 1
document_type: implementation-checklist
status: ready-for-execution
date: 2026-05-22
session: research-agent
companion: "phase-5-candidate-1-implementation-verification.md"
---

# Phase 5 Candidate 1: Implementation Checklist

**Copy-paste ready for execution once user approves Phase 5 direction (May 23-24 decision).**

All items verified against live system state (2026-05-22). Working directory for all commands: `/home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/`

---

## Pre-Flight Checks (5 minutes)

- [ ] **Confirm working directory**: `pwd` should return `...projects/open-repo/backend`
- [ ] **Confirm libzim installed**: `./`.venv/bin/python -c "import importlib.metadata; print(importlib.metadata.version('libzim'))"` — expected output: `3.10.0`
- [ ] **Confirm baseline tests pass**: `uv run pytest tests/integration/test_export_pipeline.py -q --tb=no` — expected: `88 passed`
- [ ] **Confirm git status clean**: `git status` — should be on `master` with no uncommitted changes
- [ ] **Create feature branch**: `git checkout -b feature/zimwriter-libzim-activation`
  - Dependency: clean git status above

---

## Stage A: Dependency Declaration (5-10 minutes)

### A.1 — Add libzim to pyproject.toml
- [ ] Open `backend/pyproject.toml`
- [ ] Add `"libzim>=3.10.0,<4.0",` to the `[project.dependencies]` list (after `meilisearch>=0.30.0`)
- [ ] Save file
- [ ] Run: `uv pip install -e .`
  - Expected: installs cleanly, no download needed (already in venv)
- [ ] Verify: `./`.venv/bin/python -c "import importlib.metadata; print(importlib.metadata.version('libzim'))"` — expected: `3.10.0`
- **Duration**: 5 minutes
- **Dependency**: None — this is the first change

---

## Stage B: zim_writer.py Core Changes (2-4 hours total)

### B.1 — Add libzim import guard
- [ ] Open `backend/app/services/export/zim_writer.py`
- [ ] Find line 50: `from typing import Optional`
- [ ] Insert the following block AFTER line 50:

```python
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None  # type: ignore[assignment,misc]
    Item = object   # type: ignore[assignment,misc]
    StringProvider = None  # type: ignore[assignment,misc]
    Hint = None  # type: ignore[assignment,misc]
```

- [ ] Save file
- [ ] Verify module still imports cleanly:
  ```
  ./`.venv/bin/python -c "from app.services.export.zim_writer import ZimWriter; print('import OK')"
  ```
  Expected output: `import OK`
- **Duration**: 5 minutes
- **Dependency**: A.1 complete (libzim in pyproject.toml)

### B.2 — Add ArticleItem class
- [ ] In `zim_writer.py`, find the end of the `ZimEntry` class (~line 405, the `has_attribution()` method)
- [ ] Find the separator comment block that starts at ~line 407: `# ---------------------------------------------------------------------------`
- [ ] Insert the following class BEFORE that separator comment (i.e., after `ZimEntry.has_attribution()`, before the `ZimWriter` class):

```python
class ArticleItem(Item):
    """
    Adapter from ZimEntry to libzim's Item interface.

    libzim.writer.Creator.add_item() requires an Item subclass.
    This class bridges ZimEntry (our data model) to libzim's API.
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

- [ ] Save file
- [ ] Run test suite: `uv run pytest tests/integration/test_export_pipeline.py -q --tb=no`
  - Expected: `88 passed` (ArticleItem is not called yet; tests use stub path)
  - If fewer than 88 pass: do not continue until resolved
- **Duration**: 15 minutes
- **Dependency**: B.1 complete

### B.3 — Replace stub in create_zim() [CRITICAL CHANGE]

> CRITICAL: config_indexing() MUST be called BEFORE the `with creator:` context. Calling it inside the context raises RuntimeError: Creator started. Follow the exact pattern below.

- [ ] In `zim_writer.py`, find lines 762-765:
```python
        # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
        # See the docstring above for the correct implementation pattern.
        # For now, write a placeholder file to allow test harness to run.
        self._stub_write_placeholder()
```

- [ ] Replace those 4 lines with:
```python
        if not _LIBZIM_AVAILABLE:
            self._stub_write_placeholder()
        else:
            creator = Creator(str(self.output_path))
            creator.config_indexing(True, self.config.language_iso3)
            creator.set_mainpath("index")
            with creator:
                self._apply_metadata_to_creator(creator)
                for entry in self._entries:
                    creator.add_item(ArticleItem(entry))
            # Creator.__exit__ triggers ZIM file finalization and write
```

- [ ] Save file
- **Duration**: 10 minutes for the edit
- **Dependency**: B.2 complete

### B.4 — Fix _apply_metadata_to_creator() [CRITICAL CHANGE]

> CRITICAL: The current implementation has two bugs: (1) calls config_indexing() inside the method (wrong — must be before context), and (2) has a silent `except AttributeError: pass` that masks real errors. Both must be fixed simultaneously with B.3.

- [ ] In `zim_writer.py`, find the `_apply_metadata_to_creator()` method (starts ~line 873)
- [ ] Find the entire method body from the `try:` block through the `except AttributeError: pass` line (~lines 885-904)
- [ ] Replace the entire method body (everything from the `try:` to end of method) with:

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
        if self.metadata.long_description:
            creator.add_metadata("LongDescription", self.metadata.long_description)
        illustration_bytes = self._get_illustration_bytes()
        creator.add_illustration(48, illustration_bytes)
```

- [ ] Verify the method signature line reads: `def _apply_metadata_to_creator(self, creator: object) -> None:`
- [ ] Save file
- **Duration**: 10 minutes for the edit
- **Dependency**: B.3 complete (do both B.3 and B.4 before testing)

### B.5 — Smoke test with real libzim Creator

- [ ] Run the smoke test script (save as `/tmp/smoke_test.py` and run via uv):

```python
# /tmp/smoke_test.py
import sys
sys.path.insert(0, '/home/awank/dev/SuperClaude_Framework/projects/open-repo/backend')

import tempfile, pathlib
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

with tempfile.TemporaryDirectory() as tmpdir:
    metadata = ZimMetadata(
        title="Smoke Test",
        description="Phase 5.1 smoke test",
        language="eng",
        name="open-repo_en_test",
        flavour="nopic",
        creator="Open-Repo",
        publisher="Open-Repo",
        source_url="http://localhost",
    )
    config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
    output = pathlib.Path(tmpdir) / "test.zim"
    writer = ZimWriter(metadata=metadata, config=config, output_path=output)
    writer.add_article(
        path="index",
        content="<html><body><h1>Test Article</h1><p>Hello world.</p></body></html>",
        article_type="article",
        language="en",
    )
    result = writer.create_zim(run_zimcheck=False)

    with open(output, 'rb') as f:
        magic = f.read(4)

    assert magic == b'\x5a\x49\x4d\x04', f"Expected ZIM magic bytes, got: {magic.hex()}"
    print(f"ZIM magic bytes: {magic.hex()} (OK)")
    print(f"ZIM file size: {result.file_size_bytes:,} bytes")
    print(f"SHA-256 prefix: {result.sha256[:16]}...")
    print(f"Article count: {result.article_count}")
    print("SMOKE TEST PASSED")
```

- [ ] Run: `cd backend && .venv/bin/python /tmp/smoke_test.py`
- [ ] Expected output:
  ```
  ZIM magic bytes: 5a494d04 (OK)
  ZIM file size: ~50,000-100,000 bytes
  SHA-256 prefix: ...
  Article count: 1
  SMOKE TEST PASSED
  ```
- [ ] If `RuntimeError: Creator started`: config_indexing is inside the context manager — recheck B.3 edit
- [ ] If `AttributeError` on any metadata call: remove any remaining `try/except AttributeError` block — recheck B.4 edit
- [ ] If ZIM magic bytes are wrong (e.g., `535455422`): stub is still active — check `_LIBZIM_AVAILABLE` is `True`
- **Duration**: 15-60 minutes (including debugging if needed)
- **Dependency**: B.3 and B.4 complete

### B.6 — Run 88-test suite post-implementation

- [ ] Run: `uv run pytest tests/integration/test_export_pipeline.py -q --tb=short`
- [ ] Expected: `88 passed`
- [ ] If any test fails: identify whether it's asserting on stub file content (look for "STUB ZIM PLACEHOLDER" in test assertions)
  - If yes: the test needs updating to expect real ZIM output or a RuntimeError
- **Duration**: 5-15 minutes
- **Dependency**: B.5 smoke test passed

---

## Stage C: Database Schema (50 minutes)

### C.1 — Add ZimExport model to app/models.py

- [ ] Open `backend/app/models.py`
- [ ] Add the following imports at the top if not already present:
  ```python
  import enum
  from sqlalchemy import BigInteger, Boolean, Enum, Float, Text
  ```
- [ ] Append the following two classes to the end of the file:

```python
class ZimExportStatus(str, enum.Enum):
    GENERATING = "generating"
    VALIDATING = "validating"
    UPLOADING = "uploading"
    AVAILABLE = "available"
    SUPERSEDED = "superseded"
    DELETED = "deleted"
    ERROR = "error"


class ZimExport(Base):
    """Records completed ZIM offline export jobs."""

    __tablename__ = "zim_exports"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    zim_uuid = Column(String(36), unique=True, nullable=False, index=True)
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
    status = Column(Enum(ZimExportStatus), nullable=False,
                    default=ZimExportStatus.GENERATING, index=True)
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
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<ZimExport id={self.id} name={self.name} period={self.period} status={self.status}>"
```

- [ ] Save file
- [ ] Verify: `./`.venv/bin/python -c "from app.models import ZimExport, ZimExportStatus; print('ZimExport model OK')"` — expected: `ZimExport model OK`
- **Duration**: 20-30 minutes
- **Dependency**: None (can be done in parallel with B stages if splitting work)

### C.2 — Create Alembic migration 003

- [ ] Run: `alembic revision --autogenerate -m "add_zim_exports_table"`
  - If alembic is not in PATH: `./`.venv/bin/alembic revision --autogenerate -m "add_zim_exports_table"`
- [ ] Open the generated file in `alembic/versions/` (will have a timestamp prefix)
- [ ] Review the generated SQL:
  - Confirm: `op.create_table('zim_exports', ...)` is present
  - Confirm: `op.create_index('idx_zim_exports_is_current', ...)` or equivalent indexes are present
  - Confirm: `downgrade()` function has `op.drop_table('zim_exports')`
- [ ] Add the three production indexes manually if autogenerate omitted them:
  ```python
  op.create_index('idx_zim_exports_name_flavour', 'zim_exports', ['name', 'flavour'])
  op.create_index('idx_zim_exports_is_current', 'zim_exports', ['is_current'],
                  postgresql_where="is_current = TRUE")
  op.create_index('idx_zim_exports_status', 'zim_exports', ['status'])
  ```
- [ ] Apply to local database: `alembic upgrade head`
  - Note: this requires a running PostgreSQL instance. If none is available locally, skip and apply in deployment environment.
- **Duration**: 20 minutes
- **Dependency**: C.1 complete

---

## Stage D: Validation and Cleanup (1-1.5 hours)

### D.1 — Delete _stub_write_placeholder() [Change 5]

- [ ] Confirm smoke test (B.5) has passed — DO NOT do this step before B.5 succeeds
- [ ] In `zim_writer.py`, locate the `_stub_write_placeholder()` method (lines 922-939)
- [ ] Delete the entire method
- [ ] In `create_zim()`, update the `if not _LIBZIM_AVAILABLE:` branch:
  - Change `self._stub_write_placeholder()` to:
    ```python
    raise RuntimeError("libzim is not installed. Cannot create ZIM file. Run: uv pip install libzim>=3.10.0")
    ```
- [ ] Run: `uv run pytest tests/integration/test_export_pipeline.py -q --tb=short`
  - Expected: `88 passed`
  - If any test fails with AttributeError or similar: grep for `_stub_write_placeholder` in `tests/` to find what's testing the stub path
- **Duration**: 20 minutes
- **Dependency**: B.5 smoke test passed, B.6 tests passing

### D.2 — Install zimcheck (optional but recommended)

- [ ] Run: `sudo apt install zim-tools`
  - Expected: installs zimcheck 3.1.3 from Debian Bookworm
- [ ] Verify: `which zimcheck` returns `/usr/bin/zimcheck`
- [ ] Test: `zimcheck --version`
- [ ] If sudo unavailable: skip and use Docker approach (see Section 5 of verification doc)
- **Duration**: 5 minutes
- **Dependency**: None (can be done at any point)

### D.3 — Run zimcheck on a test export (if D.2 complete)

- [ ] Modify smoke test to run zimcheck:
  - In the smoke test script: change `writer.create_zim(run_zimcheck=False)` to `writer.create_zim(run_zimcheck=True)`
  - Add: `print(f"zimcheck passed: {result.zimcheck_passed}")`
- [ ] Run smoke test again
- [ ] Expected: `zimcheck passed: True`
- [ ] If zimcheck fails: run `zimcheck /path/to/test.zim --verbose` and review errors
  - Common cause: Description > 80 chars (ZimMetadata.validate() checks this — should not occur)
  - Common cause: Empty Name field (check metadata.name is set)
- **Duration**: 15 minutes
- **Dependency**: D.2 complete, B.5 smoke test passed

### D.4 — Full end-to-end test with real corpus

- [ ] Write a script that loads all 32 articles from `../data/openfarm_procedures.jsonl` and creates a real ZIM:

```python
# /tmp/e2e_test.py
import sys, json, tempfile, pathlib
sys.path.insert(0, '/home/awank/dev/SuperClaude_Framework/projects/open-repo/backend')

from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

articles = [json.loads(l) for l in open(
    '/home/awank/dev/SuperClaude_Framework/projects/open-repo/data/openfarm_procedures.jsonl'
) if l.strip()]

with tempfile.TemporaryDirectory() as tmpdir:
    metadata = ZimMetadata(
        title="Open-Repo: Farming Procedures",
        description="Offline practical farming knowledge",
        language="eng",
        name="open-repo_en_nopic",
        flavour="nopic",
        creator="Open-Repo Community",
        publisher="Open-Repo",
        source_url="https://localhost",
    )
    config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
    output = pathlib.Path(tmpdir) / "open-repo_en_nopic_2026-05.zim"
    writer = ZimWriter(metadata=metadata, config=config, output_path=output)

    for art in articles:
        title = art['title']['en'] if isinstance(art['title'], dict) else art['title']
        steps_html = "".join(
            f"<li><p>{s['body']['en']}</p></li>" for s in art.get('steps', [])
        )
        html = f"<html><head><title>{title}</title></head><body><h1>{title}</h1><ol>{steps_html}</ol></body></html>"
        writer.add_article(
            path=art['cid'],
            content=html,
            article_type="procedure",
            language="en",
        )

    result = writer.create_zim(run_zimcheck=False)

    with open(output, 'rb') as f:
        magic = f.read(4)

    print(f"ZIM magic: {magic.hex()} (expected: 5a494d04)")
    print(f"Articles: {result.article_count}")
    print(f"File size: {result.file_size_bytes:,} bytes")
    print(f"Duration: {result.generation_duration_seconds:.2f}s")
    print(f"SHA-256: {result.sha256[:16]}...")
    assert magic == b'\x5a\x49\x4d\x04'
    assert result.article_count == len(articles)
    print(f"END-TO-END TEST PASSED ({len(articles)} articles)")
```

- [ ] Run: `cd backend && .venv/bin/python /tmp/e2e_test.py`
- [ ] Expected: 32 articles, magic bytes `5a494d04`, duration 1-5 seconds, file 500 KB-2 MB
- [ ] Record actual duration and file size (baseline for monitoring)
- **Duration**: 30 minutes (including script writing and debugging)
- **Dependency**: D.1 complete

### D.5 — Add new P0 integration tests

- [ ] Create `tests/integration/test_zim_real_output.py` with at minimum:
  - `test_zim_writer_creates_real_zim_file`: verifies magic bytes `5a494d04`
  - `test_article_count_matches_input`: verifies article count in real ZIM matches input
  - `test_zim_metadata_fields_present`: uses libzim.reader.Archive to verify Title, Description, Language fields
- [ ] Run: `uv run pytest tests/integration/test_zim_real_output.py -v`
- [ ] Expected: all new tests pass
- **Duration**: 45-60 minutes
- **Dependency**: D.1 complete

---

## Stage E: Documentation and PR (1-1.5 hours)

### E.1 — Update backend/README.md

- [ ] Add Phase 5 offline export section covering:
  - libzim dependency and install instructions
  - zimcheck binary requirement (`sudo apt install zim-tools`)
  - How to run a manual ZIM export
  - Where ZIM files are written
- **Duration**: 30 minutes

### E.2 — Commit and PR

- [ ] Stage changed files:
  ```bash
  git add backend/pyproject.toml
  git add backend/app/services/export/zim_writer.py
  git add backend/app/models.py
  git add backend/alembic/versions/003_add_zim_exports_table.py
  git add backend/tests/integration/test_zim_real_output.py
  git add backend/README.md
  ```
- [ ] Commit:
  ```bash
  git commit -m "feat(phase-5): activate libzim integration in ZimWriter"
  ```
- [ ] Create PR with title: `feat(phase-5): activate libzim integration in ZimWriter`
- **Duration**: 15 minutes

---

## Completion Criteria

- [ ] `uv run pytest tests/ -k "export or zim" -v` — all tests pass (88 existing + new P0 tests)
- [ ] ZIM magic bytes `5a494d04` confirmed on real output
- [ ] `result.article_count == len(input_articles)` for 32-article corpus
- [ ] Alembic migration 003 applied cleanly (or documented for deployment)
- [ ] `zimcheck` passes on test output (if D.2 complete)
- [ ] PR created with all changes staged

---

## Timing Summary

| Stage | Description | Est. Duration |
|-------|-------------|---------------|
| Pre-flight | Branch, verify baseline | 10 min |
| A | pyproject.toml dependency | 5 min |
| B.1-B.2 | Import guard + ArticleItem | 20 min |
| B.3-B.4 | Stub replacement + metadata fix (CRITICAL) | 20 min |
| B.5 | Smoke test with real Creator | 15-60 min |
| B.6 | 88-test suite verify | 10 min |
| C.1 | ZimExport model | 25 min |
| C.2 | Alembic migration 003 | 20 min |
| D.1 | Delete stub method | 20 min |
| D.2-D.3 | zimcheck install + validate | 20 min |
| D.4 | End-to-end 32-article test | 30 min |
| D.5 | New P0 integration tests | 50 min |
| E.1-E.2 | README + PR | 45 min |
| **Total** | | **5-8 hours core, 8-11 hours full** |

---

## Critical Warnings

1. **Do not follow the docstring at line 736** — it shows `config_indexing` inside the `with creator:` block, which raises `RuntimeError: Creator started` in libzim 3.9+. Use the pattern in B.3 above.

2. **Do not replace the `_FALLBACK_ILLUSTRATION_PNG` bytes** — the bytes at line 55 of `zim_writer.py` were live-tested against libzim. The bytes in the roadmap document are different and untested.

3. **Do not remove the `_stub_write_placeholder()` method before B.5 smoke test passes** — the stub is the fallback for test environments; remove it only after confirming the real Creator path works.

4. **Do B.3 and B.4 together before testing** — they are interdependent. Testing after only B.3 will show the config_indexing RuntimeError propagating from `_apply_metadata_to_creator`. Apply both edits, then test.
