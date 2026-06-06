---
title: "Open-Repo June 12, 2026 Deployment Incident Response Playbook"
project: open-repo
phase: 5 (final production deployment)
document_type: incident-response-playbook
status: PRODUCTION READY
created: 2026-06-06
target_deployment_date: 2026-06-12 (09:00 UTC)
deployment_window: "09:00–10:45 UTC"
references:
  - DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md
  - POST_DEPLOYMENT_MONITORING_PLAN.md
---

# Deployment Incident Response Playbook — June 12, 2026

**Purpose**: This playbook governs incident response during the June 12 deployment window (09:00–10:45 UTC) and the 60-minute active monitoring period that follows. It covers cascade failures, rollback decisions, root-cause starting points, and pre-rollback verification.

**Primary audience**: The deployer executing the June 12 runbook. Assumes SSH access to production (100.70.184.84) but no deep code knowledge.

**Threshold source**: All alert thresholds are taken directly from POST_DEPLOYMENT_MONITORING_PLAN.md Section 2. Do not apply different numbers.

---

## Section 1: Cascade Failure Priority Matrix

A cascade failure is defined as two or more alert types firing simultaneously. When multiple alerts fire, the sequence below determines which condition to address first. The rationale: higher-tier conditions are either unrecoverable if ignored or invalidate the meaning of lower-tier metrics.

### Priority Tier Order (highest to lowest)

| Priority | Condition | Tier | Why It Leads |
|----------|-----------|------|-------------|
| 1 | Database connectivity lost | CRITICAL | All other metrics are meaningless if the database is down; endpoints will return 500 regardless of code health |
| 2 | Health endpoint non-200 or timeout | CRITICAL | Confirms application process is dead or hung; no other fixes are viable until the process is confirmed alive |
| 3 | Error rate >20% | CRITICAL | System-wide failure; any endpoint fix is ineffective at this scale |
| 4 | OPDS response time >5000ms | CRITICAL | OPDS is the primary user-facing function; sustained 5s+ indicates database query failure or process hang |
| 5 | CPU idle <20% sustained | CRITICAL | Runaway process is starving the application; endpoint fixes cannot succeed under resource exhaustion |
| 6 | Memory available <1GB | CRITICAL | OOM killer may terminate the process; any restart will fail again until memory is freed |
| 7 | Error rate 10–20% | CRITICAL | Widespread but not total failure; investigate while preparing rollback |
| 8 | Response time >2000ms on /health or /docs | WARN→CRITICAL | Performance degradation; may be temporary or may be precursor to full failure |
| 9 | Disk available <5GB | CRITICAL | May block log writes and crash the process; but service may remain running momentarily |
| 10 | Error rate 5–10% | WARN | Significant but not fatal; investigate before preparing rollback |

**Rule**: Address the highest-priority firing condition first. Do not split attention across conditions simultaneously unless you have a second operator available.

---

## Section 2: Scenario Decision Trees

Each decision tree represents a testable scenario with concrete conditions and branching logic. All threshold values match POST_DEPLOYMENT_MONITORING_PLAN.md Section 2.

---

### Scenario A: Cascade — Response Time + Error Rate + CPU Exhaustion

**Trigger conditions firing simultaneously**:
- Health endpoint response time: 5000ms (threshold: OPDS >5000ms = CRITICAL; /health >2000ms = CRITICAL)
- Error rate: 15% (threshold: 10–20% = CRITICAL)
- CPU idle: 5% (threshold: <20% = CRITICAL)

**Decision tree**:

```
STEP 1: Is database reachable?
  Run: ssh ubuntu@100.70.184.84 'sudo journalctl -u open-repo --since "2 min ago" | grep -i "database\|connect"'
  │
  ├─ YES (no database errors in logs)
  │    STEP 2: Is a runaway process consuming CPU?
  │      Run: ssh ubuntu@100.70.184.84 'ps aux --sort=-%cpu | head -5'
  │      │
  │      ├─ YES (single process >80% CPU)
  │      │    → Identify the process PID from ps output
  │      │    → If it is NOT open-repo: kill it, re-check CPU idle, re-test endpoints
  │      │    → If it IS open-repo: the application has a runaway loop
  │      │         → Do not attempt restart yet; go to STEP 3
  │      │
  │      └─ NO (CPU spread across processes, none >50%)
  │           → The slow response is not CPU-caused; proceed to STEP 3
  │
  └─ NO (database connection errors present)
       → Priority: Database (Tier 1)
       → See Scenario D (database failure tree)
       → Do not investigate response time or error rate until DB is resolved

STEP 3: Has the application process crashed or is it still running?
  Run: ssh ubuntu@100.70.184.84 'sudo systemctl is-active open-repo'
  │
  ├─ active → Process is running but degraded
  │    STEP 4: Attempt service restart (only if rollback decision clock <3 min remaining)
  │      Run: ssh ubuntu@100.70.184.84 'sudo systemctl restart open-repo && sleep 5 && sudo systemctl is-active open-repo'
  │      │
  │      ├─ Returns "active" → Re-test all endpoints immediately
  │      │    If endpoints recover: CONTINUE MONITORING, document restart
  │      │    If endpoints do not recover within 2 min: EXECUTE ROLLBACK
  │      │
  │      └─ Returns "failed" → EXECUTE ROLLBACK immediately
  │
  └─ inactive / failed → Process is dead
       → EXECUTE ROLLBACK immediately
       → Do not attempt restart; the new code has a startup failure

DECISION SUMMARY for this scenario:
- If CPU runaway from non-app process: kill process → re-test → monitor
- If database down: go to Scenario D
- If app process failed: rollback
- If app running but degraded: one restart attempt → rollback if no recovery in 2 min
```

---

### Scenario B: OPDS Endpoints Failing + Health Endpoint Healthy

**Trigger conditions firing simultaneously**:
- Health endpoint: HTTP 200, <200ms (OK)
- OPDS /api/v2/opds/root.xml: HTTP 500 or response time >5000ms (CRITICAL)
- Error rate: 12% (CRITICAL)

**Decision tree**:

```
STEP 1: Confirm health endpoint is actually OK (not a false positive)
  Run: curl -s -w "HTTP %{http_code} Time: %{time_total}s\n" http://100.70.184.84:8000/health
  │
  ├─ HTTP 200, <200ms → Health is genuinely fine; the issue is OPDS-specific
  │
  └─ HTTP 200 but >500ms → Degraded; treat as combined response time issue (Scenario A)

STEP 2: What does the 500 error say?
  Run: ssh ubuntu@100.70.184.84 'sudo journalctl -u open-repo --since "5 min ago" | grep -i "opds\|500\|error" | tail -20'
  │
  ├─ "OPDS initialization failed" or "OPDSGenerator error"
  │    → Database table missing or migration incomplete (likely Alembic issue)
  │    → Check: ssh ubuntu@100.70.184.84 'cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend && source /opt/venv/open-repo/bin/activate && alembic current'
  │         If revision ≠ head: migration did not apply → EXECUTE ROLLBACK
  │         If revision = head: OPDS generator code error, not a migration issue
  │              → Document for post-incident; decide: is OPDS critical to June 12 deployment purpose?
  │                   YES → EXECUTE ROLLBACK
  │                   NO (OPDS is secondary for this release) → continue with PARTIAL SUCCESS state, document
  │
  ├─ "database connection failed" or "timeout"
  │    → Go to Scenario D (database failure tree)
  │
  └─ "ZIM export table not found" or "relation does not exist"
       → Schema mismatch; migration gap
       → EXECUTE ROLLBACK

DECISION SUMMARY:
- OPDS 500 with DB errors → Scenario D first
- OPDS 500 with OPDSGenerator errors → assess criticality → rollback if OPDS is required
- OPDS 500 with schema errors → rollback
```

---

### Scenario C: Memory Exhaustion + Degraded Response Times

