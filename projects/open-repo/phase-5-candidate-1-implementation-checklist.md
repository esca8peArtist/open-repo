---
title: "Phase 5 Candidate 1 — ZimWriter/libzim Activation Checklist"
project: open-repo
phase: 5
candidate: 1
document_version: "4.0 (Session 1483)"
date: 2026-05-21
status: ready-to-execute
prerequisite: "feature/zimwriter-libzim-activation branch merged to master"
total_estimate: "8–14 hours (merge: 0.5h; activation: 7–13h)"
---

# Phase 5 Candidate 1: Hour-by-Hour Activation Checklist

**Two-stage structure**:
- **Stage A — Merge** (0.5 hours): Resolve doc conflicts, merge feature branch. No code risk.
- **Stage B — Activation** (7–13 hours): Apply the 3 pre-activation gaps, write post-activation tests, run smoke test, validate ZIM in Kiwix.

Both stages can be done back-to-back or split across sessions. Stage A unblocks nothing until Stage B begins.

---

## Pre-Flight Checks (10 minutes, before either stage)

Run all checks before touching any code. If any fail, investigate before proceeding.

| # | Check | Command | Expected |
|---|-------|---------|---------|
| PF1 | Architecture | `uname -m` | `aarch64` |
| PF2 | Python version | `python3 --version` | `Python 3.11.x` |
| PF3 | Clean working tree | `git status` | On master, no uncommitted changes |
| PF4 | Baseline tests | `cd projects/open-repo/backend && python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no` | `88 passed` |
| PF5 | Feature branch exists | `git branch -a \| grep zimwriter-libzim-activation` | Shows branch |
| PF6 | Disk space | `df -h /tmp` | >=2 GB free |
| PF7 | libzim in venv | `cd projects/open-repo/backend && uv run python3 -c "from libzim.writer import Creator; print('OK')"` | `OK` |

If PF4 returns anything other than `88 passed`, stop. The baseline must be green before any changes.

---

## Stage A: Merge (0.5 hours)

### A.1 — Resolve Documentation Conflicts (15 minutes)

The merge has exactly two conflicts, both in documentation files. Backend code merges cleanly.

```bash
cd /home/awank/dev/SuperClaude_Framework
git checkout master
git merge feature/zimwriter-libzim-activation --no-ff
```

When git reports conflicts, they will be in:
1. `projects/open-repo/phase-5-candidate-1-implementation-verification.md`
2. `projects/open-repo/phase-5-candidate-1-implementation-checklist.md`

**Resolution for both files**: Keep the master version. These are the current verified documents; the feature branch versions are earlier drafts.

```bash
# For each conflicting file:
git checkout --ours projects/open-repo/phase-5-candidate-1-implementation-verification.md
git checkout --ours projects/open-repo/phase-5-candidate-1-implementation-checklist.md
git add projects/open-repo/phase-5-candidate-1-implementation-verification.md
git add projects/open-repo/phase-5-candidate-1-implementation-checklist.md
```

All other files (backend code, tests, migration, other docs) should merge without conflict. If any backend file shows a conflict, stop and investigate.

### A.2 — Complete the Merge (5 minutes)

```bash
git commit -m "feat(open-repo): merge Phase 5 Candidate 1 — ZimWriter libzim integration"
```

**Verify immediately**:
```bash
cd projects/open-repo/backend
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no
```

Expected: `88 passed`. If count drops below 88, check git diff HEAD to identify what changed in the test file and investigate before proceeding.

### A.3 — Verify Feature Branch Changes Are Present (5 minutes)

```bash
# Confirm pyproject.toml now has libzim
grep libzim projects/open-repo/backend/pyproject.toml

# Confirm migration 003 exists
ls projects/open-repo/backend/alembic/versions/

# Confirm _LIBZIM_AVAILABLE exists in zim_writer.py
grep "_LIBZIM_AVAILABLE" projects/open-repo/backend/app/services/export/zim_writer.py | head -3

# Confirm ArticleItem class exists
grep "class ArticleItem" projects/open-repo/backend/app/services/export/zim_writer.py
```

Expected: libzim in pyproject.toml, 003 migration file present, _LIBZIM_AVAILABLE defined, ArticleItem class present.

Stage A is complete. The feature branch code is now on master. The stub is still active — nothing in production behavior has changed yet.

---

## Stage B: Activation (7–13 hours)

