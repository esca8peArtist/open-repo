---
title: "Phase 3 Ransomware Recovery Plan"
project: cybersecurity-hardening
phase: 3
status: research-complete
created: 2026-05-21
target-execution: June–July 2026
confidence: high
---

# Phase 3: Ransomware Recovery Plan

**Most critical finding**: The 3-2-1 backup rule is no longer sufficient for ransomware protection. The original rule predates ransomware as a dominant threat. Modern ransomware operators specifically hunt for and destroy backup systems before triggering encryption — including cloud-synced backups (Dropbox, Google Drive, OneDrive) and connected external drives. The evolved standard is the **3-2-1-1-0 rule**: three copies, two media types, one offsite, **one immutable**, **zero errors** (verified restore). Immutability is the non-negotiable addition.

---

## 1. Backup Strategy: The 3-2-1-1-0 Rule

| Copy | Location | Media | Immutable? | Tool |
|---|---|---|---|---|
| Primary | Local system | NVMe/SSD | No | Live system |
| Copy 1 | External drive | USB HDD | Partial (disconnected) | restic |
| Copy 2 | Cloud (Backblaze B2) | Object storage | Yes (Object Lock) | restic |
| Copy 3 | Second cloud / friend's offsite | Object storage | Yes | restic |

**Why Backblaze B2**: Backblaze B2 offers Object Lock (true immutability — even the account owner cannot delete before the retention period expires), generous free tier (10 GB), and very low cost ($6/TB/month for storage, $0.01/GB download). For home lab backup volumes (10–100 GB), monthly cost is negligible.

**The "zero errors" requirement**: Every backup must be tested. A backup you have never restored is a backup you do not have. See Section 5 for restore drill protocol.

---

## 2. Immutable Backup Implementation: restic + Backblaze B2

### Why restic

restic is open-source, cross-platform, encrypted by default, and performs cryptographic verification of backup integrity natively. Every snapshot is content-addressed; restic detects any tampering or corruption before restore. It supports incremental backups (only changed chunks are uploaded), making it bandwidth-efficient for home lab use.

### Setup

**Install restic**:
```bash
# Debian/Ubuntu/Raspberry Pi OS
sudo apt install restic

# Or download binary directly
curl -LO https://github.com/restic/restic/releases/latest/download/restic_linux_arm64.bz2
bunzip2 restic_linux_arm64.bz2 && chmod +x restic_linux_arm64 && sudo mv restic_linux_arm64 /usr/local/bin/restic
```

**Create Backblaze B2 bucket with Object Lock**:
1. Log into Backblaze console
2. Create a new bucket: `homelab-backups-immutable`
3. Enable "Object Lock" with default retention mode "Compliance", retention period 30 days
4. Create an Application Key with read/write access to this bucket only — never use the master key for backups
5. Set lifecycle rules: hide deleted objects after 1 day, delete hidden objects after 31 days (preserves 30-day immutability window)

**Initialize restic repository on B2**:
```bash
export B2_ACCOUNT_ID="your_account_id"
export B2_ACCOUNT_KEY="your_app_key"
export RESTIC_PASSWORD="your_strong_passphrase"

restic -r b2:homelab-backups-immutable init
```

Store the `RESTIC_PASSWORD` in a password manager (Bitwarden) AND on a printed sheet stored physically offsite. If you lose the passphrase, the backup is permanently inaccessible.

**Backup script** (`/usr/local/bin/backup-homelab.sh`):
```bash
#!/bin/bash
set -euo pipefail

export B2_ACCOUNT_ID="your_account_id"
export B2_ACCOUNT_KEY="your_app_key"
export RESTIC_PASSWORD="your_strong_passphrase"
REPO="b2:homelab-backups-immutable"

# Backup stockbot data and config
restic -r "$REPO" backup \
  /home/pi/stockbot/data \
  /home/pi/stockbot/config \
  /home/pi/.env \
  --tag stockbot \
  --exclude "*.pyc" \
  --exclude "__pycache__"

# Backup seedwarden
restic -r "$REPO" backup \
  /home/pi/seedwarden \
  --tag seedwarden

# Verify the latest snapshot
restic -r "$REPO" check

# Remove snapshots older than 90 days (B2 Object Lock still protects the 30-day window)
restic -r "$REPO" forget \
  --keep-daily 7 \
  --keep-weekly 4 \
  --keep-monthly 3 \
  --prune

echo "Backup completed: $(date)"
```

