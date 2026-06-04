---
title: "Open-Repo June 12, 2026 Go-Live Execution Checklist"
project: open-repo
phase: 5 (final production deployment)
document_type: operational-checklist
status: READY TO EXECUTE
created: 2026-06-04
deployment_date: 2026-06-12 (20:00 UTC)
deployment_window: "20:00–21:30 UTC (90 minutes)"
audience: "Deployment executor / on-call engineer"
---

# June 12 Go-Live Execution Checklist

**For the person executing the June 12 deployment at 20:00 UTC**

This checklist is designed to be used **alongside** the deployment runbook (`DEPLOYMENT_JUNE_12_RUNBOOK.md`). Where the runbook provides technical commands, this checklist provides operational guidance, decision points, contingency plans, and stakeholder communication templates.

**Print this document and keep it open during deployment.** Mark items as you complete them. When in doubt, escalate per the **Escalation Paths** section.

---

## Pre-Deployment: T-2 Hours (18:00 UTC)

### Phase 1A: Personal Readiness (5 minutes)

- [ ] **Have you reviewed the runbook in full?**
  - If not, read `DEPLOYMENT_JUNE_12_RUNBOOK.md` now (15–20 min read)
  - If yes, continue

- [ ] **Do you have a clear, interruption-free 2-hour window?**
  - Deployment is 90 min (20:00–21:30 UTC) + 60 min monitoring
  - Total time commitment: 2.5–3 hours
  - If interruptions likely, reschedule deployment to a safer window
  - If clear, continue

- [ ] **Is your environment ready?**
  - Laptop fully charged or plugged in
  - Fast, stable internet connection verified
  - No VPN/network issues
  - SSH key and git credentials ready
  - Terminal application open and logged in

- [ ] **Slack/communication app is open and active**
  - You will post status updates every 15 minutes during deployment
  - Have the #deployments channel (or equivalent) pinned/visible

### Phase 1B: Code and Environment Verification (15 minutes)

**Note**: This section mirrors the runbook but with operational guidance. Execute commands from the runbook, verify outputs match expectations below.

- [ ] **Ping production host** (from runbook: Pre-Deployment Checklist, Environment Verification step 1)
  ```bash
  ping -c 3 100.70.184.84
  ```
  **Expected**: All 3 packets received, latency <100ms
  **If different**: Network connectivity issue. Do NOT proceed. Troubleshoot or reschedule.
  **Decision**: Go / No-Go: ________

- [ ] **Verify git remote** (from runbook: step 2)
  ```bash
  cd /home/awank/dev/SuperClaude_Framework
  git remote -v
  ```
  **Expected**: `origin` pointing to GitHub superclauderepo
  **If different**: Remote misconfigured. Fix or use manual deployment (rsync).
  **Decision**: Go / No-Go: ________

- [ ] **Verify SSH key access** (from runbook: step 3)
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'echo "SSH OK"'
  ```
  **Expected**: "SSH OK" printed, no errors
  **If different**: SSH key issue. Debug or contact infrastructure team.
  **Decision**: Go / No-Go: ________

- [ ] **Verify local git state** (from runbook: step 4-5)
  ```bash
  git status && git branch --show-current
  ```
  **Expected**: "nothing to commit, working tree clean" and branch is "master"
  **If different**: Stash/commit local changes before proceeding.
  **Decision**: Go / No-Go: ________

- [ ] **Verify OPDS tests pass locally** (from runbook: Code and Testing Verification, step 1)
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  python -m pytest tests/test_opds_generator.py -q
  ```
  **Expected**: "50 passed"
  **If different**: Test failure. Investigate and fix before proceeding. Do NOT deploy failing code.
  **Decision**: Go / No-Go: ________

- [ ] **Verify route tests pass locally** (from runbook: step 2)
  ```bash
  cd /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend
  python -m pytest tests/test_routes.py -q
  ```
  **Expected**: "35 passed"
  **If different**: Test failure. Investigate and fix before proceeding.
  **Decision**: Go / No-Go: ________

### Phase 1C: Database and Rollback Readiness (10 minutes)

