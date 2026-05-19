---
title: "May 21 Synthesis Execution Framework"
created: 2026-05-19
execute_at: "May 21, 2026, 19:00 UTC"
complete_by: "May 21, 2026, 20:30 UTC"
status: PRE-BUILT — autonomous execution document; zero ambiguity required
scope: "Authoritative framework for May 21 synthesis; extends and consolidates may21-synthesis-execution-checklist.md"
audience: orchestrator — autonomous execution; user fills signal log before 19:00 UTC
companion_files:
  - post-wave-1-monitoring/may21-synthesis-execution-checklist.md
  - post-wave-1-monitoring/wave-1-signal-log-may18-21.md
  - post-wave-1-monitoring/phase-2-path-activation-summary.md
---

# May 21 Synthesis Execution Framework

*Autonomous execution document. User fills `post-wave-1-monitoring/wave-1-signal-log-may18-21.md` May 20 evening and May 21 morning. Orchestrator executes synthesis May 21 19:00–20:00 UTC. This framework specifies every decision, rule, branch path, and exception condition — execution requires no judgment calls beyond applying the rules below to the filled signal log data.*

---

## 1. Synthesis Process Overview

**What the orchestrator does, May 21 19:00–20:00 UTC, in this order**:

1. **Read signal log** (19:00–19:08 UTC): Open `post-wave-1-monitoring/wave-1-signal-log-may18-21.md`. Read all rows in the SIGNAL LOG TABLE, all three daily snapshot sections (May 19, 20, 21). Note total reply count, score of each reply, and Gist delta figures.

2. **Inbox check** (19:08 UTC, concurrent with or immediately after reading signal log): Confirm no replies have arrived since the last monitoring check that are not yet logged. If any unlogged replies exist, score them using the SIGNAL CATEGORY REFERENCE (Section 5 of the signal log) and add them to the signal log table before proceeding.

3. **Check Gist view counts** (19:10–19:12 UTC): Open each Gist URL in incognito browser. Record delta since H+0 (May 18, ~08:00 UTC). Add to the May 21 snapshot section of the signal log if not already filled. The four URLs are: main proposal (`gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261`), executive summary (`gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4`), Domain 37 (create before May 21 per PROJECTS.md standing note), litigation tracker (`gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0`).

4. **Assemble data** (19:12–19:20 UTC): Fill the contact response summary table (Section 2 of this document). Compute aggregate metrics. Confirm all five contacts have a row and all [FILL] fields are populated.

5. **Classify** (19:20–19:28 UTC): Apply the deterministic signal classification rules (Section 3 of this document). Stop at first match. Check Score 5 override first, then Quality Reply Points thresholds, then structural fallback.

6. **Select branch path** (19:28–19:32 UTC): From the classification, go directly to the corresponding branch path section (Section 4). Read the immediate action, May 22–26 milestones, and Phase 2 implications.

7. **Post CHECKIN.md entry** (19:32–20:00 UTC): Using the template in Section 7 of this document, fill all fields from live signal data and post under "Wave 1 Synthesis — May 21" in CHECKIN.md. Include the Domain 42 DEA deadline reminder. Post by 20:00 UTC.

8. **Update companion files** (20:00–20:30 UTC): Fill the May 21 synthesis snapshot section in `wave-1-signal-log-may18-21.md`, fill the May 21 row in the Update Log of `preliminary-signal-analysis-may18.md`.

**Total execution time**: 60–90 minutes from first read to CHECKIN.md post.

---

## 2. Signal Log Format Specification

**What the user must fill in `post-wave-1-monitoring/wave-1-signal-log-may18-21.md` before May 21 19:00 UTC**:

### Required fields in the SIGNAL LOG TABLE

For each response signal received (reply, OOO, bounce, notable Gist event), one row:

| Field | What to enter |
|-------|--------------|
| Date | YYYY-MM-DD format |
| UTC Time | HH:MM UTC at time of check |
| Contact | First and last name |
| Org | Organization name |
| Signal Type | REPLY, OOO AUTOREPLY, HARD BOUNCE, or GIST SPIKE |
| Score | 0 (no signal) through 5 (STRONG OVERRIDE); use scoring guide below |
| Category Indicator | STRONG / MODERATE / WEAK / ADMINISTRATIVE / TOO EARLY |
| Key Content | One sentence description of what the response said or what the signal was |
| Quality Points | 0 (Score 1–2), 1 (Score 3), 2 (Score 4), STOP/STRONG OVERRIDE (Score 5) |
| Notes | Any relevant context (forwarding signal, referral, delivery anomaly) |

