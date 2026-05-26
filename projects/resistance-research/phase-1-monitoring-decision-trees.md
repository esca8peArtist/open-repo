---
title: "Phase 1 Monitoring — Checkpoint Decision Trees"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Three decision trees with numeric thresholds for Day 7, Day 14, and Day 30 checkpoints.
  Each tree terminates in an explicit action. No "wait for Claude" branches.
companion_files:
  - PHASE_1_MONITORING_DASHBOARD.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - PHASE_1_DECISION_TREES.md
checkpoint_dates:
  day_7: "June 4, 2026 (Domain 56 send: May 28)"
  day_14: "June 11, 2026"
  day_30: "June 27, 2026"
---

# Phase 1 Monitoring — Checkpoint Decision Trees

**Version 1.0 — May 26, 2026**

Run each tree on its checkpoint date. Open the dashboard first, pull the four numbers listed at the top of each tree, then follow the branches. Every branch terminates in a named action you can execute the same day without further consultation.

**Data sources**:
- Total Bitly clicks: Gist Views sheet, "Total_Clicks_This_Week" column for current week, "Cumulative_Clicks" for running total
- Reply count: Contacts sheet, auto-calculation row "Total replies"
- Score 3+ count and rate: Contacts sheet, auto-calculation row "Score 3+ count" and "Score 3+ rate"
- Constituency status: Constituencies sheet, columns G (Day7_Status), H (Day30_Strong), I (Day30_Moderate)
- Adoption signals: Adoptions sheet, COUNTIF of Confirmed rows
- Cross-org references: Contacts sheet, COUNTA of K column (Referral_Made)

---

## Tree 1 — Day 7 Checkpoint

**Run on**: June 4, 2026 (or 7 days after your actual first send date, if different from May 28)

**Pull these two numbers from the dashboard before starting**:
- (A) Week 1 total Bitly clicks (all links combined — Gist Views sheet, row 1, column I)
- (B) Total replies received (Contacts sheet, auto-calculation row)

```
PULL NUMBERS A AND B
         |
         v
STEP 1: CHECK DELIVERY INTEGRITY
         |
Did any emails bounce? (Contacts sheet: any rows with Delivery_Status = Bounced)
         |
    +----+----+
    |         |
  YES         NO — skip to Step 2
    |
How many bounces?
    |
  +---+---+
  |       |
 3+      1-2
  |       |
ACTION:  NOTE: Record bounce. Find
PAUSE.   correct email address from
Pull     organization website.
BATCH_1  Re-send to corrected address.
_CONTACT Continue tree.
_VERIF-
ICATION.md
Re-verify
all emails.
Re-send
corrected.
Restart
Day 7
clock.
         |
         v
STEP 2: CHECK BITLY CLICKS (Number A)
         |
         +---------------+--------------+
         |               |              |
    A >= 15          A = 5 to 14    A = 0 to 4
         |               |              |
    ON TRACK         MONITOR        INVESTIGATE
    Go to Step 3.    Go to Step 3.  Were emails
                                   actually sent?
                                       |
                                   +---+---+
                                   |       |
                                 YES,      NOT SURE:
                                 confirmed  Check Gmail
                                 sent but   Sent folder.
                                 0 clicks:  Confirm sends.
                                       |
                                   ESCALATE:
                                   (1) Test Bitly
                                   link manually
                                   by clicking it
                                   yourself.
                                   (2) Check Bitly
                                   dashboard for
                                   impressions vs.
                                   clicks.
                                   (3) If Bitly link
                                   is broken, create
                                   new short link,
                                   resend to all
                                   contacts with
                                   corrected link.
                                   Add ESCALATE note
                                   to CHECKIN.md.
         |
         v
STEP 3: CHECK REPLY COUNT (Number B)
         |
         +-------------+-------------+
         |             |             |
      B >= 2         B = 1        B = 0
         |             |             |
    HOLD:          MONITOR:     MONITOR:
    Normal         Below        Record. Check
    trajectory.    baseline     again Day 10.
    Record in      but not      If 0 replies
    Checkpoints    zero.        by Day 14,
    sheet.         Check        apply framing
    Continue       again        revision
    to Day 30.     Day 10-12.   (see below).
```

**Day 7 determination — record in Checkpoints sheet**:

| Determination | Criteria | Action |
|---------------|----------|--------|
| HOLD | A >= 15 AND B >= 2 | No action. Continue to Day 30. |
| MONITOR | A = 5-14 OR B = 0-1 (with confirmed delivery) | Check again at Day 14. Do not resend yet. |
| ESCALATE | A = 0-4 with confirmed delivery, OR 3+ bounces | Investigate delivery. Resolve before Day 14. |

**If MONITOR at Day 7**: Run the mid-cycle check at Day 10-12 (not a formal checkpoint — just pull numbers A and B again). If A has climbed above 15 and B is 1+, upgrade to HOLD. If still below thresholds at Day 14, the Tree 2 (Day 14) check applies.

---

## Tree 2 — Day 14 Checkpoint

**Run on**: June 11, 2026 (or 14 days after your actual first send date)

