---
title: "Track B — May 22 Pre-Launch Status Brief"
created: 2026-05-22
days-to-launch: 8
launch-date: 2026-05-30
status: ALL USER GATES OVERDUE — launch at risk if gates not resolved by May 25
purpose: >
  Current-state snapshot as of May 22. Consolidates gate status, overdue items,
  recoverable vs. not-recoverable scenarios, and a day-by-day action plan for the
  remaining 8 days. Replaces need to read 12+ separate status documents.
---

# Track B — May 22 Pre-Launch Status Brief

**Date**: May 22, 2026
**Days to launch**: 8 (May 30 target)
**Go/No-Go decision deadline**: May 29, 20:00 UTC

---

## One-Line Status

All three user gates are overdue. Infrastructure documentation is complete. The launch is
recoverable if Gate 1 and Gate 2 execute this weekend (May 23–24) and Gate 3 executes
May 26–28. If Gate 1 does not start by May 25, the May 30 launch slips to June 6.

---

## Gate Status (as of May 22)

| Gate | Original Deadline | Days Overdue | Status | Time Required | Reference |
|------|------------------|-------------|--------|---------------|-----------|
| Gate 1: Social accounts (Instagram, TikTok, Pinterest) | May 18 | 4 days | NOT STARTED | 45–60 min | TRACK_B_GATE_1_QUICK_REFERENCE.md |
| Gate 2: Canva Brand Kit + zone card production | May 24 | Due in 2 days | NOT STARTED | 30 min Brand Kit + 4–6 hrs zone cards | TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md |
| Gate 3: Kit email account + landing page + 5-email sequence | May 28 | Due in 6 days | NOT STARTED | 3–4.5 hrs (after zone cards exist) | TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md |

**Assets confirmed ready (no user action needed):**
- 18 wild-edibles habit photos: present in `projects/seedwarden/assets/wild-edibles/` (18/18, all CC-licensed, attribution logged in WORKLOG.md lines 3778–3797)
- 63 product mockup images: present in `projects/seedwarden/mockups/` (21 products × 3 variants)
- Logo: `projects/seedwarden/logos/seedwarden_logo_1.png`
- All email copy: `marketing/email-and-launch-plan.md`
- 60-day content calendar: `phase-2-social-content-calendar-60day.md`
- All contingency and go/no-go documents: present and current
- Phase 3 decision package: `TRACK_B_MAY_30_DECISION_PACKAGE.md` (ready May 30)

---

## Recovery Path: May 23–30 Execution Plan

**This plan recovers May 30 launch if executed as written. Each day has a fixed action.**

### May 23 (Friday) — Gate 1 [USER: 45–60 min]

**Required output**: Instagram, TikTok, and Pinterest accounts created and active.

Action: Open `TRACK_B_GATE_1_QUICK_REFERENCE.md`. Execute all steps in order. This is
platform UI work only — all bio copy, handle options, and fallback handles are pre-written
in the document. No decisions needed during execution.

**If handle `seedwarden` is taken on any platform**: use `seedwarden.co` first, then
`seedwarden.seeds`. Document actual handles used in WORKLOG.md using the template in
`TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md`.

**Leave bio links blank**: The Kit landing page URL goes in after Gate 3 (May 27–28).
Backfilling bios takes 2 minutes per platform.

**Asset needed**: Download `projects/seedwarden/logos/seedwarden_logo_1.png` to phone and
computer before starting. TikTok account creation requires the mobile app.

**Done signal**: Three accounts live, each with logo and bio text. Confirm by opening each
account URL in a browser.

---

### May 24 (Saturday) — Gate 2: Brand Kit [USER: 30 min]

**Required output**: Canva Brand Kit live with all colors, fonts, and logo.

Action: Open `TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md`. Execute Section 1 (Brand Kit setup).

**Brand Kit specification (pre-loaded — no decisions needed):**

| Color Name | Hex Code |
|---|---|
| Deep Forest Green | #143b28 |
| Deep Ink Green | #1A3A2A |
| Warm Cream | #F5EDD6 |
| Parchment | #EDE0C4 |
| Sage | #8FA882 |
| Burnt Sienna | #A0522D |
| Zone Band 1 (Hot Band) | #A0522D |
| Zone Band 2 (Warm Band) | #8FA882 |
| Zone Band 3 (Cool Band) | #1A3A2A |
| Zone Band 4 (Cold Band) | #143b28 |

**Fonts**: Playfair Display (heading), Lato or Source Sans 3 (body), Cormorant Garamond (accent). All available free in Canva.

**Note on Canva free tier**: Canva free plan limits Brand Kit to 3 colors. If you hit the
3-color limit, start a Canva Pro free trial (30 days, cancel anytime, credit card required).
The trial covers the full zone card production window. See `GATE_2_DECISION_AND_EXECUTION_GUIDE.md`
for the exact trial activation path.

