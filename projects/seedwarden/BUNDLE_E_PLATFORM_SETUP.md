---
title: "Bundle E Platform Setup & Upload Procedures"
prepared: 2026-05-13
status: production-ready
execution-window: May 15-18, 2026
scope: Pre-upload verification, Etsy listing setup, Kit email setup, social media scheduling, testing protocol, troubleshooting matrix, rollback procedure
---

# Bundle E — Platform Setup & Upload Procedures

**Purpose**: Step-by-step operational guide for configuring all platforms between May 15-18 so that May 19 launch executes without improvisation. Every task in this document assumes the 5 guides are complete and QA-passed by May 14 EOD.

**Prerequisites before starting**:
- [ ] All 5 guides are complete (1,000+ words each)
- [ ] QA checklist (BUNDLE_E_QA_CHECKLIST.md) is passed for all 5 guides
- [ ] All 15 photos are sourced, attributed, and embedded in guides
- [ ] Guide PDFs exported from Canva or generated via Pandoc, each under 5 MB

**Total platform setup time**: 9-12 hours across May 15-18. Do not compress into fewer days — each day has a specific function and verification step.

---

## Pre-Upload Verification (May 15 Morning, 08:00-12:00 local)

Run this block before touching any platform. It takes 2-3 hours and prevents the majority of platform-day issues.

### Guide File Verification

- [ ] All 5 guide PDF files exist in your local working folder
- [ ] Each PDF opens correctly (spot-check each one)
- [ ] Each PDF is under 5 MB (Etsy hard limit). If any exceeds 5 MB:
  - Option A: Re-export from Canva with "Lower quality" setting
  - Option B: Use Squoosh or TinyPDF (browser tool) to compress embedded images
  - Option C: Export each guide as a separate PDF, then merge using a free PDF tool (Smallpdf, ILovePDF) with compression enabled
- [ ] All 5 PDFs together equal less than 25 MB (not a platform limit, but confirms file sizes are reasonable)

**File naming convention for upload** (use exactly these names — referenced in the Kit email attribution template):
```
bundle-e-garlic-mustard-guide.pdf
bundle-e-japanese-knotweed-guide.pdf
bundle-e-autumn-olive-guide.pdf
bundle-e-purslane-guide.pdf
bundle-e-multiflora-rose-guide.pdf
```

### Account Access Verification

Before platform work begins, confirm you can log in to all platforms. Do not assume sessions are active.

- [ ] Etsy: Log in to Etsy.com (wanka95@gmail.com). Confirm you reach Etsy Shop Manager for the seedwarden shop. If 2FA is required, have backup codes ready: `projects/seedwarden/etsy_2fa_backup_codes.txt`
- [ ] Kit: Log in to kit.co. Confirm subscriber list is visible and existing automations are not broken.
- [ ] Social scheduling tool (Buffer or Later): Log in and confirm Instagram, Pinterest, and TikTok connections are active. If any shows "Reconnect required," fix it now before scheduling content.
- [ ] Google Drive: If using Google Drive to host guide PDFs for Kit email delivery, confirm drive is accessible and sharing permissions are set to "Anyone with the link."

---

## Day 1 (May 15): Etsy Listing Finalization

**Time estimate**: 3-4 hours
**Output**: Bundle E Etsy listing live in Draft status, all 5 guide PDFs uploaded, cover image assigned, launch date set to May 19

### Step 1: Create the Bundle E Listing

1. In Etsy Shop Manager, click "Add a listing"
2. Listing type: Digital download
3. Title: Paste exactly from BUNDLE_E_PUBLICATION_PACKAGE.md Section 1:
   ```
   Invasive Edibles: 5-Species Foraging Guide — Harvest, Process, Profit
   ```
4. Category: Craft Supplies & Tools > Patterns & How To > Gardening (same as Phase 1 listings)
5. Description: Paste hero description from BUNDLE_E_PUBLICATION_PACKAGE.md Section 1 (the full block starting "INVASIVE SPECIES ARE PROFIT")
6. Price: $24.99
7. Quantity: Leave as unlimited (digital product)
8. Tags: Paste all 13 tags from BUNDLE_E_PUBLICATION_PACKAGE.md Section 1

### Step 2: Upload the 5 Guide PDFs as Digital Files

