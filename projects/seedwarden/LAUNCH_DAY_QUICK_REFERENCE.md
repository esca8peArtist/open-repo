---
title: "May 30 Launch Day Quick Reference — One-Page Decision Tree"
prepared: 2026-05-19
launch-date: 2026-05-30
status: print-ready
use: "Open on May 30 morning. Keep visible throughout the day. When something fails, find the matching box and follow the arrow. Each path points to the full playbook in SEEDWARDEN_LAUNCH_CONTINGENCIES.md."
companion: SEEDWARDEN_LAUNCH_CONTINGENCIES.md
---

# May 30 Launch Day Quick Reference

Open this document at 8:00am on May 30. Keep it visible throughout the day.
When something goes wrong, scan the failure boxes below and follow the arrows.
"See Playbook" means: go to SEEDWARDEN_LAUNCH_CONTINGENCIES.md, Part 3, that section.

---

## LAUNCH SEQUENCE — REFERENCE TIMES

```
08:00   System checks: Kit Active, Etsy listings draft-ready, social logins confirmed
10:00   Etsy listings PUBLISH
10:05   VERIFY: open each listing URL in incognito → must see "Add to cart"
12:00   Kit broadcast SEND (ONLY after Etsy listings confirmed live at 10:05)
14:00   Instagram + TikTok posts publish
15:30   Pinterest pins publish
21:00   End-of-day check: Etsy Stats sales count, Kit signups, Instagram impressions
```

---

## FAILURE MODE TRIAGE

```
SOMETHING FAILED
       |
       v
  WHICH SYSTEM FAILED?
       |
  +----|------+----------+----------+----------+
  |           |          |          |          |
CANVA        KIT        ETSY      SOCIAL      GA4
(Gate 1)  (Gate 2)   (Gate 3)  (Gate 3)   (Gate 3)
  |           |          |          |          |
  v           v          v          v          v
[P1A-P1D]  [P2A-P2D]  [P3A,C5]  [P3C]      [P3D]
```

---

## GATE 1 FAILURES (Canva, May 24 window)

### P1A — Cannot add more than 3 Brand Kit colors
```
Canva blocks adding color 4+ with upgrade prompt?
    YES → This is the free plan 3-color cap. NOT a bug.
          IMMEDIATE FIX (5 min): Add these 3 to Brand Kit:
            #143b28  Deep Forest Green
            #F5EDD6  Warm Cream
            #A0522D  Burnt Sienna
          For remaining 7: paste hex manually into the color picker
          per design session. 20-30 sec overhead per session.
          OR: Canva Pro $15/mo → unlimited colors.
          Decision rule: manual hex if ≤10 designs, Pro if ≥11.
    NO (spinner or network error) → Hard-refresh browser, try incognito.
          Still blocked? → That is the plan limit too. Follow YES path.
    Escalate if: hex entry broken AND Pro upgrade declined → involve user.
    → Full procedure: Playbook 1A
```

### P1B — Upload fails (logo, template, or asset)
```
Error message says what?
    "File too large" → Resize to 1000px wide, export as PNG via Preview/Paint/squoosh.app
    "Unsupported format" → Convert to PNG. Brand Kit logos only accept PNG and SVG.
    Spinner never completes → Hard-refresh. Try incognito. Try different browser.
          status.canva.com shows incident? → Wait 30-60 min, retry.
    File uploaded but not visible → Wait 60 sec, refresh panel. Still missing: re-upload.
    All uploads failing across browsers, no Canva incident → Possible firewall. Try mobile data.
    FALLBACK: skip logo in Brand Kit. Add logo manually per design (30 sec/design).
    Escalate if: all uploads fail for >1 hour blocking all production → involve user.
    → Full procedure: Playbook 1B
```

### P1C — Brand Kit corrupted or disappeared
```
Brand Kit not in Brand Hub list?
    First check: are you logged into wanka95@gmail.com in Canva? Log out, log back in.
    Wrong account → log out and in → Brand Kit reappears → done.
    Right account, Kit still missing → Kit was deleted. Rebuild:
          Reenter all 10 colors from hex cheat sheet (5 min).
          Add fonts: Playfair Display, Lato, Cormorant Garamond.
          Re-upload logo from projects/seedwarden/logos/seedwarden_logo_1.png.
          Full rebuild: 15 min.
Brand Kit present but colors or fonts missing?
    Wait 30 sec for slow connection to load. Still empty after 30 sec → re-enter colors.
    Re-enter all 10 hex codes: 5-10 min. Re-add fonts: 3 min.
Zone card design file gone?
    Canva > Home > Recent designs → found? Open it. Done.
    Not in Recent → Canva > Projects > All projects → found? Open it.
    Not in Projects → canva.com/trash → restore if found.
    Not in Trash → rebuild from CANVA_ZONE_CARD_DESIGN_GUIDE.md. Budget 2-3 hrs Zone 5 master.
PREVENTION NOTE: Export each zone card as PDF to assets/zone-cards/ immediately after completion.
    An exported PDF is permanent and independent of the Canva file state.
    → Full procedure: Playbook 1C
```

