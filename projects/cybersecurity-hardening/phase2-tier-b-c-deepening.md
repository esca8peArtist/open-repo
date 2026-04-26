---
title: "Phase 2: Tier B and C Broker Intelligence, Bypass Techniques, and 2026 Policy Watch"
project: cybersecurity-hardening
created: 2026-04-26
status: complete
depends_on: implementation-guide.md, phase2-osint-deepening.md, osint-data-broker-deepening.md
confidence: high — primary sources (USASpending.gov, FedScoop, AFSC Investigate, CFPB, court records, FTC press releases); medium on opt-out operational details where broker documentation is ambiguous
---

# Phase 2: Tier B and C Broker Intelligence, Bypass Techniques, and 2026 Policy Watch

**How this document fits the trilogy**: `implementation-guide.md` Part 0 covers opt-out mechanics for Tier A law enforcement data vendors and the highest-priority listing brokers. `phase2-osint-deepening.md` covers ID barriers, Clearview BIPA litigation, and the CCPA/PADFAA regulatory landscape. This document goes deeper on two things those documents do not fully address: the brokers between Tier A and the people-search commodity sites (Tier B and C), and the scenarios where opt-out is unavailable or inapplicable. Read `implementation-guide.md` Part 0 first — this document extends it, not replaces it.

**Lead finding**: The mid-tier broker landscape (Tier B) is where most people's address history, employment records, property records, and financial behavior data live in a form that is practically accessible to law enforcement without a warrant but that also has meaningful opt-out mechanisms. TransUnion TLOxp is the most important addition not covered in Part 0 — it holds an active ICE contract, reaches 95% of the U.S. population, and accepts a consumer suppression request. CoreLogic (now rebranded Cotality) is the primary property and tenant-screening database and has a targeted opt-out for California residents. Equifax Workforce Solutions (The Work Number) holds employment history on virtually the entire salaried workforce and provides a data freeze that is free and immediate.

---

## Part 1 — Tier B Brokers: Medium Surveillance Risk, Partial Opt-Out Paths

Tier B brokers are distinguished from Tier A by one or more of these characteristics: they lack a confirmed direct ICE/CBP/FBI law enforcement contract, their law enforcement relationship is documented but dated or smaller in scope, or they primarily function as a data supplier to Tier A vendors rather than a direct law enforcement tool. All Tier B brokers still represent meaningful exposure because they either feed into Tier A products or have law enforcement data-sharing provisions in their terms of service that enable warrantless government access on request.

---

### 1.1 TransUnion / TLOxp

**Risk level**: High — active ICE contract, near-universal coverage.

**What it holds**: TLOxp aggregates over 100 billion public and proprietary data points, with self-reported coverage of more than 95% of the U.S. population. Data types include: current and historical addresses, phone numbers, relatives, associates, business affiliations, court records, vehicle registrations, professional licenses, and digital identifiers. TransUnion's core credit bureau data feeds directly into TLOxp queries, giving law enforcement access to financial account history alongside OSINT aggregation.

**Government contracts**: ICE awarded TransUnion a contract in September 2023 with a potential end date of September 2028, value up to $1.1 million per documented award — but this likely understates the full scope, as ICE's main TLOxp relationship is through a broader "support services" award structure. Separately, Brennan Center obtained the TLOxp Law Enforcement Transactional Pricing Schedule through FOIA, confirming per-query pricing for law enforcement agencies covering address history, associate mapping, and real-time location functions. CBP held an earlier TLOxp contract that ended in 2015; the current ICE contract appears to have replaced it. ([AFSC Investigate: TransUnion](https://investigate.afsc.org/company/transunion), [Brennan Center: TLOxp Pricing](https://www.brennancenter.org/sites/default/files/2024-04/C1007%20TLOxp%20Transactional%20Pricing.pdf))

**No-consent breach history**: TransUnion's U.S. consumer database was breached in July 2025. Attackers gained unauthorized access to a third-party consumer support application, compromising Social Security numbers and personal information of more than 4.4 million Americans. The incident was contained within hours of detection, but the breach window ran from July 28, 2025, until detection — meaning data was accessible externally during that period. ([TransUnion data breach reporting, July 2025](https://money.com/transunion-data-breach/))

