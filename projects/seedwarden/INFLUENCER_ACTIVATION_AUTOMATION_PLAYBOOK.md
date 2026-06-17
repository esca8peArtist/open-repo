---
title: "Influencer Activation Automation Playbook — Phase 2 Scaling"
prepared: 2026-06-17
status: production-ready
phase: phase-2
activation-date: 2026-06-22
scope: >
  Outreach templating (3-5 base templates with placeholders), response triage automation,
  tier-based follow-up sequences, CRM integration points (Airtable/Notion),
  Discord webhook orchestration.
references:
  - LAUNCH_WEEK_INFLUENCER_OUTREACH.md
  - PHASE_2_SOCIAL_GROWTH_STRATEGY.md
  - PHASE_2_SEASONAL_CONTENT_CALENDAR.md
---

# Influencer Activation Automation Playbook
## Phase 2 High-Volume Scaling — June 22+

**Purpose**: Scale the launch-week influencer system (55-contact manual outreach) into a
repeatable, semi-automated pipeline that supports 150+ contacts per quarter without
proportional time investment. Phase 1 outreach required ~3 hours total for 55 contacts.
Phase 2 target is 15+ new contacts/week at under 20 minutes/week marginal time.

**Architecture summary**: Five personalization-ready base templates cover all four content
cohorts. Auto-triage workflow routes responses to action queues within 2 hours of receipt.
Three-tier follow-up sequences run on Airtable or Notion with calendar reminders. Discord
webhooks surface response notifications in real time without requiring active email monitoring.

---

## Section 1: Base Outreach Templates (5 Templates)

All templates use `[PLACEHOLDER]` syntax for personalization fields. The minimum required
personalization is marked **Required**. Optional fields improve response rate but are not
blocking.

### Template 1 — Forager / Wild Edibles (Primary)

**Use for**: @chaoticforager, @findersfeeders, @wellfedwild, @feral.foraging,
@growingthroughtheweeds, @foraging.witch — and any account whose content is 60%+ wild plant
or mushroom identification.

**Subject line**: `Field guides for your foraging content — honest review offer`

```
Hi [FIRST_NAME],  [Required]

[SPECIFIC_REFERENCE] — that's the kind of content I point people toward when they're  [Required: 1 sentence citing a specific post/video topic]
learning to forage.

I'm the founder of Seedwarden. We make research-backed digital field guides for foragers
and wildcrafters — the kind you'd actually use in the field, not leave on a coffee table.
[GUIDE_OFFER] covers [GUIDE_DETAIL], with identification, dangerous lookalikes,  [Required: match guide to their niche]
harvest windows, and regional notes for North America.

I'd like to send you a free copy to look at honestly. No posting requirement — if you find
it useful for your audience, I can set up a 15% affiliate code ([HANDLE_CODE]) so your
followers get a discount. If it's not the right fit, keep the guide with my thanks.

Would that interest you? I can send a download link immediately.

— [YOUR_NAME]
Seedwarden
seedwarden.etsy.com
```

**Personalization fill-in guide**:

| Placeholder | What to write | Time |
|-------------|--------------|------|
| `[FIRST_NAME]` | Their first name from bio or intro video | 30 sec |
| `[SPECIFIC_REFERENCE]` | "Your video on ramp identification last March" or "Your recent post on stinging nettle prep" — one specific piece | 2 min (view their recent content) |
| `[GUIDE_OFFER]` | "The Wild Edibles Quick Reference" or "the Wild Edibles + Medicinals bundle" — matched to their focus | 30 sec |
| `[GUIDE_DETAIL]` | "18 species with identification, dangerous lookalikes, and harvest windows" | Pre-filled from template |
| `[HANDLE_CODE]` | Their handle in caps + 15, e.g. "CHAOTICFORAGER15" | 30 sec |

**Total personalization time**: 4–5 minutes per contact.

**DM version (Instagram/TikTok, 280 characters)**:
```
Hi [FIRST_NAME] — I make research-backed field guides for foragers (Seedwarden). I'd love
to send you a free copy of the Wild Edibles guide to review honestly — no posting required.
Interested? I'll drop a download link.
```

---

