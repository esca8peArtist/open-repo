---
title: "Etsy + GA4 Event Tracking — Technical Specification"
created: 2026-05-05
session: 733
status: implement-at-launch
cross-references:
  - post-launch-analytics-framework.md
  - google-analytics-integration-guide.md
  - analytics/monthly-metrics-checklist.md
---

# Etsy + GA4 Event Tracking: Technical Specification

**Purpose**: Precise schema for all GA4 custom events, custom dimensions, audience segment definitions, and attribution logic applicable to Seedwarden on Etsy. This document is complementary to `google-analytics-integration-guide.md` (setup instructions) and `post-launch-analytics-framework.md` (architecture). Read those first if you have not already.

**Hard constraints to keep in mind**:
- GA4 fires on Etsy listing pages only when the GA4 Measurement ID is entered in Shop Manager. It does not fire on the Etsy homepage, search results, or checkout pages.
- Purchase events cannot be captured by GA4 on Etsy. Transaction data must come from the Etsy API or manual dashboard exports.
- Etsy blocks third-party JavaScript injection; only the standard GA4 gtag snippet via the Shop Manager integration is supported.

---

## 1. Standard Event Inventory

These are the GA4 events that will fire on Etsy listing pages automatically once the GA4 ID is configured. No custom code is needed for these.

| Event Name | Fires When | Key Parameters Collected Automatically |
|---|---|---|
| `page_view` | User opens a listing page | `page_title`, `page_location`, `page_referrer` |
| `session_start` | New session begins | `session_id`, `engagement_time_msec` |
| `user_engagement` | User is active on the page | `engagement_time_msec` |
| `scroll` | User scrolls to 90% of page | `percent_scrolled` (90) |
| `first_visit` | New user visits for the first time | — |

**What these give you**: Traffic source attribution (which channel drove the visit), device type, user country/city, whether the visitor is new or returning, and how long they engaged with the listing page.

**What these do not give you**: Whether the visitor purchased, what they searched for on Etsy, or any event that happens after they leave the listing page to go to cart/checkout.

---

## 2. GA4 Custom Dimensions

Custom dimensions let you segment reports by attributes specific to Seedwarden. These must be registered in GA4 Admin before events that carry them are processed.

### 2.1 Event-Scoped Custom Dimensions

Register these in GA4 Admin > Custom Definitions > Custom Dimensions:

| Dimension Name | Scope | Event Parameter Name | Description | Example Values |
|---|---|---|---|---|
| Guide Type | Event | `guide_type` | Category of guide viewed | `wild_edibles`, `medicinal_plants`, `native_plants`, `complete_bundle`, `mushroom_id`, `survival_prep` |
| Acquisition Source | Event | `acquisition_source` | UTM source from the referral | `kit`, `pinterest`, `reddit`, `instagram`, `etsy_organic`, `direct` |
| Customer Cohort (inferred) | Event | `inferred_cohort` | Cohort signal from session behavior | `forager`, `prepper`, `homesteader`, `gift_buyer`, `unknown` |
| Season | Event | `visit_season` | Season of the visit | `spring_planning`, `preservation`, `holiday_gift`, `long_tail` |
| Listing Slug | Event | `listing_slug` | URL-safe identifier for the listing | `wild-edibles-guide`, `medicinal-plants-guide`, `complete-bundle` |
| Return Visitor | Event | `is_return_visitor` | Whether GA4 has seen this user before | `true`, `false` |

### 2.2 How to Register a Custom Dimension

1. Go to GA4 > Admin > Data Display > Custom Definitions
2. Click "Create custom dimension"
3. Enter the Dimension Name (from table above)
4. Set Scope to "Event"
5. Enter the Event Parameter Name exactly as shown in the table (these are case-sensitive)
6. Click Save

Repeat for each dimension. Custom dimensions only apply to events fired after registration; historical events will not be retroactively populated.

---

## 3. Custom Event Schema

