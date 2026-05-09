---
title: "Phase 2 Launch Day Checklist — May 30, 2026"
subtitle: "Hour-by-hour timeline with 6 user-only checkpoints, automated alerts, and rollback procedures"
date: 2026-05-09
status: production-ready
launch-date: 2026-05-30
source: projects/seedwarden/phase-2-launch-day-checklist.md and phase-2-launch-day-master-checklist.md (root-level canonicals)
references:
  - may-30-launch-sequence.md
  - phase-2-tool-integration-map.md
  - phase-2-automation-contingency-playbook.md (this docs folder)
---

# Phase 2 Launch Day Checklist
## May 30, 2026 — Hour-by-Hour Timeline

**How to use this document**: Open at 6:00am on May 30. Work through each block in sequence. Check every box before moving forward. Each block has a "Done signal" — a specific confirmed state that tells you the block is complete.

**The 6 user-only checkpoints** (the moments that require your judgment, not automation):
- T+0h (6:00am) — System verification before any traffic
- T+6h (12:00pm) — Email broadcast sent, assess delivery metrics
- T+12h (6:00pm) — First traffic wave assessment; go/no-go for social amplification
- T+24h (May 31, 6:00am) — Day 2 open, confirm overnight activity
- T+38h (May 31, 8:00pm) — Full first-cycle assessment; Phase 3 pre-gate
- T+48h (June 1, 6:00am) — Day 3 open, confirm Week 1 trajectory

**Stagger rationale**: Etsy 10:00am — Etsy's algorithm registers listing changes 2 hours before email traffic arrives. Organic buyers from 10am–12pm are the highest-quality conversion signal. Email 12:00pm — reaches subscribers who already know Seedwarden; a controlled, high-intent spike. Social 2:00–3:30pm — reaches the coldest audience last; staggered by platform to extend the content footprint and avoid same-audience reach overlap within one day.

---

## CHECKPOINT T+0h: 6:00am — Device Setup and Pre-Launch Verification

Open all monitoring tabs before QA begins. You are not checking anything yet — just loading tabs so they are ready.

| Tab | What to open |
|---|---|
| Tab 1 | Etsy Shop Manager > Stats > Today |
| Tab 2 | Etsy public store URL (incognito, logged out) — the URL buyers see |
| Tab 3 | Kit > Broadcasts |
| Tab 4 | Kit > Automations |
| Tab 5 | Kit > Subscribers (to see live count) |
| Tab 6 | Buffer (or Later) queue view |
| Phone | Etsy Seller app, push notifications enabled |

---

## 7:00am — Pre-Launch System Verification (60 min)

Block this time. Do not start other tasks. This QA window eliminates 90% of recoverable launch-day errors before any traffic hits.

### Etsy Verification (20 min)

- [ ] Etsy Shop Manager > Listings. All 21 listings show "Active" status (green dot). Any listing showing "Draft" is invisible in search — click Publish immediately.
- [ ] Click into 5 listings at random. In the Photos section, confirm 5 images are present and in order (Slots 1–3 are mockups; Slots 4–5 are lifestyle images).
- [ ] Open 3 highest-traffic listings in Tab 2 (public incognito). Confirm lifestyle images appear in the listing gallery.
- [ ] Etsy Shop Manager > Marketing > Sales and Coupons. Confirm SEEDWARDEN15 coupon shows "Active" status with 15% discount, no minimum, no expiry.

**Done signal**: All 21 listings active with 5 images each. SEEDWARDEN15 coupon confirmed active. No errors in public browser.

**If issues found**:
- Missing image: Etsy > Edit Listing > Photos > upload. 2 minutes.
- Listing in Draft: click "Publish." 30 seconds.
- Invalid coupon: Marketing > Create Discount > code SEEDWARDEN15 > 15% > no minimum > no expiry. 3 minutes.

---

### Kit Verification (20 min)

- [ ] Kit > Broadcasts. Find the launch broadcast. Status reads "Scheduled" with time showing "12:00pm May 30." Not "Draft." Not "Pending." "Scheduled."
  - If "Draft": click into broadcast > Schedule > 12:00pm today > confirm. 30 seconds.
