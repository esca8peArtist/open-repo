---
title: "Seedwarden Launch Contingency Playbooks — Gates 2, 3, and May 30 Launch Day"
prepared: 2026-05-15
launch-date: 2026-05-30
status: production-ready
scope: >
  12 playbooks covering Gate 2 (Canva, May 19-24), Gate 3 (Kit, May 27-28),
  and launch day (May 30) — Etsy, Kit broadcast, social, GA4, multi-modal timing.
references:
  - TRACK_B_USER_GATES.md
  - CANVA_ZONE_CARD_DESIGN_GUIDE.md
  - CANVA_SETUP_AND_EXECUTION_GUIDE.md
  - TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md
  - KIT_SETUP_NOTES.md
  - MAY_30_RISK_AND_CONTINGENCY_PLAN.md
  - MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md
  - etsy-ga4-event-tracking.md
  - LAUNCH_CONTINGENCY_PLAYBOOKS.md (predecessor document, Item 60)
---

# Seedwarden Launch Contingency Playbooks

**How to use this document**: This is your calm, step-by-step recovery guide for every
likely failure across the three gates (May 19-28) and launch day (May 30). Each playbook
covers one failure mode. The structure is always the same: trigger condition (how to know
it is really this problem), immediate action (first five minutes: stop damage), recovery
path (full fix), and escalation (when to involve the user versus when to self-resolve).

Work through only the playbook that matches your situation. Do not read this cover to cover
on launch day. Go directly to the section whose trigger matches what you observe, or use
`failure-mode-decision-tree.md` to navigate here in under five minutes.

**Quick-reference companion**: `failure-mode-decision-tree.md` is the one-page flowchart.
Start there. Come here for full procedures.

**Minimum viable launch principle**: Etsy listings live is a real launch. Everything else
adds reach. If only one system fails, the others proceed on schedule.

---

## PART A: Gate 2 — Canva Brand Kit (May 19-24 window)

---

### Playbook A1: Color Limit — Canva Free Plan Blocks More Than 3 Brand Kit Colors

**Trigger condition**: You open Brand Hub in Canva and attempt to add a 4th, 5th, or any
additional color after the initial three, and Canva blocks the action with an upgrade prompt
or a "not available on your current plan" message.

**How to confirm this is the real problem**: Attempt to add color number 4. If Canva shows
an upgrade/paywall prompt, this is confirmed as a plan limit, not a UI error. If Canva shows
a network error or spinner, do not conclude it is a plan limit yet — refresh first.

**Immediate action (first 5 minutes)**: Do not close the Brand Hub. Add the three most
critical colors to the Brand Kit before doing anything else:
- Deep Forest Green `#143b28` — header and border on every zone card and social graphic
- Warm Cream `#F5EDD6` — background on every card and pin
- Burnt Sienna `#A0522D` — accent and zone band header color

Open a plain text file or note and paste all 10 hex codes as a cheat sheet. Keep it open
in a second window for every Canva session. This takes two minutes and is the fallback for
the remaining 7 colors.

**Recovery path — manual hex entry workaround (no cost, works for all design volume):**

During each Canva design session, click any colored element to open the color picker. Click
the hex code field at the bottom of the color picker panel and paste the hex code directly.
Canva remembers your last 20 custom colors in its "Recent colors" row for the duration of
that session — paste each color once per session and it appears as a click target for
subsequent elements. This method adds approximately 20-30 seconds per design session, not
per element. Across a launch-week production run of 8 zone cards and 15 social graphics,
the total overhead is under 15 minutes.

The complete hex cheat sheet for all 10 Seedwarden colors:
```
#143b28  Deep Forest Green
#1A3A2A  Deep Ink Green
#F5EDD6  Warm Cream
#EDE0C4  Parchment
#8FA882  Sage
#A0522D  Burnt Sienna
#3D6B8A  Cool band (Zones 3-4)
#2D5016  Temperate band (Zones 5-6)
#C9943A  Warm band (Zones 7-8)
#A0522D  Hot band (Zones 9-10, same as Burnt Sienna)
```

**Recovery path — Canva Pro upgrade ($15/month, full Brand Kit):**

If you plan to produce more than 20 designs before June 7, upgrading for one month is worth
the trade-off. Canva Pro unlocks unlimited Brand Kit colors. After upgrade: add all 10 colors
to the Brand Kit at once, confirm they save correctly, then proceed with zone card production.
Cancel after the launch week if ongoing cost is not desired. Canva Pro also unlocks premium
elements, but none are needed for the Seedwarden spec — all required fonts and layouts are
free-tier assets.

**Decision rule**: Use manual hex entry if producing 10 or fewer designs before May 30.
Upgrade to Canva Pro if producing 20 or more. Zone card batch production (8 cards) is a
borderline case — either option works. Make this decision based on your time tolerance for
minor friction per session, not on strategic grounds.

**Escalation**: If both options fail (billing error on Pro, color picker not accepting hex
input), screenshot the error and log it in WORKLOG.md. Post to community.canva.com — responses
within 24 hours. For launch day: use pre-built mockup images from `projects/seedwarden/mockups/`
for all social posts. These require no Canva Brand Kit colors and are already sized correctly.

---

### Playbook A2: File Size or Format Error on Upload (Canva or Logo Upload)

