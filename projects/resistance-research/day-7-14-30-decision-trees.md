---
title: "Day 7–14–30 Decision Trees — Phase 1 Wave 1"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Executable decision trees for the three critical Phase 1 checkpoints.
  Specific numerical thresholds, logical branches, and immediate actions for each outcome.
  All deterministic — no subjective judgment required.
word_count: ~2200
companion_files:
  - PHASE_1_WAVE_1_MONITORING_DASHBOARD.md
  - reply-triage-framework.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - PHASE_1_DECISION_TREES.md (reference)
---

# Day 7–14–30 Decision Trees — Phase 1 Wave 1

**Version 1.0 — May 26, 2026**

Use these trees to make deterministic Phase 1 checkpoint decisions. Open your dashboard, pull the numbers, follow the tree, and execute the action at the terminal branch.

---

## Day 7 Checkpoint Decision Tree

**Run date**: 7 calendar days after Wave 1 send (May 28 Domain 56 send → June 4–5 checkpoint)

**Data to pull from dashboard**:
- Gist Views sheet: **Week 1 Bitly clicks** (total across both Domain 56 and Domain 39 links)
- Contacts sheet: **Reply count** (count of non-empty cells in Reply_Date column)
- Contacts sheet: **Delivery status** (count of "Bounced" in Delivery_Status column)

### Day 7 Decision Tree

```
START: Pull Week 1 Bitly clicks, total replies, bounce count

    ├─ [Check delivery first]
    │
    ├─ Bounced count ≥ 3?
    │  YES → DETERMINATION: CONTACT_VERIFY
    │        ACTION: Pull DISTRIBUTION_OUTREACH_CONTACTS.md
    │                Verify all email addresses are correct
    │                Check for typos, outdated emails
    │                Resend to corrected list
    │                Restart Day 7 clock (new send date = today)
    │                Document in CHECKIN.md: "Email verification re-send executed [date]"
    │
    │  NO → Continue to next check
    │
    ├─ [Check total Bitly clicks]
    │
    ├─ Total Bitly clicks ≥ 15?
    │  YES → Continue to reply check (below)
    │
    │  NO → Is it 5–14 clicks?
    │       YES → Goto: MONITOR branch (low engagement)
    │
    │       NO → Is it 0–4 clicks?
    │            YES → Goto: ESCALATE branch (delivery failure)
    │
    ├─ [Check reply count]
    │
    ├─ Total replies ≥ 2 (at any score)?
    │  YES → DETERMINATION: HOLD
    │        Proceed to normal Phase 1 trajectory
    │        (Continue monitoring, checkpoint again at Day 30)
    │
    │  NO → Is it 0–1 replies?
    │       YES → DETERMINATION: MONITOR
    │            Below baseline but not failure
    │            Check again at Day 14
    │            If still 0–1 at Day 14 → Apply Modification 2
    │                                        (framing revision, see below)
    │
    └─ MONITOR BRANCH (5–14 clicks + any reply count):
       DETERMINATION: MONITOR
       ACTION: Recheck at Day 14
               Monitor for email reply spikes Days 8–14
               If Day 14 shows 25+ cumulative clicks → Escalate to HOLD
               If Day 14 shows <10 cumulative clicks → Escalate to ESCALATE
    
    └─ ESCALATE BRANCH (0–4 clicks + confirmed delivery):
       DETERMINATION: ESCALATE
       ACTION: Within 24 hours:
               1. Verify Bitly link works (click it yourself in incognito browser)
               2. Check Gmail: Are the sent emails in spam folder?
               3. Forward one email to a test account, verify delivery and click
               4. If Bitly link is broken: Create new links and resend to full list
               5. If emails are in spam: Contact email provider or ask Tier 1 to check spam folder
               6. If test click works: Possible audience issue — proceed to Modification 2
               Document findings in CHECKIN.md: "Day 7 ESCALATE diagnostic completed [date]"
```

### Day 7 Determination Reference

