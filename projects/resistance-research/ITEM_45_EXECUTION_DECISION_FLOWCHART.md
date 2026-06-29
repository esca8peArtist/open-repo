---
title: "Item 45 — Execution Decision Flowchart"
subtitle: "Domain 51 Wave 1 + Domain M Contingency — June 30 / July 1-15"
created: "2026-06-29"
item: "Item 45"
type: "decision flowchart (ASCII)"
deadline: "2026-06-30 23:59 UTC (Domain 51) / 2026-07-15 23:59 UTC (Domain M contingency)"
---

# Item 45 — Execution Decision Flowchart

## Primary Decision Tree

```
====================================================================
START: You are reading this on June 29-30, 2026
====================================================================

STEP 1 — PRE-FLIGHT (5 minutes)
                 |
    +------------v-------------+
    |  Is Gist URL live?       |
    |  https://gist.github.com |
    |  /esca8peArtist/6dce895c |
    |  5192e6a3ba2abfed40733372|
    +------------+-------------+
                 |
       YES       |     NO
        |        |      |
        |        |      v
        |        |  STOP — recreate Gist
        |        |  (DOMAIN_51_CONTINGENCY_
        |        |   SB_299_FALLBACK.md)
        |        |      |
        |        +------+
        v
====================================================================
STEP 2 — WAVE 1 EXECUTION (June 30, any time before 22:29 UTC)
====================================================================

             |
             v
   Send 1: echlopak@campaignlegalcenter.org
   Subject: "Constitutional architecture research on
             Citizens United — Hawaii/Montana model
             + FEC collapse analysis"
             |
         Log send time UTC
         Set timer: 90 minutes
             |
             v
   [90 minute wait]
             |
             v
   Send 2: info@issueone.org
   Subject: "Dark money architecture research —
             FEC collapse documentation + state
             ballot measure analysis"
             |
         Log send time UTC
             |
             v
   WAVE 1 COMPLETE
             |
             v
====================================================================
STEP 3 — WAVE 2 EXECUTION (same session or June 30 morning)
         Must complete by June 30, 23:59 UTC
====================================================================

             |
             v
   Send 3: dkemp@commoncause.org
             [CC: info@commoncause.org]
   Subject: "Research on Citizens United architecture
             for CA Fair Elections Act campaign"
             |
         Log send time UTC
         Set timer: 90 minutes
             |
             v
   [90 minute wait]
             |
             v
   Send 4: lwvc@lwvc.org
   Subject: "Dark money architecture research for
             California Fair Elections Act campaign"
             |
         Log send time UTC
         Set timer: 90 minutes
             |
             v
   [90 minute wait]
             |
             v
   Send 5: info@CAclean.org
   NOTE: NOT cleanmoney.org — use CAclean.org
   Subject: "Dark money research for California
             Fair Elections Act — 58 citations"
             |
         Log send time UTC
             |
             v
   WAVE 2 COMPLETE
             |
====================================================================
STEP 4 — DEADLINE CHECK: June 30, 23:59 UTC
====================================================================

             |
    +--------v---------+
    | Were ALL 5 sends |
    | logged by        |
    | June 30 23:59 UTC|
    +--------+---------+
             |
     YES     |     NO / PARTIAL
      |      |          |
      v      |          v
   SUCCESS   |   +------+--------+
   Value:    |   | How many sends|
   100%      |   | completed?    |
   No        |   +------+--------+
   contingency|         |
   required  |    0-1   |   2-4
             |    sends  |   sends
             |     |     |     |
             |     v     |     v
             | FULL      | PARTIAL
             | CONTINGENCY| CONTINGENCY
             | (Domain 51 | (Domain 51
             | Tier 2 +   | Tier 2 for
             | Domain M)  | incomplete
             |     |      | + Domain M)
             |     |      |      |
             +-----+------+------+
                         |
                         v
====================================================================
                IF CONTINGENCY TRIGGERED
          DOMAIN M AUTO-ACTIVATES: July 1, 00:00 UTC
====================================================================

             |
             v
+============================================+
|  DOMAIN M CONTINGENCY ACTIVATION RUNBOOK   |
|  (DOMAIN_M_JULY_1_15_CONTINGENCY_           |
|   ACTIVATION_RUNBOOK.md)                   |
+============================================+

             |
             v
====================================================================
PHASE 1: Research Sprint (July 1-5)
====================================================================

             |
             v
   Draft "Direct Democracy Under Supermajority Attack"
   3,000-4,000 words / 25+ citations / CC Attribution 4.0
   Sources: Ballotpedia (MO Amendment 4, ND Measure 2),
            BISC (ballot.org/defenddirectdemocracy),
            Bolts Magazine, NBC News, Brennan Center
             |
    +--------v---------+
    | Brief complete   |
    | by July 5?       |
    +--------+---------+
             |
     YES     |     NO
      |      |      |
      |      |      v
      |      |  Extend 1-2 days
      |      |  Shift all send
      |      |  dates forward
      |      |  by same interval
      |      |      |
      +------+------+
             |
             v
====================================================================
PHASE 2: Create Gist (July 5-7)
====================================================================

             |
             v
   1. gist.github.com/new (esca8peArtist login)
   2. Filename: domain-m-direct-democracy-
      supermajority-attack-2026.md
   3. Paste brief text — create as PUBLIC
   4. Copy URL (format: gist.github.com/esca8peArtist/[hash])
   5. Verify HTTP 200 in incognito browser
   6. Fill [DOMAIN_M_GIST_URL] in all 7 templates
             |
    +--------v---------+
    | Gist live        |
    | (HTTP 200)?      |
    +--------+---------+
             |
     YES     |     NO
      |      |      |
      |      |      v
      |      |  Fix Gist
      |      |  before
      |      |  any send
      |      |      |
      +------+------+
             |
             v
====================================================================
PHASE 3: Tier 1 Sends (July 7-11)
====================================================================

             |
             v
   July 7, 14:00 UTC
   Send 1: BISC
   To: ballot.org/contact form
   [bypass mechanism argument + empirical record]
             |
         Log send time
             |
             v
   July 9, 14:00 UTC
   Send 2: Democracy Docket
   To: info@democracydocket.com
   [litigation framing + bypass mechanism argument]
             |
         Log send time
             |
             v
   July 11, 14:00 UTC
   Send 3: Common Cause National
   To: commoncause@commoncause.org
   [state chapter routing request + empirical record]
             |
         Log send time
             |
             v
   GATE 3: July 14 — Check for Tier 1 replies
    +--------v---------+
    | Any reply from   |
    | BISC, DD, or CC  |
    | by July 14?      |
    +--------+---------+
             |
   YES (proceed)  |  NO (also proceed)
             |              |
             +--------------+
             |
             v
   PROCEED WITH TIER 2 REGARDLESS OF REPLY STATUS
             |
             v
====================================================================
PHASE 4: Tier 2 Sends (July 12-15)
====================================================================

             |
             v
   July 12, 14:00 UTC
   Send 4: League of Women Voters National
   To: Contact@lwv.org
   [voter education + state chapter routing]
             |
             v
   July 14, 14:00 UTC
   Send 5: Brennan Center
   To: democracy@brennancenter.org
   [publication opportunity + direct democracy series]
             |
             v
   July 15, 10:00 UTC
   Send 6: Missourians for Fair Governance
   To: respectmissourivoters.org contact form
   [MO Amendment 4 structural framing + empirical record]
             |
             v
   July 15, 14:00 UTC
   Send 7: Common Cause State Chapters (MO/ND/SD)
   To: state chapter contacts
   [state-specific bypass mechanism + empirical record]
             |
             v
====================================================================
GATE 4: July 15, 23:59 UTC — FINAL DOMAIN M DEADLINE
====================================================================

             |
    +--------v---------+
    | All 7 sends      |
    | logged by        |
    | July 15 23:59?   |
    +--------+---------+
             |
     YES     |     NO / PARTIAL
      |      |          |
      v      |          v
  DOMAIN M  |    Continue remaining
  SUCCESS   |    sends ASAP
  Value:    |    Value: 50-65%
  75-85%    |    (partial contingency)
```

