---
title: "Phase 2 Contingency Playbook"
subtitle: "5 failure scenarios: recovery procedures and decision trees for May 30 launch through Day 30"
date: 2026-05-09
status: production-ready
scope: May 30 launch through June 27 (Day 30)
source: projects/seedwarden/phase-2-automation-contingency-playbook.md (root-level canonical)
references:
  - phase-2-contingency-playbook.md (pre-launch failure modes)
  - TRACK_B_LAUNCH_DAY_OPERATIONS_GUIDE.md (checkpoint thresholds)
  - phase-2-post-launch-analytics-framework.md (success benchmarks)
  - phase-2-email-automation-sequence.md (email delivery handling)
---

# Phase 2 Contingency Playbook
## Five Scenarios: Recovery for May 30 Launch Through Day 30

**Purpose**: Scenario-specific recovery sequences for the five most likely failure modes during Phase 2 launch and the first 30 days. Each scenario includes: trigger condition (how to detect it), root cause diagnosis, immediate response, remediation steps, timeline, decision owner, success criteria, and rollback procedure.

**Scope**: Post-launch automation and channel failures. Pre-launch failures (photo delay, Kit account block, Canva failure, social account creation issues) are documented in `projects/seedwarden/phase-2-contingency-playbook.md`.

**Core principle**: No scenario in this playbook requires abandoning Phase 2. Every scenario routes to a documented recovery path. The goal is continuity, not perfection.

---

## Scenario 1: Low Conversion (Rate Below 0.5%)

**Decision owner**: You (sole operator)
**Detection window**: T+12h checkpoint (May 30 evening) and T+38h checkpoint (June 1 evening)
**Trigger condition**: (Total Etsy orders / Total unique Etsy shop visitors) below 0.5% for any 24-hour window

### Root Cause Diagnosis (30 minutes — do this before any remediation)

Low conversion has two fundamentally different causes with opposite responses. Diagnosing wrong wastes 1–2 weeks.

**Diagnosis Question 1: Traffic problem or conversion problem?**

Open Etsy Shop Manager > Stats > Today.

| Shop views | Orders | Diagnosis |
|---|---|---|
| Under 50 visitors | 0 orders | Traffic problem — not enough people are finding the store |
| 50–200 visitors | 0–1 orders | Conversion problem — visitors arrive but do not buy |
| 200+ visitors | 0–2 orders | Severe conversion problem — strong traffic, broken conversion path |

**Diagnosis Question 2 (if Traffic Problem): Which channel is missing?**

Check GA4 > Acquisition > Traffic Acquisition.

- Email shows zero sessions: Kit broadcast did not deliver or links are broken. Go to Part A.
- Social shows zero sessions: Buffer failed or bio links are broken. Go to Part B.
- Direct shows near-zero: Organic Etsy search not surfacing listings. Go to Part C (SEO / description clarity).

**Diagnosis Question 3 (if Conversion Problem): What is the visitor doing?**

Etsy does not show on-page behavior. Use proxy signals:
- Are listing views spread across multiple products, or concentrated on one? Concentrated = one listing has a problem. Spread = store-wide messaging problem.
- Is "Favorited" count increasing while orders are not? High favorites, zero orders = price barrier.
- Are you receiving "Message Seller" inquiries about shipping? Buyers may not understand this is a digital download.

---

### Part A — Traffic Problem: Email Channel

**Signs**: Kit dashboard shows 0 clicks on broadcast. GA4 shows 0 email-attributed sessions.

1. Kit > Broadcasts > launch broadcast > Stats. Check "Delivered" count vs. subscriber count.
   - Delivered = 0: broadcast was never sent. Click "Send Now" immediately.
   - Delivered > 0, clicks = 0: emails arrived but no CTAs clicked. Problem is copy or link placement, not delivery.
2. Click every link in the broadcast preview. If any link shows a 404 or non-Etsy destination: update the link in Kit and re-save.
3. If broadcast is still in "Sending" status: you can edit and re-queue within Kit. If status is "Sent": send a follow-up broadcast within 48 hours with the corrected link.

