---
title: "Phase 3 Week 1-2 Failure Recovery Procedures"
date: 2026-06-29
version: 1.0
status: production-ready
scope: Recovery procedures for 5 common failure modes during Week 1-2 execution
---

# Phase 3 Week 1-2 Failure Recovery Procedures

This document outlines recovery steps for common failures during Week 1-2 (June 29 – July 13). All procedures include: symptom description, root cause checklist, recovery steps, time cost, and escalation thresholds.

---

## FAILURE MODE 1: Email Send Fails / Bounces

**Severity**: MEDIUM (5-10% engagement impact if delayed 30-60 min)  
**Frequency**: Low (1-2 incidents per quarter typical)  
**Time to resolve**: 10-15 minutes (30-min delay for retry)

---

### Symptoms

- Kit dashboard shows error message: "Send failed — [error type]"
- Email appears as "Draft" or "Scheduled" but never "Sent"
- Kit returns API error (e.g., "Invalid API credentials", "Server error", "Rate limit exceeded")
- Email recipient list shows 0 or incorrect count
- Send button is disabled or grayed out

---

### Root Cause Checklist

**Check each item below**. Mark YES/NO for each. First YES you find is likely the root cause.

- [ ] **Kit API credentials expired or invalid**
  - How to check: Kit dashboard → Settings → Integrations → Check "Kit API status"
  - Status indicator: GREEN = valid, RED = invalid
  - Fix: Re-authenticate Kit account (Settings → Disconnect → Reconnect)

- [ ] **Recipient list empty or incorrect segment selected**
  - How to check: Broadcast composer → Segment dropdown → Verify "Phase_3_Interested" selected
  - Status: Should show [250-500] recipients in preview
  - Fix: Select correct segment from dropdown

- [ ] **Email template has formatting issues**
  - How to check: Open broadcast preview (Broadcast composer → "Preview" button)
  - Look for: Broken links [ETSY_LINK], missing images, HTML errors
  - Fix: Review email body for [BRACKETS] that weren't replaced

- [ ] **Kit server issues or platform downtime**
  - How to check: Kit Status page https://status.kit.co/
  - Status: Look for yellow/red indicators ("Operational Issue", "Partial Outage")
  - Fix: Wait 15-30 min, retry send (server issues usually resolve within 30 min)

- [ ] **Send time conflict (trying to send during scheduled send window)**
  - How to check: Broadcast editor → Check "Scheduled for [time]" field
  - Status: If sending NOW (not scheduled), should complete immediately
  - Fix: If scheduled, wait for scheduled time to pass

---

### Recovery Steps

**Step 1: Verify the error (2 min)**

1. Open Kit dashboard: https://kit.co/account/broadcasts
2. Find the failed broadcast (name: "Women's Health Email 1 — Jun 29" or similar)
3. Click broadcast → Click "History" or "Details" tab
4. Screenshot the error message
5. Copy error text: "Error: [exact error message]"

**Step 2: Diagnose using checklist above (3-5 min)**

1. Go through checklist above
2. For each YES item, note the fix
3. Most common: Segment not selected or API credential invalid

**Step 3: Fix the issue (5-10 min)**

1. **If API credentials invalid**: 
   - Kit dashboard → Settings → Integrations
   - Click "Disconnect" (next to Kit)
   - Click "Connect" and re-authenticate with Kit account
   - Wait 2 min for re-sync
   - Return to broadcast and retry send

2. **If segment empty or wrong**:
   - Broadcast editor → Segment dropdown
   - Select correct segment ("Phase_3_Interested")
   - Verify [250-500] recipients shown
   - Retry send

3. **If email body has formatting issues**:
   - Broadcast editor → Click "Preview" button
   - Look for broken links or placeholder text [ETSY_LINK]
   - Edit email body → Replace [ETSY_LINK] with actual Etsy URL
   - Retry send

4. **If Kit server down**:
   - Wait 15-30 min
   - Retry send at [original time + 30 min]
   - If still failing after 30 min: escalate to user

**Step 4: Retry send (2-3 min)**

1. Broadcast editor → Click "Send Now" (if immediate send)
2. OR set new scheduled time if original time passed
3. Wait 5 seconds for send to complete
4. Screenshot "Sent" confirmation page
5. Log in PHASE_3_EXECUTION_LOG.md: "Email resent at [time]. Original send failed [reason]. Retry successful."

