---
title: "Seedwarden Launch Contingency Playbooks — May 24–30 Gate Framework"
prepared: 2026-05-19
supersedes: SEEDWARDEN_LAUNCH_CONTINGENCIES.md (2026-05-15 version, 12 playbooks, old gate numbering)
launch-date: 2026-05-30
status: production-ready
gate-framework:
  gate-1: "May 24 — Canva Brand Kit finalization + template sync"
  gate-2: "May 27-28 — Kit email automation setup + subscriber list verification"
  gate-3: "May 30 — Launch execution (Etsy go-live + email send + social posts)"
references:
  - SEEDWARDEN_MAY_27_29_PRELAUNCH_MASTER_CHECKLIST.md
  - SEEDWARDEN_EMAIL_LAUNCH_SEQUENCE_GUIDE.md
  - MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md
  - TRACK_B_EXECUTION_READINESS.md
  - MAY_30_RISK_AND_CONTINGENCY_PLAN.md
  - LAUNCH_DAY_QUICK_REFERENCE.md (companion one-page flowchart)
companion: LAUNCH_DAY_QUICK_REFERENCE.md
---

# Seedwarden Launch Contingency Playbooks
## May 24–30 Gate Framework — 16 Failure Mode Playbooks

**How to use this document**: This is your step-by-step recovery guide for every
foreseeable failure across the three gates. Each playbook follows the same structure:

1. **Trigger condition** — observable symptoms that confirm this is the right playbook
2. **Immediate action** — what to do in the first five minutes to prevent damage spreading
3. **Recovery path** — the complete fix with all steps
4. **Escalation** — when the failure exceeds autonomous resolution and requires the user

On launch day, do not read this cover to cover. Open `LAUNCH_DAY_QUICK_REFERENCE.md`
first. It will route you here to the correct playbook within five minutes.

**Minimum viable launch principle**: Etsy listings live constitutes a real launch. Every
other system adds reach to a working foundation. If one channel fails, all others continue
on schedule.

**Gate structure**:
- Part 1 (Gate 1, May 24): Canva Brand Kit and template sync — 4 playbooks
- Part 2 (Gate 2, May 27-28): Kit email automation — 4 playbooks
- Part 3 (Gate 3, May 30): Launch day execution — 4 playbooks
- Part 4: Tracking and escalation protocol

---

## PART 1: Gate 1 — Canva Brand Kit Finalization and Template Sync (May 24)

Gate 1 goal: Brand Kit is active, all 10 colors are accessible, logo is uploaded, fonts are
configured, and at least one zone card template exports correctly as a PDF.

---

### Playbook 1A: Color Limit Exceeded — Canva Blocks More Than 3 Brand Colors

**Trigger condition**: You open Canva Brand Hub and attempt to add a fourth, fifth, or any
additional color after the initial three, and Canva returns an upgrade prompt or a message
stating "not available on your current plan." This is a real platform constraint documented
in the May 13 Item 57 audit — Canva free tier stores exactly three colors in Brand Kit.

**How to confirm this is the right problem**: Attempt to add hex color number four. If Canva
shows a paywall or upgrade screen, the plan limit is confirmed. If Canva shows a spinner or
network error, do a hard-refresh first (Ctrl+Shift+R or Cmd+Shift+R) and retry before
concluding it is a plan limit.

**Immediate action — first five minutes**:

Do not close Brand Hub. Add these three colors to the Brand Kit before doing anything else:
- Deep Forest Green `#143b28` — header and border on every zone card and social graphic
- Warm Cream `#F5EDD6` — background on every zone card and social graphic
- Burnt Sienna `#A0522D` — accent and zone band header color

These three appear on every single asset. Locking them in Brand Kit means every click-to-Brand
Kit color action in a design session uses these without typing. Open a text file immediately
and paste all ten hex codes as a cheat sheet to keep open during every Canva session.

Full ten-color cheat sheet (paste this into a note and keep it open):
```
#143b28  Deep Forest Green     (headers, borders — every asset)
#1A3A2A  Deep Ink Green        (dark text elements)
#F5EDD6  Warm Cream            (background — every card)
#EDE0C4  Parchment             (secondary background)
#8FA882  Sage                  (supporting accents)
#A0522D  Burnt Sienna          (zone band accent — Zones 7-8-9-10)
#3D6B8A  Cool Band             (zone color — Zones 3-4)
#2D5016  Temperate Band        (zone color — Zones 5-6)
#C9943A  Warm Band             (zone color — Zones 7-8)
#A0522D  Hot Band              (zone color — Zones 9-10, same as Burnt Sienna)
```

**Recovery path (a) — manual hex entry for all remaining colors**:

For any color not stored in Brand Kit: click any colored element in the canvas to open the
color picker. At the bottom of the picker is a hex code text field. Click it and paste the
hex code directly. Canva remembers the last 20 custom colors in the "Recent colors" row for
the duration of that session — paste each code once and it becomes a one-click target for
all subsequent elements in that session. Overhead is approximately 20-30 seconds per design
session and under 30 seconds per new color. Across a full zone card production run of eight
cards and fifteen social graphics, total added time is under fifteen minutes.

**Recovery path (b) — export/paste method for color-consistent templates**:

Build one zone card at full spec using manual hex entry. Once complete, duplicate the design
in Canva (three-dot menu on design card > Duplicate). The duplicate retains all colors as
element-level overrides — no Brand Kit reference needed. Each zone variant is built by
duplicating the master and changing content, never by starting from scratch. This eliminates
repeated hex entry across the batch.

**Recovery path (c) — alternative tool assessment**:

If Canva color limits are creating unacceptable friction across a production run of 20+
designs, three alternatives exist:

- **Canva Pro ($15/month)**: Unlocks unlimited Brand Kit colors. Full color automation
  across the existing template set. Decision rule: if production volume is 20+ designs
  before June 7, the $15 cost is justified. Upgrade at canva.com/pro. Activation takes
  three minutes. Cancel before day 30 if ongoing cost is not warranted.
- **Figma (free tier)**: Supports full design systems and unlimited color variables.
  Migration cost: two to three hours to rebuild the Zone 5 master template in Figma.
  Asset output quality is identical. Justified only if Canva continues to fail after the
  Pro upgrade option is exhausted.
- **Affinity Publisher 2 ($70 one-time)**: Desktop-only, full professional typesetting and
  color management. Not recommended for a one-week sprint unless the user already owns it.

**Decision rule for tool pivot**: Use manual hex entry for 10 or fewer designs. Upgrade
Canva Pro for 11 or more. Consider Figma only if a paid Canva account is declined or
produces new errors. Log the decision in WORKLOG.md with the production volume count.

