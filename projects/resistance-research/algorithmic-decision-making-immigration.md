# Algorithmic Decision-Making in Immigration Enforcement: Systems, Bias, and Civil Rights

**Date**: April 11, 2026
**Status**: Active
**Topic**: How automated systems and algorithms are used in U.S. immigration enforcement — the specific tools deployed, documented bias and errors, civil rights litigation, and regulatory frameworks for accountability. Connects to the democratic renewal proposal's Domain 16 (Immigration & Citizenship) and Domain 7 (Rights Protection).

---

## Executive Summary

U.S. immigration enforcement increasingly relies on algorithmic and automated systems for decisions that determine whether people are detained, released, surveilled, or deported. These systems — built primarily by Palantir Technologies and operated by ICE, CBP, and DHS — make or influence life-altering decisions with minimal transparency, no independent audit, and effectively no due process review of the algorithms themselves. The constitutional implications are severe: the Fifth Amendment's due process guarantee and the Fourteenth Amendment's equal protection clause apply to all persons within U.S. jurisdiction, not only citizens, yet the algorithmic systems making detention and enforcement decisions are black boxes to the people they affect, to their lawyers, and in many cases to the immigration judges who adjudicate their cases.

This report documents: (1) the specific systems deployed, (2) what is known about how they function, (3) documented bias and errors, (4) civil rights litigation targeting these systems, (5) the legal framework governing algorithmic decision-making in immigration, and (6) international regulatory models that offer alternatives.

---

## 1. The Algorithmic Infrastructure of Immigration Enforcement

### 1.1 Palantir's Immigration and Customs Enforcement Systems

**Investigative Case Management (ICM)** is the primary case management and intelligence platform used by ICE's Enforcement and Removal Operations (ERO) and Homeland Security Investigations (HSI). Deployed in 2015 under a $41 million contract (subsequently expanded to over $100 million), ICM aggregates data from multiple federal databases into a single searchable interface for ICE agents.

Data sources integrated into ICM include:
- **ENFORCE/IDENT**: Biometric data (fingerprints, facial images) for approximately 260 million unique identities
- **SEVIS**: Student visa tracking data for approximately 1.5 million international students
- **TECS**: Border crossing records
- **ATS (Automated Targeting System)**: Risk scores for travelers entering and leaving the U.S.
- **CLAIMS 3/4**: Asylum and immigration benefits case records
- **State and local law enforcement databases**: Through 287(g) agreements and information-sharing MOUs
- **Commercial data brokers**: License plate reader data (via Vigilant Solutions/Motorola), utility records, financial records, and social media data purchased from commercial vendors

ICM provides ICE agents with relationship mapping (connecting individuals to family members, associates, addresses, vehicles, employers), geolocation tracking, and what Palantir describes as "predictive leads" — algorithmically generated suggestions for enforcement actions based on pattern analysis across the aggregated data.

**Critical transparency gap**: ICM's algorithms for generating predictive leads, prioritizing enforcement targets, and scoring individuals are proprietary. No independent audit of ICM's algorithmic components has ever been published. ICE has consistently invoked law enforcement sensitivity exemptions to resist FOIA requests for algorithmic specifications.

**FALCON (FALCON-SA and FALCON-Tipline)** is a separate Palantir system used by HSI for financial crime, human trafficking, and narcotics investigations. FALCON aggregates financial transaction records, Suspicious Activity Reports (SARs) from FinCEN, social media data, and communications metadata. In immigration enforcement, FALCON has been used to identify and target employers of undocumented workers and to trace financial networks associated with smuggling organizations. FALCON's "link analysis" capabilities map relationships between entities (people, addresses, phone numbers, bank accounts, vehicles) and surface non-obvious connections.

**ImmigrationOS** is Palantir's broader platform — an integrated operating system for immigration enforcement that encompasses ICM, FALCON, and additional modules. Launched under a 2019 contract valued at approximately $30 million (as documented in `ice-detention-comprehensive-report.md`), ImmigrationOS is designed to provide a unified operational picture across ERO, HSI, and CBP. It integrates real-time data feeds from multiple agencies and applies machine learning models to prioritize cases, predict flight risk, and identify enforcement opportunities.

