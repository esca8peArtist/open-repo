---
title: "Phase 2 Launch Day Checklist — May 30"
subtitle: "Minute-by-minute checklist: what gets pressed when, in sequence"
date: 2026-05-06
status: production-ready
launch-date: 2026-05-30
references:
  - may-30-launch-sequence.md
  - phase-2-tool-integration-map.md
  - phase-2-pre-launch-checklist.md
---

# Phase 2 Launch Day Checklist
## May 30, 2026

**How to use this document**: Open at 7:45am on May 30. Work through each block in order. Check every box before moving to the next block. Do not skip ahead. Each block has a "Done signal" — a specific confirmed state that tells you the block is complete.

**Stagger rationale**:
- Etsy 10am: Etsy's search algorithm registers listing changes 2 hours before email traffic arrives. Organic buyers in the 10am-12pm window are the highest-quality conversion signal.
- Email 12pm: reaches subscribers who already know Seedwarden. Drives a controlled, high-intent traffic spike.
- Social 2pm-3:30pm: reaches the coldest audience last. Staggered by platform to extend the launch-day content footprint and avoid same-audience reach overlap within one day.

---

## 7:45am — Device Setup (15 min)

Open all monitoring tabs before QA begins. You are not checking anything yet — just loading tabs so they are ready.

| Tab | What to Open |
|---|---|
| Tab 1 | Etsy Shop Manager > Stats > Today |
| Tab 2 | Etsy public store URL (incognito, logged out) |
| Tab 3 | Kit > Broadcasts |
| Tab 4 | Kit > Automations |
| Tab 5 | Kit > Subscribers (to see live count) |
| Tab 6 | Buffer (or Later) queue view |
| Phone | Etsy Seller app open in background (push notifications for new orders) |

---

## 8:00am — Final QA Block (60 min total)

Block this time. Do not start other tasks. This QA window eliminates 90% of recoverable launch-day errors before any traffic hits.

### Etsy Verification (20 min)

Open Etsy Shop Manager > Listings.

- [ ] All 21 listings show "Active" status (green dot). Any listing showing "Draft" is invisible in search — click Publish immediately.
- [ ] Click into 5 listings at random. In the Photos section, confirm 5 images are present and in order (Slots 1-3 are mockups; Slots 4 and 5 are lifestyle images).
- [ ] Open 3 of the highest-traffic listings in Tab 2 (public incognito browser). Confirm lifestyle images appear in the listing gallery.
- [ ] Etsy Shop Manager > Marketing > Sales and Coupons. Confirm SEEDWARDEN15 coupon shows "Active" status with 15% discount. If missing or expired: recreate now (15% off, no minimum, no expiry — 3 minutes).

**Done signal**: All 21 listings active with 5 images each. SEEDWARDEN15 coupon confirmed active. No listing errors visible in public browser.

**If issues found**:
- Missing image on a listing: Etsy > Edit Listing > Photos > upload takes 2 minutes
- Listing in Draft: click "Publish" takes 30 seconds
- Invalid coupon: Marketing > Create Discount > code SEEDWARDEN15 > 15% > no minimum > no expiry takes 3 minutes

---

### Kit Verification (20 min)

Open Kit dashboard.

- [ ] Kit > Broadcasts. Find the launch broadcast. Confirm status reads "Scheduled" and the time reads "12:00pm May 30 [year]." Not "Draft." Not "Pending." "Scheduled."
  - If status shows "Draft": click into the broadcast > click Schedule > enter 12:00pm today > confirm. This takes 30 seconds.
- [ ] Kit > Automations. Find "Seedwarden Welcome." Confirm status reads "Published" (not Draft, not Paused). If paused: click Resume.
- [ ] Open the Kit landing page in an incognito browser window. Fill in: first name "Test," a disposable test email address (wanka95+launchday@gmail.com), and Zone 5. Click "Send My Zone Card."
- [ ] Wait up to 60 seconds. Confirm Email 1 arrives at the test address. Open the zone card download button. Confirm a Zone 5 PDF downloads (not a viewer page, not a "request access" error).
- [ ] Record the current subscriber count: Kit > Subscribers. Write it in customer-analytics.csv > "Pre-Launch Subscriber Count" field.

