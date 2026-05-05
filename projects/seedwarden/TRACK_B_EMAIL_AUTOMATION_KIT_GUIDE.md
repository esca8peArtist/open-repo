---
title: "Email Automation — Kit Platform Setup Guide"
date: 2026-05-05
session: 728
status: production-ready — user account creation required; all decisions resolved
scope: Kit (kit.co) account setup, landing page, zone routing, 5-email welcome sequence, testing
references:
  - KIT_SETUP_NOTES.md (detailed platform setup with all 15 tags)
  - PHASE_2_EMAIL_STRATEGY.md (email strategy and sequence architecture)
  - marketing/email-and-launch-plan.md (full email copy, all 5 emails)
  - CANVA_ZONE_CARD_BATCH_WORKFLOW.md (zone card content)
  - MAY_CONTENT_EXECUTION_PLAN.md (email sequences section with Email 1-3 copy)
---

# Email Automation — Kit Platform Setup Guide

**Purpose**: Complete step-by-step guide for setting up Kit (kit.co) as the email automation
platform for the Zone Quick-Start Card funnel. Every decision is made. You are clicking
through a UI following these instructions.

**Time required**:
- Account setup + landing page: 30-60 minutes (do this with social account creation)
- 15 tags setup: 15 minutes
- Email 1 (8 zone variants): 60-90 minutes (do after zone cards are built)
- Emails 2-5: 60-90 minutes total
- Zone routing automation: 30 minutes
- End-to-end testing: 20 minutes

**Total**: 3-4.5 hours, done in stages across Week 1 and Week 3.

**Email copy location**: All 5 email full bodies are in `marketing/email-and-launch-plan.md`.
Additional Email 1-3 copy is in `MAY_CONTENT_EXECUTION_PLAN.md` Section "Email Sequences."

---

## Step 1: Account Creation

1. Go to kit.co
2. Click "Start for free"
3. Enter email: wanka95@gmail.com
4. Sender name: `Seedwarden`
5. Sender email: wanka95@gmail.com (can update to custom domain in Phase 3)
6. Time zone: your local time zone
7. Business type: "Creator" or "E-commerce" — either works

**Free tier capacity** (confirmed adequate for Phase 2):
- Up to 10,000 subscribers
- Unlimited email sends
- 1 landing page (all 8 zone variants route through one page)
- Conditional logic for zone routing (available on free tier)
- No A/B testing (Phase 3 feature)

---

## Step 2: Create All 15 Tags

Tags must exist before building any automation. Create them all in one session.

Navigate to: Kit > Subscribers > Tags > "Create a tag"

### Zone Tags (8 tags)

Create one tag per zone. Name them exactly as shown:

| Tag Name | Applied When |
|---|---|
| zone-3 | Subscriber selects Zone 3 on sign-up form |
| zone-4 | Subscriber selects Zone 4 |
| zone-5 | Subscriber selects Zone 5 |
| zone-6 | Subscriber selects Zone 6 |
| zone-7 | Subscriber selects Zone 7 |
| zone-8 | Subscriber selects Zone 8 |
| zone-9 | Subscriber selects Zone 9 |
| zone-10 | Subscriber selects Zone 10 |

### Interest Cohort Tags (7 tags)

| Tag Name | Applied When |
|---|---|
| seed-saver | Subscriber clicks Seed Saving Manual link in Email 3 OR food sovereignty link in Email 4 |
| city-grower | Subscriber clicks apartment/container link in Email 4 |
| preservationist | Subscriber clicks preservation link in Email 4 |
| forager | Subscriber clicks wild plants or foraging link in any email |
| prepper | Subscriber clicks survival/livestock link in any email |
| homesteader | Subscriber clicks livestock or homestead link in any email |
| etsy-buyer | Applied via Etsy integration or manual import after a purchase |

**Note on cohort tags**: Do not ask subscribers to self-identify on the sign-up form.
The form captures zone only. Cohort tags are earned by what subscribers click, not what
they say they are. This produces more reliable segmentation.

---

## Step 3: Landing Page Setup

Build the landing page before the email sequence. The landing page URL must be live before
you add it to social bios and zone card footers.

### Create the Page

1. In Kit: navigate to "Landing Pages and Forms" > "Create New" > "Landing Page"
2. Select a simple single-column template (minimal is better for this audience)
3. Configure:

**Page headline**: `Your Free Zone Quick-Start Card`

**Page subheadline**:
```
Know exactly what to plant, when to plant it, and what to do right now in your zone —
one-page reference card, free.
```

