# Phase 3 Candidate 7: Technology Governance and Digital Rights
## Digital-Age Democratic Infrastructure — Preventing Surveillance Capture, Enabling Algorithmic Accountability

**Research completed**: April 28, 2026
**Status**: Phase 3 Exploration — Production-ready for institutional distribution
**Priority designation**: Phase 3 Expansion — Feeds Phase 1 distribution to policy influencers, law schools, tech policy institutions, civil liberties organizations
**Cross-domain connections**: Domain 36 (AI Governance / Algorithmic Accountability), Domain 35 (Post-*Loper Bright* Landscape), Domain 21 (Data Privacy), Domain 5 (Administrative Procedure Act), Domain 6 (Judicial Independence), Domain 29 (DOJ Capture and Prosecutorial Weaponization), Domain 26 (Government Accountability)

---

## Executive Summary

The United States faces a technology governance trilemma: every proposed regulatory framework for artificial intelligence, surveillance, and cryptography must simultaneously serve innovation (maintaining US competitive advantage), security (preserving national defense and law enforcement capacity), and rights (protecting constitutional guarantees against authoritarian misuse). No framework that satisfies all three has been enacted. No framework that ignores any one of the three is sustainable.

The current US posture satisfies innovation at the expense of both security and rights. The federal government has deployed AI systems across every major domestic agency — immigration enforcement, Medicare, Social Security, criminal sentencing — without a single statute specifically governing those deployments. It purchases Americans' location data from data brokers without a warrant, bypassing Fourth Amendment protections that would apply if it collected the same data directly. It operates bulk surveillance programs under authorities that three successive Congresses have failed to reform despite documented abuses. And it does so while the *Loper Bright* decision (2024) has simultaneously stripped the regulatory frameworks that executive-branch accountability relied on — leaving AI governance, surveillance oversight, and data protection dependent on executive orders that last only as long as the administration that issues them.

The failure is not primarily technical. The structural mechanisms — impact assessments, audit requirements, warrant standards, human review mandates, private rights of action — all exist in other democratic legal systems. The EU AI Act's risk-tiered classification framework, Canada's (now-failed) AIDA model's civil enforcement approach, the UK Online Safety Act's duty-of-care architecture, Illinois's Biometric Information Privacy Act's private right of action structure, and California's CPRA automated decision-making transparency rules collectively demonstrate that democracies can regulate algorithmic systems without destroying either innovation or national security. The United States has chosen not to adopt any of them at the federal level.

The north star for this domain is durable statutory architecture: rules that survive changes in administration, survive *Loper Bright* de novo judicial review, and survive the cycle of executive order issuance and revocation that has defined US AI policy since 2017. Five statutory reform pathways — an AI Governance Act, an Algorithmic Accountability Act, a Biometric Protection Act, a Cryptography Standards Act, and a Section 230 Reform Act — each address distinct vulnerability clusters within a unified constitutional framework. Together, they constitute the statutory infrastructure that makes algorithmic democracy possible.

---

## 1. Current Technology Governance Vulnerabilities

### 1.1 Unaccountable Government AI: The Three-System Crisis

The clearest evidence that the accountability gap is real and consequential comes from three operating federal AI systems: WISeR (Medicare prior authorization), ImmigrationOS / Palantir ICE (deportation targeting), and SSA's Insight/HeaRT systems (disability adjudication). Each represents a different failure mode of the same structural problem: algorithmic systems making or substantially influencing decisions that deprive individuals of life, liberty, or property, with no statutory accountability framework governing them.

**WISeR (Wasteful and Inappropriate Service Reduction Model).** Launched January 1, 2026, by CMS Administrator Mehmet Oz, WISeR deploys AI and machine learning to evaluate prior authorization requests from 6.4 million Medicare beneficiaries across six states (Arizona, New Jersey, Ohio, Oklahoma, Texas, Washington) and runs through 2031. Vendor compensation is structured as a percentage of savings from denied services — up to 20% — creating a financial incentive structure that rewards denial volume over decision accuracy. What is publicly known about WISeR could fit in a paragraph. What is unknown includes: the identity of the AI vendors, the model architecture, the training data, the accuracy rate on independent validation sets, racial or disability-status bias testing results, and the denial rate compared to prior human review. The Electronic Frontier Foundation filed a FOIA request in January 2026 and received no responsive records; it filed suit on March 25, 2026, in *EFF v. CMS*. A STAT News investigation published April 22, 2026, documented that WISeR is delaying care for seniors, with Washington State hospitals reporting weeks-long approval delays for services that previously required no prior authorization. Senator Maria Cantwell called WISeR a "denial device." No statute required CMS to disclose how the system works before deploying it. No statute required a pre-deployment bias assessment. No statute required human review of adverse determinations. The accountability gap is not accidental — it is the absence of law.

**ImmigrationOS and the Palantir Architecture.** ICE's deployment of Palantir's ImmigrationOS platform — a $30 million (growing to $287 million) contract signed April 2025 — consolidates deportation targeting, monitors "self-deportation" with near-real-time location tracking, and streamlines arrest logistics. The system pulls from passport records, Social Security files, IRS tax data, and license-plate reader databases regardless of the accuracy of those underlying databases. FALCON, a predecessor tip-synthesis tool operational since 2012, uses AI to summarize, categorize, and prioritize anonymous tips — unverified by design. ELITE, another Palantir product, identifies target-rich enforcement areas and tracks anyone with an "immigration nexus," including naturalized US citizens. Amnesty International documented in August 2025 that these systems pose specific surveillance threats to pro-Palestine student protestors and undocumented migrants, with location data sourced from commercial brokers who obtained it without individual consent. The ACLU's analysis of these systems, as of April 2026, finds: "We know little about the selection criteria and algorithms used for identifying targets, the fairness or bias of those algorithms, their transparency, or their compatibility with due process rights." No statute requires ICE to disclose its algorithmic targeting criteria. No statute mandates bias testing. No statute preserves a right to appeal a targeting score.

**SSA Disability Adjudication AI.** The Social Security Administration's deployment of AI in disability adjudication presents the quietest but systemically broadest accountability gap. The HeaRT (Hearing Recording and Transcriptions) system, fully deployed by March 2025, uses generative AI to transcribe disability hearings — introducing hallucination risk into the formal record. The Insight program uses NLP to identify "weaknesses and inconsistencies" in draft ALJ opinions, effectively providing the agency with an AI tool to flag cases where an administrative judge might decide in favor of the claimant. SSA's September 2025 AI strategy commits to "humans at the center" — but offers no statutory definition of that commitment, no audit requirement, and no enforcement mechanism. The National Academy of Social Insurance's April 2025 Phase One Report on AI and disability benefits documented risks of non-diverse training data producing bias for conditions not listed in SSA's Adult Listings, automated transcription hallucinations, and predictive models missing nuanced conditions. As of April 2026, approximately 70 million Americans receive Social Security benefits. No statute governs which of those benefit determinations are AI-influenced or requires disclosure of that fact.

### 1.2 Mass Surveillance: The Statutory Authority Crisis

The federal government's surveillance infrastructure operates under legal authorities that were designed for a pre-internet, pre-smartphone world and have not been meaningfully reformed in decades.

