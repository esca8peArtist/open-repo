---
title: "Immigration + Surveillance Evasion Playbook: Digital Defense Against ICE Enforcement"
project: cybersecurity-hardening
created: 2026-05-07
last_updated: 2026-06-06
status: production-ready
phase: Phase 2
session: 875
version: 1.1
depends_on:
  - threat-model.md
  - opsec-playbook.md
  - implementation-guide.md
  - palantir-threat-model.md
  - THREAT_ENVIRONMENT_Q2_2026_UPDATE.md
  - PHASE_2_THREAT_INTEGRATION_CHECKLIST.md
confidence: high — grounded in documented ICE capabilities (ELITE/Palantir, ImmigrationOS, Mobile Fortify/NEC, Penlink geofencing, Thomson Reuters CLEAR, Medicaid data-sharing agreement, Bi2 iris scanning, Clearview AI, DOGE SSA access), court filings, EFF/Brennan Center primary source reporting, and immigration attorney community feedback; updated June 6, 2026 with iris scanning contract (The Register/Biometric Update/IDTechWire), Clearview AI HSI contract (American Immigration Council/Immigration Policy Tracking Project), DOGE SSA access (Democracy Forward/NPR/Democracy Docket), Thomson Reuters LEIDS-5 expiration (LawNext), and DHS administrative subpoenas (ACLU/EFF/Military.com)
audience: Undocumented immigrants, DACA recipients, visa holders under enforcement risk, immigration attorneys, legal aid organizations, immigrant rights orgs, family support networks
word_count: ~4,200
changelog: v1.1 — Q2 2026 threat integration (5 patches): UPDATE-IMM-01 iris scanning added to field toolkit (Section 1.3 expansion); UPDATE-IMM-02 Clearview AI HSI contract documented (Section 1.3 addition); UPDATE-IMM-03 DOGE SSA data as enforcement pipeline (new Section 1.6); UPDATE-IMM-04 Thomson Reuters LEIDS-5 expiration note (Section 1.1); UPDATE-IMM-05 DHS administrative subpoenas against anonymous accounts (Section 3.4 new)
---

# Immigration + Surveillance Evasion Playbook

**For legal service providers and workshop facilitators**: This guide translates the ICE surveillance stack into an immigration-specific operational framework with concrete countermeasures for each layer. The threat is documented and operational — not theoretical. Every tool named in Section 1 has a confirmed contract, a user manual, or court filings attesting to its use. The countermeasures in Sections 2–7 address each layer directly and are designed for implementation without technical expertise. Section 8 provides copy-paste-ready checklists for distribution to clients.

**Version 1.1 — Q2 2026 patch integration (June 6, 2026)**: Five critical threat updates have been applied to this version: (1) Iris scanning added to the ICE field biometric toolkit — $25.1M Bi2 Technologies contract, 1,570+ scanners, June 1 deployment (Section 1.3); (2) Clearview AI's 50B-image database confirmed operational for ICE HSI investigations — a parallel facial recognition layer beyond the HART database (Section 1.3); (3) DOGE's unlawful Social Security Administration data access documented as a new immigration enforcement pipeline — SSA holds immigration status, wage history, and employer data for 300M+ Americans (Section 1.6); (4) Thomson Reuters LEIDS-5 contract expired May 31, 2026, status unconfirmed — data broker opt-outs remain essential regardless (Section 1.1); (5) DHS administrative subpoenas have unmasked anonymous social media accounts criticizing ICE — anonymous account infrastructure requirements documented (Section 3.4).

Cross-references to `opsec-playbook.md` and `implementation-guide.md` are provided throughout. Do not repeat work: if a client has already completed device hardening per the core playbook, those measures apply directly here.

---

## Section 1: The ICE Surveillance Stack — What Is Actually Being Used Against You

Understanding the specific tools ICE deploys changes what you prioritize. This is not a list of theoretical capabilities. Each tool listed has a documented contract and confirmed operational use.

### 1.1 ELITE — Address Confidence Scoring (Palantir, $29.9M contract, September 2025)

**What it does**: ELITE (Enhanced Leads Identification and Targeting for Enforcement) is a Palantir-built tool that populates a map with deportation targets and generates an "address confidence score" — a percentage rating (e.g., 98.95 or 77.25 out of 100) representing how certain ICE is that you live at a given address.

**Data sources the score draws from**:
- HHS/Medicaid records: A data-sharing agreement signed December 2025 gives ICE access to basic biographical and contact information — including home addresses — from nearly 80 million Medicaid patients. A U.S. District Judge allowed this sharing to resume on January 5, 2026. If you or a family member has ever received Medicaid, that address is in the ELITE system.
- Thomson Reuters CLEAR: ICE's $22.8 million LEIDS-5 contract ran through May 31, 2026. *(June 2026 update: The LEIDS-5 contract expired May 31, 2026. As of June 6, 2026, no confirmed renewal has been announced. More than 200 Thomson Reuters employees signed a letter demanding non-renewal; union investors launched a shareholder campaign ahead of the June 10, 2026 shareholder vote. However, Thomson Reuters maintains multiple DHS/ICE contract vehicles estimated at ~$60M total, providing alternative access paths to CLEAR data. CLEAR opt-out remains a recommended action — removing your records from CLEAR at source protects you regardless of which specific contract vehicle provides access.)* CLEAR aggregates driver's license data, voter registrations, marriage records, property records, and commercial location data.
- LexisNexis Accurint: A separate ICE contract with LexisNexis feeds commercial consumer data (utility records, credit inquiries, address history) directly into ELITE's confidence scoring.
- Facebook and social media EXIF data: Penlink (ICE subscription, September 2025) extracts GPS coordinates embedded in photos uploaded to Facebook and other platforms, creating a real-time location timeline from photos you or contacts have posted publicly.

