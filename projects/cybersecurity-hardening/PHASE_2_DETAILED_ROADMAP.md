---
title: "Phase 2 Detailed Implementation Roadmap — Personal OpSec"
project: cybersecurity-hardening
created: 2026-05-19
status: ready-for-review
target-review-date: 2026-05-25
depends-on: PHASE_1_NEXT_STEPS_GUIDE.md (Phase 1 must be complete before starting Phase 2)
threat-model: government/mass surveillance + targeted harassment + corporate tracking
devices: Windows (primary), iPhone, Linux
---

# Phase 2 Detailed Implementation Roadmap

**Bottom line**: Phase 1 put you in the 85th percentile of personal security. Phase 2 closes the remaining gaps — always-on traffic encryption, phishing-proof authentication, persistent identity fragmentation, communication metadata minimization, physical counter-surveillance, organizational breach resilience, and a quarterly review practice that keeps everything current. This document turns the Phase 2 outline into executable, step-by-step guidance across all 7 modules.

**How to use this document**: Read Section 1 (scope and timeline) before starting. Then follow the module sequence in Section 3 based on your threat model. Each module in Section 2 is self-contained — you can execute them independently once prerequisites are met.

---

## Section 1: Phase 2 Scope and Timeline

### Summary

Phase 2 covers 7 modules delivered over approximately 3 weeks at 4–5 hours per week. The total time investment is 12–15 hours of active setup work. After that, maintenance drops to roughly 15 minutes per month.

**Phase 1 completion prerequisite**: Phase 2 should begin only after Phase 1 steps 1.1–1.7 are complete and verified. Based on current status (Step 1.3 restart pending), Phase 1 completion is estimated around June 1–2, 2026. Phase 2 start target: June 2–3, 2026.

**Phase 2 completion target**: Mid-June 2026 (approximately June 14–18, 2026).

**Total cost range**:
- Minimum (open-source, manual): $55–75 (VPN only)
- Moderate (VPN + 2 security keys + data broker automation): $200–250
- Comprehensive (all tools, redundant hardware): $350–500

### Module Sequencing Overview

Modules are not all independent. The dependency chain is:

1. **Module 1** (device encryption) — must complete first; other modules assume an encrypted device
2. **Module 2** (hardware security keys + MFA) — can start in parallel with Module 1 after ordering hardware
3. **Module 3** (network anonymization) — can start immediately; no dependencies
4. **Module 4** (metadata minimization) — can start immediately; no dependencies
5. **Module 5** (physical security) — can start immediately; behavioral and no hard dependencies
6. **Module 6** (organizational OpSec) — should follow Module 2 (credential management is a prerequisite)
7. **Module 7** (threat model refresh + continuous improvement) — follows all other modules; also runs as an ongoing practice

### Risk Assessment: External Dependencies

- **Hardware delivery (Module 2)**: YubiKey ships in 2–5 business days from Yubico.com. Order on Day 1 of Phase 2. This is your longest external dependency.
- **Data broker removal (Module 4)**: Automated removal services begin processing immediately but full removal takes 2–4 weeks. Not a blocker — start the service and continue other modules.
- **VPN account setup (Module 3)**: Mullvad anonymous payment by physical cash mail takes 5–10 days. Use prepaid Visa card as bridge until cash is processed.
- **Apple security key registration (Module 2)**: Apple requires a paired trusted device to be present. No external dependency, but budget extra 30 minutes.

### Recommended 3-Week Calendar

| Week | Days | Module | Key Action | Time |
|------|------|--------|-----------|------|
| Week 1 | Days 1–2 | 3 | Set up Mullvad VPN on Windows + iPhone | 1.5 hrs |
| Week 1 | Day 1 | 2 | Order 2x YubiKey 5 NFC | 10 min |
| Week 1 | Days 3–5 | 4 | Signal hardening + email aliases | 2 hrs |
| Week 1 | Days 4–7 | 5 | Physical security habits + location review | 1 hr |
| Week 2 | Days 8–10 | 2 | Register YubiKeys on all critical accounts | 2 hrs |
| Week 2 | Days 9–12 | 1 | VeraCrypt containers + Mac/Linux encryption audit | 2 hrs |
| Week 2 | Days 11–14 | 6 | Credential compartmentalization + breach protocol | 1.5 hrs |
| Week 3 | Days 15–18 | 6 | Incident response dry run | 1 hr |
| Week 3 | Days 19–21 | 7 | Threat model refresh + quarterly review protocol | 1 hr |

---

## Section 2: Module-by-Module Breakdown

---

### Module 1: Device-Level Encryption and Full-Disk Protection

#### Overview

Phase 1 handled Windows BitLocker and iPhone Advanced Data Protection. Module 1 closes the remaining device encryption gaps: VeraCrypt encrypted containers for highly sensitive files, macOS FileVault if the user also has a Mac, Linux LUKS configuration, and encrypted external drives. The goal is zero plaintext sensitive data on any storage medium — if a device is seized while powered off, nothing is recoverable without the passphrase.

**Why this matters for your threat model**: FBI and federal law enforcement conduct device seizures. Full-disk encryption means a powered-off seized device yields nothing without your passphrase. Importantly, the Fifth Amendment protects you from being compelled to reveal a passphrase (unlike biometrics — they CAN compel Face ID). Without encryption, any powered-off device is readable in minutes with commodity forensics tools (Cellebrite, FTK).

#### User Prerequisites

- Phase 1 Step 1.3 complete (Windows VeraCrypt pre-boot encryption running or BitLocker active)
- Bitwarden password manager set up (Phase 1 Step 1.5) for passphrase storage
- Recovery codes from Phase 1 stored securely

#### Step-by-Step Implementation

**Part A: Verify Phase 1 encryption is actually running**

1. Open Windows Start menu → search "Manage BitLocker" → verify C: drive shows "BitLocker on" with a lock icon. If it shows "BitLocker suspended" you need to resume it: click "Resume protection."
2. If you used VeraCrypt pre-boot: restart your computer and verify the VeraCrypt password prompt appears before Windows loads. If Windows loads directly, your VeraCrypt encryption is not active — return to PERSONAL_OPSEC_PLAN.md Step 1.3.
3. On iPhone: Settings → [your name] → iCloud → Advanced Data Protection → should show "On." If not, complete Phase 1 Step 1.2 first.

**Part B: Create an encrypted VeraCrypt container for sensitive files**

This is different from full-disk encryption — it creates a single encrypted file that acts as a virtual drive. Use this for especially sensitive documents (legal files, financial records, private keys).

4. Download VeraCrypt from https://veracrypt.fr/en/Downloads.html — verify the checksum on the download page before installing.
5. Open VeraCrypt → click "Create Volume."
6. Select "Create an encrypted file container" → click Next.
7. Select "Standard VeraCrypt volume" → click Next.
8. Choose where to save the container file. Name it something neutral like "archive.vc" and save it on your Desktop or Documents. Click Next.
9. Leave encryption at "AES" and hash at "SHA-512" — these are strong defaults. Click Next.
10. Set the container size. For most users: 5 GB is sufficient for documents, keys, and records.
11. Set a strong passphrase. This should be different from your BitLocker/VeraCrypt pre-boot passphrase. 20+ characters, random words or a memorable phrase. Save it in Bitwarden under "VeraCrypt container passphrase."
12. Move your mouse randomly inside the VeraCrypt window for 30 seconds to generate entropy, then click "Format." This creates the container.
13. To open the container: VeraCrypt → "Select File" → choose your container → "Mount" → enter passphrase → it appears as a drive letter in Windows Explorer. Drag sensitive files in. When done: VeraCrypt → "Dismount."
14. Store your most sensitive files here: GPG keys, credential recovery codes, legal documents, financial records.

**Part C: macOS FileVault (if you use a Mac)**

15. System Settings → Privacy & Security → FileVault → "Turn On."
16. Choose "Create a recovery key and do not use my iCloud account" — write the recovery key on paper and store it physically separate from the Mac. Do not store it in iCloud or email.
17. FileVault will encrypt in the background — takes 1–3 hours on a modern SSD. Mac can be used during encryption.

**Part D: Linux full-disk encryption (if you use Linux)**

18. If you're installing Linux fresh: during installation, select "Encrypt the installation" or "Use LVM with encryption." This installs LUKS full-disk encryption. Choose a strong passphrase.
19. If Linux is already installed without encryption: migrating an existing unencrypted install to LUKS requires a full reinstall. If this machine holds sensitive data, back it up, reinstall with encryption enabled, restore data.
20. Verify LUKS is active: open a terminal and run `lsblk -f` — you should see type "crypto_LUKS" on your main partition.
21. Set automatic screen lock: Settings → Privacy → Screen Lock → enable, set timeout to 5 minutes.

**Part E: Encrypted external drives**

22. For any USB drives storing sensitive data: use VeraCrypt to create a full-volume encrypted drive. VeraCrypt → Create Volume → "Encrypt a non-system partition/drive" → select the USB drive → set passphrase. This wipes the drive, so back it up first.

#### Key Decisions and Trade-offs

- **BitLocker vs. VeraCrypt for full-disk**: BitLocker (if already set up in Phase 1) is fine for your threat model. VeraCrypt is open-source and auditable but requires more user management. Use BitLocker for your primary disk, VeraCrypt containers for highly sensitive files.
- **Container vs. full-disk**: For most users, full-disk encryption (Phase 1) covers 90% of the risk. Containers add protection for files you specifically don't want visible even to someone with your Windows login password.
- **Passphrase complexity**: 20+ character random passphrases resist brute-force attacks. Shorter passphrases (under 15 characters) can be cracked with modern GPU rigs in weeks if the encrypted volume is captured.

#### Tools and Resources

| Tool | Cost | Open Source | Notes |
|------|------|-------------|-------|
| VeraCrypt | Free | Yes | Windows/Mac/Linux; audited 2016, maintained |
| BitLocker | Free (Win Pro) | No | Microsoft; requires Windows Pro or higher |
| macOS FileVault | Free | No | Apple; built into macOS |
| Linux LUKS | Free | Yes | Built into modern Linux installers |

- VeraCrypt download + checksums: https://veracrypt.fr/en/Downloads.html
- VeraCrypt documentation: https://veracrypt.fr/en/Documentation.html

#### Testing and Verification

- **BitLocker**: Manage BitLocker panel shows "BitLocker on" for C: drive
- **VeraCrypt pre-boot**: Restart laptop; VeraCrypt passphrase prompt appears before Windows
- **VeraCrypt container**: Mount container, write a test file, dismount, verify the container file is not browseable from File Explorer without VeraCrypt
- **FileVault**: System Settings → Privacy & Security → FileVault shows "FileVault is turned on"
- **iPhone ADP**: Settings → [name] → iCloud → Advanced Data Protection shows "On"

#### Common Mistakes

- Not saving recovery keys. If you forget your BitLocker passphrase and haven't saved the recovery key, your data is permanently inaccessible.
- TPM auto-unlock on BitLocker without a PIN means BitLocker provides no protection if someone boots your machine while it is powered on (e.g., a "hot" seizure). To require a PIN at startup: Group Policy → Computer Config → Admin Templates → Windows Components → BitLocker → Operating System Drives → "Require additional authentication at startup" → enable "Require startup PIN with TPM."
- Dismounting a VeraCrypt container before unplugging the drive. Always dismount first; unplugging while mounted can corrupt the container.

#### Estimated Time Commitment

