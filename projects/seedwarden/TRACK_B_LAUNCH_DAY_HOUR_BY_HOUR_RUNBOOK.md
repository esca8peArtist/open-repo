---
title: "Track B Launch Day Hour-by-Hour Runbook — May 30 08:00–14:00 UTC"
date: 2026-05-30
version: 1.0
status: production-ready
purpose: "Timestamp-based operational sequence with explicit success signals and escalation triggers. Use this document alone for launch-day execution."
---

# Track B Launch Day Hour-by-Hour Runbook
## May 30, 2026 — 08:00–14:00 UTC

**Solo operator time budget**: 6 hours total (includes monitoring, response handling, metric logging)

**How to use this document**: Open at 08:00 UTC on May 30. Work through each hour in sequence. Every hour includes:
- **Exact UTC time range**
- **Action checklist** (copy-paste ready, no ambiguity)
- **Expected metric** (what you should see if everything is working)
- **Success signal** (specific confirmation that this hour succeeded)
- **Failure signal** (specific indication something is wrong)
- **Escalation action** (what to do if failure signal appears)

---

## HOUR 0: 08:00–09:00 UTC — PRE-LAUNCH VERIFICATION

**Block this hour completely. Do not answer messages. Lock notifications.**

### Actions

- [ ] **Step 1 (5 min)**: Open Gist URL in incognito browser. Confirm all 8 zone PDFs are listed (Zone 3–10). Click one PDF — confirm it downloads immediately without "request access" error.
- [ ] **Step 2 (5 min)**: Open Etsy Shop Manager > Listings. Filter by "Draft." Confirm all Phase 2 listings (count: ___) show Draft status. Do NOT publish yet.
- [ ] **Step 3 (5 min)**: Open Kit dashboard > Broadcasts. Find the "Seedwarden is live" broadcast. Confirm status shows "Scheduled" for 12:00 UTC today. Do NOT send yet.
- [ ] **Step 4 (3 min)**: Open Instagram profile. Confirm bio link is set to the Gist URL (not a placeholder). If placeholder: edit now.
- [ ] **Step 5 (3 min)**: Open Buffer/Later queue. Confirm all May 30 posts show "Scheduled" status:
  - Instagram launch post — 08:30 UTC
  - TikTok launch video — 08:45 UTC
  - Pinterest pins — 09:00 UTC
  - [ ] All three show scheduled status with correct times
- [ ] **Step 6 (2 min)**: Record baseline metrics in spreadsheet (customer-analytics.csv):
  - Etsy shop views (last 7 days, from Shop Manager > Stats)
  - Kit subscriber count (Kit > Subscribers)
  - Instagram follower count
  - TikTok follower count
  - Pinterest monthly viewers (Pinterest Analytics)

### Expected Metric
All infrastructure online. No errors in any system.

### Success Signal
**Checklist complete. All 6 steps checked. No FAIL items.** Proceed to Hour 1.

### Failure Signal
- Gist URL returns 404 or access error
- Any Kit/Etsy/Buffer connection shows error status
- Baseline metrics cannot be recorded (authentication failure)

### Escalation Action
**If Gist is down**:
1. Immediately switch to backup URL (Google Drive folder or Dropbox link)
2. Update Instagram bio to backup URL
3. Update any unsent social posts with backup URL
4. Proceed with launch at 08:30 UTC using backup URL
5. Note in WORKLOG.md: "Switched to backup Gist link at 08:15 UTC"

**If Kit shows error**:
1. Log out and log back in
2. If error persists: Kit may be experiencing maintenance. Proceed with manual email fallback plan: Gmail BCC to Kit subscriber export list (do this at 12:00 UTC)
3. Note in WORKLOG.md: "Kit error at 08:15 UTC; activated manual broadcast fallback"

---

## HOUR 1: 08:30–09:30 UTC — EMAIL INFLUENCER OUTREACH

**Duration**: 15 minutes of action + 45 minutes of monitoring

### Actions

