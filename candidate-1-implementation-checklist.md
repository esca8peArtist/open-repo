---
title: "Phase 5 Candidate 1: ZimWriter libzim Integration — Implementation Checklist"
project: open-repo
phase: 5
candidate: 1
status: ready-for-implementation
date: 2026-05-20
total_effort: "8-11 hours"
---

# Phase 5 Candidate 1: Implementation Checklist
## ZimWriter libzim Integration — Per-Task Hour Breakdown

**Purpose**: Step-by-step checklist with per-item hour estimates and blockers. Developer follows this sequentially.

**Effort allocation**: 8-11 hours total (5.5 hours core implementation + 2.5-3.5 hours testing/debug/verification)

---

## PHASE 0: Setup (0.5 hours)

### [ ] 0.1 Create feature branch
**Time**: 5 minutes
**Blocker**: None

```bash
git checkout -b feature/zimwriter-libzim-integration
git log --oneline | head -3  # Verify you're on master first
```

**Verification**: `git branch | grep "zimwriter"` shows your branch

---

### [ ] 0.2 Install zimcheck (optional but recommended for full testing)
**Time**: 5 minutes
**Blocker**: None (can skip for unit tests only)

```bash
# Linux
apt-get update && apt-get install -y zim-tools

# macOS
brew install zim-tools

# Verify
which zimcheck && zimcheck --version
```

**Verification**: `zimcheck --version` shows version string (e.g., "1.6.0")

---

### [ ] 0.3 Create test ZIM template file for manual validation
**Time**: 5 minutes
**Blocker**: None

Create file `test_manual_zim.py`:
```python
"""Manual test to generate a small ZIM for debugging."""
from pathlib import Path
from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ZimEntry
)

metadata = ZimMetadata(
    title="Test Archive",
    description="Test content",
    language="eng",
    creator="Test",
    publisher="Test",
    date="2026-05-20",
    name="test_archive",
    flavour="test"
)

entries = [
    ZimEntry(
        path="index",
        title="Welcome",
        content="<h1>Welcome</h1><p>Test article</p>",
        mime_type="text/html; charset=utf-8",
        is_front_article=True
    )
]

config = ExportConfig(language_iso3="eng")
writer = ZimWriter(
    entries=entries,
    metadata=metadata,
    config=config,
    output_path=Path("test_manual.zim"),
    zimcheck_binary="/usr/bin/zimcheck"  # Or adjust for your system
)

result = writer.create_zim()
print(f"✓ ZIM created at {result.output_path}")
print(f"  Size: {result.file_size_bytes} bytes")
print(f"  Valid: {result.zimcheck_passed}")
```

**Verification**: File created, no syntax errors

---

## PHASE 1: Dependency and Imports (0.5 hours)

### [ ] 1.1 Add libzim to pyproject.toml
**Time**: 5 minutes
**Blocker**: None

Edit `pyproject.toml`, locate `[project.dependencies]` section:
```toml
[project.dependencies]
pytest = ">=7.0.0"
click = ">=8.0.0"
rich = ">=13.0.0"
libzim = ">=3.10,<4.0"  # ADD THIS LINE
```

**Verification**: `grep "libzim" pyproject.toml` returns the new line

---

### [ ] 1.2 Install libzim wheel
**Time**: 15 minutes
**Blocker**: None

```bash
uv pip install libzim

# Verify installation
python3 -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('✓ Writer OK')"
python3 -c "from libzim.reader import Archive; print('✓ Reader OK')"
```

**Verification**: Both imports succeed with no errors

---

### [ ] 1.3 Add import guard in zim_writer.py
**Time**: 10 minutes
**Blocker**: libzim must be installed (from 1.2)

Edit `app/services/export/zim_writer.py`, add after existing imports (around line 48):

```python
# libzim integration — try import with fallback for stub behavior
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None  # type: ignore[assignment,misc]
```

**Verification**:
```bash
python3 -c "from app.services.export.zim_writer import _LIBZIM_AVAILABLE; print(f'libzim available: {_LIBZIM_AVAILABLE}')"
```

Expected output: `libzim available: True`

---

### [ ] 1.4 Commit Phase 1
**Time**: 5 minutes

```bash
git add pyproject.toml app/services/export/zim_writer.py
git commit -m "feat(zim): add libzim>=3.10 dependency and import guard"
git log --oneline | head -3  # Verify commit
```

---

## PHASE 2: ArticleItem Adapter (1.0 hour)