**Done signal**: Broadcast shows "Scheduled" at 12:00pm today. Automation shows "Published." Zone 5 landing page test download works. Subscriber count logged.

**If broadcast is missing**: Kit > Broadcasts > New Broadcast. Subject: "Phase 2 is live — your zone card library just doubled." Paste body from marketing/email-and-launch-plan.md > Launch Broadcast section. Send to "All Confirmed Subscribers." Schedule for today 12:00pm. Takes 10 minutes.

**If zone card download fails**: Diagnose in order: (1) Is the Google Drive link format correct in Kit Email 1 Zone 5? Must be `?export=download&id=` format. (2) Is Drive sharing permission still "Anyone with the link"? (3) Is the Kit automation still published? Fix whichever step is broken — 5 minutes per item.

---

### Social Media Verification (10 min)

Open Buffer or Later queue view.

- [ ] Find the Instagram launch post. Status shows "Scheduled" at 2:00pm today. Click Preview — image shows correctly, caption is complete.
- [ ] Find the TikTok launch post. Status shows "Scheduled" at 2:00pm today. File is a video (not a static image — TikTok suppresses static image posts in the algorithm).
- [ ] Find the Pinterest launch pins. Status shows "Scheduled" at 3:30pm today.
- [ ] Open Buffer > Settings > Connected Accounts. All three platforms (Instagram, TikTok, Pinterest) show green/active status. No "Reconnect" or error warning visible.

**Done signal**: All three platforms show "Scheduled" status with correct times. No connection errors.

**If a post is missing**: Open phase-2-social-content-calendar-60day.md Day 30. Copy the caption and hashtags. Upload the corresponding image from /marketing/lifestyle-photos/etsy-ready/. Schedule for 2:00pm (Instagram/TikTok) or 3:30pm (Pinterest). Takes 5 minutes per platform.

**If Buffer shows "Reconnect" for any platform**: Click "Reconnect," authorize the account again, confirm the scheduled posts are still in the queue after reconnection. Takes 2 minutes per platform.

---

### Zone Card Delivery Final Check (10 min)

- [ ] Open all 8 Google Drive zone card download URLs in 8 incognito tabs. Confirm each downloads a PDF. Do not accept a viewer page — it must download.
- [ ] Spot-check the zone number in each downloaded PDF (check the header band text matches the expected zone number).
- [ ] If any URL returns "Request access": go to Google Drive, find the file, set sharing to "Anyone with the link can view," copy the updated URL (use ?export=download&id= format), paste into Kit Email 1 [zone] variant. Resave Kit email. Takes 5 minutes per affected zone.

**Done signal**: All 8 zone card PDFs accessible as downloads from incognito.

---

## 9:00am — Pre-Launch Communications (55 min)

### Record Baseline Metrics (15 min)

Record in customer-analytics.csv before any traffic changes occur. These are the "before" state numbers. Every metric measured after 10:00am is Phase 2 attributable.

| Metric | Where | Record Here |
|---|---|---|
| Etsy shop views (last 7 days) | Etsy Shop Manager > Stats | |
| Etsy total orders (all time) | Etsy Shop Manager > Stats | |
| Kit subscriber count | Kit dashboard > Subscribers | |
| Instagram followers | Instagram profile | |
| TikTok followers | TikTok profile | |
| Pinterest monthly viewers | Pinterest Analytics | |

---

### Personal Prep (30 min)

Protect this window. Do not start new tasks. Do not open email. Be available to respond immediately to any issue that surfaces in the launch sequence.

Confirm:
- [ ] You have access to your Etsy Shop Manager account (can log in)
- [ ] You have access to Kit dashboard (can log in)
- [ ] You can access Gmail (wanka95@gmail.com) on your phone for real-time monitoring
- [ ] You have the Etsy Seller app open and push notifications enabled
- [ ] launch-day-script.md is open in a tab for extended troubleshooting reference

---

## 10:00am — Phase 1: Etsy Launch