### Template 2 — Homesteader / Seed Saving

**Use for**: @michelles_farmstead, @thetravelingfarmacy, @motherhenshomestead, @tatumyada —
any account whose content is 50%+ garden process, seed saving, or self-sufficient food growing.

**Subject line**: `Seed saving + zone planting guides for your homestead audience`

```
Hi [FIRST_NAME],  [Required]

[SPECIFIC_REFERENCE] — exactly the kind of thing our guides are built around.  [Required]

I'm the founder of Seedwarden. We publish research-backed digital guides for homesteaders —
seed saving, companion planting, zone-specific growing calendars, and preservation. [GUIDE_OFFER]
covers [GUIDE_DETAIL].  [Required: choose the 1-2 guides most relevant to their content]

I'd love to send you a free copy. No posting requirement — review it honestly, and if it
fits your content, I can set up an affiliate code ([HANDLE_CODE]) for your audience.
If it's not the right fit, the guide is yours regardless.

Let me know if you'd like a download link — I can send it immediately.

— [YOUR_NAME]
Seedwarden
seedwarden.etsy.com
```

**Best guide pairings for homesteaders by content type**:
- Seed saving focus → Seed Saving Field Manual + Zone-by-Zone Seed Starting Calendar
- Companion planting focus → Companion Planting Chart + Seed Saving Field Manual
- Preservation focus → Fermented & Preserved Harvest Handbook + Harvest Preservation Field Manual
- Urban/container focus → Container Growing Blueprint Pack + Apartment Growing Complete Guide

---

### Template 3 — Prepper / Survival / Self-Reliance

**Use for**: @buckskin_revolution, @graybeardedgreenberet, @naturvival, @danwowak,
@ravenwildernessschool — any account where preparedness, ancestral skills, or bushcraft is
the primary content angle.

**Subject line**: `Wild foraging + field manuals for your preparedness audience`

```
Hi [FIRST_NAME],  [Required]

[SPECIFIC_REFERENCE] is the kind of practical, no-fluff content that actually prepares  [Required]
people — I try to bring the same discipline to our guides.

I'm the founder of Seedwarden. We produce zone-specific digital field guides covering
wild edibles, survival gardening, hunting and trapping, and meat preservation.
[GUIDE_OFFER] — [GUIDE_DETAIL]. No fluff, field-functional.  [Required]

I'd like to send you [GUIDE_OFFER] to review honestly. Free, no strings. If your audience
finds them useful, I can set up a 15% affiliate code ([HANDLE_CODE]). If not, they're yours
with my thanks.

Interested in a download link?

— [YOUR_NAME]
Seedwarden
seedwarden.etsy.com
```

**Best guide pairings for preppers**:
- Wilderness/bushcraft focus → Wild Edibles Quick Reference + Hunting, Fishing & Trapping Manual
- Food security focus → Survival Garden Regional Plans + Meat/Fish Preservation Manual
- Plant ID focus → Wild Edibles + Medicinal Plants Regional Guide

---

### Template 4 — Permaculture / Sustainable Living

**Use for**: @farmer_nick, @grace.roots.gardening, @kt.burdett, @youcandoitgardening —
accounts where permaculture design, food forest, or sustainable lifestyle is the primary frame.

**Subject line**: `Permaculture + native plant guides for your audience`

```
Hi [FIRST_NAME],  [Required]

[SPECIFIC_REFERENCE] — the integration of [THEIR_APPROACH] with practical growing advice  [Required]
is exactly what's missing in most plant content.

I'm the founder of Seedwarden. We make research-backed digital field guides — native plants,
companion planting, and zone-specific growing resources. [GUIDE_OFFER] covers
[GUIDE_DETAIL], oriented toward the kind of layered, ecology-aware growing that your
audience practices.  [Required]

I'd like to send you a free copy to look at honestly. No posting requirement. If it's the
right fit, I can set up an affiliate code ([HANDLE_CODE]) for your audience.

Would that interest you?

— [YOUR_NAME]
Seedwarden
seedwarden.etsy.com
```

