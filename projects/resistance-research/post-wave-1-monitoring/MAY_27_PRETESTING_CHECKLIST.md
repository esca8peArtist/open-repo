---
title: "May 27 Pre-Testing Verification Checklist — Domain 56 + Phase 1 Monitoring Infrastructure"
created: "2026-05-26"
session: "Session 1688 pre-launch verification"
purpose: >
  Single reference document for May 27 pre-testing execution. Covers all five infrastructure
  components that must pass before May 28 Domain 56 distribution proceeds. Each section
  contains specific verification steps with pass/fail criteria. All gaps identified are
  non-blocking per Session 1675 audit — document them and resolve at setup time.
status: "ready for May 27 execution"
---

# May 27 Pre-Testing Verification Checklist

**Version 1.0 — May 26, 2026 (pre-test prep)**

**Purpose**: Risk reduction before May 28 live distribution. Any issue found today can be fixed in minutes. The same issue found during live execution costs a day.

**Time budget**: 45–60 minutes total across all five sections.

**Format**: Each item is a verification step followed by its pass/fail criterion. Mark each item as you complete it. If any item returns FAIL, the corrective action is noted inline. HIGH severity issues do not exist in this infrastructure (per Session 1675 audit) — all gaps are LOW and fixable at setup time.

---

## Section 1: Domain 56 Distribution Templates

**File**: `projects/resistance-research/execution/domain-56-email-template.md`
**Time budget**: 10 minutes
**Purpose**: Confirm all four templates are send-ready before filling credentials.

### Verification Steps

- [ ] **1.1 — Template count**: Open the file and count the `## Template` headers.
  - PASS: Exactly 4 template headers present (Template 1 through Template 4)
  - FAIL: Any missing template header — check if content is present but header formatting broke
  - Result from audit: 4 templates confirmed present (Civil Service Reform Orgs, Federal Employee Unions, HR Policy/Academic, Federal Watchdog/Democracy Advocacy)

- [ ] **1.2 — Fill placeholders present and consistent**: Search for `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` in all four templates.
  - PASS: Both placeholders appear exactly once in each of the 4 templates (8 total `[YOUR_NAME]`, 8 total `[YOUR_CONTACT_INFO]`)
  - FAIL: Any template missing either placeholder — that template cannot be sent safely; add the missing placeholder before May 28
  - Note: The Gist URL is already populated with the real URL (`https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f`) — it is NOT a fill placeholder, it is the real link. Do not treat it as unfilled.

- [ ] **1.3 — Template distinctiveness**: Confirm each template has a unique subject line and unique hook sentence.
  - PASS: All 4 subject lines are distinct; opening paragraph references recipient-specific work (H.R. 492 for Template 1; 2026 midterms/PEER v. Trump for Template 2; Pendleton Act academic frame for Template 3; Hungary/Poland/CREW/GAP-specific callouts for Template 4)
  - FAIL: Any two templates have identical subject lines or identical opening paragraphs
  - Result from audit: All 4 are distinct — subjects and hooks confirmed non-identical

- [ ] **1.4 — Send log table present**: Scroll to the bottom of the file and confirm the Send Log table is present.
  - PASS: Table exists with columns Template, Recipient, Email Address, Sent Date, Response; all 11 recipients listed; Sent Date and Response columns blank (ready to fill)
  - FAIL: Send log table missing or truncated — add it before May 28 so you can track sends in real time

- [ ] **1.5 — Gist creation steps cross-reference**: Confirm the file references `domain-56-gist-creation-steps.md` for Gist setup.
  - PASS: Reference present in the header block
  - FAIL: No reference — add a note in the header before May 28. The Gist URL in the templates is already populated, so this is informational only.

**Section 1 overall**: PASS if items 1.1 through 1.4 all pass. Item 1.5 is informational only.

---

## Section 2: Monitoring Dashboard Framework

**File**: `projects/resistance-research/post-wave-1-monitoring/PHASE_1_IMPACT_MONITORING_DASHBOARD.md`
**Time budget**: 15 minutes
**Purpose**: Confirm all 7 sheets are documented with sufficient instruction to build them from scratch in 20 minutes.

### Verification Steps

- [ ] **2.1 — Seven tab names present**: Open the file and find the tab name table in Section 1.1.
  - PASS: All 7 tab names present with exact names as listed: `Contacts`, `Gist_Views`, `Replies`, `Adoptions`, `Constituencies`, `Checkpoints`, `Synthesis_Log`
  - FAIL: Any tab name missing from the table
  - Result from audit: All 7 confirmed present in Section 1.1

