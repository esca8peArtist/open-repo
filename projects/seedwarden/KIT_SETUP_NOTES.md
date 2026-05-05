---
title: "Kit Email Automation — Setup Notes and Platform Configuration"
date: 2026-05-05
session: 724
status: setup-guide-ready — user account creation required
platform: Kit (kit.co, formerly ConvertKit)
references:
  - PHASE_2_EMAIL_STRATEGY.md (full email strategy and sequence copy locations)
  - ZONE_QUICKSTART_CARD_SPEC.md (zone card format and delivery spec)
  - CANVA_ZONE_CARD_BATCH_WORKFLOW.md (zone card content for all 8 zones)
  - marketing/email-and-launch-plan.md (full 5-email welcome sequence copy)
---

# Kit Email Automation Platform — Setup Notes

**Purpose**: Step-by-step configuration guide for setting up Kit (kit.co) as the email
automation platform for the Zone Quick-Start Card lead magnet funnel. All decisions about
platform architecture, segmentation, and email content are made here — the remaining work
is clicking through Kit's UI following these instructions.

**Time required**: 30–60 minutes for initial account setup and landing page creation.
Additional 2–3 hours to build the full 5-email welcome sequence (can be done in stages).

---

## Step 1: Account Creation

1. Go to kit.co and click "Start for free"
2. Enter email: wanka95@gmail.com
3. Set sender name: Seedwarden
4. Set sender email: wanka95@gmail.com (can update to a custom domain later if one is set up)
5. Time zone: set to your local time zone
6. Business type: select "Creator" or "E-commerce" — either works for this use case

**Free tier limits** (confirmed adequate for Phase 2):
- Up to 10,000 subscribers (more than sufficient for launch)
- Unlimited email sends
- 1 landing page (sufficient — one page covers all 8 zone sign-up variants)
- Basic automations — conditional logic for zone routing is available on free tier

---

## Step 2: Subscriber Segmentation Setup — Tags

Create these tags before building any automation. Tags are applied automatically based on
subscriber behavior and used to route newsletter content.

### Tags to Create (Kit > Subscribers > Tags > Add a Tag)

| Tag Name | Applied When | Used For |
|---|---|---|
| zone-3 | Subscriber selects Zone 3 on sign-up form | Zone card email routing |
| zone-4 | Subscriber selects Zone 4 | Zone card email routing |
| zone-5 | Subscriber selects Zone 5 | Zone card email routing |
| zone-6 | Subscriber selects Zone 6 | Zone card email routing |
| zone-7 | Subscriber selects Zone 7 | Zone card email routing |
| zone-8 | Subscriber selects Zone 8 | Zone card email routing |
| zone-9 | Subscriber selects Zone 9 | Zone card email routing |
| zone-10 | Subscriber selects Zone 10 | Zone card email routing |
| seed-saver | Subscriber clicks Seed Saving Manual link in Email 3 OR food sovereignty link in Email 4 | Newsletter segmentation |
| city-grower | Subscriber clicks apartment/container link in Email 4 | Newsletter segmentation |
| preservationist | Subscriber clicks preservation link in Email 4 | Newsletter segmentation |
| forager | Subscriber clicks wild plants or foraging link (any email) | Newsletter segmentation — add if foraging content is featured |
| prepper | Subscriber clicks survival/livestock link (any email) | Newsletter segmentation |
| homesteader | Subscriber clicks livestock or homestead link (any email) | Newsletter segmentation |
| gift-buyer | Apply manually after Phase 1 Etsy data shows gift purchase patterns | Holiday campaign segmentation |
| etsy-buyer | Applied via Etsy purchase integration or manual import | Post-purchase sequence trigger |

**Note on cohort tags**: The four primary audience cohorts (foragers, preppers, homesteaders,
gift-buyers) are identified by click behavior in the welcome sequence. Do not ask subscribers
to self-identify on the sign-up form — the form asks zone only. The tags are earned by what
the subscriber clicks, not what they say they are.

---

## Step 3: Landing Page Setup

### Page Configuration

1. In Kit, go to Landing Pages and Forms > Create New > Landing Page
2. Select a simple single-column template (minimal is better — Seedwarden's audience is not
   drawn to polished marketing aesthetics)
3. Configure these fields:

**Page headline**: "Your Free Zone Quick-Start Card"

**Page subheadline**: "Know exactly what to plant, when to plant it, and what to do right
now in your zone — one-page reference card, free."

**Form fields** (two fields only — each additional field reduces conversion 10–15%):
- First name (required)
- Email address (required)
- Growing zone (dropdown, required) — values: Zone 3, Zone 4, Zone 5, Zone 6, Zone 7,
  Zone 8, Zone 9, Zone 10

**CTA button text**: "Send My Zone Card"

**Below the button** (trust text, small font): "No spam. Unsubscribe anytime. Seedwarden
sends one email per week about growing, foraging, and real food."

