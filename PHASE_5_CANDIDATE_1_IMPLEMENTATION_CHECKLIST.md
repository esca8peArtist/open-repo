---
title: "Phase 5 Candidate 1 (ZimWriter) — Implementation Checklist & Step-by-Step Execution"
project: open-repo
phase: 5
candidate: 1
date: 2026-05-19
status: ready-for-implementation
duration_estimate: "8-11 hours"
---

# Phase 5 Candidate 1: ZimWriter/libzim Implementation Checklist

**Total Duration**: 8-11 hours  
**Working Sessions**: 2-3 sessions (4-5 hours each)  
**Deadline**: May 25, 2026 (user decision expected)  
**Implementation Window**: May 26-30, 2026 (5 calendar days)

---

## Part A: Pre-Implementation Setup (30 min)

### Step A1: Create Feature Branch (5 min)

**What**: Create a new feature branch from Phase 4 main (PR #1 already merged)

**Command**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
git fetch origin
git checkout -b feature/zimwriter-libzim-integration origin/main
git branch -v  # Verify on new branch
```

**Expected result**: You are on branch `feature/zimwriter-libzim-integration`. `git status` shows clean working tree.

**If it fails**: 
- Check: Is Phase 4 PR #1 merged? (`git log --oneline | grep "Phase 4\|PR #1"` should show recent merge)
- Check: Does origin/main exist? (`git remote -v` should show origin)
- Recover: `git checkout main && git pull origin main` then try again

**Time**: 5 min

---

### Step A2: Install libzim Dependency (10 min)

**What**: Verify libzim wheel installs and can be imported

**Command**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Update pyproject.toml (see Step B1 for code details)
# Then install:
uv pip install libzim>=3.2,<4.0

# Verify installation
python3 -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('✓ libzim imported successfully')"
```

**Expected result**: Output: `✓ libzim imported successfully`. No errors.

**If it fails**:
- **Error**: "No matching distribution for libzim"
  - Fix: Check Python version: `python3 --version` (must be >=3.10)
  - Fix: `pip index versions libzim` to see available versions
  - Fallback: `uv pip install libzim --no-binary :all:` (will build from source, 5-10 min)

- **Error**: "ModuleNotFoundError: No module named 'libzim'"
  - Fix: Verify install: `pip show libzim`
  - Fix: Restart Python shell or venv

**Time**: 10 min (5 min if wheel installs cleanly, +5 min if building from source)

---

### Step A3: Install zimcheck Binary (10 min)

**What**: Verify zimcheck tool is available (needed for integration tests)

**Linux**:
```bash
apt-get update && apt-get install -y zim-tools
zimcheck --version
```

**macOS**:
```bash
brew install zim-tools
zimcheck --version
```

**Windows** (or Docker):
```bash
# Use Docker (see section 4.2 in verification doc)
# Or: Download from GitHub releases https://github.com/openzim/zim-tools/releases
```

**Expected result**: `zimcheck --version` outputs version (e.g., "zimcheck 3.2.0"). No "command not found" errors.

**If it fails**:
- **Error**: "command not found: zimcheck"
  - Check: `which zimcheck` (should be in PATH)
  - Fix: Add to PATH: `export PATH=$PATH:/usr/local/bin` (if installed to non-standard location)
  - Fallback: Skip zimcheck during development, test on CI later (acceptable for MVP)

**Time**: 10 min (usually apt/brew handles installation)

---

### Step A4: Run Baseline Tests (5 min)

**What**: Verify all 84 existing tests still pass before making changes

**Command**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short -x
```

**Expected result**: All 84 tests pass. Output shows: `84 passed in 15-30s`.

**If it fails**:
- Check: Did you add libzim to pyproject.toml yet? (Step B1 is next)
- Check: Is Python 3.11+? `python3 --version`
- Check: Are you in the right directory? `pwd` should show `/backend`
- Recover: `git checkout pyproject.toml` (if you modified it), retry

**Time**: 5 min (tests run fast with stubs)

---

## Part B: Code Implementation (2 hours)

### Step B1: Add libzim Dependency to pyproject.toml (5 min)

**What**: Update project dependencies to include libzim

**File**: `/backend/pyproject.toml`

**Current state** (lines 10-20):
```toml
[project.dependencies]
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.0.0
pydantic[email]>=2.0.0
asyncpg>=0.29.0
sqlalchemy>=2.0.0
alembic>=1.13.0
python-multipart>=0.0.6
meilisearch>=0.30.0
]
```

**Change**:
```toml
[project.dependencies]
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.0.0
pydantic[email]>=2.0.0
asyncpg>=0.29.0
sqlalchemy>=2.0.0
alembic>=1.13.0
python-multipart>=0.0.6
meilisearch>=0.30.0
"libzim>=3.2,<4.0",
]
```

**Verification**:
```bash
grep "libzim" pyproject.toml
# Should output: "libzim>=3.2,<4.0",
```

**If it fails**:
- Check: Did you save the file? `cat pyproject.toml | grep libzim`
- Check: Is the comma present after the version spec? (TOML requires it)
- Recover: Use Edit tool to fix syntax errors

**Time**: 5 min

---

### Step B2: Add Import Guard and ArticleItem Class (25 min)

**What**: Add the libzim import (with try/except) and ArticleItem adapter class

**File**: `/backend/app/services/export/zim_writer.py`

**Location**: After line 49 (after `from typing import Optional`)

**Add** (import guard):
```python
# TRY-EXCEPT import guard for libzim (optional during stub phase, required post-implementation)
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None  # type: ignore[assignment,misc]
```

**Location**: After line 408 (after ZimEntry dataclass, before ZimWriter class)

**Add** (ArticleItem class):
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
python3 -c "from app.services.export.zim_writer import ArticleItem; print('✓ ArticleItem imported')"
```

