---
title: "Seedwarden Email Automation Blueprint"
date: 2026-04-27
status: ready-to-implement
platform: Kit (ConvertKit)
prerequisite: Phase 1 Etsy live, Kit account created
tags: [email, automation, kit, lead-magnet, funnel, seedwarden]
---

# Seedwarden Email Automation Blueprint

**Purpose**: This document is the implementation guide for the full email funnel — from lead magnet to re-engagement. It complements the existing email-and-launch-plan.md (which documents the 5-email welcome sequence in full) and the annual-product-plan.md (which covers the seasonal campaign strategy). This document covers the technical architecture: what automations to build, what triggers them, and how to measure whether they are working.

---

## Part 1: Lead Magnet

### Recommended Lead Magnet: The Seedwarden Zone Quick-Start Card

**Concept**: A single-page printable PDF personalized to the subscriber's USDA hardiness zone, covering three things:
1. When to start seeds indoors (6 crops, with specific dates for their zone)
2. Last frost date range for their zone
3. Three heirloom varieties that perform well in their zone's climate

**Why this outperforms the alternative**: The existing email-and-launch-plan.md proposes a 5-variety guide (strong, already written, immediately deployable). The Zone Quick-Start Card adds one important dimension: personal relevance. A subscriber in Minnesota gets information calibrated to their climate, not generic advice that could apply to anyone. This personalization drives higher completion rates (people read the whole thing) and higher perceived value ("this was written for my situation").

**Simpler alternative if zone customization is too complex to implement initially**: Keep the existing "5 Heirloom Varieties for Small Spaces" guide from email-and-launch-plan.md. It is well-written and deployable today. Add a zone-specific quick-start card as a Phase 2 email upgrade once the list reaches 500 subscribers.

**Format**: 1 page (2 pages maximum), PDF, Canva-designed. Clean layout: Seedwarden branding, botanical illustration or seed photography, clear typography. File size under 2MB. Hosted on Google Drive or Dropbox with anyone-with-link access.

**Delivery mechanism**: Kit form → automation → immediate email with PDF download link. Setup time: 45 minutes including form design.

**Where to promote the lead magnet**:
1. TikTok/Instagram bio link (rotated in on non-product-feature weeks)
2. Pinterest: dedicated pin for the lead magnet linking to the Kit landing page (not to Etsy)
3. Every Etsy product delivery: a page at the end of every PDF guide with "Get our free Zone Quick-Start Card: [landing page URL]"
4. End of every email in the welcome sequence: "If you found this useful, share the free guide with someone who's starting a garden this year."
5. Reddit: used organically in r/vegetablegardening, r/homesteading, r/seedsaving when answering zone-related questions

**Conversion expectations**: Cold traffic (TikTok/Instagram bio clicks) converts at 15–25% to email sign-ups if the landing page is specific and the lead magnet is genuinely useful. Warm traffic (existing Etsy buyers clicking through from PDF) converts at 25–40%.

---

## Part 2: Email Sequence Architecture

### Overview of All Automations

Kit (ConvertKit) organizes these as separate sequences. Build them in this order — the welcome sequence first, everything else after Phase 1 has real buyers.

```
AUTOMATION 1: Welcome Sequence
  Trigger: Form submission (lead magnet download)
  Duration: 10 days / 5 emails
  Goal: Deliver lead magnet, build trust, make first offer

AUTOMATION 2: Post-Purchase Sequence
  Trigger: Coupon code used OR manual tag "purchased" applied
  Duration: 21 days / 3 emails
  Goal: Onboard buyer, cross-sell, generate review

AUTOMATION 3: Weekly Newsletter
  Trigger: Subscriber completes welcome sequence
  Cadence: Every Thursday
  Goal: Relationship maintenance, seasonal product features

AUTOMATION 4: Win-Back Campaign
  Trigger: Subscriber has not opened any email in 6 consecutive sends
  Duration: 3 emails over 90 days
  Goal: Re-engage or cleanly remove inactive subscribers

AUTOMATION 5: Seasonal Campaign Broadcasts
  Trigger: Manual (sent to full list or segment)
  Frequency: 4–6 per year (Black Friday, spring planting, preservation season, etc.)
  Goal: Revenue-generating promotional sends
```

---

## Part 3: Automation 1 — Welcome Sequence (Full Detail)

The full email copy for all 5 emails is documented in email-and-launch-plan.md. This section documents the Kit setup and refinements.

