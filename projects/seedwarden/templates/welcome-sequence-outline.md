---
title: "Seedwarden Welcome Sequence Outline — 30-Day Subscriber Journey"
date: 2026-04-28
status: ready-to-implement
platform: Kit (ConvertKit)
emails: 5 emails over 10 days, then weekly newsletter
tags: [email, welcome-sequence, automation, template, seedwarden]
---

# Welcome Sequence Outline: 30-Day Subscriber Journey

**What this is**: A structural outline and writing brief for the Seedwarden 5-email welcome sequence. Full email copy is in `marketing/email-and-launch-plan.md`. Use this document as the operational blueprint: who gets each email, when, why, and what the email must accomplish.

**Platform setup**: Kit (ConvertKit) sequence — each email is a node in the "Seedwarden Welcome" sequence, triggered by the lead magnet form submission.

---

## Overview: The 5-Email Structure

| # | Subject Line (Working) | Day | Trigger Condition | Primary Goal |
|---|----------------------|-----|-------------------|-------------|
| 1 | Your Seedwarden Starter Pack is here (+ a quick hello) | Day 0 (immediate) | Form submitted | Deliver lead magnet; set tone; establish sender identity |
| 2 | The difference between an heirloom tomato and a lie | Day 2 | Always send | Build authority; introduce brand philosophy |
| 3 | The mistake that wiped out a full season of seeds | Day 5 | Always send | Practical value; first behavioral tag opportunity |
| 4 | What I've been building (and why digital guides made sense) | Day 7 | Always send | Catalog introduction; second behavioral tag; soft cross-reference |
| 5 | One more thing before I stop showing up in your inbox | Day 10 | Always send | First direct offer; SEEDWARDEN15 coupon; conversion event |

After Email 5: subscriber moves automatically to the weekly Thursday newsletter (Automation 3). No gap — if Email 5 sends on a Wednesday, they receive their first newsletter the following Thursday.

---

## Email 1 — Delivery + Welcome

**Subject**: Your Seedwarden Starter Pack is here (+ a quick hello)
**Day**: Immediately after form submission
**Length**: 200–300 words
**Tone**: Warm, direct, not corporate. Write as a person, not a brand.

**Must include**:
- The lead magnet download link (Google Drive shared link to Zone Quick-Start Card or 5-variety guide PDF). Place this in the FIRST paragraph — do not make the subscriber scroll to find what they signed up for.
- A 2–3 sentence personal introduction: who is behind Seedwarden, what they care about, what the subscriber will receive from now on.
- One expectation-setting sentence: "You'll hear from me again in two days with something I think you'll find useful — no fluff, just practical information for people who grow food."
- A reply prompt: "Hit reply and tell me one thing — what are you hoping to grow (or preserve) this season?" This drives inbox deliverability by encouraging a reply and generates product intelligence at zero cost.

**Must not include**:
- A product pitch. Email 1 is a delivery email. Making a pitch before delivering the lead magnet damages trust and increases unsubscribes.
- A long narrative or personal backstory. Save that for Emails 2 and 4.
- Multiple CTAs. One action only: download the free guide.

**Kit setup note**: Set delay to "Immediately" — do not use the default 1-hour or next-day delay. Subscribers expect instant delivery when they opt in for a free resource. Delays above 60 minutes correlate with higher unsubscribe rates on Email 1.

---

## Email 2 — Authority and Brand Philosophy

**Subject**: The difference between an heirloom tomato and a lie
**Day**: Day 2 (48 hours after Email 1)
**Length**: 400–600 words
**Tone**: Slightly irreverent, opinionated, confident without being aggressive.

**Story frame**: A short narrative contrasting what the seed industry sells vs. what an actual heirloom variety delivers. This is the email where the subscriber learns what Seedwarden stands for — not just practical growing information, but a specific point of view on the industrial food system and why seed saving and growing your own food matters.

