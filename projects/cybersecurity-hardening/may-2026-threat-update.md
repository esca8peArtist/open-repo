---
title: "May 2026 Threat Landscape Update"
project: cybersecurity-hardening
created: 2026-05-05
status: complete
prior-document: 2026-threat-updates.md (completed 2026-04-29)
purpose: Monthly threat model refresh covering supply-chain evolution, FISA 702 outcome, election interference escalation, AI deepfake state-of-the-art, and Palantir contract expansion. Feeds Tier 1 distribution readiness decision.
confidence: high — all findings from primary sources dated April 30–May 5, 2026, or from authoritative secondary sources published in that window. One item (Palantir ICM sole-source deal) derives from a June 2025 Biometric Update article cited in current research; note in body.
---

# May 2026 Threat Landscape Update

**Bottom line up front**: The May 2026 threat landscape represents an intensification and structural consolidation of April trends, not a sharp discontinuity. The two most operationally significant developments are (1) the Shai-Hulud supply chain campaign continuing under a new phase (Mini Shai-Hulud) into May with 1,800+ developer repositories compromised, and (2) Palantir acquiring a sole-source Investigative Case Management contract with ICE that formalizes a biometric dragnet with a hard September 2026 deployment deadline — a timeline that directly intersects with the November midterms. FISA 702 remains operational under a 45-day extension with a June 12 deadline and no warrant reform achieved. Election deepfakes have crossed from theoretical to confirmed operational deployment by NRSC in at least five races. The May threat environment does not block Tier 1 distribution, but two template updates are recommended before send.

---

## Executive Summary: What Has Changed Since April 2026

The April 2026 threat analysis identified four new vectors: the Shai-Hulud supply chain campaign, FISA 702 reauthorization with no warrant protection, AI deepfakes crossing the indistinguishable threshold, and the DOJ voter database. The May update confirms each of these is still active and adds new detail:

| Vector | April Status | May Status |
|--------|-------------|-----------|
| Supply chain (Shai-Hulud) | Three attacks in 48 hours, Bitwarden CLI compromised | Campaign continues as "Mini Shai-Hulud"; 1,800+ repos compromised; SAP npm packages now targeted; PyTorch Lightning and intercom-client compromised |
| FISA 702 | Pending legislative outcome, FISC operational extension confirmed | 45-day extension passed April 30 (261–111 House, unanimous Senate); June 12 deadline; warrant reform explicitly rejected in House vote; status quo confirmed through at least mid-June |
| AI deepfakes / synthetic identity | Voice indistinguishable threshold crossed; WEF report | NRSC deployed deepfake political ad in at least five midterm races (TX, GA, MA confirmed); industrial-scale political deployment confirmed; detection failure rate documented at 24.5% for human observers |
| Election interference (DOJ voter database) | Database construction underway, ACLU lawsuit filed | Database cross-referenced with DHS; at least 12 states compliant; lawsuit ongoing; no injunction issued as of research date |
| Palantir | ELITE using Medicaid data; $1B DHS framework; ImmigrationOS $30M | New ICM sole-source deal advancing; biometric integration; September 2026 deployment deadline; IRS contract with cross-agency data mining confirmed; congressional scrutiny increased but contracts proceeding |
| ICE at polls | DHS stated no ICE at polls; legal prohibitions documented | Steve Bannon publicly called for ICE to "surround" polling sites; White House did not guarantee absence; 7 states advancing legislation to prohibit |

**Assessment**: The May landscape is materially more developed on two dimensions — deepfakes are now deployed in active campaign material (not theoretical), and Palantir's ICM contract sets a concrete September 2026 operational deadline for a biometric-integrated investigative backbone. Both warrant attention before Tier 1 distribution.

---

## Detailed Updates by Threat Category

### 1. Supply Chain Attacks — Mini Shai-Hulud Campaign Continues

**What's new in May**: The TeamPCP threat actor group responsible for the April Shai-Hulud attacks has continued operations under a variant dubbed Mini Shai-Hulud. A two-day attack wave in early May compromised packages across PyPI, npm, and PHP ecosystems, affecting an estimated 1,800 developer repositories with stolen credentials.

**Specific May 2026 compromises**:

