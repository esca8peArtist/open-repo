---
title: "May 30 Launch Sequence — Minute-by-Minute Execution Guide"
date: 2026-05-06
status: production-ready
references:
  - launch-day-script.md (detailed action blocks)
  - phase-2-tool-integration-map.md (verification steps)
  - phase-2-pre-launch-checklist.md (7-day QA)
---

# May 30 Launch Sequence
## Minute-by-Minute Execution Guide

**How to use this document**: Open at 8:00am on May 30. Work through each block in sequence. Do not skip ahead. Each block has a "Done signal" — a specific thing you can confirm to know you are ready for the next block.

**Staggered sequence rationale**:
- **Etsy 10am**: Etsy's search algorithm registers listing changes before email traffic arrives. Organic buyers in the 10am-12pm window are the highest-quality signal (converted without any push). 2-hour pre-email window also gives time to fix any listing issues.
- **Email 12pm**: Launch broadcast reaches subscribers who already know Seedwarden. Email drives a controlled traffic spike to listings that are already confirmed live.
- **Social 2pm (Instagram/TikTok), 3:30pm (Pinterest)**: Staggered by platform to avoid reach overlap within one day and to extend the launch-day content footprint. Social goes last because it reaches the coldest audience (non-subscribers).

---

## 8:00am — Final QA Block (60 minutes)

Block this time. Do not skip or compress it. Running this QA eliminates 90% of recoverable launch-day errors.

### Etsy Verification (20 min)

Open Etsy Shop Manager > Listings.

- [ ] Confirm all 21 listings show "Active" status (green). Any listing showing "Draft" is invisible in search — publish it now.
- [ ] Click into 5 listings at random. In the Photos section, confirm 5 images are uploaded and in order (Slots 1-3: mockups, Slot 4: lifestyle flat-lay, Slot 5: contextual in-use).
- [ ] Open 3 of the highest-traffic listings in a public browser window (logged out or incognito). Confirm lifestyle images are visible in the listing gallery.
- [ ] Navigate to Etsy Shop Manager > Marketing > Sales and Coupons. Confirm SEEDWARDEN15 coupon shows "Active" status. If it shows "Expired" or is missing: recreate now (15% off, no minimum, no expiry — takes 3 minutes).

**Done signal**: All 21 listings active with 5 images each, SEEDWARDEN15 coupon confirmed active.

**If you find issues**: Fix them now. You have 2 hours before the broadcast drives traffic. Missing image: upload takes 2 minutes. Inactive listing: click "Publish" takes 30 seconds. Invalid coupon: recreate takes 3 minutes.

---

### Kit Verification (20 min)

Open Kit dashboard.

- [ ] Navigate to Broadcasts. Find the launch broadcast. Confirm status shows "Scheduled" and the scheduled time reads "12:00pm [today's date]." If it shows "Draft": click to open, click Schedule, enter 12:00pm May 30, confirm.
- [ ] Navigate to Automations. Find the "Seedwarden Welcome" automation. Confirm status shows "Published" (not Draft, not Paused). If paused: click Resume.
- [ ] Open the Kit landing page in an incognito browser window. Fill in: a test first name, a disposable test email address (e.g., your email + "+test30"), and Zone 5 in the dropdown. Click "Send My Zone Card."
- [ ] Wait up to 60 seconds. Confirm Email 1 arrives at the test address. Open the zone card download link. Confirm a Zone 5 PDF downloads (not a viewer page, not a "request access" error).
- [ ] Record the current subscriber count: Kit dashboard > Subscribers. Write it in customer-analytics.csv launch row under "Pre-Launch Subscriber Count."

**Done signal**: Broadcast shows "Scheduled," automation shows "Published," Zone 5 test download works.

**If broadcast is missing or wrong time**: Stage it now. Kit > Broadcasts > New Broadcast > "Seedwarden Phase 2 is live" subject > paste launch email copy from `marketing/email-and-launch-plan.md` > Send to "All Confirmed Subscribers" > Schedule for today 12:00pm.

**If zone card download fails**: Diagnose in order: (1) Is the Google Drive link still correct in Kit Email 1 Zone 5? (2) Is the Google Drive sharing permission still "Anyone with the link"? (3) Is the URL using the `?export=download&id=` format? Fix whichever is broken — takes 5 minutes.

---

### Social Media Verification (10 min)

Open Buffer or Later.

