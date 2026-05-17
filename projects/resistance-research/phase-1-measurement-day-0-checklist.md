---
title: "Phase 1 Measurement — Day 0 Execution Checklist"
subtitle: "Pre-Wave-1 Setup Through First 24h Post-Distribution"
created: 2026-05-17
status: production-ready — fill-in-ready for May 18 06:00 UTC
scope: "Setup actions required before Wave 1 sends; go/no-go checkpoints; platform-specific instructions"
audience: "thorn — execute May 17 evening through May 18 10:00 UTC"
companion_files:
  - PHASE_1_DISTRIBUTION_MEASUREMENT_PLAYBOOK.md
  - POST_WAVE_1_PHASE_1_MEASUREMENT_FRAMEWORK.md
  - WAVE_1_MONITORING_DASHBOARD.md
  - phase-1-daily-monitoring-template.md
  - phase-1-week-1-synthesis.md
estimated_total_setup_time: "45–75 minutes (May 17 evening) + 30 min pre-launch (May 18 morning)"
---

# Phase 1 Measurement — Day 0 Execution Checklist

**Use this checklist in two passes**:
- **Pass 1 — May 17 evening** (items marked SETUP): Configure tools, create tracking sheet, set up alerts. ~45–75 min.
- **Pass 2 — May 18 06:00–08:00 UTC** (items marked PRE-LAUNCH): Verify baselines, final checks. ~30 min.

Do not begin Wave 1 sends until all PRE-LAUNCH items are checked. A 2-hour delay is recoverable. A broken measurement baseline is not.

---

## BLOCK 1 — GitHub Gist Analytics Verification (SETUP — 10 min)

**Why**: Gist view counts are the primary proxy for email opens. You need a pre-send baseline for each of the 8 Gists to calculate the delta after distribution. GitHub does not expose Gist views via a public API — counts are read manually from each Gist page.

**How to check Gist view counts**:
1. Log into github.com as esca8peArtist
2. Navigate to gist.github.com/esca8peArtist
3. Click each Gist individually — the view count appears as a small number below the Gist title (example: "3 views")
4. If the count does not appear, open the Gist in an incognito window to confirm it is publicly accessible — the view count only appears when logged in

**Action — record baseline counts for all 8 Gists** (fill in the blanks below):

| Gist | URL | Baseline Count (May 17 evening) | Baseline Count (May 18 pre-send) |
|------|-----|-------------------------------|--------------------------------|
| Democratic Renewal Proposal | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | ___ views | ___ views |
| Executive Summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | ___ views | ___ views |
| Domain 37 — Federal Election Interference | https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0 | ___ views | ___ views |
| Litigation Tracker 2026 | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | ___ views | ___ views |
| First Amendment Suppression | https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c | ___ views | ___ views |
| Environmental Rollbacks | https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4 | ___ views | ___ views |
| Police Consent Decree | https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731 | ___ views | ___ views |
| Domain 42 — DEA | https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab | ___ views | ___ views |

**Go/No-Go check**: All 8 Gists load in incognito without authentication — if any returns 404 or requires login, do not proceed until resolved.

- [ ] All 8 Gists publicly accessible (incognito test passed)
- [ ] Baseline view counts recorded for all 8 above (May 17 evening column)

**Time estimate**: 10 minutes

---

## BLOCK 2 — Email Tracking Configuration (SETUP — 10 min)

**Why**: You need to distinguish between "delivered and opened" vs. "delivered but never opened" vs. "bounced." The primary mechanism is Gist/Bitly click-through as a proxy for opens; bounces are detected by Gmail itself.

**Step 1 — Gmail label setup** (5 min):
In Gmail settings → Labels → Create:
- `wave-1-batch-1` — apply to all 5 Batch 1 sent emails
- `wave-1-replies` — apply to all incoming replies from Batch 1 contacts
- `wave-1-bounces` — apply to any delivery failure notifications

**Step 2 — Bounce detection window** (1 min):
Hard bounces appear in your inbox within 60–120 minutes of send. Check your inbox for "Mail Delivery Subsystem" messages within 2 hours of each send. Soft bounces ("temporarily unable to deliver") appear within 24–48 hours.