- [ ] **Confirm backup strategy**
  - The runbook includes backup step (Step 3 of deployment)
  - Verify `/opt/backups/` directory exists on production and is writable
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'ls -la /opt/backups/ | head -5'
  ```
  **Expected**: Directory listing showing previous backups (if any)
  **If error** (directory doesn't exist): Step 3 will create it with `mkdir -p`. OK to proceed.

- [ ] **Note pre-deployment commit hash for manual rollback** (if needed)
  ```bash
  git rev-parse origin/master
  ```
  **Action**: Write this hash down: `_______________________`
  - If git-based rollback fails, you can use this to manually verify the previous version

- [ ] **Verify rollback procedure accessibility**
  - The runbook includes full rollback steps (Rollback Procedure section)
  - If you need to rollback:
    1. Reference the Rollback section (starts at line 426 of runbook)
    2. Follow steps 1–4 (3–5 minutes total)
    3. Post-rollback actions: notify stakeholders, create incident report

- [ ] **Confirm backup location is accessible**
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'mkdir -p /opt/backups && ls -la /opt/backups'
  ```
  **Expected**: Writable directory (may be empty if first deployment)

### Phase 1D: Stakeholder Communication (5 minutes)

- [ ] **Send pre-deployment notification**
  
  **Template**:
  ```
  📢 DEPLOYMENT NOTICE: Open-Repo Phase 5 A11y
  
  Status: 🟡 STARTING SOON (in ~2 hours)
  Time: 20:00 UTC (adjust for your timezone: ________)
  Duration: 90 minutes deployment + 60 min monitoring
  
  **What's deploying**: 
  - WCAG 2.1 AA accessibility improvements
  - OPDS v2 feed endpoints
  - Swagger UI & ReDoc enhancements
  - Zero breaking changes
  
  **Expected impact**:
  - 📖 /docs (Swagger UI) will be briefly unavailable
  - 📄 /redoc (ReDoc) will be briefly unavailable
  - 📡 /api/v2/opds/* endpoints will be briefly unavailable
  - All other endpoints: no impact
  
  **Communication during deployment**:
  - Status updates every 15 minutes in this channel
  - If issues arise: I will post immediately
  
  Questions? Reply in thread. Otherwise, stand by.
  ```
  
  - [ ] Post to #deployments (or equivalent Slack channel)
  - [ ] Include link to this checklist (for transparency)

- [ ] **Confirm key stakeholders have read the notice**
  - Product lead: _________ (confirm receipt)
  - Infrastructure/ops lead: _________ (confirm receipt)
  - On-call support: _________ (confirm receipt)

---

## T-0 Hour: Deployment Window (20:00–20:25 UTC)

### Phase 2A: Final Pre-Flight Checks (20:00–20:05 UTC)

Before starting Step 1, complete these checks:

- [ ] **Verify time**: Current UTC time is 20:00 or within 5 minutes
  - `date -u` to check
  - If significantly off, sync time or reschedule

- [ ] **Post start notification to Slack**
  ```
  🚀 DEPLOYMENT STARTING NOW (20:00 UTC)
  
  Executor: [Your name]
  Runbook version: 1.0
  Expected completion: 20:25 UTC
  Monitoring starts: 20:25 UTC (duration: 60 min)
  
  Status: ✅ All pre-flight checks passed
  Next update: 20:10 UTC
  ```

- [ ] **Close all other applications** that might distract you
  - Email, Slack (except deployment channel), browser tabs unrelated to deployment
  - Minimize notifications

### Phase 2B: Execute Deployment Steps 1–8 (20:05–20:25 UTC)

**Follow the runbook exactly. This checklist just tracks progress.**

For each step below, execute the commands from `DEPLOYMENT_JUNE_12_RUNBOOK.md` Deployment Steps section (lines 98–248).

#### Step 1: Pull Latest Code (20:05–20:06 UTC)

- [ ] **Execute**: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'...` (runbook line 105)
- [ ] **Verify**: Latest commit shown in output
- [ ] **Status**: PASS / FAIL
- [ ] **If FAIL**: See troubleshooting in runbook Appendix, section "Git fetch/push fails"
  - [ ] If git fails, use manual deployment: `rsync -avz . ubuntu@100.70.184.84:/home/awank/dev/SuperClaude_Framework/projects/open-repo/`
  - [ ] Re-verify commit after rsync
  - [ ] Continue to Step 2

**Decision**: Go to Step 2 / Rollback: ________

#### Step 2: Stop Running Application (20:06–20:07 UTC)

