---
title: "Phase 2 Detailed Implementation Roadmap"
project: cybersecurity-hardening
created: 2026-05-19
status: implementation-ready
author: research-agent
session: 1339
depends-on:
  - PHASE_2_SEQUENCING_STRATEGY.md
  - PHASE_2_SEQUENCING.md
  - TIER2_DISTRIBUTION_PREP.md
  - TIER3_DISTRIBUTION_PREP.md
  - PHASE_2_DEPLOYMENT_READINESS.md
  - threat-update-cadence.md
  - SCENARIO_PLAYBOOK_INDEX.md
---

# Phase 2 Detailed Implementation Roadmap

**Bottom line**: All six scenario playbooks are complete and production-ready as of May 2026. Phase 2 implementation is not a content-creation problem — it is a sequencing, distribution, feedback integration, and maintenance problem. This roadmap converts the high-level Phase 2 strategy into concrete execution: named deliverables, week-level timelines, effort estimates, success criteria, and quantitative decision gates for every module and quarterly review.

**Current Phase 2 status** (as of May 19, 2026):
- All six scenario playbooks: complete (v1.0–v1.1)
- Tier 2 messaging templates: complete
- Tier 2 (33 organizations) and Tier 3 (30 organizations) distribution prep: complete
- Threat update cadence and monitoring infrastructure: established
- Phase 1 Tier 1 outreach: in progress (user at Phase 1 walkthrough step 1.3)

This roadmap covers the 12-month implementation window beginning Q2 2026 (June) through Q2 2027. It assumes Phase 1 Tier 1 outreach begins no later than June 15, 2026, making the Week 7 adoption gate fall in early August and the first Phase 2 public content launch at the July 26 quarterly review.

---

## Section 1: Module-by-Module Execution Plan

The seven Phase 2 modules are not sequential silos — research tracks 1 and 2 (threat model expansion and advanced protection) can run immediately, while distribution modules (3 through 7) gate on Phase 1 adoption data per PHASE_2_SEQUENCING.md. The order below reflects priority and dependency, not strict sequencing.

---

### Module 1: Government Surveillance Full-Stack Threat Model Expansion

**Goal**: Update the core threat model to accurately reflect the 2026 operational landscape, particularly the five capability gaps identified in PHASE_2_SEQUENCING_STRATEGY.md Section 1: FBI biometric (FACE Services + NGI + AI), DHS HART biometric platform, ICE Mobile Fortify field deployment, drone surveillance (Skydio, MQ-9), and post-SCOTUS DOGE/SSA cross-agency fusion.

**Prerequisites from Phase 1**: None. This module is independent of adoption data. The threat model corrections (Mobile Fortify framing, BFU/AFU distinction) are Phase 1 accuracy issues, not Phase 2 content — those two sections should be updated in opsec-playbook.md and implementation-guide.md before or concurrent with Tier 1 distribution, not deferred.

**Deliverables**:
- Updated `threat-model.md` Section V (Biometrics): Add Mobile Fortify field deployment, HART 75–100 year retention, age restriction removal (children now included), CBP entry-exit facial biometrics
- New `threat-model.md` Section XI (Aerial Surveillance): Drone capabilities (Skydio X10D 7.5-mile detection range, MQ-9 military deployment), FAA exclusion zone ruling, LAPD/NYPD protest deployment documentation, countermeasure framework
- Updated `threat-model.md` DOGE/SSA section: Post-SCOTUS status (SSA data access operational), Fourth Circuit April 2026 ruling, specific SSA data categories now accessible (SSN, address history, benefit history, employer records)
- Updated NSA Section 702 section: June 12, 2026 deadline resolution (to be documented after the date passes)
- Threat matrix table update (Section 1.4 of PHASE_2_SEQUENCING_STRATEGY.md format) reflecting current operational status of all 13 tracked systems
- One-paragraph pre-launch correction to opsec-playbook.md covering Mobile Fortify field biometrics (Immediate — before Tier 1 launch)
- BFU/AFU distinction and auto-reboot configuration added to implementation-guide.md (Immediate — before Tier 1 launch)

**Timeline**: Weeks 1–8 (June through mid-July 2026). The pre-launch corrections are Week 0. The full Gist update publishes at the July 26, 2026 quarterly review.

**Effort estimate**: 12–16 orchestrator research hours. The research base is largely complete in PHASE_2_SEQUENCING_STRATEGY.md Section 1; execution is primarily synthesis, fact-checking against current primary sources (USASpending.gov, FPDS, PACER, Nextgov/FCW), and writing.

**Success criteria**:
- Updated Gist published with version date July 26, 2026
- All five gaps from PHASE_2_SEQUENCING_STRATEGY.md Section 1 reflected in the updated threat model
- No factual claims in the updated sections are from single-source journalism without corroboration (confidence level notation added where appropriate)
- At least one Tier 1 or Tier 2 contact who has already received the corpus is notified of the update and acknowledges

---

### Module 2: Advanced Protection Techniques — Identity Compartmentalization and Forensic Hardening

**Goal**: Produce a standalone advanced-protection supplement addressing the protection gaps in Phase 1: three-tier identity compartmentalization architecture, behavioral fingerprint countermeasures, aerial surveillance response, and device forensic hardening (BFU/AFU, duress PIN, auto-reboot).

**Prerequisites from Phase 1**: None for research. For publication, wait for Week 7 gate — the advanced protection guide is not appropriate for the full Tier 1 distribution (it is too complex for most Tier 1 audiences) and should be the Phase 2 Tier 2 lead deliverable.

**Deliverables**:
- `advanced-identity-compartmentalization-guide.md`: Three-tier identity architecture guide covering device-level compartmentalization (two-device minimum, cash-purchased sensitive device, never co-located), network-level compartmentalization (different network fingerprints per context), communication compartmentalization (separate Signal profiles, no source/contact overlap), financial compartmentalization (cash + Monero entry/exit hygiene), and temporal compartmentalization (breaking behavioral co-location signals)
- `behavioral-fingerprint-countermeasures.md`: Practical guide to behavioral de-anonymization (typing cadence, Wi-Fi probe requests, acoustic beacons, battery fingerprinting) with countermeasures — GrapheneOS settings, Tails OS for highest-risk activities, MAC randomization verification, microphone access policy
- `aerial-surveillance-field-guide.md`: Drone threat environment (Skydio X10D specs, MQ-9 capabilities, LAPD/NYPD operational deployment), ground-level counter-surveillance (mask+hat+sunglasses degradation of facial recognition accuracy, clothing-based re-ID break), aerial counter-surveillance (overhead cover, umbrella, generic clothing, ADS-B Exchange monitoring for active flights)
- Two compartmentalization checklists (desktop reference card format, printable): one for activists preparing for a public action, one for journalists managing source communications
- Addition of advanced forensic hardening to implementation-guide.md: BFU vs. AFU state explanation, auto-reboot configuration (12–24 hours), duress PIN/wipe passphrase setup with legal caveat, LogoFAIL UEFI mitigation note for laptop users

**Timeline**: Research: Weeks 1–6 (June–early July). Production: Weeks 6–10 (mid-July through mid-August). Publication: concurrent with or just after the July 26 quarterly review.

**Effort estimate**: 20–25 orchestrator hours. The conceptual framework is established in PHASE_2_SEQUENCING_STRATEGY.md Sections 2.1–2.5; the deliverable work is converting that into structured, practical documentation with step-by-step verification.

**Success criteria**:
- Advanced compartmentalization guide reviewed by at least one Tier 2C security researcher contact before publication (technical accuracy check)
- Both checklists fit on a single printed page (A4 or letter) — usability constraint
- Device forensic hardening additions to implementation-guide.md tested against a real GrapheneOS device (auto-reboot and wipe passphrase settings confirmed present in current GrapheneOS build)
- Module 2 deliverables linked from the main Gist as supplementary resources, not embedded in the core corpus

---

### Module 3: Scenario Playbook Final Validation and Deployment

**Goal**: Move all six completed scenario playbooks from production-ready status to deployed and actively used by target organizations.

**Prerequisites from Phase 1**: All six playbooks are written (v1.0–v1.1). Deployment gates on the Week 7 Phase 1 adoption metric (minimum: 40 orgs contacted, 5+ responses or 3+ Bitly clicks or 1+ integration signal). The journalist and whistleblower playbooks are ready for immediate pilot deployment without waiting for the full Week 7 gate, per PHASE_2_DEPLOYMENT_READINESS.md.

