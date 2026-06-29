---
title: "Domain 51 — Fallback Activation Decision Tree (Mechanical Routing)"
created: "2026-06-29"
status: "production-ready — zero-interpretation logic"
purpose: "Mechanical routing from current date to correct contingency sequence. No subjective judgment required."
zero_value_condition: "If both Wave 1 sends execute by July 1, 23:59 UTC — do not open this file."
congressional_calendar_source: "senate.gov/legislative/2026_schedule.htm (verified June 29, 2026)"
---

# Domain 51 — Fallback Activation Decision Tree

## STOP CONDITION — Read This First

**If both of the following are true, this document has zero value. Close it and proceed to DOMAIN_51_RESPONSE_MONITORING_PROTOCOL.md.**

- [ ] echlopak@campaignlegalcenter.org — sent and logged
- [ ] info@issueone.org — sent and logged

**Both must be checked and logged in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md with a UTC timestamp on or before July 1, 23:59 UTC.**

If either box is unchecked, or if no log entry exists, continue to Step 1 below.

---

## Step 1 — Check the Execution Log

Open: `/projects/resistance-research/DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md`

Look for the Send 1 and Send 2 entries. Find the "Send Date/Time" field for each.

**Question**: Is there a timestamp for Send 1 (CLC) AND Send 2 (Issue One)?

- If **NO timestamp for either send**: go to Step 2 — No Sends Logged.
- If **YES, both have timestamps**: go to Step 3 — Verify Deadline.

---

## Step 2 — No Sends Logged

No sends have been executed. Today is June 29, 2026. You have 2 days until the July 1 deadline.

**Immediate action**: Execute Wave 1 now. Open `DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md`. Send CLC and Issue One. Return to this document only if you miss July 1.

If you are reading this on July 2 or later with no sends logged, go to Step 4.

---

## Step 3 — Verify Deadline

The sends have timestamps. Check the dates against the threshold.

**Question**: Are both timestamps on or before July 1, 23:59 UTC?

- If **YES**: No contingency needed. Both sends executed on-time. Proceed to `DOMAIN_51_RESPONSE_MONITORING_PROTOCOL.md`.
- If **NO** (either or both timestamps are July 2 or later): Go to Step 4.

---

## Step 4 — Date-Based Routing (Post-Deadline)

What is today's date? Match it to the routing table below.

