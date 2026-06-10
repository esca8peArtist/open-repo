---
title: "Open-Repo June 12, 2026 — Post-Deployment Success Criteria and Validation Checklist"
project: open-repo
phase: "5 — ZimWriter libzim activation"
document_type: post-deployment-success-criteria
status: EXECUTE JUNE 12 — after deployment completes
created: 2026-06-10
target_deployment_date: 2026-06-12
execute_after: DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md Steps 1–8
monitoring_window: "60 minutes active monitoring post-deploy; 24 hours elevated monitoring"
rollback_authority: "Deployer — no escalation required within first 24 hours"
---

# Post-Deployment Success Criteria and Validation Checklist
## June 12, 2026 — Execute Immediately After Deployment Completes

**Purpose**: Immediately after the deployment procedure completes, run every check in this document in sequence. The deployment is not considered successful until the Final Verdict section is signed off. If any check fails, follow the rollback decision criteria in Section 5.

**Execution time**: 20–30 minutes for full validation.

**Who executes this**: The deployer, in the same terminal session used for deployment. Do not hand off to a different person mid-validation.

---

## TIMING CONFLICT REMINDER

This document uses **09:00 UTC** as deployment start. If 20:00 UTC is canonical, all post-deployment timing references shift by +11 hours. Confirm the canonical time before executing.

---

## Section 1 — Deployment Success Metrics

### 1.1 — Full Test Suite: 157/157 Still Passing Post-Deploy

Run the full test suite on the production code immediately after deployment. This confirms no test regression was introduced by the deployment process (environment changes, database state changes).

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== Post-Deployment Test Suite Verification ==="
echo "Start: $(date -u +%T UTC)"

uv run pytest tests/ -v --tb=short 2>&1 | tee /tmp/post-deploy-tests-$(date +%s).txt

SUMMARY=$(tail -5 /tmp/post-deploy-tests-*.txt | grep -E "passed|failed|error" | tail -1)
echo ""
echo "Result: $SUMMARY"

PASSED=$(echo "$SUMMARY" | grep -oP '\d+(?= passed)' | head -1)
FAILED=$(echo "$SUMMARY" | grep -oP '\d+(?= failed)' | head -1)

if [ "$PASSED" = "157" ] && [ -z "$FAILED" ]; then
  echo "PASS: 157/157 tests passing post-deployment"
else
  echo "FAIL: Test count changed post-deployment — passed=$PASSED failed=$FAILED"
  echo "Failing tests:"
  grep "^FAILED" /tmp/post-deploy-tests-*.txt | tail -20
fi

echo "End: $(date -u +%T UTC)"
```

**Expected output**:
```
157 passed in X.XXs
PASS: 157/157 tests passing post-deployment
```

**Pass criteria**: Exactly 157 passed, 0 failed, 0 errors. The count must match pre-deployment.

**If this fails**: Do not attempt to fix the failing tests in the production environment. Initiate rollback. The test failures indicate an environment or database state change that should be investigated on a development machine.

**Status**: [ ] PASS   [ ] FAIL

---

### 1.2 — ZimWriter Integration: Functional End-to-End Export

Verify the ZimWriter feature works in the deployed production environment by calling the actual API endpoint.

```bash
PROD_HOST="100.70.184.84"
echo "=== ZimWriter Integration Functional Test ==="

# Step 1: Trigger a test ZIM export via the API
# Adjust endpoint and payload to match the actual open-repo API schema
ZIM_RESPONSE=$(curl -s -w "\n%{http_code}" \
  -X POST "http://${PROD_HOST}:8000/api/v2/export/zim" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Post-Deployment Integration Test",
    "description": "Automated validation — June 12 deployment",
    "language": "eng",
    "entry_ids": []
  }')

HTTP_CODE=$(echo "$ZIM_RESPONSE" | tail -1)
BODY=$(echo "$ZIM_RESPONSE" | head -n -1)