**Outreach script (copy-paste for each contact)**:
```
Subject: Zone guides are live — [CONTACT_NAME], here's the link

Hi [FIRST_NAME],

The Seedwarden Zone Quick-Start Cards are live as of this morning.

All 8 zone guides — free, direct download, no email required:
[GIST_URL]

If you'd still like to share these with your [community/audience/newsletter], 
I'd love that. No obligation and no particular ask — just letting you know 
they're up.

Happy to provide pre-written social copy or a short newsletter blurb 
if that would help.

Best,
[YOUR_NAME]
Seedwarden
```

**Send outreach emails** (check each as sent):
- [ ] Sabrena Gwin (AHG) — if she responded to pre-launch outreach
- [ ] Susan Leopold (UpS) — if she responded to pre-launch outreach
- [ ] John Gallagher (LearningHerbs) — if he responded to pre-launch outreach
- [ ] Juliet Blankespoor (Chestnut School) — if she responded to pre-launch outreach
- [ ] Any other contact who pre-approved sharing

**Time spent on outreach**: 10–15 minutes total (depends on number of contacts who pre-approved)

**For remainder of hour**: Monitor email inbox for immediate replies. Respond to any replies within 2 hours.

### Expected Metric
Email outreach to 3–8 contacts (Tier 1 who pre-approved). Zero bounce errors.

### Success Signal
All outreach emails sent without error. At least 1 contact replies positively within this hour.

### Failure Signal
- Email fails to send (SMTP error, authentication failure)
- Multiple outreach emails bounce (5+ addresses show "delivery failed")

### Escalation Action
**If email sending fails**:
1. Check your email provider's authentication settings (Gmail: ensure "Less secure app access" is enabled if using non-standard client)
2. Send one test email to your own address — confirm it arrives
3. If successful: retry the outreach batch
4. If failed: proceed without email outreach. The social posts will carry the announcement.

**If emails bounce**:
1. Remove bounced addresses from your contact list
2. Continue with remaining contacts
3. Note in WORKLOG.md: "[X] addresses bounced"

---

## HOUR 2: 09:00–10:00 UTC — SOCIAL MEDIA LAUNCH

**Duration**: 30 minutes of action (platform posts) + 30 minutes of monitoring

### Actions

**Reddit (manual post at 09:00 UTC exactly)**:
- [ ] Open r/herbalism
- [ ] Click "Create Post"
- [ ] Title: "I built free zone-specific growing guides for herbalists — all zones 3–10"
- [ ] Body: "Just launched eight quick-start cards designed for registered herbalists and clinical practitioners. Each guide covers frost dates, varieties, and sourcing ethics for your region. Free download — [GIST_URL]"
- [ ] Click Post
- [ ] Confirm post appears on r/herbalism within 2 minutes

**Instagram (scheduled, should auto-post at 08:30 UTC)**:
- [ ] At 08:35 UTC: Navigate to Instagram profile
- [ ] Confirm launch post is visible at top of feed
- [ ] Confirm caption includes the call-to-action directing to bio link
- [ ] If post did NOT post automatically: open Instagram directly, create new post with the saved caption and image, post manually

**TikTok (scheduled, should auto-post at 08:45 UTC)**:
- [ ] At 08:50 UTC: Open TikTok profile
- [ ] Confirm video is visible
- [ ] Confirm video is playing (not showing error)
- [ ] If not posted: log into TikTok app, upload video manually using saved caption and video file

**Pinterest (scheduled, should auto-post at 09:00 UTC)**:
- [ ] At 09:10 UTC: Open Pinterest profile
- [ ] Confirm pins are visible in profile
- [ ] If not posted: log into Pinterest, create pins manually using saved images and descriptions

**Monitoring (remainder of hour)**:
- [ ] Check Reddit post every 10 minutes — note upvote count
- [ ] Check Instagram Insights — note impressions
- [ ] Check TikTok Analytics — note views

### Expected Metric
- Reddit post visible, no mod removal notice
- Instagram post live with 20+ impressions in first hour
- TikTok video live with 30+ views in first hour
- Pinterest pins indexing (lower immediate traffic is expected; Pinterest indexes over 24 hours)