**Section 702 FISA.** Congress reauthorized Section 702 in April 2024 via the Reforming Intelligence and Securing America Act (RISAA), extending it two years to April 20, 2026. RISAA limited US person queries by prohibiting queries "solely designed to find and extract evidence of criminal activity" — but in August 2024, DOJ overseers discovered the FBI had been using a querying tool that allowed access to Americans' communications without adhering to RISAA's procedures. The warrant-requirement amendment — which would have required a court order before querying Section 702 databases for US persons — was narrowly defeated in the 2024 House vote. In December 2024, Judge LaShann DeArcy Hall (E.D.N.Y.) ruled that US person queries of Section 702 databases require a warrant under the Fourth Amendment. The April 2026 reauthorization deadline proved chaotic: Congress passed a 10-day stop-gap on April 17 after a coalition of Republicans joined Democrats to block a five-year clean reauthorization; Speaker Johnson released an updated "Foreign Intelligence Accountability Act" proposing a three-year reauthorization with procedural reforms falling short of a warrant requirement; the EFF and CDT called the proposal a "rubber stamp for warrantless surveillance." As of April 28, 2026, the April 30 deadline is imminent and no final resolution has been announced.

**The Data Broker Loophole.** Government agencies cannot seize location history without a court order — but they can buy it from data brokers without any judicial approval. FBI Director Kash Patel confirmed in March 2026 Senate testimony that the FBI purchases Americans' location data from commercial data brokers. DHS signed a $1 billion contract with Palantir in February 2026 for AI-powered data analytics across CBP and ICE. ICE uses Penlink's "Webloc" tool to track mobile phones; the FBI pays Babel Street up to $27 million for Locate X location product licenses. The Fourth Amendment Is Not For Sale Act, which would close this loophole, passed the House with bipartisan support in April 2024 but stalled in the Senate. The Yale Law & Policy Review analysis of this doctrine — "End-Running Warrants: Purchasing Data Under the Fourth Amendment" — finds it "constitutionally indefensible" but legally unresolved, awaiting a definitive Supreme Court ruling that has not come.

**Biometric Surveillance Expansion.** Federal law enforcement's use of facial recognition has expanded without a federal statute governing it. NIST's Face Recognition Vendor Testing program has consistently documented demographic differentials: NISTIR 8280 (2019) found higher false-positive rates for Asian, African American, and Native populations compared to white populations for US-developed algorithms. The FTC's January 2025 settlement with IntelliVision confirmed that vendors can and do make false claims about bias-free performance. At least 16 states have enacted some form of facial recognition restriction, but no federal law governs federal law enforcement use, and the December 2025 Trump executive order directed the DOJ to challenge state AI accountability laws in federal court — explicitly targeting state-level protections as obstacles to federal deployment authority.

### 1.3 The Crypto Wars: Third and Fourth Generation