**Why this matters**: A high confidence score (above 80%) means ICE will prioritize your address for a raid. A low score means the address is uncertain enough to deprioritize. You cannot delete yourself from Medicaid records, but you can reduce the score that other data sources contribute.

**Your countermeasure**: Section 2 below — data broker opt-outs that remove your address from LexisNexis and Thomson Reuters CLEAR feeds.

### 1.2 ImmigrationOS — Case File and Social Network Platform (Palantir, $30M contract, July 2025)

**What it does**: ImmigrationOS is the case management and social graph platform that consolidates your immigration case file, travel history, prior enforcement encounters, biometric data, family relationships, and workplace connections into a single searchable record. ICE officers query it in real time during traffic stops, at checkpoints, and during field operations.

**Social graph capability**: ImmigrationOS uses entity resolution to create persistent links between associated persons. If you are connected — even indirectly — to someone who is already in the system as an enforcement target, you enter the investigation's social graph. This is documented in `palantir-threat-model.md`. A family member's detention, a workplace colleague's arrest, or a community organization's presence in the system can draw you into an investigation without any independent action by ICE against you.

**Your countermeasure**: Minimize your digital connections to known enforcement targets (social media contact, publicly listed association with flagged organizations). This does not mean abandoning community — it means managing what is visible to automated systems. Section 3 covers social media hygiene.

### 1.3 Mobile Fortify + Iris Scanning + Clearview AI — The Full ICE Field Biometric Toolkit

**What Mobile Fortify does**: Mobile Fortify is an ICE smartphone app that allows agents to photograph anyone they encounter and run the image against DHS's HART biometric database (150M+ records). The device returns a photo match with a confidence percentage. It was deployed without a required Privacy Impact Assessment. Illinois and Chicago sued ICE over this deployment in January 2026, documenting over 100,000 uses.

**Where it is being used**: Not only at formal detention facilities. ICE agents have used Mobile Fortify:
- At protests, including Minneapolis (documented February 2026 — see Section 1.4 case study)
- At traffic stops
- At workplaces and outside community organizations
- At churches (after the Trump administration rescinded sensitive-location protections on January 20, 2025)

**Accuracy problems**: The device has documented misidentification issues. In documented cases it has returned two different, both incorrect, names for the same person in a single encounter. Accuracy is worse for women and people of color. A positive match is not legally conclusive.

**UPDATE (June 2026): Iris Scanning Added to Field Toolkit.** On May 22, 2026, ICE finalized a $25.1M no-bid contract with Bi2 Technologies for 1,570+ mobile iris scanners, effective June 1, 2026. The scanners access a 5M+ record database drawn from booking, arrest, and incarceration records from 47 states. This is a 5x increase from the prior $4.6M Bi2 contract. ICE agents may now use iris scanning as a secondary biometric confirmation step when facial identification via Mobile Fortify is uncertain — creating a two-stage pipeline: identification at distance (Mobile Fortify/facial recognition) and identity confirmation at close range (iris scan). Iris scanning requires close physical contact, so its primary risk is in detention processing and checkpoint encounters where an agent can approach you.

**Do not consent to iris scanning outside of a formal arrest processing context.** Compelled iris scanning in a street or checkpoint encounter without arrest is legally unsettled — assert your right to consult an attorney before submitting to any biometric collection. Unlike a facial photograph (which an agent can take from a distance without your cooperation), iris scanning requires your proximity and cooperation. You can and should decline.

**UPDATE (June 2026): Clearview AI — The Parallel Facial Recognition Layer.** The prior threat model described Mobile Fortify as using the NEC facial recognition engine against the DHS HART database (150M+ records). A parallel layer is now confirmed: ICE's Homeland Security Investigations (HSI) division holds a $9.2M Clearview AI contract; Clearview's database contains 50+ billion images scraped from the internet. CBP separately signed a $225,000 Clearview contract in February 2026. The jurisdictional distinction matters: ICE ERO (deportation enforcement) primarily uses the NEC/HART stack. ICE HSI (which handles workplace raids, financial investigations, labor trafficking, and organized crime) uses the Clearview layer. If a client has any connection to an HSI investigation — not just deportation enforcement — Clearview AI's internet-scraped database is in scope. Clearview includes social media profile photos, news photos, protest photos, community organization website photos, and any public photo ever posted online. It is not limited to people who have ever been arrested or enrolled in a government database.

**Your countermeasures**: Physical countermeasures (Section 4) and legal response strategy if misidentified (Section 5.2). Social media hygiene (Section 3) reduces Clearview's ability to scrape new images of you. Images already posted publicly cannot be removed from Clearview's database retroactively — evaluate all future public photos against your exposure level.

### 1.4 Penlink — Geofencing and Location Tracking (ICE subscription, September 2025)

