---
title: "Phase 2 Pre-Launch Readiness Checklist — 7-Day Validation"
date: 2026-05-06
status: production-ready
window: May 24 to May 29, 2026
references:
  - tool-integration-map.md (detailed handoff specs)
  - may-30-launch-sequence.md (launch day QA)
  - phase-2-launch-timeline.md (25-day master plan)
---

# Phase 2 Pre-Launch Readiness Checklist
## 7-Day Validation Window: May 24 to May 29

**Purpose**: Structured verification that every track is complete and functional before launch day begins. This checklist is designed to surface problems 7 days before launch — not on launch morning. Each item that fails has enough lead time for correction.

**How to use**: Work through each section in order on the day specified. A single missed item does not abort the launch — it creates a time-boxed fix task. Log any fix tasks in WORKLOG.md with the planned resolution date.

**Sections**:
1. Canva Verification (May 24-25)
2. Etsy Verification (May 25-26)
3. Kit Verification (May 25-27)
4. Social Verification (May 27-28)
5. Final 48-Hour Verification (May 28-29)
6. Launch Day Go/No-Go Decision (May 29)

---

## Section 1: Canva Verification
### Complete by: May 25

**Zone Card Production**

- [ ] Zone 3 card: built, content verified, no placeholder text in any field
- [ ] Zone 4 card: built, content verified, no placeholder text in any field
- [ ] Zone 5 card: built, content verified, no placeholder text in any field
- [ ] Zone 6 card: built, content verified, no placeholder text in any field
- [ ] Zone 7 card: built, content verified, no placeholder text in any field
- [ ] Zone 8 card: built, content verified, no placeholder text in any field
- [ ] Zone 9 card: built, content verified, no placeholder text in any field
- [ ] Zone 10 card: built, content verified, no placeholder text in any field

**Zone Card Footer Verification** (critical — footer URLs must be live pages, not placeholders)

- [ ] Every zone card footer contains the correct Etsy store URL (not "[ETSY-URL]" placeholder)
- [ ] Every zone card footer contains the correct Kit landing page URL (not "[KIT-URL]" placeholder)
- [ ] Etsy store URL tested — opens Etsy store, not a 404 or draft page
- [ ] Kit landing page URL tested — opens the Seedwarden zone card signup form

**Zone Card Export Verification**

- [ ] All 8 zone cards exported from Canva at PDF Print quality (not PDF Standard)
- [ ] All 8 PDFs named correctly: `zone-[N]-quick-start-card.pdf` (lowercase, hyphenated)
- [ ] File sizes checked: all between 1-4MB (if under 500KB, was likely exported at PDF Standard by mistake — re-export)
- [ ] One PDF opened at 100% zoom on screen — confirm text in the fine-print footer is crisp and not blurry
- [ ] One PDF printed (if printer available) — confirm no unexpected color shifts

**Lifestyle Image Production**

- [ ] SW-Master-FlatLay template built (2400×2400px, brand strip, product overlay slot)
- [ ] SW-Master-Tablet template built (1280×960px base, resized to 2400×2400 on export)
- [ ] Cluster A lifestyle images: 8 products × 2 images = 16 files complete
- [ ] Cluster B lifestyle images: 4 products × 2 images = 8 files complete
- [ ] Cluster C lifestyle images: 3 products × 2 images = 6 files complete
- [ ] Cluster D+E composited images: 5 products × 2 images = 10 files complete (uses stock-raw)
- [ ] Total lifestyle image count: 42 files in `marketing/lifestyle-photos/etsy-ready/`
- [ ] All files under 2MB (run Squoosh on any over 2MB)
- [ ] All files named: `[product-slug]-slot4.jpg` and `[product-slug]-slot5.jpg`

**Dimension Verification**

- [ ] Random sample of 5 lifestyle images: open in any image viewer, confirm dimensions are 2400×2400px
- [ ] Random sample of 3 Pinterest pins: confirm dimensions are 1000×1500px
- [ ] Instagram launch post image: confirm 1080×1080px
- [ ] TikTok launch content: confirm 9:16 aspect ratio (1080×1920px for video thumbnail)

**Canva Section Status**: Date completed: ___________ Issues found: ___________

---

## Section 2: Etsy Verification
### Complete by: May 26

**Listing Completeness**

