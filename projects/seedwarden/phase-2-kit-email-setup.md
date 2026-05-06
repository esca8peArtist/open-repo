---
title: "Phase 2 Kit Email Setup Guide"
subtitle: "5-email welcome sequence, zone routing, segmentation, testing protocol — field-by-field setup"
date: 2026-05-06
status: production-ready
platform: Kit (kit.co)
references:
  - TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md
  - KIT_SETUP_NOTES.md
  - marketing/email-and-launch-plan.md
  - MAY_CONTENT_EXECUTION_PLAN.md
---

# Phase 2 Kit Email Setup Guide

**Purpose**: Field-by-field setup instructions for the entire Kit email infrastructure. Every click path is specified. Every field value is given. You are following a recipe, not making decisions.

**Total time**: 3-4.5 hours, done in stages:
- Stage 1 (May 6): Account creation + landing page (60 min)
- Stage 2 (May 6): All 15 tags (15 min)
- Stage 3 (May 16): All 5 emails built (2-2.5 hrs)
- Stage 4 (May 16): Zone routing automation wired (30 min)
- Stage 5 (May 23): End-to-end tests, go-live (45 min)

**Platform**: Kit (kit.co), free tier. Supports up to 10,000 subscribers with full automation and conditional routing.

---

## Stage 1: Account Creation and Landing Page (May 6, 60 min)

### Step 1.1: Create Kit Account

1. Go to kit.co
2. Click "Start for free"
3. Enter email: wanka95@gmail.com
4. Sender name: `Seedwarden`
5. Sender email: wanka95@gmail.com (migrate to custom domain before list reaches 500 subscribers)
6. Time zone: your local time zone
7. Business type: "Creator" or "E-commerce" — either works
8. Complete email verification if prompted

**Free tier confirms**:
- Up to 10,000 subscribers
- Unlimited email sends
- 1 landing page (sufficient — all 8 zone variants route through one page)
- Conditional logic for zone routing (fully supported on free tier)

---

### Step 1.2: DNS Authentication (Do Now — Takes 24-48h to Propagate)

Without these DNS records, welcome emails land in spam at a high rate. Add them immediately after account creation so they are propagated before the first real subscriber signs up.

**SPF record** (prevents email spoofing):
1. Log into your domain registrar (Namecheap, GoDaddy, Google Domains, or wherever your domain is registered)
2. Navigate to DNS management for your domain
3. Add a TXT record:
   - Name/Host: `@` (or leave blank, depending on registrar)
   - Value: `v=spf1 include:sendgrid.net ~all`
   - TTL: 3600 (or "Automatic")
4. Save

**If an SPF record already exists** (for Gmail or another service): merge it. Do not add two separate SPF records. Example merge:
- Existing: `v=spf1 include:_spf.google.com ~all`
- After merge: `v=spf1 include:_spf.google.com include:sendgrid.net ~all`

**DKIM record** (email authentication):
1. In Kit: Settings > Email Settings > DKIM Signing
2. Kit displays a CNAME record — copy the Name and Value exactly
3. In your domain registrar: add a CNAME record with the Name and Value from Kit
4. Save
5. Return to Kit > Settings > Email Settings: both SPF and DKIM should show a green checkmark within 24-48 hours

**If no custom domain exists**: Use wanka95@gmail.com as sender address. Gmail provides basic deliverability without custom DNS. This is acceptable for launch. Migrate before the list reaches 500 subscribers.

---

### Step 1.3: Landing Page Build

Navigate to: Kit > Landing Pages and Forms > Create New > Landing Page

Select a minimal single-column template. Configure every field as follows:

**Page title/headline**:
```
Your Free Zone Quick-Start Card
```
Font: use the template's heading font (Kit's template defaults are fine — zone card aesthetic is handled by the PDF, not the landing page)

**Page subheadline**:
```
Know exactly what to plant, when to plant it, and what to do right now in your zone —
one-page reference card, free.
```