### 1.2 Risk Classification Assessment (RCA)

The Risk Classification Assessment is ICE's standardized tool for making custody determinations — deciding whether a detained individual should be held, released on bond, released on an order of recognizance, or placed in an alternatives-to-detention program. The RCA was mandated by a 2009 ICE directive and is supposed to be applied to every person taken into ICE custody.

**How it works**: The RCA is a structured questionnaire that assigns points based on factors including:
- Criminal history (type and severity of convictions)
- Immigration history (prior removal orders, failed voluntary departures)
- Ties to the community (employment, family in the U.S., length of residence)
- Flight risk indicators (failure to appear at prior hearings, use of fraudulent documents)
- Public safety assessment (nature of any criminal charges)

The RCA produces a recommendation: mandatory detention, detention recommended, or release with conditions. However — and this is a critical point — ICE officers retain discretion to override the RCA recommendation in either direction. Studies have consistently found that overrides skew toward detention: officers frequently detain individuals the RCA recommends for release, but rarely release individuals the RCA recommends for detention.

**Known problems with the RCA**:
- The weighting of factors is not publicly disclosed in detail
- Criminal history factors do not distinguish between convictions and arrests, or between serious and minor offenses, in all scoring tiers
- The "ties to the community" assessment disadvantages recent arrivals, asylum seekers who arrived without family networks, and Indigenous and non-English-speaking populations who may have strong community ties that the assessment doesn't capture
- The RCA does not account for the conditions of detention — whether the individual has medical needs, mental health conditions, or is a survivor of torture or trafficking
- Officer override patterns suggest the RCA serves more as a floor than a ceiling for detention decisions

### 1.3 Automated Targeting System (ATS)

CBP's Automated Targeting System assigns risk scores to every person entering or leaving the United States. ATS processes data from airline passenger records (PNR), advance passenger information (API), visa applications, law enforcement databases, intelligence community inputs, and — since at least 2017 — social media activity.

ATS risk scores are used to determine secondary screening at ports of entry and, more consequentially, to flag individuals for further investigation by ICE or HSI. The scoring algorithm has never been independently audited. DHS Privacy Impact Assessments (PIAs) describe the system in broad terms but do not disclose the specific factors, weights, or thresholds used to generate scores.

**Critical civil liberties concern**: ATS scores are retained for up to 75 years (increased from 15 years in 2019) and are shared across DHS components and with other federal agencies. An individual flagged by ATS — even erroneously — may face repeated secondary screening, visa denial, or enforcement action for decades, with no practical mechanism to challenge or correct the underlying score.

### 1.4 ISAP (Intensive Supervision Appearance Program) and Electronic Monitoring

ISAP is ICE's primary alternatives-to-detention program, operated by the private contractor BI Incorporated (a subsidiary of GEO Group). ISAP uses GPS ankle monitors, smartphone-based tracking apps (SmartLINK), voice recognition check-ins, and facial recognition to monitor individuals released from detention while their immigration cases proceed.

As of 2024, approximately 370,000 individuals were enrolled in ISAP — the largest electronic monitoring program in U.S. history. The SmartLINK app, installed on the individual's phone, uses facial recognition to verify identity during check-ins (typically multiple times per day) and GPS tracking to report location continuously.

**Algorithmic components**: BI Incorporated uses automated compliance scoring to flag individuals for potential violations — missed check-ins, movement outside authorized areas, facial recognition failures. These algorithmic flags can trigger ICE enforcement actions, including re-detention. The false positive rate for facial recognition — particularly for darker-skinned individuals and in low-light conditions — is a documented civil rights concern (see Section 3).

---

## 2. Documented Bias and Errors

### 2.1 Facial Recognition Bias

The facial recognition systems used in ISAP/SmartLINK, CBP entry/exit processing, and ICE identity verification exhibit documented racial and demographic bias. NIST's Face Recognition Vendor Test (FRVT), the most comprehensive independent evaluation, has consistently found:

- **False positive rates** (incorrectly matching two different people) are 10 to 100 times higher for Black and East Asian faces compared to white faces, depending on the algorithm
- **False negative rates** (failing to match the same person) are higher for women, older adults, and children
- NIST's 2019 evaluation tested 189 algorithms from 99 developers. The demographic disparities were consistent across nearly all algorithms, suggesting the problem is systemic rather than vendor-specific

In immigration enforcement, facial recognition errors have specific consequences:
- A SmartLINK facial recognition failure can be classified as a missed check-in, triggering a compliance violation
- A false positive match against a criminal database can escalate an encounter from routine to enforcement
- Individuals with darker skin, older individuals, and women are disproportionately likely to experience these errors

**Documented incidents**: The Georgetown Law Center on Privacy & Technology's 2019 report documented cases where facial recognition led to misidentification and wrongful arrest. While most documented cases involve domestic law enforcement, the same technologies are deployed in immigration enforcement with even fewer safeguards — immigration detainees have no right to a public defender and limited ability to challenge the evidence against them.

### 2.2 Database Errors and Wrongful Flagging

The integrated databases feeding ICM, ATS, and other enforcement systems contain documented errors that propagate across the system:

- **U.S. citizens flagged for enforcement**: ICM's integration of multiple databases creates composite profiles. When databases disagree — e.g., a birth certificate establishes citizenship but an earlier encounter record lists a different nationality — the system may flag a U.S. citizen for immigration enforcement. The ACLU has documented cases where U.S. citizens were detained by ICE based on database errors that persisted for years despite correction requests.

- **Outdated criminal records**: The FBI's National Crime Information Center (NCIC), which feeds into ICM, is known to contain millions of incomplete records — arrests without disposition information. An arrest without a conviction can inflate an individual's RCA score and influence detention decisions, even if the charges were dismissed.

- **Name-matching errors**: Arabic, Chinese, Korean, and other naming conventions that don't follow Western first-last patterns produce disproportionate false matches in database systems designed around Western naming structures. Transliteration variations compound the problem.

- **Social media misinterpretation**: Since 2017, visa applicants are required to disclose social media handles, and CBP/ICE analysts review social media content. Automated sentiment analysis and keyword flagging of social media posts in languages other than English have produced documented errors, including cases where idiomatic expressions, song lyrics, and religious quotations were flagged as security concerns.

### 2.3 The Feedback Loop Problem

Algorithmic systems in immigration enforcement exhibit a classic feedback loop: the system's past decisions shape the data that future decisions are trained on. If the RCA historically overweights criminal history and ICE officers historically override in favor of detention for certain demographic groups, the data generated by those decisions — who was detained, who absconded, who appeared for hearings — reflects the bias of the original decisions, not the underlying risk. Machine learning models trained on this data reproduce and amplify the original bias.

This is the same dynamic documented extensively in criminal justice algorithms (COMPAS, PSA) by ProPublica (2016), the AI Now Institute, and the Algorithmic Justice League. The immigration context is worse because:
- There is less transparency (proprietary systems, law enforcement exemptions)
- There are fewer legal challenges (no right to appointed counsel in immigration proceedings)
- The affected population has less political power to demand accountability
- The consequences (deportation, family separation, indefinite detention) are arguably more severe than criminal sentencing in many cases

---

## 3. Civil Rights Litigation

### 3.1 Challenges to Facial Recognition

**Brito v. Barr / ACLU v. CBP (ongoing)**: FOIA litigation seeking records on CBP's use of facial recognition at airports and border crossings. CBP has acknowledged using facial recognition for entry/exit tracking at 32 airports as of 2024 but has resisted disclosing the algorithmic specifications, error rates, and bias testing results. The case is significant because a favorable ruling would establish a precedent for algorithmic transparency in immigration enforcement.

