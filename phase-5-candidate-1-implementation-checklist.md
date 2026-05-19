---
title: "Phase 5 Candidate 1 — ZimWriter/libzim: Hour-by-Hour Implementation Checklist"
project: open-repo
phase: 5
candidate: 1
document_type: execution-checklist
status: ready-to-execute
date: 2026-05-19
session: 1365
prerequisite: "Phase 4 PRs merged to main; feature/zimwriter-libzim-activation branch exists"
total_estimate: "0.5–1h if merging feature branch; 8–11h if implementing from scratch"
---

# Phase 5 Candidate 1: Hour-by-Hour Implementation Checklist

**Critical decision before starting**: The implementation is already complete on `feature/zimwriter-libzim-activation` (commit `ec0ff7be`). There are two valid paths:

- **Path A (Recommended)**: Merge the existing feature branch. Total time: 0.5–1 hour.
- **Path B**: Implement from scratch using the roadmap. Total time: 8–11 hours.

This checklist covers both paths. Path A is presented first since it is recommended. Path B provides a complete from-scratch guide for reference.

---

## Pre-Flight Verification (Both Paths — 10 minutes)

Complete all items before touching any code.

| # | Check | Command | Expected result |
|---|-------|---------|----------------|
| PF1 | Python version | `python3 --version` | `Python 3.11.x` |
| PF2 | Architecture | `uname -m` | `aarch64` |
| PF3 | Working directory | `git status` | On `master`, no uncommitted changes |
| PF4 | Baseline tests pass | `cd projects/open-repo/backend && python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no` | `84 passed` |
| PF5 | Feature branch exists | `git branch -a \| grep zimwriter` | Shows `feature/zimwriter-libzim-activation` |
| PF6 | Disk space | `df -h /tmp` | At least 2 GB free |
| PF7 | Internet connectivity | `curl -s https://pypi.org/pypi/libzim/json \| python3 -c "import json,sys; d=json.load(sys.stdin); print(d['info']['version'])"` | `3.10.0` |

If PF4 fails (not 84 passed), stop and investigate before proceeding. The baseline must be green before any changes.

---

## Path A: Merge Existing Feature Branch (Recommended — 0.5–1 hour)

### A.1 — Environment Setup (15 minutes)

#### A.1.1 Install libzim wheel

**Duration**: 2 minutes  
**Working directory**: `projects/open-repo/backend`

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
uv pip install "libzim>=3.2,<4.0"
```

**Verify immediately**:
```bash
uv run python3 -c "
from libzim.writer import Creator, Item, StringProvider, Hint
import libzim
print('libzim version:', libzim.__version__)
print('Creator:', Creator)
print('All imports OK')
"
```

**Expected output**:
```
libzim version: 3.10.0
Creator: <class 'libzim.writer.Creator'>
All imports OK
```

**If install fails**: Check `uv pip install libzim --verbose` for the error. If "no matching distribution," verify Python version is 3.11 and architecture is aarch64. The wheel `libzim-3.10.0-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl` must be resolvable. If behind a proxy, set `UV_HTTP_TIMEOUT=120`.

#### A.1.2 Install zimcheck binary

**Duration**: 3 minutes  
**Parallel with A.1.1**: Yes, run in a separate terminal.

```bash
sudo apt-get install -y zim-tools
```

**Verify**:
```bash
which zimcheck
zimcheck --version
```

**Expected**: Path printed (e.g., `/usr/bin/zimcheck`), version printed (3.1.3 or similar).

**If apt fails**: Alternative — download a static zimcheck binary from `https://github.com/openzim/zim-tools/releases`. Extract to `/usr/local/bin/zimcheck` and `chmod +x`.

---

### A.2 — Merge Feature Branch (10 minutes)

**Duration**: 5–10 minutes  
**Risk**: Low — the branch has been triple-verified.

