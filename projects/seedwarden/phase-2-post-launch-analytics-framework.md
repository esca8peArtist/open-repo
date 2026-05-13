---
title: "Phase 2 Post-Launch Analytics & Cohort Segmentation Framework"
date: 2026-05-13
status: production-ready — implement before May 20
launch-date: 2026-05-30
analytics-ready-date: 2026-05-20
scope: Endangered species guides; conservation naturalists, herbalists/practitioners, educators/schools
cross-references:
  - phase-2-analytics-strategy.md (data source architecture and GA4 constraints)
  - etsy-ga4-event-tracking.md (GA4 custom event schema and audience definitions)
  - customer-cohort-analysis-framework.md (segment profiles and messaging)
  - phase-2-kit-email-setup.md (Kit tag configuration)
  - analytics/monthly-metrics-checklist.md (monthly operator runbook)
  - endangered-species-candidate-list.md (species and guide inventory)
---

# Phase 2 Post-Launch Analytics & Cohort Segmentation Framework

**Purpose**: Measurement infrastructure for the May 30, 2026 Phase 2 launch of Seedwarden's
endangered species guide series. This document defines what to track, how to segment buyers by
the three Phase 2 cohorts (conservation naturalists, herbalists/practitioners, educators/schools),
which dashboards to maintain, and which specific conditions should trigger a product or channel
pivot decision.

**Who this is for**: One operator. All templates run in Google Sheets plus manual Kit/Etsy CSV
exports. No database or code is required. Every mechanism described here can be fully operational
before May 20, within the 10-day pre-launch testing window.

**Analytics-ready target**: May 20, 2026 (10 days before launch, per implementation timeline
in Part 6). One week of pre-launch testing on live infrastructure before first order arrives.

---

## Part 1: Analytics Architecture

### 1.1 Data Source Overview

Phase 2 draws data from four systems. None of these systems communicate with each other
automatically at Phase 2 scale. The integration layer is a single Google Sheets workbook
maintained manually, with monthly CSV imports from each source.

```
Etsy Shop Manager          Kit (Email Platform)
  Orders, revenue,           Subscriber tags,
  views, CVR, traffic        cohort classifications,
  source, search terms       open/click rates,
        |                    zone distribution
        |                          |
        +----------+  +-----------+
                   |  |
           [Google Sheets Workbook]
            - Daily tab
            - Weekly tab
            - Monthly tab
            - LTV Tracker
            - Cohort Dashboard
                   |
        +----------+----------+
        |                     |
  GA4 (traffic source,   Social Insights
  listing engagement,    (Instagram, Pinterest,
  zone landing page CVR) TikTok — manual monthly)
```

**What each source provides that the others cannot:**

| Source | Unique Data | Collection Method | Cadence |
|---|---|---|---|
| Etsy Shop Manager | Revenue per guide, CVR per listing, Etsy search terms driving views, repeat customer flag | Manual CSV export | Weekly (Sunday) |
| GA4 | Channel breakdown (Pinterest vs. Instagram vs. TikTok vs. email), device type per channel, listing engagement duration, zone landing page conversion | Manual report export | Monthly |
| Kit | Cohort tag distribution, email open/click rates by segment, zone-subscriber mapping, pre-purchase subscriber-to-buyer conversion rate | Manual CSV export | Monthly (first Monday) |
| Social (native analytics) | Follower growth by platform, post reach, profile link clicks (proxy for Etsy referral) | Screenshot / manual | Monthly |

### 1.2 Etsy API Capabilities and Practical Limits

The Etsy Open API v3 provides order data, listing stats, and payment transactions via OAuth 2.0.
Rate limit: 10 requests/second; practical ceiling for a solo operator running automated daily
pulls is well under documented limits.

**Available via Etsy API v3 or dashboard export:**
- Order count and revenue per listing (granularity: per order)
- Views per listing (daily granularity)
- Conversion rate: derived as orders/visits, available at listing level, monthly
- Traffic source breakdown: Etsy organic search, direct, social referral, other (monthly aggregate)
- Geographic distribution: city/state per order
- Repeat customer flag: detectable via email match across order history
- Top 20 search terms driving views to each listing (monthly, not real-time)

**Not available via Etsy API:**
- Individual buyer demographics (age, income, educational background)
- Abandoned cart data in real time
- Which specific endangered species guide titles a visitor browsed before purchasing another
- Individual buyer browsing sessions on Etsy's marketplace

**Recommendation for Phase 2**: Manual CSV exports are sufficient through Month 3 (estimated
order volume: 25–70 orders/month). The Etsy API Python client (documented in
`phase-2-analytics-strategy.md` Section 5.2) becomes worth the setup time when monthly orders
exceed 100 and Sunday manual entry exceeds 45 minutes.

### 1.3 GA4 Zone-Based Segmentation

GA4 fires on Etsy listing pages only — it does not fire on Etsy search results, the Etsy
homepage, or at checkout. The Kit landing page (a Seedwarden-controlled surface) is the only
place where full custom event implementation is possible.

