---
title: "Phase 2 Email Strategy — Production Plan"
date: 2026-04-30
status: production-ready
context: Phase 2, Track B — email sequence production planning and platform setup
references:
  - email-growth-playbook.md (list-building strategy, KPI gates, subscriber targets)
  - marketing/email-automation-blueprint.md (all 5 automations, full technical setup)
  - marketing/email-and-launch-plan.md (welcome sequence full copy, all 5 emails)
  - ZONE_CARD_PRODUCTION_TIMELINE.md (Zone Quick-Start Card build schedule)
  - PHOTO_SHOOT_PLANNING.md (lifestyle photo release schedule)
  - ZONE_QUICKSTART_CARD_SPEC.md (zone card content spec)
---

# Phase 2 Email Strategy — Production Plan
## Seedwarden Track B — Email Sequence, Platform Setup, and Release Coordination

**Purpose**: This document consolidates the email work stream for Phase 2 Track B into a single production plan. The email copy, automation architecture, list-building tactics, and KPI framework all exist in the reference documents above — this document does not repeat them. Instead it serves three functions:

1. Maps each email in the sequence to its corresponding zone card variant and photo release
2. Defines the platform setup sequence (Kit account through live automation)
3. Provides the production order so email, zone card, and photography work streams stay coordinated

All three work streams (email, zone cards, photography) share a production dependency: the Zone Quick-Start Card is the lead magnet that feeds the email list. Zone cards must be production-ready before the email list-building funnel goes live. Photography assets are not required for the email funnel to launch — they improve it but do not block it.

---

## Part 1: Email Sequence Structure

### Overview of the Full Sequence

Seedwarden runs five distinct email automations, documented in full in `marketing/email-automation-blueprint.md`. The Phase 2 production priority order is:

| Priority | Automation | Trigger | Purpose |
|---|---|---|---|
| 1 | Welcome Sequence (5 emails) | Lead magnet sign-up | Deliver zone card, build trust, make first offer |
| 2 | Post-Purchase Sequence (3 emails) | Etsy purchase tagged in Kit | Onboard buyer, cross-sell, request review |
| 3 | Weekly Newsletter | Subscriber completes welcome sequence | Ongoing relationship, seasonal product features |
| 4 | Win-Back Campaign (3 emails) | 6 consecutive unopened sends | Re-engage or cleanly remove inactive subscribers |
| 5 | Seasonal Campaign Broadcasts (5/year) | Manual sends | Revenue-generating promotional sends |

Build in this exact order. Automations 4 and 5 are Phase 3 work — do not build them before the list has 200+ subscribers.

### The 5-Email Welcome Sequence — Copy and Theme Summary

Full copy for all 5 emails is in `marketing/email-and-launch-plan.md`. The summary below is for production coordination — confirming theme alignment with zone card content and product catalog.

| Email | Day | Subject Theme | Copy Location | Content Alignment with Zone Card |
|---|---|---|---|---|
| 1 | 0 (immediate) | Deliver lead magnet + warm founder welcome | email-and-launch-plan.md Email 1 | Zone card download link is the primary CTA. Email body should name the subscriber's zone explicitly: "Your Zone [X] Quick-Start Card is ready." |
| 2 | 2 | Heirloom seed philosophy — Brandywine story | email-and-launch-plan.md Email 2 | No zone card reference. Educational. Builds brand authority before any catalog mention. |
| 3 | 5 | Seed saving mistake story — builds trust through vulnerability | email-and-launch-plan.md Email 3 | Include a behavioral tag link to the Seed Saving Field Manual (subscribers who click → tagged "seed-saver"). This is the first click-tracked link in the sequence. |
| 4 | 7 | Catalog introduction — why digital guides | email-and-launch-plan.md Email 4 | Three segmentation links: apartment/container → "city-grower" tag; seed saving/food sovereignty → "seed-saver" tag; food preservation → "preservationist" tag. Tags feed newsletter segmentation. |
| 5 | 10 | First offer — SEEDWARDEN15 coupon (15% off, 5-day window) | email-and-launch-plan.md Email 5 | Product recommendations in this email should reflect conversion data from Phase 1 if available. If Phase 1 data is not yet available, use: Seed Saving Field Manual (new growers), Zone Calendar (planners), Harvest Preservation Handbook (preservationists). |