```bash
cd /home/awank/dev/SuperClaude_Framework

# Confirm the branch exists and check its tip
git log feature/zimwriter-libzim-activation --oneline -5

# Merge to master (fast-forward or create merge commit)
git checkout master
git merge feature/zimwriter-libzim-activation --no-ff -m "feat(open-repo): merge Phase 5 Candidate 1 — ZimWriter libzim integration"
```

**Expected result**: Clean merge, no conflicts. The merge brings in:
- Updated `projects/open-repo/backend/app/services/export/zim_writer.py` (1,155 lines, real libzim integration)
- New `projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py`
- Updated `projects/open-repo/backend/pyproject.toml` (libzim dependency added)

**If merge conflict occurs**: Check `git status` to identify conflicting files. The most likely conflict is in `ORCHESTRATOR_STATE.md` if that file was modified in both branches. Resolve by keeping master's version of ORCHESTRATOR_STATE.md and accepting all feature branch changes to the backend files.

---

### A.3 — Validate Against Real libzim (10 minutes)

**Duration**: 5–10 minutes  
**Critical checkpoint**: Do not proceed to A.4 unless these pass.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Run all 84 tests against real libzim
uv run python3 -m pytest tests/integration/test_export_pipeline.py -v --tb=short
```

**Expected**: 84 passed. Execution time will be significantly longer than 0.14s (stub) — expect 1–5 seconds per test that calls `create_zim()`, totalling 15–60 seconds for the full suite. This is correct: real libzim Creator I/O replaces the placeholder text write.

**Key tests to watch**:
- `test_create_zim_produces_output_file` — must pass (verifies real Creator writes a file)
- `test_create_zim_returns_result_with_sha256` — must pass (SHA-256 of real ZIM binary)
- `test_full_pipeline_with_synthetic_data` — must pass (full pipeline smoke test)

**If tests fail post-merge**: Run with `--tb=long` to get full tracebacks. Common failure modes:
- `ImportError: cannot import name 'Creator'` — libzim not in .venv; repeat A.1.1
- `ValueError: ZimWriter.create_zim() can only be called once` — test isolation issue; check if any fixture is shared across test instances
- `FileNotFoundError: output directory does not exist` — tmp_path fixture should handle this; run with `-s` to see output

---

### A.4 — Apply Database Migration (5 minutes)

**Duration**: 2–5 minutes  
**Pre-req**: PostgreSQL must be running. If only testing locally without a DB, skip and apply before first production export.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Check current migration state
uv run alembic current

# Apply migration 003
uv run alembic upgrade head

# Verify the migration applied
uv run alembic current
```

**Expected**: Output shows `003 (head)`.

**Verify the table exists**:
```bash
# If psql is available:
psql $DATABASE_URL -c "\d zim_exports"
```

**Expected**: Table with 28 columns listed.

**If running without DB**: Note the migration for deployment. The `zim_exports` table must exist before any export job is run. The migration has a proper `downgrade()` function for rollback.

---

### A.5 — Smoke Test with Synthetic ZIM (30 minutes)

**Duration**: 20–30 minutes  
**Pre-req**: A.1, A.2, A.3 complete; zimcheck installed.

This is the manual end-to-end test required before the PR is considered production-ready.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

uv run python3 - <<'SMOKE_TEST'
import sys
from pathlib import Path

# Ensure backend package is importable
sys.path.insert(0, str(Path.cwd()))

from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ExportScope
)

output_path = Path("/tmp/open-repo-smoke-test.zim")
output_path.parent.mkdir(parents=True, exist_ok=True)

metadata = ZimMetadata(
    title="Open-Repo Smoke Test",
    description="Smoke test export for Phase 5 verification",
    language="eng",
    name="open-repo_en_nopic",
    flavour="nopic",
    creator="Open-Repo",
    publisher="Open-Repo",
    source_url="https://example.open-repo.org",
)

config = ExportConfig(
    scope=ExportScope.LOCAL_ONLY,
    flavour="nopic",
    include_images=False,
    language="en",
    language_iso3="eng",
)