In the Etsy listing editor, scroll to "Digital files" section:
1. Click "Upload a file"
2. Upload each of the 5 PDFs individually:
   - `bundle-e-garlic-mustard-guide.pdf`
   - `bundle-e-japanese-knotweed-guide.pdf`
   - `bundle-e-autumn-olive-guide.pdf`
   - `bundle-e-purslane-guide.pdf`
   - `bundle-e-multiflora-rose-guide.pdf`
3. After each upload, confirm the file name appears in the digital files list and shows a green checkmark (not an error indicator)
4. Etsy will warn if a file exceeds 20 MB — if this occurs, return to the compression step

### Step 3: Upload Cover Image

Cover image requirements: Minimum 2000px on short side, square or landscape, JPEG or PNG
- If a custom Bundle E mockup exists in `projects/seedwarden/mockups/`, use it
- If no Bundle E mockup exists: Create a simple cover in Canva using the existing Canva brand template, or use one of the plant photos (e.g., Japanese Knotweed shoots) with a text overlay "Invasive Edibles: 5-Species Foraging Bundle"
- Secondary image (optional): Add one species page screenshot as image 2 to show interior content quality

### Step 4: Set Launch Scheduling

- In the listing editor, look for "Schedule your listing" or publishing options
- Set status to "Draft" (not yet active)
- Note: Etsy does not have built-in listing scheduling on all plan types. If scheduling is unavailable:
  - Leave listing in Draft
  - On May 19 morning, manually change status to "Active" — takes 30 seconds

### Step 5: Save and Verify Draft

- [ ] Save listing as Draft
- [ ] Click "Preview listing" — confirm listing renders correctly in buyer view
- [ ] Confirm all 5 digital files are visible in the listing preview
- [ ] Confirm price shows $24.99
- [ ] Save the Etsy listing URL (will be something like `etsy.com/listing/[number]/invasive-edibles`)
- [ ] Update all email template links in BUNDLE_E_PUBLICATION_PACKAGE.md: replace `[YOUR_LISTING_ID]` with the actual listing number

---

## Day 2-3 (May 16-17): Email Sequence and Social Media Setup

**Time estimate**: 4-5 hours across 2 days
**Output**: All 5 Kit emails loaded and scheduled, 7 social media posts scheduled

### Kit Email Setup (May 16, 2-3 hours)

#### Step 1: Create a New Broadcast for Each Launch Email

In Kit, navigate to Broadcasts (not Automations — these are one-time campaign emails, not automated sequences):

1. Create Broadcast — Email 1 (Launch)
   - Subject line option A: "Invasive species are profit: here's how to harvest them"
   - Preview text: "5 invasive plants you can eat starting this week"
   - Body: Paste Email 1 body from BUNDLE_E_PUBLICATION_PACKAGE.md Section 2
   - Replace `[LINK: Pre-Order Bundle E — $24.99]` with actual Etsy listing URL
   - Send to: All subscribers
   - Schedule: May 19, 9:00 AM EST
   - Status: Scheduled (not Draft, not Sent)

2. Repeat for Emails 2-5, using schedule from BUNDLE_E_PUBLICATION_PACKAGE.md:
   - Email 2: May 22, 10:00 AM EST
   - Email 3: May 24, 2:00 PM EST
   - Email 4: May 26, 9:00 AM EST
   - Email 5: May 28, 11:00 AM EST

#### Step 2: Verify Email Rendering

- [ ] Send a test email to wanka95@gmail.com for Email 1 only (do not test-send all 5 — wastes time)
- [ ] Confirm Etsy link is live and clickable in the test email
- [ ] Confirm subject line displays correctly in mobile email preview
- [ ] Confirm "From" name shows "Anya" or "Seedwarden" (not a system default)

#### Step 3: Confirm Scheduling Status

In Kit Broadcasts, verify:
- [ ] Email 1 shows "Scheduled: May 19, 9:00 AM EST"
- [ ] Emails 2-5 show "Scheduled" status with correct dates
- [ ] None show "Draft" status

### Social Media Scheduling (May 17, 2 hours)

Use Buffer, Later, or manual scheduling. The sprint plan calls for 10 posts; schedule the first 7 now (May 19-25) and add posts 8-10 manually during the campaign.

#### Posts to Schedule Now

