---
title: "May 30 Launch Day Decision Tree — Quick Reference"
prepared: 2026-05-15
launch-date: 2026-05-30
status: print-ready
scope: One-page rapid diagnosis for all 8 failure modes. Print on May 30 morning.
references:
  - LAUNCH_CONTINGENCY_PLAYBOOKS.md (full step-by-step recovery for each failure)
  - MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md (hour-by-hour sequence)
---

# May 30 Launch Day Decision Tree

**Print this page on May 30 morning. Keep it next to your keyboard.**
When something goes wrong, find the failure mode below and follow the arrows.
Each "see Playbook" reference points to the full recovery in LAUNCH_CONTINGENCY_PLAYBOOKS.md.

---

## LAUNCH DAY SEQUENCE (reference times)

    8:00am   System checks and QA
    10:00am  Etsy listings publish
    12:00pm  Kit broadcast sends
    2:00pm   Instagram + TikTok posts go live
    3:30pm   Pinterest pins go live
    9:00pm   End-of-day log

---

## FAILURE MODE FLOWCHART

```
START HERE when something fails
         |
         v
    What failed?
         |
    +----|----+--------+--------+--------+
    |         |        |        |        |
  CANVA     KIT      ETSY   SOCIAL    GA4
    |         |        |        |        |
    v         v        v        v        v
  [F1]      [F2]     [F5]    [F7]     [F8]
  [F3]      [F3]
  [F4]      [F4]
            [F6]
```

---

## FAILURE MODES

### F1 — Canva: Cannot add 10 colors to Brand Kit

    Can you add any colors at all?
          |
    YES --+-- NO
    |              |
    v              v
How many         Canva may have a
can you add?     browser error.
    |            Hard-refresh browser,
    v            try incognito, try again.
Less than 10?         |
    |                 v
    v           Still blocked?
This is the          |
free plan limit      v
(confirmed:     See Playbook A1
3-color cap     full recovery section.
on free tier).  Options: upgrade to
    |           Pro ($15/mo) or use
    v           manual hex entry.
IMMEDIATE FIX (5 min):
Add only these 3 to Brand Kit:
  #143b28 (Deep Forest Green)
  #F5EDD6 (Warm Cream)
  #A0522D (Burnt Sienna)
Enter remaining 7 manually
per design. Keep hex list open
in a separate text file.

---

### F2 — Canva: Brand Kit upload failed / page error

    Is status.canva.com showing an outage?
          |
    YES --+-- NO
    |              |
    v              v
Wait 30-60 min.  Try hard-refresh,
Check back.      incognito browser,
                 different browser.
                      |
                 Still failing?
                      |
                      v
               See Playbook A2.
               Core principle:
               Brand Kit is a
               convenience tool.
               Work without it
               using manual hex
               entry from cheat sheet.
               Do NOT let this
               block launch.

---

### F3 — Canva or Kit: Design file or sequence disappeared

    Check "Recent designs" in Canva
    OR check Kit > Automations.
          |
    Found it? (different folder, filter issue)
          |
    YES --+-- NO
    |              |
    v              v
Move it to       For Canva: rebuild
correct place.   from scratch per
Continue.        CANVA_ZONE_CARD_DESIGN_GUIDE.md
                 For Kit: rebuild
                 sequence per
                 KIT_SETUP_NOTES.md Step 5.
                 Budget: 2-3 hours for
                 Zone 5 master rebuild.
                 See Playbook A3.

---

### F4 — Kit: Conditional zone routing blocked / upgrade prompt

    Does Kit show "upgrade to use this feature"
    for conditional automation steps?
          |
    YES --+-- NO
    |              |
    v              v
Free plan does   Something else
NOT support      is wrong. Check
conditionals.    automation trigger
This is expected.and tag names.
    |            See Playbook B1.
    v
CHOOSE ONE:
A) Single all-zones email (FREE, 10 min):
   Build 1 Email 1 with all 8 zone
   card links listed. No routing needed.
   Subscriber clicks their zone link.
   Recommended for launch.

B) Upgrade to Kit Creator ($33/mo):
   Unlocks full conditional logic.
   Implement full zone routing.
   Takes 1 extra hour to build.

C) Manual daily follow-up:
   Check Kit > Subscribers daily.
   Send correct zone card manually
   to each new subscriber.
   Scales only to ~30 subscribers.

See Playbook B2 for full decision guide.

---

### F5 — Etsy: Listing won't publish

    Click Publish. What happens?
          |
    Error message? ---YES---> Read the error.
          |
         NO
          |
          v
    Listing stays in Draft?
          |
    YES --+-- NO (published OK)
    |              |
    v              v
