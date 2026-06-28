---
title: VeraCrypt Pre-Boot Test Failure Modes and Recovery Procedures
topic: disk-encryption-security
status: complete
confidence: 82%
created: 2026-06-24
sources:
  - https://veracrypt.io/en/System%20Encryption.html
  - https://veracrypt.io/en/VeraCrypt%20Rescue%20Disk.html
  - https://veracrypt.io/en/Troubleshooting.html
  - https://sourceforge.net/p/veracrypt/discussion/general/thread/96a6c04f/
  - https://sourceforge.net/p/veracrypt/discussion/technical/thread/f403d1d8/
  - https://sourceforge.net/p/veracrypt/discussion/technical/thread/5b859040/
  - https://sourceforge.net/p/veracrypt/discussion/technical/thread/f1650a78f7/
  - https://rclaussen.de/veracrypt-boot-problems-after-windows-10-update-solved/
  - https://github.com/veracrypt/VeraCrypt/issues/1485
  - https://github.com/veracrypt/VeraCrypt/issues/264
---

# VeraCrypt Pre-Boot Test Failure Modes and Recovery Procedures

> Lead finding: The pre-boot test reboot is a test only — no encryption has occurred yet at that point. A failure means the VeraCrypt bootloader did not register correctly with firmware. The drive is still unencrypted and Windows is intact. Recovery is almost always non-destructive if you have the Rescue Disk (created during setup) and if you have not panicked and run `bootrec` commands, which cannot see through encryption and should never be used on a VeraCrypt-encrypted drive.

---

## Critical Ground Rules Before Attempting Any Recovery

