---
title: "Device Hardening Implementation Guide (macOS, Linux, Windows)"
project: cybersecurity-hardening
created: 2026-05-05
status: complete
depends_on: opsec-playbook.md, threat-model.md, device-hardening-guide.md
confidence: high — sourced from drduh macOS security guide, Linux UFW documentation, Microsoft security hardening guides, NCSC Windows guidance, Privacy Guides browser recommendations
---

# Device Hardening Implementation Guide

> **Danger**: Test hardening configurations on non-critical devices or in virtual machines first. Misconfigured firewalls, AppArmor profiles, or browser settings can break functionality in ways that are difficult to diagnose. Apply changes incrementally, verify functionality after each step, and document what you change so you can reverse it.

> **Note**: This guide covers desktop and laptop systems (macOS, Linux, Windows). For mobile device hardening, see `device-hardening-guide.md`, which covers iOS and Android comprehensively.

---

## Threat Model

This guide addresses the following threat actors and attack surfaces:

| Threat | Counter-measure |
|---|---|
| Malware installed via phishing, downloads | Permission reduction, app sandboxing, update hygiene |
| Network-level surveillance | Firewall rules, DNS encryption |
| Data harvest if device seized | Full-disk encryption |
| Browser fingerprinting | Browser hardening |
| Unpatched vulnerability exploitation | Update procedures |
| Firmware-level attacks | BIOS/UEFI/TPM hardening |

**Who this guide is for**: Users with administrative access to their own devices who want to reduce their attack surface without specialized security training.

---

## Part 1: macOS Hardening

### 1.1 System-Level Settings

**Enable FileVault (full disk encryption)**:
1. System Settings → Privacy & Security → FileVault → Turn On.
2. FileVault uses XTS-AES-128 encryption tied to your login password and (optionally) an iCloud recovery key.
3. Choose "Create a recovery key and do not use my iCloud account" if your threat model includes Apple being compelled to assist with account recovery.
4. Store the recovery key offline (printed and stored securely, or in a hardware password manager).

If you forget your password and lose your recovery key, your data is permanently unrecoverable. This is the correct tradeoff — it means an adversary with your physical device also cannot recover your data without your password.

**Require password immediately on sleep/screen saver**:
1. System Settings → Lock Screen → "Require password after screen saver begins or display is turned off" → "Immediately."

**Disable automatic login**:
1. System Settings → Users & Groups → disable automatic login.

**Review privacy settings for each application**:
1. System Settings → Privacy & Security.
2. Review each category: Location Services, Contacts, Calendars, Photos, Microphone, Camera, Accessibility, Full Disk Access.
3. Remove access for any application that does not require it. If you are unsure why an app needs a permission, remove it and see if the app stops working for a specific needed function.

**Disable Spotlight suggestions (reduces data sent to Apple)**:
1. System Settings → Siri & Spotlight → uncheck "Siri Suggestions" and individual web search categories.

### 1.2 Firewall Configuration

**Enable the macOS application firewall**:
1. System Settings → Network → Firewall → turn on.
2. Click Firewall Options.
3. Enable "Block all incoming connections" — this allows only outbound connections that your applications initiate. Incoming connection requests are blocked.
4. Exception: If you run local servers (web server, file sharing), you must add specific exceptions. Do so only for services you actively use.
5. Enable "Enable stealth mode" — this prevents your Mac from responding to network probing (ICMP ping, port scans).

**pf (Packet Filter) for advanced users**:

macOS includes BSD's `pf` firewall, which provides more granular control than the application firewall. For most users, the application firewall above is sufficient and safer to configure. For users familiar with packet filtering who want to monitor outbound "phone home" behavior:

```bash
# Check pf status
sudo pfctl -si

# View current pf rules
sudo pfctl -sr

# Load a custom ruleset (example: block all inbound, allow established outbound)
# Create /etc/pf.anchors/custom.rules:
```