- [ ] All target Phase 2 Etsy listings are in "Active" (published) status — none left as Draft
- [ ] All listings have exactly 5 images uploaded (slots 1-5)
- [ ] Slot 1 (primary thumbnail): mockup image — product cover visible at thumbnail size
- [ ] Slot 2: second mockup angle
- [ ] Slot 3: third mockup (lifestyle staging or detail)
- [ ] Slot 4: lifestyle flat-lay from `etsy-ready/`
- [ ] Slot 5: in-use contextual from `etsy-ready/`
- [ ] No listing has a black, white, or blank image in any slot

**Listing Image Quality Check (public view)**

Check from a logged-out browser:
- [ ] 3 listings checked: open each in Etsy search view and click in. Confirm gallery shows lifestyle images without cropping the product out of the primary viewable area.
- [ ] Etsy's zoom feature tested on 2 listings: click the "+" zoom icon. Confirm image stays sharp at full zoom (not pixelated). If pixelated: the image was exported below 2400px — re-export and replace.

**Coupon and Pricing**

- [ ] SEEDWARDEN15 coupon: Etsy Shop Manager > Marketing > Sales and Coupons — shows "Active"
- [ ] Coupon discount: 15% off
- [ ] Coupon has no minimum order requirement (Kit Email 5 makes no mention of a minimum — coupon must match the email's claim)
- [ ] Coupon has no expiry OR expiry is set far enough out that it will not expire during the first subscriber's Email 5 window (Email 5 sends Day 10 post-signup — last new signup before June 14 hits Email 5 by June 24; coupon must be active through June 30 minimum)
- [ ] Phase 2 bundle listings: confirm all bundle Etsy URLs are correct and active (for use in Kit email UTM links)

**SEO and Listing Copy**

- [ ] Listing titles: natural language format, under 15 words (Etsy May 2026 title algorithm)
- [ ] All listings have 13 tags (maximum allowed by Etsy)
- [ ] Etsy store bio links to Kit landing page URL
- [ ] Any seasonal keywords relevant to May/June are present in tags (per `may-2026-competitor-pricing-update.md` seasonal keyword table)

**Etsy Section Status**: Date completed: ___________ Issues found: ___________

---

## Section 3: Kit Verification
### Complete by: May 27

**Account Configuration**

- [ ] Kit account email: wanka95@gmail.com (or Seedwarden custom domain)
- [ ] Kit sender name: "Seedwarden" (not personal name)
- [ ] SPF record: Kit Settings > Email Settings shows green checkmark
- [ ] DKIM record: Kit Settings > Email Settings shows green checkmark
- [ ] If using Gmail as sender: open rate benchmark noted (Gmail DMARC may cause alignment issues — monitor open rate in first week)

**Landing Page**

- [ ] Landing page is published (not Draft)
- [ ] Landing page URL is live and accessible from incognito browser
- [ ] Form fields: First Name (required), Email (required), Growing Zone dropdown (required; options: Zone 3, 4, 5, 6, 7, 8, 9, 10)
- [ ] CTA button text: "Send My Zone Card" (exact)
- [ ] Landing page does not show any Kit or Seedwarden branding errors (logo absent, wrong colors, form fields not rendering)
- [ ] Landing page URL is present in all social bios (Instagram, TikTok, Pinterest)

**Email Sequence Build**

- [ ] Email 1, Zone 3 variant: subject line set, body loaded, zone card download link correct, delay set to "Immediately"
- [ ] Email 1, Zone 4 variant: all of the above
- [ ] Email 1, Zone 5 variant: all of the above
- [ ] Email 1, Zone 6 variant: all of the above
- [ ] Email 1, Zone 7 variant: all of the above
- [ ] Email 1, Zone 8 variant: all of the above
- [ ] Email 1, Zone 9 variant: all of the above
- [ ] Email 1, Zone 10 variant: all of the above
- [ ] Email 2: body loaded, delay set to Day 2 (48 hours)
- [ ] Email 3: body loaded, delay set to Day 5; seed-saver click-tag link present
- [ ] Email 4: body loaded, delay set to Day 7; city-grower and preservationist click-tag links present
- [ ] Email 5: body loaded, delay set to Day 10; SEEDWARDEN15 coupon code present with exact Etsy UTM link

**Email Link Verification**

- [ ] Email 1 Zone 5: download link uses `?export=download&id=` format — click link in Kit Preview, confirm PDF downloads in incognito
- [ ] Email 1 Zone 7: same verification
- [ ] Email 3 Etsy product link: uses UTM format `?utm_source=kit&utm_medium=email&utm_campaign=welcome-sequence&utm_content=email3-[slug]`
- [ ] Email 4 Etsy product links: all three segmentation links use UTM format
- [ ] Email 5 coupon link: links to the Etsy store with UTM `utm_campaign=welcome-sequence&utm_content=email5-coupon`

**Automation**

- [ ] Welcome automation is in "Published" status (not Draft, not Paused)
- [ ] Automation trigger: Form submitted (on the Seedwarden zone card landing page specifically)
- [ ] Automation action 1: Apply tag "new-subscriber"
- [ ] Automation action 2: Add to Seedwarden Welcome sequence
- [ ] Automation action 3: Zone routing — if Zone = [N], send Email 1 variant [N] (for all 8 zones)
- [ ] Behavioral tags configured: "seed-saver" tag fires on Email 3 link click, "city-grower" tag fires on Email 4 city link click, "preservationist" tag fires on Email 4 preservation link click

**End-to-End Tests** (must complete both before launch)

Test 1 (Zone 5):
- [ ] Open Kit landing page in incognito window
- [ ] Sign up: test name, secondary email address, Zone 5 selected
- [ ] Email 1 arrives within 60 seconds
- [ ] Email 1 subject line confirms Zone 5
- [ ] Download link in Email 1 opens a download dialog (not a viewer) in incognito
- [ ] The downloaded PDF is the Zone 5 zone card (not Zone 6 or another zone)
- [ ] Email did not land in spam folder

Test 2 (Zone 3 or Zone 7):
- [ ] Open landing page in incognito, new test email
- [ ] Sign up with Zone 7 selected (or Zone 3)
- [ ] Email 1 arrives, subject confirms Zone 7
- [ ] Download link delivers correct zone PDF
- [ ] Email did not land in spam

**Broadcast Staging**

- [ ] Launch broadcast email drafted: subject line from `marketing/email-and-launch-plan.md` launch broadcast section
- [ ] Launch broadcast send target: "All Confirmed Subscribers" (NOT "All Subscribers")
- [ ] Launch broadcast status: "Scheduled" for May 30 12:00pm
- [ ] UTM parameters applied to all Etsy product links in the broadcast

**Kit Section Status**: Date completed: ___________ Issues found: ___________

---

## Section 4: Social Verification
### Complete by: May 28

**Account Setup**

- [ ] Instagram Business account: active, handle confirmed (@seedwarden or agreed fallback)
- [ ] TikTok Business account: active, handle confirmed
- [ ] Pinterest Business account: active, handle confirmed
- [ ] All three profiles: Seedwarden logo uploaded as profile image (from `logos/seedwarden_logo_1.png`)
- [ ] All three bios: Kit landing page URL present and linking correctly
- [ ] Instagram bio: includes relevant keywords (zone cards, native plants, seed saving)
- [ ] TikTok bio: 80 characters max, CTA to link in bio
- [ ] Pinterest bio: includes keyword-rich profile description

**Pre-Launch Content**

- [ ] Day 1 Reel (origin story) uploaded to Instagram and TikTok
- [ ] Day 3 Carousel posted to Instagram
- [ ] Batch 1 Pinterest pins (6 pins) scheduled and live
- [ ] Account has at least 1 week of posting history before launch day (reduces algorithm suppression of launch posts)

**Launch Content Staging in Buffer/Later**

- [ ] Instagram launch post: image uploaded, caption + hashtags from calendar loaded, scheduled for May 30 2:00pm
- [ ] TikTok launch post: video file uploaded, caption loaded, scheduled for May 30 2:00pm
- [ ] Pinterest launch pins: 3-5 pins uploaded at 1000×1500px, descriptions loaded, scheduled for May 30 3:30pm

**Buffer/Later Connection Check**

- [ ] Instagram connection: active (green status in Buffer Settings > Connected Accounts)
- [ ] TikTok connection: active
- [ ] Pinterest connection: active
- [ ] All three connections re-authorized within the last 7 days (OAuth tokens)

**Content Quality Check**

- [ ] Instagram post image preview in Buffer: product is visible and not cropped
- [ ] TikTok post: confirms it is a video file, not a static image
- [ ] Pinterest pins: product is in upper two-thirds of the 1000×1500 frame (not bottom-cropped in feed)
- [ ] Captions contain no broken links (Etsy store links, Kit landing page links)

**Social Section Status**: Date completed: ___________ Issues found: ___________

---

## Section 5: Final 48-Hour Verification
### Complete May 28-29

**May 28 — System Checks**

- [ ] Re-authorize all three Buffer connections (takes 5 minutes; prevents launch-day OAuth failure)
- [ ] Open all 8 Google Drive zone card download URLs in incognito — confirm all still download correctly (Drive sharing settings can reset if not checked)
- [ ] Run Kit end-to-end test one final time (Zone 5) — confirm automation is still live and routing correctly
- [ ] Confirm SEEDWARDEN15 coupon still shows "Active" in Etsy

**May 29 — Pre-Launch Staging Confirmation**

- [ ] All 21 Etsy listings confirmed "Active" with 5 images
- [ ] Kit launch broadcast shows "Scheduled" for May 30 12:00pm
- [ ] Buffer/Later: all three launch posts show "Scheduled" status with correct times
- [ ] WORKLOG.md entry written for May 29: list of all items verified, any outstanding issues and their resolution status
- [ ] customer-analytics.csv: fill in "Pre-Launch Baseline" row with current Etsy shop views (7 days), current Kit subscriber count, current social follower counts

**Optional but recommended — May 29**

- [ ] Test sign-up from phone (not desktop): open Kit landing page on mobile browser, complete form, confirm Email 1 arrives and download link works on mobile (mobile browsers handle Google Drive downloads differently)
- [ ] Open Etsy store on phone in incognito: confirm lifestyle images load correctly on mobile view

---

## Section 6: Launch Day Go/No-Go Decision
### Complete by 8:00pm May 29

Review the status of all four tracks. Make a GO or NO-GO decision for each track.

| Track | GO Criteria | GO/NO-GO | If NO-GO: Recovery Path |
|---|---|---|---|
| Etsy | All 21 listings active with 5 images, coupon active | ___ | Upload any missing images, activate coupon — takes 30 min maximum |
| Kit | Automation published, broadcast scheduled, e2e test passed | ___ | Re-run test, fix automation routing if broken — takes 60 min maximum |
| Social | All posts scheduled in Buffer, connections active | ___ | Reschedule manually or plan manual posting on launch day |
| Canva/Files | All 8 zone card PDFs downloadable via Google Drive | ___ | Re-share Drive files, update Kit email links if needed — takes 30 min |

**Decision logic**:
- All four tracks GO: Proceed to May 30 launch.
- Etsy NO-GO only: Proceed with email and social launch. Etsy images can be uploaded same-day.
- Kit NO-GO only: Proceed with Etsy and social launch. Kit issues that cannot be resolved by May 30 8am shift to manual email workaround (see `june-6-contingency-path.md`).
- Canva/Files NO-GO (broken download links): Hard stop. Fix all 8 download links before launch. The zone card download is the primary value delivery of the email automation — a broken link on launch day corrupts the subscriber's first experience.
- Social NO-GO: Social posts are non-critical for revenue. Proceed with Etsy and email. Post to social manually on May 30 if scheduler is not working.

**Final confirmation entry in WORKLOG.md** (required before May 30):

```
May 29 Pre-Launch GO/NO-GO:
- Etsy: [GO/NO-GO]
- Kit: [GO/NO-GO]
- Social: [GO/NO-GO]
- Canva/Files: [GO/NO-GO]
- Overall: [LAUNCH PROCEEDING / SHIFTED TO JUNE 6]
- Outstanding issues: [list or "none"]
```

---

## Quick-Reference: Fix Times for Common Issues

| Issue | Fix Time | Where to Fix |
|---|---|---|
| Missing Etsy image (1 slot) | 2 min | Etsy Shop Manager > Edit listing > Photos |
| Listing in Draft status | 30 sec | Etsy Shop Manager > click Publish |
| SEEDWARDEN15 coupon expired | 3 min | Etsy Shop Manager > Marketing > Coupons > Create |
| Google Drive file not downloadable | 5 min | Drive > file > Share > change to "Anyone with the link" |
| Kit Email 1 wrong zone card URL | 5 min | Kit > Sequences > Email 1 [zone] > edit link |
| Kit automation paused | 30 sec | Kit > Automations > Resume |
| Kit broadcast in Draft | 10 min | Kit > Broadcasts > schedule for May 30 12pm |
| Buffer post not scheduled | 5 min | Re-create post in Buffer, schedule manually |
| Buffer connection expired | 2 min | Buffer Settings > Connected Accounts > Reconnect |
| Wrong image on Etsy slot | 5 min | Edit listing, drag correct image to correct slot |

---

*Generated: 2026-05-06. References: tool-integration-map.md (handoff specs and failure modes), may-30-launch-sequence.md (launch day QA), phase-2-launch-timeline.md (25-day master plan).*
