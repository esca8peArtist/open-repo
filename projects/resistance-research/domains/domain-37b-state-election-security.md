---
title: "Domain 37b: State Election Security and Election Administration Vulnerability"
project: resistance-research
created: 2026-05-06
session: Phase 2 Domain 37b Research
phase: Phase 2
domain_type: Structural Security Analysis
status: production-ready
word_count: ~6800
confidence: high — sourced to CISA primary documentation, Brennan Center surveys, EAC grant data, Verified Voting equipment database, NCSL audit tracker, Votebeat state reporting, ProPublica investigations, MS-ISAC transition documentation, OSCE 2024 election observation final report, Elections Canada official documentation, Bundeswahlleiterin 2025 technical framework, and AEC 2025 security framework
cross_domain:
  - "Domain 1 (Voting Rights and Elections)"
  - "Domain 37 (Federal Executive Interference in 2026 Midterms)"
  - "Domain 37a (Post-Election Section 3 Litigation and Certification Recovery)"
  - "Domain E (Election Administration Seizure and 2026 Midterm Defense)"
  - "Domain 33 (State Legislative Autocratization)"
  - "Domain 36 (AI Governance and Algorithmic Accountability)"
distinction: >
  Domain 37 documents federal interference mechanisms — CISA destruction, DOJ capture, executive overreach.
  Domain E documents operational administration seizure — who runs elections, certification capture, official turnover.
  Domain 37b covers the structural state-level substrate: vendor lock-in, equipment vulnerabilities, audit gaps,
  voter database integrity, supply chain security, and poll worker vetting — the physical and technical
  infrastructure that must function correctly regardless of which political actors are in charge.
advocacy_windows:
  - "June 15, 2026: CISA state election security assessment release window"
  - "August 7, 2026: NVRA 90-day quiet period begins — systematic purge window closes"
  - "August 7–October 31, 2026: Certification season for 2026 general election"
---

# Domain 37b: State Election Security and Election Administration Vulnerability

**Research completed**: May 6, 2026
**Domain status**: Active pre-election security crisis — six months to November 2026 midterms
**Priority designation**: Phase 2 Tier B — acute calendar-driven urgency
**Advocacy windows**: June 15, 2026 (CISA assessment); August 7–October 31, 2026 (certification season)

---

## Executive Summary

State election security in the United States is structurally fragile in ways that exist independent of — and compound — the federal interference documented in Domains 37 and E. The fragility has three roots: a highly concentrated voting technology market controlled by three vendors whose proprietary code and certification processes resist independent audit; a patchwork post-election audit landscape in which nearly half of states lack the gold standard of risk-limiting audits; and a voter registration database ecosystem in which nine states have withdrawn from the only interstate data-sharing cooperative (ERIC), creating isolated voter rolls susceptible to both error and manipulation.

These structural vulnerabilities have been made acute by the collapse of the federal support architecture. CISA's election security program has been effectively zeroed out — $39.6 million eliminated, 130 staff fired, 700 annual cybersecurity assessments discontinued, 1,300 physical security assessments ended — and the FY27 budget proposes to eliminate the program entirely from the appropriations baseline. MS-ISAC, the multi-state cybersecurity sharing network, lost its federal funding on September 30, 2025, and has moved to a paid membership model that only 11 states have joined. The EI-ISAC, which served as the national election-specific incident-sharing network, has been defunded. The $45 million in FY26 EAC security grants — approximately $900,000 per state — is insufficient for any substantial security program at the county level where elections are actually administered.

The vendor landscape compounds the risk. Dominion Voting Systems, which serves approximately 30 percent of the U.S. election market, was sold in October 2025 to Liberty Vote — a company controlled by a former Republican Missouri elections official and e-pollbook vendor with existing commercial relationships with election jurisdictions. ES&S, the market's largest vendor by share, has a documented history of using litigation to protect its market position and has resisted independent code audits. Hart InterCivic serves approximately 15 percent of the market. Together, the three companies control roughly 90 percent of U.S. election technology with no federal oversight of their supply chains, no mandatory source code disclosure, and no independent penetration testing requirement as a condition of EAC certification.

The certification season running from August 7 through October 31, 2026 — when 26 states elect new chief election officials, at least 53 election-denying candidates are competing for offices with certification authority, and states must complete canvassing and certification for November results — represents the convergence of every vulnerability documented in this analysis. The structural recommendations are clear. The advocacy window is closing.

---

## Part 1: The Vendor Landscape — Concentration, Proprietary Control, and Certification Gaps

### 1.1 Market Concentration and the Three-Vendor Duopoly

Three companies — Election Systems and Software (ES&S), Liberty Vote (formerly Dominion Voting Systems), and Hart InterCivic — control approximately 90 percent of U.S. election technology. This concentration is not the product of superior competition but of market structure: the election technology sector is uniquely resistant to new entrants because of the high cost of EAC certification, the long procurement cycles of local governments, and the legal leverage that dominant vendors exercise when contracts are threatened.

ProPublica's investigation into the market documented that ES&S, which holds the largest market share of the three major vendors, "used a variety of controversial tactics" to maintain its position, including "routinely going to court when it fails to win contracts or has them taken away, suing voting jurisdictions, rivals, advocates for greater election security and others." The investigation found that election officials and experts across the political spectrum characterized the market's structure — not any individual company — as the fundamental problem: the very nature of the industry and the way it is regulated "work against innovation and reward the tiny handful of often trouble-plagued companies that have been around for decades."

The consequence of this concentration for security is straightforward: a zero-day vulnerability in ES&S software affects every jurisdiction that uses ES&S equipment, potentially across dozens of states, simultaneously. There is no market diversity to contain the blast radius of a successful attack on a dominant vendor.

**The Liberty Vote acquisition** introduces a new and unresolved risk factor. In October 2025, Scott Leiendecker — a former Republican Missouri elections director and founder of KnowInk, the nation's most widely used e-pollbook vendor — purchased Dominion Voting Systems and rebranded it as Liberty Vote. Leiendecker privately financed the acquisition for an undisclosed sum. The acquisition creates an unusual ownership profile: a single individual who is simultaneously the founder of the e-pollbook company with the largest national market share and the owner of the voting machine company serving approximately 30 percent of U.S. jurisdictions. Neither the Department of Justice nor the Department of Homeland Security has requested a security review of the acquisition or of Liberty Vote's equipment. State election officials were assured that "no staff changes, contract terminations, or product overhauls are expected" — an assurance that substitutes for, not supplements, independent security assessment.

Liberty Vote has stated its goal is "to restore public confidence in the electoral process through transparent, secure, and trustworthy voting systems, including the use of hand-marked paper ballots." Whether the new ownership translates into more or less security transparency than Dominion's prior ownership structure is not yet empirically assessable.

