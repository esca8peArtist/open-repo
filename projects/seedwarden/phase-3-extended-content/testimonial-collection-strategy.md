---
title: "Phase 3 Testimonial Collection Strategy — Request Templates, Incentive Models, Aggregation"
date: 2026-06-28
version: 1.0
status: production-ready
sprint-window: June 29 onward (collection begins at first bundle sale)
cross-references:
  - PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md (implementation notes: contractor testimonial requests)
  - phase-3-extended-content/promotional-email-sequences.md (placeholder testimonials in email sequences)
  - PHASE_3_EXTENDED_SOCIAL_CALENDAR_JUL_SEP.md (placeholder testimonials in posts 33, 38, 43, etc.)
  - PHASE_3_LAUNCH_MARKETING_CALENDAR.md (week-6 post-launch testimonial request timing)
---

# Phase 3 Testimonial Collection Strategy

**Purpose**: Mechanistic process for requesting, receiving, storing, and deploying buyer testimonials across email sequences, social posts, and landing pages. Collection begins at first bundle sale (June 29). All post placeholders and email placeholders are replaced with real testimonials as they are collected.

**What counts as a testimonial**: Any unsolicited or solicited statement from a buyer or community member that describes a specific, verifiable outcome or changed behavior as a result of using the guides. General praise ("loved it") is not a testimonial. Specific behavior change ("I harvested my echinacea root in year 3 instead of year 2 after reading the timing section") is a testimonial.

**Why this distinction matters**: Specific testimonials convert. Vague praise does not. The collection process is designed to elicit specific, useful statements — not encourage positive-but-useless reviews.

---

## Part 1 — Collection Timeline

### Phase 1: First 30 Days Post-Launch (June 29 – July 28)

**Goal**: 5 usable testimonials from early buyers across at least 2 bundles.

**Who to target**: Anyone who purchases in the first week (launch adopters are most likely to engage with a request). Tag in Kit: `early-adopter` if purchase date is within 7 days of bundle launch.

**When to ask**: Day 7 after purchase. Not immediately — they need to have read at least part of the guide before they can say something specific. Not day 30 — the immediacy of the experience fades.

**Expected response rate**: 10–20% of early buyers with a direct request. Lower than "star rating" reviews because testimonials require more effort.

**Minimum viable outcome**: 3 usable testimonials from Phase 1. If below 3 by July 28, activate the incentive model (Part 2).

---

### Phase 2: Bundle-by-Bundle Collection (July – August)

**Goal**: At least 1 testimonial per bundle (5 bundles = 5 testimonials minimum). Practitioner Tier gets its own dedicated testimonial.

**Trigger for each bundle**: 14 days after each bundle's launch date (see below):

| Bundle | Launch Date | Testimonial Request Send Date |
|---|---|---|
| Women's Health | Jun 29 | Jul 13 |
| Respiratory Health | Jul 6 | Jul 20 |
| Sleep & Nervines | Jul 13 | Jul 27 |
| Immunity Support | Jul 20 | Aug 3 |
| Practitioner Tier | Jul 15 | Jul 29 |
| Digestive Support | Aug 3 | Aug 17 |

**Who to target**: All buyers of that specific bundle who have not yet provided a testimonial.

**Expected yield**: If 20+ buyers per bundle, expect 2–5 responses. If fewer than 10 buyers per bundle, contact every buyer individually (not broadcast — personal email to each).

---

### Phase 3: Sustained Collection (August – December)

**Goal**: 2–3 new usable testimonials per month to keep the collection fresh for seasonal campaigns.

**Mechanism**: Monthly newsletter (see PHASE_3_PROMOTIONAL_EMAIL_SEQUENCES.md, Monthly Educational Newsletter template) includes a one-line footer: "Have a story about growing with Seedwarden? Reply and tell us. We feature community growing stories monthly."

This is passive collection — not a dedicated request. It captures the motivated community member who is already thinking about it.

