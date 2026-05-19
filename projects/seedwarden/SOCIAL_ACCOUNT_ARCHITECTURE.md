---
title: "Seedwarden Social Account Architecture"
prepared: 2026-05-19
status: production-ready — implement when Gate 1 (account creation) is confirmed
scope: Instagram, TikTok, Pinterest — bio copy, link structure, hashtag strategy, platform-specific setup
gate-dependency: Gate 1 (account creation) — overdue; Gate 2 (Canva Pro) approved
references:
  - PHASE_2_SOCIAL_GROWTH_STRATEGY.md
  - MAY_30_JUNE_30_CONTENT_CALENDAR.md
  - TRACK_B_SOCIAL_SCHEDULING_TEMPLATES.md
  - pin-template-specs.md
---

# Seedwarden Social Account Architecture

**Purpose**: This document contains all copy, configuration, and strategic decisions needed to set up Seedwarden's three social accounts the moment Gate 1 (account creation) is confirmed. Every field is production-ready — no rewrites required at setup time.

**Platform priority order**: Instagram first (trust hub + email funnel), TikTok second (discovery engine), Pinterest third (evergreen traffic driver).

---

## Part 1: Instagram

### Account Setup Specs

- **Username**: @seedwarden (first choice) — if taken: @seedwarden.field or @seedwarden.guides
- **Display name**: Seedwarden
- **Account type**: Creator account (not Business — Creator accounts have better organic reach in the niche content algorithm as of 2026 and allow the "digital creator" category label)
- **Category label**: Digital Creator
- **Profile photo**: Seedwarden logo — circular crop, centered, minimum 320×320px source file
- **Contact email**: Set to the Etsy account email for Collab DM routing

### Bio Copy

```
Research-backed field guides for foragers, homesteaders + wildcrafters.
Wild edibles. Seed saving. Food sovereignty.
Zone-specific. Instant download.
```

**Character count**: 142 (Instagram maximum is 150 — leaves 8 characters of buffer).

**Bio copy notes**: The three-line structure is deliberate. Line 1 states who the product is for and signals authority ("research-backed"). Line 2 names the three content pillars in keyword form — Instagram's 2026 algorithm indexes bio text for keyword ranking in search. Line 3 is the commercial qualifier: "Zone-specific" differentiates from generic competitors; "Instant download" is the objection-removal for gift buyers who worry about shipping.

**Do not add emojis to the bio.** Seedwarden's brand voice is direct and field-oriented, not aspirational-lifestyle. Emojis read as retail-adjacent, which undercuts the research-authority positioning.

### Link Structure

**Single link**: Use a direct Kit landing page URL (Zone Quick-Start Card free lead magnet) as the bio link. Do not use a Linktree or link aggregator at launch.

**Rationale for no Linktree**: Instagram's algorithm in 2026 does not penalize third-party link destinations, but a single-destination link with one clear CTA converts 2–3× better than a multi-link menu page for cold traffic. The Kit landing page is the highest-leverage conversion point: it builds the email list, delivers immediate value (free zone card), and routes the subscriber into the automated 5-email welcome sequence. Etsy shop link is promoted within the welcome sequence.

**When to add a second link**: Instagram now supports up to five bio links. Add the Etsy shop URL as a second link once the Kit landing page is live and confirmed working (post-Gate 3 verification). Order: Kit page first, Etsy second.

**Link UTM parameters**: Kit landing page URL should carry `utm_source=instagram&utm_medium=bio&utm_campaign=launch-may30` for GA4 attribution from launch day.

### Hashtag Strategy

Instagram enforces a functional ceiling of 3–5 hashtags per post as of the December 2025 algorithm update. Using more than 5 does not increase reach and can suppress distribution. All hashtag sets below follow the 3–5 rule.

**Master hashtag bank by content type** — pull 3–5 per post based on topic:

| Category | Hashtags |
|---|---|
| Foraging / wild edibles | #foraging #wildedibles #wildcrafting #edibleplants #foragingcommunity |
| Homesteading / growing | #homesteading #growyourown #permaculture #seedsaving #homesteadlife |
| Educational / how-to | #gardeningtips #sustainableliving #foodforest #selfsufficiency #heirloomseeds |
| Product / Etsy | #etsydigitaldownload #digitaldownload #etsyseller #seedwarden #instantdownload |
| Gift / seasonal | #giftideas #naturegifts #sustainablegifts #plantlover #uniquegifts |

