---
title: "Phase 5 Candidate 1 — Hour-by-Hour Implementation Checklist"
project: open-repo
phase: 5
candidate: 1
date: 2026-05-22
status: ready-for-execution
total_estimated_duration: "6–8 hours (5 code changes) + 2–3 hours (API endpoint, optional)"
deadline: "May 25, 2026 — pre-Phase 5.2 Wave 1 (June 1)"
---

# Phase 5 Candidate 1: Hour-by-Hour Implementation Checklist

**Purpose**: Step-by-step execution guide for activating libzim in ZimWriter. Covers all five code changes, the three blocking prerequisites not in the roadmap (zimcheck, migration, API endpoint), and a Docker test environment setup.

**Start on a feature branch**: `git checkout -b feature/zimwriter-libzim-activation` (or the existing branch if already created)

**Test environment reference**: See Section 6 for Docker config before running integration tests.

---

## Hour 0: Environment Verification (30 minutes)

**Goal**: Confirm all prerequisites are met before touching any code.

### Step 0.1 — Platform check (5 minutes)

- [ ] Run: `python3 --version`
  - Expected: `Python 3.11.2`
  - If not 3.11: verify the venv Python: `.venv/bin/python --version`

- [ ] Run: `uname -m`
  - Expected: `aarch64`

- [ ] Run: `ldd --version | head -1`
  - Expected: `ldd (Debian GLIBC 2.36...)`
  - glibc 2.36 confirms manylinux_2_27 wheel compatibility

### Step 0.2 — Virtual environment check (5 minutes)

- [ ] Navigate to: `cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend`

- [ ] Confirm venv exists: `ls .venv/bin/python`

- [ ] Activate: `source .venv/bin/activate`
  - Prompt should show `(.venv)`

### Step 0.3 — Baseline test run (10 minutes)

- [ ] Run: `python3 -m pytest tests/integration/test_export_pipeline.py -q`
  - Expected: `88 passed in 0.14s`
  - If any fail: do not proceed. Diagnose and fix baseline failures first.

- [ ] Record baseline: `python3 -m pytest tests/ -q 2>&1 | tail -3`
  - Record the total pass count for comparison after changes

### Step 0.4 — zimcheck installation (5 minutes)

- [ ] Check if zimcheck is present: `which zimcheck`
  - If found: skip to Step 0.5
  - If not found: install now

- [ ] Install zimcheck: `sudo apt-get install -y zim-tools`
  - Expected: installs `zimcheck` and `zimdump` and related tools
  - Verify: `zimcheck --version`

**Blocker**: zimcheck is required for integration test validation. Do not skip this step.

### Step 0.5 — Confirm libzim wheel is available (5 minutes)

- [ ] Test wheel availability without installing:
  ```
  pip3 download libzim --no-deps --dest /tmp/zimtest
  ```
  - Expected: `Successfully downloaded libzim` with `manylinux_2_27_aarch64` in the filename
  - If fails: check internet connectivity; the wheel is 8.3 MB

- [ ] Clean up: `rm -rf /tmp/zimtest`

---

## Hour 1: Change 1 — pyproject.toml Dependency (15 minutes)

**Goal**: Add `libzim` to the project's declared dependencies and install the wheel.

### Step 1.1 — Edit pyproject.toml (5 minutes)

- [ ] Open: `backend/pyproject.toml`

- [ ] Locate `[project.dependencies]` section

- [ ] Add after the last dependency (`"meilisearch>=0.30.0",`):
  ```toml
  "libzim>=3.10.0,<4.0",
  ```

  Note: The roadmap document says `>=3.2,<4.0` but the feature branch already has `>=3.10.0,<4.0`. Use the tighter bound — there is no reason to support versions before 3.10.0 from May 2026.

- [ ] Save the file

### Step 1.2 — Install via uv (5 minutes)

- [ ] Run: `uv pip install 'libzim>=3.10.0,<4.0'`
  - Expected output: `Successfully installed libzim-3.10.0`
  - Expected duration: under 10 seconds on fast network (wheel is 8.3 MB)
  - If uv fails: fall back to `.venv/bin/pip install 'libzim>=3.10.0,<4.0'`

### Step 1.3 — Verify installation (5 minutes)

- [ ] Test import:
  ```
  python3 -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('libzim imports OK')"
  ```
  Expected: `libzim imports OK`

