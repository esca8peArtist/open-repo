---
title: "Domestic Violence Survivor Security Playbook: Escaping Intimate Partner Surveillance, Building Digital Independence, and Safe Exit Planning"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2
version: 1.0
depends_on:
  - opsec-playbook.md
  - phase-2-dv-survivor-safety-playbook.md
confidence: high — grounded in NNEDV Safety Net Project documentation (half of victim service providers report partner use of phone stalkerware), Coalition Against Stalkerware 2025 Annual Report, AV-Comparatives 2025 Stalkerware Test, Gen Digital Stalking Awareness Month 2026 report, Apple/Google unwanted tracking specification, Apple Support AirTag documentation, Tech Safety Canada survivor guide to location tracking, NNEDV Virtual Tech Summit 2026, myPlan DV safety resource, iMazing documentation, National DV Hotline technology safety resources, Congressional Tech Safety for DV Victims Act (2025–2026)
audience: Domestic violence survivors planning exit; DV advocates, shelter staff, and safety planning counselors; hotline workers providing technology safety planning; legal advocates and attorneys representing DV survivors
word_count: ~3,900
safety_notice: CRITICAL — Read this before any other action. Removing stalkerware, changing account security, or altering location sharing can immediately alert an abusive partner and escalate danger. This guide must be used with a safety plan and with the support of a domestic violence advocate. Contact the National Domestic Violence Hotline (1-800-799-7233 or text START to 88788) before taking any technical steps. If your current device may be monitored, use a device your abuser does not know about — a library computer, a friend's device, or a phone purchased with cash — to access this guide and contact advocates. thehotline.org is accessible via chat on any device.
---

# Domestic Violence Survivor Security Playbook

**For DV advocates and shelter staff**: This playbook is designed to be worked through together with a survivor, not handed over as a standalone document. Technology safety without a completed safety plan is incomplete and potentially dangerous. The National Network to End Domestic Violence's Safety Net Project reports that approximately half of victim service providers document abusers using phone applications to stalk their partners. This is the norm, not the exception. Your role is to assess which technical measures are appropriate given the survivor's specific situation and timeline.

**The structural difference from all other playbooks in this corpus**: Every other playbook in this series addresses a threat actor who is external to the target's life. The DV survivor's threat actor is intimate — they know the target's routines, have had access to devices and accounts, may share legal financial relationships, and may be in law enforcement or have law enforcement relationships. Standard "hardening" approaches address perimeter defense; the DV survivor must rebuild from inside a perimeter that has been fully compromised.

---

## Section 1: Threat Model — The Intimate Adversary

The abusive partner's threat capabilities are categorically different from government or corporate surveillance:

| Capability | Government/Corporate | Intimate Partner |
|---|---|---|
| Device access | Requires legal process or exploit | Had physical device access; may have installed stalkerware during normal use |
| Account access | Requires warrants or cooperation | Knows passwords; set up family plans; is the account owner |
| Location knowledge | Requires metadata correlation | Has direct knowledge of routines, frequent locations, vehicle |
| Social network | Must build through OSINT | Already knows the target's family, friends, colleagues, and advocates |
| Financial access | Requires financial institution cooperation | May have joint accounts, be listed on credit cards, or control primary account |
| Legal mechanisms | Works with law enforcement | May have law enforcement connections; custody orders and civil proceedings are weaponizable |

The threat model is not "someone is monitoring your device." It is "someone with significant pre-existing intimate access has embedded surveillance into your daily life and knows exactly what changed if anything changes."

### 1.1 Stalkerware — The Primary Surveillance Mechanism

**What it is**: Commercial stalkerware applications — including mSpy, FlexiSPY, Hoverwatch, Cocospy, and dozens of others — are sold for as little as $30/month as "parental monitoring" or "employee monitoring" tools. They require one-time physical access to the target device for installation. They run in background with no visible icon on iOS (when using MDM profiles) or disguised as a system utility on Android.

**What stalkerware captures** (varies by product):
- Real-time GPS location (updates every 1–15 minutes)
- All call logs with duration and contact identity
- All text messages, including SMS and iMessage
- Screen capture capability in some products, capturing content from Signal, WhatsApp, Snapchat, and other encrypted apps
- Keystroke logging: captures everything typed, including passwords as they are entered
- Camera and microphone activation (available in FlexiSPY and select others)
- Browser history
- Photos and videos