Check each field:  Done. Verify in
  Title: under     incognito browser.
    140 chars?
  Tags: 13 tags,
    each under
    20 chars?
  Image: 2000px
    minimum?
  Price: not $0?
  PDF attached?
  Shipping: set
    to Digital?
          |
   Fix field,
   click Publish.
          |
    Still failing?
          |
          v
   Is it an account
   verification hold?
          |
    YES --+-- NO
    |              |
    v              v
Gumroad fallback: Contact Etsy support.
  gumroad.com      Meanwhile run
  15-min setup.    Gumroad fallback.
  List guides at   See Playbook C1.
  same prices.
  Update Kit email
  links before noon.

---

### F6 — Kit: Broadcast send failed

    What is the broadcast status at 12:05pm?
          |
    +-----|------+----------+
    |            |          |
 Sending/     Scheduled   Failed
  Sent           |          |
    |            v          v
    v       Click "Send  Read failure
  Check      Now" button  reason in Kit.
  stats at       |          |
  12:30pm.  Delivered?   Common causes:
  Done.          |        - Sender address
                YES        not verified
                 |          (5-min fix)
                 v        - List is empty
               Done.       (not an error,
                           list builds
                           from social)
                                |
                           Still failed?
                                |
                                v
                         Gmail fallback:
                           BCC all known
                           subscriber emails.
                           Use exact subject
                           and body from
                           email-and-launch-plan.md
                           launch broadcast section.
                           See Playbook C2.

---

### F7 — Social: Post did not go live

    Check the platform directly (not just Buffer).
    Is the post visible?
          |
    YES --+-- NO
    |              |
    v              v
Done. Buffer's   What platform?
log is just           |
delayed.         +----|----+----------+
                 |         |          |
            Instagram   TikTok    Pinterest
                 |         |          |
                 v         v          v
             Reconnect   Upload    Create a board
             Instagram   video     in Pinterest
             in Buffer   directly  first, then
             (auth       via TikTok retry Buffer.
             expired?).  app (Buffer OR reconnect
             2 min fix.  cannot auto- Pinterest
                         post video   in Buffer.
             OR:         on free      2 min fix.
             Post manual.plan).
                         Post manual.
                              |
                     Manual posting:
                     image from mockups/
                     caption from
                     social-content-
                     calendar-60day.md
                     Day 30.
                     5 min per platform.
                     See Playbook C3.

---

### F8 — GA4: No tracking data appearing

    Check GA4 Realtime while visiting your
    own Etsy listing page in incognito.
    Do you see a pageview event?
          |
    YES --+-- NO
    |              |
    v              v
GA4 is working.  Check Etsy Shop Manager
Standard         > Settings > Web analytics.
reports lag      Is your GA4 Measurement
24-48 hours.     ID (G-XXXXXXXXXX) entered?
Check May 31.         |
                 YES --+-- NO
                 |              |
                 v              v
           ID entered but  Enter it now.
           not working.    Verify exact
           Check: does     match with
           the ID in Etsy  GA4 > Admin
           EXACTLY match   > Property
           GA4 > Admin?    Settings.
           One wrong       Save. Wait
           character = no  60 seconds.
           tracking.       Retest.
                 |
           Still nothing?
                 |
                 v
           Purchase events
           CANNOT be tracked
           on Etsy (hard limit).
           Etsy stats are your
           purchase source of
           truth, not GA4.
           GA4 = traffic only.
           See Playbook C4.
           Start fresh from today.
           No backfill possible.

---

## ESCALATE TO ORCHESTRATOR WHEN:

- A failure persists after 60 minutes of recovery work
- Any platform shows an account-level suspension (not just a posting error)
- A cost decision above $50 is needed to resolve the failure
- A Gate is entirely blocked with no workaround found

Log every escalation: time, playbook used, step that failed, what you need.

---

## MINIMUM VIABLE LAUNCH REMINDER

The Etsy listing is the only hard requirement.
Everything else adds reach to a working launch.

    Etsy listings live              = LAUNCH IS REAL
    + Kit broadcast sent            = EMAIL LAUNCH
    + 1 social post live            = SOCIAL LAUNCH
    + GA4 tracking confirmed        = ANALYTICS ACTIVE

If only Etsy listings go live today and nothing else works:
the launch happened. Week 1 is when reach is built.

---

*Prepared: 2026-05-15. Seedwarden Agent. Item 60.
Full recovery procedures: LAUNCH_CONTINGENCY_PLAYBOOKS.md
Hour-by-hour sequence: MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md*
