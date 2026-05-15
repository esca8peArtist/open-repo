---
title: "May 30 Launch Contingency Protocols and Failure Mode Recovery Playbooks"
prepared: 2026-05-15
launch-date: 2026-05-30
status: production-ready
scope: Gate 2 (Canva Brand Kit), Gate 3 (Kit email), Launch day (Etsy, Kit broadcast, social, GA4)
references:
  - MAY_30_RISK_AND_CONTINGENCY_PLAN.md (gate-level risk summary)
  - TRACK_B_USER_GATES.md (gate specifications and steps)
  - TRACK_B_EXECUTION_READINESS.md (Item 57 gap audit with Canva and Kit platform limits)
  - MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md (hour-by-hour sequence)
  - KIT_SETUP_NOTES.md (Kit platform configuration)
  - TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md (Brand Kit spec)
---

# May 30 Launch Contingency Protocols and Failure Mode Recovery Playbooks

**How to use this document**: This document is your calm, step-by-step guide for when
something does not go as planned. Each playbook covers one specific failure mode. The
structure is always: what you observe, how to confirm it is really the problem, what you
do in the next 5 minutes, what you do in the next 30-60 minutes, and when to escalate.

Work through only the playbook that applies to your situation. Do not try to read this
cover to cover on launch day — go directly to the section whose trigger matches what you
are seeing.

**Companion document**: `LAUNCH_DAY_DECISION_TREE.md` is the one-page quick-reference
flowchart. Read that first on launch morning. Come here for the full recovery procedures
when the decision tree points you to a specific playbook.

---

## Part A: Gate 2 Contingencies — Canva Brand Kit (May 19-24 window)

---

### Playbook A1: "I can't add 10 colors to my Brand Kit"

**Trigger**: You open Brand Hub in Canva and attempt to add a 7th, 8th, 9th, or 10th
color, and Canva blocks the addition or shows an upgrade prompt.

**Why this happens**: As confirmed in the Item 57 audit (TRACK_B_EXECUTION_READINESS.md),
Canva's free plan limits Brand Kit to 3 colors. The gate specification calls for 10 colors
(6 brand colors plus 4 zone band colors). This is a real platform constraint, not a UI bug.

**Step 1 — Detection (2 minutes). Confirm this is actually a plan limit, not a UI error:**
1. In Canva Brand Hub, attempt to add color number 4.
2. If Canva shows "Upgrade to Canva Pro" or "This feature is not available on your current
   plan" — you have hit the free plan limit. Proceed to the fix below.
3. If Canva shows a different error (network error, session timeout) — refresh the browser
   and try again before concluding it is a plan limit.
4. If you can add color 4 but not 7 — Canva may have quietly raised the free tier limit.
   Document the actual limit you observe and add as many colors as the plan allows.

**Immediate fix — 5 minutes. Add only the 3 most critical colors to the Brand Kit:**

If you can only store 3 colors in the Brand Kit, choose these three:
- Deep Forest Green: `#143b28` — the primary header and border color used on every asset
- Warm Cream: `#F5EDD6` — the background color used on every card and graphic
- Burnt Sienna: `#A0522D` — the accent used in zone band headers and call-to-action elements

These 3 colors cover the majority of every Canva design. The remaining 7 can be entered
manually by pasting the hex code into Canva's color picker during each design session. This
adds approximately 20 seconds per color per design — a manageable overhead for the launch week.

**Full recovery — 30 minutes. Two options (choose one):**

Option 1 — Upgrade to Canva Pro for one month:
- Cost: approximately $15 USD billed monthly, cancel any time
- Canva Pro allows unlimited Brand Kit colors
- After upgrade: add all 10 colors at once, build the full Brand Kit, produce all zone cards
  and pin templates in one session
- Cancel Canva Pro after the May 30 launch week if ongoing cost is not desired
- Canva Pro also unlocks premium elements, but none are required for the Seedwarden
  specification — all fonts and layouts in the spec are on the free tier

Option 2 — Manual hex entry during every design session (no cost):
- Create a "Seedwarden Color Cheat Sheet" document (text file or note) with all 10 hex codes
  listed. Keep it open whenever you are working in Canva.
