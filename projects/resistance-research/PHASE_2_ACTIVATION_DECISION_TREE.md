---
title: "Phase 2 Activation Decision Tree"
created: "2026-06-01"
purpose: "Response-based routing for Phase 2 (Domains 38, 39, 58) activation, sequencing, and contingency"
trigger_inputs:
  - Domain 39 T+3 (June 4)
  - Domain 39 T+7 (June 8)
  - Domain 39 T+14 (June 15) — PRIMARY GATE
  - Domain 39 T+30 (July 1)
outputs: Phase 2 timing and scope decisions for Domains 38, 40, 58
cross_references:
  - DOMAIN_39_RESPONSE_MONITORING_PLAN.md
  - WAVE_2_EXECUTION_TIMELINE_WITH_TRIGGERS.md
  - DOMAIN_38_40_CONTINGENCY_DECISION_TREE.md
  - DOMAIN_58_RULING_TRIGGER_READINESS.md
status: "activation-ready — all four paths fully specified"
---

# Phase 2 Activation Decision Tree
## Response-Based Routing: Domain 39 Data Drives Domains 38, 40, 58 Sequencing

*This tree is consulted at four checkpoints: T+3 (June 4), T+7 (June 8), T+14 (June 15), and T+30 (July 1). The T+14 assessment is the binding gate — it determines the Phase 2 path that governs June 15 – August 15 execution. Earlier checkpoints provide early-warning signals and minor routing adjustments. Later checkpoints close the loop.*

*All Phase 2 infrastructure (contact lists, Gist procedures, timelines) is production-ready regardless of path. This tree adjusts timing and scope; it does not change content.*

---

## Pre-Tree Checklist (Run June 2, 09:00 UTC)

Before the decision tree is consulted, confirm the following:

- [ ] Domain 39 June 1 Tier A send is confirmed complete (all 5 emails sent, logged in DISTRIBUTION_EXECUTION_LOG.md)
- [ ] No immediate bounce notifications received within 24 hours of send
- [ ] Domain 38 source document confirmed production-ready: `domain-38-ai-regulatory-capture-governance.md`
- [ ] Domain 40 source document confirmed production-ready: `domain-40-surveillance-capitalism-electoral-manipulation.md`
- [ ] Domain 58 Gist creation status confirmed (required before ruling issues): see DOMAIN_58_GIST_URL.md
- [ ] Contact lists confirmed: DOMAIN_38_CONTACT_STRATIFICATION.md, DOMAIN_40_CONTACT_STRATIFICATION.md
- [ ] DOMAIN_39_RESPONSE_MONITORING_PLAN.md is open and tracking has begun

If all items checked: Phase 2 is activated. Begin T+3 monitoring.

---

## Path Overview

Four Phase 2 paths exist, determined by Domain 39 T+14 response data:

| Path | T+14 Criteria | Label | Core posture |
|------|--------------|-------|-------------|
| **STRONG** | 3+ confirmed engagements | Full acceleration | All domains advance at maximum speed |
| **MODERATE** | 2 confirmed engagements | Caution gates active | Proceed with daily monitoring; contingency standing by |
| **WEAK** | 0–1 confirmed engagements | Phase 2 delayed | Tier 2 focus; extended outreach June 15 – July 15 |
| **DELIVERY_PROBLEM** | 1+ unresolved bounces at T+14 | Escalation | Alternative outreach channels; verify contact infrastructure |

---

## Checkpoint 1: T+3 Early Signal
### June 4, 2026

This checkpoint is diagnostic, not decisional. No path changes are triggered at T+3 alone.

**What to measure**: How many of the 5 Tier A contacts have replied within 72 hours?

---

### Branch 1A: T+3 = 0 responses, no bounces

Normal range for cold outreach to policy organizations. No action.

**Log**: "T+3 clean zero — within expected range. Monitoring continues to T+7."

---

### Branch 1B: T+3 = 1 response

Positive early signal. Respond within 24 hours. If the response indicates litigation or coalition interest, note as qualitative flag.

**Log**: "T+3 early engagement: [org name, response type]."

---

### Branch 1C: T+3 = 2–5 responses

Strong early signal. Respond to each contact within 24 hours.

**Qualitative scan**: Does any respondent mention AI governance, election protection, or other orgs they are sharing the document with? If yes, flag for Domain 38/40 warm contact list and log.

**Log**: "T+3 exceptional early engagement: __ responses. Coalition interest noted: [yes/no]."

---

### Branch 1D: T+3 = any bounce

**Action**: Do not wait for T+7. Immediately attempt alternative contact:
- Georgetown CCF: Catherine.Hope@Georgetown.edu
- Brennan Center: brennancenter@nyu.edu
- IRG: dan@responsivegov.org
- BMMA: Re-verify blackmamasmatter.org/contact for current address
- NHeLP: Re-verify healthlaw.org/contact

