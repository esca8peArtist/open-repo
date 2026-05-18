---
title: "Phase 2 Wave 1 Post-Execution Analysis & Learning Framework"
created: 2026-05-18
status: production-ready — execute from Wave 1 completion (May 18 10:00 UTC) through Week 1 synthesis (May 25 20:00 UTC)
scope: "Real-time metrics tracking, daily checkpoint templates, Week 1 synthesis protocol, success threshold definitions by constituency"
audience: thorn — operational reference from send completion through Phase 2 path decision
decision_gate: "May 25 20:00 UTC (Phase 2 path confirmed based on Week 1 synthesis output)"
companion_files:
  - WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv
  - WAVE_1_MONITORING_DASHBOARD.md
  - WAVE_1_SYNTHESIS_FRAMEWORK.md
  - WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md
  - PHASE_2_OUTCOME_LAUNCH_ROADMAP.md
  - BATCH_1_CONTACT_LOG.md
---

# Phase 2 Wave 1 Post-Execution Analysis & Learning Framework

*Resistance Research Agent — May 18, 2026*

**How to use this document**: This is the learning infrastructure for the 72-hour post-Wave-1 window and the Week 1 synthesis on May 25. Section 1 is the real-time metrics spreadsheet template — populate it continuously from May 18 10:00 UTC through May 25. Section 2 is the daily checkpoint template — open the correct day's block each morning and execute it in 10–15 minutes. Section 3 is the Week 1 synthesis protocol — execute it May 25 (2–3 hours total). Section 4 defines success thresholds by metric type and constituency. The output of this document feeds WAVE_1_SYNTHESIS_FRAMEWORK.md at the May 21 decision gate and the Phase 2 path decision at May 25.

**What this document is not**: A monitoring dashboard (that is WAVE_1_MONITORING_DASHBOARD.md) or a classification formula (that is WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md). This document adds the learning layer — it asks "what did this round teach us, and how does that change Phase 2 design?" — on top of the monitoring and classification infrastructure.

---

## SECTION 1: Real-Time Metrics Spreadsheet Template

### 1.1 Contact Response Rate Tracker

Populate one row per Batch 1 contact. Update daily through Day 14. This is the master engagement record for Phase 1 learning.

| Contact | Institution | Constituency | Sent Date/Time | Delivery Status | First Open | First Reply Date | Reply Type | Score (0–5) | Content Keywords | Referral Given? | Follow-Up Required? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Goodman | Just Security / NYU Law | Law School | May 18, 08:00 UTC | — | — | — | — | — | — | — | — |
| Wendy Weiser | Brennan Center | Think Tank | May 18, 08:30 UTC | — | — | — | — | — | — | — | — |
| Erica Chenoweth | Harvard Kennedy School | Law School | May 18, 09:00 UTC | — | — | — | — | — | — | — | — |
| Ian Bassin | Protect Democracy | Think Tank | May 18, 09:30 UTC | — | — | — | — | — | — | — | — |
| Marc Elias | Democracy Docket | Immigration Legal Aid | May 18, 10:00 UTC | — | — | — | — | — | — | — | — |

**Score definitions** (from WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv — replicated here for quick reference):
- **Score 0**: Silence. No bounce, no reply.
- **Score 1**: Acknowledgment only — "Thanks, received." No domain-specific content.
- **Score 2**: Generic engagement — positive but no specific domain citation or question.
- **Score 3**: Substantive engagement — cites a domain by number, asks a methodological question, or challenges a specific argument.
- **Score 4**: Implementation or referral signal — asks how to operationalize, names a colleague or organization to forward to, or requests domain-specific content in a particular format.
- **Score 5**: Integration signal — publicly cites the framework, uses it in a filing or brief, or explicitly offers formal collaboration.

**Delivery status values**: CONFIRMED (email opened or Gist clicked from expected IP region), HARD_BOUNCE (permanent failure — re-verify address), SOFT_BOUNCE (temporary failure — retry in 48h), OOO (auto-reply received — add return date to Follow-Up Required column), UNCONFIRMED (no signal either way — log as such at Day 7).

---

### 1.2 Gist View Rate Tracker

Check Gist view counts in incognito mode at each daily checkpoint. Record the delta since baseline (H+0, May 18 ~08:00 UTC).

| Gist Document | Baseline Views (H+0) | Day 1 Views | Day 1 Delta | Day 2 Views | Day 2 Delta | Day 3 Views | Day 3 Delta | Day 7 Views | Day 7 Delta | Day 14 Views | Day 14 Delta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Main Democratic Renewal Proposal | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Executive Summary | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Litigation Tracker 2026 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Domain 37 (Election Interference) | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Domain 42 (Drug Policy/DEA) | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| **Total across all Gists** | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |

**Interpretation guide**: A Gist view delta does not map directly to a single contact. Multiple contacts may click one Gist; one contact may click multiple Gists. The signal value of Gist views is as a proxy for reach beyond the direct recipient (forwarding). If the total Gist delta exceeds 5 × the number of emails sent (25 in this case), this indicates forwarding has occurred. If the Litigation Tracker Gist shows a large delta relative to the main proposal, that suggests contacts are drilling into the case-specific evidence — a higher-engagement signal than viewing the executive summary only.