**Target personas for sustained collection** (prioritize these for focused outreach if response rates drop):
- Practitioner buyers (highest conversion value, most credibility with LinkedIn audience)
- Educators who assigned the guides to students
- Zone-specific buyers (zone 4, 6, and 7 are underrepresented in the initial calendar — collect those specifically)
- Year-1 herb growers (relatable to the largest audience segment)

---

## Part 2 — Request Templates

### Template A — Direct Testimonial Request (Primary Template)
**Use for**: All bundle buyers, Day 7 post-purchase
**Format**: Email (Kit automation or manual), sent from [YOUR_EMAIL] not a Kit newsletter address if possible (increases open rate and response rate for personal requests)

---

**Subject**: "A quick question about [BUNDLE NAME]"
**Preview text**: "Not a survey. One question."

---

Hi [FIRST_NAME],

You downloaded [BUNDLE NAME] last week.

One question: has anything in the guide changed how you think about [herb growing / sourcing / using a specific herb — tailor to bundle]?

I am not looking for a star rating or a polished review. I am looking for a specific moment — something you read that changed what you were going to do next.

If something like that happened, reply to this email and tell me. I may feature your note (with your permission) in a future email or social post, with exactly the level of anonymity you prefer — first name and state only, first initial only, or fully anonymous.

If nothing landed yet, that is fine — you may still be reading.

[YOUR NAME]
Seedwarden

---

**Automation note**: Load as Kit automation, triggered by `[bundle-name]-purchased` tag, send on Day 7. Reply goes directly to your email inbox — not a Kit form. This is intentional: a direct reply feels personal and generates longer, more useful testimonials than a form.

---

### Template B — Social Proof Request (Instagram Stories / Community Tab)
**Use for**: Passive collection from followers who have not necessarily purchased (captures community engagement)
**Platform**: Instagram Stories, YouTube Community Tab
**Post this once per month, rotated with other engagement content**

---

**Instagram Stories copy**:

Growing with Seedwarden guides this season?

Tell me one thing you did differently in your garden because of something you read.

Reply to this Story — I read every one.

---

**YouTube Community Tab copy**:

Growers using the Phase 3 guides this season:

What changed in how you grow, harvest, or source after reading one of the bundles?

Drop the herb name and the change in the comments. Specific answers are the ones we use in future content — "I loved it" is kind but does not help us know what to write more of.

---

**What to do with responses**: Screenshot usable responses immediately. Log in the Testimonial Tracker (Part 4 below). Follow up within 24 hours with a direct message: "Thanks for sharing that — can I use your note in a future Seedwarden post or email? First name and state only, or fully anonymous if you prefer."

---

### Template C — Practitioner / Educator Testimonial Request
**Use for**: Buyers tagged `practitioner`, `educator`, or `herbalism-student`
**Format**: Personal email, not automated — write individually after a practitioner purchase is detected
**Timing**: Day 14 after Practitioner Tier purchase (longer delay because the integration reference takes more time to use)

---

**Subject**: "A question about how you are using the Practitioner Tier"

---

Hi [FIRST_NAME],

You downloaded the Practitioner Tier two weeks ago.

A direct question: are you using it in a patient care, student curriculum, or workshop context? And if so, has anything in the guides or the cross-bundle integration reference changed your workflow?

I ask because practitioner-specific use cases are the hardest to document from the outside — I only know about them when someone tells me. If you have found a specific use for the integration reference (pre-appointment prep, curriculum assignment, student handout), I would genuinely like to know.

If the guides are proving useful in a professional context, I may ask if you are willing to share a quote (attributed to first name and professional context only, or anonymously — your call) for a future LinkedIn post or email.

No obligation. If the guides are not in your workflow yet, no worries — they take time to integrate.

[YOUR NAME]
Seedwarden

---

**Conversion note**: Practitioner testimonials are disproportionately valuable for the LinkedIn audience and for the Practitioner Tier sales page. Even one well-framed practitioner testimonial outweighs ten general testimonials on LinkedIn.