**The 2025–2026 escalation**: AirTag stalking cases rose from 57 in 2018 to nearly 600 by end of 2024, with a 1,034% increase in coercive control cases involving tracking technology. The Coalition Against Stalkerware's 2025 annual report documented 14,000+ cases reported through partner organizations — and that number substantially undercounts unreported cases.

**The survivor's dilemma**: Removing stalkerware without a safety plan triggers a notification on many products when the monitoring feed goes dark. The abuser learns that the device is no longer monitored — which may signal a planned exit and cause escalation. **Never remove stalkerware without a safety plan and advocate support.**

### 1.2 Hardware Location Trackers — AirTags and Alternatives

**AirTags**: Apple AirTags transmit Bluetooth signals that are detected by nearby Apple devices and reported to the AirTag owner's Find My account. An AirTag hidden in a car, bag, jacket lining, or child's backpack allows precise continuous location tracking without any software on the target's device.

**Detection**: iPhones running iOS 14.5+ receive automatic alerts if an unknown AirTag has been traveling with them for 8–24 hours. Android users can download the "Tracker Detect" app (Android 6.0+) for manual scanning, or receive automatic alerts if running Google's detection service. The 8–24 hour alert window means an AirTag placed in the morning may not trigger an alert until that evening.

**Apple/Google industry standard**: Apple and Google released an industry specification for unwanted tracking detection in 2024, incorporated into iOS 17.5+ (automatic background scanning) and Android's "Unknown Tracker Alert" feature. This is the current most reliable detection method for Apple ecosystem trackers.

**Non-Apple trackers**: Tile, Samsung SmartTag, and commodity Bluetooth trackers may not trigger the Apple/Google unwanted tracking alerts. Manual scanning with dedicated apps (Tile app, Samsung SmartThings) or a Bluetooth scanner app can detect these.

**Physical search guidance**: Common hiding spots in vehicles — wheel wells (magnetic), under bumpers, in trunk lining, under driver's seat, inside children's car seats, inside the spare tire well. In belongings: bag lining, jacket pockets, purse interior pockets, inside children's toy or backpack. A hardware store sweep involves physically checking all of these locations.

### 1.3 Shared Account Surveillance — The Account Ownership Problem

**Family sharing plans**: Many survivors are on the abuser's phone plan as a secondary line. The primary account holder has access to call logs, text message records (if using the carrier's messaging apps), and data usage patterns through the carrier's account portal. Sprint/T-Mobile, Verizon, and AT&T all provide these records to primary account holders.

**iCloud Family Sharing / Google Family Link**: If the survivor's Apple ID is part of an iCloud Family group controlled by the abuser, the abuser has access to location sharing, app purchase history, and the ability to screen time reports. "Screen Time" controls can also be used to monitor usage remotely.

**Find My / Google Maps location sharing**: Many couples share location as a matter of routine convenience. If location sharing was enabled voluntarily during the relationship, the abuser continues to receive location data until sharing is revoked. Revoking sharing is visible to the other party — they receive a notification that sharing has ended. This action should be part of a coordinated safety plan, not a spontaneous one.

**Account recovery access**: The abuser may be listed as an account recovery contact for email, financial, and social media accounts. Account recovery contact access allows resetting the target's password and taking over the account. Review all account recovery contacts as part of the digital safety plan.

### 1.4 Financial Surveillance — Control Through Money

**Joint accounts**: Access to joint bank accounts gives the abuser real-time visibility into spending: what was purchased, where, and when. Many banks offer real-time spending alerts. A purchase at a gas station 30 miles from home reveals a location.

**Credit card monitoring**: If the abuser is the primary cardholder on a supplemental credit card held by the survivor, every transaction generates a notification to the primary holder. This is real-time location and behavior surveillance.

**Credit report access**: In some jurisdictions, abusers have accessed credit reports (legally or through identity theft) to identify the survivor's new address. Credit freeze (available free from Equifax, Experian, and TransUnion) prevents new credit inquiries that could reveal a new address.

