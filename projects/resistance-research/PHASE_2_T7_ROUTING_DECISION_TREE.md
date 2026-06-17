---
title: "Phase 2 T+7 Routing Decision Tree"
created: "2026-06-17"
status: "production-ready"
domains_covered: [48, 51, 59]
purpose: "Deterministic routing from checkpoint signal strength to Tier 2 activation sequences"
input_document: "JUNE_17_DAY7_CHECKPOINT_EXECUTION_CHECKLIST.md (Section 6 outputs)"
output_documents: "PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md (per-domain activation sequences)"
---

# Phase 2 T+7 Routing Decision Tree

*Resistance Research — Day 7-14 Checkpoint Routing*
*Built June 17, 2026. Input: signal scores from Day 7 checklist. Output: deterministic Tier 2 activation sequence.*

---

## How to Use This Document

**Prerequisites**: Complete JUNE_17_DAY7_CHECKPOINT_EXECUTION_CHECKLIST.md through Section 6. You need three values before entering this tree:
- Domain 59 composite signal: STRONG / MODERATE / WEAK
- Domain 51 composite signal: STRONG / MODERATE / WEAK
- Domain 48 composite signal: STRONG / MODERATE / WEAK

Enter the tree at Section 1, apply the signal thresholds for each domain, then follow the routing arrows to the correct activation sequence. The tree is fully deterministic — there is no ambiguous cell. Every combination of three signals has a prescribed output.

---

## Section 1: Outcome Classification Framework

### 1.1 Numerical Thresholds Per Domain

These thresholds govern the composite signal assignment. They supersede individual contact assessment.

**Domain 59 — Economic Precarity / CTC**

| Composite Signal | Condition |
|-----------------|-----------|
| STRONG | 2+ STRONG individual replies from 5 Wave 1 contacts AND 80%+ delivery rate |
| MODERATE | 1 STRONG individual reply, OR 3+ MODERATE individual replies, OR 3+ Gist clicks with no email replies |
| WEAK | 0 STRONG individual replies AND fewer than 3 MODERATE replies AND 0-2 Gist clicks AND 80%+ delivery |
| DIAGNOSTIC | Any delivery rate below 80% — run delivery diagnostic before signal classification |

**Why 2+ threshold for STRONG**: Domain 59 has 5 contacts with response probabilities of 45-70%. At this response probability range, a single STRONG reply is within the baseline expectation for a well-targeted research distribution. Two STRONG replies indicate above-baseline organizational interest — the signal is real, not noise.

**Domain 51 — Campaign Finance / Dark Money**

| Composite Signal | Condition |
|-----------------|-----------|
| STRONG | 2+ STRONG individual replies from Wave 1-2 (5 contacts) AND 80%+ delivery rate |
| MODERATE | 1 STRONG individual reply from Wave 1-2, OR 2+ MODERATE individual replies, OR CLC reply of any kind (highest-value anchor) |
| WEAK | 0 STRONG individual replies AND 0-1 MODERATE replies AND no Gist activity AND 80%+ delivery |
| DIAGNOSTIC | Delivery rate below 80% |

**Note on CLC as standalone MODERATE**: A reply from CLC (Erin Chlopak) at any quality level automatically elevates Domain 51 to MODERATE, regardless of other contacts. CLC's campaign finance constitutional team is the highest-value Domain 51 relationship. Even a boilerplate acknowledgment from CLC is a relationship confirmation.

**Domain 48 — Criminal Justice / Civic Exclusion**

| Composite Signal | Condition |
|-----------------|-----------|
| STRONG | 2+ STRONG individual replies from Wave 1-2 (6 contacts) AND 80%+ delivery rate |
| MODERATE | 1 STRONG individual reply, OR reply from Sentencing Project (any quality), OR 2+ MODERATE replies |
| WEAK | 0 STRONG individual replies AND no Sentencing Project reply AND 0-1 MODERATE replies AND 80%+ delivery |
| DIAGNOSTIC | Delivery rate below 80% |

**Note on Sentencing Project as standalone MODERATE**: Like CLC for Domain 51, a Sentencing Project reply at any quality level automatically elevates Domain 48 to MODERATE. The Sentencing Project "Locked Out" data is the primary empirical source for Domain 48 — a response from Nicole Porter signals the synthesis is being received as legitimate follow-on research.

