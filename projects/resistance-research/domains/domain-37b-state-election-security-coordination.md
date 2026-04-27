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