### Success Signal
**All four platforms have live posts by 09:15 UTC.** Posts are visible in public view (incognito browser confirms).

### Failure Signal
- Reddit post removed by moderator within 15 minutes
- Instagram/TikTok posts fail to publish from Buffer (error message visible in Buffer > queue)
- Social posts contain placeholder URL instead of real Gist URL

### Escalation Action
**If Reddit post is removed**:
1. Check the removal reason (mod message or auto-filter notification)
2. If promotional filter: repost immediately with personal framing: "I built a free zone-specific growing guide — here's Zone [X] as a reference"
3. If mod-banned account: do NOT create new account. Pivot to r/foraging instead.

**If Instagram/TikTok fails to post from Buffer**:
1. Log into Instagram directly
2. Create new post manually: paste caption from saved file, select image from camera roll, post
3. Do the same for TikTok (TikTok does not support Buffer on free tier; manual upload is expected)

**If social posts have placeholder URL**:
1. Edit each post immediately (most platforms allow caption edits within 30 minutes)
2. Replace placeholder with real Gist URL
3. Confirm edit appears on platform within 2 minutes

---

## HOUR 3: 10:00–11:00 UTC — FIRST ENGAGEMENT CHECK

**Duration**: 10 minutes of checking + 50 minutes of monitoring and response

### Actions

**Engagement snapshot** (at 10:05 UTC):
- [ ] Reddit post upvotes: _____ (record count)
- [ ] Reddit post comments: _____ (record count)
- [ ] Instagram impressions (Insights): _____ (record count)
- [ ] TikTok views (Analytics): _____ (record count)
- [ ] Any DMs received on Instagram: _____ (record count)
- [ ] Any replies to emails: _____ (record count)

**Response protocol**:
- [ ] Reply to every Reddit comment (first 10 if volume is high)
- [ ] Reply to every Instagram DM within 2 minutes
- [ ] Check email replies; respond to any influencer inquiries within 1 hour

**Monitoring cadence for remainder of hour**:
- At 10:15, 10:30, 10:45 UTC: Check each platform for new comments/DMs
- Respond to new engagement immediately

### Expected Metric
- Reddit post: 5–15 upvotes in first hour
- Instagram: 30–100 impressions
- TikTok: 50–150 views
- At least 1 comment on Reddit or Instagram

### Success Signal
**Post has engagement (upvotes, comments, or views visible).** Zero negative comments.

### Failure Signal
- Reddit post at 0 upvotes after 30 minutes (may indicate mod removal or spam filter)
- Instagram impressions under 10 (may indicate shadowban or bot suppression)
- TikTok views under 20 (may indicate account suppression)
- Any negative or troll comments (rare, but escalate if more than 1)

### Escalation Action
**If Reddit post has 0 upvotes after 30 minutes**:
1. Check Reddit post history — if the post is missing, it was removed. Repost as image post (upload Zone 5 or Zone 6 PDF as image) with personal framing
2. If post is visible but unpromoted: Reddit's algorithm favors early engagement. Responding to comments helps. Leave it for now, check again at 11:00 UTC

**If Instagram impressions under 10**:
1. Post an Instagram Story immediately with text "Zone guides are live" + link sticker
2. Reply to any comments to boost engagement signals
3. This is normal for new accounts. Continue.

**If negative comments**:
1. Do NOT delete the comment
2. Respond publicly with a brief, professional reply: "Thanks for your thoughts — the guides are free because [reason]. Appreciate your feedback."
3. Move on

---

## HOUR 4: 11:00–12:00 UTC — FINAL PRE-EMAIL CHECKLIST

**Duration**: 5 minutes of checking + 55 minutes of monitoring

### Actions

**Final verification before email broadcast** (at 11:00 UTC):
- [ ] Open Kit > Broadcasts > "Seedwarden is live"
- [ ] Confirm status shows "Scheduled" for 12:00 UTC
- [ ] Confirm email subject line is finalized (not a placeholder)
- [ ] Click "Preview" — confirm all links work and images load
- [ ] Confirm broadcast is set to send to "All Confirmed Subscribers" (not a test list)