**What it does**: Penlink provides ICE with access to billions of daily location signals from hundreds of millions of mobile phones, with both forensic (historical) and predictive analytics. ICE's internal legal analysis claims it can query this data without a warrant because it was purchased from commercial vendors rather than obtained from telecommunications carriers.

Penlink's geofencing feature allows ICE to identify every cell phone that was present in a defined geographic area (a neighborhood, a building, a protest route) during a defined time window — and then pull the identity and movement history associated with each device.

**The specific risk**: If your phone was present in an area where ICE was conducting or planning an operation, your device's location history is accessible to ICE without a warrant. This includes areas around community organizations, churches, and any location where other enforcement targets are known to congregate.

**Your countermeasure**: Section 6 covers phone-off protocols and geofencing evasion for high-risk situations.

### 1.5 Social Media Surveillance — Babel Street + ICE Social Media Monitoring Contracts

**What it does**: ICE issued a Request for Information in October 2025 seeking contractors to monitor Facebook, Instagram, X/Twitter, TikTok, YouTube, Reddit, WhatsApp, LinkedIn, and additional platforms for immigration enforcement purposes. The Babel Street platform (confirmed DHS/ICE contract) provides persistent monitoring — continuously flagging new content from tracked individuals without requiring a new search query.

**Documented enforcement use**: Social media posts have been used directly in deportation proceedings. Migrant Justice organizers in Vermont were arrested in part based on ICE surveillance of their public Facebook and Twitter activity. ICE used Facebook event listings to track New York Sanctuary Coalition activities in 2018; the same capability is expanded and automated in 2026.

**The "Catch and Revoke" pipeline**: The State Department and DHS run a coordinated program that uses AI to review social media for protest-related content by visa holders, leading directly to visa revocation. Documented enforcement against pro-Palestine student protesters in 2025 demonstrates this pipeline is operational. If you hold any visa category, public protest-related social media posts carry revocation risk.

**Your countermeasure**: Section 3 — social media hygiene protocol.

### 1.6 DOGE — Federal Benefit Data as an Enforcement Pipeline (NEW — June 2026)

**What it does**: In January 2026, court filings revealed that DOGE employees at the Social Security Administration secretly accessed records for 300M+ Americans — including immigration status, bank account numbers, wage histories, and health records — and coordinated with a political advocacy group to match SSA data against state voter rolls. Whistleblower Charles Borges confirmed a dataset of 300M+ people was copied to a virtual database without security protocols. The Trump administration admitted to mishandling the data.

**Current legal status**: The Supreme Court authorized some DOGE access to SSA data in an April 2026 ruling. A separate federal court (Judge Denise Cote, Southern District of New York) issued a preliminary injunction on June 6, 2026 halting DOGE's access to Office of Personnel Management data and requiring DOGE employees' names to be disclosed. New System of Record Notices (SORNs) have been issued in parallel, expanding formal data-sharing authorization between SSA and other agencies — creating legal authority for data flows that previously existed only through unauthorized DOGE access.

**Your exposure**: If you have ever received Social Security benefits, held a Social Security number, or had wage income reported to SSA, your records were part of the accessed dataset. SSA holds immigration status data that can cross-reference with ICE enforcement systems. SSA's wage history data also reveals your employer — which can be cross-referenced with workplace enforcement operations.

**Why this matters specifically for immigration clients**: ELITE already draws from Medicaid records under the December 2025 data-sharing agreement. The DOGE/SSA pathway represents a second federal benefit database — wage history, immigration status, employer information — that could be incorporated into enforcement targeting. The pathway has been opened at the administrative level (via SORNs) even while litigation over its legality continues.

**Your countermeasure**: This data cannot be removed from SSA records. The practical countermeasure is to minimize what other data sources (commercial data brokers) contribute to enforcement confidence scores — because the SSA data cannot be deleted, reducing the commercial supplement data reduces the combined confidence score that ELITE or a successor system would generate. Complete the data broker opt-outs in Section 2.

---

## Section 2: Data Broker Opt-Outs — Degrading ELITE's Address Confidence Score

The ELITE address confidence score depends on data from LexisNexis, Thomson Reuters CLEAR, and commercial data brokers. Removing yourself from these databases directly degrades the score ICE uses to prioritize your address.

**Complete these in order — highest impact first.**

### 2.1 LexisNexis Accurint (CRITICAL — Direct ICE Contract)

LexisNexis holds a direct contract with ICE and is the primary address data source for ELITE scoring.

**Process**:
1. Go to https://optout.lexisnexis.com/
2. Select "Opt out of LexisNexis risk solutions products"
3. Enter your full name, current address, date of birth
4. Upload a government-issued ID (do this — it increases the likelihood of successful opt-out)
5. Select "permanent opt-out" for a 7-year suppression

**Timeline**: 30 days to removal from public searches; 90 days for full suppression from law enforcement queries.

**For undocumented immigrants without government ID**: The opt-out form still accepts submissions without ID, but processing is slower. Submit it without ID if that is your situation.

### 2.2 California Residents — DROP Platform (Most Powerful Tool Available)

If you are a California resident, the DROP (Delete Request and Opt-Out Platform) at privacy.ca.gov is a single submission that cascades to all California data brokers automatically.

