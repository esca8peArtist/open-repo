---
title: "Phase 2 Email Campaign Copy Drafts — Campaigns 1, 2, 3"
date: 2026-05-07
status: paste-ready
scope: 7 email templates (Campaign 1: 2 emails, Campaign 2: 3 emails, Campaign 3: 2 emails)
merge-tags: Kit format — {{ subscriber.first_name }}, {{ subscriber.fields.zone_number }}, {{ subscriber.fields.cohort_tag }}
template-map: Campaign 1 → Template W; Campaign 2 → Template C; Campaign 3 → Template O
references:
  - phase-2-buyer-retention-lifecycle-strategy.md (Section 2 — full campaign specs)
  - phase-2-kit-email-setup.md (Kit automation field values)
  - PHASE_2_BUNDLE_STRATEGY.md (bundle names and pricing)
  - phase-2-analytics-strategy.md (tag architecture)
a-b-test-notes: Subject line A/B variants are marked below. Kit A/B: 10% sample per variant, winner selected at 48-hour open rate.
---

# Phase 2 Email Campaign Copy Drafts

**How to use**: Paste each email body directly into the Kit sequence editor. Replace
`[PRODUCT-NAME]`, `[ETSY-LISTING-URL]`, and `[BUNDLE-NAME]` with the specific values for each
cohort or zone variant you are building. All `{{ }}` tags are Kit merge fields — paste them
exactly as written. Subject line A/B variants are marked A and B; enable Kit's built-in A/B
split on Email 1A only. All other emails use the A variant as default.

---

## CAMPAIGN 1 — WELCOME (Days 0–3)

Sequence name in Kit: `Welcome — Phase 2 Buyers`
Trigger: Tag applied — `purchased`
Template: W (two-column — body left, product image + CTA right)

---

### Email 1A — Order Confirmation + Immediate Value
**Day 0 — send immediately on `purchased` tag applied (within 2 hours)**

**Subject Line A (default):**
Your [PRODUCT-NAME] is on its way — here's what to do first

**Subject Line B (A/B test variant):**
{{ subscriber.first_name }}, welcome to Seedwarden — one thing to try this week

---

Hi {{ subscriber.first_name }},

Your [PRODUCT-NAME] is confirmed. Thank you — it means a lot that you chose Seedwarden.

[COHORT OPENING — Kit conditional content block by tag. Paste the matching paragraph:]

*Cohort_Forager:*
Fellow foragers — before you dig in, one thing worth knowing for this week: [SEASONAL-PLANT-TIP — e.g., "Black raspberries are just coming ripe in Zones 5–7 right now. Look for the distinctive arching canes along forest edges and trail margins. They're often overlooked because they ripen two weeks before the more familiar red raspberries most people watch for."] Your guide goes deep on identification and harvest timing for plants exactly like this.

*Cohort_Prepper:*
If you're building a food-resilient household, you already know the calendar matters more than the wish list. The guides in your kit are designed around what's actually available and storable, season by season. One note for this month: [SEASONAL-STORAGE-TIP — e.g., "If you're in Zone 6 or 7, late May through June is the prime window for garlic scapes and early brassicas — both dry and freeze well."]

*Cohort_Homesteader:*
Whether you're in your first season or your tenth, the [PRODUCT-NAME] is built to be the reference you reach for when you're not sure — not the one that assumes you already know everything. [SEASONAL-GROWING-TIP — e.g., "For Zone 5 in late May: your cool-weather transplants should be in the ground by now; if they're not, there's still a short window before daytime temps make it hard on them."]

*Cohort_Herbalist:*
For those working with plant medicine — a note on timing: [SEASONAL-HERB-TIP — e.g., "Elder flowers are at peak harvest in Zones 6–8 right now. The window is short — about 10 days from when the clusters open before they begin to drop. Worth knowing whether or not you have elderberry on your property."]

*Cohort_GiftBuyer (no cohort opening — use this paragraph instead):*
The [PRODUCT-NAME] is designed to be genuinely useful, whether you're the one who'll be using it or you picked it up for someone who will. There's a lot of plant information out there — we focused on what actually matters in the field.

---

If you haven't grabbed your Zone {{ subscriber.fields.zone_number }} Quick-Start Card yet, it's free and it pairs directly with your purchase. It covers your specific frost dates, seasonal windows, and the highest-value plants in your region.

