---
title: "April to May Tool Update Guidance: What Changed in Existing Templates"
project: cybersecurity-hardening
created: 2026-05-06
status: ready-for-use
audience: Template maintainers — anyone updating April 2026 cybersecurity templates for May 2026 distribution
purpose: >
  Documents exactly what to change in April 2026 device hardening, communication
  security, and opsec templates based on May 2026 threat developments. Each entry
  specifies: what the April template said, what changed, and the exact replacement
  or addition. No structural rewrites required — these are targeted inserts and
  corrections.
depends-on: device-hardening-guide.md, opsec-playbook.md, may-2026-advanced-threats.md, 2026-threat-updates.md
---

# April to May Tool Update Guidance

**Bottom line**: April 2026 templates remain substantially correct. Seven targeted additions and three recommendation upgrades are needed before May distribution. No full rewrites. All existing countermeasures for Signal, iCloud ADP, data broker opt-outs, and basic device hardening are current and correct.

---

## Change Log Summary

| Change | Template Section | Type | Priority |
|--------|----------------|------|----------|
| Add "voice and video no longer prove identity" section | Communication security | New section | **Immediate** |
| Add code word protocol | Social engineering / communication security | New countermeasure | **Immediate** |
| Add two-channel verification rule | Social engineering / financial security | New countermeasure | **Immediate** |
| Clarify Bitwarden installation path | Password management | Reinforce existing | **Immediate** |
| Upgrade FIDO2 hardware MFA from recommended to required | Authentication | Recommendation upgrade | This month |
| Add UEFI firmware update to device hardening | Device hardening | New action item | This month |
| Add supply chain caution for April 21–May 31 window | Software installation | Time-specific notice | **Immediate** |
| Add state-level election security contacts (Tier 2) | Election protection | New resource | This month |
| Add FISA June 12 advocacy action | Policy section | Time-sensitive addition | **Immediate** |
| Remove voice biometrics from reliable MFA list | Authentication | Removal | This month |

---

## Change 1: Add "Voice and Video No Longer Prove Identity" Section

**Why**: The ProKYC platform, confirmed commercially deployed in 2026 at $629/year, can clone any person's voice from three seconds of publicly available audio and inject real-time deepfake video into liveness verification checks. Human detection of high-quality deepfakes is below 30% accuracy. AI liveness checks are defeated by frame injection before the feed reaches the verification server.

**Where it goes**: Communication security section, social engineering defense section. All tiers.

**Exact text to add**:

---

**When Voice and Video No Longer Prove Identity**

AI voice cloning can replicate anyone's voice using three seconds of audio from any public source — a podcast, a social media video, a voicemail greeting. Deepfake video tools can produce a real-time video feed that defeats liveness detection checks. A caller or video conference participant who looks and sounds like your colleague, attorney, or source may not be that person.

**Two things that still work**:

**1. A code word** — a brief phrase known only to you and the person you need to verify. Establish a code word with your key contacts before a crisis. If an unexpected call from a "known" person requests urgent action and they cannot provide the code word, treat the contact as potentially synthetic and verify through a separate channel before acting.

**2. Signal safety number comparison** — verifies cryptographic key ownership, not biometric characteristics. This is the only remote verification mechanism that synthetic voice and deepfakes cannot defeat. Compare safety numbers with high-value contacts in person. Re-verify if any contact reports a new device.

**The two-channel verification rule**: Any unexpected request for money, sensitive documents, or high-stakes action that arrives through one channel (a call, a video meeting, an email) must be confirmed through a separately established channel before you act. Do not call back the same number that called you. Use a pre-established desk number or text through a Signal thread opened at a prior in-person meeting.

---

**Tier relevance**: All tiers. Tier 1 emphasis: family emergency calls requesting money. Tier 2 emphasis: organizational wire transfers, requests from apparent colleagues. Tier 3 emphasis: source contact verification, any unexpected contact requesting sensitive action.

---

## Change 2: Add Code Word Protocol

**Why**: Code words are the most accessible, zero-cost countermeasure against voice cloning. They require no technology and can be implemented in minutes. They are not in current April templates.

**Where it goes**: Immediate actions section (Week 1 / Day 1), social engineering defense section. All tiers.

**Exact text to add**:

---

**Establish a Code Word This Week**

A code word is a brief phrase — not a common expression, not something that could appear in normal conversation — known only to you and the people you need to verify. Examples of format (not the actual words): a two-word phrase involving a color and an animal, a line from an obscure shared experience, a made-up word.

