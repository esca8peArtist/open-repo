---
title: "Phase 5 Candidate 1 (ZimWriter) — Implementation Checklist & Timeline"
project: open-repo
phase: 5
candidate: 1
status: implementation-ready
estimated_duration: "8-11 hours"
date: 2026-05-20
---

# Phase 5 Candidate 1: Implementation Checklist & Timeline

## Overview

This checklist guides you through the complete implementation of Phase 5 Candidate 1 (ZimWriter/libzim integration). All code changes are clearly specified and copy-paste ready from the implementation roadmap.

**Total estimated time**: 4–5 hours for implementation (within the 8–11 hour Phase 5 window)

**Success criteria**: 
- All 84 tests pass with real libzim integration
- Manual ZIM generation produces a valid file readable by Kiwix
- Zero code regressions to Phase 4 federation infrastructure

---

## PRE-IMPLEMENTATION SETUP (30 minutes)

### Step 1: Verify Environment ✅ (5 minutes)

```bash
# Confirm Python version
python3 --version
# Expected: Python 3.11.x

# Confirm project directory
pwd
# Expected: /home/awank/dev/SuperClaude_Framework/projects/open-repo

# Confirm test suite passes with stubs (pre-implementation baseline)
cd backend
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short
# Expected: 84 passed in ~0.5s
```

**Blocker if fails**: If test count is not 84, stop and investigate test coverage.

---

### Step 2: Create Feature Branch (5 minutes)

```bash
# Ensure clean working directory
git status
# Expected: no uncommitted changes

# Create feature branch
git checkout -b feature/zimwriter-libzim-integration

# Verify branch created
git branch -vv
# Expected: * feature/zimwriter-libzim-integration
```

---

### Step 3: Install zimcheck Binary (5 minutes)

```bash
# Install zim-tools package (one-time setup, required for validation)
apt-get update && apt-get install -y zim-tools

# Verify installation
zimcheck --version
# Expected: output like "zimcheck 3.x.x"
```

**Note**: If zimcheck installation fails, continue with implementation. You can run tests with `run_zimcheck=False` and add zimcheck later.

---

### Step 4: Activate Development Environment (5 minutes)

```bash
# Ensure UV is installed
which uv
# If not found: pip install uv

# Install development dependencies (includes libzim once we add it to pyproject.toml)
cd backend
uv pip install -e ".[dev]"
```

---

### Step 5: Create Checkpoint Commit (5 minutes)

```bash
# Verify everything is ready
git status
# Expected: all changes staged or committed

# Create checkpoint commit (before implementation starts)
git commit -m "chore(open-repo): pre-implementation checkpoint — zimwriter phase 5.1"
```

---

## IMPLEMENTATION: CHANGE 1 (15 minutes)

### File: `backend/pyproject.toml`

**Location**: Line 20, under `[project.dependencies]`

**Current state**:
```toml
[project]
name = "open-repo-backend"
version = "0.2.0"
description = "Open-Repo MVP backend - FastAPI + PostgreSQL + Meilisearch"
requires-python = ">=3.10"
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

**Task**: Add one line before the closing bracket `]`

**New line to add**:
```toml
    "libzim>=3.2,<4.0",
```

**Expected result**:
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
    "libzim>=3.2,<4.0",
]
```

**Verification** (5 minutes):

```bash
# Reinstall dependencies to fetch libzim wheel
cd backend
uv pip install -e ".[dev]"

# Confirm libzim is installed
uv pip list | grep libzim
# Expected: libzim  3.9.0

# Verify import works
uv run python -c "from libzim.writer import Creator; print('✅ libzim imported successfully')"
```

**Next**: Commit this change

```bash
git add backend/pyproject.toml
git commit -m "feat(zimwriter): add libzim>=3.2,<4.0 dependency to pyproject.toml"
```

---

## IMPLEMENTATION: CHANGE 2 (15 minutes)

### File: `backend/app/services/export/zim_writer.py`

**Location**: After line 48 (after `from typing import Optional`)

**Task**: Add import guard for libzim

**Copy this code** (from the implementation roadmap, lines 136-142):