- [ ] Verify version:
  ```
  python3 -c "import libzim; print(libzim.__version__)"
  ```
  Expected: `3.10.0`

- [ ] Confirm Xapian is bundled:
  ```
  python3 -c "import libzim; v = libzim.get_versions(); print(v)"
  ```
  Expected: dict showing `libzim`, `libxapian`, `libzstd`, `libicu` versions

**Risk flag**: If `ImportError` persists after installation, check that you are using the venv Python, not the system Python. The system Python is externally managed and cannot receive packages directly.

---

## Hour 1 (continued): Change 2 — Import Guard (15 minutes)

**Goal**: Add the conditional import block to zim_writer.py that enables graceful degradation when libzim is absent.

### Step 2.1 — Locate insertion point (2 minutes)

- [ ] Open: `backend/app/services/export/zim_writer.py`

- [ ] Find line 49: `from typing import Optional`

- [ ] This is where the import guard goes (insert after this line)

### Step 2.2 — Add import guard (5 minutes)

- [ ] After `from typing import Optional`, add:
  ```python

  # Conditional libzim import — allows module to load in environments without the wheel.
  # Remove this guard after integration is verified in CI.
  try:
      from libzim.writer import Creator, Item, StringProvider, Hint
      _LIBZIM_AVAILABLE = True
  except ImportError:
      _LIBZIM_AVAILABLE = False
      Creator = None  # type: ignore[assignment,misc]
  ```

### Step 2.3 — Verify module still imports (3 minutes)

- [ ] Run: `python3 -c "from app.services.export.zim_writer import ZimWriter; print('import OK')"` (from `backend/` directory)
  - Expected: `import OK`

### Step 2.4 — Run baseline tests (5 minutes)

- [ ] Run: `python3 -m pytest tests/integration/test_export_pipeline.py -q`
  - Expected: `88 passed` — same as baseline
  - If any test newly fails: the import guard introduction broke something; investigate before continuing

---

## Hour 2: Change 3 — ArticleItem Class (30 minutes)

**Goal**: Add the `ArticleItem` adapter class that bridges `ZimEntry` to libzim's `Item` interface.

### Step 3.1 — Locate insertion point (5 minutes)

- [ ] In `zim_writer.py`, find the `ZimEntry` dataclass (around line 360)

- [ ] Find the line after the `has_attribution()` method — this is just before the `ZimWriter` class definition (around line 407: `# Main ZimWriter class`)

- [ ] The `ArticleItem` class goes between `ZimEntry` and `ZimWriter`

### Step 3.2 — Add ArticleItem class (15 minutes)

- [ ] Insert the following class after `ZimEntry` and before the `ZimWriter` class:

  ```python
  class ArticleItem(Item):
      """
      Adapter from ZimEntry to libzim's Item interface.

      libzim.writer.Creator.add_item() requires an Item subclass.
      This class bridges ZimEntry (our data model) to libzim's API.

      Thread safety: Each ArticleItem instance is consumed once by add_item()
      and not retained. Thread-safe as long as the owning ZimWriter is
      called from a single thread (enforced by ZimWriter's design).
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

  Note: This class references `Hint` and `StringProvider` from the conditional import above. If `_LIBZIM_AVAILABLE` is False, this class definition will fail because `Item` is undefined. Wrap the class in a guard block:

  ```python
  if _LIBZIM_AVAILABLE:
      class ArticleItem(Item):
          ...
  else:
      class ArticleItem:  # type: ignore[no-redef]
          """Stub ArticleItem for environments without libzim."""
          def __init__(self, entry: "ZimEntry") -> None:
              self._entry = entry
  ```

  Alternatively (simpler): only define `ArticleItem(Item)` once, but guard the `Hint` and `StringProvider` references inside `get_hints()` and `get_contentprovider()`.

### Step 3.3 — Verify tests still pass (10 minutes)

- [ ] Run: `python3 -m pytest tests/integration/test_export_pipeline.py -q`
  - Expected: `88 passed`
  - The `ArticleItem` class is not yet called by any test, so no new tests should pass or fail from this change alone

---

## Hour 2–3: Change 4 — Replace Stub in create_zim() (45 minutes)

**Goal**: Replace `self._stub_write_placeholder()` with the real libzim Creator context manager.

### Step 4.1 — Locate the stub call (5 minutes)

- [ ] In `zim_writer.py`, find around line 762:
  ```python
  # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
  # See the docstring above for the correct implementation pattern.
  # For now, write a placeholder file to allow test harness to run.
  self._stub_write_placeholder()
  ```

### Step 4.2 — Replace stub with Creator block (15 minutes)

- [ ] Replace the TODO comment and `self._stub_write_placeholder()` with:
  ```python
  if not _LIBZIM_AVAILABLE:
      # Fallback stub: write placeholder file for test environments without libzim
      self._stub_write_placeholder()
  else:
      with Creator(str(self.output_path)) as creator:
          creator.config_indexing(True, self.config.language_iso3)
          creator.set_mainpath("index")
          self._apply_metadata_to_creator(creator)
          for entry in self._entries:
              creator.add_item(ArticleItem(entry))
      # Creator.__exit__ triggers ZIM file finalization and disk write
  ```

  The `self._is_finalized = True` line should remain immediately after this block — do not remove it.

### Step 4.3 — Fix _apply_metadata_to_creator() AttributeError catch (10 minutes)

**This step is required.** The current implementation at lines 885-903 wraps all metadata calls in `try: ... except AttributeError: pass`. This silencing catch must be removed now that a real Creator is being passed.

- [ ] In `_apply_metadata_to_creator()`, remove the outer `try:` and `except AttributeError: pass` wrapping, leaving the direct method calls:
  ```python
  def _apply_metadata_to_creator(self, creator: object) -> None:
      """Apply all ZimMetadata fields to the open libzim Creator instance."""
      creator.config_indexing(True, self.config.language_iso3)
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

