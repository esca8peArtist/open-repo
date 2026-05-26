---
title: "Day 7 / Day 14 / Day 30 Decision Trees — Phase 1 Synthesis Outcome Logic"
created: 2026-05-27
version: 1.0
status: production-ready
scope: >
  Three decision trees with specific numeric thresholds for checkpoints after Domain 56
  (May 28 send) and Domain 39 (June 1 send). Each tree terminates in a named action
  with no "wait for Claude" branches. Includes Phase 2 timing decision logic: when to
  escalate Tier 2, when to pause, when to pivot messaging.
checkpoint_dates:
  day_7_d56: "June 4, 2026 (Domain 56 reference date)"
  day_7_d39: "June 8, 2026 (Domain 39 reference date)"
  day_14: "June 11, 2026"
  day_30: "June 27, 2026"
data_sources:
  - "PHASE_1_IMPACT_MONITORING_DASHBOARD.md (this directory)"
  - "Google Sheets dashboard — Contacts tab, Gist_Views tab, Checkpoints tab"
---

# Day 7 / Day 14 / Day 30 Decision Trees

**Version 1.0 — May 27, 2026**

**How to use this document**: Open your Google Sheets dashboard first. Pull the four numbers listed at the top of each tree. Then follow the branches — every branch terminates in a named action. All actions can be executed the same day without additional research or consultation.

**Domain 39 is non-negotiable throughout**: In every tree, every branch — Domain 39 sends to all 5 contacts regardless of any engagement metric. The June 1 HHS deadline overrides all Phase 2 sequencing decisions. The Domain 39 send instruction appears explicitly in every decision path below.

---

## Score 5 Override (Applies at Any Time — Supersedes All Trees)

A Score 5 reply is: explicit citation in a formal document, institutional integration statement, or formal adoption confirmation. This is not a checkpoint — it is a standing trigger.

**When you receive a Score 5 reply, regardless of what day it is**:

1. Stop the current checkpoint tree — you do not need to finish it
2. Add to CHECKIN.md: "SCORE 5 RECEIVED — [date] — [org] — [domain] — [description]"
3. Within 24 hours: verify Domain 39 has been sent to all 5 contacts (if not, send immediately)
4. Within 48 hours: prepare Tier 2 outreach for the domain that generated the Score 5, using this social proof framing in the subject line: "[Org Name] is citing this research — [Domain title]"
5. Log in Adoptions tab: Signal_Type = [specific type], Verification_Status = Confirmed

Score 5 from Domain 56 does not automatically activate Domain 39 Tier 2 — these are separate distribution tracks. Handle each domain independently when applying the Score 5 override.

---

## Tree 1 — Day 7 Checkpoint

**Reference date**: June 4, 2026 (Domain 56, May 28 send)  
Secondary date: June 8, 2026 (Domain 39, June 1 send — run Tree 1 again on this date for Domain 39 only)

**Before starting, pull these three numbers from the dashboard**:
- (A) Week 1 total Bitly clicks: Gist_Views tab, Total_This_Week, row for Week 1
- (B) Total replies received: Contacts tab, auto-calculation row "Total replies"
- (C) Confirmed delivery count: Contacts tab, auto-calculation row "Confirmed delivered"

---

### Step 1: Delivery Integrity Check

Pull Contacts tab, filter Column I for "Bounced."

```
How many contacts bounced?

   3 or more              1–2                  0
        |                  |                   |
  PAUSE TREE.         Record bounce.         Continue to Step 2.
  Pull                Find corrected
  BATCH_1_CONTACT     email from org
  _VERIFICATION.md.   website. Resend.
  Re-verify all       Update Contacts
  emails before       tab: new address,
  any checkpoint      new Send_Date,
  calculations.       Delivery_Status
  Restart Day 7       reset to Unknown.
  clock from re-
  send date.
```

---

### Step 2: Bitly Clicks Check (Number A)

```
Number A (Week 1 total clicks):

   A >= 15                A = 5–14               A = 0–4
       |                      |                      |
   ON TRACK               MONITOR               INVESTIGATE
   Continue               Continue              Were emails sent?
   to Step 3.             to Step 3.            Check Gmail Sent.
                                                    |
                                              +-----+-----+
                                              |            |
                                           YES            NOT SURE
                                              |            |
                                         Emails sent    Confirm sends
                                         but 0 clicks.  then re-run.
                                              |
                                         ESCALATE:
                                         (1) Test each Bitly link —
                                             click it yourself and
                                             verify counter increments.
                                         (2) If link is broken:
                                             recreate the short link,
                                             resend corrected link to
                                             all contacts with a brief
                                             apology note.
                                         (3) Add ESCALATE note to
                                             CHECKIN.md: "Day 7 click
                                             investigation — [date]."
                                         (4) Restart Day 7 clock
                                             from corrected send date.
```