| Post # | Date | Time (EST) | Platform | Format | Content Source |
|---|---|---|---|---|---|
| 1 | May 19 | 10:30 AM | Instagram Reels + TikTok | 15-30 sec video | BUNDLE_E_PUBLICATION_PACKAGE.md Post 1 script |
| 2 | May 20 | 9:00 AM | Instagram Carousel + Pinterest | 5-7 slide carousel | Post 2 caption + Garlic Mustard content |
| 3 | May 21 | 10:00 AM | TikTok | 30-sec video | Post 3 (Knotweed ID) |
| 4 | May 22 | 9:30 AM | Instagram (feed post) | Static image | Post 4 (Why We Harvest Invasives) |
| 5 | May 23 | 11:00 AM | Instagram Reels | Video | Post 5 (Autumn Olive) |
| 6 | May 24 | 9:00 AM | Instagram Carousel | 6-slide | Post 6 (Purslane + Multiflora Rose) |
| 7 | May 25 | 10:00 AM | TikTok | 30-sec | Post 7 (Remove Invasives) |

**For each post**:
- [ ] Caption is written and pasted into scheduling tool
- [ ] Image or video file is uploaded and attached
- [ ] Hashtags are included (copy from post captions in BUNDLE_E_PUBLICATION_PACKAGE.md)
- [ ] Etsy link is in bio — confirm via Instagram Settings > Bio before May 19
- [ ] Scheduling tool shows "Scheduled" (green) status, not "Draft"

**If you do not have video content for Reels/TikTok posts**: Replace video post with a static carousel showing photo + text overlay. This reduces engagement but does not block launch. A photo of Japanese Knotweed shoots with text overlay "This is harvestable RIGHT NOW" is a functional replacement.

---

## Day 4 (May 18): Final Verification and Content Backup

**Time estimate**: 2-3 hours
**Output**: All platforms verified, content backup completed, contingency contacts documented

### Step 1: End-to-End Platform Verification

**Etsy verification (30 minutes)**:
- [ ] Log in, open Bundle E listing in Draft status
- [ ] Click "Preview listing" — confirm all 5 digital files still attached
- [ ] Confirm price still shows $24.99 (Etsy sometimes resets draft listings)
- [ ] Attempt a test purchase if your Etsy plan allows (some plans allow self-purchase testing)
- [ ] If test purchase is not possible: confirm the "Purchase" button is visible in preview and digital files section shows 5 files ready for delivery
- [ ] Confirm the Etsy listing URL (copy and paste into a browser in incognito mode) reaches the listing

**Kit verification (20 minutes)**:
- [ ] Open Kit Broadcasts > confirm all 5 emails show "Scheduled" status
- [ ] Click Email 1 > Edit > confirm Etsy link is correct (not the placeholder `[YOUR_LISTING_ID]`)
- [ ] Send a second test of Email 1 to confirm no changes broke the link
- [ ] Check subscriber count and note it (this is your baseline for measuring list growth during the campaign)

**Social media verification (20 minutes)**:
- [ ] Log into scheduling tool > confirm all 7 posts still show "Scheduled" status
- [ ] Check Instagram bio contains the Etsy listing link (direct link, not just shop home)
- [ ] Check TikTok bio contains the Etsy link if TikTok is being used
- [ ] If any post shows a platform connection error: reconnect the account, then re-check the post's scheduled status

### Step 2: Content Backup

Create a single backup folder before May 19. If something breaks on any platform, you need to be able to re-upload without hunting for files.

Create: `projects/seedwarden/bundle-e-launch-backup/` containing:
- [ ] All 5 guide PDFs (copies, not originals — keep originals in working folder)
- [ ] Cover image file
- [ ] A text file: `email-links.txt` — containing Etsy listing URL, Kit account login URL, social profiles
- [ ] A PDF or screenshot export of the Etsy listing draft (in case the Etsy listing is accidentally deleted)

### Step 3: Press Release Distribution

From BUNDLE_E_PUBLICATION_PACKAGE.md Section 5, the press release is ready. Distribute today (May 18 EOD) so outlets receive it 24 hours before launch:

**Target outlets** (minimum 5, target 10):
1. Mother Earth News: Use their online submission form or editor email
2. Permaculture Research Institute: Contact form at permaculturenews.org
3. HARO (Help A Reporter Out): Submit as a source if any active queries match "foraging", "invasive species", "permaculture"
4. Local agricultural extension newsletters: Search "[your state] invasive species newsletter" for relevant regional outlets
5. Homesteading Facebook groups: This is not press per se, but a post in a 10,000-member homesteading group reaches more relevant buyers than most publications

