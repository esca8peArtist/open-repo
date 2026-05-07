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

## Part 10: Financial Privacy — Avoiding Financial Surveillance and De-Banking

Financial transactions are a major vector for tracking undocumented immigrants. Bank records, payment apps, and remittance services can be subpoenaed by ICE or obtained through data-sharing arrangements with DHS. The ImmigrationOS platform can cross-reference financial data with immigration records to build location timelines and social network maps.

### 10.1 Why Financial Activity Is a Surveillance Vector

**Bank records and subpoenas**: ICE can subpoena bank records through grand jury process or via administrative subpoena in civil immigration enforcement. Bank records reveal: where you live (billing address), where you shop (merchant location), where you work (payroll deposits), who pays you (employer identity), and your regular movement patterns (ATM withdrawals at specific branches).

**Payment apps**: Venmo, Cash App, Zelle, and PayPal create transaction records that are stored on commercial servers and accessible via legal process. Venmo transaction history is public by default (merchants, amounts, and counterparty usernames are visible to anyone unless privacy settings are changed). Even with privacy settings enabled, the companies retain the transaction data and can be compelled to produce it.

**Remittance services**: Western Union, MoneyGram, and similar international money transfer services are regulated financial institutions required to verify identity for transfers above $1,000 and maintain records accessible via subpoena. If you use remittance services frequently, those records create a timeline of financial activity.

**Data broker financial cross-referencing**: Commercial data brokers (LexisNexis, Equifax, and others operating under the "alternative data" framework) collect and sell financial behavioral data — not account balances, but patterns: what types of merchants you frequent, what financial products you use, what zip codes your financial activity clusters in. This data is used by ELITE-type systems to triangulate location even without formal bank record subpoenas.

### 10.2 Cash-First Workflow

The most effective countermeasure against financial surveillance is conducting as many transactions as possible with cash, which creates no electronic record.

**Practical implementation**:
- Withdraw cash from ATMs in amounts you will use within 1–2 weeks. Do not carry large cash sums that create theft risk.
- Pay for groceries, transit, utilities, and everyday expenses in cash wherever accepted. Most retail and grocery stores accept cash; most utility providers accept cash payment at customer service locations or through money order.
- For recurring expenses (rent), a money order purchased with cash creates a payment record that the landlord can verify, without linking to a bank account. Purchase money orders at convenience stores, supermarkets, or USPS locations.

**Limitations**: Employers are generally required to pay wages through bank transfer or check for tax compliance. If your employer pays via direct deposit, that creates a bank record. This is a legal obligation on the employer's side that you cannot change. The countermeasure is to limit the digital footprint attached to that account (avoid using the account for purchases; withdraw in cash).

### 10.3 Prepaid Cards and Debit Cards

Prepaid debit cards (Visa Prepaid, Mastercard Prepaid) purchased with cash at retail stores (Walmart, CVS, Walgreens, 7-Eleven) allow electronic payments without a bank account in your name.

**How to use prepaid cards without identity linking**:
- Purchase the card with cash (some cards require identity verification for amounts over $500 loaded; for smaller amounts, many do not require ID)
- Load cash onto the card as needed at retail reload locations
- Use for online purchases, subscription services, or places that do not accept cash

**Important limitation**: Prepaid cards purchased with identity verification are registered to your name. For maximum privacy, use prepaid cards that do not require ID verification and reload with cash (not via bank transfer).

**Payroll cards**: Some employers provide "payroll cards" for workers without bank accounts. Payroll cards are a form of prepaid card loaded with wages. These are legal, require no bank account, and create less paper trail than a traditional bank relationship if used primarily as cash sources. However, the employer's payroll records still document your employment regardless of the payment method.

### 10.4 Cryptocurrency — Practical Limits and Appropriate Use

Cryptocurrency (Bitcoin, Monero, Ethereum) is sometimes recommended as a privacy tool, but its use for financial privacy is more limited than often claimed in activist contexts.