**Financial control post-exit**: Some abusers attempt to freeze shared accounts, drain shared accounts, or close credit lines immediately upon learning of an exit, to create financial dependency. Pre-exit steps to establish independent financial access are essential.

---

## Section 2: Safety-First Framework — Technology Safety Requires a Safety Plan

### The Non-Negotiable Sequence

1. **Contact a DV advocate before taking any technical action.** The National DV Hotline (1-800-799-7233 or text START to 88788) or thehotline.org chat connects you with an advocate who can help assess the safety implications of each step.

2. **Safety plan for escalation.** Any change to surveillance infrastructure — turning off location sharing, removing stalkerware, creating a new email account, changing passwords — can be detected and can trigger escalation. The safety plan answers: where do you go if escalation occurs? Who do you call? What do the children do?

3. **Timing matters.** Technology changes are safest to implement when you have physical separation from the abuser — a stay at a shelter, a visit to a family member's home, or after the abuser leaves for work. Do not make changes when the abuser could notice the change in real time and confront you before you have a path to safety.

4. **Not everything needs to be addressed immediately.** Some surveillance (financial monitoring, family plan membership) can continue temporarily without immediate danger while a longer-term exit is planned. Maintaining the appearance of normalcy while building toward exit is a legitimate safety strategy.

---

## Section 3: Creating an Independent, Untraceable Digital Life

### 3.1 New Phone — The Foundation

The safest approach to a compromised device is not remediation — it is replacement. A new device, acquired without the abuser's knowledge, purchased with cash, and set up with entirely new accounts creates a clean break.

**Acquisition**:
- Purchase a prepaid "burner" phone with cash at a big-box retailer, pharmacy, or convenience store. No-contract Android phones are available for $25–$70. No ID is required for cash purchase of a prepaid device with a prepaid SIM.
- Do not use a loyalty card or credit card for the purchase. Cash only.
- Common retailers: Walmart, Walgreens, CVS, Target, Dollar General.

**SIM selection**:
- A prepaid SIM (Tracfone, Mint Mobile, Cricket, Boost Mobile) purchased with cash requires no ID at purchase. The phone number is not registered to your real name.
- Do not port your existing phone number to the new device — the port request is visible to the current carrier account holder (the abuser, if they are the primary account holder).
- The new phone has a new number that the abuser does not know.