| Determination | Criteria | Action | Next Checkpoint |
|---------------|----------|--------|-----------------|
| **HOLD** | 15+ clicks AND 2+ replies | None — proceed normally | Day 30 (skip Day 14) |
| **MONITOR** | 5–14 clicks OR 0–1 replies (but not both at zero) | Check again at Day 14 | Day 14 recheck |
| **ESCALATE** | 0–4 clicks with confirmed delivery | Delivery diagnostic + possible re-send | Restart Day 7 if re-send |
| **CONTACT_VERIFY** | 3+ bounced addresses | Fix emails, re-send to corrected list | Restart Day 7 |

### Day 7 Status Update to CHECKIN.md

Add an entry to CHECKIN.md under "Phase 1 Day 7 Checkpoint":

```
## Phase 1 Day 7 Checkpoint — [Date]

**Determination**: [HOLD / MONITOR / ESCALATE / CONTACT_VERIFY]

**Metrics**:
- Domain 56 clicks: [X]
- Domain 39 clicks: [X]
- Total replies: [X]
- Bounce rate: [X%]

**Decision**: [HOLD = Continue to Day 30]
           [MONITOR = Recheck at Day 14]
           [ESCALATE = Run diagnostic, possible re-send]

**Next action**: [e.g., "No action required; monitoring continues"; or "Day 14 recheck scheduled for June 11"]
```

---

## Day 14 Checkpoint (Optional – Applies Only if Day 7 = MONITOR)

**Run date**: 14 calendar days after Wave 1 send (June 11–12)

**Data to pull**:
- Gist Views sheet: **Cumulative clicks to date** (should be 30+ if on track)
- Contacts sheet: **Total replies to date** (should show upward trend from Day 7)

### Day 14 Micro-Checkpoint Decision Tree

```
START: Pull cumulative Bitly clicks and total replies

    ├─ Cumulative clicks ≥ 25?
    │  YES → Engagement recovering; trajectory positive
    │        DETERMINATION: Escalate to HOLD
    │        ACTION: No action; continue to Day 30
    │        Next checkpoint: Day 30 (June 27–28)
    │
    │  NO → Continue below
    │
    ├─ Cumulative clicks 10–24?
    │  YES → Engagement stalled; below target but not zero
    │        DETERMINATION: CONTINUE_MONITOR
    │        ACTION: Apply Modification 2 (framing revision)
    │                 Prepare revised email with single-domain focus
    │                 (See failure recovery protocol in PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md)
    │                 Plan for Day 45 re-send with adjusted approach
    │        Next checkpoint: Day 30 (normal schedule)
    │
    │  NO → Continue below
    │
    └─ Cumulative clicks < 10?
       DETERMINATION: FAILURE_IMMINENT
       ACTION: Within 48 hours:
               1. Contact Tier 1 directly (phone/video if possible)
                  Sample script: "Hi [Name], I sent a framework on [date].
                                 Did you receive it? Any technical issues?
                                 Happy to resend or discuss any questions."
               2. Resend to corrected list if addresses were wrong
               3. Create new Bitly links (old ones may be broken)
               4. Full failure recovery protocol (see PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md)
       Next checkpoint: Day 30 (normal schedule, but with contingency mode active)
```

### Day 14 Status Update

```
## Phase 1 Day 14 Micro-Checkpoint — [Date]

**Determination**: [HOLD / CONTINUE_MONITOR / FAILURE_IMMINENT]

**Cumulative metrics**:
- Cumulative clicks: [X]
- Total replies: [X]

**Decision**: [If HOLD: Continue to Day 30 with no changes]
           [If CONTINUE_MONITOR: Apply Modification 2 framing revision by Day 21]
           [If FAILURE_IMMINENT: Execute failure recovery protocol]

**Failure recovery actions taken**: [List any diagnostic calls, re-sends, etc.]
```

---

## Day 30 Checkpoint Decision Tree

**Run date**: 30 calendar days after Wave 1 send (June 27–28)

**Critical**: This checkpoint determines whether Phase 2 launches immediately, is delayed, or requires contingency planning.

**Data to pull from dashboard**:
- Contacts sheet: **Score 3+ reply rate** = (count of Score 3+ replies) / (count of delivered emails)
- Constituencies sheet: **Count of constituencies with ≥3 Score 3+ replies** (Law Schools, Immigration Legal Aid, etc.)
- Adoptions sheet: **Count of confirmed adoption signals** (Verification_Status = "Confirmed")
- Network Map sheet: **Count of cross-organizational referrals** (confirmed or probable)

