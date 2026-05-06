---
title: "Phase 2 Tool Integration Map — Workflow Diagram and API Integrations"
date: 2026-05-06
status: production-ready
references:
  - tool-integration-map.md (detailed per-handoff failure modes)
  - KIT_SETUP_NOTES.md
  - kit-account-setup-guide.md
  - CANVA_EXECUTION_PLAYBOOK.md
  - etsy-ga4-event-tracking.md
---

# Phase 2 Tool Integration Map
## Workflow Diagram, Data Flow, and Integration Checklist

**Purpose**: Shows how every tool in Phase 2 connects to every other tool, what format the output takes at each handoff, which handoffs have API automation behind them, and where the human-in-the-loop steps occur.

---

## Master Workflow Diagram

```
USER ACTIONS + CONTENT CREATION
         |
         v
+------------------+     PDF Print quality        +------------------+
|     CANVA        |----------------------------->|   GOOGLE DRIVE   |
|  (design tool)   |     zone-[N]-quick-start-    |  (file hosting)  |
|                  |     card.pdf                 |                  |
| - Zone cards (8) |     600x200px PNG header     | Folder: "Seedwarden|
| - Etsy lifestyle |                               | Zone Cards — Live"|
|   images (42)    |<-----------------------------| Sharing: Anyone  |
| - Social images  |     (no return flow)         | with the link    |
| - Email header   |                               |                  |
+------------------+                               +------------------+
         |                                                  |
         | JPEG 2400x2400px                                 | ?export=download&id=
         | (per-product naming)                             | (direct DL URLs, x8)
         |                                                  |
         v                                                  v
+------------------+                               +------------------+
|   ETSY SHOP      |                               |      KIT         |
|  MANAGER         |  <-- ETSY API (one-way) ---   | (email platform) |
|                  |      (product data pull)      |                  |
| - 21 listings    |                               | - Landing page   |
| - Slots 1-3:     |  Coupon: SEEDWARDEN15         | - Welcome seq.   |
|   mockups (done) |  (manually created in Etsy,   |   Emails 1-5     |
| - Slots 4-5:     |   referenced in Kit Email 5)  | - Broadcast      |
|   lifestyle JPEGs|                               | - Automation     |
|                  |  UTM links from Kit emails    | - Segmentation   |
| - GA4 pixel      |  -> Etsy -> GA4 conversion    |   tags (15)      |
|   (if active)    |     tracking                  |                  |
+------------------+                               +------------------+
         |                                                  |
         | Organic + email traffic                          | Email sends
         |                                                  | (Zone-conditional)
         v                                                  v
+------------------+     Zapier/IFTTT               +------------------+
|  SOCIAL MEDIA    |     (optional automation)      |   SUBSCRIBER     |
|                  |<-- new Etsy sale trigger       |   INBOX          |
| - Instagram      |    -> post "sold" content      |                  |
|   Business       |                                | Email 1: Zone card|
| - TikTok         |                                |   DL link        |
|   Business       |                                | Email 2: Day 2   |
| - Pinterest      |                                | Email 3: Day 5   |
|   Business       |                                | Email 4: Day 7   |
|                  |                                | Email 5: Day 10  |
+------------------+                                |   (SEEDWARDEN15) |
         ^                                          +------------------+
         |                                                  |
         | Scheduled posts                                  | Click behavior
         | (pre-loaded)                                     | (behavioral tags)
         |                                                  v
+------------------+                               +------------------+
|  BUFFER / LATER  |                               |  SEGMENTATION    |
| (scheduler)      |                               |                  |
|                  |                               | seed-saver       |
| Instagram: 1080  |                               | city-grower      |
| TikTok: 9:16 MP4 |                               | preservationist  |
| Pinterest: 1000x |                               | unclassified     |
|   1500px         |                               |                  |
| Posts pre-loaded |                               | -> Future product|
| for May 30 2-4pm |                               |   spotlights     |
+------------------+                               +------------------+
                                                           |
                                                           | Manual cross-ref
                                                           v
                                                  +------------------+
                                                  | ANALYTICS        |
                                                  |                  |
                                                  | GA4 (via Etsy)   |
                                                  | Kit click data   |
                                                  | customer-        |
                                                  |   analytics.csv  |
                                                  | (manual LTV log) |
                                                  +------------------+
```