**Opt-out mechanism (2026 confirmed)**: TransUnion's consumer-facing opt-out covers its credit bureau and people-search products. For the law enforcement TLOxp product specifically, TransUnion does not offer a public consumer suppression mechanism distinct from credit bureau opt-out. The achievable action is:
1. Submit the TransUnion opt-out for marketing and people-search: [transunion.com/consumer-privacy](https://www.transunion.com/consumer-privacy)
2. Place a credit freeze with TransUnion (free, immediate, effective): [transunion.com/credit-help/credit-freeze](https://service.transunion.com/dss/freeze_index.page). A freeze doesn't prevent TLOxp law enforcement queries against your credit history, but it limits the marketing data footprint.
3. Dispute inaccurate information in your credit file — inaccurate addresses in the credit bureau database degrade TLOxp address confidence scores used in location targeting.

**Practical countermeasure**: Inconsistent address history is specifically useful against TransUnion because TLOxp's law enforcement value lies in address confidence. If you've recently moved, promptly update your address with creditors (so your credit file reflects current reality) while removing your old address from people-search brokers. This creates a single authoritative current address in the credit bureau layer without leaving a trail of uncontrolled historical addresses in the people-search layer.

---

### 1.2 CoreLogic / Cotality

**Risk level**: Medium — property and tenant screening focus; no confirmed direct ICE contract, but address verification use is documented.

**What it holds**: CoreLogic rebranded to Cotality in March 2025. It is the dominant property data aggregator in the U.S., covering mortgage origination, property ownership, deed and lien records, tenant screening, and homeowner associations. CoreLogic data is used in address verification for financial services, insurance underwriting, and background checks. Because property records are a primary vector for locating current addresses, CoreLogic-derived data reaches law enforcement indirectly through aggregators like LexisNexis/Accurint that purchase property data as a feed. ([CoreLogic rebrand to Cotality, March 2025](https://www.cotality.com/press-releases/meet-cotality))

**Government contracts**: No confirmed direct DHS or ICE contract for immigration enforcement purposes as of April 2026. CoreLogic's stated government clients are in the financial regulation and housing policy sectors. The indirect exposure is through data resale: LexisNexis's Accurint product (which has a confirmed $22.1 million ICE contract) ingests property and address data from multiple commercial vendors including CoreLogic. Suppressing your CoreLogic record degrades the accuracy of downstream Accurint profiles.

**No-consent breach history**: No major public breach attributed to CoreLogic/Cotality as of April 2026.

**Opt-out mechanism (2026 confirmed)**: CoreLogic's opt-out is currently California-resident-only for full deletion. All U.S. residents can submit a request for inaccurate data correction. Process:
- California residents: Email privacy@corelogic.com with subject "CCPA Deletion Request." Include full name and California address. CoreLogic must acknowledge within 10 business days and complete processing within 30-45 days. CoreLogic may place a suppression flag that prevents re-ingestion from public records on an ongoing basis — request this explicitly.
- Non-California residents: Call 1-800-634-4149 to request review of specific records. This does not carry CCPA deletion force, but data correction requests for inaccurate information must be honored under FCRA (if your data is used in tenant screening decisions).
- Formerly listed at https://optout.corelogic.com/ — this URL now redirects to Cotality's privacy page (cotality.com/privacy). Submit by email until a new direct form is confirmed.

**Practical countermeasure**: If you rent and have moved, request removal of your previous addresses from Cotality and from tenant screening systems (separate action: submit a dispute to any tenant screening report you've received). Tenant screening companies are required to give you a copy of your report and a dispute mechanism under FCRA when an adverse action is taken. Proactively requesting your report before applying prevents surprises.

---

### 1.3 Equifax Workforce Solutions — The Work Number

**Risk level**: Medium-high — employment and income data; covers virtually the entire salaried U.S. workforce.

**What it holds**: The Work Number database (operated by Equifax Workforce Solutions) aggregates payroll data directly from employers via ADP, Gusto, Workday, and most major payroll providers, which sync paycheck data automatically every two weeks in most cases. It holds: employer name, employment dates, compensation history, pay frequency, and in some integrations, 401(k) contribution data. The database is used for income verification by landlords, mortgage lenders, and — per Equifax's own documentation — government agencies with a valid FCRA permissible purpose. ([Fast Company: Facebook and America's largest companies quietly give worker data to Equifax](https://www.fastcompany.com/40485634/equifax-salary-data-and-the-work-number-database))

**Government contracts**: Equifax Workforce Solutions explicitly states that employment verifications may be provided to immigration officials needing confirmation of employment, along with other law enforcement agencies with a valid FCRA permissible purpose. This is not an ICE direct-access contract in the Accurint sense — it is FCRA-governed response to legal process. However, for immigration enforcement specifically, knowing that a person's employer has submitted their payroll data to The Work Number creates a secondary exposure vector: if ICE learns an individual's employer through other means, they can legally obtain income and employment confirmation through The Work Number under FCRA.

**No-consent breach history**: Equifax's larger 2017 breach (147 million Social Security numbers) affected the credit bureau, not The Work Number directly. No major public breach specific to The Work Number as of April 2026.

**Opt-out mechanism (2026 confirmed)**: The Work Number offers a free data freeze — not an opt-out, but a freeze that prevents most verifiers from accessing your employment history. This is the most useful available action.
- URL: https://employees.theworknumber.com/employee-data-freeze
- Process: Create an account (requires SSN and employer name), request a data freeze. Processed within three business days. Free of charge.
- Consequence of freeze: Landlords, lenders, and employers cannot verify your employment history through The Work Number during the freeze period. You can lift it temporarily for a specific transaction and then re-freeze.
- Limitation: A freeze prevents prospective verifiers from accessing data. It does not delete existing employment history from the database or prevent access by parties with existing access before the freeze.

**Practical countermeasure**: Place a Work Number freeze if you are at risk and do not currently need employment verification for housing or credit applications. For people who have recently changed employers or moved — the transition period is when The Work Number data is most likely to be used to locate you. Freeze it during that window.

Note on scope: The Work Number's enforcement relevance is not from ICE querying it directly. The relevance is that skip-tracing contractors — ICE signed contracts with 13 companies worth up to $1.2 billion over two years in December 2025, with contractors receiving up to 50,000 names per month to locate — can use employment data to confirm that a target is still in a given city, narrow address candidates, or verify a tip. Contractors named in reporting include Bluehawk LLC, SOS International, and BI Incorporated (linked to GEO Group, a private prison operator). ([Source Material: ICE Skip Tracing Contracts, December 2025](https://sourcematerialblog.substack.com/p/ice-signs-deals-potentially-worth)) A Work Number freeze does not prevent law enforcement from obtaining employment information via subpoena, but it removes the frictionless query access that these private contractors use.

---

### 1.4 Verisk Analytics

**Risk level**: Medium — insurance and claims focus; indirect law enforcement exposure.

**What it holds**: Verisk is primarily an insurance industry data aggregator. Its core products include: ISO (Insurance Services Office) auto and property claims history, ClaimSearch (claims fraud detection database covering 1+ billion claims from 1,600+ insurers), and property risk assessment data. The data types most relevant to surveillance are: prior insurance claims by address, vehicle ownership and accident history, and property damage event history. These feed into address history reconstruction — knowing what addresses were insured under a given name provides historical location data distinct from credit bureau address history.

**Government contracts**: No confirmed direct immigration enforcement contract. Verisk noted in Q4 2025 earnings calls that a government contract work stoppage began in Q1 2026 affecting revenue — but this appears to be in the financial/regulatory analytics sector, not immigration enforcement. Verisk's exposure to law enforcement use is primarily indirect: insurers submit subrogation claims that reveal addresses; those records sit in ClaimSearch, which is accessible to participating insurers and, on request with appropriate legal process, to law enforcement.

**No-consent breach history**: No major public breach attributed to Verisk as of April 2026.

**Opt-out mechanism (2026 confirmed)**: Verisk's consumer-facing opt-out is limited. Process:
- URL: https://www.verisk.com/privacy/ (navigate to "Consumer Information" section)
- Scope: You can request a copy of your FACT Act disclosure (your insurance history report) and dispute inaccurate information. This is FCRA-governed and applies to data used in insurance decisions.
- Limitation: Verisk's property risk assessments are made at the property level, not the individual level, and are not subject to individual opt-out. Your insurance history is tied to claims you filed — those records cannot be removed if accurate, only corrected if inaccurate.

**Practical countermeasure**: Request your FACT Act disclosure from Verisk (free, once per year) to see what's in your claims file. Correct any inaccurate address entries. An inaccurate historical address in your claims file degrades address history confidence for anyone using insurance data as a location vector.

---

### 1.5 Clarity Services (Experian Subsidiary)

**Risk level**: Medium — alternative financial services focus; subprime credit data.

**What it holds**: Clarity Services, owned by Experian since 2017, is a specialty consumer reporting agency focused on the subprime and non-traditional lending market. Data types include: payday loan history, installment loan applications, check cashing activity, rent-to-own transactions, telecom account applications, and financial service transactions from the lower-income and subprime market segments. Clarity specifically serves lenders who serve the population that does not use traditional credit — making it an important database for people without standard credit histories, including immigrants and people new to the U.S. financial system. ([Clarity Services: CFPB Listing](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/consumer-reporting-companies/companies-list/clarity-services/))

**Government contracts**: No confirmed direct law enforcement or immigration enforcement contract. Clarity's law enforcement exposure is through FCRA permissible purpose requests — law enforcement can legally request consumer reports from CRAs including Clarity with appropriate legal process. Because Clarity holds financial account activity for people who may not appear in traditional credit bureaus, it is a secondary data source for building financial profiles of individuals with limited traditional credit history.

**No-consent breach history**: No major public breach specific to Clarity Services as of April 2026.

**Opt-out mechanism (2026 confirmed)**: Clarity Services allows opt-out from prescreened offers only — it does not offer a CCPA-style deletion for non-California residents. Options:
- Prescreened offer opt-out: Email clarityconsumers@experian.com or call (714) 830-7613. Opt-out covers 5-year or permanent removal from prescreened lists.
- California CCPA deletion: File through Experian's parent CCPA request mechanism (see Section 2.1) — Clarity as an Experian subsidiary is covered under Experian's CCPA obligations.
- Request your Clarity report under FCRA: Visit clarityservices.com and submit a consumer disclosure request. Review for accuracy and dispute any inaccurate items. ([clarityservices.com](https://www.clarityservices.com/support/opt-out-2/))

**Practical countermeasure**: For people with limited traditional credit history who use alternative financial services, request your Clarity report to understand what's in it. Clarity is particularly relevant for individuals who have used check cashing services, payday lenders, or similar providers — these transactions are in the Clarity database even if they don't appear on your traditional credit report.

---

### 1.6 Samba TV

**Risk level**: Medium — smart TV viewing data; political and behavioral profiling.

**What it holds**: Samba TV uses automatic content recognition (ACR) technology embedded in smart TVs (Sony and others) to track viewing history at the frame level. Data collected includes: what you watch, when, for how long, your IP address, household demographics inferred from viewing, and political behavior inferences from content choices. This data is sold to political campaigns, advertisers, and content producers. A California federal court allowed wiretap and federal privacy claims against Samba TV to proceed in April 2026, ruling that collecting viewing data without consent from consumers was actionable. ([Law360: Samba TV Must Face Wiretap Claims, April 2026](https://www.law360.com/classaction/articles/2468645))

**Government contracts**: No confirmed direct law enforcement or immigration enforcement contract. Samba TV's privacy policy discloses that it may share personal information with law enforcement in response to valid legal requests. The exposure for the implementation guide's audience is primarily political: viewing behavior data sold to political campaigns can be used to identify political sympathizers, protest attendees, and organizers through household-level inference from news consumption patterns.

**No-consent breach history**: No major public breach as of April 2026. The April 2026 litigation concerns the unconsented collection itself — Samba's ACR operates by default on compatible TVs, meaning collection occurs before consumers are aware of it.

**Opt-out mechanism (2026 confirmed)**: Samba TV offers an ACR opt-out:
- URL: https://www.samba.tv/legal/opt-out
- Process: Visit the page, enter your email, select opt-out. No ID required.
- Also opt-out through your TV settings directly, which is more reliable because it prevents data collection at the source rather than just removing you from the downstream sales pipeline:
  - **Sony Bravia (Google TV/Android TV)**: Home button > Settings > Initial Setup > Samba Interactive TV > Off. Also: Settings > Device Preferences > Usage & Diagnostics > Off. Sony requires both toggles because it runs both Samba's ACR and Google's own viewing diagnostics simultaneously. ([SmartHomePerfected: How to Disable ACR, 2026](https://www.smarthomeperfected.com/how-to-disable-acr-smart-tv/))
  - **Samsung**: Settings > Support > Terms & Privacy > Viewing Information Services > Off
  - **LG**: Settings > All Settings > General > Live Plus > Off
  - **Vizio**: System > Reset & Admin > Viewing Data > Off
- Limitation: Data already collected before opt-out is retained. Opt-out stops future collection. Legal note: Texas AG lawsuits filed against Sony, LG, Hisense, and TCL in 2025 argue that existing ACR disclosures are inadequate under Texas consumer protection law — these cases are ongoing as of April 2026.

**Practical countermeasure**: Disable ACR through your TV settings directly and complete the web opt-out as a secondary layer. Keep your smart TV on a separate network segment from your primary devices (a guest WiFi or a dedicated VLAN if your router supports it). This limits the correlation between your TV viewing behavior and your primary IP address, reducing the quality of Samba's household identity graph about you.

---

### 1.7 Early Warning Services (EWS)

**Risk level**: Low-Medium — banking fraud data; limited opt-out.

**What it holds**: EWS is a consortium database co-owned by Bank of America, Capital One, JPMorgan Chase, PNC Bank, Truist, U.S. Bank, and Wells Fargo. It holds data on checking and savings account applications, closures, and fraud events. It also operates the Zelle payment network. Data types include: bank account application history, reason codes for account closures, check fraud flags, and payment transaction data. EWS is one of the "second-tier" credit bureaus for banking — a negative EWS record can prevent you from opening a bank account at major financial institutions. ([Early Warning Services: CFPB Listing](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/consumer-reporting-companies/companies-list/early-warning-services-llc/))

**Government contracts**: No confirmed direct law enforcement contract. EWS data is accessible to law enforcement through FCRA-permitted financial institution requests and subpoenas. In December 2024, the CFPB filed suit against EWS, Bank of America, JPMorgan Chase, and Wells Fargo for failing to adequately protect consumers from Zelle fraud — this is a consumer harm case, not a surveillance case, but it highlights EWS's institutional posture on consumer data.

**No-consent breach history**: EWS itself has not had a publicly reported data breach as of April 2026. The Zelle fraud litigation concerns failure to remediate fraud losses, not unauthorized data access.

**Opt-out mechanism (2026 confirmed)**: EWS offers a consumer disclosure request (to see your file) and a dispute process for inaccurate information. There is no deletion opt-out — EWS records are FCRA-regulated and accurate negative information cannot be removed. Contact: 800-325-7775. ([earlywarning.com/consumer-information](https://www.earlywarning.com/consumer-information))

**Practical countermeasure**: Request your EWS consumer disclosure annually to check for inaccurate negative flags. An inaccurate flag can prevent bank account access — dispute it under FCRA if found.

---

### 1.8 Acxiom

**Covered in**: `implementation-guide.md` Step 0.2 (Priority 7-20 table). **New information since publication**:

In January 2025, a federal class action was filed in the Eastern District of Virginia alleging that Acxiom sold millions of Virginia residents' personal information to third parties without consent, violating Virginia's consumer data property rights statute. The case is ongoing as of April 2026. ([Bloomberg Law: Acxiom Sold Data Without Consent, 2025](https://news.bloomberglaw.com/privacy-and-data-security/acxiom-sold-millions-of-peoples-data-without-consent-suit-says)) This strengthens the case for completing the Acxiom opt-out already listed in Part 0.

**Opt-out URL (confirmed April 2026)**: https://isapps.acxiom.com/optout/optout.aspx — still active and functional. KBA-based, no ID upload required.

---

## Part 2 — Tier C Brokers: Lower Surveillance Risk or Harder to Access

Tier C brokers are either: (a) lower direct law enforcement risk because they lack confirmed government data relationships and are primarily consumer-facing marketing or people-search tools; (b) harder to opt out of due to technical or institutional friction; or (c) specialty databases that are relevant to narrower sub-populations. Complete these after Tier A and Tier B actions.

---

### 2.1 Experian

**Risk level**: Low-Medium — credit bureau with marketing subsidiary; opt-out path fragmented.

**What it holds**: Experian operates as both a credit bureau (FCRA-regulated) and a marketing data broker (Experian Marketing Services, Experian Health, Experian Consumer Services). The marketing arm holds purchase behavior, lifestyle inferences, loyalty card data, email response behavior, and demographic profiles. Experian Marketing Solutions is registered as a data broker in Texas and other states. Experian subsidiary Clarity Services (see Section 1.5) covers the subprime credit segment separately.

**Government contracts**: Experian is described in media coverage as part of the broader commercial data ecosystem that feeds immigration enforcement — but no direct confirmed ICE or CBP contract for Experian's core products has been documented in public records as of April 2026. Experian's privacy policy explicitly states it may share data to comply with law enforcement requests and legal process, which creates indirect exposure. State of Surveillance's reporting on ICE's data ecosystem names Experian as a "credit bureau turned surveillance company" in the broader ecosystem, but contract-level sourcing for Experian specifically is not available in public records. ([State of Surveillance: Data Brokers and ICE, 2025](https://stateofsurveillance.org/articles/corporate/data-brokers-ice-contracts/))

**No-consent breach history**: Experian's largest breach was the T-Mobile data breach of 2015 (15 million T-Mobile customer records exposed through Experian's credit checking system). No major breach specific to Experian's marketing data as of April 2026.

**Opt-out mechanism (2026 confirmed)**: Experian's opt-out is fragmented across products:
- Marketing direct mail: Email optout@experian.com or visit https://www.experian.com/privacy/opting_out
- Targeted advertising: https://www.experian.com/privacy/opt-out-targeted-advertising
- Marketing channel-specific opt-out (separated by direct mail, telemarketing, email, online ads): https://www.experianmarketingservices.digital/OptOut
- Credit bureau freeze (separate from marketing opt-out): https://www.experian.com/freeze/center.html — free, immediate. A credit freeze does not affect Experian Marketing's data.
- California CCPA deletion (covers Experian Marketing Services and Clarity subsidiary): Submit via consumerprivacy.experian.com or call 833-210-4615.

**Practical countermeasure**: Complete all four opt-out paths — they cover different products. The credit freeze is the highest-priority action because it prevents new credit inquiries that create fresh address data points. The marketing opt-out reduces the behavioral profile fed to downstream marketing aggregators.

---

### 2.2 Axiom (note: distinct from Acxiom)

**Risk level**: Low — regional and niche data aggregation.

**Note on naming confusion**: "Axiom" is a common generic name used by multiple unrelated companies. The major data broker in this space is **Acxiom** (covered in Part 1.8 and in `implementation-guide.md` Part 0). If you encounter references to "Axiom" as a data broker in opt-out guides, verify you are not looking at a name variant of Acxiom. Legitimate separate "Axiom" data companies typically operate in narrower verticals (legal data, real estate data) and have FCRA dispute mechanisms for their specific category.

---

### 2.3 LexisNexis (Consumer File)

**Covered in**: `implementation-guide.md` Step 0.2, Priority 1. **Update since publication**:

LexisNexis disclosed a data breach in April 2025. The incident occurred December 25, 2024, but remained undetected for months. 364,333 individuals had their names, dates of birth, Social Security numbers, and driver's license numbers exposed via a third-party GitHub account used in LexisNexis's development pipeline. ([TechCrunch: LexisNexis breach, May 2025](https://techcrunch.com/2025/05/28/data-broker-giant-lexisnexis-says-breach-exposed-personal-information-of-over-364000-people/))

The ICE contract was under renewal pressure in early 2025 — over 80 advocacy organizations including EPIC, NIJC, POGO, Just Futures Law, and Mijente called on DHS not to renew. The USASpending.gov record shows a new LexisNexis contract with ICE (CONT_AWD_70B06C26F00000023) active in 2026, suggesting the contract was renewed. The total value of LexisNexis's ICE relationship is now documented at $22.1 million. ([EPIC coalition letter to ICE, 2023](https://epic.org/epic-coalition-call-for-ice-to-cancel-contract-with-lexisnexis-for-invasive-surveillance-databases/), [FedScoop coverage](https://fedscoop.com/nonprofits-oppose-lexisnexis-contract-renewal/), [USASpending.gov](https://www.usaspending.gov/award/CONT_AWD_70B06C26F00000023_7014_GS00F178DA_4732))

The 2025 breach underscores that submitting your SSN and ID to LexisNexis's opt-out system carries real risk — you are handing a law enforcement data vendor the most sensitive identifiers you possess, through a system that was breached the prior December. Weigh this explicitly. If you are in a high-risk category and have completed LexisNexis opt-out previously, monitor [HaveIBeenPwned](https://haveibeenpwned.com) for your email address being included in the LexisNexis breach data as it propagates.

---

### 2.4 Smaller Regional Brokers

The following warrant batch attention in a single afternoon session. These are primarily people-search brokers without confirmed law enforcement relationships but with wide public visibility — they are what a private investigator, a stalker, or a bail bonds company would use, and they contribute to the public-facing data profile that feeds the larger aggregators over time.

| Broker | Opt-Out URL | Notes |
|--------|-------------|-------|
| PrivateEye | https://www.privateeye.com/static/view/optout/ | People-search |
| Clustrmaps | https://clustrmaps.com/bl/opt-out | Crowd-sourced location data |
| Neighbor.report | https://neighbor.report/remove | Address-associated reporting |
| Nuwber | https://nuwber.com/removal/link | People-search |
| USPhoneBook | https://www.usphonebook.com/opt-out | Phone-to-name lookup |
| Spy Dialer | https://www.spydialer.com/optout.aspx | Phone and address lookup |
| NumLooker | https://www.numlooker.com/removal/ | Phone lookup |
| LocatePeople | https://www.locatepeople.org/optout | Skip-tracing focused |
| PublicRecords360 | https://www.publicrecords360.com/optout.html | Public records aggregation |
| PeopleSmart / Coreplus | https://www.peoplesmart.com/optout | Rebrands frequently |

Source: [Big-Ass-Data-Broker-Opt-Out-List (GitHub, March 2026)](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List)

**Batch strategy**: Use a single spare email address for all confirmations from this list. Set a calendar reminder for 30 days to verify removal and re-submit any that haven't processed. Many of these brokers process opt-outs within 24-72 hours.

---

### 2.5 DataLogix / Oracle Data Cloud

**Risk level**: Low — marketing behavioral data; opt-out available, no confirmed LE relationship.

**What it holds**: Oracle Data Cloud (formerly DataLogix, acquired 2014) aggregates purchase behavior from loyalty card programs, subscription data, and retail transaction records. It holds purchase-behavior profiles tied to household addresses and email addresses — what you buy, where, and at what frequency. This data is sold for targeted advertising. The risk for this document's audience is primarily behavioral fingerprinting: loyalty card data can reveal store locations, which reveals neighborhood and travel patterns.

**Government contracts**: No confirmed direct law enforcement contract. Oracle's government cloud division is separate from Oracle Data Cloud and operates in defense and intelligence sectors; no cross-contamination into the consumer data brokerage function has been publicly documented.

**Opt-out mechanism (2026 confirmed)**: Oracle's opt-out for Data Cloud targets marketing use:
- URL: https://www.oracle.com/legal/privacy/marketing-cloud-data-cloud-privacy-policy.html (navigate to "Your Privacy Rights / Opt Out" section)
- Process: Submit a request form with name and email. No ID required.
- California CCPA: Oracle Marketing Cloud accepts CCPA deletion requests at oracleprivacy@oracle.com.
- Limitation: Opt-out removes you from Oracle Data Cloud's marketing pipelines. It does not affect Oracle's enterprise cloud or government cloud products.

**Practical countermeasure**: Cancel loyalty cards that you use primarily for discounts at stores near your home. The discount is not worth the location-behavior data trail. Most grocery stores and pharmacies offer equivalent prices without a loyalty card, or have one-time coupon codes that don't require account registration.

---

## Part 3 — 2026 Policy Watch: Legislation That Changes Everything

This section tracks three legislative and regulatory vectors that could materially change which brokers are reachable by opt-out, which protections remain in place, and which enforcement regimes exist.

### 3.1 SECURE Data Act (HR 8413) — The Preemption Threat

**Introduced**: April 22, 2026, by House Energy and Commerce Committee Vice Chairman John Joyce (R-PA). Referred to committee on introduction date.

**What it does, affirmatively**: Requires FTC data broker registration nationwide. Creates national minimum standards for data collection, use, and deletion rights. Provides consumers a right to know, correct, and delete personal information.

**What it does, destructively**: The bill embraces "strong preemption" — any state law or provision that "relates to" the bill's provisions would be rendered moot. Legal analysis (IAPP, Future of Privacy Forum) identifies the following state frameworks at risk: ([IAPP: SECURE Data Act Analysis](https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill))
- California CCPA/CPRA (likely partially preempted)
- California DELETE Act and DROP platform (likely preempted — federal broker registration would supersede California's DELETE Act registration system)
- Colorado CPA, Connecticut CTDPA, and equivalent state laws
- State biometric privacy statutes without private rights of action (Texas CUBI, Washington WFBPA) are less at risk because they may be characterized as non-conflicting sector law
- Illinois BIPA: Its private right of action and explicit damages schedule may be harder to preempt because BIPA predates most federal privacy framework discussions and has generated significant case law

**Current status (April 2026)**: Committee referral only. The bill is a Republican-only effort as introduced and lacks the bipartisan support that would accelerate passage. It is likely to be significantly revised through negotiation. Even in its introduced form, preemption would not be automatic — individual state laws would need to be challenged in federal court on a provision-by-provision basis.

**Broker impact if enacted**:
- Tier A: FTC registration creates a public list of data brokers, giving advocates a targeting list for PADFAA and consumer rights complaints. This is the bill's most positive feature for the implementation guide's audience.
- Tier B: National deletion rights would extend opt-out access to residents of states that currently lack CCPA-equivalent protections.
- Tier C: Preemption of state enforcement removes the most active enforcement mechanism (California AG + CPPA) that has generated real fines against unregistered brokers.

**Watch indicator**: Track EFF Deeplinks (https://www.eff.org/deeplinks) and IAPP (https://iapp.org) for committee markup activity. If the bill receives a markup hearing, legislative movement is likely within 60-90 days.

---

### 3.2 PADFAA — The Pressure Lever

**What it is**: The Protecting Americans' Data from Foreign Adversaries Act (enacted June 23, 2024) prohibits data brokers from selling sensitive data (geolocation, biometrics, health, financial, military status) to entities controlled by or based in China, Russia, Iran, or North Korea.

**2026 enforcement status**: On February 9, 2026, the FTC sent warning letters to 13 data brokers reminding them of PADFAA obligations. The FTC specifically identified instances where brokers offered military status data — one of the enumerated sensitive categories. Civil penalties under PADFAA can reach $53,088 per violation. ([FTC PADFAA reminder letters, February 2026](https://www.ftc.gov/news-events/news/press-releases/2026/02/ftc-reminds-data-brokers-their-obligations-comply-padfaa))

**Strategic relevance for this document**: PADFAA is an indirect lever for advocates. Brokers that sell sensitive data categories (location, health, financial) to both foreign entities and domestic law enforcement are simultaneously:
1. Subject to FTC PADFAA enforcement for the foreign sales
2. Subject to advocacy pressure on the domestic law enforcement sales

A broker facing PADFAA compliance exposure for its foreign data sales may be more responsive to opt-out requests and more careful about documentation of its law enforcement data access protocols — because PADFAA creates an active FTC enforcement relationship that increases regulatory scrutiny generally.

**Broker impact by tier**:
- Tier A (Venntel/Gravy): FTC already acted against Gravy Analytics in January 2025. PADFAA is a reinforcing pressure, not a new one.
- Tier B (TransUnion, Verisk, Samba TV): All sell data in categories PADFAA covers (location, financial, viewing behavior). The February 2026 FTC letters may have included some of these companies (the named recipients were not publicly disclosed).
- Tier C (people-search brokers): PADFAA's "data broker" definition is broad enough to potentially cover people-search sites that sell data to foreign buyers. Enforcement against this tier has not yet been documented.

---

### 3.3 State Ballot Measures and Legislative Pipeline — Fall 2026

**California Kids AI Safety Act ballot initiative**: Expected to qualify for the November 2026 ballot. Packages children's data protections including bans on selling children's data and a private right of action for violations. While primarily child-focused, the private right of action mechanism — if established by ballot initiative — could create model language for broader privacy ballot measures. ([Squire Patton Boggs: 2025 State Privacy Roundup](https://www.squirepattonboggs.com/insights/publications/2025-state-privacy-roundup-key-trends-and-california-developments-to-watch-in-2026/))

**California SB 361 (effective January 2026)**: Already in effect. Requires data brokers to disclose AI use, whether they share data with government entities or law enforcement, and whether they share data with foreign adversaries. Doubles penalties for non-compliance. This disclosure requirement is directly relevant to Tier A and Tier B brokers — it creates a public record of which California-registered brokers self-report government data sharing. ([ScanComply: SB 361 analysis](https://scancomply.com/blog/california-sb-361-data-broker-law-2026))

**BIPA-model legislation in non-Illinois states**: The Clearview AI settlement's success has generated interest in biometric privacy legislation with private rights of action in additional states. Texas and Washington have biometric statutes without private rights of action; advocacy groups are pushing for amendments. If either state adds a private right of action in 2026 legislative sessions, the litigation landscape shifts significantly — both states have major biometric data processor presences.

**Broker impact by tier if state pipeline advances**:
- Tier A (Clearview AI, Venntel): Already under settled consent orders and FTC action. State BIPA expansion primarily affects new violators, not settled defendants.
- Tier B (TransUnion, Samba TV, CoreLogic): All serve California-registered data product customers. SB 361 disclosure requirements force these brokers to publicly acknowledge government data relationships, creating public records useful for advocacy and litigation.
- Tier C (people-search brokers): DROP enforcement for unregistered brokers continues to generate fines. The $200/day-per-unfulfilled-deletion-request penalty structure creates increasing financial pressure on non-compliant smaller brokers.

---

## Part 4 — Broker Bypass Techniques: When Opt-Out Is Unavailable

Not all data can be reached through opt-out. This section addresses four specific scenarios where standard opt-out either doesn't apply or is structurally blocked, and documents what is actually achievable in each case.

### 4.1 Scenario: Data Already Sold Before Your Opt-Out

**The problem**: Data broker opt-outs are prospective. When you submit a deletion or opt-out request, the broker must delete your data from its current database and stop future sales. It cannot recall data already delivered to third-party customers. ICE, marketing companies, and political campaigns that purchased your data before your opt-out date retain that data subject to their own retention policies, not the broker's.

**What is actually achievable**:
- Opt-outs stop future data accumulation and sale. They do not erase historical exposure.
- The American Dragnet report (Georgetown Center on Privacy, 2022, still the most comprehensive public analysis) documents that ICE's ELITE platform builds profiles from aggregated fragmented records — partial suppression of data feeds still degrades profile quality by reducing data density and confidence scores. A profile built on 10 data sources with current addresses is more actionable than a profile built on 5 sources with 3-year-old addresses. Opt-outs are worth doing even if some data has already been sold. ([American Dragnet, Georgetown Center on Privacy](https://americandragnet.org/))
- For data sold to marketing companies: Most marketing platforms honor downstream opt-out signals (NAI, DAA opt-outs; Global Privacy Control) that suppress use of previously purchased data for targeting purposes, even if they cannot delete the underlying data. Complete the NAI and DAA opt-outs in Step 0.1 of the implementation guide.
- For data sold to law enforcement: No mechanism exists to recall data delivered under a law enforcement contract. The countermeasure for already-sold law enforcement data is platform-level (not broker-level): reduce future MAID generation, change your address association patterns, and implement the Parts 1-3 countermeasures in the implementation guide.

---

### 4.2 Scenario: No Record Found — You Can't Opt Out What Isn't Listed

**The problem**: Some brokers require you to locate your own record in their search interface before submitting an opt-out. If you search your name and find no record, the process ends there — but this doesn't mean the broker has no data on you. Some brokers hold data only accessible in their paid or law enforcement tiers, not the public-facing search.

**What is actually achievable**:
- Use multiple name variations (middle name, middle initial, no middle name), multiple cities (current and all past addresses for the last 10 years), and maiden/former names.
- Try searching your phone number and email address instead of name — some brokers index by contact information rather than name.
- If no record appears on any variation: note this and move on. The absence of a listing-tier record is good news for privacy from the public-facing layer. It does not mean absence from the law enforcement tier.
- For brokers with known law enforcement access that have no consumer search interface (CLEAR, TLOxp law enforcement product): accept that the consumer opt-out does not reach the law enforcement layer. Focus on platform countermeasures.

---

### 4.3 Scenario: No U.S. Address on File — Opt-Outs That Require Address Verification

**The problem**: Many opt-out forms require you to enter a current address to locate your record. If you are recently arrived, have never had a U.S. address, are homeless, or are using a P.O. box or UPS Store mailbox, these forms may be unable to locate your record — or may create a new address association in their database from the address you provide in the opt-out form.

**What is actually achievable**:
- Use previous addresses: If you previously had a U.S. address (a shelter, a friend's address used for mail, a prior apartment), use that to search for your record. Opt-out using that address entry; the broker's record is likely indexed under that address.
- Virtual mailbox services (e.g., Earth Class Mail, Traveling Mailbox): These provide a real street address (not P.O. box) that some forms accept. The risk: using a virtual mailbox creates a new address data point that will be associated with your name in future data broker pulls. For Tier 3 individuals, this is not a useful option.
- Focus on KBA-based brokers: Acxiom and Epsilon use Knowledge-Based Authentication (security questions about your history) rather than address entry. These are accessible without a current U.S. address.
- California DROP if applicable: DROP accepts California state ID under AB 60/AB 1766, which does not require proof of authorized presence. If you have a California ID obtained under these statutes, use DROP — it reaches all registered California brokers without individual address searches. (Covered in detail in `implementation-guide.md` Step 0.1 and `phase2-osint-deepening.md` Part B.)
- Accept the limit: For recently arrived individuals or those with no prior U.S. address, the broker opt-out layer is largely inaccessible. The higher-leverage actions are platform-level: obtain GrapheneOS or a hardened iOS device, rotate or reset your advertising ID (see implementation guide Part 3), and minimize app installs that generate MAID location data.

---

### 4.4 Scenario: No Government ID — Brokers That Demand ID Upload

**The problem**: LexisNexis, Thomson Reuters CLEAR, and Clearview AI require government-issued photo ID for opt-out or removal. These are simultaneously the highest-risk Tier A brokers and the ones with the highest ID verification friction. The population most targeted by these databases is the population least likely to have U.S. government-issued ID.

**Documented options (confirmed and unconfirmed — see confidence notes)**:

| Option | Confirmed workable | Risk tradeoff |
|--------|-------------------|---------------|
| Foreign passport submitted to LexisNexis | Not confirmed — LexisNexis states "government-issued ID" without specifying U.S. issuance | Submitting foreign passport to a law enforcement data vendor exposes that passport to their systems |
| ITIN in place of SSN on LexisNexis opt-out form | Not confirmed — reported by some practitioners, no official LexisNexis documentation | Lower risk than passport; ITIN is already known to IRS and available to undocumented individuals |
| Matrícula Consular (Mexican consular ID) | Not confirmed for LexisNexis specifically | Government-issued, accepted by several U.S. banks; broker acceptance undocumented |
| Proxy opt-out via advocacy org or legal aid | No nationwide infrastructure as of April 2026 — some local DACA support orgs have piloted this | Avoids individual directly submitting credentials to commercial data vendors |
| Skip LexisNexis, focus on KBA-based brokers | Fully confirmed — Acxiom and Epsilon use KBA, no ID | Leaves LexisNexis unsuppressed; partially offset by platform countermeasures |

**The hard limit**: Thomson Reuters CLEAR has no consumer-facing opt-out mechanism at all — it is exclusively a law enforcement product. No workaround reaches it. Clearview AI's consumer opt-out blocks commercial access but explicitly does not apply to federal law enforcement. ICE retains Clearview access under a contract worth up to $9.2 million. For both CLEAR and Clearview at the federal law enforcement tier, opt-out is not a viable countermeasure — the countermeasure is social media OPSEC and physical avoidance of camera-dense public spaces (addressed in `opsec-playbook.md`).

**What this document does not cover**: IRS tax record data (now accessible to ICE under a February 2025 data-sharing agreement — see `threat-model.md` for sourcing), DMV records (state-level, not accessible through broker opt-out), and DOGE-driven cross-agency database integration (also in `threat-model.md`). These are upstream data sources that predate the commercial broker layer and cannot be addressed through consumer opt-out. The broker opt-out layer addresses commercial data products that supplement and enrich government-held records — not the government-held records themselves.

---

### 4.5 Scenario: The Skip-Tracing Contractor Layer

**The problem**: Since December 2025, ICE has outsourced location-finding to 13 private skip-tracing contractors under contracts worth up to $1.2 billion over two years. These contractors receive up to 50,000 names per month and use a mix of database queries, open-source research, and AI tools to locate individuals. The databases they query include many of the brokers in this document — but they access them as paying law enforcement customers, not as consumers. Your opt-out at the consumer tier does not prevent a contractor from querying TLOxp's law enforcement product or LexisNexis Accurint.

**What is actually achievable**:
- Opt-outs reduce data density in source databases, which degrades the quality of contractor queries. A sparse profile is harder to confirm than a dense one.
- Skip-tracing contractors work from a name list — they are trying to confirm a current address for a person they already know exists. Address instability (recent move, inconsistent address across databases) slows but does not stop this process.
- The most effective countermeasure against skip-tracing contractor access is not opt-out but address dissociation: ensuring that your current address does not appear in the commercial databases that contractors query. This means: completing Part 0 opt-outs to reduce historical address accumulation, not linking your current address to a phone number or email in new service signups, and using a P.O. box or third-party address for mail when legally permissible.
- In states with address confidentiality programs: ACP enrollment substitutes a confidential address for your real address in government records, which are one of the sources contractors use. See Section 4.6 below.

---

### 4.6 Scenario: Data Reappears After Opt-Out

**The problem**: Data brokers continuously re-ingest from public records (property databases, court records, utility connections, voter registration). A successful opt-out can be reversed within 90 days if public records are re-pulled. This is documented behavior, not a bug — it is how broker databases maintain currency.

**What is actually achievable**:
- The California DROP platform is the only mechanism providing automatic ongoing re-deletion: brokers must check DROP every 45 days and re-process deletion requests for data that has reappeared. If you are a California resident, this is why DROP is the highest-priority action — it handles the re-addition problem automatically.
- For non-California residents: Use an automated removal service (Incogni or EasyOptOuts, covered in `implementation-guide.md` Step 0.3). These services re-submit opt-outs on a 60-90 day cycle, matching the re-addition cadence.
- For Tier 3 individuals: Reduce the public records that feed re-addition. In some states, voter registration can be made confidential (designated as a participant in address confidentiality programs — California Safe at Home, Washington ACP, similar programs in 31 states). Court records containing current addresses can sometimes be redacted on petition. Property records are harder — if you own property, your name appears on the deed, and that is a public record in every U.S. state.
- Address confidentiality programs: 31 states have ACP programs that substitute a confidential mail forwarding address for your real address on government records. This is specifically designed for domestic violence survivors but is available more broadly in some states. If your state has an ACP, enrollment prevents your home address from appearing in the public records that feed re-addition cycles. Search "[your state] address confidentiality program" to find enrollment information.

---

## Part 5 — Cross-Reference: Which Tier A/B/C Brokers Are Affected by 2026 Policy

| Policy instrument | Tier A brokers affected | Tier B brokers affected | Tier C brokers affected | Net direction |
|-------------------|------------------------|------------------------|------------------------|---------------|
| SECURE Data Act (if passed as introduced) | LexisNexis: national registration required; Venntel/Gravy: already FTC-ordered | TransUnion, CoreLogic, Equifax WF: national deletion rights extend beyond California | All people-search brokers: national registration + state preemption removes California enforcement leverage | Mixed: new rights in red states, weaker enforcement nationally |
| SECURE Data Act state preemption | Clearview AI BIPA consent order (Illinois state law): potentially challenged under preemption | Samba TV: California wiretap claims potentially preempted | CPPA DROP enforcement: preempted if DELETE Act is preempted | Negative for existing protections |
| PADFAA enforcement (FTC) | Venntel/Gravy: already addressed; Babel Street: potential FTC scrutiny for foreign data sales | TransUnion, Verisk, Samba TV: may face PADFAA compliance requirements for sensitive data category sales | People-search brokers: "data broker" definition broad enough to cover foreign sales; enforcement not yet documented at this tier | Positive for indirect pressure; negative for federal law enforcement use (PADFAA doesn't restrict domestic LE access) |
| California SB 361 (effective now) | LexisNexis: must disclose government data relationships to California CPPA | CoreLogic, TransUnion, Equifax WF: must disclose if sharing with law enforcement | California-registered people-search brokers: must disclose AI use and government sharing | Positive: creates public disclosure record usable by advocates |
| California DROP (ongoing) | No direct effect on Tier A LE products | CoreLogic: California CCPA deletion covers Cotality data; DROP includes Cotality | All California-registered people-search brokers: mandatory 45-day re-deletion cycle | Positive for California residents |
| BIPA expansion (pending in TX/WA) | Clearview AI: would face expanded liability in additional states | Not directly affected | Not directly affected | Positive if enacted; uncertain timeline |

---

## Sources

- [AFSC Investigate: TransUnion](https://investigate.afsc.org/company/transunion)
- [Brennan Center: TLOxp Transactional Pricing for Law Enforcement](https://www.brennancenter.org/sites/default/files/2024-04/C1007%20TLOxp%20Transactional%20Pricing.pdf)
- [TransUnion: TLOxp Law Enforcement Product Page](https://www.transunion.com/industry/public-sector/law-enforcement)
- [Money.com: TransUnion Data Breach, July 2025](https://money.com/transunion-data-breach/)
- [USASpending.gov: LexisNexis ICE Contract (2026)](https://www.usaspending.gov/award/CONT_AWD_70B06C26F00000023_7014_GS00F178DA_4732)
- [EPIC: Coalition Call to ICE to Cancel LexisNexis Contract](https://epic.org/epic-coalition-call-for-ice-to-cancel-contract-with-lexisnexis-for-invasive-surveillance-databases/)
- [FedScoop: 80+ Groups Oppose LexisNexis ICE Contract Renewal](https://fedscoop.com/nonprofits-oppose-lexisnexis-contract-renewal/)
- [TechCrunch: LexisNexis Data Breach, May 2025](https://techcrunch.com/2025/05/28/data-broker-giant-lexisnexis-says-breach-exposed-personal-information-of-over-364000-people/)
- [Cotality (CoreLogic) Rebrand Announcement, March 2025](https://www.cotality.com/press-releases/meet-cotality)
- [GhostMyData: CoreLogic Opt-Out Guide 2026](https://ghostmydata.com/remove-from/corelogic)
- [Fast Company: Equifax Salary Data and The Work Number Database](https://www.fastcompany.com/40485634/equifax-salary-data-and-the-work-number-database)
- [Equifax: The Work Number Employee Data Freeze](https://employees.theworknumber.com/employee-data-freeze)
- [Privacy Rights Clearinghouse: Clarity Services, Inc.](https://privacyrights.org/data-brokers/clarity-services-inc)
- [CFPB: Clarity Services Consumer Reporting Companies List](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/consumer-reporting-companies/companies-list/clarity-services/)
- [CFPB: Early Warning Services Consumer Information](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/consumer-reporting-companies/companies-list/early-warning-services-llc/)
- [Law360: Samba TV Must Face Wiretap, Privacy Claims, April 2026](https://www.law360.com/classaction/articles/2468645)
- [Bloomberg Law: Acxiom Sold Data Without Consent, Virginia Suit, January 2025](https://news.bloomberglaw.com/privacy-and-data-security/acxiom-sold-millions-of-peoples-data-without-consent-suit-says)
- [State of Surveillance: Data Brokers Selling to ICE, 2025](https://stateofsurveillance.org/articles/corporate/data-brokers-ice-contracts/)
- [IAPP: SECURE Data Act Analysis](https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill)
- [Future of Privacy Forum: SECURE Data Act in State Privacy Landscape](https://fpf.org/blog/contextualizing-the-proposed-secure-data-act-in-the-state-privacy-landscape/)
- [Hunton: House Republicans Introduce SECURE Data Act](https://www.hunton.com/privacy-and-cybersecurity-law-blog/house-republicans-introduce-comprehensive-federal-privacy-bill-secure-data-act)
- [FTC: PADFAA Reminder Letters to Data Brokers, February 2026](https://www.ftc.gov/news-events/news/press-releases/2026/02/ftc-reminds-data-brokers-their-obligations-comply-padfaa)
- [FTC: PADFAA Statute Page](https://www.ftc.gov/legal-library/browse/statutes/protecting-americans-data-foreign-adversaries-act-2024-padfaa)
- [Wiley Law: FTC Warning Letters on PADFAA](https://www.wiley.law/alert-FTC-Sends-Warning-Letters-to-Data-Brokers-on-PADFA-Compliance)
- [ScanComply: California SB 361 Data Broker Law 2026](https://scancomply.com/blog/california-sb-361-data-broker-law-2026)
- [Squire Patton Boggs: 2025 State Privacy Roundup](https://www.squirepattonboggs.com/insights/publications/2025-state-privacy-roundup-key-trends-and-california-developments-to-watch-in-2026/)
- [Source Material: ICE Skip Tracing Contracts, $1.2 Billion, December 2025](https://sourcematerialblog.substack.com/p/ice-signs-deals-potentially-worth)
- [American Immigration Council: ICE Private Bounty Hunters and Skip Tracing](https://www.americanimmigrationcouncil.org/blog/ice-bounty-hunters-use-ai-track-immigrants/)
- [American Dragnet: Data-Driven Deportation (Georgetown Center on Privacy)](https://americandragnet.org/)
- [Big-Ass-Data-Broker-Opt-Out-List (GitHub, March 2026)](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List)
- [EFF Deeplinks (ongoing monitoring)](https://www.eff.org/deeplinks)
- [SmartHomePerfected: How to Disable ACR on Smart TVs (2026)](https://www.smarthomeperfected.com/how-to-disable-acr-smart-tv/)
- [Consumer Reports: How to Turn Off Smart TV Snooping Features](https://www.consumerreports.org/electronics/privacy/how-to-turn-off-smart-tv-snooping-features-a4840102036/)
- [State of Surveillance: How to Disable Smart TV ACR Surveillance (2026)](https://stateofsurveillance.org/guides/basic/disable-smart-tv-acr-surveillance-2026/)
- [Krebs on Security: How to Opt Out of Equifax Revealing Your Salary History](https://krebsonsecurity.com/2017/11/how-to-opt-out-of-equifax-revealing-your-salary-history/)
- [Oracle: Data Cloud Privacy Policy and Opt-Out](https://www.oracle.com/legal/privacy/marketing-cloud-data-cloud-privacy-policy.html)
- [POGO: ICE Inc. — Companies Profiting from Immigration Crackdown](https://www.pogo.org/investigates/ice-inc-the-top-companies-profiting-from-trumps-immigration-crackdown)
- [EFF: ICE Is Going on a Surveillance Shopping Spree, January 2026](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree)