| Today's Date | Sequence to Activate | Protocol File | Value | Congressional Context |
|---|---|---|---|---|
| July 2 | **Sequence A** | `DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | 60-75% | Senate recess ends ~July 13; sends land during recess read period |
| July 3 | **Sequence A** | `DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | 60-75% | Same |
| July 4 | **Sequence A** | `DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | 60-75% | Independence Day — sends arrive; staff reads July 5-7 |
| July 5 | **Sequence A** | `DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | 60-70% | Same |
| July 6 | **Sequence A** | `DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | 60-70% | Same |
| July 7 | **Sequence A** | `DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | 65% | Same |
| July 8 | **Sequence A** | `DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | 60% | 5 days before Congress reconvenes |
| July 9 | **Sequence A** | `DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` | 55-60% | 4 days before Congress reconvenes |
| July 10 | **Sequence A (compressed)** | `DOMAIN_51_CONTINGENCY_SEQUENCE_A_JULY_2_10.md` — Section: Emergency Compression | 50-55% | Last day of recess; compress sends |
| July 11 | **Sequence B** | `DOMAIN_51_CONTINGENCY_SEQUENCE_B_TIER_3_JULY_4_8.md` | 50-55% | Congress reconvenes (tentative July 13 per Senate calendar) |
| July 12 | **Sequence B** | `DOMAIN_51_CONTINGENCY_SEQUENCE_B_TIER_3_JULY_4_8.md` | 50% | Same |
| July 13 | **Sequence B** | `DOMAIN_51_CONTINGENCY_SEQUENCE_B_TIER_3_JULY_4_8.md` | 50% | Senate in session; Hill staff at desks |
| July 14 | **Sequence B** | `DOMAIN_51_CONTINGENCY_SEQUENCE_B_TIER_3_JULY_4_8.md` | 45-50% | Same |
| July 15 | **Sequence C** | `DOMAIN_51_CONTINGENCY_SEQUENCE_C_LEGISLATIVE_WINDOW_JULY_15_PLUS.md` | 40-50% | Full legislative session; recess framing begins |
| July 16-31 | **Sequence C** | `DOMAIN_51_CONTINGENCY_SEQUENCE_C_LEGISLATIVE_WINDOW_JULY_15_PLUS.md` | 40-45% | Same |
| Aug 1-8 | **Sequence C** | `DOMAIN_51_CONTINGENCY_SEQUENCE_C_LEGISLATIVE_WINDOW_JULY_15_PLUS.md` | 35-40% | Approaching recess (Aug 10 start); sends land before recess |
| Aug 9 | **Sequence C (final window)** | `DOMAIN_51_CONTINGENCY_SEQUENCE_C_LEGISLATIVE_WINDOW_JULY_15_PLUS.md` | 30-35% | One day before August recess |
| Aug 10+ | **Recess window — academic track only** | See note below | 25-30% | Senate recess Aug 10-Sep 11; advocacy orgs only |
| Sep 14+ | **Sequence C (residual only)** | See note below | 15-20% | Very low value; academic and data orgs only |

**Note on August 10+ sends**: Senate recess runs August 10 - September 11 (per senate.gov/legislative/2026_schedule.htm). During this window, Hill staff are in districts. Advocacy orgs and academic contacts remain valid. If sending after August 10, strip any Hill-staff or committee-framing language from templates. Send only to: Hasen, Douglas, Levitt, Ghosh, Graves, Wertheimer, OpenSecrets. Skip: End Citizens United, ACLU, Sentencing Project, EPI.

---

## Step 5 — Confirm Sequence Activation

Once you have identified which sequence to activate, confirm:

1. **Open the sequence file** listed in the table above.
2. **Do the sends have not been done yet** — check DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md to avoid duplicate sends.
3. **Fill [YOUR_NAME] and [YOUR_CONTACT_INFO]** in every template before sending.
4. **Log every send** in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md immediately after sending.
5. **Space sends by 90 minutes minimum** on the same day.

---

## Step 6 — Post-Send Monitoring

After the first send in any sequence:

- Set a T+7 checkpoint: 7 days after the first send date.
- Open DOMAIN_51_RESPONSE_MONITORING_PROTOCOL.md on the checkpoint date.
- Log all replies in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md with signal classification (STRONG / MODERATE / WEAK / NONE).

---

## Three-Branch Outcome Summary

| Branch | Trigger | Sequence | Value Score | Success Criteria |
|---|---|---|---|---|
| **A (1-10 days late)** | July 2-10 | Sequence A | 60-75% | 10 sends by July 10; 1+ reply by July 9 |
| **B (11-14 days late)** | July 11-14 | Sequence B | 50-55% | 8 sends by July 14; congressional-session framing |
| **C (>14 days late)** | July 15+ | Sequence C | 40-50% | 15 sends by Aug 8; T+30 assessment Aug 15 |

---

## Congressional Calendar Reference (Embedded)

Source: senate.gov/legislative/2026_schedule.htm (verified June 29, 2026)

| Date | Status | Relevance to Sends |
|---|---|---|
| June 29 - July 10 | Senate State Work Period (recess) | Sends land in recess inbox — higher read probability |
| July 4 | Independence Day | Staff not checking email; sends still land and accumulate |
| ~July 13 | Senate reconvenes (tentative) | Hill staff return to office; sends July 2-10 will be read post-return |
| July 13 - Aug 8 | Senate in session | Full legislative session; DISCLOSE Act markup window |
| Aug 10 - Sep 11 | Senate State Work Period (recess) | Strip Hill-staff framing; academic and policy orgs only |
| Sep 14 | Senate returns | Normal operations resume |

**CORRECTION NOTE**: Prior Domain 51 documents state Congress reconvenes July 11. The verified Senate schedule shows the State Work Period ends around July 10-12, with reconvening ~July 13. This discrepancy does not materially affect Sequence A timing but corrects the July 11 framing used in earlier documents.

---

## Escalation Override

**If you are unsure which sequence applies**: Use Sequence A if it is before July 11. Use Sequence C if it is July 15 or later. The value difference between sequences is not large enough to warrant delay — send now in the current window rather than waiting for a "better" window.

**The only situation that permanently closes the activation window**: Sends executing after September 14 without any prior distribution. At that point, the California Fair Elections Act legislative window is fully closed and the academic track is the only remaining value pathway.

---

*Produced June 29, 2026. Congressional calendar data from senate.gov/legislative/2026_schedule.htm, verified June 29, 2026. Sequence files are in `/projects/resistance-research/contingency/`. This document is the entry point — all routing flows from here.*
