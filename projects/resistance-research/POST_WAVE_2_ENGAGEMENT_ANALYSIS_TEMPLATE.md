---
title: "Post-Wave 2 Engagement Analysis Template"
subtitle: "Wave 1 vs Wave 2 Comparative Metrics, Constituency Clustering, and Phase 2 Forecasting"
created: "2026-06-14"
status: "production-ready — complete at June 17-18 Day 7 checkpoint"
usable_at: "17:00 UTC June 17, 2026 (immediately after Wave 1-2 execution completes)"
execution_time: "25-35 minutes to complete all sections"
data_source_window: "June 14-15, 2026 (Wave 1-2 sends) → June 17-18 (Day 7 read)"
companion_docs:
  - "DAY_7_CHECKPOINT_ROUTING_DECISION_TREE.md (routes this analysis to action)"
  - "PHASE_2_RESOURCE_ALLOCATION_CONTINGENCY_MATRIX.md (converts metrics to capacity plan)"
  - "DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md (sequencing logic)"
  - "DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md (Domain 51 sprint scaffold)"
  - "DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md (Domain 59 sprint scaffold)"
  - "PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md (baseline constituencies and scoring)"
domains: [51, 59]
note: >
  This template requires NO pre-existing Wave 1-2 data to use. All data fields are blank
  and filled at checkpoint. The framework sections, benchmarks, and constituency clusters
  are pre-built. Data arrives June 15 post-execution; analysis runs June 17.
---

# Post-Wave 2 Engagement Analysis Template

**Version 1.0 — June 14, 2026**

**Lead finding**: The Day 7 checkpoint is the highest-leverage diagnostic point in Phase 2 outreach. Seven days captures delivery confirmation (bounces surface within 24-72 hours), initial reply velocity (most replies to cold advocacy emails arrive within the first 3-5 days), and first-pass Gist click data. This template aggregates all available signals at exactly that point and feeds the routing decision in `DAY_7_CHECKPOINT_ROUTING_DECISION_TREE.md`.

Instructions: Complete each section in order. Estimated completion time is 25-35 minutes. The analysis does not require contacting any recipient to ask about engagement — all data is pulled from inbox, Gist click logs, and send confirmation records.

---

## Section 1: Wave Execution Confirmation

*Complete this section first. If any send is unconfirmed, resolve before proceeding to metrics.*

### 1.1 Wave 1 Send Confirmation (Target: June 14, 2026)

**Domain 59 — Wave 1 (Economic Precarity / CTC)**

| Contact # | Organization | Email | Send Confirmed? | Send Timestamp | Bounce? |
|-----------|---|---|---|---|---|
| 1 | AFL-CIO | feedback@aflcio.org | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |
| 2 | CBPP | cbpp@cbpp.org | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |
| 3 | NWLC | info@nwlc.org | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |
| 4 | MomsRising | info@momsrising.org | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |
| 5 | ITEP | itep@itep.org | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |

**Domain 59 Wave 1 Summary**: _____ / 5 confirmed delivered. Bounce count: _____

**Domain 51 — Wave 1 (Campaign Finance / Dark Money)**

| Contact # | Organization | Email | Send Confirmed? | Send Timestamp | Bounce? |
|-----------|---|---|---|---|---|
| 1 | Campaign Legal Center | echlopak@campaignlegalcenter.org | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |
| 2 | Issue One | ________________ | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |

**Domain 51 Wave 1 Summary**: _____ / 2 confirmed delivered. Bounce count: _____

---

### 1.2 Wave 2 Send Confirmation (Target: June 15, 2026)

**Domain 51 — Wave 2 (Campaign Finance / State Ballot)**

| Contact # | Organization | Email | Send Confirmed? | Send Timestamp | Bounce? |
|-----------|---|---|---|---|---|
| 1 | Common Cause California | ________________ | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |
| 2 | League of Women Voters CA | ________________ | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |
| 3 | Clean Money Action Fund | ________________ | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |

**Domain 51 Wave 2 Summary**: _____ / 3 confirmed delivered. Bounce count: _____

**Domain 59 — Wave 2 (if additional sends executed)**

| Contact # | Organization | Email | Send Confirmed? | Send Timestamp | Bounce? |
|-----------|---|---|---|---|---|
| 1 | [Additional D59 contact] | ________________ | [ ] YES / [ ] NO | _________ UTC | [ ] YES / [ ] NO |