**Bitcoin (and most cryptocurrencies): Not private by default**. Every Bitcoin transaction is recorded on a public blockchain, permanently and globally visible. If you ever connect a Bitcoin wallet to your real identity (by purchasing with a bank account, using an exchange that did KYC verification, or receiving a payment from an identified sender), that address can be traced.

**Monero: Meaningfully private**. Monero is a cryptocurrency specifically designed to obscure sender, recipient, and transaction amounts. It is the only major cryptocurrency recommended for genuine financial privacy. However, converting cash to Monero and back to cash without identity exposure requires using peer-to-peer exchanges (LocalMonero, or others operating without KYC), which involves in-person transactions with counterparties you do not know. This creates safety risks and practical friction that make Monero unsuitable as a primary financial tool for most immigrants.

**Recommendation**: Cryptocurrency is not a replacement for cash or prepaid cards for most undocumented immigrants. The friction and technical complexity are high, and the privacy benefit is only realized if the acquisition of the cryptocurrency is also private. Use cash and prepaid cards as the primary financial privacy tools, and do not rely on cryptocurrency unless you have specifically learned the Monero peer-to-peer exchange workflow.

### 10.5 Avoiding Financial De-Banking

"De-banking" — the closure of a bank account by the institution — has been documented against communities perceived as high-risk. This is distinct from government action but has similar consequences: loss of financial infrastructure at a vulnerable moment.

**Risk reduction**:
- Maintain minimal account balances (only what you need for near-term expenses) to reduce the account's visibility to risk-monitoring systems that flag large transaction patterns
- Do not use your primary bank account for transactions that pattern-match to high-risk categories (large cash deposits without explanation, frequent international transfers, cryptocurrency exchanges)
- If you use a community credit union rather than a large bank, you are dealing with a non-profit institution whose de-banking risk profile is different — community credit unions have less automated risk scoring infrastructure and more human relationship-based account management

**If de-banked**: A bank account is legally optional — no US law requires you to have one. Prepare for this possibility by:
- Maintaining a working prepaid card system before you need it (do not wait until your bank account is closed)
- Establishing a relationship with a credit union if possible, as a backup banking relationship
- Knowing which money order providers (USPS, 7-Eleven, supermarkets) are in your area for rent and utility payments

### 10.6 Financial Evidence in Immigration Cases

Financial records can be both a surveillance risk and a legal asset. If you have legal proceedings (asylum case, U visa application, work permit), financial records demonstrating continuous presence in the US are valuable evidence of your ties to the community and your history.

Consult with your immigration attorney about which financial records to preserve and how to present them in legal proceedings. Your attorney can advise on the balance between financial privacy (to reduce surveillance risk) and financial documentation (to support your legal case).

---

## Part 11: SIM Isolation and Phone Number Privacy

### 11.1 Why Multiple SIM Cards Matter

Your phone number is an identity anchor that links your device to your carrier account, your contacts, and your real identity. In the immigration context, a single phone number used for both personal and community organizing activity creates a single point of surveillance: anyone who has your number can track your communication patterns, and carrier records connect that number to your billing address, payment method, and account history.

**SIM isolation** means using separate SIM cards for separate activities, each with a different number, so that a compromise of one number does not expose all your communications.

### 11.2 Practical SIM Isolation Setup

**Three-SIM model for high-risk individuals**:

| SIM | Purpose | Registration | Loaded with |
|-----|---------|-------------|-------------|
| SIM A — Personal | Family, personal contacts, non-organizing use | Prepaid, purchased with cash | $20–$30/month as needed |
| SIM B — Organizing | Community organizing, advocacy contacts, legal aid organizations | Prepaid, purchased with cash, no identity link | $10–$20/month for calls/texts |
| SIM C — Legal/Emergency | Immigration attorney, emergency contacts, hotline numbers | May be more permanent; consider a VoIP number | Minimal usage; keep loaded |

**Device handling**: On a GrapheneOS Pixel, you can use eSIM or physical SIM swapping. Alternatively, a second inexpensive phone ($30–$60 prepaid) running on SIM B is a viable low-cost approach.

