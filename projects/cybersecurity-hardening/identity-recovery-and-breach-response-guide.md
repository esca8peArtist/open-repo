---
title: "Identity Recovery and Breach Response Guide"
project: cybersecurity-hardening
created: 2026-05-05
status: complete
depends_on: opsec-playbook.md, threat-model.md, operational-security-workflows-guide.md
confidence: high — sourced from FRSecure Compromised Credentials Playbook, CISA Incident Response Playbooks, The Hacker News identity-focused IR guide, Microsoft incident response documentation
---

# Identity Recovery and Breach Response Guide

> **Danger**: Recovery is not always possible. Once a sensitive communication is exposed, exposed contact identities cannot be un-exposed. Once an adversary has established persistent access to a device, clean recovery requires full reinstallation. Prevention is always less costly than recovery. This guide assumes you have already been compromised or are planning for that scenario.

> **Primary warning**: Move quickly. Dwell time — the period between compromise and detection — is the most important variable. Every hour an adversary has active access, they gather more information, expand their foothold, and potentially alert others. The first hour response is more important than any other phase.

---

## Threat Model

**Who this guide is for**: People who have experienced or suspect:
- Account access from an unknown device or location
- Messages they did not send appearing in their accounts
- Device behavior that suggests malware (unexpected outbound connections, battery drain, performance degradation)
- Notification that an associate or contact has been compromised (which may mean your communications with them are visible)
- Legal process (subpoena, warrant) that may have compelled data from a provider

**Assets at stake**: Your accounts, your contacts' safety, your ongoing operations, and potentially your legal exposure if sensitive communications are accessible.

---

## Part 1: Breach Response Playbook

### First Hour: Contain

The goal of the first hour is to stop the bleeding — prevent the adversary from expanding their access or using your compromised identity to harm others.

**Step 1: Disconnect the compromised device from the network**

If you suspect a device is compromised (malware, unauthorized access):
1. Turn off Wi-Fi and mobile data. Do not just disconnect from one network — disable all connectivity.
2. Do not shut down the device yet if you want to preserve forensic evidence (running memory may contain artifacts). If you do not need forensics, shut it down.
3. Do not use the compromised device to attempt recovery — this gives the adversary visibility into your recovery actions.

**Step 2: Alert your most sensitive contacts immediately**

From a clean, uncompromised device:
1. Contact your highest-sensitivity associates via a secure channel that does not depend on the compromised platform.
2. Message: "My [device/account] may be compromised. Do not send sensitive information to [compromised identifier] until further notice. I will contact you on [alternative identifier] to verify."
3. Provide them with an alternative contact method you establish now.

**Reason**: If an adversary has your account, they can impersonate you to your contacts. Alerting contacts quickly reduces the window for adversarial impersonation.

**Step 3: Revoke access tokens and sessions on all affected accounts**

For Google account:
1. From a clean device: `myaccount.google.com` → Security → Your devices → sign out of unknown devices.
2. `myaccount.google.com` → Security → Third-party apps with account access → revoke any you do not recognize.

For Microsoft/Outlook:
1. `account.microsoft.com` → Security → Recent activity → sign out of unknown sessions.

For Signal:
1. Signal → Settings → Linked Devices → review and remove any device you do not recognize.
2. If you suspect account takeover: change your Signal PIN (Settings → Account → Change PIN) and ensure Registration Lock is enabled.

For ProtonMail:
1. `account.proton.me` → Security → Active sessions → terminate unknown sessions.

> **Common pitfall**: Signing in from the compromised device to revoke access. The adversary may see your recovery actions in real time and escalate. Use a clean device.

**Step 4: Change credentials in priority order**

Start with the accounts most likely to cause cascading damage if compromised:
1. Email (highest priority: used for password resets of all other accounts)
2. Password manager
3. Any account linked to financial assets
4. Messaging accounts
5. All other accounts

For each account:
1. Change the password to a new, unique, randomly generated password (via a password manager).
2. Revoke all existing sessions.
3. Update MFA/2FA to a new authenticator code (not SMS if possible — see Part 3 on SMS MFA risks).

---

### First 24 Hours: Assess

**Step 5: Determine the scope of access**

Answer these questions:
- What credentials/data did the adversary have access to?
- What was the time period of access?
- Which accounts and devices were on the same password or linked to the compromised account?