### Kit Setup

1. Create a **Form** in Kit: "Seedwarden Zone Quick-Start Card" — landing page style, two fields (first name, email), one CTA button ("Send me the guide")
2. Create a **Sequence** in Kit: "Seedwarden Welcome" — 5 emails, delays as specified below
3. Create an **Automation** in Kit: Form submitted → Add to sequence "Seedwarden Welcome" → Tag subscriber with "new-subscriber"

### Email Schedule and Trigger Conditions

| Email | Subject | Delay | Condition |
|---|---|---|---|
| 1 | Your Seedwarden Starter Pack is here (+ a quick hello) | Immediately | Always send |
| 2 | The difference between an heirloom tomato and a lie | 2 days after Email 1 | Only if Email 1 was opened |
| 3 | The mistake that wiped out a full season of seeds | 5 days after Email 1 | Always send (regardless of Email 2 open) |
| 4 | What I've been building (and why digital guides made sense) | 7 days after Email 1 | Always send |
| 5 | One more thing before I stop showing up in your inbox | 10 days after Email 1 | Always send |

**Conditional send note**: Kit's conditional sending for Email 2 (only if Email 1 was opened) is optional — implement it in Phase 2 of email setup, not at launch. At launch, send all 5 emails to all subscribers who sign up.

### Behavioral Tags Applied in Welcome Sequence

In Emails 3 and 4, add click-tracked links to test which product category the subscriber is most interested in:

- Email 3 (seed saving story): Add a link to the Seed Saving Field Manual listing — subscribers who click get tagged "seed-saver"
- Email 4 (product introduction): List 3 product categories with distinct links:
  - "For apartment and container growers" → link to Apartment Plant Catalog → tag "city-grower"
  - "For seed saving and food sovereignty" → link to Seed Saving Field Manual → tag "seed-saver"
  - "For food preservation" → link to Harvest Preservation Field Manual → tag "preservationist"

These tags feed Automation 3 (newsletter) and allow segment-targeted sends.

### Coupon Code in Email 5

The SEEDWARDEN15 coupon code (15% off, 5-day expiry) is generated in the Etsy seller dashboard under Shop Manager > Coupons. Set the expiry dynamically — the code issued to each subscriber is the same code, but the 5-day clock is communicated as a deadline. Kit does not natively integrate with Etsy's coupon system, so the expiry is communicated as a deadline in the email text ("expires [date 5 days from now]") and honored manually if a subscriber contacts you after expiry with a genuine explanation. This is workable at a list size below 2,000 subscribers.

---

## Part 4: Automation 2 — Post-Purchase Sequence

### Trigger Setup

Kit does not natively receive purchase events from Etsy. Two options:

**Option A (simplest)**: Manually tag purchasers. When you see a sale in your Etsy dashboard, find the buyer's email (Etsy provides this in order details), search for them in Kit, and apply the tag "purchased" if they are on the list. This is viable up to approximately 10 sales per week — above that, consider Option B.

**Option B (automated, recommended at 20+ sales/month)**: Use Zapier to connect Etsy → Kit. Etsy triggers a Zap on new order, Zap applies tag "purchased" in Kit. Zapier Starter plan: $19.99/month. At 20+ Etsy sales per month, the automation value exceeds the cost.

### Email Schedule

| Email | Subject | Delay | Goal |
|---|---|---|---|
| 1 | Thank you — and here's what to read first | Day 1 post-purchase | Onboard, reduce buyer's remorse |
| 2 | A week in — here's what pairs well with [Product] | Day 7 post-purchase | Cross-sell / upsell |
| 3 | One thing that would help us enormously | Day 21 post-purchase | Review request |

### Email 1 — Thank You and Orientation

**Subject**: Thank you — and here's what to read first

Body: Short (under 150 words). Thank the buyer by first name. Tell them which section to read first based on the product they purchased (this requires a segment per product, or a generic version pointing to "the first section"). Ask one open question: "What are you hoping to grow or preserve this season? Reply and let me know — I read everything." This reply-encouraging question has two functions: it drives inbox deliverability (replies signal to Gmail/Outlook that the email is wanted) and it generates real product intelligence.

### Email 2 — Cross-Sell / Upsell

This email names the "natural next guide" based on what the subscriber purchased. Build one variant per major product cluster:

- **Seed Saving purchasers**: "A week with the Seed Saving Manual — here's the guide that pairs with it." → Feature Anti-Catalog (30 Heirlooms) or Food Sovereignty Bundle
- **Apartment/Container purchasers**: "Now that you've got the growing setup — here's the preservation side." → Feature Harvest Preservation or Fermented Harvest
- **Preservation purchasers**: "You've got the preservation covered — here's the growing side." → Feature Survival Garden Plans or Container Blueprint
- **Bundle purchasers**: "You've got the complete set — here's one more thing we made." → Feature the one product not included in their bundle, or the Zone Calendar

This cross-sell is not a discount. It is a "here's the natural next step" framing. No coupon code, no pressure, no countdown. Buyers who have already found value in the first product convert at a higher rate without needing an incentive.

### Email 3 — Review Request

**Subject**: One thing that would help us enormously

Body: Under 100 words. Direct: "If you've found [Product] useful, a short review on Etsy helps other growers find it. It takes about 45 seconds." Include the direct Etsy review link (the link to leave a review on a specific listing, formatted as: `https://www.etsy.com/your-etsy-username/purchases`). Do not use guilt-based language. Do not offer a discount in exchange for a review (Etsy's terms prohibit incentivized reviews). The honest, direct approach generates the best review rates.

**Expected review rate from this email**: 8–15% of purchasers who receive the email. At 10 sales/week with a 10% review rate, this generates 1 new review per week. At 52 weeks, this is 52 reviews by end of year — a meaningful trust signal.

---

## Part 5: Automation 3 — Weekly Newsletter

### Format and Cadence

- Send: Every Thursday, 8–9am Eastern
- Length: 500–800 words (shorter than originally planned in phase-3-operations-playbook.md — test shows shorter emails have higher read rates)
- Four-section structure (from phase-3-operations-playbook.md):
  1. Growing update (2–3 sentences about what's happening in your actual garden right now)
  2. Technique or tip (the main educational content, 200–350 words)
  3. Product spotlight (one product, 3–4 sentences, always includes the Etsy link)
  4. Reader question (answer one question from a recent reply or comment, 50–100 words)

### Seasonal Product Rotation in Section 3

The product featured in Section 3 of each newsletter should rotate according to the monthly product focus documented in the annual-product-plan.md and product-calendar-2026-2027.json. Do not feature preservation products in February. Do not feature seed starting guides in August. Alignment between newsletter content and actual seasonal buying intent is the single most important factor in newsletter click-through rate.

### Subject Line Formula

Ten-word maximum. Three proven formulas for this niche:
1. **Question format**: "Why do your seedlings look like that?" (curiosity gap)
2. **Specific tip format**: "How to ferment hot peppers in 4 days" (actionable)
3. **Story format**: "The seed I almost threw away (and didn't)" (narrative hook)

Avoid: Subject lines that feel like marketing ("Don't miss this week's guide!"). This audience is sophisticated about marketing tactics and will not open obvious promotional subject lines.

---

## Part 6: Automation 4 — Win-Back Campaign

### Trigger

Kit's inactivity automation: subscriber has not opened any email in 6 consecutive sends (approximately 6 weeks on weekly cadence). This is the threshold before inbox placement starts to degrade — Gmail's algorithm deprioritizes senders whose emails consistently go unopened.

### Three-Email Structure (90-day campaign)

**Email 1 (Day 0): "Are we still a good fit?"**
- Subject: "Still interested in heirloom seeds / homesteading?"
- Body: Direct. "I've noticed you haven't opened a few recent emails. That's completely okay — inboxes get full and topics shift. If you're still interested in [seed saving / growing food / homesteading], I'd love to keep sending you practical content. If not, unsubscribe below and I won't take it personally."
- Include: Link to the most popular recent newsletter content ("In case you missed it: [subject line]")

**Email 2 (Day 30): Free resource re-engagement**
- Subject: "A free resource I made that might actually be useful"
- Body: Offer a new piece of free content not previously sent — a one-page seasonal reference, a quick-start checklist, or a short guide on one specific technique. This creates a new value moment without requiring a purchase.
- Goal: Get the subscriber to click on something, which re-establishes engagement signals.

**Email 3 (Day 90): "Should I remove you from my list?"**
- Subject: "Quick question before I go"
- Body: "If you don't click the link below in the next 7 days, I'll remove you from my list. I won't be offended — it keeps the list healthy and makes sure I'm only sending to people who want to hear from me."
- Include a prominent "Keep me on the list" link that applies a "re-engaged" tag in Kit
- Anyone who does not click is removed from the active list (Kit allows this via automation)

**Why this matters**: A list of 1,000 subscribers with 40% open rate is more valuable than a list of 2,000 subscribers with 15% open rate. Email deliverability and inbox placement degrade when large portions of a list are unengaged. Pruning the list actively protects the deliverability of every other email sent.

---

## Part 7: Automation 5 — Seasonal Campaign Broadcasts

### Five Planned Broadcast Campaigns Per Year

These are one-off emails sent to the full list (or a segment) on specific occasions. They are in addition to the weekly newsletter.

| Campaign | Timing | List | Primary CTA |
|---|---|---|---|
| Spring Planting Push | First week of February | Full list | Zone Calendar + Seed Starting Kit |
| Preservation Season Launch | First week of July | Full list | Preservation Bundle |
| Fall Seed Saving | Third week of September | Full list (Seed Saver segment featured) | Seed Saving Manual |
| Holiday Gift Guide | December 3 | Full list | Homesteader's Complete Bundle |
| Black Friday Sale | Thanksgiving morning | Full list | 25% off, all products |

**Rules for broadcast campaigns**:
1. No more than one broadcast per week — do not send a broadcast on the same week as a promotional newsletter
2. Always include an unsubscribe reminder at the top of promotional emails ("If you'd rather not receive sale announcements, unsubscribe here")
3. Subject lines for promotional broadcasts should be honest about what they are: "25% off this weekend" rather than a curiosity-gap subject that buries the promotional nature

---

## Part 8: Success Metrics and Optimization Triggers

### Primary Metrics (Check Monthly)

| Metric | Healthy Range | Action If Below Range |
|---|---|---|
| Welcome sequence Email 1 open rate | 45–60% | Check spam folder delivery; test subject line variants |
| Welcome sequence Email 5 coupon redemption | 8–15% | Revise product recommendations (use Phase 1 conversion data) |
| Weekly newsletter open rate | 28–40% | Test subject line formulas; reduce send frequency temporarily |
| Newsletter click-through rate | 3–6% | Review product spotlight relevance; align with seasonal demand |
| Post-purchase review email conversion | 8–15% | Adjust Email 3 timing (try Day 14 vs. Day 21) |
| Win-back Email 1 re-engagement rate | 15–25% | Adjust trigger threshold (try 8 weeks vs. 6 weeks) |
| Monthly unsubscribe rate | Below 0.5% | If above 0.5%, too many promotional sends or irrelevant content |

### Quarterly Review Protocol

At the end of each quarter (August 2026, November 2026, February 2027, May 2027), review:
1. Which welcome sequence email has the highest open-to-click ratio? This is the audience's highest-interest topic — create more content in that area.
2. Which post-purchase upsell (Email 2) generates the most secondary purchases? Move that product to the primary cross-sell position.
3. Which newsletter subject line formula generates the best open rates? Increase its share of sends.
4. What is the net list growth rate (new subscribers minus unsubscribes)? If growth has slowed, increase lead magnet promotion via social channels.

---

## Implementation Timeline

**Week 1 (Before Phase 1 launch)**
- Create Kit account (free, up to 10,000 subscribers)
- Design lead magnet PDF (existing 5-variety guide from email-and-launch-plan.md is ready to use)
- Create Kit landing page form
- Set up Automation 1 (welcome sequence) with all 5 emails loaded and scheduled
- Add lead magnet link to TikTok/Instagram bio and to the "end page" of all Etsy PDFs

**Month 1 (Phase 1 live)**
- Weekly newsletter begins after welcome sequence is tested and confirmed working
- Monitor Email 1 open rate and Email 5 coupon redemption daily for first two weeks

**Month 2 (First buyers)**
- Set up Automation 2 (post-purchase) — either manually tagging buyers or via Zapier if volume warrants
- Apply behavioral tags from welcome sequence click data to begin segmenting

**Month 3+**
- Set up Automation 4 (win-back) as list grows past 300 subscribers
- Run first seasonal broadcast campaign (July: Preservation Season Launch)
- Evaluate whether zone-personalization upgrade to lead magnet is worth implementing

---

*Prepared: 2026-04-27. References: email-and-launch-plan.md (full email copy), annual-product-plan.md (seasonal campaign strategy), phase-3-operations-playbook.md (newsletter template and segment strategy), product-calendar-2026-2027.json (monthly product feature rotation).*