---

### Step 3: Reply Count Check (Number B, relative to C)

```
Number B (total replies):

   B >= 2                  B = 1                  B = 0
      |                     |                       |
   HOLD:               MONITOR:               MONITOR:
   Normal              Below baseline         Record.
   trajectory.         but not zero.          Check again
   Record in           Check again            Day 10-11.
   Checkpoints         Day 10-11.             If still 0
   tab:                                       replies by
   Determination                              Day 14, apply
   = HOLD.                                    framing
   Continue to                                revision
   Day 30.                                    (see Tree 2).
```

---

### Day 7 Determination — Record in Checkpoints Tab

| Determination | Criteria | Action |
|---------------|----------|--------|
| HOLD | A >= 15 AND B >= 2 | No action. Continue to Day 30. Next scheduled check: Day 14. |
| MONITOR | (A = 5–14 OR B = 0–1) with confirmed delivery | Do not resend yet. Check again Day 10–12. If still below threshold at Day 14, run Tree 2 early. |
| ESCALATE | A = 0–4 with confirmed delivery, OR 3+ bounces | Investigate delivery today. Resolve before Day 14. |

**After recording**: Add one line to WORKLOG.md: `[date] — Day 7 checkpoint: A=[clicks] B=[replies] Determination=[HOLD/MONITOR/ESCALATE]. Domain 56.`

**Run Tree 1 again on June 8 for Domain 39** (substituting Domain 39 Bitly link clicks for Number A).

---

## Tree 2 — Day 14 Mid-Cycle Checkpoint

**Reference date**: June 11, 2026

**Before starting, pull these four numbers**:
- (A) Cumulative Bitly clicks to date: Gist_Views tab, Cumulative column, latest row
- (B) Total replies received: Contacts tab, auto-calculation
- (C) Day 7 determination: Checkpoints tab (HOLD / MONITOR / ESCALATE)
- (D) Overall reply rate: Contacts tab, auto-calculation (Total replies / Confirmed delivered)

---

### Step 1: Day 7 Status Check (Number C)

```
C = HOLD         C = MONITOR         C = ESCALATE
    |                  |                   |
Continue           Continue         Was the delivery
to Step 2.         to Step 2.       problem resolved?
                   (mid-cycle)           |
                                    +----+----+
                                    |         |
                                   YES        NO
                                    |         |
                               Continue   Add to CHECKIN.md:
                               to Step 2. "Delivery problem
                                          unresolved — Day 14.
                                          [description]."
                                          Do NOT include
                                          undelivered contacts
                                          in any threshold
                                          calculations.
                                          STOP TREE.
```

---

### Step 2: Cumulative Clicks Check (Number A)

```
A >= 25               A = 10–24              A < 10
    |                      |                     |
ON TRACK           BELOW TARGET           LOW SIGNAL:
Continue           Continue               Consider resend
to Step 3.         to Step 3.             to non-responders
                                          with revised
                                          subject line.
                                          See Messaging
                                          Revision section
                                          below before
                                          resending.
```

---

### Step 3: Reply Rate Check (Number D)

```
D >= 20%              D = 10–19%             D < 10%
    |                      |                     |
STRONG START:         MODERATE:           LOW TRAJECTORY:
Continue              Continue            Continue to
to Step 4.            to Step 4.          Step 4. Flag
                                          WEAK trajectory
                                          risk in
                                          Checkpoints tab.
```

---

### Step 4: Early Activation Check

```
Has any Score 5 reply been received at any point so far?
(Score 5 = formal adoption, institutional integration, citation confirmation)

        YES                              NO
         |                               |
   EARLY SIGNAL:                 Has 2+ Score 4 replies been received?
   Execute Phase 2               (Score 4 = forward to colleague,
   pre-activation                collaboration request)
   checklist from
   PHASE_1_IMPACT_                    YES              NO
   EVALUATION_                         |                |
   FRAMEWORK.md              PRE-DAY 30          No early
   Section 6.1.              STRONG signal.      activation.
   See also Score 5           Flag in             Continue
   Override above.            CHECKIN.md:         monitoring.
                              "2x Score 4 at      Day 30 is
                              Day 14."            next gate.
                              Continue
                              monitoring.
```