**If no signals have been received**: Leave the signal table with the baseline row only. The May 21 snapshot section must still be filled.

### Required fields in the May 21 72-Hour Synthesis Snapshot section

| Field | What to enter |
|-------|--------------|
| Total sent | 5 (fixed) |
| Total hard bounces | Count of hard bounce notifications received |
| Effective send count | 5 minus hard bounces minus OOOs where return date is after May 21 |
| Total responses (any type) | Count of all reply signals including acknowledgment-only and OOO |
| Substantive responses (Score 3+) | Count of replies scored 3 or higher |
| Substantive response rate | (Score 3+ count / effective send count) x 100 |
| Total Gist delta | Sum of view count increases across all Gist URLs since H+0 (May 18 08:00 UTC) |
| OOO contacts with return date after May 21 | Count of contacts with auto-reply showing return after synthesis date |
| Score 4+ signals | Count of replies scored 4 or higher |
| Score 5 signals (STRONG OVERRIDE) | Count of citations, filings, formal collaboration offers |
| TOTAL QUALITY REPLY POINTS | Sum of quality points from all contact scores plus Gist bonus (total Gist delta divided by 5, capped at 1.0) |

### Scoring guide for replies

| Score | Description | Examples | Quality Points Awarded |
|-------|-------------|----------|----------------------|
| 0 | No signal at all | No reply, no OOO, no bounce | 0 |
| 1 | Delivery confirmed, no engagement | "Thanks, will read"; OOO autoreply | 0 |
| 2 | General positive, no domain specificity | "This is interesting"; "Glad to see this research" | 0 |
| 3 | Substantive engagement — domain-specific | Question about specific domain content; methodological critique; specific citation reference | 1 |
| 4 | Implementation or referral signal | Asks how to use in a filing; names a specific colleague or org to forward to; requests participation notice draft | 2 |
| 5 | Integration signal | Cites in published filing, brief, testimony, or public article; offers formal collaboration or institutional co-authorship; introduces to active case docket | STRONG OVERRIDE — stop, classify STRONG immediately |

### Gist view count check procedure

Open each Gist URL in an incognito (private) browser window. GitHub Gists do not display a public view counter visible to viewers — view counts are only visible to the Gist owner when logged in. If logged in as esca8peArtist, the view count is visible in the Gist settings. If not logged in, use the Gist's "Files changed" activity as a proxy, or rely on the email reply pattern for delivery confirmation. If the view count system is unavailable, record Gist delta as [not confirmed] and proceed — do not block classification on this single data point.

---

## 3. Signal Classification Rules

Classification is deterministic. Apply rules in this exact order. Stop at first match.

### Rule 1: Score 5 Override (check first — highest priority)

**Condition**: Any Batch 1 contact has cited the framework in a published work (filing, brief, testimony, article, tweet, public statement), OR has offered formal institutional collaboration (co-authorship offer, formal partnership proposal, introduction to an active case docket by name).

**If Rule 1 triggers**: Classify as STRONG immediately. Do not proceed to Rule 2 or Rule 3. Note which contact triggered the override and what the citation or collaboration was. Proceed directly to STRONG path (Section 4.1).

**Rule 1 examples**:
- Elias files a participation notice with DEA-1362 that cites the framework by name
- Weiser publishes a Brennan Center post that links to a Gist
- Goodman publishes a Just Security article that incorporates Domain 37 analysis
- Chenoweth references the research in a tweet, post, or public presentation
- Bassin introduces the framework to an active Protect Democracy litigation brief

---

### Rule 2: Quality Reply Points Classification (check after Rule 1)

Compute Total Quality Reply Points using:

**Total QRP = (Sum of quality points from all Score 3+ replies) + (min(total Gist delta / 5, 1.0))**

Examples:
- One Score 3 reply, Gist delta 8: QRP = 1 + 1.0 = 2.0
- One Score 4 reply, Gist delta 3: QRP = 2 + 0.6 = 2.6
- Zero replies, Gist delta 15: QRP = 0 + 1.0 = 1.0 (Gist bonus capped at 1.0)
- Zero replies, Gist delta 0: QRP = 0 + 0 = 0.0

