---
title: "Phase 2 Launch Day Master Checklist"
subtitle: "Hour-by-hour timeline: May 30 06:00 UTC → May 31 06:00 UTC"
date: 2026-05-09
session: 907-item36
status: production-ready
launch-date: 2026-05-30
references:
  - TRACK_B_LAUNCH_DAY_OPERATIONS_GUIDE.md (checkpoint logic and KPI definitions)
  - phase-2-launch-day-checklist.md (platform verification steps)
  - phase-2-automation-contingency-playbook.md (failure mode responses)
  - phase-2-email-automation-sequence.md (broadcast and automation specs)
  - phase-2-social-posting-scheduler.csv (May 30 content schedule)
---

# Phase 2 Launch Day Master Checklist
## May 30, 2026 — 06:00 UTC Through May 31, 2026 — 06:00 UTC

**How to use this document**: Open at 05:45 UTC on May 30. Work through each time block in sequence. Check every box before moving to the next block. Each block shows the exact dashboard to open, the exact number to record, and the exact decision to make. This is the only document you need open on launch day.

**Alert system**: Automated alerts via Kit (email) and Discord webhook are specified per checkpoint. Configure these before May 30 — see the Alert Setup section at the end of this document.

---

## Pre-Launch Block — May 29, 17:00–20:00 UTC (T-17h)

This block is the last opportunity to fix any systemic issue before launch. Complete it on the evening of May 29.

**17:00 UTC — System Verification (30 min)**

- [ ] **Buffer queue**: Open Buffer > Queue view. Confirm 7 social posts are queued for May 30. Each shows a future timestamp (not "Failed" or "Draft"). If any post shows an error, re-upload now.
- [ ] **Kit broadcast**: Open Kit > Broadcasts. Find the launch broadcast. Status reads "Scheduled" with timestamp "12:00pm May 30." If status is "Draft": click into broadcast > Schedule > enter 12:00pm May 30 UTC > Confirm.
- [ ] **Kit automation**: Open Kit > Automations. Find "Seedwarden Welcome." Status reads "Published." If paused: click Resume.
- [ ] **Etsy listings**: Open Etsy Shop Manager > Listings. Count listings with "Active" status. All 21 should show Active (green dot). If any show "Draft": click Publish.
- [ ] **SEEDWARDEN15 coupon**: Etsy > Marketing > Sales & Coupons. SEEDWARDEN15 shows "Active" with 15% discount and no expiry. If missing: create it now (15% off, no minimum, no expiry — 3 minutes).
- [ ] **Zone card downloads**: Open all 8 Google Drive zone card URLs in 8 incognito tabs. Each downloads a PDF within 10 seconds. If any shows "Request access": go to Drive > sharing settings > "Anyone with the link can view" > copy the ?export=download URL > update Kit Email 1 zone variant > re-save.

**Done signal**: All 6 items above checked. No errors visible. Log "T-17h system check passed" in WORKLOG.md with timestamp.

**17:30 UTC — Supplier Readiness (15 min)**

*Skip this block if all 21 Phase 2 products are digital downloads — skip to 18:00 UTC.*

- [ ] Email your supplier: "Phase 2 launches May 30. Expecting 10–20 orders by May 31 EOD. Can you confirm you can handle fulfillment May 31–June 2? Please reply within 1 hour."
- [ ] Wait for reply. If reply confirms capacity: check this box and proceed.
- [ ] If no reply within 1 hour: call or text supplier directly. Log response in WORKLOG.md.
- [ ] If supplier says "cannot handle": activate `phase-2-automation-contingency-playbook.md` Scenario 5 immediately.

**18:00 UTC — Pre-Launch Stand-Down**

- [ ] Close all non-essential tabs and apps
- [ ] Confirm phone is charged and notifications are on for Kit, Etsy Seller app, and email
- [ ] Confirm laptop is charged or plugged in for the morning session
- [ ] Set alarm for 05:30 UTC (05:30 = 1:30am ET / 10:30pm PT — adjust if your time zone differs)
- [ ] Log "Pre-launch stand-down complete" in WORKLOG.md

---

## Launch Morning — May 30, 05:30–09:00 UTC

**05:30 UTC — Wake and Device Setup (15 min)**

