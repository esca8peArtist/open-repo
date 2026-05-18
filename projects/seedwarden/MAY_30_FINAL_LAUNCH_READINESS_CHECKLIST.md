---
title: "May 30 Final Launch Readiness Checklist — Phase 2"
prepared: 2026-05-18
launch-date: 2026-05-30
days-remaining: 12
status: ACTIVE — complete May 28-29, go/no-go decision May 29 21:00 UTC
scope: >
  100-item comprehensive pre-launch audit. Covers inventory, Etsy store, email sequence,
  social media scheduling, payment processing, customer support, analytics, fulfillment,
  contingency, and go/no-go decision gate.
references:
  - PHASE_2_GO_NO_GO_DASHBOARD.md (5-criteria go/no-go framework)
  - TRACK_B_MAY_30_LAUNCH_READINESS_CHECKLIST.md (Track B binary verification)
  - MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md (hour-by-hour launch sequence)
  - LAUNCH_CONTINGENCY_PLAYBOOKS.md (failure mode recovery)
  - KIT_EMAIL_LAUNCH_SEQUENCE.md (email automation specs)
  - PHASE_2_ANALYTICS_INFRASTRUCTURE_PRESTAGING.md (analytics setup)
  - phase-2-launch-day-checklist.md (minute-by-minute script)
---

# May 30 Final Launch Readiness Checklist

**Launch target**: May 30, 2026
**Verification window**: May 28 (T-2) and May 29 (T-1). Minimum 2 hours per sitting.
**Go/no-go decision**: May 29 at 21:00 UTC. All 100 items must be checked.
**Decision rule**: If more than 2 items are FAIL on May 29 evening, delay launch 24 hours to May 31. Correct failures overnight. Re-run the failed items only on May 31 morning before proceeding.
**Companion documents**: Open `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md` alongside this checklist on verification day. That document contains the minute-by-minute May 30 script.

---

## How to Use This Checklist

Mark each item PASS or FAIL. Do not mark "in progress" — every item is either verifiably done or it is not. If an item is FAIL, write the corrective action and who completes it before leaving the verification session. Items with a star (*) are blocking: a single FAIL on a starred item triggers an immediate escalation decision, regardless of the 2-item rule.

Estimated time to complete: 2 hours on May 28, 1 hour on May 29 (re-check FAIL items only).

---

## Section 1: Inventory Checklist (Items 1-10)

This section verifies that every product going live May 30 is complete, file-correct, and priced accurately.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 1 | **Phase 2 guide files present — all 5** * | `ls projects/seedwarden/products/` returns at least 5 Phase 2 guide files (Ginseng, Goldenseal, Wild Bergamot, Trillium, Bloodroot — or the confirmed Core Four + 1 substitute). Record exact filenames. | PASS / FAIL |
| 2 | **Guide completeness — no placeholder text** * | Open each of the 5 guide files. Search for the strings "PLACEHOLDER", "TODO", and "TBD". Must return zero matches across all 5 files. | PASS / FAIL |
| 3 | **Bundle E assembly — 5 guides + assets confirmed** | Open `BUNDLE_E_PUBLICATION_PACKAGE.md`. Confirm that all 5 guide PDFs, all required zone card PDFs, and all mockup images listed in that document are present at their stated file paths. | PASS / FAIL |
| 4 | **Phase 1 carryover products — status confirmed** | Open `UPLOAD_READY_CHECKLIST.md`. For every Phase 1 product listed as "ready," confirm: (a) the Etsy listing is live or in Draft pending activation, and (b) any tag corrections documented in that file have been applied. | PASS / FAIL |
| 5 | **All product PDFs under Etsy 5 MB file limit** | Run `ls -lh projects/seedwarden/products/*.pdf` (or equivalent). Confirm every PDF file is under 5.0 MB. Flag any file above 4.5 MB for review. | PASS / FAIL |
| 6 | **Mockup images present and current** | Run `ls projects/seedwarden/mockups/` — confirm mockup files exist for every Phase 2 product. Cross-check timestamps: no mockup should be older than its corresponding PDF. If any mockup predates its PDF, regenerate before May 30. | PASS / FAIL |
| 7 | **Phase 2 product pricing verified** | Open `etsy-store-copy.md`. Confirm the price listed for every Phase 2 product matches the price set in the Etsy Draft listing. Record each price pair. Mismatches must be corrected in Etsy before launch. | PASS / FAIL |
| 8 | **Zone card PDFs present — all 8 zones** | Run `ls projects/seedwarden/assets/zone-cards/*.pdf \| wc -l` — must return 8. If fewer than 8 are present, follow `CANVA_ZONE_CARD_BATCH_WORKFLOW.md` immediately. This is the highest-risk gap in Phase 2. | PASS / FAIL |
| 9 | **Habit photos licensed and documented — all 18** | Open `WORKLOG.md`. Confirm all 18 wild edibles species have a license entry with source URL. No species may have a blank or "pending" license field. | PASS / FAIL |
| 10 | **SEEDWARDEN15 coupon active** | Log into Etsy Shop Manager > Marketing > Sales and Coupons. Confirm SEEDWARDEN15 exists: 15% off, no minimum purchase, no expiry date. If absent, create it now. | PASS / FAIL |