**Log**: "Bounce received from [org]. Alternative contact attempted [date/method]."

---

## Checkpoint 2: T+7 Signal Assessment
### June 8, 2026

**What to measure**: Cumulative Domain 39 responses as of Day 7.

---

### Branch 2A: T+7 = 0 responses (weak signal)

Zero responses at Day 7 is a meaningful weak signal requiring proactive adjustment.

**Wave 2 adjustment**:
- For Domain 38: Expand Tier A outreach to include 5 Tier B contacts (Data and Society, Upturn, Color of Change, NELP, Center for AI Safety) — add them to the June 15 send batch
- For Domain 40: Move social media / community distribution (Reddit, Twitter) from August to July 1 to build organic awareness before July 15 Tier A send
- Prepare alternative subject lines for Domain 38 Tier A emails — lead with EU August 2 enforcement deadline rather than org-specific research hook

**Do not cancel**: Zero T+7 Domain 39 response does not predict Domain 38 or Domain 40 response rates.

**Log**: "T+7 zero responses. Tier B expansion prepared for Domain 38. D40 social distribution moved to July 1."

---

### Branch 2B: T+7 = 1–2 responses (marginal)

Below the 2+ healthy baseline but not zero.

**Wave 2 adjustment**: None. Proceed with default timeline. Monitor T+14 closely.

**Opportunity**: If any respondent engaged on electoral/health nexus themes, note them as a potential warm reference for Domain 40 July sends.

---

### Branch 2C: T+7 = 3–5 responses (healthy)

Meets or exceeds expected Day 7 baseline.

**Wave 2 adjustment**: None. Default timeline is appropriate.

**Opportunity**: Respond to each engaged contact within 24 hours. Ask if any would be interested in a brief follow-up conversation or would find the companion AI governance framework (Domain 38) relevant to their work.

---

### Branch 2D: T+7 = 5 responses (exceptional / all-response)

All 5 Tier A contacts responded within a week. Strong coalition formation signal.

**Wave 2 acceleration**:
1. Expand Domain 38 Tier B immediately (begin June 8–12 rather than June 21–28)
2. Consider Domain 40 early Gist creation (begin June 8 instead of June 21–30) to enable a possible June 15 simultaneous launch with Domain 38
3. If 2+ respondents indicate interest in connecting to other orgs, facilitate introductions (with their permission)

**Log**: "T+7 full response. Domain 40 Gist creation beginning June 8. Introductions facilitated: [yes/no]."

---

## Checkpoint 3: T+14 Primary Activation Gate
### June 15, 2026, 09:00 UTC

**This is the binding gate.** Assess at 09:00 UTC before any Domain 38 emails go out (Domain 38 first send at 09:30 UTC).

**What to measure**: Total Domain 39 weighted response score as of June 15.

---

## PATH: STRONG
### T+14 criteria: 3+ confirmed engagements (weighted score 3.0+)

**Definition of confirmed engagement**: A response coded SE, BC, CIT, or FWD per DOMAIN_39_RESPONSE_MONITORING_PLAN.md response schema. A use-case signal (citation, litigation mention, publication reference) elevates any path to STRONG regardless of raw count.

**Phase 2 activation**: FULL ACCELERATION

**Domain 38**:
- Tier A send proceeds June 15–20 as planned (default timeline)
- Tier B send accelerates: begin June 21 (not delayed to June 28)
- In Domain 38 Tier A emails, reference Domain 39 engagement: "Healthcare organizations engaged with this democratic infrastructure framework in the first two weeks — here is the companion AI governance analysis that extends the same frame"

**Domain 40**:
- Tier A send remains July 15 default
- If any Domain 39 respondents mentioned election protection or electoral surveillance themes: flag as warm contacts and reference in Domain 40 emails
- Gist creation June 21–30 as planned

**Domain 58**:
- Independent of Domain 39 results; continues on ruling-triggered timeline (see DOMAIN_58_RULING_TRIGGER_READINESS.md)
- No acceleration or delay based on Domain 39 STRONG outcome — Domain 58 is on its own ruling-dependent clock

**Monitoring**:
- Switch from daily email checks to every-other-day checks (response urgency has passed)
- Continue citation search protocol at T+30

**Log**: "T+14 STRONG — __ responses, weighted score __. Phase 2 full acceleration confirmed. Domain 38 Tier B moved to June 21."

---

## PATH: MODERATE
### T+14 criteria: 2 confirmed engagements (weighted score 2.0–2.9)

**Phase 2 activation**: PROCEED WITH CAUTION GATES