- During each design, click any color element, select "Custom color," and paste the hex code.
- Save frequently used colors to Canva's "Recent colors" bar (Canva remembers your last 20
  custom colors for the session).
- This approach adds 2-3 minutes per design session and scales fine for 50 or fewer designs.
- The zone band colors (#3D6B8A, #2D5016, #C9943A, #A0522D) are used only in zone cards.
  You will use each zone color in one dedicated work session, so manual entry is not repetitive.

**Recommendation**: If you plan to produce more than 20 Canva designs before the end of May,
upgrade to Canva Pro for one month. If you expect to produce 10 or fewer designs before launch,
use Option 2. The zone card batch requires 8 distinct design sessions — Canva's "Recent colors"
memory means you only paste each hex code once per session, not once per element.

**Prevention for future work**: If this constraint causes friction in the first week post-launch,
Canva Pro is a sustainable tool investment at $15/month given the 30-day content calendar volume.
Make that decision based on actual time spent in Week 1, not speculation before launch.

**Escalation trigger**: If neither option works (billing error on Pro upgrade, or color picker
is not accepting hex codes), take a screenshot of the error and log it in WORKLOG.md. Post
to the Canva support community at community.canva.com — responses are typically within 24 hours.
For launch day: use mockup images from `projects/seedwarden/mockups/` as social post images.
These are already built and require no Brand Kit colors.

---

### Playbook A2: "Brand Kit upload failed / Canva API error"

**Trigger**: You attempt to create the Brand Kit (Step 1 of Brand Hub setup) or upload the
logo (Step 4), and Canva shows an error message, spinner that never resolves, or the Brand Kit
disappears after appearing to save.

**Step 1 — Detection (3 minutes). Distinguish between transient and persistent failures:**
1. Refresh the browser tab (Cmd/Ctrl + Shift + R for hard refresh). Try the action again.
2. Try an incognito/private browsing window. Log in to canva.com/wanka95@gmail.com and
   navigate to Brand Hub again. Transient session errors clear in incognito.
3. Try a different browser (Chrome vs. Firefox vs. Safari). This eliminates browser extension
   interference.
4. Check status.canva.com — if there is a live incident, the error is on Canva's side and
   will self-resolve. Check back in 30-60 minutes.

**Immediate fix — 5 minutes:**
- If the Brand Kit creation step fails: try naming it with a shorter name (e.g., "SW" instead
  of "Seedwarden"). Rarely, Brand Kit names with special characters can cause submission errors.
- If the logo upload fails: ensure the file is PNG format and under 5 MB. The file at
  `projects/seedwarden/logos/seedwarden_logo_1.png` meets both requirements. Resize using
  any image editor if the file has been modified since its creation.
- If colors fail to save: enter one color, click Save, verify it persists, then add the next.
  Adding all colors at once in a single paste session occasionally times out.

**Full recovery — 30-60 minutes:**
- If the Brand Kit consistently fails to save across multiple sessions: do not spend more
  than 30 minutes debugging this. Instead, work without the Brand Kit using the manual hex
  entry method described in Playbook A1, Option 2.
- The Brand Kit is a convenience tool — it is not a hard technical requirement for any
  deliverable. Every zone card, pin, and social graphic in the specification can be built by
  manually entering hex codes and selecting fonts by name.
- Contact Canva support (help.canva.com/hc/en-us/requests/new) with a screenshot of the
  error. File the support ticket, then continue working without waiting for a response.

**Escalation trigger**: If you have been unable to create the Brand Kit after two separate
browser sessions on two different days, log this in WORKLOG.md and proceed with manual hex
entry as the permanent approach. Do not let Brand Kit debugging block zone card production.

---

### Playbook A3: "Canva Brand Kit is corrupted / design template disappeared"

**Trigger**: A Brand Kit that was working correctly now shows an error, displays no colors
or fonts, or a zone card design file you previously saved is no longer accessible.

**Detection:**
1. Navigate to Brand Hub directly (canva.com/brand-hub). Does the Kit appear in the list?
2. If the Kit appears but shows no content: click into it and wait 30 seconds for assets to
   load. Slow connections can cause Brand Hub assets to appear empty until they load.
3. If a design file has disappeared: check Canva > Home > Recent designs. Canva does not
   permanently delete user designs without explicit user action (Move to trash + Empty trash).
   Disappeared designs are almost always in a different folder or accessible via Recent.
4. Check Canva > Projects > All projects for the file.

**Recovery path:**
- If the Brand Kit lost its colors: re-add colors in 5 minutes using the hex code table in
  `TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md` Part 1, Step 2. This is faster than the original
  setup because you are not making decisions — just re-entering known values.
- If the Brand Kit lost its logo: re-upload seedwarden_logo_1.png from
  `projects/seedwarden/logos/`. The upload takes under 1 minute.
- If a zone card design is missing: rebuild from the Zone 5 master template. If Zone 5 is
  also missing, rebuild from scratch using `CANVA_ZONE_CARD_DESIGN_GUIDE.md`. This is the
  worst case — budget 2-3 hours for full Zone 5 rebuild, then 30-45 minutes per subsequent zone.

**Fallback (if Brand Kit cannot be recovered before launch):**
- Use Canva's plain templates without Brand Kit. Enter colors manually as described in
  Playbook A1 Option 2.
- Zone card exports are PDFs — once exported, they are independent of the Canva Brand Kit.
  If zone card PDFs are already exported and on Google Drive, a Brand Kit failure after that
  point has zero impact on launch.

**Prevention:**
- After completing each zone card, immediately export the PDF and save it to
  `projects/seedwarden/assets/zone-cards/`. Do not leave all exports until the end.
  A crashed design session loses unsaved work; an exported PDF is permanent.
- After completing the Brand Kit setup, take a screenshot of the Brand Kit screen and save
  it locally. This serves as a recovery reference if anything resets.

---

## Part B: Gate 3 Contingencies — Kit Email Account (May 27-28 window)

---

### Playbook B1: "Email routing not working / subscribers not receiving emails"

**Trigger**: You complete the end-to-end test (sign up via landing page with a test email)
and the test email does not receive Email 1 within 5 minutes. Or: on launch day, you receive
reports that subscribers are not receiving emails.

**Step 1 — Detection. Work through this checklist before taking any action:**

1. Check Kit > Automations > Sequences. Is the automation status "Active" or "Draft/Paused"?
   An automation in Draft or Paused state sends nothing. Click "Activate" if it shows as paused.

2. Check Kit > Subscribers. Did the test subscriber appear in the subscriber list? If the
   subscriber is not listed, the form submission did not complete. The issue is in the landing
   page form, not the email automation.

3. If the subscriber IS listed in Kit: click their name and verify the zone tag was applied
   (e.g., "zone-5"). If no tag was applied, the form's zone dropdown is not connected to the
   automation rule. See fix below.

4. Check the test email's spam/junk folder. Kit emails from a Gmail sender address
   (wanka95@gmail.com) occasionally land in spam for Gmail recipients, especially on new Kit
   accounts. If the email is in spam: this is a DKIM/SPF issue, not an automation failure.

5. Check Kit > Activity (subscriber activity log). Does it show "Email 1 sent" for the test
   subscriber? If yes: the email sent but was filtered. If no: the automation did not trigger.

**DKIM/SPF/DMARC verification (if email lands in spam):**

Kit sends email on behalf of your Gmail address. For delivery to be reliable:
- Go to Kit > Settings > Email > Email deliverability.
- Kit will show you whether SPF and DKIM are configured for your sending domain.
- If you are using wanka95@gmail.com (not a custom domain), DKIM and SPF are managed by
  Google, not by you. Kit's verification will show limited or basic deliverability.
- For launch at a small list size (under 200 subscribers), Gmail-based sending delivers
  adequately. Spam filtering is low risk for educational content to opted-in subscribers.
- If deliverability is flagged: the long-term fix is a custom domain (seedwarden.com) with
  proper SPF/DKIM records. This is a Phase 3 improvement, not required for May 30.

**Immediate fix — 5 minutes (if automation not triggering):**
1. In Kit > Automations > Sequences, click into the sequence.
2. Verify the trigger condition: it should read "When subscriber subscribes via [your landing
   page name]." If it says a different trigger or shows a blank, re-add the trigger.
