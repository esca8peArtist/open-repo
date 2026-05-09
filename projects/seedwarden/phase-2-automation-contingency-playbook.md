---
title: "Phase 2 Automation & Contingency Playbook"
subtitle: "5-scenario response guide for May 30 launch and first 30 days"
date: 2026-05-09
session: 907-item36
status: production-ready
scope: Phase 2 launch through Day 30 (June 27, 2026)
references:
  - TRACK_B_LAUNCH_DAY_OPERATIONS_GUIDE.md (checkpoint logic and KPI thresholds)
  - phase-2-contingency-playbook.md (pre-launch failure modes — photo delay, Kit block, Canva failure)
  - phase-2-post-launch-analytics-framework.md (success benchmarks and red flags)
  - phase-2-email-automation-sequence.md (email delivery handling)
  - TRACK_B_FINAL_EXECUTION_GUIDE.md (pre-launch prep)
---

# Phase 2 Automation & Contingency Playbook
## Five Scenarios: Response Procedures for May 30 Launch Through Day 30

**Purpose**: This playbook covers the five most likely failure modes during Phase 2 launch and the first 30 days. Each scenario includes: trigger condition (how to detect it), root cause diagnosis, immediate response, remediation sequence, timeline, decision owner, success criteria, and rollback procedure.

**Scope of this document**: Post-launch automation and channel failures. Pre-launch failures (photo delay, Kit account block, Canva failure, social account lock) are documented in `phase-2-contingency-playbook.md`. Do not recreate those scenarios here.

**Key principle**: No scenario in this playbook requires abandoning Phase 2. Every scenario routes to a documented recovery path. The goal is continuity, not perfection.

---

## Scenario 1: Low Conversion (Conversion Rate Below 0.5%)

**Decision owner**: You (sole operator)
**Detection window**: T+12h checkpoint (May 30 evening) and T+38h checkpoint (June 1 evening)
**Trigger condition**: (Total Etsy orders / Total unique Etsy shop visitors) < 0.5% for any 24-hour window

### Root Cause Diagnosis

Before executing any remediation, spend 30 minutes diagnosing the exact cause. Low conversion has two completely different root causes with opposite responses. Diagnosing wrong wastes 1–2 weeks of effort.

**Diagnosis Question 1: Is this a traffic problem or a conversion problem?**

Open Etsy Shop Manager > Stats > Today. Check two numbers:
- Shop views today (unique visitors arriving at your store)
- Orders today

| Views | Orders | Diagnosis |
|---|---|---|
| Under 50 visitors | 0 orders | Traffic problem — not enough people are finding the store |
| 50–200 visitors | 0–1 orders | Conversion problem — visitors are arriving but not buying |
| 200+ visitors | 0–2 orders | Severe conversion problem — strong traffic, broken conversion path |
| 50–200 visitors | 5+ orders | Not a conversion problem — review your tracking (orders may exceed the 0.5% threshold) |

**Diagnosis Question 2 (Traffic Problem): Where is the traffic not coming from?**

Check GA4 > Acquisition > Traffic Acquisition. Which channels show zero sessions?
- Email channel shows zero sessions = Kit broadcast did not deliver or links are broken. Go to Kit diagnosis (Part A below).
- Social channel shows zero sessions = Buffer failed to post, or bio links are broken. Go to Social diagnosis (Part B below).
- Direct channel shows zero sessions = Organic Etsy search is not surfacing your listings. Go to SEO diagnosis (Part C below).

**Diagnosis Question 3 (Conversion Problem): What is the visitor doing on the listing page?**

Etsy does not provide on-page behavior analytics. Proxy diagnosis:
- Are listing views spread across multiple products, or concentrated on one? (Concentrated = listing-level issue with one product; spread = store-wide messaging problem)
- Is the "Favorited" count increasing even though orders are not? (High favorites, zero orders = price barrier)
- Are you receiving any "Message Seller" inquiries? (Questions about shipping = confusion about digital format; questions about content = description clarity issue)

