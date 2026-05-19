---
title: "Phase 5 Candidate 1 — Pre-Deployment Implementation Checklist"
project: open-repo
phase: 5
candidate: 1
date: 2026-05-19
branch: feature/zimwriter-libzim-activation
commit: ec0ff7be
status: IMPLEMENTATION COMPLETE — awaiting user merge approval May 25-26
---

# Phase 5 Candidate 1: Pre-Deployment Checklist

**What this covers**: Step-by-step actions from user merge approval through to production
deployment. The implementation code is complete; this checklist covers the operational
steps only.

**Total estimated time**: 2.5–3.5 hours (one deployment window)
**Deployment target**: May 30-31 (per ORCHESTRATOR_STATE.md)
**No further code changes required.**

---

## Prerequisites (verify before starting)

- [ ] User has approved merge of `feature/zimwriter-libzim-activation` to `main` (May 25-26)
- [ ] Production PostgreSQL is accessible
- [ ] You have SSH access to the deployment machine
- [ ] Current production migration state is `002` (verify: `alembic current`)
- [ ] Staging environment is available for smoke testing

---

## Phase A: Merge (May 25-26, 15 min)

### A1 — Review CHECKIN.md entry, then merge
**Duration**: 5 min

Check that the PR description in CHECKIN.md under "Needs Your Input" matches the expected scope.
Approve and merge `feature/zimwriter-libzim-activation` to `main` on the open-repo GitHub repo.

```bash
# Via gh CLI (run from SuperClaude_Framework root):
# Verify branch exists remotely:
git fetch open-repo
git log open-repo/feature/zimwriter-libzim-activation --oneline -3

# If not pushed yet, push it:
git push open-repo feature/zimwriter-libzim-activation

# Then create and merge PR via GitHub UI or gh CLI
```

**Blocker**: If the branch is not on the remote yet, push it via git subtree before merging.
See note on git subtree push below.

### A2 — Git subtree push to open-repo remote
**Duration**: 5 min

The open-repo project lives inside this monorepo but has its own remote. Push only the
`projects/open-repo/` subtree:

```bash
cd /home/awank/dev/SuperClaude_Framework
git subtree push --prefix=projects/open-repo open-repo feature/zimwriter-libzim-activation
```

If this fails due to history divergence, use:
```bash
git push open-repo $(git subtree split --prefix=projects/open-repo HEAD):feature/zimwriter-libzim-activation
```

### A3 — Confirm merge on GitHub
**Duration**: 5 min

- Open `https://github.com/esca8peArtist/open-repo`
- Confirm PR shows `Merged` status
- Confirm `main` branch includes commit `ec0ff7be` content (check README or pyproject.toml for libzim dependency)

**Completion marker**: `main` branch at open-repo remote shows `libzim>=3.2,<4.0` in `backend/pyproject.toml`

---

## Phase B: Staging Smoke Test (30–45 min)

### B1 — Install dependencies on staging
**Duration**: 5–10 min

```bash
cd /path/to/open-repo/backend
uv sync  # installs libzim>=3.2,<4.0 and all other dependencies
```

Verify libzim is installed:
```bash
uv run python3 -c "from libzim.writer import Creator, Item; print('libzim OK')"
```

Expected output: `libzim OK`

**Blocker**: If wheel is not available for the staging platform, check:
- Platform must be Linux x86_64, Linux aarch64, macOS x86_64/arm64, or Windows x64
- Python must be 3.10–3.14

### B2 — Apply migration 003 to staging database
**Duration**: 5 min

```bash
cd /path/to/open-repo/backend
alembic upgrade head
```

Expected output:
```
INFO  [alembic.runtime.migration] Running upgrade 002 -> 003, Add zim_exports table...
```

Verify table created:
```sql
SELECT table_name FROM information_schema.tables WHERE table_name = 'zim_exports';
-- Should return one row

SELECT indexname FROM pg_indexes WHERE tablename = 'zim_exports';
-- Should return 3 rows: idx_zim_exports_name_flavour, idx_zim_exports_is_current,
--   and the UNIQUE index on zim_uuid
```

**Blocker**: If migration fails, check:
1. `alembic current` shows `002` (not `003`)
2. Database user has CREATE TABLE and CREATE INDEX privileges
3. `down_revision = "002"` matches the existing migration file