### P1D — Templates not reflecting Brand Kit updates
```
Updated Brand Kit color but designs still show old color?
    This is EXPECTED. Canva does not auto-propagate Brand Kit changes to existing designs.
    Fix option A (per element): click element → color picker → click Brand Kit swatch. Repeat.
    Fix option B (mass replace): Edit > Replace color → enter old hex → enter new hex → Replace.
          Run in each affected design file individually.
    Fix option C: if original hex values were correct and visual difference is minor,
          SKIP re-linking. Consistent colors without Brand Kit links are visually identical.
          This is NOT a launch blocker. Proceed.
    → Full procedure: Playbook 1D
```

---

## GATE 2 FAILURES (Kit, May 27-28 window)

### P2A — Email routing broken / wrong zone card delivered
```
Test sign-up ran. Email 1 did not arrive within 5 min?
    Check spam/junk first.
    In spam → DKIM/SPF issue. OK for launch (opt-in list). Continue.
    Not in spam, not in inbox → go to Kit > Automations > Sequences:
          Sequence status = Draft or Paused? → Click Activate. Retest.
          Sequence Active? → Check: did test subscriber appear in Kit > Subscribers?
              NO → form-to-Kit connection broken. Fix landing page form connection first.
              YES → Did zone tag apply (e.g. "zone-5")? 
                    NO → form zone selector not connected to tag rule. Fix in Kit > Forms.
                    YES → check subscriber Activity log: "Email 1 sent" shows? 
                          YES → sent, check inbox/spam again.
                          NO → trigger not firing. Verify trigger name matches landing page EXACTLY (case-sensitive).
Email 1 arrives but delivers wrong zone card?
    Tag name mismatch. Check: kit tag "zone-5" vs automation rule "Zone-5"? Must match exactly.
    Fix takes >30 min? → Use all-zones fallback email (all 8 links in one email). See P2B Option 1.
    Escalation deadline: unresolved by May 28 18:00 UTC → involve user.
    → Full procedure: Playbook 2A
```

### P2B — Kit upgrade prompt blocks conditional automation
```
Kit shows "upgrade to use this feature" on any conditional step?
    YES → Free plan does not support conditionals. This is confirmed. Do not debug further.
    CHOOSE ONE NOW:
    OPTION 1 (recommended, free, 10 min):
          Build 1 Email 1 with all 8 zone card links listed by zone.
          No conditional logic required. Subscriber clicks their own zone.
          This is fully functional for a launch list under 100 subscribers.
    OPTION 2 ($33/mo):
          Upgrade to Kit Creator. Unlocks full conditional logic.
          Budget 1 extra hour for routing setup after upgrade.
    OPTION 3 (free, labor-intensive):
          Check Kit > Subscribers daily. Manually send correct zone card.
          Scales to ~30 new subscribers/day maximum.
    Default: Use Option 1 for launch. Build conditional routing in Week 2.
    → Full procedure: Playbook 2B
```

### P2C — Subscriber list count is wrong or list corrupted
```
Subscriber count looks wrong?
    First check: is the view filter set to "Active only"? Change to "All subscribers."
    Count restores? → No data lost. Inactive records were filtered. Proceed.
    Viewing a segment? → Clear segment filter. Recheck total.
Count higher than expected (possible duplicates)?
    Sort by email address. Identify duplicate rows.
    Export to CSV → deduplicate in spreadsheet → re-import.
Count is zero and should not be?
    Do you have a CSV backup? → Re-import via Kit > Subscribers > Import.
    No CSV backup? → For a list under 50: manually re-invite subscribers via Gmail.
    Contact Kit support if data was deleted: support@kit.com. They retain data 30 days.
PREVENTION: After May 29 Gate 2 testing, export subscriber list CSV to projects/seedwarden/data/.
    → Full procedure: Playbook 2C
```

