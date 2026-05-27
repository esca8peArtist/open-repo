---
title: "Phase 1 Weekly Synthesis Template"
created: 2026-05-26
version: 1.1
status: production-ready
scope: >
  Copy-paste template for Monday morning weekly synthesis of Phase 1 monitoring data.
  Structured in 13 sections. Sections 1–6 are required every week (~12 minutes).
  Sections 7–13 are checkpoint-week-only or as-needed (~6 additional minutes when applicable).
  Total budget: 15–20 minutes per week.
companion_files:
  - PHASE_1_MEASUREMENT_SYSTEM.md
  - PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - PHASE_1_DECISION_TREES.md
usage: >
  Copy this entire template. Save as monitoring/phase-1-week-[N]-synthesis-[YYYY-MM-DD].md.
  Fill all bracketed fields. Commit when done.
first_use_date: "Monday, June 4, 2026 (Day 7 checkpoint)"
updated: 2026-05-27
update_notes: >
  v1.1: Updated companion_files to reference new PHASE_1_MEASUREMENT_SYSTEM.md and
  PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md. Added Week 1 pre-populated example and
  escalation checklist appendix at end of document.
---

# Phase 1 Weekly Synthesis Template

**How to use**: Copy this entire file every Monday. Save as `monitoring/phase-1-week-[N]-synthesis-[YYYY-MM-DD].md`. Fill all `[bracketed]` fields. Commit the completed file. The synthesis is your single source of truth for what happened this week — the dashboard shows raw numbers, this file shows what they mean.

---

# Phase 1 Wave 1 — Week [N] Synthesis

**Week of**: [Monday YYYY-MM-DD] through [Sunday YYYY-MM-DD]
**Date completed**: [Today YYYY-MM-DD]
**Time started / completed**: [HH:MM] — [HH:MM]
**Days elapsed since first Wave 1 send (May 28)**: Day [X] through Day [Y]
**Domains in active distribution**: [Domain 56 / Domain 39 / both / other]

---

## Section 1: Running Metrics (pull from dashboard — 3 minutes)

Open the Google Sheets dashboard. Pull numbers from the summary blocks. Fill in the table below.

| Metric | This Week | Cumulative to Date |
|--------|-----------|-------------------|
| Contacts with Send_Date populated | — | [Contacts!H total] |
| Confirmed delivered (Delivery_Status = "Delivered") | — | [Contacts!I count] |
| Gist clicks — Domain 56 (bit.ly/drp-d56) | [Gist Views!C this week] | [Gist Views!J cumulative] |
| Gist clicks — Domain 39 (bit.ly/drp-d39) | [Gist Views!D this week] | — |
| All links total clicks | [Gist Views!I this week] | [Gist Views!J cumulative] |
| New replies received | [count of new Replies rows this week] | [Replies!A total count] |
| Overall reply rate (replies / delivered) | — | [Contacts summary: reply rate] |
| Score 3+ replies | [new this week] | [Contacts summary: Score 3+ count] |
| Score 3+ rate (Score 3+ / delivered) | — | [Contacts summary: Score 3+ rate] |
| Score 5 (Implementation Signal) | [new this week] | [total] |
| Score 4 (Partnership) | [new this week] | [total] |
| Category 2 replies (Critique-Objection) | [new this week] | [total] |
| Critique rate (Cat 2 / total replies) | [this week] | — |
| Tier 2 candidates flagged | — | [Contacts!O count "YES"] |
| Confirmed adoption signals | — | [Adoptions!H count "Confirmed"] |
| Network referral events | — | [Network Map total rows] |

**Alert check** — flag if any of these are true:
- [ ] Critique rate this week > 30%: [YES / NO]
- [ ] Any Score 5 received: [YES / NO] — if YES, escalate per reply-triage-framework.md
- [ ] Any Score 4 received: [YES / NO] — if YES and first/second occurrence, escalate
- [ ] Cumulative clicks below weekly target: [YES / NO] — target this week: [X]+
- [ ] Any delivery bounce detected: [YES / NO]

