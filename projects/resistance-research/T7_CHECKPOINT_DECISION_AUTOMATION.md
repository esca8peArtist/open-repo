---
title: "T+7 Checkpoint Decision Automation — Domain 51 Wave 1"
subtitle: "Summing Logic, Threshold Application, and Phase 2 Routing for June 16–18 Decision Gate"
created: "2026-06-05"
item: "Exploration Queue Item 84 — Deliverable 3"
status: "production-ready"
checkpoint_date: "June 16–18, 2026"
input_sheet: "Cumulative Summary (Sheet 5)"
output: "STRONG / MODERATE / WEAK determination with explicit Phase 2 routing"
cross_references:
  - PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE_DOMAIN51.md
  - DAILY_SIGNAL_LOG_ENTRY_GUIDE.md
  - PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md
  - DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
---

# T+7 Checkpoint Decision Automation
## Threshold Logic, Decision Tree, and Phase 2 Routing — June 16–18

*Prepared June 5, 2026. This document answers: given the signal counts in Sheet 5 on June 16–18, what exactly is the T+7 determination and what does that determination require you to do next? No ambiguity. No judgment calls. Run the formula, get the output, execute the action.*

---

## Lead Finding

The T+7 checkpoint (June 16–18) is the Phase 2 go/no-go gate. All Phase 2 domain activation decisions — from Domain 48 preparation timing to Domain 50 urgency escalation — route through this single determination. The threshold is STRONG signals only: the count of contacts who demonstrated substantive engagement (not merely positive acknowledgment). STRONG requires ≥4 STRONG signals across 5 organizations for full Phase 2 activation; 2–3 STRONG for conditional approval; <2 STRONG for deferral.

---

## Input: Sheet 5 Signal Counts

**Pull these three numbers from Sheet 5, Cumulative Summary, at the time of T+7 assessment:**

| Cell | Metric | Formula |
|------|--------|---------|
| B4 | Total STRONG Signals | =COUNTIF('Daily Signal Log'!E:E,"STRONG") |
| B5 | Total MODERATE Signals | =COUNTIF('Daily Signal Log'!E:E,"MODERATE") |
| B6 | Total WEAK Signals | =COUNTIF('Daily Signal Log'!E:E,"WEAK") |
| B7 | Confirmed Orgs | =COUNTIF('Engagement Classification'!G:G,"Confirmed") |
| B14 | T7 Gate Status | =IF(B4>=4,"STRONG",IF(B4>=2,"MODERATE","WEAK")) |

**The decision is made from B4 (STRONG count) and B14 (gate status). Read B14 first.**

---

## Threshold Table

| B4 Value | B14 Output | Determination | Phase 2 Action |
|---|---|---|---|
| ≥4 STRONG signals | "STRONG..." | STRONG | Phase 2 full batch activation — see Path B STRONG branch below |
| 2–3 STRONG signals | "MODERATE..." | MODERATE | Conditional approval — deferred domains stay deferred; high-confidence domains advance |
| 0–1 STRONG signals | "WEAK..." | WEAK | Defer Phase 2; run root-cause analysis; retain Domain 51/59 monitoring |

**Supplementary signals that upgrade a MODERATE to STRONG (apply at T+14 if T+7 was MODERATE)**:
- Cross-domain mention: any contact mentions multiple Phase 2 domains in their reply
- Coalition forward: contact confirms they forwarded research to another organization outside the target list
- Congressional routing: any contact routes the research to a congressional office or staff member

These do not change the T+7 determination retroactively. They apply at T+14.

---

## Decision Tree

```
READ SHEET 5, CELL B4 (Total STRONG Signals)
              |
    +---------+---------+
    |                   |
  B4 ≥ 4             B4 = 2 or 3
    |                   |
  STRONG          MODERATE
    |                   |
    |           +---------+
    |           |           |
    |        2 STRONG    3 STRONG
    |           |           |
    |      Conditional  Conditional+
    |      (cautious)   (lean-active)
    |
  B4 = 0 or 1
    |
  WEAK
    |
  Run root-cause analysis
  (see WEAK branch below)
```