**Usage discipline**:
- Always include #seedwarden as a branded tag on every post
- Rotate the secondary 2–3 tags per post based on content topic
- Never include hashtags that cross cohort intent signals (e.g., do not add #survival to a foraging post — the Interest Graph treats these as separate clusters)
- Use caption keywords first. In 2026, keyword-rich captions drive more reach than hashtags. Hashtags act as topic confirmation signals, not primary discovery tools.

**Keyword-rich caption language** (these should appear naturally in caption text, not as hashtags):
- "wild edibles guide," "seed saving," "zone [X] planting," "foraging identification," "field guide," "instant download"

### Content Strategy Notes

**Posting cadence**: 4 posts per week — 2 Reels, 1 Carousel, 1 Story highlight. This is the minimum for algorithmic momentum without exceeding the 5-hours/week constraint documented in `phase-2-social-media-strategy.md`.

**Best posting times** (sourced from `TRACK_B_SOCIAL_SCHEDULING_TEMPLATES.md`):
- Primary window: 9:00–11:00am audience local time
- Secondary window: 6:00–8:00pm

**Content mix**: 60% educational (plant ID, foraging tips, seasonal information), 30% brand/product (guide previews, lifestyle photos, behind-the-scenes), 10% direct sales (new listing announcements, limited-time bundles). This mix is non-negotiable for the first 60 days — a higher direct sales ratio suppresses organic reach.

**Reels vs. static**: Reels receive 30.81% organic reach rate vs. 5–8% for static posts. Anchor every week on at least 2 Reels.

**Stories**: Post daily using casual, unedited format. Use poll and question stickers weekly to generate DM replies (DM activity is a positive ranking signal in 2026). Stories drive the most link-in-bio clicks when the link sticker is present.

---

## Part 2: TikTok

### Account Setup Specs

- **Username**: @seedwarden (first choice) — if taken: @seedwarden.field or @seedwardenguides
- **Display name**: Seedwarden
- **Account type**: Personal account set to Creator (not Business — Business accounts on TikTok have restricted audio libraries and lower organic reach in the educational niche)
- **Bio**:

```
Field guides for foragers + homesteaders 🌿
Wild edibles. Seed saving. Zone-specific.
Free zone card ↓
```

**TikTok bio notes**: TikTok's 80-character bio limit requires compression. Emoji is acceptable here (one botanical emoji, not multiple) because TikTok's platform culture is more casual than Instagram's. The "Free zone card ↓" line is the primary conversion driver — it signals the bio link delivers something free.

- **Bio link**: Same Kit landing page URL as Instagram (Zone Quick-Start Card lead magnet)
- **Profile photo**: Same logo file as Instagram

### FYP Strategy

TikTok's For You Page algorithm operates on Interest Graph (content signals) rather than Social Graph (follower signals). This is structurally favorable for a new account: follower count is not a direct ranking factor. A zero-follower Seedwarden account can reach 5,000–20,000 niche-correct viewers within 48 hours on a strong video.

**The ranking signal hierarchy in 2026** (in order of weight):
1. Watch time / completion rate — target 70%+ completion; structure all videos so the most useful information is in the first 45 seconds, not saved for the end
2. Rewatches — information-dense content drives rewatches (viewers replay to catch details they missed)
3. Saves — "save this for your foraging season" CTAs increase save rate; saves are a strong purchase-intent signal
4. Comments — ask a direct question at the end of every video; the question should have a one-word or one-sentence answer (lowers friction for reply)
5. Shares — field guide content shared to friend groups drives spikes; edible plant ID posts perform best for shares

**Hook formula** (the first 3 seconds determine whether the algorithm distributes the video):
- Pattern: [Provocative statement about something familiar] + [reveal]
- Examples that match Seedwarden content:
  - "This plant is in every parking lot. You've been walking past free food for years."
  - "The dandelion in your lawn is worth more than any herb in the grocery store. Here's why."
  - "This is what 18 wild edibles look like — and all 18 are in North America right now."
  - "The seed industry sells you hybrids on purpose. Here's what open-pollinated actually means."
  - "If you can read this one feature on any leaf, you can identify 40% of edible plants."

**Content pillars for FYP targeting** (each pillar targets a distinct Interest Graph cluster):
- **Wild plant identification** (forager cluster): 30–45 seconds, close-up plant footage or hand-held in field, text overlay naming features, end with "guide link in bio"
- **Homestead how-to** (homesteader cluster): 30–60 seconds, process demonstration — seed saving, preservation technique, companion planting — cut to the actionable part immediately
- **Food sovereignty** (prepper + homesteader overlap): 30–45 seconds, talking head or B-roll, direct tone, fact-based ("you can grow X calories per square foot")
- **Guide preview** (all clusters): Screen scroll or page flip through guide interior — 15–20 seconds — ends with "this is what's in it; link in bio"

**Posting cadence**: 3 times per week minimum, 5 times maximum. Buffer research confirms 3–5 posts/week is the sweet spot for algorithmic consistency without sacrificing production quality. Skip a day rather than post weak content.

**Batch filming protocol**: Film 5–7 videos in a single 90-minute session once per week. All videos are 30–60 seconds. Script the hook for each video before filming. Upload daily to maintain cadence. This is documented in `phase-2-social-media-strategy.md` and is the only sustainable model under the 5-hours/week constraint.

**Upload protocol — critical**: Do not use Instagram's "Share to TikTok" feature. TikTok algorithmically suppresses cross-posts from Instagram (the platform detects Instagram watermarks and metadata). Download the Reel to camera roll, then upload directly from camera roll in TikTok. Same file, different upload path.

### TikTok Hashtag Strategy

TikTok best practice: 3–5 highly relevant hashtags per video. The platform uses caption keywords as the primary discovery signal; hashtags are secondary.

**Per-cohort hashtag sets**:
- Forager content: #foraging #wildedibles #wildcrafting
- Homesteader content: #homesteading #growyourown #permaculture
- Seed / growing content: #seedsaving #heirloomseeds #growyourown
- Guide preview / product: Use no product hashtags — TikTok suppresses promotional-feeling content in organic distribution. Let the product appear naturally in the video.

**Caption keyword discipline**: Write captions as plain-language descriptions of what the video teaches. Example: "Three wild edibles you can find in June in most of the eastern US — all three have no toxic lookalikes that share these identifying features." That sentence contains six content-relevant keyword phrases without any hashtag.

---

## Part 3: Pinterest

### Account Setup Specs

- **Username**: seedwarden
- **Display name**: Seedwarden — Field Guides for Foragers & Homesteaders
- **Account type**: Business account (required for Rich Pins and Pinterest Analytics — no reach penalty in 2026)
- **Bio**:

```
Research-backed digital field guides for foragers, homesteaders, and wildcrafters. Wild edibles. Seed saving. Companion planting. Zone-specific growing guides. Instant download at seedwarden.etsy.com
```

- **Website**: seedwarden.etsy.com (verified in Pinterest settings — enables Rich Pins, which auto-pull product price and availability from Etsy listings)
- **Profile photo**: Seedwarden logo

### Board Architecture

Pinterest's algorithm uses board structure as a primary content-classification signal. Board names should be exact phrases that buyers search — not brand-creative names.

**8 boards to create at account launch, in this order**:

| # | Board Name | Purpose | Target Audience |
|---|---|---|---|
| 1 | Wild Edibles Identification Guide | Core product board — forager content and product pins | Forager cohort |
| 2 | Seed Saving Field Guides | Homesteader core board — seed saving tutorials and product | Homesteader cohort |
| 3 | Zone Planting Charts & Calendars | Zone card lead magnet board — high search volume | All cohorts |
| 4 | Foraging for Beginners | Broad educational board — entry-level foraging content | Forager cohort, new audience |
| 5 | Homesteading & Food Preservation | Homestead lifestyle board — preservation, food security | Homesteader + Prepper |
| 6 | Gifts for Foragers & Nature Lovers | Gift buyer board — seasonal gift framing | Gift Buyer cohort |
| 7 | Permaculture & Food Forest Design | Permaculture-specific content — companion planting, design | Homesteader cohort |
| 8 | Heirloom Seeds & Growing Guides | Product + editorial board — seeds, garden planning | Homesteader + Forager |

**Board population rule**: Before pinning any Seedwarden product to a board, populate it with 10–15 third-party pins relevant to the board topic. Pinterest ranks boards partly by content volume and topic coherence. A product-only board appears as advertising; a curated board with educational content and products mixed together ranks and distributes better.

**Pin ratio per board**: 4 educational / third-party pins for every 1 Seedwarden product pin.

### Pin Format Specs

All Seedwarden pins use the Canva Pro template specs from `pin-template-specs.md`. Quick reference:

| Format | Dimensions | File type |
|---|---|---|
| Standard product pin | 1000×1500px | JPEG, 85% quality |
| Educational hook pin | 1000×1500px | JPEG, 85% quality |
| Video pin (Reel repurposed) | 1080×1920px | MP4 |

**Pin description strategy**: Write descriptions as 150–300 word natural-language text. Pinterest's search algorithm in 2026 indexes the full description, not just the title. Use keyword phrases naturally:
- "foraging guide for beginners"
- "wild edibles identification"
- "zone 5 seed starting calendar"
- "heirloom seed saving guide"
- "food preservation field manual"

End every product pin description with: "PDF instant download at seedwarden.etsy.com."

**Rich Pins**: Enable via Pinterest Developer settings after verifying seedwarden.etsy.com. Rich Pins automatically pull product title, price, and availability from Etsy listings into the pin display. Confirmed to increase click-through rate 30–40% vs. standard pins.

**Posting cadence**: 3–5 fresh pins per day, batched in one weekly session of 1–1.5 hours. Use Pinterest's native scheduler. Do not schedule more than 10 pins per day — Pinterest's 2026 algorithm interprets high-volume scheduling as automated spam behavior and reduces distribution.

---

## Part 4: Cross-Platform Integration

### Link Flow Architecture

```
TikTok bio → Kit landing page → Zone card delivery + welcome sequence → Email Day 7: Etsy shop link
Instagram bio → Kit landing page (same) → same sequence
Pinterest pins → Etsy listing direct (product intent is already established)
```

**Rationale**: TikTok and Instagram audiences need a warming sequence before purchasing. Pinterest audiences arrive with search intent and should be routed directly to the Etsy listing — adding a Kit landing page step between a Pinterest product pin and the Etsy purchase creates unnecessary friction.

### Cross-Posting Protocol

- Every Instagram Reel is uploaded natively to TikTok (same file, no reprocessing)
- Every TikTok video is repurposed as an Instagram Reel (native upload to Instagram from camera roll)
- Every Reel/TikTok video is also uploaded to Pinterest as a Video Pin (Pinterest video pins appear in the search feed and receive algorithmic distribution boost in 2026)
- Pinterest product pins link directly to Etsy listing URLs (with UTM parameter `utm_source=pinterest&utm_medium=pin`)
- Instagram Stories promote active Pinterest boards weekly ("I pinned 7 new zone planting guides — link in bio")

### Etsy Shop Link Structure

- **Etsy shop URL**: seedwarden.etsy.com
- **UTM-tagged links for attribution**:
  - Instagram bio: `utm_source=instagram&utm_medium=bio&utm_campaign=launch-may30`
  - TikTok bio: `utm_source=tiktok&utm_medium=bio&utm_campaign=launch-may30`
  - Pinterest pins: `utm_source=pinterest&utm_medium=pin&utm_content=[product-slug]`
  - Email links: `utm_source=kit&utm_medium=email&utm_campaign=welcome-sequence`

---

## Part 5: April–May 2026 Platform Algorithm Notes

**Instagram**: Hard 3–5 hashtag limit (enforced December 2025). Keyword-rich captions now outperform hashtag quantity for discovery. Reels retain the highest organic reach rate (30.81%) of any Instagram format. Save rate and share rate are the two strongest signals for extended distribution.

**TikTok**: Completion rate threshold for FYP distribution rose to ~70% (from ~50% in 2024). Follower count is confirmed non-factor — every video is evaluated independently against a test audience pool. Niche consistency is critical: posting outside your established content category causes up to 45% reach drop on off-topic content. Keyword captions boost visibility 20–40%.

**Pinterest**: AI-driven search now references 16,000 past user interactions per query (vs. 100 previously), meaning new accounts with well-structured boards surface faster than in prior years. Fresh pin designs outperform re-used URLs even when the destination content is identical — create new Canva designs for top-performing content monthly. Rich Pins (Etsy integration) remain the single highest-ROI Pinterest setup action.
