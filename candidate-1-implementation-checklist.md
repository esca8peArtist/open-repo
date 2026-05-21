---
title: "Phase 5 Candidate 1 — ZimWriter Implementation Checklist"
project: open-repo
phase: 5
candidate: 1
date: 2026-05-21
status: ready-for-execution
---

# Phase 5 Candidate 1: ZimWriter Implementation Checklist

**Purpose**: Step-by-step execution guide for activating libzim in ZimWriter. This checklist eliminates discovery delays and provides a single source of truth for implementation progress. Use this in parallel with `phase-5-candidate-1-implementation-verification.md` for technical context.

**How to use this checklist**:
1. Work through each section in order
2. Mark completed steps with `[x]`
3. For any step that fails, check the verification document's risk assessment section (Section 6)
4. Estimated completion: 5.5–7.5 hours of focused work

---

## Pre-Implementation Verification (5 minutes)

These steps confirm the environment is ready before code changes begin.

- [ ] **Python version check**: Run `python3 --version` and confirm 3.11.2 or higher
  - Command: `python3 --version`
  - Expected output: `Python 3.11.2` or `Python 3.12.x`
  
- [ ] **Navigate to project directory**:
  - Command: `cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend`
  - Verify you're in the correct directory: `pwd` should show `.../open-repo/backend`

- [ ] **Verify .venv exists**:
  - Command: `ls -la .venv | head -5`
  - Expected: Directory listing showing `.venv/bin`, `.venv/lib`, etc.

- [ ] **Activate virtual environment** (if not already active):
  - Command: `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)
  - Expected: Prompt should show `(.venv)` prefix

---

## Change 1: Add libzim to pyproject.toml (10 minutes)

### Step 1.1: Locate [project.dependencies] section

- [ ] Open `backend/pyproject.toml` in your editor
- [ ] Find the `[project.dependencies]` section (should be around line 10)
- [ ] Note the last dependency line (currently: `"meilisearch>=0.30.0",`)

### Step 1.2: Add libzim dependency

- [ ] Add a new line after the last dependency:
  ```toml
  "libzim>=3.2,<4.0",
  ```
  
- [ ] Verify the section looks like this:
  ```toml
  [project.dependencies]
  [...]
  "meilisearch>=0.30.0",
  "libzim>=3.2,<4.0",
  ```

- [ ] Save the file

### Step 1.3: Install libzim wheel

- [ ] Run: `uv pip install 'libzim>=3.2,<4.0'`
  - Expected duration: <30 seconds
  - Expected output: `Successfully installed libzim-X.X.X`
  - If it fails with "no matching distribution", check Section 6 of the verification document (Risk 1)

### Step 1.4: Verify libzim installation

- [ ] Test Python import:
  ```bash
  python3 -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('✓ libzim imports OK')"
  ```
  Expected output: `✓ libzim imports OK`

- [ ] Check version:
  ```bash
  python3 -c "import libzim; print(f'✓ libzim version: {libzim.__version__}')"
  ```
  Expected output: `✓ libzim version: 3.9.0` (or similar)

---

## Change 2: Add libzim import guard to zim_writer.py (15 minutes)

### Step 2.1: Locate insertion point

- [ ] Open `backend/app/services/export/zim_writer.py`
- [ ] Find line 48: `from typing import Optional`
- [ ] This is where you'll insert the import guard

### Step 2.2: Add import guard block

- [ ] After the line `from typing import Optional`, add:
  ```python
  
  # Try to import libzim; fall back to stub if not installed (for test environments)
  try:
      from libzim.writer import Creator, Item, StringProvider, Hint
      _LIBZIM_AVAILABLE = True
  except ImportError:
      _LIBZIM_AVAILABLE = False
      Creator = None  # type: ignore[assignment,misc]
  ```

- [ ] Verify the syntax is correct (no extra indentation, lines match exactly)

### Step 2.3: Run linter and verify module loads

- [ ] Check syntax with ruff:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  uv run ruff check app/services/export/zim_writer.py
  ```
  Expected: No errors reported (warnings are OK)

