---
title: "T+7 Checkpoint Decision Automation — Domain 51 Wave 1"
subtitle: "Summing Logic, Threshold Application, and Phase 2 Routing for Day 7 Decision Gate"
created: "2026-06-05"
updated: "2026-06-14"
version: 2.0
status: production-ready
checkpoint_window: "June 17-18 (earliest) or June 21-22 (standard T+7 after June 14-15 send)"
input_sheet: "Cumulative Summary — Sheet 5, Cell B4 and B14"
output: "STRONG / MODERATE / WEAK determination with explicit Phase 2 routing"
cross_references:
  - PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md
  - DAILY_SIGNAL_LOG_ENTRY_GUIDE.md
  - DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md
  - PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
---

# T+7 Checkpoint Decision Automation
## Threshold Logic, Decision Tree, and Phase 2 Routing

*Version 2.0 — Updated June 14, 2026. This document answers: given the signal counts in Sheet 5 at the T+7 checkpoint, what exactly is the determination and what do you do next? No judgment calls. Run the formula, read the output, execute the action. Updated to reflect June 14 execution state (sends pending) and dual checkpoint window (June 17-18 as earliest possible; June 21-22 as standard T+7 after June 14-15 send).*

---

## Lead Finding

The T+7 checkpoint is the Phase 2 go/no-go gate. All Phase 2 domain activation decisions route through a single number: Cell B4 in Sheet 5 (Total STRONG Signals). The threshold is STRONG signals only. MODERATE signals do not count toward the gate — they carry qualitative information but not decision weight. STRONG requires 4+ for full Phase 2 activation; 2-3 for conditional approval; 0-1 for deferral and root-cause diagnosis.

**Checkpoint date clarification**: Given that emails were not sent before June 14, the T+7 checkpoint windows are:
- June 17-18: Use if emails went out June 10-11 (unlikely) or treat as an early-read calendar checkpoint
- June 21-22: Standard T+7 if emails go out June 14-15 (recommended)
- Run the assessment on whichever date gives you 7 calendar days from the actual send date. Do not run T+7 before Day 5 post-send — signals are still incoming.

---

## Input: Pull These Four Numbers from Sheet 5

At the time of T+7 assessment, read:

| Cell | Metric | Formula in Sheet 5 |
|------|--------|--------------------|
| B4 | Total STRONG Signals | =COUNTIF('Daily Signal Log'!E:E,"STRONG") |
| B5 | Total MODERATE Signals | =COUNTIF('Daily Signal Log'!E:E,"MODERATE") |
| B6 | Total WEAK Signals | =COUNTIF('Daily Signal Log'!E:E,"WEAK") |
| B7 | Confirmed Orgs (Status="Confirmed") | =COUNTIF('Engagement Classification'!G:G,"Confirmed") |
| B14 | T7 Gate Status (text output) | =IF(B4>=4,"STRONG — ACTIVATE PHASE 2",IF(B4>=2,"MODERATE — CONDITIONAL APPROVAL","WEAK — DEFER AND DIAGNOSE")) |

**Read B14 first. The determination is made from B4 alone. B5, B6, and B7 provide qualitative context but do not change the threshold routing.**

---

## Aggregated Signal Formulas

These formulas, already embedded in Sheet 5 Rows 17-22, give you the per-organization breakdown needed to identify which specific organizations produced STRONG signals:

```
CLC STRONG count:           =COUNTIFS('Daily Signal Log'!B:B,"CLC",'Daily Signal Log'!E:E,"STRONG")
Issue One STRONG count:     =COUNTIFS('Daily Signal Log'!B:B,"Issue One",'Daily Signal Log'!E:E,"STRONG")
Common Cause CA STRONG:     =COUNTIFS('Daily Signal Log'!B:B,"Common Cause CA",'Daily Signal Log'!E:E,"STRONG")
LWV CA STRONG count:        =COUNTIFS('Daily Signal Log'!B:B,"LWV CA",'Daily Signal Log'!E:E,"STRONG")
Clean Money STRONG count:   =COUNTIFS('Daily Signal Log'!B:B,"Clean Money",'Daily Signal Log'!E:E,"STRONG")
TOTAL STRONG (= B4):        =SUM of the five above
```

These formulas are already in the Per-Organization Signal Block (Rows 17-22) of Sheet 5. No manual entry needed.

