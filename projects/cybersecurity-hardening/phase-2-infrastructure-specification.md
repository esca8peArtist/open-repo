# Phase 2 Infrastructure Specification

**Version**: 1.0  
**Date**: June 24, 2026  
**Status**: Production-Ready  
**Estimated implementation**: 30-40 hours over 3-4 weeks

---

## Executive Summary

Phase 2 hardens the user's broader personal computing environment across Linux systems, backup infrastructure, network segmentation, and VPN/Tor access. This specification assumes Phase 1 (Windows VeraCrypt encryption + iPhone hardening) is complete, and provides a layered defense-in-depth architecture:

- **System-level**: LUKS2 full-disk encryption with TPM + passphrase + keyfile + offline recovery key
- **Data protection**: restic + rclone encrypted backups to Proton Drive with offline LUKS/VeraCrypt USB copies
- **Network security**: UFW firewall with VPN kill-switch, DNS-over-TLS, DMZ architecture for any user-hosted services
- **Access security**: Mullvad or IVPN with WireGuard, Tor Browser hardened to "Safer" or "Safest" security level
- **Threat resilience**: Versioned backups for ransomware recovery, recovery key in offline cold storage, encrypted header backups

This specification is designed for a privacy-conscious individual with moderate Linux competency who has budget for VPN (~$5-10/month) and encrypted cloud backup (~$8-15/month). All procedures are automatable; no specialized hardware (e.g., hardware tokens, air-gapped machines) required.

---

## Part 1: Linux Full-Disk Encryption (LUKS2)

### 1.1 Technology Decision: LUKS2 vs dm-crypt vs VeraCrypt

**Chosen technology**: LUKS2 for all Linux system drives; VeraCrypt for portable external USB drives intended for multi-OS environments.

**Justification**:

| Dimension | LUKS2 (Linux) | dm-crypt (Linux) | VeraCrypt (Multi-OS) |
|---|---|---|---|
| KDF | Argon2id (GPU-resistant) | N/A (not a format, a layer) | PBKDF2 (less memory-hard) |
| Keyslots | 32 | N/A | 8 |
| Deduplication support | Yes (restic-friendly) | Yes | Limited (block-device level) |
| Cross-platform | Linux primary | Linux primary | Windows/macOS/Linux |
| Recovery after header loss | Cryptsetup header backup | Same | VeraCrypt file container backup |
| Use case | System disks, internal storage | dm-crypt is the kernel module LUKS sits on; not chosen at user level | External, portable, cold-storage backups |

**LUKS2 architecture decision**:
- **Cipher**: AES-256-XTS (industry standard; AES-128-XTS acceptable as fallback on older hardware, but AES-256-XTS recommended for data expected to persist 10+ years)
- **Key size**: 512 bits (paired with AES-256-XTS for maximum security against future cryptanalysis)
- **KDF**: Argon2id with `--iter-time 5000` (milliseconds CPU time spent deriving key; Argon2id resists both GPU and ASIC attacks)
- **Hash**: SHA-512 (LUKS2 only; supports larger keyslots and metadata)

**VeraCrypt for external drives**:
- Portable encrypted containers for off-device backup USB drives
- Support for hidden volumes (plausible deniability; optional, high-threat scenarios only)
- Cascade ciphers (AES-Twofish-Serpent) available but AES-256-XTS alone is sufficient for most threat models
- Can be mounted on Windows machines if backup restore needed on non-Linux system

### 1.2 Fresh Installation (Ubuntu 24.04 LTS)

**Hardware prerequisites**:
- TPM 2.0 (available on most modern laptops/desktops; verify in BIOS)
- UEFI firmware with Secure Boot support (optional but recommended)
- Minimum 32 MB unallocated space for LUKS header (if encrypting existing data; not needed for fresh install)

**Fresh install with full-disk encryption (encrypted /)**:

1. **Boot Ubuntu 24.04 LTS installation media**. At the installation menu, select "Advanced Features" → "Install with full-disk encryption (LVM + LUKS)".

2. **Encryption setup screen**:
   - Select "Encrypt the new installation"
   - Disk: choose target NVMe/SSD (typically `/dev/nvme0n1`)
   - LUKS version: Select "LUKS 2"
   - Passphrase: Enter a strong passphrase (30+ characters, mixed case + numbers + symbols); this passphrase must be memorized or stored in a password manager

3. **Complete installation** as normal. The installer will automatically:
   - Create LUKS2 container with default Ubuntu parameters (acceptable)
   - Set up LVM inside the container
   - Install GRUB with LUKS unlock prompt at boot
   - Optionally integrate TPM2 for automatic unlock

4. **Post-install verification**:
   ```bash
   # Confirm LUKS2 format
   sudo cryptsetup luksDump /dev/nvme0n1p3
   # Output should show: LUKS version 2
   
   # Check keyslots
   sudo cryptsetup luksDump /dev/nvme0n1p3 | grep "Keyslot"
   # Output: Keyslot 0 is ENABLED (your passphrase)
   ```

5. **Harden LUKS2 parameters** (Ubuntu defaults are adequate, but manual re-encryption with stricter KDF is optional for high-security scenarios):
   ```bash
   # ONLY if you want to re-encrypt with custom parameters (takes 4-6 hours on 500 GB drive)
   sudo cryptsetup reencrypt /dev/nvme0n1p3 \
     --type luks2 \
     --cipher aes-xts-plain64 \
     --key-size 512 \
     --hash sha512 \
     --pbkdf argon2id \
     --iter-time 5000
   # WARNING: This locks the system; run from live ISO only, with backups beforehand
   ```

### 1.3 In-Place Encryption (Existing Ubuntu Installation)

**Scenario**: Ubuntu already installed on unencrypted system; you want to encrypt without full reinstall.

**Requirements**:
- Live USB with Ubuntu 24.04 LTS (same version as installed system)
- 32 MB minimum free space on target partition
- System in consistent state (no disk corruption; run `fsck` from live ISO first)
- Full backup of data beforehand (to external USB; this procedure is safe but risk-mitigation)

**Procedure**:

1. **Backup data**:
   ```bash
   # Boot live USB
   # Mount external backup USB
   sudo mkdir -p /mnt/backup && sudo mount /dev/sda1 /mnt/backup
   
   # Copy critical data
   sudo rsync -avh /home /mnt/backup/home_backup_$(date +%Y%m%d)/
   ```

