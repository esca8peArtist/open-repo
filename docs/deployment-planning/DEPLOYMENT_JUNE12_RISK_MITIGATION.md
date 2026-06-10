---
title: "Open-Repo June 12, 2026 — Risk Mitigation and Failure Mode Playbooks (ZimWriter Phase 5)"
project: open-repo
phase: "5 — ZimWriter libzim activation"
document_type: risk-mitigation-playbook
status: EXECUTE DURING DEPLOYMENT — keep open in separate terminal window
created: 2026-06-10
target_deployment_date: 2026-06-12
deployment_window: "UNRESOLVED — 09:00 UTC or 20:00 UTC — user must confirm"
rollback_time_estimate: "7–9 minutes (all failure modes)"
decision_authority: "Deployer has unilateral rollback authority — no escalation required"
prerequisite_documents:
  - DEPLOYMENT_JUNE12_PREFLIGHT_ENVIRONMENT.md (this directory — must be completed first)
  - projects/open-repo/DEPLOYMENT_JUNE12_RISK_MITIGATION.md (root-level rollback playbook Steps 1–6)
---

# Risk Mitigation and Failure Mode Playbooks — ZimWriter Phase 5
## June 12, 2026

**Purpose**: Every identified failure mode for the June 12 ZimWriter deployment, with binary detection criteria, step-by-step recovery procedures, and time estimates. This document is ZimWriter-specific and deepens the four failure modes covered in the root-level `projects/open-repo/DEPLOYMENT_JUNE12_RISK_MITIGATION.md`.

**How to use**: Keep this document open in a terminal window (or printed) during deployment execution. The root-level risk mitigation document contains the six-step rollback playbook (Rollback Steps 1–6 in Section 1). When a failure mode in this document says "initiate rollback," go to the root-level document's Section 1 and execute those steps exactly.

**Decision rule**: You have a 5-minute budget to attempt a quick fix for any failure mode. If the quick fix does not resolve the issue within 5 minutes, initiate rollback immediately. Do not chase a second quick fix.

---

## TIMING CONFLICT NOTICE

This document uses **09:00 UTC** as the deployment start time, consistent with the June 6 documents. The June 3 runbook and go-live checklist use **20:00 UTC**. The user must resolve this before deployment. All time references herein assume 09:00 UTC. If 20:00 UTC is confirmed, add 11 hours to all "by HH:MM UTC" deadlines.

---

## Pre-Deployment Risk Register

Before reviewing individual failure modes, the deployer should internalize the overall risk profile:

| Failure Mode | Probability | Impact | Pre-Mitigated By |
|-------------|-------------|--------|-----------------|
| FM1: Database migration failure | Low (3%) | Critical | Pre-flight Section 3.3 migration dry-run |
| FM2: libzim runtime error | Medium (15%) | High | Pre-flight Sections 5.1–5.3, integration test 6.1 |
| FM3: API downtime exceeds window | Low (10%) | Medium | Maintenance window communication, fast service start |
| FM4: Rollback failure | Very Low (2%) | High | Backup restoration smoke test (pre-flight Section 7.1) |
| FM5: Communication/coordination failure | Low (5%) | Low | Communication templates, single-deployer authority |
| FM6: Deployment window slip | Medium (20%) | Low | 2-hour buffer built into schedule |

Probabilities assume all pre-flight checks passed. If any pre-flight check was skipped or failed without remediation, probability for FM1–FM4 increases by 2–3x.

---

## Failure Mode 1 — Database Migration Failure

### What Can Go Wrong

The `zim_exports` table (migration `003_add_zim_exports_table.py`) does not exist on the target production database, or the Alembic version table is out of sync with the actual schema. This causes an `OperationalError` on first database write to `zim_exports` and prevents ZIM export functionality from working post-deployment.

Note: Phase 5 does not introduce a *new* migration for the June 12 deployment. Migration 003 was created and applied during the Phase 5 implementation window. This failure mode fires only if the production database is a different instance than the development database, or if the schema has been manually modified since migration 003 was applied.

### Probability Assessment: Low (3%)

The pre-flight Section 3.3 migration dry-run and Section 3.2 schema check both catch this failure before deployment. If both pre-flight checks passed, the probability of encountering this failure at deployment time is below 3%. If the pre-flight migration checks were skipped, treat probability as High (40%).

### Impact

- **User-facing**: ZIM export button in the UI fails with HTTP 500. OPDS feed and federation functionality unaffected (different tables).
- **Data**: No data loss risk. The existing `federation_partners` and `federation_conflicts` tables are not touched.
- **Recovery time**: 7–15 minutes (schema repair) or 7–9 minutes (rollback).

