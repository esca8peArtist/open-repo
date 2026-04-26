---
title: "Device Hardening Guide: iOS and Android Against Government Surveillance"
project: cybersecurity-hardening
created: 2026-04-26
status: complete
depends_on: threat-model.md, opsec-playbook.md
confidence: high — grounded in primary source documentation (Apple legal guidelines, GrapheneOS project, Cellebrite leaked capability matrices, EFF Surveillance Self-Defense, academic forensics research)
---

# Device Hardening Guide: iOS and Android Against Government Surveillance

**Purpose**: This guide provides practical, technically grounded device hardening for people facing government-level surveillance. It is not a general privacy tutorial — it maps device-level defenses directly to confirmed threat capabilities documented in `threat-model.md`. Every recommendation has a specific threat rationale.

**Tier structure** (consistent with `opsec-playbook.md`):
- **Tier 1** — Journalists, immigration advocates, labor organizers. Primary threat: administrative data pipelines and OSINT aggregation.
- **Tier 2** — Activists, civil rights litigants, protest organizers. Primary threat: IMSI catchers, device seizure, social media surveillance.
- **Tier 3** — Direct investigation targets, national security sources, people with confirmed legal process. Primary threat: advanced persistent access, forensic device extraction, targeted spyware.

---

## Part 1: iPhone Hardening

### 1.1 The Fundamental Trade-off

iPhones offer a strong, closed security model with excellent hardware integration and a locked bootloader — but they route significant data through Apple's servers, which Apple can and does disclose to law enforcement under appropriate legal process. The key question is not whether Apple has good intentions, but what legal obligations Apple faces and what data Apple actually holds.

Apple's October 2025 law enforcement guidelines confirm the following breakdown:

| Legal instrument | What Apple provides |
|---|---|
| Subpoena | Account information (name, address, email), iCloud metadata, transaction records |
| Court order (18 U.S.C. §2703(d)) | iCloud content if not end-to-end encrypted: contacts, calendars, notes, Safari bookmarks, photos, iMessages stored in cloud |
| Search warrant | Everything above plus device backup contents, full iCloud data if not under Advanced Data Protection |
| Cannot provide even with warrant | End-to-end encrypted data under Advanced Data Protection; device contents (Apple cannot unlock iPhones) |

