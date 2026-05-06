---
title: "Phase 2 Contingency Paths"
date: 2026-05-06
status: production-ready
references:
  - phase-2-execution-timeline.md
  - phase-2-day-by-day-execution.md
  - tool-integration-map.md
---

# Phase 2 Contingency Paths
## Risk Scenarios, Recovery Sequences, and Fallback Protocols

**Purpose**: Pre-decided responses to the five most likely Phase 2 disruptions. Having these decisions made before a problem occurs means disruption doesn't cascade into paralysis. Each scenario answers three questions: (1) What exactly happened, (2) What is the revised sequence, (3) What has already been done that can stay staged vs. what must be re-done.

**How to use this document**: When a disruption occurs, find the matching scenario, follow the revised sequence, and update phase-2-day-by-day-execution.md with the new dates. Log the disruption in WORKLOG.md with the scenario name and date.

---

## Scenario 1: Phase 1 Slips to June 6 (Launch Delay 7 Days)

**Trigger**: Phase 1 Etsy store launch is delayed from late May to June 6, 2026, because tag corrections, listing reviews, or Etsy account issues push the approval past the Phase 2 window.

**Why this matters for Phase 2**: Phase 2 depends on Phase 1 in two ways. First, the Etsy store URL must be live to include in zone card footers and Kit email links. Second, lifestyle images are uploaded to existing Phase 1 listings — if those listings don't exist, there is no place to upload to.

**Revised timeline**:

| Original Date | Original Milestone | Revised Date | Notes |
|---|---|---|---|
| May 30 | Phase 2 launch | June 6 | Direct 7-day slip |
| May 29 | Etsy lifestyle image upload | June 5 | One day pre-launch |
| May 28 | Zone card URL replacement | June 4 | URLs confirmed after Phase 1 goes live |
| May 27 | Zone card QA | May 27 | No change — QA can run against placeholder URLs |
| May 25 | Kit automation live | May 25 | No change — automation can run in "draft" until Etsy URLs are confirmed |

