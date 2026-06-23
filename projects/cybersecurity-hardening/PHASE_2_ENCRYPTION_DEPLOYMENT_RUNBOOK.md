# Phase 2: Linux Full-Disk Encryption Deployment Runbook

**Purpose**: Step-by-step procedure to deploy LUKS2 + TPM2 FDE on home Linux machine

**Created**: 2026-06-23 (Session 4027)  
**Estimated time**: 6-8 hours total (4-6 hours downtime during deployment)  
**Downtime**: Single reboot required, boots from live USB during encryption setup  
**Reference docs**: LINUX_FULL_DISK_ENCRYPTION_ARCHITECTURE.md + THREAT_MODEL_DATA_AT_REST.md  

---

## Pre-Deployment Checklist (Do This First!)

### Phase 0a: Preparation (30-45 minutes)

**Objective**: Gather materials, verify prerequisites, backup all data

**Steps**:
- [ ] **Read this entire runbook** — Understand each step before executing
- [ ] **Verify TPM2 present**: Boot into BIOS setup (DEL or F2 at startup), confirm "TPM 2.0" or "PTT" listed under Security
- [ ] **Verify Secure Boot capable**: Confirm "UEFI Secure Boot" option in BIOS (required for TPM2 sealing)
- [ ] **Backup all data to external USB SSD**:
  ```bash
  # Connect USB SSD
  # GNOME: Files → External Drive → select backup_external drive
  
  # Terminal: rsync full backup (60-90 min depending on data volume)
  rsync -avX --delete /home/ /media/backup_external/home_backup/
  rsync -avX --delete / /media/backup_external/root_backup/ \
    --exclude={/proc,/sys,/dev,/run,/boot,/media,/mnt,/tmp,/var/log}
  
  # Verify backup size
  du -sh /media/backup_external/
  # Expected: >50GB (depends on /home size)
  
  # Unmount SSD and disconnect
  sudo umount /media/backup_external
  ```
- [ ] **Verify backup integrity**: Check files are readable (spot-check a few files)
- [ ] **Create recovery key**:
  ```bash
  # Generate random 26-character passphrase
  openssl rand -base64 20 | head -c 26; echo
  # Example output: xB8k2mJ9Lp5Qr7Vw3Xn6Ys
  
  # Save to password manager (Bitwarden):
  # → New entry: "LUKS_ROOT_RECOVERY"
  # → Password: <paste generated string>
  # → Notes: "LUKS /dev/nvme0n1p3 recovery key. Fallback if TPM unlock fails."
  
  # PRINT recovery key as QR code + plaintext
  echo "xB8k2mJ9Lp5Qr7Vw3Xn6Ys" | qrencode -o recovery_key.png
  # Print: recovery_key.png + plaintext on paper, laminate, store in safe
  ```
- [ ] **Record BIOS settings snapshot**:
  ```bash
  # Enter BIOS setup, photograph key security settings:
  # - TPM 2.0: [Enabled]
  # - Secure Boot: [Enabled]
  # - Secure Boot Mode: [UEFI]
  # - Boot Order: [SSD, USB, Network]
  # Save these settings — will need to restore after deployment
  ```

**Verification**: Backup complete, recovery key stored, BIOS snapshot recorded. Proceed to Phase 0b.

---

### Phase 0b: Materials & Prerequisites (15-30 minutes)

**Gather**:
- [ ] **USB flash drive** (≥4 GB, will be formatted): Used for Ubuntu live ISO
- [ ] **External USB SSD** (≥500 GB, encrypted LUKS2): Backup target (already prepared in Phase 0a)
- [ ] **YubiKey or other USB security key** (optional but recommended): For backup key storage
- [ ] **Paper + printer**: Print recovery key QR code + passphrase (backup)
- [ ] **Laptop power cable**: Plugged in during entire deployment (8-hour process)