**Done signal**: Canva Brand Hub shows "Seedwarden" Brand Kit with all 10 colors, 3 fonts,
logo uploaded.

---

### May 24–25 (Saturday–Sunday) — Zone Card Production [USER: 4–6 hrs total]

**Required output**: 8 zone card PDFs exported and ready for Google Drive.

**This is the critical path item.** Zone card production must start on May 24 immediately
after Brand Kit is complete. If this does not start May 24, the May 30 launch is at risk.

Action: Open `CANVA_ZONE_CARD_BATCH_WORKFLOW.md`. Execute in order. Content for all 8 zones
is already written — Canva production is layout/design work only using the Brand Kit you
just created.

**Efficiency note**: Create Zone 5 as the master template first. Then duplicate 7 times
and swap content. The `zone-card-production-workflow.md` documents the fastest duplication
path.

**Done signal**: 8 PDF files exported, named `zone-[X]-quick-start-card.pdf` (X = 3 through 10),
saved to `projects/seedwarden/assets/zone-cards/`.

---

### May 25 (Sunday) — Google Drive Hosting [USER: 30 min]

**Required output**: 8 zone card PDFs uploaded to Google Drive with shareable links.

Action:
1. Upload all 8 zone card PDFs to a Google Drive folder named "Seedwarden Zone Cards"
2. Set folder sharing: "Anyone with the link can view"
3. Copy the direct link for each PDF (right-click > Get link, not the folder link)
4. Paste all 8 links into `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` Section "Zone card delivery links"
5. Test each link in an incognito window — must trigger PDF download, not a Drive viewer page

**Why this matters**: Kit Email 1 delivers the zone card PDF as a download link. If the Drive
links require login or show a viewer page, subscribers cannot access their zone card.

**Done signal**: All 8 links open as PDFs in incognito. No "Request access" prompt.

---

### May 26 (Monday) — Buffer/Later Account [USER: 20 min]

**Required output**: Social scheduling account connected to all three platforms.

Action: Create a free Buffer account at buffer.com. Connect Instagram, TikTok, and Pinterest.
Buffer's free tier handles 3 channels and 10 scheduled posts — sufficient for launch week.

**Upgrade path**: If scheduling 10+ posts simultaneously, Buffer's paid plan is $6/month.
Alternatively, schedule manually via each platform's native scheduler (Instagram Creator Studio,
Pinterest native scheduler, TikTok app).

**Done signal**: Buffer dashboard shows three connected channels. Test by scheduling a draft
post (do not publish — just confirm it drafts without errors).

---

### May 27–28 (Tuesday–Wednesday) — Gate 3: Kit Full Build [USER: 3–4.5 hrs]

**Required output**: Kit account live, subscriber tags configured, landing page published,
5-email welcome sequence built, test email received.

Action: Open `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md`. Execute sections in order. All email
copy is pre-written in `marketing/email-and-launch-plan.md` — Gate 3 is copy-paste and
platform configuration only.

**Build order (from TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md):**
1. Create Kit Creator account (15 min)
2. Create 15 subscriber tags (20 min)
3. Configure zone routing rules (30 min)
4. Create Kit landing page "Your Free Zone Quick-Start Card" (45 min)
5. Build Email 1 (Zone card delivery) — highest priority (30 min)
6. Build Emails 2–5 (welcome sequence) (60 min)
7. Test protocol: subscribe with your own email, confirm zone card downloads, confirm email sequence fires (30 min)
8. Stage launch broadcast email (do not send) (20 min)

**Critical path within Gate 3**: Email 1 (zone card delivery) requires zone card Google Drive
links from May 25. Do not start Gate 3 until those links are confirmed working.

**Done signal**: Test email received in inbox, zone card PDF downloads, welcome sequence
emails queue correctly.

---

### May 29 (Thursday) — Go/No-Go Decision [USER: 2–3 hrs]

Action: Open `MAY_29_GO_NO_GO_DECISION_TEMPLATE.md`. Execute morning block (C2 Visual Assets,
C4 Sales Readiness), afternoon block (C1 Email Infrastructure, C3 Social Ready), and evening
block (final 5-question gate check). Record decision at bottom of document.

**5-question gate check:**
1. All 3 social accounts exist and have bio + logo? Y/N
2. Canva Brand Kit has 10 colors, 3 fonts, logo? Y/N
3. Kit landing page live and zone card email tested end-to-end? Y/N
4. At least 2 Etsy listings ready to publish? Y/N (Track A status determines this — see note below)
5. Launch broadcast staged in Kit? Y/N

**Track A note**: If Track A Etsy blockers (tag corrections + account verification) are not
resolved by May 29, the Etsy listing publication cannot proceed. However, Track B can still
launch with Kit email + social. A partial launch (Kit + social, Etsy listings pending) is
documented in `MAY_30_RISK_AND_CONTINGENCY_PLAN.md` Contingency 3.

