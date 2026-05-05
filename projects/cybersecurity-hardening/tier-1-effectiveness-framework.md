---
title: "Tier 1 Effectiveness Measurement Framework"
project: cybersecurity-hardening
created: 2026-05-05
status: production-ready
depends-on:
  - tier-1-success-metrics-framework.md
  - tier-1-feedback-collection-protocol.md
  - tier-1-measurement-dashboard-spec.md
  - post-distribution-impact-tracker.md
  - projects/resistance-research/post-distribution-adoption-framework.md
---

# Tier 1 Effectiveness Measurement Framework

**Lead finding**: The most important early signal is not how many organizations acknowledged receipt — it is whether the corpus generated a question. A question means someone read past the subject line and encountered something they needed to act on. An acknowledgment without a question is Stage 0. A question is Stage 1. The framework lives or dies at the boundary between those two.

---

## 1. What "Success" Means for This Distribution

Success is not uniform across the three Tier 1 sectors. The corpus serves different functions for immigration legal aid organizations (1A), community-based organizations (1B), and mutual aid networks (1C). A single adoption rate threshold would misread the signal.

### Sector-Specific Success Definitions

**Tier 1A: Immigration Legal Aid Organizations (NILC, CLINIC, RAICES, ILRC, NLG)**

Success for legal aid organizations is integration into practitioner workflow, not awareness. These organizations receive dozens of resources per month. Awareness without behavior change means nothing.

The key behaviors that indicate real adoption for 1A:
- An attorney adds Part 0 (data broker opt-outs) to the client intake checklist
- The corpus appears in an organization's published practitioner resource toolkit or intranet
- A staff member references the ELITE address confidence scoring mechanism by name in a training or brief
- An attorney in California walks a client through the DROP platform using the AB 60 pathway documented in the implementation guide

Timeline calibration: Legal aid organizations have long internal review cycles. A decision by NILC to add the corpus to their practitioner resources requires signoff from program directors and potentially general counsel. Expect 6–12 weeks from receipt to any observable institutional action. A 30-day reply rate of 20% with Stage 1 quality is success for Tier 1A; do not expect Stage 3 adoption signals before Day 60.

**Tier 1B: Community-Based Organizations (CASA, Make the Road, United We Dream, Centro CDM)**

Success for community organizations is distribution depth — how many members or clients actually receive and attempt Part 0. These organizations have community education infrastructure (Signal groups, newsletters, in-person workshops) that the corpus is designed to flow through. The failure mode is the corpus being acknowledged by communications staff and never reaching programs staff who run direct-service education.

The key behaviors that indicate real adoption for 1B:
- The corpus (or an excerpt, or a reference to it) appears in an organization's member newsletter or Signal group
- A programs coordinator schedules a community workshop around Part 0
- The Gist URL appears in a context not directly traceable to the initial outreach (organic amplification)
- An organization requests a Spanish-language version of Part 0 or the Tier 1 checklist

Timeline calibration: Community organizations move faster than legal organizations for distribution, but slower for institutional behavior change. A newsletter mention can happen within two weeks. A community workshop takes 4–8 weeks to organize. Expect first observable distribution signals from 1B within weeks 2–4.

**Tier 1C: Mutual Aid Networks (National Bail Fund Network, Community Justice Exchange)**

Success for mutual aid networks is speed of peer propagation. Mutual aid cultures have strong horizontal sharing norms — if one node finds the corpus credible and useful, it spreads without central coordination. The failure mode is the corpus not reaching the trust nodes (the 2–3 people in a network who others treat as security authorities).

The key behaviors that indicate real adoption for 1C:
- The Gist URL appears in a Signal group or Telegram channel not directly seeded by the sender
- A mutual aid organizer references the threat model in explaining ICE risk to network members
- A Bail Fund staff member begins the Part 0 opt-out process with network participants as a workshop

Timeline calibration: Mutual aid networks have the fastest propagation speed but the shortest institutional memory. Signal from this sector comes fast (days 3–14) or not at all. If mutual aid contacts do not engage in the first two weeks, the corpus did not penetrate the trust layer.