**Trigger condition**: You attempt to upload the Seedwarden logo (`logos/seedwarden_logo_1.png`)
to the Brand Kit Logos section, or upload a zone card image asset, and Canva returns an error:
"File too large," "Unsupported format," or the upload completes but the file does not appear.

**How to confirm**: Note whether the error specifies a size limit or format restriction.
Canva's free tier accepts PNG, JPG, SVG, and PDF uploads up to 25 MB per file for logos
and up to 100 MB for design pages.

**Immediate action (first 5 minutes)**:
1. Check the file size: right-click the file > Properties (Windows) or Get Info (Mac).
   `seedwarden_logo_1.png` should be well under 5 MB as a PNG logo at screen resolution.
   If it has been modified and is unexpectedly large, continue to step 2.
2. Verify the file is PNG format. Canva's Brand Kit logo upload only accepts PNG and SVG.
   If you have a JPG variant of the logo, it will not upload to Brand Kit. Use the PNG file.
3. If the file is correct but the upload spinner runs indefinitely: hard-refresh the browser
   (Ctrl+Shift+R or Cmd+Shift+R) and try again. A second upload attempt after a hard refresh
   resolves most transient upload failures.

**Recovery path (file is too large or format is wrong)**:

Resize the file using any image editor without losing quality:
- On Mac: open in Preview > Tools > Adjust Size. Set width to 1000 pixels. Export as PNG.
- On Windows: open in Paint > Home > Resize. Set to 1000px wide. Save as PNG.
- Online alternative: squoosh.app (no install, free) — paste the file, set output to PNG,
  reduce if needed. Squoosh does not require an account.

After resizing, re-upload to Canva Brand Kit. The logo at 1000px wide is fully adequate for
display in the Brand Kit preview and for all social graphic and zone card production.

**If Canva API is down (upload fails across multiple file types and browsers)**:
Check status.canva.com. If an incident is listed, wait 30-60 minutes and retry. If no
incident is listed but uploads are failing, try a different browser or incognito mode before
assuming a platform outage.

**Escalation**: If logo upload fails persistently across two sessions and two browsers:
proceed without the logo in Brand Kit. Add the logo to each design manually by uploading it
directly to that design's canvas using Canva > Uploads > Upload files. This is a minor
inconvenience for production but does not affect any launched asset.

---

### Playbook A3: Brand Kit Corrupted or Reset (Colors and Fonts Disappeared)

**Trigger condition**: A Canva Brand Kit that was configured and working now shows no colors,
no fonts, or the Kit itself is no longer listed in Brand Hub.

**How to confirm**:
1. Navigate to canva.com/brand-hub directly (not via the sidebar search).
2. Does the "Seedwarden" Brand Kit appear in the list? If yes but appears empty: click into it
   and wait 30 seconds. Slow connections cause Brand Hub to load colors and fonts with a delay.
3. If the Brand Kit is not in the list at all: check whether you are logged into the correct
   Canva account. The account for Seedwarden is tied to wanka95@gmail.com. Log out and back in.

**Recovery path (Brand Kit lost colors or fonts)**:

Re-add all colors and fonts using the hex code cheat sheet from Playbook A1. With the values
already known, re-entering the full color set takes under 5 minutes: click "Add a color,"
paste hex code, click Save, repeat. Re-add fonts by clicking "Add a font" and searching by
name: Playfair Display (heading), Lato (body, or Source Sans 3 as substitute), Cormorant
Garamond (accent). Re-upload the logo from `projects/seedwarden/logos/seedwarden_logo_1.png`.

Recovery to full Brand Kit from scratch: 10 minutes at most.

**Recovery path (Brand Kit does not appear at all)**:

This means either the wrong account is logged in, or the Brand Kit was deleted. Canva does
not delete Brand Kits without explicit user action (confirming a deletion prompt). The most
likely cause is a different Google account being auto-logged into Canva. Verify the account
email in Canva's Profile settings before concluding the Kit was deleted.

If it was genuinely deleted: recreate the Brand Kit from scratch using the hex cheat sheet.
Time required: 10-15 minutes. Log the incident in WORKLOG.md.

**Recovery path (zone card design file disappeared)**:
1. Go to Canva > Home > Recent designs. Canva lists the 30 most recent designs by last-edited
   date. The Zone 5 master template should be here unless the design is older than your 30
   most recent.
2. Go to Canva > Projects > All projects. Switch from "Owned by me" to "All" if the design
   was created in a shared workspace.
3. If still not found: check the Trash. Canva's trash retains deleted designs for 30 days.
   Go to canva.com/trash and restore the file.
4. If the design is permanently gone: rebuild from the Zone 5 master specification in
   `CANVA_ZONE_CARD_DESIGN_GUIDE.md`. Budget 2-3 hours for the Zone 5 master rebuild.
   All subsequent zone variants take 35-45 minutes each.

**Prevention**: After completing each zone card, immediately export the PDF and save it to
`projects/seedwarden/assets/zone-cards/`. Once exported, a zone card PDF is permanent and
independent of the Canva file. A corrupted or missing Canva design file does not affect an
already-exported PDF.

---

### Playbook A4: Missing Images or Empty Zones in Final Zone Card Export

**Trigger condition**: You export a zone card PDF from Canva and upon opening it, zones of
the card are blank, images are missing, placeholder text is still visible (such as
`[ETSY-ZONE-CALENDAR-LINK]`), or the PDF renders differently than the on-screen preview.

