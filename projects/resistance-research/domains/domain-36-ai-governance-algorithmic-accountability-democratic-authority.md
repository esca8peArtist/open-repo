# Domain 36: AI Governance, Algorithmic Accountability, and Democratic Authority

**Research completed**: April 27, 2026 (Session 516)
**Domain status**: Active crisis — federal AI deployment expanding without statutory accountability framework
**Priority designation**: Phase 2 Expansion — essential for adaptive reform planning across benefit systems, immigration, and administrative law
**Cross-domain connections**: Domain 5 (Administrative Procedure / APA), Domain 14 (Education), Domain 16d (Algorithmic Decision-Making in Immigration), Domain 21 (Data Privacy), Domain 29 (DOJ Capture), Domain 33 (State Legislative Autocratization), Domain 35 (Supreme Court / Loper Bright)

---

## Executive Summary

The United States federal government has deployed artificial intelligence systems across every major domestic agency — immigration enforcement, Medicare and Medicaid, Social Security disability adjudication, federal employment, law enforcement surveillance, and grant administration — without a single statute specifically governing those deployments. As of April 2026, the federal government maintains over 3,600 individually-reported AI use cases across 56 agencies. The Department of Homeland Security alone lists 238 AI use cases, with 86 deployed in law enforcement contexts. What is absent is equally significant: no federal law requires pre-deployment impact assessments for government AI. No statute mandates human review of AI-generated adverse decisions affecting individual rights. No law requires agencies to disclose algorithmic decision criteria to affected persons or to their lawyers. No independent audit mechanism exists.

This is not a technology gap. It is an accountability gap that is being actively exploited. The Trump administration revoked Biden's Executive Order 14110 — the primary accountability framework for federal AI — within hours of taking office in January 2025. In December 2025, it signed an executive order directing the Department of Justice to challenge state AI accountability laws in federal court. In January 2026, it launched the WISeR Medicare prior-authorization AI program across six states without public disclosure of the algorithmic model, its training data, its accuracy rate, or its safeguards against wrongful denial. The EFF filed a FOIA lawsuit in March 2026 when CMS produced no responsive records.

The accountability crisis is structural. When AI systems make or substantially determine government decisions about benefits, liberty, and status, the affected person has no practical right to explanation, no meaningful appeal mechanism, and no access to the criteria by which the algorithm judged them. This is not consistent with the Fifth Amendment's due process requirement as applied to government-issued deprivations. It is not consistent with the APA's arbitrary-and-capricious standard. And it will not be cured by technology alone — it requires statutory reform, enforcement authority, and a political theory that locates democratic authority over consequential decisions in elected institutions and in the people they serve, not in procurement contracts and proprietary models.

---

## 1. Current Crisis: Federal AI Deployment Without Accountability

### 1.1 The Scale Problem

The federal government's AI deployment has expanded at a pace that outstrips any available oversight mechanism. According to GAO's April 2026 report (GAO-26-107859), agencies are not yet systematically collecting lessons learned from AI acquisitions. The 2024 AI use case inventory counted 1,110 reported use cases across eleven selected agencies — nearly double the 571 counted in 2023. Generative AI adoption increased ninefold between 2023 and 2024. The OMB's 2025 federal AI use case inventory (published on GitHub at ombegov/2025-Federal-Agency-AI-Use-Case-Inventory) shows 3,611 individually-reported AI use cases at the federal level, spanning all stages of development.

What these inventories do not reveal is more important than what they do. They do not disclose the algorithmic criteria that drive decisions. They do not report denial rates, error rates, or bias testing results by race, gender, disability status, or national origin. They do not identify which systems make autonomous decisions versus advisory recommendations — a distinction that is often blurred in practice by the automation bias phenomenon: when a system generates a recommendation, human reviewers exhibit documented tendencies to defer to it even when the underlying evidence would support a different outcome.

### 1.2 Medicare and Medicaid: The WISeR Program

The clearest current illustration of the accountability gap is the Wasteful and Inappropriate Service Reduction (WISeR) model, launched by the Centers for Medicare and Medicaid Services on January 1, 2026, in six states: New Jersey, Ohio, Oklahoma, Texas, Arizona, and Washington. WISeR deploys AI and machine learning to evaluate prior authorization requests from Medicare beneficiaries and makes coverage-affecting determinations for 6.4 million seniors. The program was announced by CMS Administrator Mehmet Oz and is scheduled to run through 2031.

What is known about WISeR is primarily what CMS has chosen to disclose — which is very little. What is unknown includes: the identity of the AI vendors, the model architecture, the training data, the accuracy rate on independent validation sets, whether the model has been tested for racial or disability-status bias, what the denial rate is compared to prior human review, and what safeguards exist for wrongful denials. Compensation for participating vendors is structured as a percentage of savings from denied services — up to 20% — creating a financial incentive structure that rewards denial.

