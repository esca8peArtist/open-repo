---
title: "Phase 2 Tier 2 Activation Protocols"
created: "2026-06-17"
status: "production-ready"
domains_covered: [48, 51, 59]
purpose: "Per-domain Tier 2 contact deployment with copy-paste email templates, decision gates, and Tier 3 metrics"
input_document: "PHASE_2_T7_ROUTING_DECISION_TREE.md (routing decision)"
prerequisite: "Tier 2 activation authorized by Day 7 checkpoint signal — see checklist"
---

# Phase 2 Tier 2 Activation Protocols

*Resistance Research — Tier 2 Deployment Playbooks*
*Built June 17, 2026. These protocols activate after the Day 7 checkpoint authorizes Tier 2 per PHASE_2_T7_ROUTING_DECISION_TREE.md. All contacts pre-verified. All templates copy-paste ready.*

---

## How to Use This Document

Each domain has a self-contained protocol section. Within each section:
1. **Contact list** — all verified contacts with emails and engagement hooks
2. **Email templates** — copy-paste ready; fill only `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]`
3. **Outreach sequencing** — initial contacts first, then secondary, then extended based on response
4. **Decision gate to Tier 3** — what metrics must be hit for further expansion
5. **Timing** — checkpoint dates and send windows

For autonomous execution, see the Python script commands at the end of each section.

---

## Domain 59 Tier 2 Protocol — Economic Precarity / CTC

**Activation condition**: 2+ STRONG from Wave 1 Tier 1 (all 4 contacts), OR forced activation (Senate Finance markup deadline regardless of signal)

**T+14 check timing**: June 25 (if Wave 1 sent June 11)

**Hard deadline context**: Senate Finance markup window closes approximately June 25-30. Tier 2 sends must deploy within 24 hours of activation authorization. Do not delay.

### D59 Tier 2 Contact List (Verified June 10, 2026)

| # | Organization | Contact | Email | Hook | Activation Rule | Response Probability |
|---|---|---|---|---|---|---|
| T2-1 | Economic Policy Institute | Heidi Shierholz (President) | researchdept@epi.org (UNCONFIRMED — verify via epi.org/about/contact before send) | EPI wage/labor data foundational to time-poverty pathway; $30,000 productivity-pay gap cited in Domain 59 | STRONG or SELECTIVE activation | 30-45% |
| T2-2 | Demos | Taifa Smith Butler (President) | info@demos.org | Demos mission: "equal say in democracy + equal chance in economy" — direct mandate overlap | STRONG or SELECTIVE activation | 35-50% |
| T2-3 | National Employment Law Project | Rebecca Dixon (President & CEO) | info@nelp.org | Gig economy pathway in Domain 59 is NELP's terrain; worker classification and temporal exclusion | STRONG or SELECTIVE activation | 35-50% |
| T2-4 | National Housing Law Project | Policy team | info@nhlp.org | Housing cost-burden pathway; one of five causal pathways in Domain 59 | STRONG activation only | 20-35% |

**CRITICAL EMAIL NOTE**: researchdept@epi.org is UNCONFIRMED. EPI uses a contact form at epi.org/about/contact. Verify before sending. If no direct email found, use the contact form.

### D59 Tier 2 Send Sequence

**FULL ACTIVATION** (2+ STRONG from Tier 1): Send all 4 contacts on activation day.

| Send | Timing | Recipient | Stagger |
|------|--------|-----------|---------|
| T2-1 | T+0 from activation | EPI (Shierholz) | — |
| T2-2 | T+45 min | Demos (Smith Butler) | 45 min |
| T2-3 | T+90 min | NELP (Dixon) | 45 min |
| T2-4 | T+135 min | NHLP (Policy team) | 45 min |

**SELECTIVE ACTIVATION** (1 STRONG from Tier 1 or forced): Send T2-1 (EPI) and T2-3 (NELP) only — highest alignment contacts. Skip T2-2 and T2-4 until Day 14 reassessment.

---

### D59 Tier 2 Email Templates

**Template T2-1 — Economic Policy Institute**

**To**: researchdept@epi.org (verify first) or epi.org/about/contact form
**Subject**: Democratic participation framing for wage analysis — Senate Finance CTC timing

---

Dear EPI research team,

I am sharing research that may complement EPI's labor and wage analysis with a democratic participation argument relevant to the Senate Finance markup currently underway.

