---
title: "Phase 1 Impact Evaluation Framework"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Comprehensive impact measurement framework for Phase 1 distribution across 45 Tier 1
  organizations in 7 constituencies. Covers success metrics, measurement methodology,
  per-constituency thresholds, decision triggers, and contingency activation protocols.
word_count: ~2800
companion_files:
  - PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md
  - PHASE_1_DECISION_TREES.md
  - PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md
  - PHASE_1_DISTRIBUTION_MEASUREMENT_PLAYBOOK.md
  - DISTRIBUTION_GIST_URLS.md
  - DISTRIBUTION_OUTREACH_CONTACTS.md
purpose: >
  Eliminates guessing about Phase 1 success. Enables data-driven Phase 2 sequencing
  instead of calendar-driven. Provides early warning if Phase 1 is failing by Day 7.
  If Phase 1 exceeds targets, enables same-day Phase 2 activation.
---

# Phase 1 Impact Evaluation Framework

**Version 1.0 — May 26, 2026**

**Lead finding**: The Day 7 checkpoint is the highest-leverage monitoring point in Phase 1. Signal patterns at Day 7 — reply timing, Bitly click velocity, Gist view delta — predict 30-day and 60-day trajectories with high accuracy. A framework that only measures at Day 30 will waste 23 days of correctable drift. This document arms the Day 7 checkpoint with specific thresholds, routes signals to pre-built contingency protocols, and connects each checkpoint to a concrete Phase 2 sequencing decision.

---

## 1. What "Success" Means for Phase 1

Phase 1 has three distinct success definitions that operate at different time horizons. They are not interchangeable.

**Minimum viable success (Day 7)**: Phase 1 materials have been received, opened, and read by at least one representative of each of the 7 constituencies. Evidence: Bitly clicks on at least 3 distinct Gist documents, at least one reply to any Tier 1 email that goes beyond a form OOO response.

**Distribution success (Day 30)**: At least 50% of Tier 1 contacts have replied substantively, at least 3 cross-organizational references have been detected (one organization telling another about the framework), and at least 2 adoption signals have been recorded in the adoption signal registry. Evidence: Gmail label counts, Bitly click velocity, partner-reported referrals, web search for framework vocabulary in published documents.

**Movement-scale impact (Day 60)**: At least 15 organizations have integrated Phase 1 materials into operational practice (curriculum, litigation toolkit, policy brief, training program, governance document), and at least 100 people have been trained on or exposed to Phase 1 frameworks through organizational use. Evidence: Partner survey responses, web monitoring, direct contact log annotations, citation detection.

These three definitions correspond directly to the three decision checkpoints in Section 4. Do not conflate them — a strong Day 7 does not guarantee Day 30 success, and a weak Day 7 does not mean Phase 1 has failed.

---

## 2. Per-Domain Success Definition

Phase 1 covers 40 core domains plus Domain 37 (expanded). Success is not uniform across domains — some domains are inherently slow-moving (constitutional theory) while others have immediate operational utility (litigation toolkits, model briefs). The following domain-tier structure governs per-domain success expectations:

**Tier A — Immediate operational utility (target: adoption signal within Day 30)**
- Domain 37 (Federal Executive Interference / Election Security): Target audience is election protection organizations and law school election law clinics. Adoption signal = incorporation into a clinic seminar or election security toolkit. Measurement: Email reply from election org, or web-detectable citation in a published election security brief.
- Domain 29 (Prosecutorial Weaponization): Target is civil rights organizations and immigration legal aid. Adoption signal = reference in a brief, motion, or client advisory. Measurement: Direct contact report or PACER docket search for framework vocabulary.
- Domain 39 (Healthcare as Democratic Infrastructure): Target is policy advocacy organizations; June 1 HHS deadline makes this time-critical. Adoption signal = citation in public comment, policy brief, or state advocacy document. Measurement: Regulations.gov comment search + partner report.

**Tier B — Medium adoption cycle (target: adoption signal within Day 60)**
- Domain 1 (Voting Rights and Elections), Domain 6 (Judicial Independence), Domain 9 (Federalism), Domain 26 (Accountability Infrastructure), Domain 33 (State Autocratization): Target is academic and policy research organizations. Adoption signal = citation in a working paper, amicus brief, or policy report. Measurement: Google Scholar alert, SSRN tracking, partner report.