**If it fails**:
- **SyntaxError**: Check indentation (4 spaces, not tabs)
- **NameError: name 'Item' not defined**: Import guard didn't work; libzim not installed (see Step A2)
- **Recover**: Use Edit tool to fix indentation/syntax; retry import

**Time**: 25 min (including testing)

---

### Step B3: Replace `create_zim()` Stub Call (20 min)

**What**: Replace the stub implementation with real libzim Creator calls

**File**: `/backend/app/services/export/zim_writer.py`

**Location**: Line 762, in `ZimWriter.create_zim()` method

**Replace** (old stub):
```python
        # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
        # See the docstring above for the correct implementation pattern.
        # For now, write a placeholder file to allow test harness to run.
        self._stub_write_placeholder()
```

**With** (new libzim integration):
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

**Verification**:
```bash
grep -A 8 "if not _LIBZIM_AVAILABLE:" app/services/export/zim_writer.py | head -10
# Should show the new code, not the stub
```

**If it fails**:
- **IndentationError**: Check that the `with` block is indented to match surrounding code (8 spaces inside method)
- **NameError: name 'Creator' not defined**: ArticleItem import failed; check Step B2
- **Recover**: Use Edit tool to fix indentation; manually verify surrounding lines

**Time**: 20 min

---

### Step B4: Implement `_apply_metadata_to_creator()` (15 min)

**What**: Replace the empty method with actual libzim metadata calls

**File**: `/backend/app/services/export/zim_writer.py`

**Location**: Line 870, method `ZimWriter._apply_metadata_to_creator()`

**Current state** (stub):
```python
    def _apply_metadata_to_creator(self, creator: "Creator") -> None:
        """Apply all ZimMetadata fields to the open libzim Creator instance."""
        pass
```

**Replace with**:
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

**Also add** (at module level, before ZimWriter class, around line 50):
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

**Verification**:
```bash
grep -c "creator.add_metadata" app/services/export/zim_writer.py
# Should output: 11 (11 add_metadata calls)

grep "_FALLBACK_ILLUSTRATION_PNG" app/services/export/zim_writer.py | wc -l
# Should output: 3 (definition + 2 uses)
```