**SIM swapping discipline**: When switching between SIM contexts, turn the phone off completely before swapping. A device that connects briefly to a tower on one SIM and then on another creates a pattern that can be linked by carrier IMSI cross-referencing.

### 11.3 VoIP Numbers for Additional Separation

A Voice over IP (VoIP) phone number operates over the internet rather than a cellular carrier, and can be registered without proof of identity at most services.

**Recommended VoIP services**:
- **MySudo**: Provides multiple isolated "Sudo" numbers, each with separate email and credit card. Each Sudo is compartmentalized. Available on iOS and Android.
- **JMP.chat**: XMPP-based VoIP service; can be registered pseudonymously and paid with cryptocurrency.
- **Google Voice**: Available but requires a Google account with verified identity — only appropriate if you already have a Google account not linked to your immigration status.

**Use case for immigration context**: A VoIP number is appropriate for registering Signal (so Signal is not linked to your carrier number), for giving a contact number to services where you do not want your carrier number recorded, and as SIM C in the isolation model above.

**Limitation**: VoIP numbers are less reliable for emergency services (911 calls from VoIP may not route your location automatically). Do not use a VoIP number as your only means of making emergency calls.

### 11.4 Location Spoofing — What It Accomplishes and What It Does Not

Location spoofing means deliberately misrepresenting your device's reported location to apps and services. This can be done at the app permission level (denying location access) or via mock location tools that feed false GPS coordinates.

**What location spoofing accomplishes**:
- Prevents apps (weather apps, navigation, social media) from recording your real location and transmitting it to their servers
- Can prevent OSINT tools from identifying your location through app-submitted location data
- Can confuse pattern-of-life analysis that depends on app-reported location data

**What location spoofing does NOT accomplish**:
- It does not hide your location from your cellular carrier. Carrier location data is determined by which cell towers your phone connects to — this is at the network level, not the device level, and cannot be spoofed by the device.
- It does not hide your location from a IMSI catcher (Stingray) deployed near you.
- It does not alter EXIF data in photos already taken with location enabled.

**Practical implementation on GrapheneOS**:
- Go to Settings > Privacy > Location. For each app, set to "Deny" if the app does not need location access. Set to "Only while using" for navigation apps you use legitimately.
- For mock location: GrapheneOS supports "fake location" permissions per-app via developer mode. This is an advanced feature; consult `device-hardening-implementation-guide.md` for step-by-step configuration.

**Recommendation**: Focus first on denying location access to apps that have no need for it (which is most apps), before setting up mock location. The denial approach reduces the data that reaches data brokers far more effectively than most users realize.

---

## Part 12: Week-by-Week Implementation Timeline

This timeline assumes a starting point of no security measures in place. Adapt to your circumstances.

### Week 1: Foundation (4–6 hours total)

**Day 1–2: Data broker opt-outs**
- Complete LexisNexis Accurint opt-out: https://optout.lexisnexis.com/ (30 minutes)
- If California resident: complete DROP platform at privacy.ca.gov/drop/ (30 minutes)
- Submit secondary data broker opt-outs (BeenVerified, Spokeo, WhitePages — see Part 2.3) (45 minutes)

**Day 3–5: Communications**
- Install Signal on your current phone
- Enable disappearing messages: Settings > Privacy > Default Timer > 1 day
- Set "Who can find me" to Nobody: Settings > Privacy > Phone Number
- Identify your immigration attorney and save their contact in Signal

**Day 6–7: Legal preparation**
- Read the EFF Know Your Rights guide: https://www.eff.org/know-your-rights
- Prepare a physical card with your attorney's name and phone number. Carry it in your wallet.
- Review Part 8 of this guide (arrest and detention procedures)

### Week 2: Device and SIM Security (8–12 hours total)

**Day 8–10: Obtain hardware**
- Purchase a Pixel 6, 7, or 8 from a retail store or online (used devices are fine; $100–$250)
- Purchase one or two prepaid SIM cards from a carrier different from your current carrier