**Behavioral tag logic** (applied in Emails 3 and 4):
- "seed-saver" tag: subscriber clicked the Seed Saving Manual link in Email 3 OR the food sovereignty link in Email 4
- "city-grower" tag: subscriber clicked the apartment/container link in Email 4
- "preservationist" tag: subscriber clicked the preservation link in Email 4
- Subscribers with no clicks: receive the full untagged newsletter with mixed-cluster product features

After Email 5, subscribers enter the weekly Thursday newsletter (Automation 3). The newsletter cadence begins on the first Thursday after the subscriber's Email 5 send date.

---

## Part 2: Zone Card to Email Delivery Mapping

### How Zone Selection Drives Delivery

The Zone Quick-Start Card is a personalized lead magnet — each subscriber receives the card for their zone. This requires the sign-up form to capture zone information and Kit to route the correct PDF to each subscriber.

**Sign-up form fields** (two fields only — each additional field reduces conversion 10–15%):
- First name
- Email address

**Zone selection mechanism**: A dropdown or radio button on the sign-up form labeled "Your growing zone." Values: 3, 4, 5, 6, 7, 8, 9, 10. This is a required field, not optional — without it, Kit cannot route the correct zone card.

**How Kit routes zone-specific cards**:
- Subscriber selects Zone 5 → Kit stores zone as a custom field value
- Automation 1 checks zone value → sends Email 1 variant with Zone 5 PDF download link
- All subsequent welcome sequence emails are the same regardless of zone — only Email 1 is zone-specific

**Eight Email 1 variants required** — one per zone, each containing the correct zone-specific PDF download link. The body copy is identical across all eight; only the zone reference ("Zone [X]") and the download link change. Build all 8 variants before the form goes live.

### Zone Card to Email Delivery Table

This is the complete routing map. Each row represents one zone variant of Email 1.

| Subscriber Zone | Zone Card PDF File | Email 1 Subject | Download Link Source |
|---|---|---|---|
| Zone 3 | `zone-3-quick-start-card.pdf` | "Your Zone 3 Quick-Start Card is ready" | Kit Files upload URL |
| Zone 4 | `zone-4-quick-start-card.pdf` | "Your Zone 4 Quick-Start Card is ready" | Kit Files upload URL |
| Zone 5 | `zone-5-quick-start-card.pdf` | "Your Zone 5 Quick-Start Card is ready" | Kit Files upload URL |
| Zone 6 | `zone-6-quick-start-card.pdf` | "Your Zone 6 Quick-Start Card is ready" | Kit Files upload URL |
| Zone 7 | `zone-7-quick-start-card.pdf` | "Your Zone 7 Quick-Start Card is ready" | Kit Files upload URL |
| Zone 8 | `zone-8-quick-start-card.pdf` | "Your Zone 8 Quick-Start Card is ready" | Kit Files upload URL |
| Zone 9 | `zone-9-quick-start-card.pdf` | "Your Zone 9 Quick-Start Card is ready" | Kit Files upload URL |
| Zone 10 | `zone-10-quick-start-card.pdf` | "Your Zone 10 Quick-Start Card is ready" | Kit Files upload URL |

Zone card PDFs are built per `ZONE_CARD_PRODUCTION_TIMELINE.md`. All 8 PDFs must be uploaded to Kit (Content > Files) before the sign-up form is published. Log each Kit download URL in WORKLOG.md immediately after upload — these URLs are the link in each Email 1 variant and losing them requires re-upload.

---

## Part 3: Email-to-Photo Release Coordination

### How Lifestyle Photos Feed the Email Work Stream

Lifestyle photos (from the physical shoot documented in `PHOTO_SHOOT_PLANNING.md`) serve two email functions:

**Function 1: Newsletter product spotlight images**

Each Thursday newsletter (Automation 3, Section 3 — Product Spotlight) benefits from one lifestyle image of the featured product. This is not a requirement for launch — the newsletter can launch without lifestyle photos and add them as they become available — but images increase click-through rate on the product spotlight link by 20–35%.

**Recommended photo-to-newsletter release sequence**:

Release newsletters with lifestyle images for the product clusters in the order the physical shoot is completed:

| Newsletter Week | Featured Product Cluster | Photo Requirement | Ready After |
|---|---|---|---|
| Weeks 1–2 (May newsletter, no lifestyle photos yet) | Any — text only | No photo required | Launch immediately |
| Week 3 (after Cluster A shoot) | Seed Saving or Heirloom Guide | Cluster A slot 4 or 5 image | After Session 1 batch editing |
| Week 4 | Companion Planting Chart | Cluster A slot 4 image (chart flat lay) | After Session 1 |
| Week 5 | Container Growing Blueprint or Apartment Guide | Cluster B slot 4 image | After Session 2 |
| Week 6 | Fermented/Preserved Harvest Handbook | Cluster C slot 4 image | After Session 3 |
| Week 7+ | Any product, full rotation | All 30 lifestyle images available | After batch editing complete |

**Function 2: Lead magnet landing page hero image**

The Kit landing page for the Zone Quick-Start Card sign-up form can include a header image. This is optional — the landing page converts well on copy alone. If a lifestyle image is used, the recommended choice is the Companion Planting Chart flat lay (Product 4, Slot 4): it shows a dense, legible reference document in a real-world context, which signals exactly what the zone card is.

Add the landing page image only after Session 1 photos are available. Launch the landing page without a hero image if Session 1 photos are not yet complete — do not delay the form launch for a photo.

### Photo Release to Email Timeline

| Date Range | Photo Event | Email Action |
|---|---|---|
| April 28–30 | No photos yet | Write and load all 5 welcome sequence emails; set up Kit; test end-to-end |
| May 1–6 | No photos yet | Launch sign-up form and landing page (text-only is fine) |
| May 7–13 (Session 1) | Cluster A photos shot and edited | Add hero image to landing page; prepare first newsletter with product spotlight image |
| May 7–13 (Sessions 2–3) | Cluster B and C photos shot and edited | Remaining newsletter weeks can now feature product images through Week 7 |
| May 14+ | All 30 lifestyle photos available | Newsletter product spotlight rotation at full capacity |

---

## Part 4: Platform Setup Sequence

### Build Order

Execute Kit setup steps in this exact order. Each step depends on the previous one being complete.

**Step 1: Kit account and sender domain (30 minutes)**

- Create Kit account at kit.com (free tier, up to 10,000 subscribers)
- In Kit: Settings > Email Settings > From address
- Set the "From" name to: Seedwarden
- Set the "From" email to: a Seedwarden-branded address (e.g., hello@seedwarden.com). If no custom domain email exists yet, use a Gmail address temporarily and update when the domain is configured
- Authenticate the sender domain: Kit provides SPF and DKIM DNS records. Add these to the domain's DNS (via the domain registrar). Without authentication, welcome emails land in spam at a high rate
- If using Gmail temporarily: Kit will still deliver, but expect 10–15% lower inbox placement until a custom domain is authenticated. Resolve this before the list reaches 500 subscribers

**Step 2: Upload zone card PDFs (15 minutes)**

- In Kit: Content > Files
- Upload all 8 zone card PDFs in sequence: zone-3 through zone-10
- After each upload, copy the download URL immediately — paste into a local note with the zone number labeled
- Verify each link works by opening it in a private/incognito browser window before moving on

**Step 3: Create the sign-up form with zone selection (20 minutes)**

- In Kit: Forms > New Form
- Form style: landing page
- Headline: "Get Your Free Zone Quick-Start Card"
- Subheadline: "One page. Your zone. What to plant right now."
- Fields: First Name, Email (required); Growing Zone dropdown (required; values: 3, 4, 5, 6, 7, 8, 9, 10)
- CTA button text: "Send me my zone card"
- No image required at launch — add after Session 1 photos are available
- Publish and copy the landing page URL

**Step 4: Load the welcome sequence (60 minutes)**