### 1.2 Signal Assessment Worksheet

Complete before entering the routing tree:

```
Domain 59 composite: STRONG / MODERATE / WEAK / DIAGNOSTIC
Domain 51 composite: STRONG / MODERATE / WEAK / DIAGNOSTIC
Domain 48 composite: STRONG / MODERATE / WEAK / DIAGNOSTIC
```

---

## Section 2: Domain Sequencing Logic Per Outcome

### 2.1 Master Routing Matrix

Find your combination of three signals in the left three columns. The rightmost column is the prescribed activation sequence.

| D59 Signal | D51 Signal | D48 Signal | Prescribed Action |
|-----------|-----------|-----------|-------------------|
| STRONG | STRONG | STRONG | Full coalition protocol — see 2.2 |
| STRONG | STRONG | MODERATE | D59 Tier 2 immediate; D51 Tier 2 full; D48 Tier 2 FFJC only — see 2.3 |
| STRONG | STRONG | WEAK | D59 Tier 2 immediate; D51 Tier 2 full; D48 hold to Day 14 — see 2.4 |
| STRONG | MODERATE | STRONG | D59 Tier 2 immediate; D51 Tier 2 initial 3 only; D48 Tier 2 NAACP LDF + FFJC — see 2.5 |
| STRONG | MODERATE | MODERATE | D59 Tier 2 immediate; D51 Tier 2 initial 3; D48 Tier 2 FFJC only — see 2.6 |
| STRONG | MODERATE | WEAK | D59 Tier 2 immediate; D51 Tier 2 initial 3; D48 hold — see 2.7 |
| STRONG | WEAK | any | D59 Tier 2 immediate; D51 follow-up to CLC only on Day 14; D48 per D48 signal — see 2.8 |
| MODERATE | STRONG | any | D59 Tier 2 selective (EPI+NELP); D51 Tier 2 full; D48 per D48 signal — see 2.9 |
| MODERATE | MODERATE | STRONG | D59 Tier 2 selective (EPI+NELP); D51 Tier 2 initial 3; D48 Tier 2 NAACP LDF + FFJC — see 2.10 |
| MODERATE | MODERATE | MODERATE | D59 Tier 2 selective; D51 Tier 2 initial 3; D48 Tier 2 FFJC only — see 2.11 |
| MODERATE | MODERATE | WEAK | D59 Tier 2 selective; D51 Tier 2 initial 3; D48 hold — see 2.12 |
| MODERATE | WEAK | any | D59 Tier 2 EPI+NELP; D51 Day 14 CLC follow-up; D48 per D48 signal — see 2.13 |
| WEAK | STRONG | any | D59 forced activation (markup deadline); D51 Tier 2 full; D48 per D48 signal — see 2.14 |
| WEAK | MODERATE | any | D59 forced activation; D51 Tier 2 initial 3; D48 per D48 signal — see 2.15 |
| WEAK | WEAK | any | D59 forced activation; D51 Day 14 only; D48 per D48 signal — see 2.16 |
| DIAGNOSTIC | any | any | Delivery repair first; re-run checkpoint after repair — see 2.17 |

### 2.2 Full Coalition Protocol (All STRONG)

**Condition**: Domain 59 STRONG + Domain 51 STRONG + Domain 48 STRONG

This is the peak outcome. Indicates all three research documents are being received as substantive by their target constituencies. Activate at full scope simultaneously.

```
Day 0 (checkpoint day):
  Domain 59: Activate all 4 Tier 2 contacts (EPI, Demos, NELP, NHLP) — same day
  Domain 51: Activate initial 3 Tier 2 contacts (True North Research, Montana I-194, Michigan Clean Elections)
  Domain 48: Activate NAACP LDF + FFJC same day; schedule ACLU VA for June 27

Day 1-3:
  Domain 51: Activate secondary 5 Tier 2 contacts (after initial 3 confirmed sent)
  Domain 59: Monitor Tier 2 response; prepare Tier 3 activation for T+15
  Domain 48: Execute NAACP LDF + FFJC sends; confirm Virginia Right to Vote Coalition integration timeline

Day 4-7:
  Domain 51: Activate extended 5 Tier 2 contacts if initial 3 + secondary 5 confirmed sent
  Cross-domain coalition: Activate coordinated Tier 2 per Section 4 (coalition opportunity windows)
  
June 25 checkpoint: Assess Tier 2 response across all domains before July 1 deadline
```