- [ ] Kit > Automations. Find "Seedwarden Welcome." Status reads "Published" (not Draft, not Paused). If paused: click Resume.
- [ ] Open the Kit landing page in incognito. Fill in: name "Test," email wanka95+launchday@gmail.com, Zone 5. Click "Send My Zone Card."
- [ ] Wait up to 60 seconds. Confirm Email 1 arrives at wanka95+launchday@gmail.com. Open the zone card download button. Confirm a Zone 5 PDF downloads — not a viewer page, not a "request access" error.
- [ ] Record current subscriber count: Kit > Subscribers. Write it in customer-analytics.csv > "Pre-Launch Subscriber Count."

**Done signal**: Broadcast shows "Scheduled" at 12:00pm. Automation shows "Published." Zone 5 landing page test download works. Subscriber count logged.

**If broadcast is missing**: Kit > Broadcasts > New Broadcast. Subject: "Phase 2 is live — your zone card library just doubled." Paste body from marketing/email-and-launch-plan.md > Launch Broadcast. Send to "All Confirmed Subscribers." Schedule for today 12:00pm. 10 minutes.

**If zone card download fails**: Diagnose in order: (1) Is the Google Drive link in `?export=download&id=` format? (2) Is Drive sharing set to "Anyone with the link"? (3) Is the Kit automation still published? Fix whichever step is broken — 5 minutes per item.

---

### Social Media Verification (10 min)

- [ ] Buffer > queue view. Instagram launch post: status shows "Scheduled" at 2:00pm today. Preview — image correct, caption complete.
- [ ] TikTok launch post: status shows "Scheduled" at 2:00pm today. File is a video file (not a static image — TikTok suppresses static image posts).
- [ ] Pinterest launch pins: status shows "Scheduled" at 3:30pm today.
- [ ] Buffer > Settings > Connected Accounts. All three platforms show green/active status. No "Reconnect" warning.

**Done signal**: All three platforms show "Scheduled" status with correct times. No connection errors.

**If a post is missing**: Open `docs/phase-2-operations/phase-2-social-posting-scheduler.csv` > June 1 block. Copy the caption and hashtags. Upload the corresponding image from /marketing/lifestyle-photos/etsy-ready/. Schedule for 2:00pm (Instagram/TikTok) or 3:30pm (Pinterest). 5 minutes per platform.

**If Buffer shows "Reconnect"**: Click Reconnect, authorize the account, confirm scheduled posts are still in queue. 2 minutes per platform.

---

### Zone Card Delivery Final Check (10 min)

- [ ] Open all 8 Google Drive zone card download URLs in 8 incognito tabs. Confirm each downloads a PDF — not a viewer page.
- [ ] Spot-check the zone number in each downloaded PDF (header band text matches expected zone).
- [ ] If any URL returns "Request access": Google Drive > find file > set sharing to "Anyone with the link can view" > copy URL in `?export=download&id=` format > paste into Kit Email 1 [zone] variant > resave. 5 minutes per affected zone.

**Done signal**: All 8 zone card PDFs accessible as downloads from incognito.

---

## 8:30am — Record Baseline Metrics

Record in customer-analytics.csv before any traffic changes occur. Everything measured after 10:00am is Phase 2 attributable.

| Metric | Source | Record |
|---|---|---|
| Etsy shop views (last 7 days) | Shop Manager > Stats | |
| Etsy total orders (all time) | Shop Manager > Stats | |
| Kit subscriber count | Kit > Subscribers | |
| Instagram followers | Instagram profile | |
| TikTok followers | TikTok profile | |
| Pinterest monthly viewers | Pinterest Analytics | |

---

## 9:00am — Personal Prep (55 min)

Protect this window. Do not open email. Do not start new tasks. Be available to respond immediately to any issue in the launch sequence.

- [ ] You can log into Etsy Shop Manager
- [ ] You can log into Kit dashboard
- [ ] Gmail is accessible on your phone for real-time monitoring
- [ ] Etsy Seller app is open with push notifications enabled
- [ ] `docs/phase-2-operations/phase-2-contingency-playbook.md` is open in a tab for troubleshooting reference

---

## CHECKPOINT T+6h: 10:00am — Phase 1 Etsy Launch