| Total QRP | Response Rate | Classification |
|-----------|--------------|----------------|
| >= 2 | >= 40% (2+ of effective send count at Score 3+) | **STRONG** |
| >= 2 | < 40% (QRP driven by Gist bonus, not replies) | **MODERATE** |
| >= 1 | Any | **MODERATE** |
| < 1, and Gist delta > 10 with zero replies | Any | **MODERATE** (proxy signal) |
| 0, and Gist delta <= 5 | Any | Proceed to Rule 3 |

---

### Rule 3: Structural Fallback (check after Rules 1 and 2)

Used only when QRP is 0 and Gist delta is <= 5.

**Step 3a: Delivery check (mandatory before WEAK classification)**

Send a test email from the same sending account to your own email address. If the test email lands in your spam folder rather than inbox, the issue is sender reputation / delivery, not content. Classify as DELIVERY PROBLEM, not WEAK. Do not revise messaging until delivery is fixed.

| Condition | Classification |
|-----------|---------------|
| Zero replies, zero Gist delta, no bounces, delivery confirmed (inbox test passes) | **WEAK** |
| Zero replies, zero Gist delta, no bounces, test email lands in spam | **DELIVERY PROBLEM** (not WEAK) |
| Zero replies, zero Gist delta, no bounces, test email inconclusive | **TOO EARLY** — hold, do not classify until May 25 |

**Step 3b: Law school structural carve-out**

The TOO EARLY classification applies regardless of QRP score when the only contacts who have not replied are the law school contacts (Goodman, Chenoweth) and there are no negative signals (no WEAK indicators) from the policy org and active litigator contacts. Specifically:

- If Weiser and Bassin (think tanks) have not replied but are within their 5-day window (before May 23): Do not classify as Weak. These contacts have had fewer than the expected minimum days to respond.
- If Elias has not replied but is within his 7-day window (before May 25): Do not classify immigration legal aid constituency as Weak. Silence at 72h is within sector norm.
- If Goodman and Chenoweth have not replied: Classify these two as TOO EARLY unconditionally through May 25.

**If all five contacts are silent but no bounces have occurred and the delivery test passes**: Classify overall as **TOO EARLY**, not Weak. The May 25 gate resolves this classification with full data.

---

### Classification Summary Table

| Classification | Condition | Phase 2 Path |
|---------------|-----------|-------------|
| **STRONG** | Any Score 5 override, OR QRP >= 2 AND response rate >= 40% | June 15 parallel D57+D59 launch; user approval required before pre-production (Section 4.1) |
| **MODERATE** | QRP >= 1 (any Score 3+), OR Gist delta > 10 with zero replies | Standard Phase 2 timeline; D57 PRIMARY June 10, D59 SECONDARY July 1 (Section 4.2) |
| **WEAK** | QRP = 0, Gist delta <= 5, delivery confirmed | Phase 1 continuation; D39 June 1 non-negotiable; D57/D59 deferred; messaging audit required (Section 4.3) |
| **TOO EARLY** | Zero signals, no bounces, law school window not closed OR delivery inconclusive | Hold; continue monitoring; full classification at May 25 gate (Section 4.4) |
| **DELIVERY PROBLEM** | Zero signals, test email lands in spam | Fix sender reputation before any classification; do not revise content (Section 6.2) |

---

## 4. Synthesis Branch Paths

### 4.1 STRONG Path

**Triggering conditions**: Rule 1 override, OR QRP >= 2 with response rate >= 40%.

**Immediate action (May 21 20:30 UTC)**:

Post to CHECKIN.md under "Wave 1 Synthesis — May 21": "STRONG outcome — Phase 2 June 15 parallel launch. D57 + D59 pre-production pending user approval at May 25 gate. Tier 2 pre-contact list ready."

Do NOT begin D57/D59 pre-production research without user confirmation at May 25 gate. The user confirmation step is non-optional — it prevents domain work from beginning before the user has reviewed the pre-contact list and approved the accelerated timeline.

Immediately queue:
- D57 pre-production checklist: Confirm 21 source URLs live; outline constitutional asymmetry (Section 2) drafted by June 8; acquire Ikenberry ("Liberal Leviathan") for international order framing.
- D59 pre-production checklist: Confirm 22 source URLs live; read Domains 31 and 47 for Section 5 synthesis prep; acquire BLS gig economy data for economic precarity analysis.
- Tier 2 pre-contact list: Immigration legal aid and law schools first; unions Week 6; think tanks concurrent with research-in-progress access framing.