**What stays staged (no reset required)**:
- All Canva zone card designs. Continue building on the original May 15–27 schedule. Use "[ETSY-URL]" placeholder in zone card footers. Replace with live Etsy URL on June 4.
- Kit account setup, tags, landing page, and welcome sequence. All can be built and tested against placeholder URLs. The landing page URL (Kit's own URL) is independent of Etsy.
- Google Drive zone card PDF uploads. Upload PDFs and record Google Drive URLs on the original May 28 schedule.
- Social media post drafts. Written content and images can be built and loaded into Buffer/Later. Change scheduled send dates from May 30 to June 6.

**What must be reset or held**:
- Zone card footer URL replacement: hold until June 4 (one day after Phase 1 goes live).
- Kit Email 3 and 4 Etsy product links: hold the UTM-tagged Etsy URLs until Phase 1 listing IDs are confirmed. You cannot build a correct Etsy listing URL until the listing exists.
- Kit broadcast staging: move the scheduled date from May 30 12pm to June 6 12pm. In Kit: Broadcasts > the staged broadcast > Edit > change scheduled send time.
- Buffer/Later social posts: reschedule from May 30 to June 6.
- Etsy lifestyle image upload: move from May 29 to June 5.

**Communication step**: If you have any subscribers already on the welcome sequence (from pre-Phase-1 social bio links), no communication is needed. They are receiving the welcome sequence on its existing schedule. The launch broadcast is the only thing that changes dates.

**Revenue impact**: Zero. Phase 2 revenue depends on the launch broadcast going to a subscriber list. The subscriber list will be marginally smaller on June 6 vs. May 30 (7 fewer days of organic sign-ups), but at launch-window list sizes (50–200 subscribers), the difference is single digits.

**Decision rule**: If Phase 1 is confirmed delayed by May 20, immediately update Buffer/Later, Kit broadcast, and calendar blocks to the June 6 sequence. Do not wait — rescheduling is a 10-minute task that eliminates launch-day confusion.

---

## Scenario 2: Photo Shoot Pushed to May 20

**Trigger**: The May 10–11 photo shoot is unavailable. The next workable window is May 17–18 or May 20–21.

**What is blocked by this delay**:
- Lifestyle image compositing in Canva (requires physical photos).
- Social media posts that use lifestyle imagery.
- Etsy slot 4 and slot 5 image uploads (the images don't exist yet).

**What is NOT blocked by this delay (proceed as planned)**:
- Canva zone card production: completely independent of photography. Build Zones 5 and 6 on May 15–17 as scheduled. The zone cards contain no photography.
- Kit account setup: completely independent. Build the full account, all tags, landing page, and all 5 emails on May 15–24 as scheduled. The welcome sequence delivers zone card PDFs, not photos.
- SEEDWARDEN15 Etsy coupon creation: independent. Create on May 20 as scheduled.
- Email testing and automation publishing: independent. The automation can go live on May 25 regardless of photography status.

**Revised photo track (if shoot moved to May 20–21)**:

| Task | Original Date | Revised Date |
|---|---|---|
| Photo shoot — Day 1 | May 10 | May 20 |
| Photo shoot — Day 2 | May 11 | May 21 |
| Image culling | May 11–12 | May 21–22 |
| Editing and export | May 12–13 | May 22–23 |
| Canva compositing | May 25–26 | May 26–27 |
| Etsy upload | May 29 | May 29 (unchanged — 2 days post-export) |

**This scenario produces zero launch-day change**: if the shoot is on May 20–21 and exports are ready May 22–23, Canva compositing completes May 26–27, and Etsy upload happens May 29 — which is the same pre-launch date as the original plan. The launch on May 30 is unaffected.

**The only difference**: Canva zone cards are built before photography arrives (May 15–19), which is actually the recommended build order anyway (zone cards are independent of photos).

**If the shoot slips further — to May 24 or later**:
- Run the math: export available May 26, Canva compositing May 27–28, Etsy upload May 29. This is still achievable but is a one-day sprint with no buffer.
- If the shoot slips to May 27 or later: launch with the first 6 stock-composited images (Clusters D and E, which use stock photos from Phase 1) in slots 4 and 5. The 15 physical-photo products launch without new lifestyle images — their existing slots 1–3 are still present and functional. Add lifestyle images as an update post-launch when photos are available.
- This "partial library launch" is documented in Scenario 3 below.

---

## Scenario 3: Photo Quality Issue — Reshoot Required

**Trigger**: After culling and reviewing, one or more clusters do not yield usable images. Causes include: out-of-focus shots across an entire session, severe color cast from problematic window light, or props significantly mismatched with the product type.

**Diagnosis before deciding to reshoot**:
Do not call a reshoot before running post-processing. Lightroom's Upright tool corrects significant perspective issues. White Balance correction can fix 80% of color cast problems. Sharpening can recover mild soft-focus if the product is still readable at 50% zoom. Give editing a genuine attempt before scheduling a reshoot.

If after editing you have fewer than 1 usable select per product for a given cluster, schedule the reshoot.

**One-day backup shoot plan**:
- Required window: any day with 3+ hours of window light in the morning. A Tuesday or Wednesday evening is not adequate for Cluster A (insufficient light duration). A weekend morning is required for Cluster A. Cluster C (kitchen) can be shot any time.
- Identify the backup shoot date before May 14. Candidates: May 14 (evening, Cluster C only), May 17 (Sunday morning, full backup).
- Keep all props staged and not disassembled after the primary shoot. If a reshoot is possible, having props ready eliminates re-setup time.
- On the reshoot day: focus only on the affected cluster. Use the same window, same light conditions. Do not adjust the setup from what produced the original shots — you want consistency between the new selects and any original selects you are keeping.

**Expedited Canva timeline (one-cluster reshoot)**:
If Cluster A (8 products) must be reshot on May 17, edited and exported by May 18:
- Canva compositing for Cluster A: May 19–20 (2 days, ~4 hours total).
- Clusters B and C were not reshot — their compositing runs on the original schedule.
- Etsy upload: May 29, unchanged.
- No launch-day impact.

**Launch-day override — partial library launch**:
If the photo quality issue affects more than one cluster and a full reshoot cannot be completed before May 28:

Decision protocol:
- Identify which products have confirmed usable lifestyle images.
- Launch May 30 with only those products' lifestyle images uploaded to Etsy.
- For products without lifestyle images: their existing slots 1–3 remain visible. Etsy listings function and sell without slots 4–5. They are just less optimized.
- Add remaining zone lifestyle images post-launch as a Week 1 update (June 1–7).
- Send a single post-launch broadcast: "New images added to the full guide library." This is not a second launch — it is a maintenance update framed as an enhancement.

**Priority order for partial launch** (if only some lifestyle images are available):
1. Seed Saving Field Manual — highest search volume, most valuable slot 4 optimization
2. Zone-by-Zone Seed Starting Calendar — high seasonal relevance in May
3. Harvest Preservation Field Manual — highest existing conversion rate
4. Remaining Cluster A products
5. Cluster B (Urban/Container) products
6. Cluster C (Preservation) products

If only Clusters D and E (stock composites) are available at launch: this is still a net improvement over current state (slots 1–3 only). Launch with what you have.

---

## Scenario 4: Tool Failure

### Scenario 4a: Kit Account Locked or Inaccessible

**Trigger**: Kit account is suspended, locked due to billing error, or inaccessible due to login issues.

**Immediate steps**:
1. Check Kit's status page: status.kit.co. If there is a platform-wide outage, wait — this is not an account-specific issue.
2. If account-specific: attempt password reset via wanka95@gmail.com. Check spam folder for the reset email.
3. If account suspended: Kit sends an email with the suspension reason. Most suspensions are due to: importing an email list that did not consent to Kit specifically (GDPR), or a complaint rate above 0.1%. If the suspension reason is legitimate, address it before reinstatement. If it is an error, use Kit's support chat.

**Fallback email platform — Substack**:
If Kit is inaccessible for more than 48 hours before the May 30 launch:

- Create a Substack account at substack.com (free, no payment required to send emails).
- Substack has no automation sequences — only broadcast newsletters. This means the zone card delivery automation cannot be replicated exactly. Workaround: create a single Substack sign-up page with zone selection. Use a Substack "welcome note" (Settings > Welcome Note > Email) to deliver a single email pointing to a page that lists all 8 zone card download links grouped by zone number.
- This is not ideal — subscribers self-select their zone from a list rather than receiving automatic zone-specific delivery. But it is functional for launch.
- Zone card PDFs are already hosted on Google Drive — the links work regardless of the email platform.
- Migration back to Kit: when the Kit issue is resolved, export the Substack subscriber list (Settings > Subscribers > Export) and import into Kit. Tag all imported subscribers with "substack-import" and enroll them in the welcome sequence from Email 2 (skip Email 1, as they have already received a zone card).

**Fallback email platform — Gmail (manual) for lists under 50 subscribers**:
If the subscriber list is small at time of failure (under 50 people), individual Gmail sends are viable as a bridge. Send the launch broadcast as a blind-carbon-copy (BCC) email from wanka95@gmail.com. This is GDPR-noncompliant if any EU subscribers are present but is legally acceptable for US-only small lists. Include an unsubscribe instruction in the email footer manually.

### Scenario 4b: Canva Offline or Inaccessible

**Trigger**: Canva experiences a platform outage or the account is inaccessible during the production window.

**Duration assessment**:
- Under 4 hours: wait. Canva's uptime is historically above 99.9%. Short outages are not worth triggering a tool migration. Check Canva's status page (canvadesigncompany.statuspage.io) for outage updates.
- 24+ hours: use a fallback tool.

**Fallback tool — Adobe Express (free tier)**:
Adobe Express at express.adobe.com has comparable template and layout features to Canva Free. Notable advantage: Adobe Express Free includes background removal, which Canva Free does not.

Migration checklist:
- [ ] Canva Brand Kit colors and fonts noted locally (available in tool-integration-map.md Section 2 — Seedwarden Brand Quick Reference block from CANVA_EXECUTION_PLAYBOOK.md)
- [ ] All uploaded lifestyle photos saved locally (they were sourced from `/projects/seedwarden/marketing/lifestyle-photos/etsy-ready/` — already local)
- [ ] Zone card content notes available (CANVA_ZONE_CARD_BATCH_WORKFLOW.md)
- Build master templates in Adobe Express from scratch — approximate 2 hours for both masters
- Rebuild zone cards in Adobe Express — approximate 60–90 minutes each

If the outage occurs after zone cards are partially built in Canva: take screenshots of completed cards before the outage fully prevents access. Use screenshots as visual reference when rebuilding in Adobe Express.

**Fallback tool — Google Slides (emergency)**:
If neither Canva nor Adobe Express is accessible: Google Slides at slides.google.com supports custom canvas sizes, image uploads, and PDF export. It is not a design tool but it can produce functional zone cards. Set slide dimensions to 1200×900px (File > Page setup > Custom). Add content as text boxes and image placeholders. Export as PDF.

The output will lack the visual refinement of Canva but will be functional for digital delivery. A rough zone card that works is better than a polished zone card that cannot be exported.

### Scenario 4c: Etsy Account Issues

**Trigger**: Etsy account is suspended, a listing is removed, or the shop shows an error during the lifestyle image upload.

**Listing-level image error**: If a specific listing fails to accept an image upload (Etsy returns an error), try: reducing the JPEG quality to 85% (smaller file size), switching from PNG to JPEG format, or uploading from a different browser. Etsy's image processor occasionally rejects files with certain metadata profiles. Running the file through Squoosh and re-exporting eliminates most metadata issues.

**Shop-level suspension**: Log into Etsy Seller Account > Account Health. Any suspension notice will appear there with the reason. Etsy suspensions during a launch window are low probability but not zero — the risk increases if listings are edited rapidly in a short window (which the Phase 2 upload involves). Space out listing edits at no more than 5 listings per 30 minutes to avoid triggering Etsy's anomalous activity detection.

**Contingency if Etsy is unavailable on launch day**: The launch is not solely Etsy-dependent. The Kit broadcast email and social media posts can still execute on schedule. They simply direct traffic to the Etsy store — if the store is temporarily inaccessible, traffic will bounce. Delay the broadcast email by 24 hours if the Etsy outage persists past 10am on May 30.

---

## Scenario 5: Launch Day Overages — Zone 5 Photos Late or Other Partial Launch

**Trigger**: On launch day (May 30), one zone's assets are not finalized — specifically, a lifestyle image for a high-traffic product or a zone card PDF has a critical error discovered during the T-2h QA check.

**Decision rule**: Launch with what is ready. Withholding the entire launch because one asset has an issue is always the wrong call. The launch broadcast goes to a list of subscribers who are waiting. Every day of delay costs subscribers (people forget) and momentum.

**Go-live with Zones 1–4 protocol (if Zone 5 content has a critical error)**:
This scenario is unlikely because Zone 5 is the first zone built and the most-tested, but here is the protocol:

1. Remove the broken Zone 5 download link from Email 1 Zone 5 variant in Kit. Replace with: "Your Zone 5 card is being finalized — I'll send it to you directly within 48 hours."
2. Launch all other components on schedule: Etsy images, Kit broadcast to full list, social posts.
3. Fix the Zone 5 issue on May 30 or May 31.
4. When fixed: manually send Email 1 Zone 5 to all subscribers tagged "zone-5" as a one-off direct email from Kit. Subject: "Your Zone 5 card is ready." This auto-delivers within 24 hours of the original launch.

**Go-live with partial lifestyle image library**:
If 15 of 21 lifestyle images are ready on May 29 and 6 are not:

1. Upload the 15 ready images to their respective Etsy listings.
2. Leave the 6 unready listings at their current state (slots 1–3 only). They are still live, still discoverable, still purchasable.
3. In the launch broadcast email, do not reference "all 21 products now have lifestyle photos." Frame the email around the zone card lead magnet and the overall Phase 2 launch — the image count is not a buyer-facing metric.
4. Upload the remaining 6 images as a post-launch update within 7 days.

**Contingency email — Zone 5 follow-up 48 hours after launch**:
If a significant piece of content (a popular product's lifestyle images or a zone card) is not ready at launch but will be ready within 48 hours:

Pre-write this email and stage it as a draft in Kit before launch day:
Subject: "One more thing — [Zone 5 / the [Product Name] images] are live now"
Body: Brief, warm. Explains you wanted to make sure it was right before sending. Includes the download link or Etsy listing link. No apology necessary — framing this as "worth the wait" is accurate and avoids drawing attention to any slip.

Stage this draft in Kit before launch day. If the contingency is triggered, update the body with the correct links and schedule the send.