**Domain 38**:
- Tier A send proceeds June 15–20 as planned (no change)
- Tier B send proceeds June 21–28 as default
- Daily response monitoring for Domain 38 continues through its T+14 gate (June 29)
- Caution gate: If Domain 38 T+14 also shows 2 or fewer responses, activate Branch 3A consolidation

**Domain 40**:
- Tier A send July 15 default — no change
- Contingency Tier 2 standing by: if Domain 38 Day 14 is also MODERATE or WEAK, move Domain 40 social distribution to July 1

**Domain 58**:
- No change; independent timeline

**Contingency standing by**:
- Maintain Tier 2 Domain 39 contact list (CBPP, NDRN, DRA, SisterSong, etc.) in ready state
- If T+30 Domain 39 score drops below 2.0, activate Tier 2 sends retroactively (July 1–10)

**Monitoring**: Daily checks continue at T+14 through T+30.

**Log**: "T+14 MODERATE — __ responses, weighted score __. Default timeline proceeds. Caution gates active. Contingency Tier 2 standing by."

---

## PATH: WEAK
### T+14 criteria: 0–1 confirmed engagements (weighted score 0–1.9)

**Phase 2 activation**: DELAYED — TIER 2 FOCUS

**This does not cancel Phase 2.** It reroutes it.

**Domain 39 (Tier 2 activation)**:
- Begin Tier 2 outreach June 15–July 15 to expand contact base:
  - CBPP, NDRN, Disability Rights Advocates, AMCHP, SisterSong, NACHC, Commonwealth Fund
  - These 7 organizations have direct relevance to Domain 39's five pathways
- Before sending Tier 2 emails, revise subject lines: test an alternative hook (e.g., lead with the APSR rural hospital-turnout finding rather than HHS rule framing)

**Domain 38**:
- Tier A send proceeds June 15–20 as planned (different audience — do not delay Domain 38 based on Domain 39 weak outcome)
- Add social distribution (Reddit, Twitter) for Domain 38 on June 15–16 simultaneously with Tier A email send — community awareness compensates for reduced email engagement signal
- Revise subject lines: lead with EU August 2 enforcement deadline hook

**Domain 40**:
- Delay Tier A send from July 15 to August 1 (allows more time for warm contacts to develop via Domain 38 engagement and EU enforcement news cycle to build)
- Begin Tier D social distribution August 2 to coincide with EU AI Act enforcement news

**Domain 58**:
- No change; independent timeline — Domain 58 activation is ruling-triggered, not response-rate-triggered

**Monitoring**: Daily checks through T+30; escalation review at July 1.

**Log**: "T+14 WEAK — __ responses, weighted score __. Tier 2 outreach begins June 15. Domain 40 Tier A delayed to August 1. Domain 38 social distribution added June 15."

---

## PATH: DELIVERY_PROBLEM
### T+14 criteria: 1+ unresolved bounce, or evidence of non-delivery (no opens confirmed after 14 days and 0 responses)

**Phase 2 activation**: ESCALATION

**Immediate actions**:

1. **Contact via alternative channels** (execute within 24 hours of identifying the problem):
   - Georgetown CCF: Call 202.784.3138 (Catherine Hope) or use Georgetown faculty directory to find staff email
   - NHeLP: Call (202) 289-7661 or (310) 204-6010
   - BMMA: Check blackmamasmatter.org for any updated contact form or Instagram/social DM
   - Brennan Center: Use brennancenter@nyu.edu as fallback; check brennancenter.org for staff directory
   - IRG: Call or use dan@responsivegov.org (media contact)

2. **LinkedIn outreach** (for orgs with no phone resolution within 48 hours):
   - Identify staff at each org working on relevant issue areas
   - Connect and send brief LinkedIn message with Gist URL and one-sentence hook

3. **Alternative email discovery** (if primary email undeliverable):
   - Georgetown CCF: Try Joan Alker (Executive Director) directly — check Georgetown faculty pages
   - IRG: info@responsivegov.org confirmed working; if bouncing, try dan@responsivegov.org
   - BMMA: Try connect@blackmamasmatter.org as variant

**After delivery problem resolved**: Route to MODERATE or STRONG path based on actual response rate once delivery confirmed.

**Log**: "T+14 DELIVERY_PROBLEM — bounce from [org]. Alternative contact attempted [date/method/outcome]."

---

## Checkpoint 4: T+30 Final Assessment
### July 1, 2026

**What to measure**: Final Domain 39 response tally and citation check.

---

### Branch 4A: T+30 weighted score < 2.0 (minimum viable not achieved)

**Assessment**: Domain 39 cold email outreach to this specific Tier A contact set did not achieve minimum viable outcome.

