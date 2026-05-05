---
title: "Post-Distribution Impact Tracker — Individual Adoption & Threat-Model Outcomes"
project: cybersecurity-hardening
created: 2026-05-05
version: 2.0
status: ready-for-use
supersedes: v1.0 (session 717, organizational-adoption focus)
depends-on: tier-1-success-metrics-framework.md, tier-1-feedback-collection-protocol.md, adoption-tracking-dashboard-spec.md
---

# Post-Distribution Impact Tracker v2.0

**Purpose**: Extend the organizational adoption tracking framework (v1.0) with individual-level adoption metrics by audience segment, threat-model-specific outcome measurement, temporal milestones, and failure mode detection. The v1.0 document tracks whether NILC or RAICES engages with the corpus. This document tracks whether the journalist, immigration attorney, activist, or undocumented immigrant actually implements the guidance and whether it changes their security posture.

**Lead finding**: The hardest measurement problem in security guidance is that effectiveness is a non-event — the source who was not exposed, the deportation that did not happen. The framework resolves this by tracking three proxy categories instead of the non-event itself: (1) verified implementation of countermeasures (did the person complete the action?), (2) near-miss prevention (did the person encounter a threat that the guidance helped deflect?), and (3) institutional acceptance (did the organization not experience adverse consequences from implementing the hardening?). All three are measurable. The non-event is not.

**Relationship to v1.0**: Read v1.0 (`post-distribution-impact-tracker.md`) for the organizational outreach tracking framework, 30/90/180-day follow-up email templates, stage-of-adoption model, and assessment gate structure. This document covers the individual-level layer above that organizational foundation.

---

## Section A: Individual Adoption Metrics by Audience Segment

### A.1 Journalists

**What adoption looks like at the individual level**

Journalists implementing the corpus move through four observable stages that do not require self-reporting to verify:

| Stage | Behavior | Observable Signal |
|-------|----------|------------------|
| 0 — Awareness | Read the guide | Download metric, help desk question |
| 1 — Tool installation | Installed Signal, ProtonMail, or Tails | Help desk confirmations, tool-specific download referral links |
| 2 — Operational integration | Using secure tools in active reporting | Requests for Signal contact info rather than phone, ProtonMail address on byline |
| 3 — Operational security practice change | Changed sourcing habits, cover story discipline, pattern-of-life awareness | Near-miss narrative, source contact via secure channel, no phone at protest |
| 4 — Incident prevention | Documented near-miss where hardening worked | Self-reported testimonial, incident narrative |

**Leading indicators (weeks 1-4 of distribution)**