---

## Data Flow: Output-to-Input Per Tool Pair

### 1. Canva → Google Drive

**What moves**: 8 zone card PDFs + 1 email header PNG.

**Format at handoff**:
- Zone cards: PDF Print quality, 300 DPI equivalent, RGB color space, 1-4MB per file.
- Email header: PNG, 600×200px, under 200KB.

**Naming at handoff**:
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

**Human step required**: Yes. Canva does not push files to Google Drive automatically. User downloads from Canva, uploads to Drive, sets sharing permissions.

**Sharing permission required**: "Anyone with the link can view" (not Restricted, which is the default).

**URL format for next step** (critical — wrong format breaks subscriber delivery):
```
https://drive.google.com/uc?export=download&id=[FILE-ID]
```
Not: `https://drive.google.com/file/d/[ID]/view` (this opens a viewer, not a download).

---

### 2. Google Drive → Kit Email Editor

**What moves**: 8 zone card download URLs (the `?export=download&id=` format URLs).

**Format at handoff**: Plain text URLs pasted into Kit's link editor for each Email 1 zone variant.

**Human step required**: Yes. Kit does not pull from Drive automatically.

**Embedding method in Kit**: Hyperlinked button block (Deep Forest Green #143b28 background, Warm Cream #F5EDD6 text, full-width for mobile). NOT an email attachment.

**API status**: No API. Manual URL paste per zone variant.

**Verification step**: After pasting, click "Preview" in Kit's email editor and confirm the full URL including the `?export=download` parameter was accepted and not stripped.

---

### 3. Canva → Etsy (lifestyle images)

**What moves**: 42 lifestyle JPEGs (21 products × 2 slots each).

**Format at handoff**:
- JPEG, 2400×2400px, 90% quality, <2MB each.
- Naming: `[product-slug]-slot4.jpg`, `[product-slug]-slot5.jpg`.

**Human step required**: Yes. Etsy has no API for image upload from Canva.

**Upload workflow**: Etsy Shop Manager → Listings → Edit → Photos section → drag to slots 4 and 5 → Save.

**Verification after upload**: Open listing in public browser (not Shop Manager). Confirm images appear in the correct slot order and are not cropped at the thumbnail level.

---

### 4. Canva → Social Media (via Buffer/Later)

**What moves**: Platform-specific crops of lifestyle images.

**Formats at handoff**:
| Platform | Size | Format |
|---|---|---|
| Instagram feed | 1080×1080px | JPEG |
| Instagram Reel/Story | 1080×1920px | MP4 or JPEG |
| TikTok | 1080×1920px | MP4 (video required for algorithm) |
| Pinterest static pin | 1000×1500px | JPEG |
| Pinterest Idea Pin | 1080×1920px | MP4 or JPEG |

**Human step required**: Yes. Buffer/Later requires manual upload and schedule configuration.

**API status**: Buffer connects to Instagram, TikTok, and Pinterest via OAuth. Authorize each connection at least 48 hours before launch day. Buffer's free plan supports 3 channels and 10 scheduled posts per channel.

**Verification step**: Click "Preview" on each scheduled post in Buffer/Later to confirm image is attached and crops correctly for the platform's feed view.

---

### 5. Kit → Subscriber Inboxes

**What moves**: Zone card delivery emails, welcome sequence, launch broadcast.

**API status**: Full automation. Kit sends automatically on triggers and schedule.

**Authentication requirements** (must be set before first send or deliverability degrades):
| DNS Record | Value | Location |
|---|---|---|
| SPF | `v=spf1 include:sendgrid.net ~all` | Domain DNS TXT record |
| DKIM | CNAME provided by Kit | Domain DNS CNAME |

**Verification**: Kit Settings > Email Settings shows green checkmark for both records.

**Broadcast segmentation**: Send to "All Confirmed Subscribers" — NOT "All Subscribers" (includes unconfirmed; damages sender reputation).

**Human step required for broadcast**: Yes. Broadcast must be manually staged and scheduled. It does not send automatically.

---

### 6. Kit → Etsy Revenue Attribution (manual workflow)

**What moves**: UTM parameters embedded in Etsy product links within Kit emails.

**Format at handoff**:
```
https://www.etsy.com/listing/[ID]/[slug]?utm_source=kit&utm_medium=email&utm_campaign=welcome-sequence&utm_content=email3-seed-saving-link
```

**API status**: No direct API between Kit and Etsy. Attribution is manual via GA4 cross-reference (if Etsy GA4 pixel is active, documented in `etsy-ga4-event-tracking.md`). Zone-level attribution logged manually in `customer-analytics.csv`.

**Build tool**: Use Google's Campaign URL Builder (ga-dev-tools.google.com/campaign-url-builder) to generate UTM-tagged URLs. Paste into Kit email editor as hyperlinked button elements.

---

### 7. Etsy → Kit (Etsy API — product data)

**What moves**: New Etsy product data (listing ID, title, price) pulled by Kit for product spotlights.

**API status**: Kit has a native Etsy API integration (beta as of 2026). Go to Kit > Integrations > Etsy. Connects the Etsy store to Kit and can trigger emails when new products are published.

**Phase 2 use case**: Optional. The welcome sequence and launch broadcast are hand-coded. The Etsy API integration is primarily useful for Phase 3 automation (auto-emails when new listings go live).

**Human step**: One-time setup. Kit Integrations → Etsy → Authorize. Confirm Etsy store URL matches the store that holds the Phase 2 listings.

---

### 8. Zapier/IFTTT → Social (optional automation)

**What moves**: New Etsy sale event → social media "sold" post or counter update.

**API status**: Zapier has Etsy trigger support. Trigger: "New Sale on Etsy." Action: post to Instagram, TikTok, or Pinterest.

**Phase 2 use case**: Nice-to-have. Creates social proof content automatically. Not required for launch.

**Setup time**: 30-45 minutes for a working Zap. Free Zapier plan supports 5 Zaps and 100 tasks/month — sufficient for Phase 2 scale.

**Risk**: Zapier Etsy integration may require a paid Etsy Pattern subscription or Etsy API developer key. Check Etsy API terms before configuring. If Zapier is unavailable: manually post sales milestones to social (e.g., "5 zone card subscribers this week") as an alternative.

---

## Handoff Points and Bottlenecks

### Handoff 1: Zone Card Export (Day ~19)

**Location in workflow**: Canva → Google Drive → Kit email editor.

**Bottleneck risk**: High. This is a three-step human handoff. Each step has a distinct failure mode (wrong export format, wrong sharing permission, wrong URL format). The failure is invisible until a subscriber tries to download their zone card and gets a "request access" page or a viewer instead of a download.

**Mitigation**: Test all 8 URLs in incognito before loading into Kit. This is non-negotiable.

---

### Handoff 2: Kit Broadcast Staging (Day ~27)

**Location in workflow**: Kit → scheduled send at May 30 12pm.

**Bottleneck risk**: Medium. The broadcast must be manually staged; Kit does not automatically convert a draft to a scheduled send. A broadcast left as "Draft" silently does not send.

**Mitigation**: Verify broadcast shows "Scheduled" status after staging. Re-verify on May 29.

---

### Handoff 3: Buffer/Later OAuth Token Expiry (Day ~28)

**Location in workflow**: Buffer → Instagram/TikTok/Pinterest.

**Bottleneck risk**: Medium. OAuth connections to social platforms expire periodically and silently. A scheduled post with an expired connection shows as "Failed" at send time with no advance warning.

**Mitigation**: Re-authorize all three Buffer connections on May 28 (two days before launch). Takes 5 minutes per platform.

---

### Handoff 4: Etsy Coupon Confirmation (Day ~21)

**Location in workflow**: Etsy coupon → Kit Email 5 → subscriber purchase.

**Bottleneck risk**: Low risk of technical failure; high risk of timing gap. Email 5 goes to the subscriber 10 days after they sign up. If the coupon is created after the first subscriber's Email 5 date, that subscriber gets a broken coupon.

**Mitigation**: Create the SEEDWARDEN15 coupon in Etsy by May 20 (10 days before the first potential Email 5 delivery window).

---

## API Integrations Summary

| Integration | Type | Phase 2 Status | Notes |
|---|---|---|---|
| Kit → Email delivery | Automated (Kit native) | Required | SPF/DKIM DNS setup required before first send |
| Kit → Zone routing | Automated (Kit automation) | Required | Conditional logic on zone dropdown field |
| Buffer → Instagram | OAuth API | Required | Re-authorize May 28 |
| Buffer → TikTok | OAuth API | Required | Re-authorize May 28 |
| Buffer → Pinterest | OAuth API | Required | Re-authorize May 28 |
| Etsy → Kit | Kit native Etsy API (beta) | Optional (Phase 3) | Not needed for Phase 2 manual sequences |
| Etsy → GA4 | Etsy GA4 pixel | Optional | Configured per `etsy-ga4-event-tracking.md` |
| Zapier → social | Zapier Etsy trigger | Optional | Sales milestone social automation |
| Canva → Drive | None (manual export) | Manual | Per-PDF download and upload |
| Drive → Kit | None (URL paste) | Manual | Per-zone URL paste into email editor |

---

## Tool Integration QA Checklist

Run this checklist on May 27-28 before the final pre-launch window.

**Canva → Google Drive**:
- [ ] All 8 zone card PDFs exported at PDF Print quality (not PDF Standard)
- [ ] All 8 PDFs named with the standard `zone-[N]-quick-start-card.pdf` convention
- [ ] All 8 PDFs uploaded to "Seedwarden Zone Cards — Live" Google Drive folder
- [ ] All 8 files have sharing set to "Anyone with the link can view"
- [ ] All 8 direct download URLs use the `uc?export=download&id=` format
- [ ] All 8 URLs tested in incognito — download dialog appears (not viewer or access request)
- [ ] All 8 URLs logged in WORKLOG.md by zone number

**Google Drive → Kit**:
- [ ] Zone 3 download URL pasted into Kit Email 1 Zone 3 variant
- [ ] Zone 4 download URL pasted into Kit Email 1 Zone 4 variant
- [ ] Zone 5 download URL pasted into Kit Email 1 Zone 5 variant
- [ ] Zone 6 download URL pasted into Kit Email 1 Zone 6 variant
- [ ] Zone 7 download URL pasted into Kit Email 1 Zone 7 variant
- [ ] Zone 8 download URL pasted into Kit Email 1 Zone 8 variant
- [ ] Zone 9 download URL pasted into Kit Email 1 Zone 9 variant
- [ ] Zone 10 download URL pasted into Kit Email 1 Zone 10 variant
- [ ] All 8 zone variants previewed in Kit — link resolves to download

**Kit → Email delivery**:
- [ ] SPF record active (Kit Settings shows green)
- [ ] DKIM record active (Kit Settings shows green)
- [ ] End-to-end test completed for Zone 5 (email received, download works)
- [ ] End-to-end test completed for one other zone (Zone 7 or 3)
- [ ] SEEDWARDEN15 coupon active in Etsy (checked in Etsy > Marketing > Coupons)
- [ ] All Etsy URLs in Email 3 and Email 4 are UTM-tagged
- [ ] Launch broadcast staged and showing "Scheduled" for May 30 12pm

**Canva → Etsy**:
- [ ] All 42 lifestyle images exported at 2400×2400px JPEG 90%
- [ ] All files under 2MB (batch check before uploading)
- [ ] All 21 Etsy products updated with slot 4 and slot 5 images
- [ ] All 21 listings verified in public browser — images in correct slot order

**Canva → Social (Buffer/Later)**:
- [ ] Instagram post image: 1080×1080px JPEG, product visible at thumbnail size
- [ ] Pinterest pin: 1000×1500px JPEG, product in upper two-thirds
- [ ] TikTok: 9:16 video file (not a static image)
- [ ] All three launch posts scheduled in Buffer/Later, showing "Scheduled" status
- [ ] Buffer OAuth connections re-authorized within last 2 days

---

*Generated: 2026-05-06. Extends tool-integration-map.md (per-handoff failure modes) with workflow diagram, API status, and launch integration checklist.*
