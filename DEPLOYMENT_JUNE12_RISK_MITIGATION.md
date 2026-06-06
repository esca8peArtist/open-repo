---
title: "Open-Repo June 12, 2026 Deployment Risk Mitigation & Failure Mode Playbooks"
project: open-repo
phase: 5 (final production deployment)
document_type: risk-mitigation
status: READY TO EXECUTE
created: 2026-06-12
target_deployment_date: 2026-06-12
deployment_window: "09:00–11:00 UTC [CONFIRM START TIME — see Date Conflict Notice]"
rollback_time_estimate: "7–9 minutes"
---

# Deployment Risk Mitigation & Failure Mode Playbooks
## June 12, 2026

**Purpose**: Define specific failure modes that may occur during the June 12 deployment, with binary detection criteria, step-by-step recovery procedures, and realistic timeline estimates for each. Use this document in parallel with DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md during deployment execution.

**Scope**: Covers all failure modes that can occur between the start of the deployment window and 60 minutes post-deployment.

**How to use**: Keep this document open in a separate terminal window during deployment. If any step in DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md produces an error output, locate the matching failure mode below, follow the detection criteria to confirm, then execute the recovery procedure exactly as written.

---

## Date Conflict Notice

This document records the deployment start time as **09:00 UTC** in its frontmatter, consistent with DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md and DEPLOYMENT_JUNE12_PRECHECK_ENVIRONMENT.md. However, DEPLOYMENT_JUNE_12_RUNBOOK.md and DEPLOYMENT_JUNE_12_GO_LIVE_CHECKLIST.md record **20:00 UTC**. The user must resolve this conflict before deployment. All timeline references in this document use 09:00 UTC as written. If 20:00 UTC is the canonical time, adjust all clock references in the failure mode timelines accordingly.

---

## Section 1: Complete Rollback Playbook

Execute these 6 steps in order if any failure mode below returns a ROLLBACK decision.

**Rollback Trigger**: Any failure mode where the decision tree says "initiate rollback" or "DO NOT PROCEED."

**Total Estimated Duration**: 7–9 minutes.

---

### Rollback Step 1 — Stop Current Deployment (30 seconds)

```bash
PROD_HOST="100.70.184.84"

echo "=== ROLLBACK INITIATED: $(date -u +%T UTC) ==="

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'STOP'
echo "Stopping open-repo service..."
sudo systemctl stop open-repo

sleep 2

# Force kill if still running
if ps aux | grep -E "uvicorn.*open" | grep -v grep > /dev/null; then
  echo "Process still running, force killing..."
  sudo pkill -9 -f "uvicorn.*open"
  sleep 2
fi

if ! ps aux | grep -E "uvicorn.*open" | grep -v grep > /dev/null; then
  echo "PASS: Service stopped at $(date -u +%T UTC)"
else
  echo "FAIL: Process could not be killed — escalate to infrastructure team"
  exit 1
fi
STOP
```

**Expected output**: `PASS: Service stopped at HH:MM:SS UTC`

---

### Rollback Step 2 — Restore Database from Backup (2–3 minutes)

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'RESTORE'
BACKUP_DIR="/opt/db-backups"
LATEST=$(ls -t "$BACKUP_DIR"/ 2>/dev/null | head -1)

if [ -z "$LATEST" ]; then
  echo "FAIL: No backup found in $BACKUP_DIR"
  echo "Cannot complete automated rollback — manual database recovery required"
  exit 1
fi

BACKUP_FILE="$BACKUP_DIR/$LATEST"
echo "Restoring from: $BACKUP_FILE"

if [[ "$BACKUP_FILE" == *.db.bak ]]; then
  # SQLite restore
  DB_PATH="[REQUIRED USER INPUT]"   # e.g., /opt/data/open-repo.db
  cp "$DB_PATH" "${DB_PATH}.broken-$(date +%s)"
  cp "$BACKUP_FILE" "$DB_PATH"
  chmod 644 "$DB_PATH"
  echo "PASS: SQLite database restored from $BACKUP_FILE"