writer = ZimWriter(
    metadata=metadata,
    config=config,
    output_path=output_path,
    zimcheck_binary="zimcheck",  # Real zimcheck run
)

# Add index article (required — front article must exist)
writer.add_article(
    path="index",
    content="""<!DOCTYPE html><html lang='en'>
<head><title>Open-Repo Offline Library</title>
<style>body{font-family:sans-serif;margin:1rem;}</style></head>
<body><h1>Open-Repo Offline Library</h1>
<p>Welcome to the offline knowledge library.</p>
</body></html>""",
    article_type="procedure",
)

# Add a sample article
writer.add_article(
    path="water/biosand-filter",
    content="""<!DOCTYPE html><html lang='en'>
<head><title>Biosand Water Filter</title>
<style>body{font-family:sans-serif;margin:1rem;}</style></head>
<body><h1>Biosand Water Filter Construction</h1>
<p>Step-by-step guide to building a biosand filter for clean water.</p>
<p>Materials needed: fine sand, coarse gravel, concrete block, PVC pipe.</p>
</body></html>""",
    article_type="procedure",
)

print(f"Articles added: {writer.article_count}")

# Create real ZIM file with zimcheck validation
result = writer.create_zim(run_zimcheck=True)

print(f"Output file: {result.output_path}")
print(f"File size: {result.file_size_bytes:,} bytes")
print(f"SHA-256: {result.sha256}")
print(f"Article count: {result.article_count}")
print(f"zimcheck passed: {result.zimcheck_passed}")
print(f"Generation time: {result.generation_duration_seconds:.3f}s")
print()

if not result.zimcheck_passed:
    print("WARNING: zimcheck failed — check ZimWriter logs above for details")
    sys.exit(1)

if result.file_size_bytes < 1024:
    print("WARNING: ZIM file is suspiciously small (<1KB) — may be stub output")
    sys.exit(1)

print("Smoke test PASSED. ZIM file is at:", result.output_path)
print("Open with: kiwix-desktop /tmp/open-repo-smoke-test.zim")
SMOKE_TEST
```

**Expected output**:
```
Articles added: 2
Output file: /tmp/open-repo-smoke-test.zim
File size: [>10000] bytes
SHA-256: [64 hex chars]
Article count: 2
zimcheck passed: True
Generation time: [0.1–2.0]s

Smoke test PASSED. ZIM file is at: /tmp/open-repo-smoke-test.zim
Open with: kiwix-desktop /tmp/open-repo-smoke-test.zim
```

**If zimcheck fails**: Run `zimcheck /tmp/open-repo-smoke-test.zim` manually to see the specific error. Common causes and fixes:
- `Title is too long`: Shorten the ZIM title to under 30 characters in metadata
- `Missing illustration`: The fallback PNG should cover this; if failing, `zimcheck --version` and check if it is an older strict mode version
- `Empty archive`: libzim integration is not working; check `_LIBZIM_AVAILABLE` flag
- `Bad cluster data`: Usually a libzim version incompatibility; verify 3.10.0 is installed

**If ZIM file < 1KB**: The stub fallback is still running. Check that `_LIBZIM_AVAILABLE` is `True` by running `uv run python3 -c "from app.services.export.zim_writer import _LIBZIM_AVAILABLE; print(_LIBZIM_AVAILABLE)"` in the backend directory.

---

### A.6 — Optional: Kiwix Device Test (30 minutes)

**Duration**: 20–30 minutes  
**Required before production deployment; optional for merge approval.**

Transfer the smoke test ZIM to a device with Kiwix installed:

```bash
# To Android phone via adb (if connected):
adb push /tmp/open-repo-smoke-test.zim /sdcard/kiwix/

# To another Linux machine via rsync:
rsync -av /tmp/open-repo-smoke-test.zim user@other-machine:/tmp/

