# Linux Full-Disk Encryption Architecture

**Purpose**: Pre-stage Phase 2 infrastructure for comprehensive FDE deployment on home Linux machine. Enables immediate execution once Phase 1 VeraCrypt restart (Windows) completes.

**Created**: 2026-06-23 (Session 4027)  
**Target deployment**: After Phase 1 VeraCrypt checkpoint  
**Confidence**: 82%

---

## 1. Executive Summary

This architecture document specifies a production-grade full-disk encryption (FDE) implementation for a home Linux machine using LUKS2, with TPM2 automatic unlock, recovery key escrow, encrypted swap, and a comprehensive backup encryption strategy.

**Key design decisions**:
- **Primary encryption**: LUKS2 (dm-crypt backend) — industry standard for Linux, battle-tested since 2016, supports key rotation and media degradation
- **Unlock mechanism**: TPM2 + systemd-cryptsetup integration for transparent boot-time unlock; fallback to recovery key for BIOS/firmware resets
- **Key material storage**: TPM2 sealed keys (primary), hardware security module (secondary recovery), passphrase backup (tertiary)
- **Encrypted volumes**: Root filesystem (/), /home partition, swap, /tmp, /var/log (separate encrypted volumes for compartmentalization)
- **Backup strategy**: Rclone encrypted to cloud (password + TPM seal), unencrypted local backup on encrypted external SSD, quarterly full-disk snapshot to S3 (encrypted at rest)

**Architecture rationale**:
- LUKS2 is the Linux standard for FDE and universally supported across distributions
- TPM2 eliminates password entry on every boot while maintaining security (keys never touch unencrypted storage)
- Multi-key strategy (TPM + HSM + passphrase) ensures key recovery under any failure scenario
- Compartmentalized encrypted volumes (separate /home, swap, logs) provides defense-in-depth — compromise of one volume doesn't expose all data

**Threat model coverage**:
- ✅ Stolen laptop with powered-off drive (encrypted at rest; TPM resets on physical tampering)
- ✅ Live forensic extraction (sealed TPM keys, passphrase only brute-force vulnerable)
- ✅ Cold boot attack (encrypted swap, /var/log separation prevents memory residue exfiltration)
- ✅ Ransomware infection (snapshots + versioning backup, immutable copy preserved offline)
- ✅ BIOS/firmware compromise (recovery key escrow enables alternative unlock path)

**Timeline**: 6-8 hours for initial deployment (LUKS2 setup + TPM sealing + backup configuration) + 2-3 hours for backup validation + ongoing quarterly maintenance

---

## 2. LUKS2 Volume Architecture

### 2.1 Volume Strategy

Deploy **four separate LUKS2 volumes** on the Linux machine:

| Volume | Mount Point | Use Case | Size | Encryption Key | Unlock Method |
|--------|------------|----------|------|---|---|
| **luks_root** | / | OS, system binaries, configuration | 80 GB | TPM2-sealed | Boot-time TPM unlock |
| **luks_home** | /home | User data, documents, source code | 200 GB | TPM2-sealed | Boot-time TPM unlock + passphrase fallback |
| **luks_swap** | swap | Virtual memory (encrypted at rest) | 16 GB | Random key at boot | Keyfile stored in initramfs |
| **luks_tmp** | /tmp, /var/log | Temporary files, logs (volatile data) | 20 GB | Random key at boot | Keyfile in initramfs, wiped on shutdown |

**Rationale for separation**:
- **Root encryption** prevents OS tampering; TPM unlock enables unattended boot
- **/home encryption** isolates user data; separate key allows revocation without OS reinstall
- **Encrypted swap** prevents memory disclosure via hibernation or crash dumps
- **Encrypted /tmp + /var/log** compartmentalizes volatile data; separate lifecycle management (destroy keys at shutdown for /tmp, rotate /var/log quarterly)

### 2.2 Partition Layout (Before LUKS2)

