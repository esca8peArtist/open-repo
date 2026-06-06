---
title: "Open-Repo June 12, 2026 Post-Deployment Monitoring Plan"
project: open-repo
phase: 5 (final production deployment)
document_type: monitoring-plan
status: READY TO EXECUTE
created: 2026-06-06
target_deployment_date: 2026-06-12 (09:00 UTC)
active_monitoring_window: "09:00–10:00 UTC (60 minutes)"
passive_monitoring_window: "10:00 UTC onwards (24 hours)"
---

# Post-Deployment Monitoring Plan

**Deployment Date**: June 12, 2026  
**Active Monitoring Window**: 09:00–10:00 UTC (60 minutes post-deployment start)  
**Passive Monitoring Window**: 10:00 UTC onwards (24 hours minimum)  
**Monitoring Team**: Production ops / on-call engineer  
**Alert Channel**: Slack #deployments or email to ops team

---

## Section 1: 60-Minute Active Monitoring Checklist

This section covers the critical first hour immediately following deployment start (09:00 UTC deployment → 10:00 UTC completion of active monitoring).

### Phase 1: Minutes 0–5 (Health Endpoint Verification)

**Objective**: Confirm application is running and responding to requests.

**Commands**:
```bash
# Test health endpoint
curl -s -w "\nHTTP Status: %{http_code}\nTime: %{time_total}s\n" \
  http://100.70.184.84:8000/health | jq .
```

**Expected Output**:
```json
{
  "status": "ok",
  "timestamp": "2026-06-12T09:XX:XXZ"
}

HTTP Status: 200
Time: 0.15s
```

**Success Criteria**:
- HTTP Status: **200**
- Response time: **< 200ms** (critical: >500ms indicates performance degradation)
- JSON includes both `status` and `timestamp` fields
- Status value is "ok" or "healthy"

**Failure Response**:
- If HTTP 500: Application crash detected → Check logs immediately: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 50'`
- If HTTP 502/503: Service misconfiguration → Check if service is actually running: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo systemctl status open-repo'`
- If timeout (>5s): Network issue or service deadlock → Try again once; if persists, check network connectivity
- If response time >500ms: Performance issue detected → Monitor closely in subsequent phases

**Action if Failure**: 
- Log failure timestamp and error
- Check "Incident Response Playbook" at end of this document
- If CRITICAL (timeout, 500, 502/503), escalate to rollback decision immediately

---

### Phase 2: Minutes 5–15 (Endpoint Verification)

**Objective**: Verify all critical endpoints are responding with correct HTTP status codes and reasonable latency.

#### 2a: Swagger UI Endpoint (/docs)

```bash
# Test Swagger UI loads
curl -s -w "\nHTTP Status: %{http_code}\nTime: %{time_total}s\n" \
  http://100.70.184.84:8000/docs | head -50
```

**Expected Output**: HTML page containing "swagger" text, HTTP 200, response time <500ms  
**Success Criteria**:
- HTTP Status: **200**
- Response time: **< 500ms**
- Content contains "swagger" or "swagger-ui" (case-insensitive)

**Threshold Violations**:
- HTTP 500 or 502 → WARN: Check app logs
- Response time 500–2000ms → WARN: Monitor performance
- Response time >2000ms → CRITICAL: Consider rollback

#### 2b: ReDoc Endpoint (/redoc)

```bash
# Test ReDoc loads
curl -s -w "\nHTTP Status: %{http_code}\nTime: %{time_total}s\n" \
  http://100.70.184.84:8000/redoc | head -50
```

**Expected Output**: HTML page containing "redoc" text, HTTP 200, response time <500ms  
**Success Criteria**:
- HTTP Status: **200**
- Response time: **< 500ms**
- Content contains "redoc" or "ReDoc" (case-insensitive)

**Threshold Violations**: Same as Swagger UI above

#### 2c: OPDS Root Endpoint (/api/v2/opds/root.xml)