Review account activity logs for the compromised period:
- Google: `myaccount.google.com` → Data & Privacy → My Activity
- ProtonMail: Settings → Security → Authentication Logs
- Signal: does not log access; assess based on device link history

**Step 6: Audit password reuse**

If the compromised credential was used on multiple sites (password reuse), assume all of those accounts are compromised. Change all passwords where the same credential was used.

Use your password manager to identify reused passwords (most password managers have a "Reused passwords" or "Security Checkup" feature).

**Step 7: Identify what was exposed**

For communications (Signal, email, Matrix):
- What messages were accessible during the compromise window?
- Which contacts' identities were visible in those messages?
- What operational plans or information were discussed?

For files:
- Were sensitive documents stored on the device or synced to cloud?
- If cloud-synced, the adversary may still have the files even after you remove device access.

**Step 8: Contact affected parties**

If your contact list, messages, or shared information was exposed:
1. Alert each affected contact with what may have been visible.
2. Let them make their own threat assessment and adjust their posture.
3. Do not minimize the exposure — give them the full picture.

---

### First Week: Recover

**Step 9: Clean device restoration**

If a device was compromised by malware:
1. Do not attempt to "clean" the device — malware can survive standard deletion and even OS reinstalls in some advanced cases. Full drive wipe is required.
2. Boot from external media (USB), wipe the drive completely (not just format), and reinstall the OS.
3. Restore data only from backups made before the suspected compromise date. Restoring from a post-compromise backup may restore the malware.

**Step 10: Secure backup verification**

Before restoring from any backup:
1. Verify the backup is from before the compromise date.
2. If you have reason to suspect the backup is also compromised, restore only non-executable data (documents, photos) — not installed applications or system files.

**Step 11: Establish clean identity channels**

After a significant compromise:
1. Create new accounts on new infrastructure (new email address, new Signal registration on a new number).
2. Migrate contacts to the new channels by contacting them directly over a pre-established secure channel.
3. Do not simply recover the old account — if the adversary has established persistent access mechanisms (OAuth tokens, authorized apps), the old account infrastructure may be permanently compromised.

---

## Part 2: Account Recovery Procedures

### Backup Codes

Most MFA systems provide backup codes at setup. These codes allow access to an account if you lose your authenticator device.

**Where to store backup codes**:
- Printed and stored in a physically secure location (not in the same location as your device)
- In an encrypted password manager backup stored offline
- In a password manager on a separate device from your primary one

**Never store backup codes**:
- In your email inbox (if email is compromised, so are your backup codes)
- In a photo on your phone (if phone is compromised, so are your codes)
- In a cloud note service that is not end-to-end encrypted

> **Critical**: Backup codes are single-use in most systems. When you use one, it is spent. Generate new backup codes after any security event.

### Bitwarden / Password Manager Recovery

If your password manager account is compromised or you lose access:
1. Bitwarden allows you to export your vault at any time to an encrypted file. Do this regularly (monthly) and store the export offline.
2. If you lose your master password, there is no Bitwarden recovery without an emergency access contact. Set up an emergency access contact with a trusted person: `vault.bitwarden.com` → Settings → Emergency Access → Invite someone.
3. If the password manager is compromised, change all stored passwords systematically — this will take time, prioritize by sensitivity.

### Signal Registration Lock Recovery

If you forget your Signal Registration Lock PIN:
- You must wait 7 days before Signal allows re-registration.
- During this window, your phone number cannot be registered to a new Signal account.
- After 7 days, you can register again (losing your message history, but recovering account control).
- For this reason, enable Registration Lock only with a PIN you will remember (or store in a password manager).

### ProtonMail Recovery

If you lose access to a ProtonMail account:
1. ProtonMail allows setting a recovery email and recovery phone at `account.proton.me` → Security → Recovery.
2. For users who chose not to set recovery contact (to prevent linkage to identity): there is no account recovery. This is by design — zero-knowledge means Proton cannot decrypt your account without your password.
3. Decision point: if you are using ProtonMail for high-sensitivity communications where account recovery must not be linkable to your identity, accept that you may permanently lose the account if you forget credentials. Use a password manager.

---

## Part 3: Prevention — What Makes Breach Response Easier

### Multi-Factor Authentication

MFA substantially reduces the risk of account takeover from stolen passwords. The implementation matters:

