---
title: "Week 1-2 Email Send Verification Template"
date: 2026-06-29
version: 1.0
status: production-ready
sprint-window: June 29 – July 13, 2026
cross-references:
  - PHASE_3_WEEK_1_2_EXECUTION_MASTER_CHECKLIST.md (daily checklist)
  - PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md (email templates)
  - KIT_EMAIL_LAUNCH_SEQUENCE.md (automation setup)
---

# Week 1-2 Email Send Verification Template

**PURPOSE**: Deterministic proof of email send execution. Every send requires pre-send checklist completion, post-send screenshot confirmation, and timestamp logging. This template is copy-paste for all 6 Phase 3 bundles (June 29 – August 3).

**HOW TO USE**: 
1. **Pre-send checklist**: Complete all items BEFORE clicking Send
2. **Send**: Click Send in Kit at exact time (13:00 UTC = 9:00 AM ET for launches)
3. **Post-send checklist**: Take screenshot, log timestamp, verify deliverability
4. **24/48/72-hour metrics**: Track open rate, click rate, status
5. **CSV log**: Copy final row to master spreadsheet for audit trail

---

## EMAIL 1 — WOMEN'S HEALTH LAUNCH (June 29, 9:00 AM ET / 13:00 UTC)

### PRE-SEND CHECKLIST

**Sender & Recipients**:
- [ ] From email: support@seedwarden.com (verify in Kit)
- [ ] From name: Seedwarden (or your brand name)
- [ ] Recipient list: Full subscriber list (no segmentation)
- [ ] List health: Expected deliverability 98%+ (Kit dashboard shows list size: ____ subscribers)
- [ ] Unsubscribe link: Present in footer? YES / NO
- [ ] Reply-to email: support@seedwarden.com (not support+marketing@ or no-reply@)

