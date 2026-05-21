---
title: "Phase 5.1 — ZimWriter libzim Activation: Step-by-Step Implementation Checklist"
project: open-repo
phase: "5.1"
document_version: "5.0 (Session 1492 — pre-merge prep for May 25-26 user decision)"
date: 2026-05-22
status: ready-to-execute
feature_branch: feature/zimwriter-libzim-activation
prerequisite: "User merge approval (May 25-26 decision window)"
total_estimate: "3–4 hours (merge + critical-path activation); 8–10 hours (full production-ready)"
---

# Phase 5.1 Implementation Checklist: ZimWriter libzim Activation

**Two-stage structure**:

- **Stage A — Merge** (30 minutes): Resolve two documentation file conflicts, merge feature branch. Backend code merges cleanly.
- **Stage B — Activation** (2.5–3.5 hours critical path): Fix ORM type mismatch, install zimcheck, run smoke test. Full production-ready adds post-activation tests, XSS fix, and Kiwix validation.

Stage A and Stage B can be done back-to-back in a single session or split across sessions. Stage A unblocks nothing in production until Stage B begins — the stub implementation remains active on master after merge until the real libzim Creator is exercised.

**Current state as of May 22, 2026**:

- libzim 3.10.0 installed (C++ 9.7.0) — no installation step needed
- 240/240 backend tests passing on master; 88/88 export-specific tests passing
- All 5 code changes complete on feature branch, pending merge
- New finding: ORM type mismatch (Float/Boolean vs Integer) — 5-minute fix, documented in Step B.1

---

## Pre-Flight Checks (10 minutes — run before either stage)

All checks must pass before touching any code. If any fail, investigate before proceeding.

| # | Check | Command | Expected |
|---|-------|---------|---------|
| PF1 | Architecture | `uname -m` | `aarch64` |
| PF2 | Python version | `python3 --version` | `Python 3.11.x` |
| PF3 | Clean working tree | `git status` | On master, no uncommitted changes |
| PF4 | Baseline tests (full suite) | `cd projects/open-repo/backend && python3 -m pytest tests/ -q --tb=no` | `240 passed, 19 skipped` |
| PF5 | Baseline tests (export only) | `python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no` | `88 passed` |
| PF6 | Feature branch exists | `git branch -a \| grep zimwriter-libzim-activation` | Shows branch |
| PF7 | libzim importable | `cd projects/open-repo/backend && .venv/bin/python -c "from libzim.writer import Creator; print('OK')"` | `OK` |
| PF8 | libzim C++ version | `.venv/bin/python -c "from libzim.version import get_libzim_version; print(get_libzim_version())"` | `9.7.0` |
| PF9 | Disk space | `df -h /tmp` | >=2 GB free |

If PF4 returns anything other than `240 passed, 19 skipped`, stop and investigate. The baseline must be green before any changes.

---

## Stage A: Merge (30 minutes)

**Risk**: Low. Backend code merges cleanly; only documentation files have conflicts.

### A.1 — Initiate the Merge (5 minutes)

```bash
cd /home/awank/dev/SuperClaude_Framework
git checkout master
git merge feature/zimwriter-libzim-activation --no-ff
```

Git will report exactly two conflicts in documentation files. All other files — including `zim_writer.py`, `pyproject.toml`, `app/models.py`, `alembic/versions/003_add_zim_exports_table.py`, and `test_export_pipeline.py` — will merge automatically.

**Expected conflict report**:
```
CONFLICT (content): Merge conflict in projects/open-repo/phase-5-candidate-1-implementation-verification.md
CONFLICT (content): Merge conflict in projects/open-repo/phase-5-candidate-1-implementation-checklist.md
Automatic merge failed; fix conflicts and then commit the result.
```

If git reports any conflict in a backend Python file (`.py`) or `pyproject.toml`, stop immediately and investigate before proceeding.

### A.2 — Resolve Documentation Conflicts (10 minutes)

Both conflicts are in documentation files. Resolution for both: keep the master version (the master versions are current; the feature branch versions are earlier drafts).

```bash
git checkout --ours projects/open-repo/phase-5-candidate-1-implementation-verification.md
git checkout --ours projects/open-repo/phase-5-candidate-1-implementation-checklist.md
git add projects/open-repo/phase-5-candidate-1-implementation-verification.md
git add projects/open-repo/phase-5-candidate-1-implementation-checklist.md
```

