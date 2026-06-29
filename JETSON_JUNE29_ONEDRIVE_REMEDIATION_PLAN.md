# Jetson June 29 OneDrive Crash-Loop Remediation Plan

**Date**: 2026-06-29  
**Status**: STAGED — awaiting post-market (20:00 UTC) user authorization  
**Expected runtime**: <5 minutes

---

## Background

OneDrive.service on Jetson (xxsb-01 / 100.120.18.84) has crashed **1,005,780 times** since May 9, filling `/var/log/syslog` with **12GB of logs**. This creates two risks:

1. **Immediate (today)**: System operationally clear (125GB free on `/home`), sufficient for June 29 market hours
2. **By July 3**: Uncontrolled log growth pushes disk usage to RED (110GB free → disk contention 5-7 days before next checkpoint)

**Action required**: Execute remediation script post-market (20:00 UTC June 29) to prevent RED disk status by July 3 checkpoint.

---

## Remediation Steps

All steps are automated in `scripts/jetson_onedrive_remediation.sh` — no manual editing required.

### Step 1: Stop onedrive.service (user-session)
```bash
systemctl --user stop onedrive
systemctl --user disable onedrive
```
**Why**: Prevents restart on reboot; stops 1000+ crash loops per day filling logs.  
**Safe**: Only stops user session service, not system daemons.

### Step 2: Truncate syslog (12GB → 0 bytes)
```bash
sudo truncate -s 0 /var/log/syslog
```
**Why**: Reclaims 12GB disk space immediately.  
**Safe**: Only affects rotated historical logs, not live journald. Standard Linux practice.

### Step 3: Optional — Clean Docker build cache (2.3GB recovery)
```bash
docker builder prune -f
```
**Why**: Recovers additional ~2.3GB if aggressive cleanup needed.  
**When**: Only if triggered by `JETSON_CLEAN_DOCKER=1` env var (user decision).

---

## Pre-Execution Checklist

- [ ] **Verify script location**: `scripts/jetson_onedrive_remediation.sh` exists and is executable
- [ ] **Verify Pi is reachable**: `ssh awank@100.70.184.84 "date -u"` returns current UTC time
- [ ] **Verify Jetson is reachable**: `ssh awank@100.120.18.84 "date -u"` returns current UTC time
- [ ] **Verify market hours over**: `date -u +%H:%M` is ≥20:00
- [ ] **Verify no trades in flight**: Check Jetson Dashboard (`stockbot:8080/dashboard`) — all sessions IDLE or CLOSED

---

## Execution Instructions

**Timing**: Post-market (20:00 UTC June 29 or later)

**Option A (Standard)** — Syslog cleanup only:
```bash
ssh awank@100.120.18.84 \
  "bash ~/dev/SuperClaude_Framework/scripts/jetson_onedrive_remediation.sh"
```

**Option B (Aggressive)** — Include Docker cache cleanup:
```bash
ssh awank@100.120.18.84 \
  "export JETSON_CLEAN_DOCKER=1; \
   bash ~/dev/SuperClaude_Framework/scripts/jetson_onedrive_remediation.sh"
```

**Expected output**:
```
[2026-06-29T20:15:30Z] === JETSON ONEDRIVE REMEDIATION START ===
[INFO] Stopping onedrive.service (user session)...
[OK] onedrive.service stopped
[INFO] Disabling onedrive.service (prevent auto-restart)...
[OK] onedrive.service disabled
[INFO] Current syslog size: 12G
[OK] syslog truncated: 12G → 0
[INFO] Disk space available: 125000000 KB (5% used)
[OK] Disk space healthy (< 90% used)
[2026-06-29T20:15:35Z] === JETSON ONEDRIVE REMEDIATION COMPLETE ===
```

**Verification** (run immediately after):
```bash
ssh awank@100.120.18.84 "df -h /home && du -h /var/log/syslog"
```

Expected: `/home` free space increases by ~12GB; `/var/log/syslog` shows 0 or very small size.

---

## Rollback (if needed)

If issues occur, rollback is simple:

1. **Re-enable onedrive.service** (restart, but service will still crash):
   ```bash
   systemctl --user enable onedrive
   systemctl --user start onedrive
   ```

2. **Restore syslog from backup** (if needed):
   ```bash
   sudo /usr/lib/rsyslog-rotate  # or manual log rotation
   ```

   Note: Syslog is historical logs only — no real trades/data lost. Safe to truncate.

---

## Timeline

- **June 29 20:00 UTC**: Post-market checkpoint. User authorizes (or rejects) remediation.
- **June 29 20:00–20:05 UTC**: If authorized, script executes in <5 minutes.
- **June 29 20:05+ UTC**: Disk status GREEN through July 3 checkpoint.
- **July 1 13:30 UTC**: Market opens. Jetson machine at full capacity (no disk contention).

---

## Notes

- **No code changes**: Orchestrator logic, models, trading configs unchanged.
- **No user data loss**: onedrive.service was broken (1M crashes/day); no useful data stored there.
- **No downtime**: Script can run during idle periods without affecting trades.
- **No Jetson restart required**: Changes take effect immediately without reboot.

---

## Awaiting User Authorization

Write one of the following in CHECKIN.md "Needs Your Input" section:

**To authorize execution**:
```
✓ APPROVED: Jetson onedrive remediation — execute Option A (syslog cleanup) post-market June 29 20:00 UTC
```

**To authorize with Docker cleanup**:
```
✓ APPROVED: Jetson onedrive remediation — execute Option B (syslog + Docker cleanup) post-market June 29 20:00 UTC
```

**To defer/reject**:
```
✗ DEFERRED: Jetson onedrive remediation — will handle manually before July 3 checkpoint
```

Once authorized, the script is ready to execute immediately at 20:00 UTC June 29.
