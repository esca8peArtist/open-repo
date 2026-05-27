---
title: "Phase 1 Post-Distribution Measurement System"
created: 2026-05-27
version: 1.0
status: production-ready
scope: >
  Comprehensive measurement system for Phase 1 distribution (May 28 – June 4 window).
  Covers adoption scale, constituency-specific success signals, Day 7/14/30/60 numeric
  thresholds, solo operator overhead, and escalation triggers.
word_count: ~2400
companion_files:
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md
  - PHASE_1_DECISION_TREES.md
  - PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md
  - PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md
---

# Phase 1 Post-Distribution Measurement System

**Version 1.0 — May 27, 2026**

**Lead finding**: Most distribution efforts fail not because the materials are weak but because there is no agreed definition of what "working" looks like. This document provides that definition: five adoption levels with explicit false-positive exclusions, numeric thresholds per constituency at four checkpoints, a realistic overhead estimate for a solo operator, and specific escalation triggers that distinguish "needs more time" from "needs a different approach." All thresholds build on PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md without contradiction.

---

## 1. Why Measurement Matters for Phase 2 Go/No-Go

Phase 2 is not calendar-gated. It is signal-gated. Domain 56 distribution began May 28; Domain 39 sends June 1. Whether Tier 2 expansion follows on the May 28 timeline or waits until the Day 30 or Day 60 checkpoint depends entirely on what the measurement system detects.

The specific Phase 2 decisions that measurement will answer:

- **Tier 2 activation timing**: Social proof from Phase 1 Tier 1 contacts accelerates Tier 2 adoption. If three or more Score 3+ replies arrive by Day 14, Tier 2 outreach letters can cite real endorsements. If replies are sparse, Tier 2 outreach must be framed on the strength of the framework alone — a harder sell.
- **Domain prioritization**: If immigration legal aid engagement is high and labor union engagement is zero at Day 14, Domain 29 follow-up materials should be deployed before Domain 17. The measurement system tells you where to invest the next hour.
- **Failure recovery trigger timing**: A framework extended without modification will produce the same result as the original send. Measurement answers the question: modify now, or wait for more signal? Waiting past Day 30 without evidence to justify the wait is drift, not patience.
- **Phase 2 scope**: The Day 60 target is 15 confirmed organizational adoptions and 100 people reached. Without a measurement system, those numbers are aspirations. With one, they are checkpoints with pre-planned responses.

The measurement system is the difference between Phase 2 launching with evidence and Phase 2 launching on hope.

---

## 2. Five-Level Adoption Scale (False-Positive Prevention Built In)

The central failure mode in measuring distribution is inflating the signal: counting Gist views as readership, counting readership as adoption, counting one person's enthusiasm as organizational commitment. This scale is designed to prevent all three.

**Level 0 — No Engagement**
Definition: Email delivered (not bounced), no Bitly clicks, no reply of any kind within 14 days.
False-positive risk: None. This is the null signal.
Measurement: Bitly click count = 0, Gmail reply thread empty.
Note: Level 0 at Day 14 does not mean permanent non-engagement. A Level 0 contact may surface at Day 45 or Day 90. It means "no signal yet" and triggers the re-contact sequence in Section 6.

**Level 1 — Acknowledged Receipt**
Definition: A reply was received that acknowledges the email without any substantive content. This includes: "Thank you, I'll look at this when I have time," out-of-office auto-replies where no human follow-up occurred, and form acknowledgments from organizational inboxes.
False-positive exclusion: Level 1 does NOT count toward Phase 2 go/no-go thresholds. It confirms delivery and that a human saw the subject line. That is its only value.
Measurement: Gmail reply score 1 or 2. Bitly clicks may or may not be present — a polite non-reader can reply without clicking.