---

## 2. The Metric Hierarchy

Not all metrics are equal. The framework ranks metrics in three tiers by consequence, and measurement should prioritize accordingly.

### Tier 1 Metrics: Practice Change (Months 2–6)

These are the highest-consequence metrics. They require active follow-up to observe.

| Metric | Definition | Measurement Method | Target Threshold |
|--------|-----------|-------------------|-----------------|
| Protocol adoption rate | Organizations that modify a practice (intake checklist, client communication, staff training) citing the corpus | 90-day follow-up; case study interview | ≥2 of 12 named orgs by Day 90 |
| DROP platform implementation | California-based attorneys or community workers who walk clients through the AB 60 → DELETE Act pathway | 90-day follow-up, Q1 ("Has your org used any part of the guide?") | ≥1 confirmed case by Day 90 |
| Part 0 adoption (data broker opt-outs) | Individuals guided through data broker opt-outs by a Tier 1 organization | Self-report at follow-up; client numbers given if org shares them | ≥10 individuals by Day 90 |
| Corpus integration into standing resources | Corpus added to an org's practitioner toolkit, intranet, or resource page | Web search; direct confirmation | ≥1 organization by Day 60 |

### Tier 2 Metrics: Engagement Signals (Days 14–60)

These metrics are meaningful because they predict eventual adoption. They do not measure impact on their own.

| Metric | Definition | Target Threshold |
|--------|-----------|-----------------|
| Stage 1+ response rate (among replies) | Replies that show evidence of reading beyond the subject line — specific questions, section references, routing to correct internal contact | ≥50% of all replies |
| Referral factor | New warm contacts generated by Tier 1 contacts forwarding the corpus, divided by initial sends | ≥1.5 by Day 45 (18 total relationships from 12 sends) |
| Bitly click trajectory | Incremental clicks beyond initial open rate, indicating internal forwarding | ≥10 incremental clicks per week in weeks 2–4 |
| Corpus section identified by contact | Contact specifies which section is most relevant (Part 0, threat model, implementation guide) | ≥60% of Stage 1+ replies identify a specific section |

### Tier 3 Metrics: Awareness Signals (Days 1–30)

These are immediately measurable but insufficient on their own. They confirm the corpus reached human beings, not more.

| Metric | Definition | Target Threshold |
|--------|-----------|-----------------|
| Send completion rate | % of 12 named organizations contacted within 7 days of launch | 100% within Day 7 |
| Acknowledgment rate | % of sends receiving any reply within 14 days | ≥25% (3 of 12) |
| Email deliverability | Zero bounces; Bitly shows initial click activity | 0 hard bounces |
| First reply latency | Calendar days from first send to first reply | ≤7 days |

---

## 3. Early Adopter Signals

Early adopter behavior in the first 30 days is the strongest available predictor of eventual wide adoption. The resistance-research post-distribution adoption framework identifies three signals as especially predictive of Phase 2 readiness. Translated to this corpus:

**Signal 1: Vocabulary Migration (Days 1–30)**

Does any public output from a Tier 1 contact — a tweet thread, a newsletter, a social post — use terminology that originated in the corpus? Specific corpus-origin terms to monitor:

- "address confidence score" (the ELITE scoring mechanism)
- "DELETE Act DROP platform" (the California opt-out pathway)
- "data broker opt-out" paired with an immigration context (generic term, but specific context)
- "Tier 1 checklist" or "Part 0" used in a security context

Vocabulary migration in weeks 1–4 indicates the framework has been internalized as an analytical lens, not merely filed as a reference. This is the strongest 30-day predictor of eventual institutional integration.

**Signal 2: Unprompted Secondary Distribution (Days 7–21)**

Does a Tier 1 contact share the corpus without being prompted? Signs:
- A referral from someone who was not in the initial send list, citing a Tier 1 organization as the source
- A Gist view spike that correlates with no action from the sender (meaning someone else distributed the link)
- A reply from a Tier 1 contact that says "I've shared this with [colleague/partner org]" before being asked to