---

## Section 2: Etsy Store Finalization (Items 11-25)

This section confirms that every public-facing element of the Etsy store is in its final state before listings go live.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 11 | **Etsy account — no verification hold** * | Log into Etsy Shop Manager. Confirm there is no yellow or red banner indicating a verification hold, payment issue, or policy violation. If a hold is present, contact Etsy seller support immediately — this is a launch blocker. | PASS / FAIL |
| 12 | **All Phase 2 listings in Draft status** | In Etsy Shop Manager > Listings, filter by "Draft." Confirm all Phase 2 listings are in Draft (not accidentally Active, not missing). Listings should not go Active until 10:00am May 30. | PASS / FAIL |
| 13 | **All listings have correct PDFs attached** | Open each Draft listing. Under "Digital files," confirm the correct PDF is attached (file name matches product, not a leftover file from another listing). Click "Preview" to confirm the file opens without error. | PASS / FAIL |
| 14 | **Listing titles and descriptions match `etsy-store-copy.md`** | Open each Draft listing side by side with `etsy-store-copy.md`. Confirm title, first paragraph, and bullet list match the final copy in that file. No placeholder text in any listing description. | PASS / FAIL |
| 15 | **SEO tags — 13 tags per listing, all relevant** | Open each Draft listing. Confirm exactly 13 tags are populated (Etsy maximum). Tags must include primary keywords documented in `etsy-seo-market-research.md`. No tag should be generic (e.g., "digital download" alone is insufficient without specificity). | PASS / FAIL |
| 16 | **Listing category — correct Etsy category selected** | For each listing, confirm the Etsy category is set to the correct node (e.g., "Books, Movies & Music > Books > Nonfiction" or "Craft Supplies & Tools > Gardening & Plants"). Wrong categories suppress search visibility. | PASS / FAIL |
| 17 | **Primary listing image — mockup visible, correct dimensions** | Confirm Image Slot 1 of each listing is the correct mockup image at 2400x2400 px. Open each image in a new tab and verify it renders without distortion and matches the product it represents. | PASS / FAIL |
| 18 | **Additional listing images populated (Slots 2+)** | Confirm each listing has at least 2 images (primary mockup + at least one interior/lifestyle image). Single-image listings underperform significantly in Etsy search. | PASS / FAIL |
| 19 | **Etsy shop banner and announcement set** | In Etsy Shop Manager > Shop Settings > Public Profile, confirm: (a) a shop banner is uploaded (not the default grey block), (b) the Shop Announcement field contains the launch message from `etsy-store-copy.md`. | PASS / FAIL |
| 20 | **Shop bio and logo uploaded** | Confirm the Etsy shop icon (logo) is the correct Seedwarden logo file. Confirm the "About" section is populated with the Seedwarden brand story. Neither field should be blank. | PASS / FAIL |
| 21 | **Shipping profile — digital downloads configured** | In Etsy > Shop Manager > Settings > Shipping, confirm a shipping profile exists for digital downloads (instant delivery, no shipping cost, no processing time). Confirm this profile is assigned to all Phase 2 listings. | PASS / FAIL |
| 22 | **Tax settings — automatic Etsy tax collection active** | In Etsy > Shop Manager > Finances > Billing, confirm that "Etsy Payments" is enabled and that Etsy is set to collect sales tax automatically (Etsy handles this for US sales by default; verify it is not turned off). | PASS / FAIL |
| 23 | **Etsy return and exchange policy set** | In Etsy > Shop Manager > Settings > Policies, confirm the Returns & Exchanges policy states clearly that digital downloads are non-refundable except in documented cases of file delivery failure. Do not leave this field blank — blank policy creates buyer disputes. | PASS / FAIL |
| 24 | **Etsy privacy and terms policy set** | Confirm that Privacy Policy and FAQs fields in Etsy Shop Policies are populated (even with a brief statement). Blank policy pages are a trust signal deficiency. | PASS / FAIL |
| 25 | **Etsy listing preview verified in incognito browser** | Open each listing URL (from the Draft preview link) in an incognito browser window. Confirm the listing renders correctly for an unauthenticated visitor. Confirm the "Add to cart" button is absent (it should not be present on Draft listings). | PASS / FAIL |

---

## Section 3: Email Sequence Validation (Items 26-35)