Because Etsy does not allow custom JavaScript beyond the standard GA4 snippet, these custom events apply to any Seedwarden-controlled web property (a landing page, lead magnet page, Kit opt-in page, or any future standalone site). They are documented here for implementation when those surfaces exist.

### 3.1 `view_guide` — User Views a Specific Guide

Fire when: A user lands on any guide-specific landing page or product detail page (outside Etsy).

```javascript
gtag('event', 'view_guide', {
  guide_type: 'wild_edibles',          // category
  listing_slug: 'wild-edibles-guide',  // slug matching Etsy listing
  acquisition_source: 'kit',           // from UTM utm_source
  inferred_cohort: 'forager',          // cohort signal from source/behavior
  visit_season: 'spring_planning',     // derived from current month
  is_return_visitor: 'false'           // from GA4 client_id lookup
});
```

**Parameters required**: `guide_type`, `listing_slug`
**Parameters optional**: all others (pass when available from UTM or session context)

### 3.2 `view_bundle` — User Views a Bundle Listing

Fire when: User views any bundle product page.

```javascript
gtag('event', 'view_bundle', {
  guide_type: 'complete_bundle',
  listing_slug: 'seedwarden-complete-bundle',
  acquisition_source: 'pinterest',
  inferred_cohort: 'prepper',          // bundles skew prepper
  visit_season: 'holiday_gift'
});
```

### 3.3 `purchase_guide` — Purchase Confirmed (Standalone Site Only)

This event cannot fire on Etsy. Implement on any standalone checkout confirmation page.

```javascript
gtag('event', 'purchase', {
  transaction_id: 'ORD-2026-001',      // Etsy receipt_id or internal order ID
  value: 42.50,                        // order total in USD
  currency: 'USD',
  items: [
    {
      item_id: 'wild-edibles-guide',
      item_name: 'Wild Edibles Guide — Pacific Northwest',
      item_category: 'wild_edibles',
      price: 22.00,
      quantity: 1
    },
    {
      item_id: 'medicinal-plants-guide',
      item_name: 'Medicinal Plants Field Manual',
      item_category: 'medicinal_plants',
      price: 20.50,
      quantity: 1
    }
  ],
  // Custom parameters
  inferred_cohort: 'forager',
  acquisition_source: 'kit',
  visit_season: 'spring_planning'
});
```

**GA4 ecommerce items array**: Each item in the `items` array must include at least `item_name` or `item_id`. Additional recommended parameters: `item_category`, `price`, `quantity`. Up to 27 custom parameters per item are supported.

### 3.4 `lead_magnet_signup` — Email Opt-In on Kit Landing Page