---

## Bounce and Fallback Decision Tree

```
====================================================================
BOUNCE HANDLING — Any Email in Either Runbook
====================================================================

             |
             v
    +--------v---------+
    | Did email bounce?|
    | (delivery error  |
    | in sent folder)  |
    +--------+---------+
             |
     NO      |     YES
      |      |      |
      |      |      v
      |      |  HARD BOUNCE (address not found)
      |      |      |
      |      |      v
      |      |  Use fallback address:
      |      |
      |      |  DOMAIN 51:
      |      |  CLC (echlopak@) → info@campaignlegal.org
      |      |  Issue One (info@issueone.org) → nick@issueone.org
      |      |  Common Cause CA (dkemp@) → info@commoncause.org
      |      |  LWV CA (lwvc@lwvc.org) → lwvc.org contact form
      |      |  Clean Money (info@CAclean.org) → Trent.Lange@CAclean.org
      |      |
      |      |  DOMAIN M:
      |      |  BISC (ballot.org form) → ballot.org/defenddirectdemocracy
      |      |  Democracy Docket (info@) → melias@elias.law
      |      |  Common Cause (commoncause@) → no alternative; retry
      |      |
      |      |      |
      |      |      v
      |      |  Send to fallback address
      |      |  (same subject + body)
      |      |  Log fallback send in execution log
      |      |      |
      |      |      v
      |      |    +--+--+
      |      |    | >1  |
      |      |    |hard |
      |      |    |bounce|
      |      |    +--+--+
      |      |       |
      |      |  YES  |  NO
      |      |    v  |   v
      |      | ABORT  | Continue
      |      | sends  | sends
      |      | until  | per
      |      | addresses| schedule
      |      | verified |
      |
      v
   Continue per send schedule
```