Weeks after WISeR launched, hospitals and healthcare providers across participating states began reporting delays in care approval, communication gaps with the AI system, and administrative strain. The Electronic Frontier Foundation filed a FOIA request on January 29, 2026, seeking vendor agreements, accuracy and bias testing records, and monitoring and evaluation records. CMS provided no responsive documents. On March 25, 2026, EFF filed suit in federal court (*EFF v. CMS*, filed March 24, 2026) seeking the records. The lawsuit is pending. The absence of records is itself evidence: the accountability gap is not merely procedural, it is a posture of institutional opacity that treats AI deployment in government as a proprietary matter between the agency and its vendor.

The WISeR program also illustrates the interaction with Domain 31 (Healthcare Access / OBBBA / Medicaid crisis). Prior authorization denials powered by AI represent a compounding mechanism in the broader effort to reduce Medicaid and Medicare costs: algorithmic denial is cheaper, faster, and harder to appeal than clinician denial. The National Health Law Program has documented that the Trump administration's AI executive order — by preempting state laws that would mandate human review — directly threatens the state-level protections that have been the primary accountability mechanism for prior authorization in the absence of federal law.

### 1.3 ICE and DHS: Algorithmic Enforcement Without Audit

The Department of Homeland Security's 238 AI use cases, 86 of them in law enforcement, represent the most consequential deployment of AI in the federal government in terms of deprivations of liberty. The primary architecture is Palantir's. ICE operates at minimum four integrated Palantir platforms:

**Investigative Case Management (ICM)**: In use since 2014, deployed under contracts now exceeding $100 million, ICM aggregates data from FBI, DEA, ATF, SEVIS, commercial data brokers (including license plate readers via Vigilant Solutions), and financial records. It generates "predictive leads" — algorithmically surfaced enforcement suggestions. ICM's algorithms are proprietary. No independent audit has been published. FOIA requests for algorithmic specifications have been resisted under law enforcement sensitivity exemptions.

**ELITE**: Identifies deportation targets using map interfaces and "address confidence scores" and locates "target rich" areas for enforcement operations. The system tracks anyone with an "immigration nexus," including naturalized U.S. citizens.

**ImmigrationOS**: A $30 million platform (contract signed April 2025) that consolidates deportation targeting, monitors "self-deportations" with "near real-time visibility," and streamlines logistics. Prototype delivery was scheduled for September 25, 2025; the contract runs through September 2027. ImmigrationOS pulls from passport records, Social Security files, IRS tax data, and license-plate reader data regardless of the accuracy of those underlying databases.

**AI-Enhanced ICE Tip Processing**: Uses generative AI to summarize, categorize, and translate incoming tips — including anonymous tips that are unverified by design.

The 2025 DHS AI Use Case Inventory also lists 29 USCIS-related AI use cases, including an Evidence Classifier that automatically categorizes documents submitted with immigration petitions and tags them for adjudicators. DHS maintains that human adjudicators retain formal decision-making authority and that AI systems do not independently grant or deny immigration benefits. The ACLU's analysis of Palantir's immigration systems documents that "we know little about the selection criteria and algorithms used for identifying targets" or their fairness and bias, and that promises of "human oversight" in these systems "always seem to fall by the wayside."

The FBI's deployment intersects directly here. On March 18, 2026, FBI Director Kash Patel confirmed to the Senate Intelligence Committee that the FBI purchases Americans' location data from commercial data brokers. Senator Ron Wyden warned that "creating AI profiles of Americans based on that data represents a chilling expansion of mass surveillance that should not be allowed." The Trump administration's AI policy framework, released two days later, directed Congress to fund "wider deployment of AI tools across American industry" — implying federal AI expansion, not restriction.

### 1.4 Social Security Administration

SSA's AI deployment in disability adjudication is the quietest of the major accountability gaps. As documented in the April 2025 National Academy of Social Insurance report on AI and disability benefits (Phase One Report, Task Force on Artificial Intelligence, Emerging Technology, and Disability Benefits), SSA uses AI models in the Quick Disability Determination and Compassionate Allowance programs to identify applications for accelerated review. The Hearing Recording and Transcriptions (HeaRT) system, fully deployed by March 2025, uses generative AI to transcribe disability hearings. The Insight program uses natural language processing to identify "weaknesses and inconsistencies" in draft ALJ opinions — effectively providing the agency with an AI tool to flag cases where the administrative judge might be deciding in favor of the claimant.