**Escalation**: If the manual hex entry workaround is failing (color picker does not accept
pasted hex values, Recent colors row does not retain values between design elements) and a
Canva Pro upgrade is declining, screenshot the error and log it in WORKLOG.md. Post a
screenshot to community.canva.com describing the behavior — response time under 24 hours.
For same-day launch unblocking: use pre-exported mockup images from `projects/seedwarden/mockups/`
for all social posts. These require no Canva session and are already launch-sized.

**Escalation threshold**: If both hex entry and Canva Pro are blocked and a tool pivot to
Figma would cost more than two hours before May 24 end of day, involve the user for a
tool pivot decision. This is the only scenario where Gate 1 Canva work cannot self-resolve.

---

### Playbook 1B: Template Upload Failure — File Size, API Limit, or Auth Error

**Trigger condition**: You attempt to upload the Seedwarden logo (`projects/seedwarden/logos/seedwarden_logo_1.png`),
a zone card asset, or any supporting image to Canva's Brand Kit or Uploads section and Canva
returns one of the following: "File too large," "Unsupported file type," "Upload failed —
please try again," or the upload spinner runs past 60 seconds and then disappears without
confirmation.

**How to confirm which failure mode**:
- "File too large" message: file size issue — go to Recovery A below
- "Unsupported file type" message: format issue — go to Recovery B below
- Spinner runs indefinitely or upload disappears: connectivity or API issue — go to Recovery C below
- Upload appears to complete but file is not visible in the Brand Kit or Uploads library:
  Canva API cache issue — go to Recovery D below

**Immediate action — first five minutes**:
1. Note the exact error message word for word. Different error messages require different fixes.
2. Do not attempt the upload more than twice without reading the error message — repeated
   upload attempts on a rate-limited API can extend the lockout period.
3. Verify the file path: `projects/seedwarden/logos/seedwarden_logo_1.png`. Confirm the file
   exists and is not zero bytes.

**Recovery A — file too large**:

Canva Brand Kit logo upload accepts files up to 25 MB. Canva design uploads accept files up
to 100 MB. The Seedwarden logo as a standard PNG should be well under 5 MB. If the file has
been modified and is unexpectedly large:
- Mac: open in Preview > Tools > Adjust Size. Set width to 1000 pixels. Export as PNG.
- Windows: open in Paint > Home > Resize. Set to 1000 pixels wide. Save as PNG.
- Any platform: use squoosh.app (free, no account). Upload the file, select PNG output,
  reduce quality to 85%. Download. File will be under 500 KB at any logo resolution.
After resizing, re-upload. A 1000px-wide PNG of the logo is fully adequate for all uses.

**Recovery B — unsupported file type**:

Canva Brand Kit logos accept PNG and SVG only. JPG files are rejected from the Brand Kit
logo section (though JPG works in regular design uploads). Verify the file extension is
`.png`. If you have a `.jpg` variant: open it in any image editor and export as PNG. If
using the file from the logos directory, the `.png` extension is correct — confirm the file
was not accidentally renamed.

**Recovery C — connectivity or API failure**:

1. Check status.canva.com. If an incident is listed and affects uploads: wait 30-60 minutes
   and retry. Do not attempt workarounds during a confirmed platform incident — partial
   uploads may corrupt the Brand Kit entry.
2. If no incident is listed: hard-refresh the browser (Ctrl+Shift+R). Clear the browser
   cache. Try uploading in an incognito window. Try a different browser.
3. If uploads fail across two browsers with no Canva incident: the issue is likely a local
   network proxy or corporate firewall blocking Canva's upload endpoint. Try uploading from
   a mobile device on a different network (mobile data) to isolate.

**Recovery D — file uploaded but not visible**:

Canva's uploads library has a known delay of up to 60 seconds on some accounts before
newly uploaded files appear. Wait one minute and refresh the uploads panel (click away from
the tab and back). If still not visible after two minutes: the upload likely failed silently.
Try uploading again after clearing the browser cache.

**If logo upload fails persistently and Gate 1 must proceed**: proceed without the logo in
Brand Kit. Add the logo to each design manually by going to Canva > Uploads > Upload files
directly within the design canvas. This is per-design overhead of approximately 30 seconds.
For a batch of eight zone cards, this adds under five minutes total.

**Escalation**: If uploads are failing systematically across all file types after two
browsers, a cache clear, and incognito mode, and status.canva.com shows no incident: log
the issue in WORKLOG.md with browser console error details (F12 > Console tab, copy any
red errors). Contact Canva support with the screenshot. Recovery time estimate is 24 hours.
For same-day Gate 1 continuation: proceed without Brand Kit logo upload. Zone card production
does not require the logo to be in Brand Kit — logo can be added element-by-element per design.

**Escalation threshold**: If upload failures persist for more than one hour and prevent any
zone card production work, escalate to user for platform decision. Upload issues that block
all Canva work for more than one hour represent a Gate 1 slip risk.

---

### Playbook 1C: Brand Kit Corruption — Colors Reset, Fonts Missing, or Kit Disappeared

**Trigger condition**: A Canva Brand Kit that was configured and working in a previous
session now shows as empty (no colors, no fonts), or the Brand Kit itself is not listed in
Brand Hub. This can occur after a session timeout, an account switch, or a Canva platform
update that clears user Brand Kits.

**How to confirm this is actually corruption vs. a navigation issue**:
1. Go directly to canva.com/brand-hub (not the sidebar link). Does the Seedwarden Brand Kit
   appear in the list?
2. If it appears but looks empty: click into it and wait 30 seconds. Slow connections cause
   Brand Hub to load colors and fonts with a visible delay. Do not act on an empty-looking
   Brand Kit without waiting the full 30 seconds.
3. If the Brand Kit is not in the list at all: check whether you are logged into the correct
   Canva account. The Seedwarden account is tied to wanka95@gmail.com. Log out and back in,
   then re-check Brand Hub.

**Recovery path — colors disappeared but Brand Kit is present**:

Re-enter all ten colors using the hex cheat sheet from Playbook 1A. With values already
known, re-entering the full color set takes under five minutes: click "Add a color," paste
hex code from the cheat sheet, click Save, repeat ten times. This is not data recovery — it
is re-entry. Budget five to ten minutes.

**Recovery path — fonts disappeared**:

Re-add by clicking "Add a font" in Brand Kit and searching by name:
- Playfair Display (heading font)
- Lato (body font — or Source Sans 3 as direct substitute if Lato is unavailable)
- Cormorant Garamond (accent font)

All three are Google Fonts available in Canva's free font library. If any font cannot be
found by exact name, search the first word of the name — "Playfair" or "Cormorant" — to
find the font family and select the correct variant.

**Recovery path — Brand Kit not found at all**:

This typically means the wrong Google account was auto-logged into Canva (common when
multiple accounts share a browser profile). Verify the account email in Canva's Profile >
Settings. If the wrong account is active: log out, log back in with wanka95@gmail.com,
and return to Brand Hub. The Brand Kit should reappear.

If the Brand Kit was genuinely deleted (which requires explicitly confirming a deletion
prompt — Canva will not delete a Brand Kit silently): rebuild from scratch using the hex
cheat sheet. Full rebuild from zero to complete Brand Kit: fifteen minutes. Log the
incident in WORKLOG.md.

**Recovery path — zone card design file disappeared from Canva**:

1. Canva > Home > Recent designs. Canva shows the 30 most recent designs by last-edited date.
2. Canva > Projects > All projects. Switch view from "Owned by me" to "All" in case the
   design was created in a workspace view.
3. If still not found: check canva.com/trash. Canva's trash retains deleted designs for 30
   days. Restore the design from trash.
4. If the design is permanently gone: rebuild the Zone 5 master from
   `CANVA_ZONE_CARD_DESIGN_GUIDE.md`. Budget two to three hours for the Zone 5 master rebuild
   and thirty-five to forty-five minutes per zone variant. Export each zone card as a PDF to
   `projects/seedwarden/assets/zone-cards/` immediately after completion — an exported PDF is
   permanent and independent of the Canva file.

**Rollback capability**: Zone card PDFs previously exported to `projects/seedwarden/assets/zone-cards/`
are the authoritative backup. Brand Kit corruption does not affect already-exported PDFs.
The kit is a production convenience, not the deliverable itself.

**Escalation threshold**: If the Brand Kit cannot be rebuilt (Canva account is inaccessible
despite correct login) and zone card production cannot begin within two hours, involve the
user. This represents a Gate 1 slip that will compress the May 27-28 Kit setup window.

---

### Playbook 1D: Template Sync Failure — Templates Not Reflecting Brand Kit Updates

**Trigger condition**: You update a color, font, or logo in the Canva Brand Kit, then open
an existing zone card design expecting the update to propagate automatically, but the design
still shows the old color values, old font, or old logo.

**Why this happens**: Canva Brand Kit updates do NOT automatically update existing designs.
Colors and fonts stored in the Brand Kit are applied to a design only when you actively
click a "Brand Kit" color swatch within that design's color picker, or select a Brand Kit
font from the font list. Previously edited elements that were colored by direct hex entry
or by previous Brand Kit values are not retroactively updated when the Brand Kit changes.
This is expected behavior, not a bug.

**Immediate action — first five minutes**:

Before assuming a sync failure, verify this is actually a propagation issue versus an
intentional design choice:
1. Open the zone card design.
2. Click any element that should reflect the updated Brand Kit color.
3. In the color picker, check whether the element's current color matches the old Brand Kit
   value or the new one. If it shows the old value, the element was not linked to the Brand
   Kit — it was set by direct hex entry or copied from a template with hard-coded colors.

**Recovery path — manual re-apply for changed colors**:

For each element in the design that needs the updated color:
1. Click the element.
2. Open the color picker.
3. Click the Brand Kit color swatch for the correct color. The element now uses the Brand
   Kit color. Future Brand Kit color updates will still NOT propagate — this is a Canva
   Free limitation. However, the element is now using the correct current value.

For a zone card with approximately thirty colored elements, re-applying Brand Kit colors to
all elements takes under ten minutes per card. For a batch of eight zone cards, this is
approximately eighty minutes of re-apply work — do this only if the color change was
significant (hex code actually changed, not just a minor adjustment).

**Recovery path — use "Replace color" to mass-update a color in one design**:

Canva's Edit > Replace color feature (available even on free) finds all instances of one
specific color in the current design and replaces them with another color. If one Brand Kit
color's hex code changed:
1. Go to Edit > Replace color in the design.
2. In the "Find" field, enter the old hex code.
3. In the "Replace with" field, enter the new hex code.
4. Click Replace. All elements using that color in the current design are updated in one
   action.

Limitation: this must be done in each design file individually — it does not affect other
design files. For eight zone cards, run Replace color in each of the eight design files.
Time: approximately two to three minutes per file.

**Recovery path — cache clear to force Brand Kit reload**:

If Brand Kit changes you made are not appearing in the Brand Kit panel itself (not the
design canvas), the issue is a stale cache in your browser's Brand Hub view:
1. Hard-refresh the page: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac).
2. If the Brand Hub panel still shows old colors after a hard refresh: log out of Canva,
   clear browser cookies for canva.com, log back in. The Brand Hub will reload from
   Canva's servers.

**Verification after sync**: After completing color or font updates across all eight zone
card designs, export one design as PDF and open it in a PDF viewer. Confirm the colors
match the hex cheat sheet values. A verified export is the confirmation that sync is complete.

**Escalation threshold**: Brand Kit sync is a visual consistency issue, not a launch blocker.
If the manual re-apply approach would cost more than two hours and the original hex values
were correct in the first place, skip Brand Kit re-linking and proceed with the designs as
they stand. Consistent colors that do not link back to Brand Kit are visually indistinguishable
from Brand Kit-linked colors. This is not an escalation scenario — proceed with the launch.

---

## PART 2: Gate 2 — Kit Email Automation and Subscriber List Verification (May 27-28)

Gate 2 goal: Kit automation sequence is Active, the three-test protocol passes (sign up,
Email 1 received, correct zone card link included), subscriber list is clean, and the May 30
broadcast is staged with confirmed send settings.

---

### Playbook 2A: Email Routing Failure — Wrong Segment Receives Wrong Email

**Trigger condition**: You run the three-test protocol (described in
`SEEDWARDEN_MAY_27_29_PRELAUNCH_MASTER_CHECKLIST.md` Day 2 Section) and one of the
following occurs: Email 1 does not arrive within five minutes; Email 1 arrives with the
wrong zone card link; Email 1 arrives but all zone links point to the same file; or the
email arrives in spam rather than the inbox.

**Diagnostic checklist — work through all five steps before making any changes**:

1. Kit > Automations > Sequences: is the automation status "Active"? If it shows "Draft"
   or "Paused," the sequence is not running. Click Activate and retest. This is the most
   common cause of Email 1 not arriving.

2. Kit > Subscribers: did the test subscriber appear after sign-up? If not, the form
   submission did not reach Kit. The problem is in the landing page form or form connection,
   not in the email sequence itself. Fix the form-to-Kit connection before debugging the
   sequence.

3. If the subscriber appeared: click their name. Did the zone tag apply (e.g., "zone-5")?
   If no tag was applied, the form's zone selector field is not connected to Kit's tag
   automation rule. Go to Kit > Forms > Edit form > the zone selector field must have a
   "Apply tag" action set for each zone option.