This section confirms that the Kit email infrastructure will fire correctly on launch day and that the list is clean.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 26 | **May 30 launch broadcast created in Kit** * | Log into kit.co > Broadcasts. Confirm a broadcast exists titled "Seedwarden is live — [subject line from `marketing/email-and-launch-plan.md`]". Confirm status is "Scheduled," not Draft. | PASS / FAIL |
| 27 | **Broadcast scheduled for 12:00pm correct timezone** * | Open the scheduled broadcast in Kit. Confirm the send time is 12:00pm in the timezone configured during Kit account setup. If Kit is configured for UTC, that is 12:00 UTC. If configured for US/Eastern, that is 12:00pm Eastern (17:00 UTC). Confirm the timezone is consistent with all other launch timing documents. | PASS / FAIL |
| 28 | **Broadcast subject line and preview text finalized** | Open the broadcast. Confirm subject line matches the approved copy in `marketing/email-and-launch-plan.md`. Confirm preview text (the line that appears in inbox previews after the subject) is set and not left as the default Kit placeholder. | PASS / FAIL |
| 29 | **Broadcast body links verified — all Etsy URLs correct** | In the broadcast body, click every link. Confirm each link goes to the correct Etsy listing, not a placeholder URL or a 404. Note: Etsy Draft listing URLs are not the final public URLs — confirm you are using the public listing URLs (activate temporarily in a test shop or use the confirmed URL format). | PASS / FAIL |
| 30 | **Kit Welcome Sequence automation set to "Published"** | In Kit > Automations, find the "Seedwarden Welcome" sequence. Status must show "Published" (green indicator). Draft or Paused means it will not fire on new subscriptions. | PASS / FAIL |
| 31 | **Zone card delivery test — end-to-end** * | Open an incognito browser. Navigate to the Kit landing page URL. Enter a test name, email address, and select Zone 5. Submit the form. Within 60 seconds, check the test inbox. Confirm Email 1 (Zone 5 variant) arrives with the correct zone card Google Drive link. Click the link — confirm it downloads the PDF immediately without a "Request access" prompt. Log the test result in WORKLOG.md. | PASS / FAIL |
| 32 | **Recipient list — bounce check completed** | In Kit > Subscribers, filter for any "bounced" or "unconfirmed" addresses in the existing list. Remove or suppress bounced addresses. If the list is under 50 subscribers at this stage, this step is low-risk but still required. | PASS / FAIL |
| 33 | **Unsubscribe link present in every email** | Open each of the 5 Kit sequence emails. Scroll to the bottom. Confirm the Kit-generated unsubscribe link is present and active. Kit includes this by default but verify it has not been accidentally removed during editing. | PASS / FAIL |
| 34 | **Reply handling process documented** | Open `PHASE_2_CUSTOMER_SUCCESS_FRAMEWORK.md` or the equivalent support document. Confirm a process exists for handling replies to the launch broadcast (e.g., who monitors the reply-to address, what is the response time target, what are the standard response templates). | PASS / FAIL |
| 35 | **Spam filter test completed** | Send the launch broadcast to yourself as a test send (Kit has a "Send test" function). Open the test email in Gmail. Confirm: (a) it does not land in the Spam or Promotions tab, (b) all images load, (c) all links are clickable on mobile. If it lands in Spam, diagnose the trigger (link count, spam words in subject) before May 29 end of day. | PASS / FAIL |

---

## Section 4: Social Media Scheduling (Items 36-50)