Stage B converts the merged stub implementation to live libzim. Ordering matters: complete the 5 sub-stages in sequence.

### B.1 — Hour 0–0.5: Update pyproject.toml Dependency (30 minutes)

**Why**: The feature branch added `libzim>=3.2,<4.0`. This should be tightened to `>=3.10.0,<4.0` to ensure the C++ 9.7.0 hardening patches (bad redirection handling, chunk handling) are included.

**File**: `projects/open-repo/backend/pyproject.toml`

Find the libzim line and update:
```toml
# Change from:
"libzim>=3.2,<4.0",

# Change to:
"libzim>=3.10.0,<4.0",
```

**Install the updated constraint**:
```bash
cd projects/open-repo/backend
uv pip install "libzim>=3.10.0,<4.0"
```

**Verify**:
```bash
uv run python3 -c "
from libzim.writer import Creator, Item, StringProvider, Hint
from libzim.version import get_libzim_version
print('C++ libzim version:', get_libzim_version())
print('All imports OK')
"
```

Expected: `C++ libzim version: 9.7.0` (or later). If the version stays at 9.5.1, it means libzim 3.10.0 was not installed — run `uv pip install --upgrade libzim` and check the wheel tag.

**Run tests to confirm nothing broke**:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no
```

Expected: `88 passed`.

**Success criteria**: libzim C++ >= 9.7.0, 88 tests still passing.

---

### B.2 — Hour 0.5–1.5: Add ZimExport ORM Model (1 hour)

**Why**: `alembic/versions/003_add_zim_exports_table.py` creates the `zim_exports` table but `app/models.py` has no corresponding SQLAlchemy class. Any code that queries `zim_exports` will fail with `AttributeError` at runtime until the ORM class exists.

**File**: `projects/open-repo/backend/app/models.py`

Open the file and add at the end (after the `NodePublicKey` class):

```python
import enum as _enum  # Add at top of file if not already present

class ZimExportStatus(str, _enum.Enum):
    GENERATING = "generating"
    VALIDATING = "validating"
    UPLOADING = "uploading"
    AVAILABLE = "available"
    SUPERSEDED = "superseded"
    DELETED = "deleted"
    ERROR = "error"


class ZimExport(Base):
    """Phase 5 offline export record — one row per completed ZIM file."""

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

Check which Column types are already imported in models.py and add any missing ones: `Float`, `Text`, `Boolean`, `Enum`. The `enum` import for `ZimExportStatus` may need to be added.

**Verify**:
```bash
cd projects/open-repo/backend
uv run python3 -c "
from app.models import ZimExport, ZimExportStatus
print('ZimExport OK:', ZimExport.__tablename__)
print('ZimExportStatus OK:', list(ZimExportStatus))
"
```

Expected: `ZimExport OK: zim_exports` and the 7 status enum values listed.

**Run tests**:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no
```

Expected: `88 passed` (tests do not yet import ZimExport; this step just ensures no import errors in models.py).

**Commit this change**:
```bash
git add projects/open-repo/backend/app/models.py
git commit -m "feat(open-repo): add ZimExport SQLAlchemy ORM model for Phase 5 export tracking"
```

**Success criteria**: `from app.models import ZimExport` succeeds, 88 tests still passing.

---

### B.3 — Hour 1.5–2: Fix Attribution Footer XSS (30 minutes)

**Why**: `source_node_url` and `source_node_name` from federation partners are interpolated directly into HTML without escaping. A compromised partner node could inject a `<script>` tag or a `javascript:` URL. This must be fixed before FEDERATED scope exports are activated. For Phase 5.1 MVP (LOCAL_ONLY scope), this path is not exercised — but fixing it now prevents the gap from propagating to Phase 5.2.

**File**: `projects/open-repo/backend/app/services/export/zim_writer.py`

**Step 1**: Add `import html` at the top of the file (with the other standard library imports):
```python
import html as _html_lib
```

**Step 2**: In `_apply_attribution_footer()`, locate the footer construction (lines 836–847) and replace with:

```python
        # Escape and validate before HTML interpolation
        safe_name = _html_lib.escape(source_node_name or "")
        # Allow only http/https URLs in the attribution link
        safe_url = (
            source_node_url
            if source_node_url and source_node_url.startswith(("https://", "http://"))
            else "#"
        )
        safe_license_name = _html_lib.escape(license_name or "") if license_name else ""
        safe_license_url = (
            license_url
            if license_url and license_url.startswith(("https://", "http://"))
            else "#"
        )

        license_link = ""
        if safe_license_url and safe_license_name:
            license_link = f' under <a href="{safe_license_url}">{safe_license_name}</a>'
        elif safe_license_name:
            license_link = f" under {safe_license_name}"

        footer = (
            f'\n<footer class="attribution">'
            f'<p>Originally published on '
            f'<a href="{safe_url}">{safe_name}</a>{license_link}.</p>'
            f'</footer>'
        )