### 2.3-2.16 Abbreviated Routing Notes

For all scenarios below STRONG/STRONG/STRONG:

**Domain 59 sequencing rule**: Domain 59 Tier 2 activates in EVERY scenario, including WEAK. The Senate Finance markup window is an immovable external deadline. The only question is whether to activate all 4 Tier 2 contacts (STRONG signal) or selective (EPI+NELP only, MODERATE signal) or forced-activation (WEAK signal, no contact reduction).

```
FORCED ACTIVATION (WEAK D59): Activate EPI + Demos + NELP (skip NHLP unless signal is confirmed)
SELECTIVE ACTIVATION (MODERATE D59): Activate EPI + NELP only
FULL ACTIVATION (STRONG D59): Activate all 4 Tier 2 contacts
```

**Domain 51 sequencing rule**: Activate Tier 2 contacts in three stages — initial 3 first, secondary 5 after 48-hour window, extended 5 only upon Tier 1-2 signal confirmation. Never send all 13 simultaneously — staged outreach prevents the appearance of mass distribution and allows response signals from early contacts to inform later contact framing.

```
STRONG D51: All three stages proceed without waiting for response between stages (time pressure)
MODERATE D51: Initial 3 + secondary 5 proceed; extended 5 waits for signal from initial 3
WEAK D51: Initial 3 only; CLC follow-up is the Day 14 pivot point
```

**Domain 48 sequencing rule**: Virginia July 15 deadline governs. Tier 2 activation for Domain 48 is less time-critical than Domains 59/51, but the July 15 deadline for the Virginia Right to Vote Coalition integration window creates a June 27 soft deadline for Tier 2 sends.

```
STRONG D48: NAACP LDF + FFJC + ACLU VA (June 27)
MODERATE D48: FFJC only immediate; LDF and ACLU VA on June 27
WEAK D48: Hold until Day 14; if still WEAK, activate ACLU VA contingency path immediately
```

### 2.17 Diagnostic Routing

**Condition**: Delivery rate below 80% on any domain.

Do not activate Tier 2 until delivery is repaired. A Tier 2 send to organizations in the same sector as failed Tier 1 sends is wasted — the delivery failure may be domain-wide.

```
Step 1: Identify bounced addresses per domain (5 minutes)
Step 2: Re-send to fallback/form contacts (20 minutes per domain)
Step 3: Wait 48 hours
Step 4: If delivery confirmed above 80%, return to checkpoint and apply signal thresholds
Step 5: If delivery still below 80% after re-send, escalate to user via CHECKIN.md
```

---

## Section 3: Escalation Triggers for User Input

The routing is autonomous except in the following conditions. If any of these conditions are met, halt autonomous routing and flag in CHECKIN.md under "Needs Your Input."

**Trigger 1 — Organizational opposition received:**

Definition: A reply from any contact that disputes the research conclusions, challenges the democratic design framing, or expresses concern about being included in the distribution.

This is not inherently a bad signal — critical engagement from policy experts can improve the research. But it is not within the autonomous routing mandate to decide how to respond to substantive criticism. Flag for user decision.

```
Flag template for CHECKIN.md:
"[Domain XX] — Organizational opposition received from [Organization].
Reply summary: [one sentence]
Decision needed: (a) engage substantively with the critique, (b) acknowledge and note for research revision,
(c) remove from future sends. Recommended: [option based on reply content]."
```

**Trigger 2 — Senate Finance markup completes before Domain 59 Tier 2 activation:**

If the markup vote occurs before any Domain 59 Tier 2 contact is reached, the original framing (CTC markup urgency) is obsolete. Tier 2 contacts can still be reached, but the framing shifts to "Build the 2027 Reform Coalition." This is a user decision — the coalition-building framing is still valid, but the Senate Finance urgency hook is gone.