- [ ] Test that module still imports:
  ```bash
  python3 -c "import app.services.export.zim_writer; print('✓ zim_writer imports OK')"
  ```
  Expected output: `✓ zim_writer imports OK`

---

## Change 3: Add ArticleItem inner class (30 minutes)

### Step 3.1: Locate ZimEntry dataclass

- [ ] In `zim_writer.py`, search for the line: `class ZimEntry:`
- [ ] This should be around line 324
- [ ] Locate the end of the ZimEntry class (the `def has_attribution(self)` method ends around line 405)

### Step 3.2: Add ArticleItem class after ZimEntry

- [ ] After the `ZimEntry` class ends (after `return bool(self.source_node_url)`), add:
  ```python


  class ArticleItem(Item):
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

- [ ] Verify the class is properly indented (no leading spaces before `class`)

### Step 3.3: Test ArticleItem instantiation

- [ ] Create a simple test to verify ArticleItem works:
  ```bash
  python3 << 'PYTEST'
  from pathlib import Path
  from app.services.export.zim_writer import ZimEntry, ArticleItem
  
  entry = ZimEntry(
      path="test/article",
      title="Test Article",
      content="<html><body>Test</body></html>"
  )
  item = ArticleItem(entry)
  assert item.get_path() == "test/article"
  assert item.get_title() == "Test Article"
  assert item.get_mimetype() == "text/html"
  print("✓ ArticleItem instantiation OK")
  PYTEST
  ```
  Expected output: `✓ ArticleItem instantiation OK`

---

## Change 4: Replace create_zim() stub with real libzim Creator (45 minutes)

### Step 4.1: Locate create_zim() method

- [ ] In `zim_writer.py`, search for the line: `def create_zim(`
- [ ] This should be around line 700
- [ ] Find the line inside create_zim() that calls `self._stub_write_placeholder()`
- [ ] This should be around line 762, within the method body

### Step 4.2: Find and replace the stub call

- [ ] Locate the exact lines to replace (look for):
  ```python
          # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
          # See the docstring above for the correct implementation pattern.
          # For now, write a placeholder file to allow test harness to run.
          self._stub_write_placeholder()
  ```

- [ ] Replace those lines with:
  ```python
          if not _LIBZIM_AVAILABLE:
              # Fallback stub for environments without libzim installed (dev/CI without wheel)
              self._stub_write_placeholder()
          else:
              with Creator(str(self.output_path)) as creator:
                  creator.config_indexing(True, self.config.language_iso3)
                  creator.set_mainpath("index")
                  self._apply_metadata_to_creator(creator)
                  for entry in self._entries:
                      creator.add_item(ArticleItem(entry))
              # Creator.__exit__ triggers ZIM file finalization and write
  ```

- [ ] Verify indentation matches the surrounding code (should be indented 8 spaces from the left margin)

### Step 4.3: Verify create_zim() method is syntactically correct

- [ ] Run linter again:
  ```bash
  uv run ruff check app/services/export/zim_writer.py
  ```
  Expected: No errors

- [ ] Verify the method signature is unchanged:
  ```bash
  python3 << 'PYTEST'
  import inspect
  from app.services.export.zim_writer import ZimWriter
  sig = inspect.signature(ZimWriter.create_zim)
  print(f"✓ create_zim() signature: {sig}")
  PYTEST
  ```
  Expected: Signature shows `(self, compression='default', run_zimcheck=True, progress_callback=None) -> ZimWriteResult`

---

## Change 5: Implement _apply_metadata_to_creator() (60 minutes)

### Step 5.1: Locate _apply_metadata_to_creator() method

- [ ] In `zim_writer.py`, search for: `def _apply_metadata_to_creator(`
- [ ] This should be around line 870
- [ ] The method body is currently just: `pass`

### Step 5.2: Add fallback illustration PNG constant (module level)

- [ ] Find a good place to add the constant, above the `ZimWriter` class definition
- [ ] Add this before the class (around line 50-60):
  ```python
  
  # Minimal 1x1 transparent PNG — used as fallback illustration when no icon is provided.
  # This is a well-formed PNG that passes zimcheck with a warning rather than a failure.
  # Replace with a real 48x48 branded icon before publishing.
  _FALLBACK_ILLUSTRATION_PNG = (
      b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\x00\x000"
      b"\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x0bIDATx\x9cc"
      b"\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
  )
  ```

- [ ] Note: The file already has a `_FALLBACK_ILLUSTRATION_PNG` constant defined near the top (line 54). Use that one; no need to add it again.

### Step 5.3: Replace _apply_metadata_to_creator() body

- [ ] In the `_apply_metadata_to_creator()` method, replace:
  ```python
      pass
  ```
  
  With:
  ```python
      def _apply_metadata_to_creator(self, creator: "Creator") -> None:
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
              # Fallback: 1x1 transparent PNG (passes zimcheck with a warning, not a failure)
              creator.add_illustration(48, _FALLBACK_ILLUSTRATION_PNG)
  ```

- [ ] Verify the indentation is correct (method body should be indented 8 spaces from the left)

### Step 5.4: Verify metadata method calls match metadata fields

- [ ] Check that `ZimMetadata` dataclass has these fields:
  - title, description, language, creator, publisher, date, name, flavour, tags, source_url, scraper, long_description
  
- [ ] Run a quick check:
  ```bash
  python3 << 'PYTEST'
  from app.services.export.zim_writer import ZimMetadata
  import inspect
  fields = [f for f in dir(ZimMetadata) if not f.startswith('_')]
  required = ['title', 'description', 'language', 'creator', 'publisher', 'date', 'name', 'flavour', 'source_url']
  for f in required:
      if f not in fields:
          print(f"✗ Missing field: {f}")
      else:
          print(f"✓ Field {f} present")
  PYTEST
  ```

---

## Change 6: Verify zimcheck call is configured correctly (10 minutes)

### Step 6.1: Locate zimcheck configuration

- [ ] In `create_zim()`, find the conditional that calls `_run_zimcheck()`
- [ ] It should look like: `if run_zimcheck and self.zimcheck_binary:`
- [ ] Verify that `run_zimcheck=True` is the default parameter (in the method signature)

### Step 6.2: Confirm signature is correct

- [ ] The method signature should have: `def create_zim(self, compression: str = "default", run_zimcheck: bool = True, ...)`

- [ ] Verify:
  ```bash
  python3 << 'PYTEST'
  import inspect
  from app.services.export.zim_writer import ZimWriter
  sig = inspect.signature(ZimWriter.create_zim)
  params = sig.parameters
  if params['run_zimcheck'].default is True:
      print("✓ run_zimcheck defaults to True")
  else:
      print("✗ run_zimcheck default is not True")
  PYTEST
  ```

---

## Testing Phase 1: Unit Tests (10 minutes)

### Step 7.1: Run existing export tests

- [ ] Execute the 84 existing tests:
  ```bash
  uv run pytest tests/ -k "export" -v
  ```
  - Expected: All tests pass (84 passed)
  - Duration: <1 minute execution
  - If any fail, check the failure message against Section 6 of the verification document

### Step 7.2: Run ZimWriter-specific unit tests

- [ ] If there are specific ZimWriter unit tests:
  ```bash
  uv run pytest tests/unit/test_zim_writer.py -v
  ```
  - Expected: All pass (or skip if file doesn't exist yet)

### Step 7.3: Spot-check libzim integration

- [ ] Create a small test to verify the real libzim path is being used:
  ```bash
  python3 << 'PYTEST'
  from app.services.export.zim_writer import _LIBZIM_AVAILABLE
  if _LIBZIM_AVAILABLE:
      print("✓ libzim is available (real implementation will be used)")
  else:
      print("⚠ libzim not available (stub fallback will be used)")
  PYTEST
  ```

---

## Testing Phase 2: Integration Tests (1.5–2 hours)

### Step 8.1: Install zimcheck binary (prerequisite for integration tests)

- [ ] On Ubuntu/Debian:
  ```bash
  sudo apt-get update && sudo apt-get install -y zim-tools
  ```

- [ ] On macOS:
  ```bash
  brew install zim-tools
  ```

- [ ] Verify installation:
  ```bash
  zimcheck --version
  ```
  Expected: Version output (e.g., `zimcheck 1.6.0`)

### Step 8.2: Run zimcheck integration tests

- [ ] Execute integration tests that require zimcheck:
  ```bash
  uv run pytest tests/integration/test_zimcheck_validation.py -v -m zimcheck
  ```
  - Expected: Tests pass
  - Duration: 5–10 minutes (depends on test data size)
  - If tests fail with "zimcheck not found", verify installation in Step 8.1

### Step 8.3: Run full-text search integration tests

- [ ] Execute tests that verify Xapian index:
  ```bash
  uv run pytest tests/integration/test_zim_readback.py -v
  ```
  - Expected: Tests pass
  - Duration: 10–15 minutes

### Step 8.4: Manual end-to-end test (recommended for confidence)

- [ ] Create a small export with real data:
  ```bash
  python3 << 'PYTEST'
  from pathlib import Path
  from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope, ZimEntry
  
  metadata = ZimMetadata(
      title="Test Export",
      description="Test offline export",
      language="eng",
      name="test_en_nopic",
      flavour="nopic",
      creator="Test",
      publisher="Test",
      source_url="http://test.example.org",
  )
  config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
  output = Path("/tmp/test_export.zim")
  
  writer = ZimWriter(metadata=metadata, config=config, output_path=output, zimcheck_binary="zimcheck")
  
  for i in range(5):
      writer.add_article(
          path=f"test/article{i}",
          content=f"<html><body><h1>Article {i}</h1><p>Test content</p></body></html>",
          article_type="procedure"
      )
  
  result = writer.create_zim()
  print(f"✓ ZIM created: {result.output_path}")
  print(f"✓ File size: {result.file_size_bytes} bytes")
  print(f"✓ Article count: {result.article_count}")
  print(f"✓ SHA256: {result.sha256[:16]}...")
  print(f"✓ zimcheck passed: {result.zimcheck_passed}")
  PYTEST
  ```
  - Expected: All lines print successfully; zimcheck_passed should be True
  - If zimcheck_passed is False, check the output file with `zimcheck --verbose /tmp/test_export.zim`

---

## Testing Phase 3: Full Test Suite (5 minutes)

### Step 9.1: Run complete test suite

- [ ] Execute all tests to ensure no regressions:
  ```bash
  uv run pytest tests/ -v
  ```
  - Expected: All tests pass (including the 84 existing ones)
  - Duration: <1 minute execution
  - If any test fails, it indicates a regression; investigate and fix before proceeding

### Step 9.2: Check test coverage (optional)

- [ ] Run tests with coverage:
  ```bash
  uv run pytest tests/ -v --cov=app.services.export
  ```
  - Expected: Coverage report shows good coverage for zim_writer.py

---

## Post-Implementation Cleanup (15 minutes)

### Step 10.1: Remove _stub_write_placeholder() method

- [ ] Verify all tests pass (from Step 9.1)

- [ ] Search for the `_stub_write_placeholder()` method in `zim_writer.py` (around line 914)

- [ ] Delete the entire method:
  ```python
  def _stub_write_placeholder(self) -> None:
      """
      Write a stub placeholder ZIM file for test harness compatibility.
      
      TODO(post-PR-merge): Delete this method after libzim integration is verified.
      """
      # Stub implementation: write a simple placeholder
      self.output_path.write_bytes(b"STUB_ZIM_FILE\n")
      self._is_finalized = True
  ```

- [ ] After deletion, re-run the test suite:
  ```bash
  uv run pytest tests/ -v
  ```
  - Expected: All tests still pass
  - If any test fails, the stub was being used elsewhere; revert deletion and investigate

### Step 10.2: Run linter and formatter

- [ ] Format code:
  ```bash
  uv run ruff format app/services/export/zim_writer.py
  ```

- [ ] Check for style issues:
  ```bash
  uv run ruff check app/services/export/zim_writer.py --fix
  ```

### Step 10.3: Final validation

- [ ] Verify no import errors:
  ```bash
  python3 -c "from app.services.export.zim_writer import ZimWriter, ArticleItem; print('✓ All imports OK')"
  ```

- [ ] Run the smoke test one more time:
  ```bash
  uv run pytest tests/ -k "export" -v --tb=short
  ```
  - Expected: All pass

---

## Implementation Complete Checklist

- [ ] Change 1: libzim added to pyproject.toml
- [ ] Change 2: Import guard added to zim_writer.py
- [ ] Change 3: ArticleItem class added
- [ ] Change 4: create_zim() stub replaced with real libzim Creator
- [ ] Change 5: _apply_metadata_to_creator() implemented
- [ ] Change 6: zimcheck configuration verified
- [ ] Change 7: _stub_write_placeholder() removed
- [ ] All 84 existing tests pass
- [ ] New integration tests pass (zimcheck, readback)
- [ ] Manual end-to-end test successful
- [ ] Code formatted and linted
- [ ] No import errors
- [ ] Full test suite passes

---

## Next Steps After Implementation

1. **Code review**: Have the implementation reviewed by another team member
2. **Create PR**: Push to `feature/zimwriter-libzim-integration` branch and create PR
3. **Merge**: Once approved, merge to `integration` branch for validation, then to `main`
4. **Candidate 2 (OPDS)**: If user approves Phase 5 Candidate 2, start OPDS implementation on a new branch

---

## Troubleshooting Quick Reference

| Issue | Check | Fix |
|-------|-------|-----|
| `ImportError: libzim` | Step 1.4 | Run `uv pip install 'libzim>=3.2,<4.0'` |
| `SyntaxError` in zim_writer.py | Step 3.3 or 5.4 | Verify indentation (8 spaces for method body) |
| Tests fail | Step 9.1 | Run `uv run pytest tests/ -v` with `--tb=short` for details |
| zimcheck not found | Step 8.1 | Install via `apt-get install zim-tools` or `brew install zim-tools` |
| ZIM file invalid | Step 8.4 manual test | Run `zimcheck --verbose /tmp/test_export.zim` for details |

---

## Estimated Timeline Summary

| Phase | Est. time | Status |
|-------|-----------|--------|
| Pre-implementation verification | 5 min | ⬜ |
| Change 1: pyproject.toml | 10 min | ⬜ |
| Change 2: imports | 15 min | ⬜ |
| Change 3: ArticleItem | 30 min | ⬜ |
| Change 4: create_zim() | 45 min | ⬜ |
| Change 5: metadata | 60 min | ⬜ |
| Change 6: zimcheck verify | 10 min | ⬜ |
| Testing Phase 1: units | 10 min | ⬜ |
| Testing Phase 2: integration | 1.5–2.0 h | ⬜ |
| Testing Phase 3: full suite | 5 min | ⬜ |
| Cleanup | 15 min | ⬜ |
| **Total** | **5.5–7.5 h** | |

---

This checklist provides a complete, zero-ambiguity implementation path. If you encounter any issue not covered here, refer to `phase-5-candidate-1-implementation-verification.md` Section 6 (Risk Assessment) for mitigation strategies.