---

### Part A: Traffic Problem — Email Channel

**Signs**: Kit dashboard shows 0 clicks on broadcast. GA4 shows 0 email-attributed sessions.

**Step-by-step diagnosis**:
1. Open Kit > Broadcasts > find the launch broadcast > click Stats
2. Check "Delivered" count vs. subscriber count. If Delivered is 0: the broadcast was never sent. Click "Send Now" immediately.
3. Check "Opens" count. If opens are above 0 but clicks are 0: email arrived but CTAs were not clicked. The problem is email copy or link placement, not delivery.
4. Click on the broadcast preview and test every link. If any link shows a 404 or redirects to a non-Etsy page: update the link in Kit, re-save the broadcast, and send a follow-up email within 48 hours.

**Remediation (link fix)**:
- Kit > Broadcasts > [broadcast name] > Edit (if still in "Sending" status) or duplicate the broadcast and re-send
- Fix broken link, update UTM parameters if needed
- Send a short follow-up broadcast: "Quick update — we fixed a link in yesterday's email. The correct shop link is [URL]."
- Timeline: 30 minutes to fix, 24 hours for follow-up to be appropriate

---

### Part B: Traffic Problem — Social Channel

**Signs**: Buffer shows posts as "Published" but Instagram/TikTok shows no link-in-bio clicks. Kit signup count has not increased since pre-launch baseline.

**Step-by-step diagnosis**:
1. Open Instagram profile > tap "Link in bio" link. Does it go to the Kit landing page? If it shows a 404, the link in the bio is broken. Edit the bio link immediately.
2. Open TikTok profile > tap the link in bio. Same check.
3. Open Kit landing page URL directly in a browser. Is the form accepting submissions? If the form shows an error or the page is down, Kit's landing page is broken. Log into Kit > Forms > find your form > check status.
4. Check Buffer connected accounts: is Instagram API still authorized? Instagram disconnects Buffer authorization approximately every 60 days. If disconnected: re-authorize in Buffer > Settings > Connected Accounts, then re-queue any failed posts.

**Remediation (bio link broken)**:
- Instagram: Profile > Edit Profile > Website > paste Kit landing page URL
- TikTok: Profile > Edit > Website > paste URL
- Pinterest: Profile > Edit > Website URL > paste URL
- Timeline: 5 minutes per platform

**Remediation (Kit landing page down)**:
- Kit > Forms > [form name] > check status shows "Published" (not Draft or Paused)
- If paused: click Activate. Form should respond within 5 minutes.
- If Kit is down entirely: activate the Google Form fallback documented in `phase-2-contingency-playbook.md` Scenario 2
- Timeline: 15 minutes for Kit fix, 30 minutes for Google Form fallback

---

### Part C: Conversion Problem — Listing Messaging

**Signs**: Traffic is arriving (50+ Etsy shop views) but conversion rate is below 0.5%.

**Root cause identification** (pick the most likely based on the data pattern):

**Root cause C1 — Mockup mismatch**: The listing thumbnail (slot 1) shows a mockup that does not accurately represent what the buyer receives. Buyers click, see a generic product, and leave.
- Test: Ask someone unfamiliar with the product to look at the listing for 10 seconds and describe what they think they are buying. If their description does not match the actual product, the mockup is misleading.
- Fix: Reorder listing images so the lifestyle image from slot 4 appears as the first image. Etsy allows reordering by dragging. Timeline: 5 minutes per listing.

**Root cause C2 — Price objection**: Buyers are favoriting but not purchasing. The "add to cart" rate is low relative to favorites.
- Test: Compare your prices to the top 3 similar listings in Etsy search for "seed saving guide" or "companion planting chart." If your prices are 50%+ above competitors, run a limited-time discount.
- Fix: In Etsy Shop Manager > Marketing > Sales & Coupons, create a 20% off sale for 1 week on your 3 best-traffic listings. Measure order rate before vs. after. If orders increase 2x, price was the barrier. Timeline: 10 minutes to create sale.