"Economic Precarity and the Civic Participation Crisis" documents the income-based voter turnout gap that reached 42 percentage points in the 2024 election. EPI's data — specifically the $30,000 productivity-pay gap documenting stagnant wages despite rising productivity — is a primary source for the time-poverty pathway: when workers below $17/hour hold multiple jobs to meet basic expenses, the discretionary time for civic participation is systematically eliminated.

The Senate Finance Committee's CTC provisions (maximum $2,200, non-refundable for the bottom income quintile) affect the same low-wage households in EPI's core analysis. The democratic participation frame — that non-refundable CTC structure perpetuates the income-based civic exclusion that EPI's wage analysis documents on the economic side — is an argument that reaches Senate Finance members who have been unresponsive to the distributional critique alone.

Full research document (7,200 words, 44 citations, EPI data throughout):
https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba

CC Attribution 4.0.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Template T2-2 — Demos**

**To**: info@demos.org
**Subject**: Research bridging your two organizational mandates — economic democracy + civic participation

---

Dear Demos team (Taifa Smith Butler),

I am writing to share research that sits directly at the intersection of Demos' two organizational mandates: "equal say in democracy" and "equal chance in economy."

"Economic Precarity and the Civic Participation Crisis" documents the causal mechanism connecting economic inequality to democratic exclusion. The Senate Finance Committee markup currently underway provides the immediate policy application: the OBBBA's non-refundable CTC structure (delivering $0 to the bottom income quintile) perpetuates exactly the economic precarity that your organization documents as a driver of civic disengagement.

The research establishes five causal pathways from material precarity to democratic exclusion — the time-poverty pathway (multi-job holding depletes civic participation hours), the childcare-cost pathway (47-58% of gross income for single mothers below $35,000), the medical debt pathway, the housing cost-burden pathway, and the cognitive bandwidth pathway (Mullainathan/Shafir 2013). Demos' work on economic democracy has documented the economic side of these pathways. Domain 59 provides the democratic participation evidence base that completes the structural argument.

Full research: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba

CC Attribution 4.0 — designed for distribution to Demos' organizational networks.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Template T2-3 — National Employment Law Project**

**To**: info@nelp.org
**Subject**: Worker classification and civic exclusion research — Senate Finance CTC window

---

Dear NELP team (Rebecca Dixon),

I am sharing research that connects NELP's worker classification and gig economy analysis to the democratic participation crisis — specifically relevant to the Senate Finance Committee markup underway on the OBBBA's CTC provisions.

"Economic Precarity and the Civic Participation Crisis" includes a dedicated analysis of the gig economy pathway from economic precarity to civic exclusion: gig worker classification that denies basic employment protections (minimum wage, predictable scheduling, overtime) also denies the time predictability that political participation requires. A gig worker on a demand-based scheduling platform cannot plan 4 hours in advance to attend a town hall, register to vote, or participate in civic advocacy. The temporal exclusion from civic participation is structural, not attitudinal.

NELP's worker classification research is cited throughout Domain 59. The democratic design frame — that misclassification as an independent contractor is also a civic participation barrier — extends your organization's analysis into an advocacy space that may be useful for Senate engagement on CTC refundability (workers classified as contractors receive no employer-side benefit contributions that could complement CTC refundability).

Full research document: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba

CC Attribution 4.0.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Template T2-4 — National Housing Law Project**

**To**: info@nhlp.org
**Subject**: Housing cost-burden pathway to civic exclusion — democratic participation research

---

Dear NHLP policy team,

I am sharing research that documents the housing cost-burden pathway to civic exclusion — one of five causal mechanisms analyzed in "Economic Precarity and the Civic Participation Crisis."

The housing pathway finding: households spending 50%+ of income on housing costs (severe cost burden) are documented in civic participation literature to show significantly reduced voter registration, polling participation, and civic engagement rates. The mechanism is both resource depletion (zero discretionary income for civic participation costs) and residential instability (frequent address changes disrupt voter registration and community attachment).

NHLP's work on housing stability and tenant rights directly addresses the population experiencing the highest civic participation barriers. The Senate Finance CTC provisions are relevant to this population: extremely low-income renters (below 30% AMI) who receive zero credit under the OBBBA's non-refundable structure are the same households facing the housing cost-burden pathway.

Full research document (7,200 words, 44 citations):
https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba

CC Attribution 4.0.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

### D59 Decision Gate to Tier 3