# Open in kiwix-serve (Docker):
docker run -p 127.0.0.1:8080:80 -v /tmp:/data kiwix/kiwix-serve --library /data/open-repo-smoke-test.zim
# Then open http://127.0.0.1:8080 in browser
```

**Acceptance criteria**:
- [ ] ZIM opens in Kiwix without error
- [ ] "Open-Repo Offline Library" index page displays
- [ ] "Biosand Water Filter" article is accessible via navigation
- [ ] No external HTTP requests made by articles (all content is self-contained)

---

### A.7 — Commit and PR (10 minutes)

**Duration**: 5–10 minutes

```bash
cd /home/awank/dev/SuperClaude_Framework

git status
git log --oneline -5

# If merge was clean and tests pass, create the PR via gh CLI:
gh pr create \
  --title "feat(open-repo): Phase 5 Candidate 1 — ZimWriter libzim integration" \
  --body "Activates real libzim integration in ZimWriter. All 84 tests passing with real libzim Creator. Includes Alembic migration 003 for zim_exports table.

## Changes
- libzim>=3.2,<4.0 added to pyproject.toml
- ArticleItem adapter class (libzim Item interface)
- create_zim() uses real Creator context manager (fallback stub for no-libzim)
- _apply_metadata_to_creator() implements all 11 ZIM metadata fields
- 003_add_zim_exports_table.py migration (28 columns, 3 indexes)

## Test results
84 passed with real libzim integration. zimcheck smoke test: PASS."
```

---

## Path B: From-Scratch Implementation (8–11 hours)

Use this path only if the feature branch is unavailable or needs to be rebuilt. This follows the roadmap's 13-step sequence precisely.

### B.0 — Branch Setup (5 minutes)

```bash
cd /home/awank/dev/SuperClaude_Framework
git checkout -b feature/zimwriter-libzim-integration master
```

---

### B.1 — Hour 0–0.5: Environment Setup (30 minutes)

#### B.1.1 Install libzim (2 min)
```bash
cd projects/open-repo/backend
uv pip install "libzim>=3.2,<4.0"
```

#### B.1.2 Install zimcheck (3 min)
```bash
sudo apt-get install -y zim-tools
```

#### B.1.3 Verify both installs (5 min)
```bash
uv run python3 -c "from libzim.writer import Creator; print('libzim OK')"
which zimcheck && zimcheck --version
```

#### B.1.4 Run baseline tests (5 min)
```bash
uv run python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no
```
**Must see**: `84 passed` before making any code changes.

---

### B.2 — Hour 0.5–1: pyproject.toml (5 minutes)

**File**: `projects/open-repo/backend/pyproject.toml`

Add to `[project.dependencies]` list:
```toml
"libzim>=3.2,<4.0",
```

After the `meilisearch` line. Result should be 10 dependencies total.

**Verify**:
```bash
uv pip install .  # Re-install with new dependency; should be a no-op since libzim already installed
```

---

### B.3 — Hour 1–1.5: Add Import Guard and Fallback PNG (30 minutes)

**File**: `projects/open-repo/backend/app/services/export/zim_writer.py`

**Location**: After the `from typing import Optional` import (line 50), before `logger = logging.getLogger(__name__)`.

**Add**:
```python
# TRY-EXCEPT import guard for libzim
try:
    from libzim.writer import Creator, Item, StringProvider, Hint
    _LIBZIM_AVAILABLE = True
except ImportError:
    _LIBZIM_AVAILABLE = False
    Creator = None  # type: ignore[assignment,misc]
    Item = object  # type: ignore[assignment,misc]
    StringProvider = None  # type: ignore[assignment,misc]
    Hint = None  # type: ignore[assignment,misc]

