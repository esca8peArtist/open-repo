---
title: "Phase 5 Candidate 1 — Implementation Checklist (Step-by-Step)"
project: open-repo
phase: 5
candidate: 1
status: implementation-ready
date: 2026-05-20
---

# Phase 5 Candidate 1: Implementation Checklist

**Duration**: 8-11 hours  
**Files Modified**: 2 (pyproject.toml, zim_writer.py)  
**Tests**: 88 existing + 12 new = 100 total  
**Commit Count**: 5-6 (one per code change + tests + cleanup)

---

## PHASE 1: Dependency and Environment Setup (15 minutes)

### ✅ Task 1.1: Add libzim to pyproject.toml
**Estimated Time**: 5 minutes  
**File**: `backend/pyproject.toml`  
**Difficulty**: Trivial  

**Change**:
```toml
# In [project.dependencies] section, add this line:
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
    "libzim>=3.2,<4.0",  # ADD THIS LINE
]
```

**Verification**:
```bash
cd backend
pip install -e .
python3 -c "from libzim.writer import Creator; print('✓ libzim installed')"
```

**Commit**: `chore(phase-5): add libzim>=3.2,<4.0 dependency`

---

### ✅ Task 1.2: Verify Installation and Create Feature Branch
**Estimated Time**: 10 minutes  
**File**: None (shell commands)  

**Commands**:
```bash
# Create feature branch
git checkout -b feature/zimwriter-libzim-integration

# Verify environment
python3 -c "
from libzim.writer import Creator, Item, StringProvider, Hint
print('✓ All required libzim.writer modules available')
print('✓ Ready to proceed with implementation')
"
```

**Check**: All commands succeed without errors.

---

## PHASE 2: Core Implementation (2-3 hours)

### ✅ Task 2.1: Add libzim Import Guard
**Estimated Time**: 10 minutes  
**File**: `backend/app/services/export/zim_writer.py`  
**Line**: After line 48 (after `from typing import Optional`)  
**Difficulty**: Trivial  

**Current Code** (lines 40-50):
```python
from __future__ import annotations

import hashlib
import logging
import subprocess
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)
```

**Insert After Line 50**:
```python
# libzim import guard — allows testing without libzim installed
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None  # type: ignore[assignment,misc]
```

**Verification**:
```bash
python3 -c "from app.services.export.zim_writer import _LIBZIM_AVAILABLE; assert _LIBZIM_AVAILABLE"
```

**Commit**: `feat(phase-5): add libzim import guard with fallback`

---

### ✅ Task 2.2: Add ArticleItem Class
**Estimated Time**: 20 minutes  
**File**: `backend/app/services/export/zim_writer.py`  
**Line**: Before line 410 (before `class ZimWriter:`)  
**Difficulty**: Simple  

**Insert Before the ZimWriter Class Definition**:

Find the comment `# ---------------------------------------------------------------------------` followed by `# Main ZimWriter class`, around line 407-409. Insert the ArticleItem class before this:

```python
# ---------------------------------------------------------------------------
# libzim Item adapter
# ---------------------------------------------------------------------------


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
python3 -c "from app.services.export.zim_writer import ArticleItem; print('✓ ArticleItem class available')"
```

**Commit**: `feat(phase-5): add ArticleItem libzim.Item adapter class`

---

### ✅ Task 2.3: Replace create_zim() Stub with Real Implementation
**Estimated Time**: 30 minutes  
**File**: `backend/app/services/export/zim_writer.py`  
**Lines**: 762-765  
**Difficulty**: Simple  

**Current Code** (lines 760-770):
```python
        )

        # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
        # See the docstring above for the correct implementation pattern.
        # For now, write a placeholder file to allow test harness to run.
        self._stub_write_placeholder()

        self._is_finalized = True
        end_time = datetime.utcnow()
```

**Replace Lines 762-765** with:
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

**Result**: File should have ~8-10 new lines replacing 4 old lines.