```
Flag template:
"Domain 59 — Senate Finance markup completed on [date].
Domain 59 Tier 2 contacts not yet reached: [list].
Decision needed: proceed with '2027 Reform Coalition' framing per DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md
Part 7 Contingency 1, or hold all Domain 59 Tier 2 sends until next legislative window?
Recommended: proceed with coalition framing — the democratic participation argument is not time-limited to the markup."
```

**Trigger 3 — California ballot measure fails qualification:**

If the California Fair Elections Act fails to qualify for the November ballot before Domain 51 Tier 2 activation, the specific California-framed contacts (Common Cause CA, LWV California, Clean Money Action Fund) lose their primary urgent hook. Domain 51's FEC enforcement and dark money architecture materials remain valid for national contacts (CLC, Issue One, Brennan Center).

```
Flag template:
"Domain 51 — California ballot measure has [failed/status changed].
California-specific contacts (Common Cause CA, LWV CA, Clean Money AF) need framing revision.
National contacts (CLC, Issue One, Democracy 21) are unaffected.
Decision needed: proceed with national-only framing for Domain 51 Tier 2, or hold pending California status?
Recommended: proceed with national framing — FEC enforcement argument is California-independent."
```

**Trigger 4 — Tier 2 activation required before Week 2 email sends have cleared Day 7:**

If the autonomous sequence routes to Tier 2 activation for a domain whose Wave 1-2 sends are less than 7 days old, flag for user confirmation. The threshold logic assumes Day 7 has passed. Activating Tier 2 before Day 7 is possible for deadline-driven reasons (Domain 59 markup) but requires user awareness.

```
Flag template:
"Domain [XX] Tier 2 activation authorized by deadline logic before Day 7 of Wave 1-2.
Wave 1-2 send date: [date]. Tier 2 activation date: [date]. Days elapsed: [N].
This is within normal range for deadline-driven activation. Flagging for your awareness."
```

---

## Section 4: Cross-Domain Coalition Opportunity Windows

When multiple domains produce STRONG signals simultaneously, coordinated cross-domain outreach creates amplified organizational reach that single-domain activation cannot achieve.

### 4.1 Domain 51 + Domain 59 STRONG — Campaign Finance / Economic Democracy Bridge

**Condition**: Both Domain 51 (Campaign Finance / Dark Money) and Domain 59 (Economic Precarity / CTC) return STRONG signals.

**Coalition opportunity**: The dark money architecture (Domain 51) and economic precarity (Domain 59) are analytically connected: the organizations that fund the dark money infrastructure documented in Domain 51 have a direct material interest in the CTC refundability provisions Domain 59 opposes. A coordinated Tier 2 outreach to CBPP + Common Cause National + Demos frames this as a single democratic exclusion architecture argument — economic precarity creates the conditions that dark money exploits.

```
Coordinated Tier 2 outreach sequence:
Contact: Demos — Taifa Smith Butler (info@demos.org)
Frame: "Demos' mandate — 'equal say in democracy + equal chance in economy' — is the conjunction of
       Domains 51 and 59. The dark money architecture amplifies the voices of those who benefit from
       economic precarity while systematically excluding the voices of those who experience it."
Timing: Same day as Domain 59 Tier 2 activation, before Domain 51 Tier 2 activation
Purpose: Demos can serve as the cross-domain coalition anchor — they are naturally positioned in both
         the economic justice and campaign finance spaces

Contact: Common Cause National — Virginia Kase Solomón (commoncause@commoncause.org)
Frame: "Common Cause works on both campaign finance reform (Domain 51) and civic participation.
       Distributing both documents to the same Common Cause network creates internal coalition pressure
       for coordinated advocacy."
Timing: 2 days after Demos activation
```

**Estimated multiplier from coordination**: The Coalition Leverage Matrix Section 3 establishes a 2.0-2.5x reach multiplier from bridging the economic justice and campaign finance organizational ecosystems. Both domains independently reach their target sectors; the coordination argument reaches a different set of funders and advocates who sit at the intersection.

### 4.2 Domain 59 STRONG + Domain 48 MODERATE — Economic Precarity / Criminal Justice Bridge

