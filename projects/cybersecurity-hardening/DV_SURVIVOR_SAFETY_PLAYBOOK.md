---
title: "DV Survivor Safety Playbook: Threat-Informed Protection from Intimate Partner Surveillance to Long-Term Safety"
project: cybersecurity-hardening
phase: Phase 2
created: 2026-05-26
version: 1.0
status: production-ready
distribution: NNEDV pilot — June/July 2026
audience: DV survivors, DV advocates and shelter staff, hotline workers, legal advocates, safety planners
depends_on:
  - opsec-playbook.md
  - phase-2-dv-survivor-safety-playbook.md
  - phase-2-dv-survivor-security-playbook.md
word_count: ~7,200
sources_confidence: high — grounded in NNEDV Safety Net Project documentation, Coalition Against Stalkerware 2025 Annual Report, AV-Comparatives 2025 Stalkerware Test, USCIS VAWA policy manual (December 2025), California AB 2499 (effective January 2025), Washington State DV Manual for Judges (December 2025), DOJ Legal Assistance for Victims Program 2025, Apple/Google unwanted tracking specification, DomesticShelters.org shelter data, NCADV state coalition directory
cross_references:
  - opsec-playbook.md (Phase 1 integration)
  - phase-2-immigration-surveillance-evasion-playbook.md (ICE/VAWA intersection)
  - phase-2-financial-resistance-security-playbook.md (economic independence)
---

# DV Survivor Safety Playbook

**CRITICAL SAFETY NOTE — READ BEFORE ANYTHING ELSE**

This guide must be used with care. Changing device security, removing monitoring software, altering financial accounts, or breaking location sharing can alert an abusive partner and cause danger to escalate. **Do not take any technical action described in this guide without first speaking with a domestic violence advocate.** If you are in immediate danger, call 911. If you cannot call safely, text "START" to 88788 (National DV Hotline) or use the chat at thehotline.org — both are silent options. If your device may be monitored, access this guide from a device your abuser does not know about: a library computer, a friend's phone, or a phone purchased with cash.

**For advocates and shelter staff**: This playbook is designed to be worked through together with a survivor, not distributed as a self-help document. Technology safety without a completed safety plan is incomplete and potentially dangerous. Your professional judgment about what steps are appropriate for a given survivor's situation and timeline overrides any checklist in this document.

**Population context**: The National Network to End Domestic Violence (NNEDV) estimates that 10 million Americans experience intimate partner violence each year. The period immediately after separation is the most dangerous — homicide risk is elevated by roughly 10x during the weeks following an exit. The technology component of safety planning is now standard: NNEDV's Safety Net Project reports that approximately half of victim service providers document abusers using phone applications to stalk their partners.

---

## Section 1: Threat Model for the DV Context

### 1.1 How Abuser Surveillance Differs from Government or Corporate Surveillance

Every other security playbook in this corpus — the government surveillance guide, the immigration evasion playbook, the journalist security guide — addresses a threat actor who is external to the target's life. They must build knowledge about the target from the outside: requesting records, pulling data broker files, correlating metadata.

The intimate partner adversary starts from a position of complete access. This structural difference is the defining fact of the DV threat model.

| Capability | Government / Corporate Adversary | Intimate Partner Adversary |
|---|---|---|
| Device access | Requires legal process or sophisticated exploit | Had physical access to the device; may have installed monitoring software during normal use |
| Account credentials | Requires legal compulsion or a breach | Knows passwords; set up joint family plans; may be the primary account holder |
| Location knowledge | Requires metadata correlation or warrant | Has firsthand knowledge of daily routines, frequent locations, vehicle, workplace |
| Social network | Must construct through open-source intelligence | Already knows family, friends, coworkers, advocates, and children's school staff |
| Financial access | Requires financial institution cooperation | May have joint accounts, be listed as authorized user on credit cards, control primary banking |
| Legal weaponization | Works within law enforcement structures | May have law enforcement connections; custody proceedings and civil litigation are weaponizable against the survivor |

The correct framing is not "hardening a device against intrusion." It is "rebuilding a digital life from within a perimeter that has been fully compromised by someone with intimate prior access."

### 1.2 Abuser-Specific Surveillance Tactics

**Stalkerware.** Commercial applications — mSpy, FlexiSPY, Hoverwatch, Cocospy, and dozens of others — are sold for as little as $30/month as "parental monitoring" or "employee monitoring" tools. They require a single session of physical device access for installation and then run invisibly. Capabilities vary by product but commonly include: real-time GPS location updates every 1–15 minutes; all call logs with duration; all SMS messages; iMessage and some encrypted app content via screen capture; keylogging (capturing passwords as they are typed); camera and microphone activation in some products; browser history; and photos. On Android, approximately 90% of commercial stalkerware products require Accessibility Services permission for keylogging and screen content access — an Android-specific entry point. On iPhone, monitoring typically requires either device jailbreaking (visible) or access to the Apple ID credentials to monitor iCloud backups remotely (no device contact required).

The Coalition Against Stalkerware's 2025 annual report documented over 14,000 cases reported through partner organizations — a number that substantially undercounts unreported cases.

**Hardware location trackers.** AirTags and equivalent devices (Tile, Samsung SmartTag) can be hidden in vehicles (wheel wells, under bumpers, trunk lining), bags, jacket linings, children's backpacks, and car seats. An AirTag hidden in the morning may not trigger a detection alert until 8–24 hours later. Apple (iOS 17.5+) and Google jointly published an industry standard for unwanted tracker detection in 2024; automatic background scanning is now active on modern iOS and Android devices. AirTag stalking cases rose from 57 in 2018 to nearly 600 by end of 2024 — a 1,034% increase in coercive control cases involving tracking technology.

**Shared platform surveillance.** Shared carrier family plans give the primary account holder access to call logs, data usage patterns, and real-time location for all lines. Verizon, AT&T, and T-Mobile all expose this through account management portals. iCloud Family Sharing and Google Family Link extend access to app purchase history, screen time data, and location to the group owner. Voluntarily shared location apps (Life360, Google Maps location sharing, Snapchat) continue transmitting after a survivor forgets to revoke them — and revoking them sends a notification to the other party, making timing critical.

**Smart home weaponization.** Smart speakers (Amazon Echo, Google Nest) continuously process audio in the home and can be used to monitor conversations in rooms where the abuser has no physical presence. Smart locks allow the abuser to see when doors are unlocked and by whom. Smart thermostats (Nest, Ecobee) record occupancy patterns. Security cameras remain under abuser control unless account access is explicitly transferred. Smart TVs with cameras represent a visual monitoring vector in some configurations.

**Social media mining.** Even locked accounts may reveal location through background details in photos, tagged locations, check-ins by mutual friends, or metadata on image files. Abusers frequently monitor mutual friends' accounts to piece together a survivor's location and activity.

**Financial account access.** Transactions on shared accounts reveal purchase locations (gas stations reveal neighborhoods, pharmacies reveal health status, grocery stores narrow geographic radius). Credit card statements show travel patterns. Some abusers use credit report pulls (through free monitoring services or, in some cases, identity theft) to locate a survivor's new address. A credit freeze at all three bureaus (Equifax, Experian, TransUnion) blocks this access.

### 1.3 DV Survivor Threat Matrix: Five Phases

The DV threat changes as the survivor's situation changes. Security measures appropriate for one phase may be dangerous in another.

| Phase | Primary Risk | Key Security Priority |
|---|---|---|
| Phase 0: Pre-Separation | Detection of planning by abuser | Stealth — no visible changes to surveillance patterns |
| Phase 1: Separation Planning | Abuser intercepts communications, detects parallel preparations | Parallel infrastructure — new accounts, new device, new network |
| Phase 2: Immediate Post-Separation (First 72 Hours) | Physical location exposure; financial account lockout | Location security, financial access, physical safety |
| Phase 3: Ongoing Protection (First 90 Days) | Sustained surveillance, legal proceedings, escalation attempts | Sustained countermeasures, legal protective orders, address confidentiality |
| Phase 4: Recovery and Rebuilding (3–6 Months+) | Residual data broker exposure, custody weaponization, isolation | Long-term identity safety, autonomy restoration, community reintegration |

