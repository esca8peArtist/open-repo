---
title: "Phase 2 Launch Day Script — May 30, 2026"
date: 2026-05-06
status: production-ready
references:
  - phase-2-day-by-day-execution.md
  - tool-integration-map.md
  - contingency-paths.md
---

# Phase 2 Launch Day Script
## May 30, 2026

**How to use this document**: This is a sequenced script for a single day. Open it at 8:00am on May 30. Read each block in order. Do not skip ahead. Each block tells you what to do, what to verify, and what to do if something is wrong.

All prep work documented in phase-2-day-by-day-execution.md should be complete before this script begins. If any pre-launch item from Days 26–28 is incomplete, address it at T-2h rather than improvising during the launch sequence.

---

## T-2h: 8:00am — Final QA Checklist

Block 60 minutes. This is the most important hour of launch day. Running this QA in full eliminates 90% of recoverable errors before they become launch-day fires.

**Etsy verification (20 min)**:
- [ ] Open each of the 21 Etsy listings in Etsy Shop Manager. Confirm each shows 5 images (slots 1–5). If any listing shows fewer than 5 images, upload the missing image now — you have time.
- [ ] Open 3 of the highest-traffic listings in a public browser window (not logged in). Confirm the lifestyle images are visible in the listing gallery.
- [ ] Confirm SEEDWARDEN15 coupon is active: Etsy Shop Manager > Marketing > Sales and Coupons. The coupon status should show "Active." If it shows "Expired" or "Disabled," reactivate or recreate it now.
- [ ] Confirm all 21 listings are set to "Active" (published). Any listings left as "Draft" are not visible in search.

**Kit verification (20 min)**:
- [ ] Open Kit > Broadcasts. Confirm the launch broadcast shows "Scheduled" status for 12:00pm today. If it shows "Draft," reschedule it now.
- [ ] Open Kit > Automations. Confirm the Seedwarden Welcome automation is "Published" (not draft, not paused). If paused, resume it.
- [ ] Open the Kit landing page in an incognito window. Sign up with a disposable test email address. Confirm Email 1 arrives within 60 seconds with a working zone card download link. If the test fails, check: Is the automation running? Is the zone routing configured? Is the Google Drive link still accessible?
- [ ] Check Kit subscriber count. Record it in the launch day row of customer-analytics.csv.

**Social media verification (10 min)**:
- [ ] Log into Buffer or Later. Confirm all three launch posts show "Scheduled" status — Instagram (2:00pm), Pinterest (2:00pm), TikTok (4:00pm).
- [ ] Click "Preview" on each post to confirm the image is attached and formatted correctly.
- [ ] If any post shows a "Connection error" for a platform: navigate to Buffer Settings > Connected Accounts and reconnect the affected platform. Then re-confirm the post is scheduled.

**Zone card delivery verification (10 min)**:
- [ ] Open each Google Drive zone card download link (all 8) in an incognito window. Confirm each downloads a PDF with the correct zone number. A single broken link affects every subscriber in that zone.
- [ ] Spot-check Kit Email 1 Zone 5 variant: confirm the download link matches the Zone 5 Google Drive URL, not Zone 6 or another zone.

**If critical issues found during T-2h QA**:
- Broken download link: replace the Google Drive file or the Kit email URL. Takes 5 minutes.
- Missing Etsy image: upload now. Takes 2 minutes per image.
- Kit automation paused: resume it. Takes 30 seconds.
- Social post not scheduled: reschedule. Takes 3 minutes.
- If a non-critical cosmetic issue is found (wrong font, color inconsistency): note it for post-launch fix. Do not let a cosmetic issue delay the launch.

---

## T-1h: 9:00am — Pre-Launch Communications

**Team confirmation (5 min)**:
If anyone else is involved in the project (a photographer, a designer, a business partner): send a brief message confirming launch is proceeding on schedule. "QA passed, launch sequence begins at 10am. Etsy images going live at 10, email at noon, social at 2pm."

**Browser and device preparation (5 min)**:
- Open all tools you will need during the launch in separate browser tabs: Etsy Shop Manager, Kit Analytics, Buffer/Later, your Etsy store's public view (in an incognito window).
- On your phone: open Kit Analytics mobile view (kit.co is mobile-responsive) and Etsy Seller app for quick mobile monitoring.
- Keep a notepad (physical or digital) open. You will record metrics every 30 minutes for the first 4 hours.

**Metric baseline record (10 min)**:
Before launch starts, record these baseline numbers in customer-analytics.csv:
- Etsy shop views (last 7 days)
- Etsy total orders (all time)
- Kit subscriber count
- Instagram follower count
- Pinterest monthly viewers (if already active)

These are the before-state numbers. Everything measured after 10am is attributable to Phase 2.

---

## T+0: 10:00am — Etsy Launch

**Action**: Confirm all 21 Etsy listings are showing 5-image stacks in search results.

