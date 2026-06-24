# Phase 2 Threat Model and Mitigations

**Version**: 1.0  
**Date**: June 24, 2026  
**Status**: Production-Ready  
**Framework**: EFF Surveillance Self-Defense + STRIDE + NIST

---

## Executive Summary

This document maps eight concrete threat scenarios relevant to a privacy-conscious individual with a mixed Windows+Linux personal computing environment. For each scenario, we identify the adversary capability, the attack path, the Phase 2 mitigations that reduce risk, and residual risk after Phase 2 implementation.

**Key insight**: Phase 2 does NOT eliminate risk; it raises the barrier to attack and reduces the window of exposure. An adversary with nation-state resources and legal authority will still succeed. The goal is to protect against:
- Opportunistic criminals and data brokers (encryption, backups, network segmentation)
- Corporate surveillance (VPN, DoH, Tor, encrypted backups)
- Local adversaries with temporary device access (FDE, strong passphrases, versioned backups)
- ISP/network-level surveillance (VPN, Tor, DoH)

---

## Part 1: Adversary Taxonomy

**Threat actors and their capabilities**:

| Adversary | Capability | Legal power | Time budget | Detection risk |
|---|---|---|---|---|
| **Opportunistic criminal** | Plug laptop into computer, run forensic tools, search for plaintext credentials | Low (theft, local larceny) | Minutes | High (observed by others) |
| **Data broker** | Purchase or passively collect DNS/ISP logs, build behavior profile | Medium (passive collection) | Weeks | Very low (passive) |
| **ISP / telecom provider** | Observe all traffic metadata, DNS queries, connection timing | High (state-level support) | Unlimited | Low (passive infrastructure) |
| **Cloud provider (e.g., Proton Mail, Proton Drive)** | Access unencrypted metadata (file names, email headers), scan file contents for CSAM/malware | High (government requests, ToS) | Unlimited | Low (automated scanning) |
| **Malware / advanced persistent threat (APT)** | Execute code on system with user privileges, exfiltrate data, install persistent backdoor | Very high (network access) | Days to months | Medium (network monitoring, user behavior) |
| **Law enforcement / intelligence agency** | Seize device, conduct forensic imaging, attempt passphrase recovery, demand decryption | Very high (legal warrant, subpoena) | Hours to days | N/A (adversary has legal authority) |
| **Nation-state SIGINT (NSA, GCHQ, MSS)** | Mass surveillance infrastructure, traffic correlation, zero-day exploits, targeted decryption | Highest (unlimited resources) | Unlimited | Very low (targeted surveillance is hidden) |
| **Malicious insider (ISP, hosting provider, VPN)** | Access internal systems, install packet sniffer on shared infrastructure, intercept credentials | Medium (employee access) | Unlimited | Medium (unusual access patterns detected by IDS) |

---

## Part 2: Threat Scenarios and Mitigation Maps

### Scenario 1: Stolen Laptop (Opportunistic Criminal)

**Adversary**: Local thief finds unattended laptop in coffee shop or office.

**Adversary capability**: Plug laptop into network, attempt to boot, possibly run forensic tools if thief is semi-skilled (e.g., IT professional).

**Attack path**:
1. Thief steals laptop
2. Powers it on; BIOS prompts for password (if Secure Boot + BIOS password enabled)
3. If BIOS password bypassed or not set, boots into GRUB; GRUB prompts for LUKS passphrase
4. If no LUKS encryption, thief boots to OS and searches for plaintext credentials (/home, browser cache, SSH keys)
5. If credentials found, attacker accesses email, cloud storage, financial accounts

**Mitigations (Phase 1 + Phase 2)**:

| Mitigation | Component | Residual risk | Notes |
|---|---|---|---|
| Full-disk LUKS2 encryption | LUKS2 on /dev/nvme0n1p3 + strong passphrase | Low: Brute-force via GPU possible if weak passphrase | Argon2id KDF in LUKS2 makes GPU brute-force expensive |
| Strong boot passphrase (30+ chars) | Passphrase entropy ~160 bits | Low: Nation-state resources could brute-force, but takes weeks | Most opportunistic criminals give up after 10 minutes |
| No auto-login | GRUB → LUKS → login prompt (3 auth layers) | Very low: Each layer defeats different attacks | Layered authentication |
| TPM2 sealing (optional) | TPM locks Volume Key to BIOS state | Medium: TPM can be reset or extracted; adds minimal security vs. passphrase | Useful against Evil Maid attack; not primary defense |
| Encrypted backups | restic + Proton Drive + offline USB | Very high: If device lost, data on cloud/offline drives still encrypted | Thief cannot access backed-up data even if decrypts laptop |
| **Total risk reduction** | **~90%** | **Residual**: Thief spends weeks/months attempting passphrase brute-force, or $10k+ on hardware acceleration; most give up | Most attackers are not dedicated |