**How to deploy it**: Contact your key colleagues, household members, and highest-risk sources. Tell them: "I'm setting up a code word for unexpected high-stakes calls. If I — or anyone claiming to be me — ever calls you with an urgent request involving money, location, or sensitive information, ask for the code word first. If they can't provide it, call me back on my known number before acting."

**Change code words**: After any suspected compromise, after any period where a code word was discussed in writing on a digital platform, or periodically as a standard security hygiene practice.

---

## Change 3: Add Two-Channel Verification Rule

**Why**: Voice cloning enables callbacks to the same compromised caller. Two-channel verification ensures the second confirmation uses an independently established channel that the attacker cannot spoof.

**Where it goes**: Financial security section, communication security section. Tiers 2 and 3. (Also relevant to Tier 1 for family emergency scenarios.)

**Exact text to add**:

---

**Two-Channel Verification Rule**

Any unexpected request for:
- Wire transfer or financial action
- Sensitive document delivery or information transfer  
- Urgent physical location change
- Account access or credential provision

...must be confirmed through a **second, pre-established channel** before you act.

The second channel cannot be:
- A callback to the same number that called you
- A reply to the same email that sent the request
- A response to the same Signal thread that sent the request

The second channel should be:
- A pre-established desk phone number called independently
- A Signal thread initiated from a prior in-person verified contact
- An in-person confirmation if time permits

Establish second-channel contacts with all key organizational relationships now, before a crisis. Keep the list current.

---

## Change 4: Reinforce Bitwarden Installation Path

**Why**: The Bitwarden CLI (`@bitwarden/cli`) was compromised via a hijacked GitHub Action on April 22, 2026, for 90 minutes. The desktop app and browser extension were not affected. The April 2026 template added this note; it needs to be elevated in prominence and expanded to cover all security-critical tools.

**Where it goes**: Password management section, software installation guidance. All tiers.

**Current April language** (if present): "Install Bitwarden via the official website or app store, not via npm."

**Replace with or add if not present**:

---

**Critical: Official Installers Only for Security-Critical Software**

The Bitwarden CLI password manager was compromised in a supply chain attack on April 22, 2026. The attack vector was a developer package manager (npm). The official desktop app and browser extension were not affected.

