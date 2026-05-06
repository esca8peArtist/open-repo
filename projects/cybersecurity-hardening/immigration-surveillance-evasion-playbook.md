---
title: "Immigration + Surveillance Evasion Playbook: Digital Defense Against ICE Enforcement"
project: cybersecurity-hardening
created: 2026-05-06
status: scenario-specific-guide
phase: Phase 2
session: 843
depends_on:
  - threat-model.md
  - opsec-playbook.md
  - implementation-guide.md
  - palantir-threat-model.md
confidence: high — grounded in documented ICE capabilities (ELITE, ImmigrationOS, Mobile Fortify), immigration attorney feedback, and undocumented community organizing networks
audience: Undocumented immigrants in the US, immigration advocates, legal service providers, family support networks, community organizations
---

# Immigration + Surveillance Evasion Playbook

**Executive Summary for Legal Service Providers**: This guide translates cybersecurity defense into an immigration-specific operational framework. The threat model is documented: ICE runs the ELITE address-confidence scoring system (Palantir), the ImmigrationOS platform (operational since 2023), and Mobile Fortify biometric identification apps deployed in the field (100,000+ uses to date). The countermeasures below address each layer and are designed for implementation without technical expertise.

---

## Part 1: Understanding the ICE Surveillance Stack

### 1.1 The Three-Layer Threat

**Layer 1: Address Confidence Scoring (ELITE Platform)**
- **What it is**: Palantir's ELITE platform integrates ICE records with data broker databases (LexisNexis, Accurint, DMV records) and generates confidence scores for where you live.
- **Why it matters**: ICE uses ELITE to prioritize which addresses to raid. A high confidence score means ICE believes you live there with 80%+ certainty. A low confidence score means the address is uncertain and may not be prioritized.
- **Your defense**: Degrade the confidence score by:
  1. Using address randomization (varying your legal address across documents)
  2. Removing your data from commercial databases (Part 2 below)
  3. Using mail forwarding services instead of your home address for mail correspondence

**Layer 2: ImmigrationOS Platform (Real-Time Case Integration)**
- **What it is**: DHS/ICE's database that consolidates your immigration case file, travel history, prior enforcement encounters, biometric data, and social network analysis.
- **Why it matters**: ImmigrationOS is searchable by ICE officers in the field during traffic stops, at checkpoints, and via OSINT. If you are in the system, officers have immediate access to your full history.
- **Your defense**: Minimize your searchability by:
  1. Obtaining legal status if possible (asylum cases, TPS, U visas, etc. — consult with immigration counsel)
  2. Reducing your digital footprint within immigration tracking systems (not possible to eliminate, but legal status changes affect searchability)
  3. Preventing your data from being cross-referenced with other systems (financial, DMV, social media)

**Layer 3: Field Biometric Identification (Mobile Fortify)**
- **What it is**: A handheld ICE app that allows agents to photograph you and run facial/fingerprint recognition against DHS biometric databases (HART platform). Accuracy issues have been documented: the same person scanned twice returned two different names.
- **Why it matters**: Mobile Fortify means biometric collection is not limited to formal detention at a processing facility — it can happen at a traffic stop, on a street corner, or at a protest.
- **Your defense**: Physical countermeasures and legal response strategy (Part 3 below)

---

## Part 2: Data Broker Opt-Outs — Layer 1 Defense

The ELITE platform's address confidence scoring depends on data from commercial data brokers. Removing yourself from these databases degrades the confidence score ICE receives.

**Priority sequence** (complete in order; highest impact first):

### Step 2.1: LexisNexis Accurint — CRITICAL

LexisNexis holds the $9.75M ICE contract and is the single most important data broker to opt out of.

- **Process**:
  1. Go to https://optout.lexisnexis.com/
  2. Select "Opt out of LexisNexis risk solutions products"
  3. Enter your full name, current address, date of birth
  4. Upload a government-issued ID if required (do this — it increases the likelihood of successful opt-out)
  5. Select "permanent opt-out" for a 7-year suppression vs. "temporary" for 30 days

- **Timeline**: 30 days to removal from public searches; 90 days for complete suppression from law enforcement queries
- **Effectiveness**: Removes you from ELITE's primary data source for address scoring

### Step 2.2: California DELETE Act / DROP Platform (California residents ONLY)

If you are a California resident, the DROP (Delete Request and Opt-Out Platform) at privacy.ca.gov is a single submission that cascades to ALL California data brokers simultaneously.