```

**Run tests**:
```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no
```

Expected: `88 passed`. Verify that the attribution-related tests still pass (they use safe synthetic data, so the escape changes should be transparent).

**Commit**:
```bash
git add projects/open-repo/backend/app/services/export/zim_writer.py
git commit -m "fix(open-repo): escape federation attribution HTML to prevent stored XSS in ZIM exports"
```

**Success criteria**: 88 tests pass, `html.escape()` and scheme validation applied to all attribution interpolations.

---

### B.4 — Hour 2–2.5: Install zimcheck (20 minutes)

**Why**: The real libzim Creator produces a binary ZIM file. `zimcheck` validates ZIM structural correctness. Without it, the `run_zimcheck` parameter does nothing and exports could produce invalid ZIMs silently.

```bash
sudo apt-get install -y zim-tools
which zimcheck
zimcheck --version
```

Expected: `/usr/bin/zimcheck` and a version string (e.g., `3.1.3` for Debian Bookworm).

**If apt install fails** (e.g., package not in repo): Download a static binary from `https://github.com/openzim/zim-tools/releases`. Extract `zimcheck` to `/usr/local/bin/zimcheck` and run `chmod +x /usr/local/bin/zimcheck`.

**Note on zimcheck version strictness**: Debian Bookworm ships zim-tools 3.1.3. This version treats ZIM `Title` metadata longer than 30 characters as a hard error (not a warning). The production title `"Open-Repo: Full Library (English)"` is 34 characters. Either:
- Shorten the title to <=30 characters in `ZimMetadata`, OR
- Upgrade to zim-tools from upstream (3.3.0+ relaxes this to a warning)

Check: `zimcheck --version`. If it reports >= 3.3.0, no action needed. If 3.1.3, shorten the title.

---

### B.5 — Hour 2.5–4: Run Smoke Test with Real libzim (1.5 hours)

This is the first time the real Creator will be exercised on this hardware. Budget 1.5 hours for the smoke test plus debugging.

**Prerequisite**: `_LIBZIM_AVAILABLE` must be `True`. Confirm:
```bash
cd projects/open-repo/backend
uv run python3 -c "from app.services.export.zim_writer import _LIBZIM_AVAILABLE; print('Available:', _LIBZIM_AVAILABLE)"
```

Expected: `Available: True`. If `False`, libzim is not importable from within the backend package — check that `uv pip install libzim>=3.10.0` ran in the correct venv.

**Run the smoke test**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

uv run python3 - <<'SMOKE_TEST'
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ExportScope
)

output_path = Path("/tmp/open-repo-smoke.zim")

metadata = ZimMetadata(
    title="Open-Repo Smoke Test",       # Keep <=30 chars if using zim-tools 3.1.x
    description="Phase 5 smoke test",
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
    zimcheck_binary="zimcheck",
)

writer.add_article(
    path="index",
    content="<html><head><title>Open-Repo</title></head><body><h1>Open-Repo Offline Library</h1></body></html>",
    article_type="procedure",
)
writer.add_article(
    path="water/biosand-filter",
    content="<html><head><title>Biosand Water Filter</title></head><body><h1>Biosand Water Filter</h1><p>Build instructions.</p></body></html>",
    article_type="procedure",
)

result = writer.create_zim(run_zimcheck=True)
print(f"Articles: {result.article_count}")
print(f"File size: {result.file_size_bytes:,} bytes")
print(f"SHA-256: {result.sha256[:16]}...")
print(f"zimcheck passed: {result.zimcheck_passed}")
print(f"Generation time: {result.generation_duration_seconds:.2f}s")

if result.file_size_bytes < 1024:
    print("ERROR: File size < 1KB — stub fallback is running, libzim not active")
    sys.exit(1)
