---
title: "Tier 3 Deployment Sequence: 16-Week Rollout Plan"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Tier 3 Distribution Planning
session: 908
version: 1.0
word_count: ~2,000
depends_on:
  - tier-3-audience-segmentation-and-contact-list.md
  - tier-3-messaging-templates.md
  - TIER2_DISTRIBUTION_PREP.md
  - tier-2-distribution-sequencing.md
---

# Tier 3 Deployment Sequence: 16-Week Rollout Plan

**Clock start**: Week 1 begins upon user approval of Phase 2 Tier 2 distribution and Tier 3 launch decision. The proposed Week 1 date is June 1, 2026.

**Architecture**: Three sequential pilot waves (DV survivors, labor organizers, election workers) with overlapping expansion phases. Each wave has an explicit go/no-go decision gate before scaling. The Tier 3 → Tier 2 upgrade pathway begins in Week 13.

**Parallel relationship**: Tier 2 outreach (digital rights orgs, academic programs, journalist organizations, policy think tanks) should already be underway by Week 1 of this sequence. Tier 3 does not wait for Tier 2 outcomes — it runs in parallel — but Tier 2 endorsements strengthen Tier 3 credibility when they arrive.

---

## Week 1: Kickoff — Phase 2 Tier 2 User Approval + Tier 3 Launch Decision

**Trigger**: User approves Tier 2 distribution and authorizes Tier 3 launch.

**Week 1 actions**:
- Confirm Tier 2 distribution is underway (or begin Tier 2 and Tier 3 simultaneously if not yet launched)
- Send initial outreach to 12 DV coalition targets using Template 1 (tier-3-messaging-templates.md)
  - Priority order: NNEDV Safety Net Project first (June 1), top 5 state coalitions same week, remaining 7 state coalitions by June 5
- Prepare labor segment contact list for Week 5 outreach (verify AFL-CIO Technology Institute contact, Lauren McFerran; confirm current contacts at SEIU, UFW, CWA)
- Prepare election worker contact list for Week 9 outreach (verify EAC, NASED, NASS contacts; identify state election director contacts via nased.org/members)

**Materials status check**: Confirm all materials referenced in templates are accessible at the corpus Gist URL. If any materials have been updated since the Gist was last published, update before sending.

**Go condition for Week 1**: User approval received; NNEDV Safety Net Project email sent by June 1.

---

## Weeks 1–4: DV Survivor Pilot Wave

### Week 1 (June 1): Initial Contact

- Send Template 1 to 12 DV coalition targets (NNEDV + 11 largest state coalitions by population)
- Log all sends in tracking sheet with timestamp, recipient name, and role
- Set follow-up reminders for non-responses at Day 7 and Day 14

**Expected response profile**: NNEDV Safety Net Project is the highest-value target and likely the fastest responder — they actively seek curriculum additions for the Technology Safety Summit program. State coalition Executive Directors have busy inboxes; response rate within 7 days is expected to be 30–40%. Reminder follow-up increases this to 50–60% within 14 days.

### Week 2 (June 8): Cohort Establishment

**Target**: 6–8 state coalitions confirmed in pilot by end of Week 2.