**Threshold note**: The checks below run in order from highest to lowest. Check FAILURE first (most severe), then STRONG (most positive), then MODERATE, then WEAK, then ASSESS. The FAILURE check fires before any other branch if Week 3–4 Bitly clicks are zero — that condition is catastrophic regardless of other metrics. If FAILURE does not fire, proceed to STRONG.

### Day 30 Decision Tree

```
START: Pull four numbers from dashboard

(A) Score 3+ reply rate [%]
(B) Constituencies passing strong threshold [count out of 7]
(C) Cross-organizational references [count]
(D) Confirmed adoption signals [count]
(E) Week 3-4 Gist Views sheet: were Bitly clicks zero in both Week 3 AND Week 4? [YES/NO]

    ├─ [Check FAILURE first — most severe condition]
    │
    ├─ A < 10% AND C = 0 AND D = 0 AND E = YES?
    │
    │  YES → DETERMINATION: FAILURE
    │        Phase 1 severely underperforming. Stop here. Do not evaluate other branches.
    │
    │        ACTION: User decision required (within 48 hours).
    │        Update CHECKIN.md under "Needs Your Input" with all four metrics.
    │        Present three options:
    │        1. CONTINUE: Apply full failure recovery (Modifications 1–3 + 90-day extension)
    │        2. PIVOT: Shift to public-channel distribution only (no more direct outreach)
    │        3. CLOSE: End Phase 1 and move to Phase 2 with whatever social proof exists
    │        User selects path within 48 hours.
    │        Send Domain 39 regardless of FAILURE (healthcare deadline is non-negotiable).
    │
    │  NO → Continue to STRONG check
    │
    ├─ [Check for STRONG threshold]
    │
    ├─ A ≥ 50% AND B ≥ 4 AND C ≥ 3 AND D ≥ 2?
    │
    │  YES → DETERMINATION: STRONG
    │        Phase 2 launches immediately.
    │
    │        IMMEDIATE ACTIONS (within 24 hours):
    │        1. Update CHECKIN.md with STRONG result
    │        2. Prepare Domain 39 distribution materials:
    │           - Pull 5 contact email addresses from DISTRIBUTION_OUTREACH_CONTACTS.md
    │           - Prepare email template with Domain 39 Gist link
    │           - Include 2–3 quotes from Score 4–5 Tier 1 replies as social proof
    │        3. Send Domain 39 distribution by end of Day 1
    │           (June 1 HHS deadline applies — do not delay)
    │        4. Prepare Domain 56 distribution for launch within 48 hours
    │           - Gather quotes from Score 4–5 civil rights org replies
    │           - Prepare contact list (law school Tier 2 targets)
    │        5. Begin Tier 2 law school pre-outreach planning
    │           Use confirmed Score 4–5 orgs as anchor social proof
    │
    │  NO → Continue to MODERATE check
    │
    ├─ [Check for MODERATE threshold]
    │
    ├─ A 20–49% OR B ≥ 3 OR C ≥ 1 OR D ≥ 1?
    │  (Note: upper bound of A is 49% because ≥50% triggers STRONG above.
    │   Lower bound is 20% because <20% combined with all-zero B/C/D triggers WEAK below.
    │   If A is 20–49% but B/C/D are all zero, this still triggers MODERATE — partial signal.)
    │
    │  YES → DETERMINATION: MODERATE
    │        Domain 39 launches immediately (healthcare urgency).
    │        Phase 2 partial expansion.
    │
    │        ACTIONS (within 24–48 hours):
    │        1. Update CHECKIN.md with MODERATE result
    │        2. Send Domain 39 distribution within 24 hours
    │           (Same as STRONG — healthcare deadline non-negotiable)
    │        3. Hold Domain 56 distribution until Day 37–40
    │        4. Extend Phase 1 monitoring period through Day 60
    │           Continue weekly synthesis, Bitly tracking, reply scoring
    │        5. Prepare Tier 2 expansion planning but do NOT send yet
    │           Stage outreach materials for go-live at Day 37
    │
    │  NO → Continue to WEAK check
    │
    ├─ [Check for WEAK threshold]
    │
    ├─ A < 20% AND B < 2 AND C = 0 AND D = 0?
    │  (All four conditions must be true simultaneously. If any single one is not,
    │   the result falls in the ASSESS zone between WEAK and MODERATE — see below.)
    │
    │  YES → DETERMINATION: WEAK
    │        Phase 1 not tracking targets. Contingency activation required.
    │
    │        DO NOT extend Phase 1 unchanged.
    │        Apply 3-modification failure recovery:
    │
    │        MODIFICATION 1: Stakeholder substitution (by Day 37)
    │        - Replace 30% of non-responding Tier 1 with Tier 1.5 contacts
    │          (clinic directors instead of school deans, state chapter leads
    │           instead of national directors, etc.)
    │        - Prepare contact list by Day 32
    │        - Execute outreach by Day 40
    │
    │        MODIFICATION 2: Framing revision (by Day 35)
    │        - Shift from "35-domain framework overview"
    │          to "single-domain operational resource"
    │        - Law schools: "40-page election interference analysis for clinic use"
    │        - Immigration legal aid: "Model brief framework for prosecutorial
    │          weaponization brief adaptation"
    │        - Civil rights: "Litigation tracker ready for [active case/campaign]"
    │        - Prepare revised email template by Day 32
    │        - Execute re-send by Day 42
    │
    │        MODIFICATION 3: Channel shift (by Day 45)
    │        - Move 50% effort from direct email to network intermediaries
    │        - Identify 2–3 strong advocates from Day 30 replies (Score 3+)
    │        - Ask them: "Would you share with 2–3 peer organizations?"
    │        - Submit domain summaries to Just Security, Lawfare, journals
    │        - Deposit framework in conference pre-read packets
    │        - Contact state/local bar associations
    │
    │        ACTIONS (by Day 32):
    │        1. Update CHECKIN.md with WEAK result + 3 modifications listed
    │        2. Send Domain 39 anyway (healthcare urgency overrides weak signal)
    │        3. Do NOT send Domain 56 yet; hold until Day 60 checkpoint
    │        4. Prepare Modification 1 + 2 contact lists and email templates
    │        5. Set Day 90 extension checkpoint (extended timeline for Phase 1)
    │
    │  NO → [Between WEAK and MODERATE: some signals but below MODERATE threshold]
    │       DETERMINATION: ASSESS
    │       This applies when A is 10–19% with B≥1 or C≥1 or D≥1 — partial signals
    │       that do not qualify for MODERATE but are better than WEAK.
    │       ACTION: Send Domain 39 only (healthcare deadline non-negotiable)
    │              Continue Phase 1 monitoring through Day 60
    │              Prepare both contingency AND normal Phase 2 options in parallel
    │              Wait for Day 60 checkpoint with fuller data before committing
    │              Do NOT activate WEAK failure recovery yet
    │              Next checkpoint: Day 60 (July 27–28)
    │
    └─ [All checks complete. If you reach this point without a DETERMINATION:
       this should not happen — every combination of A/B/C/D values is covered
       by FAILURE, STRONG, MODERATE, WEAK, or ASSESS above.]
```