The debate over encryption and law enforcement access has run in cycles since the Clipper Chip proposal of the early 1990s. The current cycle — the fourth iteration — combines the same law enforcement arguments with new vectors: end-to-end encrypted messaging (Signal, WhatsApp), encrypted device storage (Apple's Advanced Data Protection), and post-quantum cryptographic standards that will make legacy interception systems obsolete.

In early 2025, the UK government secretly ordered Apple to add a backdoor to its global iCloud encryption services. Apple refused, removing Advanced Data Protection from UK users entirely rather than comply. The incident demonstrated both that democratic governments continue to seek encryption backdoors and that technology companies — when their business model depends on security — will resist. The EARN IT Act, which would have effectively compelled scanning of encrypted messages and photos for child exploitation material, was reintroduced in the 2023-2024 session and did not advance to a full vote, primarily because opponents identified it as a backdoor mandate in disguise. The constitutional framework remains unsettled: there is no Supreme Court ruling on whether compelled decryption violates the Fifth Amendment's testimonial privilege or the First Amendment's prohibition on compelled speech. Security researchers are unanimous that key escrow systems create vulnerabilities that cannot be bounded to authorized government use — any backdoor is a backdoor for all adversaries, including foreign intelligence services.

Meanwhile, NIST finalized the first post-quantum cryptographic standards in August 2024 (ML-KEM, ML-DSA, SLH-DSA) and selected a fifth algorithm (HQC) in March 2025, responding to the "harvest now, decrypt later" threat model: adversaries collecting encrypted data now for decryption when quantum computing matures. Federal agencies face a compliance transition mandate under OMB Memorandum M-23-02 and National Security Memorandum 10. The intersection of post-quantum standards and encryption backdoor demands is acute: if NIST standards require quantum-resistant algorithms, and law enforcement demands backdoor access to those algorithms, the security community faces an engineered vulnerability in the national cryptographic infrastructure.

### 1.4 Algorithmic Harms Without Remedies

The practical consequence of the accountability gap is that people are harmed by algorithms with no meaningful path to redress. ProPublica's 2016 investigation of the COMPAS recidivism algorithm — which found Black defendants nearly twice as likely as white defendants to be incorrectly flagged as high risk while white defendants were more likely to be incorrectly flagged as low risk — remains the canonical example of algorithmic discrimination in the criminal justice system. A 2024 Springer Nature Law analysis confirmed that COMPAS bias is "mathematically inevitable" given incompatible fairness definitions. Yet COMPAS continues to be used in bail, probation, and parole decisions across multiple states, without any federal statute requiring bias disclosure, algorithmic auditing, or right of appeal.

The harm taxonomy is wider than criminal justice: denial of credit, denial of housing, adverse employment screening, wrongful deportation targeting, wrongful Medicare denial. For each, the question is identical: who is the defendant when an algorithm causes harm? The developer who sold the system? The agency or company deploying it? The data broker whose inaccurate data drove the output? The individual who relied on the AI recommendation? No federal statute answers this question. The EU AI Act's liability framework addresses it; US law does not.

---

## 2. International Precedent and Statutory Models

### 2.1 EU AI Act: Risk-Tiered Accountability

The EU AI Act entered into force August 1, 2024, with a phased implementation schedule. Prohibited practices under Article 5 (social scoring systems, biometric categorization by protected characteristics, subliminal manipulation) became enforceable February 2, 2025. Governance rules and GPAI model obligations became applicable August 2, 2025. High-risk system obligations — the core regulatory tier — become enforceable August 2, 2026 (with a delayed 2027 deadline for systems embedded in regulated products). A November 2025 European Commission "Digital Omnibus" proposal to delay some obligations up to December 2027 reflects implementation pressure, but the core statutory structure remains intact.

The Act's four-tier risk classification provides the most practically applicable international model for US statutory drafters:
- **Unacceptable risk** (prohibited): Social credit scoring, real-time remote biometric surveillance in public spaces (with limited law enforcement exceptions), subliminal manipulation, exploitation of vulnerabilities.
- **High risk** (heavily regulated, conformity assessment required): AI in biometrics, critical infrastructure, education, employment, essential services (credit, housing, insurance), law enforcement, migration, and justice administration.
- **Limited risk** (transparency obligations): Chatbots (must disclose they are AI), deepfake generators.
- **Minimal/no risk**: All other AI systems.

High-risk systems require technical documentation, EU database registration, risk assessments, human oversight protocols, and ongoing serious incident monitoring before market entry. Enforcement penalties reach €40 million or 7% of worldwide annual turnover for prohibited-practice violations — the highest penalty tier in the Act.

The Act's interaction with GDPR and the DSA creates a layered regulatory architecture: GDPR handles data privacy; the DSA handles platform content moderation and algorithmic transparency; the AI Act handles the AI systems themselves. US statutory drafters should note that this architecture separates concerns that US reform proposals have historically conflated — creating regulatory clarity while allowing specialized enforcement.

**Critical limitation for US adoption**: The EU AI Act's conformity assessment model relies on notified bodies — third-party certification entities with no direct US equivalent. A US statute would need to create equivalent audit infrastructure, likely through an FTC-certified third-party auditor scheme or a dedicated federal AI safety board.

### 2.2 Canada's AIDA: Cautionary Precedent

Canada's Artificial Intelligence and Data Act, introduced as part of Bill C-27 (the Digital Charter Implementation Act) in June 2022, died on the Order Paper when Parliament was prorogued in January 2025, before reaching a final vote. In June 2025, Minister Evan Solomon confirmed AIDA was off the table as drafted, with only parts potentially surviving in a new framework.

AIDA's failure is instructive. The proposed framework would have created an AI and Data Commissioner to monitor compliance, with enforcement by the Minister of Innovation rather than a private right of action. Critics identified this as its central weakness: AI harms flow to individuals, but AIDA's enforcement ran through government agencies, creating the same public-interest problem as GDPR enforcement in jurisdictions without adequate Data Protection Authority resources. The absence of a private right of action meant injured parties had no direct legal mechanism; enforcement depended entirely on government willingness to act.

The AIDA failure reinforces a core design principle for US statutory reform: **enforcement mechanisms must include private rights of action with standing for injured individuals, not merely agency enforcement discretion.** Agency enforcement is revocable through budget cuts, leadership changes, and hostile administrations — as the Trump administration's revocation of Biden's AI executive orders on January 20, 2025 demonstrated. Private rights of action are more durable because they do not depend on agency priority.

### 2.3 UK Online Safety Act: Duty of Care Architecture

The UK Online Safety Act entered into force March 2025, creating a statutory duty of care for online platforms requiring action against illegal content and legal-but-harmful content where children are likely to access it. Ofcom, the communications regulator, has primary enforcement authority, with penalties up to £18 million or 10% of qualifying worldwide revenue, criminal liability for executives, and service blocking orders. By October 2025 — less than a year after full implementation — Ofcom had launched five enforcement programmes and opened 21 investigations. Ofcom fined AVS Group (adult website operator) £1 million in December 2025 for lack of age verification compliance, and fined 4chan £520,000 in March 2026 for non-compliance.

The OSA's duty-of-care model differs structurally from Section 230: rather than immunizing platforms from liability, it imposes affirmative obligations to assess and mitigate risk. The EFF's August 2025 analysis found that the OSA does not, in fact, make children safer online — because the harm-mitigation obligations are designed around content removal and age verification, not around the behavioral design features (infinite scroll, engagement optimization, notification systems) that drive the documented harms to adolescent mental health. This criticism points to a design principle for US reform: duties of care must address platform architecture and algorithmic amplification, not merely content categories.

### 2.4 Illinois BIPA: State Model for Federal Floor

The Illinois Biometric Information Privacy Act (740 ILCS 14/) remains the most litigation-tested biometric privacy statute in the world. BIPA requires private entities to obtain informed consent before collecting biometric data, prohibits sale of biometric data, mandates written retention schedules tied to operational need, and requires destruction within three years of last interaction or purpose completion. Its private right of action allows statutory damages of $1,000–$5,000 per violation — a structure that has generated substantial litigation, including the 2021 Facebook settlement of $650 million in BIPA class actions.

The 2024-2025 BIPA amendments reduced some litigation exposure while preserving the core privacy architecture. The amendment clarified per-violation limits and the interaction with federal preemption carve-outs (HIPAA-covered entities, GLBA financial institutions). Illinois's BIPA continues to serve as the most credible model for federal biometric legislation because: (1) its private right of action has survived constitutional challenge; (2) its retention and deletion requirements are administratively workable; (3) its penalty structure has demonstrably changed corporate behavior in the state; and (4) no federal law preempts it — making it available as a direct template.

### 2.5 California CPRA: Automated Decision-Making Rights

California's Consumer Privacy Rights Act created the California Privacy Protection Agency (CPPA) and authorized automated decision-making technology (ADMT) regulations. In July 2025, the CPPA Board adopted regulations effective January 1, 2026, giving consumers the right to access information about and opt out of businesses' use of ADMT. The regulations require covered businesses to provide, upon request: a description of the logic used by the ADMT system, how it processed personal information to generate its output, the specific output applied to the consumer's decision, and the role of human involvement. The California Civil Rights Council's AI employment regulations, effective October 1, 2025, expanded the California Fair Employment and Housing Act's coverage to AI employment tools, opening plaintiffs to allege algorithmic discrimination under established civil rights frameworks.

California's ADMT regulatory model demonstrates three things relevant to federal design: (1) transparency requirements (explanation of logic and output) are administratively feasible; (2) opt-out rights for ADMT can coexist with business operations; and (3) the absence of a federal floor creates enforcement gaps wherever California law does not apply.

---

## 3. Five Statutory Reform Pathways

### 3.1 The AI Governance Act: Replacing Executive Order Dependency

**The problem it solves**: The federal government has no statute governing AI deployment by federal agencies. Biden's EO 14110 created accountability requirements that lasted exactly 77 days after Trump's inauguration. OMB's guidance memos are discretionary and revocable. The NIST AI RMF 1.0 (authorized by the National Artificial Intelligence Initiative Act of 2020) is explicitly voluntary. *Loper Bright* means that agency-derived accountability frameworks cannot substitute for statutory authorization regardless of their quality.

**Core statutory elements**:

1. **Pre-deployment algorithmic impact assessment (AAIA) requirement.** For any federal AI system that makes or substantially influences decisions affecting individual rights (benefits, liberty, employment, status), the deploying agency must complete a publicly available impact assessment before deployment. Assessment elements: model architecture summary; training data sources and demographic coverage; accuracy rates on validation sets disaggregated by race, gender, disability status, and national origin; false-positive and false-negative rates for adverse outcomes; description of human review mechanisms; vendor financial incentive structures; and legal authority analysis under existing enabling statute.

2. **Human review mandate.** Any adverse decision affecting individual rights that is produced by or substantially influenced by an AI system must be reviewed by a human official before the decision is final and subject to appeal. The statute must define "substantially influenced" — the mechanism for avoiding automation bias where the agency claims human review but the human invariably adopts the algorithmic recommendation. A workable definition: an AI system substantially influences a decision if its output was generated before the human review, was available to the reviewing official, and addresses the same determination that the human official made.

3. **Disclosure right.** Any individual subject to an adverse government decision that was made by or substantially influenced by an AI system has a right to written disclosure: that the system was used, the general criteria applied, the output generated, and the basis for human review. This right is enforceable in federal court through APA cause of action.

4. **Vendor accountability.** Federal procurement contracts for AI systems used in individual-rights determinations must require: public disclosure of model architecture and training data; bias testing before deployment and annually thereafter; audit rights for GAO and agency inspector general; prohibition on compensation structures tied to adverse outcome volume.

5. **Chief AI Officer accountability.** Each agency deploying AI in individual-rights determinations designates a Chief AI Officer with statutory authority to halt deployments pending impact assessment completion, and with whistleblower protections for disclosures to Congress.

6. **Congressional audit authority.** GAO and House and Senate oversight committees have statutory access to algorithmic specifications, training data summaries, and bias testing results for federal AI systems, including systems marked law-enforcement sensitive (with appropriate classification procedures for national security systems through the PCLOB model discussed in Section 6).

**Post-*Loper Bright* drafting**: The statute must authorize each element with specific language rather than broad grants of agency discretion. Language like "the agency shall conduct an algorithmic impact assessment meeting the criteria in [specific statutory provision]" is required; language like "the agency shall develop appropriate AI governance frameworks" is insufficient because courts will no longer defer to agency interpretations of "appropriate." Justice Kagan's *Loper Bright* dissent flagged this problem explicitly: complex technical domains benefit from statutory ambiguity that allows expert agencies to adapt. After *Loper Bright*, Congress must either write the technical details into the statute or delegate them to a body (like NIST) with clear technical standard-setting authority and specific criteria that courts can evaluate without deferring to agency expertise.

### 3.2 The Algorithmic Accountability Act: Private Sector AI and Harm Remedies

**The problem it solves**: The Algorithmic Accountability Act of 2023 (S.2892 / H.R.5628), sponsored by Senators Wyden and Booker and Representative Clarke, would require FTC-supervised impact assessments of automated decision systems in housing, credit, education, and employment, and authorize FTC enforcement. It died in committee in the 118th Congress. The 119th Congress has produced competing proposals: the Trump administration's "TRUMP AMERICA AI Act" seeks to preempt state AI laws while minimizing federal obligations; the GUARDRAILS ACT (introduced March 2026) would repeal the December 2025 executive order; the American Artificial Intelligence Leadership and Uniformity Act (H.R.5388) advocates a technology-neutral, sectoral approach. None of these proposals are enacted. Meanwhile, the FTC's Section 5 authority is legally present but practically contested.

**Core statutory elements for a durable Algorithmic Accountability Act**:

1. **Covered systems definition.** An "automated decision system" is any computational process that produces an output used to make or substantially influence a consequential decision. "Consequential decisions" include: credit, insurance, housing, employment, education, healthcare, criminal justice, and immigration determinations. The definition must be specific enough to survive de novo review while broad enough to cover systems that formally present as advisory but functionally determine outcomes.

2. **Impact assessment requirement.** Covered entities deploying covered systems must conduct pre-deployment impact assessments and make a summary publicly available. The assessment must address: data sources, accuracy disaggregated by protected class, false-positive and false-negative rates for adverse outcomes, human oversight mechanisms, and appeals processes.

3. **Private right of action.** Any individual adversely affected by a covered system has a private right of action for violation of the assessment, disclosure, or appeals requirements. Statutory damages: $1,000–$10,000 per violation, or actual damages if higher, plus attorney's fees. Class actions permitted. This is the design element most critical for durability: it does not depend on FTC enforcement priority.

4. **FTC authority expansion (statutory, not discretionary).** The statute grants the FTC explicit authority to promulgate rules governing automated decision systems under the standards set forth in the statute — removing reliance on Section 5's "unfair or deceptive" general language that may not survive *Loper Bright* de novo review as an authorization for algorithmic accountability regulation.

5. **Non-discrimination mandate.** Covered systems must not produce disparate adverse outcomes based on race, color, national origin, sex, disability, religion, age, genetic information, or sexual orientation. Disparate impact standard applies: if an impacted individual establishes that a covered system produces materially disproportionate adverse outcomes for a protected class, the burden shifts to the operator to demonstrate that the design is necessary for a legitimate purpose and no less discriminatory alternative achieves the same purpose. This is the Civil Rights Act disparate impact model applied to algorithmic systems.

6. **Accountability chain.** Liability runs to the entity deploying the system (which can assert indemnity against developers), not solely to developers. This addresses the accountability fragmentation problem where agencies say "a human made the decision," vendors say "the model is proprietary," and no party is actually liable.

**Post-*Loper Bright* drafting**: FTC rulemaking authority must be stated explicitly and specifically — not derived from Section 5's general grant. The Supreme Court's *West Virginia v. EPA* (2022) major questions doctrine — which the Court applied before *Loper Bright* — remains operative and requires explicit congressional authorization for regulations with major economic significance. A statute covering AI systems across the US economy is likely to trigger major questions scrutiny; the statutory grant must be specific and clear, not left to agency interpretation.

### 3.3 The Biometric Protection Act: Federal Floor for Physical Data

**The problem it solves**: The United States has no federal biometric privacy law. BIPA applies only in Illinois. Fourteen other states have enacted some form of biometric protection, but they vary in scope, enforcement mechanism, and remedies, and the December 2025 executive order directing DOJ to challenge state AI laws creates immediate preemption risk for state biometric protections. Federal law enforcement use of facial recognition is governed by no statute at all.

**Core statutory elements**:

1. **Informed consent before collection.** No entity — public or private — may collect biometric data from an individual without informed written consent. For government collection, consent is not available as a waiver of Fourth Amendment protection; collection requires either consent or legal process (warrant, court order, or statute authorizing collection for specific programmatic purpose).

2. **Retention limits.** Biometric data may not be retained longer than necessary for the specific purpose for which it was collected, and in no case longer than three years without renewal of consent or judicial authorization. Federal law enforcement biometric databases require a specific statutory authorization for retention period, subject to annual audit.

3. **Government biometric database audit.** Each federal biometric database (CODIS, NGI, CBP biometric entry/exit) is subject to annual public audit disclosing: number of records, demographic composition, accuracy rates disaggregated by race and gender, NIST FRVT compliance status, and number and outcome of false-match incidents.

4. **Prohibition on real-time mass surveillance.** Federal law enforcement may not conduct real-time facial recognition surveillance in public spaces without a warrant authorizing the specific surveillance operation, consistent with the EU AI Act's prohibition on real-time biometric surveillance as an unacceptable-risk practice. This prohibition is not absolute — it includes law enforcement exceptions modeled on the EU Act's Article 5(2) (preventing specific imminent threats, locating missing persons) — but requires individualized judicial authorization rather than programmatic deployment.

5. **Children's biometric protections.** Biometric data of persons under 18 may not be collected by private entities without parental consent, may not be sold or shared with third parties, and must be permanently deleted upon the subject's 18th birthday or upon parental request.

6. **Private right of action.** Any individual whose biometric data is collected, retained, or used in violation of the statute has a private right of action for statutory damages of $1,000–$5,000 per violation (modeled on BIPA), plus attorney's fees. Government violations are actionable under a Federal Torts Claims Act amendment; the statute waives sovereign immunity for biometric privacy violations.

7. **Federal floor preemption (not ceiling).** The statute establishes a federal floor: states may enact more protective biometric privacy requirements but may not enact less protective ones. This structure is constitutionally grounded in Congress's Supremacy Clause authority while preserving state innovation in privacy protection — explicitly rejecting the Trump executive order's preemption-as-ceiling approach.

**Disability rights integration**: NIST FRVT data documents facial recognition systems have higher error rates for darker-skinned individuals, women, and older persons. A federal Biometric Protection Act should require that covered facial recognition systems meet minimum NIST-certified accuracy standards disaggregated by protected class before federal deployment — a parallel to FDA approval standards for medical devices, and similarly justified by the liberty consequences of false matches.

### 3.4 The Cryptography Standards Act: Ending the Backdoor Cycle

**The problem it solves**: Congress has no statute prohibiting the executive branch from mandating encryption backdoors, and no statute protecting end-to-end encryption as a secure baseline for communications. The cycle of executive-branch requests for backdoor access — Clipper Chip (1993), Apple CALEA litigation (2016), EARN IT Act (2019-2024), UK's 2025 Apple order — will continue without a statutory resolution. The constitutional framework is insufficient: the Fifth Amendment's compelled decryption doctrine remains unresolved at the appellate level, and the First Amendment hook (compelled speech) has not been definitively accepted by any court. Meanwhile, NIST's post-quantum standards have created a cryptographic infrastructure transition moment that requires legislative coordination.

**Core statutory elements**:

1. **Prohibition on backdoor mandates.** No executive agency, regulatory body, or officer of the United States may require, request, or condition approval, licensing, or market access on the inclusion of any key escrow, backdoor access, or lawful intercept mechanism in any encryption system. This prohibition is statutory and applies regardless of executive order.

2. **NIST standards protection.** Cryptographic standards adopted by NIST for federal use may not require key escrow or backdoor access capabilities. The NSA's role in NIST standard-setting (relevant to the Dual EC DRBG controversy, where a backdoored random number generator was included in NIST standards before researchers identified it in 2013) must be subject to public disclosure: any NSA input into NIST cryptographic standards must be disclosed in the Federal Register before the standard is finalized.

3. **Post-quantum transition mandate.** Federal agencies must complete transition to NIST's post-quantum cryptographic standards (ML-KEM, ML-DSA, SLH-DSA) by a date certain set in the statute (no later than 2030), with annual progress reports to Congress under OMB M-23-02's existing framework — converting an executive branch initiative into a statutory mandate that survives administration change.

4. **Lawful access framework (alternative to backdoors).** The statute codifies that lawful government access to encrypted communications requires: (a) a warrant or court order; (b) served directly on the communications provider; (c) for specific identified communications, not bulk collection; and (d) compliance may be technically impossible if the provider genuinely does not hold keys (end-to-end encryption without key escrow). The "technically impossible" provision is the critical element: it confirms that providers are not required to build key-holding infrastructure they do not currently operate.

5. **International harmonization.** The Secretary of Commerce, in consultation with the NSA and CISA, must report to Congress annually on the encryption regulatory frameworks of US trading partners and adversaries, identifying conflicts between US standards and foreign backdoor mandates, and recommending adjustments to prevent conflicts of law that would require US technology companies to choose between compliance with US law and compliance with foreign surveillance demands.

**First Amendment dimension**: The strongest constitutional hook for encryption protection is the First Amendment's protection of anonymous speech, which the Supreme Court has recognized in *McIntyre v. Ohio Elections Commission* (1995) and *Watchtower Bible Tract Society v. Village of Stratton* (2002). Encryption is the technical implementation of anonymous communication in digital environments. A Cryptography Standards Act that codifies this relationship between encryption and the First Amendment would create a constitutional floor independent of the Fifth Amendment's unresolved compelled decryption doctrine.

### 3.5 Section 230 Reform: Algorithmic Amplification Accountability

**The problem it solves**: Section 230(c)(1) of the Communications Decency Act provides that "[n]o provider or user of an interactive computer service shall be treated as the publisher or speaker of any information provided by another information content provider." Courts have interpreted this immunity broadly to cover not just user-generated content but platform decisions about how to present, recommend, and amplify that content — shielding algorithmic amplification of harmful content from civil liability. The Third Circuit's *Anderson* decision established that Section 230 does not shield platforms when algorithmic recommendations constitute "expressive activity" — a principle that has spawned over 200 product liability cases where judges denied motions to dismiss based on Section 230. The resulting judicial uncertainty is worse for democracy than a clear statutory rule would be: the current trajectory risks either complete immunity restoration or complete immunity elimination, with neither outcome serving the democratic function platforms play.

**Core statutory elements for a Section 230 Reform Act**:

1. **Algorithmic amplification carve-out.** Section 230 immunity does not apply to claims arising from the platform's own algorithmic recommendation, promotion, or amplification decisions, as distinguished from the underlying user-generated content. A platform is not liable as a publisher for hosting content; it is potentially liable for the consequences of its own decision to recommend that content to users who did not seek it. This distinction follows *Gonzalez v. Google* (2023), where the Court declined to resolve the issue, and the lower court doctrine that has developed since.

2. **Transparency requirements.** Very Large Online Platforms (defined by user count, consistent with the EU DSA's threshold of 45 million EU users, adapted for US context to approximately 100 million US monthly active users) must:
   - Publish annual risk assessments identifying how their algorithmic recommendation systems contribute to disinformation, radicalization, and harms to minors;
   - Provide researcher access to data under non-disclosure agreements for independent algorithmic impact assessment;
   - Make available a non-personalized "chronological" feed option for users who opt out of algorithmic ranking;
   - Report moderation decision data in a standardized format to the FTC quarterly.

3. **Government-request carve-out.** Section 230 immunity does not apply to moderation decisions made pursuant to government requests — addressing the Supreme Court's October 2025 term's *Murthy v. Missouri* holding, which left unresolved how to identify the line between government persuasion (protected) and government coercion (First Amendment violation). A platform that removes content at government request, absent legal compulsion, is not immunized from liability for that removal under Section 230.

4. **Children's safety mandate.** Platforms that serve minors must conduct and publish algorithmic impact assessments for their recommendation systems' effects on minors, consistent with the UK Online Safety Act's duty-of-care model. This provision does not require content removal; it requires transparency and harm-mitigation planning. The COPPA 2.0 model (passed the Senate 91-3 in July 2024) is the legislative baseline.

5. **Post-*Loper Bright* drafting**: Section 230 reform is among the highest-stakes statutory drafting challenges in the current environment, because it intersects the First Amendment, the major questions doctrine, and *Loper Bright*'s statutory interpretation requirements. The statute cannot rely on FTC or FCC interpretation to fill gaps; every regulatory obligation must be stated with specificity. The EU DSA approach — which creates specific categories of obligation for specific platform sizes, with specific reporting schedules and specific public interest researcher access rights — provides the best template for achieving specificity without triggering major questions concerns, because it calibrates obligations to platform size rather than imposing uniform requirements across the industry.

---

## 4. Post-*Loper Bright* Statutory Drafting Analysis

### 4.1 The Drafting Imperative

*Loper Bright* does not just change how courts review agency interpretations; it changes what kind of Congress must act to create durable regulatory frameworks. The pre-*Loper Bright* model — broad statutory grants of authority filled by agency expertise — is unavailable for new legislation in a policy environment where the administration changes more rapidly than regulatory frameworks can adapt. Every provision of technology governance legislation that relies on an agency to define its own scope, to determine what "substantial influence" means, or to establish the technical criteria for impact assessments, is a provision that an adverse administration can redefine and a reviewing court must independently evaluate.

The practical implications for each reform pathway:

**For the AI Governance Act**: The statute must specify the elements of an algorithmic impact assessment with sufficient detail that a reviewing court can determine whether an agency has complied without deferring to the agency's own interpretation of "adequate assessment." The EU AI Act accomplishes this through Annex IV (Technical Documentation) and Annex III (High-Risk Categories) — specific annexes with enumerated requirements that serve the same function as specific statutory language in the US context. A US statute should incorporate equivalent specificity: not "the agency shall conduct an appropriate impact assessment" but "the impact assessment shall include: (1) a description of the training data, including its demographic composition disaggregated by race, gender, and national origin; (2) accuracy rates on independent validation sets disaggregated by the categories in (1); (3) false-positive and false-negative rates for adverse outcomes disaggregated by the categories in (1)..."

**For the Algorithmic Accountability Act**: The FTC's existing Section 5 authority to regulate "unfair or deceptive acts or practices" is legally present but practically insufficient for two reasons after *Loper Bright*. First, courts must independently determine whether algorithmic discrimination is an "unfair" practice under the statutory definition — and that determination is now a judicial question, not an agency question. Second, the major questions doctrine may require explicit congressional authorization before the FTC can impose economy-wide AI regulation, even under Section 5. The statute must therefore grant the FTC specific authority, state the substantive obligation directly (not as an agency power to define the obligation), and calibrate the scope of coverage to avoid triggering the major questions concern that would apply to a regulation "transforming American industry."

**For post-*Corner Post* exposure**: *Corner Post, Inc. v. Board of Governors* (2024) held that the APA statute of limitations runs from when a plaintiff is first injured — not when a rule is issued. This creates perpetual challengeability for any regulatory obligation. For technology governance statutes, this means every provision is subject to challenge from newly formed corporate entities at any point after they are covered. Statutory drafters should build in regular congressional reauthorization cycles (every five years) to create "fresh" statutory authority that forecloses arguments that the regulation rests on outdated congressional intent.

### 4.2 The Major Questions Doctrine and Technology Governance

The major questions doctrine, applied in *West Virginia v. EPA* (2022) and reinforced by *Loper Bright*'s interpretive approach, requires that Congress speak clearly when authorizing agency action with major economic or political significance. AI regulation clearly qualifies. The doctrine's application to technology governance creates a predictable litigation risk: a statute that broadly grants the FTC authority to "regulate automated decision systems affecting consumer welfare" will face a major questions challenge arguing that the breadth of that grant — covering AI systems across the US economy — requires more explicit congressional authorization.

The design response is calibrated specificity: rather than grant broad authority, the statute imposes specific obligations with limited agency discretion in their application. This design accepts some loss of flexibility in exchange for durability. The EU AI Act's four-tier risk classification model achieves calibrated specificity through statutory annexes: Congress could adopt equivalent annexes listing categories of covered systems with specificity comparable to FDA device classifications or SEC disclosure schedules. Courts have consistently upheld FDA device regulation despite its technical complexity; the model is applicable to AI system classification.

### 4.3 Constitutional Anchors for Durability

Technology governance statutes drafted for post-*Loper Bright* durability need constitutional anchors stronger than agency expertise. Three are available:

**Due process anchor.** The Fifth Amendment's Due Process Clause prohibits the federal government from depriving persons of life, liberty, or property without due process of law. Algorithmic systems that make or substantially influence government decisions about benefits (property), immigration status (liberty), and criminal justice (liberty) implicate due process directly. The statute need not characterize AI accountability as a "new" right; it can characterize it as the implementation of existing due process guarantees in the context of algorithmic decision-making. This framing puts the statute within the uncontroversial core of congressional power rather than at its edges.

**Commerce Clause anchor.** Congress's authority under the Commerce Clause to regulate commercial activity is well-established and encompasses the regulation of automated decision systems used in commercial transactions — credit, housing, employment, insurance. The private sector provisions of an Algorithmic Accountability Act are most directly grounded here. The statute should explicitly state the commerce clause basis for each provision, tracking the *Lopez*/*Morrison* requirement that Congress identify a commercial nexus.

**Spending Clause anchor.** For government AI systems deployed through federal programs (Medicare, Medicaid, SSI), Congress can impose conditions on federal funding. An AI Governance Act provision conditioning CMS program funding on pre-deployment impact assessment compliance is grounded in the Spending Clause — a congressional power that *Loper Bright* does not disturb. This is the fastest path to accountability for WISeR specifically: make compliance a condition of Medicare program participation for vendors.

---

## 5. Implementation Dependencies

### 5.1 FTC Authority Expansion: From Discretion to Mandate

The Federal Trade Commission's Section 5 authority over "unfair or deceptive acts or practices" has been the primary vehicle for FTC AI enforcement actions, including the January 2025 IntelliVision settlement (false claims about facial recognition bias), the January 2025 DoNotPay settlement (false claims about AI legal services), and the 2025 Operation AI Comply enforcement actions against deceptive AI marketing. FTC authority under the Equal Credit Opportunity Act and Fair Credit Reporting Act extends to algorithmic discrimination in credit and employment contexts.

However, post-*Loper Bright*, FTC authority depends on whether courts independently determine that algorithmic discrimination is an "unfair" practice under the statutory definition — a definition that requires substantial consumer harm, that is not outweighed by countervailing benefits, and that consumers could not reasonably have avoided. Courts applying this test de novo to AI systems have not reached uniform conclusions. An April 2026 Morgan Lewis analysis found that "AI enforcement accelerates as federal policy stalls and states step in" — meaning the FTC's current enforcement program is a holding action, not a structural solution.

The FTC's AI preemption authority is explicitly limited: a TechPolicy.Press analysis found the FTC's authority to preempt state AI laws through Section 5 enforcement or rulemaking to be minimal without specific statutory authorization. The December 2025 executive order directing DOJ to challenge state AI laws operates through a different channel than FTC preemption — it uses the litigation arm rather than the regulatory arm — but it creates the same effect: federal action displacing state protections without federal protections replacing them.

The statutory solution: grant the FTC explicit authority to promulgate algorithmic accountability rules under a specific statutory mandate, with enforcement authority including civil penalties, injunctive relief, and authority to seek consumer restitution. This converts FTC authority from a general-power interpretation question into a specific statutory mandate that *Loper Bright* cannot disturb.

### 5.2 Congressional Oversight Capacity: The Technical Expertise Gap

Congressional oversight of AI systems requires technical expertise that Congress currently lacks. The Brennan Center's analysis of the Privacy and Civil Liberties Oversight Board as an AI oversight model found that PCLOB — the most relevant existing oversight body for national security AI — operates with a 2023 budget of $12.3 million and 25 staff members. The board provides a workable access model: members and staff have access to classified agency documents and personnel, including classified AI systems, allowing oversight without public disclosure of sensitive national security information. The PCLOB model, adapted for legislative branch use, could provide a template for a Joint Congressional AI Oversight Committee with: (1) security clearances for staff; (2) access to classified AI systems through PCLOB-equivalent procedures; (3) technical staff with computer science and machine learning credentials; (4) mandatory agency cooperation requirements backed by statutory contempt authority.

The GAO's AI audit capacity also requires expansion. GAO's April 2026 report (GAO-26-107859) found agencies "not yet systematically collecting lessons learned from AI acquisitions." GAO conducts AI-related audits but lacks specialized algorithmic auditing capacity — the technical skills needed to evaluate model architecture, training data bias, and validation methodology. A statutory AI Governance Act should direct GAO to establish an AI audit unit with staffing and technical capabilities equivalent to GAO's existing financial audit function, with mandatory agency cooperation and access to algorithmic specifications under appropriate security protocols.

### 5.3 Judicial Technical Expertise

Federal courts face a structural deficit in AI cases: Article III judges are generalists without training in machine learning, algorithmic auditing, or statistical analysis of disparate impact in AI systems. This creates two risks. First, technically complex AI accountability cases are resolved on legally correct but technically uninformed grounds — judges may correctly apply the law to factual records that are technically incomplete because neither party presented the machine learning analysis necessary to evaluate algorithmic bias. Second, the absence of technical expertise creates systematic bias toward algorithmic system defendants: opacity is the default, and courts cannot compel transparency for evidence they cannot evaluate.

Design responses: (1) FRCP amendment to establish technical masters in AI cases — court-appointed experts with machine learning credentials who can evaluate algorithmic impact claims independently; (2) FJC (Federal Judicial Center) AI training program for district court and appellate judges, analogous to FJC's existing science education programs; (3) legislative standing for NIST to submit amicus briefs in federal cases involving AI systems where NIST has relevant technical standards — converting NIST's voluntary framework into a judicially accessible knowledge source.

---

## 6. Integration with Other Democratic Recovery Mechanisms

### 6.1 Judicial Independence as AI Oversight Prerequisite

Domain 6's analysis of judicial independence is a prerequisite for technology governance: the federal judiciary is the ultimate enforcement mechanism for every statutory provision in this framework. *Loper Bright*'s de novo review requirement makes courts the primary interpreter of AI governance statutes — courts that face structural pressures toward deference to government positions (qualified immunity doctrine in Fourth Amendment surveillance cases, state secrets doctrine in national security AI cases, executive deference in immigration enforcement). The expansion of executive control over federal courts through appointments and potentially through the pending *Trump v. Slaughter* Humphrey's Executor challenge creates a technology governance risk that is independent of the quality of the statute: even perfectly drafted AI accountability legislation cannot function if the courts reviewing it are structurally captured.

The connection is bidirectional: AI governance also threatens judicial independence directly. The December 2025 executive order directing DOJ to challenge state AI laws created an AI Litigation Task Force — a specialized DOJ unit with explicit mission to override state-level democratic choices about technology regulation. If that litigation task force successfully preempts state AI laws, it removes the most active layer of AI accountability currently operating in the United States, consolidating authority in a federal executive branch that has no statutory obligation to replace the protections it eliminates.

### 6.2 Surveillance Accountability and Voting Security

Domain 1's analysis of voting rights and election security connects directly to surveillance accountability: location data, social media activity, and financial transaction data can be and has been used to build political profiles of voters, donors, and activists. The government's purchase of location data from data brokers without a warrant — documented for ICE, FBI, IRS, and Secret Service — is also purchase of data about political activity, association, and belief. The First Amendment's protection of political association (*NAACP v. Alabama*, 1958) extends to the digital equivalent of membership lists; the absence of a warrant requirement for government purchase of association-revealing location data creates a direct mechanism for executive surveillance of political opposition. Section 702's bulk collection authority compounds this: queries of 702 databases using US person search terms can surface communications between political activists and foreign nationals — a documented basis for FBI investigations of domestic dissent. The Fourth Amendment Is Not For Sale Act, which closes the data broker warrant loophole, is both a privacy statute and an election security statute.

### 6.3 Algorithmic Accountability and Prosecutorial Non-Weaponization

Domain 29's analysis of DOJ capture and prosecutorial weaponization intersects with AI governance in COMPAS and predictive policing. Pretrial risk assessment tools that predict recidivism are used in bail, detention, and sentencing decisions across the federal criminal justice system and in most states. The ProPublica COMPAS analysis documented that these systems produce racially disparate outcomes; subsequent research confirmed that bias is mathematically inevitable given incompatible fairness criteria. When DOJ is captured by an administration willing to weaponize prosecutorial authority, AI systems that produce racially disparate targeting recommendations amplify rather than constrain the weaponization. An Algorithmic Accountability Act that covers law enforcement risk assessment tools — requiring bias disclosure, disparate impact analysis, and private right of action for impacted defendants — closes a structural vulnerability in the broader prosecutorial accountability framework.

### 6.4 Fiscal Architecture and AI Procurement

Domain 34 and Phase 3 Candidate 5's analysis of congressional power of the purse connects directly: federal AI systems are procured through appropriations, and appropriations oversight is the most immediate form of AI accountability available to Congress. The WISeR vendor compensation structure — where vendors earn a percentage of Medicare denial savings — is a product of procurement contract language, not statute. An AI Governance Act provision requiring transparency in AI vendor compensation structures (prohibiting percentage-of-denial compensation) could be accomplished through appropriations riders in the short term, while substantive reform proceeds through the legislative process. Appropriations-based AI governance is a legitimate near-term tool pending substantive statutory reform.

---

## 7. Implementation Roadmap and Political Feasibility Assessment

### 7.1 Realistic Short-Term Opportunities (119th Congress, 2025-2026)

The 119th Congress is unlikely to pass comprehensive AI governance legislation. The competing legislative proposals — TRUMP AMERICA AI Act, GUARDRAILS ACT, American AI Leadership and Uniformity Act — reflect a fundamental disagreement about whether the federal role is to preempt state AI laws (Republican consensus) or to establish federal floors that complement state protections (Democratic consensus). This disagreement is not resolvable by the current Congress.

However, bipartisan opportunities exist in discrete areas:

**Children's safety provisions**: COPPA 2.0 passed the Senate 91-3 in July 2024 and received House committee approval before the session ended. The bipartisan consensus around children's digital privacy is the most immediately available legislative vehicle. A children's biometric protection provision, children's algorithmic profiling ban, and ADMT opt-out for minors can be attached to COPPA 2.0 reintroduction.

**Post-quantum cryptography mandate**: The transition to NIST's post-quantum standards has bipartisan national security support and no civil liberties opponents. Converting OMB M-23-02's executive branch transition mandate into a statutory requirement is achievable. The Quantum Computing Cybersecurity Preparedness Act of 2022 already provides a legislative precedent; an update mandating transition by 2030 with annual progress reports is a clear legislative path.

**Section 702 warrant reform**: The April 2026 reauthorization chaos demonstrates that the current authority framework is politically unstable. A three-year reauthorization with a warrant requirement for US person queries — the December 2024 Eastern District of New York ruling's constitutional requirement — may be achievable in the current negotiation if privacy-focused members from both parties maintain coalition cohesion.

**Fourth Amendment Is Not For Sale Act**: Passed the House with bipartisan support in 2024; Senate floor vote is the remaining obstacle. This is the most achievable near-term surveillance reform.

### 7.2 Medium-Term Framework (Post-2026 Midterms)

The 2026 midterms, analyzed in Domain 37, will determine whether comprehensive statutory reform is achievable in the 120th Congress. If Democrats gain House majority or significant Senate seats, the legislative window for an AI Governance Act opens. If Republican control is maintained, state-level implementation of California/Illinois models and litigation-based accountability through existing civil rights statutes represent the most durable path.

In either scenario, the litigation record being built in 2025-2026 — *EFF v. CMS* on WISeR, ACLU Palantir analyses, Fourth Amendment data broker cases — creates the factual record that statutory drafters and future administrations will need. The legal vulnerability analysis conducted for this document (AI systems without statutory authority at risk under *Loper Bright* and APA arbitrary-and-capricious review) is also the litigation theory that civil liberties organizations can bring to court without waiting for Congress. The two-track approach — statutory reform preparation and immediate litigation — is the appropriate strategy for the period until a reform-capable Congress is seated.

---

## 8. Bibliography

**Federal AI Governance and Accountability**

1. GAO, "Artificial Intelligence: Agencies Need to Improve Acquisition Practices and Lesson-Learning" (GAO-26-107859, April 2026). https://www.gao.gov
2. GAO, "Artificial Intelligence: Use by Selected Agencies and Efforts to Address Related Challenges" (GAO-25-107933, 2025). https://www.gao.gov
3. Electronic Frontier Foundation, "*EFF v. CMS*: Lawsuit for WISeR AI Documentation" (March 25, 2026). https://www.eff.org
4. STAT News, "Federal test of AI prior authorization is delaying care for seniors" (April 22, 2026). https://www.statnews.com/2026/04/22/cms-wiser-program-delays-care-washington-state-hospitals-senator-says/
5. National Academy of Social Insurance, "AI and Disability Benefits: Phase One Report" (April 2025). https://www.nasi.org
6. OMB, "Memoranda M-25-21 and M-25-22: Revised Federal AI Governance Framework" (April 2025). https://www.whitehouse.gov/omb
7. OMB, "Federal Agency AI Use Case Inventory 2025" (GitHub: ombegov/2025-Federal-Agency-AI-Use-Case-Inventory). https://github.com/ombegov
8. National AI Initiative Act of 2020, P.L. 116-283. https://www.congress.gov
9. NIST, "Artificial Intelligence Risk Management Framework (AI RMF 1.0)" (January 2023). https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
10. Sidley Austin, "Unpacking the December 11, 2025 Executive Order: Ensuring a National Policy Framework for AI" (December 2025). https://www.sidley.com

**Palantir, ICE, and Algorithmic Enforcement**

11. ACLU, "All the Ways Palantir is Assisting Trump's Abusive Removal Campaign" (April 2026). https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup
12. American Immigration Council, "ICE to Use ImmigrationOS by Palantir" (2025). https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/
13. American Immigration Council, "Mission Creep: AI Surveillance at DHS Crosses Dangerous Line Into Tracking Americans." https://www.americanimmigrationcouncil.org/blog/ice-ai-surveillance-tracking-americans/
14. Amnesty International, "Tech Made by Palantir and Babel Street Pose Surveillance Threats to Protestors and Migrants" (August 2025). https://www.amnesty.org/en/latest/news/2025/08/usa-global-tech-made-by-palantir-and-babel-street-pose-surveillance-threats/
15. State of Surveillance, "Palantir $287M 2025: ICE Immigration Tracking Machine." https://stateofsurveillance.org/articles/surveillance/palantir-immigration-machine-287-million/

**Surveillance Law and Reform**

16. Brennan Center for Justice, "Section 702 of the Foreign Intelligence Surveillance Act." https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act
17. Congressional Research Service, "FISA Section 702 and the 2024 Reforming Intelligence and Securing America Act" (CRS R48592). https://www.congress.gov/crs-product/R48592
18. EFF, "Congress Must Reject New Insufficient 702 Reauthorization Bill" (April 2026). https://www.eff.org/deeplinks/2026/04/congress-must-reject-new-insufficient-702-reauthorization-bill
19. Al Jazeera, "US Congress extends controversial surveillance power under FISA for 10 days" (April 17, 2026). https://www.aljazeera.com/news/2026/4/17/us-congress-temporarily-extends-controversial-surveillance-power-under-fisa
20. CNBC, "FISA Section 702: Congress Passes Short-Term Extension" (April 17, 2026). https://www.cnbc.com/2026/04/17/section-702-fisa-congress-surveillance.html
21. Brennan Center, "Congress Must Close Data Broker Loophole." https://www.brennancenter.org/our-work/research-reports/congress-must-close-data-broker-loophole-prohibiting-government-0
22. NPR, "Your Data Is Everywhere. The Government Is Buying It Without a Warrant" (March 25, 2026). https://www.npr.org/2026/03/25/nx-s1-5752369/ice-surveillance-data-brokers-congress-anthropic
23. Yale Law & Policy Review, "End-Running Warrants: Purchasing Data Under the Fourth Amendment and the State Action Problem." https://yalelawandpolicy.org/end-running-warrants-purchasing-data-under-fourth-amendment-and-state-action-problem
24. EPIC, "FISA Section 702: Reform or Sunset." https://epic.org/campaigns/fisa-section-702-reform-or-sunset/

**Facial Recognition and Biometric Standards**

25. NIST, "NISTIR 8280: Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects" (2019). https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8280.pdf
26. NIST, Face Recognition Technology Evaluation (FRTE) 1:1 Verification. https://pages.nist.gov/frvt/html/frvt11.html
27. FTC v. IntelliVision Technologies, Inc. (Settlement, January 2025). https://www.ftc.gov
28. Congressional Research Service, "Federal Law Enforcement Use of Facial Recognition Technology" (CRS R46586). https://www.congress.gov/crs-product/R46586
29. American Bar Association, "Face Value: The Complex Legal Implications of Facial Recognition Technology" (Winter 2025). https://www.americanbar.org/groups/criminal_justice/resources/magazine/2025-winter/face-value-complex-legal-implications-facial-recognition-tech/
30. Illinois Biometric Information Privacy Act, 740 ILCS 14/ (as amended 2024-2025). https://law.justia.com/codes/illinois/chapter-740/act-740-ilcs-14/

**Algorithmic Accountability and Harm**

31. ProPublica, "Machine Bias: Risk Assessments in Criminal Sentencing" (2016). https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
32. Springer Nature, "Code Is Law: How COMPAS Affects the Way the Judiciary Handles the Risk of Recidivism" (2024). https://link.springer.com/article/10.1007/s10506-024-09389-8
33. Wyden, Booker, Clarke, Algorithmic Accountability Act of 2023, S.2892 / H.R.5628. https://www.congress.gov/bill/118th-congress/senate-bill/2892/all-info
34. California Privacy Protection Agency, CCPA Automated Decisionmaking Technology Regulations (effective January 1, 2026). https://cppa.ca.gov/regulations/ccpa_updates.html
35. Morgan Lewis, "AI Enforcement Accelerates as Federal Policy Stalls and States Step In" (April 2026). https://www.morganlewis.com/pubs/2026/04/ai-enforcement-accelerates-as-federal-policy-stalls-and-states-step-in

**Encryption and Cryptography**

36. Stanford Law, Cyberlaw Clinic, "Governments Continue Losing Efforts to Gain Backdoor Access to Secure Communications" (May 2025). https://cyberlaw.stanford.edu/blog/2025/05/governments-continue-losing-efforts-to-gain-backdoor-access-to-secure-communications/
37. NIST, "NIST Releases First 3 Finalized Post-Quantum Encryption Standards" (August 2024). https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards
38. NIST, "NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption" (March 2025). https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption
39. Congressional Research Service, "Encryption: Selected Legal Issues" (CRS R44407). https://www.congress.gov/crs-product/R44407
40. University of San Francisco Law Review, "Security Is Not Enough: Privacy in Encryption Regulation" (2025). https://arxiv.org/pdf/2603.00841

**International Frameworks**

41. European Commission, EU AI Act (Regulation (EU) 2024/1689, in force August 1, 2024). https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
42. EU AI Act Summary, High-Level Summary, artificialintelligenceact.eu. https://artificialintelligenceact.eu/high-level-summary/
43. ISED Canada, "Artificial Intelligence and Data Act (AIDA) Companion Document." https://ised-isde.canada.ca/site/innovation-better-canada/en/artificial-intelligence-and-data-act-aida-companion-document
44. UK Online Safety Act 2023. https://www.legislation.gov.uk/ukpga/2023/50
45. ITIF, "The UK's Online Safety Act" (June 2025). https://itif.org/publications/2025/06/09/uk-online-safety-act/

**Post-*Loper Bright* Analysis**

46. *Loper Bright Enterprises v. Raimondo*, 603 U.S. ___ (2024). https://www.supremecourt.gov
47. *Corner Post, Inc. v. Board of Governors*, 603 U.S. ___ (2024). https://www.supremecourt.gov
48. Congressional Research Service, "Loper Bright Enterprises v. Raimondo and the Future of Agency Interpretations of Law" (CRS R48320). https://www.congress.gov/crs-product/R48320
49. Maine Law Review, "A (Loper) Bright Future? Charting Federal AI Governance After Chevron's Demise." https://digitalcommons.mainelaw.maine.edu/cgi/viewcontent.cgi?article=1027&context=sjipl
50. Brennan Center, "An Oversight Model for AI in National Security: The Privacy and Civil Liberties Oversight Board." https://www.brennancenter.org/our-work/analysis-opinion/oversight-model-ai-national-security-privacy-and-civil-liberties

---

*Phase 3 Candidate 7 completed April 28, 2026. Research scope: six institutional domains. Total bibliography: 50 sources. Document length: approximately 7,800 words. Production-ready for institutional distribution.*
