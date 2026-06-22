---
title: "Whistleblower Implementation Checklists: Role-Specific Operational Procedures"
project: cybersecurity-hardening
created: 2026-06-22
phase: Phase 2
version: 1.0
type: operational-checklist
depends_on:
  - phase-2-institutional-whistleblowing-security-playbook.md
  - phase-2-whistleblower-legal-framework-supplement.md
  - opsec-playbook.md
audience: Federal employees, federal contractors, government ethics counsel, compliance officers, HR professionals advising whistleblowers
---

# Whistleblower Implementation Checklists

This document provides role-specific, step-by-step operational procedures for federal employees, contractors, and organizational staff members navigating a whistleblowing situation.

---

## Checklist 1: Federal Employee Whistleblower Preparation (Pre-Disclosure)

**Timeline**: Weeks 1–4 before any formal disclosure. This checklist establishes the foundation for safe, protected whistleblowing.

### Phase 1A: Legal Foundation

- [ ] **Week 1, Day 1**: Search for and contact a whistleblower attorney specializing in federal employee protection
  - [ ] Use Government Accountability Project (whistleblower.org) referral system
  - [ ] If budget-limited, contact a government ethics law clinic (many universities provide pro bono advice)
  - [ ] Book a consultation call with the attorney (explain general situation, ask about fees; initial consultation is often free)
  - [ ] Take notes on the attorney's initial guidance before spending money

- [ ] **Week 1, Days 2–3**: Identify the appropriate disclosure channel
  - [ ] Read the "Legal Framework Supplement" Section 1 to determine WPA vs. ICWPA applicability
  - [ ] If unclassified misconduct: Plan to use IG and/or OSC and/or Congress
  - [ ] If classified misconduct: Plan to use ICWPA procedures (IG of Intelligence Community or Congressional Intelligence Committee)
  - [ ] Note the specific agency IG's contact information from Section 5

- [ ] **Week 1, Day 4**: Determine if your agency has an established internal whistleblower procedure
  - [ ] Search your agency intranet for "whistleblower procedure," "ethics reporting," or "hotline"
  - [ ] Ask HR or your ethics office whether an internal procedure exists
  - [ ] Document the name, phone, and email of the internal point of contact (if any)
  - [ ] WPA disclosure to a supervisor is only protected if an established internal procedure exists; if not, skip to IG/OSC

### Phase 1B: Evidence Foundation