---

## Value Recovery Summary

```
====================================================================
OUTCOME / VALUE MATRIX
====================================================================

SCENARIO                       VALUE   CONTINGENCY
─────────────────────────────────────────────────────────────
All 5 Domain 51 sends          100%    None
by June 30, 23:59 UTC

All 7 Domain M sends by        75-85%  Domain M only
July 15 + brief complete

Domain 51 Branch A             60-75%  Domain 51 Tier 2
(sends July 2-10)                      + Domain M

Domain 51 Branch B             50-60%  Domain 51 Tier 2
(sends July 11-14)                     + Domain M

Domain M partial               50-65%  Partial Domain M
(4-6 of 7 sends)

Domain 51 Branch C             40-50%  Domain 51 Tier 3
(sends July 15+)                       + Domain M Tier 2

Nothing sent by               0%      Phase 3 remediation
August 8
─────────────────────────────────────────────────────────────
```

---

## Quick Reference: UTC Deadlines

```
KEY DEADLINES (ALL UTC)
════════════════════════════════════════════
June 30, 23:59 UTC  — Domain 51 hard deadline
                      (all 5 sends must be logged)

July 1, 00:00 UTC   — Domain M auto-trigger
                      (if Domain 51 missed)

July 5, 23:59 UTC   — Domain M research brief
                      complete (gate)

July 7, 14:00 UTC   — Domain M Send 1 (BISC)

July 9, 14:00 UTC   — Domain M Send 2 (Democracy Docket)

July 10, 23:59 UTC  — Domain 51 Branch A deadline
                      (if on contingency)

July 11, 14:00 UTC  — Domain M Send 3 (Common Cause)

July 12, 14:00 UTC  — Domain M Send 4 (LWV)

July 14, 14:00 UTC  — Domain M Send 5 (Brennan Center)
                      + Tier 1 reply check

July 14, 23:59 UTC  — Domain 51 Branch B deadline

July 15, 10:00 UTC  — Domain M Send 6 (MFFG)

July 15, 14:00 UTC  — Domain M Send 7 (CC state chapters)

July 15, 23:59 UTC  — Domain M FINAL deadline
                      (all 7 sends must be logged)

August 8, 23:59 UTC — Domain 51 Branch C deadline
════════════════════════════════════════════
```

---

*Item 45 — Flowchart. Produced June 29, 2026.*
*Covers: Domain 51 Phase 2 Wave 1 (June 30 deadline) + Domain M contingency (July 1-15 window).*
*Decision logic is deterministic — all branch conditions are UTC timestamps or binary send-status checks.*