---

### 1.3 Email Performance Tracker

Track email delivery and engagement performance. If you used an email client with tracking (read receipts, link tracking), populate these fields. If you did not use tracking, record what you can observe indirectly (reply timing, Gist view timing relative to send time).

| Contact | Send Time (UTC) | Estimated Read Time | Hours to First Signal | Domain Referenced in Reply | Specific Citation or Question? | Forwarded To (if known) | Content Tone | Urgency Indicator |
|---|---|---|---|---|---|---|---|---|
| Ryan Goodman | May 18, ~08:00 | — | — | — | — | — | — | — |
| Wendy Weiser | May 18, ~08:30 | — | — | — | — | — | — | — |
| Erica Chenoweth | May 18, ~09:00 | — | — | — | — | — | — | — |
| Ian Bassin | May 18, ~09:30 | — | — | — | — | — | — | — |
| Marc Elias | May 18, ~10:00 | — | — | — | — | — | — | — |

**Content tone classification**:
- **Collaborative**: Contact is exploring how to use the material; opens coordination or co-production language.
- **Critical**: Contact identifies a methodological gap or data challenge — still high value, but a different engagement type.
- **Supportive**: Contact affirms the work without specific domain citation — lower signal weight than Collaborative or Critical.
- **Instrumental**: Contact asks for a specific extract or format — the highest operational engagement signal.
- **Skeptical**: Contact questions the premise — important to log accurately; skeptical replies from credible sources are substantive, not negative.

**Urgency indicator**: Note if the contact's reply references a specific deadline, court date, legislative hearing, or publication timeline — this converts a Score 3 reply into a de-facto Score 4 because it means the contact is thinking about operational application, not just intellectual interest.

---

### 1.4 Institutional Adoption Signals per Tier

This table tracks signals of institutional adoption — evidence that the framework has reached an institution's workflow, not just an individual inbox.

| Date | Signal Type | Contact or Source | Institution | Tier | Domain Referenced | Adoption Stage | Notes |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

**Adoption stage definitions**:
- **Awareness**: Contact read and acknowledged — institution has heard of the framework.
- **Consideration**: Contact asked questions or forwarded to colleagues — institution is evaluating fit.
- **Integration**: Contact asked for an extract, specific formatting, or co-production offer — institution is incorporating the analysis.
- **Advocacy**: Contact cites the framework publicly, uses it in a filing, or distributes it to their network — institution has adopted and is amplifying.

**Tier 1 contacts** are the five Batch 1 recipients. **Tier 2** would be any organization they forward to that surfaces in a reply or social signal. **Tier 3** is any downstream adoption you observe in public discourse (citation, social media reference, news coverage).

---

### 1.5 Cross-Domain Interest Mapping

This table tracks which domains are receiving disproportionate attention relative to the overall framework. It is populated by reading reply content carefully for domain citations, Gist view patterns, and any forwarding signals.

| Domain | # Contacts Referencing It | Specific Questions Asked | Urgency Signals | Likely Constituency Fit (from reply) | Phase 2 Priority Impact |
|---|---|---|---|---|---|
| Domain 37 (Federal Election Interference) | ___ | ___ | ___ | ___ | ___ |
| Domain 42 (Drug Policy / DEA Rescheduling) | ___ | ___ | ___ | ___ | ___ |
| Domain 57 (Multilateral Withdrawal) | ___ | ___ | ___ | ___ | ___ |
| Domain 59 (Economic Precarity as Civic Exclusion) | ___ | ___ | ___ | ___ | ___ |
| Domain 39 (Healthcare Access) | ___ | ___ | ___ | ___ | ___ |
| Other (specify) | ___ | ___ | ___ | ___ | ___ |

**Why this matters for Phase 2**: If contacts are referencing Domain 39 repeatedly but it is not yet in full production, that is a Phase 2 research acceleration signal. If a domain you expected to resonate (Domain 42 for the DEA contacts) is not referenced in replies from those same contacts, that is a messaging calibration signal — either the framing missed, or the timing was off relative to their current work.

---

## SECTION 2: Daily Checkpoint Templates

Execute the correct day's block each morning. Time commitment: 10–15 minutes for Days 1–6, 45–60 minutes for the Day 7 synthesis. Record findings in Section 1 tables, then log the daily assessment in WAVE_1_MONITORING_DASHBOARD.md.

---

### Day 0 — May 18 (Send Day): Post-Send Learning Capture

Execute after all five emails sent (after 10:00 UTC).

**Execution learning questions** (5 minutes — answer now, before the signal window distorts memory):

1. Were all five emails sent exactly as drafted? If not, what changed, and why? (Changes made under time pressure reveal template weaknesses.)
2. Did any email require a last-minute edit for accuracy or tone? Which contact, and what was the issue?
3. Was the send sequence followed as planned (Weiser → Elias → Goodman → Chenoweth → Bassin)? If not, what order was actually used?
4. Did any technical problem arise (email client, copy-paste error, Gist URL check fail)? Log it — this is infrastructure learning.
5. Gut-level assessment: Which of the five emails felt strongest as sent? Which felt weakest? (This is pre-signal intuition — compare it against actual results in the Day 7 synthesis.)