---

## STRONG Branch — Full Phase 2 Activation

**Threshold met**: B4 ≥ 4 (≥4 STRONG signals across the 5 organizations)

**Context**: Four of five contacts have demonstrated substantive engagement. This means the research reached decision-makers, not just inboxes. Domain 51 is generating actionable responses from the target coalition. Phase 2 batch activation proceeds at Path B STRONG tempo (from PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md Section 6, Checkpoint 2).

### Immediate Actions (within 24 hours of STRONG determination)

1. Update CHECKIN.md: enter "T+7 Determination: STRONG — [date]. STRONG signal count: [B4]. Confirmed orgs: [B7]. Phase 2 Path B STRONG variant activated."

2. Update Sheet 4 (Decision Checkpoint Record) Row 2: enter determination, signal counts, and Phase_2_Action.

3. Domain 48 (Criminal Justice): Begin Gist creation and contact verification for July 10–20 Tier 1 sends. Preparation starts June 25 per STRONG path. Note in Sheet 7 Row 8: update T7_Activation_Status to "ACTIVATE."

4. Domain 49 (Environmental Justice): Begin preparation track July 1 — not immediately, but the path is green. Note in Sheet 7 Row 9: update T7_Activation_Status to "ACTIVATE — PREP."

5. Domain 50 (LGBTQ+ Rights): Begin preparation track July 1. August 1 deadline is fixed regardless of signal — STRONG determination confirms this track is active. Note in Sheet 7 Row 10: update T7_Activation_Status to "ACTIVATE — PREP."

6. Social proof integration: Pull the verbatim STRONG replies from Sheet 1 and compile a 2–3 sentence social proof summary for use in Domain 48, 49, and 50 outreach templates. Format: "Campaign Legal Center's Erin Chlopak [or equivalent] engaged with the research and [specific action]. Issue One's research team [specific action]." Named responders from credentialed organizations materially increase opening probability for Phase 2 contacts.

7. Domain 51 Tier 2 contacts: With STRONG signal, activate the Tier 2 contact list from DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md Section 6. June 19–30 is the Tier 2 window. Priority order: Issue One Advisory Board (if Issue One was one of the STRONG signals) > OpenSecrets / CRP > Montana Plan I-194 campaign (if Montana is now on signature track) > Michigan Clean Elections Coalition.

### Per-Domain Signal Implications at STRONG

**Which domains got STRONG signals from their target contacts?**

At STRONG, reconstruct the per-org breakdown from Sheet 5's per-organization table (rows 17–22):

- CLC STRONG: Confirms Domain 51 FEC enforcement / campaign finance angle is resonating with legal advocacy organizations. Domain 48 outreach to Brennan Center Justice Program and NAACP LDF (who also engage FEC analysis) should lead with the dark money-to-civic-exclusion connection, not just Domain 48 in isolation.

- Issue One STRONG: Confirms bipartisan reform framing is working. Domain 57 (Multilateral Withdrawal) outreach to CFR and Senate Foreign Relations staff can reference Issue One's engagement — "organizations including Issue One's policy research team have engaged the framework."

- Common Cause CA STRONG: Direct California ballot campaign integration signal. This is the highest-leverage Domain 51 outcome for July advocacy. Confirms that the CA Fair Elections Act messaging window is open and research is reaching campaign decision-makers.

- LWV CA STRONG: Voter education use case confirmed. LWV's voter guide distribution network is a secondary amplification channel. If LWV CA is STRONG, request their newsletter or voter guide format guide and prepare an excerptable version of the Domain 51 Executive Summary specifically for LWV distribution.

- Clean Money STRONG: Unexpected high-value signal. Clean Money's ballot campaign execution arm is engaging — this means the research is influencing active campaign infrastructure, not just policy discussion. Priority escalation: ask Clean Money explicitly what format is most useful for their June–July campaign.

