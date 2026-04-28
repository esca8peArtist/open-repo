---
title: "Immigration Attorney & Legal Aid Worker Implementation Guide"
project: cybersecurity-hardening
created: 2026-04-28
status: complete
audience: immigration attorneys, legal aid workers, paralegals, law clinic staff
tier: 1–2
depends_on: device-hardening-guide.md, opsec-playbook.md, palantir-threat-model.md
---

# Immigration Attorney & Legal Aid Worker Implementation Guide

## Your Threat Model

Your clients are tracked by ICE's ELITE platform — a Palantir tool that scores address confidence for each deportation target using IRS records, Medicaid data, DMV records, utility bills, and commercial data brokers. The score updates near-real-time: a client who opens a new utility account can have their address refreshed within days. Your communications, case files, and contact information are all conduit vectors.

The threat is not primarily that you are a target — it is that you are a conduit. A subpoena to your firm seeks address information, contact history, and family associations ICE may not already have. Attorney-client privilege is a legal defense but does not prevent process from being initiated or servers from being seized pending litigation. At any port of entry, CBP can search devices without a warrant: a laptop with client files at a border crossing is a client file at risk.

A secondary threat is your clients' devices. Smartphone apps with advertising SDKs harvest GPS location and sell it to ICE via commercial broker contracts. Advising a client to contact you via Gmail while their Android has ad-SDK tracking active may generate a metadata record connecting you to them in the commercial broker ecosystem.

---

## Week 1: Essential Baseline