---

### Day 14 Determination — Record in Checkpoints Tab

| Signal | Criteria | Day 30 Forecast | Action |
|--------|----------|-----------------|--------|
| Strong trajectory | A >= 25 AND D >= 20% | Day 30 STRONG likely | No action. Continue. |
| Moderate trajectory | A >= 10 AND D >= 10% | Day 30 MODERATE likely | No action. Continue. |
| Weak trajectory | A < 10 OR D < 10% | Day 30 WEAK risk | Apply messaging revision now — do not wait for Day 30 |
| Early activation | Score 5 received OR 2+ Score 4 | Pre-Day 30 STRONG | Execute Phase 2 pre-activation |

**If Day 14 shows weak trajectory — messaging revision protocol**:

Do not resend with the same subject line to the same contacts. The most common cause of a low click rate at Day 14 is a subject line that does not signal operational urgency to the recipient.

**Revised subject line for Domain 56 non-responders** (resend June 12–14):
```
H.R. 492 Markup Window Now Open — Civil Service Democratic-Design Analysis
```

**Revised subject line for Domain 39 non-responders** (resend June 12–14):
```
HHS Work Requirement Rule Published — [Organization Name] Advocacy Response Support
```

Personalize the email opening: in the first sentence, reference the specific work the organization is currently doing (check their recent publications or announcements) and connect it directly to the domain. Do not resend the original email unchanged.

**After recording**: Add one line to WORKLOG.md: `[date] — Day 14 checkpoint: A=[clicks] D=[reply rate] Determination=[trajectory]. Domain 56 + 39.`

---

## Tree 3 — Day 30 Checkpoint (Phase 2 Go/No-Go)

**Reference date**: June 27, 2026

**This is the primary Phase 2 timing decision.** Every branch below terminates in a Phase 2 activation decision, a pause decision, or a pivot decision. There is no "wait and see" branch at Day 30.

**Before starting, pull these five numbers**:
- (A) Score 3+ reply rate: Contacts tab, auto-calculation "Score 3+ rate"
- (B) Constituencies meeting Day 30 strong threshold: Constituencies tab, COUNTIF of "Day30_Strong" = YES
- (C) Cross-org references confirmed: Contacts tab, COUNTA of "Referral_Made" column
- (D) Confirmed adoption signals: Adoptions tab, COUNTIF "Verification_Status" = Confirmed
- (E) Gist click activity in Weeks 3–4: Gist_Views tab, rows for Weeks 3 and 4 — are Total_This_Week values above zero?

---

### Gate 1: STRONG Threshold Check

```
Does ALL of the following hold?
  A >= 50% (Score 3+ rate)
  AND B >= 4 (constituencies strong)
  AND C >= 3 (cross-org references)
  AND D >= 2 (confirmed adoptions)

             YES                               NO
              |                                |
   DETERMINATION: STRONG                  Go to Gate 2.
              |
   Execute same day:
   (1) Add "STRONG" to CHECKIN.md with
       per-metric breakdown
   (2) Domain 39: Verify all 5 contacts
       have been sent. If any missed, send
       immediately — HHS rule is live
   (3) Domain 56: Verify Gist is current
       (check gist.github.com/esca8peArtist/
       8f11e868397921a4e6556b41196d1b1f)
   (4) Within 24 hours: Begin Domain 56
       Tier 2 outreach to next-tier contacts
       (Brookings, NAPA if not yet sent) using
       social proof framing from Tier 1 replies
   (5) Within 48 hours: Begin Tier 2 outreach
       for Domain 39 to healthcare advocacy orgs
       not in original Tier 1 list
   (6) Within 48 hours: Begin Tier 2 law school
       outreach using confirmed Tier 1 social proof
   STOP TREE. Phase 2 fully activated.
```

---

### Gate 2: MODERATE Threshold Check

