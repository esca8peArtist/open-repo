---
title: "Open-Repo June 12, 2026 Post-Incident Audit Checklist"
project: open-repo
phase: 5 (final production deployment)
document_type: post-incident-audit
status: PRODUCTION READY
created: 2026-06-06
target_deployment_date: 2026-06-12 (09:00 UTC)
deployment_window: "09:00–10:45 UTC"
audit_window: "Collect within 2 hours of incident; analyze within 24 hours"
---

# Post-Incident Audit Checklist — June 12, 2026

**Purpose**: Structured evidence collection and root-cause analysis framework for any incident occurring during or after the June 12 deployment. Applies whether the deployment resulted in rollback, partial success, or a degraded-but-running state.

**When to use this document**:
- Immediately after any CRITICAL alert fires during the 09:00–10:45 UTC active monitoring window
- After any rollback execution
- At end of 24-hour passive monitoring period (June 13, 09:00 UTC) if any anomalies occurred
- Even for successful deployments with minor WARNs — to capture the baseline for future reference

**Minimum retention**: Keep all collected evidence for 30 days after deployment. The data is needed if a user-reported issue emerges days after deployment.

---

## Part 1: Immediate Evidence Preservation (Run Within 30 Minutes of Incident)

These steps must run while the system state is still fresh. Log and timestamp files fill up and rotate; evidence is lost if not collected immediately.

### 1.1 Capture Current System State Snapshot

Run this immediately when an incident is declared or when the deployment window closes (whichever comes first):

```bash
# Run from local machine; output will be your primary evidence file
INCIDENT_TIMESTAMP=$(date -u +%Y%m%d-%H%M%S)
EVIDENCE_FILE="/tmp/open-repo-incident-${INCIDENT_TIMESTAMP}.txt"

echo "=== INCIDENT EVIDENCE SNAPSHOT: $INCIDENT_TIMESTAMP UTC ===" > "$EVIDENCE_FILE"
echo "Captured by: $(whoami) on $(hostname)" >> "$EVIDENCE_FILE"
echo "" >> "$EVIDENCE_FILE"

# Service status
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF' >> "$EVIDENCE_FILE"
echo "=== SERVICE STATUS ==="
sudo systemctl status open-repo

echo ""
echo "=== LAST 100 APPLICATION LOG LINES ==="
sudo journalctl -u open-repo -n 100

echo ""
echo "=== CPU + MEMORY + DISK ==="
top -bn1 | head -10
free -h
df -h /

echo ""
echo "=== TOP PROCESSES ==="
ps aux --sort=-%cpu | head -10

echo ""
echo "=== RECENT OOM EVENTS ==="
sudo dmesg | grep -i "oom\|killed" | tail -10 || echo "None"

echo ""
echo "=== GIT STATE ==="
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
git log --oneline -5
git status

echo ""
echo "=== MIGRATION STATE ==="
cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
source /opt/venv/open-repo/bin/activate 2>/dev/null
alembic current 2>&1 || echo "Alembic not available or failed"
EOF

echo "Evidence snapshot saved to: $EVIDENCE_FILE"
```

Copy this file off the local machine immediately:
```bash
cp "$EVIDENCE_FILE" ~/open-repo-incidents/
```

Treat this file as the primary audit artifact. It cannot be reconstructed after log rotation.

---

### 1.2 Application Log Collection (Full Deployment Window)

Collect the complete application log from 09:00–10:45 UTC, regardless of whether the deployment succeeded.