```python
# Graceful import guard — allows module to load even if libzim not installed (for testing without wheel)
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

**Verification** (5 minutes):

```bash
# Verify module still loads without errors
cd backend
uv run python -c "from app.services.export.zim_writer import ZimWriter, _LIBZIM_AVAILABLE; print(f'✅ ZimWriter imported, _LIBZIM_AVAILABLE={_LIBZIM_AVAILABLE}')"

# Expected: ✅ ZimWriter imported, _LIBZIM_AVAILABLE=True
```

**Next**: Commit this change

```bash
git add backend/app/services/export/zim_writer.py
git commit -m "feat(zimwriter): add import guard for libzim.writer classes"
```

---

## IMPLEMENTATION: CHANGE 3 (45 minutes)

### File: `backend/app/services/export/zim_writer.py`

**Location**: After the `ZimEntry` dataclass (around line 402), before the `ZimWriter` class definition

**Task**: Add `ArticleItem` adapter class

**Copy this code** (from the implementation roadmap, lines 151-184):

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

**Exact location**: This class should be placed after `ZimEntry` class definition ends and before `class ZimWriter:` begins. Look for the comment `# ---------------------------------------------------------------------------` and `# Main ZimWriter class` (around line 404-409).

**Verification** (10 minutes):

```bash
# Verify class is importable
cd backend
uv run python -c "from app.services.export.zim_writer import ArticleItem; print('✅ ArticleItem imported successfully')"

# Run tests to ensure no regressions
uv run pytest tests/integration/test_export_pipeline.py -v -k "test_valid_entry_initializes or test_add_article" --tb=short
# Expected: 2 passed
```

**Next**: Commit this change

```bash
git add backend/app/services/export/zim_writer.py
git commit -m "feat(zimwriter): implement ArticleItem adapter class for libzim Creator API"
```

---

## IMPLEMENTATION: CHANGE 4 (45 minutes)

### File: `backend/app/services/export/zim_writer.py`

**Location 1**: Before `class ZimWriter`, add fallback illustration bytes (around line 405)

**Task**: Add fallback 1x1 transparent PNG constant

**Copy this code** (from the implementation roadmap, lines 250-254):

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

Place this constant right before `class ZimWriter:` definition (around line 408).

**Location 2**: Find and replace the `create_zim()` method stub

**Find** (around line 759-762):
```python
        # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
        # See the docstring above for the correct implementation pattern.
        # For now, write a placeholder file to allow test harness to run.
        self._stub_write_placeholder()
```

**Replace with** (from the implementation roadmap, lines 200-211):
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

**Verification** (15 minutes):

```bash
# Run tests to verify create_zim() works with real libzim
cd backend
uv run pytest tests/integration/test_export_pipeline.py::TestZimWriterCreateZim -v --tb=short
# Expected: 10 passed

# Spot-check: verify a ZIM file is actually created
uv run pytest tests/integration/test_export_pipeline.py::TestZimWriterCreateZim::test_create_zim_produces_output_file -v
# Expected: 1 passed, and you'll see a real ZIM file created
```

**Next**: Commit this change

```bash
git add backend/app/services/export/zim_writer.py
git commit -m "feat(zimwriter): implement Creator context manager in create_zim() method"
```

---

## IMPLEMENTATION: CHANGE 5 (30 minutes)

### File: `backend/app/services/export/zim_writer.py`

**Location**: Find the `_apply_metadata_to_creator()` method (around line 945)

**Current state**: Method has only `pass` statement

**Task**: Implement metadata application logic

**Copy this code** (from the implementation roadmap, lines 220-241):

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

**Replace** the entire method body (currently just `pass`)

**Verification** (10 minutes):

```bash
# Run full test suite to ensure all components work together
cd backend
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short
# Expected: 84 passed

# Spot-check metadata application
uv run pytest tests/integration/test_export_pipeline.py -k "metadata" -v
# Expected: 9 passed
```

**Next**: Commit this change

```bash
git add backend/app/services/export/zim_writer.py
git commit -m "feat(zimwriter): implement _apply_metadata_to_creator() method"
```

---

## POST-IMPLEMENTATION VERIFICATION (1 hour)

### Step 1: Run Full Test Suite (20 minutes)

