---
title: "Track B — May 30 Launch Readiness Checklist"
subtitle: "Final verification before launch. Binary pass/fail on every item."
prepared: 2026-05-13
launch-date: 2026-05-30
status: ACTIVE — execute May 28–30 verification blocks
references:
  - PHASE_2_LAUNCH_LOGISTICS.md
  - phase-2-timeline.csv
  - phase-2-analytics-strategy.md
  - PHASE_2_READINESS_AUDIT_MAY_13.md
  - PHASE_2_GO_NO_GO_DASHBOARD.md
  - TRACK_B_FINAL_EXECUTION_GUIDE.md
  - may-30-launch-sequence.md
---

# Track B — May 30 Launch Readiness Checklist

**This is not a timeline. It is a verification document.**

Each item is either ready or it is not. Mark PASS or FAIL. A FAIL requires an immediate
UNRESOLVED action block — who does what, by when — or the launch slips. No item is
"in progress" on launch day. The sole question for each line: is it verifiably done right now?

**Launch target**: May 30, 2026 — Etsy listings go live at 10:00am, Kit email sends at 12:00pm,
social rollout at 2:00pm (Instagram/TikTok), 3:30pm (Pinterest), influencer outreach at 4:00pm.

**Verification window**: Run this checklist on May 28 (T-2) and again on May 29 evening (T-1).
On May 30 at 8:00am, run the Day-1 Execution Sequence (Section 7) only if all five Go/No-Go
criteria in Section 8 are marked PASS.

---

## 1. Asset Completion

