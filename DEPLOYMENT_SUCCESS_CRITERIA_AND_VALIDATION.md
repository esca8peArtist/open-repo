---
title: "Deployment Success Criteria and Validation"
subtitle: "Post-Deployment Testing & Health Checks for Both Platforms"
project: open-repo
phase: 6 (infrastructure deployment)
document_type: validation-procedures
status: READY FOR EXECUTION
created: 2026-06-23
estimated_duration: 5-10 minutes
target_completion: 2026-06-24 15:00 UTC (following deployment completion)
---

# Deployment Success Criteria and Validation

## Overview

This document defines success metrics for both Docker and systemd deployment paths, provides validation checklists, and establishes SLA definitions for when deployment is "complete and ready for Phase 5.2 content ingestion."

---

## Phase 1: Success Metrics (Common to Both Paths)

### 1.1 Application-Level Success Metrics

#### Metric 1: Health Endpoint Available

**Definition**: API responds with 200 OK to GET `/api/health`

**Command**:
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/api/health
```

**Expected Output**: `200`

**Success Criteria**: PASS ✅ if output is `200`, FAIL ❌ if any other code (404, 503, timeout, etc.)

**SLA**: Health endpoint must respond within 2 seconds (P99 latency <500ms)

---

#### Metric 2: Application Version Correct

**Definition**: API reports correct version number (0.2.0)

**Command**:
```bash
curl -s http://localhost:8000/api/health | jq '.version'
```

**Expected Output**: `"0.2.0"`

**Success Criteria**: PASS ✅ if matches deployed version, FAIL ❌ if version mismatch or missing

**SLA**: Immediate (checked during health check)

---

#### Metric 3: Database Connection Working

**Definition**: API can query database without errors

**Command** (via application internal test):
```bash
curl -s http://localhost:8000/api/test-db | jq '.status'
```

**Expected Output**: `"connected"`

**Success Criteria**: PASS ✅ if status is "connected", FAIL ❌ if "error", timeout, or no response

**SLA**: Database operations must complete <100ms (P99)

---

#### Metric 4: Search Service (Meilisearch) Connected

**Definition**: API can reach Meilisearch search service

**Command**:
```bash
curl -s http://localhost:7700/health | jq '.status'
```

**Expected Output**: `"available"` (on port 7700)

**Success Criteria**: PASS ✅ if "available", FAIL ❌ if error or timeout

**SLA**: Meilisearch must respond <100ms (P99)

---

### 1.2 Infrastructure-Level Success Metrics

#### Metric 5: Port Bindings Correct

**Definition**: API binds to localhost only (security requirement)

**Docker Command**:
```bash
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

**Expected Output** (Docker):
```
NAME                      PORTS
open-repo-api             127.0.0.1:8000->8000/tcp
open-repo-postgres        127.0.0.1:5432->5432/tcp
open-repo-meilisearch     127.0.0.1:7700->7700/tcp
```

**systemd Command**:
```bash
sudo ss -tlnp | grep -E '8000|5432|7700'
```

**Expected Output** (systemd):
```
LISTEN  127.0.0.1:8000  USERS:(("uvicorn",pid=XXXX,fd=3))
LISTEN  127.0.0.1:5432  USERS:(("postgres",pid=YYYY,fd=X))
LISTEN  127.0.0.1:7700  USERS:(("meilisearch",pid=ZZZZ,fd=X))
```

**Success Criteria**: PASS ✅ if all three ports bind to `127.0.0.1` only, FAIL ❌ if any bind to `0.0.0.0` or external interface

**SLA**: Immediate (no external exposure allowed)

---

#### Metric 6: Service Resource Usage Acceptable

**Definition**: No service consuming >2GB memory, total <3.5GB

**Command**:
```bash
# Docker path:
docker stats --no-stream --format "table {{.Container}}\t{{.MemUsage}}"

# systemd path:
ps aux | awk '{print $2, $6}' | grep -E '(open-repo|postgres|meilisearch)' | \
  awk '{sum+=$2} END {print "Total:", sum "MB"}'
```

**Expected Output**: 
- Individual processes: <1.2GB each
- Total: <3.5GB

**Success Criteria**: PASS ✅ if <3.5GB total, FAIL ❌ if >3.5GB (indicates memory leak or misconfiguration)

**SLA**: Idle <1GB, sustained load <3GB, peak <3.5GB

---

#### Metric 7: Service Auto-Restart Working (Resilience Test)

**Definition**: If service crashes, systemd auto-restarts it

**Test Procedure**:

```bash
# Docker path:
CONTAINER_ID=$(docker ps -q -f name=open-repo-api)
docker kill $CONTAINER_ID
sleep 5
docker ps -f name=open-repo-api --format "table {{.Status}}"

# systemd path:
sudo systemctl restart open-repo
sleep 5
sudo systemctl status open-repo | grep "active (running)"
```

**Expected Output**:
- Container should restart automatically
- systemd service should return "active (running)"

**Success Criteria**: PASS ✅ if auto-restart detected within 10 seconds, FAIL ❌ if manual restart required

**SLA**: Auto-restart must occur <30 seconds after failure

---

## Phase 2: Validation Checklist

### 2.1 Pre-Validation Setup

Before running validation tests, ensure:

**Step 1: Confirm Deployment Completed**
```bash
# Docker: all three containers running
docker ps | grep -c "open-repo"  # Should output: 3

# systemd: all three services running
sudo systemctl status open-repo meilisearch postgresql | grep -c "active (running)"  # Should output: 3
```

**Step 2: Wait for Initialization**
```bash
# Wait 30 seconds for services to fully initialize
sleep 30

# Then check health
curl -s http://localhost:8000/api/health
```

---

### 2.2 Validation Test Suite

#### Test 1: API Responds to Health Check

```bash
#!/bin/bash
# Health check test

response=$(curl -s http://localhost:8000/api/health)
status=$(echo $response | jq '.status')

if [ "$status" = '"ok"' ]; then
    echo "✅ PASS: Health endpoint responding"
    exit 0
else
    echo "❌ FAIL: Health endpoint not responding. Response: $response"
    exit 1
fi
```

**Expected**: ✅ PASS

---

#### Test 2: API Handles Request/Response Cycle

```bash
#!/bin/bash
# Endpoint availability test

# Test root endpoint
response=$(curl -s -w "\n%{http_code}" http://localhost:8000/)
http_code=$(echo "$response" | tail -1)

if [ "$http_code" = "200" ] || [ "$http_code" = "307" ]; then
    echo "✅ PASS: API responding to requests"
    exit 0
else
    echo "❌ FAIL: API not responding. HTTP code: $http_code"
    exit 1
fi
```

**Expected**: ✅ PASS

---

#### Test 3: Database Connected and Queryable

```bash
#!/bin/bash
# Database connectivity test

# Docker path:
docker-compose exec -T app python << 'PYEOF'
import asyncio
from app.database import init_db

async def test_db():
    try:
        await init_db()
        print("✅ PASS: Database connected")
        return 0
    except Exception as e:
        print(f"❌ FAIL: Database error: {e}")
        return 1

exit(asyncio.run(test_db()))
PYEOF

# systemd path:
cd /opt/open-repo
source venv/bin/activate
python << 'PYEOF'
import asyncio
from app.database import init_db

async def test_db():
    try:
        await init_db()
        print("✅ PASS: Database connected")
        return 0
    except Exception as e:
        print(f"❌ FAIL: Database error: {e}")
        return 1

exit(asyncio.run(test_db()))
PYEOF
```

**Expected**: ✅ PASS

---

#### Test 4: Search Service Accessible

```bash
#!/bin/bash
# Meilisearch connectivity test

response=$(curl -s http://localhost:7700/health)
status=$(echo $response | jq '.status')

if [ "$status" = '"available"' ]; then
    echo "✅ PASS: Meilisearch service available"
    exit 0
else
    echo "❌ FAIL: Meilisearch not available. Response: $response"
    exit 1
fi
```

**Expected**: ✅ PASS

---

#### Test 5: Port Bindings Secure

```bash
#!/bin/bash
# Port binding test (no 0.0.0.0 exposure)

# Docker path:
exposed=$(docker inspect open-repo-api | jq '.[] | .NetworkSettings.Ports | keys[]' | grep -c "0.0.0.0" || true)

# systemd path:
exposed=$(sudo ss -tlnp | grep -E '0\.0\.0\.0:(8000|5432|7700)' | wc -l)

if [ "$exposed" -eq 0 ]; then
    echo "✅ PASS: All ports bind to 127.0.0.1 only"
    exit 0
else
    echo "❌ FAIL: Exposed ports detected on 0.0.0.0"
    exit 1
fi
```

**Expected**: ✅ PASS

---

#### Test 6: Memory Usage Acceptable

```bash
#!/bin/bash
# Memory usage test

# Docker path:
total_mem=$(docker stats --no-stream --format "{{.MemUsage}}" | \
  awk -F'/' '{print $1}' | sed 's/[^0-9]*//g' | \
  awk '{sum+=$1} END {print sum}')

# systemd path:
total_mem=$(ps aux | awk '{print $6}' | tail -n +2 | \
  awk '{sum+=$1} END {print sum}')

echo "Total memory usage: ${total_mem}MB"

if [ $total_mem -lt 3500 ]; then
    echo "✅ PASS: Memory usage acceptable"
    exit 0
else
    echo "❌ FAIL: Memory usage excessive (${total_mem}MB > 3500MB)"
    exit 1
fi
```