**Record your answers here**:
- All emails sent as drafted: YES / NO — if NO: [describe deviation]
- Last-minute edits: [contact, issue]
- Send sequence used: [actual order]
- Technical problems: [describe or NONE]
- Felt strongest: [contact] — [reason]
- Felt weakest: [contact] — [reason]

---

### Day 1 — May 19: First Full Business Day Check

**Morning check (09:00 UTC)** — 10 minutes:
- [ ] Open inbox. Log all new messages in Section 1.1 Contact Response Rate Tracker.
- [ ] Check Gist views in incognito. Log Day 1 values in Section 1.2.
- [ ] Any hard bounces? If yes: re-verify address immediately, log in Section 1.1 Delivery Status.
- [ ] Any OOO auto-replies? If yes: log return date in Follow-Up Required column.

**Day 1 learning questions**:
1. Total early signals (any type): ___. Is this above or below the H+24 expectation of ~1–2 signals from the five contacts?
2. Which Gist is showing the highest delta so far? This predicts which content hook is being clicked through.
3. Any unexpected signal? (A reply from an email not in Batch 1, a social media reference, a colleague forwarding — all worth noting.)

**Assessment** (circle): ABOVE_EXPECTATION | WITHIN_EXPECTATION | BELOW_EXPECTATION

**Below expectation trigger**: If Day 1 shows zero Gist delta and zero replies/OOO/bounces across all five contacts, run a delivery self-test immediately (send a test email to yourself from the same account and inbox the message). If it lands in spam: flag in CHECKIN.md under "Needs Your Input" — delivery problem before content problem.

---

### Day 2 — May 20: Elias Response Window

**Context**: Marc Elias's typical response cycle is 48 hours or less for targeted, case-relevant outreach. May 20 is the window to check for any Elias signal (Score 1–5). Elias not responding by May 20 is within sector norm; Elias responding by May 20 is a high-salience signal.

**Morning check (09:00 UTC)** — 10 minutes:
- [ ] Log all new messages in Section 1.1.
- [ ] Update Gist view tracker (Day 2 column in Section 1.2).
- [ ] Check specifically for Elias signal: [YES — Score ___] / [NO — within norm]

**Day 2 learning questions**:
1. If Elias has replied: what specifically did he reference? (Callais cascade? Domain 37? A specific docket?) Log the domain and question type in the Cross-Domain Interest Mapping table (Section 1.5).
2. If Elias has not replied: is there a Gist view delta that could correspond to the Elias Law Group IP region (DC area)? Note if the Litigation Tracker Gist has a higher view count than the main proposal — this would be consistent with a litigation-focused recipient drilling into the case evidence.
3. Any signal from Weiser or Bassin (think tank cluster)? Their 48–72 hour response cycle means Day 2 is within their window.

**Assessment**: ELIAS_SIGNAL: YES/NO | THINK_TANK_SIGNAL: YES/NO

---

### Day 3 — May 21: 72-Hour Synthesis Gate

**This is the first classification checkpoint.** Execute WAVE_1_SYNTHESIS_FRAMEWORK.md after completing this daily check. The synthesis document takes 30–45 minutes to complete.

**Morning check (09:00 UTC)** — 10 minutes before synthesis:
- [ ] Log all new messages in Section 1.1.
- [ ] Update Gist view tracker (Day 3 column in Section 1.2).
- [ ] Complete the Signal Aggregation Table in WAVE_1_SYNTHESIS_FRAMEWORK.md Section 2.

**Day 3 learning questions**:
1. Which constituency showed the fastest response cycle? (Expected: Immigration Legal Aid / Elias fastest; Law Schools slowest at this point.)
2. Which domain was referenced most specifically in any replies? Compare to Section 1.5 Cross-Domain Interest Mapping.
3. What is the Gist view delta total across all five Gists? Does the pattern suggest forwarding (total delta >> 5x contacts × average views per email)?
4. Any surprise (positive or negative) in the reply content that the pre-sent templates could not have anticipated? (A contact mentioning an upcoming filing, a reference to a domain you did not highlight in their specific email, an unexpected organizational affiliation they mention.)

**Output from Day 3**: Preliminary STRONG/MODERATE/WEAK classification per WAVE_1_SYNTHESIS_FRAMEWORK.md. Log classification here: ___ and in CHECKIN.md (preliminary).

---

### Day 4 — May 22: Bassin/Weiser Window Close

**Context**: Protect Democracy (Bassin) and Brennan Center (Weiser) typically respond within 5 business days. Day 4 (May 22) is the first day to note a "no signal yet" for these two contacts without it being unexpected. It is not a Weak signal — it is within the expected range for policy organizations. Day 7 is the first day their silence matters for classification.

**Morning check (09:00 UTC)** — 10 minutes:
- [ ] Log all new messages in Section 1.1.
- [ ] Update Gist view tracker.
- [ ] Note any follow-up actions triggered by Day 3 classification:
  - If STRONG: have you flagged CHECKIN.md with "Phase 2 June 15 parallel launch pending user confirmation"?
  - If MODERATE: have you confirmed Domain 39 pre-distribution package (3-hour session) is on the schedule for Week 1?
  - If WEAK: have you run delivery diagnosis and confirmed delivery to all five contacts?

