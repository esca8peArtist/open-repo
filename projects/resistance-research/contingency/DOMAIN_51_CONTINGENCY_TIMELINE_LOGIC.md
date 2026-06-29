---
title: "Domain 51 — Contingency Timeline Logic (If X Date, Do Y)"
created: "2026-06-29"
status: "production-ready — mechanical, no human interpretation"
purpose: "Enter current date. System outputs: which sequence to activate + next send window. No judgment required."
congressional_calendar: "senate.gov/legislative/2026_schedule.htm (verified June 29, 2026)"
---

# Domain 51 — Contingency Timeline Logic

## How to Use This Document

1. Find today's date in the left column.
2. Read the "Action" column — that is exactly what to do.
3. Read the "Next Send Window" column — those are your send dates.
4. Open the listed sequence file and execute.

No analysis required. The logic is already done.

---

## Master Timeline Table

| Current Date | Wave 1 Status | Action | Sequence File | Next Send Window | Notes |
|---|---|---|---|---|---|
| June 29 | NOT SENT | Send CLC + Issue One TODAY. July 1 deadline is 2 days away. | DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md | June 29-30 | Do not open contingency files yet |
| June 30 | NOT SENT | Send CLC + Issue One TODAY. Tomorrow is the deadline. | DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md | June 30 | Last clean window |
| July 1 | NOT SENT | DEADLINE DAY. Send immediately — morning UTC preferred. | DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md | July 1, before 23:59 UTC | If you miss 23:59 UTC, activate Sequence A tomorrow |
| July 2 | NOT SENT | July 1 passed. Activate **Sequence A**. Send starts today. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | July 2 (Sends 1-2), July 3 (Sends 3-4), July 4 (Sends 5-6) | 8 days before recess ends ~July 10 |
| July 3 | NOT SENT | Activate **Sequence A**. Begin sends today. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | July 3 (Sends 1-2), July 4 (Sends 3-4), July 5-7 gap, July 8-10 (Sends 7-10) | Compress if behind |
| July 4 | NOT SENT | Activate **Sequence A** (Independence Day — sends still land). Begin today. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | July 4 (Sends 1-2), July 5 (Sends 3-4), July 6-7 (Sends 5-6), July 8-10 (Sends 7-10) | Staff reads accumulated email July 5-7 |
| July 5 | NOT SENT | Activate **Sequence A**. Start today. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | July 5 (Sends 1-2), July 6 (Sends 3-4), July 7 (Sends 5-6), July 8-10 (Sends 7-10) | 5 days before recess ends |
| July 6 | NOT SENT | Activate **Sequence A**. Start today. Compress to 2/day. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | July 6-10, 2 sends/day | Beginning to compress window |
| July 7 | NOT SENT | Activate **Sequence A (compressed)**. Start today. 2-3 sends/day. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | July 7-10, 2-3 sends/day | Only 3 send days left in Sequence A window |
| July 8 | NOT SENT | Activate **Sequence A (compressed)**. Today is the last clean start day. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | July 8 (Sends 1-2), July 9 (Sends 3-4), July 10 (Sends 5-6) — partial Sequence A | Sends 7-10 will spill to Sequence B |
| July 9 | NOT SENT | Activate **Sequence A (minimal)** today + **Sequence B** starting July 11. | Both sequence files | July 9-10 (Sends 1-2), then July 11-14 (Sends 3-8 from Sequence B) | Hybrid: A-start + B-continuation |
| July 10 | NOT SENT | Last day of Sequence A window. Send Wave 1 (CLC + Issue One) + 2 Tier 2 today. Sequence B activates July 11. | A for Wave 1; `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_B_TIER_3_JULY_4_8.md` for the rest | July 10 (Wave 1), July 11-14 (Sequence B) | Recess ends ~July 13; Hill staff return |
| July 11 | NOT SENT | Activate **Sequence B**. Congress reconvenes ~July 13. Send now. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_B_TIER_3_JULY_4_8.md` | July 11 (Wave 1 + Sends 1-2), July 12-14 (Sends 3-8) | Post-recess framing; Hill staff returning |
| July 12 | NOT SENT | Activate **Sequence B**. Congress reconvening. Send today. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_B_TIER_3_JULY_4_8.md` | July 12-14, 2-3 sends/day | Compress to fit 4-day window |
| July 13 | NOT SENT | Activate **Sequence B**. Senate likely in session today. Send immediately. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_B_TIER_3_JULY_4_8.md` | July 13-14, maximum sends per day | Window closing July 14 |
| July 14 | NOT SENT | **Last day of Sequence B**. Send Wave 1 + maximum Tier 2 today. Activate Sequence C for remainder. | B for today; `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_C_LEGISLATIVE_WINDOW_JULY_15_PLUS.md` for rest | July 14 (maximum sends), July 15+ (Sequence C) | Transition day |
| July 15 | NOT SENT | Activate **Sequence C**. Post-deadline framing. 1-2 sends/day. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_C_LEGISLATIVE_WINDOW_JULY_15_PLUS.md` | July 15 through August 8 | Evergreen documentation framing |
| July 16-31 | NOT SENT | Activate **Sequence C**. Enter today's date in sequence file to find which send to start on. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_C_LEGISLATIVE_WINDOW_JULY_15_PLUS.md` | Through August 8 | 1-2 sends/day |
| Aug 1-8 | NOT SENT | Activate **Sequence C (late)**. Send before August 10 recess. | `contingency/DOMAIN_51_CONTINGENCY_SEQUENCE_C_LEGISLATIVE_WINDOW_JULY_15_PLUS.md` | Aug 1-8 | Final window before recess |
| Aug 9 | NOT SENT | **Final pre-recess day**. Send everything remaining today. Academic contacts only if time-constrained. | Sequence C — final sends | Aug 9, all sends | Tomorrow recess begins |
| Aug 10+ | NOT SENT | Senate recess (Aug 10-Sep 11). Strip Hill-staff framing. Send to academic/research contacts only. | Sequence C — modified academic track | Aug 10 - Sep 11, academic contacts only | No Hill contacts; Hasen, Douglas, Levitt, Graves, Wertheimer, OpenSecrets only |
| Sep 14+ | NOT SENT | Senate returns. Low-value residual sends only. Evergreen framing mandatory. | Sequence C — residual | September | Very low value; only if not yet sent |