4. Check spam and junk folder for the test email address. Kit emails from a Gmail sender
   address sometimes land in spam for Gmail recipients on new accounts. If the email is in
   spam, the sequence is functioning correctly — deliverability is the issue, not routing.

5. In Kit > Subscribers > Activity log for the test subscriber: does "Email 1 sent" appear?
   If yes but the email is not in the inbox, it was sent and filtered. If no: the automation
   did not trigger. Confirm the sequence trigger is set to "When subscriber subscribes via
   [your landing page name]" and the delay on Email 1 is set to "immediately."

**Immediate action — routing is sending wrong zone card (after confirming Email 1 does arrive)**:

Wrong zone card delivery means the tag-to-email mapping is misconfigured. Each of the eight
zone tags must map to a distinct email variant. Go to Kit > Automations and verify each
conditional: "If subscriber has tag zone-5 → send Email 1 Zone 5 variant." Tag names must
match exactly — case-sensitive. A tag named `Zone-5` (capital Z) will not match an
automation rule that references `zone-5` (lowercase z). Inspect every tag name character
by character against the tags in Kit > Subscribers > Tags.

**Recovery path — wrong zone card routing**:

Fix each mismatched tag name. After fixing, delete the test subscriber from Kit and rerun
the full sign-up test. Verify tag application, then verify Email 1 content.

If finding and fixing the routing is taking more than 30 minutes: simplify to a single
Email 1 that lists all eight zone card download links clearly labeled by zone. This is the
all-zones fallback from Playbook 2B below. It costs zero additional setup time and delivers
the correct content to every subscriber regardless of zone tag. Implement this as the
launch-day email. Full conditional routing can be rebuilt and tested in Week 2.

**Recovery path — email landing in spam**:

For a Gmail-to-Gmail send on a new account, some spam filtering is expected for the first
few sends. This is a deliverability issue, not a routing issue. The email is being sent
correctly. For the pre-launch test, manually move the test email from spam to inbox and
note that real subscribers who opted in and are expecting the email are less likely to
have aggressive spam filters.

The long-term deliverability fix requires a custom domain (seedwarden.com) with SPF and
DKIM records pointing to Kit's mail servers. This is a Phase 3 improvement, not required
for May 30 launch.

**Escalation trigger**: If the Kit automation panel shows a persistent error that prevents
activation (not a configuration error but a platform error), screenshot the error and contact
Kit support at support@kit.com. Business-day first response is typically under four hours.
While waiting for support: proceed with the Gmail manual broadcast fallback described in
Playbook 2D. The Gmail fallback delivers the launch broadcast reliably with no automation
dependency.

**Escalation deadline**: If routing issues are unresolved by May 28 at 18:00 UTC, involve
the user. At that point the decision is whether to launch with the all-zones fallback email
(no routing, all links in one email — acceptable) or to delay Gate 2 to May 29 (cuts into
final QA time but is still compatible with May 30 launch).

---

### Playbook 2B: Conditional Logic Timeout — Kit Free Plan Blocks Conditional Automation

**Trigger condition**: You begin building the zone routing automation in Kit (the eight
zone-specific Email 1 variants triggered by zone tags) and Kit displays an upgrade prompt
on the conditional step, or the conditional fields are greyed out. Alternatively, you
complete the automation setup but the workflow shows "pending" for more than five minutes
without triggering, and the audit log shows a conditional step is stalling.

**How to confirm**: The Kit Newsletter free plan does not support conditional branching in
automations. This is confirmed in the Item 57 audit in `TRACK_B_EXECUTION_READINESS.md`.
If any conditional automation step shows an upgrade prompt, this is a real platform
constraint. Do not spend time debugging it — choose one of the three options below.

**Immediate action**: Stop attempting to build conditional routing on the free plan. The
feature requires Kit Creator at $33/month. Choose an option before continuing.

**Option 1 — All-zones single email (free plan, 10 minutes to implement, recommended)**:

Build one Email 1 that lists all eight zone card download links, clearly labeled by zone.
Subject line: `Your free Seedwarden zone card — download yours below`

Body:
```
Welcome to Seedwarden.

Your zone quick-start card is ready to download. Find your zone below and
click the link:

Zone 3 — [link]
Zone 4 — [link]
Zone 5 — [link]
Zone 6 — [link]
Zone 7 — [link]
Zone 8 — [link]
Zone 9 — [link]
Zone 10 — [link]

Not sure of your zone? Find it at: planthardiness.ars.usda.gov

— Seedwarden
```

Subscriber experience: one extra click (scan a list and find their zone) instead of the
ideal experience (direct link). For a launch list under 100 subscribers, this trade-off
is acceptable. No conditional logic required. Build this as a single Email 1 variant, set
the trigger to "subscriber subscribes via [landing page]," and set the delay to "immediately."

**Option 2 — Manual daily segmentation (free plan, labor-intensive)**:

After each day, check Kit > Subscribers for new sign-ups. Each subscriber's zone is
recorded as a custom field from the landing page form. Manually send the correct zone card
via Kit's one-time email feature to each subscriber who signed up that day. This approach
scales to approximately 30 new subscribers per day before the manual overhead exceeds
the time budget. Begin automating before the list exceeds 30 daily signups.

**Option 3 — Upgrade Kit Creator ($33/month)**:

Unlocks unlimited automations, sequences, and full conditional branching. After upgrading:
build the eight-variant Email 1 routing per `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md`.
Budget one additional hour for conditional rule configuration. Upgrade at kit.co > Settings >
Plan. Cancel if first-month revenue does not justify the ongoing cost.

**Recommendation**: Use Option 1 for launch. It costs nothing, takes ten minutes, and is
fully reliable. Build conditional routing in Week 2 once real subscriber zone distribution
data exists to validate the routing logic. Upgrade to Kit Creator at that point if the
subscriber volume justifies it.

**Note**: If you are reading this before May 27, choose your option now. Building
conditional routing architecture on the free plan and discovering the limit mid-session
on May 27 creates unnecessary pressure. Decide before starting Gate 2 work.

---

### Playbook 2C: Subscriber List Corruption — Import Failures, Duplicate Records, or Unsubscribes Not Honored

**Trigger condition**: Kit's Subscribers section shows a count that does not match
expectations: subscriber count is unexpectedly zero; count is far higher than sign-ups
would explain (suggesting duplicate records); subscribers who unsubscribed are still showing
as active; or an import from a CSV file returned an error or created duplicate entries.

**Diagnostic steps — confirm the failure mode**:

1. Kit > Subscribers filter check: the default view is "Active subscribers only." Subscribers
   who unsubscribed, bounced, or were marked as complained are hidden. Change the filter to
   "All subscribers" to see the full count including inactive records. If the "All" count
   matches expectations, no data was lost — the Active filter was hiding inactive subscribers.