**Condition**: Domain 59 STRONG, Domain 48 MODERATE.

**Coalition opportunity**: The economic precarity analysis (Domain 59) and criminal justice civic exclusion architecture (Domain 48) share the same affected population. A family below $35,000/year is statistically more likely to have members with felony disenfranchisement history AND more likely to experience the cognitive bandwidth depletion from financial precarity documented in Domain 59. The two domains function as a mutually reinforcing civic exclusion system.

```
Coordinated outreach:
Contact: NELP — Rebecca Dixon (info@nelp.org) [Domain 59 Tier 2]
Additional frame addition: "The gig economy and worker classification argument in Domain 59 intersects
                            with NELP's criminal record employment bar work (Domain 48 Section 2.4).
                            Workers who face both employment barriers are documented in both analyses."
Note: This does not require a new send — add two sentences to the NELP Domain 59 email that reference
      the criminal record employment bar overlap.

Contact: NAACP LDF — Janai Nelson (info@naacpldf.org) [Domain 48 Tier 2]
Additional frame addition: "NAACP LDF's work on both voting rights restoration (Domain 48) and economic
                            justice (Domain 59's CTC analysis) gives them standing to receive both
                            documents. A coordinated send to LDF that references both domains signals
                            the structural unity of the civic exclusion architecture."
```

### 4.3 Domain 51 STRONG + Domain 48 STRONG — Institutional Accountability Bridge

**Condition**: Both Domain 51 (Campaign Finance) and Domain 48 (Criminal Justice) return STRONG signals.

**Coalition opportunity**: Dark money flows into prosecutorial races and criminal justice ballot initiatives. Domain 51's FEC enforcement collapse enables the same dark money actors who fund ballot measures that roll back voting rights restoration (Domain 48). The Brennan Center is the natural bridge — they work on both campaign finance enforcement and voting rights restoration.

```
Coordinated outreach:
Contact: Brennan Center for Justice
Domain 51: Saurav Ghosh (ghoshs@brennan.law.nyu.edu) — campaign finance angle
Domain 48: Sean Morales-Doyle (brennancenter.org web form) — voting rights angle
Note: These are different staff members. Send both on the same day (or one day apart) with a
      brief cover note to each mentioning that both documents were shared with the organization.
      This signals coordinated research — Brennan Center's internal routing may surface the overlap.
Timing: Send Domain 48 first (use web form); send Domain 51 one day later (email to Ghosh)
```

---

## Section 5: Failure Paths

### 5.1 All Domains WEAK at Day 7

**Condition**: Domain 59 WEAK + Domain 51 WEAK + Domain 48 WEAK

This means zero substantive replies and minimal Gist engagement across all three domains at Day 7. This is not a campaign failure — it is a monitoring signal. Day 7 is too early to conclude engagement failure for most policy organizations.

**Day 7 WEAK action (immediate):**

```
Step 1: Run delivery diagnostic (Section 1.4 of checklist) — confirm all sends delivered
Step 2: Domain 59 FORCED activation regardless of WEAK signal — Senate markup deadline is immovable
Step 3: All other domains: hold at Day 14 checkpoint — do NOT activate Tier 2 before Day 14
Step 4: Log in WORKLOG.md: "Day 7 checkpoint — all domains WEAK signal — delivery confirmed —
        Domain 59 forced activation per Senate Finance deadline — D51/D48 hold to Day 14"
```

**Day 14 reassessment (June 24-25):**

If all domains are still WEAK at Day 14 (14 days from Wave 1-2 sends), escalation is required:

```
Escalation sequence:
1. Domain 59: Has Senate markup completed? If yes, shift to coalition framing. If no, activate all Tier 2 same day.
2. Domain 51: Direct outreach to CLC via a different contact pathway (try their media contact or conference presence)
3. Domain 48: Activate ACLU of Virginia contingency path — this is a warm coalition member, not cold outreach
4. All domains: Consider consolidating to 1-2 strongest domains for focused effort (see 5.2)
```

### 5.2 Consolidation Decision — When to Focus vs. Spread

If Domain 59 is WEAK + Domain 51 is WEAK at Day 14 but Domain 48 returns STRONG, consolidation logic applies:

**Consolidation to strongest domain**: When two or more domains return WEAK signal at Day 14, consider concentrating Tier 2 effort on the STRONG domain rather than equally distributing effort across all three. The STRONG domain's organizational relationships are the most ready for coalition deepening. The WEAK domains may benefit from being held for a Phase 3 consolidation rather than forced Tier 2 activation.

**Consolidation trigger**: If 2+ domains are WEAK at Day 14 AND the one STRONG domain is receiving active organizational engagement (Score 4-5 replies), consolidate to STRONG domain for the next 14 days before reassessing the WEAK domains.

**Anti-consolidation exception**: Domain 59 cannot be consolidated away from. The Senate Finance markup deadline means Domain 59 Tier 2 must execute regardless of signal strength. If Domain 59 is the WEAK domain, execute forced activation and treat it as a standalone late-stage distribution, not a coalition-building exercise.

### 5.3 Skipping to Phase 3

**Condition**: All Tier 1 sends are WEAK at Day 30 (July 1) with no recovery.

If 30 days after Wave 1-2 distribution, zero substantive organizational relationships have formed across all three domains, the Phase 2 multi-domain coalition strategy has not achieved its objective. This is a user decision, not an autonomous routing decision. Flag in CHECKIN.md:

```
Flag template:
"Day 30 checkpoint — all three domains (59, 51, 48) below STRONG threshold after full distribution.
Phase 2 Tier 2 contact lists remain available for future activation.
Options:
  (a) Hold all Tier 2 and reassess at August 1 with updated external deadline context
  (b) Consolidate to Domain 51 only (July 1 CA ballot) and Domain 59 only (Senate Finance 2027 window)
  (c) Skip to Phase 3 domain research (Domains H, K, 37A) without Phase 2 coalition formation
  (d) Revise research framing based on 30-day signal failure pattern

Recommended: Option (a) + (b) simultaneously — hold multi-domain Tier 2 but keep Domain 51/59
             active for their specific coalition contexts. Phase 3 research can proceed in parallel."
```

---

## Visual Summary Tree

```
                    DAY 7 CHECKPOINT
                          |
          ┌───────────────┼───────────────┐
          |               |               |
    D59 Signal       D51 Signal       D48 Signal
    (assess)         (assess)         (assess)
          |               |               |
     ┌────┴────┐     ┌────┴────┐     ┌────┴────┐
  STRONG   MOD/WEAK  STRONG   MOD/WEAK  STRONG   MOD/WEAK
     |         |        |         |        |         |
  D59 T2    D59 T2   D51 T2    D51 T2   D48 T2    D48 T2
  ALL 4    EPI+NELP  ALL 13   Initial3  LDF+FFJC   FFJC
  (imm.)  (or forced  or      only +     +          only
           if markup) Staged  Day14 CLC  ACLU VA    (June 27)
                              follow-up  June27

              CROSS-DOMAIN CHECK (Section 4):
              D59 + D51 STRONG? → Demos + Common Cause bridge
              D59 + D48 STRONG? → NELP + NAACP LDF coordination
              D51 + D48 STRONG? → Brennan Center dual-domain send
              ALL STRONG? → Full coalition protocol (Section 2.2)

              ESCALATION CHECK (Section 3):
              Opposition received? → User input required
              Markup completed? → User input required
              CA ballot failed? → User input required
              Day 14 all WEAK? → Consolidation or Phase 3 decision
```

---

## Execution Commands

After determining the routing, execute via the orchestration script:

```bash
# Run full T7 checkpoint (collects state, prints routing recommendation):
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --t7-checkpoint

# Apply routing decision with signal inputs:
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py \
  --routing-decision 59 51 48 STRONG MODERATE WEAK

# Activate Tier 2 for a specific domain:
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py \
  --activate-tier2 59 STRONG

# Check all domains status before routing:
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --all-domains-status
```

---

*Built June 17, 2026. Input framework: JUNE_17_DAY7_CHECKPOINT_EXECUTION_CHECKLIST.md. Output protocols: PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md. Autonomous routing is deterministic except for the four user-input escalation triggers in Section 3.*