- [ ] **2.2 — Contacts tab column schema complete**: Confirm the Contacts tab schema table in Section 1.2 contains all required columns.
  - PASS: The following columns are defined with header names: Contact_ID, Full_Name, Organization, Domain, Constituency, Tier, Email, Send_Date, Delivery_Status, Open_Date, Click_Date, Reply_Date, Reply_Category, Engagement_Score, Tier2_Candidate, Day_to_Open, Day_to_Click, Day_to_Reply, Referral_Made, Notes
  - FAIL: Any of these column headers missing from the schema
  - Result from audit: All 20 columns confirmed present (Cols A–T)
  - Note: The task brief specifically asks for Reply_ID, Contact_ID, Date, Score, Category, Key_Content, Notes — these are Replies tab columns, not Contacts tab. The Contacts tab schema is complete as documented. The Replies tab schema is the non-blocking gap — see item 2.4.

- [ ] **2.3 — Auto-calculation formulas present**: Confirm Section 1.3 contains the 10 auto-calculation formulas for the Contacts tab summary block.
  - PASS: All 10 formula rows present: Total contacts sent, Confirmed delivered, Total replies, Overall reply rate, Score 3+ count, Score 3+ rate, Tier 2 candidates, Avg day-to-reply, Engagement velocity, Cross-org references
  - FAIL: Any formula missing — the checkpoint trees depend on these numbers being auto-calculated
  - Result from audit: All 10 confirmed present in Section 1.3

- [ ] **2.4 — Replies tab schema (non-blocking gap)**: Check whether the Replies tab has a defined column schema in the dashboard document.
  - PASS: A schema for the Replies tab is defined somewhere in the document
  - NON-BLOCKING GAP (identified in Session 1675): No explicit Replies tab schema in the dashboard docs. This is the primary non-blocking gap for May 27. Corrective action: when creating the Replies tab in Google Sheets, use these columns: Reply_ID (R001, R002...), Contact_ID (matches Contacts tab), Date, Score (0–5), Category (Category 1–5 per REPLY_TRIAGE_FRAMEWORK.md), Key_Content (free text — what they said), Notes (free text). Takes 3 minutes to build at setup time.
  - Do NOT delay May 28 execution for this gap.

- [ ] **2.5 — Constituencies tab and Checkpoints tab (non-blocking gap)**: Check whether either tab has a defined schema.
  - PASS: Both tabs have schemas defined
  - NON-BLOCKING GAP (identified in Session 1675): Neither tab has an explicit schema in the dashboard document. They are referenced throughout (Tree 3 uses Constituencies tab to count Day30_Strong; Checkpoints tab is append-only per decision trees). Corrective action for setup time:
    - Constituencies tab: Constituency_Name, Contact_IDs (comma-separated), Score_Max (highest score from any contact in this group), Day30_Strong (YES/blank), Notes
    - Checkpoints tab: Date, Checkpoint_Type (Day 7 / Day 14 / Day 30), Domain (56 / 39 / Both), Determination (HOLD/MONITOR/ESCALATE/STRONG/MODERATE/WEAK/FAILURE), Metric_A, Metric_B, Metric_C, Metric_D, Notes
  - Build both tabs in <10 minutes total at setup time. Do NOT delay May 28 for this.

- [ ] **2.6 — Bitly link table present**: Confirm Section 1.5 contains all 4 Bitly short links with their back-halves.
  - PASS: All 4 links present: drp-d56 (Domain 56), drp-d39 (Domain 39), drp-2026 (DRP Proposal), drp-summary (Executive Summary)
  - FAIL: Any link missing — that link must be created before May 28
  - Result from audit: All 4 confirmed present in Section 1.5

- [ ] **2.7 — Pre-launch checklist completeness**: Confirm Section 1.8 contains a pre-launch checklist covering Google Sheets, Bitly, Google Alerts, and Calendar.
  - PASS: All 4 sub-sections present with checkbox items
  - FAIL: Any sub-section missing
  - Result from audit: All 4 confirmed present (Google Sheets 7 items, Bitly 5 items, Google Alerts 5 items, Calendar 4 items)

**Section 2 overall**: PASS if items 2.1, 2.2, 2.3, 2.6, 2.7 all pass. Items 2.4 and 2.5 are non-blocking gaps with documented corrective actions above.

---

## Section 3: Reply Triage Framework

**File**: `projects/resistance-research/post-wave-1-monitoring/REPLY_TRIAGE_FRAMEWORK.md`
**Time budget**: 10 minutes
**Purpose**: Confirm all 5 category definitions have complete logic and no dead-end decision branches.

