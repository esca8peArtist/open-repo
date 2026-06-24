# Phase 2 Provisioning Runbook

**Version**: 1.0  
**Date**: June 24, 2026  
**Status**: Production-Ready  
**Estimated time**: 30-40 hours over 3-4 weeks  
**Format**: Step-by-step procedures with estimated times, dependencies, and rollback instructions

---

## Executive Summary

This runbook provides detailed procedures to implement Phase 2 infrastructure across five domains:

1. **Linux Full-Disk Encryption** (LUKS2): 2-6 hours
2. **Encrypted Backups** (restic + rclone): 2-3 hours
3. **Network Segmentation & VPN** (UFW + Mullvad): 2-3 hours
4. **Tor Browser & DNS Hardening**: 1 hour
5. **Recovery Testing & Verification**: 3-4 hours

**Prerequisite**: Phase 1 (Windows VeraCrypt + iPhone hardening) should be complete before starting Phase 2. However, Sections 2 (Backups) and 4 (VPN/Tor) can proceed in parallel with Phase 1.

**Golden Rule**: Test every recovery procedure on a non-production system (VM or test laptop) BEFORE implementing on your primary machine.

---

## Section 1: Linux Full-Disk Encryption (LUKS2)

### 1A: Fresh Install with Encryption (2-4 hours)

**Scenario**: Installing Ubuntu 24.04 LTS on a new laptop/desktop; want to encrypt from the start.

**Prerequisites**:
- Ubuntu 24.04 LTS installation media (USB drive or ISO)
- Laptop/desktop with 60+ GB free space
- UEFI firmware with Secure Boot support (optional but recommended)

**Procedure**:

1. **Create installation media** (15 min):
   ```bash
   # On another Linux machine, write ISO to USB drive
   lsblk  # Identify USB drive (e.g., /dev/sdb)
   sudo dd if=ubuntu-24.04-live-server-amd64.iso of=/dev/sdb bs=4M
   sync
   ```

2. **Boot from USB and start installer** (2 min):
   - Insert USB drive into target machine
   - Power on; press F2 or F10 (BIOS setup) or DEL (depending on motherboard)
   - In BIOS: set boot order to USB first
   - Save and exit BIOS
   - Machine boots into Ubuntu installer

3. **Select "Advanced Features" → "Install with full-disk encryption"** (1 min):
   - Installer displays "Partition storage" screen
   - Look for "Advanced Features" button or checkbox
   - Select "Install with full-disk encryption (LVM + LUKS)"

4. **Configure encryption** (2 min):
   - **Disk to encrypt**: Select /dev/nvme0n1 (or /dev/sda if SATA drive)
   - **LUKS version**: Select "LUKS 2"
   - **Encryption method**: Leave as default (aes-xts-plain64)

5. **Set passphrase** (2 min):
   - Installer prompts: "Enter passphrase to encrypt partition"
   - Enter strong passphrase (30+ characters, mixed case + numbers + symbols)
   - Example: `Tr0p!cal_M0nkey$_D4nce_#47@Blue_Lagoon`
   - Confirm passphrase
   - **CRITICAL**: Write this passphrase down and store in a password manager immediately after installation

6. **Continue installation** (15-30 min):
   - Select hostname (e.g., "myworkstation")
   - Select username and password
   - Select timezone, keyboard layout
   - Installer partitions disk, creates encrypted container, installs OS
   - Reboot when complete

7. **Test encrypted boot** (2 min):
   - Machine reboots
   - GRUB prompts for LUKS passphrase (before OS boot)
   - Enter passphrase
   - System boots normally
   - Verify `/` is on encrypted partition:
     ```bash
     sudo cryptsetup luksDump /dev/nvme0n1p3
     # Should show: LUKS version 2, keyslot 0 enabled
     ```

8. **Post-install: Store passphrase securely** (5 min):
   - Open Bitwarden (or KeePass)
   - Create new entry: "LUKS Boot Passphrase"
   - Store passphrase + device name
   - Close password manager
   - Never store passphrase on the device itself (defeating encryption)

9. **Post-install: Harden LUKS parameters (optional)** (4-6 hours):
   - This step is optional if you're happy with Ubuntu's defaults
   - Only do this if you want to increase KDF iteration time from default
   - **WARNING**: This procedure locks the system; follow carefully
   ```bash
   # Boot from live USB (insert USB, reboot, press F2 to select boot device)
   
   # From live USB terminal
   lsblk  # Identify encrypted partition
   
   # Start in-place reencryption with stricter KDF
   sudo cryptsetup reencrypt /dev/nvme0n1p3 \
     --type luks2 \
     --cipher aes-xts-plain64 \
     --key-size 512 \
     --hash sha512 \
     --pbkdf argon2id \
     --iter-time 5000
   
   # You will be prompted for the existing passphrase
   # Then prompted for a new passphrase (can be same as current)
   # Reencryption will take 4-6 hours depending on drive size
   # Monitor progress with: cryptsetup status /dev/nvme0n1p3
   
   # After completion, reboot from the encrypted drive (remove USB)
   ```

**Dependencies**: None (standalone fresh install)  
**Rollback**: If installation fails, reboot from USB and start over (no data loss)  
**Time**: 2-4 hours total (most time spent waiting for OS installation and optional reencryption)

**Next step**: Section 1B (Recovery key) or skip to Section 2 (Backups)

---

### 1B: Multi-Keyslot Setup & Recovery Key (1-2 hours)

**Scenario**: You've completed Section 1A (or have existing LUKS2 system). Now add recovery key and verify all keyslots work.

**Prerequisites**:
- Ubuntu 24.04 with LUKS2 encryption running
- Root access (via `sudo`)
- Access to offline storage (USB drive or printer for paper backup)

**Procedure**:

1. **Verify existing keyslot 0 (your passphrase)** (5 min):
   ```bash
   sudo cryptsetup luksDump /dev/nvme0n1p3
   # Output should show:
   # LUKS version: 2
   # Keyslot 0: ENABLED
   
   # Test that passphrase works by trying to unlock to a temporary mapper
   sudo cryptsetup luksOpen --key-slot 0 /dev/nvme0n1p3 test_unlock
   # Enter your passphrase
   # If successful: mapper /dev/mapper/test_unlock is created
   sudo cryptsetup luksClose test_unlock
   ```

2. **Generate recovery key** (5 min):
   ```bash
   # Create a random recovery key (256 characters)
   openssl rand -base64 192 > /tmp/recovery_key.txt
   
   # Display and copy to clipboard
   cat /tmp/recovery_key.txt
   # Example output (yours will be different):
   # 8Kj3mP9lQ2vN5xY7bR4sW6dF8gH0jK2mL4nO6pQ8sT0uV2wX4yZ6aBcD9eF2gH4
   # iJ6kL8mN0oP2qR4sT6uV8wX0yZ2aBcD4eF6gH8iJ0kL2mN4oP6qR8sT0uV2wX4yZ
   # 6aBcD8eF0gH2iJ4kL6mN8oP0qR2sT4uV6wX8yZ0aBcD2eF4gH6iJ8kL0mN2oP4qR
   ```

3. **Add recovery key to LUKS keyslot 1** (3 min):
   ```bash
   sudo cryptsetup luksAddKey /dev/nvme0n1p3 --key-slot 1 --keyfile /tmp/recovery_key.txt
   # Prompt: "Enter any existing passphrase"
   # Enter your boot passphrase (from Section 1A)
   
   # Verify keyslot 1 is now active
   sudo cryptsetup luksDump /dev/nvme0n1p3 | grep -A 5 "Keyslot 1"
   # Should show: Keyslot 1: ENABLED
   ```

4. **Test recovery key unlock** (5 min):
   ```bash
   # Test that recovery key can unlock the volume
   sudo cryptsetup luksOpen --key-slot 1 --keyfile /tmp/recovery_key.txt /dev/nvme0n1p3 test_recovery
   # Should succeed without prompting for passphrase
   
   sudo cryptsetup luksClose test_recovery
   
   # Verify recovery key is correct for future reference
   cat /tmp/recovery_key.txt
   ```

