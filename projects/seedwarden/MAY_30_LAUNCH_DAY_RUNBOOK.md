---
title: "May 30 Launch Day Runbook — Seedwarden Track B"
date: 2026-05-27
version: 1.0
status: PRODUCTION-READY
scope: >
  Hour-by-hour operator guide for May 30, 2026 launch. Covers 07:30–21:00 UTC.
  Self-contained — no other documents required during the launch window unless
  a contingency fires. All post copy, thresholds, and contact names are here.
references:
  - TRACK_B_LAUNCH_DAY_RUNBOOK.md (Session 1691 — full detail)
  - LAUNCH_DAY_HOUR_BY_HOUR_RUNBOOK.md (Etsy-first variant)
  - CONTINGENCY_DECISION_PLAYBOOK.md (scenario decision trees)
  - TRACK_B_LAUNCH_DAY_COMMON_ISSUES_DECISION_TREES.md (contingency scenarios)
  - TRACK_B_LAUNCH_DAY_ROLLBACK_PROCEDURES.md (rollback playbooks)
  - TRACK_B_LAUNCH_DAY_SUCCESS_SIGNAL_CHECKPOINTS.md (success metrics)
---

# May 30, 2026 — Launch Day Runbook
## Seedwarden Track B — Hour-by-Hour Execution Guide

**Launch**: May 30, 2026, 08:00 UTC  
**Total operator time**: 3.5–4.0 hours across the full day  
**Status entering launch day**: Track B 100% production-ready (verified Session 1693, May 27)  
**Distribution URL**: https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d (inserted 2026-05-27, Session 1701); backup = Google Drive folder

---

## 07:30–07:55 UTC — Pre-Launch (25 minutes)

Complete all four blocks before touching any live platform.

### Block A: System Logins (07:30–07:38, 8 minutes)

Verify access to every platform before the launch window opens. Resolve any login failures now.

- [ ] Canva — canva.com (wanka95@gmail.com). Brand Kit and zone card project files accessible.
- [ ] Kit — kit.com. Dashboard shows zone-card delivery automation.
- [ ] Instagram — @seedwarden account. No 2FA friction. Launch post draft queued in Buffer/Later or Notes.
- [ ] TikTok — @seedwarden account. Launch video draft in Drafts or local folder.
- [ ] Pinterest — Seedwarden business account. Launch pin draft staged.
- [ ] Gmail — Seedwarden send address ready. Compose window open.
- [ ] Reddit — Your account. Navigate to r/herbalism. "Create Post" button visible.

**GO**: All 7 logins confirmed → proceed to Block B.  
**HOLD**: Any login inaccessible → resolve before 07:45. If unresolved by 07:45, note it and continue.

### Block B: File Integrity (07:38–07:48, 10 minutes)

Open an incognito/private browser window. Verify each item.

- [ ] Navigate to the Gist URL. Loads without authentication prompt.
- [ ] All 8 zone card files listed: seedwarden-zone-3 through zone-10-quickstart-card.pdf
- [ ] Download Zone 5 PDF. Opens in-browser, 630–650 KB. Any file under 100 KB = corruption.
- [ ] Test Gist URL from phone browser (not app). PDFs downloadable without login.
- [ ] Backup URL (Google Drive or Dropbox) written down and confirmed accessible in incognito.
- [ ] Kit landing page URL live in incognito — sign-up form visible, "Send My Zone Card" button visible.
- [ ] Kit zone-card delivery automation status: "Published" (not Draft). If Draft, publish now (2 minutes).
- [ ] Instagram, TikTok, and Pinterest bio links all point to Gist URL or Kit landing page.

**GO**: All PDFs accessible + automation Published + bios correct → proceed to Block C.  
**ANY PDF INACCESSIBLE**: Switch to backup URL immediately. Update all bio links before continuing.

### Block C: Channel Test Sends (07:48–07:53, 5 minutes)

One test action per channel to confirm everything fires before going public.

- [ ] Email test: In Kit, send a test email to wanka95@gmail.com. Confirm zone card download link resolves. Confirm zero [PLACEHOLDER] text visible.
- [ ] Social post preview: Open Instagram launch post draft. Confirm Gist URL is present. No bracket placeholders remain.
- [ ] DM template scan: Open influencer DM template. Gist URL placeholder replaced with real URL.