- Referral link click-through on Signal download (if distribution uses a tracking link to Signal's download page): target 15% of journalist downloads trigger a tool installation within 7 days. The 89% journalist adoption baseline for Signal in democratic countries (per 2025 industry research) means most working journalists are not starting from zero — the marginal gain is moving sporadic users to operational discipline.
- Help desk inquiries about Tails OS USB creation: Tails remains the highest-friction installation in the guide. Any help desk question about Tails is a strong implementation signal — it means the person got past reading the guide to attempting installation.
- ProtonMail account creation via referral: measurable if a referral code or tracking link is embedded in the guide's ProtonMail setup instructions. Target: 5-10% of journalist guide downloads result in new ProtonMail account creation.

**Threat-model-specific outcome signals**

The journalist threat model centers on SIGINT collection, FBI interest via NSL or FISA Section 702, and source exposure. Direct outcome measurement is impossible without access to FISA court logs. Proxy outcomes:

- Source protection improvement: can a source now contact the journalist via Signal without that contact being logged by the journalist's carrier? Measurable via journalist self-report after 90 days ("my sources now contact me via Signal").
- Operational security incident prevention: did the journalist cover a sensitive story without a demonstrated compromise attempt? Self-report ("I covered the ICE raid without my source being identified") is the primary channel.
- Section 702 exposure reduction: journalists who move sensitive communications off commercial email onto ProtonMail or Signal reduce their data residency in Section 702 collection architecture. Not directly measurable, but verifiable via implementation confirmation.

**Calibration note**: As of May 2026, Section 702 was renewed for three years (through April 2029) without a warrant requirement or data broker loophole closure (House S.1318, April 29, 2026). This increases the stakes for journalist source protection and should be cited in guide distribution communications as evidence of active threat.

---

### A.2 Immigration Attorneys

**What adoption looks like at the individual level**

Immigration attorneys face a more concrete threat model than journalists: client communications can be subpoenaed, and attorney-client privilege is not absolute when a client is subject to civil immigration proceedings. Implementation stages:

| Stage | Behavior | Observable Signal |
|-------|----------|------------------|
| 0 — Awareness | Read the guide | Download or organizational referral |
| 1 — Communication protocol change | Adopted Signal for sensitive client communications | Signal contact on business card, client intake form includes Signal number |
| 2 — Encrypted file storage | Implemented VeraCrypt or equivalent for case files | IT support request for setup, self-report in 90-day follow-up |
| 3 — Client-facing integration | Walked clients through Part 0 (data broker opt-outs) as part of intake | Self-report, organization's intake checklist updated |
| 4 — California AB 60/DROP platform integration | Helping clients without government-issued ID complete DELETE Act DROP platform enrollment | DROP completion reports from clients, self-report |

**California AB 60 / DELETE Act DROP platform implementation tracking**

This is the corpus's most distinctive contribution to immigration attorney practice. The DROP platform (privacy.ca.gov/drop) launched January 1, 2026 and requires brokers to begin processing deletion requests August 1, 2026. The AB 60 → DELETE Act pathway allows undocumented California residents to use their California driver's license (not tied to SSN) to authenticate a DROP request, removing their data from 500+ registered data brokers.

Target adoption signal: attorneys at Tier 1 legal organizations in California reporting they have walked clients through the DROP platform in client intake. Measurable via:
- 90-day follow-up question asking specifically about DROP platform adoption
- DROP platform enrollment completion confirmation from clients (if attorneys report back)
- Legal aid clinic training curricula that include the DROP pathway step

**ELITE system countermeasure adoption**

The corpus documents Palantir ELITE's address confidence scoring as a mechanism ICE uses to prioritize deportation targeting. Attorney-level countermeasure: advising clients to use address masking (mail forwarding services, P.O. boxes, or nonprofit intermediary addresses) rather than home addresses in public-facing records.

Observable signal: attorneys at immigration legal aid organizations reporting that they added address masking guidance to client intake. Verifiable via 90-day follow-up question ("Did your organization add any new guidance on address records management for clients?").

---

### A.3 Activists

**What adoption looks like at the individual level**

Activist threat models in the 2026 context involve three distinct adversary types: (1) local law enforcement with IMSI catchers and protest-area surveillance, (2) federal surveillance under 28 CFR Part 23 fusion center data sharing, and (3) financial de-platforming. Implementation is measurable at the device, communication, and financial layers.

**Device hardening adoption signals**

- GrapheneOS or CalyxOS installation (verifiable via help desk inquiries about verified bootloader installation; these are the highest-friction steps in the device hardening guide)
- Faraday bag procurement (traceable via referral links to procurement vendors if included in guide)
- EFF Rayhunter deployment: Rayhunter (released March 2025, updated September 2025) is a $20 Orbic RC400L hotspot-based IMSI catcher detector. Adoption by activists constitutes a measurable technical countermeasure. Rayhunter deployment in protest contexts is verifiable via self-report and community reports of CSS detections.

**Communication security adoption signals**

- Signal group operational security: not just using Signal but using disappearing messages, screen security, and not including full member lists. Measurable via training session self-report ("I now use disappearing messages in all organizing Signal chats").
- Pattern-of-life evasion practices: leaving phone at home during sensitive organizing meetings, using a burner device for protest-adjacent activity. Self-report only; not verifiable externally.

**Financial compartmentalization adoption signals**

- Monero adoption for financial contributions to activist work is measurable via community reports. As of early 2026, Monero dominates 58% of the privacy coin market with an all-time high of $798.91 reached January 14, 2026. Key caveat: Chainalysis Reactor 3.0 (launched January 2025) improved privacy coin flow detection by 42% — activists should be aware that Monero's privacy protections are not absolute and have been improving in the adversary's favor.
- Cash contribution protocols: switching from Venmo/PayPal to cash or money orders for dues. Measurable via organizer self-report.

**Leading indicators (weeks 1-4)**

- Rayhunter purchase referral links: if guide includes a Rayhunter purchase link to sts-collective.com or a similar distributor, click-through and purchase are verifiable proxy signals.
- Help desk questions about GrapheneOS verified bootloader process: highest-friction step in the device hardening guide; any question indicates serious implementation attempt.
- Pattern-of-life evasion questions (e.g., "how do I keep my house address off public records?") indicate the person is engaging with the strategic threat model, not just the tool checklist.

---

### A.4 Undocumented Immigrants

**What adoption looks like at the individual level**

This is the audience segment with the highest stakes and the lowest feedback rate. Undocumented immigrants implementing the corpus face direct physical risk. The feedback infrastructure must be designed to function at near-zero response rates while still producing actionable signals.

**ELITE system countermeasure adoption signals**

Palantir ELITE's address confidence scoring mechanism aggregates utility records, rental history, credit headers, and commercial data broker records into a numerical score that ICE prioritizes for enforcement targeting. Countermeasures in the corpus include address masking and data broker opt-outs. Observable adoption signals:

- DROP platform enrollment completion: measurable if legal aid organizations track client DROP enrollment as part of intake. California-based organizations can report completion rates.
- Address masking implementation: use of mail forwarding service, P.O. box, or organizational intermediary address. Self-report only; verifiable via 90-day follow-up to referring organizations.
- Data broker manual opt-out completion: the 40-60 hour manual process yields 85%+ broker removal over 3-6 months. Completion measurable via self-report ("I have completed opt-outs at 50+ brokers"); automated services ($90-130/year) are verifiable via subscription confirmation.

**DROP platform timing caveat**: Data brokers must begin processing deletion requests August 1, 2026. Any DROP enrollment before that date is real and legally binding, but the deletion processing window does not begin until August 2026. Clients enrolled in January-July 2026 should receive reminder communications around August 1 to confirm deletion is being processed.

**ICE encounter reduction**

ICE encounter reduction is a non-event that cannot be attributed to the corpus without a counterfactual. The proxy measurement strategy for this audience:

1. **Self-reported near-miss narratives**: "ICE came to my neighbor's address, not mine, and I believe the address masking helped." This is the highest-value feedback and should be actively solicited via anonymous channels (Signal number, encrypted form, paper form at legal aid office).
2. **Referral organization reports**: Legal aid organizations can aggregate reports of clients who experienced ICE contact and whether the contact involved the client's address, device data, or other data that hardening would have protected.
3. **DROP enrollment completion rates** as a leading indicator: completion is a prerequisite for data broker exposure reduction. High completion rates predict (but do not prove) reduced ELITE address confidence scores over 3-6 months.

**Communication safety signals**

- Signal adoption for family and trusted contact communication: measurable via referral link clicks and help desk inquiries
- Avoidance of unencrypted SMS for sensitive communications with legal representatives: verifiable via attorney adoption reports ("our clients now contact us via Signal")

**Leading indicators (weeks 1-4)**

Because direct feedback from undocumented immigrants is unsafe and impractical, the leading indicators are all mediated through referring organizations:

- Legal aid organizations reporting that staff have walked clients through Part 0 (data broker opt-outs)
- Community organizations reporting Signal adoption at community meetings
- DROP platform enrollment volumes in California (measurable via CPPA aggregate data if published)

---

## Section B: Organizational Adoption Metrics

*Detailed organizational-level tracking is documented in the v1.0 `post-distribution-impact-tracker.md` (stage model, follow-up templates, 30/90/180-day assessment gates). This section provides supplementary metrics not in v1.0.*

### B.1 Newsroom Hardening Policy Adoption

Target signal: a newsroom security policy document that cites or incorporates the corpus's recommendations on Signal, end-to-end communication, encrypted file storage, or VPN mandates.

Observable via:
- FPF (Freedom of the Press Foundation) training integration: FPF's Digital Security Program delivered workshops to 1,300+ journalists in 2023. If FPF integrates the corpus into its curriculum (a Tier 2 conversion target), this is the highest-leverage organizational adoption signal for journalist-facing distribution.
- IRE (Investigative Reporters and Editors) training integration: IRE trains journalists at more than 50 topics per workshop; digital security is one of their core training areas. IRE curriculum adoption is verifiable via the IRE conference schedule and session descriptions.
- SPJ Journalist's Toolbox inclusion: the SPJ Digital Security section is a practitioner reference point; inclusion is publicly verifiable.

### B.2 Legal Aid Organization Staff Training

Target signal: a legal aid organization that has added digital security content from the corpus to staff onboarding or professional development training.

Observable via:
- 90-day follow-up question: "Has [Org] added any digital security training to staff onboarding in the past 90 days?"
- Training curriculum documents shared by implementing organizations (with permission)
- Organizational newsletter or social media posts announcing the training

### B.3 Activist Collective OpSec Documentation

Target signal: a shared communication standard, financial opacity procedure, or law enforcement interaction protocol adopted by an activist collective that cites or incorporates corpus guidance.

Observable via:
- Community referrals: if an activist collective asks to be connected to the corpus author for guidance, this indicates Stage 2+ adoption
- Published collective security guides that reference the corpus's Tier 1 or Tier 2 recommendations

### B.4 Educational Institution Curriculum Adoption

Target signal: journalism school, law school, or activist training program assigns the corpus as assigned or reference reading.

Observable via:
- Google Scholar alert for corpus title or unique content markers
- IRE/J-school professor referral (if contacted directly)
- Law school clinical program adoption (verifiable via syllabi searches or faculty outreach)

---

## Section C: Threat-Model-Specific Outcome Measurement

### C.1 Journalist Threat Model: Source Protection

**What success looks like**: A journalist's source was able to make contact via Signal or another secure channel without that contact appearing in the journalist's phone carrier records, commercial data broker data, or FBI/NSL-compelled disclosure.

**What you can measure**:

| Outcome | Measurement Method | Confidence Level |
|---------|-------------------|-----------------|
| Source contacted journalist via Signal | Self-report: "my source used Signal as the guide recommended" | Medium — self-attributed |
| Source's contact not in carrier records | Not measurable without carrier records access | N/A |
| Journalist used Tails for story research | Self-report: "I used Tails when downloading leaked documents" | Medium |
| Journalist did not use work email for sensitive correspondence | Self-report: "I moved to ProtonMail for all source communications" | Medium |
| Journalist covered a high-risk story without a demonstrated compromise attempt | Self-report: no known adverse outcome after 90+ days | Low — non-event |

**Unique content marker for attribution**: A journalist who specifically references "address confidence scoring" or "ELITE system data purchase architecture" in a source protection discussion is referencing content unique to this corpus. High attribution confidence.

### C.2 Immigration Attorney Threat Model: Client Communication Protection

**What success looks like**: A client communication was not discovered by ICE through subpoena of the attorney's email records or device seizure, because the communication occurred via Signal with disappearing messages.

**What you can measure**:

| Outcome | Measurement Method | Confidence Level |
|---------|-------------------|-----------------|
| Client's data broker records removed via DROP | DROP completion confirmation via referring org | High (actionable) |
| Attorney switched from unencrypted email to Signal for client comms | Self-report + observable (Signal number on business card) | Medium |
| Client case not compromised by device seizure | Self-report after adverse event investigation | Low — non-event in most cases |
| ICE subpoena of attorney communications unsuccessful | Legal proceeding record — only visible if contested | Low — rare event |
| Client address not in ELITE high-confidence tier | Not measurable without ELITE database access | N/A |

**Attribution unique content markers**: An attorney who references the California AB 60 → DROP platform pathway or the ELITE "address confidence score" mechanism is referencing corpus-specific content.

### C.3 Activist Threat Model: Law Enforcement Scrutiny Reduction

**What success looks like**: An activist attending a protest was not identified by an IMSI catcher because they left their phone at home, or was alerted to IMSI catcher presence by Rayhunter.

**What you can measure**:

| Outcome | Measurement Method | Confidence Level |
|---------|-------------------|-----------------|
| IMSI catcher presence detected at protest via Rayhunter | Rayhunter device log + community corroboration | High (technically verifiable) |
| Activist left phone at home during sensitive meeting | Self-report | Medium |
| Activist's financial contributions not traceable via Venmo/CashApp | Self-report: switched to Monero/cash | Medium |
| Activist avoided FISA surveillance by moving off commercial email | Not measurable without FISA court records | N/A |
| No adverse law enforcement action within 12 months of hardening | Self-report: no contact, arrest, or surveillance indicator | Low — non-event |

**Rayhunter deployment as a leading indicator**: If activists in your distribution network adopt Rayhunter, this produces technically verifiable data on IMSI catcher deployment in protest contexts. The EFF's September 2025 update confirmed likely CSS detections in Chicago and New York. Activist Rayhunter deployment reports are a high-value community contribution that serves both personal protection and broader civil liberties research.

### C.4 Undocumented Immigrant Threat Model: ICE Encounter Prevention

**What success looks like**: An undocumented immigrant's address was masked from Palantir ELITE's address confidence scoring, reducing their prioritization for enforcement targeting.

**What you can measure**:

| Outcome | Measurement Method | Confidence Level |
|---------|-------------------|-----------------|
| DROP platform enrollment completed | Completion confirmation via legal aid org referral | High (actionable) |
| 80%+ data broker records removed 6 months post-enrollment | Self-report or DeleteMe/Kanary dashboard screenshot | Medium |
| Address masking implemented (forwarding service) | Self-report | Medium |
| No ICE home visit in 12 months post-hardening | Self-report: no ICE encounter at known address | Low — non-event |
| Community-level: ICE encounters declined in implementing community | Aggregated from legal aid org caseload reports | Low — confounded |

**Critical caveat on DROP platform timing**: The August 1, 2026 processing deadline means that DROP enrollments before that date establish a legal obligation for broker deletion but do not produce immediate data removal. Outcome measurement for DROP effectiveness should not begin until November 2026 at the earliest (90 days after the August processing deadline).

---

## Section D: Temporal Milestones

### Week 1-2: Access and Delivery Confirmation

| Metric | Target | Data Source |
|--------|--------|-------------|
| Guide downloads / Gist views | Baseline + 100 views week 1 | Gist traffic dashboard |
| First organizational acknowledgment | At least 1 Tier 1A reply | Email tracker |
| Help desk inquiries received | Any (volume indicates active engagement) | Feedback email |
| Tool referral link clicks (Signal, Tails, ProtonMail) | 10%+ of Gist views | Bitly or referral tracking |

### Week 3-4: Early Adoption Signals

| Metric | Target | Data Source |
|--------|--------|-------------|
| Tool installation confirmations | 3-5 users confirm Signal or ProtonMail setup | Help desk or 30-day follow-up |
| Tails OS help desk inquiries | At least 1 (high-friction signal) | Feedback email |
| First organizational referral | 1 new warm contact generated | Email tracker Q3 response |
| Testimonial or positive social mention | 1 (Reddit/Mastodon) | Social media monitoring |
| DROP platform enrollment question | Any inquiry about DROP eligibility or process | Feedback email |

### Month 2-3: First Organizational Inquiries

| Metric | Target | Data Source |
|--------|--------|-------------|
| Newsroom security policy inquiry | 1+ newsroom contacts asking about Tier 2 implementation | Email tracker |
| Law school curriculum inquiry | 1+ faculty or clinic contact | Tier 2 academic outreach tracker |
| Organizational Stage 2+ adoption | 20% of Tier 1 contacts reached internal discussion | 30-day follow-up responses |
| Gist view trajectory | Month 2 views > Month 1 views (organic growth) | Gist traffic log |
| Feedback form responses | 20+ form submissions | Feedback form dashboard |

### Month 4-6: Published Outcomes

| Metric | Target | Data Source |
|--------|--------|-------------|
| Published citation in organizational policy | 1 document citing the corpus | Google Alert, Overton.io |
| Journalist article referencing corpus | 1 story mentioning ELITE system, data brokers, or source protection drawing on corpus | Google Alert |
| Law school course assignment | 1 syllabus including corpus | Faculty follow-up |
| DROP completion reports (California) | Reports from 2+ legal aid orgs of client DROP enrollments | 90-day follow-up Q |
| Case study interview completed | 1 implementing organization | 180-day outreach |

### Month 6-12: Incident Prevention Evidence

| Metric | Target | Data Source |
|--------|--------|-------------|
| Near-miss narratives received | 1-3 user-reported prevented compromise stories | Anonymous feedback channel |
| IMSI catcher detection reports (Rayhunter) | Any community reports of CSS detection while using corpus guidance | Community self-report |
| Source contact improvement reports (journalists) | 2+ journalists reporting secure channel adoption by sources | 90-day/180-day follow-up |
| DROP effectiveness confirmation | 1+ reports of substantial broker removal after August 1, 2026 deadline | Legal aid org 90-day Q |
| Rayhunter adoption rate | Any adoption reports from activist segment | Community follow-up |

### 12+ Months: Diffusion Analysis

| Metric | Target | Data Source |
|--------|--------|-------------|
| Journalist-to-journalist training | 1 documented case of a journalist training others using corpus | Testimonial or referral |
| Attorney-to-attorney sharing | 1 documented case of an attorney distributing to a peer network | Organizational follow-up |
| Academic citation | 1 preprint or working paper citing corpus | Google Scholar alert |
| Community normalization | An organization describes corpus recommendations as "standard practice" | Case study interview |
| Legal filing citation | 1 civil rights filing citing ELITE documentation | CourtListener search |

---

## Section E: Failure Mode Detection and Mitigation

### E.1 Under-Adoption

**Detection threshold**: Fewer than 1,000 combined downloads/Gist views in Month 1. Reply rate below 15% from Tier 1 organizational contacts. No individual user help desk inquiries within 30 days.

**Root causes**:
- Distribution channel failure: the corpus did not reach the target audience, or was filtered before delivery
- Audience mismatch: the framing does not speak to the audience's immediate concerns
- Discovery barrier: the corpus is not findable by people who are not already in the direct outreach network

**Mitigation**:
- Expand distribution: submit to r/immigration, r/privacy, r/netsec; share in Signal groups for journalist networks; contact NILC, RAICES, and United We Dream directly with personalized outreach
- Revise framing: if "cybersecurity" framing is not landing, try "ICE data systems" or "protecting your records from government databases" framing for undocumented immigrant audience
- Publish standalone one-page summary: a shorter, print-ready one-page with the most critical steps (data broker opt-out, DROP platform) is more shareable than the full corpus

### E.2 High-Adoption but High-Confusion

**Detection threshold**: High download volume (1,000+ views) combined with high help desk inquiry rate indicating configuration errors, not completion. More than 20% of feedback form responses indicate confusion about a specific step.

**Root causes**:
- Technical sections above staff capacity: Tails OS installation, VeraCrypt, or GrapheneOS installation steps are too complex without additional context
- Platform inconsistency: guide instructions differ from current tool interface (Signal/ProtonMail update broke a step)
- Language barrier: English-only guide is inaccessible to undocumented immigrant audiences

**Mitigation**:
- Produce quick-start videos: a 3-5 minute screen recording for Tails OS USB creation, Signal setup, and DROP enrollment resolves the most common friction points
- Create simplified checklist: a one-page "do these five things first" checklist for each audience segment (journalist, attorney, activist, undocumented immigrant)
- Spanish-language translation: Part 0 (data broker opt-outs) and the DROP platform pathway are the highest-priority sections for translation
- Quarterly version review: establish a 90-day review cycle for tool installation steps; Signal, ProtonMail, and Tails release updates frequently

### E.3 Organizational Resistance

**Detection threshold**: Three or more explicit rejection responses from organizational contacts, or zero new organizational policy adoptions after 90 days in Tier 2 outreach.

**Root causes**:
- Operational infeasibility: Signal adoption requires clients to have smartphones; some legal aid clients do not
- Workflow disruption: encrypted communications workflows require training time organizations cannot commit
- Liability concern: organizations worry that recommending specific tools creates liability if the tool fails
- Cost barriers: hardware procurement (Faraday bags, burner devices, Rayhunter) is outside operating budgets

**Mitigation**:
- Produce low-threshold entry version: a "minimum viable hardening" guide for organizations with constrained resources (Signal only, no hardware requirements, no Tails)
- Address liability concerns explicitly: add a section to the corpus explaining that "best effort" security recommendations carry no warranty and recommending organizations have staff review with their general counsel
- Identify organizational security team liaisons: if direct-service staff cannot implement the full guide, route to IT or security staff who can implement at the infrastructure level
- Connect with digital security funders: Digital Defenders Partnership and Front Line Defenders provide implementation grants to civil society organizations; add a section pointing organizations to these resources

### E.4 Tool Ecosystem Changes

**Detection threshold**: Help desk inquiries indicating that a specific guide step fails on current versions of the tool. Three or more reports of a specific installation failure.

**Root causes**:
- Signal, ProtonMail, or Tails updated their interface or installation process after the guide was written
- California DROP platform changed its authentication process (AB 1766 ID expansion introduced new pathways)
- CPPA changed the DROP enrollment process (new regulations effective November 2025)

**Mitigation**:
- Quarterly review cycle: calendar reminders to check each tool's release notes and verify guide steps on the first Monday of each quarter (August, November, February, May)
- Establish version tracking: note the version of each tool when instructions are written; add a "verified as of [date] with [tool version]" annotation to each installation section
- Maintain tool-maintainer contact: EFF (Tails partnership), Signal Foundation, Proton AG all have community contact channels; establish a relationship to get early warnings of breaking changes
- Drop platform monitoring: follow CPPA announcements (cppa.ca.gov) for DROP platform updates; the August 1, 2026 processing deadline is the next significant event to monitor

---

## Measurement Dashboard Summary Table

| Metric | Timeline | Success Threshold | Failure Mode | Mitigation |
|--------|----------|------------------|--------------|-----------|
| Gist views | 30 days | 300+ | <100 | Expand distribution channels |
| Org acknowledgment rate (Tier 1A) | 30 days | 35%+ | <15% | Re-send with shorter subject; verify contacts |
| Tool referral link clicks | 30 days | 10% of views | <3% | Embed direct links; add "install now" CTAs |
| Help desk inquiries received | 30 days | Any | Zero at day 21 | Add feedback email prominently to guide |
| Stage 2+ org adoption | 90 days | 20% of Tier 1 contacts | <10% | Revise corpus format; produce PDF |
| Individual testimonials | 90 days | 2+ | 0 | Solicit directly via 90-day follow-up |
| Referrals generated | 90 days | 3+ warm contacts | 0 | Add explicit referral prompt to follow-up |
| DROP enrollment confirmations | 90 days | 2+ legal aid orgs report | 0 | Follow up directly with CA-based legal aid contacts |
| Organizational policy citation | 6 months | 1+ | 0 by month 6 | Prioritize Tier 2 academic/digital rights outreach |
| Near-miss narratives | 6-12 months | 1-3 | 0 | Anonymous channel must be prominently accessible |
| Academic citation | 12 months | 1+ | 0 | September re-engagement of academic contacts |

---

*Document complete. Use in conjunction with `tier-1-success-metrics-framework.md` (per-organization tracking), `tier-1-feedback-collection-protocol.md` (email follow-up templates and CRM integration), and `adoption-tracking-dashboard-spec.md` (passive monitoring infrastructure). The three files together constitute the complete operational tracking system. This document adds the individual-segment and threat-model-specific measurement layer.*

**Sources**:
- Signal adoption among journalists: [Signal User Stats 2026](https://www.engagecoders.com/signal-user-statistics-how-many-people-use-signal/); [Signal Statistics 2025](https://electroiq.com/stats/signal-statistics/)
- California DELETE Act DROP platform: [California DROP Platform](https://privacy.ca.gov/drop/); [ByteBack Law DROP launch](https://www.bytebacklaw.com/2026/02/californias-deletion-request-and-opt-out-platform-drop-is-live/)
- Section 702 renewal (S.1318, April 29, 2026): internal project tracking (see surveillance-tracking.md)
- IMSI catcher detection via Rayhunter: [EFF Rayhunter announcement](https://www.eff.org/deeplinks/2025/03/meet-rayhunter-new-open-source-tool-eff-detect-cellular-spying); [EFF Rayhunter findings 2025](https://www.eff.org/deeplinks/2025/09/rayhunter-what-we-have-found-so-far)
- Monero privacy effectiveness and Chainalysis detection: [TRM Labs Monero research](https://www.trmlabs.com/resources/blog/the-rise-of-monero-traceability-challenges-and-research-review); [State of Surveillance data broker ICE contracts](https://stateofsurveillance.org/articles/corporate/data-brokers-ice-contracts/)
- SAFETAG civil society security adoption outcomes: [Internews SAFETAG evaluation](https://greaterinternetfreedom.org/success_stories/evaluation-findings-safetag-audits-increase-digital-security-of-organizations-and-lead-to-changes-in-attitude-and-behavior/)
- Security awareness training effectiveness: [Fortinet 2025 Security Awareness Report](https://www.fortinet.com/blog/industry-trends/2025-security-awareness-report-why-training-works-and-where-organizations-still-fall-short)
- FPF digital security training reach: [FPF Digital Security Education](https://freedom.press/digisec/)