2. Segment filter check: if a segment is selected in the Subscribers view, the count reflects
   only that segment. Clear all segment filters and recheck the total count.

3. Duplicate check: if the count is higher than expected, go to Kit > Subscribers and sort
   by email address. Duplicates appear as adjacent entries with identical email addresses.
   Kit does not merge duplicates automatically on import.

4. Import history: if a CSV import was recently attempted, check Kit > Subscribers > Import
   History for error details.

5. Unsubscribe honor check: Kit is legally required to honor unsubscribe requests within ten
   business days. In practice, Kit processes unsubscribes in real time. An unsubscribed
   address should immediately disappear from the Active filter. If an unsubscribed address
   is still showing Active, this is a system error — log it and contact Kit support.

**Recovery path — filter issue (subscribers present but hidden)**:

If the "All subscribers" filter restores the expected count, no data was lost. The Active
count is the usable launch-day list. Document what percentage of addresses are inactive and
note the reason (bounced, unsubscribed, complained) for post-launch deliverability review.

**Recovery path — duplicate records from a bad import**:

1. Export the full subscriber list: Kit > Subscribers > Export.
2. Open the CSV in a spreadsheet (Google Sheets or Excel).
3. Sort by email address column. Identify duplicate rows.
4. Delete duplicate rows, keeping the one with the most complete data (tags, custom fields).
5. Re-import the deduplicated CSV: Kit > Subscribers > Import subscribers > Upload CSV.
6. Kit matches records by email address on import and updates rather than re-creating
   entries for existing addresses.
7. After re-import, verify the subscriber count matches the deduplicated CSV row count.

**Recovery path — genuine data loss (subscriber list empty with no filter explanation)**:

If you previously exported the subscriber list as a CSV: re-import it via Kit > Subscribers >
Import subscribers > Upload CSV. Tags and custom fields in the CSV will be restored.

If no CSV backup exists and the list is small (under fifty subscribers, which is expected
for a pre-launch May 30 list): subscribers must re-sign-up. For any subscriber email
addresses you have in Gmail, send a re-sign-up request directing them back to the Kit
landing page with a brief explanation. For a list under fifty, this is a one-time manual
task of under thirty minutes.

**Prevention**: After Gate 2 testing is complete on May 29, export the subscriber list CSV
and save it to `projects/seedwarden/data/` named `kit-subscribers-backup-YYYY-MM-DD.csv`.
Repeat every Sunday after launch. This thirty-second export prevents all unrecoverable
data loss scenarios.

**Escalation trigger**: If Kit's interface shows subscriber data was deleted and no CSV
backup exists, contact Kit support at support@kit.com immediately. Kit retains deleted
subscriber data on their servers for thirty days and can restore from a backup. Provide
the account email (wanka95@gmail.com) and the approximate date and time of the data change.
Log the escalation date and time in WORKLOG.md.

---

### Playbook 2D: Automation Sequence Failure — Sequence Not Sending, Stuck, or Sending Duplicates

**Trigger condition**: During May 27-28 Gate 2 testing or on May 30 launch morning, one
of these automation states is observed: the Kit sequence shows a "Failed" or "Error" state;
new subscriber sign-ups are appearing in Kit but no Email 1 is sent; email send volume is
higher than subscriber count (indicating duplicate sends); or a sequence step has been
showing "pending" for more than ten minutes.

**Immediate action — first five minutes (sequence in error state)**:

1. Do not delete or recreate the sequence. Click into the failed sequence first to read the
   specific error message. Common error messages and their causes:
   - "Email step body missing or empty": the email body was accidentally deleted or was
     never populated. Restore the email content from `SEEDWARDEN_EMAIL_LAUNCH_SEQUENCE_GUIDE.md`.
   - "Sender address unverified": the sender email address lost its verification status.
     Kit > Settings > Email > Sender addresses > Resend verification email to wanka95@gmail.com.
     Complete verification in Gmail. This takes five minutes.
   - "Trigger not found": the form or tag that triggers the sequence was renamed or deleted.
     Verify the landing page name in Kit > Landing Pages matches the name referenced in the
     sequence trigger.

2. After fixing the error: click "Resume sequence" (not "Restart" — Restart will re-send
   to subscribers who already received emails). Run a sign-up test with a new test email
   address to confirm the fix.

**Immediate action — sequence Active but not triggering**:

1. Kit > Automations > Sequences: confirm the sequence status shows "Active," not "Draft"
   or "Paused."
2. Confirm the trigger: "When subscriber subscribes via [landing page name]." The landing
   page name is case-sensitive.
3. Run a test sign-up using a fresh email address not previously used in Kit. Check that
   the subscriber appears in Kit within 60 seconds.
4. In the subscriber's activity log: does "Email 1 sent" appear? If yes: Email 1 was sent,
   check the inbox, spam, and junk folder for that address. If no: the trigger is not
   firing — the most likely cause is a tag mismatch between the form's zone selector and
   the sequence trigger.

**Recovery path — duplicate sends**:

Duplicate sends indicate either: the subscriber signed up multiple times using the same
email (Kit creates a new subscription event for each form submission), or the sequence was
restarted rather than resumed after a failure (Restart re-sends all steps from the beginning
to all subscribers in the sequence).

For duplicate sends caused by a Restart:
1. Export the current subscriber list immediately to document who received duplicates.
2. Check the subscriber activity log for each affected address — note which emails were
   sent and how many times.
3. If more than five subscribers received duplicate emails: send a brief single-line
   acknowledgment email via Kit broadcast: "If you received multiple copies of our welcome
   email today, this was a technical error on our end. You're all set — only one copy was
   intended." Keep it matter-of-fact. Log the incident in WORKLOG.md.

**Recovery path — manual send triggering (automation cannot be fixed within 2 hours)**:

Kit allows sending a one-time email to a segment or individual subscribers outside of the
automated sequence. As a launch-day fallback:
1. Kit > Broadcasts > New Broadcast.
2. Select audience: "All subscribers" (or a specific tag if routing is needed).
3. Paste Email 1 content from `SEEDWARDEN_EMAIL_LAUNCH_SEQUENCE_GUIDE.md` Email 1 section.
4. Click Send.

This delivers the welcome email as a manual broadcast without requiring the automation
sequence to be functional. The subscriber still receives the correct content. The only
difference is that the remaining sequence emails (2-5) will not auto-send on the
configured delay schedule — schedule those as additional manual broadcasts on the
planned dates.