**Process**:
1. Go to https://privacy.ca.gov/drop/
2. Verify California residency (CA driver's license, state ID, or AB60/AB1766 undocumented ID — these IDs satisfy DROP's residency verification)
3. Submit one request; it cascades to 100+ brokers automatically and re-processes when data re-enters from public records

**Timeline**: 45 days for initial processing; automatic ongoing maintenance thereafter.

**AB60/AB1766**: California law allows undocumented residents to obtain a state driver's license (AB60) or state ID (AB1766) without proof of authorized presence. These IDs satisfy DROP verification and provide access to the most comprehensive data deletion tool available in any US state.

### 2.3 Secondary Data Brokers (submit all in one 45-minute session)

| Broker | Opt-Out URL | Priority |
|--------|-------------|----------|
| BeenVerified | https://www.beenverified.com/app/optout/search | HIGH |
| Spokeo | https://www.spokeo.com/optout | HIGH |
| WhitePages | https://www.whitepages.com/suppression-requests | HIGH |
| Intelius | https://www.intelius.com/opt-out/ | MEDIUM |
| Radaris | https://radaris.com/page/how-to-remove | MEDIUM |
| TruePeopleSearch | https://www.truepeoplesearch.com/removal | MEDIUM |
| FastPeopleSearch | https://www.fastpeoplesearch.com/removal | MEDIUM |

### 2.4 Ongoing Maintenance

Data brokers re-add you from public records approximately every 90 days. Options:
- **Manual**: Re-submit Steps 2.1–2.3 every 90 days (45 minutes quarterly)
- **Automated (Incogni, $7.99/month via Surfshark)**: Covers 420+ brokers with automated 60-day re-submission cycles. For undocumented immigrants, this is a reasonable investment given the stakes.

---

## Section 3: Social Media Hygiene — Reducing Your ELITE Social Graph Exposure

### 3.1 High-Risk Content to Remove or Lock

**Remove or archive immediately if your account is public**:
- Posts or photos that identify your home neighborhood, workplace, or regular locations
- Check-ins or tagged locations
- Photos with geotags enabled (GPS coordinates are embedded in image EXIF data — Penlink extracts these from Facebook automatically)
- Posts mentioning your immigration status or proceedings
- Posts about community organizing activity or participation in advocacy events

**Change all accounts to private**:
- Instagram/Facebook: Settings > Privacy > Account Privacy > Private
- X/Twitter: Settings > Privacy and Safety > Audience and Tagging > Protect posts
- TikTok: Settings > Privacy > Private Account

### 3.2 Disable EXIF Location in Photos

Every photo taken with location services enabled embeds GPS coordinates in the file. When that photo is uploaded to Facebook, Penlink extracts the coordinates and adds them to your location timeline.

**Disable camera location access**:
- iOS: Settings > Privacy > Location Services > Camera > Never
- Android: Settings > Apps > Camera > Permissions > Location > Deny

Do this now, before the next photo you take.

### 3.3 Specific Risk: Visa Holders and DACA Recipients

The "Catch and Revoke" pipeline is not hypothetical. State Department and DHS have documented use of AI-reviewed social media to revoke visas of pro-Palestine student protesters in 2025. The mechanism applies to all visa categories. If you hold any visa status or DACA:
- Do not post publicly about protest participation, anti-ICE organizing, or immigration enforcement events
- Set all accounts to maximum privacy immediately, before making any further posts
- Consult with immigration counsel before making public statements at protests or posting protest-related content

### 3.4 DHS Administrative Subpoenas — Anonymous Account Risk (NEW — June 2026)

**What changed**: DHS has issued hundreds of administrative subpoenas — which require no court authorization — to Google, Meta, Reddit, and Discord to unmask anonymous accounts that posted about ICE raids, tracked ICE agent movements, or criticized ICE operations. Google, Meta, and Reddit partially complied before legal challenges were filed. The ACLU of Northern California and Pennsylvania successfully challenged some subpoenas; DHS withdrew some after legal pressure. However, disclosures may have already occurred before legal challenges could prevent them — withdrawal after challenge does not undo data that was already provided.

**Documented cases**:
- A Philadelphia-area man received a DHS administrative subpoena four hours after emailing a DHS official. Two DHS agents and local police subsequently appeared at his home.
- Columbia University received a subpoena pressuring it to share information about a student who had participated in pro-Palestinian protests.
- Accounts specifically tracking ICE agent location alerts and posting about immigration enforcement operations have been targeted.

**What this means**: Any social media account that was registered with a real email address, phone number, or payment method, or that was accessed from an IP address linked to your identity, can potentially be unmasked via subpoena. The platform does not have to notify you before complying. You may not know your identity was disclosed until after it happened.

**Countermeasure — if you operate accounts posting about ICE activity or immigration enforcement**: Those accounts must be created and operated with complete separation from your real identity. This requires:
- A separate email address created under a pseudonym (ProtonMail, not Gmail)
- No phone number verification linked to your real carrier number
- VPN during account creation and every use session — and the same VPN for every session on that account
- Payment for any premium services only via cash or Monero, never a card linked to your real name
- A dedicated device or browser profile not linked to your real identity
- Never accessing the account from your home or work network

If an account was already created with any real-identity link (email, phone, device), assume it is already attributable and treat it as non-anonymous. Creating a new account with full separation from that point forward is the only repair.

---