### 1.4 Data Sources Abusers Exploit

- Email accounts (especially recovery access to other accounts)
- Phone location data (carrier family plans, Find My, Google Maps sharing)
- Financial accounts (transaction-level location data, credit inquiries)
- Social media platforms (location metadata, photos, mutual friend monitoring)
- Shared cloud storage (iCloud, Google Photos — backed-up photos include location metadata)
- Utility accounts (power, water, internet — billing address reveals new location)
- Smart home systems (as noted above)
- IP addresses (a message sent from a new location reveals that IP, which can be correlated to a general geographic area)
- Data brokers (LexisNexis, Spokeo, BeenVerified — aggregate DMV records, voter registration, property records)

### 1.5 Intersection with Government Surveillance

For undocumented DV survivors, the threat model has a second layer: fear of immigration enforcement may prevent reporting abuse to police, accessing shelters, or filing for protective orders. This fear is not irrational — there are documented cases of abusers threatening to report survivors to ICE as a control mechanism. Key protective legal provisions exist (VAWA self-petition, U visa) but require legal assistance to navigate safely. See Section 5.7 for detailed immigration-DV intersection guidance.

Additionally, law enforcement database links create specific risks when the abuser is a law enforcement officer: DMV records, address databases, and law enforcement information networks are accessible to abusers who are officers without triggering external scrutiny. Address Confidentiality Programs (Section 5.4) are especially critical in this scenario.

---

## Section 2: Five-Phase Protection Architecture

### Phase 0: Pre-Separation Planning — Building Escape Without Detection

The pre-separation phase requires the most careful operational security of any phase: visible changes will alert the abuser before a safety plan is in place.

**The core principle**: maintain the appearance of normalcy on all monitored channels while building an independent, invisible parallel infrastructure.

**Secure communication setup.** Do not use any device or account the abuser has access to for safety planning. Use a device the abuser does not know about — a library computer, a trusted friend's phone, or a phone purchased with cash (see Burner Device, Phase 1). Use Tails OS (tails.boum.org) from a USB drive at a library computer for maximum security: Tails leaves no trace on the host computer and routes all traffic through Tor.