**Escalation trigger**: If the sequence is in a persistent error state that does not clear
after fixing the identified cause and resuming, and manual broadcast is also failing, contact
Kit support at support@kit.com. Provide the sequence name, the error message, and the
account email. While waiting: execute the Gmail manual broadcast fallback (open Gmail at
wanka95@gmail.com, compose with the launch broadcast subject line and body from
`SEEDWARDEN_EMAIL_LAUNCH_SEQUENCE_GUIDE.md`, BCC all known subscriber email addresses, send).

---

## PART 3: Gate 3 — May 30 Launch Day Execution

Gate 3 goal: All Etsy listings are live by 10:00am; Kit broadcast sends by 12:00pm; Instagram
and TikTok posts publish by 2:00pm; Pinterest pins publish by 3:30pm; GA4 and Etsy Stats
confirm tracking is active.

---

### Playbook 3A: Etsy Listing Publish Failure — Validation Error, Payment Issue, or Account Restriction

**Trigger condition**: At 10:00am on May 30, you click Publish on a draft Etsy listing and
one of the following occurs: Etsy returns an error message; the listing stays in Draft state
after clicking Publish; the listing publishes but is not publicly visible when you open the
URL in an incognito window; or Etsy displays an account-level banner about verification,
holds, or restricted selling.

**Immediate action — first five minutes (validation error)**:

Work through this field-by-field checklist before contacting Etsy. Every item is a known
publish blocker:

1. **Title**: must be 1 to 140 characters. Titles over 140 characters silently fail on some
   Etsy versions. Count the character length.
2. **Tags**: exactly 13 tags, each under 20 characters, no special characters (#, @, &, /,
   quotes). One invalid tag blocks the entire listing publish. Review each tag for length
   and special characters.
3. **Primary image**: minimum 2000 pixels on the longest side. Images below 2000px trigger
   a validation error. Check image dimensions in the Photos section of the listing editor.
4. **Price**: must be a positive number greater than $0.00. A blank or zero price blocks
   publication.
5. **Quantity**: for digital listings, Etsy typically auto-sets this to unlimited. Confirm
   it is not set to zero.
6. **Digital file**: at least one PDF must be attached with a green checkmark visible in the
   Digital files section. A listing with no attached file cannot publish.
7. **Shipping profile**: must be set to "Digital — no shipping." A physical shipping profile
   on a digital listing creates a conflict that may block publication.
8. **Category**: must be selected. Etsy requires a full category path (example: Books > Other).

After identifying and fixing each issue found: click Publish again. One fix cycle resolves
the vast majority of validation errors.

**Recovery path — persistent or unclear validation errors**:

If validation appears to pass but publishing still fails:
- Go to Etsy Shop Manager > Settings > About your shop. Confirm shop name, description,
  and default language are filled in.
- Go to Etsy Shop Manager > Finances > Payment settings. Confirm a payment method (PayPal
  or bank account) is verified with a green status indicator. Etsy requires a verified
  payment method before any listing can go public.
- Check status.etsy.com for an active platform incident. During an Etsy outage, publish
  attempts may fail silently or with generic errors. Wait 30 minutes and retry.

**Recovery path — account verification hold or identity verification request**:

Etsy identity holds prevent listing publication and typically take one to three business days
to resolve. This cannot be self-resolved on launch day. Execute the Gumroad fallback
immediately in parallel with contacting Etsy support:

1. Go to gumroad.com. Create an account with wanka95@gmail.com. Account creation: five minutes.
2. Create one product per guide at identical prices to the Etsy listings.
3. Set each product to "PDF file" type. Upload the guide PDF for each product.
4. Copy the Gumroad product URLs once each product is published.
5. Update the Kit launch broadcast email body to use Gumroad URLs before the 12:00pm send.
6. Update Instagram and TikTok bio links to the Gumroad store URL.
7. Proceed with the launch using Gumroad URLs. Migrate back to Etsy once the identity hold
   clears.

Gumroad setup to fully live: fifteen minutes.

**Escalation trigger**: If all fields are valid, the account has no holds, and the listing
still does not publish after two attempts: contact Etsy seller support via etsy.com/help >
Contact Etsy Support. Response time is 24-48 hours — too slow for same-day resolution.
Execute the Gumroad fallback simultaneously. Do not wait for Etsy to respond before pivoting.

**Escalation threshold**: Any account-level Etsy hold (payment verification, identity
verification, or seller restriction) requires user involvement. The user may need to complete
identity verification steps that require personal information only they can provide.

---

### Playbook 3B: Email Send Failure — Kit Rate Limiting, Auth Failure, or High Bounce Rate

**Trigger condition**: At 12:00pm on May 30, you click Send on the launch broadcast in Kit,
and one of these occurs: Kit returns an error message; the broadcast status stays at
"Scheduled" without updating to "Sending" by 12:05pm; the broadcast status shows "Failed";
or the broadcast reports as "Sent" but delivery metrics show zero emails opened or delivered
after thirty minutes.

**Immediate action — check broadcast status at 12:05pm**:

- Status "Sending" or "Sent": success. Check delivery stats at 12:30pm.
- Status "Scheduled" at 12:05pm: the timezone offset on the scheduled send time may have
  pushed the send by one hour. Click "Send now" in Kit's broadcast interface to override
  and send immediately.
- Status "Failed": click into the broadcast and read the specific failure reason.

**Common failure reasons and immediate resolution**:

"Sender address not verified": Kit > Settings > Email > Sender addresses. Click "Resend
verification email" to wanka95@gmail.com. Complete the verification in Gmail. Return to
Kit and retry the broadcast. Resolution time: five minutes.

"Recipient list is empty": the broadcast was addressed to "All subscribers" but the active
subscriber count is zero. This is not a failure — it means no subscribers are on the list
yet. The broadcast sends successfully to zero recipients. The list builds from social traffic
after launch posts go up. No action needed; the broadcast was technically successful.

"Sending limit reached" or "Daily send limit exceeded": Kit's free Newsletter plan allows
unlimited sends. This error should not appear on a new account. If it does appear: contact
Kit support at support@kit.com immediately and describe the situation. While waiting, execute
the Gmail fallback.

High bounce rate (>10% bounces on delivery metrics after 30 minutes): a bounce rate above
10% indicates the list contains invalid addresses from a bad import, or the sender domain
is being blocked. Review Kit's bounce report to identify the pattern. For a launch-day list
under 100 subscribers, even a 20% bounce rate means 80% successful delivery — proceed.

**Retry logic**:

Do not click Send on the same failed broadcast immediately. Identify the failure reason and
fix it first (steps above). Then:
1. Duplicate the failed broadcast in Kit (three-dot menu on the broadcast > Duplicate).
2. Use the duplicate as the retry attempt — this avoids any state corruption on the original.
3. Click Send on the duplicate.
4. Wait two minutes between retry attempts.
5. After two failed retries: execute the Gmail fallback.