---

## Threshold Table

| B4 Value | B14 Output | Determination | Phase 2 Action |
|---|---|---|---|
| B4 ≥ 4 | "STRONG — ACTIVATE PHASE 2" | STRONG | Full Phase 2 batch activation — see STRONG branch below |
| B4 = 2-3 | "MODERATE — CONDITIONAL APPROVAL" | MODERATE | Conditional approval — high-confidence domains advance; deferred domains stay deferred |
| B4 = 0-1 | "WEAK — DEFER AND DIAGNOSE" | WEAK | Defer Phase 2; run root-cause analysis; retain Domain 51/59 monitoring |

**Supplementary signals that can upgrade a MODERATE to STRONG at T+14 (not at T+7)**:
- Cross-domain mention: any contact references Phase 2 domains beyond Domain 51 in their reply
- Coalition forward: contact confirms they forwarded research to an organization outside the target list
- Congressional routing: any contact routes the research to a congressional office or staff member

These cannot change the T+7 determination retroactively. Apply at T+14 assessment.

---

## Decision Tree

```
READ SHEET 5, CELL B4 (Total STRONG Signals)
              |
    +---------+---------+---------+
    |                   |         |
  B4 ≥ 4             B4 = 2-3  B4 = 0-1
    |                   |         |
  STRONG          MODERATE      WEAK
    |                   |         |
    |           +---------+      Run root-cause
    |           |           |    diagnosis (see
    |        B4 = 2       B4 = 3  WEAK branch)
    |           |           |
    |       Conditional  Conditional+
    |       (cautious)   (lean-active)
    |
See STRONG branch
```

---

## STRONG Branch — Full Phase 2 Activation

**Trigger**: B4 ≥ 4 (4 or more STRONG signals across 5 organizations)

**Interpretation**: Four or five of the five contacts have demonstrated substantive engagement. The research reached decision-makers, not just inboxes. Domain 51 is generating actionable responses. Phase 2 batch activation proceeds at full tempo.

### Immediate Actions (within 24 hours of STRONG determination)

1. Update CHECKIN.md: "T+7 Determination: STRONG — [date]. STRONG signal count: [B4]. Confirmed orgs: [B7]. Phase 2 Path B STRONG variant activated."

2. Update Sheet 4 (Decision Checkpoint Record) Row for T+7: enter determination, signal counts, and Phase_2_Action.

3. Update Sheet 7 (Phase 2 Batch Readiness Matrix): for Domain 48, 49, 50 — update column F (T7_Activation_Status) to "ACTIVATE" or "ACTIVATE — PREP" per the pre-populated routing in that sheet.

4. Domain 48 (Criminal Justice / Civic Exclusion): Begin Gist creation and contact verification. Preparation timeline: 11 days after send date (approximately June 25 if sent June 14). Tier 1 sends window: approximately 25-35 days after send date (July 9-19 range). Note in Sheet 7 Row for Domain 48: T7_Activation_Status = "ACTIVATE."

5. Domain 49 (Environmental Justice): Begin preparation track approximately 17 days after send date. Not accelerated further — coalition is independent of Domain 51 contacts. Note in Sheet 7: T7_Activation_Status = "ACTIVATE — PREP."

6. Domain 50 (LGBTQ+ Rights): Begin preparation track 17 days after send date. August 1 deadline is immoveable — STRONG determination confirms this track is active on schedule. Note in Sheet 7: T7_Activation_Status = "ACTIVATE — PREP."

7. Social proof compilation: Pull verbatim STRONG replies from Sheet 1 (Daily Signal Log). Draft a 2-3 sentence social proof summary for use in Domain 48, 49, and 50 outreach templates. Format: "Campaign Legal Center's Erin Chlopak [or equivalent named person] engaged with the research and [specific action taken]. Issue One's research team [specific action]." Named responders from credentialed organizations materially increase open probability for Phase 2 contacts.

8. Domain 51 Tier 2 contacts: With STRONG signal, activate the Tier 2 contact list from DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md Section 6. The Tier 2 window opens approximately 10-15 days after the Wave 1 send. Priority: Issue One Advisory Board (if Issue One is one of the STRONG signals) → OpenSecrets / CRP → Montana Plan I-194 campaign → Michigan Clean Elections Coalition.

### Per-Organization Signal Implications at STRONG