**Email Content**:
- [ ] Subject line: "Women's Health — An 8-week herbal series starts today"
- [ ] Preview text: "Cycle support, hormone balance, and reproductive vitality herbs you can grow"
- [ ] Body copy: All [BRACKET PLACEHOLDERS] filled or removed
  - [ ] [ETSY_LINK] → Actual Etsy URL (e.g., https://www.etsy.com/listing/XXXXXXXXX)
  - [ ] [OPTIONAL: seasonal angle] → Filled or removed (keep only if relevant)
  - [ ] [OPTIONAL: testimonial] → Filled with real testimonial or removed
- [ ] CTA button text: "GET THE WOMEN'S HEALTH BUNDLE" (or similar)
- [ ] CTA button link: Points to live Etsy listing (not draft)
- [ ] Word count: ~400 words
- [ ] Tone: Consistent with PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md

**Technical Checks**:
- [ ] Test email sent to personal inbox? (Check rendering, fonts, image loading, CTA clickability)
  - [ ] Rendering looks correct: YES / NO
  - [ ] All images loaded: YES / NO
  - [ ] CTA button clickable: YES / NO
  - [ ] Links work: YES / NO
- [ ] Mobile preview checked? (Kit shows mobile rendering)
  - [ ] Readable on phone: YES / NO
  - [ ] CTA button clickable on mobile: YES / NO
- [ ] Spam check run? (Kit has spam score checker)
  - [ ] Spam score acceptable (<5): YES / NO
  - [ ] No red flags: YES / NO

**Automation & Scheduling**:
- [ ] Campaign created in Kit (not a draft)
- [ ] Send time scheduled: June 29, 2026, 9:00 AM ET (Kit will auto-convert to recipient timezone)
- [ ] Send list verified: [____ subscribers expected]
- [ ] A/B test enabled: YES / NO (if YES, log variant subjects below)
  - [ ] Variant A subject: "Women's Health — An 8-week herbal series starts today"
  - [ ] Variant B subject: [Alternative if testing]
  - [ ] Split: 50/50 (A vs B)

**Compliance**:
- [ ] CAN-SPAM laws: Physical address in footer? YES / NO (if required by law in your jurisdiction)
- [ ] GDPR/CCPA: Consent documented for all recipients? YES / NO
- [ ] No affiliate disclaimers missing (if using affiliate links): YES / NO

**Final Approval**:
- [ ] All items checked above: ✓
- [ ] Ready to send: YES / NO
- [ ] If NO: Reason ________________ (fix before proceeding)

---

### SEND EXECUTION

**Date**: June 29, 2026
**Scheduled send time**: 13:00 UTC (9:00 AM ET)
**Actual send time**: 13:00–13:05 UTC (5-minute window)

| Time | Action | Confirmation |
|------|--------|--------------|
| 12:55 UTC | Final review: All pre-send checks complete? | YES / NO |
| 12:59 UTC | Kit dashboard open, ready to send | YES / NO |
| 13:00–13:05 UTC | **SEND CAMPAIGN** (click Send button in Kit) | Sent ✓ |
| 13:05–13:15 UTC | Confirm send in Kit (should show "Sending..." then "Sent") | Confirmed ✓ |

---

### POST-SEND CHECKLIST (WITHIN 15 MINUTES)

**Confirmation Screenshot**:
- [ ] Kit dashboard showing campaign status: "Sent" (take screenshot)
  - Screenshot filename: `Women-Health-Email_Send_Confirmation_June29_1305UTC.png`
  - Screenshot saved to: `/projects/seedwarden/verification-screenshots/`
- [ ] Timestamp visible in screenshot: 13:05 UTC YES / NO
- [ ] Subscriber count visible: ____ recipients
- [ ] Send confirmation recorded: Date _____, Time 13:05 UTC

**Deliverability Verification** (check Kit dashboard every 5 minutes for first 30 minutes):

| Time (UTC) | Delivered | Failed | Bounced | Notes |
|---|---|---|---|---|
| 13:10 | __/[total] | __/[total] | __/[total] | |
| 13:15 | __/[total] | __/[total] | __/[total] | |
| 13:20 | __/[total] | __/[total] | __/[total] | |
| 13:30 | __/[total] | __/[total] | __/[total] | |

**Deliverability status**: ____/[total] delivered = ___% (target 98%+)
- [ ] Above 98%: ✓ (acceptable)
- [ ] 90-98%: ⚠ (minor issue, monitor opens)
- [ ] <90%: ❌ (potential ISP block or list quality issue — escalate)

**Recipient Feedback** (monitor inbox for bounces/complaints):
- [ ] Any hard bounces immediately after send? Count: ____
- [ ] Any unsubscribe requests immediately after send? Count: ____
- [ ] Any spam complaints? Count: ____
- [ ] Action: [If issues detected, log escalation plan below]

---

### 24-HOUR METRICS (June 30, 13:00 UTC)

**Email Engagement**:
- [ ] Open rate at 24h: ___% (expected 35-45% for launch email)
- [ ] Click rate at 24h: ___% (expected 8-12%)
- [ ] Unsubscribe rate: ___% (expected <0.5%)
- [ ] Spam complaint rate: ___% (expected <0.1%)

**Segment Breakdown** (if Kit provides):
- [ ] Opened by Gmail users: ___% (often higher due to Gmail UI)
- [ ] Opened on mobile: ___% (expect 50-60%)
- [ ] Opened on desktop: ___% (expect 40-50%)
- [ ] Clicked from mobile: ___% (usually 50%+ of clickers)

**Status Assessment**:
- [ ] GREEN (>25% opens, >3% clicks): ✓ On track
- [ ] YELLOW (20-25% opens, 2-3% clicks): ⚠ Monitor, review subject line
- [ ] RED (<20% opens, <2% clicks): ❌ Escalate, activate Tier 2 response

**If YELLOW or RED, action plan**:
1. Review subject line effectiveness (is it clear? enticing? relevant?)
2. Check list quality (are subscribers engaged with previous emails?)
3. Consider A/B test on next bundle email (try more promotional subject vs. educational)
4. Review send time (is 9 AM ET optimal for your audience?)

---

### 48-HOUR METRICS (July 1, 13:00 UTC)

- [ ] Open rate at 48h: ___% 
- [ ] Click rate at 48h: ___% 
- [ ] Final status: GREEN / YELLOW / RED
- [ ] Observations: ____

---

### 72-HOUR METRICS (July 2, 13:00 UTC) — FINAL

- [ ] Final open rate: ___% (record as "Women's Health Final")
- [ ] Final click rate: ___% 
- [ ] Conversion rate (clickers to Etsy): ___% (estimated from click behavior)
- [ ] Status vs. target: EXCEEDS / MEETS / BELOW
- [ ] Benchmark for future: ___% (this becomes Week 3 benchmark for Sleep email comparison)

---

### CSV LOG ENTRY

Copy this row to master spreadsheet after all data collected (July 2):

```
Date,Time (UTC),Email Provider,Recipient Count,Subject,Open Rate,Click Rate,Final Status,Notes
"June 29, 2026","13:05 UTC","Kit.com","[TOTAL SUBSCRIBERS]","Women's Health — An 8-week herbal series starts today","[FINAL %]","[FINAL %]","[GREEN/YELLOW/RED]","[Observations for Week 3 adjustment]"
```

---

---

## EMAIL 2 — RESPIRATORY HEALTH LAUNCH (July 6, 9:00 AM ET / 13:00 UTC)

### PRE-SEND CHECKLIST

**Sender & Recipients**:
- [ ] From email: support@seedwarden.com
- [ ] Recipient list: Full subscriber list (do NOT segment to Women's Health downloaders only)
- [ ] List size: ____ subscribers
- [ ] Unsubscribe link present: YES / NO
- [ ] Reply-to verified: YES / NO

**Email Content**:
- [ ] Subject line: "Respiratory Health — Herbs for clear airways and strong immunity"
- [ ] Preview text: "Elecampane, thyme, mullein, and more — cultivation through preparation"
- [ ] Body copy: All [BRACKETS] filled or removed
  - [ ] [ETSY_LINK] → Actual Respiratory bundle Etsy URL
  - [ ] All customization sections completed
- [ ] CTA button: Points to live Respiratory bundle (not draft)
- [ ] Tone consistent with Women's Health email: YES / NO

**Technical Checks**:
- [ ] Test email sent & rendering confirmed: YES / NO
- [ ] Mobile preview checked: YES / NO
- [ ] Spam score acceptable: YES / NO

**Automation & Scheduling**:
- [ ] Campaign created in Kit
- [ ] Send time: July 6, 2026, 9:00 AM ET (13:00 UTC)
- [ ] Ready to send: YES / NO

---

### SEND EXECUTION

**Date**: July 6, 2026
**Scheduled send time**: 13:00 UTC (9:00 AM ET)
**Actual send time**: 13:00–13:05 UTC

| Time | Action | Confirmation |
|------|--------|--------------|
| 12:55 UTC | Final review: All checks complete? | YES / NO |
| 12:59 UTC | Kit dashboard open, ready | YES / NO |
| 13:00–13:05 UTC | **SEND CAMPAIGN** | Sent ✓ |
| 13:05–13:15 UTC | Confirm send in Kit | Confirmed ✓ |

---

### POST-SEND CHECKLIST

**Confirmation Screenshot**:
- [ ] Screenshot taken: `Respiratory-Health-Email_Send_Confirmation_July6_1305UTC.png`
- [ ] Timestamp: 13:05 UTC
- [ ] Subscriber count: ____ recipients

**Deliverability Verification** (24-hour):
- [ ] Delivered: ____/[total] = ___% (target 98%+)
- [ ] Failed: ____/[total]
- [ ] Bounced: ____/[total]

---

### 24-HOUR METRICS (July 7, 13:00 UTC)

- [ ] Open rate: ___% (target 30-40% for Week 2 email — slightly lower than launch week)
- [ ] Click rate: ___% (target 7-10%)
- [ ] Status: GREEN / YELLOW / RED
- [ ] If YELLOW/RED: Action plan ____

---

### 48-HOUR METRICS (July 8, 13:00 UTC)

- [ ] Open rate: ___% 
- [ ] Click rate: ___% 

---

### 72-HOUR METRICS (July 9, 13:00 UTC) — FINAL

- [ ] Final open rate: ___% (record as "Respiratory Final")
- [ ] Final click rate: ___% 
- [ ] Status vs. target: EXCEEDS / MEETS / BELOW
- [ ] Benchmark for future: ___% (compare to Women's Health: diff ___%)

---

### CSV LOG ENTRY

```
"July 6, 2026","13:05 UTC","Kit.com","[TOTAL SUBSCRIBERS]","Respiratory Health — Herbs for clear airways and strong immunity","[FINAL %]","[FINAL %]","[GREEN/YELLOW/RED]","[Observations for Week 3 adjustment]"
```

---

---

## EMAIL SEND MASTER CSV (Track all 6 Phase 3 emails here)

### Column Definitions

- **Date**: Launch date of bundle (e.g., June 29)
- **Time (UTC)**: Send time in UTC (all 13:00 UTC for launches)
- **Email Provider**: Kit.com (our standard)
- **Recipient Count**: Number of subscribers on list at send time
- **Subject**: Exact subject line sent
- **Open Rate**: Final % after 72 hours
- **Click Rate**: Final % after 72 hours
- **Final Status**: GREEN (exceeds target) / MEETS (on target) / BELOW (below target)
- **Notes**: Observations for next bundle adjustment (subject line change, send time shift, segmentation test, etc.)

### Spreadsheet Template

| Date | Time (UTC) | Email Provider | Recipient Count | Subject | Open Rate | Click Rate | Final Status | Notes |
|------|---|---|---|---|---|---|---|---|
| June 29 | 13:05 | Kit.com | [___] | Women's Health — An 8-week herbal series starts today | [___%] | [___%] | GREEN/MEETS/BELOW | |
| July 6 | 13:05 | Kit.com | [___] | Respiratory Health — Herbs for clear airways and strong immunity | [___%] | [___%] | GREEN/MEETS/BELOW | |
| July 13 | 13:05 | Kit.com | [___] | Sleep & Nervines — Herbs for deep rest and emotional calm | [___%] | [___%] | GREEN/MEETS/BELOW | |
| July 15 | 13:05 | Kit.com | [___] | Practitioner Tier — The Complete Plant Medicine Reference | [___%] | [___%] | GREEN/MEETS/BELOW | |
| July 20 | 13:05 | Kit.com | [___] | Immunity Support — Herbs for resistance and seasonal health | [___%] | [___%] | GREEN/MEETS/BELOW | |
| Aug 3 | 13:05 | Kit.com | [___] | Digestive Support — Herbs for gut health and seasonal harvest | [___%] | [___%] | GREEN/MEETS/BELOW | |

---

## CONTINGENCY: EMAIL SEND FAILURE

**If email does NOT send at scheduled time**:

1. **Check Kit dashboard** (13:05 UTC):
   - Is campaign still in "Scheduled" status? 
   - Any error message? Log it: ____
   
2. **If campaign failed to send automatically** (quota exceeded, API error, etc.):
   - [ ] Manual send: Click "Send Now" in Kit
   - [ ] Log new timestamp: 13:__ UTC (record deviation)
   - [ ] Email notification: Notify support@seedwarden.com of delay
   - [ ] Impact assessment: Does 15-minute delay affect open rate? (Probably <1% impact)

3. **If email is stuck in draft**:
   - [ ] Check campaign status: Is it saved and scheduled?
   - [ ] Resave: Click "Save" then "Schedule" again
   - [ ] Verify send time is future, not past
   - [ ] Manual send: Click "Send Now"

4. **If Kit is down**:
   - [ ] Check Kit status page (kit.com/status)
   - [ ] Escalate to Kit support: support@kit.com
   - [ ] Email delayed: Notify this to user (transparency)
   - [ ] Resend when service restored

---

## REPLY-TO EMAIL MONITORING

**During 24-72 hour window after send**:
- [ ] Check reply-to email (support@seedwarden.com) for subscriber questions
- [ ] Response turnaround: <24 hours for customer questions
- [ ] Log common questions: ____
- [ ] Common questions = content gap for next bundle? Note for Week 3.

---

## NOTES FOR FUTURE SENDS (Sleep, Immunity, Digestive, Practitioner Tier)

**Based on Women's Health + Respiratory performance, adjust Week 3+ as follows**:

- **Subject line optimization**: [If women's health open rate was high, replicate subject structure; if low, change style]
- **Send time adjustment**: [If opens peaked at different hour, adjust subsequent sends]
- **Segmentation strategy**: [If certain segments (mobile users, Gmail users) had much higher engagement, consider segmenting future sends]
- **CTA clarity**: [If click rate was low relative to opens, review CTA button text and placement]
- **Customization sections**: [Which optional sections resonated? Keep in Week 3+ sends]

---

*Prepared: June 29, 2026. Email verification is deterministic — screenshot every send, log every metric, escalate any deviation. Week 1-2 email data informs all future Phase 3 sends.*