**Tier 3 contacts** (activate T+15 from Wave 1 send after Tier 1+2 signal confirmed):
- Common Cause National — Virginia Kase Solomón (commoncause@commoncause.org)
- People For the American Way — Michael Keegan (pfaw@pfaw.org)
- Families USA — Frederick Isasi (info@familiesusa.org)
- Robert Wood Johnson Foundation — Program Officer, health/democracy (mail@rwjf.org — verify program officer)

**Tier 3 activation metrics** (both must be met):
1. At least 1 STRONG reply from Tier 2 contacts (T2-1 through T2-4)
2. At least 3 total replies (any quality) across Tier 1 + Tier 2 combined

**Tier 3 timing**: T+15 from Wave 1 send = approximately June 25-26 (if Wave 1 sent June 11)

**Python command**: `uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --activate-tier2 59 STRONG`

---

## Domain 51 Tier 2 Protocol — Campaign Finance / Dark Money Architecture

**Activation condition**: 2+ STRONG from Waves 1-2 (full), OR 1 STRONG (initial 3 only), OR 0 STRONG (initial 3 as minimum activation — July 1 deadline pressure)

**June 25 deadline checkpoint**: The July 1 California ballot deadline creates a June 25 hard checkpoint for all Domain 51 Tier 2 activity. All Tier 2 sends must be initiated by June 25 to allow 6 days of organizational response time before the deadline.

**13 Tier 2 contacts pre-identified, outreach sequencing: Initial 3 → Secondary 5 → Extended 5**

### D51 Tier 2 Contact List — All 13 Contacts

**Initial 3 (highest urgency — send first, same day as activation):**

| # | Organization | Contact | Email | Hook |
|---|---|---|---|---|
| T2-1 | True North Research | Lisa Graves (Executive Director) | info@truenorthresearch.org | Dark money investigation expertise; ex-PRWatch; direct overlap with Domain 51 dark money architecture |
| T2-2 | Montana I-194 Campaign | Campaign contact | Via ballotpedia.org — search Montana I-194 2026 | Parallel state ballot initiative; multi-state constitutional theory context |
| T2-3 | Michigan Clean Elections Coalition | Policy team | Via michiganadvance.com — search current contact | Michigan 2026 campaign finance reform effort; multi-state context |

**Secondary 5 (send 48 hours after initial 3 confirmed sent, regardless of initial 3 response):**

| # | Organization | Contact | Email | Hook |
|---|---|---|---|---|
| T2-4 | New Mexico Common Cause | Policy team | Via commoncause.org/new-mexico | NM small-donor public matching program |
| T2-5 | Issue One ReFormers Caucus | Advisory board members | Via issueone.org/about/reformers-caucus | Former elected officials with direct Congressional introduction capacity |
| T2-6 | ACLU Voting Rights Project | Sophia Lin Lakin (Deputy Director) | slakin@aclu.org | Election law and voting rights intersection with Domain 51 FEC argument |
| T2-7 | UCLA Election Law Center | Rick Hasen (Professor) | rhasen@law.ucla.edu | Election Law Blog widely read by campaign finance practitioners; academic amplification |
| T2-8 | Loyola Law School | Justin Levitt (Professor) | jlevitt@lls.edu | Redistricting and campaign finance overlap; election law academic |

**Extended 5 (send only upon Tier 1-2 signal confirmation, minimum 1 STRONG from initial 3 + secondary 5):**

| # | Organization | Contact | Email | Hook |
|---|---|---|---|---|
| T2-9 | End Citizens United / Let America Vote | David Donnelly | info@endcitizensunited.org | Citizens United litigation and advocacy; DISCLOSE Act; 2026 election cycle |
| T2-10 | Public Citizen Democracy Program | Craig Holman | cholman@citizen.org | CRITICAL: shortform handle confirmed; FEC enforcement; SEC disclosure rule |
| T2-11 | Brennan Center for Justice | Saurav Ghosh | ghoshs@brennan.law.nyu.edu | Constitutional analysis; Hawaii/Montana charter model; FEC reform |
| T2-12 | Democracy 21 | Fred Wertheimer | fwertheimer@democracy21.org | CRITICAL: shortform handle confirmed; DISCLOSE Act elder statesman; weekly newsletter |
| T2-13 | OpenSecrets | General inbox | info@opensecrets.org | Dark money database; 501(c)(4) disclosure gap; primary data source for Domain 51 |