if not result.zimcheck_passed:
    print("ERROR: zimcheck failed — see logs above")
    sys.exit(1)
print("SMOKE TEST PASSED")
SMOKE_TEST
```

**Expected output**:
```
Articles: 2
File size: [>10,000] bytes
SHA-256: [16 hex chars]...
zimcheck passed: True
Generation time: [0.5–5.0]s
SMOKE TEST PASSED
```

**If file size < 1KB**: The `_LIBZIM_AVAILABLE = False` fallback is running. The import guard is not executing as expected. Check by running:
```bash
uv run python3 -c "
import sys
sys.path.insert(0, '.')
from app.services.export.zim_writer import _LIBZIM_AVAILABLE
print('LIBZIM_AVAILABLE:', _LIBZIM_AVAILABLE)
"
```

**If zimcheck fails with "Title too long"**: Edit `ZimMetadata.title` to be <=30 characters, or upgrade zim-tools.

**If zimcheck fails with "Missing illustration"**: The `_FALLBACK_ILLUSTRATION_PNG` bytes may be malformed. Test with `run_zimcheck=False` and inspect the raw bytes.

**If generation time > 60 seconds**: Normal for first run due to cold-start JIT. Repeat; subsequent runs should be under 10 seconds for a 2-article ZIM.

**Commit smoke test artifacts** (optional — the test script is ephemeral):
```bash
# Clean up temp file
rm -f /tmp/open-repo-smoke*.zim /tmp/open-repo-smoke*.sha256
```

---

### B.6 — Hour 4–6: Apply Alembic Migration 003 (2 hours)

**Why**: The `zim_exports` table must exist in PostgreSQL before any export job runs. The migration creates the table and its 4 indexes.

**Prerequisite**: PostgreSQL must be running. If it is not running locally, note the migration to apply at deployment time and skip to B.7.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Check current migration state
uv run alembic current

# Preview what will be applied
uv run alembic upgrade head --sql  # Dry run: shows the SQL without applying

# Apply the migration
uv run alembic upgrade head

# Verify
uv run alembic current
```

Expected: Output shows `003 (head)`.

**Verify the table was created**:
```bash
# If psql is available:
psql $DATABASE_URL -c "\d zim_exports" | head -20
```

Expected: 23 columns listed including `id`, `zim_uuid`, `name`, `flavour`, `period`, `status`, and the timestamp columns.

**If migration fails with "relation 002 does not exist"**: Run `alembic stamp 002` to mark the current state as migration 002, then re-run `alembic upgrade head`.

**If PostgreSQL is not available**: The ZimWriter code itself does not require the database — it writes to a file path. The database is only needed when the export service persists job records. Note this for deployment.

**Commit**:
```bash
# The migration file was already committed in Stage A. No new commit needed here.
# Just log that migration 003 has been applied.
```

---

### B.7 — Hour 6–8: Write Post-Activation Integration Tests (2 hours)

These 12 tests verify the ZIM binary format, not just interface contracts. They are required before declaring Phase 5.1 production-ready.

**File to create**: `projects/open-repo/backend/tests/unit/test_zim_writer_libzim.py`

The 12 test IDs from the implementation roadmap:

| # | Test ID | Category | Priority | Requires |
|---|---------|---------|---------|---------|
| 1 | `test_zim_writer_creates_real_zim_file` | Core output | P0 | libzim write |
| 2 | `test_zim_metadata_all_mandatory_fields` | Core output | P0 | libzim reader |
| 3 | `test_xapian_index_populated` | Core output | P0 | libzim reader + search |
| 4 | `test_article_count_matches_database` | Core output | P0 | libzim write |
| 5 | `test_html_no_external_dependencies` | Core output | P0 | BeautifulSoup |
| 6 | `test_zimcheck_passes_on_valid_export` | zimcheck | P0 | zimcheck binary |
| 7 | `test_zimcheck_fails_on_corrupted_archive` | zimcheck | P1 | zimcheck binary |
| 8 | `test_offline_read_article_by_path` | Offline read | P0 | libzim reader |
| 9 | `test_unicode_content_survives_roundtrip` | Offline read | P1 | libzim reader |
| 10 | `test_nopic_variant_excludes_images` | Offline read | P1 | libzim write |
| 11 | `test_period_collision_handling` | Sync | P1 | No external deps |
| 12 | `test_zimwriter_not_reusable_after_finalize` | Sync | P2 | No external deps |

