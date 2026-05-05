---
title: "Operational Security Workflows Guide"
project: cybersecurity-hardening
created: 2026-05-05
status: complete
depends_on: opsec-playbook.md, threat-model.md, encrypted-messaging-implementation-guide.md
confidence: high — sourced from EFF OPSEC training 2025 review, IVPN compartmentalization guide, State of Surveillance OPSEC basics, Freedom of the Press Foundation digital security resources
---

# Operational Security Workflows Guide

> **Danger**: OPSEC is context-dependent. The protocols in this guide are calibrated for high-risk environments. Applying maximum OPSEC to a low-risk situation wastes significant effort, creates friction that leads to abandonment, and can draw unnecessary attention. Assess your actual threat before choosing a tier.

> **Important**: OPSEC failures in 2025 have been behavioral, not cryptographic. The most significant U.S. government OPSEC failure of 2025 — the "Signalgate" incident — involved officials accidentally including a journalist in a sensitive Signal group discussing military operations. Encryption was not broken; judgment was. No tool compensates for poor operational habits.

---

## Threat Model

**Who this guide is for**: People operating in environments where their activities, associations, and identity are at genuine risk of exposure to adversaries with significant resources — law enforcement, government surveillance, organized retaliation.

**Who this guide is not for**: People primarily concerned about corporate data harvesting, account security, or general online privacy. For those cases, use the device-hardening and VPN guides with significantly lower operational friction.

**Assets at risk**:
- Your real identity (linked to activities that carry legal or physical risk)
- Your contact network (exposing who you work with)
- Your location patterns (enabling physical surveillance)
- Operational plans (enabling preemptive action by adversaries)
- Your communications content (evidence in prosecution, retaliation)

---

## Part 1: Identity Compartmentalization

### The Core Principle

Compartmentalization means that different spheres of your life operate with completely separate identities, devices, accounts, and information flows. If one compartment is compromised, the breach cannot spread to others.

**The failure mode**: Sharing a piece of information between compartments. This can happen via:
- Using the same device for sensitive and personal activity
- Logging into a sensitive account from a personal IP (or vice versa)
- Having your personal phone and sensitive phone in the same physical location simultaneously
- Reusing usernames, email addresses, or passwords across compartments
- Metadata leaking from documents (see Section 3.3)

### Compartment Design

**Define your compartments before you start**. Common models:

**Two-compartment model (minimum)**:
- Personal identity: your legal name, personal email, social accounts, shopping, banking.
- Work identity: a pseudonym, separate accounts, separate device, separate network connection.

**Three-compartment model**:
- Personal identity (as above)
- Work/organizing identity
- High-sensitivity operations identity (for activities where even your work identity should not be traceable)

**Rule**: Information flows in one direction only, and even then only by deliberate, secured means. Your personal identity never knows anything about your high-sensitivity operations identity. Even within an organization, apply need-to-know: only share information with the specific people who need it.

### Device Compartmentalization

Each significant compartment should have a dedicated device.

**Minimum viable device separation**:
- Personal laptop/phone for personal use.
- Dedicated laptop for sensitive work.
- (If needed) Dedicated phone for sensitive communications.

**Device isolation rules**:
- Never log into a personal account (Gmail, social media, Apple ID, Google account) on a sensitive device.
- Never use a sensitive device on a personal network (home Wi-Fi associated with your identity) unless routed through a VPN or Tor.
- Never carry a personal phone and a sensitive phone to the same sensitive location — they can be correlated by cell tower records.

**Budget option**: If a second physical device is not feasible, use virtual machines (VMs) for compartmentalization. VirtualBox (free, open-source) and VMware allow running a completely separate OS in an isolated environment. A sensitive VM cannot directly access the host's accounts or files. This is less secure than a physical device (the VM shares hardware and the hypervisor can in principle observe the VM) but substantially better than no compartmentalization.

---

## Part 2: Session Isolation with VMs and Containers

### When to Use a VM

Use a dedicated VM for:
- Accessing sensitive resources (organizing platforms, document repositories)
- Communicating with sources or contacts that require your pseudonymous identity
- Visiting websites that you do not want linked to your personal browsing history
- Any task that should be isolated from your daily workflow

### VirtualBox Setup (Free Option)

