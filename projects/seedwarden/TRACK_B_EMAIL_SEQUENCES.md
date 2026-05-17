---
title: "Track B Email Sequences — Send-Ready Finalization"
prepared: 2026-05-17
status: production-ready — Kit build ready for May 27–28
gate: Gate 3 — Kit Build (Phase 3C)
source: TRACK_B_EMAIL_STAGING.md (email bodies), TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md (build procedure)
---

# Track B Email Sequences — Send-Ready Finalization

**Purpose**: Complete, copy-paste-ready email build package for the Kit automation builder.
This file extends TRACK_B_EMAIL_STAGING.md with send schedule, preview text, UTM tracking
parameters, CTA button specs, and Kit-editor-ready paste blocks for all 5 emails.

**When to use**: May 27–28 during Gate 3 Phase 3C (Kit account + email sequence build).
Open this file and TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md side by side.

**Time estimate**: 45–60 minutes to build all 5 emails with this file open.

---

## Complete Send Schedule

| Email | Trigger | Delay Setting in Kit | Send Day | Best Send Window |
|-------|---------|---------------------|----------|-----------------|
| Email 1 | Subscribe via landing page | Immediately | Day 0 | Instant delivery — no window |
| Email 2 | After Email 1 | 2 days after Email 1 | Day 2 | 9:00–11:00am subscriber's time zone |
| Email 3 | After Email 2 | 3 days after Email 2 | Day 5 | 9:00–11:00am subscriber's time zone |
| Email 4 | After Email 3 | 2 days after Email 3 | Day 7 | 9:00–11:00am subscriber's time zone |
| Email 5 | After Email 4 | 3 days after Email 4 | Day 10 | 9:00–11:00am subscriber's time zone |

**Kit delay setting**: In Kit > Automations > Sequences, each email except Email 1 has a
"Send delay" field. For Email 2: type `2` in the "days" field. For Email 3: `3`. For Email 4: `2`.
For Email 5: `3`. Kit counts from the date of the previous email, not from the subscribe date.

**Time zone handling**: Kit sends at the configured delay relative to when each subscriber
joined. You do not need to set a time-of-day unless Kit's "Smart Send" feature is enabled.
If Smart Send is available on your plan, enable it — Kit will automatically deliver within
the subscriber's best open window.

---

## Email 1 — Day 0 (Immediate)

### Metadata

| Field | Value |
|-------|-------|
| Subject line | Your Seedwarden Starter Pack is here (+ a quick hello) |
| Preview text | A short guide to five heirloom varieties — no fluff, no upsell |
| Send delay | Immediately on subscribe |
| CTA button text | Download Your Starter Pack |
| CTA button URL | [Google Drive direct download link for Starter Pack PDF] |
| UTM parameters | `?utm_source=kit&utm_medium=email&utm_campaign=welcome_seq&utm_content=email1_cta` |

**Full CTA button URL format (paste into Kit button link field)**:
```
[STARTER_PACK_DRIVE_URL]?utm_source=kit&utm_medium=email&utm_campaign=welcome_seq&utm_content=email1_cta
```
Replace `[STARTER_PACK_DRIVE_URL]` with the Google Drive direct download URL.
Format: `https://drive.google.com/uc?export=download&id=[FILE_ID]`

### Kit Editor Paste Block

```
Subject: Your Seedwarden Starter Pack is here (+ a quick hello)

Hi [First Name],

Welcome — really glad you found your way here.

Your Seedwarden Starter Pack is attached below. It's a short, practical guide to five heirloom varieties that do well in small spaces, with a seed-saving note for each one. No fluff, no upsell inside — just information I actually want you to have.

[BUTTON: Download Your Starter Pack]

A little about me and why I started Seedwarden:

I got into heirloom seeds the way a lot of people do — a gift from a neighbor, a tomato that tasted like something, a slow realization that what I was buying at the hardware store was a pale substitute for what was actually possible. I started saving seeds, then researching varieties, then obsessing over the history behind them. Some of these plants have been passed between hands for hundreds of years. That felt worth protecting.

Seedwarden started as a way to share that. Right now it lives on Etsy as a collection of digital growing guides — practical PDFs you can print or keep on your phone. Each one covers a specific variety or growing skill in the kind of depth you don't find on seed packets.

Over the next couple of weeks I'll send you a few more emails — growing tips, a story or two, and eventually a look at what I've been working on in the shop. Nothing daily, nothing spammy. If at any point it's not useful, the unsubscribe link is always at the bottom and I won't take it personally.

For now — download the guide, pick a variety that catches your eye, and if you have questions, just reply to this email. I read everything.

Talk soon,
[Your first name]
Seedwarden
```