**How to confirm**: Open the exported PDF in a PDF viewer (not Canva) and compare each section
against the zone card specification in `ZONE_QUICKSTART_CARD_SPEC.md`. Blank zones, gray
boxes where images should be, and all-caps bracketed text are all failure states.

**Immediate action (first 5 minutes)**:
1. If placeholder text is visible: do not distribute or upload this PDF. Return to Canva,
   find and replace every bracketed placeholder with the live URL. The two required live URLs
   before any zone card can be exported are:
   - Left footer: the live Etsy Zone Calendar listing URL
   - Right footer: the live Kit landing page URL
   Both URLs must be confirmed before final export. If either is not yet available, use a
   temporary staging URL and note the file as "DRAFT — do not send" until URLs are finalized.

2. If images are missing (gray boxes): Canva sometimes fails to render linked external images
   during export if there was a connection interruption. Return to the design, click each
   image element to re-trigger loading, wait for all images to show full resolution on screen,
   then re-export.

3. If a zone band section is blank: confirm the element exists in the Canva design by clicking
   the area — elements with white text on white backgrounds appear blank on screen but export
   correctly. Use Canva's Layers panel (Position > Layers) to verify all elements are present.

**Recovery path (structural export failure)**:

If the PDF consistently renders incorrectly across two export attempts:
1. Try downloading as PDF Print instead of PDF Standard. In Canva: Share > Download > File
   type: PDF Print. PDF Print renders all elements at higher fidelity.
2. Try downloading as a PNG image (Share > Download > PNG). Confirm the PNG looks correct.
   If PNG exports correctly but PDF does not, the issue is in Canva's PDF renderer, not your
   design. Use PNG exports and convert to PDF using any free PDF converter (ilovepdf.com or
   Adobe Acrobat free online).

**Escalation**: If exports are systematically failing across all formats: log in WORKLOG.md,
contact Canva support with a screenshot of the failed export, and proceed with PNG exports
as the temporary format. All zone card delivery links can point to PNG files — they are
viewable on any device and do not require Adobe Reader.

---

## PART B: Gate 3 — Kit Email Automation (May 27-28 window)

---

### Playbook B1: Email Routing Failure — Subscribers Not Receiving Correct Zone Card

**Trigger condition**: You run the three-test protocol (sign up via landing page, verify
Email 1 arrives) and either: the email does not arrive within five minutes, the email arrives
with the wrong zone card link, or the email arrives but all zone links go to the same card.

**How to confirm the failure point**:

Work through this diagnostic checklist before taking any action:
1. Check Kit > Automations > Sequences. Is the automation status "Active"? If it shows
   "Draft" or "Paused," the sequence is not running. Click Activate.
2. Check Kit > Subscribers. Did the test subscriber appear? If not, the form submission did
   not complete. The problem is in the landing page form, not the email sequence.
3. If the subscriber appeared: click their name. Did the zone tag apply (e.g., "zone-5")? If
   no tag was applied, the form's zone selector is not connected to the tag automation rule.
4. Check the test email's spam and junk folder. Kit emails from a Gmail sender address may
   land in spam for Gmail recipients on new accounts.
5. In Kit > Activity (the subscriber activity log), confirm "Email 1 sent" appears. If yes
   but the email is not in the inbox: it sent and was filtered. If no: the automation did not
   trigger at all.

**Immediate action (first 5 minutes — automation not triggering)**:
1. In Kit > Automations > Sequences, click into the sequence.
2. Verify the trigger reads: "When subscriber subscribes via [your landing page name]."
3. Verify Email 1 is the first step with delay set to "immediately."
4. Verify the sequence status is "Active."
5. Re-run the test with a different test email address.

**Recovery path (wrong zone card delivered)**:

Wrong zone card delivery means the tag-to-email routing rule is misconfigured. Each of the
eight zone tag values must trigger a distinct Email 1 variant. Go to Kit > Automations and
verify each rule: "Subscriber has tag zone-5 → send Email 1 Zone 5 variant." Tag names
must be exact character matches to the tags created in Kit > Subscribers > Tags. A tag
named `Zone-5` (capital Z) will not match an automation rule referencing `zone-5`.

If finding and fixing the routing takes more than 30 minutes: simplify to a single Email 1
that lists all eight zone card download links, one per zone, clearly labeled. The subscriber
clicks their own zone link. This is the Option 1 "all-zones email" approach from Playbook B2
below, and it is fully functional for launch.

**Recovery path (DKIM/SPF — email landing in spam)**:

Kit sends on behalf of wanka95@gmail.com. For a Gmail-to-Gmail send, delivery is managed by
Google's servers and delivers adequately for a small opted-in list. Spam filtering risk at
under 200 subscribers is low for educational content with a clear opt-in path. If emails
consistently land in spam:
- Go to Kit > Settings > Email > Email deliverability. Follow Kit's verification steps for
  your sender email address.
- The long-term fix for spam deliverability is a custom domain (seedwarden.com) with SPF
  and DKIM records pointing to Kit's mail servers. This is a Phase 3 improvement item, not
  required for May 30.

**Escalation trigger**: If Kit's automation panel shows an error that cannot be cleared, or
the sequence activates but consistently fails to trigger, take a screenshot and contact Kit
support at support@kit.com. Average first response time on business days is under 4 hours.
While waiting: proceed with the Gmail manual broadcast fallback in Playbook B4.