### Detection — How You Know This Happened

Watch for these signals within 3 minutes of the new service starting:

**Signal 1 — Application log**:
```bash
sudo journalctl -u open-repo -f --since now
```
Error pattern to watch for:
```
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: zim_exports
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "zim_exports" does not exist
```

**Signal 2 — Alembic check**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
uv run alembic current
```
Failure output:
```
ERROR [alembic.util.messaging] Can't locate revision identified by '003abc...'
```
or
```
[current]  (head: 002def...)   ← not at head; migration 003 never applied
```

**Signal 3 — Schema check**:
```bash
uv run python -c "
from sqlalchemy import inspect, create_engine
import os
engine = create_engine(os.environ['DATABASE_URL'])
tables = inspect(engine).get_table_names()
print('zim_exports' in tables)
"
```
Failure output: `False`

### Root Cause Analysis

**Most likely**: The production database is a clean instance or a copy taken before migration 003 was applied.

**Second most likely**: The Alembic version table exists but records an older revision because the migration was applied manually (with SQL DDL directly) rather than via `alembic upgrade head`, leaving the version tracking out of sync.

**Third most likely**: Connection string in `DATABASE_URL` points to the wrong database host or file path (e.g., still pointing to the dev database), and that database does not have migration 003.

### Immediate Action — First 5 Minutes

Do **not** roll back immediately. Attempt a schema repair first.

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "FAILURE MODE 1 ACTIVATED: $(date -u +%T UTC)"
echo "Attempting schema repair: alembic upgrade head"

# Attempt 1: standard upgrade
uv run alembic upgrade head
UPGRADE_EXIT=$?

if [ $UPGRADE_EXIT -eq 0 ]; then
  echo "Schema repair succeeded at $(date -u +%T UTC)"
  
  # Re-verify schema
  uv run python -c "
from sqlalchemy import inspect, create_engine
import os
engine = create_engine(os.environ['DATABASE_URL'])
tables = inspect(engine).get_table_names()
for t in ['federation_partners', 'federation_conflicts', 'zim_exports']:
    status = 'PASS' if t in tables else 'FAIL'
    print(f'{status}: {t}')
"
  echo "If all 3 tables PASS — continue deployment. Do NOT restart the service."
  echo "The application will find the tables on its next database operation."
else
  echo "Schema repair failed (exit: $UPGRADE_EXIT)"
  echo "5-minute quick-fix budget exhausted"
  echo "INITIATING ROLLBACK"
fi
```

**If repair succeeds**: Resume deployment. No restart needed. Log the incident.

**If repair fails within 5 minutes**: Execute the root-level rollback playbook (Steps 1–6 from `projects/open-repo/DEPLOYMENT_JUNE12_RISK_MITIGATION.md` Section 1).

### Recovery Procedure (Full Rollback)

Follow root-level `DEPLOYMENT_JUNE12_RISK_MITIGATION.md` Section 1, Steps 1–6.

Timing breakdown:
- Step 1 (stop service): 30 seconds
- Step 2 (restore database from pre-deployment backup): 2–3 minutes — **critical**: use the backup created in pre-flight Section 3.4, not any older backup
- Step 3 (revert code): 1 minute
- Step 4 (reinstall dependencies): 2–3 minutes
- Step 5 (start service): 30 seconds
- Step 6 (verify): 1 minute

**Total**: 7–9 minutes.

### Verification After Recovery

```bash
# Verify previous version is running
curl -s http://100.70.184.84:8000/health | python3 -c "import json,sys; d=json.load(sys.stdin); print(d)"
# Expected: {"status": "ok", ...}

# Verify OPDS feed still works (federation not affected by this failure)
curl -s -H "Accept: application/atom+xml" http://100.70.184.84:8000/api/v2/opds/root.xml | head -5
# Expected: valid Atom XML starting with <?xml version="1.0"...
```

### Timeline

| Phase | Duration |
|-------|----------|
| Detection | < 3 minutes |
| Quick-fix attempt | 0–5 minutes |
| Rollback (if quick-fix fails) | 7–9 minutes |
| Verification | 2 minutes |
| **Worst-case total** | **< 17 minutes** |

### Prevention for Next Deployment

1. Add `uv run alembic current` to the deployment script as a hard gate before `systemctl restart open-repo`.
2. Add the schema check (Section 3.2 of pre-flight) to CI/CD so it runs against a production-equivalent database before any release is tagged.
3. Add an Alembic head check as a FastAPI startup event: the application should refuse to start if the database schema is not at the current head revision.