## Section 4: Physical Countermeasures Against Mobile Fortify

### 4.1 Mask + Hat + Sunglasses Protocol

Most facial recognition algorithms rely on 68–128 facial landmarks. A medical-grade mask (N95 or FFP2) removes the lower 40% of the face; a hat with a full brim reduces overhead and oblique-angle acquisition; sunglasses defeat periorbital feature extraction. Combined, they reduce recognizable features to approximately 20%, dropping recognition accuracy from 99%+ to 40–60%.

**What this does not defeat**: Mobile Fortify used at close range by an agent actively trying to photograph your face. Physical distance from ICE agents during enforcement operations is more effective than mask-alone at close range.

### 4.2 If an Agent Approaches You with Mobile Fortify

1. **Do not confirm or deny identity**. Say: "I want to speak to an attorney before answering questions." A wrong biometric match is not legally conclusive.
2. **Request the match certainty score**. If below 80%, the match is weakly supported. Courts have found misidentification cases on this basis.
3. **Document the encounter** (when safe): time, date, location, agent names and badge numbers, exact language used about the scan result.
4. **Contact an immigration attorney immediately** after the encounter. Detentions based on weak Mobile Fortify matches are challengeable.

**Case study — Maine, 2026**: Portland residents Colleen Fagan and Elinor Hilton were photographed and biometrically scanned by ICE agents while they were lawfully observing immigration enforcement operations. One agent told Fagan, "Cause we have a nice little database" when she asked why he was scanning her face; another told Hilton she would be put on a "domestic terrorist watchlist." Both were US citizens documenting a public enforcement action. They filed suit (represented by Protect Democracy and Drummond Woodsum). The case illustrates that Mobile Fortify is being used against community observers and citizens, not only against immigration enforcement targets.

---

## Section 5: Device Security — Limiting Cellebrite Extraction

ICE holds an $11M contract with Cellebrite for forensic device extraction. If your phone is seized during an encounter, Cellebrite UFED can extract all Signal message history, location history, contacts, photos, and credentials — if the device is in "After First Unlock" (AFU) state.

### 5.1 The BFU/AFU Distinction

**Before First Unlock (BFU)**: Device has been powered on but the passphrase has never been entered since the last boot. Encryption keys are not in memory. Cellebrite can access only basic device metadata. **Cannot access**: messages, contacts, photos, app data.

**After First Unlock (AFU)**: Passphrase has been entered at least once since boot. Encryption keys are in memory. Cellebrite can access everything.

**The action that matters**: If you anticipate an ICE encounter — checkpoint, planned enforcement in your area, protest environment — **power off your phone fully** before the encounter. Not screen lock, not sleep mode. Full power off. This ensures the device is in BFU state if it is seized.

### 5.2 GrapheneOS — The Highest-Protection Option

GrapheneOS (grapheneos.org, free and open-source) on a Google Pixel 6–8 provides:
- Auto-reboot to BFU state after 18 hours without unlock (configurable under Settings > Security > Auto-reboot Timer)
- Hardware-level blocking of new USB connections when the device is locked
- Support for a duress PIN that wipes the device if entered

**Installation**: Detailed step-by-step guide in `implementation-guide.md` and `device-hardening-implementation-guide.md`. Installation takes 2–4 hours and requires a computer and USB cable. Group installation workshops (see Section 7.3) are significantly more effective than individual self-installation.

### 5.3 Minimum Device Security (If GrapheneOS Is Not Yet Installed)

On any device:
- Use a strong passphrase (12+ characters), not a PIN, not biometric
- Enable full-disk encryption (enabled by default on modern Android and iOS)
- Power off the device before any anticipated ICE encounter

---

## Section 6: Phone-Off Protocol and Geofencing Evasion

Penlink's geofencing capability means your phone's presence in a location leaves a record accessible to ICE without a warrant. To prevent your phone from being detected in a sensitive location:

**Before entering any location where an ICE operation may occur or where you are meeting with a community organization for immigration-related purposes**:
1. Power off your phone fully
2. Place it in a Faraday bag (Mission Darkness, Silent Pocket — $20–$80) if available. A Faraday bag blocks all radio signals at the hardware level, providing protection against any residual baseband firmware responses that occur even during power-off on some devices.

**What this does NOT accomplish**:
- It does not prevent your carrier from having a location record from before you powered off
- It does not prevent ALPR cameras from recording your vehicle in the area
- It does not delete data from before the power-off

**Practical application**: If you know ICE is active in your neighborhood or workplace area, power off your phone when leaving home and do not power it on again until you are in a different area. This limits the geofencing data Penlink can collect about your location during the enforcement window.

---

## Section 7: Financial Privacy — Reducing Financial Surveillance Vectors

Bank records, payment app transactions, and utility payment records are accessible to ICE via administrative subpoena and are cross-referenced in ELITE's address confidence scoring through data broker feeds.

### 7.1 Cash-First for Daily Expenses

Cash creates no electronic record. For groceries, transit, and everyday expenses: pay in cash. For recurring expenses like rent, a cash-purchased money order provides a payment record the landlord can verify without linking to a bank account (purchase at USPS, CVS, Walgreens, or 7-Eleven).

### 7.2 Prepaid Cards for Electronic Payments

