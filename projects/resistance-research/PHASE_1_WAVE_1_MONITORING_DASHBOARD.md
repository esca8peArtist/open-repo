---
title: "Phase 1 Wave 1 Monitoring Dashboard — Complete Operator's Guide"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Unified, end-to-end monitoring infrastructure for Phase 1 Wave 1 distributions.
  Covers setup (May 27–28), weekly operations (15–20 minutes), reply triage,
  Gist view tracking, and Day 7/14/30 decision trees with specific thresholds.
  Solo-operator-friendly. Everything needed to run Phase 1 from May 28 to June 30.
word_count: ~4200
companion_files:
  - wave-1-metrics-template.csv
  - gist-view-tracking-protocol.md
  - reply-triage-framework.md
  - weekly-synthesis-template.md
  - day-7-14-30-decision-trees.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - PHASE_1_DECISION_TREES.md
  - DISTRIBUTION_GIST_URLS.md
timeline:
  setup: "May 27–28 (pre-Wave 1)"
  wave_1_send: "May 28 (Domain 56) + June 1 (Domain 39)"
  day_7_checkpoint: "June 4–5"
  day_14_checkpoint: "June 11–12"
  day_30_checkpoint: "June 27–28"
weekly_time_budget: "15–20 minutes per week"
---

# Phase 1 Wave 1 Monitoring Dashboard — Complete Operator's Guide

**Version 1.0 — May 26, 2026**

## Executive Summary

This document is your complete operational playbook for tracking Phase 1 Wave 1 success from Day 1 through Day 60. You will measure four core metrics — Bitly click velocity, reply rate, reply score distribution, and adoption signal count — and use them to make three critical checkpoint decisions:

- **Day 7 (June 4–5)**: Is delivery confirmed and is minimum engagement happening? → Decision: HOLD / MONITOR / ESCALATE
- **Day 30 (June 27–28)**: Is Phase 1 trajectory tracking targets? → Decision: STRONG → Phase 2 immediate activation / MODERATE → Domain 39 + Domain 56 delayed / WEAK → failure recovery
- **Day 60 (July 28–29)**: Has Phase 1 achieved movement-scale impact? → Decision: Full Phase 2 launch / Partial Phase 2 (subset of constituencies) / Extension

**Total setup time**: 45 minutes one-time (May 27–28).
**Total ongoing time**: 15–20 minutes per week (Mondays).
**First checkpoint**: June 4, 2026 (Day 7 from May 28 Domain 56 send).

---

## Part 1: Pre-Wave Setup (May 27–28)

### 1.1 Create Google Sheets Dashboard

1. Go to **Google Sheets** and create a new blank spreadsheet.
2. Title: `Phase 1 Wave 1 Impact Dashboard — May 28 2026`
3. Share settings: **Anyone with the link can view** (not edit).
4. Copy the share URL. Paste it into `CHECKIN.md` under a new section titled "Dashboard URL — Wave 1 Monitoring."

### 1.2 Add Six Sheets

Click the + button at the bottom and create sheets with these exact names:

1. **Contacts** — Master contact log (one row per contact)
2. **Gist Views** — Weekly Bitly click tracking
3. **Replies** — Reply scoring and triage
4. **Adoptions** — Confirmed adoption signal registry
5. **Constituencies** — Per-constituency aggregated metrics
6. **Checkpoints** — Append-only decision log

### 1.3 Populate Contacts Sheet

Download `wave-1-metrics-template.csv` (provided with this document). Open it in a text editor. Copy all rows (headers + data). Paste into the **Contacts** sheet starting at cell A1.

**Key columns to verify before sending any email**:
- Column G (Email): All addresses verified and current
- Column H (Send_Date): Empty until you actually send
- Column I (Delivery_Status): Will be filled manually or via bounce notification

### 1.4 Set Up Bitly Links