**Form fields** (add exactly three — each additional field reduces conversion 10-15%):
1. First name — Required
2. Email address — Required
3. Growing zone — Dropdown, Required
   - Add these dropdown values: Zone 3, Zone 4, Zone 5, Zone 6, Zone 7, Zone 8, Zone 9, Zone 10

**CTA button text**: `Send My Zone Card`

**Trust text** (small font below the button):
```
No spam. Unsubscribe anytime. Seedwarden sends one email per week about growing,
foraging, and real food.
```

**Background color**: Set to #F5EDD6 (Warm Cream) if the template supports custom hex; otherwise use white.

### Publish and Record

1. Click "Publish" to make the page live
2. Copy the landing page URL (it will be something like: kit.com/seedwarden/zone-card or similar)
3. Add the URL to:
   - All three social media bios (Instagram, TikTok, Pinterest)
   - CANVA_SETUP_STATUS.md footer placeholder field (replace `[KIT-LANDING-PAGE-URL]`)
   - social-media-setup.md (fill in the landing page URL line)

---

## Step 4: Zone Routing Automation

This automation sends the correct zone card PDF to each subscriber based on their zone selection.
Build this before any email copy.

### Recommended Method (Option A — simpler)

Create 8 variants of Email 1, one per zone. Use Kit automation rules:
"If subscriber has tag zone-5, send Email 1 Zone 5 variant."

**Why Option A**: Kit's free tier supports this approach reliably. It is slightly more work
to build (8 email drafts instead of 1) but has zero failure modes. Use this for launch.

**Build order**: Start with Zone 5, then Zone 6, then Zones 3, 4, 7, 8, 9, 10.
Zone 5 is statistically the most common US zone — test this one first.

### Automation Setup in Kit

1. Navigate to: Kit > Automations > Create Automation
2. Trigger: "When subscriber completes a form" > select the Zone Card landing page form
3. First step: "Add tag" based on zone dropdown value
   - If zone dropdown = "Zone 5" → apply tag "zone-5"
   - Repeat for all 8 zones
4. Second step: "Send email" → select Email 1 Zone 5 variant (for subscribers with zone-5 tag)
5. Repeat step 4 for all 8 zone-email combinations
6. Save automation

### PDF Upload for Zone Card Links

Zone card PDFs are built in Canva and exported to `projects/seedwarden/assets/zone-cards/`.
Kit does not host files — use Google Drive:

1. Upload each zone PDF to Google Drive
2. Right-click each file > "Share" > "Change to Anyone with the link" > Copy link
3. For direct download (bypasses Google Drive preview), replace the end of the URL:
   - Change: `...drive.google.com/file/d/[FILE_ID]/view?usp=sharing`
   - To: `...drive.google.com/uc?export=download&id=[FILE_ID]`
4. Paste the download link into the corresponding Email 1 zone variant button

Record all Google Drive links in TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md Part 2 (the link
table at the end of the zone card section).

---

## Step 5: Welcome Sequence Build — All 5 Emails

Full copy for all 5 emails is in `marketing/email-and-launch-plan.md`.
Email 1-3 copy is also in `MAY_CONTENT_EXECUTION_PLAN.md` Section "Email Sequences."

Build in this exact order:

### Email 1 — Zone Card Delivery (Day 0, immediate)

Build 8 variants, one per zone. Each variant is identical except for:
- The zone number in the subject line and body
- The PDF download button link (zone-specific Google Drive URL)
- The opening sentence ("Your Zone 5 Quick-Start Card is ready")

**Subject line template**: `Your Zone [X] Quick-Start Card is ready`

**Email body** (copy from MAY_CONTENT_EXECUTION_PLAN.md Email 1 section, substitute [X] with zone number):

Opening: Hi [First Name],

Your Zone [X] Quick-Start Card is attached — one page with everything you need to get
started this season.

[Download Your Zone [X] Card — button linking to Google Drive PDF]

Inside the card:
- Your frost date range for Zone [X]
- The 3-5 crops that do best in your zone right now
- Storage and preservation notes for your climate
- A variety spotlight: one variety that performs consistently in Zone [X]

[Continue with remainder of Email 1 copy from email-and-launch-plan.md]

**Kit setup steps**:
1. Create > Email > New Email (do this 8 times)
2. Subject: "Your Zone [X] Quick-Start Card is ready" (fill in zone number)
3. Paste body copy; add download button pointing to Google Drive URL for that zone
4. Tag email with the zone-[X] tag so automation routes correctly
5. Save all 8 drafts before connecting to automation