```bash
# Test OPDS root catalog
curl -s -H "Accept: application/atom+xml" \
  -w "\nHTTP Status: %{http_code}\nTime: %{time_total}s\nContent-Type: %{content_type}\n" \
  http://100.70.184.84:8000/api/v2/opds/root.xml | head -10
```

**Expected Output**: XML document starting with `<?xml version="1.0"...`, HTTP 200, Content-Type includes "atom+xml", response time <1s  
**Success Criteria**:
- HTTP Status: **200**
- Response time: **< 1000ms** (OPDS can be slower due to database access)
- Content-Type header includes "atom+xml"
- First line is valid XML declaration

**Threshold Violations**:
- HTTP 500 or 502 → WARN: OPDS generator may have crashed, check logs
- Response time 1–5s → WARN: Database latency issue, monitor
- Response time >5s → CRITICAL: Rollback decision needed

#### 2d: OPDS Acquisition Feed Endpoint (/api/v2/opds/entries)

```bash
# Test OPDS acquisition feed
curl -s -H "Accept: application/atom+xml" \
  -w "\nHTTP Status: %{http_code}\nTime: %{time_total}s\nContent-Type: %{content_type}\n" \
  http://100.70.184.84:8000/api/v2/opds/entries | head -10
```

**Expected Output**: Same as root, but with `<feed>` and/or `<entry>` elements  
**Success Criteria**: Same as root endpoint above

**Overall Phase 2 Decision**:
- All 4 endpoints HTTP 200 with <500ms response time → PROCEED
- Any endpoint HTTP 500 → WARN, monitor closely
- Any endpoint response time 500–2000ms → WARN, may indicate database issue
- Any endpoint response time >2000ms or timeout → CRITICAL, escalate

---

### Phase 3: Minutes 15–30 (Traffic Baseline & Error Rate Establishment)

**Objective**: Establish baseline metrics and confirm no widespread errors are occurring.

#### 3a: Request Rate Monitoring

```bash
# Count requests in last 60 seconds (from app logs)
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  sudo journalctl -u open-repo --since "1 minute ago" | grep -c "GET\|POST\|PUT\|DELETE" || echo "0"
EOF
```

**Expected Output**: Request count (typically low immediately post-deployment, should be <10 requests if no users yet)  
**Success Criteria**:
- Request rate is consistent (not increasing unexpectedly)
- No spike in requests (would indicate load test or user discovery)

**Threshold Violations**:
- Sudden spike >100 requests/min → WARN: Unexpected traffic load, monitor closely
- Continuous >500 requests/min → CRITICAL: Either load testing or system misconfiguration

#### 3b: Error Rate Monitoring

```bash
# Count errors in last 5 minutes
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  TOTAL=$(sudo journalctl -u open-repo --since "5 minutes ago" | grep -E "GET|POST|PUT|DELETE" | wc -l)
  ERRORS=$(sudo journalctl -u open-repo --since "5 minutes ago" | grep -E "500|502|503|error|ERROR|CRITICAL" | wc -l)
  
  if [ "$TOTAL" -gt 0 ]; then
    ERROR_RATE=$((ERRORS * 100 / TOTAL))
    echo "Error rate: $ERROR_RATE% ($ERRORS/$TOTAL)"
  else
    echo "No requests logged"
  fi
EOF
```

**Expected Output**: "Error rate: 0% (0/X)" or similar showing very low error percentage  
**Success Criteria**:
- Error rate: **< 1%** (healthy state)
- No spike in errors

**Threshold Violations**:
- Error rate 1–5% → WARN: Minor issue detected, monitor
- Error rate 5–10% → WARN: Significant errors, investigate root cause
- Error rate >10% → CRITICAL: Widespread failure, escalate to rollback
- Error rate >20% → CRITICAL: System-wide failure, rollback immediately

#### 3c: Log Analysis for Anomalies

```bash
# Show all log entries from last 15 minutes (real-time monitoring)
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  sudo journalctl -u open-repo --since "15 minutes ago" | tail -100
EOF
```

**Expected Output**: Normal application startup messages, request logs, no ERROR or CRITICAL entries