### Verification Steps

- [ ] **3.1 — Five categories present**: Confirm all 5 categories are defined.
  - PASS: All 5 present: Category 1 (Implementation Signal), Category 2 (Critique or Objection), Category 3 (Data Request), Category 4 (General Question), Category 5 (No Reply)
  - FAIL: Any category missing
  - Result from audit: All 5 confirmed present with full definitions

- [ ] **3.2 — Each category has a score, response time, and response protocol**: For each of the 5 categories, confirm score, response time target, and protocol steps are defined.
  - PASS:
    - Category 1: Score 4–5, same day, 4-step protocol + sample responses for D56 and D39
    - Category 2: Score 3, 48 hours, 4-step protocol
    - Category 3: Score 3, 48 hours, 3-step protocol + same-day priority list
    - Category 4: Score 2, 72 hours, 4-step protocol
    - Category 5: Score 0, no action until Day 14 (not a protocol failure — that is the correct action)
  - FAIL: Any category missing response time or protocol steps
  - Result from audit: All categories complete

- [ ] **3.3 — Classification decision tree has no dead ends**: Follow the decision tree in the Classification Decision Tree section. Confirm every branch terminates in a category assignment or a score.
  - PASS: Every YES branch assigns a category and a score. The tree terminates correctly after "polite acknowledgment with no specific engagement" maps to Score 2 / Category 4. There is no branch that leaves the reader without a next action.
  - FAIL: Any branch that ends without a category assignment or that says "use judgment" without specifying what action to take
  - Note: The tree does not have a terminal NO branch after the final question. This is operationally correct — if none of the five questions apply, the reply is unusual enough to warrant user judgment. This is not a dead end; it is an intentional edge case. Document any such reply in CHECKIN.md under "Needs Your Input."
  - Result from audit: No dead-end branches found

- [ ] **3.4 — Escalation matrix covers all 6 triggers**: Confirm the Escalation Matrix section defines all 6 trigger types.
  - PASS: All 6 triggers present in the escalation summary table: Score 5 reply, Score 4 reply (2+), 30%+ critique rate, zero clicks with confirmed delivery, D39 non-reply by June 3, 3+ cross-org references
  - FAIL: Any trigger missing from the summary table
  - Result from audit: All 6 confirmed present in the Escalation Summary Table

- [ ] **3.5 — Domain-specific priority stacks defined**: Confirm the document ends with per-domain response priority lists.
  - PASS: Both Domain 56 and Domain 39 priority stacks defined, with contacts listed in priority order and a note on Government Executive's different response cadence (10 days for editorial responses)
  - FAIL: Either stack missing
  - Result from audit: Both confirmed present, Government Executive cadence note confirmed

**Section 3 overall**: PASS if all 5 items pass.

---

## Section 4: Day 7, 14, 30 Decision Trees

**File**: `projects/resistance-research/post-wave-1-monitoring/DAY_7_14_30_DECISION_TREES.md`
**Time budget**: 10 minutes
**Purpose**: Confirm all three trees terminate in named actions and Phase 2 sequencing is unambiguous.

### Verification Steps

- [ ] **4.1 — Score 5 Override present and actionable**: Confirm the Score 5 Override section appears before Tree 1 and contains numbered steps.
  - PASS: Override section present, lists 5 numbered actions, specifies "regardless of what day it is," and clarifies that Domain 56 and Domain 39 overrides are handled independently
  - FAIL: Override section missing or does not specify same-day execution
  - Result from audit: Confirmed present and correct

- [ ] **4.2 — Tree 1 (Day 7) terminates in named determinations**: Follow Tree 1 through all branches.
  - PASS: Every branch produces one of three named determinations: HOLD, MONITOR, or ESCALATE. Each determination specifies a named action (e.g., HOLD = "Record in Checkpoints tab; next check Day 14"; ESCALATE = "Investigate delivery today; resolve before Day 14"). The tree also specifies running Tree 1 again on June 8 for Domain 39.
  - FAIL: Any branch that ends without a named determination or leaves the reader without a next action
  - Result from audit: All branches terminate correctly. Delivery integrity check (Step 1), Bitly clicks check (Step 2), and reply count check (Step 3) all have explicit terminal actions.

