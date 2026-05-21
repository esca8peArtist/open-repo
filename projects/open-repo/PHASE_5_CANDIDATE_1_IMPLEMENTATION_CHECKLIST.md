---
title: "Phase 5 Candidate 1 — ZimWriter Implementation Checklist (Session 1477)"
project: open-repo
phase: 5
candidate: 1
date: 2026-05-21
session: 1477
target_branch: feature/zimwriter-libzim-activation
merge_target: master
estimated_total: 90-120 minutes (environment verification through deployment-ready state)
status: READY TO EXECUTE — user runs this checklist after approving merge on May 25-26
---

# Phase 5 Candidate 1: Implementation Checklist

**Purpose**: Step-by-step execution guide for activating the ZimWriter libzim integration. Run this checklist after the feature branch is merged to master. Each item has a checkbox, action description, time estimate, success criterion, and rollback plan.

**Prerequisite**: User has approved the merge of `feature/zimwriter-libzim-activation` to `master` (expected May 25-26). This checklist begins after that merge is complete.

**Total estimated time**: 90-120 minutes from start to deployment-ready state.

**Working directory**: `projects/open-repo/backend/`

---

## Phase A: Environment Verification (15-20 minutes)

These steps verify the environment is correctly configured before any code changes. If any step fails, stop and consult the rollback plan before continuing.

---

### A1. Verify working branch is master (post-merge)

- [ ] **Action**: Confirm you are on the master branch after the feature branch merge.
  ```bash
  git branch --show-current
  git log --oneline -3
  ```
- **Estimated time**: 2 minutes
- **Success criterion**: Output shows `master`. Log shows a recent merge commit with message referencing `feature/zimwriter-libzim-activation` or `ZimWriter libzim integration`.
- **Rollback**: If not on master, run `git checkout master && git pull origin master`.

---

### A2. Install Python dependencies (including libzim)

- [ ] **Action**: Install all dependencies from the updated `pyproject.toml`, which now includes `libzim>=3.2,<4.0`.
  ```bash
  cd projects/open-repo/backend
  uv pip install -e ".[dev]"
  ```
- **Estimated time**: 3-8 minutes (first run downloads ~15 MB libzim wheel from PyPI; subsequent runs use cache and take < 30 seconds)
- **Success criterion**: Command exits with code 0. No error messages about failed dependencies or missing wheels.
- **Rollback**: If `libzim` wheel download fails for aarch64, try:
  ```bash
  uv pip install "libzim==3.10.0" --verbose
  # If still fails, check PyPI connectivity:
  curl -I https://pypi.org/pypi/libzim/json
  ```
  If the wheel genuinely is not available (unlikely — confirmed available), remove `"libzim>=3.2,<4.0"` from `pyproject.toml` temporarily and continue with stub mode. The 88 tests will still pass.

---

### A3. Verify libzim import succeeds

- [ ] **Action**: Confirm libzim is importable and the `_LIBZIM_AVAILABLE` flag will be `True`.
  ```bash
  uv run python -c "import libzim; print(libzim.__version__); from libzim.writer import Creator, Item, StringProvider, Hint; print('libzim OK')"
  ```
- **Estimated time**: 1 minute
- **Success criterion**: Output shows version string (e.g., `3.10.0`) followed by `libzim OK`. No ImportError.
- **Rollback**: If ImportError, re-run A2. If A2 succeeds but import still fails, there may be a virtual environment conflict. Run `uv run pip show libzim` to confirm the package is in the active environment.

---

### A4. Run baseline test suite (pre-change sanity check)