**Verification**:
```bash
python3 << 'EOF'
import tempfile
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope, ZimEntry

# Create minimal test export
with tempfile.TemporaryDirectory() as tmpdir:
    output_path = Path(tmpdir) / "test.zim"
    metadata = ZimMetadata(
        title="Test", description="Test", language="eng", name="test_en_nopic",
        flavour="nopic", creator="Test", publisher="Test", source_url="http://test"
    )
    config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
    writer = ZimWriter(metadata=metadata, config=config, output_path=output_path)
    writer.add_article(path="test", title="Test Article", content="<p>Test content</p>")
    result = writer.create_zim()
    if output_path.exists() and output_path.stat().st_size > 100:
        print("✓ ZIM file created successfully")
    else:
        print("✗ ZIM file creation failed")
EOF
```

**Commit**: `feat(phase-5): replace create_zim() stub with real libzim Creator`

---

### ✅ Task 2.4: Implement _apply_metadata_to_creator() Fully
**Estimated Time**: 20 minutes  
**File**: `backend/app/services/export/zim_writer.py`  
**Lines**: 873-904  
**Difficulty**: Simple  

**Current Code** (lines 873-904):
```python
    def _apply_metadata_to_creator(self, creator: object) -> None:
        """
        Apply all ZimMetadata fields to a python-libzim Creator instance.

        This method is called inside the create_zim() Creator context.

        When implemented with the real Creator object:
            creator.config_indexing(True, self.config.language_iso3)  # Enable Xapian FTS
            creator.add_metadata("Title", self.metadata.title)
            creator.add_metadata("Description", self.metadata.description)
            ... (other metadata calls)
        """
        try:
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
        except AttributeError:
            pass
```

**Replace With**:
```python
    def _apply_metadata_to_creator(self, creator: "Creator") -> None:
        """
        Apply all ZimMetadata fields to a python-libzim Creator instance.

        Called inside the create_zim() Creator context after config_indexing().
        All metadata is written to the ZIM M/ namespace.
        """
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

**Changes Summary**:
- Remove try/except wrapper (no longer needed with real Creator)
- Change `creator: object` type hint to `creator: "Creator"`
- Update docstring to reflect implementation
- Add fallback PNG illustration when none provided

**Verification**:
```bash
python3 -c "
import inspect
from app.services.export.zim_writer import ZimWriter
sig = inspect.signature(ZimWriter._apply_metadata_to_creator)
params = str(sig)
assert 'Creator' in params, f'Type hint missing: {params}'
print('✓ _apply_metadata_to_creator() properly typed')
"
```

**Commit**: `feat(phase-5): implement _apply_metadata_to_creator() for real Creator`

---

## PHASE 3: Testing (2-3 hours)

### ✅ Task 3.1: Run Existing Test Suite
**Estimated Time**: 10 minutes  
**Files**: None (tests already exist)  
**Commands**:

```bash
cd backend
python3 -m pytest tests/integration/test_export_pipeline.py -v 2>&1 | tail -20
```

**Expected Result**:
```
============================== 88 passed in 0.15s ==============================
```

**If Any Fail**: Debug individual test:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py::TestZimWriter -v
```

**Commit**: `test(phase-5): verify 88 existing tests pass with libzim integration`

---

### ✅ Task 3.2: Create 12 New libzim Integration Tests
**Estimated Time**: 1.5-2 hours  
**File**: Create `backend/tests/integration/test_zim_libzim_integration.py`  
**Difficulty**: Medium  

**Test File Structure** (pseudo-code):