```bash
# On production host: export full deployment window logs
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
echo "Exporting deployment window logs..."
sudo journalctl -u open-repo \
  --since "2026-06-12 09:00:00" \
  --until "2026-06-12 10:45:00" \
  --output json \
  > /tmp/open-repo-deployment-logs-json.txt

sudo journalctl -u open-repo \
  --since "2026-06-12 09:00:00" \
  --until "2026-06-12 10:45:00" \
  > /tmp/open-repo-deployment-logs-text.txt

wc -l /tmp/open-repo-deployment-logs-text.txt
echo "Log export complete"
EOF

# Copy logs to local machine for analysis
rsync -avz -e "ssh -i ~/.ssh/production_key" \
  ubuntu@100.70.184.84:/tmp/open-repo-deployment-logs-text.txt \
  ~/open-repo-incidents/deployment-logs-june12.txt

rsync -avz -e "ssh -i ~/.ssh/production_key" \
  ubuntu@100.70.184.84:/tmp/open-repo-deployment-logs-json.txt \
  ~/open-repo-incidents/deployment-logs-june12.json
```

Checkbox log collection confirmation:
- [ ] Text log exported (open-repo-deployment-logs-text.txt)
- [ ] JSON log exported (open-repo-deployment-logs-json.txt)
- [ ] Both copied to local machine or persistent storage
- [ ] Line count noted: __________ lines

---

### 1.3 Database Transaction Log Collection

```bash
# For SQLite: capture schema state and any WAL (write-ahead log) state
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
echo "=== DATABASE STATE AT AUDIT TIME ==="
echo "SQLite file info:"
ls -lah /path/to/database.db 2>/dev/null || echo "Database file not found"
ls -lah /path/to/database.db-wal 2>/dev/null || echo "No WAL file"
ls -lah /path/to/database.db-shm 2>/dev/null || echo "No SHM file"

echo ""
echo "Schema:"
sqlite3 /path/to/database.db ".schema" 2>/dev/null || echo "Cannot read schema"

echo ""
echo "Table row counts:"
sqlite3 /path/to/database.db "SELECT name, (SELECT COUNT(*) FROM name) FROM sqlite_master WHERE type='table';" 2>/dev/null || echo "Cannot query tables"
EOF

# For PostgreSQL: capture connection logs from postgres itself
# ssh ubuntu@100.70.184.84 'sudo journalctl -u postgresql --since "2026-06-12 09:00" | tail -100'
```

Checkbox database log confirmation:
- [ ] Database file size recorded: __________ 
- [ ] Schema captured
- [ ] WAL file presence noted (if present, migration may have been incomplete)
- [ ] Row counts captured for key tables

---

### 1.4 Screenshot / Command Output Preservation

For any alert that fired during the deployment window, preserve the exact command output that triggered the alert. Record these in a plain text file with timestamps.

**Template for each alert event**:

```
ALERT EVENT RECORD
------------------
Time (UTC):          [e.g., 09:47:23]
Alert type:          [e.g., OPDS 500 / Response time CRITICAL / Error rate >10%]
Severity:            [WARN / CRITICAL]
Triggered by:        [e.g., curl command output / log grep / monitoring tool]

Command run:
  [paste exact command]

Output received:
  [paste exact output]

Initial assessment:
  [1–2 sentences on what the output indicated]

Action taken:
  [what was done in response]

Timestamp of resolution or escalation:
  [UTC timestamp]
```

Create one ALERT EVENT RECORD per distinct alert. Save all records to `~/open-repo-incidents/alert-events-june12.txt`.

---

### 1.5 Metrics Retention (90-Minute Active Window)

If Prometheus or any other monitoring tool was running, export the 09:00–10:45 UTC window immediately. Monitoring data often has short retention windows.

```bash
# If using Prometheus: export 90-min window
# curl -G 'http://localhost:9090/api/v1/query_range' \
#   --data-urlencode 'query=process_cpu_seconds_total' \
#   --data-urlencode 'start=2026-06-12T09:00:00Z' \
#   --data-urlencode 'end=2026-06-12T10:45:00Z' \
#   --data-urlencode 'step=15s' \
#   > ~/open-repo-incidents/prometheus-cpu-june12.json

# Manual metrics alternative: run the monitoring script output log
# This was started as: bash /tmp/open-repo-monitoring.sh >> /tmp/open-repo-passive-monitoring.log
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'cat /tmp/open-repo-passive-monitoring.log' \
  > ~/open-repo-incidents/monitoring-script-output-june12.txt 2>/dev/null || echo "No monitoring script log found"
```