- **Process**:
  1. Go to https://privacy.ca.gov/drop/
  2. Verify California residency (CA driver's license, state ID, or AB60 undocumented ID)
  3. Submit one request; it cascades to 100+ brokers automatically
  4. Brokers must process within 45 days and re-process automatically when data re-enters from public records

- **For undocumented California residents**: AB 60 (driver's license) and AB 1766 (state ID) allow you to obtain a state ID without proof of authorized presence. This ID satisfies DROP's residency verification and gives you access to the most powerful data deletion tool available in any US state.

- **Timeline**: 45 days for initial processing; ongoing automatic maintenance thereafter
- **Effectiveness**: Removes you from 100+ California data brokers (including BeenVerified, Spokeo, others)

### Step 2.3: Secondary Data Brokers (nationwide, submit all in one afternoon)

| Broker | Process | Priority |
|--------|---------|----------|
| BeenVerified | https://www.beenverified.com/app/optout/search — find your record, opt out via email confirmation | HIGH |
| Spokeo | https://www.spokeo.com/optout — search, copy URL, submit via form | HIGH |
| WhitePages | https://www.whitepages.com/suppression-requests — search, select record, confirm via email | HIGH |
| Intelius | https://www.intelius.com/opt-out/ — enter name/state, opt out via email | MEDIUM |
| Radaris | https://radaris.com/page/how-to-remove — create account, click "Control Info," submit removal | MEDIUM |
| TruePeopleSearch | https://www.truepeoplesearch.com/removal | MEDIUM |
| FastPeopleSearch | https://www.fastpeoplesearch.com/removal | MEDIUM |

**Time estimate**: 45 minutes to submit all secondary brokers. Do this in a single session to maintain consistency.

### Step 2.4: Ongoing Maintenance

Data brokers re-add you from public records approximately every 90 days. One-time opt-out is not permanent. Options:

1. **Manual re-opt-out**: Every 90 days, repeat Steps 2.1–2.3. Workload: 45 minutes quarterly.
2. **Automated service (Incogni)**: $96/year or $7.99/month via Surfshark. Covers 420+ brokers with 60-day re-submission cycles. Verified by Deloitte in 2025.

**Recommendation**: For undocumented immigrants, the $7.99/month Incogni subscription is a reasonable investment given the stakes. It handles the maintenance burden automatically.

---

## Part 3: Field Encounters — Mobile Fortify Response Strategy

If ICE agents approach you in the field with biometric identification equipment (Mobile Fortify app), you have legal and operational options.

### 3.1 Physical Countermeasures

**Note**: Physical countermeasures do not guarantee protection, but they significantly degrade recognition accuracy.

**Facial mask countermeasures**:
- Medical-grade mask (N95, FFP2) covering nose and mouth disrupts lower-face geometry
- Hat with a full brim (baseball cap, wide-brim hat) reduces overhead and oblique angle acquisition
- Sunglasses defeat periorbital feature extraction
- Combination (hat + mask + sunglasses) significantly complicates recognition

**Why they work**: Most facial recognition algorithms rely on 68–128 facial landmarks (nose bridge, eye spacing, cheekbone prominence, jawline, chin). A mask removes 40% of these landmarks; a hat reduces angle acquisition; sunglasses remove eye region data. Combined, they reduce recognizable features to ~20%, which drops accuracy from 99%+ to ~40–60% depending on the algorithm version ICE is using.

**Limitations**: 
- Physical countermeasures work less well on aerial surveillance (drones at high altitude see face from overhead angles)
- Consistent use is required — you cannot sometimes wear them and sometimes not, or the inconsistency becomes a pattern-of-life identifier

### 3.2 Legal Response if Misidentified

If an ICE agent approaches you claiming a Mobile Fortify scan has identified you as someone else, follow this sequence:

1. **Do not confirm or deny identity** — a wrong match is not legally conclusive. Say: "I want to speak to an attorney before answering questions."

2. **Request the match certainty score** — The device returns a confidence percentage. If it's below 80%, the match is weakly supported and courts have found misidentification cases on this basis.

3. **Document the encounter** (if safe to do so):
   - Time, date, location
   - Agent names/badge numbers
   - Exactly what they said about the scan result
   - Whether you were detained vs. released

4. **Contact an immigration attorney immediately** — If ICE detained you based on a Mobile Fortify match, the detention may be challengeable if the match was weak or the device was improperly calibrated.

5. **Know your rights during field encounters**:
   - You have the right to refuse to answer questions without an attorney present
   - You can refuse consent to search your phone or vehicle
   - You do NOT have to provide your name (though doing so may reduce the likelihood of arrest for suspicion of illegal entry)
   - If you are arrested and taken into custody, your right to an attorney is reinforced — do not speak without one

**Legal precedent**: A documented case where Mobile Fortify returned two different (both incorrect) names for the same person in one encounter shows that field biometric devices have known accuracy problems. If detained based on a weak match, an immigration attorney can challenge the detention on the basis of insufficient probable cause.

---

## Part 4: Device Security — Layer 2 Defense

If your phone is seized during an ICE encounter, law enforcement can extract:
- All Signal message history (not just the disappearing-message window, but ALL messages ever sent, if still cached)
- Location history
- Contact list
- Photos
- Browsing history

This extraction is done via Cellebrite UFED (ICE holds an $11M contract).

### 4.1 Device Hardening — GrapheneOS

**Objective**: Make forensic extraction as difficult as possible if your device is seized.

**Install GrapheneOS on a Pixel phone**:
- GrapheneOS costs $0 (open-source)
- Supports Pixel 6–8 (older or newer Pixels may have issues)
- Blocks new USB connections when the device is locked at both kernel and hardware level
- Automatically reboots to BFU (Before First Unlock) state after 18 hours without unlock — at which point forensic extraction is severely limited

**How to install** (detailed steps in `device-hardening-implementation-guide.md`):
1. Back up your data
2. Download GrapheneOS from https://grapheneos.org
3. Flash to your Pixel device (requires a computer and USB cable)
4. Complete initial setup (no Google account — use offline mode or a non-identity-linked Gmail)

**Configuration after installation**:
1. Set a strong passphrase (NOT a PIN, NOT a biometric) — 12+ characters, no repeating patterns
2. Set auto-reboot to 18 hours: Settings > Security > Auto-reboot Timer
3. Disable developer options (Settings > Developer options > toggle off)
4. Disable new USB connections when locked: Settings > Developer options > USB configuration > Charging only

### 4.2 BFU vs. AFU — What Happens When Your Phone Is Seized

**Before First Unlock (BFU)**:
- Device powered on but PIN never entered since last boot
- Encryption keys NOT in memory
- Cellebrite extraction can access only:
  - Device info (IMEI, serial number)
  - Some cached SIM data
  - **Cannot access**: Messages, location, contacts, photos, app data

**After First Unlock (AFU)**:
- Device powered on and PIN entered at least once
- Encryption keys loaded into memory
- Cellebrite Physical Analyzer can access:
  - All Signal message database (full history)
  - Location history
  - All contacts
  - All photos
  - All app data
  - Credentials stored in Android Keystore

**The critical implication**: If you anticipate an ICE encounter (checkpoint, planned enforcement action, protest environment), power off your phone FULLY before the encounter. Not screen lock, not sleep mode — power off. This ensures the device boots into BFU state at next power-on, which limits Cellebrite extraction to basic metadata.

### 4.3 Duress PIN (Optional Advanced Feature)

GrapheneOS supports a "duress PIN" — a secondary PIN that you can enter if law enforcement forces you to unlock the device. Entering the duress PIN wipes the device completely, leaving no data for Cellebrite to extract.

**How to set up duress PIN**:
1. Settings > Security > Advanced > Duress PIN
2. Set a PIN that is different from your primary PIN (6–8 digits)
3. If forced to unlock, enter the duress PIN instead of your primary PIN
4. The device wipes immediately with no data left behind

**Legal considerations**: Using a duress PIN is legal in the US (you have the right to destroy your own data), but law enforcement may charge you with obstruction if you do this during an arrest. This is a judgment call you must make in the moment.

---

## Part 5: Communications Security — Layer 2 Defense

If your phone is seized, messages stored ON the device are extractable. Signal's server-side security (Signal stores nothing) is useless if your device has already been forensically accessed.

### 5.1 Signal Configuration for Undocumented Immigrants

**Disappearing messages**:
- Default to 1 day (messages auto-delete after 24 hours)
- For very sensitive conversations, set to 5 minutes
- This limits the time window for messages to exist if your device is seized, but does NOT prevent them if seized within that window

**Who can find you**:
- Settings > Privacy > Phone Number: Set to "Nobody"
- This prevents people who have your phone number from confirming you use Signal
- Register Signal with a secondary VoIP number (MySudo, JMP.chat, Google Voice) instead of your carrier phone number if possible

**Important limitation**: Signal's encryption is end-to-end, which means messages in transit are protected. But messages stored on your device are NOT encrypted from the operating system — Cellebrite can extract them if the device is AFU (unlocked). The protection comes from keeping your device in BFU state (powered off until encountered) or destroying the device (duress PIN).

### 5.2 Briar (For Anonymous Communication)

Briar is a mesh messenger that requires no phone number, no email, and no account. It routes through Tor by default.

**Why use Briar**: If you need to communicate with contacts without revealing your phone number, Briar provides that option.

**Limitations**: 
- Android-only
- Requires in-person QR code exchange to add contacts (more friction than Signal)
- Most users find it impractical as a daily driver

**Recommendation for undocumented immigrants**: Use Signal for primary communication (more familiar, better UX) and Briar for one-time or high-sensitivity contacts where phone number separation is critical.

---

## Part 6: Operational Discipline — Breaking Pattern-of-Life Analysis

The ELITE platform uses "pattern-of-life analysis" — analyzing your regular movements, work locations, friends' addresses, and routines — to build an addressability profile. Palantir explicitly documents this capability in internal materials.

### 6.1 Randomization Principles

**Address randomization**:
- Do not mail correspondence to your home address — use a mailbox service, a trusted friend's address, or a PO Box
- Vary your claimed address across different forms (if asked for address on a job application, consider providing the address of a trusted friend or organization if that doesn't create legal liability)
- Every 6 months, if circumstances permit, consider changing where you stay (this is not always practical, but when possible, prevents ICE from establishing a reliable address anchor)

**Behavioral randomization**:
- Do not establish a predictable commute to work or school
- Vary your daily routes
- Avoid regular meetings at the same location and time
- This is cognitively taxing but necessary for people at highest risk of targeted enforcement

**Digital randomization**:
- Rotate VPN providers monthly
- Use different phone SIM cards for different activities (one for work, one for community organizing, one for personal)
- Do not use the same username/email across different platforms

### 6.2 Community Trust Networks vs. Digital Opacity

**Principle**: Building trust within your immediate community (family, church, neighborhood) is more protective than digital anonymity. ICE enforcement actions often depend on tips from community members or discovery through bureaucratic processes (school enrollment, hospital visits, police encounters).

**Practical implication**: 
- Share your digital security practices with people you trust completely
- If your community knows you are undocumented and supports you, they are less likely to be leverage points for ICE
- If your status is not known, the digital/behavioral randomization above becomes more critical

---

## Part 7: Tier-by-Tier Implementation

### Tier 1: Essential (All undocumented immigrants — no exceptions)

1. **Data broker opt-out**: Complete LexisNexis Accurint opt-out (Step 2.1). If California resident, complete DROP platform (Step 2.2). Yearly maintenance.
2. **Signal**: Install Signal on your primary phone. Enable disappearing messages (1 day default). Set "Who can find me by number" to Nobody.
3. **Device** (if possible): If you can obtain a Pixel phone, install GrapheneOS. If not possible, use the strongest passphrase your current phone supports.
4. **Legal preparation**: Identify an immigration attorney and save their contact information. Know your right to refuse consent to searches and to request an attorney.

**Time to implement**: 4–6 hours (data broker opt-outs + signal configuration + legal attorney identification)

### Tier 2: Intermediate (Activist organizers, people at elevated enforcement risk)

All of Tier 1, plus:

5. **GrapheneOS**: Install GrapheneOS (not optional for Tier 2). Configure auto-reboot to 18 hours.
6. **Briar**: Install Briar on GrapheneOS device. Exchange QR codes with one trusted contact for emergency communication.
7. **VPN + Tor**: For organizing communications, connect Mullvad VPN first, then Tor Browser second. This hides Tor from your ISP.
8. **Secondary device**: If circumstances permit, keep a second GrapheneOS device powered off at home as a "quarantine device" — if one device is seized, you have a second with no forensic history.
9. **Automated data broker maintenance**: Subscribe to Incogni ($7.99/month) for quarterly automated data broker re-submissions.

**Time to implement**: 12–16 hours (includes GrapheneOS installation, Briar setup, VPN+Tor configuration)

### Tier 3: Advanced (People with active organizing roles or direct investigation targets)

All of Tier 2, plus:

10. **Qubes OS or Tails**: For sensitive digital organizing (creating documents, sending emails about organizing), use Qubes OS or Tails OS. These are specialized operating systems that isolate your activity into separate virtual machines so that a single compromise doesn't expose everything.
11. **Hardware security key**: Use a YubiKey for all critical accounts (email, financial services, organizing platform accounts).
12. **Physical security**: Maintain separate locations for sensitive activities. Do not conduct organizing meetings at your residence or workplace.
13. **Legal retainer**: Proactively retain immigration counsel and discuss incident response procedures. Establish a legal hotline number that you can call if arrested.

**Time to implement**: 20–30 hours (Qubes/Tails installation is the most time-intensive part)

---

## Part 8: If You Are Arrested or Detained

If ICE encounters you and takes you into custody:

### 8.1 Immediate Actions

1. **Say only**: "I am exercising my right to remain silent. I want to speak to an attorney."
2. **Do NOT sign any documents** — do not sign an I-9 form, do not sign consent to search, do not sign anything without an attorney present
3. **Do NOT agree to voluntary deportation** — the government may offer this to speed up the process, but it prevents future challenges to the arrest
4. **Request the name of the facility** — remember where you are being detained
5. **Ask for your phone call** — use it to call an immigration attorney or a family member who can contact an immigration attorney

### 8.2 In Detention

1. **Conserve your phone battery** — limit phone use, do not make unnecessary calls
2. **Do not discuss your case with cellmates** — anything you say can be used against you
3. **Request medical care if needed** — do not refuse treatment due to fear
4. **Maintain your document evidence** — keep any paperwork related to your immigration case

### 8.3 Know Your Legal Options

- **Asylum**: If you fear return to your home country, you can request asylum during the detention/deportation process
- **U visa**: If you are a victim of certain crimes and have suffered abuse
- **T visa**: If you are a victim of human trafficking
- **TPS (Temporary Protected Status)**: If your country is designated for TPS, you may be eligible
- **Stays of removal**: Immigration judges can stay (pause) deportations under certain circumstances

**Consult with an immigration attorney immediately** — these options have specific eligibility requirements and application windows. An attorney can assess which options apply to your case.

---

## Part 9: Community Resource Directory

### Legal Services (Free/Low-Cost)

- **RAICES (Refugee and Immigrant Center for Education and Legal Services)**: raicestexas.org
- **NILC (National Immigration Law Center)**: nilc.org (policy + training, not direct legal services)
- **Catholic Charities**: provides free immigration legal services in many dioceses
- **Local law school immigration clinics**: Most law schools offer free immigration legal services
- **American Immigration Council**: americanimmigrationcouncil.org

### Community Organizations

- **NDLON (National Day Laborer Organizing Network)**: organizes day laborers, provides know-your-rights training
- **RAICES community organizing**: includes families with undocumented members
- **SFLC (Software Freedom Law Center)**: sflc.org — provides security training for activists

### Tools

- **Signal**: signal.org (encrypted messaging)
- **GrapheneOS**: grapheneos.org (hardened mobile OS)
- **Briar**: briarproject.org (anonymous mesh messenger)
- **Mullvad VPN**: mullvad.net (privacy VPN)
- **Tor Browser**: torproject.org (anonymous browsing)

---

## Part 10: Updates and Revisions

This guide is current as of May 2026. The threat landscape changes:

- **Mobile Fortify capability updates**: ICE deployed Mobile Fortify in 2025; accuracy improvements or new features should trigger a review of Section 3.
- **ELITE platform changes**: If ICE modifies how address-confidence scoring works, Part 2 may need revision.
- **Legal status changes**: Immigration policy and enforcement priorities shift with administrations; this guide should be reviewed annually and after major policy changes.

**Planned updates**:
- July 2026: Post-election enforcement patterns assessment
- October 2026: Annual threat model review (new ICE technology deployments, new platform capabilities)
- January 2027: Post-inauguration policy assessment (new administration impacts on enforcement priorities)

---

## Summary Checklist

**Essential (everyone)**:
- [ ] Opt out of LexisNexis Accurint
- [ ] Install Signal and configure disappearing messages
- [ ] Identify and save immigration attorney contact
- [ ] Learn your rights: https://www.eff.org/know-your-rights

**Intermediate (activists, high-risk)**:
- [ ] Install GrapheneOS on Pixel phone
- [ ] Configure GrapheneOS auto-reboot to 18 hours
- [ ] Exchange QR codes with Briar contacts
- [ ] Subscribe to Incogni for automated data broker maintenance
- [ ] Set up VPN + Tor for sensitive communications

**Advanced (organizing leaders, investigation targets)**:
- [ ] Install Qubes OS or Tails OS for sensitive work
- [ ] Obtain YubiKey hardware security key
- [ ] Establish separate locations for organizing
- [ ] Retain immigration counsel; discuss incident response

---

**For questions or updates**: Contact immigration counsel or the RAICES legal team.

**Version**: 1.0  
**Last updated**: May 6, 2026  
**Next review**: July 2026