**Recovery pathway**: If laptop is stolen:
1. Connect to Mullvad VPN from another device
2. Access Proton Drive and confirm restic backups are current
3. Reset passwords for email, banking, critical accounts (assume credentials may be extracted during brute-force recovery)
4. Provision new laptop with LUKS2 encryption
5. Restore /home and personal files from restic backup

### Scenario 2: Ransomware Infection (Malware)

**Adversary**: User clicks malicious link or downloads infected file; ransomware encrypts all files and demands payment.

**Adversary capability**: Code execution with user privileges. Can enumerate and encrypt files on accessible mounts.

**Attack path**:
1. User downloads or receives phishing email with malicious attachment
2. Malware executes (e.g., via unpatched browser, PDF reader, or email client)
3. Ransomware encrypts files in /home with its own key (e.g., Conti, Cl0p)
4. Attacker demands payment or data is lost

**Mitigations (Phase 2)**:

| Mitigation | Component | Residual risk | Notes |
|---|---|---|---|
| Versioned encrypted backups | restic --keep-daily 7 --keep-weekly 4 --keep-monthly 12 | Very low: Can restore from snapshot before infection | Snapshots created before malware runs |
| Offline backup on cold storage | LUKS USB in safe | Very low: Ransomware cannot access offline USB | Requires monthly manual backup |
| Immutable snapshot (optional) | Cloud provider versioning (Proton Drive) + restic snapshots | Very low: Attacker cannot modify historical snapshots | AWS S3 Object Lock equivalent: immutable backups |
| Least privilege execution | Avoid running desktop env as root; containerize untrusted apps | Medium: Malware runs as user, can still encrypt /home | Limits scope to user files, not system files |
| Email filtering + content scanning | U2F hardware key for email, anti-phishing browser extensions | Medium: User can still be socially engineered | Reduces initial infection vector |
| System monitoring (auditd, osquery) | Log all file modifications in /home | Low: Helpful for forensics, doesn't prevent infection | Used for attack analysis post-recovery |
| **Total risk reduction** | **~95%** | **Residual**: Attacker encrypts files between snapshots (e.g., ransomware installed Monday, last backup Friday); max 3 days of data loss | Increase backup frequency to daily to reduce window |

**Recovery pathway**:
1. Identify infection date (e.g., "files started getting .conti extension on Tuesday")
2. Boot from live USB (to avoid executing any rootkits)
3. Mount LUKS-encrypted drives
4. Restore /home from restic snapshot before infection date
5. Wipe system partition and reinstall OS from scratch (to remove any rootkits)
6. Run `restic check` to verify restored data is not corrupted

### Scenario 3: ISP Passive Surveillance (Network Adversary)

**Adversary**: ISP, telecom provider, or NSA-level SIGINT. Can see all traffic metadata (source IP, destination IP, port, TLS handshake, DNS queries) but not plaintext content (TLS is encrypted).

**Adversary capability**: Decades-long passive collection of metadata. Traffic analysis to infer user behavior and interests.

**Attack path**:
1. Attacker intercepts all packets on user's ISP link
2. Extracts DNS queries (e.g., "lookup example.com", "lookup banking-app.com")
3. Observes connection patterns (timing, duration, frequency)
4. Builds behavioral profile: when user works, sleeps, browses banking sites, contacts, etc.

**Mitigations (Phase 2)**:

| Mitigation | Component | Residual risk | Notes |
|---|---|---|---|
| VPN (Mullvad/IVPN) + kill-switch | Encrypt all traffic through VPN tunnel | Medium: ISP sees "traffic to VPN server on port UDP/1194" but not destination | VPN provider now knows destination, but ISP does not |
| DNS-over-TLS | systemd-resolved with DoT to Cloudflare | Medium: ISP sees "traffic to 1.1.1.1:853" (Cloudflare DNS) but not DNS queries | DNS queries now encrypted; ISP cannot see which sites you visit |
| Tor for high-sensitivity comms | Tor Browser for financial/medical/sensitive research | Very low: Tor encrypts, obfuscates entry point, mixes traffic | Slower than VPN; use for highest-sensitivity activities |
| Avoid predictable patterns | Randomize browsing times, use scheduled VPN connections | Low: Behavioral patterns are still observable (e.g., "user connects 9-5 on weekdays") | Cannot eliminate pattern analysis without active deception |
| Disable IPv6 (if VPN IPv4-only) | sysctl net.ipv6.conf.all.disable_ipv6=1 | Very low: Prevents IPv6 leaks (not encrypted by most VPNs) | IPv6 traffic bypasses VPN tunnel on misconfigured systems |
| **Total risk reduction** | **~85%** | **Residual**: Metadata still observable (VPN server IP, connection timing, traffic volume). Timing attacks and traffic analysis can still infer user activity | ISP + VPN provider colluding can still infer behavior; nation-state with backbone wiretaps can still do traffic correlation |