**Cross-domain feedback — do contacts mention multiple domains?**

At STRONG signal levels, check each STRONG reply in Sheet 1 for multi-domain mentions:

- If any contact mentions Domain 59 economic precarity / Senate Finance: log as cross-domain mention, flag as potential coalition bridge (AFL-CIO contacts who care about both campaign finance and CTC are a high-value multiplier)
- If any contact mentions Domain 48 criminal justice / felon disenfranchisement: log as cross-domain mention, use as social proof in Domain 48 outreach specifically framing the dark money connection
- If any contact mentions redistricting or voting rights beyond Domain 51: flag for Domain 1 or Domain 37 follow-up

**Resource reallocation at STRONG**:

Phase 2 remains on Path B schedule. No reallocation of freed-up hours is needed at STRONG — all domains proceed on their documented timelines with preparation advancing 7 days earlier than MODERATE/WEAK paths. The agent hours that would have gone to root-cause analysis at WEAK are instead used for Domain 48 Gist preparation (June 25 start).

---

## MODERATE Branch — Conditional Phase 2 Approval

**Threshold met**: B4 = 2 or 3 (2–3 STRONG signals across 5 organizations)

**Context**: Research reached decision-makers at approximately half the target organizations. The distribution is working but not at saturation. Phase 2 proceeds on Path B standard tempo — no acceleration, no deceleration. The June 9–12 execution was not a failure; the measurement is simply mid-range.

### Sub-variant: 2 STRONG signals (B4 = 2)

This is the lower end of MODERATE. The two STRONG signals are likely the Tier A organizations (CLC and Issue One), which have the highest expected response rates. Tier B and C organizations have not yet engaged substantively.

**Actions**:
1. Update CHECKIN.md: "T+7 Determination: MODERATE (low end). STRONG signals: 2. Path B maintained at standard tempo."
2. Domain 48: Gist creation and preparation begins July 1 as planned (not accelerated to June 25).
3. Domain 49 and 50: Preparation begins July 15 (one week later than MODERATE+). Compile any available social proof from the 2 STRONG replies before July 15 send prep begins.
4. Continue monitoring at T+14 — there may be late replies from Tier B contacts that upgrade the determination.
5. Do not activate Tier 2 contacts from DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md Section 6 yet. Wait for T+14 to confirm signal trajectory.

### Sub-variant: 3 STRONG signals (B4 = 3)

This is the upper end of MODERATE, leaning toward STRONG. Three of five organizations are confirmed.

**Actions**:
1. Update CHECKIN.md: "T+7 Determination: MODERATE (high end). STRONG signals: 3. Evaluating Path B vs. STRONG acceleration at T+14."
2. Domain 48: Assess which of the 3 confirmed STRONG orgs are most relevant to the Domain 48 dark money connection. If CLC is STRONG and their reply references enforcement action, begin Domain 48 preparation June 28 (3 days ahead of standard July 1 start). If the 3 STRONG signals are Tier B/C orgs, maintain July 1 start.
3. Domain 49 and 50: Preparation begins July 1 as planned.
4. Use the 3 STRONG replies as social proof in Domain 48 Tier 1 outreach — name the organizations explicitly ("Campaign Legal Center and two California ballot campaign organizations have engaged the research").
5. Activate Tier 2 contacts for Domain 51 — the June 19–30 window is open. Prioritize OpenSecrets/CRP and Issue One Advisory Board.

### Deferred Domains at MODERATE

At both MODERATE sub-variants:
- Domain 57 (Multilateral Withdrawal): Fixed to August 10 regardless. MODERATE determination does not change this.
- Domain 58 (Tribal Sovereignty): Rapid-response standby. MODERATE determination does not change this.
- Domain 54 (Youth Civic Power): September–October timeline not affected.

### What Counts as MODERATE at T+7 Specifically