- In Kit: Sequences > New Sequence
- Name: "Seedwarden Welcome"
- Create 8 variants of Email 1 (one per zone). Kit handles zone routing via a conditional automation — if zone = 5, send the Email 1 variant with the Zone 5 download link
- Load Emails 2–5 as single variants (same copy for all zones)
- Set delays: Email 1 immediate, Email 2 on Day 2, Email 3 on Day 5, Email 4 on Day 7, Email 5 on Day 10
- Do not set conditional "send only if previous email was opened" in Phase 1 — add that in Phase 2 after you have open rate data to calibrate against

**Step 5: Create the welcome automation (10 minutes)**

- In Kit: Automations > New Automation
- Trigger: Form submitted (select the zone card sign-up form)
- Action 1: Add tag "new-subscriber"
- Action 2: Add to sequence "Seedwarden Welcome"
- Action 3 (conditional): If zone = [X], send Email 1 variant [X]. Replicate this conditional for all 8 zones.
- Publish the automation

**Step 6: End-to-end test (15 minutes)**

- Submit the sign-up form with a test email address and Zone 5 selected
- Confirm Email 1 arrives with the Zone 5 download link (within 60 seconds)
- Open the download link — confirm the Zone 5 PDF opens correctly
- Check the "From" address and sender name in the received email
- Check that the email did not land in the spam folder (open a Gmail test account if needed)
- If any of these checks fail, resolve before publishing the landing page URL anywhere

**Step 7: Publish landing page URL to all channels (10 minutes)**

After the end-to-end test passes:
- Add the landing page URL to the Etsy shop bio
- Add one line to every Etsy listing description: "Free zone planting guide: [URL]"
- Configure the Etsy automated thank-you message (Shop Manager > Messages to Buyers) to include: "Bonus — grab our free Zone Quick-Start Card: [URL]"
- Add the URL to the footer CTA page in all 21 product PDFs (or schedule this as a batch task — the PDF end-page is the highest-converting placement but not required on Day 1)

**Total Kit setup time**: approximately 2.5 hours for a first-time user. 90 minutes for someone familiar with Kit.

---

## Part 5: Platform Selection Rationale

### Why Kit (ConvertKit) and Not an Alternative

This decision is documented in full in `email-growth-playbook.md` Part 5. Summary for production reference:

- Kit free tier: 0–10,000 subscribers at $0/month — no cost until well past Phase 3 scale
- Native landing pages: no separate website required for lead magnet delivery or sign-up form hosting
- Conditional automations: zone-specific routing (the core delivery mechanism) is available in the free tier
- Creator economy positioning: Kit is the standard platform for solo creators selling digital products on Etsy; community support and templates are directly applicable

**Klaviyo assessment**: Klaviyo's free tier (0–250 subscribers) is more powerful for e-commerce segmentation but has a steeper setup curve and is designed for direct e-commerce integrations (Shopify, WooCommerce) rather than Etsy digital sellers. Switch to Klaviyo if and when Seedwarden builds a direct storefront (Phase 3+). For now, Kit is the correct fit.

**Mailchimp assessment**: Mailchimp free tier has an email limit of 1,000 sends/month, which creates a practical ceiling at a list size of ~200 subscribers on weekly cadence. Kit has no send limit on the free tier. Mailchimp is eliminated on this constraint.

---

## Part 6: Copy Themes for Each Email — Quick Reference

Use this section to draft or review any email copy against its intended purpose. Full copy exists in `marketing/email-and-launch-plan.md`; this is the thematic guardrail.

### Welcome Sequence Themes

**Email 1 — Welcome + Zone Card Delivery**
Core theme: "Here is your zone card; here is what Seedwarden is and why it exists." Founder voice: warm, specific, non-promotional. This email is the first impression — it establishes whether the subscriber will open Email 2. The zone card download should be the largest link on the page, not buried.

Tone guardrail: Do not write as a brand. Write as a person who made a thing and is sharing it. The difference: "Welcome to the Seedwarden community" (brand) vs. "Welcome — I'm really glad you found your way here" (person).

**Email 2 — Heirloom Seed Philosophy**
Core theme: "Why heirloom seeds matter and what makes Seedwarden different from a seed catalog." The Brandywine tomato story is the vehicle. This email should end with a forward reference to Email 3 — "Next email I'll share a mistake I made that cost me an entire season."

Tone guardrail: Educational but personal. The subscriber is learning something real. Avoid lecturing; frame as sharing something the writer finds genuinely interesting.