**Preferred MFA options** (most secure first):
1. **Hardware security key** (YubiKey, Google Titan): physical key required for login. Cannot be phished. The attacker needs the physical key.
2. **TOTP authenticator app** (Aegis on Android, Raivo on iOS): generates time-based one-time codes. Cannot be intercepted over the air. Resistant to real-time phishing but not to sophisticated social engineering.
3. **Email verification code**: acceptable if the email account itself is secured with stronger MFA.
4. **SMS one-time code**: the weakest MFA option. SIM swapping attacks (convincing your carrier to transfer your number to an attacker's SIM) bypass SMS MFA entirely. Law enforcement can obtain SMS codes via carrier cooperation. Use SMS MFA only if nothing better is available.

> **Danger**: SMS-based MFA is significantly weaker than app-based MFA. In high-risk threat models (where law enforcement access to carriers is a real concern), SMS MFA provides minimal protection. However, SMS MFA is still better than no MFA.

**Set up Aegis (Android TOTP authenticator)**:
1. Install Aegis from F-Droid or Google Play.
2. During initial setup, create a backup password for your Aegis vault.
3. Export your Aegis vault periodically (backup encrypted JSON file) and store offline.
4. Add accounts: in Aegis → "+" → scan QR code from your account's MFA setup page.

### Password Hygiene

- Every account must have a unique password. Password reuse is the most common cause of cascading breaches.
- Passwords must be random and long (20+ characters minimum). A password manager generates and stores these.
- **Recommended password managers**: Bitwarden (open source, self-hostable), KeePassXC (local-only, no cloud sync, highest security).

### Regular Backup Cadence

Recovery requires clean backups. Without them, you cannot determine the pre-compromise state.

**Backup schedule**:
- Device data: weekly encrypted backup to external drive
- Password manager vault: monthly export to encrypted file, stored offline
- Recovery codes: as generated (usually only once at account creation — do not lose them)
- Sensitive documents: as created, with encrypted offline copies

**Verify restorability**: A backup you cannot restore from is not a backup. Test restoring from your backup at least once per year.

---

## Part 4: Recovery Checklists

### Hour-by-Hour Response

**First Hour**:
- [ ] Disconnect compromised device from all networks
- [ ] Alert highest-sensitivity contacts from clean device
- [ ] Revoke sessions on affected accounts (email, password manager)
- [ ] Change email password (prioritized — this controls password reset for everything else)
- [ ] Change password manager master password
- [ ] Enable or reset MFA on email and password manager

**Hours 2–4**:
- [ ] Review account activity logs for the compromise period
- [ ] Change passwords on all accounts that shared credentials with the compromised one
- [ ] Revoke third-party app authorizations on all major accounts
- [ ] Review linked devices on Signal and Matrix
- [ ] Check for unauthorized password reset attempts on other accounts

**Day 1**:
- [ ] Scope fully documented: which accounts, which data, which time period
- [ ] All contacts whose information was exposed have been notified
- [ ] New contact channel established if old one is compromised
- [ ] Compromised device isolated, not used
- [ ] Incident documented for your own records (what happened, when, what you did)

**Week 1**:
- [ ] Compromised device wiped and OS reinstalled (or disposed of)
- [ ] Data restored only from pre-compromise backups
- [ ] All accounts migrated to new, unique credentials
- [ ] MFA enabled on all accounts that support it
- [ ] Backup strategy reviewed and updated
- [ ] Recovery codes regenerated and stored securely

**Month 1**:
- [ ] Ongoing monitoring: check `haveibeenpwned.com` for new breach notifications
- [ ] Review what operational changes prevented/would have prevented the breach
- [ ] Update threat model based on what you learned
- [ ] Security audit of remaining practices

---

### Contact Notification Template

When alerting contacts about a potential compromise, use a pre-agreed out-of-band channel to send this:

```
[Your pseudonym or name they know you by],

I need to let you know: [my Signal account / my device / my email account] may have been compromised [on or around date/time].

During this period, the following may have been accessible:
- [Our messages between date A and date B]
- [My contact list / your contact information]

Please:
1. Do not send sensitive information to [compromised identifier] until I confirm recovery
2. Review whether our recent communications contain anything that affects your safety
3. I will reach you at [new contact method] to confirm this message is from me

I will send you a verification [word / signal / method you previously agreed on].

Take care.
```

> **Note**: The verification step (pre-agreed word or signal) is essential. An adversary in control of your account can send this same message to perform a social engineering attack. A pre-agreed verification code or phrase confirms the recovery message is authentic.

---

## Part 5: Hardening Specifically to Minimize Breach Impact

These measures reduce what an adversary can access if a breach occurs.

**Minimize stored data**: The less sensitive information on your devices and accounts, the less damage a breach causes.
- Disappearing messages in Signal reduce the historical record
- Do not store sensitive documents in cloud services that are not end-to-end encrypted
- Regularly purge messages, files, and accounts you no longer need

**Compartmentalization limits blast radius**: If you follow the compartmentalization practices in the OPSEC workflows guide, a breach of one compartment cannot access others.

**Offline-only sensitive storage**: Truly sensitive files (keys, identities, operational plans) stored offline — on an encrypted USB drive that is not connected to a networked device — cannot be accessed remotely even if all your networked accounts are compromised.

**Forward secrecy in messaging**: Signal and Matrix both use forward secrecy. This means that even if a session key is compromised in the future, past messages cannot be retroactively decrypted. This is why keeping Signal updated matters — protocol improvements only protect you if you are running current software.

---

## Recovery and Breach Response Security Checklist

**Prevention (do these now)**:
- [ ] Unique, randomly generated password for every account (stored in password manager)
- [ ] Password manager vault exported monthly and stored offline
- [ ] TOTP authenticator (Aegis/Raivo) enabled on all important accounts
- [ ] SMS MFA replaced with TOTP wherever possible
- [ ] Backup codes generated and stored offline (not in email)
- [ ] Signal Registration Lock PIN stored in password manager
- [ ] Recovery contacts set up in password manager
- [ ] Regular offline device backups (weekly)
- [ ] Pre-agreed out-of-band contact method and verification code established with key contacts

**If breach suspected**:
- [ ] Compromised device isolated
- [ ] Key contacts alerted from clean device
- [ ] Email password changed (first priority)
- [ ] All sessions revoked on affected accounts
- [ ] Breach scope documented

**Recovery verification**:
- [ ] New credentials do not repeat any previous passwords
- [ ] New MFA enrolled on all accounts
- [ ] Clean backup restoration tested
- [ ] Contacts confirmed via verification code that new channel is authentic

---

## Troubleshooting

**Problem**: I cannot access my email to reset other passwords because email itself is compromised.
**Solution**: If you have set up a recovery phone number with your email provider, use SMS recovery (weakest but available). If you set up a recovery email, use that. If neither: contact the provider's support directly — Google, Microsoft, and Proton all have account recovery procedures for when email access is fully lost. These procedures are slower (days) and may require identity verification.

**Problem**: I was compromised, changed all passwords, but keep seeing unauthorized access.
**Solution**: Persistent unauthorized access after credential changes usually indicates a compromised device (malware that logs new passwords as you set them) or a still-active OAuth token you did not revoke. Review all third-party app authorizations on major accounts. Wipe and reinstall the device you used to change passwords if compromise is suspected.

**Problem**: My Signal contacts are receiving messages from me that I did not send.
**Solution**: Unauthorized device linked to your account. Immediately: Settings → Linked Devices → remove all devices → re-link only your own device. Change your Signal PIN and enable Registration Lock. Alert all recent contacts that messages from the compromised period should be treated as potentially adversarial.

**Problem**: I set up a recovery email but it was also compromised.
**Solution**: This is a cascading recovery failure. Contact your primary email provider's support directly. Most providers have a manual identity verification process for account recovery when all automated methods fail. This takes days and is degrading — it underscores why recovery methods must be on separate channels.

---

## Sources

- [FRSecure: Compromised Credentials Response Playbook](https://frsecure.com/compromised-credentials-response-playbook/)
- [The Hacker News: Identity-Focused Incident Response Playbook](https://thehackernews.com/2024/09/from-breach-to-recovery-designing.html)
- [CISA: Federal Government Cybersecurity Incident Response Playbooks](https://www.cisa.gov/sites/default/files/2024-08/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf)
- [Microsoft: Incident Response — Compromised and Malicious Apps](https://learn.microsoft.com/en-us/security/operations/incident-response-playbook-compromised-malicious-app)
- [Have I Been Pwned — Breach Notification Service](https://haveibeenpwned.com)
- [Privacy Guides: Multi-Factor Authentication](https://www.privacyguides.org/en/multi-factor-authentication/)
- [EFF: Security Self-Defense — Creating Strong Passwords](https://ssd.eff.org/module/creating-strong-passwords)