**Step 5: Verify delivery (2 min)**

1. Wait 30 min
2. Return to Kit dashboard
3. Find broadcast → Click "Analytics" or "Details"
4. Verify: Delivered count > 0 (target: 95%+ of recipients)
5. If still shows 0 delivered: escalate to user

---

### Success Criteria

- [ ] Broadcast status changed from "Draft" / "Failed" to "Sent" or "Scheduled"
- [ ] Delivered count > 0 (verify 95%+ of intended recipients)
- [ ] Screenshot of "Sent" confirmation saved
- [ ] Delay: 30-60 min from original send time
- [ ] Email engagement impact: -5-10% (later send slightly lower open rate)

---

### Escalation Threshold

**Escalate to user if**:
- Error persists after retry attempt
- More than 25% of intended recipients failed to deliver
- Time since original send > 90 min (too late to recover open rate on same day)

**Escalation message**:
```
Email send failed and could not be recovered.

Bundle: [Women's Health / Respiratory]
Email #: [1 / 2 / 3]
Intended send time: [09:00 ET, Jun 29]
Error: [exact error from Kit]
Retry attempts: 2 (unsuccessful)
Recommended action: [Manual send via Kit UI / Email list export + manual send via Gmail / Reschedule to next day with diagnostic]

Current time: [time]
Recipient count affected: [number]
Estimated engagement impact: -10-20%
```

---

## FAILURE MODE 2: Social Post Upload Fails

**Severity**: MEDIUM-HIGH (20-30% engagement impact due to algorithm timing)  
**Frequency**: Low (1-2 incidents per quarter typical)  
**Time to resolve**: 5-15 minutes (if image issue) or reschedule to next day

---

### Symptoms

- Instagram/LinkedIn shows error: "Image too large", "Unsupported format", "Upload failed"
- Post is stuck in "Uploading" status for >30 sec
- Platform app crashes during image upload
- Image appears corrupted or distorted in preview
- Caption didn't save; post shows no text
- Platform is entirely inaccessible (Instagram/LinkedIn down)

---

### Root Cause Checklist

- [ ] **Image too large (>10 MB) or wrong resolution**
  - Check: Open image in file explorer → Properties → Size
  - Instagram optimal: 1080×1350px (vertical), <5 MB
  - LinkedIn optimal: 1200×627px (horizontal), <5 MB
  - Fix: Resize image in Canva or image editor

- [ ] **Image format not supported**
  - Supported formats: JPG, PNG, GIF, WebP
  - Not supported: TIFF, BMP, raw camera files
  - Fix: Export image as PNG or JPG from Canva

- [ ] **Platform API timeout or temporary down**
  - Check: Instagram Status page https://status.instagram.com/ or LinkedIn Status https://www.linkedin.com/official/careers
  - Look for: "Operational Issue", "Partial Outage", red indicators
  - Fix: Wait 10-15 min, retry

- [ ] **Caption has forbidden characters or links**
  - Instagram: Certain Unicode characters can cause issues; too many links can trigger spam filter
  - LinkedIn: Excessive hashtags or URLs can trigger moderation
  - Fix: Review caption → Remove problem characters or URLs → Retry

- [ ] **App cache corruption**
  - Symptom: App crashes consistently when uploading, works in browser
  - Fix: Clear app cache (Settings → Storage → Clear Cache) OR use web version

---

### Recovery Steps

**Step 1: Verify the error (2 min)**

1. Read error message on screen
2. Screenshot error message (for documentation)
3. Note platform: Instagram or LinkedIn
4. Copy error text: "[exact error]"

**Step 2: Diagnose using checklist above (3-5 min)**

1. Go through root cause checklist
2. Note which item matches your error
3. Most common: Image too large OR platform API timeout

**Step 3: Fix the issue (3-10 min)**

**If image too large or wrong resolution**:
1. Open Canva (if original source) or image editor
2. Check image dimensions:
   - Instagram: Should be 1080×1350px (portrait)
   - LinkedIn: Should be 1200×627px (landscape)
3. Export image as PNG (or JPG, compressed)
4. Verify file size < 5 MB
5. Retry upload