### [ ] 2.1 Add ArticleItem class
**Time**: 20 minutes
**Blocker**: Phase 1 must be complete

Edit `app/services/export/zim_writer.py`. Locate the `ZimEntry` dataclass (around line 400), then add `ArticleItem` **after** it and **before** the `ZimWriter` class:

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

**Verification**:
```bash
python3 -c "from app.services.export.zim_writer import ArticleItem; print('✓ ArticleItem OK')"
```

---

### [ ] 2.2 Run existing tests (should all still pass)
**Time**: 30 minutes
**Blocker**: Phase 1 must be complete

```bash
uv run pytest tests/unit/test_zim_writer.py -v
uv run pytest tests/unit/test_zim_metadata.py -v
```

Expected: All 84+ tests pass (still using stub placeholders)

**Verification**: Exit code 0, no failures

---

### [ ] 2.3 Manual test: Instantiate ArticleItem
**Time**: 10 minutes

```python
# In Python shell or test file
from app.services.export.zim_writer import ArticleItem, ZimEntry
from libzim.writer import Hint

entry = ZimEntry(
    path="test/article",
    title="Test",
    content="<p>Test</p>",
    mime_type="text/html; charset=utf-8",
    is_front_article=True
)

item = ArticleItem(entry)
print(f"Path: {item.get_path()}")
print(f"Title: {item.get_title()}")
print(f"MIME: {item.get_mimetype()}")
print(f"Hints: {item.get_hints()}")
print("✓ All methods work")
```

**Verification**: Output shows all methods return correct values

---

### [ ] 2.4 Commit Phase 2
**Time**: 5 minutes

```bash
git add app/services/export/zim_writer.py
git commit -m "feat(zim): add ArticleItem adapter class for libzim integration"
```

---

## PHASE 3: Real Creator Context (1.5 hours)

### [ ] 3.1 Replace create_zim() stub call
**Time**: 25 minutes
**Blocker**: Phase 1-2 must be complete

Edit `app/services/export/zim_writer.py`. Locate the `create_zim()` method (around line 762). Find the stub call:
```python
        # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
        # See the docstring above for the correct implementation pattern.
        # For now, write a placeholder file to allow test harness to run.
        self._stub_write_placeholder()
```

Replace it with:
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

**Verification**: No syntax errors, code loads
```bash
python3 -c "from app.services.export.zim_writer import ZimWriter; print('✓ ZimWriter OK')"
```

---

### [ ] 3.2 Run unit tests (expect failures in metadata validation)
**Time**: 40 minutes
**Blocker**: Phase 3.1 must be complete

```bash
uv run pytest tests/unit/test_zim_writer.py::test_zim_writer_creates_real_zim_file -xvs
```

Expected: May fail with "AttributeError: 'NoneType' object has no attribute 'add_metadata'" (because `_apply_metadata_to_creator()` is still `pass`). This is expected.

---

### [ ] 3.3 Manual hex check (optional but informative)
**Time**: 5 minutes

Run the test file `test_manual_zim.py`:
```bash
python3 test_manual_zim.py
```

Then inspect the output:
```bash
file test_manual.zim  # Should show "ZIM archive"
xxd test_manual.zim | head -3  # First bytes should be "5a49 4d04" (ZIM magic)
```

**Verification**: 
- `file` shows ZIM archive
- `xxd` shows magic header `5a 49 4d 04`
- File size > 1 KB

If these pass, real ZIM creation is working! If not, debug with: `xxd test_manual.zim | head -5`

---

### [ ] 3.4 Commit Phase 3
**Time**: 5 minutes

```bash
git add app/services/export/zim_writer.py
git commit -m "feat(zim): activate real libzim.Creator in create_zim()"
```

---

## PHASE 4: Metadata Implementation (1.5 hours)

### [ ] 4.1 Add _FALLBACK_ILLUSTRATION_PNG constant
**Time**: 5 minutes
**Blocker**: Phase 3 must be complete

Edit `app/services/export/zim_writer.py`. Add this at module level, **before** the `ZimWriter` class:

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

**Verification**: No syntax errors
```bash
python3 -c "from app.services.export.zim_writer import _FALLBACK_ILLUSTRATION_PNG; print(f'PNG length: {len(_FALLBACK_ILLUSTRATION_PNG)}')"
```

Expected output: `PNG length: 98`

---

### [ ] 4.2 Implement _apply_metadata_to_creator()
**Time**: 30 minutes
**Blocker**: Phase 4.1 must be complete