Open all monitoring tabs before QA. Do not start checking yet — just load them.

| Tab | URL / Location |
|---|---|
| Tab 1 | Etsy Shop Manager > Stats > Today |
| Tab 2 | Etsy store public URL (incognito, logged out) |
| Tab 3 | Kit > Broadcasts |
| Tab 4 | Kit > Automations |
| Tab 5 | Kit > Subscribers (live count) |
| Tab 6 | Buffer queue view |
| Phone | Etsy Seller app — push notifications ON |
| Spreadsheet | phase-2-launch-analytics-dashboard-template.csv — open to Daily_Log sheet |

**05:45 UTC — Baseline Metrics Log (15 min)**

Record these numbers BEFORE any launch traffic. These are the "before" state. Everything measured after 08:00 UTC is Phase 2 attributable.

| Metric | Source | Pre-Launch Baseline |
|---|---|---|
| Etsy shop views (last 7 days) | Etsy Shop Manager > Stats > Traffic | ___ |
| Etsy total orders (all time) | Etsy Shop Manager > Orders > count | ___ |
| Kit subscriber count | Kit > Subscribers > count | ___ |
| Instagram followers | Instagram profile | ___ |
| TikTok followers | TikTok profile | ___ |
| Pinterest monthly viewers | Pinterest Analytics > Overview | ___ |

Record these in the Daily_Log sheet under the May 30 row, column "Notes."

**06:00 UTC — First QA Pass (60 min)**

**Etsy QA (20 min)**:
- [ ] Open Etsy Shop Manager > Listings. All 21 listings show "Active" (green dot). Any Draft → click Publish.
- [ ] Click 5 random listings > Photos section > confirm 5 images present (slots 1–3 mockups, slots 4–5 lifestyle)
- [ ] Open 3 highest-traffic listings in Tab 2 (incognito). Confirm lifestyle images visible in gallery.
- [ ] Etsy > Marketing > Sales & Coupons. SEEDWARDEN15 confirmed Active.
- [ ] Done signal: all 21 active, SEEDWARDEN15 active, no listing errors in incognito view.

**Kit QA (20 min)**:
- [ ] Kit > Broadcasts. Launch broadcast status = "Scheduled" for 12:00pm UTC. Note: DO NOT click "Send Now" — wait for the scheduled time.
- [ ] Kit > Automations. "Seedwarden Welcome" status = "Published."
- [ ] Open Kit landing page in a new incognito tab. Fill in: name "LaunchTest," test email address (wanka95+launchday@gmail.com), Zone 5. Click "Send My Zone Card."
- [ ] Wait up to 60 seconds. Confirm Email 1 arrives at test address. Open the zone card download link. Confirm Zone 5 PDF downloads.
- [ ] Record current subscriber count in the baseline table above.
- [ ] Done signal: broadcast scheduled, automation published, Zone 5 test download confirmed.

**Social QA (10 min)**:
- [ ] Buffer > Queue. Find the Instagram launch post at 10:00am EST (15:00 UTC). Status = "Scheduled." Preview shows correct image and caption.
- [ ] Find TikTok launch post at 10:00am EST. Status = "Scheduled." File is a video file.
- [ ] Find Pinterest post at 11:00am EST. Status = "Scheduled."
- [ ] Buffer > Settings > Connected Accounts. All 3 platforms show green/active status. No "Reconnect" warning.
- [ ] Done signal: all 3 platforms show scheduled status, no connection errors.

**Zone Card Final Check (10 min)**:
- [ ] Open all 8 Google Drive zone card download URLs in 8 incognito tabs. Confirm each downloads a PDF (not a viewer page).
- [ ] Spot-check zone number in each PDF (header or title should display the zone number).
- [ ] Done signal: all 8 PDFs download correctly.

---

## Launch Phase — May 30, 08:00–15:00 UTC

**08:00 UTC — Pinterest First Pin Live**

- [ ] Check Buffer: Pinterest pin scheduled for 08:00 UTC should show "Published" by 08:10 UTC
- [ ] Open Pinterest profile directly and confirm pin is visible in profile feed
- [ ] If not published by 08:15: log into Pinterest directly > Create pin > upload zone card preview image > add caption from social-posting-scheduler.csv row 3 > publish manually
- [ ] Watch for saves (first 30 min): zero saves by 08:30 is normal. Zero saves by 09:00 = check pin image quality and description text.

