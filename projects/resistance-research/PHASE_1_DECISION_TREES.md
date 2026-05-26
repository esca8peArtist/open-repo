---
title: "Phase 1 Decision Trees — Checkpoint Protocols"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Concrete decision trees for Day 7, Day 30, and Day 60 checkpoints. Includes rapid-response
  protocol for overperformance and failure-recovery protocol for low engagement.
  All thresholds are specific numbers — no vague criteria.
word_count: ~900
companion_files:
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md
  - SYNTHESIS_OUTCOME_PLAYBOOKS.md
  - PHASE_2_LAUNCH_DECISION_TRIGGERS.md
  - DOMAIN_39_DISTRIBUTION_STRATEGY.md
  - DOMAIN_56_DISTRIBUTION_STRATEGY.md
---

# Phase 1 Decision Trees

**Version 1.0 — May 26, 2026**

These decision trees translate dashboard data into specific actions. At each checkpoint date, open the dashboard, pull the numbers, and follow the tree. Each branch terminates in an explicit action, not a recommendation to "consider" something.

---

## Day 7 Decision Tree

**Run this tree**: 7 calendar days after the Wave 1 send date.
**Data source**: Gist View Log (total Bitly clicks, Week 1 column), Master Contact Log (reply count, delivery status).

```
START: Pull Week 1 Bitly total clicks and reply count from dashboard
               │
               ▼
      [Check delivery status first]
               │
      ┌────────┴────────┐
      │                 │
  Any bounces?      Zero bounces
      │                 │
  YES: How many?        │
      │                 │
  ≥3 bounces            │
      │                 │
  CONTACT VERIFY ───────┤
  Pull BATCH_1_CONTACT_ │
  VERIFICATION.md       │
  Re-check emails       │
  Re-send to corrected  │
  addresses.            │
  Restart Day 7 clock.  │
      │                 │
  <3 bounces            │
  (continue)            │
      │                 │
      └────────┬────────┘
               │
               ▼
      [Check Bitly total clicks, Week 1]
               │
         ┌─────┴──────┐
         │            │
      15+ clicks    <15 clicks
         │            │
         │    ┌───────┴───────┐
         │    │               │
         │  5-14 clicks    0-4 clicks
         │    │               │
         │  MONITOR:      Check: were emails
         │  Engagement    actually sent?
         │  below target     │
         │  but not zero.  YES delivered,
         │  Continue to    still 0 clicks:
         │  Day 14 check.    │
         │    │           ESCALATE:
         │    │           Run delivery
         │    │           diagnostic now.
         │    │           See Section 1.2
         │    │           of PHASE_1_IMPACT_
         │    │           MEASUREMENT_
         │    │           INFRASTRUCTURE.md
         │    │
         ▼    ▼
      [Check reply count]
               │
         ┌─────┴──────┐
         │            │
      2+ replies   0-1 replies
         │            │
      STATUS:      STATUS:
      HOLD         MONITOR
      Normal       Below baseline.
      trajectory.  Check again
      No action    Day 10-12.
      required.    If still 0-1,
      Continue     apply framing
      to Day 30    revision
      checkpoint.  (see Section 6.3
                   of framework).
```

**Day 7 summary statuses**:
- HOLD: 15+ clicks AND 2+ replies. Continue to Day 30.
- MONITOR: 5-14 clicks OR 0-1 replies (with confirmed delivery). Check again at Day 14.
- ESCALATE: 0-4 clicks with confirmed delivery, OR 3+ bounces. Run diagnostics and delivery check within 24 hours.

---

## Day 30 Decision Tree

**Run this tree**: 30 calendar days after the Wave 1 send date.
**Data source**: Constituency-Aggregated Metrics sheet (constituencies passing strong threshold), Master Contact Log (overall reply rate, Score 3+ rate), Adoption Signal Registry (confirmed adoption count, cross-org references).

