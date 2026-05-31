---
title: "Phase 2 Threat Model & Scenario Playbooks"
project: cybersecurity-hardening
created: 2026-05-31
status: pre-staged — ready for Phase 2 activation
author: research-agent
depends-on:
  - PERSONAL_OPSEC_PLAN.md
  - threat-model.md
  - PHASE_2_IMPLEMENTATION_ROADMAP.md
  - SCENARIO_PLAYBOOK_INDEX.md
frameworks-referenced:
  - MITRE ATT&CK
  - NIST CSF 2.0
  - Microsoft STRIDE
  - GDPR Article 33 (72-hour breach notification)
  - Canada PIPEDA Sections 10.1-10.3
---

# Phase 2 Threat Model & Scenario Playbooks

**Purpose of this document**: Phase 1 built your personal security foundation — Signal, iPhone hardening, VeraCrypt, Ente Auth, Bitwarden, data broker opt-outs. This document pre-stages Phase 2 by expanding the threat model to organizational and family scope, introducing four new adversary classes, and providing six decision-actionable scenario playbooks. These playbooks are designed for real-time use under stress: each decision tree covers the 80% of real-world variants you are likely to encounter.

**How to use this document**: Read Part 1 and Part 2 once, during planning. Keep Part 3 bookmarked. In an incident, go directly to the relevant scenario playbook and follow the decision tree from the top.

---

## Part 1: Threat Model Evolution (Phase 1 to Phase 2)

### What Phase 1 Addressed

Phase 1 threat modeling assumed a personal adversary profile: an opportunistic cybercriminal scanning for weak passwords, a stalker using data brokers to find your address, or a script kiddie running credential stuffing tools against common accounts. The countermeasures matched that profile: strong unique passwords in Bitwarden, TOTP codes in Ente Auth, encrypted device storage via VeraCrypt, Signal for communications that cannot be subpoenaed, and data broker removal to collapse the public-facing profile that enables targeted harassment and doxxing.

These are still relevant in Phase 2. They do not go away. But they are insufficient for the expanded attack surface that emerges when you add organizational systems and family members to the protected perimeter.

### What Changes at Phase 2 Scale

**The perimeter is no longer just you.** Phase 1 protected one person with one set of devices. Phase 2 adds:

- Organizational systems (email, shared drives, cloud services, internal tools) where you are not the sole administrator and cannot control every endpoint
- Family members whose devices and accounts are linked to yours by shared Wi-Fi, shared Apple ID family groups, shared financial accounts, shared calendar visibility, or simply by the fact that a sophisticated adversary targeting you will use them as a lateral access vector
- Third parties (contractors, vendors, service providers) with access to organizational data who are outside your direct control

Each of these expands the attack surface multiplicatively, not additively. A stalker who cannot find your address directly may find your parents' address on Spokeo. A ransomware group that cannot breach your workstation may breach a contractor who has a VPN tunnel to your network. A state actor who cannot compromise your encrypted Signal communications may compromise a family member's unencrypted Gmail account to reconstruct your social graph and movement patterns.

**New vectors that appear at Phase 2 scale but not at Phase 1 scale:**

- **Credential reuse across organizational accounts**: Personal password hygiene (Bitwarden) protects personal accounts. It does not protect you if a colleague reuses a weak password on a shared organizational account that has administrative access to infrastructure you depend on.
- **Business email compromise (BEC)**: Attackers spoof or compromise organizational email accounts to authorize fraudulent wire transfers or credential resets. This requires organizational email, not personal email, to be a target.
- **Supply chain compromise**: A software tool or hardware device you or your organization relies on is compromised at the vendor level before it reaches you. No amount of personal device hygiene protects against a compromised software update from a trusted source.
- **Insider threat**: Someone with legitimate access — an employee, a contractor, a family member with your password — misuses that access. Phase 1 had no trusted insiders with meaningful access to organizational systems.
- **Physical security of organizational spaces**: Your home office, your organization's office, a shared coworking space. Phase 1 focused on device encryption (VeraCrypt, BitLocker) as a protection against device seizure. Phase 2 must also address who physically enters spaces where unencrypted data is visible on screens or printed on paper.

### What Phase 1 Mitigations Become Insufficient

| Phase 1 Control | Why It Becomes Insufficient at Phase 2 |
|-----------------|----------------------------------------|
| Bitwarden (personal) | Does not protect organizational accounts managed by others; does not address shared account credentials in team contexts |
| Signal (personal) | Does not protect organizational email; family members' unencrypted communications can reconstruct context that Signal-protected messages were meant to protect |
| VeraCrypt (personal) | Does not protect shared cloud storage (Google Drive, SharePoint, Dropbox); does not address backups made by organizational IT on your behalf |
| Ente Auth TOTP (personal) | Does not protect accounts where colleagues reset MFA without your knowledge; does not address accounts where IT has bypass authority |
| Data broker opt-outs (personal) | Family members' data broker profiles remain accessible and can be used to locate or pressure you through them |
| iPhone hardening (personal) | Does not protect family members' Android or iOS devices that are on your home Wi-Fi network and potentially visible to a local network attacker |

---

## Part 2: Adversary Assumptions for Phase 2

Phase 2 introduces four adversary classes that did not appear in Phase 1 modeling. Understanding each adversary's capabilities, motivation, and operational constraints is the prerequisite for building proportionate responses.

### Adversary Class 1: State Actor / Government Surveillance Apparatus

**Operational profile**: State actors have legal compulsion authority (subpoenas, National Security Letters, FISA orders), budget that dwarfs commercial threat actors, and access to surveillance infrastructure the target cannot see. In the U.S. context, this includes the Palantir ELITE platform (confirmed address scoring against immigration nexus populations), PRISM/Section 702 (compelled access to Google, Microsoft, Apple, Meta data on foreign communication partners), NSLs (compelled carrier metadata disclosure without judicial review), and ICE Mobile Fortify (field biometrics at any encounter).

**What they do that Phase 1 does not cover**: State actors can compel your cloud provider to produce data. They can compel your carrier to produce metadata. They can access financial records without a criminal warrant in some contexts. They operate at scale — they do not need to target you specifically to have your data; bulk collection means they may have years of metadata before they focus on you.

**Phase 2 relevance**: If you or your organization operates in a sector that has attracted government scrutiny (immigration advocacy, investigative journalism, labor organizing, financial resistance), you may move from a background data collection posture (you are in the bulk dataset) to an active targeting posture (you are a named subject). The transition between these states is the highest-risk period. Indicators of active targeting include: legal process served on service providers (you will not be notified until the gag order expires, which may be never), unusual device behavior consistent with implant activity, social network mapping through people around you.