**Done signal**: Go/No-Go decision recorded in `MAY_29_GO_NO_GO_DECISION_TEMPLATE.md`.

---

### May 30 (Friday) — Launch Day

If GO decision: Open `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md`. Execute the hour-by-hour
sequence. The sequence is:
- 09:30 UTC: Etsy listings published (if Track A resolved)
- 10:00 UTC: Kit landing page confirmed live
- 12:00 UTC: Launch broadcast email sent to Kit list
- 14:00 UTC: Instagram launch post
- 14:30 UTC: TikTok launch post
- 15:00 UTC: Pinterest pin batch (first 5–7 pins)
- Evening: Monitor Etsy orders, email open rates, social engagement

---

## Scenario Analysis: What Happens If Gates Slip Further

### Scenario A — Gates 1 and 2 complete by May 25 (recoverable)

Zone card production May 24–25. Gate 3 May 27–28. May 30 launch on track.

Revenue impact: None. Full launch.

### Scenario B — Gate 1 completes May 23, Gate 2 completes May 24, but zone card production starts May 25 (tight)

Zone card production May 25–26. Gate 3 must compress to May 27–28 (doable, tight).
Buffer/Later setup deferred to May 29 (still executable).

Revenue impact: None. May 30 launch on track with reduced margin for error.

### Scenario C — Gate 1 not complete by May 25

Zone card production cannot start until Gate 2 is done. With Gate 1 on May 26, Gate 2
on May 26, zone cards May 26–28, Gate 3 on May 28–29: Gate 3 cannot complete before the
May 29 go/no-go. Launch slips to June 6.

Revenue impact: -$120–$240 from one week of lost sales. Recovered within 10 days.

Contingency: See `LAUNCH_CONTINGENCY_PLAYBOOKS.md` Contingency B (June 6 launch with
social accounts delayed) and Contingency C (launch without Kit zone card automation,
deliver cards manually for first subscribers).

### Scenario D — Track A (Etsy) remains blocked on May 30

Track B still launches: Kit + social posts go live May 30. Email list building begins.
Etsy listings activate when Track A blockers resolve (tag corrections + account verification,
documented in `TRACK_A_BLOCKER_RESOLUTION.md`). Track A user actions take approximately 30
minutes total — these are independent of Track B gates.

Revenue impact from Track A delay: $0 from digital sales until Etsy resolves; email list
continues building. If Track A resolves within 7 days of May 30, minimal revenue impact.

---

## Phase 3 Decisions: Also Due May 30

Three Phase 3 decisions are also due May 30 (independent of Track B launch gates). These are
documented in `TRACK_B_MAY_30_DECISION_PACKAGE.md` and take approximately 10 minutes to
confirm. Execute on May 29 evening or May 30 morning.

| Decision | Options | Recommendation | Reference |
|---|---|---|---|
| Sprint scope for June 22–July 13 | Option A (5 bundles, 56–66 hrs) / Option C (3 bundles, 36–44 hrs) | Option C | PHASE_3_SCOPE_DECISION_MATRIX.md |
| Goldenseal sourcing path | Path 1 (live order by June 8, $35–50) / Path 2 (Wikimedia CC, $0) | Path 2 | PHASE_3_GOLDENSEAL_SOURCING_COMPARISON.md |
| Canva Phase 3 palette | Confirm 6 hex codes now / defer to June 15 auto-lock | Auto-lock is fine — no action needed unless you want changes | PHASE_3_CANVA_DESIGN_SYSTEM.md |

After confirming decisions, the June 22 execution window is fully unblocked. No further planning
is required before June 22. The implementation checklists for all decision combinations are in
`projects/seedwarden/phase-3-implementation/`.

---

## Key Documents Quick Reference

| Need | Document |
|---|---|
| Gate 1 step-by-step | TRACK_B_GATE_1_QUICK_REFERENCE.md |
| Gate 1 troubleshooting | TRACK_B_GATE_1_REALTIME_SUPPORT.md |
| Gate 2 step-by-step | TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md |
| Zone card production | CANVA_ZONE_CARD_BATCH_WORKFLOW.md + zone-card-production-workflow.md |
| Gate 3 step-by-step | TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md |
| Email copy (all 5 emails) | marketing/email-and-launch-plan.md |
| Go/No-Go decision form | MAY_29_GO_NO_GO_DECISION_TEMPLATE.md |
| Launch day sequence | MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md |
| If any scenario fails | LAUNCH_CONTINGENCY_PLAYBOOKS.md |
| Track A blockers | TRACK_A_BLOCKER_RESOLUTION.md |
| Phase 3 decisions | TRACK_B_MAY_30_DECISION_PACKAGE.md |

---

*Generated by Seedwarden agent — 2026-05-22*