SSA's September 2025 AI strategy document commits to "continually reinforce humans at the center of AI development and AI-augmented processes." However, the NASI task force report flagged risks that this commitment does not operationalize: non-diverse training data producing bias for conditions not listed in SSA's Adult Listings, automated transcription hallucinations, and predictive models that miss nuanced conditions. The accountability mechanism — "humans at the center" — has no statutory definition, no audit requirement, and no enforcement mechanism.

### 1.5 DOGE and Automated Federal Workforce Decisions

The Department of Government Efficiency, operating outside any statutory authorization, deployed AI systems including AutoRIF for employee termination decisions and CamoGPT for scanning and categorizing government programs. More than 260,000 workers left federal service through DOGE-associated initiatives in 2025. Automated termination decisions produced documented errors — the Department of Agriculture had to rehire bird flu response staff after AI systems terminated them during an active outbreak. DOGE initially claimed $65 billion in savings, then quietly deleted major claims after calculation errors were identified. GAO has been unable to quantify what was saved or lost. Federal spending increased nearly 6% to $7.558 trillion year-over-year.

The accountability question here is not only whether the AI worked correctly. It is whether AI systems can legitimately be used to make employment decisions affecting federal workers without the procedural protections that apply to human-made adverse employment actions — notice, statement of reasons, and opportunity for response.

---

## 2. Root Causes: Why AI Proliferated Without Oversight

### 2.1 The Statutory Vacuum

The United States has no general statute governing the deployment of AI systems by the federal government. The Administrative Procedure Act (5 U.S.C. § 551 et seq.) governs agency rulemaking and adjudication but was enacted in 1946 and contains no provisions specific to automated decision-making, algorithmic transparency, or machine learning systems. The Privacy Act of 1974 requires federal agencies to maintain accurate records about individuals but does not require disclosure of algorithmic criteria or mandate human review. Section 208 of the E-Government Act of 2002 requires Privacy Impact Assessments for federal systems involving personal information but does not extend to algorithmic impact assessments or explainability requirements. The Computer Fraud and Abuse Act governs unauthorized access to computer systems, not the accountability of systems the government deploys against its own population.

GAO's 2025 report (GAO-25-107933) identified 94 AI-related government-wide requirements — but these are executive branch policies, OMB guidance documents, and agency directives, not statutes. They are revocable at will by any administration, as demonstrated by Trump's revocation of Biden's Executive Order 14110 on January 20, 2025. Biden's EO had required federal agencies to appoint Chief AI Officers, conduct impact assessments for high-impact AI uses, and maintain transparency about AI deployments. All of that was gone within hours of the new administration taking office.

### 2.2 Regulatory Fragmentation

The absence of a statutory baseline has produced a fragmented landscape in which accountability requirements vary by agency, by program, and by administration. CMS operates WISeR under Medicare program authority; SSA deploys disability adjudication AI under Social Security Act authority; ICE deploys surveillance infrastructure under immigration enforcement authority. Each operates in its own regulatory silo with no cross-government standard for impact assessment, explainability, human review, or audit. Affected persons cannot know which standard (if any) applies to the system that decided their case.

The Trump OMB memos of April 2025 (M-25-21 and M-25-22) revised the Biden AI governance framework to align with an innovation-over-accountability posture. They retain some procedural language about impact assessments and human oversight for "high-impact" AI uses, but they implement a 365-day compliance window, no enforcement mechanism, and no definition of what constitutes a sufficient human review. The memos are discretionary guidance, not binding law.

### 2.3 Opacity as Institutional Interest

Federal agencies and their private AI vendors share a structural interest in opacity that is independent of political alignment. Agencies benefit from AI that enables them to process more claims, denials, and enforcement actions with fewer staff. Vendors benefit from proprietary protection of their model architectures and training data — both to maintain competitive advantage and to insulate themselves from liability for wrongful outcomes. The combination produces a decisional system in which the agency says "a human made the decision," the vendor says "the model is proprietary," and the affected person has no access to either.

The WISeR compensation structure illustrates the mechanism: vendors earn a percentage of savings from denied services. There is no equivalent incentive for accuracy on appeals. The financial architecture of government AI procurement systematically rewards denial volume over decision quality.

### 2.4 The Post-Loper Bright Complication

*Loper Bright Enterprises v. Raimondo* (2024), analyzed in Domain 35, eliminated Chevron deference and requires courts to exercise independent judgment on statutory interpretation. This creates a two-edged problem for AI accountability. On one edge, courts reviewing AI-driven agency decisions cannot defer to agency interpretations of what their enabling statutes authorize — meaning AI deployments without clear statutory authority are now more legally vulnerable. On the other edge, *Loper Bright* means that the accountability frameworks agencies have built under discretionary authority (OMB guidance, executive orders) cannot substitute for statutory authorization. The practical implication: robust AI accountability requires Congress to act, because executive-branch-only frameworks are both legally insufficient after *Loper Bright* and politically revocable between administrations.

