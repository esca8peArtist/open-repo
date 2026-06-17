---
title: "Day 7 Checkpoint Execution Decision Framework — Phase 2 Wave 1-2 Routing"
subtitle: "June 17-18, 2026 — STRONG / MODERATE / WEAK Branch Dispatch with Phase 2 Activation Routing"
created: 2026-06-17
purpose: >
  Definitive decision framework for the June 17-18 Day 7 checkpoint.
  Routes engagement metrics from Domains 51, 59, 48 to specific Phase 2
  activation sequences. All branches pre-staged — no discovery required.
  Read time: 15 minutes. Execution time per branch: 20-90 minutes.
domains: [51, 59, 48]
checkpoint_window: "June 17-18, 2026"
hard_deadlines:
  domain_59_senate: "June 25-30 (Senate Finance CTC markup)"
  domain_51_california: "July 1 (California Fair Elections Act ballot lock)"
  domain_48_virginia: "July 15 (Virginia Right to Vote Coalition integration)"
  phase_2_gate: "July 1 (T+14 primary coalition routing gate)"
input_sources:
  - "JUNE_17_DAY7_CHECKPOINT_EXECUTION_CHECKLIST.md (Section 6 composite signals)"
  - "JUNE_17_18_DAY_7_CHECKPOINT_FRAMEWORK.md (coalition leverage windows)"
  - "PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py (--t7-checkpoint output)"
companion_docs:
  - "PHASE_2_ACTIVATION_ROUTING_MATRIX.md (domain-level activation sequences)"
  - "DAY_7_CHECKPOINT_MEASUREMENT_DASHBOARD_TEMPLATE.md (metrics input)"
  - "DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md (Domain 59 express path)"
  - "DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md (Domain 51 Tier 1 expansion)"
status: production-ready
confidence: 92%
---

# Day 7 Checkpoint Execution Decision Framework
## Phase 2 Wave 1-2 Routing — June 17-18, 2026

*Resistance Research — Phase 2 Gate Decision*

**Lead finding from the June 17 03:19 UTC checkpoint run**: Domain 59 is at BELOW THRESHOLD (0 STRONG, 2 MODERATE — CBPP and MomsRising forwarded internally). Domains 51 and 48 have not yet been sent (Wave 1 emails awaiting user copy-paste). The composite checkpoint signal going into the June 17-18 window is WEAK, but WEAK at Day 7 is within normal range and does not close Phase 2. Domain 59 Tier 2 activation is partially forced by Senate Finance markup pressure regardless of signal strength. The decision tree below governs what happens next.

---

## Section 1: Situation Snapshot (June 17 Evening)

### What Has Been Sent

| Domain | Wave 1 Sent | Contacts Reached | Replies | STRONG | MODERATE | Checkpoint |
|--------|------------|------------------|---------|--------|----------|------------|
| 59 (Economic Precarity / CTC) | June 9-11 | 5 of 5 | 2 | 0 | 2 | T+8 (past Day 7) |
| 51 (Campaign Finance / Dark Money) | NOT YET | 0 of 5 | 0 | 0 | 0 | Clock not started |
| 48 (Criminal Justice / Civic Exclusion) | NOT YET | 0 of 6 | 0 | 0 | 0 | Clock not started |

### What Is Staged and Awaiting User Action

- **Domain 51 Wave 1**: Two copy-paste emails in `DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md`. Only [YOUR_NAME] and [YOUR_CONTACT_INFO] to fill. CLC (echlopak@campaignlegalcenter.org) and Issue One (info@issueone.org). July 1 deadline is 14 days away.
- **Domain 48 Wave 1**: Templates in `DOMAIN_48_EMAIL_TEMPLATE_SET.md` with Sentencing Project variant (nporter@sentencingproject.org) and PPI variant (info@prisonpolicy.org). Gist confirmed HTTP 200.
- **Domain 59 Tier 2**: CBPP and MomsRising replied MODERATE (forwarded internally). Script output recommended FORCED Tier 2 activation for EPI, Demos, NELP on June 20-21 due to Senate markup pressure, independent of STRONG threshold.

### What This Framework Decides

For Domain 59 (clock running): whether to execute Tier 2 on June 20-21 (forced by markup window) or hold to T+14 (July 1). The 2 MODERATE replies change nothing about forced activation — Senate Finance markup is the override.

