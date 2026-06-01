---
title: "Week 1 Data Collection Framework"
created: 2026-06-03
scope: "Day 1-7 checklist, Gist view velocity curve, reply triage rules, adoption scoring calibration"
status: production-ready
activates: June 3, 2026
---

# Week 1 Data Collection Framework

**Phase 1 Wave 1 — Days 1-7 (June 1-8, 2026)**

Domain 39 sent June 1. Domain 56 sent May 28 (Day 1 of that send). This framework covers the consolidated Week 1 monitoring window starting from the June 1 Domain 39 send, which is the primary distribution event.

---

## Day-by-Day Checklist

### Day 1 (June 1, 2026) — Send Day

Actions completed at send time:
- [ ] Bitly short links created for Domain 56 (bit.ly/drp-d56) and Domain 39 (bit.ly/drp-d39) before send
- [ ] Bitly links embedded in ALL outreach emails (not raw Gist URLs)
- [ ] Gmail filter active: replies from Phase 1 contacts auto-labeled "phase-1-responses"
- [ ] Google Sheets dashboard created and shared (anyone with link can view)
- [ ] Contacts tab populated with all 45 contacts; Delivery_Status = "Unknown" initially
- [ ] State.json baseline established (run: `python3 phase-1-adoption-tracking-script.py --run-now`)

Baseline metric pull (do this within 2 hours of send):
- Log in to bitly.com — record all Bitly click counts at 0 (Day 0 baseline)
- Open Google Sheets > Gist_Views tab > enter row 1 with Week 1 start (all zeros)
- Note the send timestamp; Day 7 checkpoint runs exactly 7 calendar days later

---

### Day 2 (June 2)

Morning check (5 minutes):
- [ ] Check Gmail "phase-1-responses" label — any early replies?
- [ ] Note: replies in the first 24-48 hours are typically OOO auto-replies or quick acknowledgments. Do not score prematurely.

If any replies received:
- Enter in Replies tab (Reply_ID, Contact_ID, Reply_Date, Reply_Score, Reply_Type)
- If Score 4 or 5: flag in CHECKIN.md same day

Bitly: No pull needed today. Day 1 data is too thin to be meaningful.

---

### Day 3 (June 3)

Mid-week signal check (10 minutes):
- [ ] Pull Bitly click counts from bitly.com > Analytics > select "Last 3 days"
- [ ] Enter in Gist_Views tab, Spike_Notes column: note any single-link spikes
- [ ] Check Gmail "phase-1-responses" label

Velocity interpretation:
- 3+ clicks by Day 3 on Domain 39: on pace for Week 1 target
- 0 clicks by Day 3 AND 0 replies: check whether Bitly links were actually embedded in sent emails (review sent folder)
- Single large spike (10+ clicks on one link in one day): likely a single person sharing internally — note organization if identifiable from reply context

Reply triage (apply to any replies received Days 1-3):

| Score | Criteria | Action |
|-------|----------|--------|
| 1 | OOO auto-reply only | Log; set reminder for return date |
| 2 | "Thanks for sharing" with no substantive content | Log; no action |
| 3 | Question about methodology/content OR forward stated | Log; respond within 48h |
| 4 | Intent to use / request to adapt / names a specific case | Log; respond same day; flag Tier 2 candidate |
| 5 | Adoption confirmed (published output, court filing, curriculum adoption) | Log; CHECKIN.md same day; pre-activate Phase 2 |

---

### Day 4 (June 4) — Week 1 Check-In

This is also the Day 7 checkpoint for the Domain 56 send (May 28 + 7 days).

Full Week 1 synthesis if Day 7 checkpoint runs today:
- [ ] Pull all Bitly click counts (7-day window since send)
- [ ] Count total replies (any score) across both Domain 56 and Domain 39 sends
- [ ] Count bounces (Delivery_Status = "Bounced" in Contacts tab)
- [ ] Run Day 7 decision tree: `python3 phase-1-adoption-tracking-script.py --day7-report`
- [ ] Enter row in Checkpoints tab
- [ ] Update CHECKIN.md with determination (HOLD / MONITOR / ESCALATE / CONTACT_VERIFY)