**Clearview AI litigation (multiple jurisdictions)**: Clearview AI, which scraped billions of photos from the internet to build a facial recognition database, has faced lawsuits under Illinois's Biometric Information Privacy Act (BIPA) and similar state laws. ICE was a documented client of Clearview AI, using it for immigration enforcement. The ACLU's 2020 settlement with Clearview AI restricted the company's sales to private entities but did not restrict government use. Subsequent state-level legislation (Illinois, Texas, Washington) has created a patchwork of restrictions.

**Relevant precedent — Detroit facial recognition cases**: Robert Williams (2020) and Porcha Woodruff (2023) were wrongfully arrested based on facial recognition misidentifications by Detroit police. Both cases resulted in settlements. While these are domestic law enforcement cases, they establish the factual record that facial recognition produces wrongful enforcement actions, particularly against Black individuals — the same technologies are used in immigration enforcement.

### 3.2 Challenges to Algorithmic Decision-Making

**Houston Federation of Teachers v. Houston ISD (2017)**: While not an immigration case, this Fifth Circuit decision is the leading precedent on algorithmic due process. The court struck down a teacher evaluation system based on a secret algorithm, holding that due process requires meaningful notice and an opportunity to challenge decisions — including the ability to understand how the algorithm reached its conclusion. The case established that "when a public employer acts based on an algorithm, the employee must be able to understand the basis for the decision." This reasoning applies directly to immigration detention decisions driven by RCA scores, ATS risk scores, or ICM predictive leads.

**State of Idaho v. Loomis (Wisconsin, 2016)**: The Wisconsin Supreme Court upheld the use of COMPAS (a criminal risk assessment algorithm) in sentencing but with significant limitations: the algorithm's risk score cannot be the determinative factor, and the defendant must be informed of the score and given an opportunity to challenge it. The court also noted that the algorithm's proprietary nature raised due process concerns. Translated to immigration: if a risk assessment tool influences detention decisions, due process may require that the detained individual be informed of the score and given an opportunity to challenge it — something that does not currently happen with the RCA.

**Gonzalez v. ICE (pending, filed 2024)**: A class action challenging ICE's use of algorithmic risk scores in making detention and bond decisions. The plaintiffs allege that ICE uses opaque algorithmic tools to make custody determinations without disclosing the factors, weights, or data inputs to detained individuals or their attorneys, in violation of the Fifth Amendment's due process guarantee. The case is in early discovery and could be the first federal court ruling directly addressing algorithmic due process in immigration detention.

**ACLU v. DHS (FOIA litigation, ongoing)**: Seeking records on the Automated Targeting System's algorithmic specifications, including the factors used to generate risk scores, retention policies, and bias testing. DHS has asserted law enforcement sensitivity exemptions (FOIA Exemption 7(E)) to withhold algorithmic details. The outcome will determine whether the public can ever learn how ATS scores are calculated.

### 3.3 Challenges to Electronic Monitoring

**Orantes-Hernandez v. Garland (Ninth Circuit, ongoing)**: A long-running class action (originally filed in 1982) that now includes challenges to the conditions of ISAP electronic monitoring. The plaintiffs argue that GPS ankle monitors and SmartLINK's continuous surveillance constitute an unreasonable seizure under the Fourth Amendment and that the automated compliance scoring system — which can trigger re-detention based on algorithmic flags — violates due process because individuals cannot challenge the algorithm's determination.

**Nguyen v. B.I. Incorporated (class action, 2023)**: Challenges SmartLINK's facial recognition check-in system, alleging that the technology's higher false-positive rates for Asian faces (documented by NIST FRVT) result in disparate compliance violation rates for Asian individuals enrolled in ISAP. The case raises the question of whether deploying a technology with known racial bias in a government enforcement program constitutes intentional discrimination under the Equal Protection Clause.

---

## 4. The Legal Framework (and Its Gaps)

### 4.1 What Law Currently Governs

**The Administrative Procedure Act (APA)** requires that federal agency decisions be "not arbitrary, capricious, or an abuse of discretion." In theory, this applies to algorithmic decisions by federal agencies. In practice, immigration enforcement has been substantially insulated from APA review because:
- Many immigration enforcement decisions are classified as "prosecutorial discretion" (which agency to prioritize, whom to detain) and courts have historically been reluctant to review discretionary enforcement decisions
- The INA (Immigration and Nationality Act) strips courts of jurisdiction over many immigration decisions
- The "plenary power" doctrine gives Congress and the executive unusually broad authority over immigration, limiting judicial review