---

### Template D — Follow-Up Permission Request
**Use for**: After someone sends you a useful testimonial reply (to any template above), before featuring it
**Format**: Reply to their email or DM — do not assume permission

---

Hi [FIRST_NAME],

Thank you for this — this is exactly the kind of specific experience I was looking for.

May I use your note in a future Seedwarden email or social post? Here are the options for how I would attribute it:

1. First name and state: "— [Name], [State]"
2. First initial only: "— [Initial]., [State]"
3. Role/context only: "— A Zone 6 grower in the Midwest" or "— A first-year herbalism student"
4. Anonymous: I paraphrase without attribution

Let me know which option works for you. I will not use your note without your explicit okay.

[YOUR NAME]

---

**Response follow-through**: Log permission level in the Testimonial Tracker when received. Use only the permitted attribution level in all placements.

---

## Part 3 — Incentive Models

**Principle**: Incentives for testimonials must not compromise authenticity or create FTC disclosure complications. The goal is to reduce friction for buyers who are willing to share but have not done so yet — not to manufacture positive reviews.

**FTC note**: If any incentive is offered in exchange for a testimonial, that relationship must be disclosed in any public use of the testimonial ("received a discount on a future purchase in exchange for this review"). This is mandatory and non-negotiable. The templates below are structured to keep this clean.

---

### Incentive Tier 1 — Low Barrier (No Disclosure Required)
**What it is**: Thank-you acknowledgment + feature in monthly newsletter or social post
**Who it targets**: All buyers
**How it works**: Anyone who provides a usable testimonial receives a personal thank-you reply from you + is featured (with permission) in the monthly newsletter or a social post. No financial exchange. No disclosure required.
**ROI**: No cost. Encourages community identity as "people featured by Seedwarden." Effective for engaged audience segments.

---

### Incentive Tier 2 — Low-Cost Incentive (Disclosure Required)
**What it is**: 15–25% discount on a future bundle purchase
**Who it targets**: Buyers who provide a detailed, specific testimonial (more than 2 sentences)
**How it works**: After receiving and confirming permission to use the testimonial, reply: "As a thank-you for sharing this, here is a discount code for 15% off your next Seedwarden purchase: [CODE]. Use it whenever you are ready."
**FTC requirement**: If this testimonial is featured publicly, include "(received discount on future purchase in exchange for this review)" or equivalent disclosure near the testimonial.
**Disclosure placement**: Below the testimonial in small text. Does not need to be prominently displayed — just present.
**Cost per testimonial**: ~$3–5 per testimonial (15% off a $20 bundle). Maximum 10 discounts per quarter.
**When to use**: Activate after Phase 1 if response rate is below 10%. Do not start with incentives — start with direct requests and add incentives only if response rates are insufficient.

---

### Incentive Tier 3 — Community Builder (No Individual Incentive — Collective Value)
**What it is**: A "Community Growing Stories" feature in the monthly newsletter — regular segment where buyer growing experiences are featured
**Who it targets**: All subscribers and buyers
**How it works**: Monthly newsletter includes a "Growing Stories" section featuring 2–3 testimonials or community notes. Being featured is the recognition — no financial exchange.
**Why this works**: Community identity matters to the Seedwarden audience (herb growers who care about the practice). Being featured in a community-focused newsletter is a meaningful recognition without any financial exchange or disclosure complications.
**Activation**: Start with the August monthly newsletter. Maintain through Phase 4 regardless of volume — even thin months, run the section with 1–2 community notes.

---

### Incentive Tier 4 — Practitioner Network Incentive
**What it is**: Free educator license for one bundle in exchange for a formal written testimonial from a verified practitioner or educator
**Who it targets**: Practitioners and educators who purchase the Practitioner Tier
**How it works**: After receiving a usable practitioner testimonial with explicit permission to use it publicly, offer one complimentary educator license for a single bundle of their choice (valued at $20–$22). This enables them to use the guide in a classroom or workshop context without the standard license restriction.
**FTC requirement**: Disclosure required if testimonial is used publicly. Suggested disclosure: "(received complimentary educator license in exchange for this review)"
**When to use**: For high-value practitioner testimonials that are likely to be used in LinkedIn and Practitioner Tier sales page contexts. Maximum 3 per quarter to preserve scarcity of the offer.