This section confirms that all launch-day social content is scheduled, correctly formatted, and has a monitoring plan.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 36 | **Instagram launch post scheduled — May 30 14:00 UTC** | Log into Buffer (or Later). Confirm one Instagram post is scheduled for May 30 at 14:00 UTC. Status must show "Scheduled," not "Draft" or "Failed." | PASS / FAIL |
| 37 | **TikTok launch post scheduled — May 30 14:00 UTC** | Confirm one TikTok post is scheduled for May 30 at 14:00 UTC. Verify TikTok connection in Buffer/Later shows green (no "Reconnect" warning). | PASS / FAIL |
| 38 | **Pinterest launch pins scheduled — May 30 15:30 UTC** | Confirm at least 3 Pinterest pins are scheduled for May 30 at 15:30 UTC. Pinterest performs better with batch pinning (3-5 pins per session) versus a single pin. | PASS / FAIL |
| 39 | **Facebook launch post scheduled (if applicable)** | If a Seedwarden Facebook page exists: confirm a post is scheduled for May 30 at 14:00 UTC. If no Facebook page exists, mark this item N/A (not a blocker). | PASS / FAIL / N-A |
| 40 | **All social account connections green in Buffer/Later** | In Buffer/Later > Settings > Connected Accounts, confirm all connected accounts show a green status indicator. Any "Reconnect" or "Expired token" warning must be resolved before May 30. Reconnecting an account takes 5 minutes but must be done while logged into the social platform. | PASS / FAIL |
| 41 | **Instagram image dimensions — 1080x1080 px for feed, 1080x1920 px for Reels** | Open the scheduled Instagram post in Buffer/Later and preview it. Confirm the image is not cropped in a way that cuts off text or product imagery. For Reels: confirm the vertical 9:16 aspect ratio is preserved. | PASS / FAIL |
| 42 | **TikTok video — 1080x1920 px, under 500 MB, under 10 minutes** | If posting a TikTok video: confirm the file meets TikTok's specs. If posting an image carousel: confirm each image is 1080x1080 px or 1080x1350 px (portrait). | PASS / FAIL |
| 43 | **Pinterest image dimensions — 1000x1500 px (2:3 ratio)** | Confirm all scheduled Pinterest pins use the 1000x1500 px vertical format. Pinterest suppresses pins that do not use the 2:3 ratio. Square or horizontal images will underperform significantly. | PASS / FAIL |
| 44 | **Instagram caption finalized — includes Etsy link instruction** | Open the scheduled Instagram post. Confirm the caption includes a clear call to action directing followers to the bio link (e.g., "Link in bio to get your copy"). Instagram does not allow clickable links in captions — the bio link is the only conversion path. | PASS / FAIL |
| 45 | **TikTok caption finalized — under 2,200 characters** | Confirm TikTok caption is under 2,200 characters and includes a hook in the first line (the first ~100 characters display before "more" is clicked). Confirm any relevant hashtags are included at the end. | PASS / FAIL |
| 46 | **Hashtag strategy applied — verified in all captions** | Confirm that hashtags from the approved strategy are present in each platform's post: Instagram (20-25 relevant hashtags including #seedwarden, #wildfoods, #foraging, #nativeplants, #wildfoodlove), TikTok (5-7 hashtags), Pinterest (board-specific keywords in description). | PASS / FAIL |
| 47 | **Instagram bio link — points to Kit landing page** | Open the Seedwarden Instagram profile in a browser (not the app). Click the bio link. Confirm it opens the Kit landing page (Zone Quick-Start Card sign-up), not a stale URL from a prior campaign. | PASS / FAIL |
| 48 | **Cross-posting deduplication confirmed** | Review all scheduled May 30 posts. Confirm that identical copy is not posted verbatim across Instagram, TikTok, and Pinterest on the same day. Platform algorithms suppress cross-posted identical content. Captions should be platform-native: conversational on TikTok, keyword-rich on Pinterest, community-focused on Instagram. | PASS / FAIL |
| 49 | **Engagement response plan documented** | Confirm a process is in place for monitoring launch-day comments and DMs: who checks (this is a solo operation, so this is confirming a time block on May 30), how often (every 2 hours is the minimum on launch day), what comments require a reply versus a like, what to do with negative or troll comments (do not delete unless abusive; a calm reply is the correct response). | PASS / FAIL |
| 50 | **Social post preview approved on mobile** | Open each scheduled post in Buffer/Later's mobile preview. Confirm that text is not cut off, hashtags are not wrapping awkwardly, and images look correct at phone screen scale. Desktop preview alone is not sufficient — Seedwarden's audience is predominantly mobile. | PASS / FAIL |

---

## Section 5: Payment Processor End-to-End (Items 51-60)