Unprompted forwarding is the single strongest predictor of eventual wide adoption. In Rogers' diffusion model, the transition from innovator to early adopter happens through trusted peer referral. If a Tier 1 contact is actively passing the corpus to their network without prompting, the S-curve has started.

**Signal 3: Domain-Specific Requests (Days 7–30)**

Does any contact ask for more information on a specific section? Common high-signal request forms:
- "Can you tell me more about the DROP platform pathway for clients without ID?"
- "Does this cover X scenario?" (where X is a real client situation)
- "Is there a version of Part 0 we could print for clients without internet access?"

A request for elaboration means the corpus is being tested against real operational need, not evaluated abstractly. It is the clearest possible Stage 1 signal.

---

## 4. Timeline Expectations by Phase

### Days 0–30: Access and Readiness

**What to measure**: Whether the corpus reached the right people. The primary failure mode in this phase is not low engagement — it is the corpus being routed to communications staff rather than program staff. Communications staff acknowledge and file; program staff ask questions.

**Expected events**:
- Days 1–3: First Bitly clicks (immediate after send)
- Days 3–7: First replies from mutual aid networks (Tier 1C) and fast-moving community orgs (Tier 1B)
- Days 7–14: First replies from legal aid organizations (Tier 1A)
- Days 14–21: Follow-up wave to non-responders; first referral contacts generated
- Days 21–30: 30-day assessment; send Day 30 follow-up email

**Success threshold for this phase**: ≥3 of 12 organizations have replied at Stage 1 or above. Zero replies by Day 10 is a deliverability emergency — check spam, verify contacts, resend with subject line variant.

**What does not belong in this phase**: Expecting protocol changes, curriculum integration, or institutional policy adoption. These require internal review cycles that cannot complete in 30 days. Any organization that shows Stage 3+ signals in the first 30 days is unusual — log it and investigate why (it likely means the corpus arrived at an organization already primed to act).

### Days 30–90: Vocabulary Adoption

**What to measure**: Whether the corpus is shaping how organizations talk and think about the threat, even before formal institutional adoption.

**Expected events**:
- Weeks 5–8: First observable use of corpus language in organizational communications (newsletters, social posts, training materials)
- Weeks 6–10: Organizations that showed Stage 1 engagement in Phase 1 begin internal circulation (Stage 2)
- Day 60: Mid-cycle assessment; compare sector engagement rates; identify organizations at risk of stalling at Stage 1
- Days 84–90: 90-day follow-up sent; structured feedback collected

**Success threshold for this phase**: ≥1 documented vocabulary migration event AND ≥2 organizations at Stage 2 or above by Day 90.

**The vocabulary adoption signal matters specifically** because it is the clearest leading indicator of eventual institutional integration at a 6-month horizon. The resistance-research adoption framework shows that vocabulary migration at 30–90 days predicts institutional integration at 6–12 months with high reliability. If vocabulary migration is absent at 90 days, formal integration at 6 months is unlikely regardless of reply rate.

### Days 90–180: Practice Changes

**What to measure**: Whether organizations have changed what they actually do — intake checklists, communication protocols, client education programs.

**Expected events**:
- Months 3–4: Organizations that showed Stage 2 signals become Stage 3 (partial implementation). Watch for: intake protocol updates, Part 0 sessions scheduled for clients, corpus added to practitioner resource pages
- Month 4–5: First case study eligible organizations emerge (Stage 3+). Case study interview window opens
- Month 6: 6-month reassessment; Phase 2 (Tier 2 distribution) decision review

**Success threshold for this phase**: ≥2 of 12 organizations demonstrating Stage 3 or above (a changed practice, not just awareness) by Day 180.

**The California DROP platform signal is the single highest-confidence indicator** that the corpus reached undocumented individuals. If any Tier 1 legal organization reports walking clients through the AB 60 → DELETE Act pathway, that is a direct chain from corpus to reduced ELITE targeting risk for a specific person. This is the most consequential adoption signal available.