Example `/etc/pf.anchors/custom.rules`:
```
# Default deny all inbound
block in all

# Allow established outbound connections and their return traffic
pass out proto tcp flags S/SA keep state
pass out proto udp keep state

# Allow loopback
pass on lo0
```

> **Danger**: Incorrect pf rules can cut off network access entirely. Test in a virtual machine first. Keep a physical console or alternate access method available. The official `pf.conf` man page (`man pf.conf`) is the authoritative reference.

Reference: [drduh macOS Security and Privacy Guide — pf section](https://github.com/drduh/macOS-Security-and-Privacy-Guide)

### 1.3 Update Procedures

1. System Settings → General → Software Update → "Automatic Updates" → enable all options.
2. Enable "Install Security Responses and system files" — these are rapid-response patches for actively exploited vulnerabilities.
3. For applications from the App Store: System Settings → App Store → enable "Automatic Updates."
4. For applications installed outside the App Store: check each application's built-in update mechanism. Priority updates: browsers, PDF readers, email clients, and any application that handles remote content.

### 1.4 Application Security

**Use Gatekeeper** (verifies app signatures):
1. System Settings → Privacy & Security → "Allow apps downloaded from" → "App Store and identified developers."
2. Do not set this to "Anywhere" — that disables Gatekeeper.

**Sandbox verification**: macOS sandboxes App Store applications by default. Third-party apps installed outside the App Store are not sandboxed unless the developer explicitly adds sandbox entitlements. For highest security, prefer App Store versions of software when available.

---

## Part 2: Linux Hardening

### 2.1 Full Disk Encryption

For new installations: enable LUKS (Linux Unified Key Setup) full disk encryption during OS installation. Most major distributions (Ubuntu, Fedora, Debian) offer this as an option during installation.

For an existing system: full disk encryption cannot be easily added post-installation without reinstalling. Consider a fresh install with encryption enabled.

**Verify your disk is encrypted**:
```bash
lsblk -o NAME,TYPE,FSTYPE,MOUNTPOINT
# Look for "crypto_LUKS" in the FSTYPE column
```

### 2.2 UFW Firewall Configuration

UFW (Uncomplicated Firewall) is the recommended firewall management tool for Ubuntu/Debian. It wraps iptables with a simpler interface.

**Basic hardening setup**:

```bash
# Check if UFW is installed
sudo apt install ufw

# Set default deny for both incoming and outgoing
sudo ufw default deny incoming
sudo ufw default deny outgoing

# Allow essential outbound connections
# DNS (port 53)
sudo ufw allow out 53/tcp
sudo ufw allow out 53/udp

# HTTP/HTTPS
sudo ufw allow out 80/tcp
sudo ufw allow out 443/tcp

# NTP (time synchronization)
sudo ufw allow out 123/udp

# Allow DHCP (if you use DHCP)
sudo ufw allow out 67/udp
sudo ufw allow out 68/udp

# If you need SSH outbound (to connect to servers)
sudo ufw allow out 22/tcp

# Enable UFW
sudo ufw enable

# Verify status
sudo ufw status verbose
```

> **Danger**: Setting `default deny outgoing` without the necessary allow rules above will break network access immediately. Ensure your allow rules are in place before enabling UFW. If you lose connectivity after enabling UFW, log in via a local console and run `sudo ufw disable` to restore access.

**Allow specific inbound services only if needed**:
```bash
# Allow SSH from specific IP only (more secure than open)
sudo ufw allow from 192.168.1.0/24 to any port 22

# Rate-limit SSH to prevent brute force
sudo ufw limit ssh
```

**Log rejected connections** (for monitoring):
```bash
sudo ufw logging on
# Logs appear in /var/log/ufw.log
```

Reference: [UFW Firewall Ubuntu Guide](https://toolsana.com/blog/ufw-firewall-ubuntu-complete-configuration-guide/) | [Linux Security: UFW Hardening](https://linuxsecurity.com/news/firewall/ufw-hardening)

### 2.3 AppArmor (Application Sandboxing — Ubuntu/Debian)

AppArmor confines applications to a defined set of permissions. Most Ubuntu installations include AppArmor, but not all applications have profiles.

```bash
# Check AppArmor status
sudo aa-status

# Install AppArmor profiles (if not installed)
sudo apt install apparmor-profiles apparmor-profiles-extra

# Check which profiles are in enforce mode vs complain mode
sudo aa-status | grep -E '(enforce|complain)'

# Put a profile into enforce mode
sudo aa-enforce /etc/apparmor.d/usr.bin.firefox
```

For custom profiles, `aa-genprof` can be used to create a profile by monitoring an application:
```bash
sudo aa-genprof /path/to/application
# Run the application, exercise its functions
# Then finalize the profile with Ctrl+C and review
```

### 2.4 Automatic Security Updates

On Ubuntu/Debian:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

This automatically installs security updates. Verify configuration at `/etc/apt/apt.conf.d/50unattended-upgrades`.

On Fedora/RHEL:
```bash
sudo dnf install dnf-automatic
sudo systemctl enable --now dnf-automatic-install.timer
```

### 2.5 Kernel Hardening via sysctl

Kernel parameters can be hardened to mitigate specific attack classes. Add to `/etc/sysctl.d/99-hardening.conf`:

```ini
# Disable IPv6 if not used (reduces attack surface)
net.ipv6.conf.all.disable_ipv6 = 1

# Prevent ICMP redirect acceptance (prevents routing attacks)
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0

# Ignore ICMP ping requests (stealths the host)
net.ipv4.icmp_echo_ignore_all = 1

# Prevent IP spoofing
net.ipv4.conf.all.rp_filter = 1

# Disable source routing
net.ipv4.conf.all.accept_source_route = 0

# Enable SYN flood protection
net.ipv4.tcp_syncookies = 1

# Restrict core dumps (prevents memory content leaks)
fs.suid_dumpable = 0

# Disable magic SysRq key (prevents low-level system access)
kernel.sysrq = 0

# Restrict access to kernel pointers in /proc
kernel.kptr_restrict = 2

# Restrict ptrace (debugging) to parent processes
kernel.yama.ptrace_scope = 1
```

Apply immediately: `sudo sysctl --system`

> **Danger**: `net.ipv4.icmp_echo_ignore_all = 1` means your system will not respond to pings, which can complicate network troubleshooting. Adjust based on your needs. `net.ipv6.conf.all.disable_ipv6 = 1` will break applications that require IPv6. Test in a VM or non-critical system first.

---

## Part 3: Windows 11 Hardening

### 3.1 BitLocker Full Disk Encryption

BitLocker requires Windows 11 Pro, Enterprise, or Education editions.

1. Search "Manage BitLocker" in Start.
2. Click "Turn on BitLocker" on the C: drive.
3. Choose how to unlock on startup: "Enter a PIN" is more secure than "USB key" for portable devices.
4. Back up your recovery key: save to a file, print it, or save to your Microsoft account. For high-risk users, save to a file on a USB drive stored separately — not to a Microsoft account.
5. Choose "Encrypt entire drive" (not just used space) for maximum security.
6. Run the BitLocker system check and restart.

**Verify BitLocker status**:
```cmd
manage-bde -status C:
```

### 3.2 Windows Firewall (Windows Defender Firewall)

1. Settings → Windows Security → Firewall & network protection.
2. Confirm all three network profiles (Domain, Private, Public) show Firewall as "On."
3. For enhanced control: search "Windows Defender Firewall with Advanced Security."
4. In the advanced interface, you can create granular inbound and outbound rules by application, port, and protocol.

**Default behavior**: Windows Defender Firewall blocks unsolicited inbound connections and allows all outbound connections by default. For workstation hardening:

**Block outbound connections by default (advanced)**:
1. In "Windows Defender Firewall with Advanced Security" → Properties → each profile tab → Outbound connections → "Block."
2. Then add specific allow rules for browsers, updates, and needed applications.

> **Danger**: Blocking all outbound connections by default on Windows will immediately break many system functions (Windows Update, activation, cloud services). Build your allow rules before applying the block, and have a rollback plan. This is for advanced users with time to enumerate needed connections.

### 3.3 TPM and Secure Boot

**Verify TPM 2.0 is enabled**:
1. Press Win+R → `tpm.msc` → Enter.
2. The TPM Management console shows the TPM status. "The TPM is ready for use" with specification version 2.0 is correct.

**Enable in BIOS/UEFI** (if not enabled):
1. Restart the computer.
2. Enter BIOS/UEFI (typically F2, F10, F12, or Del during startup — varies by manufacturer).
3. Navigate to Security or Advanced → TPM/Trusted Platform Module.
4. Set to "Enabled." On Intel systems, this may be labeled "Intel Platform Trust Technology (PTT)." On AMD, "AMD fTPM" or "AMD Trusted Platform Module."
5. Save and exit.

**Enable Secure Boot**:
1. BIOS/UEFI → Secure Boot → Enable.
2. Windows 11 requires Secure Boot. If you disabled it for Linux dual-boot, re-evaluate whether to re-enable it.

**Enable Kernel DMA Protection** (prevents DMA attacks via Thunderbolt/USB-C):
1. BIOS/UEFI → Security → Kernel DMA Protection → Enable.
2. Verify in Windows: search "System Information" → check "Kernel DMA Protection" row.

### 3.4 Windows Defender Application Control (WDAC) / AppLocker

WDAC is the modern replacement for AppLocker and restricts which applications can execute.

**Basic WDAC policy (PowerShell, requires Admin)**:
```powershell
# Generate a default policy (allows only signed Windows components and Store apps)
$Policy = New-CIPolicy -Level Publisher -FilePath "C:\Policy.xml" -ScanPath "C:\Windows\System32" -UserPEs -Fallback Hash

# Convert to binary
ConvertFrom-CIPolicy -XmlFilePath "C:\Policy.xml" -BinaryFilePath "C:\SiPolicy.p7b"
```

For most workstation users, Windows Defender Antivirus with real-time protection enabled is sufficient. WDAC is primarily appropriate for managed enterprise environments.

**Ensure Windows Defender is configured**:
1. Windows Security → Virus & threat protection → Protection settings.
2. Verify Real-time protection is On.
3. Enable "Tamper Protection" — this prevents malware from disabling Defender.
4. Enable "Controlled folder access" (Settings → Virus & threat protection settings → Controlled folder access) — this blocks unauthorized writes to protected folders.

### 3.5 Update Procedures

1. Settings → Windows Update → ensure "Get the latest updates as soon as they're available" is enabled.
2. Check for updates manually: Settings → Windows Update → "Check for updates."
3. Restart promptly after critical updates — unpatched systems are the most common enterprise breach vector.

Reference: [Windows 11 Security Hardening Guide 2025](https://lorikeetsmart.com/blog/windows-security-hardening-2025.html) | [NCSC Windows Platform Guide](https://www.ncsc.gov.uk/collection/device-security-guidance/platform-guides/windows)

---

## Part 4: Browser Hardening

### 4.1 Firefox Hardening

Firefox is the recommended browser for privacy-conscious users because it is open-source, actively audited, and configurable. Chrome/Chromium shares significant telemetry with Google.

**Essential extensions**:
- **uBlock Origin**: Installs ad and tracker blocking. After installation, open its options panel and enable additional filter lists: Privacy → EasyPrivacy and AdGuard Privacy. This adds malware domain blocking in addition to ad blocking.
- **No others**: Each extension increases your browser fingerprint (making you more uniquely identifiable). More is not better.

**uBlock Origin in Medium Mode** (blocks third-party scripts by default):
1. Open uBlock Origin popup → click the shield icon to enter the dashboard.
2. Enable "I am an advanced user."
3. In the dashboard → Filter Lists: enable EasyPrivacy, AdGuard Privacy, uBlock Filters – Privacy, uBlock Filters – Unbreak.
4. Medium mode blocks all third-party JavaScript by default. You can whitelist specific domains as needed. This is more effective than standard mode but requires more maintenance when sites break.

**about:config hardening (Firefox)**:
1. Type `about:config` in the address bar → accept the warning.
2. Search for and modify the following settings:

```
# Disable telemetry
datareporting.healthreport.uploadEnabled = false
datareporting.policy.dataSubmissionEnabled = false
toolkit.telemetry.enabled = false

# Resist fingerprinting (makes Firefox more uniform across users)
privacy.resistFingerprinting = true

# Enable first-party isolation (cookies isolated per top-level domain)
privacy.firstparty.isolate = true

# Disable WebRTC (can leak real IP even with VPN)
media.peerconnection.enabled = false

# Disable safe browsing (sends URLs to Google for checking)
# Only disable this if you trust your own judgment about links
browser.safebrowsing.malware.enabled = false
browser.safebrowsing.phishing.enabled = false

# Disable preloading
network.prefetch-next = false
network.dns.disablePrefetch = true
```

> **Danger**: `privacy.resistFingerprinting = true` may break some websites. `media.peerconnection.enabled = false` disables WebRTC entirely, which breaks video calling in browsers. `browser.safebrowsing.malware.enabled = false` removes a layer of phishing protection — only disable this if you have another mitigation (e.g., DNS-level blocking via uBlock Origin's malware lists).

**DNS over HTTPS in Firefox**:
1. Settings → Privacy & Security → DNS over HTTPS → "Max Protection."
2. Choose a resolver (NextDNS, Cloudflare, Mullvad).

### 4.2 Browser Fingerprinting Defense

Browser fingerprinting creates a unique identifier from a combination of: user-agent string, installed fonts, canvas rendering, WebGL rendering, screen dimensions, audio processing fingerprint, timezone, and plugin list.

`privacy.resistFingerprinting = true` in Firefox causes Firefox to report standardized values for most fingerprinting vectors, making your Firefox look like many other Firefox instances.

**Mullvad Browser**: The Tor Project and Mullvad jointly developed Mullvad Browser, which applies Tor Browser's anti-fingerprinting protections to clearnet browsing (no Tor network required). It is the most effective anti-fingerprinting browser for clearnet use. Download from [mullvad.net/en/browser](https://mullvad.net/en/browser).

**Test your fingerprint**: [coveryourtracks.eff.org](https://coveryourtracks.eff.org) (EFF's fingerprint testing tool).

---

## Part 5: BIOS/UEFI Security

### Common Firmware Settings to Review

Regardless of operating system, firmware security applies to all platforms.

**Enable Secure Boot**: Verifies that bootloader and OS kernel are cryptographically signed. Prevents bootkit attacks. Required for Windows 11; compatible with modern Linux distributions.

**Set a firmware password**: Prevents an attacker with physical access from booting from external media (USB, network boot) or modifying BIOS settings without the password.
- BIOS → Security → Administrator Password or Supervisor Password → set a strong password.
- Store this password in your password manager — losing it can lock you out of your own firmware settings permanently.

**Disable unused boot devices**: BIOS → Boot → disable Network Boot (PXE), boot from USB (if you do not need it), and Optical Drive.

**Disable Intel ME (Management Engine) AMT / Thunderbolt pre-boot DMA** (if available): These are vectors for physical-access attacks. Not all BIOS UIs expose these options.

**Update firmware**: Firmware updates are critical — CVE-2023-1017 and CVE-2023-1018 (TPM buffer overflow) required firmware patches. Check your laptop or motherboard manufacturer's support page for firmware updates.
- Dell: run Dell Update utility
- Lenovo: System Update tool
- HP: HP Support Assistant
- ASUS, MSI, Gigabyte: download from manufacturer support page

---

## Master Device Hardening Checklist

### macOS
- [ ] FileVault enabled with offline recovery key
- [ ] Application firewall enabled with stealth mode
- [ ] Auto-updates enabled for OS and App Store apps
- [ ] Privacy settings audited (camera, microphone, location, accessibility)
- [ ] Require password immediately on sleep
- [ ] Automatic login disabled

### Linux
- [ ] LUKS full disk encryption enabled
- [ ] UFW configured: default deny incoming, selective outbound allow
- [ ] AppArmor profiles in enforce mode for key applications
- [ ] Automatic security updates configured
- [ ] sysctl hardening parameters applied
- [ ] Firewall rules tested (verify reject behavior)

### Windows
- [ ] BitLocker enabled on all drives
- [ ] Windows Defender Firewall on for all profiles
- [ ] TPM 2.0 enabled and verified
- [ ] Secure Boot enabled
- [ ] Windows Defender Tamper Protection on
- [ ] Controlled Folder Access enabled
- [ ] Windows Update configured for automatic security updates

### All Platforms
- [ ] Full disk encryption enabled
- [ ] BIOS/UEFI firmware password set
- [ ] Secure Boot enabled
- [ ] Firmware updated to latest version
- [ ] uBlock Origin installed in browser
- [ ] Firefox `privacy.resistFingerprinting` enabled
- [ ] DNS over HTTPS enabled in browser
- [ ] Browser fingerprint tested at coveryourtracks.eff.org

---

## Troubleshooting

**Problem**: UFW enabled, no internet access.
**Solution**: `sudo ufw disable` to restore access. Verify your outbound allow rules (DNS port 53, HTTP 80, HTTPS 443) before re-enabling.

**Problem**: macOS application firewall blocking a needed app.
**Solution**: System Settings → Network → Firewall → Firewall Options → add an exception for the specific application.

**Problem**: Windows Update broken after firewall changes.
**Solution**: Windows Update requires TCP outbound access to Microsoft servers (ports 80, 443). If you blocked outbound, add an allow rule for the Windows Update service (`wuauclt.exe` / `svchost.exe` for Windows Update).

**Problem**: Firefox with `privacy.resistFingerprinting` breaks websites.
**Solution**: This setting changes how Firefox reports fonts, canvas, timezone, etc. Some sites detect this as unusual and break. Create a site-specific exception in Firefox's privacy settings, or temporarily disable the setting for that site.

**Problem**: BitLocker recovery key prompt appears every boot.
**Solution**: This typically means a hardware change was detected (new RAM, BIOS update, enabling Secure Boot). Enter the recovery key, then check BIOS settings — a BIOS update may have changed the Secure Boot state that BitLocker was sealed to.

---

## Sources

- [drduh: macOS Security and Privacy Guide](https://github.com/drduh/macOS-Security-and-Privacy-Guide)
- [UFW Firewall Ubuntu Guide: Complete Setup 2025](https://toolsana.com/blog/ufw-firewall-ubuntu-complete-configuration-guide/)
- [Linux Security: UFW Hardening](https://linuxsecurity.com/news/firewall/ufw-hardening)
- [Ubuntu Server Hardening 2025: AppArmor and Firewall](https://markaicode.com/ubuntu-server-hardening-2025/)
- [Windows 11 Security Hardening Practical Steps 2025](https://lorikeetsmart.com/blog/windows-security-hardening-2025.html)
- [NCSC: Windows Platform Security Guidance](https://www.ncsc.gov.uk/collection/device-security-guidance/platform-guides/windows)
- [Microsoft: Enable TPM 2.0](https://support.microsoft.com/en-us/windows/enable-tpm-2-0-on-your-pc-1fd5a332-360d-4f46-a1e7-ae6b0c90645c)
- [Privacy Guides: Desktop Browsers](https://www.privacyguides.org/en/desktop-browsers/)
- [EFF: Cover Your Tracks (Fingerprint Test)](https://coveryourtracks.eff.org)
- [Browser Fingerprinting Defense 2025](https://mr-alias.com/articles/browser-fingerprinting-defense.html)