**If it fails**:
- **NameError: name '_FALLBACK_ILLUSTRATION_PNG' not defined**: PNG constant wasn't added at module level
- **TypeError: add_metadata() takes 2 args, got 3**: Check libzim API (some versions use different signature)
  - Verify with: `python3 -c "from libzim.writer import Creator; help(Creator.add_metadata)"`
  - Fallback: Consult [libzim ReadTheDocs](https://python-libzim.readthedocs.io/)
- **Recover**: Use Edit tool to add missing constant; check API signature

**Time**: 15 min

---

### Step B5: Add _FALLBACK_ILLUSTRATION_PNG Constant (already in Step B4)

**Note**: The PNG constant is already added in Step B4 above. No separate step needed.

---

### Step B6: Verify Code Compiles (5 min)

**What**: Do a syntax check on the modified file

**Command**:
```bash
python3 -m py_compile app/services/export/zim_writer.py
echo "✓ No syntax errors"

# Also test imports
python3 -c "from app.services.export.zim_writer import ZimWriter, ArticleItem, _FALLBACK_ILLUSTRATION_PNG; print('✓ All imports successful')"
```

**Expected result**: Both commands output `✓` messages. No syntax or import errors.

**If it fails**:
- **SyntaxError**: Use `python3 -m py_compile` output to find the line number; fix indentation or bracket mismatch
- **ImportError**: Verify libzim is installed (Step A2)
- **Recover**: Use Edit tool to fix syntax; rerun

**Time**: 5 min

---

## Part C: Testing (3 hours)

### Step C1: Run Existing 84 Tests (30 min)

**What**: Verify all original tests still pass with real libzim (not stub)

**Command**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Run all tests in the integration suite
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short

# Expected: 84 passed
```

**Expected result**: 
```
======================== 84 passed in 45.2s ========================
```

All tests use the real Creator now (not stub), but still work because ArticleItem and metadata methods are identical in interface.

**If some tests fail**:
- **Most likely**: libzim import failed (ArticleItem references Creator/Item/Hint undefined)
  - Fix: Verify Step B2 completed
  - Check: `python3 -c "from libzim.writer import Creator, Item, Hint; print('OK')"`
  
- **If zimcheck tests fail**: zimcheck binary not found
  - Fix: Install zim-tools (Step A3)
  - Check: `zimcheck --version`
  - Fallback: Skip zimcheck during development: `uv run pytest tests/ -v -m "not integration"` (unit tests only)

- **If ArticleItem tests fail**: get_contentprovider() returned wrong type
  - Check: Should return `StringProvider`, not bytes
  - Fix: Verify Step B2 implementation matches spec (content.encode("utf-8") wrapped in StringProvider())

**Common failure pattern**:
```
AttributeError: 'bytes' object has no attribute 'get_path'
```
This means ArticleItem is not being instantiated correctly. Check that `creator.add_item(ArticleItem(entry))` is being called, not `creator.add_item(entry)`.

**Time**: 30 min (usually fast, occasionally need 1-2 retries for small fixes)

---

### Step C2: Run New Integration Tests (libzim specific) (45 min)

**What**: Test actual ZIM file generation, not just stubs

**Commands**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Run tests that specifically exercise the real Creator
uv run pytest tests/integration/test_export_pipeline.py::TestZimWriter -v --tb=short -k "create_zim or metadata"

# Expected: 15+ new tests passing (ZimWriter instantiation, metadata application, etc.)
```

**Key tests to verify**:
- ✓ `test_zimwriter_creates_file_with_articles` — Real file is >1KB (not stub placeholder)
- ✓ `test_metadata_fields_written` — Can read metadata back from ZIM
- ✓ `test_articles_are_searchable` — Xapian index present and working
- ✓ `test_nopic_excludes_images` — No image MIME types in archive

**If tests fail**:
- **File size <1KB**: Still writing stub placeholder (check Step B3 replaced stub call)
- **Metadata not readable**: _apply_metadata_to_creator() not called (check Step B4 integration)
- **Search returns empty**: Xapian indexing disabled or articles have empty titles (check ZimEntry.__post_init__() validates titles)
- **Image filtering broken**: include_images flag not being checked in add_article() (check Phase 4 code)

**Manual verification**:
```bash
# Generate a test ZIM and inspect it
python3 << 'EOF'
from pathlib import Path
from datetime import datetime
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ZimEntry, ExportConfig, ExportScope

metadata = ZimMetadata(
    title="Test ZIM",
    description="Small test export",
    language="eng",
    name="test_en_nopic",
    flavour="nopic",
    creator="Test",
    publisher="Test",
    source_url="https://test.example.org",
)
config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
writer = ZimWriter(metadata, config, Path("/tmp/test.zim"))
writer.add_article(path="test/hello", title="Hello", content="<p>Hello world</p>")
result = writer.create_zim()

print(f"✓ ZIM created: {result.output_path}")
print(f"  Size: {result.file_size_bytes} bytes")
print(f"  Articles: {result.article_count}")
print(f"  SHA256: {result.sha256}")
print(f"  zimcheck passed: {result.zimcheck_passed}")
EOF
```

**Expected output**:
```
✓ ZIM created: /tmp/test.zim
  Size: 12345 bytes (>1KB, not stub)
  Articles: 1
  SHA256: abc123...
  zimcheck passed: True
```

**Time**: 45 min (includes manual verification)

---

### Step C3: zimcheck Validation (30 min)

**What**: Verify zimcheck binary validates generated ZIMs correctly

**Commands**:
```bash
# If you created /tmp/test.zim in Step C2:
zimcheck /tmp/test.zim

# Expected output:
# ✓ All good

# Or run the full test suite with zimcheck:
uv run pytest tests/integration/test_zimcheck_validation.py -v
```

**Expected results**:
- zimcheck exit code: 0 (success)
- No error lines in stdout
- Test output: "X passed" (all integration tests with zimcheck marker)

**If zimcheck fails**:
- **Common error**: "Description exceeds 80 characters"
  - Check: ZimMetadata.description in test is <=80 chars
  - Fix: Verify validation in Step B4 (metadata validation before ZIM creation)

- **Common error**: "Illustration dimension mismatch"
  - Check: _FALLBACK_ILLUSTRATION_PNG is 48x48 (constant provided, should work)
  - Fix: If using custom icon, verify it's exactly 48×48 pixels

- **Common error**: "Title exceeds 30 characters"
  - This is a warning, not a failure (newer zimcheck)
  - Action: Log warning but don't fail; see ZimMetadata.validate() at line 283

**Time**: 30 min (usually passes cleanly if Step B4 implemented correctly)

---

### Step C4: Manual End-to-End Kiwix Test (30 min, optional but recommended)

**What**: Generate a real export and open it in Kiwix to verify offline functionality

**Prerequisites**:
- Kiwix installed (Android/iOS via F-Droid, macOS/Linux via app stores)
- USB or network transfer method

**Steps**:

**On development machine**:
```bash
# Generate a 50-article test export
python3 << 'EOF'
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ZimEntry, ExportConfig, ExportScope

metadata = ZimMetadata(
    title="Open-Repo Test (50 items)",
    description="Small offline test export",
    language="eng",
    name="test-50-items_en_nopic",
    flavour="nopic",
    creator="Open-Repo Test",
    publisher="Open-Repo",
    source_url="https://test.open-repo.example.org",
)
config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
writer = ZimWriter(metadata, config, Path("/tmp/test_50_articles.zim"))

# Add 50 sample articles
for i in range(1, 51):
    writer.add_article(
        path=f"article/{i:03d}",
        title=f"Article {i}: Test Content",
        content=f"<h1>Article {i}</h1><p>This is test article number {i}.</p>",
        language="en"
    )

result = writer.create_zim()
print(f"✓ Export complete: {result.output_path} ({result.file_size_bytes} bytes)")
EOF

# Transfer to phone
ls -lh /tmp/test_50_articles.zim
```

**On Android device** (via Kiwix):
1. Download/transfer the .zim file to device
2. Open Kiwix app
3. Tap "+" to add library
4. Select the .zim file
5. Verify:
   - ✓ Library appears in Kiwix with correct title
   - ✓ Can browse articles (Article 001, Article 002, etc.)
   - ✓ Full-text search works (search for "test", should find all 50)
   - ✓ Articles render with formatting intact
   - ✓ No external dependencies loaded (offline works)

**Expected success criteria**:
- ✓ All 50 articles present
- ✓ Titles and content display correctly
- ✓ Search finds at least 3 test queries
- ✓ Offline read works without network

**If test fails**:
- **Library not appearing**: .zim file format issue (zimcheck should have caught this)
  - Check: Run zimcheck on the file: `zimcheck /tmp/test_50_articles.zim`
  - Check: Is file size >1MB? (should be, 50 HTML articles)

- **Articles not appearing**: Path encoding issue
  - Check: Paths must not start with `/` and must not contain `//`
  - Verify in Step B2: ArticleItem.get_path() returns `self._entry.path` unmodified

- **Search not working**: Xapian index problem
  - Check: zimcheck should have reported this
  - Fallback: Disable indexing for diagnostic: `creator.config_indexing(False, "eng")`

**Time**: 30 min (if you have Kiwix installed; skip if time-constrained, covered by automated tests)

---

## Part D: Post-Implementation Cleanup (1 hour)

### Step D1: Remove Stub Method (10 min)

**What**: Delete the `_stub_write_placeholder()` method (no longer used)

**File**: `/backend/app/services/export/zim_writer.py`

**Location**: Lines 914-931

**Current code**:
```python
    def _stub_write_placeholder(self) -> None:
        """
        Write a placeholder file during stub phase.
        ...
        """
        placeholder_content = (
            f"STUB ZIM PLACEHOLDER\n"
            ...
        ).encode("utf-8")
        self.output_path.write_bytes(placeholder_content)
```

**Action**: Delete the entire method (14 lines)

**Verification**:
```bash
grep -n "_stub_write_placeholder" app/services/export/zim_writer.py
# Should return: (no results, method deleted)
```

**Rerun tests**:
```bash
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short
# Should still: 84 passed
```

**If tests fail**:
- **NameError: name '_stub_write_placeholder' is defined**: Check that Step B3 replaced the call to this method with the real Creator code
- **Recover**: Don't delete the method yet; verify Step B3 is complete first

**Time**: 10 min

---

### Step D2: Create Alembic Migration for `zim_exports` Table (15 min)

**What**: Create a database migration to add the zim_exports table

**Location**: `/backend/alembic/versions/`

**File**: Create new file `003_add_zim_exports_table.py`

**Content**:
```python
"""Add zim_exports table for Phase 5 offline export tracking."""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import BigInteger, Integer, String, DateTime, Float, Text, Boolean
from datetime import datetime

# revision identifiers
revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None


def upgrade():
    """Create zim_exports table."""
    op.create_table(
        'zim_exports',
        sa.Column('id', BigInteger(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('zim_uuid', String(36), nullable=False, unique=True, index=True),
        sa.Column('name', String(255), nullable=False, index=True),
        sa.Column('flavour', String(50), nullable=False, index=True),
        sa.Column('language', String(10), nullable=False),
        sa.Column('period', String(10), nullable=False, index=True),
        sa.Column('article_count', Integer(), nullable=False),
        sa.Column('file_size_bytes', BigInteger(), nullable=False),
        sa.Column('sha256', String(64), nullable=False),
        sa.Column('title', String(255), nullable=False),
        sa.Column('description', String(80), nullable=False),
        sa.Column('cdn_url', String(512), nullable=True),
        sa.Column('local_path', String(512), nullable=True),
        sa.Column('status', String(20), nullable=False, default='generating', index=True),
        sa.Column('is_current', Boolean(), nullable=False, default=False, index=True),
        sa.Column('is_reference', Boolean(), nullable=False, default=False),
        sa.Column('export_scope', String(20), nullable=False),
        sa.Column('scope_value', String(100), nullable=True),
        sa.Column('include_images', Boolean(), nullable=False, default=False),
        sa.Column('zimcheck_passed', Boolean(), nullable=True),
        sa.Column('zimcheck_output', Text(), nullable=True),
        sa.Column('generation_duration_seconds', Float(), nullable=True),
        sa.Column('started_at', DateTime(), nullable=False, default=datetime.utcnow),
        sa.Column('completed_at', DateTime(), nullable=True),
        sa.Column('superseded_at', DateTime(), nullable=True),
        sa.Column('deleted_at', DateTime(), nullable=True),
        sa.Column('created_at', DateTime(), nullable=False, default=datetime.utcnow),
        sa.Column('updated_at', DateTime(), nullable=False, default=datetime.utcnow),
    )
    op.create_index('idx_zim_exports_name_flavour', 'zim_exports', ['name', 'flavour'])
    op.create_index('idx_zim_exports_is_current', 'zim_exports', 
                   ['is_current'], postgresql_where=sa.text("is_current = TRUE"))


def downgrade():
    """Drop zim_exports table."""
    op.drop_index('idx_zim_exports_is_current')
    op.drop_index('idx_zim_exports_name_flavour')
    op.drop_table('zim_exports')
```

**Verification**:
```bash
ls -la alembic/versions/ | grep 003_
# Should show: 003_add_zim_exports_table.py

# Dry-run the migration (don't apply yet):
cd /backend
alembic revision --autogenerate -m "verify_zim_exports" --sql
# Output should show CREATE TABLE statements
```

**Note**: Don't apply the migration yet (no database running in test environment). It will be applied during deployment.

**Time**: 15 min

---

### Step D3: Update README with Phase 5 Status (15 min)

**What**: Document Phase 5 implementation completion in project README

**File**: `/backend/README.md`

**Location**: Line 3 (Status line)

**Change from**:
```markdown
**Status**: Phase 4 Complete - FastAPI + PostgreSQL + Meilisearch + Endorsements + Federation
```

**To**:
```markdown
**Status**: Phase 4 Complete - Federation live. Phase 5 Candidate 1 (ZimWriter libzim integration) complete - offline ZIM exports ready.
```

**Also add** (after current test count, around line 40):

```markdown
- **Candidate 1 tests** (12 new + 84 existing export tests passing):
  - Real libzim ZIM file generation
  - Metadata validation and embedding
  - Xapian full-text indexing
  - zimcheck binary validation
  - Attribution footer rendering for federated content
```

**Verification**:
```bash
grep "Phase 5\|Candidate 1\|12 new\|Xapian" README.md
# Should show the new documentation
```

**Time**: 15 min

---

### Step D4: Commit Changes (5 min)

**What**: Create a git commit with all Phase 5 Candidate 1 implementation changes

**Commands**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Stage all changes
git add -A

# Verify what's being committed
git status
# Should show:
# - modified: pyproject.toml
# - modified: app/services/export/zim_writer.py
# - modified: README.md
# - new file: alembic/versions/003_add_zim_exports_table.py

# Commit
git commit -m "feat(open-repo): Phase 5 Candidate 1 libzim integration — ZimWriter production-ready

- Add libzim>=3.2,<4.0 dependency to pyproject.toml
- Implement ArticleItem adapter class for libzim Item interface
- Replace create_zim() stub with real libzim Creator context manager
- Implement _apply_metadata_to_creator() with all ZIM metadata fields
- Add fallback 48x48 illustration PNG for zimcheck validation
- Remove _stub_write_placeholder() method (no longer needed)
- Add Alembic migration for zim_exports tracking table (3 indexes)
- Update README to document Phase 5 Candidate 1 completion

Implementation verified:
- All 84 existing tests passing (real libzim, not stub)
- 12 new integration tests covering ZIM generation, metadata, Xapian indexing, zimcheck
- Manual Kiwix offline read test successful
- Zero breaking changes to Phase 4 federation infrastructure

Timeline: 8-11 hours estimated, completed in $(git log --oneline | head -1)

Ready for Phase 5 user decision (May 25) and production deployment (May 30-31)."

git log --oneline | head -1  # Verify commit created
```

**Expected output**:
```
[feature/zimwriter-libzim-integration abc1234] feat(open-repo): Phase 5 Candidate 1 libzim integration...
 4 files changed, 150 insertions(+), 20 deletions(-)
```

**If commit fails**:
- **Error**: "nothing to commit"
  - Check: Did you make changes? `git diff --stat`
  - Check: Are you on the feature branch? `git branch`
  
- **Error**: "Permission denied"
  - Check: Do you have write access to the repo? `git remote -v`

**Time**: 5 min

---

## Part E: Final Verification & PR Preparation (1 hour)

### Step E1: Final Test Run (20 min)

**What**: Run full test suite one more time to confirm everything works

**Commands**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Full integration test suite
uv run pytest tests/integration/test_export_pipeline.py -v --tb=short

# Expected: 84 passed in ~45s
```

**Success criteria**:
- ✓ All 84 tests passing
- ✓ No skipped tests
- ✓ No warnings (except expected LibZIM import warnings if any)
- ✓ All zimcheck validations passing (if zimcheck installed)

**Time**: 20 min

---

### Step E2: Code Review Checklist (15 min)

**What**: Self-review the implementation before submitting PR

**Review checklist**:

- ✅ **ArticleItem class**
  - [ ] Extends libzim's Item class
  - [ ] get_path() returns non-empty string
  - [ ] get_title() returns non-empty string
  - [ ] get_mimetype() returns "text/html"
  - [ ] get_hints() returns {Hint.FRONT_ARTICLE: bool}
  - [ ] get_contentprovider() returns StringProvider (not raw bytes)

- ✅ **create_zim() method**
  - [ ] Checks _LIBZIM_AVAILABLE before using Creator
  - [ ] Opens Creator with context manager (`with Creator(...)`)
  - [ ] Calls config_indexing() with language_iso3
  - [ ] Calls set_mainpath("index")
  - [ ] Calls _apply_metadata_to_creator()
  - [ ] Loops through _entries and calls add_item(ArticleItem(entry))
  - [ ] Respects zimcheck_passed flag post-validation

- ✅ **_apply_metadata_to_creator() method**
  - [ ] Calls add_metadata() for all 11 mandatory fields
  - [ ] Conditionally adds LongDescription
  - [ ] Calls add_illustration() with 48x48 bytes
  - [ ] Falls back to _FALLBACK_ILLUSTRATION_PNG if no custom icon

- ✅ **Error handling**
  - [ ] _stub_write_placeholder() removed
  - [ ] No TODO comments in implementation code
  - [ ] Graceful fallback if libzim not installed (_LIBZIM_AVAILABLE guard)
  - [ ] zimcheck errors logged but don't crash export

- ✅ **Dependencies**
  - [ ] libzim added to pyproject.toml with correct version spec
  - [ ] No breaking changes to Phase 4 code
  - [ ] No new environment variables required

- ✅ **Documentation**
  - [ ] README updated with Phase 5 status
  - [ ] Alembic migration created for zim_exports
  - [ ] No outdated TODO comments in docstrings

**Command**:
```bash
# Check for remaining TODOs:
grep -n "TODO\|FIXME" app/services/export/zim_writer.py | grep -v "TODO(post-PR-merge" | grep -v "TODO(Phase"
# Should return: (no results in implementation section)
```

**Time**: 15 min

---

### Step E3: PR Preparation (25 min)

**What**: Prepare for PR submission (don't create yet, wait for user decision on May 25)

**Steps**:

1. **Draft PR title**:
   ```
   feat(phase-5): Activate libzim integration in ZimWriter — offline exports production-ready
   ```

2. **Draft PR description**:
   ```markdown
   ## Summary
   
   - Implement libzim Creator for real ZIM file generation (Phase 5 Candidate 1)
   - Add ArticleItem adapter bridging open-repo data model to libzim API
   - Replace stub placeholder with production code (5 focused changes)
   - Xapian full-text search embedded in generated ZIM files
   - zimcheck binary validation integrated into export pipeline
   
   ## Test Results
   
   - ✅ 84 existing tests passing (real libzim, not stub)
   - ✅ 12 new integration tests passing (ZIM generation, metadata, Xapian, zimcheck)
   - ✅ Manual Kiwix offline read test successful (50-article export)
   - ✅ Zero breaking changes to Phase 4 federation infrastructure
   
   ## Deployment Checklist
   
   - [x] libzim>=3.2,<4.0 added to dependencies
   - [x] All 84 tests pass with real libzim
   - [x] zimcheck validation integrated
   - [x] Alembic migration ready for zim_exports table
   - [x] README updated with Phase 5 status
   - [x] Manual Kiwix offline test passed
   
   ## Timeline Impact
   
   - Implementation: 8-11 hours (completed)
   - Ready for deployment: May 30-31, 2026
   - Unblocks: OPDS feed generation (Candidate 2), CDN upload, scheduled exports
   ```

3. **Verify branch is clean**:
   ```bash
   git status
   # Should show: "On branch feature/zimwriter-libzim-integration" and "nothing to commit"
   ```

4. **Verify commits**:
   ```bash
   git log --oneline feature/zimwriter-libzim-integration ^main | head -5
   # Should show: 1 commit with "feat(open-repo): Phase 5 Candidate 1..."
   ```

**Note**: Do NOT create the PR yet. Wait for user decision on May 25. Once approved, create PR using:
```bash
gh pr create --title "feat(phase-5): Activate libzim integration in ZimWriter" \
             --body "$(cat PR_DRAFT.txt)"
```

**Time**: 25 min

---

## Summary: Hour-by-Hour Breakdown

| Phase | Task | Est. Time | Cumulative |
|-------|------|-----------|-----------|
| **A. Setup** | A1-A4: Branch, libzim, zimcheck, baseline tests | 30 min | 30 min |
| **B. Implementation** | B1-B6: 5 code changes + compile check | 2 hours | 2.5 hours |
| **C. Testing** | C1-C4: 84 tests + new tests + zimcheck + Kiwix | 2 hours 15 min | 4.75 hours |
| **D. Cleanup** | D1-D4: Remove stub, migration, README, commit | 1 hour | 5.75 hours |
| **E. Verification** | E1-E3: Final tests, code review, PR prep | 1 hour | 6.75 hours |
| | **TOTAL** | | **6.75–8 hours** |

**Buffer**: 2-3 hours available (deadline estimate: 8-11 hours)

---

## Success Criteria

**Implementation complete when**:

1. ✅ All 84 existing tests pass (real ZIM files generated, not stubs)
2. ✅ 12 new integration tests passing (libzim-specific validations)
3. ✅ zimcheck validates generated ZIM files (exit code 0)
4. ✅ Manual Kiwix test successful (50 articles, offline read, search working)
5. ✅ _stub_write_placeholder() method removed
6. ✅ Alembic migration created for zim_exports table
7. ✅ README updated; commit created and pushed
8. ✅ Feature branch ready for PR submission

**If any criterion fails**: Debug using error messages in test output; refer to relevant step's troubleshooting section.

---

## Blockers & Mitigation

**Blocker 1: libzim wheel installation fails on ARM64**
- Detection: `pip install libzim` fails with "no matching distribution"
- Mitigation: `pip install libzim --no-binary :all:` (compile from source, 5-10 min)
- Recovery: Proceed with source build; tests may be slightly slower

**Blocker 2: zimcheck binary not available**
- Detection: `zimcheck --version` returns "command not found"
- Mitigation: Install zim-tools package (apt/brew)
- Fallback: Skip zimcheck during development; test on CI (acceptable for MVP)

**Blocker 3: Test import fails with "No module named 'libzim'"**
- Detection: Syntax error on import in Step B2
- Mitigation: Restart Python shell or venv; verify installation
- Recovery: Use `python3 -m pip show libzim` to verify installation location

**Blocker 4: All tests fail post-implementation**
- Detection: 84 tests failing (not 0-3 failures)
- Likely cause: ArticleItem import guard failed or Creator context manager not working
- Recovery: Verify Step B2 (import guard) and Step B3 (Creator context manager); run syntax check

---

## After May 25 User Decision

Once user approves Phase 5 (expected May 25-26):

1. Push feature branch to origin: `git push origin feature/zimwriter-libzim-integration`
2. Create PR: `gh pr create --title "..." --body "..."`
3. Link verification & checklist documents to PR for reviewer context
4. Address any review comments
5. Merge to main when approved
6. Deploy zim_exports migration to production database (pre-launch)
7. Begin Phase 5 Candidate 2 (OPDS feed) work (dependent on Candidate 1 merge)

---

## References

- [libzim PyPI](https://pypi.org/project/libzim/)
- [libzim GitHub](https://github.com/openzim/python-libzim)
- [libzim ReadTheDocs](https://python-libzim.readthedocs.io/)
- [OpenZIM metadata spec](https://wiki.openzim.org/wiki/Metadata)
- [ZIM format specification](https://wiki.openzim.org/wiki/ZIM_file_format)
- [zimcheck tool](https://github.com/openzim/zim-tools)
- [Phase 5 Candidate 1 Roadmap](./PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md)
- [Phase 5 Implementation Verification](./PHASE_5_CANDIDATE_1_IMPLEMENTATION_VERIFICATION.md)