**Email 3 — Seed Saving Mistake Story**
Core theme: "I made a mistake so you don't have to — and it's in the guide so you can avoid it." The paper towel / fermentation story. First behavioral tag link embedded: a link to the Seed Saving Field Manual for subscribers who want to go deeper.

Tone guardrail: Vulnerability is the mechanism. The mistake must sound real. The lesson must be practical and specific — not a general "save seeds properly" but "tomato seeds require fermentation to remove the gel coating; here is why and how."

**Email 4 — Catalog Introduction**
Core theme: "Here is what I built and why digital guides made sense for this audience." Three segmentation links drive behavioral tags. This is the first time the catalog is introduced — make it feel like pulling back a curtain, not a product announcement.

Tone guardrail: Frame the catalog as a natural extension of the educational content in Emails 2 and 3. "The guides I've built are heavy on exactly this kind of detail" is the bridge from story to product.

**Email 5 — First Offer**
Core theme: "You've read four emails; here is a reason to buy now that expires in 5 days." SEEDWARDEN15 coupon. This email should acknowledge that the sequence is ending: "This is the last email in this series before I switch to my regular newsletter cadence."

Tone guardrail: The offer should be framed as a genuine gesture, not a sales tactic. "I'm not going to run a permanent discount — that's not sustainable and not honest" is the right register. Avoid countdown timer language; Seedwarden's audience is sophisticated about marketing manipulation.

### Post-Purchase Sequence Themes

**Post-Purchase Email 1 — Thank You and Orientation**
Core theme: "You bought the guide; here is where to start." Under 150 words. Ends with an open question: "What are you hoping to grow or preserve this season?" (drives reply, improves deliverability, generates product intelligence).

**Post-Purchase Email 2 — Cross-Sell**
Core theme: "Here is the natural next guide based on what you bought." No discount, no pressure. Frames the second product as the next logical step. One product recommendation only — do not list the entire catalog.

**Post-Purchase Email 3 — Review Request**
Core theme: "A short review helps other growers find this guide." Under 100 words. Direct link to the Etsy review page. No incentive (Etsy prohibits incentivized reviews). Honest framing: "It takes about 45 seconds and means a lot."

### Newsletter Section Themes (Weekly Thursday)

Each newsletter follows a four-section structure (from `marketing/email-automation-blueprint.md` Part 5):

1. **Growing update** (2–3 sentences): What is happening in the founder's actual garden or homestead right now. Seasonal specificity. Not aspirational — actual current state.
2. **Technique or tip** (200–350 words): The main educational content. Should be actionable, specific, and complete. Do not tease — give the full technique. Teasing to drive a product click is a dark pattern that erodes trust in this audience.
3. **Product spotlight** (3–4 sentences + Etsy link): One product, featured in relation to the technique topic. If the technique is about seed saving, feature the Seed Saving Field Manual. The connection should be natural, not forced.
4. **Reader question** (50–100 words): Answer one question from a recent reply, comment, or Etsy message. This shows the community that real questions get real answers. It also provides a recurring source of newsletter content that does not require original topic generation.

---

## Part 7: Work Stream Coordination — Dependency Map

### What Email Depends On

| Email Work Stream Item | Depends On | Blocks |
|---|---|---|
| Kit account setup | Nothing | All email automation |
| Zone card PDFs uploaded to Kit | Zone card PDFs built (Weeks 1–3 of ZONE_CARD_PRODUCTION_TIMELINE.md) | Email 1 zone routing; sign-up form launch |
| Sign-up form with zone dropdown | Kit account setup | Landing page URL; Etsy bio link; PDF end-page CTA |
| Welcome sequence (5 emails) loaded | Kit account setup; Email 1 zone routing tested | List-building funnel launch |
| PDF end-pages added to all 21 products | Welcome sequence landing page URL confirmed | Highest-conversion list-building tactic |
| Newsletter content ready | Welcome sequence complete; lifestyle photos optional but recommended | Week 3+ subscriber engagement |
| Post-purchase automation | Etsy sales live; manual or Zapier trigger set up | Repeat purchase rate; review generation |

### What Zone Card Build Depends On