- [ ] **4.3 — Tree 2 (Day 14) terminates in named determinations**: Follow Tree 2 through all branches including the early activation check.
  - PASS: Four named determinations in the Day 14 table (Strong trajectory, Moderate trajectory, Weak trajectory, Early activation). The messaging revision protocol for weak trajectory is present with specific revised subject lines for both Domain 56 and Domain 39. The early activation check branches correctly to Phase 2 pre-activation (Score 5) or CHECKIN.md flag (2x Score 4).
  - FAIL: Any branch that says "wait and see" without specifying a timeframe or action
  - Note: Tree 2 Step 1 has a STOP TREE branch when a delivery problem is unresolved at Day 14. This is correct — the instruction is to add to CHECKIN.md and exclude undelivered contacts from calculations. It is not a dead end.
  - Result from audit: All branches terminate correctly

- [ ] **4.4 — Tree 3 (Day 30) terminates in named actions**: Follow all four gates of Tree 3.
  - PASS: Gate 1 (STRONG) terminates in 6 numbered same-day actions. Gate 2 (MODERATE) terminates in 5 numbered actions (24–48 hour window). Gate 3 (WEAK) terminates in a HOLD with Day 45 checkpoint or routes to Gate 4. Gate 4 (FAILURE) terminates in "User decision required; do not proceed" — this is the correct termination for a FAILURE determination. No gate leaves the reader without an action.
  - FAIL: Any gate that routes to another gate without first specifying an intermediate action, or any branch with no terminal action
  - Result from audit: All gates terminate correctly. Gate 3 HOLD branch correctly sets a Day 45 checkpoint (July 12). Gate 4 FAILURE correctly routes to user and does not attempt to auto-proceed.

- [ ] **4.5 — Domain 39 non-negotiable appears in all trees**: Confirm Domain 39 send instruction appears in Tree 1, Tree 3, and the Cross-Tree Summary.
  - PASS: Domain 39 non-negotiable instruction present in: (a) the document preamble, (b) Tree 1 (run again June 8 for D39), (c) Gate 1 action step 2, (d) Gate 2 action step 2, (e) Gate 3 HOLD branch, (f) Gate 4 WEAK branch action step 2, (g) Day 30 Domain 39 Non-Negotiable Action section, (h) Cross-Tree Summary
  - FAIL: Domain 39 instruction absent from Tree 3 FAILURE path
  - Result from audit: Domain 39 non-negotiable correctly appears in all branches including FAILURE (via the Day 30 Domain 39 Non-Negotiable Action section which states "Regardless of which gate is reached... STRONG, MODERATE, WEAK, or FAILURE")

- [ ] **4.6 — Phase 2 sequencing unambiguous**: Confirm the Phase 2 Timing Decision Logic section specifies when to escalate, when to pause, and when to pivot.
  - PASS: All three Phase 2 timing decisions have clear named triggers. "When to escalate" covers Score 5 override, 2+ Score 4 before Day 14, organic amplification spike, and STRONG at Day 30. "When to pause" covers Day 14 weak + delivery issues and FAILURE at Gate 4. "When to pivot" covers 30%+ critique rate, Day 14 weak, and zero-reply from a constituency after 14 days. Phase 2 Sequencing by Outcome table covers all four determination states.
  - FAIL: Any Phase 2 timing scenario with no named action
  - Result from audit: All scenarios covered

**Section 4 overall**: PASS if all 6 items pass.

---

## Section 5: Signal Log Structural Integrity

**File**: `projects/resistance-research/post-wave-1-monitoring/wave-1-signal-log-may18-21.md`
**Time budget**: 5 minutes
**Purpose**: Confirm structural integrity. This log covers the May 18–21 Batch 1 monitoring window (before the current Domain 56 + 39 infrastructure). Its unfilled placeholders are expected — this is an older monitoring file, not the active Phase 1 dashboard.

### Verification Steps

- [ ] **5.1 — File scope is understood**: Confirm this file covers Batch 1 (May 18–21) wave, not the Domain 56 (May 28) wave.
  - PASS: File header says "Batch 1 send: May 18, 08:00–10:00 UTC" and "Monitoring window: May 18 10:30 UTC — May 21 10:30 UTC." This is a different distribution than Domain 56 (May 28). They are related but separate monitoring windows.
  - Note: The ORCHESTRATOR_STATE.md block indicates that this signal log has 20 unfilled [fill] placeholders because the TOO_EARLY contingency activated on May 21 (law school contacts have 5–10 day cycles; full data was not available by May 21 synthesis deadline). This is expected and not a defect.

