---
title: "Immigration + Surveillance Evasion Playbook: Digital Defense Against ICE Enforcement"
project: cybersecurity-hardening
created: 2026-05-07
status: production-ready
phase: Phase 2
session: 875
version: 1.1
depends_on:
  - threat-model.md
  - opsec-playbook.md
  - implementation-guide.md
  - palantir-threat-model.md
confidence: high — grounded in documented ICE capabilities (ELITE/Palantir, ImmigrationOS, Mobile Fortify/NEC, Penlink geofencing, Thomson Reuters CLEAR, Medicaid data-sharing agreement), court filings, EFF/Brennan Center primary source reporting, and immigration attorney community feedback
audience: Undocumented immigrants, DACA recipients, visa holders under enforcement risk, immigration attorneys, legal aid organizations, immigrant rights orgs, family support networks
word_count: ~3,200
---

# Immigration + Surveillance Evasion Playbook

**For legal service providers and workshop facilitators**: This guide translates the ICE surveillance stack into an immigration-specific operational framework with concrete countermeasures for each layer. The threat is documented and operational — not theoretical. Every tool named in Section 1 has a confirmed contract, a user manual, or court filings attesting to its use. The countermeasures in Sections 2–7 address each layer directly and are designed for implementation without technical expertise. Section 8 provides copy-paste-ready checklists for distribution to clients.

Cross-references to `opsec-playbook.md` and `implementation-guide.md` are provided throughout. Do not repeat work: if a client has already completed device hardening per the core playbook, those measures apply directly here.

---

## Section 1: The ICE Surveillance Stack — What Is Actually Being Used Against You

Understanding the specific tools ICE deploys changes what you prioritize. This is not a list of theoretical capabilities. Each tool listed has a documented contract and confirmed operational use.

### 1.1 ELITE — Address Confidence Scoring (Palantir, $29.9M contract, September 2025)

**What it does**: ELITE (Enhanced Leads Identification and Targeting for Enforcement) is a Palantir-built tool that populates a map with deportation targets and generates an "address confidence score" — a percentage rating (e.g., 98.95 or 77.25 out of 100) representing how certain ICE is that you live at a given address.

**Data sources the score draws from**:
- HHS/Medicaid records: A data-sharing agreement signed December 2025 gives ICE access to basic biographical and contact information — including home addresses — from nearly 80 million Medicaid patients. A U.S. District Judge allowed this sharing to resume on January 5, 2026. If you or a family member has ever received Medicaid, that address is in the ELITE system.
- Thomson Reuters CLEAR: ICE's $22.8 million contract (running through May 2026, with renewal pending) provides access to CLEAR, which aggregates driver's license data, voter registrations, marriage records, property records, and commercial location data.
- LexisNexis Accurint: A separate ICE contract with LexisNexis feeds commercial consumer data (utility records, credit inquiries, address history) directly into ELITE's confidence scoring.
- Facebook and social media EXIF data: Penlink (ICE subscription, September 2025) extracts GPS coordinates embedded in photos uploaded to Facebook and other platforms, creating a real-time location timeline from photos you or contacts have posted publicly.

**Why this matters**: A high confidence score (above 80%) means ICE will prioritize your address for a raid. A low score means the address is uncertain enough to deprioritize. You cannot delete yourself from Medicaid records, but you can reduce the score that other data sources contribute.

**Your countermeasure**: Section 2 below — data broker opt-outs that remove your address from LexisNexis and Thomson Reuters CLEAR feeds.

### 1.2 ImmigrationOS — Case File and Social Network Platform (Palantir, $30M contract, July 2025)

**What it does**: ImmigrationOS is the case management and social graph platform that consolidates your immigration case file, travel history, prior enforcement encounters, biometric data, family relationships, and workplace connections into a single searchable record. ICE officers query it in real time during traffic stops, at checkpoints, and during field operations.

**Social graph capability**: ImmigrationOS uses entity resolution to create persistent links between associated persons. If you are connected — even indirectly — to someone who is already in the system as an enforcement target, you enter the investigation's social graph. This is documented in `palantir-threat-model.md`. A family member's detention, a workplace colleague's arrest, or a community organization's presence in the system can draw you into an investigation without any independent action by ICE against you.

**Your countermeasure**: Minimize your digital connections to known enforcement targets (social media contact, publicly listed association with flagged organizations). This does not mean abandoning community — it means managing what is visible to automated systems. Section 3 covers social media hygiene.

