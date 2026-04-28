---
title: "Domain 37b: State Election Security Coordination — Post-CISA Architecture and the 2026 Vulnerability Gap"
scope_type: "Domain 37 expansion — election-integrity cluster"
created: 2026-04-27
session: "Phase 2 expansion"
status: "Scope document — ready for full research"
priority: "High — 2026 midterm security window closing; state-level coordination infrastructure needs documentation now"
parent_domain: "Domain 37 (Federal Executive Interference in 2026 Midterms)"
cross_domain:
  - "Domain 21 (Data Privacy and Digital Surveillance)"
  - "Domain 26 (Government Accountability and Institutional Resilience)"
  - "Domain 33 (State Legislative Autocratization)"
  - "Domain 36 (AI Governance and Algorithmic Accountability)"
  - "Domain 37 (Federal Executive Interference in 2026 Midterms)"
---

# Domain 37b: State Election Security Coordination — Post-CISA Architecture and the 2026 Vulnerability Gap

**Scope document — April 27, 2026**

---

## Why This Domain Is Needed

Domain 37 documents the destruction of the federal election security infrastructure — CISA's $700 million budget cut, the elimination of the EI-ISAC (Election Infrastructure Information Sharing and Analysis Center), the termination of MS-ISAC cooperative agreement funding, and the departure of career cybersecurity staff. It treats CISA's dismantlement as an interference mechanism (which it is), but does not document what states have done to fill the resulting vacuum, what coordination gaps remain, or what a viable state-level security architecture looks like in the absence of federal support.

Domain 37b fills that gap. The research question is not "what has the federal government destroyed?" — that is Domain 37's territory — but "what can states credibly build in the 6-month window before November 2026, and what are the specific vulnerabilities that remain regardless of state effort?"

This is actionable for two reasons. First, election-protection organizations can direct resources toward the highest-vulnerability states if the capacity gaps are mapped. Second, state officials need a framework for rapidly building the minimum viable security posture given time and resource constraints — and such a framework does not currently exist in the public literature.

---

## What the Research Has Established

Several facts are already confirmed through prior research (Domain 37, primary source verification):

**Services lost**: CISA previously provided 1,300 physical security assessments, 700 cybersecurity assessments, and 500 training sessions to election offices since 2023. It funded EI-ISAC, which served as the national incident-sharing network for election security threats. MS-ISAC, the multi-state equivalent, was forced into a paid membership model when federal funding was terminated. Federal election security grants through the EAC now total $45 million nationally — less than $1 million per state on average, effectively insufficient for any substantial security program.

**State response patterns**: As documented by CyberScoop (April 2026), states have adopted four main replacement mechanisms with highly uneven results:
1. National Guard cyber units (high-capacity states: California, Texas, New York — low-capacity states: Wyoming, Vermont, New Mexico)
2. State police and homeland security agency integration (Pennsylvania model — explicitly stated it "relies much less on CISA than in recent years")
3. University research center partnerships (West Virginia model — direct county clerk networks)
4. State legislative appropriations (Arizona — $650,000, widely acknowledged as insufficient)

**The coordination gap**: CISA's most important function was not any single state's security posture — it was the *national coordination mechanism*. When an adversary exploits a vulnerability in one state's voting system, CISA would alert all states within hours. That function has been replaced, in the words of state officials, by "a patchwork of informal phone calls, email lists, and association meetings." The NASS (National Association of Secretaries of State) wrote to DHS Secretary Kristi Noem in February 2026 warning that the changes "could endanger future elections" — a letter Noem has not substantively responded to.

---

## Core Research Questions

**1. What does the minimum viable state election security posture look like in 2026?**

This is the foundational analytical question. A state with $1 million or less in federal election security funding, limited National Guard cyber capacity, and no prior bilateral agreement with CISA needs a prioritized security checklist. The research should identify:

- The three to five most common attack vectors against election infrastructure (based on documented 2020, 2022, and 2024 incident reports from EI-ISAC, now partially public)
- Which attacks require federal coordination to detect and which can be handled at state level
- What endpoint detection and response (EDR) deployment costs at election-system scale (approximately 8,000 county election offices nationwide)
- What the "air gap" versus "network connectivity" tradeoff looks like for voting machine certification under VVSG 2.0 (the voluntary guidelines that the EAC has now made conditional for HSGP grants)