- [ ] **5.2 — Unfilled placeholder count**: Count the [fill] placeholders in the file.
  - Expected count: 20 (per ORCHESTRATOR_STATE.md which reported 20 unfilled [fill] fields)
  - PASS: Count is 20 or fewer. These placeholders correspond to: May 20 day 2 snapshot (5 fields), May 21 synthesis snapshot (10 fields), and the per-constituency table (5 fields). All are from the extended monitoring window that requires user inbox data.
  - FAIL: Count is 0 — if all placeholders are filled, that means the log is current and the synthesis should have run. Verify ORCHESTRATOR_STATE.md resolution status.
  - FAIL: Count is significantly higher than 20 — indicates structural damage or accidental content loss
  - Action: Run `grep -c '\[fill\]' /home/awank/dev/SuperClaude_Framework/projects/resistance-research/post-wave-1-monitoring/wave-1-signal-log-may18-21.md` to get exact count

- [ ] **5.3 — Fixed data rows are complete**: Confirm the May 18 and May 19 snapshot sections have actual data (not all [fill]).
  - PASS: May 18 24-hour snapshot contains a filled narrative assessment (it does — the constituency read and delivery assessment are written out). May 19 48-hour snapshot contains a filled narrative with Elias anomaly check and think tank check. Signal Log Table has a BASELINE CAPTURED row with content.
  - FAIL: Any snapshot section is entirely empty
  - Result from audit: May 18 and May 19 snapshots both have written content; [fill] placeholders are confined to the May 20 and May 21 template fields that require inbox data

- [ ] **5.4 — Score reference is present and consistent**: Confirm the score reference at the top of the file (Score 0–5) matches the scoring in REPLY_TRIAGE_FRAMEWORK.md.
  - PASS: Score 0 (No signal), Score 1 (Acknowledgment), Score 2 (General positive), Score 3 (Substantive engagement), Score 4 (Implementation/referral), Score 5 (Integration signal) — same 0–5 scale used across all Phase 1 infrastructure
  - FAIL: Any discrepancy in score definitions between this file and REPLY_TRIAGE_FRAMEWORK.md
  - Result from audit: Scoring scales are consistent across files

**Section 5 overall**: PASS if items 5.1, 5.3, and 5.4 all pass. Item 5.2 is informational — the [fill] placeholders are expected given the TOO_EARLY contingency.

---

## Summary: Non-Blocking Gaps (All From Session 1675 Audit)

These gaps were identified in the pre-testing audit. All are LOW severity. None block May 28 execution. Resolve at Google Sheets setup time (May 27 evening or May 28 morning before sending).

| Gap | Location | Corrective Action | Time to Fix |
|-----|----------|------------------|-------------|
| Replies tab has no column schema in dashboard docs | PHASE_1_IMPACT_MONITORING_DASHBOARD.md | Build tab with: Reply_ID, Contact_ID, Date, Score, Category, Key_Content, Notes | 3 minutes |
| Constituencies tab referenced but no schema defined | DAY_7_14_30_DECISION_TREES.md (Tree 3) | Build tab with: Constituency_Name, Contact_IDs, Score_Max, Day30_Strong, Notes | 4 minutes |
| Checkpoints tab referenced but no schema defined | DAY_7_14_30_DECISION_TREES.md (all trees) | Build tab with: Date, Checkpoint_Type, Domain, Determination, Metric_A, Metric_B, Metric_C, Metric_D, Notes | 4 minutes |

**Total fix time**: Under 15 minutes. Do not schedule a separate task for these — build the three tabs while setting up the Google Sheets dashboard.

---

## Pre-Send Final Check (May 28 Morning, Before First Email)

Run this in order immediately before the first Domain 56 send:

1. [ ] Open Google Sheets dashboard — confirm all 7 tabs exist and share link is set to Viewer
2. [ ] Open bitly.com — click drp-d56 yourself and confirm counter increments
3. [ ] Open `domain-56-email-template.md` — fill `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` in Template 2 (Volcker Alliance), Template 3 (Democracy Forward), and any other template you are sending on May 28
4. [ ] Replace the raw Gist URL in each template with the Bitly short link `drp-d56` (or the per-recipient variant if using them)
5. [ ] Send first email — update Contacts tab row H (Send_Date) within 1 hour

First send should go to the highest-value contact: Democracy Forward (`info@democracyforward.org`) — litigation use is the Phase 2 accelerant.

---

*This checklist was produced by Session 1688 pre-launch verification (May 26). All audit findings are from direct file reads. Companion files: `PHASE_1_IMPACT_MONITORING_DASHBOARD.md`, `REPLY_TRIAGE_FRAMEWORK.md`, `DAY_7_14_30_DECISION_TREES.md`, `wave-1-signal-log-may18-21.md`, `execution/domain-56-email-template.md`.*