```
/dev/nvme0n1
├── /dev/nvme0n1p1  → 512 MB    (EFI partition, unencrypted, signed bootloader)
├── /dev/nvme0n1p2  → 1 GB      (LUKS2 /boot — encrypted kernel + initramfs)
├── /dev/nvme0n1p3  → 80 GB     (LUKS2 / — root filesystem)
├── /dev/nvme0n1p4  → 200 GB    (LUKS2 /home — user data)
├── /dev/nvme0n1p5  → 16 GB     (LUKS2 swap)
└── /dev/nvme0n1p6  → 20 GB     (LUKS2 /tmp + /var/log)
```

**Boot partition encryption**:
- **/boot must be encrypted** to prevent kernel tampering (malicious kernel → TPM keys compromised)
- GRUB bootloader handles passphrase entry → TPM unlock
- Requires Secure Boot enabled (prevent pre-boot attack via bootloader substitution)

### 2.3 LUKS2 Setup Procedure

**Phase 1: Backup & ISO preparation**
```bash
# 1. Full unencrypted backup to external USB SSD
rsync -avX --delete /home/ /media/backup_external_ssd/home_backup/
rsync -avX --delete / /media/backup_external_ssd/root_backup/ --exclude={/proc,/sys,/dev,/run,/boot,/media,/mnt,/tmp}

# 2. Create GRUB-bootable Linux ISO (Ubuntu 24.04 LTS recommended)
# Download: ubuntu-24.04-live-server-amd64.iso
# Write to USB: sudo dd if=ubuntu-24.04-live-server-amd64.iso of=/dev/sdX bs=4M sync
```

**Phase 2: LUKS2 volume creation (from live ISO)**
```bash
# Boot from USB ISO (interrupt GRUB with 'e', add 'cryptdevice=' params to kernel args if needed)

# Open existing unencrypted partitions
sudo cryptsetup luksFormat --type luks2 --cipher aes-xts-plain64 --key-size 512 --hash sha256 /dev/nvme0n1p3
sudo cryptsetup luksFormat --type luks2 --cipher aes-xts-plain64 --key-size 512 --hash sha256 /dev/nvme0n1p4
sudo cryptsetup luksFormat --type luks2 --cipher aes-xts-plain64 --key-size 512 --hash sha256 /dev/nvme0n1p5
sudo cryptsetup luksFormat --type luks2 --cipher aes-xts-plain64 --key-size 512 --hash sha256 /dev/nvme0n1p6

# Open encrypted volumes
sudo cryptsetup luksOpen /dev/nvme0n1p3 luks_root
sudo cryptsetup luksOpen /dev/nvme0n1p4 luks_home
sudo cryptsetup luksOpen /dev/nvme0n1p5 luks_swap
sudo cryptsetup luksOpen /dev/nvme0n1p6 luks_tmp

# Format filesystems
sudo mkfs.ext4 /dev/mapper/luks_root
sudo mkfs.ext4 /dev/mapper/luks_home
sudo mkswap /dev/mapper/luks_swap
sudo mkfs.ext4 /dev/mapper/luks_tmp
```

**Phase 3: Restore from backup**
```bash
# Mount encrypted volumes
sudo mount /dev/mapper/luks_root /mnt/root
sudo mount /dev/mapper/luks_home /mnt/root/home
sudo mkdir -p /mnt/root/tmp /mnt/root/var/log
sudo mount /dev/mapper/luks_tmp /mnt/root/tmp

# Restore from backup
sudo rsync -avX /media/backup_external_ssd/root_backup/ /mnt/root/ --exclude={/boot,/home,/tmp,/var/log}
sudo rsync -avX /media/backup_external_ssd/home_backup/ /mnt/root/home/

# Regenerate /boot with encrypted kernel/initramfs
sudo chroot /mnt/root
sudo update-initramfs -u -k all
sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=grub /dev/nvme0n1
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

---

## 3. TPM2 Integration & Sealing

### 3.1 TPM2 Overview

**TPM2 (Trusted Platform Module 2.0)** is a hardware security chip present on most modern Linux laptops. It provides:
- **Sealed key storage**: Keys locked to specific firmware/OS state (measurement register values); inaccessible if firmware/bootloader modified
- **Attestation**: Cryptographic proof that OS booted unmodified
- **Secure random number generation**: NIST-certified entropy source
- **Transparent boot-time unlock**: No user passphrase entry required (unless TPM is reset/tampered)

### 3.2 TPM2 Sealed Key Setup with systemd-cryptsetup

```bash
# 1. Check TPM2 availability
sudo systemctl status tpm2-abrmd
# If not running: sudo systemctl enable --now tpm2-abrmd