---

## 5. Feedback Triage

Not all feedback requires the same response. The triage framework below distinguishes between three conditions:

### Condition A: Minor Tune-Up

**Definition**: Feedback identifies gaps or improvements that do not invalidate the corpus's core utility.

**Signal patterns**:
- "We needed a Spanish-language version of Part 0" — format gap, not content failure
- "The implementation guide assumes laptop access; most clients use phones only" — accessibility gap
- "The Gist format is hard to share internally; a PDF would help" — distribution format gap
- "The DROP platform instructions needed one additional step" — procedural clarification

**Response**: Address before Phase 2 distribution. These are solvable within 1–2 weeks. A Spanish-language Part 0 and a mobile-optimized single-page handout are the two most likely required additions based on population characteristics.

**Does not delay Tier 2 launch**: These are improvements, not corrections. Fix them; document them; distribute Tier 2 with the improved materials. Note the improvements in the Tier 2 outreach as evidence of active iteration.

### Condition B: Framework Isn't Landing

**Definition**: Feedback indicates the corpus is not reaching or activating the intended audience.

**Signal patterns**:
- Zero Stage 1+ replies after 30 days across all 12 named contacts
- 30-day reply rate below 15% (fewer than 2 of 12 contacts reply)
- Replies are uniformly Stage 0 routing responses with no specific content engagement
- Referral factor below 1.0 at Day 45 (no secondary distribution happening)
- Vocabulary migration absent entirely at Day 60

**Diagnostic questions before assuming framework failure**:
1. Did the corpus reach program staff or only communications staff? (Wrong routing, not wrong framework)
2. Did the subject line land in spam? (Deliverability failure, not content failure)
3. Is there a concurrent crisis (major enforcement action, organizational leadership change) absorbing staff capacity? (Timing failure, not framework failure)

**Response**: Before concluding framework failure, check the diagnostic questions. If routing was the problem, re-send to corrected contacts. If the subject line was the problem, test a variant. If the crisis timing was the problem, note it and re-engage after 30 days.

If the framework isn't landing after diagnostics are addressed, the most likely explanations are:
- The corpus is too long for the first-touch ask (organizations route long documents to "read later" indefinitely)
- The corpus leads with the threat model when the audience needs to lead with the action (Part 0 should precede the threat model for Tier 1B and 1C audiences)
- The Gist URL is being blocked by organizational email filters (produce a PDF alternative)

**Does delay Tier 2 launch**: If fewer than 2 of 12 organizations show Stage 1+ engagement at Day 90 despite diagnostic interventions, hold Tier 2 launch until at least 3 Stage 1+ signals are in hand. Tier 2 outreach to digital rights organizations and journalists will invoke Tier 1 social proof — that proof needs to exist before it can be invoked.

### Condition C: Overwhelming Demand

**Definition**: Adoption signals emerge faster and at greater scale than anticipated.

**Signal patterns**:
- Unsolicited referrals from organizations not in the initial contact list, citing a Tier 1 organization as the source
- CLINIC (400+ affiliated programs) reports forwarding to its affiliate network
- Gist view trajectory shows exponential growth (day-over-day doubling for multiple consecutive days)
- Multiple Stage 3+ organizations emerge before Day 60
- Media inquiry from a journalist who found the corpus through a Tier 1 referral

**Response**: This is a positive anomaly, not a problem — but it requires immediate attention. If demand is overwhelming:

1. Publish a concise one-page summary and standalone Part 0 document immediately. Organizations that are distributing broadly need a shorter entry point to share at scale.
2. Document the adoption signals that are safe to name (with organizational permission) before Tier 2 launch. This is powerful social proof.
3. Accelerate the Tier 2 timeline. If Tier 1 social proof is already substantial, Tier 2 outreach can launch early with credible evidence of uptake.
4. Consider whether a Spanish-language Part 0 needs to move from "optional enhancement" to "required before wider distribution."

---

## 6. Go/No-Go Decision Tree for Phase 2