### Step 4.4 — Fix ORM Float/Integer mismatch (5 minutes)

- [ ] Open: `backend/app/models.py`

- [ ] Find the `ZimExport` model class

- [ ] Locate the `generation_duration_seconds` column

- [ ] Ensure it reads: `generation_duration_seconds = Column(Float, nullable=True)`
  - If it reads `Column(Integer, nullable=True)`: change `Integer` to `Float`
  - This requires `from sqlalchemy import Float` to be in the imports (it likely is already)

### Step 4.5 — Run tests after creator block (10 minutes)

- [ ] Run: `python3 -m pytest tests/integration/test_export_pipeline.py -q`
  - Expected: `88 passed`
  - With libzim now installed and `_LIBZIM_AVAILABLE = True`, the Creator block will execute
  - The `TestZimWriterCreateZim` tests now exercise real ZIM creation

**Important**: If `test_create_zim_produces_output_file` passes, the Creator context is working. If it fails with `AttributeError` or `RuntimeError`, the `ArticleItem` class guard (Step 3.2) may need adjustment.

---

## Hour 3–4: Change 5 — _apply_metadata_to_creator() is Done (30 minutes)

Change 5 from the roadmap was partially completed in Step 4.3 above. The remaining work is verification and the addition of `_FALLBACK_ILLUSTRATION_PNG` reference at module level. The constant is already defined on line 55 of the current zim_writer.py — no new code needed for this change.

### Step 5.1 — Verify _FALLBACK_ILLUSTRATION_PNG constant (5 minutes)

- [ ] In `zim_writer.py`, find line 55 (approximately):
  ```python
  _FALLBACK_ILLUSTRATION_PNG = b'\x89PNG\r\n\x1a\n...'
  ```

- [ ] Validate struct: run this to confirm 48x48:
  ```
  python3 -c "
  import struct
  from app.services.export.zim_writer import _FALLBACK_ILLUSTRATION_PNG as p
  w = struct.unpack('>I', p[16:20])[0]
  h = struct.unpack('>I', p[20:24])[0]
  print(f'PNG dimensions: {w}x{h}')
  "
  ```
  Expected: `PNG dimensions: 48x48`

### Step 5.2 — Run the LibZIM integration stubs (10 minutes)

- [ ] Run the specific integration class:
  ```
  python3 -m pytest tests/integration/test_export_pipeline.py::TestLibZIMIntegration -v
  ```
  Expected: all 4 tests pass
  - `test_fallback_png_is_valid_48x48` — verifies PNG struct
  - `test_fallback_png_always_returned` — verifies `_get_illustration_bytes()` fallback
  - `test_config_indexing_call_in_metadata_apply` — verifies the mock Creator receives `config_indexing(True, "eng")`
  - `test_zim_magic_bytes_present` — verifies file creation

### Step 5.3 — Run full export test suite (15 minutes)