```
START: Pull four numbers from dashboard:
  (A) Overall Score 3+ reply rate [%]
  (B) Constituencies passing Day30 Strong threshold [count of 7]
  (C) Cross-organizational references [count]
  (D) Confirmed adoption signals [count]
               │
               ▼
      [Check for STRONG threshold]

  A >= 50%  AND  B >= 4  AND  C >= 3  AND  D >= 2
               │
         ┌─────┴─────┐
         │           │
       YES           NO
         │           │
    STRONG:          │
    Activate Phase 2 │
    immediately.     │
    Execute same-day │
    protocol         │
    (see below).     │
                     ▼
            [Check for MODERATE threshold]

     A 30-49%  OR  B >= 3  OR  C >= 1  OR  D >= 1
                     │
              ┌──────┴──────┐
              │             │
            YES             NO
              │             │
         MODERATE:          │
         Activate Domain 39 │
         within 24 hours.   │
         Hold Domain 56     │
         until Day 37.      │
         Continue           │
         monitoring to      │
         Day 60.            │
                            ▼
                   [Check for WEAK signal]

                A < 20%  AND  B < 2  AND  C = 0
                            │
                     ┌──────┴──────┐
                     │             │
                   YES             NO
                     │       (In between —
                  WEAK:       not weak, not
                  Do not      moderate. Hold.
                  extend same Continue to
                  approach.   Day 45 check.)
                  Apply
                  3-modification
                  failure recovery
                  (see below).

            [Check for FAILURE signal]
                A < 10%  AND  C = 0  AND  D = 0
                AND zero Gist clicks in Week 3-4
                            │
                     ┌──────┴──────┐
                     │             │
                   YES             NO
                     │             │
                 FAILURE:      Continue
                 Full          monitoring.
                 contingency
                 review.
                 Add to
                 CHECKIN.md
                 under
                 "Needs Your Input."
```

**Day 30 immediate actions by determination**:

**STRONG — execute within 24 hours**:
1. Add STRONG determination to CHECKIN.md with per-constituency breakdown
2. Pull Domain 39 distribution contact list from DOMAIN_39_DISTRIBUTION_STRATEGY.md and send within 24 hours (June 1 HHS deadline is the hard stop — do not delay)
3. Pull Domain 56 Gist URL (https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f) and verify content is current
4. Begin Domain 56 outreach within 48 hours using social proof from confirmed Score 4-5 Tier 1 replies
5. Begin Tier 2 law school pre-contact list preparation using social proof framing
6. No re-synthesis needed — STRONG at Day 30 overrides the May 25 re-synthesis calendar gate

**MODERATE — execute within 24-48 hours**:
1. Add MODERATE determination to CHECKIN.md
2. Send Domain 39 distribution within 24 hours (June 1 HHS deadline is non-negotiable)
3. Extend Phase 1 monitoring period to Day 60 for remaining constituencies
4. Prepare Domain 56 for launch at Day 37-40 — do not launch before then
5. Do not begin Tier 2 expansion yet; wait for Day 60 checkpoint

**WEAK — execute within 72 hours**:
1. Add WEAK determination to CHECKIN.md under "Needs Your Input"
2. Do not send Domain 56 or expand Tier 2 outreach yet
3. Send Domain 39 only (June 1 HHS deadline overrides weak outcome — healthcare urgency is constituency-specific)
4. Apply 3-modification failure recovery (see Failure Recovery Protocol below)
5. Set Day 90 extension checkpoint

---

## Day 60 Decision Tree

**Run this tree**: 60 calendar days after the Wave 1 send date.
**Data source**: Adoption Signal Registry (confirmed adoptions count, people reached), Constituency-Aggregated Metrics (all 7 constituencies), Network Map (network events, second-hop referrals).

```
START: Pull three numbers:
  (X) Confirmed adoptions [target: 15]
  (Y) Estimated people reached [target: 100]
  (Z) Constituencies with at least 1 confirmed adoption [count of 7]
               │
               ▼
      [Check movement-scale target]

          X >= 15  AND  Y >= 100
               │
         ┌─────┴─────┐
         │           │
       YES           NO
         │           │
    MOVEMENT:        │
    Phase 2 full     │
    scale launch.    │
    All 7            │
    constituencies   │
    at Tier 2.       │
    Activate all     │
    pending Phase 2  │
    domains in       │
    priority order.  │
                     ▼
           [Check partial success]

            X >= 8  AND  Y >= 50
                     │
              ┌──────┴──────┐
              │             │
            YES             NO
              │             │
         PARTIAL:      BELOW TARGET:
         Phase 2        Review Z.
         launches at    If Z >= 4:
         scale only     launch Phase 2
         in Z           for those 4
         constituencies constituencies.
         where adoption  If Z < 4:
         confirmed.      Add to CHECKIN.md.
         Hold others.    User decision
                         required.
```

**Day 60 full-scale activation actions**:
1. Update CHECKIN.md with Day 60 determination and all 7 constituency scores
2. Pull Phase 2 domain priority order from PHASE_2_LAUNCH_DECISION_TRIGGERS.md
3. Activate Tier 2 expansion in all constituencies where Day 60 adoption is confirmed
4. For each constituency at Tier 2: use confirmed adoption evidence as social proof in outreach ("X organizations have incorporated this framework into [their specific practice]")
5. Domain 57 (Multilateral Withdrawal) distribution deadline is August 10 — confirm it is on track given current Phase 2 research status