Prepaid debit cards purchased with cash at retail stores allow electronic payments without a bank account in your name. Most prepaid cards do not require ID verification for loads under $500. Purchase with cash; reload with cash at retail reload locations.

### 7.3 Community Credit Unions Over Large Banks

Community credit unions have less automated risk-scoring infrastructure than large banks and more human relationship-based account management. De-banking risk (account closure by the institution) is lower at community credit unions. If your primary account is at a large bank and you are concerned about de-banking, establishing a parallel relationship at a community credit union provides a backup financial infrastructure.

---

## Section 8: Arrest and Detention Protocol

If ICE takes you into custody, these are the only things you should say and do until you have spoken with an attorney.

### 8.1 In the Moment

**Say only**: "I am exercising my right to remain silent. I want to speak to an attorney."

**Do NOT**:
- Sign any documents (not an I-9, not consent to search, not anything)
- Agree to voluntary departure or voluntary return — this forecloses future legal challenges to the arrest
- Consent to a search of your phone or vehicle

### 8.2 After Arrest

1. Request the facility's name and address — you will need this for your attorney
2. Ask for your phone call — use it to call an immigration attorney or a family member who can contact one
3. Do not discuss your case with other detainees — anything you say can be used against you
4. Do not refuse medical care
5. Keep all paperwork you receive

### 8.3 Legal Options to Know

- **Asylum**: If you fear return to your home country, you can request asylum during detention/deportation proceedings. This is available regardless of how you entered.
- **U visa**: Available if you are a victim of certain crimes and have cooperated with law enforcement
- **T visa**: Available if you are a victim of human trafficking
- **VAWA**: Available to victims of domestic violence
- **TPS (Temporary Protected Status)**: If your country is designated, you may be eligible
- **Stays of removal**: An immigration judge can pause a deportation. An attorney must file for this.

---

## Section 9: Implementation Checklists

### Checklist A: 3 Days Before (for anyone in an elevated-risk situation or enforcement-active area)

- [ ] Complete LexisNexis Accurint opt-out: https://optout.lexisnexis.com/
- [ ] California residents: complete DROP platform: https://privacy.ca.gov/drop/
- [ ] Set all social media accounts to private
- [ ] Remove or archive posts with location information or immigration-related content
- [ ] Disable camera location access on your phone
- [ ] Identify immigration attorney; write their number on paper and carry it in your wallet
- [ ] Tell two trusted people your plan and attorney's number
- [ ] If you operate any social media accounts that post about ICE activity or immigration enforcement: verify those accounts were created and are used with complete identity separation (separate email, VPN for every session, no real phone number). If not, stop posting from those accounts. (Section 3.4)

### Checklist B: Day-Of (for any day when enforcement activity is anticipated)

- [ ] Leave phone powered off from before leaving home
- [ ] If phone must be on, place in Faraday bag before entering any risk area
- [ ] Wear a mask, hat, and sunglasses when in public spaces where enforcement is occurring
- [ ] Carry the physical attorney card in your wallet (not stored only in phone)
- [ ] Know the attorney's number by memory if possible, or have it written on your arm
- [ ] Travel with cash rather than payment cards
- [ ] If driving: vary your route; do not park directly in front of community organization offices
- [ ] If approached by ICE agents: do not consent to biometric collection (facial photograph, iris scan) outside a formal arrest. Say: "I do not consent to biometric collection. I want to speak to an attorney." (Section 1.3)

### Checklist C: Post-Encounter (after any ICE contact or near-contact)

- [ ] Document the encounter: time, date, location, agent names/badge numbers, what was said
- [ ] Contact your immigration attorney as soon as safely possible
- [ ] Tell trusted community contacts what happened so they can escalate if you go silent
- [ ] Review whether your threat level has increased; consider upgrading your security tier
- [ ] Do not post about the encounter on public social media until you have spoken with your attorney

### Checklist D: Ongoing Maintenance (monthly/quarterly)

- [ ] Every 90 days: re-submit LexisNexis and secondary data broker opt-outs (or subscribe to Incogni for automation)
- [ ] Monthly: review social media privacy settings — platforms reset permissions after updates
- [ ] After any device update: confirm camera location access is still disabled
- [ ] Quarterly: review who has your attorney's contact information and confirm it is current

---

## Section 10: Tier-by-Tier Implementation

### Tier 1: Essential (All Undocumented Immigrants — No Exceptions)

Time to implement: 4–6 hours. Cost: $0 required, $7.99/month optional (Incogni).

1. Complete LexisNexis Accurint opt-out (Part 2.1) — 30 minutes
2. California residents: complete DROP platform (Part 2.2) — 30 minutes
3. Submit secondary data broker opt-outs (Part 2.3) — 45 minutes
4. Set all social media to private; disable camera location access (Part 3) — 30 minutes
5. Install Signal; enable disappearing messages (1-day default); set "Who can find me" to Nobody — 30 minutes
6. Write immigration attorney's name and phone number on a physical card; carry it always (Part 8) — 5 minutes
7. Tell two trusted people your attorney's contact information — 15 minutes

### Tier 2: Intermediate (Activists, High-Risk Individuals, Enforcement-Area Residents)

All of Tier 1, plus:

8. Install GrapheneOS on a Pixel device (Part 5.2) — 2–4 hours; use a group workshop if possible
9. Configure GrapheneOS auto-reboot to 18 hours
10. Power off phone protocol: practice powering off phone at start of each day in enforcement-active period
11. Purchase a Faraday bag (Mission Darkness or equivalent — $20–$80)
12. Subscribe to Incogni ($7.99/month) for automated data broker maintenance
13. Set up a VoIP number (MySudo or JMP.chat) and register Signal with it instead of your carrier number

### Tier 3: Advanced (Organizing Leaders, Direct Investigation Targets)

All of Tier 2, plus:

14. Install Qubes OS or Tails OS for sensitive organizing work
15. Obtain a YubiKey hardware security key for all critical accounts
16. Establish separate SIM cards for personal, organizing, and legal communications (Part 11 in `immigration-surveillance-evasion-playbook.md`)
17. Retain immigration counsel proactively; discuss incident response before an incident occurs
18. Implement three-SIM isolation model for phone communications

---

## Section 11: Organizational Guidance — For Legal Aid Organizations

### Workshop Curriculum (High Impact, Low Friction)

**30-minute data broker opt-out group session** (in-person, client-facing): Guide all clients through LexisNexis Accurint opt-out at a single group session. Completion rates in group settings approach 100%; written instructions alone achieve much lower rates. Provide a laptop for clients who do not have one.

**90-minute device security workshop**: GrapheneOS installation and Signal configuration. Bring 3–4 volunteer tech supporters per 10 clients. Require clients to bring their Pixel device and a laptop, or provide loaner laptops. Focus on: passphrase (not biometric), auto-reboot timer, disappearing messages.

**60-minute Know Your Rights with rehearsal**: Cover the arrest protocol (Section 8), prepare attorney cards, and do a 10-minute "what do you say and do" rehearsal. Rehearsal creates durable behavioral change that written materials alone do not.

### Organizational Security Measures

- Use Signal (not email) for all attorney-client communication
- Store client files only in services with client-side encryption
- Staff computers holding client data must use full-disk encryption
- Train all staff — including administrative staff — on the Mobile Fortify field encounter protocol (Section 4.2)
- Field staff accompanying clients should have devices meeting Tier 2 standards

---

## Section 12: Community Resource Directory

### Legal Services
- **RAICES**: raicestexas.org — direct legal services, community organizing
- **NILC (National Immigration Law Center)**: nilc.org — policy and practitioner training
- **Catholic Charities**: free immigration legal services in most dioceses
- **American Immigration Council**: americanimmigrationcouncil.org
- **NDLON (National Day Laborer Organizing Network)**: ndlon.org — know-your-rights training, day laborer organizing

### Litigation and Accountability
- **ACLU**: aclu.org — filed suits challenging DHS administrative subpoenas and Mobile Fortify deployment
- **EFF**: eff.org — primary investigative source on Mobile Fortify, Flock Safety ALPR, and data broker ICE contracts
- **Brennan Center for Justice**: brennancenter.org — social media monitoring policy research

### Tools
- **Signal**: signal.org
- **GrapheneOS**: grapheneos.org
- **Mullvad VPN**: mullvad.net
- **Tor Browser**: torproject.org
- **Incogni** (data broker removal): incogni.com
- **Briar** (anonymous mesh messenger): briarproject.org

---

## Summary: Five Things That Matter Most

If a client will only do five things, these are the five:

1. **Opt out of LexisNexis Accurint** (degrades the single most important ICE address data source)
2. **Set all social media to private and disable camera location access** (closes the photo EXIF and social graph exposure)
3. **Write your attorney's phone number on a physical card and carry it** (works when your phone is dead, seized, or off)
4. **Power off your phone before any ICE encounter or enforcement-active area** (prevents Cellebrite extraction and Penlink geofencing)
5. **Know the three sentences**: "I am exercising my right to remain silent. I want to speak to an attorney. I do not consent to a search."

---

**For questions and updates**: Contact immigration counsel or the RAICES legal team (raicestexas.org).

**Version**: 1.1 (Q2 2026 patches applied June 6, 2026)
**Created**: May 7, 2026
**Last updated**: June 6, 2026
**Next scheduled review**: July 26, 2026 (quarterly corpus review)
**Cross-references**: `opsec-playbook.md`, `implementation-guide.md`, `device-hardening-implementation-guide.md`, `palantir-threat-model.md`, `threat-model.md`, `activist-organizing-playbook.md` (Section 2 social media hygiene is directly applicable), `THREAT_ENVIRONMENT_Q2_2026_UPDATE.md`, `PHASE_2_THREAT_INTEGRATION_CHECKLIST.md`

**Sources**:

*Original sources (v1.0/v1.1 initial)*:
- [ELITE user guide and contract documentation — 404media.co](https://www.404media.co/elite-the-palantir-app-ice-uses-to-find-neighborhoods-to-raid/)
- [Medicaid data sharing with ICE — KFF Health News](https://kffhealthnews.org/news/article/ice-immigrants-medicaid-data-sharing-hospitals-states-deportation/)
- [Mobile Fortify — Wikipedia](https://en.wikipedia.org/wiki/Mobile_Fortify)
- [EFF — Demand halt to Mobile Fortify](https://www.eff.org/deeplinks/2025/11/rights-organizations-demand-halt-mobile-fortify-ices-handheld-face-recognition)
- [ICE facial recognition app powered by NEC — Biometric Update](https://www.biometricupdate.com/202601/ice-facial-recognition-app-mobile-fortify-powered-by-nec)
- [Penlink geofencing capability — 404media.co](https://www.404media.co/inside-ices-tool-to-monitor-phones-in-entire-neighborhoods/)
- [ICE surveillance shopping spree — EFF](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree)
- [Maine ICE observer lawsuit — NPR](https://www.npr.org/2026/02/23/nx-s1-5722988/dhs-lawsuit-biometrics-domestic-terrorism)
- [DHS administrative subpoenas — TechCrunch](https://techcrunch.com/2026/02/14/homeland-security-reportedly-sent-hundreds-of-subpoenas-seeking-to-unmask-anti-ice-accounts/)
- [Thomson Reuters CLEAR and ICE — LawNext](https://www.lawnext.com/2026/04/the-legal-tech-giants-powering-ice-part-1-how-thomson-reuters-and-lexisnexis-helped-support-americas-immigration-surveillance-machine.html)
- [ICE use of Medicaid data — Stateline](https://stateline.org/?p=16545)
- [Social media surveillance immigrants — Borderless Magazine](https://borderlessmag.org/2026/01/08/ice-social-media-surveillance-immigration-applications-enforcement-chicago/)
- [ICE surveillance web — NPR](https://www.npr.org/2026/03/04/nx-s1-5717031/ice-dhs-immigrants-surveillance-confrontation-deportation-mobile-fortify)
- [ICE church raids — Axios](https://www.axios.com/2025/01/21/trump-deportation-ice-churches-schools-raids)

*Q2 2026 patch sources (added June 6, 2026)*:
- [ICE awards Bi2 $25M contract for 1,570 biometric iris scanners — The Register (May 29, 2026)](https://www.theregister.com/public-sector/2026/05/29/ice-awards-bi2-25m-contract-for-1570-biometric-scanners/5248733)
- [ICE expands field biometric identification with $25M iris recognition contract — Biometric Update](https://www.biometricupdate.com/202605/ice-expands-field-biometric-identification-with-25m-iris-recognition-contract)
- [ICE Awards $25.1M No-Bid Iris-Scanning Contract to BI2 Technologies — ID Tech Wire](https://idtechwire.com/ice-awards-25-1m-no-bid-iris-scanning-contract-to-bi2-technologies/)
- [ICE contracts with Clearview AI — Immigration Policy Tracking Project](https://immpolicytracking.org/policies/reported-ice-contracts-with-clearview-ai-for-facial-recognition-technology/)
- [ICE AI surveillance tracking Americans — American Immigration Council](https://www.americanimmigrationcouncil.org/blog/ice-ai-surveillance-tracking-americans/)
- [ICE, FBI expand facial recognition use to protest investigations — Biometric Update (February 2026)](https://www.biometricupdate.com/202602/ice-fbi-expand-facial-recognition-use-to-protest-investigations)
- [How DOGE improperly accessed Social Security data — NPR](https://www.npr.org/2026/01/23/nx-s1-5684185/doge-data-social-security-privacy)
- [Court orders probe of DOGE secret voter data deal — Democracy Docket](https://www.democracydocket.com/news-alerts/court-orders-probe-of-doges-secret-voter-data-deal/)
- [Court orders more discovery in DOGE data access case — Democracy Forward](https://democracyforward.org/news/press-releases/court-orders-more-discovery-from-the-government-in-case-challenging-doges-unlawful-access-to-sensitive-personal-data/)
- [DOGE likely violated order on Social Security data — FedScoop](https://fedscoop.com/doge-access-social-security-data-court-filing/)
- [Judge orders OPM to halt sharing Americans' personal data with DOGE — AFGE](https://www.afge.org/article/judge-orders-opm-to-halt-sharing-americans-personal-data-with-doge/)
- [Thomson Reuters LEIDS-5 expiration and pushback — LawNext (April 29, 2026)](https://xira.com/p/2026/04/29/the-legal-tech-giants-powering-ice-part-2-the-pushback-employees-shareholders-lawyers-and-the-fight-over-may-31/)
- [Ahead of June 10 shareholder vote, union investor renews push — LawNext (May 2026)](https://www.lawnext.com/2026/05/ahead-of-june-10-shareholder-vote-union-investor-renews-push-for-thomson-reuters-to-assess-human-rights-impact-of-its-products-used-by-ice.html)
- [DHS withdraws subpoena targeting critic — ACLU](https://www.aclu.org/press-releases/department-of-homeland-security-withdraws-subpoena-targeting-man-who-criticized-them)
- [Lawsuit: DHS, ICE sued over immigration subpoenas to ID social media users — Military.com (April 22, 2026)](https://www.military.com/daily-news/2026/04/22/lawsuit-dhs-ice-sued-over-immigration-subpoenas-id-social-media-users.html)
- [Open letter to tech companies on lawless DHS subpoenas — EFF](https://www.eff.org/deeplinks/2026/02/open-letter-tech-companies-protect-your-users-lawless-dhs-subpoenas)
- [FOIA lawsuit on ICE subpoenas to unmask social media users — ACLU Pennsylvania / Philadelphia Inquirer](https://www.inquirer.com/news/pennsylvania/ice-foia-lawsuit-aclu-subpoenas-social-media-dhs-20260420.html)