**Success Criteria**:
- No ERROR-level messages related to A11y, OPDS, CSS/JS loading
- No database connection errors
- No 500/502 response codes

**Common Non-Critical Log Entries**:
- "Application startup complete" → OK
- "GET /health HTTP/1.1 200" → OK
- "GET /docs HTTP/1.1 200" → OK
- "Uvicorn server listening on 127.0.0.1:8000" → OK

**Critical Log Entries** (escalate immediately):
- "CRITICAL" or "ERROR" messages
- "database connection failed"
- "500 Internal Server Error"
- "OPDS initialization failed"
- "CSS/JavaScript injection failed"

---

### Phase 4: Minutes 30–60 (Extended Monitoring & System Health)

**Objective**: Confirm sustained stability and verify system resources are not exhausted.

#### 4a: Periodic Health Check Loop

```bash
# Run health check every 5 minutes for remaining 30 minutes
for i in {1..6}; do
  echo "--- Health check iteration $i ($(date +%H:%M:%S UTC)) ---"
  
  # Health endpoint
  HEALTH=$(curl -s -w "%{http_code}" http://100.70.184.84:8000/health)
  if [[ "$HEALTH" == *"200"* ]]; then
    echo "Health: OK (200)"
  else
    echo "Health: FAIL ($(echo $HEALTH | tail -c 4))"
  fi
  
  # OPDS root endpoint
  OPDS=$(curl -s -w "%{http_code}" -H "Accept: application/atom+xml" \
    http://100.70.184.84:8000/api/v2/opds/root.xml)
  if [[ "$OPDS" == *"200"* ]]; then
    echo "OPDS: OK (200)"
  else
    echo "OPDS: FAIL ($(echo $OPDS | tail -c 4))"
  fi
  
  sleep 300  # Wait 5 minutes before next check
done
```

**Expected Output**: All iterations show "OK (200)" for both endpoints  
**Success Criteria**:
- All 6 iterations show health endpoint HTTP 200
- All 6 iterations show OPDS endpoint HTTP 200
- No changes between iterations

**Threshold Violations**:
- Any iteration shows non-200 status → CRITICAL: Intermittent failures detected, escalate
- Degrading response times → WARN: System getting slower, may need investigation

#### 4b: CPU Usage Monitoring

```bash
# Check CPU usage on production host
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  # Show top 3 processes by CPU
  ps aux --sort=-%cpu | head -4
  
  # Show overall CPU idle percentage
  top -bn1 | grep "Cpu(s)" | awk '{print "CPU idle: " $8 "%"}'
EOF
```

**Expected Output**:
```
USER  PID  %CPU  %MEM  COMMAND
...
CPU idle: 85%
```

**Success Criteria**:
- CPU idle > 50% (plenty of headroom)
- No single process consuming >30% CPU

**Threshold Violations**:
- CPU idle 20–50% → WARN: Moderate CPU load, monitor
- CPU idle <20% → CRITICAL: High CPU usage, investigate
- Any process >80% CPU → CRITICAL: Runaway process, investigate/kill

#### 4c: Memory Usage Monitoring

```bash
# Check memory usage
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  free -h | grep Mem
  # Show top 3 processes by memory
  ps aux --sort=-%mem | head -4
EOF
```

**Expected Output**:
```
Mem:   7.7Gi    1.2Gi    2.1Gi
PID    %MEM    COMMAND
...
```

**Success Criteria**:
- Available memory > 2GB
- Used memory < 85% of total
- No single process consuming > 50% memory

**Threshold Violations**:
- Available memory 1–2GB → WARN: Low memory, monitor closely
- Available memory < 1GB → CRITICAL: Risk of OOM killer, investigate
- Used memory >95% → CRITICAL: Potential memory leak, escalate

#### 4d: Disk Space Monitoring

```bash
# Check disk usage
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  df -h /
EOF
```