**Kit editor notes**:
- Replace `[First Name]` with Kit's personalization tag: `{{ subscriber.first_name | default: "there" }}`
- Replace `[Your first name]` with your actual first name (static text)
- Add a button block in Kit's editor for `[BUTTON: Download Your Starter Pack]` — link to the
  Drive URL with UTM parameters above
- Kit plain-text alternative: Kit auto-generates a plain-text version; review it after saving
  to confirm the button link appears as a full URL in the plain-text fallback

**Zone variant note**: If you are building zone-specific Email 1 variants (one per zone card,
8 total), replace the "Your Seedwarden Starter Pack" content with the zone-specific card copy.
Zone routing instructions: `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` Section 5. The above is
the non-zone-specific fallback version; use it if you build a single universal Email 1 first.

---

## Email 2 — Day 2

### Metadata

| Field | Value |
|-------|-------|
| Subject line | The difference between an heirloom tomato and a lie |
| Preview text | Brandywine has been around since the 1880s. Here's why that matters. |
| Send delay | 2 days after Email 1 |
| CTA button text | None — no CTA in this email |
| UTM parameters | N/A — no links in this email |

**Note**: Email 2 is pure value delivery. No product links, no buttons. Do not add a CTA.
The goal is to build relationship authority before the first product mention (Email 3).

### Kit Editor Paste Block

```
Subject: The difference between an heirloom tomato and a lie

Hi [First Name],

I want to tell you about a tomato called Brandywine.

It's a big, ugly, slightly lopsided pink tomato that takes 90 days to produce. It bruises easily, it doesn't ship well, and grocery stores won't touch it. By every commercial metric it is a failure.

It also tastes like someone distilled the concept of summer into a piece of fruit.

Brandywine has been grown in American gardens since at least the 1880s. Nobody owns it. The seed has passed from gardener to gardener for over a century, and every person who has grown it and saved its seed has participated in something that's a little hard to name — a kind of continuity, a thread between people who never met.

This is why I care about heirloom seeds, and it's the lens through which Seedwarden was built.

The guides I create aren't just about growing instructions. They're about understanding what you're growing — the variety's history, what makes it distinctive, why it was worth saving in the first place. That context doesn't make the tomatoes taste better, but it changes the experience of growing them. You're participating in something larger than your garden bed.

A few things worth knowing about heirlooms vs. hybrids if you're newer to this:

Heirloom: Open-pollinated, stable genetics, seed-saving works — the plant you grow from saved seed will be the same as the parent. Usually 50+ years old by definition.

Hybrid (F1): Two varieties deliberately crossed for specific traits (uniformity, shelf life, disease resistance). Not bad plants — just not seed-saveable in a meaningful way. The next generation reverts to unpredictable traits.

GMO: A separate category entirely, involving lab-based gene modification. Not relevant to home gardening — GMO seed is not sold to home growers.

Most seed packets don't explain any of this. Most gardening content treats it as too nerdy to bother with. I think that's a mistake.

Next email I'll share something more practical — a mistake I made in my first year of seed saving that cost me an entire season of work, and what I learned from it.

Talk soon,
[Your first name]
```

**Kit editor notes**:
- Replace `[First Name]` with Kit's personalization tag: `{{ subscriber.first_name | default: "there" }}`
- Apply **bold** formatting to the three term definitions: "Heirloom:", "Hybrid (F1):", "GMO:"
  Use Kit's rich text editor bold button on those terms only