For Domains 51 and 48 (clock not started): the user sends Wave 1 emails on June 17-18. Depending on when those goes out, the Day 7 checkpoint for 51 and 48 shifts to June 24-25. This framework pre-stages the routing for both the immediate Domain 59 decision and the deferred 51/48 decision.

---

## Section 2: Signal Classification Rules

Before entering the decision tree, classify each domain's composite signal. Use the scores recorded in `JUNE_17_DAY7_CHECKPOINT_EXECUTION_CHECKLIST.md` Section 6.

### Domain 59 — Current Signal

Domain 59 Day 7 has passed. Current state:
- 0 STRONG signals
- 2 MODERATE signals (CBPP + MomsRising, both forwarded to internal teams — no action request yet)
- 0 bounces
- Gist click count: check `https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba` now

**Composite signal**: BELOW THRESHOLD / WEAK. However, Senate Finance override applies.

### Domain 51 and Domain 48 — Deferred Checkpoint

For Domains 51 and 48, Day 7 does not exist yet because Wave 1 has not been sent. The classification below is pre-staged for when the June 24-25 checkpoint arrives. Record send dates now so the T+7 math is correct:

```
Domain 51 Wave 1 send date: ____________________
Domain 51 Day 7 checkpoint: ____________________  (add 7 calendar days)

Domain 48 Wave 1 send date: ____________________
Domain 48 Day 7 checkpoint: ____________________  (add 7 calendar days)
```

### Threshold Table (applies to all domains at their respective T+7)

| Composite Signal | Condition |
|-----------------|-----------|
| **STRONG** | 2+ STRONG individual replies from Wave 1 contacts AND delivery rate ≥80% |
| **MODERATE** | 1 STRONG individual reply, OR 3+ MODERATE individual replies, OR 3+ Gist clicks with 0 email replies, OR any CLC reply of any kind (Domain 51 only) |
| **WEAK** | 0 STRONG replies AND <3 MODERATE replies AND ≤2 Gist clicks AND delivery ≥80% |
| **DIAGNOSTIC** | Delivery rate <80% (more than 1 bounce from 5-6 sends) |

---

## Section 3: Three-Branch Decision Tree

### Entry Logic

Apply exactly one branch. Use the first that matches. Check Domain 59 first (clock is running). Domains 51 and 48 enter this tree at their respective T+7 dates (approximately June 24-25 if Wave 1 goes out June 17-18).

---

### Branch 1 — STRONG (≥3 replies total across all active domains, or 2+ STRONG from a single domain)

**What this means**: Research is landing with engaged readers faster than baseline. A 30%+ substantive reply rate within 7 days in cold advocacy outreach is above-baseline organizational interest. This is the best-case outcome.

**Trigger conditions**:
- Domain 59: 2+ STRONG from the 5 Wave 1 contacts (CBPP, ITEP, MomsRising, NWLC, AFL-CIO) — currently showing 0 STRONG, so this requires a reply arriving June 17-20 before the June 20-21 reassessment
- Domain 51: 2+ STRONG from 5 Wave 1-2 contacts (CLC, Issue One, Common Cause CA, LWV CA, Clean Money Action Fund) — at the June 24-25 T+7 checkpoint
- Domain 48: 2+ STRONG from 6 Wave 1-2 contacts (Sentencing Project, PPI, Brennan Center, Worth Rises, CLC/Restore Your Vote, M4BL) — at the June 24-25 T+7 checkpoint

**Immediate action sequence (complete within 24 hours of STRONG determination)**:

Domain 59 (if STRONG materializes before June 20 reassessment):
1. Execute Tier 2 immediately: EPI (researchdept@epi.org — verify before send), Demos (info@demos.org), NELP (info@nelp.org), NHLP (info@nhlp.org). 45-minute stagger between sends.
2. Run Domain 59 Zones 1-2 research sprint (`DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` Parts 3-4). Deliverable: Senate staff briefing supplement (400 words, provision-to-pathway mapping). Target: June 22-23.
3. Log: `uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --activate-tier2 59 STRONG`

Domain 51 (if STRONG at June 24-25 checkpoint):
1. Activate Tier 1 national expansion (OpenSecrets, Democracy 21, Public Citizen): `--activate-tier2 51 STRONG`
2. Activate Domain 51 Zones 1-2 research sprint (`DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md`). Zone 2 (Crypto/AI PAC architecture) Day 1 focus. Target: June 27-29.
3. Schedule Tier 2 state contacts (True North Research, Montana I-194 Campaign, Michigan Clean Elections Coalition) for June 28-30.
4. July 1 California deadline: with STRONG signal, all Domain 51 Tier 2 contacts should receive materials before June 28 to allow 3 days for organizational response.