---

## Failure Mode 2 — libzim Runtime Error

### What Can Go Wrong

The libzim C shared library (`libzim.so` or the Python wheel) raises an exception at runtime during an actual ZIM export operation. This is distinct from an import failure (which would be caught by pre-flight Section 5.1). A runtime error occurs when `Creator.__enter__()` is called, when `config_indexing()` is called, or when the ZIM file is flushed to disk at `Creator.__exit__()`.

This is the highest-risk failure mode unique to the ZimWriter feature because libzim's C/Python boundary is less predictable than pure-Python code. The pre-flight integration test in Section 6.1 substantially reduces this risk, but does not eliminate it — production content may trigger edge cases not covered by the test corpus.

### Probability Assessment: Medium (15%) without pre-flight; Low (5%) if pre-flight Section 6.1 passed

The 51 ZIM unit tests and the integration test cover the primary code paths. However:
- Production content may contain characters outside the tested corpus (special Unicode, RTL scripts)
- Production content may be larger than the 3-article integration test, triggering memory pressure on the Pi 5
- libzim's behavior under thermal throttling has not been tested

### Impact

- **User-facing**: ZIM export fails with an error message. The `/api/v2/export/zim` endpoint returns HTTP 500. OPDS, federation, and all other endpoints are unaffected.
- **Data**: No data loss. The failed export does not write a partial ZIM file to the exports directory (libzim either completes or fails atomically).
- **Recovery time**: 15–30 minutes for diagnosis and targeted fix; 7–9 minutes if full rollback is needed.

### Detection — How You Know This Happened

**Signal 1 — User report**: A user attempts a ZIM export and receives an error response.

**Signal 2 — Application log** (within seconds of an export attempt):
```bash
sudo journalctl -u open-repo -f --since now
```
Watch for:
```
RuntimeError: Creator started
AttributeError: 'Creator' object has no attribute 'config_indexing'
libzim.error.ZimFileFormatError: ...
OSError: [Errno 28] No space left on device
MemoryError
Killed    ← OOM killer terminated the process
```

**Signal 3 — Service crash** (OOM or segfault):
```bash
sudo systemctl is-active open-repo
# Returns: failed   ← libzim caused a segfault or OOM
sudo journalctl -u open-repo -n 30 | grep -E "Killed|segfault|OOM"
```

### Root Cause Analysis

**Root cause A — `RuntimeError: Creator started`**:  
`config_indexing()` was called after `Creator.__enter__()`. This is the ordering bug fixed in commits `1dee5c99` and `be29394b`. If this fires in production, the wrong code version was deployed. Verify git commit: `git log --oneline -1`.

**Root cause B — `AttributeError: config_indexing`**:  
The installed libzim version is < 3.2. The Python wheel on the production host may be older than the development wheel. Check: `uv run python -c "import libzim; print(libzim.__version__)"`.

**Root cause C — OOM / process killed**:  
The export content is large enough to exhaust the Pi 5's available RAM. The Pi 5 has 4 GB or 8 GB RAM, but available memory at export time may be lower due to OS processes and the application itself. The ZimWriter buffers all article content in memory before writing. Check: `dmesg | grep -i oom`.

**Root cause D — Disk full during write**:  
The ZIM file write exhausted available disk space. Check: `df -h /opt`.

**Root cause E — libzim shared library incompatibility**:  
The libzim Python wheel bundles a `libzim.so` compiled for a specific glibc and libc++ version. If the production host's system libraries differ from the wheel's expectations, a `ImportError: libzim.so: ... cannot open shared object file` or a silent segfault can occur. This should have been caught by pre-flight Section 5.1, but is listed here for completeness.

### Immediate Action — First 5 Minutes

```bash
# Step 1: Capture the exact error
sudo journalctl -u open-repo --since "5 minutes ago" | grep -E "ERROR|CRITICAL|Traceback|RuntimeError|AttributeError" | tail -30

# Step 2: Service still running?
sudo systemctl is-active open-repo

# Step 3: If service is still running — this is a per-request failure, not a crash
# The service remains operational for non-ZIM endpoints
# Attempt to reproduce the error with a direct test export:
curl -s -X POST http://127.0.0.1:8000/api/v2/export/zim \
  -H "Content-Type: application/json" \
  -d '{"title": "Test", "entry_ids": [1]}' | python3 -m json.tool
```

**Decision tree**:

```
Error: RuntimeError: Creator started
  → git log --oneline -1  (verify correct commit is deployed)
  → If wrong commit: revert to correct branch, redeploy
  → If correct commit: THIS IS UNEXPECTED — escalate and rollback

Error: AttributeError: config_indexing
  → uv run python -c "import libzim; print(libzim.__version__)"
  → If < 3.2: uv pip install "libzim>=3.2" && sudo systemctl restart open-repo
  → If already 3.2+: THIS IS UNEXPECTED — rollback

Error: OOM / process killed
  → Check memory: free -m
  → If memory exhausted: export limit too large for this hardware
  → Immediate workaround: limit export size in request handler (max_entries param)
  → Do NOT rollback — ZIM feature disabled temporarily; other features unaffected
  → Schedule fix for next deployment

Error: No space left on device
  → df -h /opt
  → Remove old ZIM exports: find /opt/exports -name "*.zim" -mtime +7 -delete
  → Retry export

Service crashed (is-active: failed)
  → Check for OOM or segfault (see root cause C and E above)
  → If segfault: ROLLBACK IMMEDIATELY (libzim ABI incompatibility — not fixable at deploy time)
```

**If quick fix does not resolve within 5 minutes**: Execute root-level rollback playbook Steps 1–6.

**Important exception**: If the service is still running and only ZIM exports fail (all other endpoints return 200), do NOT roll back. Instead, disable the ZIM export endpoint temporarily and schedule a targeted fix. The ZimWriter is an additive feature; rolling it back returns to the pre-Phase-5 state where ZIM export was unavailable.

### Recovery Procedure

**Option A — Targeted fix (service still running, ZIM endpoint only failing)**:

```bash
# Disable ZIM export endpoint temporarily via feature flag (if available)
# OR: rate-limit to 0 requests at the nginx/reverse-proxy level
# Continue monitoring all other endpoints
# Schedule targeted libzim fix for next deployment window
```

**Option B — Full rollback (service crashed)**:

Execute root-level `DEPLOYMENT_JUNE12_RISK_MITIGATION.md` Section 1, Steps 1–6.

### Verification After Recovery

```bash
# Verify health endpoint
curl -s http://100.70.184.84:8000/health
# Expected: HTTP 200, {"status": "ok"}

# Verify OPDS feed (not affected by ZIM failure)
curl -s -H "Accept: application/atom+xml" http://100.70.184.84:8000/api/v2/opds/root.xml | head -3
# Expected: <?xml version="1.0"...
```

### Timeline

| Phase | Duration |
|-------|----------|
| Detection (log monitoring) | 0–5 minutes |
| Root cause diagnosis | 5–15 minutes |
| Targeted fix (if applicable) | 10–20 minutes |
| Full rollback (if service crashed) | 7–9 minutes |
| **Worst-case targeted fix** | **35 minutes** |
| **Worst-case full rollback** | **25 minutes** |

### Prevention for Next Deployment

1. Add a canary export endpoint (`/api/v2/export/zim/test`) that runs a 1-article export without saving to disk, as a production health check callable post-deployment.
2. Add a ZIM export memory guard: estimate article content size before starting the `Creator` context and reject exports > 200 MB estimated output size on the Pi 5.
3. Test a production-equivalent content corpus (real data, real content sizes) in the pre-flight integration test rather than 3 dummy articles.

---

## Failure Mode 3 — API Downtime During Deploy

### What Can Go Wrong

The deployment procedure requires stopping the running service (`systemctl stop open-repo`) before deploying the new code and restarting. During this window, all API endpoints return `Connection refused`. If the deployment process stalls (dependency installation hangs, migration takes longer than expected), this downtime window extends beyond the planned maintenance window.

### Probability Assessment: Low (10%) for extended outage; High (90%) for brief planned downtime

Brief downtime (2–5 minutes) during the stop/restart sequence is **expected and planned**. This failure mode covers only the case where downtime extends beyond the maintenance window end time (09:45 UTC if 09:00 UTC start, or 20:45 UTC if 20:00 UTC start).

### Impact

- **User-facing**: All endpoints unavailable during the gap. API clients receive `Connection refused` (or HTTP 503 if a reverse proxy is in front of the service).
- **Data**: No data loss during a clean stop.
- **Recovery time**: The issue is resolved when the service starts successfully. If the service cannot start, rollback resolves it.

### Detection — How You Know This Is Exceeding Acceptable Bounds

The planned downtime window is 45 minutes total (start time to expected service restoration). Monitor from the deployment machine:

```bash
# Start a timer when you execute systemctl stop open-repo
STOP_TIME=$(date +%s)

# Poll health endpoint during deployment
while true; do
  ELAPSED=$(( $(date +%s) - STOP_TIME ))
  HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://100.70.184.84:8000/health 2>/dev/null)
  echo "$(date -u +%T UTC) — elapsed: ${ELAPSED}s — health: $HTTP_CODE"
  
  if [ "$HTTP_CODE" = "200" ]; then
    echo "SERVICE RESTORED at $(date -u +%T UTC)"
    break
  fi
  
  if [ "$ELAPSED" -gt 2700 ]; then
    echo "ALERT: Service has been down for >45 minutes — escalation required"
    break
  fi
  
  sleep 30
done
```

**Hard deadline**: If the service has not returned `HTTP 200` from `/health` within 45 minutes of `systemctl stop open-repo`, initiate rollback.

### Root Cause Analysis

**Root cause A — Dependency installation hangs**: `uv pip install -e ".[dev]"` hangs or fails on an aarch64-specific compilation. Most likely for packages with C extensions. Detection: no output from the pip install command for > 5 minutes.

**Root cause B — Migration takes longer than expected**: Not applicable for this deployment (no new migration); but if `alembic upgrade head` is included in the deployment procedure, a large table migration on production data can be slow.

**Root cause C — Service fails to start after deploy**: Covered by Failure Mode 2.

**Root cause D — Disk full during code deploy**: `rsync` or `git pull` fails because the deployment directory is full.

### Immediate Action — First 5 Minutes

```bash
# T+0: systemctl stop open-repo
# T+1 to T+5: Monitor deployment procedure progress

# If dependency install appears hung (no output for > 3 minutes):
# Cancel and check for the specific failing package:
# Kill the uv run pip install process (Ctrl+C)
uv pip install --verbose -e ".[dev]" 2>&1 | tee /tmp/dep-install-verbose.txt
# Check last line of output to see which package is stuck
```

**If at T+20 minutes the service has not started**: Short-circuit the deployment procedure. Go directly to Rollback Steps 3–5 (skip Step 2 if no code changes have been written to the production database yet). This restores the previous version without waiting for the new version to finish deploying.

### Recovery Procedure

```bash
echo "=== FAILURE MODE 3: DOWNTIME EXCEEDS WINDOW ==="
echo "Initiated at: $(date -u +%T UTC)"
echo "Elapsed downtime: $ELAPSED seconds"

# Option A: If new code was not fully deployed (stopped during install)
# Go directly to Rollback Step 3 (code revert) — skip Steps 1-2
# The service is already stopped (Step 1 is done)
# No database changes have been made (Step 2 skipped)

ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'QUICK_REVERT'
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
echo "Reverting to previous stable version..."
git fetch origin master
git reset --hard origin/master~1
echo "Previous version restored:"
git log --oneline -1

cd backend
pip install -r requirements.txt --quiet
echo "Dependencies reinstalled"

sudo systemctl start open-repo
sleep 5
sudo systemctl is-active open-repo && echo "PASS: Service started" || echo "FAIL: Service failed to start"

HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/health)
echo "Health check: $HEALTH"
QUICK_REVERT
```

### Verification After Recovery

```bash
# From deployment machine
curl -s http://100.70.184.84:8000/health
curl -s -H "Accept: application/atom+xml" http://100.70.184.84:8000/api/v2/opds/root.xml | head -3
echo "Service restored at: $(date -u +%T UTC)"
```

### Timeline

| Phase | Duration |
|-------|----------|
| Planned downtime (expected) | 2–5 minutes |
| Detection threshold (unacceptable) | > 45 minutes total |
| Recovery (code revert only) | 5–7 minutes |
| Recovery (full rollback with DB) | 7–9 minutes |
| **Maximum acceptable total downtime** | **60 minutes** |

### Prevention for Next Deployment

1. Pre-stage the dependency installation on the production host before the maintenance window opens (run `uv pip install -e ".[dev]"` the day before, using the tagged release version). This eliminates installation time from the deployment window.
2. Keep a cached copy of the previous virtual environment. If the new install fails, restore the cached venv instead of reinstalling from scratch.
3. Use a deployment script that sets a hard timeout on each step (`timeout 300 uv pip install ...`) rather than waiting indefinitely.

---

## Failure Mode 4 — Rollback Failure

### What Can Go Wrong

A rollback is initiated because of FM1, FM2, or FM3 — but the rollback itself fails. The most common cause is that the pre-deployment database backup (pre-flight Section 3.4) is unavailable, corrupt, or points to the wrong file path.

### Probability Assessment: Very Low (2%) if pre-flight Section 7.1 passed

Pre-flight Section 7.1 (backup restoration smoke test) directly validates the rollback path. If that test passed, the probability of a rollback failure is < 2%. If Section 7.1 was skipped, treat as Medium (15%).