**One final test send** (optional, but recommended):
- [ ] In Kit, click "Send test" (if available in your plan)
- [ ] Send test to your own email address
- [ ] Wait 30 seconds
- [ ] Open your email — confirm it arrives without spam filtering
- [ ] Click all links — confirm they go to correct URLs

**Monitoring** (11:05–12:00 UTC):
- [ ] Every 5 minutes: check Reddit post upvotes, Instagram Insights, TikTok views
- [ ] Update running metrics log with current numbers at 11:30 UTC
- [ ] Monitor email inbox for any last-minute influencer responses

### Expected Metric
Kit broadcast shows "Scheduled" with correct send time and confirmed audience.

### Success Signal
**Test email arrives in your inbox without errors. All links in email are clickable.**

### Failure Signal
- Kit broadcast status shows "Draft" (not scheduled)
- Test email lands in Spam folder (spam filter triggered)
- Email links are broken or malformed
- Broadcast is scheduled to send to wrong list or wrong time

### Escalation Action
**If broadcast status is Draft**:
1. Open the broadcast
2. Click "Schedule" (or "Send")
3. Select time: 12:00 UTC today
4. Click Schedule
5. Refresh to confirm status changed to "Scheduled"

**If test email lands in Spam**:
1. Check Kit's sent email for common spam triggers (too many links, aggressive CTA language)
2. Simplify if needed: reduce links, soften language
3. Send another test
4. This may be a Gmail filter issue, not a deliverability issue. Email will likely still reach subscribers; just note it

**If email links are broken**:
1. Edit the broadcast
2. Find the broken link (usually an Etsy URL or Gist URL)
3. Correct it
4. Save
5. Send another test
6. Proceed only after test link works

---

## HOUR 5: 12:00–13:00 UTC — EMAIL BROADCAST SEND & MONITORING

**Duration**: 30 seconds of action + 59.5 minutes of monitoring

### Actions

**At 12:00 UTC exactly**:
- [ ] Open Kit > Broadcasts
- [ ] Confirm the "Seedwarden is live" broadcast status shows "Sent" or "Sending"
- [ ] If status still shows "Scheduled" at 12:05 UTC: Kit may be queueing. Wait 5 minutes.
- [ ] If status still shows "Scheduled" at 12:10 UTC: click broadcast > click "Send Now" to override schedule

**Monitoring** (every 10 minutes from 12:00–13:00 UTC):

At **12:15 UTC**:
- [ ] Kit broadcast delivery rate: _____ % (target: 95%+)
- [ ] Kit bounce rate: _____ % (target: <2%)
- [ ] Etsy shop views spike visible? (check Shop Manager > Stats > Today)

At **12:30 UTC**:
- [ ] Kit open rate: _____ % (check broadcast stats; target: 15%+ at this checkpoint, 35%+ by 2 hours post-send)
- [ ] Kit click rate: _____ % (target: 3%+)
- [ ] First order received? (check Etsy Orders; YES / NO)

At **12:45 UTC**:
- [ ] Any Etsy buyer messages received? (check Etsy messages; count: _____)
- [ ] Any email replies to Kit broadcast? (check email inbox; count: _____)
- [ ] Reddit post upvotes update: _____ (record for trend)

At **13:00 UTC** (end of hour):
- [ ] Kit final snapshot: Open rate _____, Click rate _____, Delivery ____%
- [ ] Etsy snapshot: Today's views _____, Today's orders _____
- [ ] Social snapshot: Reddit upvotes _____, Instagram reach _____, TikTok views _____
- [ ] Record all numbers in customer-analytics.csv for "Hour 5" row

### Expected Metric
- Email delivery: 95%+ by 12:15 UTC
- Email bounce: <2%
- Email open rate: 15%+ by 12:30 UTC, 35%+ by 13:00 UTC
- At least 1 Etsy order received
- Etsy shop views spike relative to 08:00–10:00 UTC baseline

### Success Signal
**Email broadcast delivered to 90%+ of list. Open rate above 15% at 12:30 UTC. At least 1 order received.**