**Zone-specific tracking on the Kit landing page** is the most analytically valuable GA4
implementation for Phase 2. Two events capture the endangered-species-to-zone acquisition funnel:

- `view_zone_card_landing` — fires on page load; parameter: `acquisition_source` (from utm_source)
- `lead_magnet_signup` — fires on form submit; parameters: `acquisition_source`, `inferred_cohort`

The conversion rate between these two events (visits ÷ signups) is the primary pre-purchase
funnel metric for Phase 2. A drop in this rate signals messaging misalignment on the landing page,
not a traffic problem.

**GA4 custom dimensions for endangered species guide tracking** (register in GA4 Admin before
May 20; full schema in `etsy-ga4-event-tracking.md` Section 2):

| Dimension Name | Parameter | Phase 2 Use |
|---|---|---|
| Guide Type | `guide_type` | Distinguishes `endangered_species`, `wild_edibles`, `native_plants`, `medicinal_plants`, `complete_bundle` |
| Acquisition Source | `acquisition_source` | Attributes channel: `pinterest`, `instagram`, `tiktok`, `kit`, `etsy_organic`, `direct` |
| Customer Cohort (inferred) | `inferred_cohort` | `conservation_naturalist`, `herbalist_practitioner`, `educator_school`, `unknown` |
| Season | `visit_season` | `spring_planting`, `preservation`, `holiday_gift`, `academic_fall` |
| Listing Slug | `listing_slug` | Per-guide identifier matching Etsy URL slug |
| Return Visitor | `is_return_visitor` | `true`/`false` — identifies research-mode repeat visitors |

**UTM parameter convention (apply to every outbound link before May 30):**

| Source | UTM Template |
|---|---|
| Instagram bio link | `?utm_source=instagram&utm_medium=social&utm_campaign=phase2_launch` |
| TikTok bio link | `?utm_source=tiktok&utm_medium=social&utm_campaign=phase2_launch` |
| Pinterest pin (conservation content) | `?utm_source=pinterest&utm_medium=pin&utm_campaign=conservation-[species-slug]` |
| Email broadcast | `?utm_source=kit&utm_medium=email&utm_campaign=[email-name]` |
| Etsy listing footer CTA | `?utm_source=etsy_listing&utm_medium=product&utm_campaign=kit_signup` |

All links must carry UTM parameters from Day 1. Without them, GA4 classifies traffic as direct
and channel attribution is unresolvable.

### 1.4 Kit Cohort Export Process

Kit's free tier provides CSV export only (no public API). All Kit data collection is via manual
export.

**Phase 2 cohort tags to activate in Kit before May 20:**

Zone tags (active from Phase 1): `zone-3` through `zone-10`
Phase 2 cohort tags (new): `Cohort_ConservationNaturalist`, `Cohort_HerbalistPractitioner`,
`Cohort_EducatorSchool`
Behavioral tags (carried forward): `seed-saver`, `preservationist`, `city-grower`
Lifecycle tags: `new-subscriber`, `purchased`, `vip` (2+ purchases), `phase2-buyer`

**Cohort tag assignment logic:**
1. Post-purchase survey (Day 1 order confirmation email) — explicit self-identification
2. Product purchased — inference if survey not completed: endangered species medicinal guide →
   `Cohort_HerbalistPractitioner`; endangered species educational series →
   `Cohort_EducatorSchool`; single species conservation guide → `Cohort_ConservationNaturalist`
3. Email click behavior — Email 3 and Email 4 conservation ethics links tag
   `Cohort_ConservationNaturalist`; harvesting/preparation links tag `Cohort_HerbalistPractitioner`

**Monthly Kit export workflow (30 minutes, first Monday of each month):**
1. Kit > Subscribers > Export > All subscribers > CSV
   Save as `analytics/data/kit_subscribers_YYYY-MM.csv`
2. In Google Sheets, count subscribers per Phase 2 cohort tag using COUNTIF on the tags column
3. Average open rate per cohort by filtering tags and using AVERAGEIF
4. Count subscribers with `purchased` tag vs. total to get email-to-buyer conversion rate
5. Record all values in Monthly Data Log tab

### 1.5 Social Channel Attribution

Social platforms are acquisition channels, not analytics platforms. Track their contribution
via downstream signals: Kit sign-up spikes and Etsy traffic source shifts that correlate with
post timing.

**Monthly social metrics to record manually:**

| Platform | Metric | Tool | What It Signals |
|---|---|---|---|
| Pinterest | Monthly views, profile link clicks | Pinterest Analytics | Content discovery volume for conservation topics |
| Instagram | Follower count, bio link clicks (Linktree/direct) | Instagram Insights | Engaged audience size; direct Etsy/Kit referrals |
| TikTok | Follower count, profile link clicks | TikTok Analytics | Reach with younger conservation audience |

**Cross-reference method**: When Kit sign-ups spike or Etsy traffic shows a social referral
increase, check which post went out within 24–48 hours. Log the content type and channel in the
Weekly dashboard. This is the primary signal for which social content format drives buyers vs.
which drives list growth (they are often different — educational conservation content builds
the list; urgency or rarity-focused content drives direct Etsy purchases).

---