Open your Etsy store public page at exactly 10:00am (already logged out or in incognito). Scroll through all listings. Confirm the lifestyle images are visible. If a listing appears to have fewer than 5 images in public view, click into it to verify — Etsy's search thumbnail shows only the first image, but the gallery inside the listing shows all images.

**Why Etsy goes first** (rationale for the 10am/12pm/2pm staggered sequence):
Etsy's search algorithm responds to listing engagement. Publishing updated listing images at 10am gives the Etsy algorithm 2 hours to register the changes before the email broadcast drives a traffic spike at noon. Buyers who discover the store organically in the 10am–12pm window and purchase before the email sends are the highest-quality signal — they converted without any email push.

**What to monitor from 10am to 12pm**:
- Etsy Shop Manager > Stats > Today's Views: check every 30 minutes.
- Any organic views in this window are baseline — record them.
- If an Etsy listing shows an error or is unexpectedly removed: fix it now. You have 2 hours before the broadcast drives traffic.

---

## T+2h: 12:00pm — Email Broadcast Sends

**Action required**: None. Kit sends the broadcast automatically at the scheduled time.

**Verify at 12:05pm**:
- Open Kit > Broadcasts > [launch broadcast]. Confirm status shows "Sent" or "Sending."
- If the broadcast still shows "Scheduled" at 12:10pm: Kit may be processing a large send queue. Wait 10 minutes before investigating.
- If the broadcast still shows "Scheduled" at 12:20pm: navigate to the broadcast, click "Send Now" to override the schedule. This should not be necessary but resolves a stalled scheduled send.

**What to monitor from 12:00pm to 2:00pm**:
- Kit Analytics > Broadcasts: opens and clicks updating in real time. Target: 30%+ open rate within first hour.
- Etsy Stats > Today's Views: should spike within 30–60 minutes of broadcast send, as email subscribers click through to listings.
- Etsy Stats > Orders: the first Phase 2 order is most likely in this window. Record the timestamp when it occurs.

**Metric recording at 12:30pm and 1:30pm**:
Log in customer-analytics.csv:
- Kit broadcast opens (absolute count and percentage)
- Kit broadcast clicks (absolute count and percentage)
- Etsy views since 10am
- Etsy orders since 10am
- New Kit subscribers (signed up today via the zone card form)

---

## T+4h: 2:00pm — Social Media Launch

**Action**: Social posts go live automatically via Buffer/Later at 2pm (Instagram, Pinterest) and 4pm (TikTok).

**Verify at 2:05pm**:
- Log into Instagram and confirm the Phase 2 launch post has published.
- Log into Pinterest and confirm the launch pin has published.
- Check Buffer/Later for any publishing errors.

**If a social post fails to publish**: publish manually. Copy the post text from the Buffer/Later draft. Upload the image directly in the platform's app. Publish immediately — the 2-hour delay from the email is already built in, so posting at 2:15pm vs 2:00pm has no meaningful impact.

**Real-time social engagement (2:00pm–6:00pm)**:
- Respond to every comment on the Instagram launch post within 2 hours. Early engagement (comments and responses) within the first hour improves algorithmic distribution of the post.
- On Pinterest: pins do not generate real-time comments at this stage. Check repins and saves at 6pm.
- On TikTok: if the video generates comments within the first 3 hours, respond to the top 3. TikTok's algorithm rewards creator responses in the early comment window.

---

## T+0 to T+24h: Response Handling

### Customer questions
Most buyer questions on launch day fall into three categories:

**"Is this a PDF download or a physical product?"**
Template response: "It's an instant digital download — you'll receive a PDF link immediately after purchase. No shipping, no waiting. If you have any trouble with the download, just message me and I'll resend it directly."

**"I didn't receive my download link."**
Template response: "Etsy sends the download link automatically to the email address associated with your Etsy account. Check your spam folder for an email from Etsy (not from Seedwarden). If you don't see it, reply here with your order number and I'll send the file directly."
- In Etsy Shop Manager: Orders > [order] > send the PDF file as a message attachment.

**"Can I get a refund?"**
Template response: "Digital downloads are non-refundable once accessed. If you haven't opened the file yet and feel the product wasn't as described, I'll work with you. Can you tell me what you were expecting vs. what you received?"
- Etsy's seller protection covers digital downloads that match their descriptions. If the listing description accurately described the product, you are protected.

**"Do you have a Zone [X] that isn't listed?"**
Template response: "Zone [X] is currently in production and will be available within 30 days. If you'd like to be notified when it launches, sign up for the Zone Quick-Start Card email list [Kit landing page URL] — I'll send you your zone card as soon as it's ready."

### Tech support issues
If Kit sends a broken link to a subscriber (wrong zone card or 404 error):
- Navigate to Kit > Subscribers > find the affected subscriber by email.
- Check their zone tag. Verify the Email 1 variant they received matches their zone tag.
- If there was a routing error: manually resend the correct Email 1 variant via Kit > the subscriber's profile > "Send Email."
- Note the error in WORKLOG.md. If more than 2 subscribers had the same routing error, investigate the automation for a systematic configuration issue.

