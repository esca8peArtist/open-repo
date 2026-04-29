---
title: "TIER 3 Implementation Guide: Countermeasures for Sophisticated Adversaries"
project: cybersecurity-hardening
created: 2026-04-29
status: complete
confidence: high — grounded in confirmed tool documentation, legal precedent, and operational security research
depends_on: tier-3-threat-model.md, threat-model.md, opsec-playbook.md, implementation-guide.md
---

# TIER 3 Implementation Guide: Countermeasures for Sophisticated Adversaries

**Purpose**: This guide translates the TIER 3 threat model into executable countermeasures. Where the existing `implementation-guide.md` covers TIER 1-2 threats (data brokers, Palantir, IMSI catchers, basic device hardening), this guide covers the expanded attack surface of state-level adversaries: backbone surveillance, forensic toolkits, hardware implants, border interception, and legal compulsion.

**Prerequisites**: Read `tier-3-threat-model.md` before implementing these measures. Understanding *why* each countermeasure exists is essential for applying it correctly in novel situations. Countermeasures implemented without understanding the threat model frequently introduce gaps worse than the original configuration.

**Who should implement this**: TIER 3 is for people who have reason to believe they are the direct subject of a federal investigation, are receiving classified or highly sensitive materials, or whose communications are of active interest to a state-level intelligence service. Implementing TIER 3 measures without that profile is not harmful but introduces significant operational friction.

> **Tier 1-2 Foundation**: Every measure in the existing `implementation-guide.md` remains relevant and should be implemented first. TIER 3 adds layers on top — it does not replace TIER 1-2 practices. Data broker opt-outs, Signal configuration, and device hardening are prerequisites, not alternatives.

---

## Part 1: Compartmentalization Architecture

### 1.1 The Core Principle: Network and Identity Separation by Threat Tier

The foundational TIER 3 architecture is **compartmentalization**: no single device, network, or identity should span across different threat levels or purposes. A compromise of one compartment must not expose others.

**Practical three-tier architecture**:

**Tier A — Public Identity (lowest sensitivity)**
- Your daily-use phone and computer, registered in your name, connected to your home network
- Used for: non-sensitive communications, public-facing work, anything that can appear in discovery
- Assumption: this device may be seized and forensically examined. Nothing sensitive touches it.
- TIER 1-2 hardening applies here

**Tier B — Sensitive Work (intermediate sensitivity)**
- A dedicated device, separate from Tier A, running a privacy-hardened OS (GrapheneOS on Pixel or iOS 18.1+ with full Lockdown Mode)
- Registered to a non-attributable identity (VoIP number, pseudonymous email)
- Connected to a dedicated network path (VPN over home network, or separate carrier connection not tied to your identity)
- Used for: encrypted communications with sensitive contacts, document handling, research on sensitive topics
- Never carries personal identity data. Never connects to accounts tied to your legal name.

**Tier C — Air-Gapped System (highest sensitivity)**
- A computer that has **never connected to any network** and will never connect
- Purchased in person with cash at a physical retail location, not delivered to your address
- Used for: drafting the most sensitive documents, storing the most sensitive received files, encryption key management
- Data transfer occurs only via encrypted, verified physical media (USB drive that itself is dedicated to this purpose)
- See §1.2 for setup and maintenance

**Key operational rule**: Information flows **down** (from Tier A to Tier C) through deliberate, verified steps only. It does not flow up. Sensitive material processed on the air-gapped system is never moved to a networked device in unencrypted form.

---

### 1.2 Air-Gapped System Setup

**Hardware selection**:
- Purchase a used or refurbished laptop with cash at a physical store. Do not order online to your address — shipping records and delivery metadata link hardware to your identity and provide a window for supply chain interdiction.
- Prefer a Thinkpad (business-class, good Linux support, replaceable components) or a device whose firmware can be verified. Avoid devices from manufacturers with documented backdoor relationships with intelligence agencies.
- Immediately after purchase: remove the WiFi/Bluetooth card if the device has one and you don't need it, or use BIOS/UEFI settings to disable all wireless interfaces. Physically tape over USB ports not in use as a reminder to audit what's connected.