**Document preservation.** Photograph or photograph copies of all critical documents: Social Security card, birth certificates (yours and children's), passport, health insurance cards, medications list, financial account numbers, lease or deed, vehicle titles. Store these photos in a secure location: a Signal "Note to Self" on the new burner phone, or in an account the abuser cannot access. Physical copies stored at a trusted friend's home or a DV shelter intake are an alternative.

**Financial independence groundwork.** Open a new bank account in your name only, at an institution the abuser does not use, before any other financial changes. Fund it minimally (a $25 money order purchased with cash establishes the account without triggering a check from a joint account). Build a small cash reserve over time through small ATM withdrawals — not a large single withdrawal that would appear unusual. Store cash at a location the abuser does not control.

**Support network activation.** Identify one or two trusted people who can know your plans — not everyone needs to know, and over-informing creates information security risk if mutual friends inadvertently reveal details. Tell them what you need: a temporary place to stay, transportation, or storage for documents and a small bag. Share the National DV Hotline number with them (1-800-799-7233) so they understand the resources available.

**Contact an advocate.** The National DV Hotline (1-800-799-7233) connects survivors with safety planners 24/7. This conversation, from a safe device, is the foundation for everything else. A safety plan precedes all technology steps.

### Phase 1: Separation Planning — Setting Up the Parallel Infrastructure

With a safety plan in place and advocate support, Phase 1 builds the independent digital and physical infrastructure for exit.

**New device acquisition.** Purchase a prepaid Android or iPhone with cash at Walmart, Walgreens, CVS, Target, or Dollar General. No-contract phones are available for $25–$70 with no ID required. Also purchase a prepaid SIM (Tracfone, Mint Mobile, Cricket, Boost Mobile) with cash. Do not port your existing phone number. The new number must be unknown to the abuser. Keep the new device at a safe location outside the home: a trusted friend's, a workplace locker, or a DV shelter.

**New account setup.** From the new phone, connected to a WiFi network the abuser does not monitor (library, shelter, friend's home), create:
- A new email address on ProtonMail (proton.me) or Tutanota (tutanota.com) — both provide end-to-end encryption and do not require an existing phone number to create
- A new Apple ID or Google account, linked only to the new email
- Signal registered to the new phone number — the foundation for encrypted communication with advocates, attorneys, and trusted supporters

**Encrypted photo backup.** Install Ente Photos (ente.io) on the new device. Ente provides end-to-end encrypted cloud photo storage: documents you photograph, evidence of abuse, custody-relevant photos. Unlike iCloud or Google Photos, Ente photos are inaccessible to anyone who obtains your Google or Apple credentials.

**Legal aid engagement.** Contact a legal aid organization in your state (LawHelp.org by state) or the DV Hotline for referrals. A DV legal advocate can file for an emergency protective order, advise on custody matters, and navigate the protective order process. Many legal aid organizations handle DV cases without fee.

**Shelter and housing exploration.** DomesticShelters.org (domesticshelters.org/search) provides a searchable database of 3,000+ programs across the U.S. and Canada, filterable by location, language, services, and pet accommodation. Safe Havens for Pets (safehavensforpets.org) coordinates pet boarding for survivors whose shelter cannot accept animals.

**Do not change anything visible.** The old device continues to show normal patterns. Do not delete apps, change passwords, or alter social media settings on monitored devices or accounts. All planning activity happens on the new device, on new accounts, over networks the abuser does not monitor.

### Phase 2: Immediate Post-Separation — The First 72 Hours

The 72 hours after separation is when physical safety risk is highest and the most critical security transitions must happen.

**Location security — immediate actions.**
- Physically sweep your vehicle, bags, and clothing for AirTags and Bluetooth trackers before leaving a shelter or temporary address. Common hiding spots: wheel wells (magnetic), under bumpers, trunk lining, seat pockets, bag interior pockets, children's backpacks and car seats.
- Turn off location sharing from your Apple ID or Google account — only after reaching physical safety, because this sends the abuser a notification that sharing has ended.
- Do not bring the old (monitored) phone to a shelter or safe house. Either leave it at the former home (so it shows your old location) or carry it but keep it powered off. The new phone is your primary communication device.

**Communication security.**
- Signal on the new phone for all sensitive communications with advocates, attorneys, and trusted supporters.
- Enable disappearing messages (1-week default) on all Signal conversations.
- Enable Signal's Registration Lock (Settings > Account > Registration Lock) to prevent re-registration of your number by anyone else.
- New email address only for legal, financial, and support communications. Do not access old email from new devices.

**Financial account security.**
- Log into shared bank accounts and note the balance. Withdraw your share of accessible funds in cash or transfer to your new independent account. If joint funds are accessible and safe to withdraw, do so before the abuser can drain them. Many abusers drain joint accounts immediately upon learning of a separation.
- Contact your bank's fraud line to flag potential account takeover if you believe the abuser will attempt to lock you out.
- File a credit freeze at all three bureaus: Equifax (equifax.com), Experian (experian.com), TransUnion (transunion.com). Credit freezes are free, take effect immediately, and prevent new credit inquiries from revealing your new address.

**Restraining order filing.** Emergency protective orders (EPO) can be requested from law enforcement on the scene of an incident. Temporary restraining orders (TRO) can be filed at the courthouse, usually without an attorney, using the court clerk's forms. DV legal advocates can assist with emergency TRO filing same-day. Keep a copy of any protective order on your person and provide copies to your shelter, children's school, and workplace.

**Children and pet safety.** Bring children's critical documents (birth certificates, insurance cards, school records). Notify children's schools that a protective order is in place and provide instructions limiting the abuser's access. Pet-friendly shelters are available through DomesticShelters.org; Safe Havens for Pets coordinates foster care for pets when shelter accommodation is not available.

**Smart home device reset.** If you are leaving a home with smart devices that the abuser can monitor remotely (cameras, smart locks, smart speakers), you will be unable to change the account credentials from within the abuser's account. If you have access to a smart home account you control, change passwords from the new device. Smart home devices at the former shared residence remain under the abuser's control; this is a concern for former housemates or if children have supervised visits there.

### Phase 3: Ongoing Protection — The First 90 Days

After immediate physical safety is established, Phase 3 maintains security while navigating the legal and logistical complexity of the early separation period.

**Monthly device security audits.** Periodically scan the new device and vehicle for hardware trackers (iOS 17.5+ background scanning active; Android "Unknown Tracker Alerts" in Google Play Services). Check the new phone for unfamiliar apps, unusual battery drain, unexpected data usage, and unknown Accessibility Services on Android. The Coalition Against Stalkerware (stopstalkerware.org) maintains a list of detection tools.

**Financial monitoring.** Once the credit freeze is in place, monitor your credit report at AnnualCreditReport.com. Abusers sometimes file fraudulent credit applications or utility accounts in the survivor's name. Sign up for free credit monitoring alerts on the accounts you control.

**Data broker opt-outs.** After establishing a new address: submit opt-out requests to LexisNexis (optout.lexisnexis.com — the most important, as LexisNexis serves skip tracers and private investigators), Spokeo (spokeo.com/optout), BeenVerified (beenverified.com/app/optout/search), and WhitePages (whitepages.com/suppression-requests). California residents: use the DROP platform (privacy.ca.gov/drop/) for one-stop opt-out from 100+ brokers. Incogni ($7.99/month) automates ongoing resubmission quarterly — appropriate for survivors who cannot allocate time to manual opt-outs.

**Address Confidentiality Program enrollment.** Most states operate Address Confidentiality Programs (ACPs) that provide a substitute mailing address. The ACP address appears on voter registration, DMV records, court documents, and employment records — not your real location. Available in approximately 38 states; contact your state's Attorney General's office or a DV advocate for enrollment. California's program is California Safe at Home (Safe.Ca.Gov); Washington State's is SafePlace (sos.wa.gov/address-confidentiality). This is especially critical when the abuser has law enforcement database access.

**Legal proceedings support.** Maintain documentation of all violations of the protective order: screenshots of messages (with timestamps), call logs, physical evidence. Document in Signal "Note to Self" (end-to-end encrypted). Report violations to law enforcement; file violation reports with the court that issued the order. A DV legal advocate can help escalate if law enforcement is not responding appropriately.

**Counseling and trauma support.** RAINN (1-800-656-4673 | rainn.org) provides free counseling referrals. The National DV Hotline (1-800-799-7233) can refer to local trauma counselors. Many DV shelters provide on-site counseling for residents. SAMHSA's National Helpline (1-800-662-4357) connects survivors with mental health and substance use services when trauma intersects with other needs.

**Employment stability.** Notify an HR contact or trusted supervisor if a protective order is in place and the abuser may attempt to contact you at work or appear at the workplace. In California, Washington, New York, Illinois, and Florida (and most other states), employers are prohibited from retaliating against DV survivors for taking leave for safety planning, medical care, legal proceedings, or relocation. Federal FMLA applies when the DV situation creates a serious health condition for the employee or a covered family member.

### Phase 4: Recovery and Rebuilding — 3–6 Months and Beyond

Phase 4 addresses long-term threat reduction, autonomy restoration, and community reintegration.

**Threat reassessment.** Is the abuser incarcerated? Has the protective order been extended or made permanent? Has there been a custody resolution? Each of these changes the threat model. A DV advocate or legal aid attorney can help assess current risk level and whether additional security measures can be relaxed.

**Cybersecurity maintenance.** Password rotation on all major accounts (annually or after any suspected compromise). Device software updates kept current — updates patch vulnerabilities that stalkerware may exploit. Annual review of account recovery options (recovery phone and email should still be the new, independent credentials, not any account the abuser could access).

**Social media presence rebuild.** Create new accounts (or new profile names) with a middle name or nickname if desired. Set all profiles to private. Disable location tagging on all platforms. Search your own name and new address in major people-search sites (Spokeo, BeenVerified, WhitePages) to assess what is visible about your new location to someone searching for you. Resubmit opt-outs as needed.

**Support group engagement.** DV survivor peer networks (many organized through local shelters and DV organizations) provide community, practical advice, and normalization of the recovery experience. See Section 6 for peer support resources.

**Regaining financial autonomy.** The National Foundation for Credit Counseling (NFCC, nfcc.org) provides free or low-cost financial counseling, including credit rebuilding after economic abuse. Many DV programs include economic empowerment services: employment assistance, vocational training, emergency financial assistance, and housing stability support.

---

## Section 3: Tools and Services Per Phase

### Phase 0 Tools (Pre-Separation)

- **Tails OS** (tails.boum.org): A live operating system on a USB drive that leaves no trace on the host computer and routes traffic through Tor. Use at library computers for safety planning research. Free. Provides full deniability.
- **Library or friend's computer**: Zero-footprint access to resources. Use private browsing mode. Do not log into personal accounts.
- **ProtonMail** (proton.me): End-to-end encrypted email, no phone number required for account creation, accessible from any browser. Create from a safe network.
- **Paper-based planning**: A written safety plan kept at a trusted friend's home is not hackable. Some survivors maintain a written list of phone numbers, shelter addresses, and document locations with a trusted person.

### Phase 1 Tools (Separation Planning)

- **Prepaid "burner" phone**: Cash purchase at Walmart, Walgreens, CVS, Target, or Dollar General. No ID required. $25–$70 for a no-contract Android.
- **Prepaid SIM**: Tracfone, Mint Mobile, Cricket, or Boost Mobile. Cash purchase. New number not linked to the abuser's family plan.
- **Signal** (signal.org): End-to-end encrypted messaging and calls. Register with the new prepaid number. Enable Registration Lock and disappearing messages.
- **Ente Photos** (ente.io): End-to-end encrypted cloud photo backup. Unlike iCloud or Google Photos, inaccessible to anyone who obtains your main account credentials. Free tier available.
- **Bitwarden** (bitwarden.com): Open-source password manager. Install on new device only. Stores unique strong passwords for all new accounts. Free tier available.

### Phase 2 Tools (First 72 Hours)

- **iOS 17.5+ Tracker Detection**: Settings > Privacy & Security. Background scanning for AirTags and other unwanted trackers. Automatic alerts. No additional app required.
- **Google Unknown Tracker Alerts**: Built into modern Android via Google Play Services. Settings > Safety & Emergency > Unknown Tracker Alerts.
- **Android Tracker Detect app** (Apple, free): For older Android devices without built-in Google alerts. Manual scan for AirTags.
- **Credit Freeze**: Equifax.com, Experian.com, TransUnion.com. Free. Immediate effect. PIN-controlled temporary lift. File at all three — one freeze does not cover the others.
- **DomesticShelters.org** (domesticshelters.org/search): 3,000+ U.S. and Canadian shelter programs; filterable by services, language, pet accommodation. Find-a-shelter function does not require account creation.
- **Safe Havens for Pets** (safehavensforpets.org): Locates pet-friendly shelters and foster care for pets, for survivors who cannot leave a pet behind.
- **OurFamilyWizard** (ourfamilywizard.com) or **TalkingParents** (talkingparents.com): Court-admissible custody communication platforms. All messages timestamped and uneditable. Appropriate for documented co-parenting communications when a protective order is in place.

### Phase 3 Tools (First 90 Days)

- **LexisNexis opt-out** (optout.lexisnexis.com): Most critical data broker opt-out. LexisNexis serves skip tracers and private investigators.
- **Incogni** (incogni.com): $7.99/month subscription that automates quarterly data broker opt-out resubmissions across 100+ brokers.
- **AnnualCreditReport.com**: Free federal credit report monitoring. Check for fraudulent accounts opened in your name.
- **iMazing Spyware Analyzer** (imazing.com): Analyzes iPhone and iPad backups for known spyware indicators. Useful for confirming device compromise before replacement.
- **Coalition Against Stalkerware** (stopstalkerware.org): Stalkerware detection resources and list of partner antimalware tools for Android.
- **SAMHSA National Helpline**: 1-800-662-4357 (free, 24/7 mental health and substance use referrals).

### Phase 4 Tools (Recovery)

- **NFCC** (nfcc.org): Free and low-cost financial counseling, credit rebuilding, debt management after economic abuse.
- **Address Confidentiality Program**: State-specific enrollment. Provides substitute mailing address for DMV, voter registration, court records. Approximately 38 states. Contact thehotline.org for your state's program.
- **DROP Platform** (privacy.ca.gov/drop/): California residents only. One-stop data broker opt-out from 100+ brokers including LexisNexis.

---

## Section 4: Integration with Phase 1 OPSEC Playbook

The Phase 1 OPSEC Playbook (opsec-playbook.md) is designed for government surveillance threats: Palantir data linking, NSA signals intelligence, FBI investigative tools, and law enforcement data brokers. Most of its Tier 1 and Tier 2 recommendations apply to DV survivors, with specific modifications.

### 4.1 Where the DV Context Modifies Phase 1 Advice

**Device backup**: The Phase 1 playbook recommends encrypted cloud backups for data continuity. In the DV context: **do not restore from any backup made on the abuser's platform**. An iCloud or Google Drive backup made while stalkerware was active can re-install stalkerware if restored to a new device. Use Ente Photos for specific document and photo backup, not full device backup.

**Password manager**: Phase 1 recommends Bitwarden. In the DV context, install Bitwarden only on the new burner device, never on the old (potentially compromised) device. A keylogger on the old device would capture the Bitwarden master password.

**Signal configuration**: Phase 1's Tier 2 Signal guidance — username mode, "Who can find me by my number" set to Nobody — applies fully. For DV survivors, there is an additional consideration: enable Signal's "Screen Lock" so that the contents of Signal cannot be read by someone who briefly handles the new phone without unlocking it.

**Tor/VPN**: Phase 1's Tier 3 recommendation to route Signal through Tor is appropriate for DV survivors who have reason to believe the abuser has technical sophistication (for example, if the abuser works in technology or law enforcement and has monitoring tools beyond commercial stalkerware). For most DV contexts, Signal on a clean device over any WiFi network the abuser does not control provides adequate protection.

**GrapheneOS**: Phase 1's Tier 3 device hardening recommendation (GrapheneOS on a Pixel phone) provides the highest security for Android. For DV survivors who are technically comfortable, GrapheneOS is worth considering for the permanent replacement device — especially when the abuser has law enforcement database access or technical skills.

### 4.2 Phase-Specific Activation Checkpoints

The following Phase 1 OPSEC checkpoints activate DV-specific protocols:

**Checkpoint: "Do you believe your current device is compromised?"**
- If YES → Do not use the current device for any safety planning. Activate the burner device protocol (Section 2, Phase 1). Do not remove monitoring software from the current device without advocate support.

**Checkpoint: "Are you on a shared phone plan?"**
- If YES → Assume carrier-level location is visible to the primary account holder (the abuser, if they hold the plan). Carry the burner phone for all sensitive communications. Do not port the number to a new plan until after exit and a safety plan is in place.

**Checkpoint: "Does the abuser have your Apple ID or Google account credentials?"**
- If YES → A new device linked to the same Apple ID or Google account gives the abuser continued monitoring access through iCloud or Google account syncing. The new device must be set up with entirely new accounts.

**Checkpoint: "Is the abuser in law enforcement?"**
- If YES → Address Confidentiality Program enrollment is mandatory. File protective orders in a county where the abuser has no professional connections. Document all law enforcement interactions (officer name, badge number, agency, date, content). Contact DV Leap (dvleap.org) — specializing in DV cases with law enforcement defendants.

### 4.3 Threat Escalation Triggers and Response Protocols

**Trigger: Abuser locates shelter address**
Response: Notify shelter staff immediately. Shelter staff activate relocation protocol. Contact advocate to file police report and note violation of protective order if one is in place. Do not share new location by phone or message on any channel the abuser may have accessed. Switch to a different Signal account if you suspect the current number was discovered.

**Trigger: Abuser attempts to access new bank account or files fraudulent account**
Response: File a police report for identity theft or fraud. Contact the financial institution's fraud department. File an FTC identity theft report at identitytheft.gov. Place a fraud alert (distinct from a freeze) at all three credit bureaus.

**Trigger: Abuser serves process through custody proceedings that requires disclosure of address**
Response: Contact legal aid immediately. Address Confidentiality Program addresses can be used in court filings in most states. A DV legal advocate or attorney can file a motion to keep the address confidential in custody proceedings when safety is at risk.

**Trigger: New AirTag or tracker found after Phase 2 sweep**
Response: Document the tracker with photos before removing it (evidence for protective order violation if one is in place). Do not remove it if you are not ready to alert the abuser that it was found; instead, coordinate removal timing with advocate. File a police report.

**Trigger: Monitoring software found on new device**
Response: The new device may have been physically accessed by the abuser. Replace it again (do not factory reset — see Phase 1 device principle). File a police report for unauthorized access.

---

## Section 5: Legal and Institutional Safeguards

### 5.1 Protective Order Mechanics

Protective orders (also called restraining orders, orders of protection) legally prohibit the abuser from contacting, approaching, or appearing within a specified distance of the survivor. Violation is a criminal offense. Emergency Protective Orders (EPO) can be issued by law enforcement at the scene. Temporary Restraining Orders (TRO) are issued ex parte (without the abuser present) by courts, typically within 24–72 hours. Permanent protective orders follow a full hearing.

**Federal baseline**: Under VAWA, all states must honor protective orders issued in other states (full faith and credit provision). An order issued in California is enforceable in Texas.

**Technology-specific provisions**: When filing for a protective order, specifically request language prohibiting: electronic monitoring (including stalkerware), accessing your electronic accounts, location tracking, sharing intimate images, and contacting you through third parties or digital platforms. Most state courts can grant these provisions; DV advocates can help draft the specific language.

**State variation — five examples**:

- **California (AB 2024, 2025)**: Courts must grant all protective orders meeting minimum requirements; filing may be done electronically; remote hearing appearance permitted; survivor may file in any location rather than only the abuse jurisdiction. Orders now extendable up to 15 years (AB 2308).
- **Texas**: Texas Family Code allows for Emergency Protective Orders issued by judges or magistrates on the night of an arrest. Violation of a protective order is a Class A misdemeanor for a first offense; a third degree felony for a third or subsequent offense. Texas does not have a statewide address confidentiality program as broadly accessible as California's; some survivor address protection is available through the Secretary of State's program.
- **New York**: Family Court and Supreme Court both have jurisdiction. New York's Order of Protection can include electronic monitoring prohibitions. Family Court Act § 812 provides broad DV definitions. Legal aid organizations across New York state provide free representation.
- **Florida (Fla. Stat. § 741.30)**: Florida issues "injunctions for protection against domestic violence." Florida law (§ 741.313) provides DV workplace protections including leave and accommodation rights. Florida's domestic violence hotline: 1-800-500-1119. Note: the former Florida Coalition Against Domestic Violence (FCADV) underwent organizational transition; the Florida Partnership to End Domestic Violence (FPEDV.org) is the current state coalition.
- **Illinois**: Illinois Domestic Violence Act provides broad protections including order of protection available in civil, criminal, and juvenile court contexts. Illinois has an Address Confidentiality Program (Safe Homes Act). Legal Aid Chicago and Prairie State Legal Services provide statewide coverage.

**The enforcement gap**: The Supreme Court ruled in Town of Castle Rock v. Gonzales (2005) that domestic violence victims do not have a federal constitutional right to police enforcement of their protective orders. State legislatures bear responsibility for creating enforceable police response standards. Survivors in states with weak mandatory response laws should document non-enforcement and contact a DV legal advocate who can escalate through civil rights litigation.

### 5.2 DV Shelter Network

DomesticShelters.org provides the largest searchable database of DV programs in the U.S. and Canada (3,000+ programs). Shelters maintain confidential addresses — providing only a phone intake number publicly, with address disclosed only to accepted residents. This confidentiality is legally protected in most states. Shelters typically provide: emergency housing (usually 30–90 days), safety planning, legal advocacy, counseling, children's services, and referrals. Some provide immigration services.

**Pet accommodation**: As of 2025, approximately 18–25% of U.S. DV shelters are pet-friendly. The "25 by 2025" campaign (25by2025.org) has moved this number from 10% in 2010. For pets that cannot be accommodated at a shelter, Safe Havens for Pets (safehavensforpets.org) and local animal shelters with DV boarding programs can provide temporary foster care.

**Confidentiality protocols**: Shelters operate with strict confidentiality. Do not share the shelter address with anyone who might inadvertently disclose it. Do not post photos that show the facility's interior or surroundings. Do not receive packages at the shelter address under your real name without clearing it with shelter staff first.

### 5.3 Law Enforcement Engagement

Mandatory reporting laws vary by state. All states require law enforcement to respond to DV calls; most require written reports. Mandatory arrest laws (requiring arrest when probable cause exists for DV) exist in approximately 22 states and D.C. Law enforcement discretion failures remain a documented problem: survivors from marginalized communities (Black women, Indigenous women, undocumented immigrants, LGBTQ+ survivors) face disproportionate dismissal. Victim advocacy organizations within law enforcement agencies (specialized DV units, victim advocates embedded in police departments) generally provide better outcomes than patrol officers for follow-up.

If the responding officer dismisses your report or declines to make an arrest despite visible evidence: request a supervisor, document the officer's name and badge number, and contact a DV legal advocate. A legal advocate can file a formal complaint and in some cases engage civil rights litigation for police failures.

### 5.4 Legal Aid Resources

Legal aid organizations provide free or low-cost DV legal representation including protective orders, divorce, custody, housing, and immigration matters. Income eligibility is typically 125–200% of federal poverty level ($19,563 for individual; $40,188 for family of four in 2025 at 125%).

- **LawHelp.org**: National directory of free legal aid by state (lawhelp.org). Enter your state to find local organizations.
- **DOJ Legal Assistance for Victims (LAV) Program**: Provided $36.38 million in 2025 to 51 organizations providing direct civil and criminal legal services to DV, sexual assault, stalking, and dating violence victims.
- **State bar association referrals**: Most state bars have lawyer referral services with DV specialists.
- **University law clinics**: Law school family law and DV clinics provide free representation; available in most major metro areas.
- **WomensLaw.org**: State-by-state legal guides for DV law, custody, immigration, and protective orders. Legal email hotline for survivors without access to a local organization.

### 5.5 Workplace Protections

**Federal FMLA**: When DV creates a serious health condition (physical injury, diagnosed mental health condition, need for inpatient or continuing treatment), FMLA provides up to 12 weeks of job-protected unpaid leave per year for eligible employees (employers with 50+ employees; employee with 12+ months tenure). DV leave under FMLA can cover medical treatment, counseling, or court appearances if the health condition requirement is met.

**State-level protections** (selected):
- **California (AB 2499, effective January 1, 2025)**: Employers of all sizes must provide reasonable accommodations for DV victims and their family members; defines "victim" broadly to include DV, sexual assault, stalking, and any violent crime; protects employees from retaliation for taking leave.
- **Washington State**: Employers must provide reasonable safety accommodations to DV/sexual assault/stalking survivors and their qualifying family members; leave available for safety planning, medical care, legal proceedings, relocation, and seeking protective orders.
- **New York**: NYS Human Rights Law provides protections; NYC has additional protections under the NYC Human Rights Law.
- **Florida (§ 741.313)**: DV leave up to 3 days per year for employees of 50+ headcount employers.
- **Illinois**: Illinois Victims' Economic Security and Safety Act (VESSA) provides leave for DV/sexual assault/stalking survivors at employers with 15+ employees (up to 8 weeks/year) and at employers with 50+ employees.

**Workplace location privacy**: Workplace addresses are potentially visible through data brokers, LinkedIn, and employment records. For survivors concerned about the abuser learning the workplace address, a DV advocate can advise whether to notify HR and implement a safety plan (security briefing, visitor policy, parking safety review) or whether to seek new employment at a less known location.

### 5.6 Healthcare Provider Mandatory Reporting

Healthcare providers' mandatory reporting requirements for DV vary by state. Most states do not require mandatory reporting of adult DV (as distinguished from child abuse, which is universally mandated). However, gunshot wounds and injuries consistent with violence require reporting in most states. For undocumented survivors: healthcare providers are not immigration enforcement agents and are generally not required to report immigration status. However, the fear of reporting to healthcare providers remains a documented barrier to care access. Federally Qualified Health Centers (FQHCs) are required to serve patients regardless of immigration status and are generally safe healthcare settings for undocumented DV survivors.

### 5.7 Immigration and DV Intersection

**VAWA Self-Petition**: Allows victims of abuse by a U.S. citizen or Lawful Permanent Resident spouse, parent, or adult child to petition for immigration status independently, without the abuser's knowledge or cooperation. Filed on Form I-360 (no filing fee). USCIS will not notify the abuser of the application and will not request information from the abuser. Evidence includes: documentation of the abuse (police reports, medical records, protective orders, letters from advocates); proof of the relationship to the abuser; proof of shared residence; statement of good moral character. December 2025 USCIS policy manual update maintained the existing standards for battery and extreme cruelty.

**U Visa**: Available to victims of certain crimes (including DV, sexual assault, and stalking) who have suffered substantial mental or physical abuse and are helpful to law enforcement or prosecutors. Requires law enforcement certification (Form I-918B). Provides 4 years of temporary nonimmigrant status and work authorization; eligible for adjustment to permanent residence after 3 years. Waitlist is long; consult with an immigration attorney immediately if this option applies.

**T Visa**: Available to victims of human trafficking. If the DV situation involved labor trafficking or sex trafficking, the T visa is a separate pathway. Contact the National Human Trafficking Hotline (1-888-373-7888) for assessment.

**Resources**:
- ASISTA (asistahelp.org): Immigration technical assistance for DV advocates
- National Immigrant Women's Advocacy Project (NIWAP): Provides legal resources and training on VAWA, U visa, and T visa
- American Immigration Lawyers Association (AILA, aila.org): Referral service to qualified immigration attorneys
- KIND (Kids in Need of Defense, supportkind.org): For DV situations involving unaccompanied children or children with immigration needs

**ICE enforcement and DV**: Abusers have used threats of ICE reporting as a coercive control mechanism. VAWA's confidentiality provisions prevent DHS from disclosing that a survivor has filed a VAWA petition. Undocumented survivors can access DV shelters and services regardless of immigration status. Law enforcement agencies in many jurisdictions have policies against ICE referrals from DV calls, but practice varies. A DV advocate familiar with your jurisdiction can advise on the current local enforcement environment.

---

## Section 6: Peer Support and Community Coordination

### 6.1 Trusted Friend and Family Activation

Not everyone in a survivor's social network should know the full safety plan — over-informing creates risk if mutual friends inadvertently disclose details to the abuser or are directly questioned. The practical guidance:

**What to share with trusted supporters**: Where you are going (general area, not specific shelter address); what they can do to help (temporary housing, transportation, storage of documents or a bag); that they should not share your location with anyone including family members they trust unless you have specifically authorized it; the National DV Hotline number in case they are contacted by the abuser or law enforcement. The phrase "I need you to trust my judgment about what information is safe to share and when" establishes the ground rule.

**What not to share**: Shelter address. New phone number on the first day (share it once you are confident the channel is secure). Plans that are still in motion. Financial account details.

**Practical support roles**: Trusted supporters can hold cash reserves, store documents, provide transportation on exit day, provide temporary housing for the first night before a shelter opens, watch pets, or pick up children from school under a coordinated plan.

### 6.2 DV Survivor Peer Support Networks

Peer support from other survivors provides community, practical knowledge, and normalization of the recovery experience. Peer advisors are not advocates or attorneys — they cannot provide legal advice or professional safety planning, but they can share experience and reduce isolation.

- **Local DV shelter peer groups**: Most shelters offer facilitated peer support groups for current and former residents. These are the most appropriate setting for peer advice — conducted within a trauma-informed framework with staff oversight.
- **Online survivor communities**: The National DV Hotline hosts online survivor forums. RAINN's online support group (rainn.org/get-help/online-hotline) connects survivors to peer support. Be cautious about privacy in online spaces: do not share location or identifying details in any public or semi-public forum; use a screen name not connected to your real identity.
- **Teen DV**: loveisrespect.org (part of the National DV Hotline network) provides resources and peer support for teens and young adults experiencing dating violence.

### 6.3 Community Response Templates

For neighbors, coworkers, and community members who want to help a survivor:

**If you suspect a neighbor is experiencing DV**: Do not directly confront the abuser. The National DV Hotline (1-800-799-7233) can advise on how to offer help without escalating danger. A simple, private note to the survivor: "I'm here if you need anything. No questions asked. Here's my number." — offered when the abuser is not present — can open a door without creating risk.

**If you are a coworker**: Report concerns to HR with DV-specific language ("I'm concerned for a colleague's safety"). Many employers have Employee Assistance Programs (EAPs) with DV counseling referrals. Do not attempt to mediate with the abuser. If the abuser appears at the workplace, notify security and HR immediately.

**If you are a family member being contacted by the abuser for the survivor's location**: The phrase "I don't know where she is" is always the appropriate answer, even if you do. The survivor's location is protected information. Do not share it without the survivor's explicit advance authorization.

### 6.4 Mutual Aid Activation

DV situations frequently involve financial precarity, housing instability, childcare gaps, and transportation barriers simultaneously. Mutual aid networks can fill gaps where formal services have waitlists or eligibility requirements.

- **Housing**: Many DV organizations provide transitional housing (3–24 months) following emergency shelter. National Alliance to End Homelessness (endhomelessness.org) coordinates transitional housing resources. Local mutual aid networks (community.find mutual aid at mutualaidhub.org) sometimes provide emergency housing support.
- **Childcare**: Local DV coalitions frequently coordinate emergency childcare while survivors attend legal proceedings, job interviews, or medical appointments. Head Start programs (acf.hhs.gov/ohs) provide early childhood education with income-based eligibility that may apply during a transition period.
- **Employment support**: YWCA (ywca.org) provides employment readiness programs for DV survivors in many cities. Dress for Success (dressforsuccess.org) provides professional attire. Local workforce development programs (workforce.gov) provide job training and placement.
- **Transportation**: Many DV shelters provide transportation to appointments. Lyft and Uber have partnerships with some DV organizations for rides to shelters. Local mutual aid networks sometimes coordinate ride shares.

### 6.5 Faith Community Engagement

Faith communities can be significant sources of support, housing, childcare, and transportation. DV-competent faith leaders understand that leaving an abusive relationship is not a violation of faith commitments and support survivors actively. Red flags for faith communities that are not DV-competent: pressure to reconcile without safety conditions, counseling the survivor on submission or forgiveness as a prerequisite to safety, treating the DV situation as a "private family matter," or providing couple's counseling (which can increase danger by giving the abuser information about the survivor's disclosures).

- **FaithTrust Institute** (faithtrustinstitute.org): Provides training for faith communities on DV response; can help locate DV-trained clergy in your area.
- **Faith leaders as safe people**: A DV-trained pastor, rabbi, imam, or religious leader can provide sanctuary, witness to a protective order, and advocacy with law enforcement.
- **Religious trauma intersection**: For survivors from religious communities where the abuser used religious authority as a control mechanism, specialized counseling addressing religious trauma alongside DV trauma is available through RAINN referrals and some DV counseling programs.

---

## Section 7: Resource Directory

### National Hotlines

| Resource | Contact | Hours | Notes |
|---|---|---|---|
| **National Domestic Violence Hotline** | 1-800-799-7233 | 24/7 | Text START to 88788; chat at thehotline.org; TTY 1-800-787-3224 |
| **National Sexual Assault Hotline (RAINN)** | 1-800-656-4673 | 24/7 | rainn.org/get-help; chat available |
| **Crisis Text Line** | Text HOME to 741741 | 24/7 | Silent; no call required |
| **loveisrespect (Teen DV)** | 1-866-331-9474 | 24/7 | loveisrespect.org; text LOVEIS to 22522 |
| **SAMHSA National Helpline** | 1-800-662-4357 | 24/7 | Mental health and substance use; free; confidential |
| **National Human Trafficking Hotline** | 1-888-373-7888 | 24/7 | safeline@polarisproject.org; text 233733 |
| **Florida DV Hotline** | 1-800-500-1119 | 24/7 | Spanish available |
| **Texas DV Hotline** | 1-800-525-1978 | 24/7 | Texas Council on Family Violence |

### State DV Coalitions (Selected)

| State | Coalition | Website |
|---|---|---|
| California | California Partnership to End Domestic Violence | cpedv.org |
| Texas | Texas Council on Family Violence | tcfv.org |
| New York | New York State Coalition Against Domestic Violence | nyscadv.org |
| Florida | Florida Partnership to End Domestic Violence | fpedv.org |
| Illinois | Illinois Coalition Against Domestic Violence | ilcadv.org |
| Washington | Washington State Coalition Against Domestic Violence | wscadv.org |
| Georgia | Georgia Coalition Against Domestic Violence | gcadv.org |
| Massachusetts | Jane Doe Inc. | janedoe.org |
| Michigan | Michigan Coalition to End Domestic & Sexual Violence | mcedsv.org |
| Pennsylvania | Pennsylvania Coalition Against Domestic Violence | pcadv.org |
| Ohio | Ohio Domestic Violence Network | odvn.org |
| Wisconsin | End Domestic Abuse Wisconsin | endabusewi.org |
| Puerto Rico | Coordinadora Paz para las Mujeres | pazparalasmujeres.org |

Full list of 56 state and territorial coalitions: nnedv.org/content/state-u-s-territory-coalitions/

### National Organizations

- **NNEDV (National Network to End Domestic Violence)**: nnedv.org — leads network of 56 state/territory coalitions and 2,000+ member programs
- **NNEDV Safety Net Project**: techsafety.org — intersection of technology and DV; stalkerware resources; state-specific technology safety guides
- **NCADV (National Coalition Against Domestic Violence)**: ncadv.org — statistics, policy, state coalition directory
- **Futures Without Violence**: futureswithoutviolence.org — healthcare provider training; workplace programs; reached 20+ million people in 2025
- **DomesticShelters.org**: domesticshelters.org — searchable shelter database (3,000+ programs)
- **WomensLaw.org**: womenslaw.org — state-by-state legal information on DV law, protective orders, custody
- **Coalition Against Stalkerware**: stopstalkerware.org — stalkerware detection tools and victim resources
- **FaithTrust Institute**: faithtrustinstitute.org — DV resources for faith communities
- **DV Leap**: dvleap.org — specializes in DV cases involving law enforcement defendants

### Technology and Privacy

- **NNEDV Safety Net Project**: techsafety.org/resources-survivors — technology safety planning for survivors
- **Coalition Against Stalkerware**: stopstalkerware.org/information-for-survivors — stalkerware detection and removal guidance
- **iMazing Spyware Analyzer**: imazing.com/blog/spyware-analyzer-redux — iPhone/iPad spyware analysis
- **Crash Override Network**: (formerly active; resources archived at archive.org) — online harassment documentation and response
- **Privacy Rights Clearinghouse**: privacyrights.org — data broker opt-out guides and privacy resources
- **EFF Surveillance Self-Defense (DV)**: ssd.eff.org — security guides including DV scenario

### Legal Aid Resources

- **LawHelp.org**: lawhelp.org — national directory of free legal aid by state; enter state for local DV legal organizations
- **DOJ Legal Assistance for Victims Program**: justice.gov/ovw/legal-assistance-victims-program — federal funding program (51 grantee organizations in 2025; $36.38M awarded)
- **Legal Services Corporation (LSC)**: lsc.gov — federal funder of civil legal aid; funded programs serve households at or below 125% FPL
- **WomensLaw.org Legal Email Hotline**: womenslaw.org/find-help/legal-information-hotlines — for survivors without access to local legal organizations
- **ASISTA**: asistahelp.org — immigration legal assistance for DV survivors; VAWA and U visa technical assistance

### Financial Resources

- **National Foundation for Credit Counseling (NFCC)**: nfcc.org — free and low-cost financial counseling; credit rebuilding after economic abuse
- **Allotment.org**: allotment.org — financial resources curated for DV survivors
- **NNEDV Economic Justice resources**: nnedv.org/content/economic-justice — policy and practical economic empowerment for survivors
- **Amalgamated Bank**: amalgamatedbank.com — established policies for DV survivors opening accounts
- **FTC Identity Theft Recovery**: identitytheft.gov — step-by-step recovery plan for survivors experiencing financial identity theft by an abuser

### Immigration-Specific Resources

- **ASISTA**: asistahelp.org — VAWA and U visa technical assistance for DV organizations and survivors
- **National Immigrant Women's Advocacy Project (NIWAP)**: niwap.org — legal resources, training, VAWA/U visa/T visa guidance
- **American Immigration Lawyers Association (AILA)**: aila.org — lawyer referral service; find an immigration attorney with DV experience
- **KIND (Kids in Need of Defense)**: supportkind.org — immigration legal services for children and youth
- **CAIR Legal Defense Fund**: cair.com/legal — legal representation and resources for civil rights matters including immigration intersections
- **WomensLaw.org — Immigration**: womenslaw.org/laws/federal/immigration — plain-language VAWA self-petition, U visa, T visa guides
- **USCIS VAWA Self-Petition**: uscis.gov/green-card/green-card-eligibility/green-card-for-vawa-self-petitioner — official government information

### Children and Family

- **National Child Traumatic Stress Network (NCTSN)**: nctsn.org — resources on DV exposure in children; trauma-informed care guidelines
- **Childhelp National Child Abuse Hotline**: 1-800-422-4453 | childhelp.org — for situations involving child abuse within a DV household
- **loveisrespect.org**: loveisrespect.org — teen and young adult DV resources; peer support
- **Head Start**: acf.hhs.gov/ohs — early childhood education with income-based eligibility; stable environment for young children during DV recovery
- **OurFamilyWizard** / **TalkingParents**: ourfamilywizard.com / talkingparents.com — court-admissible co-parenting communication platforms for custody situations

### Workplace Resources

- **DOL FMLA resources**: dol.gov/agencies/whd/fmla — official FMLA employer and employee guides
- **Catalyst Legal (FMLA + DV)**: catalystlegal.org/fmla-domestic-violence-leave-what-employers-employees-should — plain-language FMLA and DV leave explainer
- **Workplace Fairness**: workplacefairness.org/domestic-violence-workplace — state-by-state guide to DV workplace protections
- **EEOC**: eeoc.gov — employer obligation information; ADA intersections with DV trauma

---

## Section 8: Key Messaging for NNEDV Distribution

### 8.1 Tone Principles

This playbook is designed for survivors navigating an already difficult situation, often with limited time, limited resources, and limited trust in institutions. The tone throughout must reflect these realities.

**Non-judgmental**: Every section acknowledges that leaving is complicated and dangerous, and that survivors make rational decisions about timing. The phrase "when and if you are ready" is not a hedge — it is accurate. This playbook does not pressure survivors to act.

**Trauma-informed**: The guide acknowledges that survivors may be managing trauma responses that affect decision-making, memory, and energy. Instructions are written to be comprehensible under stress: short sentences, numbered checklists, bolded key actions. Redundancy is intentional — a survivor should not need to read the whole document to find the one relevant action.

**Practically grounded**: Every recommendation includes a specific product name, phone number, or URL. "Get a safe phone" is not actionable. "Purchase a prepaid Android phone with cash at Walmart, Walgreens, CVS, Target, or Dollar General for $25–$70 — no ID required" is actionable.

**Honest about limits**: This guide is explicit that protective orders are not physical barriers, that law enforcement does not always respond appropriately, that data broker opt-outs require time to propagate, and that no technology measure is a substitute for physical safety. False reassurance increases risk.

### 8.2 Entry Point for Undecided Survivors

The most important message for survivors who are not ready to leave:

> "You do not have to make any decisions right now. This guide is a reference — a map of options you can use if and when you need them. Reading it does not commit you to anything. Understanding what is possible makes your own choices clearer. Nothing here requires you to act before you are ready."

This framing is supported by research on DV decision-making: survivors who access information and resources months before leaving are better prepared for exit than those who act without preparation. The goal of distribution is not to prompt immediate action — it is to ensure that every survivor has the map.

### 8.3 Accessibility Requirements

**Short-form version (for mobile and text sharing)**: A 1-page version with only the hotline numbers, the 5-item "most important actions" summary, and the DomesticShelters.org URL is appropriate for text-based distribution (hotline SMS follow-up, shelter notice boards, social media). The full document is a reference, not an SMS.

**Long-form version (for desktop and shelter use)**: This document, in its current form, is appropriate for shelter resource libraries, legal aid intake offices, and advocate training.

**Visual decision tree**: A simplified flowchart covering "Is my device safe to use for planning?" → "Do I have a safety plan?" → "What do I do in the next 24 hours?" is appropriate for distribution in formats where dense text is inaccessible (flyers, shelter bulletin boards, healthcare waiting rooms).

**Language access**: Priority translation languages for NNEDV distribution are Spanish, Mandarin, Vietnamese, and Arabic — reflecting the language demographics of the largest DV-affected populations not served in English. State coalitions in high-concentration language communities (CPEDV in California, TCFV in Texas) can advise on local language prioritization.

**Accessibility for disabilities**: Survivors with cognitive disabilities, vision impairments, or hearing impairments face additional barriers. NNEDV's Safety Net Project has specific resources for survivors with disabilities (techsafety.org); the hotline provides TTY access (1-800-787-3224) and ASL video services.

### 8.4 Explicit Limitations for Distribution Messaging

Every distribution of this document should include this statement:

> "This playbook cannot replace a domestic violence advocate or attorney. The safety steps described here carry real risks — including the risk of escalating danger if used at the wrong time or in the wrong sequence. Use this guide alongside professional support, not instead of it. Your local DV organization can walk through this with you. The National Domestic Violence Hotline (1-800-799-7233) is available 24 hours a day, 7 days a week."

### 8.5 NNEDV Pilot Distribution Recommendations

For the June/July 2026 NNEDV pilot:

1. **Pilot with 3–5 member programs** before broad distribution: select programs with technology-safety specialists on staff who can provide feedback on accuracy and usability.
2. **Advocate pre-briefing**: Distribute to advocates 2 weeks before survivor distribution. Advocates should be able to navigate the document before guiding survivors through it.
3. **Feedback collection**: Use a simple 3-question survey (What was most useful? What was confusing? What was missing?) with pilot program staff after 30 days.
4. **Version control**: Date-stamp all distributions. The technology landscape (specific apps, carrier policies, state laws) changes rapidly; this document requires quarterly review.
5. **Measurement**: Track advocate use frequency, survivor questions generated, and whether technology safety documentation is appearing more frequently in protective order petitions (a proxy for increased technology-safety awareness among advocates).

---

## Quick-Reference Checklists

### Checklist A: Before Leaving (Complete with Advocate)

- [ ] Contact DV advocate: National DV Hotline 1-800-799-7233 or text START to 88788
- [ ] Complete safety plan before any technology changes
- [ ] Purchase cash burner phone ($25–$70, no ID required, Walmart/Walgreens/CVS/Target)
- [ ] Purchase prepaid SIM with cash (Tracfone, Mint Mobile, Cricket)
- [ ] Create new ProtonMail or Tutanota email from safe device/network
- [ ] Create new Apple ID or Google account linked only to new email
- [ ] Install Signal on new phone; enable Registration Lock and disappearing messages
- [ ] Install Ente Photos on new phone; back up critical documents
- [ ] Open new bank account at institution abuser does not use
- [ ] Build small cash reserve (small ATM withdrawals over time, store at safe external location)
- [ ] Photograph all critical documents (SSN card, birth certificates, passport, health insurance)
- [ ] Identify ACP program in your state
- [ ] Physically check vehicle for AirTags and Bluetooth trackers

### Checklist B: Day Of / First 72 Hours

- [ ] Leave old (monitored) phone at home OR carry it powered off
- [ ] Use new phone only for all communications
- [ ] Take: identity documents, medications, cash reserve, children's documents
- [ ] Contact advocate to confirm safe arrival
- [ ] Place credit freeze at Equifax.com, Experian.com, TransUnion.com
- [ ] Turn off location sharing (Apple Find My, Google Maps, Life360) from new device — only after reaching physical safety
- [ ] Check new vehicle for hardware trackers
- [ ] File for emergency protective order with advocate assistance
- [ ] Notify children's school of protective order; provide a copy
- [ ] File police report if applicable; document officer name, badge number

### Checklist C: First 90 Days

- [ ] Open new independent phone plan (remove from abuser's family plan)
- [ ] Complete data broker opt-outs: LexisNexis, Spokeo, BeenVerified, WhitePages
- [ ] California: DROP platform at privacy.ca.gov/drop/
- [ ] Enroll in state Address Confidentiality Program
- [ ] Enable 2FA on all new accounts (new phone number for authentication)
- [ ] Monthly: check new accounts for unfamiliar logins
- [ ] Monthly: scan for AirTags and hardware trackers
- [ ] Attend counseling or trauma support (RAINN referral: rainn.org)
- [ ] Contact legal aid for protective order extension or related proceedings: lawhelp.org
- [ ] Review ACP status; notify of any address changes

### Checklist D: Ongoing Safety Maintenance

- [ ] Every 90 days: resubmit data broker opt-outs (or maintain Incogni subscription)
- [ ] Annually: rotate passwords on all major accounts; review account recovery contacts
- [ ] Keep software on new device updated (security patches close vulnerabilities)
- [ ] Reassess threat level with advocate when circumstances change (custody resolution, abuser release, etc.)

---

## Emergency Contact Summary

| Resource | Contact |
|---|---|
| National DV Hotline | 1-800-799-7233 / Text START to 88788 / thehotline.org |
| RAINN (Sexual Assault) | 1-800-656-4673 / rainn.org |
| Crisis Text Line | Text HOME to 741741 |
| loveisrespect (Teen DV) | 1-866-331-9474 |
| SAMHSA Mental Health | 1-800-662-4357 |
| National Trafficking Hotline | 1-888-373-7888 |
| LawHelp.org | lawhelp.org (legal aid by state) |
| DomesticShelters.org | domesticshelters.org/search |
| NNEDV Safety Net | techsafety.org/resources-survivors |

---

## Sources

- [NNEDV Safety Net Project — Technology Safety](https://nnedv.org/content/technology-safety/)
- [NNEDV Safety Net Project — Resources for Survivors](https://www.techsafety.org/resources-survivors)
- [NNEDV Safety Net Project — Virtual Tech Summit 2025](https://nnedv.org/content/safety-nets-virtual-tech-summit-2025/)
- [NNEDV State and U.S. Territorial Coalitions](https://nnedv.org/content/state-u-s-territory-coalitions/)
- [Coalition Against Stalkerware — Information for Survivors](https://stopstalkerware.org/information-for-survivors/)
- [AV-Comparatives Stalkerware Test 2025](https://av-comparatives.org/tests/stalkerware-test-2025/)
- [Gen Digital — Fighting Back Against Tech-Related Abuse (2026)](https://www.gendigital.com/blog/impact/community/stalking-awareness-month-2026)
- [Cybernews — How AirTag is fueling domestic violence](https://cybernews.com/editorial/apple-airtag-domestic-violence/)
- [Tech Safety Canada — Technology-Facilitated Gender-Based Violence](https://techsafety.ca/resources/toolkits/what-is-technology-facilitated-gender-based-violence)
- [USCIS — Green Card for VAWA Self-Petitioner](https://www.uscis.gov/green-card/green-card-eligibility/green-card-for-vawa-self-petitioner)
- [USCIS Policy Manual Update — VAWA Self-Petitioners (December 2025)](https://www.uscis.gov/sites/default/files/document/policy-manual-updates/20251222-VAWASelf-Petitioners.pdf)
- [WomensLaw.org — VAWA Self-Petitions](https://www.womenslaw.org/laws/federal/immigration/vawa-abuse-victims/vawa-self-petitions/basic-info-about-vawa-self-2)
- [ASISTA — VAWA Self-Petition](https://www.asistahelp.org/vawa-self-petition)
- [California AB 2499 — Victim Leave Expansions (effective January 2025)](https://ogletree.com/insights-resources/blog-posts/california-expands-leave-and-protections-for-victims-of-violence/)
- [Washington State — Domestic Violence Leave](https://www.lni.wa.gov/workers-rights/leave/domestic-violence-leave)
- [Florida Statutes § 741.313 — DV Workplace Protections](https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0700-0799%2F0741%2FSections%2F0741.313.html)
- [Catalyst Legal — FMLA and Domestic Violence Leave](https://catalystlegal.org/fmla-domestic-violence-leave-what-employers-employees-should/)
- [DOJ Office on Violence Against Women — Legal Assistance for Victims Program](https://www.justice.gov/ovw/legal-assistance-victims-program)
- [LawHelp.org — Find Free Legal Help](https://www.lawhelp.org/resource/legal-aid-and-other-low-cost-legal-help)
- [DomesticShelters.org — Search Shelters](https://www.domesticshelters.org/search)
- [Safe Havens for Pets](https://www.safehavensforpets.org/)
- [25 by 2025 — Pet-Friendly DV Shelters](https://25by2025.org/)
- [Futures Without Violence — 2025 Impact Report](https://futureswithoutviolence.org/news/2025-impact-report/)
- [NCADV — State Coalitions](https://ncadv.org/state-coalitions)
- [WomensLaw.org — General Restraining Orders](https://www.womenslaw.org/laws/general/restraining-orders)
- [California Courts — Domestic Violence Restraining Orders Overview](https://courts.ca.gov/sites/default/files/courts/default/2024-08/overview.pdf)
- [Washington Courts — Domestic Violence Manual for Judges (December 2025)](https://www.courts.wa.gov/content/manuals/domViol/chapter8.pdf)
- [ACLU — Supreme Court Ruling on Domestic Violence Orders of Protection](https://www.aclu.org/press-releases/aclu-disappointed-supreme-court-ruling-domestic-violence-orders-protection)

---

**Version**: 1.0
**Created**: May 26, 2026
**Next review**: August 26, 2026 (quarterly)
**Distribution**: NNEDV pilot — June/July 2026
**Cross-references**: `opsec-playbook.md` (Phase 1 integration); `phase-2-immigration-surveillance-evasion-playbook.md` (ICE/VAWA); `phase-2-financial-resistance-security-playbook.md` (economic independence); `phase-2-dv-survivor-safety-playbook.md` (device/stalkerware detail); `phase-2-dv-survivor-security-playbook.md` (account/financial/location detail)