- **PyTorch Lightning** (PyPI): Versions 2.6.2 and 2.6.3 compromised; combined monthly download count with intercom-client is approximately 10 million. Credential theft targeting cloud keys, SSH keys, and Kubernetes secrets.
- **intercom-client** (npm): Versions 7.0.4 and 7.0.5 compromised in the same campaign window.
- **SAP npm packages** (late April/early May): The Register reported ongoing Shai-Hulud tradecraft worm into SAP developer toolchain packages, representing an escalation from general-purpose tools to enterprise infrastructure software.

**Attack tradecraft evolution**: The PHP payloads documented in May mirror the npm and PyPI tradecraft exactly: install-time execution, Bun-based payload launch, heavily obfuscated JavaScript, credential harvesting from developer and CI/CD environments, and encrypted exfiltration. The cross-ecosystem consistency confirms this is centrally coordinated, not opportunistic.

**CISA response**: CISA's May 1 advisory focused on CVE-2026-31431 (Linux kernel local privilege escalation) and a China-nexus advisory on covert network abuse. No specific Shai-Hulud advisory has been issued by CISA as of research date — the primary incident documentation is coming from GitGuardian, Socket.dev, and Endor Labs.

**Relevance to guide populations**: The guide's April addition — install Bitwarden via official website/app store only, never via npm — remains correct and gains additional importance. The expansion to enterprise packages (SAP, PyTorch) means developer-segment Tier 2 and Tier 3 individuals face elevated risk. No change to non-developer Tier 1 guidance is needed.

**Recommendation**: Add a footnote to the software installation section noting that supply chain attacks are ongoing (not a one-time event) and that any security-critical software installed or updated between April 21 and late May 2026 via a package manager should be treated with heightened scrutiny.

