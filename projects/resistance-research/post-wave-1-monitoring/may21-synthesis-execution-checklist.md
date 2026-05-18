---
title: "May 21 Synthesis Execution Checklist — 19:00–20:00 UTC"
created: 2026-05-19
execute_at: "May 21, 2026, 19:00 UTC"
post_by: "May 21, 2026, 20:00 UTC"
status: PRE-BUILT — populate [FILL] fields on execution day
scope: "Step-by-step synthesis checklist for single operator; under 30 minutes"
audience: thorn — execute this, not wave-1-synthesis-framework-skeleton.md (that is the reference document; this is the action sequence)
---

# May 21 Synthesis Execution Checklist

*Execute at 19:00 UTC. Target: complete and post CHECKIN.md entry by 20:00 UTC. Total time: 25–30 minutes.*

---

## PRE-SYNTHESIS READS (19:00–19:08 UTC, ~8 min)

Read in this order. Do not skip steps — the data flows from step 1 into later sections.

- [ ] **Step 1.** Open `post-wave-1-monitoring/wave-1-signal-log-may18-21.md`. Read all entries in the SIGNAL LOG TABLE (every row added since May 18 10:30 UTC). Read all three daily snapshot sections (May 19, May 20, May 21). Note the total reply count, score of each reply, and Gist delta figures.

- [ ] **Step 2.** Open email inbox. Confirm no replies arrived since your last monitoring check that have not yet been logged in the signal log. If any unlogged replies exist, score them now (use the SIGNAL CATEGORY REFERENCE at the bottom of the signal log) and add them to the signal log table before continuing.

- [ ] **Step 3.** Check Gist view counts in incognito browser. Record delta since H+0 (May 18, ~08:00 UTC baseline). Add to the May 21 snapshot section of the signal log if not already filled.

- [ ] **Step 4.** Check bounce status. Any hard bounce received since May 18 should already be logged. If new bounces appear: remove that contact from the adjusted send count and begin email re-verification after synthesis completes.

---

## DATA ASSEMBLY (19:08–19:16 UTC, ~8 min)

Fill the contact response summary. One row per contact. Pull all data from the signal log.

| Contact | Org | Reply? (Y/N) | Score | Quality Reply Points | OOO? | Bounce? |
|---------|-----|--------------|-------|---------------------|------|---------|
| Ryan Goodman | Just Security / NYU Law | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |
| Wendy Weiser | Brennan Center | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |
| Erica Chenoweth | Harvard Kennedy School | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |
| Ian Bassin | Protect Democracy | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |
| Marc Elias | Democracy Docket / ELG | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |

**Scoring reference** (from WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv):
- Score 5 = STRONG OVERRIDE — stop, classify STRONG, skip to CHECKIN.md entry
- Score 4 = 2 Quality Reply Points
- Score 3 = 1 Quality Reply Point
- Score 1–2 = 0 Quality Reply Points (delivery confirmed, no engagement quality)
- OOO = remove from denominator; note return date
- Hard bounce = remove from denominator; re-verify email after synthesis

**Aggregate metrics** (fill from the table above):

| Metric | Value |
|--------|-------|
| Total sent | 5 |
| Hard bounces | [FILL] |
| OOOs removed from denominator | [FILL] |
| Adjusted send count | [FILL] |
| Total substantive replies (Score 3+) | [FILL] |
| Raw substantive response rate | [FILL]% |
| Gist total delta (all URLs, incognito check) | [FILL] |
| Gist bonus points (delta / 5, capped at 1.0) | [FILL] |
| TOTAL QUALITY REPLY POINTS (contact scores + Gist bonus) | [FILL] |

---

## CLASSIFICATION (19:16–19:22 UTC, ~6 min)

Execute top to bottom. Stop at first match.

**Step 5: Score 5 override check**

Has any Batch 1 contact cited the framework in a published work, filing, testimony? Offered formal institutional collaboration?
- [ ] YES — classify as STRONG. Skip to CHECKIN.md template below. Note which contact and what the citation was.
- [ ] NO — continue to Step 6.

**Step 6: Quality Reply Points classification**

Total Quality Reply Points from the table above: [FILL]

| If Total Quality Reply Points... | Classification |
|----------------------------------|---------------|
| >= 2 AND response rate >= 40% | STRONG |
| >= 1 (any Score 3+) OR Gist delta > 10 with zero replies | MODERATE |
| < 1 AND response rate < 20% AND Gist delta <= 5 | WEAK — run delivery check first (Step 7) |
| Zero replies AND zero Gist delta AND no bounces | TOO EARLY — law school window not closed |

**Preliminary classification**: [ ] STRONG [ ] MODERATE [ ] WEAK [ ] TOO EARLY

**Step 7: If WEAK — delivery check before classifying**
- Send a test email to your own account from the same sending address. Does it land in inbox or spam?
- If spam: do NOT classify as WEAK content failure. Classify as DELIVERY PROBLEM. Pause all further sends. Fix sender reputation. Do not revise messaging.
- If inbox: delivery is confirmed. WEAK classification stands. Flag for messaging audit.

**Step 8: Constituency-level classification** (run independently; used in CHECKIN.md entry)

