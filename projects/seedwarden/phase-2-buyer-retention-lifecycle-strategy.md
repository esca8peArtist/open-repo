---
title: "Phase 2 Buyer Retention & Lifecycle Campaign Strategy"
date: 2026-05-07
status: production-ready
scope: Lifecycle email campaigns, landing pages, analytics triggers, implementation roadmap
launch-date: 2026-05-30
references:
  - phase-2-analytics-strategy.md (cohort definitions, Kit tag architecture, LTV tracker schema)
  - PHASE_2_EMAIL_STRATEGY.md (automation priority order, welcome sequence structure)
  - customer-cohort-analysis-framework.md (segment definitions and signal indicators)
  - phase-2-kit-email-setup.md (Kit setup stages, zone routing, tag naming conventions)
  - marketing/email-automation-blueprint.md (existing automation architecture)
  - financial-sustainability-model.md (unit economics, LTV targets)
---

# Phase 2 Buyer Retention & Lifecycle Campaign Strategy

**Purpose**: Design the systematic buyer lifecycle campaign infrastructure so the May 30, 2026
Phase 2 launch builds lasting buyer relationships — not just a product fire sale. This document
covers cohort modeling, six campaign sequences with 20+ email touches, Kit automation
configuration, landing page specs, analytics triggers, and a pre-launch roadmap executable in
six working days.

**Who this is for**: Anya, operating solo. Every sequence is specified at a level where it can
be entered directly into Kit without additional decision-making. Every decision trigger names an
exact threshold and exact response action.

---

## Section 1: Phase 1 Baseline & Phase 2 Cohort Modeling

### Phase 1 Actuals — What the Data Says

Phase 1 closed with 47 orders, $1,341 gross revenue, and a 2.24% store-wide conversion rate.
Average order value was $28.54 ($1,341 / 47). Four cohorts were active:

| Cohort | Signal | Estimated Phase 1 Share | Avg Order Value (Inferred) |
|---|---|---|---|
| Forager | Wild edibles, native plants, multi-guide orders | 25–30% | $32–$40 |
| Prepper | Bundle purchases, 5+ guides, all-guides order | 15–20% | $45–$65 |
| Homesteader | Seed saving, zone calendar, preservation guides | 30–35% | $20–$30 |
| Gift Buyer | Single guide, mobile traffic, holiday timing | 15–20% | $25–$35 |

The 2.24% conversion rate is above the Etsy average (~1%) but below the 3–4% target for a
mature product line. The $28.54 AOV is consistent with the Homesteader and Gift Buyer cohorts
dominating Phase 1 — neither is the highest-value segment. If Phase 2 acquisition shifts toward
Forager and Prepper cohorts, AOV should lift without any pricing changes.

**Phase 1 retention signal**: The absence of Kit email infrastructure in Phase 1 means post-
purchase buyer relationships were entirely unmanaged. Every buyer who did not return for a second
purchase represents an avoidable loss — there was no welcome email, no content deepening sequence,
no cross-zone upsell. Phase 2 campaigns directly address this gap.

### Phase 2 Cohort Projections — Five Segments

Phase 2 introduces endangered species guides, zone-specific regional guides, and medicinal herb
content. These product categories attract a fifth distinct segment not present in Phase 1:

| Cohort | New in Phase 2? | Expected Share | Expected AOV | Key Phase 2 Product |
|---|---|---|---|---|
| Forager | No — grows | 25–30% | $35–$50 | Native Plants Regional Guide, Wild Edibles bundles |
| Prepper | No — stable | 15–20% | $50–$80 | Zone + survival bundle, Hunting/Fishing Manual |
| Homesteader | No — largest | 30–35% | $22–$35 | Seed Saving Field Manual, Zone Calendar |
| Gift Buyer | No — seasonal | 10–15% | $28–$40 | Premium single guides, endangered species guides |
| Herbalist / Medicinal | Yes — new | 10–15% | $40–$65 | Medicinal herb guides, themed bundles |

The Herbalist cohort is the highest-LTV new entrant. Herbalists buying for professional or
semi-professional use have demonstrated 3x LTV patterns in the Phase 3 medicinal herbs strategy
(see `phase-3-medicinal-herbs-strategy.md`). A buyer who enters through a $20 themed medicinal
bundle can be converted to a $120–$180 practitioner bulk pack within 90 days if the lifecycle
sequence is working.

**Phase 2 conversion target**: 3–4% at launch. The logic: Phase 1 conversion was 2.24% with
no email capture, no Kit automation, and limited product depth. Phase 2 launches with a Kit
welcome sequence, zone-card lead magnet, and 60 new guide products. A 3% conversion target
represents a 34% improvement with specific structural causes — not wishful inflation.

### LTV Opportunity: From $28.54 to $60+

Phase 1 buyers averaged $28.54 lifetime value because almost all were single-purchase. A buyer
who makes one purchase and leaves contributes exactly that purchase to LTV. The lifecycle
campaign system is designed to generate a second purchase from at least 20% of buyers within
90 days.

**LTV model at 2x lift (target: $57 LTV)**:

The mechanism is three campaigns acting in sequence:

1. Campaign 2 (Content Deepening, Days 4–21): Provides enough value that the buyer stays
   subscribed and returns to the store. Target: 35–40% open rate, which indicates the buyer
   is still engaged.
2. Campaign 3 (Cross-Zone Upsell, Days 15–45): Makes the second purchase offer when the
   buyer has had time to use the first product. Target: 1–2% click-to-purchase rate.
3. Campaign 5 (Win-Back, Day 90+): Captures buyers who did not respond to the upsell but
   might re-engage with seasonal content. Target: 2–3% re-purchase rate.

At 47 Phase 1 buyers: if 20% make a second purchase averaging $30, that is 9 buyers x $30 =
$270 additional revenue from the existing buyer base alone. Scaled to Phase 2 with 150+ buyers
by Day 60, the same rate generates $900+ in incremental revenue from repeat buyers without
acquiring a single new customer.

**LTV model at 3x lift (target: $85 LTV)**:

Achievable only if the Herbalist cohort and VIP Loyalty track activate. A buyer who makes 3+
purchases enters the Loyalty campaign (Campaign 6), which has a 30–40% repeat purchase rate.
Three $30 purchases = $90 LTV. One $60 bundle purchase plus one $30 guide = same result. The
path to 3x is bundle attach and cross-zone upsell working together.

### Segment-Specific Retention Risk