**May 22–26 milestones**:
- May 22: Confirm delivery of STRONG CHECKIN.md post. Do not begin research.
- May 23–24: User reviews and approves STRONG path at May 25 gate (or confirms by silence that STRONG path proceeds).
- May 25: Final classification gate. If law school contacts (Goodman, Chenoweth) have now replied, that confirms STRONG across all constituencies. If they have not replied, STRONG holds from the other constituencies — law school window extends to Day 14 (June 1) for this constituency.
- May 25–28: D57 pre-production begins (source confirmation only; no new writing).
- May 28: D57 Section 2 outline drafted. Domain 42 DEA deadline.

**Phase 2 implications**:
- STRONG path triggers Phase 2 acceleration across all domain sequences.
- Domain 57 launches June 15 parallel with Domain 59 — the most compressed timeline in the framework.
- Tier 2 activation begins June 15–21, covering all four constituencies.
- Social proof language for Tier 2 emails is available: "Distribution has produced substantive engagement from [constituency description]. We are expanding to [Tier 2 constituency] because [constituency-specific hook]." Do not name specific contacts without their explicit consent.

**Phase 2 domain sequence (STRONG path)**:
| Date | Action |
|------|--------|
| June 1 | Domain 39 pre-distribution — NON-NEGOTIABLE |
| May 28 | Domain 56 distribution — on schedule |
| June 15 | Domain 58 distribution |
| June 15 | Domain 57 LAUNCH (parallel) |
| June 15 | Domain 59 LAUNCH (parallel) |
| June 15–21 | Tier 2 pre-contact activation — all four constituencies |

---

### 4.2 MODERATE Path

**Triggering conditions**: QRP >= 1 (any single Score 3+), OR Gist delta > 10 with zero email replies.

**Immediate action (May 21 20:30 UTC)**:

Post to CHECKIN.md: "MODERATE outcome. Standard Phase 2 timeline. Monitoring continues to May 25 final gate. D57 PRIMARY research June 10."

No accelerated Tier 2 pre-contact. Standard Phase 2 timeline holds. Continue monitoring per signal log cadence May 22–24. If Gist delta is the driver of MODERATE (proxy signal, no email replies), note this in the CHECKIN.md post — it is a positive signal (internal sharing is occurring) but a different quality of signal than a direct reply.

**May 22–26 milestones**:
- May 22: Continue monitoring. Log any new signals in signal log.
- May 23: Weiser and Bassin STRONG threshold closes (Day 5). If either replies at Score 3+ by May 23, think tank constituency upgrades to STRONG — reclassify overall if this pushes QRP above STRONG threshold.
- May 24: Domain 42 DEA electronic filing deadline (11:59 p.m. ET). This is path-independent.
- May 25: Final classification gate. Law school contacts (Goodman, Chenoweth) have had 7 days. Elias has had 7 days. Run the full synthesis formula again with all available data. Confirm MODERATE path or upgrade to STRONG if additional signals arrived.
- May 25–28: D57 pre-production prep (source confirmation, outline structure).
- June 10: D57 PRIMARY research launch.

**Phase 2 implications**:
- MODERATE path does not trigger Phase 2 acceleration.
- D57 and D59 proceed on their standard timeline: D57 June 10 (one week earlier than WEAK but single domain), D59 July 1.
- Tier 2 pre-contact activation June 22–28, led by policy window urgency rather than social proof.
- Social proof framing in Tier 2 emails: "Distribution has produced initial engagement from [constituency type]. We are expanding to [Tier 2 constituency] because [policy window hook]." If zero Score 3+ replies exist (MODERATE driven by Gist delta only), do not claim social proof — lead with domain utility and policy window urgency.

**Phase 2 domain sequence (MODERATE path)**:
| Date | Action |
|------|--------|
| June 1 | Domain 39 pre-distribution — NON-NEGOTIABLE |
| May 28 | Domain 56 distribution — on schedule |
| June 15 | Domain 58 distribution |
| June 10 | Domain 57 PRIMARY research launch |
| July 1 | Domain 59 SECONDARY research launch |
| June 22–28 | Tier 2 pre-contact activation |

---

### 4.3 WEAK Path

**Triggering conditions**: QRP = 0, Gist delta <= 5, delivery self-test confirmed inbox delivery (not spam).

