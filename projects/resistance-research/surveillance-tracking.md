---
title: "Surveillance Tracking — ICE/DHS Technology, Data Brokers, and Legal Status"
date: 2026-04-26
project: resistance-research
type: surveillance-tracker
last_updated: 2026-04-26
---

# Surveillance Tracking

*First created: April 26, 2026. This document tracks ICE and DHS surveillance infrastructure — contracts, legal challenges, data broker relationships, and deployment patterns. Update as new information is confirmed.*

---

## CRITICAL: Section 702 Expiration — April 30, 2026

**This is the most time-sensitive surveillance development in the queue.**

Section 702 of the Foreign Intelligence Surveillance Act — the NSA's primary legal authority to conduct warrantless surveillance of foreign targets while collecting communications of U.S. persons — is set to expire April 30, 2026.

**What happened**: The 5-year reauthorization that House Speaker Johnson sought failed April 17 when 20 dissenting Republicans joined most Democrats to block the bill. An 18-month extension Trump demanded was also rejected. Congress passed a 10-day stop-gap to April 30, which is now the hard deadline.

**Current congressional posture (as of April 25-26)**:
- The House Rules Committee approved a closed rule on a new bill — the Foreign Intelligence Accountability Act — blocking a floor amendment to add a warrant requirement
- The proposal offers a 3-year reauthorization with reforms including monthly Civil Liberties Protection Officer reviews and attorney-level approvals for U.S. person queries — but no warrant requirement
- Freedom Caucus members and civil libertarians from both parties are pushing for a warrant requirement as the price of reauthorization
- Trump has additionally complicated passage by conditioning his signature on attaching the SAVE Act (voter ID legislation) to the FISA bill

**If Section 702 lapses**:
- NSA loses real-time authority to collect foreign-targeted communications that transit U.S. systems
- FBI loses authority to query the 702 database for U.S. persons without a warrant
- Existing collected data does not disappear — analysis of previously collected data continues; only new collection authority lapses
- Historical pattern: Congress has always reauthorized surveillance authorities; a lapse of more than a few days would be unprecedented

**Civil liberties implications of the reform debate**:
The 50-member House Democrat letter (April 14) identified the critical loophole: intelligence agencies are currently permitted to purchase location data from commercial data brokers without a warrant, even when a warrant would be required to compel the same data directly. Closing this loophole would directly affect ICE and DHS operations since both agencies route location surveillance through commercial data broker relationships (Venntel/Babel Street, Accurint) specifically to avoid the warrant requirement.

**What to watch April 26-30**: Congressional floor vote timing; whether the SAVE Act attachment demand is dropped; whether a warrant-lite compromise (requiring attorney approval but not a judicial warrant for U.S. person queries) can hold together a majority.