**Gmail fallback — complete procedure**:
1. Open Gmail at wanka95@gmail.com.
2. Compose a new email.
3. Subject line: copy exactly from `SEEDWARDEN_EMAIL_LAUNCH_SEQUENCE_GUIDE.md` Launch
   Broadcast section.
4. Body: copy exactly from the Launch Broadcast section of the same file.
5. BCC field: add all known subscriber email addresses (export the Kit subscriber list CSV
   first; open in a spreadsheet; copy all email addresses from the email column).
6. Send as close to 12:00pm as possible. A 30-minute delay is acceptable and does not
   meaningfully affect conversion rate.
7. Log in WORKLOG.md: "Kit broadcast failed at [time]. Gmail fallback sent at [time]."

**Escalation trigger**: If Kit broadcast fails and Gmail fallback is used and more than
50% of the subscriber list is affected by bounce or delivery failure, involve the user.
At that scale, the issue may indicate a sender domain reputation problem that requires
a domain-level fix (SPF, DKIM) rather than a retry.

---

### Playbook 3C: Social Media Posting Failures — Auth Expiry, Rate Limiting, or Formatting Errors

**Trigger condition**: At 2:00pm (Instagram, TikTok) or 3:30pm (Pinterest), a post
scheduled in Buffer has not appeared on the platform within fifteen minutes of its scheduled
time, or Buffer shows the post as "Failed" with an error code.

**Immediate action — before assuming failure**:

Check the platform directly — not just Buffer. Visit Instagram.com, TikTok.com, and
Pinterest.com in a browser. Buffer's publish confirmation and the live platform can show
a lag of five to ten minutes. If the post is visible on the platform, the post succeeded.
Buffer's "Failed" status may be a reporting delay, not a real failure. Only proceed with
recovery if the post is absent from the platform after fifteen minutes.

**Platform-specific recovery**:

**Instagram**:
- "Authentication expired" or "Account not connected": Buffer > Settings > Channels >
  Instagram > Reconnect. You will be redirected to Instagram for re-authorization. This
  takes two minutes. After reconnecting: go to Buffer's queue, find the failed post, and
  click "Share now" or "Add to queue."
- "Content policy violation" or "Image rejected": remove any text overlay from the image
  and repost. Educational botanical content with no promotional text overlay does not
  typically trigger Instagram content policy. This error is rare for this content type.
- Instagram Reels auto-post limitation: Buffer free plan may not support Reels auto-post.
  If a Reel is scheduled and fails: post it directly via the Instagram mobile app using
  the video file and caption from the content calendar.

**TikTok**:
- Buffer's free plan cannot auto-post video to TikTok. Buffer sends a push notification
  reminder to your phone prompting manual upload. If the notification did not arrive: upload
  the video file directly via TikTok's native app (iOS or Android) or via tiktok.com in
  a browser. Use the caption from `phase-2-social-content-calendar-60day.md` Day 30.
  This is the expected flow for TikTok on Buffer free — there is no failure state here,
  only a manual step.

**Pinterest**:
- "No boards found" or "Board required": Pinterest requires at least one board. If no board
  exists: go to Pinterest.com > Create > Create board. Name it "Growing Guides" or
  "Seedwarden Field Guides." Return to Buffer and retry the failed post. Fix time: five minutes.
- "Authorization expired": Buffer > Settings > Channels > Pinterest > Reconnect. After
  reconnecting, retry the failed post from Buffer's queue.
- Pin format error: Pinterest pins require an image with a 2:3 ratio preferred. If a
  landscape image fails to post: use a portrait-format version from `projects/seedwarden/mockups/`.

**Manual posting fallback (all platforms, five minutes per platform)**:

If Buffer cannot be resolved before the posting window, post manually. This produces an
identical result to Buffer-scheduled posts:
- Instagram: upload image from `projects/seedwarden/mockups/`. Paste caption and hashtags
  from `phase-2-social-content-calendar-60day.md` Day 30. Confirm bio link points to Kit
  landing page URL.
- TikTok: upload video or image file in TikTok app. Use shortened caption under 200 characters.
- Pinterest: upload image in Pinterest web interface. Paste pin description from content
  calendar. Link the pin to the Kit landing page URL.

Do not delay the launch waiting for Buffer to resolve. Manual posting takes five minutes
per platform and produces identical audience-facing results.

**Multiple platform failures occurring simultaneously**: If two or more platforms are
failing at the same time (e.g., Instagram and Pinterest both failing), the most likely
cause is a Buffer account-level issue rather than individual platform auth failures. Go to
Buffer > Settings > Channels and reconnect all platforms in sequence. If Buffer's own
interface is unreachable, check status.buffer.com. If Buffer is down: post manually to
all platforms as described above. Buffer's scheduling convenience is not a launch blocker.

**Escalation threshold**: If both Buffer and all manual posting attempts fail on two or
more platforms, involve the user. This typically indicates a platform-level issue (account
suspended, device issue, network block) that requires interactive troubleshooting.

---

### Playbook 3D: Tracking Setup Failure — GA4 Events Not Firing, API Not Connected, Metrics at Zero

**Trigger condition**: On May 30 at 9:00pm (end-of-day check), GA4 shows zero events or
zero traffic; Etsy's own analytics are not recording listing page views; or the dashboard
shows unexpectedly blank metrics despite confirmed social traffic.

**Critical scoping note — read before diagnosing**:

GA4 does NOT track Etsy cart, checkout, or purchase pages. GA4 only tracks Etsy listing
page views when your Measurement ID is entered in Etsy Shop Manager > Settings > Web analytics.
This means:
- GA4 cannot track purchases, adds to cart, or checkout completions on Etsy's pages.
- Etsy Shop Manager > Stats is your authoritative source for sales, revenue, and conversion data.
- GA4's role on Etsy is tracking listing page views and inferring traffic sources from UTM
  parameters in links.
- Standard GA4 reports lag 24-48 hours. GA4 Realtime is the only same-day view.
- Zero events in standard reports on Day 1 is entirely normal even when everything is working.

**Immediate action — verify tracking is actually active (five minutes)**:

1. Open GA4 > Reports > Realtime.
2. In a separate incognito browser window, open your Etsy listing URL.
3. Wait 30 seconds.
4. Return to GA4 Realtime. Does a pageview event appear with the Etsy listing URL as the
   page? If yes: GA4 is working. Standard reports will populate by May 31.
5. If no event appears in Realtime: proceed to the diagnostic steps below.

**Diagnostic — Measurement ID missing or wrong**:

1. Go to Etsy Shop Manager > Settings > Web analytics. Is your GA4 Measurement ID
   (begins with "G-") entered? If blank: GA4 is not connected to Etsy at all.