- [ ] **Execute**: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'...` (runbook line 118)
- [ ] **Verify**: Service stopped, process no longer running
- [ ] **Status**: PASS / FAIL
- [ ] **If FAIL**: Application may be hung
  - [ ] Check logs: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 20'`
  - [ ] Attempt hard kill: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo pkill -9 uvicorn'`
  - [ ] Verify process is gone
  - [ ] Continue to Step 3

**Decision**: Go to Step 3 / Rollback: ________

#### Step 3: Backup Current Deployment (20:07–20:08 UTC)

- [ ] **Execute**: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'...` (runbook line 136)
- [ ] **Verify**: Backup directory created, path printed
- [ ] **Status**: PASS / FAIL
- [ ] **If FAIL**: Backup directory creation failed
  - [ ] Check `/opt/backups/` permissions: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo ls -la /opt/backups'`
  - [ ] Create directory if missing: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo mkdir -p /opt/backups && sudo chown ubuntu:ubuntu /opt/backups'`
  - [ ] Retry backup: re-execute Step 3 command
  - [ ] Continue to Step 4

**CRITICAL**: If Step 3 fails after retry, do NOT proceed to Step 4. You cannot safely roll back without a backup. Escalate to infrastructure team.

**Decision**: Go to Step 4 / Escalate: ________

#### Step 4: Deploy Code (20:08–20:10 UTC)

- [ ] **Execute**: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'...` (runbook line 155)
- [ ] **Verify**: Correct commit checked out, message shows Phase 5 A11y changes
- [ ] **Status**: PASS / FAIL
- [ ] **If FAIL**: Git reset failed
  - [ ] Network issue or GitHub unreachable
  - [ ] Use manual deployment (rsync) if git continues to fail:
    ```bash
    rsync -avz /home/awank/dev/SuperClaude_Framework/projects/open-repo/ \
      ubuntu@100.70.184.84:/home/awank/dev/SuperClaude_Framework/projects/open-repo/
    ```
  - [ ] After rsync, verify files are in place on production
  - [ ] Continue to Step 5

**Decision**: Go to Step 5 / Troubleshoot: ________

#### Step 5: Install/Update Dependencies (20:10–20:12 UTC)

- [ ] **Execute**: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'...` (runbook line 174)
- [ ] **Verify**: Dependencies installed, pip list shows fastapi, sqlalchemy, libzim
- [ ] **Status**: PASS / FAIL
- [ ] **If FAIL**: Dependency installation failed (common: libzim on ARM64)
  - [ ] Check error message: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'pip install libzim' 2>&1 | tail -20`
  - [ ] For libzim: consult `PHASE_5.1_POST_MERGE_DEPLOYMENT_CHECKLIST.md` for ARM64 workarounds
  - [ ] Install missing system dependencies: `sudo apt-get install -y [package]`
  - [ ] Retry pip install
  - [ ] Continue to Step 6

**Decision**: Go to Step 6 / Troubleshoot: ________

#### Step 6: Database Migrations (20:12–20:13 UTC)

- [ ] **Execute**: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'...` (runbook line 197)
- [ ] **Verify**: "No migrations required" message or migration success shown
- [ ] **Status**: PASS / FAIL
- [ ] **If FAIL**: Migration failed (rare for this deployment, as A11y changes are CSS/JS only)
  - [ ] Check logs for database errors
  - [ ] If database is down: bring it online or escalate to DBA
  - [ ] If migration syntax error: fix and retry
  - [ ] Continue to Step 7

**Decision**: Go to Step 7 / Troubleshoot: ________

#### Step 7: Start Application (20:13–20:14 UTC)

- [ ] **Execute**: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'...` (runbook line 215)
- [ ] **Verify**: Service status shows "active (running)", uvicorn process listed
- [ ] **Status**: PASS / FAIL
- [ ] **If FAIL**: Application failed to start
  - [ ] Check logs immediately: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 50 | tail -30'`
  - [ ] Common issues:
    - Port already in use: `sudo lsof -i :8000` to find what's using port
    - Import errors: check Python syntax, dependencies
    - Database connection error: verify DB is online
  - [ ] Fix root cause, then retry: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo systemctl restart open-repo'`
  - [ ] If continues to fail after 2 attempts, **ROLLBACK immediately** (see Phase 3B)

**Critical Decision**: Go to Step 8 / ROLLBACK: ________