---

## Part 4 — Aggregation: Testimonial Tracker

Maintain a running log in a simple spreadsheet or document. Format below. Update within 24 hours of receiving any testimonial.

### Tracker Format

| Date | Name | Attribution Level | Bundle | Quote | Placement | Incentive | Disclosure Needed |
|---|---|---|---|---|---|---|---|
| Jul 13, 2026 | Maria T. | First name + state (Pennsylvania) | Women's Health | "I had no idea Black Cohosh was at risk..." | Email Seq 1 Email 4, Social Post 33 | None | No |
| Jul 20, 2026 | James R. | First name + descriptor (first-year student, Pacific NW) | Practitioner Tier | "The echinacea species breakdown alone saved me 4 hours..." | Social Post 38 | None | No |
| [DATE] | [NAME] | [PERMISSION LEVEL] | [BUNDLE] | [FULL QUOTE] | [WHERE USED] | [INCENTIVE IF ANY] | [YES/NO] |

### Tracker File Location

Store at: `/projects/seedwarden/data/testimonial-tracker.csv` or as a tab in an existing Google Sheets dashboard.

Minimum columns: Date Received, Buyer Name, Attribution Permission, Bundle Purchased, Quote (verbatim), Approved for Use (Y/N), Placed In (list of posts/emails where used), Incentive Offered, Disclosure Required.

---

## Part 5 — Deployment: Where Each Testimonial Type Goes

### Platform-Specific Placement Rules

**LinkedIn posts**: Practitioner or educator testimonials only. Attribution minimum: first name + professional role. General buyer testimonials do not perform on LinkedIn because the audience is professional-context oriented.

**Instagram posts**: General buyer testimonials work best. Zone-specific ("Zone 6 grower in Pennsylvania") performs well. "First harvest" narratives (first root harvest, first tincture, first year growing) are the highest-engagement format for Instagram.

**YouTube Community Tab**: Learning-journey testimonials — "I used to do X, now I understand Y." The study-habit and learning-progression narrative fits the YouTube audience.

**Email sequences**: All testimonial types. Practitioner testimonials go in Sequence 5 (Practitioner). First-year-grower testimonials go in Sequence 1 Email 4 (Free-to-Paid). Clinical use testimonials go in Sequence 2 Upgrade Email 2 (Practitioner pitch).

**Landing page / Etsy listings**: Practitioner or zone-specific testimonials, attributed clearly. These are permanent placements — use only testimonials with explicit "permanent use" permission, not just "use in one post."

---

### Content Mix Target by Quarter

**Q3 2026 (July–September)**: 5 testimonials minimum (one per bundle), 1 practitioner testimonial
**Q4 2026 (October–December)**: 10 total testimonials in library, 3 practitioner testimonials
**Q1 2027**: Testimonial library is refreshed — 2+ new testimonials per month from sustained collection

---

## Part 6 — Review Aggregation Strategy

Beyond direct testimonials, Etsy reviews are public social proof that does not require permission because they are already public. Process:

### Etsy Review Monitoring

**Trigger**: Check Etsy reviews weekly starting June 29.

**What to look for**:
- Reviews longer than 2 sentences (these contain usable content)
- Reviews that mention a specific herb, section, or use case (not just "great guide")
- Reviews that mention professional or practitioner use

**What to do with usable Etsy reviews**:
1. Screenshot immediately and save to `/projects/seedwarden/assets/testimonials/etsy-screenshots/`
2. Log in Testimonial Tracker with "Source: Etsy review" — no permission required for public review content
3. Attribution: "Etsy buyer, [Zone if mentioned]" — do not use name unless they signed their review publicly
4. Deploy on social (Instagram and YouTube) — public Etsy reviews can be shared without additional permission