**Example**: User connects to Mullvad at 09:00, stays connected 8 hours, then disconnects. ISP sees only "connection to nl-ams-wg-401.mullvad.net" but not user's actual web traffic. If Mullvad logs VPN traffic, user is deanonymized; but Mullvad claims no-logs. If nation-state does traffic correlation across all internet backbone links, they can still infer user destination IPs via statistical analysis (difficult but theoretically possible).

### Scenario 4: Cloud Provider Content Scanning (Corporate Surveillance)

**Adversary**: Proton Drive, Google Drive, Dropbox, or similar cloud provider. Legally required or incentivized to scan file contents for CSAM, malware, copyrighted material.

**Adversary capability**: Scan unencrypted or partially encrypted files (e.g., scan metadata, sometimes file contents depending on T&C and legal jurisdiction). File names are visible unless client-side encrypted.

**Attack path**:
1. User stores files on Proton Drive (encrypted by Proton in transit and at rest, but Proton has access to encryption keys)
2. Proton (or government agency via subpoena) scans file contents
3. Files are flagged as CSAM/malware and reported to law enforcement or deleted
4. Or: user's privacy dossier is built from file names, access patterns, and metadata

**Mitigations (Phase 2)**:

| Mitigation | Component | Residual risk | Notes |
|---|---|---|---|
| Client-side encryption (restic AES-256) | restic encrypts before uploading to Proton Drive | Very low: Cloud provider sees only encrypted blobs, not plaintext files | Proton cannot scan encrypted data |
| File name obfuscation | restic backup (no plaintext filenames, only snapshot IDs) | Very low: File names encrypted and hidden by restic; only metadata is "backup snapshot" | Even Proton doesn't know what files you're backing up |
| Encrypted container (VeraCrypt) | Sensitive files in VeraCrypt container, backup container to cloud | Low: Container file itself is plaintext in cloud, but contents are encrypted | Cloud provider can see container file exists, but not contents |
| **Total risk reduction** | **~98%** | **Residual**: Proton can see that backup is happening (connection to Proton servers is visible), but not the contents. Metadata (backup size, frequency) is still visible | If subpoenaed, Proton must deliver encrypted backups; decryption requires restic password or breaks AES-256 |

**Example**: User backs up sensitive medical records to Proton Drive via restic:
- Plaintext scenario: Proton scans file and sees "patient_name_2023_cancer_diagnosis.pdf", reports to Proton for CSAM/malware scanning, and file is flagged or flagged as suspicious. User's privacy is compromised.
- Encrypted scenario (restic): Proton sees only "5a3b2c1d_encrypted_blob.bin"; cannot determine contents. CSAM/malware scanning cannot determine if contents are illegal. User's privacy is protected by encryption.

### Scenario 5: Physical Search or Border Seizure (Law Enforcement)

**Adversary**: Police, border agents, or customs officer. Has legal authority to seize device and may demand decryption.

**Adversary capability**: Physical access to device for hours to days. Can use forensic tools, attempt passphrase extraction via keylogger or rubber-hose cryptanalysis (torture), or demand decryption under duress.

**Attack path**:
1. User is arrested or stopped at border; device is seized
2. Law enforcement interrogates user and demands passphrase
3. If user refuses, law enforcement uses forensic imaging (bitwise copy of storage) to attempt brute-force offline
4. If brute-force fails and user still refuses, user may be prosecuted for contempt of court (in some jurisdictions)

**Mitigations (Phase 2)**:

| Mitigation | Component | Residual risk | Notes |
|---|---|---|---|
| Strong passphrase (30+ characters) | LUKS2 passphrase with 160+ bits entropy | Very low: Brute-force would take centuries on current hardware | Assumes user doesn't crack under interrogation |
| Argon2id KDF (GPU-resistant) | LUKS2 default uses Argon2id, not PBKDF2 | Very low: GPU/ASIC acceleration is ineffective against Argon2id | Makes offline brute-force impractical even for law enforcement |
| Multi-keyslot strategy | Keyslot 0 (daily passphrase) + Keyslot 1 (recovery key in safe, 30+ chars) | Medium: Recovery key can also be brute-forced, but twice the work | Provides independent recovery path if main passphrase forgotten |
| VeraCrypt hidden volume (optional) | Create hidden volume within VeraCrypt container; two passphrases | Very low: Plausible deniability; hidden volume undetectable without knowledge of passphrase | Allows denying existence of certain files; risky if law enforcement suspects hidden volume |
| Biometric unlock rejection | Do not use fingerprint/face recognition as primary unlock | High: Biometrics can be extracted under duress (force user to put finger on scanner) | Passphrase-only requires user's knowledge, not their body |
| Device wipe (optional, extreme) | Pre-travel: wipe sensitive data, restore from backup post-travel | Low: Requires user to identify as suspicious; may trigger additional interrogation | Allows denying possession of certain data if questioned |
| **Total risk reduction** | **~75%** | **Residual**: Law enforcement with sophisticated hardware could brute-force Argon2id over weeks. User can be compelled to decrypt under duress (in some jurisdictions, contempt-of-court penalties apply). Biometric extraction is possible | Jurisdictional variation: US Fifth Amendment protects passphrase knowledge; UK/Canada may compel decryption under RIPA/PIPEDA. Consult lawyer |

**Example (US scenario)**: User is arrested with laptop. Law enforcement demands passphrase. User refuses (invokes Fifth Amendment). Law enforcement images storage, attempts offline brute-force for 2 weeks, then closes investigation (brute-force too expensive). User is released if no other evidence. Laptop may not be returned (civil forfeiture risk).

**Example (UK scenario)**: User is arrested with laptop. Law enforcement demands passphrase under UK RIPA (Regulation of Investigatory Powers Act). User refuses. User can be prosecuted for contempt of court (5+ years imprisonment) regardless of whether contents are illegal. This is a legal, not technical, risk.

### Scenario 6: Local Privilege Escalation (Malware / Insider Attack)

**Adversary**: Malware with user privileges, or insider on shared system (e.g., roommate, family member) who gains root access.

**Adversary capability**: Execute code with root privileges. Can read all files on system, install rootkits, exfiltrate data via background process.

**Attack path**:
1. Malware exploits unpatched kernel vulnerability (CVE-2023-XXXX) to escalate from user to root
2. Malware disables audit logging, modifies /etc/shadow to add backdoor account
3. Malware starts data exfiltration: copies /home, SSH keys, browser caches to attacker's C&C server
4. User is unaware of compromise for weeks until detecting unusual network traffic

**Mitigations (Phase 2)**:

| Mitigation | Component | Residual risk | Notes |
|---|---|---|---|
| Unattended-upgrades | Automatic kernel patching via Ubuntu security updates | Very low: 0-day exploits still possible; delays time to patching | Reduces window of exploitability for known CVEs |
| AppArmor or SELinux | Mandatory access control (MAC) policies limit what root can do | Medium: Misconfigured policies can be bypassed; adds operational complexity | Ubuntu enables AppArmor by default; can constrain malware |
| File integrity monitoring (AIDE/Tripwire) | Detect unauthorized changes to system files | Low: Helpful for forensics, not prevention | Alerts user to rootkit installation post-infection |
| Immutable logs | chattr +i /var/log/auth.log prevents deletion (requires root + unset immutable first) | Low: Determined attacker can disable immutability and delete logs | Discourages log tampering but doesn't prevent it |
| Containerization | Run untrusted applications in Docker with limited mounts | Medium: Requires discipline; easy to mount /home in container and break isolation | Useful for high-risk applications (PDF readers, email clients) |
| Cold backups offline | Offline restic snapshots cannot be exfiltrated | Very high: If backups are on cold USB in safe, malware cannot reach them | Even if current system compromised, historical backups are safe |
| **Total risk reduction** | **~70%** | **Residual**: Sophisticated malware can still achieve root via 0-day, disable security controls, and exfiltrate data. Cannot prevent root compromise entirely | Assume attacker gets root eventually; rely on offline backups as recovery mechanism |

**Recovery pathway**:
1. Detect signs of compromise (unusual network traffic, process list, system behavior)
2. Boot from live USB (to avoid executing compromised kernel)
3. Mount LUKS drives and backup to external USB
4. Wipe system partition and reinstall OS from scratch (from Ubuntu official ISO)
5. Restore /home and applications from restic backup
6. Rebuild from clean install to eliminate rootkits

### Scenario 7: VPN/DNS Provider Compromise (Malicious Insider)

**Adversary**: Rogue employee at Mullvad, Proton, Cloudflare, or ISP with access to internal systems. Can install packet sniffer, modify logs, or intercept credentials.

**Adversary capability**: Intercept traffic at VPN/DNS provider level; decrypt VPN traffic (if provider keeps decryption keys); modify DNS responses; log IP addresses despite no-log policy.