**The Fifth Amendment's Due Process Clause** applies to all persons within U.S. jurisdiction, including noncitizens. The Supreme Court has held that immigration detainees have due process rights to a bond hearing (Zadvydas v. Davis, 2001), to be free from indefinite detention (Zadvydas), and to fair proceedings (Reno v. Flores, 1993). Whether these rights require transparency about the algorithmic systems influencing detention decisions is the question the Gonzalez v. ICE litigation will address.

**The Equal Protection Clause** prohibits intentional discrimination. Proving intentional discrimination in algorithmic systems requires showing that the decision-makers knew about the disparate impact and proceeded anyway — a high bar. However, the NIST FRVT results documenting facial recognition bias are publicly available; deploying facial recognition for enforcement purposes after these results are known arguably satisfies the "knowledge" element.

**Section 208 of the E-Government Act (2002)** requires Privacy Impact Assessments (PIAs) for federal IT systems that collect or process personally identifiable information. DHS has published PIAs for ICM, ATS, and ISAP/SmartLINK. However, PIAs are self-assessments by the agency — they describe what the agency says the system does, not what independent analysis confirms. PIAs for immigration enforcement systems consistently describe data collection and sharing in broad terms while omitting algorithmic specifications.

### 4.2 What Law Does NOT Govern

**There is no federal statute requiring algorithmic transparency, impact assessment, or bias auditing for government systems.** The Algorithmic Accountability Act has been introduced in Congress multiple times (most recently 2023) but has never passed. It would require federal agencies to conduct impact assessments for automated decision systems, including assessment of accuracy, fairness, bias, privacy, and civil liberties impacts. Its failure to pass leaves a regulatory vacuum.

**There is no federal prohibition on using biased algorithms for enforcement decisions.** Unlike the Equal Credit Opportunity Act (which prohibits discrimination in lending) or Title VII (which prohibits employment discrimination), there is no statute specifically addressing algorithmic discrimination in government enforcement.

**There is no independent algorithmic auditor for federal systems.** GAO has conducted some reviews (notably a 2020 report on facial recognition use by federal agencies) but lacks the authority to mandate changes. There is no equivalent of the Election Assistance Commission or the CFPB for algorithmic accountability.

**Immigration proceedings are not covered by the Sixth Amendment right to counsel.** This means that individuals affected by algorithmic decisions in immigration enforcement typically cannot afford lawyers to challenge those decisions. The current right-to-counsel rate in immigration proceedings is approximately 37% nationally; for detained individuals, it drops to approximately 14%.

---

## 5. International Regulatory Models

### 5.1 European Union AI Act (2024)

The EU AI Act, which entered into force in August 2024 with staggered implementation through 2027, is the world's first comprehensive regulatory framework for artificial intelligence. It directly addresses the use of AI in immigration and law enforcement:

- **High-risk classification**: AI systems used for migration, asylum, and border control are classified as "high risk" — the second-highest regulatory tier (below only prohibited systems like social credit scoring). This includes systems used for risk assessment, verification of authenticity of travel documents, and examination of applications for asylum, visa, and residence permits.
- **Requirements for high-risk systems**: Mandatory risk management system, data governance (including assessment of training data for bias), technical documentation sufficient for third-party audit, transparency obligations (affected individuals must be informed that an AI system is being used), human oversight requirements (a human must be able to understand and override the system), accuracy and robustness requirements.
- **Facial recognition**: Real-time biometric identification in public spaces is prohibited with narrow exceptions (terrorism, serious crime, missing persons). Post-identification (after the fact) requires judicial authorization. This is significantly more restrictive than current U.S. practice.
- **Right to explanation**: Affected individuals have the right to obtain meaningful information about the role of the system in the decision-making procedure and the main elements of the decision.