**What to do with usable reviews on other platforms** (Google, Trustpilot, if applicable):
Same process. Public reviews are publicly attributable. Do not alter the quote.

### Responding to Etsy Reviews

**Every review gets a response within 48 hours.**

For 5-star reviews with specific content:
"Thank you for sharing that — [one sentence that reflects their specific feedback back to them]. If you want to share your growing experience with the broader Seedwarden community, our monthly newsletter features reader growing stories."

For 4-star reviews:
"Thank you for the feedback. [Address the specific note they gave.] If anything is unclear or missing, reply to your order confirmation email — I read all responses directly."

For 3-star or below:
Respond directly, address the specific complaint, offer a clarification or partial refund if appropriate. Do not defend — understand. Log the feedback in WORKLOG.md under the relevant bundle name.

---

## Part 7 — Quality Control

A testimonial is usable if it meets at least two of these three criteria:

1. **Specific**: Names a herb, section, or action taken ("I harvested my echinacea root in October year 3 because I read the timing section")
2. **Verifiable outcome**: Describes a change in behavior, knowledge, or practice ("I stopped buying wild-harvested goldenseal after reading the conservation sidebar")
3. **Relatable**: From a buyer persona the target audience identifies with (home grower, herbalism student, practitioner, market seller)

A testimonial fails the standard if it is:
- Vague: "Great guide!" "Very informative!" "Loved the detail!" — these are star ratings, not testimonials
- Comparative only: "Better than the other guide I read" — no specifics, no deployment value
- Overclaiming: "This guide cured my..." — do not use, legally and ethically

**What to do with vague positive feedback**: Thank the buyer. Do not feature it publicly. Keep it in a "Positive Signals" log — useful for internal motivation, not for external social proof.

---

## Implementation Checklist

**June 29** (launch day):
- [ ] Testimonial Tracker file created at `/projects/seedwarden/data/testimonial-tracker.csv` (or Google Sheets)
- [ ] Template A automation set up in Kit (trigger: any bundle purchase, Day 7 send)
- [ ] Template C personal email reminder set up (calendar reminder to send manually 14 days after each Practitioner Tier purchase)

**July 13** (first testimonial request sends for Women's Health buyers):
- [ ] Template A sends automatically — confirm Kit automation is running
- [ ] Check Etsy reviews for Women's Health; log any usable reviews

**July 28** (Phase 1 close — 30 days post-launch):
- [ ] Count usable testimonials: target is 5 minimum
- [ ] If below 3: activate Incentive Tier 2 (15% discount offer) and extend outreach
- [ ] Update social post placeholders (Posts 33, 38, 43, etc.) with real testimonials if available

**August 4** (Phase 2 begins):
- [ ] Monthly newsletter template finalized with "Growing Stories" section
- [ ] Template B (Instagram/YouTube passive collection) scheduled for first Monday of each month

**Ongoing** (monthly):
- [ ] Log all incoming testimonials within 24 hours of receipt
- [ ] Replace highest-priority placeholders in email sequences (Sequence 1 Email 4 is highest priority — it runs for all new subscribers indefinitely)
- [ ] Check and respond to all Etsy reviews within 48 hours

---

*Prepared: June 28, 2026. Collection begins at first bundle sale (June 29). All testimonial placeholder language in PHASE_3_EXTENDED_SOCIAL_CALENDAR_JUL_SEP.md (Posts 33, 38, 43, 47, 53, 58, 62, 68, 72, 78, 82, 88) and in PHASE_3_PROMOTIONAL_EMAIL_SEQUENCES.md (Sequence 1 Email 4, Sequence 5 Email B) should be replaced with real testimonials from this tracker as they are collected. FTC disclosure requirements in Part 3 are mandatory — any testimonial exchanged for compensation (discount, educator license) must be disclosed in public placements.*