3. Verify Email 1 is the first step in the sequence with delay "immediately."
4. Verify the sequence is set to "Active" (not "Draft").
5. Re-run the test: sign up via the landing page using a different test email address.

**Full recovery — 30-60 minutes (if zone tag routing is broken):**

As documented in KIT_SETUP_NOTES.md, there are two approaches to zone routing:
- Option A (recommended): 8 variants of Email 1, one per zone, each triggered by the
  corresponding zone tag (zone-5, zone-6, etc.).
- Option B: A single Email 1 with a liquid tag conditional to insert the zone-specific link.

If Option A routing is broken (tag applied but wrong email sends): verify each automation rule.
Go to Kit > Automations and check each "If subscriber has tag zone-X > send Email 1 Zone X
variant." The rule must use exact tag names matching those in Kit > Subscribers > Tags.

If Option B conditional fails (only one email variant exists but it sends the wrong link):
the liquid tag syntax may be incorrect. Kit's conditional liquid syntax is:
`{% if subscriber.fields.zone == 'Zone 5' %} [link] {% endif %}`
The field name must exactly match the custom field name you set in the sign-up form.

If you cannot resolve the routing in under 30 minutes: simplify the launch to a single Email 1
that delivers Zone 5's card (the statistically most common zone) and manually send zone-specific
emails to subscribers who signed up with other zones. This is the "soft launch routing" approach
documented in MAY_30_RISK_AND_CONTINGENCY_PLAN.md Sub-Risk 1C.

