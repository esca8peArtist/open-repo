---
title: "Phase 3 Testimonial Collection Framework — Request Templates, Incentives, Aggregation, FTC Compliance"
date: 2026-06-28
version: 1.0
status: production-ready
sprint-window: June 29 onward (collection begins at first bundle sale)
cross-references:
  - PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md (launch email implementation notes)
  - PROMOTIONAL_EMAIL_SEQUENCES.md (placeholder testimonials in email sequences)
  - EXTENDED_SOCIAL_MEDIA_CONTENT_CALENDAR.md (placeholder testimonials in posts)
  - PHASE_3_LAUNCH_MARKETING_CALENDAR.md (week-by-week testimonial request timing)
  - LANDING_PAGE_COPY_FRAMEWORK.md (placement points for collected testimonials)
---

# Phase 3 Testimonial Collection Framework

**Purpose**: Mechanistic process for requesting, receiving, storing, and deploying buyer testimonials across email sequences, social posts, and landing pages. Collection begins at first bundle sale (June 29). All post placeholders and email placeholders are replaced with real testimonials as they are collected.

**What counts as a usable testimonial**: A specific, verifiable statement from a buyer or community member that describes a changed behavior, insight, or outcome resulting from using the guides. General praise ("loved it") is not a testimonial. Specific behavior change ("I harvested my echinacea root in year 3 instead of year 2 after reading the timing section") is a testimonial.

**Why this distinction matters**: Specific testimonials convert. Vague praise does not. The collection process is designed to elicit specific, useful statements — not encourage positive-but-vague reviews.

**FTC note on this entire document**: The FTC requires clear disclosure when testimonials are made in exchange for compensation of any kind (discount, free product, free license). Templates in Part 3 are structured to keep this clean. The disclosure format is specified for each incentive tier — follow it exactly.

---

## Part 1 — Collection Timeline

### Phase 1: First 30 Days Post-Launch (June 29 – July 28)

**Goal**: 5 usable testimonials from early buyers across at least 2 bundles.

**Who to target**: Anyone who purchases in the first week. Launch adopters are most likely to engage with a testimonial request — they bought with excitement and are still in the discovery phase.

**Kit tag to apply**: `early-adopter` if purchase date is within 7 days of bundle launch.

**When to ask**: Day 7 after purchase. Not immediately — they need to have read at least part of the guide before they can say something specific. Not day 30 — the immediacy fades.

**Expected response rate**: 10–20% of early buyers with a direct, personal request.

**Minimum viable outcome**: 3 usable testimonials from Phase 1. If below 3 by July 28, activate Incentive Tier 2 (Part 3) for the next outreach wave.

---

### Phase 2: Bundle-by-Bundle Collection (July – August)

**Goal**: At least 1 testimonial per bundle (5 bundles + Practitioner Tier = 6 testimonials minimum).

**Trigger for each bundle**: 14 days after each bundle's launch date.

| Bundle | Launch Date | Testimonial Request Send Date |
|---|---|---|
| Women's Health | Jun 29 | Jul 13 |
| Respiratory Health | Jul 6 | Jul 20 |
| Sleep & Nervines | Jul 13 | Jul 27 |
| Immunity Support | Jul 20 | Aug 3 |
| Practitioner Tier | Jul 15 | Jul 29 |
| Digestive Support | Aug 3 | Aug 17 |

**Who to target**: All buyers of that specific bundle who have not yet provided a testimonial.

**Expected yield**: If 20+ buyers per bundle, expect 2–5 responses. If fewer than 10 buyers per bundle, contact every buyer individually (personal email, not broadcast) — below 10 buyers warrants the personal approach.

---

### Phase 3: Sustained Collection (August – December)

**Goal**: 2–3 new usable testimonials per month to keep the collection fresh for seasonal campaigns.

**Mechanism**: Monthly newsletter (see PROMOTIONAL_EMAIL_SEQUENCES.md, Sequence 6 Monthly Newsletter) includes a one-line footer addition in alternate months: "Have a story about growing with Seedwarden? Reply and tell us. We feature community growing stories monthly."

