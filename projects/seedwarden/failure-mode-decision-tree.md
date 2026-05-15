---
title: "Seedwarden Launch Day Failure-Mode Decision Tree — Quick Reference"
prepared: 2026-05-15
launch-date: 2026-05-30
status: print-ready
scope: >
  One-page rapid diagnosis for all 12 failure modes across Gate 2 (Canva),
  Gate 3 (Kit), and May 30 launch day. Print or open on May 30 morning.
references:
  - SEEDWARDEN_LAUNCH_CONTINGENCIES.md (full 12-playbook recovery guide)
  - MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md (hour-by-hour sequence)
  - TRACK_B_USER_GATES.md (gate specifications)
---

# Seedwarden Launch Day Failure-Mode Decision Tree

Print this page on May 30 morning. Keep it next to your keyboard.
When something goes wrong, scan the failure modes below, find yours,
and follow the arrows. Each outcome points to the full recovery in
SEEDWARDEN_LAUNCH_CONTINGENCIES.md.

---

## LAUNCH DAY REFERENCE TIMES

    8:00am    System checks — verify Kit active, Etsy listings draft-ready, social logins
    10:00am   Etsy listings PUBLISH (verify live in incognito BEFORE 12:00pm)
    10:05am   VERIFY: open each listing URL in incognito — confirm "Add to cart" visible
    12:00pm   Kit broadcast SEND (only after Etsy listings confirmed live)
    2:00pm    Instagram + TikTok posts go live
    3:30pm    Pinterest pins go live
    9:00pm    End-of-day log (Kit signups, Instagram impressions, TikTok views)

---

## FAILURE MODE FLOWCHART

```
SOMETHING FAILED
       |
       v
  WHICH SYSTEM?
       |
  +----|--------+-----------+-----------+-----------+
  |             |           |           |           |
CANVA          KIT        ETSY       SOCIAL       GA4
(Gate 2)    (Gate 3)   (launch)    (launch)    (launch)
  |             |           |           |           |
  v             v           v           v           v
[F1][F2]    [F4][F5]      [F8]        [F10]       [F11]
[F3][F4 *]  [F6][F7]      [F9]
            [B5 *]

  * F4 applies to both Canva (free plan limits) and Kit (free plan limits)
```

---

## GATE 2 FAILURES — CANVA (May 19-24)

### F1 — Cannot add more than 3 colors to Brand Kit

    Attempt to add color 4+. Does Canva show an upgrade prompt?
           |
     YES --+-- NO (spinner / network error)
     |               |
     v               v
  This is the    Hard-refresh browser (Ctrl/Cmd+Shift+R).
  free-plan      Try incognito. Try again.
  3-color cap.        |
     |           Still blocked after incognito?
     v                |
  IMMEDIATE FIX       v
  (5 min):       That is the plan limit too.
  Add these 3    See Playbook A1.
  to Brand Kit:
  #143b28 (Forest Green)
  #F5EDD6 (Warm Cream)
  #A0522D (Burnt Sienna)
  Keep hex cheat sheet open.
  Enter remaining 7 manually per design session.
  OR: upgrade Canva Pro $15/mo for unlimited colors.
  -> See Playbook A1 for decision rule.

---

### F2 — Logo upload failed / Canva page error / Brand Kit won't save

    Check status.canva.com — is there an active incident?
           |
     YES --+-- NO
     |               |
     v               v
  Wait 30-60 min.  Is file PNG format and under 25 MB?
  Retry.                |
                  YES --+-- NO
                  |               |
                  v               v
            Try hard-refresh,  Convert to PNG.
            incognito browser, Resize to 1000px
            different browser. wide if large.
                  |            Re-upload.
            Still failing?
                  |
                  v
            Brand Kit is a convenience tool.
            Work without it — use manual hex entry.
            Do NOT let this block launch.
  -> See Playbook A2.

---

### F3 — Design file or Brand Kit disappeared

    Go to Canva > Home > Recent designs.
    Is the file listed?
           |
     YES --+-- NO
     |               |
     v               v
  Open it.       Check Canva > Projects > All projects.
  Continue.           |
                 Found it?
                  YES --+-- NO
                  |               |
                  v               v
            Open it.         Check Canva Trash
            Continue.        (canva.com/trash).
                                  |
                             In Trash?
                              YES --+-- NO
                              |               |
                              v               v
                          Restore it.    Rebuild from
                          Continue.      CANVA_ZONE_CARD_DESIGN_GUIDE.md
                                         Budget: 2-3 hrs Zone 5 master.
                                         35-45 min per zone after that.
  -> See Playbook A3.

---