---

## 3. Structural Vulnerabilities

### 3.1 No Statutory Authority Review Requirement

Federal agencies can currently deploy AI systems that make or substantially influence individual-rights determinations without any requirement to demonstrate that their enabling statute authorizes algorithmic decision-making. ICE deploys ImmigrationOS under immigration enforcement authority that says nothing about Palantir contracts, predictive analytics, or automated targeting scores. CMS deploys WISeR under Medicare program authority that similarly says nothing about prior authorization AI or vendor compensation structures tied to denial rates. After *Loper Bright*, these gaps in statutory authorization are legally significant, but only if someone litigates — which requires the person affected to know they were subjected to an AI system, know its criteria, and have resources for litigation.

### 3.2 Automation Bias and Decisional Opacity

Automation bias — the documented tendency of human reviewers to defer to machine-generated outputs rather than exercise independent judgment — means that nominal "human-in-the-loop" requirements frequently do not provide the accountability they appear to. When an AI system recommends denial, and a caseworker reviews that recommendation in thirty seconds while managing hundreds of similar cases, the "human review" is a formality. Virginia Eubanks documented this mechanism in detail in *Automating Inequality* (2018), showing how Indiana's welfare fraud detection algorithm produced error rates exceeding 90% while caseworkers validated algorithmic flags without independent review. The Michigan Integrated Data Automated System (MiDAS) case is directly analogous: the unemployment fraud detection algorithm flagged cases as fraudulent at a rate five times higher than the prior system, and 93% of those findings were incorrect.

### 3.3 No Audit Trail Requirement

Federal AI systems are not required to maintain audit trails sufficient to reconstruct how a specific decision was reached. This means that in an appeal or judicial review, neither the affected person nor a reviewing court can examine the inputs, weights, training data, or intermediate outputs that produced the outcome. The arbitrary-and-capricious standard of the APA (5 U.S.C. § 706(2)(A)) requires that agency action be explained with a rational connection between facts found and choice made — but when the fact-finding is done by an opaque model, the explanation is structurally unavailable. Courts have not yet resolved whether AI-assisted decisions satisfy the APA's reasoned explanation requirement.

### 3.4 Inadequate Appeal Rights

The right to appeal a government adverse decision is formally preserved in most benefit and enforcement systems, but algorithmic opacity effectively nullifies it. An appeal of a WISeR denial requires the claimant to contest a decision whose criteria are proprietary. An appeal of an ICE enforcement action targeting someone algorithmically identified by ELITE or ImmigrationOS requires access to system criteria that have never been disclosed. The Senate Finance Committee sent a letter to SSA in June 2025 raising concerns about AI usage, but no legislation mandating disclosure has been enacted. Appeal processes designed for human decision-making — with their implicit assumption that the decision-maker can be asked to explain their reasoning — do not translate coherently to algorithmic systems whose reasoning is not reconstructable by design.

### 3.5 Private Data Broker Loophole

Federal agencies are circumventing Fourth Amendment warrant requirements by purchasing commercially available data — including location histories, financial records, and social media activity — from data brokers rather than obtaining it through compulsory legal process. This loophole, confirmed by Kash Patel's March 2026 Senate testimony on FBI location data purchases, allows AI-powered profiling and targeting without judicial authorization. The data broker loophole operates as an AI governance gap because the AI systems that analyze purchased data — including Palantir's ICE platforms — are consuming warrantless surveillance at scale.

---

## 4. International Precedent

### 4.1 The EU AI Act: Risk-Based Regulation with Enforcement

The EU Artificial Intelligence Act, which entered into force on August 1, 2024, is the most comprehensive AI governance framework in the world and the most relevant international precedent for U.S. reform. It uses a risk-based approach that categorizes AI systems by the level of risk they pose, with different requirements for each tier.

**Prohibited AI practices** became effective February 2, 2025. These include: social scoring systems used by public authorities; AI systems using subliminal techniques to manipulate behavior; real-time remote biometric identification in publicly accessible spaces (with narrow law enforcement exceptions requiring judicial authorization); and emotion recognition systems in workplace and educational settings.

**High-risk AI systems** — including those affecting benefits, immigration, law enforcement, education, employment, and access to essential services — face obligations effective August 2, 2026. These obligations include: mandatory human oversight requirements that are technically enforceable (not merely nominal); transparency to deployers and affected persons; detailed technical documentation; conformity assessments before deployment; continuous post-market monitoring; and registration in an EU-wide database.

**General-purpose AI models** have been subject to governance rules since August 2, 2025, including documentation requirements, transparency duties, and systemic risk mitigation obligations.