[BUTTON: Get Your Zone {{ subscriber.fields.zone_number }} Card → link to Kit landing page with zone pre-filled]

*Note for Kit setup: if {{ subscriber.fields.zone_number }} is blank, omit this entire paragraph and button.*

---

More from me in a couple days — I'll share some zone-specific notes for what's happening in your area right now.

— Anya
Seedwarden

*P.S. As a thank-you for your first order, here's 10% off your next guide: SEEDWARDEN10. Valid 30 days.*

---

**Footer** (standard): Unsubscribe | Seedwarden | [physical address for CAN-SPAM] | Pinterest | Instagram

---

**Metrics targets (Email 1A):**
- Open rate: 40–45%
- Click rate: 15–20% (zone card CTA is primary click)

---

### Email 1B — Zone-Specific Field Briefing
**Day 2 — 48 hours after Email 1A sends**

**Subject Line A (default):**
Your Zone {{ subscriber.fields.zone_number }} is entering [SEASONAL-STATE] — what to watch for

**Subject Line B (A/B test variant, lower priority — do not split-test this email unless Email 1A test is complete):**
3 things worth knowing for Zone {{ subscriber.fields.zone_number }} this [MONTH]

---

Hi {{ subscriber.first_name }},

A quick zone update — this is what's happening in Zone {{ subscriber.fields.zone_number }} right now.

[ZONE CONTENT BLOCK — write one paragraph per zone before entering into Kit. Example for Zone 7, May:]

*Zone 7 example:*
The spring ephemeral foraging window is closing fast. Ramps have senesced in most of Zone 7 — if you haven't harvested yet, look for the broad leaves still standing but beginning to yellow. Pawpaw flowers are at or just past peak, which means fruit set is either happening or just finished; watch those trees through August if you know where they are. Coming up in June: black raspberries, mulberries (in the warmer pockets of Zone 7), and the beginning of the elderflower season.

[ZONE CONTENT BLOCK — paste your zone-specific paragraph here. Every zone variant needs its own paragraph written for the current month before the sequence goes live.]

Whether you're just starting to identify plants in your area or you've been at it for years, what matters most in this window isn't knowing every species — it's knowing the 3–5 plants that are at peak right now in your specific region. Everything else can wait.

If you want a deeper reference for [SEASONAL-PLANT — e.g., "elderflower or black raspberry identification and harvest timing"], [PRODUCT-NAME] covers both in detail, including what to look for to distinguish them from look-alikes.

[UTM link: utm_campaign=welcome-email-2]

---

More next week — I'll send something practical from the forager and grower calendar.

— Anya

*Reply to this email if you have a question about [ZONE-SPECIFIC-TOPIC — e.g., "ramp identification or the elderflower harvest window in your area"]. I read every reply.*

---

**Metrics targets (Email 1B):**
- Open rate: 35–40%
- Click rate: 10–15%
- Reply rate: 1–3% (any reply: add `engaged-buyer` tag in Kit manually)

---

## CAMPAIGN 2 — CONTENT DEEPENING (Days 7–21)

Sequence name in Kit: `Content Deepening — Phase 2`
Trigger: Campaign 1 Email 1B sent (Day 2)
Skip rule: If Campaign 1 open count = 0 (both emails unread at Day 3), skip to Email 2.3 only at Day 14
Template: C (single column, content-first, no hero image)

---

### Email 2.1 — Ecosystem Guide / Companion Content
**Day 7 (from Campaign 1 Email 1A send date)**

**Subject Line:**
The plants that grow near [PURCHASED-PRODUCT-FOCUS — e.g., "wild garlic" or "elderberry"]

---

Hi {{ subscriber.first_name }},

[COHORT/PRODUCT CONTENT BLOCK — 400–500 words of genuine botanical content. Write one version per cohort or product type before entering. Examples below.]

*Cohort_Forager — Wild Edibles buyer example:*

Wild garlic (Allium vineale) is one of the most reliable early-spring edibles across Zones 5–9, but foragers who find it are often missing the companion plants that grow in the same disturbed habitat. Here's what the full picture looks like:

Field garlic grows in disturbed meadows, roadsides, lawn edges, and the margins of moist woodland. Where you find it, you're almost certain to find chickweed (Stellaria media) in the same patch — an equally underutilized edible that goes unrecognized because it doesn't smell like anything. Chickweed is at its best right now (late May through early June in Zones 5–7) before summer heat causes it to bolt. Look for the thin white flowers with deeply notched petals and the single line of fine hairs along the stem.

