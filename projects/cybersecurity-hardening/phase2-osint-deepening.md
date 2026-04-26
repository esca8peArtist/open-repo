---
title: "Phase 2 OSINT Deepening: Broker Expansion, ID Barriers, and Court Challenges"
project: cybersecurity-hardening
created: 2026-04-26
status: complete
confidence: high — primary sources (FTC, court records, ACLU, EFF, state agency filings); medium on ID workaround operational details (limited public documentation on this population's experience)
depends_on: osint-data-broker-deepening.md, implementation-guide.md
---

# Phase 2 OSINT Deepening: Broker Expansion, ID Barriers, and Court Challenges

**Lead finding**: Three things are true simultaneously in 2026. The broker opt-out catalog that matters most for anti-surveillance purposes is narrower than common guides suggest — around 12 brokers account for the preponderant risk to high-threat individuals, not 200. The population least able to complete formal opt-outs (undocumented people, people without government-issued ID) is the population most targeted by law enforcement data products. And the most powerful legal levers right now are state-level statutory claims under BIPA and CCPA — not federal suits — but those levers have explicit carve-outs that exempt the federal agencies doing the most harm.

---

## Part A: Expanded Broker Opt-Out Catalog

### What the 200-broker lists miss: tiered impact analysis

The GitHub [Big-Ass-Data-Broker-Opt-Out-List](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List) (last updated March 2026) is the most comprehensive public resource, covering 200+ brokers with current removal URLs. The [State of Surveillance opt-out guide](https://stateofsurveillance.org/guides/advanced/data-broker-opt-out-guide/) covers 85+. These are good references, but they treat all brokers as roughly equivalent. They are not.

The operative distinction for the implementation guide's audience is: **which brokers have confirmed or probable data pipelines into law enforcement products, and which are purely consumer-facing marketing databases?** Opting out of a direct mail list is not equivalent to opting out of Accurint.

#### Tier A — Law Enforcement Direct (highest priority, already covered in implementation-guide.md Part 0)

These are confirmed government data vendors. The existing guide's Step 0.2 Priority 1-6 list covers the ones where consumer opt-out is possible. What is not adequately documented is the subset with **no consumer opt-out path**:

| Broker | Function | Opt-Out Status | Notes |
|--------|----------|---------------|-------|
| Venntel / Gravy Analytics | MAID location data | No consumer opt-out | FTC ordered to stop selling; data already sold to government. No mechanism to remove yourself from purchased datasets. |
| Babel Street (Locate X) | Social media OSINT aggregation | No consumer opt-out | FBI contract up to $27M. Data is scraped public content — countermeasure is social media OPSEC, not opt-out. |
| Thomson Reuters CLEAR | Law enforcement records platform | No public consumer opt-out | Integrated into Palantir ELITE. ID verification required; Kanary confirms it demands front/back of driver's license + selfie via ID DataWeb. |
| Clearview AI | Facial recognition faceprint database | Limited opt-out (law enforcement access continues) | ACLU settlement (2022/2025) bars private entities and Illinois state law enforcement but explicitly does not apply to federal agencies. ICE holds a contract worth up to $9.2M. |
| Palantir (ELITE/ImmigrationOS) | Deportation targeting platform | No consumer opt-out | This is not a data broker — it is an intelligence platform that aggregates feeds. The countermeasure is reducing data at the source brokers. |

**Implication for the implementation guide**: Part 0's existing Priority 1 (LexisNexis/Accurint) remains the single highest-impact individual action because Accurint is the primary feed into ELITE that has a consumer suppression mechanism. Everything else in Tier A either lacks an opt-out or requires countermeasures other than opt-out.

#### Tier B — Large Commercial Aggregators (significant footprint, opt-out available)

These feed Tier A brokers indirectly through data re-sale chains. The implementation guide covers Acxiom and Epsilon. The following are material additions not currently listed:

| Broker | Data Types | Opt-Out URL | ID Required? | Notes |
|--------|-----------|------------|-------------|-------|
| CoreLogic | Property ownership, mortgage, tenant screening | https://optout.corelogic.com/ | No (name + address sufficient) | Major real estate data aggregator used in address verification |
| Equifax Workforce Solutions (TALX) | Employment and income verification | https://thework.com/support/efx-data-security/ | Partial SSN + employer verification | Separate from Equifax credit bureau; covers employment history data |
| DataLogix / Oracle Data Cloud | Purchase behavior, loyalty card data | https://www.oracle.com/legal/privacy/marketing-cloud-data-cloud-privacy-policy.html | No | Feeds retail and marketing targeting |
| Crossix (Veeva) | Health and prescription data | Privacy form via Veeva | No | Health behavior inference from pharmacy and insurance data |
| Verisk Analytics | Insurance risk data | https://www.verisk.com/privacy/ | Name + address | Claims history, auto and property insurance records |
| PeopleSmart | People-search, address history | https://www.peoplesmart.com/optout | Email verification | Rebrands frequently; also operates as Coreplus |
| Recorded Future | Threat intelligence (aggregates news, social media, dark web) | No consumer opt-out | Enterprise-only product | Less relevant for Tier 1/2; relevant for Tier 3 targets of sophisticated actors |
| Samba TV | Smart TV viewing history, IP address | https://www.samba.tv/legal/opt-out | No | Viewing behavior sold to political and commercial campaigns |

**For the implementation guide's audience**: Adding CoreLogic and Verisk to the batch opt-out table in Step 0.2 (Priority 7-20) is the most useful expansion. Both have clean opt-out processes and are commonly used in address verification for law enforcement queries.

#### Tier C — Broker Aggregators Worth Targeting in Batch (additions to the 7-20 list)

The following have straightforward opt-out processes and are not in the current guide:

| Broker | Opt-Out URL |
|--------|-------------|
| PrivateEye | https://www.privateeye.com/static/view/optout/ |
| Clustrmaps | https://clustrmaps.com/bl/opt-out |
| Neighbor.report | https://neighbor.report/remove |
| Nuwber | https://nuwber.com/removal/link |
| USPhoneBook | https://www.usphonebook.com/opt-out |
| Spy Dialer | https://www.spydialer.com/optout.aspx |
| NumLooker | https://www.numlooker.com/removal/ |
| Clubset | https://clubset.com/profile/optout |
| LocatePeople | https://www.locatepeople.org/optout |
| PublicRecords360 | https://www.publicrecords360.com/optout.html |

Source compilation: [Big-Ass-Data-Broker-Opt-Out-List (GitHub)](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List), [Cybernews opt-out guide 2026](https://cybernews.com/privacy-tools/data-broker-opt-out/)

---

## Part B: ID-Restricted Services — Barriers and Workarounds

### The verification barrier problem

ID requirements for data broker opt-outs create a structural paradox: the brokers with the highest law enforcement access tend to impose the highest ID verification friction, and the population most targeted by law enforcement is the population least able to meet those verification requirements.

**Brokers with confirmed hard ID requirements** (source: [Kanary guide to ID-requiring brokers](https://www.kanary.com/blog/removing-info-from-brokers-who-require-id-verification)):

- **LexisNexis/Accurint**: Requests full SSN, government ID showing proof of address and date of birth. This is the single most important opt-out for immigration-risk individuals and simultaneously the hardest to complete.
- **Thomson Reuters CLEAR**: Front and back of driver's license plus selfie via ID DataWeb. No documented acceptance of foreign passports or consular IDs.
- **Clearview AI**: Government-issued photo ID plus selfie. Moot for most: the opt-out blocks commercial access, not federal law enforcement access (see Part C below).

**Brokers using Knowledge-Based Authentication (KBA) instead of ID upload**:
Acxiom and Epsilon use KBA — answering questions about past addresses, relatives, and purchase history — rather than ID submission. This is accessible without government ID but may be harder for people with limited U.S. address history.

### Strategies for people without standard government ID

The implementation guide's current troubleshooting note (Step 0.2, Troubleshooting) says "skip LexisNexis and focus on the others" if ID submission is uncomfortable. This is correct but incomplete. More specific guidance:

**1. Foreign passport as substitute for U.S. driver's license**
LexisNexis's opt-out form states it accepts "government-issued ID" without specifying U.S. issuance. A valid foreign passport is internationally recognized as government-issued photo ID. However, LexisNexis's actual processing of foreign passports is not publicly documented — there is no confirmed report of a foreign passport opt-out being honored. Risk calculation: submitting a foreign passport to LexisNexis exposes that passport's details to a law enforcement data vendor. This is a meaningful tradeoff.

**2. ITIN as partial substitute**
An Individual Taxpayer Identification Number can be used in place of an SSN for some verification purposes. The LexisNexis opt-out form requests SSN; ITIN may function as a substitute in practice. Not confirmed. The IRS issues ITINs specifically to people who do not have or cannot obtain an SSN — making this the most relevant alternative credential for undocumented individuals.

**3. Consular ID (Matrícula Consular)**
Mexican consular identification cards are government-issued documents. Several U.S. banks accept them for account opening. Whether LexisNexis accepts them for opt-out is not publicly documented. The consular ID does not require documentation of legal immigration status, making it accessible to undocumented Mexican nationals.

**4. California DROP and identity verification**
California's DROP platform accepts Login.gov credentials or a California driver's license/ID for verification. California AB 60 (2013) allows undocumented residents to obtain driver's licenses, and AB 1766 (signed 2022, effective 2023) allows Californians to obtain state ID cards without proof of authorized presence. This means undocumented California residents have a documented path to California state ID, which then provides access to DROP. This is the most reliable verified path for undocumented individuals — but only in California.

**5. Proxy opt-out via trusted third party**
Several advocacy organizations — immigrant rights orgs, legal aid clinics — have begun offering assisted data broker opt-out services where a staff member or volunteer completes opt-outs on behalf of clients. This avoids the individual directly submitting credentials to commercial data vendors. Digital Rights Foundation, Privacy Rights Clearinghouse ([privacyrights.org/data-brokers](https://privacyrights.org/data-brokers)), and some local DACA support organizations have explored this model. No nationwide infrastructure for this exists as of April 2026.

**6. The hard limit: Tier A law enforcement products**
No workaround reaches the Tier A law enforcement databases directly. Accurint's consumer suppression mechanism — even when completed successfully — explicitly states it may retain records for law enforcement queries. CLEAR has no consumer mechanism at all. For undocumented individuals, the most reliable risk-reduction strategy for Tier A exposure is not opt-out but the platform countermeasures in Parts 1-3 of the implementation guide: MAID rotation, limiting app permissions, GrapheneOS.

**Population note**: The [American Dragnet report (Georgetown Center on Privacy)](https://americandragnet.org/) documents that ICE's data infrastructure is specifically designed to build profiles from fragmented, incomplete records — meaning partial opt-out still meaningfully degrades profile confidence scoring even when full suppression is impossible.

---

## Part C: Court Challenge and Regulatory Leverage Landscape

### What has worked and why

**Clearview AI — BIPA class action (settled March 2025)**
The landmark case. ACLU v. Clearview AI (Illinois, 2020-2022 consent order; parallel class action settled 2025) produced a $51.75 million settlement in which class members received a 23% equity stake in Clearview — the first BIPA settlement paid in equity rather than cash. ([Regulatory Oversight analysis](https://www.regulatoryoversight.com/2025/04/51-75m-settlement-in-clearview-ai-biometric-privacy-litigation-illustrates-creative-resolution-for-startups-facing-parallel-litigation-and-enforcement-action/)) The consent order from 2022 permanently bars Clearview from making its faceprint database available to private entities nationwide.

The critical limitation: the settlement and consent order explicitly do not apply to federal law enforcement. ICE retains a contract worth up to $9.2 million. Illinois state and local law enforcement are barred; ICE is not. ([WBEZ reporting, November 2025](https://www.wbez.org/immigration/2025/11/02/ice-trump-facial-recognition-clearview-police-oversight))

**Legal theory that worked: Illinois BIPA (Biometric Information Privacy Act)**
BIPA is the most powerful state biometric privacy statute in the U.S. because it provides a private right of action without requiring proof of actual harm — the violation of the notice/consent requirement itself is actionable. Damages are $1,000 per negligent violation or $5,000 per intentional violation. BIPA has generated over $1.5 billion in settlements as of 2025. Other states with biometric privacy statutes: Texas (CUBI), Washington (WFBPA), but neither provides a private right of action — only the AG can enforce them.

**State AG actions and CCPA enforcement — growing teeth**
California's CCPA enforcement has produced the largest data privacy penalties in U.S. history: Disney ($2.75M, 2025), Healthline ($1.55M, July 2025), Jam City gaming ($1.4M, November 2025), Tractor Supply ($1.35M). ([IAPP analysis](https://iapp.org/news/a/california-s-attorney-general-issues-largest-ccpa-fine-to-date/))

A 10-state Consortium of Privacy Regulators has formed, enabling coordinated sweeps. This is significant because data brokers cannot jurisdiction-shop to a non-enforcement state as easily.

**CPPA enforcement of DELETE Act registration**
The California Privacy Protection Agency has begun fining unregistered data brokers: National Public Data ($46,000 after 2.9B-record breach), ROR Partners LLC ($56,600 for failure to register). These figures are small relative to harm but establish the enforcement mechanism. ([CPPA enforcement page](https://cppa.ca.gov/announcements/2026/20260108.html))

### The structural gap: federal law enforcement is mostly unreachable

The single most important limitation of the current legal landscape: federal agencies are not subject to most state privacy laws, and no federal statute currently restricts law enforcement purchase of commercially available data. The third-party doctrine (*Smith v. Maryland*, 1979; weakened but not eliminated by *Carpenter v. United States*, 2018) is the operative legal framework. *Carpenter* held that long-term cell-site location data requires a warrant; it did not address commercially purchased MAID data, purchase history, or people-search records.

**Active litigation angles**:
- Lieff Cabraser is investigating potential class actions against ICE/Palantir for illegal data profiling of protesters and U.S. citizens. ([lieffcabraser.com/ice-data/](https://www.lieffcabraser.com/ice-data/)) Case theory would likely be First Amendment (chilling of protected speech) + Fourth Amendment (warrantless location tracking). This is pre-filing investigation stage as of April 2026.
- EPIC settled its FOIA lawsuit against ICE regarding Palantir database use in 2023, extracting some documentation of capabilities. The settlement produced records rather than injunctive relief. ([EPIC settlement record](https://epic.org/epic-settles-ice-lawsuit-about-palantir-and-profiling/))
- ACLU Minnesota is litigating First Amendment claims on behalf of 30+ individuals describing encounters with immigration agents at protests. This is the most direct active litigation on protest surveillance. ([ACLU reporting, 2026](https://www.aclu.org/news/immigrants-rights/aclu-calls-on-tech-companies-to-end-their-alliance-with-ice-and-cbp))

### Emerging regulatory leverage: PADFAA

The Protecting Americans' Data from Foreign Adversaries Act (2024) is an underused lever. In February 2026, the FTC sent warning letters to 13 data brokers reminding them that selling sensitive data to foreign adversary-controlled entities violates the statute. ([FTC press release, February 2026](https://www.ftc.gov/news-events/news/press-releases/2026/02/ftc-reminds-data-brokers-their-obligations-comply-padfaa)) PADFAA covers military status data, geolocation, biometrics, health data, and financial data. Its relevance to immigration enforcement is indirect but real: brokers that sell to foreign entities and domestic law enforcement may be more vulnerable to regulatory pressure because their foreign data sales create PADFAA liability, giving advocacy organizations a regulatory hook that doesn't require proving Fourth Amendment harm.

### The SECURE Data Act — critical threat to existing protections

The SECURE Data Act (introduced April 22, 2026, HR 8413) is the most important pending legislative development for the implementation guide's audience — and not in a good way. The bill would:
- Require FTC data broker registration (a genuine improvement)
- Preempt all state privacy laws that "relate to" its provisions

The preemption provision, if enacted, would eliminate CCPA, DELETE Act / DROP, California AG enforcement authority, and the 10-state privacy consortium's ability to bring state law claims. This would eliminate the most active enforcement regime currently constraining data brokers. ([Biometric Update analysis](https://www.biometricupdate.com/202604/us-lawmakers-push-national-data-privacy-rules-amid-state-preemption-concerns), [Hunton analysis](https://www.hunton.com/privacy-and-cybersecurity-law-blog/house-republicans-introduce-comprehensive-federal-privacy-bill-secure-data-act)) The bill as introduced is pending committee; its passage is uncertain, but its existence is worth noting in the guide as an institutional risk.

### Highest-leverage strategic recommendations by actor type

**Individual with law enforcement risk**:
1. Complete Part 0 Step 0.2 Priority 1 (LexisNexis) regardless of ID friction — the friction is the point, and submitting to it provides the only available suppression on the highest-risk database.
2. Use California DROP if a California resident (AB 60/AB 1766 provides a path to state ID for undocumented California residents).
3. For those unable to complete LexisNexis opt-out: platform-level countermeasures (Parts 1-3) reduce MAID-derived location data, which is the alternative ICE procurement vector.

**Advocacy organizations**:
1. BIPA-style state legislation is the most actionable legislative target in non-Illinois states — specifically, adding a private right of action to Texas and Washington's existing biometric statutes.
2. State registration enforcement creates a public registry of brokers, giving advocates a targeting list for compliance audits.
3. PADFAA complaints to FTC about military/veteran data sales create indirect pressure on brokers who sell to both foreign entities and domestic law enforcement.

**Litigants**:
1. First Amendment + chilling effect theory is the strongest federal path for documented protesters — doesn't require *Carpenter* extension.
2. BIPA class actions remain the highest-ROI litigation vehicle for biometric data (Illinois jurisdiction or involving Illinois plaintiffs).
3. FCRA claims for employment background checks using AI scoring are an emerging theory (March 2026 class action filed — [Norton Rose Fulbright analysis](https://www.insidetechlaw.com/blog/2026/03/class-action-questions-whether-using-ai-to-score-job-applicants-violates-the-fcra)).

---

## Sources

- [Big-Ass-Data-Broker-Opt-Out-List (GitHub, March 2026)](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List)
- [State of Surveillance: Opt Out of 85+ Brokers Guide (2025)](https://stateofsurveillance.org/guides/advanced/data-broker-opt-out-guide/)
- [Kanary: Top 11 Data Brokers Requiring ID Verification](https://www.kanary.com/blog/removing-info-from-brokers-who-require-id-verification)
- [EPIC: How Data Brokers Harm Immigrants](https://epic.org/documents/how-data-brokers-harm-immigrants/)
- [American Dragnet: Data-Driven Deportation in the 21st Century (Georgetown)](https://americandragnet.org/)
- [Lieff Cabraser: ICE/Palantir Profiling Investigation (2026)](https://www.lieffcabraser.com/ice-data/)
- [ACLU: ACLU v. Clearview AI](https://www.aclu.org/cases/aclu-v-clearview-ai)
- [ACLU of Illinois: Clearview AI Settlement (2025)](https://www.aclu-il.org/big-win-settlement-ensures-clearview-ai-complies-groundbreaking-illinois-biometric-privacy-law/)
- [Regulatory Oversight: $51.75M Clearview Settlement Analysis (April 2025)](https://www.regulatoryoversight.com/2025/04/51-75m-settlement-in-clearview-ai-biometric-privacy-litigation-illustrates-creative-resolution-for-startups-facing-parallel-litigation-and-enforcement-action/)
- [WBEZ: ICE Facial Recognition App, November 2025](https://www.wbez.org/immigration/2025/11/02/ice-trump-facial-recognition-clearview-police-optimizer-oversight)
- [EPIC: EPIC v. ICE (Palantir Databases)](https://epic.org/documents/epic-v-ice-palantir-databases/)
- [EPIC: Settlement of ICE Lawsuit re Palantir](https://epic.org/epic-settles-ice-lawsuit-about-palantir-and-profiling/)
- [FTC: PADFAA Reminder Letters to Data Brokers (February 2026)](https://www.ftc.gov/news-events/news/press-releases/2026/02/ftc-reminds-data-brokers-their-obligations-comply-padfaa)
- [Biometric Update: SECURE Data Act Preemption Analysis (April 2026)](https://www.biometricupdate.com/202604/us-lawmakers-push-national-data-privacy-rules-amid-state-preemption-concerns)
- [Hunton: House Republicans Introduce SECURE Data Act](https://www.hunton.com/privacy-and-cybersecurity-law-blog/house-republicans-introduce-comprehensive-federal-privacy-bill-secure-data-act)
- [Norton Rose Fulbright: FCRA AI Scoring Class Action (March 2026)](https://www.insidetechlaw.com/blog/2026/03/class-action-questions-whether-using-ai-to-score-job-applicants-violates-the-fcra)
- [IAPP: Largest CCPA Fine to Date (Disney, 2025)](https://iapp.org/news/a/california-s-attorney-general-issues-largest-ccpa-fine-to-date/)
- [CPPA: January 2026 Enforcement Actions](https://cppa.ca.gov/announcements/2026/20260108.html)
- [Privacy Rights Clearinghouse: Data Brokers](https://privacyrights.org/data-brokers)
- [California DROP Platform: How DROP Works](https://privacy.ca.gov/drop/how-drop-works/)
- [ILRC: California IDs for All (AB 1766 FAQ)](https://www.ilrc.org/frequently-asked-questions-ca-ids-all)
- [Cybernews: Data Broker Opt-Out Guide 2026](https://cybernews.com/privacy-tools/data-broker-opt-out/)