- [ ] Navigate to your Etsy store's public URL in Tab 2 (logged out, incognito). Scroll through the listed products. Confirm lifestyle images are visible in listing thumbnails.
- [ ] Click into 3 listings. Confirm all 5 images are visible in the gallery including slots 4 and 5.

This is the de facto launch moment. The listing images are already uploaded — confirming they are visible constitutes the Etsy launch. Etsy's algorithm begins processing updated listings from this moment.

### Monitor 10:00am–12:00pm (check every 30 minutes)

| Metric | Source | Signal |
|---|---|---|
| Etsy shop views today | Shop Manager > Stats > Today | Any organic traffic is a positive signal |
| New Etsy orders | Shop Manager > Orders | Pre-email organic order = highest-quality buyer signal |
| Listing errors | Public browser | All listings visible, none showing "no longer available" |

Log any organic views in WORKLOG.md — these are buyers who found the store without email or social push.

**Etsy success criteria by 12:00pm**:
- [ ] All 21 listings visible in public search with lifestyle images in slots 4–5
- [ ] Zero listing errors or Draft status
- [ ] SEEDWARDEN15 coupon confirmed active

---

## CHECKPOINT T+6h: 12:00pm — Phase 2 Email Broadcast

At 12:05pm: Kit > Broadcasts. Confirm launch broadcast status changed to "Sent" or "Sending."

- [ ] Status reads "Sent" or "Sending" by 12:10pm.

**If status still reads "Scheduled" at 12:20pm**: Kit is processing. Wait until 12:25pm. If still "Scheduled" at 12:25pm: click into the broadcast > "Send Now." Overrides schedule without changing the email.

**If broadcast is missing at 12:00pm**: Kit > Broadcasts > New Broadcast > paste body from marketing/email-and-launch-plan.md > Send to "All Confirmed Subscribers" > Send Now. 5 minutes.

### Monitor 12:00pm–2:00pm (check at 12:30pm, 1:00pm, 2:00pm)

| Metric | Source | Target by 2pm |
|---|---|---|
| Broadcast delivery rate | Kit > Broadcasts > Stats | Above 90% delivered |
| Broadcast open rate | Kit > Broadcasts > Stats | Above 35% (note: Apple Mail Privacy Protection inflates open rates) |
| Broadcast click rate | Kit > Broadcasts > Stats | Above 10% |
| Bounce rate | Kit > Broadcasts > Stats | Below 2% |
| New Etsy orders after 12pm | Shop Manager > Orders | Any order = email-driven |
| New Kit subscribers | Kit > Subscribers | Growing from pre-launch baseline |

**Do NOT suppress the welcome automation during the broadcast send.** New subscribers who sign up on launch day from social traffic should receive the welcome sequence immediately. Both automations run simultaneously for different audiences. This is correct behavior.

**Email success criteria by 2:00pm**:
- [ ] Delivery rate above 90%
- [ ] Open rate above 35% (4-hour open rate will continue climbing through the day)
- [ ] Click rate above 8%
- [ ] Bounce rate below 2%

---

## CHECKPOINT T+12h: 2:00pm — Phase 3 Social Media

At 2:15pm: Buffer > queue view.

- [ ] Instagram post: status shows "Published" by 2:15pm. Navigate to Seedwarden Instagram profile — launch post visible at the top of the feed.
- [ ] TikTok post: status shows "Published" by 2:15pm. Navigate to TikTok profile — video visible and playing.

**If Buffer fails to post to Instagram by 2:20pm**: Log into Instagram directly. Create a new post. Copy caption from `phase-2-social-posting-scheduler.csv` > May 30 Instagram Launch. Upload the lifestyle image from /marketing/lifestyle-photos/etsy-ready/. Post immediately. 3 minutes.

**If Buffer fails to post to TikTok by 2:20pm**: Log into TikTok directly. Upload the 9:16 vertical video. Copy caption from May 30 TikTok entry. Post. 5 minutes.

### Monitor 2:00pm–3:30pm