- Follow up with all Week 1 non-responses (concise follow-up: "Following up on the digital safety resource I shared — happy to schedule a 20-minute call if that's more useful than email.")
- For organizations that have responded: schedule onboarding calls (20–30 minutes; present the advocate training materials and legal evidence preservation section)
- Publish Tier 3 FAQ document (see below) to corpus Gist as a new file, available for coalition staff questions
- Begin cohort tracking: for each confirmed pilot organization, capture: organization name, primary contact, role, planned training delivery method, expected reach (number of advocates they'll train)

**Tier 3 FAQ minimum content**:
- What materials are available for advocates vs. survivors?
- How does this interact with existing NNEDV Safety Net curriculum?
- What are the safety planning prerequisites for technology safety work?
- How do we document adoption for grant reporting purposes?
- Is there a Spanish-language version? (Answer: in development)

### Week 3 (June 15): Training Delivery

**Target**: Pilot cohort organizations begin delivering advocate training.

- Conduct live 90-minute onboarding Zoom for pilot cohort (all 6–8 confirmed organizations)
  - Agenda: Threat model overview (30 min) → Advocate training module walkthrough (30 min) → Legal evidence preservation section (20 min) → Q&A (10 min)
  - Record session and make available to non-attendees
- Distribute feedback collection form to all pilot participants (see tier-3-deployment-sequence.md feedback protocol below)
- Track early adoption signals: number of advocates trained, number of safety planning sessions using the materials

### Week 4 (June 22): Pilot Review and Go/No-Go Decision

**DV Wave Go/No-Go Gate**:

| Metric | Target | Source |
|---|---|---|
| State coalitions confirmed in pilot | ≥6 | Tracking sheet |
| Advocates trained in pilot cohort | ≥50 | Cohort self-report |
| Training completion rate | ≥80% | Post-training survey response rate |
| Post-training adoption (advocates using materials in safety planning) | ≥50% of trained advocates | 2-week follow-up survey |
| NNEDV Safety Net Project response | Confirmed interest | Email record |

**If metrics positive**: Scale to broader NNEDV network — send outreach to remaining 44+ state coalitions (not in pilot) week of June 22. Use pilot cohort testimonials and adoption data to strengthen outreach to late adopters.

**If metrics below threshold**: Diagnose before scaling. Common failure modes: materials too complex for advocate delivery without additional simplification, Spanish translation gap blocking adoption in specific coalitions, trust barrier requiring a warmer introduction (NNEDV direct referral rather than cold email). Adjust and re-test with 4-week delay.

---

## Weeks 5–8: Labor Organizing Pilot Wave

### Week 5 (June 22): Initial Contact

- Send Template 2 to 8 labor organization targets (AFL-CIO Technology Institute + SEIU + UFW + CWA + UFCW + USW + Teamsters + AFL-CIO National)
- Priority order: AFL-CIO Technology Institute first (Lauren McFerran; a relationship here activates the entire federation network)
- Log all sends; set follow-up reminders at Day 7 and Day 14

**Expected response profile**: The AFL-CIO Technology Institute is most likely to respond quickly given their active Workers First AI Summit programming. Individual union IT directors have longer response cycles (10–14 days typical). UFW may respond through communications staff rather than organizing directly — follow the thread wherever it leads.

### Week 6 (June 29): Cohort Establishment

**Target**: 4–5 major unions/federations confirmed in pilot by end of Week 6.

- Follow up with Week 5 non-responses
- For confirmed participants: assess their preferred training delivery format (in-person at union hall, webinar, materials for self-delivery by shop stewards, integration into existing AFL-CIO Technology Institute curriculum)
- Role-specific training cohort assignment: confirm which roles each organization wants to train first (organizers, stewards, IT, legal)

**Role-specific training tracks**:
- **Organizer track** (primary): Communications security (Signal setup and discipline), Penlink geofencing awareness, social media exposure reduction. 60-minute session, deliverable by a trained steward.
- **Steward track**: Member coaching module — how to explain surveillance threat without creating panic, 20-minute member meeting delivery, escalation protocol.
- **IT track**: Infrastructure hardening for union communications systems, Signal network architecture for organizing committees, incident documentation. 90-minute technical session.
- **Legal track**: Whistleblower documentation protocols, attorney-client privilege protection for electronic communications, NLRA protections for organizing communications. 45-minute session, co-facilitated with organizing department.

### Week 7 (July 6): Training Delivery

**Target**: Pilot cohort organizations deliver first training sessions.

- Conduct live 90-minute onboarding Zoom for labor pilot cohort
  - Agenda: Penlink/Babel Street threat briefing (30 min) → Role-specific breakouts (30 min) → Q&A and adaptation discussion (30 min)
- Distribute feedback collection form optimized for organizing context:
  - Did this change how your organizing committee is using Signal?
  - Have you adjusted member social media guidance as a result?
  - What's the biggest barrier to implementing these practices in your local?

### Week 8 (July 13): Pilot Review and Go/No-Go Decision

**Labor Wave Go/No-Go Gate**:

| Metric | Target | Source |
|---|---|---|
| Major unions/federations in pilot | ≥4 | Tracking sheet |
| Organizers and stewards trained | ≥200 | Cohort self-report |
| Trainer confidence score (1–5) | ≥4.0 average | Post-training survey |
| Member uptake rate (members who changed Signal/social media practices) | ≥40% of those trained | 2-week follow-up survey |
| AFL-CIO Technology Institute response | Confirmed interest in curriculum integration | Email record |

**If metrics positive**: Contact international union affiliates (SEIU International, CWA International, etc.) and UFW international solidarity programs for expansion. Offer to develop AFL-CIO Technology Institute integration materials.

**If metrics below threshold**: Most likely failure mode is the immigration enforcement threat model being irrelevant to union locals with no immigrant worker concentration. Diagnose and develop sector-specific variants: one for majority-immigrant-worker sectors (agriculture, hospitality, food processing), one for majority-citizen sectors (industrial, tech, media).

---

## Weeks 9–12: Election Worker Pilot Wave

### Week 9 (July 20): Initial Contact

- Send Template 3 to 10 election worker organization targets (EAC + NASED + NASS + CA + TX + NY + FL + D3P + CDT + Votebeat)
- Priority order: EAC first (resource library submission is the lowest-friction entry point), NASED second (peer-to-peer cascade)
- Note: July 20 is within the optimal training window (June–July) before the active election cycle. Do not delay past August 1.

**Expected response profile**: EAC is a federal agency — expect 10–14 day response cycle. NASED and NASS will be faster as peer professional associations. State secretaries of state offices have communications staff who will triage; expect routing to an IT or election security officer. Votebeat and CDT are journalistic/advocacy organizations — faster responses, different engagement type.

### Week 10 (July 27): Cohort Establishment

**Target**: 10–15 state election offices confirmed in pilot by end of Week 10.

- Follow up with non-responses
- For confirmed states: identify the specific training delivery path (state election director trains county officials, or state provides materials for county self-delivery)
- EAC coordination: if EAC responds positively, explore whether the corpus can be added to the EAC cybersecurity resource library before the pilot training begins — resource library listing provides implicit EAC endorsement that helps with state adoption

**Cascade model for state-level training**:
- State election director level: Hardware security and infrastructure hardening (IT-oriented, 2 hours)
- County election official level: Credential management and incident response (90 minutes, delivered by state or self-paced)
- Poll worker level: Simplified USB policy and personal device security (20 minutes, incorporated into pre-election poll worker training)

### Week 11 (August 3): Training Delivery

**Target**: Pilot state election offices begin delivering training to county officials.

- State-level training sessions (state election director + county officials)
- Poll worker module reviewed and ready for incorporation into September–October pre-election poll worker training
- Feedback collection form for election context:
  - Which hardware security measures have been implemented?
  - Has MFA been enabled on election management system access?
  - Have any vendors been asked to improve their security practices as a result?
  - What's the biggest barrier in your jurisdiction?

### Week 12 (August 10): Pilot Review and Go/No-Go Decision

**Election Worker Wave Go/No-Go Gate**:

| Metric | Target | Source |
|---|---|---|
| State election offices in pilot | ≥10 | Tracking sheet |
| Election officials trained (state + county combined) | ≥500 | Cohort self-report |
| Training completion rate | ≥60% | Post-training survey response |
| Infrastructure adoption (MFA enabled, USB policy implemented) | ≥3 states confirm at least 2 measures implemented | Follow-up survey |
| Vendor security improvement requests | ≥3 state offices report requesting vendor improvements | Follow-up survey |
| EAC resource library submission | Submitted (regardless of acceptance status) | Internal record |

**If metrics positive**: Scale to remaining 35–40 state election offices not in pilot. Use pilot state testimonials. Offer to NASED as a conference presentation for their fall meeting.

**If metrics below threshold**: Most likely failure mode is distrust of non-governmental security resources in the election context. Mitigation: obtain explicit endorsement from EAC or NASED before expanding. A NASED president statement or EAC resource library listing resolves the trust barrier for most state election directors.

---

## Weeks 13–16: Tier 3 → Tier 2 Upgrade Path and Expansion

### Week 13 (August 17): Aggregate Pilot Analysis

**Actions**:
- Compile aggregate success metrics across all three waves
- Identify high-confidence cohorts for Tier 2 upgrade outreach (organizations that completed training, implemented measures, and expressed interest in deeper engagement)
- Prepare Tier 3 expansion contact lists for non-pilot organizations in each segment

**High-confidence upgrade indicators** (any two of):
- Training completion rate ≥80%
- Implementation of ≥3 recommended security measures
- Unprompted request for additional materials or deeper engagement
- Organizational leadership expressed interest in ongoing relationship
- Positive follow-up survey score ≥4.0/5.0

### Weeks 14–15 (August 24 – September 6): Upgrade Outreach

**Tier 3 → Tier 2 upgrade outreach** to high-confidence cohorts:
- Offer Tier 2 advanced training to organizations that have completed Tier 3 pilot and shown high adoption
- Tier 2 framing is institutional: advanced forensics, legal case support infrastructure, nation-state threat modeling (see ROI model in tier-3-roi-and-impact-model.md for revenue projections)
- Upgrade conversation opener: "Based on [Organization]'s strong adoption of the Tier 3 materials, we'd like to discuss a more intensive engagement that goes deeper on [legal evidence preservation / undercover infiltration countermeasures / nation-state threat modeling]."

**Tier 3 expansion to non-pilot cohorts** (weeks 14–15, parallel track):
- DV: Outreach to remaining 44+ state coalitions not in pilot, using pilot cohort adoption data and NNEDV Safety Net Project endorsement (if received) as credibility signal
- Labor: Outreach to international union affiliates and non-pilot independent unions (Teamsters independent, NEA, AFT, AFSCME)
- Election: Outreach to remaining 35–40 state election offices not in pilot

### Week 16 (September 13): Tier 3 Consolidation

**Actions**:
- Complete Tier 3 expansion outreach
- First Tier 3 → Tier 2 upgrade meetings scheduled
- Publish Tier 3 impact summary (for use in Tier 2 endorsement requests and future funding conversations):
  - Total organizations engaged
  - Total individuals trained across all sectors
  - Infrastructure measures implemented (for election workers)
  - Adoption rate by sector
- Update WORKLOG.md with Tier 3 completion status and metrics

---

## Success Metrics Summary

### DV Survivor Wave (Weeks 1–4)
| Metric | Target | Notes |
|---|---|---|
| State coalitions in pilot | ≥6 | Go/no-go for national expansion |
| Training completion | ≥80% | Of advocates in pilot cohort |
| Post-training adoption | ≥50% | Advocates using materials in safety planning |
| NNEDV Safety Net endorsement | Confirmed | Single highest-value outcome |

### Labor Organizing Wave (Weeks 5–8)
| Metric | Target | Notes |
|---|---|---|
| Major unions in pilot | ≥4 | Go/no-go for federation expansion |
| Membership reached | ≥70% of pilot cohort | Via steward delivery |
| Practice change documented | ≥40% | Organizing-cell-level adoption |
| AFL-CIO Tech Institute integration | Curriculum interest confirmed | Unlocks federation network |

### Election Worker Wave (Weeks 9–12)
| Metric | Target | Notes |
|---|---|---|
| State election offices in pilot | ≥10 | Go/no-go for national expansion |
| Official training completion | ≥60% | State + county combined |
| Infrastructure measures implemented | ≥2 per pilot state | MFA, USB policy, firmware verification |
| Vendor security improvements | ≥3 states requesting | Leading indicator of systemic change |
| EAC resource library submission | Submitted | Regardless of acceptance status |

### Tier 3 → Tier 2 Upgrade (Weeks 13–16)
| Metric | Target | Notes |
|---|---|---|
| High-confidence upgrade cohorts identified | ≥15% of all Tier 3 participants | Per success indicator criteria |
| Upgrade meetings scheduled | ≥5 organizations | Across all three segments |
| Tier 3 expansion outreach complete | All segments | Remaining non-pilot organizations |

---

## Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| NNEDV Safety Net Project does not respond | Low | High — blocks DV cascade | Warm introduction from a known NNEDV partner (CDT, EFF, or safety researcher in NNEDV network) |
| AFL-CIO Technology Institute response delayed beyond Week 6 | Medium | Medium — delays federation endorsement | Proceed with individual union outreach in parallel; don't wait for federation before contacting SEIU, UFW, CWA |
| Election officials distrust non-government security resources | Medium | High — blocks adoption in security-sensitive audience | EAC resource library submission as credibility mechanism; D3P as non-government trusted peer |
| Penlink geofencing threat deemed too politically charged by union legal | Medium | Medium — limits labor training content | Dual framing: employer surveillance (non-political) is equally valid entry point for labor audience |
| August election cycle begins before Week 12 metrics complete | Low | Low — timing overlap is manageable | Poll worker training module is ready for incorporation regardless of overall pilot metrics |
| Tier 2 distribution outcomes are negative (orgs decline or ignore) | Low | Low — Tier 3 is independent | Tier 3 does not depend on Tier 2 outcomes; NNEDV/AFL-CIO/EAC relationships are independent of Tier 2 contacts |

---

## Sources

- [Nextgov/FCW — CISA election pullback warning, May 2026](https://www.nextgov.com/cybersecurity/2026/05/senator-warns-cisa-election-security-pullback-could-leave-midterms-vulnerable/413378/)
- [Votebeat — CISA trust broken, January 2026](https://www.votebeat.org/2026/01/15/cisa-election-security-trust-broken-trump-chris-krebs-denise-merrill/)
- [AFL-CIO Technology Institute](https://aflciotechinstitute.org/)
- [NNEDV Safety Net Project — Tech Summit 2026](https://nnedv.org/content/safety-nets-tech-summit-2026/)
- [EAC Election Security Resource Library](https://www.eac.gov/election-officials/election-security-preparedness)
- [NASED — 2026 President announcement (Brinson Bell, NC)](https://www.ncsbe.gov/news/press-releases/2025/02/13/brinson-bell-line-become-2026-president-national-elections-association)
- [NASS #TrustedInfo2026](https://www.nass.org/node/2685)
- [Prism Reports — Penlink PLX contract, April 2026](https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/)