---

## Section 2: New Reply Scoring (2 minutes per reply)

*For each reply received this week, assign a category and score using the scoring decision tree in `reply-triage-framework.md`. Record here, then enter in the Replies tab.*

### Reply [R###] — [Organization name]

- **Date received**: [YYYY-MM-DD]
- **Category**: [Implementation Signal / Critique-Objection / Data Request / General Question / Partnership / Opt-Out]
- **Engagement Score**: [0–5]
- **Key content** (1–3 sentences, direct quote if possible): [fill]
- **Action required**: [YES / NO]
- **Response sent by**: [YYYY-MM-DD or "N/A"]
- **Escalation**: [ESCALATE / none]
- **FAQ entry created**: [YES / NO — topic if YES]
- **Tier 2 candidate**: [YES / NO]

*(Copy this block for each reply received this week. If no replies: write "No replies received this week.")*

---

## Section 3: Gist Views Summary (1 minute)

*Pull from Gist Views tab.*

**Domain 56 (bit.ly/drp-d56)**: [X] clicks this week
**Domain 39 (bit.ly/drp-d39)**: [Y] clicks this week
**All links combined this week**: [Z]
**Cumulative since launch**: [N]
**Delta vs. prior week**: [+N or -N or "first week"]

**Spike detected**: YES / NO
- If YES: [which link, what date, timing relative to last send, interpretation]

**Click velocity**: [cumulative clicks] / [days since first send] = [X.X] clicks/day

**Target check**:
- Week [N] cumulative target: [X]+ (from PHASE_1_GIST_TRACKING_PROTOCOL.md weekly targets table)
- Actual cumulative: [N]
- Status: On track / Below target / Above target

**Interpretation** (1 sentence): [e.g., "Domain 56 spike Day 8 confirms forwarding — watching for replies from non-contacted law schools by June 15."]

---

## Section 4: Engagement Patterns — What Is Working (2 minutes)

*Answer each question in 1–3 bullets. Write "No data yet" if insufficient signals.*

**Which constituency or domain is generating the strongest response?**
- [fill]

**Which framing, subject line, or opening is producing Category 1/2/3 replies?**
- [fill]

**Are senior contacts (directors, faculty) or staff-level contacts responding faster?**
- [fill]

**Is Gist click rate correlating with reply rate, or are there clicks without follow-up?**
- [fill]

---

## Section 5: Problem Signals — What Needs Attention (2 minutes)

*Write "None detected" for any item with no issues.*

**Delivery failures or bounces**: [none / list any]

**Constituencies with zero engagement for 2+ weeks**: [none / list any — note: not a failure until Day 30]

**Critique rate above 30%**: [YES: [X]% / NO]
- If YES: clusters around which topic? [fill]

**Gist click velocity declining (negative delta week over week)**: [YES / NO]

**Contacts who replied negatively or requested removal**: [none / list any]

**Any technical issues** (Bitly links broken, email bouncing, Gist inaccessible): [none / describe if any]

---

## Section 6: Tier 2 Candidates (1 minute)

*List any contacts who reached Score 3+ this week and qualify for follow-up Tier 2 outreach.*

**New Tier 2 candidates this week**: [count]

For each candidate:
- **Organization**: [name]
- **Score**: [3 / 4 / 5]
- **What they said**: [1 sentence]
- **Domain they engaged with**: [Domain 56 / Domain 39]
- **Recommended follow-up**: [e.g., "Offer phone call to discuss clinic integration"; "Send Domain 39 materials given their healthcare policy focus"]
- **Flagged in Contacts!O**: [YES / done]

If no new candidates: "No new Tier 2 candidates this week."

---

## Section 7: Cross-Organizational References and Network Effects

*Only fill if any referrals or network events occurred. Otherwise write "None detected."*

**New referrals detected this week**: [count]
- [Source org] forwarded to [Referred org / unknown] — Domain [N] — [evidence: reply quote / spike / new email]
- Record in Network Map tab: YES / done

