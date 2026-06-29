---
title: "Phase 3 Week 1-2 Execution Master Checklist — Q3 Launch June 29–July 13"
date: 2026-06-29
version: 1.0
status: active
sprint-window: June 29 – July 13, 2026
cross-references:
  - PHASE_3_WEEK_1_2_DAILY_EXECUTION_CHECKLIST.md (day-by-day operational log)
  - PHASE_3_WEEK_1_2_CONTENT_BLOCKS_READY_TO_SHIP.md (copy-paste email + social blocks)
  - PHASE_3_WEEK_1_2_VERIFICATION_TEMPLATES.md (quality gate run-sheets)
  - PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md (numeric go/no-go gates)
  - PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md (source email templates)
  - PHASE_3_SOCIAL_MEDIA_CONTENT_CALENDAR.md (source social post copy)
  - PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md (contractor tracking + quality gates)
  - PHASE_3_LAUNCH_MARKETING_CALENDAR.md (week-by-week execution plan)
---

# Phase 3 Week 1-2 Execution Master Checklist

**Coverage**: June 29 (Women's Health launch, Day 0) through July 13 (Sleep & Nervines Day 1, Week 1-2 close).
**Daily overhead**: 30-45 minutes.
**Execution architecture**: Three parallel tracks run simultaneously — Email sends (Kit.com), Social posts (Buffer/Later), Contractor communications. All three tracks converge at 9am ET each active day.

**How to use this document**:
- Complete Section 1 (Pre-Execution Setup) in full before 9am ET June 29.
- Run the daily execution blocks in Section 2 (one block per day, June 29-July 13).
- Use Section 3 (Weekly Roll-Ups) to record aggregate metrics at the end of Week 1 (Jul 6) and Week 2 (Jul 13).
- Keep Section 4 (Contingency Quick-Reference) open in a browser tab during every active send window.
- Section 5 (Automation Readiness) is optional but reduces daily overhead by 15-20 minutes per day if fully implemented.

---

## SECTION 1 — PRE-EXECUTION SETUP (Complete before 9am ET June 29)

All tasks below must be verified complete before the first email send. Time estimate: 45-60 minutes total if running sequentially; 20-25 minutes if running platforms in parallel.

### 1-A: Kit.com Email Account Verification

- [ ] Log in to Kit.com. Confirm account status shows "Active" (not "Suspended" or "Paused").
- [ ] Confirm sender name is set correctly: "Seedwarden" (Settings > Sender info).
- [ ] Confirm reply-to email is a working address you monitor.
- [ ] Verify unsubscribe link is active: send a test email to yourself and confirm the unsubscribe footer renders.
- [ ] Confirm subscriber count is accurate. Log it here: _____ subscribers as of June 29.
- [ ] Load Email 1 (Women's Health) into Kit as a broadcast campaign:
  - Campaign name: `Phase 3 — Women's Health Launch`
  - Subject line: `Women's Health — An 8-week herbal series starts today`
  - Preview text: `Cycle support, hormone balance, and reproductive vitality herbs you can grow`
  - Replace [ETSY_LINK] with live Etsy listing URL for Women's Health bundle
  - Audience: Full subscriber list (no segmentation)
  - Scheduled send time: 9:00am ET, June 29
  - Kit automation tag to apply on send: `phase3-womens-health-launch`
- [ ] Send test email to your own inbox. Verify: links work, images load, unsubscribe footer present, sender name correct.
- [ ] Screenshot the Kit draft screen with send time visible. Save as `kit-email1-draft-screenshot.png`.

### 1-B: Social Media Platform Login Test

Test all three platforms. If login fails, do not proceed until resolved — account lockout on launch day is a critical failure.

**Instagram**:
- [ ] Log in to Instagram. Confirm you are on the correct Seedwarden account (not a personal account).
- [ ] Confirm posting is unrestricted (no "account under review" or "action blocked" banners).
- [ ] Load Post 1 (Women's Health launch) into Instagram scheduler or drafts:
  - Text: Copy from `PHASE_3_SOCIAL_MEDIA_CONTENT_CALENDAR.md` Post 1 Instagram section (~80 words, 10 hashtags)
  - Replace [ETSY_LINK] placeholder text with "link in bio" (update bio link separately)
  - Schedule: 9:00am ET, June 29 (or 8:00am ET if using Instagram-native scheduling)
  - Post type: Feed post (not Story, not Reel unless video brief is ready)
- [ ] Update Instagram bio link to Women's Health Etsy listing URL.

**LinkedIn**:
- [ ] Log in to LinkedIn. Confirm access to Seedwarden company profile (not personal profile).
- [ ] Confirm no pending notifications about content policy violations.
- [ ] Load Post 1 (Women's Health launch) into LinkedIn scheduler:
  - Text: Copy from `PHASE_3_SOCIAL_MEDIA_CONTENT_CALENDAR.md` Post 1 LinkedIn section (~240 words)
  - Add [ETSY_LINK] in post body (LinkedIn allows clickable links in body text)
  - Schedule: 9:00am ET, June 29
- [ ] Confirm LinkedIn company page has admin access (not just "editor").

**YouTube**:
- [ ] Log in to YouTube Studio. Confirm Seedwarden channel is the active channel.
- [ ] If YouTube Shorts video is ready: upload and schedule for 12:00pm ET June 29 (YouTube Shorts optimal time differs from LinkedIn/Instagram — see Section 5 for cron note).
- [ ] If YouTube Shorts video is not ready: substitute a still-image Shorts post with text overlay, or skip YouTube Shorts for Post 1 (Instagram + LinkedIn are the priority).

### 1-C: Contractor Payment Method Verification

- [ ] Confirm Upwork account has sufficient funds or payment method on file for Milestone 1 deposits (due at contract signing, before June 29).
- [ ] Confirm PayPal or direct payment method is active for contractors hired off-platform (Rebecca Lexa, Arthur Haines).
- [ ] Log the contracted rate for each hired contractor in `PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md` [ACTUAL] column before Week 1 begins.
- [ ] Milestone 1 deposit (25% of contract rate) sent to each hired contractor at contract signing — confirm all are sent:
  - Photographer (Upwork): [ ] Deposit sent | Amount: $_____
  - Writer (if via Upwork): [ ] Deposit sent | Amount: $_____
  - Rebecca Lexa (direct): [ ] Deposit sent | Amount: $_____
  - Adrian White (if hired): [ ] Deposit sent | Amount: $_____
  - Arthur Haines (direct): [ ] Deposit sent | Amount: $_____
  - Conservation Board referral (if hired): [ ] Deposit sent | Amount: $_____

### 1-D: Email Template Final QA (All Three Week 1-2 Templates)

For each template: open in Kit, verify every [BRACKET] is filled, confirm Etsy link resolves to a live listing, and send test email.

**Email 1 — Women's Health (send June 29)**:
- [ ] Subject line confirmed: "Women's Health — An 8-week herbal series starts today"
- [ ] [ETSY_LINK] replaced with live listing URL
- [ ] Sender name shows "Seedwarden"
- [ ] Price in body reads "$22"
- [ ] Test email sent + verified: [ ] Pass

**Email 2 — Respiratory Health (send July 6)**:
- [ ] Subject line confirmed: "Respiratory Health — Herbs for clear airways and strong immunity"
- [ ] [ETSY_LINK] placeholder filled in (Respiratory Health Etsy listing URL — must be live before July 6 8am ET)
- [ ] Price in body reads "$20"
- [ ] Load into Kit as scheduled broadcast for 9:00am ET July 6
- [ ] Test email sent + verified: [ ] Pass

**Email 3 — Sleep & Nervines (send July 13)**:
- [ ] Subject line confirmed: "Sleep & Nervines — The herbal foundation for deep rest"
- [ ] [ETSY_LINK] filled in (Sleep & Nervines Etsy listing URL — must be live before July 13 8am ET)
- [ ] Price in body reads "$20"
- [ ] Load into Kit as scheduled broadcast for 9:00am ET July 13
- [ ] Test email sent + verified: [ ] Pass

### 1-E: Canva Design Assets Staged and Downloaded

- [ ] Women's Health bundle cover: final Canva file exported as PDF + JPEG. File is in Etsy draft listing.
- [ ] Respiratory Health bundle cover: final Canva file exported. File staged for Etsy upload by July 5 (one day before launch).
- [ ] Sleep & Nervines bundle cover: final Canva file exported. File staged for Etsy upload by July 12.
- [ ] Immunity Support bundle cover: status — in progress (due July 3 Design Lock deadline).
- [ ] Digestive Support bundle cover: status — in progress (due July 3 Design Lock deadline).
- [ ] All social image assets (herb photography or Canva graphics) downloaded to local folder `projects/seedwarden/phase-3-assets/week-1-2/` for offline access during send window.

### 1-F: Setup Verification Final Gate

Do not proceed to June 29 execution until all boxes below are checked:

- [ ] Kit account active, Email 1 loaded and test-sent
- [ ] Instagram: Post 1 scheduled 9am ET June 29, bio link updated
- [ ] LinkedIn: Post 1 scheduled 9am ET June 29
- [ ] All Milestone 1 deposits sent (or contractor start confirmed)
- [ ] All three email templates (Emails 1-3) loaded in Kit with send dates set
- [ ] Women's Health bundle live on Etsy (not in draft)

**If any item above is unchecked at 8:45am ET June 29: delay the 9am send by 15 minutes. Do not send with an unverified Etsy link or untested email.**

---

## SECTION 2 — DAILY EXECUTION BLOCKS (June 29 – July 13)

Each block follows a fixed format: Morning Brief → 9am ET Execution → Mid-Day Check → Evening Review. All times Eastern.

The day-by-day task detail (every checkbox) lives in `PHASE_3_WEEK_1_2_DAILY_EXECUTION_CHECKLIST.md`. This section provides the master timing reference and copy-paste instruction blocks for each send.

---

### WEEK 1 (Jun 29 – Jul 6): Women's Health Launch

#### June 29 (Monday) — Day 0: Women's Health Launch

**06:00 ET** — Prepare and final-check Day 0 send:
- Open Kit. Confirm Email 1 (Women's Health) is scheduled for 9:00am ET, status "Scheduled."
- Open Etsy. Confirm Women's Health bundle listing is "Active" (not "Draft"). Copy the live URL.
- If [ETSY_LINK] in Email 1 has not been updated with the live URL: edit now. Re-send test email.

**08:00 ET** — Morning brief:
- Re-verify: bundle live on Etsy + email scheduled in Kit + Post 1 scheduled in scheduler.
- Confirm Instagram bio link points to Women's Health Etsy listing.

**09:00 ET** — Execute:

Email 1 send instruction (copy-paste into Kit "Send Now" or confirm scheduled broadcast fires):
```
Campaign: Phase 3 — Women's Health Launch
Subject: Women's Health — An 8-week herbal series starts today
Send to: Full subscriber list
Kit tag: phase3-womens-health-launch
```
- [ ] Kit confirmation screen shows "Sending" or "Sent" by 9:05am ET.
- [ ] Screenshot the Kit "Sent" confirmation. Save as `june29-email1-send-confirm.png`.

Social Post 1 send instruction:
- LinkedIn: Confirm ~240-word launch post is live on Seedwarden company page by 9:05am ET.
- Instagram: Confirm ~80-word post + 10 hashtags is live on feed by 9:05am ET.
- YouTube Shorts: If video ready, confirm live by 12:00pm ET. If not ready, mark N/A.

**12:00 ET** — Mid-day check (5 min):
- Kit dashboard: delivery rate _____ % (target >95%)
- Kit dashboard: open rate at 3 hours _____ % (expect 10-20% by noon)
- Social: any comments? Reply within 4 hours.

**18:00 ET** — Evening review (15 min):
- Email 1 preliminary open rate: _____ % (target >22% at 24 hours)
- LinkedIn engagement: likes _____ comments _____
- Instagram engagement: likes _____ comments _____
- Etsy: views _____ purchases _____
- Log all numbers in `WORKLOG.md` under entry `2026-06-29 Day 0 metrics`.

**Alert**: If open rate <15% by 18:00 ET on June 29, see Section 4-A (Email Send Failed contingency). Do not intervene before 48 hours unless delivery rate is also below 90%.

---

#### June 30 (Tuesday) — Day 1: Red Clover Spotlight

**08:00 ET** — Morning brief:
- Check Kit 24-hour open rate for Email 1. Record: _____ %
- Confirm Post 2 (Red Clover spotlight, LinkedIn only) is loaded in scheduler for 9am ET.

**09:00 ET** — Execute:

Social Post 2 send instruction:
```
Platform: LinkedIn only
Post: "Why Red Clover is often the first herb women add to their garden..."
~270 words, professional educational tone
Add Etsy link in first comment (not in post body for algorithm reasons)
```
- [ ] Post 2 live on LinkedIn by 9:05am ET.

**18:00 ET** — Evening review (10 min):
- 48-hour Email 1 open rate (if >24 hours since send): _____ % (final baseline)
- Post 2 LinkedIn engagement: likes _____ comments _____
- Log in `WORKLOG.md` under `2026-06-30 Day 1 metrics`.

**Decision point — EOD June 30**: If Email 1 48-hour open rate <22%: plan subject line A/B test for Email 2 (Respiratory, July 6). Do not change anything yet — just note in WORKLOG.md.

---

#### July 1 (Wednesday) — Day 2: Contractor Onboarding + Post 3

**06:00 ET** — Prepare contractor onboarding kit emails:
- Copy onboarding kit template from `PHASE_3_WEEK_1_2_CONTENT_BLOCKS_READY_TO_SHIP.md` Section C.
- Fill in for each contractor: name, bundle assigned, first deliverable date, Milestone 1 payment amount confirmed.

**08:00 ET** — Morning brief:
- Confirm Post 3 (Harvest Timing, Instagram) loaded for 9am ET.
- Confirm contractor onboarding emails drafted and ready to send.

**09:00 ET** — Execute:

Social Post 3 send instruction:
```
Platform: Instagram only
Post: "Timing is everything. The same herb — harvested at different times — has completely different active compounds..."
~110 words, 8 hashtags (#herbalism #harvest #herbgarden #plantscience #medicinalherbs #timing #seedwarden #growwhatyouuse)
Feed post (not Story)
```
- [ ] Post 3 live on Instagram by 9:05am ET.

**09:00–10:00 ET** — Send contractor onboarding kits:
- [ ] Contractor 1 (Photographer): onboarding kit sent
- [ ] Contractor 2 (Photo licensing): onboarding kit sent
- [ ] Contractor 3 (Photographer fallback): onboarding kit sent
- [ ] Contractor 4 (Writer+Habitat, Rebecca Lexa): onboarding kit sent
- [ ] Contractor 5 (Writer): onboarding kit sent
- [ ] Contractor 6 (Clinical Writer, Adrian White): onboarding kit sent
- [ ] Kickoff call calendar invites sent to all 6 contractors (photographers: 20 min, writers: 30 min, specialists: 20 min — target dates July 2-3)

**18:00 ET** — Evening review:
- Contractor responses received: _____ / 6
- Outstanding questions to answer within 24 hours: _____
- Post 3 Instagram engagement: likes _____ comments _____
- Log in `WORKLOG.md` under `2026-07-01 Day 2 contractor onboarding`.

---

#### July 2 (Thursday) — Day 3: Grower Feature + Kickoff Calls

**08:00 ET** — Morning brief:
- Answer any contractor questions from Day 2 (24-hour SLA — must respond by 10am ET today).
- Confirm Post 4 (Grower Feature 1, LinkedIn + Instagram) loaded for 9am ET.

**09:00 ET** — Execute:

Social Post 4 send instruction:
```
Platform: LinkedIn + Instagram
LinkedIn: "One of our testers, a home gardener in zone 5, planted red clover for the first time this spring..." ~180 words
Instagram: "I had no idea it would come back every year." — Zone 5 gardener, first red clover harvest..." ~80 words, 7 hashtags (#gardening #herbgarden #sustainability #permaculture #medicinalherbs #womenshealth #seedwarden)
Replace [ETSY_LINK] with Women's Health listing URL
```
- [ ] Post 4 live on LinkedIn by 9:05am ET.
- [ ] Post 4 live on Instagram by 9:05am ET.

**09:00–17:00 ET** — Kickoff calls window:
- [ ] Photographer kickoff call (20 min): shot list reviewed, Session 1 date locked (target July 5 delivery), prop list confirmed.
- [ ] Writer kickoff call (30 min): bundle outlines reviewed, FTC Quick Reference acknowledged, Respiratory first draft due date confirmed (July 8).
- [ ] Specialist kickoff call (20 min): scoped sections confirmed, primary source guidance provided (USDA PLANTS, NatureServe, UpS).

**18:00 ET** — Evening review:
- Kickoff calls completed: _____ / 3 tracks
- Post 4 engagement: LinkedIn _____, Instagram _____
- Contractor Q&A SLA met (all questions answered): [ ] Yes [ ] No (log outstanding items)
- Log in `WORKLOG.md`.

**Decision point — Day 3**: If any contractor has not responded to onboarding kit within 48 hours of send (by July 3 10am ET): send one follow-up email same day. If still no response by July 4 10am ET: see Section 4-C (Contractor Missed Deadline escalation template).

---

#### July 3 (Friday) — Day 4: Expectorant/Demulcent Post + Design Lock

**06:00 ET** — Design Lock pre-check:
- Review all 5 Canva bundle covers. Identify any that are not final by this morning.

**08:00 ET** — Morning brief:
- Confirm Post 5 (Expectorant vs. Demulcent, LinkedIn) loaded for 9am ET.
- Confirm Respiratory Email 2 template is in Kit with [ETSY_LINK] filled in and scheduled for 9am ET July 6.

**09:00 ET** — Execute:

Social Post 5 send instruction:
```
Platform: LinkedIn only
Post: "Two very different respiratory strategies. Most guides don't distinguish them..."
~260 words, educational, expectorant vs. demulcent framework
Etsy link at end for Respiratory Health pre-launch teaser
```
- [ ] Post 5 live on LinkedIn by 9:05am ET.

**17:00 ET** — Design Lock deadline:
- [ ] Women's Health cover: [ ] Final
- [ ] Respiratory Health cover: [ ] Final
- [ ] Sleep & Nervines cover: [ ] Final
- [ ] Immunity Support cover: [ ] Final
- [ ] Digestive Support cover: [ ] Final

**Alert**: If any cover is not final by 17:00 ET today: log in WORKLOG.md with reason. Respiratory launch (July 6) is zero-float on cover design — the bundle cannot go live on Etsy without a final cover.

**18:00 ET** — Evening review:
- Design lock status: _____ / 5 covers final
- Post 5 engagement: _____
- Log in `WORKLOG.md`.

---

#### July 4 (Saturday) — Day 5: Photographer Session 1 Delivery

**No social post today.** Holiday. Use the day for contractor deliverable review.

**09:00 ET** — Check for Session 1 images from photographer:
- Check email + shared drive/Dropbox.
- Session 1 due: today (per kickoff call confirmed date).

**If Session 1 images received — run quality gate**:

```
PHOTOGRAPHER QUALITY GATE — SESSION 1

Source: PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md Section 3

[ ] 5 images delivered: top-down flat-lay, 45° flat-lay, lifestyle ×2, close-up detail
[ ] Minimum resolution 2000×2000px confirmed (check image properties)
[ ] White balance consistent across all 5 images (compare side by side)
[ ] sRGB color space confirmed (check image metadata)
[ ] No harsh shadows obscuring herbs or guide text
[ ] File naming follows: respiratory-[type]-[sequence].jpg (e.g. respiratory-flatlay-01.jpg)
[ ] Commercial license confirmed per contract (no additional purchase required)

Result: [ ] ALL PASS → send Praise Email (Template 3A) within 48 hours
        [ ] PARTIAL FAIL → send Course Correction (Template 3B) with specific reshoot notes
        [ ] TOTAL FAIL / NONE RECEIVED → trigger Wikimedia CC fallback (see Section 4-C)
```

**If NO images received by 17:00 ET**: Send follow-up message today. If still no response by July 6 10am ET: activate contingency (Section 4-C).

**18:00 ET** — Evening review:
- Session 1 received: [ ] Yes [ ] No
- Quality gate result: [ ] Pass [ ] Partial [ ] Fail
- Reshoot items noted: _____
- Praise or correction email drafted for Monday: [ ] Yes
- Respiratory bundle live on Etsy: confirm tonight (not draft) for Monday 9am send

---

#### July 5 (Sunday) — Day 6: Respiratory Launch Prep

**No social post, no email send.** Preparation only.

**Launch prep checklist for July 6**:
- [ ] Respiratory Health bundle live on Etsy (verify listing URL resolves, price shows $20, images correct) — confirm by 20:00 ET tonight.
- [ ] Email 2 (Respiratory) in Kit: [ETSY_LINK] filled in, scheduled for 9:00am ET July 6, test email sent and passes.
- [ ] Social Post 6 (Respiratory launch) loaded in all three schedulers for 9:00am ET July 6 (LinkedIn + Instagram + YouTube Shorts).
- [ ] Contractor Week 2 check-in email drafted (Template 2 from `PHASE_3_WEEK_1_2_CONTENT_BLOCKS_READY_TO_SHIP.md` Section C) — ready to send at 10am ET July 6.
- [ ] Photographer Session 1 praise or correction email ready to send Monday morning.

**Time estimate**: 20 minutes.

---

### WEEK 2 (Jul 6 – Jul 13): Respiratory Health Launch

#### July 6 (Monday) — Day 7: Respiratory Launch + Contractor Week 2 Check-In

**06:00 ET** — Final pre-flight:
- Confirm Respiratory Health Etsy listing is "Active."
- Confirm Email 2 Kit status is "Scheduled" for 9:00am ET.
- Confirm Post 6 is scheduled across all three platforms.

**08:00 ET** — Morning brief:
- One final review: all pre-flight items complete.

**09:00 ET** — Execute:

Email 2 send instruction:
```
Campaign: Phase 3 — Respiratory Health Launch
Subject: Respiratory Health — Herbs for clear airways and strong immunity
Preview text: Elecampane, thyme, mullein, and more — cultivation through preparation
Send to: Full subscriber list
Kit tag: phase3-respiratory-launch
```
- [ ] Kit confirmation shows "Sending" or "Sent" by 9:05am ET.
- [ ] Screenshot Kit "Sent" confirmation. Save as `july06-email2-send-confirm.png`.

Social Post 6 send instruction:
```
Platform: LinkedIn + Instagram + YouTube Shorts
LinkedIn: "The Respiratory Health bundle is live..." ~210 words
Instagram: "Respiratory Health is LIVE..." ~75 words, 8 hashtags (#herbalism #respiratoryhealth #medicinalherbs #plantmedicine #herbgarden #seedwarden #herbalremedies #naturalimmunity)
YouTube Shorts: "Timing changes everything. Thyme at peak bloom has 3x the thymol..." (video brief from PHASE_3_SOCIAL_MEDIA_CONTENT_CALENDAR.md Post 6)
```
- [ ] All three platforms live by 9:15am ET.

**10:00 ET** — Contractor Week 2 check-in (send as async email, not requiring live reply):
```
WEEKLY CHECK-IN TEMPLATE (copy-paste, fill in [BRACKETS])
To: [Contractor Name]
Subject: Seedwarden — Week 2 check-in + this week's priorities

Hi [Name],

Quick async check-in for Week 2 (July 6-12):

Expected this week:
- [State the specific deliverable due this week — e.g., "Respiratory bundle first draft, 3,600 words, due July 8"]
- [State Session 2 due date for photographer — July 12]

Quality status from Week 1:
- [If Session 1 approved: "Session 1 images approved — excellent work on the flat-lay."]
- [If revision needed: "Session 1 reshoot notes sent separately — please confirm receipt."]

This week's priority: [Bundle name + specific section if applicable]

Available resources: [Any reference materials, style guide updates, or access credentials]

Blockers? Reply with any obstacles by EOD today so I can help clear them.

Payment status: [Milestone 1 sent June 28 / Milestone 2 will process after Session 1 approval]

[Your name]
Seedwarden
```
- [ ] Check-in sent to Contractor 1 (Photographer): [ ]
- [ ] Check-in sent to Contractor 4 (Writer, Rebecca Lexa): [ ]
- [ ] Check-in sent to Contractor 5 (Writer): [ ]
- [ ] Check-in sent to Contractor 6 (Clinical Writer): [ ]
- [ ] Check-in sent to Contractor 7/8 (Habitat Specialist): [ ]
- [ ] Photographer Session 1 praise/correction email sent (drafted over weekend): [ ]

**12:00 ET** — Mid-day check (5 min):
- Email 2 delivery rate: _____ % (target >95%)
- Open rate at 3 hours: _____ % (expect 10-20%)
- Social: any comments needing 4-hour reply?

**18:00 ET** — Evening review:
- Email 2 preliminary open rate: _____ %
- Respiratory bundle Etsy views: _____
- All contractor check-ins sent: [ ] Yes
- Post 6 engagement: LinkedIn _____, Instagram _____, YouTube _____
- Log in `WORKLOG.md` under `2026-07-06 Day 7 Respiratory launch`.

---

#### July 7 (Tuesday) — Day 8: Mullein ID Video + Session 1 Approval Window

**08:00 ET** — Morning brief:
- Post 7 (Mullein identification, YouTube + Instagram) loaded for 9am ET.
- Session 1 photo review due by 17:00 ET today (if not completed Saturday/Sunday).

**09:00 ET** — Execute:

Social Post 7 send instruction:
```
Platform: YouTube Shorts (primary) + Instagram Reels (secondary)
Video brief: Mullein leaf close-up, flower spike in yellow bloom, 3 look-alike images with "NOT mullein" labels
Text overlay: "Mullein Identification"
Voiceover/captions: "Mullein leaf is the softest texture of any medicinal herb. One touch and you recognize it..."
CTA: "Learn to harvest safely. Respiratory Health guide. Link in bio."
YouTube: 12pm ET optimal | Instagram Reels: 9am ET
```
- [ ] Post 7 live on YouTube Shorts by 12:00pm ET.
- [ ] Post 7 live on Instagram Reels by 9:05am ET.

**17:00 ET** — Session 1 approval deadline:
- [ ] Full quality gate review completed (checklist in Day 5 above).
- [ ] Decision: [ ] All approved [ ] Reshoot needed: _____
- [ ] If approved: Milestone 2 payment to photographer scheduled for July 8.

**18:00 ET** — Evening review:
- Post 7 engagement: YouTube _____, Instagram _____
- Session 1 review decision: _____
- Log in `WORKLOG.md`.

---

#### July 8 (Wednesday) — Day 9: Echinacea Post + Writer Draft Due + Milestone 2 Payment

**08:00 ET** — Morning brief:
- Post 8 (Echinacea species, LinkedIn) loaded for 9am ET.
- Writer first draft (Respiratory bundle, 3,600 words) due today — check email.

**09:00 ET** — Execute:

Social Post 8 send instruction:
```
Platform: LinkedIn only
Post: "Why echinacea product labels matter more than the product itself..."
~260 words, species comparison (purpurea vs. angustifolia vs. pallida), educational
Etsy link at end for Respiratory Health bundle
```
- [ ] Post 8 live on LinkedIn by 9:05am ET.

**Photographer Milestone 2 Payment** (if Session 1 approved July 7):
- [ ] Session 1 approved: [ ] Yes → process payment | [ ] No → hold
- [ ] If yes: payment sent via [agreed method: Upwork / PayPal] for 25% of contract rate: $_____ sent.
- [ ] Payment confirmation email sent to photographer.

**Writer Draft Receipt Check**:
- [ ] Respiratory bundle first draft received from writer by 17:00 ET: [ ] Yes [ ] No
- [ ] If YES: begin 48-hour review (FTC compliance + species accuracy). Review due July 10.
- [ ] If NO by 17:00 ET: send follow-up: "Checking in — Respiratory draft was due today. Please confirm current status and expected delivery time."

**18:00 ET** — Evening review:
- Writer draft received: [ ] Yes [ ] No
- Photographer Milestone 2 sent: [ ] Yes ($_____ ) [ ] No (held — reshoot pending)
- Post 8 engagement: _____
- Log in `WORKLOG.md`.

---

#### July 9 (Thursday) — Day 10: Contractor Spotlight + Draft Review in Progress

**08:00 ET** — Morning brief:
- Post 9 (Contractor spotlight, Instagram) loaded for 9am ET.
- Writer draft review in progress (48-hour window: July 8-10).

**09:00 ET** — Execute:

Social Post 9 send instruction:
```
Platform: Instagram only
Post: "Meet [Photographer Name], who captured the respiratory bundle images..."
Fill in: [Photographer Name], [1-2 sentences about their style], [link to their portfolio/Instagram]
~100 words + hashtags (#herbphotography #botanicalart #medicinalherbs #craftmanship #herbalism #seedwarden)
```
- [ ] Post 9 live on Instagram by 9:05am ET.

**Writer Draft Review — in progress**:
- [ ] FTC compliance pass: all therapeutic claims qualified with evidence-tier framing? ("traditionally used for" / "research suggests" / "clinical evidence supports" — no "prevents," "cures," "treats")
- [ ] Latin binomials on first mention of each species: [ ] verified
- [ ] Word count check: target 3,600 words ±360 (3,240–3,960): _____ words
- [ ] CITES sidebar (Goldenseal) present if covering Immunity content: N/A for Respiratory draft

**18:00 ET** — Evening review:
- Draft review progress: _____ % complete
- FTC flags or accuracy issues to note: _____
- Post 9 engagement: _____
- Log in `WORKLOG.md`.

---

#### July 10 (Friday) — Day 11: Writer Draft Review Decision

**No social post today.** Writer draft review closes today.

**Writer Draft Review — Final Decision** (target: complete by 12:00pm ET):

```
WRITER QUALITY GATE — RESPIRATORY BUNDLE

Source: PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md Section 3

[ ] Word count: _____ words (target 3,600 ±360)
[ ] All species covered with Latin binomial on first mention
[ ] FTC: no unqualified therapeutic claims ("prevents"/"cures"/"treats" without evidence context)
[ ] Contraindication panels cite primary source (NatMed Pro, MSK Integrative Medicine, or equivalent)
[ ] Black Cohosh and Echinacea angustifolia conservation sidebars present
[ ] Self-edit pass confirmed in writer submission message
[ ] No content placeholders remaining ([TBD], [INSERT], [XXX])

Result: [ ] APPROVED → send Template 3A (Praise Email) + schedule Milestone 2 payment
        [ ] REVISION NEEDED → send Template 3B (Course Correction) with specific revision notes
                              Set revision due date: _____ (allow 2-3 days)
```

**If APPROVED**:
- [ ] Send praise email to writer today (use Template 3A from `PHASE_3_WEEK_1_2_CONTENT_BLOCKS_READY_TO_SHIP.md` Section C).
- [ ] Milestone 2 payment to writer scheduled.

**If REVISION NEEDED**:
- [ ] Send course correction email today with itemized revision list.
- [ ] Confirm revised draft due date does not conflict with Sleep & Nervines launch July 13.

**18:00 ET** — Evening review:
- Draft review decision: [ ] Approved [ ] Revision needed
- Approval or revision email sent: [ ] Yes
- Log in `WORKLOG.md`.

---

#### July 11 (Saturday) — Day 12: Session 2 Check + Sleep Launch Prep

**No social post.** Prep day.

**Photographer Session 2 check**:
- [ ] Session 2 images received (due July 12 per calendar): [ ] Yes (arrived early) [ ] Pending
- [ ] If received: run quality gate (same checklist as Session 1 in Day 5).

**Sleep & Nervines launch prep**:
- [ ] Sleep & Nervines bundle confirmed on Etsy draft — upload by end of today if not done.
- [ ] Email 3 in Kit with [ETSY_LINK] filled in, scheduled for 9:00am ET July 13.
- [ ] Post 10 (Sleep & Nervines launch) loaded in all schedulers for 9:00am ET July 13.

**Time estimate**: 25 minutes.

---

#### July 12 (Sunday) — Day 13: Session 2 Review + Final Prep

**Session 2 Photo Review — close by 17:00 ET**:
- [ ] All 5 Session 2 images reviewed against quality gate.
- [ ] Decision: [ ] Approved [ ] Reshoot needed: _____
- [ ] Photographer notified.
- [ ] If approved: Milestone 3 payment to photographer scheduled.

**Sleep & Nervines final launch verification**:
- [ ] Sleep & Nervines bundle live on Etsy (verify URL resolves, price $20, images correct).
- [ ] Email 3 Kit status: "Scheduled" for 9:00am ET July 13.
- [ ] Post 10 (Sleep launch) in schedulers for 9:00am ET July 13 — all three platforms.
- [ ] Week 3 contractor check-in (Template 2) drafted and ready to send July 13 at 10am ET.

**Time estimate**: 25 minutes.

---

#### July 13 (Monday) — Day 14: Sleep & Nervines Launch + Week 1-2 Close

**06:00 ET** — Final pre-flight:
- Sleep & Nervines Etsy listing active.
- Email 3 Kit status "Scheduled" for 9:00am ET.
- Post 10 scheduled on all three platforms.

**09:00 ET** — Execute:

Email 3 send instruction:
```
Campaign: Phase 3 — Sleep & Nervines Launch
Subject: Sleep & Nervines — The herbal foundation for deep rest
Preview text: Valerian, passionflower, lemon balm, and nervine teas for restorative sleep
Send to: Full subscriber list
Kit tag: phase3-sleep-nervines-launch
```
- [ ] Kit confirmation shows "Sending" or "Sent" by 9:05am ET.
- [ ] Screenshot Kit "Sent" confirmation. Save as `july13-email3-send-confirm.png`.

Social Post 10 send instruction:
```
Platform: LinkedIn + Instagram + YouTube Shorts
LinkedIn: "Sleep & Nervines bundle is live. That's three of five bundles launched..." ~270 words
Instagram: "Sleep & Nervines is LIVE..." ~85 words, 11 hashtags (#sleep #sleepwell #nervine #herbalism #herbgarden #valerian #lavender #chamomile #medicinalherbs #seedwarden #naturalhealth)
YouTube Shorts: Valerian root time-lapse or lavender field close-up with text overlay
```

**10:00 ET** — Week 3 contractor check-in sent (same Template 2 as July 6 check-in, updated for Week 3 deliverables).

**18:00 ET** — Week 1-2 Retrospective (log all actuals):

```
WEEK 1-2 CLOSE METRICS — July 13 EOD

Email Performance:
  Email 1 (Women's Health) final open rate: _____ % (target 22-28%)
  Email 2 (Respiratory) final open rate: _____ % (target 22-28%)
  Email 3 (Sleep & Nervines) preliminary open rate: _____ % (48-hour window still open)
  Combined total opens (Emails 1+2): _____ (target >250)
  Combined click rate: _____ % (target 3-5%)

Social Performance:
  Total posts published (Posts 1-9): _____
  Total combined engagements (all platforms, Posts 1-9): _____ (target >500)
  LinkedIn average engagement per post: _____
  Instagram average engagement per post: _____
  YouTube Shorts total views: _____
  Estimated impressions per post: _____ (target 150-250)

Contractor Status:
  Session 1 delivered and approved: [ ] Yes [ ] No
  Session 2 delivered: [ ] Yes [ ] No (due today per calendar)
  Writer Respiratory first draft: [ ] Approved [ ] In revision
  All onboarding calls complete: _____ / 3 tracks
  All Week 2 check-ins sent: [ ] Yes

Etsy Performance:
  Women's Health views: _____ | Purchases: _____
  Respiratory Health views: _____ | Purchases: _____
  Sleep & Nervines views: _____ | Purchases: _____

Week 3 Pacing Decision:
  [ ] All GREEN (email >250 combined opens, social >500 engagements, contractors 3/4+ on track): proceed to Week 3 at full pace
  [ ] Any YELLOW: review PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md for compressed timeline option
  [ ] Any RED: escalate — see PHASE_3_LAUNCH_CONTINGENCY_ROUTING.md
```

---

## SECTION 3 — WEEKLY ROLL-UP SUMMARIES

### Week 1 Roll-Up (June 29 – July 6): Women's Health Launch

**Expected metrics at July 6 EOD**:

| Metric | Expected Range | Actual | Status |
|--------|---------------|--------|--------|
| Email 1 (Women's Health) open rate | 22-28% | _____ % | [ ] |
| Email 1 click rate | 3-5% | _____ % | [ ] |
| Social posts published (Posts 1-5) | 5 | _____ | [ ] |
| Total social engagements (Posts 1-5) | >200 | _____ | [ ] |
| Estimated impressions per post | 150-250 | _____ avg | [ ] |
| Women's Health Etsy views | 50-200 | _____ | [ ] |
| Women's Health purchases | 5-20 | _____ | [ ] |
| Contractor onboarding complete | 6/6 | _____ | [ ] |
| Kickoff calls complete | 3/3 tracks | _____ | [ ] |

**Alert thresholds — Week 1**:
- Open rate <15% at 48 hours: see Section 4-A
- 0 social engagement on Posts 1-5 combined: see Section 4-B
- Any contractor no-show on kickoff call by July 4: see Section 4-C

**Week 1 narrative summary** (write 2-3 sentences after EOD July 6):
> _____

---

### Week 2 Roll-Up (July 6 – July 13): Respiratory Health Launch

**Expected metrics at July 13 EOD**:

| Metric | Expected Range | Actual | Status |
|--------|---------------|--------|--------|
| Email 2 (Respiratory) open rate | 22-28% | _____ % | [ ] |
| Email 2 click rate | 3-5% | _____ % | [ ] |
| Social posts published (Posts 6-9) | 4 | _____ | [ ] |
| Total social engagements (Posts 6-9) | >200 | _____ | [ ] |
| Respiratory Etsy views | 30-150 | _____ | [ ] |
| Respiratory purchases | 3-15 | _____ | [ ] |
| Session 1 photos approved | Pass | _____ | [ ] |
| Session 2 photos received | Delivered | _____ | [ ] |
| Writer Respiratory draft: approved | Approved | _____ | [ ] |
| Contractor Week 2 check-in sent | All 6 | _____ | [ ] |

**Alert thresholds — Week 2**:
- Email 2 open rate <15% at 48 hours: run 3-step investigation (Section 4-A) before Email 3 sends July 13
- Photographer Session 1 not received by July 8: activate Wikimedia CC image fallback (Section 4-C)
- Writer draft not received by July 8 EOD: escalation follow-up same day (Section 4-C)

**Week 2 narrative summary** (write 2-3 sentences after EOD July 13):
> _____

---

## SECTION 4 — CONTINGENCY QUICK-REFERENCE

All procedures below are copy-paste ready. Execute in order. Log every action with timestamp in `WORKLOG.md`.

### 4-A: Email Send Failed

**Trigger**: Kit campaign does not show "Sent" status by 9:15am ET. Or delivery rate drops below 90%.

**Step 1**: Check Kit dashboard. Look for error message ("sending limit reached," "account suspended," "IP reputation flag").

**Step 2**: If no error shown — click "Resend" in Kit. Kit resend link:
```
kit.com → Campaigns → [Campaign Name] → ... menu → Resend to non-openers
Note: "Resend to non-openers" is the correct option if initial send failed. This will not double-send to those who already received it.
```

**Step 3**: If Kit account is suspended: contact Kit support immediately.
```
Email: support@kit.com
Subject: Account suspension — active launch, time-sensitive
Body: "My account appears suspended. I have a scheduled email broadcast for a product launch. My account name is [Seedwarden / your email]. Please advise on resolution timeline."
```

**Step 4**: If Kit is down entirely — send email manually from your email client (Gmail / Outlook) to your subscriber list using BCC (do not CC — subscribers will not see each other's addresses). Use the full email body from `PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md`.

**Step 5**: Log in WORKLOG.md: timestamp, error message, action taken, resolution time.

---

### 4-B: Social Post Failed to Schedule

**Trigger**: Post not live on platform by 9:15am ET (15-minute grace window).

**Step 1**: Open the platform directly (LinkedIn, Instagram, or YouTube Studio). Do not wait for scheduler notification.

**Step 2**: Post manually using the "Post Now" option. Copy text directly from `PHASE_3_SOCIAL_MEDIA_CONTENT_CALENDAR.md` for the relevant post.

**LinkedIn post-now**:
```
linkedin.com/company/[seedwarden-profile] → Start a post → paste text → Post (no scheduling needed, post immediately)
```

**Instagram post-now**:
```
instagram.com → New post → upload image → paste caption and hashtags → Share
```

**YouTube post-now**:
```
studio.youtube.com → Create → Upload video → paste title + description → Publish now (or set to "Public")
```

**Step 3**: If a scheduler is malfunctioning consistently: switch to native platform posting for the remainder of Week 1-2. Native posting takes 3-4 minutes per post — budget this time into your 9am ET window.

**Step 4**: Log the scheduler failure in WORKLOG.md with platform and date. Do not resume using the scheduler until you confirm the root cause.

---

### 4-C: Contractor Missed Deadline — Escalation Email Template

**Trigger**: Contractor misses any of the following: onboarding kit acknowledgement (48 hours), kickoff call (rescheduled twice), or first deliverable (missed by 24+ hours with no communication).

**Copy-paste response (send within 3 minutes of identifying the miss)**:
```
Subject: Quick check-in — [deliverable] was due [date]

Hi [Contractor Name],

Quick check-in — [specific deliverable: "Session 1 photos" / "Respiratory bundle first draft" / "onboarding kit response"] was due [specific date].

I haven't received it yet. Can you give me a quick status update:

1. Is the work complete and just not sent yet?
2. Is there a blocker I can help with?
3. Do you need a short extension? (If so, what's a realistic new date?)

I need to hear back by [today's date + 24 hours] so I can plan accordingly. If I don't hear back by then, I'll need to start contingency planning.

Please reply to this email — even a one-line update is helpful.

[Your name]
Seedwarden
```

**If no response within 24 hours of escalation email**: Activate solo fallback for that deliverable.

**Wikimedia CC image fallback** (for photographer no-show):
- Search: `commons.wikimedia.org/wiki/Special:Search?search=[species+name]+habit`
- Require: CC BY or CC BY-SA license
- Download and log in WORKLOG.md: species name, source URL, license, photographer credit required

**Solo writing fallback** (for writer no-show):
- Use `PHASE_3_MEDICINAL_HERBS_BUNDLE_CONTENT.md` as the species accuracy source
- Write 800-1,200 words per species section (reduced scope, launch-viable)
- FTC review yourself using the qualifier checklist in `PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md` Section 3

---

### 4-D: Metrics Tracking Dashboard Template (Google Sheets)

Create a new Google Sheet with the following structure for Week 1-2. Update after each send and each evening review.

**Tab 1: Email Metrics**
```
Column A: Date
Column B: Email Name
Column C: Send Time (actual)
Column D: Recipient Count
Column E: Delivery Rate %
Column F: Open Rate % (24hr)
Column G: Open Rate % (48hr, final)
Column H: Click Rate %
Column I: Etsy Clicks
Column J: Unsubscribes
Column K: Notes
```

**Tab 2: Social Metrics**
```
Column A: Date
Column B: Post #
Column C: Platform
Column D: Post Type (Educational / Promotional / Community)
Column E: Impressions
Column F: Engagements (likes + comments)
Column G: Engagement Rate %
Column H: Profile Clicks (to Etsy or bio)
Column I: Notes
```

**Tab 3: Contractor Log**
```
Column A: Date
Column B: Contractor
Column C: Event (onboarding sent / kickoff call / deliverable received / payment sent)
Column D: Status
Column E: Notes / Action Required
```

**Tab 4: Etsy Performance**
```
Column A: Date
Column B: Bundle
Column C: Daily Views
Column D: Daily Purchases
Column E: Revenue ($)
Column F: Cumulative Views
Column G: Cumulative Purchases
Column H: Notes
```

---

## SECTION 5 — AUTOMATION READINESS

All items in this section are optional but reduce manual overhead. Implement before June 29 if you have 2+ hours. If not, skip — manual execution per Section 2 is fully sufficient.

### 5-A: Kit.com Scheduled Broadcasts (Automated)

All three emails can be scheduled in Kit before June 29 and will fire automatically at the specified times.

**To schedule all three at once**:
1. Log in to Kit.com.
2. Navigate to: Broadcasts → New Broadcast.
3. Create each campaign, fill in content, and set the send time (9:00am ET = 13:00 UTC).
4. Click "Schedule" (not "Send Now").
5. Confirm all three campaigns show status "Scheduled" with correct dates.

**Benefit**: You will not need to manually trigger emails on June 29, July 6, or July 13. Kit fires them automatically. Your 9am ET window becomes verification-only (screenshot the sent confirmation).

### 5-B: Buffer/Later Social Scheduling (Automated)

Load all 9 Week 1-2 social posts into Buffer or Later before June 29:

**Bulk scheduling order**:
```
Post 1: Jun 29, 9:00am ET — LinkedIn + Instagram + YouTube
Post 2: Jun 30, 9:00am ET — LinkedIn
Post 3: Jul 1, 9:00am ET — Instagram
Post 4: Jul 2, 9:00am ET — LinkedIn + Instagram
Post 5: Jul 3, 9:00am ET — LinkedIn
Post 6: Jul 6, 9:00am ET — LinkedIn + Instagram + YouTube
Post 7: Jul 7, 9:00am ET — Instagram Reels + YouTube (12pm ET for YouTube)
Post 8: Jul 8, 9:00am ET — LinkedIn
Post 9: Jul 9, 9:00am ET — Instagram
```

**Note on YouTube Shorts timing**: YouTube Shorts optimal engagement time is 12pm ET (lunch), not 9am ET. If using a scheduler, set YouTube posts to 12pm ET. LinkedIn and Instagram posts stay at 9am ET (or 8am ET for Instagram).

### 5-C: Cron Commands for Metric Collection (Optional, local machine)

If you want automated reminders for metric review windows, add these to your crontab on the machine you use daily:

```bash
# Open crontab editor
crontab -e

# Add the following entries:

# Daily 9am ET reminder — check Kit send confirmation (Mon-Fri only, during send weeks)
0 13 29 6 1 echo "CHECK: Kit email send confirmation for today. Verify delivery rate in Kit dashboard." | mail -s "Seedwarden 9am ET email check" wanka95@gmail.com

# Daily 6pm ET reminder — log evening metrics
0 22 * 6,7 * echo "LOG: Evening metrics in WORKLOG.md. Email open rate, social engagement, Etsy views." | mail -s "Seedwarden evening metrics" wanka95@gmail.com

# Week 1 retrospective reminder — July 6 6pm ET
0 22 6 7 1 echo "WEEK 1 CLOSE: Run Week 1 roll-up in PHASE_3_WEEK_1_2_EXECUTION_CHECKLIST.md Section 3." | mail -s "Seedwarden Week 1 close" wanka95@gmail.com

# Week 2 retrospective reminder — July 13 6pm ET
0 22 13 7 1 echo "WEEK 2 CLOSE: Run Week 2 roll-up + retrospective in PHASE_3_WEEK_1_2_EXECUTION_CHECKLIST.md Section 3." | mail -s "Seedwarden Week 2 close" wanka95@gmail.com
```

**Note on cron syntax**: The entries above use date-specific targeting which standard cron does not support natively. For simplicity, set a recurring daily reminder in your phone or calendar app instead. Cron is useful for recurring checks (the 6pm metrics reminder) — set that one up if you have the environment configured.

**Simpler alternative — add these as calendar events now** (zero setup required):
- June 29, 9:00am ET: "Email 1 send + social post 1 — verify in Kit + scheduler"
- June 29, 12:00pm ET: "Check Kit delivery rate"
- June 29, 6:00pm ET: "Log Email 1 preliminary metrics in WORKLOG.md"
- July 6, 9:00am ET: "Email 2 send + social post 6 — verify"
- July 6, 10:00am ET: "Send contractor Week 2 check-ins"
- July 13, 9:00am ET: "Email 3 send + social post 10 — verify"
- July 13, 6:00pm ET: "Week 1-2 retrospective + log all metrics"

### 5-D: Discord Webhook Notifications for Send Confirmations (Optional)

If you use Discord for project management, you can trigger a notification each time a Kit email sends. This requires a Zapier or n8n automation connecting Kit webhooks to your Discord channel.

**Setup outline** (implement only if you already use Discord and Zapier):
1. In Zapier: Create a Zap — Trigger: Kit "Broadcast sent" event. Action: Discord "Send message."
2. Message format:
   ```
   Seedwarden email sent: {{campaign_name}}
   Send time: {{sent_at}}
   Recipients: {{recipients_count}}
   Open rate (available in 1 hour): check Kit dashboard
   ```
3. Test with a dummy Kit broadcast before June 29.

**Simpler alternative**: Set a manual reminder to check Kit at 9:05am ET each launch day and screenshot the "Sent" confirmation. This takes 2 minutes and requires no integration setup.

---

## QUICK-REFERENCE: EMAIL SCHEDULE WEEKS 1-2

| Date | Time ET | Email # | Subject Line | Kit Tag | Audience |
|------|---------|---------|-------------|---------|----------|
| Jun 29 (Mon) | 9:00am | Email 1 | Women's Health — An 8-week herbal series starts today | `phase3-womens-health-launch` | Full list |
| Jul 6 (Mon) | 9:00am | Email 2 | Respiratory Health — Herbs for clear airways and strong immunity | `phase3-respiratory-launch` | Full list |
| Jul 13 (Mon) | 9:00am | Email 3 | Sleep & Nervines — The herbal foundation for deep rest | `phase3-sleep-nervines-launch` | Full list |

---

## QUICK-REFERENCE: SOCIAL POST SCHEDULE WEEKS 1-2

| Date | Time ET | Post | Platform(s) | Copy Source |
|------|---------|------|-------------|------------|
| Jun 29 (Mon) | 9:00am | Post 1 — Women's Health launch | LinkedIn + Instagram + YouTube | Calendar Post 1 |
| Jun 30 (Tue) | 9:00am | Post 2 — Red Clover spotlight | LinkedIn | Calendar Post 2 |
| Jul 1 (Wed) | 9:00am | Post 3 — Harvest timing | Instagram | Calendar Post 3 |
| Jul 2 (Thu) | 9:00am | Post 4 — Grower feature 1 | LinkedIn + Instagram | Calendar Post 4 |
| Jul 3 (Fri) | 9:00am | Post 5 — Expectorant vs. demulcent | LinkedIn | Calendar Post 5 |
| Jul 6 (Mon) | 9:00am | Post 6 — Respiratory launch | LinkedIn + Instagram + YouTube | Calendar Post 6 |
| Jul 7 (Tue) | 9:00am / 12pm | Post 7 — Mullein identification | YouTube (12pm) + Instagram Reels (9am) | Calendar Post 7 |
| Jul 8 (Wed) | 9:00am | Post 8 — Echinacea species | LinkedIn | Calendar Post 8 |
| Jul 9 (Thu) | 9:00am | Post 9 — Contractor spotlight | Instagram | Calendar Post 9 |

---

## QUICK-REFERENCE: CONTRACTOR CRITICAL DATES WEEKS 1-2

| Date | Event | Contractor | Action |
|------|-------|------------|--------|
| Jun 28 (Sun, pre-launch) | Milestone 1 deposits sent | All hired | Confirm all paid before June 29 |
| Jul 1 (Wed) | Onboarding kits sent | All 6 | Send by 10am ET |
| Jul 2-3 (Thu-Fri) | Kickoff calls | All 3 tracks | Complete 20-30 min calls |
| Jul 5 (Sat) | Session 1 delivery | Photographer | Review quality gate same day |
| Jul 6 (Mon) | Weekly check-in #1 | All 6 | Template 2, send by 10am ET |
| Jul 7 (Tue) | Session 1 approval/flag | Photographer | Decision by 17:00 ET |
| Jul 8 (Wed) | Milestone 2 payment (photo) | Photographer | Send if Session 1 approved |
| Jul 8 (Wed) | Writer first draft due | Writer | Receive + begin 48-hour review |
| Jul 10 (Fri) | Draft review decision | Writer | Approve or send revision notes |
| Jul 12 (Sun) | Session 2 delivery | Photographer | Review on receipt |
| Jul 13 (Mon) | Weekly check-in #2 | All 6 | Template 2, send by 10am ET |

---

*Prepared: June 29, 2026. Activation begins 9:00am ET June 29. All times Eastern. This is the master execution checklist for Phase 3 Week 1-2 (June 29-July 13). Day-by-day task detail: PHASE_3_WEEK_1_2_DAILY_EXECUTION_CHECKLIST.md. Copy-paste content blocks: PHASE_3_WEEK_1_2_CONTENT_BLOCKS_READY_TO_SHIP.md. Quality gates: PHASE_3_WEEK_1_2_VERIFICATION_TEMPLATES.md. Alert thresholds: PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md.*