2. Open GA4 > Admin > Property settings. Copy the Measurement ID.
3. Compare the Measurement ID in GA4 against what is in Etsy Shop Manager, character by
   character. One wrong character (transposed digit, lowercase vs uppercase) causes
   complete tracking failure.

**Fix — Measurement ID missing or incorrect (five minutes)**:

1. Open GA4 > Admin > Property settings > Measurement ID. Copy it.
2. Open Etsy Shop Manager > Settings > Web analytics.
3. Paste the Measurement ID. Click Save.
4. Wait 60 seconds.
5. Open your Etsy listing in incognito.
6. Return to GA4 Realtime. A pageview event should appear within 30 seconds.

**Fix — Measurement ID is correct but Realtime events still missing**:

This indicates either a network-level blocking of GA4 scripts, or an Etsy-side issue with
how the tag is being injected. First: confirm Etsy Shop Manager shows the Measurement ID is
saved (reload the Settings > Web analytics page after saving). If the ID disappears after
reload: there may be an Etsy account setting preventing tracking integration.

Check Etsy Shop Manager > Finances > Legal. Some Etsy regions require explicit consent
configurations that affect analytics. If this applies: document it in WORKLOG.md and move on.

**GA4 custom dimensions not appearing in reports**:

Custom dimensions registered in `etsy-ga4-event-tracking.md` (guide_type, acquisition_source,
inferred_cohort) must be created in GA4 Admin > Custom Definitions before they appear in
reports. Custom dimensions only populate for future events — they do not backfill historical
data. If they are missing from reports: register them in Custom Definitions and allow 48
hours. This does not require any action on May 30.

**All traffic showing as "Direct" in GA4**:

If GA4 shows sessions but all show as Direct (no source attribution): UTM parameters are
missing from the links in the Kit broadcast email and social bio links. Without UTM
parameters, GA4 cannot distinguish Kit email traffic from social traffic from direct browser
visits. Add UTMs to all campaign links going forward. The UTM structure is documented in
`google-analytics-integration-guide.md`. Retroactive backfill is not possible for May 30
data already collected without UTMs.

**Escalation trigger and priority**:

GA4 is an analytics tool, not a launch requirement. If GA4 is not tracking on launch day,
the launch is unaffected. Etsy Shop Manager provides sales and revenue data. Fix GA4 in the
48 hours after launch using the Realtime test described above. Log the issue in WORKLOG.md
with a flag to verify in the June 1 checkpoint. This is a low-priority post-launch cleanup
item, not an escalation trigger for launch day.

**Exception**: If Etsy's own statistics (Etsy Shop Manager > Stats > Views) also show zero
listing views despite confirmed social traffic to the listing URL, this indicates an Etsy
account issue, not a GA4 issue. In this case: verify the listings are publicly accessible
(open each listing URL in incognito, confirm you see the listing with "Add to cart" button).
If a listing that was published at 10:00am is now returning "This item is unavailable,"
re-publish it immediately using the steps in Playbook 3A.

---

## PART 4: Escalation Protocol

---

### When to self-resolve versus when to escalate

Every failure mode above has a self-resolve path. The escalation paths are for situations
where the self-resolve path is exhausted or where a decision requires the user's authority
(financial decisions, personal account verification, or tool pivot decisions above the
$50 threshold).

**Escalate to the user immediately when**:

1. An Etsy account-level hold (identity verification, payment verification, seller restriction)
   is blocking listing publication. These holds require the user's personal information.
2. A cost decision above $50 is required to proceed (tool upgrade, API service, emergency
   graphic design resource).
3. Both Etsy and Kit are simultaneously failing and the Gumroad fallback is also encountering
   issues.
4. A social media account (Instagram, TikTok, Pinterest) has been suspended at the account
   level, not just a post failure.
5. GA4 Realtime shows zero events after the Measurement ID fix AND Etsy Stats also shows
   zero views for confirmed live listings.

**Escalate after self-resolution attempts when**:

1. Any single recovery playbook has been executed in full and the failure persists after
   60 minutes of active work.
2. A platform shows an account-level error (not a content posting error, but an account
   status message preventing all activity on that platform).
3. The multi-modal timing failure scenario is active (broadcast sent before Etsy listings
   are live) and Gumroad fallback setup is taking longer than thirty minutes.

**How to escalate**:

Write a log entry in WORKLOG.md with: timestamp, which playbook number was executed,
what step was reached in the recovery path, what specific error message or symptom persists,
and what decision or resource is needed from the user. This allows the next session or the
user to immediately pick up at the right point without repeating any diagnostic steps.

---

### Minimum viable launch definition

Etsy listings live and publicly accessible is a real launch. All other systems add reach
and analytics to a working product. If every other system fails on May 30 but the Etsy
listings are live, the launch happened.

```
Etsy listings live                         = LAUNCH IS REAL
+ Kit broadcast sent                       = EMAIL LAUNCH
+ 1 social post live (any platform)        = SOCIAL LAUNCH
+ GA4 tracking confirmed                   = ANALYTICS ACTIVE
```

---

## CROSS-REFERENCE: Related Documents

This document supersedes `SEEDWARDEN_LAUNCH_CONTINGENCIES.md` prepared 2026-05-15 (which
used a different gate numbering covering old Gate 2/Gate 3 Canva and Kit windows).

| Document | Scope |
|---|---|
| `LAUNCH_DAY_QUICK_REFERENCE.md` | One-page decision tree for May 30. Open this first on launch morning. |
| `SEEDWARDEN_MAY_27_29_PRELAUNCH_MASTER_CHECKLIST.md` | Three-day pre-launch checklist May 27-29. |
| `SEEDWARDEN_EMAIL_LAUNCH_SEQUENCE_GUIDE.md` | Complete 5-email copy and Kit setup. |
| `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md` | Hour-by-hour May 30 execution sequence. |
| `MAY_30_RISK_AND_CONTINGENCY_PLAN.md` | Gate-level risk summary (Sub-Risks 1A-3C). |
| `TRACK_B_EXECUTION_READINESS.md` | Item 57 platform constraints audit (Canva 3-color limit, Kit free plan limits). |
| `failure-mode-decision-tree.md` | Predecessor quick-reference (12 playbooks, old gate numbering). |
| `june-6-contingency-path.md` | Full slip path if May 30 launch is cancelled. |

---

*Prepared: 2026-05-19. Seedwarden Agent. Session following Items 91-92 (May 20 session).
Gate framework: Gate 1 (May 24, Canva), Gate 2 (May 27-28, Kit), Gate 3 (May 30, launch).
16 playbooks covering all failure modes across the three-gate May 24-30 window.
Companion: LAUNCH_DAY_QUICK_REFERENCE.md.*