**Second-hop referrals** (referred org further refers to another org): [count / none]

**Total network events to date**: [running count from Network Map tab]

**Interpretation**: [e.g., "Law school forwarding pattern detected — watching for new replies from clinical faculty at non-contacted schools."]

---

## Section 8: Web Monitoring and Organic Signals

*Check Google Alerts, Regulations.gov, and SSRN.*

**Google Alerts new mentions this week**: [count]
- [If any: publication name, brief description, URL if available]
- Label used: [phase1-alerts filter in Gmail]

**Regulations.gov comments** (Domain 39 / Domain 42 dockets): [count / none]
- [If any: docket ID, brief content, relevance]

**SSRN / academic papers citing or related to Phase 1 domains**: [count / none]
- [If any: author, title, relevance, URL]

**Organic Bitly clicks** (clicks that do not correlate with any send date): [count / none]
- [If any: which link, date, estimated source]

---

## Section 9: Dashboard Data Entry Confirmation

**This week I updated the following tabs** (check when done):
- [ ] Contacts — new replies logged with Reply_Date, Reply_Category, Engagement_Score
- [ ] Contacts — Tier2_Candidate column updated where applicable
- [ ] Gist Views — new row added with this week's click data
- [ ] Replies — one row per reply received
- [ ] Adoptions — any new adoption signals logged
- [ ] Network Map — any new referral events logged
- [ ] Constituencies — formula results verified (no manual errors)
- [ ] Checkpoints — new row added only if this is a checkpoint week

---

## Section 10: Checkpoint Decision (checkpoint weeks only)

*Fill ONLY in weeks containing Day 7 (June 4–5), Day 14 (June 11–12), Day 30 (June 27–28), or Day 60 (July 27–28). Otherwise leave blank.*

**Checkpoint**: [Day 7 / Day 14 / Day 30 / Day 60]
**Checkpoint date**: [YYYY-MM-DD]

**Four numbers pulled from dashboard**:
- (A) Score 3+ reply rate: [X%]
- (B) Constituencies meeting strong threshold: [X of 7]
- (C) Cross-organizational references (confirmed or probable): [X]
- (D) Confirmed adoption signals: [X]

**Decision tree executed**: [`day-7-14-30-decision-trees.md`, [Day X] tree]

**DETERMINATION**: [HOLD / MONITOR / ESCALATE / CONTACT_VERIFY / CONTINUE_MONITOR / FAILURE_IMMINENT / STRONG / MODERATE / WEAK / ASSESS / FAILURE]

**Phase 2 decision**:
- Domain 39 status: [LAUNCHING / LAUNCHING WITHIN 24H / HOLD / ALREADY ACTIVE]
- Domain 56 status: [LAUNCHING / LAUNCHING WITHIN 48H / HOLD / ALREADY ACTIVE]
- Tier 2 expansion: [ACTIVATING NOW / STAGING FOR DAY [X] / NOT YET / N/A]

**Actions I am taking as a result**:
- [ ] CHECKIN.md updated with checkpoint determination
- [ ] Domain 39 distribution sent or staged
- [ ] Domain 56 distribution sent or staged
- [ ] User notified of any Score 4–5 escalations
- [ ] Failure recovery modifications activated (if WEAK): Mod 1 / Mod 2 / Mod 3
- [ ] Checkpoints tab updated with new row

**Next scheduled checkpoint**: [Day 14 June 11 / Day 30 June 27 / Day 60 July 27 / other]

---

## Section 11: FAQ Entries Created This Week

*Document any recurring questions or critiques that should inform Phase 2 messaging.*

**New FAQ entries**: [count]

1. **Q**: [Exact or paraphrased question from contact]
   **A**: [2–4 sentence answer, referencing specific framework section if applicable]
   **Source**: [Organization / Contact_ID]
   **Recurrence**: [first time / N contacts have now asked this]

*(Repeat for each new FAQ entry. If none: write "No new FAQ entries this week.")*

