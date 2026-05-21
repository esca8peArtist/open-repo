---
title: BitLocker Setup Checklist
project: cybersecurity-hardening
phase: 2
created: 2026-05-21
status: production-ready
companion: WINDOWS_ENCRYPTION_TRANSITION_GUIDE.md
---

# BitLocker Setup Checklist

Complete each section in order. Do not skip to encryption before pre-setup verification is done.

---

## Section 1: Pre-Setup Verification

### 1.1 Confirm Windows Edition

- [ ] Open Settings → System → About
- [ ] Under "Windows specifications," confirm Edition is one of:
  - Windows 10/11 Pro
  - Windows 10/11 Enterprise
  - Windows 10/11 Education
  - Windows 10/11 Pro Education/SE
- [ ] If Edition is "Home": proceed to Section 1.5 (Device Encryption path) instead

**PowerShell alternative**:
```powershell
(Get-WmiObject -Class Win32_OperatingSystem).Caption
```

### 1.2 Verify TPM 2.0

Run in elevated PowerShell (right-click PowerShell → Run as Administrator):

```powershell
Get-Tpm
```

- [ ] `TpmPresent` = True
- [ ] `TpmEnabled` = True
- [ ] `TpmReady` = True

Check TPM version:
```powershell
Get-CimInstance -Namespace "Root/CIMv2/Security/MicrosoftTpm" -ClassName Win32_Tpm | Select-Object SpecVersion
```

- [ ] `SpecVersion` begins with `2.0` (preferred) or `1.2` (minimum)
- [ ] If no TPM present: see Section 1.4 (BitLocker without TPM)

### 1.3 Verify UEFI Firmware Mode

Run: `msinfo32.exe`

- [ ] "BIOS Mode" = UEFI (not Legacy)
- [ ] "Secure Boot State" = On
- [ ] "PCR7 Configuration" = Binding Possible (ideal for Device Encryption)

**If "BIOS Mode" = Legacy**:
1. Run `mbr2gpt /validate` in elevated PowerShell to check if conversion is possible
2. If valid: run `mbr2gpt /convert` to convert disk layout
3. Then change BIOS setting from Legacy/CSM to UEFI
4. Do not change BIOS mode before converting the disk — this will prevent Windows from booting

### 1.4 BitLocker Without TPM (Non-TPM Hardware Including Raspberry Pi 5)

BitLocker can run without a TPM using a USB startup key. Requirements:

- [ ] USB drive dedicated for startup key (minimum 1 GB; key file is ~2 KB)
- [ ] BIOS must support reading USB in pre-boot environment (enable "USB Legacy Support" or similar)
- [ ] Enable Group Policy to allow no-TPM BitLocker:
  - Run `gpedit.msc`
  - Navigate: Computer Configuration → Administrative Templates → Windows Components → BitLocker Drive Encryption → Operating System Drives
  - Enable "Require additional authentication at startup"
  - Set "Configure TPM startup" = "Allow BitLocker without a compatible TPM"

**Note**: USB startup key must be present at every boot. The USB is the encryption key. If lost and recovery key is also lost, data is unrecoverable. Store a second copy of the recovery key separately.

### 1.5 Windows Home: Device Encryption Path

Device Encryption uses BitLocker technology with fewer options. Available on Windows Home if hardware qualifies.

- [ ] Run `msinfo32.exe`
- [ ] Find row "Device Encryption Support" — must read "Meets prerequisites"
- [ ] Sign in with Microsoft account (required for automatic key backup)
- [ ] Open Settings → Privacy & Security → Device Encryption
- [ ] Toggle Device Encryption to On
- [ ] Verify encryption completes: Settings → Privacy & Security → Device Encryption → status shows "On"

