---
title: "May 30 Launch Day Hour-by-Hour Runbook — Seedwarden Track B"
date: 2026-05-27
version: 1.0
status: PRODUCTION-READY
scope: Minute-by-minute execution guide for May 30 launch day (08:00–21:00 UTC)
references:
  - LAUNCH_DAY_DECISION_TREES.md (one-page troubleshooting)
  - LAUNCH_DAY_ROLLBACK_PROCEDURES.md (how to pause/revert mid-launch)
  - LAUNCH_DAY_SUCCESS_METRICS.md (thresholds and escalation rules)
---

# May 30 Launch Day Hour-by-Hour Runbook

**Launch window: 08:00–21:00 UTC (May 30, 2026)**

Track B is 100% launch-ready. This runbook eliminates ambiguity and enables rapid decision-making when things move fast. All decisions are time-gated and decision-tree referenced.

---

## Pre-Launch Checklist (May 30, 06:00–08:00 UTC)

Complete these before 08:00 UTC. Allocate 1.5 hours.

**System checks** (30 minutes):
- [ ] Verify all 8 Etsy Zone Card listings are in "Draft" status and ready to publish (not already published)
- [ ] Verify Kit broadcast email is in "Scheduled" status with correct send time (12:00 UTC)
- [ ] Open all 4 social media schedulers in separate browser tabs (Instagram via Buffer, TikTok via TikTok app, Pinterest via Pinterest app, Reddit direct)
- [ ] Verify GA4 Real-Time dashboard loads without errors (https://analytics.google.com > Real-Time > Overview)
- [ ] Test GA4 real-time tracking: visit one Etsy listing in incognito, wait 10 seconds, check if page_view event appears in GA4
- [ ] Verify Discord webhook: run `python3 scripts/test_discord_webhook.py` — should post test message to #analytics-alerts channel

**Content verification** (30 minutes):
- [ ] All email copy (subject + body) has been copy-edited for typos (search for common issues: "teh", "recieve", "occured")
- [ ] All social media captions have been copy-edited for tone, typos, and hashtag accuracy
- [ ] All URLs in email and social are shortened (use Bitly prefix "seedwarden-" for tracking) and tested by clicking them in incognito browser
- [ ] Verify all Etsy listings have correct product images (2000px minimum), pricing, and PDF attachment

**Team/communication setup** (10 minutes):
- [ ] Open LAUNCH_DAY_STATUS_UPDATES.md in a text editor (you will paste hourly status bullets here)
- [ ] Open Discord in a browser tab — you'll post launch status updates to #launch-updates every 2 hours
- [ ] Print LAUNCH_DAY_DECISION_TREE.md one-pager and place next to keyboard
- [ ] Have LAUNCH_DAY_ROLLBACK_PROCEDURES.md and LAUNCH_DAY_DECISION_TREES.md open in separate browser tabs
- [ ] Silence notifications on phone except Discord, email, and text

---

## 08:00 UTC — LAUNCH TRIGGER

**Critical decision point: Go/No-Go for publish**

All pre-launch checks passed? **YES → PROCEED**

**08:00–08:15 UTC: Publish Etsy Listings (15 minutes)**

1. Open Etsy Shop Manager > Listings
2. Filter: Status = Draft
3. You should see 8 listings: Zone Cards 3–10 (Zone 1–2 are pre-published; do not touch)
4. **Publish ALL 8 listings in rapid sequence**:
   - Select all 8 listings (checkbox at top)
   - Click "Publish" button
   - If any listing fails to publish, do NOT pause the full sequence. Note the failure, publish the others, then come back to troubleshoot the single failure (see LAUNCH_DAY_DECISION_TREES.md, Failure Mode F5)
5. **Confirm all 8 are now "Active"** in the listings view (status column should show green checkmark)
6. Do a spot check: click one published listing, verify it is fully visible in incognito browser (GA4 event should fire)

**Decision point after 08:15**:
- All 8 published OK → Proceed to 08:30 checkpoint
- 1–2 failed → Escalate to decision tree F5 (Etsy listing won't publish), attempt recovery, proceed if fixed; if not fixed, proceed with remaining 6–7 listings
- 3+ failed → **ESCALATE IMMEDIATELY** to Orchestrator with screenshot of error messages

**Status update**: Post to LAUNCH_DAY_STATUS_UPDATES.md: "08:15 — [X] of 8 Etsy listings published. Status: [ON TRACK / DEGRADED / BLOCKED]"

---

## 08:30 UTC — METRICS BASELINE & SOCIAL QUEUING

**Goal: Establish clean baseline for Day 1 metrics and queue all social posts**

**08:30–08:45 UTC: GA4 Baseline (10 minutes)**
1. Open GA4 > Real-Time > Overview
2. Take a screenshot of Real-Time pageviews, active users (should be low; just your testing)
3. Note the exact timestamp in LAUNCH_DAY_METRICS.md as "Day 1 Hour 0 baseline"
4. This baseline lets you measure the impact of each social post later

**08:45–09:00 UTC: Social Post Queuing (15 minutes)**

Your social posts go live on a staggered schedule:
- **Instagram**: 09:30 UTC (Tile + Reel post)
- **TikTok**: 10:30 UTC (Video post)
- **Pinterest**: 11:00 UTC (Pin post)
- **Reddit**: 14:00 UTC (Link post, r/vegetablegardening)

**For each platform, do this:**
1. Open Buffer (Instagram), or native scheduler (TikTok, Pinterest, Reddit)
2. Verify the scheduled post is queued with correct publish time
3. Verify caption has correct Bitly link and hashtags (cross-reference with social-content-calendar-60day.md Day 30)
4. If using Buffer for Instagram, verify post type is correct (Tile vs. Reel — refer to mockups)
5. **Do NOT post manually.** The scheduler will auto-publish at the scheduled time. Let it do its job.

**Status update**: "08:45–09:00 — Social posts queued [Instagram 09:30 / TikTok 10:30 / Pinterest 11:00 / Reddit 14:00]. Status: ON TRACK"

---

## 09:30 UTC — INSTAGRAM CHECKPOINT

**Decision point: Did Instagram post go live?**

**09:30–09:45 UTC: Instagram Post Verification**

1. Open Instagram directly (not Buffer; Buffer logs can lag)
2. Go to your Seedwarden account > Feed
3. **Is the post visible in the feed?**
   - **YES**: GA4 baseline is now 90 minutes into post-publication. Do not touch. Continue to 10:00 checkpoint.
   - **NO**: Check these in order:
     - Is Buffer showing the post as "Sent"? (Check Buffer dashboard)
     - Did the post appear as a draft instead of published? (Check Drafts tab)
     - Did Instagram report an error? (Check Buffer Activity log)
     - If any of the above, follow decision tree F7 (Social: Post did not go live)

**Metrics check** (if post is live):
1. GA4 > Real-Time > Events: you should see a spike in pageviews compared to 08:30 baseline (expect +20–100 pageviews in the next 30 minutes)
2. Instagram app: check the post's immediate engagement (likes, comments, saves over first 15 minutes)
3. If Instagram reach is in the low range (1–10 impressions in first 15 minutes), note it in LAUNCH_DAY_METRICS.md but **do NOT panic**. Instagram's algorithm throttles new posts initially and ramps up over 2–6 hours. Normal behavior.

**Status update**: "09:45 — Instagram post live. Baseline reach: [X] impressions at 30 min mark. Next post scheduled for 10:30 (TikTok). Status: ON TRACK"

---

## 10:00 UTC — FIRST METRICS CHECK

**Decision point: Are we tracking anything on GA4? Is early engagement in the expected range?**

**10:00–10:15 UTC: GA4 & Email Setup Verification**

1. **GA4 Health Check**:
   - Open GA4 > Real-Time > Overview
   - Pageviews since 08:00: expect 30–200 pageviews by 10:00 (mostly from your Etsy listings being discoverable + Instagram post starting to push traffic)
   - If you see 0 pageviews: there is a tracking issue. Open LAUNCH_DAY_DECISION_TREES.md, Failure Mode F8 (GA4 no tracking data). Attempt recovery now; if not resolved by 10:15, note it as a known issue and proceed (GA4 is a secondary metric; Etsy stats are primary)

2. **Kit Email Setup Verification**:
   - Open Kit.com > Automations > [Your broadcast name]
   - Status should show: "Scheduled for 12:00 UTC"
   - Do NOT send the email yet. It should auto-send at 12:00 UTC per schedule.
   - If status shows anything other than "Scheduled", click into the broadcast and verify the scheduled time is correct. If it is, do not change it; Kit may just have a UI lag.

**Metrics interpretation**:
- 30–200 pageviews by 10:00 UTC: Normal, early-stage traffic. Continue as planned.
- <30 pageviews: Below expected baseline. Diagnose: have all social posts gone live? Check Instagram, verify GA4 tracking code is on Etsy pages (Run F8 diagnostic if needed). Proceed; this is still early.
- >200 pageviews: Excellent. Above baseline. One of the social posts is driving unexpectedly strong traffic (check which one in GA4 > Traffic > Medium). Make a note and monitor if this accelerates.

**Status update**: "10:15 — GA4 pageviews (2 hours): [X]. Kit broadcast: Ready for 12:00 UTC send. Status: ON TRACK"

---

## 10:30 UTC — TIKTOK CHECKPOINT

**Decision point: Did TikTok post go live?**

**10:30–10:45 UTC: TikTok Post Verification**

1. Open TikTok directly (not the app UI; use tiktok.com)
2. Go to your Seedwarden account > Videos
3. **Is the most recent video the Zone Card promo video?**
   - **YES**: Good. TikTok takes longer to gain traction than Instagram. Do not expect significant views for 2–4 hours. Continue to 11:00 checkpoint.
   - **NO**: Check if you posted manually or if the scheduler failed:
     - Open TikTok Creator Studio (https://www.tiktok.com/creator/content)
     - Look for "Scheduled" or "Failed" status
     - If scheduled but not published: TikTok scheduler can delay 10–30 min; check back at 10:45
     - If failed: See LAUNCH_DAY_DECISION_TREES.md, Failure Mode F7 (Social post did not go live). You will need to post the video manually via TikTok app (5–10 min)

**Status update**: "10:45 — TikTok post live. Manual post upload time if needed: 5–10 min. Status: ON TRACK (or RECOVERED from scheduler failure)"

---

## 11:00 UTC — PINTEREST CHECKPOINT

**Decision point: Did Pinterest post go live?**

**11:00–11:15 UTC: Pinterest Post Verification**

1. Open Pinterest.com directly (not Buffer)
2. Go to your Seedwarden board (should be named "Seedwarden Zone Cards" or similar)
3. **Is the Zone Card pin visible at the top of your board?**
   - **YES**: Good. Pinterest drives slower initial traffic but high long-tail value. Do not expect significant clicks in hour 1. Continue to 11:30 checkpoint.
   - **NO**: Check these:
     - Is the board missing or renamed? (Check Boards > All boards)
     - Did you forget to create the board before scheduling the pin? (Pinterest requires board to exist before pinning)
     - If board is missing: Create board immediately named "Seedwarden Zone Cards", set to public, then post the pin manually (copy caption from social calendar Day 30)
     - If board exists but pin didn't appear: Follow LAUNCH_DAY_DECISION_TREES.md, Failure Mode F7

**Status update**: "11:15 — Pinterest pin live. Status: ON TRACK"

---

## 12:00 UTC — KIT BROADCAST SEND CHECKPOINT

**Critical decision point: Is the Kit broadcast sending?**

**12:00–12:05 UTC: Email Send Verification**

1. Open Kit.com
2. Go to your broadcast email automation
3. **What is the status?**
   - **"Sent" or "Completed"**: Email finished sending. Great. Do not touch. Proceed to 12:15 checkpoint to analyze open rates.
   - **"Sending"**: Email is in progress. This is normal for broadcasts to large lists (can take 2–5 min). Wait until 12:05, then recheck. If still "Sending" at 12:05, do not interrupt; let it finish.
   - **"Scheduled" and the time is past 12:00**: There may be a clock sync issue or Kit is running late. Wait 5 more minutes and recheck. Do not resend manually yet.
   - **"Failed"**: Email failed to send. Check the failure reason (usually: sender address not verified, or list is empty). Follow LAUNCH_DAY_DECISION_TREES.md, Failure Mode F6 (Kit broadcast send failed).

**If email fails at 12:00–12:05 UTC**:
- Failure reason: "Sender address not verified"? Go to Kit > Settings > Sender email, verify it is a real email address you control, click "Verify" if needed (takes 5–10 min). Then resend broadcast manually.
- Failure reason: "List is empty"? This is expected on Day 1; your email list grows from social sign-up forms. Do NOT panic. Your Kit broadcast will send to 0 subscribers today. This is OK. Move to the Gmail fallback: see LAUNCH_DAY_ROLLBACK_PROCEDURES.md.
- Failure reason: Something else? Note the error message and escalate to decision tree F6.

**Expected outcome by 12:05 UTC**: Email sent to however many subscribers are currently on your Kit list (could be 0 on Day 1; this is normal).

**Status update**: "12:05 — Kit broadcast sent [status: success / failure / 0 subscribers]. Email count: [X]. Status: [ON TRACK / FALLBACK ENGAGED]"

---

## 12:15 UTC — EMAIL ENGAGEMENT CHECK

**Goal: Verify email is tracking opens and clicks**

**12:15–12:30 UTC: Kit Email Analytics**

1. Open Kit > Broadcasts > [Your broadcast]
2. Check these metrics:
   - **Delivered**: How many subscribers received the email (should equal the count from 12:05)
   - **Opened**: Expect 0–5% open rate in the first 15 minutes (emails take time to hit inboxes and for people to see them; most opens happen 1–24 hours later)
   - **Clicked**: Expect 0 clicks in the first 15 minutes; focus on this number again at 15:00 UTC and 18:00 UTC

3. **If you sent 0 emails** (empty list): Note in LAUNCH_DAY_STATUS_UPDATES.md "Email list empty on Day 1 (expected)". Your email list will grow as people join via social sign-ups or referrals over the coming days.

**Status update**: "12:30 — Kit broadcast metrics. Delivered: [X] / Opened: [X] / Clicked: [X]. Status: ON TRACK"

---

## 12:30–14:00 UTC — LUNCH & MONITORING WINDOW

**Goal: Monitor metrics passively, do not make changes**

**What you should do**:
- Eat lunch
- Check GA4 every 15 minutes (no action; just observe)
- Check Instagram/TikTok/Pinterest every 30 minutes for engagement (likes, comments, shares)
- Log these observations to LAUNCH_DAY_METRICS.md

**What you should NOT do**:
- Edit any social posts
- Re-post anything
- Change email content
- Make any platform changes

**Expected metrics by 14:00 UTC** (4 hours in):
- GA4 pageviews: 100–500 cumulative (depends on Instagram reach)
- Instagram impressions: 50–300 (low for new account is normal)
- TikTok views: 20–200 (TikTok starts slow and ramps)
- Reddit post (goes live at 14:00): has not posted yet
- Kit email: 5–15% open rate (emails take 1–24 hours to accumulate opens)

---

## 14:00 UTC — REDDIT POST & AFTERNOON CHECKPOINT

**Decision point: Is Reddit post live and are we on track to meet 18:00 checkpoint targets?**

**14:00–14:15 UTC: Reddit Post Verification**

1. Open Reddit directly
2. Go to r/vegetablegardening > New
3. **Is your Zone Card post visible in the new section?**
   - **YES**: Good. Reddit posts take 4–8 hours to accumulate upvotes and visibility. Check back at 18:00 UTC.
   - **NO**: You may have hit the subreddit's posting limit or a filter. Check Reddit mod queue (if you have access) or just post manually:
     - Go to r/vegetablegardening > Create Post
     - Title: "Guide: [Zone] Zone Hardiness Quick-Start Cards for [Crop Type]" (from social calendar Day 30)
     - Post type: Link
     - URL: [Your Bitly link]
     - Post. Takes 2 minutes.

2. **If post is live**: Do NOT reply to comments yet. Let the post gain organic traction for 2 hours, then engage at 16:00 UTC.

**14:15–14:30 UTC: Mid-Day Metrics Review**

| Metric | Expected | Actual | Status |
|--------|----------|--------|--------|
| GA4 pageviews (6 hours) | 100–500 | ___ | |
| Instagram reach | 50–300 | ___ | |
| Kit email opens | 5–15% | ___ | |
| Reddit upvotes (first 30 min) | 0–5 | ___ | |

Look at your Actual column. Any major red flags?

**Decision tree for mid-day metrics**:

- **All metrics in expected range**: Continue as planned. Next checkpoint is 15:00 UTC.
- **GA4 pageviews very low (<100 by 14:00)**: Did all social posts go live? Check: Instagram post is published? TikTok video is posted? Pinterest pin is on board? If any failed, you need to manually post (see LAUNCH_DAY_ROLLBACK_PROCEDURES.md for rapid recovery). If all posted but metrics are still low: this is not unusual for a new product account. Proceed; Day 3 metrics matter more than Day 1.
- **Instagram reach very low (<50 impressions by 14:00)**: This is expected for a new account. Do NOT panic. Instagram organic reach for accounts under 100 followers is typically 20–100 impressions on first posts. Proceed.
- **Reddit post downvoted instead of upvoted**: This is rare but can happen if the post is perceived as promotional. If post drops below 0 upvotes, note it and do NOT delete it (deletion triggers mod notifications). Let it rest; it may recover. Check again at 18:00 UTC.
- **Kit email shows 0 opens**: Expect this. Most email opens happen 2–24 hours after send. Check again at 18:00 UTC.

**Status update**: "14:30 — Mid-day checkpoint. GA4: [X] pageviews. Instagram: [X] reach. Reddit: [X] upvotes. Status: [ON TRACK / DEGRADED / ESCALATING]"

---

## 15:00 UTC — DECISION CHECKPOINT: Continue vs. Pause

**Critical decision point: Are we continuing the launch as planned, or do we need to pause and investigate?**

This is your "go/no-go" for the final 6 hours of launch day.

**Decision criteria**:

| Scenario | Decision | Action |
|----------|----------|--------|
| GA4 pageviews ≥ 100 by 15:00 UTC | CONTINUE | Proceed normally to 21:00 UTC |
| GA4 pageviews 50–99 by 15:00 UTC | CONTINUE (monitor) | All systems are up; traffic is just lower than expected. This is normal. Check again at 18:00 UTC. |
| GA4 pageviews < 50 by 15:00 UTC | DIAGNOSE (30 min) | Investigate: Is GA4 tracking broken? Are social posts live? Have we confirmed Etsy listings are discoverable? Use decision trees F8 and F7. If issue is minor, recover and CONTINUE. If issue is major, escalate. |
| Any social platform account suspended | ESCALATE | This is rare. Contact Orchestrator immediately with screenshot. |
| >2 separate platform errors (e.g., Instagram + TikTok both failed) | ESCALATE | Multiple failures suggest systemic issue. Contact Orchestrator. |

**15:00–15:15 UTC: Go/No-Go Decision**

Make a binary decision: **Continue or pause?**

- **CONTINUE**: All systems functional, metrics are at least baseline, no major failures. Proceed normally to 21:00 UTC. Your remaining checkpoints are 18:00 and 21:00 UTC.
- **PAUSE**: Pause outreach (do not post anything new to social or email for 24 hours), investigate the failure, and create a remediation plan. Update LAUNCH_DAY_STATUS_UPDATES.md with the pause reason and estimated recovery time.

**If CONTINUE**:

**Status update**: "15:15 — Go/No-Go decision: CONTINUE. All systems nominal. Next checkpoint: 18:00 UTC. Status: ON TRACK"

---

## 15:15–18:00 UTC — AFTERNOON MONITORING

**What you should do**:
- Monitor metrics passively (GA4 every 15 min, social every 30 min)
- At 16:00 UTC: Reply to Reddit comments (if any). Engage authentically, answer questions, do NOT be promotional.
- At 17:00 UTC: Check Instagram/TikTok comments and reply to 2–3 engagement questions to boost algorithm visibility
- Update LAUNCH_DAY_METRICS.md with cumulative metrics every hour

**What you should NOT do**:
- Post anything new
- Edit published content
- Make any platform changes

---

## 18:00 UTC — EVENING CHECKPOINT

**Decision point: Should we continue evening outreach, or has something broken?**

**18:00–18:15 UTC: Evening Metrics Review**

| Metric | Expected | Actual | Status |
|--------|----------|--------|--------|
| GA4 pageviews (10 hours) | 200–1,000 | ___ | |
| Instagram reach | 100–500 | ___ | |
| Kit email opens | 10–30% | ___ | |
| TikTok views | 50–500 | ___ | |
| Reddit upvotes | 5–25 | ___ | |

**Decision tree for evening checkpoint**:

- **All metrics tracking well (on expected curve)**: Continue as planned. Final checkpoint is 21:00 UTC (end of launch day).
- **GA4 pageviews are flat or declining since 15:00 UTC**: This can indicate that initial traffic spike is over and we've exhausted organic reach for the day. This is normal. Expect metrics to pick up again on Day 2–3 as organic shares happen and social algorithms distribute posts. Proceed normally.
- **Kit email opens are low (<10% by 18:00 UTC)**: This is normal. Most email opens happen overnight (18:00–06:00 UTC). Check again at 21:00 UTC and Day 2 morning.
- **Reddit post is being downvoted or has negative score**: Do NOT delete the post. Downvoting can happen if Reddit users perceive it as promotional spam. The post is still visible to the subreddit; a negative score is still engagement. Leave it up. If post drops below -5 score, check it one more time at 21:00 UTC, and if it has stabilized, move on. This does not indicate a launch failure.

**18:15–18:30 UTC: Evening Decision**

- **CONTINUE**: Proceed normally to 21:00 UTC final checkpoint.
- **INVESTIGATE**: If metrics show unusual patterns (sharp drop, platform error, unusual engagement spike), take 20 min to diagnose using decision trees. If resolved, CONTINUE. If not resolved, note it as a known issue and CONTINUE (it may be a platform glitch or normal variance).

**Status update**: "18:30 — Evening checkpoint. GA4: [X] pageviews (10 hours). Kit: [X]% opens. Social engagement stable. Status: ON TRACK"

---

## 18:30–21:00 UTC — FINAL STRETCH

**What you should do**:
- Continue monitoring metrics every 30 min
- Do NOT make any platform changes
- At 19:00 UTC: Log cumulative Day 1 final metrics to LAUNCH_DAY_METRICS.md
- At 20:00 UTC: Discord alert script will auto-fire (if configured). Check #analytics-alerts channel to verify webhook is working.
- At 20:30 UTC: Prepare end-of-day status update for LAUNCH_DAY_STATUS_UPDATES.md

---

## 21:00 UTC — LAUNCH DAY CLOSE & FINAL CHECKPOINT

**Decision point: Launch day debrief. Did we meet minimum success criteria?**

**21:00–21:15 UTC: Final Metrics Summary**

Compile these into LAUNCH_DAY_METRICS.md:

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Etsy listings published | 8 | ___ | |
| GA4 pageviews (Day 1 total) | 200+ | ___ | |
| Kit emails sent | 1 | ___ | |
| Social posts live | 4 | ___ | |
| Email open rate (24-hour estimate) | 10%+ | ___ | |
| Instagram reach | 100+ | ___ | |
| TikTok views | 50+ | ___ | |
| Reddit upvotes | 5+ | ___ | |
| Pinterest saves | 2+ | ___ | |

**21:15–21:30 UTC: Go/No-Go Final Assessment**

**Minimum success criteria** (all must pass for "SUCCESSFUL LAUNCH"):
1. ✓ At least 6 of 8 Etsy listings published (1–2 failures are recoverable)
2. ✓ Kit email sent (sent to however many subscribers you have, even if 0)
3. ✓ At least 3 of 4 social posts live (missing 1 post is acceptable)
4. ✓ GA4 tracking confirmed working (at least 50+ pageviews by 21:00 UTC)

**If all 4 criteria are met**: **LAUNCH DAY WAS SUCCESSFUL**

This is not about reaching 1,000 pageviews on Day 1. It is about ensuring all systems are operational and firing. Organic reach will grow over Days 2–7.

**21:30 UTC: Final Status Update & Debrief**

Write to LAUNCH_DAY_STATUS_UPDATES.md:

```
## Launch Day (May 30, 2026) — FINAL SUMMARY

**Outcome**: [SUCCESSFUL / SUCCESSFUL WITH RECOVERY / REQUIRES FOLLOW-UP]

**Key Metrics (Day 1 Final)**:
- Etsy listings published: [X] of 8
- GA4 pageviews: [X] (estimate)
- Email sent: Yes / No [if no, fallback used]
- Social posts live: [X] of 4
- GA4 tracking: Confirmed / Requires troubleshooting

**Unresolved Issues** (if any):
- [Issue 1 and recovery plan]
- [Issue 2 and recovery plan]

**Day 2 Actions**:
- [ ] Check email open rate again (expect 10–30% by Day 2 morning)
- [ ] Monitor Reddit post at 06:00 UTC (expect upvotes to have climbed)
- [ ] Check Instagram/TikTok reach again (both posts should have 2–4x reach by Day 2)
- [ ] Review GA4 for which social channel drove the most traffic
- [ ] Update CONTINGENCY_DECISION_THRESHOLDS.md Day 3 column with actual metrics

**Notes**: [Any observations about what worked, what could improve, anomalies]
```

---

## Escalation Rules

**Escalate to Orchestrator immediately if**:

1. **3+ Etsy listings fail to publish** — indicates account-level issue
2. **GA4 shows 0 pageviews by 14:00 UTC** — indicates tracking failure or platform issue
3. **Multiple social platforms show account suspension** — rare, but indicates account security issue
4. **A failure persists after 60 minutes of recovery work** — you've exhausted decision trees; needs fresh perspective
5. **A cost decision >$50 is needed** (e.g., paid social ads to recover, platform upgrade) — needs approval

**How to escalate**:
1. Take a screenshot of the error or metric
2. Note the exact time the issue was discovered
3. Document which decision tree steps you followed and where they failed
4. Post to #alerts in Discord with: timestamp, failure mode, screenshot, decision tree reference, and estimated recovery time
5. Do NOT make major changes while waiting for response; continue with fallback procedures

---

## Quick Reference: Decision Points & Time Gates

| Time | Checkpoint | Decision | Reference |
|------|------------|----------|-----------|
| 08:00 UTC | Publish Etsy | Go/No-Go | This doc, Etsy section |
| 09:30 UTC | Instagram live? | Proceed / Troubleshoot F7 | This doc |
| 10:00 UTC | Metrics baseline | Continue / Escalate | This doc |
| 10:30 UTC | TikTok live? | Proceed / Troubleshoot F7 | This doc |
| 11:00 UTC | Pinterest live? | Proceed / Troubleshoot F7 | This doc |
| 12:00 UTC | Kit broadcast send | Monitor / Troubleshoot F6 | This doc |
| 14:00 UTC | Reddit live? | Proceed / Troubleshoot F7 | This doc |
| 15:00 UTC | Continue or pause? | CRITICAL GO/NO-GO | This doc |
| 18:00 UTC | Evening checkpoint | Monitor / Adjust | This doc |
| 21:00 UTC | Final assessment | Successful / Requires follow-up | This doc |

---

*Prepared: May 27, 2026. Seedwarden Launch Operations Team.*
*Companion docs: LAUNCH_DAY_DECISION_TREES.md, LAUNCH_DAY_ROLLBACK_PROCEDURES.md, LAUNCH_DAY_SUCCESS_METRICS.md*
