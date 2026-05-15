---
title: "Track A Blocker Resolution Protocol"
project: seedwarden
created: 2026-05-15
status: active — both blockers open (user action required)
references:
  - TRACK_A_BLOCKER_RESOLUTION.md (specific tag correction steps and Etsy verification checklist)
  - TRACK_A_CONTINGENCY_LAUNCH_PLAN.md (May 20 decision trigger and Option B/C paths)
  - TRACK_B_USER_GATES.md (May 15–28 execution window)
  - PHASE_2_EXECUTION_DAILY_TRACKER_MAY_15_30.md (parallel Track B activity)
  - PHASE_2_GO_NO_GO_DASHBOARD.md (May 29 go/no-go checkpoint)
---

# Track A Blocker Resolution Protocol

**Lead finding:** Both Track A blockers are solvable within 30 minutes of user time plus a 1–5 day Etsy verification wait. As of May 15, the most important action is initiating Etsy account verification today — the verification clock starts the moment documents are submitted, and waiting even one additional day compresses the window before the May 29 go/no-go check. The tag corrections are a 15-minute copy-paste operation that can happen alongside verification. Track B (May 15–28 execution gates) proceeds in parallel regardless of Track A status.

---

## Part 1: Current State Assessment

### 1.1 What Each Blocker Actually Is

**Blocker 1: Tag Corrections**

Three specific Etsy listings have tag sets requiring correction before upload. These are not editorial or content changes — they are character-count compliance fixes and keyword precision improvements. All three corrections are already documented to the exact replacement level in `TRACK_A_BLOCKER_RESOLUTION.md`.

| Listing | Issue | Correction Required | Estimated Time |
|---------|-------|---------------------|----------------|
| Companion Planting Chart | Existing tag set needs replacement | Apply the documented 13-tag set | 5 minutes |
| Survival Garden Regional Plans | `self sufficient garden` (21 chars) violates Etsy 20-char limit | Replace with `self-sufficient` (15 chars) | 2 minutes |
| Zone-by-Zone Seed Starting Calendar | `veggie planting guide` (borderline 20 chars, inconsistently accepted) | Replace with `veggie plant guide` (18 chars, stronger keyword) | 2 minutes |

Total estimated time: 15 minutes.

These corrections are not blocking because the tags are wrong in some complex sense — they are blocking because uploading with character-count violations causes Etsy to silently truncate tags, which wastes the listing's keyword authority from Day 1. The cost of fixing this post-launch is regenerating organic ranking from scratch. Fix it now.

**No other listings require tag corrections.** The 18 remaining Phase 1 products are upload-ready as-is.

**Blocker 2: Etsy Account Verification**

Etsy now requires mandatory identity verification for all sellers before listings can be published (made visible to buyers). This requirement became mandatory for new sellers in mid-2025 and applies to Etsy Payments enrollment. The verification uses Persona (a third-party identity verification service) and requires:

- A government-issued ID (driver's license or passport): photo of front and back
- A selfie (Persona compares biometric data from ID photo and selfie)
- Bank account details (routing number + account number)
- Tax information (SSN or EIN for US sellers)

The verification process itself takes 10 minutes to submit. Etsy's review period after submission is typically 1–5 business days.

**Why this is blocking**: Even if all 21 product listings are in Draft status and fully prepared, they cannot be published (visible to buyers) until Etsy Payments is active and verification is complete. Attempting to publish before verification results in listings that appear live on the seller side but are invisible to buyers.

**Time to resolve**: 10 minutes of user submission + 1–5 business days Etsy review. Total real-world time to unblock: 1–5 business days from today.

### 1.2 Estimated Resolution Timeline

| Blocker | User Action Time | External Wait | Unblocked By |
|---------|-----------------|---------------|--------------|
| Blocker 1: Tag corrections | 15 minutes | None | Same day as action |
| Blocker 2: Etsy verification | 10 minutes + document gathering (~20 min total) | 1–5 business days | May 16–22 (if initiated May 15) |

**If both actions are taken today (May 15)**:
- Blocker 1 cleared: May 15 (same day)
- Blocker 2 cleared: May 16–22 (1–5 business days)
- Upload window available: May 16–22
- Phase 1 live: May 16–22 — well ahead of the May 29 go/no-go and the May 30 launch target

**If actions are delayed to May 19**:
- Blocker 1 cleared: May 19
- Blocker 2 cleared: May 20–26
- This is within the acceptable window but eliminates the buffer before May 29 go/no-go

**Hard deadline**: Both blockers must be at least initiated by May 19. If verification is submitted by May 19, Etsy's 5-business-day window puts the latest possible clearance at May 28 — one day before the go/no-go checkpoint. This is tight but viable.

---

## Part 2: Blocker 1 — Tag Corrections Execution

### 2.1 Which Files Need Updates

The tag corrections are applied directly in Etsy's listing draft interface, not in local project files. There are no local file changes required — the correct tag sets are already documented in `TRACK_A_BLOCKER_RESOLUTION.md` and reproduced below for convenience.

The three affected listings are all in Etsy > Shop Manager > Listings (as Drafts). No local `products/` or `data/` files need modification for this correction.

### 2.2 The Tag Standard

Etsy's tagging rules:
- Maximum 13 tags per listing
- Maximum 20 characters per tag (including spaces)
- Tags are case-insensitive; title case has no SEO benefit
- Duplicate tags across listings are fine (and often appropriate for related products)
- Tags should reflect actual search terms buyers use, not internal categorization names

The specific corrections below comply with all four rules and improve keyword match precision for the affected listings.

### 2.3 Exact Corrections (Copy-Paste Ready)

**Correction 1: Companion Planting Chart**

In Etsy listing draft for "Companion Planting Chart", replace the full current tag set with exactly these 13 tags:

```
companion planting
garden planning
vegetable garden
organic gardening
plant combinations
pest control
garden chart
raised bed garden
square foot garden
permaculture
homestead garden
garden printable
digital download
```

Verify each tag is 20 characters or fewer before saving. "companion planting" = 18 characters (within limit). "raised bed garden" = 17 characters. All tags in this set are within the limit.

**Correction 2: Survival Garden Regional Plans**

In Etsy listing draft for "Survival Garden Regional Plans":
- Find tag: `self sufficient garden`
- Delete it
- Add: `self-sufficient`
- All other tags remain unchanged

**Correction 3: Zone-by-Zone Seed Starting Calendar**

In Etsy listing draft for "Zone-by-Zone Seed Starting Calendar":
- Find tag: `veggie planting guide`
- Delete it
- Add: `veggie plant guide`
- All other tags remain unchanged

### 2.4 Script Auto-Correction Assessment

**Can any tags be auto-corrected via a script?** No, and here is why: Etsy's tag interface does not expose a public API for bulk tag modification to third-party scripts. The listing data lives in Etsy's internal systems, not in local project files. The three corrections above require manual navigation to each listing draft in Etsy's web interface.

**Is there a local file that contains the tags that could be auto-corrected as a pre-upload step?** Checking the project structure: if tag data is stored in any local `products/` JSON or CSV files before the Etsy upload step, those files could be scripted. However, based on `ETSY_PHASE_1_UPLOAD_CHECKLIST.md` and `UPLOAD_READY_CHECKLIST.md`, the tag corrections apply to Etsy draft listings that are already partially uploaded — meaning the tags exist in Etsy's system, not in local editable files.

**Manual verification required**: All three corrections must be verified manually by the user in the Etsy interface.

### 2.5 Verification Checklist

After applying corrections:

- [ ] Companion Planting Chart: 13 tags present, all visible in Etsy tag field, no tag exceeds 20 characters
- [ ] Survival Garden Regional Plans: `self-sufficient` present, `self sufficient garden` absent
- [ ] Zone-by-Zone Seed Starting Calendar: `veggie plant guide` present, `veggie planting guide` absent
- [ ] No other listings were modified during this session
- [ ] Log in WORKLOG.md: "Track A Blocker 1 — tag corrections applied [date]"

---

## Part 3: Blocker 2 — Etsy Account Verification

### 3.1 What Type of Verification Is Required

Based on Etsy's current 2025–2026 requirements, this is a two-component verification:

**Component A: Identity Verification (Persona)**
Etsy uses Persona (a third-party identity verification service) for biometric identity confirmation. Required documents:
- Government-issued photo ID: driver's license (front and back) or passport (photo page)
- Live selfie via Persona's interface (not an uploaded photo — it is an in-browser or in-app capture)

This is mandatory for all new US sellers as of June 2025.

**Component B: Etsy Payments Enrollment**
To receive payouts and publish listings, sellers must enroll in Etsy Payments:
- Bank account information: routing number + account number
- Tax information: SSN (for individuals/sole proprietors) or EIN (for business entities)
- Business address

Both components must be complete before listings can go live.

### 3.2 Pre-Verification Documentation Checklist

Gather the following before opening the Etsy verification interface. Having these ready eliminates mid-verification delays:

- [ ] Government-issued photo ID (driver's license front and back, or passport photo page). Must show: full name, date of birth, expiration date.
- [ ] Bank routing number and account number (for Etsy Payments payout account)
- [ ] Social Security Number (SSN) or EIN for tax reporting
- [ ] Business address (your address if operating as sole proprietor)
- [ ] Device with front-facing camera (for selfie via Persona — phone or laptop with webcam)
- [ ] Email access (Etsy sends confirmation and status updates to registered email)

### 3.3 Verification Steps

**Step 1: Check current account status (2 minutes)**

Log in to Etsy > profile icon > Sell on Etsy > Shop Manager.

Look for any of these banners at the top of Shop Manager:
- "Your shop is under review"
- "Identity verification required"
- "Complete your shop setup"
- "Connect Etsy Payments to start selling"

If no banner is visible, proceed to Step 3 (verification test) before assuming the account is clear.

**Step 2: Complete verification (10–15 minutes with documents ready)**

For "Identity verification required":
- Navigate to: Etsy > Account Settings > Security > Identity Verification
- Select your ID type (driver's license or passport)
- Upload photos of your ID (front and back if driver's license)
- Complete the live selfie via Persona's in-browser interface
- Submit. You will receive an email from Persona/Etsy within minutes confirming submission.

For "Connect Etsy Payments":
- Navigate to: Etsy > Shop Manager > Finances > Payment Settings
- Click "Set up Etsy Payments"
- Enter bank routing number and account number
- Enter SSN or EIN
- Confirm business type (individual/sole proprietor or registered business)
- Submit.

For "Complete your shop setup":
- Navigate to: Etsy > Shop Manager > Settings > General Settings
- Verify all required fields are complete: shop name, shop announcement, shop policies (returns, exchanges), billing information
- Save each section before moving to the next.

**Step 3: Verification test after submission (3 minutes)**

After submitting, verify submission is in progress:
- Navigate to your shop public URL: etsy.com/shop/[your-shop-name]
- Open this URL in an incognito browser window
- If the shop page loads and shows a shop (even with no active listings): identity verification is either complete or in progress (listings will become publishable when verification clears)
- If the page shows "This shop is currently unavailable": either verification is pending OR the shop was not properly set up

**Step 4: If verification is still pending after 5 business days**

Contact Etsy support directly:
- URL: help.etsy.com > Contact Us > "Shop verification" topic
- Message: "I submitted my identity verification documents on [date] and have not yet received confirmation. My shop name is [shop name]. I have products ready to publish and need to understand the current timeline."
- Expected response time: 24–48 hours

### 3.4 Estimated Timeline

| Action | Date (if executed May 15) | Date (if delayed to May 19) |
|--------|--------------------------|----------------------------|
| Submit verification documents | May 15 | May 19 |
| Verification complete (best case: 1 business day) | May 16 | May 20 |
| Verification complete (typical: 2–3 business days) | May 19–20 | May 22–23 |
| Verification complete (worst case: 5 business days) | May 22 | May 26 |
| Last viable date for Phase 1 upload before May 30 | May 28 | May 28 |
| Buffer before go/no-go (May 29) | 6–13 days | 2–8 days |

**Recommendation**: Submit verification today (May 15). Each day of delay reduces the buffer before the May 29 go/no-go checkpoint without any upside.

---

## Part 4: Unblocking Sequence

### 4.1 Day-by-Day Execution

**Day 1 (May 15) — Today: Initiate both blockers in parallel**

Order of operations (both can be done in a single 45-minute session):

1. Open Etsy Shop Manager. Navigate to identity verification / Etsy Payments setup. Submit all documents. (20–25 minutes including document gathering)
2. In the same Etsy session, navigate to Listings > Companion Planting Chart draft. Apply the 13-tag correction. Save. (5 minutes)
3. Navigate to Survival Garden Regional Plans draft. Remove `self sufficient garden`, add `self-sufficient`. Save. (2 minutes)
4. Navigate to Zone-by-Zone Seed Starting Calendar draft. Remove `veggie planting guide`, add `veggie plant guide`. Save. (2 minutes)
5. Log completions in WORKLOG.md:
   - "Track A Blocker 1 — tag corrections applied 2026-05-15"
   - "Track A Blocker 2 — Etsy account verification submitted 2026-05-15"
6. Note confirmation email from Persona/Etsy in inbox. This is the timestamp for tracking the 1–5 day window.

**Days 2–3 (May 16–17): Track B execution proceeds; no Track A action needed**

Track B gates (May 15–28) are executing in parallel. No Track A action is required during this window. Monitor Etsy email for verification completion notification.

**If verification email arrives on Days 2–3**: Proceed immediately to Phase 1 upload (Section 4.2 below). Do not wait until the scheduled upload window.

**Days 3–5 (May 17–19): Verification window**

No action required unless verification has not cleared by May 19. If not cleared by May 19: contact Etsy support (Step 4 above). Provide submission timestamp and request estimated completion date.

**Days 6–10 (May 20–24): Upload window opens**

When verification clears:
1. Run Phase 1 upload session: ETSY_PHASE_1_UPLOAD_CHECKLIST.md. Estimated 2–3 hours for all 21 listings.
2. Confirm all listings are Active (green dot in Shop Manager, not Draft).
3. Run a test purchase on a lower-cost listing using a secondary account or trusted contact. Confirm PDF delivers automatically via Etsy Digital Downloads.
4. Create the SEEDWARDEN15 coupon: Etsy > Marketing > Sales and Coupons > 15% off, no minimum, no expiry.
5. Update social media bios to include the Etsy shop URL.
6. Log: "Track A Phase 1 live — [date]" in WORKLOG.md and `customer-analytics.csv`.

**Day 14 (May 29): Go/no-go checkpoint**

The May 29 go/no-go (per `PHASE_2_GO_NO_GO_DASHBOARD.md`) incorporates Track A status. At this point:
- If Track A is live: both Phase 1 (Track A) and Phase 2 (Track B) launch together on May 30. Full parallel operation.
- If Track A verification is still pending (highly unlikely if submitted May 15, but possible if submitted late): activate the interim channel fallback (Section 5 below) and proceed with Phase 2-only launch on May 30.

---

## Part 5: Interim Channel Fallback (If Verification Exceeds May 28)

If Etsy verification has not cleared by May 28, Track A does not hold back Track B. Phase 2 launches on May 30 regardless. Track A follows whenever verification clears. However, if there is user demand to begin selling Phase 1 products before Etsy verification completes, two interim channels are available.

### 5.1 Gumroad (Primary Fallback)

Gumroad is the fastest viable digital product sales channel that does not require pre-launch identity verification.

- **Setup time**: 15–30 minutes (create account, upload PDF, set price)
- **Transaction fee**: 10% of sale price (vs. Etsy's 6.5% transaction + ~3% payment processing = ~9.5% total — Gumroad is slightly more expensive per sale)
- **Identity verification**: Gumroad requires bank account and tax information for payout, but does not require pre-launch ID verification before listings go live
- **Customer experience**: Direct checkout via gumroad.com/[your-shop]. PDF delivery is automated.
- **Limitation**: No organic discovery. Gumroad does not have a marketplace. All traffic must come from your social media or email list.

**If activating Gumroad as interim**:
1. Create a Gumroad account (gumroad.com/signup)
2. Upload a single test product (the Companion Planting Chart or Zone-by-Zone Calendar — highest cross-appeal items)
3. Post the Gumroad link in the Phase 2 social media launch announcement
4. Migrate all customers to Etsy once verification clears — Gumroad to Etsy migration does not require customer action (just update the links)

### 5.2 Direct Sales via Social Media (Secondary Fallback)

If Gumroad setup is also blocked (unlikely, but included for completeness):
- Accept payment via Venmo or PayPal Friends & Family
- Deliver PDFs manually via email
- This is not a scalable system, but it can generate revenue and reviews from the first 5–10 buyers while Etsy verifies

**Recommendation**: Only use direct sales for buyers who ask during the launch window. Do not actively promote a manual delivery workflow — it creates support overhead.

### 5.3 Fallback Decision Logic

```
May 29 go/no-go: Is Etsy verification complete?
        |
    YES / NO
    |       |
    v       v
Phase 1  Has user received
live.    demand for Phase 1
Proceed  products before
normally verification clears?
              |
          YES / NO
          |       |
          v       v
      Activate   Proceed with
      Gumroad    Phase 2 only.
      interim.   Phase 1 follows
      Monitor    when verification
      Etsy for   clears.
      clearance.
```

---

## Part 6: Track A + Track B Parallelization

### 6.1 What Track B Is Doing During the Blocker Resolution Window

Track B (May 15–28 user gates per `TRACK_B_USER_GATES.md`) is executing independently. The following Track B actions proceed regardless of Track A status:

- Social account setup verification (complete or near-complete as of May 13 per `TRACK_B_READINESS_REPORT_MAY_13.md`)
- Canva zone card production (ongoing via `CANVA_ZONE_CARD_BATCH_WORKFLOW.md`)
- Kit email automation setup (`KIT_SETUP_NOTES.md`)
- Bundle E final QA (`BUNDLE_E_QA_CHECKLIST.md`)
- Photo shoot execution (if not yet completed)

None of these have any dependency on Track A. Track B gates can all be completed before May 28 regardless of when Etsy verification clears.

### 6.2 The May 30 Launch Scenarios

| Scenario | Track A Status | Track B Status | May 30 Outcome |
|----------|---------------|----------------|----------------|
| Full launch | Etsy verified + tags corrected + Phase 1 uploaded | All gates complete | Phase 1 (21 listings) + Phase 2 launch together. Maximum Day 1 product catalog. |
| Track B only | Etsy verification pending | All gates complete | Phase 2 launches May 30. Phase 1 follows within days of verification clearing. Revenue begins from Phase 2 products. |
| Delayed full launch | Etsy verified after May 30 | All gates complete | Phase 2 live May 30. Phase 1 added to live shop same day verification clears — no rebuild required, just publish drafts. |
| Partial launch (Gumroad) | Etsy pending, Gumroad active | All gates complete | Phase 2 live May 30. Phase 1 via Gumroad. Migrate to Etsy when verification clears. |

All scenarios result in revenue beginning on May 30. The difference is only whether Phase 1 products are on Etsy or on a temporary interim channel.

---

## Part 7: Success Criteria

### 7.1 Track A Completion (Full Success)

All of the following are true:
- [ ] All three tag corrections applied and verified in Etsy
- [ ] Etsy account identity verification complete (no pending banners in Shop Manager)
- [ ] Etsy Payments connected (bank account and tax info on file)
- [ ] All 21 Phase 1 listings Active (not Draft) in Etsy Shop Manager
- [ ] Test purchase verified (automated PDF delivery confirmed)
- [ ] SEEDWARDEN15 coupon created
- [ ] Phase 1 live date logged in WORKLOG.md

### 7.2 Conditional Success (Verification Pending)

All of the following are true:
- [ ] All three tag corrections applied and verified
- [ ] Etsy verification submitted (pending clearance)
- [ ] Gumroad activated with at least 1 Phase 1 listing live (or decision made to wait for Etsy)
- [ ] Phase 2 (Track B) proceeds to May 30 launch without interruption
- [ ] Phase 1 Etsy upload queued and ready to execute same day verification clears

### 7.3 Failure State (Postpone Track A to June)

This state requires a user decision:
- User unable to initiate Etsy verification by May 19 (hard deadline for within-May clearance)
- AND user does not want to use Gumroad as interim channel
- **Decision**: Postpone Phase 1 Etsy launch to June 1–7. Phase 2 launches May 30 as planned. Phase 1 follows when Etsy verification clears in June.
- **Revenue impact**: Minimal. Phase 1 products are evergreen — a 1–2 week delay does not compress the product's market opportunity.
- **Action required**: Log postponement decision in WORKLOG.md; update PROJECTS.md Track A status; proceed with Phase 2 launch.

---

## Part 8: Advisory — Hunting Manual Slug

This is a non-blocking documentation note carried forward from `TRACK_A_BLOCKER_RESOLUTION.md`.

**Correct slug**: `hunting-fishing-trapping-field-manual` (with `-field-` in the middle)

**Files confirmed using the correct slug**: all three mockup images in `projects/seedwarden/mockups/`.

**When it matters**: Only at upload time, when naming the exported Etsy listing images for slots 4 and 5 of this specific listing. Use the correct slug at that moment. No action required now.

---

*Created: 2026-05-15. Both blockers are user-action items — no agent work is required or possible until user completes verification submission and tag corrections. Track B (Phase 2) is fully independent and executes May 15–30 on its own gate sequence. Recommended immediate action: initiate Etsy verification today, apply tag corrections in the same session.*

*Sources: Etsy Help Center identity verification documentation; Persona/Etsy integration guide; Etsy Payments Policy (updated February 12, 2026); Etsy seller policy changes 2026 (cedcommerce.com analysis); SkladUSA mandatory verification overview; TRACK_A_BLOCKER_RESOLUTION.md (Sessions 700s, May 2026).*