**Note**: The other project files changed on the feature branch (seedwarden, mfg-farm, resistance-research, systems-resilience documents) will merge automatically without conflict. These were committed to the feature branch during session work while the branch was checked out and do not overlap with master changes.

### A.3 — Complete the Merge (5 minutes)

```bash
git commit -m "feat(open-repo): merge Phase 5 Candidate 1 — ZimWriter libzim integration

- 5 code changes: import guard, ArticleItem class, create_zim() real impl,
  _apply_metadata_to_creator() fix, _stub_write_placeholder removal
- libzim>=3.10.0,<4.0 added to pyproject.toml
- ZimExport ORM model added to app/models.py
- Migration 003 (zim_exports table) added
- Stub remains active until Stage B activation"
```

### A.4 — Verify Post-Merge State (10 minutes)

Run the full verification:

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# 1. Test suite must still pass at baseline
python3 -m pytest tests/ -q --tb=no
# Expected: 240 passed, 19 skipped

# 2. Export tests specifically
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no
# Expected: 88 passed

# 3. Feature branch changes are present
grep libzim pyproject.toml
# Expected: "libzim>=3.10.0,<4.0"

grep "class ZimExport" app/models.py
# Expected: class ZimExport(Base):

ls alembic/versions/
# Expected: 001_add_federation_partners.py, 002_add_federation_conflicts.py, 003_add_zim_exports_table.py

grep "_LIBZIM_AVAILABLE" app/services/export/zim_writer.py | head -2
# Expected: _LIBZIM_AVAILABLE = True / _LIBZIM_AVAILABLE = False

grep "class ArticleItem" app/services/export/zim_writer.py
# Expected: class ArticleItem(Item):
```

If all checks pass, Stage A is complete. The feature branch code is on master. The stub is still active — no production behavior has changed yet.

**Blocker**: If any test drops below 240 (full suite) or 88 (export suite), stop and diff `git show HEAD -- tests/integration/test_export_pipeline.py` to identify what changed.

---

## Stage B: Activation (2.5–3.5 hours critical path; 6–8 hours full)

Stage B converts the merged stub to live libzim. Complete sub-stages in order. Estimated durations are conservative.

### B.1 — Fix ORM Type Mismatch (15 minutes) — NEW FINDING

**Why**: `generation_duration_seconds` is defined as `Float` in migration 003 but `Integer` in the ORM model. Boolean columns (`is_current`, `is_reference`, `include_images`, `zimcheck_passed`) use `Integer(0/1)` in the ORM but `Boolean` in the migration. Fix now before any export job writes to the database.

**File**: `projects/open-repo/backend/app/models.py`

First, confirm the current import line to see which types are already imported:

```bash
grep "^from sqlalchemy import" projects/open-repo/backend/app/models.py
```

Expected current imports: `Column, String, DateTime, JSON, Text, Integer, ForeignKey, Enum, BigInteger`

Missing: `Float, Boolean`

Add `Float` and `Boolean` to the import line, then update the five columns in the `ZimExport` class:

```python
# In the ZimExport class, change:
is_current = Column(Integer, nullable=False, default=0, index=True)
is_reference = Column(Integer, nullable=False, default=0)
include_images = Column(Integer, nullable=False, default=0)
zimcheck_passed = Column(Integer, nullable=True)
generation_duration_seconds = Column(Integer, nullable=True)