The third plant in this habitat trio is ground ivy (Glechoma hederacea) — technically edible but very strongly flavored, historically used as a bittering agent before hops. Not everyone likes it, but identifying it is useful: it's the low-growing, kidney-shaped-leaf creeper with purple flowers that often carpets the same disturbed ground as garlic and chickweed.

This isn't coincidence. These three plants share a preference for disturbed, moderately fertile soil. When you're learning to read a landscape, the presence of any one of them suggests the others are nearby.

[END EXAMPLE — replace with the appropriate ecosystem guide content for the product the buyer purchased]

*Cohort_Homesteader — Zone Calendar buyer example:*

If you're working with the Zone Calendar and planning your June plantings, understanding companion relationships can double the value of a small plot. [Continue with 400+ words on companion planting logic for their zone...]

*Cohort_Herbalist — Medicinal guide buyer example:*

The medicinal herbs in your guide don't exist in isolation — they're part of habitat communities that often include additional useful plants. [Continue with 400+ words on medicinal preparation context and habitat companions...]

---

If you want the full reference for [TOPIC — e.g., "wild alliums and their look-alikes across your zone"], [PRODUCT-NAME] covers the identification, harvest, and preparation in detail.

[UTM link: utm_campaign=content-deepening-1]

---

— Anya

---

**Metrics targets (Email 2.1):**
- Open rate: 35–40%
- Unsubscribe rate: below 2%. If above 2%: pause sequence, simplify content to 200–300 words focused on one practical tip, re-test

---

### Email 2.2 — Seasonal Planning Content
**Day 14 (from Campaign 1 Email 1A send date)**

**Subject Line A (default):**
What [CURRENT-MONTH] means for Zone {{ subscriber.fields.zone_number }} growers

**Subject Line B:**
The next 30 days in Zone {{ subscriber.fields.zone_number }}: what to prioritize

---

Hi {{ subscriber.first_name }},

Three things worth prioritizing in Zone {{ subscriber.fields.zone_number }} right now:

[ZONE + MONTH CONTENT BLOCK — write one block per zone per month. Update monthly or write 3–4 months in advance. Example for Zone 5, May/June:]

**1. Plant your warm-season transplants (last chance)**
In Zone 5, the window for putting tomatoes, peppers, and basil in the ground typically closes by late May. Nighttime temps below 50°F slow growth significantly. If they're not in the ground by May 28, wait until June 5 and watch the forecast — a late cold snap is always possible.

**2. Harvest perennials before they bolt**
Ramps, chives, and lovage are at or approaching their peak. Harvest the leaves now; the bulbs and roots can wait until fall. Bolting begins to make leaves bitter — harvest while the plants still look lush.

**3. Start your seed-saving log**
If you're planning to save seeds this fall, now is the time to mark which plants you want to let go to seed. A piece of colored yarn on the stem works. Don't wait until August — by then you'll have forgotten which tomato or pepper was the best one.

[END EXAMPLE — replace with zone-specific content for the current month]

For a deeper guide to Zone {{ subscriber.fields.zone_number }} timing and what to grow, see this month's zone guides in the Seedwarden catalog:

[UTM link to Etsy store section filtered by zone: utm_campaign=content-deepening-2]

---

— Anya

---

**Metrics targets (Email 2.2):**
- Open rate: 35–40%
- Feature click rate (Etsy store link): 5–10%. A click here is the primary signal the buyer is considering a second purchase — apply `browse-signal` tag if Kit supports click-triggered tags on this link

---

### Email 2.3 — Practical Technique Deep-Dive
**Day 21 (from Campaign 1 Email 1A send date)**
*(This is the only Email 2 sent to subscribers on the digest track — no cohort branching on this email)*

**Subject Line:**
One technique worth knowing before [SEASONAL-EVENT — e.g., "summer foraging starts" or "the preservation window opens"]

---

Hi {{ subscriber.first_name }},

One practical thing worth knowing for this time of year — this works across almost every zone and growing situation.

[TECHNIQUE CONTENT — 300–400 words, universally applicable. Choose one topic per send. Examples:]

*Example 1 — Drying and storing wild herbs:*

The most common mistake in drying herbs is doing it too slowly. Slow drying (anything below 95°F in a humid environment) allows the essential oils to off-gas before the cell structure dries and seals. The result: dried herb with color and volume but very little flavor or medicinal activity.