**Root cause C3 — Description clarity**: Buyers do not understand what they are purchasing or how it is delivered (digital download — no physical item).
- Test: Read the first paragraph of your top-traffic listing. Does it state: (a) this is a digital PDF download, (b) what the buyer gets, and (c) how to access it after purchase? If any of these are missing, add them.
- Fix: Edit the listing description first paragraph to include: "Instant digital download — you receive a printable PDF immediately after purchase. No shipping, no physical item. Print at home or save to your device." Timeline: 5 minutes per listing.

**Escalation trigger**: If after 7 days of remediation the conversion rate has not improved from below 0.5% to above 0.5%, this is a product-market fit signal, not a messaging issue. Log in WORKLOG.md and review the Phase 2 readiness scoring criteria in `phase-2-launch-analytics-dashboard-template.csv` Sheet 5.

**Success criteria**: Conversion rate above 0.5% for 3 consecutive days.
**Rollback**: If price discount reduces AOV without increasing total revenue, revert prices to original. Measure daily revenue (not just orders) as the success metric.

---

## Scenario 2: Photos Fail (Canva Rendering Issues or Stock Images Unavailable)

**Decision owner**: You (sole operator)
**Detection window**: May 12–17 (editing and compositing window after May 10-11 shoot) or at any point between May 12 and May 28 when uploading to Etsy
**Trigger condition**: Canva export produces corrupted or blank files, OR lifestyle photos from the shoot are not usable (exposure, blur, or framing problems make editing impossible)

### Root Cause Diagnosis

**Diagnosis A — Canva export failure** (files produced but corrupted or blank):
1. Try exporting a simple 1-page test document in Canva to confirm whether export is broken account-wide or only for zone card files.
2. If test exports work: the zone card files themselves have a corrupt element. Try duplicating the page in Canva and re-exporting the duplicate.
3. If test exports fail: browser issue. Clear cache, try incognito, try a different browser. If all fail: Canva service disruption — check canva.com/status.
4. If Canva account is inaccessible: contact Canva support at canva.com/help. Free tier accounts are rarely blocked; if blocked, resolution typically occurs within 24 hours.

**Diagnosis B — Physical photos unusable** (exposure/blur):
1. Import all photos from the shoot to Snapseed or Lightroom Mobile. Look for: focus on the product (not the background), sufficient exposure to show product details, no motion blur.
2. If fewer than 10 of 30 shots are usable: partial shoot failure. Use the usable shots for priority products and use Cluster D/E stock compositing for the remaining products.
3. If 0 shots are usable: complete shoot failure. Activate the stock-compositing-only path (all 21 products use Cluster D/E stock images from `assets/stock-raw/`).

---

### Recovery Procedures

**Recovery A1 — Canva export failure (browser fix):**
1. Clear browser cache (Chrome: Settings > Privacy > Clear Browsing Data > Cached Images and Files)
2. Try Canva in a new incognito window
3. Try in Firefox or Safari if Chrome is the default
4. If export works after browser reset: export all zone card PDFs immediately and save locally as backup
5. Upload to Google Drive and copy download URLs to WORKLOG.md before closing any Canva sessions
6. Timeline: 30–60 minutes

**Recovery A2 — Canva export failure (fallback to Figma):**
Full Figma fallback is documented in `phase-2-contingency-playbook.md` Scenario 3, Recovery Option B. Summary:
- Create a free Figma account at figma.com
- Import Brand Kit colors and fonts
- Rebuild Zone 5 master card in a new Figma frame (1200×900px)
- Duplicate for Zones 6–10; complete Zones 3 and 4 last
- Export as PDF from Figma: File > Export > PDF
- Timeline: 3–4 hours for the Zone 5 master, 30 minutes per additional zone clone