The MODERATE determination at T+7 is based on STRONG signals only — not on MODERATE or WEAK signals. Two contacts with only MODERATE signals (positive but non-committal) is not equivalent to one contact with a STRONG signal in Phase 2 decision logic. The rationale: MODERATE signals (routing acknowledgments, general expressions of alignment) do not predict operational use of the research. STRONG signals (substantive engagement, forwarding with context, request for meeting) predict Phase 2 reception.

---

## WEAK Branch — Defer and Diagnose

**Threshold met**: B4 ≤ 1 (0 or 1 STRONG signals across 5 organizations)

**Context**: The research has not demonstrably reached decision-makers who found it actionable. This does not mean distribution failed — it means the engagement data does not yet support confident Phase 2 batch activation. Root-cause diagnosis is required before activating new domains.

**Important**: WEAK at T+7 does not mean Phase 1 failed. Domain 51 and Domain 59 continue regardless. The T+7 WEAK path defers new activations while protecting the executing domains and investigating why engagement is below threshold.

### Step 1: Root-Cause Diagnosis (before any Phase 2 decision)

Run through this checklist within 48 hours of WEAK determination:

**Infrastructure check (can identify mechanical failures)**:
- Was the Gist URL accessible on June 9? Re-test now: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
- Did any send produce a delivery failure notification? Check sent-mail folder for bounce-back emails
- Is the Bitly click count consistent with zero — or is Bitly simply not tracking? Verify by clicking your own Gist link and confirming it registers in Bitly within 5 minutes
- Did the emails arrive in recipients' inboxes or were they filtered to spam? (No way to confirm directly, but organizational email firewalls may block external email with GitHub links — note if the Gist URL is embedded directly versus shortened via Bitly)