- [ ] Find the Instagram launch post. Confirm status "Scheduled" at 2:00pm today. Click Preview — confirm the image shows the product correctly (not cropped, not blank).
- [ ] Find the TikTok launch post. Confirm status "Scheduled" at 2:00pm today. Confirm it is a video file (not a static image — TikTok suppresses static image posts in the algorithm).
- [ ] Find the Pinterest launch pins. Confirm status "Scheduled" at 3:30pm today.
- [ ] Navigate to Buffer > Settings > Connected Accounts. Confirm all three platform connections show a green or active status. If any shows "Reconnect" or an error: click to re-authorize now. Takes 2 minutes per platform.

**Done signal**: All three platforms show "Scheduled" status with correct times, no connection errors.

**If a post is missing**: Navigate to the social calendar file (`phase-2-social-content-calendar-60day.md` Day 30). Copy the caption and hashtags. Upload the corresponding image from `marketing/lifestyle-photos/etsy-ready/`. Schedule for 2:00pm (Instagram/TikTok) or 3:30pm (Pinterest).

---

### Zone Card Delivery Final Check (10 min)

- [ ] Open all 8 Google Drive zone card download URLs in 8 incognito tabs. Confirm each downloads a PDF with the correct zone number (spot-check zone number in the PDF title or header).
- [ ] If any URL returns a "request access" page: re-open Google Drive, navigate to the file, confirm sharing is set to "Anyone with the link," copy the updated URL, paste into Kit Email 1 [zone] variant.

**Done signal**: All 8 zone card PDFs accessible from incognito.

---

## 9:00am — Pre-Launch Communications (55 minutes)

### Baseline Metrics Record (15 min)

Record in customer-analytics.csv before any traffic changes:
- Etsy shop views (last 7 days) — from Etsy Shop Manager > Stats
- Etsy total orders (all time) — from Etsy Shop Manager > Stats
- Kit subscriber count (exact number from Kit dashboard)
- Instagram follower count
- TikTok follower count
- Pinterest monthly viewers (Pinterest Analytics)

These are the before-state numbers. Every metric measured after 10:00am is Phase 2 attributable.

### Browser and Device Setup (10 min)

Open all monitoring tabs now so you are not searching during the launch:
- Tab 1: Etsy Shop Manager > Stats > Today (set to refresh)
- Tab 2: Etsy store public view (incognito, logged out)
- Tab 3: Kit > Broadcasts (to verify send status at 12:05pm)
- Tab 4: Kit > Analytics (to monitor opens and clicks)
- Tab 5: Buffer/Later queue view
- Phone: Etsy Seller app open in background for push notifications

### Personal Prep (30 min)

Protect this block. Do not start new tasks. Be available to respond to any issue that surfaces in the T+0 window.

---

## 10:00am — Phase 1 (Etsy)

### Action: Confirm All 21 Listings Are at 5-Image Status in Public View

- Navigate to your Etsy store's public URL (not Shop Manager — the URL that buyers see).
- Scroll through all listings. Each listing's gallery thumbnail in search results shows the primary image (Slot 1). Click into each listing to confirm 5 images are in the gallery.
- Alternatively: In Etsy Shop Manager, confirm the "5 photos" indicator on each listing's thumbnail.

**This is the de facto launch moment**. The listing images are already uploaded — confirming they are visible constitutes launch. Etsy's algorithm begins processing the updated listings from this point.

### What to Monitor: 10:00am to 12:00pm

| Metric | Check Frequency | Where | Target |
|---|---|---|---|
| Etsy shop views (today) | Every 30 min | Shop Manager > Stats > Today | Any organic traffic is a signal |
| Any new Etsy orders | Every 30 min | Shop Manager > Orders | A pre-email organic order = high intent buyer |
| Etsy listing errors | Once at 10:15am | Public browser | All listings visible, no "This listing is no longer available" |

**Note any organic views in WORKLOG.md**: These represent buyers who found the store without any email or social push — they are the highest-quality conversion signal for Phase 2.

### Etsy Success Criteria by 12:00pm

- All 21 listings visible in public search with lifestyle images in slots 4-5.
- Zero listing errors or "draft" status.
- SEEDWARDEN15 coupon active.
- Any pre-email organic orders noted in customer-analytics.csv.

---

## 12:00pm — Phase 2 (Email Broadcast)

### Action at 12:05pm: Verify Broadcast Status

- Navigate to Kit > Broadcasts > [launch broadcast].
- Confirm status shows "Sent" or "Sending."

**If status shows "Scheduled" at 12:10pm**: Kit may be processing a send queue (normal for large lists). Wait.

**If status still shows "Scheduled" at 12:20pm**: Click into the broadcast. Click "Send Now." This overrides the schedule without changing the email.