**Form fields** (add exactly three — each additional field reduces conversion 10-15%):

| Field | Type | Required | Details |
|---|---|---|---|
| First name | Text | Yes | Label: "First name" |
| Email address | Email | Yes | Label: "Email" |
| Growing zone | Dropdown | Yes | Label: "Your growing zone" — add values: Zone 3, Zone 4, Zone 5, Zone 6, Zone 7, Zone 8, Zone 9, Zone 10 |

**CTA button text**:
```
Send My Zone Card
```
Button color: set to #143b28 (Deep Forest Green) if the template allows custom hex. Otherwise use the darkest green in the template palette.

**Trust text** (small text below the button):
```
No spam. Unsubscribe anytime. Seedwarden sends one email per week about growing,
foraging, and real food.
```

**Background color**: #F5EDD6 (Warm Cream) if the template accepts a hex input. If not available, use white.

**Confirmation / thank-you message** (what subscribers see after clicking the button):
```
Your zone card is on its way! Check your inbox in the next 60 seconds.
Add seedwarden@gmail.com to your contacts to keep it out of spam.
```

### Publish and Record the URL

1. Click Publish
2. Copy the full landing page URL (format: something like kit.com/seedwarden/zone-card or app.kit.com/landing-pages/[ID])
3. Record this URL in three places immediately:
   - KIT_SETUP_NOTES.md — "Landing Page URL: _____" field
   - Instagram bio link field
   - TikTok bio link field
   - Pinterest website field
4. Also add to CANVA_SETUP_STATUS.md footer placeholder (replaces [KIT-LANDING-PAGE-URL] in zone cards before export)

**Done signal**: Landing page is live at a public URL. Visiting the URL shows the form with First Name, Email, and Zone dropdown. The URL is added to all social bios.

---

## Stage 2: All 15 Tags (May 6, 15 min)

Tags must exist before building any automation. Create them all in one session.

Navigate to: Kit > Subscribers > Tags > "Add a tag" (one at a time)

**Zone tags (create all 8)**:

| Tag Name | When Applied |
|---|---|
| zone-3 | Subscriber selects Zone 3 on sign-up form |
| zone-4 | Subscriber selects Zone 4 |
| zone-5 | Subscriber selects Zone 5 |
| zone-6 | Subscriber selects Zone 6 |
| zone-7 | Subscriber selects Zone 7 |
| zone-8 | Subscriber selects Zone 8 |
| zone-9 | Subscriber selects Zone 9 |
| zone-10 | Subscriber selects Zone 10 |

**Interest cohort tags (create all 4)**:

| Tag Name | When Applied |
|---|---|
| seed-saver | Subscriber clicks Seed Saving Field Manual link in Email 3 or food sovereignty link in Email 4 |
| city-grower | Subscriber clicks apartment/container link in Email 4 |
| preservationist | Subscriber clicks preservation link in Email 4 |
| forager | Subscriber clicks wild plants or foraging link in any email |

**Lifecycle tags (create all 3)**:

| Tag Name | When Applied |
|---|---|
| new-subscriber | Applied at form submission (via automation action) |
| etsy-buyer | Applied via manual import after a confirmed Etsy purchase |
| gift-buyer | Applied manually for subscribers identified as buying for another person |

**Done signal**: Kit > Subscribers > Tags shows all 15 tags listed.

---

## Stage 3: Welcome Sequence — All 5 Emails (May 16, 2-2.5 hrs)

Navigate to: Kit > Sequences > New Sequence > Name: "Seedwarden Welcome"

Build in this order: Email 5 first (so the sequence delay is set up in reverse and Email 1 is built last when you have the most context), then work backward. Actually — build in chronological order for sanity: Email 1 through Email 5.

---

### Email 1 — Zone Card Delivery (Day 0, Immediate Send)

Build 8 variants of this email, one per zone. Each variant is identical except for three elements: zone number in subject line, zone number in opening sentence, and PDF download link.

**Start with Zone 5** (test zone — highest US population):