**Trigger conditions firing simultaneously**:
- Memory available: 800MB (threshold: <1GB = CRITICAL)
- Health endpoint response time: 1200ms (threshold: 500–2000ms = WARN toward CRITICAL)
- Error rate: 3% (threshold: 1–5% = WARN)

**Decision tree**:

```
STEP 1: Identify what is consuming memory
  Run: ssh ubuntu@100.70.184.84 'ps aux --sort=-%mem | head -6'
  │
  ├─ open-repo process consuming >50% memory
  │    → Likely memory leak introduced by new code
  │    → Check how long the service has been running:
  │         ssh ubuntu@100.70.184.84 'sudo systemctl status open-repo | grep "Active:"'
  │    ├─ Running <30 min: memory growth rate is high, likely a startup leak
  │    │    → EXECUTE ROLLBACK; memory will exhaust and crash within active monitoring window
  │    └─ Running >30 min with stable memory: may be one-time allocation, not a leak
  │         → Continue monitoring for 10 more minutes; if memory continues dropping, rollback
  │
  └─ Other process consuming memory (not open-repo)
       → Identify process and assess: is it a known background process?
       ├─ YES (e.g., system update, log rotation): Wait for it to complete; re-check memory
       └─ NO (unknown process): Kill it, re-test

STEP 2: Is OOM killer risk imminent?
  Run: ssh ubuntu@100.70.184.84 'free -m | grep Mem'
  │
  ├─ Available memory dropping below 500MB → Imminent OOM risk
  │    → EXECUTE ROLLBACK before OOM killer fires (OOM kill leaves corrupted state)
  │
  └─ Memory stable between 800MB–1GB → WARN state; not yet CRITICAL
       → Monitor every 2 minutes; set 10-minute escalation timer
       → If does not recover above 1GB in 10 min → EXECUTE ROLLBACK

DECISION SUMMARY:
- Open-repo memory leak + <1GB available → rollback
- Unknown process eating memory + open-repo stable → kill process, re-monitor
- Stable at 800MB–1GB → 10-minute monitoring window before rollback decision
```

---

### Scenario D: Database Connectivity Loss

**Trigger conditions firing simultaneously**:
- Database connection errors in logs (any count)
- OPDS endpoints: HTTP 500
- Health endpoint: HTTP 500 or degraded

**Decision tree**:

```
STEP 1: Is the database process running (if local/SQLite)?
  Run: ssh ubuntu@100.70.184.84 'ls -lah /opt/db-backups/ | head -5'  # Verify backup exists before anything else
  Run: ssh ubuntu@100.70.184.84 'ls -lah /path/to/database.db'  # SQLite file check

  If PostgreSQL:
  Run: ssh ubuntu@100.70.184.84 'sudo systemctl is-active postgresql || sudo systemctl is-active postgres'
  │
  ├─ Database process not running (PostgreSQL stopped)
  │    → Attempt restart: ssh ubuntu@100.70.184.84 'sudo systemctl start postgresql'
  │    → Re-test: ssh ubuntu@100.70.184.84 'sudo systemctl is-active postgresql'
  │    ├─ Restarts OK: re-test application endpoints; if healthy → CONTINUE MONITORING
  │    └─ Will not start: EXECUTE ROLLBACK (database-level failure is not fixable in 5-min window)
  │
  └─ Database process is running (connection issue is not a stopped process)
       STEP 2: Is it a migration lock?
         Run: ssh ubuntu@100.70.184.84 'sudo journalctl -u open-repo --since "5 min ago" | grep -i "lock\|deadlock\|transaction"'
         │
         ├─ Lock/deadlock messages present
         │    → The Alembic migration has locked a table and not released it
         │    → Do NOT restart the service immediately (restart will not release the lock)
         │    → Check current migration state: alembic current
         │    → If migration is in-progress: wait 2 minutes; if not resolving → EXECUTE ROLLBACK
         │         Rollback will require: alembic downgrade -1 (see Section 4, Step 2)
         │
         └─ No lock messages; general connection failure
              → Network or credentials issue
              → EXECUTE ROLLBACK (cannot diagnose credentials in deployment window)

DECISION SUMMARY:
- DB process stopped: attempt restart once → rollback if fails
- DB lock from migration: wait 2 min → rollback
- DB connection failure (network/credentials): rollback
- ALWAYS verify backup exists before any rollback action
```