**Day 11–14: Install GrapheneOS**
- Follow the GrapheneOS installation guide at grapheneos.org/install
- This takes 2–4 hours for a first-time installer; proceed carefully
- After installation, configure auto-reboot timer (18 hours) and strong passphrase
- Install Signal on GrapheneOS device with a new VoIP number (MySudo or JMP.chat)

### Week 3: Financial and Behavioral Security (2–3 hours total)

**Day 15–17: Financial audit**
- Identify which of your regular expenses are currently linked to a bank account or payment app
- Determine which can be moved to cash or prepaid card (groceries, transit, everyday expenses)
- Purchase a prepaid debit card at a retail store with cash; confirm it works for your use case

**Day 18–21: Behavioral randomization**
- Read Part 6 of this guide (operational discipline / pattern-of-life)
- Identify two or three specific behavioral patterns to change (commute route, meeting location, mailing address)
- Implement at least one address randomization step: if currently using your home address for non-essential mail, obtain a mailbox service or use a trusted community organization's address

### Week 4: Integration and Escalation Preparation (2–4 hours)

**Day 22–25: Community trust network**
- Identify two trusted people (family, community, trusted friend) who know your situation and can be contacted if you are arrested
- Share the arrest protocol from Part 8 with them
- Confirm they have your attorney's contact information

**Day 26–28: Incogni automation (optional)**
- If budget permits, subscribe to Incogni ($7.99/month) to automate data broker re-submissions quarterly
- Without Incogni: schedule a calendar reminder every 90 days to repeat the data broker opt-outs from Week 1

**Ongoing (monthly)**:
- Every 30–90 days: rotate VPN providers and review Signal contact list for inactive or unverified contacts
- Every 90 days: re-submit data broker opt-outs if not using Incogni
- After any ICE encounter: document the encounter details and share with your attorney; review whether threat level has changed

---

## Part 13: Organization Resource Mapping — For Legal Aid Organizations

This section addresses the specific question: **which recommendations are for individual implementation, and which are for the organizations that serve immigrant communities?**

### 13.1 Individual Implementation (Clients/Community Members)

The following recommendations are designed for individual undocumented immigrants to implement on their own or with minimal organizational support:

| Recommendation | Part | Time | Cost | Skill Level |
|---|---|---|---|---|
| LexisNexis Accurint opt-out | Part 2.1 | 30 min | Free | None |
| California DROP platform | Part 2.2 | 30 min | Free | None |
| Signal installation and configuration | Part 5.1 | 1 hour | Free | Basic |
| Secondary data broker opt-outs | Part 2.3 | 45 min | Free | None |
| Prepare physical attorney card | Part 8 | 15 min | Free | None |
| Prepaid card acquisition | Part 10.3 | 30 min | $20–$50 | None |
| Cash-first behavioral changes | Part 10.2 | Ongoing | None | None |

### 13.2 Organizational Support Recommended (for Complex Steps)

The following recommendations benefit from organizational support — either trained volunteers, tech staff, or a structured workshop setting:

| Recommendation | Part | Why Org Support Helps |
|---|---|---|
| GrapheneOS installation | Part 4.1 | Technical — first-time installation takes 2–4 hours and requires a computer; group installation workshops are efficient |
| SIM isolation setup | Part 11 | Choosing carriers, purchasing SIMs, configuring multiple numbers — works better in a group setting with tech support |
| Incogni subscription management | Part 2.4 | Payment card and subscription management; organizations can set up group subscriptions for clients |
| Briar setup and QR code exchange | Part 7.2 | Requires in-person exchange; community events are natural settings |
| Legal retainer identification | Part 7.3 | Organizations have existing referral networks; individuals searching for attorneys independently face significant barriers |

### 13.3 Organizational-Level Recommendations (For the Legal Aid Org Itself)

The following recommendations are not about individual client security but about how legal aid organizations can protect their client data and communications:

**Attorney-client confidentiality**:
- Immigration attorneys must use end-to-end encrypted communication channels for client communication. Email is not sufficient. Signal or a legal practice management system with end-to-end encryption (Clio, MyCase — confirm encryption specifications) should be standard.
- Client files stored in cloud services (Google Drive, Dropbox, etc.) should be in services with client-side encryption or client access controls. ICE can subpoena cloud-hosted client data; attorney-client privilege protects content but delays, not prevents, production.
- Staff computers that hold client information should use full-disk encryption (FileVault on Mac, BitLocker on Windows).