---

### Email 2 — Heirloom Seed Philosophy (Day 2)

Single version, all subscribers. No zone personalization required.

**Subject**: Copy from `marketing/email-and-launch-plan.md` Email 2
**Body**: Full copy in `marketing/email-and-launch-plan.md` Email 2
**Purpose**: Educational. Builds brand authority before any catalog mention.
**No product links in this email.** No tracked links. No calls to action to buy.

---

### Email 3 — Seed Saving Story (Day 5)

Single version, all subscribers.

**Subject**: Copy from `marketing/email-and-launch-plan.md` Email 3
**Body**: Full copy in `marketing/email-and-launch-plan.md` Email 3
**Purpose**: Trust building through a personal story about a seed saving mistake.

**Behavioral tag link required**:
- Include a tracked link to the Seed Saving Field Manual Etsy listing (or placeholder URL)
- In Kit: when creating this link, enable "Click to add tag" > select "seed-saver"
- Subscribers who click this link automatically receive the "seed-saver" tag
- This is the first click-tracked link in the sequence — it is how Kit learns what each
  subscriber is interested in

---

### Email 4 — Catalog Introduction (Day 7)

Single version, all subscribers.

**Subject**: Copy from `marketing/email-and-launch-plan.md` Email 4
**Body**: Full copy in `marketing/email-and-launch-plan.md` Email 4
**Purpose**: Introduce the full product catalog. Three segmentation links.

**Three behavioral tag links required**:

| Link Destination | Kit Tag to Apply on Click |
|---|---|
| Apartment/container growing products | city-grower |
| Seed saving / food sovereignty products | seed-saver |
| Food preservation products | preservationist |

Set up each link in Kit with "Click to add tag" enabled. This is how Kit segments the
subscriber list for future newsletter personalization.

---

### Email 5 — First Offer (Day 10)

Single version, all subscribers.

**Subject**: Copy from `marketing/email-and-launch-plan.md` Email 5
**Body**: Full copy in `marketing/email-and-launch-plan.md` Email 5
**Purpose**: First product recommendation with a discount code.

**Coupon code**: `SEEDWARDEN15` (15% off, 5-day window)

**Product recommendations**: Use these defaults if Phase 1 Etsy conversion data is not
yet available:
- Seed Saving Field Manual — best fit for new growers
- Zone Seed Starting Calendar — best fit for planners
- Harvest Preservation Field Manual — best fit for preservationists

When Etsy data becomes available (30+ days after first listing view), update Email 5
recommendations to reflect actual top-converting products.

**Coupon setup**: Create the Etsy coupon before Email 5 goes live:
- Etsy Shop Manager > Marketing > Sales and Discounts > Create Discount
- Code: SEEDWARDEN15
- Discount: 15% off
- Minimum order: none
- Expiration: set to 7 days after creation (refresh weekly if needed, or leave evergreen)

---

## Step 6: End-to-End Testing (Required Before Going Live)

Complete before linking the landing page from any social bio.

### Test 1 — Zone 5

1. Open the Kit landing page in an incognito browser window
2. Fill in: test first name, a secondary email address (not wanka95@gmail.com), Zone 5
3. Click "Send My Zone Card"
4. Confirm: test email receives Email 1 with Zone 5 PDF download button
5. Confirm: PDF download button works and opens the Zone 5 card
6. Confirm: test subscriber appears in Kit with tag "zone-5" applied
7. Confirm: Kit shows Email 2 scheduled for Day 2 after sign-up

### Test 2 — Zone 7

Repeat Test 1 with Zone 7 selected. Zone 7 is the most populous US zone — testing it
separately confirms the routing logic works for a different zone.

### Test 3 — Behavioral Tags (Email 3 Link)

1. In Kit, manually send Email 3 to your test email
2. Click the Seed Saving Field Manual link in Email 3
3. Confirm: test subscriber now has "seed-saver" tag applied in Kit
4. If tag is not applied: re-check the click-tracking setup on that link in Email 3

### Test Result Log

| Test | Date | Result | Notes |
|---|---|---|---|
| Zone 5 full flow | | | |
| Zone 7 full flow | | | |
| Email 3 behavioral tag | | | |

Record test dates and results here. Do not go live (add landing page URL to social bios)
until all three tests pass.

---

## Step 7: Merge Field Reference