# Minimal 48x48 transparent PNG — fallback illustration when no icon is provided.
# Passes zimcheck with a warning; replace with a real branded icon before public release.
_FALLBACK_ILLUSTRATION_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\x00\x000"
    b"\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x0bIDATx\x9cc"
    b"\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
)
```

**Verify** (no errors expected):
```bash
uv run python3 -c "from app.services.export.zim_writer import _LIBZIM_AVAILABLE; print('Available:', _LIBZIM_AVAILABLE)"
```
**Expected**: `Available: True`

**Duration estimate**: 15 minutes (including verification).

---

### B.4 — Hour 1.5–2: Add ArticleItem Class (30 minutes)

**File**: `projects/open-repo/backend/app/services/export/zim_writer.py`

**Location**: After the `ZimEntry` dataclass definition and before the `ZimWriter` class. Look for the comment `# ---------------------------------------------------------------------------` block before `class ZimWriter:`.

**Add this class immediately before `class ZimWriter:`**:
```python
# ---------------------------------------------------------------------------
# libzim adapter class
# ---------------------------------------------------------------------------


class ArticleItem(Item):
    """
    Adapter from ZimEntry to libzim's Item interface.

    libzim.writer.Creator.add_item() requires an Item subclass.
    This bridges ZimEntry (our data model) to libzim's API.

    Thread safety: Each ArticleItem instance is consumed once by add_item()
    and not retained.
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
uv run python3 -c "
from app.services.export.zim_writer import ArticleItem, ZimEntry
e = ZimEntry(path='test', title='Test', content='<html></html>', mime_type='text/html', is_front_article=True)
item = ArticleItem(e)
print('path:', item.get_path())
print('title:', item.get_title())
print('mimetype:', item.get_mimetype())
print('ArticleItem OK')
"
```

**Duration estimate**: 20 minutes.

---

### B.5 — Hour 2–3: Replace create_zim() Stub (1 hour)

**File**: `projects/open-repo/backend/app/services/export/zim_writer.py`

**Location**: Inside `ZimWriter.create_zim()`, around line 759. Find:
```python
        # TODO(post-PR-merge): Replace this stub with actual python-libzim Creator calls
        # See the docstring above for the correct implementation pattern.
        # For now, write a placeholder file to allow test harness to run.
        self._stub_write_placeholder()
```

**Replace with**:
```python
        if not _LIBZIM_AVAILABLE:
            # Fallback stub for environments without libzim
            placeholder_content = (
                f"STUB ZIM PLACEHOLDER\n"
                f"name={self.metadata.name}\n"
                f"articles={self._article_count}\n"
                f"resources={self._resource_count}\n"
                f"generated_at={datetime.utcnow().isoformat()}\n"
            ).encode("utf-8")
            self.output_path.write_bytes(placeholder_content)
        else:
            # Real libzim Creator integration
            with Creator(str(self.output_path)) as creator:
                creator.set_mainpath("index")
                self._apply_metadata_to_creator(creator)
                for entry in self._entries:
                    creator.add_item(ArticleItem(entry))
            # Creator.__exit__ triggers ZIM file finalization and write
```

**Run tests immediately after**:
```bash
uv run python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=short
```

**Expected**: 84 passed (now using real Creator for tests with `run_zimcheck=False`).

**If test count drops**: A test that previously used stub behavior may fail with real libzim. Check the specific failure with `-v` and `--tb=long`.

**Duration estimate**: 30 minutes for the edit + 30 minutes for test debugging if needed.

---

### B.6 — Hour 3–4: Implement _apply_metadata_to_creator() (1 hour)

**File**: `projects/open-repo/backend/app/services/export/zim_writer.py`

**Location**: `_apply_metadata_to_creator()` method, around line 870. Find the method body which currently contains only `pass` (and the TODO docstring).

**Replace the entire method body** (the `pass` line and the TODO in the docstring) with:
```python
    def _apply_metadata_to_creator(self, creator: object) -> None:
        """Apply all ZimMetadata fields to a libzim Creator instance."""
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

**Run tests**:
```bash
uv run python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=short
```

**Expected**: 84 passed.

**Also verify metadata fields individually**:
```bash
uv run python3 - <<'EOF'
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