**09:00 UTC — Etsy Launch Confirmation**

- [ ] Open Etsy store in Tab 2 (incognito). Scroll the store front. Lifestyle images visible in listing thumbnails? (Thumbnails show slot 1 — mockup. This is correct. Lifestyle images appear in slots 4–5 inside the listing.)
- [ ] Click 3 listings. Confirm all 5 images visible in each gallery.
- [ ] Record: first organic Etsy shop views arriving? (Tab 1 > Stats > Today > Views) Log count in Daily_Log spreadsheet.
- [ ] This is the de facto launch moment. Etsy's algorithm processes the updated listings from this point.

**09:00–12:00 UTC — Pre-Email Organic Monitoring (every 30 min)**

Check these at 09:00, 09:30, 10:00, 10:30, 11:00, 11:30, 12:00 UTC:

| Metric | Source | Log in spreadsheet |
|---|---|---|
| Etsy shop views today | Tab 1 > Stats > Today | Daily_Log col B |
| Etsy new orders (if any) | Tab 1 > Orders | Daily_Log col D and E |
| Kit subscribers (if any new) | Tab 5 | Daily_Log col C |

Pre-email organic orders (before 12:00 UTC) = highest-quality conversion signal. Log each one in WORKLOG.md with timestamp and product purchased.

**10:00 UTC — Instagram Launch Post (10:00am EST)**

Buffer should auto-post. Check at 10:10 UTC:
- [ ] Buffer > Queue: Instagram post shows "Published"
- [ ] Open Instagram profile directly: launch post visible at top of feed
- [ ] Check caption and link in post — correct Kit landing page URL in bio link
- [ ] If Buffer failed: open Instagram app > Create post > upload hero image from `marketing/lifestyle-photos/etsy-ready/cluster-a-hero.jpg` > paste caption from social-posting-scheduler.csv May 30 Instagram row 1 > post now

**10:00 UTC — TikTok Launch Post (10:00am EST)**

Buffer should auto-post TikTok simultaneously. Check at 10:10 UTC:
- [ ] Buffer > Queue: TikTok post shows "Published"
- [ ] Open TikTok profile: video visible and playing
- [ ] Check view count at 10:15, 10:30, 11:00 UTC. Log in spreadsheet.
- [ ] TikTok velocity feedback: if zero views by 11:00 UTC, video may have failed to process. Delete and re-upload directly in TikTok app.

**11:00 UTC — Pinterest Pins #2 and #3**

Buffer auto-posts per schedule. Check at 11:10 UTC:
- [ ] Pinterest pin #2 (11:00 UTC) shows "Published" in Buffer. Visible on Pinterest profile.
- [ ] Pinterest pin #3 queued for 03:30pm EST (20:30 UTC) — verify in queue.

**12:00 UTC — CHECKPOINT 1 (T+7h from first content, T+6h from Etsy launch)**

This is a system health check — not a go/no-go decision. The T+12h checkpoint at 21:00 UTC is the go/no-go.

Collect all 4 metrics now:

| Metric | Target | Actual | Status |
|---|---|---|---|
| Kit form submissions so far | 3+ | ___ | Green / Yellow / Red |
| Instagram posts live | 1, with engagement (likes or comments) | ___ | Green / Yellow / Red |
| TikTok videos live | 1, with 10+ views | ___ | Green / Yellow / Red |
| Shopify/Etsy orders | 0–2 is normal; 5+ is excellent | ___ | — |

**Decision rule at Checkpoint 1**:
- All 4 metrics at target → continue normal operations
- Any metric at 0 AND you have not already diagnosed the cause → spend 30 min diagnosing now (see `phase-2-automation-contingency-playbook.md` Scenario 1)
- Kit submissions = 0 → check bio links on all 3 platforms immediately (tap each link manually)

Log Checkpoint 1 results in WORKLOG.md: timestamp, all 4 metric values, decision made.

**12:00 UTC — Email Broadcast Fires**

The Kit broadcast fires automatically at 12:00pm UTC. You will NOT press any button — Kit sends automatically.