This section confirms that payments can be accepted, receipts deliver, and refunds can be processed. For a digital-only Etsy store, most payment infrastructure is Etsy-native; these items verify that the Etsy Payments setup is functioning and tested.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 51 | **Etsy Payments enrolled and active** * | In Etsy > Shop Manager > Finances > Billing, confirm "Etsy Payments" shows status "Active." If it shows "Enrollment required" or any error, resolve immediately — no purchases can be completed without Etsy Payments. | PASS / FAIL |
| 52 | **Etsy Payments bank account linked** * | In Etsy > Finances > Payment account, confirm a bank account is linked for deposit. Confirm the account number last 4 digits match the intended deposit account. If not linked: add bank account now (takes 1-3 business days for micro-deposit verification — do this before May 26). | PASS / FAIL |
| 53 | **Test order placed and receipt verified** | Place a test purchase on a Phase 2 listing using a personal or test Etsy buyer account (not the seller account). Confirm: (a) checkout completes without error, (b) confirmation email arrives in the buyer inbox within 5 minutes, (c) the PDF download link in the confirmation email is clickable and delivers the correct file. | PASS / FAIL |
| 54 | **Order appears in Etsy Shop Manager** | After the test purchase, log into Etsy Shop Manager > Orders & Shipping. Confirm the test order appears with status "Complete" (digital orders should auto-complete since no shipping is required). | PASS / FAIL |
| 55 | **Test refund processed** | From the test order, issue a refund using Etsy's refund workflow (Shop Manager > Orders > [Order] > Issue a refund). Confirm the refund is processed and a refund confirmation email is sent to the buyer. Document the refund steps in `PHASE_2_CUSTOMER_SUCCESS_FRAMEWORK.md` if not already there. | PASS / FAIL |
| 56 | **Fulfillment triggered correctly — digital delivery** | Confirm that digital file delivery for the test order was automatic (Etsy delivers digital files immediately on payment for digital listings). Confirm no manual step was required to send the file. If manual delivery was triggered, investigate why — digital listings should auto-deliver. | PASS / FAIL |
| 57 | **Tax calculation correct on test order** | Review the test order receipt. Confirm Etsy applied the correct state sales tax for the test buyer's location (Etsy collects this automatically for US states that require marketplace facilitator tax). If the tax line is absent on a taxable order, investigate Etsy's tax settings. | PASS / FAIL |
| 58 | **PayPal accepted as payment method (verify Etsy Payments includes it)** | In Etsy > Finances > Etsy Payments, confirm that PayPal is listed as one of the accepted payment methods (Etsy Payments includes PayPal, Apple Pay, Google Pay, and credit cards by default). No action required if this is confirming the default state — just verify it is not disabled. | PASS / FAIL |
| 59 | **Deposit schedule reviewed** | In Etsy > Finances > Billing, review the deposit schedule (weekly or daily). Confirm the schedule matches your expectation for when revenue will reach the bank account after launch. No action required; this is informational but must be known before launch day. | PASS / FAIL |
| 60 | **Currency set to USD** | Confirm the Etsy shop currency is set to USD. If the shop currency is set to a non-USD currency, international buyers will see conversion rates that may differ from the listed price — this can create buyer confusion and support tickets. | PASS / FAIL |

---

## Section 6: Customer Support Setup (Items 61-68)

This section confirms that buyer questions, complaints, and requests can be handled within the response time SLA.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 61 | **Etsy response time target documented** | Confirm a response time SLA is documented (recommend: within 4 hours during business hours, within 12 hours outside business hours). This must be a written commitment, not an informal intention. Location: `PHASE_2_CUSTOMER_SUCCESS_FRAMEWORK.md`. | PASS / FAIL |
| 62 | **Etsy message notifications active** | Log into Etsy (mobile app or desktop). Confirm notifications are enabled for new messages. On launch day, missed messages within the first 4 hours can result in negative reviews if buyers are confused. | PASS / FAIL |
| 63 | **Standard response templates ready — common queries** | Confirm templates exist for: (a) "I can't find my download" (explain the Etsy digital delivery link in the order confirmation email), (b) "I want a refund" (confirm policy: refunds for delivery failure only, link to the policy page), (c) "I have a question about plant X" (warm response directing to Seedwarden guides and suggesting a purchase if applicable). Templates location: `PHASE_2_CUSTOMER_SUCCESS_FRAMEWORK.md` or `templates/`. | PASS / FAIL |
| 64 | **wanka95@gmail.com checked for any pre-launch inquiries** | Check the email inbox for any pre-launch questions from buyers, press contacts, or partners. Respond to any unanswered messages before May 30. Any press inquiry received before launch should receive a brief acknowledgment and launch date confirmation. | PASS / FAIL |
| 65 | **Etsy auto-reply configured (if supported)** | In Etsy > Shop Manager > Messages, check if an auto-reply can be configured. If available, set an auto-reply for messages received outside business hours (e.g., "Thank you for contacting Seedwarden. We'll respond within 12 hours."). This reduces negative reviews from buyers who message at midnight and feel ignored. | PASS / FAIL |
| 66 | **Digital download troubleshooting guide accessible** | Confirm a brief digital download troubleshooting guide is available for buyers (e.g., as part of the listing FAQ or as a response template). Common issues: buyer cannot find the download link (it is in the Etsy purchase confirmation email and the Etsy "Purchases and Reviews" section), file does not open (recommend Adobe Acrobat or free PDF reader), file appears blank on mobile (some mobile PDF apps have rendering issues — recommend downloading to desktop). | PASS / FAIL |
| 67 | **Review request process documented** | After an order completes, Etsy prompts buyers to leave a review. Confirm you will not manually message buyers asking for reviews (this violates Etsy policy). Confirm the process is to let Etsy's automated review prompt handle this. If any buyer leaves a negative review, respond publicly within 24 hours using a professional, non-defensive tone. | PASS / FAIL |
| 68 | **Response time SLA achievable on launch day** | Confirm you have a specific time block set aside on May 30 for monitoring and responding to messages (recommend: check at 12:00pm, 3:00pm, 6:00pm, and 9:00pm). If you are managing other launch activities during these times, confirm the message check can be completed in 5-10 minutes per slot. | PASS / FAIL |