Reconstruct which organizations produced STRONG signals from Sheet 5 Per-Organization block (Rows 17-22). The identity of the STRONG respondents determines Phase 2 social proof framing:

**CLC STRONG**: Confirms Domain 51 FEC enforcement / campaign finance angle resonates with legal advocacy organizations. Domain 48 outreach to Brennan Center and NAACP LDF should lead with the dark money-to-civic-exclusion connection. Social proof sentence: "Campaign Legal Center's campaign finance team engaged the research, which documents the dark money architecture funding opposition to felony disenfranchisement reform."

**Issue One STRONG**: Confirms bipartisan reform framing is working. Domain 57 outreach to CFR and Senate Foreign Relations staff can reference Issue One's engagement. Social proof: "Organizations including Issue One's policy research team have engaged the framework."

**Common Cause CA STRONG**: Direct California ballot campaign integration signal — the highest-leverage Domain 51 outcome. July advocacy window is open. Confirms research reaches campaign decision-makers, not just policy staff. Action: request Common Cause CA's preferred format for campaign materials.

**LWV CA STRONG**: Voter education use case confirmed. LWV's voter guide distribution network is a secondary amplification channel. Request their newsletter or voter guide format guide; prepare an excerptable version of the Domain 51 Executive Summary specifically for LWV distribution.

**Clean Money STRONG**: Unexpected high-value signal. Active ballot campaign infrastructure is engaging. Priority escalation: ask Clean Money explicitly what format is most useful for their June-July campaign.

**Cross-domain feedback at STRONG**: Check each STRONG reply for mentions of any domain other than Domain 51. Any cross-domain mention should generate a NOTE row in Sheet 1 with Signal_Code: N/A and Notes: "Cross-domain mention: [domain referenced] — potential Phase 2 bridge."

---

## MODERATE Branch — Conditional Phase 2 Approval

**Trigger**: B4 = 2 or 3 (2-3 STRONG signals)

**Interpretation**: Research reached decision-makers at roughly half the target organizations. Distribution is working but not at saturation. Phase 2 proceeds on standard Path B tempo — no acceleration, no deceleration.

### Sub-variant: B4 = 2 (Low MODERATE)

Two STRONG signals, likely the two Tier A organizations (CLC and Issue One). Tier B and C organizations have not engaged substantively yet.

**Actions**:
1. Update CHECKIN.md: "T+7 Determination: MODERATE (low end, B4=2). Path B maintained at standard tempo."
2. Domain 48: Gist creation and preparation begins at standard timeline (approximately 17 days after send date). No acceleration.
3. Domains 49 and 50: Preparation begins approximately 31 days after send date (one week later than MODERATE+ scenario). Compile social proof from the 2 STRONG replies before prep begins.
4. Continue monitoring at T+14 — Tier B contacts (Common Cause CA, LWV CA) may produce late STRONG signals that upgrade the determination.
5. Do not activate Domain 51 Tier 2 contacts yet. Wait for T+14 to confirm trajectory. The Tier 2 window (approximately Days 10-25) remains open — there is time.

### Sub-variant: B4 = 3 (High MODERATE)

Three STRONG signals — approaching STRONG threshold. Three of five organizations confirmed.

**Actions**:
1. Update CHECKIN.md: "T+7 Determination: MODERATE (high end, B4=3). Evaluating Path B vs. STRONG acceleration at T+14."
2. Domain 48: Assess which 3 organizations produced STRONG. If CLC is one and their reply references enforcement action or active litigation, begin Domain 48 preparation 4 days earlier than standard. If the 3 STRONG signals are Tier B/C organizations, maintain standard timeline.
3. Domains 49 and 50: Preparation begins at standard timeline (approximately 17 days after send date). Use 3 STRONG replies as social proof in Domain 48 outreach — name organizations explicitly ("Campaign Legal Center and two California ballot campaign organizations have engaged the research").
4. Activate Domain 51 Tier 2 contacts. The Tier 2 window is open. Priority: Issue One Advisory Board → OpenSecrets/CRP.
5. If the third STRONG signal came from Common Cause CA or LWV CA, the California ballot campaign integration signal is confirmed — treat the July 1 messaging deadline as a fixed anchor and work backward from it.

### What MODERATE Means at T+7 Specifically

