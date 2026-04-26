---
title: "Palantir Threat Model: Technical Capabilities and OpSec Implications"
project: cybersecurity-hardening
created: 2026-04-26
status: complete
confidence: high — sourced from FOIA disclosures, government contract databases, investigative journalism (The Intercept, 404 Media, Vice), EFF, ACLU, Amnesty International, and Palantir's own technical documentation
related: threat-model.md
---

# Palantir Threat Model: Technical Capabilities and OpSec Implications

**Purpose**: This is a companion to the broader `threat-model.md`. Where that document maps the full surveillance infrastructure landscape, this document goes deep on Palantir specifically — its technical methodology, the mechanics of how it links identity across data sources, what it concretely knows about U.S. persons, and what that means for individual threat modeling.

**Lead finding**: Palantir is not a single database. It is a software platform that makes dozens of previously siloed databases queryable as a unified system. The practical threat is not that Palantir "has" your data — it is that Palantir enables a single analyst to *query across all of them simultaneously* and receive a single integrated profile. The data existed before Palantir. Palantir's contribution is removing friction from cross-database identity resolution at scale.

---

## I. Technical Architecture: How Palantir Works

### A. The Three Platforms

**Gotham** is the law enforcement and intelligence product. It is the primary tool used by the CIA, NSA, FBI, ICE, CBP, military, and dozens of local police departments. Gotham is designed for investigations: it ingests structured and unstructured data from multiple agencies and commercial sources, then provides an interface for analysts to identify individuals, map their relationships, trace their movements, and develop predictive profiles. The marketing tagline used internally has been "Your software is the weapons system."

**Foundry** is the enterprise data integration and pipeline platform. It ingests raw data from 200+ source connectors, transforms it through automated pipelines, and surfaces it as a unified queryable data environment. Foundry is the back-end infrastructure for the DOGE-era cross-agency master database project. At least four federal agencies now run Foundry, including DHS and HHS. The IRS also uses a Foundry-based system (LCA). The significance: once agencies run Foundry instances, those instances can be made interoperable, enabling cross-agency queries without full centralization. A WIRED investigation confirmed that the DOGE hackathon was plotting a "mega API" connecting agency Foundry instances, likely hosted on Foundry itself.

**AIP (Artificial Intelligence Platform)** is the 2023-era layer that integrates large language models and autonomous agents on top of Gotham and Foundry data. For government contexts, this means AI agents that can autonomously perform analysis tasks — not just passive querying, but active pattern detection, lead generation, and autonomous flagging of individuals without analyst initiation. The U.S. Army's $10 billion Enterprise Service Agreement (July 2025) explicitly incorporates AIP. AIP agents can, per Palantir's own documentation, take actions autonomously within defined parameters.

### B. The Ontology: How Palantir Thinks About Data

Palantir's core data model is an "ontology" — a semantic graph of real-world entities (Person, Vehicle, Address, Phone Number, Transaction, Event) connected by typed relationships (Person "owns" Vehicle, Person "resides at" Address, Person "contacted" Person). Every raw data source, regardless of format, is ingested and mapped to this ontology through pipeline transformations.

This architecture is what makes Palantir dangerous for identity resolution. When a new record arrives — a utility bill, an arrest report, a Medicaid enrollment — the system does not file it in isolation. It runs entity resolution to determine whether this record refers to an entity already in the ontology. If it does, the record is attached to that entity's profile. If not, a new entity is created. Over time, an individual's ontological object accumulates links to every database in which they appear.

A confirmed technical feature is **Foundry Entity Resolution** — Palantir's AI-powered record deduplication and linking product. Per Palantir's own marketing: "seamlessly links records with AI to establish a reliable, de-duplicated data foundation." Entity resolution is the automated process of determining that "John P. Smith, 123 Main St" in the tax database and "J. Smith, 124 Main St" in the DMV database refer to the same person.

The identifiers used for resolution, based on confirmed ingested data sources, include: SSN, name, date of birth, address (current and historical), phone number, email address, vehicle identification number, license plate, biometric identifiers, immigration number (Alien number), IP address, and associated persons. These overlap sufficiently that pseudonymous operation becomes very difficult once even two anchors are connected.