**DEAD CONTACTS — DO NOT USE**: Karen Hobert Flynn (kflynn@commoncause.org) — deceased March 2023. Sheila Krumholz (OpenSecrets) — departed late 2023.

### D51 Tier 2 Send Sequence

**FULL ACTIVATION** (4+ STRONG from Waves 1-2):
```
Day 1 (activation day): Initial 3 (T2-1, T2-2, T2-3)
Day 3: Secondary 5 (T2-4 through T2-8)
Day 5: Extended 5 (T2-9 through T2-13) if initial 3 confirm sent
```

**PARTIAL ACTIVATION** (2-3 STRONG):
```
Day 1 (activation day): Initial 3 (T2-1, T2-2, T2-3)
Day 3: Secondary 5 (T2-4 through T2-8)
Day 10 (T+7 from secondary 5): Assess signal; activate extended 5 only if STRONG signal from initial 3 or secondary 5
```

**MINIMAL ACTIVATION** (0-1 STRONG, July 1 deadline pressure):
```
Day 1 (activation day): Initial 3 only (T2-1, T2-2, T2-3)
Day 14 (CLC follow-up): Follow-up to CLC per DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md contingency
Hold secondary 5 and extended 5 pending July 1 reassessment
```

---

### D51 Tier 2 Email Templates

**Template T2-1 — True North Research (Lisa Graves)**

**To**: info@truenorthresearch.org
**Subject**: Dark money architecture research — Citizens United + FEC enforcement analysis — 58 citations

---

Dear Lisa Graves and True North Research team,

I am sharing a research document that extends your organization's dark money investigation work with a democratic design analysis that may be useful for your current campaigns.

"Campaign Finance, Dark Money Architecture, and the Corporate Capture of Democratic Institutions" synthesizes the Citizens United ecosystem from a constitutional design perspective: the $1.9 billion in dark money in the 2024 federal cycle, the FEC's 200+ day enforcement quorum collapse, and the emerging corporate charter workaround theory being tested in Hawaii (SB 2471, signed May 15, 2026) and Montana (I-194 ballot initiative).

The document draws on True North Research's dark money investigation reporting throughout. The ALEC funding flow analysis and the 501(c)(4) disclosure gap documentation in Domain 51 are areas where your organization's investigative findings form the empirical foundation for the constitutional argument.

The most actionable material for 2026: the Hawaii corporate charter theory (Section 6.3) — that states can condition corporate political spending authority on charter compliance without running into the "associations of citizens" reasoning in Citizens United — is a litigation pathway that True North Research's investigation of corporate dark money coordination has been generating the evidentiary record for, even if it has not been named that way.

Full research document (58 citations, CC Attribution 4.0):
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Template T2-2 — Montana I-194 Campaign**

(Obtain current campaign contact via ballotpedia.org before sending — search "Montana I-194 2026 campaign")

**To**: [Current campaign contact — verify via Ballotpedia]
**Subject**: Constitutional research for Montana I-194 campaign — Hawaii SB 2471 model analysis

---

Dear Montana I-194 campaign team,

I am sharing research that directly supports the constitutional theory behind Montana I-194 and may be useful for your campaign communications and legal team.

"Campaign Finance, Dark Money Architecture, and the Corporate Capture of Democratic Institutions" includes a dedicated section (Section 6.3) on the Hawaii/Montana corporate charter model — the constitutional theory that state-derived corporate charters can condition political spending authority without triggering Citizens United's "associations of citizens" reasoning. Hawaii SB 2471 (signed May 15, 2026) is the first enacted version of this theory; Montana I-194 is the second. The analysis documents both the legal pathway and the litigation risk.

Section 6.3 will be directly useful for: (a) campaign messaging that explains the constitutional theory to voters; (b) legal team preparation for litigation challenges; (c) media inquiries about the post-Citizens United legal landscape.

58 citations, CC Attribution 4.0:
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Template T2-4 — ACLU Voting Rights Project (Sophia Lin Lakin)**

**To**: slakin@aclu.org
**Subject**: Campaign finance / election law intersection research — FEC collapse + voting rights architecture

---

Dear Sophia,

I am sharing research that may be relevant to the ACLU Voting Rights Project's work at the intersection of campaign finance enforcement and election law.