**Important**: Do not reach WEAK classification without completing the delivery self-test (Rule 3a). A WEAK classification that is actually a delivery problem wastes Phase 1 remediation resources and incorrectly diagnoses a technical issue as a content issue.

**Immediate action (May 21 20:30 UTC)**:

Post to CHECKIN.md: "WEAK outcome — delivery confirmed. Phase 1 continuation. Messaging audit required before Phase 2. User decision needed: delivery diagnosis vs. content revision. D39 June 1 non-negotiable."

Begin 8–12 hours/week remediation work alongside domain production. Remediation runs through June 1. Three-track diagnosis: (1) delivery audit (re-verify all five email addresses, check sender reputation), (2) messaging audit (is the ask too complex? is the framing too academic? is the subject line getting filtered?), (3) contact quality audit (are these the right Batch 1 contacts, or should Batch 2/3 be accelerated?).

Do NOT revise content until you know whether the problem is delivery or content. These are different interventions. Content revision wastes effort if the problem is delivery.

**May 22–26 milestones**:
- May 22: Begin delivery audit. Re-check all five email addresses against current organizational websites.
- May 23: Check whether Weiser, Bassin, or Elias have now replied (late-arriving signals after the 72h window can upgrade WEAK to MODERATE). If any Score 3+ reply arrives after May 21 synthesis, reclassify at May 25 gate.
- May 24: Domain 42 DEA electronic filing deadline — path-independent, execute regardless.
- May 25: Final classification gate. If law school contacts have now replied, remove them from the WEAK diagnosis (academic silence at 72h is structural, not content failure). Confirm or revise the WEAK classification with full data.
- June 1: Domain 39 pre-distribution — non-negotiable across all paths.

**Phase 2 implications**:
- WEAK path defers D57 and D59 research.
- Phase 1 remediation runs June 1–June 28.
- D38 (AI Regulatory Capture) and D40 (Surveillance Capitalism) begin in June as higher-relevance/lower-friction domains.
- D57 research begins August 1 (September 1 completion; 3-week UNGA lead time for UNGA 81 High-Level Week September 22–28).
- Tier 2 activation is contingent on D39 producing at least one positive engagement signal in its June distribution.

**Phase 2 domain sequence (WEAK path)**:
| Date | Action |
|------|--------|
| June 1 | Domain 39 pre-distribution — NON-NEGOTIABLE |
| May 28 | Domain 56 distribution — on schedule |
| June 15 | Domain 58 distribution |
| June 3 | Domain 38 pre-production begins |
| June 30 | Domain 38 distribution target |
| June 22 | Domain 40 production begins |
| July 15 | Domain 40 distribution target |
| August 1 | Domain 57 research start |
| July 15 | Domain 59 research start |
| June 29–July 5 | Tier 2 activation — contingent on D39 signal |

---

### 4.4 TOO EARLY Path

**Triggering conditions**: Zero replies from all contacts, zero Gist delta, no bounces at 72h — AND law school response window has not yet closed.

**Important structural note**: TOO EARLY is not a content failure classification. It is a timing classification. 2 of 5 Batch 1 contacts (Goodman, Chenoweth) have 5–10 day academic response cycles, and a third (Elias) has a 7-day sector norm. A zero-reply result at 72h for this cohort is structurally expected, not diagnostically negative.

**Immediate action (May 21 20:30 UTC)**:

Post to CHECKIN.md: "TOO EARLY at 72h — law school response window not yet closed. No path decision before May 25. Monitoring continues. Delivery confirmed [or: delivery inconclusive — running self-test]."

Do NOT begin Phase 1 remediation based on 72h silence. Do not reclassify to WEAK until May 25 with full data. Run the delivery self-test to confirm no spam-folding issue — this is the one action that is warranted immediately.

Continue monitoring May 22–24 per signal log cadence:
- May 23: Think tank window closes (Day 5 for Weiser/Bassin). Any Score 3+ reply by this date upgrades to MODERATE.
- May 25: Law school window reaches Day 7. Elias reaches Day 7. Run full synthesis formula. TOO EARLY resolves into STRONG, MODERATE, or WEAK at this gate — it cannot remain TOO EARLY past May 25.