**Escalation trigger**: If Kit's automation panel shows an error message or "sequence cannot
be activated," take a screenshot and contact Kit support at support@kit.com. Kit's average
first response time is under 4 hours on business days. While waiting for support response,
proceed with the Gmail manual broadcast fallback documented in Playbook B3 below.

---

### Playbook B2: "Conditional logic doesn't work / Kit shows 'limitations' warning"

**Trigger**: You attempt to build the zone routing automation in Kit (8 zone-specific email
variants triggered by zone tags) and Kit displays an upgrade prompt, a "limitations" warning,
or the conditional automation steps are grayed out and uneditable.

**Why this happens**: As confirmed in the Item 57 audit, Kit's free plan (Newsletter plan)
allows only 1 automation and 1 sequence, with no conditional logic. The full zone routing
architecture in the gate specification requires conditional steps that are gated behind the
Kit Creator plan at approximately $33/month. This is a real platform constraint.

**Decision framework — choose before taking any action:**

Question: How many distinct zones do you expect your launch-week subscribers to be in?
- If you expect primarily Zone 5 and Zone 6 subscribers (temperate US, most common): the
  single-sequence Option A below is the correct launch approach.
- If you expect wide zone diversity across all 8 zones from Day 1: upgrade to Kit Creator
  plan is the correct approach.

For a brand-new account with zero subscribers launching May 30, Zone 5-6 concentration
is the most likely outcome. The full conditional routing is a Week 3-4 optimization.

**Option 1 — Simplify to a single email (no cost, 10 minutes to implement):**
- Build one Email 1 that includes all 8 zone card download links, clearly labeled.
- Subject: "Your free zone quick-start card — all zones below"
- Body: "Select your zone from the list below to download your card:"
  [Zone 3 link] [Zone 4 link] [Zone 5 link] ... [Zone 10 link]
- This approach is fully functional. It is slightly less elegant than zone-specific routing
  but delivers the correct card to every subscriber. For a list under 100 subscribers, this
  is acceptable and requires no platform upgrade.
- The subscriber experience is: sign up > receive one email with all zones listed > click
  their zone > download their card. Functional and clear.

**Option 2 — Manual segmentation (no cost, ongoing manual work):**
- When a new subscriber signs up, Kit records which zone they selected as a custom field.
- Check Kit > Subscribers once daily. For each new subscriber, manually send them the
  correct zone card by replying directly from Kit using the one-time email feature.
- This scales only to small list sizes (under 30 subscribers). Build automated routing
  before the list exceeds 30 subscribers.

**Option 3 — Upgrade to Kit Creator plan ($33/month):**
- Unlocks unlimited automations, unlimited sequences, and conditional logic.
- Conditional zone routing as specified in TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md becomes
  fully available.