At 12:05 UTC:
- [ ] Kit > Broadcasts. Launch broadcast status should show "Sending" or "Sent" (may show "Sending" for up to 20 minutes while Kit processes the queue)
- [ ] If status still shows "Scheduled" at 12:20 UTC: click into the broadcast > click "Send Now." This overrides the schedule without changing the email.
- [ ] If broadcast is missing entirely: Kit > Broadcasts > New Broadcast. Subject: "Phase 2 is live — your zone card library just doubled." Body from `marketing/email-and-launch-plan.md` > Launch Broadcast section. Send to "All Confirmed Subscribers" > Send Now. Takes 10 minutes.

**12:00–15:00 UTC — Post-Broadcast Monitoring (every 30 min)**

Check at 12:30, 13:00, 13:30, 14:00, 14:30, 15:00 UTC:

| Metric | Source | Target by 15:00 UTC | Log |
|---|---|---|---|
| Broadcast delivery rate | Kit > Broadcasts > Stats | 90%+ delivered | Daily_Log |
| Broadcast open rate | Kit > Broadcasts > Stats | 25%+ (check at T+4h) | Daily_Log |
| Broadcast click rate | Kit > Broadcasts > Stats | 8%+ | Daily_Log |
| Bounce rate | Kit > Broadcasts > Stats | Under 2% | Real_Time_Alerts sheet |
| Etsy orders (email-attributed) | Shop Manager > Orders | Any order after 12:00 UTC | Daily_Log col D |
| Kit new subscribers | Kit > Subscribers | Growing from baseline | Daily_Log col C |

**Bounce rate alert**: If bounce rate hits 5%+ within the first hour of sending, pause the broadcast: Kit > Broadcasts > [broadcast] > Pause Send. Then diagnose. A 5%+ bounce rate in the first hour means a significant portion of your list has invalid addresses — sending to all of them will damage your sender reputation. See `phase-2-automation-contingency-playbook.md` Scenario 3 for list cleaning procedure.

---

## Afternoon/Evening Launch Phase — May 30, 15:00–21:00 UTC

**15:00 UTC — Instagram Post #2 (10:00am EST was post #1; this is the 2:00pm EST carousel)**

Buffer auto-posts the afternoon carousel. Check at 15:10 UTC:
- [ ] Buffer > Queue: Instagram carousel shows "Published"
- [ ] Open Instagram profile: carousel post visible. Tap through all 5 slides — confirm correct images and captions.
- [ ] Check engagement (likes + comments) on both Instagram posts combined. Log in spreadsheet.

**17:00 UTC — Email and Social Mid-Day Check**

- [ ] Kit open rate: check at 5h after send (12:00 UTC send → check at 17:00 UTC). Open rate stabilizes at T+4h to T+6h.
  - Above 30%: excellent. Log as Green.
  - 20–29%: on target. Log as Yellow-Green.
  - Below 20%: investigate inbox placement. Check Kit > Settings > Email Settings for sender authentication status.
- [ ] TikTok video #1 cumulative views: should be 50–200+ by 17:00 UTC. Log in spreadsheet.
  - Above 50 views: good algorithm velocity. Log Green.
  - 10–49 views: normal range for a newer account. Log Yellow.
  - Under 10 views: possible algorithmic suppression. Try posting TikTok video #2 (from 06:00pm EST slot) now, slightly earlier, to test if the platform is responsive.

**19:00 UTC — Etsy Mid-Day Check**

- [ ] Etsy Shop Manager > Orders: total orders placed today? Log in Daily_Log.
- [ ] Etsy > Stats > Today > Traffic sources: which source is driving the most views? (Etsy search organic, social referral, direct?) Note the breakdown.
- [ ] Kit > Subscribers: total new subscribers today (current count minus pre-launch baseline). Log in Daily_Log col C.

**20:00 UTC — T+12h Checkpoint Prep (30 min)**

Collect all 7 KPI values before the T+12h checkpoint:

| KPI | Source | Target | Actual |
|---|---|---|---|
| Kit form submissions (since 05:00 UTC) | Kit > Subscribers (current minus baseline) | 12+ | ___ |
| Instagram posts live + engagement | Instagram Insights > [each post] | 2+ posts, 20+ combined likes+comments | ___ |
| TikTok videos live + views | TikTok Analytics | 2 videos, 50+ combined views | ___ |
| Pinterest pins live + saves | Pinterest Analytics | 2+ pins, 5+ saves | ___ |
| Etsy orders (since 05:00 UTC) | Shop Manager > Orders | 5–12 | ___ |
| Email open rate | Kit > Broadcasts > Stats | 25%+ | ___ |
| Avg order value | Shop Manager > Orders > total revenue / order count | $18–25 | ___ |

---

## T+12h Checkpoint — May 30, 21:00 UTC (Major Decision)

**21:00 UTC — Checkpoint 2: Go/No-Go for Continued Phase 2 Operations**

Apply the 7 KPIs collected at 20:00 UTC against success criteria:

**Green (proceed normally)** — 5 or more of 7 KPIs at target:
- Continue scheduled operations. Confirm suppliers are ready for May 31–June 2 fulfillment.
- Log "T+12h: GREEN" in WORKLOG.md with timestamp and all 7 values.
- Send Discord webhook alert: "LAUNCH STATUS: GREEN — [X] orders, [Y] signups, [Z]% email opens"
- Go to bed. May 31 is normal ops day.

**Yellow (proceed with elevated monitoring)** — 3 or 4 of 7 KPIs at target:
- Continue all scheduled content. Increase checkpoint frequency to every 4h (next check at 01:00 UTC).
- Identify the 2–4 KPIs below target. For each, run the diagnosis checklist from `phase-2-automation-contingency-playbook.md`.
- Log "T+12h: YELLOW" in WORKLOG.md with which KPIs missed and diagnosis notes.
- Send Discord webhook alert: "LAUNCH STATUS: YELLOW — monitoring elevated. [X] KPIs at target, [Y] KPIs below target."

**Red (pause and investigate)** — fewer than 3 of 7 KPIs at target, OR zero orders by T+12h:
- Pause any additional content scheduled for May 31 until root cause is identified.
- Open `phase-2-automation-contingency-playbook.md` Scenario 1 diagnosis tree — work through it systematically.
- Log "T+12h: RED" in WORKLOG.md with full metric snapshot and time.
- Send Discord webhook alert: "LAUNCH STATUS: RED — pause new content, diagnose. [X] KPIs at target."
- Do not schedule or post any new social content until you have identified the root cause.

**Document decision in WORKLOG.md** with: timestamp, all 7 KPI values, color status, decision made, any contingency actions initiated.

---

## May 31 — Continued Operations (T+24h)

**05:00 UTC — Overnight Metrics Check**

Review what happened between 21:00 UTC May 30 and 05:00 UTC May 31 (8 hours overnight):

- [ ] New Etsy orders (check Shop Manager > Orders > filter "Last 8 hours")
- [ ] New Kit subscribers (current count minus T+12h count)
- [ ] TikTok video overnight views (check both videos)
- [ ] Email bounce rate — has it changed since T+12h? (Kit > Broadcasts > Stats)
- [ ] Any customer messages in Etsy inbox? Respond within 4 hours per launch-day protocol.

**06:00 UTC — May 31 Social Content**

Buffer auto-posts the Instagram Story series (behind-the-scenes shoot content) at 09:00am EST (14:00 UTC). Verify in Buffer that this post is queued.

TikTok educational video #2 (11:00am EST, 16:00 UTC) — verify in Buffer or queue natively.

Pinterest pin scheduled for 08:00pm EST (01:00 UTC June 1) — verify in Buffer.

**Morning monitoring May 31 (05:00–13:00 UTC)**:

| Time | Action |
|---|---|
| 05:00 UTC | Overnight metrics check (see above) |
| 09:00 UTC | Confirm supplier fulfillment for May 30 orders — any orders shipped yet? |
| 12:00 UTC | Log 24h metrics snapshot: orders, signups, email open rate |
| 13:00 UTC | Check: any metric down 30%+ from T+12h? If yes → investigate (see Contingency Scenario 1) |

---

## T+38h Checkpoint — June 1, 20:00–21:00 UTC (Phase Gate Decision)

**20:00 UTC — Collect 48h Metrics**

Collect all 7 metrics for the full 48-hour window (May 30 05:00 UTC through June 1 20:00 UTC):