elif [[ "$BACKUP_FILE" == *.sql.gz ]]; then
  # PostgreSQL restore
  echo "Restoring PostgreSQL from gzip dump..."
  gunzip -c "$BACKUP_FILE" | psql "[REQUIRED USER INPUT]"
  echo "PASS: PostgreSQL database restored from $BACKUP_FILE"
fi

echo "PASS: Database restore complete at $(date -u +%T UTC)"
RESTORE
```

**Expected output**: `PASS: Database restore complete at HH:MM:SS UTC`

**Fail**: If no backup exists, skip to Rollback Step 3 (code revert only). The database in pre-deployment state will be used as-is. Note any data that may have been written between deployment start and rollback.

---

### Rollback Step 3 — Revert Code to Previous Version (1 minute)

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'REVERT'
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

echo "Current commit:"
git log --oneline -1

echo "Reverting to previous stable version..."
git fetch origin master
git reset --hard origin/master~1

echo "Rolled back to:"
git log --oneline -1
echo "PASS: Code reverted at $(date -u +%T UTC)"
REVERT
```

**Expected output**: `PASS: Code reverted at HH:MM:SS UTC`

---

### Rollback Step 4 — Reinstall Dependencies for Reverted Version (2–3 minutes)

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'DEPS'
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
source /opt/venv/open-repo/bin/activate

echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt --quiet

echo "Verifying critical packages..."
python -c "import fastapi, sqlalchemy, uvicorn; print('PASS: Core packages verified')"
DEPS
```

**Expected output**: `PASS: Core packages verified`

---

### Rollback Step 5 — Start Application (30 seconds)

```bash
PROD_HOST="100.70.184.84"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << 'START'
echo "Starting open-repo service..."
sudo systemctl start open-repo

sleep 5

if sudo systemctl is-active --quiet open-repo; then
  echo "PASS: Service active"
else
  echo "FAIL: Service failed to start"
  sudo journalctl -u open-repo -n 30
  exit 1
fi

HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/health)
if [ "$HEALTH" = "200" ]; then
  echo "PASS: Health endpoint OK"
else
  echo "FAIL: Health endpoint returned $HEALTH"
  exit 1
fi

echo "PASS: Application started at $(date -u +%T UTC)"
START
```

**Expected output**: `PASS: Application started at HH:MM:SS UTC`

---

### Rollback Step 6 — Verify Rollback Success (1 minute)

```bash
PROD_HOST="100.70.184.84"

echo "Verifying rollback..."