**Organizational operating security**:
- Intake forms and client contact records should be stored with role-based access controls (not all staff need access to all client records).
- Client contact information (phone numbers, addresses) should be purged from staff personal phones. Use Signal's "Note to Self" feature or an organizational secure messaging tool to store client contact notes.
- Train all staff (including administrative staff who handle intake) on the Part 3 Mobile Fortify field encounter protocol — staff may encounter ICE agents at courthouses, detention facilities, or in the community.

**Organizational device policy**:
- Field staff who accompany clients to appointments or visit clients in the community should have device policies that align with the Tier 2 guidance in Part 7: encrypted devices, Signal for field communications, and a protocol for what to do if a device is seized.

### 13.4 Recommended Workshop Curriculum for Legal Aid Organizations

Organizations distributing this guide should consider offering workshops on three core topics:

1. **30-minute data broker opt-out session** (in-person, client-facing): Guide all clients through LexisNexis Accurint opt-out and (for California residents) DROP platform submission at a single group session. The 30-minute group format is dramatically more effective than handing out written instructions — completion rates are near 100% vs. low for printed instructions alone.

2. **90-minute device security workshop**: GrapheneOS installation and Signal configuration. Bring 3–4 volunteer tech supporters for every 10 clients. Require clients to bring their Pixel device and a laptop or provide loaner laptops for the installation step. Focus on the most impactful settings: passphrase (not biometric), auto-reboot timer, disappearing messages.

3. **Know Your Rights briefing with incident response drill**: 60-minute session covering the arrest protocol (Part 8), the attorney card preparation, and a 10-minute "what do you say and do" rehearsal. This is the session that produces the most durable behavioral change — rehearsal creates muscle memory that written materials do not.

---

## Part 15: Updates and Revisions

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
- [ ] Opt out of LexisNexis Accurint (Part 2.1)
- [ ] California residents: complete DROP platform at privacy.ca.gov/drop (Part 2.2)
- [ ] Install Signal and configure disappearing messages (Part 5.1)
- [ ] Identify and save immigration attorney contact (Part 8.3)
- [ ] Prepare physical attorney card — write number on paper, carry in wallet
- [ ] Learn your rights: https://www.eff.org/know-your-rights
- [ ] Begin shifting daily expenses to cash (Part 10.2)
- [ ] Submit secondary data broker opt-outs: BeenVerified, Spokeo, WhitePages (Part 2.3)

**Intermediate (activists, high-risk individuals)**:
- [ ] Install GrapheneOS on Pixel phone (Part 4.1)
- [ ] Configure GrapheneOS auto-reboot to 18 hours (Part 4.1)
- [ ] Exchange QR codes with Briar contacts (Part 5.2)
- [ ] Subscribe to Incogni for automated data broker maintenance ($7.99/month) (Part 2.4)
- [ ] Set up VPN + Tor for sensitive communications (Part 7.2)
- [ ] Acquire prepaid debit card with cash (Part 10.3)
- [ ] Set up SIM B on separate prepaid carrier for organizing communications (Part 11.2)

**Advanced (organizing leaders, investigation targets)**:
- [ ] Install Qubes OS or Tails OS for sensitive work (Part 7.3)
- [ ] Obtain YubiKey hardware security key (Part 7.3)
- [ ] Establish separate locations for organizing (Part 7.3)
- [ ] Retain immigration counsel; discuss incident response
- [ ] Implement VoIP number (MySudo or JMP.chat) for Signal registration (Part 11.3)
- [ ] Complete full financial audit; move maximum expenses off bank-tracked channels (Part 10)
- [ ] Review organizational resource mapping section with your legal aid organization (Part 13)

---

**For questions or updates**: Contact immigration counsel or the RAICES legal team.

**Version**: 1.0  
**Last updated**: May 6, 2026  
**Next review**: July 2026