**How to send**:
- [ ] Replace all `[YOUR_LISTING_ID]` and `[YOUR-SHOP-NAME]` placeholders in the press release
- [ ] Add your actual name to the quote ("said Anya [your last name]") or use just "Anya, Seedwarden founder"
- [ ] Send via email with subject line: "Press Release: New Guide Teaches Foragers to Harvest Invasive Species"
- [ ] Log each outlet contacted in a quick text file — you will need this for follow-up

---

## Testing Protocol Summary

Run these tests before each platform goes live:

| Platform | Test | How to Test | Pass Criteria |
|---|---|---|---|
| Etsy | Listing renders correctly | Open listing URL in incognito browser | All images visible, price correct, description complete |
| Etsy | Digital files attached | View listing as buyer | "Instant download" shown, 5 files listed |
| Kit | Email sends and link works | Test send Email 1 to yourself | Email arrives, Etsy link opens correctly |
| Kit | Scheduling active | Check Broadcasts panel | All 5 emails show "Scheduled" status |
| Social | Posts scheduled | Scheduling tool dashboard | All 7 posts show "Scheduled" with correct dates |
| Social | Bio link works | Open Instagram/TikTok profile | Link in bio opens Etsy listing |

---

## Troubleshooting Matrix

| Problem | Likely Cause | Solution | Time Required |
|---|---|---|---|
| Etsy rejects PDF upload | File over 20 MB | Compress PDF using TinyPDF or re-export at lower quality | 15-30 min |
| Etsy listing won't save | Browser session timed out | Refresh page, save draft again. If fields reset, paste from backup | 10-20 min |
| Kit email shows broken link | Placeholder not replaced | Edit broadcast, replace placeholder URL with actual Etsy URL, save | 5 min |
| Kit broadcast won't schedule | Scheduled time is in the past | Change scheduled time to a future time, then reschedule | 5 min |
| Social post shows "Connection error" | Platform OAuth token expired | In scheduling tool Settings > Connected Accounts, reconnect platform | 10-15 min |
| Instagram link not clickable in post | Instagram does not allow links in captions | Add "link in bio" to caption, confirm bio URL is correct | 5 min |
| Guide PDF appears corrupted on open | Export failed partially | Re-export PDF from source. Open in multiple PDF readers to verify | 20-30 min |
| Kit account shows 0 subscribers | Account is new / list not imported | If existing subscriber list exists elsewhere, import via CSV. If list is small, launch with what's there — launch email still goes out | 20-40 min |

---

## Rollback Procedures

If something breaks after the May 19 launch:

**Etsy listing goes down (deleted, suspended, or inaccessible)**:
1. Check Etsy Shop Manager for any policy violation notices
2. If deleted: re-create from backup (use the saved listing draft screenshot or text backup)
3. Update all email and social links with the new listing URL
4. Send a brief email to your list: "Quick note — the Etsy listing moved, here's the updated link: [URL]"
5. Time to restore: 30-60 minutes

**Email blast sends with wrong link**:
1. Cannot unsend an email once delivered
2. Send a follow-up email within 2 hours: "Correction: the correct link is [URL]. Apologies for the confusion."
3. Kit allows you to duplicate the broadcast and re-send to recipients who did not click
4. The correction email often has higher open rates than the original — do not skip it

**Kit campaign pauses mid-sequence**:
1. Kit > Broadcasts > find the affected scheduled email
2. Check if the email shows "Paused" — if so, click "Resume"
3. If the scheduled time passed while paused, change the send time to "Send immediately"
4. Confirm with a test send that the resumed email still contains the correct link

**Social media posts fail to publish**:
1. Check scheduling tool for error notification
2. Manually publish the failed post from the scheduling tool or directly from the platform
3. Adjust future scheduled posts if the publishing window matters (e.g., if a post was timed to coincide with an email send)
4. Manual backup: all captions and images are saved in `bundle-e-launch-backup/` — copy and paste to post manually if scheduling tool is unavailable

**Guide contains an error discovered post-launch**:
1. Fix the error in the source guide file
2. Re-export PDF
3. In Etsy Shop Manager, go to the listing > Digital files > Replace the affected file with the corrected version
4. Customers who already downloaded receive the corrected version on next download (Etsy does not re-notify buyers of file updates)
5. If the error is significant (incorrect safety information), send an email notification to all purchasers via Kit with subject "Important update to your Invasive Edibles guide"