### P2D — Kit sequence stuck, not sending, or sending duplicates
```
Sequence shows error state?
    Click into sequence. Read the error message.
    "Email body missing" → restore content from SEEDWARDEN_EMAIL_LAUNCH_SEQUENCE_GUIDE.md.
    "Sender address unverified" → Kit > Settings > Email > resend verification to wanka95@gmail.com.
    "Trigger not found" → landing page name in trigger must match actual landing page name exactly.
    After fixing → click "Resume sequence" (NOT Restart). Retest with fresh email address.
Sequence Active but not triggering?
    Confirm trigger: "When subscriber subscribes via [exact landing page name]."
    Run test sign-up. Check subscriber activity log for "Email 1 sent."
    Not logged as sent? → Tag name mismatch between form and trigger. See P2A.
Duplicate sends occurring?
    Likely caused by clicking "Restart" instead of "Resume" on a failed sequence.
    For >5 subscribers affected: send brief acknowledgment broadcast. See Playbook 2D.
Manual fallback (sequence cannot be fixed within 2 hours):
    Kit > Broadcasts > New Broadcast → paste Email 1 content → send to "All subscribers."
    Schedule emails 2-5 as additional manual broadcasts on the planned dates.
    → Full procedure: Playbook 2D
```

---

## GATE 3 FAILURES (May 30 launch day)

### P3A — Etsy listing will not publish
```
Click Publish → what happens?
    Returns error message → read it carefully → field-by-field checklist:
          Title: ≤140 chars?
          Tags: exactly 13, each ≤20 chars, no # @ & / characters?
          Primary image: ≥2000px on longest side?
          Price: >$0.00?
          Quantity: not zero?
          Digital PDF: attached with green checkmark?
          Shipping: set to Digital, no shipping?
          Category: selected?
          → Fix each issue found. Click Publish again.
    Listing stays in Draft despite no errors?
          Shop settings complete? (name, description, language)
          Payment method verified in Finances > Payment settings?
          status.etsy.com showing outage? → Wait 30 min.
    Account verification hold / identity verification required?
          INVOLVES USER. User must complete identity steps.
          WHILE WAITING → Gumroad fallback (15 min):
              gumroad.com → create account (wanka95@gmail.com) → create product per guide
              → upload guide PDF → copy product URLs → update Kit broadcast links before noon.
    Contact Etsy support via etsy.com/help AND run Gumroad fallback simultaneously.
    Do not wait for Etsy to respond before pivoting to Gumroad.
    → Full procedure: Playbook 3A
```

### C5 — CRITICAL: Emails sent but Etsy listing not live
```
THIS IS THE MOST DAMAGING SCENARIO.
Subscribers receive broken product links = worst possible first impression.

PREVENTION (do this at 10:05am BEFORE touching Kit broadcast):
    Open each Etsy listing URL in an incognito window.
    Confirm "Add to cart" is visible on each listing.
    ONLY THEN proceed to the 12:00pm broadcast send.

If broadcast already sent and Etsy is not live:
    Do NOT send a correction email immediately.
    First: how long until Etsy can be live?
          <30 min → fix Etsy fields now. Send brief correction email once live.
          30-60 min → fix Etsy. Once live: send correction email with correct URLs.
          >60 min (account hold, platform outage) → Gumroad fallback NOW (15 min).
                Send correction email with Gumroad URLs immediately after Gumroad is live.
    Correction email:
          Subject: "Quick update from Seedwarden — corrected links inside"
          Body: "The links are now live. Here are the correct product links: [URLs].
                Thank you for your patience."
          Keep it short, matter-of-fact, one brief acknowledgment.
    → Full procedure: Playbook 3A + Playbook 3B (broadcast timing)
```

### P3B — Kit broadcast failed at 12:00pm
```
Check broadcast status at 12:05pm.
    Status "Sending" or "Sent" → success. Check delivery stats at 12:30pm.
    Status "Scheduled" at 12:05 → timezone offset. Click "Send Now" to override.
    Status "Failed" → read failure reason:
          "Sender not verified" → Kit > Settings > Email > resend verification → 5 min fix.
          "List empty" → NOT an error. List builds from social traffic. Proceed.
          Other reason → duplicate the broadcast → fix identified issue → send duplicate.
    Two failed retries → Gmail fallback:
          Open Gmail at wanka95@gmail.com.
          Subject and body: copy from SEEDWARDEN_EMAIL_LAUNCH_SEQUENCE_GUIDE.md Launch Broadcast section.
          BCC: all subscriber email addresses (export CSV from Kit first).
          Send as close to 12:00pm as possible. 30-min delay is acceptable.
          Log: "Kit failed at [time]. Gmail fallback sent at [time]." → WORKLOG.md
    Escalate if: >50% of list affected by bounce/delivery failure → involve user.
    → Full procedure: Playbook 3B
```