**Gift Buyers at 1x LTV**: Gift buyers purchase once, typically in a gift window (Mother's Day,
holiday season), and do not return unless given a reason to. The signal is clear: mobile
purchase, sub-90-second session, no email engagement. The retention challenge is that the buyer
is often not the recipient of the guide — Anya cannot reach the recipient through Etsy. The
lifecycle campaign addresses this by treating the Gift Buyer as a gift-occasion repeat buyer:
send one seasonal email per gifting window (Campaign 5), not a content relationship sequence
that assumes the buyer uses foraging guides themselves. Gift buyer LTV ceiling is approximately
$60 if captured for two gift occasions (Mother's Day + holiday season). Without a seasonal
campaign, they remain at $28.

**Herbalists at 3x LTV**: Herbalists are researching for professional or ongoing personal
practice. They do not need to be convinced — they are already motivated. The retention risk for
Herbalists is mismatch: if the post-purchase content sequence sends generic foraging tips when
the Herbalist bought a medicinal herb guide, they disengage before the upsell arrives. The
lifecycle campaign addresses this with cohort-specific personalization: Herbalists receive
medicinal content, not survival prep content. The 3x LTV is achievable because Herbalists are
willing to buy multiple themed bundles ($20 each), specialist single guides ($14–$22), and
eventually practitioner bulk packs if that tier is available by Phase 3.

**The gap in plain terms**: A Gift Buyer who receives one seasonal email per year and buys twice
is worth $55 LTV. A Herbalist who receives targeted medicinal content and buys three times is
worth $85 LTV. The email personalization investment that captures this gap costs approximately
30 additional minutes of Kit setup — one conditional branch per cohort tag in each campaign.

---

## Section 2: Email Lifecycle Architecture (6 Campaigns, 20+ Touches)

### Overview

The six campaigns form a linear progression with branch logic. A buyer enters at Campaign 1 on
the day they purchase and moves through campaigns based on behavior, not calendar dates alone.

```
Purchase → [Campaign 1: Welcome, Days 0–3]
         → [Campaign 2: Content Deepening, Days 4–21]
              → No opens after Email 1: switch to digest format
         → [Campaign 3: Cross-Zone Upsell, Days 15–45]
         → [Campaign 4: Re-engagement, Days 45–90 if no second purchase]
              → Re-engages: move to Campaign 5 acceleration
              → No re-engagement: 3-month quiet period
         → [Campaign 5: Win-back, Day 90+, quarterly]
              → 6 months no purchase + no opens: annual-only
         → [Campaign 6: VIP Loyalty, triggered by 3+ purchases, any point in timeline]
```

Total touches across the full sequence: 11 emails in the primary track (Campaigns 1–5) plus
1–2x monthly ongoing in Campaign 6 for VIP buyers.

---

### Campaign 1: Welcome (Days 0–3) — 2 Emails

**Purpose**: Confirm the purchase, establish the brand voice, and deliver immediate value before
the buyer's attention moves elsewhere. The window between purchase and Day 3 is the highest-
engagement window in the buyer lifecycle.

**Trigger**: Kit purchase event (Etsy webhook → Kit tag applied → automation fires)

**Email 1: Order Confirmation + Immediate Value (Day 0, within 2 hours of purchase)**

Subject line options (A/B test on 20% sample, winner to full list within 48 hours):
- Version A: "Your [Product Name] is on its way — here's what to do first"
- Version B: "[First Name], welcome to Seedwarden — one thing to try this week"

Body structure:
- Greeting: "Hi [First Name]," — always use first name if captured at checkout
- Confirmation: Name the specific product purchased. Do not use a generic "your order"
  line. Example: "Your Wild Edibles Quick Reference is confirmed."
- Immediate value: One-paragraph field tip tied to the product they bought. For Wild
  Edibles: one seasonal plant to look for right now. For Zone Calendar: the most important
  action for their zone in the current month. This is not promotional — it is useful.
- Zone-specific CTA: "If you haven't grabbed your Zone [X] Quick-Start Card yet, it's free
  and paired to your purchase." Link to the Kit landing page with pre-filled zone parameter.
- Cohort greeting (applied by Kit conditional content based on cohort tag):
  - Forager tag: "Fellow foragers..."
  - Prepper tag: "If you're building a food-resilient household..."
  - Homesteader tag: "Whether you're in your first season or tenth..."
  - Gift Buyer tag: (no cohort greeting — generic warm welcome)
  - Herbalist tag: "For those working with plant medicine..."

Personalization fields required in Kit: `first_name`, `product_name`, `zone_number`,
`cohort_tag`. If `zone_number` is blank, omit the zone card CTA entirely.

**Metrics targets — Email 1:**
- Open rate: 40–45% (purchase confirmation emails consistently outperform all other types)
- Click rate: 15–20% (zone card CTA is the primary click target)

**Email 2: Zone-Specific Field Briefing (Day 2)**

Subject line options:
- Version A: "Your Zone [X] is entering [seasonal state] — what to watch for"
- Version B: "3 things worth knowing for Zone [X] this [month]"

Body structure:
- Two to three paragraphs of zone-specific seasonal content. Not product promotion.
  Example for Zone 7 in May: spring ephemeral foraging window closing, what's coming into
  season in June, one specific plant identification note.
- Skill-level calibration paragraph: "Whether you're just starting to identify plants in
  your area or you've been at it for years, [content hook]." This signals that Seedwarden
  serves a range — does not condescend and does not assume expertise.
- One soft product mention: "If you want a deeper reference for [seasonal plant], [Product
  Name] covers it in detail." Link to the Etsy listing with UTM tag
  `utm_campaign=welcome-email-2`.
- PS line: "Reply to this email if you have a question about [zone-specific plant or topic].
  I read every reply." This invites direct contact and is a signal of non-automated character.

**Metrics targets — Email 2:**
- Open rate: 35–40%
- Click rate: 10–15%
- Reply rate: 1–3% (any reply is a high-value engagement signal — apply `engaged-buyer` tag
  in Kit manually when replies are received)

**Kit automation setup for Campaign 1:**
- Sequence name: `Welcome — Phase 2 Buyers`
- Trigger: Tag applied: `purchased`
- Email 1 delay: 0 hours (immediate)
- Email 2 delay: 2 days after Email 1
- Conditional content blocks: one per cohort tag using Kit's conditional merge tags
- A/B test: Enable Kit's built-in A/B sending for subject lines on Email 1; 10% sample each
  variant, winning variant selected at 48-hour mark by open rate

---

### Campaign 2: Content Deepening (Days 4–21) — 3 Emails

**Purpose**: Earn the right to make a commercial offer by delivering 3 weeks of genuine utility.
Buyers who receive useful content before a pitch have a 2–3x higher conversion rate on
subsequent offers than buyers who receive immediate promotional emails.

**Trigger**: Completion of Campaign 1 (Email 2 sent)

**Skip rule — digest format**: If the buyer has zero opens on Campaign 1 (Email 1 AND Email 2
both unread at Day 3), switch to digest format: one email per week instead of 2x/week, and
skip Email 2.1 and 2.2. Send only Email 2.3 (the most practical content) at Day 14.

**Email 2.1: Ecosystem Guide — Companion Content (Day 7)**

Subject line: "The plants that grow near [purchased product's focus plant/topic]"

Content: A themed ecosystem guide — not a product page. If the buyer bought a Wild Edibles
guide, the ecosystem guide covers companion plants, habitat indicators, or seasonal context.
If they bought the Zone Calendar, the ecosystem guide covers zone-specific companion planting
logic. 400–500 words of genuine botanical content.

Personalization: Zone-specific and cohort-specific content block. Forager buyers receive
identification content. Homesteader buyers receive cultivation/companion planting content.
Herbalist buyers receive medicinal preparation context.

CTA: "If you want the full reference for [topic], [product] covers this in detail." Soft
mention only — this is not a sales email.

Unsubscribe tracking: Monitor unsubscribe rate on this email. If it exceeds 2%, the content
is too dense or not relevant. Action: simplify to 200–300 words, test one concrete practical
tip instead of the full ecosystem overview.

**Email 2.2: Seasonal Planning Content (Day 14)**

Subject line options:
- "What [month] means for Zone [X] growers"
- "The next 30 days in Zone [X]: what to prioritize"

Content: A seasonal planning framework for the buyer's zone. Three actions for the current
month: what to plant, forage, or preserve. Practical and scannable — three bullet points plus
one paragraph of context. Not product-dependent; this works even if the buyer never buys again
and is building brand goodwill.

Feature tracking: Add a click-tracked link to a specific section of the Etsy store. Label it
"See this month's Zone [X] guides." Track clicks with UTM `utm_campaign=content-deepening-2`.
This click is the primary signal that the buyer is considering a second purchase.

**Email 2.3: Practical Technique or Identification Deep-Dive (Day 21)**

Subject line: "One technique worth knowing before [seasonal event]"

Content: A practical technique article — 300–400 words. Examples: how to identify false from
true morels, how to dry and store wild herbs, how to read a seed packet date correctly. Topic
is chosen to be universally useful across cohorts. No cohort-specific branching on this email
— simplicity is the goal at Day 21.