**Step 3 — Optional Bitly shortlinks** (4 min, optional but recommended):
If you have a Bitly account, create shortened tracking links for the two primary Gists (Proposal + Domain 37). Use these in email bodies instead of raw GitHub URLs. Bitly shows click count, click time, and referring source.

- Proposal Gist short link: ___ (create at bit.ly, paste full URL)
- Domain 37 Gist short link: ___ (create at bit.ly)

If you do not have Bitly: use the raw GitHub Gist URLs. Rely on Gist view counts alone as the engagement proxy. This is acceptable — view counts are sufficient for Day 1–7 measurement.

- [ ] Gmail labels created (wave-1-batch-1, wave-1-replies, wave-1-bounces)
- [ ] Bounce detection: you know where to look and what to look for
- [ ] Bitly links created (optional) — or confirmed you will use raw Gist URLs

**Time estimate**: 10 minutes

---

## BLOCK 3 — Contact List and CRM Setup (SETUP — 15 min)

**Why**: The contact tracking sheet is your single source of truth for Phase 1 measurement. Without it, data lives across email threads, notes, and memory — unusable for Day 7 and Week 1 synthesis.

**Primary source files** (read before creating the sheet):
- `WAVE_1_MONITORING_DASHBOARD.md` Section 1 — contains Batch 1 pre-populated rows
- `WAVE_1_PRESTAGING_READINESS.md` Section 1 — full 25-contact verification table

**Action — create Google Sheets workbook** named "Phase 1 Wave 1 Tracking — May 2026":

**Tab 1: Contact Tracking** (core tab — fill before send)

| Column | Header | Instructions |
|--------|--------|-------------|
| A | Date Sent | YYYY-MM-DD |
| B | Contact Name | Full name |
| C | Organization | Abbreviated (BCJ, HKS, DD, PD, ELG, etc.) |
| D | Sector | Law School / Policy Org / Immigration Legal / Mutual Aid / Think Tank |
| E | Batch | 1, 2, or 3 |
| F | Email Address | Address used for send |
| G | Template Variant | Which email variant sent (B1-Domain37, B1-litigation, etc.) |
| H | Date Sent (actual) | Fill on day of send |
| I | Bounce? | Y/N — fill within 2h of send |
| J | OOO Reply? | Y/N/date — fill if out-of-office received |
| K | Replied? | Y/N — fill when reply arrives |
| L | Reply Date | YYYY-MM-DD |
| M | Reply Type | Integration / Implementation / Referral / Clarification / Critique / Acknowledgment / Decline / None |
| N | Engagement Score | 0–5 (see scoring formula below) |
| O | Domains Mentioned | Comma-separated numbers (e.g., 1, 37, 57) |
| P | Tier 2 Candidate? | Y / N / Maybe |
| Q | Secondary Contact ID | Name and org of any contact they referred |
| R | Policy Uptake Signal | Y/N + brief description |
| S | Notes | Verbatim quote or paraphrase of key content |

**Engagement score formula**:
```
Score = (reply_score × 0.6) + (gist_click_proxy × 0.2) + (opened_24h_proxy × 0.2)

Reply scores:
- Integration signal (using in work) = 5
- Implementation question (how to use) = 4
- Referral (connecting to colleague) = 4
- Clarification question = 3
- Substantive critique = 3
- Acknowledgment only = 1
- Decline = 0
- No reply = 0
```

**Pre-populate Batch 1 rows** (do this before May 18 send):

| Date | Contact | Org | Sector | Batch | Email | Template |
|------|---------|-----|--------|-------|-------|---------|
| 2026-05-18 | Ryan Goodman | Just Security / NYU Law | Law School | 1 | ryan.goodman@nyu.edu | B1-Domain28/29 |
| 2026-05-18 | Wendy Weiser | Brennan Center | Policy Org | 1 | wweiser@brennancenter.org | B1-Domain1/37 |
| 2026-05-18 | Erica Chenoweth | Harvard HKS | Law School | 1 | erica_chenoweth@hks.harvard.edu | B1-methodology |
| 2026-05-18 | Ian Bassin | Protect Democracy | Policy Org | 1 | ian@protectdemocracy.org | B1-implementation |
| 2026-05-18 | Marc Elias | Elias Law Group | Immigration Legal | 1 | melias@elias.law | B1-litigation |