MODERATE at T+7 means exactly B4 = 2 or 3 — not that you have many MODERATE signals. A result of 0 STRONG and 5 MODERATE is still WEAK by the formula. The rationale is that MODERATE signals (routing acknowledgments, general positive tone) do not predict operational use of the research. Only STRONG signals (substantive engagement, forwarding with context, meeting request, use case identification) predict Phase 2 reception.

If you have 0-1 STRONG and 3-4 MODERATE at T+7, the determination is WEAK. However: 3-4 MODERATE organizations mean 3-4 contacts received the research and responded positively. The T+14 checkpoint may see MODERATE signals convert to STRONG through follow-up. A targeted follow-up to MODERATE contacts that specifically asks for a meeting or a specific use case ("Does the Hawaii SB 2471 model apply to the California ballot context?") is appropriate before T+14.

### Deferred Domains at MODERATE

- Domain 57 (Multilateral Withdrawal): Fixed to August 10 regardless of MODERATE determination. No action at T+7.
- Domain 58 (Tribal Sovereignty): Rapid-response standby. MODERATE does not change this.
- Domain 54 (Youth Civic Power): September-October timeline not affected.

---

## WEAK Branch — Defer and Diagnose

**Trigger**: B4 ≤ 1 (0 or 1 STRONG signals)

**Interpretation**: Research has not demonstrably reached decision-makers who found it actionable. This does not mean distribution failed — it may mean delivery failed, timing was poor, or messaging did not land. Root-cause diagnosis is required before any Phase 2 batch activation.

**Important**: WEAK at T+7 does not mean Phase 1 failed. Domain 51 and Domain 59 continue regardless. The WEAK path defers new activations while protecting executing domains and investigating why engagement is below threshold.

### Step 1: Root-Cause Diagnosis (before any Phase 2 decision, within 48 hours)

Run through this checklist. Each item identifies a different type of failure. Address the identified failure type before taking any other action.

**Infrastructure check** (identifies mechanical failures):
- Is the Gist URL accessible right now? Test: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 — does it load without error?
- Did any send produce a delivery failure notification? Check sent-mail folder for bounce-back emails to each address
- Is Bitly tracking your clicks at all? Verify by clicking your own Gist link from a different device and confirming it registers in Bitly within 5 minutes
- Are the GitHub links in your emails clickable hyperlinks, or raw text? Raw text URLs in some email clients do not register as Bitly clicks (the recipient must copy-paste rather than click)

**Timing check** (identifies non-engagement vs. low-priority engagement):
- Are any Tier B/C organizations (Common Cause CA, LWV CA) known to have OOO periods extending past T+7? If yes, mark PENDING not WEAK for those organizations
- Were all 5 sends sent in the correct UTC windows? Check send logs
- Is it possible any replies arrived in a spam folder or incorrect Gmail label? Check Gmail "All Mail" search for each sender domain

**Messaging check** (can only be evaluated against prior outreach data):
- Compare Domain 51 outreach subject lines against subject lines that generated STRONG signals in prior distribution cycles (Domains 39, 56 data in DISTRIBUTION_EXECUTION_LOG.md)
- Did any prior domain's Tier 1 contacts come from campaign finance or voting rights organizations? If yes, what subject line worked there?

### Step 2: If Infrastructure Gap Identified

- Bounce: re-send to backup address immediately; log in Sheet 6 Contingency Trigger Log
- Gist URL inaccessible: create PDF fallback of Domain 51 research; re-send with PDF attachment or alternative hosting URL
- Spam filter suspected: re-send from a different sender domain; remove GitHub link; attach PDF directly
- Bitly not tracking: use GitHub authenticated view count instead; proceed with manual Gist view count method (see PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md Email Analytics section)

After mechanical fix: do not re-run T+7 determination. Wait for T+14 (approximately 14 days after actual send) and re-assess at that checkpoint with the corrected distribution.

### Step 3: If No Infrastructure Gap (Messaging or Timing Issue)

WEAK determination stands. Execute:

1. Update CHECKIN.md: "T+7 Determination: WEAK. STRONG signal count: [B4]. Root-cause: [infrastructure gap / messaging / timing / unknown]. Deferring Phase 2 batch activation pending T+14 reassessment."

2. Update Sheet 4 Row for T+7 with WEAK determination, signal counts, and root-cause notes.