### B3 — Run full test suite on staging
**Duration**: 5–10 min

```bash
cd /path/to/open-repo/backend
uv run pytest tests/integration/test_export_pipeline.py -v
```

Expected: `84 passed` — if real libzim is installed, execution time should be 1–5 seconds
(not <0.5s which indicates stub mode).

**Blocker**: If tests run in <0.3s, libzim is not active. Check `_LIBZIM_AVAILABLE`:
```bash
uv run python3 -c "from app.services.export.zim_writer import _LIBZIM_AVAILABLE; print(_LIBZIM_AVAILABLE)"
```
If False, libzim did not install correctly.

### B4 — Manual ZIM generation smoke test
**Duration**: 10–15 min

Run this script to generate a test ZIM file and verify it is valid:

```python
# save as /tmp/smoke_test.py, run with: uv run python3 /tmp/smoke_test.py
import sys, pathlib
sys.path.insert(0, '/path/to/open-repo/backend')

from app.services.export.zim_writer import ZimWriter, ZimMetadata, ExportConfig, ExportScope

out = pathlib.Path('/tmp/smoke-test.zim')
meta = ZimMetadata(
    title="Open-Repo Smoke Test",
    description="Smoke test export",
    language="eng",
    name="open-repo_en_nopic",
    flavour="nopic",
    creator="Open-Repo Community",
    publisher="Open-Repo",
    source_url="https://your-node.example.org",
)
cfg = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
writer = ZimWriter(metadata=meta, config=cfg, output_path=out, zimcheck_binary=None)
writer.add_article(
    path="index",
    content="<html><head><title>Smoke Test</title></head><body><h1>Test</h1></body></html>",
    article_type="procedure",
)
result = writer.create_zim(run_zimcheck=False)
print(f"File size: {result.file_size_bytes} bytes")
print(f"SHA-256: {result.sha256}")
assert result.file_size_bytes > 1000, "File too small — stub mode?"
print("SMOKE TEST PASSED")
```

Expected output:
```
File size: 35000+ bytes
SHA-256: [64-char hex]
SMOKE TEST PASSED
```

**Blocker**: File size <200 bytes means stub mode is active (libzim not installed).

### B5 — Open smoke test ZIM in Kiwix (optional but recommended)
**Duration**: 5 min

```bash
# If zimcheck is installed on staging:
zimcheck /tmp/smoke-test.zim
# Expected: "ZIM file is OK" or warnings (not errors)

# If Kiwix desktop is available:
# Open the .zim file in Kiwix and verify the article is readable
```

---

## Phase C: Production Deployment (May 30-31, 60–90 min)

### C1 — Pre-deployment backup
**Duration**: 10–15 min

```bash
# PostgreSQL backup:
pg_dump -h <host> -U <user> <database> > backup-pre-migration-003-$(date +%Y%m%d).sql

# Verify backup:
ls -la backup-pre-migration-003-*.sql
```

**Do not skip this step.** Migration 003 is additive (new table + indexes only), but the
backup provides a rollback path if any issue arises.

### C2 — Deploy updated application code
**Duration**: 10–20 min (depends on deployment method)

Deploy the `main` branch to production. The key change is `pyproject.toml` now includes
`libzim>=3.2,<4.0`.

```bash
# If using direct deploy:
git pull origin main
uv sync

# Verify libzim installed:
uv run python3 -c "from libzim.writer import Creator; print('libzim ready')"
```

**Blocker**: If `uv sync` fails to install libzim, check platform compatibility.
libzim provides wheels for Linux x86_64, aarch64, macOS x86_64/arm64, Windows x64.
If the production platform is not in this list, build from source (requires C++17 compiler).

### C3 — Apply migration 003 to production database
**Duration**: 5 min

```bash
# Verify current state before running:
alembic current
# Expected: 002

# Apply migration:
alembic upgrade head
# Expected: INFO [alembic.runtime.migration] Running upgrade 002 -> 003...

# Verify:
alembic current
# Expected: 003 (head)
```

**Rollback if needed**:
```bash
alembic downgrade 002
# Drops zim_exports table and its 3 indexes
# Does NOT affect any other tables
```

### C4 — Post-deployment verification
**Duration**: 10–15 min