1. Create a free Bitly account at `bitly.com`.
2. Create one short link per Gist (not per contact). Use the mappings from `DISTRIBUTION_GIST_URLS.md`:
   - Example: `bit.ly/drp-domain56` → (Gist URL for Domain 56)
   - Example: `bit.ly/drp-domain39` → (Gist URL for Domain 39)
3. Test each link: click it, verify the Gist loads, return to Bitly dashboard and confirm the click registered.
4. Replace all raw Gist URLs in your email templates with the Bitly short links before sending.

### 1.5 Set Up Gmail Labels

In Gmail Settings → Labels:

```
phase1-outreach/
  ├── sent/
  │   ├── domain-56-wave-1
  │   └── domain-39-wave-1
  ├── replies/
  │   ├── score-5-adoption
  │   ├── score-4-collaboration
  │   ├── score-3-substantive
  │   ├── score-2-acknowledgment
  │   └── score-1-ooo-only
  └── bounced/
```

When you send emails: manually create a Gmail filter or label the sent message with `phase1-outreach/sent/domain-56-wave-1` (or `domain-39-wave-1`).

When replies arrive: manually score and label them (or set up a Zapier automation to route based on keywords).

---

## Part 2: Weekly Operations (Mondays, 15–20 Minutes)

Every Monday starting June 3, run the following checklist. Use `weekly-synthesis-template.md` to structure your notes.

### Step 1: Email Review (5 minutes)

1. Open Gmail. Filter by label: `phase1-outreach/replies/`
2. For each new reply since last Monday:
   - Open the reply and read it fully
   - **Score it using the 5-point scale** (detailed below; also see `reply-triage-framework.md`):
     - **Score 5**: Explicit adoption statement (citation, curriculum integration, formal partnership offer)
     - **Score 4**: Forwarding or collaboration request ("I'm passing this to my colleagues")
     - **Score 3**: Substantive engagement (question, feedback, request for elaboration)
     - **Score 2**: Polite acknowledgment ("Thanks for sharing, interesting work")
     - **Score 1**: Out-of-office or form reply only
   - Enter the score in **Contacts sheet, Column N (Engagement_Score)**
   - Add the reply date to **Column L (Reply_Date)**
   - Use **Column S (Notes)** to capture key phrases that indicate triage category (e.g., "mentioned adopting for clinic curriculum" → Score 5)

3. **Triage check**: If any reply is Score 4–5, flag in **Column O (Tier2_Candidate)** with "YES". These are your Phase 2 social proof contacts.

### Step 2: Bitly Click Pull (3 minutes)

1. Log in to `bitly.com/a/dashboard`
2. For each Gist link (e.g., `bit.ly/drp-domain56`):
   - Note the **total click count** for the week (or daily if you prefer granularity)
   - Enter in **Gist Views sheet** under the appropriate week column
3. **Spike detection**: If any single link had 5+ clicks in one day, flag it:
   - Enter "YES" in the **Spike_Flag** column
   - Note which link and what date in **Spike_Notes**
   - Cross-reference the spike date against when Domain 56 / Domain 39 waves were sent. Spikes 24–72 hours post-send = confirmed delivery engagement.

### Step 3: Web Monitoring (4 minutes)

1. **Google Alerts**: Check your email for alerts set up under `phase1-outreach`. Any new mentions of the framework?
   - If yes: verify the source, score it, add to **Adoptions sheet**
2. **Regulations.gov**: For Domain 39 (Healthcare), check the HHS interim Medicaid rule comment docket (document number TBD, will be provided in DISTRIBUTION_GIST_URLS.md).
   - Any comments citing framework vocabulary?
   - If yes: add to **Adoptions sheet** as web detection
3. **SSRN / Scholar alerts** (if applicable): Any new academic uploads from Tier 1 contacts?

### Step 4: Dashboard Update (3 minutes)

1. Open **Constituencies** sheet
2. For each constituency (Law School, Immigration Legal Aid, Civil Rights, Academic, Faith, Labor, Mutual Aid):
   - Check formulas (they auto-calculate from Contacts sheet)
   - Verify counts are current