**Tier C — Long-cycle academic domains (target: integration signal within Day 90)**
- Constitutional theory domains, comparative democracy domains, and domains requiring peer review cycles. These are not expected to show adoption signals within Day 60. Track separately; do not penalize Phase 1 for slow Tier C signals when making Phase 2 go/no-go decisions.

**Cross-domain multiplier effect**: The primary success signal for Phase 1 is not per-domain adoption but cross-domain synthesis — when a recipient contacts say that they are using the framework as a whole rather than a single domain. This is a qualitatively different signal from domain-specific adoption and should be scored at 3x the weight of single-domain adoption in the engagement tracker.

---

## 3. Measurement Methodology

All measurement methods must meet two criteria: they must be automatable or require less than 5 minutes of manual data entry per week, and they must not require contacting Tier 1 organizations to ask whether they have adopted the framework.

### 3.1 GitHub Gist View Tracking (automated, weekly)

The primary passive engagement signal is Gist view count delta. Each week, pull the view count from each live Gist and record the delta from the prior week. The canonical Gist URLs are documented in DISTRIBUTION_GIST_URLS.md.

**Automation method**: GitHub does not provide an API for anonymous Gist view counts. The automated workaround is a weekly scheduled check via Bitly click data (Bitly tracks clicks on the short URLs that resolve to each Gist — see PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md Section 1.1 for setup). Bitly free tier provides daily and weekly click counts per link. Record in Column G of the "Gist View Log" sheet in the measurement dashboard.

**Spike detection**: A single-day Bitly spike of more than 5 clicks on any link is a flag event. Cross-reference the spike date against the email wave send date. If the spike occurs 24-72 hours after a wave send, it confirms delivery and click-through. If a spike occurs with no corresponding send (organic amplification), flag it as a network multiplier signal and record the referrer country if visible in Bitly.

**Weekly time required**: 5 minutes. Log in to Bitly, record daily click totals for each link, enter delta in dashboard.

### 3.2 Email Engagement Tracking

**Reply rate tracking**: The Gmail label structure (phase1-outreach/sent/wave-N, phase1-outreach/replies/[score 1-5]) documented in PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md Section 1.2 provides the raw data. The reply rate calculation is: (count of Score 2+ replies) / (count of confirmed-delivered emails in that wave). Do not include bounces or OOO-only responses in the denominator.

**Reply content analysis**: Each reply is scored using the 5-level scoring system from PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md. For Phase 2 decision purposes, only Score 3+ replies (substantive engagement, request for additional information, forward to colleague, or explicit adoption statement) count toward the "strong engagement" threshold. Score 1-2 replies (acknowledgment, polite decline) do not count toward trajectory signals.

**Forwarding detection**: If a Tier 1 contact reports forwarding the framework to a colleague, or if you receive an unsolicited email from someone not on the Tier 1 list who found the framework through a contact, this is a network multiplier event. Score it as a "referral" in Column J of the Master Contact Log. Each referral is weighted 3x a standard reply in the composite engagement score.

**Weekly time required**: 5 minutes. Review Gmail labels, score any new replies, enter scores in dashboard.

### 3.3 Web Analytics and Open-Web Monitoring

**Google Alerts**: Set three alerts before Phase 1 launch: (1) "35-domain democratic renewal framework", (2) "democratic renewal framework" + law OR litigation, (3) [author name/handle if applicable]. These alerts will catch any external mention, citation, or repost of Phase 1 materials in indexed web documents. Alerts arrive by email; forward relevant alerts to a dedicated Gmail label.

**SSRN monitoring**: Set up an SSRN author alert for any Tier 1 academic contact who downloads the framework materials. SSRN sends weekly digests of new uploads by followed authors. Cross-reference any new SSRN upload from a Tier 1 contact against Phase 1 domains — if they upload a paper citing framework vocabulary, score it as an academic adoption signal.

**Regulations.gov comment search**: For Domain 39 (Healthcare) and Domain 42 (DEA rescheduling), check the relevant comment docket for any public comment that cites the framework or uses its vocabulary. This is a Tier A adoption signal. Time required: 5 minutes per docket per week.

