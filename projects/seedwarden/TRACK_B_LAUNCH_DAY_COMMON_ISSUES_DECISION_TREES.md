---
title: "Track B Launch Day Common Issues — Decision Trees"
date: 2026-05-30
version: 1.0
status: production-ready
purpose: "Six specific failure scenarios with 2–3 decision points each, leading to concrete actions. Use when a problem appears on launch day."
---

# Track B Launch Day Common Issues — Decision Trees
## Six Scenarios with Step-by-Step Resolution Paths

**How to use this document**: When something goes wrong on May 30, find the matching scenario below. Follow the decision tree. Each branch leads to specific actions (copy-paste ready, no interpretation needed).

---

## ISSUE 1: Email Bounce Rate Above 1% (Kit Delivery)

**Symptom**: Kit dashboard shows bounce rate >1% at 12:30 UTC, or you see "X addresses bounced" notification.

**Why this matters**: >2% bounce rate indicates list quality problem. May signal authentication issue (bad SMTP setup) or stale email list (addresses deleted by email providers). Does not necessarily stop the launch, but is a metric to track.

---

### Decision Tree — Email Bounce Rate Issue

```
START: Bounce rate > 1% at 12:30 UTC
│
├─ Is bounce rate < 2%?
│  │
│  ├─ YES (1–2% bounce)
│  │  └─ PROCEED. This is acceptable. Document in WORKLOG.md: "Bounce rate 1.5%, within acceptable range."
│  │
│  └─ NO (> 2% bounce)
│     │
│     └─ Check Kit delivery log: Click on broadcast > Stats > view "Delivery report"
│        │
│        ├─ Are most bounces "hard bounces" (permanent, invalid address)?
│        │  │
│        │  ├─ YES
│        │  │  └─ Diagnosis: Your subscriber list has stale addresses. 
│        │  │     Action: Document in WORKLOG.md. Remove hard-bounced addresses from Kit 
│        │  │     subscriber list (Kit > Subscribers > filter bounced > delete).
│        │  │     Proceed with launch. Bounce rate will be lower for future sends.
│        │  │
│        │  └─ NO (mostly "soft bounces" or temporary failures)
│        │     │
│        │     └─ Diagnosis: Kit's sending server may have been throttled by email providers.
│        │        Symptoms: temporary delivery delays, not permanent bounce.
│        │        Action: (A) Kit will retry soft bounces automatically over 24 hours.
│        │        (B) If bounce rate is still >2% at 13:00 UTC, STOP and diagnose further:
│        │             - Check Kit's logs for authentication errors (DKIM, DMARC, SPF)
│        │             - If auth errors present: contact Kit support immediately
│        │             - If no auth errors: likely ISP throttling. Proceed with launch.
│        │        (C) Proceed with launch. Soft bounces do not indicate a blocker.
│        │
│        └─ Are bounce reasons showing "DNS / SPF / DKIM / DMARC failure"?
│           │
│           ├─ YES
│           │  └─ CRITICAL: Your email authentication is misconfigured. This will prevent 
│           │     delivery to major providers.
│           │     Action: STOP. Contact Kit support immediately for SPF/DKIM/DMARC setup.
│           │     Estimated resolution time: 30 minutes to 24 hours.
│           │     If resolution takes >30 min: switch to manual broadcast (see Issue Escalation below).
│           │
│           └─ NO (bounce reasons are just "invalid address", "mailbox full", etc.)
│              └─ Diagnosis: List quality issue, not authentication issue.
│                 Action: Proceed with launch. Document bounce rate in WORKLOG.md.
```

---

### Resolution Actions (Pick One Path)

**Path A: Bounce rate 1–2% — PROCEED**
1. Open WORKLOG.md
2. Log: "Kit broadcast bounce rate 1–2%. Acceptable. Proceed."
3. No action needed. Proceed to Hour 5 monitoring.

**Path B: Hard bounces > 2% — PROCEED with list cleanup**
1. Open Kit > Subscribers
2. Filter by "Bounced"
3. Select all bounced addresses
4. Click "Delete" (or "Remove")
5. Open WORKLOG.md
6. Log: "Removed [X] hard-bounced addresses from subscriber list. Bounce rate cleaned for future sends."
7. Proceed to Hour 5 monitoring

