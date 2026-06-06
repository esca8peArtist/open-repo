---
title: "Open-Repo June 12, 2026 Deployment Incident Response Playbook"
project: open-repo
phase: 5 (final production deployment)
document_type: incident-response-playbook
status: PRODUCTION READY
created: 2026-06-06
target_deployment_date: 2026-06-12 (09:00 UTC)
---

# Deployment Incident Response Playbook

**Deployment Date**: June 12, 2026  
**Deployment Window**: 09:00–10:45 UTC (105 minutes total: 45 min deployment + 60 min active monitoring)  
**Purpose**: Define decision procedures for cascade failures, data corruption, and partial deployment states during June 12 deployment  
**Audience**: On-call engineer, incident commander, database team, operations team

---

## Overview: When to Use This Playbook

This playbook activates when **ANY** of these conditions occur:

1. **Multiple simultaneous alerts** (cascade failure): 2+ alert types firing at the same time
2. **Health check failures**: `/health` endpoint returns 500 or timeout
3. **Critical endpoint failures**: /docs, /redoc, or OPDS endpoints all returning 500+
4. **Data integrity concerns**: Database errors detected (constraint violations, failed migrations)
5. **Partial deployment state**: Service starts but some subsystems don't
6. **Monitoring infrastructure fails**: Cannot observe system status

**Response Time**: Must decide within 5 minutes whether to fix or rollback

---

## Section 1: Cascade Failure Priority Matrix

When 2+ alert types fire simultaneously, use this matrix to establish response priority.

### Alert Type Definitions

| Alert Type | Triggered When | Severity | Time to Decision |
|-----------|----------------|----------|------------------|
| **Response Time Critical** | Any endpoint >5000ms OR timeout | CRITICAL | 2 min |
| **Error Rate Critical** | >20% requests returning 5XX | CRITICAL | 2 min |
| **Health Endpoint Failure** | /health returns non-200 or times out | CRITICAL | 2 min |
| **Database Connectivity** | Database connection errors in logs | CRITICAL | 3 min |
| **Resource Exhaustion** | CPU idle <20% OR memory <1GB OR disk <5GB | CRITICAL | 3 min |
| **OPDS-Specific Failure** | Both root.xml and entries endpoints 500+ | CRITICAL | 2 min |

### Priority Matrix: Response Order When Multiple Alerts Fire

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CASCADE FAILURE PRIORITY MATRIX                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  PRIORITY 1 (Handle First):  Health Endpoint Failure                    │
│  ──────────────────────────────────────────────────────────────────    │
│  Why: If health check is down, entire system is unreachable             │
│  Action: Check application process (is it running?)                     │
│  Timeline: Diagnose within 1 minute, decide within 2 minutes            │
│  Next: If health check still failing, go to ROLLBACK DECISION          │
│                                                                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  PRIORITY 2 (Handle Second): Database Connectivity                      │
│  ───────────────────────────────────────────────────────────────────   │
│  Why: If database is down, all endpoints will fail                      │
│  Action: Verify database is reachable and responding                    │
│  Timeline: Diagnose within 2 minutes                                    │
│  Decision: If DB is down and you can't restart it, ROLLBACK             │
│           (data corruption risk if you force restart)                    │
│                                                                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  PRIORITY 3 (Handle Third): Error Rate Critical                         │
│  ───────────────────────────────────────────────────────────────────   │
│  Why: Indicates widespread failure across endpoints                     │
│  Action: Identify which endpoint category is failing (OPDS vs. Docs)   │
│  Timeline: Diagnose within 2 minutes                                    │
│  Decision: If >20% errors, attempt restart; if persists >3 min,        │
│           ROLLBACK                                                        │
│                                                                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  PRIORITY 4 (Handle Fourth): Response Time Critical                     │
│  ──────────────────────────────────────────────────────────────────    │
│  Why: May indicate database query slowness or resource contention      │
│  Action: Check system resources AND database query logs                 │
│  Timeline: Diagnose within 3 minutes                                    │
│  Decision: If resource-constrained, may need to optimize or rollback   │
│                                                                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  PRIORITY 5 (Handle Fifth): Resource Exhaustion                         │
│  ───────────────────────────────────────────────────────────────────   │
│  Why: System running out of CPU/memory/disk affects all operations     │
│  Action: Identify which resource is exhausted                          │
│  Timeline: Diagnose within 3 minutes                                    │
│  Decision: Attempt to free up resource; if cannot, ROLLBACK             │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### Response Order Algorithm

