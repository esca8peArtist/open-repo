# User Operational Security Manual
**For Safe Execution of Resistance-Research Phase 1 Distribution & Cybersecurity-Hardening Deployment**

**Created**: 2026-05-09 06:10 UTC  
**Scope**: Practical operational security guidance for you (the user) while executing Phase 1 distribution  
**Status**: Ready for use during Phase 1 and Phase 2 distribution (May 2026 onwards)

---

## Executive Summary

**Why this matters**: Distributing materials about surveillance threats, democratic vulnerability, and government overreach creates operational security risks for *you*. Your email metadata, device, network, and patterns become observable to the same agencies/capabilities you're documenting. This manual provides practical, implementable protections without requiring advanced technical skills.

**What this is NOT**: This is not paranoia or security theater. This is threat modeling grounded in documented capabilities (FISA 702, NSL metadata, subpoena authority, DHS surveillance tools) and realistic risk assessment (you're not a state-level target, but network operators and federal agencies monitor activist distribution).

**What this IS**: Practical daily behaviors (email routing, device hygiene, communication channels) that significantly reduce the observable surface area of your work.

**Reading time**: 15 minutes  
**Implementation time**: 2-4 hours (one-time setup); 5-10 min/day (ongoing habits)

---

## Part 1: Threat Assessment (What Could Happen)

### 1a. Low-Risk Scenarios (Likelihood: Medium, Impact: Low)

**Scenario 1: Email monitoring**
- **What**: ISP, email provider, or network operator logs your Phase 1 outreach emails (recipient lists, subject lines, timestamps)
- **Who**: ISP infrastructure; email provider (Gmail, Proton, etc.); network admin if you're on institutional WiFi
- **Impact**: They know you're contacting organizations about democratic renewal; they know which organizations you're reaching (from email addresses visible in metadata)
- **Legal basis**: ISP and email provider TOS (lawful but data-minimizing with encryption); government could obtain via subpoena

**Scenario 2: Contact list compromise**
- **What**: Your local contact list (spreadsheet, email client) becomes visible to unauthorized person
- **Who**: Someone with device access (physically nearby, remote compromise), accidental exposure (email forwarded to wrong person)
- **Impact**: 150+ organizational contacts and their contact info becomes known; downstream organizations could be contacted impersonating you
- **Legal basis**: Theft, breach, or accident — no legal authority needed

**Scenario 3: Response tracking via email opens**
- **What**: Mailtrack or similar email tracking tool reveals which contacts opened your emails and when
- **Who**: Anyone with access to your Mailtrack account (weak password, shared device, account breach)
- **Impact**: Granular engagement data on 150+ organizations becomes observable; an attacker could see which organizations engaged most
- **Legal basis**: Mailtrack ToS; no government authority, but private company data

### 1b. Medium-Risk Scenarios (Likelihood: Low, Impact: Medium)

**Scenario 4: Email account compromise**
- **What**: Someone gains access to your email account (password breach, phishing, SIM swap)
- **Who**: Attacker with common attack tools (credential stuffing, phishing); sophisticated adversary via 2FA compromise
- **Impact**: All your Phase 1 emails, responses, and internal notes become readable; attacker could send emails impersonating you
- **Legal basis**: Unauthorized access (federal crime if interstate); government could obtain via warrant

**Scenario 5: Subpoena of email archives and metadata**
- **What**: Federal grand jury or civil litigation subpoenas your email provider for all emails matching keywords (e.g., "Phase 1", "distribution", contact names)
- **Who**: DOJ grand jury (criminal investigation); plaintiff's counsel (civil litigation); investigative agency (FBI, DHS)
- **Impact**: Email provider produces all matching emails + metadata (recipients, send times, read receipts); complete Phase 1 distribution and response logs become visible
- **Legal basis**: Federal subpoena power; warrant not required for content <180 days old under SCA

**Scenario 6: Device compromise**
- **What**: Malware on your computer intercepts Phase 1 emails before encryption; spyware logs keyboard (capturing email passwords, response drafts)
- **Who**: Sophisticated attacker (nation-state, well-funded criminal); compromise vector: email attachment, software download, 0-day
- **Impact**: All Phase 1 and Phase 2 work becomes observable before encryption; attacker can see drafts, research, coordination, responses
- **Legal basis**: Unauthorized access; government could deploy via warrant or COINTELPRO-style operation

### 1c. High-Risk Scenarios (Likelihood: Very Low, Impact: High)

**Scenario 7: Participant or infiltrator becomes hostile**
- **What**: Someone you're coordinating with on Phase 2 implementation becomes an informant or hostile actor; they provide all your communications to law enforcement or a political adversary
- **Who**: Participant with legitimate access; motivated by coercion (threatened prosecution), ideology, or financial incentive
- **Impact**: All Phase 2 coordination, strategy, and implementation plans become known; your relationships and communications with partner organizations become visible
- **Legal basis**: No legal authority needed; they're sharing information they already have

**Scenario 8: Government investigation of "misinformation" or "election interference"**
- **What**: DOJ opens investigation into your Phase 1/2 activities framed as coordinated misinformation, election interference, or COINTELPRO-adjacent
- **Who**: FBI, DOJ, state law enforcement; political motivation likely (your material contradicts official narratives)
- **Impact**: Subpoenas issued for all devices, email, communications; interviews/pressure on organizations you've contacted; potential charges (conspiracy, wire fraud, etc. — unlikely to stick but chilling effect is the goal)
- **Legal basis**: Government can investigate; subpoena authority; (baseless charges unlikely to prosecute but chilling effect is the goal)

---

## Part 2: Risk Mitigation Checklist (Implementation)

### Tier 1 Mitigations (High Impact, Low Cost, Do First)

**Mitigation 1: Email Separation Strategy**

**Rationale**: Keeps Phase 1 distribution separate from your personal/work email; if one email account is compromised, the other remains secure.

**Action**:
1. Create a new Gmail or Proton Mail account specifically for Phase 1/2 distribution work
   - If using Gmail: Enable 2FA immediately (phone + backup codes)
   - If using Proton: Use their encrypted email service; enables zero-knowledge storage
   - **Important**: Use a strong, unique password (20+ characters, mix of symbols/numbers/letters)

2. Create a separate password manager entry for this account
   - Password manager: Bitwarden (open source) or 1Password (commercial)
   - Store backup codes for 2FA in the password manager (encrypted)

3. Use this distribution email ONLY for Phase 1/2 outreach; do NOT use it for personal mail, work, or other projects

4. Contacts see distribution email in "From:" field but cannot reply-all to compromise your personal email

**Implementation time**: 15 minutes  
**Ongoing cost**: <1 minute/day (checking account)

---

**Mitigation 2: Disable Email Tracking on Phase 1 Emails**

**Rationale**: Mailtrack and similar tools reveal which organizations engaged with your materials and when. Instead of tracking, accept that you won't know who opened your emails.

**Action**:
1. Do NOT use Mailtrack, HubSpot, or similar email tracking tools for Phase 1 distribution
2. Instead, use spreadsheet-based tracking: organizations who respond are added to a "responses" column
3. This way, you only know about engagement that generates actual contact (replies, calls)
4. If you want metrics: track open/engagement based on response rate, not pixel tracking

**Why**: Email tracking pixels can be:
- Logged by your email provider, ISP, or network operator
- Subpoenaed in litigation
- Used to build a profile of which organizations you're interested in

**Implementation time**: 0 minutes (don't use tracking tool)  
**Ongoing benefit**: Removes trackable metadata from Phase 1

---

**Mitigation 3: Contact List Encryption & Backup**

**Rationale**: Your 150+ contact list is a high-value target. If your device is lost, stolen, or breached, encryption ensures it remains unreadable.

**Action**:
1. Store contact list in an encrypted format:
   - **Option A** (Simple): Password-protected Excel/Google Sheet
     - Google Sheets: File → Properties → encrypt with password
     - Excel: File → Info → Protect Workbook → Encrypt with Password
   - **Option B** (Better): Bitwarden password manager (stores contacts with each entry)
   - **Option C** (Best): Encrypted flash drive using VeraCrypt (full-disk encryption portable)

2. Never store contact list as an unencrypted CSV or plain text document
3. Backup encrypted contact list to:
   - Personal encrypted cloud storage (ProtonDrive, Tresorit, Sync.com)
   - NOT to Dropbox, Google Drive, or OneDrive (unencrypted by default)

4. Test your encryption: close the encrypted file; verify you can't read it without password
5. Test your backup: verify you can decrypt and restore from backup

**Implementation time**: 20 minutes  
**Ongoing time**: 1-2 minutes/week to back up updated contact list

---

**Mitigation 4: Device & Network Hygiene**

**Rationale**: Malware or network monitoring can compromise your Phase 1 work before encryption.

**Action**:
1. **Device security**:
   - [ ] All devices you use for Phase 1: enable automatic updates (OS + security patches)
   - [ ] Install reputable antivirus (Windows Defender on Windows; built-in on Mac/Linux)
   - [ ] Disable unnecessary auto-run, USB auto-mount, and file sharing features
   - [ ] Review device software: uninstall anything you don't use regularly (reduces attack surface)

2. **Network security**:
   - [ ] Do NOT use public WiFi for Phase 1 email/communication
   - [ ] If using public WiFi: use VPN (Mullvad, ProtonVPN, or Wireguard) + HTTPS-only browsing
   - [ ] At home: secure WiFi with strong password (20+ chars); update router firmware
   - [ ] If on institutional network: use VPN to tunnel traffic (prevents network admin observation)

3. **Password managers**:
   - [ ] If using cloud password manager (Bitwarden, 1Password): ensure master password is strong (20+ chars, random)
   - [ ] Use unique passwords for each account (password manager generates them)
   - [ ] Enable 2FA on password manager account

**Implementation time**: 1-2 hours (initial setup); 10 min/month (updates)

---

### Tier 2 Mitigations (Medium Impact, Medium Cost, Do After Tier 1)

**Mitigation 5: Email Encryption (End-to-End)**

**Rationale**: Encrypts email content so only the recipient (and you) can read it. Prevents ISP, email provider, and network monitoring from reading message content.

**How it works**: You encrypt the email before sending; recipient must have the decryption key to read it.

**Action**:
1. **Option A (Simple, Limited)**: PGP/GPG encryption
   - Works best if recipients also use PGP (many security-conscious organizations do)
   - Generates a key pair (public key for encryption, private key for decryption)
   - Tool: GnuPG (free, open source)
   - Learning curve: Moderate (3-4 hours to set up)

2. **Option B (Better, More Practical)**: Use Proton Mail as your distribution email
   - Proton Mail encrypts all emails by default (between two Proton accounts)
   - Non-Proton recipients can open via password-protected link
   - No setup required beyond using Proton instead of Gmail

3. **Option C (Most Practical)**: Secure collaboration platform
   - Use a private, encrypted workspace for Phase 1/2 coordination
   - Tool: Slack (encrypted); ProtonDocs (encrypted collaborative docs); Signal (for group chat)
   - Trade-off: Requires participants to join your workspace, not just email

**Recommendation**: Start with Option B (Proton Mail for distribution email). PGP (Option A) if recipients request it.

**Implementation time**: 15 minutes (switch to Proton) or 3-4 hours (set up PGP)

---

**Mitigation 6: Communication Compartmentalization**

**Rationale**: If one communication channel is compromised, others remain secure. Separates Phase 1 distribution (low-sensitivity outreach) from Phase 2 coordination (sensitive strategy).

**Action**:
1. **Phase 1 (Distribution) — Email**:
   - Use distribution email account for all Batch 1-5 outreach
   - Mass messages; semi-public framework
   - Channel: Standard encrypted email (Proton Mail)

2. **Phase 2 (Coordination) — Encrypted Group**:
   - Organizations expressing implementation interest → invite to encrypted workspace
   - Actual strategy, timeline, organizational partnerships → discussed only in encrypted group
   - Channel: Signal (group chat), ProtonMail (encrypted email thread per partner), or private Slack workspace

3. **Personal/Work — Separate Email**:
   - Personal email account for non-Phase 1/2 work
   - Keep completely separate from distribution email
   - If personal email is compromised, Phase 1 remains unaffected

4. **Document Collaboration**:
   - Public documents (proposal, executive summary): GitHub Gist (public, but no personal data)
   - Internal strategy docs (campaign timeline, contact strategy): encrypted Google Doc or ProtonDocs (password-protected, shared link)
   - Never store strategy docs in unencrypted Dropbox, Drive, or OneDrive

**Implementation time**: 1 hour to set up Signal groups, Proton workspace, encrypted doc sharing

---

**Mitigation 7: Metadata Minimization**

**Rationale**: Even if email content is encrypted, metadata (who you're emailing, when, how often) reveals patterns. Minimize this metadata.

**Action**:
1. **Email patterns**:
   - Don't send all Phase 1 emails in one hour (creates obvious batch pattern)
   - Space sends across 2-3 hours (as execution playbook already recommends)
   - Vary send times day-to-day (if Day 1 is 9am, don't send Day 2 emails all at 9am)
   - Vary send frequency (don't email exactly 5 contacts per day every day)

2. **Device patterns**:
   - Don't always access distribution email from same device at same time
   - Occasional access from home WiFi, work, phone, cafe WiFi (if using VPN)
   - Reduces ability to locate you via device fingerprinting

3. **Network patterns**:
   - If always on same WiFi when doing Phase 1 work, VPN usage becomes identifiable pattern
   - Occasional work from different networks to avoid obvious pattern
   - (This is low-priority; other mitigations are higher impact)

**Implementation time**: 0 minutes (already built into execution playbook); 1 minute/day awareness

---

### Tier 3 Mitigations (Lower Impact, Higher Cost, Do If High-Risk)

**Mitigation 8: Decentralized Coordination & Operational Security Compartments**

**Rationale**: If you're coordinating with multiple organizations on Phase 2, compartmentalization limits the damage if one organization's communications are compromised.

**Action**:
1. Organize Phase 2 implementation into independent "cells":
   - Law school adoption → separate Signal group (you + interested law school contacts)
   - Labor organization implementation → separate Signal group (you + interested labor contacts)
   - Election protection partnership → separate Signal group (you + election organizations)

2. You're the only person in all groups; no single group knows about other groups' coordination
3. If one group's communications are compromised, other groups remain unaffected
4. Information flows "up" from groups to you, not across groups

**Why this works**: COINTELPRO and other surveillance operations reveal themselves when they try to map all relationships. Compartmentalization prevents full network visibility.

**Downside**: Higher overhead (you manage 3-5 separate conversations); less coordination across groups

**Implementation time**: 15 minutes per group setup; 1-2 hours/week management

---

**Mitigation 9: Offline Document Backup & Dead-Man's Switch**

**Rationale**: If government seizes your devices/accounts, having offline backups ensures your work survives. Dead-man's switch notifies trusted parties if you stop checking in.

**Action**:
1. **Offline backup**:
   - Print key Phase 1/2 documents (proposal, implementation roadmap) and store in secure location (safe deposit box, trusted friend's house)
   - Encrypted flash drive with complete Phase 1/2 files, stored offline
   - Password/decryption key stored separately (not on backup device)

2. **Dead-man's switch** (if doing sensitive Phase 2 work):
   - Set up automated message: "If you don't hear from me by [date], release [document]"
   - Tools: Dead Man's Switch (automatic email), or simple Google Form to trusted friend: "Have you heard from [your name] in the last 7 days?"
   - Define what "silence" means: if you don't log in for 7 days, trigger the switch

3. **Document for sealed envelope**:
   - Prepare a document explaining Phase 1/2 work, key contacts, and why it matters
   - Sealed envelope with dead-man's switch friend
   - Only opened if you go missing or communications are seized

**Implementation time**: 2-3 hours (initial setup); 5 minutes/week (checking in with dead-man's switch)  
**Cost**: Safe deposit box (~$50-200/year) or trusted friend's time

---

**Mitigation 10: Legal & Operational Insurance**

**Rationale**: If you're investigated or sued, having a plan for legal representation significantly improves outcomes.

**Action**:
1. **Identify a civil rights attorney NOW** (before you need one):
   - Who specializes in government investigation defense and COINTELPRO-adjacent cases
   - Examples: ACLU local chapter, National Lawyers Guild, CRAG (Center for Racial Justice), local civil rights firm
   - Contact them: brief exploratory call ("I'm working on democratic reform materials and want to understand my legal exposure")
   - Ask: "If I'm investigated or subpoenaed, how should I respond?" and "Do you offer phone consults?"

2. **Establish "retainer" or "on-call" arrangement**:
   - Some attorneys offer reduced rates for "available when needed"
   - Not full retainer, but a standing agreement they'll take your case if contacted
   - Cost: $0-2,000 depending on attorney

3. **Understand your legal rights**:
   - You have the right to refuse FBI interviews without a lawyer
   - You have the right to refuse searches without a warrant
   - You have rights against self-incrimination (5th Amendment)
   - Attorney can protect these rights for you

4. **Document your intentions**:
   - Keep a record: "Phase 1 distribution of democratic renewal proposal is lawful civic speech; goal is to reach 150+ organizations with policy ideas"
   - This prevents framing as "conspiracy" or "misinformation campaign"
   - Attorney can advise what documentation protects you

**Implementation time**: 2-3 hours (finding attorney, initial call); 1 hour/year (refresher call)  
**Cost**: $0-3,000 (depends on attorney and whether you need actual representation)

---

## Part 3: Daily Habits for Operational Security

### Morning Habit (2 minutes)
- [ ] Update contact spreadsheet backups (if you added new responses)
- [ ] Review encrypted email inbox for any urgent communications
- [ ] Confirm no unusual device activity (check device logs for logins, antivirus status)

### Weekly Habit (10 minutes)
- [ ] Back up encrypted contact list to secure cloud storage
- [ ] Review email for any suspicious phishing attempts or unusual communications
- [ ] Check password manager for any compromised passwords (tools like Have I Been Pwned)
- [ ] Confirm VPN is running (if using VPN on public networks)

### Monthly Habit (30 minutes)
- [ ] Run full device antivirus scan
- [ ] Update all software (OS, antivirus, password manager, VPN, browser)
- [ ] Review Phase 1/2 documentation for any unencrypted files; encrypt or delete
- [ ] Refresh understanding of legal rights: re-read your notes on attorney advice
- [ ] Delete old emails you no longer need (reduces stored metadata if subpoenaed)

---

## Part 4: Incident Response Plans

### Incident 1: Email Account Appears Compromised

**Signs**: Unexpected password reset emails, emails in sent folder you didn't send, 2FA prompted without you initiating

**Immediate response** (within 1 hour):
1. Change password immediately (strong new password, 20+ chars)
2. Review recent login activity (Gmail: Google Account → Security → Activity)
3. Check all recovery options: is backup phone number/email still yours?
4. Enable 2FA if not already enabled
5. Log out all other sessions (Gmail: Manage Your Google Account → Security → Your Devices)
6. Scan device for malware (run antivirus)

**Secondary response** (within 24 hours):
1. If email was used for distribution: email Batch 1-5 contacts: "Our email may have been compromised; if you receive suspicious emails claiming to be from us, disregard them"
2. Change passwords for any account using this email as recovery email (distribution password manager, etc.)
3. Do NOT assume compromise happened from email itself; could have been password reuse elsewhere

**Long-term**:
1. Set up email monitoring (Have I Been Pwned alerts for this email)
2. Consider switching distribution email to Proton Mail (more secure by design)

---

### Incident 2: Device Appears Compromised (Malware/Spyware)

**Signs**: Unusual device behavior (slow, fan running constantly, unexpected network activity), antivirus alerts, unusual processes in Task Manager

**Immediate response** (within 1 hour):
1. Disconnect device from network (WiFi + Ethernet)
2. Do NOT input any passwords or sensitive info on this device
3. Run antivirus in Safe Mode (Windows) or Recovery Mode (Mac)
4. If antivirus finds malware: let it quarantine/delete
5. If you're not confident: take device to IT specialist or backup and reset OS

**Secondary response** (within 24 hours):
1. Once device is clean: change all passwords you used on that device (distribution email, password manager, etc.) from a different device
2. Review recent files accessed to understand what may have been compromised
3. Contact attorney if concerned about what information may have been extracted

**Long-term**:
1. Reduce device compromise risk: update software automatically, use antivirus, limit downloads
2. Consider using separate device for Phase 1/2 work (if high-risk)

---

### Incident 3: Subpoena Received for Email or Documents

**Receiving subpoena**:
- [ ] Do NOT respond immediately
- [ ] Contact attorney same day
- [ ] Attorney will file motion to quash or negotiate scope of production

**Your attorney will guide**:
- What documents must be produced
- What information is privileged (attorney-client, work product)
- How to preserve documents (don't delete)
- Deadline for production
- Whether to seek protective order

**DO NOT**:
- Delete documents (obstruction of justice)
- Ignore subpoena (contempt)
- Produce documents without attorney guidance (may waive privilege)

---

### Incident 4: FBI or Investigative Interview Request

**If contacted**:
- [ ] Respond politely but firmly: "I decline to speak without my attorney present"
- [ ] Get attorney's name and number from your pre-identified attorney
- [ ] Tell FBI: "I'm requesting my attorney be present for any conversation"
- [ ] Do NOT answer detailed questions without attorney

**Your attorney will**:
- Guide whether to do interview or refuse
- Be present if interview happens
- Protect your rights against self-incrimination

**Key right**: You can refuse FBI interview. You are not obligated to cooperate. Refusing is not illegal.

---

## Part 5: Decision Framework — When to Use Which Mitigation

### Low-Risk Distribution (Path A or A+37, broad organizational reach)

**Apply these mitigations**:
- Tier 1, all: Email separation, disable tracking, encrypt contact list, device/network hygiene
- Tier 2: Email encryption (Proton Mail), compartmentalization
- Optional: Metadata minimization

**Time investment**: 2-3 hours setup; 5-10 min/day maintenance  
**Result**: Significant risk reduction; comfortable level of privacy

---

### Medium-Risk Distribution (Path B, staged with feedback, building partnerships)

**Apply these mitigations**:
- All Tier 1
- All Tier 2
- Tier 3: Decentralized coordination, legal insurance

**Time investment**: 4-6 hours setup; 1-2 hours/week coordination  
**Result**: Very strong operational security; minimizes damage if any one partnership is compromised

---

### High-Risk Scenario (You're targeted by investigation, or doing sensitive Phase 2 work with election organizations)

**Apply these mitigations**:
- All Tier 1-2
- All Tier 3
- Dead-man's switch, offline backups, attorney retained with standing agreement

**Time investment**: 8-10 hours setup; 2-3 hours/week ongoing  
**Result**: Comprehensive operational security; prepared for government investigation

---

## Part 6: Threat Assessment Update (Quarterly)

Every 3 months, update your threat assessment:

1. **News check**: Have there been new government investigative targets? New surveillance tools revealed (FISA 702, CBP surveillance)?
2. **Phase 1/2 status**: Who's engaged? Which organizations are most visible/public about adoption?
3. **Personal situation**: Has your risk profile changed? (New employer, different locations, media attention?)
4. **Legal environment**: Any new laws criminalizing democratic organizing? New court rulings on surveillance?

Based on update, adjust mitigations:
- If threat level increased: upgrade to higher Tiers
- If threat level decreased: can reduce overhead on lower-priority mitigations
- If new surveillance tools revealed: update defenses against those tools

---

## Key Principles

**Principle 1: Security is Ongoing, Not One-Time**
- Operational security is daily habits, not a single setup
- Plan for 5-10 minutes/day, not 5 hours once

**Principle 2: Imperfect Security is Better Than None**
- You don't need perfect anonymity; you need to be harder to target than obvious targets
- If 100 organizations adopt Phase 1, targeting you specifically has lower ROI than other targets
- Mitigations reduce your surface area; they don't make you invisible

**Principle 3: Asymmetric Time Trade**
- 3-4 hours setup saves 50+ hours of trouble if investigated
- Attorney retainer ($2,000) is cheap insurance against legal defense ($50,000+)
- Compartmentalization overhead (1 hour/week) is worth the damage limitation

**Principle 4: Know Your Threat Model**
- You're not defending against NSA (they can break most encryption)
- You're defending against: ISP monitoring, email provider logging, routine searches, low-level forensics
- These are defeatable with practical mitigations

**Principle 5: Lawyer is Essential**
- Before distributing sensitive materials, know a lawyer
- Before you're in trouble, have an attorney relationship
- This is your cheapest, most important defense

---

## Final Checklist — Before You Begin Phase 1 Distribution

- [ ] **Email**: Created new distribution email account (Gmail or Proton); enabled 2FA
- [ ] **Contacts**: Stored contact list in encrypted format (Password-protected sheet or encrypted file)
- [ ] **Tracking**: Decided NOT to use email tracking; using spreadsheet-based response tracking instead
- [ ] **Device**: Confirmed antivirus is running; OS is up to date
- [ ] **Network**: If using public WiFi, configured to use VPN
- [ ] **Passwords**: All Phase 1/2 passwords are unique and strong (20+ characters); stored in password manager
- [ ] **Backup**: Contact list backed up to encrypted cloud storage
- [ ] **Attorney**: Identified a civil rights attorney; had exploratory conversation
- [ ] **Documents**: Phase 1/2 strategy docs are stored encrypted (not in unencrypted Dropbox/Drive)
- [ ] **Compartmentalization**: Planned separation of Phase 1 (email) and Phase 2 (encrypted groups) communication
- [ ] **Daily habits**: Understood morning (2 min), weekly (10 min), monthly (30 min) OpSec tasks

**If all are checked**: You're ready to begin Phase 1 distribution with strong operational security.

---

## Questions? Legal Concerns? When to Contact Attorney

**Contact your attorney BEFORE Phase 1 if**:
- You work for government (need to understand conflict of interest rules)
- You have security clearance (need to understand disclosure requirements)
- You're in profession with gag rules (healthcare, finance, military)
- You've been previously investigated or subpoenaed
- You're coordinating with specific organizations and need legal guidance

**Contact attorney IF** (during Phase 1/2):
- You receive any government contact, interview request, or subpoena
- You suspect device compromise or account compromise
- Any participant in Phase 2 coordination is investigated or prosecuted
- Any organization you've contacted faces legal action

**Escalate to attorney IF**:
- Pattern of government surveillance (repeated interviews, unusual contacts)
- Your work is publicly characterized as illegal or subversive
- Participants in Phase 2 are charged with federal crimes related to coordination with you

---

## Resources

**Password Managers**:
- Bitwarden: Free, open source (bitwarden.com)
- 1Password: Commercial ($3/month) (1password.com)

**VPN Providers**:
- Mullvad: Free or paid ($5/month), recommended for activists (mullvad.net)
- ProtonVPN: Commercial ($4-10/month) (protonvpn.com)

**Encrypted Email**:
- Proton Mail: Free or paid ($4-12/month) (proton.me)

**Encrypted Chat**:
- Signal: Free, open source (signal.org)
- Wire: Free or commercial (wire.com)

**Encrypted Cloud Storage**:
- ProtonDrive: Free or paid ($4-30/month) (proton.me/drive)
- Tresorit: Paid ($12/month) (tresorit.com)

**Legal Resources**:
- National Lawyers Guild: nlg.org (find local chapter for attorney referral)
- ACLU: aclu.org (legal resources + potential representation)
- Center for Racial Justice: centerforracialjustice.org (civil rights legal support)

---

## Summary: Your Operational Security Posture

After implementing Tier 1-2 mitigations:
- **Email metadata**: Hidden (separate account, no tracking)
- **Email content**: Encrypted (Proton Mail or PGP)
- **Contact list**: Encrypted (password-protected or encrypted file)
- **Device**: Protected (antivirus, updates, clean)
- **Network**: Encrypted (VPN on public networks)
- **Coordination**: Compartmentalized (separate groups for different partnerships)
- **Legal**: Prepared (attorney identified and available)

**Result**: Strong operational security appropriate for Phase 1/2 distributed democracy work. Not perfect; sufficient to defend against most threats you'll encounter.