**Expected Output**:
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       30G   5G   25G  17% /
```

**Success Criteria**:
- Available disk space > 10GB
- Used space < 80% of total

**Threshold Violations**:
- Available disk 5–10GB → WARN: Low disk space, check logs for growth
- Available disk < 5GB → CRITICAL: Critical disk space shortage, may cause service crash
- Used space >95% → CRITICAL: Investigate and free space immediately

#### 4e: Database Connectivity & Query Performance

```bash
# Test database connectivity (if database is deployed)
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  # Check if app logs show any database errors
  sudo journalctl -u open-repo --since "30 minutes ago" | \
    grep -i "database\|postgres\|sqlite\|connection" || echo "No database entries"
  
  # Alternative: if database port is accessible, test directly
  # (requires db credentials; adjust for your setup)
  # psql -h [db_host] -U [user] -d [db_name] -c "SELECT COUNT(*) FROM [table]"
EOF
```

**Expected Output**: No error messages about database connectivity

**Success Criteria**:
- No "database connection failed" messages
- No "timeout" messages related to queries
- Application logs show normal database interaction

**Threshold Violations**:
- "database connection failed" → CRITICAL: Database is down or unreachable, investigate
- Multiple "timeout" messages → CRITICAL: Database responding very slowly, may need rollback
- "connection pool exhausted" → CRITICAL: Database connections running out, investigate leak

---

## Section 2: Alert Thresholds & Escalation

This section defines specific numeric thresholds for all critical metrics. When a threshold is breached, follow the escalation procedure.

### Response Time Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| Health endpoint response time | <200ms | OK |
| Health endpoint response time | 200–500ms | WARN: Monitor closely |
| Health endpoint response time | 500–2000ms | WARN: Likely database latency |
| Health endpoint response time | >2000ms or timeout | CRITICAL: Rollback decision |
| | | |
| /docs, /redoc response time | <500ms | OK |
| /docs, /redoc response time | 500–2000ms | WARN: Possible infrastructure issue |
| /docs, /redoc response time | >2000ms | CRITICAL: Rollback decision |
| | | |
| OPDS endpoint response time | <1000ms | OK |
| OPDS endpoint response time | 1000–5000ms | WARN: Database query slow |
| OPDS endpoint response time | >5000ms or timeout | CRITICAL: Rollback decision |

### Error Rate Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| Overall error rate | <1% | OK |
| Overall error rate | 1–5% | WARN: Monitor, check logs |
| Overall error rate | 5–10% | WARN: Significant failures, investigate |
| Overall error rate | 10–20% | CRITICAL: Widespread issue, prepare rollback |
| Overall error rate | >20% | CRITICAL: System failure, rollback immediately |
| | | |
| 5XX error rate (500/502/503) | 0% | OK |
| 5XX error rate | 1–3% | WARN: Minor failures |
| 5XX error rate | >3% | CRITICAL: Application errors, escalate |

### CPU Usage Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| CPU idle percentage | >50% | OK (plenty of headroom) |
| CPU idle percentage | 20–50% | WARN: Moderate load, monitor |
| CPU idle percentage | <20% | CRITICAL: High CPU, investigate |
| | | |
| Single process CPU usage | <30% | OK |
| Single process CPU usage | 30–50% | WARN: Process consuming significant CPU |
| Single process CPU usage | >80% | CRITICAL: Runaway process, stop it |

### Memory Usage Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| Memory available | >2GB | OK |
| Memory available | 1–2GB | WARN: Low memory, monitor |
| Memory available | <1GB | CRITICAL: Risk of OOM, escalate |
| | | |
| Memory used percentage | <85% | OK |
| Memory used percentage | 85–95% | WARN: Possible memory leak |
| Memory used percentage | >95% | CRITICAL: Near OOM condition |

### Disk Space Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| Disk available | >10GB | OK |
| Disk available | 5–10GB | WARN: Low disk space |
| Disk available | <5GB | CRITICAL: Critical shortage |
| | | |
| Disk used percentage | <80% | OK |
| Disk used percentage | 80–95% | WARN: High usage |
| Disk used percentage | >95% | CRITICAL: Critical full |

### Database Query Latency Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| Database query execution time | <100ms | OK |
| Database query execution time | 100–1000ms | WARN: Slow queries, monitor |
| Database query execution time | >1000ms | CRITICAL: Database bottleneck, investigate |
| | | |
| Database connection latency | <50ms | OK |
| Database connection latency | 50–500ms | WARN: Network latency |
| Database connection latency | >500ms | CRITICAL: Connection issue |

### Request Timeout Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| Request timeouts | 0 per 5 min | OK |
| Request timeouts | 1–2 per 5 min | WARN: Minor timeouts, investigate |
| Request timeouts | >2 per 5 min | CRITICAL: Widespread timeout, escalate |

---

### Escalation Procedure for Threshold Breaches

When any threshold is breached:

1. **WARN Condition** (yellow alert):
   - Log the issue with timestamp and metric value
   - Increase monitoring frequency from 5 min to 1 min
   - Check application logs for root cause
   - If issue persists for 10+ minutes, escalate to CRITICAL
   - Continue monitoring but do not trigger rollback unless escalates

2. **CRITICAL Condition** (red alert):
   - Log immediately with timestamp, metric value, and context
   - Execute incident response playbook (see Section 4)
   - Notify on-call engineer and team lead
   - Prepare for rollback (have backup verified and ready)
   - If issue cannot be resolved in 5 minutes, execute rollback
   - If issue is data-related (database) vs. code-related, prioritize rollback

3. **Post-Escalation**:
   - Do not attempt fixes during deployment window (increases risk)
   - Document what triggered escalation
   - Execute rollback if within 60-minute active monitoring window
   - If outside active window (after 10:00 UTC), follow 24-hour passive monitoring procedures

---

## Section 3: 24-Hour Passive Monitoring Plan

This section covers monitoring after the 60-minute active monitoring window (10:00 UTC onwards).

### Monitoring Schedule

**Hours 1–8 (10:00–18:00 UTC on June 12)**:
- Check key metrics every 1 hour
- Review logs for errors
- Alert on any CRITICAL threshold

**Hours 8–24 (18:00 UTC June 12 – 09:00 UTC June 13)**:
- Check key metrics every 2 hours
- Review logs for patterns
- Alert on sustained errors (>5 in 24hr window)

**After 24 hours (from 09:00 UTC June 13)**:
- Switch to normal operational monitoring
- Daily review of deployment metrics
- Archive monitoring logs

### Log Aggregation & Collection

**Primary Log Location**: Application logs from systemd journal

```bash
# View application logs in real-time
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  'sudo journalctl -u open-repo -f'