### Day 30 Determination Reference Table

Check order: FAILURE first, then STRONG, MODERATE, WEAK, ASSESS.

| Determination | Criteria (all conditions listed must be true) | Domain 39 | Domain 56 | Phase 2 Tier 2 | Timeline |
|---------------|----------------------------------------------|-----------|-----------|----------------|----------|
| **FAILURE** | A<10% AND C=0 AND D=0 AND Week 3+4 Bitly=0 | Send immediately (healthcare non-negotiable) | User decision | User decision | User decides within 48h |
| **STRONG** | A≥50% AND B≥4 AND C≥3 AND D≥2 | Launch Day 1 | Launch Day 1–2 | Begin immediately | Full scale |
| **MODERATE** | A 20–49% OR B≥3 OR C≥1 OR D≥1 (but not STRONG) | Launch Day 1 | Hold to Day 37 | Plan but wait | Partial scale |
| **WEAK** | A<20% AND B<2 AND C=0 AND D=0 (but not FAILURE) | Launch Day 1 | Hold to Day 60 | Not yet — apply recovery Mods 1–3 | Extended to Day 90 |
| **ASSESS** | Partial signals: some of A/B/C/D above zero but below MODERATE threshold | Launch Day 1 | Hold to Day 60 | Prepare both paths | Wait for Day 60 |