The CDT (Center for Democracy and Technology) published a "Countdown to the Midterms" analysis in April 2026 mapping the evolution of election security; this should be a primary source despite its 402 paywall — CDT materials are typically accessible through institutional access or direct contact.

**2. Which states have the largest security gaps, and are those gaps correlated with electoral competitiveness?**

The research hypothesis — which Domain 37 implies but does not prove — is that security gap and electoral competitiveness are correlated: the states that the administration most wants to influence in November 2026 are also the states least able to protect their election infrastructure.

The 2026 competitive state map (Arizona, Georgia, Michigan, Nevada, Pennsylvania, Wisconsin — plus possible Senate flips in Montana, Ohio, North Carolina) should be cross-referenced against the documented state capacity indicators: size of state election security budget, existence of National Guard cyber unit, status of MS-ISAC membership (paid vs. lapsed), and existing CISA bilateral agreements (which states had them, which have replacements).

Arizona is the documented case study of high electoral competitiveness combined with documented security vulnerability: it suffered cyberattacks in 2025, received a $650,000 state appropriation it describes as "not going to go anywhere near" its needs, and has an explicitly "diminished" CISA relationship. Arizona is the clearest documented case of the correlation this domain hypothesizes.

**3. What is the international adversary threat landscape for 2026 specifically?**

CISA's termination of the Mis-, Dis-, Malinformation (MDM) team and the firing of Chris Krebs (who ran CISA's election security infrastructure during 2020) removed the two functions that would normally track and respond to foreign adversary operations: the technical infrastructure protection function and the disinformation response function. The research should document:

- What DHS intelligence reporting exists about Russian, Chinese, and Iranian election interference threats for 2026 (public threat assessments, intelligence community statements)
- Whether the absence of EI-ISAC has created documented detection gaps — and whether adversaries have exploited the gap window (January 2025–present) for reconnaissance
- The AI-enhanced social engineering threat identified by state officials: "tailored social engineering attacks" (StateTech Magazine, April 2026) targeting election workers specifically — an attack surface that has grown dramatically since 2020 due to poll worker turnover, and that CISA's training program specifically addressed

**4. What state-to-state coordination mechanisms have emerged organically?**

The formal CISA-mediated coordination network collapsed, but informal coordination has emerged. The research should map:

- Whether NASS has moved from letter-writing to operational coordination (building a secure communication channel, information-sharing protocol, or mutual aid agreement)
- Whether any regional coalitions of secretaries of state have formed security cooperation agreements (New England, Great Lakes, or Pacific Coast models)
- Whether the paid MS-ISAC membership model has drawn the competitive states — and what the paid model offers versus the prior free model
- Whether any universities (MIT Lincoln Lab, Stanford Internet Observatory, Georgia Tech GTRI) have stepped in with state government contracts for election security monitoring

---

## The Structural Argument This Domain Must Make

The core analytical finding of Domain 37b should be: **the CISA dismantlement has created a security gap that individual state action cannot close, because the critical function CISA served — national coordination and cross-state threat intelligence sharing — is by definition impossible at state level.**

This argument has a specific implication: regardless of how much Arizona or Wisconsin spends on state-level EDR, AI monitoring, or National Guard deployment, a zero-day exploit discovered targeting one state's voting machine firmware will not be shared with the other 49 states within the time horizon that matters. In 2020, CISA detected a ransomware campaign targeting election infrastructure in Georgia and alerted all states within 12 hours. That capability is gone.

The governance implication is not simply "restore CISA funding" — though that is the obvious first-order recommendation. The structural implication is that there is a constitutional mismatch between the Elections Clause (which gives states administration authority) and cybersecurity (which requires national-level threat intelligence) that the CISA model resolved through a voluntary federal-state partnership. When that partnership is deliberately terminated by the federal executive as an interference mechanism, the constitutional design has no fallback. This is a genuine gap in the constitutional architecture, not just a funding problem.

---

## Expected Key Sources