- [ ] Run: `python3 -m pytest tests/integration/test_export_pipeline.py -v 2>&1 | tail -20`
  - Expected: `88 passed`

- [ ] Run the complete test suite to check for regressions:
  ```
  python3 -m pytest tests/ -q
  ```
  Expected: same total pass count as baseline (plus any new tests)

---

## Hour 4–5: Integration Testing (60 minutes)

**Goal**: Run zimcheck against a real generated ZIM file. This validates the full pipeline end-to-end.

### Step 6.1 — Generate a test ZIM (20 minutes)

- [ ] Create a test script at `/tmp/test_zim_gen.py`:
  ```python
  import sys
  sys.path.insert(0, '/home/awank/dev/SuperClaude_Framework/projects/open-repo/backend')

  from pathlib import Path
  from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

  output_path = Path('/tmp/test_export.zim')

  metadata = ZimMetadata(
      title="Open-Repo Test",
      description="Offline practical knowledge library",
      language="eng",
      name="open-repo_en_nopic",
      flavour="nopic",
      creator="Open-Repo Community",
      publisher="Open-Repo",
      source_url="https://test.open-repo.example.org",
  )

  config = ExportConfig(
      scope=ExportScope.LOCAL_ONLY,
      flavour="nopic",
      include_images=False,
      language_iso3="eng",
  )

  writer = ZimWriter(
      metadata=metadata,
      config=config,
      output_path=output_path,
      zimcheck_binary=None,  # We will run zimcheck manually
  )

  # Add 10 test articles
  for i in range(10):
      writer.add_article(
          path=f"water/article-{i:04d}",
          content=f"<html><head><title>Article {i}</title><style>body{{font-family:sans-serif;}}</style></head><body><h1>Article {i}</h1><p>Test content for article number {i}. Biosand filter installation step {i}.</p></body></html>",
          article_type="procedure",
      )

  # Add index article (required by set_mainpath("index"))
  writer.add_article(
      path="index",
      content="<html><head><title>Open-Repo</title></head><body><h1>Open-Repo Offline Library</h1><p>Test export with 10 articles.</p></body></html>",
      article_type="procedure",
  )

  result = writer.create_zim(run_zimcheck=False)
  print(f"ZIM created: {result.output_path}")
  print(f"Size: {result.file_size_bytes:,} bytes")
  print(f"Articles: {result.article_count}")
  print(f"SHA-256: {result.sha256}")

  # Check magic bytes
  data = output_path.read_bytes()
  print(f"Magic bytes: {data[:4].hex()}")
  expected_magic = bytes([0x5a, 0x49, 0x4d, 0x04])
  print(f"ZIM magic match: {data[:4] == expected_magic}")
  ```

- [ ] Run: `python3 /tmp/test_zim_gen.py`
  - Expected output includes: `ZIM magic match: True`
  - Expected file size: >5 KB (stub produces <200 bytes; real ZIM with 11 articles should be >50 KB)

**Blocker check**: If `ZIM magic match: False`, the Creator did not run (still using stub). Check `_LIBZIM_AVAILABLE` is `True` in the running Python process.

### Step 6.2 — Run zimcheck validation (10 minutes)

- [ ] Run: `zimcheck /tmp/test_export.zim`
  - Expected: `No error detected` and exit code 0
  - Any `ERROR:` lines are hard failures that must be fixed before Wave 1

- [ ] If zimcheck fails: run verbose mode for diagnosis:
  ```
  zimcheck -v /tmp/test_export.zim
  ```

  Common failures and fixes:
  | Error message | Cause | Fix |
  |---------------|-------|-----|
  | `Empty ZIM file` | Creator block did not execute | Verify `_LIBZIM_AVAILABLE = True` |
  | `Title is longer than 30 characters` | Warning only in zimcheck 3.x+ | Not a failure; proceed |
  | `Missing Illustration` | `add_illustration()` not called | Check `_apply_metadata_to_creator()` |
  | `Illustration size` | PNG dimensions wrong | Verify fallback PNG is 48x48 |
  | `External link found` | Article HTML has `http://` in src/href | Scrub content before `add_article()` |

### Step 6.3 — SHA-256 sidecar verification (10 minutes)

- [ ] Generate the sidecar file:
  ```
  sha256sum /tmp/test_export.zim > /tmp/test_export.zim.sha256
  ```