Fire when: User submits the Kit landing page form (via Kit's embed on a landing page you control, or a Kit-hosted page with a custom domain).

```javascript
gtag('event', 'lead_magnet_signup', {
  acquisition_source: 'pinterest',     // from utm_source
  inferred_cohort: 'forager',          // from utm_campaign or landing page
  visit_season: 'spring_planning',
  form_location: 'kit_landing_page'
});
```

### 3.5 `return_visitor` — Visitor Returns Within 30 Days

Fire when: A returning user (GA4 first_visit date > 30 days ago) opens a listing page. This is approximated using GA4's client ID age; it cannot be done directly in Etsy's GA4 integration, but can be implemented on a standalone site.

```javascript
gtag('event', 'return_visitor', {
  listing_slug: 'wild-edibles-guide',
  days_since_first_visit: 14,          // derived from GA4 client_id first_seen timestamp
  inferred_cohort: 'forager'
});
```

### 3.6 `high_engagement` — User Spends 3+ Minutes on a Page

Fire when: 180 seconds have elapsed on any guide page (standalone site only).

```javascript
setTimeout(function() {
  gtag('event', 'high_engagement', {
    listing_slug: 'wild-edibles-guide',
    guide_type: 'wild_edibles',
    time_threshold_seconds: 180,
    inferred_cohort: 'forager'
  });
}, 180000);
```

---

## 4. Audience Segment Definitions

These are GA4 audience definitions to create in Admin > Audiences. They enable cohort-level reporting and can be used to build remarketing lists if you later connect Google Ads.

### Segment 1: Active Forager Signal

**Definition**: Sessions that viewed a wild_edibles or medicinal_plants guide AND session duration exceeded 120 seconds.

**GA4 Configuration**:
- Condition 1: Event `page_view` where `page_location` contains `/wild-edibles` OR `/medicinal-plants`
- Condition 2: Session duration > 120 seconds

**Membership duration**: 30 days (foragers are seasonally active; stale after one month)

**Use**: Target with seasonal foraging campaigns (spring mushroom, fall nut season). Export list monthly to Kit for email segmentation.

### Segment 2: Prepper / Bundle Buyer Signal

**Definition**: Sessions that viewed a complete_bundle listing OR viewed 4+ separate guide listings in one session.

**GA4 Configuration**:
- Condition 1: Event `page_view` where `page_location` contains `/complete-bundle` OR `/survival`
- OR: Count of distinct `page_view` events in session > 3 (research depth signal)

**Membership duration**: 60 days (preppers make less frequent but deliberate purchases)

**Use**: Bundle promotions, event-triggered campaigns (news of economic/natural disruption).

### Segment 3: Homesteader Signal

**Definition**: Sessions from users who viewed both a medicinal guide AND a plant ID or native plants guide within any 7-day window.

**GA4 Configuration**:
- Sequence condition within 7 days:
  - Step 1: `page_view` where `guide_type` = `medicinal_plants`
  - Step 2 (any time after): `page_view` where `guide_type` = `native_plants` OR `wild_edibles`

**Membership duration**: 90 days (homesteaders are project-driven, return at project intervals)

**Use**: Project-seasonal campaigns (spring planting, fall preservation), medicinal herb content.

### Segment 4: Gift Buyer Signal

**Definition**: Sessions from mobile devices, session duration under 90 seconds, occurring in May 1–10, November 1 – December 31, or June 1–20.

**GA4 Configuration**:
- Device category: `mobile`
- Session duration: < 90 seconds
- Date-based condition: sessions within gift-giving windows

**Membership duration**: 14 days (gift buying is highly time-bound)

**Use**: Holiday and occasion-specific promotions. Do not include in botanical content campaigns.

### Segment 5: High-Value Repeat Candidate

**Definition**: Return visitors (not first_visit) who have viewed 3+ different listing slugs across two or more sessions.

**GA4 Configuration**:
- Condition: `first_visit` event NOT in session (i.e., returning user)
- Condition: Count of distinct `page_location` values across sessions > 2

**Membership duration**: 30 days

**Use**: This segment identifies buyers who are researching before purchasing a second time. Target with cross-sell email at Day 21 post-first-purchase (overlaps with Kit Automation 2, Email 3).

---

## 5. Attribution Model

### For Traffic Measurement (GA4)

**Model**: Last non-direct click (GA4's default data-driven model for traffic reports).

**Rationale**: For Seedwarden, the channel that immediately preceded the Etsy visit is the most actionable attribution signal. A user who clicked a Pinterest pin and then visited the listing two days later should credit Pinterest, not a prior organic search from three weeks ago.

**Exception**: Email campaigns. When a user clicks an email link and visits within 5 days, credit email even if they return via direct the next day. This is handled by Kit's own click tracking and is reported separately from GA4.

### For Guides vs. Bundles (Different Attribution Logic)

Individual guide purchases are typically single-session decisions — the customer searches Etsy, finds the listing, and buys. Last-click attribution is appropriate.

Bundle purchases show a longer consideration window. Analysis of session data should account for the fact that bundle buyers may view individual listings over 2–4 sessions before converting. When you see a bundle purchase in Etsy API data, look at GA4 session history for that same timeframe to reconstruct the multi-touch path (GA4 > Explore > Path exploration, filtered by the bundle listing URL).

### For Email Attribution

Kit provides native email open and click tracking. Use Kit's dashboard as the source of truth for email-originated conversions, not GA4. Cross-reference Kit click dates with Etsy order dates within a 7-day window to measure email-to-purchase conversion rate per campaign. This cross-reference is done manually in `analytics/monthly-metrics-checklist.md` Section 3.

---

## 6. Custom Dimension Derivation Logic

When a user arrives via a UTM link, derive dimension values as follows:

| UTM Parameter | Custom Dimension | Derivation Logic |
|---|---|---|
| `utm_source=kit` | `acquisition_source = kit` | Direct |
| `utm_source=pinterest` | `acquisition_source = pinterest` | Direct |
| `utm_source=reddit` | `acquisition_source = reddit` | Direct |
| (no UTM, referrer = etsy.com) | `acquisition_source = etsy_organic` | Referrer check |
| (no UTM, referrer = none) | `acquisition_source = direct` | No referrer |
| `utm_campaign` contains `forager` | `inferred_cohort = forager` | Campaign name signal |
| `utm_campaign` contains `prepper` or `survival` | `inferred_cohort = prepper` | Campaign name signal |
| `utm_campaign` contains `homestead` | `inferred_cohort = homesteader` | Campaign name signal |
| `utm_campaign` contains `gift` or `holiday` | `inferred_cohort = gift_buyer` | Campaign name signal |
| Month 3, 4, 5 | `visit_season = preservation` | Server-side date |
| Month 11, 12 | `visit_season = holiday_gift` | Server-side date |
| Month 1, 2, 3 | `visit_season = spring_planning` | Server-side date |

---

## 7. Monthly GA4 Reporting Workflow

On the first Monday of each month (integrated into `analytics/monthly-metrics-checklist.md`):

1. GA4 > Reports > Acquisition > Traffic acquisition — export by session source / medium. Note top 3 channels by session volume. Record in Monthly Data Log.

2. GA4 > Reports > Engagement > Pages and screens — filter by listing pages only (filter `page_location` contains `etsy.com/listing`). Export the top 10 listing pages by views. Cross-reference against Etsy order data to check which high-view listings are converting and which are not.

3. GA4 > Explore > Create Free Form exploration:
   - Rows: `session_default_channel_group`
   - Columns: `device_category`
   - Values: Sessions, Engaged sessions, Engagement rate
   - This shows whether mobile or desktop users are more engaged per channel.

4. GA4 > Explore > Cohort exploration (if using a standalone landing page):
   - Cohort dimension: `First touch date` (weekly)
   - Metric: Retention per week
   - This shows how many users return to your landing page each week after their first visit.

5. Export segment sizes for all 5 defined audiences. If a segment size exceeds 1,000 users, it is large enough to use for Google Ads remarketing (activate if Gate D is triggered).

---

## 8. Event Parameter Quick Reference

| Parameter | Max Length | Required In | Notes |
|---|---|---|---|
| `guide_type` | 100 chars | All custom events | Use snake_case; match to product slug convention |
| `listing_slug` | 100 chars | `view_guide`, `view_bundle`, `high_engagement` | Must match Etsy listing URL segment |
| `acquisition_source` | 100 chars | All custom events | Derive from `utm_source` |
| `inferred_cohort` | 100 chars | All custom events | Best-guess at time of event; revise with survey data |
| `visit_season` | 100 chars | All custom events | Derive from calendar month |
| `is_return_visitor` | 5 chars | `view_guide`, `view_bundle` | Boolean as string: `true` / `false` |
| `time_threshold_seconds` | — | `high_engagement` | Integer value; use 180 |
| `transaction_id` | 100 chars | `purchase` | Use Etsy receipt_id |
| `value` | — | `purchase` | Float, USD |
| `currency` | 3 chars | `purchase` | Always `USD` |
| Items array `item_id` | 100 chars | `purchase` | Use listing slug |
| Items array `item_category` | 100 chars | `purchase` | Use guide_type value |

---

*Cross-references: `post-launch-analytics-framework.md` (architecture and data sources), `google-analytics-integration-guide.md` (GA4 setup steps), `customer-cohort-analysis-framework.md` (cohort definitions), `analytics/cohort-analysis-template.sql` (SQL queries for Etsy API data).*