The EU AI Act's most significant contribution to U.S. reform thinking is the distinction between nominal human oversight and technically meaningful human oversight. The Act requires that high-risk AI systems be designed to allow human operators to "fully understand the AI system's capacities and limitations" and to "correctly interpret the AI system's output" — not merely to rubber-stamp it. This operationalizes the accountability principle that automation bias research demonstrates is necessary: oversight is only meaningful if it is technically equipped to be independent.

The EU framework also requires high-risk AI systems to be tested for accuracy, robustness, and bias before deployment — including testing on representative population subgroups. This is the accountability mechanism conspicuously absent from WISeR, ImmigrationOS, and SSA's disability adjudication AI.

### 4.2 Canada AIDA: A Cautionary Note

Canada introduced the Artificial Intelligence and Data Act (AIDA) as part of Bill C-27, the Digital Charter Implementation Act 2022. AIDA would have required pre-deployment risk assessments for "high-impact" AI systems, bias mitigation measures, transparency obligations, and record-keeping. The bill died on the order paper on January 6, 2025, when Prime Minister Trudeau's resignation triggered prorogation of Parliament.

AIDA's failure is instructive. The bill was pending for nearly three years without becoming law, demonstrating that AI governance legislation faces strong institutional headwinds even in democratic systems with political will to act. Canada's Directive on Automated Decision-Making (2019), a binding policy instrument for federal government AI deployments, remains in force and provides an operational model: it requires algorithmic impact assessments calibrated to decision impact level, peer review, notice to affected persons, explanation of decisions, human review options, and audit trail maintenance. Canada's experience establishes that a regulatory model (government-binding directive) can operate in advance of legislation, but also that regulatory frameworks without statutory backing are vulnerable to political change.

### 4.3 The UK Framework: Sector-Specific Oversight

The United Kingdom published its AI Opportunities Action Plan on January 13, 2025, and the Department for Science, Innovation and Technology released a progress report on January 29, 2026. The UK maintains a sector-specific approach: existing regulators apply AI-specific guidance within their established domains (financial services, healthcare, employment), with requirements to report annually on how they have enabled AI while maintaining safety.

The UK framework's contribution is its approach to meaningful human oversight: it identifies "human in the loop" as inadequate when checks become "formalities rather than critical parts of the process" and flags criminal liability where organizations over-rely on automated outputs without genuine review. It also requires documentation, audit trails, testing, and incident reporting as the practical infrastructure for accountability — not as aspirational principles but as operational prerequisites.

The UK has not enacted comprehensive AI legislation comparable to the EU AI Act. The Artificial Intelligence (Regulation) Bill, introduced in Parliament in 2023, has not advanced. This makes the UK framework closer to the current U.S. posture — and demonstrates the limits of principle-based approaches without enforcement authority.

---

## 5. Reform Pathways

### 5.1 Reform 1: Federal AI Governance Act — Statutory Baseline

**The gap it closes**: No single statute currently requires federal agencies to follow any accountability procedure for AI deployments. Executive orders and OMB memos are revocable and have been revoked.

**Core provisions**:

A Federal AI Governance Act should establish: (1) A classification requirement for all federal AI systems by impact level — automated flag for review, advisory input to human decision, primary factor in outcome, autonomous determination — with accountability requirements scaled to classification. (2) Pre-deployment testing requirements for all Class 3 and 4 systems (those substantially shaping or autonomously making individual-affecting decisions), including accuracy testing, bias testing disaggregated by protected class, and adversarial testing for edge cases. (3) Technical documentation requirements sufficient for independent audit: training data description, model architecture at a conceptually graspable level, validation methodology, and ongoing performance monitoring results. (4) Disclosure to affected persons: when an AI system substantially shaped or made a decision affecting an individual's rights, benefits, or liberty, the agency must disclose the fact of AI use, the factors the system considered, and the basis for the outcome, in plain language accessible to a person without legal training. (5) Mandatory human review: for any adverse decision in Class 3 or 4 — including benefit denials, enforcement targeting, and custody determinations — the human reviewer must document their independent assessment, and the review must be technically equipped to deviate from the AI output.

**Statutory sketch**: "No agency may deploy an AI system at Class 3 or Class 4 impact level without completing a pre-deployment impact assessment meeting the standards published by the AI Governance Board under Section [X], filing that assessment with the Board and the relevant congressional oversight committee, and publishing a summary accessible to the public. An adverse decision substantially shaped by a Class 3 or Class 4 system shall not be final until a qualified human reviewer has issued a documented independent assessment. The affected person shall receive a written explanation meeting the standards of Section [Y]."

### 5.2 Reform 2: APA Modernization — Algorithmic Due Process Amendment