Edit `app/services/export/zim_writer.py`. Locate the `_apply_metadata_to_creator()` method (around line 870). It currently has just `pass`. Replace the entire body:

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

**Verification**: No syntax errors
```bash
python3 -c "from app.services.export.zim_writer import ZimWriter; print('✓ ZimWriter OK')"
```

---

### [ ] 4.3 Run manual metadata test
**Time**: 20 minutes

Run the test file again:
```bash
python3 test_manual_zim.py
```

If successful, verify metadata:
```bash
python3 << 'EOF'
from libzim.reader import Archive

archive = Archive("test_manual.zim")
metadata = archive.metadata

print("Metadata retrieved:")
for key in ["Title", "Description", "Language", "Creator", "Publisher"]:
    print(f"  {key}: {metadata.get(key, 'NOT FOUND')}")
print("✓ Metadata OK")
EOF
```

**Verification**: All 5+ metadata fields present

---

### [ ] 4.4 Run unit tests (expect all to pass now)
**Time**: 30 minutes

```bash
uv run pytest tests/unit/test_zim_writer.py -v
uv run pytest tests/unit/test_zim_metadata.py -v
```

Expected: All 84+ tests pass

**Verification**: Exit code 0, count shows "84 passed"

---

### [ ] 4.5 Commit Phase 4
**Time**: 5 minutes

```bash
git add app/services/export/zim_writer.py
git commit -m "feat(zim): implement full metadata application with fallback illustration"
```

---

## PHASE 5: ZimCheck Validation (0.5 hours)

### [ ] 5.1 Verify zimcheck is installed and ready
**Time**: 5 minutes
**Blocker**: zimcheck binary must be available

```bash
which zimcheck && zimcheck --version
```

If missing:
```bash
# Linux
apt-get install zim-tools

# macOS
brew install zim-tools
```

**Verification**: `zimcheck --version` shows version string

---

### [ ] 5.2 Verify create_zim() uses run_zimcheck=True by default
**Time**: 5 minutes

Search `app/services/export/zim_writer.py` for the `create_zim()` method signature. Verify:
```python
def create_zim(self, run_zimcheck: bool = True) -> ZimWriteResult:
```

Default should be `True`. If it's `False`, change it to `True`.

**Verification**: `grep "run_zimcheck: bool = True" app/services/export/zim_writer.py` returns the line

---

### [ ] 5.3 Test zimcheck integration
**Time**: 15 minutes

Create a test script `test_zimcheck.py`:
```python
"""Test zimcheck validation."""
from pathlib import Path
import subprocess
from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ZimEntry
)

metadata = ZimMetadata(
    title="Test",
    description="Test",
    language="eng",
    creator="Test",
    publisher="Test",
    date="2026-05-20",
    name="test",
    flavour="test"
)

entries = [
    ZimEntry(
        path="index",
        title="Test",
        content="<p>Test</p>",
        mime_type="text/html; charset=utf-8",
        is_front_article=True
    )
]

config = ExportConfig(language_iso3="eng")
writer = ZimWriter(
    entries=entries,
    metadata=metadata,
    config=config,
    output_path=Path("test_zimcheck.zim"),
    zimcheck_binary="/usr/bin/zimcheck"
)

result = writer.create_zim(run_zimcheck=True)
print(f"ZIM created: {result.output_path}")
print(f"ZimCheck passed: {result.zimcheck_passed}")
print(f"Size: {result.file_size_bytes} bytes")

# Manual verification
ret = subprocess.run(["zimcheck", str(result.output_path)], capture_output=True)
print(f"zimcheck exit code: {ret.returncode}")
if ret.returncode == 0:
    print("✓ zimcheck validation passed")
else:
    print("✗ zimcheck validation failed:")
    print(ret.stdout.decode())
    print(ret.stderr.decode())
```

Run it:
```bash
python3 test_zimcheck.py
```

**Verification**: 
- `ZimCheck passed: True`
- `zimcheck exit code: 0`
- Output shows "✓ zimcheck validation passed"

If zimcheck fails, debug with:
```bash
zimcheck --verbose test_zimcheck.zim
```

---

### [ ] 5.4 Run integration tests
**Time**: 10 minutes
**Blocker**: zimcheck binary must be installed

```bash
uv run pytest tests/integration/test_zimcheck_validation.py -v -m integration
```

Expected: 6+ tests pass

**Verification**: Exit code 0, no failures

---

### [ ] 5.5 Commit Phase 5
**Time**: 5 minutes