2. **Boot live USB and start re-encryption**:
   ```bash
   # Identify your system partition (typically /dev/nvme0n1p3 for root)
   lsblk
   
   # Start LUKS2 encryption (this runs in-place, no data loss, takes 4-8 hours on 500GB)
   sudo cryptsetup reencrypt /dev/nvme0n1p3 \
     --type luks2 \
     --encrypt \
     --cipher aes-xts-plain64 \
     --key-size 512 \
     --hash sha512 \
     --pbkdf pbkdf2 \
     --reduce-device-size 32M \
     /dev/nvme0n1p3
   
   # You will be prompted for a new passphrase for the encrypted volume
   # After reencryption completes, the original filesystem is encrypted and shrunk by 32 MB (for LUKS header)
   ```

3. **Reinstall GRUB to decrypt at boot**:
   ```bash
   # From live USB, mount the encrypted drive
   sudo cryptsetup luksOpen /dev/nvme0n1p3 my_crypt
   sudo mount /dev/mapper/my_crypt /mnt
   
   # Mount EFI partition
   sudo mount /dev/nvme0n1p2 /mnt/boot/efi
   
   # Reinstall GRUB with LUKS support
   sudo grub-install --root-directory=/mnt --efi-directory=/mnt/boot/efi /dev/nvme0n1
   
   # Update initramfs to include cryptsetup
   sudo chroot /mnt update-initramfs -u
   
   # Unmount and reboot
   sudo umount -R /mnt
   sudo cryptsetup luksClose my_crypt
   ```

4. **Test reboot**: Machine should prompt for LUKS passphrase before boot.

### 1.4 Multi-Keyslot Strategy (LUKS2)

**Recommended keyslot configuration** (applies to both fresh install and post-encryption):

| Keyslot | Type | Usage | Storage | Recovery path |
|---|---|---|---|---|
| 0 | Passphrase | Daily boot / decryption | Memorized or password manager | Primary |
| 1 | Random recovery key | Offline cold storage | Printed paper + encrypted USB | If keyslot 0 forgotten |
| 2 (optional) | Keyfile | Automated unlock of secondary volumes | On-disk, read by root-only systemd unit | If primary/recovery both compromised |

**Implementation**:

1. **Verify keyslot 0 (already set during install)**:
   ```bash
   sudo cryptsetup luksDump /dev/nvme0n1p3 | grep -A 20 "Keyslot 0"
   ```

2. **Generate and add recovery key (Keyslot 1)**:
   ```bash
   # Generate a 256-character random recovery key
   openssl rand -base64 192 > /tmp/recovery_key.txt
   cat /tmp/recovery_key.txt
   
   # Add to LUKS2 keyslot 1
   sudo cryptsetup luksAddKey /dev/nvme0n1p3 --key-slot 1 --keyfile /tmp/recovery_key.txt
   # Prompt: "Enter any existing passphrase" (enter your boot passphrase from step 1.2)
   
   # Verify keyslot 1 is now active
   sudo cryptsetup luksDump /dev/nvme0n1p3 | grep -A 5 "Keyslot 1"
   
   # Securely delete the temporary file
   shred -vfz /tmp/recovery_key.txt
   ```

3. **Store recovery key offline** (two independent copies):
   - **Copy 1 (paper)**: Print recovery key on paper, sign/date it, store in safe or safety deposit box. Include instructions: "To recover: Boot live USB, run: `sudo cryptsetup luksOpen --key-file <usb_drive>/recovery_key.txt /dev/nvme0n1p3 my_crypt`"
   - **Copy 2 (encrypted USB)**: Save recovery key on a VeraCrypt-encrypted USB drive stored in a different physical location (home vs office, for example)

4. **Optionally add keyfile (Keyslot 2)** for automated unlock of secondary data volumes:
   ```bash
   # Generate keyfile (readable by root only)
   sudo openssl rand -out /etc/keys/secondary.keyfile 256
   sudo chmod 400 /etc/keys/secondary.keyfile
   
   # Add keyfile to a secondary data volume (if you have one; see Section 2 for encrypted /home setup)
   sudo cryptsetup luksAddKey /dev/mapper/secondary_data /etc/keys/secondary.keyfile
   
   # Never add a keyfile to the root keyslot (0); keep the passphrase as sole recovery path
   ```

### 1.5 LUKS Header Backup (MANDATORY)

**Critical**: LUKS header contains all keyslot material and encryption metadata. Header corruption = permanent data loss.

**Backup procedure**:

```bash
# Backup LUKS header to external, offline USB
sudo cryptsetup luksHeaderBackup /dev/nvme0n1p3 \
  --header-backup-file /media/usb_backup/luks_root_header_$(date +%Y%m%d_%H%M%S).bin

# Verify backup integrity by attempting a test restore to a temporary file
sudo cryptsetup luksHeaderRestore /dev/nvme0n1p3 \
  --header-backup-file /media/usb_backup/luks_root_header_20260624_120000.bin \
  --force-password  # This will fail with --force-password on a live device; omit this to test header validity without restoring

# Better: test on a copy of the drive partition (if test device available)
sudo dd if=/dev/nvme0n1p3 of=/tmp/test_partition.img bs=1M count=100
sudo losetup /dev/loop0 /tmp/test_partition.img
sudo cryptsetup luksHeaderRestore /dev/loop0 \
  --header-backup-file /media/usb_backup/luks_root_header_20260624_120000.bin
# If this succeeds, header backup is valid
```

**Backup schedule**:
- After initial encryption: Immediately
- After any keyslot change (passphrase rotation, adding/removing recovery keys): Within 1 day
- Quarterly: Verify existing backup integrity
- Storage: Encrypted USB drive in safe + paper copy of critical parameters (volume UUID, cipher used) in safe

**Two-backup rule**: Store header backups in at least two separate physical locations. If your home burns down, the office backup is unaffected.

### 1.6 TPM2 Integration (Optional, Ubuntu 24.04+)

**Note**: Ubuntu's installer may have already integrated TPM2 for automatic unlock. This section details manual TPM2 setup or verification.

**TPM2 concept**: Encrypts the Volume Key using TPM Platform Configuration Registers (PCRs). Volume Key is released only if PCR values match those at sealing time. PCRs reset if BIOS/firmware changes.

**Check TPM2 status**:
```bash
sudo tpm2_getcap properties-fixed
# Should show: TPM2_PT_FIRMWARE_VERSION

# Check if LUKS volume is already TPM2-sealed
sudo cryptsetup luksDump /dev/nvme0n1p3 | grep -i "tpm"
```