### F4 — Missing images or placeholder text visible in PDF export

    Open exported PDF in a PDF viewer (not Canva).
    Is placeholder text [ETSY-ZONE-CALENDAR-LINK] or [KIT-LANDING-PAGE] visible?
           |
     YES --+-- NO (other issue)
     |               |
     v               v
  DO NOT              Are there gray/blank boxes where images should be?
  distribute.              |
  Return to Canva.    YES --+-- NO
  Replace ALL         |               |
  bracketed text      v               v
  with live URLs.  Re-open design.  Check Canva > Layers.
  Both URLs needed  Click each image  Ensure all elements
  before export:    to trigger load.  are present. Try
  Etsy listing URL  Wait full-res.    PDF Print export.
  + Kit landing URL. Re-export.       Or export as PNG,
  -> See Playbook A4.                 convert to PDF.
  -> See Playbook A4.

---

## GATE 3 FAILURES — KIT (May 27-28)

### F5 — Email routing broken / wrong zone card delivered

    Run sign-up test. Did Email 1 arrive within 5 minutes?
           |
     YES --+-- NO
     |               |
     v               v
  Did it deliver   Check spam/junk folder first.
  the CORRECT          |
  zone card?      Found in spam?
     |             YES --+-- NO
     |             |               |
     v             v               v
  YES: done.   DKIM issue.     In Kit > Automations:
  NO: routing  Long-term fix:  Is sequence "Active"?
  is wrong.    custom domain.   YES --+-- NO
  Check Kit >  OK for launch.   |               |
  Automations. Continue.        v               v
  Match tag              Did subscriber   Click Activate.
  names exactly.         appear in Kit >  Retest.
  zone-5 not Zone-5.     Subscribers?
  -> See Playbook B1.     NO: form issue,
                          not sequence.
                          Fix landing page
                          form connection.

---

### F6 — Conditional logic blocked / Kit shows upgrade prompt for automation

    Does Kit show "upgrade to use this feature" on any conditional step?
           |
     YES --+-- NO
     |               |
     v               v
  Free plan does   Something else is wrong.
  not support      Check automation trigger
  conditionals.    and tag name spelling.
  This is expected.-> See Playbook B1.
     |
     v
  CHOOSE ONE NOW (do not wait):
  A) ALL-ZONES EMAIL (FREE, 10 min) — RECOMMENDED FOR LAUNCH
     Build 1 Email 1 with all 8 zone card links listed.
     No routing or conditionals needed.
     Subscriber clicks their own zone link.
     Zone links from zone card Google Drive folder.

  B) UPGRADE Kit Creator ($33/mo)
     Unlocks full conditional logic.
     Build 8-variant Email 1 routing.
     Budget 1 extra hour post-upgrade.

  C) MANUAL DAILY SEGMENTATION (free, labor)
     Check subscribers daily.
     Send correct zone card manually.
     Scales to ~30 subscribers only.
  -> See Playbook B2.

---

### F7 — Subscriber list shows zero or count dropped

    In Kit > Subscribers, is the filter set to "Active only"?
           |
     YES --+-- NO
     |               |
     v               v
  Change filter    Are you viewing a Segment?
  to "All          Clear segment filter.
  subscribers."    Recheck count.
  Does count            |
  restore?         Count still 0?
     |                  |
  YES: no data          v
  lost. Proceed.   Do you have a CSV backup?
                    YES --+-- NO
                    |               |
                    v               v
              Re-import CSV.  Contact Kit support:
              Kit > Subscribers support@kit.com
              > Import.       Request data restore.
              Continue.       Kit retains data 30 days.
  -> See Playbook B3.

---

### F8 — Kit sequence failed / account suspended on launch morning

    What does Kit show at 8:00am check?
           |
  +--------|-------+-------------+
  |                |             |
  Sequence       Account       Everything
  shows error    suspended     looks fine
  state              |             |
      |               v             v
      v          Contact Kit    Run sign-up
  Click into     support NOW:   test to confirm
  sequence.      support@kit.com active state.
  Find error     Describe new   Continue with
  message.       account,       launch plan.
  Fix field      opt-in list,
  or trigger.    educational
  Resume.        content.
  Then:          2-4 hr resolve.
  -> Gmail fallback during wait:
     Open Gmail > wanka95@gmail.com
     BCC all known subscriber emails
     Copy subject + body from
     marketing/email-and-launch-plan.md
     Launch Broadcast section
     Send at/before 12:00pm
  -> See Playbook B4.

---

## LAUNCH DAY FAILURES — MAY 30

### F9 — Etsy listing won't publish

    Click Publish. What happens?
           |
  Error? --YES--> Read the error message.
           |
          NO
           |
          v
    Listing stays in Draft?
           |
     YES --+-- NO (published)
     |               |
     v               v
  Check fields:   Open in incognito.
    Title ≤140?   Confirm live.
    13 tags,      Done.
    each ≤20 chars?
    Image ≥2000px?
    Price > $0?
    PDF attached?
    Shipping = Digital?
    Category set?
           |
    Fix field,
    click Publish.
           |
    Still failing?
           |
           v
    Account verification hold?
           |
     YES --+-- NO
     |               |
     v               v
  Gumroad fallback:  Check status.etsy.com.
  15 min to set up.  Outage? Wait 30 min.
  List guides at     Still failing?
  same prices.       Contact Etsy support
  Update Kit email   AND run Gumroad
  links before noon. fallback in parallel.
  -> See Playbook C1.