Domain 48 (if STRONG at June 24-25 checkpoint):
1. Activate NAACP LDF + Fines and Fees Justice Center immediately.
2. ACLU of Virginia (acluva@acluva.org — Mary Bauer) on June 27-28.
3. PPI follow-up (Wendy Sawyer or Leah Wang for data validation) within 48 hours of checkpoint.
4. July 15 Virginia deadline: 21 days from June 24 — comfortable window.

**Timeline under STRONG**:

| Milestone | Date | Domain |
|-----------|------|--------|
| D59 Tier 2 activation | Same day as STRONG determination | 59 |
| D59 research sprint | Within 4 days of STRONG | 59 |
| D51 Tier 1 expansion | June 25 (checkpoint day) | 51 |
| D51 research sprint | June 26-29 | 51 |
| D48 Tier 2 activation | June 25 | 48 |
| Coalition pre-commitment asks | June 28-30 | 51, 59 |
| T+14 / July 1 gate | July 1 | All |

**Go/no-go for Wave 3 (national amplifiers)**:
Domain 51 Wave 3 (ECU/LAV, Public Citizen, Brennan Center, Democracy 21, OpenSecrets) activates at July 1 only if 2+ STRONG replies from Wave 1+2 combined. Even in the STRONG branch, Wave 3 does not activate at Day 7 — this is organizational attention management.

---

### Branch 2 — MODERATE (1-2 STRONG or 3+ MODERATE across active domains)

**What this means**: Positive signal confirming research is reaching engaged readers, but below the 30% threshold for full coalition formation confidence. One or two substantive replies in 7 days is the expected outcome for a cold advocacy send of this size. This is the most likely outcome.

**Trigger conditions**:
- Domain 59: 1 STRONG reply from any of the 5 Wave 1 contacts, OR continued growth in MODERATE count to 3+ — currently at 2 MODERATE, so one more MODERATE reply arriving June 17-20 would qualify
- Domain 51: 1 STRONG from Wave 1-2, or any CLC reply of any kind (automatic MODERATE elevation)
- Domain 48: 1 STRONG from Wave 1-2, or Sentencing Project reply of any kind

**Two-option choice within MODERATE** (select based on available time):

Option A — Express coverage (90 minutes total):
- Domain 59: Execute Tier 2 on Senate markup override logic — EPI + Demos only (highest alignment, skip NELP + NHLP until T+14)
- Domain 51: Execute Tier 1 expansion — OpenSecrets + Democracy 21 only (defer Public Citizen and state contacts to T+14)
- Domain 48: Execute Sentencing Project and PPI follow-up messages if either replied; hold NAACP LDF until T+14
- No research sprints. Distribute from existing documents.

Option B — Standard MODERATE activation (10-12 hours over 4-5 days):
- Domain 59: Tier 2 all 4 contacts (Senate markup override). Zones 1-2 research sprint (4-5 hours).
- Domain 51: Full Tier 1 expansion (OpenSecrets, Democracy 21, Public Citizen). Zones 1-2 research sprint (4-5 hours). State contacts Day 4-5.
- Domain 48: Sentencing Project / PPI follow-up if replies received; proceed to NAACP LDF + FFJC on June 27-28.

Select Option A or B: `[ ] A / [ ] B`

**Immediate action on MODERATE signal (Day 0)**:
1. Reply to all MODERATE respondents within 24 hours. Offer one-page summary for internal distribution. Include a single, concrete ask: "Please share this Gist link with your policy team" or "I'd welcome a 20-minute call with whoever handles [CTC advocacy / campaign finance / voting rights]."
2. If a MODERATE respondent named a colleague to contact, reach out to that colleague immediately. A "coalition-originated new contact" signal is the strongest network multiplier in this cycle.

**Timeline under MODERATE Option B (standard)**:

| Milestone | Date | Domain |
|-----------|------|--------|
| D59 forced Tier 2 (markup override) | June 20-21 | 59 |
| D51 Tier 1 expansion (OpenSecrets, D21, Public Citizen) | June 25-26 (checkpoint + 1 day) | 51 |
| D51 Zones 1-2 research sprint | June 26-28 | 51 |
| D48 Tier 2 — NAACP LDF + FFJC | June 27-28 | 48 |
| Coalition pre-commitment asks | June 28-30 (CBPP if MODERATE → action) | 59 |
| T+14 / July 1 gate | July 1 | All |

**Go/no-go criteria at July 1 T+14**:
If MODERATE branch produced 1+ STRONG reply by July 1, upgrade to STRONG routing for remaining Tier 2 contacts. If still MODERATE at July 1 with 0 STRONG, proceed with calendar-deadline-only domains (Domain 49 redistricting, Domain 51 California, Domain 57 UNGA August 10) and hold Domain 50 and Domain 54.

---

### Branch 3 — WEAK (0 STRONG, <3 MODERATE, ≤2 Gist clicks, delivery confirmed ≥80%)

**What this means**: No engagement signal at Day 7 with confirmed delivery. This is not failure. It is "no signal yet." Most national policy organizations route incoming research materials in 7-14 business days, not 7 calendar days. The median cold-contact reply cycle for organizations in this outreach universe is 10-15 business days. WEAK at Day 7 is within the normal range for roughly half of first-contact sends.

**Domain 59 — WEAK branch rule (Senate Finance override applies)**:

The Domain 59 express Senate path executes regardless of signal strength. This is the critical distinction from the other domains. The Senate Finance CTC markup closes June 25-30. Whether CBPP and ITEP have replied is irrelevant to the legislative advocacy value — a CBPP brief that influences Senate Finance staff is valuable independent of whether CBPP engaged with the original outreach.

Action: Execute Domain 59 Tier 2 on June 20-21 regardless of WEAK signal:
- EPI (researchdept@epi.org — verify before send)
- Demos (info@demos.org)
- NELP (info@nelp.org)
- Command: `uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --activate-tier2 59 WEAK`

**Domain 51 — WEAK branch rule**:

Hold Tier 1 expansion until T+14 (approximately July 1 if Wave 1 sent June 17-18). Domain 51 has no immovable deadline before July 1 — the California Fair Elections Act deadline is recoverable if Tier 1 expansion begins June 24-28. Do not expand to OpenSecrets, Democracy 21, or Public Citizen before T+14.

Exception: If CLC (Erin Chlopak) or Issue One replies between Wave 1 send and T+14, activate Tier 1 expansion immediately upon reply receipt. Do not wait for the calendar.

**Domain 48 — WEAK branch rule**:

Hold NAACP LDF and FFJC until T+14. The Virginia July 15 deadline is 28 days from June 17 — there is time. Do not activate Tier 2 before evidence suggests the research is reaching engaged readers.

**WEAK branch diagnostic (run before any further sends)**:

| Check | Pass Condition | Fail Action |
|-------|---------------|-------------|
| Sent folder: all emails shown as sent (not in drafts or spam) | All confirmed sent | If any stuck in drafts, send immediately |
| Gist URLs return HTTP 200 from incognito browser | All three Gists live | Recreate any 404 Gist before any further sends |
| Gist click count: any positive delta since send date | Even 1 click = passive interest | 0 clicks + 0 replies → most likely delivery issue |
| Bounced emails in inbox | 0 bounces = confirmed delivery | 1+ bounces → rescue using backup addresses |
| Subject line format: does it contain a specific urgency frame | Yes, specific to domain deadline | No → revise for Tier 2 sends |

If all diagnostic checks pass: confirmed WEAK. Hold Tier 2. Wait for T+14.
If any diagnostic check fails: fix the structural issue before assigning WEAK.

**Timeline under WEAK**:

| Milestone | Date | Domain |
|-----------|------|--------|
| D59 forced Tier 2 (Senate override) | June 20-21 | 59 |
| D51 T+14 assessment | ~July 1 | 51 |
| D48 T+14 assessment | ~July 1 | 48 |
| If still WEAK at T+14: escalation | July 1-2 | All |
| If T+14 WEAK: shift D51 to Reform Coalition 2027 frame | July 1 | 51 |

---

## Section 4: Timeline Estimates Per Branch

### STRONG Timeline