When multiple alerts fire:

```
1. Sort all firing alerts by priority (Health → DB → Error Rate → Response → Resources)
2. Handle Priority 1 alerts first (usually 1–2 alerts)
3. Once Priority 1 handled, move to Priority 2
4. If any alert in higher priority is not resolved in 2–3 minutes, escalate to ROLLBACK DECISION
5. If multiple priority 1 alerts firing (health + database), execute ROLLBACK immediately
   (indicates systemic failure, not localized issue)
```

**Key Rule**: Do not attempt to fix a lower-priority issue if a higher-priority issue exists. Address in order.

---

## Section 2: Five Critical Scenario Decision Trees

Use these decision trees during deployment to determine: diagnose → decide → act.

---

### Scenario 1: Response Time CRITICAL + Error Rate CRITICAL (Simultaneous)

**Conditions**: 
- Response time threshold breached (>5000ms on any endpoint)
- Error rate threshold breached (>20% of requests returning 5XX)
- Both detected within 1 minute of each other

**Decision Tree**:

```
SCENARIO 1 STARTS: Response time CRITICAL + Error rate CRITICAL
│
├─ Step 1: Check if application is running
│  │
│  ├─ YES, process is running
│  │  │
│  │  └─ Step 2: Check application crash logs
│  │     │
│  │     ├─ Crashes detected in logs (CRITICAL)
│  │     │  └─ GO TO: ROLLBACK DECISION (application is broken)
│  │     │
│  │     └─ No crashes in logs, but high errors
│  │        │
│  │        └─ Step 3: Is it database issue?
│  │           │
│  │           ├─ YES (database connection errors in logs)
│  │           │  └─ GO TO: DATABASE RECOVERY PROCEDURE
│  │           │
│  │           └─ NO (application is trying to respond)
│  │              │
│  │              └─ Step 4: Attempt graceful restart
│  │                 │
│  │                 ├─ Restart succeeds, errors drop below 5%
│  │                 │  └─ GO TO: CONTINUE MONITORING
│  │                 │
│  │                 └─ Restart fails or errors persist >3 min
│  │                    └─ GO TO: ROLLBACK DECISION
│  │
│  └─ NO, application is not running
│     │
│     ├─ Step 2: Why is it not running?
│     │  │
│     │  ├─ Service exited cleanly (exit code 0)
│     │  │  └─ GO TO: ROLLBACK DECISION (deployment introduced shutdown bug)
│     │  │
│     │  └─ Service crashed (non-zero exit code)
│     │     └─ Check logs for reason
│     │        │
│     │        ├─ Memory/disk error → GO TO: ROLLBACK DECISION
│     │        ├─ Database error → GO TO: DATABASE RECOVERY PROCEDURE
│     │        └─ Other → GO TO: ROLLBACK DECISION (code is broken)
│     │
│     └─ Step 3: Attempt to restart application
│        │
│        ├─ Restart succeeds, errors resolve
│        │  └─ GO TO: CONTINUE MONITORING
│        │
│        └─ Restart fails or errors persist
│           └─ GO TO: ROLLBACK DECISION
│
└─ OUTCOME: Either CONTINUE MONITORING or ROLLBACK DECISION

DECISION TIMELINE: 5 minutes max (2 min diagnose + 3 min attempt fix or decide)
```

**Diagnosis Commands**:
```bash
# 1. Is application running?
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo systemctl is-active open-repo'

# 2. Check crash logs
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 50'

# 3. Check for database errors
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  'sudo journalctl -u open-repo --since "5 minutes ago" | grep -i "database\|connection" | head -5'

# 4. Attempt restart
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo systemctl restart open-repo'
sleep 5

# 5. Re-check error rate
curl -s http://100.70.184.84:8000/health
```

---

### Scenario 2: Health Check PASS but OPDS Endpoints FAIL

**Conditions**:
- `/health` endpoint returns 200 OK (application appears healthy)
- `/api/v2/opds/root.xml` returns 500 or times out
- `/api/v2/opds/entries` returns 500 or times out
- Swagger UI (`/docs`) and ReDoc (`/redoc`) return 200 OK