**Path C: Soft bounces, not auth failure — PROCEED**
1. Open WORKLOG.md
2. Log: "Soft bounces detected at 12:30 UTC. Kit will retry automatically. Proceeding."
3. Continue Hour 5 monitoring
4. Check bounce rate again at 13:00 UTC (may improve as Kit retries)

**Path D: SPF/DKIM/DMARC failure — CRITICAL, ACTIVATE FALLBACK**
1. This is a blocker. Email authentication is broken.
2. Action: Contact Kit support immediately (support.kit.com or chat)
3. While waiting for support response: prepare to switch to manual Gmail broadcast fallback
   - Open Gmail
   - Create new email with subject: "Seedwarden Zone Quick-Start Cards are live"
   - Paste email body from marketing/email-and-launch-plan.md
   - In "To" field, enter your own email
   - In "BCC" field, paste the Kit subscriber export list (must be exported first if not already done)
   - Wait for Kit support response (max 30 min). If resolved: cancel Gmail draft, use Kit.
   - If not resolved after 30 min: send Gmail broadcast immediately
4. Log in WORKLOG.md: "Email auth failure at 12:15 UTC. Activated manual Gmail fallback. Kit support escalation opened at [TIME]."

---

## ISSUE 2: Social Media Auto-Post Fails (Buffer/Later)

**Symptom**: At scheduled time, post does not appear on platform (Instagram/TikTok/Pinterest). Buffer/Later shows error status or "post failed."

**Why this matters**: Social posts are a major traffic driver. A failed post reduces reach by 25–35% vs. planned. Critical to recover quickly.

---

### Decision Tree — Social Media Post Failure

```
START: Post failed to publish at scheduled time
│
├─ Check platform: Where did it fail?
│  │
│  ├─ INSTAGRAM
│  │  │
│  │  └─ Is the post still showing "Scheduled" in Buffer > 2 min after scheduled time?
│  │     │
│  │     ├─ YES (stuck in Scheduled status)
│  │     │  │
│  │     │  └─ Is the Buffer/Later connection showing green or error?
│  │     │     │
│  │     │     ├─ GREEN (connection ok)
│  │     │     │  └─ Likely a temporary delay. Wait 5 more minutes, then check again.
│  │     │     │     If still Scheduled after 5 more min: proceed to MANUAL POST (below).
│  │     │     │
│  │     │     └─ RED / ERROR (connection broken)
│  │     │        └─ Instagram connection expired. Proceed to RECONNECT (below).
│  │     │
│  │     └─ NO (post is missing from Buffer queue, or shows "Failed")
│  │        └─ Post did not send. Proceed to MANUAL POST (below).
│  │
│  ├─ TIKTOK
│  │  │
│  │  └─ Buffer/Later does not post TikTok natively on free tier. Expected behavior: 
│  │     Buffer sends you a notification at scheduled time to upload manually.
│  │     │
│  │     ├─ Did you receive notification at scheduled time?
│  │     │  │
│  │     │  ├─ YES
│  │     │  │  └─ This is expected. Proceed to MANUAL UPLOAD (below).
│  │     │  │
│  │     │  └─ NO
│  │     │     └─ Buffer notification may have gone to email/app. Check:
│  │     │        (1) Email inbox for "Buffer reminder" email
│  │     │        (2) Buffer mobile app for notifications
│  │     │        If found: proceed to MANUAL UPLOAD
│  │     │        If not found: TikTok upload was missed. Proceed to MANUAL UPLOAD (do it now)
│  │
│  └─ PINTEREST
│     │
│     └─ Check Pinterest connection in Buffer > Settings > Accounts
│        │
│        ├─ GREEN (connected)
│        │  └─ Wait 10 minutes. Pinterest's indexing is slower than other platforms.
│        │     At 10 min: check your Pinterest profile. If pins are visible: success.
│        │     If still not visible at 10 min: proceed to MANUAL POST (below).
│        │
│        └─ RED / ERROR (connection broken)
│           └─ Pinterest connection expired. Proceed to RECONNECT (below).
│

End decisions: Proceed to one of 3 resolution paths below.
```

---

### Resolution Actions (Pick One)

**Action 1: RECONNECT Account**
(Use when connection shows RED/Error)