**Tab 2: Gist View Log** (update daily)

| Date | Time (UTC) | Proposal Views | Exec Summary Views | Domain 37 Views | Litigation Views | 1A Views | Environmental Views | Police Views | Domain 42 Views | Delta From Baseline |
|------|-----------|----------------|-------------------|----------------|-----------------|----------|--------------------|--------------|--------------|--------------------|
| 2026-05-17 | Evening | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | — (baseline) |
| 2026-05-18 | Pre-send | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | — (baseline 2) |
| 2026-05-18 | 20:00 | | | | | | | | | |

**Tab 3: Daily KPI Summary** (auto-calculated):

| Metric | Day 1 (5/18) | Day 2 (5/19) | Day 3 (5/20) | Day 5 (5/22) | Day 7 (5/24) |
|--------|-------------|-------------|-------------|-------------|-------------|
| Cumulative sent | | | | | |
| Bounces | | | | | |
| Replies received | | | | | |
| Reply rate (%) | | | | | |
| Avg engagement score | | | | | |
| Tier 2 candidates | | | | | |
| Gist view delta (total) | | | | | |

- [ ] Google Sheets workbook created ("Phase 1 Wave 1 Tracking — May 2026")
- [ ] Tab 1 created with all columns above
- [ ] Batch 1 rows pre-populated (5 rows, all fields except H–S which fill during/after send)
- [ ] Tab 2 (Gist View Log) created with baseline row pre-filled from Block 1
- [ ] Tab 3 (Daily KPI Summary) created with column headers

**Time estimate**: 15 minutes

---

## BLOCK 4 — Monitoring Schedule Definition (SETUP — 5 min)

**Why**: Undefined monitoring becomes ad hoc, missed, or obsessive. You need a fixed schedule that takes under 15 min/day and covers every failure mode.

**Daily monitoring cadence** (add to calendar or phone reminders now):

| Time (UTC) | Day | Action | Duration |
|-----------|-----|--------|---------|
| 06:00 | May 18 | Pre-launch final check (Block 6 below) | 30 min |
| 10:30 | May 18 | Post-send bounce scan + Gist baseline H+0 | 10 min |
| 15:00 | May 18 | H+6 check: bounces, OOO, early Gist delta | 10 min |
| 20:00 | May 18 | Day 1 EOD: full tracking update, Day 1 reflection | 20 min |
| 10:00 | May 19 | H+24 morning: reply scan + classify + Gist delta | 15 min |
| 16:00 | May 19 | H+30 afternoon spot-check | 10 min |
| 20:00 | May 19 | Day 2 EOD: update tracking, H+36 engagement snapshot | 20 min |
| 10:00 | May 20 | H+48 morning: reply rate calculation, preliminary assessment | 20 min |
| 20:00 | May 20 | H+72 analysis: PASS/NEAR-MISS/FAR-MISS determination | 30 min |
| 10:00 | May 22–31 | Daily morning check (10 min/day, reduce to EOD-only after May 25) | 10 min |

**Total monitoring time Day 1–3**: approximately 2.5 hours over 3 days
**Total monitoring time Day 4–7**: approximately 70 minutes (10 min/day)

**Action**: Set the following 9 phone/calendar reminders now (they take 2 minutes to set):
- May 18 at 06:00 UTC: "Wave 1 pre-launch check"
- May 18 at 10:30 UTC: "Post-send bounce scan"
- May 18 at 15:00 UTC: "H+6 Gist + bounce check"
- May 18 at 20:00 UTC: "Day 1 EOD update"
- May 19 at 10:00 UTC: "H+24 morning check"
- May 19 at 20:00 UTC: "Day 2 EOD update"
- May 20 at 10:00 UTC: "H+48 preliminary assessment"
- May 20 at 20:00 UTC: "H+72 PASS/NEAR-MISS/FAR-MISS determination"
- May 25 at 18:00 UTC: "Day 7 weekly synthesis (use phase-1-week-1-synthesis.md)"