**Interpretation**: Application started fine, but OPDS-specific code has a bug or dependency issue

**Decision Tree**:

```
SCENARIO 2 STARTS: Health OK but OPDS endpoints failing
│
├─ Step 1: Is it a database issue specific to OPDS table?
│  │
│  ├─ Check if OPDS tables exist and have data
│  │  │
│  │  ├─ Tables missing or empty (CRITICAL)
│  │  │  └─ GO TO: DATABASE RECOVERY PROCEDURE
│  │  │  (Database migration failed or data not present)
│  │  │
│  │  └─ Tables exist and have data
│  │     │
│  │     └─ Step 2: Check OPDS endpoint logs for errors
│  │        │
│  │        ├─ Constraint violation errors (CRITICAL)
│  │        │  └─ GO TO: DATABASE RECOVERY PROCEDURE
│  │        │
│  │        └─ Code/import errors in OPDS generator
│  │           │
│  │           └─ Step 3: Was OPDS code changed in this deployment?
│  │              │
│  │              ├─ YES (OPDS code was modified)
│  │              │  └─ GO TO: ROLLBACK DECISION (code change broke OPDS)
│  │              │
│  │              └─ NO (OPDS code unchanged, only A11y changes)
│  │                 │
│  │                 └─ Step 4: Try clearing OPDS cache (if applicable)
│  │                    │
│  │                    ├─ Cache clear succeeds, endpoints recover
│  │                    │  └─ GO TO: CONTINUE MONITORING
│  │                    │
│  │                    └─ Cache clear fails or endpoints still fail
│  │                       └─ GO TO: ROLLBACK DECISION
│  │                       (Partial deployment state cannot be recovered)
│  │
│  └─ If cannot determine database state
│     └─ GO TO: ROLLBACK DECISION (fail-safe: unknown state)
│
└─ OUTCOME: CONTINUE MONITORING or ROLLBACK DECISION

DECISION TIMELINE: 4 minutes max (2 min diagnose + 2 min attempt fix or decide)
DECISION LOGIC: If OPDS code unchanged, this is likely a data issue → investigate DB first.
                If OPDS code was changed, this is a code bug → rollback.
```

**Diagnosis Commands**:
```bash
# 1. Check OPDS endpoint error details
curl -s -H "Accept: application/atom+xml" http://100.70.184.84:8000/api/v2/opds/root.xml 2>&1 | head -20

# 2. Check database tables exist
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
# For SQLite:
sqlite3 /path/to/database.db "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%opds%' OR name LIKE '%zim%';"

# For PostgreSQL:
psql $DATABASE_URL -c "\dt *opds* OR *zim*"
EOF

# 3. Check OPDS-specific errors in logs
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  'sudo journalctl -u open-repo --since "10 minutes ago" | grep -i "opds\|atom\|feed" | tail -10'

# 4. Check recent code changes (if applicable)
git log --oneline -5 | grep -i "opds"
```

---

### Scenario 3: Database Migration Succeeds but Constraints Violated

**Conditions**:
- Deployment Step 6 (Database Migrations) reported success
- Application starts without errors
- Endpoints return 200 OK but with partial/incorrect data
- Database logs show constraint violations or integrity warnings

**Interpretation**: Migration script ran, but resulted in invalid data state

**Decision Tree**:

```
SCENARIO 3 STARTS: Migration succeeded but constraints violated
│
├─ Step 1: Determine severity of constraint violation
│  │
│  ├─ Critical (foreign key, unique constraint):
│  │  │
│  │  └─ Step 2: Can violation be fixed without data loss?
│  │     │
│  │     ├─ YES (simple fix, e.g., update orphaned rows)
│  │     │  │
│  │     │  └─ Step 3: Attempt fix
│  │     │     │
│  │     │     ├─ Fix succeeds, data is valid
│  │     │     │  └─ GO TO: CONTINUE MONITORING
│  │     │     │
│  │     │     └─ Fix fails or introduces new errors
│  │     │        └─ GO TO: ROLLBACK DECISION (data state unknown)
│  │     │
│  │     └─ NO (cannot fix without manual intervention)
│  │        └─ GO TO: ROLLBACK DECISION (data is corrupted)
│  │
│  └─ Non-critical (check constraint, not null on new column):
│     │
│     └─ Step 2: Will this violation cause production errors?
│        │
│        ├─ YES (endpoints will fail when accessing affected data)
│        │  └─ GO TO: ROLLBACK DECISION
│        │
│        └─ NO (constraint violation won't affect runtime)
│           └─ GO TO: CONTINUE MONITORING
│           (Document constraint violation for post-deployment review)
│
└─ OUTCOME: CONTINUE MONITORING or ROLLBACK DECISION

DECISION TIMELINE: 5 minutes max (2 min diagnose + 2 min attempt fix + 1 min decide)
DECISION LOGIC: Never override constraint violations during deployment window.
                If data cannot be trusted, rollback is safer than attempting live fixes.
```