# 2. Seal LUKS passphrase to TPM2 (for /dev/nvme0n1p3 luks_root)
# Measure current boot state:
tpm2_pcrread -o pcr.bin sha256:0,1,2,3,7

# Create sealed key:
echo "YOUR_LUKS_PASSPHRASE" | tpm2_createprimary -C e -c primary.ctx
tpm2_create -C primary.ctx -g sha256 -G aes -r sealed_key.priv -u sealed_key.pub -L "pcr:sha256:0,1,2,3,7" -i-  << EOF
YOUR_LUKS_PASSPHRASE
EOF

# Persist sealed key to TPM2:
tpm2_evictcontrol -C o -c sealed_key.priv 0x81000001

# Verify:
tpm2_readpublic -c 0x81000001
```

### 3.3 Boot-Time Integration (systemd-cryptsetup)

**File**: `/etc/crypttab` — configure encrypted volume unlock at boot

```
# /etc/crypttab
# Format: name  device  key_file  options

luks_root  /dev/nvme0n1p3  -  x-systemd.device-timeout=0,x-systemd.requires=initrd-root-fs.target
luks_home  /dev/nvme0n1p4  /etc/luks_keys/home.key  x-systemd.device-timeout=0
luks_swap  /dev/nvme0n1p5  /etc/luks_keys/swap.key  x-systemd.device-timeout=0
luks_tmp   /dev/nvme0n1p6  /etc/luks_keys/tmp.key   x-systemd.device-timeout=0
```

**Unlock via TPM2 at boot** — use `initramfs` hook (systemd-cryptsetup checks TPM before prompting passphrase):

```bash
# Install systemd-cryptsetup generator
sudo apt install systemd

# Generate initramfs with TPM2 unlock:
sudo cryptsetup config /dev/nvme0n1p3 --tpm2-device=auto --tpm2-pcrs=0,1,2,3,7

# Regenerate initramfs
sudo update-initramfs -u -k all
```

**Fallback mechanism**:
- If TPM2 unlock fails (firmware tamper detected, TPM reset), systemd-cryptsetup prompts for passphrase manually
- Recovery key stored in `/etc/luks_keys/recovery.key` enables alternative unlock (details in Section 5)

### 3.4 TPM2 PCR Measurements

**PCR (Platform Configuration Register) index** controls what boot state triggers TPM unlock:

| PCR | Measures | Locked to |
|-----|----------|-----------|
| **0** | BIOS/UEFI firmware | Firmware hash |
| **1** | BIOS configuration | BIOS settings |
| **2** | Option ROM code | Expansion cards |
| **3** | Option ROM configuration | Card settings |
| **7** | Secure Boot state | Secure Boot enabled/disabled, signed binaries |

**Sealing to PCRs 0,1,2,3,7** means:
- ✅ TPM unlock works as long as BIOS firmware, Secure Boot, and bootloader are unchanged
- ❌ If BIOS is updated or modified → TPM unlock fails → passphrase prompt (recovery key available)
- ❌ If Secure Boot disabled → TPM unlock fails (security-conscious design)

**Risk**: BIOS updates reset TPM — will require passphrase entry (acceptable for home machine, annoying for frequent BIOS updates). Mitigated by recovery key escrow.

---

## 4. Key Management Strategy

### 4.1 Three-Layer Key Hierarchy

```
┌─────────────────────────────────┐
│  LAYER 1: TPM2 Sealed Keys      │  Primary unlock mechanism
│  (luks_root, luks_home)         │  Transparent boot, auto-unlock
│  Location: TPM2 chip            │  Lost if: firmware tamper, TPM reset
└─────────────────────────────────┘
            ↓ Fallback