**Weekly time required**: 8 minutes across all three channels.

### 3.4 Partner Feedback Forms

A one-click survey template is deployed once per constituency at the Day 30 checkpoint. The survey is three questions maximum, delivered via Google Forms, and linked in a brief follow-up email sent 28-30 days after the initial outreach. The survey is voluntary and framed as a 60-second check-in, not an evaluation.

**Standard three questions (all constituencies)**:
1. "Have you incorporated any Phase 1 materials into your organization's work? (Yes / Not yet / Passed to a colleague)"
2. "If yes, which area: curriculum / litigation toolkit / policy brief / training program / governance document / other"
3. "Would you welcome a brief call to discuss the research further? (Yes / Not now)"

**Constituency-specific question (added as Question 4 for targeted constituencies)**:
- Law schools: "Has any student organization, clinic, or course incorporated these materials?"
- Immigration legal aid: "Have you incorporated any model brief language or amicus framework?"
- Labor unions: "Has any local union chapter or training program engaged with these materials?"

**Survey data entry**: Enter responses into the "Adoption Signals" sheet in the measurement dashboard. Time required: 3 minutes per response. Expected response rate from the survey: 15-30% of Tier 1 contacts.

### 3.5 Network Analysis (Cross-Organizational References)

The highest-value measurement in Phase 1 is the network multiplier effect: does one law school adoption lead to three to five peer school adoptions? This effect is measured through:

**Direct referral logging**: When a new contact reaches out citing a Tier 1 contact as the source, record in Column J ("Referral Source") of the Master Contact Log. Track: referring organization, referred organization, domain(s) referenced, date.

**Cross-organizational reference detection in replies**: When a Tier 1 reply mentions having "shared with colleagues at [other organization]" or "forwarded to our [role] at [institution]," treat this as a preliminary network event. Score it as a half-referral until confirmed by contact from the referred organization.

**Citation chain analysis (Day 60)**: At Day 60, conduct a structured search of PACER, Google Scholar, SSRN, and public policy databases for any document that cites the framework. Map the citation chain: which Tier 1 contact cited it first, what their organization published, and whether peer organizations then cited that document. This is the primary evidence for the "network multiplier" claim in Phase 2 solicitation materials.

---

## 4. Per-Constituency Success Thresholds

The following thresholds are specific and must not be aggregated across constituencies. A strong result from law schools does not compensate for zero signals from mutual aid networks.

### Constituency 1: Law Schools (target: 12 contacts across HLS, Columbia, Yale, NYU, Stanford, Berkeley, Chicago, UC Davis)

**Primary metric**: Reply rate. Target is 25% substantive reply rate (Score 3+) within Day 30.
**Adoption signal definition**: Any of — (a) explicit statement that the research will be used in a seminar, clinic, or course; (b) request for a shareable version for students; (c) faculty citation in a working paper or draft article; (d) student organization outreach attributable to faculty introduction.
**Day 7 minimum**: At least 2 law school contacts have opened the email (confirmed by Bitly click on the Gist link embedded in the law school outreach).
**Day 30 threshold (strong)**: 3 or more law school contacts have replied at Score 3+.
**Day 30 threshold (weak)**: Fewer than 2 replies at any score. Trigger: re-contact via clinic administrator rather than direct faculty.
**Network multiplier target**: If any 1 law school faculty member forwards to a peer school, that is a network event. Target is 1 cross-school referral by Day 60.

### Constituency 2: Immigration Legal Aid Organizations

**Primary metric**: Litigation toolkit integration. Target is at least 1 confirmed integration into a model brief, amicus framework, or client advisory document within Day 60.
**Adoption signal definition**: Any of — (a) reply explicitly requesting permission to adapt model brief language; (b) amicus filing in any federal case that cites framework vocabulary; (c) training bulletin or internal advisory citing Phase 1 materials; (d) partner report at Day 30 survey confirming operational use.
**Day 7 minimum**: At least 1 immigration legal aid contact has clicked through to the Gist (Bitly detection).
**Day 30 threshold (strong)**: 2 or more organizations have replied with substantive engagement (Score 3+), OR 1 confirmed litigation use.
**Day 30 threshold (weak)**: Zero replies from immigration legal aid contacts. Trigger: re-contact via staff attorney rather than director; shift framing from framework overview to specific model brief offer.
**Urgency note**: Domain 29 (Prosecutorial Weaponization) and Domain 37 are the two highest-value domains for this constituency. Ensure email templates for immigration legal aid lead with those domains, not the full framework overview.