**Pattern alert**: If the same question or critique appears from 3+ contacts, flag it here:
- [Topic]: [X contacts have raised this] — [action: revise framing / add clarifying note to outreach / other]

---

## Section 12: Carries Forward to Next Week

*What requires follow-up next week?*

**Pending responses I owe to contacts**:
- [Contact / Org]: [What I promised, by when]

**Expected replies or developments**:
- [e.g., "Score 3 reply from Georgetown CCF expected — sent follow-up June 3; watch for response by June 10"]
- [e.g., "Domain 39 sends June 1 — expect first click data by June 2"]

**Reminders for next Monday**:
- [ ] Check Bitly: compare Week [N+1] clicks against Week [N] delta
- [ ] Follow up with any contacts who opened but did not reply (if identifiable)
- [ ] Check Regulations.gov Domain 39 docket for new comments
- [ ] [Any other monitoring reminder]

---

## Section 13: Overall Assessment (1 minute)

**Trajectory**: On Track / Below Track / Accelerating / Concerning

**Confidence in Phase 2 timing**:
- [ ] HIGH — on track for Day 30 STRONG; Phase 2 launch within 30 days
- [ ] MEDIUM — on MODERATE track; Phase 2 partial launch likely by Day 30–45
- [ ] LOW — below MODERATE; need Day 14 recheck before assessing Phase 2 timing
- [ ] VERY LOW — failure recovery needed

**One-sentence summary of this week**: [e.g., "Week 1 delivered above-target click velocity (15 clicks, target 15+) with two Score 3 replies from law school contacts — strong trajectory toward Day 30 MODERATE or STRONG."]

**Risk flags**:
- [ ] No flags
- [ ] Minor: [describe]
- [ ] Moderate: [describe — consider adding to CHECKIN.md]
- [ ] Major: [describe — add to CHECKIN.md "Needs Your Input" immediately]

---

## Synthesis Completion

**Date completed**: [YYYY-MM-DD]
**Time spent**: [X minutes]
**File saved as**: `monitoring/phase-1-week-[N]-synthesis-[YYYY-MM-DD].md`
**Committed to git**: [YES / NO]

---

## Alert Trigger Reference (quick-scan)

Use this reference to check whether any alerts were triggered this week:

| Alert | Threshold | This Week | Triggered? |
|-------|-----------|-----------|-----------|
| Critique rate | > 30% of replies | [X%] | YES / NO |
| Score 5 received | Any single event | [count] | YES / NO |
| Score 4 cluster | 2+ within 14 days | [count this period] | YES / NO |
| Opt-out cluster | 2+ within 7 days | [count] | YES / NO |
| Zero clicks (post-Week 2) | 0 clicks in any week | [this week total] | YES / NO |
| Below cumulative target | See weekly target table | [cumulative vs. target] | YES / NO |
| Delivery bounce | 3+ bounces | [count] | YES / NO |

---

*Template version 1.1 — May 27, 2026. Use starting June 4, 2026 (Day 7 checkpoint) through at least Week 8 (late July). After Day 60 checkpoint, assess whether continued weekly synthesis is warranted based on Phase 2 launch status.*

---

## Appendix A: Week 1 Pre-Populated Example (May 28 – June 3, 2026)

This example shows what a completed Week 1 synthesis looks like under a moderate-positive scenario. Use it as a reference for calibrating scoring and interpretation, not as a template to copy verbatim.

---

# Phase 1 Wave 1 — Week 1 Synthesis (EXAMPLE)

**Week of**: May 28, 2026 through June 3, 2026
**Date completed**: June 4, 2026
**Time started / completed**: 09:00 — 09:22 UTC
**Days elapsed since first Wave 1 send (May 28)**: Day 1 through Day 7
**Domains in active distribution**: Domain 56 (May 28), Domain 39 (June 1)

---

### Section 1: Running Metrics