Kit personalizes emails using merge fields. These are the merge fields used in the welcome sequence:

| Merge Field | What It Inserts | Used In |
|---|---|---|
| `{{ subscriber.first_name }}` | Subscriber's first name from sign-up form | Emails 1, 2, 3, 4, 5 (opening line) |
| `{{ subscriber.fields.zone }}` | Zone number from dropdown selection | Email 1 only |
| `[ZONE-PDF-LINK]` | Google Drive download URL (per zone variant) | Email 1 only |

**Fallback for first name**: If subscriber did not enter a name, Kit uses a fallback. Set the
fallback to "there" — so the email reads "Hi there" instead of "Hi [First Name]."

In Kit: when inserting the merge field for first name, click the field > set fallback value > type "there"

---

## Step 8: Post-Launch Monitoring

Pull these metrics every Friday for the first 4 weeks. Log in WORKLOG.md.

| Metric | Week 2 Target | Week 4 Target | Where to Find |
|---|---|---|---|
| Total subscribers | 10+ | 50+ | Kit dashboard > Subscribers |
| Email 1 open rate | 60%+ | 60%+ | Kit > Broadcasts or Automations > Email 1 |
| Email 1 click rate | 40%+ (PDF download) | 40%+ | Same |
| Email 3 click rate | 20%+ (seed saver link) | 20%+ | Kit > Email 3 |
| Subscribers with cohort tags | Any | 30%+ of list | Kit > Subscribers > filter by tag |

**If Email 1 open rate falls below 40%**: Review subject line. Subject line carries 80% of the
open-rate weight. "Your Zone 5 Quick-Start Card is ready" is direct and specific — if opens are
low, check that the email is not landing in spam (send test from a different email provider).

**If PDF download click rate falls below 30%**: The button is not visible enough. Increase
button size and change button color to #143b28 (Deep Forest Green) with white text.

---

## Segmentation Rules — Future Newsletter Use

Once the list reaches 50+ subscribers, the cohort tags enable segmented newsletters:

| Segment | Tag | Newsletter Angle |
|---|---|---|
| Seed savers | seed-saver | Lead with seed saving content; feature Seed Saving Manual and Heirloom Guide |
| City growers | city-grower | Lead with apartment/container content; feature Container Blueprint and Apartment Guide |
| Preservationists | preservationist | Lead with harvest and fermentation content; feature Preservation and Fermented Harvest handbooks |
| Untagged | (no cohort tag) | Mixed content covering all product lines |

Do not segment newsletters before the list reaches 50 subscribers — small segment sizes
produce statistically meaningless data and the personalization effort is not worth it at
low volumes.

---

## Setup Completion Log

Update this table as each step is completed:

| Step | Status | Date Completed | Notes |
|---|---|---|---|
| Kit account created | NOT STARTED | | |
| All 15 tags created | NOT STARTED | | |
| Landing page built and published | NOT STARTED | | |
| Landing page URL recorded | NOT STARTED | | |
| Landing page URL added to social bios | BLOCKED — social accounts not yet created | | |
| Zone PDFs uploaded to Google Drive | BLOCKED — zone cards not yet built | | |
| Zone PDF download links recorded | BLOCKED — Google Drive upload pending | | |
| Email 1 — Zone 5 variant built | NOT STARTED | | |
| Email 1 — Zone 6 variant built | NOT STARTED | | |
| Email 1 — Zones 3, 4, 7, 8 built | NOT STARTED | | |
| Email 1 — Zones 9, 10 built | NOT STARTED | | |
| Email 2 built | NOT STARTED | | |
| Email 3 built (with behavioral tag link) | NOT STARTED | | |
| Email 4 built (with 3 tag links) | NOT STARTED | | |
| Email 5 built (with coupon code) | NOT STARTED | | |
| Zone routing automation wired | NOT STARTED | | |
| End-to-end test — Zone 5 | NOT STARTED | | |
| End-to-end test — Zone 7 | NOT STARTED | | |
| Behavioral tag test (Email 3) | NOT STARTED | | |
| Landing page linked from all social bios | BLOCKED — social accounts not yet created | | |

---

*Prepared: 2026-05-05. Session 728. Platform: Kit (kit.co). Full email copy: marketing/email-and-launch-plan.md.
Additional Email 1-3 copy: MAY_CONTENT_EXECUTION_PLAN.md. Zone card PDF output: projects/seedwarden/assets/zone-cards/.
Coupon code: SEEDWARDEN15.*