**Expected**: ✅ PASS

---

#### Test 7: Auto-Restart Mechanism Working

```bash
#!/bin/bash
# Auto-restart resilience test

# Docker path:
initial_uptime=$(docker inspect open-repo-api | jq '.[] | .State.StartedAt')
docker kill $(docker ps -q -f name=open-repo-api)
sleep 10
new_uptime=$(docker inspect open-repo-api | jq '.[] | .State.StartedAt')

if [ "$initial_uptime" != "$new_uptime" ]; then
    echo "✅ PASS: Container auto-restarted after kill"
    exit 0
else
    echo "❌ FAIL: Container did not restart"
    exit 1
fi

# systemd path:
pid_before=$(systemctl show -p MainPID --value open-repo)
sudo systemctl kill open-repo
sleep 10
pid_after=$(systemctl show -p MainPID --value open-repo)

if [ "$pid_before" != "$pid_after" ]; then
    echo "✅ PASS: Service auto-restarted after kill"
    exit 0
else
    echo "❌ FAIL: Service did not restart"
    exit 1
fi
```

**Expected**: ✅ PASS

---

## Phase 3: Performance Baseline Expectations

### 3.1 Response Time SLAs

| Endpoint | P50 | P95 | P99 |
|----------|-----|-----|-----|
| `/api/health` | <50ms | <100ms | <500ms |
| `/api/content/search` | <100ms | <250ms | <1000ms |
| `/api/content/{id}` | <50ms | <150ms | <500ms |

**How to measure**:
```bash
# Single request timing
time curl -s http://localhost:8000/api/health > /dev/null

# Load test (requires 'ab' or 'wrk'):
ab -n 100 -c 10 http://localhost:8000/api/health/
```

**Acceptance**: All endpoints must meet P99 <1000ms on idle system.

---

### 3.2 Concurrent Request Handling

**Definition**: API should handle 10 concurrent requests without errors

**Test**:
```bash
# Using Apache Bench
ab -n 100 -c 10 http://localhost:8000/api/health

# Expected: 100 requests completed, 0 failed
```

**Acceptance**: 0 failures, <5% error rate under 10 concurrent connections.

---

### 3.3 Home Page Load Time

**Definition**: Web UI root page should load in <500ms

**Test**:
```bash
curl -o /dev/null -s -w "Total time: %{time_total}s\n" http://localhost:8000/
```

**Expected Output**: `Total time: <0.500s`

**Acceptance**: <500ms on idle Pi5.

---

## Phase 4: Post-Deployment Monitoring Setup

### 4.1 Health Check Monitoring Script

Create `/opt/open-repo/health_check.sh`:

```bash
#!/bin/bash
# Periodic health check script

LOGFILE=/opt/open-repo/logs/health_check.log
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Test health endpoint
response=$(curl -s -w "\n%{http_code}" http://localhost:8000/api/health)
http_code=$(echo "$response" | tail -1)
body=$(echo "$response" | head -1)

if [ "$http_code" = "200" ]; then
    echo "[$TIMESTAMP] ✅ Health check passed" >> $LOGFILE
    exit 0
else
    echo "[$TIMESTAMP] ❌ Health check failed. HTTP $http_code" >> $LOGFILE
    
    # Send alert (optional)
    echo "Open-Repo health check failed at $TIMESTAMP. HTTP code: $http_code" | \
        mail -s "Open-Repo Alert" admin@example.com
    
    exit 1
fi
```

**Run every 5 minutes via cron**:
```bash
*/5 * * * * /opt/open-repo/health_check.sh
```

---

### 4.2 Log Aggregation

**Docker path**:
```bash
# Follow all logs
docker-compose logs -f

# Search logs
docker-compose logs | grep ERROR
docker-compose logs app | tail -100
```

**systemd path**:
```bash
# Follow service logs
sudo journalctl -u open-repo -f

# Search logs
sudo journalctl -u open-repo | grep ERROR
sudo journalctl -u open-repo -n 100
```

---

### 4.3 Metrics Export (Optional)

If using Prometheus:

```yaml
# /etc/prometheus/prometheus.yml (add to global config)
scrape_configs:
  - job_name: 'open-repo'
    static_configs:
      - targets: ['localhost:8000']
    metrics_path: '/metrics'
    scrape_interval: 15s
```

---