**Level 2 — Active Read**
Definition: Evidence that the recipient read at least one Gist document. Measurement: Bitly click on a Gist link combined with either (a) any reply showing familiarity with framework content, or (b) a click count that implies sustained reading time (three or more clicks across different Gists for one recipient, if linkable by referrer data).
False-positive exclusion: A single Bitly click does not confirm reading — it confirms the link was opened. A single click with no reply scores as Level 2 only if the click occurred on a Gist with substantial content (the main proposal or a domain-specific document), not on a landing page or short summary.
Why this matters: Bitly reports raw clicks. A spam scanner may click a link. A 2-second preview does not equal reading a 40-page domain document. Level 2 requires a behavioral signal that implies engagement, not just delivery.

**Level 3 — Substantive Engagement**
Definition: A reply that demonstrates the recipient read and processed specific content. Markers: reference to a specific domain by name or concept, a question about methodology or sourcing, a statement that they forwarded to a colleague, a request for additional materials, or any statement that uses framework vocabulary in their own words (not just quoting back a phrase from the email).
Measurement: Gmail reply score 3 or 4.
This is the minimum threshold that counts toward Phase 2 go/no-go decisions. Only Level 3+ signals from Tier 1 contacts should be included in the reply rate calculations in the constituency dashboard.
False-positive exclusion: Flattery without substance ("this is impressive work!") is Level 2, not Level 3. The test is: does this reply tell you anything about what the person plans to do with the material?

**Level 4 — Organizational Intent**
Definition: Explicit statement of intent to use Phase 1 materials in organizational work, OR confirmed forwarding to an organizational decision-maker with a use-case in mind. Examples: "We're going to discuss this in our next clinic faculty meeting," "I'm forwarding this to our litigation director for our amicus brief project," "I want to include this in our member education module for the fall training cycle."
Measurement: Gmail reply score 4. Record in Adoption Signal Registry as "Probable" adoption (Verification_Status = Probable until confirmed).
Note: Level 4 is an intent signal, not a confirmed adoption. The conversion from Level 4 to Level 5 is the measurement challenge for the Day 30-60 window.

**Level 5 — Confirmed Adoption**
Definition: Documented evidence that the organization has incorporated Phase 1 materials into an operational artifact: a curriculum, a litigation brief, a policy document, a training module, a governance document, a published paper, or a web-accessible citation. Evidence must come from a source external to the initial outreach email — a survey response, a web detection, a PACER filing, a published document, or a direct confirmation call.
False-positive exclusion: A Level 4 intent statement, even a strong one, does not become Level 5 without external confirmation. Verbal statements in emails count as Level 4. The adoption must leave a traceable artifact outside the email thread.
Measurement: Gmail reply score 5, OR web-detected citation, OR Adoption Signal Registry entry with Verification_Status = Confirmed.

---

## 3. Constituency-Specific Success Signals

Phase 1 materials traveled to seven different organizational cultures. The signal that means "this is working" is different in each. Applying a uniform threshold across all seven would produce false confidence in some and false pessimism in others.

**Law Schools** — The adoption path runs through curriculum and scholarship, not policy documents. Level 3 success signal: "I'm sharing this with my election law seminar" or "I want to include your Domain 6 analysis in my judicial independence course readings." Level 5 success signal: a published working paper from a Tier 1 faculty member that cites the framework, or a course syllabus update confirmed by web search. Latency: Level 5 may take 60-90 days even for a highly engaged faculty member because of publication and course cycle timelines. Do not penalize law schools for slow Level 5 progression — Level 3 and Level 4 are the leading indicators.

**Immigration Legal Aid** — The adoption path runs through litigation documents: model briefs, amicus frameworks, client advisories. Level 3 success signal: specific interest in Domain 29 model brief language, or a reference to a pending case where the framework is relevant. Level 5 success signal: a PACER docket entry or a published advisory that uses framework vocabulary. Latency: Level 5 can occur within 30 days if there is active litigation. This is the constituency where early adoption is most plausible in the May 28 – June 28 window.

**Civil Rights Organizations** — The adoption path runs through policy documents and public advocacy. Level 3 success signal: forwarding to a policy director, or reference to an upcoming publication or campaign where the framework is relevant. Level 5 success signal: framework vocabulary in a published brief, press statement, annual report, or public policy document from the organization. Latency: 30-60 days for a policy brief; longer for annual reports.