Day 7 targets (system-level):
- Clicks >= 15: HOLD
- Clicks 5-14 or replies 0-1: MONITOR
- Clicks 0-4 with confirmed delivery: ESCALATE

---

### Day 5 (June 5)

Focus: Constituency-level triage

Review which constituencies have any signal and which have none:

| Constituency | Min Day 7 signal | Check |
|--------------|-----------------|-------|
| Law Schools | >= 2 Bitly clicks attributable to law school send | [ ] |
| Immigration Legal Aid | >= 1 click or reply | [ ] |
| Civil Rights | >= 1 click or reply | [ ] |
| Academic Research | >= 1 reply at any score | [ ] |
| Faith Coalitions | >= 1 click | [ ] |
| Labor Unions | >= 1 click | [ ] |
| Mutual Aid | >= 1 click | [ ] |

A constituency with zero signal at Day 5 is not yet a problem. Flag it as WATCH only if still zero at Day 7.

---

### Day 6 (June 6)

Pre-checkpoint prep (5 minutes):
- [ ] Ensure all replies received Days 1-5 are entered and scored in Replies tab
- [ ] Verify Delivery_Status is filled for all 45 contacts (change "Unknown" to "Delivered" if no bounce and email was sent; "Bounced" only if you received a bounce notification)
- [ ] Check that Constituencies tab formula results are displaying correctly

No action items today unless an alert was triggered. Steady-state monitoring.

---

### Day 7 (June 7-8) — Formal Checkpoint

Full Day 7 checkpoint (15-20 minutes):

**Step 1: Pull the three numbers**
- Total Bitly clicks (all links, last 7 days): [X] — from bitly.com > Analytics
- Total replies (any score): [X] — Contacts tab summary row
- Total bounces: [X] — Contacts tab COUNTIF(G:G,"Bounced")

**Step 2: Run decision tree**
Open `day-7-14-30-decision-trees.md`, Day 7 section.
Follow tree with your three numbers.
Record determination: HOLD / MONITOR / ESCALATE / CONTACT_VERIFY

**Step 3: Run script report**
```
python3 phase-1-adoption-tracking-script.py --day7-report
```

**Step 4: Update Checkpoints tab**
Add row to Google Sheets Checkpoints tab with:
- Assessment_Date: today
- Checkpoint_Type: Day 7
- Overall_Reply_Rate: [formula result]
- Score3Plus_Rate: [formula result]
- Determination: [your result]

**Step 5: Update CHECKIN.md**
Copy the CHECKIN.md template from day-7-14-30-decision-trees.md and fill in.

**Step 6: Update Synthesis_Log tab**
Add Week 1 row with this week's metrics.

---

## Gist View Velocity Curve

GitHub does not expose view counts via API. The script uses comment/fork counts as proxy signals only. For real click data, use Bitly.

**Expected velocity curve — moderate positive scenario:**

| Day | Expected cumulative Bitly clicks | Interpretation |
|-----|----------------------------------|----------------|
| 1   | 0-2 | Send day; immediate openers only |
| 2   | 2-6 | Early engaged readers |
| 3   | 5-10 | Normal open window peaks Day 2-3 |
| 4   | 8-15 | Secondary wave (forwards from early readers) |
| 5   | 10-18 | Plateau begins |
| 7   | 12-25 | End of initial wave |
| 14  | 20-35 | Second wave from referrals |

**What the curve shape tells you:**

Healthy (Day 1-3 slow, Day 3-7 acceleration):
- Recipients are reading carefully and then forwarding
- Multiple people at one organization accessing the same Gist
- Interpret as: organizational circulation underway

Spike then flat (all clicks Day 1):
- One highly engaged person clicked multiple links immediately
- Low organizational circulation so far
- Interpret as: single-person engagement; watch for reply to confirm

Completely flat (0 clicks through Day 5):
- Bitly links may not have been embedded in sent emails
- Or emails went to spam
- Action: check sent folder; verify Bitly links are live; if dead, create new links and re-send

**Spike flag threshold**: Any single link with >= 5 clicks in one day = enter in Spike_Notes column. Possible cause: internal sharing event at a large organization.

---

## Reply Triage Rules

Apply these rules to every reply. Score first, then route.

### The 5-Second Classification Rule

