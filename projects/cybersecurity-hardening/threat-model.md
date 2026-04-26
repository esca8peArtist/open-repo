---
title: "Threat Model: Government Surveillance Infrastructure (2025-2026)"
project: cybersecurity-hardening
created: 2026-04-26
status: initial-draft
confidence: high — primary sources (FOIA disclosures, court filings, government contracts, investigative journalism, Amnesty International)
---

# Threat Model: Government Surveillance Infrastructure (2025-2026)

**Purpose**: This document maps the actual, verified capabilities of U.S. government surveillance systems as a foundation for building realistic OpSec countermeasures. It covers Palantir's government contracts, NSA signals intelligence, FBI investigative tools, law enforcement data-broker pipelines, and the DOGE-driven data consolidation effort currently underway.

**Scope**: Federal surveillance actors with confirmed capabilities as of April 2026. This is not speculative — every capability described here has a primary or near-primary source citation.

---

## I. The Central Threat: Palantir as the Integration Layer

Palantir Technologies is not merely a contractor. It functions as the data integration backbone connecting previously siloed government databases into a unified, searchable intelligence environment. Understanding Palantir is the prerequisite for understanding the rest of the threat landscape.

### A. Scale and Financial Commitment (Confirmed)

- **$970.5 million** in federal contracts in 2025, nearly double the prior year. ([The Hill](https://thehill.com/policy/technology/5667232-palantir-trump-administration-surveillance/))
- **$10 billion** U.S. Army Enterprise Service Agreement (July 2025), consolidating 75 previously separate data contracts. ([State of Surveillance](https://stateofsurveillance.org/articles/surveillance/palantir-government-surveillance-ecosystem-billions/))
- **$130 million** IRS Criminal Investigation contract since 2018 for the Lead and Case Analytics (LCA) platform. ([The Intercept, April 24, 2026](https://theintercept.com/2026/04/24/palantir-irs-contract-data/))
- **$30 million** ImmigrationOS contract with ICE (April 2025), prototype due September 2025. ([immpolicytracking.org](https://immpolicytracking.org/policies/reported-palantir-awarded-30-million-to-build-immigrationos-surveillance-platform-for-ice/))
- **$29.9 million** ELITE platform contract for ICE (September 2025, running through at least 2026). ([404 Media](https://www.404media.co/elite-the-palantir-app-ice-uses-to-find-neighborhoods-to-raid/))

Conflict of interest note: Stephen Miller, the Trump administration's chief architect of immigration policy, holds a substantial financial stake in Palantir. ([ACLU](https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup))

---

### B. Platform Architecture

Palantir operates three core platforms relevant to government surveillance:

**1. Gotham** — The law enforcement and intelligence platform. Used by the CIA, NSA, FBI, DOD, ICE, and CBP. Designed for identity linking, relationship mapping, and predictive targeting. This is the primary intelligence tool.

**2. Foundry** — The enterprise data integration and pipeline platform. Used by IRS, Army, and commercial clients. Connects 200+ data source types into a unified ontology. This is the data ingestion backbone.

**3. AIP (Artificial Intelligence Platform)** — Launched 2023, integrated into both Gotham and Foundry. Deploys large language models and agentic AI on top of existing data pipelines. Government use is expanding rapidly — the Army's $10B ESA uses AIP. ([Palantir AIP docs](https://www.palantir.com/platforms/aip/))

---

### C. Confirmed Palantir Tools Deployed Against Immigrants and Activists

#### Tool 1: ELITE (Enhanced Leads Identification and Targeting for Enforcement)
**Contract value**: $29.9M (September 2025–2026+)
**What it does**:
- Displays potential deportation targets as pins on a map interface
- Generates a dossier per person (name, photo, Alien number, DOB)
- Provides an **address confidence score** (example scores in the user guide: 98.95/100, 77.25/100)
- Identifies neighborhoods with high concentrations of people with "immigration nexus"
- Described internally as "kind of like Google Maps" for finding deportation targets

**Confirmed data sources feeding ELITE**:
- HHS / Medicaid records (this is the most alarming — medical assistance records used for targeting)
- USCIS databases
- CLEAR (Thomson-Reuters' commercial law enforcement data product)
- DMV records
- Additional undisclosed government databases

Sources: [EFF](https://www.eff.org/deeplinks/2026/01/report-ice-using-palantir-tool-feeds-medicaid-data), [404 Media](https://www.404media.co/here-is-the-user-guide-for-elite-the-tool-palantir-made-for-ice/), [ACLU](https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup)

---

#### Tool 2: ICM (Investigative Case Management) — in use since 2014
**What it does**:
- Manages the full deportation case lifecycle
- Enables agents to construct cases against individuals
- Consolidates: schooling records, family relationships, employment history, biometric traits, criminal records, current and previous addresses

**Confirmed data sources**:
- FBI, DEA, ATF databases
- SEVIS (Student and Exchange Visitor Information System) — tracks foreign students
- Phone records
- Field-seized device data
- Multiple interconnected federal and commercial databases

Source: [ACLU](https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup)

---

#### Tool 3: ImmigrationOS — prototype September 2025, contract through 2027
**What it does** (three primary functions):
1. **Targeting**: AI-assisted selection of who to apprehend, with priority weighting for visa overstays, alleged gang affiliations, and other red flags
2. **Self-deportation monitoring**: Near real-time tracking of whether individuals are leaving voluntarily
3. **Lifecycle logistics**: Optimization of the full deportation pipeline from identification to removal

**Data sources**: Leverages full ICM data ecosystem plus "external" sources — the contract language explicitly references non-DHS data. Palantir confirmed in its Amnesty International response that ImmigrationOS serves ICE's Enforcement and Removal Operations mission directly.

**OSINT/Social media surveillance**: ImmigrationOS includes automated OSINT capabilities including real-time social media monitoring across multiple platforms, sentiment analysis, and data aggregation from public and private sources. This is the system likely involved in "Catch and Revoke" visa/residency revocations of pro-Palestinian student protesters.

Sources: [American Immigration Council](https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/), [Amnesty International (August 2025)](https://www.amnesty.org/en/latest/news/2025/08/usa-global-tech-made-by-palantir-and-babel-street-pose-surveillance-threats-to-pro-palestine-student-protestors-migrants/)

---

#### Tool 4: IRS Lead and Case Analytics (LCA) Platform — since 2018
**What it does**:
- "Massive-scale" data mining described in contract documents
- Searches "connections from millions of records with thousands of links"
- Maps social networks among investigation targets
- Identifies suspects through IP analysis
- Visualizes relationship chains across federal databases

**Confirmed data sources**:
- Individual tax forms and returns (1040, corporate filings)
- Affordable Care Act enrollment data
- Bank statements and financial transactions
- FinCEN (Treasury Financial Crimes Enforcement Network) records — includes Suspicious Activity Reports
- Cryptocurrency wallet data: Bitcoin, Ethereum, Litecoin, Ripple
- Dark web data from seized servers and exchangers (Coinbase, others)
- Communications metadata: calls, texts, emails
- IP address records

**Current concern**: The IRS Criminal Investigation division has reportedly shifted focus toward investigating "left-leaning groups" under Trump's direction. The LCA system gives investigators the technical capacity to do this at scale.

Sources: [The Intercept](https://theintercept.com/2026/04/24/palantir-irs-contract-data/), [TechCrunch](https://techcrunch.com/2026/04/24/palantir-is-reportedly-helping-the-irs-investigate-financial-crimes/)

---

#### Tool 5: Falcon (ICE field operations app) — used until 2022
Historical: Tracked agents' and targets' physical locations during enforcement operations in real time. Decommissioned in 2022 per public reporting, likely superseded by ELITE.

Source: [State of Surveillance](https://stateofsurveillance.org/articles/government/palantir-immigrationos-ice-contract-2025/)

---

## II. The Data Broker Pipeline: Commercial Surveillance Without a Warrant

Government agencies are legally permitted to purchase commercially available data that would require a warrant to obtain directly. This is the single most significant Fourth Amendment gap in contemporary surveillance law.

### A. The Legal Framework

The **"third-party doctrine"** holds that information voluntarily shared with a third party (your carrier, your bank, your app) loses Fourth Amendment protection. Purchasing commercially aggregated data from brokers exploits this doctrine to circumvent warrant requirements entirely.

A DHS Inspector General report (September 28, 2023) **confirmed that CBP, ICE, and the Secret Service all violated federal law** in their warrantless purchase and use of location data — but the violations were procedural, not prohibitions on the practice itself. ([NPR, March 2026](https://www.npr.org/2026/03/25/nx-s1-5752369/ice-surveillance-data-brokers-congress-anthropic))

---

### B. Key Data Brokers with Government Contracts

**LexisNexis (Accurint product)**
- 2021 DHS contract: $9.75M for "identity verification services" — gives ICE access to one of the world's largest commercial surveillance databases covering virtually every American adult
- Accurint aggregates: court records, property records, financial records, address history, relatives, associates
- Active ICE litigation: plaintiffs allege Accurint violates consent and privacy laws for non-citizens
- May 2025: LexisNexis confirmed a breach of 364,000+ individuals via a third-party development platform

Sources: [The ICE-Lexisnexus journal paper](https://journals.sagepub.com/doi/10.1177/20539517251351323), [TechCrunch breach report](https://techcrunch.com/2025/05/28/data-broker-giant-lexisnexis-says-breach-exposed-personal-information-of-over-364000-people/)

**Venntel (owned by Gravy Analytics)**
- ICE Enforcement and Removal Operations used Venntel to "access/gain information to accurately identify digital devices"
- Collects location data harvested from smartphone apps (through the ad SDK ecosystem) — this is commercial location data derived from apps you install
- FTC alleged in 2024 that Venntel sold sensitive consumer location data without proper consent
- Note: Gravy Analytics itself was breached in early 2025

Source: [Vice investigative report](https://www.vice.com/en/article/ice-dhs-fbi-location-data-venntel-apps/)

**Babel Street**
- Provides social media monitoring and OSINT aggregation to DHS agencies
- Amnesty International (August 2025) identified Babel Street technology as posing direct surveillance threats to pro-Palestine protesters
- Babel Street did not respond to Amnesty's inquiry

Source: [Amnesty International](https://www.amnesty.org/en/latest/news/2025/08/usa-global-tech-made-by-palantir-and-babel-street-pose-surveillance-threats-to-pro-palestine-student-protestors-migrants/)

**Acxiom, Epsilon**
- Not confirmed in specific government contracts for immigration enforcement, but part of the broader commercial data ecosystem
- Acxiom claims data on 2.5 billion consumers globally; average broker holds ~1,500 data points per individual

Source: [State of Surveillance](https://stateofsurveillance.org/articles/corporate/data-brokers-ice-contracts/)

**CLEAR (Thomson-Reuters)**
- Direct confirmed integration into Palantir's ELITE platform
- Provides law enforcement with public records, address verification, background check infrastructure

---

### C. Ad Tech Location Data (Emerging, 2026)

ICE filed a market research request in January 2026 explicitly seeking "ad tech" data tools — the first time ICE has referenced advertising technology in a federal procurement document. This would allow ICE to purchase location data derived from mobile advertising identifiers (MAIDs), which are harvested by thousands of apps and aggregated by data brokers.

Source: [The Register](https://www.theregister.com/2026/01/27/ice_data_advertising_tech_firms/)

**Practical implication**: Any phone running apps with advertising SDKs — which is nearly every commercial smartphone — continuously broadcasts its location to data brokers who can legally sell that data to law enforcement without a warrant.

---

## III. NSA Signals Intelligence

### A. PRISM (Section 702 Downstream Collection)

PRISM authorizes the NSA to compel U.S.-based tech companies to provide direct access to stored user data for named non-U.S. targets. The legal authority is Section 702 of FISA.

**Current scope (2025-2026)**:
- 349,823 surveillance targets in 2025 — up from ~246,000 in 2022
- Companies that have complied include: Google, Apple, Microsoft, Meta, Yahoo, Skype, YouTube, AOL
- Stored data accessible: email content, chat messages, video/voice calls, photos, stored documents, connection logs

**The "backdoor search" problem for Americans**: While PRISM targets non-U.S. persons abroad, an untold but significant amount of Americans' communications are swept in when they communicate with targeted individuals. The NSA, FBI, and CIA can then query this incidentally collected U.S. person data. A federal district court held on January 21, 2025 that a warrant is required for queries using American identifiers — but this ruling is on appeal.

**Section 702 reauthorization**: RISAA (April 20, 2024) extended Section 702 through **April 20, 2026**. As of this writing, reauthorization debate is active. The Senate rejected an amendment that would have required warrants for U.S. person queries.

Sources: [PRISM Wikipedia](https://en.wikipedia.org/wiki/PRISM), [NPR Section 702 explainer](https://www.npr.org/2026/04/14/nx-s1-5768270/what-to-know-about-section-702-surveillance), [Penn CERL](https://www.penncerl.org/the-rule-of-law-post/after-a-bruising-battle-fisa-section-702-lives-on-now-let-the-2026-section-702-reauthorization-debate-begin/)

---

### B. Upstream Collection (Section 702 + Internet Backbone Taps)

Upstream collection intercepts data directly from the Internet backbone — fiber optic cables and switching infrastructure — rather than from company servers.

**Confirmed technical infrastructure**:
- NSA taps at AT&T switching facilities (Room 641A in San Francisco — publicly confirmed in 2006 AT&T EFF lawsuit)
- More than a dozen major U.S. Internet switching stations with filtering equipment
- Data flowing "to," "from," and formerly "about" (discontinued in 2017 after FISC order) surveillance selectors

**XKeyscore**: The NSA's primary search and analysis tool across collected data. Functions as a clearinghouse across Upstream and PRISM-collected data. Content stored 3-5 days; metadata stored up to 30 days on rolling basis. Enables analysts to search by email, username, IP address, activity type.

Sources: [XKeyscore Wikipedia](https://en.wikipedia.org/wiki/XKeyscore), [Upstream collection Wikipedia](https://en.wikipedia.org/wiki/Upstream_collection)

---

### C. What NSA Can and Cannot Do (Based on Known Constraints)

**Can do (confirmed)**:
- Collect and store communications metadata at scale for extended periods
- Access content of communications to/from targeted selectors under Section 702
- Conduct "contact chaining" — mapping everyone a target communicates with
- Query incidentally collected U.S. person data (status legally contested as of 2025)
- Access cloud-stored data (documents, photos, backups) of targeted individuals

**Appears constrained by (per current law)**:
- Direct warrantless targeting of U.S. persons on U.S. soil requires a traditional FISA order or criminal warrant
- Using NSA intelligence as direct evidence in domestic criminal prosecutions (though "parallel construction" circumvents this in practice)

**Uncertainty**: The extent to which AI/ML tools are now applied to bulk-collected metadata for predictive targeting of domestic individuals is not publicly confirmed.

---

## IV. FBI Investigative Tools

### A. National Security Letters (NSLs)

NSLs are administrative subpoenas requiring no prior judicial approval. The FBI issues thousands per year.

**What NSLs compel disclosure of**:
- Name, address, length of service
- Phone and Internet connection records (times, durations, account identifiers)
- Financial and credit records
- Banking records

**What NSLs cannot directly compel** (requires a court order):
- Content of communications
- Full browsing history (currently — the FBI has lobbied to expand this)

**Gag orders**: Recipients are legally prohibited from disclosing they received an NSL, even to the target whose records were sought. This means a person cannot learn through normal means that the FBI has subpoenaed their records.

Source: [EFF NSL FAQ](https://www.eff.org/issues/national-security-letters/faq)

---

### B. FISA Orders (Traditional)

For U.S. persons, the FBI must obtain a FISA order from the Foreign Intelligence Surveillance Court (FISC) for:
- Interception of content in real time
- Physical search
- Installation of pen registers/trap-and-trace devices

FISA orders are granted ex parte (government only) and are classified. Approval rates historically exceed 99%.

---

### C. Tech Company Legal Process

The FBI can compel disclosure from tech companies through:
- **NSLs**: metadata, connection records, no judicial approval required
- **ECPA orders (18 U.S.C. 2703(d))**: transaction records, lower than probable cause standard
- **Search warrants**: content of communications, requires probable cause
- **FISA orders**: content for national security investigations, FISC approval

**Signal's position**: Signal can only disclose what it has. In response to grand jury subpoenas, Signal has provided: the date an account was created and the date of last connection to Signal's servers. Signal cannot provide message content, contact lists, or profile information because it does not retain this data. This is a meaningful protection — but metadata about *who uses Signal* and *when* is visible to carriers and can be compelled.

---

### D. Parallel Construction

A documented practice: law enforcement learns of a lead through NSA signals intelligence (which cannot be used as evidence), then "rebuilds" the case through conventional investigative methods to obscure the surveillance origins. Reuters reported this in 2013 via DEA's Special Operations Division; it has not been officially discontinued.

---

## V. Facial Recognition and Biometric Surveillance

### A. Clearview AI

- **September 2025**: ICE Homeland Security Investigations awarded Clearview AI a **$9.2 million** contract for biometric matching software
- Scope per contract: child sexual exploitation investigations and assaults on law enforcement — but the system can be queried against any face
- Clearview's database: scraped from the public internet, claimed to contain tens of billions of facial images
- ICE has held Clearview contracts since 2020; the 2021 enterprise license expanded to agency-wide access

**Oversight gap**: In February 2026, DHS removed from its website the Biden-era directive governing face recognition use. No replacement policy has been announced.

Sources: [Biometric Update](https://www.biometricupdate.com/202509/ice-awards-clearview-ai-9-2m-facial-recognition-contract), [FedScoop](https://fedscoop.com/dhs-cbp-contract-biometric-facial-recognition-ai/)

---

### B. License Plate Readers (ALPR)

- CBP operates a **nationwide** ALPR dragnet via contracts with Vigilant Solutions, Flock Safety, and data-sharing agreements
- Palantir ELITE and Gotham both ingest ALPR data as a component of address/location confidence scoring
- ALPR captures vehicle location, time-stamped, with no warrant requirement as vehicles are on public roads

Source: [State of Surveillance ALPR report](https://stateofsurveillance.org/articles/surveillance/border-patrol-alpr-nationwide-dragnet/)

---

### C. Cell-Site Simulators (Stingrays/IMSI Catchers)

Devices that impersonate cell towers, forcing nearby phones to connect and revealing their location and identity.

**Confirmed users**: FBI, DEA, NSA, Secret Service, ICE, U.S. Marshals, Army, Navy, Marine Corps, National Guard

**Deployment method**: Mounted in vehicles, aircraft (FBI/U.S. Marshals have used plane-mounted stingrays over cities), and fixed locations

**Confirmed oversight violations**: In 2023, it was revealed that ICE, DHS, and the Secret Service used cell-site simulators without following their own rules or obtaining warrants

**Detection tool**: EFF released Rayhunter (March 2025), open-source stingray detection software for Android

Source: [EFF Street Level Surveillance](https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers)

---

## VI. DOGE Data Consolidation: The Emerging Cross-Agency Database

This is the most significant structural change to the surveillance landscape since the post-9/11 NSA expansions. DOGE is building what amounts to a centralized government data warehouse that would enable cross-agency profiling at a scale previously impossible.

### Confirmed Actions (Primary Sources)

1. **SSA data transferred to unauthorized server**: A DOGE employee transmitted an encrypted file — believed to contain names and addresses of ~1,000 individuals drawn from SSA systems — to a DHS-linked server without agency knowledge or authorization. Confirmed via DOJ court filing. ([DOGE Congressional reporting](https://larson.house.gov/media-center/in-the-news/doge-shared-social-security-data-unauthorized-server-according-court))

2. **Live SSA database copied to cloud server**: DOGE employees transferred a live copy of the country's Social Security database to a cloud server without independent security controls. SSA cannot confirm what data was shared or whether it still exists on the third-party server. ([NPR](https://www.npr.org/2026/01/23/nx-s1-5684185/doge-data-social-security-privacy))

3. **IRS-DHS data sharing agreement**: The IRS and DHS signed an agreement for the IRS to share taxpayer information with DHS for immigration enforcement purposes. A federal court has **blocked most IRS data sharing** pending litigation. ([Nextgov/FCW](https://www.nextgov.com/digital-government/2026/03/irs-ceo-largely-dodges-questions-about-data-sharing-irs-ssa/411893/))

4. **Trump executive order authorizing data consolidation**: March 2025, EO "Stopping Waste, Fraud, and Abuse by Eliminating Information Silos" directed agencies to share data across the government. ([Brookings](https://www.brookings.edu/articles/privacy-under-siege-doges-one-big-beautiful-database/))

5. **Palantir's role confirmed**: Palantir is involved in building out the cross-agency master database at DHS — specifically connecting SSA data, IRS data, biometric data, and voting records. ([CNN Politics](https://www.cnn.com/2025/04/25/politics/doge-building-master-database-immigration))

6. **SAVE system overhaul**: DHS and DOGE overhauled the SAVE (Systematic Alien Verification for Entitlements) database into a centralized national citizenship tool linking to SSA records.

7. **At least 15 active federal lawsuits** challenging DOGE data access as of early 2026.

### What This Means If Completed

If the master database is fully built, a single query on an individual could surface: their tax returns, income, employment history, Social Security records, healthcare enrollment, immigration status, biometric identifiers, family connections, address history, and voter registration — all in one interface, operated by agents with minimal oversight.

---

## VII. Threat Matrix: What Can They Actually See?

| Data Type | Who Can Access | Method | Warrant Required? |
|-----------|---------------|--------|-------------------|
| Cell location (real-time, carrier) | FBI, DEA, all federal LE | NSL or ECPA order | No (NSL); Yes for content |
| Cell location (historical, broker) | ICE, CBP, FBI | Purchase from Venntel/broker | No — commercial purchase |
| Cell location (stingray, live) | FBI, DEA, ICE, NSA, military | Direct device operation | Contested; frequently bypassed |
| Internet metadata | NSA (bulk), FBI | Upstream collection, NSL | NSA: No; FBI: NSL no warrant |
| Email/message content | NSA (targets), FBI | PRISM, search warrant | NSA: FISA/702; FBI: warrant or FISA |
| Tax records | IRS (via Palantir LCA), DHS (contested) | Palantir LCA; DHS agreement | IRS internal access; DHS blocked by court |
| Social Security records | DHS/ICE (contested), DOGE | SSA-DHS agreement, DOGE transfer | Contested; court-blocked partially |
| Medical/Medicaid records | ICE via ELITE | HHS data feed to ELITE | No — administrative data sharing |
| Financial transactions | FBI via FinCEN, IRS/Palantir | FinCEN SAR data, Palantir LCA | FinCEN: no warrant; bank records: NSL |
| DMV / driver's license | ICE, CBP, Palantir | State DMV agreements | Administrative |
| Social media (public) | All agencies, Babel Street | Open-source monitoring | No warrant — public |
| Social media (private/subpoenaed) | NSA, FBI | PRISM, warrant | Warrant or FISA |
| Facial image matching | ICE, CBP | Clearview AI contract | No — no law requires warrant |
| ALPR / vehicle location | CBP, ICE, local LE | ALPR network, Vigilant | No warrant — public roads |
| Student/visa status | ICE | SEVIS database | Administrative |
| Crypto transactions | IRS/Palantir | LCA platform, blockchain analysis | Analysis of public blockchain; exchange records via warrant |

---

## VIII. Analytical Capabilities: What Palantir/NSA Can DO With That Data

### Identity Resolution
Linking disparate records to a single confirmed individual even when they use different names, addresses, or identifiers. Confirmed Palantir capability: can search by tattoo, physical description, partial address, vehicle, associate's name, or immigration number.

### Pattern of Life Analysis
Mapping where an individual is, has been, and is likely to go based on aggregated data over time. Used operationally by Gotham for military targeting; same capability applies domestically via ELITE and ICM.

### Social Graph Mapping
Identifying all known associates, family members, and contacts of a target. ICM explicitly stores "family relationships." NSA contact chaining extends this to all communications partners within multiple "hops."

### Predictive Targeting / Confidence Scoring
ELITE's address confidence scoring (e.g., 98.95/100) represents algorithmic prediction of where a target currently is. ImmigrationOS uses AI to prioritize targets for apprehension. The criteria and weighting are not public.

### Bulk Social Media Monitoring
Babel Street and ImmigrationOS both have confirmed capability for real-time social media monitoring with sentiment analysis across multiple platforms simultaneously. This is not targeted — it scans for patterns and flags individuals.

### Cross-Agency Record Linking
Foundry's core capability: connecting datasets that were never designed to interoperate. The IRS LCA connects tax records to FinCEN records to communications metadata. ELITE connects HHS Medicaid to USCIS to CLEAR. These links are the analytical product.

---

## IX. Confirmed Gaps and Open Questions

**What is confirmed**: Specific contracts, specific dollar values, specific named data sources feeding specific Palantir tools — sourced from FOIA disclosures, court filings, government contract databases (USASpending.gov), and investigative reporting by The Intercept, 404 Media, EFF, ACLU, and Amnesty International.

**What remains uncertain or unconfirmed**:
1. The full list of data sources feeding ImmigrationOS beyond those confirmed
2. The specific AI/ML models used for targeting scores and whether they have been independently audited
3. The extent to which DOGE's master database project succeeded before being challenged in court
4. Whether NSA's AI/ML tools are being applied to metadata for domestic predictive targeting (strongly suspected, not confirmed)
5. The specific role of Signal metadata (carrier-visible) in NSA/FBI analysis chains
6. Whether Palantir's Foundry has live feeds from carrier location data or only from data brokers

**The parallel construction gap**: The documented DEA/SOD practice of rebuilding cases to hide intelligence origins means that even when courts block certain surveillance, the information may already have been used to generate leads through other channels.

---

## X. Key Sources (All Primary or Near-Primary)

- [ACLU: All the Ways Palantir Is Assisting Trump's Removal Campaign](https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup)
- [The Intercept: Palantir Is Helping Trump's IRS Conduct "Massive-Scale" Data Mining (April 24, 2026)](https://theintercept.com/2026/04/24/palantir-irs-contract-data/)
- [404 Media: Here Is the User Guide for ELITE, the Tool Palantir Made for ICE](https://www.404media.co/here-is-the-user-guide-for-elite-the-tool-palantir-made-for-ice/)
- [404 Media: ELITE — The Palantir App ICE Uses to Find Neighborhoods to Raid](https://www.404media.co/elite-the-palantir-app-ice-uses-to-find-neighborhoods-to-raid/)
- [EFF: Report — ICE Using Palantir Tool That Feeds on Medicaid Data](https://www.eff.org/deeplinks/2026/01/report-ice-using-palantir-tool-feeds-medicaid-data)
- [Amnesty International: Palantir and Babel Street Pose Surveillance Threats to Pro-Palestine Protesters (August 2025)](https://www.amnesty.org/en/latest/news/2025/08/usa-global-tech-made-by-palantir-and-babel-street-pose-surveillance-threats-to-pro-palestine-student-protestors-migrants/)
- [American Immigration Council: ICE to Use ImmigrationOS](https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/)
- [NPR: Your data is everywhere. The government is buying it without a warrant (March 2026)](https://www.npr.org/2026/03/25/nx-s1-5752369/ice-surveillance-data-brokers-congress-anthropic)
- [CNN: DOGE is building a master database for immigration enforcement (April 2025)](https://www.cnn.com/2025/04/25/politics/doge-building-master-database-immigration)
- [NPR: How DOGE improperly accessed and shared Social Security data](https://www.npr.org/2026/01/23/nx-s1-5684185/doge-data-social-security-privacy)
- [USASpending.gov: Palantir contract with ICE](https://www.usaspending.gov/award/CONT_AWD_70CTD022FR0000170_7012_GS35F0086U_4730)
- [ICE FOIA contract document: Palantir HSCETC-15-C-00001](https://www.ice.gov/doclib/foia/contracts/palantirTechHSCETC15C00001.pdf)
- [EFF: Cell-Site Simulators / IMSI Catchers](https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers)
- [Vice: How an ICE Contractor Tracks Phones Around the World (Venntel)](https://www.vice.com/en/article/ice-dhs-fbi-location-data-venntel-apps/)
- [Biometric Update: ICE awards Clearview AI $9.2M contract](https://www.biometricupdate.com/202509/ice-awards-clearview-ai-9-2m-facial-recognition-contract)
- [Penn CERL: Section 702 reauthorization outlook](https://www.penncerl.org/the-rule-of-law-post/after-a-bruising-battle-fisa-section-702-lives-on-now-let-the-2026-section-702-reauthorization-debate-begin/)
- [Privacy International: All Roads Lead to Palantir (2020)](https://privacyinternational.org/sites/default/files/2020-11/All%20roads%20lead%20to%20Palantir%20with%20Palantir%20response%20v3.pdf)

---

*Next document to produce*: `defensive-opsec-guide.md` — layered countermeasures mapped against each threat vector identified here.
