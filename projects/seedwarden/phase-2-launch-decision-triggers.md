---
title: "Phase 2 Launch Decision Triggers — 1-Page Reference"
date: 2026-05-07
status: print-ready
use: Open on May 29 (pre-launch), keep open on May 30 (launch day), reference through Week 2 (Jun 6)
references:
  - phase-2-launch-control-center.md (risk mitigation, Part 3)
  - may-30-launch-sequence.md (8am QA blocks)
  - phase-2-contingency-playbook.md (full recovery sequences)
  - phase-2-buyer-retention-lifecycle-strategy.md (Section 5 decision triggers, Section 6 contingencies)
  - phase-2-pre-launch-checklist.md (7-day validation)
---

# Phase 2 Launch Decision Triggers
## If X Happens, Do Y — Reference Sheet

**How to use**: Print this page or bookmark it. Read it top to bottom on May 29. On May 30, open it alongside may-30-launch-sequence.md. Each trigger is a single decision: if you see the condition described, take the action listed. No judgment required.

---

## PRE-LAUNCH TRIGGERS (May 21–29)

---

**If Buffer or Later shows "Reconnect" on any platform**
Do: Re-authorize the OAuth connection immediately.
Path: Buffer > Settings > Connected Accounts > click the platform with the error > follow the re-authorization steps (takes 2 minutes per platform). Do this same day — do not leave an expired OAuth token for launch day.
Why: OAuth tokens expire silently. A "Reconnect" warning means scheduled posts will fail to publish automatically.

---

**If the Kit landing page URL returns a 404 or is inaccessible**
Do: Check Kit > Landing Pages > confirm the page is "Published" (not "Draft"). Click "Publish" if it is in draft.
If Kit account access is blocked: activate Google Form fallback (see phase-2-contingency-playbook.md Scenario 3). Collect sign-ups via Google Form until Kit resolves.
Why: The landing page is the entry point for the entire email list. It must be live before any social bio traffic arrives.

---

**If SEEDWARDEN15 coupon shows "Expired" or does not appear in Etsy > Marketing > Coupons**
Do: Recreate it immediately.
Path: Etsy Shop Manager > Marketing > Sales and Coupons > Create a coupon > 15% off > applies to all listings > no minimum order > set expiry to June 30, 2026.
This takes 3 minutes. Do it on the same day you notice the issue.
Why: The coupon code appears in the Kit broadcast (May 30 12pm) and in Campaign 3 Email 3.1. If it is invalid when buyers try to apply it, issue manual Etsy credits of $3–$5 to affected buyers on Day 1.

---

**If only 28 of 30 lifestyle photos are ready by May 20**
Do: Use stock-sourced or Cluster D+E composite images for the missing 2 listings. These are Canva composites already available in /marketing/lifestyle-photos/stock-raw/. Upload to Etsy slots 4–5 for the missing listings.
Do not delay the full launch over 2 photos. The 21-listing 5-image status target (phase-2-launch-control-center.md Part 4) has a minimum acceptable threshold of 18 of 21.
Replace with lifestyle photos in Week 2 after the shoot completes.

---

**If all 8 zone card PDFs are not uploaded to Google Drive with working download URLs by May 22**
Do: Prioritize the 4 highest-population zones first: Zone 5, Zone 6, Zone 7, Zone 8.
Send "Zone [3/4/9/10] Quick-Start Card — coming Week 2" placeholder text in Email 1 for those zones, with a follow-up email when the missing cards go live.
Hard deadline: all 8 cards must be live and tested by May 28.

---

**If Kit DNS (SPF/DKIM) shows "Not verified" on May 22 or later**
Do: Check the DNS records again — propagation can take up to 72 hours from when the records were added.
If records are correctly formatted and still not propagating after 72 hours: contact your domain registrar support.
Do not launch Kit automation until SPF and DKIM are green. Emails sent from an unauthenticated domain will land in spam, killing open rates on the welcome sequence.

---