| Metric | Source | Target |
|---|---|---|
| Instagram impressions | Instagram Insights | Above 50 by 4pm |
| Instagram profile visits | Instagram Insights | Above 20 by 4pm |
| TikTok views | TikTok Analytics | Above 50 by 4pm |
| New Kit sign-ups | Kit > Subscribers | Any new sign-ups = social is driving traffic |

---

## 3:30pm — Pinterest Pins

- [ ] Buffer queue: Pinterest pins should show "Published" by 3:45pm.
- [ ] Pinterest profile: confirm pins are visible in the profile feed.

Pinterest indexes new pins within 2–24 hours. Day 1 Pinterest impressions will be lower than Instagram and TikTok — this is expected. Pins compound over days and weeks, not hours.

---

## 7:00pm–9:00pm — Day 1 Wrap

### Final Metric Log (15 min)

Record in customer-analytics.csv:

| Metric | Source | Value |
|---|---|---|
| Etsy shop views today | Shop Manager > Stats | |
| New Etsy orders today | Shop Manager > Orders | |
| Kit subscriber count (end of day) | Kit > Subscribers | |
| Net new subscribers today | Calculated: EOD minus pre-launch baseline | |
| Kit broadcast open rate | Kit > Broadcasts > Stats | |
| Kit broadcast click rate | Kit > Broadcasts > Stats | |
| Instagram impressions | Instagram Insights | |
| TikTok views | TikTok Analytics | |
| Net new Instagram followers | Instagram profile | |
| Net new TikTok followers | TikTok profile | |

Record in WORKLOG.md: any anomalies, technical issues encountered, manual interventions made.

### Response Handling

If any buyers message the Etsy shop or reply to the launch email: respond within 4 hours. Templates for three common buyer questions are in `launch-day-script.md` (T+24h section).

---

## CHECKPOINT T+24h: May 31, 6:00am — Day 2 Open

Check in 10 minutes:
- [ ] Kit > Automations. Welcome sequence still shows "Published." Any paused state: click Resume.
- [ ] Kit > Subscribers. Night sign-ups from Asia/European time zones may have trickled in — note count.
- [ ] Etsy > Orders. Any overnight orders? Note and confirm automatic digital delivery processed.
- [ ] Buffer queue: confirm today's scheduled posts (May 31 IG story + TikTok educational video) show "Scheduled."

**Red flags to escalate immediately**:
- Kit automation shows "Paused": Resume and check if any subscriber received Email 1 then stopped receiving subsequent emails.
- Etsy order showing "Payment Pending" for more than 4 hours: contact Etsy seller support.
- Bounce rate on Kit has climbed above 2%: go to `docs/phase-2-operations/phase-2-contingency-playbook.md` Scenario 3.

---

## Week 1 Monitoring Schedule

Do not check metrics continuously after Day 1. Stick to this cadence:

| Day | When | What to check |
|---|---|---|
| May 31 (Day 2) | Evening | Kit Email 1 open rate and click rate; any new orders |
| June 1 (Day 3) | Evening | Kit Email 1 delivery complete for all subscribers; Etsy traffic trend |
| June 3 (Day 5) | Evening | Email 3 open rate (target 40%+); behavioral tag count |
| June 5 (Day 7) | Morning | Full Week 1 review — see `phase-2-week-1-success-metrics.md` |

---

## CHECKPOINT T+38h: May 31, 8:00pm — First Cycle Assessment

Structured 30-minute assessment. This is the first major decision point after launch.

### 7-Metric Green / Yellow / Red Framework

| Metric | Green | Yellow | Red |
|---|---|---|---|
| Total Etsy orders | 10+ | 5–9 | Under 5 |
| Kit sign-ups | 20+ | 12–19 | Under 12 |
| Email open rate | Above 35% | 20–35% | Under 20% |
| Email click rate | Above 8% | 5–8% | Under 5% |
| Hard bounce rate | Under 0.5% | 0.5–1% | Above 1% |
| Social sign-ups from bio link | Any | — | Zero (bio link broken) |
| Etsy listing visibility | All 21 active | Any errors recoverable | Any listing removed |

**If 5+ metrics are GREEN**: proceed with Week 1 operations on current plan.
**If 2–4 metrics are YELLOW**: identify lowest-performing channel and execute the relevant contingency procedure from this docs folder before June 3.
**If any metric is RED**: execute the relevant contingency procedure immediately. Do not wait.