```
Does ANY of the following hold?
  A = 30–49% (Score 3+ rate between 30-49%)
  OR B >= 3 (3+ constituencies strong)
  OR C >= 1 (at least 1 cross-org reference)
  OR D >= 1 (at least 1 confirmed adoption)

             YES                               NO
              |                                |
   DETERMINATION: MODERATE              Go to Gate 3.
              |
   Execute within 24–48 hours:
   (1) Add "MODERATE" to CHECKIN.md
   (2) Domain 39: Send to all 5 contacts
       within 24 hours regardless — June 1
       deadline has passed but advocacy
       window is still open
   (3) Domain 56: Extend Phase 1 monitoring
       to Day 60; prepare but do not send
       Tier 2 outreach yet
   (4) At Day 37–40: Re-assess Domain 56
       Tier 2 readiness with 10 more days
       of engagement data
   (5) Hold full Tier 2 expansion until
       Day 60 checkpoint provides
       additional signal
   STOP TREE.
```

---

### Gate 3: Weak Signal Check

```
Does ALL of the following hold?
  A < 20% (Score 3+ rate below 20%)
  AND B < 2 (fewer than 2 constituencies strong)
  AND C = 0 (no cross-org references)

             YES                               NO
              |                          (In between: not
              |                           clearly WEAK but
              |                           not qualifying for
              |                           MODERATE either)
              |                                |
   Go to Gate 4.                    DETERMINATION: HOLD
                                    Set a Day 45 checkpoint
                                    (July 12, 2026). Re-run
                                    Gate 2 on that date.
                                    Domain 39: send regardless.
```

---

### Gate 4: WEAK vs. FAILURE Check

```
(Only reach this gate if Gate 3 = YES)

Does ALL of the following hold?
  A < 10% (Score 3+ rate below 10%)
  AND C = 0 (no cross-org references)
  AND D = 0 (no confirmed adoptions)
  AND E shows zero Gist clicks in Weeks 3–4

             YES                               NO
              |                                |
   DETERMINATION: FAILURE             DETERMINATION: WEAK
              |                                |
   Add "FAILURE" to CHECKIN.md      Execute within 72 hours:
   under "Needs Your Input."        (1) Add "WEAK" to CHECKIN.md
   Full contingency review               under "Needs Your Input"
   required before Phase 2.        (2) Domain 39: Send regardless.
   Do not proceed with             (3) Domain 56: Do NOT send
   any Tier 2 outreach until            Tier 2 yet.
   you have reviewed and           (4) Apply 3-modification
   made a decision.                     failure recovery:
                                        MOD 1 — Stakeholder sub:
                                        Replace 30% of non-
                                        responding contacts with
                                        next-tier equivalents
                                        (clinic directors not
                                        deans; state chapters
                                        not national)
                                        MOD 2 — Single-domain
                                        pitch: Drop full framework
                                        overview. Lead with one
                                        domain specific to each
                                        contact's current work.
                                        MOD 3 — Network
                                        intermediary: Any Score 3+
                                        reply holder is now an
                                        intermediary candidate.
                                        Ask them to distribute
                                        internally rather than
                                        you sending directly.
                                   (5) Set Day 60 checkpoint
                                        for WEAK recovery
                                        assessment.
```

---

### Day 30 Per-Constituency Strong Thresholds

Use these to populate the Constituencies tab "Day30_Strong" column (YES / NO) before running Tree 3.

| Constituency | Strong Criteria (Day 30) |
|--------------|--------------------------|
| Civil Service Reform | 2+ contacts replied at Score 3+, OR 1 confirmed use in an advocacy document |
| Federal Employee Union | 2+ contacts engaged at Score 2+, OR 1 confirmed training integration |
| Civil Rights / Rule of Law | 2+ contacts replied at Score 3+, OR 1 confirmed policy document adoption |
| Watchdog / Media | 1 substantive reply at Score 3+, OR Government Executive editorial acceptance |
| Healthcare Policy | 2+ contacts replied at Score 3+, OR 1 confirmed public comment citation |
| Maternal Health | 1 substantive reply at Score 3+, OR 1 confirmed coalition integration |

A constituency "passes" (Day30_Strong = YES) if it meets the criteria above. Any constituency with zero engagement at Day 30 — regardless of whether the other constituencies are strong — is a WEAK signal for that constituency and feeds the B value (constituencies strong count) downward.

---

### Day 30 Domain 39 Non-Negotiable Action

Regardless of which gate is reached in Tree 3 — STRONG, MODERATE, WEAK, or FAILURE — execute the following for Domain 39:

1. Confirm all 5 contacts (Georgetown CCF, NHeLP, Brennan Center, IRG, Black Mamas Matter) have been sent and received delivery confirmation
2. For any contact with no reply by Day 30: send a brief follow-up citing any concrete advocacy developments since June 1 (any state Medicaid waiver filings, any litigation filed, any HHS implementation guidance issued) as a new hook
3. Do not score Domain 39 as failing even if Domain 56 is WEAK or FAILURE — they are separate distribution tracks with separate audiences and different success criteria