### Constituency 3: Civil Rights Organizations

**Primary metric**: Policy brief adoption. Target is citation of Phase 1 frameworks in at least 1 annual strategy document, policy brief, or public advocacy document within Day 60.
**Adoption signal definition**: Any of — (a) explicit statement of intent to cite in an upcoming publication; (b) request to co-author or contribute to a policy brief; (c) framework vocabulary appearing in any published document from a Tier 1 civil rights organization; (d) speaking or panel invitation attributable to Phase 1 materials.
**Day 7 minimum**: At least 1 civil rights organization contact has clicked through (Bitly detection) or replied.
**Day 30 threshold (strong)**: 3 or more civil rights contacts have engaged at Score 2+, OR 1 confirmed policy document adoption.
**Day 30 threshold (weak)**: Zero replies from civil rights contacts. Trigger: shift outreach to state-level ACLU chapters and racial justice policy offices rather than national directors.

### Constituency 4: Academic Research (Policy Schools and Social Science Departments)

**Primary metric**: Citation velocity. Target is at least 1 SSRN download, working paper citation, or teaching integration announcement within Day 60.
**Adoption signal definition**: Any of — (a) SSRN paper uploaded by a Tier 1 contact that cites framework vocabulary; (b) course syllabus update detectable via web search; (c) public announcement of research extension (grant application, dissertation proposal, working paper) that references Phase 1 frameworks; (d) conference paper citation.
**Day 7 minimum**: Reply from at least 1 policy school contact at any score level.
**Day 30 threshold (strong)**: 2 or more academic contacts have replied with substantive engagement, OR 1 confirmed citation event.
**Day 30 threshold (weak)**: Zero replies from academic contacts. Trigger: shift to department seminar organizers and graduate student organizations rather than senior faculty.
**Note on academic cycle time**: Academic adoption inherently runs 60-90 days for citation and 12-18 months for syllabus integration. The Day 30 threshold for academics should be set lower than for operational constituencies — engagement (reply) is the leading indicator, not adoption.

### Constituency 5: Faith Coalitions

**Primary metric**: Congregational toolkit adoption. Target is at least 1 sermon guide, congregational discussion toolkit, or faith-based policy brief that incorporates Phase 1 frameworks within Day 60.
**Adoption signal definition**: Any of — (a) explicit request for a congregational adaptation of framework materials; (b) publication of a faith-oriented commentary or bulletin citing Phase 1 research; (c) speaker training request mentioning framework vocabulary; (d) Day 30 survey response confirming congregational discussion integration.
**Day 7 minimum**: At least 1 click from a faith coalition contact.
**Day 30 threshold (strong)**: 2 or more faith contacts have engaged, OR 1 confirmed pastoral/congregational use.
**Day 30 threshold (weak)**: Zero engagement from faith coalitions. Trigger: re-frame outreach around specific themes with high faith resonance (Domains 39, 22, 9) rather than the full framework.

### Constituency 6: Labor Unions

**Primary metric**: Member education module adoption. Target is at least 1 union local chapter or member education program incorporating Phase 1 frameworks within Day 60.
**Adoption signal definition**: Any of — (a) request for a simplified member-facing version of any domain; (b) citation in a contract negotiation brief or member advisory; (c) union officer training curriculum update referencing Phase 1 materials; (d) Day 30 survey response confirming training use.
**Day 7 minimum**: At least 1 click from a labor union contact.
**Day 30 threshold (strong)**: 2 or more union contacts have engaged, OR 1 confirmed training integration.
**Day 30 threshold (weak)**: Zero engagement from labor unions. Trigger: shift to state AFL-CIO chapters and union education directors; offer a simplified 2-page member education brief as an entry point.

### Constituency 7: Mutual Aid Networks