- [ ] **Action**: Run the full 88-test suite to confirm baseline passes before any code modifications.
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/ -v --tb=short 2>&1 | tail -20
  ```
- **Estimated time**: 2 minutes
- **Success criterion**: `88 passed` in the final summary line. Zero failures, zero errors.
- **Rollback**: If tests fail at baseline, the merge may have introduced a conflict. Do NOT proceed with implementation steps. Diagnose the failure with `uv run pytest tests/ -v --tb=long`.

---

### A5. Verify zim-tools is installed (or document its absence)

- [ ] **Action**: Check whether `zimcheck` binary is available.
  ```bash
  which zimcheck && zimcheck --version || echo "zimcheck NOT installed"
  ```
- **Estimated time**: 1 minute
- **Success criterion**: Either `zimcheck` path is printed (e.g., `/usr/bin/zimcheck`), or the message `zimcheck NOT installed` appears. Both outcomes are acceptable — absence is documented, not blocking.
- **If not installed**: Install with `sudo apt-get install zim-tools`. If apt fails, zimcheck validation can be deferred — ZimWriter handles its absence gracefully (logs warning, continues). Production exports should have zimcheck available; MVP testing can proceed without it.
- **Rollback**: N/A — this is a verification step, not a destructive action.

---

### A6. Verify Alembic migration state

- [ ] **Action**: Check current migration head to confirm migration 002 is the current state.
  ```bash
  cd projects/open-repo/backend
  uv run alembic current
  ```
- **Estimated time**: 1 minute
- **Success criterion**: Output shows `002 (head)` or similar indicating migration 002 is applied and 003 is pending.
- **Rollback**: If alembic cannot connect to database, check DB connection string in `alembic.ini` and ensure PostgreSQL is running. Migration state is separate from code — no rollback needed if only connectivity fails.

---

## Phase B: Code Changes (40-50 minutes)

These are the five code changes from the roadmap plus the `config_indexing` fix identified in the verification report. Apply them in order — Changes B2 through B5 depend on B2 (import guard).

---

### B1. Update pyproject.toml dependency (already applied by merge)

- [ ] **Action**: Verify `libzim>=3.2,<4.0` is present in `pyproject.toml`. (This was applied by the merge from the feature branch — this is a verification step, not a code change.)
  ```bash
  grep libzim projects/open-repo/backend/pyproject.toml
  ```
- **Estimated time**: 1 minute
- **Success criterion**: Output shows `"libzim>=3.2,<4.0"` in the dependencies list.
- **Rollback**: If line is absent (unlikely after merge), add it manually to `[project.dependencies]` in `pyproject.toml` and re-run A2.

---

### B2. Apply libzim import guard to zim_writer.py

- [ ] **Action**: Locate the line `from typing import Optional` in `backend/app/services/export/zim_writer.py`. After it, insert the libzim import guard block. The feature branch has this at lines 51-60. Key: do not add `_FALLBACK_ILLUSTRATION_PNG` — it is already present in master.
  ```python
  # ADD after "from typing import Optional":
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
- **Estimated time**: 8 minutes (read the file, locate insertion point, apply edit, verify no duplicate `_FALLBACK_ILLUSTRATION_PNG`)
- **Success criterion**: `uv run python -c "from app.services.export.zim_writer import _LIBZIM_AVAILABLE; print(_LIBZIM_AVAILABLE)"` prints `True`.
- **Rollback**: Revert the file with `git checkout projects/open-repo/backend/app/services/export/zim_writer.py`.

---

### B3. Insert ArticleItem adapter class

- [ ] **Action**: Locate the end of the `ZimEntry` dataclass (the `has_attribution()` method). After the closing of that class, insert the `ArticleItem` class block before the `ZimWriter` class definition.
  ```python
  class ArticleItem(Item):
      """
      Adapter from ZimEntry to libzim's Item interface.

      libzim.writer.Creator.add_item() requires an Item subclass.
      This class bridges ZimEntry (our data model) to libzim's API.

      Thread safety: Each ArticleItem instance is consumed once by add_item()
      and not retained. Thread-safe as long as the owning ZimWriter is
      called from a single thread (which ZimWriter docs enforce).
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
- **Estimated time**: 5 minutes
- **Success criterion**: `uv run python -c "from app.services.export.zim_writer import ArticleItem; print('ArticleItem OK')"` prints `ArticleItem OK`.
- **Rollback**: `git checkout projects/open-repo/backend/app/services/export/zim_writer.py`

---

### B4. Replace stub call in create_zim() with real Creator block (plus config_indexing fix)

- [ ] **Action**: In `ZimWriter.create_zim()`, locate the line `self._stub_write_placeholder()`. Replace it with the conditional block below. Include `creator.config_indexing(True, self.config.language_iso3)` as the first call inside the context manager (this is the critical fix from the verification report — it is NOT present on the feature branch and must be added manually):
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
          creator.config_indexing(True, self.config.language_iso3)  # enables Xapian FTS
          creator.set_mainpath("index")
          self._apply_metadata_to_creator(creator)
          for entry in self._entries:
              creator.add_item(ArticleItem(entry))
      # Creator.__exit__ triggers ZIM file finalization and write
  ```
