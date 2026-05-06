---
title: "Tool Integration Map — Phase 2 Cross-Platform Workflow"
date: 2026-05-06
status: production-ready
references:
  - CANVA_EXECUTION_PLAYBOOK.md
  - KIT_SETUP_NOTES.md
  - phase-2-day-by-day-execution.md
---

# Tool Integration Map
## Phase 2 Cross-Platform Workflow Specifications

**Purpose**: Every place in Phase 2 where content moves from one tool to another has a failure mode. This document specifies exactly how to execute each cross-tool handoff — what format to export, what filename to use, what settings to configure on the receiving end, and where each handoff breaks in practice.

Read this document before beginning any export or import step. Knowing the failure modes in advance saves an hour of debugging per broken handoff.

---

## 1. Canva → Kit Email Embedding

### What transfers
Zone Quick-Start Card PDFs (8 files), Email header image (1 file).

### Export settings from Canva
Zone card PDFs:
- File format: PDF (Print)
- Canva setting: File > Download > PDF Print. This produces a vector-quality PDF with embedded fonts. Do NOT use "PDF Standard" — it reduces color quality and may rasterize text on complex designs.
- DPI: PDF Print uses 300 DPI equivalent. Kit does not display the PDF at high resolution — it delivers it as a download — so high quality here protects against buyer complaints about blurry text when printed.
- Crop marks and bleed: Off (no bleed needed for digital delivery). Toggle is in the PDF export dialog.
- Color space: RGB (Canva default). Do NOT change to CMYK — these files are for screen use and digital download. CMYK shifts greens toward yellow and makes #143b28 look muddy.
- File size: expect 1–4MB per PDF at Print quality. This is acceptable for delivery links. Kit does not host the file — you host it on Google Drive.

