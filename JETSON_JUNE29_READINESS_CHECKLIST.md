# Jetson June 29 Post-Market Readiness Checklist

**Status**: Ready for user authorization  
**Timeline**: Execute 20:00 UTC+ (post-market)  
**Estimated duration**: 5 minutes  
**Risk level**: LOW (reversible, service-level only, no code changes)

## Context

Jetson system audit (Session 4507) found:
- **onedrive.service crash-loop**: 1,005,780 crashes since May 9
- **syslog impact**: 12GB of logs (125GB disk free currently)
- **Timeline risk**: Without remediation, disk contention RED by July 3-4

## Remediation Steps

### Step 1: Stop onedrive.service (30 sec)
```bash
ssh awank@100.120.18.84
systemctl --user stop onedrive.service
```
**Verification**: `systemctl --user is-active onedrive.service` → should return inactive

### Step 2: Disable onedrive.service (30 sec)
```bash
systemctl --user disable onedrive.service
```
**Verification**: `systemctl --user is-enabled onedrive.service` → should return inactive

### Step 3: Truncate syslog (1 min)
```bash
sudo truncate -s 0 /var/log/syslog
```
**Verification**: `du -sh /var/log/syslog` → should show ~4KB (system baseline)

### Step 4: Verify disk status (1 min)
```bash
df -h /
```
**Expected**: 100GB+ free disk (was 125GB, now 113GB+ after truncate)

## Rollback Procedures

If remediation causes issues:

### Re-enable onedrive
```bash
systemctl --user enable onedrive.service
systemctl --user start onedrive.service
```

### Restore syslog from previous day
```bash
# Syslog archives are in /var/log/
ls -la /var/log/syslog*
zcat /var/log/syslog.1.gz | head -1000 > /var/log/syslog
```

## Decision Gates

**PROCEED if**:
- ✅ User confirms understanding (service will no longer auto-start)
- ✅ Disk free currently >100GB (verified as 125GB)
- ✅ Stockbot container is healthy (verified 2026-06-29 14:11 UTC)

**HOLD if**:
- ❌ onedrive.service needed for daily backup (discuss alternative approach)
- ❌ Disk free <100GB (skip and use Docker cache cleanup instead)

## Automated Script

All steps can be executed via pre-staged script:
```bash
ssh awank@100.120.18.84 'bash /opt/stockbot/scripts/jetson_onedrive_remediation.sh'
```

(Script file: `jetson_onedrive_remediation.sh` — staged for post-market execution)

## Timeline

- **June 29 20:00 UTC+**: User confirms proceed
- **June 29 20:05 UTC**: Remediation complete (5 min execution)
- **June 30-July 3**: System operates with clean syslog
- **July 3-4**: Disk would be RED without this fix (syslog would grow to 24GB+)

## Confidence

95% (remediation is mechanical, onedrive is user-session service not critical for trading)

---

**Orchestrator Note**: This item is queued as Item 32 in PROJECTS.md Exploration Queue. Ready for post-market user authorization trigger (20:00 UTC+).