---

## Section 7: Analytics Activation (Items 69-78)

This section confirms that all monitoring and analytics systems will capture launch-day data from the first hour.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 69 | **GA4 property confirmed active** | Log into Google Analytics > Seedwarden property. Confirm real-time data is flowing (open the GA4 Real-Time report; if you visit the site/landing page in another tab, a real-time visitor should appear within 30 seconds). | PASS / FAIL |
| 70 | **GA4 custom events firing on product pages** | Using the GA4 DebugView (enable debug mode per `etsy-ga4-event-tracking.md`), confirm that key custom events are firing on the relevant pages. At minimum: `view_item` on listing pages, `add_to_cart`, `purchase`. | PASS / FAIL |
| 71 | **Etsy API OAuth token active and not expired** | Run the Etsy API health check from `scripts/etsy_oauth_token.py` (or manually verify at developer.etsy.com). Confirm the access token has not expired. If the token is within 48 hours of expiry, refresh it now. | PASS / FAIL |
| 72 | **Kit analytics — open rate and click rate visible** | Log into kit.co. Open the scheduled launch broadcast. Confirm that the analytics pane shows "Scheduled" and that after the send, open rate and click rate fields will be populated. Run a test send and confirm those fields populate for the test. | PASS / FAIL |
| 73 | **Discord webhook active for real-time alerts** | If the Discord alert webhook is configured (per `TRACK_B_ANALYTICS_SETUP_DISCORD_AND_GA4.md`): send a test message via the webhook URL using curl or the test function in the analytics script. Confirm the test message appears in the correct Discord channel within 10 seconds. | PASS / FAIL |
| 74 | **Google Sheets dashboard formulas calculating correctly** | Open the Phase 2 analytics Google Sheet (per `PHASE_2_ANALYTICS_GOOGLE_SHEETS_TEMPLATE_SPEC.md`). Confirm that all formula cells return values (not `#REF!`, `#VALUE!`, or `#N/A` errors). Enter a test row of data in the raw data tab and confirm the dashboard summary updates accordingly. | PASS / FAIL |
| 75 | **Dashboard accessible to user — correct sharing permissions** | Open the Google Sheet URL in an incognito browser (logged out of all Google accounts). Confirm the sheet is either publicly accessible or confirm you can access it when logged into wanka95@gmail.com specifically. If the sheet requires login and is shared only with a different Google account, update permissions now. | PASS / FAIL |
| 76 | **Etsy Shop Stats baseline recorded** | Log into Etsy Shop Manager > Stats. Record the current values for: (a) shop views (last 30 days), (b) listing views (last 30 days), (c) total orders, (d) total revenue. Record these in `customer-analytics.csv` as the "May 29 baseline" row. This baseline is required to measure Day 1 lift accurately. | PASS / FAIL |
| 77 | **Kit subscriber count baseline recorded** | Log into kit.co > Subscribers. Record the total subscriber count. Record in `customer-analytics.csv` as the "May 29 baseline" row. If count is 0, that is not a blocker — it is the baseline. | PASS / FAIL |
| 78 | **Social follower baselines recorded** | Record follower counts for each active platform (Instagram, TikTok, Pinterest) in `customer-analytics.csv`. If accounts are newly created with 0 followers, record 0. These counts confirm Day 1 follower growth at the end of launch day. | PASS / FAIL |

---

## Section 8: Fulfillment Dry-Run (Items 79-88)