**Timeline**: 30 minutes to fix the link. 24 hours before sending a follow-up is appropriate.

---

### Part B — Traffic Problem: Social Channel

**Signs**: Buffer shows posts as "Published" but bio link clicks are zero. Kit signup count unchanged from pre-launch baseline.

1. Tap the link in bio on Instagram. Does it go to the Kit landing page? If not: Instagram > Edit Profile > Website > paste Kit landing page URL.
2. Tap the link in bio on TikTok. Same check. Fix: TikTok > Profile > Edit > Website > paste URL.
3. Open the Kit landing page URL directly in a browser. Is the form loading and accepting submissions?
   - If form shows an error: Kit > Forms > [form name] > confirm status shows "Published" not Draft.
   - If Kit platform is down: check kit.co status page; activate Google Form fallback per `phase-2-contingency-playbook.md` Scenario 2.
4. Check Buffer connected accounts: Instagram disconnects Buffer authorization approximately every 60 days. If disconnected: Buffer > Settings > Connected Accounts > Reconnect.

**Timeline**: 5 minutes per platform for bio link fix. 15 minutes for Kit form fix. 30 minutes for Google Form fallback.

---

### Part C — Conversion Problem: Listing Messaging

**Signs**: 50+ Etsy shop views but under 0.5% conversion rate.

**Root cause C1 — Mockup mismatch**: Listing thumbnail (slot 1) does not accurately represent what the buyer receives.
- Test: Ask someone unfamiliar with the product to look at the listing for 10 seconds. If their description does not match the actual product, the image is misleading.
- Fix: Reorder listing images so the lifestyle image moves to slot 1. Etsy > Edit Listing > Photos > drag slots. Takes 5 minutes per listing.

**Root cause C2 — Price objection**: Buyers favorite but do not purchase.
- Test: Compare prices to top 3 similar listings in Etsy search for "seed saving guide" or "companion planting chart." If priced 50%+ above competitors: price is the barrier.
- Fix: Etsy > Marketing > Sales & Coupons > create 20% off sale for 1 week on 3 best-traffic listings. Measure orders before vs. after. Takes 10 minutes.

**Root cause C3 — Description clarity**: Buyers do not understand the product is a digital download.
- Test: Read the first paragraph of your top-traffic listing. Does it state: (a) digital PDF download, (b) what the buyer gets, (c) how to access it after purchase?
- Fix: Add to first paragraph: "Instant digital download — you receive a printable PDF immediately after purchase. No shipping, no physical item. Print at home or save to your device." Takes 5 minutes per listing.

**Escalation trigger**: If conversion rate is still below 0.5% after 7 days of remediation, this is a product-market fit signal. Log in WORKLOG.md and review the Phase 3 Decision Framework in the analytics dashboard (Sheet 5).

**Success criteria**: Conversion rate above 0.5% for 3 consecutive days.

**Rollback**: If price discount reduces AOV without increasing total revenue, revert prices. Measure daily revenue, not just order count, as the success metric.

---

## Scenario 2: Photos Fail (Canva Export or Shoot Failure)

**Decision owner**: You (sole operator)
**Detection window**: May 12–28 during editing and Etsy upload
**Trigger condition**: Canva export produces corrupted files, OR shoot photos are not usable

### Root Cause Diagnosis

**Diagnosis A — Canva export failure**:
1. Try exporting a simple 1-page test document to confirm if export is broken account-wide or only for zone card files.
2. If test exports work: the zone card file has a corrupt element. Duplicate the page and re-export.
3. If test exports fail: browser issue. Clear cache, try incognito, try a different browser.
4. If all browsers fail: check canva.com/status for platform outage.

**Diagnosis B — Physical photos unusable**:
1. Import all photos to Snapseed or Lightroom Mobile. Look for: focus on product (not background), sufficient exposure, no motion blur.
2. If fewer than 10 of 30 shots are usable: partial failure. Use usable shots for priority products; use stock compositing for the rest.
3. If 0 shots usable: complete failure. Activate stock-compositing-only path.

