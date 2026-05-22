---
title: "Phase 5.1 Activation Checklist — Step-by-Step Post-Merge Execution Roadmap"
project: open-repo
phase: "5.1"
created: 2026-05-22
status: READY-TO-EXECUTE — pending user decision (medical reviewer ID May 31)
scope: "Real libzim activation: merge reconciliation, smoke test, migration, production validation"
audience: thorn — execute after Phase 5 activation decision
decision_gate: "Medical reviewer ID confirmation May 31 → activation May 31 or June 1"
total_estimate: "2–4 hours for minimum viable activation; 6–7 hours for production-ready"
---

# Phase 5.1 Activation Checklist

**Scope**: Convert local master from stub ZIM generation to real libzim Creator output.

**Current state**: `open-repo/main` remote has real libzim activation merged (PR #3). Local `master` still has stub. This checklist reconciles the two and produces a working, validated Phase 5.1 installation.

**Minimum viable activation**: Steps 0 through B3 — approximately 2 hours. After these steps, `create_zim()` produces real ZIM files readable by Kiwix.

**Production-ready**: All steps through B8 — approximately 6–7 hours total.

---

## Blocker Identification

Before starting, confirm these blockers are resolved:

| Blocker | Status | Action |
|---------|--------|--------|
| Medical reviewer ID confirmation | PENDING (May 31) | User decision required |
| Pi 5 temperature <82°C before starting | CHECK — currently 80.7°C idle | Monitor; add cooling if ambient is high |
| Disk space ≥2 GB free in /tmp | CHECK via `df -h /tmp` | Free space if needed |

Do not begin activation if the medical reviewer decision has not been made. The activation is reversible but creates database state that complicates rollback.

---

## Pre-Flight Checklist (15 minutes)

Run all checks before touching any code. Stop and investigate if any check fails.

```bash
# PF1: Architecture
uname -m
# Expected: aarch64

# PF2: Python version
python3 --version
# Expected: Python 3.11.x

# PF3: Working tree clean
cd /home/awank/dev/SuperClaude_Framework
git status
# Expected: On branch master, nothing to commit

# PF4: Baseline test suite
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
python3 -m pytest tests/ -q --tb=no
# Expected: 240 passed, 19 skipped

# PF5: Export pipeline tests
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no
# Expected: 88 passed

# PF6: libzim importable
.venv/bin/python -c "from libzim.writer import Creator; print('OK')"
# Expected: OK

# PF7: libzim C++ version
.venv/bin/python -c "from libzim.version import get_libzim_version; print(get_libzim_version())"
# Expected: 9.7.0

# PF8: Temperature check
vcgencmd measure_temp
# Expected: ideally <82°C. If >84°C, wait for cooling before continuing.

# PF9: Disk space
df -h /tmp
# Expected: >=2 GB free
```

**If PF4 fails**: do not proceed. The baseline must be green before any changes.
**If PF8 shows >84°C**: wait or improve cooling before the smoke test (Step B3).

---

## Stage 0: Reconcile Local Master with Remote Main (30 minutes)

This stage brings the real libzim activation code from `open-repo/main` into the local working tree. It is the most critical step.

### Why This Is Needed

Local `master` and `open-repo/main` diverged after PR #3 was merged on May 19. The key differences (verified):

| Component | Local master | open-repo/main |
|-----------|-------------|----------------|
| `create_zim()` | Calls `_stub_write_placeholder()` | Real Creator integration |
| `_LIBZIM_AVAILABLE` flag | Absent | Present (try/except guard) |
| `ArticleItem` class | Absent (was removed in post-fix commit) | Present |
| Migration 003 | ABSENT from working tree | Present |
| `libzim` pin | `>=3.10.0,<4.0` | `>=3.2,<4.0` |
| Test count | 88 (4 extra from commit 198a146d) | 84 |

### Option A: Cherry-Pick the Real Implementation (Recommended)

Cherry-pick just the `zim_writer.py` changes from the remote feature branch. This preserves the 4 extra integration tests on local master (from commit 198a146d) while gaining the real Creator path.

```bash
# Step 0.1: Fetch remote
cd /home/awank/dev/SuperClaude_Framework
git fetch open-repo

# Step 0.2: Identify the feature branch tip
git log --oneline open-repo/feature/zimwriter-libzim-activation | head -5
# Note the commit hash for feat(open-repo): Phase 5 Candidate 1 libzim integration
# It should be commit 3c9362e9 or 274eb1f2

# Step 0.3: Check what zim_writer.py looks like on the feature branch
git show open-repo/feature/zimwriter-libzim-activation:projects/open-repo/backend/app/services/export/zim_writer.py | grep -n "_LIBZIM_AVAILABLE\|class ArticleItem\|def create_zim\|with Creator" | head -15
# Expected: shows _LIBZIM_AVAILABLE flag, ArticleItem class, real Creator block
```

**Manual merge approach** (safer for targeted changes):

Instead of a full cherry-pick (which may bring in unwanted documentation changes), extract and apply just the `zim_writer.py` changes:

```bash
# Step 0.4: Get the feature branch version of zim_writer.py
git show open-repo/feature/zimwriter-libzim-activation:projects/open-repo/backend/app/services/export/zim_writer.py > /tmp/zim_writer_feature.py

# Step 0.5: Review the key differences
diff projects/open-repo/backend/app/services/export/zim_writer.py /tmp/zim_writer_feature.py | head -80
# Review carefully: should see _LIBZIM_AVAILABLE, ArticleItem class, and real create_zim() path

# Step 0.6: Copy the feature branch version (WARNING: this replaces the current file)
# Only do this after verifying the diff looks correct
cp /tmp/zim_writer_feature.py projects/open-repo/backend/app/services/export/zim_writer.py

# Step 0.7: Run tests immediately
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=short 2>&1 | tail -5
# Expected: 84 passed (4 fewer because TestLibZIMIntegration tests adapted to feature branch version)
# OR if tests need updating: investigate failures before proceeding
```

**If test count drops below 80**: the feature branch version may be incompatible with the 4 tests added by commit 198a146d. Roll back (`git checkout -- projects/open-repo/backend/app/services/export/zim_writer.py`) and use Option B instead.

### Option B: Get migration 003 Only (Parallel step, always required)

Migration 003 is not in the local master working tree. Regardless of which approach is used for `zim_writer.py`, migration 003 must be restored:

```bash
# Get migration 003 from feature branch
git show open-repo/feature/zimwriter-libzim-activation:projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py > /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py

# Verify file exists
ls projects/open-repo/backend/alembic/versions/
# Expected: 001_..., 002_..., 003_add_zim_exports_table.py

# Verify migration content
head -20 projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py
# Expected: revision = "003", down_revision = "002"
```

### Step 0 Commit

```bash
git add projects/open-repo/backend/app/services/export/zim_writer.py
git add projects/open-repo/backend/alembic/versions/003_add_zim_exports_table.py
git commit -m "feat(open-repo): activate real libzim Creator + restore migration 003

- zim_writer.py: replaced stub with real libzim Creator integration
- Added _LIBZIM_AVAILABLE try/except guard
- Added ArticleItem adapter class (ZimEntry -> libzim Item bridge)
- create_zim() now calls Creator context manager when libzim available
- alembic/versions/003_add_zim_exports_table.py: restored (was absent from local master)"
```

**Time estimate**: 20–30 minutes
**Risk**: Low-Medium. File replacement is reversible via git. Test count may change by 0–4 tests.
**Blocker if skipped**: `create_zim()` writes stub text files; no real ZIM output possible.

---

## Stage A: Install zimcheck (15 minutes)

### Why Required

`create_zim(run_zimcheck=True)` calls `_run_zimcheck()`. Without the `zimcheck` binary, this silently returns `True` (validation skipped). You need zimcheck to know if generated ZIM files are structurally valid.

```bash
# A.1: Install via apt
sudo apt-get install -y zim-tools

# A.2: Verify installation
which zimcheck
# Expected: /usr/bin/zimcheck

zimcheck --version
# Expected: zimcheck X.Y.Z
# Note version here: _______________

# A.3: Critical title length check
# Debian Bookworm ships zim-tools 3.1.3
# zimcheck 3.1.3 treats titles >30 characters as a HARD ERROR (not a warning)
# The smoke test title "Open-Repo Smoke Test" is 20 chars -- safe
# Production exports must use titles <=30 chars until zim-tools is upgraded to >=3.3.0
```

**If apt fails** (package not available in Bookworm repos):
```bash
# Download static binary from GitHub releases
wget https://github.com/openzim/zim-tools/releases/latest/download/zimcheck-linux-aarch64 -O /usr/local/bin/zimcheck
chmod +x /usr/local/bin/zimcheck
zimcheck --version
```

**Time estimate**: 5–15 minutes (network dependent)
**Risk**: Low
**Blocker if skipped**: Cannot verify ZIM file validity; exports may silently produce invalid files

---

## Stage B: Smoke Test with Real libzim (45–90 minutes including debugging budget)

This is the first real Creator invocation on this hardware. Budget time for first-run surprises.

### B.1: Verify libzim is Active

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

.venv/bin/python -c "
from app.services.export.zim_writer import _LIBZIM_AVAILABLE
print('_LIBZIM_AVAILABLE:', _LIBZIM_AVAILABLE)
"
# Expected: _LIBZIM_AVAILABLE: True
# If False: libzim import guard is failing; check 'from libzim.writer import Creator' works independently
```

If `_LIBZIM_AVAILABLE` is `False`:
```bash
.venv/bin/python -c "from libzim.writer import Creator, Item, StringProvider, Hint; print('libzim direct import OK')"
# If this fails: libzim wheel not in venv path; run:
# cd projects/open-repo/backend && uv pip install "libzim>=3.10.0,<4.0"
```

### B.2: Temperature Check Before Smoke Test

```bash
vcgencmd measure_temp
# If >84°C: wait 10 minutes or improve cooling before proceeding
# The smoke test is short (2 articles, <5 seconds) but the first Creator init
# can spike CPU briefly due to Xapian initialization
```

### B.3: Run the Smoke Test

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

# Title <=20 chars to be safe with zimcheck 3.1.3
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
    content="<html><head><title>Open-Repo</title></head><body><h1>Open-Repo Offline Library</h1><p>Phase 5 smoke test.</p></body></html>",
    article_type="procedure",
)
writer.add_article(
    path="procedures/biosand-filter",
    content="<html><head><title>Biosand Water Filter</title></head><body><h1>Biosand Water Filter</h1><p>Build instructions for a biosand water filter.</p></body></html>",
    article_type="procedure",
)

result = writer.create_zim(run_zimcheck=True)
print(f"Articles: {result.article_count}")
print(f"File size: {result.file_size_bytes:,} bytes")
print(f"SHA-256: {result.sha256[:16]}...")
print(f"zimcheck passed: {result.zimcheck_passed}")
print(f"Generation time: {result.generation_duration_seconds:.3f}s")

if result.file_size_bytes < 1024:
    print("FAIL: File < 1 KB — stub fallback is running, libzim not active")
    sys.exit(1)
if not result.zimcheck_passed:
    print("FAIL: zimcheck failed — ZIM file is invalid")
    sys.exit(1)

header = output_path.read_bytes()[:4]
if header == b'STUB':
    print("FAIL: Stub placeholder written — libzim Creator not activated")
    sys.exit(1)

print("SMOKE TEST PASSED")
print(f"ZIM header bytes: {header.hex()} (expect: 5a494d04)")
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
ZIM header bytes: 5a494d04
```

### B.3 Troubleshooting

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| File size < 1 KB | Stub running — `_LIBZIM_AVAILABLE = False` | Re-check Step B.1; reinstall libzim |
| `zimcheck failed: Title too long` | zimcheck 3.1.3 hard error for title >30 chars | Title "Open-Repo Smoke Test" is 20 chars — should not trigger; check actual ZIM metadata |
| `AttributeError on Creator` | libzim API changed in 3.10.0 | Check `Compression` import: `from libzim.writer import Creator, Item, StringProvider, Hint, Compression` |
| Generation time >60s | Thermal throttling or cold-start JIT | Record temperature, wait for cool, re-run |
| `zimcheck: command not found` | zimcheck not installed | Complete Stage A first |
| `config_indexing` AttributeError | API difference between versions | Check that `creator.config_indexing()` is called BEFORE `with creator:` |

### B.3 Thermal Note

Monitor temperature during the smoke test:
```bash
# In a second terminal while smoke test runs:
watch -n 1 vcgencmd measure_temp
```

If temperature exceeds 87°C during the 5-second smoke test, something else is consuming CPU. Check for concurrent processes (`htop`). The smoke test itself should not cause sustained throttling.

**Time estimate**: 15–45 minutes
**Risk**: Medium (first real Creator invocation — unknown behavior possible)
**Pass criteria**: File size >10 KB, zimcheck passed, ZIM header `5a494d04`

---

## Stage C: Apply Migration 003 (20 minutes)

**Prerequisite**: PostgreSQL must be running and `DATABASE_URL` must be set.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# C.1: Check current migration state
.venv/bin/python -m alembic current
# Expected: 002 (head) or (empty if no migrations applied)

# C.2: Preview SQL (dry run)
.venv/bin/python -m alembic upgrade head --sql 2>&1 | head -30
# Expected: CREATE TABLE zim_exports with 28 columns

# C.3: Apply migration
.venv/bin/python -m alembic upgrade head

# C.4: Verify
.venv/bin/python -m alembic current
# Expected: 003 (head)

# C.5: Schema spot-check
.venv/bin/python -c "
from app.database import engine
from sqlalchemy import inspect
inspector = inspect(engine)
cols = [c['name'] for c in inspector.get_columns('zim_exports')]
print('Columns:', len(cols))
assert 'zim_uuid' in cols
assert 'sha256' in cols
assert 'is_current' in cols
assert 'generation_duration_seconds' in cols
print('Schema OK')
"
# Expected: Columns: 28  Schema OK
```

**If migration fails with "relation alembic_version does not exist"**:
```bash
# Database has never had alembic run on it
.venv/bin/python -m alembic stamp head
# Then re-run: .venv/bin/python -m alembic upgrade head
```

**If PostgreSQL is unavailable**: Skip Stage C. ZimWriter writes to a file path and does not require the database. Note: migration 003 MUST be applied before activating any API endpoint that queries `zim_exports`.

**Time estimate**: 10–20 minutes
**Risk**: Medium (database dependency)
**Blocker if skipped**: Export service cannot persist job records

---

## Stage D: Post-Activation Test Suite (30 minutes)

After completing Stages 0, A, B, C, run the full test suite:

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# D.1: Full suite (must match or exceed baseline)
python3 -m pytest tests/ -q --tb=no
# Expected: >=240 passed, 19 skipped, 0 failed
# If test count changes: investigate; some tests may need updating for real Creator path

# D.2: Export pipeline specifically
python3 -m pytest tests/integration/test_export_pipeline.py -q --tb=no
# Expected: >=84 passed, 0 failed

# D.3: Record test count
python3 -m pytest tests/ --tb=no 2>&1 | tail -3
# Save this output — it is the post-activation baseline
```

**If tests fail after Stage 0**: The feature branch `zim_writer.py` may be incompatible with the 4 tests added by commit 198a146d (the post-fix tests). The likely failures would be in `TestLibZIMIntegration`. Update the tests to match the feature branch API, or update the feature branch code to include the fix commit's PNG and config_indexing improvements.

---

## Stage E: Corpus Export Test (45 minutes)

This validates that the full 32-article corpus produces a valid ZIM file.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

.venv/bin/python - <<'CORPUS_TEST'
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

from app.services.export.zim_writer import (
    ZimWriter, ZimMetadata, ExportConfig, ExportScope
)

records = []
with open('../data/openfarm_procedures.jsonl') as f:
    for line in f:
        records.append(json.loads(line))

print(f"Loading {len(records)} articles...")

metadata = ZimMetadata(
    title="Open-Repo Corpus Test",
    description="32-article corpus validation",
    language="eng",
    name="open-repo_en_nopic",
    flavour="nopic",
    creator="Open-Repo",
    publisher="Open-Repo",
    source_url="https://example.open-repo.org",
)
config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic", language_iso3="eng")

output = Path("/tmp/open-repo-corpus.zim")
writer = ZimWriter(metadata=metadata, config=config, output_path=output, zimcheck_binary="zimcheck")

for r in records:
    cid = r['cid']
    title = r.get('title', {}).get('en', '')
    outcome = r.get('outcome', {}).get('en', '')
    steps_html = ''
    for s in r.get('steps', []):
        steps_html += f"<h3>Step {s['stepNumber']}: {s.get('title',{}).get('en','')}</h3><p>{s.get('body',{}).get('en','')}</p>"
    content = f"<html><head><title>{title}</title></head><body><h1>{title}</h1><p>{outcome}</p>{steps_html}</body></html>"
    writer.add_article(path=cid, content=content, article_type='procedure')

t0 = time.time()
result = writer.create_zim(run_zimcheck=True)
elapsed = time.time() - t0

print(f"Articles: {result.article_count}/32")
print(f"File size: {result.file_size_bytes:,} bytes ({result.file_size_bytes/1024:.0f} KB)")
print(f"Generation time: {elapsed:.2f}s")
print(f"zimcheck passed: {result.zimcheck_passed}")
print(f"SHA-256: {result.sha256[:32]}...")

assert result.article_count == 32, f"Expected 32 articles, got {result.article_count}"
assert result.file_size_bytes > 10000, "File too small — stub still running"
assert result.zimcheck_passed, "zimcheck failed"

print("CORPUS TEST PASSED")
print(f"ZIM written to: /tmp/open-repo-corpus.zim")
CORPUS_TEST
```

Record the output for the post-activation baseline:
- Article count: ___/32
- File size: ___ KB
- Generation time: ___ seconds
- zimcheck passed: ___

**Time estimate**: 30–45 minutes (including 15-minute debugging budget)
**Risk**: Medium (first multi-article real export)
**Pass criteria**: 32/32 articles, file >10 KB, zimcheck passed

---

## Stage F: Kiwix Validation (45–60 minutes, deferrable)

This confirms the ZIM file is navigable in a real Kiwix interface. Can be deferred to a separate session.

```bash
# SECURITY: bind to 127.0.0.1 only — never 0.0.0.0
docker run --rm \
  -p 127.0.0.1:8080:80 \
  -v /tmp:/data \
  kiwix/kiwix-serve \
  /data/open-repo-corpus.zim
```

Open `http://127.0.0.1:8080` in a browser. Acceptance criteria:
- Index page loads ("Open-Repo Corpus Test" title visible)
- At least one article navigable by clicking
- Full-text search returns results for "potato" or "garlic"
- No external HTTP requests in browser DevTools network panel

**Time estimate**: 30–60 minutes
**Risk**: Low
**Required for**: Production-ready declaration (can defer to separate session)

---

## Stage G: ORM Type Mismatch Fix (15 minutes)

**Status**: May already be fixed. Verify before assuming.

```bash
.venv/bin/python -c "
from app.models import ZimExport
from sqlalchemy import Float, Boolean
cols = {c.name: type(c.type).__name__ for c in ZimExport.__table__.columns}
print('generation_duration_seconds:', cols.get('generation_duration_seconds'))
print('is_current:', cols.get('is_current'))
print('zimcheck_passed:', cols.get('zimcheck_passed'))
"
# Desired output: FLOAT, BOOLEAN, BOOLEAN
# Current state (commit 274eb1f2): Integer for all three — needs fix
```

If output shows `INTEGER` for boolean/float fields, apply fix:

In `projects/open-repo/backend/app/models.py`, update the `ZimExport` class:
- Add `Float, Boolean` to the `from sqlalchemy import` line
- Change `is_current = Column(Integer, ...)` to `Column(Boolean, ...)`
- Change `is_reference = Column(Integer, ...)` to `Column(Boolean, ...)`
- Change `include_images = Column(Integer, ...)` to `Column(Boolean, ...)`
- Change `zimcheck_passed = Column(Integer, ...)` to `Column(Boolean, ...)`
- Change `generation_duration_seconds = Column(Integer, ...)` to `Column(Float, ...)`

Verify after change:
```bash
python3 -m pytest tests/ -q --tb=no
# Expected: same pass count as before, 0 failures
```

**Time estimate**: 15 minutes
**Risk**: Low (nullable columns, no existing data)
**Blocker if skipped**: Export timing data truncated; Boolean ORM queries return integers

---

## Hour-by-Hour Timeline

| Hour | Stage | Activity | Risk | Thermal load |
|------|-------|----------|------|-------------|
| H0–H0.25 | Pre-flight | 9 checks, verify baseline | None | None |
| H0.25–H1 | Stage 0 | Reconcile local master with remote main | Low-Med | None |
| H1–H1.25 | Stage A | Install zimcheck | Low | None |
| H1.25–H2 | Stage B | Smoke test (2 articles, real Creator) | Medium | Brief spike (5–10s) |
| **H2 = minimum viable** | — | Real ZIM exports working | — | — |
| H2–H2.5 | Stage C | Apply migration 003 | Medium | None |
| H2.5–H3 | Stage D | Post-activation test suite | Low | None |
| H3–H4 | Stage E | 32-article corpus export | Medium | Moderate (10–40s) |
| H4–H5 | Stage F | Kiwix validation (deferrable) | Low | None |
| H5–H5.25 | Stage G | ORM type mismatch fix | Low | None |
| **H5.25 = production-ready** | — | All validation complete | — | — |

---

## Blocker Identification Table

Blockers that will stop the checklist if encountered:

| Blocker | Step where it surfaces | Resolution |
|---------|----------------------|------------|
| `_LIBZIM_AVAILABLE = False` after Stage 0 | B.1 | Reinstall libzim: `uv pip install "libzim>=3.10.0,<4.0"` |
| File size <1 KB after smoke test | B.3 | Stage 0 was not correctly applied; re-examine `create_zim()` in zim_writer.py |
| zimcheck fails on valid ZIM | B.3 | Check title length (<= 30 chars required); check zimcheck version |
| Tests fail after Stage 0 | D | Feature branch `zim_writer.py` incompatible with 198a146d tests; update tests or code |
| PostgreSQL unavailable | C | Skip Stage C; note for deployment. Activation still possible without DB. |
| Temperature >87°C during corpus test | E | Abort export; add cooling before retrying; do not run concurrent workloads |
| Migration 003 chain broken | C | Run `alembic stamp 002` first, then `alembic upgrade head` |

---

## Validation Checklist — Definition of Done

All items marked before declaring Phase 5.1 production-ready:

| # | Item | Verification command | Gate |
|---|------|---------------------|------|
| V1 | `_LIBZIM_AVAILABLE = True` | `from app.services.export.zim_writer import _LIBZIM_AVAILABLE; print(_LIBZIM_AVAILABLE)` | Activation |
| V2 | libzim C++ 9.7.0 | `from libzim.version import get_libzim_version; print(get_libzim_version())` | Pre-activation |
| V3 | Smoke test ZIM >10 KB | `ls -la /tmp/open-repo-smoke.zim` shows size >10000 | Activation |
| V4 | zimcheck passes on smoke | `/tmp/open-repo-smoke.zim` checked, exits 0 | Activation |
| V5 | ZIM magic bytes correct | First 4 bytes = `5a494d04` (ZIM\x04) | Activation |
| V6 | 240/240 backend tests | `pytest tests/ -q --tb=no` | Throughout |
| V7 | Export tests pass | `pytest tests/integration/test_export_pipeline.py -q` | Throughout |
| V8 | Migration 003 applied | `alembic current` shows `003 (head)` | Deployment |
| V9 | ZimExport ORM types correct | `Float` for duration, `Boolean` for flags | Pre-first-export |
| V10 | 32-article corpus export | File >10 KB, zimcheck passed, 32 articles | Production-ready |
| V11 | Kiwix renders articles | Browser test via kiwix-serve | Production-ready |
| V12 | No 0.0.0.0 bindings | `grep -r "0.0.0.0" backend/app/` returns nothing | Throughout |
| V13 | Temperature <87°C during corpus | `vcgencmd measure_temp` monitored | Production-ready |

---

## Post-Activation Monitoring

Once Phase 5.1 is live, watch these metrics for the first 7 days:

| Metric | Alert threshold | Source |
|--------|----------------|--------|
| Export generation time | >120s for 32-article nopic | `zim_exports.generation_duration_seconds` |
| zimcheck pass rate | Any failure | `zim_exports.zimcheck_passed = FALSE` |
| ZIM file size | <1 KB (stub running) or >500 MB | `zim_exports.file_size_bytes` |
| Pi temperature during export | >87°C sustained | `vcgencmd measure_temp` |
| `_LIBZIM_AVAILABLE` | False (import regression) | Application startup log |

---

## What Is Not Required for Phase 5.1

These items are Phase 5.2 scope and do not block activation:

- Export API endpoint (`POST /api/v1/export/zim`) — currently no route wired
- CDN upload step — `ZimWriteResult.cdn_url` field defined but upload logic deferred
- Streaming mode (ZimWriter buffers all articles) — safe for <5,000 articles
- Attribution XSS fix — required only before FEDERATED scope exports; MVP uses LOCAL_ONLY
- OPDS catalog integration with export records — Phase 5.2
- 12 post-activation binary-format tests — Phase 5.2 (current tests use stub output)

---

*Checklist last updated: 2026-05-22*
*Based on: live code audit of local master + open-repo/main remote + pre-deployment verification report*