**Manual TPM2 sealing** (if not already set up by installer):
```bash
# Install tpm2-tools if not present
sudo apt install tpm2-tools tpm2-abrmd

# Seal Volume Key with TPM2 PCRs 0,1,2,7 (firmware, config, bootloader, secure-boot state)
sudo cryptsetup token add --key-slot 0 --token-type systemd-tpm2 \
  --tpm2-pcrs 0,1,2,7 \
  --tpm2-pubkey /usr/share/systemd/tpm2-pcr-public-key.pem \
  /dev/nvme0n1p3

# Verify token was added
sudo cryptsetup luksDump /dev/nvme0n1p3 | grep -A 10 "Token 0"
```

**Re-sealing after firmware update**:
If you update BIOS/UEFI firmware, TPM2 PCRs change. Boot will require manual passphrase entry until re-sealed:
```bash
# After firmware update and successful boot with passphrase
sudo cryptsetup token remove --token-slot 0 /dev/nvme0n1p3
sudo cryptsetup token add --key-slot 0 --token-type systemd-tpm2 \
  --tpm2-pcrs 0,1,2,7 \
  --tpm2-pubkey /usr/share/systemd/tpm2-pcr-public-key.pem \
  /dev/nvme0n1p3
```

**Trade-off**: TPM2 automatic unlock is convenient but adds complexity. If you forget your passphrase AND the TPM2 seal breaks, recovery requires the offline recovery key. For highest simplicity, use passphrase only (no TPM2). For highest convenience + security, use both passphrase + TPM2 seal + offline recovery key.

### 1.7 Encrypted /home Partition (Optional, Recommended for Multi-User Systems)

**Use case**: If multiple users on the system, encrypt each user's /home separately. This allows one user to decrypt without affecting others.

**Create encrypted /home on separate partition**:

1. **Create partition** (using GParted or `parted`):
   ```bash
   # If you have spare SSD space (e.g., 100 GB unallocated)
   # Create partition /dev/nvme0n1p4 (100 GB)
   sudo parted /dev/nvme0n1 mkpart primary ext4 500GB 600GB
   
   # Encrypt the new partition
   sudo cryptsetup luksFormat --type luks2 --cipher aes-xts-plain64 \
     --key-size 512 --hash sha512 --pbkdf argon2id --iter-time 5000 \
     /dev/nvme0n1p4
   
   # Open encrypted volume
   sudo cryptsetup luksOpen /dev/nvme0n1p4 home_crypt
   
   # Create filesystem
   sudo mkfs.ext4 /dev/mapper/home_crypt
   
   # Mount
   sudo mkdir -p /mnt/home_new
   sudo mount /dev/mapper/home_crypt /mnt/home_new
   
   # Copy existing /home data
   sudo rsync -av /home/ /mnt/home_new/
   ```

2. **Configure fstab for automatic unlock**:
   ```bash
   # Get UUID of encrypted partition
   sudo cryptsetup luksDump /dev/nvme0n1p4 | grep "UUID"
   # Example: UUID: 550e8400-e29b-41d4-a716-446655440000
   
   # Add crypttab entry
   echo "home_crypt UUID=550e8400-e29b-41d4-a716-446655440000 /etc/keys/home.keyfile luks" \
     | sudo tee -a /etc/crypttab
   
   # Create keyfile (for unattended unlock during boot)
   sudo openssl rand -out /etc/keys/home.keyfile 256
   sudo chmod 400 /etc/keys/home.keyfile
   sudo cryptsetup luksAddKey /dev/nvme0n1p4 /etc/keys/home.keyfile
   
   # Add fstab entry
   home_uuid=$(blkid -s UUID -o value /dev/mapper/home_crypt)
   echo "UUID=$home_uuid /home ext4 defaults,noatime 0 2" | sudo tee -a /etc/fstab
   
   # Test (safe to reboot after this)
   sudo mount -a
   ```

3. **Backup /home keyfile and header**:
   ```bash
   sudo cryptsetup luksHeaderBackup /dev/nvme0n1p4 \
     --header-backup-file /media/usb_backup/luks_home_header_$(date +%Y%m%d).bin
   sudo cp /etc/keys/home.keyfile /media/usb_backup/home.keyfile.backup
   ```

---

## Part 2: Encrypted Backup Strategy

### 2.1 Backup Architecture Decision

**Three-tier backup strategy** (primary, fallback, offline):

1. **Primary**: restic + rclone → Proton Drive (cloud)
2. **Fallback**: restic + rclone → Backblaze B2 (cloud, if Proton Drive unavailable)
3. **Offline**: LUKS-encrypted USB (local, updated monthly)

**Tool choice justification**:

- **restic**: Automatic encryption (AES-256-GCM), deduplication via Content-Defined Chunking (CDC), snapshot history, integrity verification (`restic check`), cross-platform
- **rclone**: 40+ cloud providers, handles authentication, transparently encrypts to Proton Drive, can fall back to other backends
- **Proton Drive**: End-to-end encrypted cloud storage (Proton handles encryption for you), plans start at $5.99/month for 200 GB
- **Backblaze B2**: S3-compatible, $0.006/GB/month storage + restore costs, well-supported by restic

**Not chosen**:
- Duplicacy: Overkill for personal use (global dedup designed for multi-client fleets)
- `tar + gpg`: Manual and error-prone; no snapshot history or deduplication
- Nextcloud: Adds infrastructure complexity; requires your own server or subscription

### 2.2 Installation and Initial Setup

**Install restic and rclone**:
```bash
sudo apt update && sudo apt install restic rclone

# Verify versions
restic version
rclone version
```

**Configure rclone for Proton Drive** (interactive):
```bash
rclone config

# When prompted:
# New remote name? → proton_drive
# Type of storage? → protondrive (search for 'proton')
# Proton Mail email? → your.email@protonmail.com
# Proton Mail password? → [You must have logged in via browser first to generate encryption keys]
# Do you want to use a server-side copy? → y
# Confirm password? → y
# Save config? → y
```

**Important pre-requisite for Proton Drive**: You must have logged into Proton Drive via the web interface at least once before rclone can connect. This generates encryption keys that rclone needs.

**Verify rclone connection**:
```bash
rclone ls proton_drive:
# Should list your Proton Drive contents without error
```