**Recovery B1 — Partial photo failure (10–29 usable shots):**
1. Identify which products have usable lifestyle photos from the shoot
2. Upload usable photos to Etsy slots 4–5 for those products immediately
3. For remaining products: use Cluster D/E stock compositing from `assets/stock-raw/` via Canva
4. Canva compositing: open a new Canva design > set dimensions to 2400×2400px > place the stock image > add product PDF print overlay > export as JPEG
5. Timeline: 30 minutes per composite image; 5 products × 2 images = approximately 5 hours for the full 10-image batch

**Recovery B2 — Complete photo failure (0 usable shots):**
1. Confirm: all 10 stock images in `assets/stock-raw/` are valid and usable
2. Build all 21 products × 2 image slots via Canva compositing (42 total images)
3. Timeline: 30 minutes per image = 21 hours total. Allocate across May 15–28 in 2–3 hour daily sessions.
4. Communication plan: no public communication needed — buyers see finished listing images, not behind-the-scenes. Do not announce the stock image use on social media unless directly asked.
5. Social content pivot: replace lifestyle-photo-dependent social posts (Reels showing the flat-lay setup) with educational content that does not require product photography. The social-posting-scheduler.csv has educational posts for every day — use those instead.

### Communication Plan

No external communication is required for Canva or photo failures. These are internal production issues. Buyers see the finished listing — they do not need to know production details.

If launch is delayed past May 30 due to photo failure, post on social media: "Phase 2 drops [new date]. Get your free zone card in the meantime at the link in bio." Frame the delay as anticipation-building, not a problem.

### Success Criteria

All 21 Etsy listings have 5 images in all slots (slots 1–3 mockups, slots 4–5 lifestyle or composite) before May 30 10:00am UTC.

### Rollback Procedure

If Canva compositing cannot be completed before May 30: launch with only lifestyle images for the products that have them (minimum 5 products). Do not delay the email broadcast or social posts. Post partial-image listings and add remaining images over the following week. Etsy does not penalize listings for having fewer than 5 images — the listing remains active.

---

## Scenario 3: Email Delivery Issues (List Bounces, ISP Blocks)

**Decision owner**: You (sole operator)
**Detection window**: T+4h after any broadcast or at any point when monitoring Kit analytics
**Trigger condition**: Hard bounce rate above 1% on any single send, OR open rate drops to 0% for a specific email domain, OR Kit reports delivery failures

### Root Cause Diagnosis

**Diagnosis A — High hard bounce rate (above 1%):**
In Kit > Broadcasts > [broadcast] > Stats > Bounced tab:
- Are bounces concentrated in one specific email domain (e.g., all @aol.com addresses)?
  - YES: ISP-level block. Go to Recovery A (ISP whitelist).
  - NO: Spread across multiple domains — likely invalid email addresses collected via form.
- What was the source of the bouncing addresses? If they came from a single sign-up burst (e.g., all signed up within one hour), suspicious activity may have submitted fake emails via your form.

**Diagnosis B — Zero open rate for a specific domain:**
In Kit > Broadcasts > Stats > Opens tab: filter by email domain. If all @gmail.com addresses show opens but all @hotmail.com addresses show 0 opens, Hotmail/Outlook is likely spam-filtering Kit's emails.

**Diagnosis C — Sender domain authentication failure:**
In Kit > Settings > Email Settings > Sender Authentication: verify that SPF and DKIM records show green checkmarks. If any record shows an error, your emails are going to spam at high rates across all providers.

---

### Recovery Procedures

**Recovery A — ISP whitelist request:**
1. Identify the blocking ISP from Kit's bounce report (domain = the ISP)
2. Contact Kit support at support.kit.com: describe the issue, the affected domain, your sender email address, and your approximate list size
3. Kit uses SendGrid's infrastructure — Kit support can escalate to SendGrid's ISP relations team
4. Request SendGrid to contact the blocking ISP's postmaster directly
5. Timeline: 24–72 hours for ISP delisting requests. Most ISPs respond within 48 hours.
6. During the waiting period: send a manual follow-up to affected subscribers via Gmail with the zone card PDF attached. Subject: "Resending your zone card — our email had a delivery issue."