**Operating system**:

- **Tails OS** is the recommended choice for most TIER 3 use cases. It is amnesic by default (leaves no trace on the host machine), routes all traffic through Tor when network is used, and has a well-reviewed security model. For an air-gapped system, the Tor routing is irrelevant, but the amnesia and the clean-room environment for each session remain valuable. ([Tails project](https://tails.boum.org/))
- **Qubes OS** is appropriate if the system needs persistent state and you need strong application-level isolation (different VMs for different tasks). Qubes requires more capable hardware and has a steeper learning curve, but provides compartmentalization within a single machine. ([Qubes OS](https://www.qubes-os.org/))
- **Whonix** is designed for Tor-routed usage and is most useful on networked machines, not air-gapped ones.

**Boot verification**: Enable UEFI Secure Boot if the OS supports verified boot (Qubes does; Tails currently does not without modification). At minimum, verify the cryptographic signature of the OS image before installation using PGP. Instructions are provided by both projects. This addresses the supply chain threat at the software level.

**Storage**: Full-disk encryption with a strong passphrase (minimum 7 random words, diceware method). The passphrase is the last line of defense if the device is seized. Do not store the passphrase anywhere on the device or in the cloud.

**Verification step**: After setup, confirm that all network interfaces show as disabled or absent. On Linux: `ip link show` should list no wireless interfaces in UP state. `rfkill list` should show all wireless blocked.

---

### 1.3 Physical Isolation Protocols

Air-gapped security fails if physical access is compromised. Physical workspace security is a prerequisite.

**Workspace considerations**:
- Conduct sensitive work in a location that is not your home address if your home address is associated with surveillance interest. IMSI catchers, vehicle surveillance, and physical observation of who enters and exits are real TIER 3 tools.
- If working at home: be aware that network traffic patterns from your home IP address (even if content is encrypted) can reveal when you are active and can be correlated with other events.
- Use a **screened room** (Faraday cage) for the most sensitive work if electromagnetic interception is a concern. In practice, this is TIER 4+ territory — most TIER 3 actors do not deploy RF collection against individual homes. But awareness that unshielded electronics emit RF that can be recovered at short range (van Eck phreaking) is appropriate.

**Port tamper evidence**: Apply tamper-evident seals (commercial or nail polish with photograph documentation) over unused USB ports, the case seam, and the storage device access point of the air-gapped machine. Inspect before each use. This provides a low-cost indication of physical access.

**Device provenance for peripherals**: Every cable, mouse, and keyboard connected to a sensitive machine is a potential implant vector (see tier-3-threat-model.md §II.B). Purchase peripherals separately from devices, at a different time, from a different location. Do not accept peripherals from anyone whose provenance you cannot verify. Inspect cables for weight, length, and end-connector irregularities that might indicate an inline implant.

---

## Part 2: Device Configuration for Networked Tier B Systems

### 2.1 iOS Configuration (iPhone)

**Critical settings for forensic resistance**:

1. **Update immediately**: iOS 18.1+ defeats GrayKey extraction in confirmed testing. Never delay iOS updates — the forensic gap exists specifically on unpatched devices. Enable automatic updates.

2. **Use a strong numeric PIN, not biometrics**: Biometric authentication (Face ID, Touch ID) is legally compellable in most U.S. jurisdictions — courts have ordered defendants to unlock phones with fingerprints or faces. A PIN may be protected by the Fifth Amendment (privilege against self-incrimination) — the circuit courts are split but this protection exists in some jurisdictions. Use a 6-digit or longer numeric PIN. Do not use biometrics on the Tier B device.

3. **Enable Lockdown Mode**: Settings > Privacy & Security > Lockdown Mode. This disables iMessage link previews, complex web technologies, FaceTime from unknown callers, wired data connections to computers when locked, and configuration profile installation. It substantially reduces zero-click attack surface at the cost of some functionality. For a Tier B device used only for sensitive work, these tradeoffs are acceptable. ([Apple Lockdown Mode documentation](https://support.apple.com/en-us/HT212650))

4. **Automatic reboot after inactivity**: iOS 18 introduced automatic device reboot after 72 hours without unlock. This returns the device to Before First Unlock (BFU) state, which defeats tools that require an AFU state to extract data. Ensure this setting is not disabled.

5. **Disable iCloud backup**: Settings > [Name] > iCloud > iCloud Backup. If iCloud backup is enabled, a law enforcement request to Apple produces unencrypted backups of your device content. Apple has no ability to resist a valid legal order for iCloud data. Disable entirely. Do not use iCloud for any data that should not be producible to law enforcement.

6. **Signal configuration**: Use a VoIP number not linked to your identity. Enable disappearing messages (1 day or less for sensitive conversations). Verify safety numbers with all sensitive contacts in person. Check Settings > Linked Devices regularly — any device listed that you did not authorize should trigger immediate account migration.

---

### 2.2 Android Configuration (GrapheneOS on Google Pixel)

GrapheneOS provides stronger hardening than stock Android or iOS in several respects: the exploit mitigations are more aggressive, the Titan M2 integration is tighter, and the ability to use network permission controls (allowing apps to have no network access) reduces the attack surface for data exfiltration.

**Why Pixel and not Samsung**: The Titan M2 secure element in Pixel devices provides hardware-backed key storage and PIN attempt rate-limiting that other Android OEMs do not replicate to the same standard. Samsung Knox provides some security features but Cellebrite has demonstrated more complete extraction capability against Samsung devices than against Pixel/GrapheneOS. ([Google Mobile Device Security Scorecard 2024](https://services.google.com/fh/files/misc/mobile_device_security_scorecard_2024_v2.pdf))

**Critical configuration steps**:

1. **Install GrapheneOS only from official source**: [grapheneos.org](https://grapheneos.org/install). Verify the installer's PGP signature before use. Install via the web installer on a trusted machine.

2. **Enable duress PIN**: GrapheneOS supports a secondary PIN that, when entered, triggers a factory reset. Configure this for high-risk scenarios (border crossing, anticipated arrest). This is configured during setup.

3. **Storage scopes**: GrapheneOS provides per-app storage permissions more granular than stock Android. Configure apps to access only the files they need.

4. **Network permissions**: GrapheneOS allows completely blocking network access per app. Any app that does not require network access for its core function should be denied network permission, reducing exfiltration surface.

5. **Auto-reboot**: Settings > Security > Auto Reboot. Set to 8 hours or less. This returns the device to BFU state, defeating AFU-dependent forensics tools.

6. **Disable USB data**: Settings > Security > USB. Set to "Charging only" when locked. This prevents data transfer via USB when the device is locked, defeating forensic tools that require a USB data connection.

---

### 2.3 Carrier and Phone Number Management

**The SS7 threat requires carrier-level countermeasures**:

1. **Do not use your legal-name SIM for sensitive communications**: Purchase a prepaid SIM with cash, from a physical store, without creating an account tied to your identity. Activate it using a public Wi-Fi connection, not from your home IP. This SIM is for Tier B use only. ([SS7 threat — tier-3-threat-model.md §II.A])

2. **Use Signal over the internet, not SMS**: Signal's encrypted messages transit the internet, not the SS7 SMS network. SS7 attacks against SMS content are defeated by not using SMS. However: your carrier can see that data is being sent to Signal's servers (metadata), and SS7 location tracking is not defeated by Signal — it is a carrier-level attack against your SIM's registration, independent of what app you're using.

3. **SIM swapping protection**: Contact your carrier and add a PIN or passcode to your account that is required before any account changes (including SIM swaps). This does not defeat SS7 attacks by a sophisticated adversary but raises the bar against criminal SIM swapping.

4. **Consider Wi-Fi-only Tier B device**: A phone running GrapheneOS or iOS with a purchased VoIP number (JMP.chat, MySudo) and no physical SIM has no SS7-trackable IMSI. It communicates only over Wi-Fi. This eliminates the SS7 attack surface entirely — you are not registered with any carrier and cannot be located via ProvideSubscriberInfo. The tradeoff is that you are dependent on Wi-Fi network availability.

---

## Part 3: Operational Security for Groups

### 3.1 Compartmentalization Within Organizations

The weakest point in a group's security is usually not technical — it is organizational. Information shared with the full group expands the exposure surface to every member's device security, legal vulnerability, and potential for human intelligence infiltration.

**Need-to-know discipline**: Define in advance what each role within an organization needs to know. Planning details that only operational leadership needs should not be shared in a 50-person Signal group. Use separate, smaller groups by function (legal support, action planning, communications, finance) with overlap only at the leadership layer.

**Cell structure for highest-risk activities**: For activities where arrest is a realistic outcome and where knowledge of other participants would create legal exposure for them, consider a cell structure where participants know only the people in their immediate cell (3–5 people) and one liaison to the next level. This is a Cold War intelligence tradecraft adapted to activist organizing and is appropriate only when the threat model genuinely warrants it — overuse of cell structure fragments organizations in ways that damage effectiveness.

**Separate channels by sensitivity level**:
- **Public channel** (social media, group email): No operational details. For announcements and public outreach only.
- **General internal channel** (Signal group): logistics and coordination. Assume this may be compromised.
- **Operational channel** (smaller Signal group, short disappearing messages): Actual planning. Access strictly limited. Disappearing messages enabled (1 hour or less).
- **Legal defense channel**: Protected by attorney-client privilege if an attorney is a participant and the communication is for legal advice. Keep legal strategy discussion strictly within this channel with your attorney. Do not discuss legal strategy in non-privileged channels.

### 3.2 Dead Drops and Minimal Digital Contact

For the transfer of physical documents, information, or materials where even encrypted digital communication creates metadata exposure:

**Physical dead drop**:
- A pre-agreed location where one party leaves material and another party retrieves it, without both parties being present simultaneously
- Advantages: No digital metadata, no electronic devices required
- Procedure: Agree on location, timing signal, and authentication method (how the retrieving party knows the drop is legitimate and has not been compromised) in advance, via an encrypted channel, before any operational use
- The location should not be associated with either party. Public places with natural foot traffic (parks, library book returns, locker systems) that neither party frequents in their normal patterns are appropriate.

**Encrypted physical media**:
- For transferring large files without network exposure, use a USB drive encrypted with VeraCrypt ([veracrypt.fr](https://veracrypt.fr)) with a strong passphrase. Share the passphrase via a separate channel than the physical media.
- The drive itself, if seized, reveals only ciphertext. The passphrase is not on the drive.
- After transfer, securely wipe the drive: `shred -vzu -n 3 /dev/sdX` on Linux, or use VeraCrypt's wipe function.

**Minimal contact protocol**: For the most sensitive communications, reduce the frequency and volume of all contact. Each communication event creates metadata. Batch communications, use prearranged times rather than real-time back-and-forth, and let disappearing messages remove the content record. The social graph — who talks to whom — is itself the information that network analysis extracts. Reducing contact frequency reduces the richness of the graph.

---

## Part 4: Border Crossing Protocols

### 4.1 Legal Framework Review

CBP has authority to search devices without a warrant at border crossings and their "functional equivalent" (airports for international arrivals, within 100 miles of the border). Advanced forensic searches (connecting to Cellebrite, GrayKey) require "reasonable suspicion" as an **internal policy matter** — this is not a constitutional requirement enforceable by the traveler in real time.

You have the right to:
- Decline to provide the password to a device (you may face detention and device confiscation as a consequence)
- Ask whether you are free to leave
- Request to speak with an attorney (this will typically be denied during the encounter itself)
- Document the encounter (badge numbers, names if available)

You do not have the right to:
- Prevent the physical inspection of the device
- Prevent the device from being confiscated (CBP may confiscate for further examination, with or without your cooperation)
- Immediate access to an attorney during the border encounter

([CBP legal authority — DHS Directive, November 2024](https://www.dhs.gov/sites/default/files/2025-02/2024_1126_cbp_border_searches_of_electronic_devices_at_ports_of_entry.pdf), [Yale Law Journal — constitutional limits on electronic border searches](https://yalelawjournal.org/forum/customs-immigration-and-rights))

### 4.2 Device Preparation Before Border Crossing

**Option A — Minimal device crossing**: Travel with a device that contains no sensitive data. This is a burner or a device that has been reset to factory state before crossing. Accounts are logged out. After crossing, log back in and re-sync needed data from a trusted server. What cannot be found cannot be extracted.

**Option B — Remote wipe standby**: If you must travel with your regular device, ensure remote wipe capability is configured and that you have a trusted person who can initiate a remote wipe if you are detained. Coordinate this before travel. Remote wipe is only effective if: (1) the device still has a network connection when the wipe command is sent, and (2) the wipe is initiated before Faraday-shielding by CBP prevents network access. This is not a reliable countermeasure against a prepared adversary.

**Option C — Encryption with PIN refusal**: Travel with a fully encrypted device and refuse to provide the PIN. Accept that the device will likely be confiscated. This tests the legal question in your specific situation and may result in the device being returned without forensic access (if the encryption holds and the law does not compel production in your circuit). Document everything.

**Practical recommendation**: Option A is the most reliable. The friction cost of traveling with a clean device and re-establishing access on the far side is real but manageable. A forensically clean device eliminates the entire border search threat.

**Cloud data warning**: Even if your device is clean, CBP can request (or subpoena) cloud provider records for accounts associated with you. If sensitive data exists in iCloud, Google Drive, Dropbox, or any cloud service accessible from your accounts, a clean device does not protect that data at the border.

---

## Part 5: International Jurisdiction and Communication Routing

### 5.1 Where Communications Are Not Subject to U.S. Surveillance Law

U.S. law governs what U.S. government agencies can compel from U.S. providers and what they can collect from U.S. infrastructure. It does not govern what foreign providers are required to produce to the U.S. government — though mutual legal assistance treaties (MLATs) create compulsion mechanisms with allied countries.

**Relevant distinctions**:

- **Five Eyes partners (UK, Canada, Australia, New Zealand)**: Intelligence-sharing arrangements mean that communications collected by GCHQ (UK), CSIS (Canada), ASD (Australia), or GCSB (New Zealand) can be shared with the NSA outside the domestic collection restrictions that apply to the NSA itself. The "Five Eyes" framework was documented in the Snowden disclosures. Routing communications through servers in Five Eyes countries provides **no additional protection** from U.S. intelligence collection.

- **EU-jurisdiction providers**: EU providers are subject to GDPR and cannot transfer data to the U.S. without meeting adequacy requirements. The EU-U.S. Data Privacy Framework (successor to Privacy Shield) provides a mechanism for transfers but has been legally contested. For adversarial intelligence collection, EU providers are somewhat harder to compel than U.S. providers — but an MLAT or a FISA order targeting a specific person can still reach non-U.S. providers in some circumstances. This is partial protection, not complete protection.

- **Providers in non-MLAT countries**: Providers in countries with no MLAT or diplomatic relationship with the U.S. cannot be directly compelled by U.S. law. However: (1) the content stored on those servers may still be intercepted in transit; (2) the U.S. can impose sanctions or other pressure; (3) those providers may have worse security practices or be subject to their own governments' demands.

**Practical guidance**: The jurisdiction of the server matters less than the **encryption architecture**. A U.S.-jurisdiction provider storing data in ciphertext that only the user can decrypt (true end-to-end encryption with no provider key escrow) provides stronger protection than a foreign-jurisdiction provider storing plaintext. Signal, ProtonMail, and Tutanota all provide E2E encryption by design. iCloud and standard Gmail do not.

### 5.2 VPN and Tor for Communication Routing

**VPN limitations**: A VPN shifts the observer from your ISP to the VPN provider. If the VPN provider is located in the U.S. or a Five Eyes country, they are subject to NSL-style legal demands. Many VPNs claim to retain no logs — but without independent audit, this is unverifiable. Mullvad VPN has been independently audited and has a confirmed no-log policy with no accounts required. ([Mullvad privacy policy](https://mullvad.net/en/help/no-logging-of-traffic-data/)). Use for: protecting content from local ISP observation, preventing your home IP from appearing in server logs.

**Tor for metadata protection**: Tor's three-hop routing prevents the exit node from knowing your IP and prevents your ISP from knowing what destination you're reaching. It is effective against local observers and service providers. Its limitation at TIER 3: a global passive adversary (NSA-scale) may be able to correlate entry and exit traffic patterns. For communications that are end-to-end encrypted (Signal, PGP email), Tor adds metadata protection — the recipient's server does not see your IP. Use Orbot on Android (in VPN mode, routing Signal traffic through Tor) for this purpose.

---

## Part 6: Legal Countermeasures

### 6.1 Warrant Challenges and Motion to Suppress

At TIER 3, legal process is likely — subpoenas, search warrants, or covert legal orders (NSLs, FISA). Defense counsel's ability to challenge these depends on knowing they exist, which classified collection may deliberately obscure.

**Suppression motions**: If evidence is used against you in a criminal prosecution, your attorney can file a motion to suppress that evidence if it was obtained illegally. In February 2025, a federal district court ruled that FBI queries of Section 702 data using U.S.-person identifiers require a warrant — and suppressed evidence obtained without one. This ruling creates a suppression argument for anyone whose prosecution relies on Section 702 evidence obtained via warrantless U.S.-person query. ([Court ruling reference — Brennan Center 2026](https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page))

**Parallel construction challenge**: When law enforcement uses classified surveillance to identify a suspect then develops evidence through parallel means, the original collection is concealed from the defense. Ask your attorney to specifically request disclosure of any "parallel construction" or "derived information" as part of discovery. NACDL has sample discovery motions addressing this issue. ([NACDL resources](https://www.nacdl.org/Document/Seymour-Reply-to-People-s-Response-to-Motion-to-Su))

**Geofence warrant challenge**: If location evidence derived from a geofence warrant is used against you, the constitutionality of geofence warrants is currently before the U.S. Supreme Court (2026 term). This is an active litigation front. ([Brookings — Supreme Court geofence warrant case](https://www.brookings.edu/articles/supreme-court-agrees-to-hear-a-fourth-amendment-case-regarding-geofence-warrants/))

**Border search challenge**: The circuit courts are split on whether a warrant is required for advanced border device searches. If a device search at the border produces evidence used against you, a suppression motion on Fourth Amendment grounds is viable in at least some circuits.

### 6.2 FOIA Requests for Surveillance Records

You have the right to request records about yourself from government agencies via FOIA. The practical value at TIER 3 is limited because: (1) intelligence collection is routinely exempted from FOIA under national security exemptions; (2) the existence of an NSL investigation may be classified and the gag order prevents agencies from confirming it; (3) response delays can run years.

**Where FOIA is useful**:
- Obtaining your FBI file (file requests to FBI directly: [fbi.gov/services/information-management/foipa](https://www.fbi.gov/services/information-management/foipa))
- Requesting DHS records on your travel history, border encounter records, and any DHS watch-listing
- Requesting CBP records of any device searches conducted against you
- Requesting records about government contracts with specific surveillance vendors (useful for confirming confirmed capabilities)

**Mandatory Declassification Review**: For classified records, an MDR request under Executive Order 13526 can run concurrently with a FOIA appeal. This requests a classification review rather than production of unclassified records and is appropriate when you believe classified records about you exist.

### 6.3 Constitutional Litigation

Several organizations litigate surveillance authority challenges:

- **ACLU National Security Project**: Challenges to FISA, NSL authority, and border search of devices. Active litigation on all three fronts. ([aclu.org/national-security](https://www.aclu.org/national-security))
- **Electronic Frontier Foundation**: First Amendment challenges to gag orders, Fourth Amendment challenges to digital surveillance. Has produced many of the leading cases on digital privacy. ([eff.org](https://www.eff.org))
- **Knight First Amendment Institute at Columbia**: Academic freedom and press freedom challenges. Particularly relevant for journalists. ([knightcolumbia.org](https://knightcolumbia.org))
- **Brennan Center for Justice**: Legislative advocacy and legal research on FISA reform, NSLs, and surveillance oversight. ([brennancenter.org](https://www.brennancenter.org))

**Legal retainer**: At TIER 3, you should have legal counsel identified **before** any investigation contact. When law enforcement contacts you, you have the right to say "I will not speak with you until I have spoken with my attorney" and then stop speaking. This is the single most important legal countermeasure — more important than any technical tool.

---

## Part 7: Infrastructure Resilience

### 7.1 Hardware Degradation Schedules

Hardware used for sensitive communications has a security lifecycle. Older devices accumulate more known vulnerabilities, and forensic tools update continuously to address newer models.

**Recommended replacement cycles**:

- **Primary Tier B mobile device**: Replace every 2 years or when the device's OS no longer receives security updates (whichever comes first). A device running an unsupported OS version is a forensic tool's friend — known vulnerabilities are not patched.
- **Air-gapped system**: No network exposure means less urgency for hardware replacement driven by network vulnerability. Replace when: the OS can no longer be supported in a verified-boot configuration, or physical inspection reveals tampering evidence that cannot be ruled out, or a new acquisition method is confirmed that affects the hardware in use.
- **SIM/phone number**: Rotate the non-attributable SIM used for Tier B communications every 6 months or after any contact with law enforcement that could have captured the IMSI. IMSI capture via IMSI catcher is a TIER 2 threat that creates a persistent identifier the adversary can track.

**Device retirement**: Wiping and discarding old devices creates exposure if the wipe is incomplete. For storage containing highly sensitive material, physical destruction of the storage medium (drilling through flash storage chips, degaussing, or commercial destruction services) is more reliable than software-only wiping. Do not donate, sell, or recycle retired Tier B or Tier C devices through standard consumer channels.

### 7.2 Backup Communication Channels

A primary communication channel disruption — device seized, account suspended, provider compromised — requires a pre-arranged backup channel. Without this, a single-point disruption severs all secure communication.

**Protocol for backup channels**:

1. Establish backup contact information for key contacts **in advance** via in-person exchange or via the secure primary channel. This includes: a backup Signal number (Tier B with different VoIP registration), a PGP key for encrypted email, and a physical address for emergency paper correspondence.

2. Establish a **check-in protocol**: If you have not been heard from via the primary channel by a specified time, the backup channel is attempted. If neither responds, a specific person (your attorney, a trusted colleague) is notified. This is not technically sophisticated — it is a human protocol, and human protocols are more reliable than technical ones for low-frequency emergency use.

3. **PGP email as a last-resort channel**: ProtonMail and Tutanota both provide E2E encrypted email that is harder to intercept than standard email. PGP email is slower and more friction-heavy than Signal, but it is decentralized — it does not require a specific service to remain operational. Exchange PGP public keys in advance. ([ProtonMail](https://proton.me/mail), [Tutanota](https://tutanota.com/))

4. **Paper, in extremis**: A physical letter sent to a PO box not associated with either party, containing information encrypted with a pre-shared key (a book cipher, or a printed PGP message), is essentially uninterceptable at the content level if the physical delivery is not observed. This is slow and cumbersome but is not dependent on any technical infrastructure.

---

## Summary: TIER 3 Implementation Checklist

**Compartmentalization**:
- [ ] Three-tier device architecture defined (Public / Sensitive / Air-gapped)
- [ ] Air-gapped machine purchased cash, in-person, configured with Tails or Qubes
- [ ] Tamper-evident seals applied to air-gapped machine ports
- [ ] Peripheral provenance verified for all hardware connected to Tier B/C machines

**Device configuration**:
- [ ] iOS: Updated to latest, Lockdown Mode enabled, biometrics disabled on Tier B device, iCloud backup disabled
- [ ] Android: GrapheneOS installed from official source, auto-reboot 8h, USB restricted, duress PIN configured
- [ ] Separate non-attributable SIM for Tier B device (or Wi-Fi-only with VoIP number)

**Border crossing**:
- [ ] Border crossing plan defined (clean device or factory reset protocol)
- [ ] Remote wipe contact identified if Option B used
- [ ] Know your rights documentation reviewed before travel

**Legal**:
- [ ] Legal counsel identified and retained (or at least a named attorney to call)
- [ ] FOIA requests filed for your own government records if relevant
- [ ] Key contacts aware of your right-to-silence protocol

**Organizational**:
- [ ] Need-to-know communication architecture defined for your group
- [ ] Dead drop protocol established with key contacts if warranted
- [ ] Backup communication channels exchanged in advance with critical contacts

**Infrastructure**:
- [ ] Device replacement schedule defined
- [ ] Retired device destruction protocol established

---

## Sources

- [Apple — Lockdown Mode documentation](https://support.apple.com/en-us/HT212650)
- [GrapheneOS — Installation](https://grapheneos.org/install)
- [Tails — Project home](https://tails.boum.org/)
- [Qubes OS — Project home](https://www.qubes-os.org/)
- [Whonix — Project home](https://www.whonix.org/)
- [Mullvad VPN — Privacy policy (no-log audit)](https://mullvad.net/en/help/no-logging-of-traffic-data/)
- [VeraCrypt — Project home](https://veracrypt.fr)
- [ProtonMail — Encrypted email](https://proton.me/mail)
- [Tutanota — Encrypted email](https://tutanota.com/)
- [DHS — CBP Border Search Directive, November 2024](https://www.dhs.gov/sites/default/files/2025-02/2024_1126_cbp_border_searches_of_electronic_devices_at_ports_of_entry.pdf)
- [CBP — Border Search official page](https://www.cbp.gov/travel/cbp-search-authority/border-search-electronic-devices)
- [Yale Law Journal — Constitutional limits on electronic border searches](https://yalelawjournal.org/forum/customs-immigration-and-rights)
- [Brennan Center — FISA 2026 Resource Page](https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page)
- [Brookings — Supreme Court geofence warrant case](https://www.brookings.edu/articles/supreme-court-agrees-to-hear-a-fourth-amendment-case-regarding-geofence-warrants/)
- [NACDL — Suppression resources](https://www.nacdl.org/Document/Seymour-Reply-to-People-s-Response-to-Motion-to-Su)
- [Google — Mobile Device Security Scorecard 2024](https://services.google.com/fh/files/misc/mobile_device_security_scorecard_2024_v2.pdf)
- [ACLU — National Security Project](https://www.aclu.org/national-security)
- [EFF — Digital rights](https://www.eff.org)
- [Brennan Center — Justice program](https://www.brennancenter.org)
- [Knight First Amendment Institute](https://knightcolumbia.org)
- [FOIA.gov — How to make a FOIA request](https://www.foia.gov/how-to.html)
- [NSA — FOIA request submission](https://www.nsa.gov/about/contact-us/Submit-a-FOIA-Request/)
- [DHS — FOIA request submission](https://www.dhs.gov/submit-freedom-information-act-foia-request)