**Initialize restic repository on Proton Drive**:
```bash
# This creates a new restic repository in Proton Drive
restic -r rclone:proton_drive:restic-backups init

# You will be prompted for a repository password
# This is DIFFERENT from your Proton credentials
# Store this password securely in your password manager AND in cold storage

restic -r rclone:proton_drive:restic-backups key list
# Should show the password key you just created
```

### 2.3 Backup Automation (Systemd Timer)

**Create systemd service for daily backups**:

File: `/etc/systemd/system/restic-backup.service`
```ini
[Unit]
Description=Restic Backup Service
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
User=root
Environment="RESTIC_REPOSITORY=rclone:proton_drive:restic-backups"
Environment="RESTIC_PASSWORD_FILE=/root/.restic_password"

# Backup directories
ExecStart=/usr/bin/restic backup \
  --verbose \
  /home \
  /etc \
  /root \
  --exclude-file=/etc/restic_excludes.txt

# Forget old snapshots (run after backup completes)
ExecStartPost=/usr/bin/restic forget \
  --keep-daily 7 \
  --keep-weekly 4 \
  --keep-monthly 12 \
  --keep-yearly 2 \
  --prune

StandardOutput=journal
StandardError=journal
```

**Create systemd timer** (runs backup daily at 03:00 AM):

File: `/etc/systemd/system/restic-backup.timer`
```ini
[Unit]
Description=Daily Restic Backup Timer
Requires=restic-backup.service

[Timer]
OnCalendar=daily
OnCalendar=*-*-* 03:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

**Store repository password securely**:
```bash
# Create password file (readable by root only)
sudo bash -c 'echo "YOUR_RESTIC_REPOSITORY_PASSWORD" > /root/.restic_password'
sudo chmod 600 /root/.restic_password