Email header image:
- Export as PNG, 600×200px. This matches Kit's email header template slot.
- Use Canva Resize (top bar) to set custom dimensions 600×200 before exporting.
- Color space: RGB. Background: Warm Cream (#F5EDD6) with the Seedwarden logo and tagline centered.
- File size: under 200KB for email embedding. Run through Squoosh if over 200KB.

### File naming convention for Kit integration
```
zone-3-quick-start-card.pdf
zone-4-quick-start-card.pdf
zone-5-quick-start-card.pdf
zone-6-quick-start-card.pdf
zone-7-quick-start-card.pdf
zone-8-quick-start-card.pdf
zone-9-quick-start-card.pdf
zone-10-quick-start-card.pdf
seedwarden-email-header.png
```
Lowercase, hyphenated, no spaces. Kit uses the filename as part of its internal content reference — inconsistent naming creates confusion when troubleshooting which file version is live.

### Upload to Google Drive (intermediary — Kit does not host files directly)
Kit's free tier does not offer file hosting for deliverables. The handoff requires an intermediary host.

Step-by-step:
1. Create Google Drive folder: "Seedwarden Zone Cards — Live." Do not use "Phase 2 Zone Cards" or any draft-sounding name — subscribers may see the folder name in the download URL.
2. Upload each PDF. After upload, right-click each file > Share > Change to "Anyone with the link" > Viewer access. Confirm this setting is active before copying the URL.
3. For each file, copy the direct download URL format: `https://drive.google.com/uc?export=download&id=[FILE-ID]`
   - To find the FILE-ID: the standard share link is `https://drive.google.com/file/d/[FILE-ID]/view`. Copy the FILE-ID portion only.
   - The `?export=download` parameter forces a download dialog rather than opening the Google Docs viewer. Without this parameter, clicking the link in email opens a browser preview — not a download.
4. Test each URL in an incognito window before pasting into Kit. Confirm a download dialog appears, not a viewer or a "request access" screen.

### Embedding the link in Kit
In Kit's email composer, the zone card link is a hyperlinked button or hyperlinked text — not an embedded image of the PDF.

- In Kit's email editor: highlight the CTA text ("Download your Zone 5 card here") > click the link icon > paste the Google Drive download URL.
- Alternatively: use a Kit button block. Style the button with the Seedwarden green (#143b28) background and Warm Cream (#F5EDD6) text. Button width: full-width is preferred for mobile (most email opens are on mobile).
- Do NOT embed the PDF as an attachment in Kit. Attachments trigger spam filters. Always use a hosted download link.
- Alt text for the email header image: "Seedwarden — Zone Quick-Start Cards." Kit's image block has an alt text field — fill it. Missing alt text reduces deliverability scores.

### Known failure modes — Canva to Kit
- **Failure mode 1**: Exporting as PDF Standard instead of PDF Print produces blurry text in the zone card's fine-print footer. Always select PDF Print.
- **Failure mode 2**: Google Drive share link requires Google sign-in. This happens when the sharing setting is left at "Restricted" (the default). Confirm "Anyone with the link" is set before copying the URL.
- **Failure mode 3**: The `?export=download` URL parameter is omitted. The subscriber gets a Google Docs preview page, not a download. Always use the `uc?export=download&id=` format.
- **Failure mode 4**: Kit's click tracking wraps the link URL in a Kit redirect URL. This is normal behavior — do not try to disable it. The Kit click-tracking URL resolves to the Google Drive URL when clicked.
- **Failure mode 5**: Kit's email editor strips the query string from the URL. If the link shows as `https://drive.google.com/file/d/[ID]/view` instead of the download format after pasting, you must re-paste and confirm the full URL was accepted. Check the link by clicking "Preview" in Kit's email editor.

---

## 2. Canva → Etsy Image Upload

### What transfers
21 product lifestyle images (slots 4 and 5), zone card preview image (optional), email header variant (optional).

### Export settings from Canva for Etsy
- Format: JPEG (preferred over PNG for Etsy) — JPEG files load faster in Etsy's CDN and produce smaller file sizes at equivalent visual quality.
- Resolution: 2400×2400px. This is Etsy's recommended minimum for full-quality zoom. Larger is acceptable (up to 5MB) but adds upload time with no buyer-visible benefit.
- JPEG quality: 90% in Canva's download dialog. If the exported file is over 2MB, re-export at 85%. Below 80% produces visible compression artifacts at full zoom.
- Color space: RGB. Canva exports RGB by default. Never export as CMYK for Etsy — the color shift will make the Deep Forest Green look brown on screen.
- DPI: 72 DPI (screen use). Canva sets this automatically for non-print exports.

**How to export from Canva at exactly 2400×2400px**:
1. With your design open: click "Resize" in the top navigation bar.
2. Enter Custom Size: 2400 × 2400 px.
3. Click "Resize" — this creates a new copy of the design at the new dimensions. Do not use this resized copy as your working master — it will have stretched or repositioned elements if your original design was not square.
4. Download > JPEG > 90% quality.
5. Rename the file immediately after download.

Alternatively: build all lifestyle image templates at 2400×2400px from the start (as specified in SW-Master-FlatLay at 2400×2400). This eliminates the resize step.

### File naming for Etsy
Etsy does not display filenames to buyers, but the filename becomes part of the image's URL in Etsy's CDN — consistent naming makes troubleshooting easier when a listing's image needs to be replaced.
```
[product-slug]-slot4.jpg    (lifestyle / flat-lay, Etsy slot 4)
[product-slug]-slot5.jpg    (in-use / contextual, Etsy slot 5)
```
Full slug list in CANVA_EXECUTION_PLAYBOOK.md Section 6.1.

### Etsy upload workflow
Etsy allows up to 10 images per listing. Slots 1–3 are complete (mockups from Phase 1). Slots 4 and 5 are added in this phase.

1. Open Etsy Shop Manager.
2. Navigate to Listings > select the listing by name.
3. Click "Edit."
4. Scroll to the Photos section. Drag the new images into slots 4 and 5 in the correct order.
5. Slot 4 = lifestyle flat-lay. Slot 5 = in-use contextual. Etsy displays images in the order they are arranged in the listing editor — drag to confirm position.
6. Click "Save draft." The image update takes effect immediately on published listings.
7. After saving: open the listing in a browser tab to confirm the images appear in the correct slots.

**Etsy thumbnail rendering** (important for upload verification):
Etsy displays slot 1 as the primary search thumbnail, but the photo thumbnails in the listing scroll gallery pull from slots 1–10 in order. If your lifestyle image has important detail in the center of the frame, it may be cropped by Etsy's thumbnail generator. Verify each image at its actual thumbnail size by viewing the listing in Etsy search results and confirming the product is visible in the thumbnail.

### Known failure modes — Canva to Etsy
- **Failure mode 1**: Exporting at 1280×960px (the Canva design size) instead of 2400×2400px. Etsy will accept it but the image will appear pixelated at full zoom. Always resize to 2400×2400 before export.
- **Failure mode 2**: Uploading a PNG with a transparent background to Etsy. Etsy's image processor fills transparency with white, which may conflict with cream or parchment backgrounds. Export as JPEG to avoid this — JPEG does not support transparency, so the background is always filled.
- **Failure mode 3**: File size over 20MB. This rarely occurs with JPEG at 2400×2400 but can happen with PNG. Etsy's uploader times out on files over 20MB. Always check file size before uploading.
- **Failure mode 4**: Uploading to the wrong slot. Etsy's drag-and-drop slot interface is easy to misorder. After uploading, view the listing and confirm the correct image is in each position.

---

## 3. Canva → Social Media (Instagram, TikTok, Pinterest)

### Platform-specific image specifications
Each platform renders images at different aspect ratios. The same 2400×2400 Etsy image requires a platform-specific crop or resize for social use.

| Platform | Format | Aspect Ratio | Recommended Size | Notes |
|---|---|---|---|---|
| Instagram Feed Post | JPEG or PNG | 1:1 (square) | 1080×1080px | 2400×2400 scales down without cropping |
| Instagram Reel / Story | MP4 or JPEG | 9:16 (vertical) | 1080×1920px | Canva has an Instagram Story template at this size |
| Instagram Carousel | JPEG | 1:1 per slide | 1080×1080px | Up to 10 slides; first slide is the cover |
| TikTok | MP4 | 9:16 | 1080×1920px | Videos only; no static image posts indexed by algorithm |
| Pinterest Static Pin | JPEG or PNG | 2:3 | 1000×1500px | Taller pins take more feed real estate; max 1500px tall |
| Pinterest Idea Pin | MP4 or JPEG | 9:16 | 1080×1920px | Multi-page format; first frame is the cover |

### How to build platform-specific crops from the Etsy master in Canva
Do not build separate designs from scratch for each platform. Use the following workflow to derive all platform variants from the Etsy master:

1. Open the 2400×2400 Etsy export in Canva: Uploads > upload the JPEG > open as new design.
2. Use Canva's Resize feature to create variants:
   - Instagram/Pinterest square: already 1:1 — download at 1080×1080.
   - Pinterest Pin: Resize to 1000×1500. Reposition the image so the product and key props are in the center-upper portion (Pinterest crops from the bottom in some feed contexts). Add a text overlay with the zone name or product category if desired — Pinterest SEO benefits from text on pins.
   - Instagram Story/TikTok thumbnail: Resize to 1080×1920. The square product image becomes a center element — add a Deep Forest Green background behind it if the image does not fill the vertical space.

### Metadata preservation
Canva does not strip EXIF metadata from exported images. Instagram reads GPS coordinates from EXIF if present — this is not a privacy concern for product photos but is worth noting if any lifestyle photos were shot on a phone with location services enabled.

To strip EXIF data before upload: run the file through Squoosh (squoosh.app) at 95% quality — Squoosh strips all EXIF on export. This is optional for Seedwarden's use case but eliminates any metadata leakage.

### Scheduling via Buffer or Later
Buffer and Later both accept direct image uploads and schedule posts to Instagram, Pinterest, and TikTok from a single queue.

**Buffer setup**:
- Connect Instagram Business Account, Pinterest Business Account, and TikTok Creator Account.
- Each platform requires separate OAuth authorization — complete this setup at least 48 hours before launch day to allow time to resolve any connection errors.
- Buffer's free plan allows 3 connected channels and 10 scheduled posts per channel. This is sufficient for the launch window.

**Image sizing in Buffer**:
- Buffer displays a preview of how the image will render on each platform when scheduling. Review the preview before confirming the schedule. If the platform preview shows the product being cut off, adjust the crop in Canva before re-uploading.
- Buffer does not resize images automatically for each platform — you must upload the correctly-sized image for each platform separately.

### Known failure modes — Canva to Social Media
- **Failure mode 1**: Uploading a 2400×2400 image to Pinterest without cropping to 2:3. Pinterest crops square images to fit its vertical feed format, often cutting off the product. Always resize to 1000×1500 before uploading to Pinterest.
- **Failure mode 2**: TikTok does not support static image posts in the same way Instagram does. TikTok "photo mode" posts exist but do not receive the same algorithmic distribution as videos. For TikTok, use a 9:16 vertical video. Canva's video export can create a simple Ken Burns-style animation from a static image — this qualifies as a video for TikTok's algorithm.
- **Failure mode 3**: Buffer's connection to Instagram or TikTok expires. OAuth tokens for social platforms expire periodically. Re-authorize each connection before scheduling launch posts. Check the connection status in Buffer > Settings > Connected Accounts on Day 27.
- **Failure mode 4**: Instagram Reels thumbnail selection. When uploading a Reel, Instagram allows you to select a thumbnail frame. If using a Canva-exported video, the first frame is often a black title card — select a frame that shows the product before confirming the upload.

---

## 4. Kit → Email Sending

### Authentication checklist (required for inbox delivery)
Email deliverability depends on three DNS records being correctly set before the first send:

| Record Type | Required Value | Where to Set | Verification |
|---|---|---|---|
| SPF | `v=spf1 include:sendgrid.net ~all` | DNS TXT record on your domain | Kit Settings > Email Settings shows green checkmark |
| DKIM | CNAME record provided by Kit | DNS CNAME record on your domain | Kit Settings > Email Settings shows green checkmark |
| From Address | wanka95@gmail.com or custom domain | Kit Settings > Sender Email | Shows in all sent emails as the "From" address |

**If using Gmail as the sender address**: Gmail's DMARC policy can cause alignment failures with Kit's DKIM signing. If open rates are unexpectedly low (below 15%) in the first two weeks, switch to a custom domain email address. Free option: create a Zoho Mail account at zoho.com with a custom domain — Zoho's free plan supports one custom domain email with DKIM/SPF/DMARC configuration.

**Segment configuration for broadcasts**:
Broadcast emails (the May 30 launch email) should be sent to "All Confirmed Subscribers." In Kit: Broadcasts > New Broadcast > "Send to" > All Confirmed Subscribers. This sends to all subscribers who have confirmed their email address via the double opt-in process (or who signed up before double opt-in was enabled).

Do NOT send to "All Subscribers" — this includes unconfirmed addresses and dramatically increases bounce rates, which damages sender reputation.

### Tracking pixel setup
Kit inserts an open-tracking pixel automatically. You cannot disable this without affecting Kit's analytics. Tracking pixel behavior:
- Apple's Mail Privacy Protection (MPP, iOS 15+) pre-loads tracking pixels regardless of whether the subscriber opens the email. This inflates Kit's reported open rate by 20–40% for iOS users.
- Kit's open rate for Seedwarden's audience should be interpreted with this caveat. Click rate is more reliable than open rate for measuring true engagement.
- No action required — Kit handles this automatically. Just interpret open rates with the MPP inflation caveat when making decisions.

### Unsubscribe compliance
Kit inserts an unsubscribe link in every broadcast and sequence email automatically. Do not remove it. Do not hide it in small gray text. The unsubscribe link is legally required under CAN-SPAM (US) and GDPR (EU).

- Kit's default unsubscribe link text: "Unsubscribe." This is compliant.
- Adding context above the unsubscribe link is optional but reduces unsubscribe rates: "If this isn't useful, unsubscribe here — no hard feelings."
- Subscribers who click unsubscribe are removed from all sequences and broadcasts automatically by Kit.

---

## 5. Kit → Analytics and Revenue Attribution

### Conversion tracking setup
Kit's built-in analytics tracks opens, clicks, unsubscribes, and sequence completion rates. It does not natively track revenue attribution (which email led to which Etsy purchase). Revenue attribution requires a manual workflow.

**UTM parameter setup for Etsy links in Kit emails**:
Add UTM parameters to all Etsy product links embedded in Kit emails. UTM parameters allow Google Analytics (if enabled on your Etsy store via the GA4 integration in etsy-ga4-event-tracking.md) to attribute purchases to specific emails.

Required format:
```
https://www.etsy.com/listing/[LISTING-ID]/[SLUG]?utm_source=kit&utm_medium=email&utm_campaign=welcome-sequence&utm_content=email3-seed-saving-link
```

UTM parameters to use:
- `utm_source=kit` — identifies Kit as the traffic source
- `utm_medium=email` — identifies the channel as email
- `utm_campaign=welcome-sequence` or `utm_campaign=launch-broadcast` — identifies which campaign
- `utm_content=email1-zone5-download` — identifies the specific link within the email

Build these UTM-tagged URLs in Google's Campaign URL Builder (ga-dev-tools.google.com/campaign-url-builder) and paste them into Kit's email editor. Note: UTM-tagged URLs look long and ugly — use Kit's link button element rather than showing the raw URL in email text.

**Zone-specific revenue attribution**:
To attribute revenue by zone (which zones convert to buyers at higher rates):
- In Kit, navigate to Subscribers > filter by tag "zone-5." Export the subscriber list. Cross-reference with Etsy orders using the buyer's email address (if available) or by correlating purchase timing with email send timing.
- Kit does not integrate directly with Etsy for purchase event tracking. The attribution is manual at this stage. Record zone-level conversion observations in customer-analytics.csv.
- Phase 3 improvement: integrate Etsy with GA4 and use the custom dimension "subscriber_zone" (set via UTM parameters) to track zone-level conversion rates automatically.

**LTV measurement**:
Kit's subscriber view shows individual subscriber click history, sequence position, and tags. For repeat buyers, manually update the `etsy-buyer` tag and note purchase count in a custom field (if using Kit paid tier) or in customer-analytics.csv.

### Sequence performance benchmarks
Target metrics for the Seedwarden welcome sequence at launch:

| Email | Target Open Rate | Target Click Rate | Action if Below Target |
|---|---|---|---|
| Email 1 | 60%+ | 40%+ (download link) | If below 40% click: test subject line, verify download link works |
| Email 2 | 45%+ | 10%+ | If below 10%: subject line test in next broadcast |
| Email 3 | 40%+ | 15%+ | Most important signal. Below 15% click = low-intent list |
| Email 4 | 35%+ | 20%+ (any link) | Below 20%: rewrite the three segmentation link anchors |
| Email 5 | 35%+ | 8%+ (coupon use) | Below 8%: adjust coupon framing, not the discount amount |

---

## Tool-Switching Checklist — Complete Cross-Platform QA

Run this checklist in sequence before going live. Each line is a specific verification step, not a general category.

**Canva to Google Drive**:
- [ ] All 8 zone card PDFs exported at PDF Print quality
- [ ] All 8 PDFs uploaded to "Seedwarden Zone Cards — Live" Google Drive folder
- [ ] All 8 PDFs have sharing set to "Anyone with the link can view" (confirmed by opening each URL in incognito)
- [ ] All 8 direct download URLs use the `uc?export=download&id=` format
- [ ] Each URL saved in local "Phase 2 Live URLs" note with zone number label

**Google Drive to Kit**:
- [ ] All 8 zone-specific download URLs pasted into correct Email 1 variants in Kit
- [ ] Each link tested by clicking "Preview" in Kit's email editor and confirming the URL resolves correctly
- [ ] Email header image (600×200px PNG) uploaded to Kit
- [ ] Alt text set for email header image: "Seedwarden — Zone Quick-Start Cards"

**Kit to subscribers**:
- [ ] SPF and DKIM records showing green in Kit Settings > Email Settings
- [ ] End-to-end test completed (sign up via landing page, receive Email 1 with working download link)
- [ ] SEEDWARDEN15 coupon confirmed active in Etsy
- [ ] All Etsy product links in emails use UTM parameters
- [ ] Broadcast email staged and showing "Scheduled" status for May 30 12:00pm

**Canva to Etsy**:
- [ ] All 42 lifestyle images exported at 2400×2400px JPEG 90%
- [ ] All files under 2MB
- [ ] All 21 products updated with slot 4 and slot 5 images
- [ ] Each listing verified in browser — images visible in correct slots
- [ ] No thumbnail cropping that obscures the product title or primary graphic

**Canva to Social (Buffer/Later)**:
- [ ] Instagram post image: 1080×1080px JPEG, product visible at thumbnail size
- [ ] Pinterest pin: 1000×1500px JPEG, product in upper two-thirds, text overlay with zone keyword
- [ ] TikTok content: 9:16 video or Canva-animated image, not a static square
- [ ] All three posts scheduled in Buffer/Later, showing "Scheduled" status
- [ ] Buffer connections to all three platforms verified active within last 7 days