**Diagnosis Commands**:
```bash
# 1. Check for constraint violations in logs
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
sudo journalctl -u open-repo --since "15 minutes ago" | \
  grep -i "constraint\|integrity\|unique\|foreign key" | head -10
EOF

# 2. For PostgreSQL: Check violated constraints
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
psql $DATABASE_URL << 'SQL'
SELECT constraint_name, table_name, constraint_type 
FROM information_schema.table_constraints 
WHERE constraint_type IN ('PRIMARY KEY', 'UNIQUE', 'FOREIGN KEY')
ORDER BY table_name;
SQL
EOF

# 3. For SQLite: Check foreign key status
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
sqlite3 /path/to/database.db "PRAGMA foreign_key_check;"
EOF

# 4. Rollback migration (if safe to do so)
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
source /opt/venv/open-repo/bin/activate
alembic downgrade -1  # Revert one migration version
EOF
```

---

### Scenario 4: Deployment Completes but Traffic Doesn't Flow

**Conditions**:
- All deployment steps completed successfully
- Health endpoint returns 200 OK
- OPDS endpoints return 200 OK with valid data
- Application logs show normal operation
- **BUT**: Monitoring from client side shows no traffic, or `/health` unreachable from external networks

**Interpretation**: Application is running locally, but network routing or firewall is blocking access

**Decision Tree**:

```
SCENARIO 4 STARTS: Application works locally but unreachable from network
│
├─ Step 1: Verify application is bound to correct network interface
│  │
│  ├─ Bound to 127.0.0.1 (only local access):
│  │  │
│  │  └─ Is this expected for this deployment?
│  │     │
│  │     ├─ YES (internal-only service)
│  │     │  └─ GO TO: CONTINUE MONITORING
│  │     │
│  │     └─ NO (should be accessible from monitoring network)
│  │        │
│  │        └─ Step 2: Change binding to correct interface
│  │           │
│  │           └─ Check CLAUDE.md: bind to 100.70.184.84 or specific Tailscale IP
│  │           (NEVER bind to 0.0.0.0)
│  │
│  └─ Bound to correct interface (100.70.184.84 or equivalent):
│     │
│     └─ Step 2: Check firewall rules on production host
│        │
│        ├─ Firewall blocking port 8000
│        │  │
│        │  └─ Allow port 8000: sudo ufw allow 8000/tcp
│        │  └─ Verify: sudo ufw status | grep 8000
│        │  └─ Re-test: curl http://100.70.184.84:8000/health
│        │  └─ If works, GO TO: CONTINUE MONITORING
│        │
│        └─ Firewall allows 8000 but still unreachable
│           │
│           └─ Step 3: Check network routing
│              │
│              ├─ Can monitoring machine ping production host?
│              │  ping -c 1 100.70.184.84
│              │  └─ If NO, network is down → GO TO: ROLLBACK DECISION
│              │
│              └─ Ping works, but curl fails
│                 │
│                 ├─ Check reverse proxy (nginx) if configured
│                 │  sudo systemctl status nginx
│                 │  sudo journalctl -u nginx -n 20
│                 │
│                 └─ If nginx is down, restart it
│                    sudo systemctl start nginx
│                    Re-test access, GO TO: CONTINUE MONITORING
│
└─ OUTCOME: CONTINUE MONITORING or ROLLBACK DECISION

DECISION TIMELINE: 3 minutes max (1 min diagnose network + 1 min attempt fix + 1 min verify)
DECISION LOGIC: This is usually a network/configuration issue, not an application issue.
                Fix the network/firewall problem, do NOT rollback code.
                If network is confirmed down, network team must fix (outside deployment scope).
```