3. Open **Checkpoints** sheet
4. If today is a checkpoint date (Day 7, Day 14, Day 30, Day 60):
   - Add a new row with today's date
   - Run the decision tree (see Part 4 below)
   - Document the decision in **Column I (Determination)** and **Column J (Phase_2_Decision)**

---

## Part 3: Reply Triage Framework

See `reply-triage-framework.md` for the full framework. Quick summary:

### Five Reply Categories

| Category | Definition | Score | Phase 2 Signal | Action |
|----------|-----------|-------|---------------|--------|
| **Implementation Signal** | Org is building on your framework (curriculum use, model brief integration, policy brief citation) | 5 | YES — escalate to Phase 2 immediately | Document in Adoptions sheet; use as social proof in Phase 2 outreach |
| **Critique / Feedback** | Substantive criticism, suggestion for improvement, request for elaboration | 3 | MAYBE — wait for follow-up | Log in Replies sheet; send response email within 48 hours; may turn into Score 5 |
| **Partnership / Collaboration** | Explicit offer to co-author, co-host, or work together on adjacent research | 4 | YES — escalate to Phase 2 planning | Treat as partnership candidate; involve user in Phase 2 design |
| **Question / Clarification** | Ask for specific information, seek permission to adapt, want more resources | 3 | MAYBE — offers growth opportunity | Create FAQ entry; may surface in multiple replies |
| **Opt-Out** | Unsubscribe, do not contact, not interested | 0 | NO — remove from further outreach | Remove from Contacts sheet or mark "Opted Out" in Column I; do not include in Phase 2 |

**Escalation thresholds**:
- Any Score 5 → Log in Adoptions sheet within 24 hours → User notification within 48 hours
- 2+ Score 4 replies within first 14 days → Early signal for Phase 2 pre-activation
- 3+ Score 3+ replies per constituency by Day 30 → Strong signal, proceed with Phase 2

---

## Part 4: Gist View Tracking Protocol

See `gist-view-tracking-protocol.md` for full details. Quick workflow:

### Manual Weekly Snapshot

Every Monday, record in the **Gist Views** sheet:

| Column | Data | Source |
|--------|------|--------|
| Week_Number | 1, 2, 3, etc. | Count from send date |
| Week_End_Date | Sunday of that week | Calendar |
| Domain56_Clicks | Bitly cumulative total for Domain 56 link | Bitly dashboard |
| Domain39_Clicks | Bitly cumulative total for Domain 39 link | Bitly dashboard |
| Total_Week_Clicks | Sum of above two | Formula: =SUM(C2:D2) |
| Cumulative_Clicks | Running total from Week 1 | Formula: =SUM($C$2:C2) |

### Success Targets

- **Week 1 (Day 7)**: 15+ total clicks minimum → signals delivery confirmed
- **Week 2 (Day 14)**: 30+ cumulative clicks → signals sustained engagement
- **Week 4 (Day 30)**: 60+ cumulative clicks → signals strong ongoing interest

**Spike detection**: If any single link has 5+ clicks in one day, note the date and likely cause (e.g., "Law school group forwarded to clinic directors on June 6").

---

## Part 5: Day 7 / Day 14 / Day 30 Decision Trees

See `day-7-14-30-decision-trees.md` for the full trees with all branches. Executive summary:

### Day 7 Checkpoint (June 4–5)

**Run this tree 7 calendar days after Wave 1 send (May 28 Domain 56 send → June 4 checkpoint).**

Pull from dashboard:
- Week 1 Bitly clicks (Gist Views sheet)
- Total replies received (Contacts sheet, Column L count)
- Delivery status check (any 3+ bounces? any 0-click links?)

**Decision branches**:

```
15+ clicks  AND  2+ replies  → STATUS: HOLD (normal trajectory, continue to Day 30)
5-14 clicks OR 0-1 replies   → STATUS: MONITOR (below target, re-check Day 14)
0-4 clicks (with delivery)   → STATUS: ESCALATE (possible delivery failure, run diagnostic)
3+ bounces                   → STATUS: CONTACT_VERIFY (fix emails, re-send, restart Day 7 clock)
```