5. **Store recovery key offline** (20 min):
   ```bash
   # Copy 1: Encrypted USB drive (for emergency access)
   # Insert USB drive
   lsblk  # Identify USB (e.g., /dev/sdb1)
   
   # Create VeraCrypt container on USB (optional, for extra security)
   # Or simply copy file with proper permissions
   mkdir -p /mnt/backup_usb
   sudo mount /dev/sdb1 /mnt/backup_usb
   
   sudo cp /tmp/recovery_key.txt /mnt/backup_usb/luks_recovery_key_$(date +%Y%m%d).txt
   sudo chmod 600 /mnt/backup_usb/luks_recovery_key_*.txt
   
   sudo umount /mnt/backup_usb
   ```

6. **Print recovery key for paper backup** (10 min):
   ```bash
   # Print recovery key with metadata
   cat > /tmp/recovery_key_printout.txt << 'EOF'
   ==========================================
   LUKS ENCRYPTION RECOVERY KEY
   ==========================================
   Device: /dev/nvme0n1p3
   Date generated: $(date)
   Passphrase keyslot: 0
   Recovery key keyslot: 1
   
   RECOVERY KEY (256 characters):
   $(cat /tmp/recovery_key.txt)
   
   RECOVERY INSTRUCTIONS:
   1. Boot into Ubuntu Live USB
   2. Open terminal
   3. Run: sudo cryptsetup luksOpen --key-file <path_to_usb>/luks_recovery_key.txt /dev/nvme0n1p3 my_crypt
   4. Mount filesystem: sudo mount /dev/mapper/my_crypt /mnt
   5. Access your files in /mnt/home and /mnt/root
   
   SECURITY:
   - Store this printout in a safe or safety deposit box
   - Do NOT email this key or store in cloud storage
   - Only use recovery key if you've forgotten your boot passphrase
   - Never share recovery key with anyone
   ==========================================
   EOF
   
   # Print to file
   lpr /tmp/recovery_key_printout.txt
   # Or copy to a USB drive and print from another computer
   ```

7. **Securely delete temporary recovery key** (1 min):
   ```bash
   # Overwrite and delete temporary files
   shred -vfz /tmp/recovery_key.txt
   shred -vfz /tmp/recovery_key_printout.txt
   
   # Verify files are deleted
   ls /tmp/recovery_key*
   # Should show: No such file or directory
   ```

8. **Document recovery procedure** (5 min):
   ```bash
   # Create a recovery guide document (store in Bitwarden notes)
   cat > ~/.local/share/LUKS_RECOVERY_PROCEDURE.txt << 'EOF'
   LUKS Recovery Procedure (if boot passphrase is forgotten)
   
   1. Boot from Ubuntu Live USB (press F2 at boot to select device)
   2. Open terminal
   3. Identify encrypted partition: lsblk
   4. Decrypt using recovery key: sudo cryptsetup luksOpen --key-file /media/usb_backup/recovery_key.txt /dev/nvme0n1p3 my_crypt
   5. Mount filesystem: sudo mount /dev/mapper/my_crypt /mnt
   6. Change boot passphrase: sudo cryptsetup luksChangeKey /dev/nvme0n1p3 --key-slot 0 --key-file /media/usb_backup/recovery_key.txt
   7. Enter new passphrase when prompted
   8. Reboot and test new passphrase
   EOF
   
   cat ~/.local/share/LUKS_RECOVERY_PROCEDURE.txt
   ```

**Dependencies**: Section 1A (existing LUKS2 encryption)  
**Rollback**: Recovery key can be removed with `cryptsetup luksKillSlot /dev/nvme0n1p3 1`, but keep it for emergencies  
**Time**: 1-2 hours total (mostly manual, no waiting)

**Next step**: Section 1C (Header Backup)

---

### 1C: LUKS Header Backup (30 min)

**Scenario**: Protect yourself against LUKS header corruption (disk I/O error, accidental overwrite).

**Prerequisites**:
- LUKS2 encryption active
- External USB drive (minimum 1 GB, for header backups)
- Offline storage location (safe, office, safety deposit box)

**Procedure**:

1. **Mount external backup USB** (2 min):
   ```bash
   lsblk  # Identify USB drive (e.g., /dev/sdb1)
   mkdir -p /mnt/backup_usb
   sudo mount /dev/sdb1 /mnt/backup_usb
   
   # Verify mount
   df -h /mnt/backup_usb
   ```

2. **Backup LUKS header** (2 min):
   ```bash
   # Create backup with timestamp
   sudo cryptsetup luksHeaderBackup /dev/nvme0n1p3 \
     --header-backup-file /mnt/backup_usb/luks_root_header_$(date +%Y%m%d_%H%M%S).bin
   
   # Verify backup was created
   ls -lh /mnt/backup_usb/luks_root_header_*.bin
   # Example output: -rw-r--r-- 1 root root 16K Jun 24 10:30 luks_root_header_20260624_103000.bin
   ```

3. **Test header restore (non-destructive)** (5 min):
   ```bash
   # To safely test header restore without affecting your real drive:
   # Option A: Create a test partition (if you have spare space)
   # Option B: Use a loop device (recommended for non-destructive testing)
   
   # Create a temporary copy of your encrypted partition header for testing
   sudo dd if=/dev/nvme0n1p3 of=/tmp/test_partition.img bs=1M count=100
   sudo losetup /dev/loop0 /tmp/test_partition.img
   
   # Test restore to loop device
   sudo cryptsetup luksHeaderRestore /dev/loop0 \
     --header-backup-file /mnt/backup_usb/luks_root_header_20260624_103000.bin
   # Should succeed silently
   
   # Verify header restore worked
   sudo cryptsetup luksDump /dev/loop0 | head -20
   # Should show LUKS version 2, keyslot info
   
   # Clean up test
   sudo losetup -d /dev/loop0
   sudo rm /tmp/test_partition.img
   ```

4. **Store backup in two locations** (5 min):
   ```bash
   # Location 1: USB drive in office / alternate home location
   # (already done in step 2)
   
   # Location 2: Encrypted USB drive in a safe
   # If you don't have a second USB drive, create a VeraCrypt container
   # on the same USB with a separate partition, or use an encrypted cloud backup
   
   # Option: Store copy on encrypted Nextcloud / Proton Drive
   # WARNING: Only if you trust the provider
   # cp /mnt/backup_usb/luks_root_header_*.bin /tmp/header_for_cloud.bin
   # Then manually upload to encrypted cloud storage (don't automate this)
   ```

5. **Document backup location** (3 min):
   ```bash
   # Add to Bitwarden or offline notes
   # LUKS Header Backup Locations:
   # - Primary: /mnt/backup_usb/ (at office)
   # - Secondary: Encrypted USB in safe at home
   # - Regenerate backup after any keyslot change (password rotation, etc.)
   ```

6. **Unmount backup USB** (1 min):
   ```bash
   sudo umount /mnt/backup_usb
   ```

7. **Set calendar reminder for quarterly verification** (1 min):
   ```bash
   # Test header restore at least quarterly
   # Add to calendar: "Verify LUKS header backup (quarterly)"
   # Method: Repeat steps 3A-3B above quarterly
   ```

**Dependencies**: Section 1B (recovery key setup)  
**Rollback**: Header backups are read-only; no rollback needed  
**Time**: 30 minutes total

**Next step**: Section 2 (Encrypted Backups)

---

## Section 2: Encrypted Backups (restic + rclone)

### 2A: Account Setup (Proton Drive + rclone) (45 min)

**Scenario**: Set up cloud storage for encrypted backups using Proton Drive and rclone.