This is passive collection — not a dedicated request. It captures motivated community members who are already thinking about it.

**Priority personas for focused outreach** (if response rates drop below 1 testimonial/month):
- Practitioner buyers: highest conversion value for LinkedIn audience; most credibility for Practitioner Tier sales page
- Educators who assigned the guides to students: unique use case that opens educator audience
- Zone-specific buyers in underrepresented zones: zone 3, zone 9, and urban growers are underrepresented in the initial calendar — collect specifically
- Year-1 herb growers: relatable to the largest audience segment; "first harvest" narrative is highest-engagement format for Instagram

---

## Part 2 — Request Templates (5 templates, different lengths and tones)

### Template A — Direct Request (Primary Template)

**Use for**: All bundle buyers, Day 7 post-purchase, automated via Kit
**Format**: Email from [YOUR_EMAIL], not a Kit newsletter address — personal sender address increases open rate and response rate for testimonial requests
**Tone**: Conversational, direct, low-pressure
**Length**: Short (under 120 words)

---

**Subject**: A quick question about [BUNDLE_NAME]
**Preview text**: Not a survey. One question.

---

Hi [FIRST_NAME],

You downloaded [BUNDLE_NAME] last week.

One question: has anything in the guide changed how you think about [herb growing / sourcing / using a specific herb — tailor to bundle]?

I am not looking for a star rating or a polished review. I am looking for a specific moment — something you read that changed what you were going to do next.

If something like that happened, reply to this email and tell me. I may feature your note (with your permission) in a future email or social post, with exactly the level of anonymity you prefer — first name and state only, first initial only, or fully anonymous.

If nothing landed yet, that is fine — you may still be reading.

[YOUR NAME]
Seedwarden

---

*Automation note*: Load as Kit automation triggered by `[bundle-name]-purchased` tag, send on Day 7. Reply goes directly to your email inbox — not a Kit form. This is intentional: a direct reply feels personal and generates longer, more useful testimonials than a form.

---

### Template B — Social Proof Request (Instagram Stories / YouTube Community Tab)

**Use for**: Passive collection from followers who have not necessarily purchased
**Platform**: Instagram Stories, YouTube Community Tab
**Post frequency**: Once per month, rotated with other engagement content
**Tone**: Community-focused, curious, inviting
**Length**: Very short (50–80 words)

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

*What to do with responses*: Screenshot usable responses immediately. Log in the Testimonial Tracker (Part 5). Follow up within 24 hours with a direct message: "Thanks for sharing that — can I use your note in a future Seedwarden post or email? First name and state only, or fully anonymous if you prefer."

---

### Template C — Practitioner and Educator Request

**Use for**: Buyers tagged `practitioner`, `educator`, or `herbalism-student`
**Format**: Personal email — write individually after a Practitioner Tier purchase is detected; do not automate this one
**Timing**: Day 14 after Practitioner Tier purchase (longer delay because the integration reference takes more time to use in practice)
**Tone**: Peer-to-peer professional, respectful, genuinely curious
**Length**: Medium (120–160 words)

---

**Subject**: A question about how you are using the Practitioner Tier

---

Hi [FIRST_NAME],

You downloaded the Practitioner Tier two weeks ago.

A direct question: are you using it in a patient care, student curriculum, or workshop context? And if so, has anything in the guides or the cross-bundle integration reference changed your workflow?

I ask because practitioner-specific use cases are the hardest to document from the outside — I only know about them when someone tells me. If you have found a specific use for the integration reference (pre-appointment prep, curriculum assignment, student handout), I would genuinely like to know.

If the guides are proving useful in a professional context, I may ask if you are willing to share a quote (attributed to first name and professional context only, or anonymously — your call) for a future LinkedIn post or the Practitioner Tier listing.

No obligation. If the guides are not in your workflow yet, no worries.

[YOUR NAME]
Seedwarden

---

*Conversion note*: Practitioner testimonials are disproportionately valuable for the LinkedIn audience and for the Practitioner Tier sales page. One well-framed practitioner testimonial outweighs ten general testimonials on LinkedIn.

---

### Template D — Follow-Up Permission Request