**Academic Research** — The adoption path runs through scholarly infrastructure: SSRN downloads, conference presentations, syllabi, grant proposals. Level 3 success signal: any reply showing intellectual engagement with methodology or analytical framework. Level 5 success signal: SSRN alert, Google Scholar entry, or course listing update. Latency: Academic adoption cycles are the longest. Level 3 by Day 30 is the target; Level 5 may take 90-180 days. Do not use Day 60 Level 5 count to assess academic constituency performance.

**Faith Coalitions** — The adoption path runs through congregational communication: sermon guides, pastoral letters, discussion guides, faith-based policy statements. Level 3 success signal: request for a version adapted for congregational use, or reference to a specific sermon or adult education series. Level 5 success signal: a published sermon guide, faith-based newsletter, or denominational policy statement citing framework materials. Latency: Faith adoption is often faster than academic adoption because publication cycles are internal. Level 5 within 30-60 days is plausible.

**Labor Unions** — The adoption path runs through member education: training modules, contract negotiation briefs, union officer education programs. Level 3 success signal: request for a simplified member-facing version, or reference to an upcoming training cycle. Level 5 success signal: a union local education bulletin, training curriculum update, or member advisory citing framework materials. Latency: Union adoption speed varies by whether training cycles are already scheduled. If a training cycle is upcoming, Level 5 can appear within 30 days. If not, 60-90 days.

**Mutual Aid Networks** — The adoption path runs through governance documents and network communications: protocol guides, trainer certification materials, network newsletters. Level 3 success signal: any reply from a network coordinator (not just a national umbrella contact), or reference to a specific local network use case. Level 5 success signal: a network governance document, trainer guide, or network newsletter citing framework vocabulary. Latency: Mutual aid networks are often the fastest adopters at the local level but the slowest at producing documented artifacts. Level 4 intent signals from local coordinators are the highest-value leading indicator for this constituency.

---

## 4. Day 7/14/30/60 Checkpoint Definitions with Numeric Thresholds

Checkpoint definitions expand on PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 4 and PHASE_1_DECISION_TREES.md. They do not contradict those documents; they add the Day 14 checkpoint (not previously specified) and clarify constituency-level pass/fail criteria.

### Day 7 Checkpoint (June 4, 2026)

**Purpose**: Confirm that emails were delivered and opened by at least a minimum sample. Not a performance assessment — a delivery confirmation.

**System-level pass (HOLD)**: Total Bitly clicks across all tracked links >= 15, AND at least 2 replies at any score level, AND fewer than 3 bounces.
**System-level monitor**: Bitly clicks 5-14 AND at least 1 reply. Check again at Day 10-12.
**System-level escalate**: Bitly clicks < 5 with confirmed delivery, OR 3+ bounces. Run delivery diagnostic immediately.

**Constituency-level minimums (Day 7)**:
| Constituency | Minimum signal |
|---|---|
| Law Schools | >= 2 Bitly clicks attributable to law school outreach |
| Immigration Legal Aid | >= 1 click or reply |
| Civil Rights | >= 1 click or reply |
| Academic | >= 1 reply at any score |
| Faith | >= 1 click |
| Labor | >= 1 click |
| Mutual Aid | >= 1 click |

A constituency with zero signal at Day 7 is flagged MONITOR for that constituency specifically — not system-level ESCALATE unless three or more constituencies show zero signal simultaneously.

### Day 14 Checkpoint (June 11, 2026)

**Purpose**: First quality-of-engagement check. By Day 14, email reply timing patterns are established. Recipients who will engage at Level 3+ typically do so within 10 days of receiving a well-targeted email.

**System-level thresholds**:
- On track: >= 3 Level 3+ replies across any constituencies
- Monitor: 1-2 Level 3+ replies — re-evaluate at Day 21
- Below baseline: Zero Level 3+ replies at Day 14 with confirmed delivery — apply framing revision now (do not wait until Day 30)