**Must include**:
- A specific anecdote or example (a named variety, a specific flavor or yield comparison, a concrete story moment that grounds the philosophy in reality)
- One forward-looking bridge: "In my next email, I'm going to tell you about a mistake that wiped out one of my grow seasons — and what I learned from it."
- A single light CTA — a link to one Seedwarden listing is acceptable here (framed as "if you want to go deeper on this right now"), but the click-through is not the goal. The goal is building anticipation for Email 3.

**Must not include**:
- A coupon or direct sales offer (too early — this email is building, not converting)
- Multiple product links or a "shop the full catalog" link

**Behavioral signal**: If the subscriber opened Email 1 and also opens Email 2, they are a highly engaged subscriber. Kit does not require you to act on this in the sequence — but after the welcome sequence completes, these double-openers are the subscribers to prioritize for any one-off broadcast.

---

## Email 3 — Practical Value + First Behavioral Tag

**Subject**: The mistake that wiped out a full season of seeds
**Day**: Day 5 (5 days after Email 1)
**Length**: 500–700 words
**Tone**: Honest, practical, slightly self-deprecating. The subscriber should feel they learned something useful from someone who made a real mistake.

**Story frame**: A seed saving failure — a specific mistake (wrong drying method, cross-pollination between varieties, improper storage) that destroyed a seed batch. Walk through what happened, why it happened, and the specific technique that prevents it. This is the highest-value educational email in the sequence.

**Must include**:
- A concrete, specific technique (not "make sure you dry your seeds properly" — but the actual method, the actual humidity level, the actual container type)
- The FIRST behavioral tag opportunity: embed a click-tracked link to the Seed Saving Field Manual listing, framed as "If you want the full framework: [link]." Subscribers who click get tagged `seed-saver` in Kit.
- A preview of what is coming in Email 4: "On Wednesday I'm going to show you everything I've been building over the past year — including why digital guides became the format."

**Must not include**:
- A hard sell on the Seed Saving Manual. The link is there for interested subscribers. It is not the CTA.
- A discount offer (that is reserved for Email 5)

**Kit tag setup**: In Kit, on the link to the Seed Saving Field Manual, click "Link Actions" → Add tag → "seed-saver." Any subscriber who clicks that link is automatically tagged. This requires no manual work after setup.

---

## Email 4 — Catalog Introduction + Cohort Tags

**Subject**: What I've been building (and why digital guides made sense)
**Day**: Day 7 (7 days after Email 1)
**Length**: 500–700 words
**Tone**: Behind-the-scenes, honest about the decision-making process behind creating guides, warm.

**Story frame**: The origin of Seedwarden — what problem was being solved, why digital guides were the format, what the catalog is now. This is the email where the subscriber sees the full catalog for the first time, but through a narrative lens rather than a product list.

**Must include**:
- A 2–3 paragraph narrative explaining why Seedwarden exists (the problem with generic growing advice, the value of content-dense specific guides)
- The SECOND behavioral tag opportunity: three product category links with distinct click-tracked labels:
  - "For container and apartment growers: [Apartment Plant Catalog or Container Blueprint link]" → tag `city-grower`
  - "For seed saving and food sovereignty: [Seed Saving Field Manual or Food Sovereignty Guide link]" → tag `seed-saver`
  - "For food preservation and storage: [Harvest Preservation or Fermented Harvest link]" → tag `preservationist`
- A preview of Email 5: "Tomorrow I'm going to send you something — a discount on anything in the Seedwarden catalog. I don't send coupons often, so it's worth looking for."

**Must not include**:
- More than three category links (decision paralysis reduces clicks)
- A specific price for any product (the discount in Email 5 makes any pre-coupon price feel like the wrong price)

**Kit tag setup**: Set up three separate click-tracked links. Each link goes to a different Etsy listing and triggers a different tag. A subscriber who clicks two links gets two tags — that is correct behavior.