Before scoring, ask: "Does this reply tell me anything about what the person plans to do with the material?"

- NO: Score 1 or 2 (OOO or polite ack)
- YES: Score 3, 4, or 5 depending on specificity

### Scoring Calibration Examples

**Score 1 — OOO only**
"I'm out of the office until June 10. I'll respond when I return."
Action: Log; add June 10 follow-up reminder to calendar.

**Score 2 — Polite ack, no substance**
"Thanks for sharing this important work."
"We appreciate you reaching out."
Action: Log. No follow-up needed. Do not upgrade to Score 3 even if the person is senior.

**Score 2 borderline — Vague forward**
"I'm going to pass this along to my team."
Action: Score 2 (vague forward; no named recipient, no stated use case). Upgrade to Score 3 only if they reply again with specifics.

**Score 3 — Substantive engagement**
"How are you distinguishing 'democratic erosion' from normal political contestation in Domain 37?"
"Your Domain 29 analysis aligns with what we're seeing in the Ninth Circuit. Tell me more about the prosecutorial pattern methodology."
"I'm sharing this with our election law seminar — do you have a syllabus-friendly version?"
Action: Log; respond within 48 hours. Flag as Tier 2 candidate if reply is from Tier 1 contact.

**Score 4 — Intent to use**
"I'm forwarding this to our litigation director for an amicus brief we're preparing."
"We want to integrate Domain 56 into our civil service training module for the fall cycle."
"I'm recommending this to our climate coalition steering committee — they'll find the executive authority sections directly relevant."
Action: Log; respond same day. Enter in Adoption Signal Registry as "Probable." Flag in CHECKIN.md.

**Score 5 — Adoption confirmed**
"We cited your Domain 29 analysis in our brief filed today in [case name] (PACER link: ...)"
"Our fall syllabus now includes the Phase 1 executive summary as required reading."
"We published a policy brief this week drawing on your Domain 56 framework — here's the link."
Action: Enter in Adoptions tab as Confirmed. CHECKIN.md same day. Pre-activate Phase 2.

### False Positive Prevention

Do NOT upgrade to Score 4 for:
- "This is impressive work" (flattery without intent statement)
- "I've bookmarked this" (reading intent, not use intent)
- "Relevant for our team" (vague; could mean anything)

DO upgrade to Score 4 for:
- Any specific named use case (amicus, training, policy brief, sermon series)
- Any specific named person receiving the forward (litigation director, etc.)
- Any request that implies active deployment (can you adapt this for courtroom use?)

### Constituency-Specific Reply Interpretation

**Law Schools**: The delay between Score 3 reply and Score 5 adoption is typically 60-90 days (publication cycle). A Score 3 from a faculty member in Week 1 is a strong leading indicator. Do not expect Level 5 by Day 30.

**Immigration Legal Aid**: Adoption timeline can be extremely fast (days) if active litigation is in progress. Any mention of a pending case should escalate to CHECKIN.md immediately.

**Civil Rights (ACLU, Brennan Center, etc.)**: Policy team referrals (Score 4) have a 30-60 day adoption cycle. A "passed to policy team" reply in Week 1 means Day 30-60 adoption is plausible.

**Academic Research**: Score 3 in Week 1 may be the ceiling for the first 30 days. Academic citation cycles run 90-180 days. Count Score 3 from academic contacts as a strong leading indicator, not a lagging one.

**Faith Coalitions**: Adoption signals often come via congregational communications that are not publicly accessible. A Score 4 (intent to use in sermon series) is high confidence for actual adoption.

**Labor Unions**: Training cycle timing is key. If a union contact says "our next training cycle is in September," that Score 3 reply converts to Score 5 in September — plan accordingly.

**Mutual Aid**: Local coordinators (not national umbrella contacts) are the real decision-makers. A Score 3 from a national contact is worth less than a Score 3 from a local network coordinator.

---

## Adoption Scoring Calibration

### Calibration Exercise (before Week 1 ends)

Before scoring your first batch of replies, run this calibration:

1. Read the five adoption level definitions in PHASE_1_MEASUREMENT_SYSTEM.md Section 2
2. Re-read the false positive prevention notes in each level definition
3. Apply the "5-second classification rule" to each reply before assigning a score
4. If uncertain between two scores, always assign the lower score (prevents inflation)
5. Re-score at Day 14 if additional context arrives (a Score 2 contact may follow up with a Score 4)

