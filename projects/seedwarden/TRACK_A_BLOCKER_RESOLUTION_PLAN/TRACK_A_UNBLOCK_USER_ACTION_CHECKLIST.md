---
title: "Track A Unblock — User Action Checklist"
created: 2026-05-27
status: production-ready — execute today
total-user-time: 45–60 minutes (one session) + 1–5 business days waiting
references:
  - TRACK_A_BLOCKER_TAG_CORRECTION_SPEC.md (full tag correction detail)
  - TRACK_A_BLOCKER_ETSY_VERIFICATION_SPEC.md (full verification detail)
  - TRACK_A_CONTINGENCY_DECISION_TREE.md (Gumroad fallback paths)
  - phase-3-gate-tracker.md (June 22 Phase 3 launch dependency)
---

# Track A Unblock — User Action Checklist

**Execute this checklist in a single session.** Both blockers can be initiated simultaneously and take approximately 45 minutes of your time total. After that, the only remaining item is an external wait (1–5 business days) for Etsy to process your verification.

Track B is unaffected by this checklist and launches May 30 regardless.

---

## Recommended Sequence

Do Etsy verification first, then tag corrections in the same session. The reason for this order is that verification has a mandatory external wait period of 1–5 business days — the clock starts the moment you submit your documents. Starting verification first maximizes the chance of clearance before June 3. Tag corrections are immediate and can be done any time, so they go second.

**Total session time**: 45–60 minutes  
**External wait after session**: 1–5 business days (Etsy verification only)  
**Verification detail**: TRACK_A_BLOCKER_ETSY_VERIFICATION_SPEC.md  
**Tag correction detail**: TRACK_A_BLOCKER_TAG_CORRECTION_SPEC.md

---

## Pre-Session Document Preparation (10 minutes before you start)

Gather these items before opening Etsy. Having them ready prevents mid-verification interruptions that can cause Persona's session to time out.