- Part A verification: 15 minutes
- Part B VeraCrypt container: 30 minutes
- Part C FileVault (Mac): 15 minutes + background encryption
- Part D Linux LUKS (if applicable): 45 minutes (fresh install) or 3+ hours (reinstall)
- Part E USB drives: 20 minutes each

**Total active time: 1.5–2.5 hours** depending on platforms used.

#### Success Criteria

- [ ] All devices show active encryption (BitLocker/FileVault/LUKS)
- [ ] VeraCrypt container created and tested
- [ ] Sensitive files moved into encrypted container
- [ ] Recovery keys stored physically and in Bitwarden
- [ ] Screen lock enabled on all devices (5–15 minute timeout)

---

### Module 2: Hardware Security Keys and Multi-Factor Authentication

#### Overview

Hardware security keys replace every other form of two-factor authentication (2FA) with phishing-proof cryptographic proof of account ownership. A YubiKey is a USB/NFC device — you tap it when logging in, and it generates a signature that only works on the exact legitimate domain. A fake phishing site cannot accept it. Unlike TOTP codes (6-digit numbers), hardware keys cannot be phished remotely.

**Why this matters for your threat model**: SIM swapping attacks allow an attacker to take over your phone number and receive your SMS 2FA codes. Law enforcement social engineering and "legal process" letters to phone carriers can produce the same result. TOTP codes from apps like Ente Auth are phishing-resistant against most attackers but can still be intercepted in real-time man-in-the-middle attacks. Hardware keys are the only authentication method currently resistant to all three attack vectors.

#### User Prerequisites

- Bitwarden password manager set up (Phase 1 Step 1.5)
- Ente Auth installed and active for critical accounts (Phase 1 Step 1.4)
- YubiKey 5 NFC ordered and received (order on Day 1; arrives 2–5 business days)

#### Step-by-Step Implementation

**Part A: Order hardware (do this on Day 1 of Phase 2)**

1. Go to https://www.yubico.com/store/ — order 2x "YubiKey 5 NFC" ($60 each, $120 total). Two keys: one primary (daily use), one backup (stored securely at home).
2. Alternative (open-source): SoloKeys Solo 2 (~$50 each) at https://solokeys.com — FIDO2/WebAuthn support, no NFC on the basic model.
3. Ship to a P.O. box or pickup location rather than your home address if location privacy is a concern.
4. While waiting for delivery: proceed with Modules 3 and 4.

**Part B: Register primary YubiKey on critical accounts**

Complete this once hardware arrives.

5. Start with Gmail (Google account — highest priority, as it controls account recovery for most services):
   - Go to https://myaccount.google.com → Security → "How you sign in to Google" → "2-Step Verification"
   - Scroll to "Security keys" → "Add security key"
   - Insert YubiKey into USB port (or hold against phone for NFC) → tap the gold circle on the key when it flashes
   - Name the key (e.g., "YubiKey Primary") → Done
6. Repeat for your backup key on Gmail (same process, name it "YubiKey Backup").
7. Register on Bitwarden:
   - Log into https://vault.bitwarden.com → Account Settings → Security → Two-step Login
   - FIDO2 WebAuthn → "Add FIDO2 WebAuthn Credential"
   - Insert key and tap when prompted
   - Repeat for backup key
8. Register on Microsoft/Outlook (if applicable):
   - https://account.microsoft.com → Security → Advanced security options → "Add a new way to sign in" → "Use a security key"
9. Register on GitHub (if applicable):
   - Settings → Password and authentication → Security keys → "Register new security key"
10. Register on Apple ID:
    - Settings → [your name] → Sign-In & Security → Security Keys → "Add Security Key"
    - Requires iOS 16.3+ and a trusted iPhone or iPad present
    - Note: Registering a security key on Apple ID removes the ability to use iCloud.com for account recovery — ensure you have a backup key registered before proceeding
11. Register on financial accounts (bank, brokerage):
    - Most major banks now support FIDO2 under Settings → Security → Two-factor authentication → "Security key"
    - Not all banks support hardware keys; use TOTP (Ente Auth) as the fallback

**Part C: Generate and store recovery codes**

12. After registering keys on each account, save the account's recovery/backup codes in Bitwarden. These are one-time codes that unlock the account if you lose all your hardware keys.
13. Print a master recovery code sheet and store it in a physically secure location (not near your computer). This sheet should have: [Service name] | [Recovery code 1] | [Recovery code 2] ... for each critical service.
14. Test recovery codes: on a non-critical service, log out, then use a recovery code to log back in. Confirm they work before you need them in an emergency.

**Part D: Establish key storage protocol**

15. Primary YubiKey: Keep on your keychain or in your wallet.
16. Backup YubiKey: Store in a secure location separate from your primary key (different physical location — not the same bag or drawer). If one is lost, you still have the other.
17. If you ever lose a key: immediately log into every registered service and deregister the lost key from the Security Keys list. Replace with a new key.

**Part E: Gradual account migration (ongoing, weeks 1–4)**

18. You do not need to register keys on every account in one session. Migrate accounts as you naturally log into them:
    - Next time you log into your bank → add YubiKey to that session
    - Next time you log into GitHub → add YubiKey
    - After 3–4 weeks, all critical accounts will have keys registered

#### Key Decisions and Trade-offs

- **YubiKey 5 NFC vs. Security Key NFC**: YubiKey 5 NFC ($60) supports FIDO2 + TOTP + PIV + OpenPGP. Security Key NFC ($30) supports only FIDO2/WebAuthn. For your threat model, FIDO2-only is sufficient and saves $60 per key. However, the YubiKey 5 NFC adds OpenPGP support useful for email signing later.
- **How many keys to buy**: Minimum 2 (primary + backup). 3 if you have multiple high-risk locations (home + office + offsite cache).
- **What if a service doesn't support hardware keys**: Use Ente Auth TOTP as fallback. Never revert to SMS 2FA — if a service only offers SMS, consider whether you need that service.
- **Passkeys vs. Security Keys**: Some services now offer "passkeys" (device-bound cryptographic keys stored in your OS/browser). These are convenient but tied to a device — if you factory-reset your phone, you lose them. Hardware keys are portable and device-independent.

#### Tools and Resources

| Tool | Cost | Open Source | Notes |
|------|------|-------------|-------|
| YubiKey 5 NFC | $60/key | No | Industry standard; USB-A/C + NFC; most compatible |
| YubiKey Security Key NFC | $30/key | No | FIDO2 only; budget option |
| SoloKeys Solo 2 | $50/key | Yes | Open-source firmware; FIDO2 + TOTP; no NFC on base |
| OnlyKey | $47/key | Yes | Open-source; adds password storage |

- Yubico store: https://www.yubico.com/store/
- FIDO2 standards documentation: https://fidoalliance.org/fido2/
- Which sites support YubiKey: https://www.yubico.com/works-with-yubikey/catalog/

#### Testing and Verification

- Log out of Gmail completely, log back in → when prompted for 2FA, insert YubiKey and tap → should log in without entering any code
- Log into Bitwarden → verify key prompt appears instead of TOTP
- Test one backup key: register it, remove primary key, log out, log back in using only backup key
- Verify recovery codes work on one non-critical account

#### Common Mistakes

- Registering only one key. If you lose it before registering a backup, account recovery using backup codes takes time and may require identity verification with the service.
- Forgetting to register the backup key on every account you register the primary on.
- Losing the recovery codes. Store them physically AND in Bitwarden.
- Registering keys on Apple ID without understanding it disables iCloud.com recovery — read Apple's instructions fully.

#### Estimated Time Commitment

- Ordering hardware: 10 minutes
- Registering on 6–8 critical accounts: 1.5–2 hours
- Ongoing migration (as you log into services): 15 minutes/week for 3–4 weeks

**Total active time: 2–3 hours** (plus hardware delivery wait)

#### Success Criteria

- [ ] 2x YubiKeys received
- [ ] Both keys registered on: Gmail, Bitwarden, Apple ID, primary bank
- [ ] Recovery codes for all key accounts stored in Bitwarden + printed backup
- [ ] Tested: log in using only hardware key, no TOTP
- [ ] Tested: log in using only recovery codes on one account
- [ ] Backup key stored at separate physical location

---

### Module 3: Network Anonymization and Routing

#### Overview

Module 3 covers always-on VPN via Mullvad, browser hardening against fingerprinting, Tor integration for high-risk research, and the trade-offs between them. After this module, your internet traffic is encrypted before it leaves your machine, your IP address is hidden from the sites you visit, and your browser cannot be uniquely fingerprinted.

**Why this matters for your threat model**: Your ISP sees every domain you visit (unencrypted DNS) and sells that data. ICE and law enforcement purchase location data from ad brokers using mobile advertising IDs harvested from your phone's apps. Mullvad hides your IP from websites and your browsing from your ISP. The VPN kill switch ensures that if the VPN drops, traffic stops entirely rather than leaking in plaintext.

#### User Prerequisites

- None. This module is independent and can start immediately.
- Budget: $5–6/month for Mullvad VPN

#### Step-by-Step Implementation

**Part A: Set up Mullvad VPN on Windows**

1. Go to https://mullvad.net/en/download — download the Windows installer.
2. Run the installer. Accept defaults. Mullvad installs as a system service.
3. Open Mullvad → click "Create account" → a 16-digit account number is generated immediately. No email required. No password. Write this number down and store it in Bitwarden.
4. Add time to your account:
   - **Most private**: Mail physical cash to Mullvad's office (instructions at https://mullvad.net/help/sending-cash/). Takes 5–10 business days.
   - **Practical bridge**: Buy a prepaid Visa/Mastercard with cash at a grocery store → use that to pay at https://mullvad.net/en/account/payment. This keeps your real credit card out of the record.
   - **Least private**: Use a real credit card (acceptable if VPN metadata is not in your threat model — this only reveals you subscribe to Mullvad, not what you do with it).
5. In Mullvad settings: Settings → VPN Settings → toggle "Launch app on start-up" to ON.
6. Settings → VPN Settings → toggle "Auto-connect" to ON.
7. Settings → VPN Settings → toggle "Kill switch" (also called "Lockdown mode") to ON. This blocks all traffic if the VPN disconnects.
8. Settings → DNS → toggle "Block ads" and "Block malware" to ON (optional but recommended).
9. Click "Connect" — select any server. Sweden, Switzerland, or Iceland are strong jurisdictions.
10. Verify: go to https://mullvad.net/en/check — it should show "You are connected to Mullvad" and display a Mullvad IP, not your ISP's IP.

**Part B: Set up Mullvad VPN on iPhone**