**Pull these four numbers from the dashboard before starting**:
- (A) Cumulative Bitly clicks to date (Gist Views sheet, Cumulative_Clicks column, latest row)
- (B) Total replies received (Contacts sheet, auto-calculation)
- (C) Day 7 determination from Checkpoints sheet (HOLD / MONITOR / ESCALATE)
- (D) Overall reply rate (Contacts sheet, auto-calculation: Total replies / Confirmed delivered)

```
PULL NUMBERS A, B, C, D
         |
         v
STEP 1: CHECK DAY 7 STATUS
         |
         +------------------+-------------------+
         |                  |                   |
   C = HOLD           C = MONITOR         C = ESCALATE
         |                  |                   |
  Go to Step 2.      Go to Step 2         Is the delivery
                     (mid-cycle           problem resolved?
                     check).                   |
                                          +----+----+
                                          |         |
                                         YES        NO
                                          |         |
                                     Go to      ADD TO CHECKIN.md
                                     Step 2.    under "Needs Your
                                                Input": describe
                                                delivery problem.
                                                STOP TREE.
                                                Do not count
                                                undelivered contacts
                                                in any threshold
                                                calculation.
         |
         v
STEP 2: CHECK CUMULATIVE CLICKS (Number A)
         |
         +--------------+--------------+
         |              |              |
      A >= 25        A = 10-24       A < 10
         |              |              |
    ON TRACK        BELOW TARGET   LOW SIGNAL:
    Go to Step 3.   Go to Step 3.  Consider
                                   resend with
                                   revised subject
                                   line to non-
                                   responders.
                                   See Modification 2
                                   in PHASE_1_DECISION_
                                   TREES.md before
                                   resending.
         |
         v
STEP 3: CHECK REPLY RATE (Number D)
         |
         +----------------+-----------------+
         |                |                 |
      D >= 20%         D = 10-19%         D < 10%
         |                |                 |
    STRONG START:      MODERATE:         LOW:
    Go to Step 4.      Go to Step 4.     Go to Step 4
                                         AND note WEAK
                                         trajectory
                                         risk.
         |
         v
STEP 4: EARLY ACTIVATION CHECK
         |
Have any Score 5 replies been received at any point so far?
(Score 5 = citation, formal adoption, explicit institutional use statement)
         |
         +------+------+
         |              |
        YES             NO
         |              |
    EARLY SIGNAL:   Have 2+ Score 4 replies been received?
    Execute         (Score 4 = forward to colleague, collaboration request)
    Phase 2             |
    pre-activation      +------+------+
    checklist.          |              |
    See PHASE_1_       YES             NO
    DECISION_           |              |
    TREES.md        PRE-DAY 30     No early
    Rapid-Response  STRONG         activation.
    Protocol.       signal.        Continue
                    Flag in        monitoring.
                    CHECKIN.md.    Day 30
                    Continue       checkpoint
                    monitoring.    is next gate.
```

**Day 14 summary — record in Checkpoints sheet**:

| Signal | Criteria | Day 30 Forecast |
|--------|----------|-----------------|
| Strong trajectory | A >= 25 AND D >= 20% | Day 30 STRONG likely |
| Moderate trajectory | A >= 10 AND D >= 10% | Day 30 MODERATE likely |
| Weak trajectory | A < 10 OR D < 10% | Day 30 WEAK risk — consider resend strategy now |
| Early activation triggered | Score 5 received OR 2+ Score 4 received | Pre-Day 30 activation — run pre-activation checklist |

**If Day 14 shows weak trajectory**: Do not wait for Day 30 to act. Review the subject line of your outreach email. The most common cause of low open/click rates is a generic subject line that does not signal urgency or specificity to the recipient's work. Consider resending to non-responders with a revised subject line that references the June 1 HHS deadline (for Domain 39) or the current federal workforce news cycle (for Domain 56).

---

## Tree 3 — Day 30 Checkpoint

**Run on**: June 27, 2026 (or 30 days after your actual first send date)

**Pull these five numbers from the dashboard before starting**:
- (A) Score 3+ reply rate (Contacts sheet: Score 3+ rate)
- (B) Constituencies meeting Day 30 Strong threshold (Constituencies sheet: COUNTIF of H column = "YES")
- (C) Cross-organizational references confirmed (Contacts sheet: COUNTA of K column)
- (D) Confirmed adoption signals (Adoptions sheet: COUNTIF Verification_Status = "Confirmed")
- (E) Gist click velocity in Weeks 3-4 (Gist Views sheet: rows for Weeks 3 and 4 — are they above zero?)