---

## Email 5 — First Offer and Conversion Event

**Subject**: One more thing before I stop showing up in your inbox
**Day**: Day 10 (10 days after Email 1)
**Length**: 300–400 words
**Tone**: Low-pressure, conversational, honest about what the email is.

**Frame**: This is a "graduation" email — the subscriber has completed the welcome sequence and is transitioning to the regular Thursday newsletter. The coupon is framed as a thank-you for reading, not a hard-sell.

**Must include**:
- The SEEDWARDEN15 coupon code (15% off all products, 5-day expiry from the send date)
- The expiry date stated explicitly in plain text: "This code expires [date 5 days from now]. I'll honor it a few days past that if you reach out — I'm not trying to pressure you."
- A link to the Etsy shop (not a specific product — let the subscriber browse)
- A closing transition: "Starting next Thursday, you'll get one email per week from me — a brief growing update, a practical technique, and whichever Seedwarden guide fits the season. I try to keep it under 5 minutes to read."
- An easy unsubscribe option explicitly mentioned: "If this isn't for you, the unsubscribe link is below — no hard feelings."

**Must not include**:
- A countdown timer or artificial urgency language ("LAST CHANCE," "Don't miss out")
- Multiple product links or a full catalog listing
- Any additional pitch beyond the coupon and shop link

**Kit setup note**: Generate the SEEDWARDEN15 coupon code in Etsy Seller Dashboard under Shop Manager > Discounts before setting up this email. Set the discount to 15% off the entire order. The code can be used multiple times — Kit does not integrate with Etsy's single-use coupon system on the free tier. Communicate the deadline via the email text only.

**Expected conversion rate**: 8–15% of Email 5 recipients will redeem the coupon. At 50 subscribers in Month 1, that is 4–7 incremental purchases. At 150 subscribers by Month 3, that is 12–22 incremental purchases.

---

## Post-Sequence Transition

After Email 5 sends, Kit automatically moves the subscriber into the regular newsletter segment. The first Thursday newsletter they receive should not reference the welcome sequence — it should be a standalone edition that works for any reader.

**Behavioral tag usage from this point forward**:
- `seed-saver` tagged subscribers: Thursday newsletter features seed saving and heirloom products in the product spotlight section once per month
- `city-grower` tagged subscribers: Newsletter features apartment/container products in the spotlight section
- `preservationist` tagged subscribers: Newsletter features preservation and fermentation products in the spotlight section

If a subscriber has no behavioral tag (they opened all emails but clicked no product links), they receive the untagged newsletter version, which features the product with the highest conversion rate that month.

---

## Subject Line Alternatives (for A/B Testing)

If open rates on any email fall below threshold, test these alternatives:

| Email | Current Subject | Alternative A | Alternative B |
|-------|----------------|--------------|--------------|
| 1 | Your Seedwarden Starter Pack is here | Here's your free zone guide | Your free planting guide is ready |
| 2 | The difference between an heirloom tomato and a lie | Why most seed catalogs aren't honest | What they don't tell you about heirloom seeds |
| 3 | The mistake that wiped out a full season of seeds | The seed storage mistake I'll never repeat | How I destroyed a year's worth of seeds (and what I learned) |
| 4 | What I've been building (and why digital guides made sense) | Here's everything I've made for homesteaders | The full Seedwarden catalog — here's what to start with |
| 5 | One more thing before I stop showing up in your inbox | A discount, and then I'll let you get on with it | 15% off, for the next 5 days |

Test by sending the alternative subject to 30% of new subscribers for 30 days and comparing open rates. Kit's A/B testing on sequences is available on the free tier for subject line testing.

---

*Template prepared: 2026-04-28. Full email copy: `marketing/email-and-launch-plan.md`. Automation technical setup: `marketing/email-automation-blueprint.md` Part 3. Revenue targets: `docs/phase-1-revenue-roadmap.md`.*
