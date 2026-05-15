---
title: "Track B — Gate Completion Verification Checklist"
created: 2026-05-15
launch-date: 2026-05-30
days-remaining: 15
status: VERIFICATION FRAMEWORK — execute May 15-29
scope: >
  Three user-action gates (social accounts, Canva Brand Kit, Kit email automation)
  with detailed verification checklists, pass/fail criteria, dependency matrix,
  May 29 go/no-go decision procedure, and failure escalation paths.
references:
  - TRACK_B_USER_GATES.md (procedural execution steps)
  - PHASE_2_GO_NO_GO_DASHBOARD.md (launch-day coordination framework)
  - PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md (GA4 tracking code requirement)
---

# Track B — Gate Completion Verification Checklist

**Purpose**: Did you execute the gates correctly? This document is your verification script.
Assume you have already completed the gates per TRACK_B_USER_GATES.md. Your job now is to
confirm each one meets production-ready criteria.

**Who should read this**: User executing Gates 1–3 (May 15–28). Use May 29 evening to run
the full go/no-go verification before May 30 launch.

**Total time estimate**: 3–4 hours (verification only; not counting gate execution)
- Gate 1 verification: 30 minutes
- Gate 2 verification: 25 minutes
- Gate 3 verification: 35 minutes
- Dependency matrix review: 10 minutes
- May 29 go/no-go decision: 30 minutes

**Critical dates**:
- Gate 1 completion: May 18 deadline
- Gate 2 completion: May 24 deadline
- Gate 3 completion: May 28 deadline
- Gate 1 verification: May 19–25
- Gate 2 verification: May 25–28
- Gate 3 verification: May 28–29 evening
- Final go/no-go decision: May 29 20:00 UTC

---

## Gate 1: Social Media Account Verification (30 minutes)

**Scope**: Instagram, TikTok, Pinterest accounts created with correct bio, profile image, and business account type.

**Reference**: TRACK_B_USER_GATES.md "Gate 1: Social Media Account Setup"

### Gate 1 Verification Checklist

#### Instagram Account Verification (10 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Handle claimed correctly | Account exists at instagram.com/[handle]; handle is `seedwarden` or `seedwarden.co` or `seedwarden.seeds` | [ ] PASS [ ] FAIL | Check if your chosen fallback was needed |
| 2 | Business account type | Profile > Settings > Account > Account Type shows "Professional (Business)" | [ ] PASS [ ] FAIL | Not a personal account; business is required |
| 3 | Profile photo uploaded | Profile photo displays the Seedwarden logo (`seedwarden_logo_1.png`) clearly | [ ] PASS [ ] FAIL | Logo must be visible at small thumbnail size |
| 4 | Display name correct | Name field shows exactly "Seedwarden" (not "Seedwarden Official" or other variant) | [ ] PASS [ ] FAIL | Consistency across platforms |
| 5 | Bio text matches spec | Bio contains all required elements: "Field guides for growers, foragers + food preservers. Heirloom seeds. Wild edibles. Real food skills. Zone-specific free card below" | [ ] PASS [ ] FAIL | Exactly 150 characters max; must include "zone-specific free card" |
| 6 | Bio text includes location reference | Bio mentions location context (implicit via "field guides") OR includes geographic zone reference | [ ] PASS [ ] FAIL | Optional but recommended per spec |
| 7 | Link in bio configured | If Kit landing page URL is ready: bio contains Kit URL in link-in-bio. If Gate 3 not complete: link field blank or placeholder | [ ] PASS [ ] FAIL | Update this on May 28 after Gate 3 complete |
| 8 | Email contact button enabled | Edit Profile > Contact Options > Show Email Contact Button is ON; email is wanka95@gmail.com | [ ] PASS [ ] FAIL | Allows DMs about product inquiries |

**Gate 1A Status** (Instagram):
```
Verification timestamp: ___
Instagram handle claimed: ___
URL: instagram.com/___
Overall Instagram: [ ] PASS [ ] FAIL — If FAIL, note which steps failed: ___
```

---

#### TikTok Account Verification (10 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Handle claimed correctly | Account exists at tiktok.com/@[handle]; handle is `seedwarden` or `seedwarden.co` or `seedwarden.seeds` | [ ] PASS [ ] FAIL | Consistent with Instagram handle |
| 2 | Business account type | Profile > Settings and Privacy > Account > Account Type shows "Business"; Category is "Agriculture" or "Education" | [ ] PASS [ ] FAIL | Business category required for insights |
| 3 | Profile photo uploaded | Profile displays Seedwarden logo; thumbnail is clear at small size | [ ] PASS [ ] FAIL | Same logo as Instagram and Pinterest |
| 4 | Display name correct | Name field shows "Seedwarden" | [ ] PASS [ ] FAIL | Not a variant |
| 5 | Bio text matches spec | Bio contains: "Field guides for growers + foragers\nFree zone card in bio" (80 char max, may use line break) | [ ] PASS [ ] FAIL | Shorter than Instagram due to TikTok limits |
| 6 | Link in bio configured | If Kit ready: bio contains Kit URL. If not: blank or placeholder. DO NOT link to Instagram (avoids ping-pong) | [ ] PASS [ ] FAIL | Update May 28 after Gate 3 complete |
| 7 | Email verified | Profile > Account > Email shows wanka95@gmail.com is confirmed/verified | [ ] PASS [ ] FAIL | Required for business account features |
| 8 | Native upload capability confirmed | Verified you can upload video natively (not cross-posting from Instagram). Test: upload a 15-second video OR verify Settings > Connections does not show "Instagram" as auto-cross-post target | [ ] PASS [ ] FAIL | Critical: cross-posted TikToks are algorithmically suppressed |