---

### Playbook B2: Conditional Logic Blocked — Kit Free Plan Cannot Route by Zone

**Trigger condition**: You begin building the zone routing automation in Kit (8 zone-specific
Email 1 variants triggered by zone tags) and Kit displays an upgrade prompt, a "limitations"
warning, or the conditional automation step fields are grayed out and uneditable.

**How to confirm**: The Kit Newsletter (free) plan's automation limits are confirmed in the
Item 57 audit in `TRACK_B_EXECUTION_READINESS.md`. Conditional branching in automations
requires the Kit Creator plan at $33/month. If you see an upgrade prompt on any conditional
automation step, this is a real platform constraint, not a UI error.

**Immediate action**: Stop attempting to build conditional routing on the free plan. Do not
spend time debugging it — the feature genuinely requires an upgrade. Choose one option below.

**Option 1 — Single all-zones email (free, 10 minutes to implement, recommended for launch)**:

Build one Email 1 that includes all eight zone card download links, clearly labeled by zone.

Subject line: `Your free Seedwarden zone card — download yours below`

Body structure:
```
Welcome to Seedwarden. Your zone quick-start card is ready.

Find your zone below and click the link to download your card:

Zone 3 — link
Zone 4 — link
Zone 5 — link
Zone 6 — link
Zone 7 — link
Zone 8 — link
Zone 9 — link
Zone 10 — link

Not sure of your zone? Enter your zip code at the USDA plant hardiness map:
planthardiness.ars.usda.gov

— Seedwarden
```