**Diagnosis Commands**:
```bash
# 1. Check application binding address
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  'sudo netstat -tulpn | grep open-repo' || 'sudo lsof -i :8000'

# 2. Test local connectivity on production host
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  'curl -s http://127.0.0.1:8000/health | jq .'

# 3. Test connectivity from monitoring network
curl -s http://100.70.184.84:8000/health | jq .

# 4. Check firewall
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  'sudo ufw status | grep 8000'

# 5. Check nginx (if reverse proxy)
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  'sudo systemctl status nginx && sudo nginx -t'
```

---

### Scenario 5: Monitoring Infrastructure Fails (Blind Deployment)

**Conditions**:
- Deployment proceeds normally
- Application logs are inaccessible (journalctl unavailable, log file missing)
- Cannot reach monitoring endpoints (curl commands fail entirely)
- Cannot SSH to production host reliably
- **Complete visibility loss for 5+ minutes**

**Interpretation**: Monitoring tools have failed; operating deployment "blind"

**Decision Tree**:

```
SCENARIO 5 STARTS: Monitoring infrastructure fails, cannot observe system
│
├─ Step 1: Is this a local monitoring tool failure or production host is down?
│  │
│  ├─ Can ping production host?
│  │  │
│  │  ├─ YES (ping succeeds)
│  │  │  │
│  │  │  └─ Step 2: Can SSH to host?
│  │  │     │
│  │  │     ├─ YES (SSH succeeds)
│  │  │     │  │
│  │  │     │  └─ Monitoring tool is broken, but host is up
│  │  │     │     │
│  │  │     │     └─ Step 3: Try alternate monitoring method
│  │  │     │        │
│  │  │     │        ├─ Restart journalctl/syslog: sudo systemctl restart systemd-journald
│  │  │     │        ├─ Check if nginx/reverse proxy is blocking: systemctl status nginx
│  │  │     │        └─ After restart, attempt to access application again
│  │  │     │           │
│  │  │     │           ├─ Succeeds → GO TO: CONTINUE MONITORING
│  │  │     │           └─ Still fails → GO TO: ROLLBACK DECISION (cannot verify state)
│  │  │     │
│  │  │     └─ NO (SSH fails)
│  │  │        │
│  │  │        └─ Production host is isolated or hung
│  │  │           │
│  │  │           └─ Can manual health check recover access?
│  │  │              │
│  │  │              └─ Try hard reboot: (contact server admin to force reboot)
│  │  │              │
│  │  │              └─ Reboot not available, access not recovering
│  │  │                 └─ GO TO: ROLLBACK DECISION (cannot verify host state)
│  │  │
│  │  └─ NO (ping fails)
│  │     │
│  │     └─ Production host is completely unreachable (network down)
│  │        │
│  │        └─ This is network team issue, not deployment issue
│  │           │
│  │           ├─ If network is expected to be down: Contact ops team
│  │           └─ If network failure unexpected: Cannot proceed
│  │              DO NOT ROLLBACK yet; wait for network recovery (max 10 min)
│  │              After 10 min recovery, execute ROLLBACK DECISION if still down
│  │
│  └─ Step 4: Overall decision
│     │
│     └─ If any monitoring method recovers and shows application OK
│        └─ GO TO: CONTINUE MONITORING (increase monitoring frequency to 1 min)
│     └─ If no monitoring method recovers within 5 minutes
│        └─ GO TO: ROLLBACK DECISION (fail-safe: cannot verify system state)
│
└─ OUTCOME: CONTINUE MONITORING or ROLLBACK DECISION (fail-safe default)

DECISION TIMELINE: 5 minutes max for monitoring recovery attempt
                   If no recovery, automatic ROLLBACK DECISION after 5 min
DECISION LOGIC: During active monitoring window, cannot operate blind.
                Fail-safe: If cannot observe system, rollback to known-good state.
```

**Recovery Commands**:
```bash
# 1. Test network reachability
ping -c 2 100.70.184.84

# 2. Test SSH connectivity
ssh -i ~/.ssh/production_key -o ConnectTimeout=5 ubuntu@100.70.184.84 'echo OK'

# 3. Restart monitoring services (if SSH succeeds)
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
sudo systemctl restart systemd-journald
sudo systemctl restart rsyslog
EOF

# 4. Restart reverse proxy if blocking access
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo systemctl restart nginx'

# 5. Attempt basic connectivity test
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'systemctl is-active open-repo'

# 6. If all else fails, initiate rollback
# See ROLLBACK DECISION section below
```