All design deliverables, photography, and content files must be in their final export
location and confirmed open without errors before launch.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 1.1 | **8 zone card PDFs exported** — Zones 3–10, one PDF per zone, named `zone-[X]-quick-start-card.pdf` | `ls projects/seedwarden/assets/zone-cards/*.pdf \| wc -l` returns 8 | PASS / FAIL |
| 1.2 | **Zone card Google Drive links live** — All 8 PDF links accessible from an incognito browser without a "Request access" prompt | Open each URL in incognito; confirm immediate download, not viewer | PASS / FAIL |
| 1.3 | **30 lifestyle product photos exported** — Clusters A, B, C; 2400px JPEG, 1:1 crop; saved to `marketing/lifestyle-photos/etsy-ready/` | `ls marketing/lifestyle-photos/etsy-ready/*.jpg \| wc -l` returns ≥30 | PASS / FAIL |
| 1.4 | **Canva Brand Kit active** — 6 hex colors (#143b28, #1A3A2A, #F5EDD6, #EDE0C4, #8FA882, #A0522D), 3 fonts (Playfair Display, Lato, Cormorant Garamond), logo uploaded | Log into canva.com > Brand Hub; confirm Brand Kit shows all 6 colors and 3 fonts | PASS / FAIL |
| 1.5 | **Endangered Species Series palette added to Canva** — 7 colors (#1C2B1A, #3B2A1A, #F0E6C8, #7A9A6E, #F5F1E8, #8B2000, #C49A2A) | Canva Brand Hub shows second palette group labeled "Endangered Species Series" | PASS / FAIL |
| 1.6 | **5 Appalachian Medicinals guide PDFs exported** — Ginseng, Goldenseal, Black Cohosh, Bloodroot, Ramps; final export, no placeholder text | Open each PDF; search for "TBD," "INSERT," "[Name]" — none found; all 6 sections populated | PASS / FAIL |
| 1.7 | **63 product mockup images present** — 21 products × 3 images (tablet, phone, interior) | `ls projects/seedwarden/mockups/*.* \| wc -l` returns ≥63 | PASS / FAIL |
| 1.8 | **iNaturalist CC-BY photo attributions documented** — All photos sourced from iNaturalist CC-BY have attribution logged in WORKLOG.md in the format: "Photo: [Observer], iNaturalist, CC BY 4.0" | Open WORKLOG.md; search for each species name; confirm attribution entry exists | PASS / FAIL |
| 1.9 | **Landing page design live** — Kit landing page published at a working URL with "Your Free Zone Quick-Start Card" headline, zone dropdown (Zones 3–10), and "Send My Zone Card" CTA button | Open the Kit landing page URL in an incognito window; page loads; form submits | PASS / FAIL |

**UNRESOLVED items — fill in if any item above is FAIL:**

> UNRESOLVED 1.X: [Item description] — [Who must do what] by [date/time].

---

## 2. Technical Setup

All platform accounts, integrations, and tracking tools must be configured and confirmed
operational before launch day traffic arrives.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 2.1 | **Kit account created and active** — Account exists at kit.co under wanka95@gmail.com; sender name "Seedwarden"; free tier active | Log into kit.co; account dashboard loads with no setup prompts remaining | PASS / FAIL |
| 2.2 | **Kit welcome automation published** — "Seedwarden Welcome" automation shows "Published" status (not Draft, not Paused) | Kit > Automations > find "Seedwarden Welcome" > confirm status is "Published" | PASS / FAIL |
| 2.3 | **Kit tags created** — All 15 tags present: zone-3 through zone-10 (8), seed-saver, city-grower, preservationist, Cohort_Forager, Cohort_Prepper, Cohort_Homesteader, Cohort_GiftBuyer | Kit > Subscribers > Tags; count 15 tags; names match exactly (case-sensitive) | PASS / FAIL |
| 2.4 | **Etsy account verified** — Shop Manager shows no verification hold banner; store is open to buyers | Log into Etsy Shop Manager; no "Your shop is under review" or "Identity verification required" banner visible | PASS / FAIL |
| 2.5 | **Etsy Shop Manager digital delivery configured** — All Phase 2 listings have "Instant Download" selected and the corresponding PDF file attached | Open 3 listings at random in Shop Manager > confirm "Digital file" section shows uploaded PDF; no empty attachment slot | PASS / FAIL |
| 2.6 | **GA4 Measurement ID entered in Etsy** — GA4 property linked to Etsy Shop Manager | Etsy Shop Manager > Settings > Web Analytics > confirm a GA4 Measurement ID (format: G-XXXXXXXXXX) is entered | PASS / FAIL |
| 2.7 | **GA4 events firing** — GA4 is collecting data from Etsy listing pages | Open a Seedwarden listing in a browser; open GA4 > Real-Time > Events; confirm `page_view` event appears within 60 seconds | PASS / FAIL |
| 2.8 | **GA4 custom dimensions registered** — 6 custom dimensions configured per `etsy-ga4-event-tracking.md` Section 2 | GA4 > Admin > Custom Definitions > Custom dimensions; confirm 6 dimensions present with correct names (case-sensitive) | PASS / FAIL |
| 2.9 | **Social accounts live** — Instagram Business (@seedwarden or documented fallback), TikTok Business (@seedwarden or fallback), Pinterest Business (seedwarden or fallback) | Navigate to each profile URL; accounts are live, have profile photo, have bio text, have Kit landing page link in bio | PASS / FAIL |
| 2.10 | **Social scheduling tool connected** — Buffer or Later shows green/active status for all three platforms (Instagram, TikTok, Pinterest) | Buffer > Settings > Connected Accounts; no "Reconnect" warnings on any platform | PASS / FAIL |
| 2.11 | **UTM parameters applied** — All outbound links from Kit emails, social bios, and Etsy listing CTAs use the correct UTM convention (utm_source, utm_medium, utm_campaign) | Spot-check Instagram bio link and Kit Email 5 Etsy link; confirm UTM parameters present in URL | PASS / FAIL |
| 2.12 | **SEEDWARDEN15 coupon active** — 15% discount, no minimum order, no expiry | Etsy Shop Manager > Marketing > Sales and Coupons; "SEEDWARDEN15" shows status "Active" | PASS / FAIL |

**UNRESOLVED items:**

> UNRESOLVED 2.X: [Item description] — [Who must do what] by [date/time].

---

## 3. Content Staging

All product copy, SEO data, pricing, and promotional structures must be finalized in their
publishing platforms before launch. Nothing is edited after 10:00am May 30.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 3.1 | **Etsy listing descriptions finalized** — All Phase 2 guide listings have complete title, description, and tags matching `etsy-store-copy.md`; no placeholder text | Open each listing in Etsy Shop Manager; search description for "PLACEHOLDER," "TBD," "INSERT" — none found | PASS / FAIL |
| 3.2 | **Pricing verified** — All Phase 2 listings have correct prices as specified in `etsy-store-copy.md`; no listing shows $0.00 or blank | Etsy Shop Manager > Listings; confirm price column shows non-zero values matching the pricing table | PASS / FAIL |
| 3.3 | **Phase 2 listings in Draft status on May 29** — All 5 Appalachian Medicinals listings plus bundle listing exist as Etsy drafts (not yet Active — activation happens at 10:00am May 30) | Etsy Shop Manager > Listings > filter by Draft; count confirms 6 items (5 individual + 1 bundle) | PASS / FAIL |
| 3.4 | **Phase 1 listings remain Active** — All Phase 1 guide listings are published and visible to buyers (not accidentally drafted) | Etsy store public URL in incognito; Phase 1 listings appear in store; no "This listing is unavailable" errors | PASS / FAIL |
| 3.5 | **Bundle listing configured** — 5-guide Appalachian Medicinals bundle exists as a draft listing with correct pricing (bundle price set below sum of individual guides), all 5 PDFs attached | Open the bundle draft listing in Shop Manager; confirm 5 PDF attachments, correct bundle price, description references all 5 species | PASS / FAIL |
| 3.6 | **SEO tags set** — Each Phase 2 listing has 13 tags (Etsy maximum); tags match primary keyword research from `etsy-seo-market-research.md` | Open each listing in Shop Manager > Tags section; confirm 13 tags present, no duplicates | PASS / FAIL |
| 3.7 | **Educational disclaimer present** — Every Appalachian Medicinals guide PDF and Etsy listing description contains the disclaimer: "This guide is for educational purposes. Consult a qualified practitioner before using any plant medicinally." | Open each guide PDF; search for "educational purposes"; open each listing description; confirm disclaimer present | PASS / FAIL |
| 3.8 | **Kit launch broadcast copy finalized** — The May 30 12:00pm broadcast email is written, uses the exact subject line and body copy from `marketing/email-and-launch-plan.md` (Launch Broadcast section), and is staged in Kit | Kit > Broadcasts; find the May 30 broadcast; open and read subject line and first paragraph; confirm matches the approved copy | PASS / FAIL |
| 3.9 | **Kit launch broadcast scheduled** — Broadcast shows "Scheduled" status with send time set to 12:00pm May 30, recipient list "All Confirmed Subscribers" | Kit > Broadcasts; status column shows "Scheduled"; send time reads "May 30, 2026 12:00pm" | PASS / FAIL |
| 3.10 | **Post-purchase survey active** — Kit automation sends a cohort-identification survey in the Day 1 post-purchase email; survey responses apply Cohort_Forager / Cohort_Prepper / Cohort_Homesteader / Cohort_GiftBuyer tags | Kit > Automations > find post-purchase sequence; open survey email; confirm form link is live and tags are mapped | PASS / FAIL |

**UNRESOLVED items:**

> UNRESOLVED 3.X: [Item description] — [Who must do what] by [date/time].

---

## 4. Distribution Channels

All channels through which buyers or subscribers will arrive on launch day must be verified
as live, populated, and connected to the correct destination links.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 4.1 | **Email list exists with at least 1 confirmed subscriber** — Kit subscriber count is ≥1 before launch; automation has fired correctly for at least one real subscriber | Kit > Subscribers; count is ≥1; at least one subscriber has "zone-[X]" tag applied | PASS / FAIL |
| 4.2 | **Instagram launch post staged** — Buffer/Later shows Instagram launch post scheduled for 2:00pm May 30; image is a lifestyle flat-lay from `marketing/lifestyle-photos/etsy-ready/`; caption and hashtags from `phase-2-social-content-calendar-60day.md` Day 30 are present | Buffer queue; find Instagram post; click Preview; image renders correctly; caption is complete; 30 launch day only — PASS / FAIL |
| 4.3 | **TikTok launch post staged** — Buffer/Later shows TikTok launch post scheduled for 2:00pm May 30; content is a video file (MP4, not static image) | Buffer queue; find TikTok post; confirm file type is video; caption present | PASS / FAIL |
| 4.4 | **Pinterest launch pins staged** — At minimum 3 Pinterest pins scheduled for 3:30pm May 30 in Buffer/Later; pins use lifestyle images at 1000×1500px | Buffer queue; find Pinterest pins scheduled May 30 3:30pm; click Preview; images display correctly | PASS / FAIL |
| 4.5 | **Social bio links updated** — All three social bios (Instagram, TikTok, Pinterest) link to the Kit landing page URL (not a placeholder or old URL) | Navigate to each social profile; click the bio link; Kit landing page loads | PASS / FAIL |
| 4.6 | **60-day content calendar loaded into scheduling tool** — At minimum Days 1–14 (May 30–June 12) are scheduled in Buffer/Later for all three platforms | Buffer/Later queue view; posts are present for the first 14 days of the calendar with no gap days | PASS / FAIL |
| 4.7 | **Influencer contact list documented** — List of at least 3 foraging/homesteading accounts to mention at 4:00pm on launch day exists in project docs; each contact has a platform handle and a specific reason for relevance | Open `phase-2-social-content-calendar-60day.md` or a dedicated influencer list; confirm ≥3 handles documented with notes | PASS / FAIL |
| 4.8 | **Analytics Google Sheet created** — A Google Sheet with tabs: Daily, Weekly, Monthly, LTV Tracker, Monthly Data Log exists and is writable | Open the sheet; all 5 tabs present; enter a test value in the Daily tab and save | PASS / FAIL |

**UNRESOLVED items:**

> UNRESOLVED 4.X: [Item description] — [Who must do what] by [date/time].

---

## 5. Operational Readiness

Launch day operations require documented procedures, not improvised decisions. Each item
confirms a specific workflow, policy, or protocol is written and retrievable.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 5.1 | **Etsy digital delivery tested end-to-end** — A test purchase (or simulated purchase confirmation) confirms that Etsy's automatic PDF delivery fires correctly for at least one Phase 2 listing | Ask a trusted contact to purchase one listing using a test account, OR manually verify via Etsy's "Preview listing > test download" flow; PDF downloads without error | PASS / FAIL |
| 5.2 | **Kit end-to-end delivery tested** — From an incognito browser, submitted a test signup (first name "Test", email alias `wanka95+test[date]@gmail.com`, Zone 5); Email 1 arrived within 60 seconds; Zone 5 PDF downloaded without error | Run the test now; record result and timestamp in WORKLOG.md | PASS / FAIL |
| 5.3 | **Refund policy published in Etsy shop** — Etsy Shop Policies section contains the standard digital goods refund policy: no refunds after download except for technical delivery failures | Etsy Shop Manager > Settings > Policies; refund policy text is present and matches `etsy-store-copy.md` Shop Policies section | PASS / FAIL |
| 5.4 | **Customer support message templates written** — At minimum 3 canned responses exist for: (a) download failure, (b) product content question, (c) refund request | Open `launch-day-script.md` or a designated template file; confirm 3 templates present with complete message text | PASS / FAIL |
| 5.5 | **Launch day monitoring tabs documented** — The 6 monitoring tabs to open at 8:00am on May 30 are specified: Etsy Stats > Today, Etsy public store (incognito), Kit > Broadcasts, Kit > Automations, Kit > Subscribers, Buffer/Later queue | Reference `may-30-launch-sequence.md` Section "9:00am — Browser and Device Setup"; confirm the tab list is present | PASS / FAIL |
| 5.6 | **Post-launch monitoring cadence set** — Calendar blocks confirmed for: May 31 (Day 2 email check), June 1 (Day 3 Etsy traffic trend), June 3 (Day 5 Email 3 check), June 6 (Day 7 full review) | Confirm calendar holds exist for all four dates; no competing blocks | PASS / FAIL |
| 5.7 | **Analytics baseline row ready to fill** — `customer-analytics.csv` has correct column headers and a blank row for May 30 launch day metrics | Open `customer-analytics.csv`; file loads; headers present; a blank row exists for 2026-05-30 | PASS / FAIL |
| 5.8 | **LTV tracker configured** — `phase-2-ltv-tracker-phase1-baseline.csv` has columns: buyer_email, first_order_date, first_product, cohort_tag, order_1_date, order_1_value, order_1_products, ltv_to_date | Open the CSV; all columns present; file accepts a new row entry | PASS / FAIL |

**UNRESOLVED items:**

> UNRESOLVED 5.X: [Item description] — [Who must do what] by [date/time].

---

## 6. Risk Mitigation

The following items confirm that contingency plans are documented and executable within the
time constraints of launch day. None of these should require decision-making under pressure
on May 30.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 6.1 | **Etsy verification contingency documented** — If Etsy account is still under review at 06:00am May 30, Gumroad backup path is documented (15-minute setup, product prices match, Kit and social links updated) | Confirm `PHASE_2_GO_NO_GO_DASHBOARD.md` Contingency Tree B exists and Gumroad as Path B2 is readable with step-by-step instructions | PASS / FAIL |
| 6.2 | **Zone card delivery failure protocol documented** — If any zone card Google Drive link returns "Request access" on launch morning, the 5-minute fix procedure is written (change sharing to "Anyone with the link" → copy `uc?export=download&id=` URL → paste into Kit Email 1 variant) | Confirm `PHASE_2_GO_NO_GO_DASHBOARD.md` Contingency Tree D has the exact Drive URL format and Kit navigation path | PASS / FAIL |
| 6.3 | **Buffer/Later manual fallback documented** — If Buffer fails to post social content, the manual posting procedure is written with platform-specific steps and the caption/image source for each post | Confirm `may-30-launch-sequence.md` contains manual fallback instructions for Instagram, TikTok, and Pinterest | PASS / FAIL |
| 6.4 | **Minimum viable launch threshold defined** — The minimum state that constitutes a valid May 30 launch is explicitly documented: at minimum, 2 guides published on Etsy (Ginseng + Goldenseal), Kit automation live, and at least 1 social post live. Fewer than this triggers a slip to June 6. | Confirm `PHASE_2_LAUNCH_LOGISTICS.md` Section 6 Risk 5 or `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 3 documents this threshold explicitly | PASS / FAIL |
| 6.5 | **Technical support contacts available** — Etsy support URL (`help.etsy.com`), Kit support URL (`kit.com/support` or in-app chat), and Buffer support URL are known and accessible | Verify each URL loads in a browser now; bookmark all three | PASS / FAIL |

**UNRESOLVED items:**

> UNRESOLVED 6.X: [Item description] — [Who must do what] by [date/time].

---

## 7. Day 1 Execution Sequence

This is the minute-by-minute launch protocol for May 30. It is not a checklist to complete
in advance — it is a script to execute on the day. It is included here so the sequence is
confirmed as written and agreed before launch day, not improvised at 8:00am.

The full reference document is `may-30-launch-sequence.md`. The summary below is the
sequence contract: these are the exact times and actions, in order.

| Time | Action | Done Signal |
|------|--------|-------------|
| **8:00am** | Open 6 monitoring tabs. Run final QA: verify all 21 listings are Active with 5 images each; verify SEEDWARDEN15 coupon shows "Active"; run Kit end-to-end test (Zone 5 incognito signup → PDF download in 60 seconds); check Buffer shows all posts scheduled with no reconnect warnings | All 6 tabs open; QA items pass; any fix completed before 9:00am |
| **9:00am** | Record pre-launch baseline metrics in `customer-analytics.csv`: Etsy 7-day views, Etsy total orders to date, Kit subscriber count, Instagram followers, TikTok followers, Pinterest monthly viewers | Row entered in `customer-analytics.csv` with timestamp 09:00 May 30 |
| **9:45am** | Personal prep. Do not start new tasks. Be present to respond to any issue surfacing in the T+0 window. | No new tasks started |
| **10:00am** | **Etsy listings go live.** Etsy Shop Manager > Listings > select all Phase 2 listings in Draft > click "Publish." All listings become Active simultaneously. Navigate to public store in incognito to confirm listings appear. | Phase 2 listings visible in public Etsy store; note launch timestamp in `customer-analytics.csv` |
| **10:00am–12:00pm** | Monitor Etsy. Check every 30 minutes: shop views today, any new orders. Any pre-email organic order is a high-value signal — record buyer and listing in WORKLOG.md. Fix any listing errors found immediately. | No listing errors; views incrementing |
| **12:00pm** | **Kit launch email sends.** At 12:05pm, navigate to Kit > Broadcasts; confirm status reads "Sending" or "Sent." If still "Scheduled" at 12:20pm, click "Send Now." | Broadcast status shows "Sending" or "Sent" |
| **12:30pm** | Check Kit broadcast delivery rate (target >90%), open rate (target >35%), click rate (target >8%). Note any bounce rate above 2% — if bounce rate exceeds 2%, pause any remaining queue and remove hard bounces before resuming. | Delivery rate >80% minimum; click rate checked |
| **2:00pm** | **Instagram and TikTok posts go live** via Buffer/Later. At 2:15pm, confirm Instagram launch post is visible at top of profile feed. Confirm TikTok video is live. If either fails, post manually using `phase-2-social-content-calendar-60day.md` Day 30 caption and corresponding image. | Both posts visible on their respective platforms |
| **3:30pm** | **Pinterest launch pins go live** via Buffer/Later. At 3:45pm, navigate to Pinterest profile and confirm pins are visible. Note: Pinterest's indexing takes 2–24 hours; Day 1 Pinterest impressions are lower than Instagram and TikTok — do not calibrate against Pinterest Day 1 data. | Pins visible on Pinterest profile |
| **4:00pm** | **Influencer mentions.** Post story mentions or comments to the ≥3 foraging/homesteading accounts documented in the influencer list. Use genuine, specific engagement — not a generic tag. | ≥3 outreach interactions completed; noted in WORKLOG.md |
| **7:00pm–9:00pm** | **End-of-day log.** Record in `customer-analytics.csv`: Etsy views, Etsy orders, Etsy revenue, Kit broadcast open rate, Kit broadcast click rate, Kit new subscribers, Instagram impressions, TikTok views, new followers across platforms. Note any anomalies in WORKLOG.md. Respond to any buyer messages within 4 hours. | Day 1 row complete in `customer-analytics.csv`; all buyer messages acknowledged |

---

## 8. Go/No-Go Decision Criteria

**All five criteria must be GO for the May 30 launch to proceed.** Evaluate on May 29 evening
by working through this section against live systems. Record the full audit block in WORKLOG.md.

One NO-GO with a clear 24-hour remediation path = YELLOW (launch proceeds after fix, same day).
Two or more NO-GO, or any NO-GO with no feasible same-day fix = RED (launch slips; execute
the contingency decision tree in `PHASE_2_GO_NO_GO_DASHBOARD.md` Section 3).

---

### Criterion 1: Guides Complete

**Definition**: All 5 Appalachian Medicinals guides (Ginseng, Goldenseal, Black Cohosh,
Bloodroot, Ramps) exist as exported PDFs with all 6 content sections populated, no
placeholder text, and all iNaturalist CC-BY photo attributions present in the file footer.

**Minimum viable**: 2 guides complete (Ginseng + Goldenseal). With 2 guides, launch is
reduced-scope but viable. 3–4 guides is the realistic minimum for full launch messaging.
Fewer than 2 = NO-GO.

| Sub-check | Verification | GO Signal |
|-----------|-------------|-----------|
| C1.1 — 5 guide PDFs present | `ls projects/seedwarden/products/*.pdf` includes all 5 species | 5 files present |
| C1.2 — No placeholder text | Search each PDF for "TBD", "INSERT", "[Name]" | 0 instances found |
| C1.3 — Attribution footers | Open each PDF; footer contains "Photo: [Name], iNaturalist, CC BY 4.0" for each CC-BY image | All attributions present |
| C1.4 — Educational disclaimer | Each PDF contains the educational disclaimer | Disclaimer visible in all 5 |
| C1.5 — Conservation status accurate | Each species' conservation status matches the reference in `endangered-species-candidate-list.md` | Status language verified against source |

**Criterion 1 assessment**: GO / NO-GO

---

### Criterion 2: Visual Assets Ready

**Definition**: All 8 zone card PDFs are exported and their Google Drive download links are
confirmed accessible. Canva Brand Kit (both palettes) is active. At least 30 lifestyle photos
are in the export directory.

| Sub-check | Verification | GO Signal |
|-----------|-------------|-----------|
| C2.1 — 8 zone cards exported | `ls assets/zone-cards/*.pdf \| wc -l` | Returns 8 |
| C2.2 — Zone card links accessible | Open all 8 Google Drive URLs in incognito | All 8 download without "Request access" |
| C2.3 — Canva Brand Kit active | Brand Hub shows Kit with 6 base colors + 7 Endangered Species colors | Both palette groups confirmed |
| C2.4 — 30 lifestyle photos present | Count files in `marketing/lifestyle-photos/etsy-ready/` | ≥30 JPEG files |
| C2.5 — Mockup images present | `ls projects/seedwarden/mockups/ \| wc -l` | ≥63 files |

**Criterion 2 assessment**: GO / NO-GO

---

### Criterion 3: Marketing Infrastructure Live

**Definition**: Kit welcome automation is published, launch broadcast is scheduled for 12:00pm
May 30, a Zone 5 test sign-up delivers the PDF within 60 seconds, and all 3 social posts are
scheduled for their correct times in Buffer/Later with no platform connection errors.

| Sub-check | Verification | GO Signal |
|-----------|-------------|-----------|
| C3.1 — Kit automation published | Kit > Automations > "Seedwarden Welcome" | Status: "Published" |
| C3.2 — Broadcast scheduled | Kit > Broadcasts > May 30 broadcast | Status: "Scheduled" at 12:00pm May 30 |
| C3.3 — End-to-end Kit test | Incognito signup Zone 5 → Gmail → Zone 5 PDF downloads | Delivery within 60 seconds |
| C3.4 — Social posts scheduled | Buffer/Later queue | Instagram 2:00pm, TikTok 2:00pm, Pinterest 3:30pm — all confirmed |
| C3.5 — Platform connections active | Buffer > Settings > Connected Accounts | Instagram, TikTok, Pinterest all green |

**Criterion 3 assessment**: GO / NO-GO

---

### Criterion 4: Sales Channel Ready

**Definition**: Etsy account is verified and open to buyers, all Phase 2 listings are in Draft
(ready to publish at 10:00am), a test PDF delivery confirms Etsy's digital download mechanism
works, prices match the approved pricing table, and SEEDWARDEN15 coupon is active.

| Sub-check | Verification | GO Signal |
|-----------|-------------|-----------|
| C4.1 — Etsy account verified | Etsy Shop Manager loads with no verification hold banner | No hold; shop open to buyers |
| C4.2 — Phase 2 listings in Draft | Shop Manager > Listings > Draft filter | 6 listings (5 individual + 1 bundle) in Draft |
| C4.3 — Digital delivery works | Test purchase or Etsy preview confirms PDF attaches and delivers | PDF downloads immediately post-purchase |
| C4.4 — Prices correct | Each listing price matches `etsy-store-copy.md` pricing table | No $0.00 or blank prices |
| C4.5 — SEEDWARDEN15 active | Etsy > Marketing > Sales and Coupons | Code "SEEDWARDEN15" shows "Active", 15% discount |

**Criterion 4 assessment**: GO / NO-GO

---

### Criterion 5: Analytics Infrastructure Ready

**Definition**: The Google Sheets analytics workbook is created with all required tabs,
`customer-analytics.csv` has correct headers and is writable, the LTV tracker has correct
columns, Week 1 numeric targets are documented, and calendar blocks for post-launch monitoring
sessions are confirmed for May 31, June 1, June 3, and June 6.

| Sub-check | Verification | GO Signal |
|-----------|-------------|-----------|
| C5.1 — Analytics CSV writable | Open `customer-analytics.csv`; write a test value; save | File accepts writes; no permission errors |
| C5.2 — LTV tracker configured | Open `phase-2-ltv-tracker-phase1-baseline.csv`; check columns | buyer_email, cohort_tag, order dates/values, ltv_to_date all present |
| C5.3 — Week 1 targets documented | Open `phase-2-week-1-success-metrics.md` | Numeric targets present for orders, revenue, Kit subscribers, email open rate |
| C5.4 — Monitoring calendar confirmed | Check calendar for May 31, June 1, June 3, June 6 | All 4 dates have review blocks; no competing events |

**Criterion 5 assessment**: GO / NO-GO

---

### Overall Go/No-Go Verdict (record in WORKLOG.md on May 29 evening)

```
## Phase 2 Go/No-Go Audit — May 29, 2026 (T-1 Day)

Criterion 1 — Guides Complete:          GO / NO-GO
Criterion 2 — Visual Assets Ready:      GO / NO-GO
Criterion 3 — Marketing Infrastructure: GO / NO-GO
Criterion 4 — Sales Channel Ready:      GO / NO-GO
Criterion 5 — Analytics Ready:          GO / NO-GO

OVERALL: ___ of 5 criteria GO
STATUS: GREEN (5/5) / YELLOW (4/5 with remediable gap) / RED (3 or fewer)
DECISION: LAUNCH May 30 / SLIP TO June 6 / ESCALATE
Contingency activated (if any): ___
Next action: ___
Confidence level (1–10): ___
```

**If confidence level is below 7/10**: Do not launch May 30. Document the specific concern,
activate the relevant contingency tree from `PHASE_2_GO_NO_GO_DASHBOARD.md`, and set June 6
as the new target. A partial launch with unresolved doubts produces worse outcomes than a
one-week slip.

---

*Checklist prepared May 13, 2026. To be executed May 28 (first pass) and May 29 evening (final
Go/No-Go pass). Day 1 execution sequence (Section 7) runs on May 30 only after all Section 8
criteria are marked GO. Reference documents for any UNRESOLVED item: `PHASE_2_GO_NO_GO_DASHBOARD.md`
(contingency trees), `may-30-launch-sequence.md` (minute-by-minute protocol), `TRACK_B_FINAL_EXECUTION_GUIDE.md`
(production gates), `PHASE_2_LAUNCH_LOGISTICS.md` (photography and guide production timeline).*