The faster method that works without a dehydrator: tie the stems in loose bundles (no more than 8–10 stems per bundle), hang in a warm, well-ventilated space away from direct sunlight. A car parked in shade with the windows cracked 2 inches is actually an excellent drying environment in June or July — temperatures of 100–120°F dry most herbs in 24–36 hours without bleaching them.

Test for doneness: crush a leaf between your fingers. It should crumble completely, not bend. If it bends, there is still moisture inside that will cause mold in storage. Store in glass — not plastic — in a dark cabinet. Whole leaves store longer than crumbled ones; crumble when you're ready to use.

Herbs worth drying right now in most zones: elder flowers (window closes in 2 weeks), calendula (long season, harvest continuously), and lemon balm (cut the whole top third of the plant, which encourages it to regrow twice more this season).

[END EXAMPLE — choose a different practical technique each month. Options: how to identify false vs. true morels, how to read a seed packet date, how to make a plant press for identification records, how to blanch and freeze wild greens]

---

I'll have something for you next week that goes a bit deeper into the catalog. There's a guide that pairs directly with what you've been reading — and I'd like to offer it to you at a discount. More soon.

— Anya

---

**Metrics targets (Email 2.3):**
- Open rate: 35–40%
- Unsubscribe rate: below 2%
- Note: this email is the transition into Campaign 3. The final paragraph is intentional — it primes the buyer for the Day 15 upsell without revealing it yet

---

## CAMPAIGN 3 — CROSS-ZONE UPSELL (Days 15–45)

Sequence name in Kit: `Cross-Zone Upsell — Phase 2`
Trigger: 15 days after Campaign 1 Email 1A send date
Template: O (offer layout — product hero image, price display, large CTA button)

Email 3.2 condition: Send only if Email 3.1 was opened AND not clicked. Skip if Email 3.1 was clicked (buyer already in consideration). Skip if second `purchased` tag event detected.

---

### Email 3.1 — Zone Bundle Recommendation
**Day 15 (from Campaign 1 Email 1A send date)**

**Subject Line A (default):**
Based on what you bought — here's what pairs with it

**Subject Line B:**
The natural next step for Zone {{ subscriber.fields.zone_number }} buyers

---

Hi {{ subscriber.first_name }},

You picked up [PRODUCT-NAME] a couple of weeks ago. Based on what that guide covers, there's a natural next step — and right now you can get it at a discount.

[PRODUCT RECOMMENDATION BLOCK — use the pairing logic from the lifecycle strategy. One example per pairing:]

*First purchase: Wild Edibles Quick Reference → recommendation: Medicinal Herbs guide*
The wild plants in the Wild Edibles guide and the medicinal herbs guide overlap more than most people realize — plants like elderberry, yarrow, and plantain appear in both. The Medicinal Herbs guide covers preparation methods (tinctures, teas, poultices) for plants you're already learning to identify. It's the most natural second guide for someone who started with wild edibles.

*First purchase: Zone Calendar → recommendation: Seed Saving Field Manual*
The Zone Calendar tells you when to plant. The Seed Saving Field Manual tells you which plants are worth saving seed from, how to do it, and how to store seeds reliably across winters. They're designed to work in sequence — planning first, then building your own seed supply.

*First purchase: any single zone guide → recommendation: adjacent zone bundle*
If you're in Zone {{ subscriber.fields.zone_number }}, the guides for the zones directly adjacent (Zone [ZONE-1] and Zone [ZONE+1]) cover a lot of the same species in overlapping terrain. The three-zone bundle covers your full regional range at a better price than buying each separately.

*Default (no specific pairing) — any single guide → Zone bundle at 15% off:*
The most useful second purchase for anyone who started with a single guide is the zone bundle — it covers your full growing and foraging range at 15% off the individual prices.

[END PAIRING EXAMPLES — choose the correct one for each cohort/product variant]

Here's the bundle: **[BUNDLE-NAME]** — [WHAT'S INCLUDED, 3–5 items]

Individual price: $[XX]. Bundle price: $[XX] (15% off).

[BUTTON: See [BUNDLE-NAME] on Etsy → utm_campaign=upsell-bundle]

---

— Anya

*P.S. Coupon code SEEDWARDEN15 applies at checkout for 15% off any order over $[minimum if applicable]. Valid through [DATE — 30 days from send].*