┌─────────────────────────────────┐
│  LAYER 2: Hardware Security     │  Secondary unlock (offline)
│  Module (YubiKey/Titan)         │  Offline decryption, backup restore
│  Location: USB security key     │  Lost if: security key stolen + no backup
└─────────────────────────────────┘
            ↓ Fallback
┌─────────────────────────────────┐
│  LAYER 3: Recovery Passphrase   │  Tertiary unlock (manual)
│  (26-character random)          │  Paper backup, offline storage
│  Location: Paper + encrypted    │  Lost if: paper burned + no digital copy
│  digital backup                 │
└─────────────────────────────────┘
```

### 4.2 Key Material Storage

**LUKS passphrase** — Random 26-character string (not used day-to-day):
```bash
# Generate passphrase
openssl rand -base64 20 | head -c 26
# Example: xB8k2mJ9Lp5Qr7Vw3Xn6Ys

# Store encrypted copy in password manager
# - Bitwarden: LUKS_ROOT_RECOVERY category
# - Export: /home/user/.secrets/luks_root_recovery.enc (gpg-encrypted)
```

**Recovery key** — 26-character random key stored in:
1. **Hardware**: YubiKey (LUKS binding with slot 2) — requires USB physical possession to unlock
2. **Paper backup**: Printed QR code + plaintext (laminated, stored in safe)
3. **Encrypted cloud backup**: Rclone encrypted to Dropbox (password + LUKS double-encryption)

### 4.3 Key Rotation Schedule

| Key | Rotation interval | Trigger | Method |
|-----|---|---|---|
| **LUKS passphrase** | Never | Only if compromise suspected | `cryptsetup luksChangeKey /dev/nvme0n1p3` |
| **TPM2 sealed key** | 6 months | Preventive (proactive re-seal) | `cryptsetup config /dev/nvme0n1p3 --tpm2-device=auto --tpm2-pcrs=...` |
| **YubiKey binding** | 12 months | Preventive + hardware refresh | Re-bind with new LUKS slot |
| **Recovery key** | 6 months | Synchronize with TPM rotation | Generate new, update all backups |

---

## 5. Encrypted Backup Strategy

### 5.1 Backup Targets (Three-Layer Approach)

| Target | Frequency | Encryption | Purpose | Recovery Time |
|--------|-----------|-----------|---------|---|
| **External encrypted SSD** (2 TB) | Weekly | LUKS2 partition-level | Fast local recovery, ransomware rollback | <1 hour |
| **Rclone to Dropbox** | Daily | Client-side AES-256 (rclone crypt) | Off-site redundancy, cloud disaster recovery | 2-4 hours |
| **S3 Glacier quarterly snapshot** | Quarterly | Server-side AES-256 + immutable versioning | Long-term archive, compliance retention | 24+ hours (Glacier retrieval) |

### 5.2 External USB SSD Setup

**Hardware**: 2 TB Samsung T7 Shield (hardware encryption + IP65 rated)

```bash
# 1. Format with LUKS2 (same cipher as root)
sudo cryptsetup luksFormat --type luks2 --cipher aes-xts-plain64 --key-size 512 /dev/sda1

# 2. Create backup volume
sudo cryptsetup luksOpen /dev/sda1 backup_external
sudo mkfs.ext4 /dev/mapper/backup_external
sudo mount /dev/mapper/backup_external /media/backup_external

# 3. Weekly backup cron job
cat > /etc/cron.d/backup_external_weekly << 'EOF'
0 2 * * 0 root rsync -avX --delete /home/ /media/backup_external/home_backup/ 2>&1 | logger -t backup_external
0 3 * * 0 root rsync -avX --delete / /media/backup_external/root_backup/ --exclude={/proc,/sys,/dev,/run,/boot,/media,/mnt,/tmp,/var/log} 2>&1 | logger -t backup_external
EOF