# To:
is_current = Column(Boolean, nullable=False, default=False, index=True)
is_reference = Column(Boolean, nullable=False, default=False)
include_images = Column(Boolean, nullable=False, default=False)
zimcheck_passed = Column(Boolean, nullable=True)
generation_duration_seconds = Column(Float, nullable=True)
```

**Verify**:
```bash
cd projects/open-repo/backend
.venv/bin/python -c "
from app.models import ZimExport
cols = {c.name: str(c.type) for c in ZimExport.__table__.columns}
print('generation_duration_seconds:', cols.get('generation_duration_seconds'))
print('is_current:', cols.get('is_current'))
print('zimcheck_passed:', cols.get('zimcheck_passed'))
"
# Expected: FLOAT, BOOLEAN, BOOLEAN
```

**Run tests**:
```bash
python3 -m pytest tests/ -q --tb=no
# Expected: 240 passed, 19 skipped
```

**Commit**:
```bash
git add projects/open-repo/backend/app/models.py
git commit -m "fix(open-repo): correct ZimExport ORM column types (Float/Boolean vs Integer)"
```

**Estimated duration**: 15 minutes  
**Risk**: Low — nullable columns, no data exists yet  
**Blocker if skipped**: Export timing data will truncate to whole seconds; Boolean ORM queries return 0/1 instead of True/False

---

### B.2 — Install zimcheck (15 minutes)

**Why**: The real libzim Creator produces a binary ZIM file. `zimcheck` validates the file's structural integrity. Without it, `run_zimcheck=True` in `create_zim()` silently skips validation.

```bash
sudo apt-get install -y zim-tools
which zimcheck
zimcheck --version
```

**Expected**: `/usr/bin/zimcheck` and version string.

**CRITICAL: Title length check**

Debian Bookworm ships `zim-tools 3.1.3`. This version treats `Title` metadata longer than 30 characters as a hard zimcheck failure (not a warning). The smoke test in Step B.3 uses a short title, so this is safe for testing. For production exports:

- If `zimcheck --version` reports < 3.3.0: ensure `ZimMetadata.title` is <=30 characters in all export jobs, OR upgrade zim-tools from upstream.
- If `zimcheck --version` reports >= 3.3.0: no action needed.

**If apt install fails** (package not in repo): Download a static binary from `https://github.com/openzim/zim-tools/releases`. Extract `zimcheck` to `/usr/local/bin/zimcheck` and run `chmod +x /usr/local/bin/zimcheck`.

**Estimated duration**: 5-15 minutes (depending on network)  
**Risk**: Low  
**Blocker if skipped**: Cannot validate ZIM file integrity; production exports may produce silently invalid ZIM files

---

### B.3 — Smoke Test with Real libzim (45 minutes including debugging budget)

This is the first time the real Creator will run on this hardware. Budget extra time for first-run debugging.

**Prerequisite**: Confirm `_LIBZIM_AVAILABLE` is `True` in the merged code:

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
.venv/bin/python -c "
from app.services.export.zim_writer import _LIBZIM_AVAILABLE
print('LIBZIM_AVAILABLE:', _LIBZIM_AVAILABLE)
"
# Expected: LIBZIM_AVAILABLE: True
```

If `False`, libzim import is failing despite being installed. Check: `from libzim.writer import Creator` runs successfully from the backend venv? If not, re-run `uv pip install "libzim>=3.10.0,<4.0"` inside the backend directory.

**Run the smoke test**:

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

.venv/bin/python - <<'SMOKE_TEST'
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ExportScope
)

output_path = Path("/tmp/open-repo-smoke.zim")

# Title <=30 chars — safe for zimcheck 3.1.3
metadata = ZimMetadata(
    title="Open-Repo Smoke Test",
    description="Phase 5 smoke test export",
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
    print("ERROR: File < 1KB — stub fallback is running, libzim not active")
    sys.exit(1)
if not result.zimcheck_passed:
    print("ERROR: zimcheck failed")
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

**Troubleshooting**:

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| File size < 1 KB | `_LIBZIM_AVAILABLE = False` — stub running | Check `from libzim.writer import Creator` works in venv |
| `zimcheck failed: Title too long` | zim-tools 3.1.3 treats titles >30 chars as error | Title in smoke test is already <=30 chars; check `metadata.title` |
| `AttributeError: 'NoneType' object` | `Creator = None` — libzim import guard triggered | Reinstall libzim: `uv pip install "libzim>=3.10.0,<4.0"` |
| Generation time > 60 seconds | Cold-start JIT or thermal throttling | Check temperature; repeat test; first run is often slower |
| `zimcheck not found` | zimcheck not installed | Complete Step B.2 first |

**Thermal note**: Monitor CPU temperature during the smoke test. If it reaches 87°C, the export will continue but may slow due to throttling. For a 2-article smoke test this is unlikely to be an issue; for 500+ articles, schedule during off-peak hours.

**Estimated duration**: 15-45 minutes  
**Risk**: Medium (first real Creator invocation — unknown behavior possible)  
**Success criteria**: File size > 10 KB, `zimcheck passed: True`, `SMOKE TEST PASSED`

---

### B.4 — Apply Migration 003 (20 minutes)

**Why**: The `zim_exports` table must exist in PostgreSQL before any export service code that persists results is deployed. Migration 003 creates the table and its indexes.

**Prerequisite**: PostgreSQL must be running and `DATABASE_URL` must be set.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Confirm current migration state
.venv/bin/python -m alembic current

# Preview SQL (dry run, no changes applied)
.venv/bin/python -m alembic upgrade head --sql

# Apply migration
.venv/bin/python -m alembic upgrade head

# Verify
.venv/bin/python -m alembic current
# Expected: 003 (head)
```