This is fully functional. The subscriber experience is one extra click (find their zone in
a list) versus one click (link goes directly to their zone's card). For a launch list of
under 100 subscribers, this is an acceptable trade-off. Build this as a single Email 1
variant with no conditional logic required.

**Option 2 — Manual daily segmentation (free, no automation, labor-intensive)**:

Check Kit > Subscribers once daily. Each new subscriber's zone is recorded as a custom
field from the landing page form. Manually send the correct zone card via Kit's one-time
email feature to each subscriber who signed up that day. This approach scales to approximately
30 subscribers before the manual overhead becomes unsustainable. Begin automating before
the list exceeds 30 new daily signups.

**Option 3 — Upgrade to Kit Creator ($33/month)**:

Unlocks unlimited automations, sequences, and full conditional logic. After upgrading: build
the 8-variant Email 1 routing per `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` specifications.
Budget one additional hour to set up conditional rules. Upgrade at kit.co > Settings > Plan.
Cancel if Zone 1 revenue does not justify ongoing cost.

**Recommendation**: Use Option 1 for launch day. It costs nothing, takes 10 minutes, and
is fully reliable. Upgrade to Creator and implement full conditional routing in Week 2 when
you have real subscriber zone distribution data to validate the routing logic.

**Note on timing**: If you are reading this before May 27 (Gate 3 start), choose your option
now. Do not begin building conditional routing architecture on the free plan and discover
the limit mid-session.

---

### Playbook B3: Subscriber List Corrupted or Count Appears as Zero

**Trigger condition**: Kit's Subscribers section shows zero subscribers when you know
signups have occurred, or the subscriber count drops suddenly during or after a test period.

**How to confirm**:
1. In Kit > Subscribers, check whether the view filter is set to "Active" only. This is Kit's
   default filter. Subscribers who unsubscribed, bounced, or were marked as complained are
   hidden from the Active filter. Change the filter to "All subscribers" to see the full count.
2. Check Kit > Subscribers > Segments. If a segment is selected, the count reflects only that
   segment. Clear any segment filters.
3. If you previously imported or exported subscribers, verify the import completed without
   errors: Kit > Subscribers > Import History.

**Recovery path — subscribers filtered but present**:

If switching to "All subscribers" restores the count, no data was lost. Document which
subscribers have unsubscribed or bounced and note that the "Active" count is the usable
launch-day list. Bounce-heavy lists indicate deliverability issues, not data loss.

**Recovery path — subscriber list genuinely lost or corrupted**:

If you previously exported the subscriber list as a CSV file from Kit > Subscribers > Export,
that file is your backup. Re-import it via Kit > Subscribers > Import subscribers > Upload CSV.
Kit will match records by email address and restore subscriber data including tags.

If no CSV backup exists: subscribers who signed up before the data loss must re-sign up. For
a pre-launch list of under 50 subscribers, this is a recoverable situation. Send a re-sign-up
request via Gmail to any subscriber email addresses you have access to, directing them to the
Kit landing page again.

**Prevention**: After Gate 3 testing is complete (May 29), export the subscriber list CSV
and save it to `projects/seedwarden/data/` as `kit-subscribers-backup-YYYY-MM-DD.csv`.
Repeat this export every Sunday after launch.

**Escalation trigger**: If Kit shows subscriber data was deleted and you have no CSV backup,
contact Kit support at support@kit.com immediately. Kit retains deleted subscriber data for
30 days and can restore it from their server backups. Provide the account email address and
the approximate date of the data loss. Log the escalation in WORKLOG.md.

---

### Playbook B4: Kit Automation Fails or Account Suspended on Launch Day

**Trigger condition**: On May 30 at 8:00am system check, Kit's automation sequence status
shows "Failed" or "Error," OR Kit displays an account-level message such as "Your account
has been suspended," "Broadcasting is paused pending review," or any red account banner.

**How to confirm and triage**:
1. Distinguish between sequence-level failure and account-level failure.
   - Sequence failed: Kit > Automations > Sequences shows a specific sequence with a red error
     state. The account itself is fine. Go to the recovery steps for sequence failure below.
   - Account suspended: a red banner appears at the top of any Kit page, or all broadcast and
     sequence options are greyed out. Go to the account suspension procedure below.

**Recovery path — sequence failed**:
1. Click into the failed sequence. Kit will show which email step failed and the error message.
2. Common failure reasons: email step body was deleted or corrupted, sender address became
   unverified, or a triggering tag was renamed. Each has a direct fix: restore the email body
   from `marketing/email-and-launch-plan.md`, re-verify the sender address in Settings > Email,
   or match the tag name exactly to the tag in Kit > Subscribers > Tags.
3. After fixing: click "Resume sequence" and run a test sign-up to confirm Email 1 triggers.

**Recovery path — account suspended**:

Account suspension on a new educational content account is rare but can be triggered by
automated spam filters if Kit's onboarding checks flag the account. Steps:
1. Contact Kit support immediately: support@kit.com. Describe that this is a brand-new account
   for a scheduled launch day, the account sends educational botanical/foraging content, and
   all subscribers are opted-in through a landing page form. Include the account email
   (wanka95@gmail.com) in the message. Kit's typical resolution time for wrongful suspension
   flags is 2-4 hours during business hours.
2. While waiting: execute the Gmail manual broadcast fallback.

**Gmail manual broadcast fallback (complete procedure)**:
1. Open Gmail at wanka95@gmail.com.
2. Compose a new email.
3. Subject line: copy exactly from `marketing/email-and-launch-plan.md` Launch Broadcast section.
4. Body: copy exactly from the Launch Broadcast section of the same file.
5. BCC field: add all known subscriber email addresses. For a pre-launch list under 50 people,
   BCC works without violating spam law. For larger lists, use Gmail's "Send to groups"
   feature or a second Kit account as a bridge.
6. Send at or before 12:00pm. A 30-minute delay is acceptable.
7. Log "Kit broadcast failure — Gmail fallback executed" in WORKLOG.md with the exact time.

**Escalation trigger**: If Gmail fallback is used and Kit suspension is not resolved by May 31,
flag for a platform migration to an alternative. Mailchimp's free tier supports up to 500
subscribers and includes basic automation — subscriber import from the CSV backup would move
the list in under 20 minutes.

---

### Playbook B5: Etsy Webhook Not Firing (Kit-Etsy Integration Failure)

**Trigger condition**: During testing or on launch day, a buyer completes an Etsy purchase
and does not receive the expected post-purchase email from Kit, OR the buyer's email is not
appearing in Kit > Subscribers after the purchase.

**Context**: Etsy does not natively integrate with Kit via webhook. Buyer email addresses
from Etsy purchases are not automatically transferred to Kit unless a third-party connector
(such as Zapier or Make) is configured and active. If no such connector was set up, this
is expected behavior, not a failure state.

**How to confirm**:
1. Check Kit > Subscribers for any known test buyer email address. If it is not present, the
   Etsy-to-Kit integration is not configured (this is the most likely situation for a new account).
2. Go to Etsy Shop Manager > Settings > Integrations. Check whether any third-party service
   (Zapier, Make) is connected.

**If no integration is configured (most likely scenario)**:

This is not a launch-blocking failure. The Kit landing page and welcome sequence handle email
capture for new subscribers independently of Etsy purchases. Etsy buyers receive their digital
files directly through Etsy's purchase confirmation email — they do not need Kit to access
their purchase.

The Kit list grows from social traffic to the landing page, not from Etsy purchases. Etsy
buyers who want to join the email list will sign up via the link in the product description
or social bio.

**If a Zapier/Make connector was set up but is not firing**:
1. Log into Zapier or Make and check the Zap/scenario status. Confirm it is enabled (not paused).
2. Check the automation's run history for the last 24 hours. Zapier and Make log every
   trigger attempt — a failed run will appear with an error message.
3. Common failures: Etsy connection token expired (re-authorize the Etsy connection in Zapier),
   Kit connection token expired (re-authorize the Kit connection), or the Zap hit a free-tier
   task limit.
4. If the Zap is over its free-tier task limit: upgrade Zapier for one month or rebuild the
   automation in Make (Make has a more generous free tier).

**Escalation**: If Etsy-to-Kit automation is broken and cannot be fixed in 30 minutes: disable
the Zap and run without the integration for launch week. Handle Etsy buyer tagging manually
once daily: check Etsy orders, add each buyer's email to Kit manually with the `phase-1-buyer`
tag. This approach scales to the launch-week volume.

---

## PART C: Launch Day — May 30

---

### Playbook C1: Etsy Listing Will Not Publish

**Trigger condition**: At 10:00am on May 30, you click Publish on a Draft listing in Etsy
Shop Manager and the listing either shows a validation error, stays in Draft state, disappears,
or publishes but is not publicly visible.

**Immediate action — field-by-field validation checklist (5 minutes)**:

Work through every field before contacting Etsy:

1. **Title**: must be 1 to 140 characters. Titles over 140 characters silently fail. Count yours.
2. **Tags**: exactly 13 tags, each under 20 characters, no special characters (no #, no @, no &).
   Etsy is strict — one invalid tag blocks the entire listing publish.
3. **Primary image**: minimum 2000 pixels on the longest side. Images below 2000px trigger a
   validation block. Check dimensions in the Photos section.
4. **Price**: must be a positive number greater than $0.00. A blank Price field blocks publication.
5. **Quantity**: for digital listings, Etsy typically auto-sets unlimited. Confirm it is not 0.
6. **Digital file attached**: at least one PDF must be in the Digital files section with a
   green checkmark. A listing with no attached file cannot publish.
7. **Shipping**: must be set to Digital — no shipping. A physical shipping profile on a digital
   listing creates a conflict that may block publication.
8. **Category**: must be selected. Etsy requires a category path (e.g., Books > Other).

After fixing each issue found: click Publish again. Most errors clear in one fix cycle.

**Recovery path — persistent or unclear errors**:

If Etsy shows "Your shop is not open for business" or "Complete your shop setup":
- Go to Shop Manager > Settings > About your shop. Confirm shop name, description, and
  language are filled in.
- Go to Shop Manager > Finances > Payment settings. Confirm a payment method is verified.
  Etsy requires PayPal or a bank account before listings can go public.

If Etsy shows a verification hold or identity verification request:
- This is the Track A risk documented in `MAY_30_RISK_AND_CONTINGENCY_PLAN.md` Sub-Risk 2D.
- Etsy identity holds take 1-3 business days to resolve. You cannot publish listings during
  a hold.
- Immediate fallback: Gumroad.
  1. Go to gumroad.com. Click "Start selling."
  2. Create an account with wanka95@gmail.com. Gumroad account creation takes under 5 minutes.
  3. Create one product per guide at identical prices to the Etsy listings.
  4. Set each product to "PDF file" type and upload the guide PDF.
  5. Copy the Gumroad product URLs.
  6. Update the Kit launch broadcast email to point to Gumroad URLs before the 12:00pm send.
  7. Update Instagram and TikTok bio links to the Gumroad store.
  8. The launch proceeds on Gumroad. Migrate back to Etsy after the identity hold clears.

If status.etsy.com shows a platform outage: wait 30 minutes and retry. Do not attempt to fix
listing fields during a platform outage — changes may not save correctly.

**Escalation trigger**: If all fields are valid and the listing still does not publish, contact
Etsy seller support via etsy.com/help > Contact Etsy Support. Etsy support response time is
24-48 hours — too slow for same-day resolution. Execute the Gumroad fallback in parallel
without waiting for Etsy's response.

---

### Playbook C2: Kit Email Broadcast Send Failed

**Trigger condition**: At 12:00pm you click Send on the launch broadcast in Kit, and one of
these occurs: Kit shows an error message; the broadcast status stays at "Scheduled" and does
not update to "Sending" by 12:05pm; the broadcast status shows "Failed."

**How to confirm and detect status at 12:05pm**:
- Status "Sending" or "Sent": success. Check delivery stats at 12:30pm.
- Status "Scheduled" at 12:05pm: the send time timezone setting may have offset the schedule
  by one hour. Click "Send now" to override and send immediately.
- Status "Failed": click into the broadcast for the failure reason Kit displays.

**Common failure reasons and immediate fixes**:

"Sender address not verified": Go to Kit > Settings > Email > Sender addresses. Click
"Resend verification email" to wanka95@gmail.com, complete verification in Gmail, then retry.
Fix time: 5 minutes.

"Recipient list is empty": The broadcast was addressed to "All subscribers" but there are
currently zero subscribers on the list. This is not a failure — it means no one has signed
up yet. The broadcast sends to 0 recipients without error. Your list builds from social
traffic after launch posts go up. No action needed.

"Send limit exceeded": Kit's free Newsletter plan allows unlimited sends. This error should
not appear for a new account. If it does: contact Kit support and provide your account email.

**Retry logic**:
- Do not click Send on the same failed broadcast immediately.
- Identify and fix the failure reason (above) first.
- Then click "Retry send" in Kit's broadcast interface, or create a new broadcast with
  identical content by duplicating the failed broadcast.
- Wait 2 minutes between retry attempts.
- After two failed retries: execute the Gmail manual broadcast fallback.

**Gmail fallback procedure**:
1. Open Gmail at wanka95@gmail.com.
2. Compose a new email.
3. Subject: copy exactly from `marketing/email-and-launch-plan.md` Launch Broadcast section.
4. Body: copy exactly from the same file.
5. BCC: all known subscriber email addresses.
6. Send as close to 12:00pm as possible. A 30-minute delay is acceptable.
7. Log in WORKLOG.md: "Kit broadcast failed at [time]. Gmail fallback sent at [time]."

---

### Playbook C3: Social Media Post Failed or Did Not Go Live

**Trigger condition**: At 2:00pm (Instagram, TikTok) or 3:30pm (Pinterest), a scheduled
post in Buffer has not appeared on the platform within 15 minutes of its scheduled time,
or Buffer shows the post as "Failed."

**How to confirm it is a real failure**:
1. Check the platform's native app or website directly (not just Buffer). Buffer's queue
   and the live platform can show a 5-10 minute lag. If the post is on the platform but not
   in Buffer's "Published" log, it succeeded.
2. If the post is visible on the platform: done. Buffer's reporting is delayed, not the post.
3. If Buffer shows "Failed" with an error code: proceed to platform-specific recovery below.

**Instagram-specific recovery**:

"Authentication expired" or "Account not connected": Instagram requires periodic re-authorization
of third-party connections including Buffer. Fix: Buffer > Settings > Channels > Instagram >
Reconnect. You will be redirected to Instagram for re-authorization. Takes 2 minutes. Then
manually trigger the failed post from Buffer's queue by clicking "Add to queue" or "Share now."

"Content policy violation" or "Image rejected": This rarely triggers for educational botanical
content. If it does: remove any text overlay from the image and repost.

**TikTok-specific recovery**:

Buffer cannot auto-post video to TikTok on the free plan. Buffer sends a push notification
reminder to your phone, which you use to complete the upload. If the notification did not
arrive: upload the video file directly from your phone or computer via TikTok's native upload
interface. Use the caption from `phase-2-social-content-calendar-60day.md` Day 30.

**Pinterest-specific recovery**:

"No boards found" or "Board required": Pinterest requires at least one board before pins
can be posted via Buffer. If no board exists: go to Pinterest > Create board. Name it
"Growing Guides" or "Seedwarden Field Guides." Then retry the Buffer post. Fix time: 5 minutes.

"Authorization expired": Reconnect Pinterest in Buffer > Settings > Channels > Pinterest.

**Manual posting fallback (all platforms, 5 minutes each)**:

If Buffer cannot be resolved before 2:00pm, post manually without Buffer:
- Instagram: upload image from `mockups/` directory, paste caption from
  `phase-2-social-content-calendar-60day.md` Day 30.
- TikTok: upload video or image file directly in the TikTok mobile app, use shortened caption
  (under 200 characters).
- Pinterest: upload image file in Pinterest, paste description from the content calendar.

Do not delay launch waiting for Buffer to resolve. Manual posting takes 5 minutes per platform
and produces an identical result to scheduled posting.

---

### Playbook C4: GA4 Tracking Not Firing or Showing No Data

**Trigger condition**: On May 30 evening (9:00pm end-of-day check), you check GA4 and see
zero events, the Etsy listing pages are not appearing in GA4 reports, or expected events from
social traffic are missing.

**Critical scoping note before any diagnosis**:

GA4 does NOT track Etsy cart, checkout, or purchase pages. GA4 only fires on Etsy listing
pages when your Measurement ID is entered in Etsy Shop Manager. This means:
- GA4 cannot track purchases, cart adds, or checkout completions on Etsy (Etsy's pages).
- Etsy Shop Manager > Stats is your purchase and revenue source of truth.
- GA4's role is tracking listing page views and inferring traffic sources from UTM parameters.
- Sparse GA4 data on Day 1 is normal even when everything is working correctly.

**Detection checklist**:
1. In GA4, go to Reports > Realtime. Visit your own Etsy listing page in a different browser
   window (use incognito so your session is not filtered out by GA4's own "exclude internal
   traffic" setting). Does a pageview event appear in Realtime within 30 seconds? If yes: GA4
   is working.
2. If no event appears in Realtime: go to Etsy Shop Manager > Settings > Web analytics. Is
   your GA4 Measurement ID (begins with "G-") entered?
3. Verify the Measurement ID is exactly correct. Open GA4 > Admin > Property settings. Copy
   the Measurement ID. Compare it character by character with what is in Etsy Shop Manager.
   One wrong character causes complete tracking failure.

**Immediate fix — Measurement ID missing or wrong (5 minutes)**:
1. Open GA4 > Admin > Property settings > Measurement ID. Copy it.
2. Open Etsy Shop Manager > Settings > Web analytics.
3. Paste the Measurement ID. Click Save.
4. Wait 60 seconds. Reload your Etsy listing in incognito.
5. Return to GA4 Realtime and verify an event appears.

**Recovery path — Measurement ID is correct but events are missing**:

GA4 standard reports lag 24-48 hours. If Realtime shows events, check standard reports on
May 31 (not May 30). This is expected behavior.

If custom dimensions (guide_type, acquisition_source, inferred_cohort from `etsy-ga4-event-tracking.md`)
are not appearing: they must be registered in GA4 Admin > Custom Definitions before they
populate in reports. Custom dimensions only apply to future events. They will not backfill.
Register them as documented in `etsy-ga4-event-tracking.md` Section 2.2 and allow 48 hours
for data to appear.

If all traffic shows as "Direct" with no source attribution: add UTM parameters to all Kit
broadcast email links and social bio links. Without UTMs, GA4 treats any non-Google click as
direct traffic. UTM guide: `google-analytics-integration-guide.md`.

**Backfill posture**: GA4 cannot be backfilled retroactively. May 30 is Day 1 of your GA4
data. Use Etsy Shop Manager stats for any pre-launch historical context.

**Escalation trigger**: GA4 is an analytics tool, not a launch requirement. If it is not
working on launch day, continue with the launch. Fix GA4 in the first 48 hours after launch
using the Realtime test described above. Log the issue in WORKLOG.md with a note to verify
in the June 1 checkpoint.

---

### Playbook C5: Multi-Modal Timing Failure — Emails Go Out Before Etsy Listing Is Live

**Trigger condition**: The Kit broadcast sends at 12:00pm as planned, but the Etsy listings
have not published yet (they were supposed to go live at 10:00am). Email recipients click
through to Etsy and see "This item is no longer available" or "Page not found."

**Why this scenario matters**: It is the most damaging launch-day failure mode. Email opens
peak within 15-30 minutes of send. If subscribers click broken product links during that
window, the first impression of Seedwarden is a 404 page. This destroys conversion rate for
the warm audience (the most likely buyers) and is difficult to recover from.

**Immediate action (first 5 minutes — if both Etsy and email launches are still ahead of you)**:

The standard sequence is: Etsy listings live at 10:00am, Kit broadcast at 12:00pm.
At 10:05am, before anything else, verify Etsy listings are publicly visible:
1. Open a new incognito browser window.
2. Navigate directly to each Etsy listing URL.
3. Confirm each listing shows "Add to cart" — not "This item is unavailable" or a 404 page.
4. If all listings are live: proceed to 12:00pm broadcast as planned.
5. If any listing is NOT live: do not send the broadcast until it is.

**Immediate action (first 5 minutes — emails already sent, Etsy not yet live)**:

If the broadcast has already gone out and Etsy is not live:
1. Do not send a follow-up correction email immediately. A second email within 30 minutes
   of the first looks like spam and degrades trust further.
2. In Kit > Broadcasts, check whether you can send a "correction" broadcast to the same
   audience. Kit allows sending a second broadcast to the same subscriber segment. Compose
   a correction email with subject: "Update — links are now live."
3. Work on getting Etsy listings published as fast as possible. Use the Etsy field-by-field
   checklist from Playbook C1 to identify and fix any publish blockers.
4. If Etsy will be live within 30 minutes: wait. Send the correction email once Etsy is
   confirmed live. Total window between initial send and correction: under 60 minutes.
5. If Etsy will not be live within 60 minutes (account hold, outage): send the Gumroad
   fallback links as the correction email. Gumroad setup takes 15 minutes.

**Correction email template**:

Subject: `Quick update from Seedwarden — corrected links inside`

Body: `A note on the email we just sent: the links are now live. Here are the correct product
links: [Etsy or Gumroad URL for each guide]. We appreciate your patience and look forward
to getting the guides in your hands today.`

Keep it short, matter-of-fact, and friendly. Do not over-apologize — one brief acknowledgment
is better than a long explanation.

**Prevention (the only reliable fix)**:

The 2-hour window between Etsy go-live (10:00am) and broadcast send (12:00pm) exists
specifically to prevent this failure mode. Never compress this window below 1 hour. On May 29
during the pre-launch check, verify all Etsy listing URLs load correctly in incognito and log
them in WORKLOG.md. Copy-paste all listing URLs into the Kit broadcast email during staging
so the links are confirmed before they are ever sent.

**Escalation trigger**: If Etsy listings are not live within 90 minutes of the broadcast send,
escalate to the orchestrator and deploy the Gumroad fallback immediately. Do not wait for
Etsy to self-resolve when email recipients have already received broken links.

---

## ESCALATION PROTOCOL

For all playbooks above, escalate to the orchestrator agent when:
1. You have worked through the full recovery procedure and the failure persists after 60 minutes.
2. Any platform shows an account-level suspension (not just a posting error, but an account
   status issue that prevents all activity).
3. A cost decision above $50 is needed to resolve the failure.
4. The multi-modal timing failure scenario (Playbook C5) is active and both Etsy and Kit are
   simultaneously failing.

**Log every escalation in WORKLOG.md with**: timestamp, which playbook was executed, which
step failed, and what you need from the orchestrator. This makes the next session's context
recovery faster and prevents repeated debugging of the same failure.

**The single most important principle on launch day**: A failure in one channel does not
require fixing before proceeding in another. If Kit broadcast fails at 12:00pm, post to
Instagram at 2:00pm as planned. If Instagram fails, post to TikTok. If social fails entirely,
the Etsy listing is still live and discoverable. The Etsy listing is the only hard requirement.

---

## CROSS-REFERENCE: Existing Contingency Documents

This document extends and complements the following earlier files. Do not duplicate work —
reference the applicable document for the scope described:

| Document | Scope |
|---|---|
| `LAUNCH_CONTINGENCY_PLAYBOOKS.md` | Item 60 predecessor: 8 playbooks for Gate 2, Gate 3, and launch day. Overlapping coverage; this document supersedes it with 12 playbooks and expanded detail. |
| `LAUNCH_DAY_DECISION_TREE.md` | Item 60 quick-reference decision tree. Updated version: `failure-mode-decision-tree.md`. |
| `MAY_30_RISK_AND_CONTINGENCY_PLAN.md` | Gate-level risk summary (Sub-Risks 1A-3C). Read once before May 20. |
| `TRACK_B_EXECUTION_READINESS.md` | Item 57 platform constraints audit. Source of Canva 3-color limit and Kit conditional logic limit documentation. |
| `june-6-contingency-path.md` | If May 30 launch is cancelled entirely: June 6 slip path. |

---

*Prepared: 2026-05-15. Seedwarden Agent. Exploration Queue Item 3.
12 playbooks covering all Gate 2, Gate 3, and May 30 launch day failure modes.
Platform constraint data from TRACK_B_EXECUTION_READINESS.md (Item 57 audit).
Predecessor: LAUNCH_CONTINGENCY_PLAYBOOKS.md (Item 60, 8 playbooks).*
