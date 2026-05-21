---
title: "Affiliate Partnership Framework — Phase 3 Launch"
prepared: 2026-05-21
status: production-ready
phase: Phase 3 pre-launch
purpose: >
  Formal affiliate program structure for Seedwarden Phase 3 medicinal herbs launch.
  Covers commission tiers, co-marketing assets, referral tracking, payout schedule,
  agreement terms, and performance expectations. Designed for June 22, 2026 launch.
word-count: ~2,000
cross-references:
  - AFFILIATE_PARTNERSHIP_MATRIX.csv
  - PRACTITIONER_FIRST_CONTACT_SEQUENCE.md
  - HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md
  - PRACTITIONER_RELATIONSHIP_ROADMAP.md
  - CMARKETING_PARTNERSHIP_OPPORTUNITIES.md
tags: [seedwarden, phase-3, affiliate, partnership, commission, marketing]
---

# Affiliate Partnership Framework
## Phase 3 Medicinal Herbs Bundle — June 22, 2026 Launch

**Prepared**: May 21, 2026
**Launch date**: June 22, 2026
**Affiliate program live date**: June 15, 2026 (one week pre-launch for partner testing)
**Program type**: Native Etsy coupon code tracking (Phase 3); Payhip Pro migration planned for Phase 4

---

## 1. Program Overview

### 1.1 Why This Structure

The Phase 3 affiliate program is intentionally simple. Seedwarden sells on Etsy; Etsy's native coupon code system provides per-influencer tracking at zero setup cost. Each affiliate receives a unique 15% discount coupon code. Sales linked to each code appear in Etsy's coupon redemption report. Monthly PayPal payouts eliminate platform fee overhead. The system scales to 15 active affiliates before spreadsheet management becomes burdensome.

Phase 4 recommendation: Migrate to Payhip Pro ($99/month, 0% transaction fee) with a built-in affiliate dashboard once Phase 3 volume is established and a direct storefront makes strategic sense. This is the correct moment to invest in software — not before launch.

### 1.2 Competitive Context

Standard affiliate commission rates in the herbalism and wellness digital guide space:
- Amazon Associates (gardening/plants category): 3%, 24-hour cookie
- Etsy Affiliate (via Awin): 4%, 30-day cookie
- Herbal Academy affiliate (for affiliates promoting HA courses): 15%, 21-day cookie
- Mountain Rose Herbs (for affiliates promoting MRH products): 10%, unspecified window
- Typical wellness product digital affiliate: 10–20%, 30-day cookie

Seedwarden Phase 3 rates are set above the bottom of this range to attract practitioners who have audience trust worth more than mass-reach influencers. An RH practitioner with 2,000 highly engaged followers converts at a higher rate than a generalist with 50,000 casual followers.

---

## 2. Commission Tiers

### Tier 1 — AHG/NAMA-Credentialed Practitioners

**Eligibility**: Registered Herbalists (AHG), licensed Naturopathic Doctors (ND), certified NAMA practitioners (AHC/AP/AAP/AV), and NPs in integrative settings.

**Commission rate**: 20% of sale price per referred purchase
**Discount offered to their audience**: 15% off using their unique code
**Cookie window**: N/A (coupon code tracking — sale is attributed to the code, not a cookie)
**Minimum payout**: $25 (no minimum required before first payout — first payout triggered immediately once threshold met)
**Payout schedule**: Monthly on the 1st for prior-month sales
**Payment method**: PayPal (primary); Venmo accepted on request
**Additional benefits**:
- Complimentary full practitioner bundle (5 guides, $120–$150 value) upon program activation
- Named credit on Seedwarden Etsy listings if peer review is provided ("Reviewed by [Name], RH (AHG)")
- First access to Phase 4 bundle preview for early review opportunity

**Rationale for 20%**: The credentialed practitioner endorsement converts at 2–4x the rate of a general wellness influencer recommendation. The premium commission compensates for a smaller audience and recognizes the credibility transfer value. At $40/bundle sale, 20% = $8 per conversion. At $120 practitioner bundle, 20% = $24 per conversion. Five sales per month from one credentialed partner = $40–$120/month.