**GO**: All three pass → proceed to Block D.  
**PLACEHOLDER FOUND**: Fix before proceeding (2 minutes per item).

### Block D: GO/HOLD Decision (07:53–07:55, 2 minutes)

All three must be YES to proceed:

1. All 8 zone card PDFs publicly accessible at the distribution URL? YES / NO
2. Kit zone-card delivery automation in Published state? YES / NO
3. All social post drafts contain the real distribution URL? YES / NO

**All YES**: Cleared for launch. Move to 08:00 UTC.  
**Any NO**: Hold. Resolve the failing item. A 15–30 minute delay is better than a broken launch. Do not proceed with a broken distribution link.

---

## 08:00–09:00 UTC — Launch Window (60 minutes)

Execute the 3-channel activation in the order below. Order matters: Reddit posts first (algorithm rewards early organic engagement before external links appear on social); email second (notifies pre-qualified audience); influencer DMs parallel with social.

### 08:00 UTC — Reddit (5 minutes, manual)

Reddit posts cannot be pre-scheduled. Post manually.

Navigate to r/herbalism. Submit new post using copy from TRACK_B_SOCIAL_CALENDAR_MAY28_30.md Post 11.

**Post title** (copy exactly):
```
Free zone-specific quick-start guides for herbalists and gardeners — all 8 USDA zones, no email required
```

**Post body** (Gist URL inserted 2026-05-27):
```
I spent the last few weeks building zone-specific quick-start cards for gardeners and herbalists. Each card covers:

- First/last frost dates for your zone
- Best planting windows for medicinal herbs + vegetables
- Top 5 wild edibles in season by month
- Soil prep notes and variety recommendations

All 8 zones (3–10) are free to download here: https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d

Zone 5 and Zone 7 are the most requested — if you're in one of those, the timing tables are the main thing people find useful.

Happy to answer questions about specific zones or what went into the research.
```

After posting:
- [ ] Post is live on r/herbalism. Screenshot taken.
- [ ] Note the post URL: `_______________________`

**Contingency**: If r/herbalism mod-approval is required and post stays "pending," proceed with other steps. Check status at 09:00 UTC check.

### 08:05–08:15 UTC — Email to Pre-Approved Influencer Contacts (10 minutes)

Send launch notification to every contact who responded to pre-launch outreach. Do not send to contacts with no response — those receive DMs in the next step.

**Email subject**: Zone guides are live — [CONTACT_NAME], here's the link

**Email body**:
```
Hi [FIRST_NAME],

The Seedwarden Zone Quick-Start Cards are live as of this morning.

All 8 zone guides — free, direct download, no email required:
[GIST_URL]

If you'd still like to share these with your community, I'd love that.
No obligation — just letting you know they're up.

Happy to provide pre-written social copy or a newsletter blurb if that helps.

Best,
[YOUR_NAME]
Seedwarden
```

Send to confirmed-interested contacts:
- [ ] Sabrena Gwin (chapters@americanherbalistsguild.com) — if confirmed interest
- [ ] Susan Leopold (info@unitedplantsavers.org) — if confirmed interest
- [ ] John Gallagher (partnerships@learningherbs.com) — if confirmed interest
- [ ] Juliet Blankespoor (chestnutherbs.com contact or Instagram DM) — if confirmed interest
- [ ] Any other contact who responded to pre-launch outreach

Check sent folder. Confirm each delivered (no bounce within 2 minutes).

### 08:15–08:30 UTC — DMs to Non-Responded Contacts (10 minutes, parallel)

For all 15 contacts who did NOT respond to pre-launch outreach, send a short launch notification DM. This runs parallel to social posting.

**DM format** (adapt by platform — Reddit modmail, Discord DM, Instagram DM, or Facebook message):
```
Hi [NAME] — the Seedwarden Zone Quick-Start Cards are live today. Free download for all 8 zones: [GIST_URL]. Thought your community might find them useful. No obligation.
```

Send to non-responded contacts (check off each):
- [ ] r/herbalism mods (Reddit modmail)
- [ ] r/gardening mods (Reddit modmail)
- [ ] r/HerbalMedicine mods (Reddit modmail)
- [ ] The Herbal Haven Discord admin (Discord DM)
- [ ] Materia Medica Discord admin (Discord DM)
- [ ] Herb Club Discord admin (Discord DM)
- [ ] Seattle Herbalism Society admin (Facebook message)
- [ ] AHG chapter coordinators via Sabrena Gwin routing (if not yet responded)
- [ ] Herbal Academy (partnerships@theherbalacademy.com)
- [ ] Any remaining contacts from INFLUENCER_STAGING_VERIFICATION.md

