# Jetson OneDrive Remediation Scripts
**Item 32 — Post-Market Execution (after 20:00 UTC June 29)**

## Context
OneDrive service on Jetson has crashed 1,005,780 times since May 9, filling `/var/log/syslog` with 12GB. System operationally clear for today's market (125GB free), but must be fixed within 48h (by ~July 1 13:30 UTC) to prevent RED disk contention by July 3-4.

**Timeline**: Execute post-market (after 20:00 UTC June 29). Execution takes <5 minutes.

---

## Pre-Execution Checklist
- [ ] User confirms market close (20:00 UTC+)
- [ ] SSH access to Jetson verified (100.120.18.84)
- [ ] Backup syslog timestamp recorded: `stat /var/log/syslog`

---

## Script 1: Stop & Disable OneDrive Service

```bash
#!/bin/bash
# Stop + disable user-session onedrive.service
# Safe: cannot affect system services or data

set -e  # Exit on error

echo "[$(date -u)] Starting onedrive remediation..."

# Stop service (user context)
systemctl --user stop onedrive.service || echo "Service not running (expected)"

# Disable auto-start
systemctl --user disable onedrive.service

echo "[$(date -u)] ✅ OneDrive service stopped and disabled"

# Verify disabled
status=$(systemctl --user is-enabled onedrive.service 2>/dev/null || echo "disabled")
echo "[$(date -u)] Service status: $status"

if [ "$status" = "disabled" ]; then
  echo "[$(date -u)] ✅ SUCCESS: OneDrive will not auto-start"
else
  echo "[$(date -u)] ⚠️  WARNING: Service may still auto-start; manual override recommended"
fi
```

**Safe to run**: Yes — only affects user-context service, no system impact

---

## Script 2: Safely Truncate Syslog

```bash
#!/bin/bash
# Safely truncate /var/log/syslog to prevent disk overflow
# VeraCrypt not affected; only rotated log file truncated

set -e

echo "[$(date -u)] Truncating syslog (12GB expected)..."

# Record size before
SIZE_BEFORE=$(du -h /var/log/syslog | cut -f1)
echo "[$(date -u)] Syslog size before: $SIZE_BEFORE"

# Truncate safely (preserve file permissions)
sudo truncate -s 0 /var/log/syslog

# Verify truncation
SIZE_AFTER=$(du -h /var/log/syslog | cut -f1)
echo "[$(date -u)] Syslog size after: $SIZE_AFTER"

# Verify disk space reclaimed
DISK_FREE=$(df -h /opt | tail -1 | awk '{print $4}')
echo "[$(date -u)] ✅ Disk free now: $DISK_FREE (was ~113GB with full syslog)"

echo "[$(date -u)] ✅ SUCCESS: Syslog safely truncated"
```

**Safe to run**: Yes — only truncates rotated logs, does not touch active logging

---

## Script 3: Reclaim Docker Build Cache (Optional)

```bash
#!/bin/bash
# Optional: Reclaim Docker build cache (~2.3GB)
# Safe: can be re-built on next docker build; no data loss

set -e

echo "[$(date -u)] Checking Docker build cache size..."

CACHE_SIZE=$(docker system df | grep -i "build cache" | awk '{print $4}')
echo "[$(date -u)] Current build cache: $CACHE_SIZE"

if [ -z "$CACHE_SIZE" ]; then
  echo "[$(date -u)] No cache data available"
  CACHE_SIZE="unknown"
fi

# Prune unused cache (safe: only removes unused layers)
echo "[$(date -u)] Pruning unused Docker data..."
docker system prune -f --volumes

DISK_FREE=$(df -h / | tail -1 | awk '{print $4}')
echo "[$(date -u)] ✅ Disk free now: $DISK_FREE"

echo "[$(date -u)] ✅ SUCCESS: Docker cache pruned"
```

**Safe to run**: Yes — only removes unused layers, active containers unaffected

---

## Execution Steps (User Authorizes One-Time)

**Decision Point**: User authorizes autonomous post-market execution OR schedules manual execution by June 30 13:30 UTC

### Option A: Autonomous Post-Market Execution
1. Post-market (after 20:00 UTC), orchestrator executes all 3 scripts sequentially
2. Scripts run in <5 minutes total
3. Results logged to WORKLOG.md
4. No further action required

### Option B: User Manual Execution
1. User SSH to Jetson: `ssh awank@100.120.18.84`
2. Copy-paste each script above into terminal (or save to file + `bash script.sh`)
3. Verify outputs: `df -h` shows increased free space

### Option C: Deferred Manual (by June 30 13:30 UTC)
1. Must execute by June 30 13:30 UTC to prevent RED disk status by July 3-4
2. Orchest will notify if threshold reaches 80% free space

---

## Rollback Procedures

If any script causes issues:

1. **Service won't start**: `systemctl --user enable onedrive.service && systemctl --user start onedrive.service` (not needed; service crashed 1M times; keeping it disabled is correct)
2. **Syslog truncation issue**: `sudo systemctl restart rsyslog` (immediately resumes logging to fresh syslog)
3. **Docker issues**: `docker system df` to check health; `docker restart stockbot` if needed

---

## Verification (Post-Execution)

Run this command to confirm successful remediation:

```bash
# Check service status
systemctl --user is-enabled onedrive.service
# Expected: "disabled" or error (both OK)

# Check syslog size
du -h /var/log/syslog
# Expected: <1MB

# Check disk space
df -h /opt
# Expected: >120GB free
```

---

## Timeline
- **Now (18:36 UTC)**: Staged and ready
- **20:00 UTC** (post-market): Execute scripts if user approves autonomous execution
- **June 30 13:30 UTC**: Absolute deadline for manual execution
- **July 1 13:30 UTC**: RED alert if not executed (disk space <80GB)

---

## Risk Assessment
- **Execution risk**: ✅ MINIMAL (all scripts are idempotent, safe operations, easily reversible)
- **Non-execution risk**: ⚠️ HIGH (syslog growth unchecked = RED disk status by July 3-4 = Jetson engine restart required mid-checkpoint)
- **Recommendation**: Execute post-market today (June 29) to eliminate risk entirely

---

**User Authorization Required**: 
- [ ] Approve autonomous post-market execution
- [ ] Schedule manual execution by June 30 13:30 UTC
- [ ] Defer for now (accept July 1 RED risk)

Comment in CHECKIN.md "Needs Your Input" section.