- [ ] 9 monitoring reminders set in calendar/phone
- [ ] Daily monitoring template (`phase-1-daily-monitoring-template.md`) bookmarked or open

**Time estimate**: 5 minutes

---

## BLOCK 5 — Google Alerts and Ambient Monitoring (SETUP — 10 min)

**Why**: Reputational amplification (media pickup, academic citation) cannot be tracked manually. Google Alerts runs in background and surfaces any mention of the framework in indexed content. You need to set these up before distribution so any Day 1 mentions are captured.

**Platform**: google.com/alerts (requires Google account)

**Create the following 5 alerts** (delivery: "As-it-happens" for first 7 days, then "Once a day"):

| Alert query | Intended to catch |
|-------------|------------------|
| `"democratic renewal framework"` | Direct framework citations in media, blogs, policy documents |
| `"35-domain framework"` OR `"40-domain framework"` | References to the proposal's scope |
| `"prosecutorial weaponization" democratic` | Domain 29 pickup in journalism or legal commentary |
| `"federal executive interference" 2026 midterms` | Domain 37 pickup in election coverage |
| `"democratic renewal proposal" site:github.com` | GitHub/Gist citations or forks |

**Google Scholar alert** (scholar.google.com → "Create alert"):
- Query: `"democratic renewal" framework governance 2026`
- This catches any academic paper or preprint that references the framework

**Delivery email**: Use the same Gmail account you're sending Wave 1 from, so all signals aggregate in one inbox.

- [ ] 5 Google Alerts created (queries above, "As-it-happens" delivery)
- [ ] 1 Google Scholar alert created
- [ ] Delivery going to correct email (same as Wave 1 sending account)

**Time estimate**: 10 minutes

---

## BLOCK 6 — Pre-Launch Go/No-Go Verification (PRE-LAUNCH — May 18 06:00–08:00 UTC — 30 min)

**This is the final gate before first email leaves your outbox.** Do not skip any item. Address every unchecked item before sending.

### Technical Verification

- [ ] All 8 Gist URLs open in incognito — none require login, none return 404
- [ ] Record May 18 pre-send Gist view counts in Tab 2 of tracking sheet (these are your H=0 baselines)
- [ ] Send one test email to yourself from the sending account
  - Arrives in inbox (not spam) within 3 minutes: Y / N
  - All Gist links are clickable and resolve correctly: Y / N
  - If test email lands in spam: **STOP — address spam flag before any contact send** (see PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.3)

### Contact Verification (90 seconds per contact)

- [ ] Ryan Goodman: justsecurity.org author page — name confirmed as of today
- [ ] Wendy Weiser: brennancenter.org/about/leadership — VP Democracy confirmed
- [ ] Erica Chenoweth: hks.harvard.edu faculty directory — Academic Dean confirmed
- [ ] Ian Bassin: protectdemocracy.org homepage — org confirmed active
- [ ] Marc Elias: democracydocket.com — confirmed active; using melias@elias.law (NOT perkinscoie)

### Template Verification (15 min)

- [ ] Open all 5 email drafts
- [ ] Zero `{{placeholder}}` or `[bracket]` strings remain in any template
- [ ] `{{YOUR_NAME}}` filled with actual name in all 5
- [ ] `{{YOUR_CONTACT_INFO}}` filled in all 5
- [ ] Elias template: Callais decision framed as "decided April 29, 2026 — redistricting cascade underway" (NOT "pending")
- [ ] Watson v. RNC framed as "pending — decision expected end of June term"
- [ ] Path A+37 block selected — Path A and Path B paragraphs deleted from all 5
- [ ] Gist URLs in email bodies match canonical URLs in DISTRIBUTION_GIST_URLS.md (not old versions)
- [ ] Elias email uses melias@elias.law — perkinscoie.com is permanently stale

### Tracking Sheet Verification

- [ ] Tab 1 (Contact Tracking): All 5 Batch 1 rows pre-populated with name, org, sector, email
- [ ] Tab 2 (Gist View Log): Baseline row filled with May 18 pre-send counts
- [ ] Tab 3 (Daily KPI Summary): Column headers in place, all cells blank ready to fill