**If broadcast is missing entirely**: Copy the launch email body from `marketing/email-and-launch-plan.md` Section: Launch Broadcast. Create a new broadcast in Kit. Send to "All Confirmed Subscribers." Send immediately.

### What to Monitor: 12:00pm to 2:00pm

| Metric | Check Frequency | Where | Target by 2pm |
|---|---|---|---|
| Kit broadcast delivery rate | At 12:30pm | Kit > Broadcasts > [broadcast] > Stats | >90% delivered |
| Kit open rate | At 1:00pm and 2:00pm | Kit > Broadcasts > Stats | >35% (note: inflated by Apple MPP) |
| Kit click rate | At 1:00pm and 2:00pm | Kit > Broadcasts > Stats | >10% |
| Bounce rate | At 12:30pm | Kit > Broadcasts > Stats | <2% |
| Etsy views spike | Every 30 min | Shop Manager > Stats > Today | Traffic increase relative to 10am-12pm baseline |
| Any new Etsy orders | Every 30 min | Shop Manager > Orders | Email-attributed purchases |

### Email Phase Success Criteria

| Metric | Target | Action if Below Target |
|---|---|---|
| Delivery rate | >90% by 12:30pm | If below 80%: check Kit's delivery log for bounce reasons. DNS records may need 24-48 hours to propagate if recently updated |
| Bounce rate | <2% | Above 2%: pause broadcast if still in queue, remove hard bounces from list before resuming |
| Open rate (4 hrs post-send) | >35% | Below 20%: subject line issue; note for next broadcast test |
| Click rate (4 hrs post-send) | >8% | Below 5%: CTA button issue; check Kit Preview to confirm buttons rendered on mobile |

### What NOT to Do During Email Phase

Do not suppress the welcome automation during the broadcast send. New subscribers who sign up on launch day (from social posts or organic) should receive the welcome sequence, not the broadcast. This is correct behavior — welcome sequence and broadcast run simultaneously for different audiences.

---

## 2:00pm — Phase 3 (Social Media)

### Action: Confirm Social Posts Sent by 2:15pm

- Check Buffer/Later queue. Instagram and TikTok posts should show "Published" by 2:15pm.
- Navigate to Instagram profile: confirm the launch post is visible at the top of the feed.
- Navigate to TikTok profile: confirm the video is visible and playing.

**If Buffer fails to post to Instagram**: Log into Instagram directly. Create a new post. Copy the caption from `phase-2-social-content-calendar-60day.md` Day 30 (Instagram launch). Upload the lifestyle image from `marketing/lifestyle-photos/etsy-ready/`. Post manually.

**If Buffer fails to post to TikTok**: Log into TikTok directly. Upload the 9:16 video. Copy the caption from the calendar. Post manually.

### Instagram Post Specifications (Day 30 launch)

- Image: top lifestyle flat-lay from `marketing/lifestyle-photos/etsy-ready/` (the strongest Cluster A image, chosen May 22-25)
- Format: 1080×1080px JPEG
- Caption: copy from `phase-2-social-content-calendar-60day.md` Day 30
- Hashtags: included in calendar entry
- CTA in caption: "Zone card link in bio"

### TikTok Post Specifications (Day 30 launch)

- Format: 9:16 vertical video, 1080×1920px
- If no video was filmed: use Canva's video export (Ken Burns animation from lifestyle flat-lay image). Export as MP4.
- Caption: from calendar Day 30, TikTok variant
- Do not use hashtags in the caption body — move them to a comment after posting for cleaner copy

### What to Monitor: 2:00pm to End of Day

| Metric | Check Frequency | Where | Target by End of Day |
|---|---|---|---|
| Instagram impressions | At 4pm and EOD | Instagram Insights | >50 impressions |
| Instagram profile visits | At 4pm and EOD | Instagram Insights | >20 |
| TikTok views | At 4pm and EOD | TikTok Analytics | >50 views |
| Pinterest impressions | At EOD | Pinterest Analytics | >30 impressions |
| Kit landing page sign-ups | At 4pm and EOD | Kit > Subscribers | Any new sign-ups from social |

### 3:30pm — Pinterest Launch Pins

Buffer should post Pinterest pins automatically at 3:30pm.

- Confirm at 3:45pm: navigate to Pinterest profile, confirm pins are visible.
- Pinterest's algorithm indexes new pins within 2-24 hours. Day 1 impressions on Pinterest are lower than Instagram and TikTok — do not calibrate expectations from Pinterest Day 1 data.

### Social Phase Success Criteria (Day 1)