### Metric tracking schedule

| Time | Where to Check | What to Record |
|---|---|---|
| 10:00am | Etsy Stats (baseline post-launch confirmation) | Views, orders |
| 12:30pm | Kit, Etsy | Open rate, clicks, Etsy views since 10am, orders |
| 2:00pm | Kit, Etsy | Updated broadcast metrics, social post published confirmation |
| 6:00pm | Etsy, Kit, Instagram, Pinterest | End-of-day views, orders, social post engagement |
| 9:00am next day (May 31) | All channels | 24-hour total: views, orders, new subscribers, social engagement |

Record all readings in the launch-day row of customer-analytics.csv.

---

## Rollback Procedure

**When to trigger a rollback**: Only if a critical error is found that cannot be fixed without pausing the launch. Critical means: wrong product is being sold at the wrong price, Kit automation is sending subscribers a competitor's link, or an Etsy listing contains incorrect or potentially dangerous information.

Non-critical issues (image in wrong slot, typo in email body, wrong coupon code) do not trigger a rollback. Fix them while the launch continues.

**How to pause the email broadcast**:
- Kit > Broadcasts > [launch broadcast] > Pause. This stops sends to subscribers who haven't received it yet. Subscribers who already received it are unaffected.
- Fix the issue. Resume the broadcast from Kit > Broadcasts > [launch broadcast] > Resume.

**How to pause social posts**:
- Buffer/Later > Scheduled queue > find the post > Pause or Delete.
- If already published: you cannot unpublish from Buffer. Log into each platform directly and delete the post from there.

**How to pause the Kit welcome automation**:
- Kit > Automations > [Seedwarden Welcome] > Pause. New subscribers will not enter the automation while it is paused. Existing subscribers in the sequence receive no further emails until you resume.
- Resume: same path > Resume. Subscribers re-enter the sequence at their current position.

**Relaunch after rollback**:
- Fix the critical issue. Confirm the fix in a test environment (incognito window, test subscriber) before relaunching.
- Resume automation and rescheduled broadcast.
- Send a brief follow-up message to any subscribers who received a broken email: "Quick correction — here's the right link: [URL]." Subject: "Correction: [what was wrong]." A transparent, brief correction email preserves trust better than silence.

---

## Success Metrics

### Launch-day targets (May 30)

| Metric | Target | Stretch | Below-Target Response |
|---|---|---|---|
| Kit broadcast open rate | 30%+ | 45%+ | If below 20%: check spam — may be a deliverability issue |
| Kit broadcast click rate | 12%+ | 20%+ | If below 8%: email copy issue — revise for next broadcast |
| New Zone Card sign-ups (launch day) | 5+ | 15+ | If 0: check that landing page is linked in social bios |
| Etsy views (launch day) | 50+ | 150+ | If below 20: check listing SEO and broadcast link accuracy |
| Etsy orders (launch day) | 1+ | 4+ | 0 orders on launch day is acceptable — SEEDWARDEN15 coupon redeems on Day 10 |

### Week 1 targets (May 30 – June 6)

| Metric | Target |
|---|---|
| Total Phase 2 orders (first 7 days) | 3–8 orders |
| SEEDWARDEN15 coupon redemptions | 4–8% of list size |
| New email subscribers (sign-ups via zone card form) | 20+ |
| Etsy favorites on lifestyle listings | 15+ |

### Zone-specific metrics
Track in customer-analytics.csv:
- Which zone generates the most sign-ups (leading indicator of geographic demand)
- Which products generate the most Etsy views from the broadcast click-through (which UTM links are most clicked)
- Which zone produces the first buyer (early purchase geography signal)

### Buyer segment profiles to watch
In the first 72 hours: check whether buyers are new (no prior Etsy history with Seedwarden) or returning (tagged etsy-buyer already). Note this in customer-analytics.csv. A high proportion of returning buyers indicates Phase 1 list-building is working. A high proportion of new buyers indicates the broadcast reached new organic discovery traffic.

---

## Monitoring Dashboard Setup

**Daily standup template** (5 minutes each morning, May 31 through June 14):
```
Date:
Etsy views (24h):
Etsy orders (24h):
New Kit subscribers (24h):
Kit welcome sequence — new subscribers in sequence:
Social post with highest engagement (and engagement count):
Any customer messages requiring response? (Y/N):
One observation:
```

Record each standup in a running section at the bottom of customer-analytics.csv.

**Alert thresholds** (things that require same-day investigation, not next-day):
- Zero Etsy views for 24 consecutive hours: check if listings are still active in Shop Manager
- Kit automation "failed" status: check Kit > Automations for error messages
- Google Drive zone card link returns 404 or "access denied": re-share the file and update Kit email links
- Social account connection error in Buffer: reconnect the account within 24 hours to avoid missing scheduled posts