**What to do**:
- HOLD: No action. Continue to Day 30 checkpoint.
- MONITOR: Check again at Day 14. If still below threshold, apply framing revision (Modification 2 in PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 6.3).
- ESCALATE: Check email delivery logs. Verify from addresses not marked as spam. Consider re-send to corrected list.

### Day 30 Checkpoint (June 27–28)

**Run 30 calendar days after Wave 1 send.**

Pull from dashboard:
- Overall reply rate (Score 3+) — target: 50% for STRONG
- Constituencies passing strong threshold — target: 4+ of 7 for STRONG
- Cross-organizational references — target: 3+ for STRONG
- Confirmed adoption signals — target: 2+ for STRONG

**Decision branches**:

```
50%+ Score 3+  AND  4+ constituencies  AND  3+ references  AND  2+ adoptions
  → DETERMINATION: STRONG
     ACTION: Activate Phase 2 immediately (same day)
             • Send Domain 39 distribution within 24 hours (June 1 HHS deadline applies)
             • Send Domain 56 distribution within 48 hours
             • Begin Tier 2 law school pre-outreach using Score 4–5 replies as social proof

30-49% Score 3+  OR  3+ constituencies  OR  1+ references  OR  1+ adoptions
  → DETERMINATION: MODERATE
     ACTION: Activate Domain 39 only (June 1 HHS deadline applies)
             • Send Domain 39 within 24 hours
             • Hold Domain 56 until Day 37 (allow more Phase 1 data to accumulate)
             • Continue Phase 1 monitoring to Day 60
             • Begin Tier 2 planning but do not send outreach yet

<20% Score 3+  AND  <2 constituencies  AND  0 references  AND  0 adoptions
  → DETERMINATION: WEAK
     ACTION: Do not extend same approach to Day 60
             • Apply 3-modification failure recovery (see framework)
             • Send Domain 39 (healthcare urgency overrides weak signal)
             • Hold Domain 56 until Day 60 checkpoint
             • Prepare stakeholder substitution + framing revision for Day 45 re-send
```

### Day 60 Checkpoint (July 28–29)

**Run 60 calendar days after Wave 1 send.**

Pull from dashboard:
- Confirmed adoptions (Adoptions sheet, count "Confirmed" in verification column) — target: 15
- People reached (Adoptions sheet, sum of estimated count column) — target: 100
- Constituencies with at least 1 confirmed adoption — all 7 for full scale, 4+ for partial scale

**Decision branches**:

```
15+ confirmed adoptions  AND  100+ people reached
  → DETERMINATION: MOVEMENT-SCALE IMPACT ACHIEVED
     ACTION: Full Phase 2 launch (all 7 constituencies at Tier 2)
             • Activate all pending Phase 2 domains per priority order
             • Use adoption evidence as social proof in Tier 2 outreach

8+ confirmed adoptions  AND  50+ people reached
  → DETERMINATION: PARTIAL SUCCESS
     ACTION: Phase 2 partial launch (constituencies with confirmed adoption only)
             • Activate Tier 2 for constituencies with adoption evidence
             • Hold others for extended Phase 1 or targeted re-engagement

<8 confirmed adoptions  OR  <50 people reached
  → DETERMINATION: BELOW TARGET
     ACTION: User decision required
             • Log in CHECKIN.md under "Needs Your Input"
             • Provide per-constituency breakdown
             • User decides: continue Phase 1 extension, pivot to public channels, or close Phase 1
```

---

## Part 6: Constituency-Specific Benchmarks

The Day 7 / Day 30 / Day 60 checkpoints use **overall** aggregate metrics. However, Phase 2 decision-making is **per-constituency**. Your dashboard's **Constituencies** sheet must track each of 7 separately:

### Day 7 Minimum Viable Engagement (per constituency)