| KPI | Target (PASS) | At Risk | Fail | Actual |
|---|---|---|---|---|
| Total Kit signups (48h) | 20+ | 15–19 | Under 15 | ___ |
| Total Etsy orders (48h) | 10–20 | 8–11 | Under 8 | ___ |
| Average order value (48h) | $18–25 | $12–17 | Under $12 | ___ |
| Email sequence completion rate | 80%+ | 70–79% | Under 70% | ___ |
| Repeat customer orders (Phase 1 customers) | 2–4 | 1 | 0 | ___ |
| New customer orders (non-Phase-1) | 0–2 initially | — | — | ___ |
| Fulfillment status | 100% shipped by June 2 | 80–99% processed | Under 80% | ___ |

**21:00 UTC — T+38h Phase Gate Decision**

Apply the PASS/AT RISK/FAIL criteria:

**PASS** — 20+ orders AND $200+ combined revenue AND 80%+ email sequence AND 100% fulfillment on schedule:
- Phase 2 is on track for the June 30 gate (30-day conversion validation)
- Continue daily monitoring through June 30 per the monitoring schedule below
- Log "T+38h: PASS" in WORKLOG.md with all metric values
- Send Discord webhook: "PHASE GATE T+38H: PASS — Phase 2 on track"

**AT RISK** — 10–19 orders OR below 80% email sequence OR fulfillment delays up to 2 days:
- Daily monitoring through June 8 to identify and fix issues
- Identify which specific criterion is at risk and activate the corresponding contingency in this playbook
- Log "T+38h: AT RISK" in WORKLOG.md with specific criteria at risk and action plan
- Expected resolution by June 8 before the Phase 2 monitoring escalates

**FAIL** — Under 10 orders OR broken email sequence OR 50%+ fulfillment failure:
- Pause new content scheduling immediately
- Investigate root cause: use diagnosis trees in `phase-2-automation-contingency-playbook.md`
- Do not proceed past June 8 without resolution
- Log "T+38h: FAIL" in WORKLOG.md with full incident documentation
- Send Discord webhook: "PHASE GATE T+38H: FAIL — pause new content, diagnose"
- Document all steps taken to resolve in WORKLOG.md daily

---

## Automated Alert Setup (Configure Before May 30)

### Kit Email Alerts

In Kit, create these automation rules to trigger email alerts to wanka95@gmail.com:

| Alert condition | Kit trigger | Email subject |
|---|---|---|
| Broadcast bounce rate above 5% | Kit does not natively alert — check manually at T+1h, T+4h, T+12h | Manual check only |
| New subscriber joins | Kit > Automations > New rule: Form submitted → send notification email to wanka95@gmail.com | "New subscriber: [name] signed up (Zone [X])" |
| New Etsy order | Kit does not track Etsy — use Etsy app push notification instead | Etsy app sends a push notification for every new order automatically |

### Discord Webhook Alerts (Optional but Recommended)

Set up a Discord server (free) with a single channel named #launch-monitoring. Create a webhook URL in Discord > Server Settings > Integrations > Webhooks > New Webhook > copy URL.

At each checkpoint, manually send a Discord webhook using any free webhook test tool (e.g., webhook.site) or simply post the status update directly in Discord. This serves as an audit log of decisions made in real time.

**Manual Discord post template at each checkpoint**:
```
LAUNCH STATUS UPDATE — May 30, [UTC time]
Orders: [X]
Kit signups: [Y]
Email open rate: [Z]%
Decision: [GREEN / YELLOW / RED / PASS / AT RISK / FAIL]
Action: [Continue normal ops / Contingency A activated / etc.]
```

### Etsy Push Notifications

In the Etsy Seller app (iOS or Android):
- Settings > Notifications > Orders: ON
- Settings > Notifications > Messages: ON
- Settings > Notifications > Shop Stats: Daily digest ON

Every new Etsy order sends a push notification within 60 seconds. This is your most reliable real-time order signal.

---

## Rollback Procedures by Failure Mode

