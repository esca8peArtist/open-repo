---
title: "Journalist Implementation Guide: Source Protection and Device Security"
project: cybersecurity-hardening
created: 2026-04-28
status: complete
audience: journalists, investigative reporters, photojournalists, freelancers
tier: 1–3 (escalates by activity)
depends_on: device-hardening-guide.md, opsec-playbook.md, palantir-threat-model.md
---

# Journalist Implementation Guide: Source Protection and Device Security

## Your Threat Model

Your primary obligation is protecting your sources. Palantir's IRS LCA platform maps "social networks among investigation targets" using phone call metadata, text records, and financial transactions — a subpoena to your carrier, not to you, can expose who called you and when. A search warrant to Apple for your iCloud backup can reveal conversations years old. Palantir ICM stores phone records, family relationships, and employment history on individuals ICE tracks.

The second threat is border seizure. EFF documented in June 2025 that CBP conducts device searches without a warrant at ports of entry. A phone unlocked within the last 72 hours is substantially more vulnerable to Cellebrite extraction than one powered off (the BFU/AFU difference; see `device-hardening-guide.md` Section 2.3).

---

## Week 1: Essential Baseline

**1. Enable Advanced Data Protection on iPhone**
Settings → [your name] → iCloud → Advanced Data Protection → Turn On. This end-to-end encrypts iCloud backups, documents, and photos — Apple cannot hand over this data under a warrant. Write your recovery key on paper and store it physically secure (not in email or cloud notes).

**2. Set an alphanumeric passcode**
Settings → Face ID & Passcode → Change Passcode → Passcode Options → Alphanumeric. Use 4+ random words. The Fifth Amendment protects memorized passphrases more robustly than numeric PINs, and alphanumeric passcodes resist forensic brute-forcing. Disable Face ID for iPhone Unlock; memorize the SOS shortcut (side + volume down) to disable Face ID quickly.