## Part 2: Cohort Segmentation Framework

### 2.1 The Three Phase 2 Buyer Segments

Phase 2 introduces three new primary cohorts, replacing the Phase 1 framing (forager/prepper/
homesteader/gift buyer). The Phase 1 cohort definitions remain active in Kit and the LTV tracker
— Phase 2 buyers get both their new cohort tag and their most likely Phase 1 analog for
continuity in existing automations.

---

**Cohort A: Conservation-Focused Naturalist**
Expected share of Phase 2 buyers: 35–45%

*Profile*: Buys guides to understand at-risk species ecology, identify plants in the field,
and support conservation outcomes. Likely a member of a native plant society, iNaturalist
contributor, or active in local land stewardship. Education level: college or graduate degree.
Geographic concentration: Pacific Northwest, New England, Upper Midwest.

*Purchase signals*:
- First purchase: single endangered species guide for a specific species with strong regional
  story (American Ginseng in Appalachia, Goldenseal in the Southeast, Trillium in the PNW)
- Session behavior: GA4 session duration >150 seconds on endangered species listing pages;
  reading the full species conservation status section
- AOV: $18–$35 single guide or two-guide pair; does not bulk-buy initially
- Repeat pattern: 2–4 purchases over 6–12 months as they encounter different species
- Email behavior: high open rate on conservation ethics content; clicks species identification
  links; subscribes to the iNaturalist-linked newsletter sections

*Pre-launch hypothesis to validate*: This cohort will be the most likely to share guide links
in online naturalist communities (iNaturalist forums, local native plant society email lists).
If referral traffic from these communities appears in GA4 within 30 days, organic amplification
is working and Pinterest/Instagram efforts should lean into conservation ethics framing over
the plant identification framing.

*Phase 1 analog*: Closest match to the High-Intent Forager cohort tag in existing Kit
automations. Assign `Cohort_ConservationNaturalist` as primary tag; retain `Cohort_Forager`
as secondary for continuity in Phase 1 email sequences.

---

**Cohort B: Herbalists / Practitioners**
Expected share of Phase 2 buyers: 30–40%

*Profile*: Buys guides primarily for the medicinal and practical use information: harvesting
windows, preparation methods, conservation-compliant sourcing, legal alternatives to wild-
harvesting. Includes clinical herbalists, amateur herbalists, and buyers researching personal
medicine alternatives. Purchasing behavior is seasonal, tied to harvesting seasons
(spring/early summer for above-ground herbs; fall for roots).

*Purchase signals*:
- First purchase: medicinal-angle endangered species guides (American Ginseng, Goldenseal,
  Black Cohosh, Bloodroot — the CITES-regulated or UpS At-Risk species with strongest
  herbal practitioner demand)
- Bundle behavior: more likely than conservation naturalists to bundle two or three
  related species (e.g., "the three forest medicinals" — ginseng, goldenseal, black cohosh)
- AOV: $22–$48; medium bundle affinity
- Seasonal peaks: April–May (spring root harvest window) and September–October (fall root
  harvest, preservation prep)
- Email behavior: high click rate on harvesting windows and preparation sections; responds
  to seasonal timing content ("Goldenseal root harvest window opens in 3 weeks")

*Pre-launch hypothesis to validate*: Herbalist cohort will show stronger seasonal revenue
concentration than conservation naturalists. If herbalist-linked purchases (medicinal-angle
guides) represent more than 50% of May 30–June 30 revenue, the summer content calendar
should run a harvesting-windows campaign in August to capture late-summer herbalist demand
before the fall root harvest window.

*Phase 1 analog*: Closest match to Homesteader cohort. Assign `Cohort_HerbalistPractitioner`
as primary; retain `Cohort_Homesteader` as secondary.

---

**Cohort C: Educators / Schools**
Expected share of Phase 2 buyers: 15–25%

*Profile*: Institutional and semi-institutional buyers: K–12 science teachers, community
college instructors, nature center educators, botanical garden education staff, homeschool
co-ops. Purchases are bulk or multi-copy; payment often through institutional procurement
or personal card with reimbursement intent. Buying decisions align with academic calendar
(August–September back-to-school procurement, January curriculum refreshes, May end-of-year
special purchases).

*Purchase signals*:
- Order quantity: 3+ copies of the same guide in a single transaction
- Institutional email domains: `.edu`, `.k12`, `.gov`, or recognizable school district
  domains in the Etsy buyer email (visible in order export)
- Messaging: Etsy conversation messages from buyers asking about bulk discount, curriculum
  alignment, or whether guides are available in a non-PDF format
- AOV: $45–$120 (multi-copy purchases)
- Repeat pattern: strongly seasonal — concentrated in August–September and January

*Pre-launch hypothesis to validate*: The May 30 launch falls near the end of the academic year.
If educator-pattern orders (bulk quantity + institutional email domain) appear in June, this
cohort is shopping for end-of-year curriculum additions. If they are absent in June, do not
interpret this as low demand — the academic calendar means August is the primary acquisition
window and the October–November back-to-school Pinterest campaign targeting educators
should be prepared in advance.