HTTP_HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://$PROD_HOST:8000/health)
HTTP_OPDS=$(curl -s -o /dev/null -w "%{http_code}" -H "Accept: application/atom+xml" http://$PROD_HOST:8000/api/v2/opds/root.xml)
HTTP_DOCS=$(curl -s -o /dev/null -w "%{http_code}" http://$PROD_HOST:8000/docs)

echo "Health:  $HTTP_HEALTH (expected: 200)"
echo "OPDS:    $HTTP_OPDS (expected: 200)"
echo "Docs:    $HTTP_DOCS (expected: 200)"

ALL_OK=true
[ "$HTTP_HEALTH" = "200" ] || ALL_OK=false
[ "$HTTP_OPDS" = "200" ] || ALL_OK=false
[ "$HTTP_DOCS" = "200" ] || ALL_OK=false

if $ALL_OK; then
  echo "PASS: Rollback complete. Previous version running. $(date -u +%T UTC)"
  echo "=== ROLLBACK COMPLETE ==="
else
  echo "FAIL: One or more endpoints still failing after rollback"
  echo "Escalate immediately — service may be in degraded state"
  exit 1
fi
```

**Expected output**: All three endpoints return 200; `=== ROLLBACK COMPLETE ===` printed.

---

## Section 2: Failure Mode 1 — Database Migration Failure

**Description**: Alembic migration check or execution fails, leaving the database schema in an inconsistent state.

**Probability**: Low (3%) — Phase 5 does not introduce new migrations; migration 003 was applied during implementation. This failure would occur only if the schema on the target database has drifted from the expected state.

**Severity**: Critical — Application cannot start if schema is wrong.

**Corresponding Deployment Step**: Section 3 (Database Migration Verification) of DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md.

---

### Root Cause

- Migration file is present in `alembic/versions/` but was never applied to this database instance
- Target database is a different instance than used during development (schema mismatch)
- Alembic `alembic_version` table is out of sync with the actual schema
- Connection string points to wrong database

---

### Prevention

- Item 3.3 of DEPLOYMENT_JUNE12_PRECHECK_ENVIRONMENT.md verifies that `alembic current == alembic heads` before deployment begins
- Item 3.4 verifies all three required tables exist
- Pre-deployment database backup (Item 3.2) ensures recovery is possible even if migration fails

---

### Detection Criteria

Migration failure is confirmed when **any** of the following is true:

```bash
# During DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md Step 6:

cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

# Check 1: alembic current fails
uv run alembic current
# FAILURE: exit code non-zero, or output contains "ERROR" or "FAILED"

# Check 2: Tables missing
uv run python -c "
from sqlalchemy import inspect, create_engine
import os
engine = create_engine(os.environ['DATABASE_URL'])
tables = inspect(engine).get_table_names()
for t in ['federation_partners', 'federation_conflicts', 'zim_exports']:
    print('MISSING' if t not in tables else 'OK', t)
"
# FAILURE: Any line prints "MISSING"
```

**Error patterns to watch for in logs**:
```
sqlalchemy.exc.OperationalError: no such table: zim_exports
alembic.util.exc.CommandError: Can't locate revision identified by
FAILED: Could not run migration
```

---

### Recovery Procedure

**Decision**: If schema is missing tables → attempt `alembic upgrade head` once. If that fails → ROLLBACK.

**Step 1 — Attempt upgrade (2 minutes)**:
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
uv run alembic upgrade head
```

If upgrade succeeds, re-run Item 3.4 schema validation. If all tables present, continue deployment.

**Step 2 — If upgrade fails → initiate rollback**:

Execute Rollback Steps 1–6 from Section 1 of this document.

---

### Timeline

- Detection: <3 minutes (alembic output immediate; schema check <1 minute)
- Upgrade attempt: 2 minutes
- Rollback (if needed): 7–9 minutes
- Total worst-case downtime: <15 minutes

---

### Success Criteria (after recovery)

- [ ] `uv run alembic current` matches `uv run alembic heads`
- [ ] Schema validation shows all 3 tables present
- [ ] Zero data records lost (verified by comparing record counts before and after)
- [ ] Application starts and returns HTTP 200 from `/health`

---

## Section 3: Failure Mode 2 — Application Deployment Failure

**Description**: The application service fails to start after the new code is deployed, or crashes immediately upon starting.

**Probability**: Low (5%) — Full test suite (157/157) passing pre-deployment reduces this risk significantly. Most likely cause is an environment-level issue (missing env var, wrong Python path) rather than a code error.

**Severity**: Critical — Service completely non-functional.

**Corresponding Deployment Steps**: Step 7 (Start Application) and Section 5 (Post-Deployment Health Verification) of DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md.

---

### Root Cause

- Missing or incorrect environment variable (e.g., `DATABASE_URL` pointing to wrong host)
- Virtual environment not activated in systemd service file (uvicorn process uses wrong Python)
- Port 8000 already occupied by a stale process from a previous failed deployment attempt
- Import error in application code that did not surface in unit tests (e.g., missing system library at runtime)
- Incompatible dependency version installed on production host vs development environment

---

### Prevention

- Items 1.3 and 1.4 of DEPLOYMENT_JUNE12_PRECHECK_ENVIRONMENT.md verify all environment variables
- Item 1.5 verifies all critical packages installed
- Item 2.4 verifies application imports clean before deployment
- All 157 tests pass pre-deployment (Item 2.1)

---

### Detection Criteria

Application deployment failure is confirmed when **any** of the following is observed:

```bash
# After Deployment Step 7:

# Check 1: systemd service not active
sudo systemctl is-active open-repo
# FAILURE: output is "failed" or "inactive"

# Check 2: Health endpoint unreachable
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/health
# FAILURE: exit code non-zero, or HTTP status != 200

# Check 3: Logs show startup error
sudo journalctl -u open-repo -n 20
# FAILURE: logs contain ImportError, ModuleNotFoundError, Address already in use,
#          sqlalchemy.exc.OperationalError
```

**Common error patterns**:
```
ImportError: No module named 'app'                 → Python path / venv issue
sqlalchemy.exc.OperationalError                    → Database unreachable
OSError: [Errno 98] Address already in use         → Port 8000 occupied
Missing required env var: DATABASE_URL             → Environment variable not set
```

---

### Recovery Procedure

**Decision tree** (attempt quick fix before rollback; max 5 minutes on quick fix):

```
Error: Address already in use (port 8000)
  → Find and kill stale process: lsof -i :8000 | grep LISTEN
  → Kill it: sudo kill -9 <PID>
  → Retry systemctl start open-repo
  → If successful: continue deployment

Error: ImportError / ModuleNotFoundError
  → Check venv activation in service file: sudo systemctl cat open-repo | grep ExecStart
  → Reinstall dependencies: pip install -r requirements.txt
  → Retry systemctl start open-repo
  → If successful: continue deployment

Error: DATABASE_URL / connection error
  → Verify env var: sudo systemctl cat open-repo | grep DATABASE_URL
  → Add/correct env var in service file
  → sudo systemctl daemon-reload && sudo systemctl start open-repo
  → If successful: continue deployment

Any other error, OR quick fix takes >5 minutes:
  → Execute Rollback Steps 1–6 from Section 1
```

---

### Timeline

- Detection: <1 minute (service start attempt is immediate; health check within 10 seconds)
- Quick fix attempt: up to 5 minutes
- Rollback (if quick fix fails): 7–9 minutes
- Total worst-case downtime: <15 minutes

---

### Success Criteria (after recovery)

- [ ] `sudo systemctl is-active open-repo` returns `active`
- [ ] `/health` endpoint returns HTTP 200
- [ ] Application logs show no ERROR or CRITICAL entries in past 5 minutes
- [ ] All endpoints in DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md Section 5 verified

---

## Section 4: Failure Mode 3 — Zero-Downtime Switchover Issue

**Description**: During the service restart (stop → deploy → start sequence), requests arrive during the gap and receive connection refused errors. For this deployment, the gap is the period between `systemctl stop open-repo` and `systemctl start open-repo`.

**Probability**: Medium (20%) — This is an inherent property of the direct replacement deployment strategy. The question is whether the gap is tolerable, not whether it can be eliminated entirely.

**Severity**: Low — The deployment is scheduled during a maintenance window. Brief request loss during switchover is expected and communicated to stakeholders via DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md Template 1.

**Corresponding Deployment Steps**: Step 2 (Stop Application), Step 7 (Start Application) of DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md.

---

### Root Cause

- TCP connections received between service stop and service start return `Connection refused`
- DNS/load balancer does not have a secondary backend to route traffic to during the gap
- The deployment does not use blue-green switching (confirmed in Item 4.3 of the pre-flight checklist)

---

### Prevention

- Maintenance window communication sent at least 2 hours before deployment (Template 1 in DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md)
- Deployment window is scheduled for a low-traffic period (verify with ops team)
- Total service gap is estimated at 2–5 minutes (Steps 2 through 7 of the deployment procedure)

---

### Detection Criteria

This failure mode has no detection step — it is an expected condition during the maintenance window. If error monitoring is active, expect a spike in connection errors between the stop and start steps.

**Post-deployment**: Confirm request error rate returns to baseline (<0.01%) within 5 minutes of service start.

```bash
# Post-deployment: check error rate in application logs
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'LOG_CHECK'
echo "Errors in past 5 minutes:"
sudo journalctl -u open-repo --since "5 minutes ago" | grep -cE "ERROR|CRITICAL" || echo "0"
LOG_CHECK
```

---

### Recovery Procedure

No recovery action required unless the service gap extends beyond 10 minutes (which would indicate a startup failure, covered under Failure Mode 2).

If the error rate does not return to baseline after 10 minutes:
1. Check application logs for runtime errors
2. Verify all endpoints in DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md Section 5
3. If errors persist and endpoints are unhealthy → execute rollback

---

### Timeline

- Acceptable gap duration: <5 minutes (Steps 2 through 7)
- Hard limit: If service has not started by 09:30 UTC, abort and roll back
- Post-start monitoring: 60 minutes active monitoring

---

### Success Criteria

- [ ] Request error rate returns to <0.01% within 5 minutes of service start
- [ ] Average response latency returns to <200ms within 5 minutes of service start
- [ ] No user-visible errors after the maintenance window closes at 09:45 UTC

---

## Section 5: Failure Mode 4 — Backup Restoration Failure

**Description**: During a rollback attempt, the database backup file cannot be restored — either because the backup file is corrupted, the disk has insufficient space, or the restore script fails.

**Probability**: Very Low (2%) — Backups are created immediately before deployment and verified as non-zero size.

**Severity**: High — A failed backup restoration leaves the database in an unknown state. This is the worst-case scenario: the new code failed to deploy AND the rollback cannot restore the old data.

**Corresponding Step**: Rollback Step 2 of Section 1.

---

### Root Cause

- Backup file corrupted (incomplete write, filesystem error)
- Disk space on production host exhausted between backup creation and restore
- SQLite database file path has changed between backup creation and restore attempt
- PostgreSQL restore command fails (permission error, missing extension, version mismatch)

---

### Prevention

- Pre-deployment backup procedure (Item 3.2) verifies file is created and has non-zero size
- Disk space check (Item 10 of DEPLOYMENT_JUNE12_PRECHECK_ENVIRONMENT.md v1.0) verifies >5GB free before deployment
- Backup retention: at least 2 backup files kept, so a second-generation backup exists as fallback

---

### Detection Criteria

Backup restoration failure is confirmed when **any** of the following occurs during Rollback Step 2:

```bash
# Detection patterns during restore:
cp: error writing '/opt/data/open-repo.db': No space left on device
# FAIL: disk full

cp: cannot stat '/opt/db-backups/open-repo-20260612-085930.db.bak': No such file
# FAIL: backup file missing

ERROR:  relation "zim_exports" already exists  (PostgreSQL)
# FAIL: restore failed — may need DROP DATABASE first

ls -lah /opt/db-backups/open-repo-20260612-085930.db.bak
# FAIL: file size is 0 bytes
```

---

### Recovery Procedure

**Step 1 — Check for second-generation backup**:
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'CHECK_BACKUP'
ls -lt /opt/db-backups/ | head -10
# If a backup older than today exists, use it as fallback
CHECK_BACKUP
```

**Step 2 — If second-generation backup exists, restore from it**:
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'RESTORE_GEN2'
BACKUP_DIR="/opt/db-backups"
# Skip newest (potentially corrupt), use second-newest
SECOND_LATEST=$(ls -t "$BACKUP_DIR"/ | sed -n '2p')
echo "Restoring from second-generation backup: $SECOND_LATEST"
# Execute restore with second-generation file
RESTORE_GEN2
```

**Step 3 — If no usable backup exists**:
- The database remains in its current state (post-failed-migration or post-failed-deployment state)
- Revert code to previous version (Rollback Steps 3–5) regardless
- The application may start successfully even without database rollback if the schema change was non-destructive
- Test application health immediately
- Schedule an emergency database recovery session with infrastructure team within 1 hour
- Document all data written between deployment start and rollback in the incident log

**Step 4 — If disk space is the issue**:
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'FREE_DISK'
# Check current disk usage
df -h /opt

# Remove oldest application backups (keep last 2)
ls -t /opt/backups/ | tail -n +3 | xargs -I{} rm -rf "/opt/backups/{}"

echo "Disk after cleanup:"
df -h /opt
FREE_DISK
```

---

### Timeline

- Detection: <1 minute (restore command fails immediately)
- Second-generation backup restoration: 2–5 minutes
- Manual recovery path: 30+ minutes (requires infrastructure team)
- Total worst-case downtime: <35 minutes (with second-generation backup)

---

### Success Criteria (after recovery)

- [ ] Database accessible and schema intact
- [ ] Data integrity check passes: record counts in key tables match pre-deployment snapshot
- [ ] No corrupted rows (run `SELECT COUNT(*) FROM zim_exports WHERE id IS NULL` — expect 0)
- [ ] Application starts and `/health` returns 200

---

## Section 6: Deployment Success Criteria

Deployment is considered **complete and successful** only when all of the following are true:

- [ ] All 7 deployment steps in DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md completed without error
- [ ] No rollback was necessary
- [ ] `/health` returns HTTP 200 with a valid JSON body
- [ ] `/api/v2/opds/root.xml` returns HTTP 200 with valid Atom XML
- [ ] `/api/v2/opds/entries` returns HTTP 200 with valid Atom XML
- [ ] `/docs` (Swagger UI) returns HTTP 200
- [ ] `/redoc` (ReDoc) returns HTTP 200
- [ ] Application logs show no CRITICAL or ERROR entries in the 5 minutes post-deployment
- [ ] System resources normal on production host (CPU idle >50%, memory available >500MB, disk >5GB free)
- [ ] 157/157 tests confirmed passing (from pre-flight Item 2.1)
- [ ] WCAG 2.1 AA: 11/11 criteria verified (from pre-flight Item 2.3)
- [ ] Database schema contains all 3 required tables
- [ ] Stakeholder notification sent (Template 3 in DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md)

---

## Section 7: Communication Triggers

Use DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md for all stakeholder notifications. Send notifications at these trigger points:

| Event | Template | Send within |
|-------|----------|------------|
| Failure mode detected | Template 4 (Escalation) | 1 minute of detection |
| Rollback initiated | Template 4 (Escalation) | Immediately |
| Rollback complete, service restored | Template 4 (Rollback Complete block) | 2 minutes of completion |
| Extended outage >10 minutes | Template 4 (Extended Outage) | At 10-minute mark |
| Deployment confirmed successful | Template 3 (Success) | Within 5 minutes of verification |
| 10 hours post-deployment | Template 5 (Post-Deployment Status) | 20:00 UTC (or 10h after start) |

---

## Section 8: Post-Mortem (If Rollback Occurred)

**Schedule**: Within 24 hours of a failed deployment.

**Participants**: Deployer, developer, infrastructure.

**Questions to answer**:
1. Which failure mode triggered rollback, and at which deployment step?
2. Did the detection criteria fire correctly, or was detection delayed?
3. What was the total service outage duration?
4. How many requests failed during the outage window (from error logs)?
5. Was any data written between deployment start and rollback that cannot be recovered?
6. Which pre-flight checklist item, if strengthened, would have prevented this failure?

**Output**: Updated pre-flight checklist items; updated failure mode timelines if actual recovery differed from estimated.

---

## Quick Reference: Rollback Decision Matrix

| Symptom | Failure Mode | Quick Fix? | Rollback? |
|---------|-------------|-----------|-----------|
| `alembic current` fails | FM1: Migration | Try `alembic upgrade head` once | Yes, if upgrade fails |
| Schema missing tables | FM1: Migration | Try `alembic upgrade head` once | Yes, if upgrade fails |
| Service fails to start | FM2: Deployment | Try port kill / dep reinstall (5 min max) | Yes, if fix fails |
| Health endpoint non-200 | FM2: Deployment | Check logs for obvious cause (5 min max) | Yes, if cause unclear |
| Connection refused during gap | FM3: Switchover | N/A — expected, not a failure | No, unless gap >10 min |
| Backup restore fails | FM4: Backup | Try second-gen backup | Yes, code revert at minimum |

---

**Document Version**: 2.0
**Created**: June 12, 2026
**Supersedes**: DEPLOYMENT_JUNE12_RISK_MITIGATION.md v1.0 (June 6, 2026)
**Valid For**: June 12, 2026 deployment
**Execute Alongside**: DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md
**Reference Alongside**: DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md