**If migration fails with "relation 002 does not exist"**: The database does not have migrations 001 or 002 applied. Run `alembic stamp 002` to mark the current state as migration 002, then re-run `alembic upgrade head`.

**If PostgreSQL is unavailable**: Skip this step. The ZimWriter code writes to a file path and does not require the database. Note this for deployment: migration 003 must be applied before the export service API endpoint is activated.

**Estimated duration**: 10-20 minutes (including PostgreSQL setup if needed)  
**Risk**: Medium (depends on database availability)  
**Blocker if skipped**: Export service cannot persist job records; API endpoint will fail at runtime

---

### B.5 — Fix Attribution Footer XSS (20 minutes) — Required before FEDERATED scope

**Why**: `source_node_url` and `source_node_name` from federation partners are interpolated into HTML without escaping. A compromised partner could inject `<script>` elements or `javascript:` URL handlers. Not exploitable in `LOCAL_ONLY` scope (Phase 5.1 default), but must be fixed before FEDERATED exports are activated.

**File**: `projects/open-repo/backend/app/services/export/zim_writer.py`

Step 1: Add `import html as _html_lib` at the top of the file (with standard library imports).

Step 2: In `_apply_attribution_footer()`, locate the footer construction block (approximately lines 836-847 on master after merge) and replace the f-string interpolation with:

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
# Expected: 88 passed
```

**Commit**:
```bash
git add projects/open-repo/backend/app/services/export/zim_writer.py
git commit -m "fix(open-repo): escape attribution HTML to prevent XSS in ZIM exports"
```

**Estimated duration**: 20 minutes  
**Risk**: Low — synthetic test data uses safe values, so existing attribution tests pass unchanged  
**Required for**: FEDERATED scope exports (not required for Phase 5.1 LOCAL_ONLY MVP)

---

### B.6 — Write Post-Activation Integration Tests (2 hours)

These 12 tests verify the ZIM binary format, not just interface contracts. They require real libzim and are required before Phase 5.1 is declared production-ready.

**File to create**: `projects/open-repo/backend/tests/unit/test_zim_writer_libzim.py`

Priority P0 tests (implement first):

| Test ID | What it verifies | Key assertion |
|---------|-----------------|--------------|
| `test_zim_writer_creates_real_zim_file` | Output is a real ZIM binary | First 4 bytes == `b'ZIM\x04'` |
| `test_zimcheck_passes_on_valid_export` | zimcheck exits 0 | `result.zimcheck_passed is True` |
| `test_offline_read_article_by_path` | ZIM is readable via libzim.reader | `Archive(path).get_article("water/biosand-filter").title == "Biosand Water Filter"` |
| `test_xapian_index_populated` | Full-text search works | `len(list(archive.search("biosand"))) > 0` |
| `test_zim_metadata_all_mandatory_fields` | All 11 metadata fields written | `archive.get_metadata("Title")` etc. non-empty |
| `test_article_count_matches_database` | article_count in result matches articles added | `result.article_count == n_articles_added` |

After writing the tests:

```bash
python3 -m pytest tests/unit/test_zim_writer_libzim.py tests/integration/test_export_pipeline.py -v --tb=short
# Expected: 12 new + 88 existing = 100 passed
```

**Estimated duration**: 2 hours  
**Risk**: Low — tests verify behavior of working code  
**Required for**: Phase 5.1 production-ready declaration

---

### B.7 — Kiwix Device Validation (1 hour — can defer to separate session)

Manual verification that the ZIM file opens and is navigable in Kiwix.

**Method A — kiwix-serve via Docker** (no physical device needed):

```bash
# SECURITY: bind to 127.0.0.1 only — never 0.0.0.0
docker run --rm -p 127.0.0.1:8080:80 \
  -v /tmp:/data \
  kiwix/kiwix-serve \
  /data/open-repo-smoke.zim
```

Open `http://127.0.0.1:8080` in a browser. Acceptance criteria:

- Index page loads without error
- Articles are navigable by path
- Full-text search returns results for keywords present in the content
- No external HTTP requests in browser DevTools network panel (true offline export)

**Method B — Kiwix Android** (if device available):

```bash
adb push /tmp/open-repo-smoke.zim /sdcard/kiwix/
```

Open Kiwix app, navigate to the transferred file.

**Estimated duration**: 30-60 minutes  
**Required for**: Phase 5.1 production-ready declaration (can be done in a separate session)

---

### B.8 — Remove Pre-Go-Live Code Artifacts (15 minutes)

Two cleanup items documented in v4.0 that should be removed before any production announcement:

**Item 1**: The broad `try/except AttributeError: pass` wrapping `_apply_metadata_to_creator()`. This suppresses real Creator errors. Remove after B.3 smoke test confirms correctness with real libzim.

**Item 2**: The `_stub_write_placeholder` reference in the `_run_zimcheck()` docstring (approximately line 1015) — a leftover reference after the method was removed. Delete that `TODO` line.

```bash
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no
# Expected: 88 passed (cleanup does not affect test behavior)
```

**Estimated duration**: 15 minutes  
**Risk**: None

---

### B.9 — Update README (1 hour)

`projects/open-repo/backend/README.md` needs a Phase 5 offline export section. Minimum additions:

- "Phase 5: Offline Export (ZIM)" section describing the ZimWriter pipeline
- Installation notes: `libzim` (already in pyproject.toml) and `zim-tools` (system package)
- ZIM file usage guide: how to load in Kiwix (link to kiwix.org)
- Updated project structure tree showing `app/services/export/`

**Estimated duration**: 1 hour  
**Required for**: Before public surfacing of the offline export feature

---

## Validation Checklist — Definition of Done

All items must pass before Phase 5.1 is declared production-ready:

| # | Item | Verification command | Required for |
|---|------|---------------------|-------------|
| V1 | libzim >=3.10.0 in pyproject.toml | `grep libzim pyproject.toml` shows `>=3.10.0` | Merge |
| V2 | libzim C++ 9.7.0 installed | `.venv/bin/python -c "from libzim.version import get_libzim_version; print(get_libzim_version())"` | Pre-activation |
| V3 | ORM types correct (Float/Boolean) | `from app.models import ZimExport; print(ZimExport.generation_duration_seconds.type)` shows FLOAT | Pre-first-export |
| V4 | 240/240 backend tests passing | `pytest tests/ -q --tb=no` shows `240 passed` | Throughout |
| V5 | 88/88 export tests passing | `pytest tests/integration/test_export_pipeline.py -q --tb=no` shows `88 passed` | Throughout |
| V6 | Smoke test ZIM > 10 KB | `ls -la /tmp/open-repo-smoke.zim` | Activation |
| V7 | zimcheck passes on smoke ZIM | `zimcheck /tmp/open-repo-smoke.zim` exits 0 | Activation |
| V8 | SHA-256 sidecar verifiable | `sha256sum -c /tmp/open-repo-smoke.zim.sha256` | Activation |
| V9 | Migration 003 applied | `alembic current` shows `003 (head)` | Deployment |
| V10 | ZimExport ORM importable | `from app.models import ZimExport` succeeds | Pre-first-export |
| V11 | Attribution XSS fixed | `grep "_html_lib.escape" app/services/export/zim_writer.py` finds result | Pre-FEDERATED |
| V12 | No 0.0.0.0 bindings | `grep -r "0.0.0.0" projects/open-repo/backend/app/` returns nothing | Throughout |
| V13 | 100/100 tests (88 + 12 new) | `pytest tests/ -q --tb=no` shows `100 passed` | Production-ready |
| V14 | ZIM opens in Kiwix | Manual browser test via kiwix-serve | Production-ready |
| V15 | Broad try/except removed from _apply_metadata | Manual code review | Pre-production |

---

## Risk Flags

**Thermal — HIGH for repeated or large exports**

The Pi 5 reaches 87.8°C under sustained compute. ZIM creation sustains high CPU utilization for the full export duration. For the MVP corpus (500–1,000 articles, 15–45 seconds), this is within the safe envelope for occasional exports. For weekly automated exports:

- A heatsink upgrade is strongly recommended before scheduling automated exports
- Schedule exports at 02:00 UTC when ambient temperature is lowest
- Do not run exports concurrently with other CPU-intensive workloads (Meilisearch indexing, ActivityPub federation)
- Monitor: `vcgencmd measure_temp` during the first real export run

**ORM Type Mismatch — MEDIUM (new finding)**

The `generation_duration_seconds` column is `Integer` in the ORM but `Float` in the migration. Fix in Step B.1 before any export job writes timing data. If not fixed, all timing records will be truncated to whole seconds, impacting any monitoring that tracks export duration for performance alerting.

**zimcheck Title Length — MEDIUM**

Debian Bookworm's zim-tools 3.1.3 treats titles >30 characters as a hard error. The roadmap example title "Open-Repo: Full Library (English)" is 34 characters. Production `ZimMetadata` configurations must use titles <=30 characters until zim-tools is upgraded to 3.3.0+. The smoke test title ("Open-Repo Smoke Test" = 20 chars) is safe.

**Migration Ordering — MEDIUM**

Apply migration 003 before activating any API endpoint that queries the `zim_exports` table. Running the export API with migration 003 code but without the table applied causes a `ProgrammingError` at runtime on the first export request. Safe path: apply migration in the same deployment step that enables the export endpoint.

**Memory Buffering — LOW for MVP**

`ZimWriter` buffers all `ZimEntry` objects before `create_zim()`. Safe for <5,000 articles. Streaming mode is required before Phase 5.2 corpora are generated.

**Concurrent Export Jobs — LOW for MVP**

APScheduler can overlap with a manual export trigger, producing duplicate ZIM files for the same name+flavour+period combination. Add a database lock check (query `zim_exports` for `status='generating'` with matching name+flavour before starting any export) when the export API endpoint is implemented.

---

## Hour-by-Hour Timeline Summary

| Time | Stage | Task | Risk | Thermal load |
|------|-------|------|------|-------------|
| H0–H0.5 | A | Merge with doc conflict resolution | Low | None |
| H0.5–H0.75 | B.1 | Fix ORM type mismatch | Low | None |
| H0.75–H1 | B.2 | Install zimcheck via apt | Low | None |
| H1–H1.75 | B.3 | Smoke test with real libzim | Medium | High (brief) |
| H1.75–H2 | B.4 | Apply migration 003 (needs PostgreSQL) | Medium | None |
| **H2 = minimum viable activation** | | LOCAL_ONLY exports functional | | |
| H2–H2.5 | B.5 | Fix attribution XSS | Low | None |
| H2.5–H4.5 | B.6 | Write 12 post-activation tests | Low | None |
| H4.5–H5.5 | B.7 | Kiwix validation (can defer) | Low | None |
| H5.5–H5.75 | B.8 | Remove code artifacts | None | None |
| H5.75–H6.75 | B.9 | README update | None | None |
| **H6.75 = production-ready** | | | | |

**Minimum viable activation** (just enough for LOCAL_ONLY scope to produce real ZIM files):
Stage A + B.1 + B.2 + B.3 = approximately 2 hours. Migration 003 (B.4) is required before export job records can be persisted to the database.

---

## Post-Activation Monitoring

Once Phase 5.1 is live, watch these metrics:

| Metric | Alert threshold | Source |
|--------|----------------|--------|
| Export generation time | >300 seconds for nopic flavour | `zim_exports.generation_duration_seconds` |
| zimcheck pass rate | Any failure on automated export | `zim_exports.zimcheck_passed = FALSE` |
| ZIM file size | <1 KB (stub running) or >500 MB (runaway) | `zim_exports.file_size_bytes` |
| Pi temperature during export | >87°C sustained | `vcgencmd measure_temp` |
| CDN upload errors | Any exception on upload | Application logs |

A `GET /api/exports/health` endpoint returning last successful export metadata and zimcheck pass rate for the past 7 days is recommended for observable readiness.

---

## Change Log

| Date | Session | Change |
|------|---------|--------|
| 2026-05-21 | 1447 | Initial checklist (Part A/B structure) |
| 2026-05-21 | 1483 | v4.0 — expanded with B.6–B.10 stages, full timeline |
| 2026-05-22 | 1492 | v5.0 — new finding (ORM type mismatch), live verification of libzim 3.10.0 install, updated test counts (240/240 full suite vs 88/88 export suite clarification), thermal notes updated, zimcheck 3.1.3 apt availability confirmed |