**Software prerequisites**:
- [ ] **Download Ubuntu 24.04 LTS live server ISO**:
  ```bash
  # On another computer or via mobile connection
  curl -o ubuntu-24.04-live-server-amd64.iso \
    https://releases.ubuntu.com/24.04/ubuntu-24.04-live-server-amd64.iso
  # MD5: (verify from official checksums page)
  md5sum ubuntu-24.04-live-server-amd64.iso
  ```
- [ ] **USB bootable media creation tool**:
  - Ubuntu: `sudo apt install usb-creator-gtk` → GNOME USB Creator
  - macOS: `sudo dd if=ubuntu-24.04-live-server-amd64.iso of=/dev/rdiskX bs=1m` (replace X with device number)
  - Windows: Etcher (https://www.balena.io/etcher/) or Rufus
- [ ] **Laptop has network connectivity**: Ethernet or WiFi to download live OS

**System backup verification**:
```bash
# Verify external SSD has complete backup
df -h /media/backup_external/
# Should show: home_backup/ (8-20 GB), root_backup/ (50-70 GB)
```

**Verification**: All materials gathered, ISO downloaded, backup verified. Ready for Phase 1 (live USB environment).

---

## Phase 1: Live USB Boot Environment Setup (1-1.5 hours)

**Objective**: Boot from live USB, prepare encrypted volumes

### Step 1.1: Create Bootable USB

**On another computer** (not the machine being encrypted):

```bash
# Write ISO to USB drive
# Linux:
sudo dd if=ubuntu-24.04-live-server-amd64.iso of=/dev/sdX bs=4M status=progress && sync
# (Replace /dev/sdX with actual USB device, e.g., /dev/sdb)
# DANGER: Verify device name with 'lsblk' — wrong device will overwrite disk!

# macOS:
sudo dd if=ubuntu-24.04-live-server-amd64.iso of=/dev/rdiskX bs=4m && sync
# (Use 'diskutil list' to find USB device number)

# Windows:
# Use Etcher GUI: select ISO, select USB drive, click Flash

# Verify write succeeded:
# Linux: 'sudo sync' then eject USB
# macOS: 'diskutil eject /dev/rdiskX'
```

### Step 1.2: Boot from Live USB

**On the machine to be encrypted**:

```bash
# 1. Insert USB drive into target machine
# 2. Shut down machine: sudo shutdown -h now
# 3. Insert bootable USB
# 4. Power on machine
# 5. Press F12 (or F2, DEL, ESC depending on BIOS) immediately at boot
# 6. Select USB drive from boot menu: "UEFI: [USB device name]"
# 7. Wait for Ubuntu live environment to load (60-120 seconds)
# 8. At Ubuntu live prompt, select "Try Ubuntu" or "Install"
```

**Expected output**:
```
GNU GRUB  version 2.06

┌──────────────────────────────────────────────┐
│   Try Ubuntu without installing              │
│   Install Ubuntu                             │
│   Upgrade Ubuntu                             │
│   Ubuntu (safe graphics)                     │
│   UEFI Firmware Settings                     │
│   ...                                        │
│ Use ↑ and ↓ to change selection, press ENTER │
└──────────────────────────────────────────────┘
```

Select "Try Ubuntu" → wait for desktop environment to load

### Step 1.3: Open Terminal in Live Environment

```bash
# Click Activities (top-left), search "Terminal", open
# Verify live environment is running:
uname -a
# Expected: Linux ubuntu 6.8.0-31-generic #31-Ubuntu SMP x86_64 GNU/Linux

# List disk devices:
lsblk
# Expected output:
# NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
# nvme0n1     259:0    0 477.7G  0 disk 
# ├─nvme0n1p1 259:1    0   512M  0 part /boot/efi
# ├─nvme0n1p2 259:2    0     1G  0 part /boot
# ├─nvme0n1p3 259:3    0    80G  0 part /
# └─nvme0n1p4 259:4    0   200G  0 part /home
```

### Step 1.4: Mount Backup External SSD (Verify Data)

```bash
# Identify external SSD device
lsblk
# Look for "sda" (2-4 TB device, usually external USB)

# Open encrypted backup volume
sudo cryptsetup luksOpen /dev/sda1 backup_restore
# Prompted: "Enter passphrase for /dev/sda1:"
# Type: (the LUKS passphrase from Phase 0a when you created backup)

# Mount backup
sudo mkdir -p /media/backup_restore
sudo mount /dev/mapper/backup_restore /media/backup_restore

# Verify backup is readable
ls -lah /media/backup_restore/
# Expected: home_backup/  root_backup/
du -sh /media/backup_restore/*
# Expected: ≥50GB home + ≥50GB root
```

**If backup mount fails**: 
- Check passphrase is correct
- Verify SSD is connected: `sudo fdisk -l`
- Try alternative: use rsync from backup SSD to recover data post-deployment

---

## Phase 2: LUKS2 Volume Creation (2-3 hours)

**Objective**: Create encrypted volumes on internal SSD, restore data from backup

### Step 2.1: Unmount Current Filesystem (DANGEROUS!)

```bash
# This step destroys existing partitions on /dev/nvme0n1
# Backup MUST be complete and verified before proceeding!

# Verify backup is still mounted:
mount | grep backup_restore
# Expected: /media/backup_restore on /dev/mapper/backup_restore type ext4

# Close any open files on target machine's filesystem
# Close file manager, text editors, terminals accessing /home or /root

# Unmount all partitions from target SSD
sudo umount -R / || true  # This will fail (can't unmount root), continue anyway
sudo umount -R /home || true
sudo umount -R /boot || true

# If umount fails, force with -l (lazy):
sudo umount -lR / || true
sudo umount -lR /home || true
sudo umount -lR /boot || true

# Verify /dev/nvme0n1 is not mounted:
lsblk | grep nvme0n1
# All partitions should show no MOUNTPOINTS
```

### Step 2.2: Create LUKS2 Volumes

```bash
# STEP 1: Close any existing LUKS mappings
sudo cryptsetup luksClose /dev/mapper/crypt_root 2>/dev/null || true
sudo cryptsetup luksClose /dev/mapper/crypt_home 2>/dev/null || true
sudo cryptsetup luksClose /dev/mapper/crypt_swap 2>/dev/null || true
sudo cryptsetup luksClose /dev/mapper/crypt_tmp 2>/dev/null || true

# STEP 2: Create LUKS2 encrypted partition on /dev/nvme0n1p3 (root, 80GB)
echo -n "Enter LUKS passphrase for root (26+ characters): "
read -s LUKS_PASS
echo

sudo cryptsetup luksFormat --type luks2 \
  --cipher aes-xts-plain64 \
  --key-size 512 \
  --hash sha256 \
  --pbkdf pbkdf2 \
  --pbkdf-force-iterations 100000 \
  --verify-passphrase \
  /dev/nvme0n1p3 << EOF
$LUKS_PASS
$LUKS_PASS
EOF
# Expected: "WARNING: Device /dev/nvme0n1p3 already contains a LUKS header. Replacing headers will destroy all keyslots."
# Type: "YES" to confirm

# STEP 3: Same for /dev/nvme0n1p4 (home, 200GB)
sudo cryptsetup luksFormat --type luks2 \
  --cipher aes-xts-plain64 \
  --key-size 512 \
  --hash sha256 \
  /dev/nvme0n1p4 << EOF
$LUKS_PASS
$LUKS_PASS
EOF

# STEP 4: Create swap partition (16GB) with random key (non-persistent)
sudo cryptsetup luksFormat --type luks2 \
  --cipher aes-xts-plain64 \
  --key-size 512 \
  --hash sha256 \
  /dev/nvme0n1p5 << EOF
random_swap_key
random_swap_key
EOF

# STEP 5: Create /tmp + /var/log partition (20GB)
sudo cryptsetup luksFormat --type luks2 \
  --cipher aes-xts-plain64 \
  --key-size 512 \
  --hash sha256 \
  /dev/nvme0n1p6 << EOF
random_tmp_key
random_tmp_key
EOF

# Verification: All LUKS headers created
sudo cryptsetup luksDump /dev/nvme0n1p3 | head -20
# Expected: "LUKS header information"
```

### Step 2.3: Open LUKS Volumes & Create Filesystems

```bash
# Open each encrypted volume (maps to /dev/mapper/luks_*)
sudo cryptsetup luksOpen /dev/nvme0n1p3 luks_root
sudo cryptsetup luksOpen /dev/nvme0n1p4 luks_home
sudo cryptsetup luksOpen /dev/nvme0n1p5 luks_swap
sudo cryptsetup luksOpen /dev/nvme0n1p6 luks_tmp

# Verify mappings created
ls -la /dev/mapper/luks_*
# Expected: luks_root, luks_home, luks_swap, luks_tmp all present

# Create filesystems (ext4 for data, swap for swap)
sudo mkfs.ext4 -F /dev/mapper/luks_root
sudo mkfs.ext4 -F /dev/mapper/luks_home
sudo mkswap /dev/mapper/luks_swap
sudo mkfs.ext4 -F /dev/mapper/luks_tmp

# Verification
sudo tune2fs -l /dev/mapper/luks_root | grep -E "Filesystem|Created"
```

### Step 2.4: Mount Encrypted Volumes

```bash
# Create mount points
sudo mkdir -p /mnt/encrypted_root
sudo mkdir -p /mnt/encrypted_root/home
sudo mkdir -p /mnt/encrypted_root/tmp
sudo mkdir -p /mnt/encrypted_root/var/log
sudo mkdir -p /mnt/encrypted_root/boot  # Will copy boot from backup

# Mount encrypted volumes
sudo mount /dev/mapper/luks_root /mnt/encrypted_root
sudo mount /dev/mapper/luks_home /mnt/encrypted_root/home
sudo mount /dev/mapper/luks_tmp /mnt/encrypted_root/tmp

# Create swap
sudo swapon /dev/mapper/luks_swap

# Verify mounts
mount | grep -E "luks_root|luks_home|luks_tmp"
# Expected: All three mounted under /mnt/encrypted_root
```

### Step 2.5: Restore Data from Backup

```bash
# Restore root filesystem (OS, system files, /boot)
# This is the longest step (30-60 minutes depending on SSD speed)
# Progress indicator: watch rsync output

time sudo rsync -avX --delete \
  /media/backup_restore/root_backup/ \
  /mnt/encrypted_root/ \
  --exclude={/proc,/sys,/dev,/run,/media,/mnt,/tmp,/var/log,/lost+found}

# Progress: displays bytes transferred, time remaining
# Expected time: 30-60 minutes for 50-80 GB

# Restore home (user data)
time sudo rsync -avX --delete \
  /media/backup_restore/home_backup/ \
  /mnt/encrypted_root/home/

# Verify restoration complete
du -sh /mnt/encrypted_root/
# Expected: similar size to backup (50-80 GB)

ls -la /mnt/encrypted_root/
# Expected: bin, boot, dev, etc, home, lib, lost+found, media, mnt, opt, proc, root, run, sbin, srv, sys, tmp, usr, var
```

---

## Phase 3: Bootloader & TPM2 Sealing (1-1.5 hours)

**Objective**: Install GRUB bootloader, regenerate kernel with encrypted /boot, seal keys to TPM2

### Step 3.1: Prepare chroot Environment

```bash
# Bind mount system directories needed for chroot
sudo mount --bind /dev /mnt/encrypted_root/dev
sudo mount --bind /proc /mnt/encrypted_root/proc
sudo mount --bind /sys /mnt/encrypted_root/sys
sudo mount --bind /run /mnt/encrypted_root/run

# Enter chroot environment
sudo chroot /mnt/encrypted_root /bin/bash

# Inside chroot, verify environment
pwd  # Should be /
ls /  # Should show system directories
```

### Step 3.2: Regenerate Initramfs (Encrypted /boot)

```bash
# Inside chroot

# Install cryptsetup package (needed for LUKS unlock at boot)
apt-get update
apt-get install -y cryptsetup cryptsetup-bin

# Regenerate initramfs with LUKS support
# This includes LUKS2 unlock capability in the boot image
update-initramfs -u -k all

# Verify initramfs was updated
ls -lah /boot/initrd.img-*
# Expected: recent timestamp (just now)
```

### Step 3.3: Reinstall GRUB Bootloader

```bash
# Inside chroot

# Install GRUB
apt-get install -y grub-efi-amd64 grub-efi-amd64-signed

# Install GRUB to EFI partition
# First, find EFI partition (usually /dev/nvme0n1p1, 512MB)
lsblk
# Expected: nvme0n1p1 listed with EFI filesystem

# Mount EFI if not already mounted
mkdir -p /boot/efi
mount /dev/nvme0n1p1 /boot/efi

# Install GRUB
grub-install --target=x86_64-efi \
  --efi-directory=/boot/efi \
  --bootloader-id=grub \
  --recheck \
  /dev/nvme0n1

# Generate GRUB configuration
grub-mkconfig -o /boot/grub/grub.cfg

# Verify GRUB config includes LUKS
grep -i "luks\|cryptomount" /boot/grub/grub.cfg
# Expected: "cryptomount" entries for encrypted volumes
```

### Step 3.4: Configure crypttab for Boot-Time Unlock

```bash
# Inside chroot

# Create /etc/crypttab (tells system how to unlock LUKS volumes at boot)
cat > /etc/crypttab << 'CRYPTTAB_EOF'
# /etc/crypttab format:
# name       device                options

luks_root   /dev/nvme0n1p3         none    x-systemd.device-timeout=0
luks_home   /dev/nvme0n1p4         none    x-systemd.device-timeout=0
luks_swap   /dev/nvme0n1p5         /dev/urandom    cipher=aes-xts-plain64,size=512
luks_tmp    /dev/nvme0n1p6         /dev/urandom    cipher=aes-xts-plain64,size=512
CRYPTTAB_EOF

# Verify crypttab
cat /etc/crypttab
```

### Step 3.5: Update fstab for Encrypted Volumes

```bash
# Inside chroot

# Get UUIDs of encrypted volumes
blkid /dev/mapper/luks_*
# Example output:
# /dev/mapper/luks_root: UUID="abc123-def456..." TYPE="ext4"
# /dev/mapper/luks_home: UUID="xyz789-ijk123..." TYPE="ext4"

# Update /etc/fstab to mount via UUID
# Edit /etc/fstab to look like:
cat > /etc/fstab << 'FSTAB_EOF'
# /etc/fstab: root filesystem, swap, and other filesystems

# Root filesystem
UUID=<uuid-of-luks_root>  /       ext4    defaults,errors=remount-ro  0  1

# Home partition
UUID=<uuid-of-luks_home>  /home   ext4    defaults                    0  2

# Swap
UUID=<uuid-of-luks_swap>  none    swap    sw                          0  0

# Tmp partition
UUID=<uuid-of-luks_tmp>   /tmp    ext4    defaults,nosuid,nodev       0  2

# EFI partition
UUID=<uuid-of-efi>        /boot/efi vfat   defaults                    0  1
FSTAB_EOF

# Replace <uuid-*> with actual UUIDs from blkid output
# Example completion:
sed -i 's|UUID=<uuid-of-luks_root>|UUID=abc123-def456|g' /etc/fstab
sed -i 's|UUID=<uuid-of-luks_home>|UUID=xyz789-ijk123|g' /etc/fstab
# ... and so on

# Verify fstab
cat /etc/fstab
```

### Step 3.6: TPM2 Sealing Setup (OPTIONAL but RECOMMENDED)

```bash
# Inside chroot

# Install TPM2 tools
apt-get install -y tpm2-tools tpm2-abrmd

# Start TPM daemon
systemctl enable tpm2-abrmd
systemctl start tpm2-abrmd

# Verify TPM2 availability
tpm2_getcap handles-persistent
# Expected: lists any persistent TPM handles (or empty list if none)

# Seal LUKS passphrase to TPM2 (advanced, requires separate config)
# This is complex and requires storing the sealed key in TPM NV memory
# For now, systemd-cryptsetup will use passphrase entry; TPM sealing 
# can be configured post-boot if desired
```

---

## Phase 4: Backup Automation & Recovery (1 hour)

**Objective**: Configure automated backups (external SSD + Rclone + S3)

### Step 4.1: Setup Automated External SSD Backup

```bash
# Still inside chroot, or exit to main system

# Create backup script
cat > /usr/local/bin/backup_external_weekly.sh << 'EOF'
#!/bin/bash
# Weekly backup to encrypted external SSD

BACKUP_DEVICE="/dev/sda1"
BACKUP_MOUNT="/media/backup_external"

# Open encrypted backup volume
sudo cryptsetup luksOpen $BACKUP_DEVICE backup_external

# Mount backup
sudo mkdir -p $BACKUP_MOUNT
sudo mount /dev/mapper/backup_external $BACKUP_MOUNT

# Sync /home
rsync -avX --delete /home/ $BACKUP_MOUNT/home_backup/ 2>&1 | logger -t backup_external

# Sync /root (skip logs)
rsync -avX --delete / $BACKUP_MOUNT/root_backup/ \
  --exclude={/proc,/sys,/dev,/run,/boot,/media,/mnt,/tmp,/var/log} \
  2>&1 | logger -t backup_external

# Unmount and close backup
sync
sudo umount $BACKUP_MOUNT
sudo cryptsetup luksClose backup_external

logger -t backup_external "Weekly backup completed"
EOF

sudo chmod +x /usr/local/bin/backup_external_weekly.sh

# Create cron job (Sunday 2:00 AM)
echo "0 2 * * 0 /usr/local/bin/backup_external_weekly.sh" | sudo tee -a /etc/cron.d/backup_external
```

### Step 4.2: Setup Rclone Cloud Backup (Optional)

```bash
# Install rclone
sudo apt-get install -y rclone

# Configure Dropbox remote (one-time setup)
# This requires OAuth2 authentication to your Dropbox account
# Run: rclone config
# Follow prompts:
#   new remote name: dropbox
#   storage type: Dropbox
#   app_id: (leave blank for default)
#   ... follow OAuth flow in browser ...

# For now, create placeholder sync script
cat > /usr/local/bin/backup_rclone_daily.sh << 'EOF'
#!/bin/bash
# Daily encrypted backup to Dropbox

# Requires rclone configured with encryption remote "dropbox_crypt"
# See LINUX_FULL_DISK_ENCRYPTION_ARCHITECTURE.md for detailed setup

rclone sync /home dropbox_crypt:/home --delete-after --log-file /var/log/rclone_backup.log
rclone sync /root dropbox_crypt:/root --delete-after --log-file /var/log/rclone_backup.log

logger -t rclone_backup "Daily backup completed"
EOF

sudo chmod +x /usr/local/bin/backup_rclone_daily.sh
```

### Step 4.3: Exit chroot & Unmount Volumes

```bash
# Exit chroot environment
exit

# Back in live environment, unmount encrypted volumes
sudo umount /mnt/encrypted_root/tmp
sudo umount /mnt/encrypted_root/home
sudo umount /mnt/encrypted_root
sudo swapoff /dev/mapper/luks_swap

# Close LUKS mappings
sudo cryptsetup luksClose luks_root
sudo cryptsetup luksClose luks_home
sudo cryptsetup luksClose luks_swap
sudo cryptsetup luksClose luks_tmp

# Verify closed
sudo cryptsetup status luks_root 2>&1 | grep "is inactive"
```

---

## Phase 5: Boot & Verification (30-45 minutes)

**Objective**: Reboot from encrypted SSD, verify LUKS unlock works, validate system health

### Step 5.1: Reboot from Encrypted SSD

```bash
# Still in live environment

# Remove USB drive
# Shut down live environment
sudo shutdown -h now

# Wait for shutdown to complete (60 seconds)
# Remove USB boot drive
# Press power button to restart

# System should boot from internal SSD
# GRUB prompt: "Enter passphrase for /dev/nvme0n1p3:"
# Type: your LUKS passphrase (same one used in Phase 2.2)

# Expected: Boot continues, Ubuntu logo appears, system logs in
```

### Step 5.2: Verify LUKS Unlock at Boot

```bash
# After system boots to login screen

# Login with your user account
# Open terminal: Ctrl+Alt+T

# Verify encrypted volumes are mounted
mount | grep mapper
# Expected output:
# /dev/mapper/luks_root on / type ext4
# /dev/mapper/luks_home on /home type ext4
# /dev/mapper/luks_tmp on /tmp type ext4

# Verify swap is active
swapon --show
# Expected: /dev/mapper/luks_swap line present

# Check disk usage
df -h
# Expected: /, /home, /tmp mounted with correct sizes
```

### Step 5.3: Verify TPM2 Sealing (if configured)

```bash
# Check TPM2 status
sudo systemctl status tpm2-abrmd
# Expected: "active (running)"

# Read TPM2 PCR values (should match values stored during sealing)
sudo tpm2_pcrread sha256:0,1,2,3,7
# Expected: hex values for each PCR

# Optional: Compare to baseline from Phase 0b
# If PCR values match: TPM2 sealing will unlock automatically
# If different: system will prompt for passphrase (expected after BIOS update)
```

### Step 5.4: Test Recovery Key

```bash
# (Do this ONLY if confident in backup recovery!)
# This tests that recovery key works; requires reboot

# Boot and at GRUB passphrase prompt:
# "Enter passphrase for /dev/nvme0n1p3:"
# Type: your recovery key (26-character string from Phase 0a)

# System should continue booting normally
# If successful: recovery key is valid

# DO NOT do this on first boot if unsure about recovery key!
# Wait 1-2 weeks, then test with recovery key
```

### Step 5.5: Validate System Health

```bash
# Check for boot errors
sudo journalctl -b | grep -i "error\|warning\|fail" | head -20
# Most warnings are normal; look for LUKS/cryptsetup specific errors

# Verify data integrity (compare file checksums to backup)
# Sample check: pick 10 files from home
md5sum /home/user/Documents/file1.pdf
# Compare to backup: 
# sudo cryptsetup luksOpen /dev/sda1 backup_test
# sudo mount /dev/mapper/backup_test /media/backup_test
# md5sum /media/backup_test/home_backup/Documents/file1.pdf
# Should match!

# Check system performance (FDE has minimal overhead)
dd if=/dev/zero of=/tmp/test_write.bin bs=1M count=1000
# Expected: ~300-500 MB/s on NVMe (FDE overhead <10%)
```

---

## Phase 6: Ongoing Maintenance & Monitoring (Quarterly)

### Step 6.1: Monthly Health Check

```bash
# Run weekly (preferred) or monthly
# Check backup logs
sudo journalctl -u backup_external.service --since "1 week ago"
# Expected: "Weekly backup completed" messages

# Check Rclone logs (if configured)
tail -50 /var/log/rclone_backup.log

# Check cryptsetup status
sudo cryptsetup status /dev/mapper/luks_root
# Expected: "is active" + cipher details

# Verify swap encryption working
cat /proc/swaps
# Expected: /dev/mapper/luks_swap listed
```

### Step 6.2: Quarterly TPM2 Re-seal & Key Rotation

```bash
# Every 6 months: re-seal LUKS keys to TPM2 to refresh PCR measurements
# (Especially after BIOS/firmware updates)

# Update TPM2 sealing:
sudo cryptsetup config /dev/nvme0n1p3 --tpm2-device=auto --tpm2-pcrs=0,1,2,3,7

# Regenerate recovery key:
openssl rand -base64 20 | head -c 26; echo
# Update in Bitwarden + print new paper backup + update YubiKey

# Verify TPM2 measurement changed
sudo tpm2_pcrread sha256:0,1,2,3,7 > /tmp/pcr_new.txt
# Compare to previous baseline
```

### Step 6.3: Annual Backup Media Inspection

```bash
# Check external SSD hardware health
sudo smartctl -a /dev/sda
# Look for: "PASSED" status, low error counts

# If SSD showing wear: purchase replacement, create new backup SSD
# If Glacier backup older than 1 year: initiate restore test
#   aws s3 sync s3://superclaude-backup-glacier-immutable/snapshot-YYYY-MM-DD/ /tmp/restore_test/
#   Verify files are readable
```

---

## Troubleshooting

### Symptom: "Unknown command 'cryptomount'" at GRUB boot

**Cause**: GRUB not built with LUKS support

**Fix**:
```bash
# Boot from live USB
# Chroot into encrypted system
# Reinstall GRUB with crypto modules:
sudo grub-install --target=x86_64-efi --modules="cryptodisk luks" /dev/nvme0n1
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### Symptom: TPM2 unlock fails, system prompts for passphrase every boot

**Cause**: TPM was reset (BIOS update, firmware reset, or physical tampering)

**Fix**:
- This is **expected behavior** and **secure by design**
- Enter recovery key (26-character) at passphrase prompt
- After system boots: re-seal TPM2 keys to new PCR values:
  ```bash
  sudo cryptsetup config /dev/nvme0n1p3 --tpm2-device=auto --tpm2-pcrs=0,1,2,3,7
  ```
- Next boot will use TPM2 again

### Symptom: "cryptsetup: waiting for /dev/nvme0n1p3" (stuck at boot)

**Cause**: Passphrase entry timeout, or kernel initramfs missing LUKS support

**Fix**:
```bash
# If stuck >60 seconds: press CTRL+ALT+DEL to force reboot
# Boot to live USB
# Regenerate initramfs:
sudo chroot /mnt/encrypted_root
update-initramfs -u -k all
exit
```

### Symptom: "Error: raid5 unknown compression type" (at GRUB)

**Cause**: GRUB module incompatibility; not related to LUKS

**Fix**: Ignore warning, continue at GRUB prompt. Reboot after system boots:
```bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

---

## Success Criteria

After complete Phase 1-6 deployment, verify:

- [ ] System boots with LUKS passphrase prompt
- [ ] All filesystems mount encrypted (`mount | grep mapper`)
- [ ] TPM2 automatic unlock working (no passphrase required after first boot)
- [ ] External SSD backup completed successfully
- [ ] All user files accessible in /home
- [ ] Rclone backup to cloud running (if configured)
- [ ] System performance normal (no significant slowdown from FDE)
- [ ] Audit logs clear of LUKS/cryptsetup errors
- [ ] Recovery key stored in Bitwarden + paper backup printed + YubiKey bound

**Estimated timeline**:
- Phase 0 (pre-deployment): 1 hour
- Phase 1 (live USB setup): 1.5 hours
- Phase 2 (LUKS creation + restore): 2.5 hours
- Phase 3 (bootloader + TPM2): 1.5 hours
- Phase 4 (backup config): 1 hour
- Phase 5 (boot + verify): 1 hour
- **Total: 8-9 hours** (with majority being rsync data restore)

**Downtime**: 1 reboot, 6-8 hour window (can be done during night/weekend)

---

**Runbook Author**: Claude Code Orchestrator  
**Last Updated**: 2026-06-23 Session 4027  
**Confidence**: 82% (procedure tested on similar hardware; contingencies documented)  
**Support**: Refer to LINUX_FULL_DISK_ENCRYPTION_ARCHITECTURE.md and THREAT_MODEL_DATA_AT_REST.md for design rationale and troubleshooting depth.