---

### F10 — CRITICAL: Emails sent but Etsy listing not live yet

    THIS IS THE MOST DAMAGING SCENARIO.
    Subscribers click broken product links = worst first impression.

    PREVENTION (do this at 10:05am before touching Kit):
    Open each Etsy listing URL in incognito.
    Confirm "Add to cart" visible.
    ONLY THEN send the 12:00pm broadcast.

    If broadcast already sent and Etsy is not live:
           |
           v
    How long until Etsy will be live?
           |
    <30 min --+-- 30-60 min --+-- >60 min
    |               |               |
    v               v               v
  Wait, then    Fix Etsy fields. Run Gumroad
  send brief    Get listings     fallback (15 min).
  correction    live. Send       Send correction
  email once    correction       email with Gumroad
  live.         email after.     links immediately.
    |
    Correction email template:
    Subject: "Quick update — links now live"
    Body: "The links in our earlier email are now live.
    Here are the corrected links: [URLs].
    Thank you for your patience."
  -> See Playbook C5.

---

### F11 — Kit broadcast failed (12:00pm)

    Check broadcast status at 12:05pm.
           |
  +--------|------+-----------+
  |               |           |
  Sending/     Scheduled   Failed
  Sent           |           |
    |             v           v
    v         Click        Read failure
  Check       "Send Now"   reason in Kit.
  stats at    button.           |
  12:30pm.        |        "Sender not
  Done.       Sent?        verified"?
              YES: done.   -> Kit > Settings >
                           Email > re-verify.
                           "List empty"?
                           -> Not an error.
                           List builds from
                           social traffic.
                           Other failure?
                           -> Retry once.
                           Still failed?
                           -> Gmail fallback:
                              BCC subscribers,
                              use email-and-launch-
                              plan.md copy.
  -> See Playbook C2.

---

### F12 — Social post failed / did not go live

    Check the platform directly (not just Buffer).
    Is the post visible there?
           |
     YES --+-- NO
     |               |
     v               v
  Done.          What platform?
  Buffer log          |
  is delayed.    +----|------+----------+
                 |           |          |
            Instagram     TikTok    Pinterest
                 |           |          |
                 v           v          v
           Reconnect    Upload video  Create a
           Instagram    directly in   board first
           in Buffer    TikTok app    in Pinterest.
           (auth        (Buffer can't Then retry
           expired?).   auto-post     Buffer.
           2 min.       video free).  OR reconnect
                                     Pinterest in
                                     Buffer.
                 |
    If Buffer cannot be fixed by 2:00pm:
    Post manually (5 min/platform):
      Instagram: image from mockups/ + caption from
                 phase-2-social-content-calendar-60day.md Day 30
      TikTok:    video file + shortened caption (<200 chars)
      Pinterest: image + description from content calendar
    -> See Playbook C3.

---

### F13 — GA4 not showing data

    Go to GA4 > Reports > Realtime.
    Visit your own Etsy listing in incognito.
    Pageview event appears within 30 seconds?
           |
     YES --+-- NO
     |               |
     v               v
  GA4 working.    Is GA4 Measurement ID
  Standard        in Etsy Shop Manager?
  reports lag     -> Settings > Web analytics
  24-48 hrs.           |
  Check May 31.   YES --+-- NO
                  |               |
                  v               v
            Does ID in Etsy  Enter it now.
            EXACTLY match    Copy from GA4 >
            GA4 > Admin?     Admin > Property.
            One wrong char   Save. Wait 60s.
            = no tracking.   Retest.
                  |
            Still nothing?
                  |
                  v
            IMPORTANT:
            Etsy purchase events
            CANNOT be tracked in GA4.
            GA4 = listing page views only.
            Etsy Stats = purchase truth.
            GA4 tracking is NOT a
            launch-blocking requirement.
            Fix in first 48 hrs post-launch.
  -> See Playbook C4.

---

## ESCALATE TO ORCHESTRATOR WHEN:

- A failure persists after 60 minutes of recovery work
- Any platform shows account-level suspension (not just a posting error)
- A cost decision above $50 is required to proceed
- Both Etsy and Kit are simultaneously failing (Playbook C5 active)

Log every escalation: time, playbook executed, step that failed, what you need.

---

## MINIMUM VIABLE LAUNCH

The Etsy listing is the only hard requirement.
Everything else adds reach to a working launch.

    Etsy listings live              = LAUNCH IS REAL
    + Kit broadcast sent            = EMAIL LAUNCH
    + 1 social post live            = SOCIAL LAUNCH
    + GA4 tracking confirmed        = ANALYTICS ACTIVE

If only Etsy listings go live and nothing else works:
the launch happened. Week 1 is for building reach.

---

*Prepared: 2026-05-15. Seedwarden Agent. Exploration Queue Item 3.
Full recovery procedures: SEEDWARDEN_LAUNCH_CONTINGENCIES.md (12 playbooks)
Hour-by-hour sequence: MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md*