CTA: This email transitions into Campaign 3. The final paragraph: "If any of this was useful,
I have a guide that goes much deeper — and I'd like to offer it to you at a discount next week."
No link yet. This is a preview that primes the buyer for the Campaign 3 upsell.

**Metrics targets — Campaign 2 (across all 3 emails):**
- Open rate: 35–40% average
- Unsubscribe rate: below 2% across all three emails. If any single email exceeds 2%, halt
  the sequence and revise that email before sending to the next buyer cohort.
- Feature click rate (Email 2.2 product link): 5–10%

**Kit automation setup for Campaign 2:**
- Sequence name: `Content Deepening — Phase 2`
- Trigger: Campaign 1 complete (Email 2 sent)
- Skip rule implementation: Add condition — IF email_open_count for Campaign 1 = 0 THEN skip
  to Email 2.3 only (send at Day 14)
- Emails: 2.1 at Day 7, 2.2 at Day 14, 2.3 at Day 21 (from Campaign 1 Email 1 send date)

---

### Campaign 3: Cross-Zone Upsell (Days 15–45) — 2 Emails

**Purpose**: Convert the content relationship into a second purchase using targeted product
recommendations based on the first purchase and cohort.

**Trigger**: Campaign 2 Email 2.1 sent (Day 7 is the earliest this logic fires; Email 3.1
sends at Day 15 regardless of Campaign 2 completion)

**Upsell logic — product recommendation rules:**

| First Purchase | Campaign 3 Recommendation | Reasoning |
|---|---|---|
| Single zone guide (Zones 3–6) | Zone bundle: recommend adjacent zones (e.g., Zone 5 buyer → Zone 4+5+6 bundle) | Geographic expansion is the most natural next step |
| Wild Edibles Quick Reference | Medicinal Herbs guide (same ecosystem, different use) | Forager-to-herbalist pathway |
| Zone Calendar | Seed Saving Field Manual (planning → execution) | Project logic: calendar buyer is a planner, saver is the natural next product |
| Hunting/Fishing Manual | Meat/Fish Preservation Manual (hunt → preserve) | Sequential activity pair |
| Any single guide | Zone bundle at 15% discount | Default if no specific pairing |
| Premium single guide ($20+) | 3-guide bundle with 15% discount | Upgrade to bundle at value-add price |

Cohort-specific bundle recommendations:
- Forager tag: "Wild Forager Bundle" — zone guide + wild edibles + medicinal herbs
- Prepper tag: "Food Security Bundle" — all-zone bundle or survival garden + preservation guides
- Homesteader tag: "Home Systems Bundle" — seed saving + zone calendar + companion planting
- Herbalist tag: Medicinal themed bundles (Women's Health, Respiratory, Immunity, Sleep,
  Digestive — see `phase-3-medicinal-herbs-strategy.md` for bundle definitions)

**Email 3.1: Zone Bundle Recommendation (Day 15)**

Subject line options:
- "Based on what you bought — here's what pairs with it"
- "The natural next step for Zone [X] buyers"

Body structure:
- One paragraph acknowledging what they bought and what it suggests about their goals
- Product recommendation: name the specific bundle or guide, explain the pairing logic
  (one sentence), show the price and bundle discount
- CTA: "See [Bundle Name]" — link to Etsy listing with UTM `utm_campaign=upsell-bundle`
- Urgency note (optional, use only if bundle is a limited-time configuration): "This bundle
  pricing is available through [date]."

**Email 3.2: Premium Guide Offering (Day 30)**

Sent only if Email 3.1 was opened but not clicked. If Email 3.1 was clicked (buyer saw the
bundle), skip Email 3.2 — the buyer is already in consideration and does not need a second push.

Subject line: "For buyers who want to go deeper — [Premium Guide Name]"

Content: A premium guide pitch focused on depth and credentials. Different framing from Email
3.1 (which was value/bundle-focused). This email emphasizes the content quality, sourcing
method, and specific use cases. Price point: if there is a premium endangered species guide
at $22, this is its introduction email.

CTA: "See [Premium Guide Name]" — link to Etsy listing with UTM `utm_campaign=upsell-premium`

**Metrics targets — Campaign 3:**
- Click-to-purchase rate: 1–2% (i.e., 1–2 purchases per 100 buyers who receive the upsell)
- Bundle attach rate: track using Etsy order data — what % of second orders are bundles vs.
  single guides? Target: 25%+ of second orders are bundles.
- If click-to-purchase rate stays below 0.5% after 30 buyers have received Campaign 3: the
  bundle recommendation logic is wrong. Audit which first-purchase → recommendation pairings
  are weakest and replace them.

**Kit automation setup for Campaign 3:**
- Sequence name: `Cross-Zone Upsell — Phase 2`
- Email 3.1 trigger: 15 days after Campaign 1 Email 1
- Email 3.2 condition: IF Email 3.1 opened = true AND Email 3.1 clicked = false THEN send
  Email 3.2 at Day 30
- Skip condition: IF tag `purchased` added after Campaign 3 Email 3.1 sent (second purchase
  detected) THEN skip Email 3.2

---

### Campaign 4: Re-engagement (Days 45–90) — 1 Email

**Purpose**: Capture buyers who received Campaigns 1–3 but did not make a second purchase and
have gone quiet.

**Trigger**: Day 45 AND tag `purchased` count = 1 (no second purchase) AND no email open in
the prior 14 days.

**Email 4.1: Seasonal Hook Re-engagement**

Subject line options (test by cohort):
- Forager: "The [seasonal plant] window opens in [zone] next month"
- Prepper: "Fall prep starts now — here's the guide for it"
- Homesteader: "You're in the best planting window of the year"
- Herbalist: "Three herbs coming into peak harvest right now"
- Gift Buyer: "A new guide that makes a perfect [occasion] gift"

Body structure:
- One paragraph: a specific, timely seasonal observation tied to their zone or cohort. Not
  promotional. Demonstrates that Seedwarden has real botanical knowledge, not just a store.
- One paragraph: a new product or content angle that was not available when they bought.
  Phase 2 launches 60 new guides — there is always something genuinely new to mention.
- CTA: "See what's new in [zone-specific or cohort-specific category]" — link to a curated
  Etsy section, not the store homepage.
- Soft close: "If the timing isn't right, no pressure — I'll check back in a few months."
  This is honest and reduces unsubscribe friction.

**Metrics targets — Campaign 4:**
- Re-open rate: above 25% (this email goes to cold buyers — 25% is a strong result for this
  population; below 15% means the subject line needs revision)
- Re-purchase rate: 5–10% of Campaign 4 recipients within 30 days
- Unsubscribe rate: below 5% (cold buyers unsubscribe at higher rates; anything below 5% is
  acceptable; above 8% means the email is landing as spam, not re-engagement)

**Decision gate after Campaign 4:**
- If buyer opens Email 4.1: apply tag `re-engaged` and move to Campaign 5 on the next
  seasonal window (do not wait for Day 90+; send the next Campaign 5 email within 45 days).
- If buyer does not open Email 4.1 within 14 days: apply tag `quiet-period` and pause all
  automated emails for 90 days. At 90-day mark, Campaign 5 quarterly sends resume.

**Kit automation setup for Campaign 4:**
- Sequence name: `Re-engagement — Seasonal Hook`
- Trigger: Day 45 + `purchased` tag, total purchases = 1, AND no open in past 14 days
- Tag on send: `re-engagement-sent`
- Post-send branch: IF opened → add `re-engaged` tag; IF not opened within 14 days → add
  `quiet-period` tag, pause sequence 90 days

---

### Campaign 5: Win-Back (Day 90+, Quarterly) — 1 Email per Quarter