#### Step 8: Verify Deployment (20:14–20:25 UTC)

- [ ] **Execute all verification commands** from runbook (runbook line 234–244)
  - [ ] Health endpoint check
  - [ ] Swagger UI check
  - [ ] ReDoc check
  - [ ] OPDS endpoint check

- [ ] **Compile results**:
  | Check | Status | Notes |
  |-------|--------|-------|
  | Health | PASS / FAIL | ________ |
  | Swagger UI | PASS / FAIL | ________ |
  | ReDoc | PASS / FAIL | ________ |
  | OPDS Root | PASS / FAIL | ________ |

- [ ] **All checks passed?**
  - **If YES**: Proceed to Phase 3A (Post-Deployment Monitoring)
  - **If NO**: At least one endpoint failed. See Phase 3B (Rollback Decision)

**Decision**: Go to Phase 3A (Monitoring) / Phase 3B (Rollback): ________

- [ ] **Post deployment status to Slack**
  ```
  ✅ DEPLOYMENT STEPS COMPLETE (20:25 UTC)
  
  All 8 steps executed successfully:
  ✅ Code pulled
  ✅ App stopped
  ✅ Backup created
  ✅ Code deployed
  ✅ Dependencies updated
  ✅ Migrations (none required)
  ✅ App started
  ✅ Endpoints verified
  
  Now entering 60-minute monitoring window.
  Next status update: 20:40 UTC
  ```

---

## Post-Deployment: T+0 to T+60 Minutes (20:25–21:25 UTC)

### Phase 3A: Post-Deployment Monitoring (All Items Required)

**This is critical.** Do not skip checks. Mark time for each check to verify you're on schedule.

#### Minute 0–5: Initial Health Checks (20:25–20:30 UTC)

- [ ] **Time check**: _________ UTC (should be ~20:25–20:30)

- [ ] **Application is running**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo systemctl status open-repo'
  ```
  **Expected**: "active (running)"
  **If different**: App crashed. Investigate immediately and rollback if needed.

- [ ] **No critical errors in logs**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 30 | grep -i "error\|critical"'
  ```
  **Expected**: No output or only non-critical warnings
  **If ERROR found**: Investigate (see troubleshooting below)

- [ ] **Initial health: PASS / FAIL / PARTIAL**
  - PASS: App running, no errors → continue to minute 5–15 checks
  - FAIL: App down or critical errors → **ROLLBACK immediately** (see Phase 3B)
  - PARTIAL: Minor warnings only → continue, monitor closely

**Decision**: Continue / Rollback: ________

#### Minute 5–15: Endpoint Verification (20:30–20:40 UTC)

- [ ] **Time check**: _________ UTC (should be ~20:30–20:40)

- [ ] **`/docs` (Swagger UI) verification**:
  ```bash
  curl -s http://100.70.184.84:8000/docs -w "\nHTTP Status: %{http_code}\n" | head -5
  ```
  **Expected**: HTTP 200, content includes "swagger"
  **If 500 or blank**: CSS/JS not loading. Check logs. If persistent, rollback.
  **Status**: PASS / FAIL

- [ ] **`/redoc` (ReDoc) verification**:
  ```bash
  curl -s http://100.70.184.84:8000/redoc -w "\nHTTP Status: %{http_code}\n" | head -5
  ```
  **Expected**: HTTP 200, content includes "redoc"
  **If 500 or blank**: CSS/JS not loading. Check logs. If persistent, rollback.
  **Status**: PASS / FAIL

- [ ] **OPDS root catalog**:
  ```bash
  curl -s -H "Accept: application/atom+xml" http://100.70.184.84:8000/api/v2/opds/root.xml | head -3
  ```
  **Expected**: Valid XML starting with `<?xml`, Content-Type includes `application/atom+xml`
  **If 500 or not XML**: Database issue. Check logs. If persistent, rollback.
  **Status**: PASS / FAIL

- [ ] **OPDS acquisition feed**:
  ```bash
  curl -s -H "Accept: application/atom+xml" http://100.70.184.84:8000/api/v2/opds/entries | head -3
  ```
  **Expected**: Valid XML with `<feed>` root element
  **If 500 or not XML**: Database issue. If persistent, rollback.
  **Status**: PASS / FAIL

- [ ] **Endpoint verification: PASS / FAIL**
  - PASS: All 4 endpoints respond correctly → continue monitoring
  - FAIL: 1+ endpoints returning errors → investigate, then decide to rollback