3. Update Sheet 7 (Phase 2 Batch Readiness Matrix): update T7_Activation_Status to "DEFER" for Domains 48, 49; update to "CONDITIONAL — MANDATORY" for Domain 50 (August 1 deadline does not flex even at WEAK).

4. Do NOT halt Domain 51 Wave 2 follow-up. If the CA follow-up send (Common Cause CA, LWV CA re-contact) has not been sent, send it. WEAK engagement from the initial send makes follow-up more necessary, not less.

5. Do NOT halt Domain 59. External deadline (Senate Finance CTC markup) is fixed and does not wait for engagement data.

### Phase 2 Domain Actions at WEAK

| Domain | WEAK Action | Revised Preparation Start |
|---|---|---|
| Domain 48 — Criminal Justice | Defer Gist creation. Revise email templates using root-cause findings before any sends. Note: M4BL Policy Table contact is independent of Domain 51 coalition — do not over-apply Domain 51 WEAK to Domain 48 expectations. | ~31 days after send date |
| Domain 49 — Environmental Justice | Defer preparation. Climate Justice Alliance contact strategy is independent of Domain 51 coalition. | ~47 days after send date |
| Domain 50 — LGBTQ+ Rights | August 1 deadline is immoveable. Even at WEAK, begin preparation by approximately 31 days post-send to protect the ballot campaign integration window. WEAK does not grant permission to miss this deadline. | ~31 days post-send MANDATORY |
| Domain 57 — Multilateral | No change. August 10 fixed. WEAK determination does not affect this domain. | August 10, unchanged |
| Domain 58 — Tribal Sovereignty | No change. Rapid-response standby. | Ruling-triggered, unchanged |
| Domain 51 Tier 2 | Do not activate Tier 2 contacts. Wait for T+14 reassessment. If T+14 shows any STRONG signal (including from CA follow-up), Tier 2 may still be activatable within the extended window. | Conditional on T+14 |

### Resource Reallocation at WEAK

Agent hours that would have gone to Domain 48 Gist preparation and Domains 49/50 prep are freed for:

1. Root-cause analysis documentation (1 hour): write findings in CHECKIN.md explaining what happened and what was changed. Be specific about which infrastructure or messaging gap was identified.

2. Template revision for Domain 48 (2 hours): revise outreach templates using findings. If a messaging gap was identified, test revised framing using lessons from what (if anything) did generate engagement in Domain 51. If zero signals, consider a fundamentally different approach: a single-domain pitch rather than a framework overview.

3. Domain 51 supplementary research (2 hours): if Gist view count is zero but there are no infrastructure gaps, the research content may not be landing as novel. Consider adding a June 2026 update section specifically for the California contacts — new data on Montana ballot initiative qualification status, AI PAC formation second wave, any DISCLOSE Act committee developments that post-date the original research.

---

## T+7 Quick Reference Card (20-30 minute execution)

**Run the assessment on the date that is 7 calendar days from the actual Wave 1 send date.**

1. Open Google Sheet → Cumulative Summary (Sheet 5)
2. Read cell B4 (Total STRONG Signals)
3. Read cell B14 (T7 Gate Status text)
4. Match to branch:
   - B4 ≥ 4 → STRONG → activate Phase 2 full batch; social proof compilation; Tier 2 activation
   - B4 = 2-3 → MODERATE → maintain standard Path B tempo; activate Tier 2 if B4=3; monitor at T+14
   - B4 ≤ 1 → WEAK → root-cause diagnosis; defer batch activation; retain Domain 51/59 monitoring

5. Update Sheet 4 (Decision Checkpoint Record) with determination and actions
6. Update Sheet 7 (Phase 2 Batch Readiness Matrix) column F for all domains
7. Update CHECKIN.md with one-line T+7 determination entry
8. If STRONG or MODERATE: compile social proof summary from STRONG replies for Phase 2 templates

**Total time: 20-30 minutes.**

---

## Domain-Specific Signal Implications for Phase 2

### What Domain 51 Signal Predicts for Each Phase 2 Domain

**Domain 48 (Criminal Justice / Civic Exclusion)**:
CLC STRONG is the most directly transferable signal. CLC litigates both campaign finance and voting rights cases. A CLC staffer who engaged Domain 51 FEC enforcement analysis is likely familiar with Domain 48's LFO/poll tax argument. Social proof framing for Brennan Center: "Campaign Legal Center's campaign finance team engaged the research, which documents the dark money architecture funding opposition to felony disenfranchisement reform."