---

### Tier 2 — Independent Practitioners and Educators (Non-Credentialed or Credential-Unverified)

**Eligibility**: Practicing herbalists without formal AHG/NAMA credential but with demonstrated practitioner-level audience (herb school instructors, long-form educators, community practitioners). Minimum 500 engaged social followers or equivalent active email list.

**Commission rate**: 15% of sale price per referred purchase
**Discount offered to their audience**: 15% off using their unique code
**Payout schedule**: Monthly on the 1st for prior-month sales
**Payment method**: PayPal
**Additional benefits**:
- Complimentary single bundle (partner's choice) upon program activation

**Rationale for 15%**: Aligns with Herbal Academy's affiliate rate (the most credible comparable benchmark in this market). Competitive with standard wellness digital affiliate rates. Recognizes audience trust without the clinical credibility premium.

---

### Tier 3 — Media Channels and Distribution Partners

**Eligibility**: Newsletters, podcasts, schools, and organizations that distribute Seedwarden content to their audience (Mountain Rose Herbs, LearningHerbs, Herbal Academy affiliate placement, UpS newsletter, AHG chapter newsletters).

**Commission rate**: 10% of referred sales OR flat newsletter placement fee (negotiated case-by-case)
**Discount offered to their audience**: 10–15% off (negotiated; higher discount for larger lists)
**Payout schedule**: Monthly on the 1st
**Payment method**: PayPal or check (for organizations)
**Additional benefits**:
- Co-branded content assets (email snippet, social caption, product images)
- Reciprocal editorial mentions where appropriate (e.g., Seedwarden blog post featuring partner organization's mission)

**Rationale for 10%**: These partners drive volume, not conversion-depth. A newsletter mention to 10,000 subscribers at 0.5% conversion rate = 50 sales. At $40 average bundle price, 10% = $2,000 Seedwarden revenue on which the partner earns $200. This is fair value for a single newsletter placement. Flat fees ($50–$150 per newsletter issue) are an alternative where ongoing performance tracking is not practical.

---

## 3. Referral Tracking

### 3.1 Etsy Coupon Code System (Phase 3 Primary Method)

Each affiliate receives a unique alphanumeric coupon code. Code naming convention: `[FIRSTNAME][2-digit number]` — for example `ROSALEE15`, `JADE15`, `MASON15`. The trailing number represents the discount percentage.

**How tracking works**:
1. Affiliate shares their unique code with their audience verbally, in email, or on social media
2. Buyer applies the code at Etsy checkout — 15% is deducted from list price
3. Etsy records the coupon redemption in the seller's shop manager coupon report
4. Monthly: export Etsy coupon report, calculate revenue attributable to each code, compute commission, send PayPal payment

**Reporting to affiliates**: Each affiliate receives a monthly plain-text earnings statement (email) on the 5th of the following month, showing:
- Number of sales attributed to their code during the prior month
- Gross revenue attributed
- Commission amount
- PayPal payment confirmation

### 3.2 UTM Parameter Tracking (For Link-Based Affiliates)

For affiliates who prefer to drive traffic via a trackable URL (e.g., in a newsletter or blog post) rather than a coupon code:

UTM format:
```
https://www.etsy.com/shop/seedwarden?utm_source=[partner_slug]&utm_medium=affiliate&utm_campaign=phase3_launch&utm_content=[content_type]
```

Examples:
- Mountain Rose Herbs newsletter: `...&utm_source=mountainrose&utm_medium=email&utm_campaign=phase3_launch&utm_content=newsletter_june`
- HerbRally podcast mention: `...&utm_source=herbrally&utm_medium=podcast&utm_campaign=phase3_launch&utm_content=episode_mention`

UTM data is visible in Google Analytics (GA4) linked to Etsy. Track in the GA4 Acquisition > Traffic Acquisition report filtered by `utm_source`.

Note: UTM tracking is supplemental. For commission calculation, the Etsy coupon code report is the authoritative source. UTM data provides attribution context for traffic analysis, not payout calculation.

### 3.3 Tracking Limitations and Dispute Resolution

The coupon code system has one limitation: it cannot track a sale where the buyer discovers the product through the affiliate's content but does not apply the affiliate's code at checkout. This is a known limitation of all coupon-code affiliate systems.

**Policy**: Commission is paid only on sales confirmed via coupon code attribution. If a partner believes they drove significant unconverted traffic (discoverable via UTM), Seedwarden may offer a one-time goodwill payment at its discretion. This is not a contractual obligation.

If a commission dispute arises, the Etsy coupon report is the binding record. Disputes must be raised within 30 days of the monthly statement.

---

## 4. Co-Marketing Assets

Each confirmed affiliate receives a co-marketing asset package within 48 hours of program activation. All assets are editable to the partner's voice.

### Asset 1 — Email Snippet (150 words)

Ready to paste into the affiliate's newsletter. Two versions: (A) general audience (students/enthusiasts), (B) clinical practitioner audience.

**Version A (general audience)**:

> I wanted to share something I came across recently that I think you will find genuinely useful — a new series of printable medicinal herb guides from Seedwarden, launching June 22.
>
> What sets these apart: evidence-tiered therapeutic claims (they actually tell you whether something is RCT-backed or traditional use), complete contraindication tables, and cultivation guides for the species they cover. The sourcing section includes United Plant Savers at-risk status and Forest Grown Verified alternatives — which I appreciate.
>
> If you have been looking for a reference you can hand to clients or use in a workshop, use code [AFFILIATECODE] for 15% off. They are available at seedwarden.etsy.com.

**Version B (clinical practitioner audience)**:

> A practitioner-grade plant reference worth examining: Seedwarden's medicinal herbs bundle (launching June 22) covers five clinical herb categories with evidence-tiered claims, drug-herb interaction tables, and FTC-compliant client-facing language. Correct Latin binomials, dosage ranges by preparation method, CITES guidance for Goldenseal. Reviewed by RH practitioners. Use [AFFILIATECODE] for 15% off at seedwarden.etsy.com.

### Asset 2 — Social Media Captions (Instagram/Facebook)

Two caption variants per bundle. Example for Women's Health bundle:

**Caption A (educational angle)**:
> Black Cohosh (*Actaea racemosa*), Vitex (*Vitex agnus-castus*), Red Raspberry (*Rubus idaeus*) — three of the most clinically relevant women's health herbs in one printable reference.
>
> Seedwarden's Women's Health bundle includes evidence-tiered therapeutic claims, complete contraindication tables, and cultivation instructions. Forest Grown Verified sourcing guidance for at-risk species. FTC-compliant language for clinical distribution.
>
> Launching June 22. Code [AFFILIATECODE] saves you 15%: seedwarden.etsy.com

**Caption B (community angle)**:
> The reference guide I wish existed when I started practicing — all the clinical detail, evidence tiers, drug interactions, and cultivation in one printable format. Seedwarden's Women's Health bundle is exactly that. [AFFILIATECODE] for 15% off. Link in bio.

### Asset 3 — Product Images for Social

Three product-style images provided (Etsy-hosted):
1. Cover page mockup with bundle title and species list
2. Sample spread showing evidence-tier legend and contraindication table structure
3. Sourcing section sample showing UpS at-risk status notation

Image files will be shared via Google Drive link in the asset delivery email.

### Asset 4 — Landing Page Section (For Affiliate Websites/Blogs)

300-word description block with headline, features list, and a "buy with code" CTA. Formatted in plain HTML and plain text. Can be embedded in any affiliate's website.

---

## 5. Payout Schedule

| Month | Period Covered | Statement Sent | Payment Sent |
|-------|---------------|----------------|-------------|
| July 2026 | June 22–30 (launch week) | July 5 | July 7 |
| August 2026 | July 1–31 | August 5 | August 7 |
| September 2026 | August 1–31 | September 5 | September 7 |
| October 2026 | September 1–30 | October 5 | October 7 |

**Minimum payout**: $10 cumulative earned before PayPal payment is sent. Earnings below $10 roll to the next month. No expiration on accrued earnings.

**International partners**: PayPal USD payments sent to any PayPal account. Partner is responsible for any currency conversion fees. No alternative payment method currently available.

---

## 6. Agreement Terms

### 6.1 What the Agreement Covers

The Seedwarden affiliate agreement is a plain-language email confirmation, not a formal contract. For Tier 1 and Tier 2 individual practitioners, the agreement is the reply to the first-contact email confirming participation. For Tier 3 organizational partners (newsletters, schools), a one-page agreement letter is used.

**Core terms (all tiers)**:

- Affiliate agrees to represent the product accurately, using the provided asset language or equivalent
- Affiliate will not make health claims beyond what is included in the provided co-marketing assets
- Affiliate agrees to include an affiliate disclosure in any promotional communication (FTC requirement): "I may earn a commission on purchases made using my discount code"
- Seedwarden reserves the right to terminate the program with 30 days' notice
- Commission rates are fixed for the calendar year of activation; adjusted rates communicated 60 days in advance

### 6.2 No NDA Required

Phase 3 affiliate partners are not required to sign an NDA. Product content is not proprietary in a way that requires legal protection at this stage. Affiliates may discuss the guides' content, approach, and methodology freely.

### 6.3 Exclusivity

This is a non-exclusive arrangement. Affiliates may simultaneously promote other herb guides, reference materials, or educational products.

### 6.4 Termination

Either party may end the arrangement at any time by email notice. Accrued commissions are paid within 30 days of termination.

---

## 7. Performance Expectations and Tier Status

### Tier Maintenance

| Tier | Initial Eligibility | Annual Minimum Activity | Consequence of Inactivity |
|------|---------------------|------------------------|--------------------------|
| Tier 1 | AHG/NAMA credential + confirmed | 1 sale in any 6-month period | Downgrade to Tier 2 after 6 months of zero sales |
| Tier 2 | Independent practitioner, 500+ followers | 1 sale in any 6-month period | Code deactivated after 12 months of zero sales |
| Tier 3 | Organizational partner | Per negotiated agreement | Renewal negotiated annually |

### Affiliate Deactivation

A unique coupon code is deactivated (not deleted) after 12 consecutive months of zero redemptions. The affiliate is notified by email 30 days before deactivation. Codes can be reactivated on request at any time.

### Performance Bonuses (Phase 3 Trial)

As a Phase 3 launch incentive, any affiliate who generates 10 or more sales in the first 30 days (June 22–July 22) will receive a 5% commission bonus on all sales in July 2026. This is a one-time launch incentive, not a recurring program feature.

---

## 8. Phase 4 Upgrade Path

When Phase 3 monthly revenue reaches $1,500+ consistently (estimated October 2026 based on projections in PHASE_3_OPTION_ANALYSIS.md), migrate to Payhip Pro:
- $99/month platform fee
- 0% transaction fees (saves ~5% vs. Etsy transaction fees on high-volume sales)
- Built-in affiliate dashboard with automated payouts, real-time tracking, and self-serve portal for affiliates
- Custom storefront branded as Seedwarden, removing Etsy platform dependency

The Payhip migration is also the moment to formalize affiliate agreements with proper contracts for any partners generating $500+/month in commissions.

---

*Document version 1.0 — May 21, 2026.*
*Cross-references: AFFILIATE_PARTNERSHIP_MATRIX.csv, PRACTITIONER_FIRST_CONTACT_SEQUENCE.md, CMARKETING_PARTNERSHIP_OPPORTUNITIES.md.*
*Next action: Activate Tier 1 codes for first confirmed partners by June 15. First payout July 7 covering launch-week sales.*