**Combined Delivery Rate**: _____ / _____ total contacts confirmed delivered = _____% delivery rate

**Bounce Flag Threshold**: Any bounce rate above 10% (>1 in 10 sends) triggers Section 7.1 Delivery Diagnostic before proceeding.

---

## Section 2: Per-Wave Metrics Aggregation — Wave 1 vs Wave 2

*Pull data from email inbox and Gist click logs. All calculations are shown so any data gap is immediately visible.*

### 2.1 Reply Rate by Wave

**Definition**: A reply is any response that is not an auto-OOO. Include substantive and non-substantive replies in the raw count; apply the scoring filter in Section 2.2.

| Wave | Domain | Sends Delivered | Replies Received | Raw Reply Rate | Score 3+ Replies | Substantive Reply Rate |
|------|--------|---|---|---|---|---|
| Wave 1 | D59 (CTC) | _____ | _____ | ____% | _____ | ____%|
| Wave 1 | D51 (Campaign Finance) | _____ | _____ | ____% | _____ | ____%|
| Wave 2 | D51 (State Ballot) | _____ | _____ | ____% | _____ | ____%|
| **TOTAL** | **Both domains** | **_____** | **_____** | **____%** | **_____** | **____%** |

**Phase 1 Wave 1 Baseline (from PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md)**: The Day 7 minimum viable engagement threshold from Phase 1 is: at least 4 of 7 constituencies showing at least 1 engagement signal, and at least 15 total Bitly clicks. Phase 2 does not track Bitly clicks (no Bitly links in Phase 2 wave emails), so the analogous baseline is: at least 1 substantive reply per domain per wave.

---

### 2.2 Reply Scoring (Apply to Each Reply Received)

Use the scoring system from PHASE_1_IMPACT_MEASUREMENT_INFRASTRUCTURE.md. Enter each reply in the log below.

| # | Date | From | Organization | Domain | Score (1-5) | Score Rationale | Notes |
|---|------|------|---|---|---|---|---|
| 1 | _______ | _______ | _______ | ___ | ___ | _______ | _______ |
| 2 | _______ | _______ | _______ | ___ | ___ | _______ | _______ |
| 3 | _______ | _______ | _______ | ___ | ___ | _______ | _______ |
| 4 | _______ | _______ | _______ | ___ | ___ | _______ | _______ |
| 5 | _______ | _______ | _______ | ___ | ___ | _______ | _______ |

**Scoring key**:
- Score 1: Auto-reply or OOO only (do not count as a reply in Section 2.1)
- Score 2: Acknowledgment without substantive content ("Thank you for sharing")
- Score 3: Substantive engagement — response engages with specific content, asks a follow-up question, or requests additional information
- Score 4: High-value engagement — request for materials, offer to forward to colleague, or statement of intent to use
- Score 5: Adoption signal — explicit commitment to incorporate into organizational work, litigation, curriculum, or testimony

**Network multiplier events** (weighted 3x in composite score): Record any instance where a recipient reports forwarding to a colleague or where an unsolicited contact appears who was referred by a Wave 1-2 recipient.

| # | Date | Referring Contact | Referred To | Domain | Notes |
|---|------|---|---|---|---|
| 1 | _______ | _______ | _______ | ___ | _______ |

---

### 2.3 Open Rate Proxy — Gist Click Data