The following decision tree synthesizes the 90-day assessment into an explicit Phase 2 launch decision. Assess at Day 90.

```
PHASE 2 (TIER 2 DISTRIBUTION) GO/NO-GO ASSESSMENT
Assessment Date: [Day 90 from first Tier 1 send]

GATE 1 — BASIC DISTRIBUTION CONFIRMATION
Did at least 10 of 12 named Tier 1 organizations receive the corpus?
  YES → proceed to Gate 2
  NO → complete remaining sends before assessing; delay Gate 2 by [N] weeks

GATE 2 — ENGAGEMENT QUALITY
Of the organizations that replied, are at least 50% at Stage 1 or above?
  YES → proceed to Gate 3
  NO (but ≥25% replied) → diagnose routing failure; try corrected contacts
     → If corrected contacts still produce Stage 0 majority at Day 105: hold Phase 2
  NO (below 15% replied) → deliverability or framework failure; run diagnostics (Section 5, Condition B)
     → Resolve before launching Phase 2

GATE 3 — ADOPTION SIGNAL
Has at least 1 of the following occurred by Day 90?
  [ ] An organization has added the corpus to a practitioner resource page or intranet
  [ ] An organization has referenced the corpus in a client-facing training or workshop
  [ ] An attorney or community worker has guided at least 1 client through Part 0
  [ ] The corpus has been distributed by a Tier 1 contact to an affiliated network without prompting
  [ ] A referral contact (generated via Question 3) has engaged substantively

  1 or more boxes checked → proceed to Gate 4
  0 boxes checked → Hold Phase 2 until Gate 3 criterion is met OR Day 120, whichever comes first
                  → At Day 120 with no Gate 3 signal: revise corpus format (see Section 5, Condition B)

GATE 4 — FEEDBACK INTEGRATION
Have the following questions been answered by at least 3 Tier 1 contacts?
  [ ] Which section was most relevant? (Section 2, Q2)
  [ ] What barriers prevented or delayed implementation? (Day 90 follow-up, Q3)
  [ ] Is there anyone else who should have this? (Day 30 follow-up, Q3)

  All three answered by ≥3 contacts → proceed to Phase 2 launch decision
  One or more unanswered → send targeted follow-up to highest-Stage contacts before proceeding

PHASE 2 LAUNCH DECISION

  All 4 gates pass → LAUNCH (proceed with Tier 2 sends)

  Gates 1, 2, 4 pass; Gate 3 at zero → CONDITIONAL HOLD
    Wait for first Gate 3 signal, maximum 30 additional days
    If no Gate 3 signal by Day 120: REVISE and re-engage Tier 1 before launching Tier 2

  Gate 2 fails (engagement quality below threshold) → HOLD
    Diagnose routing vs. content vs. deliverability failure
    Attempt corrected Tier 1 contacts
    Re-assess at Day 105

  Gate 2 fails and feedback shows consistent barrier pattern → REVISE FRAMEWORK
    Produce format variants (PDF, standalone Part 0, Spanish-language Part 0)
    Re-engage revised materials with 3 highest-potential Tier 1 contacts
    Phase 2 launch delayed by minimum 45 days from revision completion

  Condition C (overwhelming demand) detected → ACCELERATE
    Confirm organizational permission to cite adoption signals
    Produce standalone Part 0 and one-page summary
    Launch Phase 2 immediately with social proof framing
```

### What to Tell Tier 2 Contacts About Tier 1 Results

The framing for Tier 2 outreach depends on which gate result you achieved:

**All gates pass**: "This corpus has been shared with immigration legal aid organizations and community-based organizations serving undocumented clients. [Specific signal, e.g., 'CLINIC has distributed it to affiliated programs'] confirms the threat model is accurate and the countermeasures are actionable for the at-risk population."

**Conditional hold resolved**: "Tier 1 legal aid organizations have begun incorporating Part 0 into client intake. That adoption confirms the corpus addresses a real operational gap." (No need to disclose the delayed Gate 3 signal — only the resolved outcome matters.)