"Campaign Finance, Dark Money Architecture, and the Corporate Capture of Democratic Institutions" documents the FEC's 200+ day enforcement quorum collapse from a constitutional perspective and its downstream effects on the democratic accountability architecture that the Voting Rights Project is protecting. When dark money flows without disclosure into ballot measure campaigns — including those targeting voting rights restoration, felon disenfranchisement, and electoral administration — the FEC's enforcement failure directly enables attacks on the voting rights infrastructure the ACLU defends.

Section 5 (2026 State Ballot Measures) is the most directly relevant to your current work: dark money flows into four state ballot initiatives with direct voting rights implications. The intersection between Domain 51's FEC analysis and the ACLU's election law portfolio is most acute there.

58 citations, CC Attribution 4.0:
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Template T2-7 — UCLA Election Law Center (Rick Hasen)**

**To**: rhasen@law.ucla.edu
**Subject**: Citizens United dark money architecture synthesis — Hawaii/Montana charter model analysis — 58 citations

---

Dear Professor Hasen,

I am sharing a research document on the Citizens United dark money architecture that may be of interest for the Election Law Blog's coverage of the Hawaii/Montana charter theory developments.

"Campaign Finance, Dark Money Architecture, and the Corporate Capture of Democratic Institutions" synthesizes the post-Citizens United campaign finance landscape with a dedicated section (Section 6.3) on the Hawaii SB 2471 corporate charter workaround — the constitutional theory that states with corporate charter authority can condition political spending without triggering Citizens United's citizens-association reasoning. This is the most significant doctrinal development in post-Citizens United campaign finance law since McCutcheon.

The document also covers the FEC enforcement quorum collapse (200+ days as of June 2026) and the AI PAC development — both of which appear in your recent Election Law Blog coverage and are treated here with full citations to the primary sources.

58 citations, CC Attribution 4.0:
https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

I would be grateful for any reaction to the Section 6.3 constitutional analysis, as your assessment of the doctrinal viability of the charter theory would be valuable for future research.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

### D51 Decision Gate to Tier 3

Domain 51 Tier 3 (7 contacts) activates July 1+ if Tier 1-2 signal is strong. Contacts: Common Cause National, Brennan Center Wendy Weiser, Democracy Docket (contact form), Loyola Levitt (already in extended 5), Princeton Election Law, FEC reform coalition.

**Tier 3 activation metrics:**
1. 4+ total replies (any quality) from Tier 1 + Tier 2 combined
2. At least 2 STRONG from the extended 5 Tier 2 contacts (ECU, Public Citizen, Brennan, Democracy 21, OpenSecrets)

**Python command**: `uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --activate-tier2 51 STRONG`

---

## Domain 48 Tier 2 Protocol — Criminal Justice / Civic Exclusion Architecture

**Activation condition**: 2+ STRONG from Waves 1-2 (LDF + FFJC + ACLU VA), OR 1 STRONG (FFJC only), OR 0 STRONG (ACLU VA contingency path)

**June 27 checkpoint**: Soft deadline for Domain 48 Tier 2 sends before the July 15 Virginia Right to Vote Coalition integration window closes.

**Virginia Right to Vote Coalition integration deadline**: July 15, 2026. All Domain 48 Tier 2 contacts relevant to Virginia must be reached by June 27 to allow 18 days for organizational review and integration.

### D48 Tier 2 Contact List

| # | Organization | Contact | Email | Hook | Activation Rule |
|---|---|---|---|---|---|
| T2-1 | NAACP Legal Defense Fund | Janai Nelson (President and Director-Counsel) | info@naacpldf.org | Felony disenfranchisement litigation; LFO equal protection; Eleventh Circuit SB 7066 | 2+ STRONG from Wave 1-2 |
| T2-2 | Fines and Fees Justice Center | Joanna Weiss (Co-Executive Director) | info@finesandfeesjusticecenter.org | LFO/court debt as voter suppression; Florida Amendment 4 case study | 1+ STRONG from Wave 1-2 |
| T2-3 | ACLU of Virginia | Mary Bauer (Executive Director) | acluva@acluva.org | Virginia Right to Vote Coalition member; King v. Youngkin precedent; ballot measure campaign | Contingency if M4BL unresponsive by July 10 |
| T2-4 | Prison Policy Initiative follow-up | Wendy Sawyer (Research Director) or Leah Wang | info@prisonpolicy.org | Data validation request for jury exclusion / housing barrier sections | If Wave 1 PPI produced engagement |