### Impact

**This is the worst-case failure mode.** If rollback fails:
- The new code failed to deploy
- The production database may be in an inconsistent state
- The previous code version cannot be restored automatically
- Service remains down until manual intervention

**Severity**: High — extended downtime, possible data inconsistency, requires infrastructure team involvement.

### Detection — How You Know Rollback Is Failing

```bash
# During Rollback Step 2 (restore database), look for:
cp: error writing '/opt/data/open-repo.db': No space left on device
# → Disk full

cp: cannot stat '/opt/db-backups/open-repo-20260612-*.db.bak': No such file or directory
# → Backup file missing

sqlite3 /opt/data/open-repo.db "PRAGMA integrity_check;" → "*** in database main ***"
# → Backup is corrupt (restoration completed but database is invalid)

# During Rollback Step 3 (code revert):
error: cannot lock ref 'HEAD': ...
fatal: cannot reset — git failure
# → Git repository in bad state (locked index, detached HEAD with pending files)
```

### Root Cause Analysis

**Root cause A — Backup file missing**: The backup path variable was wrong during the backup step. The file was created in a different location than where the restore script looks.

**Root cause B — Disk full at restore time**: The failed deployment wrote partial files that consumed the disk space available at rollback time.

**Root cause C — Backup is corrupt**: The `cp` command during backup was interrupted (power loss, kernel panic). The file exists but is truncated.

**Root cause D — Git repository locked**: A previous git operation left a `.git/index.lock` file. `git reset --hard` fails.

### Immediate Action — First 5 Minutes

```bash
echo "=== FAILURE MODE 4: ROLLBACK FAILURE ==="

# Assess situation
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'ASSESS'
echo "--- Disk space ---"
df -h /opt /

echo "--- Backup files ---"
ls -lah /opt/db-backups/ 2>/dev/null || echo "Backup directory not found"
find /tmp -name "*.db.bak" -o -name "*.db" 2>/dev/null | head -5

echo "--- Git state ---"
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
git status
ls .git/index.lock 2>/dev/null && echo "INDEX.LOCK EXISTS — remove it" || echo "No index lock"

echo "--- Database file ---"
ls -lah /opt/data/open-repo.db 2>/dev/null || echo "Database file not found"
ASSESS
```

### Recovery Procedures by Root Cause

**Procedure A — Backup file missing**: Find it.
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'FIND_BACKUP'
echo "Searching for backup files..."
find / -name "*.db.bak" -newer /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend 2>/dev/null
find / -name "open-repo*.db" 2>/dev/null | head -10
FIND_BACKUP
```

**Procedure B — Disk full at restore time**: Free space first.
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'FREE_DISK'
# Remove partial deployment artifacts
find /tmp -name "*.zim" -delete 2>/dev/null
find /opt -name "*.pyc" -delete 2>/dev/null
# Remove non-essential logs older than 1 day
find /var/log -name "*.log.gz" -mtime +1 -delete 2>/dev/null
df -h /opt
FREE_DISK
# Then retry the backup restore
```