| Failure mode | Rollback action | Time required |
|---|---|---|
| Etsy listing error (under review) | Do not recreate. Email Etsy support. Launch with remaining active listings. | 5 min to report; 24–48h for Etsy to resolve |
| Kit broadcast not sent | Kit > Broadcasts > [broadcast] > Send Now | 30 seconds |
| Kit automation paused | Kit > Automations > "Seedwarden Welcome" > Resume | 5 seconds |
| Zone card download link broken | Kit > Sequences > Email 1 > [zone variant] > update link to ?export=download format > re-test | 5 min per zone |
| Buffer fails all social posts | Log into each platform directly. Post manually. Captions and images in social-posting-scheduler.csv. | 15–20 min total |
| Bounce rate above 5% | Pause broadcast (Kit > Broadcasts > Pause). Export subscriber list. Clean invalid addresses. Re-send to cleaned list. | 2–4 hours |
| T+12h checkpoint: RED | Stop new content. Open phase-2-automation-contingency-playbook.md Scenario 1. Diagnose traffic vs. conversion problem. | 30 min diagnosis, 1–2h remediation |
| T+38h gate: FAIL | Pause new content. Document full incident. Set 7-day investigation period. Do not proceed to Phase 3 planning. | 7 days |

---

## Daily Monitoring Schedule (June 1–30)

After the T+38h checkpoint, transition to ongoing monitoring:

| Day | Time (UTC) | Action |
|---|---|---|
| Every day | 06:00 UTC | Morning check: overnight orders, email engagement, social comments. Log 5 key metrics in Daily_Log. |
| Every day | 20:00 UTC | Evening check: day's performance. If any metric drops 20%+ from prior day, investigate. |
| Mon/Wed/Fri | 09:00 UTC | Supplier fulfillment check: confirm shipping deadlines being met |
| Every Sunday | 20:00 UTC | Weekly summary: compile week's numbers, post to WORKLOG.md |
| June 27 | 20:00 UTC | 30-day snapshot: run full analytics export, update Decision Framework sheet in dashboard |

### June 30 Gate (30-day Phase 2 validation)

At June 30, run the Early_Decision_Framework sheet in `phase-2-launch-analytics-dashboard-template.csv`. Score all 6 criteria. If 5 or more pass: Phase 2 is succeeding — proceed to Phase 3 planning timeline. If fewer than 5 pass: document failures in WORKLOG.md, set a 2-week remediation period, and re-evaluate.

---

## Quick-Reference Card (Print for May 30)

```
T-17h (May 29, 17:00 UTC): System verification. All 6 checks pass? Log and stand down.

05:30 UTC (May 30): Wake. Open 6 browser tabs. Record baseline metrics.
05:45 UTC: Baseline log complete.
06:00 UTC: QA block begins (60 min). Etsy / Kit / Buffer / Zone cards.
07:00 UTC: All QA complete. Wait for 08:00 UTC.
08:00 UTC: First Pinterest pin. Verify published.
09:00 UTC: Etsy launch confirmation. Begin 30-min monitoring cadence.
10:00 UTC: Instagram + TikTok launch posts. Verify both published.
11:00 UTC: Pinterest pin #2.
12:00 UTC: CHECKPOINT 1 (4 metrics). Kit broadcast fires automatically.
12:05 UTC: Confirm broadcast status = Sending.
13:00–14:00 UTC: Instagram carousel post.
15:00 UTC: Instagram post #2. Mid-day social check.
17:00 UTC: Email open rate check at T+5h. TikTok views check.
19:00 UTC: Etsy orders mid-day check.
20:00 UTC: Collect all 7 KPIs for T+12h checkpoint.
21:00 UTC: T+12H CHECKPOINT (7 KPIs → GREEN / YELLOW / RED decision).
          Log in WORKLOG.md. Send Discord update. Sleep.

May 31, 05:00 UTC: Overnight check. Resume monitoring.
June 1, 20:00 UTC: T+38H PHASE GATE (PASS / AT RISK / FAIL decision).
```

---

*Prepared: 2026-05-09. This is the consolidated launch-day execution document. References: `TRACK_B_LAUNCH_DAY_OPERATIONS_GUIDE.md` (checkpoint KPI definitions), `phase-2-launch-day-checklist.md` (platform verification detail), `phase-2-automation-contingency-playbook.md` (failure mode responses), `phase-2-email-automation-sequence.md` (broadcast and automation specs).*