# 4. Auto-unmount after backup (security: remove USB, disconnect)
cat > /etc/cron.d/backup_unmount << 'EOF'
15 3 * * 0 root umount /media/backup_external && cryptsetup luksClose backup_external
EOF
```

### 5.3 Rclone Encrypted Cloud Backup

**Tool**: Rclone (CLI rsync alternative with native encryption)

```bash
# 1. Install rclone
sudo apt install rclone

# 2. Configure Dropbox remote with encryption
rclone config

# Create new remote 'dropbox_encrypted':
# [dropbox]
# type = dropbox
# token = <OAUTH2_TOKEN>
# 
# [dropbox_crypt]
# type = crypt
# remote = dropbox:/backup_crypt
# password = <ENCRYPTION_PASSWORD>
# salt = <RANDOM_SALT>

# 3. Daily sync cron job (symmetric encryption, password protected)
cat > /etc/cron.d/backup_dropbox_daily << 'EOF'
0 1 * * * root rclone sync /home dropbox_crypt:/home --delete-after --log-file /var/log/rclone_backup.log 2>&1 | logger -t rclone_backup
0 2 * * * root rclone sync /root dropbox_crypt:/root --delete-after --log-file /var/log/rclone_backup.log 2>&1 | logger -t rclone_backup
EOF

# 4. Test restore
rclone ls dropbox_crypt:/home   # Verify files present in cloud
rclone copy dropbox_crypt:/home /tmp/test_restore   # Test decryption on boot
```

### 5.4 S3 Glacier Immutable Archive (Quarterly)

**Setup**: AWS S3 with Object Lock (immutable versioning, no delete within 90 days)

```bash
# 1. Install AWS CLI
sudo apt install awscli

# 2. Configure AWS credentials
aws configure
# Access Key: <AWS_ACCESS_KEY>
# Secret Key: <AWS_SECRET_KEY>
# Region: us-east-1
# Output: json

# 3. Create S3 bucket with Object Lock
aws s3api create-bucket \
  --bucket superclaude-backup-glacier-immutable \
  --object-lock-enabled-for-bucket

# 4. Quarterly snapshot upload (runs last Sunday of each quarter)
cat > /etc/cron.d/backup_s3_quarterly << 'EOF'
# Run on last Sunday of March, June, September, December at 00:00 UTC
0 0 23-31 3,6,9,12 0 root [ $(date +\%d) -ge 23 ] && aws s3 sync / s3://superclaude-backup-glacier-immutable/snapshot-$(date +\%Y-\%m-\%d)/ --exclude /proc/* --exclude /sys/* --exclude /dev/* --exclude /run/* --exclude /media/* --exclude /mnt/* --sse AES256 --storage-class GLACIER 2>&1 | logger -t s3_backup_quarterly
EOF