*Law schools (Goodman, Chenoweth)*: At 72h, law school contacts are structurally TOO EARLY regardless of reply status. Their first likely reply window is May 23–28. Do not classify as Weak at 72h.
- 72h result: [FILL — reply status if any] | Classification: TOO EARLY (classify at May 25)

*Think tanks / policy orgs (Weiser, Bassin)*: STRONG threshold = 1 of 2 at Score 3+ within 5 days (May 23). At 72h, within their window.
- 72h result: [FILL] | Classification: [STRONG / MODERATE / WEAK / TOO EARLY]

*Immigration legal aid (Elias)*: STRONG threshold = Score 3+ within 72h, OR case-specific content within 5 days (May 23).
- 72h result: [FILL] | Classification: [STRONG / MODERATE / WEAK / TOO EARLY]

---

## PATH SELECTION (19:22–19:26 UTC, ~4 min)

**Step 9: Identify path from the classification table**

For a full decision tree with Phase 2 domain sequences, see `post-wave-1-monitoring/phase-2-path-activation-summary.md`. The quick reference:

- **STRONG** (Quality Reply Points >= 2 + response rate >= 40%; OR Score 5 override): Phase 2 June 15 parallel launch. D57 + D59 pre-production checklists. Tier 2 activation Week 5. Flag in CHECKIN.md — requires user approval before D57/D59 pre-production begins.

- **MODERATE** (>= 1 Quality Reply Point, OR Gist delta > 10): Standard Phase 2 timeline. Continue monitoring to May 25 final gate. No accelerated action. D57 PRIMARY research June 10, D59 SECONDARY July 1.

- **WEAK** (delivery confirmed, zero quality signal): Phase 1 remediation before Phase 2. D39 June 1 non-negotiable. D38 and D40 accelerated. D57/D59 deferred. Flag in CHECKIN.md — requires user decision on delivery vs. content diagnosis.

- **TOO EARLY**: Hold. Continue monitoring. No path decision before May 25. Log as TOO EARLY, not Weak.

**Selected path**: [ ] STRONG [ ] MODERATE [ ] WEAK [ ] TOO EARLY

---

## CHECKIN.MD POST (19:26–20:00 UTC, ~4 min)

**Step 10: Open CHECKIN.md and post under "Needs Your Input" using this exact template**

```
## Wave 1 Synthesis — May 21, 20:00 UTC

**Preliminary classification**: [STRONG / MODERATE / WEAK / TOO EARLY]
**Quality Reply Points**: [X] / [adjusted send count] contacts
**Strongest signal**: [Contact name], [Org], Score [X] — [one sentence description of content]
**Law school constituency**: TOO EARLY — classify at May 25 (5–10 day response cycle)
**Think tank constituency**: [STRONG / MODERATE / WEAK / TOO EARLY]
**Immigration legal constituency**: [STRONG / MODERATE / WEAK / TOO EARLY]
**Gist delta**: [X] views since H+0

**Recommended path**: [A: STRONG / B: MODERATE / C: WEAK / D: TOO EARLY]
**Needs Your Input**: [Specific decision required — see phase-2-path-activation-summary.md for full path details]

**May 25 final gate**: [what to classify / what to check by May 25]
**Domain 42 DEA deadline**: May 28 — 7 days remaining. Check send status before end of day.
```

**Step 11: Update wave-1-signal-log-may18-21.md**
- Fill May 21 72-hour synthesis snapshot table
- Check the preliminary classification box
- Add synthesis completion note to the signal table

**Step 12: Update preliminary-signal-analysis-may18.md**
- Fill the May 21 row in the Update Log (Section 6) with: date, "Synthesis complete. Classification: [X]. See wave-1-synthesis-framework-skeleton.md Part 2 for full data."

---

## AFTER SYNTHESIS

**If STRONG**: Read `post-wave-1-monitoring/phase-2-path-activation-summary.md` Strong path. Do not begin D57/D59 pre-production until user confirms at May 25 gate. Flag in CHECKIN.md as requiring user approval.

**If MODERATE or TOO EARLY**: No research action required until May 25. Continue monitoring per `post-wave-1-monitoring/wave-1-signal-log-may18-21.md` May 22–24 cadence.

**If WEAK**: Before any content revision, confirm delivery per Step 7. Flag in CHECKIN.md. Read `PHASE_2_OUTCOME_LAUNCH_ROADMAP.md` Section 4.4 for remediation protocol.

**Domain 42 regardless of classification**: Check BATCH_1_CONTACT_LOG.md Domain 42 section. If Category A sub-batch (DPA, MPP, NORML, LEAP, ACLU, Sentencing Project, SSDP) still shows blank send dates, these must go out TODAY. 7 days to May 28. See `post-wave-1-monitoring/may28-dea-deadline-tracking.md` for compressed execution calendar.

---

*Created: May 19, 2026. Execute: May 21, 19:00–20:00 UTC. Post CHECKIN.md by 20:00 UTC.*
*Companion files: `wave-1-synthesis-framework-skeleton.md` (reference); `wave-1-signal-log-may18-21.md` (raw data); `phase-2-path-activation-summary.md` (path decision guide); `may28-dea-deadline-tracking.md` (Domain 42).*