---

### Scenario E: Partial Deployment State (New Code Deployed, Migration Not Applied)

**Indicators**:
- Application starts and /health returns 200
- OPDS endpoints return 500 with "column does not exist" or "relation does not exist" errors
- `alembic current` shows old revision, not head

**Decision tree**:

```
STEP 1: Confirm the diagnosis
  Run: ssh ubuntu@100.70.184.84 'cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend && source /opt/venv/open-repo/bin/activate && alembic current 2>&1'
  │
  ├─ Output shows old revision (not head)
  │    → Migration was not applied during deployment Step 6
  │    → Assess: how many migrations are pending?
  │         alembic history | head -10
  │    ├─ 1 migration pending, simple schema change (add column, index)
  │    │    → Attempt forward migration: alembic upgrade head
  │    │    → Run within 3-minute window; if completes cleanly → re-test endpoints
  │    │    → If migration fails: EXECUTE ROLLBACK using alembic downgrade -1 first (see Section 4)
  │    └─ Multiple migrations pending, or migration involves destructive changes (drop column, rename)
  │         → Do not attempt forward migration during incident window
  │         → EXECUTE ROLLBACK
  │
  └─ Output shows head revision
       → Migration is current; the 500 error is a code bug, not a schema mismatch
       → Document the specific error; assess: is it OPDS-only or all endpoints?
            OPDS-only: see Scenario B
            All endpoints: EXECUTE ROLLBACK

DECISION SUMMARY:
- Migration not applied, simple change → attempt upgrade, rollback if fails
- Migration not applied, complex change → rollback
- Migration applied but still 500 → code bug → assess impact → likely rollback
```

---

## Section 3: Rollback Procedures with Data Integrity Preservation

All rollback steps are reversible. No step permanently destroys data. The backup created in deployment Step 3 (at `/opt/backups/open-repo-YYYYMMDD-HHMMSS`) is the recovery target.

### Pre-Rollback Checklist (Run Before Any Rollback Action)

Complete all four checks before executing rollback. If any check fails, note the failure and proceed — do not let a failed check block a necessary rollback, but document it for the post-incident audit.

```bash
# CHECK 1: Confirm backup exists and is readable
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
echo "=== PRE-ROLLBACK CHECK 1: Backup verification ==="
LATEST_BACKUP=$(ls -t /opt/backups/ | head -1)
if [ -z "$LATEST_BACKUP" ]; then
  echo "WARN: No backup found in /opt/backups — rollback will use git revert only"
else
  echo "Backup found: /opt/backups/$LATEST_BACKUP"
  du -sh "/opt/backups/$LATEST_BACKUP"
fi

# CHECK 2: Record current git state
echo ""
echo "=== PRE-ROLLBACK CHECK 2: Current git state ==="
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
git log --oneline -3
echo "Current HEAD: $(git rev-parse HEAD)"

# CHECK 3: Check for active database transactions
echo ""
echo "=== PRE-ROLLBACK CHECK 3: Active transactions ==="
sudo journalctl -u open-repo --since "2 min ago" | grep -i "transaction\|BEGIN\|COMMIT\|ROLLBACK" | tail -5 || echo "No active transaction log entries"

# CHECK 4: Confirm database backup (pre-deployment)
echo ""
echo "=== PRE-ROLLBACK CHECK 4: Database backup ==="
ls -lah /opt/db-backups/ 2>/dev/null | head -5 || echo "No database backups found in /opt/db-backups"
EOF
```

Record the output. If no backup exists, the rollback path is git-only (see Step 2 below, git-only path).

---