**Deliverables**:

*Pilot deployment (Weeks 4–6, before Week 7 gate)*:
- Journalist playbook to Freedom of the Press Foundation security team (security@freedom.press) with specific feedback request (CBP device protocol, Signal safety number verification)
- Whistleblower playbook to Government Accountability Project and POGO with WPA gap table and parallel construction risk discussion as framing anchors

*Full deployment by playbook* (post-Week 7 gate):
- Immigration evasion playbook: Gist integration + distribution through Tier 1 immigration legal aid contacts (natural channel from Phase 1 outreach)
- Activist organizing playbook: Distribution through Tier 2 digital rights and civil liberties organizations (EFF, CDT, Access Now) — frame as protest security resource
- Journalist security playbook: Full Tier 2D wave (CPJ, RCFP, PEN America, journalism schools) — June 12 FISA deadline creates urgency window
- Whistleblower playbook: GAP, POGO, National Whistleblower Center, congressional oversight staff contacts
- Financial resistance playbook: Nonprofit attorney networks, labor organizing departments, mutual aid fund managers — note: requires nonprofit tax counsel review of the donor privacy and fiscal sponsorship sections before formal distribution
- DV survivor safety playbook: NNEDV Safety Net review required before any distribution; no distribution until NNEDV Safety Net Project practitioner validates safety planning framework escalation risk language

**Deployment format for all playbooks**: Each playbook is a standalone Gist or linked document. Do not embed playbooks in the core corpus Gist — keep the core Gist as the three-document set and link playbooks as additive resources. Each playbook should have its own short URL (Bitly or equivalent) for independent tracking.

**Timeline**: Pilot deployments: Weeks 4–6. Full deployment wave: Weeks 8–16 (August through October 2026).

**Effort estimate**: 15–20 orchestrator hours for coordination, outreach drafting, feedback integration, and tracking setup. The playbooks themselves are written; this module is about managed distribution, not content creation.

**Success criteria**:
- At least one named organization (FPF, GAP, NNEDV Safety Net, or equivalent) has reviewed and provided feedback on their relevant playbook before full deployment
- DV survivor playbook does not deploy until NNEDV Safety Net practitioner feedback is received and incorporated
- Each playbook has an independent tracking link with click metrics separated from core corpus tracking
- By Week 16: at least three of six playbooks have been forwarded, cited, or actively distributed by a receiving organization (not just acknowledged)

---

### Module 4: Tier 2 Pilot Launch and Organizational Feedback Loop

**Goal**: Execute the Tier 2 outreach campaign (33 organizations) and build the feedback mechanisms that inform both Tier 3 sequencing and Phase 2 content refinement.

**Prerequisites from Phase 1**: Tier 1 active outreach complete (Weeks 1–3). Tier 2 transition criteria met (per PHASE_2_SEQUENCING.md Section 2): 40+ orgs contacted, 5+ responses or 3+ clicks or 1+ integration signal, no critical failures.

**Pilot design (5 organizations, Weeks 4–6)**:
The pilot runs before the full Tier 2 wave. Five organizations selected based on highest expected receptivity and fastest feedback cycle:
1. Freedom of the Press Foundation — journalist playbook review (fastest feedback cycle, most operationally aligned)
2. Electronic Frontier Foundation — threat model validation (highest credibility amplification value)
3. Access Now Digital Security Helpline — immigration/activist population alignment (bilingual reach)
4. Government Accountability Project — whistleblower playbook review
5. Surveillance Technology Oversight Project (STOP) — NYC ICE surveillance context, Albert Fox Cahn track record on rapid engagement

**Pilot feedback collection**: Each pilot contact receives a structured feedback ask: (1) Is the threat model technically accurate? (2) Is there a gap in the countermeasures for your specific audience? (3) Are you willing to forward to your network? Simple three-question ask, not a survey form.

**Full Tier 2 wave** (Weeks 5–12 per PHASE_2_SEQUENCING.md Section 1):
- Weeks 5–6: Digital rights organizations (12 orgs, 3–4 contacts/day)
- Weeks 7–8: Journalist organizations (7 orgs)
- Weeks 9–11: Academic programs (9 orgs) — note: May–August is bad timing for academic contacts; shift 2B wave to September if needed
- Weeks 9–12: Security researcher communities (5 channels), ongoing

**Feedback loop mechanism**: Separate Gmail label structure (`Tier2-Feedback/`) tracks substantive responses by type: technical-validation, gap-identification, distribution-intent, curriculum-intent. Gap-identification responses are the most valuable — they directly inform Module 2 content gaps and potential playbook revisions. Review Tier 2 feedback weekly during Weeks 5–12 and summarize in a feedback digest document at Week 12.

**Timeline**: Pilot: Weeks 4–6. Full wave: Weeks 5–12. Feedback synthesis: Week 12–13.

**Effort estimate**: 25–30 orchestrator hours across the full Tier 2 window (matching the 65–85 total hours estimate in PHASE_2_SEQUENCING.md Section 4, with roughly one-third attributed to Tier 2).

**Success criteria**:
- Pilot: All 5 pilot organizations contacted and at least 2 substantive responses received before full wave launch
- Wave: 25 of 33 Tier 2 organizations contacted (Tier 2 → Tier 3 transition criterion)
- Institutional validation: At least one of EFF, CDT, Access Now, or Privacy International acknowledges the corpus (Tier 2 → Tier 3 gate, Section 2 of PHASE_2_SEQUENCING.md)
- Feedback synthesis document produced by Week 13 with at least 3 actionable findings that inform Module 2 or playbook revisions

---

### Module 5: Tier 3 Institutional Expansion

**Goal**: Reach policy organizations, labor unions, and academic law/policy schools that shape long-term regulatory and legal frameworks governing commercial surveillance.

**Prerequisites**: Tier 2 transition criteria met (25+ orgs contacted, institutional validation from at least one major digital rights org, 6-week minimum gap from Tier 2 launch). Semester timing confirmed for 3C academic contacts (target September–October 2026 for fall start).

**Sequencing within Tier 3** (Weeks 11–20 per PHASE_2_SEQUENCING.md):
- Weeks 11–12: Policy organizations (Georgetown CPT, ACLU SPT, Brennan Center, New America OTI, Brookings CTI) — these receive any Tier 2 credibility signals as part of the outreach
- Weeks 13–14: Labor organizations (AFL-CIO Tech Institute, UFW, NDWA, SEIU, CWA) — UFW and NDWA are direct-member-protection contacts, requiring less credibility runway; AFL-CIO Tech Institute frames around their AI Principles for Workers and the commercial surveillance data broker angle
- Weeks 14–18: Academic law and policy schools (Georgetown Law CPT, Harvard Cyberlaw Clinic, Yale ISP, UW Tech Policy Lab, Columbia Knight Institute, Berkeley BCLT) — semester-dependent, do not send during May–August crunch

**Special track — Phase 2 audience expansion contacts** (Weeks 15–20, separate from core Tier 3 wave):
These six organizations were not in the original Tier 1/2/3 pipeline and require separate outreach infrastructure:
- NNEDV Safety Net Project: DV survivor distribution channel (required review for DV playbook)
- AFL-CIO Technology Institute: Labor + tech intersection
- National Association of State Election Directors (NASED): Election worker security gap post-CISA withdrawal
- National Association of Election Officials (Election Center): Same rationale
- National Legal Aid and Defender Association (NLADA): Public defenders who need to understand the surveillance infrastructure used against their clients
- VITA (Volunteer Income Tax Assistance) programs: ITIN filer tax preparers in the IRS-DHS data sharing pipeline

**Effort estimate**: 20–25 orchestrator hours for Tier 3 proper (contact research, personalization, tracking, follow-up). Additional 8–12 hours for Phase 2 audience expansion track. Tier 3 contacts require substantially more personalization per email than Tier 1 or 2 — the effort ratio is higher per contact.

**Success criteria**:
- Short-term (Month 1–3): At least one policy organization begins internal review; at least one labor organization requests adapted member materials
- Medium-term (Month 3–6): One policy brief or white paper cites the corpus; one academic course integrates the threat model
- Long-term (Month 6–12): Legislative testimony or agency comment letters cite the corpus; NLADA or public defender network uses playbook in client representation context
- NNEDV Safety Net engaged by Week 16 (required before DV playbook general release)