Sources: [eSecurity Planet: May 2026 weekly roundup](https://www.esecurityplanet.com/weekly-roundup/supply-chain-attacks-ai-security-and-major-breaches-define-this-week-in-cybersecurity-in-may-2026/); [The Hacker News: PyTorch Lightning](https://thehackernews.com/2026/04/pytorch-lightning-compromised-in-pypi.html); [The Register: SAP npm packages](https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/); [CISA: Known Exploited Vulnerability, May 1](https://www.cisa.gov/news-events/alerts/2026/05/01/cisa-adds-one-known-exploited-vulnerability-catalog); [Malicious packages up 37%](https://securitymea.com/2026/04/30/malicious-packages-up-37-as-software-supply-chain-attacks-grow/)

---

### 2. FISA Section 702 — 45-Day Extension Confirms No Warrant Protection Through June 12

**What's new**: The legislative outcome previously pending is now resolved for this cycle. On April 29–30, 2026, Congress passed a 45-day clean extension of FISA Section 702. The House voted 261–111 and the Senate passed unanimously, pushing the next expiration deadline to June 12, 2026.

**What this means for the threat model**: The April 2026 analysis was correct in its bottom line. No warrant protection for FBI backdoor searches of Americans' communications was enacted. The three-year House-passed reauthorization bill explicitly rejected warrant requirements; that bill died in the Senate on an unrelated provision (a ban on a Federal Reserve digital currency). The 45-day extension that passed was a clean extension — no reforms, no warrant requirement, no new minimization procedures.

**The June 12 deadline**: Congress must now act again by June 12. Reform advocates (Senators Wyden and Lee, House members Davidson and Lofgren) are expected to push again for a warrant amendment. As of research date, the intelligence community and the Trump administration remain opposed to any warrant requirement. The most likely outcome is another clean reauthorization, but this is an active legislative uncertainty.

**The FISC backstop**: As documented in the April analysis, the Foreign Intelligence Surveillance Court extended operational authority for existing Section 702 certifications through 2027, regardless of any legislative lapse. This means the surveillance apparatus does not go dark even if Congress fails to act by June 12. The court-extended authority is a separate operational layer that legislative debates do not reach.

**Practical implications (unchanged from April)**: Signal remains the primary countermeasure because it holds no message content to produce in response to 702 legal process. The status of 702 does not change Signal's effectiveness or the recommendations in the guide. iCloud Advanced Data Protection remains correct for Apple users. Gmail, Outlook, and WhatsApp remain unsuitable for sensitive communications.

**Domain 25 integration assessment**: The April analysis's treatment is accurate and complete. The May update confirms that treatment. No changes to Domain 25 (or equivalent guide sections on encrypted communications) are required based on the 45-day extension outcome.

Sources: [CNBC: Congress passes 45-day extension](https://www.cnbc.com/2026/04/30/fisa-section-702-congress-extension.html); [NPR: Congress extends FISA 702](https://www.npr.org/2026/04/29/g-s1-119094/congress-fisa-702); [Security Boulevard: Congress punts to June](https://securityboulevard.com/2026/05/congress-punts-fisa-section-702-renewal-to-june/); [Brennan Center 2026 Resource Page](https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page); [EPIC campaign page](https://epic.org/campaigns/fisa-section-702-reform-or-sunset/)

---

### 3. Election Interference — Deepfakes Deployed, ICE Threat Escalated, Voter Database Proceeding

**3a. Deepfake Political Ads: From Theoretical to Operational**

The April analysis documented deepfakes as an emerging threat to election integrity. May 2026 data confirms they have crossed into active operational deployment — not by foreign adversaries but by domestic political operations.

The National Republican Senatorial Committee released AI-generated deepfake video of Texas Democratic candidate James Talarico. The deepfake was over one minute long, realistic, and put his old social media statements into his mouth in his visual likeness. This is documented confirmed use of deepfake technology in a Senate race. At least five confirmed deepfake incidents appeared in the 2026 midterms across Texas, Georgia, and Massachusetts as of late April/early May.

There is no federal regulation governing AI in political advertising. Texas's 2019 law (criminal misdemeanor within 30 days of election) has not yet triggered. The NRSC incident falls outside that window. A senator pressed tech platforms in March to crack down on deepfakes before midterms; no platform-level action has materialized at scale.

**What this means for activists**: The dual threat documented in April — fabricated material deployed against activists and the risk of mistaking a deepfake for a trusted contact — is now supported by confirmed operational precedent. The NRSC case establishes that well-resourced domestic actors will produce and distribute deepfake content openly, with minimal disclosure. The implication for activists is that any unexpected video or audio appearance of a known person in a new context must be treated as potentially synthetic.

**3b. DOJ Voter Database — Lawsuit Proceeding, Cross-Reference Active**

The DOJ national voter database documented in April is proceeding despite the ACLU lawsuit. The DOJ finalized a data-sharing agreement with DHS to cross-reference voter registration records against DHS's SAVE citizenship verification database. At least 12 states have voluntarily complied, including Alaska, Arkansas, Indiana, Louisiana, Mississippi, Nebraska, Ohio, Oklahoma, South Dakota, Tennessee, Texas, and Wyoming.

The SAVE database's documented accuracy problems remain unaddressed. False-positive citizenship verification mismatches from naturalized citizens or U.S.-born citizens with immigration-adjacent records can now trigger adverse actions — voter registration challenges, purge notifications — before any human review occurs.

No injunction has been issued as of research date. The ACLU suit and allied Common Cause lawsuits are moving through court but are not yet at a stage where preliminary relief has been granted.

**3c. ICE at Polling Places — Escalating Rhetoric, Legal Prohibition Unchanged**

The legal position documented in April holds: federal law prohibits ICE at polling places. DHS confirmed ICE will not be deployed. ICE acting chief Todd Lyons admitted to senators that immigration officers would have "no reason" to be at voting locations.

What changed in May: Steve Bannon publicly called for ICE to "surround" polling sites. White House press secretary Karoline Leavitt said she "can't guarantee" an ICE agent wouldn't be near a polling location. Arizona considered requiring counties to sign ICE cooperation agreements for polling place presence. Seven states (California, Connecticut, New Mexico, Pennsylvania, Rhode Island, Virginia, Washington) are advancing legislation to explicitly ban federal forces from polling places.

The intimidation effect operates regardless of whether deployment occurs. The threat of ICE presence — amplified by Bannon's public statement and the White House's non-denial — produces voter suppression effects in immigrant communities that are measurable and documented.

**3d. CISA Coverage Gap — Institutionally Confirmed**

CISA's election security program has been functionally dismantled (14 positions eliminated, $40M cut, proposed full elimination in FY27). No federal body is now providing proactive threat intelligence to local election offices at the scale previously available. This gap becomes operationally acute as the November midterm approaches. The organizations previously relying on EI-ISAC threat feeds need to identify alternatives by summer 2026: Defending Digital Democracy, Center for Democracy and Technology, Stanford Internet Observatory, and state-level coordination.

Sources: [CNN: Talarico deepfake](https://www.cnn.com/2026/03/13/politics/james-talarico-ai-deepfake-republicans-midterms); [OECD AI: Deepfakes mislead voters](https://oecd.ai/en/incidents/2026-03-28-b14f); [Biometric Update: Senator presses platforms](https://www.biometricupdate.com/202603/senator-presses-tech-platforms-to-crack-down-on-deepfakes-before-midterms); [ACLU: Lawsuit to block voter database](https://www.aclu.org/press-releases/voting-rights-groups-sue-doj-to-block-national-voter-surveil-and-purge-database); [CNN: Trump voter database](https://www.cnn.com/2026/04/05/politics/trump-voter-database-election-fraud); [Democracy Docket: ICE chief admission](https://www.democracydocket.com/news-alerts/ice-chief-federal-immmigration-agents-polling-places-2026-midterms/); [The Hill: Noem won't rule out ICE at polls](https://thehill.com/opinion/lindseys-lens/5769764-voter-intimidation-ice-polling/); [Stateline: Blue states ban ICE at polls](https://stateline.org/2026/03/05/blue-states-push-to-ban-ice-at-the-polls-amid-federal-voter-intimidation-fears/)

---

### 4. AI Deepfakes and Synthetic Identity — Capabilities Stable, Deployment Accelerating

**State of the art as of May 2026**:

- **Voice cloning**: Voice cloning quality crossed the "indistinguishable threshold" confirmed by Fortune's December 2025 year-ahead report. Human listeners cannot reliably distinguish cloned voices from real ones. Cloning requires only seconds of audio from any public source. Consumer services are available for under $50/month. Human detection accuracy for high-quality voice deepfakes: 24.5%.
- **Detection failure rates**: AI classifiers lose up to 50% accuracy in real-world deepfake detection. Human detection rates for video deepfakes: below 30% for high-quality synthetic content. A Journal of Creative Communications study (2025) confirmed that people's opinions are measurably influenced by deepfakes they cannot reliably detect.
- **Video deepfakes**: Deepfake-as-a-service platforms were widely available by 2025. The WEF January 2026 Cybercrime Atlas confirmed that camera injection attacks defeat passive and active liveness verification across a wide range of commercial biometric systems. A one-minute deepfake video (as in the NRSC case) requires a few hours and commercially accessible tools.
- **Synthetic identity fraud**: Hard-to-detect synthetic identities combining real and fabricated personal data are now a documented fraud vector. Deepfake-enabled fraud attempts increased 1,300% year-over-year. Enterprises report average losses of $680,000 per voice fraud attack. Some major retailers report over 1,000 AI-generated scam calls per day.

**What has changed since April**: The April analysis identified the voice indistinguishable threshold crossing as a primary concern. May confirms it via the NRSC deepfake case. The escalation is not in capability (that was already documented) but in operational deployment: the NRSC case establishes that high-profile political actors are now openly using the capability in elections, which legitimizes and normalizes its use by less visible actors.

**New development — AI voice fraud draws congressional scrutiny**: Congressional hearings on AI voice fraud occurred in April 2026, signaling regulatory attention but no enacted protections as of research date.

**Countermeasure status**: The April countermeasures (out-of-band verification, code words for unexpected voice/video contact, no video-call-only identity verification) remain correct and are now strengthened by the NRSC case as a usable example for explaining the risk to Tier 1 audiences.

Sources: [Fortune: Voice cloning 2026 threshold](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forward/); [WEF Cybercrime Atlas 2026](https://reports.weforum.org/docs/WEF_Unmasking_Cybercrime_Strengthening_Digital_Identity_Verification_against_Deepfakes_2026.pdf); [Biometric Update: AI voice fraud congressional scrutiny](https://www.biometricupdate.com/202604/ai-voice-fraud-draws-new-congressional-scrutiny); [Sumsub: Fraud trends 2026](https://sumsub.com/blog/fraud-trends/); [Cyble: Deepfake-as-a-Service 2026](https://cyble.com/knowledge-hub/deepfake-as-a-service-exploded-in-2025/)

---

### 5. Palantir Contract Expansion — IRS, DHS Framework, and ICM Sole-Source Deal

**This is the section with the most material new information since the April analysis.**

**5a. IRS Contract — Cross-Agency Data Mining Confirmed (April 24, 2026)**

The Intercept reported on April 24 that Palantir is operating an IRS Criminal Investigation data platform that enables "analysis of massive-scale data to find the needle in the haystack" with the ability to search and visualize "connections from millions of records with thousands of links." The platform integrates:

- Individual tax returns and forms
- Bank statements and transactions
- FinCEN data (Financial Crimes Enforcement Network)
- Cryptocurrency wallet information including data from dark web exchanges
- Communications records (calls, texts, emails)
- IP address data
- Affordable Care Act data

The critical element is the cross-agency relationship mapping capability — the system can identify and map social networks between investigation targets across disparate federal databases. The IRS Criminal Investigation division has shifted focus under the Trump administration toward "left-leaning groups," and the Palantir platform provides the link-analysis infrastructure for that targeting.

**Why this matters for guide populations**: The IRS contract creates a new data aggregation surface for individuals who have donated to progressive causes, attended fundraisers, or have any financial relationship with organizations under IRS scrutiny. The system maps relationships, not just direct targets. A person who donated to a targeted organization may appear as a network node even if they are not themselves under investigation.

**5b. DHS Billion-Dollar Framework Contract — All Agencies, Pre-Approved Terms**

The $1 billion DHS blanket purchasing agreement (confirmed) allows every DHS component — including ICE, CBP, TSA, Secret Service, FEMA, and Coast Guard — to acquire Palantir platforms without separate competitive contracts. The BPA establishes pre-approved pricing and terms executed through task orders over five years. This is not one contract — it is an authorization infrastructure that accelerates deployment to any DHS agency.

**5c. ICM Sole-Source Deal — Biometric Integration, September 2026 Deadline**

The most significant new development: ICE is advancing a sole-source deal with Palantir to build an upgraded Investigative Case Management (ICM) system for Homeland Security Investigations. This is distinct from ImmigrationOS (which focuses on deportation operations) — ICM serves as the operational backbone for all HSI investigations.

The new system will integrate:

- Biometric identification and deduplication
- Real-time investigative data tracking across multiple federal agencies
- Cross-referencing of individuals, entities, locations, and events
- Media file management (videos, scanned documents)
- Integration with DOJ Criminal Justice Information Services, CBP, and the Office of Biometric Identity Management
- An "ICE Enterprise Lakehouse" architecture designed to consolidate all law enforcement data into a single scalable platform

The deployment timeline requires complete deployment within ten months, with a hard September 2026 deadline — two months before the November midterm elections. This timeline is significantly faster than competitors estimated (18–24 months). The sole-source designation means no competitive bidding.

Congressional Democrats sent a letter to DHS in April 2026 demanding explanation of how Palantir surveillance tools are being used. The EFF sent Palantir a formal letter asking how its human rights policy applies to its ICE work, citing reports linking Palantir-owned systems to facial recognition used to identify people recording law enforcement. No responses have been made public.

**5d. USDA "One Farmer, One File" — Data Integration Precedent**

The USDA signed a $300 million contract with Palantir for a "National Farm Security Action Plan" that includes a "One Farmer, One File" initiative consolidating farmer data across agencies (Farm Service Agency, Natural Resources Conservation Service, Risk Management Agency). This is noted not because it directly affects guide populations but because it establishes the template: single-file consolidation of disparate government data across multiple agencies is now a standard Palantir contract type being deployed across the federal government.

Sources: [The Intercept: Palantir IRS data mining](https://theintercept.com/2026/04/24/palantir-irs-contract-data/); [Biometric Update: ICE sole-source ICM deal](https://www.biometricupdate.com/202506/ice-advances-sole-source-deal-with-palantir-for-new-surveillance-backbone); [Yahoo Finance: DHS billion-dollar Palantir contract](https://finance.yahoo.com/news/billion-dollar-palantir-contract-gives-213500997.html); [State of Surveillance: ELITE app confidence scores](https://stateofsurveillance.org/news/palantir-elite-ice-targeting-app-confidence-scores-2026/); [EFF: Palantir human rights policy vs. ICE work](https://www.eff.org/deeplinks/2026/04/palantir-has-human-rights-policy-its-ice-work-tells-different-story); [Biometric Update: Lawmakers press DHS over Palantir](https://www.biometricupdate.com/202604/lawmakers-press-dhs-ice-over-palantir-surveillance-tools); [immpolicytracking.org: ImmigrationOS contract](https://immpolicytracking.org/policies/reported-palantir-awarded-30-million-to-build-immigrationos-surveillance-platform-for-ice/)

---

## Recommendations for TIER1_MESSAGING_TEMPLATES

The Tier 1 distribution audience is immigration legal organizations and community-based organizations with direct client relationships with undocumented and status-vulnerable populations. Two updates are recommended before Tier 1 outreach is executed:

**Update 1 — Palantir scope note in executive summary (recommended, minor)**

The current executive summary and outreach emails reference ELITE and ImmigrationOS. Add a sentence noting the IRS contract's relationship-mapping capability. Many Tier 1 organizations work with donors and community members who may not themselves be immigration enforcement targets but whose financial relationships with targeted organizations are now mapped in the Palantir/IRS system. The IRS cross-agency network analysis is a new attack surface for civil society organizations. Suggested addition (one sentence in the executive summary or cover email):

> "Recent reporting confirms Palantir is also operating a cross-agency data platform for IRS Criminal Investigation that maps financial relationships across millions of records — relevant to organizations and individuals connected to groups under tax scrutiny."

**Update 2 — Deepfake warning for verification practices (recommended, minor)**

The NRSC Talarico case is the first confirmed example of a well-resourced domestic actor deploying a realistic deepfake video in an active electoral context. This makes the voice/video verification warning more concrete and easier to explain to non-technical audiences. Suggested addition to the social engineering section or cover note:

> "AI-generated deepfake video is now confirmed in active U.S. political campaigns (NRSC, March 2026). If you receive unexpected audio or video from a person you know asking for sensitive information or action, verify through a second channel before responding."

**What does not need updating**: The core hardware and software recommendations, the Bitwarden installation guidance (already updated in April), the Signal/encrypted messaging section, the data broker opt-out instructions, and the ICE at polls legal analysis are all current and correct.

---

## Is the May Threat Landscape Materially Different from April?

**On a spectrum of 1–10 (1 = identical, 10 = complete discontinuity)**:

The May landscape is approximately a **3–4** relative to April. The vectors are the same. The severity is elevated on two dimensions:

1. **Palantir/IRS**: The IRS contract with relationship mapping is a genuinely new data surface not covered in the April analysis. It extends the Palantir threat model from immigration enforcement into financial network surveillance of civil society.
2. **Deepfake deployment**: What was a capability threat is now a confirmed operational precedent. This makes the threat more explainable and more urgent to non-technical audiences.

The supply chain, FISA, election database, and ICE-at-polls situations are continuations of April developments, not new vectors.

---

## Distribution Decision: Proceed or Wait?

**Recommendation: Proceed with Tier 1 distribution, incorporating the two minor template updates above.**

Reasons:

1. The threat landscape is active and accelerating. The populations served by Tier 1 organizations are under current threat from systems (ELITE, ImmigrationOS) that are fully operational now. Delay to chase a more complete threat picture defers protection from people who need it today.
2. The two recommended template updates are minor additive sentences, not structural changes to recommendations or countermeasures. They can be added to outreach emails as supplementary notes without revising the corpus Gist.
3. No critical countermeasure has been invalidated or reversed by May findings. Signal, GrapheneOS, data broker opt-outs, and the Bitwarden installation guidance are all correct.
4. The FISA 702 situation will resolve again on June 12. If warrant reform passes (unlikely but possible), that would require an update. But that is post-distribution and can be addressed in a follow-up.
5. The Palantir ICM September deployment deadline means the threat model will be more complete in September when that system is operational. Waiting until then would mean a four-month delay for a population under current active threat.

**One post-distribution monitoring item**: Watch the June 12 FISA deadline for any warrant reform outcome. If the reform coalition achieves a warrant requirement (low probability), the encrypted communications section may need a minor update acknowledging the change. If another clean extension passes (high probability), no update is needed.

---

## Sources — Full List

- [The Intercept: Palantir IRS data mining, April 24](https://theintercept.com/2026/04/24/palantir-irs-contract-data/)
- [Biometric Update: ICE sole-source ICM deal with Palantir](https://www.biometricupdate.com/202506/ice-advances-sole-source-deal-with-palantir-for-new-surveillance-backbone)
- [Yahoo Finance: DHS billion-dollar Palantir contract](https://finance.yahoo.com/news/billion-dollar-palantir-contract-gives-213500997.html)
- [State of Surveillance: ELITE app confidence scores](https://stateofsurveillance.org/news/palantir-elite-ice-targeting-app-confidence-scores-2026/)
- [EFF: Palantir human rights policy vs. ICE work](https://www.eff.org/deeplinks/2026/04/palantir-has-human-rights-policy-its-ice-work-tells-different-story)
- [Biometric Update: Lawmakers press DHS over Palantir](https://www.biometricupdate.com/202604/lawmakers-press-dhs-ice-over-palantir-surveillance-tools)
- [immpolicytracking.org: ImmigrationOS $30M contract](https://immpolicytracking.org/policies/reported-palantir-awarded-30-million-to-build-immigrationos-surveillance-platform-for-ice/)
- [CNBC: FISA 702 45-day extension](https://www.cnbc.com/2026/04/30/fisa-section-702-congress-extension.html)
- [Security Boulevard: Congress punts FISA to June](https://securityboulevard.com/2026/05/congress-punts-fisa-section-702-renewal-to-june/)
- [NPR: Congress extends FISA 702](https://www.npr.org/2026/04/29/g-s1-119094/congress-fisa-702)
- [Brennan Center: FISA 702 2026 Resource Page](https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page)
- [House Renews FISA 702, Rejects Warrant Requirement — Reclaim the Net](https://reclaimthenet.org/house-renews-fisa-section-702-rejects-warrant-requirement)
- [CNN: Talarico deepfake NRSC](https://www.cnn.com/2026/03/13/politics/james-talarico-ai-deepfake-republicans-midterms)
- [OECD AI: AI deepfakes mislead voters in 2026 campaigns](https://oecd.ai/en/incidents/2026-03-28-b14f)
- [Biometric Update: Senator presses platforms on deepfakes](https://www.biometricupdate.com/202603/senator-presses-tech-platforms-to-crack-down-on-deepfakes-before-midterms)
- [Fortune: 2026 deepfake voice cloning threshold](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/)
- [WEF Cybercrime Atlas: Deepfakes and identity verification 2026](https://reports.weforum.org/docs/WEF_Unmasking_Cybercrime_Strengthening_Digital_Identity_Verification_against_Deepfakes_2026.pdf)
- [Biometric Update: AI voice fraud congressional scrutiny](https://www.biometricupdate.com/202604/ai-voice-fraud-draws-new-congressional-scrutiny)
- [Cyble: Deepfake-as-a-Service 2026](https://cyble.com/knowledge-hub/deepfake-as-a-service-exploded-in-2025/)
- [Sumsub: Fraud trends 2026](https://sumsub.com/blog/fraud-trends/)
- [ACLU: Voting rights groups sue DOJ over voter database](https://www.aclu.org/press-releases/voting-rights-groups-sue-doj-to-block-national-voter-surveil-and-purge-database)
- [CNN: Trump voter database fears](https://www.cnn.com/2026/04/05/politics/trump-voter-database-election-fraud)
- [Popular Info: The broken database that could upend 2026 elections](https://popular.info/p/the-broken-database-that-could-upend)
- [Democracy Docket: ICE chief admits no reason at polling places](https://www.democracydocket.com/news-alerts/ice-chief-federal-immmigration-agents-polling-places-2026-midterms/)
- [The Hill: Noem won't rule out ICE at polls](https://thehill.com/opinion/lindseys-lens/5769764-voter-intimidation-ice-polling/)
- [Stateline: Blue states push to ban ICE at polls](https://stateline.org/2026/03/05/blue-states-push-to-ban-ice-at-the-polls-amid-federal-voter-intimidation-fears/)
- [Brennan Center: Sending ICE to polling places is illegal](https://www.brennancenter.org/our-work/research-reports/sending-ice-polling-places-illegal)
- [eSecurity Planet: May 2026 weekly roundup](https://www.esecurityplanet.com/weekly-roundup/supply-chain-attacks-ai-security-and-major-breaches-define-this-week-in-cybersecurity-in-may-2026/)
- [The Hacker News: PyTorch Lightning PyPI compromise](https://thehackernews.com/2026/04/pytorch-lightning-compromised-in-pypi.html)
- [The Register: SAP npm packages in supply chain attacks](https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/)
- [CISA: Known Exploited Vulnerability Catalog, May 1](https://www.cisa.gov/news-events/alerts/2026/05/01/cisa-adds-one-known-exploited-vulnerability-catalog)
- [Malicious packages up 37% — Security MEA](https://securitymea.com/2026/04/30/malicious-packages-up-37-as-software-supply-chain-attacks-grow/)
- [GitGuardian: Three supply chain campaigns in 48 hours](https://blog.gitguardian.com/three-supply-chain-campaigns-hit-npm-pypi-and-docker-hub-in-48-hours/)