**The gap it closes**: The APA's arbitrary-and-capricious and reasoned explanation standards (5 U.S.C. § 706) were designed for human decision-making. Courts have not resolved whether AI-assisted decisions satisfy these standards when the decision rationale is structurally inaccessible.

**Core provisions**: An Algorithmic Due Process Amendment to the APA should establish that: (1) An agency decision substantially shaped by an AI system satisfies the reasoned explanation requirement only if the agency can reconstruct, from an audit trail, the inputs the system considered, the weights applied, and the basis for the output. (2) If no such audit trail exists, the decision is per se arbitrary and capricious. (3) An affected person may, in any challenge to an AI-assisted adverse agency decision, compel production of the audit trail documentation in administrative proceedings, not only in judicial review — reversing the current pattern in which algorithmic opacity makes administrative appeal effectively unavailable. (4) For high-impact AI decisions (benefit denials, removal orders, custody determinations), the agency must produce an explanation that the affected person can use to construct an appeal — meaning the explanation must identify the factors that drove the adverse outcome, not merely confirm that a system was used.

**Connection to Domain 5**: This reform directly extends the administrative procedure domain. The APA's due process architecture currently has no mechanism for the situation in which the decision-maker cannot explain its reasoning because it is an opaque model.

### 5.3 Reform 3: Algorithmic Impact Assessment Requirement

**The gap it closes**: Federal agencies can deploy AI systems affecting millions of people without any pre-deployment evaluation of accuracy, bias, or adverse-impact potential. This parallels the absence of environmental impact assessments before NEPA (42 U.S.C. § 4321 et seq.), which established pre-decisional review as a structural principle of government accountability.

**Core provisions**: Modeled on Canada's Directive on Automated Decision-Making and the EU AI Act's conformity assessment requirements, a federal Algorithmic Impact Assessment (AIA) requirement should: (1) Require any federal agency deploying a Class 3 or Class 4 AI system to complete an AIA before deployment and publish it publicly. (2) The AIA must document: the decision the system is designed to support; the population affected; the training data and its representational completeness; bias testing results disaggregated by race, gender, disability status, national origin, and income; accuracy metrics on independent validation sets; the compensation and incentive structure of any vendor contract; and the available appeal mechanism for adverse outcomes. (3) Congress's Government Accountability Office should receive all AIAs and conduct risk-based audits. (4) Existing systems deployed before the Act's enactment must complete retrospective AIAs within 24 months or be suspended from Class 3/4 use.

**The WISeR precedent**: Under this requirement, WISeR could not have launched without a public AIA disclosing vendor compensation structure, bias testing, and accuracy data. The EFF's FOIA lawsuit illustrates precisely the enforcement mechanism an AIA requirement replaces: mandatory pre-deployment disclosure instead of litigation-forced post-hoc disclosure.

### 5.4 Reform 4: AI Audit Rights — Congressional and Inspector General Access

**The gap it closes**: Congress has no reliable mechanism to audit the AI systems that agencies deploy. Inspector Generals have institutional authority but lack technical AI audit expertise, access to proprietary model documentation, and a statutory mandate for AI-specific audits.

**Core provisions**: (1) A federal AI Audit Act should require that all Class 3 and Class 4 AI systems be registered in a congressional AI registry maintained by GAO, with technical documentation sufficient for audit. (2) Each agency's Inspector General should receive statutory AI audit authority, including the power to commission independent third-party technical audits of model performance, bias, and accuracy. (3) GAO should be authorized and resourced to conduct AI-specific audits as part of its agency oversight mandate, with access to proprietary model documentation under protective orders. (4) Vendor contracts for government AI must include mandatory audit-access provisions — the government retains the right to audit model performance, training data, and decision rationale. This provision directly addresses the proprietary trade secret defense that has insulated systems like ICM and WISeR from accountability.

**Connection to Domain 34**: This reform reinforces the congressional power-of-the-purse and oversight function. Congress cannot exercise meaningful fiscal or programmatic oversight of agencies whose most consequential operational decisions are made by systems Congress has never reviewed.

### 5.5 Reform 5: State AI Authority Floor — Minimum Standards, No Federal Ceiling

**The gap it closes**: The Trump December 2025 Executive Order directs DOJ to challenge state AI accountability laws as inconsistent with federal policy. The national AI policy framework released March 20, 2026, pushes for federal preemption of state AI regulation. This removes the primary accountability mechanism currently in place — state laws — without replacing them with anything equivalent.