*Phase 1 analog*: No direct match. Assign `Cohort_EducatorSchool` as primary tag only; do
not assign a Phase 1 secondary tag. Route into a separate Kit automation sequence (B2B
educator sequence, not the standard welcome flow) if an educator tag is applied.

---

### 2.2 Cohort Definition Table

| Dimension | Conservation Naturalist | Herbalist / Practitioner | Educator / School |
|---|---|---|---|
| Expected share | 35–45% | 30–40% | 15–25% |
| Primary purchase type | Single endangered species guide | Medicinal-angle guides, 2–3 species bundles | Multi-copy same guide |
| Expected AOV | $18–$35 | $22–$48 | $45–$120 |
| Seasonal peak | Spring (April–June), early fall (Sept) | Spring root harvest (Apr–May), fall root harvest (Sept–Oct) | Academic: Aug–Sept, Jan, May |
| Likely Etsy traffic source | Etsy organic search (species name), iNaturalist referral, Pinterest conservation content | Etsy organic search (herb name), email, Pinterest herbal content | Etsy search, direct (heard from colleague), email |
| Expected repeat rate at 90d | 15–25% | 25–35% | 10–20% (seasonal, not monthly) |
| LTV signal | Multiple single guides over 12 months | Seasonal guide bundles; re-buys updated editions | Annual bulk re-purchase per curriculum cycle |
| Kit tag | `Cohort_ConservationNaturalist` | `Cohort_HerbalistPractitioner` | `Cohort_EducatorSchool` |
| Decision threshold | <15% share at Day 60 → conservation messaging needs amplification | <20% share at Day 60 → harvesting-window content needs more prominence | >25% share in Aug–Sept → prepare bulk pricing tier and educator outreach |

### 2.3 Cohort Inference from Product Purchased

When post-purchase survey is not completed, infer cohort from first purchase:

| Guide Purchased | Primary Inference | Confidence |
|---|---|---|
| American Ginseng conservation guide | Herbalist or Conservation Naturalist (50/50) | Medium — verify via Email 3 click behavior |
| Goldenseal forest-farming guide | Herbalist Practitioner | High |
| Black Cohosh ecological guide | Conservation Naturalist | High |
| Bloodroot or Trillium guide (ornamental/ID emphasis) | Conservation Naturalist | High |
| Any guide purchased in quantity ≥3 | Educator / School | High |
| Complete endangered species series bundle | Educator / School or Conservation Naturalist | Medium |
| Wild edibles + 1 endangered species guide | Conservation Naturalist (crossover buyer) | Medium |

Inference accuracy degrades for single-species guides that appeal to both herbalists and
naturalists (ginseng, black cohosh). For these, use Email 3 behavioral click tracking to
disambiguate: if the subscriber clicks the harvesting preparation link, apply
`Cohort_HerbalistPractitioner`; if they click the conservation status / iNaturalist link,
apply `Cohort_ConservationNaturalist`.

---

## Part 3: Dashboard Specifications

### 3.1 Daily Dashboard

**Purpose**: Anomaly detection only. Not a decision-making session.
**Tool**: Google Sheets "Daily" tab, or Etsy Shop Manager mobile app.
**When**: 8–10am daily for the first 30 days; Monday/Wednesday/Friday after Day 30 once
patterns are established.
**Time required**: 10 minutes.

```
SEEDWARDEN DAILY CHECK — [DATE]
=====================================================
Source: Etsy Shop Manager > Stats (today view)

Orders today:              ___    (7-day avg: ___)
Revenue today:             $___   (7-day avg: $___)
Top guide today:           ___    [species name]
Conversion rate:           ___%   (target: ≥1.5%)

Kit sign-ups today:        ___    (Kit dashboard)
Total Kit subscribers:     ___

Errors:  [ ] Wrong file delivered  [ ] Negative review  [ ] Payment issue
=====================================================
SIGNAL INTERPRETATION:
  Revenue >200% of 7-day avg    → Log corresponding social post; note species/channel
  Revenue <30% of 7-day avg, 3d → Check Etsy search ranking (open listing incognito)
  0 orders + 50+ views today    → Conversion problem; check listing cover image and price
  Kit sign-ups = 0              → Verify Kit landing page is live and UTM links work
```

**What to log**: When a revenue or sign-up spike occurs, record in the Weekly tab: date,
anomaly type, what was posted or sent within 24 hours. This record becomes the channel
attribution intelligence for Phase 3 content planning.

### 3.2 Weekly Dashboard

**Purpose**: Trend identification before problems compound.
**Tool**: Google Sheets "Weekly" tab, populated manually from Etsy Stats and Kit dashboard.
**When**: Sunday evening, every week.
**Time required**: 30 minutes.
**Refresh cadence**: Every 7 days (Sunday), with 4-week rolling view.