This section verifies the end-to-end order fulfillment workflow for digital products, from purchase through delivery confirmation.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 79 | **Test order placed successfully** | Using a secondary Etsy buyer account (or a friend's account), place a test order on one Phase 2 listing (use the lowest-priced listing to minimize cost). Confirm the checkout process completes without error. If you have already done this in Section 5 (Item 53), this item is covered — do not repeat the purchase, simply reference the prior test. | PASS / FAIL |
| 80 | **Order confirmation email received by buyer** | Confirm the buyer-side order confirmation email arrived within 5 minutes. Open the email. Confirm it contains: (a) the order summary, (b) a "Download your files" button or link, (c) the Etsy logo and correct shop name. | PASS / FAIL |
| 81 | **Digital file download from order confirmation** | Click the download link in the order confirmation email. Confirm the PDF downloads immediately (not redirected to a viewer, not prompted to log into Etsy). Open the downloaded PDF and confirm it is the correct guide, not corrupted, and not missing pages. | PASS / FAIL |
| 82 | **Digital file accessible from Etsy Purchases page** | Log into the buyer Etsy account. Navigate to Purchases and Reviews. Confirm the order appears and a "Download files" button is visible. Click it. Confirm the same PDF downloads correctly from this alternative access path. | PASS / FAIL |
| 83 | **No shipping label generated for digital order** | Confirm in Etsy Shop Manager > Orders that the test digital order does not show a "Print shipping label" button and does not require any shipping action. Digital orders should auto-fulfill immediately. | PASS / FAIL |
| 84 | **Order status auto-updates to "Complete"** | Confirm the test order status in Etsy Shop Manager shows "Complete" without any manual action required. If the order shows "In Progress" for a digital item, investigate the listing configuration — digital listings should not require manual completion. | PASS / FAIL |
| 85 | **Inventory auto-decrement not applicable — confirmed** | Digital products on Etsy do not have inventory counts (they are unlimited). Confirm no quantity limit is set on any Phase 2 listing. In each listing, the "Quantity" field should either be blank, set to a large number, or set to "unlimited" (Etsy's digital listing default). A quantity of 1 will cause the listing to deactivate after the first sale. | PASS / FAIL |
| 86 | **Return and refund workflow tested** | Execute the test refund from Item 55 (or confirm it was already completed there). Confirm the refund appears in Etsy Finances within 24 hours. Confirm the buyer receives a refund confirmation email. | PASS / FAIL |
| 87 | **File re-download confirmed after 48 hours** | Etsy stores purchased digital files for buyers to re-download for a long period. If possible, wait 48 hours and re-download the file from the buyer Purchases page. Confirm the file is still accessible. (If timeline does not permit a 48-hour test before May 30, this item can be marked PASS based on Etsy's documented policy — note this in WORKLOG.md.) | PASS / FAIL |
| 88 | **Packing confirmation workflow not applicable for digital — documented** | Confirm in `PHASE_2_CUSTOMER_SUCCESS_FRAMEWORK.md` that the fulfillment workflow for digital products is documented as: order received → auto-fulfilled by Etsy → no manual steps required → monitor for buyer message if delivery issue. No physical packing checklist is needed. | PASS / FAIL |

---

## Section 9: Contingency Preparation (Items 89-98)

This section confirms that failure modes are planned for and that rollback procedures are documented and accessible.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 89 | **Etsy seller support contact method documented** | Confirm you have the Etsy seller support contact path documented: Help Center > Contact Support (requires login). Etsy does not offer a public phone number — support is via chat or email ticket. Response time on launch day may be 2-8 hours; plan accordingly. | PASS / FAIL |
| 90 | **Kit support contact method documented** | Confirm you have Kit's support contact path: kit.co > Help > Chat with Support (business hours) or support@kit.com (async). If Kit automation fails on launch day, the manual fallback is a Gmail broadcast — this is documented in `LAUNCH_CONTINGENCY_PLAYBOOKS.md`. | PASS / FAIL |
| 91 | **Buffer/Later support contact method documented** | Confirm Buffer (buffer.com/support) or Later (help.later.com) support contact method is documented. If scheduled posts fail on May 30, the fallback is manual posting using the exact caption text from `phase-2-social-content-calendar-60day.md`. | PASS / FAIL |
| 92 | **Rollback procedure — Etsy listing goes live before ready** | Confirm that if an Etsy listing accidentally goes live before 10:00am on May 30, the procedure is: Etsy Shop Manager > Listings > click listing > Edit > change status to Draft > Save. Time to execute: under 2 minutes. | PASS / FAIL |
| 93 | **Rollback procedure — Kit broadcast sends early or to wrong list** | Confirm the procedure if the Kit broadcast fires early: immediately go to Kit > Broadcasts > [Broadcast] > Cancel (if still in "Sending" status). If already sent to the wrong list, send a follow-up correction email within 30 minutes acknowledging the error and providing the correct content. Do not delete the erroneous email from recipient inboxes (you cannot). | PASS / FAIL |
| 94 | **Rollback procedure — payment processor unavailable** | If Etsy Payments goes down on May 30 (rare but possible), the procedure is: (a) do not attempt to take payments outside Etsy (violates Etsy Terms of Service), (b) monitor etsy.com/status for service restoration, (c) post an Instagram Story noting "launching shortly" to hold audience attention, (d) proceed with email and social launches on schedule, then activate Etsy listings once payments are restored. | PASS / FAIL |
| 95 | **Backup email plan — if Kit fails entirely** | Confirm the Gmail manual broadcast procedure from `LAUNCH_CONTINGENCY_PLAYBOOKS.md` is complete: (a) export current Kit subscriber list as CSV (Kit > Subscribers > Export), (b) store CSV at `projects/seedwarden/data/kit-export-[date].csv`, (c) if Kit is down on May 30, send the launch broadcast via Gmail using BCC to the exported list (BCC required; do not CC all subscribers to each other). | PASS / FAIL |
| 96 | **Backup social plan — if Buffer/Later fails** | Confirm the manual posting fallback is ready: the May 30 caption text, hashtags, and images are saved locally (not only in Buffer) at `projects/seedwarden/assets/social/may-30-launch/`. If Buffer fails on May 30, open Instagram, TikTok, and Pinterest directly and post manually using the saved assets and caption text. | PASS / FAIL |
| 97 | **Escalation procedure — who decides if >2 items fail on May 29** | Confirm the delay decision process: if May 29 audit finds more than 2 FAIL items, do not launch on May 30. Set launch date to May 31. On May 31 morning, re-run only the failed items. If all previously-failed items now pass, proceed. If any still fail after the overnight correction window, make a case-by-case decision per `PHASE_2_GO_NO_GO_DASHBOARD.md` Contingency Tree. | PASS / FAIL |
| 98 | **May 29 go/no-go decision logged** | After completing all 100 items on May 29, record the go/no-go decision in WORKLOG.md: date, time, total PASS count, total FAIL count, decision (GO / NO-GO / CONDITIONAL GO with named actions), and any items deferred to launch morning. | PASS / FAIL |

---

## Section 10: May 29 Go/No-Go Decision Gate (Items 99-100)

These are the final two meta-items. They do not verify infrastructure — they verify that the verification itself is complete.

| # | Item | Verification Step | Status |
|---|------|-------------------|--------|
| 99 | **All 100 items reviewed — no items skipped or marked "TBD"** | Scroll through this entire checklist. Confirm every item has a PASS, FAIL, or documented N/A mark. No item may be left blank. Blank items are treated as FAIL for the decision gate. | PASS / FAIL |
| 100 | **Go/no-go decision recorded and launch sequenced** | Count all FAIL items. Apply the decision rule: 0-2 FAILs = GO for May 30. 3+ FAILs = NO-GO; delay to May 31 and correct overnight. Record decision in WORKLOG.md. If GO: open `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md` at 08:00 UTC May 30 and execute in order. If NO-GO: re-run this checklist for FAIL items only on May 31 morning before proceeding. | PASS / FAIL |

---

## Decision Gate Summary

After completing all 100 items, tally results here before closing the session on May 29.

```
Total items reviewed  : _____ / 100
Total PASS            : _____
Total FAIL            : _____
Total N/A             : _____

Starred items (*) FAIL: _____ (list item numbers)

DECISION (circle one): GO  /  NO-GO  /  CONDITIONAL GO

If NO-GO — new launch date: ___________________
Corrective actions required before launch:
  1.
  2.
  3.

Decision recorded in WORKLOG.md at: _________ UTC on May 29, 2026
```

---

## Delay Protocol (If NO-GO Triggered)

If more than 2 items are FAIL on May 29 evening:

1. Do not communicate a delay publicly. Delay nothing that is already scheduled and not yet visible to buyers (Kit broadcast and Buffer posts can be rescheduled in under 10 minutes each).
2. Reschedule the Kit launch broadcast: Kit > Broadcasts > [Broadcast] > Edit > change send time from May 30 12:00pm to May 31 12:00pm > Save.
3. Reschedule all Buffer/Later posts: move each scheduled post forward 24 hours.
4. On May 30, work through FAIL items only. Verify each one. Log corrections in WORKLOG.md.
5. On May 31 morning at 08:00 UTC, re-run the failed items from this checklist. If all now PASS: execute the launch sequence on May 31. If any still FAIL: apply Contingency Tree A from `PHASE_2_GO_NO_GO_DASHBOARD.md` for each category.
6. If the delay extends beyond May 31, the decision framework in `june-6-contingency-path.md` applies.

---

## Quick Reference — Launch Day Timing (May 30)

| Time (UTC) | Action |
|-----------|--------|
| 06:00 | Open this checklist. Run any items that were deferred to launch morning. |
| 08:00 | Run the full QA pass from `MAY_30_LAUNCH_DAY_EXECUTION_PLAN.md` Section 3. Fix any last-minute issues. |
| 09:00 | Record pre-launch baseline metrics in `customer-analytics.csv`. |
| 10:00 | **Etsy Phase 2 listings go live.** Publish all Draft listings from Etsy Shop Manager. Verify in incognito. |
| 12:00 | **Kit launch broadcast sends.** Verify "Sending" status at 12:05 UTC. |
| 14:00 | **Instagram + TikTok launch posts go live** via Buffer. Verify at 14:15 UTC. |
| 15:30 | **Pinterest launch pins go live** via Buffer. Verify at 15:45 UTC. |
| 16:00 | Influencer engagement — comment on or mention 3+ foraging/homesteading accounts. |
| 21:00 | End-of-day metrics log in `customer-analytics.csv`. Respond to all buyer messages. |