Issue One STRONG transfers to Domain 48 via their bipartisan reform mandate — their ReFormers Caucus includes former elected officials who have sponsored criminal justice reform legislation.

Common Cause CA STRONG transfers weakly to Domain 48 — their primary focus is ballot initiatives. Check whether Common Cause CA is running any criminal justice-adjacent California measures in 2026 before Domain 48 sends.

**Domain 49 (Environmental Justice)**:
No direct signal transfer from Domain 51 contacts to Domain 49 coalition. Climate Justice Alliance, WE ACT, Earthjustice, and IEN are entirely separate networks. Do not use Domain 51 T+7 signal to predict Domain 49 reception. Each domain's coalition is independent.

**Domain 50 (LGBTQ+ Rights)**:
Lambda Legal and AT4E have overlapping concerns with campaign finance (AI industry PACs have funded anti-LGBTQ+ candidates through intermediary committees). If CLC or Issue One engaged the AI PAC section specifically, note this in Domain 50 template preparation — the cross-domain connection is usable as social proof framing.

**Cross-domain feedback rule**: If any T+7 STRONG reply from any organization mentions a domain other than Domain 51 — redistricting, voting rights, criminal justice, healthcare, anything — log a NOTE row in Sheet 1 with Signal_Code: N/A and Notes: "Cross-domain mention: [domain referenced] — potential bridge for Phase 2 outreach."

---

## Secondary Signal Interpretation

### Gist Clicks Without Replies (Sheet 5 Row 12)

Gist clicks confirm the link was opened but not that the research influenced any decision. Use click totals as a diagnostic modifier:

- Gist clicks ≥ 5 (Sheet 5 Row 12) with B4 = 0-1: delivery worked, content did not generate reply-level engagement. Points to messaging gap, not infrastructure gap. Appropriate response: targeted follow-up asking a specific question ("Does the Hawaii SB 2471 model apply to the California ballot context?") rather than a general sharing message.

- Gist clicks < 5 with B4 = 0-1: suggests delivery failure or spam filtering. Infrastructure diagnosis takes priority over messaging revision.

- Gist clicks ≥ 5 with B4 ≥ 4: confirms genuine engagement traceable to research content. Use click data in social proof framing for Phase 2 contacts ("the research generated significant engagement from target organizations").

### MODERATE Signals and Their T+7 Weight

MODERATE signals do not count toward the STRONG threshold. However:

- 4 MODERATE signals with B4 = 1: not MODERATE determination (B4 = 1 → WEAK). But 4 MODERATE signals means 4 organizations received the research and responded positively. A targeted follow-up asking for a specific meeting or use case is appropriate before T+14.

- B4 = 2 (MODERATE) with 3 additional MODERATE: the three MODERATE organizations are actively tracking the research. Phase 2 begins at standard tempo. By T+30, some MODERATE may have converted. Use the Domain 51 Tier 2 window to generate one additional STRONG signal if possible.

---

## GO / CAUTION / NO-GO Summary

For situations where a quick verbal determination is needed before full data review:

| B4 | Verbal Determination | Action Summary |
|---|---|---|
| 4-5 | GO | Phase 2 full batch — Domains 48, 49, 50 all move; social proof ready; Tier 2 activate |
| 3 | CAUTION-GO | Phase 2 advances at standard tempo; Tier 2 activate; monitor for B4=4 at T+14 |
| 2 | CAUTION | Phase 2 standard tempo; no Tier 2 yet; wait for T+14 to confirm direction |
| 1 | CAUTION-NO-GO | Defer Phase 2 batch; run root-cause; targeted follow-up to MODERATE contacts before T+14 |
| 0 | NO-GO | Defer all batch; root-cause mandatory; messaging or delivery failure likely |

**CAUTION-GO and CAUTION are both MODERATE branch in the formula.** The verbal labels are for rapid communication. The formula-based determination (B14 in Sheet 5) is the canonical output for documentation.

---

*Version 2.0 — Updated June 14, 2026. Threshold sources: PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 5 (Day 7 Checkpoint thresholds), PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md Section 6 (Checkpoint 2, Strategic Pivot Gate), DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md Section 6 (Tier 2 activation conditions). Phase 2 domain sequencing: PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md Section 7 (Gantt Timeline, Path B).*