**Day 4 learning question** (the only one that matters today):
Are there any signals that change the Day 3 preliminary classification? If yes, what changed and in which direction?

**Classification update**: [UNCHANGED / UPGRADED TO STRONG / DOWNGRADED TO WEAK] — reason: ___

---

### Day 5 — May 23: Goodman / Chenoweth First Possible Window

**Context**: Ryan Goodman (Just Security) and Erica Chenoweth (Harvard Kennedy School) operate on 5–10 day response cycles. Day 5 is the earliest this constituency would respond under normal conditions. A Day 5 reply from either law school contact is a higher-than-expected signal (Score 4 equivalent in weight even if technically Score 3 content — the speed of response indicates salience).

**Morning check (09:00 UTC)** — 10 minutes:
- [ ] Log all new messages in Section 1.1.
- [ ] Update Gist view tracker.
- [ ] Note any replies from Goodman or Chenoweth.

**Day 5 learning questions**:
1. What is the cumulative response rate so far (contacts who have produced any signal / 5 contacts)? ___
2. Is the cross-domain interest map developing a pattern? (e.g., all replies referencing election law domains, or all replies referencing the economic precarity angle?) Log in Section 1.5.
3. Any signals that suggest forwarding has occurred — a contact at an organization not in Batch 1 reaching out, a Gist view spike on a specific day and time that suggests a team meeting or presentation?

---

### Day 6 — May 24: Pre-Synthesis Preparation

**Purpose**: Prepare data for the Day 7 full synthesis. Check all fields in Section 1 for completeness and accuracy. Identify any gaps before the synthesis.

**Morning check** — 15 minutes:
- [ ] Review Section 1.1: Is every contact's Delivery Status filled in (CONFIRMED, OOO, HARD_BOUNCE, UNCONFIRMED)? Fix any gaps.
- [ ] Review Section 1.2: Is every Gist row current through Day 6? Fill in Day 3 delta if it was not recorded day-of.
- [ ] Review Section 1.5: Does every reply reference at least one domain? If a reply did not cite a domain, classify the reply content to the closest domain by topic.
- [ ] Identify the single most important thing this round has taught you so far — one sentence. Record it here: ___

**Pre-synthesis classification** (preliminary — Day 3 classification updated with 6 days of additional signal):
- Aggregate classification: STRONG / MODERATE / WEAK
- Highest-performing constituency: Law Schools / Immigration Legal Aid / Think Tanks / (None yet)
- Most-referenced domain: ___
- Biggest surprise (if any): ___

---

### Day 7 — May 25: Week 1 Full Synthesis

Execute Section 3 of this document (Week 1 Synthesis Protocol) in its entirety after the morning check.

**Morning check** — 10 minutes before synthesis:
- [ ] Log all new messages in Section 1.1.
- [ ] Update Gist view tracker (Day 7 column).
- [ ] Check for any OOO contacts whose return dates have now passed — do they need a follow-up?
- [ ] Confirm the Phase 2 path decision gate is on the calendar for May 25 20:00 UTC.

---

## SECTION 3: Week 1 Synthesis Protocol

**Execute May 25, starting after Day 7 morning check. Total time: 2–3 hours.**

This protocol is the learning output for Phase 1 Wave 1. It produces: (1) a final STRONG/MODERATE/WEAK classification for each constituency, (2) a cross-domain interest map informing Phase 2 research priorities, (3) a messaging effectiveness assessment, (4) a Tier 2 targeting recommendation, and (5) three to five actionable adjustments for Phase 2 messaging or content.

---

### 3.1 Signal Aggregation (30 minutes)

**Step 1**: Pull all rows from Section 1.1 (Contact Response Rate Tracker). For each contact, record:
- Final Score (0–5)
- Content keywords (what specific concepts did they reference?)
- Whether they are an OOO contact still in window (if so, extend their classification by return date)
- Any referral made (who did they name or forward to?)

**Step 2**: Compute Quality Reply Points (QRP) using the formula from WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md:

```
Score 5 = STRONG OVERRIDE (classify entire Wave as STRONG regardless of other data)
Score 4 = 2.0 QRP
Score 3 = 1.0 QRP
Score 2 = 0.5 QRP
Score 1 = 0.0 QRP (acknowledged delivery, no substantive signal)
Score 0 = 0.0 QRP (may indicate delivery problem — check)
Gist delta: 1.0 QRP per 20-view increment above baseline, max 1.0 QRP total
```

**Total QRP**: ___

**Step 3**: Apply the classification formula:
- STRONG: QRP >= 2.0 OR any Score 5
- MODERATE: QRP >= 1.0 with at least one substantive reply (Score 3+)
- WEAK: QRP < 1.0 OR no substantive replies AND Gist delta < 10

**Final aggregate classification**: STRONG / MODERATE / WEAK

---

### 3.2 Constituency-Level Classification (20 minutes)

For each constituency, classify performance independently using the thresholds from PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 1.

Fill in the table:

| Constituency | Contacts in Wave 1 | Replies Received | Highest Score | Classification | Notes |
|---|---|---|---|---|---|
| Law Schools | Goodman, Chenoweth (2) | ___ | ___ | STRONG / EXPECTED / WEAK | ___ |
| Immigration Legal Aid | Elias (1) | ___ | ___ | STRONG / EXPECTED / WEAK | ___ |
| Think Tanks | Weiser, Bassin (2) | ___ | ___ | STRONG / EXPECTED / WEAK | ___ |
| Unions / Labor | 0 (Tier 2 only) | N/A | N/A | N/A — assess after Tier 2 | — |

**Key question**: Does any constituency-level divergence from the aggregate classification suggest a different Phase 2 sequencing than the aggregate outcome would prescribe? (See PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 2.2 and 6.3 for split-outcome handling.)

If YES: ___ constituency performing at STRONG while aggregate is MODERATE/WEAK. Action: apply the STRONG sequence for domains serving that constituency; apply MODERATE/WEAK sequence for others.

---

### 3.3 Cross-Domain Interest Analysis (20 minutes)

Review all reply content and Gist view data. Identify which domains generated the most specific references, questions, or click-through signals.

**Domain interest ranking** (1 = most referenced):

| Rank | Domain | Evidence | Phase 2 Implication |
|---|---|---|---|
| 1 | ___ | ___ | ___ |
| 2 | ___ | ___ | ___ |
| 3 | ___ | ___ | ___ |
| 4+ | Other | ___ | ___ |

**Key question**: Is the domain interest pattern aligned with the Phase 2 sequence in PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 4? If contacts referenced domains that are not yet scheduled (e.g., Domain 39, which is in the non-negotiable pre-distribution category), this confirms those priorities. If contacts referenced domains not in the Phase 2 core sequence (e.g., a contact repeatedly cited Domain 42 on drug policy), this is a signal to consider whether that domain should move up in the Phase 2 queue.

**Domain misalignment flag**: If any domain in the top 3 is NOT in the Phase 2 sequence, flag in CHECKIN.md under "Needs Your Input" with a recommendation.

---

### 3.4 Messaging Effectiveness Assessment (30 minutes)

This step evaluates whether the email framing worked as designed — not whether contacts liked the material, but whether the specific arguments in each email generated the expected type of engagement.

**For each reply received at Score 2 or above**:

1. Which paragraph in the original email did the contact reference or respond to? (The opening, the domain hook, the specific study cited, the reform proposal, the call to action?)
2. Was the contact's question or comment expected based on the email design, or unexpected?
3. Did the contact's reply reveal any misalignment between the email's framing and their actual priorities? (e.g., you framed Domain 37 as an election administration issue and the contact responded from a civil liberties angle — this is a misalignment that informs Tier 2 framing)
4. Did the contact ignore the primary domain hook and reference a secondary or even unmentioned domain? (This is the most valuable signal — it tells you what this constituency actually cares about regardless of your framing.)

**Messaging assessment table**:

| Contact | Email Primary Hook | Contact's Actual Reference | Alignment | Implication for Tier 2 Messaging |
|---|---|---|---|---|
| Goodman | ___ | ___ | ALIGNED / MISALIGNED | ___ |
| Weiser | ___ | ___ | ALIGNED / MISALIGNED | ___ |
| Chenoweth | ___ | ___ | ALIGNED / MISALIGNED | ___ |
| Bassin | ___ | ___ | ALIGNED / MISALIGNED | ___ |
| Elias | ___ | ___ | ALIGNED / MISALIGNED | ___ |