---

**GO/NO-GO GATE**:

If ALL items above are checked: proceed to send block (08:00–10:30 UTC per WAVE_1_EXECUTION_CHECKLIST.md)

If ANY item is unchecked: resolve before sending. Log the delay reason:
- Delay start time: ___
- Issue: ___
- Resolved at: ___
- First send moved to: ___

A delay of 1–4 hours is inconsequential. Do not rush a template with a known error.

---

## BLOCK 7 — Post-Send Confirmation (PRE-LAUNCH → DAY 1 — 10 min, immediately after last send)

Complete this block within 30 minutes of the final Batch 1 send (approximately 10:30 UTC May 18).

- [ ] All 5 sends confirmed dispatched (check sent folder — all 5 present)
- [ ] Record actual send times in Tab 1 Column H:
  - Goodman: ___ UTC
  - Weiser: ___ UTC
  - Chenoweth: ___ UTC
  - Bassin: ___ UTC
  - Elias: ___ UTC
- [ ] Apply Gmail label `wave-1-batch-1` to all 5 sent emails
- [ ] Record Gist view counts at H+0 (immediately post-send, before any contact opens) in Tab 2
- [ ] Log in DISTRIBUTION_EXECUTION_LOG.md: "Wave 1 Batch 1 sent — May 18 [time range] UTC — 5 contacts"
- [ ] Check inbox for bounce notifications (anything in "Mail Delivery Subsystem" thread)
  - If 0 bounces: log "0 bounces at H+0" in Tab 3
  - If 1+ bounces: go immediately to PHASE_1_CONTINGENCY_STRATEGY.md Trigger 1
- [ ] Open `phase-1-daily-monitoring-template.md` — it is now active for the first daily fill at 20:00 UTC

**Time estimate**: 10 minutes

---

## Summary: Total Setup Time

| Block | Activity | When | Time |
|-------|---------|------|------|
| Block 1 | GitHub Gist analytics baseline | May 17 evening | 10 min |
| Block 2 | Email tracking setup | May 17 evening | 10 min |
| Block 3 | Contact list and CRM (Google Sheets) | May 17 evening | 15 min |
| Block 4 | Monitoring schedule / reminders | May 17 evening | 5 min |
| Block 5 | Google Alerts setup | May 17 evening | 10 min |
| Block 6 | Pre-launch go/no-go (May 18 morning) | May 18 06:00–08:00 UTC | 30 min |
| Block 7 | Post-send confirmation | May 18 ~10:30 UTC | 10 min |
| **Total** | | | **90 min** |

**Sustainable Day 1–7 effort**: approximately 15–20 min/day after setup is complete.

---

## Contingency Quick Reference

If something goes wrong during setup or Day 1, use this table:

| Problem | Where to look |
|---------|--------------|
| Gist returns 404 | PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.1 |
| Test email lands in spam | PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.3 |
| Hard bounce (1 contact) | PHASE_1_WAVE1_EXECUTION_PREP.md Section 1 — alternate addresses |
| Hard bounce (3+ contacts) | PHASE_1_CONTINGENCY_STRATEGY.md Trigger 1 |
| Google Sheets formulas not working | Manual count in the column — formulas are a convenience not a requirement |
| Contact changed roles since verification | Do not send to former-role contact; use WAVE_1_PRESTAGING_READINESS.md Section 1 for alternates |
| Zero bounces AND zero OOO AND zero Gist views at H+48 | PHASE_1_CONTINGENCY_STRATEGY.md — delivery failure diagnosis |

---

*Prepared: May 17, 2026 — Item 34 (Phase 1 Measurement Staging)*
*Cross-references: PHASE_1_DISTRIBUTION_MEASUREMENT_PLAYBOOK.md (Section 9 checklist); POST_WAVE_1_PHASE_1_MEASUREMENT_FRAMEWORK.md (Section 1 send block); WAVE_1_MONITORING_DASHBOARD.md (Section 1 tracking table); WAVE_1_EXECUTION_CHECKLIST.md (pre-launch and send blocks)*