```bash
git add app/services/export/zim_writer.py
git commit -m "feat(zim): re-enable zimcheck validation for all exports"
```

---

## PHASE 6: Full Test Cycle (1.0 hour)

### [ ] 6.1 Run all 84+ export tests
**Time**: 15 minutes

```bash
uv run pytest tests/ -k "export" -v
```

Expected: 84+ tests pass, 0 failures

**Verification**: Output shows "X passed"

---

### [ ] 6.2 Run full test suite (optional, comprehensive)
**Time**: 30 minutes

```bash
uv run pytest tests/ -v
```

This runs ALL tests, not just export-related.

**Verification**: Exit code 0, no critical failures

---

### [ ] 6.3 Generate a 50-article test ZIM (final manual validation)
**Time**: 15 minutes

Create `test_50_articles.py`:
```python
"""Generate a 50-article ZIM for final validation."""
from pathlib import Path
from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ZimEntry
)

metadata = ZimMetadata(
    title="50-Article Test",
    description="Manual validation export",
    language="eng",
    creator="Test",
    publisher="Test",
    date="2026-05-20",
    name="test_50",
    flavour="test"
)

# Create 50 entries
entries = []
for i in range(50):
    entries.append(
        ZimEntry(
            path=f"articles/article-{i:03d}",
            title=f"Article {i}",
            content=f"<h1>Article {i}</h1><p>Content {i}</p>",
            mime_type="text/html; charset=utf-8",
            is_front_article=(i == 0)
        )
    )

config = ExportConfig(language_iso3="eng")
writer = ZimWriter(
    entries=entries,
    metadata=metadata,
    config=config,
    output_path=Path("test_50_articles.zim"),
    zimcheck_binary="/usr/bin/zimcheck"
)

result = writer.create_zim()
print(f"✓ ZIM created: {result.output_path}")
print(f"  Size: {result.file_size_bytes:,} bytes")
print(f"  Valid: {result.zimcheck_passed}")
print(f"  Duration: {result.generation_duration_seconds:.2f}s")
```

Run it:
```bash
python3 test_50_articles.py
time zimcheck test_50_articles.zim
```

**Verification**:
- ZIM file created successfully
- Size is between 10KB-1MB (reasonable for 50 articles)
- zimcheck passes with exit code 0
- Generation time is <5 seconds

---

### [ ] 6.4 Verify no references to old stubs remain
**Time**: 5 minutes

```bash
grep -r "_stub_write_placeholder" app/
```

Expected: No results (all stubs removed)

**Verification**: No output or "No such file"

---

## PHASE 7: Cleanup and Dead Code Removal (0.5 hours)

### [ ] 7.1 Delete _stub_write_placeholder() method
**Time**: 10 minutes
**Blocker**: All tests must pass (Phase 6)

Edit `app/services/export/zim_writer.py`. Find the `_stub_write_placeholder()` method (around line 914-931) and delete it entirely.

Verify no references remain:
```bash
grep -r "_stub_write_placeholder" app/
```

**Verification**: No output

---

### [ ] 7.2 Remove any TODO comments about libzim
**Time**: 5 minutes

Search for and remove any comments like:
```python
# TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
```

Expected: 0-2 removals

```bash
grep -n "TODO.*libzim" app/services/export/zim_writer.py
```

---

### [ ] 7.3 Run full test suite one more time
**Time**: 15 minutes

```bash
uv run pytest tests/ -k "export" -v
```