echo "HTTP status: $HTTP_CODE"
echo "Response body: $BODY"

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ] || [ "$HTTP_CODE" = "202" ]; then
  echo "PASS: ZIM export endpoint accepted the request (HTTP $HTTP_CODE)"
  
  # If async: check for a job ID in the response
  JOB_ID=$(echo "$BODY" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('job_id', d.get('id', 'none')))" 2>/dev/null)
  if [ "$JOB_ID" != "none" ] && [ -n "$JOB_ID" ]; then
    echo "PASS: Async export job created with ID: $JOB_ID"
    
    # Poll for completion (max 30 seconds)
    for i in $(seq 1 6); do
      sleep 5
      STATUS_RESPONSE=$(curl -s "http://${PROD_HOST}:8000/api/v2/export/zim/${JOB_ID}/status" 2>/dev/null)
      STATUS=$(echo "$STATUS_RESPONSE" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('status','unknown'))" 2>/dev/null)
      echo "  Export status at T+${i}0s: $STATUS"
      if [ "$STATUS" = "completed" ] || [ "$STATUS" = "done" ]; then
        echo "PASS: ZIM export completed successfully"
        break
      elif [ "$STATUS" = "failed" ] || [ "$STATUS" = "error" ]; then
        echo "FAIL: ZIM export returned error status: $STATUS_RESPONSE"
        break
      fi
    done
  fi
else
  echo "FAIL: ZIM export endpoint returned HTTP $HTTP_CODE"
  echo "Response: $BODY"
fi
```

**Expected output**:
```
HTTP status: 202
PASS: ZIM export endpoint accepted the request (HTTP 202)
PASS: Async export job created with ID: abc123
  Export status at T+10s: processing
  Export status at T+20s: completed
PASS: ZIM export completed successfully
```

**If this fails**: Check application logs for the specific error (`sudo journalctl -u open-repo -n 30`). If the error matches a Failure Mode in `DEPLOYMENT_JUNE12_RISK_MITIGATION.md` (this directory), follow that playbook.

**Status**: [ ] PASS   [ ] FAIL

---

### 1.3 — API Health Endpoint: HTTP 200 with Valid JSON

```bash
PROD_HOST="100.70.184.84"

echo "=== API Health Endpoint Check ==="
HEALTH_RESPONSE=$(curl -s -w "\n%{http_code}" "http://${PROD_HOST}:8000/health")
HTTP_CODE=$(echo "$HEALTH_RESPONSE" | tail -1)
BODY=$(echo "$HEALTH_RESPONSE" | head -n -1)

echo "HTTP status: $HTTP_CODE"
echo "Body: $BODY"

if [ "$HTTP_CODE" = "200" ]; then
  # Validate JSON
  echo "$BODY" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    status = data.get('status', 'unknown')
    print(f'PASS: Health endpoint returns valid JSON — status: {status}')
    if status not in ('ok', 'healthy', 'up'):
        print(f'WARN: status field value is \"{status}\" — verify this is correct')
except json.JSONDecodeError as e:
    print(f'FAIL: Response is not valid JSON: {e}')
    sys.exit(1)
"
else
  echo "FAIL: Health endpoint returned HTTP $HTTP_CODE (expected 200)"
fi
```

**Expected output**:
```
HTTP status: 200
PASS: Health endpoint returns valid JSON — status: ok
```

**Status**: [ ] PASS   [ ] FAIL

---

### 1.4 — Database Accessible and Queryable

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

echo "=== Database Accessibility Check ==="

uv run python << 'DB_ACCESS'
import os
from sqlalchemy import create_engine, text, inspect

engine = create_engine(os.environ["DATABASE_URL"])

# Check 1: Basic connectivity
with engine.connect() as conn:
    conn.execute(text("SELECT 1"))
    print("PASS: Database connection successful")

# Check 2: All tables present
inspector = inspect(engine)
tables = set(inspector.get_table_names())
required = {"federation_partners", "federation_conflicts", "zim_exports"}
missing = required - tables
if missing:
    print(f"FAIL: Tables missing post-deployment: {missing}")
    raise SystemExit(1)
else:
    print(f"PASS: All 3 required tables present: {sorted(required)}")

# Check 3: Row counts (verify data integrity — no truncation occurred)
with engine.connect() as conn:
    for table in sorted(required):
        count = conn.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()
        print(f"      {table}: {count} rows")

print("PASS: Database accessible, schema intact, data readable")
DB_ACCESS
```

**Expected output**:
```
PASS: Database connection successful
PASS: All 3 required tables present: ['federation_conflicts', 'federation_partners', 'zim_exports']
      federation_conflicts: X rows
      federation_partners: X rows
      zim_exports: X rows
PASS: Database accessible, schema intact, data readable
```