# Export logs to file for analysis
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  'sudo journalctl -u open-repo --since "2026-06-12 09:00" --until "2026-06-13 09:00" > /tmp/open-repo-deployment-logs.txt'

# Copy logs to local machine
scp -i ~/.ssh/production_key ubuntu@100.70.184.84:/tmp/open-repo-deployment-logs.txt ./deployment-logs-june12.txt
```

**Secondary Log Locations** (if configured):
- Application error logs: `/var/log/open-repo/error.log` (if configured)
- Web server logs: `/var/log/nginx/access.log` (if using nginx reverse proxy)
- System logs: `/var/log/syslog`

### Passive Monitoring Checklist (Every 1 Hour for First 8 Hours)

Create a checklist file to track hourly monitoring:

```
Monitoring Log: June 12, 2026 — Open-Repo Deployment

10:00 UTC: [ ] Health check [ ] Error rate [ ] Resources [ ] Logs reviewed
11:00 UTC: [ ] Health check [ ] Error rate [ ] Resources [ ] Logs reviewed
12:00 UTC: [ ] Health check [ ] Error rate [ ] Resources [ ] Logs reviewed
13:00 UTC: [ ] Health check [ ] Error rate [ ] Resources [ ] Logs reviewed
14:00 UTC: [ ] Health check [ ] Error rate [ ] Resources [ ] Logs reviewed
15:00 UTC: [ ] Health check [ ] Error rate [ ] Resources [ ] Logs reviewed
16:00 UTC: [ ] Health check [ ] Error rate [ ] Resources [ ] Logs reviewed
17:00 UTC: [ ] Health check [ ] Error rate [ ] Resources [ ] Logs reviewed
18:00 UTC: Transition to 2-hour schedule