**Decision**: Continue / Troubleshoot / Rollback: ________

#### Minute 15–30: User Traffic & Metrics Baseline (20:40–20:55 UTC)

- [ ] **Time check**: _________ UTC (should be ~20:40–20:55)

- [ ] **Check disk space** (ensure no runaway logs):
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'df -h / | tail -1'
  ```
  **Expected**: Used space <80% of total
  **If >80%**: Check for log growth or other issues
  **Status**: ________ GB used / ________ GB total

- [ ] **Check memory usage**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'free -h | grep Mem'
  ```
  **Expected**: Available memory >1GB
  **If <1GB**: Check for memory leak or heavy traffic. Monitor closely.
  **Status**: ________ MB available

- [ ] **Check for warnings in logs**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 100 | grep -i "warn"'
  ```
  **Expected**: No warnings or only minor warnings about third-party libs
  **If warnings found**: Document and monitor. Only escalate if pattern emerges.
  **Status**: _________ warnings found

- [ ] **System metrics baseline: PASS / STABLE**

#### Minute 30–60: Extended Monitoring & Final Checks (20:55–21:25 UTC)

- [ ] **Time check**: _________ UTC (should be ~20:55–21:25)

- [ ] **Health endpoint periodic test** (run every 10 minutes, 6 times):
  ```bash
  for i in {1..6}; do
    echo "Check $i: $(date -u +%T)"
    curl -s http://100.70.184.84:8000/health | jq .status 2>/dev/null || echo "ERROR"
    sleep 600  # 10 minutes
  done
  ```
  **Expected**: All 6 responses show status "ok" or "healthy"
  **If failures**: Note which checks failed. If pattern, investigate.

  - Check 1 (20:55): ________
  - Check 2 (21:05): ________
  - Check 3 (21:15): ________
  - Check 4 (21:25): ________
  - Check 5 (21:35): ________
  - Check 6 (21:45): ________

  **Note**: If 60 minutes extends past your availability, you can stop after check 3–4 and hand off to on-call support with notes.

- [ ] **Final disk space check**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'df -h /'
  ```
  **Expected**: No significant change from minute 15–30 check
  **Status**: ________ GB used

- [ ] **Final memory check**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'free -h'
  ```
  **Expected**: No significant degradation
  **Status**: ________ MB available

- [ ] **Final log review**:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 50 | tail -20'
  ```
  **Expected**: No new errors since last check
  **Status**: ________

### Phase 3B: Rollback Decision (Only If Needed)

**Only execute this phase if monitoring detects critical issues.**

#### Rollback Trigger Checklist

Rollback is **mandatory** if **any** of the following occurs:

- [ ] **Application won't start or keeps crashing**
  - Symptom: `systemctl status` shows "failed" or service repeatedly restarts
  - Trigger: YES / NO

- [ ] **Health endpoint returns error (Step 8 verification failed)**
  - Symptom: `/health` returns 500 or non-200
  - Trigger: YES / NO

- [ ] **Swagger UI or ReDoc not loading**
  - Symptom: `/docs` or `/redoc` returns 500 or blank page
  - Trigger: YES / NO

- [ ] **OPDS endpoints crash**
  - Symptom: `/api/v2/opds/*` returns 500
  - Trigger: YES / NO

- [ ] **Critical errors in logs**
  - Symptom: `journalctl` shows CRITICAL or ERROR (not just warnings)
  - Trigger: YES / NO

- [ ] **Any trigger present? YES / NO**

---

**If ANY trigger is YES, execute rollback immediately:**

#### Rollback Execution (3–5 minutes)

**Follow the runbook Rollback Procedure section exactly (lines 454–511).**

- [ ] **Step 1: Stop current deployment**
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
    sudo systemctl stop open-repo
    echo "Service stopped at $(date -u +%T)"
  EOF
  ```
  **Verify**: Service stopped

- [ ] **Step 2: Restore from backup**
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
    cd /home/awank/dev/SuperClaude_Framework/projects/open-repo
    LATEST_BACKUP=$(ls -t /opt/backups | grep "open-repo" | head -1)
    if [ -z "$LATEST_BACKUP" ]; then
      echo "ERROR: No backup found!"
      exit 1
    fi
    echo "Restoring from: $LATEST_BACKUP"
    rm -rf ./* && cp -r /opt/backups/$LATEST_BACKUP/* .
    echo "Restore complete"
  EOF
  ```
  **Verify**: Backup found and restored