**This means**: Install all security-critical software — password managers, VPN clients, Signal, device management tools — **exclusively via**:
- Official website direct download (bitwarden.com, mullvad.net, signal.org)
- App Store (iOS App Store, Google Play Store)
- System package manager maintained by your OS vendor (Apple's built-in update, Windows Update)

**Never install or update security-critical software via**:
- npm (`npm install`)
- pip (`pip install`)
- Homebrew (`brew install`) for security tools specifically
- Any third-party package manager or developer tool registry

**If you installed or updated any security tool via a package manager between April 21 and late May 2026**: Rotate all credentials associated with that tool. Treat the installation as potentially compromised.

---

## Change 5: Upgrade FIDO2 Hardware MFA from Recommended to Required

**Why**: Voice biometrics used as a second factor are now defeated by voice cloning from publicly available audio. Time-based OTP (TOTP) apps are better than SMS but do not provide hardware assurance. FIDO2 hardware tokens (YubiKey, SoloKey) require physical possession and a PIN — they cannot be remotely extracted, cloned from audio, or bypassed by deepfake video.

**Where it goes**: Authentication section, device hardening section. Tiers 2 and 3. Tier 1 as "strongly recommended."

**Current April language**: FIDO2 hardware MFA recommended for high-value accounts.

**Update to**:

---

**Hardware FIDO2 MFA: Now Required for High-Risk Accounts**

Voice biometrics used as authentication factors are no longer reliable against current AI voice cloning attacks. TOTP (authenticator app) codes are better than SMS but do not provide hardware-level assurance.

**2026 MFA recommendation hierarchy**:

| Factor type | Reliability against current attacks | Recommendation |
|-------------|-------------------------------------|---------------|
| FIDO2 hardware token (YubiKey, SoloKey) | High — requires physical possession + PIN | **Required for**: email, cloud storage, password manager, VPN accounts. Order two (primary + backup). |
| TOTP authenticator app (Ente Auth, Raivo OTP) | Medium — can be phished but not remotely extracted | Minimum for all accounts not using hardware token |
| Voice biometric | **Failed** — defeated by 3-second audio sample | Remove from all account authentication |
| SMS-based 2FA | Low — defeated by SIM swap + carrier interception | Downgrade: better than nothing, not sufficient for sensitive accounts |
| No 2FA | None | Never for accounts holding sensitive communications or credentials |

**Implementation**: Order two YubiKeys (yubico.com). Register both on each critical account — one primary, one backup stored physically secure. Set a PIN on each key (this requires physical possession + PIN for use). Instructions: yubico.com/setup.

---

## Change 6: Add UEFI Firmware Update to Device Hardening

**Why**: The LogoFAIL vulnerability (in UEFI image-parsing code from the three major BIOS vendors, affecting ~95% of x86 devices) was exploited by BootKitty, a Linux UEFI bootkit, which injects rogue certificates into UEFI variables and disables kernel signature verification. This attack pre-dates OS load, Secure Boot enforcement, and every endpoint security product. A production-grade variant would survive OS reinstallation and disk re-encryption.

**Where it goes**: Device hardening section, quarterly maintenance section. Tiers 2 and 3. Tier 1 simplified note.

**Exact text to add**:

---

**UEFI Firmware: Required for Complete Device Hardening**

Most device hardening guidance focuses on the operating system layer. A class of firmware vulnerabilities (documented as LogoFAIL, affecting AMI, Insyde, and Phoenix BIOS implementations on ~95% of x86 devices) attacks below the operating system — before the OS loads, before Secure Boot enforces verification, before any security software is active.

A working exploit for Linux (BootKitty) was published in November 2024 and confirmed operational against specific Ubuntu kernel versions. Nation-state variants with broader targeting are not confirmed but represent the expected development trajectory given a 12–24 month research-to-deployment gap.

**Action required**:

1. Check your device manufacturer's support page for UEFI/BIOS security updates. Dell, Lenovo, HP, and major manufacturers publish UEFI updates through standard system update channels. Apply any available security updates.

2. Verify UEFI Secure Boot is enabled: on most devices, this is accessible via BIOS settings (press F2, F12, or Del at startup). Secure Boot should be in "Enabled" state with default keys unless you have a specific reason to modify it.

3. **Technical staff only**: Scan UEFI firmware images for LogoFAIL-vulnerable components using Binarly's free analysis tool at https://fwcheck.binarly.io. For organizational hardware fleets without active vendor UEFI update programs, this tool identifies whether the specific firmware version is affected.

4. **Hardware procurement going forward**: Add "vendor UEFI security update program" as a criterion. Vendors with documented UEFI security programs (recent ThinkPads, certain Dell models with BIOS update-as-a-service) are preferable to budget hardware with undocumented firmware support. Check the vendor's security advisory feed for UEFI-related CVEs before procurement.

---

## Change 7: Add Time-Specific Supply Chain Warning

**Why**: The April 21–May 31 window is a specific exposure period when Shai-Hulud Wave 3 and Mini Shai-Hulud compromises were actively deployed. Anyone who updated developer tools via package managers during this period should rotate affected credentials. This is time-bounded and should be noted as such.

**Where it goes**: Supply chain warning box, quick-action sidebar. Tiers 2 and 3.

**Exact text to add** (as a callout/warning box):

---

**TIME-SPECIFIC SUPPLY CHAIN NOTICE: April 21 – May 2026**

A sustained supply chain campaign (Shai-Hulud Wave 3 / Mini Shai-Hulud) compromised developer packages across npm, PyPI, and PHP ecosystems between April 21 and at least late May 2026. Affected packages include: Bitwarden CLI (April 22), PyTorch Lightning (April, Python), intercom-client (npm), SAP developer toolchain packages, and 1,800+ developer repositories.

**If you or your technical staff installed or updated any developer tool via a package manager during this window**:

- Treat all credentials accessible from that environment as potentially compromised
- Rotate: cloud service credentials (AWS, Azure, GCP keys), SSH keys, VPN credentials, GitHub personal access tokens, npm publish tokens, any service API keys
- Verify Bitwarden account breach status: Bitwarden has published guidance; check bitwarden.com/help for current recommendations
- Check your CI/CD pipeline environment for unexpected entries in log output from the April 21–May 31 period

The campaign remains the primary ongoing supply chain threat in Q2 2026. Going forward: SBOM generation at build time enables rapid identification of affected packages in future disclosures.

---

## Change 8: Add State-Level Election Security Contacts (Tier 2)

**Why**: EI-ISAC was defunded in February 2026. Organizations previously relying on EI-ISAC threat intelligence feeds for election infrastructure protection need to identify alternative contacts. The state-level election security office is now the primary channel.

**Where it goes**: Election protection section. Tier 2 only (organizations connected to election administration).

**Exact text to add**:

---

**State-Level Election Security Contacts: Now the Primary Channel**

CISA's EI-ISAC (which provided cyber threat intelligence and incident response support to local election offices) was defunded in February 2026. Organizations connected to election administration should now coordinate with state-level contacts:

- **Your state's Secretary of State office**: Maintains a cyber incident reporting channel. Identify the contact and add it to your emergency response documentation before Election Day, not during an incident.
- **National Association of Secretaries of State (NASS)**: https://www.nass.org — provides peer coordination across state election officials.
- **National Association of County & City Clerks (NACO)**: https://www.naco.org — election administration coordination at the county level.
- **Defending Digital Democracy (D3P, Harvard Kennedy School)**: https://d3p.hks.harvard.edu — provides election security guidance and resources independent of federal agencies.
- **Center for Democracy and Technology (CDT)**: https://cdt.org — publishes ongoing analysis of election security posture.

**Election Assistance Commission emergency contact**: The EAC maintains an emergency contact list for election office incidents: https://www.eac.gov. This is the remaining federal channel with any operational election security function.

---

## Change 9: Add FISA June 12 Advocacy Action

**Why**: The June 12 FISA 702 deadline is a time-bounded policy window. Organizations with policy advocacy capacity should be directing constituent engagement at uncommitted senators before June 5. This is the most relevant policy window in the current threat landscape.

**Where it goes**: Policy action section. All tiers. Time-sensitive.

**Exact text to add**:

---

**FISA Section 702 — June 12 Policy Window**

Congress must act on FISA Section 702 by June 12, 2026. The April 30 clean extension included no warrant protections.

The Government Surveillance Reform Act (S.4082, bipartisan: Wyden D, Lee R, Davidson R, Lofgren D) includes a provision to prohibit federal agencies — including DHS, FBI, ICE, IRS, and Secret Service — from purchasing cell phone location data, browsing history, and other commercial data broker records without a warrant. This is the specific mechanism by which ICE and DHS currently acquire location data for targeting without any court process.

**Constituent engagement window: now through June 5, 2026**

- Contact your senators. Identify whether your senators are co-sponsors of S.4082. If not, constituent contact before June 5 reaches them before procedural deadlines close.
- Priority: Republican senators from competitive states who are not yet co-sponsors. The data broker provision has bipartisan backing and is severable from the more contested warrant requirement for FBI backdoor searches.
- EFF action page: https://act.eff.org (updated for June 12 deadline)
- Brennan Center: https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page

---

## Change 10: Remove Voice Biometrics from Reliable MFA

**Why**: Voice biometric second factors are defeated by three seconds of publicly available audio through TD-VIM (Time-domain Voice Identity Morphing). Any template currently listing voice biometrics as a reliable second authentication factor needs this corrected.

**Where it goes**: Authentication section, 2FA guidance, any login security section. All tiers.

**What to remove or flag as deprecated**: Any statement recommending voice biometrics as a reliable 2FA method. Any guidance that treats a voice call from a known number as identity verification for sensitive accounts.

**What to add**: See Change 5 (FIDO2 MFA recommendation hierarchy) for the replacement guidance.

---

## Implementation Priority Summary

**This week (pre-distribution must-haves)**:
1. Add "voice and video no longer prove identity" section
2. Add code word protocol
3. Add two-channel verification rule
4. Reinforce Bitwarden installation path / official installer only
5. Add time-specific April 21–May 31 supply chain warning
6. Add FISA June 12 advocacy action (time-sensitive)

**This month**:
7. Upgrade FIDO2 MFA to required
8. Add UEFI firmware update to device hardening
9. Add state-level election security contacts (Tier 2 only)
10. Remove voice biometrics from reliable MFA list

**No change required**:
- Signal for sensitive communications: current and correct
- iCloud Advanced Data Protection: current and correct
- Data broker opt-out instructions: current and correct
- GrapheneOS recommendation: current and correct
- Tor/Mullvad VPN guidance: current and correct
- Border crossing protocol: current and correct
- SecureDrop / OnionShare for journalists: current and correct
- ProtonMail recommendation: current and correct

---

*Document version: May 2026. Update this document when new supply chain incidents, new tool compromises, or material threat model changes occur. Next scheduled review: August 2026 (ahead of November midterm cycle).*