| Constituency | Minimum by Day 7 | Evidence |
|--------------|------------------|----------|
| Law Schools | ≥1 click on Gist link | Bitly detection or email open |
| Immigration Legal Aid | ≥1 click | Bitly detection or email reply |
| Civil Rights Orgs | ≥1 click or reply | Any engagement signal |
| Academic / Policy | ≥1 reply at any score | Email reply only (researchers slower to click) |
| Faith Coalitions | ≥1 click | Bitly detection |
| Labor Unions | ≥1 click | Bitly detection |
| Mutual Aid Networks | ≥1 click | Bitly detection |

### Day 30 Strong Threshold (per constituency)

| Constituency | Strong Threshold | Definition |
|--------------|------------------|-----------|
| Law Schools | 3+ replies at Score 3+ | Substantive engagement from clinic directors, faculty, student orgs |
| Immigration Legal Aid | 2+ Score 3+ replies OR 1 litigation use case | Operational integration into brief or advisory |
| Civil Rights Orgs | 3+ Score 2+ replies OR 1 policy document citation | Citation in annual report, strategy doc, or published brief |
| Academic / Policy | 2+ Score 3+ replies OR 1 SSRN upload | Research integration signal |
| Faith Coalitions | 2+ Score 3+ replies OR 1 congregational use | Incorporation into sermon guide, discussion toolkit, etc. |
| Labor Unions | 2+ Score 3+ replies OR 1 training program integration | Union education module adoption |
| Mutual Aid Networks | 2+ Score 3+ replies OR 1 governance doc integration | Incorporation into network governance, trainer program, etc. |

**Note**: A single Score 5 reply from a constituency counts as "strong threshold met" immediately.

---

## Part 7: Key Templates and Artifacts

Four companion documents provide detailed operational procedures:

1. **`wave-1-metrics-template.csv`** — Pre-populated contact list for Domain 56 (11 contacts) and Domain 39 (5 contacts). Download, paste into Contacts sheet.

2. **`gist-view-tracking-protocol.md`** — Manual weekly Bitly snapshot procedure (5 minutes). Explains how to detect spikes and interpret their meaning.

3. **`reply-triage-framework.md`** — 5-category triage system with escalation protocols. Use when scoring replies.

4. **`weekly-synthesis-template.md`** — Copy-paste markdown template for your Monday synthesis notes. Keeps weekly data organized in one place for end-of-phase analysis.

5. **`day-7-14-30-decision-trees.md`** — Detailed decision trees with all branches, thresholds, and immediate actions to take at each checkpoint.

---

## Part 8: Timeline and Critical Dates

| Date | Event | Action | Checkpoint |
|------|-------|--------|-----------|
| May 27–28 | Setup | Create Sheets, set up Bitly, add labels | Pre-Wave 1 |
| May 28 | Domain 56 Wave 1 Send | Label 11 emails with `phase1-outreach/sent/domain-56-wave-1` | Delivery confirmed |
| June 1 | Domain 39 Wave 1 Send | Label 5 emails with `phase1-outreach/sent/domain-39-wave-1` | Delivery confirmed |
| June 3 (Mon) | **First Weekly Synthesis** | Run Step 1–4 checklist | Week 1 data |
| June 4–5 | **DAY 7 CHECKPOINT** | Pull Week 1 metrics, run decision tree, update CHECKIN.md | HOLD / MONITOR / ESCALATE |
| June 10 (Mon) | Weekly Synthesis | Run checklist | Week 2 data |
| June 11–12 | Day 14 checkpoint (optional) | Check if MONITOR status has improved | Early warning |
| June 17 (Mon) | Weekly Synthesis | Run checklist | Week 3 data |
| June 24 (Mon) | Weekly Synthesis | Run checklist | Week 4 data |
| June 27–28 | **DAY 30 CHECKPOINT** | Pull all-metrics, run decision tree, activate Phase 2 if STRONG/MODERATE | STRONG / MODERATE / WEAK |
| July 1 onward | Phase 2 Tier 1 Distribution | Domain 56 or Domain 39 Tier 2 outreach begins | Phase 2 Wave 1 |
| July 28–29 | **DAY 60 CHECKPOINT** | Pull adoption registry, run decision tree, decide full/partial/extension Phase 2 | Movement-scale impact assessment |