**Attack path**:
1. Disgruntled Mullvad employee installs tcpdump on VPN gateway server
2. For user X (identified by residential IP + payment info), captures all decrypted traffic
3. Exfiltrates captured data to personal cloud storage
4. User is unaware that VPN is not protecting them

**Mitigations (Phase 2)**:

| Mitigation | Component | Residual risk | Notes |
|---|---|---|---|
| No-log audits | Third-party audits (Cure53, Securitum) of VPN provider code and infrastructure | Low: Audits are point-in-time snapshots; cannot detect real-time insider threats | Mullvad/IVPN have strong audit track records |
| Multi-hop / chained VPN | Route through two independent VPN providers (slow, complex) | Very low: Insider at one provider doesn't correlate traffic with other provider | Requires running two VPN clients; significant latency penalty |
| Tor (instead of VPN) | Use Tor Browser for high-sensitivity traffic | Medium: Tor is slower; exit node can still see plaintext traffic if not HTTPS | Traffic is anonymized at Tor level, not endpoint-visible |
| Encrypted application layer | Use HTTPS, E2EE messaging, encrypted email (Signal, ProtonMail) | Very high: Even if VPN is compromised, application-level encryption protects content | Cannot prevent metadata (IP, timing) from being visible |
| Threat modeling assumption | Assume VPN provider is compromised for threat modeling purposes | Medium: Difficult to design without trust; requires Tor or encrypted applications | Conservative approach: design for untrusted VPN |
| **Total risk reduction** | **~80%** | **Residual**: Insider at VPN provider can still see your IP address and timing. Metadata (IP, ports, connection duration) is still visible. Cannot prevent insider access entirely | Only Tor + encrypted applications fully protects against VPN insider |