### C. The "Beyond Anonymisation" Admission

Palantir published a technical whitepaper titled "Beyond Anonymisation: A Comprehensive Approach to Handling Personal Data." The document explicitly acknowledges that "partial information from anonymised data, linked with insights from other data sources, can be used to reverse engineer aspects of the anonymisation process" — i.e., re-identification through data fusion is a known risk that Palantir's own engineers understand well. This is the same capability deployed against targets.

The implication: any single pseudonymous data point is only as private as the weakest cross-reference. A person using a burner phone is protected only until that phone appears in the same location as a known device, the same financial transaction as a real identity, or the same address as a known individual.

Sources: [Palantir Entity Resolution product page](https://www.palantir.com/foundry-entity-resolution/), [Palantir "Beyond Anonymisation" whitepaper](https://www.palantir.com/assets/xrfr7uokpv1b/5oWSVdic2rPQtBlKnqTw25/a87cbcc9439481cf21cdf693bcd4f575/Beyond_Anonymisation-_A_comprehensive_approach_to_handling_personal_data.pdf), [Palantir Ontology overview](https://www.palantir.com/platforms/ontology/)

---

## II. Confirmed Federal and State Contracts

### A. Federal Agency Contracts (Confirmed)

#### ICE — Multiple Active Platforms

**ELITE (Enhanced Leads Identification and Targeting for Enforcement)**
- Contract value: $29.9 million (September 2025, running into 2026+)
- Function: Displays deportation targets as pins on a map with per-person dossiers and address confidence scores
- Address confidence scoring: expressed 0-100, reflects recency and source quality of the most recent address signal. Example scores in leaked user guide: 98.95 and 77.25 out of 100
- Underlying algorithm pulls from: IRS records, SSA records, DMV records, Medicaid/HHS files, utility bills, license plate reader data, commercial data brokers
- Identifies "target-rich areas" — neighborhoods with high concentrations of people with "immigration nexus"
- Described internally by ICE agents as "kind of like Google Maps" for finding deportation targets
- Data sources confirmed by FOIA and EFF reporting: HHS/Medicaid records, USCIS databases, Thomson-Reuters CLEAR, DMV records

Sources: [404 Media — ELITE user guide](https://www.404media.co/here-is-the-user-guide-for-elite-the-tool-palantir-made-for-ice/), [404 Media — ELITE neighborhoods](https://www.404media.co/elite-the-palantir-app-ice-uses-to-find-neighborhoods-to-raid/), [EFF — Medicaid data in ELITE](https://www.eff.org/deeplinks/2026/01/report-ice-using-palantir-tool-feeds-medicaid-data)

**ICM (Investigative Case Management)** — in use since 2014, sole-source contract through April 2026
- Function: Full deportation case lifecycle management; case construction against individuals
- Data consolidated: schooling records, family relationships, employment history, biometric traits, criminal records, current and previous addresses, phone records, field-seized device data
- Database connections: FBI, DEA, ATF databases; SEVIS (student/visa tracking); multiple interconnected federal and commercial databases

Source: [ACLU full breakdown](https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup)

**ImmigrationOS** — $30 million contract, April 2025; prototype due September 2025; contract runs through 2027
- Three core functions: (1) AI-assisted target prioritization/apprehension, (2) self-deportation near real-time tracking, (3) deportation logistics optimization
- Data sources: Full ICM ecosystem plus explicitly "external" sources per contract language — non-DHS data confirmed
- OSINT/social media: ImmigrationOS incorporates OSINT capabilities including automated social media monitoring. Note: social media scanning primarily attributed to Babel Street (Babel X) in Amnesty International's report; the boundary between Palantir and Babel Street capabilities in combined deployments is not always clear from public sources
- Context: This system is reportedly the infrastructure behind "Catch and Revoke" — visa/residency revocations of individuals flagged for protest activity

Sources: [American Immigration Council](https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/), [Amnesty International August 2025](https://www.amnesty.org/en/latest/news/2025/08/usa-global-tech-made-by-palantir-and-babel-street-pose-surveillance-threats-to-pro-palestine-student-protestors-migrants/), [immpolicytracking.org](https://immpolicytracking.org/policies/reported-palantir-awarded-30-million-to-build-immigrationos-surveillance-platform-for-ice/)

#### CBP — Analytical Framework for Intelligence (AFI)

- Function: Real-time evaluation of non-immigrant visa holders at ports of entry
- Data confirmed: travel histories, previous immigration records, criminal checks, social media activities, emails, WhatsApp and Telegram chats, cellphone call logs, Instagram accounts
- Context: CBP's legal basis for accessing email/messaging content differs from domestic law enforcement. At the border, CBP operates under reduced Fourth Amendment constraints; device search authority does not require a warrant

Source: [Reddy Neumann Brown analysis](https://www.rnlawgroup.com/palantirs-role-in-immigration-vetting-how-uscis-cbp-ice-and-dos-use-data-analytics/), [Biometric Update](https://www.biometricupdate.com/202506/ice-advances-sole-source-deal-with-palantir-for-new-surveillance-backbone)

#### IRS — Lead and Case Analytics (LCA) Platform

- Total contract value: $130+ million since 2018
- Function: "Massive-scale data mining" for financial crimes investigation
- Data confirmed by contract documents: individual tax forms and returns; ACA enrollment data; bank statements and financial transactions; FinCEN records including Suspicious Activity Reports; cryptocurrency wallet data (Bitcoin, Ethereum, Litecoin, Ripple) from seized servers, dark web sources, and exchanges including Coinbase; communications metadata (calls, texts, emails events); IP address records
- Analytical capabilities: searches "connections from millions of records with thousands of links"; maps social networks among investigation targets; visualizes relationship chains
- Current concern: IRS Criminal Investigation division has reportedly shifted focus toward "left-leaning groups" under Trump administration direction. The LCA system provides the technical capacity for this at scale

Source: [The Intercept, April 24, 2026](https://theintercept.com/2026/04/24/palantir-irs-contract-data/)

#### CIA, NSA, FBI, DOD

- Palantir confirms the CIA was its first government customer; CIA use of Gotham predates all commercial contracts
- NSA and NSA-adjacent intelligence uses: confirmed, details classified
- FBI: uses Gotham for domestic investigations; scope of data access not fully confirmed through public sources
- Army: $10 billion Enterprise Service Agreement (July 2025, 10-year term), consolidating 75 prior contracts, incorporating AIP. This is the largest government contract in Palantir's history.

Sources: [The Hill](https://thehill.com/policy/technology/5667232-palantir-trump-administration-surveillance/), [State of Surveillance](https://stateofsurveillance.org/articles/surveillance/palantir-government-surveillance-ecosystem-billions/)

#### DOGE / Cross-Agency Master Database (In Progress as of April 2026)

- A March 2025 Executive Order directed federal agencies to end "information silos" and share datasets across agencies
- Palantir's role confirmed: building cross-agency connectivity at DHS, linking SSA data, IRS data, biometric data, and voting records
- Technical architecture: Foundry instances at multiple agencies made interoperable via API. Once Foundry instances are interoperable, "you don't necessarily have to centralize all that data — you're able to query a variety of data systems across government"
- DOGE-associated engineers were embedded at IRS to build a "mega API" unifying all IRS data, likely hosted on Foundry
- At least 15 active federal lawsuits challenging DOGE data access as of early 2026
- Federal court has partially blocked IRS-DHS data sharing pending litigation

Sources: [CNN Politics](https://www.cnn.com/2025/04/25/politics/doge-building-master-database-immigration), [Democracy Now](https://www.democracynow.org/2025/6/3/makena_kelly), [Federal data-sharing WBIW](https://www.wbiw.com/2025/06/02/federal-data-sharing-initiative-sparks-debate-over-privacy-oversight-as-palantir-takes-lead/)

### B. State and Local Law Enforcement

**Scale**: Palantir's local law enforcement presence is concentrated in major metropolitan areas and regional fusion centers rather than universally deployed in small departments. However, its footprint includes some of the largest police departments in the country.

**Documented deployments** (confirmed through investigative reporting and FOIA):

- **NYPD**: Customer since approximately 2012; paying approximately $3.5 million/year as of 2015. Data ingested: arrest records, license plate reads, parking tickets, incident reports, and other policing data. The NYPD's history includes warrantless surveillance of Muslim communities.
- **LAPD**: Deployed Gotham with integration of field interview cards (officers document suspected individuals' names, addresses, physical characteristics, gang affiliations); arrest records; 1 billion+ ALPR images from traffic lights and toll booths; telecom data; county health services records; California DMV records; California Law Enforcement Telecommunications System data. The system created documented feedback loops: each police stop increased a person's "point value," justifying increased surveillance, disproportionately affecting minority neighborhoods.
- **New Orleans NOPD**: Secret predictive policing contract 2012–2018, run through a charitable intermediary to avoid public oversight. Used for gang identification — NOPD used the software to aid in the arrest of 83 suspected gang members between 2012 and 2014. Program ended in 2018 after investigative journalism exposed it; city council had not known the arrangement existed.

**The feedback loop problem** (LAPD documented): Palantir's scoring systems incorporate police contact history. Each time an individual is stopped, they accumulate data points. Because policing is not uniformly distributed, individuals in over-policed areas accumulate more data points, which justifies more surveillance, which creates more stops. The system reinforces existing bias rather than correcting for it.

Sources: [Brennan Center — NYPD contract](https://www.brennancenter.org/our-work/analysis-opinion/palantir-contract-dispute-exposes-nypds-lack-transparency), [The Intercept — LAPD/Palantir](https://theintercept.com/2021/01/30/lapd-palantir-data-driven-policing/), [BuzzFeed News — LAPD training documents](https://www.buzzfeednews.com/article/carolinehaskins1/training-documents-palantir-lapd), [Type Investigations — New Orleans](https://www.typeinvestigations.org/investigation/2018/02/27/palantir-secretly-use-new-orleans-test-predictive-policing/), [ACLU — New Orleans](https://www.aclu.org/news/privacy-technology/new-orleans-program-offers-lessons-pitfalls-predictive-policing)

---

## III. Realistic Citizen Threat Model: What Palantir Likely Knows

This section distinguishes between what Palantir *likely* has on any U.S. person (high confidence, confirmed through contracts and data source analysis) versus what is uncertain.

### A. What Palantir Almost Certainly Has (High Confidence)

The following data categories are confirmed as feeding Palantir's government systems. If you are a U.S. adult, assume this baseline is available to a Palantir analyst with appropriate agency access:

**Financial profile**:
- Federal tax returns (IRS LCA contract)
- Bank transaction records (IRS LCA — FinCEN data)
- Cryptocurrency transaction history associated with your real identity (IRS LCA — exchanges including Coinbase have complied with court orders; blockchain analysis of Bitcoin, Ethereum, Litecoin, Ripple confirmed)
- Suspicious Activity Reports filed by your bank (IRS LCA — FinCEN feed)
- ACA/healthcare enrollment financial data (IRS LCA)

**Location and movement**:
- DMV records: vehicle registration, address history, physical description (confirmed in LAPD/ELITE)
- License plate reader records: ALPR data from traffic lights, toll booths, and CBP infrastructure. ELITE and Gotham both explicitly ingest ALPR data. CBP's network covers major roads in border regions; urban ALPR coverage is extensive
- Address confidence scoring pulls from utility bill data, credit check records, and recent administrative interactions — meaning recent applications, enrollments, or utility service changes update your known address in near real-time
- Cell location data available via commercial broker purchase (no Palantir-specific confirmation, but confirmed as ICE practice via Venntel/Gravy Analytics contracts)

**Identity and associations**:
- Full name, date of birth, SSN linkage (present in tax, SSA, and immigration records)
- Current and historical addresses (aggregated from DMV, utility, tax, credit, and court records)
- Family relationships (explicitly stored in ICM)
- Employment history (tax records, ACA enrollment)
- Criminal history, arrest records, field contact cards (Gotham police deployments)
- Immigration status and history (USCIS, ICM)
- Biometric identifiers where available: fingerprints (immigration touchpoints), face (Clearview AI separate system with confirmed ICE contract)
- Student and exchange visitor status (SEVIS, fed through ICM)

**Social and digital**:
- Public social media content: aggregated, though primarily through Babel Street rather than Palantir directly. Social media OSINT confirmed in ImmigrationOS and CBP AFI
- Email, WhatsApp, Telegram, Instagram: CBP AFI confirmed access at ports of entry; this is device-search data extracted at the border, not bulk collection
- Phone call metadata: confirmed in IRS LCA as "calls, texts, emails events" linked to investigation targets

### B. What Palantir Does NOT Reliably Have on Random U.S. Persons (Lower Confidence)

The following categories are either technically inaccessible, require elevated access (specific investigation), or are not confirmed in public contracts:

- **Encrypted message content** (Signal, properly used): Signal stores nothing. Even under legal process, Signal can only confirm account creation date and last connection date. This is the most robust confirmed gap.
- **Live location without a legal order**: Real-time tracking requires either carrier cooperation (requires legal process), a cell-site simulator (requires deployment), or commercial broker purchase (confirmed ICE practice via expired Venntel contract; FTC has now restricted future sales).
- **Financial records outside U.S. jurisdiction**: Foreign bank accounts not subject to FinCEN SAR reporting are harder to access; still potentially reachable through SWIFT data and DOJ processes, but not via Palantir's confirmed domestic data feeds.
- **Purely cash transactions**: Cash leaves no digital trail. This is a real gap, though it is being narrowed by the decline of cash usage and by FinCEN requirements for cash transactions above $10,000.
- **Data from services with strong legal resistance**: Warrant canaries and strong encryption are meaningful when a provider commits to contesting legal process. Most providers do not.

### C. The Identity Linking Problem: Why Metadata-Only Privacy Fails

The most important thing to understand about Palantir's threat model is not any single data source — it is the linking methodology.

Palantir's entity resolution system can connect records through what security researchers call the "identity graph": a web of relationships between identifying attributes that collectively narrow to a single individual even when no single attribute is used consistently.

**Concrete example of how pseudonymous data fails**:

A person uses a prepaid phone, pays for it with cash, and only uses it with public WiFi. This seems resistant. But:
1. The phone's IMEI is logged when it connects to a cell tower near their home (carrier metadata)
2. The WiFi access point's IP is associated with a physical location in ALPR records
3. The phone appears at the same coffee shop WiFi as their primary phone on multiple occasions
4. The phone's first call is to a family member in ICM
5. ICM already has the family member's record, which lists this person as a family relationship

Entity resolution connects these dots. The pseudonymous phone becomes associated with the real identity not through any single link but through probabilistic convergence of co-located signals.

This is not speculative. Palantir's LAPD training documents demonstrate exactly this pattern: "search 140 million records for a hypothetical man of average build driving a black four-door sedan, narrowing results to 2 million, then 160,000, and finally 13 people." Identity narrowing through attribute convergence is the core capability.

**Cryptocurrency-specific note**: IRS LCA has confirmed access to cryptocurrency wallet data from exchanges (Coinbase specifically named), seized servers, and dark web sources. Blockchain transactions are public by design; the question is whether a wallet address can be linked to a real identity. If you've ever transacted through a U.S.-regulated exchange (Coinbase, Kraken, etc.), that exchange has KYC (Know Your Customer) data linking your wallet address to your SSN. The IRS LCA platform then connects that wallet to your tax profile and your other financial associations.

---

## IV. Documented Failures, Controversies, and Accuracy Problems

### Confirmed False Positive and Accuracy Issues

**LAPD feedback loops and false positive admission**: In a documented Palantir demonstration, an engineer narrowed 140 million records to 13 suspects through attribute filtering, then admitted — when asked about false positives — "I don't know." There is no confirmed independent accuracy audit of Palantir's predictive policing systems.

**Predictive policing racial bias (LAPD, documented)**: The system disproportionately targeted minority neighborhoods because field interview cards, the primary data input, were disproportionately collected there. The result was a feedback loop: over-policed communities generated more data points, which justified more policing, which generated more data. A sergeant privately described the system as "bitching, but it's worthless."

**Visa revocations 2025**: At least 1,800–4,000 students had visas revoked under the "Catch and Revoke" program, with multiple reported cases of students targeted who had no protest involvement. Students from African, Arab, Asian, Middle Eastern, and Muslim backgrounds were disproportionately affected, with some targeted based only on minor law enforcement contacts such as traffic tickets. These incidents demonstrate the real-world consequence of false positives in algorithmic targeting: the burden of proving innocence falls on the flagged person, not the system.

**New Orleans predictive policing (2012–2018)**: The program ran for six years before the city council knew it existed. When it ended, the city had no mechanism to audit the accuracy of the gang membership predictions or delete incorrect records. Records generated through predictive policing may persist in federal databases indefinitely.

**Algorithm opacity**: Palantir's systems are proprietary. The public, elected officials, and defendants cannot inspect how targeting weights are assigned, what error rates are, or how to challenge incorrect predictions. There are no confirmed independent audits of Palantir's government-facing algorithms.

Sources: [The Intercept — LAPD](https://theintercept.com/2021/01/30/lapd-palantir-data-driven-policing/), [BuzzFeed News — LAPD training docs](https://www.buzzfeednews.com/article/carolinehaskins1/training-documents-palantir-lapd), [Biometric Update — lawmakers press DHS](https://www.biometricupdate.com/202604/lawmakers-press-dhs-ice-over-palantir-surveillance-tools), [PMC — predictive policing academic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10846878/)

### Congressional and Legal Challenges

In June 2025, Senators Wyden and Velázquez sent a letter to Palantir CEO Alex Karp demanding answers on ICE's use of Palantir-developed technologies for mass surveillance. [Source: Senate Finance Committee letter](https://www.finance.senate.gov/imo/media/doc/wyden_aoc_palantir_letter_061725.pdf)

As of April 2026, at least 15 active federal lawsuits challenge various aspects of DOGE and agency data sharing. A federal court has blocked most IRS-DHS data sharing pending litigation. [Source: [Nextgov/FCW](https://www.nextgov.com/digital-government/2026/03/irs-ceo-largely-dodges-questions-about-data-sharing-irs-ssa/411893/)]

---

## V. Implications for OpSec Decision-Making

### The Correct Mental Model

Do not think of Palantir as having "a file on you." Think of it as providing a capability to rapidly build a file on you from data that already exists in government systems, commercial brokers, and public records — the moment a query is run.

The practical security implication: your threat is not primarily about preventing data collection (much of it is already done and cannot be undone). Your threat is about minimizing the number of fresh data points that can update or confirm your location, associations, and activities in near real-time.

### Specific OpSec Considerations

**Financial behavior**:
- Assume your tax records, bank transactions, and any transactions with U.S.-regulated cryptocurrency exchanges are in or accessible to the IRS LCA system
- FinCEN Suspicious Activity Reports can be generated by banks without your knowledge or consent, and they feed into the LCA platform
- Cash transactions below $10,000 leave minimal digital trails; above $10,000 trigger mandatory FinCEN reports
- Cryptocurrency mixers and privacy coins reduce blockchain traceability but do not help if the entry or exit point involved a regulated exchange with KYC data

**Location and movement**:
- ALPR coverage in urban areas is extensive; assume your vehicle's movements are logged at significant chokepoints
- Cell phone location (carrier metadata) is accessible via NSL without a warrant for historical records
- Address confidence scoring updates near real-time from utility connections, credit applications, and similar administrative interactions — moving does not help if you generate administrative records at the new address
- Mobile advertising identifiers (MAIDs) from standard smartphones feed location data to brokers that ICE has contracted to purchase; this is device-level, not carrier-level, and requires app-level permissions to generate

**Identity and associations**:
- Family relationships stored in ICM mean that ICE already knows your family members if any of them have had any interaction with immigration systems
- Associates who have police contact records in Gotham-connected jurisdictions may be linked to you through co-location, shared addresses, or phone contact
- The "secondary surveillance network" documented in LAPD Gotham deployment: people who associate with or live near primary targets accumulate records even without direct police contact

**Digital behavior**:
- Public social media content is aggregated via Babel Street and ImmigrationOS. Assume anything posted publicly is indexed
- Encrypted messaging (Signal) represents a genuine capability gap — the content is inaccessible if properly implemented. Metadata (who communicates with whom, when) is still visible to carriers
- At U.S. border crossings, CBP has documented access to email, WhatsApp, Telegram, and Instagram content from searched devices. This is not a warrant requirement. Device search at the border is legally distinct from domestic surveillance

**What actually works**:
The threat model suggests that reducing exposure requires primarily: (1) eliminating advertising identifiers from your device (GrapheneOS or iOS hardened settings), (2) using Signal for sensitive communications, (3) being aware that cash financial activity and in-person activity are harder to aggregate than digital activity, and (4) maintaining awareness of what administrative records (utility, credit, medical) refresh your location data in Palantir-accessible systems.

See `implementation-guide.md` and `opsec-playbook.md` for operational countermeasures.

---

## VI. Key Unknowns: What Is Not Confirmed

Be explicit about what is speculation versus confirmed fact:

1. **Full scope of ImmigrationOS data sources**: The contract confirms "external" non-DHS sources; which specific commercial brokers or databases are included is not public.
2. **Algorithm weights and error rates**: No confirmed independent audit of ELITE's confidence scoring, ICM's targeting prioritization, or ImmigrationOS's AI targeting criteria. Error rates are unknown.
3. **Whether Palantir Foundry has live carrier location feeds**: Confirmed that ICE has purchased carrier location data through commercial brokers; not confirmed whether this data feeds directly into Palantir systems in real-time versus being available as a separate query.
4. **NSA-Palantir integration depth**: NSA uses Palantir Gotham; the extent to which NSA's bulk-collected intelligence flows into the same Gotham instances used by domestic law enforcement is not confirmed from public sources.
5. **Extent of DOGE master database completion**: Cross-agency Foundry interoperability is partially operational; full scope of what was connected before court challenges is not publicly confirmed.
6. **AI/ML targeting for domestic political surveillance**: AIP's agentic capabilities are confirmed; whether they are currently deployed for autonomous flagging of domestic political activity (rather than immigration violations) is not confirmed, though the infrastructure would support it.
7. **Social media monitoring specifics**: The boundary between Babel Street OSINT capabilities and Palantir ImmigrationOS OSINT capabilities in combined deployments is not clearly distinguishable from public sources. Assume both systems can see public social media content.
8. **Protest surveillance direct linkage**: It is documented that tools built for immigration enforcement could be extended to other administration targets; direct documented cases of Palantir being used to surveil immigration protesters or civil rights activists specifically are not yet confirmed from primary sources (as distinct from Babel Street use for protest monitoring, which is documented).

---

## VII. Primary Sources

- [ACLU: All the Ways Palantir Is Assisting Trump's Removal Campaign](https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup)
- [The Intercept: Palantir Is Helping Trump's IRS Conduct "Massive-Scale" Data Mining (April 24, 2026)](https://theintercept.com/2026/04/24/palantir-irs-contract-data/)
- [The Intercept: How the LAPD and Palantir Use Data to Justify Racist Policing](https://theintercept.com/2021/01/30/lapd-palantir-data-driven-policing/)
- [404 Media: Here Is the User Guide for ELITE, the Tool Palantir Made for ICE](https://www.404media.co/here-is-the-user-guide-for-elite-the-tool-palantir-made-for-ice/)
- [404 Media: ELITE — The Palantir App ICE Uses to Find Neighborhoods to Raid](https://www.404media.co/elite-the-palantir-app-ice-uses-to-find-neighborhoods-to-raid/)
- [EFF: Report — ICE Using Palantir Tool That Feeds on Medicaid Data](https://www.eff.org/deeplinks/2026/01/report-ice-using-palantir-tool-feeds-medicaid-data)
- [Amnesty International: Palantir and Babel Street Pose Surveillance Threats to Pro-Palestine Protesters (August 2025)](https://www.amnesty.org/en/latest/news/2025/08/usa-global-tech-made-by-palantir-and-babel-street-pose-surveillance-threats-to-pro-palestine-student-protestors-migrants/)
- [American Immigration Council: ICE to Use ImmigrationOS](https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/)
- [State of Surveillance: Palantir Government Surveillance Ecosystem $10B+](https://stateofsurveillance.org/articles/surveillance/palantir-government-surveillance-ecosystem-billions/)
- [BuzzFeed News: Leaked LAPD Palantir Training Documents](https://www.buzzfeednews.com/article/carolinehaskins1/training-documents-palantir-lapd)
- [Vice: Palantir's Top-Secret User Manual for Cops](https://www.vice.com/en/article/revealed-this-is-palantirs-top-secret-user-manual-for-cops/)
- [Type Investigations: Palantir Secretly Used New Orleans for Predictive Policing](https://www.typeinvestigations.org/investigation/2018/02/27/palantir-secretly-use-new-orleans-test-predictive-policing/)
- [ACLU: New Orleans Program Offers Lessons in Pitfalls of Predictive Policing](https://www.aclu.org/news/privacy-technology/new-orleans-program-offers-lessons-pitfalls-predictive-policing)
- [CNN Politics: DOGE Is Building a Master Database for Immigration Enforcement](https://www.cnn.com/2025/04/25/politics/doge-building-master-database-immigration)
- [The Conversation: When the Government Can See Everything](https://theconversation.com/when-the-government-can-see-everything-how-one-company-palantir-is-mapping-the-nations-data-263178)
- [USASpending.gov: Palantir ICE contract](https://www.usaspending.gov/award/CONT_AWD_70CTD022FR0000170_7012_GS35F0086U_4730)
- [ICE FOIA: Palantir contract HSCETC-15-C-00001](https://www.ice.gov/doclib/foia/contracts/palantirTechHSCETC15C00001.pdf)
- [Biometric Update: ICE advances sole-source deal with Palantir](https://www.biometricupdate.com/202506/ice-advances-sole-source-deal-with-palantir-for-new-surveillance-backbone)
- [immpolicytracking.org: ImmigrationOS $30M contract](https://immpolicytracking.org/policies/reported-palantir-awarded-30-million-to-build-immigrationos-surveillance-platform-for-ice/)
- [Senate Finance Committee: Wyden/AOC letter to Palantir CEO, June 2025](https://www.finance.senate.gov/imo/media/doc/wyden_aoc_palantir_letter_061725.pdf)
- [Palantir Entity Resolution product page](https://www.palantir.com/foundry-entity-resolution/)
- [Palantir Ontology overview](https://www.palantir.com/platforms/ontology/)
- [Palantir "Beyond Anonymisation" whitepaper](https://www.palantir.com/assets/xrfr7uokpv1b/5oWSVdic2rPQtBlKnqTw25/a87cbcc9439481cf21cdf693bcd4f575/Beyond_Anonymisation-_A_comprehensive_approach_to_handling_personal_data.pdf)
- [Reddy Neumann Brown: Palantir's Role at USCIS, CBP, ICE, DOS](https://www.rnlawgroup.com/palantirs-role-in-immigration-vetting-how-uscis-cbp-ice-and-dos-use-data-analytics/)
- [PMC: Big Data Surveillance — The Case of Policing](https://pmc.ncbi.nlm.nih.gov/articles/PMC10846878/)
- [Privacy International: All Roads Lead to Palantir](https://privacyinternational.org/sites/default/files/2021-11/All%20roads%20lead%20to%20Palantir%20with%20Palantir%20response%20v3.pdf)