Notes:
-------
```

**Hourly Check Template** (use for each hour):

```bash
#!/bin/bash
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

echo "=== Hourly Monitoring Check: $TIMESTAMP ==="

# 1. Health check
echo "1. Health endpoint:"
curl -s -w "HTTP %{http_code} | Time: %{time_total}s\n" \
  http://100.70.184.84:8000/health | tail -1

# 2. Error rate (last hour)
echo "2. Error rate (last 60 min):"
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  TOTAL=$(sudo journalctl -u open-repo --since "60 min ago" | \
    grep -E "GET|POST|PUT|DELETE" | wc -l)
  ERRORS=$(sudo journalctl -u open-repo --since "60 min ago" | \
    grep -E "500|502|503" | wc -l)
  if [ "$TOTAL" -gt 0 ]; then
    PCT=$((ERRORS * 100 / TOTAL))
    echo "$PCT% ($ERRORS/$TOTAL)"
  else
    echo "No requests"
  fi
EOF

# 3. System resources
echo "3. System resources:"
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  echo "CPU idle: $(top -bn1 | grep "Cpu(s)" | awk '{print $8 "%"}')"
  echo "Memory available: $(free -h | grep Mem | awk '{print $7}')"
  echo "Disk available: $(df -h / | tail -1 | awk '{print $4}')"
EOF

# 4. Recent errors (last 30 min)
echo "4. Recent errors (last 30 min):"
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 \
  'sudo journalctl -u open-repo --since "30 min ago" | grep -i "error\|critical" | tail -3 || echo "None"'

echo ""
```

Save as `/tmp/open-repo-monitoring.sh` and run hourly:
```bash
bash /tmp/open-repo-monitoring.sh >> /tmp/open-repo-passive-monitoring.log
```

### Key Metrics to Track (24-Hour Window)

Record these metrics every hour for first 8 hours, then every 2 hours:

1. **Error Rate**: Daily total, should trend toward 0%
2. **Response Times**: Average, p95, p99 (if metrics available)
3. **Request Count**: Daily total (indicates user adoption)
4. **Database Query Latency**: Average, max (if available)
5. **System Resources**: CPU, memory, disk (trend line)
6. **Unique Error Types**: Count distinct errors seen

### Monitoring Dashboard (If Available)

If you have access to a monitoring tool (Prometheus, DataDog, New Relic, etc.), create a simple dashboard:

**Dashboard Name**: "Open-Repo June 12 Deployment"

**Dashboard Panels**:

1. **Error Rate Over Time** (line chart)
   - X-axis: Time (UTC)
   - Y-axis: Error rate (%)
   - Alert line at 5%
   - Duration: 24 hours from 09:00 UTC June 12

2. **Response Time Distribution** (histogram or line chart)
   - X-axis: Time (UTC)
   - Y-axis: Response time (ms)
   - Show separate lines for /health, /docs, /api/v2/opds/root.xml
   - Threshold line at 500ms and 2000ms

3. **Request Volume** (bar or area chart)
   - X-axis: Time (hourly buckets)
   - Y-axis: Request count
   - Useful for detecting unexpected traffic spikes

4. **System Resources** (gauge or line chart)
   - CPU idle percentage (should be >50%)
   - Memory available (GB, should be >2GB)
   - Disk free (GB, should be >10GB)

5. **Request Status Codes** (stacked bar chart)
   - X-axis: Time (hourly)
   - Y-axis: Request count
   - Stacked by status code (2xx, 3xx, 4xx, 5xx)
   - All 5xx should be near 0%

6. **Top Errors** (table)
   - Error message
   - Count
   - Last seen
   - Update every hour

### Alert Configuration for Monitoring Tool

If using a monitoring tool, configure these alerts:

```
Alert: High Error Rate
Condition: error_rate > 5% for 5 minutes
Severity: CRITICAL
Action: Email ops team, ping Slack #deployments