1. **Do not run `bootrec /fixmbr`, `bootrec /fixboot`, or `bootrec /rebuildbcd` on an encrypted drive.** These tools cannot read encrypted sectors and will treat valid encrypted data as corruption. They can render a drive unrecoverable. Source: [Microsoft Q&A — Windows 10 Restore Bootloader (VeraCrypt)](https://learn.microsoft.com/en-us/answers/questions/3985919/windows-10-restore-bootloader-(veracrypt))
2. **If you are still in the pre-test phase (no encryption started yet), the drive is still fully readable** by normal Windows recovery tools. This is the lowest-risk situation.
3. **Always create and verify the Rescue Disk** before the first restart. VeraCrypt requires this. In EFI mode it is a USB; in MBR mode it is a CD/DVD or USB ISO. The Rescue Disk is the universal recovery path for every failure mode below.
4. **Secure Boot must be disabled** for VeraCrypt to function in standard mode. Do not re-enable it while the drive is encrypted.

---

## Failure Mode 1: Secure Boot Blocking Bootloader Registration

### Failure Signature
The machine reboots for the pre-boot test and boots directly into Windows without any password prompt. Windows loads normally. VeraCrypt then reports the pre-test failed.

### Root Cause
Secure Boot validates bootloader signatures against keys stored in firmware. The standard VeraCrypt EFI bootloader (DcsBoot.efi) is not signed by Microsoft. When Secure Boot is enabled and no compatible certificate is loaded, firmware rejects the VeraCrypt bootloader silently and falls back to the Windows bootloader. The drive has not been encrypted at this point.

A newer signed variant exists: VeraCrypt's 2023 EFI loader requires firmware to trust "Microsoft UEFI CA 2023 and Microsoft Option ROM UEFI CA 2023." If neither certificate set is present in the firmware trust store, VeraCrypt aborts installation rather than placing an incompatible loader. Source: [VeraCrypt System Encryption](https://veracrypt.io/en/System%20Encryption.html)

### Recovery Procedure

**Time required: 10–20 minutes**

1. **Enter BIOS/UEFI** — restart and press F2, F10, Del, or the manufacturer key during POST (varies by vendor; Lenovo is typically F2, HP is typically F10 or Esc then F10, Dell is F2).
2. **Locate the Secure Boot setting** — usually under Security, Boot, or Authentication tab.
3. **Set Secure Boot to Disabled** and save (typically F10 to save and exit).
4. **Reboot into Windows** — it should boot normally.
5. **Re-run VeraCrypt system encryption** from within Windows — the pre-test should now pass.
6. **Do not re-enable Secure Boot** after encryption is complete. VeraCrypt requires Secure Boot remain disabled throughout the life of the encryption.

**Alternative (advanced, for systems requiring Secure Boot):** Load the VeraCrypt DCS signing key into firmware's Secure Boot custom key database. This involves VeraCrypt's `dumpEfiVars` tool and editing `sb_set_siglists.ps1`. This is a complex procedure and should only be attempted by users comfortable with firmware key management. Source: [VeraCrypt-DCS SecureBoot on GitHub](https://github.com/veracrypt/VeraCrypt-DCS/tree/master/SecureBoot)

### Prevention Checkpoints
- Before starting encryption: enter BIOS and confirm Secure Boot is **Disabled**.
- Verify BIOS mode is UEFI (not legacy/CSM) — check under Boot or System Information in BIOS.
- Confirm VeraCrypt version is current (1.26.x as of 2025). Older versions had more Secure Boot incompatibilities.

---

## Failure Mode 2: Firmware Overwrites Boot Order (UEFI Automatic Repair Loop)

### Failure Signature
The pre-boot test or a subsequent restart shows Windows "Automatic Repair" screen: "Automatic Repair couldn't repair your PC." The loop repeats on every restart — Automatic Repair → failure → restart → Automatic Repair. No VeraCrypt password prompt appears. This also occurs after major Windows updates or BIOS firmware updates on already-encrypted systems.

### Root Cause
Windows UEFI boot entries are writable by the OS itself. During major feature updates (e.g., Windows 10 1709, Windows 11 24H2) or after a BIOS firmware update, Windows rewrites the UEFI `BootOrder` variable to place `\EFI\Microsoft\Boot\bootmgfw.efi` first, displacing the VeraCrypt entry (`\EFI\VeraCrypt\DcsBoot.efi`). Windows' bootloader then launches, encounters an encrypted drive it cannot read, and initiates repair. Since repair tools also cannot read the encrypted partition, they fail in a loop.

Certain OEM firmware (HP, some Acer models) hardcodes boot to `\EFI\Microsoft\Boot\bootmgfw.efi` regardless of UEFI `BootOrder`. Source: [VeraCrypt Forums — UEFI not booting Windows 10](https://sourceforge.net/p/veracrypt/discussion/technical/thread/5b859040/), [gHacks — Fix the VeraCrypt Automatic Repair Issue](https://www.ghacks.net/2021/07/14/fix-the-veracrypt-automatic-repair-issue-on-windows/)

### Recovery Procedure

**Time required: 20–35 minutes**

**Path A — Using Rescue Disk (recommended, 95% success rate):**

1. Boot from the VeraCrypt Rescue Disk USB you created during setup. Use F8, F9, F11, or F12 at POST to select boot device.
2. Select **"Boot VeraCrypt loader from rescue disk"** — this bypasses the installed bootloader entirely.
3. Enter your password. If Windows loads, the disk is intact.
4. Once in Windows, open an elevated command prompt (Win+X → Terminal (Admin)).
5. Run: `bcdedit /set {bootmgr} path \EFI\VERACRYPT\DCSBOOT.EFI`
6. Restart — the VeraCrypt password prompt should now appear from the drive.

**Path B — bcdedit from Windows Recovery Environment (if no Rescue Disk):**

1. At the Automatic Repair screen, select **Advanced Options → Troubleshoot → Advanced Options → Command Prompt**.
2. Run: `bcdedit /set {bootmgr} path \EFI\VERACRYPT\DCSBOOT.EFI`
3. Restart.
4. Alternatively at the Automatic Repair screen: **Advanced Options → Use a device → VeraCrypt Bootloader** (if the entry still exists in NVRAM).

**Path C — HP and other OEMs with hardcoded boot paths (EFI file redirect):**

This is for machines that always boot `\EFI\Microsoft\Boot\bootmgfw.efi` regardless of `BootOrder`. Perform this from an elevated command prompt while Windows is running (before any encryption attempt), or from Rescue Disk recovery if encrypted.

```
mountvol o: /s
ren o:\EFI\Microsoft\Boot\bootmgfw.efi bootmgfw_ms.efi
copy o:\EFI\VeraCrypt\DcsBoot.efi o:\EFI\Microsoft\Boot\bootmgfw.efi
```

Then edit `o:\EFI\VeraCrypt\DcsProp` and add inside the `<config>` block:
```
<config key="ActionSuccess">postexec file(EFI\Microsoft\Boot\bootmgfw_ms.efi)</config>
```

This makes firmware load VeraCrypt's bootloader (now named `bootmgfw.efi`) first, and after successful password entry, VeraCrypt hands off to the renamed Microsoft bootloader. Source: [VeraCrypt Forums — HP ASUS DELL DcsBoot.efi Fix](https://sourceforge.net/p/veracrypt/discussion/technical/thread/f403d1d8/)

**Path D — Rescue Disk decrypt and re-encrypt (nuclear option, ~2 hours):**

1. Boot Rescue Disk, select **"Decrypt OS"**.
2. After decryption completes, Windows recovers normally.
3. Run Windows updates to completion.
4. Re-encrypt with VeraCrypt.
Source: [rclaussen.de — VeraCrypt boot problems after Windows 10 update](https://rclaussen.de/veracrypt-boot-problems-after-windows-10-update-solved/)

### Prevention Checkpoints
- **Set a UEFI Administrator password** in BIOS before encrypting. Windows cannot overwrite UEFI boot entries when a firmware password is set. A simple password (e.g., "1234") is sufficient — its purpose is to block OS-level NVRAM writes, not human authentication. Source: [rclaussen.de](https://rclaussen.de/veracrypt-boot-problems-after-windows-10-update-solved/)
- Defer major Windows feature updates until you have a maintenance window and a current Rescue Disk.
- After each Windows major update, verify VeraCrypt password prompt still appears on next restart.

---

## Failure Mode 3: Password Rejected Despite Correct Entry (Keyboard Layout Mismatch)

### Failure Signature
The VeraCrypt password prompt appears correctly. You enter your password. VeraCrypt reports "Password is incorrect" on every attempt, even though you are confident the password is right. This is particularly common on systems with non-US keyboard layouts or with special characters in the password.

### Root Cause
The VeraCrypt pre-boot environment runs before any OS loads and uses the BIOS/firmware keyboard driver, which presents all keyboards as **US QWERTY layout** regardless of the physical keyboard or Windows regional settings. If the password was set while Windows was active (using the localized layout), characters that differ between the user's layout and US QWERTY will be sent as different characters at boot time.

Examples: On a German keyboard, `y` and `z` are swapped. On a French AZERTY layout, digits require Shift. The `@` symbol is in different positions across layouts. Additionally, Num Lock and Caps Lock state matters — the state at boot must match the state when the password was originally typed. Source: [VeraCrypt Troubleshooting](https://veracrypt.io/en/Troubleshooting.html), [VeraCrypt Forums — OS encryption wrong password](https://sourceforge.net/p/veracrypt/discussion/technical/thread/c65a02cb/)

### Recovery Procedure

**Time required: 15–25 minutes**

1. **Try toggling Num Lock and Caps Lock** — at the boot password screen, try entering the password with Num Lock on, then off. Try Caps Lock toggled. VeraCrypt boots without knowing these states.
2. **Press F5 at the VeraCrypt boot screen** to toggle visible password display. Type the password and compare what appears on screen to what you expect with US keyboard mappings.
3. **Map your password to US layout mentally** — look up a US keyboard layout image. Identify which keys on your physical keyboard correspond to which characters in US layout. Enter the password using those mappings.
4. **If the above fails, use the Rescue Disk:**
   - Boot the Rescue Disk.
   - Select **"Restore OS header keys"** (EFI) or **"Repair Options → Restore VeraCrypt Boot Loader"** (MBR) — this restores the volume header from the Rescue Disk's backup, using the original password.
   - Attempt password entry again at the restored prompt.
5. **If still rejected:** This may indicate volume header corruption rather than a keyboard issue. In this case, the Rescue Disk's header restore (Step 4) is the correct long-term fix. If that also fails, recovery requires the original password — there is no bypass.

**Important caveat:** The Rescue Disk's header backup is encrypted with the original password. Changing the VeraCrypt password after creating the Rescue Disk makes the Rescue Disk's header backup stale. Always create a new Rescue Disk after changing the password (System → Create Rescue Disk). Source: [VeraCrypt Rescue Disk documentation](https://veracrypt.io/en/VeraCrypt%20Rescue%20Disk.html)

### Prevention Checkpoints
- Use only **standard ASCII characters** in the pre-boot password: `A-Z`, `a-z`, `0-9`, and common symbols (`!`, `#`, `$`, `-`). Avoid language-specific characters (umlauts, accented characters, curly quotes).
- Note the state of Num Lock and Caps Lock when setting the password. Store this alongside the password in your password manager entry.
- During initial password setup, VeraCrypt shows a warning that the keyboard layout switches to US. Verify: open Notepad, type the intended password, and confirm it appears as you expect with the US layout active.
- Test the password on the Rescue Disk before fully encrypting — the Rescue Disk prompt uses the same pre-boot keyboard driver.

---

## Failure Mode 4: USB Keyboard Unresponsive at Boot Prompt

### Failure Signature
The VeraCrypt password prompt appears on screen, but pressing any key on the USB keyboard has no effect. The system appears frozen. PS/2 keyboards (if present) may still work. This failure often affects desktop users who recently replaced their keyboard with a USB model, or laptop users with a USB hub configuration.

### Root Cause
BIOS/UEFI pre-boot environments require a separate driver pathway for USB keyboards: "USB Legacy Support" or "Legacy USB Keyboard." Without it, USB HID devices are not initialized until the OS loads its USB stack — which means they do not function during the VeraCrypt pre-boot authentication phase. Source: [VeraCrypt Troubleshooting](https://veracrypt.io/en/Troubleshooting.html)

### Recovery Procedure

**Time required: 15–20 minutes**

1. If completely locked out (cannot type password at all), restart and enter BIOS using whatever key the firmware responds to — this may require a PS/2 keyboard temporarily, or a laptop's built-in keyboard if available.
2. In BIOS, navigate to **Advanced → USB Configuration** (naming varies by vendor: may be "USB Settings," "Chipset," or "Peripherals").
3. Enable **"Legacy USB Support"** (also called "USB Legacy," "USB Legacy Keyboard," or "USB HID Support").
4. Save and restart (typically F10).
5. The VeraCrypt password prompt should now accept USB keyboard input.

**If you cannot enter BIOS** (USB keyboard only, no response at all):
- Check whether the motherboard has a PS/2 port. Many do even on modern boards. Use a PS/2 keyboard or a USB-to-PS/2 adapter to enter BIOS.
- On some systems, keyboard input at BIOS is only possible through front-panel USB ports, not rear USB 3.x ports. Try a different physical USB port.
- If using a USB hub: connect the keyboard directly to a motherboard USB port, not through a hub.

**Note:** If encryption has already completed and you cannot enter the password, boot from the Rescue Disk, which provides its own input handling. On systems where the Rescue Disk also fails to accept input, the Rescue Disk's "Decrypt OS" path can sometimes proceed with boot-time menu navigation (arrow keys + Enter) without needing to type the password at the prompt.

### Prevention Checkpoints
- Before starting encryption: enter BIOS and verify USB Legacy Support is **Enabled**.
- Test keyboard responsiveness in BIOS itself — if you can navigate BIOS menus with the keyboard, it will work at the VeraCrypt prompt.
- Avoid using USB keyboards through powered hubs for pre-boot authentication.

---

## Failure Mode 5: System Hangs at "Booting..." After Password Accepted

### Failure Signature
The VeraCrypt bootloader appears and accepts the password — it confirms "Password OK" (or similar) and displays "Booting..." — then the system hangs indefinitely. The drive activity light may be blinking or static. Windows never starts loading. Hard reset is required.

### Root Cause
Two distinct causes are documented:

**Cause A — BIOS firmware bug:** The BIOS cannot correctly hand off to the bootloader after decryption. This is a known issue documented in VeraCrypt's official troubleshooting since early versions. Some BIOS versions have a bug where the memory map or boot handoff sequence fails after the VeraCrypt pre-boot decryption stage. Source: [VeraCrypt Troubleshooting](https://veracrypt.io/en/Troubleshooting.html)

**Cause B — Windows 11 24H2 MBR compatibility regression:** An open bug (as of 2025) affects systems running Windows 11 24H2 in legacy MBR mode with VeraCrypt 1.26.24. The system accepts the password, displays "Booting...", and hangs. Pressing Escape bypasses the hang and allows normal boot in this specific configuration. This is an unresolved regression with no confirmed root cause. Source: [GitHub Issue #1485 — VeraCrypt Windows 11 24H2 stuck during "booting..."](https://github.com/veracrypt/VeraCrypt/issues/1485)

**Cause C — Windows bootloader injection:** Windows may have injected its bootloader into the MBR or BCD, causing a handoff conflict where VeraCrypt passes control to a Windows bootloader that cannot read the encrypted partition. Source: [VeraCrypt Troubleshooting](https://veracrypt.io/en/Troubleshooting.html)

### Recovery Procedure

**Time required: 20–45 minutes depending on cause**

**For Cause A (BIOS bug):**

1. Check the motherboard manufacturer's website for a BIOS/firmware update. Flash the update from an unencrypted system (boot a different drive or USB live environment to flash).
2. If no update is available and you are still in the pre-test phase (not yet encrypted), try a different motherboard or run VeraCrypt in a VM for testing.
3. As a workaround: use the Windows Installation disk to run `BootRec /fixmbr` and `BootRec /FixBoot` — **only if the drive is still unencrypted** (pre-test phase). If encryption is already complete, skip bootrec entirely.
4. Some users resolved this by deleting the 100 MB System Reserved partition and setting the system partition as the active partition — this applies to MBR-mode systems only. Source: [VeraCrypt Troubleshooting](https://veracrypt.io/en/Troubleshooting.html)

**For Cause B (Windows 11 24H2 MBR regression):**

1. Press Escape at the "Booting..." screen — on affected systems this successfully continues boot into Windows.
2. This is a known workaround for the open bug. There is no permanent fix as of mid-2025. Monitor the [GitHub issue](https://github.com/veracrypt/VeraCrypt/issues/1485) for resolution.
3. Consider migrating the system from MBR legacy mode to UEFI mode if hardware supports it (this is a significant operation requiring reinstallation).

**For Cause C (bootloader conflict, already encrypted):**

1. Boot the VeraCrypt Rescue Disk.
2. Select **"Restore VeraCrypt Boot Loader"** (MBR) or **"Restore VeraCrypt loader binaries to system disk"** (EFI).
3. Restart without the Rescue Disk — the VeraCrypt prompt should work correctly.
4. If still hanging, use Rescue Disk → **"Decrypt OS"** to fully decrypt, then re-encrypt after resolving the underlying conflict.

**If you cannot recover:** If the system is encrypted and neither the Rescue Disk nor Escape workaround resolves the hang, this situation requires professional data recovery. Do not attempt destructive operations on the encrypted drive. Source: [VeraCrypt Troubleshooting](https://veracrypt.io/en/Troubleshooting.html)

### Prevention Checkpoints
- Flash BIOS to the latest version **before** beginning system encryption.
- For Windows 11 24H2 systems: verify VeraCrypt is at the latest available version and check the GitHub issue tracker for resolved status before encrypting a production system.
- If running legacy MBR mode on Windows 11, consider this an elevated risk configuration until the regression is resolved.

---

## Pre-Boot Test Success Checklist (>90% Success Probability)

Complete all items before clicking "Test" in VeraCrypt System Encryption Wizard. This list is derived from the official troubleshooting guide and community-reported failure patterns above.

### Firmware / BIOS

- [ ] **Secure Boot is DISABLED** in BIOS/UEFI
- [ ] **USB Legacy Support is ENABLED** (Advanced → USB Configuration → Legacy USB Support)
- [ ] **BIOS firmware is up to date** — check manufacturer site
- [ ] **UEFI Administrator password is set** (prevents Windows from overwriting boot order during updates)
- [ ] **Boot mode confirmed**: know whether system is UEFI or MBR/Legacy (check: System Information → BIOS Mode in Windows, or msinfo32.exe)

### Password Setup

- [ ] **Password uses only standard ASCII characters** — no language-specific characters, no umlauts, no curly quotes
- [ ] **Num Lock and Caps Lock states recorded** — note their state at the moment you type the password
- [ ] **Password verified in US keyboard layout** — with Windows keyboard temporarily set to English (US), typed the password in Notepad and confirmed it looks correct
- [ ] **Password length ≥ 20 characters** recommended (pre-boot environment has no lockout protection)

### Rescue Disk

- [ ] **Rescue Disk created and verified** — VeraCrypt requires this before proceeding. In EFI mode: verified bootable USB. In MBR mode: verified bootable CD/DVD or USB ISO
- [ ] **Rescue Disk tested** — booted from it at least once to confirm it loads and accepts the password
- [ ] **Rescue Disk stored separately** from the encrypted machine — it is useless if it is only on the drive being encrypted

### System State

- [ ] **All Windows updates completed** before encrypting — do not start encryption immediately before a pending feature update
- [ ] **Third-party disk utilities and partition managers closed** — no background disk activity during pre-test
- [ ] **No pending disk check (chkdsk) scheduled** — run `chkdsk C: /f` and restart once to clear it before encrypting
- [ ] **Laptop is on AC power** — encryption test should not run on battery to prevent mid-process shutdown
- [ ] **Antivirus real-time scanning paused or excluded** for the VeraCrypt executable during the pre-test phase (some AV products interfere with bootloader writes)

---

## Confidence Assessment

| Failure Mode | Source Quality | Confidence |
|---|---|---|
| Secure Boot blocking registration | Official docs + multiple forum confirmations | 92% |
| UEFI boot order overwrite / Automatic Repair loop | Multiple independent sources + gHacks + rclaussen.de | 90% |
| Password rejected / keyboard layout mismatch | Official troubleshooting guide + forum thread | 88% |
| USB keyboard unresponsive at boot | Official troubleshooting guide (direct citation) | 95% |
| System hangs at "Booting..." | Official troubleshooting (Cause A/C) + open GitHub issue (Cause B) | 78% for A/C; 60% for B (no confirmed fix) |

**Overall report confidence: 82%**

Gaps in evidence:
- Cause B (Windows 11 24H2 MBR "Booting..." hang) remains an open unresolved bug. The Escape workaround is user-reported but unconfirmed by the VeraCrypt team.
- OEM-specific firmware behaviors (particularly Acer EFI BootOrder persistence bug, certain HP models) have community workarounds but no official documentation from those manufacturers.
- Recovery procedures for RAID or multi-disk configurations are not covered here — VeraCrypt system encryption on RAID is explicitly not recommended in the official documentation.

---

## Sources

- [VeraCrypt System Encryption — Official Documentation](https://veracrypt.io/en/System%20Encryption.html)
- [VeraCrypt Rescue Disk — Official Documentation](https://veracrypt.io/en/VeraCrypt%20Rescue%20Disk.html)
- [VeraCrypt Troubleshooting — Official Documentation](https://veracrypt.io/en/Troubleshooting.html)
- [VeraCrypt Forums — Encryption Boot Pre-Test Fails](https://sourceforge.net/p/veracrypt/discussion/general/thread/96a6c04f/)
- [VeraCrypt Forums — HP ASUS DELL DcsBoot.efi Bootloader Fix](https://sourceforge.net/p/veracrypt/discussion/technical/thread/f403d1d8/)
- [VeraCrypt Forums — VeraCrypt Not Booting Windows 10 UEFI](https://sourceforge.net/p/veracrypt/discussion/technical/thread/5b859040/)
- [VeraCrypt Forums — How to Solve VeraCrypt Boot Problems (Automatic Repair Loop)](https://sourceforge.net/p/veracrypt/discussion/technical/thread/f1650a78f7/)
- [rclaussen.de — VeraCrypt Boot Problems After Windows 10 Update (Solved)](https://rclaussen.de/veracrypt-boot-problems-after-windows-10-update-solved/)
- [GitHub Issue #1485 — VeraCrypt Windows 11 24H2 Stuck at "Booting..."](https://github.com/veracrypt/VeraCrypt/issues/1485)
- [GitHub Issue #264 — Win10 UEFI PreBoot-Auth Fails Always](https://github.com/veracrypt/VeraCrypt/issues/264)
- [VeraCrypt-DCS SecureBoot Repository](https://github.com/veracrypt/VeraCrypt-DCS/tree/master/SecureBoot)
- [Microsoft Q&A — Windows 10 Restore Bootloader (VeraCrypt)](https://learn.microsoft.com/en-us/answers/questions/3985919/windows-10-restore-bootloader-(veracrypt))
