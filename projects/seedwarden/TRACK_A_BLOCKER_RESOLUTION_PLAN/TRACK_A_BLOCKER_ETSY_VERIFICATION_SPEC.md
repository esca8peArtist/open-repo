---
title: "Track A Blocker 2 — Etsy Account Verification Specification"
created: 2026-05-27
status: production-ready — user action required
effort: 30 minutes user action + 1–5 business days external wait
references:
  - TRACK_A_BLOCKER_RESOLUTION.md (verification checklist, Sessions 700s)
  - TRACK_A_RESOLUTION_PROTOCOL.md (Persona flow, May 15)
  - Etsy Help Center identity verification documentation (2026)
---

# Track A Blocker 2: Etsy Account Verification Specification

**Blocker type**: User action + external wait (Etsy processing)  
**User effort**: 30 minutes (document gathering + submission)  
**External wait**: 1–5 business days (Etsy/Persona review)  
**Hard dependency**: Listings cannot be published to Etsy buyers until this is complete  
**Status as of May 27**: Unresolved — current account state unknown (check Shop Manager)

---

## 1. Why This Is Blocking

Etsy requires all sellers to complete identity verification before any listings can be made publicly visible (published). This requirement became mandatory for new US sellers in June 2025 and applies universally in 2026. The verification has two components that must both be complete:

**Component A — Identity Verification via Persona**: Etsy partners with Persona, a third-party biometric identity service. Persona compares your government-issued photo ID against a live selfie. Without this, Etsy's fraud controls prevent listing publication.

**Component B — Etsy Payments Enrollment**: To receive payouts and publish listings for sale, your Etsy Payments account must be active. This requires connecting a bank account and providing tax information (SSN or EIN for US sellers).

The consequence of incomplete verification is specific and important: listings can exist in Draft status in your Shop Manager and appear live from your account view, but they are invisible to buyers. Etsy does not display unverified listings in search or on your public shop page.

---

## 2. Current Account State — Check First

Before taking any action, determine which verification state you are currently in. This determines exactly which steps remain.

**Action: Log into Etsy > profile icon > Sell on Etsy > Shop Manager.**

Look for banners at the top of the Shop Manager dashboard. Match your screen to one of these states:

| What you see | What it means | What to do |
|---|---|---|
| Banner: "Identity verification required" | Persona ID verification not submitted | Go to Section 4 (Identity Verification) |
| Banner: "Connect Etsy Payments to start selling" | Bank account and tax info not entered | Go to Section 5 (Etsy Payments Setup) |
| Banner: "Complete your shop setup" | Shop profile fields incomplete | Go to Section 6 (Shop Setup Completion) |
| Banner: "Your shop is under review" | Etsy reviewing submitted documents | Go to Section 7 (Monitoring and Escalation) |
| No banners visible | Account may be fully verified OR verification in progress | Go to Section 3 (Verification Test) |

---

## 3. Verification Test (Run This First If No Banners)

If no banners are visible in Shop Manager, run this test before assuming the account is clear:

1. Open a new incognito browser window (Chrome: Ctrl+Shift+N; Firefox: Ctrl+Shift+P; Safari: Shift+Cmd+N)
2. Navigate to: `etsy.com/shop/[your-shop-name]` (replace with your actual shop URL slug)
3. Observe what loads:

| What you see in incognito | What it means |
|---|---|
| Your shop page loads (even if showing 0 active listings) | Account is verified or in progress — go to Section 8 (Publish Test) |
| "This shop is currently unavailable" | Verification still pending OR shop not properly set up |
| Redirect to etsy.com homepage or setup page | Verification pending |
| 404 error | Shop may not exist yet — confirm your shop name |

If the shop page loads: proceed to Section 8 (Publish Test) to confirm listings can actually be published.

If the shop is unavailable: follow the steps in Section 4 and Section 5 to identify which component is incomplete.

---

## 4. Identity Verification via Persona

### Documents You Need

Gather these before opening the Etsy verification interface:

- [ ] **Government-issued photo ID** — one of:
  - US driver's license (front and back required)
  - US passport (photo page only)
  - State-issued photo ID card (front and back)
  - The ID must show: your full legal name, date of birth, expiration date, and a photo. Expired IDs are rejected.
- [ ] **A device with a front-facing camera** — phone or laptop with webcam. The selfie step requires a live camera capture (not a uploaded selfie photo). Persona initiates the camera in-browser or via mobile — you cannot substitute a saved image.
- [ ] **Access to your Etsy account email** — Persona sends confirmation to the registered Etsy address.

### Step-by-Step Identity Verification

1. Log into Etsy
2. Navigate to: Account Settings > Security > Identity Verification
   - Alternate path if banner is showing: click the banner directly — it links to the same page
3. Click "Verify my identity" or "Start verification"
4. Persona's interface loads (may open a new tab or overlay)
5. Select your ID type (driver's license or passport)
6. Follow Persona's prompts:
   - **Step 1 — ID scan**: Use your camera to photograph your ID. For a driver's license, Persona requires front and back. Hold the ID flat and steady; the auto-capture triggers when the image is clear.
   - **Step 2 — Selfie**: Persona activates your front-facing camera. Follow the on-screen guide (usually: center your face, hold still, wait for auto-capture). This is a biometric comparison step — Persona compares the selfie against your ID photo.
   - **Step 3 — Confirm**: Review the captured images and submit.
7. After submission: Persona displays a confirmation screen. Etsy sends a confirmation email within minutes.
8. **Save the confirmation email with its timestamp** — this is your evidence of submission if follow-up is needed.

### What Persona Reviews

Persona compares biometric identifiers (facial geometry) from the selfie against the ID photo. Per Etsy's privacy policy (2026), the selfie and ID image are retained for up to 6 years after shop closure; biometric data is stored for up to 1 year by Persona.

You may be offered a choice between:
- **Express review** — uses biometric comparison (faster, typically 24–48 hours)
- **Manual review** — human review without biometric processing (slower, 3–5 business days)

If the option is presented, choose Express review to minimize wait time.

### After Submission

Etsy/Persona reviews the documents and notifies you by email when complete. The email subject will be from Etsy (not Persona) and will confirm either:
- Verification approved — your account can now publish listings
- Verification failed — Etsy will specify what was unclear (photo quality, ID issue, etc.) and prompt you to resubmit

Do not attempt to resubmit before receiving the outcome email. Duplicate submissions can slow the process.

---

## 5. Etsy Payments Setup

Etsy Payments must be enrolled and active before listings can be published. If you have not connected Etsy Payments, or if the banner "Connect Etsy Payments" is visible, complete this step.

### Documents You Need

- [ ] **Bank routing number** — 9-digit number, found at the bottom of a check or in your online banking account details
- [ ] **Bank account number** — checking account number (not savings — Etsy Payments deposits to checking)
- [ ] **Social Security Number (SSN)** — for US individual/sole proprietor sellers, required for tax reporting. If operating as a registered business: **EIN (Employer Identification Number)** instead.
- [ ] **Legal name** — must match the name on your bank account and government ID exactly
- [ ] **Business address** — your address if operating as sole proprietor; registered business address if applicable
- [ ] **Date of birth** — for identity verification cross-check

### Step-by-Step Etsy Payments Enrollment

1. Log into Etsy > Shop Manager
2. Click "Finances" in the left sidebar > "Payment Settings"
3. Click "Set up Etsy Payments" (or "Add bank account" if the button is different)
4. Select your country (United States)
5. Enter your bank account details:
   - Bank routing number (9 digits)
   - Bank account number
   - Account type: Checking
6. Etsy uses Plaid for US bank verification. Plaid will either:
   - **Instant verification** — log into your bank through Plaid's interface to verify instantly (most major banks supported); or
   - **Micro-deposit verification** — Plaid deposits $0.01 to your account with a 3-letter code starting with #. You enter that code in Etsy within 3–5 business days to confirm.
7. Enter your legal name, date of birth, and SSN (or EIN)
8. Enter your business address
9. Submit. Etsy confirms Payments enrollment by email.

### Bank Verification Timeline

| Verification method | How it works | Timeline |
|---|---|---|
| Plaid instant (most banks) | Log into your bank through Plaid UI | Immediate — completes in the same session |
| Plaid micro-deposit | $0.01 deposit + 3-letter code | 1–3 business days to appear in your account |
| Manual bank verification (rare) | Etsy reviews account details | Up to 5 business days |

**New seller payout hold**: After Etsy Payments is active, your first payouts may be held for 3–7 days while Etsy verifies account legitimacy. This does not prevent listings from going live — it only affects when the first deposit hits your bank.

---

## 6. Shop Setup Completion (If "Complete Your Shop" Banner)

If the banner says "Complete your shop setup," these fields need to be filled in before publishing is available:

1. Etsy > Shop Manager > Settings > General Settings
   - Shop name: must be set (cannot be blank or "placeholder")
   - Shop announcement: brief description (1–2 sentences) — can be edited later
2. Etsy > Shop Manager > Settings > Policies
   - Returns and exchanges policy: required field — minimum entry is "No returns accepted for digital products"
   - Privacy policy: Etsy provides a template — accept or customize
3. Etsy > Shop Manager > Finances > Billing
   - Credit or debit card on file for Etsy fees (separate from your payout bank account)
   
After filling in each section, click "Save" before navigating away. Etsy does not auto-save.

---

## 7. Monitoring After Submission and Escalation Protocol

### Normal Timeline After Submission

| Milestone | Timing |
|---|---|
| Submission confirmation email from Etsy/Persona | Within minutes of submitting |
| Express review complete (best case) | 24–48 hours |
| Express review complete (typical) | 2–3 business days |
| Manual review complete | 3–5 business days |
| Maximum normal processing window | 5 business days |
| Escalation threshold (contact Etsy support) | If not resolved after 5 business days |

"Business days" for Etsy purposes means Monday–Friday, US Eastern time. A submission made on Friday afternoon may not begin processing until Monday.

### What to Monitor

Check your Etsy account email for a message from Etsy (subject will reference "identity verification" or "shop verification"). Additionally:

- Check Etsy Shop Manager once per day — the verification banners disappear once verification clears
- Run the incognito shop page test (Section 3) after Day 2 — if your shop page loads, verification is cleared even if the email has not arrived yet

### Escalation: If Not Resolved After 5 Business Days

1. Navigate to: help.etsy.com > Contact Us
2. Select topic: "Shop verification" or "Account issues"
3. Send this message:
   > "I submitted my identity verification documents on [date] and have not yet received a confirmation or outcome email. My shop name is [your shop name]. The email on my account is [email]. I have products ready to publish and need to understand the current review timeline. Could you please check the status of my verification and advise when it will be complete?"
4. Expected Etsy support response: 24–48 hours
5. Log the support ticket number and date in WORKLOG.md

---

## 8. Publish Test (Final Verification That Everything Is Active)

After all components show complete (no banners, shop page visible in incognito), confirm listings can actually be published:

1. In Etsy Shop Manager > Listings, find any one of your Phase 1 Draft listings
2. Click to edit the listing
3. Look at the button in the top right of the listing editor — it should say "Publish" (active, not grayed out)
4. **Do not click Publish yet** — just confirm the button is active
5. If the button says "Publish" and is clickable: verification is complete, Track A is unblocked
6. If the button is grayed out or says "Pending verification": verification is still processing — wait and recheck in 24 hours

This is the definitive success signal. A clickable "Publish" button on a fully completed listing means Etsy Payments is active, identity verification is complete, and your shop is ready to go live.

---

## 9. Documentation Checklist — What to Gather Before Starting

Have all of these ready before opening the Etsy verification interface. Stopping mid-session to find documents can cause Persona's session to time out.

- [ ] Government-issued photo ID (driver's license or passport) — within arm's reach
- [ ] Device with working front-facing camera (phone preferred for selfie step)
- [ ] Bank routing number (9 digits)
- [ ] Bank account number (checking account)
- [ ] SSN or EIN
- [ ] Legal name (exactly as it appears on your ID and bank account)
- [ ] Business address (mailing address)
- [ ] Date of birth
- [ ] Access to your Etsy account email (to receive confirmation)
- [ ] Credit or debit card (for Etsy billing, separate from payout account)

---

## 10. Timeline Summary for May 27 Execution

As of today (May 27), the verification window is tight relative to Phase 3's June 22 gate but fully workable:

| Event | Date (if submitted May 27) |
|---|---|
| Submit verification documents | May 27 |
| Confirmation email received | May 27 (same day) |
| Best-case clearance (1 business day) | May 28 |
| Typical clearance (2–3 business days) | May 29–30 |
| Worst-case clearance (5 business days) | June 3 |
| Phase 1 upload window (post-clearance) | Same day verification clears |
| Track B May 30 launch | NOT affected — Track B has zero dependency on this |
| June 22 Phase 3 gate | NOT directly affected — Phase 3 gates (forager cohort %, Native Plants conversion) are data-driven, not contingent on Track A unblock date |

The June 22 Phase 3 gate is cleared by demand data from Track B's May 30 launch, not by Track A. Track A's Etsy verification only affects Phase 1 product availability — Phase 3 can proceed regardless of when Track A unblocks, as long as the two demand gates (forager cohort ≥20%, Native Plants conversion ≥1.5%) remain cleared through June 20.

---

## 11. Contingency: If Verification Is Delayed Beyond June 3

If Etsy verification has not cleared by June 3 (the 5-business-day worst-case from a May 27 submission), the following fallback is available:

**Gumroad interim channel (15-minute setup):**

1. Create account at gumroad.com/signup
2. Upload Phase 1 product PDFs and set pricing equivalent to Etsy pricing
3. Share the Gumroad shop URL in social profiles and the Track B May 30 launch announcement
4. Phase 1 revenue begins immediately with no verification requirement
5. Transaction fee: 10% (vs. Etsy's 6.5% + ~3% payment processing ≈ 9.5% — similar)
6. When Etsy verification clears, publish all Phase 1 listings on Etsy and update all links
7. Gumroad can remain live as a secondary channel or be deactivated

The key point: a Gumroad delay does not mean zero Track A revenue. It means Track A revenue begins on a different platform and migrates to Etsy when verification resolves.

---

## 12. Success Criteria — When to Declare Blocker 2 Resolved

Blocker 2 is resolved when ALL of the following are true simultaneously:

- [ ] No verification banners visible in Etsy Shop Manager
- [ ] Shop page is visible in incognito browser (etsy.com/shop/[your-shop-name] loads)
- [ ] Etsy Payments is enrolled — bank account and tax info on file (visible in Shop Manager > Finances > Payment Settings)
- [ ] "Publish" button is active (not grayed out) on at least one Phase 1 Draft listing
- [ ] Logged in WORKLOG.md: "Track A Blocker 2 — Etsy account verified [date]"

When all five criteria are met, Track A Blocker 2 is fully resolved and Phase 1 upload can begin immediately.

---

*Sources: Etsy Help Center — Identity Verification with Persona (help.etsy.com/hc/en-us/articles/22504854625815); Etsy Help Center — How to Verify Your Identity on Etsy (help.etsy.com/hc/en-us/articles/22481159004567); Etsy Help Center — How to Verify Your Seller Information for Etsy Payments (help.etsy.com/hc/en-us/articles/360001980067); Alura.io Etsy Business Verification Guide (alura.io/docs/article/etsy-business-verification-guide); InsightAgent How to Make a Business Account on Etsy 2026 (insightagent.app/guides/etsy-business-account-setup); TRACK_A_RESOLUTION_PROTOCOL.md (Session 1344, May 15, 2026).*
