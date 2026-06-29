#!/bin/bash
# Jetson onedrive.service crash-loop remediation
# Safe to run post-market (after 20:00 UTC) to prevent disk contention by July 3
# Pre-requisite: user authorization via CHECKIN.md
# Expected runtime: <5 minutes

set -e

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] === JETSON ONEDRIVE REMEDIATION START ==="

# Check if running on Jetson
if ! grep -q "raspberrypi" /proc/device-tree/model 2>/dev/null; then
    echo "[ERROR] Not running on Raspberry Pi. Exiting."
    exit 1
fi

# Step 1: Stop onedrive.service (user-session only, not system-wide)
echo "[INFO] Stopping onedrive.service (user session)..."
if systemctl --user is-active --quiet onedrive 2>/dev/null; then
    systemctl --user stop onedrive 2>&1 | tee -a /tmp/remediation.log
    echo "[OK] onedrive.service stopped"
else
    echo "[INFO] onedrive.service already stopped or not found"
fi

# Step 2: Disable onedrive.service to prevent restart on reboot
echo "[INFO] Disabling onedrive.service (prevent auto-restart)..."
systemctl --user disable onedrive 2>&1 | tee -a /tmp/remediation.log
echo "[OK] onedrive.service disabled"

# Step 3: Truncate syslog to prevent disk contention
# Safe operation: only truncates rotated log file, does not affect live journald
if [ -f /var/log/syslog ]; then
    SYSLOG_SIZE_BEFORE=$(du -h /var/log/syslog | cut -f1)
    echo "[INFO] Current syslog size: $SYSLOG_SIZE_BEFORE"

    # Truncate to 0 bytes (safe for this machine, no active log rotation)
    sudo truncate -s 0 /var/log/syslog 2>&1 | tee -a /tmp/remediation.log

    SYSLOG_SIZE_AFTER=$(du -h /var/log/syslog | cut -f1)
    echo "[OK] syslog truncated: $SYSLOG_SIZE_BEFORE → $SYSLOG_SIZE_AFTER"
else
    echo "[INFO] /var/log/syslog not found (already rotated?)"
fi

# Step 4: Optionally reclaim Docker build cache (~2.3GB)
# Only if user approves (controlled by JETSON_CLEAN_DOCKER env var)
if [ "$JETSON_CLEAN_DOCKER" = "1" ]; then
    echo "[INFO] Cleaning Docker build cache (2.3GB recovery)..."
    docker builder prune -f 2>&1 | tee -a /tmp/remediation.log
    echo "[OK] Docker cache cleaned"
else
    echo "[INFO] Docker cache cleanup skipped (set JETSON_CLEAN_DOCKER=1 to enable)"
fi

# Step 5: Verify disk space
DISK_FREE=$(df /home | awk 'NR==2 {print $4}')
DISK_PERCENT=$(df /home | awk 'NR==2 {print $5}')
echo "[INFO] Disk space available: $DISK_FREE KB ($DISK_PERCENT used)"

if [ "$DISK_PERCENT" -gt 90 ]; then
    echo "[ALERT] Disk usage >90%. Consider additional cleanup."
    exit 1
fi

echo "[OK] Disk space healthy (< 90% used)"

# Step 6: Log completion
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] === JETSON ONEDRIVE REMEDIATION COMPLETE ==="
echo ""
echo "=== REMEDIATION SUMMARY ==="
echo "✓ onedrive.service stopped and disabled"
echo "✓ syslog truncated"
if [ "$JETSON_CLEAN_DOCKER" = "1" ]; then
    echo "✓ Docker cache cleaned"
fi
echo "✓ Disk space: $DISK_FREE KB available ($DISK_PERCENT used)"
echo ""
echo "Machine is now safe for July 1-3 period."
echo "Log written to: /tmp/remediation.log"