```
SEEDWARDEN WEEKLY REVIEW — Week of [DATE]
=====================================================
SECTION 1: SALES VELOCITY

               | This Week | Last Week | 4-Wk Avg  | Trend
Orders         |           |           |           | ↑ ↓ →
Revenue        | $         | $         | $         |
AOV            | $         | $         | $         |
Units sold     |           |           |           |

SECTION 2: ENDANGERED SPECIES GUIDE PERFORMANCE (top 5)

Guide                    | Orders | Revenue | % of Total | vs Last Wk
                         |        | $       |     %      |
                         |        | $       |     %      |
                         |        | $       |     %      |
                         |        | $       |     %      |
                         |        | $       |     %      |
Other guides (all)       |        | $       |     %      |

SECTION 3: COHORT MIX (inferred from products + survey responses)

Cohort                    | % Orders | Avg AOV | Repeat (90d) | Target
Conservation Naturalist   |     %    | $       |      %       | 35–45%
Herbalist / Practitioner  |     %    | $       |      %       | 30–40%
Educator / School         |     %    | $       |      %       | 15–25%
Unknown / Unclassified    |     %    | $       |      —       | <15%

SECTION 4: EMAIL FUNNEL

Kit subscribers (end of week):      ___
New sign-ups this week:             ___
Email 1 open rate (recent cohort):  ___% (target: 45%+)
Email 5 coupon redemptions:         ___
Newsletter open rate (last send):   ___% (target: 28%+)

SECTION 5: CHANNEL PERFORMANCE (Etsy Stats > Traffic Sources)

Channel                  | Sessions  | % of Total
Etsy organic search      |           |
Social referral          |           |
Direct                   |           |
Other                    |           |

=====================================================
WEEKLY QUESTIONS (answer, do not skip):
1. Which guide drove the most growth? → Can it cross-sell with a related endangered species?
2. Which cohort is underrepresented vs. target? → Seasonal or messaging gap?
3. Is AOV trending up (bundling) or flat (single-guide preference)?
4. Did any social post correlate with an Etsy or Kit sign-up spike this week?
```

### 3.3 Monthly Dashboard (Deep Dive)

**Purpose**: Cohort LTV analysis, product classification, seasonal pattern check, Phase 3
readiness scoring.
**Tool**: Google Sheets "Monthly" tab + Kit subscribers CSV + Etsy orders CSV.
**When**: First Monday of each month.
**Time required**: 2 hours.
**Refresh cadence**: Monthly.

```
SEEDWARDEN MONTHLY DEEP DIVE — [MONTH YEAR]
=====================================================
DATA PREP (before starting):
  [ ] Export Etsy Shop Manager > Finances CSV → save as analytics/data/etsy_orders_YYYY-MM.csv
  [ ] Export Kit > Subscribers > CSV → save as analytics/data/kit_subscribers_YYYY-MM.csv
  [ ] Update customer-ltv-tracker.csv with new orders this month

BLOCK 1: REVENUE SUMMARY
  Gross revenue:               $___    MoM change: ___% | vs target ___
  Net revenue:                 $___    (gross × 0.905 − $0.25 × orders)
  Orders:                      ___     MoM: ___%
  Unique buyers:               ___
  AOV:                         $___    target M1: $20–30; M3+: $28–40
  Bundle revenue %:            ___%    target: 15%+ by Month 3
  Phase 1 buyer cross-sells:   ___     (returning buyers from before May 30)

BLOCK 2: COHORT LTV ANALYSIS (from LTV tracker, filtered by cohort_tag)

  Cohort                     | Buyers | Avg LTV | 30d Repeat % | 90d Repeat % | Target 90d
  Conservation Naturalist    |        | $       |      %       |       %      | 15–25%
  Herbalist / Practitioner   |        | $       |      %       |       %      | 25–35%
  Educator / School          |        | $       |      %       |       %      | 10–20%

  Acquisition cost proxy:
    Etsy Ads spend (if running) / new buyers from ads  =  $___/buyer
    Social-only acquisition:  $0 direct cost; estimate 2–3 hours/week content at [hourly rate]

BLOCK 3: ENDANGERED SPECIES GUIDE CLASSIFICATION
  Classification criteria:
    Star     = top 3 by revenue, CVR ≥1.5%, repeat purchases visible
    Workhorse = steady orders, not top 3, consistent month-over-month
    Anchor   = high views, below-average CVR (traffic magnet, conversion problem)
    Dog      = <5 orders, CVR <1% after 30+ days live
    Hidden Gem = few orders but strong reviews or high session duration in GA4

  Guide                   | Orders | Revenue | CVR% | GA4 Duration | Class   | Action
  American Ginseng guide  |        | $       |    % |        sec   |         |
  Goldenseal guide        |        | $       |    % |        sec   |         |
  Black Cohosh guide      |        | $       |    % |        sec   |         |
  [other guides]          |        |         |      |              |         |

BLOCK 4: ZONE-COHORT CORRELATION (from Kit export)
  Top 3 zones by subscriber count:  Zone ___, Zone ___, Zone ___
  Zone-cohort dominant pairs:
    Zone ___  → primary cohort tag: ___  (% of zone subscribers)
    Zone ___  → primary cohort tag: ___
    Zone ___  → primary cohort tag: ___
  Action if actual distribution differs >15 percentage points from Part 2.2 hypothesis:
    → Adjust zone-specific newsletter content for following month

BLOCK 5: SEASONAL PATTERN CHECK
  Month ___ falls in:  [ ] Spring/Harvest  [ ] Academic back-to-school  [ ] Holiday gift
  Expected lift vs. baseline: ___% (herbalist spring: +25–40%; educator Aug: +30–50%)
  Actual vs. expected: above / at / below
  If below expected for a seasonal peak: diagnose (messaging? product? channel not reaching cohort?)

BLOCK 6: EMAIL LIST HEALTH
  Total active subscribers:       ___   M1 target: 50+; M3 target: 200+
  New subscribers this month:     ___
  MoM growth rate:                ___%
  Email 1 open rate:              ___%  target: 45%+  alert: <30%
  Newsletter open rate (avg):     ___%  target: 28%+  alert: <22%
  Newsletter CTR:                 ___%  target: 3%+   alert: <2%
  Monthly unsubscribe rate:       ___%  healthy: <0.5%
  Cohort tag counts:
    ConservationNaturalist: ___ | HerbalistPractitioner: ___ | EducatorSchool: ___ |
    purchased: ___ | vip: ___

BLOCK 7: PHASE 3 READINESS SCORE
  [ ] ≥50 orders in this 30-day period         PASS / FAIL
  [ ] ≥$600 gross revenue in 30 days           PASS / FAIL
  [ ] ≥1 "Star" endangered species guide       PASS / FAIL
  [ ] ≥2 cohorts each >20% of buyers           PASS / FAIL
  [ ] ≥5% repeat purchase rate at 30 days      PASS / FAIL
  [ ] <2% operational error rate               PASS / FAIL

  Phase 3 recommendation:  GO / CONDITIONAL / NO-GO

ACTIONS ARISING:
  Priority 1 (this week):    ___
  Priority 2 (this month):   ___
  Priority 3 (watch/next):   ___
=====================================================
```