---

## Part 9: Failure Modes and Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Day 7: 0 clicks, emails delivered | Possible content issue or wrong audience | Run diagnostic: forward to 2 test contacts, verify Bitly link clicks work, check spam folder |
| Day 7: High bounce rate (3+) | Email addresses outdated | Pull corrected emails from DISTRIBUTION_OUTREACH_CONTACTS.md, re-send to corrected list, restart Day 7 clock |
| Day 30: <20% reply rate, no adoption | Framing issue or low relevance to audience | Apply Modification 2 (framing revision): lead with single domain most relevant to each constituency, not full framework |
| Day 30: WEAK signal | Phase 1 not tracking targets | Do not extend Phase 1 unchanged. Apply 3-modification failure recovery: stakeholder substitution (swap high-volume-inbox contacts with lower-tier, more responsive contacts), channel shift (move 50% effort to network intermediaries / conferences / publications), re-send with revised framing by Day 45 |
| Any checkpoint: Can't locate Adoption signals | No one filling in Adoptions sheet regularly | Set recurring phone reminder for Monday 9:00 AM (before weekly synthesis), or email yourself: "Phase 1 Adoption Registry — any news to log this week?" |

---

## Part 10: Success Indicators at Each Checkpoint

### Day 7 — Delivery and Early Engagement

✅ **GOOD**: 15+ total Bitly clicks across both domains + 2+ substantive replies (Score 3+)
⚠️ **CONCERNING**: 5–14 clicks OR 0–1 replies (not failure, but re-check at Day 14)
🔴 **FAILURE**: 0 clicks with confirmed delivery OR 3+ bounces (investigate immediately)

### Day 30 — Movement Begins

✅ **STRONG**: 50%+ Score 3+ reply rate, 4+ constituencies passing strong threshold, 3+ cross-org references, 2+ adoption signals
⚠️ **MODERATE**: 30–49% reply rate OR 3+ constituencies strong OR 1+ adoption signals (proceed with Domain 39, hold Domain 56)
🔴 **WEAK**: <20% reply rate AND <2 constituencies strong AND 0 references AND 0 adoptions (apply failure recovery, do not extend without changes)

### Day 60 — Movement-Scale Impact

✅ **MOVEMENT**: 15+ confirmed adoptions, 100+ people reached → Full Phase 2 launch
⚠️ **PARTIAL**: 8–14 adoptions, 50–99 people reached → Phase 2 in confirmed-adoption constituencies only
🔴 **BELOW TARGET**: <8 adoptions OR <50 people reached → User decision on Phase 1 extension vs closure

---

## Quick Reference: What to Check Every Monday

1. **Email replies** (5 min): Score new replies 1–5, flag Score 4–5 as Tier 2 candidates
2. **Bitly clicks** (3 min): Record weekly totals, note any 5+ single-day spikes
3. **Web mentions** (4 min): Check Google Alerts, Regulations.gov, SSRN
4. **Dashboard update** (3 min): Refresh formulas, check if checkpoint date requires decision tree
5. **Total time**: 15–20 minutes

That's it. Everything else flows from those four inputs.

---

## Document Relationships

- **PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md** — Why these thresholds exist; per-constituency success definitions
- **PHASE_1_DECISION_TREES.md** — The decision tree logic (reference for checkpoints)
- **PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md** — The Google Sheets schema (reference for column setup)
- **DISTRIBUTION_GIST_URLS.md** — Canonical Gist URLs and Bitly mappings
- **DISTRIBUTION_OUTREACH_CONTACTS.md** — Tier 1 contact list (populate Contacts sheet from this)

---

**Status**: Production-ready. Use this as your Day 1 playbook on May 28.

