---
title: "Open-Repo June 12, 2026 Production Deployment Runbook"
project: open-repo
phase: 5 (final production deployment)
document_type: deployment-runbook
status: READY TO EXECUTE
created: 2026-06-03
target_deployment_date: 2026-06-12 (20:00 UTC)
deployment_window: "20:00–21:30 UTC (90 minutes)"
affected_endpoints: /docs, /redoc, /api/v2/opds/*
rollback_path: "revert commit, redeploy previous master"
rollback_time: "10 minutes"
---

# June 12 Production Deployment Runbook

**Deployment Date**: June 12, 2026  
**Deployment Time**: 20:00 UTC (evening UTC, adjust for your timezone)  
**Estimated Duration**: 15–25 minutes (plus 60 minutes post-deployment monitoring)  
**Deployment Target**: Production environment (Raspberry Pi 5, 100.70.184.84)  
**Deployer**: Must have SSH access to production host and git push access to upstream

---

## Pre-Deployment Checklist (June 12, 19:45 UTC)

Complete all items before proceeding to deployment steps.

### Environment and Access Verification (5 minutes)

- [ ] **Confirm production host is reachable**:
  ```bash
  ping 100.70.184.84
  ```
  Expected: ICMP reply within 100ms. If timeout, do not proceed; troubleshoot network connectivity first.

- [ ] **Confirm git access to upstream**:
  ```bash
  cd /home/awank/dev/SuperClaude_Framework
  git remote -v
  ```
  Expected output includes `origin` pointing to GitHub repository. If missing, configure remote.

- [ ] **Confirm SSH key for production host**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'echo "SSH OK"'
  ```
  Expected: "SSH OK" printed. If connection fails, configure SSH key before proceeding.

- [ ] **Verify no uncommitted changes in local repo**:
  ```bash
  git status
  ```
  Expected: "nothing to commit, working tree clean". If changes exist, stash or commit them first.

- [ ] **Confirm current branch is master**:
  ```bash
  git branch --show-current
  ```
  Expected: `master`. If on different branch, switch: `git checkout master`.

### Code and Testing Verification (5 minutes)

- [ ] **Verify deployment commit exists and is on master**:
  ```bash
  git log --oneline master | head -1
  # Should show recent commit with "feat(open-repo): Phase 5 A11y verification..."
  ```

- [ ] **Re-run OPDS tests locally** (confirms no regressions):
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  python -m pytest tests/test_opds_generator.py -q
  ```
  Expected: "50 passed". If failures, investigate root cause before proceeding.

- [ ] **Re-run route tests locally** (confirms no API breakage):
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  python -m pytest tests/test_routes.py -q
  ```
  Expected: "35 passed". If failures, investigate root cause before proceeding.

- [ ] **Confirm environment variables on production** (if needed):
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'grep OPDS /etc/environment'
  ```
  Expected: Any OPDS-related variables that have been set. (If none, that's OK; OPDS defaults are built-in.)

### Stakeholder Notification (2 minutes)

- [ ] **Send pre-deployment notification**:
  - Send message to #deployments Slack channel or equivalent
  - Include: "Open-Repo deployment starting at 20:00 UTC, expect 15–25 min downtime, monitoring 60 min post-deployment"

---

## Deployment Steps (20:00–20:25 UTC)

Execute each step in order. Do not skip steps. If any step fails, see **Rollback Procedure** section.

### Step 1: Pull Latest Code on Production (1 minute)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
  git fetch origin master
  git log --oneline origin/master | head -3
EOF
```

**Expected output**: Latest commit from local master is shown (should match your local `git log`).  
**If different**: Commits exist on origin that aren't in your local; run `git pull origin master` locally first, then retry this step.

### Step 2: Stop Running Application (1 minute)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  # Assuming app runs in systemd or supervisor; adjust command for your setup
  sudo systemctl stop open-repo || echo "Service not running or no systemctl"
  
  # Wait for graceful shutdown
  sleep 3
  
  # Verify stopped
  ps aux | grep "uvicorn" | grep -v grep || echo "Process stopped"
EOF
```

**Expected output**: Service stopped message or "Process stopped".  
**If error**: Check logs for why service won't stop. If hung, use `sudo kill -9` (hard kill).

### Step 3: Backup Current Deployment (30 seconds)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
  BACKUP_DIR="/opt/backups/open-repo-$(date +%Y%m%d-%H%M%S)"
  mkdir -p /opt/backups
  cp -r . "$BACKUP_DIR"
  echo "Backup created at: $BACKUP_DIR"
  ls -la /opt/backups | tail -3
EOF
```

**Expected output**: Backup directory path and directory listing showing recent backup.  
**If error**: Verify `/opt/backups` directory exists and is writable. Create if needed:
```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo mkdir -p /opt/backups && sudo chown ubuntu:ubuntu /opt/backups'
```

### Step 4: Deploy Code (2 minutes)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
  
  # Reset to origin/master (discards any local changes)
  git fetch origin master
  git reset --hard origin/master
  
  # Verify correct commit is checked out
  echo "Current commit:"
  git log --oneline -1
EOF
```

**Expected output**: Commit message showing Phase 5 A11y changes.  
**If error**: Check network connectivity to GitHub; if persistent, proceed with manual deployment (copy files via rsync).

### Step 5: Install/Update Python Dependencies (2 minutes)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  
  # Activate virtual environment (adjust path for your setup)
  source /opt/venv/open-repo/bin/activate 2>/dev/null || python -m venv /opt/venv/open-repo && source /opt/venv/open-repo/bin/activate
  
  # Upgrade pip
  pip install --upgrade pip setuptools wheel
  
  # Install dependencies
  pip install -r requirements.txt
  
  # Verify installation
  pip list | grep -E "fastapi|sqlalchemy|libzim" || echo "Warning: check dependency versions"
EOF
```

**Expected output**: Dependency installation complete, pip list shows key packages.  
**If error**: Check requirements.txt exists and is valid. If libzim fails on ARM64, consult PHASE_5.1_POST_MERGE_DEPLOYMENT_CHECKLIST.md.

### Step 6: Database Migrations (1 minute)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  
  # Check if migrations needed (Alembic or direct ORM)
  # For this deployment: no new migrations (A11y changes are CSS/JS only)
  echo "No migrations required for Phase 5 A11y deployment"
  
  # If migrations were needed, run:
  # alembic upgrade head || python -m app.db.migration_tool
  # (adjust command for your migration tool)
EOF
```

**Expected output**: "No migrations required" or migration success message.

### Step 7: Start Application (1 minute)

```bash
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  # Start service
  sudo systemctl start open-repo || echo "Starting service..."
  
  # Wait for startup
  sleep 5
  
  # Verify running
  sudo systemctl status open-repo
  ps aux | grep "uvicorn" | grep -v grep && echo "Process running" || echo "ERROR: Process not running"
EOF
```

**Expected output**: Service status shows "active (running)" and process listed.  
**If error**: Check logs: `sudo journalctl -u open-repo -n 50`. If app fails to start, see **Rollback Procedure**.

### Step 8: Verify Deployment (2 minutes)

```bash
# Test basic connectivity
curl -s http://100.70.184.84:8000/health | jq . || echo "Health check response:"

# Test Swagger UI loads
curl -s http://100.70.184.84:8000/docs | head -20 | grep -E "swagger|Swagger" && echo "Swagger UI OK" || echo "WARNING: Swagger UI may not be loading"

# Test ReDoc loads
curl -s http://100.70.184.84:8000/redoc | head -20 | grep -E "redoc|ReDoc" && echo "ReDoc OK" || echo "WARNING: ReDoc may not be loading"

# Test OPDS endpoint
curl -s http://100.70.184.84:8000/api/v2/opds/root.xml | head -3 && echo "OPDS OK" || echo "WARNING: OPDS endpoint not responding"
```

**Expected output**: All health checks pass, endpoints respond.  
**If any endpoint fails**: Check application logs and see Rollback Procedure.

---

## Post-Deployment Monitoring (20:30–21:30 UTC)

Do **not** consider deployment complete until post-deployment checks are done. Monitor for 60 minutes.

### Minute 0–5: Initial Health Checks

- [ ] **Application is running** (systemctl status shows active)
- [ ] **No error logs in past 5 minutes**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 30'
  ```
  Expected: No CRITICAL or ERROR level messages related to A11y, OPDS, or CSS/JS.

### Minute 5–15: Endpoint Verification

- [ ] **`/docs` (Swagger UI) loads without errors**:
  ```bash
  curl -s http://100.70.184.84:8000/docs -w "\nHTTP Status: %{http_code}\n"
  ```
  Expected: HTTP 200. Content includes "swagger" string and page title.

- [ ] **`/redoc` (ReDoc) loads without errors**:
  ```bash
  curl -s http://100.70.184.84:8000/redoc -w "\nHTTP Status: %{http_code}\n"
  ```
  Expected: HTTP 200. Content includes "redoc" string.

- [ ] **OPDS endpoints respond**:
  ```bash
  # Root catalog
  curl -s -H "Accept: application/atom+xml" http://100.70.184.84:8000/api/v2/opds/root.xml | head -5
  # Acquisition feed
  curl -s -H "Accept: application/atom+xml" http://100.70.184.84:8000/api/v2/opds/entries | head -5
  ```
  Expected: Both return valid XML starting with `<?xml version="1.0"...`. Content-Type is `application/atom+xml`.

### Minute 15–30: User Traffic Baseline

- [ ] **Monitor application metrics** (if monitoring tool available):
  - Request rate (should be normal or slightly elevated due to testing)
  - Error rate (should be 0%)
  - Response times (should be <500ms for /docs, /redoc; <1s for /api/v2/opds/*)

- [ ] **Check logs for warnings**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 100 | grep -i "warn"'
  ```
  Expected: No warnings related to A11y, OPDS, CSS, or JavaScript.

### Minute 30–60: Extended Monitoring

- [ ] **Periodically test endpoints** (every 10 minutes):
  ```bash
  for i in {1..6}; do
    curl -s http://100.70.184.84:8000/health | jq .status
    sleep 10
  done
  ```
  Expected: All responses show status "ok" or "healthy".

- [ ] **Check disk space** (ensure no runaway logs):
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'df -h / | tail -1'
  ```
  Expected: Used space <80% of total.

- [ ] **Monitor memory usage**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'free -h | grep Mem'
  ```
  Expected: Available memory >1GB.

### Minute 60: Deployment Confirmed

Once all post-deployment checks pass for 60 minutes:

- [ ] **Mark deployment as complete**:
  ```bash
  echo "Deployment completed at $(date)" >> /tmp/open-repo-deployment-log
  ```

- [ ] **Send post-deployment notification**:
  - Message: "Open-Repo Phase 5 deployment complete. All endpoints verified. No issues detected."
  - Channel: #deployments or equivalent

- [ ] **Create post-deployment summary**:
  ```
  Deployment Date: 2026-06-12
  Deployment Window: 20:00–20:30 UTC
  Deployment Status: SUCCESS
  Issues Detected: None
  Rollback Activated: No
  Post-deployment Monitoring: 60 minutes, all checks passed
  ```

---

## Smoke Tests (Automated, Optional)

If you have automated testing infrastructure, run this script post-deployment:

```bash
#!/bin/bash
# open-repo-smoke-test.sh

HOST="http://100.70.184.84:8000"
PASSED=0
FAILED=0

# Test 1: Health endpoint
echo "Test 1: Health check..."
if curl -s "$HOST/health" | grep -q "ok\|healthy"; then
  echo "  PASS: Health endpoint responds"
  ((PASSED++))
else
  echo "  FAIL: Health endpoint not responding"
  ((FAILED++))
fi

# Test 2: Swagger UI
echo "Test 2: Swagger UI loads..."
if curl -s "$HOST/docs" | grep -q "swagger"; then
  echo "  PASS: Swagger UI loaded"
  ((PASSED++))
else
  echo "  FAIL: Swagger UI not loading"
  ((FAILED++))
fi

# Test 3: ReDoc
echo "Test 3: ReDoc loads..."
if curl -s "$HOST/redoc" | grep -q "redoc"; then
  echo "  PASS: ReDoc loaded"
  ((PASSED++))
else
  echo "  FAIL: ReDoc not loading"
  ((FAILED++))
fi

# Test 4: OPDS root catalog
echo "Test 4: OPDS root catalog..."
if curl -s "$HOST/api/v2/opds/root.xml" | grep -q '<?xml'; then
  echo "  PASS: OPDS root catalog responds"
  ((PASSED++))
else
  echo "  FAIL: OPDS root catalog not responding"
  ((FAILED++))
fi

# Test 5: OPDS acquisition feed
echo "Test 5: OPDS acquisition feed..."
if curl -s "$HOST/api/v2/opds/entries" | grep -q 'feed\|entry'; then
  echo "  PASS: OPDS acquisition feed responds"
  ((PASSED++))
else
  echo "  FAIL: OPDS acquisition feed not responding"
  ((FAILED++))
fi

echo ""
echo "Smoke Test Results: $PASSED passed, $FAILED failed"
[ $FAILED -eq 0 ] && echo "All tests passed!" || echo "Some tests failed; investigate."
exit $FAILED
```

Run with:
```bash
bash open-repo-smoke-test.sh
```

Expected output: "All tests passed!" with 5 passed, 0 failed.

---

## Rollback Procedure (If Deployment Fails)

If deployment fails at any step or post-deployment monitoring detects critical issues, execute rollback immediately.

### Rollback Trigger Conditions

Rollback is required if any of the following occurs:

1. **Application won't start** after Step 7
   - Symptom: `sudo systemctl start open-repo` fails
   - Action: Proceed to rollback

2. **Health endpoint returns error** (Step 8)
   - Symptom: `/health` returns 500 or non-200 status code
   - Action: Proceed to rollback

3. **Swagger UI/ReDoc not loading** (Post-deployment check)
   - Symptom: `/docs` or `/redoc` returns 500 or blank page
   - Action: Proceed to rollback

4. **OPDS endpoints crash** (Post-deployment check)
   - Symptom: `/api/v2/opds/*` returns 500 or timeout
   - Action: Proceed to rollback

5. **Critical errors in logs** (Post-deployment monitoring)
   - Symptom: journalctl shows CRITICAL or ERROR related to deployed code
   - Action: Proceed to rollback

### Rollback Steps (3–5 minutes)

```bash
# 1. Stop current deployment
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  sudo systemctl stop open-repo
  echo "Service stopped"
EOF

# 2. Restore from backup
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
  LATEST_BACKUP=$(ls -t /opt/backups | grep "open-repo" | head -1)
  if [ -z "$LATEST_BACKUP" ]; then
    echo "ERROR: No backup found. Manual recovery required."
    exit 1
  fi
  echo "Restoring from backup: $LATEST_BACKUP"
  rm -rf ./* && cp -r /opt/backups/$LATEST_BACKUP/* .
  echo "Restore complete"
EOF

# 3. Start previous version
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  
  # Activate venv and restart
  source /opt/venv/open-repo/bin/activate
  sudo systemctl start open-repo
  
  # Verify
  sleep 3
  sudo systemctl status open-repo
EOF

# 4. Re-run post-deployment checks
# (Use same checks from Post-Deployment Monitoring section)

echo "Rollback complete. Previous version is running."
```

### Post-Rollback Actions

After rollback is complete:

1. **Notify stakeholders** that rollback occurred
2. **Create incident report** with:
   - When rollback was triggered
   - What failed
   - Root cause (if known)
   - Action items to fix before next deployment attempt
3. **Do not retry deployment** until root cause is identified and fixed
4. **Review logs** to determine what went wrong:
   ```bash
   ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 200 > /tmp/open-repo-failure.log'
   # Examine /tmp/open-repo-failure.log locally
   ```

---

## Appendix: Troubleshooting Common Issues

### Issue: SSH connection refused

**Symptom**: `ssh: connect to host 100.70.184.84 port 22: Connection refused`

**Cause**: Production host unreachable or SSH daemon down.

**Fix**:
1. Verify network connectivity: `ping 100.70.184.84`
2. If ping works but SSH fails, host SSH daemon may be down; restart or check firewall
3. If ping fails, check network routing to production environment

### Issue: Git fetch/push fails

**Symptom**: `fatal: unable to access 'https://github.com/...'`

**Cause**: Network or authentication issue.

**Fix**:
1. Check internet connectivity on deployment machine: `ping google.com`
2. Verify SSH key or PAT for GitHub authentication
3. Try manual deployment: copy files via rsync instead of git

### Issue: Dependencies fail to install

**Symptom**: `pip install` fails with compilation error or missing wheel.

**Cause**: Missing system dependencies (especially libzim on ARM64).

**Fix**:
1. For libzim specifically: consult PHASE_5.1_POST_MERGE_DEPLOYMENT_CHECKLIST.md
2. Install missing system libraries:
   ```bash
   sudo apt-get update && sudo apt-get install -y [missing-package]
   ```
3. Retry pip install

### Issue: Application starts but 503/502 errors on all endpoints

**Symptom**: `curl http://100.70.184.84:8000/health` returns 502/503

**Cause**: Application is running but not responding correctly (likely database connection issue).

**Fix**:
1. Check application logs: `sudo journalctl -u open-repo -n 50 | tail -30`
2. Verify database is accessible from production host:
   ```bash
   ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'psql -h [db-host] -U [user] -d [db-name] -c "SELECT 1"'
   ```
3. If database is down, bring it online or trigger rollback

### Issue: OPDS endpoints return 500

**Symptom**: `curl http://100.70.184.84:8000/api/v2/opds/root.xml` returns HTTP 500

**Cause**: OPDSGenerator initialization fails (missing database data or configuration).

**Fix**:
1. Check logs for specific error: `sudo journalctl -u open-repo | grep -i "opds"`
2. Verify ZIM export table exists and has data: `SELECT COUNT(*) FROM zim_export;`
3. If no ZIM data exists, that's OK (endpoint will return empty feed); verify endpoint still returns HTTP 200
4. If HTTP 500 persists, trigger rollback

### Issue: Swagger UI/ReDoc shows broken layout

**Symptom**: `/docs` or `/redoc` loads but CSS is missing (unstyled)

**Cause**: CSS overrides in a11y_docs.py not loading or JavaScript not executing.

**Fix**:
1. Clear browser cache: Ctrl+Shift+Delete (or Cmd+Shift+Delete on Mac)
2. Verify CSS is being injected: Check page source for `<style>` tag with `color-contrast` overrides
3. If CSS missing, check a11y_docs.py was deployed correctly:
   ```bash
   ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'grep -n "color-contrast" /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/app/a11y_docs.py'
   ```
4. If CSS is present but layout still broken, JavaScript DOM patch may not be running; check browser console for errors

---

## Contact & Escalation

**Deployment Owner**: [Your name/team]  
**On-Call Support**: [On-call contact]  
**Escalation**: [Manager/Lead contact]  

If any step fails and you are unable to diagnose, escalate to on-call support with:
1. Step where deployment failed
2. Error message from logs
3. Output of diagnostic commands
4. Time of failure (UTC)

---

## Sign-Off

**Deployment Executed By**: ________________  
**Date/Time**: ________________ UTC  
**Duration**: ________________ minutes  
**Status**: [ ] SUCCESS [ ] ROLLED BACK [ ] PARTIAL  
**Issues Encountered**: ________________  
**Monitoring Completed**: [ ] Yes (60 minutes) [ ] Abbreviated  
**Next Steps**: ________________  

---

**Runbook Version**: 1.0  
**Created**: June 3, 2026  
**Last Updated**: June 3, 2026  
**Valid Until**: June 12, 2026 (single-use runbook)