---

## Part 4: Decision Trigger Matrix

The following conditions, when met, trigger a defined response. Evaluate each trigger
during the Sunday weekly review. Starred triggers (*) are also evaluated daily.

### 4.1 Revenue Triggers

| Condition | Action |
|---|---|
| * Daily revenue <30% of 7-day avg for 3+ consecutive days | Check Etsy search ranking first (incognito browser, primary keyword). If listing not on page 1: refresh tags using currently trending long-tail keywords; update listing description first paragraph. Do not increase social posting volume until listing is diagnosed. |
| Monthly gross revenue <$300 (Month 1) or <$600 (Month 2–3) | Diagnose views vs. conversion: if views >1,000/listing but orders <10, problem is conversion (messaging, pricing, mockup quality). If views <200/listing, problem is visibility (SEO, social not driving clicks). Apply correct fix only. |
| Single-guide revenue >65% of total revenue after 45 days | Over-dependence on one species guide. Begin cross-sell campaign to adjacent species in the same family (herbalists who buy ginseng are likely candidates for goldenseal). |
| Etsy Ads ROAS <1.5 for a single listing after 21 days | Pause that ad immediately. Fix the listing (cover image, description opening, price). Restart ads after 14 days of organic-only testing shows CVR improvement. |
| Etsy Ads ROAS >2.5 for 30+ days | Increase daily budget for that listing by 25–50%. This is a scale signal. |
| Bundle revenue >25% of monthly total before Month 3 | Advance the Phase 3 bundle expansion planning timeline by 30 days. Demand signal is ahead of projection. |

### 4.2 Cohort Balance Triggers

| Condition | Action |
|---|---|
| Conservation Naturalist cohort <20% of buyers at Day 60 | Content is skewing too far toward medicinal/harvesting angle. Add 2 conservation ethics posts per week for 30 days. Check Kit landing page copy — if it leads with "grow your own medicine" language, test a variant leading with "protect what's disappearing." |
| Herbalist / Practitioner cohort <15% of buyers at Day 60 | Harvesting-window seasonal content is not present or not visible. Add one "harvest window alert" email per month. Check whether medicinal-angle guide listings have preparation content visible above the fold in the description. |
| Educator / School cohort >30% of buyers in August–September | Positive signal — educators are adopting at higher rate than projected. Prepare a bulk pricing tier (3–5 copies at 15% discount, 6+ copies at 25% discount). Draft an outreach email template for nature centers and botanical garden education departments. Do not wait for Phase 3 planning cycle. |
| Educator / School cohort 0% at Day 90 (outside Aug–Sept) | Expected — this cohort is academic-calendar-driven. Do not misinterpret absence outside back-to-school window as zero demand. Evaluate this cohort exclusively in the August–October window. |
| Any single cohort >60% of buyers at Day 60 | Concentration risk: one cohort dominates and the seasonal revenue pattern becomes volatile. Identify the under-represented cohort. Run a 30-day targeted content experiment (2 posts/week, 1 email/month) directed at that cohort's specific value framing. Measure cohort mix shift at Day 90. |
| "Unknown/Unclassified" exceeds 25% of buyers at Day 30 | Post-purchase survey response rate is too low. Switch from optional survey to a Kit automation trigger: offer a $3 coupon on next purchase in exchange for completing the 1-question cohort survey. Re-evaluate after 30 days. |