- [ ] Navigate to your Etsy store's public URL in Tab 2 (logged out, incognito browser — the URL that buyers see, not Shop Manager).
- [ ] Scroll through the listed products. Confirm lifestyle images are visible in listing thumbnails (Slot 1 determines the thumbnail — if thumbnails still show mockups, the lifestyle image upload has not yet been processed or the first slot was not lifestyle images, which is correct by design — mockups stay in slots 1-3).
- [ ] Click into 3 listings and confirm all 5 images are visible in the gallery, including slots 4 and 5 (lifestyle flat-lay and contextual).

This is the de facto launch moment. The listing images are already uploaded — confirming they are visible constitutes the Etsy launch. Etsy's algorithm begins processing the updated listings from this moment.

### Monitor 10:00am–12:00pm

Check every 30 minutes:

| Metric | Where | What to Look For |
|---|---|---|
| Etsy shop views today | Shop Manager > Stats > Today | Any organic traffic is a positive signal |
| New Etsy orders | Shop Manager > Orders | A pre-email organic order = highest-quality buyer |
| Listing errors | Public browser | All listings visible, none showing "no longer available" |

Log any organic views in WORKLOG.md. These represent buyers who found the store without any email or social push — they are the highest-quality conversion signal for Phase 2.

**Etsy Success Criteria by 12:00pm**:
- [ ] All 21 listings visible in public search with lifestyle images in slots 4-5
- [ ] Zero listing errors or Draft status
- [ ] SEEDWARDEN15 coupon confirmed active
- [ ] Any pre-email organic orders noted in customer-analytics.csv

---

## 12:00pm — Phase 2: Email Broadcast

At 12:05pm: open Tab 3 (Kit > Broadcasts). Confirm the launch broadcast status has changed to "Sent" or "Sending."

- [ ] Status reads "Sent" or "Sending" by 12:10pm. This is normal — Kit processes the send queue.

**If status still reads "Scheduled" at 12:20pm**: Kit is processing. Wait until 12:25pm. If still "Scheduled" at 12:25pm: click into the broadcast > click "Send Now." This overrides the schedule without changing the email.

**If broadcast is missing entirely at 12:00pm**: Kit > Broadcasts > New Broadcast. Subject: "Phase 2 is live — your zone card library just doubled." Body: marketing/email-and-launch-plan.md > Launch Broadcast. Send to "All Confirmed Subscribers." Send immediately. Takes 5 minutes.

### Monitor 12:00pm–2:00pm

Check at 12:30pm, 1:00pm, and 2:00pm:

| Metric | Where | Target by 2pm |
|---|---|---|
| Broadcast delivery rate | Kit > Broadcasts > Stats | >90% delivered |
| Broadcast open rate | Kit > Broadcasts > Stats | >35% (note: Apple Mail Privacy Protection inflates open rates) |
| Broadcast click rate | Kit > Broadcasts > Stats | >10% |
| Bounce rate | Kit > Broadcasts > Stats | <2% |
| New Etsy orders (email-attributed) | Shop Manager > Orders | Any order after 12pm = email-driven |
| Kit new subscribers (day total) | Kit > Subscribers | Growing from pre-launch baseline |

**Do NOT suppress the welcome automation during the broadcast send.** New subscribers who sign up on launch day (from social traffic or organic) should receive the welcome sequence immediately, not the broadcast. Both automations run simultaneously for different audiences. This is correct behavior.

**Email Phase Success Criteria by 2:00pm**:
- [ ] Delivery rate >90% (if below 80%: check Kit delivery log for bounce reasons)
- [ ] Open rate >35% (check at 4 hours post-send; initial rate will climb throughout the day)
- [ ] Click rate >8%
- [ ] Bounce rate <2%

---

## 2:00pm — Phase 3: Social Media

At 2:15pm: open Buffer or Later queue view.

- [ ] Instagram post: status shows "Published" by 2:15pm. Navigate to the Seedwarden Instagram profile and confirm the launch post is visible at the top of the feed.
- [ ] TikTok post: status shows "Published" by 2:15pm. Navigate to TikTok profile and confirm the video is visible and playing.

**If Buffer fails to post to Instagram by 2:20pm**: Log into Instagram directly. Create a new post. Copy the caption from phase-2-social-content-calendar-60day.md Day 30 (Instagram launch). Upload the lifestyle image from /marketing/lifestyle-photos/etsy-ready/. Post immediately. Takes 3 minutes.