**Primary metric**: Protocol adoption. Target is at least 1 mutual aid network governance document or trainer certification program referencing Phase 1 frameworks within Day 60.
**Adoption signal definition**: Any of — (a) explicit statement that framework materials will be incorporated into network governance or training; (b) network newsletter or communication citing Phase 1 materials; (c) trainer certification request mentioning framework vocabulary; (d) Day 30 survey response confirming governance integration.
**Day 7 minimum**: At least 1 click from a mutual aid contact.
**Day 30 threshold (strong)**: 2 or more mutual aid contacts have engaged, OR 1 confirmed governance use.
**Day 30 threshold (weak)**: Zero engagement from mutual aid networks. Trigger: shift to local mutual aid network coordinators rather than national umbrella organizations; offer a community resilience framing rather than a policy framework framing.

---

## 5. Decision Triggers — Three Checkpoints

### Day 7 Checkpoint: Minimum Viable Engagement

**Date**: 7 days after Wave 1 send date.
**Threshold for hold pattern (no action required)**: At least 4 of 7 constituencies show at least 1 engagement signal (Bitly click or email reply). Aggregate Bitly clicks across all Gist links: at least 15 total in 7 days.
**Threshold for early warning**: Fewer than 10 Bitly clicks across all links, and fewer than 2 replies from any constituency. This is not a failure signal — it may be a delivery problem or a timing issue. Run the delivery diagnostic from PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md before concluding engagement is low.
**Threshold for immediate action**: Zero clicks and zero replies with confirmed email delivery. Escalate to contingency protocol (see Section 6.3).

**Decision output at Day 7**: One of three statuses — HOLD (normal trajectory), MONITOR (below threshold but not in failure range), or ESCALATE (confirmed delivery failure or zero engagement requiring contingency activation).

### Day 30 Checkpoint: Strong Engagement Trajectory

**Date**: 30 days after Wave 1 send date.
**Threshold for Phase 2 acceleration (STRONG signal)**: All of — (a) overall reply rate from Tier 1 contacts is at or above 50%; (b) at least 4 of 7 constituencies have met their individual Day 30 strong threshold; (c) at least 3 cross-organizational references have been detected; (d) at least 2 confirmed adoption signals are recorded in the adoption signal registry.

**Threshold for standard Phase 2 launch (MODERATE signal)**: Any of — (a) overall reply rate is 30-49%; (b) at least 3 of 7 constituencies have met their individual Day 30 strong threshold; (c) at least 1 cross-organizational reference; (d) at least 1 confirmed adoption signal.

**Threshold for Phase 1 extension (WEAK signal)**: Any of — (a) overall reply rate is below 20%; (b) fewer than 2 constituencies have met their individual Day 30 strong threshold; (c) zero cross-organizational references; (d) zero confirmed adoption signals.

**Threshold for failure**: Overall reply rate below 10% AND zero adoption signals AND zero cross-organizational references AND zero Gist clicks in Week 3-4 (indicating no ongoing organic engagement after the initial wave). This is the failure signal that requires a full contingency review, not just a Phase 2 delay.

### Day 60 Checkpoint: Movement-Scale Impact

**Date**: 60 days after Wave 1 send date.
**Target**: At least 15 organizations have integrated Phase 1 into operational practice, and at least 100 people have been trained on or exposed to Phase 1 frameworks through organizational use.
**Measurement method**: Partner survey at Day 30 plus follow-up, direct contact log annotations, citation search, web monitoring. This checkpoint uses all measurement channels simultaneously.
**Decision output at Day 60**: Determines whether Phase 2 is launched at full scale (all 7 constituencies at Tier 2), partial scale (4-5 constituencies), or extended (Phase 1 continues with revised strategy).

---

## 6. Contingency Activation

### 6.1 STRONG Outcome: Same-Day Phase 2 Activation

If Day 30 checkpoint meets the STRONG threshold, Phase 2 activation does not wait for the May 25 re-synthesis. Execute within 24 hours of confirming the STRONG signal:

**STRONG + Day 30 pass**: Activate Domains 56 and 39 immediately. Domain 56 (Civil Service Politicization) targets Tier 2 law school contacts and civil service reform organizations — its distribution pipeline is documented in DOMAIN_56_DISTRIBUTION_STRATEGY.md and is ready to execute. Domain 39 (Healthcare as Democratic Infrastructure) has a hard external deadline of June 1 (HHS interim Medicaid rule) and must distribute to healthcare policy contacts in this window regardless of synthesis outcome. The Day 30 STRONG signal means Tier 1 social proof is available to accelerate Tier 2 adoption — use it explicitly in Tier 2 outreach ("this framework has been engaged by [named Tier 1 contacts]").

