---
title: "May 30 Launch Day Decision Trees — Detailed Troubleshooting Guide"
date: 2026-05-27
version: 1.0
status: PRODUCTION-READY
scope: Step-by-step recovery for 12 common launch-day failure modes
references:
  - LAUNCH_DAY_HOUR_BY_HOUR_RUNBOOK.md (timeline context)
  - LAUNCH_DAY_ROLLBACK_PROCEDURES.md (recovery procedures)
  - LAUNCH_DAY_DECISION_TREE.md (one-pager quick reference)
---

# May 30 Launch Day Decision Trees — Detailed Troubleshooting Guide

**Use this doc when**: You encounter a specific failure and need step-by-step recovery instructions.

**How to use**:
1. Identify the failure mode from the checklist below
2. Follow the decision tree for that mode
3. Execute the recovery procedure
4. Document the outcome in LAUNCH_DAY_ROLLBACK_LOG.md
5. If stuck after 15 min, escalate to Orchestrator with the tree reference

---

## DT1: Email Broadcast Won't Send (Kit)

**Symptom**: Kit broadcast is scheduled for 12:00 UTC but shows "Failed" status or "Pending" at 12:05 UTC.

**Discovery checkpoint**: 12:00–12:05 UTC

---

### DT1 Decision Tree

```
Kit broadcast status at 12:00 UTC:
       |
       +-- "Sent" or "Completed" → Done! No action needed.
       |
       +-- "Sending" → Normal in progress. Wait until 12:05, recheck.
       |   If still sending at 12:05: This is unusual but not a failure.
       |   Kit is slow but it will finish. Let it run.
       |
       +-- "Scheduled" and time is past 12:00
       |   → Kit may be running late. Wait 5 more minutes and recheck.
       |
       +-- "Failed" → What is the error message?
           |
           +-- "Sender email not verified"
           |   → Go to DT1-A: Verify Sender Email (below)
           |
           +-- "List is empty"
           |   → Go to DT1-B: Empty List Fallback (below)
           |
           +-- "Account billing issue"
           |   → Go to DT1-C: Billing Issue (below)
           |
           +-- Other error → Screenshot error. Escalate to Orchestrator.
```

---

### DT1-A: Verify Sender Email

**Time to execute**: 5–10 minutes

**Steps**:

1. Kit dashboard > Settings (gear icon, top right)
2. Look for "Email Settings" or "Sender Address"
3. Find the sender email address (should be your email, like `hi@seedwarden.com` or your personal email)
4. Click "Verify" or "Verify Email" if there is a button
5. Check your email inbox for a verification email from Kit
6. Click the verification link in the email (takes 2 seconds)
7. Return to Kit > Settings. Sender should now show "Verified" ✓
8. Go back to Broadcasts
9. Resend the broadcast email manually:
   - Find the failed broadcast
   - Click "Send Now" or "Resend"
   - Confirm you want to send to all subscribers
   - Click "Send"
10. Wait 10 seconds. Status should change to "Sending" then "Sent"

**Outcome**:
- ✅ Email sent successfully → Document in log, continue to next checkpoint
- ❌ Email still fails → Escalate to Orchestrator with error code

---

### DT1-B: Empty Email List Fallback

**Time to execute**: 10–15 minutes

**Scenario**: Kit shows "List is empty" — your email list has 0 subscribers (normal on Day 1).

**Decision**: This is NOT an error. Your email list is empty because it just launched. However, you still need to send the launch email *somewhere* so it is documented that email outreach was attempted.

**Fallback: Use Gmail**

1. Open Gmail
2. Click "Compose"
3. **TO field**: Leave blank or use your own email
4. **BCC field**: Enter all subscriber emails (if you have a list from somewhere). If no list exists, just use your own email as a test send.
5. **Subject**: Copy from the Kit broadcast email subject line
6. **Body**: Copy the full Kit broadcast email body (including all formatting, links, images)
7. Review the entire email for typos and broken links:
   - Click every link to verify it works
   - Check the lead magnet PDF link specifically
8. Click "Send"
9. Immediately go to Sent folder and confirm the email is there