| Platform | Target | Timeframe |
|---|---|---|
| Instagram impressions | >50 | By end of Day 1 |
| Instagram profile clicks | >20 | By end of Day 1 |
| TikTok views | >50 | By end of Day 1 |
| Pinterest impressions | >30 | By end of Day 2 (indexing delay) |
| New email sign-ups from social | >3 | By end of Day 1 |

---

## End of Day Wrap — 7:00pm to 9:00pm

### Metric Log (15 min)

Record in customer-analytics.csv:
- Etsy shop views today
- New Etsy orders (count, not product details)
- Kit subscriber count (compare to pre-launch baseline)
- Kit broadcast open rate and click rate
- Instagram impressions (from Insights)
- TikTok views
- New social followers (Instagram, TikTok, Pinterest vs. pre-launch)

**Note in WORKLOG.md**: Any anomalies, technical issues encountered, manual interventions made.

### Response Handling

If any buyers message the Etsy shop or reply to the launch email: respond within 4 hours. Templates for three common buyer questions are in `launch-day-script.md` (T+24h section).

### Week 1 Monitoring Schedule

Do not check metrics continuously after Day 1 — it produces anxiety without insight. Set a monitoring cadence:

| Day | When | What to Check |
|---|---|---|
| May 31 | Evening | Kit Email 1 open rate + click rate; any new orders |
| June 1 | Evening | Kit Email 1 completion (all zones); Etsy traffic trend |
| June 3 | Evening | Day 5 benchmark: Email 3 open rate (40%+ target) |
| June 6 | Morning | Week 1 full review: subscriber count, total orders, social growth |

---

## Launch-Day Success Metrics Summary

### Phase 1 (Etsy) — by 12:00pm

| Metric | Target | Minimum Acceptable |
|---|---|---|
| Listings active with 5 images | 21 of 21 | 18 of 21 (6 stock-composited minimum) |
| SEEDWARDEN15 coupon active | Yes | Yes |
| Listing errors | 0 | 0 |
| Organic views (10am-12pm) | Any | — |

### Phase 2 (Email) — by 6:00pm

| Metric | Target | Minimum Acceptable |
|---|---|---|
| Broadcast delivery rate | >90% | >80% |
| Broadcast bounce rate | <2% | <5% |
| Open rate (6 hrs post-send) | >35% | >20% |
| Click rate (6 hrs post-send) | >8% | >3% |
| New day-1 subscribers | >5 | >1 |

### Phase 3 (Social) — by end of Day 1

| Platform | Target | Minimum Acceptable |
|---|---|---|
| Instagram impressions | >50 | >20 |
| TikTok views | >50 | >20 |
| Pinterest impressions | >30 (by Day 2) | >10 (by Day 2) |
| New sign-ups attributed to social | >3 | >0 |

---

## Rollback Procedure (if critical issues found after launch has started)

**Rollback is not a failure — it is a recovery protocol.**

**Scenario A: Kit broadcast is sending to wrong audience or with broken links**

1. Navigate to Kit > Broadcasts > [launch broadcast].
2. If still in "Sending" status: click "Pause" (if Kit offers this option for ongoing sends). Not all Kit plan levels allow mid-send pause.
3. If pause is not available: the broadcast will complete its send. Do not attempt to recall sent emails.
4. Issue a follow-up broadcast ("Quick update from Seedwarden") with the corrected link or clarification. Send immediately.
5. Document: which emails went out with the issue, what the issue was, what the correction was.

**Scenario B: Kit automation is not routing zones correctly**

1. Navigate to Kit > Automations. Pause the welcome automation.
2. For any new subscriber who signed up during the error window: manually identify their zone (from their Kit subscriber profile), manually send the correct Email 1 zone variant.
3. Fix the automation routing logic.
4. Resume the automation.
5. This scenario affects only new subscribers during the error window — it does not affect the broadcast or the existing sequence.

**Scenario C: Buffer/Later fails to post all social content**

1. Note which posts failed.
2. Log into each platform directly.
3. Post manually using the captions and images from the launch calendar.
4. This is a 15-minute manual recovery — it is not a crisis.

**Scenario D: Etsy listing issue (listing removed or inactive)**

1. Identify which listing is affected.
2. In Etsy Shop Manager: check the listing for any policy violations flagged by Etsy.
3. If listing was inadvertently set to Draft: click Publish.
4. If listing is under Etsy review: it will appear again when review completes. Do not attempt to re-create the listing.
5. Send a brief note to any buyers who already purchased the affected product confirming their order is processing normally.

---

*Generated: 2026-05-06. References: launch-day-script.md (detailed T+0 through T+24 blocks), tool-integration-map.md (verification checklists), phase-2-execution-timeline.md (launch sequence rationale).*