---

## Rapid-Response Protocol: Overperformance Before Day 30

If Day 7 data shows STRONG signals (reply rate already above 30% by Day 7, or Score 5 reply received from any Tier 1 contact), do not wait for Day 30 to activate Phase 2. Same-day activation is available:

**Score 5 trigger (any single contact)**:
A Score 5 event is: citation in a published work, formal collaboration offer, or explicit statement of institutional adoption (e.g., "we are incorporating this into our clinic curriculum"). Receipt of a single Score 5 event from any Tier 1 contact at any point in Phase 1 triggers immediate Phase 2 pre-activation, regardless of the calendar date.

**Pre-Day 30 activation checklist**:
1. Record the Score 5 event in Master Contact Log and Adoption Signal Registry
2. Add EARLY SIGNAL note to CHECKIN.md within 24 hours
3. Pull Domain 39 distribution contact list and send within 48 hours (healthcare urgency applies regardless of timing)
4. Begin Domain 56 Gist distribution preparation
5. Notify orchestrator via CHECKIN.md entry: "SCORE 5 RECEIVED — Phase 2 pre-activation underway"
6. Do not begin Tier 2 scale outreach yet — wait until at least 3 Score 3+ replies are in hand before using social proof framing

**Score 4 trigger (two or more contacts)**:
Receipt of Score 4 events (forward to colleague, collaboration request) from 2 or more Tier 1 contacts within the first 14 days is a pre-Day 30 STRONG signal. Apply the same checklist as above.

---

## Failure Recovery Protocol: Low Engagement by Day 30

If Day 30 determination is WEAK or FAILURE, the recovery protocol requires three concrete modifications before extending Phase 1 to Day 90. Extending without modifying will produce the same result.

**Modification 1 — Stakeholder substitution (apply within 7 days of WEAK determination)**:
Replace 30% of non-responding Tier 1 contacts with next-tier equivalents:
- Law schools: Replace school-level dean contacts with clinic directors and faculty seminar organizers
- Civil rights orgs: Replace national directors with state chapter leads and voting rights staff attorneys
- Academic: Replace senior faculty with assistant professors and postdoctoral fellows (faster response cycles)
- Faith coalitions: Replace national denominational contacts with regional faith justice coordinators
- Labor unions: Replace national union presidents with state AFL-CIO education directors
- Mutual aid: Replace national umbrella organizations with local network coordinators

**Modification 2 — Framing revision (apply to all Day 90 outreach)**:
Replace the full framework pitch with a single-domain operational offer:
- Law schools (election law): Lead with Domain 37 only; frame as "a 40-page election interference analysis ready for clinic use"
- Immigration legal aid: Lead with Domain 29 model brief language only; frame as "a prosecutorial weaponization brief framework available for immediate adaptation"
- Civil rights: Lead with the litigation tracker or Domain 1 only; tie directly to an active case or advocacy campaign
- Academic: Lead with Domain 37 or Domain 6 research notes only; frame as "working notes I'd welcome scholarly critique on"
- Faith: Lead with Domains 39 or 22; frame around healthcare justice or racial equity themes
- Labor: Lead with Domain 17 (labor relations) only; tie directly to current NLRB or PRO Act developments
- Mutual aid: Lead with the community resilience framing from any domain; avoid policy-framework terminology

**Modification 3 — Channel shift (apply by Day 45)**:
Move 50% of Phase 1 effort from direct email outreach to network-intermediary distribution:
- Identify 2-3 existing strong advocates in each constituency (anyone who replied at Score 3+ becomes an intermediary candidate)
- Ask each strong advocate directly: "Would you be willing to share this with 2-3 colleagues at peer organizations?"
- Submit domain summaries to Just Security, Lawfare, or the Yale Journal on Regulation as short online essays
- Deposit framework materials in conference pre-read packets for the next relevant convening in each constituency's field
- Approach state and local bar associations directly (lower prestige than national targets, but much higher response rates to independent research outreach)

**Day 90 extension checkpoint**: If Modification 1-3 are applied and the Day 90 checkpoint still shows below MODERATE engagement, add a formal note to CHECKIN.md requesting user decision on whether to continue Phase 1, pivot to public-channel distribution only, or close Phase 1 and move to Phase 2 with whatever social proof has been gathered.