**Schedule with systemd timer** (preferred over cron for reliability):
```ini
# /etc/systemd/system/homelab-backup.service
[Unit]
Description=Homelab restic backup to B2
After=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup-homelab.sh
StandardOutput=journal
StandardError=journal

# /etc/systemd/system/homelab-backup.timer
[Unit]
Description=Run homelab backup daily at 02:00

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```
```bash
sudo systemctl enable --now homelab-backup.timer
```

---

## 3. Recovery Time Objective (RTO) and Recovery Point Objective (RPO)

| System | RTO Target | RPO Target | Rationale |
|---|---|---|---|
| stockbot (trading bot) | 4 hours | 24 hours | Financial impact if down; nightly backups acceptable |
| seedwarden (sensor data) | 24 hours | 24 hours | Low financial impact; data loss of 1 day acceptable |
| open-repo (public tool) | 48 hours | 7 days | No financial impact; weekly backup sufficient |
| Home NAS / file server | 8 hours | 24 hours | Personal data; requires recovery before returning to work |

**RTO = how long you can tolerate the system being down**
**RPO = how much data loss (time window) is acceptable**

These are personal decisions. The targets above are conservative and achievable with the restic + B2 setup.

---

## 4. Disaster Recovery Simulation: Annual Restore Drill

A backup that has never been tested is not a backup. Run this drill annually (calendar it for the first weekend of January each year).

**Drill procedure**:
1. Provision a clean VM or spare Pi
2. Install OS from scratch (do not restore OS image — restore data only)
3. Install restic: `sudo apt install restic`
4. Set environment variables (use the password from your password manager)
5. List available snapshots: `restic -r b2:homelab-backups-immutable snapshots`
6. Restore to a staging directory: `restic -r b2:homelab-backups-immutable restore latest --target /tmp/restore-test/`
7. Verify file integrity: compare checksums of critical files against known-good values
8. Bring up the application (e.g., stockbot) against the restored data and confirm it functions
9. Document: how long did the restore take? What was the file size? Any errors?
10. Update RTO estimate based on actual observed restore time

**What to verify**:
- Data completeness: are all expected files present?
- Data integrity: restic verifies checksums automatically; check for any "corrupt chunk" warnings
- Application functionality: can the application actually run against the restored data?
- Secret recovery: can you retrieve all necessary credentials from your password manager to reconfigure the application?

---

## 5. Ransomware Incident Response Steps

### Detection

Ransomware indicators:
- Files renamed with unknown extensions (`.locked`, `.encrypted`, `.crypted`, random 6-char suffix)
- Ransom note files (`README.txt`, `HOW_TO_DECRYPT.txt`) appearing in directories
- Wazuh FIM alert: mass file modification events across multiple directories in short time window
- Dramatically elevated disk I/O on the system (ransomware is CPU and I/O intensive during encryption)
- System becomes sluggish or unresponsive

**Immediate response (first 5 minutes)**:
1. Do NOT pay ransom without law enforcement consultation — decryption keys are frequently never provided even after payment, and payment funds further attacks
2. Power off the affected system immediately — pulling the power cord is acceptable if ransomware is actively encrypting; it stops encryption mid-process and may preserve some files
3. Isolate from network: disconnect ethernet, disable WiFi, remove from Tailscale

### Notification

**Within 72 hours** (if applicable):
- CISA Report (US): `report@cisa.dhs.gov` or `1-888-282-0870`
- FBI IC3 (Internet Crime Complaint Center): `ic3.gov`
- Local FBI field office if financial losses exceed $1,000

Notification is not legally required for purely personal systems in the US, but reporting helps threat intelligence sharing that protects others. If the compromised system processed any personal data of third parties (contacts, clients, etc.), consult a lawyer about notification obligations.

### Containment and Assessment

1. Do not attempt to clean the ransomware in place — assume the system is fully compromised
2. Assess blast radius: which other systems did the infected machine have network/SSH access to?
3. Check whether backup systems are also compromised:
   - Is the external USB drive currently connected? If so, it may be encrypted too
   - Check the B2 bucket via the Backblaze web console (not from the infected machine) — Object Lock protects against API-level deletion but not against encryption of already-uploaded data if restic was running at the time of infection
4. Identify the oldest clean backup snapshot: `restic -r b2:homelab-backups-immutable snapshots --tag stockbot`

### Recovery

1. Provision a clean system (fresh OS install)
2. Restore from the most recent clean snapshot (before the ransomware infection timestamp)
3. If the most recent snapshot is also encrypted (rare with proper immutable backups): go back to an older snapshot before the infection window. Object Lock ensures these older snapshots cannot have been deleted by the ransomware.
4. Change all credentials that were accessible from the compromised machine
5. Identify and patch the initial access vector before restoring network connectivity