```bash
# Run test suite on production environment:
uv run pytest tests/integration/test_export_pipeline.py -v
# Expected: 84 passed in 1-5 seconds

# Verify _LIBZIM_AVAILABLE is True:
uv run python3 -c "from app.services.export.zim_writer import _LIBZIM_AVAILABLE; print('libzim active:', _LIBZIM_AVAILABLE)"
# Expected: libzim active: True

# Check application logs for any import warnings:
# grep for "_LIBZIM_AVAILABLE = False" or "libzim not available" in application startup logs
```

### C5 — Generate first production ZIM export
**Duration**: 15–30 min (depends on content volume)

Trigger the first real ZIM export via the export API or management command:

```bash
# If export is triggered via API:
curl -X POST https://your-node.example.org/api/v1/exports/generate \
  -H "Content-Type: application/json" \
  -d '{"scope": "LOCAL_ONLY", "flavour": "nopic"}'

# Verify result in zim_exports table:
psql -c "SELECT name, flavour, article_count, file_size_bytes, status, zimcheck_passed FROM zim_exports ORDER BY started_at DESC LIMIT 1;"
```

Expected columns:
- `status`: `complete`
- `file_size_bytes`: >1000 (not stub)
- `sha256`: 64-char hex string
- `zimcheck_passed`: True or NULL (if zimcheck not installed — acceptable for Phase 5.1)

**Blocker**: If `status = 'error'`, check application logs for the exception. Common causes:
- Output directory does not exist (create it and update config)
- Database connection failure during record insert
- libzim import failure (verify _LIBZIM_AVAILABLE)

---

## Phase D: Post-Deployment Validation (15 min)

### D1 — Verify OPDS catalog includes the new export
```bash
curl https://your-node.example.org/opds/v2/root.xml
# Should return valid XML with at least one <entry> element
```

### D2 — Optional: Test ZIM in Kiwix
Download the generated ZIM file (from `local_path` in zim_exports table) and open in Kiwix
desktop client to confirm articles are readable and the catalog page loads.

### D3 — Record deployment in ORCHESTRATOR_STATE.md
Update open-repo status:
- Phase 5 Candidate 1: DEPLOYED
- Migration 003: APPLIED
- First ZIM export: [size] bytes, [article count] articles
- Deployment date: [date]

---

## Known Blockers and Resolutions

| Blocker | Probability | Resolution |
|---------|------------|-----------|
| libzim wheel not available for production platform | Low | Build from source (C++17 required) |
| zimcheck not installed | Medium (dev) | `apt-get install zim-tools` — optional for Phase 5.1 |
| migration 002 not applied yet | Very low | Run `alembic upgrade 002` first |
| Output directory does not exist | Medium (first deploy) | Create directory, add to deployment config |
| libzim import silently fails | Low | Check logs for _LIBZIM_AVAILABLE warning |

---

## Hour-by-Hour Timeline (Deployment Day)

| Hour | Activity | Duration |
|------|---------|---------|
| +0:00 | Pre-deployment backup (C1) | 15 min |
| +0:15 | Deploy code + uv sync (C2) | 20 min |
| +0:35 | Apply migration 003 (C3) | 5 min |
| +0:40 | Post-deployment verification (C4) | 15 min |
| +0:55 | First production ZIM export (C5) | 15–30 min |
| +1:25 | OPDS catalog verification (D1) | 5 min |
| +1:30 | Optional Kiwix test (D2) | 10 min |
| +1:40 | Update orchestrator state (D3) | 5 min |
| +1:45 | **DONE** | — |

**Total wall clock: 1.75–2.5 hours** (vs. 2–3 hour setup friction estimate from task spec)

---

## What is NOT Required

- No new Python packages beyond libzim (already in pyproject.toml)
- No new system packages required for Phase 5.1 (zimcheck is optional)
- No Docker config changes
- No changes to any existing code (Phase 4 federation is unaffected)
- No new environment variables or secrets
- No OPDS changes — OPDS generator was implemented in Phase 4, works as-is

---

*Generated: 2026-05-19*
*Implementation complete at commit ec0ff7be on feature/zimwriter-libzim-activation*
*Merge target: main (open-repo remote)*
*Deployment target: May 30-31*