1. Download VirtualBox from [virtualbox.org](https://www.virtualbox.org) — verify the SHA256 hash on the download page.
2. Install on your host system.
3. Create a new VM: New → Name it (use a non-descriptive name like "VM1") → choose Linux (Ubuntu is recommended for a hardened guest).
4. Allocate RAM: 2–4 GB is sufficient for most tasks.
5. Create a virtual hard disk (dynamically allocated is fine for a VM).
6. Install your OS from a downloaded ISO.

**VM network isolation**:
- In VirtualBox settings for the VM → Network → Adapter 1:
  - "NAT" (default): VM shares your host IP and routes through your host. Websites see your host IP (or VPN IP if host is on VPN).
  - "Internal Network": VM can only communicate with other VMs on the same internal network — no internet access. Useful for air-gapped analysis.
  - "Host-only adapter": VM can reach the host but not the internet.

**For routing VM traffic through Tor**:
- Install Whonix instead of a standard Ubuntu VM. Whonix is a two-VM system: a "Gateway" VM that routes all traffic through Tor, and a "Workstation" VM that sends all traffic through the Gateway. Even if the Workstation is compromised, it cannot determine your real IP. Download from [whonix.org](https://www.whonix.org).

### VM Hygiene

- Take a "clean snapshot" of the VM after initial setup before use. You can revert to this clean state after each sensitive session.
- Do not accumulate data in the VM across sessions if your goal is isolation. Files created in the VM can contain metadata.
- If using the VM for document work, remember: the VM's system clock, language settings, and default fonts can appear in document metadata. Use LibreOffice and strip metadata before sharing (see Section 3.3).

---

## Part 3: Metadata Minimization

### 3.1 Document Metadata

Documents (Word, PDF, LibreOffice) store metadata that includes: author name, organization, revision history, comments, and time of creation. This metadata can identify you even if the document's content is anonymous.

**Remove metadata from documents before sharing**:

LibreOffice (Linux/macOS/Windows):
1. File → Properties → General tab → remove fields.
2. File → Properties → Custom Properties → delete all entries.
3. Before export to PDF: File → Export as PDF → ensure "Export document metadata" is unchecked.

Microsoft Word:
1. File → Info → Inspect Document → Document Inspector → Inspect → Remove All for each category.

Command-line tool (Linux):
```bash
# Install mat2
sudo apt install mat2

# Strip metadata from a PDF
mat2 document.pdf

# Strip metadata from an image
mat2 photo.jpg

# Strip and output to a new file
mat2 --output clean.pdf original.pdf
```

### 3.2 Image Metadata (EXIF)

Photos taken with smartphones embed GPS coordinates, device model, date/time, and camera settings in EXIF metadata. Sharing a photo with GPS metadata embedded reveals your location.

**Strip EXIF before sharing images**:
```bash
# Install exiftool
sudo apt install exiftool  # Linux
brew install exiftool       # macOS

# Remove all metadata from an image
exiftool -all= photo.jpg

# Verify removal
exiftool photo.jpg  # Should show minimal or no metadata
```

Mobile apps for stripping EXIF:
- **Scrambled EXIF** (Android, F-Droid): shares images with metadata stripped
- **Metapho** (iOS): view and remove EXIF data before sharing

### 3.3 Communication Metadata

Even with encrypted messaging, metadata (who you communicate with, when, how often, message length patterns) is often visible to providers or carriers.

**Minimize metadata exposure**:
- Use Signal usernames (not phone numbers) so contacts cannot tell who is behind the account
- Communicate during varied times (not always the same hour each day)
- Vary message length and frequency — uniform patterns are more fingerprintable than varied ones
- For highest-sensitivity communication, use Briar (which routes via Tor, hiding metadata from your carrier)

---

## Part 4: Communication Protocols

### 4.1 Establishing Contact Securely

Before sensitive communication begins, establish trust. The risk: being connected to an adversary or monitored contact from the start.

**Verification hierarchy**:
1. In-person contact exchange is most secure (no digital trace, voice and face verification)
2. Video call where you recognize the person
3. Voice call (recognizing voice)
4. Comparison of cryptographic fingerprints (Safety Numbers in Signal, key fingerprints in PGP)

Never rely solely on a message from an existing channel to introduce a new contact — a compromised device means an adversary can impersonate the existing contact.

### 4.2 Information Sharing Protocol

**Need-to-know**: Only share information with people who need it for their role. "I told everyone in the group" is an OPSEC failure waiting to happen.

**Timing decoupling**: Do not share a plan at the time of its execution. Discussion of a plan creates a record. Operational details shared in advance of an action create a trail. Where possible, communicate about completed actions rather than planned ones.

**Language hygiene**: In sensitive channels, use pre-agreed terminology for sensitive subjects rather than clear language. This is not security through obscurity — it is a metadata and context-stripping technique that limits the damage if a message is seen out of context.

### 4.3 Dead-Drop Techniques (Digital)

A digital dead drop is a way to exchange information without direct communication between parties.

**Shared document method** (simple):
1. Two parties create a shared encrypted document or note (e.g., in a ProtonDrive folder, or an encrypted cloud storage service).
2. Party A writes a message to the document and does not send a direct message.
3. Party B checks the document periodically.
4. Neither party sends a message to the other — the communication channel appears inactive.

**Limitation**: Both parties must have prior access to the shared storage. The storage provider can still see access times.

**Draft folder method** (classic but limited):
1. Two parties share credentials to a single email account.
2. Messages are written to "Drafts" and never sent.
3. The provider sees both parties accessing the same account, not a message exchange between two accounts.
4. This is a weak technique against providers with full access — Proton or Tutanota are preferable for this use case if the provider cooperation is a concern.

---

## Part 5: Scenario Workflows

### Scenario A: Journalist Covering a Protest

**Before the protest**:
- Leave your primary phone at home or turn it off before approaching the venue. Carry it only for emergencies unrelated to protest activity.
- Use a secondary device for communications during the event: prepaid with a non-identity SIM, registered to Signal with a VoIP number.
- Communicate with sources using Signal with disappearing messages set to 1 day.
- Clear your device of sensitive contacts before entering a location where seizure is possible.

**At the event**:
- Your secondary device's presence in the area is logged by cell towers. It cannot be avoided if the device is on.
- Do not connect to event Wi-Fi networks — they can be monitored.
- Use mobile data routed through a VPN.
- Take photos only with a camera that does not embed GPS (disable location in camera settings, or use a camera without a GPS chip). Strip EXIF before any sharing.

**After the event**:
- Move sensitive files off the device to an encrypted storage medium before crossing any checkpoint.
- Review what you communicated and with whom. If a contact's status is uncertain (arrested, device seized), treat your communications with them as potentially visible.

**Decision tree**:
```
Am I crossing a border or checkpoint?
  Yes → Encrypted device, minimal data, know your legal rights, consider "travel profile" device
  No → Normal operational posture

Am I attending a location associated with an investigation?
  Yes → Leave primary phone behind, use secondary device, route traffic through VPN
  No → VPN is sufficient

Is my source identity at risk?
  Yes → Signal with disappearing messages + verified safety numbers + source uses Briar or Signal with VoIP
  No → Signal without additional measures
```

### Scenario B: Activist in a Repressive Country

**Communications**:
- Register Signal with a VoIP number obtained via Tor (MySudo is US-based; for non-US users, research alternatives that do not require identity verification). Do not use your primary carrier number.
- Use Briar for your highest-sensitivity contacts — Tor routing means your carrier cannot see that you are using a messaging service.
- Access any organizing platforms via Tor Browser or over a VPN. Mullvad is recommended (see VPN guide).

**Protecting your network**:
- If you are arrested, adversaries will want your contact list. Use Signal's "PIN lock" to prevent immediate access. Enable Registration Lock to prevent account takeover.
- Periodically review your Signal contact list and remove contacts who no longer need access.
- Practice "contact hygiene": only have people's contacts under pseudonyms you both know. A contact list of real names is a list of associates to interrogate.

**Travel OPSEC**:
- Border crossings are legal but high-risk for device search. Research the specific laws of your country. In the U.S., border agents can search devices without a warrant. Abroad, laws vary.
- A "travel profile" approach: before any border crossing or potential detention, transfer sensitive data to encrypted offline storage and do a factory reset of your device. After crossing, restore from encrypted backup.
- Understand that a factory reset does not permanently delete data — sophisticated forensics tools can recover recently deleted files. For highest protection, use a device that has never had sensitive data and restore selectively after crossing.

**Decision tree**:
```
Am I planning an action that could trigger legal consequences?
  Yes → Only essential people know, information on need-to-know basis, Briar or Signal for comms
  No → Standard Signal with disappearing messages

Could I be detained in the next 24 hours?
  Yes → Reduce sensitive data on device, enable PIN lock everywhere, alert a trusted contact
  No → Normal posture

Has a network member been arrested?
  Yes → Assume their device is compromised. Review what they knew. Change contact methods.
  No → Monitor, maintain normal posture
```

---

## Part 6: OPSEC Intensity Levels

Use this framework to match your practices to your actual risk.

| Level | Trigger | Required Practices |
|---|---|---|
| **Baseline** | General privacy concerns, no specific threat | Signal with disappearing messages, VPN for browsing, strong passwords |
| **Elevated** | Potential for legal attention, known monitoring of your community | Signal username isolation, device separation, metadata stripping from documents, VPN with no-log provider |
| **High** | Direct threat signals (legal process, confirmed surveillance, arrest of associates) | Separate device per compartment, Briar for sensitive contacts, Tor for anonymous browsing, no personal accounts on sensitive devices |
| **Critical** | Imminent arrest risk, active investigation confirmed | Device wipe/restoration cycle at borders, air-gapped communication for most sensitive content, minimal digital footprint, Whonix for all sensitive computing |

**Important**: "Critical" level OPSEC is unsustainable as a daily practice. It is appropriate for specific high-risk periods. Transition down when the acute risk passes.

---

## Operational Security Checklist

### Identity Compartmentalization
- [ ] Compartments clearly defined with no information cross-over
- [ ] Separate device (or VM) for each significant compartment
- [ ] Personal accounts never accessed from sensitive device
- [ ] Sensitive device never used on network linked to real identity
- [ ] Personal phone and sensitive phone never co-located at sensitive venues

### Session Practices
- [ ] Metadata stripped from documents before sharing
- [ ] EXIF removed from photos before sharing
- [ ] VMs used for sensitive web access (or Tor Browser)
- [ ] VM snapshots reset to clean state after sensitive sessions

### Communication Protocol
- [ ] Need-to-know principle applied to information sharing
- [ ] New contacts verified through in-person or out-of-band means
- [ ] Signal Safety Numbers verified with sensitive contacts
- [ ] Disappearing messages enabled on all sensitive conversations

### Physical OPSEC
- [ ] Primary phone absent or off at sensitive locations
- [ ] Travel device strategy defined for border crossings
- [ ] Contact list maintained with pseudonyms, not real names
- [ ] Sensitive data moved off device before high-risk events

---

## Troubleshooting

**Problem**: Using two devices is impractical — I only have one phone.
**Solution**: Signal's username feature allows you to have a separate contact identity without a second device. For higher separation, a second SIM card with a separate carrier identity is possible on dual-SIM phones. For a second internet identity, a dedicated browser profile with separate cookies and history (or Firefox Multi-Account Containers extension) creates lightweight compartmentalization without a second device.

**Problem**: VM setup is too technically complex.
**Solution**: For basic web browsing isolation, a separate Firefox profile (Menu → Profile Manager) provides lightweight session isolation without full VM overhead. Not equivalent to a VM but better than a single profile.

**Problem**: My organization needs everyone to know the plan for coordination purposes.
**Solution**: Distinguish between "need to execute" and "need to know in advance." People can know their specific role and timing without knowing others' roles. Information that could compromise the whole operation if one person is detained should be compartmented to those whose decisions depend on it.

**Problem**: I don't know if I'm at high enough risk to justify this.
**Solution**: Threat model first (see `threat-model.md`). The baseline practices (Signal, VPN, device encryption) are low-friction and appropriate for everyone. Add higher-friction practices only when you have a specific, identifiable reason. Vague anxiety about surveillance does not justify critical OPSEC; credible specific threats do.

---

## Sources

- [EFF: OPSEC Trainings 2025 Review](https://www.eff.org/deeplinks/2025/12/operations-security-opsec-trainings-2025-review)
- [State of Surveillance: OPSEC Basics 2025](https://stateofsurveillance.org/guides/basic/opsec-basics/)
- [IVPN: Online Privacy Through OPSEC and Compartmentalization](https://www.ivpn.net/privacy-guides/online-privacy-through-opsec-and-compartmentalization-part-4/)
- [Mr. Alias: OPSEC Handbook 2025](https://mr-alias.com/articles/opsec-handbook.html)
- [Freedom of the Press Foundation: Digital Security for Journalists](https://freedom.press/digisec/)
- [LevelBlue: Managing Pseudonyms with Compartmentalization](https://cybersecurity.att.com/blogs/security-essentials/managing-pseudonyms-with-compartmentalization-identity-management-of-personas)
- [Whonix: Download and Documentation](https://www.whonix.org)