### Day 30 Status Update to CHECKIN.md

```
## Phase 1 Day 30 Checkpoint — [Date]

**Determination**: [STRONG / MODERATE / WEAK / ASSESS / FAILURE]

**Metrics at Day 30**:
- Score 3+ reply rate: [X%]
- Constituencies passing strong threshold: [X of 7]
- Cross-org references: [X]
- Confirmed adoptions: [X]

**Phase 2 Decisions**:
- Domain 39 status: [LAUNCHED / LAUNCHING SOON / HOLD]
- Domain 56 status: [LAUNCHED / LAUNCHING SOON / HOLD]
- Tier 2 expansion: [BEGAN / PLANNED FOR DAY X / CONTINGENT / NOT STARTING]

**Contingency modifications activated** (if WEAK):
- [ ] Modification 1 (Stakeholder substitution) by Day 37
- [ ] Modification 2 (Framing revision) by Day 35
- [ ] Modification 3 (Channel shift) by Day 45
- [ ] Day 90 extension checkpoint set

**Next checkpoint**: [Day 60 (July 28–29) / OR Day 90 if contingency / OR User decision required]
```

---

## Pre-Day-30 Rapid-Response Signals

If a **Score 5 event** is received before Day 30 (any single contact reporting adoption), trigger **immediate Phase 2 pre-activation** regardless of calendar date:

```
Score 5 DETECTED (before Day 30)
├─ Adoption confirmed from [Organization]: [Description]
├─ DECISION: Pre-activate Phase 2 immediately
│
└─ ACTIONS (within 24 hours):
   1. Log in Adoptions sheet
   2. Email user: "Score 5 received from [Org] — Phase 2 pre-activation underway"
   3. Prepare Domain 39 distribution (send within 48 hours)
   4. Prepare Domain 56 distribution (send within 48 hours)
   5. Do NOT wait for Day 30 checkpoint
```

Similarly, **two or more Score 4 events within 14 days** is a pre-Day-30 STRONG signal:

```
Score 4 CLUSTER (2+ Score 4s within first 14 days)
├─ Partnership requests from [Org 1] and [Org 2]
├─ DECISION: Early STRONG signal (treat as pre-Day-30 STRONG determination)
│
└─ ACTIONS (within 24 hours):
   1. Email user: "Score 4 cluster detected — Phase 2 pre-activation underway"
   2. Execute STRONG protocol (see Day 30 tree above)
   3. Launch Domain 39 + Domain 56 within 48 hours
   4. Begin Tier 2 social proof outreach using Score 4 partnerships
```

---

## Quick Reference: Checkpoint Dates & Actions

| Checkpoint | Date | Decision Options | If STRONG | If MODERATE | If WEAK | If FAILURE |
|-----------|------|---|---|---|---|---|
| **Day 7** | June 4–5 | HOLD / MONITOR / ESCALATE | N/A | Recheck Day 14 | Diagnostic + possible re-send | Verify emails |
| **Day 14** | June 11–12 | HOLD / CONTINUE_MONITOR / FAILURE_IMMINENT | (implied HOLD) | Apply Modification 2 | Execute failure recovery | Contact Tier 1 directly |
| **Day 30** | June 27–28 | STRONG / MODERATE / WEAK / ASSESS / FAILURE | Launch both domains | Domain 39 launch, 56 delayed | Activate recovery, send Domain 39 | User decision |
| **Day 60** | July 28–29 | MOVEMENT / PARTIAL / BELOW_TARGET | Full Phase 2 launch all constituencies | Phase 2 for confirmed adoption constituencies | Extended Phase 1 or close | User review |

---

**Status**: Production-ready. Use these trees starting June 4 (Day 7 checkpoint) through July 28 (Day 60 checkpoint).