**Silence analysis** (for contacts at Score 0 or Score 1 after Day 7):
- Is silence a delivery problem (check Gist views for IP/timing correlation)?
- Is silence a content problem (framing did not match this contact's current priorities — check their recent public work for what they are actively engaged in right now)?
- Is silence a timing problem (late-semester, travel, pending publication deadline, hearing prep — check public calendar or recent social media)?

Silence analysis for each non-responding contact:
- [Contact]: Likely reason — DELIVERY / CONTENT / TIMING / UNKNOWN

---

### 3.5 Tier 2 Candidate Identification (20 minutes)

Based on Week 1 engagement data, identify the three to five highest-priority Tier 2 contacts to target first in the upcoming Phase 2 outreach round.

**Tier 2 candidate table**:

| Contact | Institution | Constituency | Why Prioritized | Domain Hook | Timing Recommendation |
|---|---|---|---|---|---|
| ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ |

**Priority criteria for Tier 2 selection**:
1. **Referrals from Wave 1 contacts**: Any name or organization that a Batch 1 contact mentioned in their reply is the single highest-priority Tier 2 candidate. A referred contact has a 4–6x higher reply probability than a cold contact.
2. **Domain alignment with strongest-performing constituency**: If law school contacts performed at STRONG, prioritize law school Tier 2 contacts whose specialty aligns with the most-referenced domain.
3. **Institutional leverage**: Contacts at organizations whose adoption would create downstream amplification (e.g., a Brennan Center researcher who publishes widely, a union legislative staff member who testifies frequently, an immigration legal aid clinic that trains hundreds of law students).
4. **Policy window urgency**: If a Tier 2 contact has a public deadline approaching (a hearing, a filing, a publication) that the framework's domains are relevant to, that contact moves to the top of the list regardless of institutional prestige.

---

### 3.6 Content and Messaging Adjustments (20 minutes)

Identify three to five specific adjustments to make to Phase 2 messaging before Tier 2 sends, based on the Week 1 data.

Use this table:

| Adjustment | Evidence That Prompted It | Specific Change to Make | Applies To | Priority |
|---|---|---|---|---|
| ___ | ___ | ___ | Subject line / Lead paragraph / Domain hook / Call to action | HIGH / MEDIUM |
| ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ |

**Adjustment categories to consider**:
- **Subject line**: If no contacts referenced a domain by its full title (suggesting they did not read past the subject line), consider a more specific or urgent subject line for Tier 2.
- **Lead paragraph**: If replies focused on concerns you did not address in the lead paragraph, restructure Tier 2 lead paragraphs to open with the concern rather than the methodology.
- **Domain hook**: If replies referenced a domain you did not feature prominently in their email, revise the domain emphasis for Tier 2 emails to that constituency.
- **Call to action**: If contacts replied but did not take the action you intended (e.g., they engaged with the material but did not ask for an extract or share it), consider a more specific call to action in Tier 2 emails.
- **Format or length**: If any contact's reply indicated they skimmed rather than read (e.g., "interesting work, I'll read more carefully later"), consider offering a shorter entry point (executive summary, domain one-pager) as the primary artifact in Tier 2 sends.

---

### 3.7 Week 1 Synthesis Output Summary (10 minutes)

Produce a one-page summary to carry into the Phase 2 path decision conversation. Write it here, then copy relevant sections to CHECKIN.md if user input is needed.

**Week 1 Synthesis Summary — May 25, 2026**

**Final aggregate classification**: STRONG / MODERATE / WEAK

**Constituency-level summary**:
- Law Schools: STRONG / EXPECTED / WEAK — strongest signal from: ___
- Immigration Legal Aid: STRONG / EXPECTED / WEAK — strongest signal from: ___
- Think Tanks: STRONG / EXPECTED / WEAK — strongest signal from: ___

**Most referenced domains** (in order): (1) ___ (2) ___ (3) ___

**Biggest surprise**: ___

**Top 3 Tier 2 candidates identified**: (1) ___ (2) ___ (3) ___

**Top 3 messaging adjustments for Tier 2**: (1) ___ (2) ___ (3) ___

**Phase 2 sequence recommendation** (from PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 2 matrix, applied to your classification):
- Under [CLASSIFICATION]: Domain sequencing is [per Section 4.2 / 4.3 / 4.4 of PHASE_2_OUTCOME_LAUNCH_ROADMAP.md]
- Tier 2 activation window: [per Section 5.1 of PHASE_2_OUTCOME_LAUNCH_ROADMAP.md]
- Highest-priority Tier 2 constituency: ___

**User decision required by May 25 20:00 UTC**: CONFIRM Phase 2 path (A / A+37 / B) based on aggregate classification above. Decision unlocks same-day Phase 2 research launch.

---

## SECTION 4: Success Threshold Definitions

### 4.1 Framing: What "Success" Means at This Stage

Phase 1 Wave 1 is not a mass email campaign. It is five personalized, highly targeted sends to institutional contacts who have been verified as actively working on the domains in the framework. Success thresholds should not be set against mass email benchmarks (1.4% open rate, M+R 2026). They should be set against targeted practitioner outreach benchmarks and the specific goals of this wave: (1) establish that the framework reaches working practitioners, (2) generate substantive engagement that informs Phase 2 sequencing, (3) identify the two to three highest-leverage Tier 2 contacts through referrals or domain signals.

A Wave 1 that produces one Score 5 (public citation or formal collaboration offer) is a complete success even if four contacts do not respond. A Wave 1 that produces five Score 1 replies (all acknowledged, none engaged) is a meaningful signal even if the response rate is technically 100% — it means the framing did not connect with what these specific contacts are working on right now.

Success is defined at the level of what the data teaches, not at the level of response rate.

---

### 4.2 Success Thresholds by Metric Type

#### Gist View Rates

| Threshold | Definition | What It Indicates |
|---|---|---|
| Exceptional | Total Gist delta >50 views in 7 days with >3 distinct Gist documents showing delta | Contacts have clicked through to multiple documents; forwarding is likely; reach has extended beyond the five direct recipients |
| Good | Total Gist delta 15–50 views in 7 days; at least 2 Gist documents showing delta | At least 2–3 contacts clicked through; primary proposal is being read, not just acknowledged |
| Minimum Viable | Total Gist delta 5–14 views in 7 days; at least 1 Gist showing delta | At least 1 contact clicked through; delivery confirmed through behavior even without reply |
| Below Minimum | Total Gist delta <5 views in 7 days with delivery confirmed | Check for Gist URL expiration; check if contacts access documents differently (downloads, screenshots); do not classify as content failure until technical diagnosis is complete |
| Inconclusive | Total Gist delta = 0 AND zero replies AND zero bounces | Delivery problem until proven otherwise; do not make content or messaging changes until delivery is confirmed |

#### Email Response Rates

| Threshold | Definition | What It Indicates |
|---|---|---|
| Exceptional | 3 or more Score 3+ replies within 7 days from 5 contacts (60%+ reply rate) | Strong constituency-level validation; at least one referral or implementation signal expected within 14 days; Tier 2 activation immediately justified |
| Good | 1–2 Score 3+ replies within 7 days (20–40% reply rate) | Minimum threshold for STRONG classification; domain hooks working; Tier 2 activation justified on Days 20–28 with strong social proof framing |
| Minimum Viable | 1 Score 3+ reply within 14 days from any contact | MODERATE classification threshold; confirms the framework reaches working practitioners; Tier 2 activation on Days 27–35 |
| Below Minimum | 0 Score 3+ replies within 14 days, with delivery confirmed | WEAK classification; triggers messaging and framing audit before Tier 2; does not indicate the framework is wrong — may indicate framing, timing, or contact selection issues |
| Acknowledged Only | All replies at Score 1 within 7 days | Not a failure; confirms delivery; indicates the email hook did not create urgency; revise subject line and lead paragraph for Tier 2 |

---

### 4.3 Success Thresholds by Constituency

#### Law Schools (Goodman, Chenoweth — 2 Batch 1 contacts)

| Threshold | Definition |
|---|---|
| Exceptional | Both contacts reply at Score 3+ within 10 days; at least one contact offers a referral or names a clinic director |
| Good | 1 of 2 contacts replies at Score 3+ within 10 days; the second may still be in window at Day 10 (extended window applies) |
| Minimum Viable | 1 of 2 contacts replies at Score 3+ within 14 days. Law school contacts have a 14-day effective window (not 7). A Day 12 reply from Chenoweth at Score 3 is still minimum viable. |
| Below Minimum (Weak) | Zero Score 3+ replies from either contact by Day 14, with delivery confirmed |
| Note | A Score 4 from one contact with silence from the other = GOOD for this constituency. Academic contacts' silence through Day 10 is not meaningful — they are in end-of-semester review periods or traveling |

**Phase 2 signal implications**:
- Exceptional or Good: Domain 57 acceleration justified (constitutional asymmetry analysis — highest law school utility); think tank Tier 2 social proof framing available
- Minimum Viable: Domain 57 proceeds on Moderate timeline; think tank Tier 2 uses utility framing only (no social proof from law schools at this threshold)
- Weak: Pivot Tier 2 law school hook to Domain 39 (health law clinic) and Domain 56 (civil service law clinic) — both have faster operational utility than Domain 57 for clinic work

#### Immigration Legal Aid (Elias — 1 Batch 1 contact)

| Threshold | Definition |
|---|---|
| Exceptional | Elias replies within 48 hours with case-specific content — names a docket, references a specific litigation theory, or asks for a domain extract for a filing |
| Good | Elias replies within 5 days at Score 3+ with substantive content but without specific case application |
| Minimum Viable | Elias replies within 7 days at Score 2+ OR provides a referral to a named colleague without substantive content |
| Below Minimum (Weak) | No reply from Elias by Day 7 with delivery confirmed, OR Score 1 reply with no follow-up by Day 10 |
| Note | At one contact, percentage thresholds are proxies for signal quality. "50% response rate" means nothing at n=1; classify by content quality, not rate |

**Phase 2 signal implications**:
- Exceptional: Domain 39 pre-distribution (June 1) and Domain 57 Section 3 (ICC sanctions) become the joint Tier 2 immigration legal aid hook; accelerate NILC and CLINIC contacts into Week 5 outreach
- Good: Domain 39 pre-distribution proceeds (non-negotiable regardless); Domain 57 Section 3 available as a secondary hook in Tier 2 immigration legal emails by Week 6
- Minimum Viable: Domain 39 is the sole hook for immigration legal Tier 2; Domain 57 Section 3 not yet validated by practitioner engagement — lead with policy window urgency (HHS June 1) not methodological novelty
- Weak: Domain 39 June 1 distribution proceeds regardless; revise immigration legal Tier 2 subject lines to lead with June 1 deadline rather than methodology or framework description

#### Think Tanks (Weiser, Bassin — 2 Batch 1 proxy contacts)

| Threshold | Definition |
|---|---|
| Exceptional | Both Weiser and Bassin reply at Score 3+ within 7 days; at least one explicitly asks for early access to a Phase 2 domain outline or names a specific colleague at a Tier 2 think tank |
| Good | 1 of 2 replies at Score 3+ within 7 days |
| Minimum Viable | 1 of 2 replies at Score 2+ within 10 days, OR both reply at Score 1 with a follow-up question arriving within 14 days |
| Below Minimum (Weak) | Zero Score 3+ replies from both Weiser and Bassin by Day 7 with delivery confirmed; or both at Score 1 with no follow-up |
| Note | Democracy-focused organizations (Protect Democracy, Brennan Center) are more likely to respond at Score 4 (implementation signal) than research think tanks (Brookings, EPI) — Bassin asking for an implementation summary is a stronger expected signal than Weiser asking for a methodological question |

**Phase 2 signal implications**:
- Exceptional or Good: Think tank Tier 2 pre-contact activates Week 5 (June 15–21) with research-in-progress access offer for Domain 57 and Domain 59 — the two analytically novel arguments think tanks are most positioned to extend
- Minimum Viable: Think tank Tier 2 activates Week 6 (June 22–28) with utility framing; the research-in-progress access offer is available for Domain 57 only (D59 not yet at outline stage)
- Weak: Think tank Tier 2 deferred to Week 7+ and re-anchored to Domain 38 (AI regulatory capture — Brookings/AEI terrain) and Domain 40 (electoral manipulation — CFR and democracy think tank concerns); Domain 57/D59 novelty framing deferred until practitioners validate the methodology first

#### Unions / Labor (0 Batch 1 contacts — Tier 2 only)

No direct Wave 1 signal exists for this constituency. Thresholds apply when Tier 2 union outreach launches.

| Threshold | Applied at | Definition |
|---|---|---|
| Exceptional | Tier 2 assessment, Day 7 post-send | 4+ of 10 union contacts reply at Score 3+ within 10 days; at least one requests Domain 59 content formatted for legislative testimony |
| Good | Tier 2 assessment, Day 7 post-send | 2–3 of 10 contacts reply at Score 3+ within 10 days |
| Minimum Viable | Tier 2 assessment, Day 14 post-send | 1–2 contacts reply at Score 3+ within 14 days |
| Below Minimum (Weak) | Tier 2 assessment, Day 14 post-send | Fewer than 2 substantive replies from 10 contacts within 14 days |

**Wave 1 → Tier 2 bridge for unions** (what to watch in Wave 1 that predicts union engagement): If Weiser or Bassin (think tank proxies) reply with content about economic precarity or OBBBA's worker impact, this validates the Domain 59 union hook and supports leading Tier 2 union emails with the OBBBA compounding argument. If the think tank proxies are silent, lead Tier 2 union emails with the operational hook (Domain 39 June 1 HHS rule, rural hospital voter turnout) rather than the analytical novelty argument.

---

### 4.4 Success Thresholds for Institutional Adoption Signals (All Constituencies)

These thresholds apply regardless of constituency. A single adoption signal at any stage below can override constituency-level Weak classifications.

| Adoption Stage | Minimum Viable | Good | Exceptional |
|---|---|---|---|
| Awareness | All 5 contacts at Score 1+ (delivery confirmed) | All 5 at Score 2+ within 14 days | All 5 at Score 3+ within 14 days |
| Consideration | 1 contact asks a domain-specific question (Score 3) within 14 days | 2+ contacts ask domain-specific questions; at least 1 referral named | 3+ contacts engaged; 2+ referrals named; Gist delta >30 |
| Integration | 1 contact asks for a specific extract or formatted version of a domain (Score 4) | 2+ contacts request formatted extracts or offer co-production | 3+ contacts with integration asks; at least 1 from a previously unreached organization (forwarding confirmed) |
| Advocacy | 1 public citation or formal collaboration offer (Score 5) from any contact | 1 Score 5 + 1 Score 4 from different contacts | 2+ Score 5 signals; framework cited in a public forum (testimony, brief, published article) |

**Override rule**: A single Advocacy-stage signal (Score 5) at any point during the monitoring window overrides all other thresholds and triggers an immediate STRONG classification across all constituencies. Activate the Strong outcome timeline from PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 4.2 immediately upon receiving a Score 5. Notify in CHECKIN.md under "Needs Your Input."

---

### 4.5 Per-Metric Minimum Viable Thresholds — Quick Reference

| Metric | Minimum Viable | Good | Exceptional |
|---|---|---|---|
| Total QRP (all contacts) | 1.0 | 2.0 | 3.0+ |
| Reply rate (Score 3+ within 14 days) | 1 of 5 (20%) | 2 of 5 (40%) | 3+ of 5 (60%+) |
| Gist total delta (7 days) | 5 views | 15 views | 50+ views |
| Referrals named by contacts | 1 named referral | 2 named referrals | 3+ named referrals |
| Time to first Score 3+ reply | Within 14 days | Within 7 days | Within 72 hours |
| Cross-domain interest signals | 1 domain referenced specifically | 2 domains referenced | 3+ domains with specific questions |
| Forwarding signals (Gist timing, referral mentions) | 1 forwarding indicator | 2 forwarding indicators | Confirmed Tier 2 contact reaching out directly |

---

*Document prepared: May 18, 2026 — Wave 1 execution complete 10:00 UTC. Monitoring window active May 18–25. Week 1 synthesis date: May 25. Phase 2 path decision gate: May 25 20:00 UTC.*

*Cross-references: WAVE_1_SYNTHESIS_FRAMEWORK.md (May 21 decision instrument — STRONG/MODERATE/WEAK classification); WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md (QRP formula and worked examples); PHASE_2_OUTCOME_LAUNCH_ROADMAP.md (domain prioritization matrix, per-constituency email templates, Tier 2 pre-contact checklist); WAVE_1_MONITORING_DASHBOARD.md (daily tracking log); WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv (QRP raw data); BATCH_1_CONTACT_LOG.md (contact verification record).*