### Post-Incident

1. Preserve the encrypted disk image if possible (law enforcement may need it; future decryptors may be released — see `nomoreransom.org` for available free decryptors)
2. Submit ransomware sample to `nomoreransom.org` to identify the ransomware family
3. Document the attack timeline for your records
4. Review whether backup immutability held (it should have under the described setup)
5. Update Wazuh detection rules to catch the specific initial access vector

---

## 6. Ransomware Insurance

**Current state (2026)**: Ransomware insurance for individuals and small home labs is largely unavailable as a standalone product. Coverage typically comes through:

- **Homeowners/renters insurance** — some policies include cyber coverage as a rider ($5–15/month additional). Typical limits: $25,000–$100,000. Read the exclusions carefully: many exclude "business use" which could affect stockbot if it generates income.
- **Small business cyber insurance** — if any home lab project constitutes a business, cyber liability policies from insurers like Chubb, AIG, or Coalition start at ~$500–1,500/year for $1M coverage. Coalition offers incident response retainer included in the policy.
- **Credit card purchase protection** — some premium cards (Amex Platinum, Chase Sapphire Reserve) include cyber security services as a cardholder benefit.

**Filing a ransomware insurance claim**:
1. Contact insurer immediately upon detection (most policies have 24–72 hour notification requirements)
2. Preserve evidence: do not wipe the affected system until the insurer's forensic team has assessed it (or explicitly waives this requirement)
3. Document all costs: incident response labor (even your own time), hardware replacement, data recovery, business interruption losses
4. Get a formal incident report number from IC3 or local law enforcement — insurers require this

**Known gap**: Cyber insurance claims for ransomware have faced significant insurer resistance, with insurers invoking "act of war" exclusions when ransomware is attributed to nation-state actors. This legal question is unresolved as of 2026. Do not rely on insurance as the primary recovery mechanism — the restic + B2 immutable backup setup is your primary recovery path.

---

## 7. Confidence Levels and Known Gaps

**High confidence**: restic + B2 with Object Lock is a production-proven, technically sound immutable backup architecture. The 3-2-1-1-0 rule is the current industry standard.

**High confidence**: The incident response procedure follows current NIST SP 800-61 Rev. 3 guidance (2025).

**Medium confidence**: Annual restore drills are well-established best practice but frequently not executed in home lab settings. The drill procedure described is straightforward; the risk is not doing it.

**Known gap**: Pre-ransomware detection. Wazuh FIM provides post-encryption detection (files have already been encrypted when the alert fires). True pre-encryption detection requires behavioral analytics that identify the ransomware process before it finishes encrypting. This requires commercial EDR. For home lab threat models, detecting ransomware within minutes of start and limiting loss to the RPO window (24 hours) is acceptable.

**Known gap**: Backup encryption key management. The restic passphrase is the single point of failure for recovery. Losing it makes all B2 backups permanently inaccessible. Mitigation: store in Bitwarden AND on a printed sheet in a physically secure, offsite location (safe deposit box, trusted family member's home).

---

## Sources

- [Restic + Backblaze B2 — Ransomware-Resistant Backup](https://medium.com/@benjamin.ritter/how-to-do-ransomware-resistant-backups-properly-with-restic-and-backblaze-b2-e649e676b7fa)
- [3-2-1-1-0 Backup Rule Explained](https://i3businesssolutions.com/the-3-2-1-1-0-backup-rule-explained/)
- [Ransomware-Resistant Hosting Backup Strategy](https://www.dchost.com/blog/en/ransomware-resistant-hosting-backup-strategy-3-2-1-immutable-copies-and-real-air-gaps/)
- [The 3-2-1 Backup Rule for Modern Threats (March 2026)](https://medium.com/@frankd228801/the-3-2-1-backup-rule-a-framework-built-for-modern-threats-221966875071)
- [Veeam — 3-2-1 Backup Rule Explained](https://www.veeam.com/blog/321-backup-rule.html)
- [Arcserve — 3-2-1-1 Strategy for Ransomware](https://www.arcserve.com/blog/how-protect-against-ransomware-3-2-1-1-strategy)
- [NIST SP 800-61 Rev. 3 — Incident Response](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [NIST 800-61 Rev. 3 Framework Analysis](https://linfordco.com/blog/nist-sp-800-61/)
- [No More Ransom — Free Decryption Tools](https://www.nomoreransom.org)