- [ ] **Step 3: Start previous version**
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 << 'EOF'
    sudo systemctl start open-repo
    sleep 3
    sudo systemctl status open-repo
  EOF
  ```
  **Verify**: Service status shows "active (running)"

- [ ] **Step 4: Re-run post-deployment checks**
  - Run health check: `curl -s http://100.70.184.84:8000/health | jq .`
  - Run Swagger check: `curl -s http://100.70.184.84:8000/docs | grep -o "swagger"`
  - Run ReDoc check: `curl -s http://100.70.184.84:8000/redoc | grep -o "redoc"`
  - All should pass
  - **Verify**: All checks pass, app is stable

- [ ] **Rollback Status**: SUCCESS / PARTIAL / FAILED

#### Post-Rollback Actions (Mandatory)

- [ ] **Post rollback notification to Slack**
  ```
  🔙 ROLLBACK EXECUTED (HH:MM UTC)
  
  Reason: [Describe what failed]
  Time to rollback: [X] minutes
  Current status: Previous version now running
  
  **Next Steps**:
  1. Incident report being created
  2. Root cause investigation required
  3. Deployment rescheduled (date TBD)
  
  Slack thread for incident discussion: [link]
  ```

- [ ] **Create incident report** with:
  - [ ] When rollback was triggered (UTC time)
  - [ ] What failed (which step, which endpoint)
  - [ ] Error message from logs
  - [ ] Root cause hypothesis (if known)
  - [ ] Action items to fix before retry
  - [ ] File: `/tmp/open-repo-incident-HH-MM-UTC.md` (save for review)

- [ ] **Collect failure logs** for root cause analysis:
  ```bash
  ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -n 200 > /tmp/open-repo-failure.log 2>&1'
  scp -i ~/.ssh/production_key ubuntu@100.70.184.84:/tmp/open-repo-failure.log ./open-repo-failure-$(date +%Y%m%d-%H%M%S).log
  ```

- [ ] **Notify stakeholders**
  - Manager/lead: [Contact with incident details]
  - Product owner: [Deployment failed, ETA for next attempt]
  - Engineering team: [Review incident report]

- [ ] **Do not retry deployment** until root cause is identified and fixed

---

### Phase 3C: Deployment Confirmation (If Monitoring Passes)

**Execute this section only after all 60 minutes of monitoring are complete and all checks pass.**

- [ ] **Time check**: _________ UTC (should be 21:25 or later)

- [ ] **All monitoring checks passed?**
  - Health checks (6/6): PASS
  - Endpoint verification: PASS
  - No critical errors in logs: PASS
  - Disk/memory stable: PASS
  - [ ] If any FAIL, see Phase 3B (Rollback)

- [ ] **Post deployment success notification**
  ```
  ✅ DEPLOYMENT COMPLETE & VERIFIED (21:25 UTC)
  
  **Deployment Summary**:
  - Start time: 20:00 UTC
  - Duration: 25 minutes
  - Rollback activated: No
  - Post-deployment monitoring: 60 minutes
  - Final status: ✅ ALL SYSTEMS OPERATIONAL
  
  **Verified Endpoints**:
  ✅ /docs (Swagger UI) — accessible
  ✅ /redoc (ReDoc) — accessible
  ✅ /api/v2/opds/root.xml — accessible
  ✅ /api/v2/opds/entries — accessible
  ✅ /health — operational
  
  **System Health**:
  - Memory: stable
  - Disk: <80% used
  - Errors: 0 critical
  - Warnings: none
  
  Phase 5 A11y deployment to production is **LIVE**.
  
  Go-live successful. Now monitoring for Day 1 issues.
  ```

- [ ] **Mark deployment as complete in this checklist**

- [ ] **Create post-deployment summary** (for archives)
  ```
  DEPLOYMENT LOG
  Deployment Date: June 12, 2026
  Deployment Window: 20:00–20:25 UTC (actual: HH:MM–HH:MM UTC)
  Deployment Duration: [X] minutes
  Deployment Status: ✅ SUCCESS
  Issues Encountered: None
  Rollback Activated: No
  Post-deployment Monitoring: 60 minutes, all checks passed
  Executor: [Your name]
  Sign-off Time: [HH:MM UTC]
  ```
  Save to: `/tmp/open-repo-deployment-summary-$(date +%Y%m%d).txt`