**Gate 1B Status** (TikTok):
```
Verification timestamp: ___
TikTok handle claimed: ___
URL: tiktok.com/@___
Overall TikTok: [ ] PASS [ ] FAIL — If FAIL, note which steps failed: ___
```

---

#### Pinterest Account Verification (10 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Handle claimed correctly | Account exists at pinterest.com/[handle]; handle matches Instagram root (e.g., if Instagram is `seedwarden.co`, Pinterest should also be `seedwarden.co` or `seedwarden`) | [ ] PASS [ ] FAIL | All three platforms should share consistent handle |
| 2 | Business account type | Settings > Account Settings > Account Status shows "Business" (not Personal) | [ ] PASS [ ] FAIL | Required for analytics and scheduling |
| 3 | Profile photo uploaded | Displays Seedwarden logo; thumbnail is legible | [ ] PASS [ ] FAIL | Same logo as Instagram and TikTok |
| 4 | Display name correct | Name field shows "Seedwarden" | [ ] PASS [ ] FAIL | Consistency across platforms |
| 5 | About section matches spec | About text contains: "Seedwarden — heirloom seeds, wild edibles, food preservation + zone-specific growing guides. Practical field guides for real food growers." (160 char max) | [ ] PASS [ ] FAIL | Must include "zone-specific" and "practical field guides" |
| 6 | Website field configured | If Kit ready: website field contains Kit URL. If not: blank or "Coming Soon". Do NOT link to Etsy yet (confuses lead-magnet flow) | [ ] PASS [ ] FAIL | Update May 28 after Gate 3 complete |
| 7 | Email verified | Account > Email shows wanka95@gmail.com is confirmed | [ ] PASS [ ] FAIL | Required for business messaging |
| 8 | Business category set | Account > Business Category shows "Online Retailer" or "Media" | [ ] PASS [ ] FAIL | Allows access to analytics and promotion tools |

**Gate 1C Status** (Pinterest):
```
Verification timestamp: ___
Pinterest handle claimed: ___
URL: pinterest.com/___
Overall Pinterest: [ ] PASS [ ] FAIL — If FAIL, note which steps failed: ___
```

---

#### Cross-Platform Consistency Check (5 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Handle consistency | All three handles share the same root word (`seedwarden` or `seedwarden.co` or `seedwarden.seeds`) | [ ] PASS [ ] FAIL | Allows users to find you across platforms |
| 2 | Profile photo consistency | All three platform thumbnails display the SAME logo image (not different crops or versions) | [ ] PASS [ ] FAIL | Brand consistency |
| 3 | Bio consistency | All three bios mention "field guides" and "zone-specific" (language may vary per platform limits) | [ ] PASS [ ] FAIL | Consistent value proposition |
| 4 | Account type consistency | All three are Business (not Personal) accounts | [ ] PASS [ ] FAIL | Required for professional credibility |
| 5 | Email consistency | All three accounts are linked to wanka95@gmail.com | [ ] PASS [ ] FAIL | Single email ownership |

**Gate 1 Overall Status**:
```
Instagram: [ ] PASS [ ] FAIL
TikTok: [ ] PASS [ ] FAIL
Pinterest: [ ] PASS [ ] FAIL
Cross-platform: [ ] PASS [ ] FAIL

GATE 1 FINAL: [ ] PASS [ ] FAIL
If FAIL: which sub-gates failed? ___
Completion timestamp: ___
```

**Expected completion time**: 30 minutes

---

## Gate 2: Canva Brand Kit Verification (25 minutes)

**Scope**: Canva Brand Kit created with 10 colors, 3 fonts, logo uploaded, and export functions working.

**Reference**: TRACK_B_USER_GATES.md "Gate 2: Canva Brand Kit Configuration"

### Gate 2 Verification Checklist