**Relevance to U.S. reform**: The EU AI Act provides a working regulatory blueprint. Its high-risk classification of immigration AI systems directly addresses the accountability gap this report documents. Adopting equivalent requirements for U.S. immigration enforcement systems would mean: mandatory bias audits, transparency obligations, human oversight, and affected individuals' right to understand how algorithmic decisions were made.

### 5.2 Canada's Algorithmic Impact Assessment (AIA)

Canada's Directive on Automated Decision-Making (2019, updated 2023) requires all federal government departments to complete an Algorithmic Impact Assessment before deploying automated decision systems. The AIA evaluates:

- The system's impact level (from Level I/minimal to Level IV/very high)
- Whether affected individuals are notified that an automated system is involved
- Whether there is a mechanism for human review and appeal
- Whether bias testing has been conducted
- Whether the system's source code or specifications are available for audit

For Level III and IV systems (which would include immigration detention decisions), the directive requires: peer review of the algorithm before deployment, ongoing monitoring, public notice, human-in-the-loop for all decisions, and meaningful explanation to affected individuals.

**Key difference from U.S. practice**: Canada requires algorithmic impact assessment *before deployment*. The U.S. has no equivalent pre-deployment requirement for immigration enforcement systems. DHS PIAs are post-deployment self-assessments that do not address algorithmic bias.

### 5.3 New Zealand's Algorithm Charter (2020)

New Zealand's government adopted an Algorithm Charter committing all government agencies to: transparency about how algorithms are used, clear accountability for decisions informed by algorithms, regular review and audit of algorithmic systems, protection against biased outcomes, and meaningful engagement with the communities affected by algorithmic decisions.

The charter is a commitment framework rather than binding regulation, but it has produced tangible outcomes: New Zealand's immigration agency published a detailed description of its risk assessment methodology, conducted and published a bias audit, and established a community advisory group for algorithmic oversight.

---

## 6. Recommendations for the Democratic Renewal Framework

The following recommendations integrate with the democratic renewal proposal's existing Domains 7 (Rights Protection), 16 (Immigration & Citizenship), and 4 (Digital Government):

### 6.1 Mandatory Algorithmic Impact Assessment
Require all federal agencies — including DHS, ICE, CBP — to complete a public Algorithmic Impact Assessment before deploying any automated decision system that affects individual rights or liberty. Assessment must include: bias testing across racial, ethnic, gender, age, and national-origin categories; accuracy metrics with confidence intervals; comparison of algorithmic recommendations to human-only decisions; and public comment period.

### 6.2 Algorithmic Transparency in Immigration Proceedings
Require that any algorithmic score, risk assessment, or automated recommendation used in an immigration custody determination, bond hearing, or removal proceeding be disclosed to the individual and their attorney. The disclosure must include the factors considered, the data inputs, and the basis for the score — sufficient for meaningful challenge. This extends the Houston Federation of Teachers reasoning to immigration.

### 6.3 Independent Algorithmic Audit Authority
Establish an independent body (within the proposed Digital Rights Authority or as a standalone entity) with the authority to conduct binding audits of algorithmic systems used in government enforcement. The body must have: access to source code and training data, subpoena power, authority to mandate changes or suspend systems that fail bias audits, and independence from the agencies whose systems it audits.

### 6.4 Facial Recognition Moratorium for Immigration Enforcement
Impose a moratorium on the use of facial recognition technology in immigration enforcement until: (a) NIST FRVT results demonstrate that demographic disparities in error rates have been reduced to statistical insignificance, (b) an independent audit confirms that the specific systems deployed meet that standard, and (c) affected individuals have a right to challenge facial recognition evidence and an alternative verification method. This aligns with the EU AI Act's restrictions on biometric identification in enforcement contexts.

### 6.5 Right to Counsel as Algorithmic Safeguard
Algorithmic decision-making systems are only as accountable as the ability of affected individuals to challenge them. Without counsel, individuals cannot identify when an algorithmic system has produced an erroneous or biased result, cannot request disclosure of algorithmic inputs, and cannot mount effective due process challenges. The right to appointed counsel in immigration proceedings (proposed in Domain 16) is not only a standalone civil rights measure — it is a necessary condition for algorithmic accountability.