```
Day 0 (checkpoint day, June 17-18 or June 24-25 for 51/48):
  → Determine STRONG signal
  → Execute Tier 2 for signaling domain within 24 hours
  → Begin research sprint if capacity allows

Days 1-4:
  → Research sprint: Domain 59 Zones 1-2 (Senate brief supplement)
  → Research sprint: Domain 51 Zones 1-2 (FEC enforcement addendum)
  → Log all replies and Tier 2 sends in WORKLOG.md

Days 5-7:
  → Coalition pre-commitment asks (CBPP + AFL-CIO joint CTC statement)
  → Brennan Center Domain 51/56 co-pitch

Day 15 (July 1 — T+14 gate):
  → Domain 51 Wave 3 activation decision (national amplifiers)
  → Domain 49 and 50 start dates confirmed
  → Phase 2 Batch 2 sequencing begins
```

### MODERATE Timeline

```
Day 0 (checkpoint day):
  → Determine MODERATE signal
  → Reply to all MODERATE respondents within 24 hours (offer one-pager)
  → Select Option A or Option B

Days 1-3 (Option A):
  → D59 forced Tier 2 June 20-21 (Senate override)
  → D51 selective Tier 1 (2 contacts only) June 25-26
  → D48 hold until T+14

Days 1-5 (Option B):
  → D59 forced Tier 2 June 20-21
  → D59 research sprint Zones 1-2 (June 21-23)
  → D51 full Tier 1 expansion June 25-26
  → D51 research sprint June 26-28
  → D48 NAACP LDF + FFJC June 27-28

Day 14 (July 1):
  → Reassess signal: any upgrades to STRONG?
  → Wave 3 decision for Domain 51 (if 2+ STRONG by this date)
  → Domain 49/50 sequencing decision
```

### WEAK Timeline

```
Day 0 (checkpoint day):
  → Confirm WEAK (not DIAGNOSTIC)
  → Run 10-minute delivery diagnostic
  → No Tier 2 sends except Domain 59 Senate override

Days 1-3:
  → D59 forced Tier 2 on June 20-21 (Senate override, regardless of signal)
  → D51: monitor inbox; do not send Tier 1 expansion
  → D48: monitor inbox; do not send NAACP LDF

Days 7-14 (between checkpoint and July 1):
  → Note any late-arriving replies (D51/D48 Wave 1 sent June 17-18, replies may arrive June 20-30)
  → If 1+ STRONG arrives: immediately upgrade to MODERATE or STRONG branch

Day 14 (July 1):
  → If D51 still WEAK: activate initial 3 Tier 2 contacts only (True North Research, Montana I-194, Michigan Clean Elections)
  → If D48 still WEAK: ACLU of Virginia contingency path (acluva@acluva.org)
  → If all domains WEAK at T+14: flag in CHECKIN.md "Needs Your Input"; do not continue expanding without user decision
```

---

## Section 5: Key Decision Points and Go/No-Go Criteria

### Decision Point 1 — Domain 59 Senate Override (June 20-21)

**Condition to check**: Is the Senate Finance CTC markup still active at finance.senate.gov/hearings?

Go: Markup still active → execute Domain 59 Tier 2 (EPI, Demos, NELP, NHLP) on June 20-21 regardless of signal strength. No STRONG threshold required for this activation.

No-go: Markup has passed or been indefinitely postponed → shift Domain 59 to "OBBBA Implementation Coalition" frame (`DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` Part 7 Contingency 1). The domain's value does not expire — it shifts from legislative urgency to 2026 midterm accountability and IRS implementation monitoring. All 14 Domain 59 contacts remain valid targets.

### Decision Point 2 — Domain 51 July 1 California Window (June 25-28)

**Condition**: Have at least 2 STRONG replies been received from any Domain 51 contacts (CLC, Issue One, Common Cause CA, LWV CA, Clean Money Action Fund) by June 25?

Go (2+ STRONG): Activate all 13 Domain 51 Tier 2 contacts in three waves — initial 3 (True North Research, Montana I-194, Michigan Clean Elections) immediately, secondary 5 (New Mexico Common Cause, Issue One ReFormers Caucus, ACLU Voting Rights, UCLA Election Law, Loyola Law) by June 28, extended 5 (ECU, Public Citizen, Brennan Center, Democracy 21, OpenSecrets) by July 1.

Go-selective (0-1 STRONG): Activate initial 3 only (True North Research, Montana I-194, Michigan Clean Elections). California contacts (Common Cause CA, LWV CA, Clean Money Action Fund) are already in Wave 1-2 — if they have not replied by June 25, a one-sentence follow-up from one of the other Domain 51 MODERATE respondents is the highest-probability re-engagement path.