**May 22–26 milestones**:
- May 22: Delivery self-test if not already run. Continue monitoring.
- May 23: Think tank first full classification window closes. If Weiser or Bassin reply at Score 3+, upgrade from TOO EARLY to MODERATE (or STRONG if both reply).
- May 24: Domain 42 DEA electronic filing deadline — path-independent.
- May 25: Full classification. All five contacts have had 7 days. The TOO EARLY classification must resolve here. Apply the full classification rules (Section 3) to all signals received through May 25.
- If still zero signals at May 25 with delivery confirmed: Reclassify as WEAK. Begin remediation. D39 June 1 non-negotiable.
- If law school contacts have replied at Score 3+: Reclassify to MODERATE or STRONG per QRP calculation.

**Phase 2 implications**: No Phase 2 domain sequence changes before May 25. Domain 39 June 1 distribution is non-negotiable and path-independent. Domain 56 May 28 distribution is on schedule regardless of classification. The TOO EARLY path is a holding pattern, not a divergent path — it resolves into one of the three active paths at May 25.

---

## 5. Per-Domain Phase 2 Implications Summary

| Domain | STRONG path | MODERATE path | WEAK path | TOO EARLY path (pending May 25) |
|--------|-------------|---------------|-----------|--------------------------------|
| Domain 39 | June 1 non-negotiable | June 1 non-negotiable | June 1 non-negotiable | June 1 non-negotiable |
| Domain 56 | May 28 on schedule | May 28 on schedule | May 28 on schedule | May 28 on schedule |
| Domain 57 | June 15 parallel launch (with D59) | June 10 primary launch | August 1 start | Pending May 25 resolution |
| Domain 58 | June 15 distribution | June 15 distribution | June 15 distribution | June 15 distribution |
| Domain 59 | June 15 parallel launch (with D57) | July 1 secondary launch | July 15 start | Pending May 25 resolution |
| Domain 38 | Standard timeline | Standard timeline | June 3 accelerated | Pending May 25 resolution |
| Domain 40 | Standard timeline | Standard timeline | June 22 accelerated | Pending May 25 resolution |
| Tier 2 activation | June 15–21 (all 4 constituencies) | June 22–28 | Contingent on D39 signal | Pending May 25 resolution |
| Domain 42 DEA | May 28 hard deadline — all paths | | | |

---

## 6. Exception Handling

### 6.1 Signal Log Is Incomplete

**Condition**: User has not filled the May 20 and/or May 21 pre-synthesis snapshot sections in `wave-1-signal-log-may18-21.md` before 19:00 UTC.

**Action**:
1. Do not delay synthesis execution past 20:00 UTC to wait for user-filled data.
2. Check the email inbox directly at synthesis time. Score any found replies immediately.
3. Check Gist view counts incognito at synthesis time.
4. If signal log table has no entries beyond the baseline row, this means either (a) no signals were received, or (b) signals were not logged. Treat this as zero-signal data for synthesis purposes, with a note in the CHECKIN.md post: "Signal log not fully filled before synthesis — classified on direct inbox check at synthesis time."
5. Classify based on the direct inbox check and Gist view check performed at 19:00 UTC. Do not postpone the CHECKIN.md post.
6. Flag in CHECKIN.md: "Signal log fill incomplete — user should verify signal log completeness after synthesis for accuracy."

### 6.2 Unexpected Positive Result (Strong Signal Before Expected Window)

**Condition**: A Score 4+ signal arrives before May 21 synthesis — for example, Elias replies on May 20 with a specific docket reference, or a Batch 1 contact publishes content citing the framework.

**Action**:
1. Log in the signal log immediately upon discovery.
2. Post in CHECKIN.md under "Needs Your Input": "PRELIMINARY STRONG SIGNAL — [contact], [org], Score [X]. [One sentence description]. 72h synthesis at May 21 19:00 UTC. Phase 2 STRONG path may activate pending user confirmation."
3. Do not begin D57/D59 pre-production before May 21 synthesis. The preliminary flag is for visibility only — path activation happens at synthesis.
4. At May 21 synthesis, the early strong signal is already logged. Classification runs normally and is likely STRONG. Execute the STRONG path per Section 4.1.

### 6.3 Hard Bounce on a Contact

**Condition**: One or more of the five Batch 1 emails hard-bounced (delivery failure notification received).