**If Buffer fails to post to TikTok by 2:20pm**: Log into TikTok directly. Upload the 9:16 vertical video. Copy the caption from Day 30 (TikTok variant). Post. Takes 5 minutes.

### Monitor 2:00pm–3:30pm

| Metric | Where | Target |
|---|---|---|
| Instagram impressions | Instagram Insights | >50 by 4pm |
| Instagram profile visits | Instagram Insights | >20 by 4pm |
| TikTok views | TikTok Analytics | >50 by 4pm |
| New Kit sign-ups from social | Kit > Subscribers | Any new sign-ups = social is driving traffic |

---

## 3:30pm — Pinterest Pins

- [ ] Check Buffer queue: Pinterest pins should show "Published" by 3:45pm.
- [ ] Navigate to Pinterest profile: confirm pins are visible in the profile feed.

Pinterest indexes new pins within 2-24 hours. Day 1 Pinterest impressions are lower than Instagram and TikTok — do not calibrate expectations from Day 1 Pinterest data. Pins compound over days and weeks, not hours.

---

## End of Day: 7:00pm–9:00pm — Wrap

### Final Metric Log (15 min)

Record in customer-analytics.csv:

| Metric | Source | Value |
|---|---|---|
| Etsy shop views today | Shop Manager > Stats | |
| New Etsy orders today | Shop Manager > Orders | |
| Kit subscriber count (end of day) | Kit > Subscribers | |
| Net new subscribers today (EOD minus pre-launch baseline) | Calculated | |
| Kit broadcast open rate | Kit > Broadcasts > Stats | |
| Kit broadcast click rate | Kit > Broadcasts > Stats | |
| Instagram impressions | Instagram Insights | |
| TikTok views | TikTok Analytics | |
| Net new social followers (Instagram) | Instagram profile | |
| Net new social followers (TikTok) | TikTok profile | |

Record in WORKLOG.md: any anomalies, technical issues encountered, manual interventions made.

---

### Response Handling

If any buyers message the Etsy shop or reply to the launch email: respond within 4 hours. Templates for three common buyer questions are in launch-day-script.md (T+24h section).

---

### Week 1 Monitoring Schedule

Do not check metrics continuously after Day 1 — anxiety without insight. Stick to this cadence:

| Day | When | What to Check |
|---|---|---|
| May 31 (Day 2) | Evening | Kit Email 1 open rate + click rate; any new orders |
| June 1 (Day 3) | Evening | Kit Email 1 delivery complete for all subscribers; Etsy traffic trend |
| June 3 (Day 5) | Evening | Email 3 open rate (40%+ target); behavioral tag count |
| June 6 (Day 7) | Morning | Full Week 1 review — see phase-2-week-1-success-metrics.md |

---

## Quick-Reference Recovery Procedures

**Etsy listing error (under review or removed)**: Identify listing in Shop Manager. Check for policy violation note. If Draft: publish. If under review: do not recreate — email Etsy support and launch with 20 active listings.

**Kit broadcast not sent**: Kit > Broadcasts > find broadcast > click "Send Now." Takes 30 seconds.

**Kit automation paused or stopped**: Kit > Automations > find "Seedwarden Welcome" > click Resume. Takes 5 seconds.

**Zone card download link broken**: Kit > Sequences > Email 1 > [zone variant] > find download button > update link to ?export=download&id= Google Drive URL. Re-test from incognito. Takes 5 minutes.

**Buffer fails all social posts**: Log into each platform directly. Post manually using captions and images from phase-2-social-content-calendar-60day.md Day 30. Total manual time: 15-20 minutes.

**Bounce rate above 5%**: Kit > Broadcasts > Stats > check "Bounced" tab for specific addresses. If a specific domain is bouncing (e.g., all AOL addresses): deliverability issue with that provider. Kit's SendGrid infrastructure handles most cases automatically — if bounce rate stabilizes below 5% within 2 hours, no action required. If rate climbs: pause the broadcast if still in queue.

---

*Generated: 2026-05-06. References: may-30-launch-sequence.md (full narrative), phase-2-tool-integration-map.md (verification steps), phase-2-launch-control-center.md (decision gates). This checklist distills the full launch sequence into a 30-minute press-by-press execution guide.*