**Important notes**:
- Do NOT put email addresses in the TO field (this exposes everyone's email to the group)
- Always use BCC for group emails
- Gmail fallback email will not track opens/clicks like Kit does
- This is acceptable for launch day; it documents that email outreach happened

**Document in log**: "Kit broadcast failed (empty list). Gmail fallback sent at [TIME] UTC to [X] recipients."

**Next steps**: Your email list will grow over Days 2–7 as people sign up via social media. Starting Day 2, you will have real subscribers.

---

### DT1-C: Billing Issue Fallback

**Time to execute**: 15 minutes (no resolution; fallback only)

**Scenario**: Kit payment method is expired or billing is suspended.

**Decision**: You cannot fix billing on launch day. Use Gmail fallback immediately.

**Steps**:

1. Go to Kit > Settings > Billing or Plan
2. Note the billing issue (expired card, overdue payment, etc.)
3. **Do NOT try to fix this now.** Use the Gmail fallback (DT1-B above).
4. After launch day, update your Kit payment method and you can resume using Kit for email.

**Fallback**: Execute the Gmail fallback (DT1-B) immediately.

**Document in log**: "Kit billing issue detected. Fallback: Gmail broadcast sent at [TIME] UTC."

---

## DT2: Etsy Listing Won't Publish

**Symptom**: Etsy "Publish" button is clicked, but the listing stays in Draft status or shows an error.

**Discovery checkpoint**: 08:00–08:15 UTC during Etsy publish phase

---

### DT2 Decision Tree

```
Click "Publish" on the Etsy listing:
       |
       v
Does Etsy show an error message?
       |
    NO → Check listing status
       |  Is it now "Active" (published)?
       |       |
       |      YES → Success! Move to next listing.
       |       |
       |      NO → Listing stays in Draft
       |             → Go to DT2-A: Check Required Fields (below)
       |
    YES → Read the error message. Is it one of these?
           |
           +-- "Title is too long" (>140 characters)
           |   → DT2-A: Fix title length
           |
           +-- "Price is invalid" (includes $0 or negative)
           |   → DT2-A: Set a valid price (>$0)
           |
           +-- "Missing required field: [FIELD]"
           |   → DT2-A: Complete the missing field
           |
           +-- "Image too small" (must be 2000px minimum)
           |   → DT2-B: Replace image with larger version
           |
           +-- "You have too many listings in Draft" (account limit)
           |   → DT2-C: Delete old draft listings
           |
           +-- "Account issue: please contact Etsy"
           |   → DT2-D: Account-Level Issue (escalate)
           |
           +-- Other error
               → Screenshot error. Escalate to Orchestrator.
```

---

### DT2-A: Fix Required Fields

**Time to execute**: 5 minutes per listing

**Steps**:

1. Click on the listing to open edit mode
2. Check these fields against Etsy requirements:

| Field | Etsy Requirement | How to Check | Fix |
|-------|---|---|---|
| **Title** | Under 140 characters | Check length in edit field | Shorten title |
| **Price** | Greater than $0 | Look at price field | Set to $5–15 |
| **Tags** | 13 tags, each under 20 chars | Count tags and check lengths | Remove or shorten tags |
| **Category** | Required | Make sure a category is selected | Select "Digital Download" |
| **Primary image** | 2000px minimum | Check image specs | Upload larger image |
| **Listing type** | Digital or Physical | Make sure "Digital" is selected | Select Digital Download |
| **Shipping** | Set to "Digital" (no shipping) | Check shipping settings | Set to Digital, shipping-free |
| **PDF attached** | Required for digital | Look for PDF section | Upload the guide PDF |

3. Fix any failed fields
4. Click "Save"
5. Try "Publish" again
6. If it publishes → Success! Move to next listing.
7. If it fails again → Go back to checklist above. Is there another field missing?

---

### DT2-B: Replace Image

**Time to execute**: 5 minutes per listing

**Steps**:

1. Open the listing in edit mode
2. Find the "Images" section
3. Delete the small image (click the X on the image thumbnail)
4. Click "Add images"
5. Do you have a larger version of the image (2000px or more)?
   - **YES**: Upload the large image
   - **NO**: Use a placeholder image that is at least 2000px (search your design files for the master Canva export)
6. Save the listing
7. Try "Publish" again

---

### DT2-C: Delete Old Draft Listings

**Time to execute**: 10 minutes

**Scenario**: Etsy account has hit the draft listing limit (usually 25–50 drafts depending on account type).

**Steps**:

1. Etsy Shop Manager > Listings
2. Filter by Status = "Draft"
3. Look through the draft list. Are there any very old ones from previous launches (e.g., 2025 or early 2026)?
4. Select the oldest/least relevant drafts
5. Right-click > "Delete listing" (or click the trash icon)
6. Confirm deletion
7. Return to your May 30 listing and try "Publish" again

---

### DT2-D: Account-Level Issue

**Time to execute**: 0 minutes (escalate immediately)

**Scenario**: Etsy shows "Account issue" or "Account verification required" or "Your account has been suspended."

**This requires Orchestrator action. Do NOT attempt to fix this yourself.**

**Immediate steps**:

1. Screenshot the error
2. Go to Etsy > Account > Overview and check for any red banners or notifications
3. Screenshot any account warnings
4. Post to Discord #alerts:
   ```
   🚨 ESCALATION: Etsy account issue detected
   Error: [Copy exact error]
   Time: [TIME] UTC
   Action taken: None (account-level issue)
   ```
5. Continue with the other 7 listings if possible (you may be able to publish some even if one listing has an error)

**Fallback**: If Etsy is completely blocked, use Gumroad instead:
- Go to gumroad.com
- Create a free product listing for the Zone Cards
- Set price to $5–15
- Upload PDF
- Publish
- Takes 10–15 minutes
- Update Kit email link to point to Gumroad instead of Etsy

---

## DT3: Social Media Post Not Going Live

**Symptom**: A scheduled social media post (Instagram, TikTok, Pinterest, or Reddit) did not auto-publish at the scheduled time.

**Discovery checkpoints**: 
- Instagram/TikTok: 09:30 and 10:30 UTC
- Pinterest: 11:00 UTC
- Reddit: 14:00 UTC

---

### DT3 Decision Tree

```
Check the platform directly (not the scheduler):
       |
       v
Is the post visible on the platform?
       |
    YES → Scheduler log is just delayed. Done. No action needed.
       |
    NO → Check: Did the scheduler queue the post?
           |
    YES → Did you get an error message in the scheduler?
           |
    YES → Platform auth failed. Go to DT3-A: Re-authenticate (below)
       |
    NO → Something else failed. Go to DT3-B: Manual Post (below)
           |
    NO → Post was never scheduled. User error. Go to DT3-B: Manual Post
```

---

### DT3-A: Re-authenticate Platform in Scheduler

**Time to execute**: 5 minutes per platform

**Steps for Instagram (via Buffer)**:

1. Open Buffer.com
2. Click "Channels" or "Social Accounts"
3. Find Instagram
4. If there is a "Reconnect" button or red error badge → Click it
5. You will be redirected to Instagram login
6. Log in with your Seedwarden Instagram credentials
7. Instagram will ask for permission (click "Authorize")
8. Return to Buffer. Instagram should now show "Connected" ✓
9. Retry the scheduled post:
   - Find the post in Buffer queue
   - Click the three-dot menu
   - Click "Send Now" or "Publish Immediately"

**Steps for TikTok (via TikTok app)**:

1. Open TikTok app on your phone
2. Go to Profile > Creator Center (or three-dot menu)
3. Look for "Schedule" or "Scheduled videos"
4. Is your video listed as "Scheduled"?
   - **YES**: Click the video and try to publish it manually
   - **NO**: The video was never uploaded. Use DT3-B: Manual Post
5. If there is an auth error: Log out of TikTok and log back in
6. Return to TikTok Creator tools and try scheduling again

**Steps for Pinterest (via Pinterest app)**:

1. Open Pinterest.com
2. Go to Profile > Creator tools > Scheduled pins
3. Is your pin listed?
   - **YES**: Click it and try to publish manually
   - **NO**: The pin was never scheduled. Use DT3-B: Manual Post
4. If there is a "Board not found" error: You may need to create the board first. See DT3-B.

**Steps for Reddit (direct post)**:

1. Open Reddit
2. Go to your profile > Saved posts or Submitted
3. Is your post in "Scheduled" status?
   - **YES**: Click the post and try to publish it manually (if Reddit allows). If not, just delete it and repost manually.
   - **NO**: Post was never saved. Use DT3-B: Manual Post

---

### DT3-B: Manual Post

**Time to execute**: 5–10 minutes per platform

**When to use**: Scheduler failed and needs manual recovery, or you want a clean slate.

**Instagram Manual Post**:

1. Open Instagram app (or web)
2. Click "Create" (+ icon)
3. Select the image/video from mockups folder
4. Write the caption (copy from LAUNCH_DAY_STATUS_TEMPLATE.md or social calendar Day 30)
5. Add location tag if applicable
6. Click "Share"
7. Confirm post is live by viewing your profile feed

**TikTok Manual Post**:

1. Open TikTok app
2. Tap the + (create) icon at bottom
3. Select the video from your files
4. Add caption (copy from social calendar Day 30)
5. Add hashtags (#Zone #Seedwarden #Gardening etc.)
6. Tap "Post"
7. Confirm post is live by checking your profile

**Pinterest Manual Post**:

1. Open Pinterest.com
2. Go to your Seedwarden board (if it doesn't exist, create it: Boards > Create board, name: "Seedwarden Zone Cards", set to public)
3. Click "Create" or the pin button
4. Upload the image
5. Add caption/title from social calendar
6. Add description and URL (link to Etsy listing)
7. Select the correct board ("Seedwarden Zone Cards")
8. Click "Save"
9. Confirm the pin is on your board

**Reddit Manual Post**:

1. Open Reddit
2. Go to r/vegetablegardening
3. Click "Create post"
4. Title: "[Zone] Hardiness Quick-Start Cards for [Crop]" (from social calendar Day 30)
5. Post type: Link
6. URL: [Your Bitly link]
7. Flair: "Resource" or "Educational" (if available)
8. Click "Post"
9. Confirm post is visible in the subreddit's new section

**Document in log**: "Social manual post: [PLATFORM] published at [TIME] UTC due to scheduler failure."

---

## DT4: Instagram Reach Very Low (New Account)

**Symptom**: Instagram post has been live for 2+ hours but shows only 10–30 impressions (very low reach).

**Discovery checkpoint**: 11:00 UTC or later

**Important context**: Instagram organic reach for new accounts (under 100 followers) is typically 20–100 impressions on first posts. This is normal, not a failure.

---

### DT4 Decision Tree

```
Is your Seedwarden Instagram account new (created in May 2026)?
       |
    YES → Low reach is EXPECTED. Do not panic.
           This is how Instagram works for new accounts.
           Organic reach will grow as you post more.
           Go to DT4-A: Normal New Account (below)
       |
    NO → Account is established (>100 followers, multiple posts)
           Low reach may indicate:
           - Post didn't get pushed to followers
           - Post violates community guidelines
           - Instagram algorithm is limiting reach
           Go to DT4-B: Established Account Low Reach (below)
```

---

### DT4-A: Normal New Account — Do Not Intervene

**What's happening**: Instagram is showing your post to a small percentage of followers because your account is new and untrusted. This is normal.

**Expected reach curve for new accounts**:
- Hour 1: 5–15 impressions
- Hour 2: 10–30 impressions
- Hour 4: 30–100 impressions
- Hour 8: 100–300 impressions
- Hour 24: 200–500 impressions
- Day 3: 500–1,000+ impressions (as other users share, and Instagram has more trust)

**What to do**:
- Do NOT change the post
- Do NOT delete and repost (this resets engagement metrics)
- Do NOT boost with paid ads yet (wait until Day 3)
- Continue posting daily (Days 2–7 per calendar). More posts = Instagram trusts your account more
- By Day 7, you should see 1,000+ impressions per post

**Check again at**: 18:00 UTC (full 9 hours). Reach should be 100+ by then.

---

### DT4-B: Established Account Low Reach — Investigate

**Steps**:

1. Open the post on Instagram directly
2. Check the comments: Are there any angry comments or rule-breaking reports?
   - If yes: Instagram may have shadowbanned the post for violating guidelines. The post is still there, but reach is suppressed.
3. Check Instagram Help > Community Guidelines. Did your post violate anything (spam, misleading, promotional)?
   - If yes: Delete the post and repost with toned-down messaging
   - If no: Continue
4. Check Instagram account status: Settings > Account > Instagram account status. Is there a warning?
   - If there is a warning: Follow Instagram's instructions to fix the issue
   - If not: Continue
5. Your reach is genuinely low. This happens sometimes due to algorithm variance.

**Decision**: Continue as planned. Sometimes posts have lower reach. Tomorrow's posts may perform better. This is not a failure.

---

## DT5: TikTok Video Getting 0–10 Views

**Symptom**: TikTok video has been live for 4+ hours but only has 5–10 views.

**Discovery checkpoint**: 14:00 UTC or later

**Important context**: TikTok is slower to ramping than Instagram on Day 1, especially for new accounts. It is normal.

---

### DT5 Decision Tree

```
Is your Seedwarden TikTok account very new (created in May 2026)?
       |
    YES → Low views are EXPECTED. Do not intervene.
           TikTok often suppresses new creator videos initially.
           Views will accelerate over 24–48 hours.
           Go to DT5-A: New Account (below)
       |
    NO → Account has history. Low views are unusual.
           Go to DT5-B: Established Account (below)
```

---

### DT5-A: New TikTok Account — Normal Startup Phase

**What's happening**: TikTok's For You Page (FYP) algorithm is testing your content with a small subset of users first. If it passes (watch time, likes, shares), views accelerate. This can take 4–24 hours.

**Expected view curve for new TikTok accounts**:
- Hour 1: 2–10 views
- Hour 4: 5–50 views
- Hour 12: 50–200 views
- Hour 24: 200–1,000+ views (if video performed well)

**What to do**:
- Do NOT delete and repost (TikTok algorithm penalizes deletion)
- Do NOT boost with paid ads yet (wait to see organic performance)
- Continue posting daily (Days 2–7). More videos = TikTok trusts your account more
- Engage with comments when they arrive (reply authentically to boost engagement)

**Check again at**: 18:00 UTC (8+ hours). Views should be 50+ by then.

---

### DT5-B: Established TikTok Account Low Views — Investigate

**Steps**:

1. Open the video on TikTok
2. Check the captions and comments: Did you write anything misleading or spam-like?
   - If yes: Edit the caption to be clearer and more authentic
3. Check video quality: Is the audio clear? Is the video properly formatted (not blurry, correctly oriented)?
   - If no: Delete and repost a corrected version
4. Check engagement: Are there comments? Likes?
   - If zero: This is unusual. Video may be shadowbanned. Delete and repost.
   - If yes: Video is reaching people; views will accelerate soon.

**Decision**: Do NOT panic. Sometimes videos perform slower on day 1. Proceed normally.

---

## DT6: Reddit Post Downvoted or No Engagement

**Symptom**: Reddit post has been live for 6+ hours and has negative score (downvotes > upvotes) or zero comments.

**Discovery checkpoint**: 18:00 UTC or later

---

### DT6 Decision Tree

```
What is the current score (upvotes - downvotes)?
       |
    POSITIVE (>0) → Post is doing fine.
                     Comments may arrive overnight (Reddit traffic is global).
                     Do NOT delete.
                     Go to DT6-A: Let It Mature (below)
       |
    ZERO or NEGATIVE → Check: Does the post look promotional or spammy?
                         |
                    YES → Post may violate r/vegetablegardening rules.
                          Go to DT6-B: Repost in Different Community (below)
                         |
                    NO → Sometimes Reddit users downvote for unclear reasons.
                          Go to DT6-A: Let It Mature (below)
```

---

### DT6-A: Let Post Mature

**What's happening**: Reddit posts often start with downvotes, then recover as different user groups see them (Reddit has global audience, traffic peaks at different times).

**Expected Reddit curve**:
- Hour 1: 0–5 upvotes (initial spike from your network)
- Hour 4: 0–20 upvotes (or downvoted if community doesn't like it)
- Hour 12: 5–50 upvotes (second wave of visibility)
- Hour 48: 10–100+ upvotes (if post gained traction)

**What to do**:
- Do NOT delete the post (deletion flags as spam to mods)
- Do NOT repost the same content (post again with different framing on Day 2 if you want)
- Engage with comments when they arrive (reply to questions authentically)
- Do NOT be promotional in replies (Reddit hates self-promotion)

**Check again at**: Day 2 morning (24 hours). Upvote score typically stabilizes by then.

---

### DT6-B: Repost in Different Community

**When to use**: Post has been negative or zero engagement for 24 hours and is not recovering.

**Steps**:

1. Leave the original post up (do NOT delete)
2. Choose a different subreddit:
   - r/foraging (750K members, specifically about wild plants) — RECOMMEND
   - r/homesteading (500K members, about self-sufficient living) — GOOD
   - r/gardening (general, largest, 4M+ members) — TRY IF OTHERS FAIL
3. Go to the new subreddit
4. Click "Create Post"
5. Use slightly different framing than the original:
   - Original: "Zone Card Quick-Start Guides" (link post)
   - New: "I built a free guide for [zone] gardening — sharing with the community" (personal framing, image post instead of link)
6. Use the image version of one zone card (PNG from mockups folder) instead of a link
7. In the caption, mention the Bitly link naturally: "...check out the full guides here: [link]"
8. Post
9. Engage naturally with any comments

**Document in log**: "Reddit repost: r/vegetablegardening (original) underperformed. Reposted to r/foraging (image format) at [TIME] UTC."

---

## DT7: GA4 Shows Zero Pageviews

**Symptom**: By 14:00 UTC, GA4 Real-Time shows 0 pageviews (expected is 100+).

**Discovery checkpoint**: 14:00 UTC

---

### DT7 Decision Tree

```
Open GA4 > Real-Time > Overview:
       |
       v
Do you see ANY events at all?
       |
    YES, I see events → But are they pageview events?
                        |
                      YES → GA4 is working! Zero pageviews is a
                            different issue (low traffic).
                            Do NOT escalate. Proceed normally.
                      |
                      NO → GA4 is firing custom events but not pageviews.
                            Configuration issue.
                            Go to DT7-A: Check GA4 Tracking Code (below)
       |
    NO, zero events → Tracking is completely broken.
                      Go to DT7-B: Verify GA4 ID (below)
```

---

### DT7-A: Check GA4 Tracking Code

**Time to execute**: 10 minutes

**Steps**:

1. Open a Seedwarden Etsy listing in incognito browser (important: incognito so you're not already logged in)
2. Visit the page
3. Right-click > "View page source"
4. Search (Ctrl+F) for "gtag" or "GA4" or "G-"
5. **Do you see the tracking code?** (It should look like: `gtag('config', 'G-XXXXXXXXXX')`)
   - **YES**: Tracking code is installed. Firing events correctly.
   - **NO**: Tracking code is missing. This is the problem.

**If tracking code is missing**:

1. Go to the Etsy listing HTML/source
2. Add the GA4 tracking code to the `<head>` section (see TRACK_B_ANALYTICS_SETUP_DISCORD_AND_GA4.md for the code)
3. Save and verify code is now present
4. Wait 5 minutes for GA4 to register new events
5. Retest: Open Etsy listing in incognito, wait 60 seconds, check GA4 Real-Time > Events

---

### DT7-B: Verify GA4 Measurement ID

**Time to execute**: 10 minutes

**Steps**:

1. Go to Etsy Shop Manager > Settings > Options > Web Analytics
2. Copy the GA4 Measurement ID (should look like `G-XXXXXXXXXX`)
3. Go to GA4 Admin (gear icon, bottom left) > Property > Property Settings
4. Find the GA4 Measurement ID in Property Settings
5. **Do the two IDs match exactly?** (One character wrong = no tracking)
   - **YES**: IDs match. Re-enter the ID in Etsy Shop Manager to refresh the connection.
   - **NO**: IDs don't match. Check which one is correct.

**If IDs don't match**:

1. The GA4 ID in Etsy Shop Manager is outdated or wrong
2. Go back to Etsy Shop Manager
3. Delete the incorrect ID
4. Copy the correct ID from GA4 Admin and paste it into Etsy Shop Manager
5. Click "Save"
6. Wait 5 minutes
7. Retest: Open Etsy listing in incognito, wait 60 seconds, check GA4 Real-Time

**If GA4 tracking is still broken after 15 min**:

- This is a secondary metric. Do NOT pause launch day.
- Document the issue: "GA4 tracking broken [reason]. Primary metric is Etsy sales data."
- Focus on Etsy metrics (which you can see in Etsy Shop Manager > Orders)
- Escalate GA4 issue after launch day (Day 2 or later)

---

## DT8: Email List Shows Zero Subscribers

**Symptom**: Kit shows "List is empty" when trying to send broadcast, or broadcast delivered to 0 recipients.

**Discovery checkpoint**: 12:00–12:05 UTC

---

### DT8 Decision Tree

```
Kit broadcast delivery status:
       |
    DELIVERED TO 0 RECIPIENTS → Is this Day 1 of launch?
                                 |
                              YES → Expected! Your email list is new
                                    and grows from social sign-ups.
                                    Go to DT8-A: Day 1 Empty List (below)
                                 |
                              NO → How many days/weeks into launch?
                                    If >7 days: Something is wrong.
                                    Go to DT8-B: List Decay (below)
       |
    DELIVERED TO X SUBSCRIBERS → Good! Email outreach happened.
                                  List is growing. No action needed.
```

---

### DT8-A: Day 1 Empty List — Expected

**What's happening**: Your Kit email list is brand new. On Day 1 of launch, subscribers come from:
- Previous signups (if you had a landing page pre-launch): might have 1–10
- Social media sign-ups: typically 0 on Day 1 (people haven't signed up yet)

**Expected email list growth**:
- Day 1: 0–10 subscribers
- Day 2–3: 5–20 subscribers (social traffic drives sign-ups)
- Day 7: 20–50 subscribers (ongoing social reach)
- Day 14: 50–100+ subscribers (if social is growing)

**What to do**:

- **Do NOT wait to send launch email**: Send it to whoever is on your list (even if 0). It establishes the automation.
- **Use Gmail fallback** if Kit shows "Failed": Send the same email via Gmail BCC to any existing subscriber emails you have
- **Continue social outreach** (Days 2–7): This is where your email list growth comes from
- **Monitor list growth** on the metrics dashboard: your Day 2/3/7 checkpoint emails will go to a larger list

**Decision**: Proceed normally. This is not a failure.

---

### DT8-B: List Decay (Not Applicable for Day 1)

N/A for May 30 launch day. This applies to mature launches where the list should be growing but isn't.

---

## Escalation Guide: When to Stop Troubleshooting

**Escalate to Orchestrator when**:

1. **You've spent 15+ minutes on a single issue** using the decision tree steps and the problem persists
2. **You cannot find your issue in the decision trees** — it's something unexpected
3. **A failure affects multiple systems** simultaneously (e.g., Etsy + Kit + Instagram all fail)
4. **An account-level block** is detected (suspension, verification hold, etc.)
5. **You need a cost decision** (upgrade Kit to Creator plan, buy paid ads, etc.)

**How to escalate**:

1. Screenshot or copy the exact error
2. Note the time and which decision tree you used
3. Post to Discord #alerts:
   ```
   🚨 **ESCALATION REQUEST**
   Issue: [Brief description]
   Decision tree: [F1, DT2-A, etc.]
   Steps taken: [What you tried]
   Time: [TIME] UTC
   Screenshot: [Attached]
   
   Status: [PAUSED / DEGRADED / CONTINUING WITH WORKAROUND]
   ```
4. Wait for Orchestrator response before making major changes

---

*Prepared: May 27, 2026. Seedwarden Launch Operations.*
*Quick reference: LAUNCH_DAY_DECISION_TREE.md (one-pager)*
*Full execution guide: LAUNCH_DAY_HOUR_BY_HOUR_RUNBOOK.md*