```
PULL NUMBERS A, B, C, D, E
         |
         v
GATE 1: STRONG THRESHOLD CHECK
Does A >= 50% AND B >= 4 AND C >= 3 AND D >= 2?
         |
         +------+------+
         |              |
        YES             NO
         |              |
    DETERMINATION:  Go to Gate 2.
    STRONG
         |
    Execute same-day:
    (1) Add STRONG to CHECKIN.md
    (2) Pull Domain 39 contacts
        (DOMAIN_39_DISTRIBUTION_
        STRATEGY.md) and send
        within 24 hours — June 1
        HHS deadline is hard stop
    (3) Verify Domain 56 Gist
        (gist.github.com/
        esca8peArtist/
        8f11e868397921a4e6556b41196d1b1f)
        is current
    (4) Begin Domain 56 Tier 2
        outreach within 48 hours
    (5) Begin Tier 2 law school
        pre-contact using social
        proof framing
    STOP TREE. Phase 2 activated.
         |
         v
GATE 2: MODERATE THRESHOLD CHECK
Does A = 30-49% OR B >= 3 OR C >= 1 OR D >= 1?
         |
         +------+------+
         |              |
        YES             NO
         |              |
    DETERMINATION:  Go to Gate 3.
    MODERATE
         |
    Execute within 24-48 hours:
    (1) Add MODERATE to CHECKIN.md
    (2) Send Domain 39 within 24
        hours regardless (June 1
        HHS deadline overrides
        all thresholds)
    (3) Extend Phase 1 monitoring
        to Day 60
    (4) Prepare Domain 56 for
        launch at Day 37-40
    (5) Hold Tier 2 expansion
        until Day 60
    STOP TREE.
         |
         v
GATE 3: WEAK SIGNAL CHECK
Does A < 20% AND B < 2 AND C = 0?
         |
         +------+------+
         |              |
        YES             NO
         |          (In between:
         |           not WEAK but
         |           not MODERATE.
         |           Hold to Day 45.
         |           Re-run Gate 2
         |           then.)
         |
    DETERMINATION:
    WEAK
         |
    Execute within 72 hours:
    (1) Add WEAK to CHECKIN.md
        under "Needs Your Input"
    (2) Send Domain 39 regardless
        (June 1 deadline)
    (3) Do NOT send Domain 56 yet
    (4) Apply 3-modification failure
        recovery:
        MOD 1: Replace 30% of non-
        responding contacts with
        next-tier equivalents
        (clinic directors not deans;
        state chapters not national
        directors)
        MOD 2: Shift to single-domain
        pitch — not full framework
        overview
        MOD 3: Shift 50% of effort
        to network-intermediary
        distribution (anyone who
        replied at Score 3+ is now
        an intermediary candidate)
    (5) Set Day 90 extension checkpoint
         |
         v
GATE 4: FAILURE SIGNAL CHECK (only if WEAK in Gate 3)
Does A < 10% AND C = 0 AND D = 0 AND E shows zero Gist clicks in Weeks 3-4?
         |
         +------+------+
         |              |
        YES             NO
         |              |
    DETERMINATION:  WEAK determination
    FAILURE         confirmed. Apply
         |          3-modification
    Add FAILURE     recovery as above.
    to CHECKIN.md   No failure review
    under "Needs    needed yet.
    Your Input."
    Full contingency
    review required.
    Do not proceed
    with Phase 2
    sequencing until
    user decision.
```

**Day 30 per-constituency strong thresholds** (for evaluating B — use these to fill in the Constituencies sheet):

| Constituency | Day 30 Strong Criteria |
|--------------|------------------------|
| Law Schools | 3+ contacts replied at Score 3+ |
| Immigration Legal Aid | 2+ orgs replied at Score 3+, OR 1 confirmed litigation use |
| Civil Rights Organizations | 3+ contacts engaged at Score 2+, OR 1 confirmed policy doc adoption |
| Academic Research | 2+ contacts replied substantively, OR 1 confirmed citation event |
| Faith Coalitions | 2+ contacts engaged, OR 1 confirmed pastoral/congregational use |
| Labor Unions | 2+ contacts engaged, OR 1 confirmed training integration |
| Mutual Aid Networks | 2+ contacts engaged, OR 1 confirmed governance use |

A constituency "passes" (H column = YES in Constituencies sheet) if it meets its strong criteria listed above.

---

## Quick-Reference: All Three Trees in One Table

| Checkpoint | Date | Key Metric A | Key Metric B | HOLD/PASS | MONITOR | ESCALATE/ACT |
|------------|------|--------------|--------------|-----------|---------|--------------|
| Day 7 | June 4 | Bitly clicks Week 1 | Reply count | A>=15, B>=2 | A=5-14 or B=0-1 | A<5 with confirmed delivery |
| Day 14 | June 11 | Cumulative clicks | Reply rate | A>=25, D>=20% | A=10-24 or D=10-19% | A<10 or D<10% |
| Day 30 | June 27 | Score 3+ rate | Constituencies Strong | A>=50%, B>=4 = STRONG | A=30-49% or B>=3 = MODERATE | A<20%, B<2 = WEAK |

**Domain 39 send is non-negotiable**: Regardless of Day 30 determination (STRONG, MODERATE, or WEAK), send Domain 39 distribution to all 5 contacts within 24 hours of the Day 30 checkpoint. The June 1 HHS deadline for public comment on the interim Medicaid rule is the hard external constraint — Phase 1 engagement metrics do not override it.

**Score 5 override**: A single Score 5 reply (formal adoption, citation, institutional integration statement) from any contact at any point in Phase 1 triggers immediate Phase 2 pre-activation. Do not wait for a checkpoint date. See PHASE_1_DECISION_TREES.md Rapid-Response Protocol.