**Background color**: match brand cream (#F5EDD6) or white — whatever the template supports
without custom CSS. Exact brand color is a Phase 3 improvement.

4. Publish the landing page and copy the URL
5. Add the landing page URL to the social media bios (Instagram, TikTok, Pinterest)
6. Update `social-media-setup.md` with the live Kit landing page URL

---

## Step 4: Zone Routing Automation

This automation sends the correct zone card PDF to each subscriber based on their zone
selection. Build this before any welcome sequence emails.

### How to Build Zone Routing in Kit (Free Tier)

Kit's free tier supports conditional email content via custom fields. The zone dropdown on
the sign-up form creates a custom field called "zone" (or whatever you name it). Use this
field in Email 1 to insert the correct download link.

**Option A (simpler — recommended for launch)**: Create 8 variants of Email 1, one per zone.
Use Kit's automation rules: "If subscriber has tag zone-5, send Email 1 Zone 5 variant."

Build order: Start with Zone 5 (most subscribers statistically), then Zone 6, then outward.

**Option B (advanced)**: Use Kit's liquid tags to insert the zone-specific PDF URL dynamically
in a single Email 1 template. This requires correct custom field mapping and is more fragile.
Use Option A for launch; migrate to Option B after the first 100 subscribers if desired.

### PDF Upload Process

Zone card PDFs are built in Canva and exported to `projects/seedwarden/assets/zone-cards/`.
Upload each PDF to Kit's "Deliverables" or file hosting. Kit does not host files directly —
use one of these methods:

**Recommended**: Upload each zone card PDF to Google Drive, set sharing to "Anyone with the
link can view," and copy the direct download link. Use that Google Drive link as the download
link in each zone-specific Email 1 variant.

**Alternative**: Upload to Dropbox or any file host. The link just needs to be a direct
download URL that works without the subscriber logging in to anything.

**File naming for uploads**:
- zone-3-quick-start-card.pdf
- zone-4-quick-start-card.pdf
- zone-5-quick-start-card.pdf
- zone-6-quick-start-card.pdf
- zone-7-quick-start-card.pdf
- zone-8-quick-start-card.pdf
- zone-9-quick-start-card.pdf
- zone-10-quick-start-card.pdf

Zone cards are not yet built — this is the Canva step. PDFs will be produced following
`CANVA_ZONE_CARD_DESIGN_GUIDE.md`. Upload links once PDFs are exported.

---

## Step 5: Welcome Sequence — Build Order

Full copy for all 5 emails is in `marketing/email-and-launch-plan.md`. Build in this order:

| Email | Day | Action |
|---|---|---|
| Email 1 — Zone Card Delivery | Day 0 | Build 8 zone variants. Each contains the subscriber's first name, zone number, and the zone-specific PDF download link. This is the delivery email — build it first. |
| Email 2 — Heirloom Seed Philosophy | Day 2 | Single version, all subscribers. Educational. No product links. |
| Email 3 — Seed Saving Story | Day 5 | Single version. Include tracked link to Seed Saving Field Manual — subscribers who click receive "seed-saver" tag automatically. |
| Email 4 — Catalog Introduction | Day 7 | Single version. Three segmentation links (apartment/container, seed saving/food sovereignty, food preservation). Each click applies the corresponding tag. |
| Email 5 — First Offer | Day 10 | Single version. Coupon code: SEEDWARDEN15 (15% off, 5-day window). Product recommendations based on Phase 1 conversion data if available. |

**Do not build the post-purchase sequence or win-back campaign before the list reaches 200
subscribers.** Those are Phase 3 automations.

---

## Step 6: End-to-End Test

Before the landing page goes live and linked from social bios, test the full flow:

1. Open the landing page in an incognito window
2. Sign up using a test email address (not wanka95@gmail.com — use a secondary email)
3. Select Zone 5 from the dropdown
4. Confirm: test email receives Email 1 with Zone 5 PDF download link
5. Confirm: subscriber appears in Kit with zone-5 tag applied
6. Confirm: PDF download link opens the Zone 5 card correctly
7. Confirm: subscriber will receive Email 2 at Day 2 (check automation schedule in Kit)

**Test result status**: Not yet completed — account not yet created.

---

## Platform Notes

**Kit free tier limitations that affect Phase 2**:
- No A/B testing on landing pages (Phase 3 feature)
- No custom domain for the landing page URL (the URL will be kit.com/seedwarden or similar)
- No visual email editor in all free plan versions — check current free tier scope at kit.co
  before assuming rich editing is available

**Custom domain**: If `seedwarden.com` is registered, it can be pointed to the Kit landing
page. If not yet registered, the kit.co URL is sufficient for launch.

---

## Setup Completion Log

| Step | Status | Date Completed | Notes |
|---|---|---|---|
| Kit account created | NOT STARTED | | |
| Tags created (all 15) | NOT STARTED | | |
| Landing page built and published | NOT STARTED | | |
| Landing page URL added to social bios | NOT STARTED | | |
| Zone PDFs uploaded to file host | BLOCKED — zone cards not yet built | | Unblocked after Canva zone card production |
| Email 1 (8 zone variants) built | NOT STARTED | | |
| Email 2 built | NOT STARTED | | |
| Email 3 built | NOT STARTED | | |
| Email 4 built | NOT STARTED | | |
| Email 5 built | NOT STARTED | | |
| End-to-end test completed | NOT STARTED | | |
| Landing page linked from all 3 social bios | BLOCKED — accounts not yet created | | |

---

*Prepared: 2026-05-05. Platform: Kit (kit.co). Email copy location: marketing/email-and-launch-plan.md.
Zone card content location: CANVA_ZONE_CARD_BATCH_WORKFLOW.md. Session 724.*