**If image format wrong**:
1. Download image from current location (screenshot or export)
2. Open in image editor (macOS Preview, Windows Photos, or online https://pixlr.com/)
3. Export as PNG (File → Export → PNG format)
4. Retry upload

**If platform API timeout**:
1. Wait 10 minutes (platform may be recovering)
2. Check platform status page:
   - Instagram: https://status.instagram.com/
   - LinkedIn: Check for any service advisories
3. If status shows "Operational Issue": wait 15-30 min
4. If status shows "All operational": retry upload

**If caption has problem characters**:
1. Open Instagram/LinkedIn post composer
2. Copy caption into text editor (Google Docs, Notepad)
3. Look for unusual characters (emoji, non-ASCII text, excessive links)
4. Simplify caption: remove extra emoji, convert links to "link in bio" format
5. Retry upload

**If app cache corrupted**:
1. Instagram/LinkedIn app (mobile):
   - Settings → Storage → Clear Cache (do NOT clear data)
   - Close and reopen app
   - Retry upload
2. Web version (browser):
   - Open https://www.instagram.com/ or https://www.linkedin.com/
   - Try uploading from browser instead of app

**Step 4: Retry upload (5-10 min)**

1. Open Instagram or LinkedIn
2. Start new post (+ Create button)
3. Upload resized/fixed image
4. Copy caption (from PHASE_3_EXECUTION_AUTOMATION_TEMPLATES.md or checklist)
5. Add hashtags
6. Set post time: 10:00 ET (14:00 UTC for Instagram) OR 15:00 ET (19:00 UTC for LinkedIn)
7. Post immediately OR schedule for correct time
8. Wait 10 sec for success confirmation
9. Screenshot post preview and post URL

**Step 5: Verify post live (2 min)**

1. Wait 5 min for post to appear on feed
2. Open Instagram/LinkedIn profile → find post
3. Verify post is visible with correct caption and image
4. Copy post URL from share button
5. Log in PHASE_3_EXECUTION_LOG.md: "Post rescheduled to [time]. Original upload failed [reason]. Retry successful. URL: [link]"

---

### Success Criteria

- [ ] Post successfully uploaded and visible on feed
- [ ] Image displays correctly (no distortion, correct size)
- [ ] Caption visible with all hashtags
- [ ] Post URL copied and logged
- [ ] Screenshot of live post saved
- [ ] Time delay: <30 min from original post time (within peak engagement window)

---

### Escalation Threshold

**Escalate to user if**:
- Post cannot be uploaded to any social platform (multiple platforms down)
- Time since original post time > 60 min (missed peak engagement window)
- Image corrupted after retry (need backup image from contractor)

**Escalation message**:
```
Social post upload failed and could not be recovered on time.

Platform: [Instagram / LinkedIn]
Post #: [1 / 2 / 3]
Bundle: [Women's Health / Respiratory]
Intended post time: [10:00 ET, Jun 29]
Error: [exact error message]
Retry attempts: 2 (unsuccessful)
Recommended action: [Reschedule post for next day, same time / Use backup image from Canva / Manual post via web]

Time since original: [minutes]
Engagement window impact: Missed peak hours (post will receive -20-30% less engagement if delayed >1 hour)
```

---

## FAILURE MODE 3: Contractor Unresponsive / Missed Deadline

**Severity**: HIGH (bundle launch may be delayed 1-2 days OR requires fallback content)  
**Frequency**: MEDIUM (1-2 contractors per 5-6 week cycle typical)  
**Time to resolve**: 4-24 hours (escalation to user) OR 2-4 hours (contingency content deploy)

---

### Symptoms

- Contractor doesn't respond to Jul 1 check-in by Jul 2 EOD (24-hour no-response window)
- Contractor responds but says "running late, will deliver by [date after launch]"
- Contractor deliverable delivered but quality is below standard (blurry photos, thin written content, etc.)
- Contractor disappears entirely (no response >48 hours)
- Deliverable count is lower than agreed (e.g., promised 10 photos, delivered 5)

---

### Root Cause Checklist

- [ ] **Contractor didn't receive check-in message**
  - Check: Confirm email/Slack/WhatsApp sent successfully (delivery receipt if available)
  - Fix: Resend via alternate platform (if email failed, try Slack; if Slack failed, try WhatsApp or phone)

- [ ] **Contractor personal emergency or schedule conflict**
  - Check: Wait for response or phone call to confirm
  - Common reasons: Illness, family issue, unexpected work conflict, power outage
  - Fix: Extend deadline by 1-2 days (if launch timeline allows) OR deploy contingency content

- [ ] **Contractor scope misalignment (thought deliverable was different)**
  - Check: Review original contract or onboarding message
  - Example: Contractor thought they were delivering 5 photos, contract says 10
  - Fix: Clarify expectation, agree on adjusted scope, extend deadline 1-2 days

- [ ] **Contractor payment hasn't been received**
  - Check: Ask contractor directly: "Did you receive payment for Week 1? When?"
  - Fix: Verify payment was sent in PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md, resend if needed

- [ ] **Contractor ghosting (intentional non-response)**
  - Check: >3 days no response despite multiple follow-ups
  - Fix: Mark as "non-performing", deploy contingency content, escalate to user for payment/contract decision

---

### Recovery Steps

**Timeline**: Jul 1 check-in → Jul 2 EOD (24-hour response window) → Jul 3 follow-up (if needed) → Jul 4 escalation (if still no response)

---

### Step 1: Initial Check-In (Jul 1, 12:00 UTC)

Send check-in message using PHASE_3_EXECUTION_AUTOMATION_TEMPLATES.md, Contractor Check-In Template:

```
Hi [Name],
Week 1 check-in — are your deliverables on track for [bundle] launch [date]?
Expected: [specific deliverable]
Deadline: [date]
Response needed by: [Jul 2, 12:00 UTC]
```

Log in PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md:
- Date sent: Jul 1, 12:00 UTC
- Deadline for response: Jul 2, 12:00 UTC (24 hours)
- Status: Awaiting response

---

### Step 2: Monitor Response (Jul 1-2)

**Jul 2, 12:00 UTC** (24 hours after initial check-in):
1. Check email/Slack/WhatsApp for contractor response
2. **If YES (contractor responded, on track)**:
   - Update PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md
   - Status: "Responded — on-track"
   - No action needed → proceed to Week 2
3. **If NO (no response)**:
   - Proceed to Step 3 (Follow-up)
4. **If YES BUT DELAYED (contractor says delivery will be late)**:
   - Proceed to Step 4 (Delay assessment)

---

### Step 3: Follow-Up (Jul 3, if no response by Jul 2 EOD)

Send follow-up message:

```
Hi [Name],

Quick follow-up — did you receive my message from Jul 1?

I need a status update on your [specific deliverable] for the [bundle] launch [date].
Please reply with:
1. Current status (complete / in progress / blocked?)
2. Expected delivery date
3. Any blockers or questions

Thanks,
Seedwarden
```

Log in PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md:
- Date sent: Jul 3
- Deadline for response: Jul 3, 12:00 UTC + 24 hours = Jul 4, 12:00 UTC
- Status: "Follow-up sent, awaiting response"

---

### Step 4: Delay Assessment (If contractor reports delay)

**Contractor says**: "I'll have photos ready by [date after launch], not [original date]"

**Decision flowchart**:

1. **Can bundle launch be delayed by 1-2 days?**
   - YES → Approve delay, adjust email/social schedule, extend contractor deadline
   - NO → Deploy contingency content (see Step 5)

2. **How much is deliverable late?**
   - 1-2 days late: Acceptable, proceed with delay
   - 3+ days late: Likely unacceptable, escalate to user

3. **Quality confirmation**: Ask contractor to send 1-2 sample items for preview
   - If samples are strong: approve delay
   - If samples are weak: escalate to user for contingency decision

**Update PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md**:
- Status: "Responded — delayed, [#] days behind schedule"
- New expected delivery: [contractor's new date]
- Approval: [YES / needs approval from user]

---

### Step 5: Escalation & Contingency (Jul 4, if no response after follow-up OR >3 days delay)

**Escalate to user immediately** with this message:

```
Contractor Status Escalation — Action Required

Contractor: [Name]
Week: [#]
Deliverable: [type — photos/written/video]
Original deadline: [date]
Status: [No response / Delayed [#] days]
Last contact: [date/time]
Response attempts: [Jul 1 check-in, Jul 3 follow-up, attempts to contact via [platform1/platform2]]

Decision needed:
1. Accept delay and extend to [new date]? (if contractor will deliver)
2. Proceed with contingency content (fallback images/copy)? (if contractor ghosting)
3. Hold payment / activate contract termination? (if severe delay)

Contingency content available in PHASE_3_CONTINGENCY_CONTENT_LIBRARY.md:
- Fallback images: [#] stock photos available
- Fallback testimonials: [#] template testimonials available
- Timeline to deploy: [#] hours

Awaiting your decision. Time-sensitive: [bundle] launches [date].
```

---

### Step 6: Deploy Contingency Content (If Needed)

**If user approves contingency**, proceed with fallback:

1. **Access contingency library**:
   - File: PHASE_3_CONTINGENCY_CONTENT_LIBRARY.md (if it exists)
   - Contains: Stock photos, template testimonials, template written content for each bundle

2. **Select fallback content**:
   - For missing photos: Use high-quality Wikimedia CC or contractor stock (see library)
   - For missing testimonials: Use template placeholder ("A reader from [Zone]...")
   - For missing written content: Use bundle email copy (already written)

3. **Deploy to social/email**:
   - Update Instagram post with fallback image
   - Add note to caption: "[Photo from Wikimedia CC, shared under CC BY-SA 3.0]" (if required)
   - Update any contractor bios/testimonials with fallback text

4. **Log deployment**:
   - PHASE_3_EXECUTION_LOG.md: "Contingency content deployed for Contractor [Name]. Reason: [no response / late delivery]. Fallback type: [photos / testimonials]."
   - PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md: Status marked "Contingency deployed — [date]"

---

### Success Criteria

- [ ] Contractor responded and confirmed on-track delivery
- [ ] OR delay assessed and user approved extended timeline
- [ ] OR contingency content successfully deployed (bundle launch not blocked)
- [ ] PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md updated with final status
- [ ] Time delay: 24-48 hours from initial check-in to resolution

---

### Escalation Threshold

**Escalate to user if**:
- Contractor unresponsive >48 hours after initial check-in
- Contractor delay >3 days beyond original deadline
- Contractor deliverable quality below standard (requires rework)
- Unable to deploy contingency content in time for launch

---

## FAILURE MODE 4: Email Engagement Low (<15% Open Rate)

**Severity**: MEDIUM (indicates targeting or messaging issue, correctable in Week 2)  
**Frequency**: LOW (3-5% of campaigns typical, only if targeting poor)  
**Time to resolve**: 24-48 hours (diagnostic investigation + optional A/B resend)

---

### Symptoms

- Email open rate <15% cumulative 4 hours after send (target: 22-28%)
- Open rate declining over time instead of rising (suggests deliverability issue, not just early-adopter timing)
- High bounce rate (>3% of sent)
- High spam complaint rate (>0.5% of opened)
- Manual check of personal email: email in spam folder, not inbox

---

### Root Cause Checklist

- [ ] **Email landed in spam folder (deliverability issue)**
  - Check: Send test email to personal account, check spam folder
  - Common causes: SPF/DKIM not configured, sender reputation new, too many links, recipient email system blocking
  - Fix: Check sender domain reputation (https://www.senderscore.org/), review Kit SPF/DKIM settings

- [ ] **Subject line not compelling (engagement issue)**
  - Check: Compare this email's subject to historical subjects that had 25%+ open rate
  - Example: "Women's Health bundle" (generic) vs. "Women's Health — An 8-week herbal series starts today" (specific, benefit-driven)
  - Fix: Note for Week 2 subjects, add time-urgency or benefit (e.g., "Limited: Women's Health Guides — End of Week Pricing")

- [ ] **Send time misaligned with audience timezone**
  - Check: Intended send time was 09:00 ET (13:00 UTC)
  - Question: Is audience mostly European (would prefer 7:00 ET / 11:00 UTC)?
  - Fix: A/B test alternate time in Week 2 (e.g., 6:00 AM ET vs. 9:00 AM ET)

- [ ] **Audience engagement declining (list quality issue)**
  - Check: Are opens declining across ALL recent emails (not just this one)?
  - Symptoms: 25% open rate Jun 28 → 20% Jun 29 → 15% Jun 30 (downward trend)
  - Possible cause: List growth with lower-engagement segments, inactive subscribers
  - Fix: Segment list by engagement tier in Week 2 (send to high-engagement first)

- [ ] **Email design or readability issue**
  - Check: Did email render correctly in preview? (check Kit preview)
  - Common issues: Image doesn't display, text misaligned on mobile, links don't work
  - Fix: Review email in Kit preview on mobile device, adjust design

- [ ] **Recipient list targeted wrong audience**
  - Check: Which segment was email sent to?
  - Expected: "Phase_3_Interested" (people who opted into herbal bundles)
  - If sent to: "All subscribers" or wrong segment, engagement will be low
  - Fix: Verify segment selection before send in Week 2

---

### Investigation Steps (2-3 hours total)

**Step 1: Gather data (15 min)**

1. Open Kit dashboard → Find affected email broadcast
2. Record metrics:
   - Send time (ET/UTC): __________
   - Recipients: __________
   - Delivered: __________ (%)
   - Opens: __________ (%)
   - Clicks: __________ (%)
   - Bounces: __________ (%)
   - Spam complaints: __________ (%)
3. Compare to target (22-28% open rate expected)
4. Document: "Email open rate [X]% — [# points] below target"

**Step 2: Check spam folder (10 min)**

1. Send test email to personal Gmail/Outlook account
2. Wait 2 minutes for delivery
3. Check Inbox (should appear here)
4. If NOT in inbox → Check Spam/Junk folder
5. Screenshot result

**If email in SPAM folder**:
- Root cause: Deliverability issue
- Fix: Check Kit settings for SPF/DKIM (Settings → Email Authentication)
- Note for Week 2: May need to warm up sender domain or check recipient email provider settings
- Proceed to "A/B Resend" (Step 3)

**If email in INBOX**:
- Root cause: Likely NOT spam issue; may be subject line or audience issue
- Proceed to "A/B Resend" (Step 3)

**Step 3: A/B Resend (Optional — if user approves)**

Only proceed if engagement is low AND likely fixable in real-time.

**Option 1: Alternate subject line A/B test**

1. Compose new email with same body, different subject line
2. Send to 25% of original recipient list (randomized)
3. Subject line options:
   - Original: "Women's Health — An 8-week herbal series starts today"
   - Test A: "Limited: Women's Health Bundle — Herbal Series (Ends Sunday)"
   - Test B: "Women's Health: Cycle Support, Hormone Balance, Reproductive Vitality"
4. Send test at 14:00 ET (18:00 UTC) next day (e.g., if Jun 29 email failed, resend test Jun 30 afternoon)
5. Wait 4 hours, check open rates
6. Winning subject line (higher open %): Note for Week 2 emails

**Option 2: Alternate send time A/B test**

1. Resend original email to 25% of recipient list at different time
2. Time options:
   - Original: 09:00 ET (13:00 UTC)
   - Test: 06:00 AM ET (10:00 UTC) — earlier, catch overnight readers
   - Test 2: 03:00 PM ET (19:00 UTC) — afternoon, catch end-of-day check
3. Wait 4 hours after each send, compare open rates
4. Winning time: Note for Week 2 emails

**Step 4: Document findings (15 min)**

Log in PHASE_3_EXECUTION_LOG.md:

```
EMAIL ENGAGEMENT INVESTIGATION — [Email name, date]

Low Open Rate Detected:
- Open rate: [X]% (target: 22-28%)
- Deviation: [Y]% below target
- Sent to: [segment name]
- Recipient count: [number]

Root Cause Analysis:
- Spam folder check: [Email in inbox / Email in spam folder]
- Subject line quality: [Generic / Specific and benefit-driven]
- Send time: [09:00 ET / time UTC]
- Audience quality: [High engagement list / Mixed engagement / Declining trend]
- Email design: [Preview OK / Mobile issues detected]

Recommended Actions for Week 2:
1. [If spam issue] Check SPF/DKIM settings in Kit
2. [If subject line issue] Add urgency or benefit to subject in Week 2 emails
3. [If send time issue] A/B test alternate send time (e.g., 06:00 AM ET)
4. [If list quality issue] Segment list by engagement tier; send high-engagement first

A/B Test Results (if performed):
- Test 1: [subject line / send time] — Open rate [X]% (winner / loser)
- Test 2: [alternate option] — Open rate [X]%
- Winning variant: [which test won]
- Action: Apply winning variant to Week 2 emails

Follow-up:
- Email 2 (Jun 30): Monitor open rate, apply any fixes from Email 1 investigation
- Email 3 (Jul 2): Monitor for trend (improving or declining?)
```

---

### Success Criteria

- [ ] Root cause identified (spam folder, subject line, send time, or list quality)
- [ ] Investigation documented in execution log
- [ ] Week 2 emails adjusted based on findings
- [ ] If A/B test performed: winning variant identified
- [ ] Week 1 bundle still launches on time (no delay)
- [ ] Week 2 emails see improved engagement (25%+ open rate expected)

---

### Escalation Threshold

**Escalate to user if**:
- Open rate <10% cumulative (suggests major deliverability or list quality issue)
- Spam folder rate >50% (domain reputation problem)
- Engagement declining across multiple days (list quality deteriorating rapidly)
- Unable to diagnose root cause after full investigation

---

## FAILURE MODE 5: Unsubscribe Rate Spikes (>0.5% Daily)

**Severity**: MEDIUM-HIGH (indicates content or audience mismatch; impacts long-term list health)  
**Frequency**: RARE (occurs <1% of campaigns if targeting correct)  
**Time to resolve**: 24 hours (content adjustment) to ongoing (list health improvement)

---

### Symptoms

- Daily unsubscribe rate >0.5% of email opens
- Example: 100 opens → 1+ unsubscribe (0.5% or higher)
- Unsubscribe comments indicate frustration (if Kit provides feedback):
  - "Too many emails"
  - "Not relevant to me"
  - "Wrong audience"
  - "Inappropriate content"
- Unsubscribe rate accelerating (higher each day)
- Cumulative unsubscribe rate >2% after 3 emails (high)

---

### Root Cause Checklist

- [ ] **Email frequency too high (bombarding audience)**
  - Check: How many emails sent in last 7 days?
  - Example: Week 1 = 3 emails (Jun 29, Jun 30, Jul 2) over 4 days = 0.75 emails/day
  - Typical acceptable: 0.3-0.5 emails/day (2-3 per week)
  - If >1 email/day: too frequent, subscribers unsubscribing

- [ ] **Email content off-topic or irrelevant to subscriber segment**
  - Check: Who is receiving email? (Segment: "Phase_3_Interested" should be herbalist/wellness audience)
  - If sent to: "All subscribers" or wrong segment, content may miss audience
  - Example: Sending women's health email to general gardening list → irrelevant, will unsubscribe

- [ ] **Email design or tone inconsistent with brand**
  - Check: Does email match prior emails (tone, structure, call-to-action)?
  - Symptom: Sudden shift to hard-sell or overly promotional language
  - Fix: Review tone, make more consistent with prior successful emails

- [ ] **Unsubscribe link not working (technical issue)**
  - Check: Can subscriber actually unsubscribe? Or is link broken?
  - Symptom: Unsubscribe complaints + high unsubscribe clicks but low actual unsubscribes
  - Fix: Verify Kit unsubscribe settings (Settings → Email Management → Unsubscribe preferences)

- [ ] **Timing misaligned with subscriber expectations**
  - Check: Did you promise "weekly emails" but sent 3 in 4 days?
  - Or: Sent email at odd time (3 AM instead of morning) → looks like spam
  - Fix: Set consistent send times, match frequency to subscriber expectations

---

### Recovery Steps

**Step 1: Assess unsubscribe spike (10 min)**

1. Open Kit dashboard → Find email broadcast
2. Record daily unsubscribe rate for each email:
   - Email 1 (Jun 29): [#] unsubscribes = [%] of opens
   - Email 2 (Jun 30): [#] unsubscribes = [%] of opens
   - Email 3 (Jul 2): [#] unsubscribes = [%] of opens
3. Calculate trend: Increasing / Decreasing / Flat
4. Cumulative unsubscribe % (total across all 3 emails)

**Example data**:
```
Email 1 (Jun 29): 68 opens, 0 unsubscribes = 0% (normal)
Email 2 (Jun 30): 71 opens, 1 unsubscribe = 1.4% (HIGH)
Email 3 (Jul 2): 65 opens, 2 unsubscribes = 3.1% (VERY HIGH — escalating)
Trend: Increasing (🔴 RED)
```

---

**Step 2: Diagnose root cause (10-15 min)**

Go through root cause checklist above. Check each item.

**For each YES item** → Note the fix

Most common: Email frequency too high OR content off-topic

---

**Step 3: Adjust Week 2 based on findings (vary by root cause)**

**If frequency too high**:
- Reduce email sends in Week 2
- Original plan: 3 emails per bundle (Jun 29-Jul 2 = 3 in 4 days)
- Adjusted: 2 emails per bundle, spaced 3-4 days apart
- Update PHASE_3_WEEK_1_2_EXECUTION_CHECKLIST.md: Skip "Email 3" for Respiratory bundle, space Email 2 to Jul 9

**If content off-topic**:
- Re-evaluate subscriber segment
- Confirm: Email only sent to "Phase_3_Interested" OR "Herbalism subscribers"
- Do NOT send Women's Health email to "All subscribers" or "Gardening list"
- For Week 2: Segment more precisely, exclude low-engagement subscribers

**If email tone too sales-y**:
- Review Email 1 and Email 2 content (copy from PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md)
- Assess: % educational (60%+) vs. % promotional (<40%)
- Adjust Week 2: Increase educational content, reduce calls-to-action

**If timing issue**:
- Check: Send times are 09:00 ET (13:00 UTC) for all emails
- Confirm: Consistent timing, not random times
- For Week 2: Maintain 09:00 ET send time, same day of week if possible

---

**Step 4: Communicate retention (optional but recommended)**

If unsubscribe rate is high, consider sending optional "preference update" email:

**Email subject**: "We missed you — tell us what you'd like to hear"

**Email body**:
```
Hi there,

We noticed some of you unsubscribed from recent emails.

We get it — email fatigue is real. We're adjusting our sending frequency to [1-2 per week] 
and making sure content is highly relevant to your interests.

If you want to stay in touch, here's what we're planning:

Women's Health bundle deep-dive (highly personalized)
Respiratory season prep (timing and cultivation guides)
Sleep support (for fall season coming up)

All guides are written specifically for home growers, not just wellness enthusiasts.

Would you like to re-subscribe? Or just want to hear from us less frequently?

[Resubscribe link] [Frequency preference center] [Permanently unsubscribe]

Thanks for the feedback.
Seedwarden
```

---

**Step 5: Document findings (10 min)**

Log in PHASE_3_EXECUTION_LOG.md:

```
UNSUBSCRIBE SPIKE DETECTED — [Date]

Unsubscribe Rate Analysis:
- Email 1: [X] unsubscribes = [Y]% of opens (normal / HIGH / VERY HIGH)
- Email 2: [X] unsubscribes = [Y]% of opens
- Email 3: [X] unsubscribes = [Y]% of opens
- Cumulative: [X] total unsubscribes = [Y]% of total opens
- Trend: [Increasing / Decreasing / Flat]

Root Cause: [Frequency too high / Content off-topic / Tone too sales-y / Timing issue]

Week 2 Adjustments:
1. [Reduce frequency from 3 to 2 emails per bundle]
2. [Segment more precisely; exclude low-engagement subscribers]
3. [Increase educational content %; decrease sales %]
4. [Maintain consistent 09:00 ET send time]
5. [Send optional "preference update" email to reassure list]

Expected impact:
- Unsubscribe rate: Reduced to <0.5% daily
- Re-engagement: [X]% of previous unsubscribers may re-subscribe (optional)
- Long-term list health: Healthier, more engaged audience

Follow-up:
- Week 2 Email 1 (Jul 6): Monitor unsubscribe rate closely
- If still >0.5%: Further reduce frequency or segment more
- If normalized (<0.5%): Continue adjusted strategy through Phase 3
```

---

### Success Criteria

- [ ] Root cause identified and documented
- [ ] Week 2 emails adjusted (reduced frequency, better segmentation, tone adjusted, or timing optimized)
- [ ] Unsubscribe rate normalized (<0.5% daily) by Week 2
- [ ] Optional retention email sent (if appropriate)
- [ ] Long-term list health improved (engaged, not fatigue-stricken)

---

### Escalation Threshold

**Escalate to user if**:
- Unsubscribe rate >2% cumulative (unacceptably high)
- Unsubscribe spike continues after Week 2 adjustments (may indicate fundamental list quality issue)
- Multiple failure modes co-occurring (high unsubscribes + low open rates + high bounces)

---

## DOCUMENT VERSION

**Version**: 1.0  
**Date**: June 29, 2026  
**Failure modes covered**: 5 (Email, Social, Contractor, Email Engagement, Unsubscribe Rate)  
**Total recovery procedures**: 5 major + sub-procedures  
**Estimated consultation time per failure**: 5-30 minutes  
**Use with**: PHASE_3_WEEK_1_2_EXECUTION_CHECKLIST.md and PHASE_3_EXECUTION_AUTOMATION_TEMPLATES.md