**Action**:
1. Remove the bounced contact from the denominator for all response-rate calculations.
2. Begin email re-verification immediately: check current organizational website for the contact's email address. If a new address is found, re-send with the same email text.
3. Note: If Chenoweth's email (erica_chenoweth@hks.harvard.edu — underscore format) bounced, re-check HKS faculty page for current format before resending.
4. For synthesis classification: use the adjusted denominator (4 contacts instead of 5 if one bounced) for response-rate calculations. A 40% response rate with 4 contacts requires 1.6 replies — round up to 2 replies required for STRONG threshold.
5. A hard bounce does not by itself downgrade classification. It adjusts the denominator.

### 6.4 Score 5 Signal Appears During May 22–25 Extended Window

**Condition**: After the May 21 synthesis, a contact cites the framework in a published filing, brief, or article, or offers formal institutional collaboration.

**Action**:
1. Log in signal log immediately.
2. Post in CHECKIN.md immediately: "STRONG OVERRIDE POST-SYNTHESIS — [contact], [org]. [One sentence]. Upgrading May 21 classification to STRONG regardless of prior classification. Phase 2 STRONG path activates. D57/D59 pre-production pending user confirmation at May 25 gate."
3. Proceed to STRONG path per Section 4.1. The user gate at May 25 applies.

### 6.5 Two or More Contacts Reply with Contradictory Quality Signals

**Condition**: One contact replies at Score 3 and another at Score 1 (acknowledgment only).

**Action**: The Score 3 contact generates 1 Quality Reply Point. The Score 1 contact generates 0 Quality Reply Points. Total QRP is 1. Classification is MODERATE. The contradictory quality signals do not cancel out — only Score 3+ signals contribute Quality Reply Points. The Score 1 acknowledgment is logged as delivery confirmation but does not affect the classification arithmetic.

### 6.6 Gist View Counts Are Unavailable

**Condition**: The Gist view count interface is inaccessible, the Gist has been deleted or privatized, or the view count cannot be confirmed at synthesis time.

**Action**: Treat Gist delta as 0 for classification purposes. Do not block classification on this single data point. Note in CHECKIN.md post: "Gist view count not available at synthesis — classification based on email signals only." If email signals alone classify as STRONG or MODERATE, that classification holds.

---

## 7. Success Criteria

**How to know if the synthesis was executed correctly**:

After the synthesis (May 21 20:30 UTC), verify all of the following:

- [ ] All 5 Batch 1 contacts have a row in the contact response summary (even if Score 0)
- [ ] Aggregate metrics table is complete — no [FILL] fields remaining in the May 21 snapshot
- [ ] Exactly one of STRONG/MODERATE/WEAK/TOO EARLY is checked as the classification
- [ ] The CHECKIN.md post is present under "Wave 1 Synthesis — May 21" with all template fields filled
- [ ] The selected path is written in the CHECKIN.md post with the correct May 22–26 milestones
- [ ] The Domain 42 DEA deadline reminder is included in the CHECKIN.md post
- [ ] The May 25 final classification gate is explicitly noted in the CHECKIN.md post
- [ ] `wave-1-signal-log-may18-21.md` May 21 synthesis snapshot section is filled
- [ ] `preliminary-signal-analysis-may18.md` Update Log May 21 row is filled

**Indicators that synthesis was NOT executed correctly**:
- CHECKIN.md post is absent
- More than one classification is checked
- The WEAK classification was assigned without a delivery self-test
- The TOO EARLY classification was assigned without noting the May 25 resolution gate
- Domain 42 DEA deadline reminder is missing from the CHECKIN.md post

---

## 8. CHECKIN.md Post Template

Copy this template exactly. Fill all [FILL] fields from live signal data. Post under "Wave 1 Synthesis — May 21" in CHECKIN.md before 20:00 UTC.