11. App Store → search "Mullvad VPN" (developer: Amagicom AB) → install.
12. Open app → enter your 16-digit account number → tap "Log in."
13. Tap the gear icon → VPN Settings → enable "Always On VPN" (this uses iOS's built-in VPN management to reconnect automatically if dropped).
14. Enable "Kill Switch" in settings.
15. Tap the large power button to connect.
16. Verify: visit https://mullvad.net/en/check on your phone's browser — should show Mullvad connection.

**Part C: Browser hardening against fingerprinting**

Your browser can be uniquely identified ("fingerprinted") even with a VPN, using combinations of: screen size, font list, timezone, hardware capabilities, and installed extensions. This matters if you're doing sensitive research.

17. Install Mullvad Browser from https://mullvad.net/en/browser — this is a Firefox-based browser developed by Tor Project specifically to resist fingerprinting. It is the right browser for sensitive research.
18. Use Mullvad Browser for all sensitive activity (reading news, research, any site you don't want linked to your identity). Keep Chrome/Edge/Safari for logged-in accounts.
19. In Mullvad Browser: never log into any personal accounts. It should remain cookieless and fingerprint-neutral.
20. Install uBlock Origin in any non-Mullvad browser you use: https://ublockorigin.com — blocks ad trackers that feed location data to brokers.

**Part D: Tor for high-risk research (optional, high-threat scenarios)**

Use Tor Browser when you need stronger anonymity than a VPN provides — for example: reading leaked documents, visiting whistleblowing platforms, researching something where your IP appearing in a server log is a serious risk.

21. Download Tor Browser from https://www.torproject.org/download/ — verify the signature.
22. Open Tor Browser. It routes your traffic through 3 volunteer-run relays before reaching the destination. Your IP is never visible to the destination.
23. Use Tor in combination with Mullvad: Mullvad Settings → VPN Settings → "SOCKS5 proxy" → enable. This routes Tor traffic through Mullvad's servers, so your ISP sees encrypted VPN traffic, not Tor traffic patterns (Tor use itself can flag attention in some threat models).
24. Tor limitations: 2–5x slower than normal browsing. Some sites block Tor exit nodes. Not suitable for streaming or daily browsing. Use selectively.

**Understanding the VPN vs. Tor trade-off**:

| Need | Best Tool |
|------|-----------|
| Hide browsing from ISP, general privacy | Mullvad VPN |
| Fingerprint-resistant browsing | Mullvad Browser |
| Strong anonymity from destination site | Tor Browser |
| State-level adversary, leaked docs, whistleblowing | Tor over Mullvad |
| Everyday usability | Mullvad VPN + Mullvad Browser |

#### Key Decisions and Trade-offs

- **VPN provider choice**: Mullvad is the strongest choice for your threat model: Swedish jurisdiction, no email account (just account number), verified no-log (Swedish police subpoena confirmed no data available), anonymous payment options. ProtonVPN is acceptable as a second choice (Swiss jurisdiction, open-source client). Avoid US-based VPN providers — subject to US legal process.
- **Kill switch**: Always on. The minor inconvenience of briefly losing internet if the VPN drops is worth avoiding any accidental IP leak.
- **Browser separation**: Three-browser approach is ideal: (1) Mullvad Browser for sensitive research (no logins), (2) regular browser for logged-in daily use, (3) Tor for high-risk scenarios. Mixing these breaks the protection model.
- **Mullvad Browser vs. Tor Browser**: Mullvad Browser is faster and more compatible. Tor provides stronger anonymity via three-hop routing but is slower. Choose based on threat level.

#### Tools and Resources

| Tool | Cost | Open Source | Notes |
|------|------|-------------|-------|
| Mullvad VPN | $5/month | Yes (client) | Swedish jurisdiction; no email; verified no-log |
| ProtonVPN | $4–10/month | Yes | Swiss jurisdiction; solid alternative |
| Mullvad Browser | Free | Yes | Firefox-based; Tor Project-developed; fingerprint-resistant |
| Tor Browser | Free | Yes | Three-hop onion routing; strongest anonymity |
| uBlock Origin | Free | Yes | Content blocker; essential for any browser |

- Mullvad VPN: https://mullvad.net
- Mullvad Browser: https://mullvad.net/en/browser
- Tor Project: https://www.torproject.org
- EFF: Surveillance Self-Defense: https://ssd.eff.org

#### Testing and Verification

- Windows: https://mullvad.net/en/check shows "Connected to Mullvad" + Mullvad IP
- iPhone: same check on mobile browser
- Kill switch test: disconnect Mullvad, attempt to browse → traffic should fail entirely, not fall back to ISP
- Browser fingerprint test: visit https://coveryourtracks.eff.org with Mullvad Browser — "strong protection against Web tracking"
- DNS leak test: https://dnsleaktest.com while on Mullvad — only Mullvad DNS servers should appear

#### Common Mistakes

- Forgetting to re-enable kill switch after a Mullvad update (some updates reset settings — check after every update).
- Using Mullvad Browser while logged into personal accounts. The entire point is a logged-out, fingerprint-neutral browser.
- Relying on a VPN alone as "full anonymity." A VPN hides your IP from destinations and your browsing from your ISP. It does not protect against browser fingerprinting, cookies, logged-in accounts, or correlation attacks.
- Paying for Mullvad with a credit card registered to your real identity if payment anonymity matters. Use prepaid card or cash.

#### Estimated Time Commitment

- Part A (Windows VPN): 30 minutes
- Part B (iPhone VPN): 15 minutes
- Part C (Browser hardening): 30 minutes
- Part D (Tor setup): 20 minutes (optional)

**Total active time: 1–1.5 hours**

#### Success Criteria

- [ ] Mullvad running on Windows with kill switch enabled, auto-connect on startup
- [ ] Mullvad running on iPhone with always-on VPN
- [ ] Mullvad Browser installed and used for sensitive research
- [ ] uBlock Origin installed in daily-use browser
- [ ] https://mullvad.net/en/check confirms connection from both devices
- [ ] DNS leak test clean

---

### Module 4: Metadata Minimization and Communication Security

#### Overview

End-to-end encryption like Signal protects the *content* of your messages. But metadata — who you talked to, when, how often, how long — remains visible and actionable. Module 4 covers Signal hardening, email alias deployment, metadata erasure for sent files, and PII compartmentalization across services. The goal is to fragment your digital identity into context-separated shards that cannot be linked by a data broker or surveillance platform.

**Why this matters for your threat model**: IRS and law enforcement platforms map "social networks among targets" using communications metadata. Even without reading a single message, metadata logs show when you communicate with specific people, what topics may be implied by timing correlations, and your behavioral patterns. The DOGE fusion architecture can link email metadata from a breach to IRS records to location data. Fragmentation makes this linking computationally expensive and incomplete.

#### User Prerequisites

- Signal installed (Phase 1 Step 1.1) with privacy settings configured
- Bitwarden active (Phase 1 Step 1.5) for alias management
- Mullvad VPN running (Module 3) — use VPN during all alias setup

#### Step-by-Step Implementation

**Part A: Signal hardening and metadata minimization**

1. Open Signal → Settings → Privacy:
   - "Phone number" → "Who can see my phone number" → Nobody
   - "Phone number" → "Who can find me by my number" → Nobody
   - "Default timer for new chats" → 1 Week (existing chats: open each, tap name → "Disappearing messages" → 1 Week)
   - "Read receipts" → OFF
   - "Typing indicators" → OFF
   - "Link previews" → OFF (prevents Signal from fetching URLs you send)
2. Settings → Notifications → "Show" → "No name or message" — prevents message preview from appearing on your lock screen.
3. Settings → Profile → verify your display name is not your real name. Use a pseudonym or nickname.
4. Go through your Signal contacts: remove anyone you no longer actively communicate with. Fewer contacts = smaller exposure surface.
5. For truly sensitive conversations (organizing, legal matters): create a new Signal group with these specific settings enforced:
   - Open group → tap group name → "Disappearing messages" → 1 Day
   - Add only the minimum necessary participants
   - Verify safety numbers (Settings → Privacy → Advanced → verify safety numbers with each person in person or via a separate channel)

**Part B: Briar for high-risk offline scenarios (optional)**

Use Briar only when: internet access is unavailable or unsafe, you need to communicate with someone locally without creating an internet-routable record, or you are coordinating in an environment where cell network monitoring is suspected.

6. Android only: Install Briar from https://briarproject.org or F-Droid. (iOS version in beta as of 2026.)
7. Create a Briar account — no phone number, no email required. Choose a pseudonym.
8. Add contacts: in Briar, you add contacts by being physically present (Bluetooth introduction) or via a one-time link. This contact verification eliminates impersonation.
9. Briar works over Tor when internet is available, Bluetooth/Wi-Fi mesh when it isn't.
10. Limitation: Briar's Bluetooth range is ~100 meters. Both parties must have the app running. Battery drain is significant. Use Signal for routine secure communication and Briar only for specific high-risk scenarios.

**Part C: Email alias system setup**

11. Go to https://app.simplelogin.io — create an account using a pseudonymous email address, not your primary email. (Yes: create a temporary account just to sign up, then point the aliases to your real email.)
12. In SimpleLogin: "Aliases" → "Create new alias" — create aliases for each service category:
    - `shopping-amazon@[your-domain].simplelogin.co` → forwards to your real email
    - `banking-primary@[...]` → for financial institutions
    - `subscriptions-news@[...]` → for newsletters
    - `activism@[...]` → if applicable
    - Create a generic "burner" alias for any new signup you're not sure about
13. In Bitwarden: for each service login entry, update the "Username" field to the alias you're using for that service.
14. Going forward: whenever you sign up for a new service, create a new SimpleLogin alias first.
15. Benefits: if an alias gets spammed or breached, you disable just that alias. You can identify *which* service sold or leaked your address.
16. Alternative: Apple iCloud+ Hide My Email (free with iCloud+) — generates on-device aliases with one tap. Simpler but less configurable than SimpleLogin.

**Part D: File metadata stripping**

Before sending any document or photo, strip the embedded metadata (EXIF data) that can reveal your location, device type, and creation time.

17. Photos on Windows: right-click → Properties → Details → "Remove Properties and Personal Information" → "Create a copy with all possible properties removed." Send the copy.
18. Photos on iPhone: when sharing a photo, iOS 16+ offers "Remove Location" before sending. Enable this by default: Settings → Privacy → Photos → review which apps have location access.
19. Documents (Word, PDF): File → Info → "Check for Issues" → "Inspect Document" → remove all personal info → Save. Alternatively, print to PDF and resave — this often strips embedded author/metadata.
20. For sensitive documents: use MAT2 (metadata anonymization toolkit) if you have Linux access: `mat2 file.pdf` strips all metadata. Available at https://0xacab.org/jvoisin/mat2

**Part E: PII compartmentalization across services**

21. Review your accounts in Bitwarden. For any service that does not need your real name, update the profile to a pseudonym.
22. For services that require a real name (banking, legal, government): these are unavoidable. Contain the data leakage by ensuring those accounts are not linked to your activist/research/sensitive email or phone number.
23. Create a mental (or documented) map of your identity tiers:
    - **Tier 1 (real identity)**: banking, insurance, government, employer
    - **Tier 2 (pseudonymous)**: news subscriptions, research tools, libraries, VPNs
    - **Tier 3 (anonymous)**: activist organizing, sensitive research, any account where real identity is a risk
    - Never cross-link tiers (don't use your banking email on an activist account, etc.)

#### Key Decisions and Trade-offs

- **Signal vs. Briar**: Signal for routine secure communication (phone number required, internet required). Briar for high-risk or internet-unavailable scenarios. Both for a comprehensive activist setup.
- **SimpleLogin vs. iCloud Hide My Email**: SimpleLogin is more configurable, open-source, and works cross-platform. iCloud is simpler if you're in Apple's ecosystem. SimpleLogin is better if you want long-term alias management.
- **Disappearing messages timer**: 1 week is a good default. Shorten to 1 day for the most sensitive conversations. Lengthening to 4 weeks is acceptable for low-risk contacts where conversation history is useful.
- **Metadata stripping**: high friction if done manually every time. Build it into your workflow: never send a photo without checking location is stripped; never send a document without running metadata check.

#### Tools and Resources

| Tool | Cost | Open Source | Notes |
|------|------|-------------|-------|
| Signal | Free | Yes | Gold standard E2E messaging; iOS + Android + Desktop |
| Briar | Free | Yes | Offline mesh; Android; Tor-routed when online |
| SimpleLogin | Free (15 aliases) / $30/yr unlimited | Yes | Email aliases; Proton ecosystem |
| Apple Hide My Email | Free (iCloud+) | No | On-device alias generation; simpler than SimpleLogin |
| MAT2 | Free | Yes | Metadata stripping; Linux; CLI tool |

- Signal best practices (2026): https://libraryfreedom.org/wp-content/uploads/2026/01/signal-best-practices.pdf
- SimpleLogin: https://simplelogin.io
- EFF Surveillance Self-Defense on metadata: https://ssd.eff.org/module/why-metadata-matters

#### Testing and Verification

- Signal: ask a contact to look up your profile by phone number — they should find nothing
- Disappearing messages: verify timer is active in all sensitive chats
- SimpleLogin: send an email to one of your aliases from a different email account — confirm it forwards correctly
- Metadata: send a photo to yourself through Signal, save it, check properties in Windows Explorer — GPS coordinates should be absent
- Identity tiers: review your 5 most-used services and confirm each uses the appropriate alias tier

#### Common Mistakes

- Leaving disappearing messages off by default. The EFF and Freedom of the Press Foundation both document that this is the single highest-impact Signal hardening step.
- Using the same alias across multiple unrelated services — this defeats the purpose of compartmentalization.
- Sending files from a desktop client that auto-attaches your real name as document author metadata.
- Enabling Briar and leaving it running constantly — the battery drain is significant. Run it only when actively using it.

#### Estimated Time Commitment

- Part A Signal hardening: 20 minutes
- Part B Briar setup: 30 minutes (optional)
- Part C Email aliases: 45 minutes
- Part D Metadata workflow: 15 minutes (setup) + ongoing
- Part E PII audit: 30–60 minutes

**Total active time: 2–3 hours**

#### Success Criteria

- [ ] Signal: phone number hidden, read receipts off, disappearing messages on for all chats
- [ ] Safety numbers verified with at least 2 most-trusted Signal contacts
- [ ] 5+ SimpleLogin aliases created and deployed in Bitwarden
- [ ] No new account signups using your real email address
- [ ] Metadata stripping process tested on a photo and document
- [ ] Identity tiers documented (even informally)

---

### Module 5: Physical Security and Location Privacy

#### Overview

Digital OpSec protects what leaves your devices. Physical OpSec protects what can be observed about you in the physical world — your face, your location, your associations, and your devices. Module 5 covers facial recognition countermeasures, location pattern hardening, device security in hostile environments, and physical counter-surveillance basics.

**Why this matters for your threat model**: DHS HART biometric platform retains facial recognition data for 75–100 years. ICE Mobile Fortify field deployment puts facial recognition capability into the hands of individual agents in the field. LAPD and NYPD deploy drones at protests. Palantir's fusion architecture links a facial recognition match to your SSN, address history, and communication patterns. You cannot control your face, but you can reduce the circumstances under which it's captured and linked.

#### User Prerequisites

- None. This module is primarily behavioral and requires no software installation.
- Some optional hardware purchases are listed below.

#### Step-by-Step Implementation

**Part A: Location data minimization (devices)**

1. Review every app on your iPhone that has location access: Settings → Privacy & Security → Location Services. Set to "Never" for any app that doesn't genuinely need it. Set to "While Using" for navigation apps. No app should have "Always" access unless it's a safety app you trust entirely.
2. Turn off "Significant Locations": Settings → Privacy & Security → Location Services → System Services → Significant Locations → OFF. This disables Apple's passive recording of places you frequently visit.
3. Disable Wi-Fi scanning even when Wi-Fi is off: Settings → Privacy & Security → Location Services → System Services → Wi-Fi Networking → OFF.
4. When attending any event or location where your presence is sensitive: put your phone into Airplane Mode before arriving and keep it in Airplane mode until you leave the general area. Cellular triangulation and Wi-Fi probe requests (your phone broadcasting to find known networks) can place you at a location even without GPS.
5. Consider purchasing a second, unregistered device (a cheap Android phone purchased with cash, never linked to your real accounts) for use at high-risk events. This device has no SIM, connects to Wi-Fi only when needed, and has no apps with personal account data.

**Part B: Facial recognition countermeasures**

6. At public events, protests, or any setting where you don't want your face linked to your presence:
   - Wear a well-fitting mask covering nose and mouth
   - Wear a hat with a brim that obscures overhead camera angles
   - Wear sunglasses
   - Current facial recognition accuracy degrades significantly with all three combined — studies show 30–60% accuracy reduction with mask+hat+sunglasses vs. bare face
7. Avoid looking directly into overhead cameras. Cameras at protests are often positioned to capture faces looking up at police lines — keep your head angled slightly down.
8. Wear generic, non-distinctive clothing. Bright colors, unique patterns, or distinctive logos enable re-identification even when facial recognition fails — this is called "gait and clothing re-identification."
9. Do not carry your daily phone to sensitive events (see Part A step 5).

**Part C: Hardware security for devices**

10. Enable auto-reboot on your iPhone: Settings → Face ID & Passcode → scroll to "Require Passcode" → set to "Immediately." This isn't auto-reboot, but ensures the device requires a PIN immediately when locked. For auto-reboot: iPhones running iOS 18+ automatically reboot after 72 hours of no unlock — this is sufficient for most threat models.
11. Before any event where device seizure is possible: power your phone completely off. A powered-off phone is in BFU (Before First Unlock) state, which encrypts all data including the keychain. An unlocked or locked-but-not-off iPhone is in AFU (After First Unlock) state — the encryption keys are resident in memory and forensic tools can extract them. Powered off = maximum protection.
12. Disable USB accessories while locked: Settings → Face ID & Passcode → "Accessories" (at the bottom) → OFF. This prevents Cellebrite-style USB forensics tools from accessing your phone via the Lightning/USB-C port while locked.
13. On Windows: set your computer to lock screen after 5 minutes of inactivity (Settings → Accounts → Sign-in options → "Require sign-in" → "When PC wakes from sleep" → Immediately).
14. Enable Secure Boot in UEFI/BIOS to prevent bootkit attacks. Access BIOS at startup (usually F2, F12, or Delete during POST) → Secure Boot → enable. This prevents someone from booting your machine from a USB drive to read your disk.

**Part D: Physical counter-surveillance basics**

15. Vary your routes: if you walk, drive, or take transit the same route every day at the same time, you are easy to track and intercept. Vary departure times and routes for locations you visit regularly for sensitive reasons.
16. Detect if you're being followed: use the "surveillance detection route" technique — take an indirect route with at least one U-turn or doubling back, and note any vehicles or persons who follow the same path. Not paranoia — a 5-minute awareness habit.
17. Meetings for sensitive subjects: conduct in person, in public places with multiple exits, without devices (or with devices in Faraday bags / airplane mode). Coffee shops with ambient noise are preferred over quiet spaces where conversation is easier to record.
18. Faraday bags: a phone in a Faraday bag cannot receive or transmit signals. This is the only reliable way to prevent real-time location tracking if you must carry your device. Quality Faraday bags are available from Mission Darkness (~$30–60) or DIY from layers of aluminum foil (less reliable).

**Part E: Check your digital footprint for physical exposure**

19. Search your full name and address on: Spokeo.com, BeenVerified.com, WhitePages.com, and FastPeopleSearch.com. If your current address appears, submit opt-out requests (each site has an "opt out" link, usually in the footer).
20. Check Google Maps and Google Street View for your home address — verify no sensitive vehicles, home layout details, or identifying features are clearly visible. If there's an issue, you can request a face/plate blur from Google.
21. Check if any of your social media profiles expose your current neighborhood, employer, daily routine, or family members' names. These are OSINT attack vectors.

#### Key Decisions and Trade-offs

- **Second device vs. Airplane mode**: A second, unregistered device is more private (no link to your identity at all). Airplane mode is much simpler and sufficient for most threat models. If you regularly attend sensitive events, a $50 cash-purchased Android is worth the investment.
- **Faraday bag vs. Airplane mode**: Airplane mode depends on your phone's software correctly disabling radios. A Faraday bag is a hardware guarantee. For threat models involving government-level adversaries: Faraday bag is more reliable.
- **Facial recognition countermeasures**: effective but disruptive to normal life. Don't use them everywhere — use them selectively at events where your presence is sensitive. Daily facial recognition countermeasure use signals unusual behavior in itself.

#### Tools and Resources

| Tool | Cost | Open Source | Notes |
|------|------|-------------|-------|
| Mission Darkness Faraday bag | $30–60 | No | Hardware-verified signal blocking |
| Prepaid Android (cash purchase) | $50–80 | N/A | For events; no SIM, no personal accounts |
| Outdoor hat with brim | $15–30 | N/A | Overhead camera obstruction |
| Quality mask (N95 or similar) | $1–5 each | N/A | Facial recognition degradation |

- EFF's guide to devices at protests: https://ssd.eff.org/module/attending-protest
- DHS HART biometric system: https://www.dhs.gov/science-and-technology/biometrics
- Aerial surveillance ADS-B tracking (monitor active planes over your area): https://adsbexchange.com

#### Testing and Verification

- Location review: Settings → Privacy → Location Services — every app should have a documented reason for its access level
- Lock screen test: lock your iPhone, attempt USB connection with a computer → should prompt for pin
- BFU test: power off your phone, power back on, confirm it prompts for PIN before loading the OS (not just Face ID)
- Data broker search: search your name + city on Spokeo; verify no home address exposure

#### Common Mistakes

- Keeping your personal phone on and connected while at sensitive events. This creates a geolocation record even if you don't use the phone.
- Assuming a VPN provides physical location anonymity. A VPN masks your IP online; it does not mask your cellular tower pings.
- Taking photos at sensitive events with your real phone's camera. Photos embed EXIF GPS data and are linked to your Apple/Google account.

#### Estimated Time Commitment

- Part A location audit: 20 minutes
- Part B countermeasures: 0 (behavioral; purchase time 10 minutes online)
- Part C device hardening: 20 minutes
- Part D counter-surveillance: 0 (behavioral habit)
- Part E digital footprint check: 30 minutes

**Total active time: 1.5 hours** (plus any data broker opt-outs if new exposures found)

#### Success Criteria

- [ ] All iPhone apps reviewed for location access; only necessary apps have it
- [ ] Significant Locations and Wi-Fi scanning disabled
- [ ] USB accessories while locked: disabled
- [ ] Secure Boot enabled in UEFI
- [ ] Data broker search completed; opt-outs submitted for any new address exposure
- [ ] Faraday bag or Airplane-mode protocol decided for high-risk events

---

### Module 6: Organizational OpSec and Incident Response

#### Overview

Organizational OpSec governs how you manage your collection of credentials, what happens when a breach or arrest occurs, and how you respond to legal process (subpoenas, warrants, National Security Letters). This module covers credential compartmentalization, breach detection, incident response drills, and the legal knowledge needed to protect yourself and others if law enforcement makes contact.

**Why this matters for your threat model**: A single credential breach can cascade into exposure across all linked services if you use the same passwords or recovery methods. Activists and journalists are not just individuals — their compromised accounts can expose their networks. Legal process (warrants, subpoenas) requires specific response behaviors that most people never prepare for. Knowing what to say and what not to say before a crisis is the difference between a manageable incident and a catastrophic one.

#### User Prerequisites

- Bitwarden active with all critical accounts stored
- Hardware security keys registered (Module 2) on all critical accounts
- Phase 1 data broker opt-outs complete

#### Step-by-Step Implementation

**Part A: Credential compartmentalization audit**

1. Open Bitwarden → review all saved logins. For each login, answer: "If this account was compromised, what other accounts would be at risk?" A compromised Gmail account used as recovery for 20 other services is catastrophic. A compartmentalized Gmail used only for Gmail is contained.
2. Identify your "master recovery chain." This is typically: Gmail → (recovers bank, social media, other services). Protect this chain above all else.
3. For every account: verify it uses a unique Bitwarden-generated password. No reuse. Use Bitwarden's built-in password health report (Tools → Exposed Passwords) to find any reused or compromised passwords.
4. Change any reused passwords immediately. Bitwarden's password generator: default to 20+ character random passwords for high-value accounts.
5. Review recovery email addresses: if your "recovery email" for Gmail is an old Yahoo account you haven't checked in years, that's an attack vector. Update recovery emails to your current primary email. Consider pointing critical accounts' recovery email to a SimpleLogin alias rather than a real inbox.
6. Review backup phone numbers: remove SMS-based 2FA from all accounts that support hardware key or TOTP alternatives. SMS is the weakest link.

**Part B: Breach detection and monitoring**

7. Set up HaveIBeenPwned monitoring: go to https://haveibeenpwned.com/NotifyMe → enter your email addresses (including all SimpleLogin aliases). This sends you an alert if any of your addresses appears in a data breach.
8. Check current breach status: https://haveibeenpwned.com — enter each email address. If any appear in a breach, immediately:
   - Change that account's password via Bitwarden
   - Check if the breach site has your phone number, address, or SSN — if yes, assume that data is circulating
   - Check if that account was used as recovery for others
9. Check if your passwords appear in known password lists: Bitwarden Tools → Exposed Passwords → this queries HaveIBeenPwned's password database (anonymously). Change any flagged passwords.
10. Set a calendar reminder: check HaveIBeenPwned manually every 3 months (or rely on email notifications from step 7).

**Part C: Incident response protocol (device seizure / arrest)**

Prepare this now, before you need it.

11. Power off your phone before any anticipated confrontation with law enforcement. A powered-off phone in BFU state has the strongest encryption. Law enforcement cannot compel you to unlock it with biometrics while it's off.
12. Know your rights:
    - You are NOT required to provide your phone PIN or computer passphrase (Fifth Amendment protection, confirmed in most federal circuits as of 2026)
    - You CAN be compelled to provide biometrics (Face ID, fingerprint) — this is currently not considered protected compelled testimony
    - You CAN refuse to consent to a device search — require a warrant
    - The only thing you must provide: your name (in most states, ID if operating a vehicle)
    - Everything else: "I invoke my Fifth Amendment right to remain silent. I want a lawyer."
13. Memorize this phrase or write it on a card in your wallet: "I do not consent to any search. I am invoking my Fifth Amendment right. I want a lawyer."
14. Know who to call: have a lawyer's phone number memorized (not just in your locked phone). Many public defenders and civil rights organizations (ACLU, National Lawyers Guild) maintain 24-hour arrest hotlines.
    - National Lawyers Guild: 212-679-6018 (US)
    - ACLU: state-specific numbers at https://www.aclu.org/legal-help
15. If your device is seized: as soon as you have access to another device, log into all your critical accounts and:
    - Deregister the seized device from iCloud, Google account, Microsoft account
    - Change master passwords for email, Bitwarden
    - Revoke any active sessions from account security dashboards
    - Contact your lawyer before any other action

**Part D: Subpoena and legal process awareness**

16. If you receive a subpoena or legal demand: do not respond without a lawyer. Contact an attorney before acknowledging receipt.
17. Know what can be obtained with different legal process levels:
    - **Subpoena (civil)**: Lower bar; can compel production of existing records. Cannot compel you to decrypt.
    - **Search warrant**: Requires probable cause; gives physical access to your devices.
    - **National Security Letter (NSL)**: No judicial review required; comes with gag order; targets communications providers, not usually individuals.
    - **Title III wiretap**: Requires judicial order; targets future communications, not stored data.
18. Services you use have their own legal response policies. Review:
    - Mullvad's warrant canary and transparency report: https://mullvad.net/en/blog/tag/transparency
    - Signal's minimal data policy (only stores account creation date + last connection time): https://signal.org/bigbrother/
    - Proton's transparency report: https://proton.me/legal/transparency

**Part E: Incident response drill**

19. Once a year, run through a simulated breach scenario: "My email has been compromised." Walk through the steps: identify impact, change passwords, check linked accounts, alert contacts if their security may be affected.
20. Document your response protocol in Bitwarden's secure notes: "In case of device seizure, do X, Y, Z." You won't be thinking clearly under stress — having it written down matters.
21. Tell a trusted person (lawyer, partner, close friend) where your backup YubiKey is stored and how to recover your accounts if you are incapacitated.

#### Key Decisions and Trade-offs

- **How many "tiers" of identity compartmentalization**: Two tiers (real identity + pseudonymous) is manageable for most people. Three tiers (real + pseudonymous + anonymous) is the target for activists. More tiers = more management overhead.
- **Whether to remove biometrics entirely**: Disabling Face ID/Touch ID and using PIN only is more legally protective (biometrics can be compelled; PINs legally cannot, in most jurisdictions). The trade-off is convenience. Given the threat model, consider enabling biometrics only on low-risk devices and using PIN-only on devices holding sensitive information.
- **Data retention**: For sensitive accounts: enable shorter account data retention and delete old conversations, emails, and files regularly. Data that doesn't exist can't be subpoenaed.

#### Tools and Resources

| Tool | Cost | Open Source | Notes |
|------|------|-------------|-------|
| HaveIBeenPwned | Free | No | Breach monitoring; email notifications |
| Bitwarden password health | Free (built-in) | Yes | Checks for reused + exposed passwords |
| National Lawyers Guild hotline | Free | N/A | 212-679-6018; arrest support |
| EFF Know Your Rights guide | Free | N/A | Legal rights at protests and during device seizure |

- EFF Know Your Rights: https://www.eff.org/know-your-rights
- Signal transparency report: https://signal.org/bigbrother/
- Surveillance Self-Defense guide to arrest: https://ssd.eff.org/module/know-your-rights

#### Testing and Verification

- Bitwarden health report: zero reused passwords, zero exposed passwords
- HaveIBeenPwned: email addresses checked, monitoring alerts active
- Know your rights: can you recite what to say to law enforcement from memory?
- Emergency contact: does a trusted person know where your backup key is?
- Sessions audit: review active sessions on Gmail (Security → Your devices), Bitwarden (Settings → Account → Purge Sessions), Apple ID (Settings → [name] → devices)

#### Common Mistakes

- Using SMS 2FA as a backup when hardware keys are unavailable. SMS is the weakest 2FA method; it should be removed from accounts, not kept as a fallback.
- Not having a lawyer's number memorized. If your phone is seized, your contacts list is also seized.
- Responding to law enforcement questions without representation, even to "clear things up." This is universally harmful.
- Failing to revoke sessions on seized devices. A seized device that is still an "authorized device" in your Google account can still be used to access some data.

#### Estimated Time Commitment

- Part A credential audit: 45–60 minutes
- Part B breach monitoring setup: 15 minutes
- Part C rights preparation: 30 minutes (read + memorize)
- Part D legal process reading: 20 minutes
- Part E incident drill: 30 minutes annually

**Total active time: 2–3 hours** (first time); 30 minutes/year thereafter

#### Success Criteria

- [ ] Bitwarden password health report: 0 reused, 0 exposed passwords
- [ ] HaveIBeenPwned monitoring active for all email addresses
- [ ] SMS 2FA removed from all accounts that support alternatives
- [ ] Emergency phrase memorized: "I do not consent. I invoke my Fifth Amendment right. I want a lawyer."
- [ ] Lawyer contact number memorized or written on physical card
- [ ] Trusted person knows backup key location and account recovery procedure

---

### Module 7: Threat Model Refresh and Continuous Improvement

#### Overview

A threat model is not a document you write once. Adversary capabilities evolve. Tools change. Your own life circumstances change your threat surface. Module 7 establishes a quarterly review practice that keeps your security current and catches new threats before they affect you. It also covers how to evaluate new security tools, how to track the threat landscape, and when to seek expert review.

**Why this matters for your threat model**: The threat model that was accurate in 2024 is partially outdated in 2026. NSA Section 702 renewal, DOGE's cross-agency fusion architecture, ICE Mobile Fortify field deployment, and AI-enhanced facial recognition are all developments from the last 18 months. A 2019 threat model is not a 2026 threat model — and a 2026 model will need updating by 2027.

#### User Prerequisites

- All previous modules complete (or substantially underway)
- Basic familiarity with your Phase 1 and Phase 2 tools

#### Step-by-Step Implementation

**Part A: Document your current threat model**

1. Write a one-page summary of your current threat model. Answer four questions:
   - **What am I protecting?** (data types, accounts, physical safety, network of contacts)
   - **Who wants it?** (commercial data brokers, law enforcement, specific hostile individuals, nation-state?)
   - **What can they actually do?** (subpoena provider records, seize devices, purchase location data, conduct surveillance)
   - **What happens if I get it wrong?** (data breach, arrest, physical safety risk, professional consequences)
2. Save this in Bitwarden as a secure note titled "Threat Model — [current date]." You will update this note quarterly.
3. Rate your current implementation against each threat: "Is my Mullvad VPN sufficient against my ISP selling my browsing data? Yes. Is my current setup sufficient against a federal warrant targeting my device? Partially — depends on whether device is powered off."

**Part B: Set up threat landscape monitoring**

4. Subscribe to these free sources for surveillance and privacy news:
   - EFF Deeplinks newsletter: https://www.eff.org/deeplinks (weekly digest of surveillance/privacy developments)
   - ACLU news alerts: https://action.aclu.org/signup/aclu-news
   - Surveillance Technology Oversight Project: https://www.stopspying.org/news
   - Brennan Center Justice Newsletter: https://www.brennancenter.org/subscribe
5. Set up a Google Alert or RSS feed for: "ICE surveillance," "NSA Section 702," "law enforcement biometrics," "[your state] data privacy," "Palantir government contract."
6. Check https://govtribe.com or https://usaspending.gov monthly for new government procurement of surveillance technology. These public databases show new DHS/ICE/FBI contracts before they appear in news coverage.

**Part C: Quarterly review protocol**

Run this review every 3 months (calendar reminder). Estimated time: 30–45 minutes per quarter.

7. **Data broker check**: Search your full name on Spokeo, BeenVerified, FastPeopleSearch. If your address, phone, or employment has reappeared, submit new opt-out requests.
8. **Breach check**: Visit https://haveibeenpwned.com with all your email addresses. Change any passwords for breached accounts.
9. **Software updates**: Verify all security tools are current:
   - Mullvad VPN: check Settings → About for current version vs. https://mullvad.net/changelog
   - Signal: App Store/Play Store → update
   - Bitwarden: verify auto-update is enabled
   - VeraCrypt: check https://veracrypt.fr for latest release
10. **Account audit**: Review your 10 most critical accounts (in Bitwarden). For each: is hardware key still registered? Is the recovery email still valid? Are there any unfamiliar active sessions?
11. **Threat model update**: Read your saved threat model note. Has anything changed? New surveillance capability disclosed? New legal ruling? New tool available? Update the note.
12. **New tool evaluation**: If a new privacy tool has appeared in your monitoring sources, evaluate it against:
    - Is it open-source? (Can the code be audited?)
    - Has it been independently audited? (Cure53, iSEC Partners, etc.)
    - Who funds it, and what are their interests?
    - Does it have a warrant canary/transparency report?
    - What is the jurisdiction of the company?

**Part D: When to seek expert review**

13. Conditions that should trigger expert consultation rather than self-service:
    - You believe you are under active surveillance
    - You receive any legal process (subpoena, warrant, NSL)
    - You are planning activity that significantly increases your threat surface (whistleblowing, investigative reporting, high-profile organizing)
    - Your threat model changes significantly (new job, new political involvement, new hostile actors)
14. Where to find expert help:
    - EFF's legal referral: https://www.eff.org/about/offices/legal-referrals
    - Access Now Digital Security Helpline (free for journalists, activists): https://www.accessnow.org/help/
    - Freedom of the Press Foundation: https://freedom.press/training/
    - Security in a Box community forum: https://securityinabox.org
    - Reddit r/privacy and r/netsec (for tool-specific questions, not specific threat situations)
    - Security.StackExchange (for technical questions)

**Part E: Fast-track vs. comprehensive path review**

15. After your first quarterly review, assess which path you're on:
    - **Fast track (4–5 modules)**: If your primary threat is commercial tracking and data broker exposure: prioritize Modules 1, 2, 3, 4, and 7. Skip Module 5 (physical security) unless attending sensitive events, skip Module 6 unless you have sensitive professional activities.
    - **Comprehensive track (all 7 modules)**: If your threat model includes government surveillance, activist organizing, or professional risk: all 7 modules are necessary.
16. Re-assess your track at each quarterly review. Threat models escalate and de-escalate. You are not locked into a track permanently.

#### Key Decisions and Trade-offs

- **Review frequency**: Quarterly is the minimum for an active threat model. Monthly is better if your threat surface is high. Annual is better than nothing but misses fast-moving developments.
- **How much is enough**: There is no endpoint in security. The goal is not perfect security but proportionate security — protection adequate for your threat model at manageable cost and friction. Over-investing in security for a threat that doesn't apply to you wastes time and creates false confidence.
- **Expert vs. self-service**: Self-service (this guide) is appropriate for implementing known best practices. Expert consultation is appropriate when you face specific threats, receive legal process, or are about to take a significant high-risk action.

#### Tools and Resources

| Resource | Cost | Notes |
|----------|------|-------|
| EFF Deeplinks | Free | Weekly privacy/surveillance news |
| Access Now Helpline | Free | Expert security help for journalists/activists |
| Freedom of the Press Foundation Training | Free | Journalist-specific security training |
| LINDDUN threat modeling framework | Free | Systematic privacy threat analysis |
| HaveIBeenPwned | Free | Breach monitoring |
| USASpending.gov | Free | Government surveillance procurement tracking |

- LINDDUN framework: https://linddun.org
- Zero Trace Hub threat modeling guide: https://www.zerotracehub.com/opsec/threat-modeling-guide/
- EFF legal referral: https://www.eff.org/about/offices/legal-referrals

#### Testing and Verification

- Quarterly review: completed and documented in Bitwarden secure note with date
- Threat model note: updated with current date
- Data broker search: clean (or opt-outs submitted)
- All security software: current versions confirmed
- Expert help channels: URLs bookmarked, at least one contact method saved

#### Common Mistakes

- Not scheduling the quarterly review. "I'll do it when I remember" means it never happens. Put it in your calendar now: September 1, December 1, March 1, June 1.
- Assuming current tools are still best-in-class. The security tool landscape changes rapidly. What was best practice in 2023 may be deprecated or compromised by 2026.
- Conflating "no breach detected" with "secure." Absence of evidence of compromise is not evidence of absence.

#### Estimated Time Commitment

- Part A threat model documentation: 30 minutes
- Part B monitoring setup: 20 minutes
- Part C quarterly review (first time): 45 minutes; ongoing: 30 minutes/quarter
- Part D expert help research: 20 minutes

**Total active time: 1.5–2 hours** (initial); 30 minutes/quarter thereafter

#### Success Criteria

- [ ] Threat model document written and saved in Bitwarden
- [ ] 4 monitoring sources subscribed to
- [ ] Quarterly review calendar reminders set (next 2 years)
- [ ] Expert help channels bookmarked
- [ ] First quarterly review completed within 90 days of completing Phase 2

---

## Section 3: Sequencing and Dependencies

### Critical Path Analysis

The critical path through Phase 2 — the sequence that unblocks the most downstream work — is:

**Module 1** (device encryption verified) → **Module 2** (hardware keys received + registered) → **Module 6** (credential compartmentalization requires knowing your full account landscape, which Module 2 forces you to audit)

Modules 3, 4, and 5 are parallel tracks that can run simultaneously and do not block each other or the critical path.

Module 7 (threat model + continuous improvement) depends on having all modules in place, but its initial setup can begin as soon as Module 3 is complete (monitoring sources and review calendar don't require other modules).

### Recommended Module Ordering

**Day 1**: Order YubiKeys (Module 2). Set up Mullvad VPN on Windows + iPhone (Module 3). This takes ~2 hours and establishes the two highest-impact protections immediately.

**Days 2–7**: Deploy email aliases and Signal hardening (Module 4). Review location settings and physical security habits (Module 5). These are lower friction and fill the week while hardware ships.

**Days 8–12** (when YubiKeys arrive): Register keys on all critical accounts (Module 2). This is the most time-intensive active work in Phase 2.

**Days 10–14**: Verify Phase 1 encryption, create VeraCrypt containers, check Linux setup (Module 1). This parallels Module 2 registration.

**Days 14–18**: Credential compartmentalization audit, breach monitoring setup, rights protocol (Module 6).

**Days 19–21**: Threat model documentation, monitoring subscriptions, first quarterly review setup (Module 7).

### Decision Tree: "What Should I Prioritize?"

```
My primary threat is corporate tracking and data broker exposure
→ Fast track: Modules 3, 4, 7, then 1, 2
→ Module 5 optional; Module 6 optional

My primary threat is law enforcement or government surveillance
→ Comprehensive track in order: 1, 3, 2, 4, 6, 5, 7

My primary threat is targeted harassment / doxxing
→ Fast track: 4 (email aliases + PII), 5 (physical footprint), 7, then 1, 2

I am an activist or journalist at elevated risk
→ Comprehensive track all 7 modules; seek expert review before high-risk activities

I want maximum protection with minimum ongoing overhead
→ Modules 1, 2, 3, 7 (these are largely "set and forget" after initial setup)
```

### Milestone Gates

**Gate 1 (end of Week 1)**: Mullvad VPN running and verified on all devices. This is the single highest-impact change. If nothing else happens in Phase 2, this alone moves the needle significantly.

**Gate 2 (when hardware arrives, ~Day 7)**: YubiKeys registered on Gmail and Bitwarden. The two accounts that everything else depends on.

**Gate 3 (end of Week 2)**: All critical accounts have hardware keys registered OR TOTP with Ente Auth (for services not supporting hardware keys). No account uses SMS 2FA.

**Gate 4 (end of Week 3)**: Breach monitoring active, incident response protocol documented, quarterly review calendar set.

**Gate 5 (90 days post-completion)**: First quarterly review completed and threat model updated.

---

## Section 4: Resource Compendium

### Tools Inventory

#### Authentication and Access Control

| Tool | Cost | Open Source | Maintained | Key Feature | Alternative |
|------|------|-------------|-----------|-------------|-------------|
| YubiKey 5 NFC | $60/key | No | Yes (Yubico) | FIDO2 + TOTP + PIV + NFC | SoloKeys Solo 2 |
| YubiKey Security Key NFC | $30/key | No | Yes | FIDO2 only; budget option | OnlyKey |
| SoloKeys Solo 2 | $50/key | Yes | Yes | Open-source firmware; FIDO2 | YubiKey |
| Bitwarden | Free / $10/yr | Yes | Yes | Password manager + hardware key 2FA | 1Password |
| Ente Auth | Free | Yes | Yes | TOTP authenticator; encrypted backup | Aegis (Android) |

#### Device Encryption

| Tool | Cost | Open Source | Maintained | Key Feature | Alternative |
|------|------|-------------|-----------|-------------|-------------|
| VeraCrypt | Free | Yes | Yes | Cross-platform; containers + full-disk | LUKS (Linux) |
| BitLocker | Free (Win Pro) | No | Yes (Microsoft) | Native Windows; TPM integration | VeraCrypt |
| macOS FileVault | Free | No | Yes (Apple) | Native macOS; hardware-backed | VeraCrypt |
| Linux LUKS | Free | Yes | Yes | Native Linux FDE | VeraCrypt |

#### Network Privacy

| Tool | Cost | Open Source | Maintained | Key Feature | Alternative |
|------|------|-------------|-----------|-------------|-------------|
| Mullvad VPN | $5/month | Yes (client) | Yes | Swedish jurisdiction; no-log verified | ProtonVPN |
| ProtonVPN | $4–10/month | Yes | Yes | Swiss jurisdiction; audited | Mullvad |
| Mullvad Browser | Free | Yes | Yes | Fingerprint-resistant; Tor-developed | LibreWolf |
| Tor Browser | Free | Yes | Yes | Three-hop onion routing; strongest anonymity | I2P |
| uBlock Origin | Free | Yes | Yes | Ad + tracker blocking | Privacy Badger |

#### Communication Security

| Tool | Cost | Open Source | Maintained | Key Feature | Alternative |
|------|------|-------------|-----------|-------------|-------------|
| Signal | Free | Yes | Yes | E2E messaging; sealed sender; minimal metadata | Matrix/Element |
| Briar | Free | Yes | Yes | Offline mesh; no server; Tor-routed | Meshtastic |
| SimpleLogin | Free (15 aliases) / $30/yr | Yes | Yes | Email aliases; Proton ecosystem | Apple Hide My Email |
| MAT2 | Free | Yes | Yes | Metadata stripping; CLI; Linux | ExifTool |
| ProtonMail | Free / $4/month | Yes | Yes | Encrypted email; Swiss jurisdiction | Tutanota |

#### Physical Security

| Tool | Cost | Open Source | Notes |
|------|------|-------------|-------|
| Mission Darkness Faraday bag | $30–60 | No | Hardware signal blocking; phone/laptop sizes |
| Prepaid Android (cash) | $50–80 | N/A | Burner device for high-risk events |
| N95 mask | $1–5 each | N/A | Facial recognition degradation |

#### Monitoring and Auditing

| Tool | Cost | Open Source | Maintained | Key Feature |
|------|------|-------------|-----------|-------------|
| HaveIBeenPwned | Free | No | Yes | Breach email monitoring |
| EFF Cover Your Tracks | Free | Yes | Yes | Browser fingerprint testing |
| DNS Leak Test | Free | No | Yes | VPN DNS leak verification |
| ADS-B Exchange | Free | Yes | Yes | Aerial surveillance plane tracking |
| USASpending.gov | Free | N/A | Yes | Government surveillance procurement |

### External Learning Resources

#### Foundations

- [EFF Surveillance Self-Defense](https://ssd.eff.org) — The most comprehensive, practical, free guide to digital security for at-risk populations. Read every module.
- [Security in a Box](https://securityinabox.org) — Practical tool guides by Frontline Defenders, focused on activists and journalists.
- [Access Now Digital Security Helpline](https://www.accessnow.org/help/) — Free expert help for civil society organizations and journalists.
- [Freedom of the Press Foundation Security Training](https://freedom.press/training/) — Journalist-specific; covers source protection and device security.
- [Privacy Guides](https://www.privacyguides.org) — Curated privacy tool recommendations with detailed rationales.

#### Threat Modeling

- [LINDDUN Privacy Threat Modeling Framework](https://linddun.org) — Systematic framework for identifying privacy threats; academic but accessible.
- [Zero Trace Hub Threat Modeling Guide](https://www.zerotracehub.com/opsec/threat-modeling-guide/) — Practical personal OpSec threat modeling.
- [EFF: Assessing Your Threat Model](https://ssd.eff.org/module/your-security-plan) — Simplified personal threat modeling walkthrough.
- [Cybersecurity Dive: STRIDE vs. LINDDUN vs. PASTA](https://www.cybersecuritydive.com/news/cyber-threat-modeling-framworks-STRIDE-LINDDUN-decision-trees/713587/) — Framework comparison article.

#### Signal and Communications

- [Library Freedom Project Signal Best Practices (2026)](https://libraryfreedom.org/wp-content/uploads/2026/01/signal-best-practices.pdf) — Current Signal hardening guide.
- [Signal: How We Handle Government Requests](https://signal.org/bigbrother/) — Signal's minimal data policy in practice.
- [Protect Democracy Coalition Security Guide (March 2026)](https://protectdemocracy.org/wp-content/uploads/2026/03/Security-Coalition-Guide.pdf) — Group OpSec for coalitions.
- [Consumer Reports: How to Use Signal](https://www.consumerreports.org/electronics-computers/privacy/how-to-use-signal-app-secure-messaging-a4159663583/) — Accessible introductory guide.
- [RedSec Labs: Signal Disappearing Messages and iOS Alerts](https://www.redseclabs.com/blog/signal-disappearing-messages-fbi-ios-notification-database/) — Forensic analysis of Signal metadata risks.

#### VPN and Network Security

- [Mullvad: Why We Support Sending Cash](https://mullvad.net/help/sending-cash/) — Anonymous payment guide.
- [Mullvad Transparency Reports](https://mullvad.net/en/blog/tag/transparency) — Warrant canary and data request history.
- [EFF Cover Your Tracks](https://coveryourtracks.eff.org) — Live browser fingerprinting test.
- [Factually: Privacy Browser Comparison 2026](https://factually.co/fact-checks/electronics-tech/best-privacy-first-browsers-2026-mullvad-tor-librewolf-brave-comparison-694b3f) — Current browser comparison.
- [DNS Leak Test](https://dnsleaktest.com) — Verify your VPN is not leaking DNS queries.

#### Encryption

- [VeraCrypt Documentation](https://veracrypt.fr/en/Documentation.html) — Complete usage guide.
- [Comparison: BitLocker vs. VeraCrypt (2026)](https://cryptoexpert-online.com/guides/bitlocker-vs-veracrypt/) — Detailed feature comparison.
- [Apple Advanced Data Protection Documentation](https://support.apple.com/en-us/HT212520) — Official Apple guide.

#### Legal Rights and Incident Response

- [EFF Know Your Rights](https://www.eff.org/know-your-rights) — Rights during device seizure and at protests.
- [EFF: Attending a Protest](https://ssd.eff.org/module/attending-protest) — Device security and rights for protest situations.
- [National Lawyers Guild](https://www.nlg.org) — Legal support for activists; arrest hotline 212-679-6018.
- [ACLU: Your Rights at a Protest](https://www.aclu.org/know-your-rights/protest-and-free-speech) — First Amendment and law enforcement rights.
- [Cloudflare: What is a Warrant Canary?](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/) — Explanation of warrant canaries.

#### Surveillance Landscape and Threat Intelligence

- [Palantir Threat Model (this project)](projects/cybersecurity-hardening/palantir-threat-model.md) — Detailed analysis of current surveillance platform capabilities.
- [DHS HART Biometric Platform](https://www.dhs.gov/science-and-technology/biometrics) — Official DHS documentation.
- [Privacy International: Facial Recognition Regulation](https://privacyinternational.org/long-read/5682/toward-regulation-addressing-legal-void-facial-recognition-technology) — Legal analysis of facial recognition use.
- [ADS-B Exchange](https://adsbexchange.com) — Real-time aerial surveillance tracking.
- [USASpending.gov](https://usaspending.gov) — Government surveillance procurement database.
- [Brennan Center Justice](https://www.brennancenter.org) — Constitutional law analysis of surveillance programs.

#### Data Brokers

- [EasyOptOuts](https://easyoptouts.com) — Automated data broker removal; $20/year; 100+ sites.
- [DeleteMe](https://www.deleteme.com) — More comprehensive; $130/year; 750+ sites; human-verified.
- [OffList: How to Remove Your Data from Data Brokers](https://www.offlist.me/how-to-remove-your-data-from-data-brokers) — Manual opt-out guide.
- [HaveIBeenPwned](https://haveibeenpwned.com) — Breach monitoring; free email alerts.

#### Community and Expert Contacts

- [Access Now Digital Security Helpline](https://www.accessnow.org/help/) — Free expert security consultation for civil society; response within 24 hours.
- [Freedom of the Press Foundation](https://freedom.press/training/) — Journalist security training; contact via https://freedom.press.
- [Electronic Frontier Foundation](https://www.eff.org/about/offices/legal-referrals) — Legal referrals for digital rights cases.
- [Frontline Defenders](https://www.frontlinedefenders.org/en/security) — Security support for human rights defenders globally.
- [Reddit r/privacy](https://www.reddit.com/r/privacy/) — Community discussion; good for tool questions, not specific threat situations.
- [Reddit r/netsec](https://www.reddit.com/r/netsec/) — Technical security community; for advanced questions.
- [Security.StackExchange](https://security.stackexchange.com) — Q&A for specific technical security questions.
- Security conferences for staying current: DEF CON (Las Vegas, August), RSA Conference (San Francisco, May), PrivacyCon (FTC-organized, Washington DC, typically spring).

### Budget Estimate

#### Low-Cost Path: ~$55–75/year

Focus: VPN + browser hardening + behavioral practices. Covers commercial tracking and most ISP/DNS exposure.

| Item | Cost |
|------|------|
| Mullvad VPN | $60/year |
| Bitwarden free tier | Free |
| Signal | Free |
| Mullvad Browser + Tor | Free |
| VeraCrypt | Free |
| SimpleLogin (15 aliases) | Free |
| EasyOptOuts data broker removal | $20/year |
| **Total** | **~$80/year** |

What this covers: ISP tracking, most browser fingerprinting, email compartmentalization, basic data broker exposure. Does not cover hardware key authentication.

#### Moderate Path: ~$200–250 total first year

Focus: All low-cost tools plus hardware security keys.

| Item | Cost |
|------|------|
| Everything from low-cost path | $80 |
| 2x YubiKey 5 NFC | $120 |
| **Total first year** | **~$200** |
| **Annual recurring** | **~$80** |

What this covers: All of the above plus phishing-proof authentication. The YubiKeys are a one-time purchase (keys last 5+ years with normal use).

#### Comprehensive Path: ~$350–500 total first year

Focus: Full protection including physical security hardware, automated data broker monitoring, and professional email.

| Item | Cost |
|------|------|
| Everything from moderate path | $200 |
| DeleteMe automated removal (upgrade from EasyOptOuts) | +$110 |
| Mission Darkness Faraday bag | $50 |
| Prepaid Android device (cash) | $50–80 |
| 3rd YubiKey (additional backup) | $60 |
| ProtonMail Plus (encrypted email hosting) | $48/year |
| **Total first year** | **~$520** |
| **Annual recurring** | **~$220** |

What this covers: Everything above plus hardware physical security, professional encrypted email hosting, and comprehensive data broker removal.

---

## Section 5: Success Metrics and Graduation Criteria

### What Does "Phase 2 Complete" Mean?

Phase 2 is complete when:
1. All devices have verified active full-disk encryption
2. Hardware security keys are registered on all critical accounts (email, password manager, banking, primary identity accounts)
3. Mullvad VPN is running with kill switch on all devices, connection verified
4. Disappearing messages are active on all Signal chats; phone number is hidden
5. At minimum 5 email aliases deployed; no new accounts created with real email
6. Bitwarden password health report shows 0 reused, 0 exposed passwords
7. HaveIBeenPwned monitoring active for all email addresses
8. Quarterly review calendar set for next 2 years
9. Incident response protocol documented; rights phrase memorized; lawyer contact accessible

### Verification Checklist (Module-by-Module)

**Module 1 — Device Encryption**
- [ ] BitLocker/FileVault/LUKS: "On" on all devices
- [ ] VeraCrypt container created, tested, sensitive files migrated in
- [ ] VeraCrypt pre-boot: password prompt appears before Windows loads (if using)
- [ ] Recovery keys: saved in Bitwarden + physical paper copy
- [ ] Screen lock: 5–15 minute timeout on all devices

**Module 2 — Hardware Security Keys**
- [ ] 2x hardware keys received
- [ ] Both keys registered on Gmail and Bitwarden (minimum)
- [ ] Both keys registered on Apple ID, banking, GitHub (expand to all critical accounts)
- [ ] Recovery codes saved in Bitwarden + printed
- [ ] Test: log in with hardware key only (no TOTP)
- [ ] Test: log in with recovery code only
- [ ] Backup key stored at separate physical location

**Module 3 — Network Anonymization**
- [ ] Mullvad connected + kill switch on (Windows)
- [ ] Mullvad connected + always-on VPN (iPhone)
- [ ] https://mullvad.net/en/check: connected
- [ ] https://dnsleaktest.com: clean (only Mullvad DNS)
- [ ] https://coveryourtracks.eff.org (Mullvad Browser): strong protection
- [ ] Kill switch test: VPN off → traffic fails (doesn't fall back to ISP)
- [ ] uBlock Origin installed in daily-use browser

**Module 4 — Metadata Minimization**
- [ ] Signal: phone number hidden from all contacts
- [ ] Signal: disappearing messages on all chats (1 week default minimum)
- [ ] Signal: read receipts off, typing indicators off, link previews off
- [ ] Safety numbers verified with 2+ most-trusted contacts
- [ ] 5+ SimpleLogin aliases deployed and in Bitwarden
- [ ] Last photo sent: GPS coordinates verified absent from EXIF data

**Module 5 — Physical Security**
- [ ] All iPhone apps: location access reviewed and set appropriately
- [ ] Significant Locations: disabled
- [ ] USB accessories while locked: disabled
- [ ] Secure Boot: enabled in UEFI
- [ ] Data broker search (Spokeo, BeenVerified): completed; no current address exposure (or opt-outs submitted)
- [ ] High-risk event protocol decided: Airplane mode or Faraday bag

**Module 6 — Organizational OpSec**
- [ ] Bitwarden password health: 0 reused passwords, 0 exposed
- [ ] SMS 2FA: removed from all accounts with alternatives
- [ ] HaveIBeenPwned monitoring: active for all email addresses
- [ ] Rights phrase: memorized
- [ ] Lawyer contact: memorized or on physical card
- [ ] Active sessions: reviewed on Gmail, Apple ID, Bitwarden; unfamiliar sessions revoked
- [ ] Trusted person: knows backup key location

**Module 7 — Threat Model Refresh**
- [ ] Threat model document: written and saved in Bitwarden
- [ ] 4 monitoring sources: subscribed
- [ ] Quarterly review calendar: set for next 2 years
- [ ] Expert help channels: bookmarked
- [ ] First quarterly review: completed (within 90 days)

### Threat-Specific Validation

| Threat | Test |
|--------|------|
| ISP can see my browsing | Visit https://mullvad.net/en/check — should show Mullvad IP, not ISP |
| My location is tracked via apps | Settings → Privacy → Location Services → verify all apps on "Never" or "While Using" only |
| My email can be traced to me | Create a SimpleLogin alias; send email from that alias; verify reply address shows alias, not real email |
| My account can be phished | Attempt to log into Gmail on a test fake-domain (phishing simulation sites exist) — hardware key should reject |
| Data brokers have my home address | Search your name on Spokeo.com — "Not found" or outdated address |
| My communication metadata can map my social network | Signal: verify phone number is hidden; verify disappearing messages are on |
| My device can be forensically read if seized | Power off your computer; restart — confirm encryption passphrase prompt appears before OS loads |

### Confidence Assessment Framework

Rate each module on a 1–5 scale:

| Rating | Meaning |
|--------|---------|
| 5 | Implemented and tested; verified working |
| 4 | Implemented; not fully tested |
| 3 | Partially implemented |
| 2 | Planned but not started |
| 1 | Not started |

A Phase 2 "graduation" score: average across all 7 modules ≥ 4.0, with no module below 3.

### Post-Phase-2 Monitoring

After Phase 2 is complete, ongoing maintenance is minimal:

| Task | Frequency | Time |
|------|-----------|------|
| Data broker search (Spokeo, BeenVerified) | Quarterly | 10 min |
| HaveIBeenPwned check | Quarterly (+ email alerts) | 5 min |
| Security tool updates verified | Monthly | 5 min |
| Mullvad VPN status check | Weekly or daily | 1 min |
| Threat model review and update | Quarterly | 20 min |
| Signal contact list audit | Quarterly | 10 min |
| Active sessions review (Gmail, Apple) | Quarterly | 10 min |

**Total ongoing: ~1 hour/quarter after Phase 2 is complete.**

---

## Section 6: User Decision Tree

Different threat models lead to different Phase 2 priorities. Use this tree to determine your ordering.

### Start Here: What is your primary concern?

**A. I primarily want to stop commercial tracking and data broker exposure**
- Essential modules: 3 (VPN), 4 (email aliases + metadata), 7 (monitoring)
- Important: 1 (device encryption verification), 5 (location review)
- Optional: 2 (hardware keys — adds protection against account takeover), 6 (incident response)
- Timeline: 2 weeks, ~6–8 hours total
- Cost: $80–100/year

**B. I want protection against government surveillance and law enforcement**
- Essential modules: All 7, in order: 1, 3, 2, 4, 6, 5, 7
- Do not skip Module 2 (hardware keys) or Module 6 (incident response + rights protocol)
- Consider consulting Access Now Digital Security Helpline before high-risk activities
- Timeline: 3 weeks, ~12–15 hours
- Cost: $200–300/year

**C. I am primarily concerned about targeted harassment or doxxing**
- Essential modules: 4 (PII compartmentalization + email aliases), 5 (data broker audit + physical footprint), 7 (monitoring)
- Important: 2 (hardware keys prevent account takeover by harassers), 6 (breach monitoring + session audit)
- Optional: 1, 3
- Timeline: 2 weeks, ~7–9 hours
- Cost: $80–150/year

**D. I am a journalist or activist at elevated risk**
- All 7 modules, comprehensive track
- Seek professional security review from Access Now or Freedom of the Press Foundation before undertaking sensitive activities
- Consider a GrapheneOS device for the most sensitive work (not covered in this guide — requires separate research)
- Timeline: 3–4 weeks, ~15–20 hours
- Cost: $350–500/year

**E. I have limited time and just want to do the most important things**
- Do these 4 in order (the highest-impact, lowest-overhead setup):
  1. Module 3: Mullvad VPN (2 hours; ongoing: 0)
  2. Module 2: Hardware security keys (2–3 hours once hardware arrives; ongoing: 0)
  3. Module 4: Signal hardening + email aliases (2 hours; ongoing: minimal)
  4. Module 7: Quarterly review calendar + monitoring sources (1 hour initial)
- Total: ~7–8 hours
- Cost: $200 initial + $80/year

### Module Priority Quick Reference

| If you care most about... | Start with... |
|--------------------------|---------------|
| Hiding internet traffic from ISP | Module 3 (VPN) |
| Preventing account takeover | Module 2 (hardware keys) |
| Stopping data broker exposure | Module 4 Part C (email aliases) + Module 5 Part E (footprint check) |
| Communication security | Module 4 Parts A–B (Signal + Briar) |
| Physical surveillance | Module 5 |
| Breach and legal resilience | Module 6 |
| Staying current as threats evolve | Module 7 |
| Everything (comprehensive protection) | Module 1 → 3 → 2 → 4 → 6 → 5 → 7 |

---

## Section 7: Failure Modes and Recovery

### If a Module Fails or Doesn't Work

**Mullvad VPN (Module 3) won't connect**
- First check: do you have an active subscription? Mullvad App → your account number → "Time remaining" should show > 0.
- Check firewall: Windows Defender Firewall may be blocking Mullvad. Windows Settings → Firewall → Allow an app → verify Mullvad is allowed.
- Try a different server: click the server location → choose a different country.
- Reinstall: uninstall Mullvad completely, reboot, reinstall from https://mullvad.net/en/download.
- Support: https://mullvad.net/en/help (no email required)

**YubiKey not recognized (Module 2)**
- Ensure the key is fully inserted into the USB port.
- Try a different USB port (USB-A vs USB-C adapter issues are common).
- On some Windows machines, YubiKey may need the Yubico Authenticator app: https://www.yubico.com/products/yubico-authenticator/
- For NFC on iPhone: hold key flat against the top-back of the iPhone where the NFC chip is located (not the charging port).
- If a service isn't accepting the key: check that the service supports FIDO2 (not just "security key" labeling — some services use an older U2F standard that requires the key in USB mode, not NFC).

**VeraCrypt container won't mount (Module 1)**
- Confirm you are using the correct passphrase. Passphrases are case-sensitive.
- Verify the container file is not corrupted: VeraCrypt → Tools → "Restore volume header from embedded backup." This recovers a backup header stored within the container.
- If the container is corrupted beyond recovery: restore from backup. (This is why keeping a backup copy of the container — encrypted — in a second location matters.)
- Never delete a VeraCrypt container without dismounting it first.

**BitLocker recovery key needed**
- If you saved your BitLocker recovery key in Bitwarden: open Bitwarden from another device, retrieve the key.
- If you saved it to a Microsoft account: go to https://account.microsoft.com/devices/recoverykey from another device.
- If you printed it: use the printed copy.
- If none of the above are available: the data is inaccessible without the recovery key. There is no backdoor.

**SimpleLogin alias not receiving mail (Module 4)**
- Check SimpleLogin's status page for outages: https://simplelogin.io (footer links)
- Verify the alias is enabled (aliases can be individually toggled off)
- Check your spam folder — mail from SimpleLogin may be marked spam by aggressive filters
- Verify the alias is properly forwarding to your real email: SimpleLogin → Aliases → alias name → "Mailboxes" → should show your real email

**YubiKey lost (Module 2)**
- Immediately log into all accounts where the key was registered.
- In each account's Security settings: remove the lost key from the list of registered security keys.
- Log in using your backup YubiKey (this is why you have two).
- Order a replacement key and register it.
- Update Bitwarden's secure note listing your registered keys.

**Device seized by law enforcement (Module 6)**
- Say nothing except your name and "I want a lawyer." Do not explain your security setup.
- As soon as you have access to another device: change Gmail password, change Bitwarden master password, revoke active sessions on all critical accounts.
- Contact your lawyer immediately. Do not communicate with law enforcement without representation present.
- Consider contacting EFF (https://www.eff.org/about/offices/legal-referrals) if you need referral to a digital rights attorney.
- Document: write down the time, date, location, and officers' badge numbers of the seizure.

**Passphrase forgotten (device locked out)**
- BitLocker: use recovery key (saved in Bitwarden or on printed paper)
- VeraCrypt container: no recovery without passphrase — this is by design. Restore from backup if available.
- iPhone: if Advanced Data Protection is on and you've lost your recovery key, data recovery is not possible. You can erase the device from iCloud.com to regain access to a new setup.
- Bitwarden: Bitwarden account recovery requires either the emergency access feature (set up in advance with a trusted contact) or a verified email address. If you've lost your master password AND haven't set up emergency access, contact Bitwarden support — recovery options are limited by design.

### Rollback Procedures

**If Mullvad VPN creates problems (site incompatibilities, streaming services blocked)**
- Mullvad → Disconnect to temporarily use your real IP for specific services
- Mullvad → Settings → "Mullvad VPN exclusions" (Split tunneling): add specific apps that should bypass VPN (e.g., streaming services). This allows selective VPN use.
- Kill switch: disable temporarily if you need to access a site that blocks VPN IPs. Re-enable immediately after.

**If hardware keys lock you out of an account**
- Use recovery codes (you saved these in Bitwarden and printed a copy).
- Recovery codes are single-use — each used code is invalidated. After using, generate new recovery codes from the service.

**If you want to revert a Phase 2 change entirely**
- Hardware keys: deregister from account security settings, revert to TOTP (Ente Auth)
- Mullvad: uninstall the app; your IP returns to your ISP IP immediately
- VeraCrypt container: move files out, delete the container file
- Email aliases: disable the alias in SimpleLogin; update your login to use the real email

### When to Seek Expert Help

Self-service (this guide) is appropriate for implementing known best practices. Seek professional expertise when:

- You believe you are currently under active surveillance
- You receive any legal process: subpoena, search warrant, NSL, civil subpoena from hostile party
- You are planning a specific high-risk action (whistleblowing, investigative journalism on powerful targets, organizing that may attract law enforcement attention)
- Your threat model changes dramatically (new adversary, new risk surface)
- Something in your current setup is behaving unexpectedly and you cannot diagnose it

**Expert resources**:
- Access Now Digital Security Helpline: https://www.accessnow.org/help/ (free; response within 24 hours; for civil society and journalists)
- Freedom of the Press Foundation: https://freedom.press/training/ (journalist-specific)
- EFF legal referrals: https://www.eff.org/about/offices/legal-referrals (for active legal matters)
- National Lawyers Guild arrest line: 212-679-6018 (immediate arrest situations)
- Frontline Defenders: https://www.frontlinedefenders.org/en/security (human rights defenders globally)
- Reddit r/privacy: https://www.reddit.com/r/privacy/ (tool questions, general guidance — not for specific threat situations involving personal identifying details)
- Security.StackExchange: https://security.stackexchange.com (specific technical questions)

---

*Document version: 1.0 | Created: 2026-05-19 | Status: Ready for May 25–27 user review | Implementation start target: June 2–3, 2026 (post Phase 1 completion)*