1. Open Buffer or Later
2. Go to Settings > Connected Accounts
3. Find the disconnected platform (Instagram / TikTok / Pinterest)
4. Click "Reconnect"
5. Authorize the platform (you will be redirected to Instagram/Pinterest login)
6. Log in using your platform credentials
7. Grant permission to Buffer/Later
8. Return to Buffer/Later
9. Confirm connection now shows GREEN
10. **Then proceed to MANUAL POST** (see below) to publish the scheduled post manually

**Action 2: MANUAL POST to Instagram**
(Use when post failed to publish or connection needs to be rebuilt)

1. Open Instagram app or Instagram.com
2. Click "+" (Create) or "New Post"
3. Upload the image from saved file: `marketing/lifestyle-photos/etsy-ready/[product]-slot4-lifestyle.jpg`
4. In caption field, paste the exact caption text from `TRACK_B_SOCIAL_SCHEDULING_TEMPLATES.md` May 30 Instagram section
5. Paste hashtags at the end of caption (all hashtags from template)
6. Click "Share" or "Post"
7. Confirm post appears on your profile feed within 30 seconds
8. Screenshot proof and save to WORKLOG.md
9. Log in WORKLOG.md: "Instagram launch post published manually at [TIME] UTC due to Buffer failure"

**Action 3: MANUAL UPLOAD to TikTok**
(Use when Buffer notification was received or missed)