```bash
cd backend
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short

# Expected output:
# ============================= 84 passed in X.XXs =============================
```

**If tests fail**:
1. Review error message carefully
2. Check if error is in your code change or in a pre-existing stub
3. Revert to last working commit and try again: `git reset --hard HEAD~1`

---

### Step 2: Manual ZIM Generation & Validation (30 minutes)

Create a test script to generate a real ZIM file and verify it with zimcheck:

```bash
# Create test script
cat > /tmp/test_zim_generation.py << 'TESTEOF'
import sys
sys.path.insert(0, '/home/awank/dev/SuperClaude_Framework/projects/open-repo/backend')

from pathlib import Path
from app.services.export.zim_writer import (
    ZimWriter,
    ZimMetadata,
    ZimEntry,
    ExportConfig,
    ExportScope,
)

# Create test metadata
metadata = ZimMetadata(
    title="Open-Repo Test Export",
    description="Test ZIM generation with libzim",
    language="eng",
    name="test_en_nopic",
    flavour="nopic",
    creator="Test Suite",
    publisher="Open-Repo",
    source_url="https://test.example.com",
    tags="test;offline;verification",
)

# Create config
config = ExportConfig(
    scope=ExportScope.LOCAL_ONLY,
    flavour="nopic",
    include_images=False,
)

# Create ZimWriter
output_path = Path("/tmp/test_export.zim")
writer = ZimWriter(
    metadata=metadata,
    config=config,
    output_path=output_path,
)

# Add test articles
for i in range(5):
    writer.add_article(
        path=f"article-{i}",
        content=f"<html><body><h1>Test Article {i}</h1><p>This is test content {i}.</p></body></html>",
        article_type="test",
        language="en",
    )

# Create ZIM file
result = writer.create_zim(run_zimcheck=True)

print(f"✅ ZIM file created: {result.output_path}")
print(f"   File size: {result.file_size_bytes} bytes")
print(f"   SHA-256: {result.sha256}")
print(f"   Article count: {result.article_count}")
print(f"   zimcheck passed: {result.zimcheck_passed}")

TESTEOF

# Run the test script
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
uv run python /tmp/test_zim_generation.py
```

**Expected output**:
```
✅ ZIM file created: /tmp/test_export.zim
   File size: XXXX bytes
   SHA-256: 64-character-hex-string
   Article count: 5
   zimcheck passed: True
```

**If zimcheck fails**:
- Check that zim-tools is installed: `zimcheck --version`
- Review zimcheck output in the test result
- Common issue: illustration dimensions; the fallback PNG is minimal but valid

---

### Step 3: Verify File with Kiwix (10 minutes)

```bash
# Install Kiwix (if not already installed)
apt-get install -y kiwix-tools

# List ZIM file info
kiwix-info /tmp/test_export.zim

# Expected output includes:
# - Title: "Open-Repo Test Export"
# - Article count: 5
# - Language: eng
```

---

## CLEANUP & COMMIT (30 minutes)

### Step 1: Remove Stub Code (15 minutes)

**Find and delete** the `_stub_write_placeholder()` method (around line 914-931)

This method should be removed after verifying that real libzim works. Search for:

```python
def _stub_write_placeholder(self) -> None:
    """
    Write a placeholder file during stub phase.
    ...
    """
```

Delete the entire method (typically ~15 lines).

**Verify removal**:
```bash
cd backend
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short
# Expected: 84 passed (same as before)
```

**Commit the removal**:
```bash
git add backend/app/services/export/zim_writer.py
git commit -m "chore(zimwriter): remove _stub_write_placeholder() method — no longer needed"
```

---

### Step 2: Update Module Docstring (10 minutes)

**Find** the module-level docstring (top of `zim_writer.py`, around line 1-38)

**Update** the docstring to remove mentions of "stub" and mark as implemented:

**Change this**:
```python
"""
ZimWriter: Python-libzim-based ZIM file generation for open-repo offline exports.

This module provides the stub interfaces for Phase 5 ZIM file generation. The class
structure, method signatures, docstrings, and data models are complete. The actual
python-libzim integration is stubbed with TODO markers at each integration point.
```