**Best guide pairings for permaculture**:
- Food forest focus → Native Plants Regional Guide + Companion Planting Chart
- Design focus → Companion Planting Chart + Zone-by-Zone Seed Starting Calendar
- Medicinal layer → Medicinal Plants Regional Guide + Wild Edibles Quick Reference

---

### Template 5 — Large Account / Mid-Tier Modifier

**Use for**: Accounts with 100K+ followers (@epicgardening, @gardeningwithtara, @spicymoustache,
@homegrown_handgathered). Standard templates work but need one additional paragraph that
acknowledges their scale without groveling.

**Add this paragraph after the guide offer paragraph**:
```
I know your following is large, so I want to be direct: I'm sending this as a genuine
review copy, with no posting expectation or timeline. If it resonates with your audience
and you decide to mention it organically, I'd love to set up an affiliate code for them
([HANDLE_CODE]). If it's not the right fit for your content, the guides are yours to keep.
```

**Note on macro accounts**: Response rate for 100K+ accounts is 5–15% vs. 20–35% for
micro accounts (10K–100K). Allocate proportionally — do not spend 20 minutes personalizing
an outreach to a 3M-follower account that will likely not respond.

---

## Section 2: Personalization Efficiency Protocol

### The 4-Minute Rule

Each outreach contact should receive 4 minutes of personalization, not 15. The difference
between a generic email (0 min personalization) and a response-rate-optimized email (4 min)
is 3–4x response rate. Beyond 4 minutes, marginal return drops sharply.

**4-minute allocation**:
- 2 minutes: view their 3 most recent posts/videos; identify one specific, genuine reference
- 1 minute: confirm guide match to their content focus; select the right template and pairings
- 1 minute: fill in all placeholders and draft the custom `[SPECIFIC_REFERENCE]` sentence

**Kill criteria for personalization**: If you cannot find a specific post to reference after
3 minutes of scrolling, default to their pinned post or "most viewed" content. Do not send
an empty `[SPECIFIC_REFERENCE]` — it signals template use and tanks response rate.

### Template + Personalization Batch Workflow

For a batch of 10 contacts in one sitting:

1. Open a spreadsheet with 10 rows (handle, platform, tier, template, guide offer, specific reference note)
2. Spend 20 minutes filling all 10 rows — 2 min/contact for the research
3. Draft all 10 emails from the completed spreadsheet — 2 min/email for fill-in
4. Send or stage for sending: 1 min/email

**Total for 10 contacts**: ~50 minutes. Target: under 60 minutes per 10-contact batch.

---

## Section 3: Response Triage Workflow

### Response Classification (2-Minute Decision)

Every response falls into one of four categories. Classify within 2 hours of receipt.

| Category | Signal | Action | Time to Act |
|----------|--------|--------|-------------|
| HOT | Positive reply, expresses interest in guides, asks for link | Send guide access immediately; assign affiliate code; log in CRM | Within 2 hours |
| WARM | Polite interest, asks a question or wants more info | Answer question; send guide access; follow up in 5 days | Within 4 hours |
| COLD | Polite decline or non-response after first follow-up | Log as No; no further contact for 90 days | No action needed |
| SPAM/WRONG | Clearly wrong audience, spam reply | Delete and unsubscribe from sequence | Immediate |

### HOT Response Workflow

1. Reply within 2 hours with guide access link (Google Drive shared link or Kit download URL)
2. Assign unique affiliate code: `[HANDLE_IN_CAPS][15 or 20]` — e.g., CHAOTICFORAGER15
3. Send affiliate code setup email (see Template Addendum A below)
4. Log in Airtable/Notion CRM: Status → "Guides Sent," Date, Guide(s) sent, Code assigned
5. Set a 10-day reminder: "Did [Name] post about Seedwarden?"
6. Set a 30-day reminder: "Has [Name]'s affiliate code generated any sales?"

### WARM Response Workflow

1. Answer their question directly — do not pitch again
2. Send guide access link alongside the answer
3. Set a 5-day follow-up reminder: "Send check-in message"
4. If they post within 5 days: thank them publicly (comment), share the post in Stories
5. If no post in 10 days: send one low-pressure check-in (see Follow-Up Sequence B)

### Auto-Reply Template for Acknowledgment (Immediate, sent within minutes of response receipt)