In Kit > Sequence > Add Email:

**Subject line**:
```
Your Zone 5 Quick-Start Card is ready, {{ subscriber.first_name | default: "there" }}
```

**Preview text**:
```
One page. Everything you need for your zone right now.
```

**Email body** (copy from marketing/email-and-launch-plan.md Email 1, substituting [X] = 5):

Opening paragraph:
```
Hi {{ subscriber.first_name | default: "there" }},

Your Zone 5 Quick-Start Card is ready — I put it below as a direct download link.
One page with your frost dates, the best crops to start right now, and a variety
that performs consistently in Zone 5.
```

**Download button** (this is the critical element):
- Button text: "Download Your Zone 5 Card"
- Button link: `[ZONE-5-PDF-URL]` — use this exact placeholder during the initial build. You will replace it with the actual Google Drive download URL on May 22.
- Button color in Kit editor: #143b28 (Deep Forest Green) if available
- Button style: full-width for mobile

Remaining body copy: paste from marketing/email-and-launch-plan.md Email 1 section.

Closing:
```
More soon,
Seedwarden
```

**Delay setting**: Send immediately (no delay — this is the first email in the sequence, triggered at form submit)

**After building Zone 5 variant**: duplicate the email 7 times for the remaining zones. For each duplicate:
- Change subject line zone number (Zone 3, Zone 4, Zone 6, Zone 7, Zone 8, Zone 9, Zone 10)
- Change opening sentence zone number
- Change download button text zone number
- Change button link placeholder to [ZONE-[N]-PDF-URL]

Zone variant naming in Kit (for your organization):
- Email 1 — Zone 5
- Email 1 — Zone 6
- Email 1 — Zone 3
(etc.)

**Internal tag note on each variant**: Add an internal note or label in Kit associating each variant with its zone. This makes automation wiring in Stage 4 easier.

---

### Email 2 — Heirloom Seed Philosophy (Day 2 delay)

**Subject line**: (from marketing/email-and-launch-plan.md Email 2 — copy exactly)

**Preview text**: (from the same source)

**Key rules for Email 2**:
- Single version — all subscribers receive this same email regardless of zone
- No tracked links
- No product links or store URLs
- No CTAs to buy anything
- Purpose: build brand authority through education before any catalog mention
- Delay setting: "Send 2 days after subscriber joins sequence"

**Body**: Full copy from marketing/email-and-launch-plan.md Email 2 section.

---

### Email 3 — Seed Saving Story (Day 5 delay)

**Subject line**: (from marketing/email-and-launch-plan.md Email 3)

**Key rules for Email 3**:
- Single version — all subscribers
- Contains one behavioral tracking link
- Delay setting: "Send 5 days after subscriber joins sequence"

**The behavioral tracking link (critical — set up this way)**:
- Link destination: the Etsy listing URL for the Seed Saving Field Manual
- In Kit: when creating this link, enable "Click Trigger" or "Add Tag on Click"
- Select tag: `seed-saver`
- This means: every subscriber who clicks this link automatically receives the "seed-saver" tag in their Kit profile
- Verify: in Kit's link editor, the tag icon shows next to the link confirming the trigger is active

**Body**: Full copy from marketing/email-and-launch-plan.md Email 3 section.

**Why Email 3 matters**: Open rate on Email 3 is the single best leading indicator for Email 5 coupon redemption. Subscribers who open Email 3 and click are the highest-intent segment. If Email 3 open rate falls below 30%, flag for subject line review.

---

### Email 4 — Catalog Introduction (Day 7 delay)

**Subject line**: (from marketing/email-and-launch-plan.md Email 4)

**Key rules for Email 4**:
- Single version — all subscribers
- Contains three behavioral tracking links (each applies a different cohort tag)
- Delay setting: "Send 7 days after subscriber joins sequence"

**Three behavioral tracking links**:

| Link Destination | Tag Applied on Click | Label in Kit |
|---|---|---|
| Apartment/container growing products (Etsy listing URL or category page) | city-grower | "apartment-link" |
| Seed saving / food sovereignty products (Etsy listing URL) | seed-saver | "seed-saver-link" |
| Food preservation products (Etsy listing URL) | preservationist | "preservation-link" |

Set up each link with "Add Tag on Click" enabled, each pointing to the correct tag.

**UTM parameters for revenue attribution** (add to each Etsy URL before embedding):
```
?utm_source=kit&utm_medium=email&utm_campaign=welcome-sequence&utm_content=email4-[link-type]
```

Example for the apartment link:
```
https://www.etsy.com/listing/[ID]/container-growing-blueprint-pack?utm_source=kit&utm_medium=email&utm_campaign=welcome-sequence&utm_content=email4-apartment-link
```

Build UTM URLs at: ga-dev-tools.google.com/campaign-url-builder

**Body**: Full copy from marketing/email-and-launch-plan.md Email 4 section.

---

### Email 5 — First Offer (Day 10 delay)

**Subject line**: (from marketing/email-and-launch-plan.md Email 5)

**Key rules for Email 5**:
- Single version — all subscribers
- Contains the SEEDWARDEN15 coupon code
- Delay setting: "Send 10 days after subscriber joins sequence"
- The coupon must be active in Etsy before the first subscriber reaches Day 10 (first possible Day 10 is May 16 if the first subscriber signs up on May 6)

**Coupon copy to include in email body**:
```
Use code SEEDWARDEN15 at checkout for 15% off any guide.
This is good for the next 5 days.
```

**Product recommendations** (default — update when Phase 1 conversion data is available):
1. Seed Saving Field Manual — best fit for new growers (most versatile product)
2. Zone-by-Zone Seed Starting Calendar — best fit for planners
3. Harvest Preservation Field Manual — best fit for food-focused subscribers

**Framing note**: Do not use countdown timer language or scarcity phrasing. Seedwarden's audience is sophisticated about marketing tactics and countdown language erodes trust. The copy frames the offer as "something I don't usually do" rather than a sales mechanism.

**Body**: Full copy from marketing/email-and-launch-plan.md Email 5 section.

---

## Stage 4: Zone Routing Automation (May 16, 30 min)

Navigate to: Kit > Automations > Create Automation

**Automation name**: Seedwarden Welcome

**Trigger**: "When subscriber completes a form" > select the Zone Quick-Start Card landing page form

**Automation steps** (add in this order):

**Step 1**: Add tag "new-subscriber" to all subscribers (applies regardless of zone)

**Step 2**: Conditional routing based on zone dropdown value

Kit automation conditional logic setup:
- Add a "Conditional" step
- Condition: "Subscriber's field 'Growing Zone' is equal to 'Zone 5'"
- If TRUE: send "Email 1 — Zone 5" variant
- Repeat this for all 8 zones as separate conditions

Structure in Kit:
```
Trigger: Form submitted (Zone Card landing page)
  ↓
Action: Add tag "new-subscriber"
  ↓
Branch: If zone = Zone 3 → Send Email 1 Zone 3 variant
Branch: If zone = Zone 4 → Send Email 1 Zone 4 variant
Branch: If zone = Zone 5 → Send Email 1 Zone 5 variant
Branch: If zone = Zone 6 → Send Email 1 Zone 6 variant
Branch: If zone = Zone 7 → Send Email 1 Zone 7 variant
Branch: If zone = Zone 8 → Send Email 1 Zone 8 variant
Branch: If zone = Zone 9 → Send Email 1 Zone 9 variant
Branch: If zone = Zone 10 → Send Email 1 Zone 10 variant
  ↓ (all branches converge)
Action: Add to "Seedwarden Welcome" sequence (starting at Email 2)
```

Note: Email 1 (the zone-specific email) is sent via the automation branch. Emails 2-5 are standard sequence emails that all subscribers receive regardless of zone. The sequence starts at Email 2 after the automation delivers Email 1.