1. Open TikTok app on phone
2. Click "+" (Create)
3. Click "Upload" (don't film new video)
4. Select video file from camera roll: `marketing/lifestyle-photos/etsy-ready/[product]-launch-reel.mp4`
   - If file is not in camera roll: AirDrop or email it to yourself, then save to camera roll
5. In caption field, paste caption text from `TRACK_B_SOCIAL_SCHEDULING_TEMPLATES.md` May 30 TikTok section
6. Add hashtags: `#foraging #heirloomseeds #wildedibles` (or use hashtags from template)
7. Click "Post" (do NOT use "Schedule" — we are posting now)
8. Confirm video appears on your profile within 30 seconds
9. Screenshot proof
10. Log in WORKLOG.md: "TikTok launch video posted manually at [TIME] UTC due to Buffer notification timing"

**Action 4: MANUAL POST to Pinterest**
(Use when post failed or connection is broken)

1. Open Pinterest.com
2. Click "+" or "Create"
3. Click "Create a pin"
4. Upload image: `marketing/lifestyle-photos/etsy-ready/[product]-pin-may30.jpg`
5. In description field, paste description from `TRACK_B_SOCIAL_SCHEDULING_TEMPLATES.md` May 30 Pinterest section
6. In "Destination URL" field, paste: Etsy listing URL (from Etsy Shop Manager)
7. Select board: "Heirloom Seeds & Growing Guides" (or create if not exists)
8. Click "Save" or "Publish"
9. Confirm pin appears on board within 1–2 minutes
10. Log in WORKLOG.md: "Pinterest pin posted manually at [TIME] UTC due to Buffer failure"

---

## ISSUE 3: Platform Login Issues (Instagram/TikTok/Pinterest Account Locked or 2FA Required)

**Symptom**: When trying to manually post or reconnect, platform asks for 2FA code, or account shows "suspicious activity detected" lock.

**Why this matters**: Locked account prevents manual post recovery. Must be resolved within minutes.

---

### Decision Tree — Account Login Issue

```
START: Cannot access platform account (locked, 2FA, or suspended)
│
├─ What is the specific error?
│  │
│  ├─ TWO-FACTOR AUTHENTICATION REQUIRED
│  │  │
│  │  └─ You have the device that receives 2FA codes?
│  │     │
│  │     ├─ YES (phone with authenticator app or SMS)
│  │     │  └─ Action: Retrieve 2FA code from phone > enter in login prompt > proceed.
│  │     │     Should take < 2 minutes. Then: proceed to MANUAL POST action (above).
│  │     │
│  │     └─ NO (lost phone, changed number, no access to 2FA device)
│  │        └─ BLOCKER. 2FA recovery via email typically takes 24 hours.
│  │           Action: Email platform support immediately requesting emergency account access.
│  │           Backup: use a different account (if you have admin access to a business account, use that).
│  │           If no backup account: note in WORKLOG.md and proceed. One failed post is recoverable.
│  │
│  ├─ ACCOUNT LOCKED: "Suspicious Activity Detected"
│  │  │
│  │  └─ Platform typically sends unlock link to email
│  │     │
│  │     ├─ Check email inbox (including spam folder)
│  │     │  │
│  │     │  ├─ Unlock link found?
│  │     │  │  │
│  │     │  │  ├─ YES
│  │     │  │  │  └─ Action: Click unlock link in email > complete verification > account restored.
│  │     │  │  │     Should take < 5 minutes. Then: proceed to MANUAL POST.
│  │     │  │  │
│  │     │  │  └─ NO (email not found in inbox or spam)
│  │     │  │     └─ Action: Log into platform's Help Center / Account Support.
│  │     │  │        Follow "Unlock My Account" process.
│  │     │  │        If resolution not available online: contact support chat (may have 2–4 hour wait).
│  │     │  │        Proceed without this platform if resolution takes >30 min.
│  │     │  │
│  │     │  └─ Did NOT check email
│  │     │     └─ Action: Check email immediately. Look for message from platform's no-reply address.
│  │     │
│  │     └─ Unlock link expired
│  │        └─ Action: Go to platform's help center > request new unlock link.
│  │           Typically arrives within 5 minutes.
│  │
│  └─ ACCOUNT SUSPENDED: "This account is suspended" or "This account is not available"
│     │
│     └─ This is permanent. Account may have violated platform's terms.
│        │
│        └─ Action: (A) Log into account settings / support to request review (may take 24–72 hours).
│           (B) If you have a business account: switch to that account for manual post.
│           (C) If no other account: note in WORKLOG.md that this platform is unavailable.
│               Proceed with remaining 2 platforms. One platform failure is not a launch blocker.
```

---

### Resolution Actions (Pick One)

**Path A: 2FA Code Available — UNLOCK IMMEDIATELY**
1. Open authenticator app or check SMS for 2FA code (usually 6 digits)
2. Go to platform login page (Instagram/TikTok/Pinterest)
3. Enter username and password
4. When prompted for 2FA code: enter the 6-digit code
5. Click "Verify"
6. You should be logged in within seconds
7. Proceed to MANUAL POST action above

**Path B: 2FA Unavailable, Lost Phone — CONTACT SUPPORT**
1. On platform login page, look for "Can't access two-factor?" or similar link
2. Click it
3. Follow the recovery flow (usually requires you to verify with email)
4. Recovery may take 15–30 minutes
5. If not recovered by 30 min: note in WORKLOG.md "Account [platform] 2FA unrecoverable. Proceeded without this platform."
6. Continue with remaining platforms

**Path C: Account Locked, Found Unlock Email — CLICK UNLOCK LINK**
1. Open email from platform support (check spam folder if needed)
2. Find the "Unlock Account" or "Verify Your Account" link
3. Click the link (you may be redirected to the platform)
4. Complete any additional verification if prompted (security questions, email confirmation, etc.)
5. You should see "Account Restored" or "Unlocked" message
6. Log back into platform
7. Proceed to MANUAL POST action above

**Path D: Account Locked, No Unlock Email — REQUEST NEW UNLOCK EMAIL**
1. Go to platform's login page
2. Click "Forgot password?" or "Help with login"
3. Follow "Unlock Account" or "Account Locked" process
4. Platform will send new unlock email (usually within 5 minutes)
5. Check email (including spam)
6. Click unlock link when received
7. Follow path C above

**Path E: Account Suspended — SWITCH TO BACKUP ACCOUNT OR SKIP PLATFORM**
1. Check if you have a business account or secondary account on this platform
2. If yes: log into that account and proceed to MANUAL POST using the backup
3. If no: note in WORKLOG.md "Primary account suspended on [platform]. Unable to post today."
4. Proceed with remaining platforms (Instagram and TikTok, for example; Pinterest suspended means skip Pinterest)

---

## ISSUE 4: Low Early Engagement (No Upvotes, No Views, No Comments)

**Symptom**: By 10:30 UTC, posts show <5 upvotes, <10 views, or zero comments. Significantly below expected.

**Why this matters**: May indicate algorithm suppression, spam filter, or wrong audience. Decision: continue or investigate.

---

### Decision Tree — Low Engagement

```
START: Engagement below expected by 10:30 UTC
│
├─ Check each platform's specific metric:
│  │
│  ├─ REDDIT: Post has 0 upvotes, 0 comments after 30 min
│  │  │
│  │  └─ Is post still visible on r/herbalism? (check your post history)
│  │     │
│  │     ├─ YES (post visible)
│  │     │  │
│  │     │  └─ Likely: Reddit algorithm has not yet promoted it, or audience has not seen it yet.
│  │     │     Reddit's "new" posts are not automatically shown to all members; they need upvotes
│  │     │     to break through. Your response to comments helps.
│  │     │     │
│  │     │     └─ Action: Post a thoughtful reply to any comments (even if just 1–2).
│  │     │        Wait until 11:00 UTC to check again. If still 0 upvotes and 0 comments at 11:00:
│  │     │        see "Post Removed" path below.
│  │     │
│  │     └─ NO (post not visible, missing from history)
│  │        │
│  │        └─ Post was removed by moderator or auto-filter.
│  │           │
│  │           ├─ Was there a removal notice in your inbox or on the post itself?
│  │           │  │
│  │           │  ├─ YES (mod removed for violating rules)
│  │           │  │  └─ Check the reason. Common reasons:
│  │           │  │     - "Promotional content" (if you used affiliate links or sales language)
│  │           │  │     - "Self-promotion" (if your post reads as an ad)
│  │           │  │     - "Off-topic" (wrong subreddit)
│  │           │  │     │
│  │           │  │     └─ Action: REPOST with different framing. See "Post Removed" action below.
│  │           │  │
│  │           │  └─ NO notice, just missing
│  │           │     │
│  │           │     └─ Post was caught by spam filter (likely due to URL or domain reputation).
│  │           │        Action: REPOST AS IMAGE. See "Post Removed" action below.
│  │
│  ├─ INSTAGRAM: Impressions < 10 by 10:30 UTC
│  │  │
│  │  └─ Is the post visible on your profile? (open your Instagram profile)
│  │     │
│  │     ├─ YES (post visible)
│  │     │  │
│  │     │  └─ Low impressions on new accounts is expected for first 24 hours. Instagram's
│  │     │     algorithm prioritizes accounts with established history.
│  │     │     │
│  │     │     └─ Action: Boost visibility by (A) replying to any comments immediately,
│  │     │        (B) posting an Instagram Story with link sticker pointing to the post,
│  │     │        (C) wait until 14:00 UTC to check again.
│  │     │        Impressions often grow 2–4x on Hours 2–6 of post as algorithm tests it.
│  │     │
│  │     └─ NO (post not visible)
│  │        │
│  │        └─ Post failed to upload or was removed.
│  │           │
│  │           ├─ Action: Check Instagram app for error notification. If error message visible:
│  │           │  note the error message. Try uploading again.
│  │           │  If still fails: try posting to Stories instead (less filtering).
│  │           │  Note in WORKLOG.md: "Instagram post failed after 2 attempts. Proceeded without IG."
│  │           │
│  │           └─ Action: Proceed with TikTok and Pinterest only.
│  │
│  └─ TIKTOK: Views < 10 by 10:30 UTC
│     │
│     └─ Normal for new TikTok accounts. TikTok's "For You" algorithm is slow on day 1 for new accounts.
│        │
│        └─ Action: (A) Proceed without changes. Views often grow 10–50x on Hours 2–6.
│           (B) Do NOT delete the video (deletion resets algorithm learning).
│           (C) Respond to any comments immediately (boosts engagement signals).
│           (D) Wait until 13:00 UTC to check again.
```

---

### Resolution Actions (Pick One)

**Path A: Reddit Post Removed, Repost as Image**
1. Screenshot one zone card PDF (or export as image)
2. Crop to show the header and first section clearly
3. Open Reddit
4. Go to r/herbalism
5. Click "Create Post"
6. Select "Images & Video"
7. Upload the zone card image
8. New title (personal framing): "I built a free Zone 5 quick-start card for herbalists — frost dates, varieties, and sourcing notes"
9. In post description: "Available for all zones 3–10. Free download: [GIST_URL]"
10. Click "Post"
11. Confirm post appears on r/herbalism
12. Log in WORKLOG.md: "Original Reddit post removed. Reposted as image post at [TIME] UTC"

**Path B: Instagram Low Impressions, Boost with Story & Engagement**
1. Open Instagram Stories
2. Click "+" to create new Story
3. Add text: "Zone guides are live in bio 🌱"
4. Add link sticker: paste your Gist URL or bio link
5. Post the Story
6. Then: reply to any comments on the main post (even generic replies like "Thanks for sharing!" or "Happy to help")
7. Log in WORKLOG.md: "Posted Instagram Story to boost main post visibility"
8. Check main post Insights again at 13:00 UTC (impressions typically grow 2–4x by 6 hours)

**Path C: Platform Post Failed After Multiple Attempts — DOCUMENT & PROCEED**
1. Log in WORKLOG.md: "Post failed on [platform] after [X] upload attempts at [TIME] UTC. Error: [error message if available]. Proceeded without this platform."
2. Continue with remaining platforms
3. Do NOT spend more than 15 min total on troubleshooting one platform
4. One failed platform does not stop the launch

---

## ISSUE 5: Bot or Spam Flag on Social Platform

**Symptom**: Post was published, but Instagram/TikTok/Pinterest immediately shows warning "This content may have violated our community guidelines" or "Limited reach" or "Content flagged for review."

**Why this matters**: Flagged content has 50–90% lower reach. May impact Day 1 engagement significantly. Recovery possible but limited.

---

### Decision Tree — Spam Flag

```
START: Post flagged for policy violation or limited reach
│
├─ Is the flag showing a specific reason?
│  │
│  ├─ "This content may have violated our community guidelines"
│  │  │
│  │  └─ Platform will review. Review typically takes 24–72 hours.
│  │     │
│  │     ├─ Action: (A) Do NOT delete the post (deletion = admission of violation).
│  │     │  (B) Click "Appeal" or "Request Review" (usually available in post options).
│  │     │  (C) Select reason: "This doesn't violate guidelines" or similar.
│  │     │  (D) Submit appeal.
│  │     │  (E) Platform will notify you in 24–72 hours if appeal approved (usually approved for false flags).
│  │     │  (F) In the meantime: post normally to other platforms.
│  │     │  (G) Log in WORKLOG.md: "Content flagged on [platform] at [TIME]. Appeal submitted."
│  │     │
│  │     └─ If appeal is approved (24–72 hrs later): reach is fully restored.
│  │        If appeal is denied: note in lessons learned for next launch.
│  │
│  ├─ "Limited reach" or "Reach reduced due to violating guidelines"
│  │  │
│  │  └─ Likely false trigger (spam filter sensitivity issue).
│  │     │
│  │     └─ Action: (A) Appeal the flag if available. Same process as above.
│  │        (B) Do NOT delete the post.
│  │        (C) Continue normal posting schedule (do not post to same platform again within 2 hours; space posts out).
│  │        (D) Log in WORKLOG.md: "Limited reach flag on [platform]. Appeal submitted if available."
│  │
│  └─ "Content is spam" or "Potential spam detected"
│     │
│     └─ This is a stronger flag. Usually caused by:
│     │  - Multiple identical posts in short time (cross-posting from Buffer)
│     │  - URL-heavy content (too many links)
│     │  - Account age (brand new account with instant high-engagement post)
│     │  │
│     │  └─ Action: (A) Appeal the flag and explain: "This is an educational resource. No commercial intent."
│     │     (B) Pause posting to this platform for 24 hours (do not post again today).
│     │     (C) Focus on other platforms for Day 1 reach.
│     │     (D) Resume posting on Day 2 (May 31) with single post, spaced out.
│     │     (E) Log in WORKLOG.md: "Spam flag on [platform]. Appeal submitted. Paused posting to this platform."

```

---

### Resolution Actions (Pick One)

**Path A: Dispute False Flag (Most Common Case)**
1. Go to the flagged post
2. Tap/click the three dots (more options)
3. Look for "Appeal decision," "Report," or "Request review" option
4. Select "Appeal decision" or "This doesn't violate guidelines"
5. Reason: "This is educational content about gardening. No commercial or misleading intent."
6. Submit appeal
7. Platform will review (usually 24–48 hours)
8. You'll receive notification when decision is made (usually "Appeal approved")
9. Once approved, post reach returns to normal
10. Log in WORKLOG.md: "Flag on [platform] appealed at [TIME] UTC. Awaiting review."

**Path B: Pause Platform Until Appeal Resolves**
1. Do NOT post to this platform for 24 hours
2. Continue posting normally to other platforms
3. On May 31, check if appeal was approved
4. If approved: resume normal posting schedule
5. If not approved: do not post to this platform for 7 days (platform may have account-level restriction)
6. Log in WORKLOG.md: "Paused [platform] posting until appeal resolved"

**Path C: Cross-Posting Related — Space Out Posts**
(Use if you suspect the flag was triggered by cross-posting identical content)
1. If you have multiple posts scheduled for the same day on the same platform:
   - Stagger them 2–3 hours apart instead of posting all at once
2. Variation in captions: if you did post the same image+caption to multiple platforms, create slightly different captions for each platform
3. Example: Instead of identical copy on Instagram/TikTok/Pinterest, adjust captions to be platform-appropriate
4. Log in WORKLOG.md: "Adjusted posting strategy to avoid cross-post spam flag. Spaced posts [X] hours apart."

---

## ISSUE 6: Analytics Not Populating (Kit, Etsy, Google Analytics)

**Symptom**: At 10:00–11:00 UTC, analytics dashboards show no data, zeros, or "connecting..." status. Email open rate not visible, Etsy orders not showing, GA4 not recording events.

**Why this matters**: Without analytics, you cannot measure launch success or make decisions. However, this is usually a display issue, not a data-loss issue. Data is being collected; dashboards just lag.

---

### Decision Tree — Analytics Not Populating

```
START: Analytics dashboard showing no data / zeros / connecting status
│
├─ Which analytics are not working?
│  │
│  ├─ KIT EMAIL ANALYTICS (broadcast open rate, click rate not visible)
│  │  │
│  │  └─ Kit's stats typically update with 5–10 minute lag.
│  │     │
│  │     ├─ Is the broadcast still showing "Sending" status?
│  │     │  │
│  │     │  ├─ YES
│  │     │  │  └─ Broadcast is still being sent. Stats will not populate until send completes.
│  │     │  │     Broadcast completes within 10–15 minutes for lists <1000 subscribers.
│  │     │  │     Action: Wait 10 minutes, then refresh. Stats will appear.
│  │     │  │
│  │     │  └─ NO (status shows "Sent")
│  │     │     │
│  │     │     └─ Broadcast send complete. Stats should be visible.
│  │     │        │
│  │     │        ├─ Refresh the page (Cmd+R or Ctrl+R)
│  │     │        │  │
│  │     │        │  ├─ YES (stats visible after refresh)
│  │     │        │  │  └─ Success. Dashboard lag issue, now resolved.
│  │     │        │  │
│  │     │        │  └─ NO (still blank)
│  │     │        │     │
│  │     │        │     └─ Try logging out and logging back into Kit
│  │     │        │        (session may be stale, preventing data load).
│  │     │        │        │
│  │     │        │        └─ If still blank: data IS being collected (emails are arriving).
│  │     │        │           Dashboards are just lagging. Wait 15 minutes and check again.
│  │     │        │           This does not prevent launch success; just prevents real-time monitoring.
│  │
│  ├─ ETSY ORDERS NOT SHOWING (Shop Manager > Orders shows 0)
│  │  │
│  │  └─ Orders should appear in Shop Manager within 30 seconds of purchase.
│  │     │
│  │     ├─ Is it possible no orders have been received yet? (check: is it before 13:00 UTC?)
│  │     │  │
│  │     │  ├─ YES (early in launch)
│  │     │  │  └─ No orders yet is normal. Email open rate is still ramping up.
│  │     │  │     Check again at 13:00 UTC. First order typically arrives within 2–4 hours post-email.
│  │     │  │
│  │     │  └─ NO (past 13:00 UTC, email has been sent >1 hour ago)
│  │     │     │
│  │     │     └─ If orders have been received (you received email notifications):
│  │     │        Check Etsy Shop Manager again by:
│  │     │        (A) Refresh page
│  │     │        (B) Log out, log back in
│  │     │        (C) Try a different browser
│  │     │        Data lag at Etsy is unusual but possible during high-traffic times.
│  │     │
│  │     └─ If no orders at all by 13:00 UTC:
│  │        See "ZERO ORDERS RECEIVED" section in Issue escalation below.
│  │
│  └─ GOOGLE ANALYTICS (GA4 not showing events / bounce data / goal conversions)
│     │
│     └─ GA4 has up to 24-hour reporting delay, but real-time data should show within 5 minutes.
│        │
│        ├─ Check GA4 Real-Time dashboard (Reports > Real-Time)
│        │  │
│        │  ├─ Any users showing in Real-Time view?
│        │  │  │
│        │  │  ├─ YES (users visible in real-time)
│        │  │  │  └─ Real-time data is flowing. Standard reports will populate within 24 hours.
│        │  │  │     This is expected GA4 behavior. Proceed without GA4 data for today.
│        │  │  │
│        │  │  └─ NO (0 users in real-time)
│        │  │     │
│        │  │     └─ GA4 tracking may not be installed correctly on your landing page/Etsy links.
│        │  │        │
│        │  │        ├─ Action: Open your Kit landing page in a browser.
│        │  │        │  Open browser DevTools (F12 or Cmd+Option+I).
│        │  │        │  Go to "Network" tab.
│        │  │        │  Scroll down to "google-analytics" requests.
│        │  │        │  If you see GA requests, GA is installed. Data should appear in real-time soon.
│        │  │        │  If you don't see GA requests, GA is not installed on this page.
│        │  │        │
│        │  │        └─ If GA not installed: you can proceed without GA data for today.
│        │  │           Do not try to install mid-launch (too much risk).
│        │  │           Install GA properly after launch.
```

---

### Resolution Actions (Pick One)

**Path A: Kit Stats Lag — WAIT 10 MINUTES AND REFRESH**
1. Close Kit dashboard
2. Take a 10-minute break
3. Reopen Kit > Broadcasts > [launch broadcast]
4. Refresh page (Cmd+R / Ctrl+R)
5. Stats should now be visible (open rate, click rate, delivery %)
6. If still blank: this is a display lag issue, not a data issue. Proceed. Data IS being collected.
7. Log in WORKLOG.md: "Kit analytics lag experienced. Refreshed at [TIME]. Stats populated."

**Path B: Etsy Orders Not Showing — REFRESH & VERIFY BROWSER SESSION**
1. Refresh Etsy Shop Manager (Cmd+R / Ctrl+R)
2. If still showing 0 orders: log out of Etsy
3. Close all Etsy tabs
4. Log back in
5. Navigate to Shop Manager > Orders & Shipping
6. Check if orders now appear
7. If still 0: no orders have been received yet (check time; is it still early in launch window?)
8. If time is >2 hours post-email send and still 0: check Etsy listings for visibility (see Issue 4 "zero orders" escalation below)

**Path C: GA4 Not Recording Events — CHECK REAL-TIME, THEN PROCEED**
1. Open Google Analytics > Real-Time
2. Check if any active users are visible
3. If yes: GA is working. Standard reports will populate within 24 hours. Proceed without live GA data.
4. If no: GA may not be installed on your landing page. Do not try to debug mid-launch.
5. Proceed with other analytics (Kit, Etsy). Install GA properly after launch.
6. Log in WORKLOG.md: "GA4 real-time data: [Y/N]. Proceeding with Kit/Etsy analytics."

---

## QUICK REFERENCE — ESCALATION CONTACTS

| Issue | Escalation | Response Time | Action |
|-------|-----------|----------------|--------|
| Email bounce >2% + auth error | Kit support (support@kit.com or chat at kit.co) | 30 min–2 hours | Contact immediately; prepare Gmail fallback |
| Social post failed | Platform support (Instagram, TikTok, Pinterest help centers) | 2–8 hours | Manual post as workaround; do not wait for support |
| Account locked / 2FA | Platform support | 5 min–24 hours | Use backup account if available; one platform failure is manageable |
| Content flagged for spam | Platform support (appeal process) | 24–72 hours | Appeal automatically; continue posting to other platforms |
| Analytics blank | Platform support (Kit, Etsy, GA) | 30 min–24 hours | Refresh page and wait; usually just lag, not a blocker |

---

*Document status: Production-ready. May 30, 2026.*
*Use this document when something goes wrong during launch day.*
*All decision trees lead to actions you can complete in <15 minutes.*