### 4.3 Zone Performance Triggers

| Condition | Action |
|---|---|
| Zone 3–4 subscribers <8% of total Kit list at Day 90 | Northern states are underrepresented. These zones have strong homesteader and prepper overlap with conservation interest. Create 2–3 Zone 3–4 specific Pinterest pins featuring short-season endangered plant species. Measure zone growth over 30-day follow period. |
| Zone-cohort hypothesis wrong by >15pp in any zone | Adjust newsletter content plan for that zone. Example: if Zone 9–10 skews HerbalistPractitioner rather than ConservationNaturalist, de-emphasize iNaturalist identification content and add more cultivation and harvest-timing content for those zones. |
| A zone's subscriber growth flat/declining for 2 consecutive months despite active promotion, AND zone >15% of total list | Zone saturation signal. Stop acquisition-focused content for that zone; shift to retention content (seasonal guides, species spotlight for plants found in that zone). Redirect acquisition posts toward under-represented zones. |

### 4.4 Email Performance Triggers

| Condition | Action |
|---|---|
| Email 1 open rate <25% | Deliverability problem. Check SPF/DKIM DNS records in Kit; verify From address uses custom domain; confirm subject line "Your Zone [X] Quick-Start Card is ready" is not triggering spam filters. Do not revise content before fixing deliverability. |
| Welcome sequence Email 3–4 click rate <5% | Content hook is not compelling. Revise Email 3 to name the specific conservation issue (not a general framing): "95% of wild goldenseal is still harvested from the forest" rather than "goldenseal is at risk." Specific facts outperform abstract framing. |
| Newsletter open rate <22% for 3 consecutive sends | List health degradation. Check cold subscriber percentage (open rate <15%). If cold subscribers >25% of list, trigger win-back automation immediately (3-email sequence; remove non-responders). Test bi-weekly send frequency for 4 weeks. |
| Any single email unsubscribe rate >2% | That email is misaligned with subscriber expectations. Most likely cause: Email 4 catalog introduction is too promotional. Move catalog reference to second half; lead with educational story. |
| Email-to-buyer conversion rate (purchased tag / total subscribers) <5% at Day 60 | Email 5 coupon (SEEDWARDEN15) is not converting. Test: (a) increase coupon value from 15% to 20%; (b) reframe coupon email around species urgency ("This guide covers a species losing habitat every year — and the 15% code expires Sunday"). Measure lift after one test cycle. |

### 4.5 Zone-Specific Guide Performance Triggers

| Condition | Action |
|---|---|
| A specific endangered species guide has >500 views and <1% CVR after 30 days | This is an Anchor guide: driving traffic but not converting. Actions in priority order: (1) update cover image to show the specific plant in habitat (not a generic botanical illustration), (2) move the strongest unique fact about the species to the first sentence of the description, (3) check that the guide price is within $3 of comparable competitor listings. |
| A specific species guide converts at >3% CVR for 30+ days | This is a breakout Star. Create a related species guide in the same genus or ecological guild. Cross-sell from the Star listing. Pin the Star listing to top of shop. |
| No endangered species guide reaches Star classification by Day 60 | Messaging problem, not a product problem. Run a 14-day A/B test: split the two highest-view guides into two listing variants. Variant A: conservation framing in the title and first sentence. Variant B: practical use framing (medicinal preparation, identification in the field). Compare conversion rates at end of test. |

---

## Part 5: Historical Phase 1 Baseline Integration

Phase 1 data (from `etsy-analytics-template.csv` and `phase-2-ltv-tracker-phase1-baseline.csv`)
provides the performance baseline for calibrating Phase 2 expectations.

**Phase 1 reference benchmarks (actual data, May 2026 sample period):**

| Metric | Phase 1 Actual | Phase 2 Conservative | Phase 2 Target | Phase 2 Stretch |
|---|---|---|---|---|
| Orders / month | 47 | 25–45 | 46–70 | 71–100 |
| Gross revenue / month | $1,341 | $400–$700 | $700–$1,400 | $1,400–$2,200 |
| Conversion rate | 2.24% | 1.0–1.5% | 1.5–2.5% | 2.5–3.5% |
| AOV | $28.51 | $16–$22 | $22–$32 | $32–$45 |
| Repeat rate (30d) | 14.9% | 5–10% | 10–20% | 20%+ |
| Kit sign-ups / month | n/a (new funnel) | 20–50 | 50–100 | 100–200 |

**Phase 2 starts with a lower conversion rate assumption** than Phase 1 actual because
endangered species guides are a new product category for Seedwarden buyers. Expect a 4–6 week
establishment period before brand recognition and Etsy algorithm placement stabilize. If
Month 1 Phase 2 conversion rate matches Phase 1's 2.24%, that is an overperformance signal —
accelerate the Phase 3 content calendar by 30 days.