**Prerequisites**:
- Proton Mail account (create at https://protonmail.com if you don't have one)
- Ubuntu 24.04 with root access
- Internet connection

**Procedure**:

1. **Create Proton Mail account (if needed)** (5 min):
   - Go to https://protonmail.com
   - Click "Create free account"
   - Choose username (e.g., myemail@protonmail.com)
   - Set password (strong, 30+ characters)
   - Verify recovery email + phone (optional but recommended)
   - Click "Create account"

2. **Log into Proton Drive via web browser** (5 min):
   - Go to https://drive.proton.me
   - Log in with Proton Mail credentials
   - This generates encryption keys that rclone will need

3. **Install rclone** (5 min):
   ```bash
   sudo apt update && sudo apt install rclone
   
   # Verify installation
   rclone version
   # Output should show: rclone v1.66+ (adjust version as needed)
   ```

4. **Configure rclone for Proton Drive** (15 min):
   ```bash
   rclone config
   # Output:
   # Current remotes:
   # 
   # e) Edit existing remote
   # n) New remote
   # d) Delete remote
   # r) Rename remote
   # c) Copy remote
   # s) Set password/token
   # a) Add a new remote
   # l) List remotes
   # q) Quit config
   # e/n/d/r/c/s/a/l/q> a
   
   # When prompted "name> " → type: proton_drive
   # When prompted "Type of storage> " → search for "protondrive" (or type 18)
   # When prompted "Proton Mail email> " → type: myemail@protonmail.com
   # When prompted "Proton Mail password> " → type: your_proton_password
   # When prompted "Confirm password> " → type: your_proton_password
   # When prompted "Do you want to use a server-side copy> " → y
   # When prompted "Edit advanced config> " → n
   # When prompted "Keep this 'proton_drive' remote> " → y
   # When prompted "Save config> " → y
   # When prompted "q) Quit config> " → q
   ```

5. **Test rclone connection** (5 min):
   ```bash
   rclone ls proton_drive:
   # Should list your Proton Drive contents without error
   # If error: "unauthorized", verify you logged into web Proton Drive first
   ```

6. **Create backup directory in Proton Drive** (5 min):
   ```bash
   rclone mkdir proton_drive:restic-backups
   
   # Verify directory was created
   rclone ls proton_drive: | grep restic
   ```

**Dependencies**: None  
**Rollback**: `rclone config delete proton_drive` to remove configuration  
**Time**: 45 minutes total

**Next step**: Section 2B (restic initialization)

---

### 2B: Initialize restic Repository (30 min)

**Scenario**: Create restic backup repository on Proton Drive.

**Prerequisites**:
- Section 2A (rclone configured)
- Internet connection

**Procedure**:

1. **Create restic repository** (2 min):
   ```bash
   RESTIC_REPOSITORY=rclone:proton_drive:restic-backups restic init
   # Output:
   # created restic backend at rclone:proton_drive:restic-backups
   # Please note that knowledge of your password is required to access the repository.
   # Losing your password means that your data is irrecoverably lost.
   ```

2. **You will be prompted for a repository password** (1 min):
   ```bash
   # Enter password (different from Proton password):
   # Password: [Type a strong, unique password, 30+ characters]
   # Confirm password: [Repeat password]
   ```

3. **Store repository password securely** (5 min):
   ```bash
   # Open Bitwarden and create new entry
   # Title: "Restic Repository Password"
   # Username: proton_drive:restic-backups
   # Password: [paste your repository password]
   # Notes: "Decrypt all restic backups. Store separately from LUKS passphrase."
   
   # Save in Bitwarden
   ```

4. **Create password file for automated backups** (5 min):
   ```bash
   # Store password in a file (readable by root only)
   sudo bash -c 'echo "YOUR_REPOSITORY_PASSWORD" > /root/.restic_password'
   sudo chmod 600 /root/.restic_password
   
   # Verify permissions
   ls -la /root/.restic_password
   # Output: -rw------- 1 root root 50 Jun 24 10:35 /root/.restic_password
   
   # WARNING: This file is critical; if someone gains root access, they can read it
   # That's why restic encryption (AES-256) is essential; plaintext password file + LUKS encryption = defense in depth
   ```

5. **Test restic connection** (5 min):
   ```bash
   RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
   RESTIC_PASSWORD_FILE=/root/.restic_password \
   restic snapshots
   # Output: No snapshots found in repository
   # (This is expected; no backups yet)
   ```

6. **Create exclude file for backups** (5 min):
   ```bash
   # Create file to exclude cache, temp files, etc.
   sudo tee /etc/restic_excludes.txt > /dev/null << 'EOF'
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
   *.swo
   
   # System snapshots
   /dev/
   /proc/
   /sys/
   /run/
   /mnt/
   /media/
   
   # Large files not needed
   node_modules/
   .git/objects/
   .terraform/
   venv/
   
   # Application-specific
   .docker/
   Trash/
   .Trash/
   EOF
   
   # Verify
   cat /etc/restic_excludes.txt
   ```

7. **Run first manual backup** (3 min):
   ```bash
   RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
   RESTIC_PASSWORD_FILE=/root/.restic_password \
   restic backup /home /etc /root --exclude-file=/etc/restic_excludes.txt
   # This will take several minutes depending on data size
   # Output: [progress bar] X files, Y GiB processed
   ```

8. **Verify backup completed** (2 min):
   ```bash
   RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
   RESTIC_PASSWORD_FILE=/root/.restic_password \
   restic snapshots
   # Output:
   # ID        Time                 Host        Tags  Paths
   # abc1234   2026-06-24 11:00:00  myhost            /home /etc /root
   ```

**Dependencies**: Section 2A (rclone configured)  
**Rollback**: `rclone purge proton_drive:restic-backups` to delete repository (destructive!)  
**Time**: 30 minutes (plus time for first backup, depends on data size)

**Next step**: Section 2C (Systemd automation)

---

### 2C: Automate Backups with Systemd (1 hour)

**Scenario**: Schedule daily backups automatically without manual intervention.

**Prerequisites**:
- Section 2B (restic repository initialized)
- /root/.restic_password file created

**Procedure**:

1. **Create systemd service file** (5 min):
   ```bash
   sudo tee /etc/systemd/system/restic-backup.service > /dev/null << 'EOF'
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
   
   # Forget old snapshots (keep daily 7, weekly 4, monthly 12, yearly 2)
   ExecStartPost=/usr/bin/restic forget \
     --keep-daily 7 \
     --keep-weekly 4 \
     --keep-monthly 12 \
     --keep-yearly 2 \
     --prune
   
   StandardOutput=journal
   StandardError=journal
   EOF
   
   # Verify file was created
   cat /etc/systemd/system/restic-backup.service
   ```

2. **Create systemd timer** (3 min):
   ```bash
   sudo tee /etc/systemd/system/restic-backup.timer > /dev/null << 'EOF'
   [Unit]
   Description=Daily Restic Backup Timer
   Requires=restic-backup.service
   
   [Timer]
   OnCalendar=daily
   OnCalendar=*-*-* 03:00:00
   Persistent=true
   
   [Install]
   WantedBy=timers.target
   EOF
   
   # Verify
   cat /etc/systemd/system/restic-backup.timer
   ```

3. **Create monthly integrity check service** (5 min):
   ```bash
   sudo tee /etc/systemd/system/restic-check.service > /dev/null << 'EOF'
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
   EOF
   ```

4. **Create monthly check timer** (3 min):
   ```bash
   sudo tee /etc/systemd/system/restic-check.timer > /dev/null << 'EOF'
   [Unit]
   Description=Monthly Restic Check Timer
   
   [Timer]
   OnCalendar=Sun *-*-1..7 04:00:00
   Persistent=true
   
   [Install]
   WantedBy=timers.target
   EOF
   ```

5. **Enable and start timers** (3 min):
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable restic-backup.timer
   sudo systemctl enable restic-check.timer
   sudo systemctl start restic-backup.timer
   sudo systemctl start restic-check.timer
   
   # Verify timers are active
   sudo systemctl list-timers restic-*
   # Output should show next activation time for both timers
   ```

6. **Test backup execution (trigger manually)** (10 min):
   ```bash
   # Manually start backup (for testing)
   sudo systemctl start restic-backup.service
   
   # Watch progress in real-time
   sudo journalctl -u restic-backup.service -f
   # Wait for "[progress bar] finished" message
   
   # After completion, verify snapshots
   RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
   RESTIC_PASSWORD_FILE=/root/.restic_password \
   restic snapshots
   ```

7. **Set up backup failure alerts (optional)** (10 min):
   ```bash
   # Install mail support (for system alerts)
   sudo apt install mailutils
   
   # Add to /etc/systemd/system/restic-backup.service:
   # OnFailure=status-mail-user@%n.service
   # This sends email to root@localhost if backup fails
   
   # Or use systemd-journal-remote to forward logs to a remote syslog server
   ```

8. **Document backup location and retention policy** (5 min):
   ```bash
   # Add to Bitwarden or ~/BACKUP_NOTES.txt
   # Restic Backup Configuration
   # - Repository: rclone:proton_drive:restic-backups
   # - Schedule: Daily at 03:00 AM UTC
   # - Retention: Daily (7 days), Weekly (4 weeks), Monthly (12 months), Yearly (2 years)
   # - Excluded: Caches, temp files, system directories, large build artifacts
   # - Check: Monthly (first Sunday 04:00 AM UTC)
   ```

**Dependencies**: Section 2B (restic initialized)  
**Rollback**: `sudo systemctl disable restic-backup.timer restic-check.timer` to stop automation  
**Time**: 1 hour total

**Next step**: Section 2D (Offline USB backup)

---

### 2D: Offline USB Backup (1 hour)

**Scenario**: Create monthly encrypted USB backup for disaster recovery (cold storage).

**Prerequisites**:
- External USB drive (minimum 100 GB)
- Section 2C (systemd automation set up)

**Procedure**:

1. **Prepare encrypted USB drive** (20 min):
   ```bash
   # Identify USB device
   lsblk
   # Example: /dev/sdb (100GB external drive)
   
   # WARNING: This will erase the USB drive
   # Double-check you're formatting the correct device
   
   # Partition USB with GPT
   sudo parted /dev/sdb mklabel gpt
   sudo parted /dev/sdb mkpart primary ext4 1MB 100GB
   
   # Encrypt partition with LUKS2
   sudo cryptsetup luksFormat --type luks2 --cipher aes-xts-plain64 \
     --key-size 512 /dev/sdb1
   # Prompted: "Are you sure? (Type uppercase yes)" → YES
   # Prompted: "Enter passphrase:" → [Use a strong passphrase, different from LUKS boot passphrase]
   # Prompted: "Verify passphrase:" → [Repeat]
   
   # Open encrypted volume
   sudo cryptsetup luksOpen /dev/sdb1 backup_usb
   
   # Create filesystem
   sudo mkfs.ext4 /dev/mapper/backup_usb
   
   # Mount
   mkdir -p /mnt/backup_usb
   sudo mount /dev/mapper/backup_usb /mnt/backup_usb
   
   # Verify
   df -h /mnt/backup_usb
   ```

2. **Store USB passphrase** (2 min):
   ```bash
   # Add to Bitwarden
   # Title: "Offline USB Backup Passphrase"
   # Password: [your USB encryption passphrase]
   # Notes: "Decrypt external USB for cold storage backups. Keep separate from LUKS boot passphrase."
   ```

3. **Create restic repository on USB** (5 min):
   ```bash
   RESTIC_REPOSITORY=/mnt/backup_usb/restic-offline restic init
   # Prompted: "Password:" → [Use same password as cloud backup, or different; up to you]
   # Prompted: "Confirm password:" → [Repeat]
   
   # Verify
   ls -la /mnt/backup_usb/restic-offline/
   ```

4. **Create monthly backup script** (5 min):
   ```bash
   sudo tee /usr/local/bin/backup_to_usb.sh > /dev/null << 'EOF'
   #!/bin/bash
   set -e
   
   BACKUP_USB="/mnt/backup_usb"
   REPO_PATH="$BACKUP_USB/restic-offline"
   RESTIC_REPO_PASSWORD="YOUR_RESTIC_PASSWORD"  # Same as cloud backup
   
   echo "=== Offline USB Backup ===" 
   
   # Check if USB is mounted
   if ! mountpoint -q "$BACKUP_USB"; then
     echo "Error: USB not mounted at $BACKUP_USB"
     echo "To mount: sudo cryptsetup luksOpen /dev/sdb1 backup_usb && sudo mount /dev/mapper/backup_usb $BACKUP_USB"
     exit 1
   fi
   
   # Check free space
   available=$(df "$BACKUP_USB" | awk 'NR==2 {print $4}')
   if [ "$available" -lt 5000000 ]; then  # Less than 5GB free
     echo "Error: Less than 5GB free on USB"
     exit 1
   fi
   
   # Backup to USB
   echo "Starting backup to offline USB..."
   RESTIC_REPOSITORY="$REPO_PATH" \
   RESTIC_PASSWORD="$RESTIC_REPO_PASSWORD" \
   restic backup /home /etc /root --exclude-file=/etc/restic_excludes.txt --verbose
   
   # Verify
   RESTIC_REPOSITORY="$REPO_PATH" \
   RESTIC_PASSWORD="$RESTIC_REPO_PASSWORD" \
   restic check
   
   echo "=== Backup complete ===" 
   echo "USB can now be unmounted and stored safely"
   EOF
   
   sudo chmod +x /usr/local/bin/backup_to_usb.sh
   ```

5. **Create cron job for monthly backup** (3 min):
   ```bash
   # Edit crontab
   sudo crontab -e
   
   # Add this line (run last Sunday of month at 20:00)
   0 20 * * 0 [ $(date +\%d) -gt 21 ] && /usr/local/bin/backup_to_usb.sh
   
   # Save and exit
   ```

6. **Test backup script** (10 min):
   ```bash
   # Manually run the script
   sudo /usr/local/bin/backup_to_usb.sh
   # Watch for "[progress bar] finished" message
   
   # Verify snapshots on USB
   RESTIC_REPOSITORY=/mnt/backup_usb/restic-offline \
   RESTIC_PASSWORD="YOUR_RESTIC_PASSWORD" \
   restic snapshots
   ```

7. **Unmount USB and store safely** (5 min):
   ```bash
   # Unmount
   sudo umount /mnt/backup_usb
   
   # Close encrypted volume
   sudo cryptsetup luksClose backup_usb
   
   # Label USB (optional)
   # Write on label: "Offline Backup USB #1 - June 2026"
   
   # Store in safe or separate physical location
   ```

**Dependencies**: Section 2C (systemd timers set up)  
**Rollback**: USB can be deleted/reformatted  
**Time**: 1 hour total (mostly formatting; actual first backup takes 10-20 min)

**Next step**: Section 3 (Network Security & VPN)

---

## Section 3: Network Security & VPN Setup

### 3A: DNS-over-TLS Configuration (30 min)

**Scenario**: Encrypt DNS queries to prevent ISP surveillance.

**Prerequisites**:
- Ubuntu 24.04 running with systemd-resolved (default)

**Procedure**:

1. **Verify systemd-resolved is running** (2 min):
   ```bash
   sudo systemctl status systemd-resolved
   # Output: active (running)
   
   # Check DNS servers currently configured
   systemd-resolve --status
   ```

2. **Edit systemd-resolved configuration** (5 min):
   ```bash
   sudo nano /etc/systemd/resolved.conf
   
   # Find and modify these lines (uncomment if necessary):
   [Resolve]
   DNS=1.1.1.1#cloudflare-dns.com
   DNSSECValidation=yes
   DNSOverTLS=yes
   FallbackDNS=8.8.8.8#dns.google
   LLMNR=no
   MulticastDNS=no
   
   # Save (Ctrl+X, Y, Enter)
   ```

3. **Explanation of settings** (optional):
   ```
   DNS=1.1.1.1#cloudflare-dns.com     : Cloudflare DoT server + SNI hostname
   DNSSECValidation=yes                : Enable DNSSEC validation
   DNSOverTLS=yes                      : Enforce DNS over TLS (not plain UDP)
   FallbackDNS=8.8.8.8#dns.google      : Google DNS as fallback
   LLMNR=no                            : Disable Local Link Multicast Name Resolution (mDNS alternative)
   MulticastDNS=no                     : Disable mDNS (local network only)
   ```

4. **Restart systemd-resolved** (2 min):
   ```bash
   sudo systemctl restart systemd-resolved
   
   # Verify it restarted successfully
   sudo systemctl status systemd-resolved
   ```

5. **Verify DoT is active** (5 min):
   ```bash
   systemd-resolve --status
   # Look for:
   # DNSSEC setting: yes
   # DNS over TLS (DoT): yes
   
   # Test DNS resolution
   systemd-resolve www.google.com
   # Should resolve without error
   
   # Verify DNS queries are encrypted (monitor with tcpdump)
   # You should see port 853 (DoT) traffic, not port 53 (plaintext DNS)
   sudo tcpdump -ni any 'port 853'
   # Ctrl+C to stop
   ```

6. **Test DNS leak** (5 min):
   ```bash
   # Optional: Test if DNS queries are actually encrypted
   # Using dnsleaktest tool or curl
   curl -s https://1.1.1.1/dns-query?name=whoami.akamai.net | jq .
   # Should return Cloudflare's resolver IP, not your ISP's
   ```

7. **Optional: Alternative DNS providers** (5 min):
   ```bash
   # Other DoT providers you can use:
   # Quad9 (9.9.9.9#dns.quad9.net)
   # Mullvad DNS (if on Mullvad VPN: 10.64.0.1)
   # NextDNS (123.45.67.89#abc123.nextdns.io)
   
   # To switch providers, edit /etc/systemd/resolved.conf and restart
   ```

**Dependencies**: None (systemd-resolved is built-in)  
**Rollback**: Revert /etc/systemd/resolved.conf to original and restart  
**Time**: 30 minutes total

**Next step**: Section 3B (UFW firewall + VPN kill-switch)

---

### 3B: UFW Firewall with VPN Kill-Switch (1-2 hours)

**Scenario**: Configure firewall to allow traffic only through VPN tunnel, preventing leaks if VPN disconnects.

**Prerequisites**:
- UFW installed (default on Ubuntu)
- VPN client will be installed in Section 4A

**Procedure**:

1. **Enable UFW** (2 min):
   ```bash
   sudo ufw enable
   
   # Verify it's enabled
   sudo ufw status
   # Output: Status: active
   ```

2. **Set default policies (deny all)** (3 min):
   ```bash
   # Most restrictive: deny all by default, then allow what you need
   sudo ufw default deny outgoing
   sudo ufw default deny incoming
   sudo ufw default deny routed
   
   # Verify
   sudo ufw status numbered
   ```

3. **Allow SSH (so you don't lock yourself out)** (2 min):
   ```bash
   sudo ufw allow ssh
   # Or more specific:
   sudo ufw allow in from 192.168.1.0/24 to any port 22
   ```

4. **Allow local traffic** (2 min):
   ```bash
   # Allow loopback interface (localhost communication, systemd-resolved)
   sudo ufw allow in on lo from 127.0.0.1 to 127.0.0.1
   sudo ufw allow out on lo from 127.0.0.1 to 127.0.0.1
   ```

5. **Allow local LAN (if on home network)** (2 min):
   ```bash
   # Allow your home network (adjust IP range as needed)
   sudo ufw allow from 192.168.1.0/24 to any port any
   
   # Or restrict to specific services
   sudo ufw allow from 192.168.1.100 to any port 22  # SSH from specific device
   ```

6. **Prepare for VPN kill-switch** (5 min):
   ```bash
   # After VPN client is installed, we'll identify the tunnel interface (tun0 or wg0)
   # For now, plan the rules:
   # - Allow ALL traffic on VPN tunnel interface only
   # - Block all outbound traffic except to VPN server + VPN tunnel
   # - Block UDP/TCP port 53 (DNS) except on VPN tunnel
   ```

7. **Verify current rule set** (2 min):
   ```bash
   sudo ufw status verbose
   # Output should show allow rules for SSH and local, deny for everything else
   ```

8. **Test firewall (carefully)** (5 min):
   ```bash
   # You should still have internet access through VPN (which you haven't installed yet)
   # For now, verify SSH still works
   ssh localhost
   # Should connect; exit with Ctrl+D
   
   # Verify outbound traffic is blocked (for non-VPN)
   timeout 3 curl https://google.com
   # Should timeout (connection refused, no internet yet)
   ```

**Dependencies**: None  
**Rollback**: `sudo ufw disable` to turn off firewall  
**Time**: 1 hour (mostly planning; actual configuration takes 10 minutes)

**Next step**: Section 4A (VPN Installation)

---

### 3C: UFW Rules for VPN Kill-Switch (After VPN Install) (30 min)

**Scenario**: After VPN is installed, add firewall rules to only allow traffic through VPN tunnel.

**Prerequisites**:
- Section 3B (UFW enabled and configured)
- Section 4A (VPN client installed and working)

**Procedure** (Execute this after Section 4A):

1. **Identify VPN tunnel interface** (2 min):
   ```bash
   # Start VPN
   mullvad connect us
   # or: sudo systemctl start openvpn@client
   
   # Identify tunnel interface
   ip link show
   # Look for: tun0 (OpenVPN) or wg0 (WireGuard) or mullvad0 (Mullvad native)
   # Example: 3: tun0: <POINTOPOINT,NOTRAILERS,UP,LOWER_UP> mtu 1500
   ```

2. **Allow traffic on VPN tunnel interface** (3 min):
   ```bash
   # Replace tun0 with your actual interface (wg0 for WireGuard, etc.)
   sudo ufw allow in on tun0 from any to any
   sudo ufw allow out on tun0 from any to any
   ```

3. **Prevent DNS leaks** (3 min):
   ```bash
   # Block DNS (UDP/TCP 53) to anywhere except VPN tunnel
   sudo ufw deny out to any port 53
   sudo ufw allow out on tun0 to any port 53
   
   # Alternative: Block DNS entirely except to local resolver (which uses DoT)
   sudo ufw allow out to 127.0.0.1 port 53
   sudo ufw allow out on tun0 to any port 53
   ```

4. **Allow connection to VPN server itself** (3 min):
   ```bash
   # Get VPN server IP (example: Mullvad gateway)
   # Mullvad public addresses: https://api.mullvad.net/public/relays/wireguard/
   # Example: nl-ams-wg-401.mullvad.net resolves to 209.250.35.198
   
   # Add to /etc/hosts to avoid DNS lookup
   echo "209.250.35.198  nl-ams-wg-401.mullvad.net" | sudo tee -a /etc/hosts
   
   # Allow outbound to VPN server
   sudo ufw allow out to 209.250.35.198
   # Or, more specific:
   sudo ufw allow out to 209.250.35.198 port 1194  # OpenVPN
   sudo ufw allow out to 209.250.35.198 port 51820  # WireGuard
   ```

5. **Optional: Disable IPv6 (if VPN is IPv4-only)** (3 min):
   ```bash
   # Prevent IPv6 leaks (traffic that bypasses VPN)
   echo "net.ipv6.conf.all.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
   echo "net.ipv6.conf.default.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
   sudo sysctl -p
   
   # Verify
   cat /proc/sys/net/ipv6/conf/all/disable_ipv6
   # Should output: 1
   ```

6. **Verify final rule set** (5 min):
   ```bash
   sudo ufw status verbose
   # Should show:
   # - Allow SSH from local network
   # - Allow all traffic on tun0 interface
   # - Block all other outbound
   # - Allow specific VPN server IP
   ```

7. **Test kill-switch** (5 min):
   ```bash
   # Verify you're connected to VPN
   curl https://api.ipify.org
   # Should return a VPN IP (e.g., 209.250.35.198), not your home ISP IP
   
   # Kill VPN connection (simulate disconnect)
   sudo kill $(pgrep -f "mullvad-daemon")
   # or: sudo systemctl stop openvpn@client
   
   # Try to access external resource
   timeout 5 curl https://google.com
   # Should HANG and timeout (not reach external host)
   # This proves kill-switch is working!
   
   # Reconnect VPN
   mullvad connect us
   # or: sudo systemctl start openvpn@client
   
   # Verify you're back online
   curl https://api.ipify.org
   # Should return VPN IP again
   ```

**Dependencies**: Sections 3B and 4A  
**Rollback**: `sudo ufw reset` to clear all rules  
**Time**: 30 minutes

**Next step**: Section 4A (VPN Installation)

---

## Section 4: VPN and Tor Browser

### 4A: VPN Installation (Mullvad or ProtonVPN) (45 min)

**Scenario**: Install and configure Mullvad VPN for encrypted internet access.

**Prerequisites**:
- Ubuntu 24.04 with root access
- Internet connection

**Procedure for Mullvad**:

1. **Add Mullvad repository** (5 min):
   ```bash
   # Download and add signing key
   curl https://repository.mullvad.net/deb/mullvad-keyring.asc | sudo apt-key add -
   
   # Add repository
   echo "deb [arch=amd64] https://repository.mullvad.net/deb/stable main" \
     | sudo tee /etc/apt/sources.list.d/mullvad.list
   
   # Update package list
   sudo apt update
   ```

2. **Install Mullvad** (5 min):
   ```bash
   sudo apt install mullvad-vpn
   
   # Verify installation
   mullvad version
   ```

3. **Start Mullvad daemon** (2 min):
   ```bash
   sudo systemctl enable mullvad-daemon
   sudo systemctl start mullvad-daemon
   
   # Verify it's running
   sudo systemctl status mullvad-daemon
   ```

4. **Connect to VPN** (2 min):
   ```bash
   # Connect to auto-selected server
   mullvad connect
   
   # Or connect to specific country/city
   mullvad connect us-west
   mullvad list locations  # See available options
   
   # Verify you're connected
   mullvad status
   # Output: Tunnel state: Connected
   ```

5. **Verify VPN IP** (2 min):
   ```bash
   # Check your public IP
   curl https://api.ipify.org
   # Should return a VPN IP (not your home ISP IP)
   
   # Verify DNS is also through VPN (optional)
   curl -s https://api.mullvad.net/ip | jq .
   # Should show DNS resolver = Mullvad's
   ```

6. **Enable "Always On" VPN** (3 min):
   ```bash
   # This makes Mullvad auto-reconnect if disconnected
   mullvad always-on set true
   
   # Verify
   mullvad settings list
   ```

7. **Configure additional privacy settings** (5 min):
   ```bash
   # Disable IPv6 (prevent leaks)
   mullvad ipv6 set off
   
   # Enable local network access (if needed for LAN devices)
   mullvad local-network-sharing set off  # Most secure
   
   # Use multihop (two VPN servers)
   mullvad tunnel set wireguard multihop true
   
   # Verify settings
   mullvad settings list
   ```

8. **Set up automatic reconnection** (3 min):
   ```bash
   # Mullvad will automatically reconnect on daemon start
   # To test:
   sudo systemctl restart mullvad-daemon
   sleep 5
   mullvad status
   # Should still be connected
   ```

9. **Optional: Configure via GUI** (if you prefer):
   ```bash
   # Launch Mullvad GUI application
   mullvad-gui &
   # Or from application menu
   ```

10. **Document VPN configuration** (5 min):
    ```bash
    # Store in Bitwarden
    # Title: "Mullvad VPN Configuration"
    # Notes: "Auto-connected via systemd. Kill-switch enabled via UFW firewall. IPv6 disabled. Multihop enabled."
    ```

**Procedure for ProtonVPN** (if preferred):

```bash
# Add ProtonVPN repository
wget https://repo3.protonvpn.com/debian/dists/focal/main/binary-amd64/protonvpn-stable-release_1.0.3~focal_all.deb
sudo apt install ./protonvpn-stable-release_1.0.3~focal_all.deb

# Install
sudo apt update && sudo apt install protonvpn

# Login
protonvpn login

# Connect
protonvpn connect us

# Verify
protonvpn status
```

**Dependencies**: None  
**Rollback**: `sudo systemctl disable mullvad-daemon` and `sudo apt remove mullvad-vpn`  
**Time**: 45 minutes total

**Next step**: Section 3C (UFW rules for VPN kill-switch) or Section 4B (Tor Browser)

---

### 4B: Tor Browser Installation and Hardening (30 min)

**Scenario**: Install Tor Browser for high-sensitivity research and communications.

**Prerequisites**:
- Ubuntu 24.04 with desktop environment (GNOME, KDE, etc.)
- Internet connection

**Procedure**:

1. **Download Tor Browser from official source** (5 min):
   ```bash
   cd ~/Downloads
   
   # Download Tor Browser
   wget https://www.torproject.org/dist/torbrowser/13.5/tor-browser-linux64-13.5.tar.xz
   
   # Download signature file for verification
   wget https://www.torproject.org/dist/torbrowser/13.5/tor-browser-linux64-13.5.tar.xz.asc
   
   # Verify signature (requires gpg)
   gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org
   gpg --verify tor-browser-linux64-13.5.tar.xz.asc tor-browser-linux64-13.5.tar.xz
   # Should output: Good signature from "The Tor Project <torbrowser@torproject.org>"
   
   # If signature fails, DO NOT proceed (potential compromised download)
   ```

2. **Extract and install Tor Browser** (3 min):
   ```bash
   tar xf tor-browser-linux64-13.5.tar.xz
   
   # Move to standard location
   mv tor-browser /opt/
   
   # Create symlink for easy launch
   sudo ln -s /opt/tor-browser/start-tor-browser.desktop /usr/share/applications/
   
   # Make executable
   chmod +x /opt/tor-browser/start-tor-browser.desktop
   ```

3. **Launch Tor Browser** (3 min):
   ```bash
   /opt/tor-browser/start-tor-browser.desktop &
   
   # Or from application menu: Activities → Tor Browser
   # Wait for Tor to connect (may take 30-60 seconds on first launch)
   ```

4. **Configure security level** (5 min):
   ```
   1. Click Shield icon (top-left corner)
   2. Click "Advanced Security Settings" (or "Settings...")
   3. Under "Security Level", select one of:
      - Standard (default): Not recommended, JavaScript enabled
      - Safer (recommended): Disables JavaScript on HTTP sites, good compatibility
      - Safest (recommended for high-risk): Disables JavaScript everywhere, limited site compatibility
   4. Click to confirm selection
   5. Restart Tor Browser for settings to take effect
   ```

5. **Test Tor connection** (5 min):
   ```bash
   # Go to https://check.torproject.org
   # Should display: "Congratulations! Your browser is configured to use Tor."
   
   # Verify Tor exit node changes
   # Reload page; you should see a different exit node IP
   ```

6. **Harden browser settings** (5 min):
   ```
   Menu (≡) → Preferences:
   
   Under "Privacy & Security":
   - Disable all cookies (or set to "Reject non-necessary")
   - Disable autofill (passwords, forms)
   - Do NOT enable "Remember passwords"
   - Enable "Enhanced Tracking Protection" (always on)
   
   Under "Browsing":
   - DISABLE "Autoscroll"
   - DISABLE "Smooth scrolling"
   
   Under "Search":
   - Set search engine to DuckDuckGo (or Searx)
   
   DO NOT install additional extensions (breaks fingerprinting protection)
   ```

7. **Testing and verification** (5 min):
   ```bash
   # Test various fingerprinting defenses
   
   # 1. Visit https://browserleaks.com/webrtc
   # Should show: "All your IP addresses are hidden"
   
   # 2. Visit https://www.eff.org/deeplinks/2010/01/primer-information-theory-and-privacy
   # Check for: Canvas fingerprinting blocked, WebGL blocked
   
   # 3. Visit https://panopticlick.eff.org
   # Your browser fingerprint should be unique (due to letterboxing randomization)
   ```

8. **Document Tor Browser usage** (2 min):
   ```bash
   # Add to Bitwarden notes
   # Tor Browser Configuration:
   # - Security level: Safer (or Safest for high-risk)
   # - No extensions installed
   # - Use for: Sensitive research, financial accounts, health portals
   # - Do NOT use for routine browsing (privacy loss when mixing Tor + non-Tor sessions)
   # - Restart browser after security level change (bug in 13.0-13.5)
   ```

**Dependencies**: None  
**Rollback**: `rm -rf /opt/tor-browser` to uninstall  
**Time**: 30 minutes total

**Next step**: Section 5 (Testing & Verification)

---

## Section 5: Testing and Verification

### 5A: Backup Recovery Test (1-2 hours)

**Scenario**: Verify that you can actually restore data from restic backups.

**Prerequisites**:
- Section 2 (backups configured and running)
- Temporary 50 GB free space for test restore

**Procedure**:

1. **Create test file and backup** (5 min):
   ```bash
   # Create a test file with unique content
   echo "This is a test file created on $(date)" > /tmp/test_restore.txt
   
   # Force a backup run (so test file is captured)
   sudo systemctl start restic-backup.service
   
   # Wait for backup to complete
   sudo journalctl -u restic-backup.service -f
   # Until you see: "[progress bar] finished"
   ```

2. **List backup snapshots** (2 min):
   ```bash
   RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
   RESTIC_PASSWORD_FILE=/root/.restic_password \
   restic snapshots
   
   # Example output:
   # ID        Time                 Host        Tags  Paths
   # abc1234   2026-06-24 11:00:00  myhost            /home /etc /root
   # def5678   2026-06-24 12:00:00  myhost            /home /etc /root
   ```

3. **Restore specific file to test directory** (5 min):
   ```bash
   # Restore most recent snapshot to /tmp/restore_test
   RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
   RESTIC_PASSWORD_FILE=/root/.restic_password \
   restic restore latest --target /tmp/restore_test
   
   # Verify test file is in restored data
   cat /tmp/restore_test/tmp/test_restore.txt
   # Should output: "This is a test file created on [date]"
   ```

4. **Test file integrity** (5 min):
   ```bash
   # Verify a few random files from restore
   ls -la /tmp/restore_test/home/
   cat /tmp/restore_test/etc/hostname
   
   # Check that file sizes and permissions are preserved
   # Example: Compare original and restored /etc/hostname
   diff /etc/hostname /tmp/restore_test/etc/hostname
   # Should output nothing (files are identical)
   ```

5. **Run integrity check on repository** (10 min):
   ```bash
   # Verify that backups are not corrupted
   RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
   RESTIC_PASSWORD_FILE=/root/.restic_password \
   restic check --verbose
   # Should complete without errors
   # Output: "All packs are valid, all files are complete, no errors"
   ```

6. **Clean up test restore** (2 min):
   ```bash
   # Delete test restore
   sudo rm -rf /tmp/restore_test
   sudo rm /tmp/test_restore.txt
   ```

7. **Document test results** (2 min):
   ```bash
   # Add to ~/BACKUP_TEST_LOG.txt
   # Date: June 24, 2026
   # Test: Restore latest snapshot to /tmp/restore_test
   # Result: PASS (test file recovered, integrity check passed)
   # Next test date: July 24, 2026 (monthly)
   ```

**Dependencies**: Section 2 (backups running)  
**Rollback**: None needed (test restore is non-destructive)  
**Time**: 1-2 hours (mostly waiting for restore)

**Next step**: Section 5B (LUKS Recovery Test)

---

### 5B: LUKS Recovery Key Test (30 min)

**Scenario**: Verify that you can unlock your encrypted disk using the recovery key (in case you forget your passphrase).

**Prerequisites**:
- Section 1B (recovery key created and stored)
- Ubuntu live USB (for safe testing)

**Procedure** (TEST IN A VIRTUAL MACHINE FIRST):

1. **Create a test LUKS volume** (on test VM, not production):
   ```bash
   # On a test VM, create a LUKS2 volume for testing
   # (Do NOT do this on your real encrypted drive)
   
   sudo dd if=/dev/zero of=/tmp/test.img bs=1M count=100
   sudo losetup /dev/loop0 /tmp/test.img
   
   # Create LUKS volume
   sudo cryptsetup luksFormat --type luks2 /dev/loop0
   # Prompted: "Is this OK? (Type uppercase yes)" → YES
   # Prompted: "Enter passphrase:" → testpass123
   # Prompted: "Verify passphrase:" → testpass123
   ```

2. **Add recovery key to test volume** (3 min):
   ```bash
   # Generate recovery key
   openssl rand -base64 192 > /tmp/test_recovery.txt
   
   # Add to test LUKS volume
   sudo cryptsetup luksAddKey /dev/loop0 --key-slot 1 --keyfile /tmp/test_recovery.txt
   # Prompted: "Enter any existing passphrase:" → testpass123
   ```

3. **Test recovery key unlock** (5 min):
   ```bash
   # Simulate forgetting passphrase by trying to unlock with recovery key only
   sudo cryptsetup luksClose /dev/mapper/test_crypt 2>/dev/null || true
   
   # Unlock using recovery key (not passphrase)
   sudo cryptsetup luksOpen --key-file /tmp/test_recovery.txt /dev/loop0 test_crypt
   
   # If successful, you can mount and access the volume
   sudo mkfs.ext4 /dev/mapper/test_crypt
   mkdir -p /tmp/test_mnt
   sudo mount /dev/mapper/test_crypt /tmp/test_mnt
   
   # Verify you can write and read files
   echo "Recovery key works!" | sudo tee /tmp/test_mnt/test.txt
   cat /tmp/test_mnt/test.txt
   # Should output: "Recovery key works!"
   ```

4. **Clean up test volume** (3 min):
   ```bash
   sudo umount /tmp/test_mnt
   sudo cryptsetup luksClose test_crypt
   sudo losetup -d /dev/loop0
   rm /tmp/test.img /tmp/test_recovery.txt
   ```

5. **Test on production drive (optional, advanced)** (5 min):
   ```bash
   # This is a NON-DESTRUCTIVE test on your real encrypted drive
   # It does NOT unlock the drive or access your data
   
   # Just verify that the recovery key can be used as a valid keyslot
   RESTIC_REPOSITORY=rclone:proton_drive:restic-backups \
   RESTIC_PASSWORD_FILE=/root/.restic_password \
   sudo cryptsetup luksDump /dev/nvme0n1p3 | grep "Keyslot 1"
   # Should show: Keyslot 1: ENABLED (valid)
   ```

6. **Document recovery key verification** (2 min):
   ```bash
   # Add to ~/LUKS_RECOVERY_LOG.txt
   # Date: June 24, 2026
   # Test: Created test LUKS volume, added recovery key, verified unlock
   # Result: PASS (recovery key successfully unlocked test volume)
   # Next test: Quarterly (set calendar reminder)
   ```

**Dependencies**: Section 1B (recovery key created)  
**Rollback**: None (test volume is temporary)  
**Time**: 30 minutes

**Next step**: Section 5C (VPN Kill-Switch Test)

---

### 5C: VPN Kill-Switch Test (15 min)

**Scenario**: Verify that your firewall kill-switch actually blocks traffic when VPN disconnects.

**Prerequisites**:
- Section 3B (UFW configured)
- Section 3C (VPN kill-switch rules added)
- Section 4A (VPN installed)

**Procedure**:

1. **Connect to VPN** (2 min):
   ```bash
   # Start VPN
   mullvad connect us
   
   # Verify you're connected
   mullvad status
   # Output: Tunnel state: Connected
   
   # Verify external IP is VPN IP (not home ISP IP)
   curl https://api.ipify.org
   # Example output: 209.250.35.198 (Mullvad IP, not your ISP IP)
   ```

2. **Simulate VPN disconnect** (2 min):
   ```bash
   # Kill VPN process to simulate unexpected disconnect
   sudo kill $(pgrep -f "mullvad-daemon")
   
   # Verify VPN is disconnected
   mullvad status 2>&1
   # Output: error: Could not connect to daemon (expected)
   ```

3. **Test external connectivity (should be blocked)** (5 min):
   ```bash
   # Try to access external website
   timeout 10 curl https://google.com
   # Should HANG and timeout after 10 seconds
   # This proves kill-switch is working!
   
   # Expected output: curl: (28) Operation timeout. [10 seconds elapsed]
   ```

4. **Verify no data leaked** (2 min):
   ```bash
   # Check if you leaked your real IP address
   # If you can access external sites, kill-switch FAILED
   # If timeout occurs, kill-switch is WORKING
   
   # Monitor firewall logs (optional)
   sudo journalctl -u ufw -f
   # You should see DROP rules being triggered
   ```

5. **Reconnect VPN** (2 min):
   ```bash
   # Restart VPN daemon
   sudo systemctl restart mullvad-daemon
   sleep 5
   
   # Verify reconnection
   mullvad status
   # Output: Tunnel state: Connected
   
   # Verify external connectivity is restored
   curl https://api.ipify.org
   # Should return VPN IP
   ```

6. **Document test results** (2 min):
   ```bash
   # Add to ~/VPN_KILLSWITCH_LOG.txt
   # Date: June 24, 2026
   # Test: Disconnected VPN, verified traffic blocked by firewall
   # Result: PASS (timeout on curl = kill-switch working)
   # Next test: Quarterly or after system update
   ```

**Dependencies**: Sections 3B, 3C, 4A  
**Rollback**: None needed (test is non-destructive)  
**Time**: 15 minutes

**Next step**: Section 5D (Final Verification Checklist)

---

### 5D: Final Verification Checklist (30 min)

**Scenario**: Verify all Phase 2 components are working correctly before declaring completion.

**Procedure**:

**LUKS2 Encryption**:
- [ ] Boot system and enter LUKS passphrase at GRUB prompt
- [ ] System boots successfully and loads desktop
- [ ] Run: `sudo cryptsetup luksDump /dev/nvme0n1p3 | head -20` — Verify LUKS version 2
- [ ] Run: `sudo cryptsetup luksDump /dev/nvme0n1p3 | grep Keyslot` — Verify keyslots 0, 1 are enabled
- [ ] Recovery key is stored offline in two locations (encrypted USB + paper in safe)

**Encrypted Backups**:
- [ ] Run: `RESTIC_REPOSITORY=rclone:proton_drive:restic-backups RESTIC_PASSWORD_FILE=/root/.restic_password restic snapshots` — At least 2 snapshots exist
- [ ] Systemd timer is running: `sudo systemctl status restic-backup.timer`
- [ ] Manual backup succeeded: `sudo systemctl start restic-backup.service` (check journal)
- [ ] Restore test passed: Can restore files from snapshot (Section 5A)
- [ ] Offline USB backup completed: USB drive is encrypted and contains restic repository
- [ ] Repository password is stored in Bitwarden

**Network Security**:
- [ ] DNS-over-TLS is active: `systemd-resolve --status | grep "DNS over TLS"`
- [ ] UFW firewall is enabled: `sudo ufw status | grep active`
- [ ] Default policies are deny: `sudo ufw status verbose | head -5`
- [ ] SSH rule is allowed: `sudo ufw status | grep 22`

**VPN + Tor**:
- [ ] VPN is installed and running: `mullvad status`
- [ ] Public IP is VPN IP (not home ISP IP): `curl https://api.ipify.org`
- [ ] Kill-switch test passed: Traffic blocked when VPN disconnected (Section 5C)
- [ ] Tor Browser is installed: `/opt/tor-browser/start-tor-browser.desktop`
- [ ] Tor Browser security level is "Safer" or "Safest"
- [ ] Tor connection test passed: https://check.torproject.org shows "Congratulations!"

**Credentials & Data Management**:
- [ ] Bitwarden (or KeePass) is set up with master password
- [ ] Critical passphrases stored in Bitwarden: LUKS boot, restic repository, USB encryption
- [ ] SSH keys generated and passphrase-protected: `ls -la ~/.ssh/id_ed25519`
- [ ] Recovery codes printed and stored offline

**Documentation**:
- [ ] Recovery procedures documented (LUKS header restore, restic restore, password reset)
- [ ] VPN + Tor configuration documented
- [ ] Backup retention policy documented (daily 7, weekly 4, monthly 12, yearly 2)
- [ ] Calendar reminders set for: quarterly recovery key test, quarterly DNS leak test, monthly backup check

**Final Sign-Off**:
- [ ] All tests in Sections 5A-5C have passed
- [ ] No sensitive data was compromised during testing
- [ ] All critical files are backed up and verified
- [ ] System is production-ready for Phase 2 use

---

## Timeline and Dependencies

**Sequential order (required)**:

1. Section 1A: Linux encryption (fresh install) — **2-4 hours**
2. Section 1B: Recovery key setup — **1-2 hours**
3. Section 1C: Header backup — **30 min**
4. Section 2A: Account setup (Proton Drive) — **45 min**
5. Section 2B: Restic initialization — **30 min**
6. Section 2C: Systemd automation — **1 hour**
7. Section 2D: Offline USB backup — **1 hour**
8. Section 3A: DNS-over-TLS — **30 min**
9. Section 3B: UFW firewall — **1-2 hours**
10. Section 4A: VPN installation — **45 min**
11. Section 3C: UFW + VPN kill-switch rules — **30 min**
12. Section 4B: Tor Browser — **30 min**
13. Section 5A-5D: Testing & verification — **2-3 hours**

**Parallel work possible**:
- Sections 2 (backups) and 4 (VPN/Tor) can run in parallel with Section 1 (encryption)
- Sections 3 (network) and 4 (VPN/Tor) can overlap

**Total estimated time**: 30-40 hours over 3-4 weeks

---

## Troubleshooting

**Backup fails with "error: rclone operation failed"**:
- Verify rclone Proton Drive connection: `rclone ls proton_drive:`
- Verify Proton Drive credentials are correct: `rclone config`
- Check journal: `sudo journalctl -u restic-backup.service -n 50`
- Fallback to Backblaze B2 (Section 2.5)

**VPN kill-switch not working (traffic not blocked when VPN disconnects)**:
- Verify UFW is enabled: `sudo ufw status`
- Verify VPN tunnel interface rules: `sudo ufw status verbose | grep tun0`
- Check if traffic is on different interface (wg0, mullvad0): `ip link show` while VPN connected
- Disable IPv6 globally: `echo "net.ipv6.conf.all.disable_ipv6=1" | sudo tee -a /etc/sysctl.conf && sudo sysctl -p`

**LUKS passphrase not working at boot**:
- Try recovery key unlock from live USB (Section 1B)
- If recovery key also fails: header may be corrupted; restore from header backup (Section 1C)

**Tor Browser sites not loading**:
- Disable "Safest" security level and try "Safer"
- Disable all extensions
- Restart Tor Browser
- Try accessing via HTTP (not HTTPS) on Safer mode (some sites have compatibility issues)

---

## Next Steps After Phase 2 Completion

1. **Schedule recurring tests** (calendar reminders):
   - Monthly: Verify backup completed (`systemctl status restic-backup.timer`)
   - Quarterly: Test recovery key unlock, test VPN kill-switch, test DNS leak

2. **Phase 3 (advanced, optional)**:
   - Hardware security key (YubiKey 5) for 2FA on email and banking
   - Air-gapped machine for signing/encrypting sensitive documents
   - Dedicated Tor/proxy server on home network
   - Hardened router with custom firewall rules

3. **Continuous monitoring**:
   - Monitor systemd journal for backup failures
   - Set up Prometheus + Alertmanager for automated alerts
   - Review VPN logs for unexpected disconnects

---

**End of Phase 2 Provisioning Runbook**
