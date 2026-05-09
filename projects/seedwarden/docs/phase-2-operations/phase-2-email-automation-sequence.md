---
title: "Phase 2 Email Automation Sequence"
subtitle: "Day-by-day timing, Kit tags, A/B variants, link tracking, and delivery handling"
date: 2026-05-09
status: production-ready
scope: May 30 launch through Week 4 (June 27, 2026)
source: projects/seedwarden/phase-2-email-automation-sequence.md (root-level canonical)
references:
  - PHASE_2_EMAIL_STRATEGY.md
  - marketing/email-and-launch-plan.md
  - KIT_SETUP_NOTES.md
  - kit-account-setup-guide.md
---

# Phase 2 Email Automation Sequence
## May 30, 2026 — Week 4 (June 27)

This document is the operations reference for Phase 2 email automation. It specifies every send, trigger, tag, A/B variant, UTM parameter, and delivery-handling rule. No TODOs remain. Execute directly in Kit.

---

## Part 1: Sequence Architecture

Four email tracks run simultaneously through Phase 2.

| Track | Name | Trigger | Audience | Volume | Active |
|---|---|---|---|---|---|
| A | Welcome Sequence | New sign-up on Kit landing page | New subscribers | 5 emails over 10 days | From May 30 |
| B | Launch Broadcast | Manual send, May 30 12:00pm UTC | All confirmed subscribers | 1 broadcast | May 30 only |
| C | Post-Launch Nurture | Completion of Welcome Sequence | Subscribers who finished Email 5 | Weekly newsletter, Thursdays | From June 5 |
| D | Re-Engagement | 6 consecutive unopened sends | Inactive subscribers | 3 emails | Phase 3 only — do not build yet |

**Build order**: B first (schedule before launch), then A (active on launch), then C (first send June 5). Do not build D until subscriber list exceeds 200.

---

## Part 2: Launch Broadcast (Track B) — May 30

### Send Specifications

| Field | Value |
|---|---|
| Send date | May 30, 2026 |
| Send time | 12:00pm UTC (8:00am Eastern, 5:00am Pacific) |
| Recipients | All Confirmed Subscribers — exclude tags "bounced" and "unsubscribed" |
| Kit action | Broadcasts > Schedule > 12:00pm May 30 UTC |
| Preflight check | Confirm status shows "Scheduled" in Broadcasts list by May 29 17:00 UTC |

### Subject Line A/B Test (50/50 split)

| Variant | Subject | Preview text |
|---|---|---|
| A — control | Phase 2 is live — your zone card library just doubled | What to plant right now in your zone, with two new cards added this week. |
| B — test | Your Zone [X] just got an upgrade | We added two new zone cards — including yours. Here's what changed. |

Kit A/B setup: Broadcasts > New Broadcast > Subject Line Test > 50/50 split. Winner determination: Open Rate at 4-hour mark. Kit auto-sends winning variant to the remainder at 4:00pm UTC.

### Link Tracking — Broadcast UTM Parameters

| Destination | Full URL format |
|---|---|
| Etsy store root | `[etsy-store-url]?utm_source=kit&utm_medium=email&utm_campaign=phase2_launch&utm_content=broadcast_cta1` |
| Specific Etsy listing | `[listing-url]?utm_source=kit&utm_medium=email&utm_campaign=phase2_launch&utm_content=broadcast_listing_[product-slug]` |
| Kit landing page | `[kit-landing-url]?utm_source=kit&utm_medium=email&utm_campaign=phase2_launch&utm_content=broadcast_zonecta` |

Paste the full URL including UTM string into Kit's link field. Do not shorten these links — Kit tracks clicks independently and shortening breaks the UTM chain in GA4.

---

## Part 3: Welcome Sequence (Track A) — Day 0 through Day 10

### Sequence Configuration in Kit

| Field | Value |
|---|---|
| Sequence name | Seedwarden Welcome |
| Trigger | Form submitted on Zone Quick-Start Card landing page |
| Tags applied on trigger | `new-subscriber`, `zone-[X]` (zone field from form) |
| Total emails | 5 |
| Duration | Day 0 through Day 10 |
| Post-sequence action | Add tag `welcome-complete`; add to "Newsletter Subscribers" segment; remove `new-subscriber` tag |

### Email 1 — Day 0 (Immediate)