**Core provisions**: Congress should enact a State AI Authority Act establishing that: (1) Federal AI governance standards under a Federal AI Governance Act are floors, not ceilings. States may enact additional requirements, provided they do not conflict with specific federal standards. (2) The carve-outs in the Trump executive order for state government procurement and state AI use — which the December 2025 EO preserved — should be codified in statute as non-preemptible. (3) State prior authorization laws requiring human review of healthcare coverage decisions are specifically not preempted by federal AI policy, resolving the ambiguity the Trump executive order created. (4) DOJ's AI Litigation Task Force (created by the December 2025 EO) should be prohibited from challenging state AI laws that meet or exceed federal minimum standards.

**Connection to Domain 33**: State legislative autocratization (Domain 33) has produced a landscape in which states are simultaneously the source of AI accountability protections (California SB 1120, Texas PA human review law, Colorado Consumer Protections Act) and targets of federal preemption. The federal floor mechanism is essential to preserve state-level democratic experimentation.

### 5.6 Reform 6: Private Right of Action for Algorithmic Harm

**The gap it closes**: Individuals harmed by government or private AI systems — wrongfully denied benefits, wrongfully arrested through facial recognition error, wrongfully terminated from federal employment — currently have no direct private cause of action specific to algorithmic harm. They must rely on existing civil rights statutes, the APA, or constitutional claims, all of which have structural difficulties with opaque algorithmic systems.

**Core provisions**: The Artificial Intelligence Civil Rights Act of 2025 (S. 3308, introduced in the 119th Congress) provides a model: it prohibits developers and deployers from using AI in a manner that causes disparate impact or discrimination on the basis of protected characteristics, requires pre-deployment evaluations, and provides for a private right of action. A comprehensive reform should: (1) Establish a private right of action for any person adversely affected by a federal agency's use of a Class 3 or Class 4 AI system who was not provided the required explanation, human review, or appeal opportunity. (2) Establish a cause of action for any person whose facial recognition misidentification contributed to a wrongful arrest, custody determination, or adverse agency action — without requiring proof of discriminatory intent. (3) Provide for fee-shifting in cases of successful challenge to AI-assisted government decisions that lacked required accountability procedures, making such litigation viable for individuals without resources. (4) Eliminate the proprietary trade secret defense as a complete bar to discovery in litigation over algorithmic government decisions — the government's claim of trade secret protection on behalf of its vendors cannot override a citizen's right to contest a government adverse action.

**The facial recognition record**: ACLU has documented 14 wrongful arrests attributable to facial recognition misidentification, all involving people of color. Without a private right of action specific to algorithmic harm, victims of facial recognition error must navigate general civil rights frameworks designed for intentional discrimination — a poor fit for probabilistic machine error.

---

## 6. Implementation Timeline

The sequencing of these reforms must account for the current political environment, in which unified federal AI accountability legislation is not achievable in the 119th Congress. The realistic implementation horizon runs through a democratic recovery scenario (2027 at the earliest for meaningful legislative change), with preparatory work achievable before then.

**Immediate (now through 2026)**: The Algorithmic Accountability Act of 2025 (S. 2164 / H.R. 5511) and the Eliminating Bias in Algorithmic Systems Act of 2026 (H.R. 7110 / S. 3680) are minority-sponsored bills unlikely to pass in current congressional alignment, but they establish the legislative language baseline. Civil society organizations should treat EFF v. CMS and parallel FOIA litigation as discovery mechanisms — the records obtained will document the accountability gap with agency-specific precision needed for post-recovery legislation. State AI legislation (Colorado, California, New York, Texas PA laws) should be defended against DOJ preemption challenges; loss in those cases creates appellate precedent that will shape any federal floor statute. GAO's ongoing AI work (GAO-26-107859 and successor reports) should be actively directed by sympathetic congressional members toward the specific accountability gaps documented here.

**Near-term (2027–2028, democratic recovery scenario)**: First priority is APA Algorithmic Due Process Amendment — it can be attached to broader APA modernization and has bipartisan appeal as a rule-of-law measure. Second priority is the Algorithmic Impact Assessment requirement for new federal AI deployments — analogous to NEPA's pre-decisional review, it is a procedural rather than substantive constraint and may draw broader support. Third priority is the State AI Authority Floor, which codifies the carve-outs the Trump EO recognized and prevents federal preemption of accountability-oriented state law.

**Medium-term (2028–2030)**: Federal AI Governance Act — the comprehensive statutory baseline — requires sustained congressional attention and is likely to emerge from the framework established by the earlier reforms. Congressional and IG AI Audit Rights should accompany the FAGA to provide enforcement infrastructure. Private Right of Action provisions are likely to require the most political negotiation and may initially be enacted with narrower standing requirements before expansion.

---

## Sources