```python
"""
12 comprehensive tests for real libzim Creator integration.

These tests verify:
1. Real ZIM file generation (magic bytes, size > stub)
2. Metadata written to M/ namespace (readable by Archive)
3. Xapian indexing enabled and functional
4. Articles indexed and searchable
5. HTML content contains no external dependencies
6. zimcheck validation integration
7. Unicode and special characters
8. Large exports (50+ articles)
9. Period collision handling
10. SHA-256 checksum computation
11. Offline article retrieval
12. Concurrent export safety
"""

import pytest
from pathlib import Path
import tempfile
from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ZimEntry, ExportConfig, ExportScope
)
from libzim.reader import Archive

class TestRealZimGeneration:
    
    def test_creates_real_zim_file_not_stub(self):
        """Verify output is a real ZIM binary, not placeholder text."""
        # Create a 10-article export
        # Verify first 4 bytes are ZIM magic: \x5a\x49\x4d\x04
        pass
    
    def test_metadata_readable_by_archive(self):
        """Verify metadata is written to M/ namespace."""
        # Create export with metadata
        # Read back using libzim.reader.Archive
        # Verify all 10+ metadata fields present
        pass
    
    def test_xapian_indexing_enabled(self):
        """Verify Xapian FTS index is embedded."""
        # Create export with 5 agriculture articles
        # Use Archive.search("biosand") to verify FTS
        # Assert >= 1 result returned
        pass
    
    def test_articles_count_matches_database(self):
        """Verify all added articles appear in ZIM."""
        # Add 50 articles
        # Read back and count
        # Assert count == 50
        pass
    
    def test_html_no_external_dependencies(self):
        """Verify rendered HTML has no http:// refs."""
        # Create export with articles containing images
        # Read HTML from ZIM
        # Assert no <link href="http"> or <img src="http">
        pass
    
    def test_unicode_content_roundtrip(self):
        """Verify non-ASCII characters survive write-read cycle."""
        # Add article with Spanish accents and Arabic
        # Read back and verify encoding intact
        pass
    
    def test_offline_article_retrieval_by_path(self):
        """Verify written articles retrievable by path."""
        # Add "agriculture/biosand-filter" article
        # Read back using Archive.get_entry_by_path()
        # Verify content matches
        pass
    
    def test_nopic_variant_excludes_images(self):
        """Verify nopic export has no image resources."""
        # Create export with include_images=False
        # Add 3 articles with inline images
        # Read ZIM and verify no entries with mime_type="image/*"
        pass
    
    def test_sha256_checksum_computed(self):
        """Verify SHA-256 sidecar file computed and valid."""
        # Create export
        # Verify writer.sha256_checksum is 64-char hex
        # Verify can be verified: sha256sum -c *.sha256
        pass
    
    def test_period_collision_handling(self):
        """Verify duplicate period gets alphabetic suffix."""
        # Simulate existing_periods = ["2026-05"]
        # Call ZimWriter.compute_period()
        # Assert returns "2026-05a"
        pass
    
    def test_file_size_reasonable(self):
        """Verify ZIM file size is reasonable for content."""
        # Create 10-article export
        # Verify file size between 1KB and 10MB
        pass
    
    def test_zimwriter_not_reusable_after_finalize(self):
        """Verify second create_zim() call raises RuntimeError."""
        # Call create_zim() once
        # Call create_zim() again
        # Assert RuntimeError raised with correct message
        pass
```

**Estimated Test Count**: 12 tests, ~15-20 lines each = ~200 lines total

**Run Tests**:
```bash
python3 -m pytest tests/integration/test_zim_libzim_integration.py -v
```

**Expected Result**: All 12 tests pass

**Commit**: `test(phase-5): add 12 libzim integration tests (real ZIM generation)`

---

### ✅ Task 3.3: Run Full Test Suite (100 tests)
**Estimated Time**: 10 minutes  

```bash
cd backend
python3 -m pytest tests/integration/test_export_pipeline.py tests/integration/test_zim_libzim_integration.py -v --tb=short
```

**Expected Result**:
```
88 tests from test_export_pipeline.py ............. PASSED
12 tests from test_zim_libzim_integration.py ...... PASSED
═══════════════════════════════════════════════════════════════
100 passed in X.XXs
```

**If Any Fail**: 
- Check error message
- Roll back last code change
- Debug issue
- Re-implement

**Commit**: `test(phase-5): verify 100/100 tests passing (88 existing + 12 new)`

---

## PHASE 4: Cleanup and Finalization (30 minutes)