### Failure Signal
- Email delivery <80% at 12:30 UTC (indicates sending issue or list quality problem)
- Email bounce rate >5% (indicates list has many invalid addresses)
- Email open rate <5% at 12:30 UTC (indicates subject line or deliverability problem)
- Zero orders received by 13:00 UTC (not necessarily a failure, but unusual)

### Escalation Action
**If email delivery below 80%**:
1. Check Kit's delivery report for bounce details
2. Common causes: old email addresses, domain reputation issue, ISP throttling
3. Document bounce reasons in WORKLOG.md
4. Proceed — this is not a launch blocker, just a data point

**If bounce rate above 5%**:
1. Note in WORKLOG.md: "High bounce rate: X%"
2. For future broadcasts: clean the list by removing hard bounces before sending
3. Proceed with current launch

**If open rate below 5% at 12:30 UTC**:
1. Subject line may have been weak. Note for next broadcast.
2. Continue monitoring — open rate may increase over the next hour as more subscribers check email
3. If still <10% at 14:00 UTC: this is data for post-launch analysis, not a blocker

**If zero orders by 13:00 UTC**:
1. This is not unusual for the first hour post-email. Orders typically arrive within 2–6 hours of send.
2. Continue monitoring
3. If still 0 by end of day: check Etsy for listing errors (all 21 listings active? images loading?)

---

## HOUR 6: 13:00–14:00 UTC — END-OF-LAUNCH-WINDOW SUMMARY

**Duration**: 30 minutes of metric collection + 30 minutes of final checklist and logging

### Actions

**At 13:00 UTC, collect metrics** (this is your 6-hour snapshot):

From Kit dashboard:
- [ ] Broadcast open rate (6 hours post-send): _____% (expected: 30%+)
- [ ] Broadcast click rate: _____% (expected: 8%+)
- [ ] New subscribers from landing page: _____ (expected: 2–5)

From Etsy Shop Manager > Stats:
- [ ] Shop views today (as of 13:00): _____ (expected: 50%+ above baseline)
- [ ] Orders today: _____ (expected: 1–3 minimum)
- [ ] Order revenue today: $_____ (expected: $10–30 minimum from 1–3 orders)

From social platforms:
- [ ] Reddit post final upvotes: _____
- [ ] Reddit post final comments: _____
- [ ] Instagram reach (past 6 hours): _____
- [ ] Instagram profile visits: _____
- [ ] TikTok views: _____
- [ ] TikTok profile visits: _____

**Record in customer-analytics.csv**:
- [ ] Create row labeled "Day 0 — 14:00 UTC Final"
- [ ] Paste all numbers from above
- [ ] Include notes column: any anomalies, manual interventions, escalations used

**Final checklist**:
- [ ] All 4 social platforms have live posts (confirmed incognito)
- [ ] Email broadcast delivered and opens are tracked
- [ ] No critical platform errors or outages
- [ ] Escalation actions completed (if any were needed)
- [ ] Customer inquiries responded to (if any received)

**Log in WORKLOG.md**:
- [ ] Time: May 30 14:00 UTC
- [ ] Status: "Launch complete"
- [ ] Summary line: "[X] orders received, [X]% email open rate, [Y] social engagement"
- [ ] Any issues and resolutions applied
- [ ] Next checkpoint: June 2 (Day 3)

### Expected Metric
- Email open rate 30%+ (6 hours post-send)
- Email click rate 8%+
- 1–3 Etsy orders
- Reddit post 10+ upvotes
- Instagram reach 100+ impressions
- TikTok views 100+
- Zero critical platform failures

### Success Signal
**Launch-window metrics meet all targets.** No customer complaints or critical errors. Post content is live across 4 platforms and email has been delivered.

### Failure Signal
- Email open rate <15% (significant CTA or deliverability issue)
- Zero orders (may indicate listing visibility issue)
- Social posts removed by platforms (rare, but indicates policy violation)

### Escalation Action
**If email open rate <15%**:
1. Not a blocker. Open rates for new product launches are often lower.
2. Note subject line for future testing
3. Proceed to Day 1 post-launch monitoring