| Field | Value |
|---|---|
| Send delay | 0 minutes — send within 60 seconds of form submission |
| Variants | 8 (one per zone, Zones 3–10) |
| Subject (all zones) | Your Zone [X] Quick-Start Card is ready |
| Preview text | One page. What to plant right now in Zone [X]. |
| Primary CTA | Zone card download — Google Drive direct download URL per zone |
| Secondary CTA | None — no product links in Email 1 |
| Tags applied | None new |
| Copy source | marketing/email-and-launch-plan.md > Email 1 |

**Zone routing in Kit**: IF subscriber field "zone" = 3 THEN send Zone 3 variant. Replicate for Zones 4–10. Verify conditional rules published before any subscriber submits the form.

**A/B subject test** (activate after 50 subscribers to collect data):

| Variant | Subject |
|---|---|
| A — control | Your Zone [X] Quick-Start Card is ready |
| B — test | Here's your Zone [X] planting guide — one page, what to grow right now |

Winner determination: open rate at 24-hour mark. Apply winning subject to all new subscribers from that point.

### Email 2 — Day 2

| Field | Value |
|---|---|
| Send delay | 2 days after Email 1 |
| Variants | 1 (same for all zones) |
| Subject — A | The tomato that changed how I think about seeds |
| Subject — B | Why the seeds at your local nursery aren't what they used to be |
| Preview text | A 1940s farmer, a Brandywine, and why heirloom seeds matter now. |
| Primary CTA | None — educational email, no product links |
| Forward hook | "Next email I'll share a mistake I made that cost me an entire season." |
| Copy source | marketing/email-and-launch-plan.md > Email 2 |

### Email 3 — Day 5

| Field | Value |
|---|---|
| Send delay | 5 days after Email 1 (3 days after Email 2) |
| Variants | 1 |
| Subject — A | The seed-saving mistake that cost me a whole season |
| Subject — B | What I got wrong about tomato seeds (and how to fix it) |
| Preview text | I learned the hard way. You don't have to. |
| Primary CTA | Behavioral tag link — "Read more about seed saving" → Seed Saving Field Manual Etsy listing |
| Tag applied on click | `seed-saver` |
| Copy source | marketing/email-and-launch-plan.md > Email 3 |

**Kit tag automation for Email 3**: Automations > New Rule > Trigger: Subscriber clicks link > URL contains Seed Saving Field Manual listing ID > Action: Add tag `seed-saver`.

### Email 4 — Day 7

| Field | Value |
|---|---|
| Send delay | 7 days after Email 1 (2 days after Email 3) |
| Subject — A | Here's what I've been building |
| Subject — B | Three guides for three kinds of growers — which one are you? |
| Preview text | Three guides. Three kinds of growers. See which one fits you. |
| Primary CTA | Three segmentation links — each applies an interest tag |
| Copy source | marketing/email-and-launch-plan.md > Email 4 |

**Segmentation CTAs — three separate links in Email 4 body**:

| Link text | Destination | Tag on click |
|---|---|---|
| "Growing in an apartment or container?" | Container Growing Blueprint listing | `city-grower` |
| "Saving seeds and building food sovereignty?" | Seed Saving Field Manual listing | `seed-saver` |
| "Preserving your harvest?" | Harvest Preservation Handbook listing | `preservationist` |

Subscribers who click no links: no tag applied; receive full untagged newsletter.

### Email 5 — Day 10

| Field | Value |
|---|---|
| Send delay | 10 days after Email 1 (3 days after Email 4) |
| Subject | A thank-you — and an offer that expires in 5 days |
| Preview text | SEEDWARDEN15 takes 15% off anything in the shop. Here's why I made it. |
| Coupon code | SEEDWARDEN15 (15% off, no minimum, manual entry at Etsy checkout) |
| Coupon expiry | 5 days from Email 5 send date |
| Tag-based product lead | See table below |
| Copy source | marketing/email-and-launch-plan.md > Email 5 |

**Tag-conditional product lead in Email 5**:

| Subscriber has tag | Product to lead with |
|---|---|
| `seed-saver` | Seed Saving Field Manual |
| `city-grower` | Container Growing Blueprint |
| `preservationist` | Harvest Preservation Handbook |
| No interest tag | Zone Calendar (highest Phase 1 sales volume) |

**Coupon attribution tracking**: Etsy does not provide email-source attribution. Track SEEDWARDEN15 "Times Used" in Etsy > Marketing > Coupons at Day 10, Day 15 (coupon expiry), and Day 30. The Day 10–Day 15 delta represents Email 5 attributed redemptions. Log each count in WORKLOG.md.