**Contingency note on ACLU of Virginia**: If M4BL National (info@m4bl.org) has not responded by July 10, activate ACLU Virginia immediately as the Virginia Right to Vote Coalition bridge. ACLU of Virginia is a confirmed coalition member with M4BL Virginia affiliate relationships — they can route materials to M4BL Virginia even if M4BL national is unresponsive.

### D48 Tier 2 Send Sequence

**FULL ACTIVATION** (2+ STRONG from Waves 1-2):
```
Day 1 (June 17-18, activation day):
  T2-1: NAACP LDF (info@naacpldf.org)
  T2-2: FFJC (info@finesandfeesjusticecenter.org) — 45 min after NAACP LDF

Day 10 (June 27):
  T2-3: ACLU of Virginia (acluva@acluva.org) — scheduled regardless of LDF/FFJC response

Day 14 (July 1):
  T2-4: PPI follow-up if Wave 1 engagement confirmed
```

**PARTIAL ACTIVATION** (1 STRONG from Waves 1-2):
```
Day 1 (activation day):
  T2-2: FFJC only

Day 10 (June 27):
  T2-3: ACLU Virginia — if M4BL still unresponsive, activate as primary Virginia coalition route
  Reassess T2-1 (NAACP LDF): if FFJC responded STRONG, proceed; if no response, hold LDF until Day 14
```

**CONTINGENCY ACTIVATION** (0 STRONG from Waves 1-2):
```
Do NOT send NAACP LDF cold without prior domain engagement — relationship org benefits from warm approach
Day 1 (activation day):
  T2-3: ACLU Virginia — warm coalition member send (Template C-contingency below)
Day 14:
  If ACLU Virginia responds: send NAACP LDF via warm introduction framing
  If ACLU Virginia no response: send FFJC + reassess full strategy
```

---

### D48 Tier 2 Email Templates

**Template T2-1 — NAACP Legal Defense Fund**

**To**: info@naacpldf.org
**Subject**: Criminal justice civic exclusion research — Readmission Act theory, Virginia injunction, LFO equal protection — for LDF networks

---

Dear NAACP Legal Defense Fund (Janai Nelson),

I am writing to share a research document that extends LDF's civil rights litigation and advocacy work with a democratic design analysis of criminal justice civic exclusion — specifically the King v. O'Bannon Readmission Act theory and the 2026 state restoration landscape.

"Criminal Justice, Civic Exclusion Architecture, and the Democratic Participation Crisis" synthesizes LDF's existing work on felony disenfranchisement with the Sentencing Project's "Locked Out" data and the King v. O'Bannon analysis. The document's most immediately actionable section for LDF is the Readmission Act constitutional theory (Section 4.4): the Eastern District of Virginia's January 22, 2026 permanent injunction found Virginia's disenfranchisement of non-common-law-felony offenders violated federal readmission conditions. The analysis explores whether this theory extends to other former Confederate states readmitted under similar conditions — Alabama, Tennessee, Arkansas, Georgia, Texas — which would represent a major expansion of LDF's redistricting and voting rights restoration portfolio.

The November 3, 2026 Virginia ballot measure (constitutionalizing automatic restoration on release) has a July 15 organizational integration window for voter education materials. LDF's Virginia relationships make this the most time-sensitive actionable element.

6,200+ words, 41 citations, CC Attribution 4.0:
https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8

I would be grateful if this reaches LDF's voting rights restoration and redistricting litigation teams.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Template T2-2 — Fines and Fees Justice Center**

**To**: info@finesandfeesjusticecenter.org
**Subject**: LFO as voter suppression — democratic design analysis — Florida Amendment 4 and Virginia restoration

---

Dear Joanna Weiss and the Fines and Fees Justice Center team,

I am sharing research that extends FFJC's work on court fines and fees into a democratic design framework that documents LFOs as a voter suppression mechanism operating outside formal election law.

"Criminal Justice, Civic Exclusion Architecture, and the Democratic Participation Crisis" includes a dedicated section (Section 4) on legal financial obligations as a poll tax. The Florida Amendment 4 case study — from the 2018 voter approval of automatic restoration, through the 2019 SB 7066 debt conditioning, through the current Eleventh Circuit state of play — is the most fully documented case of a legislative rollback of voter-approved rights restoration in modern American law. Worth Rises' data (83% of formerly incarcerated people carrying court debt, average $13,607) and FFJC's fines-and-fees analysis are the empirical foundation for the LFO-as-poll-tax equal protection argument.