Alert: Slow Response Time
Condition: response_time_p95 > 2000ms for 5 minutes
Severity: WARN
Action: Email ops team

Alert: Low Memory
Condition: memory_available < 1GB
Severity: CRITICAL
Action: Email ops team, page on-call

Alert: Low Disk Space
Condition: disk_free < 5GB
Severity: CRITICAL
Action: Email ops team, page on-call

Alert: High CPU
Condition: cpu_idle < 20% for 10 minutes
Severity: WARN
Action: Email ops team
```

### Alert Destinations

**Primary**: Slack #deployments channel
- Create webhook: `https://hooks.slack.com/services/YOUR/WEBHOOK/HERE`
- Message format: `[DEPLOYMENT] Alert: High Error Rate (8.3%) at 12:15 UTC — Check: <url-to-dashboard>`

**Secondary**: Email to ops team
- Recipients: ops@company.com, oncall@company.com
- Subject: `[ALERT] Open-Repo Deployment Issue at 12:15 UTC`

**Tertiary**: SMS/Page (for CRITICAL only)
- Reserved for CRITICAL alerts only (error rate >10%, response time >5s, system down)

---

## Section 4: Incident Response Playbook

This playbook defines actions to take when alerts trigger during the 60-minute active monitoring window and 24-hour passive monitoring period.

### Incident Response Trigger Conditions

An "incident" is declared when any of these conditions occur:

1. **Health Check Failure**: `/health` endpoint returns non-200 or timeout
2. **Endpoint Error**: Any critical endpoint (/docs, /redoc, /api/v2/opds/*) returns 500 or times out
3. **Error Rate Spike**: Error rate exceeds 5% (WARN) or 10% (CRITICAL)
4. **Response Time Spike**: Any endpoint exceeds 2000ms (CRITICAL) or 5000ms (ROLLBACK)
5. **Resource Exhaustion**: CPU idle <20%, memory available <1GB, disk free <5GB
6. **Database Connectivity Loss**: Database connection errors appear in logs

### Incident Response Workflow

**WARN Incident (Yellow Alert)** – Response Time: 5 minutes

```
1. DETECT & LOG
   └─ Record timestamp, metric name, value, threshold
   
2. INVESTIGATE (max 5 minutes)
   ├─ Check application logs (last 50 lines)
   ├─ Verify endpoint is actually failing (test twice)
   ├─ Check system resources (CPU, memory, disk)
   └─ Determine: Code issue vs. Infrastructure issue vs. External (DB)

3. ACTION
   ├─ If Code Issue:
   │  └─ Check recent commits, review changes
   │  └─ If clear cause, document for post-deployment review
   ├─ If Infrastructure Issue:
   │  └─ Check network connectivity
   │  └─ Restart service if safe: sudo systemctl restart open-repo
   ├─ If External (DB):
   │  └─ Verify database is reachable
   │  └─ Check database logs
   │  └─ Escalate to database team if not responding
   
4. CONTINUE MONITORING
   └─ Increase check frequency to every 1 minute
   └─ Re-test affected endpoints every 30 seconds
   └─ If issue persists 10+ minutes, escalate to CRITICAL
```

**CRITICAL Incident (Red Alert)** – Response Time: 2 minutes → Rollback Decision

```
1. IMMEDIATE ACTIONS
   ├─ Record timestamp, issue, context
   ├─ Notify on-call engineer (Slack ping + phone call)
   ├─ Notify team lead
   └─ Pause any ongoing deployments/changes

2. ROOT CAUSE ANALYSIS (max 3 minutes)
   ├─ Is it a code problem?
   │  └─ Check application crash in logs
   │  └─ Did recent code change break something?
   ├─ Is it a database problem?
   │  └─ Can the app connect to the database?
   │  └─ Are queries hanging or returning 500?
   ├─ Is it infrastructure?
   │  └─ Network connectivity lost?
   │  └─ Disk full?
   │  └─ OOM killer activated?
   └─ If root cause unclear, escalate to ROLLBACK (fail-safe)

3. DECISION POINT (< 5 min from incident start)
   ├─ IF: Can fix quickly (e.g., restart service, clear logs)
   │  └─ Attempt fix, re-test immediately
   │  └─ If fixed, document fix and continue monitoring
   │  └─ If not fixed after 2 min, escalate to ROLLBACK
   │
   ├─ IF: Root cause is unknown
   │  └─ EXECUTE ROLLBACK immediately (fail-safe)
   │
   ├─ IF: Multiple systems failing
   │  └─ EXECUTE ROLLBACK immediately
   │
   └─ IF: Data/database is corrupted
       └─ EXECUTE ROLLBACK immediately

4. ESCALATION
   └─ If not resolved in 5 minutes, go to ROLLBACK PROCEDURE
```

### ROLLBACK Procedure

Rollback is the fail-safe mechanism when a CRITICAL incident cannot be resolved in 5 minutes.

**Decision Point**: ROLLBACK → Check DEPLOYMENT_JUNE_12_RUNBOOK.md "Rollback Procedure" section

**Key Steps** (extract from main runbook, see that document for full details):

1. Stop the currently deployed application
2. Restore from pre-deployment backup
3. Restart previous version
4. Re-run post-deployment health checks
5. Notify all stakeholders
6. Create incident report

**Rollback Timeline**: Should complete in 5–10 minutes

**Post-Rollback Actions**:
- Send "ROLLBACK EXECUTED" notification to team
- Do NOT attempt re-deployment immediately
- Schedule post-mortem within 24 hours
- Document root cause and prevention steps

### Post-Incident Review (After 24 Hours)

Once 24-hour passive monitoring is complete, conduct post-incident review:

1. **Collect Metrics**:
   - Total error rate over 24 hours (should be near 0%)
   - Max response time observed
   - Resource usage peak values
   - Any errors encountered

2. **Determine Impact**:
   - Was deployment successful? YES / NO
   - If rollback occurred, was it appropriate?
   - Were any users affected? If so, how many?

3. **Document Findings**:
   - Create incident report
   - List all errors encountered
   - Identify if systematic issue or one-off
   - Recommend preventive measures

4. **Archive Data**:
   - Save monitoring logs
   - Export dashboard metrics
   - Save application logs from deployment window

---

## Quick Reference: Alert Decision Tree

```
ALERT TRIGGERED
    ↓
Is it CRITICAL (response timeout, 500 error, rollback threshold)?
    │
    ├─ YES → Escalate immediately, prepare rollback
    │         Follow CRITICAL response procedure
    │         Decision: Fix or Rollback (within 5 min)
    │
    └─ NO (WARN condition)
         → Log issue, investigate root cause
         → Increase monitoring frequency
         → If persists 10+ min, escalate to CRITICAL
```

---

## Appendix: Monitoring Commands Quick Reference

**Fast Health Check** (copy-paste ready):
```bash
echo "Health:" && curl -s http://100.70.184.84:8000/health | jq .status
echo "OPDS:" && curl -s -I -H "Accept: application/atom+xml" http://100.70.184.84:8000/api/v2/opds/root.xml | head -1
echo "Time: $(date -u +%H:%M:%S)" && echo "Resources:" && \
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'free -h | grep Mem && df -h / | tail -1'
```

**Full Monitoring Check** (1-min execution):
```bash
bash /tmp/open-repo-monitoring.sh
```

**Emergency Log Access**:
```bash
# Real-time log stream
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -f'

# Last 100 lines
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 100'

# Last hour
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo --since "1 hour ago"'
```

---

**Monitoring Plan Version**: 1.0  
**Created**: June 6, 2026  
**Valid For**: June 12, 2026 deployment  
**Last Updated**: June 6, 2026