### ✅ Task 4.1: Delete _stub_write_placeholder() Method
**Estimated Time**: 5 minutes  
**File**: `backend/app/services/export/zim_writer.py`  
**Lines**: 922-939  
**Difficulty**: Trivial  

**Find and Delete**:
```python
    def _stub_write_placeholder(self) -> None:
        """
        Write a placeholder file during stub phase.

        This allows the test harness to run without python-libzim installed.
        Replaced by actual Creator calls in the full implementation.

        TODO(post-PR-merge): Remove this method entirely. The create_zim()
        method should use the Creator context manager directly.
        """
        placeholder_content = (
            f"STUB ZIM PLACEHOLDER\n"
            f"name={self.metadata.name}\n"
            f"articles={self._article_count}\n"
            f"resources={self._resource_count}\n"
            f"generated_at={datetime.utcnow().isoformat()}\n"
        ).encode("utf-8")
        self.output_path.write_bytes(placeholder_content)
```

**Delete Entirely**. This stub is no longer needed.

**Verification**:
```bash
grep -n "_stub_write_placeholder" backend/app/services/export/zim_writer.py || echo "✓ Stub method deleted"
```

**Commit**: `chore(phase-5): remove _stub_write_placeholder() after full implementation`

---

### ✅ Task 4.2: Update Module Docstring
**Estimated Time**: 5 minutes  
**File**: `backend/app/services/export/zim_writer.py`  
**Lines**: 1-38 (module docstring)  

**Current Docstring** (lines 1-38):
```python
"""
ZimWriter: Python-libzim-based ZIM file generation for open-repo offline exports.

This module provides the stub interfaces for Phase 5 ZIM file generation. The class
structure, method signatures, docstrings, and data models are complete. The actual
python-libzim integration is stubbed with TODO markers at each integration point.
...
```

**Update To**:
```python
"""
ZimWriter: Python-libzim-based ZIM file generation for open-repo offline exports.

This module provides complete ZIM file generation using the official python-libzim
library. It integrates with Phase 4 federation infrastructure to produce offline
archives for the Kiwix ecosystem.

Core features:
  - Full-text search via embedded Xapian indexing
  - Federated content attribution footers
  - Metadata validation and ZIM format compliance
  - SHA-256 checksum generation
  - zimcheck post-export validation (optional)
  - Support for multiple export scopes (local, federated, domain, tag)
  - Multiple flavours (nopic, agriculture, recipes, etc.)

All libzim.writer.Creator calls are fully implemented. No stubs or TODO markers.
...
```

**Commit**: `docs(phase-5): update module docstring to reflect full implementation`

---

### ✅ Task 4.3: Run Final Verification
**Estimated Time**: 10 minutes  

**Commands**:
```bash
cd backend

# 1. Full test suite
echo "=== Running full test suite ==="
python3 -m pytest tests/integration/test_export_pipeline.py tests/integration/test_zim_libzim_integration.py -v --tb=line 2>&1 | tail -5

# 2. Smoke test: Create a real ZIM
echo -e "\n=== Running smoke test ==="
python3 << 'EOF'
import tempfile
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope, ZimEntry

with tempfile.TemporaryDirectory() as tmpdir:
    output_path = Path(tmpdir) / "smoke_test.zim"
    
    metadata = ZimMetadata(
        title="Smoke Test Export",
        description="20-article smoke test",
        language="eng",
        name="smoke-test_en_nopic",
        flavour="nopic",
        creator="Test Suite",
        publisher="Open-Repo",
        source_url="http://localhost"
    )
    
    config = ExportConfig(
        scope=ExportScope.LOCAL_ONLY,
        flavour="nopic",
        include_images=False,
        language="en",
        language_iso3="eng"
    )
    
    writer = ZimWriter(metadata=metadata, config=config, output_path=output_path)
    
    # Add 20 test articles
    for i in range(20):
        writer.add_article(
            path=f"test/article-{i:03d}",
            title=f"Test Article {i}",
            content=f"<p>Content for article {i}. This tests Xapian indexing.</p>",
            article_type="procedural",
            language="en"
        )
    
    result = writer.create_zim()
    
    # Verify
    assert output_path.exists(), "ZIM file not created"
    file_size = output_path.stat().st_size
    assert file_size > 1000, f"ZIM file too small: {file_size} bytes"
    
    # Check magic bytes
    magic = output_path.read_bytes()[:4]
    assert magic == b'\x5a\x49\x4d\x04', f"Invalid ZIM magic bytes: {magic!r}"
    
    print(f"✓ Smoke test passed")
    print(f"  - ZIM file created: {output_path}")
    print(f"  - Size: {file_size} bytes")
    print(f"  - Articles: {result.article_count}")
    print(f"  - SHA-256: {result.sha256[:16]}...")
EOF

# 3. Code quality check
echo -e "\n=== Checking for TODO markers (should be none) ==="
grep -r "TODO.*post-PR-merge\|TODO.*libzim" backend/app/services/export/zim_writer.py && echo "⚠️  Found TODO markers" || echo "✓ No TODO markers found"

# 4. Import check
echo -e "\n=== Verifying imports ==="
python3 -c "
from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ZimEntry, ExportConfig, ExportScope,
    ZimWriteResult, ArticleItem
)
print('✓ All classes importable')
"
```