Checkbox metrics retention:
- [ ] Prometheus/monitoring data exported (if available)
- [ ] Manual monitoring script log captured
- [ ] Response time measurements recorded per endpoint (from health check iterations)
- [ ] Peak CPU, memory, disk values recorded

---

## Part 2: Root-Cause Investigation Template

Complete this section within 24 hours of the incident. The 5-Why drill-down is not optional — "what happened" is insufficient; the goal is "why it will not happen again".

### 2.1 Incident Timeline Reconstruction

Reconstruct events in chronological order. Use log timestamps, not recollection.

```
INCIDENT TIMELINE — June 12, 2026
-----------------------------------

09:00 UTC   Deployment window opened
            Git state: [commit hash]
            Service state: stopped (Step 2 completed)

09:10 UTC   Pre-flight checks: [PASSED / FAILED — note which]

[fill in actual deployment step timestamps from execution]

[TIME] UTC  First anomaly observed:
            What: [e.g., "OPDS returned HTTP 500"]
            Source: [e.g., "Phase 2 endpoint check" / "monitoring alert"]
            Initial response: [e.g., "Checked logs, saw OPDSGenerator error"]

[TIME] UTC  Second alert (if cascade):
            What: [e.g., "Error rate crossed 10%"]
            Relationship to first alert: [same root cause / separate issue]

[TIME] UTC  Decision point reached:
            Decision: [rollback / continue monitoring / restart service]
            Rationale: [why this decision was made]

[TIME] UTC  Action taken:
            [exact steps executed]

[TIME] UTC  Outcome:
            [service restored / rollback completed / escalated]

10:45 UTC   Active monitoring window closed
            Final state: [healthy / degraded / rolled back]
```

---

### 2.2 Five-Why Drill-Down

The 5-Why method requires asking "why" at each level until you reach a root cause that is preventable by a process or code change. Stop at 5 levels or when you reach a root cause that a concrete change can address.

**Template — fill in for the primary incident**:

```
FIVE-WHY ANALYSIS
-----------------

Problem statement:
  [1 sentence: what failed, when, at what threshold]
  Example: "OPDS endpoint returned HTTP 500 from 09:47 to 10:05 UTC"

Why 1: Why did the OPDS endpoint return 500?
  Answer: [e.g., "OPDSGenerator raised AttributeError: 'NoneType' has no attribute 'books'"]

Why 2: Why did OPDSGenerator raise that error?
  Answer: [e.g., "The 'zim_exports' table was missing from the database"]

Why 3: Why was the 'zim_exports' table missing?
  Answer: [e.g., "Alembic migration 0045_add_zim_exports_table.py failed mid-execution"]

Why 4: Why did the migration fail mid-execution?
  Answer: [e.g., "A unique constraint violation on existing data halted the SQL transaction"]

Why 5: Why did a constraint violation occur?
  Answer: [e.g., "A duplicate entry existed in the source table that the new unique index would reject — this was not checked in pre-deployment testing"]

Root cause:
  [The actual preventable condition: e.g., "Pre-deployment testing did not include a data integrity check against the production data snapshot before running the migration"]

Preventive action:
  [Concrete, specific change: e.g., "Add a pre-migration data validation step to the deployment runbook that counts duplicate entries in source table before running alembic upgrade"]
```

---

### 2.3 Code / Config Change Tracking

For every code or configuration change that was part of the deployment, record:

| Change ID | File Changed | Nature of Change | Relation to Incident | Pass/Fail |
|-----------|-------------|------------------|---------------------|-----------|
| 1 | [e.g., backend/app/opds.py] | [e.g., Added ZIM export link generation] | [e.g., Direct cause of OPDSGenerator error] | FAIL |
| 2 | [e.g., alembic/versions/0045_*.py] | [e.g., Added zim_exports table] | [e.g., Migration that failed] | FAIL |
| 3 | [e.g., static/css/a11y.css] | [e.g., Phase 5 A11y styles] | [e.g., Not involved in incident] | PASS |

This table establishes which changes are safe (did not contribute to incident) and which require fixes before re-deployment.

---

### 2.4 Remediation Tracking

For each root cause identified:

```
REMEDIATION ITEM [N]
--------------------
Root cause:         [from 5-Why analysis]
What failed:        [specific code file, config, or process step]
Why it failed:      [technical explanation]
Fix required:       [what must change — code, config, or process]
Fix owner:          [who will implement]
Target completion:  [date before re-deployment attempt]
Verification test:  [how will you confirm the fix works before next deployment]
Status:             [ ] Open  [ ] In Progress  [ ] Resolved
```

---

## Part 3: Post-24-Hour Review (June 13, 09:00 UTC)

Complete this section at the end of the 24-hour passive monitoring window.

### 3.1 24-Hour Stability Report

```bash
# Run from local machine at June 13, 09:00 UTC
echo "=== 24-HOUR STABILITY REPORT ==="

# Total error count over 24 hours
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
echo "Error count (09:00 Jun12 – 09:00 Jun13):"
sudo journalctl -u open-repo \
  --since "2026-06-12 09:00" \
  --until "2026-06-13 09:00" \
  | grep -cE "500|ERROR|CRITICAL" || echo "0"

echo ""
echo "Total requests served:"
sudo journalctl -u open-repo \
  --since "2026-06-12 09:00" \
  --until "2026-06-13 09:00" \
  | grep -cE "GET|POST|PUT|DELETE" || echo "0"

echo ""
echo "Distinct error messages:"
sudo journalctl -u open-repo \
  --since "2026-06-12 09:00" \
  --until "2026-06-13 09:00" \
  | grep -E "ERROR|CRITICAL" \
  | sort -u \
  | head -10
EOF
```

### 3.2 Deployment Outcome Classification

Based on the 24-hour review, classify the deployment outcome:

| Classification | Criteria | Next Steps |
|----------------|----------|------------|
| FULL SUCCESS | All endpoints healthy, error rate <1% over 24h, no rollback, no user impact | Archive logs, mark deployment complete |
| PARTIAL SUCCESS | Primary endpoints healthy, minor errors logged, no rollback, no user-facing impact | Investigate minor errors, schedule fix within 7 days |
| DEGRADED OPERATION | Service running but one or more endpoints degraded; rollback not executed | Immediate fix required; schedule re-deployment within 48h |
| ROLLBACK | Deployment reverted to previous version | Complete 5-Why analysis before scheduling retry |
| EXTENDED INCIDENT | Service was down for >30 minutes and/or data integrity was affected | Full post-mortem required; re-deployment only after root cause resolved and tested |

**Deployment outcome for June 12**: ________________________

### 3.3 Archive Checklist

- [ ] Evidence snapshot file archived to persistent storage
- [ ] Application logs (text + JSON) archived
- [ ] Database state snapshot archived
- [ ] Monitoring script output archived
- [ ] Alert event records archived
- [ ] Five-Why analysis completed and reviewed
- [ ] All remediation items have owners and target dates
- [ ] Deployment outcome classification recorded
- [ ] Incident report shared with team (if CRITICAL or ROLLBACK outcome)
- [ ] Re-deployment schedule confirmed (if applicable)

---

**Audit Checklist Version**: 1.0
**Created**: June 6, 2026
**Valid For**: June 12, 2026 deployment
**References**: DEPLOYMENT_INCIDENT_RESPONSE_PLAYBOOK.md, POST_DEPLOYMENT_MONITORING_PLAN.md