**Status**: [ ] PASS   [ ] FAIL

---

### 1.5 — Automated Backups Verified

Confirm the post-deployment state is captured in a backup (separate from the pre-deployment backup), so the deployed state can itself be rolled back if needed in the 24-hour monitoring window.

```bash
PROD_HOST="100.70.184.84"
BACKUP_DIR="[SAME VALUE AS SECTION 3.4 OF PREFLIGHT]"

ssh -i ~/.ssh/production_key ubuntu@"$PROD_HOST" << POSTDEPLOY_BACKUP
TIMESTAMP=\$(date +%Y%m%d-%H%M%S)
BACKUP_DIR="$BACKUP_DIR"
SQLITE_FILE="[SQLITE PATH — same as pre-flight]"

mkdir -p "\$BACKUP_DIR"

POST_BACKUP="\${BACKUP_DIR}/open-repo-POST-DEPLOY-\${TIMESTAMP}.db.bak"
cp "\$SQLITE_FILE" "\$POST_BACKUP"

if [ -s "\$POST_BACKUP" ]; then
  SIZE=\$(du -sh "\$POST_BACKUP" | cut -f1)
  echo "PASS: Post-deployment backup created: \$POST_BACKUP (\$SIZE)"
  sqlite3 "\$POST_BACKUP" "PRAGMA integrity_check;" | head -1
else
  echo "FAIL: Post-deployment backup was not created"
fi

echo ""
echo "Backup directory contents:"
ls -lah "\$BACKUP_DIR"/ | grep "open-repo"
echo ""
echo "PRE-DEPLOY backup:  $(ls -t \$BACKUP_DIR/open-repo-2026*db.bak 2>/dev/null | grep -v POST | head -1)"
echo "POST-DEPLOY backup: \$POST_BACKUP"
POSTDEPLOY_BACKUP
```

**Expected output**:
```
PASS: Post-deployment backup created: /opt/db-backups/open-repo-POST-DEPLOY-20260612-091530.db.bak (2.1M)
ok
PRE-DEPLOY backup:  /opt/db-backups/open-repo-20260611-143022.db.bak
POST-DEPLOY backup: /opt/db-backups/open-repo-POST-DEPLOY-20260612-091530.db.bak
```

**Status**: [ ] PASS   [ ] FAIL

---

**Section 1 Summary**:

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Full test suite | 157/157 pass | __ / 157 | [ ] PASS / [ ] FAIL |
| ZimWriter integration | HTTP 200/201/202 + export completes | HTTP __ | [ ] PASS / [ ] FAIL |
| API health endpoint | HTTP 200, valid JSON | HTTP __ | [ ] PASS / [ ] FAIL |
| Database accessible | 3 tables, rows readable | __ tables | [ ] PASS / [ ] FAIL |
| Post-deploy backup | Non-zero file, integrity ok | __ | [ ] PASS / [ ] FAIL |

**Section 1 Decision**: [ ] GO — proceed to monitoring   [ ] NO-GO — rollback

---

## Section 2 — SLA Targets

These are realistic baselines derived from the existing codebase characteristics on Raspberry Pi 5 aarch64 hardware. Targets are conservative — they account for the Pi 5's thermal throttling behavior and the single-threaded uvicorn worker.

Measure these immediately after deployment while the system is under light load (post-deployment validation, no concurrent user traffic).

---

### 2.1 — API Response Time: p95 < 200ms

```bash
PROD_HOST="100.70.184.84"

echo "=== API Response Time Benchmark ==="
echo "Running 50 requests against /health and /api/v2/opds/root.xml"

# Measure /health endpoint (20 requests)
echo "--- /health endpoint ---"
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{time_total}\n" "http://${PROD_HOST}:8000/health"
done | tee /tmp/health-times.txt | \
  python3 -c "
import sys
times = [float(l.strip()) * 1000 for l in sys.stdin if l.strip()]
times.sort()
p50 = times[len(times)//2]
p95 = times[int(len(times)*0.95)]
p99 = times[int(len(times)*0.99)]
print(f'  p50: {p50:.0f}ms  p95: {p95:.0f}ms  p99: {p99:.0f}ms')
status = 'PASS' if p95 < 200 else 'WARN' if p95 < 500 else 'FAIL'
print(f'  {status}: p95 {p95:.0f}ms (target: < 200ms)')
"

# Measure /api/v2/opds/root.xml (20 requests)
echo "--- /api/v2/opds/root.xml endpoint ---"
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{time_total}\n" \
    -H "Accept: application/atom+xml" "http://${PROD_HOST}:8000/api/v2/opds/root.xml"
done | \
  python3 -c "
import sys
times = [float(l.strip()) * 1000 for l in sys.stdin if l.strip()]
times.sort()
p50 = times[len(times)//2]
p95 = times[int(len(times)*0.95)]
print(f'  p50: {p50:.0f}ms  p95: {p95:.0f}ms')
status = 'PASS' if p95 < 200 else 'WARN' if p95 < 500 else 'FAIL'
print(f'  {status}: p95 {p95:.0f}ms (target: < 200ms)')
"
```