The critical variable is whether **Advanced Data Protection (ADP)** is enabled. With ADP off (the default), Apple holds decryption keys for most iCloud data and will hand it over under a warrant. With ADP on, Apple cannot decrypt it. However, Apple confirmed in a high-profile case that [enabling ADP does create a genuine barrier to lawful access](https://warrantbuilder.com/advanced-data-protection/).

### 1.2 Passcode and Biometrics

**Use an alphanumeric passcode, not a 6-digit PIN.** The Fifth Amendment right against self-incrimination has been held by several courts to protect compelled passcode disclosure — you cannot be legally forced to reveal what you know. Biometrics, however, are physical characteristics courts have found are not protected in the same way. Law enforcement officers are trained to use biometrics quickly when detaining someone.

**Practical action**: Settings → Face ID & Passcode → turn off Face ID for iPhone Unlock if facing arrest risk. Re-enable afterward. Alternatively, press the side button and volume button simultaneously to trigger SOS mode, which disables Face ID until the passcode is re-entered.

### 1.3 iCloud: The Principal Attack Surface

Standard iCloud is the most productive target for government legal process against iPhone users. The data set Apple holds under a standard account includes 12 months of iMessage metadata even without device access, all iCloud-synced app data, and full device backups.

**Three-tier backup strategy by risk level**:

- **Tier 1**: Enable Advanced Data Protection (Settings → [your name] → iCloud → Advanced Data Protection). This end-to-end encrypts iCloud backups, documents, photos, and notes. Apple cannot decrypt them under any legal order. Trade-off: if you forget your passcode and lose your recovery key, you will lose your data. This is the correct trade-off for Tier 1 and above.

- **Tier 2**: Disable iCloud backup entirely. Use only local encrypted backups (iTunes/Finder, with a strong backup password). A local encrypted backup is not accessible to law enforcement without the encryption password, which enjoys Fifth Amendment protection. Local backups also back up items (like passwords) that are excluded from non-encrypted backups.

- **Tier 3**: No cloud backup. Local backup on an encrypted device that stays in a physically secure location. Or no backup at all — accept that data loss is the cost of non-recoverability.

### 1.4 Airplane Mode vs. Full Power-Off

**This distinction matters more than most guides acknowledge.**

Airplane mode disables the cellular radio, but as of iOS 15.5 and later, it does not fully silence the device if "Find My" is enabled. When you power off a modern iPhone (iPhone 11 or later) with Find My active, the phone enters a **low-power Bluetooth beacon mode** — the Bluetooth radio continues to transmit a rotating cryptographic identifier that any nearby Apple device can detect and report to Apple's servers. This continues for up to 24 hours after shutdown.

What this means for surveillance:
- **Airplane mode** disables cellular (no IMSI catcher risk, no carrier location data), but Wi-Fi and Bluetooth may re-enable silently, and apps can still use cached GPS data.
- **Power-off with Find My enabled** provides cellular silence but continues Bluetooth beaconing through nearby Apple devices.
- **Power-off with Find My disabled** (Settings → [your name] → Find My → Find My iPhone → toggle off) provides the most complete RF silence short of a Faraday pouch.

**Practical recommendation for Tier 2+**: Before sensitive meetings, power off and disable Find My first — or use a Faraday pouch after confirming the device is powered off. The pouch ensures no RF emission regardless of software state.

### 1.5 Lockdown Mode

Lockdown Mode (iOS 16+) is Apple's hardening mode for people facing targeted mercenary spyware (Pegasus, Predator, commercial zero-click exploits). It should be understood as a Tier 3 tool with Tier 2 utility.

What Lockdown Mode specifically blocks:
- Most attachment types in Messages (images allowed; documents, most links, link previews blocked)
- JIT JavaScript compilation in Safari (dramatically reduces browser attack surface; breaks some sites)
- Incoming FaceTime from non-contacts
- Location metadata stripped from shared photos
- Wired connections to accessories when locked
- Configuration profile installation

What it does not protect against: social engineering, metadata collection, network surveillance, carrier-level IMSI tracking.

**Recommendation**: Enable Lockdown Mode for any Tier 3 individual. Consider it for Tier 2 people who have attended protests or are subjects of monitoring. The usability cost (some websites break, some attachments don't open) is acceptable given the threat level.

Enable at: Settings → Privacy & Security → Lockdown Mode → Turn On Lockdown Mode.

### 1.6 SIM Swapping: The Carrier Vulnerability

SIM swapping is an attack on your carrier account, not your device. An attacker convinces your carrier's customer service (via social engineering or bribed insiders) to transfer your phone number to a SIM they control. Once successful, they receive your SMS messages including all SMS-based 2FA codes, potentially taking over every account that uses your phone number for recovery.

This is not a theoretical threat. T-Mobile paid $33 million in arbitration in early 2025 after a SIM swap led to $38 million in cryptocurrency theft. The FCC mandated carrier notification requirements effective mid-2024.

**Countermeasures in priority order**:

1. **Set a carrier port-out PIN** — distinct from your SIM PIN. On AT&T, call customer service and enable "Extra Security." On T-Mobile, enable SIM Protection in the app. On Verizon, enable Number Lock. These require a PIN or in-person verification before any SIM change. This is the highest-impact single action.

2. **Set a SIM PIN** (Settings → Cellular → SIM PIN). This PIN is required every time the device reboots or exits airplane mode. It prevents physical SIM removal and re-insertion in another device. This addresses physical theft, not social engineering.

3. **Remove SMS from all 2FA**. Every account that uses SMS as a 2FA factor is vulnerable to SIM swap. Replace SMS 2FA with a hardware key (YubiKey) or authenticator app (Ente Auth, Raivo). FIDO2/WebAuthn keys are immune to both SIM swapping and phishing.

4. **Consider eSIM-only** if your carrier supports it. eSIM swapping is harder to execute than physical SIM swapping (requires device-level authentication, not just a call to customer service), though not impossible.

### 1.7 Physical Security and Faraday Pouches

**Border crossing protocol** (EFF, June 2025):
- Power off the device completely before reaching the checkpoint
- Enable full-disk encryption (iPhones use hardware encryption by default; the passcode activates it)
- Use an alphanumeric passcode, not biometrics
- If ordered to unlock: you may decline (legal right at U.S. borders is contested — courts are divided — but you can decline and face potential device seizure)
- If the device is taken: request a Form 6051D (custody receipt), document what forensic equipment is connected, and assume the device is compromised until you can factory reset it

**Faraday pouches**: Military-grade bags (Mission Darkness, GoDark) independently tested to exceed 100 dB EMF attenuation, blocking all cellular, Wi-Fi, Bluetooth, GPS, and 5G signals. This is the only reliable way to guarantee RF silence regardless of software state. Use when:
- Entering sensitive meetings where device-as-microphone risk is a concern (a device with malware can still record audio even in airplane mode; the Faraday pouch prevents exfiltration until the device is removed)
- Storing a powered-on device you cannot monitor
- Traveling through a checkpoint you cannot avoid with a device you've already disabled

### 1.8 Compartmentalization

**The single most important device security decision** is whether your sensitive communications happen on the same device as your daily life. For Tier 2 and above, they should not.

A separate device for sensitive communications provides:
- **Identity separation**: the device has no account history, no location trail, no contact list linking to your identity
- **Compromise containment**: if your daily phone is seized or infected, the sensitive device is unaffected
- **Metadata hygiene**: Signal on a device never associated with your real identity provides much stronger metadata protection

**Practical secondary device setup** (Tier 2):
- Purchase a used iPhone with cash at a retail store, away from home
- Activate with a VoIP number (MySudo, JMP.chat) not linked to your identity
- No Apple ID, or a pseudonymous Apple ID with no payment method
- Install only Signal; no email, no social media
- Never bring to home, work, or locations associated with your identity
- Keep it in a Faraday pouch when not in use

---

## Part 2: Android Hardening

### 2.1 The Platform Choice: GrapheneOS vs. CalyxOS vs. Stock Android

This is not a preference question. For a government-level surveillance threat model, the choice has measurable, documented consequences.

**Stock Android** (any manufacturer): sends data to Google servers approximately 300 times per day, as confirmed by academic measurement research. Location data, app usage, and network metadata flow continuously to Google's infrastructure. Under a subpoena, Google provides account data; under a warrant, Google provides far more. Stock Android is not a credible platform for Tier 2 or above.

**CalyxOS**: A hardened AOSP derivative that replaces Google Play Services with microG (an open-source re-implementation). It reduces Google data flows significantly but microG still maintains some connections to Google's infrastructure. CalyxOS provides meaningful privacy improvement over stock Android with better app compatibility than GrapheneOS. However, CalyxOS historically ships security patches slower than GrapheneOS and implements fewer low-level exploit mitigations. For Tier 1-2 use where compatibility matters more than maximum hardening, CalyxOS is defensible.

**GrapheneOS**: The highest-security Android derivative for which primary evidence exists. Key documented advantages over alternatives:

- **Verified boot re-locking**: GrapheneOS re-locks the bootloader after installation (see section 2.2). This means a seized device in BFU state has the full protection of verified boot, not just the protection of a known-good bootloader.
- **Hardened memory allocator (hardened_malloc)**: Implements metadata protection, zero-on-free, and ARM Memory Tagging Extension support, materially reducing the attack surface for exploits used by Cellebrite and similar forensic tools.
- **USB control**: Disables new USB connections when locked by default. This blocks the primary vector for forensic extraction tools (USB-based exploits targeting locked devices).
- **Auto-reboot**: Default 18-hour auto-reboot returns the device to BFU state, where encryption keys are not in memory. Configurable to 10 minutes for higher security.
- **Cellebrite resistance**: A leaked Cellebrite support matrix (reported February 2025) flagged Pixel devices running GrapheneOS as inaccessible for most extraction scenarios, including BFU and recent security-patch builds, in contrast to standard Pixel devices which had significantly more extraction vectors.

GrapheneOS runs only on Google Pixel devices. The March 2026 partnership announcement with Motorola (MWC 2026) may expand supported hardware.

**Recommendation**: GrapheneOS on a Pixel 8 or Pixel 9 series device is the correct choice for Tier 2 and above. CalyxOS is an acceptable Tier 1 option with better compatibility. Stock Android is not acceptable above Tier 1.

### 2.2 Bootloader Implications: The Critical Paradox

This is the most misunderstood aspect of Android security for custom ROM users.

**The sequence matters**: Installing a custom ROM requires unlocking the bootloader. An **unlocked bootloader** fundamentally weakens the device's security — it allows unsigned code to boot, which means forensic extraction tools can boot into a custom environment to access data even if the device has a strong PIN. This is the primary forensic attack vector against Android devices.

**GrapheneOS's solution**: After installing GrapheneOS, the bootloader is **re-locked** with GrapheneOS's own signing keys. This means:
- Verified boot is active and enforces that only GrapheneOS-signed images can boot
- Forensic extraction tools cannot boot a custom environment to bypass encryption
- The device is functionally as protected as a stock Android device with a locked bootloader — but running GrapheneOS's hardened codebase

**The failure mode**: Installing CalyxOS, LineageOS, or any other custom ROM and leaving the bootloader unlocked provides a false sense of security. The privacy features of the ROM are meaningless if forensic tools can boot around them. Any ROM installation that does not re-lock the bootloader should be considered forensically weaker than stock Android, not stronger.

**Verification**: After installing GrapheneOS, verify the bootloader is relocked by going to Settings → About Phone → Device Identifiers → confirm "OEM unlocking" is grayed out. Alternatively, boot into fastboot (`adb reboot bootloader`) and confirm the status line reads `LOCK STATE - locked`.

### 2.3 BFU vs. AFU: Understanding the Key States

**Before First Unlock (BFU)**: The device has been powered on but the user has not entered their PIN since boot. Encryption keys are not in memory. In BFU state, an attacker with physical access cannot decrypt user data — even with forensic tools — unless they can defeat the secure element's brute-force protections (this requires significant resources or an unpatched vulnerability).

**After First Unlock (AFU)**: The user has entered their PIN at least once. Encryption keys are loaded into memory. Sophisticated forensic tools can potentially extract data via memory attacks even if the screen is subsequently locked.

The practical implication: **power off your phone before any situation where seizure is likely**. A powered-off device is in BFU state. A phone that has been unlocked recently (even if currently screen-locked) is in AFU state and more vulnerable.

GrapheneOS's auto-reboot feature addresses the scenario where you cannot power off: it automatically reboots after the configured period (default 18 hours, minimum 10 minutes), returning the device to BFU state. This protects against scenarios where authorities detain your device overnight before applying for a warrant.

### 2.4 SIM Swapping on Android

The threat and countermeasures are identical to iOS (section 1.6). Android-specific additions:

- **Disable 2G** at the OS level. 2G networks are trivially intercepted and are the primary protocol exploited by IMSI catchers (StingRays). On stock Android: Settings → Network & internet → SIMs → Allow 2G → Off. On GrapheneOS, LTE-only mode is available in network settings and is strongly recommended.
- **GrapheneOS IMSI protections**: GrapheneOS blocks IMSI catching attacks that exploit 2G fallback by defaulting to LTE-only mode and removing the 2G modem firmware from the attack surface when disabled.

### 2.5 App Distribution: F-Droid vs. Play Store

**The counterintuitive recommendation**: For a security threat model (as opposed to a privacy threat model), the Google Play Store is generally safer than F-Droid for most users.

F-Droid's security vulnerabilities, documented by the privsec.dev security research community:
- F-Droid signs all apps with its own keys rather than the developer's keys, requiring trust in a third party
- The F-Droid client historically targeted API level 29 (Android 7.1), missing years of Android security improvements
- The build infrastructure runs on aging servers with delayed security patches
- App updates are delayed (sometimes weeks to months), extending exposure to known vulnerabilities
- No TLS certificate pinning in the client

Google Play Store enforces modern security standards, timely updates from developers, and sandboxing benefits from current Android models. Its weakness is Google's data collection.

**GrapheneOS-specific recommendation**: GrapheneOS includes a sandboxed Google Play layer that allows you to run Google Play Store apps with strictly limited permissions — Google Play Services have no special privileges and cannot access data outside their sandboxed container. This is the correct solution: Play Store's update reliability and app catalog, without the system-level access Google normally receives.

**For apps not available on Play Store**: Download APKs directly from the developer's GitHub releases. Verify the APK signing certificate using `apksigner verify --print-certs app.apk` and compare against the fingerprint published by the developer. Accrescent is an emerging alternative with better security than F-Droid.

### 2.6 Location Data Broker Opt-Out

Location data brokers (Babel Street, Venntel, X-Mode/Outlogic) purchase location data from app SDKs embedded in ordinary consumer apps. This data flows to Palantir ELITE and ImmigrationOS as documented in `threat-model.md`. The threat is not from the phone OS itself but from apps you voluntarily install.

**System-level controls**:
- Settings → Privacy → Ads → Delete advertising ID (Android 12+). This removes the cross-app identifier that enables data brokers to link location records to your profile.
- Settings → Location → App permissions → Audit every app. The only apps that require "Precise" and "Always" location are navigation apps. Everything else should be "Approximate" and "Only while using."
- GrapheneOS extends this with a permission to disable GPS entirely for specific apps (they receive fake location data instead of an error, which prevents apps from detecting the restriction).

**Data broker removal**: The permanent fix requires removing your data from existing broker databases. For California residents, the DROP platform (launched January 1, 2026) allows a single request to reach 500+ registered brokers, with deletion required within 90 days beginning August 1, 2026. Outside California: services like DeleteMe and Optery (ranked #1 by Consumer Reports 2022-2025) automate opt-outs across major brokers. The GitHub repository `yaelwrites/Big-Ass-Data-Broker-Opt-Out-List` provides free manual opt-out links for the highest-traffic brokers.

---

## Part 3: Cross-Platform Considerations

### 3.1 When Full Power-Off Is Required vs. Airplane Mode Sufficient

| Scenario | Airplane Mode | Full Power-Off |
|---|---|---|
| Avoiding IMSI catcher during protest | Sufficient | Not necessary |
| Preventing carrier location data | Sufficient | Not necessary |
| Entering a sensitive meeting | Insufficient alone | Required + Faraday pouch for Tier 3 |
| Preventing iPhone Bluetooth beaconing | Insufficient | Required (with Find My disabled) |
| Device about to be seized by law enforcement | Insufficient | Power off immediately (enter BFU state) |
| Airport/border crossing | Insufficient | Required |
| Preventing malware audio exfiltration | Insufficient (malware queues and sends later) | Required + Faraday pouch |

**Key principle**: Airplane mode addresses network surveillance. Full power-off addresses forensic extraction (enters BFU state). A Faraday pouch addresses RF emission from a device that cannot be trusted to stay off. All three serve different threat vectors.

### 3.2 Device Compartmentalization Strategy

The governing principle: **data that doesn't exist on a device cannot be extracted from it**.

**Recommended profile for Tier 2+ individuals**:

| Device | Purpose | Accounts | Location trail |
|---|---|---|---|
| Primary phone | Daily life, navigation, banking | Real identity | Linked to real identity — accept this |
| Secondary phone | Signal, encrypted communications | Pseudonymous VoIP number | Never at home/work; no carrier SIM if possible |
| Dedicated laptop | Research, document drafting | Tor Browser, no real-identity accounts | No location hardware if possible |

When the secondary phone is not in use, it lives in a Faraday pouch. It never travels to your home or workplace. It does not connect to your home Wi-Fi (which appears in log data). It is charged from a portable battery, not from a home outlet with smart meter connectivity.

### 3.3 Backup and Recovery in a High-Security Context

Cloud backup is an attack surface. Local backup is a physical security dependency. The correct approach:

- **iOS**: Enable Advanced Data Protection. Rotate your recovery key into secure offline storage (paper, locked in a safe). Take periodic local encrypted backups stored on an encrypted external drive that is physically secured. Test restore once to verify the backup is intact.
- **Android (GrapheneOS)**: Use Seedvault for encrypted backups. Back up to USB storage, not a cloud provider. Note that each user profile requires a separate backup. Verify backup integrity.
- **What not to back up**: Signal databases should not be backed up to cloud storage on any platform. Signal's disappearing messages feature reduces the value of backups as an attack surface.

### 3.4 Practical OpSec Workflows

**Daily operations (Tier 1)**:
- Primary iPhone with ADP enabled
- Carrier port-out PIN set, SIM PIN enabled
- All SMS-based 2FA replaced with authenticator app or hardware key
- Advertising ID deleted; location services audited
- Auto-lock set to 30 seconds or less
- Screen notifications hidden on lock screen

**Elevated operations — before a protest, sensitive meeting, or travel (Tier 2)**:
- Secondary device goes into Faraday pouch before departure
- Primary phone: disable Face ID (side button + volume), ensure full-disk encryption is active
- Review and clear recent Signal conversations (enable disappearing messages before the event)
- Leave at home: any device that has location data linked to your daily pattern
- At the event: airplane mode (Tier 2) or power off (Tier 3) primary phone
- After: review and remove any photos with identifiable faces before sharing

**Crisis operations — active legal process or arrest (Tier 3)**:
- Power off all devices immediately upon being approached by law enforcement
- A device powered off and not yet unlocked (BFU state) is the highest-protection posture
- Do not consent to device searches; request an attorney
- Assume any device returned after seizure is compromised — factory reset before re-use
- Contact EFF (eff.org/privacy) or ACLU Digital Rights Project for legal support

---

## Confidence Assessment and Gaps

**High confidence** (primary sources available):
- Apple law enforcement disclosure framework (Apple's own legal guidelines, published October 2025)
- GrapheneOS security features and Cellebrite resistance (leaked Cellebrite support matrix, GrapheneOS documentation)
- BFU/AFU forensic extraction model (academic forensics research, Cellebrite's own documentation)
- F-Droid security issues (privsec.dev primary analysis)
- SIM swap regulatory changes (FCC confirmed mid-2024 requirements)

**Medium confidence** (well-supported but evolving):
- Cellebrite's current capabilities against specific iOS versions — the forensics arms race moves faster than public documentation. Assume capabilities are more advanced than leaked documents suggest.
- Find My BFU Bluetooth behavior — documented by security researchers and confirmed by Apple Community reports, but Apple has not published precise technical specifications for this behavior.

**Known gaps**:
- GrapheneOS on Motorola hardware (partnership announced March 2026 but not yet shipping)
- GrapheneOS's specific resistance to Graykey (Cellebrite competitor) — limited public data
- Whether California DROP platform enforcement will be effective against data brokers with operations outside California

---

## Sources

- [Apple Law Enforcement Guidelines (October 2025)](https://www.apple.com/legal/privacy/law-enforcement-guidelines-us.pdf)
- [iCloud Advanced Data Protection: A challenge for law enforcement](https://warrantbuilder.com/advanced-data-protection/)
- [GrapheneOS Features Overview](https://grapheneos.org/features)
- [Practical GrapheneOS for the Paranoid — Ventral Digital](https://ventral.digital/posts/2024/12/9/practical-grapheneos-for-the-paranoid/)
- [Cellebrite Pixel Forensics Leak: BFU AFU Limits and GrapheneOS Impact](https://windowsforum.com/threads/cellebrite-pixel-forensics-leak-bfu-afu-limits-and-grapheneos-impact.387314/)
- [GrapheneOS Discussion: Cellebrite defenses](https://discuss.grapheneos.org/d/1183-cellebrite-defenses)
- [A deep dive into Cellebrite: Android support as of February 2025 — Osservatorio Nessuno](https://osservatorionessuno.org/blog/2025/03/a-deep-dive-into-cellebrite-android-support-as-of-february-2025/)
- [EFF: How to Enable Lockdown Mode on iPhone — Surveillance Self-Defense](https://ssd.eff.org/module/how-to-enable-lockdown-mode-on-iphone)
- [EFF: Journalist Security Checklist — Preparing Devices for Travel Through a US Border (June 2025)](https://www.eff.org/deeplinks/2025/06/journalist-security-checklist-preparing-devices-travel-through-us-border)
- [EFF: How to Get to Know iPhone Privacy and Security Settings](https://ssd.eff.org/module/how-to-get-to-know-iphone-privacy-and-security-settings)
- [F-Droid Security Issues — privsec.dev](https://privsec.dev/posts/android/f-droid-security-issues/)
- [GrapheneOS vs. CalyxOS: The Best Pick for 2025 — Cape](https://www.cape.co/blog/grapheneos-vs-calyxos)
- [Activists' Guide to Securing Your Smartphone — Privacy Guides (January 2025)](https://www.privacyguides.org/articles/2025/01/23/activists-guide-securing-your-smartphone/)
- [SIM Swap Fraud 2025: Stats, Legal Risks and 360 Defenses — Keepnet](https://keepnetlabs.com/blog/what-is-sim-swap-fraud)
- [How Port-Out Locks Protect You From SIM Swap Attacks — Efani](https://www.efani.com/blog/port-out-locks-protect-sim-swap-attacks)
- [California DELETE Request and Opt-Out Platform (DROP)](https://privacy.ca.gov/drop/)
- [Big-Ass Data Broker Opt-Out List — Yael Grauer, GitHub](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List)
- [BFU and AFU Lock States — DigForCE Lab, Dakota State University](https://blogs.dsu.edu/digforce/2023/08/23/bfu-and-afu-lock-states/)
- [Google adds Android auto-reboot to block forensic data extractions — BleepingComputer](https://www.bleepingcomputer.com/news/security/google-adds-android-auto-reboot-to-block-forensic-data-extractions/)
- [iPhone Findable After Power Off — Apple Community](https://discussions.apple.com/thread/254909274)
- [Committee to Protect Journalists: When Spyware Turns Phones Into Weapons](https://cpj.org/reports/2022/10/when-spyware-turns-phones-into-weapons/)
- [Surveillance Self-Defense — EFF](https://ssd.eff.org/)