---

### Module 6: Threat Model Maintenance and Currency

**Goal**: Implement the systematic threat monitoring infrastructure established in threat-update-cadence.md, with specific sentinel tracking for Phase 2's expanded threat landscape.

**Prerequisites**: Threat update cadence framework is already established. Module 6 is operational infrastructure, not content creation.

**Deliverables**:
- Monthly Primary Source Check List scan (2–3 hours/month): FPDS contract tracking (Palantir), PACER docket monitoring (IRS-ICE data sharing litigation, DOGE/SSA cases), Nextgov/FCW for capability updates, Democracy Docket for election and voting rights litigation
- Google Alerts configured for: "Palantir ICE", "Mobile Fortify", "HART biometric", "Shai-Hulud", "FISA 702", "DOGE SSA", "Flock Safety", "Cellebrite Signal" — 8 sentinel alert streams
- Quarterly deep-dive updates (September, December 2026, March 2027): Full briefing accuracy review, update any stale claims, increment version date in frontmatter, notify all Score 3+ contacts who have received the corpus
- Five priority sentinel threat vectors for Phase 2 (in addition to existing Tier 2 briefing sentinel vectors):
  1. **Mobile Fortify deployment expansion**: New agency adoptions, new vendor contracts (currently NEC), false-positive incident documentation — any expansion triggers opsec-playbook.md update
  2. **Flock Safety new agency deployments**: Currently documented in 5,000+ communities; any acceleration in major immigrant-population metro areas (LA, NYC, Chicago, Houston, Miami) triggers activist organizing playbook update
  3. **Palantir AIP autonomous flagging rollouts**: New AIP deployments at immigration or financial agencies — triggers threat model update to behavioral de-anonymization section
  4. **Cellebrite Physical Analyzer capability updates**: New platform support, new app extraction modules (particularly for messaging apps) — triggers device hardening guide update
  5. **NSA Section 702 legislative outcome**: June 12, 2026 deadline passed; outcome (with or without warrant reform) triggers update to all briefings' policy sections within 48 hours

**Update distribution process** (for mid-campaign updates to already-reached contacts): Per threat-update-cadence.md — Trigger Category 1 events (FISA 702, IRS-ICE injunction, ProKYC takedown, major supply chain incident) require update email to all acknowledged contacts within 48 hours. Template already established. Keep update email under 150 words.

**Timeline**: Ongoing from June 2026 through at least Q1 2027. Monthly scan cycle starts June 2026. First quarterly deep-dive: September 2026.

**Effort estimate**: 2–3 hours/month for monthly scans. 6–8 hours/quarter for full quarterly reviews. Total over 12 months: approximately 40–48 hours.

**Success criteria**:
- Zero factually stale claims in any distributed briefing or playbook (no documented case of an organization adopting guidance that has been superseded without notification)
- All five sentinel vectors have active monitoring by June 30, 2026
- Quarterly review dates are calendar events, not tasks — July 26, September, December, March
- Update log in threat-update-cadence.md maintained in real time (not retroactively reconstructed)

---

### Module 7: Format Diversification and Accessibility

**Goal**: Produce Spanish translation of highest-impact content, a decision tree routing document, and video primer scripts — contingent on adoption data showing format is a meaningful adoption barrier.

**Prerequisites**: Adoption data from Months 1–6. Format diversification is contingent: if Tier 1 and Tier 2 engagement shows language access or reading-level access is a significant barrier, prioritize Spanish translation. If geographic gap (Texas users without access to California DROP platform) is the dominant complaint, prioritize the state-specific supplement. If DV and labor union feedback shows members need visual formats, prioritize video scripts.

**Deliverables (contingent on adoption data)**:

*Spanish translation (priority)*:
- Part 0 (data broker opt-outs) translation: The single highest-ROI translation. Requires no technical knowledge to execute, has direct impact for the most at-risk population (undocumented immigrants), and is self-contained. Target translator: community health worker or legal aid paralegal with bilingual Spanish-English fluency, not a professional translation service (because the audience needs natural spoken Spanish, not formal translation). Scope: approximately 2,500 words. Estimated external cost: $200–400 if contracted; $0 if a Tier 1 organization volunteers a staff translator.
- One-page Spanish-language summary of key actions (GrapheneOS, Signal, Mullvad, data broker opt-outs): 400 words, printable format.
- Note on translation scope: the threat model and implementation guide should not be translated in Phase 2 — they are too long and technically complex to maintain accuracy across languages without significant investment.

*Texas supplement decision tree*:
- The California DROP platform path (documented in Part 0) does not apply to Texas residents without California nexus. Texas-specific alternatives (Texas Data Broker Law S.B. 2105 if passed; national opt-out pathways not dependent on state residency; SORN opt-out mechanisms that apply federally) need documentation.
- Format: branching decision tree, not a prose supplement. "Where do you live?" → state branches → platform-specific instructions. The Texas branch is the first priority; other state branches added as needed based on Tier 1 feedback geography.
- Effort: 6–8 orchestrator hours to research Texas-specific data broker law status and build the decision tree document.

*Video primer scripts*:
- Content-only deliverables (no production). Scripts for four 3–5 minute primers:
  1. "What is ELITE and why does my address matter?" (immigration surveillance primer)
  2. "How to use Signal safely" (communication security primer)
  3. "What to do if ICE approaches you" (rights and counter-surveillance primer)
  4. "How to protect your phone before a protest" (device and physical security primer)
- Each script is a 600–800 word document with scene descriptions, key points, and visual cues. Production is a separate decision — DIY (user records with phone) is viable for primers 3 and 4; primers 1 and 2 benefit from screen recording of actual tool setup. External production cost if commissioned: $800–2,000 per video.

**Timeline**: Month 7–12 (December 2026 through May 2027). Spanish translation starts if language access is confirmed as a barrier by Month 4 Tier 2 feedback. Texas supplement if geographic gap confirmed by Month 3. Video scripts are the lowest priority and should be deferred until playbook and translation work is complete.

**Effort estimate**: Spanish translation: 8–12 orchestrator hours (research, translation coordination, review). Texas supplement: 6–8 hours. Video scripts: 10–14 hours (four scripts). Total Module 7: 24–34 hours.

**Success criteria**:
- Spanish Part 0 translation: At least one Tier 1 immigration legal aid organization reports using Spanish translation materials with clients
- Texas supplement: At least one Texas-based contact acknowledges the decision tree addresses their specific state gap
- Video scripts: At least one Tier 2 organization (FPF, IRE, or a journalism school) expresses willingness to produce or use video content based on scripts

---

## Section 2: Scenario Playbook Deployment Detail

All six playbooks are complete and production-ready. This section specifies threat model summary, deployment format, audience, timing, and validation for each.

---

### Playbook 1: Immigration Surveillance Evasion (phase-2-immigration-surveillance-evasion-playbook.md, v1.1)

**Threat model**: The primary surveillance system for this population is Palantir's ELITE address confidence scoring, which aggregates Medicaid records, HHS data, DMV records, commercial data broker location data, and ALPR hits near known addresses. ICE Mobile Fortify extends biometric identification to any street-level encounter (no formal processing required). ICM social graph mapping uses family member relationships as location anchors. DOGE/SSA post-SCOTUS access adds SSN-linked identity records, benefit history, and address history to the active data fusion layer. The population faces the highest combination of surveillance intensity and legal vulnerability of any group in the corpus.

**Specific Phase 2 techniques required**: Address administrative record hygiene (no new records at shelter/safe-house addresses), Medicaid address alignment (keep Medicaid address pointing to the known public address, not safe locations), ICM family graph awareness (predictable family contact patterns are surveillance anchors), Mobile Fortify field encounter awareness and mask countermeasures in any street-level interaction with enforcement personnel.

**Deliverable format**: Standalone Gist with its own short URL. Format: numbered protocol with 4 sections (Address Management, Device Security, Communication Security, Encounter Protocols). No more than 1,500 words. Designed to be read in one sitting and shared by a legal aid case manager with a client. No footnotes — reference links are at the bottom, not inline.