**Key capability**: NSO Group Pegasus and equivalent commercial spyware (Predator, Graphite, Hermit) can achieve zero-click compromise of fully patched iOS and Android devices. As of 2025-2026, Pegasus variants using BLASTPASS have been confirmed operational against activists and journalists. iVerify has detected persistent variants on iOS 17 and Android 14 devices. iOS 26 erases key forensic indicators in shutdown.log that previously enabled detection. MVT (Amnesty International's Mobile Verification Toolkit) and iMazing Spyware Analyzer remain the primary detection tools for sophisticated mobile implants.

**Proportionate response boundary**: Most individuals and organizations will not face NSO-level capability. The appropriate Phase 2 response is not to assume Pegasus unless you are in a demonstrably high-risk sector; it is to layer defenses that raise the cost of surveillance to a level that redirects adversary resources to easier targets, while maintaining the ability to recognize and escalate if indicators of sophisticated targeting appear.

### Adversary Class 2: Insider Threat

**Operational profile**: A trusted person with legitimate access who misuses that access — intentionally or through negligence. The 2025 Ponemon Cost of Insider Risks Report puts the average annual cost of insider risk at $17.4 million per organization. The categories are: malicious insider (intentional exfiltration or sabotage), negligent insider (accidental exposure through careless behavior), and compromised insider (external attacker using a legitimate employee's credentials without their knowledge).

**What they do that Phase 1 does not cover**: Insiders bypass perimeter defenses entirely. They are already inside. They have legitimate credentials. They know where the sensitive data is and how systems work. A malicious insider exporting a customer database to a personal Google Drive does not trigger the same alerts as an external attacker brute-forcing login attempts.

**Family context**: In a household threat model, the insider category includes family members who share devices, passwords, or accounts. This is not necessarily malicious — a family member who uses your laptop logged into your cloud storage, then loses that laptop, has created an insider-equivalent exposure. Coerced access (a family member pressured by a third party to provide your credentials) is a distinct sub-scenario addressed in Scenario 6.

**Phase 2 relevance**: Build a minimum-privilege access model for organizational systems before Phase 2 expansion. Each person should have access only to what they need. Audit logs should capture who accessed what. For family context: separate accounts, separate devices where possible, and explicit household security agreements about what is shared.

### Adversary Class 3: Supply Chain Attacker

**Operational profile**: Rather than attacking you directly, the attacker compromises a vendor, software publisher, hardware manufacturer, or service provider that you trust, and uses that trusted relationship to reach you. The 2026 supply chain security landscape shows a surge in March 2026 specifically (documented by Zscaler ThreatLabz), with software supply chain attacks increasingly targeting developer credential stores, build pipelines, and package registries (npm, PyPI, RubyGems).

**Canonical Phase 2 scenarios**: A software tool your organization uses receives a malicious update signed with the vendor's legitimate signing key (analogous to SolarWinds/SUNBURST). A hardware device (router, USB hub, webcam) is intercepted in transit or manufactured with a pre-installed implant (supply chain interdiction). A telecom provider is compromised, exposing metadata or enabling SIM-swapping at scale (Salt Typhoon's confirmed 2024-2025 compromise of U.S. carrier infrastructure, which exposed call records and SMS metadata across multiple major carriers).

**Detection signals**: Behavior-analysis scanners like Socket and Endor Labs can detect suspicious package lifecycle behavior before advisories exist. Maintaining a software bill of materials (SBOM) and diffing it against previous builds surfaces new transitive dependencies before they execute. Network traffic anomalies (unexpected outbound connections from trusted software) are often the first runtime indicator.

**Phase 2 relevance**: You cannot audit every piece of software your organization uses. The appropriate response is defense-in-depth that limits blast radius: segment networks so a compromised device cannot reach the entire environment, maintain offline backups that a compromised cloud service cannot reach, and verify software signatures and download integrity before installing updates on sensitive systems.

### Adversary Class 4: Sophisticated Persistent Attacker (Non-State)

**Operational profile**: Organized cybercriminal groups, ransomware-as-a-service affiliates, and targeted commercial espionage actors. These are not script kiddies — they operate with patience, tradecraft, and specialization. The Bybit heist (2025) exemplifies this: the attacker spent 20 days posing as a trusted contributor before executing the theft. Pretexting now accounts for 27% of social engineering breaches, nearly double prior-year rates, with AI-enabled multi-channel pretexting emerging as the dominant vector in 2026.

**What distinguishes them from Phase 1 adversaries**: Time. A Phase 1 opportunistic attacker tries once, fails, and moves on. A sophisticated persistent attacker invests weeks or months, maps your organization, identifies weak links (employees, vendors, family), and waits for the right moment. They adapt their approach based on what works. They conduct reconnaissance before attacking — your public social media, your organization's website, your LinkedIn, your employees' profiles.

**Ransomware specific**: Modern ransomware groups use a "double extortion" model: they exfiltrate data before encrypting it, so even a successful recovery from backup does not eliminate the extortion threat (the threat actor still has a copy of your data and will publish or sell it). The decision tree in Scenario 1 addresses this explicitly.

---

## Part 3: Six Scenario Playbooks

**How to use these playbooks**: Each playbook has a detection signal checklist, an immediate response section (first 24 hours), a decision tree, and a recovery section (days 2 to 30+). Follow the decision tree from the first question. Each terminal node has a named action and a timeline. If you are working through an active incident, assign the actions to a specific person before leaving that node.

---

### Scenario 1: Ransomware Attack on Organizational Systems

**What this scenario covers**: Discovery that organizational systems (workstations, servers, shared drives, cloud infrastructure) have been encrypted by ransomware, with or without prior data exfiltration.

**Detection signals** (any one of these triggers the playbook):
- Files on workstations or shared drives have unrecognizable extensions (e.g., `.locked`, `.enc`, `.WASTED`, random alphanumeric suffix)
- Ransom note appears on desktop or in directories as a text or HTML file
- Users cannot open previously accessible files
- Antivirus or EDR alerts fire for ransomware-associated behaviors (mass file encryption, shadow copy deletion, LSASS access)
- Network monitoring shows unusual lateral movement or mass SMB connections prior to encryption event
- A cloud storage service (Google Drive, Dropbox, SharePoint) shows a bulk file change or deletion event from an unfamiliar device

**Immediate response — first 2 hours:**

1. **Isolate affected systems immediately.** Disconnect from the network (unplug Ethernet, disable Wi-Fi at the adapter level, do not just close the lid). Do this physically — do not attempt to "fix" the system first. Every additional minute a ransomware process runs increases encrypted file count and potential lateral spread.
2. **Do not power off.** Counter-intuitive, but critical: powered-off machines lose volatile memory that may contain encryption keys or attacker artifacts. Leave systems running but isolated. Exception: if the system is actively spreading to others on the network, power off trumps forensic preservation.
3. **Identify the blast radius.** Which systems are affected? Which are not? Network segment the unaffected systems immediately (physically isolate them from the affected segment if shared-switch infrastructure is involved).
4. **Assess backup status.** Are backups intact? Where are they stored? Are they offline (air-gapped) or cloud-synced (potentially also encrypted)? Do not connect backup media to an infected network.
5. **Do not pay the ransom yet.** Paying does not guarantee decryption. It funds future attacks. Approximately 80% of organizations that pay are attacked again within a year. Exhaust decryption options first.

**Decision tree:**

```
Q1: Are systems still actively encrypting?
  YES → Immediately physically isolate ALL networked systems (unplug everything).
        Go to Q2.
  NO  → Systems isolated or encryption complete. Go to Q2.

Q2: Is this ransomware variant known? (Check No More Ransom: nomoreransom.org)
  YES, free decryptor exists → Download decryptor on a CLEAN, isolated machine.
                               Do not connect to the infected network.
                               Test decryptor on a non-critical file first. Go to Q5.
  NO, no decryptor available → Go to Q3.

Q3: Are offline backups intact and from before the infection date?
  YES → Identify infection date (earliest ransom note timestamp or log evidence).
        Confirm backups predate that timestamp. Go to Q4.
  NO, backups also encrypted or missing → Go to Q3b.

  Q3b: Was data exfiltrated before encryption?
    UNKNOWN → Assume yes. Begin breach assessment. Go to Q6.
    CONFIRMED YES → Begin breach assessment. Go to Q6.
    CONFIRMED NO → Ransomware-only. Negotiate only as last resort. Go to Q3c.

  Q3c: Is the encrypted data business-critical with no recovery path?
    YES → Engage a ransomware negotiation specialist BEFORE paying anything.
          Never negotiate directly. Document negotiation for law enforcement.
          Go to Q6.
    NO  → Accept data loss. Proceed to clean rebuild. Go to Q5.

Q4: Restore from backup on clean hardware (not the infected machine).
    Verify restored files are intact before reconnecting to network.
    After restoration: go to Q6 for breach assessment and notification.

Q5: Decryption/restore successful?
  YES → Before reconnecting: rebuild trust by reimaging affected systems from
        clean media. Restoring files to a compromised OS does not remove
        the attacker's persistence mechanisms. Go to Q6.
  NO  → Go back to Q3.

Q6: Was data exfiltrated (known or suspected)?
  YES or UNKNOWN → Initiate breach notification assessment.
    - GDPR: notify supervisory authority within 72 hours if EU resident data
    - PIPEDA: notify OPC "as soon as feasible" if real risk of significant harm
    - U.S.: notify affected individuals per applicable state law (most require
      notification within 30-60 days)
    - Assign: Legal counsel + named responsible person.
    - Deadline: 72 hours for GDPR; document PIPEDA assessment within 24h.
  NO  → No notification required. Document finding. Go to prevention phase.
```

**Recovery — days 2 to 30+:**

Days 2-7: Forensic investigation on isolated systems (or via specialist). Identify the initial access vector (phishing email? RDP brute force? Compromised vendor credential? Malicious software update?). Document the infection chain. This is not optional — without knowing how they got in, you cannot close the door.

Days 7-14: Rebuild affected systems from clean media. Do not restore from backup to the same OS image — the OS may contain persistence mechanisms. Reimage first, restore data second.

Days 14-30: Address root cause. If initial access was a phishing email, implement mandatory MFA on email and deploy email security (DMARC, DKIM, SPF). If RDP was the vector, disable public-facing RDP and use a VPN with MFA for remote access. If a vendor credential was compromised, revoke and rotate all third-party credentials and implement a vendor access review.

**Phase 1 integration**: VeraCrypt local encryption protects your personal files from a ransomware sweep if the encrypted container is dismounted at time of attack. Bitwarden ensures you have unique credentials for each organizational service, limiting credential reuse as a lateral movement vector.

**Phase 2 Wave integration**: This scenario is the primary driver of the offline backup infrastructure in Phase 2 Wave 1. The Scenario 3 (PHASE_3_RANSOMWARE_RECOVERY_PLAN.md) document in the project provides additional infrastructure-level detail.

---

### Scenario 2: Credential Compromise (Email or Password Breach)

**What this scenario covers**: Discovery that one or more credentials (password, session token, API key) for an account you or your organization controls have been compromised — either confirmed via notification, or inferred from suspicious account activity.

**Detection signals:**
- Breach notification email from a service (Have I Been Pwned alert, service's own notification)
- Unexpected password reset email you did not request
- Login from an unrecognized location or device (visible in account security logs)
- Accounts behave abnormally: sent messages you did not write, settings changed, contacts removed
- A colleague reports receiving a suspicious email "from you"
- Security audit of Bitwarden or organizational password manager surfaces reused credentials

**Immediate response — first 1 hour:**

1. **Do not dismiss the alert.** Treat every breach notification as real until confirmed otherwise.
2. **Assess the account type.** Is this a personal account, an organizational account, or an account that has administrative access to other accounts? The scope of response scales with the account's privilege level.
3. **Change the password immediately** from a clean device (not the potentially compromised device). Use Bitwarden to generate a new unique 20+ character password.
4. **Revoke all active sessions** (most services have a "Sign out of all devices" option in security settings). This terminates any active attacker session using the compromised credential.
5. **Rotate the MFA credential** if the account uses TOTP (Ente Auth). Generate a new TOTP secret. If the attacker has your TOTP seed, they can generate codes indefinitely — a password change alone is insufficient.

**Decision tree:**

```
Q1: How was the compromise discovered?
  BREACH NOTIFICATION (service or HaveIBeenPwned) → Go to Q2.
  SUSPICIOUS ACTIVITY OBSERVED → Go to Q3.
  SECURITY AUDIT / PROACTIVE DISCOVERY → Go to Q4.

Q2 (Breach notification path):
  Is the breached service one you currently use or have used?
  NO, never had an account → Ignore. Document false positive.
  YES, former account → Change password if you haven't already.
                        Check if this email/password was reused elsewhere
                        (check Bitwarden for duplicate passwords). Go to Q5.
  YES, active account → Go to Q3.

Q3 (Suspicious activity observed):
  Is the activity ongoing right now?
  YES → Immediately revoke all sessions (sign out everywhere).
        Change password on a clean device. Go to Q4.
  NO, historical → Determine timeframe of unauthorized access. Go to Q4.

Q4 (Assess scope):
  Was this account used to manage other accounts (SSO, admin role, email)?
  YES → This is a privileged account compromise. Go to Q4a.
  NO  → Single account breach. Go to Q5.

  Q4a (Privileged account):
    Does this account control organizational email, DNS, or cloud infrastructure?
    YES → Treat as potential full organizational compromise.
          Engage all organization administrators immediately.
          Audit ALL accounts that could be reset via this email address.
          Rotate credentials for ALL dependent systems in order of privilege.
          Timeline: complete within 4 hours.
    NO  → Elevated personal account. Audit downstream accounts. Go to Q5.

Q5 (Credential reuse check):
  Were any other accounts using the same password?
  YES → Change password on EVERY account that shared this password immediately.
        Prioritize: email, banking, organizational accounts, identity providers.
        Use Bitwarden's reused passwords report to find all instances.
  NO  → This password was unique. Damage is limited to this account. Go to Q6.

Q6 (Notification assessment):
  Did the compromised account contain personal data belonging to others
  (customers, clients, employees)?
  YES → Begin breach notification assessment per applicable law. (See Q6 in
        Scenario 1 for GDPR/PIPEDA/state law thresholds.)
        Responsible person: Legal counsel. Timeline: 24 hours to assess.
  NO  → Document the incident. Implement post-incident improvements. Done.
```

**Recovery — days 2 to 30+:**

Days 2-7: Audit what the attacker could have accessed during their window. If they had access to email, they may have read messages, forwarded future email to an attacker-controlled address (check mail forwarding rules), or used password reset flows to access other accounts. Check every account that accepts password reset via the compromised email.

Days 7-14: Enable hardware security key (YubiKey) as primary MFA for email and any privileged account if not already in place. TOTP is significantly better than SMS, but a hardware key is phishing-resistant in a way that TOTP is not (TOTP codes can be captured by a real-time phishing proxy; hardware keys cannot because they bind to the domain of the legitimate site).

Days 14-30: Run a full Bitwarden audit. Eliminate all reused passwords. Set up Have I Been Pwned monitoring for all organizational email domains.

**Phase 1 integration**: Bitwarden ensures no password reuse. Ente Auth provides TOTP isolation (if compromised, only TOTP codes leak, not TOTP seeds if stored encrypted). Data broker opt-outs reduce the publicly available information an attacker can use for account recovery social engineering.

---

### Scenario 3: Targeted Social Engineering Campaign

**What this scenario covers**: A multi-touch attempt to manipulate you, a family member, or an organizational colleague into revealing credentials, granting access, making a financial transfer, or taking an action that benefits the attacker. Distinguishing feature: the attacker has done research on you specifically and the attempt is personalized.

**Detection signals** (the harder to recognize, the more sophisticated the attacker):
- An email, call, or message that references accurate personal details (your job title, a recent event, a colleague's name) but arrives via an unexpected channel
- A request to "verify" credentials, approve a financial transaction, or take urgent action that bypasses normal process
- A caller or emailer who creates urgency ("this has to happen today or the account will be suspended")
- A message appearing to be from a trusted party (IT, bank, vendor, family member) but arriving from a slightly wrong address or through an unusual channel
- A colleague reports receiving a message "from you" that you did not send
- A vendor or service provider asks you to update payment information or banking details
- You receive a login notification for an account you just tried to reset, suggesting someone else triggered the flow simultaneously (real-time phishing proxy attack)

**Immediate response — first 30 minutes:**

1. **Stop. Do not take the requested action.** Urgency is the primary social engineering lever. Slowing down and verifying costs nothing; acting immediately may be irreversible.
2. **Verify through an independent channel.** If the email claims to be from your bank, call the number on your card, not the number in the email. If it claims to be from a colleague, call or Signal them directly. Do not reply to the suspicious message to ask if it is real — the attacker controls that channel.
3. **Document everything.** Screenshot the message before you do anything else. Note the timestamp, sender details (hover over the display name to see the actual email address), and the requested action. This is your forensic record.
4. **Do not click links in the suspected message.** If you need to visit a site mentioned in the message, navigate there directly in your browser.

**Decision tree:**

```
Q1: Has anyone taken the requested action already?
  YES → What was the action?
    Financial transfer → Contact bank immediately to initiate recall.
                         Not all transfers are reversible, but time matters.
                         Recall window: wire transfers 24-48h, ACH 2 business days.
                         Go to Q2 after bank contact.
    Credentials entered → Treat as Scenario 2 (credential compromise). Go there.
    Access granted → Revoke the access immediately. Go to Q2.
    Information shared → Assess what was shared and with whom. Go to Q2.
  NO → No action taken. Verify the message is indeed suspicious. Go to Q2.

Q2: Was this targeted at you specifically (personalized details) or generic?
  PERSONALIZED → This is a targeted attack. Attacker has conducted reconnaissance.
                 Go to Q3.
  GENERIC (mass phishing) → Lower severity. Report to IT/email provider.
                             Document for awareness. Go to Q4.

Q3 (Targeted attack — investigation protocol):
  Who else in your organization or household might receive similar messages?
  YES → Alert all household members and organizational colleagues immediately.
        Use a trusted out-of-band channel (Signal, in-person, phone call).
        Brief: "We are under a targeted social engineering attempt. Do not
        take any urgent requests at face value. Verify all requests by calling
        back on known numbers before acting."
        Timeline: within 1 hour of confirming the attack is targeted.
  NO / UNKNOWN → Proceed as if others may be targeted. Issue the alert.

Q4 (Notify external authorities?):
  Was money transferred or credentials for financial accounts compromised?
  YES → File report with FBI IC3 (ic3.gov) and FTC (reportfraud.ftc.gov).
        If wire transfer: notify bank immediately AND file IC3 within 24 hours
        (FBI Financial Fraud Kill Chain is most effective within 72 hours of transfer).
  Were organizational systems accessed or data exfiltrated?
  YES → Depending on sector: notify relevant regulator (FTC, SEC, HHS, etc.)
        Engage legal counsel to assess notification obligations.
  NO significant loss → Document internally. No mandatory reporting triggered.

Q5 (Post-incident security measures):
  Implement or verify:
  - Domain-based email authentication (DMARC, DKIM, SPF) — prevents display-name spoofing
  - Organizational procedure: ALL financial transfers above $X require
    phone verification on a number pre-established out-of-band
  - Hardware security keys for privileged accounts (phishing-resistant MFA)
  - Security awareness notification for all team members describing the
    specific technique used in this attempt (within 1 week of incident)
```

**Recovery — days 2 to 30+:**

Days 2-7: Review email logs for signs of prior reconnaissance (unusual link clicks, file downloads from people who may have been the attacker scoping your organization). Attackers often conduct weeks of low-and-slow reconnaissance before the overt social engineering attempt.

Days 7-14: Run a tabletop exercise specifically recreating the vector used in this attack with your team or household. The highest-fidelity training is a scenario the organization just survived.

Days 14-30: Implement vendor payment verification procedures if this was a business email compromise attempt. Establish a verbal confirmation protocol: any change to banking or payment details requires a call to a pre-known number to confirm before processing.

**Phase 2 Wave integration**: Phase 2 Wave 1 includes deploying DMARC/DKIM/SPF for organizational email domains. This is the single highest-leverage technical control against impersonation-based social engineering.

---

### Scenario 4: Physical Device Theft or Seizure

**What this scenario covers**: A device (laptop, phone, tablet, external drive) is lost, stolen, or seized by law enforcement or another party. The threat is unauthorized access to data on that device.

**Pre-theft prevention — confirm these are in place before an incident occurs:**

- **FileVault (macOS) or BitLocker (Windows)**: Full disk encryption, enabled with a strong passphrase not stored on the device. Seized powered-off encrypted laptop = unreadable.
- **iPhone passcode**: 6+ digit numeric or alphanumeric. The device auto-wipes after 10 failed attempts if enabled. All data is encrypted if a passcode is set.
- **iCloud Advanced Data Protection**: Enabled (per Phase 1). Your iCloud backups are encrypted end-to-end. Even if Apple receives a legal order, they cannot produce decrypted backup content.
- **Remote wipe capability**: Apple: Find My (Settings > [Your Name] > Find My). Enrolled MDM (Mobile Device Management) for organizational devices.
- **Lock screen notifications disabled**: Settings > Notifications > Show Previews = Never. This prevents anyone holding your phone from reading message content without unlocking.

**Immediate response — first 1 hour:**

1. **Confirm the device is actually gone.** Use Find My (Apple) or Android's Find My Device to locate it. If it shows at an address you recognize (office, car), retrieve it before initiating remote wipe.
2. **Assess BFU (Before First Unlock) status.** A device that was powered off or rebooted and never unlocked after reboot is in BFU state. Modern forensic tools (Cellebrite, GrayKey) have significantly reduced capability against BFU devices. If the device was powered off at time of seizure/theft, your encryption provides maximum protection.
3. **Remote wipe if you cannot recover.** Apple: iCloud.com > Find My > select device > Erase. Android: myaccount.google.com > Security > Find a lost device > Erase device. This requires the device to have network connectivity. If it is offline, the wipe command queues and executes on next network connection.
4. **Change credentials immediately.** Even if the device is encrypted and wiped, change passwords for any account that was logged in on that device. Session tokens stored on a device can be extracted before decryption in some forensic scenarios. Prioritize: email, Bitwarden master, any organizational account.

**Decision tree:**

```
Q1: Is this theft (external party, criminal) or seizure (law enforcement)?
  THEFT → Go to Q2.
  SEIZURE (law enforcement with warrant) → Go to Q3.
  SEIZURE (law enforcement without warrant or unclear authority) → Go to Q3b.

Q2 (Theft):
  Is the device encrypted (BitLocker/FileVault/iPhone passcode)?
  YES, confirmed → Data risk is low if device remains offline and attacker
                   does not have the passphrase. Remote wipe as precaution.
                   Change all account credentials. Go to Q4.
  NO, or unknown → Assume all data on the device is compromised.
                   Treat as data breach. Go to Q4 plus breach assessment.

Q3 (Law enforcement seizure with warrant):
  Do not physically resist. Do not provide passwords unless compelled by court order.
  The Fifth Amendment (U.S.) protects against compelled password disclosure in
  most circumstances (though this is contested law — consult an attorney).
  Has encryption been confirmed active at time of seizure?
  YES → Contact legal counsel. Document the seizure (date, time, what was taken,
        agency, badge number). Do not consent to additional searches.
  NO  → Assume data accessible. Notify legal counsel immediately.
  In either case: Go to Q4.

Q3b (Seizure without warrant or under unclear authority):
  Border crossing (CBP): CBP claims authority to search devices at the border
  without a warrant. Logging out of accounts (not deleting — just logging out)
  before crossing a border limits accessible data to what is locally cached.
  Factory reset is legal but may appear suspicious.
  State the device is encrypted. Do not provide the passphrase. CBP may detain
  the device. Contact legal counsel before the crossing if traveling to a
  high-risk border.
  Employer seizure: If your employer has MDM on the device, they may have remote
  wipe authority. Know your organization's MDM policy before putting personal
  data on an employer device.
  Go to Q4 after documenting the encounter.

Q4 (Notification and recovery):
  Was organizational data on the device?
  YES → Notify IT/security lead within 2 hours. Begin breach assessment.
  Were personal communications of others on the device?
  YES → Notify the individuals whose communications may have been exposed.
        Use Signal (per Phase 1 setup) to notify — other channels may also be
        compromised if account credentials were on the device.
  Was data specifically subject to GDPR/PIPEDA protection on the device?
  YES → Begin breach notification assessment per applicable law.
  NO / PERSONAL ONLY → Document the incident. Monitor accounts for unauthorized
                        access for 30 days.
```

**Recovery — days 2 to 30+:**

Days 2-7: Audit what was stored on the device. Reconstruct the data inventory (apps logged in, documents cached, passwords in browser, photos, contacts). This list defines your exposure surface.

Days 7-14: Replace the device. When setting up a new device, audit which apps you reinstall — use this as a forced opportunity to reduce surface area. Do not restore from an iCloud or Android backup to a new device without verifying the backup was made before the incident.

Days 14-30: For high-risk travelers (journalists, activists, anyone crossing borders into jurisdictions with aggressive device search authority): implement a travel device protocol. Use a clean device with minimal data for international travel. Log out of all accounts before crossing. Cross with only the data you need for the specific trip.

**Phase 1 integration**: BitLocker/VeraCrypt encryption ensures a stolen powered-off device is unreadable. iPhone Advanced Data Protection ensures cloud backup is not accessible via legal compulsion.

---

### Scenario 5: Communications Intercept or Surveillance Indication

**What this scenario covers**: Discovery of evidence — behavioral, technical, or circumstantial — that your communications or activities are being monitored by a third party. This ranges from targeted stalkerware on a device to sophisticated state-actor implants.

**Detection signals** (organized by sophistication level):**

Low-sophistication indicators:
- A person knows things they could only know by monitoring your communications
- Someone references a conversation that you conducted privately
- Unusual SMS messages containing strange characters (some stalkerware uses SMS-based command-and-control)
- Unexplained data usage spikes (Settings > Cellular/Mobile Data > sort by data used)
- Battery drain significantly faster than usual on a device that has not changed in use pattern
- Device warmer than expected when idle
- Microphone or camera indicator (orange dot on iPhone) appearing when no app should be using it

Moderate-sophistication indicators:
- Network traffic analysis shows unexpected outbound connections from a trusted device (requires router log access or network monitoring tool like Little Snitch on macOS)
- A Signal conversation shows the safety number changed without your contact having changed their device (could indicate a Signal link-device attack — see Phase 1 implementation guide on Signal safety numbers)
- A trusted contact received a message purportedly from you that you did not send
- iVerify (iverify.io) or MVT scan returns positive indicators of compromise

High-sophistication indicators:
- MVT (mvt.re) or iMazing Spyware Analyzer returns Pegasus, Predator, or equivalent IOCs
- Law enforcement contact that reveals they have knowledge that could only come from intercepted communications
- Device forensics by a trusted security researcher identifies implant artifacts

**Immediate response — first 2 hours:**

1. **Move to a clean device immediately.** Do not continue sensitive communications on a device you suspect is compromised. If you do not have a clean device, borrow one or use a freshly factory-reset device (note: factory reset may not remove sophisticated implants — a new device is preferable).
2. **Do not power off or wipe the suspected device yet.** It is forensic evidence. The implant may leave more traces during operation than after a wipe. Isolate it (Airplane Mode) and preserve it for analysis.
3. **Alert trusted contacts via a different channel.** If Signal on your iPhone is potentially compromised, contact your most sensitive sources or family members via a different device or app immediately. Inform them that your device may be compromised and to treat any unusual messages from your known account with skepticism until you confirm your situation.
4. **Change account passwords from the clean device.** The compromised device may have captured passwords entered on it. Rotate credentials for all accounts using Bitwarden on a clean device.

**Decision tree:**

```
Q1: What severity level are the indicators?
  LOW (behavioral only, no technical confirmation) → Go to Q2.
  MODERATE (technical indicators, unconfirmed) → Go to Q3.
  HIGH (confirmed implant or forensic confirmation) → Go to Q4.

Q2 (Low severity — behavioral indicators):
  Is there an innocent explanation for the information leak?
  YES → Document, monitor, do not escalate yet.
  NO  → Conduct a technical sweep.
    Run iVerify (iverify.io) on iPhone — basic version is free.
    Run MVT on a computer to analyze iPhone backup (advanced, requires technical comfort).
    Check app permissions: Settings > Privacy — look for unexpected apps with
    microphone, camera, or location access.
    If technical sweep returns negative → behavioral indicators only.
    Continue monitoring, increase operational security (see Q5 security pivots).

Q3 (Moderate severity — technical indicators):
  Have you clicked any unexpected links recently? Opened any attachments from
  unknown senders? Accepted any unexpected QR codes (Signal group invite exploit)?
  YES → Identify the likely infection vector. Document it.
  NO  → Zero-click or supply chain is possible. This escalates severity.
  In either case: Go to Q4 response protocol. The boundary between moderate
  and high is a judgment call — if in doubt, treat as high.

Q4 (High severity — escalation protocol):
  Are you a journalist, activist, attorney, or other high-risk occupation?
  YES → Contact Access Now's Digital Security Helpline (accessnow.org/help)
        or EFF's Surveillance Self-Defense resources for referral to a trusted
        digital security researcher who can conduct forensic analysis.
        Do not hand your device to law enforcement for "forensic analysis" unless
        legally compelled — this is not the same as a trusted security researcher.
  NO  → Contact a reputable cybersecurity firm for device forensics.
        Preserve the device in Airplane Mode as forensic evidence.
        Go to Q5.

Q5 (Operational security pivots):
  Immediate pivots (regardless of severity level confirmed):
  - Primary communications: Signal on a new device (not the suspected one)
  - Verify Signal safety numbers with all key contacts in person or via
    authenticated out-of-band channel (not via the same potentially-compromised device)
  - Sensitive conversations: in-person only, in locations you have not visited
    with the potentially-compromised device recently (phone may log location
    even before active surveillance was deployed)
  - For 30 days: assume all communications on the suspected device were monitored.
    Act accordingly in legal, professional, and personal contexts.

  Are others in your household at potential risk?
  YES → Sweep household devices (check permissions, run iVerify on each iPhone,
        look for unfamiliar apps on Android).
        Change home Wi-Fi password — some implants use local network for C2.
  NO / UNKNOWN → Assume yes. Sweep household devices as above.

  Law enforcement contact:
  Should you contact law enforcement?
  This depends entirely on whether law enforcement is the threat actor.
  If the suspected surveillance is FROM law enforcement (state actor model):
  do not contact law enforcement. Contact an attorney (privileged) and
  a trusted digital security researcher.
  If the suspected surveillance is from a private party (stalkerware, criminal):
  yes, contact law enforcement AND a digital security researcher.
```

**Recovery — days 2 to 30+:**

Days 2-7: If a device was forensically confirmed compromised, do not reuse it. Factory reset eliminates most commercial stalkerware but sophisticated state-actor implants may survive. Purchase a new device. When activating the new device, do not restore from a backup made while the old device was potentially compromised — restore from a backup predating the suspected infection window, or start fresh.

Days 7-30: Security posture hardening specific to surveillance threat. Enable Lockdown Mode on iPhone (Settings > Privacy & Security > Lockdown Mode). Lockdown Mode disables JavaScript JIT compilation, limits message attachment types, disables link previews in Messages, blocks configuration profiles, and restricts Bluetooth accessories — substantially reducing the attack surface for zero-click exploits at some cost to functionality.

**Phase 1 integration**: Signal (with proper safety number verification per Phase 1 setup) remains one of the highest-assurance messaging options available. The key caveat is device integrity: Signal's encryption is only as strong as the device it runs on. A compromised device can capture Signal messages before they are encrypted for transmission. Device security (Phase 1 iPhone hardening) and communications security (Signal) must be maintained together.

---

### Scenario 6: Family Member Compromise

**What this scenario covers**: A threat that materializes through a household member rather than directly through you. This includes: a family member's account being taken over by an external attacker, a family member being coerced or deceived into providing access to your systems, or a family member's compromised device creating a lateral access path to the household network or shared accounts.

**Why this is a distinct scenario**: Family members may have different security awareness levels, different devices, and different accounts than you — but they share your threat environment. A sophisticated attacker who cannot compromise you directly has strong incentive to compromise someone around you. The DV survivor safety playbook in the project corpus (`dv-survivor-safety-playbook.md`) covers intimate partner surveillance in detail. This scenario covers the broader household threat model.

**Detection signals:**
- A family member reports receiving unusual messages, password reset emails they did not request, or account behavior they cannot explain
- You receive notifications about account activity on a shared account (family iCloud, shared Netflix, shared banking) that you did not initiate
- A family member mentions they shared a password, clicked a link, or responded to an urgent request from someone claiming to be from a service or authority
- A family member's device is behaving strangely (battery drain, heat, data usage spikes)
- You receive communications from an attacker who demonstrates knowledge of household details that only a compromised family member's device or account could provide
- A family member reports being pressured by someone to provide access to your accounts, devices, or communications

**Immediate response — first 2 hours:**

1. **Assess the family member's safety first.** If coercion is involved, their physical safety is the priority before any technical response.
2. **Identify the scope without alarming the family member unnecessarily.** If you suspect a device is compromised but the family member does not know, your approach depends on whether they are a potential vector for the attacker or a victim. Ask open-ended questions to understand what happened without creating panic.
3. **Remove shared access immediately.** If the compromised account or device has access to shared systems (family iCloud, shared password manager, shared Wi-Fi with organizational devices), revoke that access while you assess the situation. This is not punitive — it is containment.

**Decision tree:**

```
Q1: What is the nature of the compromise?
  EXTERNAL ATTACKER took over family member's account → Go to Q2.
  FAMILY MEMBER was coerced or deceived into providing access → Go to Q3.
  FAMILY MEMBER'S DEVICE is suspected to be compromised → Go to Q4.
  FAMILY MEMBER voluntarily shared access (without understanding risk) → Go to Q5.

Q2 (External account takeover of family member):
  Apply the Scenario 2 (credential compromise) playbook for the family member's
  account immediately. The decision tree is the same. Additional considerations:
  - Attacker may use the family member's account to impersonate them to you.
    Verify all messages from the family member via an independent channel
    (phone call, in-person) until the account is recovered.
  - Check if the family member's account was used to access any shared accounts
    (shared streaming, shared banking, shared cloud storage).
  - If yes: treat those shared accounts as potentially compromised. Rotate
    credentials on all shared accounts. Timeline: within 2 hours.

Q3 (Coercion or deception of family member):
  Is the family member in immediate physical danger?
  YES → Physical safety first. Personal security second. Contact law enforcement
        if the threat is credible and immediate. The digital response can wait.
  NO  → Who coerced them, and what access was provided?
    ACCESS TO YOUR ACCOUNTS provided → Change all compromised account passwords
                                        immediately from a clean device.
                                        Treat as Scenario 2.
    PHYSICAL ACCESS TO YOUR DEVICES → Treat as Scenario 4. Check for installed
                                       apps, inspect recent activity logs.
    INFORMATION DISCLOSED (your schedule, address, habits) → Assess what was
                                                              disclosed. Notify
                                                              others at risk
                                                              (colleagues,
                                                              contacts) if the
                                                              information
                                                              enables targeting.

Q4 (Family member's device suspected compromised):
  Does the family member's device share a Wi-Fi network with your organizational
  or sensitive personal devices?
  YES → Segment the network. Create a separate guest network for the family
        member's device until it is cleaned or replaced. Most home routers
        support guest networks. This prevents a compromised device from
        scanning or accessing other devices on the same subnet.
  Is the family member willing to run a security scan?
  YES → Run iVerify (iPhone) or a reputable mobile security tool on the device.
        If confirmed compromised: replace the device (not just factory reset
        for sophisticated implants). Do not restore from a potentially compromised
        backup.
  NO  → Respect their autonomy. But isolate their device from shared networks
        until you can assess. Explain the risk plainly without blame.

Q5 (Family member voluntarily shared access, did not understand risk):
  What was shared?
  YOUR PASSWORD → Change it immediately. Implement separate accounts for each
                  household member. A shared password is an uncontrolled
                  credential — you cannot track who has used it or audit access.
  YOUR DEVICE (unlocked) → Check recent activity logs (browser history, app
                            access, file access timestamps). If unclear:
                            rotate credentials for any account that was logged
                            in on the device during the window it was shared.
  INFORMATION ABOUT YOUR SCHEDULE / LOCATION → Low technical risk. Assess
                                                whether the recipient of that
                                                information is a threat actor.

Q6 (Household coordination protocol — applicable in all branches):
  Which family members need to know about this incident?
  ALL household members → If the attack was targeted at the household (not
                          just one member), all members need an immediate
                          brief at their level of security awareness.
  SOME members → If some family members are the potential vector and do not
                 know they are being targeted, calibrate the brief carefully.
                 You want to alert them without creating panic or inadvertently
                 tipping off an attacker through their subsequent behavior change.
  NOBODY yet → You are still in assessment. Set a 24-hour limit: by the end
               of assessment, household members who are at risk must be informed.
```

**Recovery — days 2 to 30+:**

Days 2-7: Establish household security agreements. Not rules imposed from above — agreements reached collaboratively. What accounts are shared? What are the expectations around sharing passwords? What does each household member do if they receive an unusual message or request? Write this down and share it. Security that is understood is security that is practiced.

Days 7-14: Audit shared accounts and access. Every service where multiple household members have the same login credential is a shared risk. Where separate accounts exist (each person's Apple ID, each person's email), shared access should be via explicit sharing features (Family Sharing, shared folders) not shared credentials.

Days 14-30: Calibrate household security training to the actual sophistication of each household member. Not everyone needs to understand the full threat model. Everyone needs to understand: (1) how to recognize a suspicious message, (2) to verify urgent requests independently before acting, (3) to report unusual device or account behavior immediately without fear of blame.

**Phase 1 integration**: Data broker opt-outs reduce the information available for profiling household members. Signal setup for all household members who are willing creates an encrypted channel for family coordination that does not expose message content to a network-level attacker or to service provider subpoena.

**Phase 2 Wave integration**: The household network segmentation capability (guest network isolation, separate VLANs for organizational devices) is a Phase 2 Wave 1 infrastructure item. Until that is implemented, a stopgap is using a travel router (GL.iNet or similar) to create a physically separate network segment for sensitive organizational devices.

---

## Part 4: Cross-Project Integration

### How Phase 2 Threat Model Connects to Phase 2 Implementation Roadmap

The six playbooks above map directly to the Phase 2 implementation waves described in `PHASE_2_IMPLEMENTATION_ROADMAP.md` and `PHASE_2_DETAILED_IMPLEMENTATION_ROADMAP.md`. The connection is as follows:

**Wave 1 (July 2026)**: The ransomware and credential compromise playbooks (Scenarios 1 and 2) are the primary drivers for Wave 1 technical infrastructure:
- Offline backup system (ransomware recovery path in Scenario 1 Q3)
- Hardware security keys/YubiKey for privileged accounts (Scenario 2 recovery)
- DMARC/DKIM/SPF deployment for organizational email (Scenario 3 prevention)

**Wave 2 (September 2026)**: The social engineering and physical theft playbooks (Scenarios 3 and 4) drive Wave 2 organizational security controls:
- Vendor payment verification protocol (Scenario 3, Q4)
- Travel device protocol (Scenario 4 recovery)
- Network segmentation for organizational devices (Scenario 6 Q4)

**Wave 3 (Post-adoption gate)**: The surveillance and family compromise playbooks (Scenarios 5 and 6) require sustained household-level coordination and are appropriate for Wave 3 once the organizational infrastructure from Waves 1-2 is stable.

### Adversary-to-Playbook Mapping

| Adversary Class | Primary Scenarios | Phase 2 Technical Counter |
|-----------------|-------------------|---------------------------|
| State Actor | Scenario 5, 4 | Lockdown Mode, hardware keys, border device protocol |
| Insider Threat | Scenario 6, 2 | Minimum privilege access, audit logging, separate accounts |
| Supply Chain | Scenario 1, 5 | SBOM tracking, network segmentation, software verification |
| Sophisticated Persistent | Scenario 1, 2, 3 | MFA everywhere, offline backups, DMARC, behavioral monitoring |

### Phase 1 Controls That Remain Load-Bearing in Phase 2

These are not superseded by Phase 2 — they remain the foundation:

- **Signal + safety number verification**: Still the primary secure communications channel. Becomes more important as organizational context introduces more communication vectors. Verify safety numbers with any contact whose communications carry significant risk if intercepted.
- **VeraCrypt**: Remains the primary protection for sensitive files at rest on Windows. Phase 2 adds organizational data scope — VeraCrypt containers should be used for any locally cached organizational data that would be damaging if a device were seized.
- **Bitwarden + unique passwords**: The zero-reuse credential policy becomes the single most important control at organizational scale. Every shared organizational account where the password was ever stored in a browser or reused from another service is a potential breach vector.
- **iPhone hardening (Advanced Data Protection, Lockdown Mode)**: Lockdown Mode specifically becomes relevant at Phase 2 because the threat model now includes state-actor-grade mobile implants, not just opportunistic malware.
- **Data broker opt-outs**: Remain important for reducing reconnaissance surface, both for you and for family members. Phase 2 should extend opt-out efforts to household members who agree.

---

## Sources and References

**Threat modeling frameworks**:
- [MITRE ATT&CK](https://attack.mitre.org/) — adversary tactics and techniques knowledge base
- [NIST CSF 2.0](https://www.nist.gov/cyberframework) — organizational cybersecurity framework
- [RE&CT Framework](https://atc-project.github.io/atc-react/) — incident response action catalog mapped to ATT&CK
- [Graylog: Using MITRE ATT&CK for Incident Response Playbooks](https://graylog.org/post/using-mitre-attck-for-incident-response-playbooks/)

**Ransomware response**:
- [No More Ransom Project](https://www.nomoreransom.org/) — free decryption tools for known ransomware variants
- [FBI IC3 Ransomware reporting](https://www.ic3.gov/)
- [ACM Digital Threats: Ransomware Response Framework](https://dl.acm.org/doi/full/10.1145/3606022)

**Spyware and surveillance indicators**:
- [Amnesty International MVT Forensic Methodology](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/)
- [iVerify: Pegasus and Predator IOCs](https://iverify.io/blog/key-iocs-for-pegasus-and-predator-spyware-cleaned-with-ios-26-update)
- [Cunicula: AI State Spyware 2026](https://cunicula.com/en/articles/ai-spyware-state-actors-2026)
- [Corrata: Pegasus to DarkSword iOS spyware history](https://corrata.com/pegasus-predator-hermit-spyware-nso-and-its-clones/)
- [foresiet: Pegasus November 2025 surge](https://foresiet.com/blog/pegasus-spyware-november-2025-a-deep-dive-into-shadowy-surge-and-the-global-surveillance-crisis/)

**Insider threat**:
- [CISA Insider Risk Management Program Evaluation](https://www.cisa.gov/sites/default/files/images/IRMPE%20NIST%20CSF%20Crosswalk%20-v1%2010.15.21.pdf)
- [Huntress: Insider Threat Incident Response Plan](https://www.huntress.com/insider-threats-guide/insider-threat-response-plan)
- [Ponemon 2025 Cost of Insider Risks Report](https://deepstrike.io/blog/insider-threat-statistics-2025)

**Supply chain security**:
- [Zscaler ThreatLabz: Supply Chain Attacks Surge March 2026](https://www.zscaler.com/blogs/security-research/supply-chain-attacks-surge-march-2026)
- [ReversingLabs: Software Supply Chain Security Report 2026](https://www.reversinglabs.com/blog/sscs-report-2026-guidance-timeline)
- [Bastion: 2026 Supply Chain Security Report](https://bastion.tech/blog/2026-supply-chain-security-report/)

**Social engineering**:
- [Palo Alto Unit 42: 2025 Global Incident Response Report — Social Engineering Edition](https://unit42.paloaltonetworks.com/2025-unit-42-global-incident-response-report-social-engineering-edition/)
- [AI-Enabled Social Engineering in 2026](https://marklynd.com/articles/ai-enabled-social-engineering-enterprise-2026/)

**Breach notification requirements**:
- [GDPR Article 33 breach notification requirements](https://www.reform.app/blog/gdpr-breach-notification-requirements)
- [PIPEDA Breach Notification — Office of the Privacy Commissioner of Canada](https://www.priv.gc.ca/en/privacy-topics/business-privacy/breaches-and-safeguards/privacy-breaches-at-your-business/gd_pb_201810/)
- [BreachRx: Canada PIPEDA Incident Response](https://www.breachrx.com/global-regulations-data-privacy-laws/canada-pipeda/)
- [Kroll: Integrate Breach Notification and Incident Response](https://www.kroll.com/en/publications/cyber/integrate-breach-notification-incident-response-plan)

**Access Now Digital Security Helpline** (for high-risk individuals needing device forensics referral): [accessnow.org/help](https://www.accessnow.org/help/)