---

**Metrics targets (Email 3.1):**
- Click-to-purchase rate: 1–2%
- Bundle attach rate (second orders that are bundles): target 25%+

---

### Email 3.2 — Premium Guide Offering
**Day 30 — sends only if Email 3.1 was opened but not clicked**

**Subject Line:**
For buyers who want to go deeper — [PREMIUM-GUIDE-NAME]

---

Hi {{ subscriber.first_name }},

Last week I mentioned a guide that pairs with what you've been reading. I want to give you a bit more context on it before the offer closes.

[PREMIUM GUIDE CONTENT — 200–250 words. Focus on depth, credentials, and specific use cases rather than price. Example for an endangered species premium guide at $22:]

The [PREMIUM-GUIDE-NAME] is different from most of what you'll find in the Seedwarden catalog. It focuses specifically on [SUBJECT — e.g., "native plant species that are disappearing from the eastern deciduous forest"] — a narrower scope, but researched more deeply.

Every species entry in this guide is cross-referenced with USDA PLANTS database records and iNaturalist observation data. The identification notes go beyond leaf shape and flower color — they cover seasonal variation, habitat indicators, and the specific conditions that tell you the population you're looking at is healthy versus stressed.

This guide is for buyers who want to understand a plant, not just identify it. If you've been using the [FIRST-PRODUCT-NAME] to learn what's in your area, this is the next level of that same work.

Price: $22. Includes [SPECIFIC CONTENT FEATURES — e.g., "6 full species accounts, 24 field photographs, range maps cross-referenced to iNaturalist observations"].

[BUTTON: See [PREMIUM-GUIDE-NAME] → utm_campaign=upsell-premium]

---

This offer is available through [DATE — 7 days from send]. After that it returns to standard pricing.

— Anya

---

**Metrics targets (Email 3.2):**
- Click-to-purchase rate: 1–2%
- Note: this email is only sent to a subset of Campaign 3 recipients (opened 3.1, did not click). The pool is small but warm — open buyers who considered the bundle are the ideal premium pitch audience

---

## A/B TEST SCHEDULE

| Week | Email | Test Variable | Variant A | Variant B | Decision Rule |
|---|---|---|---|---|---|
| Week 1 (May 23–29) | Email 1A | Subject line | "Your [Product] is on its way..." | "{{ subscriber.first_name }}, welcome to Seedwarden..." | Winning variant by open rate at 48 hours |
| Week 2 (Jun 1–7) | Email 2.1 | Send time | 9am local | 6pm local | Winning variant by open rate at 48 hours |
| Week 3 (Jun 8–14) | Email 3.1 | CTA button text | "See the bundle" | "Get 15% off [Bundle]" | Winning variant by click rate at 7 days |
| Week 4 (Jun 15–21) | Email 3.2 | Subject line framing | Premium guide focus | Depth/credentials focus | Winning variant by open rate at 48 hours |

Do not run two simultaneous tests on the same list. Complete one before starting the next.

---

## KIT MERGE TAG REFERENCE

| Tag | What It Pulls | Fallback if Blank |
|---|---|---|
| `{{ subscriber.first_name }}` | Subscriber first name from signup form | "Friend" |
| `{{ subscriber.fields.zone_number }}` | Zone selected on Kit landing page | omit zone card CTA entirely |
| `{{ subscriber.fields.cohort_tag }}` | Cohort assigned by post-purchase survey or manual review | omit cohort greeting, use Gift Buyer generic |

**Cohort tags in Kit** (use exact names — do not create variants):
`Cohort_Forager`, `Cohort_Prepper`, `Cohort_Homesteader`, `Cohort_GiftBuyer`, `Cohort_Herbalist`

**Lifecycle tags applied during these campaigns:**
- `purchased` — trigger tag; must be applied before Campaign 1 fires
- `engaged-buyer` — apply manually in Kit when a subscriber replies to any email
- `re-engagement-sent` — Kit applies automatically (add to Campaign 4 setup)

---

*Copy status: paste-ready for all 7 emails. Before entering into Kit: (1) write zone-specific content blocks for each zone variant of Emails 1B and 2.2 — these are marked [ZONE CONTENT BLOCK] above. (2) Confirm product names and Etsy listing URLs for the pairing logic in Email 3.1. (3) Verify SEEDWARDEN15 coupon is active in Etsy before Email 3.1 sends.*