### Adoption Level Conversion Rates (expected baseline)

Based on cold institutional outreach benchmarks and Phase 1 contact quality:

| Level | Expected % of contacts | Expected count (45 contacts) |
|-------|------------------------|------------------------------|
| Level 0 (no engagement) | 40-60% | 18-27 |
| Level 1 (OOO/ack) | 15-25% | 7-11 |
| Level 2 (read, no reply) | 10-20% | 5-9 |
| Level 3 (substantive reply) | 10-15% | 5-7 |
| Level 4 (intent) | 3-8% | 1-4 |
| Level 5 (confirmed) | 0-3% | 0-1 (by Day 30) |

If your Week 1 results are significantly above these ranges (e.g., 4+ Level 3 replies), that is a positive signal — the contact list quality is high. Preserve those contacts for Tier 2 social proof framing.

If results are significantly below (0 Level 3 replies by Day 14 with confirmed delivery), that triggers the Day 14 framing revision (Modification 2).

### What Counts as "Strong" for Phase 2 Domain 58/59 Activation

Domain 58 (Tribal Sovereignty) activation gate — requires by Day 30:
- Score 3+ replies from: law schools OR civil rights orgs (this is Domain 58's primary audience)
- At least 1 constituency at strong threshold (3+ Score 3+ replies)
- No WEAK or FAILURE determination at Day 30

Domain 59 (Economic Precarity) activation gate — requires by Day 30:
- Score 3+ replies from: labor unions OR mutual aid OR academic (primary audience)
- MODERATE or better determination at Day 30
- No FAILURE determination

Both Domain 58 and 59 are in the existing contact list if those constituencies are represented. If labor/mutual aid constituencies show zero engagement at Day 14, reassess the Domain 59 targeting before committing to send.

---

## Integration with Existing Scripts and Templates

### Script invocation sequence for Week 1

```bash
# Day 1 — establish baseline
python3 phase-1-adoption-tracking-script.py --check-config
python3 phase-1-adoption-tracking-script.py --run-now

# Day 4 (or Day 7) — checkpoint
python3 phase-1-adoption-tracking-script.py --run-now
python3 phase-1-adoption-tracking-script.py --day7-report

# If ESCALATE or FAILURE_IMMINENT alerts in log:
# Review data/week-01-*.md summary
# Follow action steps in the alert
```

### Sheets update sequence (manual, 10 min/week)

1. bitly.com > Analytics > Last 7 days > enter per-link counts in Gist_Views tab
2. Gmail > phase-1-responses label > score each reply > enter in Replies tab
3. Update Contacts tab: Reply_Date, Reply_Score, Delivery_Status
4. Verify Constituencies tab formula results (no manual entry needed)
5. Checkpoint week only: enter row in Checkpoints tab, enter row in Synthesis_Log tab

### Weekly synthesis (Monday, 15-20 min)

Use PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md. Copy to:
`projects/resistance-research/monitoring/phase-1-week-1-synthesis-2026-06-08.md`

Complete Sections 1-6 every week. Sections 7-13 only in checkpoint weeks.

---

## Overhead Validation

Target: < 20 min/day user input, formulas autonomous.

| Activity | Frequency | Time |
|----------|-----------|------|
| Morning reply check (Gmail label) | Daily | 2 min |
| Reply scoring and Sheets entry | Per reply (~3 per week average) | 3 min/reply |
| Bitly pull and Sheets entry | Once per week (Monday) | 3 min |
| Script run | Once per week (Monday cron, no user action needed) | 0 min |
| Weekly synthesis (Sections 1-6) | Monday | 12 min |
| Checkpoint decision tree | Weeks 1, 2, 4, 8 | 20 min |
| CHECKIN.md update | As needed (~ 1x/week) | 5 min |

**Normal week total**: ~15-18 min
**Checkpoint week total**: ~35-40 min
**High-reply week total (Weeks 1-2)**: up to 45 min

All formula calculations in Constituencies, Adoptions summary, and Contacts summary rows run automatically when data is entered. No manual arithmetic required.