---

## Send Window Summary by Branch

### Branch A Window — July 2-10

```
July 2:  Send 1 (Lisa Graves, True North)     10:00 UTC
         Send 2 (Rick Hasen, UCLA)             11:30 UTC
July 3:  Send 3 (Taifa Smith Butler, Demos)   10:00 UTC
         Send 4 (Sophia Lin Lakin, ACLU)       11:30 UTC
July 4:  Send 5 (Lawrence Norden, Brennan)    10:00 UTC
         Send 6 (Virginia Kase, Common Cause)  11:30 UTC
[Gap: July 5-7 — no sends; replies accumulate]
July 8:  Send 7 (Joshua Douglas, ELJ)         10:00 UTC
July 9:  Send 8 (Justin Levitt, Loyola)       10:00 UTC
July 10: Send 9 (Heidi Shierholz, EPI)        10:00 UTC
         Send 10 (Kara Gotsch, Sentencing)     11:30 UTC
```

T+7 checkpoint: July 9, 18:00 UTC (check for replies from Sends 1-6)

### Branch B Window — July 11-14

```
July 11: Wave 1 (CLC, Issue One) — if not yet sent
         Send 1 (Lisa Graves, True North)     10:00 UTC
         Send 2 (Rick Hasen, UCLA)             12:00 UTC
July 12: Send 3 (Taifa Smith Butler, Demos)   10:00 UTC
         Send 4 (Sophia Lin Lakin, ACLU)       12:00 UTC
         Send 5 (Lawrence Norden, Brennan)    14:00 UTC
July 13: Send 6 (Virginia Kase, Common Cause) 10:00 UTC
         Send 7 (Joshua Douglas, ELJ)         12:00 UTC
         Send 8 (Fred Wertheimer, Dem. 21)    14:00 UTC
July 14: Send 9 (Craig Holman, Public Citizen)10:00 UTC
         Send 10 (David Donnelly, ECU)         12:00 UTC
```

T+4 checkpoint: July 15 (check for replies from all sends)

### Branch C Window — July 15 through August 8

```
July 15: Send 1 (Rick Hasen, UCLA)
July 17: Send 2 (Joshua Douglas, ELJ)
July 19: Send 3 (Justin Levitt, Loyola)
July 22: Send 4 (Saurav Ghosh, Brennan Democracy)
July 24: Send 5 (Lisa Graves, True North)
July 26: Send 6 (Fred Wertheimer, Democracy 21)
July 29: Send 7 (Craig Holman, Public Citizen)
July 31: Send 8 (Virginia Kase, Common Cause National)
Aug  2:  Send 9 (Taifa Smith Butler, Demos)
Aug  4:  Send 10 (David Donnelly, End Citizens United)
Aug  5:  Send 11 (Lawrence Norden, Brennan Elections)
Aug  6:  Send 12 (Sophia Lin Lakin, ACLU)
Aug  7:  Send 13 (Heidi Shierholz, EPI)
Aug  7:  Send 14 (Kara Gotsch, Sentencing Project)
Aug  8:  Send 15 (OpenSecrets research team)
```

T+30 composite checkpoint: August 15

---

## Emergency Compression Protocol

**If you are behind schedule and need to close the gap**:

**Sequence A — behind by 2 days**: Send 3 contacts in one day (10:00, 11:30, 13:00 UTC). Do not compress below 90-minute spacing.

**Sequence A — behind by 4+ days**: Send 3-4 per day, 60-minute minimum spacing, maximum 4 per day. Flag this as compressed in the execution log.

**Sequence B — behind and only July 13-14 remain**: Send only the highest-priority contacts (Graves, Hasen, Wertheimer, Douglas). Skip Shierholz and Gotsch (lowest value in compressed window).

**Sequence C — any send skipped**: Skip rather than delay. Each day's recipient is selected for that day because their timing alignment is highest then. If a contact is skipped, do not double-send the following day — just skip it permanently and continue with the next scheduled contact.

---

## Hard Stop Conditions

These conditions stop the send sequence entirely:

1. **Bounce on Wave 1 (CLC or Issue One)**: Immediately research corrected address. Do not proceed with Tier 2 sends until Wave 1 is confirmed delivered.

2. **Gist URL returns 404 or 403**: Do not send any emails until the gist is restored. Verify: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 — if it returns an error, restore the gist from the local source (domain-51-campaign-finance-dark-money.md) before any send.

3. **User explicitly cancels**: No autonomous sends. This is a contingency staging document — user executes all sends manually.

---

## Calendar Verification Note

The Senate 2026 legislative schedule shows a State Work Period ending approximately July 10-12, with Senate reconvening ~July 13. This was verified at senate.gov/legislative/2026_schedule.htm on June 29, 2026.

Earlier Domain 51 documents reference July 11 as the congressional reconvening date. The correct date per the official Senate schedule is ~July 13. This does not require modifying existing protocol files — the July 2-10 window timing and framing are unaffected, and the Sequence B framing (post-recess, congress-in-session) is accurate regardless of whether reconvening is July 11, 12, or 13.

---

*Produced June 29, 2026. This document is the mechanical routing layer — enter current date, get sequence and send window, execute. No interpretation required.*