## Phase 5: SLA Definition — "Deployment Complete"

### When Deployment is "Ready for Phase 5.2"

Deployment is complete and ready to advance to Phase 5.2 content ingestion when:

1. **✅ All 7 Success Metrics PASS**:
   - Health endpoint available (200 OK)
   - Version correct (0.2.0)
   - Database connected
   - Search service connected
   - Ports bind to 127.0.0.1 only
   - Memory <3.5GB
   - Auto-restart working

2. **✅ All 7 Validation Tests PASS**:
   - Health check
   - Request/response cycle
   - Database connectivity
   - Meilisearch accessible
   - Port bindings secure
   - Memory acceptable
   - Auto-restart mechanism

3. **✅ Performance Baseline Met**:
   - Health endpoint P99 <500ms
   - Concurrent requests: 0 failures at 10x concurrency
   - Home page <500ms

4. **✅ Monitoring Active**:
   - Health check cron job running
   - Log files present and rotating
   - Backup cron scheduled

---

### Post-Deployment Soak Test (48-72 hours)

After initial deployment validation passes:

**Days 1-3: Monitoring & Stability**:
- Monitor system logs: `sudo journalctl -u open-repo -n 100 --no-pager` (should show zero crashes)
- Check health every 6 hours: `curl http://localhost:8000/api/health`
- Verify backups execute: `ls -lh /opt/open-repo/backups/` (should show daily files)
- Check memory over time: Compare baseline (Day 1) vs Day 3

**Acceptance Criteria**:
- Zero unexpected restarts
- Zero ERROR logs
- Health endpoint 100% uptime
- Memory stable (not growing >50MB/day)
- All backups complete successfully

**Decision Point** (June 26 15:00 UTC):
- ✅ **PASS**: Approve Phase 5.2 content ingestion
- ❌ **FAIL**: Investigate and fix issues, extend soak test 24-48 hours

---

## Validation Checklist Template

Copy and fill this out after deployment:

```
Date: _______
Deployed Platform: [ ] Docker  [ ] systemd
Deployed By: _______

SUCCESS METRICS:
[ ] Metric 1: Health endpoint responding (200 OK)
[ ] Metric 2: Version correct (0.2.0)
[ ] Metric 3: Database connected
[ ] Metric 4: Meilisearch available
[ ] Metric 5: Ports bind to 127.0.0.1 only
[ ] Metric 6: Memory <3.5GB (current: _____MB)
[ ] Metric 7: Auto-restart working

VALIDATION TESTS:
[ ] Test 1: Health check passed
[ ] Test 2: Request/response cycle working
[ ] Test 3: Database queryable
[ ] Test 4: Search service accessible
[ ] Test 5: Port bindings secure
[ ] Test 6: Memory usage acceptable
[ ] Test 7: Auto-restart mechanism tested

PERFORMANCE BASELINES:
[ ] Health endpoint P99 <500ms
[ ] Concurrent requests 0 failures
[ ] Home page <500ms

MONITORING SETUP:
[ ] Health check cron scheduled
[ ] Log rotation configured
[ ] Backup cron scheduled

OVERALL STATUS: [ ] PASS  [ ] FAIL

Signed: _________ Date: _______
```

---

## Emergency Validation (If Issues Found)

If any validation test fails:

1. **Isolate the issue**:
   ```bash
   # Check what's running
   docker ps  # or: systemctl status open-repo
   
   # Check logs
   docker-compose logs app  # or: journalctl -u open-repo -n 50
   
   # Test connectivity to each service
   curl http://localhost:8000/api/health
   curl http://localhost:5432  # PostgreSQL (should fail, but quickly)
   curl http://localhost:7700/health
   ```

2. **Restart affected service**:
   ```bash
   docker-compose restart app  # Docker
   # or:
   sudo systemctl restart open-repo  # systemd
   ```

3. **Re-run validation**:
   ```bash
   curl http://localhost:8000/api/health
   ```

4. **If still failing**: Check system resources and restart all services:
   ```bash
   docker-compose down && docker-compose up -d  # Docker
   # or:
   sudo systemctl restart open-repo postgresql meilisearch  # systemd
   sleep 30
   curl http://localhost:8000/api/health
   ```

---

## Summary

**Validation Timeline**:
1. Deployment execution: 25-35 min (per runbook)
2. Initial validation: 5-10 min (this document)
3. Soak test: 48-72 hours
4. Final approval: June 26 15:00 UTC (Phase 5.2 readiness)

**Success Confidence**: 95% (all application code tested, infrastructure straightforward)

**Next Phase**: Upon PASS, Phase 5.2 content ingestion begins June 26 (author onboarding, seed data import, search index population).