Sources:
- [EFF — Keep Pushing: We Get 10 More Days to Reform Section 702](https://www.eff.org/deeplinks/2026/04/keep-pushing-we-get-10-more-days-reform-section-702)
- [NPR — Congress extends controversial surveillance powers for 10 days](https://www.npr.org/2026/04/17/nx-s1-5788573/house-extends-surveillance-powers-for-10-days)
- [Nextgov/FCW — House readies vote to renew FISA 702 without a warrant amendment](https://www.nextgov.com/policy/2026/04/house-readies-vote-renew-fisa-702-without-warrant-amendment/412856/)
- [Reason — Congress still has a chance to curb Section 702 surveillance abuses](https://reason.com/2026/04/24/congress-still-has-a-chance-to-curb-section-702-surveillance-abuses/)
- [GovPing — FISA 702 Reauthorization Stalls in Congress](https://changeflow.com/govping/data-privacy-cybersecurity/fisa-702-reauthorization-stalls-in-congress-2026-04-25)
- [Brookings — A key intelligence law expires in April](https://www.brookings.edu/articles/a-key-intelligence-law-expires-in-april-and-the-path-for-reauthorization-is-unclear/)
- [Penn CERL — FISA Section 702 lives on, now let the 2026 debate begin](https://www.penncerl.org/the-rule-of-law-post/after-a-bruising-battle-fisa-section-702-lives-on-now-let-the-2026-section-702-reauthorization-debate-begin/)

---

## Part 1: Palantir Contract Landscape (Updated April 2026)

### ImmigrationOS — $30 Million ICE Contract

**Contract awarded**: April 17, 2025. Prototype delivery deadline: September 25, 2025. Contract runs through September 2027.

**What it is**: "Immigration Lifecycle Operating System" — a unified AI-driven enforcement and surveillance platform integrating data from multiple federal databases into a single deportation workflow engine.

**Three core functions**:
1. Streamline identification and apprehension of prioritized targets (visa overstays, criminal records, gang designations)
2. Track self-deportations with "near real-time visibility" — ICE monitoring people leaving the country without enforcement action
3. Optimize deportation logistics — identifying individuals and routing removal operations

**Data sources ImmigrationOS pulls from**: IRS records, Social Security databases, passport databases, license plate readers, and existing Palantir Integrated Case Management (ICM) system data. The IRS data access is directly connected to the IRS-ICE data sharing MOU being litigated before Judges Talwani and Kollar-Kotelly (see litigation tracker).

**Contract justification**: Awarded as a sole-source contract based on Palantir being the only vendor capable of providing "specialized investigative case management software."

**Current protests**: The New Jersey State Investment Council was urged in a February 17, 2026 letter from Rep. Menendez to review its Palantir holdings given the contract. NYC Comptroller Mark Levine requested a third-party human rights risk assessment from Palantir. The ACLU published a comprehensive breakdown of all Palantir-ICE integration points in April 2026.

Sources:
- [Immigration Policy Tracking Project — ImmigrationOS](https://immpolicytracking.org/policies/reported-palantir-awarded-30-million-to-build-immigrationos-surveillance-platform-for-ice/)
- [American Immigration Council — ICE to Use ImmigrationOS](https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/)
- [State of Surveillance — ICE Paid Palantir $30 Million](https://stateofsurveillance.org/articles/government/palantir-immigrationos-ice-contract-2025/)
- [ACLU — All the Ways Palantir is Assisting Trump's Abusive Removal Campaign](https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup)
- [USASpending — Palantir Technologies ICE contract](https://www.usaspending.gov/award/CONT_AWD_70CTD022FR0000170_7012_GS35F0086U_4730)

---

### Palantir USDA Contract — Federal Worker Surveillance ("Bossware"), March 2026

**New development, March 2026**: Palantir received a no-bid contract worth up to $75 million from the USDA to track federal employees' return-to-office compliance. Sole-source award signed by USDA Chief Data and AI Officer Christopher Alvares.

**Stated purpose**: "Real-time analytics to optimize space utilization and employee seat assignments" and "continuous compliance monitoring" for the White House return-to-office directive.

**What this actually is**: Employee surveillance at scale — monitoring which federal workers appear at assigned offices, tracking compliance with RTO mandates, and generating compliance data that can be used in employment actions.

**Why it matters for the broader surveillance picture**: This is Palantir expanding its federal footprint from immigration and intelligence into workforce management. The GSA's governmentwide contract vehicles allow other agencies to use the same tool — if USDA's deployment succeeds, Interior, Commerce, and Transportation are logical next targets. It builds a unified data layer across the federal government with Palantir at the integration center.

**Separate $300 million USDA contract (April 22, 2026)**: Palantir also signed a $300 million software deal with USDA for food security and IT modernization ("One Farmer, One File" farm data system), announced April 22, 2026. This is distinct from the bossware contract and covers agricultural data infrastructure.

Sources:
- [State of Surveillance — Palantir's New Target: Federal Workers](https://stateofsurveillance.org/news/palantir-usda-bossware-federal-workforce-surveillance-2026/)
- [Jacobin — Is Palantir Under Contract to Surveil the Federal Workforce?](https://jacobin.com/2026/03/palantir-bossware-workforce-surveillance-tech)
- [The Register — USDA needs Palantir to tell workers where to sit](https://www.theregister.com/2026/03/10/palantir_usda_seating_software/)
- [CNBC — Palantir inks $300 million deal with USDA](https://www.cnbc.com/2026/04/22/palantir-inks-300-million-deal-with-usda-to-safeguard-food-supply.html)
- [The Hill — Palantir courts major federal contracts in Trump era](https://thehill.com/policy/technology/5667232-palantir-trump-administration-surveillance/)

---

### Palantir Government Contract Scale (Current)

- **Total federal contracts (2025)**: $970.5 million — up from $541.2 million in 2024 (a 79% annual increase)
- **Total estimated federal lifetime awards**: $13.7 billion across all agencies
- **ICE contracts (cumulative)**: At least $248.3 million documented (USASpending)
- **Agencies with active Palantir contracts**: CIA, Pentagon, ICE, IRS, CDC, Army, USDA, and dozens of others
- **Senate concern**: The scale of Palantir's government expansion has drawn attention in the Senate; former Sen. Menendez (NJ) called for investment review

Sources:
- [Fed-Spend — Palantir Government Contracts: $13.7 Billion in Awards](https://fed-spend.com/blog/palantir-government-contracts-deep-dive)
- [Statista — The U.S. Government Is a Palantir Regular](https://www.statista.com/chart/34847/financial-obligations-from-the-us-government-to-palantir/)

---

## Part 2: Data Broker Activity

### Venntel / Gravy Analytics — FTC Ban (January 2025)

**What happened**: The FTC finalized an order in January 2025 prohibiting Gravy Analytics and its subsidiary Venntel from selling sensitive location data.

**The order requires**:
- Cessation of all sales, disclosure, or use of sensitive location data (exceptions for national security and law enforcement under specific conditions)
- Deletion of all historic location data
- Notification to all customers who received location data in the last 3 years that they must delete, de-identify, or render non-sensitive the data they received

**What ICE had been doing with Venntel data**: CBP and ICE contracted through Babel Street to purchase Venntel location data. The data enabled tracking of individuals at churches, medical appointments, schools, protests, and homes. This was used as a warrant-end-run — purchasing commercial location data rather than obtaining a judicial warrant.

**Current enforcement gap**: The FTC order constrains Venntel's future commercial data sales, but law enforcement exceptions in the order preserve some government access pathways. Senator Wyden sent a letter to the DHS Inspector General on March 3, 2026, demanding investigation into whether ICE continues purchasing location data in violation of the FTC order.

**Alternative vendor pathway**: With Venntel constrained, ICE's location surveillance is being routed through Babel Street's other data products and through the Accurint (LexisNexis) platform, which was not subject to the FTC action.

Sources:
- [FTC — Final Order Prohibiting Gravy Analytics, Venntel](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-prohibiting-gravy-analytics-venntel-selling-sensitive-location-data)
- [Wyden letter to DHS OIG (March 3, 2026)](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_dhs_oig_on_ice_purchasing_location_datapdf.pdf)
- [EPIC — FTC Takes Action Against Data Brokers](https://epic.org/ftc-takes-action-against-data-brokers-for-selling-sensitive-location-data/)

---

### Accurint (LexisNexis) — Active ICE Platform

**Contract**: ICE pays approximately $4.7 million for Accurint subscription; over 11,000 ICE agents have access.

**What it does**: Automates decisions about vetting, screening, and targeting people for deportation. Agents performed over 1.2 million searches using the LexisNexis Accurint Virtual Crime Center tool in a single seven-month period (2022 documented data; access has expanded significantly since 2025).

**Current status**: No legal challenge to the Accurint contract has reached injunction stage as of April 26, 2026. The IRS-ICE data sharing injunctions (Talwani, D.Mass.; Kollar-Kotelly, D.D.C.) affect IRS-sourced data but do not directly reach third-party aggregation through LexisNexis.

---

### Clearview AI — Facial Recognition at Scale

**ICE contract (HSI)**: $9.2 million contract finalized September 2025. Provides Clearview's biometric matching software for two stated investigative uses: child sexual exploitation investigations and investigations into assaults on law enforcement officers.

**Database size**: 50+ billion facial images — the largest proprietary facial recognition database commercially available.

**CBP contract (February 2026)**: Separate 1-year, $225,000 contract signed with CBP.

**Mobile Fortify**: ICE's field facial recognition app (distinct from Clearview, but complementary). Deployed at field interactions. As of March 2026, documented use in stops and identity checks on individuals who had not committed any crime.

**Wrongful arrests in 2026**: At least 8 documented wrongful arrests in 2026 attributable to false positive matches from facial recognition tools (as of mid-April 2026).

**Legislative response**: In February 2026, Congress introduced the ICE Out of Our Faces Act, which would ban ICE and CBP from using facial recognition. No floor vote scheduled.

**May Day relevance**: DHS has characterized filming of ICE agents as potential "obstruction." The combination of facial recognition tools + the DHS posture on documentation creates risk at protest environments. Any facial scan at a protest environment could be matched against Clearview's database without any prior individualized suspicion.

**Army expansion**: The U.S. Army Special Forces signed a 4-year Clearview AI contract in 2026, extending the company's footprint beyond immigration enforcement.

Sources:
- [ID Tech Wire — ICE Awards $9.2 Million Clearview AI Contract](https://idtechwire.com/ice-awards-9-2-million-clearview-ai-contract-for-facial-recognition-investigations/)
- [404 Media — ICE Spends Millions on Clearview AI Facial Recognition to Find People Assaulting Officers](https://www.404media.co/ice-spends-millions-on-clearview-ai-face-recognition-to-find-people-assaulting-officers/)
- [Biometric Update — ICE awards Clearview AI $9.2M facial recognition contract](https://www.biometricupdate.com/202509/ice-awards-clearview-ai-9-2m-facial-recognition-contract)
- [NPR — ICE has spun a massive surveillance web](https://www.npr.org/2026/03/04/nx-s1-5717031/ice-dhs-immigrants-surveillance-confrontation-deportation-mobile-fortify)
- [State of Surveillance — Green Berets Are Using Clearview AI](https://stateofsurveillance.org/news/us-army-special-forces-clearview-ai-contract-2026/)

---

### ICE "Ad Tech and Big Data" Investigation (January 2026)

In January 2026, ICE published a Request for Information (RFI) seeking vendor input on "Ad Tech and Big Data Tools for Enhanced Investigative Capabilities." This signals ICE is actively building out its next generation of commercial data purchase relationships beyond the Venntel/Babel Street model the FTC constrained.

What the RFI sought input on: targeting of individuals for enforcement using behavioral data derived from commercial advertising technology pipelines — the same data infrastructure that allows advertisers to target individuals based on movement patterns, app usage, and online behavior.

The legal status of this approach is untested. The FTC's Venntel action explicitly covered "sensitive location data." Ad tech data may be characterized as "non-sensitive behavioral data" in a way that sidesteps the Venntel precedent. This is the surveillance frontier to watch in mid-2026.

Source: [IT Magazine — ICE Investigates: Seeking Input on 'Ad Tech and Big Data' Tools](https://itmagazine.com/2026/01/25/ice-investigates-seeking-input-on-ad-tech-and-big-data-tools-for-enhanced-investigative-capabilities/)

---

## Part 3: Regional ICE Deployment Shifts

### Post-Minneapolis Tactical Shift (April 2026)

**The headline number**: ICE arrests fell from ~8,347/week to ~7,369/week — a 12% national decline in the five weeks following Tom Homan's February 4 drawdown announcement after the Minneapolis (Operation Metro Surge) killings. (Source: Deportation Data Project, April 25 analysis)

**What the decline is not**: A strategic withdrawal. Collateral arrests (sweeping non-targeted individuals) declined from over 25% to under 20% of all arrests. The tactical shift is away from high-profile mass operations toward quieter enforcement relying more on local police partnerships. ICE's own public statements confirm enforcement goals are unchanged.

**Regional enforcement elevations** (arrests increased above national average):
- Kentucky
- Indiana
- North Carolina (new regional field office being established in Raleigh; multiple daily patrols planned)
- Florida

**Regional declines** (arrests down from surge peaks):
- Minnesota (post-Metro Surge drawdown)
- Texas (down from surge levels, though still high overall)

**Workforce expansion**: January 3, 2026 announcement of 120% workforce increase — adding 12,000+ officers and agents through a nationwide recruitment campaign. This represents the most significant ICE workforce expansion in the agency's history.

**Field office expansion**: 150+ new leases and facility expansions documented in 2026, placing new ICE facilities in nearly every state. Significant new investment in suburban and rural areas previously outside consistent ICE coverage.

**Deportation Data Project**: The most current operational data on ICE enforcement tempo is maintained at [deportationdata.org](https://deportationdata.org/data/processed/ice-offices.html) — updates weekly from FOIA-obtained operational data.

Sources:
- [Washington Times — ICE arrests drop nearly 12% after immigration shake-up](https://www.washingtontimes.com/news/2026/apr/25/ice-arrests-drop-nearly-12-minneapolis-killings-immigration-shake/)
- [NPR/MPR News — After the Minnesota surge, ICE is moving to a quieter enforcement approach](https://www.mprnews.org/story/2026/04/04/npr-after-minnesota-ice-surge-shift-to-quieter-enforcement)
- [Portside/Mother Jones — ICE Is Expanding Across the US at Breakneck Speed](https://portside.org/2026-02-12/ice-expanding-across-us-breakneck-speed-heres-where-its-going-next)
- [Vasquez Law Firm — Where ICE Is Expanding Nationwide in 2026](https://www.vasquezlawnc.com/blog/ice-expands-nationwide-2026-next)
- [Britannica — 2025-26 Minnesota ICE Deployment](https://www.britannica.com/event/2025-26-Minnesota-ICE-Deployment)

---

## Part 4: Active Surveillance Legal Challenges

### IRS-ICE Data Sharing Injunctions

*Full case details in litigation-tracker-2026.md (Category 3, entry 3.2)*

Current status as of April 26:
- Judge Kollar-Kotelly (D.D.C.): Found IRS violated federal law 42,695 times. Two orders blocking large-scale transfers remain in place.
- Judge Talwani (D.Mass.): Preliminary injunction blocking the MOU remains in place.
- D.C. Circuit: Denied preliminary injunction for Centro de Trabajadores Unidos, meaning some transfers continue pending merits review.
- ImmigrationOS implication: To the extent ImmigrationOS pulls from IRS data, these injunctions may constrain the platform's data integration.

---

### ICE Tracker Apps — First Amendment Injunction (April 17-23, 2026)

*Full case details in monitoring/2026-04-27-tracking.md, Thread 4*

U.S. District Judge Jorge L. Alonso (N.D. Illinois) granted a preliminary injunction protecting ICE-tracking applications (Eyes Up; ICE Sightings - Chicagoland) from government censorship demands. The injunction blocks the government from pressuring Apple and Facebook to remove the apps. It does not compel Apple or Facebook to restore the apps — platform restoration is each company's independent editorial decision.

As of April 27, neither app has confirmed restoration in its original form. Eyes Up was removed from the App Store in October 2025; ICE Sightings - Chicagoland Facebook group was disabled October 14, 2025.

**Resistance relevance**: This ruling has two implications beyond May Day logistics. First, it establishes that ICE's public operational activity (agents in the field making observable arrests) is a subject of constitutionally protected public documentation and monitoring. Second, it creates a legal record supporting community surveillance of law enforcement as a First Amendment practice — useful for future tool development.

Sources:
- [Reason/Volokh — First Amendment ruling](https://reason.com/volokh/2026/04/18/government-likely-violated-first-amendment-in-getting-apple-and-google-to-block-ice-sightings-content-court-holds/)
- [9to5Mac — Judge blocks government pressure on Apple](https://9to5mac.com/2026/04/20/judge-says-white-house-cant-strong-arm-apple-into-blocking-ice-trackers/)
- [Eric Goldman — injunction analysis](https://blog.ericgoldman.org/archives/2026/04/the-federal-government-used-jawboning-to-censor-ice-transparency-initiatives-rosado-v-bondi.htm)

---

### Maryland HB 711 — State-Level Data Privacy (DMV Records)

Maryland enacted HB 711 (signed 2026), making it illegal to share DMV records with ICE. This is the leading state model for using data privacy law as a brake on immigration enforcement.

Why it matters: DMV databases are one of the most valuable data sources for immigration enforcement — they contain address history, photo, and vehicle registration. By blocking the DMV-ICE data pathway, Maryland closes a significant enforcement data lane. California, Illinois, and New Jersey have similar prohibitions. The legal theory is state sovereignty over state-managed databases — different from sanctuary policy, which operates through non-cooperation with enforcement requests.

Source: [State of Surveillance — Maryland HB 711](https://stateofsurveillance.org/news/maryland-data-privacy-act-hb711-ice-immigration-enforcement-database-2026/)

---

## Part 5: Surveillance Counter-Measures (Confirmed Operational)

For May Day and ongoing protest environments:

| Tool | Status | Notes |
|------|--------|-------|
| Airplane mode / Faraday sleeve | Operational | Prevents location broadcast to ALPR/tower scans |
| Biometric lock bypass | Best practice | Use PIN/password not Face ID or fingerprint — facial recognition + biometric lock is a dual attack surface |
| Signal app | Operational | End-to-end encrypted; recommended for coordination |
| Alianza Americas rapid-response | Operational | [alianzaamericas.org](https://alianzaamericas.org) |
| United We Dream ICE sightings | Operational | [unitedwedream.org](https://unitedwedream.org/take-action/ice-raid-response/) |
| Eyes Up (iOS) | Status uncertain — removed Oct 2025; injunction doesn't compel Apple restoration | Do not direct participants to this as active resource |
| ICE Sightings - Chicagoland | Status uncertain — removed Oct 2025; same injunction | Do not direct participants to this as active resource |
| No Kings Coalition "Eyes on ICE" training | Operational — 200,000+ trained | Active community monitoring network |

*Surveillance context documented in monitoring/2026-04-27-tracking.md, Thread 3*
*Source: TechPolicy.Press — how ICE will spy on protesters (February 11, 2026)*

---

## Cross-Reference Index

| Surveillance issue | Litigation thread | Monitoring file |
|---|---|---|
| IRS-ICE data sharing | litigation-tracker-2026.md 3.2 | — |
| DOGE-SSA data sharing | litigation-tracker-2026.md 3.1, 3.1a | monitoring/2026-04-11.md |
| ICE tracker apps | litigation-tracker-2026.md (CHECKIN note) | monitoring/2026-04-27-tracking.md Thread 4 |
| ImmigrationOS (Palantir) | corporate-accountability-ice-contractors.md | — |
| Section 702 reauth | — | This file; update needed May 1 |
| Warrantless home entry | litigation-tracker-2026.md 1.6 | monitoring/2026-04-11.md |

---

*Created: April 26, 2026*
*Next scheduled update: May 1, 2026 — after Section 702 vote outcome, after May Day*
*See also: corporate-accountability-ice-contractors.md for full contractor accountability tracker*