Path("/tmp/meta-test").mkdir(exist_ok=True)
metadata = ZimMetadata(
    title="Meta Test",
    description="Testing metadata",
    language="eng",
    name="open-repo_en_nopic",
    flavour="nopic",
    creator="Test",
    publisher="Test",
    source_url="https://example.org",
)
config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
writer = ZimWriter(metadata=metadata, config=config, output_path=Path("/tmp/meta-test/test.zim"))
writer.add_article(path="index", content="<html><head><title>T</title></head><body>T</body></html>", article_type="procedure")
result = writer.create_zim(run_zimcheck=False)
print("Metadata applied — file size:", result.file_size_bytes)
EOF
```

**Duration estimate**: 45 minutes.

---

### B.7 — Hour 4–4.5: Run Full Validation with zimcheck (30 minutes)

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

uv run python3 - <<'ZIMCHECK_TEST'
from pathlib import Path
from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

Path("/tmp/zimcheck-test").mkdir(exist_ok=True)

metadata = ZimMetadata(
    title="ZimCheck Test",
    description="Testing zimcheck validation",
    language="eng",
    name="open-repo_en_nopic",
    flavour="nopic",
    creator="Open-Repo",
    publisher="Open-Repo",
    source_url="https://example.org",
)
config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
writer = ZimWriter(
    metadata=metadata,
    config=config,
    output_path=Path("/tmp/zimcheck-test/test.zim"),
    zimcheck_binary="zimcheck",
)

writer.add_article(
    path="index",
    content="<html><head><title>ZimCheck Test</title></head><body><h1>Test</h1><p>Content</p></body></html>",
    article_type="procedure",
)

result = writer.create_zim(run_zimcheck=True)
print(f"zimcheck passed: {result.zimcheck_passed}")
print(f"File size: {result.file_size_bytes:,} bytes")
ZIMCHECK_TEST
```

**Expected**: `zimcheck passed: True`, file size > 10,000 bytes.

**If zimcheck returns False**: Run manually to see errors:
```bash
zimcheck /tmp/zimcheck-test/test.zim
```

Interpret errors using the roadmap's Risk 2 guidance. Most common fixable issues:
- Title too long: Shorten to < 30 chars
- Illustration problem: Check `_FALLBACK_ILLUSTRATION_PNG` bytes
- Name field invalid: Must match `[a-z0-9][a-z0-9_-]+` pattern

---

### B.8 — Hour 4.5–5: Remove Stub Method and Re-test (30 minutes)

**File**: `projects/open-repo/backend/app/services/export/zim_writer.py`

**Remove** the `_stub_write_placeholder()` method entirely (approximately lines 914–931 in the original master file). The inline fallback in `create_zim()` replaces it.

**Run tests to confirm nothing breaks**:
```bash
uv run python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=short
```

**Expected**: 84 passed (same count as before removal).

**Commit the implementation**:
```bash
git add projects/open-repo/backend/app/services/export/zim_writer.py
git add projects/open-repo/backend/pyproject.toml
git commit -m "feat(open-repo): activate libzim integration in ZimWriter — real Creator, ArticleItem, metadata"
```

---

### B.9 — Hour 5–6: Alembic Migration (1 hour)

**File to create**: `projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py`

Create this file with the following content (copy exactly — all 28 columns required):

```python
"""Add zim_exports table for Phase 5 offline export tracking."""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import BigInteger, Integer, String, DateTime, Float, Text, Boolean
from datetime import datetime

revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None


def upgrade():
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
    op.drop_index('idx_zim_exports_is_current')
    op.drop_index('idx_zim_exports_name_flavour')
    op.drop_table('zim_exports')
```

**Apply the migration**:
```bash
uv run alembic upgrade head
uv run alembic current  # Should show: 003 (head)
```

**Commit**:
```bash
git add projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py
git commit -m "feat(open-repo): add zim_exports Alembic migration (003)"
```

**Duration estimate**: 30 minutes to write, 20 minutes to apply and verify.

---

### B.10 — Hour 6–8: New Integration Tests (2 hours)