### P3C — Social post failed or did not go live
```
FIRST: check the platform directly (not just Buffer).
Is the post visible on Instagram.com / TikTok.com / Pinterest.com?
    YES → Buffer reporting is delayed. Post succeeded. Done.
    NO → real failure. Which platform?

Instagram failed:
    Buffer > Settings > Channels > Instagram > Reconnect (auth expired). 2 min.
    After reconnecting → Buffer queue → Share Now.
    Reels post: upload directly via Instagram app if Buffer cannot auto-post Reels.

TikTok failed:
    Buffer free does NOT auto-post TikTok video. Buffer sends a push notification.
    Notification missed? → Upload video directly in TikTok app. This is normal flow.

Pinterest failed:
    No boards? → Pinterest > Create board ("Growing Guides") → retry Buffer post. 5 min.
    Auth expired? → Buffer > Settings > Channels > Pinterest > Reconnect.
    Wrong aspect ratio? → Use portrait image from projects/seedwarden/mockups/.

Buffer down or unresolvable by 2:00pm → manual post all platforms (5 min each):
    Instagram: image from mockups/ + caption from phase-2-social-content-calendar-60day.md Day 30
    TikTok: video file + caption under 200 chars
    Pinterest: image + description from content calendar, link to Kit landing page
    DO NOT delay the launch waiting for Buffer. Manual posting = identical result.
Escalate if: 2+ platforms failing simultaneously AND manual posting also failing → involve user.
    → Full procedure: Playbook 3C
```

### P3D — GA4 shows zero events or no tracking data
```
IMPORTANT: GA4 is NOT a launch requirement. It cannot be backfilled. Fix it post-launch.

First: go to GA4 > Reports > Realtime.
Open your Etsy listing in incognito. Wait 30 sec.
    Pageview event appears? → GA4 working. Standard reports lag 24-48 hrs. Check May 31.
    No event in Realtime:
          Etsy Shop Manager > Settings > Web analytics: is GA4 Measurement ID entered?
              NO → enter it now. Copy from GA4 > Admin > Property settings (starts with "G-").
                   Save. Wait 60 sec. Reload Etsy listing in incognito. Recheck Realtime.
              YES → compare ID character by character. One wrong character = no tracking.
                    Fix mismatch. Save. Retest.
          Still no events after ID fix? → Document in WORKLOG.md. Fix in 48 hrs post-launch.
All traffic showing as "Direct" in GA4?
    UTM parameters missing from Kit broadcast links and social bio links.
    Add UTMs going forward. Retroactive backfill not possible.
Etsy Shop Manager Stats also showing zero views for live listings?
    That is an Etsy listing visibility issue, not a GA4 issue.
    Open each listing URL in incognito → confirm "Add to cart" visible → if not, re-publish.
PRIORITY: GA4 failure does not block or delay the launch. Etsy Stats is the sales truth.
    → Full procedure: Playbook 3D
```

---

## ESCALATION DECISION GUIDE

```
ESCALATE TO USER IMMEDIATELY IF:
   Etsy account hold requires identity verification (user's personal info needed)
   Any cost decision >$50 is required to unblock a failure
   Both Etsy AND Kit are simultaneously failing AND Gumroad fallback is also failing
   A social media account is suspended at account level (not just a post error)
   GA4 AND Etsy Stats both show zero views for confirmed live listings

ESCALATE AFTER 60 MIN OF SELF-RESOLUTION IF:
   Full recovery path executed, failure persists
   Platform shows account-level error preventing all activity
   C5 scenario active: broadcast sent, Etsy not live, Gumroad taking >30 min

HOW TO ESCALATE:
   Write in WORKLOG.md: timestamp + playbook number + last step reached
   + exact error message + what decision or resource is needed.
```

---

## MINIMUM VIABLE LAUNCH

```
Etsy listings publicly accessible         = THE LAUNCH IS REAL
+ Kit broadcast sent to list              = EMAIL LAUNCH
+ 1 social post on any platform           = SOCIAL LAUNCH
+ GA4 tracking confirmed                  = ANALYTICS ACTIVE

If only Etsy listings go live and everything else fails:
the launch happened. Week 1 is for building reach on a working foundation.
```

---

*Prepared: 2026-05-19. Seedwarden Agent.
Full playbooks: SEEDWARDEN_LAUNCH_CONTINGENCIES.md (Parts 1-4, 16 playbooks)
Hour-by-hour sequence: MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md
Pre-launch 3-day checklist: SEEDWARDEN_MAY_27_29_PRELAUNCH_MASTER_CHECKLIST.md*
