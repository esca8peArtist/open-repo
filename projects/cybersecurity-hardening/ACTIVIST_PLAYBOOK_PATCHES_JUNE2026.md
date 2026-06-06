---
title: "Activist Playbook v1.1 Patch Summary — June 2026"
project: cybersecurity-hardening
created: 2026-06-06
status: complete
version: 1.0
purpose: >
  Documents all five Q2 2026 patches applied to phase-2-activist-organizing-security-playbook.md,
  corresponding to UPDATE-ACT-01 through UPDATE-ACT-05 per PHASE_2_THREAT_INTEGRATION_CHECKLIST.md,
  plus the Thomson Reuters LEIDS-5 expiration note. Produced as part of the June 2026 sprint
  to reach v1.1 COMPLETE status matching immigration playbook.
---

# Activist Organizing Security Playbook — v1.1 Patch Summary (June 6, 2026)

This document records all five patches applied to `phase-2-activist-organizing-security-playbook.md` in the June 2026 sprint. Each patch is mapped to the source checklist item, the section modified, and the sources added.

---

## Patch 1: Thomson Reuters LEIDS-5 Expiration Note

**Checklist reference**: Adapted from UPDATE-IMM-04 for activist context  
**Priority**: MEDIUM  
**Section modified**: Section 1.1 (Layer 1 — Babel Street social media monitoring)  
**Type of change**: Contextual note added after the "What this means for you" paragraph

**What was added**: A June 2026 update note explaining that the Thomson Reuters LEIDS-5 contract expired May 31, 2026 with no confirmed renewal; that ICE maintains ~$60M in Thomson Reuters contract vehicles; and that data broker opt-outs (LexisNexis Accurint + Thomson Reuters CLEAR) remain recommended for core organizers regardless of renewal status.

Also added: Thomson Reuters CLEAR opt-out to Checklist D (Ongoing Organizational Security) and Tier 2 implementation guidance.