**Kit automation also applies zone tag**: In each branch condition, add an action: "Add tag [zone-N]" so subscribers are tagged with their zone for future segmentation.

**Save as draft — do NOT publish until end-to-end test passes**.

---

## Stage 5: End-to-End Tests and Go-Live (May 23, 45 min)

Do not publish the automation or link the landing page from social bios until all 3 tests pass.

### Test 1 — Zone 5 Full Flow

1. Open Kit landing page in an incognito browser window
2. Fill in:
   - First name: "Test"
   - Email: your secondary email address (NOT wanka95@gmail.com — use a Gmail + alias like wanka95+test1@gmail.com or a separate email account)
   - Growing zone: Zone 5
3. Click "Send My Zone Card"
4. Open the test email inbox
5. Confirm:
   - [ ] Email 1 arrives within 60 seconds
   - [ ] Subject line reads "Your Zone 5 Quick-Start Card is ready"
   - [ ] Email contains a download button
   - [ ] Clicking the download button downloads a PDF (not a viewer, not a "request access" page)
   - [ ] The downloaded PDF is the Zone 5 card (check the zone number in the header)
   - [ ] Email did NOT land in spam (check the Spam folder too)
6. In Kit > Subscribers: confirm the test subscriber shows:
   - [ ] Tags: "zone-5" and "new-subscriber" applied
   - [ ] Email 2 scheduled for 2 days from now

### Test 2 — Zone 7 Full Flow

Repeat Test 1 with Zone 7 selected and a different test email address (wanka95+test2@gmail.com). Zone 7 is the most populous US zone — testing it separately confirms routing logic works for a different conditional branch.

### Test 3 — Email 3 Behavioral Tag

1. In Kit > Sequences > Seedwarden Welcome: find Email 3 in the sequence
2. Click "Send a test" (Kit allows manually sending a sequence email to a test address)
3. Send Email 3 to wanka95@gmail.com or the test address
4. Open the email and click the Seed Saving Field Manual link
5. In Kit > Subscribers: confirm the test subscriber now has "seed-saver" tag applied
6. If tag is not applied: check that the click trigger was set up correctly on that link in Email 3 (Kit > Sequence > Email 3 > the link element should show a tag icon or click trigger indicator)

### Test Result Log (fill in after each test)

| Test | Date Completed | Pass/Fail | Notes |
|---|---|---|---|
| Zone 5 full flow | | | |
| Zone 7 full flow | | | |
| Email 3 behavioral tag | | | |

### Go-Live (After All 3 Tests Pass)

1. Kit > Automations > Seedwarden Welcome > click "Publish" (changes status from Draft to Active)
2. Verify: automation shows "Published" or "Active" status (not Draft, not Paused)
3. The landing page is now live and delivering zone cards to real subscribers automatically

---

## Stage 6: Pre-Launch Broadcast Setup (May 27-29)

### Stage the Launch Broadcast

Navigate to: Kit > Broadcasts > New Broadcast

**Subject line**:
```
Phase 2 is live — your zone card library just doubled
```

**Preview text**:
```
21 guides now with lifestyle photos, and something new in your zone.
```

**Send to**: "All Confirmed Subscribers" — NOT "All Subscribers" (unconfirmed subscribers hurt sender reputation and deliverability)

**Body**: paste from marketing/email-and-launch-plan.md > Section: "Launch Broadcast"

**Personalization**: Add `{{ subscriber.first_name | default: "there" }}` at the opening

**Schedule**: May 30, 12:00pm (your local time zone — confirm the Kit time zone is set to your local zone)

**Final step — THIS IS THE CRITICAL STEP**: Click "Schedule" or "Confirm Schedule" to move the broadcast from "Draft" to "Scheduled" status. A broadcast in Draft state does NOT send automatically. The status field must read "Scheduled" with the correct date and time visible before you navigate away.

**Verify on May 29 evening**: Kit > Broadcasts > confirm the launch broadcast shows "Scheduled — May 30 12:00pm." If it shows "Draft": click into it and confirm the schedule again.