---

## CHECKPOINT T+48h: June 1, 6:00am — Day 3 Open

- [ ] Kit > Automations > confirm "Seedwarden Welcome" still Published.
- [ ] Check Email 2 (Day 2 email in welcome sequence) open rate for May 30 sign-ups. Target: 40%+.
- [ ] Etsy > Stats > Today. Confirm organic traffic continues in absence of email push (post-broadcast baseline behavior).
- [ ] Check SEEDWARDEN15 "Times Used" count in Etsy > Marketing > Coupons. Log in WORKLOG.md.
- [ ] Confirm social posts scheduled for June 1 are queued in Buffer (Pinterest educational pin 8:00pm, Instagram single image 10:00am, TikTok video 6:00pm).

---

## Automated Alerts

### Discord Webhook (set up before May 30 if Discord is in use)

1. Discord > Server Settings > Integrations > Webhooks > Create Webhook.
2. Copy the webhook URL.
3. In Etsy: there is no native Discord integration. Use a Zapier free-tier flow: Trigger = Etsy New Order > Action = Post message to Discord webhook. Message format: "New Etsy order: [order number] — [product name] — $[amount]."
4. This gives a real-time Discord notification for every Etsy order without checking Shop Manager manually.

### Etsy Push Notifications

1. Etsy Seller app > Settings > Notifications.
2. Enable: New Order, New Message, Listing Sold Out (if quantities are used).
3. Keep phone volume on during May 30 and May 31.

### Email Alerts from Kit

1. Kit > Settings > Notifications > enable email notifications for: New Subscriber, Automation Error, Broadcast Send Complete.
2. These arrive in wanka95@gmail.com. During launch day, check Gmail every 30 minutes.

---

## Rollback Procedures

| Issue | Rollback action |
|---|---|
| Etsy listing under review or removed | Do not recreate. Email Etsy support. Launch with 20 active listings. |
| Kit broadcast not sent | Kit > Broadcasts > find broadcast > "Send Now." 30 seconds. |
| Kit automation paused | Kit > Automations > "Seedwarden Welcome" > Resume. 5 seconds. |
| Zone card download link broken | Kit > Sequences > Email 1 > [zone variant] > update link to `?export=download&id=` format. Re-test from incognito. 5 minutes. |
| Buffer fails all social posts | Log into each platform directly. Post manually using captions from `phase-2-social-posting-scheduler.csv`. 15–20 minutes total. |
| Bounce rate above 5% | Stop sending. Kit > Broadcasts > Stats > Bounced tab. Review domain pattern. Contact Kit support. |
| Instagram or TikTok account locked | See `docs/phase-2-operations/phase-2-contingency-playbook.md` Scenario 4. Shift content to other 2 platforms immediately. |
| All Buffer social posts fail (API issue) | Post manually to Instagram, TikTok, and Pinterest directly from platform apps. Captions in the social scheduler CSV. |

---

## Quick Reference: Where to Find Everything

| Task | Location |
|---|---|
| Email copy for all 5 welcome emails | marketing/email-and-launch-plan.md |
| Launch broadcast copy | marketing/email-and-launch-plan.md > Launch Broadcast |
| Social post captions (June 1–30) | docs/phase-2-operations/phase-2-social-posting-scheduler.csv |
| Email automation spec | docs/phase-2-operations/phase-2-email-automation-sequence.md |
| Contingency scenarios | docs/phase-2-operations/phase-2-contingency-playbook.md |
| Analytics dashboard | docs/phase-2-operations/phase-2-launch-analytics-dashboard-template.xlsx |
| Week 1 success metrics | phase-2-week-1-success-metrics.md |
| Launch narrative script | launch-day-script.md |

---

*Status: production-ready. Six user checkpoints: T+0h (6am), T+6h (10am and 12pm combined into a dual checkpoint), T+12h (2pm), T+24h (May 31 6am), T+38h (May 31 8pm), T+48h (June 1 6am). Automated alerts: Discord webhook (Etsy orders), Etsy Seller app push (order and message), Kit email notifications. Rollback procedures for 8 failure modes. Execute directly on May 30.*