**New sources added**:
- [Thomson Reuters LEIDS-5 contract and employee pressure — LawNext](https://www.lawnext.com/2026/04/the-legal-tech-giants-powering-ice-part-2-the-pushback-employees-shareholders-lawyers-and-the-fight-over-may-31.html)

**Activist-specific framing**: Thomson Reuters CLEAR opt-out reduces commercial data inputs to identity resolution across multiple federal surveillance stacks (Babel Street, ELITE address confidence scoring, any Thomson Reuters contract vehicle). Relevant to Catch and Revoke pipeline for visa-holder activists; also relevant to commercial record layer feeding Flock Safety "Nova" enrichment.

---

## Patch 2: Gait Recognition Future Trajectory Note (UPDATE-ACT-05)

**Checklist reference**: UPDATE-ACT-05  
**Priority**: LOW  
**Section modified**: Section 1.2 (Layer 2 — Aerial Surveillance drone deployment)  
**Type of change**: Parenthetical footnote added after "key implication for countermeasures" paragraph

**What was added**: Note that LiDAR-based gait recognition is in early domestic deployment at border installations but is not yet deployed at US protest sites. Current clothing-based masking countermeasures remain adequate for 2026. Flags this as a 2027+ trajectory to monitor.

**New sources added**: None (trajectory note only, no current deployment to document)

**Activist-specific framing**: If/when gait recognition deploys at protest sites, the clothing change protocol (Section 4.2) would need to add gait disruption techniques (altered gait, variable pace). Not actionable in 2026 but important for organizations planning multi-year security posture updates.

---

## Patch 3: FBI + Clearview AI at Protests, Two Class Actions (UPDATE-ACT-01)

**Checklist reference**: UPDATE-ACT-01  
**Priority**: HIGH  
**Section modified**: Section 1.4 (Layer 4 — Mobile Fortify at protest perimeters)  
**Type of change**: Two parenthetical update blocks added; new Case Study 4 added

**What was added**:

*To Section 1.4*: Confirmation that ICE agents at Minneapolis protests used both Mobile Fortify (NEC/HART) and Clearview AI (50B+ images) simultaneously. FBI agents present separately using facial recognition to populate federal investigative databases. Two class actions: Hilton v. Noem (Maine, February 2026) and Tincher v. Noem (Minnesota, February 2026), documenting agents scanning observers, photographing plates, following people home, and placing individuals in domestic terrorism databases. DHS officially denies this database exists.

*New Case Study 4*: Minneapolis protest facial recognition case — agents documented using both systems, two class action lawsuits, distinction between immigration enforcement consequences and FBI criminal investigative database consequences.

**Why this matters beyond prior guidance**: The prior playbook framed facial recognition at protests as an ICE tool with immigration consequences. FBI integration changes the threat actor picture — FBI investigative database placement creates federal criminal investigation exposure under a different legal authority with no immigration-specific countermeasure. Any US citizen with no immigration vulnerability can now face federal investigative consequences from protest attendance.

**New sources added**:
- [ICE, FBI expand facial recognition use to protest investigations — Biometric Update](https://www.biometricupdate.com/202602/ice-fbi-expand-facial-recognition-use-to-protest-investigations)
- [ICE contracts with Clearview AI — Immigration Policy Tracking Project](https://immpolicytracking.org/policies/reported-ice-contracts-with-clearview-ai-for-facial-recognition-technology/)

---

## Patch 4: ICE Iris Scanning at Enforcement Events (UPDATE-ACT-04)

**Checklist reference**: UPDATE-ACT-04  
**Priority**: MEDIUM  
**Section modified**: Section 1.4 (Layer 4 — Mobile Fortify at protest perimeters)  
**Type of change**: Second parenthetical update block added to Section 1.4; Tier 2 guidance item added

**What was added**:

*To Section 1.4*: ICE deployed iris scanning nationally June 1, 2026 via $25.1M Bi2 Technologies contract, covering 1,570+ handheld scanners accessing 5M+ records from 47 states. Second biometric identification step for protest observers and enforcement monitors who may be physically approached. Iris scanning requires close physical contact unlike Mobile Fortify photography. Guidance: decline and assert right to attorney presence; legal status of compelled non-arrest iris scanning unsettled.

*To Tier 2 guidance (item 12)*: Know your rights regarding biometric requests; script for declining iris scan ("I do not consent to biometric collection. I am requesting an attorney.").

**Activist-specific note**: Protest observers and enforcement monitors at ICE operations face the highest iris scanning risk — agents can approach and attempt close-range scanning. Legal observers attending enforcement operations (not only protests) are in scope. This complements the Section 4.1 ground-level countermeasures which address photography but not close-range iris scanning.

**New sources added**:
- [ICE awards Bi2 $25M contract for 1,570 biometric scanners — The Register](https://www.theregister.com/public-sector/2026/05/29/ice-awards-bi2-25m-contract-for-1570-biometric-scanners/5248733)
- [ICE iris scanners expanding arsenal of tech tools — NPR](https://www.npr.org/2026/05/27/nx-s1-5822429/ice-buys-iris-scanners-tech-tools)

---

## Patch 5: DHS Administrative Subpoenas — Scale, Four-Hour Timeline, New Cases (UPDATE-ACT-02)

**Checklist reference**: UPDATE-ACT-02  
**Priority**: HIGH  
**Section modified**: Section 1.5 (Layer 5 — Account unmasking); Section 3.3 (account architecture); new Case Study 3  
**Type of change**: Expansion of Section 1.5 with new cases; addition to Section 3.3; new Case Study 3

**What was added**:

*To Section 1.5*: Confirmed hundreds of subpoenas. Partial compliance by Google, Meta, Reddit. Three new documented cases: (1) Philadelphia Jon Doe — four hours after emailing a DHS official, DHS subpoenaed Google for his identity; agents appeared at his home two weeks later; ACLU challenge successful but only after near-disclosure. (2) Columbia University targeted to identify a student protester. (3) Montco Community Watch 10–14 day challenge window (cross-reference to existing Case Study 2). Critical implication: anonymous infrastructure must precede any sensitive communication — no retroactive anonymity.

*To Section 3.3*: Added subpoena update note making explicit that four-hour response time eliminates any grace period to establish anonymity post-communication; account architecture must be in place before the account is created.

*New Case Study 3*: Philadelphia Jon Doe case — establishes that DHS uses subpoena tool against US citizens for protected speech (emailing a DHS official), not only against anonymous social media accounts; establishes four-hour response timeline.

**Why this matters beyond prior guidance**: The prior playbook described DHS subpoenas as targeting anonymous anti-ICE social media accounts. The Jon Doe case expands the scope: DHS is using administrative subpoenas to identify any person who communicates with or criticizes the agency, including via direct email under a real name. The four-hour response timeline eliminates any assumption of delay between communication and legal risk.

**New sources added**:
- [ACLU moves to quash DHS subpoena targeting Philadelphia critic — ACLU](https://www.aclu.org/press-releases/aclu-moves-to-quash-abusive-subpoena-aimed-at-tracking-down-man-who-criticized-department-of-homeland-security)
- [DHS withdraws subpoena targeting man who criticized them — ACLU](https://www.aclu.org/press-releases/department-of-homeland-security-withdraws-subpoena-targeting-man-who-criticized-them)

---

## Patch 6: DOGE Federal Data as Organizational Threat (UPDATE-ACT-03)

**Checklist reference**: UPDATE-ACT-03  
**Priority**: MEDIUM  
**Section modified**: New Section 1.6 added; Section 2 threat table updated; Checklist D updated  
**Type of change**: New section; threat table row update; ongoing maintenance checklist addition

**What was added**:

*New Section 1.6*: DOGE's unlawful SSA data access documented via Democracy Forward lawsuit (AFSCME, AFT, Alliance for Retired Americans). DOGE employees coordinated with an outside political advocacy group (widely suspected to be True the Vote) to match SSA data against voter rolls to "overturn election results." Two DOGE employees referred for Hatch Act violations. SSA data includes wage histories, employer names, home addresses, bank account numbers, and immigration status.

The activist-specific framing: this is the first documented case of federal benefit database access coordinated with an outside political organization against named political adversaries — a qualitatively different threat from individual immigration enforcement. Organizations whose staff appear in SSA records (via ACA/Medicaid enrollment, payroll reporting) face structural data exposure that no operational security practice can remove.

*Section 2 threat table*: Updated organizational leadership row to include DOGE/SSA federal data as a threat actor, cross-referencing Section 1.6.

*Checklist D*: Added annual consultation item for organizations facing political targeting regarding DOGE/SSA organizational staff exposure.

**What you cannot mitigate**: SSA data cannot be removed. Wage history and employer data for all staff with W-2 or 1099 income reported to SSA is structurally exposed. The response is legal consultation and financial separation, not operational security.

**New sources added**:
- [DOGE SSA data and voter roll coordination — Democracy Forward](https://democracyforward.org/work/legal/stopping-doges-unlawful-seizure-of-americans-social-security-data/)
- [Trump administration admits DOGE accessed sensitive personal data — NPR](https://www.npr.org/2026/01/23/nx-s1-5684185/doge-data-social-security-privacy)

---

## Summary Table

| Patch | Checklist ID | Priority | Section(s) Modified | Type | New Sources |
|-------|-------------|----------|---------------------|------|-------------|
| Thomson Reuters expiration | Adapted IMM-04 | MEDIUM | Section 1.1; Checklist D; Tier 2 | Note added | 1 |
| Gait recognition trajectory | UPDATE-ACT-05 | LOW | Section 1.2 | Footnote | 0 |
| FBI + Clearview at protests | UPDATE-ACT-01 | HIGH | Section 1.4; Case Study 4 | Expansion + new case | 2 |
| Iris scanning at enforcement | UPDATE-ACT-04 | MEDIUM | Section 1.4; Tier 2 | Addition | 2 |
| DHS subpoenas — new cases | UPDATE-ACT-02 | HIGH | Section 1.5; Section 3.3; Case Study 3 | Expansion + new case | 2 |
| DOGE organizational threat | UPDATE-ACT-03 | MEDIUM | New Section 1.6; Section 2; Checklist D | New section | 2 |

**Source count**: 17 original + 9 new = 26 total  
**Word count increase**: ~1,800 words added (original ~3,400 → updated ~5,200 estimated)  
**New case studies added**: Case Study 3 (Philadelphia DHS subpoena); Case Study 4 (Minneapolis Clearview AI + FBI)  
**Sections added**: Section 1.6 (DOGE organizational threat)

---

## v1.1 COMPLETE Status Assessment

**Criteria matched against immigration playbook v1.1**:

| Criterion | Immigration v1.1 | Activist v1.1 | Status |
|-----------|-----------------|---------------|--------|
| All 5 Q2 2026 patches applied | Yes | Yes | PASS |
| Source count 15+ | 31 sources | 26 sources | PASS |
| Q1-Q2 2026 threats documented | Yes (iris, Clearview, DOGE, LEIDS-5, subpoenas) | Yes (all 5 adapted for activist context) | PASS |
| Role-specific guidance | Yes | Yes (threat table covers 6 participant types) | PASS |
| Changelog in frontmatter | Yes | Yes | PASS |
| last_updated in frontmatter | Yes | Yes | PASS |
| Case studies grounded in documented events | Yes | Yes (5 case studies, all documented) | PASS |
| Tier 2 pilot distribution ready | Yes | Yes | PASS |

**Verdict: Activist playbook is v1.1 COMPLETE. Ready for Tier 2 pilot distribution on the June 15-21 timeline.**

Note on source count differential: The activist playbook has 26 sources vs. 31 for the immigration playbook. The immigration playbook has a higher source count because the ELITE/Palantir system has more documented contract vehicles and court filings than the protest surveillance stack. The activist playbook's 26 sources are all primary sources (court filings, investigative journalism, government contracts, EFF/ACLU documentation) and are sufficient for the depth of the guidance. If higher source count is required for parity, 5 additional sources can be added from EFF's 2025 protest surveillance coverage and the Democracy Forward DOGE litigation documents in the next update cycle.

---

*Document produced: June 6, 2026. Based on PHASE_2_THREAT_INTEGRATION_CHECKLIST.md (June 6, 2026) and web verification of all patch claims.*