Write the 12 new integration tests from the roadmap's Test Matrix. These are the tests that verify the ZIM binary format (not just the interface contracts). Target files:
- `tests/unit/test_zim_writer.py` (Tests 1–5, 7, 10–12)
- `tests/integration/test_zimcheck_validation.py` (Tests 6–7)
- `tests/integration/test_zim_readback.py` (Tests 8–9)

Refer to the roadmap's Test Matrix section for exact test IDs, inputs, and expected results.

**Run new tests**:
```bash
uv run python3 -m pytest tests/ -k "zim" -v
```

**Duration estimate**: 2 hours (writing + debugging).

---

### B.11 — Hour 8–9: Manual Kiwix Test

Same procedure as Path A, Step A.6.

---

### B.12 — Hour 9–10: PR Creation

```bash
git push origin feature/zimwriter-libzim-integration
gh pr create --title "feat(open-repo): Phase 5 Candidate 1 — ZimWriter libzim integration" \
  --body "Full implementation of ZimWriter with real libzim Creator. See PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md for design decisions."
```

---

## Docker Test Environment (Optional, Either Path)

For isolated testing without affecting the local environment:

```bash
# Create a minimal test container
docker run -it --rm \
  -v /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend:/app \
  -w /app \
  python:3.11-slim bash

# Inside container:
pip install uv
uv venv .venv-docker
uv pip install -r pyproject.toml  # Includes libzim
apt-get update && apt-get install -y zim-tools
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=short
```

**Note**: Docker containers on this ARM64 host will use the ARM64 libzim wheel automatically — same as the host environment. No architecture mismatch.

---

## Validation Checklist — Definition of Done

The feature is complete when all of the following are true:

| # | Item | Verification method |
|---|------|-------------------|
| V1 | 84 existing tests pass with real libzim | `pytest tests/integration/test_export_pipeline.py -q` shows `84 passed` |
| V2 | ZIM file is > 10KB (real binary, not stub) | `ls -la /tmp/*.zim` |
| V3 | zimcheck passes on smoke-test ZIM | `zimcheck /tmp/open-repo-smoke-test.zim` exits 0 |
| V4 | SHA-256 sidecar can be verified | `sha256sum -c /tmp/open-repo-smoke-test.zim.sha256` |
| V5 | Migration 003 applied cleanly | `alembic current` shows `003 (head)` |
| V6 | libzim dependency in pyproject.toml | `grep libzim pyproject.toml` finds the entry |
| V7 | `_stub_write_placeholder()` removed | `grep _stub_write_placeholder zim_writer.py` finds nothing |
| V8 | ZIM opens in Kiwix (desktop or serve) | Manual visual test |
| V9 | No 0.0.0.0 bindings introduced | `grep -r "0.0.0.0" projects/open-repo/backend/app/` finds nothing new |
| V10 | No breaking changes to Phase 4 federation | All Phase 4 tests still pass |

---

## Flags and Blockers

**Potential blocker: zimcheck version strictness**
zim-tools 3.1.3 (Debian Bookworm) treats Title > 30 characters as a zimcheck error in some modes. The production title "Open-Repo: Full Library (English)" is 34 characters. If zimcheck rejects it, either shorten the title or upgrade to zim-tools from upstream APT. Command to check: `zimcheck --version`. Upstream 3.3.0 relaxed this to a warning.

**Potential blocker: PostgreSQL unavailable for migration**
`alembic upgrade head` requires a running PostgreSQL. If the local DB is not running, apply the migration at deployment time. The ZimWriter itself does not require the DB to exist — only the export tracking persistence does.

**Uncertain timing: Kiwix device test**
The Kiwix device test (A.6 / B.11) requires a phone or device with Kiwix installed. If not available locally, `kiwix-serve` via Docker provides an equivalent test in the browser.

**Non-blocker: No API endpoint for export jobs**
`POST /api/exports` does not exist yet. This is expected — ZimWriter must be callable from a script or admin command for initial smoke testing. Building the API endpoint is roadmap Step 10 and is correctly out of scope for Candidate 1's 5 code changes.