**Audience**: Undocumented individuals, DACA recipients, individuals in removal proceedings. Also useful for immigration attorneys managing client data hygiene. Distribution note: this playbook should be shared by a trusted intermediary (legal aid case manager, community health worker), not cold-distributed. Direct public posting of this playbook without a trusted intermediary context is lower value.

**Delivery timeline**: July 26, 2026 quarterly review (first Phase 2 content launch). Distribution through Tier 1 legal aid channel contacts who have already received the core corpus.

**Testing and validation**: Legal review by immigration attorney for accuracy on Medicaid/HHS records and ELITE address scoring. Review by at least one Tier 1 immigration legal aid organization (NILC, CLINIC, or RAICES — whichever has the strongest Tier 1 engagement response) before broad distribution. Validation question: "Would you share this with a client in removal proceedings without modification?"

---

### Playbook 2: Activist Organizing and Counter-Surveillance (phase-2-activist-organizing-security-playbook.md, v1.1)

**Threat model**: Babel Street OSINT continuously monitors public social media for keyword and sentiment patterns; content posted immediately before or during public actions is highest-risk. ALPR networks track vehicle approach and departure from known protest sites, creating a behavioral record of protest attendance. Drone surveillance (Skydio X10D, LAPD/NYPD operational deployment confirmed) creates aerial identification at oblique angles that partially defeat ground-level mask countermeasures. Mobile Fortify at protest perimeters enables on-the-spot biometric identification. ImmigrationOS "Catch and Revoke" cross-references social media activity for visa holders. The combination of aerial + ALPR + biometric creates a layered identification system that requires layered countermeasures, not a single-point solution.