- [ ] Verify it round-trips:
  ```
  sha256sum -c /tmp/test_export.zim.sha256
  ```
  Expected: `test_export.zim: OK`

### Step 6.4 — Verify ZIM is readable with libzim reader (20 minutes)

- [ ] Run reader validation:
  ```
  python3 -c "
  from libzim.reader import Archive
  a = Archive('/tmp/test_export.zim')
  print(f'Entry count: {a.entry_count}')
  e = a.get_entry_by_path('index')
  print(f'Index title: {e.title}')
  "
  ```
  Expected: entry count 11 (10 articles + index), index title present

- [ ] Test search:
  ```
  python3 -c "
  from libzim.reader import Archive
  a = Archive('/tmp/test_export.zim')
  s = a.search('Biosand')
  results = list(s.getResults(0, 5))
  print(f'Search results for Biosand: {len(results)}')
  "
  ```
  Expected: at least 1 result (articles contain "Biosand")

---

## Hour 5–6: Database Migration (30 minutes)

### Step 7.1 — Review migration 003 (10 minutes)

- [ ] Find the migration file:
  ```
  ls backend/alembic/versions/ | grep zim_exports
  ```

- [ ] Read the migration to confirm it creates the correct schema:
  - Table name: `zim_exports`
  - Primary key: `id BIGSERIAL`
  - UUID field: `zim_uuid VARCHAR(36) UNIQUE NOT NULL`
  - Status field: `status VARCHAR(20) NOT NULL DEFAULT 'generating'`
  - `generation_duration_seconds` type: confirm it is `FLOAT` (matches the ORM fix from Step 4.4)

### Step 7.2 — Apply migration (5 minutes)

- [ ] Ensure database is accessible: `alembic current`
  - Expected: shows current migration head

- [ ] Apply: `alembic upgrade head`
  - Expected: runs migration 003
  - Verify: `alembic current` shows the new head

### Step 7.3 — Verify table schema (5 minutes)

- [ ] Connect to the database and run:
  ```sql
  \d zim_exports
  ```
  or via SQLAlchemy:
  ```
  python3 -c "
  from app.database import engine
  from sqlalchemy import inspect
  inspector = inspect(engine)
  cols = inspector.get_columns('zim_exports')
  print([c['name'] for c in cols])
  "
  ```

### Step 7.4 — Run full test suite after migration (10 minutes)

- [ ] Run: `python3 -m pytest tests/ -q`
  - Expected: same or greater pass count than baseline

---

## Hour 6–8: Export API Endpoint (90–120 minutes, optional for Wave 1 test but required for scheduled jobs)

This section covers the export API endpoint. Without it, ZIM exports can only be triggered manually from a Python shell. This step is required before any APScheduler integration or manual UI triggers.

### Step 8.1 — Create app/api/v1/export.py (60 minutes)

- [ ] Create `backend/app/api/v1/export.py` with:
  - `POST /api/v1/exports` — triggers an export job asynchronously via FastAPI BackgroundTask
    - Request body: `scope`, `flavour`, `include_images` (optional)
    - Response: `{"job_id": "<uuid>", "status": "generating"}`
  - `GET /api/v1/exports/{job_id}` — returns status of an export job
  - `GET /api/v1/exports/health` — returns last successful export stats

- [ ] The endpoint instantiates `ZimWriter` with metadata derived from the request, calls `create_zim()` in the background task, and writes the result to the `zim_exports` table.

### Step 8.2 — Register route (10 minutes)

- [ ] In `backend/app/main.py` (or routes.py), register the new router:
  ```python
  from app.api.v1 import export as export_router
  app.include_router(export_router.router, prefix="/api/v1")
  ```

### Step 8.3 — Test the endpoint (20 minutes)

- [ ] Start the server: `uvicorn app.main:app --host 127.0.0.1 --port 8000`

- [ ] Trigger an export:
  ```
  curl -X POST http://127.0.0.1:8000/api/v1/exports \
    -H "Content-Type: application/json" \
    -d '{"scope": "local", "flavour": "nopic"}'
  ```
  Expected response: `{"job_id": "...", "status": "generating"}`

- [ ] Poll status:
  ```
  curl http://127.0.0.1:8000/api/v1/exports/{job_id}
  ```

---

## Hour 6 (parallel track): Step 9 — Remove Stub Method (15 minutes)

**Prerequisites**: All 88 tests pass with libzim active, zimcheck passes on test ZIM.