- [ ] Government-issued photo ID (driver's license front + back, or passport photo page)
- [ ] Device with working front-facing camera (phone preferred for the selfie capture step)
- [ ] Bank routing number (9 digits — from a check or your online banking account details)
- [ ] Bank account number (checking account)
- [ ] Social Security Number (SSN) or EIN if operating as a registered business
- [ ] Legal name exactly as it appears on your ID and bank account
- [ ] Business/mailing address
- [ ] Date of birth
- [ ] Access to your Etsy account email inbox
- [ ] Credit or debit card (for Etsy billing fees, separate from payout account)

Do not start the Etsy verification flow until all items above are on hand.

---

## Phase 1: Etsy Account Verification (20–25 minutes)

**Estimated time**: 20–25 minutes including document gathering  
**External wait after this phase**: 1–5 business days  
**Full detail**: TRACK_A_BLOCKER_ETSY_VERIFICATION_SPEC.md

### Step 1.1 — Check Your Current Account State (2 minutes)

- [ ] Log into etsy.com > profile icon > Sell on Etsy > Shop Manager
- [ ] Check for any of these banners at the top of your dashboard:
  - "Identity verification required" → proceed to Step 1.2
  - "Connect Etsy Payments to start selling" → proceed to Step 1.3
  - "Complete your shop setup" → proceed to Step 1.4
  - "Your shop is under review" → skip to Step 1.5 (verification already in progress)
  - No banners → proceed to Step 1.6 (run the verification test)

**Success signal for Step 1.1**: You know which banner (if any) is present and know which step to go to next.

### Step 1.2 — Identity Verification via Persona (10–15 minutes)

Run this step if "Identity verification required" banner is visible.

- [ ] Navigate to: Account Settings > Security > Identity Verification (or click the banner directly)
- [ ] Click "Verify my identity" or "Start verification"
- [ ] When Persona loads: select your ID type (driver's license or passport)
- [ ] Photograph your ID using Persona's camera interface (front and back if driver's license)
- [ ] Complete the live selfie step — use your front-facing camera, center your face, wait for auto-capture
- [ ] Review captured images and click Submit
- [ ] Confirm you receive a submission confirmation on screen
- [ ] Check your email — Persona/Etsy sends a confirmation email within minutes. Save this email.

**Success signal for Step 1.2**: Confirmation email received. Persona screen shows "submitted" or "under review." Estimated timeline to approval: 1–3 business days (Express review), up to 5 business days (Manual review).

### Step 1.3 — Etsy Payments Enrollment (10 minutes)

Run this step if "Connect Etsy Payments" banner is visible, or run after completing Step 1.2.

- [ ] Navigate to: Shop Manager > Finances > Payment Settings
- [ ] Click "Set up Etsy Payments"
- [ ] Select country: United States
- [ ] Enter bank routing number (9 digits)
- [ ] Enter bank account number (checking account)
- [ ] Select account type: Checking
- [ ] Complete Plaid bank verification:
  - If Plaid instant: log into your bank through Plaid's interface — completes immediately
  - If Plaid micro-deposit: a $0.01 deposit will appear in your bank account within 1–3 business days with a 3-letter code starting with #. Enter that code in Etsy to confirm.
- [ ] Enter your legal name (exactly as on your ID and bank account)
- [ ] Enter your date of birth
- [ ] Enter your SSN (or EIN)
- [ ] Enter your business/mailing address
- [ ] Submit

**Success signal for Step 1.3**: Etsy confirms "Etsy Payments enrolled" or "Bank account connected." If using micro-deposit verification, the success signal is completing the code entry after the deposit arrives.

### Step 1.4 — Shop Setup Completion (5 minutes)

Run this step only if "Complete your shop setup" banner is visible.

- [ ] Navigate to: Shop Manager > Settings > General Settings
- [ ] Confirm shop name is set (not blank or placeholder)
- [ ] Add a shop announcement (1–2 sentences, can be revised later)
- [ ] Click Save
- [ ] Navigate to: Shop Manager > Settings > Policies
- [ ] Set returns/exchanges policy to at minimum: "No returns accepted for digital products"
- [ ] Click Save
- [ ] Navigate to: Shop Manager > Finances > Billing
- [ ] Confirm a credit or debit card is on file for Etsy fees
- [ ] Click Save

**Success signal for Step 1.4**: No more "Complete your shop setup" banner. All Settings sections show saved state.

### Step 1.5 — If "Under Review" Banner Is Showing

This means verification was already submitted in a prior session.

- [ ] Note the date verification was submitted (check email for the Persona confirmation)
- [ ] Calculate: has it been more than 5 business days since submission?
  - If NO: wait. Check again tomorrow and each day after.
  - If YES: escalate to Etsy support (see Step 1.7 below)
- [ ] No other action needed at this stage

**Success signal for Step 1.5**: Etsy sends a "verification approved" email. Banner disappears from Shop Manager.

### Step 1.6 — Verification Test (3 minutes)

Run this step if no banners were visible in Step 1.1.

- [ ] Open a new incognito browser window
- [ ] Navigate to: etsy.com/shop/[your-exact-shop-name]
- [ ] Observe what loads:
  - Shop page loads (even with 0 active listings): account is verified or nearly clear
  - "Shop currently unavailable" or redirect: verification still pending — return to Step 1.2 or 1.3

**Success signal for Step 1.6**: Your shop page is visible in an incognito browser.

### Step 1.7 — Escalation: If Verification Delayed Beyond 5 Business Days

- [ ] Navigate to: help.etsy.com > Contact Us > topic "Shop verification"
- [ ] Send the escalation message (copy this):
  > "I submitted my identity verification documents on [date]. I have not yet received a confirmation or outcome. My shop name is [your shop name] and my account email is [your email]. I have products ready to publish and need to understand the current review timeline. Please advise on the status."
- [ ] Log the support ticket number and date in WORKLOG.md
- [ ] Expected response: 24–48 hours

**Success signal for Step 1.7**: Etsy support responds with a clearance date estimate or immediate approval.

### Step 1.8 — Log Verification Submission in WORKLOG.md

Do this immediately after submitting verification documents, even before the review is complete.

- [ ] Open `/home/awank/dev/SuperClaude_Framework/projects/seedwarden/WORKLOG.md`
- [ ] Add entry: "Track A Blocker 2 — Etsy account verification submitted [date and time]"
- [ ] Note: expected clearance date based on submission date (add 1–5 business days)

---

## Phase 2: Tag Corrections (15 minutes)

**Estimated time**: 15 minutes  
**External wait**: None — corrections take effect immediately on save  
**Full detail**: TRACK_A_BLOCKER_TAG_CORRECTION_SPEC.md

Do this in the same Etsy session immediately after completing Phase 1 steps.

### Step 2.1 — Companion Planting Chart: Full Tag Set Replacement (5 minutes)

- [ ] In Etsy Shop Manager > Listings, find "Companion Planting Chart" (Draft)
- [ ] Click to edit the listing
- [ ] Scroll to the Tags field
- [ ] Delete all existing tags (click X next to each)
- [ ] Enter these 13 tags exactly, pressing Enter after each one:
  1. companion planting
  2. garden planning
  3. vegetable garden
  4. organic gardening
  5. plant combinations
  6. pest control
  7. garden chart
  8. raised bed garden
  9. square foot garden
  10. permaculture
  11. homestead garden
  12. garden printable
  13. digital download
- [ ] Confirm 13 tags are present in the field
- [ ] Click "Save and continue" (do NOT click Publish — keep as Draft)

**Success signal**: 13 tags visible in the Tags field. No tag exceeds 20 characters. Listing saved as Draft.

### Step 2.2 — Survival Garden Regional Plans: Single Tag Swap (2 minutes)

- [ ] In Etsy Shop Manager > Listings, find "Survival Garden Regional Plans" (Draft)
- [ ] Click to edit the listing
- [ ] Scroll to the Tags field
- [ ] Locate the tag `self sufficient garden` — click X to remove it
- [ ] In the tag input field, type `self-sufficient` and press Enter
- [ ] Confirm `self-sufficient` is now in the tag list
- [ ] Confirm `self sufficient garden` is absent
- [ ] Confirm all other tags for this listing are unchanged
- [ ] Click "Save and continue"

**Success signal**: `self-sufficient` present, `self sufficient garden` absent. All other tags unchanged. Listing saved.

### Step 2.3 — Zone-by-Zone Seed Starting Calendar: Single Tag Swap (2 minutes)

- [ ] In Etsy Shop Manager > Listings, find "Zone-by-Zone Seed Starting Calendar" (Draft)
- [ ] Click to edit the listing
- [ ] Scroll to the Tags field
- [ ] Locate the tag `veggie planting guide` — click X to remove it
- [ ] In the tag input field, type `veggie plant guide` and press Enter
- [ ] Confirm `veggie plant guide` is now in the tag list
- [ ] Confirm `veggie planting guide` is absent
- [ ] Confirm all other tags for this listing are unchanged
- [ ] Click "Save and continue"

**Success signal**: `veggie plant guide` present, `veggie planting guide` absent. All other tags unchanged. Listing saved.

### Step 2.4 — Tag Verification Check (3 minutes)

Do a quick pass after all three corrections to confirm nothing was inadvertently changed:

- [ ] Click into Companion Planting Chart listing — confirm exactly 13 tags, none appears truncated
- [ ] Click into Survival Garden Regional Plans — confirm `self-sufficient` present
- [ ] Click into Zone-by-Zone Seed Starting Calendar — confirm `veggie plant guide` present
- [ ] No other listings were opened or modified during this session

### Step 2.5 — Log Tag Corrections in WORKLOG.md

- [ ] Open WORKLOG.md
- [ ] Add entry: "Track A Blocker 1 — tag corrections applied [date]"

**Success signal for Phase 2**: All three WORKLOG entries present. All three listings show correct tags. Estimated time from completion to resolution: 0 additional days (tags are correct the moment you save them).

---

## Phase 3: Post-Verification — Publish Phase 1 Listings (When Etsy Clears)

This phase runs after Etsy verification completes (1–5 business days after Phase 1 above). Do not start Phase 3 before receiving Etsy's clearance email.

**Estimated time**: 2–3 hours (publishing 21 listings)  
**Trigger**: Etsy sends "verification approved" email AND "Publish" button is active on Draft listings

### Step 3.1 — Confirm Publish-Ready State (5 minutes)

- [ ] Log into Etsy Shop Manager
- [ ] Confirm no verification banners are present
- [ ] Open any one Draft listing and confirm the "Publish" button is active (not grayed out)
- [ ] Run the incognito shop page test: etsy.com/shop/[your-shop-name] loads in an incognito window

If all four are true: proceed to Step 3.2.

### Step 3.2 — Publish All 21 Phase 1 Listings (2–3 hours)

- [ ] In Shop Manager > Listings, publish each of the 21 Phase 1 Draft listings one by one
- [ ] After publishing each listing, confirm its status changes from "Draft" to "Active" (green dot)
- [ ] After all 21 are published, confirm the public shop page (etsy.com/shop/[your-shop-name]) shows listings

### Step 3.3 — Post-Launch Validation (30 minutes)

- [ ] Search Etsy for 2–3 of your product titles (e.g., "companion planting chart") — confirm your listings appear in results
- [ ] Run a test purchase on your lowest-priced listing using a secondary account or trusted contact — confirm the PDF delivers automatically via Etsy Digital Downloads
- [ ] If PDF delivery fails: go to Etsy > listing editor > "Files" section — confirm the PDF is uploaded and attached

### Step 3.4 — Create SEEDWARDEN15 Coupon

- [ ] Navigate to: Etsy > Marketing > Sales and Coupons > Create a coupon
- [ ] Code: SEEDWARDEN15
- [ ] Discount type: Percentage off
- [ ] Discount amount: 15%
- [ ] Minimum order: none
- [ ] Expiration: no expiry
- [ ] Apply to: all items
- [ ] Save and activate the coupon

### Step 3.5 — Update Social Media Bios

- [ ] Update Instagram bio with Etsy shop URL
- [ ] Update Facebook page/profile with Etsy shop URL
- [ ] Update Pinterest profile with Etsy shop URL

### Step 3.6 — Log Phase 1 Launch in WORKLOG.md

- [ ] Add entry: "Track A Phase 1 live on Etsy — [date]. All 21 listings active. SEEDWARDEN15 coupon created."

---

## Escalation Paths

| Problem | First step | Second step | Escalation path |
|---|---|---|---|
| Tag correction saves but tag appears truncated | Delete the tag, retype it manually (do not paste), save again | If still truncated: character-count the tag manually (must be ≤20 chars including spaces) | Tag correction spec: TRACK_A_BLOCKER_TAG_CORRECTION_SPEC.md Section 2 |
| Etsy verification not cleared after 5 business days | Contact Etsy support (help.etsy.com > Contact Us) with ticket request | If support does not resolve within 2 business days: activate Gumroad interim (see below) | TRACK_A_BLOCKER_ETSY_VERIFICATION_SPEC.md Section 7 |
| Persona selfie not accepting (camera not working) | Switch to mobile device — use phone front camera instead of laptop webcam | If Persona still fails: request Manual review option instead of Express | TRACK_A_BLOCKER_ETSY_VERIFICATION_SPEC.md Section 4 |
| Plaid instant bank verification fails | Switch to micro-deposit verification (takes 1–3 days for the deposit to arrive) | If micro-deposit also fails: contact your bank to confirm routing/account numbers | TRACK_A_BLOCKER_ETSY_VERIFICATION_SPEC.md Section 5 |
| All Etsy blockers delayed past June 3 | Activate Gumroad as interim channel | Publish Phase 1 products on Gumroad (15-minute setup) | TRACK_A_CONTINGENCY_DECISION_TREE.md (Gumroad setup checklist) |

---

## June 22 Phase 3 Launch Gate — What Track A Unblock Affects

Phase 3 (medicinal herbs, June 22 launch target) is gated on two demand-signal metrics measured from Track B's May 30 launch, not on Track A's unblock date:

| Gate | Threshold | Current status (Phase 1 baseline) | Monitoring window |
|---|---|---|---|
| Forager cohort | ≥20% of Track B buyers | 21.3% (cleared) | May 30 – June 20, weekly checks |
| Native Plants conversion | ≥1.5% view-to-sale rate | 2.24% (cleared) | May 30 – June 20, weekly checks |

Both gates are currently cleared. The June 22 decision point is whether these rates hold through the Track B launch period. Track A being unblocked or still blocked does not change these numbers.

However, Track A being live on Etsy before June 22 provides a secondary benefit: it completes the shop catalog (21 additional products visible), which increases overall shop credibility and may marginally improve Track B conversion rates. This is a "nice to have," not a gate requirement.

**Latest date Track A unblock must complete to support Phase 3**: There is no hard deadline from Track A to Phase 3. Phase 3 proceeds on June 22 if the forager cohort and conversion gates are cleared, regardless of Track A status.

**Practical implication**: If Etsy verification clears by June 3 (worst case from a May 27 submission), Phase 1 can be published before the May 30 Track B launch or immediately after. Either timing supports the June 22 Phase 3 gate fully.

---

## Post-Unblock Validation — Track A Launch-Ready Checklist

Run this checklist after both blockers are resolved and Phase 1 is live:

- [ ] All 21 Phase 1 listings are Active (green dot) in Etsy Shop Manager
- [ ] Public shop page (etsy.com/shop/[your-shop-name]) shows at least the 21 Phase 1 listings
- [ ] No Etsy account warnings or banners present in Shop Manager
- [ ] Test purchase confirmed: PDF delivered automatically via Etsy Digital Downloads
- [ ] SEEDWARDEN15 coupon active (15% off, no minimum, no expiry)
- [ ] Social media bios updated with Etsy shop URL
- [ ] WORKLOG.md entries logged: Blocker 1 (tag corrections), Blocker 2 (verification), Phase 1 launch date
- [ ] PROJECTS.md Track A status updated to "Active — Phase 1 live on Etsy, [date]"

When all eight items above are complete, Track A is fully unblocked and operational.

---

## Timeline Summary

| Milestone | Date (from May 27 start) |
|---|---|
| Documents gathered, ready to begin | May 27 (today) |
| Phase 1 (verification submitted) complete | May 27 |
| Phase 2 (tag corrections) complete | May 27 (same session) |
| Verification cleared — best case (1 business day) | May 28 |
| Verification cleared — typical (2–3 business days) | May 29–30 |
| Verification cleared — worst case (5 business days) | June 3 |
| Phase 1 listings published (day verification clears) | May 28 – June 3 |
| Track B May 30 launch | Not affected — no dependency |
| June 22 Phase 3 gate decision | Not affected — demand-data driven |

---

*Cross-references: TRACK_A_BLOCKER_TAG_CORRECTION_SPEC.md (full tag detail + character counts); TRACK_A_BLOCKER_ETSY_VERIFICATION_SPEC.md (full verification flow + Persona documents + Etsy Payments setup); TRACK_A_CONTINGENCY_DECISION_TREE.md (Gumroad fallback); phase-3-gate-tracker.md (June 22 gate criteria); TRACK_A_BLOCKER_RESOLUTION.md (original blockers document, Sessions 700s).*