**For HOT or WARM responses** — set up as a canned response in Gmail or Fastmail:

```
Hi [FIRST_NAME],

Thanks for getting back to me. Your guide access link is below — no sign-up required,
just click to download:

[GUIDE_DOWNLOAD_LINK]

If you decide to share it with your audience, here's your affiliate code for 15% off:
[HANDLE_CODE]

Any questions, just reply here.

— [YOUR_NAME]
```

**Setup**: In Gmail, save as a template ("Seedwarden Guide Access — Auto Response"). Use
Gmail's canned response feature (not a separate tool) to send within 60 seconds of reading
a HOT/WARM reply.

---

## Section 4: Tier-Based Follow-Up Sequences

### Tier 1 (10K–100K followers, primary outreach targets)

Tier 1 accounts are the highest-value, highest-probability contacts. They receive the
most complete follow-up sequence.

**Sequence T1**:
- **Day 0**: Initial outreach sent (Template 1–4)
- **Day 5**: If no response — one DM follow-up (see T1-FU1 below)
- **Day 12**: If still no response — final "leaving this open" email (see T1-FU2)
- **Day 90**: Re-contact window opens (seasonal angle; different guide offer if season has changed)

**T1-FU1 — Day 5 DM (Instagram or TikTok, 200 characters)**:
```
Hi [FIRST_NAME] — sent you an email about Seedwarden guides earlier this week. In case
it landed in spam: I'd love to send you a free copy of [GUIDE_NAME] to review. No
posting required. Still interested?
```

**T1-FU2 — Day 12 email (final)**:
```
Subject: Leaving this open for you, [FIRST_NAME]

Hi [FIRST_NAME],

Sent you a note last week about a free copy of [GUIDE_NAME] — just wanted to circle
back once more in case the timing wasn't right.

If you'd ever like to take a look, my offer stands: free copy, no strings, affiliate
code available if your audience finds it useful.

No need to reply if it's not a fit — and thanks for the content you put out.

— [YOUR_NAME]
Seedwarden
```

**Cadence note**: Two follow-ups maximum for Tier 1. Any more is spam. If no response after
Day 12, status → "No Response" in CRM. Re-contact at Day 90 with a genuinely different angle
(new product, seasonal news, or referencing a specific recent post of theirs).

---

### Tier 2 (100K+ followers, permaculture/sustainable living, lower probability)

Tier 2 response rate is 5–15%. Do not invest equivalent follow-up depth.

**Sequence T2**:
- **Day 0**: Initial outreach sent (Template + large-account modifier)
- **Day 7**: If no response — one email follow-up only (no DM, does not want to feel hounded)
- **Day 90**: Re-contact only if there is new product news that is genuinely relevant

**T2-FU1 — Day 7 email only**:
```
Subject: Quick follow-up — Seedwarden guides

Hi [FIRST_NAME],

Wanted to circle back once on the guide offer I sent last week. Still happy to send
a free copy of [GUIDE_NAME] if the timing works better now.

No pressure — and I'll leave it there either way.

— [YOUR_NAME]
Seedwarden
```

---

### Tier 3 (Confirmed Partners — Post-Activation)

Tier 3 is a separate track for influencers who have already received guides and
posted content. These are warm relationships requiring a different cadence.

**Sequence T3 — Active Partner Maintenance**:
- **Monthly**: Send a brief note about what's new (new product, seasonal content angle, bundle update). 3–5 sentences. No ask.
- **Quarterly**: Offer a commission rate upgrade if their code has generated 5+ sales. Move from 15% to 20%.
- **Seasonal**: Send preview access to a new guide before it launches publicly. Creates exclusivity, encourages organic early posting.
- **Annually**: Thank-you note at year-end (or at their follower milestone). No ask. Relationship maintenance.

**T3-Monthly update template**:
```
Subject: [Month] update from Seedwarden — thought you'd want to know

Hi [FIRST_NAME],

Quick update: [ONE LINE: new product / seasonal content angle / something relevant
to their audience]. [Your affiliate code (HANDLE_CODE)] is still active for your
audience if you'd like to use it.

Nothing you need to do — just keeping you in the loop.

— [YOUR_NAME]
```