- No button block needed
- No links to add

---

## Email 3 — Day 5

### Metadata

| Field | Value |
|-------|-------|
| Subject line | The mistake that wiped out a full season of seeds |
| Preview text | I saved seeds wrong for an entire season. Here's what I learned the hard way. |
| Send delay | 3 days after Email 2 (5 days after subscribe) |
| CTA button text | Visit the Seedwarden Etsy Shop |
| CTA button URL | [Etsy shop URL] |
| UTM parameters | `?utm_source=kit&utm_medium=email&utm_campaign=welcome_seq&utm_content=email3_shop_cta` |

**Full CTA button URL format**:
```
[ETSY_SHOP_URL]?utm_source=kit&utm_medium=email&utm_campaign=welcome_seq&utm_content=email3_shop_cta
```
Replace `[ETSY_SHOP_URL]` with the full Etsy shop URL (format: `https://www.etsy.com/shop/seedwarden`
or the verified URL from your Etsy account).

Note: Etsy may not pass UTM parameters through to GA4 on all traffic. Include them anyway —
they are tracked in Kit's click reports even if GA4 does not receive them.

### Kit Editor Paste Block

```
Subject: The mistake that wiped out a full season of seeds

Hi [First Name],

My first serious attempt at seed saving almost ended before it started.

I grew a beautiful crop of paste tomatoes — Amish Paste, which is a variety I still love — let them ripen fully on the vine, and saved the seeds using what I thought was a reasonable method: I squeezed them onto a paper towel and let them dry in the kitchen.

Seemed logical. Tomato seeds are small. Paper towel absorbs moisture. Done.

What I didn't know: tomato seeds are surrounded by a gel coating that contains germination inhibitors. That coating has to be removed through fermentation — you float the seeds in a small jar of water for 2–3 days until the viable seeds sink and the gel and mold float to the top. Then you rinse them, dry them properly on a ceramic plate (not paper — they stick), and store them in a cool, dry, dark place.

My paper towel seeds were contaminated, stuck to the towel, and had an abysmal germination rate the following spring. I got maybe 15% of what I should have.

That mistake is in the Amish Paste guide I sell on Etsy — not as a cautionary tale, but as part of the actual seed-saving instructions, because it's the kind of thing nobody puts on a seed packet and most articles skip over.

The guides I've built are heavy on this kind of detail. Not because I want to overwhelm anyone, but because the small procedural things — fermentation for tomato seeds, when exactly to harvest bean seeds (on the plant, not after), how to test old seed viability before you commit a whole bed — are what separate a frustrating first season from one that actually works.

If you want a look at what's in the shop, here's the link:

[BUTTON: Visit the Seedwarden Etsy Shop]

No pressure to buy anything. But if you're planning to grow this season and want more of the kind of information I've been sharing, that's where it lives.

More soon,
[Your first name]
```

**Kit editor notes**:
- Replace `[First Name]` with Kit's personalization tag
- Add button block linked to Etsy shop URL with UTM parameters above
- This is the first email with a trackable link — confirm Kit's click tracking is enabled
  (Kit > Account > Settings > Analytics — should be on by default)

---

## Email 4 — Day 7

### Metadata

| Field | Value |
|-------|-------|
| Subject line | What I've been building (and why digital guides made sense) |
| Preview text | I looked into physical seed packets. The economics don't work. Here's why digital is different. |
| Send delay | 2 days after Email 3 (7 days after subscribe) |
| CTA button text | Browse the Shop |
| CTA button URL | [Etsy shop URL] |
| UTM parameters | `?utm_source=kit&utm_medium=email&utm_campaign=welcome_seq&utm_content=email4_shop_cta` |

### Kit Editor Paste Block