**Constituency-level Day 14 targets**:
| Constituency | Day 14 Target | Below-target action |
|---|---|---|
| Law Schools | >= 1 Level 3+ reply | Re-contact via clinic administrator pathway |
| Immigration Legal Aid | >= 1 Level 3+ reply | Shift framing to Domain 29 model brief offer specifically |
| Civil Rights | >= 1 Level 3+ reply | Shift to state-level ACLU chapters |
| Academic | >= 1 reply at any level | Academic cycles are slower — monitor |
| Faith | >= 1 Level 3 reply OR 3 Level 2 replies | Re-frame around Domains 39 or 22 |
| Labor | >= 1 Level 3 reply | Offer simplified member brief as entry point |
| Mutual Aid | >= 1 reply from a local coordinator | Shift from national umbrella to local network contacts |

Day 14 is the last low-cost intervention point before the Day 30 checkpoint. Changes made at Day 14 (framing revision, contact substitution, channel shift) have enough time to produce replies before Day 30.

### Day 30 Checkpoint (June 27, 2026)

**Purpose**: Phase 2 sequencing decision. The four-number pull from PHASE_1_DECISION_TREES.md drives the STRONG/MODERATE/WEAK/FAILURE determination.

**System-level thresholds** (from PHASE_1_DECISION_TREES.md, reproduced for reference):
- STRONG: Score 3+ reply rate >= 50% AND >= 4 constituencies passing their individual strong threshold AND >= 3 cross-org references AND >= 2 confirmed adoptions
- MODERATE: Score 3+ rate 30-49% OR >= 3 constituencies at strong threshold OR >= 1 cross-org reference OR >= 1 confirmed adoption
- WEAK: Rate < 20% AND < 2 constituencies at strong threshold AND 0 cross-org references
- FAILURE: Rate < 10% AND 0 adoptions AND 0 cross-org references AND 0 Gist clicks in Weeks 3-4

**Constituency-level Day 30 strong thresholds** (from PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 4):
| Constituency | Strong threshold | Moderate threshold |
|---|---|---|
| Law Schools | >= 3 Score 3+ replies | >= 1 reply at any score |
| Immigration Legal Aid | >= 2 Score 3+ replies OR 1 confirmed litigation use | >= 1 Score 3+ reply |
| Civil Rights | >= 3 Score 2+ replies OR 1 confirmed policy adoption | >= 1 Score 2+ reply |
| Academic | >= 2 Score 3+ replies OR 1 confirmed citation | >= 1 reply at any score |
| Faith | >= 2 engaged contacts OR 1 pastoral use | >= 1 engaged contact |
| Labor | >= 2 engaged contacts OR 1 confirmed training integration | >= 1 engaged contact |
| Mutual Aid | >= 2 engaged contacts OR 1 confirmed governance use | >= 1 engaged contact |

### Day 60 Checkpoint (July 27, 2026)

**Purpose**: Movement-scale impact assessment and Phase 2 full-scale activation decision.

**System-level thresholds**:
- Full-scale Phase 2 activation: >= 15 confirmed organizational adoptions AND >= 100 people reached
- Partial Phase 2: >= 8 confirmed adoptions AND >= 50 people reached — launch Phase 2 in constituencies with confirmed adoption only
- Below target: < 8 confirmed adoptions — pull Z (count of constituencies with >= 1 confirmed adoption); if Z >= 4, launch Phase 2 in those 4; if Z < 4, escalate to CHECKIN.md for user decision

---

## 5. Solo Operator Measurement Overhead

**The 15-minute/week figure is real under normal conditions. Here is where it breaks down.**

The PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md Weekly Update Checklist estimates 15 minutes per week (5 min email review + 3 min Bitly pull + 4 min web sweep + 3 min dashboard update). That estimate is accurate for a steady-state week with two to three new replies and no anomalies.

Overhead increases in three scenarios:

**Scenario A — High reply week** (e.g., Day 8-10, immediately after Wave 1 send): If 8-12 replies arrive in a 3-day window, scoring and logging each reply takes 3-4 minutes per reply, not the average. A 10-reply week takes 30-40 minutes, not 15. This is front-loaded — it happens once and does not repeat at the same intensity.

**Scenario B — Adoption signal detected**: When a Level 4 or Level 5 adoption signal arrives, it requires: (1) entering in Adoption Signal Registry (5 minutes), (2) updating Constituency-Aggregated Metrics (3 minutes), (3) running a checkpoint determination if the signal tips a threshold (5-10 minutes), (4) deciding whether to log in CHECKIN.md (5 minutes). Total: 15-20 minutes for a single adoption event. Expect 2-4 such events in the May 28 – July 27 window.

**Scenario C — Synthesis weeks**: The weekly synthesis template (PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md) adds approximately 20 minutes to the standard 15-minute checklist. Synthesis weeks occur at Week 1 (June 4), Week 2 (June 11), Week 4 (June 27 Day 30 checkpoint), and Week 8 (July 27 Day 60 checkpoint). Four weeks with 35 minutes of work; four weeks with 15 minutes; remaining weeks at 15 minutes each.

**Realistic total overhead for the full May 28 – July 27 window**:
- Weeks 1-2 (high reply period): ~35-45 min/week = 70-90 minutes
- Weeks 3-6 (steady state): ~15-20 min/week = 60-80 minutes
- Week 4 (Day 30 checkpoint): ~60 minutes (full decision tree run + CHECKIN.md update)
- Week 8 (Day 60 checkpoint): ~60 minutes
- Ad hoc adoption signal logging: ~60 minutes across full window
- Total across 8 weeks: approximately 5-6 hours

Averaged across 8 weeks, that is 37-45 minutes per week — not 15. The honest framing is: 15 minutes per week in normal weeks, 45-60 minutes in checkpoint weeks, and a 30-minute burst in the first 10 days.

This is within the 30-minute/week normal / 90-minute/week synthesis constraint specified in the task. The constraint is not violated if checkpoint weeks and Week 1-2 are treated as exceptional rather than typical.

---

## 6. Escalation Triggers

Escalation means flagging something in CHECKIN.md under "Needs Your Input" rather than proceeding autonomously. The threshold for escalation is: a decision that cannot be reversed if wrong.

**Escalate immediately (same day)**:
- Zero Bitly clicks AND zero replies with confirmed delivery at Day 7. This is the delivery failure signal. The fix (re-sending to corrected addresses, switching delivery pathway) must be initiated within 48 hours to preserve the Day 30 timeline.
- A single Score 5 adoption event (citation, institutional adoption statement, co-authorship offer). This is the overperformance signal. Same-day Phase 2 pre-activation is available; that decision belongs to the user.
- Three or more email bounces. Bounce rate >= 6% from a 45-contact list suggests a contact list quality problem, not individual address errors.

**Escalate within 24 hours**:
- Day 30 determination of FAILURE (rate < 10%, zero adoptions, zero cross-org references, dead Gist clicks in Weeks 3-4). Full contingency review required.
- Day 14 shows zero Level 3+ replies AND zero Bitly activity in Days 8-14. Silence in the second week indicates the initial send did not land. This is not yet failure but requires a framing revision decision.
- Any reply that contains a legal concern, privacy concern, or request not to be contacted again. These require direct user response within 24 hours; automated handling is not appropriate.

**Do not escalate — wait for signal**:
- Level 1 and Level 2 replies only at Day 7. Polite acknowledgment is normal. Wait for the Day 14 check.
- A single constituency at zero signal at Day 7. One constituency below threshold is not a system-level problem.
- Reply rate below 25% at Day 14. Reply rates for cold institutional outreach typically peak at Days 10-21. Day 14 data is directional, not final.
- Gist click counts below the Week 1 target of 15. Low click counts in Week 1 can reflect recipients who print documents, share links without clicking them in ways Bitly captures, or who read the email without clicking through. Wait for replies to confirm whether reading happened through alternative paths.