---

## Day 1 & Day 7 Post-Deployment Checks

### Day 1 Follow-Up (June 13, 2026)

**Assign to on-call or designated team member.**

- [ ] **Morning check** (first thing upon arriving):
  - [ ] Production is still running: `curl http://100.70.184.84:8000/health`
  - [ ] No errors overnight: `ssh -i ~/.ssh/production_key ubuntu@100.70.184.84 'sudo journalctl -u open-repo -S yesterday | grep -i error'`
  - [ ] Users have not reported issues (check email, Slack, issue tracker)
  - [ ] Endpoints are responding normally (spot-check /docs, /redoc, /api/v2/opds/*)

- [ ] **If all checks pass**: No action needed. Good sign.
- [ ] **If issues detected**: Investigate and file bug report if needed.

- [ ] **Day 1 sign-off**: All checks completed: YES / NO, date: ___________

### Day 7 Follow-Up (June 19, 2026)

**Assign to product lead or senior engineer.**

- [ ] **Metric review**:
  - [ ] Deployment-related errors: 0 or minimal
  - [ ] User traffic normal: compare to baseline before June 12
  - [ ] No new issues reported since go-live

- [ ] **WCAG compliance verification**:
  - [ ] Re-run A11y audit to confirm no regressions: `pytest tests/test_a11y_*.py`
  - [ ] All WCAG 2.1 AA criteria still pass

- [ ] **OPDS endpoint health**:
  - [ ] All /api/v2/opds/* endpoints respond in <1s
  - [ ] XML output is valid and unchanged
  - [ ] Feed includes expected entries

- [ ] **Performance baseline**:
  - [ ] Response times: similar to pre-deployment
  - [ ] Memory usage: stable
  - [ ] CPU usage: normal

- [ ] **Day 7 sign-off**:
  - [ ] All checks passed: YES / NO
  - [ ] Date: ___________
  - [ ] Next review: [date]

---

## Escalation Paths & Contingency Contacts

**If any issues arise that you cannot resolve, use these paths:**

### Critical Issues (App Down / Endpoints Broken)

**Escalation Path**:
1. **Try to rollback** (Phase 3B) — most reliable fix
2. **If rollback fails**: Contact infrastructure lead immediately
   - Name: ___________
   - Phone: ___________
   - Slack: ___________

### Deployment Blocking Issues (Cannot Start / Network)

**Escalation Path**:
1. **Infrastructure team**: [contact]
   - Network connectivity issues
   - SSH/access problems
   - System dependencies
2. **On-call engineer**: [contact]
   - If infrastructure unavailable

### Dependency/Build Issues

**Escalation Path**:
1. **DevOps/Build team**: [contact]
   - libzim compilation (ARM64)
   - Missing system packages
   - Virtual environment issues
2. **If unavailable**: Defer deployment to next window

### Data/Database Issues

**Escalation Path**:
1. **DBA team**: [contact]
   - Database migration failures
   - Data corruption
   - Connection issues
2. **Backup/recovery**: [contact]
   - If data restore needed

### Communication Strategy During Incident

- **Do not panic** — you have a working rollback procedure
- **Post updates every 5–10 minutes** in Slack (even if no progress)
- **Be explicit about unknowns**: "Investigating X, will know more in 5 min"
- **Escalate early** — don't spend >10 min trying to fix unknown issue alone
- **Post-incident**: Create summary and share with team

---

## Success Criteria: Go-Live is Approved When...

All of the following must be true:

- [ ] **Code deployment**: Completed without errors (8/8 steps succeeded)
- [ ] **Application startup**: Service started and is running
- [ ] **Endpoints verified**: All 4 endpoints (/docs, /redoc, /health, /api/v2/opds/*) return HTTP 200
- [ ] **No critical errors**: journalctl shows no CRITICAL or ERROR level messages
- [ ] **60 minutes monitoring**: Completed successfully, no issues detected
- [ ] **Rollback not activated**: Indicates no major issues
- [ ] **Stakeholder notification**: Post-deployment success message sent

**Go-Live Status**: ✅ APPROVED / ❌ ROLLBACK / ⏸ CONDITIONAL

---

## Quick Reference: Decision Tree

**Use this if you're unsure what to do:**

```
Start Deployment (20:00 UTC)
↓
├─ Pre-flight checks fail?
│  └─ YES: Reschedule deployment, investigate issue
│  └─ NO: Continue
↓
├─ Any deployment step (1–8) fails?
│  └─ YES: Troubleshoot per runbook Appendix, then:
│     ├─ Fixed? Retry step, continue
│     └─ Not fixed? See Phase 3B (Rollback)
│  └─ NO: Continue
↓
├─ Step 8 verification (endpoints) passes?
│  └─ NO: Phase 3B (Rollback)
│  └─ YES: Continue to monitoring
↓
├─ Post-deployment monitoring (min 0–5) shows critical error?
│  └─ YES: Phase 3B (Rollback)
│  └─ NO: Continue
↓
├─ Post-deployment monitoring (min 5–60) shows any trigger condition?
│  └─ YES: Phase 3B (Rollback)
│  └─ NO: Continue
↓
└─ All 60 minutes passed, all checks green?
   └─ YES: Phase 3C (Deployment Confirmation) ✅ SUCCESS
   └─ NO: Phase 3B (Rollback) 🔙
```

---

## Sign-Off & Documentation

**To be completed by deployment executor:**

### Pre-Deployment Sign-Off

- [ ] **All pre-flight checks passed**: YES
- [ ] **Ready to proceed**: YES
- [ ] **Executor name**: _______________________
- [ ] **Time**: _______________________ UTC
- [ ] **Date**: June 12, 2026

### Post-Deployment Sign-Off

- [ ] **Deployment completed**: YES
- [ ] **Final status**: ✅ SUCCESS / 🔙 ROLLBACK / ⚠️ PARTIAL
- [ ] **Duration**: _______ minutes (deployment) + _______ minutes (monitoring)
- [ ] **Issues encountered**: [List any, or "None"]
- [ ] **Root cause analysis needed**: YES / NO
- [ ] **Executor name**: _______________________
- [ ] **Completion time**: _______________________ UTC
- [ ] **Witnesses/stakeholders**: [List approvers]

### Approval Sign-Offs (For Leadership)

- [ ] **Product lead approval**: _________________ (signature/date)
- [ ] **Infrastructure lead approval**: _________________ (signature/date)
- [ ] **On-call engineer sign-off**: _________________ (signature/date)

---

## Appendix: Important Contacts & Escalation Matrix

| Role | Name | Phone | Slack | Email | Notes |
|------|------|-------|-------|-------|-------|
| Deployment Owner | _____________ | _____________ | _____________ | _____________ | This person (you) |
| On-Call Support | _____________ | _____________ | _____________ | _____________ | If escalation needed |
| Infrastructure Lead | _____________ | _____________ | _____________ | _____________ | For network/host issues |
| DBA/Database Admin | _____________ | _____________ | _____________ | _____________ | For data issues |
| Product Lead | _____________ | _____________ | _____________ | _____________ | For business decisions |
| Manager/Director | _____________ | _____________ | _____________ | _____________ | Final escalation |

---

## Appendix: Useful Commands Quick Reference

```bash
# SSH into production host
ssh -i ~/.ssh/production_key ubuntu@100.70.184.84

# Check application status
sudo systemctl status open-repo
sudo systemctl restart open-repo

# View recent logs
sudo journalctl -u open-repo -n 50
sudo journalctl -u open-repo -S "1 hour ago"

# Test endpoints
curl http://100.70.184.84:8000/health
curl http://100.70.184.84:8000/docs
curl http://100.70.184.84:8000/api/v2/opds/root.xml

# Check system resources
df -h /                    # Disk usage
free -h                    # Memory usage
ps aux | grep uvicorn      # Running processes

# Backup management
ls -la /opt/backups/       # List backups
du -sh /opt/backups/       # Backup directory size

# Manual file deployment (if git fails)
rsync -avz /local/path ubuntu@100.70.184.84:/remote/path
```

---

**Document Version**: 1.0  
**Created**: June 4, 2026  
**For Deployment**: June 12, 2026, 20:00 UTC  
**Valid Until**: June 12, 2026 (single-use checklist)  
**Complementary Document**: `DEPLOYMENT_JUNE_12_RUNBOOK.md`

---

**End of Go-Live Execution Checklist**