**STRONG activation checklist (same-day)**:
1. Update CHECKIN.md with STRONG determination and per-constituency breakdown
2. Pull Domain 56 Gist (live at https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f) and verify current
3. Pull Domain 39 distribution contact list from DOMAIN_39_DISTRIBUTION_STRATEGY.md
4. Send Domain 39 distribution emails within 24 hours (June 1 HHS deadline)
5. Begin Tier 2 law school outreach using social proof framing from confirmed Tier 1 replies

### 6.2 MODERATE Outcome: Domain 39 Priority Activation

If Day 30 checkpoint meets the MODERATE threshold, activate Domain 39 immediately due to the June 1 HHS deadline — regardless of whether the full STRONG criteria are met. Healthcare urgency overrides Phase 2 sequencing decisions.

**MODERATE + Day 30 pass**: Domain 39 activates immediately. Domain 56 activates within 7 days. Tier 2 expansion holds until Day 60 checkpoint provides additional signal.

**MODERATE activation checklist**:
1. Update CHECKIN.md with MODERATE determination
2. Send Domain 39 distribution within 24 hours of Day 30 checkpoint
3. Extend Phase 1 monitoring to Day 60 for remaining constituencies
4. Prepare Domain 56 for launch at Day 37-40

### 6.3 Failure Recovery: Revised Distribution Strategy

If no adoption signals are detected by Day 30, do not extend the same Phase 1 outreach to 90 days without changing the approach. An unchanged strategy will produce unchanged results. The failure recovery protocol requires three modifications before Day 90 extension:

**Modification 1 — Stakeholder substitution**: Replace 20-30% of Day 90 contacts with contacts from the next tier down (department chairs rather than deans; clinic directors rather than school deans; state-level chapter directors rather than national directors). The Tier 1 targets are high-prestige but may also be high-volume inbox recipients who deprioritize unsolicited outreach.

**Modification 2 — Framing revision**: Shift from "framework overview" to "specific operational resource." Instead of pitching the 35-domain framework as a whole, pitch the single domain most relevant to each recipient's current work. Law schools in election law: pitch only Domain 37. Immigration legal aid: pitch only Domain 29's model brief language. The full framework is an attachment, not the lead.

**Modification 3 — Channel shift**: If email outreach is not producing replies, shift to conference-based distribution (depositing framework materials in conference proceedings or workshop pre-read packets), publication platforms (submitting domain summaries to Just Security, Lawfare, or democracy-focused law reviews), and network-intermediary approach (finding one strong advocate in each constituency who will distribute internally, rather than attempting direct outreach to all 45 contacts).

---

## 7. Cross-Reference Index

This framework builds on and extends the following existing infrastructure documents. Do not duplicate their content — use them as operational references:

- **PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md**: Bitly setup, Gmail label structure, Discord webhook alerts, Congress.gov monitoring — the technical implementation layer for everything described abstractly in Section 3 above.
- **PHASE_1_DISTRIBUTION_MEASUREMENT_PLAYBOOK.md**: Path-specific KPI tables (Path A, Path A+37, Path B); Tier 2 decision gate framework; contingency adjustments for underperforming sectors.
- **PHASE_2_LAUNCH_DECISION_TRIGGERS.md**: Detailed STRONG/MODERATE/WEAK scenario activation protocols; standing external deadlines (June 1 HHS, August 2 EU AI Act, August 10 Domain 57); Tier 2 expansion sequencing.
- **SYNTHESIS_OUTCOME_PLAYBOOKS.md**: Pre-built same-day execution protocols for each synthesis classification outcome.
- **DISTRIBUTION_GIST_URLS.md**: Canonical Gist URLs for all distributed documents; Bitly back-half mappings.
- **PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md**: The operational dashboard that collects all data described in this framework (companion document).
- **PHASE_1_DECISION_TREES.md**: Checkpoint-specific decision trees for Day 7, Day 30, Day 60 (companion document).