---

## Section 3: Rollback Decision Criteria & Procedures

### When to Rollback: Decision Criteria

Rollback is **MANDATORY** (automatic decision) if ANY of these conditions persist for >5 minutes:

1. **Health check failure**: `/health` returns non-200 or timeout
2. **Health check cannot be accessed**: Network/firewall preventing access
3. **Multiple system failures**: Database + Application both showing errors
4. **Data corruption**: Constraint violations cannot be fixed safely
5. **Monitoring blind**: Cannot observe system state for 5+ minutes
6. **Unrecoverable cascade**: 3+ different alert types firing with no fix in sight

Rollback is **RECOMMENDED** if ANY of these conditions:

1. **Error rate >20%** and not improving after 3 minutes
2. **Response time >5 seconds** on all endpoints
3. **Database cannot be reached** and database team cannot restore within 5 minutes
4. **Code crash loop**: Application starts, crashes, restarts repeatedly

### Rollback Procedure (Safe Rollback with Data Integrity)

**Phase 1: Graceful Shutdown (1 minute)**

```bash
# 1. Stop application gracefully
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'SHUTDOWN'
echo "=== ROLLBACK: Graceful Shutdown ==="
sudo systemctl stop open-repo
sleep 3

# 2. Verify stopped
if ps aux | grep -E "uvicorn.*open" | grep -v grep > /dev/null; then
  echo "WARNING: Process still running, force stopping..."
  sudo pkill -9 -f "uvicorn.*open"
fi
echo "✅ Application stopped"
SHUTDOWN

# 3. Notify monitoring system
echo "[ROLLBACK] Application stopped at $(date -u +%H:%M:%S UTC)"
```

**Phase 2: Database Snapshot Restore (2 minutes)**

```bash
# 1. Identify pre-deployment database backup
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'DB_RESTORE'
echo "=== ROLLBACK: Database Snapshot Restore ==="

# For SQLite:
BACKUP_DIR="/opt/db-backups"
LATEST_BACKUP=$(ls -t "$BACKUP_DIR"/*.db.bak 2>/dev/null | head -1)

if [ -n "$LATEST_BACKUP" ]; then
  echo "Found backup: $LATEST_BACKUP"
  
  # Restore from backup
  cp "$LATEST_BACKUP" /path/to/database.db
  chown ubuntu:ubuntu /path/to/database.db
  chmod 644 /path/to/database.db
  
  echo "✅ Database restored from backup"
else
  echo "⚠️  No backup found. Database will be restored on next application startup."
fi

# For PostgreSQL:
# LATEST_BACKUP=$(ls -t "$BACKUP_DIR"/*.sql.gz 2>/dev/null | head -1)
# pg_restore --username=postgres --dbname=open-repo < <(gunzip -c "$LATEST_BACKUP")

DB_RESTORE
```

**Phase 3: Code Rollback (1 minute)**

```bash
# 1. Revert to previous commit
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'CODE_ROLLBACK'
echo "=== ROLLBACK: Code Revert ==="

cd /home/awank/dev/SuperClaude_Framework/projects/open-repo

# Get previous commit (before current deployment)
CURRENT=$(git log --oneline -1)
PREVIOUS=$(git log --oneline -2 | tail -1)

echo "Current: $CURRENT"
echo "Reverting to: $PREVIOUS"

# Hard reset to previous commit
git fetch origin master
git reset --hard HEAD~1

# Verify
echo "New HEAD: $(git log --oneline -1)"
echo "✅ Code reverted"

CODE_ROLLBACK
```

**Phase 4: Dependency Check (1 minute)**

```bash
# 1. Verify dependencies are still compatible
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'DEPS'
echo "=== ROLLBACK: Dependency Verification ==="

cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
source /opt/venv/open-repo/bin/activate

# Check critical packages
pip list | grep -E "fastapi|sqlalchemy|pydantic|uvicorn"

echo "✅ Dependencies verified"
DEPS
```

**Phase 5: Application Restart (1 minute)**