**Actions**:
- Activate Tier 2 Domain 39 sends (July 1–10) if not already executed
- Conduct citation search (see DOMAIN_39_RESPONSE_MONITORING_PLAN.md T+30 protocol) — even without response, orgs may have referenced the document
- If Domain 38 T+14 (June 29) is also < 2 responses: activate dual weak-outcome protocol from DOMAIN_38_40_CONTINGENCY_DECISION_TREE.md
  - Consolidate messaging into a one-page synthesis of all domain findings
  - Shift from email to social/community channels as primary distribution vehicle
  - Delay Domain 40 Tier A send to August 15 (after EU enforcement news cycle)

**Do not cancel Domain 40**: The November 3 midterm deadline is absolute. Channel failure does not eliminate the need for distribution.

---

### Branch 4B: T+30 weighted score 2.0–3.9 (minimum viable achieved)

Domain 39 met its minimum viable outcome. Proceed.

**Actions**:
- Reference Domain 39 engagement in Domain 40 July 15 Tier A emails: "Organizations working on Medicaid and voter registration connected — the companion surveillance analysis documents why their convergence matters for November 3"
- If any Domain 39 respondents engaged with electoral themes: name them (with permission) as warm context in Domain 40 outreach

---

### Branch 4C: T+30 weighted score 4.0–5.9 (overperformance)

Domain 39 exceeded targets. Organic distribution is likely underway.

**Actions**:
- Activate Domain 38 Tier B secondary list (July 1–10)
- Consider simultaneous Domain 38 + Domain 40 Tier A launches if Domain 40 Gist is ready
- Prepare a brief social proof note (without naming specific orgs): "Several national organizations engaged with this framework in June — here is the companion AI governance analysis"

---

### Branch 4D: T+30 weighted score 6.0+ (exceptional / coalition formation)

**Actions**:
- Facilitate introductions between responding organizations with overlapping interests
- Consider a coordination call invitation: "Would a brief call be useful to coordinate advocacy strategy before November 3?"
- Move Domain 38 and Domain 40 Tier A to simultaneous July 1 launch
- Approach Tier 0 contacts (OpenSecrets, NASS, Senate Rules Committee staff) via warm introduction from Tier A respondents

---

## Special Trigger: Litigation Interest Signal

**Trigger**: Any respondent (at any checkpoint) signals they are interested in using Domain 39 for APA litigation, NVRA Section 7 enforcement, or congressional testimony.

**This trigger supersedes normal checkpoint timing.**

**Immediate actions**:
1. Prioritize a direct briefing call with that organization (offer within 48 hours of their signal)
2. Accelerate all Tier 2 sends to capture momentum (begin within 3 days)
3. In Domain 38 and Domain 40 Tier A emails, reference: "Organizations working on healthcare-access litigation are integrating this framework — the companion analysis documents the AI governance dimensions of the same threats to democratic infrastructure"
4. Flag organization for Domain 58 distribution as well (litigation organizations working on healthcare and voting rights are natural Domain 58 recipients)

---

## Quick Reference: All Branches

| Gate | Weighted Score | Branch | Phase 2 Adjustment |
|------|--------------|--------|-------------------|
| T+3 | Any bounce | 1D | Alternative contact immediately |
| T+3 | 0, no bounces | 1A | No action; monitor |
| T+3 | 1 | 1B | Respond; no timeline change |
| T+3 | 2–5 | 1C | Respond; note warm contacts |
| T+7 | 0 | 2A | Tier B expand; alternative subject lines; D40 social to July 1 |
| T+7 | 1–2 | 2B | No change; monitor T+14 |
| T+7 | 3–5 | 2C | Default; warm follow-ups |
| T+7 | 5 (full) | 2D | D40 Gist creation starts; introductions |
| **T+14** | **<2** | **WEAK** | **Tier 2 focus; D40 delayed to Aug 1** |
| **T+14** | **2–2.9** | **MODERATE** | **Default + caution gates** |
| **T+14** | **3+** | **STRONG** | **Full acceleration** |
| **T+14** | **bounce unresolved** | **DELIVERY_PROBLEM** | **Phone/LinkedIn escalation** |
| T+30 | <2 | 4A | Consolidate; dual weak if D38 also weak |
| T+30 | 2–3.9 | 4B | Default; warm references for D40 |
| T+30 | 4–5.9 | 4C | D38 Tier B expand; D40 acceleration option |
| T+30 | 6+ | 4D | Coalition facilitation; Tier 0 contacts |
| Any | Litigation signal | Special | Briefing call in 48h; accelerate all Tier 2 |

---

*Created June 1, 2026. Companion files: DOMAIN_39_RESPONSE_MONITORING_PLAN.md, WAVE_2_EXECUTION_TIMELINE_WITH_TRIGGERS.md, DOMAIN_38_40_CONTINGENCY_DECISION_TREE.md (predecessor), DOMAIN_58_RULING_TRIGGER_READINESS.md.*