- [ ] **Week 2, Day 1–2**: Gather baseline performance documentation
  - [ ] Create a folder on a personal device (not work device) titled "Personal - Performance Records"
  - [ ] Forward recent positive performance evaluations from work email to personal email
  - [ ] Copy text of emails from supervisors or colleagues with positive feedback
  - [ ] Screenshot or note any commendations, awards, or special recognitions
  - [ ] Create a summary document listing: dates of evaluations, summary of feedback, supervisor names
  - [ ] Store this folder in encrypted storage (use VeraCrypt or device's native encryption)

- [ ] **Week 2, Days 3–5**: Create an evidence timeline document
  - [ ] On a personal device, create a single document titled "Misconduct Timeline - Personal Notes"
  - [ ] List the first date you became aware of potential misconduct
  - [ ] List all subsequent observations, including:
     - [ ] Date and time observed
     - [ ] Specific individuals involved
     - [ ] What was said or done (verbatim, if possible)
     - [ ] Any documents you personally viewed (note title, date, classification — do not copy)
     - [ ] Location where the observation took place
     - [ ] Any witnesses who were present
  - [ ] Format as a simple chronology, not a narrative
  - [ ] Store in encrypted storage

- [ ] **Week 2**: Identify and document the specific law/rule/regulation violation
  - [ ] Using non-work resources (personal computer, library), research the specific statutes or regulations allegedly violated
  - [ ] Print or save the relevant statute text
  - [ ] Create a 1-page document connecting each observed fact to the specific regulatory violation
  - [ ] Example: "Observation on 3/15/26: Manager X instructed employee Y to delete compliance documentation. Federal Records Act (44 U.S.C. § 2107) requires retention of federal records. Violation: unlawful destruction of federal records."
  - [ ] Share this document with your attorney for review

- [ ] **Week 3**: Identify comparators (evidence of disparate treatment)
  - [ ] Identify colleagues with similar job responsibilities, tenure, and performance history
  - [ ] Note any adverse actions you received that these colleagues did NOT receive
  - [ ] Document: dates of the comparator employees' actions vs. your adverse actions
  - [ ] Example: "On 4/1/26, I was denied attendance at the quarterly training conference. Colleague Z (same grade, same division) attended on 3/20/26 with no issues. Colleague W (same grade, different division) was recommended for the conference on 4/2/26."
  - [ ] Do not discuss this with colleagues; base this on your own observation and documented records

### Phase 1C: Device and Communication Security

- [ ] **Week 3**: Establish a dedicated evidence device
  - [ ] Obtain a personal device (phone or tablet) purchased with cash or through a retailer not linked to your professional identity
  - [ ] Does NOT connect to any employer network, Wi-Fi, or device
  - [ ] Load with GrapheneOS (if Android) or factory reset iOS
  - [ ] Enable full device encryption (default on both)
  - [ ] Disable all cloud backup (iCloud, Google Drive, etc.)
  - [ ] Set a strong alphanumeric passphrase (not biometric; enable auto-reboot to 18 hours)
  - [ ] Install Signal and register with a VoIP number (MySudo or JMP.chat)
  - [ ] Store physically in your home, not in your office or car

- [ ] **Week 3**: Establish secure email
  - [ ] Create a ProtonMail or Tutanota account on personal device, over VPN or Tor (not home IP)
  - [ ] Use a username not connected to your real identity
  - [ ] Store the password in Bitwarden (on a personal device, not work device)
  - [ ] Enable 2FA using Ente Auth (on your personal phone)
  - [ ] Use this email for attorney communications and potential media contact (if applicable)

- [ ] **Week 4**: Verify secure communication with attorney
  - [ ] Confirm with your attorney their preferred secure communication method:
     - [ ] In-person meetings only (most secure)
     - [ ] Signal on a dedicated device
     - [ ] ProtonMail encrypted email
  - [ ] Test the secure communication channel before disclosing sensitive details
  - [ ] Verify your attorney's Signal safety number in person if using Signal

### Phase 1D: Operational Security Implementation

- [ ] **Week 4**: Establish normal behavior baseline on work systems
  - [ ] Review your typical work schedule and access patterns
  - [ ] Note the times you typically log in and log off
  - [ ] Note the systems and applications you typically use
  - [ ] Document your normal file access (what folders/documents you access for your job)
  - [ ] Create a document on your personal device describing "normal work behavior for [your role]"
  - [ ] This is your reference for maintaining normal patterns during the evidence collection period

- [ ] **Week 4**: Plan your evidence collection activity
  - [ ] Define exactly which documents, systems, or personnel communications you need for evidence
  - [ ] Categorize as: (a) documents you can legally access as part of your job, (b) information you can gather through memory and notes, (c) documents you cannot access without raising suspicion
  - [ ] Plan to access only category (a) through work systems, on a normal schedule, at normal times
  - [ ] All documentation should occur on personal devices, on personal networks, on personal time
  - [ ] Brief your attorney on your planned evidence collection strategy

---

## Checklist 2: Federal Employee During Evidence Collection (Weeks 5–12)

**Timeline**: This phase occurs after legal foundation is set and before formal disclosure. The critical rule is MAINTAIN NORMAL WORK BEHAVIOR on employer systems while collecting evidence only on personal systems.

### Phase 2A: Monthly Behavior Verification

- [ ] **Each month**:
  - [ ] Review your work schedule from the past 30 days. Verify it matches your normal pattern.
     - [ ] Did you work at normal times (not off-hours)?
     - [ ] Did you take your normal breaks?
     - [ ] Did you use normal Wi-Fi/networks?
  - [ ] Review your file access history (if you can pull it without arousing suspicion)
     - [ ] Did you access files outside your normal job scope? (If yes, note the access and the justification for it)
     - [ ] Did you access files at unusual times? (If yes, note when and why)
  - [ ] Review any email searches you conducted
     - [ ] Did you search for "whistleblower," "ethics," "fraud," or related terms? (If yes, do only on personal devices going forward)
  - [ ] Check your communication patterns
     - [ ] Did you have unusual conversations with colleagues about the misconduct? (If yes, document in your personal notes and discuss with attorney)

- [ ] **Each month**: Update your evidence timeline
  - [ ] Add any new observations made during the month
  - [ ] Update comparators if new information becomes available
  - [ ] Verify all dates and facts

### Phase 2B: Evidence Collection (Do's and Don'ts)

**DO**:
- [ ] Make contemporaneous notes on personal devices about what you observed in person
- [ ] Take photographs of screens displaying relevant documents (using personal phone, not connected to work Wi-Fi)
- [ ] Write down from memory what someone said, as soon as you leave their presence
- [ ] Review documents that are part of your normal job duties, at normal times
- [ ] Discuss the matter with your attorney on your secure channel
- [ ] Maintain your normal work schedule and access patterns

**DO NOT**:
- [ ] Copy files from employer systems to personal devices (this creates employer monitoring alerts)
- [ ] Forward work emails to your personal email address (this creates network logs)
- [ ] Access documents outside your normal job scope, especially on employer systems
- [ ] Conduct searches on employer systems for terms like "whistleblower," "retaliation," "fraud," "ethics"
- [ ] Discuss the potential whistleblowing with colleagues
- [ ] Post on social media about the misconduct, even vaguely
- [ ] Change your normal work behavior (working off-hours, accessing different systems, etc.)
- [ ] Use work email or messaging apps for any discussion related to the misconduct

### Phase 2C: Retaliation Monitoring and Documentation

- [ ] **Each week**: Brief self-assessment
  - [ ] Have you received any new or unusual criticism from management?
  - [ ] Have you been excluded from meetings or projects you normally attend?
  - [ ] Have you noticed any changes in your supervisor's tone or communication?
  - [ ] Have any colleagues mentioned an investigation or internal review?
  - [ ] If yes to any: document in your personal notes with date, time, and details

- [ ] **Immediately upon any adverse employment action**:
  - [ ] Document what happened: date, time, location, who was involved
  - [ ] Document what was said (direct quotes if possible)
  - [ ] Document the action (reassignment, negative review, exclusion, etc.)
  - [ ] Document timing (how many days/weeks after your protected disclosure, if applicable)
  - [ ] Identify any comparators (how were similarly-situated employees treated?)
  - [ ] Email your attorney the documentation within 24 hours

---

## Checklist 3: Formal Disclosure Preparation (1 Week Before Disclosure)

**Timeline**: The week immediately before filing your formal complaint or disclosure. At this point, your attorney has reviewed your evidence and approved your disclosure plan.

### Phase 3A: Disclosure Channel Finalization

- [ ] **Attorney approval of disclosure plan**:
  - [ ] Your attorney has reviewed your evidence and misconduct timeline
  - [ ] Your attorney has advised which disclosure channel(s) to use (IG, OSC, Congress, media, or combination)
  - [ ] If False Claims Act case: qui tam complaint is prepared and ready to file
  - [ ] If OSC case: Form OSC-14 is prepared
  - [ ] If Congressional disclosure: specific committee contact(s) identified and attorney has confirmed appropriate channel
  - [ ] If media disclosure: SecureDrop outlet selected and verified secure

- [ ] **IG disclosure (if applicable)**:
  - [ ] IG office contact information confirmed (phone, mailing address, online form URL)
  - [ ] IG hotline tested from personal device (call to confirm current hours and procedures)
  - [ ] Disclosure summary document prepared (1–2 pages describing the allegation, law violated, recommending investigation)
  - [ ] Evidence documentation organized and indexed

- [ ] **OSC disclosure (if applicable)**:
  - [ ] Form OSC-14 completed with your attorney's review
  - [ ] Description of protected disclosure(s) included
  - [ ] Description of adverse employment action(s) included
  - [ ] Timing documentation included
  - [ ] Two copies printed (one to mail, one to keep)
  - [ ] Evidence appendices prepared and indexed

- [ ] **Congressional disclosure (if applicable)**:
  - [ ] Congressional committee contact information confirmed (staff director name, phone, email)
  - [ ] Letter to Congressional staff prepared:
     - [ ] Marked "CONFIDENTIAL"
     - [ ] Addressed to specific staff member by name
     - [ ] Clearly states the alleged misconduct and specific law(s) violated
     - [ ] Requests confidentiality and protection from retaliation
     - [ ] Includes your contact information
  - [ ] Two copies printed (one to mail, one to keep)
  - [ ] Evidence appendices prepared and indexed

### Phase 3B: Device and Data Preparation

- [ ] **Secure all evidence materials**:
  - [ ] All personal notes, timelines, and documentation are stored on the dedicated evidence device
  - [ ] All evidence is encrypted (VeraCrypt container or device native encryption)
  - [ ] Evidence device has no cloud backup or synchronization
  - [ ] Evidence device is physically secured in your home
  - [ ] You have a physical backup copy of critical documents (in a safe, safety deposit box, or attorney's office)

- [ ] **Prepare evidence transmission**:
  - [ ] If disclosing via IG online form or Congressional online form: evidence files are ready to upload
  - [ ] If disclosing to attorney for submission: evidence is organized in clear folder structure
  - [ ] If submitting in person: evidence is printed in clear order with index
  - [ ] If submitting by mail: all documents are copied (keep originals), placed in sealed envelope, ready to mail

- [ ] **Secure communication verification**:
  - [ ] Signal safety numbers verified with attorney (if using Signal)
  - [ ] ProtonMail account accessible and tested
  - [ ] Tor Browser installed and tested (if planning to use SecureDrop)
  - [ ] VPN tested and functioning (if planned for use)

### Phase 3C: Personal Affairs Organization

- [ ] **Financial preparation**:
  - [ ] Emergency fund established (6 months of expenses) in a separate account, if possible
  - [ ] Debt payments are current
  - [ ] Know your unemployment insurance eligibility
  - [ ] Know your health insurance status (COBRA, spouse's plan, ACA, etc.)
  - [ ] Consider whether you can afford an extended job search or legal battle

- [ ] **Personal notification (limited)**:
  - [ ] Your spouse or partner is informed of:
     - [ ] That you are working with a whistleblower attorney
     - [ ] That you may face retaliation or employment action
     - [ ] What to do if you are approached by investigators
     - [ ] That the matter is confidential and should not be discussed with anyone
  - [ ] No colleagues, friends, or family members (beyond spouse/partner) are informed
  - [ ] You have not posted on social media

---

## Checklist 4: Disclosure Day (OSC, IG, or Congressional)

**Timeline**: The day you file your official complaint or make your protected disclosure. From this point forward, you have documented proof of a protected disclosure and legal protections attach.

### Phase 4A: IG Disclosure (Phone or Online Form)

- [ ] **By phone (most secure)**:
  - [ ] Call from personal phone or non-work line
  - [ ] Ask for the hotline investigator
  - [ ] Provide:
     - [ ] Your name and job title
     - [ ] Agency you work for
     - [ ] Brief description of the alleged misconduct
     - [ ] Request for a case number
  - [ ] Write down the case number, investigator name, and phone number
  - [ ] After the call, email your attorney with the case number and date

- [ ] **By online form or mail**:
  - [ ] Go to the IG website (e.g., oig.dhs.gov)
  - [ ] Fill out the online form or download the mail-in form
  - [ ] Provide:
     - [ ] Your name and job title (full identification is typically required for IG complaints)
     - [ ] Agency and office location
     - [ ] Description of the alleged misconduct and law(s) violated
     - [ ] Timeline of when you became aware
     - [ ] Request for confidentiality (though full confidentiality cannot be guaranteed if investigation requires identifying you)
  - [ ] If mailing: use certified mail with return receipt
  - [ ] Keep a copy for yourself
  - [ ] Email your attorney with the copy and receipt information

### Phase 4B: OSC Disclosure (Form OSC-14)

- [ ] **Prepare the submission**:
  - [ ] Form OSC-14 completed with all required information
  - [ ] Box 1: Your name, address, phone, email
  - [ ] Box 2: Agency, office location, job title
  - [ ] Box 3: Description of protected disclosure(s) you made (date, to whom, what was disclosed)
  - [ ] Box 4: Description of adverse action(s) taken against you (date, who took action, what the action was)
  - [ ] Box 5: Explanation of how the adverse action was motivated by your protected disclosure
  - [ ] Evidence appendices (timeline, comparator data, performance history, any written documentation)

- [ ] **Submit the form**:
  - [ ] Online submission via osc.gov (preferred): upload the form and evidence documents
  - [ ] Mail submission (alternative): send to Office of Special Counsel, 1730 M Street NW, Suite 218, Washington, DC 20036
  - [ ] Keep a copy for yourself
  - [ ] Email your attorney with confirmation of submission

- [ ] **Receive case number**:
  - [ ] OSC will provide a case number
  - [ ] Note the case number and keep it for future reference
  - [ ] You are protected from retaliation as of the filing date

### Phase 4C: Congressional Disclosure

- [ ] **Prepare communication**:
  - [ ] Letter prepared and reviewed by attorney
  - [ ] Letter is addressed to [Staff Director Name], [Committee Name]
  - [ ] Letter clearly describes the alleged misconduct
  - [ ] Letter references specific laws or regulations violated
  - [ ] Letter identifies you by name and position
  - [ ] Letter requests confidentiality and protection from retaliation
  - [ ] Letter includes your phone number and email for follow-up
  - [ ] Evidence appendices prepared and indexed

- [ ] **Submit to Congress**:
  - [ ] By phone (most secure): call the committee main number, ask for the staff director, provide initial summary, request a secure submission address
  - [ ] By secure email: use the committee's secure email address (if available) to send the letter and evidence
  - [ ] By mail (certified): send to the committee office address with your letter and evidence
  - [ ] Keep a copy for yourself
  - [ ] Note the date and method of submission

- [ ] **Follow-up**:
  - [ ] Congressional staff will contact you for follow-up or an interview
  - [ ] You may request to have your attorney present for any interview
  - [ ] Document all Congressional contacts in your personal notes

### Phase 4D: Post-Disclosure Immediate Actions

- [ ] **At the end of disclosure day**:
  - [ ] Update your evidence timeline with the disclosure date, method, and confirmation numbers
  - [ ] Email your attorney with:
     - [ ] Confirmation of what was submitted
     - [ ] Case numbers or confirmation receipts
     - [ ] Date and method of submission
  - [ ] Secure all original documents in your home safe or attorney's office
  - [ ] Do NOT discuss the disclosure with colleagues or on social media
  - [ ] Maintain normal work behavior

---

## Checklist 5: Post-Disclosure Months (Ongoing Protection)

**Timeline**: Weeks 1–52 after formal disclosure. This phase focuses on documentation of any retaliation and continued operational security.

### Phase 5A: Monthly Monitoring

- [ ] **Every month**:
  - [ ] Review your recent performance evaluations and feedback
     - [ ] Are reviews consistent with pre-disclosure evaluations?
     - [ ] Any new criticisms of your work?
     - [ ] Any exclusions from meetings or projects?
  - [ ] Review any communications about your assignments, promotions, or benefits
  - [ ] Check for any HR contacts, investigation notifications, or unusual inquiries
  - [ ] Update your retaliation documentation (if any adverse actions have occurred)
  - [ ] Check in with your attorney with any updates

- [ ] **Investigation communications**:
  - [ ] If your agency's IG or an investigator contacts you, note:
     - [ ] Date and method of contact (phone, email, in-person)
     - [ ] Name and title of investigator
     - [ ] Topic of questions
     - [ ] Request for documents or follow-up interview
  - [ ] Respond to all investigator requests promptly
  - [ ] Provide requested information through your attorney if possible
  - [ ] Attend any interviews requested (with attorney if possible)

### Phase 5B: Retaliation Documentation Protocol

**If you experience any adverse employment action after disclosure** (negative review, reassignment, exclusion, discipline, or termination):

- [ ] **Immediate documentation (within 24 hours)**:
  - [ ] Date, time, and location of the action
  - [ ] Who took the action (name and title)
  - [ ] What exactly was said and done
  - [ ] Any written documentation (email, performance review, notice, etc.)
  - [ ] Witnesses to the action
  - [ ] Your explanation of why the action is retaliation

- [ ] **Comparator documentation**:
  - [ ] Identify employees with similar:
     - [ ] Job title and grade
     - [ ] Tenure with the agency
     - [ ] Prior performance ratings
     - [ ] Functional responsibilities
  - [ ] Document any adverse actions they received vs. actions you received
  - [ ] Example: "I was reassigned to a lower-profile office; Colleague X (same grade, same tenure, same job title) with a similar prior performance rating was promoted to a senior position."

- [ ] **Causation documentation**:
  - [ ] Note the date of your protected disclosure
  - [ ] Note the timing of the adverse action (how many days/weeks after disclosure)
  - [ ] Closer timing = stronger evidence of retaliation
  - [ ] Note any statements made by management connecting the action to your disclosure

- [ ] **Performance record documentation**:
  - [ ] Save any performance evaluations, emails, or commendations after the adverse action that conflict with the retaliatory action
  - [ ] Save any emails from colleagues or supervisors praising your work (if received after the adverse action)
  - [ ] This creates a record showing the adverse action was not based on legitimate performance concerns

- [ ] **Notify your attorney within 48 hours**:
  - [ ] Forward all documentation of the adverse action
  - [ ] Discuss next steps (OSC retaliation amendment, Congressional re-contact, legal action preparation)

### Phase 5C: Long-Term Legal Strategy

- [ ] **Quarterly check-in with attorney**:
  - [ ] Review investigation status (if applicable)
  - [ ] Update timeline of any retaliation
  - [ ] Discuss legal options if retaliation occurs
  - [ ] Assess financial situation and funding for ongoing legal representation

- [ ] **Record preservation**:
  - [ ] Maintain all original documents in secure storage (attorney's office or home safe)
  - [ ] Keep digital backups on encrypted personal devices
  - [ ] Do not delete any documents, emails, or messages related to the disclosure

---

## Checklist 6: If You Are Identified Before Disclosure (Emergency Protocol)

**Timeline**: Immediate response if you learn that your evidence-gathering activity or whistleblower intent has been discovered before you intended to disclose.

### Phase 6A: Immediate Actions (Next 2 Hours)

- [ ] **Power off all personal devices containing evidence**:
  - [ ] Do not put them to sleep; power them off completely
  - [ ] Remove biometric authentication (no Face ID or fingerprint)
  - [ ] This puts the device in BFU (Before First Unlock) state if suddenly seized

- [ ] **Contact your attorney immediately**:
  - [ ] Call your attorney from a phone line not registered to you (borrowed phone, landline) if possible
  - [ ] Brief them on what you believe has happened
  - [ ] Ask for immediate guidance on next steps
  - [ ] Do NOT discuss on any device, text, or email until you have attorney guidance

- [ ] **Do not access work systems**:
  - [ ] Log off immediately
  - [ ] Do not log back on until you have attorney guidance
  - [ ] Do not attempt to delete, modify, or retrieve anything from work systems

- [ ] **Do not communicate with colleagues**:
  - [ ] Do not discuss the situation with anyone at work
  - [ ] Do not attempt to explain or defend yourself to colleagues
  - [ ] Do not post on social media

### Phase 6B: First 24 Hours

- [ ] **Attorney strategy session**:
  - [ ] Meet with your attorney in person if possible
  - [ ] Discuss whether to accelerate disclosure (file OSC complaint immediately) to establish protected status
  - [ ] Discuss whether to request leave of absence or resign
  - [ ] Discuss next steps with IG, OSC, or Congress
  - [ ] Discuss how to respond if questioned by investigators or HR

- [ ] **File protective disclosure (within 24 hours if recommended)**:
  - [ ] If attorney recommends, file an OSC complaint immediately
  - [ ] Accelerated filing creates a protected disclosure record before any adverse action
  - [ ] Filing creates legal protection even if the full evidence is not yet compiled

- [ ] **Document the timeline**:
  - [ ] Detailed notes of how you learned about the investigation/discovery
  - [ ] Who told you, what they said, when
  - [ ] What led you to believe your whistleblowing activity was discovered
  - [ ] What actions the employer has or has not taken

- [ ] **Preserve evidence**:
  - [ ] Transfer all personal devices to attorney's office for secure storage
  - [ ] Provide attorney with passwords and access information (in writing, stored by attorney)
  - [ ] Attorney now has custody of evidence; attorney-client privilege protects the evidence

### Phase 6C: First 72 Hours

- [ ] **HR or investigation interview preparation**:
  - [ ] If your employer requests a meeting, bring your attorney (if possible) or request to bring counsel
  - [ ] Do not attend an interview without legal representation
  - [ ] Provide only answers that your attorney has approved
  - [ ] Request written confirmation of what was discussed

- [ ] **Performance action response**:
  - [ ] If any adverse employment action is taken (suspension, termination, reassignment), document it immediately
  - [ ] Request written explanation of the action
  - [ ] Provide written response explaining why the action is retaliatory
  - [ ] Preserve all documentation

---

## Checklist 7: Tools and Resources Setup

### Communication Tools

- [ ] **Signal**:
  - [ ] Download from signal.org (not App Store or Play Store initially)
  - [ ] Register with VoIP number (MySudo.com or JMP.chat)
  - [ ] Enable disappearing messages (default to 1 hour)
  - [ ] Enable screen lock

- [ ] **ProtonMail**:
  - [ ] Create account on personal device over VPN
  - [ ] Enable 2FA with Ente Auth
  - [ ] Use for attorney communication only
  - [ ] Do not use for casual email

- [ ] **Tor Browser**:
  - [ ] Download only from torproject.org
  - [ ] Use for accessing SecureDrop (if media disclosure planned)
  - [ ] Keep updated to latest version

### Device Tools

- [ ] **VeraCrypt**:
  - [ ] Create encrypted container for evidence storage
  - [ ] Use strong passphrase (6+ random words)
  - [ ] Store on personal device
  - [ ] Keep backup copy in attorney's office

- [ ] **Bitwarden**:
  - [ ] Create account for password management
  - [ ] Store attorney contact information securely
  - [ ] Store IG/OSC contact information
  - [ ] Enable 2FA

### Legal Resources

- [ ] **Government Accountability Project**:
  - [ ] Phone: (202) 408-0034
  - [ ] Website: whistleblower.org
  - [ ] Free initial consultation for federal whistleblowers

- [ ] **National Whistleblower Center**:
  - [ ] Website: whistleblowers.org
  - [ ] FCA and other statute resources

- [ ] **Office of Special Counsel**:
  - [ ] Phone: 1-202-804-7000
  - [ ] Website: osc.gov
  - [ ] Form OSC-14 available online

- [ ] **SEC Whistleblower Office** (if applicable):
  - [ ] Website: sec.gov/whistleblower
  - [ ] Anonymous submission through attorney

- [ ] **Oversight.gov**:
  - [ ] Central directory of where to report fraud, waste, abuse
  - [ ] Lists all federal IG contacts

---

**Version**: 1.0  
**Created**: June 22, 2026  
**Author**: Cybersecurity-Hardening Project  
**Next Review**: September 22, 2026 (quarterly)

---

**Note**: These checklists are templates. Your specific situation may require variations. Work with your attorney to adapt these checklists to your circumstances.