```bash
# 1. Start application
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'RESTART'
echo "=== ROLLBACK: Application Restart ==="

sudo systemctl start open-repo
sleep 5

# 2. Verify started
if sudo systemctl is-active --quiet open-repo; then
  echo "✅ Service is active"
else
  echo "❌ Service failed to start"
  sudo journalctl -u open-repo -n 20
  exit 1
fi

RESTART
```

**Phase 6: Post-Rollback Health Check (2 minutes)**

```bash
# 1. Test all endpoints
echo "=== ROLLBACK: Post-Rollback Verification ==="

echo "1. Health endpoint:"
HEALTH=$(curl -s -w "%{http_code}" http://100.70.184.84:8000/health)
if [[ "$HEALTH" == *"200"* ]]; then
  echo "✅ Health: OK"
else
  echo "❌ Health: FAILED ($(echo $HEALTH | tail -c 4))"
  echo "ROLLBACK MAY HAVE FAILED. Check logs."
fi

echo "2. OPDS endpoint:"
OPDS=$(curl -s -w "%{http_code}" -H "Accept: application/atom+xml" \
  http://100.70.184.84:8000/api/v2/opds/root.xml)
if [[ "$OPDS" == *"200"* ]]; then
  echo "✅ OPDS: OK"
else
  echo "❌ OPDS: FAILED ($(echo $OPDS | tail -c 4))"
fi

echo ""
echo "Rollback complete. Ready for post-incident review."
```

**Total Rollback Time**: ~7–10 minutes (target: <10 minutes)

---

## Section 4: Data Corruption Recovery Procedures

### When Data Corruption is Suspected

Data corruption is indicated by:
- Constraint violations that cannot be auto-fixed
- Orphaned records (foreign key referential integrity broken)
- Partial migration state (schema changed, but old data not migrated)
- Database size mismatch (suddenly smaller or larger than expected)

### Recovery Priority

**Priority 1: Preserve Data** (rollback with data snapshot)
**Priority 2: Restore Service** (rollback application code)
**Priority 3: Investigate** (post-incident root cause analysis)

### Corruption Recovery Workflow

```
1. DETECT CORRUPTION
   ├─ Identify what is corrupted (table, row, constraint)
   ├─ Determine scope (1 table vs. database-wide)
   └─ Document: timestamp, error message, affected data

2. DECISION: Can corruption be fixed live?
   ├─ If YES (e.g., update orphaned rows):
   │  ├─ Execute fix script
   │  ├─ Verify data integrity after fix
   │  └─ If fix succeeds, GO TO: CONTINUE MONITORING
   │
   └─ If NO (unknown corruption scope):
      └─ GO TO: ROLLBACK (safer than attempting live fixes)

3. ROLLBACK (if cannot fix)
   ├─ Stop application (Phase 1 above)
   ├─ Restore database backup (Phase 2 above)
   ├─ Revert code changes (Phase 3 above)
   ├─ Restart application (Phases 4–5 above)
   └─ Verify integrity (Phase 6 above)

4. POST-ROLLBACK INVESTIGATION
   ├─ Compare old database vs. new code
   ├─ Identify why migration failed
   ├─ Plan fix for next deployment attempt
   └─ Create database integrity test for pre-deployment validation
```

### Data Recovery Examples

**Example 1: Orphaned Foreign Key Records**

```sql
-- Detect orphaned records (if PostgreSQL/MySQL)
SELECT * FROM opds_entries 
WHERE catalog_id NOT IN (SELECT id FROM opds_catalogs);

-- Fix: either delete orphans or insert missing parent
DELETE FROM opds_entries 
WHERE catalog_id NOT IN (SELECT id FROM opds_catalogs);

-- Verify fix worked
SELECT COUNT(*) FROM opds_entries;
```

**Example 2: Partial Migration (Column Added, Data Not Migrated)**

```sql
-- Issue: New column exists, but data wasn't migrated
-- Symptom: NULL in new required column

-- Detect:
SELECT COUNT(*) FROM opds_entries WHERE new_column IS NULL;

-- Fix: Populate with default or computed value
UPDATE opds_entries 
SET new_column = 'default_value' 
WHERE new_column IS NULL;

-- Verify:
SELECT COUNT(*) FROM opds_entries WHERE new_column IS NULL;
-- Should return 0
```

---