**Account setup**:
- Create a new email address (Gmail, ProtonMail, or Tutanota) using the new phone, connected to a WiFi network the abuser does not monitor (a library, shelter, or friend's home)
- Do not log in to any accounts the abuser knows about on the new device
- Do not connect the new phone to your existing Google or Apple account — this would sync contacts, location history, and app purchase records to the shared account
- For app downloads: create a new Google account or Apple ID associated with the new email address

### 3.2 Account Security Reconstruction

On the new device, rebuild essential accounts from scratch:

**Email**: ProtonMail (protonmail.com) or Tutanota (tutanota.com) for a new primary email that the abuser has no access to. These services offer end-to-end encryption and do not require a phone number for account creation.

**Password manager**: Bitwarden (bitwarden.com) with a strong master password (16+ characters, not a phrase the abuser could guess) stores new unique passwords for every account. Install only on the new device — never on the old device.

**Signal for secure communication**: Install Signal on the new phone. Register with the new phone number. Verify safety numbers with advocates, attorneys, and trusted contacts. Enable disappearing messages (recommended: 1 week) for all sensitive conversations.

**Account recovery contact audit** (do separately, on the new phone): For every account the abuser might have recovery access to (your main email, bank, social media), update the recovery contact to the new email address and new phone number. Do this systematically before taking any visible exit action — the abuser may attempt to take over your accounts through recovery access when they realize you are leaving.

### 3.3 The Existing Phone — What to Do With It

The safest approach to the old (potentially compromised) device:
- **Keep using it normally** during the planning period, so that the abuser's surveillance shows expected patterns. A suddenly idle phone is a red flag.
- **Never discuss the exit plan on the old device**, even in what you believe are encrypted apps — stalkerware with screen capture can read Signal messages as they appear on screen.
- **At exit time**: either leave the old phone at the home (which prevents its use for phone tracking your new number) or carry it to maintain location plausibility if the safety plan requires you to appear to be at a certain location temporarily.
- **Do not perform a factory reset on the old phone** before leaving — this destroys evidence of stalkerware installation that may be useful in legal proceedings. Forensic documentation of stalkerware on the old device can support a protective order application.

### 3.4 Location Hygiene — Disconnecting the Tracking Web

The sequence for disabling location tracking should be coordinated with exit timing:

**AirTag and hardware tracker check (before exit)**:
- Physical sweep of vehicle, bag, and belongings (see Section 1.2)
- Enable iOS 17.5+ unwanted tracker scanning (Settings > Privacy & Security > Tracking > Allow Tracking alerts)
- Android: Install "Tracker Detect" from the Google Play store and run a manual scan
- Have a trusted advocate or friend help with the physical vehicle sweep — a second set of eyes and hands for wheel wells and trunk spaces

**Find My / Google Maps sharing (coordinate with exit)**:
- Disable Find My sharing from your Apple ID settings at the same time as or after reaching physical safety
- Remove the abuser from any shared Google Maps location group
- Note: the abuser will be notified that sharing has stopped. This should happen after you have reached a safe location.

**Family phone plan (coordinate with exit)**:
- Contact the carrier to establish your own account using your new email and, if possible, a shelter or advocate's address as the service address
- Port your old number to the new account (if you want to keep the number) — this is detectable by the abuser; time with your safety plan
- Alternatively: abandon the old number entirely and use the new prepaid number

---

## Section 4: Financial Independence — Breaking Economic Control

### 4.1 Independent Banking Before Exit

Open an account at a financial institution the abuser does not use, using an address (a shelter, P.O. box, or advocate's address) that is not your current home:

- Many banks allow account opening with a shelter address or c/o address
- Community credit unions (not national banks) have lower automated fraud flags for new accounts with non-standard addresses
- Amalgamated Bank (amalgamatedbank.com) has established policies for DV survivors

**Account opening documentation**: Bring your government ID (driver's license or passport), your Social Security number, and a document establishing the new address (a shelter intake letter, a letter from an advocate organization, or a utility bill from a safe address). If you do not have documentation of a new address, many banks will accept a statement from a DV advocate.

**Initial funding**: A small initial deposit (even $25) from a money order (purchased with cash at a pharmacy or post office) establishes the account without a check from a joint account that the abuser could see.

### 4.2 Cash Reserve — Pre-Exit Financial Security

Build a cash reserve for immediate post-exit needs before leaving:

- Withdraw small amounts from ATMs over time, not a large single withdrawal that would be noticed
- Store cash in a location only you know about — not in the shared home, but with a trusted advocate, in a safety deposit box at a bank the abuser does not use, or at a DV shelter intake
- Emergency expenses for the first 72 hours post-exit: gas, food, medications, temporary housing deposit

**SNAP/EBT cards**: If you receive SNAP benefits, the EBT card is in your name and is accessible independently. Keep it on your person.

### 4.3 Credit Freeze — Protecting Your New Address

When you establish a new address, place a credit freeze at all three major bureaus (Equifax, Experian, TransUnion) to prevent new credit inquiries that would reveal your address to anyone (including the abuser or a skip tracer hired by the abuser):

- Equifax: equifax.com/personal/credit-report-services/credit-freeze
- Experian: experian.com/freeze/center.html
- TransUnion: transunion.com/credit-freeze

A credit freeze is free, takes effect immediately, and can be temporarily lifted (for a housing application, for example) with a PIN you set at the time of the freeze. Freeze all three bureaus, not just one.

**Address confidentiality programs (ACP)**: Most states have Address Confidentiality Programs that provide a substitute mailing address to DV survivors — a program address that appears on official records instead of your real address. This prevents the abuser from obtaining your address through voter registration, court records, DMV records, or utility company records. Contact your state Attorney General's office for ACP enrollment.

### 4.4 Cryptocurrency for Financial Independence (Limited Application)

Prepaid cards purchased with cash provide the most accessible financial independence for most survivors. Cryptocurrency is relevant for a narrower set of situations:

**When it applies**: If the abuser monitors all financial accounts closely and the survivor needs to receive money from advocates or family members without a transaction record, a Monero wallet (see `phase-2-financial-resistance-security-playbook.md`) allows receiving value without creating a bank record. This is appropriate for receiving small amounts from trusted supporters, not for general financial management.

**When it does not apply**: If the survivor is not technically comfortable with cryptocurrency, the risks of error outweigh the benefits. A prepaid cash card from a pharmacy is simpler, more accessible, and adequate for most post-exit financial needs.

---

## Section 5: Communication With Advocates Without Location Exposure

### 5.1 Signal for Advocate Communication

Signal on the new prepaid phone (Section 3.1) provides encrypted communication with DV advocates, attorneys, and trusted supporters. Key settings:

- **Registration lock**: Enable in Signal Settings > Account > Registration Lock. This prevents someone who knows your new number from re-registering Signal with it (which would expire your current session).
- **Disappearing messages**: Set 1-week disappearing messages on advocate conversations. This ensures that if the new phone is seized, conversation history is minimized.
- **Note to self for document storage**: Use Signal's "Note to Self" feature to store important photos (court documents, custody paperwork, evidence) encrypted on Signal's servers. These are accessible only with your Signal account and are not visible to anyone with access to your device (they are cloud-synced with Signal's end-to-end encryption).

### 5.2 Location-Safe Calling

When calling the DV Hotline or advocates from the new phone, location safety considerations:
- Do not call from your home (if monitored via location tracking)
- Do not call from your workplace (if you are concerned the abuser knows your work location)
- Safe calling locations: library, shelter, advocate's office, a location unfamiliar to the abuser
- Keep the new phone on airplane mode unless actively communicating — apps on any phone can send location data when connected to a network

**911 location exposure**: If you call 911 from a cell phone, your location is transmitted to the dispatcher. This is by design for emergency response. If you are in immediate danger, call 911 regardless of location exposure. If you are planning and not in immediate danger, call the DV Hotline (which does not receive your location) rather than 911.

### 5.3 Communication With Children's Schools and Custody Matters

**School notification**: If there is a custody order or protective order restricting the abuser's access to children, provide a copy to the school directly and ask that the abuser not be provided with information about pickup schedules or child location without court authorization. Schools typically comply with protective orders.

**Custody order and location**: If there is a custody order that requires regular communication with the abuser, establish a specific, narrow channel: a shared email account managed through your new email, or a legal firm-mediated communication system (platforms like OurFamilyWizard, Talking Parents, or AppClose record all messages and prevent deletion — useful for documenting harassment within custody communication).

---

## Section 6: Law Enforcement Entanglement — Abuser in Law Enforcement

When the abusive partner is employed in law enforcement, additional risks apply:

**Access to databases**: A law enforcement officer has access to address databases, DMV records, and law enforcement information networks that are not publicly accessible. An abusive partner who is a police officer can query databases to find new addresses, vehicle registrations, and employer information without triggering any external scrutiny.

**Credibility asymmetry**: Law enforcement officers have institutional credibility that affects how domestic violence reports are received by colleagues and supervisors. The survivor's report of abuse may be minimized or handled differently when the abuser is on the force.

**Recommended mitigation**:
- File reports with a law enforcement agency other than the abuser's employing department — a neighboring jurisdiction's department, a state-level law enforcement agency, or (for federal violations) the FBI
- Contact the local DV civil legal aid organization — organizations like DV Leap (dvleap.org) specialize in DV cases involving law enforcement defendants
- Document all law enforcement interactions, including officer name, badge number, agency, date, and what was said
- Address Confidentiality Programs (Section 4.3) are particularly critical when the abuser has database access
- Consider requesting a protective order from a court in a county where the abuser has no professional connections

---

## Section 7: Incident Response — If the Abuser Detects Exit Preparations

### Immediate Safety Response

**If the abuser becomes aware of exit plans while you are still in the home**:
1. Call 911 if there is immediate physical danger.
2. Text or call your safety plan contact (established in your safety plan with your advocate).
3. Leave if it is safe to do so. Take children. Take medications, identification documents (driver's license, passport, Social Security card, birth certificates for children), a small amount of cash, and the new phone if it is safely accessible.
4. Do not argue or try to explain. Physical safety is the priority.
5. Go to the pre-designated safe location: a shelter, a friend's home, or a family member's home that the abuser does not know.

**Identification documents**: If original documents are not accessible, replacements can be obtained: driver's license through DMV, Social Security card through SSA, birth certificate through the state vital records office. Many jurisdictions waive fees for DV survivors.

### Device Management During an Escalation

If you must leave quickly while the old (potentially monitored) phone is still the only phone you have:
- Do not communicate with advocates or attorneys on the old phone during an escalation event
- Use a public phone, a library computer, or a friend's device to contact the DV Hotline (1-800-799-7233) or your advocate
- The old phone's location is visible to the abuser. Do not leave it at a shelter or safe house location if you are still using the old phone.

---

## Section 8: Stalkerware Detection and Documentation

### If You Suspect Stalkerware But Have Not Left Yet

**Do not remove it yet** — removal may trigger an alert and cause escalation. Instead, document it:

1. Note any signs of stalkerware: battery draining faster than usual, device running hot when idle, data usage higher than expected, device occasionally lighting up when not in use.

2. Contact the Coalition Against Stalkerware (stopstalkerware.org) — they have a partner network of DV advocates who specialize in technology safety and can advise on the specific product and appropriate response.

3. Contact your DV advocate about getting a safety assessment. National DV Hotline: 1-800-799-7233.

4. If you have left and the device is no longer in the abuser's control: take the device to a DV technology safety specialist or forensic examiner recommended by your advocate. iMazing (imazing.com) has a "Spyware Analyzer" for iOS devices. AV-Comparatives' 2025 stalkerware test identified which Android AV products reliably detect common stalkerware applications.

**Evidence preservation**: The forensic documentation of stalkerware on the old device is evidence supporting a protective order, a civil suit, and potentially criminal stalking charges. Do not factory reset the old device — preserve it as evidence and have it examined by a qualified forensic examiner.

---

## Section 9: Scenario Playbooks

### Scenario A: Early Planning Stage — Exit Is Months Away

**Context**: Survivor is still in the home and relationship. Abuser monitors the phone and financial accounts. Survivor needs to build resources and make a safety plan without triggering detection.

**Actions (all on a new device, outside the home, on unfamiliar WiFi)**:
1. Contact DV Hotline and establish an advocate relationship
2. Create new email (ProtonMail) and Signal account on a cash-purchased prepaid phone kept hidden
3. Begin saving small cash amounts over time
4. Open a separate bank account at a community credit union not used by the abuser, using a shelter or advocate address
5. Place credit freeze at all three bureaus
6. Research Address Confidentiality Program in your state
7. Keep all of this on the new phone; say nothing on the old phone or joint accounts
8. Continue normal patterns on the old device to maintain surveillance baseline

**What not to do**: Change passwords, revoke location sharing, or remove apps on the old device. Make no changes on monitored devices or accounts during this phase.

### Scenario B: Imminent Exit — Safe Window Available

**Context**: Survivor has a 24–48 hour window when the abuser is away (travel, incarceration, hospitalization). Transition to safe housing is possible.

**Priority sequence**:
1. Collect identification documents, medications, children's documents
2. Physically sweep vehicle and belongings for AirTags (see Section 1.2)
3. If time permits: establish new phone with new number, new accounts
4. Transfer cash reserve from safe storage
5. Contact shelter or safe housing to confirm space is available
6. Leave. Do not announce the departure.
7. After reaching safety: revoke location sharing from old accounts (Apple Find My, Google Maps, family sharing), port phone number or change number, notify trusted family/friends of new contact information only
8. Do not carry the old phone to the safe location

### Scenario C: Custody Complications — Child Location Must Be Shared with Court

**Context**: Survivor has left but is in a contested custody situation requiring court-ordered communication about child location with the abuser.

**Communications architecture**:
- Use a court-mediated communication platform (TalkingParents.com or OurFamilyWizard.com) for all custody communication — all messages are logged and preserved, which documents abusive behavior within the custody communication channel
- Provide child location information only as required by the custody order — not more frequently and not through direct communication channels where the abuser can escalate
- If the abuser uses the custody communication channel for threats, document each instance in the platform's record (which creates an admissible record) and report to your attorney and the court

**Address protection**: If the court requires disclosure of your residential address to the abuser, immediately request enrollment in your state's Address Confidentiality Program and ask your attorney to request that the court use the ACP address rather than your physical address in court records.

### Scenario D: Financial Freeze — Abuser Has Drained Shared Accounts

**Context**: Survivor has left and abuser has frozen or drained the shared bank account.

**Immediate steps**:
1. Contact bank fraud department to report unauthorized account access or unauthorized transfers
2. If the abuser is a joint account holder: request emergency account separation and frozen funds documentation from the bank manager (some banks have DV protocols — ask for a "bank manager, DV protocol" call)
3. Emergency financial resources: DV Hotline can provide referrals to emergency financial assistance funds; Catholic Charities, United Way, and state DV coalitions maintain emergency funds
4. File a police report documenting the financial freeze/drain — this creates evidence for civil proceedings
5. Apply for TANF (Temporary Assistance for Needy Families) if the situation qualifies
6. Contact a DV civil legal organization about emergency financial relief through family court (temporary support orders, emergency custody orders that include financial provisions)

---

## Section 10: Tools and Resources

### Hotlines and Direct Support
- **National Domestic Violence Hotline**: 1-800-799-7233 or text START to 88788 or thehotline.org
- **NNEDV Safety Net Project**: techsafety.org — technology safety resources; staff consultation for complex cases
- **Coalition Against Stalkerware**: stopstalkerware.org — stalkerware identification; survivor support
- **DV Leap**: dvleap.org — civil legal representation for DV survivors (including cases involving LEO abusers)

### Technology Safety
- **Tech Safety Canada — Survivor's Guide to Location Tracking**: techsafety.ca/resources/toolkits/a-survivors-guide-to-location-tracking
- **Apple — Detect Unwanted Trackers**: support.apple.com/guide/personal-safety/detect-unwanted-trackers-ips139b15fd9/web
- **Apple — Get Safe Guide**: support.apple.com/guide/personal-safety/get-safe-guide-ipse14bfadaf/web
- **iMazing Spyware Analyzer** (iOS device examination): imazing.com — free device backup and spyware analysis tool
- **myPlan App**: myplanapp.org — safety planning decision support tool for DV survivors

### Communications
- **Signal**: signal.org — encrypted messaging; use on new prepaid device
- **ProtonMail**: protonmail.com — encrypted email; use for new accounts
- **TalkingParents**: talkingparents.com — court-admissible custody communication
- **OurFamilyWizard**: ourfamilywizard.com — custody communication with documentation

### Financial
- **Credit freeze — Equifax**: equifax.com/personal/credit-report-services/credit-freeze
- **Credit freeze — Experian**: experian.com/freeze/center.html
- **Credit freeze — TransUnion**: transunion.com/credit-freeze
- **Amalgamated Bank**: amalgamatedbank.com — mission-aligned banking with DV-survivor-aware policies

### Legal
- **Address Confidentiality Programs by state**: Contact state Attorney General's office; most states maintain ACP programs for DV survivors
- **WomensLaw.org**: womenslaw.org — legal information by state for DV survivors
- **National Center for Victims of Crime**: victimsofcrime.org

---

## Summary: Five Principles That Matter Most

1. **Safety plan before technology action** — a technology change that triggers an abuser response without a safety plan is more dangerous than the surveillance itself. Every technical step in this playbook is secondary to having a plan for where you go and who you call if something escalates.

2. **New device, new accounts, new number** — remediation of a compromised device is harder and less reliable than a clean start. A cash-purchased prepaid phone with new accounts is the foundation of a private communication and account structure the abuser cannot access.

3. **The old phone tells the story you want told** — during the planning period, the old (monitored) device should continue showing expected patterns. The new device is for planning. The old device is for maintaining the behavioral baseline that prevents detection of the exit preparation.

4. **Financial independence requires advance action** — opening an account at an institution the abuser does not use, establishing a cash reserve, and placing a credit freeze should happen before exit, not after. Post-exit financial freezes by an abusive partner are a documented coercion tactic; the countermeasure is pre-exit financial independence.

5. **Stalkerware is evidence** — do not delete or factory-reset a device with potential stalkerware. The forensic record of stalkerware installation supports a protective order, criminal stalking charges, and civil claims. Preserve it; have it examined by a qualified specialist; let your attorney use it.

---

**Version**: 1.0
**Created**: May 9, 2026
**Next scheduled review**: August 9, 2026 (quarterly review)
**Cross-references**: `opsec-playbook.md` (device hardening principles), `phase-2-dv-survivor-safety-playbook.md` (base DV safety guidance), `phase-2-financial-resistance-security-playbook.md` (cryptocurrency for financial independence), `threat-model.md` (commercial surveillance infrastructure)

---

## Sources

- [National Domestic Violence Hotline — Technology Safety Resources](https://www.thehotline.org/resources/technology-safety/)
- [NNEDV Safety Net Project — Cell Phone Safety Plan](https://www.techsafety.org/resources-survivors/cell-phone-safety-plan)
- [NNEDV Safety Net Project — Resources for Survivors](https://www.techsafety.org/resources-survivors)
- [Coalition Against Stalkerware — Information for Survivors](https://stopstalkerware.org/information-for-survivors/)
- [Gen Digital — Stalking Awareness Month 2026: Fighting Back Against Tech-Related Abuse](https://www.gendigital.com/blog/impact/community/stalking-awareness-month-2026)
- [Alliance for Hope — Stalkerware: The Invisible Threat Faced by Domestic Abuse Victims](https://www.allianceforhope.com/news-archive/stalkerware-the-invisible-threat-faced-by-domestic-abuse-victims)
- [Conflict International — The AirTag Epidemic: Countering the Rise of Tech-Enabled Stalking](https://conflictinternational.com/news/the-airtag-epidemic-countering-the-rise-of-tech-enabled-stalking)
- [The Feminism Project — Technology-Facilitated Stalking: How AirTags, Spyware and Apps Trap Women](https://thefeminismproject.com/harder-stuff/technology-facilitated-stalking-how-airtags-spyware-and-apps-trap-women/)
- [Apple Support — What to Do If You Get an Alert That an AirTag Is With You](https://support.apple.com/en-us/119874)
- [Apple Support — Detect Unwanted Trackers](https://support.apple.com/guide/personal-safety/detect-unwanted-trackers-ips139b15fd9/web)
- [Apple Support — Get Safe Guide](https://support.apple.com/guide/personal-safety/get-safe-guide-ipse14bfadaf/web)
- [ProtonVPN — AirTag Stalking: What It Is and How to Protect Yourself](https://protonvpn.com/blog/airtag-stalking)
- [Cybernews — How AirTag Is Fueling Domestic Violence](https://cybernews.com/editorial/apple-airtag-domestic-violence/)
- [Tech Safety Canada — A Survivor's Guide to Location Tracking](https://techsafety.ca/resources/toolkits/a-survivors-guide-to-location-tracking)
- [myPlan App — How to Get a Second Phone for Safe Communication](https://myplanapp.org/blog/a-strategy-for-communication)
- [Domestic Shelters — Guide to Online Stalking](https://www.domesticshelters.org/articles/technology/guide-to-online-stalking)
- [Domestic Shelters — Technology Safety Resources](https://www.domesticshelters.org/domestic-violence-technology-safety-resources)
- [Domestic Shelters — AirTags Can Track Belongings, Also People](https://www.domesticshelters.org/articles/escaping-violence/airtags-can-track-belongings-also-people)
- [WomensLaw.org — Abuse Using Technology: What is Spyware?](https://www.womenslaw.org/about-abuse/abuse-using-technology/ways-survivors-use-and-abusers-misuse-technology/electronic-3)
- [Privacy Guides Community — Geofencing, surveillance and SIM-based tracking in 2026](https://discuss.privacyguides.net/t/geofencing-surveillance-and-sim-based-tracking-in-2026/35239)
- [Journals SAGE — Safeguarding the Internet of Things for Victim-Survivors of Domestic and Family Violence, 2025](https://journals.sagepub.com/doi/10.1177/10778012231222486)
- [Narcissistic Abuse Rehab — Technology Abuse and Stalking After Separation](https://www.narcissisticabuserehab.com/post-separation-stalking-technology-abuse/)