### 08:30 UTC — Instagram Launch Post (3–5 minutes)

Publish or confirm the scheduled Instagram launch post from TRACK_B_SOCIAL_CALENDAR_MAY28_30.md Post 8.

If pre-scheduled in Buffer/Later: confirm queued for 08:30 UTC and URL is correct.  
If posting manually: open draft, confirm Gist URL in caption, post, check bio link.

- [ ] Instagram launch post live. Screenshot taken (timestamp visible).

**Timing rationale**: 08:30 UTC accumulates early engagement from UTC+0 to UTC+3 audiences (UK, Western Europe, Middle East) before US audiences wake. This 3–4 hour head start improves algorithmic visibility for US prime-time feed rankings (12:00–18:00 UTC).

### 08:45 UTC — TikTok Launch Video (3–5 minutes)

Post the TikTok launch video from TRACK_B_SOCIAL_CALENDAR_MAY28_30.md Post 9.

Upload natively — do not cross-post from Instagram. TikTok's algorithm penalizes cross-posted content.

- [ ] TikTok launch video live. Screenshot taken.

**Optional 16:00 UTC boost**: If you have 10 minutes at 16:00–18:00 UTC, post a 15-second follow-up TikTok ("checking in — what zone did you pick up?") to create a second algorithmic push during US peak hours.

### 09:00 UTC — Pinterest Launch Pin (2–4 minutes)

Publish the Pinterest launch pin from TRACK_B_SOCIAL_CALENDAR_MAY28_30.md Post 10.

If pre-scheduled: confirm it fires at 09:00 UTC.  
If manual: open Pinterest creator hub, create pin with launch image, add caption + Gist URL as destination link, pin to primary Seedwarden board.

- [ ] Pinterest launch pin live.

**Second Pinterest push option**: Post a Zone 5 deep-dive pin at 20:00 UTC — Pinterest's peak traffic window.

### Launch Window Completion Check (09:00 UTC)

Before moving to monitoring, confirm all 6 items complete:

- [ ] Reddit post live at r/herbalism (URL recorded)
- [ ] Email sent to all pre-approved influencer contacts (sent folder confirmed)
- [ ] DMs sent to all 15 non-responded contacts (all boxes checked above)
- [ ] Instagram launch post live (screenshot taken)
- [ ] TikTok launch video live (screenshot taken)
- [ ] Pinterest launch pin live (screenshot taken)

**All 6 confirmed**: Proceed to monitoring.  
**Any incomplete**: Complete it now. The launch window extends to 09:30 UTC if needed.

---

## 09:00–14:30 UTC — Hourly Pulse Checks

Each check takes 5 minutes. Record numbers in MAY_30_SUCCESS_METRICS_TEMPLATE.csv. At each check, answer: is anything below the concern threshold?

**What to track at each check** (see TRACK_B_LAUNCH_DAY_RUNBOOK.md Monitoring Dashboard for full list):

| Metric | Where to check |
|--------|---------------|
| Gist views (cumulative) | gist.github.com — view counter (owner-visible) |
| Reddit upvotes | Reddit profile > submitted posts |
| Instagram reach | Instagram Insights > Content > launch post |
| TikTok views | TikTok app > your videos |
| Kit new subscribers | Kit dashboard > subscriber count |
| DM/email replies received | Gmail + Instagram DMs |
| Influencer confirmations | Email/DM sent folder — count who confirmed sharing |

**Concern thresholds (Day 0 pulse checks)**:

| Metric | By 12:00 UTC (4 hours) | By 16:00 UTC (8 hours) | Contingency if below |
|--------|------------------------|------------------------|----------------------|
| Reddit post still live | YES | YES | MAY_30_ISSUE_DECISION_TREES.md Scenario 4 |
| Gist views | 10+ | 25+ | MAY_30_ISSUE_DECISION_TREES.md Scenario 3 |
| Any influencer response | 1+ | 2+ | MAY_30_ISSUE_DECISION_TREES.md Scenario 4 |
| Instagram reach | 30+ | 75+ | MAY_30_ISSUE_DECISION_TREES.md Scenario 2 |
| No platform errors | YES | YES | MAY_30_ISSUE_DECISION_TREES.md Scenario 7 |