| Zone Card Work Stream Item | Email Dependency |
|---|---|
| Zone card spec content finalized | Email 1 zone card download link cannot be written until PDF filename is confirmed |
| All 8 PDFs exported from Canva | Email 1 variants cannot be tested until PDFs are uploaded to Kit |
| Kit file URLs logged in WORKLOG.md | Email 1 variants cannot be published with correct links |

### What Photography Depends On

Photography has no hard dependency on the email work stream. Lifestyle photos improve the newsletter and landing page but do not block list-building launch. The email funnel can go live before a single photo is taken and add photos as they become available.

---

## Part 8: Launch Readiness Checklist

Before publishing the sign-up form URL anywhere, confirm all items below.

### Email Infrastructure

- [ ] Kit account created and sender domain authenticated (SPF/DKIM)
- [ ] "From" name is Seedwarden; "From" email is a Seedwarden-branded address
- [ ] All 8 zone card PDFs uploaded to Kit; all 8 download URLs logged in WORKLOG.md
- [ ] Sign-up form built with zone dropdown; landing page published; URL recorded
- [ ] All 5 welcome sequence emails loaded with correct delays
- [ ] Zone routing automation built and published (form submit → zone check → Email 1 variant)
- [ ] End-to-end test completed for at least Zone 5 (submit → Email 1 arrives → PDF link works)
- [ ] End-to-end test completed for at least one additional zone (e.g., Zone 3 or Zone 9)
- [ ] SEEDWARDEN15 coupon code generated in Etsy dashboard and confirmed active

### Distribution Points

- [ ] Landing page URL added to Etsy shop bio
- [ ] One-line lead magnet CTA added to at least the top 5 Etsy listing descriptions
- [ ] Etsy automated thank-you message updated with landing page URL
- [ ] PDF end-pages: at minimum, the top 3 best-selling products have the end-page CTA (full 21-product update can follow)

### Content Readiness

- [ ] Email 1 copy finalized for all 8 zone variants — tone and founder voice consistent with email-and-launch-plan.md
- [ ] Emails 2–5 copy finalized and loaded — no placeholder text remaining (e.g., "[Guide title]" or "[Etsy link]" must be replaced with actual values)
- [ ] SEEDWARDEN15 coupon expiry date logic understood: Email 5 communicates "expires in 5 days" as a communicated deadline, not a Kit-enforced timer; track manually or via simple spreadsheet

---

## Part 9: Metrics and Thresholds

Email metrics are tracked monthly. Full framework in `email-growth-playbook.md` Part 6. Quick reference for Phase 2:

| Metric | Healthy | Alert | Action |
|---|---|---|---|
| Landing page conversion rate | 25–45% | Under 15% | Simplify form; test headline; confirm 2 fields only |
| Email 1 open rate | 45–60% | Under 30% | Check spam delivery; test subject line; verify sender authentication |
| Welcome sequence completion rate | 80–95% | Under 70% | Review for unsubscribe triggers; check content quality |
| Email 5 coupon redemption rate | 8–15% | Under 5% | Revise product recommendations; test 5-day vs. 7-day window |
| Weekly newsletter open rate | 28–40% | Under 22% | Audit subject line formulas; reduce to bi-weekly temporarily |

**Month-by-month subscriber targets** (from `email-growth-playbook.md` Part 6):

| Month | Target | Notes |
|---|---|---|
| June 1, 2026 | 50+ subscribers | Achievable via PDF end-pages + Etsy bio alone |
| July 1, 2026 | 80+ subscribers | Pinterest pin activation required if Etsy bio pace is below target |
| August 1, 2026 | 150+ subscribers | Reddit organic participation is the main lever at this stage |
| October 2026 | 300–500 subscribers | Phase 3 product launch velocity depends on this threshold |

---

*Prepared: 2026-04-30. This document is the Phase 2 production coordinator for the email work stream. For full copy, see `marketing/email-and-launch-plan.md`. For automation technical setup, see `marketing/email-automation-blueprint.md`. For list-building tactics and KPI gates, see `email-growth-playbook.md`. For zone card build schedule, see `ZONE_CARD_PRODUCTION_TIMELINE.md`.*