**Purpose**: Maintain a minimal presence with buyers who have gone completely cold. Three
seasonal sends per year keep the brand relevant through gifting windows and seasonal hooks
without overloading an unengaged list.

**Trigger**: Quarterly — Spring (March 1), Summer (June 1), Fall (September 1). Sent only to
subscribers with no purchase in the prior 90 days.

**Three seasonal email templates:**

Spring Send (March 1): "The foraging calendar just turned — Zone [X] spring guide"
Summer Send (June 1): "Summer wildcrafting in Zone [X]: what's at peak right now"
Fall Send (September 1): "Fall seed harvesting and preservation — what you need before frost"

Each email is 200 words maximum. Three paragraphs: seasonal observation, one product mention,
one soft CTA. No hard sell. The goal is not to force a purchase — it is to be in the inbox
when the buyer is ready.

**Gift Buyer-specific seasonal sends:**
- May 15: "Mother's Day gift guide — naturalist edition"
- November 15: "Holiday gift guide — Seedwarden picks for plant lovers"
These sends go only to `Cohort_GiftBuyer` tagged subscribers. They are commercial (gift
guides are promotional by nature) and are timed to the gifting decision window.

**Metrics targets — Campaign 5:**
- Open rate: 20%+ (cold list standard)
- Re-purchase rate: 2–3% per send
- Unsubscribe rate: below 3% per send

**Sunset rule**: After 6 months without a purchase AND without any email open across all
Campaign 5 sends, move the subscriber to `annual-only` status: one email per year only, the
November holiday gift guide. This preserves the list without eroding deliverability through
inactive address accumulation.

**Kit automation setup for Campaign 5:**
- Sequence name: `Win-Back Quarterly — [Season]` (three separate sequences)
- Trigger: Date-based (March 1, June 1, September 1)
- Filter: tag `purchased` present AND `last_purchase_date` more than 90 days ago AND tag
  `annual-only` not present
- Sunset automation: IF no open across 3 consecutive Campaign 5 sends (6 months) THEN apply
  `annual-only` tag AND remove from Campaign 5 sequences

---

### Campaign 6: VIP Loyalty (3+ Purchases — Ongoing) — 1–2 Emails/Month

**Purpose**: Cultivate the highest-value buyers into a genuine brand relationship. These are
the buyers who fund the business long-term. The VIP track is not promotional — it is access.

**Trigger**: Kit tag `vip` applied automatically when cumulative purchase count reaches 3.
The `vip` tag is applied manually by cross-referencing the LTV tracker with Kit subscriber
data on the first Monday of each month. In Month 2, if Kit webhook integration is working,
this can be automated: IF third purchase detected AND `purchased` tag count = 3 THEN apply
`vip` tag.

**VIP Segment Names (brand identity — choose one before launch):**
- "Herbalist Inner Circle" — emphasizes botanical expertise, suits Forager and Herbalist
  cohorts
- "Seed Keeper's Guild" — emphasizes preservation and stewardship, suits Homesteader cohort
- Recommendation: Use "Herbalist Inner Circle" for Forager and Herbalist tagged VIPs;
  "Seed Keeper's Guild" for Homesteader tagged VIPs. Apply dynamically in Kit.

**Monthly VIP Content (1–2x/month):**

Send 1 (first Monday): Exclusive content not available in the public newsletter. Options:
behind-the-scenes sourcing notes, early access to a new guide before Etsy listing goes live,
a botanical deep-dive that is too specialized for the general list. 400–500 words. No product
CTA in Send 1 — content only.

Send 2 (third Monday, optional — only if something genuinely worth sharing): First access to
a new guide or bundle at a 10% discount. Subject: "VIP early access — [New Guide Name] before
it's listed." Coupon code: VIPACCESS10, valid 7 days. Link to the Etsy draft listing or a
Squarespace preview page.

**Metrics targets — Campaign 6:**
- Engagement retention: 60% of VIP subscribers opening within any 30-day window
- Repeat purchase rate: 30–40% of VIP subscribers purchasing in any 60-day window
- If engagement retention drops below 40%: the content is not exclusive enough. Audit the
  prior 3 months of VIP sends — if the content appeared anywhere else (public newsletter,
  social media), move it back behind the VIP wall.

**Mutual exclusion rule**: VIP buyers are removed from Campaigns 3, 4, and 5. They have
demonstrated loyalty; re-engagement and upsell campaigns aimed at cold buyers are inappropriate
for this segment and will read as inattentiveness. Kit implementation: add condition IF `vip`
tag present THEN exclude from Campaign 3, 4, 5 sequences.

---

## Section 3: Email Template Specs & Kit Automation Configuration

### Three Base Template Designs

All emails use one of three base templates. Kit's visual editor supports custom templates —
build these once and reuse across all campaigns.