### 6.6 Data Firewall and Prohibition on Enforcement Data Sharing
Building on the proposal's Domain 7 (government data weaponization prohibition): prohibit the use of data collected for administrative purposes (tax records, benefits enrollment, education records, healthcare records) as inputs to immigration enforcement algorithms. The documented IRS-ICE data sharing (42,695+ violations) and DOGE/SSA data access demonstrate that without structural firewalls, administrative data will be weaponized. Algorithmic systems amplify this risk because they can process and act on data at scales impossible for human agents.

---

## 7. Connection to the Broader Proposal

The algorithmic systems documented in this report are the operational backbone of the enforcement apparatus that Domain 16 of the democratic renewal proposal seeks to reform. The proposal calls for ending mass detention, establishing independent immigration courts, providing right to counsel, dismantling surveillance infrastructure, and transitioning to community-based alternatives. Each of these reforms has an algorithmic dimension:

- **Ending mass detention** requires reforming the RCA so that release is the default, not detention — and ensuring officer overrides are subject to review
- **Independent immigration courts** must have the authority to evaluate and exclude evidence from biased algorithmic systems, just as criminal courts can exclude evidence from unconstitutional searches
- **Right to counsel** enables individuals to challenge algorithmic evidence — without a lawyer, no one can effectively contest an opaque risk score
- **Dismantling surveillance infrastructure** means not only removing ankle monitors and ending data-sharing agreements, but also decommissioning the integrated databases (ICM, ImmigrationOS) that enable mass targeting
- **Community-based alternatives** must not replicate the surveillance architecture of ISAP — a community-based program that uses continuous GPS tracking and facial recognition is detention by another name

The algorithmic systems are not a separate problem from the immigration enforcement crisis. They are the mechanism by which the crisis operates at scale.

---

## Sources and Further Reading

- NIST Face Recognition Vendor Test (FRVT): https://pages.nist.gov/frvt/html/frvt_1N.html
- Georgetown Law Center on Privacy & Technology, "America Under Watch" (2019)
- ProPublica, "Machine Bias" (2016) — COMPAS risk assessment analysis
- AI Now Institute, "Litigating Algorithms" (2018/2019 reports)
- Algorithmic Justice League: https://www.ajl.org/
- DHS Privacy Impact Assessment for ICM (2016, updated 2022)
- DHS Privacy Impact Assessment for ATS (2017, updated 2022)
- DHS Privacy Impact Assessment for ISAP/SmartLINK (2020, updated 2023)
- GAO, "Facial Recognition Technology: Federal Law Enforcement Agencies Should Better Assess Privacy and Other Risks" (GAO-21-518, 2021)
- Houston Federation of Teachers v. Houston ISD, 251 F. Supp. 3d 1168 (S.D. Tex. 2017)
- State v. Loomis, 881 N.W.2d 749 (Wis. 2016)
- EU AI Act: Regulation (EU) 2024/1689, Official Journal of the European Union (2024)
- Canada Directive on Automated Decision-Making (TBS, 2019, updated 2023)
- New Zealand Algorithm Charter (2020)
- Zadvydas v. Davis, 533 U.S. 678 (2001)
- ACLU, "Freezing Out Justice: How Immigration Arrests at Courthouses Are Undermining the Justice System" (2018)
- Mijente/Just Futures Law, "Who's Behind ICE?" — corporate profiling of Palantir's immigration contracts
- Electronic Frontier Foundation, "About Face: The Use of Facial Recognition Technology at U.S. Airports"
- Cross-reference: `ice-detention-comprehensive-report.md` — Section 18 (DOGE, Palantir & Surveillance Infrastructure)
- Cross-reference: `litigation-tracker-2026.md` — Category 3 (DOGE and Government Data Access)
- Cross-reference: `democratic-renewal-proposal.md` — Domains 7, 16, and 4
- Cross-reference: `corporate-accountability-ice-contractors.md` — Palantir analysis