Phase 2 waves embed the Gist URLs directly in emails. Gist click data (visible via GitHub's view counter and any Bitly wrapping applied at send time) provides an open-rate proxy: a contact who clicked the Gist link has certainly opened the email.

**Check Gist view deltas at Day 7 against Day 0 (pre-send baseline).**

| Gist | URL | Day 0 View Count | Day 7 View Count | Delta (clicks) | Spike Date(s) | Spike Correlated to Wave? |
|------|-----|---|---|---|---|---|
| Domain 59 | https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba | _____ | _____ | _____ | _______ | [ ] YES / [ ] NO |
| Domain 51 | https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 | _____ | _____ | _____ | _______ | [ ] YES / [ ] NO |

**Spike detection rule (from Phase 1 framework)**: A single-day view spike of more than 5 clicks on any Gist is a flag event. Cross-reference with Wave send date. If spike occurs 24-72 hours after send, it confirms delivery and click-through. If spike occurs with no corresponding send (organic amplification), flag as a network multiplier signal.

---

### 2.4 Benchmark Table — Wave 1 vs Wave 2 vs Phase 1 Historical Baseline

| Metric | Phase 1 Wave 1 Baseline | Phase 2 Wave 1 (D59) | Phase 2 Wave 1 (D51) | Phase 2 Wave 2 (D51) | Combined |
|--------|---|---|---|---|---|
| Send count | ~45 Tier 1 (Phase 1) | 5 | 2 | 3 | 10 |
| Confirmed delivery rate | Target: >95% | ____% | ____% | ____% | ____% |
| Bounce rate | Target: <5% | ____% | ____% | ____% | ____% |
| Any reply (raw) by Day 7 | Minimum viable: 4 constituencies | _____ replies | _____ replies | _____ replies | _____ |
| Substantive reply rate (Score 3+) | Phase 1 Day 7 min: 1 per constituency | ____% | ____% | ____% | ____% |
| Gist click delta Day 7 | Phase 1 min: 15 clicks across all links | _____ | _____ | N/A | _____ |
| Network multiplier events | Phase 1 target: 1 by Day 60 | _____ | _____ | _____ | _____ |

**Benchmark interpretation**: Phase 2 sends are smaller in volume (10 contacts vs 45 in Phase 1) but more targeted. A single Score 4-5 reply from CBPP, AFL-CIO, or CLC carries more advocacy weight than a 50% reply rate from Phase 1 academic contacts. Do not penalize Phase 2 for lower raw reply counts — adjust benchmarks for contact specificity.

---

## Section 3: Constituency-Level Response Clustering

*Map each reply and click signal to its constituency. Cross-reference the 7 constituencies from PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 4.*

### 3.1 Constituency Engagement Map

| Constituency | Domain 59 Contacts in Waves 1-2 | Domain 51 Contacts in Waves 1-2 | Replies/Clicks Received | Constituency Status |
|---|---|---|---|---|
| Labor unions | AFL-CIO (D59 Wave 1) | — | _______ | [ ] Active / [ ] Silent |
| Policy research | CBPP, ITEP (D59 Wave 1) | OpenSecrets (D51 expansion) | _______ | [ ] Active / [ ] Silent |
| Women's rights advocacy | NWLC, MomsRising (D59 Wave 1) | LWV CA (D51 Wave 2) | _______ | [ ] Active / [ ] Silent |
| Campaign finance / legal | — | CLC, Issue One (D51 Wave 1) | _______ | [ ] Active / [ ] Silent |
| State ballot campaigns | — | Common Cause CA, Clean Money Action Fund (D51 Wave 2) | _______ | [ ] Active / [ ] Silent |
| Immigration / civil rights | — | — | N/A | Not in Waves 1-2 |
| Law schools | — | — | N/A | Not in Waves 1-2 |

**Note**: Phase 2 Waves 1-2 deliberately concentrate on 5 of the 7 Phase 1 constituencies. Law schools and immigration legal aid are not primary Phase 2 Domain 51/59 targets. Immigration legal aid remains a Phase 2 target in other domains (e.g., Domain 29).

### 3.2 Cross-Domain Constituency Overlap

Identify any contact whose organization spans both Domain 51 and Domain 59 thematic territory. Per DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md Section 4, the following organizations are cross-domain integration candidates:

- **Common Cause** (national): Receives Domain 51 CA state wave AND operates in economic justice space. If Common Cause National replies to Domain 51 state contacts, flag as cross-domain integration opportunity.
- **Brennan Center**: Domain 51 Tier 1 expansion target AND documented in Phase 1 as a civil rights/voting rights organization overlapping with Domain 59 participation gap research.
- **AFL-CIO**: Domain 59 Wave 1 Tier 1 recipient AND implicitly positioned to receive the integrated FEC-enforcement-collapse/dark-money framing connecting Domains 51 and 59.

**Cross-domain integration event log**:

| Organization | Received Domain 51? | Received Domain 59? | Cross-Domain Signal? | Action |
|---|---|---|---|---|
| Common Cause | [ ] YES [ ] NO [ ] PENDING | [ ] YES [ ] NO | _______ | _______ |
| Brennan Center | [ ] YES [ ] NO [ ] PENDING | [ ] YES [ ] NO | _______ | _______ |
| AFL-CIO | [ ] YES [ ] NO | [ ] YES [ ] NO [ ] PENDING | _______ | _______ |

---

## Section 4: Weak-Signal Detection — Outreach Failures

*Identify failures before they compound. Each failure type has a pre-built recovery action.*

### 4.1 Bounce Analysis

| # | Contact | Email | Bounce Type | Bounce Timestamp | Recovery Action |
|---|---------|-------|---|---|---|
| 1 | _______ | _______ | [ ] Hard / [ ] Soft / [ ] No bounce info | _______ | Use backup email per contact snapshot |
| 2 | _______ | _______ | [ ] Hard / [ ] Soft / [ ] No bounce info | _______ | Use backup email per contact snapshot |

**Backup email sources**:
- Domain 51 backups: DOMAIN_51_CONTACT_REACHABILITY_SNAPSHOT.md (June 10, 2026 audit)
- Domain 59 backups: DOMAIN_59_CONTACT_REACHABILITY_SNAPSHOT.md (June 10, 2026 audit)

**Hard bounce rule**: Any hard bounce requires switching to the backup email before Day 7 checkpoint. Do not re-send to a hard-bounced address.

**Soft bounce rule**: Wait 24 hours; if no delivery confirmation, attempt backup email.

---

### 4.2 Opt-Out and Decline Tracking

| # | Contact | Organization | Opt-Out Type | Date | Notes |
|---|---------|---|---|---|---|
| 1 | _______ | _______ | [ ] Explicit unsubscribe / [ ] Polite decline / [ ] No further contact request | _______ | _______ |

**Opt-out action**: Remove from all future sends immediately. Do not re-contact under any framing.

**Declination distinction**: A polite decline ("Not the right fit for our current work") is NOT an opt-out and does NOT preclude re-contact in 90 days with a different framing or updated materials. Log as Score 1 with note "decline — re-contact eligible Day 90+".

---

### 4.3 Non-Response Pattern Analysis

This section applies at Day 7. Non-response at Day 7 is not a failure signal — it is the base case. The diagnostic question is: what does the pattern of non-response tell us?

**Tier-based non-response interpretation**:

| Contact Tier | Day 7 Non-Response Meaning | Action |
|---|---|---|
| Tier 1 (national policy) — CLC, CBPP, AFL-CIO, NWLC | Normal. These organizations have 7-14 day typical reply cycles for cold advocacy outreach. Non-response at Day 7 is within normal range. | No action. Monitor through Day 14. |
| Tier 1 (state ballot) — Common Cause CA, LWV CA, Clean Money Action Fund | Slightly faster expected cycle (5-10 days) given active ballot campaign urgency. Non-response at Day 7 is normal; Day 10 is the first escalation signal. | No action at Day 7. Flag for Day 10 check. |
| Tier 1 (research organizations) — CBPP, ITEP, OpenSecrets | Research org reply cycles: 7-21 days. Non-response at Day 7 is early and expected. | No action. |

**Pattern-level non-response flag**: If ZERO replies are received from ALL contacts across BOTH domains by Day 7, and all sends are confirmed delivered (no bounce), this is a message-mismatch or timing signal — not a catastrophic failure. Trigger Section 7.3 Diagnostic.

**Current non-response log (fill at Day 7 checkpoint)**:

| Contact | Domain | Send Confirmed | Days Since Send | Reply Status | Pattern Flag |
|---------|--------|---|---|---|---|
| AFL-CIO | D59 | [ ] YES | _____ | [ ] No reply / [ ] Reply (score ___) | [ ] Normal / [ ] Flag |
| CBPP | D59 | [ ] YES | _____ | [ ] No reply / [ ] Reply (score ___) | [ ] Normal / [ ] Flag |
| NWLC | D59 | [ ] YES | _____ | [ ] No reply / [ ] Reply (score ___) | [ ] Normal / [ ] Flag |
| MomsRising | D59 | [ ] YES | _____ | [ ] No reply / [ ] Reply (score ___) | [ ] Normal / [ ] Flag |
| ITEP | D59 | [ ] YES | _____ | [ ] No reply / [ ] Reply (score ___) | [ ] Normal / [ ] Flag |
| CLC | D51 | [ ] YES | _____ | [ ] No reply / [ ] Reply (score ___) | [ ] Normal / [ ] Flag |
| Issue One | D51 | [ ] YES | _____ | [ ] No reply / [ ] Reply (score ___) | [ ] Normal / [ ] Flag |
| Common Cause CA | D51 | [ ] YES | _____ | [ ] No reply / [ ] Reply (score ___) | [ ] Normal / [ ] Flag |
| LWV CA | D51 | [ ] YES | _____ | [ ] No reply / [ ] Reply (score ___) | [ ] Normal / [ ] Flag |
| Clean Money Action Fund | D51 | [ ] YES | _____ | [ ] No reply / [ ] Reply (score ___) | [ ] Normal / [ ] Flag |

---

## Section 5: Success Probability Forecasting — Phase 2 Domain Paths

*Based on Day 7 data, estimate activation probability for each Phase 2 path. These are analytical estimates, not hard gates — the routing decision uses the thresholds in DAY_7_CHECKPOINT_ROUTING_DECISION_TREE.md.*

### 5.1 Domain 59 (Economic Precarity / CTC) — Activation Probability

**External deadline urgency**: Senate Finance CTC markup window June 25-30, 2026. Hard deadline. Legislative advocacy window cannot be recovered once markup closes.

| Engagement Signal | Weight | Score (fill at Day 7) | Weighted Contribution |
|---|---|---|---|
| 1+ Score 3+ reply from Domain 59 Wave 1 contacts | 40% | [ ] YES=1.0 / [ ] NO=0.0 | ______ |
| Senate Finance markup still active (confirmed at finance.senate.gov) | 30% | [ ] YES=1.0 / [ ] PASSED=0.5 / [ ] STALLED=0.7 | ______ |
| Domain 59 Gist URL live (HTTP 200) | 15% | [ ] YES=1.0 / [ ] NO=0.0 | ______ |
| No hard bounces from Tier 1 contacts (AFL-CIO, CBPP, NWLC) | 15% | [ ] YES=1.0 / [ ] 1 BOUNCE=0.5 / [ ] 2+ BOUNCES=0.0 | ______ |
| **Domain 59 Activation Probability** | 100% | | **______%** |

**Interpretation**:
- 75-100%: Activate Domain 59 immediately. Express Senate path runs same day as checkpoint.
- 50-74%: Activate with contingency monitoring. Express path runs; Day 14 assessment determines Tier 2.
- Below 50%: Diagnose before activating. Check Gist, bounce status, and Senate Finance window before proceeding.

**Note**: Domain 59 activation is largely independent of engagement signal because of the external legislative deadline. Even with 0 replies, if the Senate Finance markup is still active, the express path should execute — the advocacy value exists regardless of prior outreach signal.

---

### 5.2 Domain 51 (Campaign Finance / Dark Money) — Activation Probability

**External deadline urgency**: California Fair Elections Act messaging window locks July 1, 2026. FEC enforcement quorum remains absent (200+ days). Montana I-194 county submission deadline June 19.

| Engagement Signal | Weight | Score (fill at Day 7) | Weighted Contribution |
|---|---|---|---|
| 1+ Score 3+ reply from Domain 51 Wave 1-2 contacts | 35% | [ ] YES=1.0 / [ ] NO=0.0 | ______ |
| California Fair Elections Act still on ballot (confirmed at ballotpedia.org) | 25% | [ ] YES=1.0 / [ ] REMOVED=0.3 | ______ |
| Domain 51 Gist URL live (HTTP 200) | 15% | [ ] YES=1.0 / [ ] NO=0.0 | ______ |
| No hard bounces from Wave 1 Tier 1 contacts (CLC, Issue One) | 15% | [ ] YES=1.0 / [ ] 1 BOUNCE=0.5 | ______ |
| At least 1 Domain 51 Gist click confirmed (view count delta >0) | 10% | [ ] YES=1.0 / [ ] NO=0.0 | ______ |
| **Domain 51 Activation Probability** | 100% | | **______%** |

**Interpretation**:
- 75-100%: Activate Domain 51 Tier 1 expansion on Day 1 (day after Domain 59 express path). Per DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md, Day 1 targets: OpenSecrets, Democracy 21, Public Citizen.
- 50-74%: Activate with reduced scope. Tier 1 expansion sends proceed; skip Tier B state contacts until Day 10 signal assessment.
- Below 50%: Hold Tier 1 expansion pending Gist verification and delivery diagnostic.

---

### 5.3 Cross-Domain Integration Path — Probability

| Engagement Signal | Weight | Score | Weighted Contribution |
|---|---|---|---|
| At least 1 reply from each domain (separate contacts) | 50% | [ ] BOTH=1.0 / [ ] ONE=0.5 / [ ] NEITHER=0.0 | ______ |
| At least 1 organization in both contact pools confirmed delivered | 30% | [ ] YES=1.0 / [ ] PARTIAL=0.5 / [ ] NO=0.0 | ______ |
| Any cross-domain multiplier event logged in Section 3.2 | 20% | [ ] YES=1.0 / [ ] NO=0.0 | ______ |
| **Cross-Domain Integration Probability** | 100% | | **______%** |

**Interpretation**: Cross-domain integration (the combined FEC-enforcement/CTC-gap argument from DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md Section 4) requires both domains to be in active distribution. Probability above 60% warrants drafting the integration synthesis note. Template available in Section 4.1 of that document.

---

## Section 6: Contingency Triggers

*Pre-defined engagement patterns that require immediate routing changes, independent of the Day 7 decision tree. These triggers fire automatically — they do not require assessment.*

### Trigger 1 — Outright Failure: Zero delivery, zero clicks, zero replies

**Condition**: By Day 7, ALL of the following are true: (a) 2 or more sends have hard bounced, AND (b) zero Gist view delta across both domains, AND (c) zero replies of any score.

**Immediate action**:
1. Do not activate Tier 1 expansion for either domain.
2. Run Section 7.1 Delivery Diagnostic (infrastructure check: test send to self, Gist URL verification, spam folder check).
3. If infrastructure confirms all sends delivered, proceed to `DAY_7_CHECKPOINT_ROUTING_DECISION_TREE.md` WEAK branch — the outreach is reaching passive readers, not generating active replies.

**This trigger does NOT suspend Phase 2 planning.** It defers Tier 1 expansion by 7 days and routes to the diagnostic path. Both domains retain their production-ready status.

---

### Trigger 2 — Senate Finance Window Closes Before Domain 59 Activation

**Condition**: OBBBA passes full Senate floor vote before Domain 59 express path executes.

**Immediate action**:
1. Switch ALL Domain 59 unsent templates to "2027 Reform Coalition" frame per `DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` Part 7, Contingency 1.
2. Do not cancel sends. The contact list is unchanged; only the framing evolves.
3. This trigger does not affect Domain 51 in any way.

---

### Trigger 3 — List Fatigue Signal

**Condition**: 2 or more opt-out or explicit "no further contact" responses are received from the same domain's contact pool.

**Interpretation**: Phase 2 Wave 1-2 contacts were specifically chosen for relevance alignment. 2+ opt-outs from a 5-10 contact pool (20%+ opt-out rate) is a message-mismatch signal — the framing is wrong for that population, not the research.

**Immediate action**:
1. Halt remaining sends to that domain's contact pool pending framing review.
2. Re-examine subject line and opening paragraph of sent templates against the organizational mission of the opt-out contact.
3. Do not activate Tier 2 contacts for that domain until framing is revised.

**Note**: This trigger applies domain-specifically. If 2 Domain 51 contacts opt out, it does not affect Domain 59 distribution. Each domain's contact pool is assessed independently.

---

### Trigger 4 — Strong Early Signal (Accelerate)

**Condition**: By Day 5 (before formal Day 7 checkpoint), Score 4-5 replies received from 2 or more contacts across both domains.

**Immediate action**: Accelerate the Day 7 checkpoint to Day 5. Execute the routing decision tree now. The sequencing timing guide (DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md) still applies, but the stagger can compress from 24-48 hours to same-day.

**CBPP specific**: A CBPP reply about Senate Finance testimony is a Score 5 event that triggers same-day Domain 59 Tier 2 activation without waiting for the formal Day 7 checkpoint.

---

## Section 7: Diagnostic Procedures

### 7.1 Delivery Diagnostic (Run if bounce rate >10% or zero delivery confirmation)

1. Send a test email to yourself from the same email client and account used for wave sends. Confirm receipt within 5 minutes.
2. Load Domain 59 Gist: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba — confirm HTTP 200.
3. Load Domain 51 Gist: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 — confirm HTTP 200.
4. Check spam folder for any bounce notifications that were auto-classified.
5. Check `domain-59-send-log-june1.md` for any June 1-6 sends that may already have seeded the contact pool (duplicate send risk).

Estimated time: 5 minutes. If all five checks pass, infrastructure is functioning. Proceed with confidence to the routing decision.

---

### 7.2 Message-Mismatch Diagnostic (Run if 0 replies from a specific constituency by Day 14)

1. Re-read the opening paragraph of the sent email template against the organizational mission of the non-responding contact.
2. Check whether the Senate Finance/CTC framing (Domain 59) is still current — markup status may have changed.
3. Check whether the California ballot framing (Domain 51) is still current — ballot status may have changed.
4. If framing is stale: update template and re-send to any unsent contacts using updated framing. Do not re-send to contacts who have already received the stale version — instead, send a brief follow-up note updating the legislative status.

Estimated time: 10 minutes.

---

### 7.3 Systemic Zero-Engagement Diagnostic

*Run only if: all sends confirmed delivered, zero bounces, zero replies, zero Gist clicks after 7 days.*

This is the 95th-percentile worst case. The research is reaching passive readers who have not yet engaged. This is not a failure of the research; it is a cold-contact response-rate reality.

**At Day 14 with confirmed delivery and 0 replies**: Submit both domains to publication channels simultaneously. This converts the distribution investment to public record and generates inbound discovery:
- Just Security (justsecurity.org) — appropriate for Domain 51 FEC enforcement collapse
- Lawfare (lawfaremedia.org) — appropriate for constitutional dimensions of Domain 51
- Election Law Blog (electionlawblog.org, Rick Hasen) — appropriate for Domain 51 ballot campaign analysis
- Economic Policy Institute blog — appropriate for Domain 59 CTC refundability analysis

Publication converts a failed cold-contact distribution into an open-web citation that may reach the same organizations through organic discovery rather than email outreach.

---

## Section 8: Summary Scoring — Feed to Routing Decision Tree

*Complete at Day 7 checkpoint, 17:00 UTC June 17. Transfer scores directly to DAY_7_CHECKPOINT_ROUTING_DECISION_TREE.md Section 1 for routing.*

### Composite Engagement Score

| Component | Weight | Your Value | Weighted Score |
|---|---|---|---|
| Total Score 3+ replies across both domains | 40% | _____ replies | Fill in decision tree |
| Any Score 4-5 reply (yes/no) | 25% | [ ] YES / [ ] NO | Fill in decision tree |
| Delivery rate (% of sends confirmed, no bounce) | 20% | ____% | Fill in decision tree |
| Gist click delta (any domain, any positive number) | 15% | _____ | Fill in decision tree |

**Transfer to Decision Tree**: Take total Score 3+ reply count and delivery rate to `DAY_7_CHECKPOINT_ROUTING_DECISION_TREE.md`. The reply count determines the STRONG / MODERATE / WEAK branch. The delivery rate determines whether the diagnostic path fires first.

### External Deadline Status (confirm at checkpoint)

| Deadline | Status | Impact on Routing |
|---|---|---|
| Senate Finance CTC markup (finance.senate.gov) | [ ] ACTIVE / [ ] BILL PASSED / [ ] STALLED | ACTIVE → Domain 59 express path today regardless of engagement branch |
| California Fair Elections Act ballot (ballotpedia.org) | [ ] ON BALLOT / [ ] REMOVED / [ ] CONFIRMED | ON BALLOT → Domain 51 Tier 1 expansion Day 1 |
| Montana I-194 (June 19 county deadline) | [ ] QUALIFIED / [ ] FAILED | QUALIFIED → include MT contact in Domain 51 state sends |

---

*Analysis template prepared June 14, 2026. No Wave 1-2 data required to use this template — all data fields are blank and filled at checkpoint. Routes directly to DAY_7_CHECKPOINT_ROUTING_DECISION_TREE.md for action dispatch.*