**Condition C (overwhelming demand)**: Lead with the specific social proof. "Within [N] weeks of distribution to immigration legal aid organizations, the corpus was requested by [N] affiliated programs not in the original distribution list." This is the strongest possible opening for Tier 2 outreach to digital rights organizations and academics.

---

## 7. Sector-Specific Success Definitions for Phase 2 Readiness

These thresholds are the minimum conditions for describing each Tier 2 sector engagement as representing a success at the Tier 1 stage.

**For digital rights organizations (EFF, CDT, Access Now)**: The corpus needs to demonstrate it is sourced well enough for them to cite. The Tier 1 signal that earns this credibility is: at least one legal organization has used the threat model's documentation in a client context (even informally). Legal organizations are rigorous about sourcing. If ILRC or NILC staff are using the ELITE documentation, the sourcing standard is effectively validated for Tier 2 audiences.

**For academic cybersecurity programs**: The corpus needs to demonstrate field application, not just theoretical interest. The Tier 1 signal that earns this credibility is: at least one community organization has reported using Part 0 with non-expert clients, and the instructions worked. This is usability evidence — it demonstrates the corpus is calibrated to a real human population, not an idealized threat model subject.

**For security researcher communities**: The corpus needs to demonstrate openness to technical critique. Tier 1 adoption signals do not directly address this need. What earns credibility with security researchers is the feedback collection process itself — specifically, surfacing genuine implementation questions and gaps from Tier 1 contacts, then incorporating them. A corpus that has been actively tested against operational conditions is more credible to researchers than an untested guide, regardless of adoption rate.

**For journalist organizations (FPF, IRE, RCFP)**: The corpus needs to demonstrate that it addresses a real source protection gap, not a hypothetical one. The Tier 1 signal that earns this credibility is: at least one organization working with undocumented people has confirmed the threat model accurately describes the risks their clients face. Legal aid staff are trained to be precise about risk — if they confirm the ELITE documentation is accurate, that is journalist-grade corroboration.

---

## 8. Failure Mode Taxonomy

The following failure modes are distinct and require different responses. Misdiagnosing one as another is the most common cause of unnecessary framework revision.

| Failure Mode | Symptoms | Root Cause | Response |
|---|---|---|---|
| Routing failure | Replies arrive but are uniformly Stage 0 (generic acknowledgments); no content-specific questions | Corpus reached communications staff, not program staff | Research correct program-level contact; re-send with "please route to [program area]" note |
| Deliverability failure | Zero replies, zero Bitly clicks, after 14 days | Email blocked by spam filter, wrong address, or organizational chaos | Test alternate email address; try Signal for Tier 1B and 1C contacts; verify contact info |
| Format mismatch | Positive intent expressed, but "we'll look at it when we have time" language | Gist URL is not a format that fits organizational resource-sharing infrastructure | Produce PDF; create standalone Part 0 as printable document; re-send in adapted format |
| Audience mismatch | Active engagement, but from unexpected sectors; target sectors are unresponsive | The corpus's technical depth fits security-aware organizations, not high-volume direct-service organizations | Lead with Part 0 only for Tier 1B and 1C; reserve full corpus for Tier 1A; revise entry point |
| Content gap | Positive intent expressed, but specific requests for missing content recurring across contacts | The corpus has a real gap for this population | Document the gap, add to next version, re-engage with updated material |
| Framework isn't landing | Low engagement across all sectors after diagnostics; no vocabulary migration at Day 60 | The core framing does not resonate with target organizations' self-understanding of their mission | Reframe the entry point; test leading with Part 0 (actionable) before threat model (analytical) |

---

*Framework complete. This document should be read alongside `tier-1-success-metrics-framework.md` (per-organization tracking tables and metric definitions) and `tier-1-feedback-collection-protocol.md` (follow-up email templates and 30/90-day assessment tools). The Phase 2 decision tree in Section 6 is the operative synthesis of both documents.*

*Last reviewed: 2026-05-05*