---

## Section 5: CRM Integration Points

### Airtable Setup (Recommended)

**Base name**: "Seedwarden Influencer CRM"
**Table name**: "Outreach Contacts"

**Required fields**:

| Field | Type | Values / Notes |
|-------|------|----------------|
| Handle | Single line text | @handle as written on platform |
| Platform | Single select | Instagram / TikTok / Instagram+TikTok / Pinterest |
| Tier | Single select | T1 / T2 / T3 (Active Partner) |
| Cohort | Single select | Forager / Homesteader / Prepper / Permaculture / Gift Buyer |
| Template used | Single select | Template 1 / 2 / 3 / 4 / 5 (modifier) |
| Outreach date | Date | Date initial email/DM sent |
| Method | Single select | Email / DM / Both |
| Guide(s) sent | Multi-select | Wild Edibles / Seed Saving / Zone Card / Hunting Manual / [other] |
| Response status | Single select | No Response / Warm / Hot / Posted / Declined / Inactive |
| Follow-up 1 date | Date | Auto-populated 5 days after outreach date (T1) or 7 days (T2) |
| Follow-up 2 date | Date | Auto-populated 12 days after outreach date (T1 only) |
| Affiliate code | Single line text | e.g., CHAOTICFORAGER15 |
| UTM link | URL | Unique tracking link for their audience |
| Sales attributed | Number | Pull from Etsy coupon code report weekly |
| Email sign-ups attributed | Number | Pull from Kit referral report |
| Posted | Checkbox | Checked when they publish Seedwarden content |
| Post URL | URL | Direct link to their post |
| Notes | Long text | Personalization notes, relationship details |

**Airtable Views to create**:
1. "Follow-Up Due Today" — filter: Follow-up 1 date = today OR Follow-up 2 date = today
2. "Hot Leads (send guides)" — filter: Response status = Hot
3. "Active Partners" — filter: Tier = T3; sort by Sales attributed descending
4. "90-Day Re-Contact" — filter: Response status = No Response; Outreach date = 90+ days ago
5. "Weekly Metrics" — group by Week; sum Sales attributed + Email sign-ups

### Notion Setup (Alternative)

If Airtable is not available, replicate the same structure in a Notion database. Notion
database properties map 1:1 with the Airtable fields above. Add a "Follow-Up Queue" filtered
view that shows records where Follow-up date = today or earlier and Status ≠ Posted/Declined.

**Notion automation**: Use Notion's built-in "Create reminder" property automation to trigger
a reminder on the Follow-up 1 date field. This eliminates the need for external calendar
entries per contact.

### Kit Integration Point

Kit (email automation) connects to the influencer CRM at one point: when an influencer's
audience uses their affiliate code, Kit can track the resulting email subscriber (if the
purchase flow leads through the Kit sign-up form). Map this flow:

```
Influencer posts → audience clicks UTM link → Kit landing page (zone card) → subscriber
    → Kit tags subscriber with "affiliate: [HANDLE_CODE]"
    → Pull Kit segment by affiliate tag each week to count sign-ups attributed
```

**Kit tag naming**: `affiliate-[handle]` (lowercase, no @). Example: `affiliate-chaoticforager`.
This allows per-influencer attribution without manual counting.

---

## Section 6: Discord Webhook Orchestration

### Purpose

Discord webhooks surface influencer response notifications in a dedicated channel without
requiring active email monitoring. When an influencer replies to an outreach email, a
notification fires to #influencer-responses in Discord within minutes.

### Setup Method (Gmail + Zapier → Discord)

**Step 1**: Create a dedicated "influencer-responses" channel in the Seedwarden Discord server.

**Step 2**: Create a Discord webhook URL for that channel:
- Discord server settings → Integrations → Webhooks → New Webhook
- Name: "Influencer Replies"
- Channel: #influencer-responses
- Copy the webhook URL

**Step 3**: Create a Zapier automation (free tier supports this):
- Trigger: Gmail — "New Email" in inbox with label "seedwarden-outreach" (label all outreach
  emails you send with this label; replies inherit the label)