---

## Merge Field Reference

Kit personalization fields used in the welcome sequence:

| Merge Field | What It Inserts | Fallback Value |
|---|---|---|
| `{{ subscriber.first_name }}` | Subscriber's first name | "there" (so email reads "Hi there") |
| `{{ subscriber.fields.zone }}` | Zone dropdown selection | "your zone" |
| `[ZONE-X-PDF-URL]` | Google Drive direct download URL | None — must be replaced before go-live |

**Setting the first name fallback in Kit**: When inserting the merge field for first name in the email editor, click the field > "Set fallback" > type "there" > confirm. This applies to every email in the sequence.

---

## Segmentation Rules for Post-Launch Newsletters

Once the list reaches 50 subscribers, cohort tags enable segmented newsletters. Do not segment before 50 — small segment sizes produce meaningless data.

| Segment | Tag | Newsletter Lead Topic |
|---|---|---|
| Seed savers | seed-saver | Seed saving content; Seed Saving Manual + Heirloom Guide spotlight |
| City growers | city-grower | Apartment/container content; Container Blueprint + Apartment Guide spotlight |
| Preservationists | preservationist | Harvest and fermentation content; Preservation + Fermented Harvest spotlight |
| Untagged | (no cohort tag) | Mixed content covering all product lines |

---

## Setup Completion Log

Update this table as each step is completed:

| Step | Status | Date | Notes |
|---|---|---|---|
| Kit account created | | | |
| DNS SPF record added | | | |
| DNS DKIM record added | | | |
| All 15 tags created | | | |
| Landing page built and published | | | |
| Landing page URL recorded in all 3 social bios | | | |
| Email 1 — Zone 5 variant built | | | |
| Email 1 — Zone 6 variant built | | | |
| Email 1 — Zones 3, 4, 7, 8 built | | | |
| Email 1 — Zones 9, 10 built | | | |
| Email 2 built | | | |
| Email 3 built (with seed-saver click trigger) | | | |
| Email 4 built (with 3 cohort click triggers) | | | |
| Email 5 built (with SEEDWARDEN15 coupon) | | | |
| Zone routing automation wired (draft) | | | |
| End-to-end test Zone 5: PASS | | | |
| End-to-end test Zone 7: PASS | | | |
| Behavioral tag test (Email 3): PASS | | | |
| Kit automation PUBLISHED | | | |
| All 8 zone PDF URLs replaced in Email 1 variants | | | |
| Launch broadcast staged and SCHEDULED (May 30 12pm) | | | |

---

## Monitoring — Week 1 Post-Launch

Pull these metrics every evening for Days 1-7. Log in WORKLOG.md.

| Metric | Target | Below-Target Action |
|---|---|---|
| Total subscribers | 50+ by Day 7 | Review bio link placement on all 3 platforms; test alternate CTA wording in Instagram bio |
| Email 1 open rate | 60%+ | If below 40%: check spam placement. Send a test from Kit to wanka95@gmail.com and confirm it lands in inbox. |
| Email 1 download click rate | 40%+ | If below 30%: the download button is not visible enough. Increase button size and darken button to #143b28 with white text. |
| Email 3 open rate | 40%+ | Leading indicator for Email 5 redemptions. If below 30%: review Email 3 subject line. |
| Subscribers with cohort tags | 20%+ of list by Day 7 | Click-through on Emails 3-4 is low. Make links larger and more prominent in those emails. |
| Email 5 coupon redemptions | 8-15% of Email 5 recipients | If 0 redemptions: confirm SEEDWARDEN15 coupon is active in Etsy. Confirm the coupon code is spelled correctly in the email body. |

---

*Prepared: 2026-05-06. Sources: TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md, KIT_SETUP_NOTES.md, marketing/email-and-launch-plan.md, MAY_CONTENT_EXECUTION_PLAN.md. This guide consolidates all Kit platform setup instructions with field-level specificity for the Phase 2 launch.*