| Metric | This Week | Cumulative to Date |
|--------|-----------|-------------------|
| Contacts with Send_Date populated | — | 45 |
| Confirmed delivered | — | 42 (3 unknown — follow up) |
| Gist clicks — Domain 56 (bit.ly/drp-d56) | 8 | 8 |
| Gist clicks — Domain 39 (bit.ly/drp-d39) | 4 | 4 |
| All links total clicks | 23 | 23 |
| New replies received | 4 | 4 |
| Overall reply rate (replies / delivered) | — | 9.5% (4/42) |
| Score 3+ replies | 2 | 2 |
| Score 3+ rate | — | 4.8% |
| Score 5 (Implementation Signal) | 0 | 0 |
| Score 4 (Partnership) | 1 | 1 |
| Score 2 (Polite ack or OOO) | 1 | 1 |
| Score 1 (OOO only) | 1 | 1 |
| Tier 2 candidates flagged | — | 1 |
| Confirmed adoption signals | — | 0 |

Alert check:
- [ ] Critique rate > 30%: NO (0 of 4 replies were critiques)
- [ ] Score 5 received: NO
- [ ] Score 4 received: YES — one immigration legal aid contact (see Section 2)
- [ ] Cumulative clicks below Week 1 target: NO (23 vs. 15 target — above)
- [ ] Delivery bounce: YES — 3 contacts show unknown delivery status; not confirmed bounces

---

### Section 2: New Reply Scoring

**Reply R001 — NILC (Immigration Legal Aid)**
- Date received: June 2, 2026
- Category: Partnership
- Engagement Score: 4
- Key content: "The Domain 29 model brief language is exactly what we need for a pending Ninth Circuit amicus. I'm forwarding to our litigation director today. Can we adapt this for our specific case context?"
- Action required: YES — Reply confirming adaptation permission and request for case context details
- Response sent by: June 5, 2026
- Escalation: ESCALATE — Score 4 within Day 7. Add to CHECKIN.md under "Early Signals."
- Tier 2 candidate: YES

**Reply R002 — Harvard Law School (Law School)**
- Date received: June 2, 2026
- Category: General Question
- Engagement Score: 3
- Key content: "This is a compelling framework. Question on methodology: how are you distinguishing 'democratic erosion' events from normal political contestation in your Domain 37 typology?"
- Action required: YES — Substantive reply explaining the typology criteria
- Response sent by: June 5, 2026
- Escalation: none (Score 3; monitor for follow-up)
- Tier 2 candidate: YES (if follow-up reply upgrades to Score 4)

**Reply R003 — ACLU National (Civil Rights)**
- Date received: June 1, 2026
- Category: General Question (borderline polite ack)
- Engagement Score: 2
- Key content: "Thanks for sharing this important work. I'll pass along to our policy team."
- Action required: NO
- Response sent by: N/A
- Escalation: none
- Tier 2 candidate: NO (Score 2; monitor for policy team follow-up)

**Reply R004 — Unnamed mutual aid contact (Mutual Aid)**
- Date received: June 3, 2026
- Category: OOO auto-reply only
- Engagement Score: 1
- Key content: "Out of office through June 10."
- Action required: NO — Add June 10 reminder to follow-up calendar
- Tier 2 candidate: NO

---

### Section 3: Gist Views Summary

Domain 56 (bit.ly/drp-d56): 8 clicks this week
Domain 39 (bit.ly/drp-d39): 4 clicks this week (June 1–3 only — first 3 days)
All links combined this week: 23
Delta vs. prior week: N/A (first week)
Click velocity: 23 / 7 = 3.3 clicks/day

Spike detected: YES — Domain 56 had 5 clicks on June 1. This aligns with the Domain 39 send date. Likely cause: Domain 39 recipients saw the Domain 56 Gist URL in the email footer and clicked through. Not an organic amplification event; a cross-send click-through.

Target check: Week 1 cumulative target: 15+. Actual: 23. Status: Above target.

Interpretation: Click velocity is healthy. The June 1 cross-spike confirms that Domain 39 recipients are engaging with Domain 56 materials — a positive cross-domain signal. Watch for whether immigration legal aid contacts (who are the Domain 39 primary audience) also click Domain 56 next week.