## LAUNCH DAY TRIGGERS (May 30)

---

**If any Etsy listing shows "Draft" instead of "Active" at 8am**
Do: Click "Publish" on the draft listing. Takes 30 seconds.
Check all 21 listings are Active in Etsy Shop Manager > Listings > filter by "Active" vs. "Draft."
This must be resolved before 10am (Etsy launch hour).

---

**If any Etsy listing shows "Under Review"**
Do: Do not recreate the listing. Email Etsy support immediately via Help > Contact Etsy. The review typically clears in 24–48 hours.
Launch proceeds with the remaining active listings. Do not delay the broadcast or social posts over one listing under review.

---

**If Kit broadcast is in "Draft" status at 8am instead of "Scheduled"**
Do: Open the broadcast > click Schedule > enter today's date at 12:00pm. Confirm it reads "Scheduled."
If the broadcast copy is missing or was deleted: paste the full body from phase-2-kit-broadcast-copy.md. Takes 10 minutes.

---

**If Kit automation shows "Paused" at 8am**
Do: Kit > Automations > find "Welcome — Phase 2 Buyers" > click Resume. Takes 30 seconds.

---

**If SEEDWARDEN15 coupon code does not apply to orders on launch day**
Do: Verify the coupon is "Active" in Etsy Shop Manager > Marketing > Coupons.
If it is active but buyers report it is not working: check that the coupon is not restricted to specific listings. It should apply to all listings with no minimum.
If 1–3 buyers were affected before the issue was caught: issue manual store credits via Etsy > Conversations > send a custom coupon code directly to the affected buyers for $4 store credit (equivalent to 15% off a $28 order).

---

**If a Google Drive zone card URL returns "Request Access" instead of downloading**
Do: Open Google Drive > navigate to the zone card file > Share > change from "Restricted" to "Anyone with the link can view." Copy the new sharing URL and re-generate the download URL in the format: `https://drive.google.com/uc?export=download&id=[FILE-ID]`.
Update the URL in the corresponding Kit Email 1 zone variant before any more subscribers receive it.
This is the most common failure mode on launch day — Drive permissions reset silently after a certain period.

---

**If the Kit broadcast open rate at 6pm is below 20%**
Do: Check Kit > Broadcasts > delivery stats. Is the deliverability rate above 90%? If deliverability is low (high bounces), the issue is list hygiene — not copy. Flag for Monday morning review.
If deliverability is fine but open rate is below 20%: the subject line is underperforming. Note it and run an A/B test on the next broadcast. Do not resend the launch broadcast — resending to an unopened segment on launch day will feel spammy to those who already opened it.

---

**If no Etsy orders arrive on launch day**
Do: Do not panic. Organic-first strategy; Phase 1 launched without a Kit broadcast and still reached 47 orders. Check that listings are Active, lifestyle images are showing in Etsy search results (search your own store from incognito), and SEEDWARDEN15 is active.
The launch broadcast drives awareness — it does not guarantee same-day sales. The benchmark is 2+ orders in the first 7 days, not 1 order on Day 1.

---

**If social posts fail to publish at their scheduled times (Instagram 2pm, TikTok 2pm, Pinterest 3:30pm)**
Do: Log into each platform directly. Copy the caption from phase-2-social-content-calendar-60day.md Day 30. Upload the corresponding image from /marketing/lifestyle-photos/etsy-ready/. Post manually. 15 minutes across all 3 platforms.
Then: in Buffer/Later, check the connection status and re-authorize any expired OAuth tokens.

---

## POST-LAUNCH TRIGGERS (May 31 – June 15)

---

**If Campaign 1 open rate drops below 30% in the first week**
Do: Start an A/B test on Email 1A subject lines within 48 hours. Send 10% per variant to new subscribers. Select the winner at 48-hour open rate.
Also check Kit > Broadcasts > deliverability on Email 1A — if bounce rate is above 3%, the issue is list quality, not subject line. Review list for invalid addresses.

---