**Procedure C — Backup corrupt**: Use the previous-generation backup.
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'SECOND_GEN'
ls -lt /opt/db-backups/
SECOND_LATEST=$(ls -t /opt/db-backups/*.db.bak 2>/dev/null | sed -n '2p')
echo "Second-generation backup: $SECOND_LATEST"
if [ -n "$SECOND_LATEST" ]; then
  sqlite3 "$SECOND_LATEST" "PRAGMA integrity_check;" 
  # If "ok" → use this for restore
fi
SECOND_GEN
```

**Procedure D — Git index lock**: Remove the lock file.
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'GIT_FIX'
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
rm -f .git/index.lock
git status
git reset --hard origin/master~1
GIT_FIX
```

**Last resort — Manual service restoration**:

If no backup can be restored and git revert fails, start the application against the current (potentially inconsistent) database state:

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'MANUAL_START'
# Start with current code, whatever state it is in
# The application may work for non-ZIM functionality even with schema issues
sudo systemctl start open-repo || true

# If systemctl fails, try manual uvicorn start
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
source /opt/venv/open-repo/bin/activate
DATABASE_URL="$DATABASE_URL" uvicorn app.main:create_app \
  --host 127.0.0.1 --port 8000 &
sleep 5
curl -s http://127.0.0.1:8000/health
MANUAL_START
```

### Verification After Recovery

```bash
# Verify service is responding
curl -s http://100.70.184.84:8000/health
# Expected: any non-empty response

# Verify database is accessible (even if schema is incomplete)
curl -s http://100.70.184.84:8000/api/v2/opds/root.xml | head -3

# Document the state:
echo "Recovery state at $(date -u): $(curl -s -o /dev/null -w '%{http_code}' http://100.70.184.84:8000/health)"
```

### Timeline

| Phase | Duration |
|-------|----------|
| Detection (rollback step fails) | Immediate |
| Assessment | 5 minutes |
| Single-cause fix | 5–15 minutes |
| Multi-cause recovery | 30–60 minutes |
| Infrastructure team involvement | 1–4 hours |
| **Maximum acceptable before escalation** | **30 minutes** |

### Escalation

If rollback cannot be completed within 30 minutes by the on-call deployer alone, escalate to the infrastructure team. Provide:
1. Exact error message from the failing rollback step
2. Output of the Assessment block above
3. Current disk usage (`df -h /opt`)
4. Current git state (`git log --oneline -3` and `git status`)

### Prevention for Next Deployment

1. Store the pre-deployment backup in **two locations**: the primary backup directory and `/tmp/open-repo-rollback-backup.db.bak`. The `/tmp` location provides a fast-path restore even if `/opt` is full.
2. Run `df -h /opt` immediately before creating the backup to confirm there is 3x the database size available in free space.
3. Add the backup file path and hash to the deployment log at backup creation time, so the restore script can verify it is using the correct file.

---

## Failure Mode 5 — Communication / Coordination Failure

### What Can Go Wrong

The deployer loses their SSH connection to the production host mid-deployment, the deployment machine crashes, or there is no way to notify stakeholders of deployment status.

### Probability Assessment: Low (5%)

SSH over Tailscale is generally reliable. The main risk is a long-running deployment operation that holds the SSH session open for > 30 minutes with no activity, triggering an SSH timeout.

### Impact

- **User-facing**: If SSH drops during `systemctl stop open-repo`, the service remains stopped with no one to restart it.
- **Recovery time**: 5–15 minutes (reconnect and resume) or 7–9 minutes (rollback).

### Detection

- SSH session disconnects (terminal shows `broken pipe` or `Connection closed`)
- The deployment machine loses network connectivity to Tailscale (ping to 100.70.184.84 fails)
- No response to stakeholder status updates

### Immediate Action

```bash
# From any machine with Tailscale access, reconnect immediately
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84

# Check service state
sudo systemctl is-active open-repo

# Check what step the deployment was on
sudo journalctl -u open-repo -n 20
git -C /home/awank/dev/SuperClaude_Framework/projects/open-repo log --oneline -3
```

**If service is stopped and deployment is mid-flight**: Resume from the step where the SSH connection dropped. Review the deployment procedure document to identify the current step based on what the git log and systemctl status show.

**If the deployment state is unclear after 5 minutes of assessment**: Execute rollback. It is safer to roll back to a known-good state than to continue from an uncertain point.

### Prevention

Use `tmux` or `screen` to run the deployment inside a persistent session. If the SSH connection drops, reconnect and reattach:

```bash
# Start a named tmux session before beginning deployment
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84
tmux new-session -s deployment

# All deployment commands go inside this session.
# If SSH drops, reconnect and:
tmux attach-session -t deployment
# The session continues running and all output is preserved.
```

### Communication Templates

If the deployment extends beyond the planned window, notify stakeholders using the templates in `projects/open-repo/DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md`:
- Template 4 (Escalation): if any failure mode fires
- Template 3 (Success): when deployment completes
- Template 5 (Post-Deployment Status): 10 hours post-deployment

---

## Failure Mode 6 — Deployment Window Slip

### What Can Go Wrong

The deployment takes longer than the planned 45-minute window. The service remains in a degraded state beyond the planned maintenance window end time.

### Probability Assessment: Medium (20%)

The expected deployment duration is 25–35 minutes (per `DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md`). Dependency installation on aarch64 can be slow (5–15 minutes for packages with C extensions). If any pre-flight check was not completed June 11 and must be done June 12 morning, the window expands.

### Impact

- **User-facing**: Downtime extends beyond the communicated maintenance window end. This damages user trust if the window was communicated to stakeholders.
- **Operational**: The deployer may be under pressure to cut corners (skip verification steps). Do not cut corners. A 15-minute overrun is much better than a deployment that requires rollback.

### Detection

Monitor elapsed time from the start of `systemctl stop open-repo`:

```bash
DEPLOY_START=$(date +%s)
echo "Deployment started at: $(date -u)"

# At any point, check elapsed time:
ELAPSED=$(( $(date +%s) - DEPLOY_START ))
echo "Elapsed: $((ELAPSED / 60)) minutes $((ELAPSED % 60)) seconds"
```

**Alert thresholds**:
- 30 minutes elapsed, service not yet started: assess whether on-track
- 45 minutes elapsed, service not yet started: prepare stakeholder communication about extended window
- 60 minutes elapsed, service not yet started: initiate rollback

### Immediate Action

At 45 minutes elapsed, do **not** cut verification steps. Instead:

1. Send the extended outage communication (Template 4, "Extended Outage" block in `DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md`)
2. Continue deployment at current pace
3. Do not start a new deployment step that will take > 10 minutes if you are already at 45 minutes

At 60 minutes elapsed with service still down: rollback.

```bash
# Decision at T+60 minutes:
echo "=== DEPLOYMENT WINDOW EXCEEDED 60 MINUTES ==="
echo "Current state:"
sudo systemctl is-active open-repo
git -C /home/awank/dev/SuperClaude_Framework/projects/open-repo log --oneline -1
echo ""
echo "Initiating rollback per FM6 protocol"
# Execute root-level rollback Steps 1-6
```

### Prevention

1. Complete all pre-flight checks on June 11 (not June 12 morning). The pre-flight checks take 90 minutes; doing them during the deployment window doubles the deployment duration.
2. Pre-stage `uv pip install -e ".[dev]"` on June 11 by running it on the production host with the tagged release version. This eliminates the longest-running deployment step.
3. Have a second terminal open to the production host throughout deployment so there is no session-establishment latency when checking on service status.

---

## Rollback Decision Matrix

Reference this during deployment. If the "Rollback?" column says Yes, execute root-level `DEPLOYMENT_JUNE12_RISK_MITIGATION.md` Section 1, Steps 1–6.

| Symptom Observed | Failure Mode | Quick Fix Available? | Rollback? |
|-----------------|-------------|---------------------|-----------|
| `no such table: zim_exports` in logs | FM1: Migration | `alembic upgrade head` (1 try, 5 min) | Yes, if fix fails |
| `alembic current` mismatches head | FM1: Migration | `alembic upgrade head` (1 try, 5 min) | Yes, if fix fails |
| `RuntimeError: Creator started` | FM2: libzim | No — wrong code version | Yes |
| `AttributeError: config_indexing` | FM2: libzim | `uv pip install "libzim>=3.2"` | Yes, if install fails |
| Service crashed (is-active: failed) | FM2: libzim | Check logs; port kill if port conflict | Yes, if not port conflict |
| ZIM endpoint fails, others OK | FM2: libzim (partial) | Disable ZIM endpoint | No rollback; schedule fix |
| OOM during large export | FM2: libzim | Reduce export size | No rollback; add memory guard |
| Downtime > 45 minutes | FM3: Downtime | N/A — continue or rollback | Yes, if > 60 minutes |
| Backup restore fails | FM4: Rollback failure | Find alternate backup | N/A — rollback is in progress |
| SSH drops mid-deploy | FM5: Communication | Reconnect, assess state | Yes, if state unclear |
| Deploy > 60 minutes | FM6: Window slip | No | Yes |

---

## Incident Log Template

If any failure mode fires, document it immediately:

```
INCIDENT LOG — June 12, 2026 Deployment
Date/time: ______________ UTC
Failure mode: FM__ — [name]
Step in deployment procedure where detected: Step __
Exact error message:

  [paste here]

Action taken:
  [ ] Quick fix attempted: ____________________
  [ ] Quick fix successful / failed
  [ ] Rollback initiated at: ______________ UTC
  [ ] Rollback completed at: ______________ UTC
  [ ] Service restored at: ______________ UTC

Data impact:
  [ ] No data loss
  [ ] Possible data written between T+X and rollback: ________________

Post-incident:
  [ ] Stakeholder communication sent (Template __) at ______________ UTC
  [ ] Post-mortem scheduled for: __________________
  [ ] Prevention item added to next deployment checklist: ________________
```

---

**Document Version**: 1.0  
**Created**: 2026-06-10  
**Valid For**: June 12, 2026 deployment  
**Supersedes/augments**: projects/open-repo/DEPLOYMENT_JUNE12_RISK_MITIGATION.md (root-level, covers general failure modes; this document is ZimWriter-specific and deeper)  
**Rollback Playbook Location**: projects/open-repo/DEPLOYMENT_JUNE12_RISK_MITIGATION.md Section 1, Steps 1–6  
**Keep open during**: All deployment steps from systemctl stop to post-deployment verification