**Expected output**:
```
--- /health endpoint ---
  p50: 12ms  p95: 45ms  p99: 72ms
  PASS: p95 45ms (target: < 200ms)
--- /api/v2/opds/root.xml endpoint ---
  p50: 28ms  p95: 95ms
  PASS: p95 95ms (target: < 200ms)
```

**Note on Pi 5 baselines**: The Pi 5 under light load typically serves simple JSON/XML endpoints in 10–80ms. The 200ms target provides a 3–4x headroom buffer for thermal variation and occasional GC pauses. If p95 exceeds 200ms on the health endpoint (which has essentially zero compute), the system is thermally throttled — check CPU temperature.

**SLA target**: p95 < 200ms for all endpoints except ZIM export (which is async).

**Status**: [ ] PASS   [ ] WARN (200–500ms)   [ ] FAIL (> 500ms)

---

### 2.2 — ZIM Export Time: < 30 Seconds for 1MB Content

A ZIM export with content totalling approximately 1MB should complete within 30 seconds on the Pi 5. This baseline was established from the integration test results in ZIMWRITER_MERGE_CONFLICT_RESOLUTION.md ("51 passed in 0.99s" for unit tests; actual file creation time is dominated by libzim's ZIM assembly, not the Python layer).

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

uv run python << 'ZIM_TIMING'
import tempfile, pathlib, time

from app.services.export.zim_writer import ZimWriter, ZimConfig, ZimEntry

# Create ~1MB of article content (100 articles * ~10KB each)
ARTICLE_CONTENT = "<html><body>" + "<p>" + "x" * 10000 + "</p>" * 10 + "</body></html>"

articles = [
    ZimEntry(
        path=f"article/timing-test-{i:04d}",
        title=f"Timing Test Article {i:04d}",
        content=ARTICLE_CONTENT,
        mime_type="text/html",
    )
    for i in range(100)
]

with tempfile.TemporaryDirectory() as tmpdir:
    config = ZimConfig(
        title="Timing Benchmark",
        description="ZIM export timing test",
        language_iso3="eng",
        output_path=pathlib.Path(tmpdir) / "timing-test.zim",
        creator_name="benchmark",
        publisher_name="open-repo",
    )
    
    writer = ZimWriter(config)
    for article in articles:
        writer.add_article(article)
    
    content_size_mb = sum(len(a.content) for a in articles) / 1_048_576
    print(f"Content size: {content_size_mb:.1f} MB ({len(articles)} articles)")
    
    start = time.perf_counter()
    writer.create_zim()
    elapsed = time.perf_counter() - start
    
    zim_size = config.output_path.stat().st_size
    print(f"ZIM file size: {zim_size:,} bytes ({zim_size/1_048_576:.1f} MB)")
    print(f"Export time: {elapsed:.1f}s")
    
    if elapsed < 30:
        print(f"PASS: Export completed in {elapsed:.1f}s (target: < 30s)")
    elif elapsed < 60:
        print(f"WARN: Export took {elapsed:.1f}s (target < 30s, acceptable < 60s)")
        print("      Pi 5 thermal throttling may be a factor — check CPU temperature")
    else:
        print(f"FAIL: Export took {elapsed:.1f}s (> 60s — unacceptable for 1MB content)")
ZIM_TIMING
```

**Expected output**:
```
Content size: 1.0 MB (100 articles)
ZIM file size: 892,416 bytes (0.9 MB)
Export time: 4.3s
PASS: Export completed in 4.3s (target: < 30s)
```

**Note**: The unit tests ran in 0.99s because they mock the ZimWriter file creation. The 30-second target accounts for actual libzim file assembly, Xapian index building, and Pi 5 I/O throughput (~30 MB/s sequential write). Real-world content exports should fall well within this target.

**SLA target**: < 30 seconds for 1MB content corpus.

**Status**: [ ] PASS   [ ] WARN (30–60s)   [ ] FAIL (> 60s)

---

### 2.3 — Database Query Response: < 100ms

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend

uv run python << 'DB_TIMING'
import os, time
from sqlalchemy import create_engine, text

engine = create_engine(os.environ["DATABASE_URL"])

queries = [
    ("SELECT 1 (baseline)", "SELECT 1"),
    ("SELECT from federation_partners", "SELECT COUNT(*) FROM federation_partners"),
    ("SELECT from federation_conflicts", "SELECT COUNT(*) FROM federation_conflicts"),
    ("SELECT from zim_exports", "SELECT COUNT(*) FROM zim_exports"),
    ("JOIN query", "SELECT fp.id, fc.id FROM federation_partners fp LEFT JOIN federation_conflicts fc ON fp.id = fc.partner_id LIMIT 10"),
]

all_pass = True
with engine.connect() as conn:
    for label, sql in queries:
        start = time.perf_counter()
        result = conn.execute(text(sql))
        result.fetchall()
        elapsed_ms = (time.perf_counter() - start) * 1000
        
        status = "PASS" if elapsed_ms < 100 else "WARN" if elapsed_ms < 500 else "FAIL"
        if status == "FAIL":
            all_pass = False
        print(f"  {status}: {label}: {elapsed_ms:.1f}ms")

if all_pass:
    print("PASS: All database queries respond in < 100ms")
else:
    print("FAIL: One or more queries exceed 100ms — investigate database performance")
DB_TIMING
```

**Expected output**:
```
  PASS: SELECT 1 (baseline): 0.3ms
  PASS: SELECT from federation_partners: 1.2ms
  PASS: SELECT from federation_conflicts: 1.4ms
  PASS: SELECT from zim_exports: 1.1ms
  PASS: JOIN query: 2.1ms
PASS: All database queries respond in < 100ms
```

**SLA target**: < 100ms for all database queries at idle load. SQLite on the Pi 5's SD card or NVMe should achieve < 10ms for simple queries; the 100ms target provides a generous buffer for GC pauses and SD card write latency.

**Status**: [ ] PASS   [ ] WARN   [ ] FAIL

---

### 2.4 — Uptime Target: 99.5% During Business Hours

The 99.5% uptime target means the service can be unavailable for at most 43 minutes during an 8-hour business day. The deployment itself takes 25–35 minutes, which consumes approximately 7% of the daily uptime budget if deployed during business hours — meaning the business hours uptime for June 12 will not meet the 99.5% daily target if deployed at 09:00 UTC.

**Recommendation**: If 09:00 UTC is the confirmed deployment time, communicate to stakeholders that June 12 SLA is 95% (maintenance window) and the 99.5% SLA applies from June 13 onward. If 20:00 UTC is confirmed, June 12 business hours SLA is 100% (deployment during off-hours).

```bash
# Post-deployment uptime monitoring — run for 60 minutes
echo "=== Uptime Monitoring (60 minutes) ==="
echo "Started at: $(date -u +%T UTC)"

FAILURES=0
TOTAL=0
START=$(date +%s)
END=$((START + 3600))  # 60 minutes

while [ $(date +%s) -lt $END ]; do
  HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "http://100.70.184.84:8000/health" 2>/dev/null)
  TOTAL=$((TOTAL + 1))
  
  if [ "$HTTP_CODE" != "200" ]; then
    FAILURES=$((FAILURES + 1))
    echo "$(date -u +%T UTC) — FAIL: health endpoint returned $HTTP_CODE"
  fi
  
  sleep 30  # Poll every 30 seconds
done

UPTIME_PCT=$(python3 -c "print(f'{((${TOTAL} - ${FAILURES}) / ${TOTAL} * 100):.2f}')")
echo ""
echo "=== 60-Minute Uptime Summary ==="
echo "Total polls: $TOTAL"
echo "Failures: $FAILURES"
echo "Uptime: ${UPTIME_PCT}%"

if python3 -c "exit(0 if float('${UPTIME_PCT}') >= 99.5 else 1)"; then
  echo "PASS: 60-minute uptime ${UPTIME_PCT}% >= 99.5% target"
else
  echo "FAIL: 60-minute uptime ${UPTIME_PCT}% < 99.5% target"
fi
```

**Note**: This monitoring loop runs for 60 minutes. Start it and move on to Section 3 (review the dashboard) while it runs in a separate terminal. Check its output at the end of the monitoring window.

**SLA target**: 99.5% over any 60-minute window post-deployment.

**Status**: [ ] PASS (reviewed at end of monitoring window)   [ ] FAIL

---

**Section 2 Summary**:

| SLA Target | Threshold | Measured | Status |
|-----------|-----------|----------|--------|
| API response time (p95) | < 200ms | __ms | [ ] PASS / [ ] WARN / [ ] FAIL |
| ZIM export time (1MB) | < 30s | __s | [ ] PASS / [ ] WARN / [ ] FAIL |
| Database query response | < 100ms | __ms | [ ] PASS / [ ] WARN / [ ] FAIL |
| 60-min uptime | > 99.5% | __%  | [ ] PASS / [ ] FAIL |

---

## Section 3 — Monitoring Dashboard

Four KPIs to watch in real-time during the 60-minute active monitoring window and on an ongoing basis.

### KPI 1 — Service Health

**What to watch**: The `/health` endpoint. A `200 OK` response every 30 seconds confirms the service is alive.

**Command** (run in a separate terminal):
```bash
watch -n 30 'curl -s http://100.70.184.84:8000/health | python3 -m json.tool'
```

**Normal state**: `{"status": "ok", "timestamp": "..."}` — consistent, every poll.  
**Alert threshold**: Any single non-200 response triggers investigation. Two consecutive non-200 responses trigger rollback evaluation.

---

### KPI 2 — Application Error Rate

**What to watch**: The count of ERROR and CRITICAL log lines per 5-minute window in journald.

**Command** (run in a separate terminal):
```bash
# Real-time error monitoring
sudo journalctl -u open-repo -f --since now | grep -E "ERROR|CRITICAL|Traceback"
```

**Normal state**: Zero lines. The deployed application should produce only `INFO`-level logs under normal operation.  
**Alert threshold**: Any CRITICAL log entry triggers immediate investigation. More than 5 ERROR entries per 5 minutes triggers investigation. Sustained ERROR rate > 1% of requests triggers rollback evaluation.

---

### KPI 3 — ZIM Export Queue Depth

**What to watch**: The number of pending ZIM exports in the `zim_exports` table with `export_status != 'completed'`.

**Command** (run every 5 minutes):
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
uv run python -c "
from sqlalchemy import create_engine, text
import os
engine = create_engine(os.environ['DATABASE_URL'])
with engine.connect() as conn:
    pending = conn.execute(text(\"SELECT export_status, COUNT(*) as cnt FROM zim_exports GROUP BY export_status\")).fetchall()
    for row in pending:
        print(f'  {row[0]}: {row[1]} exports')
    total = conn.execute(text('SELECT COUNT(*) FROM zim_exports')).scalar()
    print(f'Total zim_exports rows: {total}')
"
```

**Normal state**: Most rows have `export_status = 'completed'`. Some `processing` rows are normal if exports are in progress.  
**Alert threshold**: More than 10 rows with `export_status = 'failed'` indicates a systematic ZIM export failure — review application logs.

---

### KPI 4 — System Resources

**What to watch**: CPU temperature, memory usage, and disk space on the Pi 5.

**Command** (run every 10 minutes):
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'RESOURCES'
echo "=== System Resources $(date -u +%T UTC) ==="

# CPU temperature
if [ -f /sys/class/thermal/thermal_zone0/temp ]; then
  TEMP=$(($(cat /sys/class/thermal/thermal_zone0/temp) / 1000))
  echo "CPU temp: ${TEMP}°C $([ $TEMP -gt 85 ] && echo '⚠ WARN: Thermal throttling' || echo '(OK)')"
fi

# Memory
free -m | awk '/^Mem:/ {printf "Memory: used=%dMB free=%dMB (%.0f%% used)\n", $3, $7, $3/$2*100}'

# Disk
df -h /opt | awk 'NR==2 {printf "Disk /opt: used=%s free=%s (%s)\n", $3, $4, $5}'

# Process count and CPU
ps aux | grep -E "uvicorn|python" | grep -v grep | wc -l | xargs echo "App processes:"
RESOURCES
```

**Normal state**: Temperature < 80°C, memory > 1GB free, disk usage < 80%.  
**Alert thresholds**:
- Temperature > 85°C: suspend ZIM exports until cooling is available
- Memory < 256MB free: investigate for memory leak; consider service restart
- Disk > 90% used: clean old ZIM files before further exports

---

## Section 4 — Incident Response Procedures (First 24 Hours)

### If Issues Arise in the First 60 Minutes Post-Deploy

**Severity 1 — Service down** (health endpoint non-200):

```bash
# T+0: Confirm the failure
curl -v http://100.70.184.84:8000/health

# T+1: Check service status
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 "sudo systemctl is-active open-repo && sudo journalctl -u open-repo -n 30"

# T+2: Attempt quick restart (once only)
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 "sudo systemctl restart open-repo && sleep 5 && curl -s http://127.0.0.1:8000/health"

# T+5: If not resolved after restart — initiate rollback
# Execute root-level DEPLOYMENT_JUNE12_RISK_MITIGATION.md Section 1, Steps 1-6
```

**Severity 2 — ZIM export failing** (all other endpoints working):

```bash
# Check logs for the specific error
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  "sudo journalctl -u open-repo --since '5 minutes ago' | grep -E 'zim|ZIM|libzim|export'"

# Identify from DEPLOYMENT_JUNE12_RISK_MITIGATION.md which Failure Mode matches
# Most likely: FM2 (libzim runtime error)
# Decision: rollback or disable ZIM endpoint (other features unaffected)
```

**Severity 3 — Elevated error rate** (> 5 errors per minute, service still running):

```bash
# Review error patterns
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  "sudo journalctl -u open-repo --since '10 minutes ago' | grep ERROR | sort | uniq -c | sort -rn | head -10"

# Determine if errors are ZIM-related (low impact) or affecting all requests (high impact)
# If all requests: proceed to rollback evaluation
# If ZIM-only: follow FM2 procedure in DEPLOYMENT_JUNE12_RISK_MITIGATION.md
```

### If Issues Arise Between 60 Minutes and 24 Hours Post-Deploy

The first 60 minutes covers the highest-risk window. If the deployment passes the 60-minute monitoring window cleanly, subsequent issues are unlikely to be deployment-caused. Standard on-call procedures apply.

However, retain the ability to roll back for 24 hours:
- Keep the pre-deployment backup accessible (`/opt/db-backups/open-repo-20260611-*.db.bak`)
- Keep the previous git commit hash documented: `git log --oneline -2 | tail -1`
- Keep the `DEPLOYMENT_JUNE12_RISK_MITIGATION.md` document open until 24 hours post-deploy

---

## Section 5 — User Communication

### Successful Deployment Notification

Send within 15 minutes of completing the Section 1 validation checks.

**For Slack/Mattermost/email**:
```
Subject: open-repo ZimWriter deployment complete — June 12, 2026

Deployment of the ZimWriter (Phase 5 libzim integration) completed successfully at [TIME] UTC.

What changed:
- ZIM offline export is now available via the API at /api/v2/export/zim
- 51 new ZIM-specific tests added (total test suite: 157 tests, all passing)
- OPDS, federation, and accessibility features unchanged

Validated:
- All 157 tests passing
- API health endpoint: HTTP 200
- ZIM export integration: functional
- Response times within SLA targets

The service will be under elevated monitoring for the next 24 hours.
Questions: [deployer contact]
```

**Communication template reference**: See `projects/open-repo/DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md` Template 3 for the full stakeholder notification.

---

## Section 6 — Rollback Decision Criteria

### Rollback Immediately (No Discussion Required)

Execute root-level `DEPLOYMENT_JUNE12_RISK_MITIGATION.md` Section 1, Steps 1–6 if **any** of the following is true:

| Trigger | Threshold |
|---------|-----------|
| Health endpoint down | 2 consecutive polls returning non-200 |
| Service process not running | `systemctl is-active open-repo` returns `failed` |
| CRITICAL log entry | Any single CRITICAL entry in application logs |
| Test suite failures post-deploy | Any tests failing that passed pre-deploy |
| Database connection error | `DATABASE_URL` unreachable from application |
| ZIM export causing service crash | `Killed` or `segfault` in journald after export attempt |
| Deployment window exceeded | Service down > 60 minutes from `systemctl stop` |

### Rollback After Investigation (5-Minute Budget)

Execute rollback if the quick fix does not resolve within 5 minutes:

| Trigger | Quick Fix Attempt |
|---------|------------------|
| ZIM endpoint HTTP 500 | Check logs; if libzim version mismatch → upgrade; else rollback |
| p95 response time > 500ms | Check CPU temp; if > 85°C → wait for cooling; else rollback |
| Database query > 500ms | Check disk I/O and available memory; else rollback |
| > 10 failed ZIM exports in queue | Disable ZIM endpoint, schedule fix (do not rollback) |

### Do NOT Rollback

These conditions are not rollback triggers. Handle via standard monitoring and next-sprint fixes:

- p95 response time 200–500ms (WARN level, not FAIL)
- ZIM export takes 30–60 seconds (WARN, monitor for trend)
- `INFO`-level log messages appearing in unexpected patterns
- Single isolated ZIM export failure (retry; monitor for recurrence)

---

## Final Verdict

Complete this section only after all checks in Sections 1–3 are done and the 60-minute monitoring window has completed.

**Deployment completed at**: ____________________ UTC  
**Section 1 validation completed at**: ____________________ UTC  
**60-minute monitoring window ended at**: ____________________ UTC  

**Results**:

| Section | Result |
|---------|--------|
| Section 1: Deployment Success Metrics (5 checks) | ALL PASS / PARTIAL / FAIL |
| Section 2: SLA Targets (4 targets) | ALL PASS / WARN / FAIL |
| Section 3: Monitoring (60 min, no alerts) | CLEAN / ALERTS FIRED |

**Stakeholder notification sent**: [ ] Yes, at __________ UTC via __________________

**Rollback required**: [ ] No — deployment successful   [ ] Yes — initiate root-level rollback

**Final verdict**:

- [ ] **DEPLOYMENT SUCCESSFUL** — Phase 5 ZimWriter is live in production. Elevated monitoring continues for 24 hours.
- [ ] **ROLLBACK EXECUTED** — Service restored to pre-deploy state. Post-mortem scheduled.

**Signed off by**: ____________________________  
**Time**: ____________________ UTC

---

## Appendix — All Expected Endpoint Responses Post-Deploy

Run these checks in one block to capture the full endpoint state immediately after deployment:

```bash
PROD_HOST="100.70.184.84"
echo "=== Full Endpoint Verification $(date -u) ==="

ENDPOINTS=(
  "http://${PROD_HOST}:8000/health"
  "http://${PROD_HOST}:8000/docs"
  "http://${PROD_HOST}:8000/redoc"
  "http://${PROD_HOST}:8000/api/v2/opds/root.xml"
  "http://${PROD_HOST}:8000/api/v2/opds/entries"
)
HEADERS=(
  ""
  ""
  ""
  "Accept: application/atom+xml"
  "Accept: application/atom+xml"
)

for i in "${!ENDPOINTS[@]}"; do
  URL="${ENDPOINTS[$i]}"
  HEADER="${HEADERS[$i]}"
  
  if [ -n "$HEADER" ]; then
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -H "$HEADER" "$URL")
  else
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
  fi
  
  STATUS=$( [ "$HTTP_CODE" = "200" ] && echo "PASS" || echo "FAIL" )
  echo "$STATUS: $URL → HTTP $HTTP_CODE"
done
```

**Expected output** (all lines should show PASS):
```
PASS: http://100.70.184.84:8000/health → HTTP 200
PASS: http://100.70.184.84:8000/docs → HTTP 200
PASS: http://100.70.184.84:8000/redoc → HTTP 200
PASS: http://100.70.184.84:8000/api/v2/opds/root.xml → HTTP 200
PASS: http://100.70.184.84:8000/api/v2/opds/entries → HTTP 200
```

---

**Document Version**: 1.0  
**Created**: 2026-06-10  
**Valid For**: June 12, 2026 deployment and 24-hour post-deployment monitoring window  
**Execute After**: DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md  
**Reference Alongside**: DEPLOYMENT_JUNE12_RISK_MITIGATION.md (this directory), projects/open-repo/DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md