```
## Wave 1 Synthesis — May 21, 20:00 UTC

**Classification**: [STRONG / MODERATE / WEAK / TOO EARLY]
**Total Quality Reply Points**: [X]
**Substantive response rate**: [X]% ([X] of [adjusted send count] contacts at Score 3+)
**Gist delta**: [X] views since H+0 (May 18 ~08:00 UTC)

**Per-contact status**:
- Weiser (Brennan Center): [REPLIED Score X / SILENT / OOO until DATE / BOUNCED]
- Elias (Democracy Docket): [REPLIED Score X / SILENT / OOO until DATE / BOUNCED]
- Goodman (Just Security): [REPLIED Score X / SILENT — TOO EARLY academic cycle / BOUNCED]
- Chenoweth (Harvard Kennedy): [REPLIED Score X / SILENT — TOO EARLY academic cycle / BOUNCED]
- Bassin (Protect Democracy): [REPLIED Score X / SILENT / OOO until DATE / BOUNCED]

**Strongest signal**: [Contact name, Org, Score X — one sentence description] OR [No substantive signals at 72h]
**Law school constituency**: TOO EARLY — 5–10 day academic cycle; classify at May 25
**Think tank constituency (Weiser, Bassin)**: [STRONG / MODERATE / WEAK / MONITORING]
**Immigration legal constituency (Elias)**: [STRONG / MODERATE / WEAK / MONITORING]

**Selected path**: [A: STRONG / B: MODERATE / C: WEAK / D: TOO EARLY]
**Immediate next action**: [one sentence]
**May 22–26 milestones**: [summary from the path section]

**May 25 final gate**: [what to classify / what to check — e.g., "Law school window closes Day 7. Weiser/Bassin STRONG threshold closes Day 5. Elias Day 7 Weak threshold. Run full synthesis formula with all available data."]

**Domain 42 DEA deadline**: May 28 — [X] days remaining. Electronic filing deadline May 24, 11:59 p.m. ET. Check BATCH_1_CONTACT_LOG.md Domain 42 section for send status.

[IF STRONG] **User approval required**: STRONG path activates D57 + D59 pre-production June 15. Confirm at May 25 gate before any pre-production work begins.
[IF WEAK] **User decision required**: WEAK classification confirmed with delivery verified. Determine: delivery problem or content problem? Remediation protocol at PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 4.4.
[IF DELIVERY PROBLEM] **Urgent**: Test email landed in spam. Fix sender reputation before any further sends. Do not revise content. Check domain/IP reputation tools.
```

---

## 9. Rollback and Escalation

**When synthesis requires user intervention (do not proceed autonomously)**:

1. **STRONG path activation**: Phase 2 D57 + D59 pre-production requires explicit user confirmation before research begins. Post the STRONG outcome in CHECKIN.md, queue the pre-production checklist, and wait for user confirmation at the May 25 gate. Do not begin writing or research for D57 or D59 without this confirmation.

2. **WEAK path with content diagnosis**: Determining whether a WEAK outcome is caused by delivery or content requires user decision. The orchestrator can confirm delivery via self-test, but content revision strategy (is it the framing, the length, the ask, the contact selection?) requires the user's judgment about what they want the outreach to accomplish. Flag explicitly in CHECKIN.md: "Delivery confirmed. User decision required: delivery problem or content problem."

3. **Score 5 override with an active filing**: If a contact has cited the framework in a live court filing or legal brief, the user needs to know immediately — this may require a response to the contact (to offer additional research support, to provide correct citation information, or to coordinate on a Phase 2 partnership). Post in CHECKIN.md under "Needs Your Input — URGENT."

4. **Hard bounce on Elias specifically**: Elias is the highest-probability STRONG signal contact. If his email hard-bounced, the user needs to know before May 25 — a re-send to the correct address with the same content could still produce a STRONG signal within the law school/academic extension window. Flag immediately.

5. **Signal log reveals a reply that the user sent without logging**: If the inbox check at synthesis reveals a reply that the user sent a response to but did not log, log it retroactively in the signal log and include it in the synthesis. Do not omit it.

**Self-correction protocol if synthesis classification is later found to be wrong**:

If the user informs the orchestrator after synthesis that a reply was received before the synthesis but not logged (e.g., it went to a secondary inbox), reclassify at that point using the full signal data. If the reclassification changes the path (e.g., from TOO EARLY to MODERATE), post an update in CHECKIN.md under "Wave 1 Synthesis — Correction" with the revised classification and updated path actions. Do not re-run the CHECKIN.md template from scratch — append the correction to the original post.

---

*Created: May 19, 2026. Execute at: May 21, 19:00–20:00 UTC. Post CHECKIN.md by 20:00 UTC.*
*This document is authoritative for May 21 synthesis. The companion execution checklist at `post-wave-1-monitoring/may21-synthesis-execution-checklist.md` contains the same step sequence in a shorter format. If these two documents conflict, this framework takes precedence.*
*Domain 42 DEA deadline is path-independent. May 28 is the hard cutoff. Electronic deadline May 24, 11:59 p.m. ET. Execute regardless of synthesis classification.*