At each hourly check, take 1 minute to reply to any Reddit comments or DMs. Responding to Reddit comments on launch day is the single highest-ROI action for early post performance.

### 09:30 UTC — First Check
Record metrics. No decision gates yet. Reply to any Reddit comments received.

### 11:00 UTC — Second Check
Record metrics. Check influencer response count. If zero influencer responses and all outreach confirmed sent: no action. Influencer amplification lags 24–48 hours.

### 12:00 UTC — First Hard Decision Point

**If Gist views below 10 by 12:00 UTC**: Run distribution diagnostic from MAY_30_ISSUE_DECISION_TREES.md Scenario 3 before the next check.

**12:00 UTC binary decision**: Is anything triggering a contingency? YES → open MAY_30_ISSUE_DECISION_TREES.md. NO → log numbers and continue.

### 13:00 UTC — Mid-Day Checkpoint

Mid-day engagement rate check. Decision points:

| Condition | Action |
|-----------|--------|
| Gist views 10–25, Reddit 5+ upvotes | Normal trajectory. Continue. |
| Gist views below 10, no influencer responses | Run Scenario 4 in MAY_30_ISSUE_DECISION_TREES.md |
| Instagram engagement stalling (below 30 reach) | Run Scenario 2 in MAY_30_ISSUE_DECISION_TREES.md |
| Reddit post removed | Post to r/foraging or r/homesteading as alternative. |
| Everything on track | Log metrics, continue. Post optional Reddit follow-up comment. |

**Acceleration option if tracking well**: If Gist views are above 25 by 13:00 UTC and at least 2 influencer responses received, this is a strong early signal. Consider posting a second Instagram Story with a direct link sticker for additional traffic push.

**Pause option if underperforming**: If Gist views are below 5 and all 15 DMs sent, do not escalate yet. Day 0 underperformance is normal. Wait for Day 3 data (June 2) before changing strategy.

### 14:30 UTC — Final Hourly Check

Last of the hourly pulse checks. After this, switch to 4-hour intervals. Record full metric set.

---

## 16:00 UTC — Mid-Day Extended Check (10 minutes)

Record all metrics. Make one binary decision: is anything triggering a contingency scenario?

**Actions at 16:00 UTC**:
- Post a Reddit follow-up comment on the r/herbalism launch post if it has received any upvotes. Format: "Thanks for the interest — Zone 7 seems to be the most popular so far. Happy to answer questions about specific zones." This re-engages the thread and boosts algorithmic visibility.
- Optional: Post the additional TikTok video (see 08:45 note above) if you have 10 minutes available.
- Optional: Post a Zone 5 deep-dive Pinterest pin (peak Pinterest traffic window begins at 20:00 UTC — can queue now).

---

## 18:00 UTC — Day 1 Wrap-Up Begins (30 minutes)

### Aggregate Day 0 Metrics (18:00–18:15 UTC)

Fill in the Day 0 snapshot. Paste into tracking log or MAY_30_SUCCESS_METRICS_TEMPLATE.csv:

```
Day 0 (May 30) Snapshot — logged [TIME] UTC

DISTRIBUTION
Gist views (cumulative): ___
Reddit r/herbalism upvotes: ___
Reddit comments: ___
Instagram reach (launch post): ___
Instagram new followers: ___
TikTok views (launch video): ___
Pinterest saves: ___
Kit new subscribers: ___

INFLUENCER ENGAGEMENT
Contacts reached (DM/email sent): ___ of 15
Contacts who responded (any response): ___
Contacts who confirmed they'll share: ___
Contacts who shared publicly: ___

COMMUNITY
DM or email inquiries received: ___
Comments responded to: ___
Notable qualitative feedback (1–3 sentences): ___

TECHNICAL
Any platform errors: YES / NO (describe if YES)
Gist URL accessible throughout day: YES / NO
Kit automation fired correctly: YES / NO
```

### Compare Against Day 3 Baseline (18:15–18:25 UTC)