**Recovery key location for Device Encryption**: [account.microsoft.com/devices/recoverykey](https://account.microsoft.com/devices/recoverykey)

---

## Section 2: Pre-Encryption Backup

Before encrypting, complete all backup steps. Encryption is not a backup.

- [ ] Back up all critical files to an external drive or cloud service
- [ ] Verify backup is readable (open several files from the backup location)
- [ ] If migrating from VeraCrypt: create a VeraCrypt rescue disk ISO before decrypting (VeraCrypt → System → Create Rescue Disk)
- [ ] Note current disk configuration: run `diskpart` → `list disk` → `list volume`
- [ ] Record your BitLocker recovery key storage plan (where will you save it — see Section 4)

---

## Section 3: BitLocker Activation (Pro/Enterprise)

### 3.1 Open BitLocker Management

Option A (Control Panel): Control Panel → System and Security → BitLocker Drive Encryption

Option B (PowerShell, check current status first):
```powershell
manage-bde -status
```

- [ ] Confirm C: drive (OS drive) shows "Protection Status: Protection Off"

### 3.2 Start Encryption Wizard

- [ ] Click "Turn on BitLocker" next to the C: drive
- [ ] If Windows reports a missing system partition: run `BdeHdCfg.exe -target default` in elevated CMD, then retry

### 3.3 Configure Authentication Method

- [ ] If TPM present: wizard detects TPM automatically
- [ ] Recommended — add a PIN for pre-boot authentication:
  - In `gpedit.msc`: Computer Configuration → Administrative Templates → Windows Components → BitLocker Drive Encryption → Operating System Drives
  - Enable "Require additional authentication at startup"
  - Set "Configure TPM startup PIN" = "Require startup PIN with TPM"
  - Return to BitLocker wizard and choose "Enter a PIN"
  - Set a PIN of 6+ characters (alphanumeric if using enhanced PIN policy)

### 3.4 Save Recovery Key

Choose at least two options:

- [ ] Option 1 — Save to Microsoft Account: key stored at account.microsoft.com/devices/recoverykey
- [ ] Option 2 — Save to USB flash drive: insert dedicated USB, save key file
- [ ] Option 3 — Save to file: save .txt file to a second drive, OneDrive, or password manager
- [ ] Option 4 — Print: print the recovery key, store in a secure physical location

**Do not** store the USB recovery key in the same location as the laptop. **Do not** save the recovery key file to the drive being encrypted.

- [ ] Record the 48-digit recovery key ID (first 8 digits shown on screen) for reference

### 3.5 Choose Encryption Scope

- [ ] "Encrypt used disk space only" — faster; use for new drives or drives that have been wiped
- [ ] "Encrypt entire drive" — recommended for drives that previously held unencrypted data (fills free space)
- [ ] For VeraCrypt migration: select "Encrypt entire drive"

### 3.6 Choose Encryption Mode

- [ ] "New encryption mode (XTS-AES)" — for fixed drives on Windows 10/11 (recommended)
- [ ] "Compatible mode" — only if the drive may be moved to an older Windows system

### 3.7 Run System Check and Start Encryption

- [ ] Check box: "Run BitLocker system check"
- [ ] Click Continue
- [ ] Restart when prompted
- [ ] After restart: BitLocker verifies recovery key access, then encryption begins in background
- [ ] System remains usable during encryption

Monitor progress:
```powershell
manage-bde -status C:
```

Watch "Percentage Encrypted" field until it reaches 100%.

---

## Section 4: Recovery Key Backup and Storage

### 4.1 Verify Key Is Saved

- [ ] Log in to [account.microsoft.com/devices/recoverykey](https://account.microsoft.com/devices/recoverykey) from another device and confirm the key appears (if using Microsoft account option)
- [ ] Test USB key on a different machine if USB option was used
- [ ] Read back the printed recovery key and verify it matches the 48-digit key in BitLocker management

### 4.2 Recovery Key Storage Best Practices

**Where to store**:
- Microsoft account recovery page (online, accessible from any device with credentials)
- Password manager (1Password, Bitwarden, KeePass) — store the full 48-digit key
- Printed copy in a fireproof safe or safety deposit box
- Encrypted USB drive stored separately from the computer

**Where not to store**:
- On the same drive being encrypted
- In the same physical location as the laptop (theft scenario)
- In a plaintext file on an unencrypted location
- In email or SMS

### 4.3 Test Recovery Access

Before trusting the setup, test that you can actually use the recovery key:

- [ ] Temporarily suspend BitLocker: `manage-bde -protectors -disable C:`
- [ ] Reboot — system should boot without requesting the PIN (BitLocker suspended)
- [ ] Re-enable BitLocker: `manage-bde -protectors -enable C:`
- [ ] Confirm protection is active: `manage-bde -status C:` shows "Protection Status: Protection On"

**Full recovery test** (optional but recommended): Boot from a Windows installation USB, open Command Prompt from recovery options, enter `manage-bde -unlock C: -recoverypassword [48-digit-key]`. If this succeeds, your recovery key works.

---

## Section 5: Post-Setup Verification

Run all of these after encryption completes:

```powershell
# Full status check
manage-bde -status C:
```

Confirm all of the following:

- [ ] Size: matches your drive size
- [ ] BitLocker Version: 2.0 (Windows 10/11)
- [ ] Conversion Status: Fully Encrypted
- [ ] Percentage Encrypted: 100.0%
- [ ] Encryption Method: XTS-AES 128 (minimum) or XTS-AES 256 (stronger, requires Group Policy)
- [ ] Protection Status: Protection On
- [ ] Lock Status: Unlocked (current session)
- [ ] Identification Field: None (or your organization's identifier)
- [ ] Key Protectors: TPM (and PIN if configured), Recovery Password

```powershell
# List all protectors and confirm types
manage-bde -protectors -get C:
```

- [ ] TPM protector shown (if hardware supports it)
- [ ] Numerical Password protector shown (this is your recovery key — note the ID, not the key itself)

---

## Section 6: Troubleshooting Common Issues

### "BitLocker cannot be enabled. The system drive is not configured correctly."

Cause: Missing system partition (BitLocker requires a separate, small unencrypted partition for boot files).

Fix: Run in elevated Command Prompt: `BdeHdCfg.exe -target default`. This creates the required system partition. Restart and retry BitLocker setup.

### "TPM is not usable" or "TPM not found"

Cause: TPM not enabled in BIOS, or BIOS in Legacy mode.

Fix:
1. Reboot and enter BIOS (usually Del, F2, or F10 at startup)
2. Find "Security" or "Trusted Platform Module" settings
3. Enable TPM or "Security Device"
4. If BIOS mode shows "Legacy" or "CSM," run `mbr2gpt /validate` first, convert, then switch to UEFI mode

### "A required TPM measurement is not available" at boot

Cause: TPM measurements changed after a BIOS update, hardware change, or significant firmware change.

Fix: This triggers BitLocker recovery mode. Enter the 48-digit recovery key when prompted. After booting successfully, BitLocker updates its measurements and the next boot proceeds normally.

**Important**: Always suspend BitLocker before applying BIOS/firmware updates: `manage-bde -protectors -disable C:`. Re-enable after update completes.

### "BitLocker drive encryption is not supported on this version of Windows"

Cause: Windows Home edition does not include BitLocker Drive Encryption.

Fix: Use Device Encryption instead (Settings → Privacy & Security → Device Encryption), or upgrade to Windows Pro, or use Cryptomator for file-level encryption.

### BitLocker encryption stalls or pauses

Cause: System policy to pause encryption when on battery power, or heavy disk I/O.

Fix: Connect to AC power. Encryption resumes automatically. If stuck, run: `manage-bde -resume C:`

### Recovery key not found in Microsoft account

Cause: Device was not signed into a Microsoft account when BitLocker was enabled, or key was saved only locally.

Action: Check all backup locations (USB, printed copy, password manager). If no backup exists, data may not be recoverable after a TPM failure. This is why multiple backups are mandatory at setup time.

---

## Sources

- [Microsoft Learn: BitLocker Overview](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/)
- [Microsoft Learn: Configure BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/configure)
- [Microsoft Support: Back Up Your BitLocker Recovery Key](https://support.microsoft.com/en-us/windows/back-up-your-bitlocker-recovery-key-e63607b4-77fb-4ad3-8022-d6dc428fbd0d)
- [Microsoft Learn: BitLocker Recovery Overview](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/recovery-overview)
- [Microsoft Learn: Get-Tpm PowerShell cmdlet](https://learn.microsoft.com/en-us/powershell/module/trustedplatformmodule/get-tpm?view=windowsserver2025-ps)
- [Dell: How to Enable or Disable BitLocker with TPM in Windows](https://www.dell.com/support/kbdoc/en-us/000125409/how-to-enable-or-disable-bitlocker-with-tpm-in-windows)
- [NinjaOne: How to Back Up Your BitLocker Recovery Key](https://www.ninjaone.com/blog/how-to-back-up-your-bitlocker-recovery-key/)