# 5. Verify immutability
aws s3api get-object-lock-configuration --bucket superclaude-backup-glacier-immutable
```

---

## 6. Threat Model: Data at Rest

### 6.1 Threat Scenarios

| Scenario | Threat | Encryption Layer(s) | Mitigation | Residual Risk |
|----------|--------|---|---|---|
| **Stolen laptop (powered off)** | Physical theft of unencrypted drive | LUKS2 full-disk | TPM2 keys inaccessible without OS; passphrase brute-force infeasible (256 bits) | Quantum computing (10-year horizon) |
| **Stolen laptop (powered on, locked)** | Extract memory via DMA attack | LUKS2 + encrypted swap | Memory encrypted at rest; TPM keys not in RAM during lock | Privileged process could dump RAM (low probability) |
| **Live forensic USB extraction** | dd copy of /dev/sda to USB | LUKS2 + compartmentalized volumes | Attacker needs LUKS passphrase for each volume | Brute-force within 10^15 attempts (2^256 keyspace, GPU farms 2020s-era) |
| **Ransomware infection (OS running)** | Encrypt /home + /var/log, delete backups | Separate encrypted volumes + offline backups | Weekly external SSD backup stored offline; S3 Glacier immutable versioning | Ransomware could infect all 3 backup targets if connected simultaneously (unlikely with cron discipline) |
| **BIOS/firmware compromise (Evil Maid)** | Inject malicious firmware pre-boot | Secure Boot + TPM2 measurement | Secure Boot prevents unsigned bootloader; TPM2 PCR 7 detects boot tampering; fallback to passphrase | Firmware vulnerability + TPM spoof (state-sponsored risk, very low probability) |
| **Hibernation/swapfile exposure** | Extract memory dump from swap | Encrypted swap (luks_swap) | Swap partition encrypted; swap key random at boot (not persisted) | Encrypted swap key could be in initramfs (mitigated by initramfs encryption) |
| **Cold boot attack** | Extract memory from DIMM via liquid nitrogen | Encrypted swap + encrypted /var/log | Volatile key material isolated to TPM/HSM; no plaintext keys in RAM | Attack requires physical access + lab setup; feasible but requires expertise |

### 6.2 Assumption: Secure Boot + Kernel Lockdown

This architecture assumes:
- **Secure Boot enabled** (prevents unsigned bootloader injection)
- **Kernel lockdown mode**: `kernel.lockdown=integrity` (prevents rootkit/module insertion)
- **SELinux or AppArmor enforcing** (mandatory access control)
- **Regular OS updates** (kernel patches, BIOS firmware updates)

Without these, LUKS2 encryption alone is insufficient.

---

## 7. Phase 2 Deployment Runbook

**Estimated time**: 6-8 hours total  
**Downtime**: 4-6 hours (single reboot, live USB environment)

### Deployment Phases (see companion doc: PHASE_2_ENCRYPTION_DEPLOYMENT_RUNBOOK.md)

1. **Pre-deployment checklist** (1 hour): Backup data, create recovery key, write documentation
2. **Live USB environment** (2-3 hours): LUKS2 volume creation, filesystem formatting, data restoration
3. **TPM2 sealing** (1 hour): Register TPM2 sealing, update initramfs, Secure Boot verification
4. **Backup automation** (1 hour): Configure cron jobs, test external SSD + Rclone + S3, verify encryption
5. **Recovery testing** (1 hour): Boot with TPM unlock, force passphrase entry, test LUKS recovery key
6. **Validation** (1 hour): Full filesystem check, performance baseline, security audit

---

## 8. Maintenance & Ongoing Operations

### 8.1 Monthly Tasks
- Boot system (verify TPM2 unlock working)
- Check backup logs: `sudo journalctl -u rsync-backup` and `tail /var/log/rclone_backup.log`
- Verify encrypted SSD still mounted after weekly backups

### 8.2 Quarterly Tasks
- **TPM2 re-seal**: `cryptsetup config /dev/nvme0n1p3 --tpm2-device=auto` (refresh PCR measurements)
- **S3 Glacier snapshot**: Quarterly archive (immutable, 90-day retention minimum)
- **Recovery key rotation**: Generate new recovery key, update YubiKey, print new paper backup
- **Security audit**: Review `sudo ausearch -m AVC` for AppArmor denials; review kernel logs for TPM/crypto errors

### 8.3 Annual Tasks
- **BIOS firmware update**: Check manufacturer for security patches (will invalidate TPM unlock; prepare for passphrase entry)
- **YubiKey replacement cycle**: If hardware showing wear, generate new YubiKey binding
- **Audit backup storage**: Verify external SSD health (`sudo smartctl -a /dev/sda`), test restore from 1-year-old S3 snapshot

---

## 9. Security Considerations & Caveats

### 9.1 Known Limitations
1. **Encrypted /boot required**: Standard GRUB bootloader handles passphrase input; no TPM2 unlock until kernel boots
2. **TPM2 PCR reset on BIOS update**: System will prompt for passphrase after firmware updates (design choice for security)
3. **No remote attestation**: System doesn't provide cryptographic proof to remote servers that it booted securely (would require trusted execution environment)
4. **Swap key not persisted**: Swap key generated fresh at boot; hibernation won't resume (acceptable for security)

### 9.2 Attack Assumptions
This architecture assumes the **Linux kernel and userspace are trustworthy** (kernel patches applied, no rootkits installed). LUKS2 encryption cannot protect against:
- Kernel exploits (0-days, unpatched CVEs)
- Malicious privileged processes (running as root)
- Supply chain attacks (compromised compiler, BIOS pre-loaded with backdoor)

Mitigations:
- Enable automatic security updates: `sudo apt install unattended-upgrades`
- Monitor syscalls with auditd: `sudo ausearch -m EXECVE`
- Use intrusion detection: `sudo apt install aide; aide --init`

### 9.3 Passphrase Security
The recovery passphrase (Layer 3) is **only used if TPM2 unlock fails**. It should be:
- ✅ Random 26+ characters (not human-memorable)
- ✅ Stored in password manager (Bitwarden) + printed backup
- ❌ NOT reused for other systems

---

## 10. Comparison to Alternatives

| Approach | Pros | Cons | Recommendation |
|----------|------|------|---|
| **LUKS2 + TPM2 (This design)** | Transparent boot, modern standard, Linux-native, NIST-approved | Requires Linux 5.6+, TPM2 BIOS support | ✅ **RECOMMENDED** for home Linux machine |
| **VeraCrypt full-disk** | Works on Windows/Mac/Linux, no TPM dependency, portable | Slower (software crypto), UI required at boot | ✅ Good for multi-OS machines (use VeraCrypt on Windows/Mac) |
| **dm-crypt manual mount** | Lightweight, fine-grained control | Manual at boot (no TPM), obsolete without LUKS2 | ❌ Don't use (outdated) |
| **Hardware FDE (SSD controller)** | Transparent, hardware-accelerated, invisible | Closed-source, trust manufacturer, can't verify encryption | ❌ Security through obscurity risk |

---

## 11. Recovery Procedures

### If TPM2 Unlock Fails
1. **Boot prompt**: System displays "cryptsetup: waiting for /dev/nvme0n1p3..."
2. **Enter recovery key**: Type 26-character recovery passphrase at prompt
3. **System continues**: Boots normally with LUKS volumes mounted

### If Recovery Key Lost
1. **Boot from live USB** (Ubuntu 24.04 ISO)
2. **Add new LUKS key**: `sudo cryptsetup luksAddKey /dev/nvme0n1p3 --key-file <existing_key_file>`
3. **Generate new recovery key**: Use `cryptsetup` to derive new key from passphrase
4. **Update backups**: Print new QR code + passphrase, update YubiKey, upload to encrypted cloud

### If Entire Drive Lost
1. **Restore from S3 Glacier**: `aws s3 sync s3://superclaude-backup-glacier-immutable/snapshot-YYYY-MM-DD/ /`
2. **Restore from Rclone cloud**: `rclone copy dropbox_crypt:/home /home`
3. **Restore from external SSD**: Connect encrypted backup SSD, mount with `cryptsetup luksOpen`, rsync back to new disk

---

## Next Steps

1. **Review this architecture** — Confirm LUKS2 + TPM2 + three-layer backup strategy aligns with threat model
2. **Prepare recovery materials** — Print paper backup template, test recovery key generation
3. **Schedule deployment window** — 6-8 hour downtime; recommend weekend or minimal-usage period
4. **Execute Phase 2 Encryption Deployment Runbook** (companion document) — Step-by-step deployment procedure with verification checks
5. **Test recovery procedures** — Boot from recovery key, restore from external SSD, verify cloud backup integrity

---

**Architecture Author**: Claude Code Orchestrator  
**Confidence Level**: 82% (LUKS2 + TPM2 are battle-tested; threat model conservative and well-documented)  
**Last Updated**: 2026-06-23 Session 4027