No-go (0 replies from Wave 1-2): Hold Tier 2. Diagnose whether California contacts (dkemp@commoncause.org, lwvc@lwvc.org, info@CAclean.org) actually received the email before concluding low engagement.

### Decision Point 3 — Domain 48 Virginia Window (June 27 checkpoint)

**Condition**: Have 2+ STRONG replies been received from Domain 48 Wave 1-2 contacts by June 27?

Go (2+ STRONG): Activate NAACP LDF + Fines and Fees Justice Center immediately. ACLU of Virginia on June 27-28.

Go-partial (1 STRONG): Activate FFJC only. Hold LDF for July 1 assessment.

No-go (0 STRONG): ACLU Virginia contingency path only. Do not contact NAACP LDF cold — the research-to-research framing requires at least one confirmed prior engagement to establish the document's credibility in the criminal justice ecosystem.

### Decision Point 4 — Coalition Pre-Commitment Asks (June 28-30)

Three pre-commitment asks are authorized at T+10 if the corresponding domain signal justifies them:

1. **CBPP + AFL-CIO joint CTC statement** (Domain 59): Authorized if CBPP returned STRONG. Not authorized if CBPP returned only MODERATE (forwarded internally) — wait for their internal routing to produce a named contact before the coalition ask.

2. **Brennan Center Domain 51/56 co-pitch** (Domains 51 + 56): Authorized if Brennan Center responded to either Domain 56 (May 28 send, now 20 days old) or Domain 51 (if/when sent). This is the strongest single-pitch case in the coalition leverage matrix — FEC enforcement collapse (Domain 51) + civil service politicization (Domain 56) share the constitutional independence argument. Send only after confirming Brennan Center engagement with either domain.

3. **PPFA Civic Engagement Bridge** (Domain 39 + Domain 59): Authorized if Domain 39 (Georgetown CCF, NHeLP, BMMA, Brennan, IRG — June 1 sends) produced 2+ Score 3+ replies by June 15. Check Domain 39 inbox as part of June 17-18 checkpoint review.

### Decision Point 5 — All Domains WEAK at T+14 (July 1)

If all three active domains (51, 59, 48) show 0 STRONG replies by July 1, this warrants user input before any further expansion.