### Step 1: Stop the Current Application

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
echo "=== ROLLBACK STEP 1: Stop application ==="
sudo systemctl stop open-repo
sleep 3
sudo systemctl is-active open-repo && echo "WARN: Still running" || echo "Stopped"
EOF
```

**Expected**: "Stopped". If still running after 3 seconds: `sudo systemctl kill -9 open-repo`

---

### Step 2: Abort Alembic Migration (If Migration Was In-Progress or Partially Applied)

Only run this step if deployment Step 6 ran and the migration may be partially applied. If migration was never attempted, skip to Step 3.

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
echo "=== ROLLBACK STEP 2: Revert database migration ==="
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
source /opt/venv/open-repo/bin/activate

# Show current state
echo "Current migration state:"
alembic current 2>&1

# Downgrade one step (reverses the most recent migration only)
echo ""
echo "Downgrading one migration step..."
alembic downgrade -1

if [ $? -eq 0 ]; then
  echo "Migration downgrade successful"
  echo "Post-downgrade state:"
  alembic current 2>&1
else
  echo "WARN: Migration downgrade failed"
  echo "Manual intervention may be required"
  echo "Check: alembic history for what was applied"
fi
EOF
```

**If downgrade fails**: Do not force it. Proceed to Step 3 (restore from backup). The database backup from pre-deployment will have the correct schema state.

**Data integrity note**: `alembic downgrade -1` is designed to be reversible. It runs the `downgrade()` function defined in the migration script. If the migration added a column, downgrade removes it. Existing row data in other columns is preserved.

---

### Step 3: Restore Previous Code from Backup or Git Revert

**Path A: Restore from filesystem backup** (preferred if backup exists)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
echo "=== ROLLBACK STEP 3A: Restore from filesystem backup ==="

LATEST_BACKUP=$(ls -t /opt/backups/ | head -1)
DEPLOY_DIR="/home/awank/dev/SuperClaude_Framework/projects/open-repo"

echo "Backup to restore: /opt/backups/$LATEST_BACKUP"
echo "Deploy directory: $DEPLOY_DIR"

# Rename current (failed) deployment as evidence
mv "$DEPLOY_DIR" "${DEPLOY_DIR}-failed-$(date +%H%M%S)"
echo "Moved failed deployment to: ${DEPLOY_DIR}-failed-$(date +%H%M%S)"

# Restore backup
cp -r "/opt/backups/$LATEST_BACKUP" "$DEPLOY_DIR"
echo "Restored from backup"

# Verify
git -C "$DEPLOY_DIR" log --oneline -1
EOF
```

**Path B: Revert via git** (use only if no filesystem backup exists)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
echo "=== ROLLBACK STEP 3B: Git revert to previous commit ==="
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

# Show the commit that was deployed and the one before it
echo "Currently deployed:"
git log --oneline -3

PREV_COMMIT=$(git log --oneline -2 | tail -1 | awk '{print $1}')
echo "Reverting to: $PREV_COMMIT"

# Reset hard to previous commit
git reset --hard "$PREV_COMMIT"

echo "Post-revert state:"
git log --oneline -1
EOF
```

**Reversibility**: Path A is fully reversible (the failed deployment is preserved with a timestamp suffix). Path B uses `git reset --hard` which does discard local changes, but since all production changes go through the repository, no work is lost.

---

### Step 4: Restore Database Snapshot (If Migration Caused Data Corruption)

Only execute this step if there is evidence of data corruption (e.g., duplicate rows, constraint violations, missing data in application logs). If the migration was a clean schema change with no data manipulation, skip this step.

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
echo "=== ROLLBACK STEP 4: Restore database snapshot ==="