- Upgrade at kit.co > Settings > Plan. Monthly billing, cancel any time.
- After upgrade: build the full 8-variant Email 1 routing per the gate specification.
  Budget 1 additional hour to set up the conditional automation rules.

**Recommendation**: For launch day, use Option 1 (all-zones email). It is zero-cost, requires
10 minutes to implement, and is fully reliable. Upgrade to Creator and implement full conditional
routing in Week 2 when you can see actual zone distribution data from real subscribers.

**Prevention**: The Item 57 audit identified this gap on May 15. If you are reading this on
or after May 20, you have time to choose the appropriate plan before Gate 3 begins on May 27.
Do not start building the conditional routing architecture on the free plan — it will not work
and will require rebuilding after an upgrade.

---

### Playbook B3: "Kit automation failed / subscriber list corrupted"

**Trigger**: The Kit automation was working in testing but on launch day the sequence is no
longer sending, OR Kit shows subscriber count as 0 when you know subscribers have signed up,
OR Kit shows an account-level error ("your account has been suspended" or "your broadcasts
are paused").

**Subscriber list recovery:**

If subscriber count appears to be 0 but you know signups occurred:
1. Check Kit > Subscribers and set the filter to "All" (not "Active only"). Subscribers are
   sometimes filtered to "Active" by default, hiding those who unsubscribed or were deleted.
2. Check if subscriber "status" shows as "Complained" or "Bounced" — these are hidden from
   the default active view.
3. If you had previously exported a subscriber list (CSV export from Kit > Subscribers >
   Export), this is your backup. Re-import via Kit > Subscribers > Import subscribers.

**Automation failure recovery:**

If the sequence stopped sending after previously working:
1. Go to Kit > Automations > Sequences and check the sequence status. If it shows "Paused,"
   click "Resume."
2. Check Kit > Activity to see when the last successful email send occurred and which
   subscriber received it. This tells you where in the sequence the break happened.
3. If specific subscribers appear to have been skipped: click each subscriber name and view
   their individual activity log. Kit shows whether an email was skipped (and why — typically
   because the subscriber previously unsubscribed and re-subscribed, which pauses the sequence
   for that subscriber by default).

**Account suspension recovery:**

If Kit shows a suspension or review hold:
1. This is extremely rare on new accounts with educational content. The most common trigger
   is a spam complaint rate above 0.1%.
2. Contact Kit support immediately at support@kit.com. Provide your account email
   (wanka95@gmail.com) and describe that this is a newly created account for a launch day.
3. While waiting for Kit response: execute the Gmail manual broadcast fallback.

**Gmail manual broadcast fallback (launch day only):**
- Open Gmail (wanka95@gmail.com)
- BCC all known subscriber email addresses
- Subject line: copy exactly from `marketing/email-and-launch-plan.md` Launch Broadcast section
- Body: copy exactly from the same file's Launch Broadcast section
- Send at 12:00pm as planned
- This is a one-time fallback. It is not scalable beyond 50-100 addresses, but covers the
  launch day window while Kit issues are resolved.

**Escalation trigger**: If Kit's subscriber data appears to have been deleted (not filtered),
contact Kit support and request a data restore. Kit retains deleted subscriber data for 30
days. Log the escalation time in WORKLOG.md.

---

## Part C: Launch Day Contingencies — May 30

---

### Playbook C1: "Etsy listing won't publish"

**Trigger**: At 10:00am on May 30, you click "Publish" on a Draft listing in Etsy Shop Manager
and the listing either shows an error, stays in Draft state, or disappears.

**Step 1 — Detection checklist. Verify each field before contacting Etsy:**

Work through this list in order. Most publish failures are caused by one of these:

1. Title: must be 1-140 characters. Etsy rejects titles over 140 characters. Count yours.
2. Tags: must be exactly 13 tags, each under 20 characters, no special characters (no #, no @).
   Etsy is strict about this. Open the listing and verify the Tags field.
3. Primary image: Etsy requires a minimum 2000px on the longest side. If your image is
   under 2000px, Etsy will block publication. Verify image dimensions in the listing's Photos
   section.
4. Price: must be entered and must be greater than $0.00. Verify the Price field is not blank.
5. Quantity: must be at least 1 (for digital downloads, Etsy typically auto-sets quantity).
   Verify it is not 0.
6. Digital file: for a digital download listing, at least one PDF must be attached. Verify
   the listing's "Digital files" section shows the attached PDF with a green checkmark.
7. Shipping profile: digital download listings should be set to "Digital — no shipping." If
   a physical shipping profile is attached, Etsy may block publication or create a confusing
   listing. Verify under "Shipping."

**Immediate fix — 5 minutes:**
- Identify which field is causing the error (Etsy usually highlights it in red).
- Fix that field and click Publish again.
- Most errors clear in one fix cycle.

**Full recovery — 30-60 minutes (for persistent or unclear errors):**
1. If Etsy shows "Your shop is not open for business": your Shop Manager setup is incomplete.
   Go to Shop Manager > Settings > About your shop and verify shop name, description, and
   payment method are set.
2. If Etsy shows an account verification hold: this is the Track A risk documented in
   MAY_30_RISK_AND_CONTINGENCY_PLAN.md Sub-Risk 2D. Execute the Gumroad fallback:
   - Create a Gumroad account at gumroad.com using wanka95@gmail.com (15 minutes)
   - List the guides at identical prices
   - Update the Kit broadcast email to point to Gumroad URLs before the 12:00pm send
   - Update social bio links to the Gumroad storefront
3. If Etsy is having a platform outage: check status.etsy.com. Wait and retry in 30 minutes.

**Escalation trigger**: If you have fixed all fields and the listing still does not publish,
contact Etsy seller support at etsy.com/help > Contact Etsy Support. Describe the listing ID
and error message. Etsy's seller support response is typically 24-48 hours — too slow for
same-day resolution. Execute the Gumroad fallback in parallel.

---

### Playbook C2: "Kit email broadcast send failed"

**Trigger**: At 12:00pm you click "Send" on the launch broadcast in Kit, and one of these
happens: (a) Kit shows an error message, (b) the broadcast status stays at "Scheduled" and
does not change to "Sending" by 12:05pm, (c) the broadcast status shows "Failed."

**Detection — check Kit broadcast status at 12:05pm:**
1. Go to Kit > Broadcasts. Find your launch broadcast.
2. Status "Sending" or "Sent": success, no action needed. Check delivery stats at 12:30pm.
3. Status "Scheduled" at 12:05pm: the send time may be off by timezone. Click "Send now"
   to override the schedule.
4. Status "Failed": click into the broadcast and look for the failure reason Kit displays.

**Common failure reasons and fixes:**

"Sender address not verified": Go to Kit > Settings > Email. Verify that wanka95@gmail.com
is confirmed. Click "Resend verification email" and complete email verification before retrying.
Expected fix time: 5 minutes.

"Recipient list is empty": The broadcast was addressed to "All subscribers" but there are no
subscribers yet. This is not an error — it means no one has signed up before launch. The
broadcast sends to 0 recipients successfully (0 deliveries). Your list builds from social
traffic after the launch posts go up. No action needed.

"Send limit exceeded": Kit's free Newsletter plan allows unlimited sends but may temporarily
throttle very large single sends. For a new account under 100 subscribers, this will not trigger.

**Retry logic:**
- If the broadcast showed "Failed": do not click "Send" on the same broadcast again immediately.
  First identify and fix the failure reason (above), then click "Retry send" in Kit's broadcast
  interface, or create a new broadcast with identical content.
- Wait 2 minutes between retry attempts.
- If two retry attempts both fail: execute the Gmail manual broadcast fallback from Playbook B3.

**If Gmail fallback is needed (the complete procedure):**
1. Open Gmail (wanka95@gmail.com)
2. Compose new email
3. Subject: copy exactly from `marketing/email-and-launch-plan.md` Launch Broadcast subject line
4. Paste the launch broadcast body text
5. In the BCC field: add all known subscriber addresses (if any exist from pre-launch sign-ups)
6. Send at or as close to 12:00pm as possible. A 30-minute delay is acceptable.
7. Log "Kit broadcast failure — Gmail fallback used" in WORKLOG.md with exact time.

**Testing procedure before resending:**
After resolving the Kit failure cause, test with one email address before resending to all:
- Create a test broadcast to a single subscriber (yourself)
- Verify delivery, formatting, and link functionality
- Then send the full broadcast

---

### Playbook C3: "Social media posting failed"

**Trigger**: At 2:00pm or 3:30pm, the Buffer-scheduled post does not appear on Instagram,
TikTok, or Pinterest within 15 minutes of its scheduled time.

**Step 1 — Detection. Confirm it is a real failure, not a delay:**
1. Check each platform's native app or web interface directly. Buffer's queue and the live
   platform sometimes show a 5-10 minute lag. If the post is visible on the platform but not
   in Buffer's "Published" log, it succeeded.
2. Check Buffer > Published queue. If the post is listed as "Published" with a timestamp but
   you do not see it on the platform: the post is likely still indexing. Wait 10 minutes.
3. If Buffer shows "Failed" with an error code: proceed to platform-specific fixes below.

**Instagram-specific failures:**

"Account not connected" or "Authentication expired": Instagram requires periodic re-authorization
of third-party app connections (including Buffer). Fix: Go to buffer.com > Settings > Channels >
Instagram > Reconnect. You will be redirected to Instagram to re-authorize. This takes 2 minutes.
After reconnect, manually trigger the failed post from Buffer's queue.

"Image quality rejected": Instagram requires images to be at least 1080px on one side.
If the image was resized or the wrong variant was attached, use the image directly from
`projects/seedwarden/mockups/` — all mockup images are sized correctly.

**TikTok-specific failures:**

"Buffer does not support native TikTok upload": This is a documented limitation in
`TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md` Part 8. TikTok video posting from Buffer sends
a push notification reminder — Buffer cannot auto-post video to TikTok on the free plan.
Fix: upload the video file directly to TikTok from your phone. Caption from
`phase-2-social-content-calendar-60day.md` Day 30.

"Rate limit hit": TikTok limits very new accounts to a posting rate of approximately 1-2
posts per hour. If you receive this error, wait 1 hour and post again. This does not affect
launch-day posting since you are posting once.

**Pinterest-specific failures:**

"Board not found" or "No boards on account": Pinterest Business accounts require at least
one board before pins can be posted via Buffer. If no board exists: create one in Pinterest
(call it "Growing Guides" or "Seedwarden Field Guides"), then retry the Buffer post.
Expected time: 5 minutes.

"Auth token expired": Same as Instagram — reconnect Pinterest in Buffer > Settings > Channels.

**Manual posting fallback (applicable to all platforms):**

If Buffer cannot be fixed before 2:00pm, post manually. All content needed is already documented:
- Instagram: image from `mockups/` directory, caption from `phase-2-social-content-calendar-60day.md`
  Day 30, hashtags from `TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md` Part 8 hashtag sets
- TikTok: video or image file, shortened caption (under 200 characters)
- Pinterest: image file, description from `phase-2-social-content-calendar-60day.md` Day 30

Manual posting takes 5 minutes per platform. Do not delay launch waiting for Buffer to resolve.

**Escalation trigger**: If Instagram or Pinterest shows account-level restrictions (new account
flags, spam detection), log the restriction message in WORKLOG.md and proceed with content
posting on the other platforms. A single platform failure does not block launch.

---

### Playbook C4: "GA4 tracking not working / conversions not tracking"

**Trigger**: On May 30 evening (7:00pm-9:00pm), you check GA4 and see zero events, or the
Etsy listing pages are not appearing in GA4 reports, or expected events are missing.

**Step 1 — Detection. Understand what GA4 actually tracks on Etsy before diagnosing a problem:**

As documented in `etsy-ga4-event-tracking.md` Section 1, GA4 fires on Etsy listing pages
only when the GA4 Measurement ID is entered in Etsy Shop Manager. It does NOT track:
- Etsy homepage visits
- Etsy search results pages
- Cart or checkout pages
- Any event after the user leaves your listing page

This means GA4 reports may look sparse on Day 1 even when everything is working correctly.
A Day 1 view of 30 Etsy listing page views may translate to only 30 recorded GA4 events —
which appears empty in real-time reports but is correct.

**Detection checklist:**
1. In GA4, go to Reports > Realtime. Keep this open while you visit your own Etsy listing
   page in an incognito browser window. Do you see a pageview event appear within 30 seconds?
   If yes: GA4 is working correctly.
2. If no realtime event appears: your GA4 Measurement ID is either not entered in Etsy Shop
   Manager or is entered incorrectly.
3. Go to Etsy Shop Manager > Settings > Web analytics. Is your GA4 Measurement ID listed?
   It should begin with "G-" followed by 10 alphanumeric characters.
4. Verify the Measurement ID matches exactly what is in GA4 > Admin > Property settings.
   One wrong character will cause tracking to fail completely.

**Immediate fix — 5 minutes (Measurement ID missing or wrong):**
1. Open GA4 > Admin > Property Settings. Copy the Measurement ID (e.g., G-XXXXXXXXXX).
2. Open Etsy Shop Manager > Settings > Web analytics.
3. Paste the Measurement ID into the Google Analytics field.
4. Click Save.
5. Wait 60 seconds, then refresh your Etsy listing page in incognito.
6. Return to GA4 Realtime and verify an event appears.

**Full recovery — 30-60 minutes (if Measurement ID was correct but events are not appearing):**

Verify these in order:
1. GA4 data takes 24-48 hours to appear in standard reports (not Realtime). If Realtime shows
   events but standard reports do not: this is normal. Do not re-configure anything. Check
   standard reports on May 31.
2. GA4 custom dimensions (guide_type, acquisition_source, inferred_cohort as defined in
   `etsy-ga4-event-tracking.md` Section 2) will not appear until they are registered in
   GA4 Admin > Custom Definitions. If you have not done this yet, register them now following
   the step-by-step in that document's Section 2.2. Custom dimensions only populate on
   future events; past events will not be backfilled.
3. If GA4 is receiving events but attribution is showing "direct" for all traffic: add UTM
   parameters to Kit broadcast email links and social bio links. Without UTMs, GA4 cannot
   distinguish Kit traffic from Pinterest traffic. UTM parameter guide is in
   `google-analytics-integration-guide.md`.

**Backfill vs. start fresh:**

If GA4 was not configured before May 30 and you want historical context:
- Etsy Shop Manager stats (views, visits, orders) are your historical source. Export these
  from Shop Manager > Stats for the past 30 days.
- GA4 cannot be backfilled retroactively. GA4's value begins from the day the Measurement ID
  is correctly installed.
- Start fresh is the correct posture. Day 30 is Day 1 of your GA4 data. This is fine.

**Escalation trigger**: If GA4 Realtime shows events but standard reports are missing entire
event types after 48 hours: this is likely a custom dimension configuration issue. Review
`etsy-ga4-event-tracking.md` Section 2 against your GA4 Admin settings. No urgent action
needed — GA4 tracking is an analytical tool, not a launch-blocking requirement.

---

## Escalation Protocol — When to Ask for Help

For all playbooks above, escalate to the orchestrator agent if:
1. You have worked through the full recovery procedure and the failure persists after 60 minutes
2. You see an account-level suspension on Kit, Etsy, or a social platform (not just a posting
   error but an account status issue)
3. You need to make a cost decision (upgrade subscription) above $50 to resolve the failure

Log every escalation in WORKLOG.md with: timestamp, which playbook you executed, what step
failed, and what you need from the orchestrator. This makes the next session's context-setting
faster.

**The single most important principle on launch day**: A failure in one channel does not
require fixing before proceeding in another. If Kit broadcast fails at 12:00pm, post to
Instagram at 2:00pm as planned. If Instagram fails, post to TikTok. The Etsy listing is
the critical path item. Everything else adds reach to a working launch.

---

*Prepared: 2026-05-15. Seedwarden Agent. Item 60.
Platform constraint data sourced from TRACK_B_EXECUTION_READINESS.md (Item 57 audit, May 15).
References: MAY_30_RISK_AND_CONTINGENCY_PLAN.md, TRACK_B_USER_GATES.md, KIT_SETUP_NOTES.md,
TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md, MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md,
etsy-ga4-event-tracking.md.*