**If zero orders by 14:00 UTC**:
1. Check Etsy: are listings visible in public search? (open incognito, search Etsy)
2. Check listing images: are all 5 images visible in product gallery?
3. If no: update listings now
4. If yes: order volume will likely come in next 6–24 hours from email opens over time
5. Proceed to Day 1 monitoring

---

## END-OF-LAUNCH-WINDOW WRAP-UP (14:00 UTC Onward)

**Do not check metrics continuously after 14:00 UTC.** Launch day monitoring is complete. Switch to post-launch protocol.

### Immediate post-14:00 UTC tasks:
- [ ] Respond to all buyer messages received (within 4 hours of message, per SLA)
- [ ] Respond to any influencer replies (within 2 hours)
- [ ] Take a 1-hour break (you have been working 6 hours)
- [ ] At 18:00 UTC: check metrics one final time for end-of-day snapshot
- [ ] At 21:00 UTC: log final end-of-day metrics in customer-analytics.csv

### Day 1 Evening Check (18:00–21:00 UTC):
- Kit email final open rate and click rate
- Etsy shop views and orders (full day count)
- Social follower growth
- Response count (DMs, emails, Reddit comments)

### Do NOT do:
- Do not check metrics every hour for the next 7 days
- Do not make changes to listings or social posts without waiting 24 hours (algorithm needs time to stabilize)
- Do not send follow-up emails to non-responding contacts until Day 3 (June 2)

---

## QUICK REFERENCE CARD (Print This)

```
MAY 30 LAUNCH — UTC TIMES ONLY

08:00–09:00   PRE-LAUNCH VERIFICATION
               ✓ Gist URL test
               ✓ Etsy listings confirmed Draft
               ✓ Kit broadcast confirmed Scheduled
               ✓ Social posts confirmed Scheduled
               ✓ Baseline metrics recorded

08:30–09:30   EMAIL INFLUENCER OUTREACH
               ✓ Send outreach to Tier 1 contacts (10–15 min)
               ✓ Monitor for replies (45 min)

09:00–10:00   SOCIAL MEDIA LAUNCH
               ✓ Reddit post (manual, 08:00 UTC)
               ✓ Instagram auto-post (08:30 UTC)
               ✓ TikTok auto-post (08:45 UTC)
               ✓ Pinterest auto-post (09:00 UTC)

10:00–11:00   FIRST ENGAGEMENT CHECK
               ✓ Snapshot: upvotes, impressions, views
               ✓ Respond to comments/DMs

11:00–12:00   FINAL PRE-EMAIL CHECKLIST
               ✓ Kit broadcast confirmed Scheduled
               ✓ Test email sent (optional)
               ✓ Monitor social trends

12:00–13:00   EMAIL BROADCAST SEND
               ✓ Broadcast fires at 12:00 UTC
               ✓ Monitor delivery, opens, clicks
               ✓ Record metrics every 15 min

13:00–14:00   END-OF-LAUNCH-WINDOW SUMMARY
               ✓ Collect final 6-hour snapshot
               ✓ Record in customer-analytics.csv
               ✓ Log in WORKLOG.md

ESCALATION CONTACTS & ACTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gist down        → Switch to backup URL immediately
Email bounce >5% → Note in WORKLOG; proceed
Reddit removed   → Repost as image post
Social failed    → Manual post within 15 min
Zero orders      → Check listing visibility; proceed to Day 1

SUCCESS THRESHOLD (14:00 UTC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Email open rate:    30%+ (6 hrs post-send)
Email click rate:   8%+
Orders received:    1–3 minimum
Social engagement:  Reddit 10+ upvotes, IG 100+ reach, TT 100+ views
No critical errors: All platforms online, no removals
```

---

*Document status: Production-ready. May 30, 2026.*
*Use this document as your sole operational guide for launch day. Complete each hour in sequence.*
*Next document to open: TRACK_B_LAUNCH_DAY_COMMON_ISSUES_DECISION_TREES.md (June 1+ for any issues)*