**Use for**: After receiving a useful testimonial reply (any template above), before featuring it publicly
**Format**: Reply to their email or DM — do not assume permission
**Tone**: Grateful, clear, option-giving
**Length**: Short (80–100 words)

---

Hi [FIRST_NAME],

Thank you for this — this is exactly the kind of specific experience I was looking for.

May I use your note in a future Seedwarden email or social post? Here are the attribution options:

1. First name and state: "— [Name], [State]"
2. First initial only: "— [Initial]., [State]"
3. Role/context only: "— A Zone 6 grower in the Midwest" or "— A first-year herbalism student"
4. Anonymous: I paraphrase without attribution

Let me know which option works for you. I will not use your note without your explicit okay.

[YOUR NAME]

---

*Response follow-through*: Log permission level in the Testimonial Tracker when received. Use only the permitted attribution level in all placements — every placement.

---

### Template E — Contractor Testimonial Request (Photographers, Writers, Habitat Specialists)

**Use for**: Phase 3 contractors (photographers, writers, habitat specialists onboarded June 24–28) who have used the guide content in their work
**Format**: Personal email or Slack/communication channel message
**Timing**: Week 3–4 of contractor engagement (after delivery, before final payment closeout)
**Tone**: Collegial, direct, low-pressure
**Length**: Short (100–120 words)

---

Hi [CONTRACTOR_NAME],