---

## Part 4: Post-Launch Nurture Newsletter (Track C) — June 5 onward

### Newsletter Configuration

| Field | Value |
|---|---|
| Audience | All subscribers with `welcome-complete` tag (finished 5-email sequence) |
| Send day | Thursdays |
| Send time | 10:00am Eastern (subject to adjustment based on open rate data) |
| Frequency | Weekly |
| First send | June 5, 2026 |

### June–July Newsletter Schedule

| Send date | Product spotlight | UTM content tag |
|---|---|---|
| June 5 (Newsletter 1) | Seed Saving Field Manual | `newsletter_jun5` |
| June 12 (Newsletter 2) | Zone Quick-Start Card (re-engage with new zone content) | `newsletter_jun12` |
| June 19 (Newsletter 3) | Container Growing Blueprint | `newsletter_jun19` |
| June 26 (Newsletter 4) | Harvest Preservation Handbook | `newsletter_jun26` |
| July 3 (Newsletter 5) | Companion Planting Chart | `newsletter_jul3` |
| July 10 (Newsletter 6) | Survival Garden (Phase 3 preview — if ready) | `newsletter_jul10` |

Newsletter UTM format: `utm_source=kit&utm_medium=email&utm_campaign=phase2_nurture&utm_content=[tag-above]`

---

## Part 5: Integration Points

### MailerLite vs. Klaviyo Decision

Seedwarden uses **Kit** as the primary email platform. MailerLite or Klaviyo are not required for Phase 2. If migration becomes necessary (e.g., Kit tier limits reached, advanced segmentation needed):

- **MailerLite**: Lower cost ($10/month for up to 1,000 subscribers), simpler automation builder. Migration effort: 2–3 hours. Suitable if Kit limitations are the driver.
- **Klaviyo**: E-commerce focused, native Etsy integration (connect via Zapier or direct API). $20/month for up to 500 subscribers. Justified only if Etsy order-triggered sequences are needed (Phase 3 scenario).

Decision trigger: migrate if Kit free tier subscriber limit (10,000) is reached, or if Etsy-triggered automation is required in Phase 3. No migration before Phase 3.

### GA4 Attribution

GA4 captures UTM parameters automatically when subscribers click email links and land on pages with the GA4 snippet. Seedwarden's GA4 snippet must be installed on the Kit landing page (via Kit's custom code field) and on any external pages used as destinations.

Verify in GA4 > Reports > Acquisition > Traffic Acquisition > Source/Medium. Kit email traffic appears as `kit / email` or `email / (none)` depending on whether UTMs are present. With UTMs correctly appended, it appears as `kit / email` with campaign-level breakdown available under `utm_campaign`.

---

## Part 6: Delivery Handling

### Hard Bounces

Kit automatically suppresses hard-bounced addresses (permanent delivery failures — address does not exist). No manual action required. Log the bounce count from the launch broadcast in WORKLOG.md at T+24h. If bounce count exceeds 5% of send volume, escalate: review the list source for data quality issues.

### Soft Bounces

Soft bounces (temporary failures — mailbox full, server unavailable) are retried automatically by Kit's SendGrid infrastructure for up to 72 hours. If a soft bounce resolves within 72 hours, the subscriber receives the email with no indication of the delay. No manual action.

### Unsubscribes

Kit handles unsubscribes automatically. All emails include a legal CAN-SPAM unsubscribe link. Unsubscribed addresses are removed from all future sends immediately. Log the running unsubscribe count weekly in WORKLOG.md. Alert threshold: 2% cumulative unsubscribe rate on any single send. If triggered, review that send's content for tone or relevance mismatch.

### ISP Whitelisting

If Gmail or Outlook deliverability degrades (identified by low open rates from those domains specifically), submit a whitelist request:
- Gmail Postmaster Tools: postmaster.google.com — register the sender domain and monitor domain reputation score.
- Microsoft Smart Network Data Services (SNDS): postmaster.live.com — register the sending IP range (Kit's SendGrid IPs; Kit support provides the range on request).

SPF and DKIM must be configured before submitting whitelist requests. See `kit-account-setup-guide.md` Part 1.3 for DNS authentication setup.

---

*Status: production-ready. All sequences, tags, UTMs, and delivery procedures are fully specified. No TODOs. Execute in Kit from May 28 (setup) through May 30 (launch).*