**Specific Phase 2 techniques required**: 72-hour pre-action social media hygiene, vehicle separation from personal identity (rental/transit/friend's vehicle for arrival), layered physical countermeasures (mask+hat+sunglasses + generic clothing exit strategy), emergency check-in protocol with designated legal support contact, duress communication protocols.

**Deliverable format**: Two-part document. Part 1: Pre-action checklist (printable one-page format, chronological — 72 hours before, 24 hours before, day-of). Part 2: Deeper technical guidance for organizers who coordinate others. Total length: 2,500 words. Distribution format: Gist + printable PDF version of Part 1.

**Audience**: Protest organizers, political activists, community defense networks. Secondary audience: protest legal observers who need to advise participants on security protocols. Accessibility note: Part 1 checklist must be readable without technical background. Part 2 assumes Signal familiarity.

**Delivery timeline**: Weeks 8–12 (August–September 2026). Distribution through Tier 2 digital rights organizations (EFF, CDT, Access Now) who have direct relationships with activist communities.

**Testing and validation**: Review by at least one protest legal observer network (National Lawyers Guild chapter) for accuracy on legal encounter protocols. Field test of Part 1 checklist by a Tier 2 contact with direct activist community connection to confirm that a non-technical reader can follow it independently.

---

### Playbook 3: Financial Resistance (phase-2-financial-resistance-playbook.md, v1.0)

**Threat model**: The IRS LCA platform maps financial social networks among investigation targets, connecting organizational accounts to personal accounts and to social graph neighbors via transaction patterns. DOGE-era IRS-DHS data sharing (contested in litigation but partially operational) creates a pipeline between financial records and immigration enforcement infrastructure. Palantir Foundry at IRS Criminal Investigation enables cross-agency social graph queries. Cryptocurrency exchange KYC data (Coinbase specifically documented in IRS LCA contract language) is accessible to the platform. The threat is not primarily individual audit risk — it is social graph expansion: an organization under investigation will pull in all organizations and individuals with regular financial connections.

**Specific Phase 2 techniques required**: Organizational financial hygiene (documentation of all financial activity as mission-consistent), donor privacy via fiscal sponsorship, Monero use with non-KYC entry/exit points, financial account compartmentalization by activity type, structuring law awareness (documenting legitimate purpose of cash transactions).

**Deliverable format**: Single prose document with three distinct sections: (1) Individual financial privacy, (2) Organizational financial hygiene, (3) Cryptocurrency for organizations and individuals. 3,500 words. Format does not need to be a checklist — this audience (nonprofit staff, mutual aid organizers, attorneys) can read prose. Gist distribution.

**Required review before distribution**: Nonprofit tax counsel review of the donor privacy, fiscal sponsorship, and organizational financial documentation sections. These are legal compliance recommendations and must be validated by a nonprofit attorney before formal distribution. This is the module's binding constraint.

**Audience**: Advocacy organizations under political scrutiny, mutual aid networks, individual donors to causes under IRS investigation risk, activists with financial exposure.

**Delivery timeline**: Weeks 12–16 (September–October 2026), contingent on nonprofit attorney review. If review is not obtained by September, defer financial playbook and accelerate DV playbook NNEDV review instead.

**Testing and validation**: Nonprofit tax attorney review (can be informal — a Tier 3 legal contact who specializes in nonprofit tax is the ideal reviewer). Validation question: "Does any recommendation in this playbook create legal exposure if followed in good faith?"

---

### Playbook 4: Institutional Whistleblowing Security (phase-2-institutional-whistleblowing-security-playbook.md, v1.0)

**Threat model**: All government surveillance capabilities apply at elevated intensity to suspected insider disclosure. Cellebrite UFED physical extraction from a government-issued device in AFU state is the primary device-forensics threat. Government network monitoring is comprehensive and legally available — network-layer logs at a government agency document all outbound connections. PRISM (Section 702) provides compelled access to email, cloud storage, and metadata of government employees suspected of unauthorized disclosure. The primary failure mode for whistleblowers is not operational security failure during disclosure — it is using a government device, home network, or personal email at any point in the disclosure chain.

**Specific Phase 2 techniques required**: SecureDrop access exclusively via Tor on a non-associated device and network, legal protection framework (WPA scope and gaps, OSC complaint pathway, congressional oversight channel), parallel construction awareness and documentation protocol, separation of disclosure device and network from all identity-linked infrastructure.

**Deliverable format**: Single document with a clear separation between the operational security section (how to disclose safely) and the legal protection section (what protections apply and how to use them). WPA coverage gap table (probationary period gap, intelligence community gap, press disclosure gap) as a visual reference. SecureDrop directory list (65+ participating organizations) as an appendix. Total: 3,700 words. Distribution format: Gist.

**Audience**: Federal government employees, contractors, employees of private companies with evidence of illegal government conduct. This playbook requires no modification for its audience — legal protections and SecureDrop are federally uniform. No state-specific variation needed.

**Delivery timeline**: Weeks 5–9 (pilot: Government Accountability Project, Week 5; POGO, Week 5; broader distribution Weeks 7–9). This is one of the two pilot-eligible playbooks (with journalist security) because of the GAP/POGO distribution infrastructure already in place.

**Testing and validation**: GAP and POGO review (pilot distribution at Week 5 serves as validation). Validation question: "Is the WPA coverage gap table accurate as of May 2026, and does the parallel construction risk section reflect current Department of Justice practice?"

---

### Playbook 5: Journalist Security at Scale (phase-2-journalist-security-playbook.md, v1.0)

**Threat model**: CBP device search authority at international border crossings requires no warrant or probable cause — the primary journal evidence-destruction risk is a laptop or phone with source-identifying data seized at customs. PRISM (Section 702) compels access to journalist email and cloud storage when communicating with foreign sources; the failed warrant-amendment vote (42–50 in the Senate) confirms this authority continues unconstrained for U.S. persons queried incidentally. NSLs compel carrier and provider disclosure of journalist metadata without judicial authorization. Babel Street monitors journalists' public profiles continuously. CBP has specific authority at the border that law enforcement lacks in the domestic environment — the border is the highest-risk physical encounter point for journalists with source material.

**Specific Phase 2 techniques required**: Border crossing clean device protocol (travel device with no source-identifying data, source material in encrypted cloud not accessible on travel device), source Signal account separation from personal Signal account (dedicated GrapheneOS device with VoIP number), SecureDrop deployment at news organization (FPF provides setup support), PRISM-resistant foreign source communication (Signal with foreign-registered number, safety number verification required, no Signal Note-to-Self backup syncing).

**Deliverable format**: Structured by threat scenario, not by tool. Section 1: Border crossings. Section 2: Source communication security. Section 3: SecureDrop for newsrooms. Section 4: Foreign source PRISM mitigation. This structure maps directly to the scenarios journalists actually encounter. Appendix: FPF contact for SecureDrop setup support. Total: 3,600 words. Distribution format: Gist + consideration for FPF republication in their training materials library.

**Audience**: Investigative journalists, documentary filmmakers, photojournalists, news organization IT and security teams. Secondary: journalism school curricula. Translation need: English only for primary distribution; FPF's international reach handles non-English distribution via their existing channels.

**Delivery timeline**: Weeks 4–8 (pilot: FPF, Week 4; full wave: CPJ, RCFP, PEN America, IRE, journalism schools, Weeks 6–8). June 12 FISA deadline creates urgency window for pre-deadline distribution — send before June 12 if possible.

**Testing and validation**: FPF security team pilot review (feedback ask specifically on CBP device protocol and Signal safety number verification). IRE or NICAR conference integration interest as validation signal. Validation question: "Would you include this in your reporter security training program without modification?"

---

### Playbook 6: DV Survivor Safety (phase-2-dv-survivor-safety-playbook.md, v1.0)

**Threat model**: The primary adversary is an intimate partner with pre-existing device access, shared account credentials, shared family plan location sharing, and potentially legal access to shared financial accounts. Stalkerware (FlexiSPY, Hoverwatch, mSpy — apps that run invisibly on a device with root access) is the dominant threat vector and is structurally different from government surveillance in every dimension: the adversary is close-access, not remote; the device access is physical, not network-based; the safety risk from detection is immediate physical harm, not legal consequences; and the countermeasures (device replacement, new accounts on a new device) are more operationally complex because any change to device or account configuration can trigger escalation. This playbook addresses the most dangerous threat environment of any of the six scenarios because the wrong action, executed in the wrong order, can directly increase physical danger.

**Specific Phase 2 techniques required**: Safety planning framework (assess exit risk before any action — this is the NNEDV Safety Net Project's core methodology and must be integrated, not invented), stalkerware detection and removal protocol (must recommend device replacement rather than removal for root-access stalkerware), account separation (new accounts on new device, not reset on existing device), financial account separation, and emergency exit protocol with shelter contact.

**Required review — non-negotiable**: This playbook must be reviewed by NNEDV Safety Net Project practitioners before any distribution. The escalation risk language in the safety planning section (specifically the statement that removing stalkerware from a device where the abuser has root access can trigger physical violence escalation) is clinically validated DV safety guidance and must be confirmed by a practitioner before it is distributed as advice to survivors. No distribution under any circumstances until this review is complete.

**Deliverable format**: Practitioner-mediated guide (designed to be used by a DV advocate with a survivor, not by a survivor independently without support). Two-column format: left column is the survivor-facing guidance; right column is practitioner notes on timing, escalation risk, and when to pause or redirect. This format is unusual for a security playbook but is dictated by the safety planning requirement. Total: 3,800 words plus practitioner notes. Distribution format: PDF (not Gist — Gist is too easily shared without practitioner context).

**Audience**: DV survivors via DV advocates. Distribution infrastructure: NNEDV Safety Net Project, state DV coalitions, VAWA-funded programs, shelter technology safety staff. Do not distribute through general Tier 1/2 channels — this audience needs DV-advocate-mediated distribution.

**Delivery timeline**: NNEDV Safety Net contact: Week 15–16. Review timeline: 4–8 weeks (DV organizations have their own internal review processes). Distribution: not before Month 5 (November 2026 at earliest). This is the latest-deploying playbook because of its mandatory validation requirement.

**Testing and validation**: NNEDV Safety Net Project practitioner review (binding). National Domestic Violence Hotline technology safety staff secondary review (recommended). Validation questions: "Is the escalation risk language accurate? Does the safety planning framework sequence match the NNEDV methodology? Is there any recommendation in this playbook that could increase physical danger to a survivor if followed?"

---

## Section 3: Tier 2 and Tier 3 Audience Expansion

### Tier 2 Pilot: Five Organizations, Concrete Plan

The Tier 2 pilot (Weeks 4–6) runs on five organizations before the full 33-organization wave. Selection criteria: high receptivity, fast feedback cycle, existing alignment with corpus content.

**Pilot cohort**:
1. Freedom of the Press Foundation — Journalist playbook review; send to security@freedom.press; specific feedback ask on CBP protocol and Signal safety number verification
2. Electronic Frontier Foundation — Threat model validation and distribution; send to press@eff.org; frame as request for technical review by an org with existing Palantir/ELITE coverage
3. Access Now Digital Security Helpline — Immigration population alignment; send to security@accessnow.org; frame as resource for their at-risk population helpline work; note bilingual reach requirement
4. Government Accountability Project — Whistleblower playbook review; GAP's existing representation of federal employee whistleblowers makes them the ideal validator
5. Surveillance Technology Oversight Project (STOP) — NYC ICE surveillance context; Albert Fox Cahn has published on exactly the ICE/Palantir surveillance documented in the corpus; fastest to engage of any Tier 2A contact

**Success metrics for pilot** (before full wave launch):
- 3 of 5 pilot contacts respond substantively (reply within 14 days with more than an acknowledgment)
- At least 1 contact provides technical feedback on the threat model or a playbook
- At least 1 contact indicates forwarding or integration intent

**Trigger for pausing full wave**: If only 1 or fewer pilot contacts respond substantively after 3 weeks, pause full wave and re-evaluate framing. Check: is the subject line compelling? Is the opening sentence organization-specific? Is the Gist URL accessible? Run the same diagnostic as PHASE_2_SEQUENCING.md Scenario A.

---

### Tier 2 Feedback Loop into Tier 3 and Content Revision

Tier 2 feedback is the evidence base for Tier 3 credibility and for Phase 2 content revision. The feedback loop operates on two channels:

**Credibility compounding into Tier 3**: Any Tier 2 acknowledgment or citation is referenced in Tier 3 outreach. The format: "This corpus has been engaged by [category description] — 'an international digital rights organization' or 'a major press freedom organization' — and we are sharing it with policy institutions where the documented evidence base can inform regulatory and litigation work." Do not name organizations without explicit permission. The compounding effect: Georgetown CPT's question "who else has engaged with this?" gets a real answer by Week 12.

**Content revision triggers from Tier 2 feedback**:
- If 3+ Tier 2 contacts identify the same gap in the countermeasures → trigger Module 2 revision
- If Tier 2C security researcher identifies a factual error in the countermeasures → correct and update within 48 hours (Gist version increment, update notification to all acknowledged contacts)
- If Tier 2D journalist feedback shows that the threat model framing is not compelling for their audience → revise journalist playbook framing (not core corpus)
- If Tier 2B academic feedback shows citation format is wrong for their context → produce a separate academic-citation-formatted version of the threat model

---

### Tier 3 Expansion Strategy

**Sequencing rationale**: Policy organizations (3A) receive Tier 3 outreach first because they have the fastest review cycles and the highest leverage on regulatory outcomes. Labor organizations (3B) receive it second because UFW and NDWA have direct member protection motivation — they do not need the credibility runway that policy organizations require. Academic law and policy schools (3C) receive it last, targeted at semester starts (September–October 2026 for fall; February–March 2027 for spring).

**Per-sector customization**:
- Georgetown CPT: Frame as companion to their American Dragnet report. "This corpus extends American Dragnet's Palantir analysis with the 2025–2026 capability expansions and provides the countermeasure layer that American Dragnet does not."
- ACLU SPT: Frame around their litigation against warrantless commercial data purchases. "The threat model documents the specific legal pathways through which commercial data broker purchases evade Fourth Amendment constraints — the data that their current litigation challenges."
- AFL-CIO Tech Institute: Frame around their AI Principles for Workers. "The same commercial surveillance data broker infrastructure that enables immigration enforcement targeting affects gig workers and domestic workers — members who are both producers of location data and subjects of the systems built from it."
- UFW and NDWA: Direct member protection frame. "Part 0 (data broker opt-outs) is immediately actionable for members who face immigration enforcement risk. Two to four hours, no technical expertise required, directly reduces ELITE targeting exposure."
- Harvard Cyberlaw Clinic: Frame around FOIA-sourced primary sources as litigation-ready documentation. "The threat model is built for citation in legal contexts — FOIA disclosures, government contracts, and court filings are the primary sources throughout."

**Organizations not to contact in Tier 3** (based on risk assessment):
- CNAS (Center for a New American Security): Hawkish think tank; require significant re-framing that may misrepresent the corpus's civil liberties grounding. Low value, medium risk.
- Future of Privacy Forum: Industry-aligned; their engagement could compromise the corpus's perceived independence. The forum works with commercial data brokers whose practices are documented as threats in the corpus. Avoid.

---

### Language Translation Roadmap

**Spanish translation priority rationale**: An estimated 37 million Spanish-speaking people in the U.S. include a disproportionate share of the population most at risk from ELITE targeting. Spanish-language legal aid organization staff are a primary Tier 1 distribution vector — but their most vulnerable clients often have limited English literacy. The existing Part 0 in English is inaccessible to those clients directly.

**Translation sequencing**:
- Month 4 (October 2026): Spanish Part 0 (data broker opt-outs) and one-page summary — highest priority, lowest complexity, directly actionable for at-risk population
- Month 6 (December 2026): Spanish-language summary of the immigration surveillance evasion playbook key actions (not full playbook — maintain the principle that immigration playbook distribution is intermediary-mediated)
- Month 8+ (February 2027 and beyond): Further translations based on feedback from Tier 1/2 contacts on which additional content is generating language-access barriers

**Translation approach**: Partner with a Tier 1 immigration legal aid organization that has bilingual staff, rather than contracting a professional translation service. Rationale: (1) zero cost, (2) naturally idiomatic Spanish for the target population (legal service Spanish vs. formal translated Spanish is different), (3) the translating organization becomes a co-owner of the Spanish version and has motivation to distribute it. Identify the partner organization from Tier 1 engagement data — whichever legal aid organization has the strongest engagement signal and bilingual capacity.

**Other languages**: Haitian Creole (Florida/New York Haitian immigrant population), Portuguese (Brazilian immigrant communities), Mandarin and Cantonese (Chinese immigrant communities) — all deferred to post-Tier-2 feedback. If Tier 2 contact Access Now (which operates in 20+ languages) engages substantively, their translation infrastructure may be available.

---

### Video and Visual Format Roadmap

Video primers are high-impact for accessibility but high-cost for production. The approach is to produce scripts (low cost, orchestrator-executable) and identify production partners among Tier 2 and Tier 3 contacts.

**Production approach priority order**:
1. FPF or IRE produces video using our scripts (preferred — these organizations have in-house production capacity and established distribution to journalist audiences)
2. A Tier 1 organization with video production capacity volunteers to produce community-facing primers 3 and 4
3. DIY production by user (phone camera, screen recording) for primers 1 and 2 (device hardening setup walkthrough lends itself to screen recording)
4. Commission external production only if none of the above is available and adoption data shows video is a material barrier

**Scripts priority order** (if production partner is confirmed):
1. "How to protect your phone before a protest" (most immediately actionable, clearest audience)
2. "How to use Signal safely" (highest reach, serves all six scenario audiences)
3. "What to do if ICE approaches you" (highest stakes, most need for trusted presentation — consider recording with an immigration attorney narrator if possible)
4. "What is ELITE and why does my address matter?" (most complex conceptually; needs visual diagram of data flow, not just talking head)

---

## Section 4: Quarterly Review Gates and Decision Points

The four review gates operationalize the "does Phase 2 continue as planned, pivot, accelerate, or pause?" decision. Each gate has quantitative criteria, not subjective judgments.

---

### Gate 1: End of Q2 2026 (July 26, 2026)

**What this gate decides**: Whether the Phase 2 content launch (threat model update + immigration playbook publication) proceeds as planned, and whether Phase 2 content development is on track.

**Metrics to measure**:
- Tier 1 cumulative contacts: At least 40 of 50–60 targeted organizations contacted (Phase 1 completion criterion)
- Tier 1 response rate: At least 5 responses of any type from 50 sends (10% minimum)
- Bitly total clicks: At least 50 unique clicks (indicates the corpus is being read)
- Module 1 completion: Threat model update for Mobile Fortify, drone surveillance, HART biometrics, and DOGE/SSA sections written and ready to publish
- Phase 1 pre-launch corrections: BFU/AFU and Mobile Fortify additions to core corpus confirmed live on Gist
- Tier 2 pilot status: At least 3 of 5 pilot organizations contacted; at least 1 substantive response received

**Decision criteria**:
- All criteria met: Publish threat model update, publish immigration playbook, proceed to full Tier 2 wave
- Tier 1 response rate below 10% but above 5%: Proceed with content launch; adjust Tier 2 framing based on the specific Tier 1 engagement patterns (which organizations are responding, what they're asking about)
- Tier 1 response rate below 5%: Pause Tier 2 full wave. Run the Scenario A diagnostic from PHASE_2_SEQUENCING.md. Revise framing before proceeding.
- Module 1 incomplete: Delay Gist update. Publish only what is confirmed accurate. Do not publish a partially updated threat model with known gaps.
- FISA 702 outcome (June 12): If Section 702 reauthorized without warrant reform (expected), update NSA section to reflect current deadline and remove the "pending deadline" urgency framing. If reform passes (unlikely), update advocacy sections to note the win and shift emphasis to remaining threats.

---

### Gate 2: End of Q3 2026 (September 30, 2026)

**What this gate decides**: Whether Tier 3 launch proceeds as planned, whether DV playbook has completed NNEDV review, and whether format diversification (Spanish translation, Texas supplement) should be prioritized.

**Metrics to measure**:
- Tier 2 progress: At least 25 of 33 Tier 2 organizations contacted
- Tier 2 institutional validation: At least 1 of EFF, CDT, Access Now, or Privacy International has acknowledged the corpus (Tier 2 → Tier 3 gate criterion)
- Playbook deployment: At least 3 of 6 playbooks have been forwarded or cited by a receiving organization
- NNEDV outreach: Contact initiated (even if review not yet complete)
- Module 2 completion: Advanced compartmentalization guide and device forensic hardening additions live
- Format barrier signal: Tier 1/2 feedback documents at least 3 cases where language access or format was identified as a barrier

**Decision criteria**:
- All criteria met: Launch Tier 3 (3A policy organizations first, then 3B labor, then 3C academic law in October start); initiate Spanish translation work; NNEDV Safety Net as priority outreach
- Tier 2 institutional validation absent: Delay Tier 3 by 4 weeks. Run an additional digital rights organization wave (EPIC, Restore the Fourth, Center for Constitutional Rights) before Tier 3 launch.
- Fewer than 3 playbooks forwarded or cited: Do not expand playbook distribution format. Focus on improving existing distribution before format diversification.
- Format barrier signal below threshold (fewer than 3 documented cases): Deprioritize Spanish translation; focus resources on Tier 3 outreach quality instead.
- Budget constraint: If Spanish translation requires external contractor and cost is a constraint, substitute internal partner (bilingual Tier 1 staff) and adjust timeline.

**ICM biometric contract** (expected September 2026): If ICM biometric integration contract is awarded in September as expected, trigger immediate Module 6 update — threat model's DHS biometric section requires update with confirmed operational scope.

---

### Gate 3: End of Q4 2026 (December 31, 2026)

**What this gate decides**: Whether the 12-month implementation window stays on track or requires a Phase 3 planning decision. Also the trigger for the first full annual review.

**Metrics to measure**:
- Tier 3 progress: At least 20 of 30 Tier 3 organizations contacted
- Tier 3 medium-term signals: At least 1 policy brief or white paper citing the corpus; at least 1 academic course integrating the threat model; at least 1 labor organization distributing Part 0 to members
- DV playbook status: NNEDV Safety Net review complete; playbook either deployed or in final revision
- Spanish translation: Part 0 Spanish translation published; at least 1 Tier 1 organization using it
- Threat model currency: Quarterly review complete; all five sentinel vectors confirmed as actively monitored
- Total orchestrator hours expended: Tracking against 100–150 hour total estimate

**Decision criteria**:
- All criteria met: Continue as planned through Q1 2027 (video scripts, Texas supplement, second-round Tier 3 outreach)
- No policy brief or academic citation by end of Q4: Pivot Tier 3 strategy — shift from think tank/academic outreach to litigation-support framing. Approach ACLU SPT and Georgetown CPT with specific litigation angle rather than general corpus sharing. Provide targeted threat model sections formatted for legal citation.
- DV playbook still not deployed: Either NNEDV review is in progress (acceptable delay) or outreach has not been initiated (unacceptable). If NNEDV outreach not initiated by December, escalate to direct contact with NNEDV Safety Net Project director.
- Orchestrator hours tracking significantly over estimate (>175 hours): Evaluate which modules are over-budget and whether to deprioritize Module 7 (format diversification) in favor of sustaining Module 6 (threat maintenance).
- Budget/cost tracking: Any cost-center commitments (Spanish translation external contractor, video production commission) need formal decision at this gate. Defer or accelerate based on actual adoption data.

---

### Gate 4: Year 1 (May 31, 2027)

**What this gate decides**: Whether the Phase 2 corpus requires a full v2.0 refresh, whether the maintenance model is sustainable, and whether Phase 3 (new capability development beyond Phase 2 scope) is warranted.

**Metrics to measure**:
- Reach: Total organizations contacted across all three tiers (target: 110+ across Tier 1/2/3 + audience expansion contacts)
- Adoption: Organizations at Stage 2+ engagement (confirmed reading) vs. Stage 4+ (integration)
- Citation: Any legislative testimony, agency comment letter, legal filing, or peer-reviewed paper citing the corpus
- Threat model accuracy: Percentage of specific claims still accurate vs. requiring substantive update (target: 80% or more still accurate without major revision)
- Content staleness: Number of briefings requiring full rewrite vs. incremental update
- Maintenance sustainability: Can the threat monitoring cadence continue at current effort levels? Does the primary researcher have a backup?

**Decision criteria**:
- Reach >110 organizations, at least 5 organizations at Stage 4+ engagement, at least 1 legal/legislative citation, >80% threat model claims still accurate: Maintain and continue. Begin planning Phase 3 if resources exist.
- Reach 60–110 organizations, 2–4 Stage 4+ engagements, no citation, 60–80% threat model accurate: Sustain maintenance; do not expand. Prioritize getting existing adopters to deeper engagement over reaching new organizations.
- Reach <60 organizations or <2 Stage 4+ engagements: Conduct a frank evaluation of the distribution model. The problem may be the channel (Gist/email) rather than the content. Consider whether a single organizational partner with existing distribution infrastructure should take over corpus stewardship (FPF, EFF, or Georgetown CPT as candidate stewards).
- Threat model accuracy below 60% (more than 40% of claims require substantive revision): Archive May 2026 corpus as historical documentation. Begin Phase 3 as a new cycle with a fresh threat model.
- Maintenance unsustainable: Transfer stewardship to a Tier 2 organization with research capacity (Georgetown CPT, EFF, or Access Now are the candidates). This is a positive outcome if it means the corpus has institutional backing — not a failure.

---

## Section 5: Threat Model Maintenance and Currency

### The Systemic Approach

The threat update cadence established in threat-update-cadence.md provides the operational infrastructure. This section defines the five sentinel vectors specific to Phase 2's expanded threat landscape and the trigger-to-update procedure for each.

---

### Five Phase 2 Sentinel Threat Vectors

**Sentinel 1: Mobile Fortify deployment expansion**
Current status: 100,000+ field uses documented; NEC-powered; 15-year biometric data retention; no consent mechanism.
Monitoring source: ImmpolicyTracking.org, 404 Media, EFF Deeplinks, NPR Tech, Biometric Update.
Update trigger: New agency adoption (CBP, FBI, state/local law enforcement); new vendor contract; NEC contract renewal/replacement; false-positive incident documentation at scale; court ruling on warrantless handheld biometric collection.
Affected documents when triggered: opsec-playbook.md (biometric encounter section), immigration evasion playbook, activist organizing playbook.
Target update time: Within 1 week of confirmed trigger (Trigger Category 2 per threat-update-cadence.md).

**Sentinel 2: Flock Safety new agency deployments**
Current status: 5,000+ communities; primarily ALPR but expanding capabilities; contract with CBP for border zone deployment.
Monitoring source: Flock Safety company announcements, local government meeting minutes (most ALPR contracts are public procurement), EFF Street-Level Surveillance hub, ACLU state affiliates.
Update trigger: Deployment in major immigrant-population metro areas (Los Angeles, New York, Chicago, Houston, Miami) where the activist organizing playbook is most likely to be in use; any capability expansion beyond ALPR (facial recognition integration would be a major trigger).
Affected documents when triggered: activist organizing playbook (vehicle countermeasures section), threat matrix table.
Target update time: Within 2 weeks (Trigger Category 2).

**Sentinel 3: Palantir AIP autonomous flagging rollouts**
Current status: AIP deployed at Army ($10B ESA); documented in PHASE_2_SEQUENCING_STRATEGY.md Section 1.3; immigration and financial agency AIP deployment not yet confirmed.
Monitoring source: DefenseScoop, CNBC, USASpending.gov (Palantir contracts), FPDS, Palantir SEC filings (public company disclosures).
Update trigger: AIP deployment at ICE, CBP, DHS, or IRS Criminal Investigation confirmed in a new contract or modification; autonomous flagging capability described in any public contract document.
Affected documents when triggered: threat-model.md (behavioral de-anonymization section), financial resistance playbook (IRS surveillance section), advanced identity compartmentalization guide.
Target update time: Within 1 week (Trigger Category 1 or 2 depending on whether it changes countermeasure recommendations).

**Sentinel 4: Cellebrite Physical Analyzer capability updates**
Current status: Signal module documented (accesses Signal data from physically extracted device in AFU state); ICE $11M contract confirmed.
Monitoring source: Cellebrite official release notes (published publicly at cellebrite.com/en/company/blog/), ScienceDirect forensic analysis literature, Motherboard/404 Media, GrapheneOS blog.
Update trigger: New app extraction module (particularly WhatsApp, Telegram, Briar, or Wire — any messaging platform recommended in the corpus); significant expansion of AFU/BFU bypass capability; GrapheneOS-specific forensic vulnerability documented.
Affected documents when triggered: implementation-guide.md (device forensic hardening section), device hardening guide, journalist playbook (source communication security section), whistleblower playbook (device seizure section).
Target update time: Within 48 hours for a critical capability change that directly affects countermeasure recommendations (Trigger Category 1); within 1 week for expansion to new apps (Trigger Category 2).

**Sentinel 5: NSA Section 702 legislative and operational developments**
Current status: Post-June 12, 2026 deadline — outcome to be documented. Current: 45-day extension; warrant amendment failed Senate 42–50.
Monitoring source: Wyden Senate press releases, Privacy and Civil Liberties Oversight Board (PCLOB) publications, ACLU national security reporting, Nextgov/FCW, Just Security.
Update trigger: Reauthorization without warrant reform (expected — update to remove "pending deadline" urgency framing, set next deadline); reauthorization with warrant reform (unlikely — update advocacy sections to note the win and shift emphasis); any FISC or FISA Court of Review decision that materially changes Section 702 scope.
Affected documents when triggered: All briefings' policy advocacy sections; journalist playbook (foreign source communication section, PRISM section); whistleblower playbook (government network monitoring section).
Target update time: Within 48 hours of confirmed outcome (Trigger Category 1 per threat-update-cadence.md).

---

### Procedure: When Sentinel Triggers, Which Playbooks Update

The procedure established in threat-update-cadence.md applies uniformly. For Phase 2's expanded document set, the affected-documents mapping is:

| Sentinel | Core Corpus Sections | Playbooks | Guides |
|----------|---------------------|-----------|--------|
| Mobile Fortify expansion | opsec-playbook.md §Biometrics | Immigration, Activist | — |
| Flock Safety expansion | threat-model.md §ALPR | Activist | Aerial surveillance field guide |
| Palantir AIP | threat-model.md §Behavioral analysis | Financial, Immigration | Compartmentalization guide |
| Cellebrite update | implementation-guide.md §Device forensics | Journalist, Whistleblower | Device hardening guide |
| Section 702 | threat-model.md §NSA | Journalist, Whistleblower | — |

All updates follow the minimum-necessary-change principle: change only the specific claim that has become inaccurate. Do not rewrite surrounding sections. Increment the `updated` date in frontmatter. Log the change in threat-update-cadence.md update log.

---

## Section 6: Integration with Phase 1 Tier 1 Outreach

### How Phase 1 Feedback Informs Phase 2

Phase 1 Tier 1 outreach is not just distribution — it is the research phase for Phase 2 content. Every Tier 1 response is a data point about which threat scenarios are most salient for the actual at-risk population, which countermeasures are creating implementation friction, and which geographic or legal gaps the corpus does not yet address.

**Feedback types from Tier 1 that directly inform Phase 2 content**:
- "Our clients can't do data broker opt-outs because they don't have government-issued ID" → confirms DROP platform path is the key Phase 1 contribution; also confirms that the no-ID pathway needs to be expanded beyond California in Module 7's Texas supplement
- "The device hardening section is too complex for our clients" → confirms the need for Module 7's video primers; accelerates video script production
- "Can we get this in Spanish?" → confirms Spanish translation as Phase 2 priority; escalates Module 7's Spanish Part 0 to Month 4 (earlier than planned)
- "What about [new threat or tool not in corpus]?" → every such question is a Module 1 or 2 research task
- "We've started using this in client intake" → Score 4 signal; confirms Phase 2 is on track; use as credibility anchor in Tier 2 outreach

### When to Ask Phase 1 Recipients to Beta-Test Phase 2 Playbooks

The timing question depends on the playbook and the relationship established in Tier 1 outreach:
- Score 3+ contacts (confirmed corpus reading): Eligible for playbook beta-test request starting Week 8
- Score 4–5 contacts (integration signal, active adoption): Priority beta-test candidates; can be approached as early as Week 6 with a targeted ask for the playbook most relevant to their population
- The format of the ask: "We've completed a scenario-specific guide for [immigration/activist/journalist] security. Given that your organization is already using the core corpus, would a staff member be willing to review a draft and tell us whether it works for your clients?" One question, low friction, high value.

### Coordination: Phase 1 Recipients as Phase 2 Beta-Testers

Three Phase 1 Tier 1 organizations should be approached as explicit Phase 2 beta-testers by Week 10:
1. The highest-engagement immigration legal aid contact (Score 4–5): Immigration evasion playbook review
2. The highest-engagement community organization contact (Score 4–5): Activist organizing playbook or financial resistance playbook review (depending on their population)
3. Any Tier 1 contact that specifically asked about a Phase 2 scenario (e.g., DV, journalist, whistleblower): The relevant playbook for their question

The beta-test ask is distinct from the feedback collection process (which is passive and survey-based). Beta-testers are asked to read a specific playbook and give structured feedback: (1) Is the threat model accurate for your clients' situation? (2) Are the countermeasures actionable without technical expertise? (3) What's missing?

**Timing for asking Phase 1 recipients for playbook feedback**:
- Months 2–3 (August–September 2026): First beta-test asks to Score 4–5 Tier 1 contacts
- Month 4 (October 2026): Incorporate beta-test feedback into playbook revisions before full Tier 3 distribution
- This timeline ensures playbooks are refined before they reach the higher-scrutiny Tier 3 audience (policy organizations, law clinics)

---

## Section 7: Resource and Dependency Analysis

### Total Orchestrator Hours Estimate

| Module | Effort Estimate | Status |
|--------|----------------|--------|
| Module 1: Threat model expansion | 12–16 hours | Research base complete; production needed |
| Module 2: Advanced protection guides | 20–25 hours | Conceptual framework complete; production needed |
| Module 3: Playbook deployment coordination | 15–20 hours | All 6 playbooks written; distribution work needed |
| Module 4: Tier 2 pilot and feedback loop | 25–30 hours | Templates complete; execution and tracking needed |
| Module 5: Tier 3 institutional expansion | 28–37 hours | Contact lists complete; personalization and tracking needed |
| Module 6: Threat model maintenance (12 months) | 40–48 hours | Infrastructure established; ongoing execution |
| Module 7: Format diversification | 24–34 hours | Contingent; defer until adoption data confirms need |
| **Total** | **164–210 hours** | — |

The 100–150 hour estimate in the original scope appears to undercount Module 6 (ongoing maintenance) and Module 7 (if format diversification is fully executed). A realistic total is 120–165 hours if Module 7 is partially deferred. Monthly average: 10–14 hours/month over 12 months.

---

### Tool and Infrastructure Requirements

**Distribution infrastructure** (already established or low-cost):
- GitHub Gist (free): Core corpus and playbook hosting
- Bitly (free tier): Short URL tracking per document (one Bitly link per playbook for independent tracking)
- Gmail (existing): Outreach and follow-up
- Spreadsheet tracking (Google Sheets, existing): Contact tracking per tier

**New infrastructure needed for Phase 2**:
- Separate Bitly links for each of 6 playbooks (distinct from core corpus Bitly link) — requires upgrading to Bitly paid tier ($35/year) if more than 5 custom links are needed simultaneously, OR use free tier with one link per playbook deployed sequentially
- PDF generation tool for DV playbook (format requirement is PDF, not Gist) — Google Docs export is sufficient
- Google Alerts configuration (free): 8 sentinel alert streams established

**No new platform subscriptions required** for Modules 1–6. Module 7 (video production) would require a video hosting platform if commissioned content is produced — YouTube (free) is the lowest-friction option and is widely accessible to target audiences.

---

### External Dependencies

**Binding dependencies** (Phase 2 cannot fully proceed without these):
1. NNEDV Safety Net Project review of DV playbook: Without this, DV playbook cannot be distributed. Target: contact by Week 15; review complete by Month 5. No substitute validator exists for the safety planning escalation-risk language.
2. Nonprofit tax attorney review of financial resistance playbook: Without this, financial playbook formal distribution should be deferred. The financial playbook can circulate informally (via Gist link, not formal Tier 2/3 outreach) while waiting for this review.

**Preferred dependencies** (Phase 2 is better with these but can proceed without):
1. FPF pilot engagement for journalist playbook: If FPF does not engage with the pilot, proceed to full Tier 2D wave using CPJ and RCFP as primary channels. FPF is preferred but not required.
2. Security researcher technical validation for Module 2 advanced protection guides: If no Tier 2C contact provides technical feedback, proceed with publication and note in the guides that technical review is ongoing. Publish a "known review needed" flag in the frontmatter rather than delaying indefinitely.
3. Bilingual Tier 1 partner for Spanish translation: If no Tier 1 organization volunteers a staff translator by Month 4, contract a professional translator from the budget allocation below.

---

### Budget Estimate

Phase 2 has no required external costs for its core activities. All distribution, research, and coordination work uses existing free tools and orchestrator time. Optional cost-center items:

| Item | Estimated Cost | Priority | Decision Gate |
|------|---------------|----------|---------------|
| Bitly paid tier (custom links for 6 playbooks) | $35/year | Low | Gate 1: if click tracking per playbook is confirmed necessary |
| Spanish Part 0 translation (professional contractor) | $200–400 | Medium | Gate 2: if no Tier 1 bilingual staff partner identified |
| Nonprofit tax attorney review (financial playbook) | $0–500 (pro bono or informal) | High | Gate 1: initiate contact immediately; formalize by Gate 2 |
| Video production (4 primers, commissioned) | $3,200–8,000 | Low | Gate 3: only if adoption data shows video is a material barrier AND a production partner is identified |
| Annual accessibility audit of core corpus readability | $0 (self-assessment) | Low | Gate 4 |

**Total budget estimate**: $235–435 required costs (Bitly + translation if no partner) plus $0–8,000 contingent costs (video production). For a 12-month Phase 2 implementation, the realistic budget is under $500 unless video production is commissioned.

---

*Created: 2026-05-19. Drawn from PHASE_2_SEQUENCING_STRATEGY.md (Session 837), PHASE_2_SEQUENCING.md, TIER2_DISTRIBUTION_PREP.md, TIER3_DISTRIBUTION_PREP.md, PHASE_2_DEPLOYMENT_READINESS.md, and threat-update-cadence.md. All effort estimates are for orchestrator research and implementation time; user execution time for outreach campaign is separately estimated in PHASE_2_SEQUENCING.md at 65–85 hours over 20 weeks. Quarterly review dates: July 26, 2026 (Gate 1), September 30, 2026 (Gate 2), December 31, 2026 (Gate 3), May 31, 2027 (Gate 4).*