---

## Cross-Tree Summary

| Checkpoint | Date | Number A | Number B | Pass Criteria | Action |
|------------|------|----------|----------|---------------|--------|
| Day 7 | June 4 | Week 1 Bitly clicks | Reply count | A >= 15 AND B >= 2 = HOLD | Record; continue to Day 30 |
| Day 7 (D39) | June 8 | D39 Week 1 clicks | D39 replies | A >= 8 AND B >= 1 = HOLD | Record; continue |
| Day 14 | June 11 | Cumulative clicks | Reply rate % | A >= 25 AND D >= 20% = Strong trajectory | No action if strong; messaging revision if weak |
| Day 30 | June 27 | Score 3+ rate | Constituencies strong | A >= 50% AND B >= 4 AND C >= 3 AND D >= 2 = STRONG | Phase 2 full activation |
| Day 30 moderate | June 27 | Score 3+ rate | Any constituency strong | A 30-49% OR B >= 3 OR C >= 1 OR D >= 1 = MODERATE | D39 immediate; D56 extended |
| Day 30 weak | June 27 | Score 3+ rate | Constituencies strong | A < 20% AND B < 2 AND C = 0 = WEAK | 3-mod recovery; D39 send regardless |

---

## Phase 2 Timing Decision Logic

### When to Escalate Tier 2

Escalate Tier 2 outreach immediately (do not wait for a checkpoint) when:
- A single Score 5 reply is received from any contact at any time
- Two or more Score 4 replies are received before Day 14
- An organic amplification spike occurs — Bitly clicks on a domain with no corresponding send, suggesting another party is sharing the link

Escalate Tier 2 at Day 30 when:
- STRONG determination is reached at Gate 1

### When to Pause

Pause all new outreach (not existing threads — those continue) when:
- Day 14 click count is below 10 AND reply rate is below 10% — investigate delivery before expanding contact list
- Three or more bounces are detected without corrected addresses — resolve delivery before new sends
- FAILURE determination at Gate 4 — stop and review with user before proceeding

Pausing means: do not send to new contacts. Continue responding to all existing replies on the Category-specific timelines from REPLY_TRIAGE_FRAMEWORK.md.

### When to Pivot Messaging

Pivot messaging (revise outreach content or framing) when:
- 30%+ critique rate in any 14-day window
- Day 14 weak trajectory determination
- Zero replies from a specific constituency after 14 days despite confirmed delivery (the framing may not match that constituency's priorities)

**Domain 56 pivot signals**: No reply from Democracy Forward by Day 10 despite confirmed delivery suggests the subject line or APA framing is not landing. Pivot: send a follow-up that leads with the H.R. 492 markup calendar rather than the litigation analysis.

**Domain 39 pivot signals**: No reply from Georgetown CCF or NHeLP by Day 7 suggests the democratic participation framing is either: (a) not connecting with their current work focus, or (b) the emails are in spam. Verify delivery first. If delivered, pivot to a subject line that leads with the specific HHS implementation discretion question rather than the broader democratic infrastructure thesis.

### Phase 2 Sequencing by Outcome

**STRONG + Day 30**: Full Phase 2 activation same day. Domain 39 Tier 2 (expanded healthcare advocacy orgs), Domain 56 Tier 2 (Brookings, NAPA, law school outreach), and Tier 2 expansion to remaining constituencies using Tier 1 social proof.

**MODERATE + Day 30**: Domain 39 Tier 2 activates. Domain 56 Tier 2 activates at Day 37–40. Tier 2 expansion for other constituencies holds until Day 60 checkpoint.

**WEAK + Day 30**: Domain 39 sends regardless. Domain 56 Tier 2 holds. Apply 3-modification failure recovery. Day 60 is the next go/no-go gate.

**FAILURE + Day 30**: Domain 39 sends regardless. All other Phase 2 activity holds. User decision required before proceeding.

---

*Record every checkpoint determination in the Checkpoints tab of the Google Sheets dashboard. Never edit past rows — the Checkpoints tab is append-only and serves as the authoritative decision log. All companion context is in PHASE_1_IMPACT_MONITORING_DASHBOARD.md and REPLY_TRIAGE_FRAMEWORK.md in this directory.*