---

### Section 6: Tier 2 Candidates

New Tier 2 candidates this week: 1

- Organization: NILC
- Score: 4
- What they said: Seeking permission to adapt Domain 29 model brief for Ninth Circuit amicus
- Domain engaged: Domain 56 (via cross-click), Domain 29 content request
- Recommended follow-up: Confirm adaptation permission; ask for case name so adoption can be tracked; offer any additional model brief language they need
- Flagged in Contacts!O: YES (done)

---

### Section 10: Checkpoint Decision (Day 7)

Checkpoint: Day 7
Checkpoint date: June 4, 2026

Four numbers from dashboard:
- (A) Score 3+ reply rate: 4.8%
- (B) Constituencies meeting Day 7 minimum: 4 of 7 (Law School, Imm Legal Aid, Civil Rights, Mutual Aid each have >= 1 signal; Academic, Faith, Labor have zero signal)
- (C) Cross-organizational references: 1 (NILC forward to litigation director — Probable)
- (D) Confirmed adoption signals: 0

Decision tree executed: PHASE_1_DECISION_TREES.md, Day 7 tree

DETERMINATION: HOLD — Bitly total 23 >= 15 target; 4 replies >= 2 threshold; 0 bounces confirmed. Normal trajectory.

Phase 2 decision:
- Domain 39 status: ALREADY ACTIVE (sent June 1)
- Domain 56 status: ALREADY ACTIVE (sent May 28)
- Tier 2 expansion: NOT YET — wait for Day 14 to confirm Score 4 from NILC converts to adoption signal

Actions taken:
- [x] CHECKIN.md updated with Score 4 early signal from NILC
- [x] Checkpoints tab updated with Day 7 row

Next scheduled checkpoint: Day 14, June 11, 2026

---

### Section 13: Overall Assessment

Trajectory: On Track — slightly above click target; Score 4 in first week is ahead of baseline

Confidence in Phase 2 timing: MEDIUM — on MODERATE track; early NILC signal is promising but insufficient to accelerate Tier 2 before Day 14

One-sentence summary: Week 1 delivered above-target engagement (23 clicks vs. 15 target, 4 replies including 1 Score 4 from NILC with amicus brief request) against a background of three constituencies still at zero signal — trajectory is HOLD with close Day 14 monitoring needed for Academic, Faith, and Labor.

Risk flags:
- Minor: Academic, Faith, Labor constituencies at zero signal. Not concerning at Day 7; becomes a flag if still zero at Day 14.

---

## Appendix B: Escalation Checklist

Add to CHECKIN.md under "Needs Your Input" if any of the following are true at the end of any synthesis week:

**Escalate same day**:
- Any reply expressing legal concern, privacy concern, or requesting removal from outreach
- Score 5 event received (institutional adoption confirmed — publication, curriculum, litigation filing)
- Bitly total < 5 AND confirmed delivery for all 45 contacts at Day 7

**Escalate within 24 hours**:
- Three or more email bounces (bounce rate > 6%)
- Day 14: zero Score 3+ replies from all constituencies with confirmed delivery
- Score 4 events from two or more contacts within the first 14 days (pre-Day 30 STRONG signal available)
- Day 30: FAILURE determination

**Escalate within 72 hours**:
- Day 30: WEAK determination (user decision needed on whether to extend vs. modify approach)
- Day 60: Z < 4 (fewer than 4 constituencies with at least 1 confirmed adoption — user decision on Phase 2 scope)

**Do not escalate — wait for more data**:
- Level 1 and Level 2 replies only in Week 1 — normal; wait for Day 14
- One constituency at zero signal at Day 7 — monitor, not failure
- Bitly below 15 at Day 7 with some replies present — MONITOR status, not ESCALATE
- Score 3+ rate below 25% at Day 14 — reply timing peaks at Days 10-21; wait for Day 21 before treating as a below-baseline signal