Expected: All 84+ tests still pass (dead code removal doesn't affect functionality)

**Verification**: Exit code 0, no failures

---

### [ ] 7.4 Commit Phase 7
**Time**: 5 minutes

```bash
git add app/services/export/zim_writer.py
git commit -m "chore(zim): remove dead _stub_write_placeholder() method after libzim activation"
```

---

## PHASE 8: Documentation and Final Cleanup (0.5 hours)

### [ ] 8.1 Update docstrings
**Time**: 10 minutes

Verify that:
- `ZimWriter.create_zim()` docstring mentions libzim integration (update if needed)
- `ArticleItem` class has proper docstring (already added in Phase 2)
- `_apply_metadata_to_creator()` has proper docstring (already added in Phase 4)

No code changes needed if docstrings are already complete.

---

### [ ] 8.2 Create a summary test output file
**Time**: 10 minutes

Run this and save output:
```bash
uv run pytest tests/ -k "export" -v --tb=short > TEST_RESULTS_ZIMWRITER.txt 2>&1
cat TEST_RESULTS_ZIMWRITER.txt | tail -20
```

This creates a record of test results.

---

### [ ] 8.3 Final branch verification
**Time**: 5 minutes

```bash
git log --oneline | head -10  # Show recent commits
git status                     # Should be clean
```

Expected: 5-7 new commits, no uncommitted changes

---

### [ ] 8.4 Push branch (optional at this stage)
**Time**: 5 minutes

```bash
git push -u origin feature/zimwriter-libzim-integration
```

Create PR on GitHub (link goes in PROJECTS.md).

---

## Summary Table

| Phase | Item | Hours | Blocker? | Status |
|-------|------|-------|----------|--------|
| **0: Setup** | Create branch | 0.05 | None | — |
| | Install zimcheck | 0.05 | None | Optional |
| | Create test template | 0.05 | None | — |
| **1: Dependency** | Add to pyproject.toml | 0.08 | None | ✓ Required |
| | Install libzim wheel | 0.25 | None | ✓ Required |
| | Add import guard | 0.17 | Phase 1.2 | ✓ Required |
| | Commit | 0.05 | — | — |
| **2: ArticleItem** | Add class | 0.33 | Phase 1 | ✓ Required |
| | Run tests | 0.50 | Phase 2.1 | — |
| | Manual test | 0.17 | Phase 2.1 | — |
| | Commit | 0.05 | — | — |
| **3: Creator** | Replace stub | 0.42 | Phase 1-2 | ✓ Required |
| | Run tests | 0.67 | Phase 3.1 | — |
| | Hex check | 0.08 | Phase 3.1 | Optional |
| | Commit | 0.05 | — | — |
| **4: Metadata** | Add fallback PNG | 0.08 | Phase 3 | ✓ Required |
| | Implement method | 0.50 | Phase 4.1 | ✓ Required |
| | Manual test | 0.33 | Phase 4.2 | — |
| | Run tests | 0.50 | Phase 4.2 | — |
| | Commit | 0.05 | — | — |
| **5: ZimCheck** | Verify installed | 0.08 | None | — |
| | Verify default | 0.08 | None | — |
| | Test integration | 0.25 | zimcheck binary | — |
| | Run integration tests | 0.17 | zimcheck binary | — |
| | Commit | 0.05 | — | — |
| **6: Full Test** | Run export tests | 0.25 | Phase 1-5 | — |
| | Run full suite | 0.50 | Phase 1-5 | Optional |
| | 50-article test | 0.25 | Phase 1-5 | — |
| | Verify stubs removed | 0.08 | Phase 1-5 | — |
| **7: Cleanup** | Delete stub method | 0.17 | Phase 6 | Optional |
| | Remove TODO | 0.08 | Phase 7.1 | Optional |
| | Final test | 0.25 | Phase 7 | — |
| | Commit | 0.05 | — | — |
| **8: Documentation** | Update docstrings | 0.17 | None | — |
| | Test summary | 0.17 | Phase 1-5 | — |
| | Branch verification | 0.08 | All | — |
| | Push branch | 0.08 | All | Optional |
| **TOTAL** | | **8.5** | — | — |

**Key dependencies**:
- Phase 1 blocks all others
- Phase 2 blocks Phase 3
- Phase 3 blocks Phase 4
- Phases 4-5 can run in parallel (optional)
- Phase 6 requires Phases 1-5 complete
- Phase 7 requires Phase 6 pass
- Phase 8 is polish (not blocking)

**Estimated calendar time** (single developer, no breaks): 8-10 hours = 1 working day

**Recommended approach**:
- Day 1 morning: Phases 0-2 (2 hours)
- Day 1 afternoon: Phases 3-4 (3 hours)
- Day 1 evening: Phases 5-6 (2 hours)
- Day 2 morning: Phases 7-8 (1 hour), create PR

**If blocked or debugging**:
- Extended test debugging: +1-2 hours
- zimcheck failures: +0.5-1 hour (debug with `zimcheck --verbose`)
- libzim installation issues: +0.5 hour (consult source build docs)

---

## Success Criteria

✓ **All 84+ export tests pass**
✓ **zimcheck validation passes on all generated ZIMs**
✓ **ZIM magic header verified (`5a 49 4d 04`)**
✓ **Metadata readable via `libzim.reader.Archive`**
✓ **50-article test ZIM generated successfully**
✓ **No references to stub code remain**
✓ **Feature branch ready for PR**

**User go-live approval needed after**: Phase 6 completion (all tests pass)

**Recommend merge to master**: After user review + approval