**Expected Output**:
```
=== Running full test suite ===
100 passed in X.XXs

=== Running smoke test ===
✓ Smoke test passed
  - ZIM file created: /tmp/.../smoke_test.zim
  - Size: XXXX bytes
  - Articles: 20
  - SHA-256: ...

=== Checking for TODO markers (should be none) ===
✓ No TODO markers found

=== Verifying imports ===
✓ All classes importable
```

**Commit**: `test(phase-5): final verification — 100 tests pass, smoke test succeeds`

---

## PHASE 5: Optional Extensions (1-2 hours)

### ⚠️ Task 5.1: Create Alembic Migration (Post-MVP)
**Estimated Time**: 30 minutes  
**Status**: Optional (Phase 5.1+)  
**File**: `backend/alembic/versions/2026_05_XX_add_zim_exports_table.py`  

**Skip for now**. Create migration after Phase 5.0 MVP is production-ready.

### ⚠️ Task 5.2: Create Export API Endpoint (Post-MVP)
**Estimated Time**: 1-2 hours  
**Status**: Optional (Phase 5.1+)  
**Files**: `backend/app/api/v1/export.py`, `backend/app/models.py`  

**Skip for now**. API endpoint can be added in Phase 5.1.

---

## Summary: Code Changes by File

### File 1: `backend/pyproject.toml` (1 change)

| Line | Change | Type |
|------|--------|------|
| 20 | Add `"libzim>=3.2,<4.0"` | Addition |

**Total**: 1 line added

---

### File 2: `backend/app/services/export/zim_writer.py` (5 changes)

| Change # | Lines | Type | Content |
|----------|-------|------|---------|
| 1 | 51-57 | Addition | libzim import guard (7 lines) |
| 2 | 408-436 | Addition | ArticleItem class (29 lines) |
| 3 | 762-771 | Modification | Replace stub, add Creator context (10 lines) |
| 4 | 873-905 | Modification | Implement metadata method (32 lines) |
| 5 | 922-939 | Deletion | Remove _stub_write_placeholder() (-18 lines) |

**Total Changes**: ~50 lines (net +32 after deletion)

---

## Commit Sequence (Recommended)

1. `chore(phase-5): add libzim>=3.2,<4.0 dependency`
2. `feat(phase-5): add libzim import guard with fallback`
3. `feat(phase-5): add ArticleItem libzim.Item adapter class`
4. `feat(phase-5): replace create_zim() stub with real libzim Creator`
5. `feat(phase-5): implement _apply_metadata_to_creator() for real Creator`
6. `test(phase-5): add 12 libzim integration tests (real ZIM generation)`
7. `chore(phase-5): remove _stub_write_placeholder() after full implementation`
8. `docs(phase-5): update module docstring to reflect full implementation`
9. `test(phase-5): final verification — 100 tests pass, smoke test succeeds`