Sources: [ProPublica: The Market for Voting Machines Is Broken](https://www.propublica.org/article/the-market-for-voting-machines-is-broken-this-company-has-thrived-in-it); [Votebeat: After Trump attacks, Dominion is forging ahead as Liberty Vote](https://www.votebeat.org/2026/02/12/dominion-liberty-vote-scott-leiendecker-voting-systems-machines-election-equipment/); [Spotlight PA: Dominion Voting Systems sold to GOP official](https://www.spotlightpa.org/news/2025/10/dominion-voting-systems-sale-liberty-vote-election-security-elections/)

### 1.2 Certification Standards and the VVSG 2.0 Baseline

The Voluntary Voting System Guidelines (VVSG) 2.0, administered by the Election Assistance Commission, establish the federal certification baseline for voting equipment. The key word is "voluntary": VVSG certification is a condition of EAC endorsement but not of state use, and several states have certified equipment under state standards alone without seeking EAC certification.

VVSG 2.0 requires that voting systems produce voter-verified paper records — a significant security advance over the paperless DRE systems it is designed to replace. It also requires software independence (election outcomes cannot be changed undetectably through software means) and auditability. What VVSG 2.0 does not require: mandatory source code disclosure to independent researchers, mandatory penetration testing by government-contracted security teams, or chain-of-custody standards for the software supply chain upstream of the voting machine manufacturer.

The EAC has conditioned HSGP (Homeland Security Grant Program) funds on compliance with VVSG 2.0 certification — creating a financial incentive for states to upgrade equipment. But the baseline funding level ($45 million for all states and territories in FY26) makes comprehensive equipment replacement economically infeasible for most states. The Brennan Center's 2024 cost analysis documented that replacing voting equipment across the country's approximately 8,000 county election offices would cost billions, not millions.

The administration's FY27 budget proposes eliminating CISA's election security program entirely — removing the 14 CISA staff positions and $39.6 million that supported states in conducting cybersecurity assessments of their equipment and infrastructure. This would leave EAC as the sole federal entity with any election security mandate, and EAC's mandate is limited to certification and grants — it has no operational cybersecurity function.

Source: [Nextgov: Trump proposes cutting CISA election security program in FY27 budget](https://www.nextgov.com/cybersecurity/2026/04/trump-proposes-cutting-cisa-election-security-program-fy27-budget/412672/)

### 1.3 Proprietary Code, Source Code Escrow, and the Audit Limitation

All three major U.S. voting system vendors treat their software as proprietary. Source code is not publicly available. EAC certification testing is conducted by a small number of accredited Voting System Test Laboratories (VSTLs), which review the code under non-disclosure agreements and produce reports that are partially redacted when published. Independent security researchers cannot conduct comprehensive vulnerability assessments of voting system software without vendor cooperation — which is rarely granted — or without acquiring the equipment through non-vendor channels, a legally ambiguous process that the vendors have historically contested.

The practical consequence: when CISA security researchers discovered vulnerabilities in Dominion Voting Systems ImageCast X ballot-marking devices in 2022 — including one that could allow printing of unauthorized ballots — the vulnerability disclosure required a multi-year coordination process with the vendor, the EAC, and state certification authorities before remediation reached deployed equipment. That coordination pipeline now lacks its federal coordinator: CISA's election security team no longer exists as a functional unit. Future vulnerabilities discovered in deployed equipment have no established federal triage pathway.

The 2025 German federal election (Bundestagswahl) provides a direct contrast: Germany's Bundeswahlleiter uses only hand-marked paper ballots counted publicly by citizen volunteers, with a baseline protection profile developed by a joint federal-state working group of the Federal Office for Information Security (BSI) that is published and subject to independent review. Germany's system is technically inferior to U.S. systems in processing speed but structurally superior in auditability and public verifiability. The German approach represents the logical endpoint of the audit-first principle: when you cannot verify the software, you eliminate the software from the definitive count.

Sources: [CISA: Vulnerabilities Affecting Dominion Voting Systems ImageCast X](https://www.cisa.gov/news-events/ics-advisories/icsa-22-154-01); [Bundeswahlleiterin: 2025 Bundestag Election Security Framework](https://www.bundeswahlleiterin.de/en/bundestagswahlen/2025.html); [BMI: Protecting the 2025 Bundestag elections from hybrid threats](https://www.bmi.bund.de/SharedDocs/schwerpunkte/EN/disinformation-election/disinformation-election-artikel.html)

---

## Part 2: Paper Ballot Progress and Remaining Audit Gaps

### 2.1 The 98 Percent Paper Record Achievement — and Its Limits

More than 98 percent of ballots cast in the 2024 U.S. general election had an auditable paper record — up from 93 percent in 2020. This is a genuine security achievement, driven by state legislation and EAC certification requirements adopted since 2016. Louisiana, which was among the last remaining states using exclusively paperless DRE machines, passed legislation requiring new voting systems to produce voter-verified paper records and is in the process of transitioning equipment. Indiana, Mississippi, and Tennessee have all enacted similar requirements.

But the 98 percent figure requires careful interpretation. There are two types of paper records that count toward this statistic, and they have very different security properties.

**Hand-marked paper ballots** scanned by optical readers are the gold standard: the voter's physical mark is the auditable record, and the scanner's output can be verified against the paper. If the scanner is compromised, the paper record is unaffected and a hand count is determinative.

**Ballot-marking devices (BMDs)** print a summary card with a barcode that the voter reviews before submitting. The barcode, not the printed text, is what tabulators read. Security researchers at Georgia Tech, Stanford, and MIT have documented that most voters do not and cannot verify that the printed barcode matches their intended selections — creating a residual risk that a compromised BMD produces votes that diverge from voter intent while appearing to have a paper record. This risk is theoretical but empirically grounded in voter behavior studies.

The remaining approximately 2 percent of votes cast on purely paperless equipment are concentrated in specific counties in Louisiana (transitioning), a small number of Texas counties (whose transition deadline was 2026), and scattered legacy deployments. These are the highest-priority equipment replacement targets: they cannot be audited by any means other than recounting the machine's electronic memory.

Sources: [Brennan Center: Some Good News for Donald Trump: We Already Use Paper Ballots](https://www.brennancenter.org/our-work/analysis-opinion/some-good-news-donald-trump-we-already-use-paper-ballots); [GovTech: Despite Risks, Some States Still Use Paperless Voting Machines](https://www.govtech.com/elections/despite-risks-some-states-still-use-paperless-voting-machines.html); [Governing: America Moves Decidedly Toward Paper-Based Elections](https://www.governing.com/next/america-moves-decidedly-toward-paper-based-elections)

### 2.2 Post-Election Audit Landscape: Risk-Limiting Audits and the Adoption Gap

A paper record only protects election integrity if it is actually used to verify the electronic result. Post-election audits are the mechanism for that verification. The gold standard is the risk-limiting audit (RLA), a statistically rigorous method that samples ballots at a rate calibrated to the margin of victory — ensuring that, with high confidence, a wrong outcome cannot be certified without detection.

As of 2026, the national audit landscape is significantly better than it was a decade ago but still has major gaps:

**States with RLA in statute**: Colorado (the pioneer — first statewide RLA in 2017), Georgia, Nevada, Oregon, Virginia, Washington. Colorado's law requires an RLA for all elections; Georgia enacted an RLA requirement after its 2020 certification controversy.

**States with statutory pilot or phased RLA programs**: Indiana, Michigan, Maine (pilot after 2024 general, statewide beginning 2025). Texas is required to implement RLAs statewide after August 31, 2026 — specifically for races and measures voted on statewide — making 2026 the first Texas statewide election under this requirement.

**States with optional RLA authority**: California, New Jersey, Pennsylvania, Rhode Island, Ohio, Kentucky. In these states, state or local officials may conduct RLAs but are not required to do so.

**States without meaningful post-election audit requirements**: A significant portion of states conduct only fixed-percentage audits (typically 1-5% of precincts chosen at random), which are mathematically insufficient to detect manipulation in close races and do not scale to the margin of victory. The NCSL documents that audit requirements vary dramatically — some states require only a recount of machine results against machine results, which cannot detect a machine-level compromise.

The security gap in the audit landscape is not primarily about which states have paper ballots. It is about which states have the statistical rigor to actually catch a discrepancy if one exists. A state that uses paper ballots but audits only 1 percent of precincts with no risk-limiting methodology can produce paper ballots and still certify a manipulated outcome if the manipulation was contained to non-sampled precincts.

Sources: [NCSL: Risk-Limiting Audits](https://www.ncsl.org/elections-and-campaigns/risk-limiting-audits); [Verified Voting: Risk-Limiting Audits](https://verifiedvoting.org/audits/whatisrla/); [MIT Election Lab: Post-Election Audits](https://electionlab.mit.edu/research/post-election-audits); [Movement Advancement Project: Risk-Limiting Audits](https://www.lgbtmap.org/democracy-maps/risk_limiting_audits)

---

## Part 3: Voter Registration Database Security — ERIC, SAVE, and the Integrity Gap

### 3.1 The ERIC Architecture and the Nine-State Departure

The Electronic Registration Information Center (ERIC) is a nonprofit cooperative that enables member states to share voter registration data to identify voters who have moved, died, or are registered in multiple states. ERIC's data cross-matching reduces both voter roll error (which fuels bad-faith fraud claims) and fraud risk (which the same bad-faith claims allege). It is, by design, a cooperative security measure for voter database integrity.

Nine states have withdrawn from ERIC since 2022: Louisiana, Alabama, Missouri, Florida, West Virginia, Iowa, Ohio, Virginia, and Texas. The withdrawals were driven primarily by a Gateway Pundit disinformation campaign claiming ERIC was a Democratic voter registration operation — a claim without factual basis; ERIC also helped states identify inactive voters for removal, a conservative priority. The practical consequence of withdrawal is documented: states leaving ERIC without effective replacements have less accurate voter rolls, more outdated records, and greater vulnerability to both honest error and deliberate challenge campaigns based on that error.

As of February 2026, 25 states and the District of Columbia remain ERIC members. Virginia rejoined in March 2026 after Governor Abigail Spanberger signed an executive order restoring membership. New York enacted legislation in December 2025 requiring ERIC membership by July 31, 2026. Georgia — a critical competitive state — has been subject to ongoing legislative pressure to withdraw but has retained membership after a withdrawal bill failed to pass in 2025.

The pattern of ERIC departure is electorally correlated: most departing states are Republican-governed with low electoral competitiveness. But the damage to voter roll accuracy in those states creates a database integrity problem that is genuinely non-partisan: when a state's voter rolls are inaccurate, voters from any party may be wrongly challenged or removed.

The deeper security concern is architectural: ERIC's departure states have not built equivalent replacement systems. The Votebeat investigation into post-ERIC voter roll maintenance documented that GOP-led departing states are "struggling to create a new system" and encountering "obstacles and costs to replace data they need to clean voter rolls." Inaccurate voter rolls are the raw material of bad-faith challenge campaigns — including the SAVE-based challenge campaign documented in Domain E.

Sources: [Votebeat: States that left ERIC are struggling to create a new system](https://www.votebeat.org/2023/12/13/cleaning-voter-rolls-after-eric-election-security-voter-fraud/); [Brennan Center: States Cave to Conspiracy Theories and Leave Voter Data Cooperative, ERIC](https://www.brennancenter.org/our-work/analysis-opinion/states-cave-conspiracy-theories-and-leave-voter-data-cooperative-eric); [Wikipedia: Electronic Registration Information Center](https://en.wikipedia.org/wiki/Electronic_Registration_Information_Center)

### 3.2 SAVE System Integration Risks and the Database Weaponization Threat

The DHS Systematic Alien Verification for Entitlements (SAVE) program has been expanded under the Trump administration into a voter file verification system — documented in Domain E's Section 1.2. From a database security perspective, SAVE integration creates distinct risks beyond the voter suppression mechanics analyzed there.

When a state integrates its voter rolls with SAVE, it is connecting a state database to a federal database that has demonstrated an 81 percent false positive rate in the documented Missouri deployment — meaning the system incorrectly flags naturalized U.S. citizens as potential non-citizens at a rate that is statistically catastrophic for a verification system. More significantly, the data flow is bidirectional: the state shares its voter file with a federal agency that has no statutory election security mandate, no prohibition on sharing that data with political actors within the administration, and — following CISA's defunding — no independent federal oversight with election-security expertise.

A DOJ privacy officer resigned in April 2026 when the agency prepared to share voter data with DHS, citing data protection concerns. Internal DOJ documents revealed that officials planned the sharing earlier than publicly acknowledged. These facts establish that the SAVE voter file integration is not a neutral security measure — it is a data transfer from state election databases into a federal system that the administration controls and has used for political purposes.

States that have signed SAVE-based consent agreements with DOJ — primarily Republican-governed states — are exposing their voter rolls to a dual vulnerability: the false-positive flagging risk that will remove legitimate voters, and the data security risk that voter roll information now resides in a federal system controlled by officials with documented partisan interests in its use.

Sources: [NPR: DOJ prepares to share voter data with DHS, privacy officer resigns](https://www.npr.org/2026/04/03/nx-s1-5768455/privacy-doj-dhs-voter-data); [Brennan Center: Homeland Security's SAVE Program Exacerbates Risks to Voters](https://www.brennancenter.org/our-work/research-reports/homeland-securitys-save-program-exacerbates-risks-voters); [CNN: Trump building a massive voter database](https://www.cnn.com/2026/04/05/politics/trump-voter-database-election-fraud)

---

## Part 4: The Federal Support Collapse — What Was Lost and What Remains

### 4.1 CISA's Prior Contribution — Quantifying the Loss

CISA's election security program, built between 2017 and 2024, was the only national-level technical assistance and threat intelligence function for election infrastructure. The scale of what has been eliminated:

- 130 CISA staff fired in February 2025, including election security advisers and all staff focused on foreign influence and disinformation
- All election security activities halted "pending an internal review" in February 2025; review completed in March; findings withheld from public
- In 2023-2024 alone: over 700 cybersecurity assessments conducted for election jurisdictions; approximately 1,300 physical security assessments conducted at election offices, voting locations, and tabulation centers; 500 training sessions provided to election officials
- EI-ISAC (Election Infrastructure Information Sharing and Analysis Center) funding terminated — the network that provided real-time cyber threat sharing across election jurisdictions
- MS-ISAC cooperative agreement terminated September 30, 2025 — forcing the multi-state cybersecurity sharing network to convert to paid membership
- Critical Infrastructure Partnership Advisory Council dissolved
- FY27 budget: proposes eliminating CISA's election security program from the baseline entirely — 14 positions, $39.6 million

The Arizona case is the clearest documentation of what the trust destruction means operationally. Secretary of State Adrian Fontes declined to notify CISA of a suspected Iranian cyberattack on his state's election website in summer 2025, stating he "just can't trust that this administration takes election security seriously." Pennsylvania Secretary of State Al Schmidt warned of "serious consequences" from CISA rollbacks. Maine Secretary of State Shenna Bellows describes the trust as "absolutely demolished." These are not partisan officials venting — they are the people responsible for administering elections in battleground states describing their operating environment.

Sources: [Brennan Center: How the Federal Government Is Undermining Election Security](https://www.brennancenter.org/our-work/research-reports/how-federal-government-undermining-election-security); [Votebeat: Election officials say trust with CISA is broken](https://www.votebeat.org/2026/01/15/cisa-election-security-trust-broken-trump-chris-krebs-denise-merrill/); [Nextgov: Federal drawdown of election support 'destroyed' ongoing relationships](https://www.nextgov.com/cybersecurity/2026/04/federal-drawdown-election-support-destroyed-ongoing-relationships-experts-say/413181/)

### 4.2 MS-ISAC Transition: The Paid Membership Gap

MS-ISAC, operated by the Center for Internet Security (CIS), provides 24/7 security operations center monitoring, incident response coordination, vulnerability scanning, and threat intelligence sharing to state and local government entities. It was previously free to state and local governments under the CISA cooperative agreement. As of October 1, 2025, it operates on a paid membership model.

The transition pricing is tiered by operating budget, starting at approximately $1,495 per year for small districts and scaling into tens of thousands for larger counties and states. As of the most recent reporting, 11 states have signed up for statewide MS-ISAC memberships that cover state agencies and eligible local governments — including Texas, Kansas, and Mississippi.

The arithmetic of the gap is stark: 11 states with paid statewide coverage out of 50 means that 39 states and their thousands of counties are either paying individually (at higher per-unit cost), relying on reduced state-level substitutes, or going without. The states with the most competitive 2026 Senate and House races — Arizona, Georgia, Michigan, Nevada, Pennsylvania, Wisconsin — are not among the documented early adopters of paid MS-ISAC statewide coverage, which means county-level election offices in those states are navigating 2026 without the national threat intelligence network that CISA previously provided.

Sources: [GovTech: Eleven States Have Signed Up for MS-ISAC's New Paid Membership](https://www.govtech.com/security/eleven-states-have-signed-up-for-ms-isacs-new-paid-membership); [StateTech: States Step Up as MS-ISAC Moves to Paid Model](https://statetechmagazine.com/article/2026/02/states-step-ms-isac-moves-paid-model-after-federal-funding-ends); [StateScoop: CISA confirms ending MS-ISAC support](https://statescoop.com/cisa-confirms-its-ending-ms-isac-support/)

### 4.3 EAC Funding: The $45 Million Inadequacy

Congress appropriated $45 million in FY26 for election security grants through the EAC — approximately $900,000 per state. For context: the Brennan Center's analysis of voting machine replacement costs documents that comprehensive equipment replacement across a mid-size state's counties costs many times this amount. The Brennan Center's survey found that 87 percent of local election officials believe state and local government must provide additional resources to compensate for federal reductions, and 75 percent have not received them.

The EAC's FY26 budget justification, published April 2026, confirms that the President's FY27 budget requests no additional election security grant funding — zero new appropriations beyond the HAVA baseline. The progression — $100 million in emergency election security grants in 2018 following the 2016 interference, down to $15 million in FY25, $45 million in FY26, and $0 new requested in FY27 — represents a deliberate withdrawal of federal election security investment precisely as cybersecurity threats are documented to be increasing.

Sources: [EAC: Election Security Grant](https://www.eac.gov/grants/election-security-funds); [EAC: FY 2027 Congressional Budget Justification Report](https://www.eac.gov/sites/default/files/2026-04/EAC_FY_2027_Congressional_Budget_Justification_Report_FINAL.pdf)

---

## Part 5: Election Official Security — Turnover, Training Gaps, and Insider Threats

### 5.1 The Turnover Crisis and Its Security Implications

The structural vulnerability of election administration is not exclusively digital — it is human. Issue One's tracking, cited in Domain E, documents that 50 percent of chief local election officials in Western states have left their positions since 2020. The Brennan Center's 2026 survey of local election officials finds:

- 36 percent of officials reported experiencing harassment or abuse; 16 percent reported being threatened because of their job
- Over 200 bomb threats occurred during the 2024 election cycle
- Nearly 1 in 4 officials are concerned about being assaulted at home or at work
- The 2025 survey found 38 percent of officials experienced threats or harassment — the 2026 figure of 36 percent represents marginal improvement, not resolution

Turnover has direct security implications beyond institutional knowledge loss. New election officials — 4 in 10 local offices will be run by people who have never administered a national election — are the highest-risk targets for AI-enhanced social engineering attacks. CISA specifically identified election workers as a priority social engineering target before its election security program was eliminated. The attack vector is straightforward: an adversary with publicly available information about a new county election administrator (social media profiles, employer records, professional associations) can craft a highly credible spear-phishing email that appears to come from a trusted source — a Secretary of State's office, a voting system vendor, a peer election official — and uses convincing personal details to induce the administrator to click a malicious link or share credentials.

CISA's training program, which conducted 500 sessions annually, specifically addressed this attack surface. That program no longer exists. The combination of elevated threat environment and the elimination of the federal training program creates a security gap that is entirely predictable and partially preventable.

### 5.2 Insider Threat Vulnerabilities

CISA's prior joint documentation with DHS, FBI, and EAC on election security insider threats identified several risk scenarios: election officials accessing voter data for non-authorized purposes; poll workers providing unauthorized access to voting systems; officials with financial relationships to partisan interests affecting equipment or process decisions; and officials with ideological commitments to specific electoral outcomes affecting how they administer certification and canvassing.

The Colorado 2021 case — in which an elected county official allowed an unauthorized individual to photograph and publish voting machine passwords and copy hard drives — is the clearest documented insider threat incident. The official was barred from supervising future elections. The structural lesson is that insider threat mitigation requires credential vetting, access controls, and clear chain-of-custody protocols that many county-level election offices — particularly those run by newly hired administrators without professional election background — do not have in place.

The concentration of election denier candidates seeking certification authority positions (documented in Part 6 below) creates a new category of insider threat that CISA's prior framework did not address: officials who may not attempt to alter technical systems but who may manipulate procedural decisions — which ballots to accept, how to adjudicate challenged ballots, whether to certify results — in ways that serve partisan rather than legal outcomes.

Sources: [CISA: Election Security Risk in Focus: Insider Threats](https://www.cisa.gov/resources-tools/training/election-security-risk-focus-insider-threats); [Brennan Center: Survey Finds Election Officials Remain Concerned About Safety](https://www.brennancenter.org/our-work/analysis-opinion/survey-finds-election-officials-remain-concerned-about-safety-lack); [Bridging Divides Initiative: Analysis of Threat and Harassment Data for 2024 Election](https://bridgingdivides.princeton.edu/analysis-threat-and-harassment-data-2024-election)

### 5.3 International Benchmark: Australia's Electoral Integrity Assurance Taskforce

Australia's Australian Electoral Commission (AEC) provides a functional model for multi-agency election security coordination that does not depend on a single centralized cybersecurity agency. The AEC's Electoral Integrity Assurance Taskforce (EIAT) coordinates the AEC with the Australian Signals Directorate, the Australian Cyber Security Centre, ASIO, the Australian Federal Police, and the Department of Home Affairs — creating a distributed security model where the loss of any single agency's election security function does not eliminate the national security posture.

For the 2025 federal election (April 28, 2025), the AEC engaged an independent auditor to conduct a data assurance process comparing system-captured data against actual ballot papers. Independent assessors accredited by the Australian Signals Directorate conducted security risk assessments of all computer systems used in the Senate count, with written recommendations that the AEC accepted and implemented. Australia uses optical scanning for Senate ballots with human operator verification of each captured preference — a hybrid approach that combines speed with auditability.

The AEC's published January 2025 Election Security Environment Overview identified four threat vectors: foreign interference, physical security, cybersecurity, and misinformation and disinformation. Publishing this assessment publicly — rather than withholding it, as CISA did with its March 2025 internal review — is itself a security measure: it informs local officials, civil society, and the public of known threats and enables distributed threat response.

The core Australian institutional design difference is independence: the Chief Electoral Officer is a statutory officer with security of tenure, not an executive branch appointee subject to political direction. This independence is codified in the Commonwealth Electoral Act and extends to the Electoral Integrity Commissioner (a separate office within Elections Australia's structure). No equivalent statutory independence exists for the United States election security infrastructure: CISA's director serves at the pleasure of the president, a fact demonstrated when the Trump administration removed Chris Krebs in November 2020 for contradicting the president's election fraud claims.

Sources: [AEC: Electoral Integrity Assurance Taskforce](https://www.aec.gov.au/about_aec/electoral-integrity.htm); [AEC: Election Security Environment Overview (January 2025)](https://www.aec.gov.au/About_AEC/files/eiat/election-security-environment-overview.pdf); [AEC: Central Senate Scrutiny — security and integrity](https://www.aec.gov.au/Voting/counting/security-integrity.htm)

---

## Part 6: Supply Chain, Chain-of-Custody, and Certification Season Vulnerabilities

### 6.1 Supply Chain Security Gaps

The voting system supply chain encompasses software development, hardware manufacturing, firmware updates, ballot printing, equipment transport, storage, and election-night reporting — at every stage of which an adversary could introduce a compromise. The CIS published a guide on election system supply chain risk assessment in 2024 identifying the major risk nodes; that guidance was developed under the CISA cooperative agreement that was subsequently terminated.

Key documented supply chain vulnerabilities include:

**Software updates**: Voting machines receive firmware and software updates between election cycles. The distribution of those updates — from vendor to state certification authority to county election office — involves multiple handoffs that can be interdicted. The 2022 CISA advisory on Dominion ImageCast X documented that the vendor's software update pathway could be exploited to install malicious software on deployed machines. The advisory required remediation, but the monitoring function that would verify remediation is deployed correctly across all affected jurisdictions no longer exists.

**Ballot printing**: Ballots are printed by commercial contractors, transported to election offices, stored, and issued to polling locations. A 2024 Cambria County, Pennsylvania incident in which ES&S machines had scanning errors due to a ballot printing error illustrates the operational risk at the ballot-printer interface: the failure was not malicious, but the same interface is a potential attack surface. Chain-of-custody protocols for ballot paper stock from printing through issuance vary significantly across jurisdictions.

**Election night reporting**: Unofficial election night results are transmitted electronically from county tabulation systems to state reporting systems, creating a network-connected pathway that is distinct from the physical paper record. Attacks on election night reporting systems — including denial-of-service attacks that delay result transmission, or manipulation of preliminary result displays — do not change certified results but can create the appearance of anomalies that fuel post-election disputes.

**E-pollbook supply chain**: Electronic pollbooks — the check-in systems used at polling locations to verify voter registration — are increasingly network-connected on election day and represent an attack surface that, if compromised, could delay or disrupt voter check-in at scale. KnowInk, the nation's most widely used e-pollbook vendor, was founded by Scott Leiendecker, who has now also acquired Liberty Vote (formerly Dominion). This concentration of ownership across both e-pollbooks and voting machines in a single individual is a supply chain risk factor that has not been independently assessed.

Sources: [StateScoop: New guide on election system supply chains aids risk evaluations](https://statescoop.com/center-internet-security-election-security-supply-chain/); [Security Magazine: Guarding Democracy: The software supply chain's role in elections](https://www.securitymagazine.com/articles/101133-guarding-democracy-the-software-supply-chains-role-in-elections/); [Supply Chain Dive: US elections: Just another flawed supply chain?](https://www.supplychaindive.com/news/supply-chain-elections/541190/)

### 6.2 The 2026 Certification Season — Convergence Point

The certification season for the November 2026 general election runs from August 7 (when the NVRA 90-day quiet period begins, prohibiting systematic voter purges) through October 31, 2026 (the practical deadline for most state canvassing and certification processes). This window is the convergence point of every vulnerability documented in this analysis.

**August 7–October 31, 2026** is simultaneously:

1. The period when states complete their primary canvassing and must certify primary results — creating early-season certification pressure before the general election
2. The period when 26 states conducting secretary of state elections produce results that determine who will administer the November general election and who will certify House and Senate results
3. The window during which the NVRA quiet period prohibits systematic voter purges but not individual challenges — creating maximum vulnerability to SAVE-based individual challenge campaigns targeting NVRA-compliant voters
4. The period following the expected June-July SCOTUS ruling in *Watson v. RNC* on mail ballot grace periods — when states must implement whatever the Court decides about mail ballot receipt deadlines with weeks, not years, to reconstruct procedures

The 2026 midterms will determine who oversees the 2028 presidential election in 29 states. As of May 2026, at least 53 election-denying candidates are running for offices with direct certification authority — verified by States United's ElectionDeniers.org tracking database. In 23 states including five presidential swing states, candidates who have denied election results are running for offices that will directly certify future elections.

The swing state breakdown is particularly acute:

**Arizona**: Three election-denying candidates are running for all three critical statewide positions — Secretary of State, Governor, and Attorney General — according to States United's analysis. Democratic incumbent Adrian Fontes is defending his Secretary of State seat against Alexander Kolodin, who was involved in the legal effort to overturn the 2020 election.

**Georgia**: An open Secretary of State seat with Georgia State Rep. Vernon Jones, who claimed the 2020 election was stolen, among the Republican primary candidates. Democratic candidates include former Judge Penny Brown Reynolds and Fulton County Commissioner Dana Barrett.

**Michigan**: Anthony Forlini (Republican, Macomb County Clerk) challenges Garlin Gilchrist (Democrat, Lt. Governor). Control of this seat determines election administration in one of the two states that decided the 2020 presidential election by fewer than 160,000 votes combined.

**Nevada**: Jim Marchant, a documented election denier who ran an unsuccessful 2022 campaign on election fraud claims, is among the Republican primary candidates for Secretary of State.

**Wisconsin**: A Senate race, not a Secretary of State race, but Wisconsin's election administration structure vests significant power in the bipartisan Wisconsin Elections Commission, whose partisan composition will be affected by legislative elections that November.

Sources: [Votebeat: All the secretary of state elections to watch in 2026](https://www.votebeat.org/national/2026/04/20/2026-midterms-secretary-of-state-top-election-official-election-preview/); [NPR: In many states, election-denying candidates are running to control voting](https://www.npr.org/2026/05/04/nx-s1-5803149/election-denial-2026-candidates); [States United: NEW RESEARCH: States United Launches ElectionDeniers.org Tracking for 2026](https://statesunited.org/press-release-2026-election-deniers/); [Common Dreams: Analysis Identifies 50+ Election Deniers Vying to Oversee Voting Across US](https://www.commondreams.org/news/election-deniers-2026-midterms)

---

## Part 7: Democratic Precedents — Models for Structural Election Security

### 7.1 Canada: Independent Administration and Multi-Agency Security

Canada's federal election security model provides the clearest international contrast to the U.S. structural fragility. The Canada Elections Act (S.C. 2000, c. 9) establishes Elections Canada as a permanent independent body under the authority of the Chief Electoral Officer — who is an officer of Parliament, not of the executive branch, with security of tenure and operational independence that cannot be terminated by the Prime Minister. The Commissioner of Canada Elections is a separate independent officer responsible for enforcement.

For the April 28, 2025 federal election (Canada's 45th), the security architecture involved five agencies: the Communications Security Establishment (signals intelligence and cyber defense), the Canadian Centre for Cyber Security (technical protection), CSIS (foreign intelligence), the RCMP (physical security), and Public Safety Canada (coordination). No single executive branch department controlled the security posture. The June 2024 Act respecting countering foreign interference added legislative protections specifically for electoral integrity against foreign influence operations.

This distributed multi-agency model with statutory independence at its center is directly responsive to the U.S. failure mode: when a single agency (CISA) that reports to a single executive (the president) is the sole federal election security node, a president who benefits from reduced election security can eliminate that function through administrative action alone. Canada's model requires legislative action to eliminate any individual security function because the functions are distributed across multiple statutory agencies rather than consolidated in a single discretionary program.

Sources: [Canada Elections Act (SC 2000, c. 9)](https://laws-lois.justice.gc.ca/eng/acts/E-2.01/); [Elections Canada: Election integrity and security](https://www.elections.ca/content2.aspx?section=int&document=index&lang=e); [Elections Canada: Safeguards That Protect the Federal Electoral Process](https://elections.ca/content.aspx?dir=pre&document=apr0225&lang=e&section=med); [Canada.ca: Protecting Canada's general elections](https://www.canada.ca/en/democratic-institutions/services/protecting-canada-general-election-2025.html)

### 7.2 Germany: Paper Ballots, Public Counting, and Independent Administration

Germany's 2025 Bundestagswahl (February 23, 2025) was conducted using exclusively hand-marked paper ballots counted publicly by citizen volunteers (Wahlhelfer) in approximately 90,000 polling stations. There are no voting machines in German federal elections. The Federal Returning Officer (Bundeswahlleiterin), Ruth Brand, is an independent statutory officer — not an executive appointee. The Federal Electoral Law (Bundeswahlgesetz) is a parliamentary statute that cannot be modified by executive action.

For the 2025 election, the BSI (Federal Office for Information Security) developed a joint federal-state baseline protection profile for election night IT systems, updated specifically for 2025, that was published and available to all state-level returning officers. Election results are transmitted electronically on election night but calculated definitively from physical ballot papers — a hybrid approach that ensures any cyberattack on the reporting system cannot change the certified outcome.

Germany's model is deliberately redundant: the electronic result is a preliminary estimate; the paper count is definitive. This design embeds auditability into the constitutional architecture rather than treating it as an add-on security measure. The result is a system in which "the final election result will be calculated based on actual ballot papers and cannot be manipulated by cyberattacks."

The German federal model does not translate directly to U.S. administration, which is constitutionally state-administered and operationally county-administered. But the principle — that the definitive result must be grounded in something physically verifiable independent of software — is precisely the principle that U.S. post-election auditing is designed to implement, and that the RLA adoption gap (Part 2.2 above) currently undermines.

Sources: [Bundeswahlleiterin: 2025 Bundestagswahl](https://www.bundeswahlleiterin.de/en/bundestagswahlen/2025.html); [BMI: Protecting the Bundestag elections from hybrid threats and disinformation](https://www.bmi.bund.de/SharedDocs/schwerpunkte/EN/disinformation-election/disinformation-election-artikel.html); [Deutschland.de: 2025 Bundestag elections — Federal Returning Officer Ruth Brand](https://www.deutschland.de/en/topic/politics/bundestag-election-2025-federal-returning-officer-ruth-brand-electoral-law)

### 7.3 OSCE Findings: International Standards and U.S. Gaps

The OSCE/ODIHR final report on the 2024 U.S. general election (April 2025) provided 31 recommendations for aligning U.S. election practices with international democratic standards. The report found that "threats, harassment, and violence against election administrators were a cause for serious concern and made recruiting election workers a challenge." It noted that the legal framework has remained largely unchanged since the last ODIHR observation, "leaving most previous ODIHR recommendations unaddressed."

International election observers consistently identify three structural U.S. gaps: (1) the absence of a national independent election administration body with statutory authority; (2) the decentralized administration structure that creates security quality variation across thousands of county offices; and (3) the insufficient legal protections for election officials against threats and interference. All three are structural problems that predate the current administration's actions but that the current administration's actions have made acutely dangerous in the 2026 window.

Sources: [OSCE: USA 2024 general elections ODIHR observation mission final report](https://www.osce.org/odihr/589239); [OSCE Parliamentary Assembly: US elections showed resilience with well-run process in highly polarized campaign](https://www.oscepa.org/en/news-a-media/press-releases/press-2024/us-elections-showed-resilience-of-democratic-institutions-with-a-well-run-process-in-a-highly-polarized-campaign-international-observers-say)

---

## Part 8: Structural Reform Priorities and Advocacy Windows

### 8.1 Immediate Priorities (May–June 15, 2026)

**1. State legislative action on election security appropriations — targeting the county level.**
The Brennan Center's 2026 survey documents that 75 percent of local election officials have not received additional resources from state or local government despite the federal withdrawal. The gap is at the county and municipal level, not at the state capital. Legislative sessions still open in several competitive states should pass emergency appropriations targeted at county-level election security: endpoint detection and response (EDR) software deployment, MS-ISAC paid membership, and independent security assessments of tabulation infrastructure. Georgia's legislative session ended without action — documenting the failure for electoral accountability is itself an advocacy action that frames the November contest.

**2. NASS bloc MS-ISAC membership arrangement.**
The National Association of Secretaries of State should negotiate a bloc membership arrangement covering all competitive-state secretaries of state who have not yet converted to paid MS-ISAC membership. A bloc purchase reduces per-state cost and ensures that the core competitive states have the minimum threat-intelligence sharing function that CISA previously provided for free. The 11 states already enrolled demonstrate that the model is operationally feasible.

**3. Opposition to FY27 election security zero-out.**
Civil society organizations and state officials should file coordinated opposition to the FY27 budget's elimination of CISA's election security program with House and Senate Appropriations Committees. The framing: eliminating election security infrastructure while documented adversaries (Russia, China, Iran) are conducting ongoing reconnaissance of U.S. election systems, and while the U.S. is engaged in active military confrontation with Iran (documented targeting U.S. infrastructure), constitutes a national security vulnerability. The $39.6 million is a rounding error in the federal budget; its elimination is a policy choice, not a fiscal necessity.

**4. CISA state election security assessment monitoring (June 15, 2026 window).**
The administration's internal CISA review — completed in March 2025 but withheld from public release — may produce a state-level election security assessment in the June 2026 window. If released, civil society organizations should immediately compare its findings to the Brennan Center's independent assessment and document any gaps, suppressed findings, or politically motivated characterizations. If not released, the withholding itself is an advocacy subject.

### 8.2 Pre-Certification Season (July–August 7, 2026)

**5. Independent security assessments in Arizona, Georgia, Michigan, Nevada, Pennsylvania, and Wisconsin.**
The six states combining electoral competitiveness with documented security capacity gaps should receive independent security assessments of their election infrastructure — conducted by universities (MIT Lincoln Lab, Stanford Internet Observatory, Georgia Tech GTRI), civil society organizations (Verified Voting, CDT), or state-hired contractors — before the certification season opens. The assessments should cover: tabulation system software version and patch status, EDR deployment at county offices, chain-of-custody protocols for ballot printing and storage, and MS-ISAC enrollment status at the county level.

**6. RLA legislation in non-adopting competitive states.**
States that have paper ballots but lack risk-limiting audit requirements — and are currently in legislative session or have special session authority — should enact RLA requirements before November 2026. The statistical inadequacy of fixed-percentage audits in close races is well-documented; the marginal cost of enacting an RLA requirement is legislative, not appropriations-dependent.

**7. Voter registration accuracy emergency actions.**
In states that have withdrawn from ERIC without effective replacement systems, civil society organizations should provide pro bono voter roll accuracy assistance — helping voters verify their registration status and correct errors before the NVRA quiet period begins August 7. After August 7, systematic corrections become legally constrained; individual voter registration corrections remain available but require proactive outreach.

### 8.3 Certification Season (August 7–October 31, 2026)

**8. Secretary of State race support in competitive states.**
The candidate slate in Arizona, Georgia, Michigan, and Nevada creates a direct structural security risk if election-denying candidates win Secretary of State races and then administer the certification of November 2026 results. Civil society organizations focused on election administration integrity should provide maximum support to candidates committed to lawful certification — including election law training, chain-of-custody protocol resources, and legal assistance for certification disputes.

**9. Pre-certification legal preparation.**
Democracy Docket, the Brennan Center's legal team, and state AG offices in competitive states should prepare pre-certification legal filings for anticipated certification refusal scenarios — based on the post-2020 pattern in which more than 30 local officials refused to certify results across nine states. Pre-drafted TRO applications and mandamus petitions, tailored to each state's certification statute, will enable faster judicial response if refusals materialize.

### 8.4 Medium-Term Structural Reform (2027 Legislative Session)

**10. Statutory independence for federal election security coordination.**
The post-CISA lesson is that a voluntary program dependent on executive goodwill is constitutionally insufficient. Congress should enact a statute creating an independent Election Security Coordinator with security of tenure, a statutory mandate to provide cybersecurity assessments and threat intelligence to state election offices, and an appropriations baseline that is not subject to annual zeroing. The Canadian model (statutory independence for the Chief Electoral Officer) and the Australian model (multi-agency coordination through an independent AEC) both demonstrate that this structural design is operationally feasible.

**11. Mandatory minimum security standards for HAVA-funded jurisdictions.**
The current VVSG model is voluntary. Any jurisdiction receiving HAVA funds should be required, as a condition of funding, to deploy paper-verified voting systems and to conduct post-election audits meeting minimum statistical sufficiency standards. Mandatory minimum standards would not require eliminating state certification authority — they would condition federal financial assistance on meeting federal security requirements, a model with established constitutional precedent.

**12. Interstate election security compact.**
The constitutional gap — the Elections Clause gives states administration authority while cybersecurity requires national coordination — can be addressed through an interstate compact (analogous to the Driver License Compact or the Emergency Management Assistance Compact) creating binding cross-state obligations for election security information sharing. An interstate compact does not require federal executive involvement; it requires only state legislative enactment and congressional consent. This pathway creates a coordination mechanism resilient to federal executive hostility.

**13. ERIC federal backstop legislation.**
Congress should enact legislation creating a federal backstop for interstate voter registration data sharing — a statutory mechanism that preserves the ERIC cooperative model but does not depend on voluntary state participation alone. Federal funding for interstate voter roll accuracy, conditioned on compliance with non-partisan data standards, would restore the incentive structure that made ERIC effective while insulating the program from the disinformation campaigns that drove Republican state departures.

Sources: [Brennan Center: A State Agenda for Election Security and Resiliency](https://www.brennancenter.org/our-work/policy-solutions/state-agenda-election-security-and-resiliency); [Brennan Center: How State Legislators Can Protect Election Integrity and Security](https://www.brennancenter.org/our-work/research-reports/how-state-legislators-can-protect-election-integrity-and-security); [Votebeat: 2026 midterms expert survey on election fears](https://www.votebeat.org/national/2026/04/17/2026-election-expert-survey-troops-polling-places-seize-ballots-voting-fraud/)

---

## Conclusion: The Structural Argument

State election security in 2026 faces two categories of vulnerability that are analytically distinct but operationally inseparable.

The first category is structural and pre-existing: vendor concentration without source code transparency; post-election audit standards that are sufficient in some states and inadequate in others; a voter registration database ecosystem fragmented by ERIC departures and integration with a federally-controlled system that has documented data integrity failures; an election official workforce under sustained threat with high turnover and insufficient training; and supply chain security gaps that no individual county can address.

The second category is politically induced and acute: the deliberate elimination of the federal security coordination function that compensated for structural state-level weaknesses; the conversion of the voter file verification system into a political tool; the positioning of election-denying candidates for certification authority positions in the states whose results will determine congressional control; and the proposed permanent elimination of election security from the federal appropriations baseline.

What makes 2026 distinctively dangerous is the interaction between these two categories. The structural vulnerabilities were manageable when a federal coordination function existed to monitor threats, share intelligence, and assist the most vulnerable jurisdictions. Without that function, the structural vulnerabilities are not merely unmitigated — they are unknown, because the assessment capacity that would identify specific weaknesses has been eliminated along with the remediation capacity.

The international comparison — Canada's multi-agency independent model, Germany's paper-first auditable design, Australia's independent AEC with statutory security tenure — demonstrates that the United States constitutional design does not require its current structural fragility. What it requires is the political will to enact statutory independence for election security functions, to mandate minimum audit standards as a condition of federal funding, and to create the interstate coordination mechanisms that compensate for the constitutional architecture's silence on national election security.

That political will is a November 2026 midterm question.

---

## Consolidated Source List

1. [ProPublica: The Market for Voting Machines Is Broken](https://www.propublica.org/article/the-market-for-voting-machines-is-broken-this-company-has-thrived-in-it)
2. [Votebeat: After Trump attacks, Dominion is forging ahead as Liberty Vote](https://www.votebeat.org/2026/02/12/dominion-liberty-vote-scott-leiendecker-voting-systems-machines-election-equipment/)
3. [Spotlight PA: Dominion Voting Systems sold to GOP official](https://www.spotlightpa.org/news/2025/10/dominion-voting-systems-sale-liberty-vote-election-security-elections/)
4. [Axios: Dominion Voting sold to company run by ex-GOP election official](https://www.axios.com/2025/10/09/dominion-voting-machines-sold-elections)
5. [CNN: Former GOP election official buys Dominion Voting Systems](https://www.cnn.com/2025/10/09/politics/dominion-voting-systems-bought-election-ballots)
6. [CISA: Vulnerabilities Affecting Dominion Voting Systems ImageCast X](https://www.cisa.gov/news-events/ics-advisories/icsa-22-154-01)
7. [Nextgov: Trump proposes cutting CISA election security program in FY27 budget](https://www.nextgov.com/cybersecurity/2026/04/trump-proposes-cutting-cisa-election-security-program-fy27-budget/412672/)
8. [EAC: Election Security Grant](https://www.eac.gov/grants/election-security-funds)
9. [EAC: FY 2027 Congressional Budget Justification Report](https://www.eac.gov/sites/default/files/2026-04/EAC_FY_2027_Congressional_Budget_Justification_Report_FINAL.pdf)
10. [Brennan Center: How the Federal Government Is Undermining Election Security](https://www.brennancenter.org/our-work/research-reports/how-federal-government-undermining-election-security)
11. [Brennan Center: Survey Finds Election Officials Remain Concerned About Safety](https://www.brennancenter.org/our-work/analysis-opinion/survey-finds-election-officials-remain-concerned-about-safety-lack)
12. [Brennan Center: A State Agenda for Election Security and Resiliency](https://www.brennancenter.org/our-work/policy-solutions/state-agenda-election-security-and-resiliency)
13. [Brennan Center: How State Legislators Can Protect Election Integrity and Security](https://www.brennancenter.org/our-work/research-reports/how-state-legislators-can-protect-election-integrity-and-security)
14. [Brennan Center: Homeland Security's SAVE Program Exacerbates Risks to Voters](https://www.brennancenter.org/our-work/research-reports/homeland-securitys-save-program-exacerbates-risks-voters)
15. [Brennan Center: Some Good News for Donald Trump: We Already Use Paper Ballots](https://www.brennancenter.org/our-work/analysis-opinion/some-good-news-donald-trump-we-already-use-paper-ballots)
16. [Votebeat: Election officials say trust with CISA is broken](https://www.votebeat.org/2026/01/15/cisa-election-security-trust-broken-trump-chris-krebs-denise-merrill/)
17. [Votebeat: CISA halts support for states on election security](https://www.votebeat.org/2025/03/11/cisa-ends-support-election-security-nass-nased/)
18. [Votebeat: All the secretary of state elections to watch in 2026](https://www.votebeat.org/national/2026/04/20/2026-midterms-secretary-of-state-top-election-official-election-preview/)
19. [Nextgov: Federal drawdown of election support 'destroyed' ongoing relationships](https://www.nextgov.com/cybersecurity/2026/04/federal-drawdown-election-support-destroyed-ongoing-relationships-experts-say/413181/)
20. [GovTech: Eleven States Have Signed Up for MS-ISAC's New Paid Membership](https://www.govtech.com/security/eleven-states-have-signed-up-for-ms-isacs-new-paid-membership)
21. [StateTech: States Step Up as MS-ISAC Moves to Paid Model](https://statetechmagazine.com/article/2026/02/states-step-ms-isac-moves-paid-model-after-federal-funding-ends)
22. [NCSL: Risk-Limiting Audits](https://www.ncsl.org/elections-and-campaigns/risk-limiting-audits)
23. [Verified Voting: Risk-Limiting Audits](https://verifiedvoting.org/audits/whatisrla/)
24. [Votebeat: States that left ERIC are struggling to create a new system](https://www.votebeat.org/2023/12/13/cleaning-voter-rolls-after-eric-election-security-voter-fraud/)
25. [Brennan Center: States Cave to Conspiracy Theories and Leave Voter Data Cooperative, ERIC](https://www.brennancenter.org/our-work/analysis-opinion/states-cave-conspiracy-theories-and-leave-voter-data-cooperative-eric)
26. [NPR: DOJ prepares to share voter data with DHS, privacy officer resigns](https://www.npr.org/2026/04/03/nx-s1-5768455/privacy-doj-dhs-voter-data)
27. [CNN: Trump building a massive voter database](https://www.cnn.com/2026/04/05/politics/trump-voter-database-election-fraud)
28. [CISA: Election Security Risk in Focus: Insider Threats](https://www.cisa.gov/resources-tools/training/election-security-risk-focus-insider-threats)
29. [NPR: In many states, election-denying candidates are running to control voting](https://www.npr.org/2026/05/04/nx-s1-5803149/election-denial-2026-candidates)
30. [States United: ElectionDeniers.org Tracking for 2026](https://statesunited.org/press-release-2026-election-deniers/)
31. [AEC: Electoral Integrity Assurance Taskforce](https://www.aec.gov.au/about_aec/electoral-integrity.htm)
32. [AEC: Election Security Environment Overview (January 2025)](https://www.aec.gov.au/About_AEC/files/eiat/election-security-environment-overview.pdf)
33. [AEC: Central Senate Scrutiny — security and integrity](https://www.aec.gov.au/Voting/counting/security-integrity.htm)
34. [Canada Elections Act (SC 2000, c. 9)](https://laws-lois.justice.gc.ca/eng/acts/E-2.01/)
35. [Elections Canada: Election integrity and security](https://www.elections.ca/content2.aspx?section=int&document=index&lang=e)
36. [Canada.ca: Protecting Canada's general elections](https://www.canada.ca/en/democratic-institutions/services/protecting-canada-general-election-2025.html)
37. [Bundeswahlleiterin: 2025 Bundestagswahl](https://www.bundeswahlleiterin.de/en/bundestagswahlen/2025.html)
38. [BMI: Protecting the Bundestag elections from hybrid threats](https://www.bmi.bund.de/SharedDocs/schwerpunkte/EN/disinformation-election/disinformation-election-artikel.html)
39. [OSCE: USA 2024 general elections ODIHR observation mission final report](https://www.osce.org/odihr/589239)
40. [StateScoop: New guide on election system supply chains aids risk evaluations](https://statescoop.com/center-internet-security-election-security-supply-chain/)
41. [TechCrunch: Trump administration plans to cut CISA budget by $700 million](https://techcrunch.com/2026/04/07/cisa-budget-cuts-700-million-cybersecurity-agency-trump/)
42. [GovTech: Despite Risks, Some States Still Use Paperless Voting Machines](https://www.govtech.com/elections/despite-risks-some-states-still-use-paperless-voting-machines.html)
43. [Governing: America Moves Decidedly Toward Paper-Based Elections](https://www.governing.com/next/america-moves-decidedly-toward-paper-based-elections)

---

*Domain 37b research complete. Production-ready. Cross-referenced against Domain 37, Domain E, and existing Domain 37b scope document (April 2026 update).*
*This document should be distributed to: election law organizations, state Secretaries of State networks, state AGs, election security civil society (Verified Voting, Brennan Center, CDT, Common Cause).*