- [EFF Sues for Answers About Medicare's AI Experiment — Electronic Frontier Foundation](https://www.eff.org/press/releases/eff-sues-answers-about-medicares-ai-experiment)
- [EFF v. CMS Complaint (March 24, 2026)](https://www.courthousenews.com/wp-content/uploads/2026/03/complaint_-_eff_v_cms.pdf)
- [Federal AI Policy Threatens Prior Authorization Reform — National Health Law Program](https://healthlaw.org/federal-ai-policy-threatens-prior-authorization-reform/)
- [GAO-26-107859: AI Acquisitions — Agencies Should Collect and Apply Lessons Learned (April 2026)](https://www.gao.gov/products/gao-26-107859)
- [GAO-25-107933: Artificial Intelligence: Federal Efforts Guided by Requirements and Advisory Groups (September 2025)](https://www.gao.gov/products/gao-25-107933)
- [GAO-25-107653: Artificial Intelligence: Generative AI Use and Management at Federal Agencies (July 2025)](https://www.gao.gov/products/gao-25-107653)
- [GAO-21-519SP: Artificial Intelligence: An Accountability Framework for Federal Agencies (2021)](https://www.gao.gov/products/gao-21-519sp)
- [FBI Is Buying Location Data to Track US Citizens, Kash Patel Confirms — TechCrunch](https://techcrunch.com/2026/03/18/fbi-is-buying-location-data-to-track-us-citizens-kash-patel-wyden/)
- [All the Ways Palantir Is Assisting Trump's Abusive Removal Campaign — ACLU](https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup)
- [ICE to Use ImmigrationOS by Palantir — American Immigration Council](https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants/)
- [ICE Uses a Growing Web of AI Services — American Immigration Council](https://www.americanimmigrationcouncil.org/blog/ice-uses-ai-immigration-enforcement-surveillance/)
- [DHS AI Use Case Inventory — Homeland Security](https://www.dhs.gov/ai/use-case-inventory)
- [Law Enforcement Is the Leading DHS Use Case for AI — Nextgov/FCW](https://www.nextgov.com/artificial-intelligence/2026/01/law-enforcement-leading-dhs-use-case-ai/411063/)
- [Trump Administration's December 2025 AI Executive Order — Ensuring a National Policy Framework for Artificial Intelligence, White House](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/)
- [OMB Memoranda M-25-21 and M-25-22: Federal AI Use and Procurement (April 2025)](https://www.insidegovernmentcontracts.com/2025/04/omb-issues-first-trump-2-0-era-requirements-for-ai-use-and-procurement-by-federal-agencies/)
- [Phase One Report: Task Force on AI, Emerging Technology, and Disability Benefits — National Academy of Social Insurance (April 2025)](https://www.nasi.org/wp-content/uploads/2025/04/Phase-One-Report-Task-Force-on-Artificial-Intelligence-Emerging-Technology-and-Disability-Benefits.pdf)
- [EU AI Act Implementation Timeline — artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act — European Commission Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Canada AIDA: Death of Canada's AI Regulation — Montreal AI Ethics Institute](https://montrealethics.ai/the-death-of-canadas-artificial-intelligence-and-data-act-what-happened-and-whats-next-for-ai-regulation-in-canada/)
- [Canada AIDA Companion Document — ISED Canada](https://ised-isde.canada.ca/site/innovation-better-canada/en/artificial-intelligence-and-data-act-aida-companion-document)
- [UK AI Opportunities Action Plan 2026 Progress Report — CMS Law](https://cms.law/en/gbr/publication/uk-ai-opportunities-action-plan-2026-progress-report)
- [Algorithmic Accountability Act of 2025, S. 2164 / H.R. 5511 — Congress.gov](https://www.congress.gov/bill/119th-congress/senate-bill/2164)
- [Artificial Intelligence Civil Rights Act of 2025, S. 3308 — Congress.gov](https://www.congress.gov/bill/119th-congress/senate-bill/3308/text)
- [Eliminating Bias in Algorithmic Systems Act of 2026, H.R. 7110 / S. 3680 — Congress.gov](https://www.congress.gov/bill/119th-congress/house-bill/7110/text)
- [Algorithmic Accountability Policy Toolkit — AI Now Institute](https://ainowinstitute.org/publications/algorithmic-accountability-policy-toolkit)
- [Algorithmic Accountability for the Public Sector (April 2025) — AI Now Institute / Ada Lovelace Institute](https://ainowinstitute.org/publications/algorithmic-accountability-for-the-public-sector-report)
- [2025 Federal Agency AI Use Case Inventory — OMB / GitHub](https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory)
- [DOGE AI Tools and Government Automation Concerns — CNN Business](https://edition.cnn.com/2025/03/04/tech/doge-ai-government-cuts-expert-concerns)
- Virginia Eubanks, *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor* (St. Martin's Press, 2018)