**1. Move client communications to Signal**
Install Signal ([signal.org](https://signal.org)). A subpoena to Signal returns only account creation date and last connection time — it stores nothing else. Configure: Settings → Privacy → Disappearing Messages → Default Timer → 1 Week. If clients cannot use Signal, ProtonMail (Step 4) is the backup.

**2. Assess client Signal safety**
Signal protects content regardless of the client's device. It cannot protect metadata (that a Signal message was sent from your number at a given time). For highest-risk clients: instruct them to use a secondary MySudo number ([getsudo.com](https://getsudo.com)) for the contact before sharing yours.

**3. Enable Advanced Data Protection**
Settings → [your name] → iCloud → Advanced Data Protection → Turn On. Apple cannot hand over this data under a warrant. Store your recovery key physically in your office safe — not in email or cloud notes.

**4. Create a ProtonMail account for client email**
Create a Proton account at [proton.me](https://proton.me) with a username that does not include your client's name. Proton cannot comply with subpoenas for email content — it cannot decrypt it. Proton-to-Proton email encrypts content and subject lines end-to-end. Email to Gmail/Outlook is not end-to-end encrypted even from Proton.

**5. Enable full-disk encryption on your laptop**
macOS: System Settings → Privacy & Security → FileVault → Turn On. Store recovery key yourself (not with Apple). A powered-off, encrypted laptop cannot be forensically read at a border crossing without your password.

**6. Audit cloud services holding client data**
Is client data in Dropbox, Google Drive, or Box? These comply routinely with U.S. legal process. Move case files to encrypted local storage or a Swiss-jurisdiction provider: Tresorit ([tresorit.com](https://tresorit.com)) requires a Swiss court order for access — a significant barrier compared to a U.S. subpoena to Google. Verify your case management system's cloud hosting and legal process policy.

**7. Configure PIN unlock, disable biometrics**
Law enforcement can compel biometric unlock but generally cannot compel a memorized PIN under the Fifth Amendment. Settings → Face ID & Passcode → disable Face ID for iPhone Unlock. Emergency shortcut if approached: hold side + volume down to disable Face ID temporarily.

---

## Month 1: Intermediate Hardening

**1. Establish a border-crossing protocol**
Do not cross borders with client files on your device unless unavoidable. For travel with files: power off completely before the checkpoint (enters BFU state). If ordered to unlock: you may decline; the device may be seized. Request Form 6051D. If returned, factory-reset before client work. For travel without sensitive files: back up locally, factory-reset before travel, restore after. Full protocol in `device-hardening-guide.md` Section 1.7.

**2. Advise clients on social media**
ImmigrationOS includes automated OSINT and real-time social media monitoring; Babel Street holds government contracts for the same. Advise every client: review all public posts for location, associations, or case details. Set all accounts to maximum privacy. Ideally, separate public-facing accounts from private messaging accounts.

**3. Set up secure file transfer**
Use OnionShare ([onionshare.org](https://onionshare.org)) for case documents: creates a temporary .onion address over Tor, no central server, nothing to subpoena. Documents emailed via Gmail pass through Google's servers, which comply routinely with legal process.

**4. Enable Mullvad VPN**
[mullvad.net](https://mullvad.net) ($5/month, no identifying information required). Enable before any sensitive research — immigration databases, court filings, client lookups. ISP records are accessible via NSL without a warrant. Mullvad has a court-verified no-log policy.

**5. Replace SMS two-factor authentication**
Install Ente Auth (iOS/Android, open-source, stored locally) and migrate every account's 2FA to it. SMS 2FA is vulnerable to SIM swapping — an attacker who transfers your carrier number can intercept 2FA codes and take over every SMS-protected account.

**6. Establish a client communication protocol**
Most clients will not set up sophisticated tools. Document a tiered baseline your whole organization follows: Signal (preferred) → WhatsApp (better than SMS; Facebook retains metadata) → ProtonMail (for clients without smartphones, with instruction not to access it from shared computers) → Never: case details in SMS, unencrypted email, or phone unless no alternative exists.

**7. Data broker opt-outs for your organization**
Submit your organization's address to LexisNexis opt-out at [optout.lexisnexis.com](https://optout.lexisnexis.com) (LexisNexis holds a $9.75M DHS contract giving ICE database access). Opt out staff names and phones from Spokeo, BeenVerified, and WhitePages following `implementation-guide.md` Part 0. This degrades ICE's ability to identify staff as points of contact through OSINT.

---

## Month 3: Advanced Mastery

**1. Establish a secure client intake channel**
Set up a MySudo number ([getsudo.com](https://getsudo.com)) as your client-facing contact point. New clients reach this VoIP number first; your primary carrier number — accessible in carrier records without a warrant — does not appear in clients' call history.

**2. Implement need-to-know case file access**
A single law enforcement data pull against anyone with full database access can expose every client. Implement role-based access: paralegals see only assigned cases, attorneys see only their files, one administrator has full access. This limits the blast radius of any single account compromise or legal process.

**3. Tails OS for highest-risk case work**
For clients facing active deportation enforcement, use Tails OS ([tails.net](https://tails.net)) for case documentation. Tails runs entirely in RAM from a USB drive and leaves no trace on host hardware — if the device is seized, case files handled in Tails cannot be recovered.

**4. Establish organizational incident response protocols**
Identify digital rights counsel before a crisis: NLG ([nlg.org](https://nlg.org)), EFF ([eff.org](https://eff.org)). Create a written plan: who is notified if a device is seized, which clients are at immediate risk if a particular file is exposed, and what communication is required within the organization.

**5. Advise clients on data broker opt-outs**
ELITE's address confidence scores pull from commercial brokers — opt-outs degrade those scores. Walk clients through LexisNexis opt-out at [optout.lexisnexis.com](https://optout.lexisnexis.com). California residents should use DROP at [privacy.ca.gov/drop](https://privacy.ca.gov/drop). Clients should submit opt-outs from a library computer, not from their home IP (which would confirm their current address before the opt-out processes).

---

## Common Mistakes and How to Avoid Them

**Keeping client files in U.S.-based cloud storage.** Google Drive, Dropbox, and Box comply routinely with U.S. legal process. Your client files can be compelled without you being served. Move sensitive files to encrypted local storage or a Swiss provider before a crisis — not after.

**Using the same communication channel for all clients regardless of risk level.** A client with an open deportation order has different requirements than one filing a routine visa renewal. Highest-risk clients warrant Signal with disappearing messages and a dedicated intake number. Treating every client identically creates vulnerabilities at the high end.

**Assuming clients know how to use the tools you recommend.** Installing Signal means nothing if the client backs up their phone to iCloud (where screenshots of your conversations might live). Walk every client through the specific configuration steps in their language and document that you did so.

---

## Verification Checklist

- [ ] Advanced Data Protection: Settings → [name] → iCloud → confirms "Advanced Data Protection: On"
- [ ] FileVault: macOS terminal → `fdesetup status` → returns "FileVault is On"
- [ ] Signal disappearing messages: Open a test conversation → tap name → Disappearing Messages → confirm timer is set
- [ ] Signal username: Settings → Profile → confirms @ username, not phone number visible
- [ ] Client file cloud audit: list every location where a client file exists. Confirm each one is either encrypted locally or on a non-U.S.-cloud provider
- [ ] 2FA migration: log into Proton and three other sensitive accounts, confirm 2FA is via authenticator app (not SMS)
- [ ] VPN active: at mullvad.net/check, confirm "You are connected to Mullvad"
- [ ] Border protocol: confirm you have a written procedure for what happens when crossing a border with work devices

---

## References

This guide distills from the following documents in this repository:
- `device-hardening-guide.md` — complete iOS/Android hardening with technical detail
- `opsec-playbook.md` — full countermeasure mapping by tier
- `implementation-guide.md` — step-by-step setup instructions, including data broker opt-outs
- `palantir-threat-model.md` — ICE contracts, ELITE data sources, and ImmigrationOS capabilities

For legal support: [National Lawyers Guild](https://nlg.org), [EFF](https://eff.org), [ACLU](https://aclu.org)