**Phase 1 buyers as Phase 2 warm leads**: Any Phase 1 buyer who opted into Kit via the
post-purchase thank-you email CTA is already in the welcome sequence. Flag these buyers in
the LTV tracker with `first_order_date < 2026-05-30`. When they purchase a Phase 2 guide,
record in the LTV tracker as a cross-sell (not a new buyer acquisition). Their 90-day repeat
purchase rate from Phase 1 (14.9%) is the baseline to beat with Phase 2 post-purchase
sequencing — target 18%+ for cross-sell conversion.

---

## Part 6: Implementation Checklist

### Analytics Infrastructure (Complete by May 20)

- [ ] GA4 Measurement ID confirmed in Etsy Shop Manager > Settings > Web Analytics
- [ ] GA4 custom dimensions registered: `guide_type`, `acquisition_source`, `inferred_cohort`,
  `visit_season`, `listing_slug`, `is_return_visitor` (exact names per `etsy-ga4-event-tracking.md`)
- [ ] GA4 audience segments created: Conservation Naturalist Signal, Herbalist Signal,
  Educator Signal, Gift Buyer Signal, High-Value Repeat Candidate (adapt from existing 5
  segments in `etsy-ga4-event-tracking.md` Section 4 with Phase 2 guide_type values)
- [ ] UTM parameters applied to all outbound links: Instagram bio, TikTok bio, Pinterest
  profile link, Kit landing page, all Etsy listing footer CTAs
- [ ] Kit Phase 2 cohort tags created: `Cohort_ConservationNaturalist`,
  `Cohort_HerbalistPractitioner`, `Cohort_EducatorSchool`
- [ ] Kit lifecycle tags confirmed active: `new-subscriber`, `purchased`, `vip`, `phase2-buyer`
- [ ] Post-purchase survey (1-question cohort identification) live in Kit Day 1 order
  confirmation email
- [ ] Google Sheets analytics workbook created with tabs: Daily, Weekly, Monthly, LTV Tracker,
  Monthly Data Log

### Pre-Launch Testing (May 20 – May 29)

- [ ] Day 1 of testing (May 20): Open a Seedwarden Etsy listing in incognito browser; check
  GA4 > Real-Time > Events within 60 seconds — `page_view` must appear
- [ ] Verify UTM parameters are passing correctly: click an Instagram bio link, check GA4
  Real-Time for `acquisition_source = instagram`
- [ ] Send test order through Etsy's test order system; verify Kit post-purchase email fires
  within 15 minutes of order confirmation
- [ ] Verify Kit cohort survey link is functional (click test, verify response routes to
  correct cohort tag assignment)
- [ ] Populate Daily tab with 3 days of synthetic baseline data (zeros or Phase 1 averages)
  to confirm formula references are working before real data arrives
- [ ] Confirm Kit landing page `view_zone_card_landing` and `lead_magnet_signup` events are
  firing (test via GA4 Real-Time after submitting a test form submission)

### Launch Day (May 30)

- [ ] Record baseline metrics at 9:00am before first posts go live:
  - Etsy listing views (starting count per guide)
  - Kit subscriber count
  - GA4 active users (Real-Time view)
- [ ] Record end-of-day May 30 metrics in the Daily tab (first real data row)
- [ ] Schedule first weekly review: Sunday June 7

### First Month Milestones

- [ ] June 7 (Week 1 review): Confirm cohort survey responses are arriving; check Daily tab
  for anomalies from launch week social activity
- [ ] June 13 (Day 14): Verify Phase 1 buyers in Kit post-purchase sequence are receiving
  Phase 2 cross-sell content; check `phase2-buyer` tag is assigning correctly
- [ ] June 20 (Day 21): First cohort mix read — is any cohort consistently <10% of orders?
  If so, flag for July content calendar adjustment
- [ ] June 30 (Day 30): First monthly deep dive; run Phase 3 readiness score; update LTV
  tracker with all June orders; calculate 30-day repeat rate per cohort

---

## Part 7: Dashboard Layout Summary

| Dashboard | Tool | Sections | Refresh | Time |
|---|---|---|---|---|
| Daily | Google Sheets "Daily" tab or Etsy mobile app | Revenue, orders, Kit sign-ups, anomaly signals | Every day (D1–30), then M/W/F | 10 min |
| Weekly | Google Sheets "Weekly" tab | Sales velocity (4-wk rolling), guide performance (top 5), cohort mix, email funnel, channel performance | Every Sunday | 30 min |
| Monthly | Google Sheets "Monthly" tab + CSV imports | Revenue summary, cohort LTV, guide classification, zone-cohort correlation, seasonal check, email health, Phase 3 readiness score | First Monday each month | 2 hours |

---

*Prepared: 2026-05-13. This document replaces the earlier Phase 1-era post-launch analytics
framework (which covered the forager/prepper/homesteader/gift buyer cohort model) with a
Phase 2-specific framework for the endangered species guide launch. The earlier framework
remains valid for Phase 1 product LTV tracking. For GA4 custom event implementation details,
see `etsy-ga4-event-tracking.md`. For Kit configuration details, see `phase-2-kit-email-setup.md`.
For the Phase 3 decision logic that activates when Phase 2 readiness criteria are met, see
`phase-3-product-expansion-roadmap.md`.*