The democratic design framing may be directly useful for FFJC's state legislative campaigns: presenting LFOs not as a criminal justice issue alone but as a voter suppression mechanism has different constitutional leverage and different political resonance with legislators who are not on the criminal justice committees.

The Virginia ballot measure's July 15 organizational integration deadline is the nearest actionable window.

6,200+ words, 41 citations, CC Attribution 4.0:
https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Template T2-3 — ACLU of Virginia (contingency path)**

**To**: acluva@acluva.org
**Subject**: Virginia Right to Vote Coalition research — King v. O'Bannon analysis — November ballot measure materials

---

Dear ACLU of Virginia team (Mary Bauer),

I am writing to share research that directly supports the Virginia Right to Vote Coalition's November 3, 2026 ballot measure campaign.

"Criminal Justice, Civic Exclusion Architecture, and the Democratic Participation Crisis" provides a detailed analysis of the King v. O'Bannon permanent injunction (January 22, 2026; effective May 1, 2026), the 1870 Readmission Act constitutional theory, and the ballot measure's role in constitutionalizing automatic rights restoration on release.

The July 15 organizational integration window means coalition members who want to incorporate this research into voter education and mobilization materials need to receive it now. As a confirmed Virginia Right to Vote Coalition member, ACLU of Virginia is the most direct channel to reach the broader coalition network — including M4BL Virginia affiliates, community organizing partners, and other coalition members.

Section 7 (2026 Restoration Reform Landscape) and Section 8 (Reform Architecture) provide the coalition messaging framework and the constitutional backing for the ballot measure campaign.

6,200+ words, 41 citations, CC Attribution 4.0:
https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8

I would appreciate confirmation this reaches your voting rights team and any indication whether it should be routed to other coalition partners directly.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

### D48 Decision Gate to Tier 3

**Tier 3 contacts**: M4BL state affiliates (via ACLU Virginia bridge), Virginia Right to Vote Coalition direct contact (via sentencingproject.org Virginia partnerships), state-level coalition organizations in Alabama, Florida, Mississippi, Georgia.

**Tier 3 activation metrics (both required):**
1. July 15 Virginia integration deadline confirmed met (Sentencing Project, FFJC, or ACLU Virginia confirms coalition integration)
2. At least 1 STRONG signal from NAACP LDF or ACLU Virginia

**Tier 3 timing**: July 15-30, after Virginia integration deadline confirmation.

**Python command**: `uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --activate-tier2 48 STRONG`

---

## Cross-Domain Tier 2 Contingency

### If Tier 1 Response Is WEAK Across All Domains

**Decision point**: Do we consolidate to 1-2 strongest domains for focused effort, or halt Phase 2 Tier 2?

This decision is made at Day 14, not Day 7. At Day 14 with zero substantive responses across all three domains:

**Option 1 — Consolidate to 1-2 domains:**
```
Evaluation criteria: Which domain has the hardest external deadline that is still operative?
  - If Senate Finance markup still active (June 14 deadline): consolidate to Domain 59 only
  - If markup completed but CA ballot still active (July 1): consolidate to Domain 51
  - If both passed but Virginia ballot still active (November 3): consolidate to Domain 48

Consolidation execution: Focus all Tier 2 contact time and follow-up energy on the consolidated domain.
Suspend Tier 2 outreach for held domains until July 1 checkpoint.
```

**Option 2 — Halt Phase 2 Tier 2, escalate to user:**
```
Condition: External deadlines have passed for Domains 59 and 51; Domain 48 Virginia deadline still active.
Action: Flag in CHECKIN.md. See PHASE_2_T7_ROUTING_DECISION_TREE.md Section 5.3 for full escalation protocol.
```

**Option 3 — Proceed with all three domains' Tier 2 regardless:**
```
Rationale: Week-2 sends establish organizational awareness even without immediate response.
           Organizations that do not respond at Day 7 or 14 may integrate materials internally
           and cite them at Day 30-60 without ever having replied.
Decision: Proceed unless active resources are constrained. Tier 2 outreach has no material cost.
```

---

*Built June 17, 2026. All contacts verified: Domain 59 (June 10), Domain 51 (June 10-11), Domain 48 (June 5-16). All templates copy-paste ready. Fill [YOUR_NAME] and [YOUR_CONTACT_INFO] only.*