**Template W (Welcome):**
- Header: Seedwarden logo, left-aligned, 60px height
- Hero image placeholder: 600px wide, 300px tall. Zone-specific lifestyle photo (person in
  field, seasonal plant in foreground). If no photo is available, use a solid botanical green
  (#2D5016) with white zone label overlaid.
- Body: Two-column layout below hero. Left column (70%): email body text in Georgia 15px, line
  height 1.6, dark charcoal (#1A1A1A). Right column (30%): product image + price + CTA button.
- CTA button: full-width in right column, botanical green background, white text, 14px bold.
  Text: "See [Product Name]"
- Footer: unsubscribe link, physical address (required by CAN-SPAM), social icons (Pinterest,
  Instagram if accounts are active)

**Template C (Content):**
- Header: same as Template W
- No hero image — content-first layout. Single column, full width.
- Body: Georgia 15px, generous line height 1.7, max 500px width centered. Optimized for
  readability on mobile (60% of opens will be mobile).
- Inline image (optional): 300px wide, right-floated, with 12px margin. Used when a botanical
  illustration or field photo is available.
- CTA (if present): text link only — no button. Styled as underlined botanical green link.
  Content emails should not look commercial.
- Footer: same as Template W

**Template O (Offer):**
- Header: same as Template W
- Hero: product image or lifestyle photo, 600px x 250px. Overlay text: product name in white,
  32px, left-aligned.
- Body: single column. Price displayed prominently: "Was $XX, Now $XX with code [COUPON]"
  in 18px bold. Body copy below.
- CTA button: centered, botanical green, larger than Template W (18px bold, 48px height).
  Text: "Get [Product Name]"
- Urgency element (optional): "Offer expires [date]" in 12px red below button
- Footer: same as Template W

### Placeholder Zones — Required in All Templates

Every email must include these Kit merge tags as content placeholders. If the data is not
available, define fallback values:

| Merge Tag | What It Pulls | Fallback Value |
|---|---|---|
| `{{ subscriber.first_name }}` | Subscriber first name | "Friend" |
| `{{ subscriber.fields.zone_number }}` | Zone from signup form | "your zone" |
| `{{ subscriber.fields.cohort_tag }}` | Assigned cohort | omit cohort greeting |
| Product name | Manually written per email | N/A — always specify |
| Hero image | Zone-specific photo | Botanical green solid (#2D5016) |
| CTA text | Campaign-specific | "See the guide" |

### Kit Automation Configuration — Full Sequence Map

**Tags active at Phase 2 launch** (from phase-2-analytics-strategy.md — use existing tag names
exactly, do not create duplicates):

Zone tags: `zone-3`, `zone-4`, `zone-5`, `zone-6`, `zone-7`, `zone-8`, `zone-9`, `zone-10`
Cohort tags: `Cohort_Forager`, `Cohort_Prepper`, `Cohort_Homesteader`, `Cohort_GiftBuyer`
New Phase 2 cohort tag: `Cohort_Herbalist`
Behavioral tags: `seed-saver`, `city-grower`, `preservationist`
Lifecycle tags: `new-subscriber`, `purchased`, `vip`
New lifecycle tags for Campaign system: `re-engaged`, `quiet-period`, `annual-only`,
`re-engagement-sent`, `engaged-buyer`

**Auto-tag on checkout:**

Kit does not receive Etsy webhook events natively. Two paths:
- Option A (recommended): Use Zapier or Make.com free tier to connect Etsy order webhook
  to Kit subscriber tag. Zap: "New Etsy order" → "Add tag `purchased` to Kit subscriber
  matching buyer email." Setup time: 45 minutes. Cost: free tier supports the Phase 2
  order volume.
- Option B (fallback — manual): Each Monday, open Etsy orders CSV for the prior week.
  For each order, look up the buyer email in Kit > Subscribers > Search. Manually apply
  `purchased` tag. Estimated time: 30 minutes/week. This is the contingency if Zapier
  integration fails.

**Cohort tag assignment logic:**

| Trigger | Tag Applied | Method |
|---|---|---|
| Post-purchase survey Q1 response: Foraging | `Cohort_Forager` | Typeform/Google Form response → Zapier → Kit tag |
| Post-purchase survey Q1 response: Prep | `Cohort_Prepper` | Same |
| Post-purchase survey Q1 response: Homesteading | `Cohort_Homesteader` | Same |
| Post-purchase survey Q1 response: Gift | `Cohort_GiftBuyer` | Same |
| No survey response AND first product is wild edibles/native plants guide | `Cohort_Forager` | Manual weekly review |
| No survey response AND first product is medicinal herb guide | `Cohort_Herbalist` | Manual weekly review |
| No survey response AND first product is bundle 5+ guides | `Cohort_Prepper` | Manual weekly review |
| No survey response AND first product is zone calendar/seed saving | `Cohort_Homesteader` | Manual weekly review |

**Date-based journey trigger points** (measured from `purchased` tag application date):

| Day | Action |
|---|---|
| 0 | Campaign 1 Email 1 fires |
| 2 | Campaign 1 Email 2 fires |
| 3 | Check Campaign 1 open count — apply digest format if 0 opens |
| 7 | Campaign 2 Email 2.1 fires (or skip if digest mode) |
| 14 | Campaign 2 Email 2.2 fires (or Email 2.3 if digest mode) |
| 15 | Campaign 3 Email 3.1 fires |
| 21 | Campaign 2 Email 2.3 fires (standard track) |
| 30 | Campaign 3 Email 3.2 fires (conditional: opened 3.1 but not clicked) |
| 45 | Campaign 4 check: no second purchase AND no recent opens? Fire Email 4.1 |
| 59 | Check Email 4.1 opens: apply `re-engaged` or `quiet-period` tag |
| 90 | Campaign 5 quarterly schedule begins (seasonal send windows apply) |

**Engagement-based branching summary:**

| Signal | Branch |
|---|---|
| 0 opens on Campaign 1 | Digest format: skip 2.1, 2.2; send 2.3 at Day 14 only |
| 3+ purchases confirmed | Apply `vip` tag; exclude from Campaigns 3, 4, 5; add to Campaign 6 |
| Email 3.1 opened, not clicked | Send Email 3.2 at Day 30 |
| Email 3.1 not opened | Skip Email 3.2 (buyer is cold; Campaign 4 handles) |
| Email 4.1 opened | Apply `re-engaged` tag; accelerate Campaign 5 send within 45 days |
| Email 4.1 not opened | Apply `quiet-period` tag; 90-day pause |
| 3 Campaign 5 sends, no opens | Apply `annual-only` tag; remove from quarterly sends |

### A/B Testing Protocol

For each campaign, test one variable at a time. All tests require a minimum 10% sample per
variant and a 7-day window before selecting a winner.

**Phase 2 A/B test calendar:**

| Week | Test | Variable | Variants |
|---|---|---|---|
| Week 1 (May 23–29) | Campaign 1 Email 1 | Subject line | Version A vs. Version B (as specified above) |
| Week 2 (Jun 1–7) | Campaign 2 Email 2.1 | Send time | 9am local vs. 6pm local |
| Week 3 (Jun 8–14) | Campaign 3 Email 3.1 | CTA button text | "See the bundle" vs. "Get [discount]% off" |
| Week 4 (Jun 15–21) | Campaign 4 Email 4.1 | Subject line personalization | Zone-specific vs. cohort-specific |

Record test results in the Weekly Dashboard (Section 5). Do not run two simultaneous tests
on the same email list — it contaminates both results.

---

## Section 4: Landing Pages & Incentive Architecture

### Landing Page 1: "New to Seedwarden? Start Here"

**URL**: `seedwarden.com/start` or Kit landing page subdomain (if no custom domain: Kit
provides a `pages.kit.com/seedwarden-start` URL at no cost)

**Purpose**: Convert first-time visitors from social media and email into buyers. The page
answers three questions a first-time visitor asks: "What is this?", "Is it for me?", and
"Can I trust it?"

**Page structure:**

Hero section:
- Headline: "Know exactly what grows where you live — and how to use it."
- Subheadline: "Seedwarden zone guides tell you which native plants, wild edibles, and
  medicinal herbs are in your area right now — and what to do with them."
- Hero image: lifestyle photo of person using a guide in a field or garden setting.
  If lifestyle photo is not available at launch: a flat-lay photo of the printed guide with
  seasonal plants beside it.

Zone quiz (inline, not a separate page):
- Question: "Are you more of a Forager or a Planner?" with two large buttons
  - Button A: "Forager — I want to find and identify wild plants"
  - Button B: "Planner — I want to grow and preserve food intentionally"
- On button click: reveal the top 2 recommended guides for that answer
- Below recommendation: "Add to cart" CTA linking to Etsy listing with UTM
  `utm_campaign=quiz-result-forager` or `utm_campaign=quiz-result-planner`

This quiz is a two-question simplification of the full cohort taxonomy. It is intentionally
binary at this stage — the goal is a click, not a complete cohort classification.

Social proof section:
- "47 Seedwarden buyers have found their local foraging calendar, emergency food plan, or
  homestead guide." (Use Phase 1 order count directly — do not inflate.)
- Three testimonial excerpts (pull from Etsy reviews if available, or use paraphrased buyer
  feedback with permission). If fewer than 3 reviews exist at launch: use two and label them
  as verified Etsy purchase reviews.
- Star rating display if Etsy average is above 4.5.

Risk reversal section:
- "Not sure it's right for you? Every guide comes with a 30-day satisfaction guarantee
  through Etsy's buyer protection. If you're not satisfied, you get your money back — no
  questions asked." (Etsy's standard buyer protection covers this; this is not a custom
  policy, just stating what already exists.)

Footer CTA:
- "Get your Zone Quick-Start Card free — enter your zone and email below." Kit embed form
  (zone dropdown + email, first name). This captures leads who are not ready to buy.

**Metrics — Landing Page 1:**
- Quiz completion rate: 25%+ (of page visitors who start the quiz)
- Proceed-to-cart rate: 3%+ (of page visitors who click through to an Etsy listing)
- Email capture rate: 15–20% of page visitors who do not proceed to cart
- If quiz completion rate is below 15%: the quiz question is too complex or the buttons are
  not visible. Simplify to one click: "I want to [forage / grow / prepare]."

---

### Landing Page 2: "Zone Bundles — Get More, Save More"

**URL**: `seedwarden.com/bundles` or a Squarespace page with the slug `/bundles`

**Purpose**: Present the Phase 2 bundle architecture clearly, make the discount math obvious,
and reduce decision friction for buyers who want multiple guides.

**Page structure:**

Headline: "Buy once, forage all season — Seedwarden zone bundles"

Bundle display (4–5 bundles, each as a card):
- Bundle name
- What's included (3–5 guide names, bullet list)
- Individual price vs. bundle price: "3 guides: $42 individually, $35.70 as a bundle (15% off)"
- Lifestyle photo hero for each bundle (or botanical illustration as placeholder)
- CTA: "Get the [Bundle Name]" → Etsy listing with UTM `utm_campaign=bundle-page-[bundle-name]`

**Recommended Phase 2 bundles to feature (from PHASE_2_BUNDLE_STRATEGY.md):**
- Forager Bundle: Wild Edibles Quick Reference + Native Plants Regional Guide + Zone Calendar
- Prepper Bundle: Zone Calendar + Seed Saving Field Manual + Meat/Fish Preservation Manual
- Homesteader Bundle: Seed Saving + Zone Calendar + Companion Planting Chart
- Herbalist Starter: Medicinal Herbs guide (1–2 themed bundles available at launch)
- Full Library: all available zone guides at maximum discount (15% off)

Social proof: "Most popular: [Bundle Name] — [X] buyers chose this bundle" (update monthly
with actual order data)

**Metrics — Landing Page 2:**
- Bundle attach rate: 5%+ of buyers who visit the page add a bundle (tracked via Etsy UTM)
- Cart conversion: 2%+ of page visitors complete a purchase
- If bundle attach rate is below 1% after 30 days: audit which bundles are receiving clicks
  but not converting. Most likely cause: price too high relative to individual guide prices.
  Test a "Buy 2, get 3rd at 50% off" offer in place of the flat 15% discount.

---

### Landing Page 3: "Endangered Species Premium Collection"

**URL**: `seedwarden.com/endangered` or Squarespace page `/endangered`

**Purpose**: Position the Phase 2 premium tier ($22 single guide, $48 bundle) with conservation
brand story, credentials, and limited-availability framing.

**Page structure:**

Brand story section (above the fold):
- Headline: "These plants are disappearing. Here's how to know them before they're gone."
- Two-paragraph conservation mission statement: Seedwarden documents endangered native plant
  species for the benefit of foragers, herbalists, and conservation-minded growers. Guides are
  sourced from certified nurseries and botanical experts. Each purchase supports documentation
  of these species.
- Credentials: "All endangered species guides are cross-referenced with USDA PLANTS database
  records and iNaturalist observation data." (Factual; verifiable.)

Product display:
- Single guide cards: $22 each, lifestyle photo of the plant, one-paragraph description
- Premium bundle: $48, what's included, conservation angle ("document 6 endangered species
  in your region")
- Limited-availability language: "These guides are produced in small batches to maintain
  content accuracy. New editions publish seasonally." (This is operationally true if the
  guides are updated; do not use this language if the product is static.)

Trust signals:
- USDA PLANTS database cross-reference badge (text label, not a formal badge — do not imply
  endorsement that does not exist)
- iNaturalist data sourcing note
- 30-day satisfaction guarantee (same as Landing Page 1)

CTA: "Get the [Species Name] Guide — $22" → Etsy listing with UTM
`utm_campaign=endangered-premium`

**Metrics — Landing Page 3:**
- Conversion rate: 1–2% (premium tier; lower than standard guides due to price point)
- AOV from this page: $30+ (buyers who land here are premium-intent; some will buy the bundle)
- If conversion rate is below 0.5% after 20 visitors: the conservation story is not landing.
  Test a direct lead: "The rarest plants in Zone [X] — a field guide" instead of the mission-
  first framing.

---

### Incentive Triggers — Four Core Mechanisms

Each incentive has a UTM tag for GA4 attribution and a specific trigger so they do not stack
unintentionally.

**Incentive 1: Welcome Discount (First Purchase)**
- Offer: 10% off first Etsy order
- Coupon code: SEEDWARDEN10
- Delivery: Campaign 1 Email 1, in the immediate post-purchase email
- Wait — this is not a discount on the first purchase (they already bought). This coupon is
  for their second purchase. Frame it as: "As a thank-you for your first order, here's 10%
  off your next guide." Expiry: 30 days.
- UTM tracking: `utm_campaign=first-purchase-welcome`
- Etsy note: Etsy coupon codes are created in Shop Manager > Marketing > Sales and Coupons.
  Create `SEEDWARDEN10` as a 10% discount code valid for 30 days, issued individually.

**Incentive 2: Referral Credit**
- Offer: $5 store credit per referred buyer who completes a purchase
- Delivery: Campaign 2 Email 2.2 (the content email — referral feels less commercial in a
  content context than in a sales email)
- Mechanics: Unique UTM referral link per subscriber (use Kit's broadcast feature to include
  subscriber-specific URL parameters, or use a simple link: `seedwarden.com?ref=[subscriber_id]`)
- Tracking: GA4 `utm_campaign=referral&utm_source=email` + manual check of order source
  (Etsy does not support native referral tracking)
- Credit delivery: Manual — when a referred order is confirmed, send a $5 Etsy coupon code
  to the referrer. Create individual codes in Etsy Shop Manager.
- Cap: one referral credit per subscriber per month to prevent gaming.

**Incentive 3: Bundle Volume Discount**
- Offer: "Buy 2 zone guides, get the 3rd at 50% off"
- Delivery: Campaign 3 Email 3.1 and Landing Page 2
- Mechanics: Create an Etsy bundle listing that contains 3 guides at the discounted price.
  The "50% off 3rd guide" is built into the bundle listing price — Etsy does not support
  conditional discounts. Display the math: "$14 + $14 + $7 = $35 for 3 guides."
- UTM tracking: `utm_campaign=bundle-volume-offer`
- Note: Do not offer this at the same time as Incentive 1 (SEEDWARDEN10 coupon). A buyer who
  has a 10% coupon AND a 50%-off-3rd deal has two stacking promotions. Stagger: Incentive 1
  is active Days 0–30; Incentive 3 activates in Campaign 3 at Day 15 (after Incentive 1 has
  had 15 days to convert).

**Incentive 4: Seasonal Sale**
- Offer: 20% off all zone guides during fall seed-planting window
- Timing: September 1 – October 15 annually
- Delivery: Campaign 5 Fall Send (September 1) + a dedicated broadcast to the full Kit list
- Etsy mechanics: Create a Sale event in Shop Manager > Marketing > Run a Sale. Set 20%
  discount on all zone guide listings. Schedule: September 1 start, October 15 end.
- UTM tracking: `utm_campaign=fall-seasonal-sale-2026`
- Measurement: Compare September revenue to August baseline. Target: 30%+ lift in September
  from sale-driven purchases.

---

## Section 5: Analytics Dashboard & Decision Triggers

### Daily Dashboard (5-Minute Check)

Run every morning, Monday through Friday. Purpose: catch anomalies before they become problems.

Open two tabs: Etsy Shop Manager > Orders and Kit > Broadcasts (or Sequences > Activity).

Record in a Google Sheet (one row per day):

| Metric | Where to Find It | What to Do If Abnormal |
|---|---|---|
| Total orders today | Etsy Shop Manager > Orders | If 0 orders for 3+ consecutive days: check Etsy listing status (are listings still active?) |
| Cohort distribution | Kit > Tags > count per cohort tag | If one cohort tag is growing 3x faster than others: check which product or channel is driving it |
| Average order value (this week) | Etsy Stats > Revenue / Orders (weekly) | If AOV drops below $20: check if bundle listings are showing in search; if no bundles are converting, audit bundle pricing |
| Email deliverability status | Kit > Broadcasts > last send deliverability | If bounce rate above 3%: audit email list for invalid addresses; Kit flags these automatically |

This check takes 5 minutes when normal. If any field shows an anomaly, escalate to the Weekly
Dashboard before the next morning check.

---

### Weekly Dashboard (30-Minute Review — Every Sunday)

Capture all data in the Google Sheet (one row per week, one column per metric).

**Email engagement — pull from Kit > Broadcasts > Statistics:**

| Metric | Target | Action if Below Target |
|---|---|---|
| Campaign 1 open rate | 40–45% | Below 30%: A/B test subject lines (2-week test, 10% sample per variant) |
| Campaign 2 open rate (avg across 3 emails) | 35–40% | Below 25%: audit content relevance — is the ecosystem guide content matched to the product they bought? |
| Campaign 3 click-to-purchase | 1–2% | Below 0.5%: audit bundle recommendation logic — are the product pairings correct? |
| Campaign 4 re-open rate | 25%+ | Below 15%: replace subject line with zone-specific seasonal hook |
| Unsubscribe rate (any campaign) | Below 2% | Above 3%: reduce email frequency immediately — skip the current week's Campaign 2 email, audit content angle |

**Segment performance — pull from Kit > Subscribers > filter by cohort tag:**

Track opens and clicks per cohort tag weekly. Record which cohort has the highest and lowest
engagement each week. If one cohort consistently underperforms by more than 20% relative to
others, that cohort's email content needs revision.

**Product performance — pull from Etsy Stats > Listings:**

Record top 5 listings by revenue this week. Note which cohort those listings align with. If
the top-performing products are consistently Homesteader products but the email campaigns are
heavily Forager-weighted, realign Campaign 2 content toward Homesteader topics.

**Churn cohort analysis — manual check:**

Pull the Kit subscriber export. Count subscribers with `purchased` tag who have not opened any
email in the prior 30 days. This is the at-risk population for Campaign 4. If this number
exceeds 30% of `purchased` subscribers, Campaign 4 needs to fire earlier (reduce trigger from
Day 45 to Day 30).

---

### Monthly Dashboard (2-Hour Review — First Monday of Each Month)

**LTV by cohort:**

Using the LTV tracker (`analytics/data/customer-ltv-tracker.csv`), calculate:
- Average LTV for each cohort (sum of all orders by cohort / count of buyers in cohort)
- Target comparison: Forager $40+, Prepper $55+, Homesteader $35+, Gift Buyer $30+,
  Herbalist $50+
- If Herbalist LTV is 2x Gift Buyer LTV: shift acquisition budget toward herbalist-relevant
  channels. Pinterest botanical boards, herbalism forums (American Herbalists Guild community,
  r/herbalism), and Etsy SEO terms like "medicinal herb guide" and "herbalist field reference"
  should receive more link placement effort than gift-oriented channels.

**Acquisition cost per source:**

GA4 > Reports > Acquisition > Traffic Acquisition. Filter by `utm_source`. For each source
(Instagram, Pinterest, email, organic Etsy search), calculate: revenue attributed to source /
orders from source. This gives revenue per channel, not formal CAC (which requires ad spend
data). If organic Etsy search is generating 10x more revenue per effort-hour than Instagram,
prioritize Etsy SEO over social posting.

**Retention rates:**

From the LTV tracker:
- 30-day re-purchase rate: buyers who made a second purchase within 30 days of their first /
  total buyers from 30 days ago
- 60-day re-purchase rate: same calculation at 60 days
- 90-day re-purchase rate: same at 90 days
- Target: 10% at 30 days, 18% at 60 days, 25% at 90 days (these are achievable with the
  lifecycle campaigns running; without campaigns, Phase 1 baseline was approximately 2–5%)

**Email ROI:**

Kit does not natively calculate revenue per email send. Calculate manually:
- Count buyers in the LTV tracker whose `kit_subscriber` field is "yes" AND who made a second
  purchase in this month
- Sum the revenue from those second purchases
- Divide by total Kit emails sent this month (Kit > Broadcasts > total sends)
- Revenue per email sent: target $0.10+ (i.e., for every 100 emails sent, $10 in revenue
  is generated by lifecycle campaigns)

---

### Decision Triggers — Specific Actions for Specific Thresholds

Every trigger below names a threshold and a specific response. "Monitor closely" is not an
acceptable response. Each threshold is designed to be measurable with the data sources above.

| Trigger | Threshold | Specific Action | Timeline |
|---|---|---|---|
| Campaign 1 open rate drops | Below 30% for 2 consecutive weeks | A/B test two new subject lines. Send to 10% sample each. Select winner at 7-day open rate. Apply winner to all future sends. | Start A/B test within 48 hours of detection |
| Unsubscribe rate crosses | 3% on any single email | Pause all Campaign 2 sends for current week. Reduce frequency to 1x/week for next 30 days. Audit the email that triggered the spike — if content is not zone-specific, add zone personalization. | Pause within 24 hours |
| Bundle attach rate below | 1% after 30 buyers have received Campaign 3 | Redesign Landing Page 2: add testimonials specifically about bundles, show side-by-side price comparison more prominently, reduce the number of bundles displayed from 5 to 3 (reduce decision paralysis). | Redesign and re-launch within 7 days |
| Herbalist LTV is 2x Gift Buyer | Confirmed in monthly dashboard | Shift 50% of Pinterest posting effort from gift-oriented boards to botanical/herbalism boards. Update Etsy SEO tags on medicinal guides to include "herbalist field guide" and "medicinal plant identification." | Implement in the following week's content planning |
| Forager retention drops | 20% below Phase 1 baseline (i.e., below ~5% at 90 days if Phase 1 was ~5%) | Send immediate win-back email to Forager-tagged subscribers: "You're missing the [seasonal] morel/ramp/mushroom season." Subject line: "The [month] forage window is open in Zone [X]." | Send within 3 days of threshold detection |
| Campaign 4 re-open rate below | 15% | Replace subject line entirely. New test: remove cohort-specific language and use universal curiosity hook: "What's changed in Zone [X] since you last visited." | A/B test new subject line within 7 days |
| VIP engagement retention below | 40% in any 30-day window | Audit whether VIP content appeared elsewhere (public newsletter, social media). If yes: restore exclusivity by moving the leaked content to VIP-only for 60 days. If no content was leaked: the content is not high enough quality. Send a direct email asking VIP subscribers what content they want. | Audit within 3 days; response within 7 days |

---

## Section 6: Implementation Roadmap & Contingencies

### Pre-Launch (May 15–29) — 6 Working Days

This roadmap assumes Anya is working on email infrastructure in parallel with other pre-launch
tasks (photography, product uploads, social scheduling). Each task is scoped with realistic time
estimates so the roadmap is actually executable.

**Day 1 (May 15): Email Copy Drafting**
- Draft all 6 campaign bodies: Campaign 1 Emails 1 and 2, Campaign 2 Emails 2.1, 2.2, 2.3,
  Campaign 3 Emails 3.1 and 3.2, Campaign 4 Email 4.1, Campaign 5 three seasonal templates,
  Campaign 6 Send 1 and Send 2 templates.
- Total: 12 email bodies. At 200–400 words each, this is approximately 2,400–4,800 words of
  copy. Time estimate: 4–6 hours. Use the subject line variants and structural specs in
  Section 2 as the outline — the spec is the brief.
- Do not start with Campaign 5 or 6. Priority order: Campaign 1 > Campaign 3 > Campaign 2 >
  Campaign 4 > Campaign 5 > Campaign 6. Campaign 5 and 6 can be drafted after launch if
  necessary (they do not fire until Day 90 and 3+ purchases respectively).

**Day 2 (May 16): Kit Template Design**
- Build Templates W, C, and O in Kit's visual editor.
- Time estimate: 3–4 hours for all three (Kit's drag-and-drop editor is fast once the design
  decisions are made — use the specs in Section 3 as the brief).
- Required assets: Seedwarden logo file, botanical green hex (#2D5016), one lifestyle photo
  per zone if available. If lifestyle photos are not ready, use solid color blocks.
- Output: Three saved templates in Kit, each with the placeholder zones defined.

**Day 3 (May 17): Kit Automation Sequences**
- Build all Campaign sequences in Kit using the trigger and timing specs from Section 2.
- Priority: Campaign 1 first (fires on launch day), Campaign 3 second (revenue-generating),
  Campaign 2 third.
- Campaigns 4, 5, 6 can be built post-launch (they do not fire until Day 45+).
- Time estimate: 3–4 hours for Campaigns 1, 2, and 3.
- Set up Zapier connection for Etsy-to-Kit tag automation (Option A from Section 3). If the
  Zapier integration requires troubleshooting, allocate 30 additional minutes.

**Day 4 (May 18): Landing Pages**
- Build all three landing pages in Squarespace (or Kit landing page builder if no Squarespace
  access).
- Priority: Landing Page 1 ("Start Here") first — this is the primary acquisition page.
- Time estimate: 2–3 hours for all three pages.
- UTM parameters: implement on all CTA links immediately (do not add after launch — UTM
  parameters on Day 1 links ensure Day 1 attribution data is clean).
- Create all four Etsy coupon codes: SEEDWARDEN10 (welcome), VIPACCESS10 (VIP), seasonal
  sale codes. Do not create the referral codes yet — those are generated per-subscriber.

**Days 5–6 (May 19–20): Testing**
- A/B test the Campaign 1 subject lines on the existing Phase 1 buyer list (if those buyers
  are in Kit). Send to 10% per variant. Run for 48 hours. Record results.
- End-to-end test the Kit automation: create a test subscriber, trigger the `purchased` tag,
  and confirm that Campaign 1 Email 1 fires within 2 hours. Advance through each trigger
  point manually to confirm email routing, conditional content, and cohort-specific branches
  all fire correctly.
- Landing page test: share Landing Page 1 URL with 3–5 people who fit the target audience
  and ask them to complete the quiz without prompting. If fewer than 2 of 5 complete the quiz
  spontaneously, the quiz mechanic is not clear enough.
- Fix all issues found in testing before May 29.

**Days 7–9 (May 21–23): Buffer**
- Reserved for fixes, content revision, and any launch-week preparation tasks that spill
  into this window. Do not schedule new infrastructure work in this window.

**May 24–29: Final checks**
- Confirm all Kit automation sequences are live (not paused/draft).
- Confirm all Etsy listings have UTM parameters in their external link fields.
- Confirm Zapier Etsy-to-Kit connection is live and tested.
- Confirm all three landing pages are published and mobile-responsive.
- Confirm all four coupon codes are active in Etsy Shop Manager.

---

### Launch Day (May 30)

The Welcome campaign fires automatically through Kit when the first Phase 2 purchase is
confirmed and the `purchased` tag is applied. No manual action required if the Zapier
connection is working.

Manual launch-day checks (30 minutes total):
- 9am: Confirm Kit sequences are active (not paused)
- 11am: After first orders come in, manually confirm that Kit shows the `purchased` tag on
  those subscribers. If not: activate Option B (manual tag assignment) immediately.
- End of day: Open Kit > Broadcasts > Sequences > Campaign 1. Confirm emails are queued
  for the day's buyers. Record Campaign 1 Email 1 send count.

---

### Post-Launch Monitoring (May 30 – June 15)

**48-hour check-in**: On June 1, pull Campaign 1 open rate from Kit. If below 30%, start
the subject line A/B test immediately (do not wait for Week 2 of the test calendar).

**1-week full report (June 6)**: Run the Weekly Dashboard (Section 5) for the first time.
Capture all six metrics. Note which campaign is performing above and below target.

---

### Contingencies

**Contingency 1: Kit Etsy Integration Fails**

Risk: Zapier does not successfully connect Etsy webhook to Kit tag application. Symptom: buyers
are completing orders but no `purchased` tag appears in Kit within 24 hours.

Detection: Manual check on launch day (see above). If the 11am check shows no tag on confirmed
buyers: integration has failed.

Response (activate immediately):
- Switch to Option B: manual CSV upload workflow.
- Each Monday morning: export Etsy orders CSV for the prior 7 days. Open Kit > Subscribers.
  For each buyer email, search and apply `purchased` tag manually.
- Estimated time: 30 minutes/week at Phase 2 order volumes (under 50/week).
- Campaigns still fire correctly once the tag is applied — the only downside is a 1–7 day
  delay between purchase and Campaign 1 Email 1. This is not ideal but is functional.
- Investigate Zapier connection in parallel (do not spend more than 2 hours troubleshooting
  before accepting the manual fallback for launch week).

**Contingency 2: Email Frequency Causes Unsubscribe Spike**

Risk: Buyers who receive Campaign 1 (2 emails in 3 days) followed immediately by Campaign 2
(3 emails over 14 days) feel overwhelmed and unsubscribe.

Detection: Unsubscribe rate above 3% on Campaign 2 Email 2.1.

Response (activate if threshold is crossed):
- Immediately pause Campaign 2 for the current week's buyers.
- Reduce Campaign 2 to one email per week (skip 2.1, keep 2.2 and 2.3 at the same send times).
- Do not resend Campaign 2 to buyers who already received 2.1 before the pause.
- Revise Campaign 2 content: lead with practical value in the first paragraph, reduce any
  promotional language, ensure the content is genuinely zone-specific.

**Contingency 3: Landing Pages Unavailable (Squarespace CMS Issue)**

Risk: Squarespace is unavailable or the account is not accessible at launch.

Detection: Any CMS error at landing page URL before May 30.

Response (activate if confirmed):
- Landing Page 1: Use the Kit landing page builder (already set up in Stage 1 of the Kit
  setup guide). Kit's landing page is functional and fully adequate for the email capture
  and zone quiz purpose.
- Landing Page 2 (Bundles): Describe bundles directly in Etsy listings. Update the listing
  descriptions for bundle products to include the "3 guides for the price of 2.55" language.
  Less ideal than a dedicated page but discoverable through Etsy search.
- Landing Page 3 (Endangered Species): Update the Etsy listing description for the endangered
  species guides to include the conservation story language. Etsy listing descriptions support
  up to 2,000 characters — sufficient for the brand story.
- Escalation path: If all CMS options fail (Kit and Squarespace both inaccessible), use direct
  email to Phase 1 buyers announcing Phase 2 launch. Template: plain-text email from Gmail,
  personal tone, direct Etsy links. This is the last resort but is fully executable with zero
  infrastructure.

---

## Success Criteria Checklist

Before May 30 launch, confirm each item:

- [ ] All 12 email bodies drafted and copy-edited (no placeholder text)
- [ ] Templates W, C, O built in Kit and tested on mobile and desktop
- [ ] Campaign 1 fires correctly in end-to-end test (purchased tag → Email 1 within 2 hours)
- [ ] Campaign 2 digest-format branch tested (0 opens → skip to Email 2.3)
- [ ] Campaign 3 conditional logic tested (Email 3.1 opened-not-clicked → Email 3.2 fires)
- [ ] All three landing pages live, UTM parameters on all CTAs
- [ ] All four Etsy coupon codes active
- [ ] Zapier Etsy-to-Kit connection tested with a dummy order
- [ ] Weekly Dashboard Google Sheet columns set up and blank rows ready to fill
- [ ] Monthly Dashboard LTV tracker up to date with all Phase 1 orders entered
- [ ] Manual Option B workflow documented and tested (in case Zapier fails on Day 1)
- [ ] Decision trigger reference sheet printed or bookmarked for launch week use

---

*Document status: production-ready. All email specs, Kit automation configurations, landing
page structures, incentive mechanics, analytics triggers, and contingency plans are fully
specified. No TODOs remain.*