#### Brand Kit Setup Verification (8 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Brand Kit exists | Log into canva.com > Brand Hub (left sidebar) > Find "Seedwarden" Brand Kit in the list | [ ] PASS [ ] FAIL | Brand Kit must be named exactly "Seedwarden" |
| 2 | Brand Kit is active | Click into Brand Kit > all sections (Colors, Fonts, Logos) are editable (not locked/archived) | [ ] PASS [ ] FAIL | Active status is required |
| 3 | Colors count correct | Click Colors section > count total colors. Should be 10 (6 brand + 4 zone bands) | [ ] PASS [ ] FAIL | Exact count required for zone card variants |
| 4 | Brand colors present | All 6 brand colors exist: Deep Forest Green (#143b28), Deep Ink Green (#1A3A2A), Warm Cream (#F5EDD6), Parchment (#EDE0C4), Sage (#8FA882), Burnt Sienna (#A0522D) | [ ] PASS [ ] FAIL | Verify by clicking each color and checking hex code |
| 5 | Zone band colors present | All 4 zone band colors exist: Cool (#3D6B8A), Temperate (#2D5016), Warm (#C9943A), Hot (#A0522D) | [ ] PASS [ ] FAIL | Hot band shares hex with Burnt Sienna but is a separate labeled entry |
| 6 | Fonts count correct | Click Fonts section > count total fonts. Should be 3 | [ ] PASS [ ] FAIL | Heading, Body, Accent |
| 7 | Fonts correct | All 3 fonts exist: Playfair Display (heading), Lato (body; or Source Sans 3 if Lato unavailable), Cormorant Garamond (accent) | [ ] PASS [ ] FAIL | Verify each font name is exact match |
| 8 | Logo uploaded | Click Logos section > at least 1 logo is visible with thumbnail preview | [ ] PASS [ ] FAIL | Should be `seedwarden_logo_1.png` |

**Gate 2A Status** (Brand Kit Contents):
```
Verification timestamp: ___
Brand Kit name: "Seedwarden"
Color count: ___ / 10
Font count: ___ / 3
Logo count: ___ / 1
Overall Brand Kit contents: [ ] PASS [ ] FAIL
```

---

#### Canva Export Test (12 minutes)

**Purpose**: Verify that the Canva Brand Kit is fully functional and can export production-ready assets.

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Create test design | Open Canva > "Create a design" > choose template "Pinterest Pin" (1000x1500 px) | [ ] PASS [ ] FAIL | Tests that Brand Kit integrates with design templates |
| 2 | Apply Brand Kit | While designing: click Brand Hub (or Brand Kit icon) > select "Seedwarden" Brand Kit > apply colors and fonts to the design | [ ] PASS [ ] FAIL | One-click brand application must work |
| 3 | Design preview | The design should instantly update with Brand Kit colors and fonts. Verify at least 2 colors and 1 font are visible in the design | [ ] PASS [ ] FAIL | Visual feedback that Brand Kit is active |
| 4 | Export as PNG | Download > Export > PNG > 300 DPI (for print quality zone cards) | [ ] PASS [ ] FAIL | PNG at 300 DPI is the standard for digital products |
| 5 | PNG exports without error | File downloads to computer. File size > 100 KB (proof of content). File opens in image viewer and displays correctly | [ ] PASS [ ] FAIL | No export dialog errors or blank files |
| 6 | Export as PDF | Download > Export > PDF (Print) | [ ] PASS [ ] FAIL | Some designs require PDF export (zone cards, guides) |
| 7 | PDF exports without error | File downloads to computer. File size > 100 KB. File opens in PDF reader and displays correctly | [ ] PASS [ ] FAIL | No export dialog errors or blank files |
| 8 | Export as video (optional) | Download > Export > Video (MP4) — if Canva video export is available | [ ] PASS [ ] FAIL | Optional; tests video capability for future social content |

**Gate 2B Status** (Export Functionality):
```
Verification timestamp: ___
Test design created: [ ] YES [ ] NO
Brand Kit applied successfully: [ ] YES [ ] NO
PNG 300 DPI export successful: [ ] YES [ ] NO
PDF export successful: [ ] YES [ ] NO
Overall export testing: [ ] PASS [ ] FAIL
```

---

#### Zone Card Export Test (5 minutes)

**Purpose**: If you have zone card templates already created in Canva (from CANVA_ZONE_CARD_BATCH_WORKFLOW.md),
verify that zone cards export correctly for email delivery.

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Zone card templates exist | Canva > search for "zone card" in your designs. At least 1 zone card template is visible | [ ] PASS [ ] FAIL | If no zone cards created yet, mark as CONDITIONAL and plan creation by May 28 |
| 2 | Zone card uses Brand Kit | Click into a zone card template > verify Brand Kit is applied (colors match, fonts match) | [ ] PASS [ ] FAIL | Consistency across all 8 zone variants |
| 3 | Zone card exports as PDF | Download zone card > Export > PDF (Print) | [ ] PASS [ ] FAIL | Zone cards must be PDF for email delivery |
| 4 | PDF is download-ready | PDF file opens in PDF reader, displays all content (map, color band, text), file size > 200 KB | [ ] PASS [ ] FAIL | Email attachments must be real files, not viewer pages |
| 5 | All 8 zones represented | Check Canva designs: do you have at least 8 different zone card templates (one per zone 3–10)? Or do you have a single template that can be customized? | [ ] PASS [ ] FAIL | 8 variations required for Kit email personalization |

**Gate 2C Status** (Zone Cards):
```
Verification timestamp: ___
Zone card templates exist: [ ] YES [ ] NO
Zone cards use Brand Kit: [ ] YES [ ] NO
Zone cards export as PDF: [ ] YES [ ] NO
All 8 zones represented: [ ] YES [ ] NO / [ ] CONDITIONAL (to be created by May 28)
Overall zone card status: [ ] PASS [ ] CONDITIONAL [ ] FAIL
```

---

#### Brand Kit Gallery Screenshot (2 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Take screenshot | Canva > Brand Hub > click "Seedwarden" Brand Kit > take a screenshot showing the Brand Kit overview page (colors, fonts, logo visible) | [ ] PASS [ ] FAIL | Proof that Brand Kit is live and configured |

**Gate 2 Overall Status**:
```
Brand Kit contents: [ ] PASS [ ] FAIL
Export functionality: [ ] PASS [ ] FAIL
Zone card verification: [ ] PASS [ ] CONDITIONAL [ ] FAIL
Screenshot captured: [ ] YES [ ] NO

GATE 2 FINAL: [ ] PASS [ ] CONDITIONAL [ ] FAIL
If CONDITIONAL: which items are pending? ___
If FAIL: which sub-gates failed? ___
Completion timestamp: ___
```

**Expected completion time**: 25 minutes

---

## Gate 3: Kit Email Account & Landing Page Verification (35 minutes)

**Scope**: Kit account created, 15 tags configured, 5-email sequence built, landing page live,
and 3-email delivery test passed.

**Reference**: TRACK_B_USER_GATES.md "Gate 3: Kit Email Account Setup"

### Gate 3 Verification Checklist

#### Kit Account Setup Verification (8 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Kit account created | Log into kit.co > dashboard loads. Sidebar shows account name "Seedwarden" | [ ] PASS [ ] FAIL | Account must be under wanka95@gmail.com |
| 2 | Account email verified | Kit > Account Settings > Email shows "wanka95@gmail.com — Verified" | [ ] PASS [ ] FAIL | Confirmation link must have been clicked in Gmail |
| 3 | Sender name correct | Kit > Account Settings > Sender Name shows "Seedwarden" | [ ] PASS [ ] FAIL | Emails will show "From: Seedwarden <wanka95@gmail.com>" |
| 4 | Sender email correct | Kit > Account Settings > Sender Email shows "wanka95@gmail.com" | [ ] PASS [ ] FAIL | Matches the wanka95 email requirement |
| 5 | Time zone set | Kit > Account Settings > Time Zone shows your local time zone (not UTC or default) | [ ] PASS [ ] FAIL | Automation triggers use this timezone |
| 6 | Business type set | Kit > Account Settings > Business Type shows "Creator" or "E-commerce" | [ ] PASS [ ] FAIL | Both are acceptable |

**Gate 3A Status** (Account Setup):
```
Verification timestamp: ___
Kit account name: Seedwarden
Account email: wanka95@gmail.com
Email verified: [ ] YES [ ] NO
Overall Kit account: [ ] PASS [ ] FAIL
```

---

#### Kit Tags Verification (5 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Zone tags all created | Kit > Subscribers > Tags > search for "zone-". All 8 tags should exist: zone-3, zone-4, zone-5, zone-6, zone-7, zone-8, zone-9, zone-10 | [ ] PASS [ ] FAIL | Exact names required; case-sensitive |
| 2 | Cohort tags all created | All 7 tags should exist: seed-saver, forager, food-preserver, homesteader, medicinal-herbs, vip-buyer, phase-1-buyer | [ ] PASS [ ] FAIL | These apply based on email behavior or survey responses |
| 3 | Tag count correct | Total tags in Kit > 15 (may have more, but these 15 must exist) | [ ] PASS [ ] FAIL | Verify by counting in the tag list or exporting |

**Gate 3B Status** (Tags):
```
Verification timestamp: ___
Zone tags (8): [ ] ALL PRESENT [ ] MISSING: ___
Cohort tags (7): [ ] ALL PRESENT [ ] MISSING: ___
GATE 3B FINAL: [ ] PASS [ ] FAIL
```

---

#### Kit Landing Page Verification (8 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Landing page created | Kit > Landing Pages > find a landing page named "Seedwarden" or similar | [ ] PASS [ ] FAIL | Template can be "Simple" or "Clean" (no custom code needed) |
| 2 | Landing page is published | Kit > Landing Pages > click the landing page > Status shows "Published" (not Draft) | [ ] PASS [ ] FAIL | Only published pages are accessible via URL |
| 3 | Landing page URL is public | Copy the landing page URL (Kit shows it as a shareable link). Paste into incognito browser. Page loads without login required | [ ] PASS [ ] FAIL | Must be accessible to public subscribers |
| 4 | Form has zone selector | Landing page displays a dropdown or radio button field asking "Which zone are you in?" with options Zones 3–10 | [ ] PASS [ ] FAIL | Zone selection is required for email personalization |
| 5 | Email field present | Form has an "Email" field | [ ] PASS [ ] FAIL | Standard signup field |
| 6 | Name field present | Form has a "First Name" field (or similar) | [ ] PASS [ ] FAIL | Optional but recommended per best practice |
| 7 | Submit button functional | Click the form submit button (with test email `wanka95+test1@gmail.com`). Form accepts input (no validation errors) | [ ] PASS [ ] FAIL | Will be fully tested in 3-test protocol below |
| 8 | Confirmation message | After submit, page shows a confirmation message like "Check your email for your zone card" | [ ] PASS [ ] FAIL | User should understand the next step |

**Gate 3C Status** (Landing Page):
```
Verification timestamp: ___
Landing page created: [ ] YES [ ] NO
Landing page published: [ ] YES [ ] NO
Landing page public URL: [copy URL]: ___
Form fields present: Email [ ] ✓, Name [ ] ✓, Zone [ ] ✓
Overall landing page: [ ] PASS [ ] FAIL
```

---

#### Kit Email Sequence Verification (8 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Automation exists | Kit > Automations > find an automation named "Seedwarden Welcome" or similar | [ ] PASS [ ] FAIL | Automation should contain all 5 emails |
| 2 | Automation is published | Kit > Automations > click the automation > Status shows "Published" (not Draft or Paused) | [ ] PASS [ ] FAIL | Paused automations don't trigger |
| 3 | All 5 emails loaded | Kit > Automations > click the automation > Sequences section shows all 5 emails: Email 1 (Day 0), Email 2 (Day 3), Email 3 (Day 7), Email 4 (Day 10), Email 5 (Day 14) | [ ] PASS [ ] FAIL | All 5 are required for launch |
| 4 | Trigger is correct | Kit > Automations > Trigger section shows "When subscriber joins via landing page" | [ ] PASS [ ] FAIL | Must be landing-page-triggered, not manual |
| 5 | Email 1 subject line | Email 1 > view subject line. Should be something like "Here's your [Zone #] Zone Card" or similar personalization | [ ] PASS [ ] FAIL | Subject must reference the zone for personalization |
| 6 | Email 1 has zone card link | Email 1 > Body > search for a link/button that says "Download your zone card" or similar. Link target is a Google Drive URL (or Kit file storage) | [ ] PASS [ ] FAIL | Zone card link is the core product |
| 7 | Emails 2–5 have bodies | Click into each email (Email 2, 3, 4, 5) > confirm each has substantial body text (not blank/placeholder) | [ ] PASS [ ] FAIL | Copy was loaded in TRACK_B_USER_GATES.md from marketing/email-and-launch-plan.md |
| 8 | Email 5 date reference fixed | Email 5 > Body > search for "May 20 (tomorrow)". If found: it has been removed or replaced with "the guide preview" | [ ] PASS [ ] FAIL | CRITICAL FIX from TRACK_B_USER_GATES.md task |

**Gate 3D Status** (Email Sequence):
```
Verification timestamp: ___
Automation exists and published: [ ] YES [ ] NO
All 5 emails loaded: [ ] YES [ ] NO (missing: ___)
Trigger is landing-page-based: [ ] YES [ ] NO
Zone card link in Email 1: [ ] YES [ ] NO
Date reference in Email 5 removed: [ ] YES [ ] NO
Overall email sequence: [ ] PASS [ ] FAIL
```

---

#### Kit 3-Test Protocol (12 minutes)

**Purpose**: Verify end-to-end delivery. Run this test ONLY after automation is published and landing page is live.

**Test 1: Zone 5 Signup (5 minutes)**

| # | Step | Verification | Pass/Fail | Notes |
|---|---|---|---|---|
| 1.1 | Open incognito browser | Type kit.co/seedwarden or paste your landing page URL | [ ] PASS [ ] FAIL | Incognito prevents tracking interference |
| 1.2 | Fill form | First Name: "Test User", Email: `wanka95+test1@gmail.com`, Zone: "5" (or "Zone 5") | [ ] PASS [ ] FAIL | Use a unique test email each time |
| 1.3 | Submit form | Click "Subscribe" or "Join" button | [ ] PASS [ ] FAIL | Form should accept without errors |
| 1.4 | Wait for email | Check Gmail inbox for `wanka95+test1@gmail.com` (open a new Gmail tab). Wait up to 90 seconds | [ ] PASS [ ] FAIL | Email should arrive within 60 seconds per spec |
| 1.5 | Email 1 arrives | Subject line shows "Zone 5" or zone reference. Body contains text about the zone-specific guide | [ ] PASS [ ] FAIL | Personalization is a key feature |
| 1.6 | Zone card link works | Click "Download your Zone Card" link in the email. A PDF file should download (not open a viewer page) | [ ] PASS [ ] FAIL | Downloads vs. viewers are critical difference for email links |
| 1.7 | PDF contains zone info | Open the downloaded PDF. It displays content specific to Zone 5 (e.g., "Hardiness Zone 5", color band for Zone 5) | [ ] PASS [ ] FAIL | Confirms zone personalization worked |

**Test 1 Result**:
```
Test 1 (Zone 5): [ ] PASS [ ] FAIL
Email delivery time: ___ seconds
Zone card downloaded: [ ] YES [ ] NO
Zone card correctly shows Zone 5: [ ] YES [ ] NO
Issues encountered: ___
```

---

**Test 2: Zone 8 Signup (4 minutes)**

| # | Step | Verification | Pass/Fail | Notes |
|---|---|---|---|---|
| 2.1 | Repeat Test 1 steps | Same as Test 1, but use Zone 8 and email `wanka95+test2@gmail.com` | [ ] PASS [ ] FAIL | Verifies zone 8 routing works |
| 2.2 | Email arrives with Zone 8 | Email subject/body references Zone 8 | [ ] PASS [ ] FAIL | Different zone, should show different content |
| 2.3 | Zone card shows Zone 8 | PDF downloads and displays content specific to Zone 8 | [ ] PASS [ ] FAIL | Each zone card should be unique |

**Test 2 Result**:
```
Test 2 (Zone 8): [ ] PASS [ ] FAIL
Email delivery time: ___ seconds
Zone card correctly shows Zone 8: [ ] YES [ ] NO
Issues encountered: ___
```

---

**Test 3: Delay Verification (3 minutes)**

| # | Step | Verification | Pass/Fail | Notes |
|---|---|---|---|---|
| 3.1 | Wait 1 minute | After Test 2 form submit, wait exactly 1 minute | [ ] PASS [ ] FAIL | Ensure no automatic subsequent emails |
| 3.2 | Check Gmail | Open `wanka95+test2@gmail.com` inbox. You should see ONLY Email 1. NO Email 2 should have arrived yet | [ ] PASS [ ] FAIL | Email 2 should arrive 3 days later (June 1 if tested May 29) |
| 3.3 | Delay logic confirmed | If only Email 1 is present: delay logic is working correctly | [ ] PASS [ ] FAIL | Confirms automation is NOT firing all emails immediately |

**Test 3 Result**:
```
Test 3 (Delay verification): [ ] PASS [ ] FAIL
Only Email 1 received: [ ] YES [ ] NO
No premature Email 2: [ ] YES [ ] NO
Delay logic confirmed: [ ] YES [ ] NO
Issues encountered: ___
```

---

**Gate 3E Status** (3-Test Protocol):
```
Verification timestamp: ___
Test 1 (Zone 5): [ ] PASS [ ] FAIL
Test 2 (Zone 8): [ ] PASS [ ] FAIL
Test 3 (Delay): [ ] PASS [ ] FAIL

OVERALL 3-TEST PROTOCOL: [ ] PASS [ ] FAIL
(All 3 must PASS for Gate 3 to pass)

If any test FAILED, troubleshoot:
  - Email not arriving? Check Kit > Account Settings > Email Authentication (SPF/DKIM)
  - Zone card link broken? Check Kit > Sequences > Email 1 > link URL format (must be: https://drive.google.com/uc?export=download&id=...)
  - Delay not working? Check Kit > Automations > Email delays are set (Day 0, Day 3, Day 7, etc.)
```

---

#### Kit Account Integration Check (2 minutes)

| # | Verification Step | What to Check | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Kit profile public | Kit.co > click "My Profile" or "Share" button > copy public Kit profile URL | [ ] PASS [ ] FAIL | Users can see your Kit storefront |
| 2 | Landing page listed | Your Kit profile shows the Seedwarden landing page as a public link/offer | [ ] PASS [ ] FAIL | Navigation from Kit storefront to landing page |

**Gate 3 Overall Status**:
```
Kit account setup: [ ] PASS [ ] FAIL
Kit tags created: [ ] PASS [ ] FAIL
Landing page live: [ ] PASS [ ] FAIL
Email sequence loaded: [ ] PASS [ ] FAIL
3-test protocol: [ ] PASS [ ] FAIL

GATE 3 FINAL: [ ] PASS [ ] FAIL
If FAIL: which sub-gates failed? ___
Completion timestamp: ___

Gate 3 Status for May 29 go/no-go:
  - If all PASS: Gate 3 is GO (proceed to May 30)
  - If any FAIL: troubleshoot immediately or escalate (see Failure Escalation section below)
```

**Expected completion time**: 35 minutes (including 3-test protocol)

---

## Dependency Matrix: Gate Sequencing & Parallel Work

**Can Gates 1 & 2 run in parallel?** YES — Social accounts (Gate 1) and Canva (Gate 2) have zero dependencies.

**Can Gate 3 start before Gates 1 & 2 are complete?** CONDITIONAL — Kit account can be created, but landing page cannot go live until Gate 2 (Canva Brand Kit) is ready to supply the Kit page design. Gate 3 email sequences can be drafted while Gate 2 is in progress.

**Critical path dependency**: Gate 2 (Canva Brand Kit) must be complete before Gate 3 landing page can be published, because the landing page often references or embeds Canva-designed assets (zone card preview image, etc.).

### Recommended Sequencing

| Timeline | Gate 1 | Gate 2 | Gate 3 | Notes |
|---|---|---|---|---|
| **May 15–18** | ✓ START | — | — | Complete social accounts first (fast, independent) |
| **May 19–25** | ✓ VERIFY | ✓ START & VERIFY | — | Verify Gate 1 while executing Gate 2 (parallel) |
| **May 26–28** | ✓ FINALIZE | ✓ FINALIZE | ✓ START | Gate 2 must be done before Gate 3 landing page goes live |
| **May 28 evening** | ✓ DONE | ✓ DONE | ✓ IN PROGRESS (3-test protocol pending) | All gates running; Gate 3 test protocol critical |
| **May 29 morning** | VERIFICATION | VERIFICATION | ✓ COMPLETE 3-TEST | Final verification before go/no-go decision |
| **May 29 evening** | GO/NO-GO | GO/NO-GO | GO/NO-GO | Decision gate before May 30 launch |

### Why This Order?

1. **Gate 1 first** (May 15–18): Platform account setup is fast (30–45 min total) and has no dependencies. Do this early to get social accounts aging (algorithm favors older accounts).

2. **Gate 2 parallel** (May 19–25): Canva work is independent. Start it while verifying Gate 1. Brand Kit is critical for all zone card production downstream.

3. **Gate 3 last** (May 26–28): Kit setup depends on having Canva Brand Kit ready for visual assets. Sequence building can happen in parallel, but landing page design and zone card links require Gate 2 to be finalized.

4. **Verification sequence** (May 29–30): Stack all go/no-go checks on May 29 evening so you have 12–18 hours to fix any issues before May 30 09:00 UTC launch.

---

## May 29 Evening: Go/No-Go Decision Procedure

**Time**: May 29, 20:00 UTC (or 8 hours before your local launch time)

**Duration**: 30 minutes

**Outcome**: LAUNCH, CONDITIONAL, or NO-GO

### Go/No-Go Scoring Rubric

Run all three gate verifications. Score as follows:

**GATE 1 (Social Accounts)**:
- [ ] PASS = 1 point
- [ ] FAIL = 0 points

**GATE 2 (Canva Brand Kit)**:
- [ ] PASS = 1 point
- [ ] CONDITIONAL (zone cards not yet created but all other elements ready) = 0.5 points
- [ ] FAIL = 0 points

**GATE 3 (Kit Email)**:
- [ ] PASS (3-test protocol passed) = 1 point
- [ ] CONDITIONAL (Email 1 works but Email 2+ not fully tested) = 0.5 points
- [ ] FAIL = 0 points

### Decision Matrix

| Total Score | Decision | Action |
|---|---|---|
| **3.0** | **LAUNCH GO** | Proceed to May 30 09:00 UTC launch. All gates production-ready. |
| **2.5** | **CONDITIONAL GO** | Launch May 30 with minor gaps. Execute 48-hour remediation during Week 1. See escalation paths below. |
| **2.0** | **CONDITIONAL GO** | Launch May 30 with one major gap. Activate contingency for failing gate. Monitor closely first 48 hours. |
| **< 2.0** | **NO-GO** | Do not launch May 30. Slip to June 2–7. See NO-GO escalation procedures below. |

### May 29 Go/No-Go Decision Form

Copy this into your WORKLOG.md or a separate decision log:

```
=== GATE COMPLETION VERIFICATION — May 29, 2026 (T-1 Day) ===

GATE 1 (Social Accounts) Verification:
  Instagram: [ ] PASS [ ] FAIL
  TikTok: [ ] PASS [ ] FAIL
  Pinterest: [ ] PASS [ ] FAIL
  Cross-platform consistency: [ ] PASS [ ] FAIL
  → Gate 1 Score: ___ / 1.0

GATE 2 (Canva Brand Kit) Verification:
  Brand Kit setup: [ ] PASS [ ] FAIL
  Export functionality: [ ] PASS [ ] FAIL
  Zone cards: [ ] PASS [ ] CONDITIONAL [ ] FAIL
  → Gate 2 Score: ___ / 1.0 (or 0.5 if CONDITIONAL)

GATE 3 (Kit Email) Verification:
  Kit account setup: [ ] PASS [ ] FAIL
  Tags configured: [ ] PASS [ ] FAIL
  Landing page live: [ ] PASS [ ] FAIL
  Email sequence: [ ] PASS [ ] FAIL
  3-test protocol: [ ] PASS [ ] CONDITIONAL [ ] FAIL
  → Gate 3 Score: ___ / 1.0 (or 0.5 if CONDITIONAL)

TOTAL SCORE: ___ / 3.0

DECISION:
  [ ] LAUNCH GO (score 3.0)
  [ ] CONDITIONAL GO (score 2.0–2.99)
  [ ] NO-GO (score < 2.0)

If CONDITIONAL or NO-GO:
  Failing gate(s): ___
  Root cause: ___
  Remediation action: ___
  New decision date (if slipping): ___
  Contingency activated: ___

Decision made by: [Your name]
Timestamp: ___
Next step: [ ] Proceed to May 30 launch at 09:00 UTC
           [ ] Execute contingency (see section below)
           [ ] Escalate to user for decision
```

---

## Failure Escalation Paths

Use these if any gate fails verification on May 29.

### Gate 1 Failure: Social Account Issue

**Symptom**: One or more platform accounts missing, or bio text doesn't match spec, or business account type not set.

**Troubleshooting (< 30 minutes)**:

1. **Account doesn't exist**: Immediately create account at that platform using exact steps from TRACK_B_USER_GATES.md. Most platforms approve accounts within 5–15 minutes.

2. **Bio text incomplete**: Edit profile > paste exact bio text from spec. Etsy character limit varies per platform; verify you're not exceeding max length.

3. **Business account not activated**: Settings > Switch to Professional/Business account. Some platforms require 24-hour review; if rejected, revert to personal account (acceptable fallback, though not ideal).

4. **Handle not available**: Use the fallback handles in order: `seedwarden.co`, then `seedwarden.seeds`, then `seedwarden_guides`.

5. **Profile photo not uploading**: Try different image format (JPG vs. PNG) or crop size. Max file size on most platforms: 5 MB.

**If 1 of 3 platforms fails by May 29 evening**:
- Launch with 2 platforms (acceptable fallback)
- Document which platform is missing in WORKLOG.md
- Add the 3rd platform within 3 days of launch (before June 2)
- Update all bios with Kit landing page URL once Gate 3 is live

**If 2+ platforms fail**:
- NO-GO for May 30 launch
- Defer to June 2
- Create all 3 accounts June 1–2
- Re-verify May 29 protocol

**Escalation**: Contact (if available): Etsy platform support via help.etsy.com; Instagram/TikTok/Pinterest via in-app support.

---

### Gate 2 Failure: Canva Brand Kit Issue

**Symptom**: Brand Kit missing, colors incomplete, fonts not present, logo not uploaded, or export fails.

**Troubleshooting (< 45 minutes)**:

1. **Brand Kit doesn't exist**: Log into canva.com > Brand Hub > click "Create a Brand Kit" > name it "Seedwarden". Takes 2 minutes.

2. **Colors missing**: Brand Hub > click Kit > Colors > "Add a color" > paste hex code. Add each missing color. Takes 2 minutes per color.

3. **Fonts missing**: Brand Hub > Fonts > "Add a font" > search for font name (Playfair Display, Lato, Cormorant Garamond). All are free in Canva. Takes 1 minute per font.

4. **Logo not uploading**: Try different file format (convert PNG to JPG if needed). Canva accepts most formats. File size limit: typically 10 MB. Max attempts: 2 before trying a different image.

5. **Export fails (PNG/PDF)**: Common causes:
   - Browser cache issue: Clear cache, try again
   - Browser compatibility: Try Chrome instead of Safari/Firefox
   - File size too large: Reduce design complexity (delete ornamental elements)
   - Hardware acceleration: Turn off in browser settings
   - Max troubleshooting attempts: 3 before declaring failure

6. **Zone cards not created**: If you planned to create 8 zone card templates but haven't yet:
   - CONDITIONAL status acceptable if other elements ready
   - Zone cards can be created June 1–2 (post-launch)
   - During launch, deliver a plain text zone reference email instead (lower conversion, but acceptable)
   - Complete zone cards by June 7

**If Canva export fails after 3 attempts**:
- NO-GO for May 30 launch (visual assets are non-negotiable)
- Defer to June 2
- Contact Canva support: help.canva.com
- Alternative: use Figma or Adobe Express for zone card design (not ideal, but functional)

**Escalation**: Canva support phone/chat: help.canva.com. If support is slow, try alternative design tool (Figma free tier is a backup option).

---

### Gate 3 Failure: Kit Email Issue

**Most Common Issues & Quick Fixes**:

#### 3.1 Email Not Arriving (60+ second delay)

| Diagnosis | Fix | Time |
|---|---|---|
| Kit automation in Draft | Kit > Automations > click automation > click "Publish" | 30 seconds |
| Landing page not published | Kit > Landing Pages > click page > "Publish" | 30 seconds |
| Zone card link is broken | Kit > Sequences > Email 1 > edit link. Correct format: `https://drive.google.com/uc?export=download&id=[FILE_ID]` (NOT the standard share link) | 5 minutes |
| Google Drive file not shared | Google Drive > right-click zone card file > Share > "Anyone with link" (view access) | 2 minutes |
| SPF/DKIM not verified | Kit > Account Settings > Email Authentication. If "Not verified": contact Kit support (48-hour propagation time) | Escalation |

#### 3.2 Zone Card Download Fails

| Diagnosis | Fix | Time |
|---|---|---|
| URL opens viewer instead of downloading | Change URL from `/view` format to `/uc?export=download` format | 3 minutes |
| Browser blocks download | Try different browser (Chrome instead of Safari). Some browsers require user interaction. | 5 minutes |
| File too large | Compress PDF: use Adobe Compress or online PDF compressor. Limit: 5 MB. | 10 minutes |

#### 3.3 Automation Not Triggering

| Diagnosis | Fix | Time |
|---|---|---|
| Automation is Paused | Kit > Automations > find automation > click "Resume" | 30 seconds |
| Trigger not set correctly | Kit > Automations > edit automation > Trigger section. Must say "When subscriber joins via landing page" (not manual, not other trigger) | 5 minutes |
| Landing page not linked to automation | Kit > Landing Pages > edit page > Form Action section > select the automation to trigger | 3 minutes |

**If 3-test protocol fails on May 29 evening**:

- Diagnosis: Which test(s) failed?
  - Test 1 or 2 fails (email not arriving): Email delivery problem. Priority 1.
  - Test 3 fails (delay not working): Automation delay setting. Priority 2, less critical.

- Remediation window: 4 hours (May 29, 20:00 to May 30, 00:00 UTC)
  - Run diagnosis checklist above (15 minutes)
  - Execute fix (5–15 minutes, depending on issue)
  - Re-run 3-test protocol (15 minutes)

- If remediation succeeds: CONDITIONAL GO (proceed with caution on May 30)

- If remediation fails after 2 attempts: NO-GO for May 30. Escalate to Kit support or use Gumroad fallback (see PHASE_2_GO_NO_GO_DASHBOARD.md Contingency Tree B).

**Escalation**: Kit support chat: kit.co > Help. Response time: 2–4 hours. Alternative: use Gmail + manual email send for launch day (functional but not automated).

---

## Summary: Verification Checklist Outcomes

### Ideal Outcome (All Gates PASS)

```
May 29 Evening Decision:
✅ Gate 1: PASS (3/3 social accounts live, all bios correct, links ready)
✅ Gate 2: PASS (Brand Kit configured, all exports working, zone cards created)
✅ Gate 3: PASS (Kit account live, 5-email sequence published, 3-test protocol passed)

TOTAL SCORE: 3.0 / 3.0
DECISION: LAUNCH GO ✓

Action: Wake up at 05:45 UTC May 30. Proceed to May 30 launch sequence at 09:00 UTC.
```

### Acceptable Outcome (Gates PASS with one CONDITIONAL)

```
May 29 Evening Decision:
✅ Gate 1: PASS
✅ Gate 2: CONDITIONAL (zone cards will be created June 1–2)
✅ Gate 3: PASS

TOTAL SCORE: 2.5 / 3.0
DECISION: CONDITIONAL GO

Action: Launch May 30 as planned. Week 1: complete zone card creation by June 2.
        Zone card emails can be sent manually during Week 1 or automated once cards are created.
        Impact: ~15% lower email conversion first week; recovers once cards are ready.
```

### Unacceptable Outcome (Multiple Gates FAIL)

```
May 29 Evening Decision:
✅ Gate 1: PASS
❌ Gate 2: FAIL (Canva Brand Kit export broken)
❌ Gate 3: FAIL (Kit automation not triggering)

TOTAL SCORE: 1.0 / 3.0
DECISION: NO-GO

Action: DO NOT LAUNCH MAY 30.
        Remediation window: May 30–June 1 (2 days).
        New target: June 2 launch.
        Escalate to user if either issue cannot be resolved by June 1 evening.
```

---

## Final Checklist: Complete Before Submitting "GATE VERIFICATION COMPLETE"

- [ ] Gate 1 verification form filled out (all 3 platforms, cross-platform check)
- [ ] Gate 2 verification form filled out (Brand Kit setup, export test, zone cards)
- [ ] Gate 3 verification form filled out (Kit account, tags, landing page, email sequence, 3-test protocol)
- [ ] Dependency matrix reviewed (understand why sequencing matters)
- [ ] May 29 go/no-go decision form prepared (copied into WORKLOG.md or decision document)
- [ ] Failure escalation paths read and understood
- [ ] All Kit landing page URLs updated with links to social bios (if Gate 3 complete)
- [ ] All social bios updated with Kit landing page URL (if Gate 3 complete)
- [ ] Screenshots or audit trail captured for all three gates (proof of completion)
- [ ] Contingency contact info available (Kit support, Canva support, Etsy support) if needed

---

## Quick Reference: Expected Completion Timeline

| Date | Task | Status |
|---|---|---|
| May 15–18 | Gate 1: Create social accounts | [ ] COMPLETE |
| May 19–20 | Gate 1 verification: Confirm all 3 accounts live + bios correct | [ ] COMPLETE |
| May 20–24 | Gate 2: Set up Canva Brand Kit + export test | [ ] COMPLETE |
| May 25–26 | Gate 2 verification: Confirm Kit functions + zone cards ready | [ ] COMPLETE |
| May 26–28 | Gate 3: Create Kit account + landing page + 5-email sequence | [ ] COMPLETE |
| May 28–29 | Gate 3 verification: Run 3-test protocol, confirm delivery | [ ] COMPLETE |
| May 29 | Dependency matrix review + go/no-go decision form | [ ] COMPLETE |
| May 29 20:00 UTC | Final go/no-go decision | [ ] GO / [ ] CONDITIONAL / [ ] NO-GO |
| May 30 09:00 UTC | Launch trigger (if GO) | [ ] LAUNCH |

---

*Created: 2026-05-15. Status: production-ready for user verification.
This document is designed to be executed May 15-29 in parallel with TRACK_B_USER_GATES.md.
All procedures are standalone and require no agent assistance. Use this for verification only.
If any gate fails verification and the fix exceeds 30 minutes, escalate to support or
contingency procedures per PHASE_2_GO_NO_GO_DASHBOARD.md.*