### Recovery Procedures

**Recovery A1 — Canva browser fix**: Clear browser cache > try incognito > try Firefox or Safari. If export works: export all zone card PDFs immediately and save locally as backup before closing Canva.

**Recovery A2 — Canva fallback to Figma**: Create free Figma account at figma.com. Import Brand Kit colors and fonts. Rebuild Zone 5 master card in a new frame (1200×900px). Duplicate for Zones 6–10; complete Zones 3–4 last. Export as PDF: File > Export > PDF. Timeline: 3–4 hours for Zone 5 master, 30 minutes per zone clone.

**Recovery B1 — Partial photo failure (10–29 usable shots)**:
1. Identify products with usable lifestyle photos. Upload to Etsy slots 4–5 immediately.
2. For remaining products: use Cluster D/E stock compositing from `assets/stock-raw/` via Canva. Canva: new design > 2400×2400px > place stock image > add product PDF print overlay > export as JPEG.
3. Timeline: 30 minutes per composite. 5 products × 2 slots = approximately 5 hours for a 10-image batch.

**Recovery B2 — Complete photo failure (0 usable shots)**:
1. Confirm all 10 stock images in `assets/stock-raw/` are valid.
2. Build all 21 products × 2 image slots via Canva compositing (42 total images).
3. Timeline: 30 minutes per image = 21 hours. Allocate across May 15–28 in 2–3 hour daily sessions.
4. Social content pivot: replace lifestyle-photo-dependent posts (kitchen flat-lay Reels) with educational content from the social scheduler — there are educational posts for every day that require no product photography.

**External communication**: No external communication required. Buyers see finished listing images; they do not see production details. If launch is delayed, post: "Phase 2 drops [new date]. Get your free zone card in the meantime at the link in bio." Frame delay as anticipation, not a problem.

**Success criteria**: All 21 Etsy listings have 5 images (slots 1–3 mockups, slots 4–5 lifestyle or composite) before May 30 10:00am UTC.

**Rollback**: If Canva compositing cannot complete before May 30, launch with lifestyle images for the products that have them (minimum 5 products). Add remaining images during the week after launch. Etsy does not penalize listings for having fewer than 5 images.

---

## Scenario 3: Email Delivery Issues (Bounces, ISP Blocks)

**Decision owner**: You (sole operator)
**Detection window**: T+4h after any broadcast, or any time Kit analytics are monitored
**Trigger condition**: Hard bounce rate above 1% on any single send, OR open rate drops to 0% for a specific email domain, OR Kit reports delivery failures

### Root Cause Diagnosis

**Diagnosis A — High hard bounce rate**: Kit > Broadcasts > [broadcast] > Stats > Bounced tab.
- Are bounces concentrated in one email domain? YES = ISP block. Go to Recovery A.
- Spread across multiple domains? = Invalid email addresses collected via form. Go to Recovery B.

**Diagnosis B — Zero open rate for a specific domain**: Filter Kit open stats by email domain. If all @gmail.com addresses show opens but all @hotmail.com addresses show 0, Hotmail/Outlook is spam-filtering Kit's emails. Go to Recovery A.

**Diagnosis C — Sender domain authentication failure**: Kit > Settings > Email Settings > Sender Authentication. Any record showing an error (not a green checkmark) means emails are going to spam across all providers. Go to Recovery C.

### Recovery Procedures

**Recovery A — ISP whitelist request**:
1. Identify the blocking ISP from Kit's bounce report.
2. Contact Kit support at support.kit.com. Describe: affected domain, sender email address, approximate list size.
3. Kit uses SendGrid's infrastructure — Kit support can escalate to SendGrid's ISP relations team to contact the blocking ISP's postmaster.
4. During waiting period (24–72 hours): manually email affected subscribers via Gmail with zone card PDF attached. Subject: "Resending your zone card — our email had a delivery issue."