```
Subject: What I've been building (and why digital guides made sense)

Hi [First Name],

A quick look behind the curtain today.

When I started Seedwarden, I thought about physical seed packets. It's the obvious format — it's what you picture when you think "seed brand." I spent a while looking into it: sourcing, labeling regulations, shipping logistics, storage requirements for maintaining viability.

It's doable. It's also expensive, complicated, and means competing on price and SEO with operations that have been selling seeds online for twenty years.

Digital guides let me do something different. Instead of selling you a packet of seeds you could find elsewhere, I can sell you the knowledge that makes those seeds actually work — the variety profiles, the growing notes, the seed-saving instructions, the troubleshooting. The information is the product.

Each guide is a focused PDF, typically 8–15 pages, covering one variety or one specific growing skill. You download it, print it if you want a physical copy, and have it forever.

Here's a sample of what's currently in the shop:

[LIST YOUR 4 TOP PRODUCTS HERE — example format below]
• Seed Saving Field Manual — complete fermentation, drying, and storage guide, $9
• Survival Garden Regional Plans — zone-by-zone layout and timing, $12
• Harvest Preservation Field Manual — canning, fermenting, dehydrating, $10
• Anti-Catalog: 30 Heirlooms Worth Growing — variety profiles with histories, $8

Prices are $7–$15. They are priced that way intentionally — low enough that buying one is not a significant decision, high enough that I took the time to make them actually good.

[BUTTON: Browse the Shop]

If any of those topics match what you're planning to grow this year, take a look. And if you're not sure which one fits your situation best, reply to this email and tell me what you're working with — space, climate, experience level — and I'll point you to the right one.

Talk soon,
[Your first name]
```

**Kit editor notes**:
- Replace `[First Name]` with Kit's personalization tag
- Replace the 4 product list items with actual titles, one-sentence descriptions, and prices
  from your live Etsy shop. Pull current listings from Etsy Shop Manager > Listings.
- Use Kit's bulleted list formatting for the product list (click the bullet icon in the rich
  text toolbar — do not use the dash prefix shown above; that is placeholder formatting)
- Add button block linked to Etsy shop URL with UTM parameters

---

## Email 5 — Day 10

### Metadata

| Field | Value |
|-------|-------|
| Subject line | One more thing before I stop showing up in your inbox |
| Preview text | 15% off any purchase for the next 5 days. No timer, no gimmick. |
| Send delay | 3 days after Email 4 (10 days after subscribe) |
| CTA button text | Shop Now — Use Code SEEDWARDEN15 |
| CTA button URL | [Etsy shop URL] |
| UTM parameters | `?utm_source=kit&utm_medium=email&utm_campaign=welcome_seq&utm_content=email5_offer_cta` |
| Coupon code | SEEDWARDEN15 (must be active in Etsy before sequence goes live) |

**Pre-activation check**: Before activating the Kit sequence, verify SEEDWARDEN15 is live
in Etsy Shop Manager > Marketing > Sales and Coupons. If the code is not active, Email 5
creates a negative experience (promise + broken checkout). This is a hard prerequisite.

### Kit Editor Paste Block

```
Subject: One more thing before I stop showing up in your inbox

Hi [First Name],

Last email in this sequence — I promised not to be in your inbox daily, and I meant it.

After this one, you'll hear from me when I have something worth saying: a new guide, a growing tip that's actually timely, the occasional honest look at what's working and what isn't in my own garden.

But before I go quiet, I want to make a real offer.

If you've been reading these emails and thinking about picking up a guide, this is a good time to do it: I'm giving new subscribers 15% off any purchase for the next 5 days. Use coupon code SEEDWARDEN15 at checkout on Etsy.

No countdown timer gimmick. No artificial scarcity. The code just expires in 5 days because I'm not going to run a permanent discount — that's not sustainable and it's not honest.

If you want a recommendation, here's where I'd start depending on your situation:

[LIST YOUR 3 RECOMMENDATION GUIDES HERE — example format below]
• New to heirloom growing, have a small space: Anti-Catalog: 30 Heirlooms Worth Growing — $6.80 after discount
• Ready to start saving seeds: Seed Saving Field Manual — $7.65 after discount
• Interested in growing in containers: Container Growing Blueprint Pack — $8.50 after discount

[BUTTON: Shop Now — Use Code SEEDWARDEN15]

And whether you buy something or not — thank you for reading. Building this from scratch means every person who signs up and engages actually matters. It's not a figure of speech.

If you have questions about growing, seed saving, or anything else, my inbox is always open. Reply anytime.

Good growing,
[Your first name]
Seedwarden
```