- Filter: Email is a reply (not an original send)
- Action: Discord — "Post Message to Webhook"
- Message format:
```
NEW INFLUENCER REPLY
From: {{sender_name}} ({{sender_email}})
Subject: {{email_subject}}
Preview: {{email_body_plain | truncate: 200}}
→ Action needed: triage within 2 hours
```

**Step 4**: Test with a self-sent reply to confirm the webhook fires.

### Alternative: Gmail → Slack (if Discord is not primary tool)

Same Zapier setup, swap the Action from Discord webhook to Slack webhook. The message
format is identical.

### Zero-Automation Alternative (No Zapier)

If Zapier is not available, use Gmail filters:

1. Create a Gmail label "SW — Influencer Reply"
2. Create a filter: if email is from any address in a saved group "Influencer Contacts"
   AND subject contains "Re:" → apply label "SW — Influencer Reply"
3. Set Gmail mobile notifications for this label only (settings → Notifications → selected labels)
4. This gives a push notification within minutes of any influencer reply without Zapier

**Tradeoff**: Manual Gmail filter requires adding each new contact's email to the "Influencer
Contacts" group, which adds ~30 seconds per contact to the outreach workflow.

---

## Section 7: Weekly Influencer Operations Time Budget

Phase 2 influencer operations are designed to stay under 20 minutes/week for ongoing
management once the initial activation batch is complete. The activation batch (first 4 weeks)
requires more time to build the infrastructure and contact the initial pipeline.

### Weeks 1–4 (Activation Phase): 60–90 minutes/week

| Task | Time |
|------|------|
| New outreach batch (10 contacts) | 50 min |
| Follow-up queue (reply to existing contacts due) | 15 min |
| Response triage + guide delivery | 10 min (amortized across days) |
| CRM update | 10 min |
| **Total** | **85 min/week** |

### Weeks 5+ (Steady State): 15–25 minutes/week

| Task | Time |
|------|------|
| New outreach (3–5 contacts, rotating) | 20 min |
| Follow-up queue | 5 min |
| Partner T3 monthly update (1× per month, ~5 min/partner) | 5 min/month amortized to 1.5 min/week |
| CRM update + sales attribution pull | 5 min |
| **Total** | **~30 min/week** |

The steady-state cadence is 3–5 new contacts/week indefinitely, ensuring a continuous
pipeline of fresh influencer relationships without a recurring 50-contact batch.

---

## Template Addendum A: Affiliate Code Confirmation Email

Sent to all HOT/WARM responses when guides are delivered.

```
Subject: Your Seedwarden affiliate code — [HANDLE_CODE]

Hi [FIRST_NAME],

Your guide download link is above (or attached in the previous email).

Here's your affiliate code for your audience: [HANDLE_CODE]

How it works:
- Your audience enters [HANDLE_CODE] at checkout on Etsy
- They get 15% off any Seedwarden guide
- You earn 15% of each sale (paid monthly via PayPal or Venmo)

To track your referrals: I'll send you a monthly summary of sales attributed to your code.
You don't need to sign up for anything.

If you'd like a unique tracking link to share instead of (or in addition to) the code,
let me know and I'll create one.

No obligations on posting or timeline — just here when it's useful.

— [YOUR_NAME]
Seedwarden
```

---

## Template Addendum B: Partner Commission Upgrade (Quarterly, T3 active partners)

Sent to Tier 3 partners whose code has generated 5+ sales in 90 days.

```
Subject: Your Seedwarden commission — upgrade offer

Hi [FIRST_NAME],

Your affiliate code (HANDLE_CODE) has generated [X] sales in the last 90 days —
that's genuinely meaningful for an independent shop, and I wanted to say thank you.

I'd like to increase your commission rate from 15% to 20% going forward. Your code
will work the same way — the new rate applies to any sale from today.

No action needed on your end; I'll update the tracking on my side.

Thank you for helping people find these guides.

— [YOUR_NAME]
Seedwarden
```

---

*Prepared: June 17, 2026. Activate: June 22, 2026.*
*Review triggers: After each 50-contact batch, review response rate. If below 15% on T1
contacts, audit [SPECIFIC_REFERENCE] quality (most likely failure mode) and template-guide
match accuracy.*