From CONTINGENCY_DECISION_THRESHOLDS.md — Day 3 thresholds (June 2):
- Gist views > 30 by Day 3 = baseline working
- Gist views > 70 by Day 3 = activate Track A holdout influencers
- Reddit upvotes > 10 by Day 3 = healthy distribution

Day 0 rough targets (20–30% of Day 3 baseline):
- Gist views: 10–25 (organic Day 0 without influencer amplification)
- Reddit upvotes: 5–15 on r/herbalism post
- Instagram reach: 50–150 (new account baseline)

**If Day 0 numbers are above targets**: Strong start, influencer outreach is working, no action change.  
**If Day 0 numbers are below targets**: Normal for Day 0. Do not panic. Day 3 (June 2) is the first meaningful checkpoint.

### Qualitative Notes (18:25–18:40 UTC)

Record in tracking log:
1. What did the community response look like? Any notable comments, questions, or DMs?
2. Which platform showed the most activity?
3. Were there any technical issues?
4. Any unexpected positive signals?
5. What is the single most important action for tomorrow (May 31)?

### Prepare for Day 3 Checkpoint (18:40–18:55 UTC)

The Day 3 checkpoint is June 2, 2026 at 08:00 UTC. Documented in DAY_3_AND_7_DECISION_GATES.md.

Before closing out May 30:
- [ ] May 31/June 1 social content queued (check TRACK_B_SOCIAL_CALENDAR_MAY28_30.md for June 1–7 ramp-up schedule)
- [ ] Day 0 snapshot logged in MAY_30_SUCCESS_METRICS_TEMPLATE.csv
- [ ] All open influencer responses replied to
- [ ] No unresolved platform issues (if any, document for June 2 review)

---

## 20:00 UTC — Final Monitoring Check

One final metric read before end-of-day close. If anything is still open (platform issue, unread DM, outstanding contingency), address it now or document it for May 31 morning.

---

## Quick-Reference Card

```
MAY 30 LAUNCH — ALL TIMES UTC

PRE-LAUNCH (07:30–07:55)
  07:30 — Verify 7 platform logins (Block A)
  07:38 — Verify all 8 PDFs accessible, Kit Published, bios correct (Block B)
  07:48 — Test email send to self; scan drafts for placeholders (Block C)
  07:53 — GO/HOLD decision — all 3 YES required (Block D)

LAUNCH WINDOW (08:00–09:00)
  08:00 — Reddit r/herbalism post (manual)
  08:05 — Email to pre-approved influencer contacts
  08:15 — DMs to all 15 non-responded contacts (parallel with social)
  08:30 — Instagram launch post
  08:45 — TikTok launch video
  09:00 — Pinterest launch pin

MONITORING (hourly 09:30–14:30, then 16:00, 18:00, 20:00)
  12:00 — First hard decision point (any contingency scenarios?)
  13:00 — Mid-day checkpoint (acceleration vs. pause)
  16:00 — Reddit follow-up comment + optional TikTok boost
  18:00 — Day 1 wrap-up begins

CONCERN THRESHOLDS (Day 0)
  By 12:00 UTC: Reddit post still live, 10+ Gist views, 1+ influencer response
  By 16:00 UTC: 25+ Gist views, 2+ influencer responses, no platform errors

END-OF-DAY (18:00–20:00)
  Log Day 0 snapshot in MAY_30_SUCCESS_METRICS_TEMPLATE.csv
  Queue May 31 content
  Resolve or document any open platform issues

BACKUP URL: ___________________________
CONTINGENCY PLAYBOOK: MAY_30_ISSUE_DECISION_TREES.md
ROLLBACK GUIDE: MAY_30_ROLLBACK_PROTOCOLS.md
SUCCESS THRESHOLDS: MAY_30_SUCCESS_METRICS_TEMPLATE.csv
```

---

*Document version: 1.0 — May 27, 2026*  
*Companion documents: MAY_30_ISSUE_DECISION_TREES.md, MAY_30_ROLLBACK_PROTOCOLS.md, MAY_30_SUCCESS_METRICS_TEMPLATE.csv, MAY_30_COMMUNICATION_TEMPLATES.md*  
*Full-detail reference (do not open during launch window unless needed): TRACK_B_LAUNCH_DAY_RUNBOOK.md, CONTINGENCY_DECISION_PLAYBOOK.md, LAUNCH_DAY_DECISION_TREES_DETAILED.md*