BACKUP_DIR="/opt/db-backups"
LATEST_DB_BACKUP=$(ls -t "$BACKUP_DIR"/*.db.bak 2>/dev/null | head -1)

if [ -z "$LATEST_DB_BACKUP" ]; then
  echo "ERROR: No database backup found. Cannot restore database."
  echo "If migration caused corruption, manual intervention is required."
  exit 1
fi

echo "Restoring database from: $LATEST_DB_BACKUP"

# For SQLite: backup current (corrupted) database first, then restore
cp /path/to/database.db "/path/to/database.db.corrupted-$(date +%H%M%S)"
cp "$LATEST_DB_BACKUP" /path/to/database.db
echo "Database restored."
ls -lah /path/to/database.db
EOF
```

**PostgreSQL variant** (if using PostgreSQL instead of SQLite):
```bash
# Stop app first (done in Step 1)
# Restore from pg_dump backup:
LATEST_BACKUP=$(ls -t /opt/db-backups/*.sql.gz | head -1)
gunzip -c "$LATEST_BACKUP" | psql [connection-string]
```

---

### Step 5: Restart Application on Previous Version

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
echo "=== ROLLBACK STEP 5: Start previous version ==="
sudo systemctl start open-repo
sleep 5

if sudo systemctl is-active --quiet open-repo; then
  echo "Service started"
else
  echo "ERROR: Service will not start on previous version"
  sudo journalctl -u open-repo -n 30
  exit 1
fi

echo "Re-running health check..."
EOF

# Health check from local machine
curl -s -w "HTTP %{http_code} Time: %{time_total}s\n" http://100.70.184.84:8000/health
```

---

### Step 6: Post-Rollback Verification

Run the same health checks as post-deployment verification. All endpoints must return HTTP 200 before declaring rollback complete.

```bash
# Run all endpoint checks
for ENDPOINT in "/health" "/docs" "/redoc" "/api/v2/opds/root.xml"; do
  CODE=$(curl -s -o /dev/null -w "%{http_code}" "http://100.70.184.84:8000${ENDPOINT}")
  echo "$ENDPOINT: HTTP $CODE"
done
```

Expected: all return 200. If any return non-200, escalate to manual intervention — do not attempt another rollback cycle without investigation.

---

## Section 4: Root Cause Investigation Starting Points

Use these in parallel with the decision trees above. Investigation starting points are ordered from most likely to least likely cause for a June 12 Phase 5 A11y deployment.

### Starting Point 1: Docker / Systemd Application Logs

The first 50 lines of recent logs will identify 80% of startup failures.

```bash
# Immediate: last 50 lines
ssh ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 50'

# Filter for errors only
ssh ubuntu@100.70.184.84 'sudo journalctl -u open-repo --since "09:00" | grep -E "ERROR|CRITICAL|Exception|Traceback" | head -20'

# Full startup sequence (from service start)
ssh ubuntu@100.70.184.84 'sudo journalctl -u open-repo --since "$(sudo systemctl status open-repo | grep "Active:" | grep -oP "\w{3} \d+ \d+:\d+:\d+")" | head -100'
```

**Look for**: Python traceback, import errors, database connection refused, port binding errors.

### Starting Point 2: Alembic Migration SQL

If migration Step 6 ran, check what SQL it generated and whether it completed.

```bash
ssh ubuntu@100.70.184.84 << 'EOF'
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
source /opt/venv/open-repo/bin/activate

# What is the current migration state?
alembic current 2>&1

# Show migration history
alembic history 2>&1

# Show the actual SQL that was (or would be) applied — for inspection only, do not run upgrade
alembic upgrade head --sql 2>&1 | head -50
EOF
```

**Look for**: Failed SQL statements, constraint violations, "relation already exists", "column does not exist".

### Starting Point 3: Database Constraints and Schema State

```bash
# For SQLite — inspect schema directly
ssh ubuntu@100.70.184.84 'sqlite3 /path/to/database.db ".schema" 2>/dev/null | head -50'

# Check for any constraint violations in logs
ssh ubuntu@100.70.184.84 'sudo journalctl -u open-repo --since "09:00" | grep -i "constraint\|unique\|foreign key\|integrity" | head -10'

# For PostgreSQL — check what tables exist post-migration
# ssh ubuntu@100.70.184.84 'PGPASSWORD=$DB_PASS psql -h localhost -U $DB_USER -d $DB_NAME -c "\dt"'
```

**Look for**: Missing tables the OPDS generator expects, extra tables from partial migration, constraint violation errors.

### Starting Point 4: Health Endpoint Code Path

The `/health` endpoint is the simplest code path. If it returns 500, the failure is at application startup or core initialization, not feature-specific code.

```bash
# Check if the health endpoint is even registered
ssh ubuntu@100.70.184.84 'sudo journalctl -u open-repo --since "09:00" | grep -i "health\|startup complete\|application ready" | head -10'

# Check the app startup sequence specifically
ssh ubuntu@100.70.184.84 'sudo journalctl -u open-repo --since "09:00" | head -30'
```

**Look for**: "Application startup complete" missing from logs (means startup crashed), "uvicorn running" not appearing (means the process exited immediately).

### Starting Point 5: Resource Exhaustion Root Cause

```bash
ssh ubuntu@100.70.184.84 << 'EOF'
# CPU, memory, disk snapshot
echo "=== Resource Snapshot at $(date -u +%H:%M:%S UTC) ==="
echo "CPU:"
top -bn1 | grep "Cpu(s)"
echo "Memory:"
free -h
echo "Disk:"
df -h /
echo "Top processes:"
ps aux --sort=-%cpu | head -8
echo "OOM killer activity (recent):"
sudo dmesg | grep -i "oom\|killed" | tail -5 || echo "None"
EOF
```

**Look for**: OOM killer events in dmesg (confirms memory exhaustion already caused a kill), disk at 100% (causes log write failures that look like app errors), known background processes (apt-get, systemd-journal vacuum).

---

## Section 5: Escalation — When to Stop and Ask

Do not force a decision if:

1. Rollback appears to be failing (Step 5 service does not start on previous version)
2. Database snapshot restore fails and corruption is suspected
3. The same CRITICAL alert fires again within 5 minutes after a restart
4. Alembic downgrade fails with an error (not just a warning)
5. You are unsure whether data has been modified in a way that backup restore would lose writes

In any of these cases: stop, preserve the current state (do not run further commands), and document exactly what commands were run and what outputs were received. The post-incident audit (DEPLOYMENT_POST_INCIDENT_AUDIT_CHECKLIST.md) is designed for this handoff.

**Escalation contact**: Team lead / repo owner. Share the output of the pre-rollback check and the most recent 100 log lines.

---

## Section 6: Quick Reference — Incident Severity Classification

| Symptom | Severity | Response Time | Action |
|---------|----------|---------------|--------|
| /health returns 200 but slow (200–500ms) | WARN | 5 min | Monitor; check DB latency |
| /health returns 200 but very slow (500–2000ms) | WARN→CRITICAL | 3 min | Investigate; prepare rollback |
| /health timeout or non-200 | CRITICAL | 2 min | Service restart → rollback |
| OPDS 500 error | CRITICAL | 3 min | Check migration → rollback |
| Error rate 5–10% | WARN | 5 min | Investigate logs |
| Error rate >10% | CRITICAL | 2 min | Prepare rollback |
| Error rate >20% | CRITICAL | Immediate | Rollback |
| CPU idle <20% for >5 min | CRITICAL | 3 min | Find runaway process |
| Memory available <1GB | CRITICAL | 3 min | Check open-repo memory |
| Memory available <500MB | CRITICAL | Immediate | Rollback before OOM |
| Disk available <5GB | CRITICAL | 5 min | Check log growth |
| Database connection error | CRITICAL | 2 min | Check DB process → rollback |
| 2+ CRITICAL alerts simultaneously | CASCADE | Immediate | Follow priority matrix (Section 1) |

---

**Playbook Version**: 1.0
**Created**: June 6, 2026
**Valid For**: June 12, 2026 deployment window (09:00–10:45 UTC)
**References**: DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md, POST_DEPLOYMENT_MONITORING_PLAN.md