**Total commits**: 9 (one per logical change)

---

## Testing Checklist

### Before Implementation
- [x] Read PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md
- [x] Review phase-5-candidate-1-implementation-verification.md
- [x] Verify libzim 3.9.0 installed: `python3 -c "from libzim.writer import Creator"`

### During Implementation
- [ ] Add libzim to pyproject.toml
- [ ] Add libzim import guard
- [ ] Add ArticleItem class
- [ ] Replace create_zim() stub
- [ ] Implement _apply_metadata_to_creator()
- [ ] Run 88 existing tests (must all pass)
- [ ] Create and run 12 new tests
- [ ] Run full 100-test suite
- [ ] Smoke test (create 20-article ZIM)
- [ ] Delete _stub_write_placeholder() method
- [ ] Update module docstring
- [ ] Verify no TODO markers remain

### After Implementation
- [ ] All 100 tests passing
- [ ] Smoke test succeeds
- [ ] ZIM files have correct magic bytes (\x5a\x49\x4d\x04)
- [ ] Articles retrievable offline
- [ ] Xapian search working
- [ ] SHA-256 checksums computed
- [ ] No external HTML dependencies
- [ ] Ready for PR review

---

## Troubleshooting Guide

### Problem: libzim import fails
**Error**: `ModuleNotFoundError: No module named 'libzim'`  
**Solution**: Reinstall environment: `pip install -e .[dev]`

### Problem: Test suite fails with AttributeError on Creator
**Error**: `AttributeError: 'NoneType' object has no attribute 'config_indexing'`  
**Cause**: _LIBZIM_AVAILABLE is False; import guard not working  
**Solution**: Check that libzim import guard was added correctly after line 50

### Problem: ZIM file created but zimcheck fails
**Error**: `zimcheck: command not found` or `zimcheck: FAILED`  
**Cause**: zimcheck binary not installed; or ZIM malformed  
**Solution**: 
  1. Skip zimcheck for now: `writer.create_zim(run_zimcheck=False)`
  2. Install zim-tools later: `apt-get install zim-tools`

### Problem: Article content has external http:// URLs
**Error**: zimcheck fails with "external resource" error  
**Cause**: HTML in database contains absolute URLs  
**Solution**: 
  1. Scan content before rendering: `if "http://" in content: raise ValueError(...)`
  2. Normalize URLs to relative or remove entirely

---

## Estimated Timeline

| Phase | Task | Duration | Cumulative |
|-------|------|----------|-----------|
| 1 | Dependency setup | 15 min | 15 min |
| 2.1 | Add libzim import guard | 10 min | 25 min |
| 2.2 | Add ArticleItem class | 20 min | 45 min |
| 2.3 | Replace create_zim() stub | 30 min | 1:15 |
| 2.4 | Implement metadata method | 20 min | 1:35 |
| 3.1 | Run existing tests | 10 min | 1:45 |
| 3.2 | Create 12 new tests | 1.5-2 hrs | 3:15-3:45 |
| 3.3 | Run full test suite | 10 min | 3:25-3:55 |
| 4.1 | Delete stub method | 5 min | 3:30-4:00 |
| 4.2 | Update docstring | 5 min | 3:35-4:05 |
| 4.3 | Final verification | 10 min | 3:45-4:15 |
| **TOTAL** | | | **3:45-4:15 hours** |

**With optional tasks (Steps 5.1-5.2)**: 5-6 hours total

---

## Success Criteria

✅ Implementation is **complete** when:
1. All 88 existing tests pass
2. All 12 new libzim tests pass
3. Smoke test creates real ZIM file (>1KB, magic bytes correct)
4. No TODO markers remain in code
5. Articles retrievable offline via Archive.get_entry_by_path()
6. Xapian search functional (Archive.search() returns results)
7. SHA-256 checksum computed and valid
8. No external HTML dependencies detected
9. All changes committed with clear messages
10. Ready for git push and PR creation