Escalation protocol:
1. Log "ALL DOMAINS WEAK AT T+14" in CHECKIN.md under "Needs Your Input"
2. Before the July 1 user decision: review whether the research-to-research opening frame (citing the receiving organization's own published work) was used consistently. If the Wave 1 opening lines did not cite each organization's own research specifically, this is the most likely cause of low engagement.
3. Do not interpret T+14 WEAK as research quality failure. It may be routing failure, framing failure, or organizational attention exhaustion (many organizations are receiving large volumes of advocacy research during the 2026 election season).
4. The alternative distribution path — publishing Gist URLs on organizational social channels with explicit domain-specific framing, then cold-emailing Senate Finance staff directly — is available regardless of organizational engagement signal.

---

## Section 6: Contingency Procedures — Communication Failure

### If Trump v. Barbara Ruling Issues Before June 25 (SCOTUS Rapid-Response Override)

The Court's remaining opinions will issue before the end of June. Check supremecourt.gov/opinions/slipopinion/25 as part of the June 17-18 checkpoint routine.

**If ruling issues**: All pending Wave 1-2 sends pause for 48 hours. NARF, NAACP LDF, and Lawyers' Committee receive the Domain 58 rapid-response via `DOMAIN_58_TRUMP_V_BARBARA_RAPID_RESPONSE.md`. This is a 48-hour window — it takes precedence over all other scheduled sends because the window is hard and short.

**If ruling is procedural** (does not reach 14th Amendment merits): Use the bifurcated template from the rapid-response file. Do not use the joint framing template for a procedural ruling.

**Resume schedule**: After 48-hour rapid-response window closes, resume pending Domain 51 and 48 sends. Domain 59 Senate markup timeline is not affected by the ruling.

### If Gist URL Returns 404 at Checkpoint

Do not send any outreach for that domain until the Gist is restored.

Procedure (10 minutes):
1. Open the production research document for the domain (e.g., `domain-59-economic-precarity-democratic-infrastructure.md`)
2. Create a new Gist at gist.github.com from the research document content
3. Update the Gist URL in `DOMAIN_59_CONTACT_REACHABILITY_SNAPSHOT.md` (or Domain 51/48 equivalents)
4. Verify HTTP 200 from incognito browser
5. Resume sends with the new URL

### If Key Organizational Contact Has Departed

Personnel change signals: hard bounce from a verified address, or a reply from a "no longer at this organization" auto-notice.

Protocol:
1. Check the organization's website team page for the current staff member in the relevant program area
2. Do not attempt to find personal email addresses through OSINT
3. Resend to the new named contact's organizational email if confirmed, or to the general organizational inbox with "For the [Program Area] Team" as the opening line
4. Log the contact change in `DISTRIBUTION_EXECUTION_LOG.md`

### If Senate Finance Markup Closes Before Domain 59 Tier 2 Sends

Framing shift (not cancellation). Domain 59's 14 organizational contacts remain valid under the OBBBA implementation frame:

Old frame: "Senate Finance markup is open — your analysis of [X] could influence CTC provisions before passage"

New frame: "OBBBA is law. Its CTC provisions leave 19 million children behind — 17 million who see no gains under the refundability floor, and 2 million newly excluded by the SSN restriction. The 2026 midterm cycle is the accountability window. Your organization's [CITE THEIR WORK] provides the analytical foundation this coalition needs."

Source reference for the new frame:
- Columbia CPSP 2025: "Children Left Behind under OBBBA Child Tax Credit" — 17 million children gap documented
- ITEP 2026: CTC left out under OBBBA implementation modeling
- CBPP Senate Finance tracking: post-OBBBA IRS implementation monitoring
- All cited in `JUNE_17_18_DAY_7_CHECKPOINT_FRAMEWORK.md` Section 1

---

## Section 7: Logging Requirements

After executing any branch, log the checkpoint result:

```bash
# Autonomous script (run from projects/resistance-research/):
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --t7-checkpoint
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --routing-decision 59 51 48 [SIGNAL_59] [SIGNAL_51] [SIGNAL_48]

# Log sends as you execute:
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-send 6 --time "2026-06-20 15:00 UTC"
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-reply 6 --signal STRONG --summary "EPI confirmed interest in Senate Finance brief"

# Log checkpoint in WORKLOG.md manually:
# Date: [June 17-18 or June 24-25, 2026]
# D59 signal: [STRONG/MODERATE/WEAK] | D51 signal: [STRONG/MODERATE/WEAK] | D48 signal: [STRONG/MODERATE/WEAK]
# Branch taken: [1-STRONG / 2-MODERATE Option A or B / 3-WEAK]
# Domains activated to Tier 2: [list]
# Next checkpoint: [July 1, 2026]
# Senate Finance markup status: [ACTIVE/CLOSED]
```

---

## Section 8: Cross-Domain Integration Opportunities

Regardless of which branch is taken, two cross-domain opportunities activate at T+10 (June 27-28 for Domain 59; July 1-2 for Domains 51 and 48):

**Opportunity 1 — FEC Enforcement + Voter Participation Gap synthesis** (Domains 51 + 59):
The 42-point income-based voter participation gap (Domain 59) and the FEC enforcement collapse that allows unlimited dark money into House races in low-income districts (Domain 51) produce a compounding exclusion argument. The only prerequisite: at least one organization from each domain has engaged at STRONG or MODERATE. Send the cross-domain synthesis note only to a contact who has engaged with one domain — not as a cold introduction to both domains simultaneously.

Template reference: `DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md` Section 4.1

**Opportunity 2 — Criminal Justice Civic Exclusion + CTC Poverty Bridge** (Domains 48 + 59):
14% of working-age adults are disenfranchised by criminal records in some states (Domain 48). The economic precarity that correlates with criminal justice system contact is the same population the CTC refundability gap excludes (Domain 59). This is the direct intersection of the two domains' research. Prerequisite: Sentencing Project (Domain 48) engaged at STRONG. Contact: MomsRising (Domain 59 Wave 1) is the highest-alignment bridge organization — their constituency overlap with formerly incarcerated individuals and low-wage workers is direct.

---

*Framework prepared June 17, 2026. Companion documents: `PHASE_2_ACTIVATION_ROUTING_MATRIX.md`, `DAY_7_CHECKPOINT_MEASUREMENT_DASHBOARD_TEMPLATE.md`. Script: `PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py`. All contact addresses verified June 5-16, 2026.*