**Recovery B — List cleaning procedure:**

If bounce rate is above 1% due to invalid email addresses:

1. In Kit > Subscribers > export all subscribers as CSV
2. Open the CSV and review for obvious patterns: all-numeric usernames, domains that do not exist (e.g., @test.com, @example.com), duplicate addresses
3. Remove obvious invalid addresses from the CSV
4. Import the cleaned list back into Kit: Subscribers > Import > CSV > map fields correctly
5. Before re-importing: check that Kit will not create duplicates (Kit de-duplicates by email address by default)
6. Add form protection to prevent future spam signups: Kit > Forms > [form name] > Settings > enable reCAPTCHA (if available in your Kit tier) or add a honeypot field (a hidden form field that bots fill in but humans do not — submissions with that field filled are discarded automatically)

**Recovery C — Sender domain authentication fix:**

1. Kit > Settings > Email Settings > Sender Authentication > verify which record is failing
2. Go to your domain registrar's DNS management panel (where you manage [yourdomain].com DNS records)
3. Add or correct the SPF record: typically `v=spf1 include:mail.kit.com ~all` — confirm exact record from Kit's setup page
4. Add or correct the DKIM record: Kit provides two CNAME records; add both to your DNS
5. DNS changes propagate within 15 minutes to 48 hours
6. After propagation: return to Kit settings and verify green checkmarks appear
7. Once authenticated: open rates will improve over 2–4 weeks as Gmail's algorithm re-evaluates inbox placement

**Recovery D — Gmail Promotions tab issue:**

If most of your subscribers are on Gmail and open rates are low despite correct authentication, emails may be routing to the Promotions tab instead of Primary inbox.

- This is not a deliverability error — emails are delivered, just deprioritized
- Resolution: in the next email you send, add a line: "Pro tip — move this email to your Primary inbox by dragging it from Promotions, and Gmail will put future emails there automatically."
- Do not attempt to game Gmail's filters by removing links or altering content — this violates anti-spam guidelines

### Timeline

| Recovery Action | Timeline |
|---|---|
| ISP whitelist request (Kit to SendGrid to ISP) | 24–72 hours |
| List cleaning (manual review and re-import) | 2–4 hours |
| DNS authentication fix (add records) | 15 min – 48 hours (DNS propagation) |
| Gmail inbox placement improvement (after auth fix) | 2–4 weeks |

### Success Criteria

- Hard bounce rate below 0.5% on the next broadcast after list cleaning
- Open rate above 25% for the next broadcast after authentication fix
- No ISP-specific 0% open rate domains remain in the list after ISP whitelist resolution

### Rollback Procedure

If Kit is permanently unable to resolve an ISP block: export the full subscriber list from Kit as CSV and migrate to an alternative sender (Mailchimp or ActiveCampaign) for the affected domain's subscribers only. This is a last-resort option and adds significant operational complexity — attempt all recovery steps in order before considering migration.

---

## Scenario 4: Social Platform Account Lockout

**Decision owner**: You (sole operator)
**Detection window**: Any day May 30 – June 27
**Trigger condition**: Unable to log into a social platform account, OR account shows restricted status, OR content is removed without warning

### Prevention Checklist (Complete Before May 30)

Before launch day, take these steps to minimize lockout risk:

- [ ] **Two-factor authentication (2FA)**: Enable on all three accounts. Use an authenticator app (Google Authenticator or Authy), not SMS — SMS 2FA can be social-engineered but authenticator apps cannot.
- [ ] **Save backup codes**: All three platforms provide one-time backup codes when 2FA is enabled. Print or save in a secure location separate from your phone.
- [ ] **Verify business account status**: Instagram and TikTok business accounts receive more liberal algorithm treatment and faster support response. Confirm both are set to "Business" or "Creator" account type.
- [ ] **Avoid rapid-action patterns on launch day**: Uploading 3 videos in 5 minutes, following 50 accounts in an hour, or posting 10 times in one day triggers spam detection. Stick to the posting schedule in `phase-2-social-posting-scheduler.csv` — no more than 2 posts per platform per day.
- [ ] **Do not use third-party follower growth services**: These violate all three platforms' terms of service and trigger account reviews.

### Recovery Procedure by Platform

**Instagram lockout:**
1. Go to instagram.com on a browser (not the app) > click "Get more help" on the login screen
2. Enter your registered email address > Instagram sends a 6-digit code
3. If 2FA is blocking you and you've lost your phone: use a backup code (from the list you saved before launch)
4. If account is "under review": Instagram typically resolves review within 24–72 hours. Do not attempt to create a duplicate account while the review is active — this extends the review period.
5. Contact Instagram support: Settings > Help > Report a Problem. Describe that your business account was incorrectly flagged.
6. While locked out: shift Instagram social content to Pinterest and TikTok. All scheduled Instagram posts have TikTok and Pinterest equivalents in the social scheduler.

**TikTok lockout:**
1. TikTok app > Log In > "Forgot password" > verify via registered email
2. If account is restricted for content policy review: TikTok's review team contacts you via the email on file within 48 hours. Wait for contact before escalating.
3. If age verification triggers a hold: submit ID verification in-app (Settings > Privacy > Account > Verify Identity)
4. Contact TikTok Creator Support if hold extends beyond 48 hours
5. While locked out: shift TikTok content to Instagram Reels (same video content — TikTok and Instagram Reels have near-identical audiences in this niche)

**Pinterest lockout:**
1. Pinterest > Log in > "Forgot your password?" > enter registered email
2. If account is suspended: Pinterest support at help.pinterest.com responds within 48 hours
3. Pinterest is the lowest-risk platform for lockouts — the platform has more permissive policies for content creators and business accounts
4. While locked out: temporarily redirect Pinterest link-in-bio clicks to the Instagram profile instead

### Alternative Platform Fallback

If any platform lockout extends beyond 5 days without resolution:

| Locked platform | Content shift | Impact |
|---|---|---|
| Instagram | Shift Reels to TikTok; shift Carousels to Pinterest carousel pins | Moderate — Instagram is primary audience-building platform |
| TikTok | Shift all video content to Instagram Reels | Low — TikTok audience and Instagram Reels audience overlap significantly |
| Pinterest | Shift pin production to a 2-week delay | Low — Pinterest traffic is evergreen and not time-sensitive |

At no point does a platform lockout require pausing the Kit email automation or Etsy listings — those are fully independent of social account status.

### Success Criteria

Account restored and able to post within 72 hours of lockout.

### Rollback Procedure

If one account cannot be restored within 7 days: close the locked account (after documenting all followers count and post performance data) and create a new account under the fallback handle (@seedwarden.co, @seedwarden.seeds, or @seedwarden_guides per the handle fallback documented in `phase-2-contingency-playbook.md` Scenario 5). Post an announcement on the other two active platforms: "New [platform] account — follow us at [new handle] for the same content."

---

## Scenario 5: Demand Spike Exceeds Inventory (or Supplier Capacity)

**Decision owner**: You (sole operator)
**Detection window**: T+6h on May 30, then daily through June 2
**Trigger condition**: More than 20 orders arrive within any 24-hour window, AND your supplier has not confirmed they can fulfill within 3 business days, OR your supplier explicitly says they cannot meet the order volume