You have been inside the [Women's Health / Respiratory / Immunity — specify] bundle content for the last three weeks. I have one question:

Has anything in the content changed how you think about [herbalism / plant photography / habitat documentation — tailor to contractor track]?

Not looking for a review of the working relationship — more interested in whether the content itself shifted something for you. If something specific landed, I may ask if I can feature your note in a brief "how the guides were made" piece for the Seedwarden LinkedIn audience.

Completely optional. No obligation, no impact on your contract relationship.

[YOUR NAME]

---

*Contractor testimonial note*: Contractor testimonials work well on LinkedIn for the "how this was built" angle (see Post 48, EXTENDED_SOCIAL_MEDIA_CONTENT_CALENDAR.md). They validate production quality without being buyer testimonials. They do not replace buyer testimonials in sales contexts — they supplement them.

---

## Part 3 — Incentive Structure

**Principle**: Incentives reduce friction for buyers who are willing to share but have not done so yet. They do not manufacture positive reviews. Start with direct requests. Add incentives only if response rates are insufficient (below 10%).

**FTC rule for all incentivized testimonials**: If any compensation is offered in exchange for a testimonial, that relationship must be disclosed in any public use of the testimonial. This is mandatory and non-negotiable.

---

### Incentive Tier 1 — No-Cost Recognition (No Disclosure Required)

**What it is**: Personal thank-you + community feature in monthly newsletter or social post
**Who it targets**: All buyers
**How it works**: Anyone who provides a usable testimonial receives a personal thank-you reply + is featured (with permission) in the monthly newsletter or a social post. No financial exchange.
**FTC status**: No disclosure required (no financial exchange)
**ROI**: No cost. Encourages community identity. Effective for engaged segments.
**When to use**: Always use this first. Recognition is the primary incentive for most buyers who care about the community.

---

### Incentive Tier 2 — Discount on Future Purchase (Disclosure Required)

**What it is**: 15% discount code for a future bundle purchase
**Who it targets**: Buyers who provide a detailed, specific testimonial (2+ sentences)
**How it works**: After receiving and confirming permission to use the testimonial, reply: "As a thank-you for sharing this, here is a 15% discount code for your next Seedwarden purchase: [CODE]. Use it whenever you are ready."
**FTC disclosure required**: "*(received a discount on a future purchase in exchange for this review)*" — include below the testimonial in any public placement
**Placement of disclosure**: Small text below the testimonial. Does not need to be prominent — just present.
**Cost per testimonial**: ~$3–5 (15% off a $20 bundle)
**Maximum per quarter**: 10 discounts
**When to activate**: After Phase 1 (July 28) if response rate is below 10%. Do not start with incentives.

---

### Incentive Tier 3 — Community Growing Stories Feature (No Disclosure Required)

**What it is**: Regular "Growing Stories" section in the monthly newsletter featuring buyer experiences
**Who it targets**: All subscribers and buyers
**How it works**: Monthly newsletter includes "Growing Stories" — 2–3 testimonials or community notes. Being featured is the recognition.
**FTC status**: No disclosure required (no financial exchange — community recognition is not compensation)
**Why this works**: Herb growers care about the community. Being featured in a community newsletter is meaningful recognition without financial exchange or disclosure complications.
**Activation**: Start with the August monthly newsletter. Maintain through Phase 4 regardless of volume — even in thin months, run the section with 1–2 community notes.

---

### Incentive Tier 4 — Practitioner Educator License (Disclosure Required)

**What it is**: Complimentary educator license for one bundle in exchange for a formal written testimonial from a verified practitioner or educator
**Who it targets**: Practitioner Tier purchasers who are clinical herbalists, educators, or NDs
**How it works**: After receiving a usable practitioner testimonial with explicit permission to use it publicly, offer one complimentary educator license for a single bundle of their choice ($20–$22 value). This enables classroom or workshop use.
**FTC disclosure required**: "*(received a complimentary educator license in exchange for this review)*"
**When to use**: For high-value practitioner testimonials likely to be used on LinkedIn and the Practitioner Tier sales page. Maximum 3 per quarter — preserve scarcity.
**Activation criteria**: Testimonial must be (a) from a verified practitioner or educator, (b) specific and verifiable, (c) usable for at least one high-visibility placement (LinkedIn post or Practitioner Tier listing)

---

## Part 4 — Contractor Testimonial Guidance

Contractors (photographers, writers, habitat specialists) onboarded June 24–28 are a testimonial source for production quality and content depth — different from buyer testimonials but valuable for LinkedIn credibility content.

### What to Ask Contractors

Use Template E timing (Week 3–4 of engagement). Ask specifically about the content — not the working relationship, not the payment process. One specific moment of insight from the content is more valuable than general praise.

Target testimony areas by contractor track:

| Track | What to Ask About |
|---|---|
| Photographer | Whether photographing the herbs changed their understanding of the species |
| Writer | Whether writing the clinical sections changed their understanding of cultivation |
| Habitat Specialist | Whether the conservation context changed how they think about sourcing or foraging |

### How to Write a Testimonial (for Contractors)

If a contractor asks how to write a testimonial, share this brief guidance:

"I am not looking for a performance review or a review of our working relationship. I am looking for something specific: one thing you learned or understood differently because of the content in the guides. Ideally: what you knew before, what you read, and what you understand now. If nothing changed for you, that is a completely valid answer — don't force it."

Examples of the right format:
- "Before writing the echinacea section, I assumed the three species were interchangeable. After the research phase, I understand that alkylamide concentration varies significantly enough that the species distinction matters for anyone buying commercial echinacea. I source differently now."
- "Photographing the mullein plants changed how I see them on roadside verges. I now notice the woolly leaf texture that distinguishes V. thapsus from the look-alike species — something I completely overlooked before."

### FTC Note for Contractor Testimonials

If contractors are paid for their work (they are — they are contracted workers), any testimonial they provide is technically incentivized by that business relationship. Contractor testimonials should be attributed as "collaborator" or "production team" rather than "buyer" and do not need the standard FTC incentive disclosure — their role should be clear from context.

---

## Part 5 — Testimonial Tracker

Maintain a running log. Update within 24 hours of receiving any testimonial. Store at: `/projects/seedwarden/data/testimonial-tracker.csv` or as a tab in an existing Google Sheets dashboard.

### Tracker Format (copy into spreadsheet)

| Date | Source | Name (as permitted) | Attribution Level | Bundle | Full Quote (verbatim) | Platform Placed | Incentive | Disclosure Needed | Approved |
|---|---|---|---|---|---|---|---|---|---|
| Jul 13 | Email reply | Maria T. | First name + state (Pennsylvania) | Women's Health | "I had no idea Black Cohosh was at risk..." | Email Seq 1 Email 4, Social Post 33 | None | No | Yes |
| Jul 20 | Email reply | James R. | First name + descriptor | Practitioner Tier | "The echinacea species breakdown..." | Social Post 38 | None | No | Yes |
| [DATE] | [SOURCE] | [NAME] | [PERMISSION LEVEL] | [BUNDLE] | [FULL QUOTE] | [WHERE PLACED] | [INCENTIVE] | [YES/NO] | [YES/NO] |

**Minimum tracker columns**: Date Received, Source (Email reply / Etsy review / Instagram DM / YouTube comment), Attribution Permission Level, Bundle Purchased, Full Quote Verbatim, Approved for Use (Y/N), Placed In (list), Incentive Offered (if any), Disclosure Required (Y/N).

---

## Part 6 — Deployment: Where Each Testimonial Type Goes

### Platform-Specific Placement Rules

**LinkedIn posts**: Practitioner or educator testimonials only. Attribution minimum: first name + professional role. General buyer testimonials ("I loved the guide") do not perform on LinkedIn because the audience is professional-context oriented. Specific practitioner use case ("changed my pre-appointment prep time") performs strongly.

**Instagram posts**: General buyer testimonials work best. Zone-specific attribution ("Zone 6 grower, Pennsylvania") performs well. "First harvest" narratives (first root harvest, first tincture, first year growing from seed) are the highest-engagement format for Instagram. Keep quotes short — 1–2 sentences max for the featured quote.

**YouTube Community Tab**: Learning-journey testimonials — "I used to do X, now I understand Y." The study-habit and learning-progression narrative fits the YouTube audience.

**Email sequences**: All testimonial types work. Assignment by sequence:
- Sequence 1 Email 4 (Free-to-Paid): first-year-grower testimonials, home gardener voice — relatable to new subscribers
- Sequence 2 Email 2 (Practitioner Tier pitch): clinical use testimonials — relevant to the conversion goal
- Sequence 5 (Practitioner Back-to-School): student or educator testimonials — matches the audience

**Landing pages and Etsy listings**: Practitioner or zone-specific testimonials, attributed clearly. These are permanent placements — use only testimonials with explicit "permanent use" permission, not one-time post permission. Update when stronger testimonials arrive.

---

### Content Mix Target by Quarter

**Q3 2026 (July–September)**: 5 testimonials minimum (one per bundle), 1 practitioner testimonial
**Q4 2026 (October–December)**: 10 total in library, 3 practitioner testimonials
**Q1 2027**: Testimonial library refreshed — 2+ new testimonials per month from sustained collection, enough to rotate social posts without repeating

---

## Part 7 — Etsy Review Aggregation

Etsy reviews are public social proof that does not require additional permission because they are already public. This is a separate collection mechanism from direct testimonial requests.

### Etsy Review Monitoring

**Trigger**: Check Etsy reviews weekly starting June 29.

**What to look for**:
- Reviews longer than 2 sentences (contain usable content)
- Reviews that mention a specific herb, section, or use case
- Reviews that mention professional or practitioner use

**Process for usable Etsy reviews**:
1. Screenshot immediately; save to `/projects/seedwarden/assets/testimonials/etsy-screenshots/`
2. Log in Testimonial Tracker with "Source: Etsy review" — no additional permission required for public review content
3. Attribution: "Etsy buyer, [Zone if mentioned]" — do not use buyer's name unless they signed their review publicly
4. Deploy on social (Instagram and YouTube) — public Etsy reviews can be shared without permission
5. Do not feature on email without adding "[public Etsy review]" to the attribution — maintains transparency

**What to do with usable reviews on other platforms** (Google, if applicable):
Same process. Public reviews are publicly attributable. Never alter the quote.

---

### Responding to Etsy Reviews

Every review gets a response within 48 hours.

**5-star reviews with specific content**:
"Thank you for sharing that — [one sentence that reflects their specific feedback]. If you want to share your growing experience with the broader Seedwarden community, our monthly newsletter features reader growing stories."

**4-star reviews**:
"Thank you for the feedback. [Address the specific note they gave.] If anything is unclear or missing, reply to your order confirmation email — I read all responses directly."

**3-star or below**:
Respond directly, address the specific complaint, offer a clarification or partial refund if warranted. Do not defend — understand. Log the feedback in WORKLOG.md under the relevant bundle name. These are product improvement signals.

---

## Part 8 — Quality Standards

A testimonial is usable if it meets at least two of these three criteria:

1. **Specific**: Names a herb, section, or action taken ("I harvested my echinacea root in October year 3 because I read the timing section")
2. **Verifiable outcome**: Describes a change in behavior, knowledge, or practice ("I stopped buying wild-harvested goldenseal after reading the conservation sidebar")
3. **Relatable**: From a buyer persona the target audience identifies with (home grower, herbalism student, practitioner, market seller)

A testimonial fails the standard if it is:
- **Vague**: "Great guide!" "Very informative!" "Loved the detail!" — these are star ratings in disguise, not deployable testimonials
- **Comparative only**: "Better than the other guide I read" — no specifics, no deployment value
- **Overclaiming**: "This guide cured my..." — do not use, legally and ethically. Log in a "Received but Not Deployable" tracker tab.

**What to do with vague positive feedback**: Thank the buyer. Do not feature publicly. Keep it in a "Positive Signals" log — useful for internal confidence, not external social proof. It also confirms the product is being used positively.

---

## Part 9 — Monthly Review Aggregation Checklist

Run this checklist on the first Monday of each month starting August:

**Testimonial health check**:
- [ ] Log all testimonials received since last month's check (email replies, DMs, Etsy reviews, YouTube comments)
- [ ] Count total usable testimonials in library by platform type (buyer / practitioner / contractor)
- [ ] Identify the highest-priority open placeholder to replace (priority: Sequence 1 Email 4 > Practitioner Tier listing > Instagram posts > LinkedIn posts)
- [ ] Confirm all Incentive Tier 2 disclosure text is present wherever incentivized testimonials are placed

**Content rotation**:
- [ ] Update at least one social post testimonial placeholder with a real testimonial if available
- [ ] Add new testimonials to the "Growing Stories" section of the monthly newsletter
- [ ] Check and respond to all Etsy reviews posted in the last 30 days

**Q-target tracking**:
- [ ] Compare to quarterly targets: Q3 (5 total + 1 practitioner), Q4 (10 total + 3 practitioner)
- [ ] If below target: activate Template B passive collection (Instagram Stories / YouTube) for the current month
- [ ] If still below target after Template B: activate Incentive Tier 2 for the next direct outreach wave

---

## Implementation Checklist — Launch Day (June 29)

- [ ] Testimonial Tracker file created at `/projects/seedwarden/data/testimonial-tracker.csv` (or Google Sheets equivalent)
- [ ] Template A automation set up in Kit: trigger `womens-health-purchased`, Day 7 send, reply goes to personal email inbox
- [ ] Template C calendar reminder set: Day 14 after each Practitioner Tier purchase (manual send, not automated)
- [ ] Etsy review monitoring calendar entry: every Monday, check all active listings

**July 13 (first testimonial request sends — Women's Health buyers)**:
- [ ] Template A sends automatically — confirm Kit automation is running
- [ ] Check Etsy reviews for Women's Health; log any usable reviews

**July 28 (Phase 1 close — 30 days post-launch)**:
- [ ] Count usable testimonials: target is 5 minimum
- [ ] If below 3: activate Incentive Tier 2 for next outreach wave; extend collection window to August 7
- [ ] Update highest-priority social post placeholder with real testimonial if available

**August 4 (Phase 2 begins)**:
- [ ] Monthly newsletter "Growing Stories" section template finalized
- [ ] Template B (Instagram/YouTube passive collection) scheduled for first Monday of each month
- [ ] Q3 testimonial target check: on track for 5 total + 1 practitioner by September 30?

**Ongoing (monthly)**:
- [ ] Run Monthly Review Aggregation Checklist (Part 9 above)
- [ ] Log all incoming testimonials within 24 hours of receipt
- [ ] Respond to all Etsy reviews within 48 hours
- [ ] Rotate at least one placeholder in email sequences with a real testimonial per quarter