**Kit editor notes**:
- Replace `[First Name]` with Kit's personalization tag
- Replace the 3 recommendation items with actual guide titles and post-discount prices
  (calculate: price x 0.85 = post-discount price, round to nearest $0.05)
- The "5 days" language is dynamic and correct as written — Kit sends this email 10 days
  after signup, and the 5-day window is relative to that receive date. No calendar date needed.
- Add button block linked to Etsy shop URL with UTM parameters
- Verify SEEDWARDEN15 is live in Etsy before activating this sequence

---

## UTM Parameter Reference

All links in this sequence use the same UTM structure for consistency in GA4 and Kit reports:

| Parameter | Value | Notes |
|-----------|-------|-------|
| utm_source | kit | Identifies Kit as the traffic source |
| utm_medium | email | Identifies email as the channel |
| utm_campaign | welcome_seq | Identifies this welcome sequence |
| utm_content | email1_cta / email3_shop_cta / email4_shop_cta / email5_offer_cta | Distinguishes which email and CTA drove the click |

**GA4 tracking**: These parameters feed directly into the `acquisition_source` and
`email_campaign_id` custom dimensions defined in `TRACK_B_ANALYTICS_SETUP_DISCORD_AND_GA4.md`.

---

## Sequence Activation Checklist

Complete these steps in order before activating the sequence on May 28–29:

- [ ] Email 1: Subject, preview text, body, and download button loaded in Kit
- [ ] Email 1: Starter Pack Drive URL confirmed working in incognito (PDF downloads, no login required)
- [ ] Email 2: Subject, preview text, body loaded — no links — bold formatting on 3 terms
- [ ] Email 3: Subject, preview text, body, Etsy shop button with UTM loaded
- [ ] Email 4: Subject, preview text, body loaded — product list populated with real titles/prices
- [ ] Email 4: Etsy shop button with UTM loaded
- [ ] Email 5: Subject, preview text, body loaded — 3 recommendations populated with real prices
- [ ] Email 5: Etsy shop button with UTM loaded
- [ ] SEEDWARDEN15 coupon active in Etsy Shop Manager (verify before enabling sequence)
- [ ] All delays set: E2=2d, E3=3d, E4=2d, E5=3d
- [ ] Send test to personal email: confirm Email 1 arrives, PDF downloads, formatting correct
- [ ] Send test for zone-specific routing (if using zone variants): confirm correct zone card delivered
- [ ] Sequence status changed from Draft to Active in Kit > Automations
- [ ] Landing page is live and form submission triggers the sequence (test end-to-end)

**After activation**: Run the 3-test protocol from `TRACK_B_USER_GATES.md` Gate 3 section.
All 3 tests must pass before May 30.

---

## Preview Text Reference

Preview text appears in the email client inbox view, next to the subject line.
Keep under 90 characters for full display across clients.

| Email | Preview Text | Char Count |
|-------|-------------|------------|
| Email 1 | A short guide to five heirloom varieties — no fluff, no upsell | 62 |
| Email 2 | Brandywine has been around since the 1880s. Here's why that matters. | 69 |
| Email 3 | I saved seeds wrong for an entire season. Here's what I learned the hard way. | 79 |
| Email 4 | I looked into physical seed packets. The economics don't work. Here's why digital is different. | 95 (trim if needed) |
| Email 5 | 15% off any purchase for the next 5 days. No timer, no gimmick. | 63 |

To add preview text in Kit: In the email editor, click the subject line area — a secondary
field labeled "Preview text" appears directly below the subject line input. Paste the preview
text there. Do not add preview text to the body of the email.

---

*Source: TRACK_B_EMAIL_STAGING.md (email bodies). Finalized with send schedule, UTM parameters,
preview text, and Kit paste blocks on 2026-05-17. Gate 3 execution: May 27–28.*