Test 11 and 12 likely already pass in the existing suite (period collision and reusability guards are already tested). Focus implementation time on Tests 1, 4, 6, 8 (P0, require libzim binary).

For Test 3 (Xapian search): Use `libzim.reader.Archive` to open the written ZIM and run `archive.search("biosand filter")`. The Xapian index is embedded in the ZIM during creation.

**Run the new tests**:
```bash
python3 -m pytest tests/unit/test_zim_writer_libzim.py tests/integration/test_export_pipeline.py -q --tb=short
```

Expected: All 12 new tests + original 88 = 100 tests passing.

---

### B.8 — Hour 8–9: Optional Kiwix Device Validation (1 hour)

This step is required before declaring Phase 5.1 production-ready, but can be deferred to a separate session.

**Method A — kiwix-serve via Docker** (no physical device needed):
```bash
docker run -p 127.0.0.1:8080:80 \
  -v /tmp:/data \
  kiwix/kiwix-serve \
  /data/open-repo-smoke.zim
```

Open `http://127.0.0.1:8080` in a browser. Accept criteria:
- [ ] Index page loads without error
- [ ] Articles are navigable
- [ ] Full-text search returns results for keywords like "biosand" or "water"
- [ ] No external HTTP requests in browser DevTools network panel

**Method B — Kiwix Android**:
```bash
adb push /tmp/open-repo-smoke.zim /sdcard/kiwix/
```

Open Kiwix app, navigate to the transferred file.

---

### B.9 — Hour 9–10: Update README (1 hour)

`projects/open-repo/backend/README.md` has been partially updated on the feature branch (Phase 5 header and status added) but still lacks:
- ZimWriter section documenting the export pipeline
- Installation instructions for `libzim` and `zim-tools`
- ZIM file download/Kiwix usage instructions for end users
- Updated project structure tree showing `app/services/export/`
- Phase 5 offline export endpoint (when created)

Minimum acceptable update for activation: Add a "Phase 5: Offline Export (ZIM)" section to the README documenting the library export feature and how to access ZIM files via Kiwix.

---

### B.10 — Hour 10–11: Wire Export API Endpoint (optional, 1 hour)

`POST /api/exports` and `GET /api/exports/{job_id}` are not yet implemented. These are out of scope for the 5 core code changes but are required for the production export pipeline to be user-accessible.

For initial activation, ZimWriter can be triggered via a management script or direct Python invocation. The API endpoint is Phase 5.1 Step 10 from the implementation roadmap and can be implemented independently.

---

## Validation Checklist — Definition of Done

All items must be checked before Phase 5.1 is declared production-ready:

| # | Item | Verification | Required |
|---|------|-------------|---------|
| V1 | libzim >=3.10.0 in pyproject.toml | `grep libzim pyproject.toml` shows `>=3.10.0` | Yes |
| V2 | libzim C++ >= 9.7.0 installed | `uv run python3 -c "from libzim.version import get_libzim_version; print(get_libzim_version())"` | Yes |
| V3 | 88 + 12 = 100 tests passing | `pytest tests/ -q --tb=no` shows `100 passed` | Yes |
| V4 | Smoke test ZIM > 10 KB | `ls -la /tmp/open-repo-smoke.zim` | Yes |
| V5 | zimcheck passes on smoke ZIM | `zimcheck /tmp/open-repo-smoke.zim` exits 0 | Yes |
| V6 | SHA-256 sidecar verifiable | `sha256sum -c /tmp/open-repo-smoke.zim.sha256` | Yes |
| V7 | Migration 003 applied | `alembic current` shows `003 (head)` | Yes (deployment) |
| V8 | ZimExport ORM in models.py | `from app.models import ZimExport` succeeds | Yes |
| V9 | Attribution XSS fixed | `grep "html_module.escape\|_html_lib.escape" app/services/export/zim_writer.py` finds result | Yes (pre-FEDERATED) |
| V10 | _stub_write_placeholder removed | `grep "def _stub_write_placeholder" zim_writer.py` returns empty | Before go-live |
| V11 | No 0.0.0.0 bindings | `grep -r "0.0.0.0" projects/open-repo/backend/app/` returns nothing | Yes |
| V12 | ZIM opens in Kiwix | Manual visual test | Yes (pre-production) |
| V13 | _apply_metadata_to_creator try/except removed | Manual code review | Before go-live |