**To this**:
```python
"""
ZimWriter: Python-libzim-based ZIM file generation for open-repo offline exports.

This module provides complete ZIM file generation using the python-libzim library
(libzim >= 3.2). ZimWriter bridges open-repo's content database to the Kiwix
ecosystem, handling metadata validation, Xapian full-text indexing, zimcheck
validation, and offline archive generation.
```

**Commit the documentation update**:
```bash
git add backend/app/services/export/zim_writer.py
git commit -m "docs(zimwriter): update module docstring — implementation complete"
```

---

### Step 3: Verify No Regressions (10 minutes)

Run the full test suite one final time:

```bash
cd backend
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short

# Expected: 84 passed in < 1s
```

Also run any other related tests:

```bash
# If there are federation tests
uv run pytest tests/integration/ -v --tb=short

# Check for linting issues
uv run ruff check app/services/export/zim_writer.py
# Expected: no issues
```

---

### Step 4: Create Final Integration Commit (5 minutes)

```bash
# Create a final commit summarizing the entire feature
git commit --allow-empty -m "feat(zimwriter): Phase 5 Candidate 1 — libzim integration complete

- Added libzim>=3.2,<4.0 dependency
- Implemented import guard for graceful fallback
- Created ArticleItem adapter for libzim Creator API
- Implemented create_zim() with real libzim Creator
- Implemented _apply_metadata_to_creator() for ZIM metadata
- Removed _stub_write_placeholder() method
- All 84 tests passing with real libzim integration
- Manual ZIM generation verified with zimcheck
- Zero breaking changes to Phase 4 federation infrastructure

Implementation time: 4-5 hours as estimated"
```

---

## FINAL CHECKLIST

Before merging, verify all items are complete:

```
[✅] All 5 code changes implemented
[✅] Import guard added for libzim
[✅] ArticleItem adapter class added
[✅] create_zim() uses real Creator context manager
[✅] _apply_metadata_to_creator() implemented
[✅] _stub_write_placeholder() removed
[✅] libzim>=3.2,<4.0 added to pyproject.toml
[✅] All 84 tests passing
[✅] Manual ZIM generation tested
[✅] zimcheck validation working
[✅] Module docstring updated
[✅] No linting errors
[✅] Zero breaking changes to Phase 4
[✅] Docker environment verified (optional)
```

---

## MERGE & DEPLOYMENT

### Step 1: Create Pull Request

```bash
# Push branch to remote
git push -u origin feature/zimwriter-libzim-integration

# Create PR (via GitHub UI or gh CLI)
gh pr create --title "feat: Phase 5 Candidate 1 — ZimWriter libzim Integration" \
  --body "Complete implementation of ZimWriter with real libzim integration.

- Adds libzim>=3.2,<4.0 dependency
- Implements all 5 required code changes
- All 84 tests passing
- Manual verification with zimcheck complete
- Ready for immediate merge to master"
```

---

### Step 2: Code Review & Merge

1. Request code review from team
2. Address any feedback
3. Merge to `master` branch
4. Deploy via standard CI/CD pipeline

---

## SUCCESS CRITERIA

✅ **Implementation is complete when**:

1. All 84 integration tests pass with real libzim
2. Manual ZIM generation produces files readable by Kiwix
3. zimcheck validation passes without errors
4. Zero breaking changes to Phase 4 federation
5. Code review approved
6. PR merged to master
7. Deployed to production environment

---

## ROLLBACK PROCEDURE (if needed)

If implementation fails post-merge:

```bash
# Revert to previous commit
git revert <merge-commit-hash>

# Or reset hard to pre-implementation state
git reset --hard origin/master~1
```

---

## Reference Documentation

- Implementation roadmap: `PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md`
- Verification audit: `phase-5-candidate-1-implementation-verification.md`
- Decision framework: `PHASE_5_DECISION_FRAMEWORK.md`
- libzim docs: https://python-libzim.readthedocs.io/

---

**Estimated total time**: 4–5 hours (implementation) + 1–2 hours (review/deploy) = 5–7 hours

**Timeline fits within**: 8–11 hour Phase 5 window ✅

**Status**: Ready to implement on May 24–26, 2026