**Example**: User connects to Mullvad for privacy while accessing banking website. Mullvad insider captures traffic and sees:
- User IP (192.168.1.100)
- Destination IP (bank.com's server IP)
- TLS handshake (indicates encrypted connection to bank.com)
- Timing (connection lasts 30 minutes)
- BUT NOT: password, account balance, or any plaintext content (TLS encryption protects this)

Result: Insider knows user accessed banking site at certain time, but not the specific transaction details (unless insider also compromises bank server).

### Scenario 8: Device Loss + Account Takeover (Multi-Factor Failure)

**Adversary**: Theft or loss of laptop + temporary access to email (e.g., email password reused on stolen device, email account recovered via SMS interception).

**Adversary capability**: Device access + email access = ability to reset passwords on all linked services (banking, cloud storage, email provider).

**Attack path**:
1. Laptop is stolen and quickly powered on
2. Thief guesses or cracks LUKS passphrase (weak passphrase scenario)
3. Thief accesses browser caches and finds email client passwords or browser auto-fill credentials
4. Thief logs into email account
5. Thief uses email to reset passwords on banking, cloud storage, social media
6. Attacker locks user out and exfiltrates data

**Mitigations (Phase 2 + Phase 1)**:

| Mitigation | Component | Residual risk | Notes |
|---|---|---|---|
| Strong LUKS passphrase (30+ chars) | LUKS2 encryption with 160+ bit entropy | Low: Brute-force would take weeks; thief gives up | Slowdown buys time for user to detect loss |
| Hardware security key (U2F) | YubiKey 5 for email + banking | Very low: 2FA via USB key is resistant to online attacks | Requires user to purchase and register hardware key |
| Email recovery codes (offline) | Printed recovery codes stored in safe (not on device) | Very low: Even if email is compromised, recovery codes prevent permanent lockout | Requires manual setup and secure storage |
| Bitwarden password manager (unique passwords) | Each service has unique, random 30+ char password | Very high: If email is compromised, thief cannot reset other services (each has different password) | Assumes thief cannot access Bitwarden vault |
| Bitwarden vault encryption | Master password (separate from email password) | Very high: Vault is encrypted locally; even if device stolen, vault cannot be accessed without master password | Thief must crack Bitwarden + LUKS + email password (three independent unknowns) |
| Immediate account freeze | User notices loss quickly, calls bank and email provider | Low: Requires user to detect loss within minutes | Most users detect within hours; damage is limited |
| Transaction monitoring | Bank alerts user to unusual activity (geographic, amount, time) | Low: Alerts are reactive; attacker may exfiltrate data before detection | Helps with incident response, not prevention |
| Offline recovery codes | Email recovery codes stored offline (not in cloud, not on device) | Very low: If all online access is compromised, recovery codes allow account recovery | Requires user discipline to store securely |
| **Total risk reduction** | **~90%** | **Residual**: If thief can crack LUKS + email password + Bitwarden master password (three layers), full account takeover is possible. Unlikely unless thief is very sophisticated or user has weak passwords | Layered authentication makes attack very difficult |

**Recovery pathway**:
1. Detect loss (phone gets suspicious email notification, unusual account access)
2. Immediately change passwords for email, banking, critical services from another device
3. Enable 2FA with hardware security key if not already enabled
4. Check Bitwarden (cloud version) to confirm no new passwords added
5. Contact bank to dispute any fraudulent transactions
6. File police report for stolen device
7. Once located, wipe old device remotely (if device tracking enabled)

---

## Part 3: Threat Model Summary Table

| Scenario | Adversary | Attack type | Phase 2 defense | Risk reduction | Residual risk |
|---|---|---|---|---|
| 1. Stolen laptop | Opportunistic criminal | Physical + brute-force | FDE (LUKS2) + encrypted backups | ~90% | GPU brute-force over weeks |
| 2. Ransomware | Malware / APT | Code execution + encryption | Versioned backups + offline USB | ~95% | 3-day window between backups |
| 3. ISP surveillance | Network adversary | Passive metadata collection | VPN + DoH + Tor | ~85% | Timing/traffic volume still visible |
| 4. Cloud provider scanning | Corporate entity | Content scanning + metadata analysis | Client-side encryption (restic AES-256) | ~98% | File names still visible to attacker |
| 5. Border seizure | Law enforcement | Physical seizure + interrogation | Strong passphrase + Argon2id KDF | ~75% | Compulsion via legal duress |
| 6. Privilege escalation | Malware / insider | 0-day kernel exploit → root | Unattended-upgrades + offline backups | ~70% | Root compromise still possible via 0-day |
| 7. VPN insider | Malicious employee | VPN provider compromise | Encrypted applications (HTTPS, E2EE) | ~80% | Metadata (IP, timing) still visible |
| 8. Device loss + account takeover | Thief + email compromise | Multi-factor password reset | Hardware 2FA + unique passwords + Bitwarden | ~90% | Requires cracking 3 independent layers |

---

## Part 4: Threat Model by Adversary Capability

### Low-Capability Adversary (Opportunistic Criminal)

**Threats mitigated by Phase 2**:
- Stolen laptop: FDE prevents plaintext file access
- Ransomware: Versioned backups enable recovery without paying ransom
- Account takeover: Unique passwords + Bitwarden prevent lateral movement

**Risk: ~5-10% after Phase 2**  
*Reasoning*: Opportunistic criminals lack the sophistication or resources for brute-force attacks or 0-day exploits. FDE + backups eliminate their primary attack vectors.

### Medium-Capability Adversary (Organized Crime, Corporate Espionage)

**Threats mitigated by Phase 2**:
- ISP surveillance: VPN + DoH hides browsing patterns
- Cloud scanning: Client-side encryption (restic) hides file contents
- Privilege escalation: Offline backups provide recovery even if system compromised

**Risk: ~10-20% after Phase 2**  
*Reasoning*: Medium-capability adversaries have limited budgets and cannot conduct extended brute-force or develop 0-day exploits. VPN + encryption raise the barrier significantly.

### High-Capability Adversary (Law Enforcement, Nation-State SIGINT)

**Threats mitigated by Phase 2**:
- Border seizure: Strong passphrase + Argon2id delays brute-force by weeks to months
- Network surveillance: VPN + Tor reduces fingerprinting and timing analysis
- Account takeover: Hardware 2FA makes remote password reset impossible

**Risk: ~30-50% after Phase 2**  
*Reasoning*: Nation-state adversaries have unlimited resources (supercomputers, zero-days, legal authority) and can eventually decrypt LUKS or subpoena cloud providers. Phase 2 delays attack but does not eliminate risk. The goal is to make the cost of attack proportional to the value of the target. If you are a journalist or dissident, nation-state targeting is possible; Phase 2 raises the barrier but doesn't make you immune.

---

## Part 5: Cross-Scenario Protection Matrix

**Rows**: Phase 2 components; **Columns**: Threat scenarios

|  | Laptop theft | Ransomware | ISP surveillance | Cloud scanning | Border seizure | Privilege escalation | VPN insider | Account takeover |
|---|---|---|---|---|---|---|---|---|
| LUKS2 FDE | ●●● | ◐ | ◐ | ◐ | ●●● | ◐ | ◐ | ◐ |
| Strong passphrase | ●●● | ◐ | ◐ | ◐ | ●● | ◐ | ◐ | ◐ |
| Encrypted backups (restic) | ●● | ●●● | ◐ | ●●● | ●● | ●●● | ◐ | ◐ |
| Offline USB backups | ◐ | ●●● | ◐ | ●●● | ●● | ●●● | ◐ | ◐ |
| VPN + DoH | ◐ | ◐ | ●●● | ◐ | ◐ | ◐ | ●● | ◐ |
| Tor Browser | ◐ | ◐ | ●● | ◐ | ◐ | ◐ | ●● | ◐ |
| Hardware 2FA (U2F) | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ●●● |
| Unique passwords (Bitwarden) | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ●●● |
| Unattended-upgrades | ◐ | ◐ | ◐ | ◐ | ◐ | ●● | ◐ | ◐ |
| Email recovery codes (offline) | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ●● |

**Legend**:
- ●●●: Highly effective (80%+ risk reduction)
- ●●: Moderately effective (50-80% risk reduction)
- ●: Somewhat effective (20-50% risk reduction)
- ◐: Minimal protection (< 20% risk reduction)

---

## Part 6: Detection and Response

### Threat Detection Indicators

| Threat | Detection signal | Response action | Time to respond |
|---|---|---|---|
| Ransomware infection | File extensions change, processes using high CPU, disk I/O spikes | Boot live USB, restore from offline backup | 30 minutes |
| Malware / rootkit | Unusual network traffic (outbound to unknown IPs), modified system files, suspicious processes | Forensic imaging (bitwise copy to external USB), wipe and reinstall OS | 2-4 hours |
| Password brute-force | SSH login failures in /var/log/auth.log | Block IP via firewall, enable fail2ban, rotate SSH keys | 10 minutes |
| Privilege escalation attempt | Unrecognized process with root privileges, modified sudo logs | Audit logs, check for backdoor accounts, kill malicious process | 15 minutes |
| VPN disconnection | IP address changes from VPN IP back to home ISP IP | Kill-switch blocks traffic, reconnect to VPN | Automatic (< 1 second) |
| Backup failure | Restic check failure, systemd journal shows "error", no new snapshots in 24 hours | Check Proton Drive connection, verify rclone auth, manually run restic backup | 30 minutes |

### Incident Response Plan (Post-Compromise)

1. **Detect** (0-30 min):
   - Monitor system logs for indicators (failed logins, unauthorized processes, file modifications)
   - Run `restic check` to verify backup integrity
   - Check `systemctl status restic-backup` for failures

2. **Isolate** (30-60 min):
   - Disconnect from network (unplug Ethernet or disable WiFi)
   - Do NOT trust any running processes; boot from live USB
   - Power off device

3. **Evaluate** (1-2 hours):
   - From live USB, mount LUKS drives
   - Run `restic snapshots` to identify last clean backup
   - Determine attack surface (ransomware vs. rootkit vs. data exfiltration)

4. **Recover** (2-6 hours):
   - For ransomware: restore entire /home from clean snapshot
   - For rootkit: wipe system partition, reinstall OS from scratch, restore /home
   - For data exfiltration: assume breach; reset all passwords; enable 2FA on critical accounts

5. **Rebuild** (6-24 hours):
   - Reinstall applications and dependencies
   - Restore personal files from restic backup
   - Re-enable monitoring (auditd, systemd-journalctl alerts)

6. **Harden** (Post-incident):
   - Audit what went wrong (weak password? unpatched software? phishing link?)
   - Implement additional controls to prevent recurrence
   - Review backups to ensure no malware was backed up (run antivirus scan on restored files)

---

## Part 7: Integration with Phase 1 (Windows)

### Windows + Linux Unified Threat Model

**Phase 1 (Windows)**:
- VeraCrypt full-disk encryption
- BitLocker (if available)
- Windows Defender + MalwareBytes
- Windows Update auto-patching

**Phase 2 (Linux)**:
- LUKS2 full-disk encryption
- Encrypted backups to Proton Drive (shared with Windows)
- UFW firewall + VPN kill-switch
- Tor Browser for sensitive research

**Cross-system threat scenarios**:

| Scenario | Windows mitigation | Linux mitigation | Combined effect |
|---|---|---|---|
| **Stolen laptop** | VeraCrypt FDE + BIOS password | LUKS2 FDE + passphrase | Attacker cannot access either OS |
| **Cloud account compromise** | OneDrive recovery codes stored offline | Proton Drive credentials in Bitwarden (encrypted) | Both cloud accounts protected |
| **ISP surveillance** | Windows VPN (ProtonVPN) | Linux VPN (Mullvad) + DoH | Both systems route through encrypted VPN tunnel |
| **Network malware** | Windows Defender scans incoming traffic | UFW firewall blocks unexpected connections | Defense-in-depth |
| **Ransomware on either OS** | OneDrive versioning (cloud) | restic versioned backups (cloud + USB) | Recovery possible from cloud or offline backups |

---

## Part 8: Limitations and Assumptions

### What Phase 2 Does NOT Protect Against

1. **Nation-state targeted encryption**: If NSA specifically targets you with custom malware or legal authority to demand decryption, Phase 2 provides limited protection. The goal is to make you "too expensive to target", not to make you immune.

2. **Physical coercion**: If law enforcement can compel you to decrypt under legal duress (RIPA in UK) or physical threat, Phase 2 cannot help. This is a legal/political problem, not a technical one.

3. **Weak passphrase**: If your boot passphrase is "password123", all other security measures are circumvented. User discipline is mandatory.

4. **Compromised backup password**: If someone gains your restic repository password, they can restore data from cloud backups. Store this password as carefully as your LUKS passphrase.

5. **Biometric extraction**: If law enforcement can force you to put your finger on the fingerprint scanner, biometric 2FA is bypassed. Phase 2 recommends passphrase-only unlock for high-risk scenarios.

6. **Supply-chain compromise**: If your laptop manufacturer installs malware at the factory (rare but documented for targeted individuals), Phase 2 cannot detect it. This is a procurement/verification issue.

### Assumptions

- **User has moderate Linux competency**: Can follow documentation, troubleshoot basic issues, read logs.
- **User can afford $20/month** for VPN + cloud backup.
- **User is not specifically targeted by nation-state**: Phase 2 is designed for opportunistic criminals, corporate surveillance, and ISP-level adversaries.
- **User has physical access to a safe** for storing recovery keys and offline backups.
- **User will test recovery procedures** at least once before relying on them.
- **User will rotate passwords** and keep systems patched (unattended-upgrades helps).

---

## Part 9: Metrics and Monitoring

### Key Performance Indicators (KPIs)

| Metric | Target | Frequency | Action if missed |
|---|---|---|---|
| Backup success | 100% (all snapshots complete) | Daily | Email alert; manual backup within 24 hours |
| Backup integrity | `restic check` passes | Monthly | Investigate Proton Drive API issue; test restore |
| Passphrase tested | Successful boot at least once | Quarterly | Update recovery key if passphrase changed |
| Recovery key verified | Can decrypt LUKS using recovery key | Annually | Regenerate recovery key; update offline copies |
| VPN kill-switch tested | Connectivity lost when VPN disconnects | Quarterly | Audit UFW rules; test on new OS update |
| System patches current | All security updates installed | Weekly | `sudo apt upgrade` (unattended-upgrades) |
| Hardware 2FA working | Can authenticate to critical accounts | Monthly | Test login to banking, email with U2F |

### Monitoring Tools

- **Systemd journal**: `journalctl -u restic-backup -f` (monitor backup logs)
- **Prometheus + Alertmanager**: (optional) scrape restic metrics, alert on backup failure
- **Auditd**: Log all system calls to /var/log/audit (helpful for forensics post-compromise)
- **Fail2ban**: Automatically block IPs with repeated SSH failures
- **Checkrestart**: Detect daemons that need restarting after kernel update (`checkrestart -b`)

---

## Part 10: Threat Model Revision Schedule

| Review period | Trigger | Action |
|---|---|---|
| Quarterly | Automated (calendar) | Review new CVEs, update unattended-upgrades, test recovery procedures |
| On major OS update | Ubuntu 24.04 → 26.04 LTS (2 years) | Re-validate LUKS, VPN, backup procedures on new kernel/services |
| On security incident (external) | New malware family, zero-day, new attack pattern | Analyze applicability to Phase 2; implement additional controls if needed |
| On security incident (internal) | Compromise, failed backup, misconfiguration discovered | Post-mortem; update documentation; revise threat model to cover the attack vector |

---

## Conclusion

Phase 2 infrastructure raises the barrier to attack from opportunistic criminals (90% risk reduction) to medium-capability adversaries (85% risk reduction for network surveillance). Against high-capability adversaries (nation-state), residual risk remains significant (50%+ after Phase 2); however, the goal is not to achieve zero risk but to make the cost of attacking you proportional to your perceived value.

The hierarchy of protections is:

1. **Encryption at rest** (LUKS2 FDE) — protects against physical theft
2. **Encryption in flight** (VPN + DoH) — protects against network surveillance
3. **Encrypted backups** (restic AES-256) — enables recovery from malware/disaster
4. **Layered authentication** (LUKS + passphrase + 2FA) — prevents unauthorized access
5. **Offline recovery** (cold storage keys, printed recovery codes) — enables recovery even if all online systems compromised

Implement these in order; each layer independently provides value. Quarterly testing of recovery procedures is essential; untested backups are a false sense of security.

---

**End of Phase 2 Threat Model and Mitigations**