**Note on digital products**: If all 21 Phase 2 products are digital downloads (PDFs delivered via Etsy), there is no inventory constraint — Etsy delivers downloads automatically to every buyer instantly. This scenario applies only if Phase 2 includes physical products (printed guides, seed packets, physical bundles) that require supplier fulfillment.

**If all products are digital downloads**: Skip this scenario. Demand cannot exceed inventory for digital goods. Monitor Etsy platform status instead — if Etsy is slow processing payments or deliveries, contact Etsy seller support.

### Scaling Procedure (Physical Products)

**Step 1 — Confirm order volume (T+6h, May 30)**

Open Etsy Shop Manager > Orders > filter by "Open." Count orders. Compare to supplier capacity confirmation from T-24h check (documented in `TRACK_B_LAUNCH_DAY_OPERATIONS_GUIDE.md` Section 1).

| Order count | Supplier status | Action |
|---|---|---|
| Under 20 orders | Confirmed capacity | No action — normal operations |
| 20–40 orders | Confirmed capacity | Send supplier heads-up: "Volume tracking toward 40 orders — please confirm you can handle that by June 2." |
| 20–40 orders | Not confirmed | Contact supplier immediately — get written confirmation of fulfillment timeline |
| 40+ orders | Any | Activate demand management protocol below |

**Step 2 — Demand management protocol (if orders exceed confirmed capacity)**

1. Do not cancel existing orders — fulfill all orders already placed
2. Add a fulfillment delay notice to all Etsy product pages: "Due to high demand, orders placed after [time] on May 30 will ship June 3–5. We'll send tracking as soon as your order ships. Thank you for your patience."
3. If digital and physical products are mixed: continue selling digital products normally (no inventory constraint); apply fulfillment delay notice only to physical products
4. Contact the supplier: "We have [X] orders. Current capacity is [Y]. We need [Z] additional units by [date]. Can you fulfill?"
5. If supplier cannot expand: activate the waitlist strategy below

**Step 3 — Waitlist strategy**

If supplier capacity is definitively exceeded and additional units cannot be sourced within 72 hours:

1. Remove the "Add to Cart" button from the affected product listings: Etsy Shop Manager > Listings > [listing] > edit Quantity to 0 (this marks the listing as "sold out" and removes the cart button)
2. Add text to each affected listing description: "SOLD OUT — join the waitlist to be notified when we restock. Link in bio."
3. Create a simple waitlist form: Google Forms > "Seedwarden Waitlist" > fields: Name, Email, Which product interests you? > collect responses to a Google Sheet
4. Update all social bios to link to the waitlist form instead of the Kit zone card landing page
5. Send an email broadcast to the Kit subscriber list: "We sold out faster than expected. We're restocking [product] by [date]. Join the waitlist and you'll be first to know." Include the waitlist form link.
6. Post on all social platforms: "We sold out. Here's what happened and when we restock." Frame as success, not failure.

### Communication to Customers Who Already Ordered

For customers who placed orders before the sold-out notice, send a proactive update via Etsy's messaging system within 12 hours of discovering the delay:

"Thank you for your order! Due to overwhelming demand for Phase 2, we're processing a slightly larger batch than planned. Your order will ship [new date]. I'll send tracking as soon as it's on its way. Thank you for your patience — we'll make it worth the wait."

Do not wait for customers to message you about delays. Proactive communication prevents 80% of negative reviews caused by fulfillment delays.

### Post-Launch Mitigation (After June 2)

Once the initial surge is fulfilled:
1. Update supplier agreement to include a 48-hour surge buffer (supplier agrees to keep 20 additional units on standby for the first 30 days of any new product launch)
2. For future launches: pre-manufacture 30% more units than the baseline forecast before announcing launch date
3. Document the surge volume (peak orders per 24-hour window) in WORKLOG.md — this becomes the input for Phase 3 inventory planning

### Success Criteria

- All orders placed before sold-out notice are fulfilled within 5 business days
- Waitlist captures at least 50% of demand that arrived after sold-out notice
- No negative reviews citing fulfillment delay