**Timing check (can identify non-engagement vs. low-priority engagement)**:
- Were all 5 sends sent in the correct UTC windows per DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md?
- Are any Tier B/C organizations known to have out-of-office periods that extend beyond June 16? (Darius Kemp's OOO was already noted; if OOO extends, mark PENDING not WEAK)
- Is it possible that replies arrived in a spam folder or incorrect Gmail label?

**Messaging check (can only be evaluated against prior outreach data)**:
- Compare Domain 51 outreach template subject lines against subject lines that generated STRONG signals in prior distribution cycles (Domains 39, 56 data in DISTRIBUTION_EXECUTION_LOG.md)
- Is the Domain 51 Gist link in the email template clickable as a hyperlink, or does it appear as raw text? Raw text links in some email clients do not register as Bitly clicks

### Step 2: If Infrastructure Gap Identified

If root-cause shows an infrastructure problem (bounce, Gist URL inaccessible, spam filter), execute the relevant contingency:
- Bounce: re-send to alternate address; log in Sheet 6 Contingency Trigger Log
- Gist URL inaccessible: create a PDF fallback; re-send with PDF attachment or alternative hosting URL
- Spam filter: re-send from a different sender domain; remove GitHub link; include document as PDF attachment

After mechanical fix: do not re-run T+7 determination. Wait for T+14 (June 23–25) with the corrected distribution and re-assess at that checkpoint.

### Step 3: If No Infrastructure Gap (Messaging or Timing Issue)

If all infrastructure checks pass and engagement is genuinely low, the WEAK determination stands. Execute the following:

1. Update CHECKIN.md: "T+7 Determination: WEAK. STRONG signal count: [B4]. Root-cause: [infrastructure gap / messaging / timing / unknown]. Deferring Phase 2 batch activation pending T+14 reassessment."

2. Update Sheet 4 Row 2 with WEAK determination and root-cause notes.

3. Update Sheet 7 (Phase 2 Batch Readiness): For Domain 48, 49, 50 — update T7_Activation_Status to "DEFER"; add notes per the WEAK routing below.

4. Do NOT halt Domain 51 Wave 2 follow-up. If Wave 2 CA follow-up (June 15 per DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md Section 4 Wave 3) has not been sent, send it. WEAK engagement from the initial send does not make the follow-up less appropriate — it makes it more necessary.

5. Do NOT halt Domain 59. Senate Finance CTC markup closes June 30 — this is a fixed external deadline that does not wait for engagement data.

### Phase 2 Actions at WEAK

| Domain | WEAK Action | Revised Timeline |
|---|---|---|
| Domain 48 — Criminal Justice | Defer Gist creation to July 15 (not July 1). Revise email templates using root-cause findings before any sends. M4BL Policy Table contact has no dependency on Domain 51 signals — their response rate is independent; do not over-apply Domain 51 WEAK to Domain 48 expectations. | Gist: July 15; T1 sends: July 25–August 1 |
| Domain 49 — Environmental Justice | Defer preparation to August 1 (not July 1). Climate Justice Alliance contact strategy is independent of Domain 51 coalition. Root-cause analysis findings about messaging apply only if Domain 49 uses similar template structure. | Prep: August 1; T1 sends: August 15–25 |
| Domain 50 — LGBTQ+ Rights | August 1 deadline is immoveable. Even at WEAK, begin Domain 50 preparation by July 15 to protect the ballot campaign integration window. WEAK does not grant permission to miss this deadline. | Prep MANDATORY by July 15; T1 sends: July 25–August 1 |
| Domain 57 — Multilateral | No change. August 10 fixed. WEAK determination does not affect this domain's fixed-date send. | August 10, unchanged |
| Domain 58 — Tribal | No change. Rapid-response standby. | Ruling-triggered, unchanged |
| Domain 51 Tier 2 | Do not activate Tier 2 contacts. Wait for T+14 re-assessment. If T+14 shows any STRONG signal from the June 15 CA follow-up, Tier 2 may still be activatable within the June 19–30 window. | Conditional on T+14 |

### Resource Reallocation at WEAK

The agent hours that would have gone to Domain 48 Gist preparation (June 25) and Domain 49/50 preparation (July 1) are now freed for:

1. Root-cause analysis documentation (1 hour): write findings in CHECKIN.md explaining what happened and what was changed
2. Template revision for Domain 48 (2 hours): revise outreach templates using findings from root-cause analysis; if messaging gap identified, test revised framing on Domain 48 using lessons from what (if anything) did generate engagement in Domain 51
3. Domain 51 supplementary research (2 hours): if the Gist view count is zero but there are no infrastructure gaps, the research may not be landing as novel to these organizations. Consider adding a June 2026 update section to the Domain 51 Gist specifically for the California contacts — new data on Montana ballot initiative qualification, AI PAC formation second wave, any DISCLOSE Act committee developments

---

## T+7 Quick Reference Card

**Run the assessment on June 16, 17, or 18 (any of the three days is acceptable).**

1. Open Google Sheet → Cumulative Summary (Sheet 5)
2. Read cell B4 (Total STRONG Signals)
3. Read cell B14 (T7 Gate Status text)
4. Match to branch:
   - B4 ≥ 4 → STRONG → activate Phase 2 full batch
   - B4 = 2–3 → MODERATE → maintain Path B standard tempo; activate Tier 2 Domain 51 contacts
   - B4 ≤ 1 → WEAK → root-cause diagnosis; defer batch activation; retain Domain 51/59 monitoring

5. Update Sheet 4 (Decision Checkpoint Record) Row 2 with determination and action
6. Update Sheet 7 (Phase 2 Batch Readiness Matrix) column F for all domains
7. Update CHECKIN.md with one-line T+7 determination entry
8. If STRONG or MODERATE: compile social proof summary from STRONG replies for use in Phase 2 templates

**Total time for T+7 assessment: 20–30 minutes.**

---

## Secondary Signal Interpretation

### Gist Clicks Without Replies

Gist clicks (Sheet 5, Row 12) are a secondary signal — they confirm the link was opened but not that the research influenced any decision. At T+7, use Gist clicks as a modifier:

- High Gist clicks (≥5 total across all organizations, from Sheet 5 Row 12) with low STRONG count: suggests delivery worked but content did not generate reply-level engagement. This points to a messaging gap, not an infrastructure gap. Organizations read the research but did not feel compelled to respond. Consider a follow-up that specifically asks a question ("Does the Hawaii SB 2471 model apply to the California context?" to Common Cause CA) rather than a general sharing message.

- Low Gist clicks (< 5) with low STRONG count: suggests either delivery failure or spam filtering. Infrastructure diagnosis takes priority.

- High Gist clicks (≥5) with high STRONG count (≥4): confirms the engagement is genuine and traceable to the research content. Use click data to reinforce the Phase 2 social proof ("the research generated significant engagement from target organizations").

### MODERATE Signals and Their T+7 Weight

MODERATE signals do not count toward the STRONG threshold. However, they carry information:

- 4+ MODERATE signals with 1 STRONG: not a MODERATE determination (B4 = 1, so WEAK branch). But: 4 MODERATE signals means 4 organizations received the research and responded positively. At T+14, these MODERATE contacts may convert to STRONG — a follow-up that specifically asks for a meeting or requests a specific use case is appropriate for any organization currently at MODERATE.

- 2 STRONG + 3 MODERATE (B4 = 2, MODERATE determination): the three MODERATE orgs are actively tracking the research. Phase 2 begins at standard tempo. By T+30, some MODERATE signals may have converted. Domain 51 Tier 2 contact window (June 19–30) should be used to generate one additional STRONG signal if possible, upgrading the T+30 determination.

### What the Domain 51 Signal Implies for Each Phase 2 Domain

**Domain 48 (Criminal Justice / Civic Exclusion)**:
CLC STRONG signal is the most directly transferable to Domain 48. CLC litigates both campaign finance cases and voting rights cases. A CLC staffer who engaged Domain 51 FEC enforcement analysis is likely familiar with Domain 48's LFO / poll tax argument. The social proof sentence for Domain 48 outreach to Brennan Center: "Campaign Legal Center's campaign finance team engaged the research, which documents the dark money architecture funding opposition to felony disenfranchisement reform."

Issue One STRONG signal transfers to Domain 48 via their bipartisan reform mandate. Issue One's ReFormers Caucus includes former elected officials who have sponsored criminal justice reform legislation. An Issue One engagement in Domain 51 can open a bridging conversation: "Is your advocacy network engaged in the civic exclusion angle in Domain 48?"

Common Cause CA STRONG signal transfers weakly to Domain 48 — their primary focus is ballot initiatives in California. However, if Common Cause CA is running any criminal justice-adjacent ballot measures in 2026 (which is possible — California has had multiple felony disenfranchisement measures), the dark money connection is directly relevant. Check Common Cause CA's current California campaign portfolio before Domain 48 sends.

**Domain 49 (Environmental Justice)**:
No direct signal transfer from Domain 51 contacts to Domain 49 coalition. Climate Justice Alliance, WE ACT, Earthjustice, and IEN are entirely separate networks. The Domain 51 T+7 signal should not be used to predict Domain 49 reception. Each domain's coalition is independent.

**Domain 50 (LGBTQ+ Rights)**:
Lambda Legal and AT4E have worked on campaign finance cases. Any CLC or Issue One STRONG signal that references the AI PAC argument may be useful in Domain 50 framing — AI industry PACs have funded anti-LGBTQ+ candidates through intermediary committees. If CLC or Issue One engaged the AI PAC section specifically, note this in Domain 50 template preparation.

**Cross-domain feedback rule**: If any T+7 STRONG reply from any organization mentions a domain other than Domain 51 — redistricting, voting rights, criminal justice, healthcare, anything — log it as a separate NOTE row in Sheet 1 with Signal_Code: N/A and Notes: "Cross-domain mention: [domain referenced] — potential bridge for Phase 2 outreach."

---

*Prepared June 5, 2026. Threshold sources: PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 5 (Day 7 Checkpoint thresholds), PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md Section 6 (Checkpoint 2, Strategic Pivot Gate), DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md Section 6 (Tier 2 activation conditions). Phase 2 domain sequencing: PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md Section 7 (Gantt Timeline, Path B).*