- [ ] In `zim_writer.py`, delete `_stub_write_placeholder()` (currently lines 922–939)

- [ ] Remove any remaining `# TODO(post-PR-merge)` comments from the file

- [ ] Run: `python3 -m pytest tests/integration/test_export_pipeline.py -q`
  - Expected: `88 passed` — no test should reference the stub method directly

---

## Section 6: Docker Test Environment

Use this Docker configuration for isolated ZimWriter testing when you need a clean environment without affecting the development system.

### Dockerfile

```dockerfile
FROM python:3.11-slim-bookworm

# Install zimcheck and runtime dependencies
RUN apt-get update && apt-get install -y \
    zim-tools \
    && rm -rf /var/lib/apt/lists/*

# Install libzim wheel
RUN pip install libzim==3.10.0

# Copy backend source
WORKDIR /app
COPY backend/pyproject.toml backend/README.md ./
COPY backend/app/ ./app/
COPY backend/tests/ ./tests/
COPY backend/alembic/ ./alembic/
COPY backend/alembic.ini ./

# Install project dependencies (excludes libzim since already installed above)
RUN pip install -e ".[dev]"

# Default: run export tests only
CMD ["python", "-m", "pytest", "tests/integration/test_export_pipeline.py", "-v"]
```

### docker-compose.yml for integration testing

```yaml
version: "3.9"

services:
  zimwriter-test:
    build:
      context: .
      dockerfile: Dockerfile.zimtest
    volumes:
      - ./backend:/app:ro
      - /tmp/zim-test-output:/tmp/zim-output
    environment:
      - PYTHONDONTWRITEBYTECODE=1
      - PYTHONUNBUFFERED=1
    network_mode: none  # No network needed for unit/integration tests

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: openrepo_test
      POSTGRES_USER: openrepo
      POSTGRES_PASSWORD: test_password_local
    ports:
      - "127.0.0.1:5432:5432"  # Bind to localhost only — never 0.0.0.0
    volumes:
      - postgres_test_data:/var/lib/postgresql/data

volumes:
  postgres_test_data:
```

### Running the Docker test environment

```bash
# Build
docker build -f Dockerfile.zimtest -t open-repo-zimtest .

# Run export pipeline tests only
docker run --rm open-repo-zimtest

# Run with output volume for ZIM inspection
docker run --rm -v /tmp/zim-output:/tmp/zim-output open-repo-zimtest \
  python3 /tmp/test_zim_gen.py

# Inspect the generated ZIM
docker run --rm -v /tmp/zim-output:/tmp/zim-output open-repo-zimtest \
  zimcheck /tmp/zim-output/test_export.zim
```

### Notes on the Docker environment

- The container binds postgres to `127.0.0.1:5432` — never bare `5432:5432` or `0.0.0.0:5432:5432`
- `network_mode: none` for the test container prevents any accidental outbound calls during tests
- The `/tmp/zim-output` volume allows host-side inspection of generated ZIM files with Kiwix Desktop or zimcheck

---

## Final Verification Checklist (Pre-PR)

Run these in sequence before creating the PR.

- [ ] `python3 -m pytest tests/integration/test_export_pipeline.py -v` — 88 passed
- [ ] `python3 -m pytest tests/ -q` — all baseline tests plus new tests pass
- [ ] `zimcheck /tmp/test_export.zim` — no errors, exit code 0
- [ ] `sha256sum -c /tmp/test_export.zim.sha256` — OK
- [ ] ZIM opens in kiwix-serve: `docker run -v /tmp/test_export.zim:/data/test.zim kiwix/kiwix-serve --library` accessible at http://127.0.0.1:8080
- [ ] `alembic current` shows migration 003 applied
- [ ] `_stub_write_placeholder()` method removed from zim_writer.py
- [ ] `generation_duration_seconds` ORM field is `Column(Float, nullable=True)`
- [ ] All `# TODO(post-PR-merge)` comments removed

### PR title

```
feat(phase-5): activate libzim integration in ZimWriter
```

### Blockers to resolve before June 1 Wave 1

| Item | Owner | Deadline |
|------|-------|----------|
| Merge feature branch to master | Dev | May 25 |
| `apt-get install zim-tools` on production host | Ops | May 28 |
| `alembic upgrade head` on production DB | Ops | May 28 |
| Export API endpoint implemented | Dev | May 30 |
| First scheduled test export (manual trigger) | QA | May 31 |