**3. Configure Signal for source communications**
Install Signal ([signal.org](https://signal.org)). Configure: Settings → Privacy → Disappearing Messages → Default Timer → 1 Week (set 24 hours for source conversations). Settings → Privacy → Screen Lock → enable. Settings → Profile → @ field → set a username. Settings → Privacy → Phone Number → "Who can find me by my number" → Nobody. Sources reach you by username only, without your carrier number exposed.

**4. Move sensitive email to ProtonMail**
Create a Proton account at [proton.me](https://proton.me) with a username not tied to your identity. Proton cannot hand over message content under legal process — it cannot decrypt it. Caveat: email metadata is not end-to-end encrypted. Subject lines are encrypted only Proton-to-Proton. For confidential source contact, Signal is still superior to email.

**5. Disable iCloud sync for sensitive apps**
Settings → [your name] → iCloud → Show All → audit app by app. Turn off sync for Messages, Health, notes apps, and any apps with source content. ADP protects backup content, but turning off sync means that data never leaves your device at all.

**6. Set carrier SIM protection**
AT&T: call customer service, enable "Extra Security." T-Mobile: app → account security → SIM Protection. Verizon: My Verizon app → Number Lock. This blocks SIM swapping — an attack where someone social-engineers your carrier into transferring your number, then intercepts your SMS 2FA codes to take over every account secured that way.

**7. Install a password manager**
Install KeePassXC ([keepassxc.org](https://keepassxc.org)). Generate a unique strong password for every service. Use a 6-word diceware passphrase to secure the database. Store the database file on your device only — not in cloud storage.

---

## Month 1: Intermediate Hardening

**1. Configure border-crossing protocol**
Before any border crossing: power off your device completely (not screen-lock or airplane mode). A powered-off device is in Before First Unlock (BFU) state — substantially more resistant to forensic extraction. Full protocol in `device-hardening-guide.md` Section 1.7. If ordered to unlock: you may decline; the device may be seized. Request Form 6051D. If returned after any forensic hold, factory-reset before using for source communications.

**2. Set up OnionShare for anonymous source document receipt**
Use OnionShare ([onionshare.org](https://onionshare.org)) to create a temporary .onion address a source can use to send files without email or cloud storage — no central server, nothing to subpoena. Longer term: advocate for SecureDrop at your publication ([securedrop.org](https://securedrop.org), supported by Freedom of the Press Foundation).

**3. Replace SMS two-factor authentication**
Audit every account's 2FA settings — migrate SMS 2FA to an authenticator app (Ente Auth or Raivo OTP; open-source, stored locally). For highest-value accounts (Proton, publication login), order two YubiKey hardware keys ([yubico.com](https://www.yubico.com)), register both, keep one as backup.

**4. Enable Mullvad VPN**
Sign up at [mullvad.net](https://mullvad.net) ($5/month, accepts cash by mail, no identifying information required). Enable before any sensitive research — ISP records of which sites you visit are accessible via NSL without a warrant. Mullvad has a court-verified no-log policy.

**5. Configure laptop full-disk encryption**
macOS: System Settings → Privacy & Security → FileVault → Turn On. When prompted, choose "Create a recovery key and do not use my iCloud account" — the iCloud option is accessible under legal process. Linux: Ubuntu and Fedora offer LUKS encryption at installation; if your current install is unencrypted, reinstalling with LUKS is the correct path.

**6. Use Tor Browser for sensitive research**
Download from [torproject.org](https://www.torproject.org). Use for any research you would not want linked to your IP — court records, FOIA databases, subject profiles. Do not install additional extensions (they weaken anonymity). Set security level to "Safest" via the shield icon in the toolbar.

**7. Audit your public social media footprint**
ImmigrationOS and Babel Street have confirmed contracts for real-time public social media monitoring — anything posted publicly is indexed. Remove historical location check-ins. Strip photo metadata before publishing: `exiftool -all= photo.jpg` (install via `brew install exiftool` on macOS). Review who can see your "following" list — sources visible in your social graph are sources exposed.

---

## Month 3: Advanced Mastery

**1. Enable Lockdown Mode for high-risk coverage**
Settings → Privacy & Security → Lockdown Mode → Turn On. Blocks most message attachment types, disables JIT JavaScript (dramatically reduces browser attack surface), blocks FaceTime from non-contacts, strips location metadata from shared photos. Enable during national security or law enforcement coverage. Some websites break — that is the correct trade-off. See `device-hardening-guide.md` Section 1.5 for full capability list.

**2. Establish a dedicated device for source communications**
Purchase a used iPhone with cash. Activate with a MySudo number ([getsudo.com](https://getsudo.com)) — not linked to your carrier or identity. Install only Signal. Never bring it to your home or office (both appear in carrier location history and would link it to you). Keep in a Faraday pouch (Mission Darkness or GoDark, ~$60) when not in use.

**3. Tails OS for document handling**
Tails ([tails.net](https://tails.net)) runs entirely in RAM from a USB drive and leaves no trace on the host computer. Use it for opening documents from untrusted sources (hostile PDFs, documents from investigation subjects) and for any task that must leave no forensic trace. A document opened in Tails cannot be recovered after shutdown.

**4. Verify Signal Safety Numbers with critical sources**
Open a Signal conversation → tap the contact name → Safety Number. Have them do the same. Read the numbers aloud in person or via a separate channel. This verifies no intermediary has been inserted. Mark as verified. Reverify if you receive a safety number change notification.

**5. Build an incident response plan**
Identify legal contacts before a crisis: EFF ([eff.org/press](https://www.eff.org/press)), Reporters Committee ([rcfp.org](https://www.rcfp.org)), CPJ ([cpj.org](https://cpj.org)). Protocol if device seized: do not voluntarily unlock, request Form 6051D, contact legal support immediately, treat returned device as compromised.

---

## Common Mistakes and How to Avoid Them

**Backing up Signal to iCloud.** Even with ADP, backing up creates a persistent copy of conversations your source assumed were ephemeral. Enable disappearing messages before starting sensitive conversations. Verify Signal is excluded from iCloud: Settings → [name] → iCloud → Signal → confirm it's off.

**Using your primary phone for source contact.** Your primary phone has a carrier account in your legal name, a location history, and an Apple/Google account with a payment card. A Signal conversation on that device links your source to all of that metadata. The dedicated device in Month 3 exists to prevent this chain.

**Publishing photos without stripping metadata.** Smartphone photos contain EXIF data: GPS coordinates, device model, timestamp, sometimes serial number. Strip it before publishing: `exiftool -all= photo.jpg` (macOS: `brew install exiftool`; Linux: `apt install exiftool`).

---

## Verification Checklist

- [ ] Advanced Data Protection: Settings → [name] → iCloud → verify it shows "Advanced Data Protection: On"
- [ ] Passcode type: Settings → Face ID & Passcode → verify the passcode option shows "Alphanumeric"
- [ ] Signal disappearing messages: open any conversation → tap the name at top → Disappearing Messages → confirm timer is set
- [ ] Signal username: Settings → Profile → confirm @ field shows a username, not a phone number
- [ ] SIM protection: call your carrier or check app to confirm port-out protection is active
- [ ] FileVault / LUKS: on macOS, `fdesetup status` in terminal should return "FileVault is On"
- [ ] 2FA audit: log into your three most sensitive accounts and verify 2FA uses an authenticator app or hardware key, not SMS
- [ ] Tor Browser works: open torproject.org → go to [check.torproject.org](https://check.torproject.org) → confirm "Congratulations. This browser is configured to use Tor."

---

## References

This guide distills from the following documents in this repository:
- `device-hardening-guide.md` — complete iOS/Android hardening with technical detail
- `opsec-playbook.md` — full countermeasure mapping by tier
- `implementation-guide.md` — step-by-step setup instructions with verification checkpoints
- `palantir-threat-model.md` — confirmed government surveillance capabilities and data sources

For legal support: [EFF](https://eff.org), [Reporters Committee for Freedom of the Press](https://www.rcfp.org), [Committee to Protect Journalists](https://cpj.org), [Freedom of the Press Foundation](https://freedom.press)