---

## Risk Flags

**Thermal (HIGH)**
ZIM creation runs CPU-intensive Zstandard compression. The Pi 5 reaches 87.8°C under compute. For the MVP corpus (500–1,000 articles, 15–45 second generation time), this is acceptable. For larger corpora or repeated exports, thermal throttling will extend generation time. Recommendation: install a heatsink before scheduling weekly automated exports. Do not run ZIM exports concurrently with other CPU-intensive tasks.

**Schema Migration Ordering (MEDIUM)**
Apply migration 003 (`alembic upgrade head`) before any application code that queries `zim_exports` is deployed. Running the application with migration 003 code but without the database table applied will cause a runtime error on any export API call. Safe path: apply migration in the same deployment step that activates the export endpoint.

**zimcheck Title Length (MEDIUM)**
Debian Bookworm's `zim-tools` package (version 3.1.3) treats `Title` metadata longer than 30 characters as a hard zimcheck failure. The example title `"Open-Repo: Full Library (English)"` is 34 characters and will fail. Check `zimcheck --version`. If < 3.3.0, either:
- Shorten `ZimMetadata.title` to <=30 characters in `ZimMetadata.validate()`, OR
- Add a check in the smoke test to detect this and advise accordingly

**Memory Buffering for Large Corpora (LOW for MVP)**
`ZimWriter` buffers all `ZimEntry` objects before calling `create_zim()`. Safe for <5,000 articles. The `TODO(post-PR-merge)` streaming mode must be implemented before Phase 5.2 corpora are generated.

**try/except AttributeError in _apply_metadata_to_creator (LOW)**
The broad `except AttributeError: pass` in `_apply_metadata_to_creator()` suppresses real Creator errors silently. If a `creator.add_metadata()` call raises `AttributeError` due to an API change in a future libzim version, the error would be swallowed and the export would proceed with missing metadata. Remove the try/except after integration tests confirm correctness with real libzim.

**Concurrent Export Jobs (LOW for MVP)**
APScheduler can overlap with a manual export trigger, producing duplicate ZIM files for the same name+flavour combination. Add a database lock check (query `zim_exports` for `status='generating'` with matching `name+flavour`) before starting any export job.

---

## Hour-by-Hour Timeline Summary

| Hours | Stage | Task | Risk |
|-------|-------|------|------|
| 0–0.5 | A | Merge with doc conflict resolution | Low |
| 0–0.5 | B.1 | Update libzim version pin, upgrade wheel | Low |
| 0.5–1.5 | B.2 | Add ZimExport ORM model | Low |
| 1.5–2 | B.3 | Fix attribution footer XSS | Low |
| 2–2.5 | B.4 | Install zimcheck via apt | Low |
| 2.5–4 | B.5 | Smoke test with real libzim | Medium (first real Creator run) |
| 4–6 | B.6 | Apply migration 003 (needs PostgreSQL) | Medium (DB dependency) |
| 6–8 | B.7 | Write 12 post-activation integration tests | Low |
| 8–9 | B.8 | Kiwix device validation (can defer) | Low |
| 9–10 | B.9 | README update | Low |
| 10–11 | B.10 | Export API endpoint (optional) | Low |
| **Total** | | **8–11 hours** (11–14 with optional steps) | |

**Minimum viable activation** (just what is required for Phase 5.1 to run in LOCAL_ONLY scope):
Stages A + B.1 + B.2 + B.4 + B.5 = ~3 hours. B.3 (XSS fix) required before FEDERATED scope. B.6 (migration) required before export jobs persist to DB.

---

## Post-Activation Monitoring

Once Phase 5.1 is live, watch these metrics:

| Metric | Alert threshold | Check |
|--------|----------------|-------|
| Export generation time | >300 seconds for nopic | `zim_exports.generation_duration_seconds` |
| zimcheck pass rate | Any failure on automated export | `zim_exports.zimcheck_passed = FALSE` |
| ZIM file size | <1 KB (stub running) or >500 MB (runaway) | `zim_exports.file_size_bytes` |
| Pi temperature | >87°C sustained during export | System monitor / MEMORY.md note |
| CDN upload errors | Any boto3 exception | Application logs |

Add `GET /api/exports/health` endpoint returning last successful export info and zimcheck pass rate for the past 7 days. This provides an observable readiness signal for Phase 5.2 planning.