# Never commit this file to git or share it
```

**Create exclude file** (skip cache, temp files):

File: `/etc/restic_excludes.txt`
```
# Cache directories
.cache/
.mozilla/cache/
.thunderbird/cache/
.local/share/*/cache/

# Temporary files
/tmp/
/var/tmp/
*.tmp
*.swp

# System snapshots
/dev/
/proc/
/sys/
/run/
/mnt/
/media/

# Large files not needed in backup
node_modules/
.git/objects/
.terraform/
venv/

# Application-specific
.docker/
Trash/
.Trash/
```

**Enable and start the timer**:
```bash
sudo systemctl daemon-reload
sudo systemctl enable restic-backup.timer
sudo systemctl start restic-backup.timer

# Verify timer is active
sudo systemctl status restic-backup.timer
sudo systemctl list-timers restic-backup.timer
```

**Manual backup (first run)**:
```bash
# Manually trigger backup to verify setup
sudo systemctl start restic-backup.service

# Monitor progress
sudo journalctl -u restic-backup.service -f

# After completion, verify repository
RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
RESTIC_PASSWORD_FILE=/root/.restic_password \
restic snapshots

# Test restore (to /tmp, non-destructive)
restic -r rclone:proton_drive:restic-backups restore latest --target /tmp/restore_test
```

### 2.4 Backup Verification and Monitoring

**Weekly integrity check** (systemd timer runs first Sunday of month):

File: `/etc/systemd/system/restic-check.service`
```ini
[Unit]
Description=Restic Repository Integrity Check
After=network-online.target

[Service]
Type=oneshot
User=root
Environment="RESTIC_REPOSITORY=rclone:proton_drive:restic-backups"
Environment="RESTIC_PASSWORD_FILE=/root/.restic_password"

ExecStart=/usr/bin/restic check --verbose

StandardOutput=journal
StandardError=journal
```

File: `/etc/systemd/system/restic-check.timer`
```ini
[Unit]
Description=Monthly Restic Check Timer

[Timer]
OnCalendar=Sun *-*-1..7 04:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

**Alert on backup failure** (optional, via mail-on-unit-failure):
```bash
# Install mail support
sudo apt install mailutils

# Add to /etc/systemd/system/restic-backup.service:
[Unit]
OnFailure=status-mail-user@%n.service

# This sends an email to root@localhost if backup fails
```

### 2.5 Proton Drive Fallback Configuration (B2)

**Reason**: Proton Drive rclone backend is in beta; documented API blockages have occurred. Configure Backblaze B2 as fallback.

**Create Backblaze B2 account**:
1. Sign up at https://www.backblaze.com/b2/
2. Create B2 account credentials (Application Key ID + Application Key)

**Configure rclone for B2**:
```bash
rclone config

# New remote name? → b2_backup
# Type of storage? → b2
# Account ID? → [Your B2 Account ID]
# Application Key? → [Your B2 Application Key]
# File name encryption? → standard (or off, your choice)
# Directory name encryption? → standard (or off)
# Save config? → y
```

**Initialize restic on B2** (keep both Proton + B2 in parallel):
```bash
restic -r rclone:b2_backup:restic-backups init
# Prompt: repository password (can be same as Proton, or different)
```

**In restic-backup.service, split backup**:
```bash
# Option 1: Backup to both Proton AND B2 (slower, safest)
/usr/bin/restic -r rclone:proton_drive:restic-backups backup /home /etc /root
/usr/bin/restic -r rclone:b2_backup:restic-backups backup /home /etc /root

# Option 2: Try Proton first; if fails, fall back to B2 (faster typical case)
/usr/bin/restic -r rclone:proton_drive:restic-backups backup /home /etc /root || \
/usr/bin/restic -r rclone:b2_backup:restic-backups backup /home /etc /root
```

**Estimated cost**:
- Proton Drive 200 GB: $5.99/month
- Backblaze B2: ~$0.30/month for 50 GB storage + restore (minimal use)
- Total cloud backup: ~$6-7/month

### 2.6 Offline USB Backup (Monthly)

**Create encrypted USB drive**:
```bash
# Identify USB device (typically /dev/sda or /dev/sdb)
lsblk

# Partition USB (100 GB external drive)
sudo parted /dev/sdb mklabel gpt
sudo parted /dev/sdb mkpart primary ext4 1MB 100GB

# Encrypt partition with LUKS2
sudo cryptsetup luksFormat --type luks2 --cipher aes-xts-plain64 \
  --key-size 512 /dev/sdb1

# Open encrypted volume
sudo cryptsetup luksOpen /dev/sdb1 backup_usb

# Create filesystem
sudo mkfs.ext4 /dev/mapper/backup_usb

# Mount
sudo mkdir -p /mnt/backup_usb
sudo mount /dev/mapper/backup_usb /mnt/backup_usb

# Verify free space
df -h /mnt/backup_usb
```

**Monthly backup to USB** (add to crontab):
```bash
# Run last Sunday of month at 20:00
0 20 * * 0 [ $(date +\%d) -gt 21 ] && /usr/local/bin/backup_to_usb.sh

# Script: /usr/local/bin/backup_to_usb.sh
#!/bin/bash
set -e

BACKUP_USB="/mnt/backup_usb"
REPO_PATH="$BACKUP_USB/restic-offline"

# Mount USB if not already mounted (prompt for passphrase)
if ! mountpoint -q "$BACKUP_USB"; then
  read -s -p "Enter USB encryption passphrase: " usb_pass
  echo "$usb_pass" | sudo cryptsetup luksOpen /dev/sdb1 backup_usb
  sudo mount /dev/mapper/backup_usb "$BACKUP_USB"
fi

# Create restic repository on USB (if first time)
if [ ! -d "$REPO_PATH" ]; then
  RESTIC_REPOSITORY="$REPO_PATH" restic init
fi

# Backup to USB
RESTIC_REPOSITORY="$REPO_PATH" restic backup /home /etc /root

# Unmount
sudo umount "$BACKUP_USB"
sudo cryptsetup luksClose backup_usb

echo "Offline backup complete. USB can be stored in safe."
```

**USB rotation schedule**:
- Keep three encrypted USB drives (USB-A, USB-B, USB-C)
- Rotate monthly: backup to USB-A one month, USB-B the next, USB-C the third
- Store inactive drives in physical safe or separate location
- Label with date: `backup_usb_june_2026`

---

## Part 3: Network Segmentation and DNS Security

### 3.1 DNS-over-TLS (DoT) Configuration

**Concept**: Encrypts DNS queries from snooping by ISP, network admin, or passive network surveillance.

**Ubuntu 24.04+ setup with systemd-resolved**:

File: `/etc/systemd/resolved.conf`
```ini
[Resolve]
DNS=1.1.1.1#cloudflare-dns.com
DNSSECValidation=yes
DNSOverTLS=yes
FallbackDNS=8.8.8.8#dns.google

# Disable MDNS and LLMNR if not needed (reduces DNS leaks)
LLMNR=no
MulticastDNS=no
```

**Restart systemd-resolved**:
```bash
sudo systemctl restart systemd-resolved

# Verify DoT is active
systemd-resolve --status

# Should show: DNSSEC setting: yes, DNS over TLS: yes
```

**DNS provider comparison** (for privacy-conscious use):

| Provider | DoH/DoT | Privacy policy | DNSSEC | Malware blocking |
|---|---|---|---|---|
| Cloudflare (1.1.1.1) | Yes | Deletes logs after 24h; strong privacy commitment | Yes | Yes (optional) |
| Quad9 (9.9.9.9) | Yes | No logs, independently audited; blocks malware | Yes | Yes (automatic) |
| NextDNS | Yes (limited free) | No logs; customizable blocklists | Yes | Yes (custom) |
| Mullvad DNS (149.112.122.112) | DoH only | No logs; free; for privacy advocates | Yes | Yes |

**Recommendation**: Use Cloudflare (1.1.1.1) or Quad9 (9.9.9.9) for general use. If on Mullvad VPN, use Mullvad's DNS (10.64.0.1) which routes through Mullvad infrastructure.

**Verify no DNS leaks** (test after configuration):
```bash
# Install dnsleaktest (optional)
sudo apt install dnsleaktest

# Or use curl to query an external DNS leak test service
curl -s https://1.1.1.1/dns-query?name=whoami.akamai.net
# Should return Cloudflare's resolver IP, not your ISP's
```

### 3.2 UFW Firewall Configuration with VPN Kill-Switch

**UFW (Uncomplicated Firewall) setup**:

```bash
# Enable UFW
sudo ufw enable

# Set default policies (most restrictive, then allow what you need)
sudo ufw default deny outgoing
sudo ufw default deny incoming
sudo ufw default deny routed

# Allow SSH (so you don't lock yourself out)
sudo ufw allow ssh

# Allow DNS locally (for systemd-resolved)
sudo ufw allow in on lo from 127.0.0.1 to 127.0.0.1 port 53

# Allow local network communication (if on home LAN)
sudo ufw allow from 192.168.1.0/24
```

**VPN kill-switch via UFW** (requires running on Mullvad/ProtonVPN/IVPN):

```bash
# Identify VPN tunnel interface
ip link show
# Look for "tun0" (OpenVPN) or "wg0" (WireGuard), or "mullvad0" (Mullvad native)

# Allow all traffic on VPN tunnel interface only
sudo ufw allow out on tun0 from any to any
sudo ufw allow in on tun0 from any to any

# Prevent DNS leaks: block UDP/TCP 53 to anywhere except VPN tunnel
sudo ufw deny out to any port 53
sudo ufw allow out on tun0 to any port 53

# Allow connection to VPN server itself (needed to establish tunnel)
# Get VPN server IP (example: 209.250.35.198 for Mullvad)
sudo ufw allow out to 209.250.35.198

# Add VPN server to /etc/hosts to prevent DNS lookup before VPN is up
echo "209.250.35.198  nl-ams-wg-401.mullvad.net" | sudo tee -a /etc/hosts

# Verify rules
sudo ufw status verbose
```

**IPv6 disable** (if VPN is IPv4-only, IPv6 traffic will leak):

```bash
# Disable IPv6 system-wide in sysctl
echo "net.ipv6.conf.all.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
echo "net.ipv6.conf.default.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Or just for VPN tunnel (less aggressive):
# Add to UFW before rules:
sudo ufw deny out from any to ::/0
```

**Test kill-switch** (while on VPN):

```bash
# Start VPN
mullvad connect
# or: sudo openvpn --config /etc/openvpn/client.conf

# Verify you can access external resources
curl https://api.ipify.org
# Should return a VPN IP, not your home IP

# Simulate VPN disconnect (kill the connection)
sudo kill <pid_of_vpn_process>

# Try to access external resources
timeout 5 curl https://api.ipify.org
# Should HANG and timeout (not reach external host)
# This proves kill-switch is working

# Reconnect VPN
mullvad connect
```

### 3.3 Reverse Proxy (Nginx) for DMZ Architecture

**Use case**: If you run any internet-facing services (e.g., Nextcloud, Matrix homeserver, personal website), run them in a DMZ behind an Nginx reverse proxy.

**Nginx reverse proxy setup** (`/etc/nginx/sites-available/reverse-proxy`):

```nginx
# Redirect HTTP to HTTPS
server {
    listen 80;
    listen [::]:80;
    server_name _;
    
    return 301 https://$host$request_uri;
}

# HTTPS reverse proxy
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name example.com www.example.com;
    
    # TLS configuration
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    ssl_stapling on;
    ssl_stapling_verify on;
    
    # Security headers
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
    add_header X-Content-Type-Options "nosniff";
    add_header X-Frame-Options "DENY";
    add_header X-XSS-Protection "1; mode=block";
    add_header Referrer-Policy "strict-origin-when-cross-origin";
    add_header Content-Security-Policy "default-src 'self'";
    server_tokens off;
    
    # Rate limiting
    limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
    limit_req zone=api_limit burst=20 nodelay;
    
    # Proxy to backend service (e.g., Nextcloud on localhost:8080)
    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
}
```

**Enable Nginx**:
```bash
sudo apt install nginx
sudo ln -s /etc/nginx/sites-available/reverse-proxy /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

**Obtain TLS certificate via Let's Encrypt** (automated renewal):
```bash
sudo apt install certbot python3-certbot-nginx

# Obtain certificate
sudo certbot certonly --nginx -d example.com -d www.example.com

# Auto-renewal via systemd timer
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer
```

---

## Part 4: VPN and Tor Setup

### 4.1 VPN Selection and Installation

**Recommended providers** (by use case):

| Use case | Provider | Rationale |
|---|---|---|
| General privacy | Mullvad | $5/month, anonymous token, verified no-logs (April 2023 police raid found zero data) |
| Balance of features | ProtonVPN | $4-10/month depending on plan; Swiss jurisdiction; NetShield malware filtering |
| Maximum anonymity | IVPN | Gibraltar jurisdiction; multi-hop available; Monero/cash payments |
| Budget (accepts tradeoffs) | ProtonVPN Free | 1 GB daily limit; good for testing |

**Installation for Mullvad** (WireGuard-based):

```bash
# Add Mullvad repository
curl https://repository.mullvad.net/deb/mullvad-keyring.asc | sudo apt-key add -
echo "deb [arch=amd64] https://repository.mullvad.net/deb/stable main" \
  | sudo tee /etc/apt/sources.list.d/mullvad.list

# Install and start
sudo apt update && sudo apt install mullvad-vpn
sudo systemctl enable mullvad-daemon
sudo systemctl start mullvad-daemon

# Verify
mullvad version
```

**Installation for ProtonVPN** (if preferred):

```bash
# Add ProtonVPN repository
wget https://repo3.protonvpn.com/debian/dists/focal/main/binary-amd64/protonvpn-stable-release_1.0.3~focal_all.deb
sudo apt install ./protonvpn-stable-release_1.0.3~focal_all.deb
sudo apt update && sudo apt install protonvpn

# Login and enable
sudo protonvpn configure
sudo protonvpn connect
```

### 4.2 VPN Kill-Switch Testing

**Test procedure** (from Section 3.2 above):

```bash
# Start VPN
mullvad connect us

# Verify you're through VPN
curl https://api.ipify.org
# Returns: 209.250.35.198 (VPN IP, not your home ISP IP)

# Kill VPN connection
sudo kill $(pgrep -f "mullvad-daemon")

# Test external access (should HANG, not reach)
timeout 5 curl https://api.ipify.org
# Hangs and times out (kill-switch active)

# Reconnect
mullvad connect us
```

**Expected behavior**: Kill-switch prevents any data leakage when VPN unexpectedly disconnects.

### 4.3 Tor Browser Hardening

**Installation**:
```bash
# Download from Tor Project official site (NOT from apt; verify signature)
cd ~/Downloads
wget https://www.torproject.org/dist/torbrowser/13.5/tor-browser-linux64-13.5.tar.xz
wget https://www.torproject.org/dist/torbrowser/13.5/tor-browser-linux64-13.5.tar.xz.asc

# Verify signature (requires gpg)
gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org
gpg --verify tor-browser-linux64-13.5.tar.xz.asc

# Extract
tar xf tor-browser-linux64-13.5.tar.xz
cd tor-browser && ./start-tor-browser.desktop
```

**Security level configuration**:

1. Open Tor Browser
2. Click Shield icon (top-left) → Advanced Security Settings
3. Set "Security Level" to **"Safer"** or **"Safest"**
   - Standard: JavaScript enabled; no restrictions (not recommended)
   - Safer: JavaScript disabled on HTTP; some HTML5 disabled; most sites work
   - Safest: JavaScript disabled everywhere; HTML5 media click-to-play; fonts restricted; some sites break

4. Do NOT increase screen size to fill browser window (breaks letterboxing)
5. Do NOT install additional extensions
6. Restart Tor Browser after changing security level (bug: some settings don't apply until restart)

**Security levels explained**:

| Level | JavaScript | Canvas | WebGL | Fonts | Use case |
|---|---|---|---|---|---|
| Standard | Enabled | Enabled | Enabled | All | General browsing (less safe) |
| Safer | HTTP only | Blocked | Blocked | Subset | Recommended default |
| Safest | All disabled | Blocked | Blocked | Limited | High-threat research, financial data |

**Recommended**: Use "Safer" level for most Tor usage. Use "Safest" only when accessing sensitive accounts (banking, health portals).

**Fingerprinting notes**:
- Tor Browser randomizes user-agent, canvas, WebGL, clock precision to prevent fingerprinting
- Letterboxing (window size rounded to 200x100px buckets) prevents screen size fingerprinting
- Do NOT browse non-Tor and Tor-only sites in same browser session; don't correlate activity

---

## Part 5: Data Asset Mapping and Access Control

### 5.1 Asset Classification

Classify data by sensitivity and backup requirements:

| Asset type | Examples | Sensitivity | Encryption | Backup frequency | Notes |
|---|---|---|---|---|---|
| Personal files | Documents, photos, videos | Medium | LUKS (at-rest) | Daily via restic | Encrypted backups to Proton Drive |
| Credentials | Passwords, SSH keys, API keys | Critical | Password manager (encrypted DB) + system LUKS | Daily restic backup | Never plaintext; use Bitwarden/KeePass |
| Communications | Email, messages, documents | High | E2EE where possible (ProtonMail, Signal) | Daily restic | Avoid plaintext email storage |
| Financial records | Statements, tax returns, invoices | Critical | LUKS at-rest, AES-256 cloud encryption | Monthly to cold storage USB | Use separate VeraCrypt container |
| Keys and certs | TLS certs, SSH keys, GPG keys | Critical | Passphrase-protected, backed up to cold storage | Quarterly manual backup | Never on single device |
| Source code | Projects, scripts, configs | Medium | System LUKS + git remote (e.g., GitHub private repo) | Daily restic | Consider removing API keys before backup |
| Logs and metadata | System logs, browser history | Low-Medium | LUKS at-rest | Monthly | Can be pruned after retention period |

### 5.2 Credential Management

**Recommended tool: Bitwarden** (open source, zero-knowledge, end-to-end encrypted):

```bash
# Install Bitwarden CLI
sudo apt install bitwarden

# Create account at https://bitwarden.com
# Login and sync
bw login your.email@example.com
bw sync

# Store master password in a separate, offline location (safe, safety deposit box)
# Never write master password in plaintext files

# Add to backup exclusion if using local database (Bitwarden syncs to zero-knowledge cloud by default)
```

**SSH key management**:
```bash
# Generate SSH key with passphrase
ssh-keygen -t ed25519 -C "your.email@example.com"
# Prompted: Enter passphrase (encrypt private key)

# Store passphrase in password manager (Bitwarden)
# Backup public key to GitHub/GitLab
# Backup private key to restic backups (encrypted by LUKS + restic encryption)

# For additional security, store offline copy of SSH private key on encrypted USB
cp ~/.ssh/id_ed25519 /mnt/backup_usb/ssh_keys/id_ed25519_$(date +%Y%m%d)
```

### 5.3 Financial Data Isolation (Optional, High-Security)

**Separate VeraCrypt container for sensitive financial data**:

```bash
# Create a VeraCrypt encrypted file container (500 MB for tax records + statements)
veracrypt --text --create

# When prompted:
# Container path? → /home/user/Volumes/financial.vc
# Container size? → 500 MB
# Encryption algorithm? → AES-256
# Hash algorithm? → BLAKE2s-256
# Filesystem? → NTFS (portable) or ext4 (Linux only)
# Password? → [Strong passphrase]

# Mount container
veracrypt --text --mount /home/user/Volumes/financial.vc /mnt/financial

# Store financial documents in /mnt/financial
# (e.g., tax returns, statements, invoices)

# Backup entire container to restic + offline USB
# When unmounted, container is encrypted on-disk and in backups
```

**Note**: VeraCrypt container is encrypted twice (VeraCrypt encryption + LUKS encryption of /home), providing defense-in-depth.

---

## Part 6: Recovery Procedures

### 6.1 Boot Passphrase Recovery (Lost or Forgotten)

**Scenario**: You've forgotten your LUKS boot passphrase, but you have the offline recovery key.

**Recovery procedure**:

1. **Boot from Ubuntu 24.04 LTS live USB**
2. **Open encrypted volume using recovery key**:
   ```bash
   # Identify encrypted partition (typically /dev/nvme0n1p3)
   lsblk
   
   # You need the recovery key (256-character string from cold storage)
   # Create temp file with recovery key
   echo "YOUR_256_CHARACTER_RECOVERY_KEY" > /tmp/recovery.key
   
   # Open encrypted volume
   sudo cryptsetup luksOpen --key-file /tmp/recovery.key /dev/nvme0n1p3 my_root
   
   # Mount and access your system
   sudo mount /dev/mapper/my_root /mnt
   sudo mount /dev/nvme0n1p2 /mnt/boot/efi  # EFI partition
   ```

3. **Reset boot passphrase**:
   ```bash
   # Chroot into mounted filesystem
   sudo chroot /mnt
   
   # Set new passphrase using recovery key
   sudo cryptsetup luksChangeKey /dev/nvme0n1p3 \
     --key-slot 0 \
     --key-file /tmp/recovery.key
   # Prompted: "Enter new passphrase"
   
   # Exit chroot
   exit
   ```

4. **Reboot and test new passphrase**:
   ```bash
   sudo umount -R /mnt
   sudo cryptsetup luksClose my_root
   # Remove live USB and reboot
   ```

### 6.2 Restore from Restic Backup (Ransomware/Disaster Recovery)

**Scenario**: Ransomware encrypted your files; you need to restore from backup.

**Restore procedure**:

```bash
# Boot into safe mode or live USB (if system is compromised)
# If using live USB, mount encrypted volumes first:
sudo cryptsetup luksOpen /dev/nvme0n1p3 my_root
sudo mount /dev/mapper/my_root /mnt

# List available snapshots
RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
RESTIC_PASSWORD_FILE=/root/.restic_password \
restic snapshots

# Restore entire /home from snapshot before ransomware
# Example: restore from snapshot 7d2a3b5 (date 2026-06-20)
RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
RESTIC_PASSWORD_FILE=/root/.restic_password \
restic restore 7d2a3b5 --target /mnt

# Alternatively, restore to temporary directory and inspect files
RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
RESTIC_PASSWORD_FILE=/root/.restic_password \
restic restore 7d2a3b5 --target /tmp/restore_check

# Verify restored files are not corrupted
ls -la /tmp/restore_check/home/
```

**Important**: Restic stores multiple snapshots per data version. Choose the snapshot date before ransomware infection occurred.

### 6.3 Header Corruption Recovery (LUKS)

**Scenario**: LUKS header is corrupted (disk I/O error, accidental overwrite). All keyslots are lost.

**Recovery procedure** (if header backup exists):

```bash
# Boot live USB
# Restore header from backup
sudo cryptsetup luksHeaderRestore /dev/nvme0n1p3 \
  --header-backup-file /media/usb_backup/luks_root_header_20260624.bin

# Unlock with restored keyslots
sudo cryptsetup luksOpen /dev/nvme0n1p3 my_root

# Verify filesystem integrity
sudo fsck.ext4 -v /dev/mapper/my_root

# Mount and recover data
sudo mount /dev/mapper/my_root /mnt
```

**If no backup exists**: All data is unrecoverable (this is why header backup is mandatory).

---

## Part 7: Integration with Phase 1

### 7.1 Windows Encryption (VeraCrypt) + Linux Encryption (LUKS) Coordination

**Complementary approach**:
- **Windows**: VeraCrypt full-disk encryption + BitLocker (if available)
- **Linux**: LUKS2 full-disk encryption + TPM2 optional
- **Result**: Both systems encrypted at rest; each is independent

**Threat model improvement**:
- Stolen Windows laptop: VeraCrypt encryption protects data at rest
- Stolen Linux laptop: LUKS2 encryption protects data at rest
- Stolen external backup USB: VeraCrypt encryption (Windows-portable) protects backups
- Compromised cloud account: restic encryption (AES-256-GCM) protects cloud backups

### 7.2 Backup Strategy Spanning Windows + Linux

**Cross-platform backup architecture**:

```
Windows (C:/)
    ↓
restic backup (via Windows Restic binary)
    ↓
rclone → Proton Drive (single cloud backup for both OSes)

Linux (/home, /etc, /root)
    ↓
restic backup (via Linux restic)
    ↓
rclone → Proton Drive (same cloud repo, different snapshots)
```

**Setup on Windows** (post-Phase 1):
```powershell
# Download Restic Windows binary from https://github.com/restic/restic/releases
# Download rclone Windows binary from https://rclone.org/downloads/

# Configure rclone for Proton Drive (same credentials as Linux)
rclone.exe config

# Initialize same restic repository (on Proton Drive)
# Use Windows Task Scheduler for daily backups
# Or use Backup app (built-in to Windows)
```

**Result**: Windows + Linux backups go to same Proton Drive repository; restic deduplication means only changed blocks are stored (not double-backed-up).

### 7.3 Unified Threat Model (Windows + Linux + Backups)

See **Part 2** of the threat model specification for scenarios.

---

## Summary and Checklist

### Completion Checklist (Per Section)

**Part 1: Linux Encryption**
- [ ] LUKS2 installed on system disk (`cryptsetup luksDump /dev/nvme0n1p3` shows LUKS version 2)
- [ ] Passphrase set and tested (boot from cold)
- [ ] Recovery key generated and stored offline (paper + encrypted USB in separate location)
- [ ] Header backup created and tested restore
- [ ] TPM2 integration verified (optional; `cryptsetup luksDump` shows token)

**Part 2: Encrypted Backups**
- [ ] restic + rclone installed and verified (`restic version`, `rclone version`)
- [ ] Proton Drive account created and rclone configured
- [ ] restic repository initialized on Proton Drive
- [ ] Repository password stored in password manager + cold storage
- [ ] Systemd timer running daily backups (`systemctl status restic-backup.timer`)
- [ ] First backup completed and verified (`restic snapshots` shows at least 1 snapshot)
- [ ] Monthly integrity check timer enabled (`systemctl status restic-check.timer`)
- [ ] Backblaze B2 fallback configured (optional but recommended)
- [ ] Offline USB drive encrypted and first copy created

**Part 3: Network Security**
- [ ] DNS-over-TLS enabled in systemd-resolved (`systemd-resolve --status` shows "DNSSEC setting: yes, DNS over TLS: yes")
- [ ] UFW firewall enabled with default deny policies
- [ ] VPN kill-switch configured (UFW rules allow only VPN tunnel interface)
- [ ] IPv6 disabled (if VPN is IPv4-only)
- [ ] VPN kill-switch tested (connection hangs when VPN unexpectedly disconnects)
- [ ] Nginx reverse proxy installed (if hosting internet-facing services)

**Part 4: VPN + Tor**
- [ ] Mullvad or ProtonVPN installed and tested
- [ ] VPN kill-switch tested successfully
- [ ] Tor Browser downloaded (from official source), signature verified, installed
- [ ] Tor Browser security level set to "Safer" or "Safest"
- [ ] Tor Browser not used for routine non-sensitive browsing

**Part 5: Data Management**
- [ ] Asset classification completed (document sensitivity, backup frequency)
- [ ] Bitwarden (or KeePass) set up for credential management
- [ ] SSH keys generated with passphrase and passphrase stored in Bitwarden
- [ ] SSH public key uploaded to GitHub/GitLab
- [ ] Sensitive financial data isolated in VeraCrypt container (if applicable)

**Part 6: Recovery**
- [ ] Recovery key tested (can successfully open LUKS volume via recovery key)
- [ ] Header backup restore tested on test partition (not production)
- [ ] Restic restore tested to temporary directory (verify snapshot recovery works)

**Part 7: Integration**
- [ ] Windows Phase 1 completion understood (VeraCrypt encryption active)
- [ ] Cross-platform backup architecture reviewed (Windows + Linux both backed up to same Proton Drive)
- [ ] Unified threat model documented

---

## Time Estimates

| Component | Time | Notes |
|---|---|---|
| LUKS2 setup (fresh install) | 2-4 hours | Includes OS install + encryption setup + testing |
| LUKS2 in-place encryption | 4-6 hours | Includes backup + reencryption (4-8 hours) + testing |
| Multi-keyslot setup + header backup | 1 hour | Recovery key generation, offline storage |
| restic + rclone setup | 1-2 hours | Account creation, rclone config, first backup run |
| Systemd timer automation | 1 hour | Service + timer creation, testing |
| UFW + VPN kill-switch | 1-2 hours | Rules configuration, testing |
| DNS-over-TLS setup | 30 minutes | systemd-resolved config, verification |
| Tor Browser installation | 30 minutes | Download, signature verification, security level config |
| Offline USB backup setup | 1 hour | Encryption, initial backup, rotation schedule |
| Documentation + asset mapping | 2 hours | Classify data, document recovery procedures |
| **Total estimated** | **30-40 hours** | Spread over 3-4 weeks |

---

## Next Steps

1. **Print or secure recovery key**: Before proceeding beyond LUKS2 setup, print the recovery key on paper and store it in a safe. Test recovery at least once.

2. **Test all recovery procedures**: In a safe environment (test laptop or VM), verify that you can recover data using the recovery key, offline header backup, and restic snapshots. This is not optional.

3. **Backup storage rotation**: Set calendar reminders for monthly offline USB backup and quarterly header backup verification.

4. **Credential management**: Migrate all passwords and secrets to Bitwarden or KeePass before implementing automated backups.

5. **Monitor backups**: Set up email alerts or Prometheus monitoring for backup failures (via `restic check` and systemd journal logging).

---

**End of Phase 2 Infrastructure Specification**