## Section 5: Partial Deployment State Handling

### Identifying Partial Deployment

Partial deployment occurs when:
- Some deployment steps completed, but not all
- Example: Code deployed, database migrated, but service won't start
- Example: Service running, but OPDS subsystem crashed mid-startup

### Partial State Decision Matrix

| State | Indicator | Decision |
|-------|-----------|----------|
| **Code deployed, service not started** | App process missing, logs show startup error | FIX or ROLLBACK (investigate startup error first) |
| **Service running, OPDS endpoints fail** | Health=OK, /docs=OK, but /api/v2/opds/*=500 | INVESTIGATE (OPDS specific) or ROLLBACK |
| **Service running, docs endpoints fail** | Health=OK, /api/v2/opds/*=OK, but /docs=500 | INVESTIGATE (docs generation) or ROLLBACK |
| **Database migrated, application won't connect** | Schema changed, but app fails to connect | ROLLBACK (connection config issue) |
| **Service partially responsive** | Some endpoints OK, others timeout | INVESTIGATE (isolated failure) or ROLLBACK |

### Recovery Workflow for Partial Deployment

```
1. IDENTIFY WHICH SUBSYSTEM FAILED
   ├─ Health endpoint works? → Application core is OK
   ├─ OPDS endpoints work? → Database and OPDS logic are OK
   ├─ Docs endpoints work? → FastAPI schema generation is OK
   └─ Try each endpoint to narrow failure scope

2. ISOLATE THE PROBLEM
   ├─ If 1 endpoint fails, 2 others work → INVESTIGATE that endpoint
   ├─ If 2+ endpoints fail → Likely core application issue → ROLLBACK
   └─ If health works but ALL content endpoints fail → Database issue → INVESTIGATE or ROLLBACK

3. ATTEMPT FIX (max 3 minutes)
   ├─ For OPDS failures: Check database, verify tables exist
   ├─ For Docs failures: Restart FastAPI app service
   ├─ For generic failures: Check logs, identify error
   └─ Apply targeted fix if obvious (e.g., restart service)

4. DECISION
   ├─ If fix successful: GO TO: CONTINUE MONITORING
   ├─ If fix failed or unknown: GO TO: ROLLBACK DECISION
   └─ Document what subsystem failed for post-incident review
```

---

## Section 6: Post-Incident Audit Procedures

### Immediate Post-Incident (Within 30 minutes of resolution)

1. **Collect Evidence**:
   - Export all application logs from deployment window
   - Screenshot system metrics (CPU, memory, disk)
   - Export monitoring alerts/notifications
   - Document timeline of events

2. **Preserve Database State**:
   - Create backup of current database (post-incident state)
   - Label backup with incident timestamp
   - Store separately from daily backups

3. **Notify Stakeholders**:
   - If deployment successful: Send success notification
   - If rollback executed: Send rollback notification with ETA for retry

### Post-Incident Investigation (Within 24 hours)

See `DEPLOYMENT_POST_INCIDENT_AUDIT_CHECKLIST.md` for detailed procedures.

---

## Appendix: Incident Response Command Reference

**Quick Access Commands for Common Scenarios**:

```bash
# Get current health status
curl -s http://100.70.184.84:8000/health | jq .

# Get OPDS status
curl -s -H "Accept: application/atom+xml" http://100.70.184.84:8000/api/v2/opds/root.xml | head -3

# Get error rate (last 5 min)
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  'ERRORS=$(sudo journalctl -u open-repo --since "5 min ago" | grep "5[0-9][0-9]" | wc -l); echo "Errors: $ERRORS"'

# Restart application
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo systemctl restart open-repo'

# Check application status
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo systemctl status open-repo'

# View recent logs
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 50'

# Initiate rollback
# See "ROLLBACK PROCEDURE" section above for full steps
```

---

## Document Sign-Off

**Playbook Version**: 1.0  
**Created**: June 6, 2026  
**Valid For**: June 12, 2026 deployment and beyond  
**Last Updated**: June 6, 2026  
**Status**: PRODUCTION READY

**Usage Notes**:
- This playbook is referenced by `POST_DEPLOYMENT_MONITORING_PLAN.md`
- Incident commander should have this document open during active monitoring window
- Decision trees are designed to complete within 5 minutes
- All rollback procedures are designed to complete within 10 minutes