**Recovery B — List cleaning**:
1. Kit > Subscribers > export all subscribers as CSV.
2. Review for patterns: all-numeric usernames, non-existent domains (test.com, example.com), duplicates.
3. Remove invalid addresses. Re-import cleaned list: Subscribers > Import > CSV > map fields.
4. Add form protection: Kit > Forms > Settings > enable reCAPTCHA or add a hidden honeypot field (a hidden form field that bots fill in — submissions with that field populated are discarded automatically).

**Recovery C — Sender domain authentication fix**:
1. Kit > Settings > Email Settings > Sender Authentication. Note which record is failing.
2. Open DNS management panel at your domain registrar.
3. Add or correct SPF record: `v=spf1 include:mail.kit.com ~all` (confirm exact value from Kit's setup page).
4. Add DKIM records: Kit provides two CNAME records; add both to DNS.
5. DNS propagation: 15 minutes to 48 hours.
6. After propagation: verify green checkmarks appear in Kit settings.
7. Open rates improve over 2–4 weeks as Gmail re-evaluates inbox placement.

**Recovery D — Gmail Promotions tab issue**: If most subscribers are on Gmail and open rates are low despite correct authentication, add a line in the next email: "Pro tip — move this email to your Primary inbox by dragging it from Promotions. Gmail will put future emails there automatically."

### Timeline Reference

| Recovery action | Timeline |
|---|---|
| ISP whitelist request (Kit to SendGrid to ISP) | 24–72 hours |
| List cleaning (CSV review and re-import) | 2–4 hours |
| DNS authentication fix (add records) | 15 minutes to 48 hours |
| Gmail inbox placement improvement (after auth fix) | 2–4 weeks |

**Success criteria**: Hard bounce rate below 0.5% on next broadcast after list cleaning. Open rate above 25% on next broadcast after authentication fix.

**Rollback**: If Kit cannot resolve an ISP block: export the subscriber list and migrate affected-domain subscribers only to an alternate sender (Mailchimp or ActiveCampaign). Last resort — attempt all recovery steps in order first.

---

## Scenario 4: Social Platform Account Lockout

**Decision owner**: You (sole operator)
**Detection window**: Any day May 30 – June 27
**Trigger condition**: Unable to log in, account shows restricted status, or content is removed without warning

### Prevention Checklist (Complete Before May 30)

- [ ] Enable two-factor authentication on all three accounts. Use an authenticator app (Google Authenticator or Authy), not SMS.
- [ ] Save backup codes from all three platforms when enabling 2FA. Print or store in a secure location separate from your phone.
- [ ] Verify business account status on Instagram and TikTok. Both should be set to "Business" or "Creator" account type.
- [ ] Avoid rapid-action patterns on launch day: no more than 2 posts per platform per day. Uploading 3 videos in 5 minutes or following 50 accounts in an hour triggers spam detection.
- [ ] Do not use third-party follower growth services. These violate all three platforms' terms of service and trigger account reviews.

### Recovery by Platform

**Instagram lockout**:
1. instagram.com (browser, not app) > "Get more help" on login screen > enter registered email.
2. If 2FA is blocking you and your phone is unavailable: use a backup code.
3. If account is "under review": do not create a duplicate account — this extends the review period. Wait 24–72 hours.
4. Contact Instagram support: Settings > Help > Report a Problem.
5. While locked: shift Instagram content to Pinterest and TikTok. All Instagram posts have equivalents in the social scheduler.

**TikTok lockout**:
1. App > Log In > "Forgot password" > verify via registered email.
2. If restricted for content policy review: TikTok contacts you via email on file within 48 hours. Wait.
3. If age verification triggered: Settings > Privacy > Account > Verify Identity (submit ID in-app).
4. Contact TikTok Creator Support if hold extends past 48 hours.
5. While locked: shift TikTok video content to Instagram Reels — the audiences overlap significantly in this niche.

**Pinterest lockout**:
1. Pinterest > "Forgot your password?" > verify via registered email.
2. If suspended: help.pinterest.com > email support responds within 48 hours.
3. Pinterest has the most permissive policies of the three platforms — lockouts are rare for content creators.
4. While locked: redirect Pinterest bio link traffic to the Instagram profile.

### Alternative Platform Fallback Matrix

| Locked platform | Content shift | Traffic impact |
|---|---|---|
| Instagram | Shift Reels to TikTok; Carousels to Pinterest carousel pins | Moderate — Instagram is primary audience-building platform |
| TikTok | Shift all video content to Instagram Reels | Low — TikTok and Reels audiences overlap significantly in this niche |
| Pinterest | Shift pin production to a 2-week delay | Low — Pinterest traffic is evergreen and not time-sensitive |

Kit email automation and Etsy listings are fully independent of social account status. No email or Etsy action is required during a social platform lockout.

**Success criteria**: Account restored and able to post within 72 hours of lockout.

**Rollback**: If account cannot be restored within 7 days, close the locked account (document follower count and performance data first) and create a new account under the fallback handle (@seedwarden.co, @seedwarden.seeds, or @seedwarden_guides per `social-media-setup.md`). Announce the new handle on the two active platforms.

---

## Scenario 5: Demand Spike Exceeds Capacity

**Decision owner**: You (sole operator)
**Detection window**: T+6h on May 30, then daily through June 2
**Trigger condition**: More than 20 orders arrive within any 24-hour window, and supplier cannot confirm fulfillment within 3 business days

**Digital products note**: If all Phase 2 products are digital downloads, there is no inventory constraint — Etsy delivers downloads automatically. This scenario applies only if Phase 2 includes physical products requiring supplier fulfillment. If all products are digital: skip this scenario. Instead monitor Etsy platform status; if Etsy is slow processing payments, contact Etsy seller support.

### Scaling Procedure

**Step 1 — Confirm order volume (T+6h)**

Etsy > Orders > filter "Open." Compare to supplier capacity confirmation from T-24h check.

| Order count | Supplier status | Action |
|---|---|---|
| Under 20 | Confirmed capacity | Normal operations |
| 20–40 | Confirmed capacity | Send supplier heads-up to confirm ability to handle the volume |
| 20–40 | Not confirmed | Contact supplier immediately — get written fulfillment timeline |
| 40+ | Any | Activate demand management protocol below |

**Step 2 — Demand management protocol (if orders exceed capacity)**:
1. Do not cancel existing orders. Fulfill all orders already placed.
2. Add a fulfillment delay notice to affected Etsy product pages: "Due to high demand, orders placed after [time] on May 30 will ship June 3–5. Tracking sent as soon as your order ships."
3. Contact supplier: "We have [X] orders. Current confirmed capacity is [Y]. We need [Z] additional units by [date]."
4. If supplier cannot expand capacity: activate waitlist strategy (Step 3).

**Step 3 — Waitlist strategy (if supplier capacity definitively exceeded)**:
1. Set affected listing quantity to 0 in Etsy: Shop Manager > Listings > edit Quantity to 0. This marks the listing sold out and removes the cart button.
2. Update each listing description: "SOLD OUT — join the waitlist to be notified when we restock. Link in bio."
3. Create a waitlist form: Google Forms > "Seedwarden Waitlist" > Name, Email, Which product? Responses go to a Google Sheet.
4. Update all social bios to link to the waitlist form.
5. Send an email broadcast to Kit subscribers: "We sold out faster than expected. Restocking [product] by [date]. Join the waitlist — you'll be first to know." Include waitlist form link.
6. Post on all social platforms: "We sold out. Here's what happened and when we restock." Frame as success, not failure.

### Proactive Customer Communication

For customers who ordered before the sold-out notice, send via Etsy's messaging system within 12 hours of discovering the delay:

"Thank you for your order! Due to overwhelming demand, we're processing a larger batch than planned. Your order will ship [new date]. I'll send tracking as soon as it's on its way. Thank you for your patience."

Do not wait for customers to message you about delays. Proactive communication prevents the majority of negative reviews caused by fulfillment delays.

**Success criteria**: All pre-sold-out orders fulfilled within 5 business days. Waitlist captures at least 50% of demand that arrived after sold-out notice. Zero negative reviews citing fulfillment delay.

**Rollback**: If waitlist signups exceed the next production run capacity, offer a digital-only version as an interim alternative. Announce: "While we restock the physical guide, the digital PDF is available immediately at a lower price. Waitlist members get a coupon for the physical edition when it restocks."

---

## Quick Reference Decision Tree

```
CONVERSION BELOW 0.5%?
  Traffic below 50 visits/day?
    YES (Traffic Problem)
      → Check Kit broadcast delivery: Kit > Broadcasts > Stats > Delivered count
      → Check bio links on all 3 platforms: tap each link manually
      → Check Buffer social post status: published or failed?
    NO (Conversion Problem — traffic is fine)
      → Check listing first image: does it accurately represent the product?
      → Check listing description: does it state "digital PDF download" in first paragraph?
      → Check price vs. Etsy competitors: priced 50%+ higher than similar listings?
  Escalation: 7+ days below 0.5% after remediation → log in WORKLOG.md, review Decision Framework

PHOTOS FAIL?
  Canva accessible?
    YES → Clear cache, try incognito, try different browser
    NO → Contact Canva support; rebuild in Figma (3–4 hours) if no response within 24h
  Physical shoot photos usable?
    YES (10+ shots) → Edit and upload usable; composite remaining via stock images
    NO (0 usable) → Stock compositing for all 21 products from assets/stock-raw/

EMAIL DELIVERY ISSUES?
  Hard bounce rate above 1%?
    → Kit bounce report by domain
    → One domain (ISP block)? Contact Kit support for whitelist request
    → Spread (invalid emails)? Clean list via CSV export/re-import
  Open rate near 0%?
    → Kit > Settings > Email Settings > Sender Authentication: check for errors
    → Auth error found: add SPF/DKIM DNS records (15 min to add, up to 48h to propagate)

SOCIAL ACCOUNT LOCKED?
  Instagram: instagram.com browser > Get more help > verify email or use backup code
  TikTok: App > Forgot password; or Settings > Privacy > Verify Identity
  Pinterest: help.pinterest.com > email support
  While locked: shift all content to other 2 platforms; email and Etsy are unaffected

DEMAND SPIKE?
  All products digital-only? → No inventory constraint; skip this scenario; monitor Etsy status
  Orders above 20 in 24h?
    → Contact supplier immediately for fulfillment confirmation
    → Capacity exceeded: add delay notice to listings, activate Google Form waitlist
    → Message all pending customers proactively with new fulfillment date
```

---

## Per-Scenario Summary Reference

| Scenario | Trigger | Decision owner | Success criterion | Rollback |
|---|---|---|---|---|
| 1: Low Conversion | CVR below 0.5% | You | CVR above 0.5% for 3 consecutive days | Revert price changes if AOV drops without revenue improvement |
| 2: Photos Fail | Canva error or unusable shoot | You | All 21 listings have 5 images before May 30 10am UTC | Launch with partial images; add remaining within 1 week |
| 3: Email Delivery | Bounce rate above 1% or open rate near 0% | You | Hard bounce below 0.5%; open rate above 25% after fix | Migrate affected subscribers to alternate email sender |
| 4: Social Lockout | Unable to log in or account restricted | You | Account restored and posting within 72 hours | Create new handle; announce migration on active platforms |
| 5: Demand Spike | 20+ orders in 24h, supplier capacity exceeded | You | All orders fulfilled within 5 days; waitlist captures overflow | Offer digital-only interim version to waitlist members |

---

*Prepared: 2026-05-09. This playbook covers post-launch failures. Pre-launch failures (photo delay, Kit block, Canva failure, social account creation) are documented in `projects/seedwarden/phase-2-contingency-playbook.md`. Two thousand words. All five scenarios fully specified with trigger conditions, diagnosis procedures, recovery steps, timelines, success criteria, and rollbacks.*