- **Estimated time**: 15 minutes (locate target, apply replacement, verify surrounding code is intact)
- **Success criterion**: `uv run pytest tests/ -v --tb=short 2>&1 | tail -5` shows 88 passed. The `test_config_indexing_call_in_metadata_apply` test should pass.
- **Rollback**: `git checkout projects/open-repo/backend/app/services/export/zim_writer.py`. Re-run tests to confirm 88 still pass.

---

### B5. Clean up _apply_metadata_to_creator() (remove try/except wrapper)

- [ ] **Action**: In `ZimWriter._apply_metadata_to_creator()`, locate the `try:` block that wraps all `creator.add_metadata()` calls. Remove the `try:` and `except AttributeError: pass` lines, leaving the metadata calls directly in the method body (unindented one level). The feature branch has the clean version — use it as the reference.
  The clean method body should be:
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
      # Add illustration — required for zimcheck to pass
      illustration_bytes = self._get_illustration_bytes()
      if illustration_bytes:
          creator.add_illustration(48, illustration_bytes)
      else:
          creator.add_illustration(48, _FALLBACK_ILLUSTRATION_PNG)
  ```
- **Estimated time**: 5 minutes
- **Success criterion**: `uv run pytest tests/ -v --tb=short 2>&1 | tail -5` shows 88 passed. No new test failures from the try/except removal.
- **Rollback**: Re-add the `try: ... except AttributeError: pass` wrapper if any mock-based test now fails. Investigate whether the test is correctly checking for AttributeError or if a mock needs updating.

---

## Phase C: Test Verification (10-15 minutes)

---

### C1. Run full 88-test suite post-change

- [ ] **Action**: Run the complete test suite to confirm all changes together produce no regressions.
  ```bash
  cd projects/open-repo/backend
  uv run pytest tests/ -v --tb=short
  ```
- **Estimated time**: 2 minutes
- **Success criterion**: `88 passed` in final summary. Zero failures, zero errors, zero unexpected xfail.
- **Rollback**: If any test fails, revert the specific changed file with `git checkout [file]` and re-run tests to isolate which change caused the failure. Common failure modes:
  - `_stub_write_placeholder` tests: Check B4 was applied correctly (stub path still writes placeholder)
  - `ArticleItem` import test: Check B3 was applied after B2
  - `config_indexing` mock test: Check B4 includes the `config_indexing` call

---

### C2. Run export-specific tests with verbose output

- [ ] **Action**: Run only the ZIM export tests to get a focused view of the changes.
  ```bash
  uv run pytest tests/integration/test_export_pipeline.py -v
  ```
- **Estimated time**: 2 minutes
- **Success criterion**: All 88 tests in the file pass (the full test suite is in this one file for the export pipeline). Output shows class names including `TestZimMetadata`, `TestExportConfig`, `TestZimEntry`, `TestZimWriter`, `TestOPDSGenerator`, and `TestLibZIMIntegration`.
- **Rollback**: See C1 rollback plan.

---

### C3. Verify _LIBZIM_AVAILABLE flag state

- [ ] **Action**: Confirm that after installing libzim (step A2), the flag is True in the actual module.
  ```bash
  uv run python -c "
  from app.services.export.zim_writer import _LIBZIM_AVAILABLE, Creator
  print(f'_LIBZIM_AVAILABLE: {_LIBZIM_AVAILABLE}')
  print(f'Creator: {Creator}')
  "
  ```
- **Estimated time**: 1 minute
- **Success criterion**: Output shows `_LIBZIM_AVAILABLE: True` and `Creator: <class 'libzim.writer.Creator'>` (not `None`).
- **Rollback**: If `_LIBZIM_AVAILABLE: False`, libzim is not installed in the active environment. Re-run A2 and verify the virtual environment path matches what `uv run` uses.

---

## Phase D: Manual Verification (15-20 minutes)

These steps exercise the real libzim Creator path to confirm a ZIM file is actually produced.

---

### D1. Instantiate ZimWriter and call create_zim()

- [ ] **Action**: Run a manual smoke test that creates a minimal ZIM file using real libzim.
  ```bash
  uv run python -c "
  import tempfile
  from pathlib import Path
  from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

  with tempfile.TemporaryDirectory() as tmp:
      output = Path(tmp) / 'test.zim'
      metadata = ZimMetadata(
          title='Test ZIM',
          description='Smoke test export',
          language='eng',
          name='open-repo_en_nopic',
          flavour='nopic',
          creator='Test',
          publisher='Open-Repo',
          source_url='https://example.org',
      )
      config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour='nopic')
      writer = ZimWriter(metadata=metadata, config=config, output_path=output, zimcheck_binary=None)
      writer.add_article(
          path='agriculture/test-article',
          content='<html><head><title>Test</title></head><body><h1>Test Article</h1><p>Hello world.</p></body></html>',
          article_type='procedure',
          language='en',
      )
      result = writer.create_zim(run_zimcheck=False)
      print(f'ZIM file written: {result.file_size_bytes} bytes')
      print(f'SHA-256: {result.sha256[:16]}...')
      print(f'Article count: {result.article_count}')
      print('SMOKE TEST PASSED')
  "
  ```
- **Estimated time**: 5 minutes
- **Success criterion**: Output shows `SMOKE TEST PASSED`, file size > 1000 bytes (stub placeholder is ~100 bytes; real ZIM file should be much larger), and a valid SHA-256 hex string.
- **Rollback**: If an error is raised, capture the full traceback. Common failure modes:
  - `ZimCheckError`: `run_zimcheck=False` prevents this, but if you accidentally left `run_zimcheck=True`, try with `False`.
  - `AttributeError on Creator`: The import guard may have set `Creator = None`. Verify A3 and B2.
  - `RuntimeError: output directory does not exist`: The tempfile directory should exist — check Path construction.

---

### D2. Verify ZIM file has real content (not stub placeholder)

- [ ] **Action**: After D1, confirm the output file is a real ZIM binary (starts with ZIM magic bytes), not the stub placeholder text.
  ```bash
  uv run python -c "
  import tempfile
  from pathlib import Path
  from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

  with tempfile.TemporaryDirectory() as tmp:
      output = Path(tmp) / 'verify.zim'
      metadata = ZimMetadata(
          title='Verify ZIM',
          description='Byte verification test',
          language='eng',
          name='open-repo_en_nopic',
          flavour='nopic',
          creator='Test',
          publisher='Open-Repo',
          source_url='https://example.org',
      )
      config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour='nopic')
      writer = ZimWriter(metadata=metadata, config=config, output_path=output, zimcheck_binary=None)
      writer.add_article(path='test/article', content='<html><body><h1>Test</h1></body></html>', article_type='procedure')
      writer.create_zim(run_zimcheck=False)
      first_bytes = output.read_bytes()[:8]
      is_stub = first_bytes.startswith(b'STUB ZIM')
      is_real_zim = first_bytes[0] == 0x5a  # ZIM magic starts with 'Z' = 0x5a
      print(f'First 8 bytes: {first_bytes.hex()}')
      print(f'Is stub placeholder: {is_stub}')
      print(f'Starts with ZIM magic: {is_real_zim}')
      if is_stub:
          print('WARNING: Stub path was used — libzim Creator did not run')
      elif is_real_zim:
          print('CONFIRMED: Real ZIM file produced by libzim Creator')
  "
  ```
- **Estimated time**: 3 minutes
- **Success criterion**: Output shows `Is stub placeholder: False` and `Starts with ZIM magic: True`. First bytes are `5a494d04` (the ZIM format magic number `ZIM\x04`).
- **Rollback**: If `Is stub placeholder: True`, libzim is not being invoked. Check that B4 was applied and `_LIBZIM_AVAILABLE` is `True` per C3.

---

### D3. Run zimcheck on the test output (if zim-tools is installed)

- [ ] **Action**: If zimcheck is available (confirmed in A5), run it against the smoke test ZIM file. Skip this step if zimcheck is not installed.
  ```bash
  # Only run if A5 confirmed zimcheck is available
  uv run python -c "
  import tempfile
  from pathlib import Path
  from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

  with tempfile.TemporaryDirectory() as tmp:
      output = Path(tmp) / 'zimcheck-test.zim'
      metadata = ZimMetadata(
          title='Zimcheck Test',
          description='Validation smoke test',
          language='eng',
          name='open-repo_en_nopic',
          flavour='nopic',
          creator='Open-Repo Community',
          publisher='Open-Repo',
          source_url='https://example.org',
      )
      config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour='nopic')
      writer = ZimWriter(metadata=metadata, config=config, output_path=output)
      writer.add_article(path='agriculture/test', content='<html><body><h1>Test</h1></body></html>', article_type='procedure')
      result = writer.create_zim(run_zimcheck=True)
      print(f'zimcheck_passed: {result.zimcheck_passed}')
  "
  ```
- **Estimated time**: 3 minutes (including zimcheck execution time)
- **Success criterion**: Output shows `zimcheck_passed: True`. If zimcheck reports warnings about illustration dimensions (the fallback PNG is 1x1, not 48x48), this is expected and acceptable for MVP.
- **Rollback**: If `zimcheck_passed: False` and the file is renamed to `.zim.invalid`, inspect the zimcheck output logged at ERROR level. Common causes: description > 80 chars (check metadata), non-ASCII in Name field (check name regex), missing mainpath. Adjust the test metadata or the ZimWriter code and retry.

---

## Phase E: Database Migration (5-10 minutes)

---

### E1. Apply Alembic migration 003

- [ ] **Action**: Apply the `zim_exports` table migration.
  ```bash
  cd projects/open-repo/backend
  uv run alembic upgrade head
  ```
- **Estimated time**: 2 minutes
- **Success criterion**: Output contains `Running upgrade 002 -> 003` and no errors. `uv run alembic current` shows `003 (head)`.
- **Rollback**: `uv run alembic downgrade 002` drops the `zim_exports` table and returns to migration 002 state.

---

### E2. Verify table was created

- [ ] **Action**: Confirm the `zim_exports` table exists in the database with the expected columns.
  ```bash
  # If using psql directly:
  # psql $DATABASE_URL -c "\d zim_exports"
  # Or via Python:
  uv run python -c "
  from sqlalchemy import create_engine, text, inspect
  import os
  engine = create_engine(os.environ['DATABASE_URL'])
  inspector = inspect(engine)
  cols = [c['name'] for c in inspector.get_columns('zim_exports')]
  print(f'Columns: {cols}')
  print(f'Column count: {len(cols)}')
  "
  ```
- **Estimated time**: 2 minutes
- **Success criterion**: 23 columns are listed including `id`, `zim_uuid`, `name`, `flavour`, `language`, `period`, `status`, `is_current`, `sha256`. Column count = 23.
- **Rollback**: If migration failed, check database connectivity and run `uv run alembic upgrade head --sql` to preview the SQL without applying it.

---

## Phase F: Docker/Deployment Verification (10-15 minutes)

---

### F1. Restart the API service and confirm health endpoint

- [ ] **Action**: Restart the API container/service and verify it starts without import errors.
  ```bash
  # If using Docker Compose:
  docker compose restart api
  # Wait 5-10 seconds, then:
  curl -s http://127.0.0.1:8000/health | python3 -m json.tool
  ```
- **Estimated time**: 5 minutes
- **Success criterion**: `curl` returns HTTP 200 with a JSON body indicating the API is healthy. No `ImportError` or `ModuleNotFoundError` lines in the Docker logs (`docker compose logs api --tail=20`).
- **Rollback**: If the API fails to start due to an import error in `zim_writer.py`, check whether the libzim wheel is installed inside the Docker container. The Docker image may need to be rebuilt with `docker compose build api` to include the updated `pyproject.toml`.

---

### F2. Verify libzim is available inside the container

- [ ] **Action**: Confirm libzim is installed in the Docker container's Python environment.
  ```bash
  docker compose exec api python -c "import libzim; print(libzim.__version__)"
  ```
- **Estimated time**: 1 minute
- **Success criterion**: Output shows `3.10.0` (or the current latest version).
- **Rollback**: If ImportError, rebuild the container image with `docker compose build api` to trigger `uv pip install -e ".[dev]"` inside the image. Ensure the `Dockerfile` runs the install step against the updated `pyproject.toml`.

---

### F3. Confirm API logs show no ZimWriter errors on startup

- [ ] **Action**: Check the startup logs for any ZimWriter-related warnings or errors.
  ```bash
  docker compose logs api --tail=50 | grep -i "zim\|libzim\|import"
  ```
- **Estimated time**: 1 minute
- **Success criterion**: No `ImportError`, no `ModuleNotFoundError`, no `ERROR` lines referencing zim_writer. A line like `INFO: _LIBZIM_AVAILABLE = True` (if logging is configured for module-level messages) is a positive signal.
- **Rollback**: N/A — this is observation only.

---

## Phase G: Commit and Branch Management (5 minutes)

---

### G1. Stage and commit all changes

- [ ] **Action**: Stage the modified `zim_writer.py` and commit the Phase 5.1 activation.
  ```bash
  git add projects/open-repo/backend/app/services/export/zim_writer.py
  git add projects/open-repo/backend/pyproject.toml
  git status
  git commit -m "feat(open-repo): activate libzim Creator in ZimWriter — Phase 5.1 production path"
  ```
- **Estimated time**: 3 minutes
- **Success criterion**: `git status` shows clean working tree after commit. `git log --oneline -3` shows the new commit at HEAD.
- **Rollback**: `git reset HEAD~1` to undo the commit if needed.

---

### G2. Document completion in CHECKIN.md

- [ ] **Action**: Update `CHECKIN.md` to reflect that Phase 5 Candidate 1 implementation is complete and the libzim stub has been activated. Note the three post-activation items remaining (html.escape(), ZimExport ORM, HTML render function).
- **Estimated time**: 2 minutes
- **Success criterion**: CHECKIN.md reflects the current state and remaining post-activation items are listed.

---

## Summary: Time Accounting

| Phase | Steps | Estimated time |
|-------|-------|---------------|
| A: Environment verification | A1-A6 | 15-20 minutes |
| B: Code changes | B1-B5 | 40-50 minutes |
| C: Test verification | C1-C3 | 10-15 minutes |
| D: Manual verification | D1-D3 | 10-15 minutes |
| E: Database migration | E1-E2 | 5-10 minutes |
| F: Docker/deployment | F1-F3 | 10-15 minutes |
| G: Commit and cleanup | G1-G2 | 5 minutes |
| **TOTAL** | | **95-130 minutes** |

This range maps to approximately 90-120 minutes under good conditions (no environment issues, no Docker rebuild required). Budget 2.5 hours if building Docker image from scratch.

---

## Post-Checklist: Remaining Activation Items

After completing this checklist, the ZimWriter libzim activation is production-ready for local-only exports. Three items remain before enabling federated content exports and the full OPDS catalog:

1. **html.escape() fix** (10 min): Apply HTML escaping to `source_node_name`, `source_node_url`, `license_name` in `_apply_attribution_footer()`. Required before any export that includes federated partner content.

2. **ZimExport ORM model** (45 min): Add `ZimExport` SQLAlchemy class to `backend/app/models.py` mirroring the `zim_exports` table schema from migration 003. Required before the export service can log completed jobs to the database.

3. **HTML render function** (2-4 hr): Write a function that converts `ContentItem.content_jsonld` (structured JSON-LD) to a self-contained HTML string suitable for passing to `add_article()`. This is the primary remaining Phase 5.2 implementation task.

These three items can be a separate follow-up PR after the Phase 5.1 merge.