**If unsubscribe rate on any Campaign 2 email exceeds 2%**
Do: Pause Campaign 2 sends for the current week's buyer batch immediately. Reduce to 1 email per week (skip the email that caused the spike; keep the sequence going with the next email at 1-week intervals). Audit the email that caused the spike — if it is not zone-specific, add zone-specific content. If it reads as promotional rather than educational, remove any product links from that email for the next 2 weeks.

---

**If the Kit automation fails to fire Campaign 1 Email 1 within 24 hours of a confirmed purchase**
Do: Switch to Option B (manual tag assignment) immediately.
Path: export Etsy orders CSV for the affected period > open Kit > Subscribers > search each buyer email > manually apply `purchased` tag. This fires the Campaign 1 sequence from that point forward.
Also: investigate the Zapier connection. Kit > Settings > Integrations > check Zapier connection status. If the Zap is failing, retest it with a dummy order before trusting it again.
Estimated time for manual fallback at Phase 2 volumes: 30 minutes per week.

---

**If the Squarespace CMS is inaccessible or returns errors (any time before June 6)**
Do: Use the Kit landing page builder as the primary landing page. Kit's landing page is fully functional for email capture and the zone quiz.
For the Bundles and Endangered Species pages: update the relevant Etsy listing descriptions to include the bundle pricing information and conservation story directly in the listing. Etsy descriptions support up to 2,000 characters.

---

**If a buyer replies to a Campaign 1 or 2 email with a question**
Do: Reply personally within 24 hours from your sending email (Kit Conversations or Gmail). Apply the `engaged-buyer` tag in Kit to that subscriber manually.
This is not a crisis — it is a high-value engagement signal. An engaged buyer who received a personal reply has a 3–5x higher repeat purchase rate than one who did not interact. Prioritize it.

---

**If Kit subscriber count is below 20 by June 6 (Week 1 review)**
Do: Review the landing page CTA in all three social bios — is the link working? Is the landing page form visible above the fold on mobile?
Test the sign-up flow yourself from incognito on a phone. If the form requires scrolling to find, move the email input field above the fold.
Consider posting one dedicated "free zone card" Reel or TikTok video in Week 2 specifically about the Quick-Start Card, with the landing page link in bio.

---

**If Etsy store views over the first 7 days are below 100**
Do: Check Etsy SEO on the top 3 listings by traffic. Confirm the title starts with the highest-value search term (not "Seedwarden" — buyers don't know the brand yet). Confirm all 13 tag slots are filled with specific long-tail terms. Update listing tags within the same week.
Do not run paid ads yet — Gate A requires 2.5% conversion rate on top listings first.

---

## WEEKLY THRESHOLDS — PERMANENT REFERENCE (Weeks 1–4)

| Metric | Source | Threshold | Action |
|---|---|---|---|
| Campaign 1 open rate | Kit > Sequences > Activity | Below 30% for 2 weeks | A/B test subject lines within 48 hours |
| Unsubscribe rate | Kit > Sequences > any email | Above 3% on any single email | Pause Campaign 2 within 24 hours; reduce to 1x/week |
| Bundle attach rate | Etsy orders + UTM | Below 1% after 30 Campaign 3 recipients | Redesign Landing Page 2: reduce to 3 bundles, add testimonials |
| Campaign 4 re-open rate | Kit > Sequences > Email 4.1 | Below 15% | Replace subject line with universal curiosity hook |
| VIP engagement retention | Kit > Subscribers > vip tag | Below 40% in 30-day window | Audit content exclusivity within 3 days |
| Bounce rate (any broadcast) | Kit > Broadcasts > Stats | Above 3% | Audit list for invalid addresses; Kit flags these automatically |

---

*Decision trigger reference status: complete. All thresholds are drawn from phase-2-buyer-retention-lifecycle-strategy.md Section 5, phase-2-launch-control-center.md Part 3, and may-30-launch-sequence.md. Every trigger names an exact action — "monitor" is not used anywhere in this document.*