**Primary documentation:**
- CyberScoop: "As feds pull back, states look inward for election security support" (April 2026) — [https://cyberscoop.com/cisa-election-security-cutbacks-states-trump-administration/](https://cyberscoop.com/cisa-election-security-cutbacks-states-trump-administration/)
- Votebeat: "Election officials say trust with CISA on election security is broken" (January 2026) — [https://www.votebeat.org/2026/01/15/cisa-election-security-trust-broken-trump-chris-krebs-denise-merrill/](https://www.votebeat.org/2026/01/15/cisa-election-security-trust-broken-trump-chris-krebs-denise-merrill/)
- Votebeat: "CISA halts support for states on election security, U.S. official confirms" (March 2025) — [https://www.votebeat.org/2025/03/11/cisa-ends-support-election-security-nass-nased/](https://www.votebeat.org/2025/03/11/cisa-ends-support-election-security-nass-nased/)
- Brennan Center for Justice: "How the Federal Government Is Undermining Election Security" — [https://www.brennancenter.org/our-work/research-reports/how-federal-government-undermining-election-security](https://www.brennancenter.org/our-work/research-reports/how-federal-government-undermining-election-security)
- StateTech Magazine: "How State and Local Governments Are Securing the 2026 Midterm Elections" (April 2026) — [https://statetechmagazine.com/article/2026/04/how-state-and-local-governments-are-securing-2026-midterm-elections](https://statetechmagazine.com/article/2026/04/how-state-and-local-governments-are-securing-2026-midterm-elections)
- CDT: "Countdown to the Midterms: Mapping the Rapid Evolution of Election Security" — [https://cdt.org/insights/countdown-to-the-midterms-mapping-the-rapid-evolution-of-election-security/](https://cdt.org/insights/countdown-to-the-midterms-mapping-the-rapid-evolution-of-election-security/)

**NASS and official documentation:**
- NASS letter to Kristi Noem (February 2026) — accessible via NASS.org press releases
- EAC HSGP grant conditionality documentation (per Domain 37) — accessible via EAC.gov
- CISA election security page (current vs. archived) — compare [https://www.cisa.gov/election-security-partnership](https://www.cisa.gov/election-security-partnership) against Wayback Machine archived versions pre-January 2025

**Technical standards:**
- VVSG 2.0 (Voluntary Voting System Guidelines) — EAC.gov; relevant to what the EAC is now conditioning HSGP grants on
- MS-ISAC current membership model documentation — CIS Security (cisecurity.org)
- EI-ISAC suspension and restoration status — CIS Security or EI-ISAC.org

---

## Document Structure (Recommended)

**Section 1**: What CISA provided — the pre-2025 federal election security architecture (brief, 600–800 words). Cross-reference to Domain 37's CISA destruction documentation rather than repeating it.

**Section 2**: What states have built — documented state-level replacement mechanisms, with specific examples (Arizona, Pennsylvania, West Virginia, California). Capacity assessment framework: high/medium/low capacity states with indicators. (1,500–2,000 words)

**Section 3**: The coordination gap that cannot be closed at state level — the national threat intelligence function, why cross-state sharing requires federal infrastructure, and what the documented absence of that function means for 2026 vulnerability. (1,000–1,500 words)

**Section 4**: Competitive state vulnerability matrix — cross-referencing the 2026 electoral map (7–8 competitive states) against documented capacity indicators. This is the table that election-protection organizations will find most actionable. (1,000–1,500 words)

**Section 5**: International adversary threat assessment — what public intelligence reporting says about 2026-specific threats in the context of the CISA gap. (800–1,000 words)

**Section 6**: Governance recommendations and advocacy windows — what individual states should do immediately, what NASS should do collectively, what Congress could do (statutory requirement for national election security coordination independent of executive discretion), and what civil society organizations can provide as a partial substitute. (1,000–1,500 words)

---

## Governance and Advocacy Implications

**Immediate (April–July 2026)**:
- NASS should convene an emergency working group to establish a minimal secure communication channel — a paid MS-ISAC membership pool funded by state appropriations if necessary — and share threat intelligence across competitive states
- The five highest-priority states (Arizona, Georgia, Michigan, Pennsylvania, Wisconsin) should conduct independent security assessments of their election infrastructure, with results shared within the state network
- Civil society organizations (Brennan Center, Verified Voting, CDT) should provide technical assistance to under-resourced counties in competitive states on a pro bono or grant basis

**Medium-term (2027 Congressional session)**:
- Statutory requirement that federal election security coordination functions are performed by an agency with statutory independence from political direction — the post-CISA lesson is that a voluntary program dependent on executive goodwill is insufficient
- Permanent funding for EI-ISAC at a level that makes it financially independent of annual appropriations: an endowment model or per-state assessment, rather than federal discretionary funding
- Mandatory minimum election security standards for states receiving any federal election funding (HAVA funds), replacing the current voluntary VVSG model

**Long-term institutional design**:
- The constitutional gap — Elections Clause giving states administration authority while cybersecurity requires national coordination — should be addressed through a cooperative compact mechanism (the Uniform Law Commission or an interstate compact, analogous to the Driver License Compact) that creates binding cross-state obligations without requiring federal executive involvement

---

## Effort Estimate

- **Type**: New standalone domain document
- **Scope**: 5,500–7,000 words
- **Research sessions required**: 1 (most primary sources accessible; CDT document may require institutional access request)
- **Output location**: `domains/domain-37b-state-election-security-coordination.md`
- **Readiness**: Research-ready now. Key sources confirmed accessible. MS-ISAC membership model details require direct check of cisecurity.org
- **Urgency**: High — the security posture of competitive states needs assessment before summer 2026 when voter roll challenges begin

---

## Cross-Domain Integration Notes

- **Domain 37**: This document is the positive counterpart to Domain 37's negative documentation. Domain 37 shows what was destroyed; Domain 37b shows what can be rebuilt in the 2026 window.
- **Domain 21 (Surveillance)**: The EI-ISAC performed a different function from the commercial surveillance infrastructure documented in Domain 21 — it was *defense* against adversary surveillance, not corporate surveillance of citizens. The termination of EI-ISAC and the expansion of commercial data broker surveillance (documented in Domain 21) operate as complementary vectors: the defense infrastructure is removed while the offensive surveillance capacity expands.
- **Domain 33**: Secretary of State capture (Domain 33, Section 1.3a) is directly relevant: states where the Secretary of State has been captured by partisan interests (or where the Georgia-style state election board replacement is underway) cannot be assumed to implement the security recommendations in this document in good faith.
- **Domain 36**: AI-enhanced social engineering attacks on election workers (identified by StateTech Magazine as the leading 2026 threat vector) intersect with Domain 36's analysis of AI governance and the absence of federal regulation of AI tools used in political targeting.

---

*Scope document complete. Ready for full research execution in next session.*
*Sources confirmed accessible as of April 27, 2026.*

---

## **April 2026 Update**

**Added**: April 28, 2026 (Phase 2 Content Maintenance)

---

### Brennan Center Election Officials Survey: Quantifying the Support Collapse

The most significant new primary source for this domain is the Brennan Center's April 2026 survey of local election officials — the most comprehensive data set on the ground-level impact of federal election security withdrawal. Key findings that directly answer the scope document's core questions:

**The resource gap is not being filled at the state level**: 75% of local election officials have not received additional resources from their state or local government to address federal cuts to election security services. The scope document hypothesized that states were adopting replacement mechanisms; the survey data shows those mechanisms are not reaching the local level where election administration actually occurs. The gap is primarily at the county and municipal level, not the state capital level — and the scope document's state-level replacement analysis (National Guard cyber units, legislative appropriations) does not address this bottom-tier vulnerability.

**Federal satisfaction has collapsed**: Officials' satisfaction with federal support decreased from 53% in 2024 to 45% in 2026. The CDC-parallel question — what happens to public health infrastructure when federal support drops below a threshold of adequacy — is now live for election security. The satisfaction drop came despite 89% of officials reporting they plan to coordinate with at least one other local or state agency, confirming that the coordination intent exists but the resources and trust do not.

**Safety and threat environment**: 36% of election officials reported experiencing harassment or abuse; 16% reported being threatened because of their job. This is directly relevant to the AI-enhanced social engineering threat vector identified in the scope document — officials who are already experiencing threats and harassment are more susceptible to tailored spear-phishing attacks that leverage publicly available personal information. The combination of reduced institutional support and elevated personal threat environment makes the 2026 election worker population the most vulnerable since direct administration of elections became professionalized.

**60% are concerned about federal cuts**: This number confirms that the scope document's concern about the coordination gap is held by election officials themselves — it is not an externally-imposed assessment. The fact that 87% say it is important for state and local government to provide additional resources, while 75% have not received them, documents the gap between political acknowledgment and resource allocation.

Source: [Brennan Center: Survey Finds Election Officials Remain Concerned About Safety, Lack of Government Support (April 2026)](https://www.brennancenter.org/our-work/analysis-opinion/survey-finds-election-officials-remain-concerned-about-safety-lack); [Local Election Officials Survey 2026 PDF](https://www.brennancenter.org/media/15483/download/2026_local_election_officials_final_0.pdf?inline=1)

### SAVE Program: A New Federal Interference Vector Against Election Officials

The DHS Systematic Alien Verification for Entitlements (SAVE) program has emerged as a major new threat to election security that the scope document did not address — and that operates through a different mechanism from cybersecurity threats. SAVE is being used to build a national voter database that Democratic secretaries of state and election security experts characterize as a voter suppression tool, while the administration frames it as a noncitizen voter verification system.

**The April 2026 developments**:
- Internal DOJ documents revealed in April 2026 show that DOJ officials planned to share voter rolls with DHS earlier than they publicly admitted, raising questions about the process by which voter data entered the federal surveillance architecture.
- DHS has flagged more than 24,000 names on U.S. voter rolls as potential noncitizens — a dataset Brennan Center analysts characterize as generating significant false positives that wrongly flag U.S. citizens.
- A DOJ privacy officer resigned in April 2026 as the agency prepared to share voter data with DHS, citing concerns about the data transfer.
- CNN reporting (April 21, 2026) documents Trump's effort to "build a massive voter database" that election officials fear will be weaponized to challenge legitimate voters before November.

The SAVE program creates a structural threat that interacts with the CISA security vacuum in a specific way: when states participate in SAVE, they hand voter roll data to a federal agency that has no statutory obligation to protect it from political use, and no independent oversight (the FEC's authority over voter suppression is limited; CISA, which might have flagged data security vulnerabilities, has been defunded for election security purposes). The states most likely to be targeted by SAVE-driven voter challenges are the same competitive states that have the largest cybersecurity gaps — creating a dual vulnerability.

**Partisan split on SAVE**: Democratic secretaries of state (12 signed a December 2025 letter opposing SAVE) uniformly opposed the program; Republican secretaries of state generally embraced it. This partisan alignment means that in competitive states with Republican secretaries of state — Georgia, Arizona, North Carolina — both the cybersecurity gap (documented) and the SAVE-based voter roll challenge threat are simultaneously operative. In states with Democratic secretaries of state who have refused SAVE — Michigan, Pennsylvania, Wisconsin, Nevada, Minnesota — the primary threat remains cybersecurity, not voter roll manipulation through the federal program.

Sources: [Brennan Center: Homeland Security's SAVE Program Exacerbates Risks to Voters](https://www.brennancenter.org/our-work/research-reports/homeland-securitys-save-program-exacerbates-risks-voters); [NPR: DOJ prepares to share voter data with DHS, privacy officer resigns (April 3, 2026)](https://www.npr.org/2026/04/03/nx-s1-5768455/privacy-doj-dhs-voter-data); [CNN: Trump building a massive voter database (April 5, 2026)](https://www.cnn.com/2026/04/05/politics/trump-voter-database-election-fraud); [Democracy Docket: Emails reveal DOJ planned voter roll sharing earlier (April 2026)](https://www.democracydocket.com/news-alerts/emails-reveal-doj-officials-planned-to-share-voter-rolls-with-dhs-much-earlier-than-they-admitted/)

### CISA FY27 Budget Cut: The Permanent Defunding Proposal

The scope document documented CISA's existing budget cuts and staff reductions. The Trump administration's FY27 budget proposal, released April 2026, takes the next step: it proposes cutting CISA's election security program entirely. This is no longer a discretionary administrative decision — it is a legislative proposal to permanently zero out federal election security infrastructure in the appropriations baseline. If enacted, it would require a future Congress and president to specifically appropriate funding to restore any election security function, rather than the current situation where election security programs continue unless affirmatively defunded.

This development transforms the advocacy framing: the current CISA cuts are administratively reversible (a future administration could restore funding without new legislation); a zero appropriation embedded in the FY27 baseline would require affirmative legislative action to undo. The window to prevent the baseline zeroing is the FY27 appropriations process — which, under the 120th Congress elected in November 2026, may be more or less favorable depending on midterm outcomes. This creates a direct link between election security and the midterms: the elections being run under compromised security conditions will determine whether the legal infrastructure for election security can be restored.

Source: [USC Election Cybersecurity Initiative Round-Up: April 4-10, 2026](https://electionsecurity.usc.edu/2026/04/20/election-cybersecurity-round-up-april-4-april-10-2026/)

### State-Level Incident Documentation: April 2026

The USC Election Cybersecurity Initiative's weekly round-ups from April 2026 document specific incidents that ground the scope document's theoretical vulnerability analysis in actual events:

**Georgia** (April 4-10 round-up): State lawmakers concluded their legislative session without addressing voting system vulnerabilities ahead of the 2026 midterms. Georgia is a documented high-vulnerability competitive state in the scope document's analysis; legislative inaction on documented vulnerabilities confirms the worst-case scenario for this state.

**Arizona** (April 11-17 round-up): A judge's ruling on election administration procedures carries implications for midterm voting processes. Arizona also appeared in prior round-ups when state officials declined to report a suspected Iran-linked hacking incident to CISA, citing distrust in how CISA would handle sensitive vulnerability information. This is the clearest documented case of the trust breakdown the scope document analyzes: even when an incident occurs that CISA would ordinarily investigate, the trust destruction the scope document documents has made state officials unwilling to use the one remaining federal-state channel.

**AI disinformation escalation**: Both April round-ups documented AI-generated political disinformation as a growing threat — fabricated political advertisements and supply chain attacks on technology companies used by election vendors. The scope document identified AI-enhanced social engineering as the leading 2026 threat vector; the weekly round-up documentation confirms this assessment is grounded in ongoing observed activity.

Sources: [USC Election Cybersecurity Round-Up: April 4-10, 2026](https://electionsecurity.usc.edu/2026/04/20/election-cybersecurity-round-up-april-4-april-10-2026/); [USC Election Cybersecurity Round-Up: April 11-17, 2026](https://electionsecurity.usc.edu/2026/04/20/election-cybersecurity-round-up-april-11-april-17-2026/); [Votebeat: Arizona officials declined to report hacking incident to CISA (January 2026)](https://www.votebeat.org/2026/01/15/cisa-election-security-trust-broken-trump-chris-krebs-denise-merrill/)

### Advocacy Window Update: April-July 2026 Priority Actions

The scope document's April-July advocacy window is now active. Based on the April 2026 evidence, the following are the most urgent priorities:

**Immediate (April-May 2026)**:
1. State legislatures with sessions still open should pass emergency appropriations for election security, specifically targeting county-level EDR deployment. The Brennan Center survey confirms the resource gap is at the county level, not the state capital. Target states: Georgia (session ended without action — document the failure for electoral accountability), Arizona ($650,000 appropriation documented as inadequate — push for supplemental), Nevada, Wisconsin.
2. File formal opposition to the FY27 budget's election security zero-out with both the House and Senate Appropriations Committees. Framing: a budget proposing to eliminate election security infrastructure while the United States is engaged in a military conflict with Iran (which has been documented targeting U.S. infrastructure including oil, gas, and water sites) constitutes a national security vulnerability, not merely a partisan policy choice.
3. Civil society organizations (Brennan Center, Verified Voting, CDT) should accelerate direct technical assistance to county election offices in competitive states — particularly in Georgia, where state legislative inaction has left county offices without updated security guidance.

**May-July 2026**:
4. Paid MS-ISAC membership coordination: NASS should facilitate a bloc membership arrangement for all competitive-state secretaries of state who have not yet converted to paid MS-ISAC membership. The bloc purchase reduces per-state cost and ensures that the competitive states have at least the minimum threat-intelligence sharing function.
5. Legal challenge to DOJ voter roll data sharing with DHS: The DOJ privacy officer's resignation and the internal document evidence of early planning create a factual record that the data sharing violated Privacy Act protections. ACLU and Democracy Docket have standing to challenge the data transfer; the April 2026 CNN and NPR reporting provides the evidentiary foundation.

---

*April 2026 Update complete — April 28, 2026*
*Key findings: 75% of local officials lack replacement resources; SAVE program is a new dual threat (voter suppression + data security); FY27 budget proposes permanent election security zero-out; Georgia failed to act on voting system vulnerabilities before session ended; Arizona officials declining to report hacking to CISA confirms trust collapse.*