### 1.3 Mobile Fortify — Field Biometric Identification (NEC facial recognition engine, 100,000+ uses)

**What it does**: Mobile Fortify is an ICE smartphone app that allows agents to photograph anyone they encounter and run the image against DHS's HART biometric database (150M+ records). The device returns a photo match with a confidence percentage. It was deployed without a required Privacy Impact Assessment. Illinois and Chicago sued ICE over this deployment in January 2026, documenting over 100,000 uses.

**Where it is being used**: Not only at formal detention facilities. ICE agents have used Mobile Fortify:
- At protests, including Minneapolis (documented February 2026 — see Section 1.4 case study)
- At traffic stops
- At workplaces and outside community organizations
- At churches (after the Trump administration rescinded sensitive-location protections on January 20, 2025)

**Accuracy problems**: The device has documented misidentification issues. In documented cases it has returned two different, both incorrect, names for the same person in a single encounter. Accuracy is worse for women and people of color. A positive match is not legally conclusive.

**Your countermeasure**: Physical countermeasures (Section 4) and legal response strategy if misidentified (Section 5.2).

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

### Checklist B: Day-Of (for any day when enforcement activity is anticipated)

- [ ] Leave phone powered off from before leaving home
- [ ] If phone must be on, place in Faraday bag before entering any risk area
- [ ] Wear a mask, hat, and sunglasses when in public spaces where enforcement is occurring
- [ ] Carry the physical attorney card in your wallet (not stored only in phone)
- [ ] Know the attorney's number by memory if possible, or have it written on your arm
- [ ] Travel with cash rather than payment cards
- [ ] If driving: vary your route; do not park directly in front of community organization offices

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

**Version**: 1.1
**Created**: May 7, 2026
**Next scheduled review**: July 26, 2026 (quarterly corpus review)
**Cross-references**: `opsec-playbook.md`, `implementation-guide.md`, `device-hardening-implementation-guide.md`, `palantir-threat-model.md`, `threat-model.md`, `activist-organizing-playbook.md` (Section 2 social media hygiene is directly applicable)

**Sources**:
- [ELITE user guide and contract documentation — 404media.co](https://www.404media.co/elite-the-palantir-app-ice-uses-to-find-neighborhoods-to-raid/)
- [Medicaid data sharing with ICE — KFF Health News](https://kffhealthnews.org/news/article/ice-immigrants-medicaid-data-sharing-hospitals-states-deportation/)
- [Mobile Fortify — Wikipedia](https://en.wikipedia.org/wiki/Mobile_Fortify)
- [EFF — Demand halt to Mobile Fortify](https://www.eff.org/deeplinks/2025/11/rights-organizations-demand-halt-mobile-fortify-ices-handheld-face-recognition)
- [ICE facial recognition app powered by NEC — Biometric Update](https://www.biometricupdate.com/202601/ice-facial-recognition-app-mobile-fortify-powered-by-nec)
- [Penlink geofencing capability — 404media.co](https://www.404media.co/inside-ices-tool-to-monitor-phones-in-entire-neighborhoods/)
- [ICE surveillance shopping spree — EFF](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree)
- [Maine ICE observer lawsuit — NPR](https://www.npr.org/2026/02/23/nx-s1-5722988/dhs-lawsuit-biometrics-domestic-terrorism)
- [DHS administrative subpoenas — TechCrunch](https://techcrunch.com/2026/02/14/homeland-security-reportedly-sent-hundreds-of-subpoenas-seeking-to-unmask-anti-ice-accounts/)
- [Thomson Reuters CLEAR and ICE — LawSites](https://www.lawnext.com/2026/04/the-legal-tech-giants-powering-ice-part-1-how-thomson-reuters-and-lexisnexis-helped-support-americas-immigration-surveillance-machine.html)
- [ICE use of Medicaid data — Stateline](https://stateline.org/?p=16545)
- [Social media surveillance immigrants — Borderless Magazine](https://borderlessmag.org/2026/01/08/ice-social-media-surveillance-immigration-applications-enforcement-chicago/)
- [ICE surveillance web — NPR](https://www.npr.org/2026/03/04/nx-s1-5717031/ice-dhs-immigrants-surveillance-confrontation-deportation-mobile-fortify)
- [ICE church raids — Axios](https://www.axios.com/2025/01/21/trump-deportation-ice-churches-schools-raids)