### Rollback Procedure

If the waitlist strategy generates more waitlist signups than the supplier can fulfill in the next production run: offer a digital-only version of the same product as an interim alternative. Announce via email and social: "While we restock the physical guide, we're making the digital PDF available immediately at a lower price. Waitlist members get a coupon for the physical edition when it restocks."

---

## Quick Reference Decision Tree

```
CONVERSION BELOW 0.5%?
  Is traffic below 50 visits/day?
    YES (Traffic Problem)
      → Check Kit broadcast delivery: Kit > Broadcasts > Stats > Delivered
      → Check bio links on all 3 platforms: tap each link manually
      → Check Buffer social post status: published or failed?
    NO (Conversion Problem, traffic is fine)
      → Check listing first image: does it accurately represent the product?
      → Check listing description: does it state "digital PDF download" in first paragraph?
      → Check price vs. Etsy competitors: are you priced 50%+ higher?
  Escalation: If below 0.5% for 7+ days after remediation → log in WORKLOG.md, review Decision Framework sheet

PHOTOS FAIL?
  Is Canva accessible?
    YES → Try incognito browser, clear cache, try different browser
    NO → Contact Canva support; rebuild in Figma (3-4 hours) if no response within 24h
  Are physical shoot photos usable?
    YES (10+ usable shots) → Edit and upload usable shots; composite remaining via stock images
    NO (0 usable shots) → Use stock compositing for all 21 products from assets/stock-raw/

EMAIL DELIVERY ISSUES?
  Hard bounce rate above 1%?
    → Check Kit bounce report by domain
    → Is it one domain (ISP block)? Contact Kit support for whitelist request
    → Is it spread (invalid emails)? Clean the list via CSV export and re-import
  Open rate dropped to near 0%?
    → Check Kit > Settings > Email Settings > Sender Authentication (green checkmarks?)
    → If authentication error: add SPF/DKIM DNS records (15 min to add, up to 48h to propagate)

SOCIAL ACCOUNT LOCKED?
  Instagram: instagram.com > Get more help > verify email or use backup code
  TikTok: App > Forgot password, or ID verification in Settings > Privacy
  Pinterest: help.pinterest.com email support
  While locked: shift content to other 2 platforms; email and Etsy operations are unaffected

DEMAND SPIKE?
  Are products digital-only? → No inventory constraint; skip this scenario
  Orders above 20 in 24h?
    → Contact supplier immediately for updated fulfillment confirmation
    → If supplier capacity exceeded: add delay notice to listings, activate waitlist form
    → Message all pending customers proactively with new fulfillment date
```

---

## Per-Scenario Summary Reference

| Scenario | Decision Owner | Success Criterion | Rollback |
|---|---|---|---|
| 1: Low Conversion | You | CVR above 0.5% for 3 consecutive days | Revert price changes if AOV drops without revenue improvement |
| 2: Photos Fail | You | All 21 listings have 5 images before May 30 10:00am UTC | Launch with partial images and add remaining within 1 week |
| 3: Email Delivery | You | Hard bounce below 0.5%; open rate above 25% after fix | Migrate affected subscribers to alternate email sender |
| 4: Social Lockout | You | Account restored and posting within 72 hours | Create new handle; announce migration on active platforms |
| 5: Demand Spike | You | All orders fulfilled within 5 days; waitlist captures overflow demand | Offer digital-only interim version to waitlist members |

---

*Prepared: 2026-05-09. This playbook covers post-launch automation failures. Pre-launch failure modes (photo delay, Kit block, Canva failure, social account creation issues) are documented in `phase-2-contingency-playbook.md`. References: `TRACK_B_LAUNCH_DAY_OPERATIONS_GUIDE.md` (checkpoint thresholds), `phase-2-post-launch-analytics-framework.md` (success benchmarks), `phase-2-email-automation-sequence.md` (email delivery handling).*
